#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import importlib.util
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HASH_ALGORITHM = "sha256"
DEFAULT_CANONICALIZATION_VERSION = "acx-ledger-canonical-v1"
AUTHORITY_MANIFEST_FILENAME = "authority_manifest.json"
AUTHORITY_EVIDENCE_FILENAME = "artifacts/acx/r3_authority_manifest_evidence.json"
ALLOWED_AUTHORITY_CLASSES = (
    "canonical_live",
    "derived_render",
    "doc_support",
    "archived_forbidden",
)
DERIVED_RENDER_PATHS = {
    "BOOT.md",
    "CURRENT_STATE.md",
    "NEXT_ACTION.md",
    "CONTEXT_INDEX.md",
    "ARIS_PHASE_LEDGER.md",
}
ARCHIVED_FORBIDDEN_PREFIXES = ("archive/superseded/",)
AUTHORITY_GENERATORS = {
    "BOOT.md": "scripts/render_boot.py",
}
SCAN_IGNORED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
    ".venv",
    "venv",
    "node_modules",
}
SCAN_IGNORED_SUFFIXES = (
    ".pyc",
    ".pyo",
    ".tmp",
    ".temp",
    ".swp",
    ".swo",
    "~",
)
SCAN_IGNORED_FILES = {
    AUTHORITY_MANIFEST_FILENAME,
    AUTHORITY_EVIDENCE_FILENAME,
    ".DS_Store",
}
SCAN_EXCLUSIONS = {
    AUTHORITY_MANIFEST_FILENAME: "Self-generated advisory output; excluded from scan to avoid manifest recursion.",
    AUTHORITY_EVIDENCE_FILENAME: "Self-generated advisory evidence; excluded from scan to avoid evidence recursion.",
}
MANUAL_WRITE_GUARD_MESSAGE = "ACX_DISABLE_HOOK=1 set; manual-write guard bypassed"
ACX_MODE_ADVISORY = "advisory"
ACX_MODE_HARD = "hard"
TRANSITION_RULES_VERSION = "acx-r5-advisory-v1"
GATE_COMPILER_VERSION = "acx-r6-gate-compiler-v1"
PACKET_MAX_WORDS = 300
ADVISORY_REPORT_PROSE_TOKENS = (
    "PASS",
    "DONE",
    "CONCLUÍDO",
    "CONCLUIDO",
    "APROVADO",
    "APPROVED",
    "READY",
)
ADVISORY_TRANSITION_RULES = {
    "transition_rules_version": TRANSITION_RULES_VERSION,
    "transitions": {
        "ACX-R4": {
            "ACX-R5": {
                "required_mode": ACX_MODE_ADVISORY,
                "require_clean_git_status": True,
                "require_empty_files_changed": True,
                "require_artifact_hashes": True,
            }
        }
    },
}
FORBIDDEN_DECISION_VOCABULARY = (
    "PASS",
    "DONE",
    "CONCLUÍDO",
    "CONCLUIDO",
    "APROVADO",
    "APPROVED",
    "AUTORIZADO",
    "AUTHORIZED",
    "PRONTO",
    "READY",
)


class LedgerError(RuntimeError):
    pass


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        check=False,
    )


def _git_stdout(root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "git command failed"
        raise LedgerError(message)
    return result.stdout


def _normalize_repo_relative_path(path_value: str, *, root: Path) -> str:
    path = Path(path_value)
    if path.is_absolute():
        try:
            return path.resolve().relative_to(root).as_posix()
        except ValueError as exc:
            raise LedgerError(f"path is outside repo root: {path_value!r}") from exc
    return path.as_posix()


def _git_cached_name_only(root: Path) -> list[str]:
    output = _git_stdout(root, ["diff", "--cached", "--name-only"])
    return [line.strip() for line in output.splitlines() if line.strip()]


def _git_index_bytes(root: Path, relative_path: str) -> bytes:
    result = _run_git(root, ["show", f":{relative_path}"])
    if result.returncode != 0:
        message = (
            result.stderr.decode("utf-8", errors="replace").strip()
            or result.stdout.decode("utf-8", errors="replace").strip()
            or f"unable to read staged path: {relative_path}"
        )
        raise LedgerError(message)
    return result.stdout


def _ledger_entries_from_text(text: str) -> list[tuple[int, dict[str, Any]]]:
    entries: list[tuple[int, dict[str, Any]]] = []
    for lineno, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise LedgerError(f"line {lineno}: invalid JSON: {exc.msg}") from exc
        if not isinstance(event, dict):
            raise LedgerError(f"line {lineno}: event must be a JSON object")
        entries.append((lineno, event))
    return entries


def _path_bytes_reader_from_root(root: Path):
    def _reader(path_value: str) -> bytes:
        return _read_bytes(_resolve_relative_path(path_value, relative_to=root))

    return _reader


def _path_bytes_reader_from_index(root: Path):
    def _reader(path_value: str) -> bytes:
        relative_path = _normalize_repo_relative_path(path_value, root=root)
        return _git_index_bytes(root, relative_path)

    return _reader


def _read_path_bytes(
    path_value: str,
    *,
    root: Path = ROOT,
    path_reader: Any = None,
) -> bytes:
    if path_reader is not None:
        return path_reader(path_value)
    return _read_bytes(_resolve_relative_path(path_value, relative_to=root))


def _normalize_root(root: Path | None) -> Path:
    return root.resolve() if root is not None else ROOT


def _relative_posix(path: Path, *, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _should_ignore_scanned_path(path_value: str) -> bool:
    if path_value in SCAN_IGNORED_FILES:
        return True
    if path_value.startswith(".git/"):
        return True
    if path_value.startswith("authority_manifest.json"):
        return True
    if path_value.startswith(AUTHORITY_EVIDENCE_FILENAME):
        return True
    return any(path_value.endswith(suffix) for suffix in SCAN_IGNORED_SUFFIXES)


def _walk_repo_files(root: Path) -> list[str]:
    discovered: list[str] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            dirname for dirname in dirnames if dirname not in SCAN_IGNORED_DIRS and dirname != ".git"
        )
        filenames = sorted(filenames)
        current_path = Path(current_root)
        for filename in filenames:
            rel_path = (current_path / filename).relative_to(root).as_posix()
            if _should_ignore_scanned_path(rel_path):
                continue
            discovered.append(rel_path)
    return sorted(discovered)


def _discover_repo_files(root: Path) -> list[str]:
    root = _normalize_root(root)
    if not root.exists():
        return []
    return _walk_repo_files(root)


def _classify_authority_path(path_value: str) -> tuple[str, str, str]:
    if any(path_value.startswith(prefix) for prefix in ARCHIVED_FORBIDDEN_PREFIXES):
        return (
            "archived_forbidden",
            "Superseded archive quarantine is historical and live-code forbidden.",
            "path_prefix:archive/superseded/",
        )
    if path_value in {
        "ACTIVE_CONTEXT_STATE.json",
        "ACTIVE_CONTEXT_SCHEMA.json",
        ".acx/ledger.jsonl",
        "tools/acx.py",
        "tools/acx_validate.py",
        "scripts/render_boot.py",
        "scripts/check_boot_sync.py",
        "ARIS_BOOT.md",
        "ROADMAP_CANONICAL.md",
    }:
        if path_value.endswith(".json") or path_value.endswith(".py") or path_value in {
            "ARIS_BOOT.md",
            "ROADMAP_CANONICAL.md",
        }:
            reason = "Live authority source or implementation used directly by active-context governance."
        else:
            reason = "Live authority source used directly by active-context governance."
        return (
            "canonical_live",
            reason,
            f"path_exact:{path_value}",
        )
    if path_value.startswith("docs/acx/") and path_value.endswith(".md"):
        return (
            "canonical_live",
            "Active-context specification document that defines live governance contracts.",
            "path_prefix:docs/acx/",
        )
    if path_value in DERIVED_RENDER_PATHS:
        if path_value == "BOOT.md":
            reason = "Derived boot render generated from live state and roadmap data."
            source_rule = "render_generator:scripts/render_boot.py"
        else:
            reason = "Derived mirror/render that reflects live state but is not authoritative."
            source_rule = "mirror_marker:derived_render"
        return ("derived_render", reason, source_rule)
    if path_value.startswith("archive/derived_mirrors/"):
        return (
            "doc_support",
            "Historical mirror support material retained for audit context.",
            "path_prefix:archive/derived_mirrors/",
        )
    if path_value.startswith("archive/"):
        return (
            "doc_support",
            "Archived supporting material retained for audit context.",
            "path_prefix:archive/",
        )
    if path_value.startswith("artifacts/"):
        return (
            "doc_support",
            "Evidence artifact or support output, not a live source of authority.",
            "path_prefix:artifacts/",
        )
    if path_value.startswith("project_mirror/"):
        return (
            "doc_support",
            "Project mirror support material, not the live active-context source of truth.",
            "path_prefix:project_mirror/",
        )
    if path_value.startswith("tests/"):
        return (
            "doc_support",
            "Test or fixture support material.",
            "path_prefix:tests/",
        )
    if path_value == "README.md":
        return (
            "doc_support",
            "Repository overview and operator guidance.",
            "path_exact:README.md",
        )
    if path_value == "DECISION_LOCKS.md" or path_value == "LAB_OPERATING_CONTRACT.md":
        return (
            "doc_support",
            "Governance support document referenced by live validation.",
            f"path_exact:{path_value}",
        )
    if path_value.endswith(".md"):
        return (
            "doc_support",
            "Markdown support document.",
            "fallback:markdown_doc_support",
        )
    return (
        "doc_support",
        "Default support artifact or implementation file.",
        "fallback:doc_support_default",
    )


def _build_authority_manifest(root: Path) -> dict[str, Any]:
    root = _normalize_root(root)
    entries: dict[str, dict[str, str]] = {}
    classes: dict[str, list[str]] = {key: [] for key in ALLOWED_AUTHORITY_CLASSES}
    for rel_path in _discover_repo_files(root):
        authority_class, reason, source_rule = _classify_authority_path(rel_path)
        entries[rel_path] = {
            "class": authority_class,
            "reason": reason,
            "source_rule": source_rule,
        }
        classes[authority_class].append(rel_path)

    for key in classes:
        classes[key].sort()

    scan_exclusions = [
        {"path": path, "reason": reason, "scope": "repo-self-reference-advisory"}
        for path, reason in sorted(SCAN_EXCLUSIONS.items())
    ]

    return {
        "manifest_version": "1",
        "mode": "advisory",
        "generated_by": "tools/acx.py authority manifest",
        "source_of_truth_note": (
            "ACTIVE_CONTEXT_STATE.json remains live canonical source; this manifest is advisory "
            "classification metadata."
        ),
        "scan_exclusions": scan_exclusions,
        "classes": classes,
        "entries": dict(sorted(entries.items())),
    }


def _load_authority_manifest(manifest_path: Path) -> dict[str, Any]:
    payload = _load_json(manifest_path)
    if not isinstance(payload, dict):
        raise LedgerError("manifest must be a JSON object")
    return payload


def _render_boot_module(root: Path):
    module_path = ROOT / "scripts" / "render_boot.py"
    spec = importlib.util.spec_from_file_location("_acx_render_boot", module_path)
    if spec is None or spec.loader is None:
        raise LedgerError("unable to load scripts/render_boot.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.STATE_PATH = root / "ACTIVE_CONTEXT_STATE.json"
    module.ROADMAP_PATH = root / "ROADMAP_CANONICAL.md"
    module.BOOT_PATH = root / "BOOT.md"
    module.MODEL_REASONING_POLICY_PATH = root / "MODEL_REASONING_POLICY.md"
    return module


def _normalize_render_bytes(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def _render_boot_for_root(root: Path) -> bytes:
    module = _render_boot_module(root)
    rendered = module.render_boot_text()
    if not isinstance(rendered, str):
        raise LedgerError("render_boot_text must return a string")
    return rendered.encode("utf-8")


def _compare_rendered_file(root: Path, rel_path: str) -> tuple[bool, str]:
    generator = AUTHORITY_GENERATORS.get(rel_path)
    if generator is None:
        return True, "render_generator_missing"

    target = root / rel_path
    generated = _render_boot_for_root(root) if rel_path == "BOOT.md" else b""
    if not target.exists():
        return False, f"{rel_path} missing on disk"
    committed = _normalize_render_bytes(target.read_bytes())
    generated = _normalize_render_bytes(generated)
    if committed != generated:
        return False, f"{rel_path} drift detected against {generator}"
    return True, "render_ok"


def _validate_authority_manifest_payload(manifest: dict[str, Any]) -> None:
    if manifest.get("manifest_version") != "1":
        raise LedgerError("manifest_version must be '1'")
    if manifest.get("mode") != "advisory":
        raise LedgerError("mode must be 'advisory'")
    if manifest.get("generated_by") != "tools/acx.py authority manifest":
        raise LedgerError("generated_by must be 'tools/acx.py authority manifest'")
    if "classes" not in manifest or "entries" not in manifest:
        raise LedgerError("manifest missing required sections")
    if "scan_exclusions" not in manifest:
        raise LedgerError("manifest missing scan_exclusions section")


def _authority_check_manifest(manifest: dict[str, Any], *, root: Path) -> None:
    _validate_authority_manifest_payload(manifest)
    classes = manifest.get("classes")
    entries = manifest.get("entries")
    scan_exclusions = manifest.get("scan_exclusions")
    if not isinstance(classes, dict) or not isinstance(entries, dict):
        raise LedgerError("manifest classes and entries must be JSON objects")
    if not isinstance(scan_exclusions, list):
        raise LedgerError("manifest scan_exclusions must be a list")
    for class_name in ALLOWED_AUTHORITY_CLASSES:
        if class_name not in classes:
            raise LedgerError(f"manifest missing class bucket: {class_name}")
        if not isinstance(classes[class_name], list):
            raise LedgerError(f"manifest class bucket must be a list: {class_name}")

    expected_scan_exclusions = [
        {"path": path, "reason": reason, "scope": "repo-self-reference-advisory"}
        for path, reason in sorted(SCAN_EXCLUSIONS.items())
    ]
    if scan_exclusions != expected_scan_exclusions:
        raise LedgerError("manifest scan_exclusions do not match advisory self-scan policy")

    discovered = _discover_repo_files(root)
    discovered_set = set(discovered)
    entry_set = set(entries)

    missing_entries = [path for path in discovered if path not in entry_set]
    if missing_entries:
        raise LedgerError(f"manifest missing entry for file: {missing_entries[0]}")

    extra_entries = sorted(entry_set - discovered_set)
    if extra_entries:
        raise LedgerError(f"manifest entry points to missing file: {extra_entries[0]}")

    for path_value, payload in sorted(entries.items()):
        if not isinstance(payload, dict):
            raise LedgerError(f"manifest entry must be a JSON object: {path_value}")
        class_name = payload.get("class")
        if class_name is None:
            raise LedgerError(f"manifest entry missing class: {path_value}")
        if class_name not in ALLOWED_AUTHORITY_CLASSES:
            raise LedgerError(f"manifest entry has invalid class {class_name!r}: {path_value}")
        if path_value not in classes.get(class_name, []):
            raise LedgerError(f"manifest class bucket mismatch for {path_value}")

    for class_name, bucket in classes.items():
        if sorted(bucket) != sorted(
            path_value for path_value, payload in entries.items() if payload.get("class") == class_name
        ):
            raise LedgerError(f"manifest class bucket out of sync: {class_name}")


def authority_manifest(root: Path, out_path: Path) -> None:
    manifest = _build_authority_manifest(root)
    _write_text(out_path, json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n")


def authority_check(root: Path, manifest_path: Path) -> None:
    manifest = _load_authority_manifest(manifest_path)
    _authority_check_manifest(manifest, root=root)


def render_check(root: Path, manifest_path: Path) -> None:
    manifest = _load_authority_manifest(manifest_path)
    _authority_check_manifest(manifest, root=root)
    entries = manifest.get("entries", {})
    missing_generators: list[str] = []
    drifted: list[str] = []

    for rel_path, payload in sorted(entries.items()):
        if not isinstance(payload, dict):
            continue
        if payload.get("class") != "derived_render":
            continue
        if rel_path not in AUTHORITY_GENERATORS:
            missing_generators.append(rel_path)
            continue
        ok, message = _compare_rendered_file(root, rel_path)
        if not ok:
            drifted.append(message)

    if missing_generators:
        print("render_generator_missing:", ", ".join(missing_generators))
    if drifted:
        raise LedgerError("; ".join(drifted))


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def _event_hash(event: dict[str, Any]) -> str:
    material = dict(event)
    material.pop("event_sha256", None)
    return hashlib.sha256(_canonical_json_bytes(material)).hexdigest()


def _state_hash_from_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _resolve_relative_path(path_value: str, *, relative_to: Path = ROOT) -> Path:
    candidate = Path(path_value)
    return candidate if candidate.is_absolute() else (relative_to / candidate).resolve()


def _load_ledger(ledger_path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not ledger_path.exists():
        return []
    return _ledger_entries_from_text(ledger_path.read_text(encoding="utf-8"))


def _ensure_field(
    event: dict[str, Any],
    name: str,
    value: Any,
    *,
    conflict_label: str | None = None,
) -> None:
    if name not in event or event[name] is None:
        event[name] = value
        return
    if event[name] != value:
        label = conflict_label or name
        raise LedgerError(f"{label} conflict: expected {value!r}, got {event[name]!r}")


def _normalize_event_for_append(
    event: dict[str, Any],
    previous_hash: str | None,
    *,
    root: Path = ROOT,
) -> dict[str, Any]:
    normalized = dict(event)
    normalized.setdefault("hash_algorithm", DEFAULT_HASH_ALGORITHM)
    normalized.setdefault("canonicalization_version", DEFAULT_CANONICALIZATION_VERSION)

    if normalized["hash_algorithm"] != DEFAULT_HASH_ALGORITHM:
        raise LedgerError(
            f"hash_algorithm must be {DEFAULT_HASH_ALGORITHM!r}, got {normalized['hash_algorithm']!r}"
        )
    if normalized["canonicalization_version"] != DEFAULT_CANONICALIZATION_VERSION:
        raise LedgerError(
            "canonicalization_version must be "
            f"{DEFAULT_CANONICALIZATION_VERSION!r}, got {normalized['canonicalization_version']!r}"
        )

    _ensure_field(normalized, "prev_sha256", previous_hash)
    _ensure_field(normalized, "ledger_head_hash", previous_hash)

    payload = normalized.get("payload")
    if normalized.get("event_type") == "genesis":
        if not isinstance(payload, dict):
            raise LedgerError("genesis payload must be a JSON object")
        baseline_path = payload.get("baseline_state_path")
        if baseline_path is None:
            raise LedgerError("genesis payload missing baseline_state_path")
        if not isinstance(baseline_path, str):
            raise LedgerError("genesis payload baseline_state_path must be a string")
        resolved = _resolve_relative_path(baseline_path, relative_to=root)
        state_bytes = _read_bytes(resolved)
        state_hash = _state_hash_from_bytes(state_bytes)
        _ensure_field(normalized, "state_blob_hash", state_hash)
    else:
        if "state_blob_hash" not in normalized:
            normalized["state_blob_hash"] = None

    computed_hash = _event_hash(normalized)
    _ensure_field(normalized, "event_sha256", computed_hash, conflict_label="event_sha256")
    return normalized


def _validate_event_record(
    event: dict[str, Any],
    *,
    line_no: int,
    previous_hash: str | None,
    check_baseline: bool,
    root: Path = ROOT,
    path_reader: Any = None,
) -> str:
    if event.get("hash_algorithm") != DEFAULT_HASH_ALGORITHM:
        raise LedgerError(
            f"line {line_no}: hash_algorithm must be {DEFAULT_HASH_ALGORITHM!r}"
        )
    if event.get("canonicalization_version") != DEFAULT_CANONICALIZATION_VERSION:
        raise LedgerError(
            f"line {line_no}: canonicalization_version must be {DEFAULT_CANONICALIZATION_VERSION!r}"
        )

    if event.get("prev_sha256") != previous_hash:
        raise LedgerError(
            f"line {line_no}: prev_sha256 mismatch: expected {previous_hash!r}, "
            f"got {event.get('prev_sha256')!r}"
        )
    if event.get("ledger_head_hash") != previous_hash:
        raise LedgerError(
            f"line {line_no}: ledger_head_hash mismatch: expected {previous_hash!r}, "
            f"got {event.get('ledger_head_hash')!r}"
        )

    computed_hash = _event_hash(event)
    if event.get("event_sha256") != computed_hash:
        raise LedgerError(
            f"line {line_no}: event_sha256 mismatch: expected {computed_hash!r}, "
            f"got {event.get('event_sha256')!r}"
        )

    if check_baseline and event.get("event_type") == "genesis":
        payload = event.get("payload")
        if not isinstance(payload, dict):
            raise LedgerError(f"line {line_no}: genesis payload must be a JSON object")
        baseline_path = payload.get("baseline_state_path")
        if not isinstance(baseline_path, str):
            raise LedgerError(
                f"line {line_no}: genesis payload baseline_state_path must be a string"
            )
        state_hash = _state_hash_from_bytes(
            _read_path_bytes(baseline_path, root=root, path_reader=path_reader)
        )
        if event.get("state_blob_hash") != state_hash:
            raise LedgerError(
                f"line {line_no}: state_blob_hash mismatch: expected {state_hash!r}, "
                f"got {event.get('state_blob_hash')!r}"
            )

    return computed_hash


def append_event(event_path: Path, ledger_path: Path, *, root: Path = ROOT) -> None:
    event = _load_json(event_path)
    if not isinstance(event, dict):
        raise LedgerError("event input must be a JSON object")

    entries = _load_ledger(ledger_path)
    previous_hash = entries[-1][1]["event_sha256"] if entries else None
    normalized = _normalize_event_for_append(event, previous_hash, root=root)

    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    with ledger_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
        handle.write("\n")


def verify_chain(ledger_path: Path, *, root: Path = ROOT) -> None:
    entries = _load_ledger(ledger_path)
    _verify_ledger_entries(entries, root=root, path_reader=_path_bytes_reader_from_root(root))


def _verify_ledger_entries(
    entries: list[tuple[int, dict[str, Any]]],
    *,
    root: Path = ROOT,
    path_reader: Any = None,
) -> None:
    previous_hash = None
    for line_no, event in entries:
        previous_hash = _validate_event_record(
            event,
            line_no=line_no,
            previous_hash=previous_hash,
            check_baseline=True,
            root=root,
            path_reader=path_reader,
        )


def _fold_genesis_state(
    event: dict[str, Any],
    *,
    root: Path = ROOT,
    path_reader: Any = None,
) -> bytes:
    payload = event.get("payload")
    if not isinstance(payload, dict):
        raise LedgerError("genesis payload must be a JSON object")

    baseline_path = payload.get("baseline_state_path")
    if isinstance(baseline_path, str):
        state_bytes = _read_path_bytes(baseline_path, root=root, path_reader=path_reader)
        expected_hash = event.get("state_blob_hash")
        if expected_hash is not None and _state_hash_from_bytes(state_bytes) != expected_hash:
            raise LedgerError(
                "genesis baseline state hash mismatch: "
                f"expected {expected_hash!r}"
            )
        return state_bytes

    baseline_state = payload.get("baseline_state")
    if baseline_state is not None:
        return json.dumps(
            baseline_state,
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        ).encode("utf-8") + b"\n"

    raise LedgerError("genesis payload missing baseline_state_path or baseline_state")


def _fold_ledger_entries(
    entries: list[tuple[int, dict[str, Any]]],
    *,
    root: Path = ROOT,
    path_reader: Any = None,
) -> bytes:
    if not entries:
        raise LedgerError("ledger is empty")

    previous_hash = None
    folded_state: bytes | None = None
    for line_no, event in entries:
        previous_hash = _validate_event_record(
            event,
            line_no=line_no,
            previous_hash=previous_hash,
            check_baseline=True,
            root=root,
            path_reader=path_reader,
        )
        event_type = event.get("event_type")
        if event_type == "genesis":
            folded_state = _fold_genesis_state(event, root=root, path_reader=path_reader)
        elif event_type == "violation_advisory":
            continue
        else:
            raise LedgerError(
                f"line {line_no}: unsupported state-mutating event type {event_type!r}"
            )

    if folded_state is None:
        raise LedgerError("ledger does not contain a genesis event")

    return folded_state


def fold(ledger_path: Path, out_path: Path, *, root: Path = ROOT) -> None:
    entries = _load_ledger(ledger_path)
    _write_bytes(out_path, _fold_ledger_entries(entries, root=root, path_reader=_path_bytes_reader_from_root(root)))


def guard_manual_write(manifest_path: Path, ledger_path: Path, state_path: Path, *, root: Path = ROOT) -> None:
    if os.environ.get("ACX_DISABLE_HOOK") == "1":
        print(MANUAL_WRITE_GUARD_MESSAGE)
        return

    staged_paths = set(_git_cached_name_only(root))
    state_rel = _normalize_repo_relative_path(str(state_path), root=root)
    if state_rel not in staged_paths:
        return

    manifest = _load_authority_manifest(manifest_path)
    _validate_authority_manifest_payload(manifest)

    ledger_rel = _normalize_repo_relative_path(str(ledger_path), root=root)
    staged_state = _git_index_bytes(root, state_rel)
    staged_ledger_text = _git_index_bytes(root, ledger_rel).decode("utf-8")
    entries = _ledger_entries_from_text(staged_ledger_text)
    staged_reader = _path_bytes_reader_from_index(root)

    try:
        folded_state = _fold_ledger_entries(entries, root=root, path_reader=staged_reader)
    except LedgerError as exc:
        raise LedgerError(f"manual write block: {exc}") from exc
    if folded_state != staged_state:
        folded_sha = hashlib.sha256(folded_state).hexdigest()
        staged_sha = hashlib.sha256(staged_state).hexdigest()
        raise LedgerError(
            "manual write block: staged ACTIVE_CONTEXT_STATE.json does not match staged ledger fold "
            f"(state_sha={staged_sha}, folded_sha={folded_sha})"
        )


def current_acx_mode() -> str:
    return os.environ.get("ACX_MODE", ACX_MODE_ADVISORY)


def hard_mode_enabled() -> bool:
    return current_acx_mode() == ACX_MODE_HARD


def _validate_sha256_hex(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def validate_transition_artifacts(artifacts: Any, *, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(artifacts, list):
        return ["artifacts must be a list"]
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            errors.append(f"artifacts[{index}] must be a JSON object")
            continue
        path_value = artifact.get("path")
        sha256_value = artifact.get("sha256")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"artifacts[{index}].path must be a non-empty string")
            continue
        if not _validate_sha256_hex(sha256_value):
            errors.append(f"artifacts[{index}].sha256 must be a sha256 hex digest")
            continue
        resolved = _resolve_relative_path(path_value, relative_to=root)
        if not resolved.exists():
            errors.append(f"artifacts[{index}].path missing on disk: {path_value}")
            continue
        actual_sha256 = hashlib.sha256(resolved.read_bytes()).hexdigest()
        if actual_sha256 != sha256_value:
            errors.append(
                f"artifacts[{index}].sha256 mismatch for {path_value}: expected {actual_sha256!r}, got {sha256_value!r}"
            )
    return errors


def validate_transition_evidence_bundle(
    bundle: Any,
    *,
    current_head: str | None = None,
    root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(bundle, dict):
        return ["evidence bundle must be a JSON object"]

    required_fields = [
        "phase_id",
        "from_phase",
        "to_phase",
        "mode",
        "head_before",
        "head_after",
        "git_status_before",
        "git_status_after",
        "files_read",
        "files_changed",
        "commands",
        "artifacts",
        "rollback_plan",
        "limitations",
        "transition_rules_version",
    ]
    for field in required_fields:
        if field not in bundle:
            errors.append(f"missing required field: {field}")

    if bundle.get("mode") != ACX_MODE_ADVISORY:
        errors.append("mode must be 'advisory'")
    if bundle.get("transition_rules_version") != TRANSITION_RULES_VERSION:
        errors.append(
            "transition_rules_version must be "
            f"{TRANSITION_RULES_VERSION!r}"
        )

    for field in ("phase_id", "from_phase", "to_phase", "head_before", "head_after", "rollback_plan"):
        value = bundle.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    for field in ("git_status_before", "git_status_after"):
        value = bundle.get(field)
        if not isinstance(value, str):
            errors.append(f"{field} must be a string")

    for field in ("files_read", "files_changed", "commands", "limitations"):
        value = bundle.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be a list")
            continue
        if any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{field} must contain only non-empty strings")

    artifacts = bundle.get("artifacts")
    errors.extend(validate_transition_artifacts(artifacts, root=root))

    if current_head is not None and bundle.get("head_before") != current_head:
        errors.append(
            "stale bundle: head_before does not match current HEAD"
        )

    files_changed = bundle.get("files_changed")
    if isinstance(files_changed, list) and not files_changed:
        if bundle.get("git_status_before") != "" or bundle.get("git_status_after") != "":
            errors.append("read-only evidence must have empty git_status_before and git_status_after")
        if bundle.get("head_before") != bundle.get("head_after"):
            errors.append("read-only evidence must keep head_before equal to head_after")

    return errors


def _get_transition_rule(rules: dict[str, Any], from_phase: str, to_phase: str) -> dict[str, Any] | None:
    transitions = rules.get("transitions")
    if not isinstance(transitions, dict):
        return None
    from_rules = transitions.get(from_phase)
    if not isinstance(from_rules, dict):
        return None
    rule = from_rules.get(to_phase)
    if not isinstance(rule, dict):
        return None
    return rule


def can_transition(
    from_phase: str,
    to_phase: str,
    evidence: Any,
    rules: dict[str, Any],
    *,
    current_head: str | None = None,
    root: Path = ROOT,
) -> bool:
    if not isinstance(rules, dict):
        return False
    if rules.get("transition_rules_version") != TRANSITION_RULES_VERSION:
        return False
    rule = _get_transition_rule(rules, from_phase, to_phase)
    if rule is None:
        return False
    if not isinstance(evidence, dict):
        return False
    if evidence.get("from_phase") != from_phase or evidence.get("to_phase") != to_phase:
        return False
    if evidence.get("mode") != ACX_MODE_ADVISORY:
        return False
    effective_current_head = current_head if current_head is not None else evidence.get("head_before")
    if validate_transition_evidence_bundle(evidence, current_head=effective_current_head, root=root):
        return False
    if rule.get("required_mode") not in {None, ACX_MODE_ADVISORY}:
        return False
    if rule.get("require_clean_git_status") and (
        evidence.get("git_status_before") != "" or evidence.get("git_status_after") != ""
    ):
        return False
    if rule.get("require_empty_files_changed") and evidence.get("files_changed"):
        return False
    return True


def scan_advisory_report_prose(
    report_text: str,
    *,
    phase_id: str,
    from_phase: str,
    to_phase: str,
) -> list[dict[str, Any]]:
    if not isinstance(report_text, str):
        return []

    report_upper = report_text.upper()
    violations: list[dict[str, Any]] = []
    seen_tokens: set[str] = set()
    for token in ADVISORY_REPORT_PROSE_TOKENS:
        if token in seen_tokens:
            continue
        if token.upper() in report_upper:
            seen_tokens.add(token)
            violations.append(
                {
                    "event_type": "violation_advisory",
                    "phase_id": phase_id,
                    "payload": {
                        "violated_rule": "advisory_report_prose",
                        "from_phase": from_phase,
                        "to_phase": to_phase,
                        "matched_token": token,
                        "severity": "low",
                        "supporting_evidence": "report text contains agent-decision language",
                    },
                }
                )
    return violations


def _phase_slug(phase_id: str) -> str:
    slug = phase_id.strip().lower()
    slug = re.sub(r"^acx[-_]", "", slug)
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")


def compute_state_blob_hash(state_path: Path) -> str:
    return hashlib.sha256(_read_bytes(state_path)).hexdigest()


def compute_head_sha(root: Path = ROOT) -> str:
    head_sha = _git_stdout(root, ["rev-parse", "HEAD"]).strip()
    if not head_sha:
        raise LedgerError("unable to compute HEAD sha")
    return head_sha


def compute_ledger_head_hash(ledger_path: Path) -> str | None:
    entries = _load_ledger(ledger_path)
    if not entries:
        return None
    return entries[-1][1].get("event_sha256")


def load_authority_allowlist(manifest_path: Path, phase_id: str | None = None) -> list[str]:
    manifest = _load_authority_manifest(manifest_path)
    classes = manifest.get("classes")
    if not isinstance(classes, dict):
        raise LedgerError("manifest classes must be a JSON object")

    phase_allowlists = manifest.get("phase_allowlists")
    if phase_id is not None and isinstance(phase_allowlists, dict):
        phase_allowlist = phase_allowlists.get(phase_id)
        if isinstance(phase_allowlist, list):
            allowlist = phase_allowlist
        else:
            allowlist = classes.get("canonical_live", [])
    else:
        allowlist = classes.get("canonical_live", [])

    if not isinstance(allowlist, list):
        raise LedgerError("manifest canonical_live allowlist must be a list")

    normalized = sorted(
        {
            item
            for item in allowlist
            if isinstance(item, str) and item.strip()
        }
    )
    return normalized


def discover_phase_evidence_artifacts(root: Path, phase_id: str) -> list[str]:
    artifacts_root = root / "artifacts" / "acx"
    if not artifacts_root.exists():
        return []

    slug = _phase_slug(phase_id)
    matches: list[str] = []
    for path in sorted(artifacts_root.glob("*.json")):
        rel_path = _relative_posix(path, root=root)
        name = path.name.lower()
        if slug and slug in name:
            matches.append(rel_path)
            continue
        try:
            payload = _load_json(path)
        except Exception:
            continue
        if isinstance(payload, dict) and payload.get("phase_id") == phase_id:
            matches.append(rel_path)
    return matches


def _load_state_authorization(state_path: Path) -> dict[str, Any]:
    state = _load_json(state_path)
    if not isinstance(state, dict):
        raise LedgerError("state must be a JSON object")
    authorization = state.get("authorization")
    if not isinstance(authorization, dict):
        raise LedgerError("state authorization must be a JSON object")
    return authorization


def compile_gate_approval(
    phase_id: str,
    *,
    root: Path = ROOT,
    state_path: Path | None = None,
    manifest_path: Path | None = None,
    ledger_path: Path | None = None,
    state_blob_hash: str | None = None,
) -> dict[str, Any]:
    root = _normalize_root(root)
    state_path = state_path or (root / "ACTIVE_CONTEXT_STATE.json")
    manifest_path = manifest_path or (root / AUTHORITY_MANIFEST_FILENAME)
    ledger_path = ledger_path or (root / ".acx" / "ledger.jsonl")

    computed_state_hash = compute_state_blob_hash(state_path)
    if state_blob_hash is not None and state_blob_hash != computed_state_hash:
        raise LedgerError("state_blob_hash must be recomputed from ACTIVE_CONTEXT_STATE.json bytes")

    authorization = _load_state_authorization(state_path)
    allowlist = load_authority_allowlist(manifest_path, phase_id=phase_id)
    head_sha = compute_head_sha(root)
    ledger_head_hash = compute_ledger_head_hash(ledger_path)

    real_execution_authorized = any(
        bool(authorization.get(key))
        for key in (
            "approval_execution_authorized",
            "real_apply_authorized",
            "real_dry_run_execution_authorized",
            "generic_action_runtime_activated",
        )
    )
    runtime_product_bedrock_secrets_opened = any(
        bool(authorization.get(key))
        for key in (
            "runtime_integration_allowed",
            "product_ready",
            "production_authorized",
            "secrets_access_authorized",
        )
    )

    network_scope = authorization.get("network_authorized_scope")
    gate = {
        "record_type": "GATE_APPROVAL",
        "task_id": f"{phase_id}:gate_compiler",
        "phase_id": phase_id,
        "generated_at_source": "system",
        "compiler_version": GATE_COMPILER_VERSION,
        "state_blob_hash": computed_state_hash,
        "head_sha": head_sha,
        "ledger_head_hash": ledger_head_hash,
        "transition_rules_version": TRANSITION_RULES_VERSION,
        "allowlist": allowlist,
        "network_policy": {
            "authorized_scope": network_scope,
            "external_network_allowed": False,
            "github_governance_only": network_scope == "github_active_context_governance_only",
        },
        "rollback_policy": {
            "source": "docs/acx/ROLLBACK.md",
            "compensating_event_required": True,
            "destructive_cleanup_allowed": False,
            "state_restoration_is_non_destructive": True,
        },
        "real_execution_authorized": real_execution_authorized,
        "runtime_product_bedrock_secrets_opened": runtime_product_bedrock_secrets_opened,
        "decision_authority": "operator_or_gate_not_compiler",
    }
    return gate


def validate_gate_approval(
    gate: Any,
    *,
    root: Path = ROOT,
    state_path: Path | None = None,
    manifest_path: Path | None = None,
    ledger_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(gate, dict):
        return ["gate approval must be a JSON object"]

    state_path = state_path or (root / "ACTIVE_CONTEXT_STATE.json")
    manifest_path = manifest_path or (root / AUTHORITY_MANIFEST_FILENAME)
    ledger_path = ledger_path or (root / ".acx" / "ledger.jsonl")

    required_fields = [
        "record_type",
        "task_id",
        "phase_id",
        "generated_at_source",
        "compiler_version",
        "state_blob_hash",
        "head_sha",
        "transition_rules_version",
        "allowlist",
        "network_policy",
        "rollback_policy",
        "real_execution_authorized",
        "runtime_product_bedrock_secrets_opened",
        "decision_authority",
    ]
    for field in required_fields:
        if field not in gate:
            errors.append(f"missing required field: {field}")

    for field in ("record_type", "task_id", "phase_id", "generated_at_source", "compiler_version", "head_sha", "transition_rules_version", "decision_authority"):
        value = gate.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    if gate.get("record_type") != "GATE_APPROVAL":
        errors.append("record_type must be 'GATE_APPROVAL'")
    if gate.get("generated_at_source") != "system":
        errors.append("generated_at_source must be 'system'")
    if gate.get("decision_authority") != "operator_or_gate_not_compiler":
        errors.append("decision_authority must be 'operator_or_gate_not_compiler'")
    if not _validate_sha256_hex(gate.get("state_blob_hash")):
        errors.append("state_blob_hash must be a sha256 hex digest")

    ledger_head_hash = gate.get("ledger_head_hash")
    if ledger_head_hash is not None and not _validate_sha256_hex(ledger_head_hash):
        errors.append("ledger_head_hash must be a sha256 hex digest or null")

    allowlist = gate.get("allowlist")
    if not isinstance(allowlist, list) or any(not isinstance(item, str) or not item.strip() for item in allowlist):
        errors.append("allowlist must be a list of non-empty strings")
    elif not allowlist:
        errors.append("allowlist must not be empty")
    elif allowlist != load_authority_allowlist(manifest_path, phase_id=gate.get("phase_id")):
        errors.append("allowlist must be derived from authority_manifest.json")

    for field in ("network_policy", "rollback_policy"):
        if not isinstance(gate.get(field), dict):
            errors.append(f"{field} must be a JSON object")

    for field in ("real_execution_authorized", "runtime_product_bedrock_secrets_opened"):
        if not isinstance(gate.get(field), bool):
            errors.append(f"{field} must be a boolean")

    computed_state_hash = compute_state_blob_hash(state_path)
    if gate.get("state_blob_hash") != computed_state_hash:
        errors.append("state_blob_hash must be computed from ACTIVE_CONTEXT_STATE.json bytes")

    if gate.get("head_sha") != compute_head_sha(root):
        errors.append("head_sha must match git rev-parse HEAD")

    if gate.get("ledger_head_hash") != compute_ledger_head_hash(ledger_path):
        errors.append("ledger_head_hash must match the current ledger head hash")

    if gate.get("transition_rules_version") != TRANSITION_RULES_VERSION:
        errors.append(f"transition_rules_version must be {TRANSITION_RULES_VERSION!r}")

    return errors


def render_gate_approval(gate: dict[str, Any], *, root: Path = ROOT) -> str:
    if not isinstance(gate, dict):
        raise LedgerError("gate approval must be a JSON object")
    rendered = json.dumps(gate, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    vocabulary_hits = contains_forbidden_decision_vocabulary(rendered)
    if vocabulary_hits:
        raise LedgerError("gate approval contains forbidden decision vocabulary")
    return rendered


def _packet_default_fields(phase_id: str) -> dict[str, Any]:
    return {
        "phase_id": phase_id,
        "objective": f"Compile review packet material for {phase_id} from repository facts.",
        "changed_files": [],
        "evidence_artifacts": [],
        "validations": [],
        "warnings": [
            "compiler output is advisory only",
            "operator review is still required",
        ],
        "limitations": [
            "compiler does not decide approval",
            "compiler does not change live state",
        ],
        "rollback_plan": "Restore source files from git and rerun the compiler after any correction.",
        "requested_operator_decision": "operator_review_requested",
    }


def _normalize_packet_lists(packet: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(packet)
    for field in ("changed_files", "evidence_artifacts", "validations", "warnings", "limitations"):
        value = normalized.get(field)
        if value is None:
            normalized[field] = []
            continue
        if not isinstance(value, list):
            normalized[field] = [str(value)]
            continue
        normalized[field] = [item for item in value if isinstance(item, str)]
    return normalized


def validate_operator_packet(packet: Any, *, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(packet, dict):
        return ["packet must be a JSON object"]

    required_fields = [
        "phase_id",
        "objective",
        "changed_files",
        "evidence_artifacts",
        "validations",
        "warnings",
        "limitations",
        "rollback_plan",
        "requested_operator_decision",
    ]
    for field in required_fields:
        if field not in packet:
            errors.append(f"missing required field: {field}")

    for field in ("phase_id", "objective", "rollback_plan", "requested_operator_decision"):
        value = packet.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    for field in ("changed_files", "evidence_artifacts", "validations", "warnings", "limitations"):
        value = packet.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be a list")
            continue
        if any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{field} must contain only non-empty strings")

    warnings = packet.get("warnings")
    if not isinstance(warnings, list) or not warnings or any(
        not isinstance(item, str) or not item.strip() for item in warnings
    ):
        errors.append("warnings must not be empty")
    limitations = packet.get("limitations")
    if not isinstance(limitations, list) or not limitations or any(
        not isinstance(item, str) or not item.strip() for item in limitations
    ):
        errors.append("limitations must not be empty")
    if not isinstance(packet.get("rollback_plan"), str) or not packet.get("rollback_plan", "").strip():
        errors.append("rollback_plan must not be empty")

    try:
        rendered = render_operator_packet(packet, root=root)
    except LedgerError as exc:
        errors.append(str(exc))
        return errors
    vocabulary_hits = contains_forbidden_decision_vocabulary(rendered)
    if vocabulary_hits:
        errors.append(
            "forbidden decision vocabulary present: " + ", ".join(sorted(set(vocabulary_hits)))
        )

    if len(rendered.split()) > PACKET_MAX_WORDS:
        errors.append(f"packet exceeds target max word count of {PACKET_MAX_WORDS}")

    return errors


def contains_forbidden_decision_vocabulary(text: str) -> list[str]:
    if not isinstance(text, str):
        return []
    matches: list[str] = []
    upper_text = text.upper()
    for token in FORBIDDEN_DECISION_VOCABULARY:
        pattern = r"\b" + re.escape(token.upper()) + r"\b"
        if re.search(pattern, upper_text):
            matches.append(token)
    return matches


def _trim_packet_for_word_limit(packet: dict[str, Any], *, max_words: int) -> dict[str, Any]:
    working = _normalize_packet_lists(packet)
    candidate_sizes = [
        (8, 8, 8),
        (4, 4, 4),
        (2, 2, 2),
        (1, 1, 1),
        (0, 0, 0),
    ]

    def _summarize_list(items: list[str], limit: int) -> list[str]:
        if limit < 0:
            limit = 0
        if len(items) <= limit:
            return items
        if limit == 0:
            return [f"... {len(items)} more"]
        summarized = items[:limit]
        summarized.append(f"... {len(items) - limit} more")
        return summarized

    for changed_files_limit, evidence_limit, validation_limit in candidate_sizes:
        candidate = copy.deepcopy(working)
        candidate["changed_files"] = _summarize_list(candidate.get("changed_files", []), changed_files_limit)
        candidate["evidence_artifacts"] = _summarize_list(candidate.get("evidence_artifacts", []), evidence_limit)
        candidate["validations"] = _summarize_list(candidate.get("validations", []), validation_limit)
        rendered = json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
        if len(rendered.split()) <= max_words:
            return candidate

    return working


def render_operator_packet(packet: dict[str, Any], *, root: Path = ROOT, max_words: int = PACKET_MAX_WORDS) -> str:
    if not isinstance(packet, dict):
        raise LedgerError("packet must be a JSON object")
    compressed = _trim_packet_for_word_limit(packet, max_words=max_words)
    rendered = json.dumps(compressed, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if contains_forbidden_decision_vocabulary(rendered):
        raise LedgerError("operator packet contains forbidden decision vocabulary")
    return rendered


def compile_operator_packet(
    phase_id: str,
    *,
    root: Path = ROOT,
    state_path: Path | None = None,
    manifest_path: Path | None = None,
    ledger_path: Path | None = None,
    evidence_path: Path | None = None,
) -> dict[str, Any]:
    root = _normalize_root(root)
    state_path = state_path or (root / "ACTIVE_CONTEXT_STATE.json")
    manifest_path = manifest_path or (root / AUTHORITY_MANIFEST_FILENAME)
    ledger_path = ledger_path or (root / ".acx" / "ledger.jsonl")

    gate = compile_gate_approval(
        phase_id,
        root=root,
        state_path=state_path,
        manifest_path=manifest_path,
        ledger_path=ledger_path,
    )
    evidence_artifacts = discover_phase_evidence_artifacts(root, phase_id)
    if evidence_path is not None:
        explicit_path = evidence_path if evidence_path.is_absolute() else (root / evidence_path)
        explicit_rel = _relative_posix(explicit_path.resolve(), root=root)
        if explicit_rel not in evidence_artifacts and explicit_path.exists():
            evidence_artifacts = [explicit_rel, *evidence_artifacts]
    if not evidence_artifacts:
        raise LedgerError(f"no phase evidence artifacts found for {phase_id}")

    evidence_payloads: list[dict[str, Any]] = []
    for rel_path in evidence_artifacts:
        payload = _load_json(root / rel_path)
        if isinstance(payload, dict):
            evidence_payloads.append(payload)

    primary = evidence_payloads[0] if evidence_payloads else {}
    objective = primary.get("purpose")
    if not isinstance(objective, str) or not objective.strip():
        objective = f"Compile review packet material for {phase_id} from repository facts."

    changed_files = primary.get("files_changed")
    if not isinstance(changed_files, list) or not all(isinstance(item, str) for item in changed_files):
        changed_files = _git_stdout(root, ["show", "--pretty=format:", "--name-only", "HEAD"]).splitlines()
    changed_files = [item for item in changed_files if isinstance(item, str) and item.strip()]

    validations = primary.get("validations")
    if not isinstance(validations, list) or any(not isinstance(item, str) or not item.strip() for item in validations):
        validations = primary.get("tests_run")
    if not isinstance(validations, list) or any(not isinstance(item, str) or not item.strip() for item in validations):
        validations = [
            "validate_active_context.py",
            "tools/acx_validate.py",
        ]

    warnings = primary.get("warnings")
    if not isinstance(warnings, list) or any(not isinstance(item, str) or not item.strip() for item in warnings):
        warnings = [
            "compiler output is advisory only",
            "operator review is still required",
        ]

    limitations = primary.get("limitations")
    if not isinstance(limitations, list) or any(not isinstance(item, str) or not item.strip() for item in limitations):
        limitations = [
            "compiler does not decide approval",
            "compiler does not change live state",
        ]

    rollback_plan = primary.get("rollback_plan")
    if not isinstance(rollback_plan, str) or not rollback_plan.strip():
        rollback_plan = "Restore source files from git and rerun the compiler after any correction."

    requested_operator_decision = primary.get("requested_operator_decision")
    if not isinstance(requested_operator_decision, str) or not requested_operator_decision.strip():
        requested_operator_decision = "operator_review_requested"

    packet = {
        "phase_id": phase_id,
        "objective": objective,
        "changed_files": changed_files,
        "evidence_artifacts": evidence_artifacts,
        "validations": validations,
        "warnings": warnings,
        "limitations": limitations,
        "rollback_plan": rollback_plan,
        "requested_operator_decision": requested_operator_decision,
        "gate_reference": {
            "task_id": gate["task_id"],
            "state_blob_hash": gate["state_blob_hash"],
            "head_sha": gate["head_sha"],
            "decision_authority": gate["decision_authority"],
        },
    }
    return packet


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="acx.py")
    parser.add_argument("--root", type=Path, default=ROOT)
    subparsers = parser.add_subparsers(dest="command", required=True)

    event_parser = subparsers.add_parser("event")
    event_subparsers = event_parser.add_subparsers(dest="event_command", required=True)
    append_parser = event_subparsers.add_parser("append")
    append_parser.add_argument("event_json", type=Path)
    append_parser.add_argument("--ledger", required=True, type=Path)

    fold_parser = subparsers.add_parser("fold")
    fold_parser.add_argument("--ledger", required=True, type=Path)
    fold_parser.add_argument("--out", required=True, type=Path)

    verify_parser = subparsers.add_parser("verify-chain")
    verify_parser.add_argument("--ledger", required=True, type=Path)

    authority_parser = subparsers.add_parser("authority")
    authority_subparsers = authority_parser.add_subparsers(dest="authority_command", required=True)
    authority_manifest_parser = authority_subparsers.add_parser("manifest")
    authority_manifest_parser.add_argument("--out", required=True, type=Path)
    authority_check_parser = authority_subparsers.add_parser("check")
    authority_check_parser.add_argument("--manifest", required=True, type=Path)

    render_parser = subparsers.add_parser("render")
    render_parser.add_argument("--check", action="store_true")
    render_parser.add_argument("--manifest", required=True, type=Path)

    guard_parser = subparsers.add_parser("guard")
    guard_subparsers = guard_parser.add_subparsers(dest="guard_command", required=True)
    manual_write_parser = guard_subparsers.add_parser("manual-write")
    manual_write_parser.add_argument("--manifest", required=True, type=Path)
    manual_write_parser.add_argument("--ledger", required=True, type=Path)
    manual_write_parser.add_argument("--state", required=True, type=Path)

    gate_parser = subparsers.add_parser("gate")
    gate_parser.add_argument("phase_id")
    gate_parser.add_argument("--phase", dest="phase_id_opt")
    gate_parser.add_argument("--manifest", type=Path, default=ROOT / AUTHORITY_MANIFEST_FILENAME)
    gate_parser.add_argument("--ledger", type=Path, default=ROOT / ".acx" / "ledger.jsonl")
    gate_parser.add_argument("--state", type=Path, default=ROOT / "ACTIVE_CONTEXT_STATE.json")

    packet_parser = subparsers.add_parser("packet")
    packet_parser.add_argument("phase_id", nargs="?")
    packet_parser.add_argument("--phase", dest="phase_id_opt")
    packet_parser.add_argument("--evidence", type=Path)
    packet_parser.add_argument("--manifest", type=Path, default=ROOT / AUTHORITY_MANIFEST_FILENAME)
    packet_parser.add_argument("--ledger", type=Path, default=ROOT / ".acx" / "ledger.jsonl")
    packet_parser.add_argument("--state", type=Path, default=ROOT / "ACTIVE_CONTEXT_STATE.json")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    root = _normalize_root(args.root)
    try:
        if args.command == "event" and args.event_command == "append":
            append_event(args.event_json, args.ledger, root=root)
        elif args.command == "fold":
            fold(args.ledger, args.out, root=root)
        elif args.command == "verify-chain":
            verify_chain(args.ledger, root=root)
        elif args.command == "authority" and args.authority_command == "manifest":
            authority_manifest(root, args.out)
        elif args.command == "authority" and args.authority_command == "check":
            authority_check(root, args.manifest)
        elif args.command == "render" and args.check:
            render_check(root, args.manifest)
        elif args.command == "guard" and args.guard_command == "manual-write":
            guard_manual_write(args.manifest, args.ledger, args.state, root=root)
        elif args.command == "gate":
            phase_id = args.phase_id or args.phase_id_opt
            if not phase_id:
                raise LedgerError("phase_id is required")
            gate = compile_gate_approval(
                phase_id,
                root=root,
                state_path=args.state,
                manifest_path=args.manifest,
                ledger_path=args.ledger,
            )
            errors = validate_gate_approval(
                gate,
                root=root,
                state_path=args.state,
                manifest_path=args.manifest,
                ledger_path=args.ledger,
            )
            if errors:
                raise LedgerError("; ".join(errors))
            print(render_gate_approval(gate), end="")
        elif args.command == "packet":
            phase_id = args.phase_id or args.phase_id_opt
            if not phase_id:
                raise LedgerError("phase_id is required")
            packet = compile_operator_packet(
                phase_id,
                root=root,
                state_path=args.state,
                manifest_path=args.manifest,
                ledger_path=args.ledger,
                evidence_path=args.evidence,
            )
            errors = validate_operator_packet(packet, root=root)
            if errors:
                raise LedgerError("; ".join(errors))
            print(render_operator_packet(packet, root=root), end="")
        else:  # pragma: no cover - argparse prevents this
            raise LedgerError(f"unsupported command: {args.command}")
    except LedgerError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
