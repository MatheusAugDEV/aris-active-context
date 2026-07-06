from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
MANIFEST_PATH = ROOT / "authority_manifest.json"
LEDGER_PATH = ROOT / ".acx" / "ledger.jsonl"
CURRENT_HEAD = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
).stdout.strip()


def _load_acx_module():
    spec = importlib.util.spec_from_file_location("acx_r6_gate_compiler_operator_packet_test", TOOLS)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load tools/acx.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ACX = _load_acx_module()


def _run_acx(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOLS), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class ACXGateCompilerOperatorPacketTest(unittest.TestCase):
    def test_gate_compiler_uses_actual_state_bytes_and_head_sha(self) -> None:
        gate = ACX.compile_gate_approval("ACX-R6")
        self.assertEqual(gate["state_blob_hash"], hashlib.sha256(STATE_PATH.read_bytes()).hexdigest())
        self.assertEqual(gate["head_sha"], CURRENT_HEAD)
        self.assertEqual(gate["ledger_head_hash"], ACX.compute_ledger_head_hash(LEDGER_PATH))

    def test_gate_compiler_derives_allowlist_from_authority_manifest(self) -> None:
        allowlist = ACX.load_authority_allowlist(MANIFEST_PATH, phase_id="ACX-R6")
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(allowlist, manifest["classes"]["canonical_live"])
        self.assertIn("ACTIVE_CONTEXT_STATE.json", allowlist)
        self.assertIn("tools/acx.py", allowlist)

    def test_gate_compiler_rejects_fake_state_hash(self) -> None:
        with self.assertRaises(ACX.LedgerError):
            ACX.compile_gate_approval("ACX-R6", state_blob_hash="f" * 64)

    def test_gate_compiler_marks_compiler_as_non_authoritative(self) -> None:
        gate = ACX.compile_gate_approval("ACX-R6")
        self.assertEqual(gate["generated_at_source"], "system")
        self.assertEqual(gate["decision_authority"], "operator_or_gate_not_compiler")
        self.assertFalse(gate["real_execution_authorized"])
        self.assertFalse(gate["runtime_product_bedrock_secrets_opened"])

    def test_cli_gate_and_packet_subcommands_emit_json(self) -> None:
        gate_result = _run_acx(["gate", "ACX-R6"])
        self.assertEqual(gate_result.returncode, 0, gate_result.stderr)
        gate = json.loads(gate_result.stdout)
        self.assertEqual(gate["phase_id"], "ACX-R6")
        self.assertEqual(gate["decision_authority"], "operator_or_gate_not_compiler")

        packet_result = _run_acx(["packet", "ACX-R6"])
        self.assertEqual(packet_result.returncode, 0, packet_result.stderr)
        packet = json.loads(packet_result.stdout)
        self.assertEqual(packet["phase_id"], "ACX-R6")
        self.assertIn("rollback_plan", packet)

    def test_packet_generator_includes_limitations_and_risks(self) -> None:
        packet = ACX.compile_operator_packet("ACX-R6")
        self.assertTrue(packet["warnings"])
        self.assertTrue(packet["limitations"])

    def test_packet_generator_includes_rollback_plan(self) -> None:
        packet = ACX.compile_operator_packet("ACX-R6")
        self.assertIsInstance(packet["rollback_plan"], str)
        self.assertTrue(packet["rollback_plan"].strip())

    def test_blank_limitations_and_risks_are_rejected(self) -> None:
        packet = ACX.compile_operator_packet("ACX-R6")
        packet["warnings"] = [""]
        packet["limitations"] = []
        errors = ACX.validate_operator_packet(packet)
        self.assertTrue(errors)
        self.assertTrue(any("warnings must not be empty" in error for error in errors))
        self.assertTrue(any("limitations must not be empty" in error for error in errors))

    def test_blank_rollback_plan_is_rejected(self) -> None:
        packet = ACX.compile_operator_packet("ACX-R6")
        packet["rollback_plan"] = " "
        errors = ACX.validate_operator_packet(packet)
        self.assertTrue(errors)
        self.assertTrue(any("rollback_plan must not be empty" in error for error in errors))

    def test_packet_truncation_preserves_limitations_risks_and_rollback_plan(self) -> None:
        packet = {
            "phase_id": "ACX-R6",
            "objective": "Validate packet truncation behavior.",
            "changed_files": [f"changed_file_{index}.txt" for index in range(160)],
            "evidence_artifacts": [f"artifact_{index}.json" for index in range(160)],
            "validations": [f"validation_{index}.json" for index in range(160)],
            "warnings": ["risk boundary must stay visible", "operator review remains required"],
            "limitations": ["limitations must survive truncation", "rollback guidance must stay intact"],
            "rollback_plan": "restore source files and rerun the compiler",
            "requested_operator_decision": "operator_review_requested",
        }
        rendered = ACX.render_operator_packet(packet, max_words=300)
        self.assertLessEqual(len(rendered.split()), 300)
        self.assertIn("risk boundary must stay visible", rendered)
        self.assertIn("limitations must survive truncation", rendered)
        self.assertIn("rollback guidance must stay intact", rendered)
        self.assertIn("restore source files and rerun the compiler", rendered)

    def test_generated_gate_output_avoids_forbidden_decision_vocabulary(self) -> None:
        gate_text = ACX.render_gate_approval(ACX.compile_gate_approval("ACX-R6"))
        self.assertEqual(ACX.contains_forbidden_decision_vocabulary(gate_text), [])

    def test_generated_packet_output_avoids_forbidden_decision_vocabulary(self) -> None:
        packet_text = ACX.render_operator_packet(ACX.compile_operator_packet("ACX-R6"))
        self.assertEqual(ACX.contains_forbidden_decision_vocabulary(packet_text), [])

    def test_compiler_does_not_mutate_active_context_state(self) -> None:
        before = STATE_PATH.read_bytes()
        ACX.compile_gate_approval("ACX-R6")
        ACX.compile_operator_packet("ACX-R6")
        after = STATE_PATH.read_bytes()
        self.assertEqual(before, after)

    def test_compiler_does_not_mutate_ledger(self) -> None:
        before = LEDGER_PATH.read_bytes()
        ACX.compile_gate_approval("ACX-R6")
        ACX.compile_operator_packet("ACX-R6")
        after = LEDGER_PATH.read_bytes()
        self.assertEqual(before, after)

    def test_hard_mode_remains_disabled(self) -> None:
        self.assertEqual(ACX.current_acx_mode(), "advisory")
        self.assertFalse(ACX.hard_mode_enabled())
        self.assertNotEqual(os.environ.get("ACX_MODE"), "hard")


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
