from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
BASE_STATE = (ROOT / "ACTIVE_CONTEXT_STATE.json").read_bytes()
BASE_LEDGER = (ROOT / ".acx" / "ledger.jsonl").read_text(encoding="utf-8")
BASE_HEAD_SHA = "7274d5429f7683106e14c5cf966da3c2c1341708"


def _run_acx(root: Path, args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    effective_env = os.environ.copy()
    if env:
        effective_env.update(env)
    return subprocess.run(
        [sys.executable, str(TOOLS), "--root", str(root), *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
        env=effective_env,
    )


def _run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _minimal_manifest() -> dict[str, object]:
    return {
        "manifest_version": "1",
        "mode": "advisory",
        "generated_by": "tools/acx.py authority manifest",
        "source_of_truth_note": (
            "ACTIVE_CONTEXT_STATE.json remains live canonical source; this manifest is advisory "
            "classification metadata."
        ),
        "scan_exclusions": [
            {
                "path": "artifacts/acx/r3_authority_manifest_evidence.json",
                "reason": "Self-generated advisory evidence; excluded from scan to avoid evidence recursion.",
                "scope": "repo-self-reference-advisory",
            },
            {
                "path": "authority_manifest.json",
                "reason": "Self-generated advisory output; excluded from scan to avoid manifest recursion.",
                "scope": "repo-self-reference-advisory",
            },
        ],
        "classes": {
            "canonical_live": [],
            "derived_render": [],
            "doc_support": [],
            "archived_forbidden": [],
        },
        "entries": {},
    }


def _bootstrap_repo(root: Path) -> None:
    _run_git(root, ["init"])
    _run_git(root, ["config", "user.name", "Codex Test"])
    _run_git(root, ["config", "user.email", "codex@example.com"])

    _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", BASE_STATE)
    _write_text(root / ".acx" / "ledger.jsonl", BASE_LEDGER)
    _write_text(root / "authority_manifest.json", json.dumps(_minimal_manifest(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")

    add_result = _run_git(root, ["add", "ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl", "authority_manifest.json"])
    if add_result.returncode != 0:
        raise RuntimeError(add_result.stderr)
    commit_result = _run_git(root, ["commit", "-m", "base"])
    if commit_result.returncode != 0:
        raise RuntimeError(commit_result.stderr)


def _append_violation_event(root: Path, ledger_path: Path, *, message: str) -> None:
    event_path = root / "violation_event.json"
    _write_text(
        event_path,
        json.dumps(
            {
                "event_id": "11111111-1111-4111-8111-111111111111",
                "event_type": "violation_advisory",
                "event_schema_version": "1.0",
                "phase_id": "ACX-R4",
                "timestamp_utc": "2026-07-06T00:00:00Z",
                "project_commit_sha": BASE_HEAD_SHA,
                "payload": {
                    "violated_rule": "manual_write_block",
                    "severity": "low",
                    "supporting_evidence": message,
                },
            },
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
    )
    result = _run_acx(root, ["event", "append", str(event_path), "--ledger", str(ledger_path)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def _write_genesis_ledger_for_state(root: Path, ledger_path: Path) -> None:
    event_path = root / "genesis_event.json"
    _write_text(
        event_path,
        json.dumps(
            {
                "event_id": "22222222-2222-4222-8222-222222222222",
                "event_type": "genesis",
                "event_schema_version": "1.0",
                "phase_id": "ACX-R4",
                "timestamp_utc": "2026-07-06T00:00:00Z",
                "project_commit_sha": BASE_HEAD_SHA,
                "payload": {"baseline_state_path": "ACTIVE_CONTEXT_STATE.json"},
            },
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
    )
    result = _run_acx(root, ["event", "append", str(event_path), "--ledger", str(ledger_path)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def _stage(root: Path, *paths: str) -> None:
    result = _run_git(root, ["add", *paths])
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


class ACXManualWriteBlockTest(unittest.TestCase):
    def test_clean_stage_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertEqual(result.returncode, 0, result.stderr)

    def test_manual_state_edit_without_ledger_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + BASE_STATE)
            _stage(root, "ACTIVE_CONTEXT_STATE.json")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manual write block", result.stderr)

    def test_manual_state_edit_plus_unrelated_ledger_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + BASE_STATE)
            _append_violation_event(root, root / ".acx" / "ledger.jsonl", message="unrelated event")
            _stage(root, "ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manual write block", result.stderr)

    def test_matching_staged_fold_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + BASE_STATE)
            temp_ledger = root / "generated_ledger.jsonl"
            _write_text(temp_ledger, "")
            _write_genesis_ledger_for_state(root, temp_ledger)
            shutil.copy2(temp_ledger, root / ".acx" / "ledger.jsonl")
            _stage(root, "ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertEqual(result.returncode, 0, result.stderr)

    def test_emergency_bypass_prints_message_and_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + BASE_STATE)
            _stage(root, "ACTIVE_CONTEXT_STATE.json")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
                env={"ACX_DISABLE_HOOK": "1"},
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("ACX_DISABLE_HOOK=1 set", result.stdout)

    def test_guard_does_not_modify_state_or_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            state_before = _read_bytes(root / "ACTIVE_CONTEXT_STATE.json")
            ledger_before = _read_bytes(root / ".acx" / "ledger.jsonl")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(state_before, _read_bytes(root / "ACTIVE_CONTEXT_STATE.json"))
            self.assertEqual(ledger_before, _read_bytes(root / ".acx" / "ledger.jsonl"))

    def test_invalid_staged_ledger_chain_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_repo(root)

            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + BASE_STATE)
            _append_violation_event(root, root / ".acx" / "ledger.jsonl", message="broken chain candidate")
            ledger_path = root / ".acx" / "ledger.jsonl"
            lines = ledger_path.read_text(encoding="utf-8").splitlines()
            bad_event = json.loads(lines[1])
            bad_event["prev_sha256"] = "0" * 64
            lines[1] = json.dumps(bad_event, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
            _write_text(ledger_path, "\n".join(lines) + "\n")
            _stage(root, "ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl")

            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manual write block", result.stderr)

    def test_pre_commit_hook_registered(self) -> None:
        text = (ROOT / ".pre-commit-config.yaml").read_text(encoding="utf-8")
        self.assertIn("acx-manual-write-block", text)
        self.assertIn("python3 tools/acx.py guard manual-write --manifest authority_manifest.json --ledger .acx/ledger.jsonl --state ACTIVE_CONTEXT_STATE.json", text)


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
