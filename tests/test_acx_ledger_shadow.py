from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
LEDGER_PATH = ROOT / ".acx" / "ledger.jsonl"
FIXTURES = ROOT / "tests" / "fixtures" / "acx_ledger"
GOLDEN_LEDGER = FIXTURES / "golden_ledger.jsonl"
EXPECTED_STATE = FIXTURES / "expected_state.json"
CANONICALIZATION_VERSION = "acx-ledger-canonical-v1"
HASH_ALGORITHM = "sha256"


def _run(args: list[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOLS), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(
        json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _read_ledger(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class ACXLedgerShadowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.state_bytes = STATE_PATH.read_bytes()
        self.state_sha256 = hashlib.sha256(self.state_bytes).hexdigest()

    def test_repo_shadow_ledger_verify_chain_passes(self) -> None:
        result = _run(["verify-chain", "--ledger", str(LEDGER_PATH)])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_verify_chain_detects_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tampered = Path(tmpdir) / "tampered.jsonl"
            tampered.write_text(GOLDEN_LEDGER.read_text(encoding="utf-8"), encoding="utf-8")
            lines = tampered.read_text(encoding="utf-8").splitlines()
            second = json.loads(lines[1])
            second["prev_sha256"] = "0" * 64
            lines[1] = json.dumps(second, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
            tampered.write_text("\n".join(lines) + "\n", encoding="utf-8")

            result = _run(["verify-chain", "--ledger", str(tampered)])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("line 2", result.stderr)
            self.assertIn("prev_sha256 mismatch", result.stderr)

    def test_fold_over_golden_fixture_equals_expected_state_byte_for_byte(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = Path(tmpdir) / "folded.json"
            result = _run(["fold", "--ledger", str(GOLDEN_LEDGER), "--out", str(out_path)])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(out_path.read_bytes(), EXPECTED_STATE.read_bytes())

    def test_fold_is_deterministic_across_two_executions(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out1 = Path(tmpdir) / "folded-1.json"
            out2 = Path(tmpdir) / "folded-2.json"

            result1 = _run(["fold", "--ledger", str(GOLDEN_LEDGER), "--out", str(out1)])
            result2 = _run(["fold", "--ledger", str(GOLDEN_LEDGER), "--out", str(out2)])

            self.assertEqual(result1.returncode, 0, result1.stderr)
            self.assertEqual(result2.returncode, 0, result2.stderr)
            self.assertEqual(out1.read_bytes(), out2.read_bytes())
            self.assertEqual(out1.read_bytes(), EXPECTED_STATE.read_bytes())

    def test_event_append_computes_prev_sha256_correctly(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            ledger = tmpdir_path / "ledger.jsonl"
            genesis_event = tmpdir_path / "genesis.json"
            advisory_event = tmpdir_path / "advisory.json"

            _write_json(
                genesis_event,
                {
                    "event_id": "00000000-0000-4000-8000-000000000001",
                    "event_type": "genesis",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:00Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"baseline_state_path": "ACTIVE_CONTEXT_STATE.json"},
                    "state_blob_hash": self.state_sha256,
                },
            )
            _write_json(
                advisory_event,
                {
                    "event_id": "00000000-0000-4000-8000-000000000002",
                    "event_type": "violation_advisory",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:01Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"message": "shadow no-op advisory"},
                },
            )

            result = _run(["event", "append", str(genesis_event), "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)
            first_event = _read_ledger(ledger)[0]
            self.assertIsNone(first_event["prev_sha256"])
            self.assertIsNone(first_event["ledger_head_hash"])
            self.assertEqual(first_event["state_blob_hash"], self.state_sha256)

            result = _run(["event", "append", str(advisory_event), "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)
            events = _read_ledger(ledger)
            self.assertEqual(events[1]["prev_sha256"], events[0]["event_sha256"])
            self.assertEqual(events[1]["ledger_head_hash"], events[0]["event_sha256"])

    def test_event_append_rejects_conflicting_event_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            ledger = tmpdir_path / "ledger.jsonl"
            genesis_event = tmpdir_path / "genesis.json"
            bad_hash = tmpdir_path / "bad-hash.json"

            _write_json(
                genesis_event,
                {
                    "event_id": "00000000-0000-4000-8000-000000000001",
                    "event_type": "genesis",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:00Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"baseline_state_path": "ACTIVE_CONTEXT_STATE.json"},
                    "state_blob_hash": self.state_sha256,
                },
            )
            _write_json(
                bad_hash,
                {
                    "event_id": "00000000-0000-4000-8000-000000000004",
                    "event_type": "violation_advisory",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:03Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"message": "bad hash"},
                    "event_sha256": "f" * 64,
                },
            )

            result = _run(["event", "append", str(genesis_event), "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)

            conflict_hash = _run(["event", "append", str(bad_hash), "--ledger", str(ledger)])
            self.assertNotEqual(conflict_hash.returncode, 0)
            self.assertIn("event_sha256 conflict", conflict_hash.stderr)

    def test_event_append_rejects_conflicting_prev_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            ledger = tmpdir_path / "ledger.jsonl"
            genesis_event = tmpdir_path / "genesis.json"
            bad_prev = tmpdir_path / "bad-prev.json"

            _write_json(
                genesis_event,
                {
                    "event_id": "00000000-0000-4000-8000-000000000001",
                    "event_type": "genesis",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:00Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"baseline_state_path": "ACTIVE_CONTEXT_STATE.json"},
                    "state_blob_hash": self.state_sha256,
                },
            )
            _write_json(
                bad_prev,
                {
                    "event_id": "00000000-0000-4000-8000-000000000003",
                    "event_type": "violation_advisory",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:02Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "prev_sha256": "1" * 64,
                    "payload": {"message": "bad prev"},
                },
            )

            result = _run(["event", "append", str(genesis_event), "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)

            conflict_prev = _run(["event", "append", str(bad_prev), "--ledger", str(ledger)])
            self.assertNotEqual(conflict_prev.returncode, 0)
            self.assertIn("prev_sha256 conflict", conflict_prev.stderr)

    def test_cli_does_not_modify_active_state(self) -> None:
        before = STATE_PATH.read_bytes()
        with tempfile.TemporaryDirectory() as tmpdir:
            ledger = Path(tmpdir) / "ledger.jsonl"
            genesis_event = Path(tmpdir) / "genesis.json"
            _write_json(
                genesis_event,
                {
                    "event_id": "00000000-0000-4000-8000-000000000010",
                    "event_type": "genesis",
                    "event_schema_version": "1.0",
                    "phase_id": "ACX-R2B",
                    "timestamp_utc": "2026-07-05T23:10:10Z",
                    "project_commit_sha": "08b5ebc452c1b6fde904cef0af2c4369fa5295c9",
                    "payload": {"baseline_state_path": "ACTIVE_CONTEXT_STATE.json"},
                    "state_blob_hash": self.state_sha256,
                },
            )
            result = _run(["event", "append", str(genesis_event), "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)
            result = _run(["verify-chain", "--ledger", str(ledger)])
            self.assertEqual(result.returncode, 0, result.stderr)
            result = _run(["fold", "--ledger", str(ledger), "--out", str(Path(tmpdir) / "folded.json")])
            self.assertEqual(result.returncode, 0, result.stderr)

        after = STATE_PATH.read_bytes()
        self.assertEqual(before, after)


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
