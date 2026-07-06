#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import hashlib
import json
import os
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
    entries: list[tuple[int, dict[str, Any]]] = []
    with ledger_path.open("r", encoding="utf-8", newline="") as handle:
        for lineno, raw_line in enumerate(handle, 1):
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
        resolved = _resolve_relative_path(baseline_path, relative_to=root)
        state_hash = _state_hash_from_bytes(_read_bytes(resolved))
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
    previous_hash = None
    for line_no, event in entries:
        previous_hash = _validate_event_record(
            event,
            line_no=line_no,
            previous_hash=previous_hash,
            check_baseline=True,
            root=root,
        )


def _fold_genesis_state(event: dict[str, Any], *, root: Path = ROOT) -> bytes:
    payload = event.get("payload")
    if not isinstance(payload, dict):
        raise LedgerError("genesis payload must be a JSON object")

    baseline_path = payload.get("baseline_state_path")
    if isinstance(baseline_path, str):
        resolved = _resolve_relative_path(baseline_path, relative_to=root)
        state_bytes = _read_bytes(resolved)
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


def fold(ledger_path: Path, out_path: Path, *, root: Path = ROOT) -> None:
    entries = _load_ledger(ledger_path)
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
        )
        event_type = event.get("event_type")
        if event_type == "genesis":
            folded_state = _fold_genesis_state(event, root=root)
        elif event_type == "violation_advisory":
            continue
        else:
            raise LedgerError(
                f"line {line_no}: unsupported state-mutating event type {event_type!r}"
            )

    if folded_state is None:
        raise LedgerError("ledger does not contain a genesis event")

    _write_bytes(out_path, folded_state)


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
        else:  # pragma: no cover - argparse prevents this
            raise LedgerError(f"unsupported command: {args.command}")
    except LedgerError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
