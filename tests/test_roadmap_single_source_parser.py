import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        ROOT / "scripts" / "validate_active_context_state.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestRoadmapSingleSourceParser(unittest.TestCase):
    def setUp(self):
        self.module = _load_validator_module()
        self.state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))

    def test_parse_active_phase_block_by_phase_id(self):
        block = self.module._find_roadmap_phase_block(self.state["current_phase_id"])
        self.assertIsNotNone(block)
        self.assertEqual(block["phase_id"], self.state["current_phase_id"])
        self.assertEqual(block["status"], "CLOSED")
        self.assertEqual(block["next_phase"], "DIAGNOSTICO_AUTOMACAO_GATE")

        row = self.module._get_transition_row(self.state["current_phase_id"], self.state["decision"])
        self.assertIsNotNone(row)
        self.assertEqual(row["current_phase_id"], self.state["current_phase_id"])
        self.assertEqual(row["next_phase_id"], "DIAGNOSTICO_AUTOMACAO_GATE")
        self.assertFalse(row["next_phase_requires_operator_decision"])

    def test_parse_simple_next_phase(self):
        parsed = self.module._parse_next_phase_spec("BenchUIX")
        self.assertEqual(parsed["next_phase_id"], "BenchUIX")
        self.assertEqual(parsed["next_phase_candidates"], ["BenchUIX"])
        self.assertFalse(parsed["next_phase_requires_operator_decision"])

    def test_parse_conditional_next_phase(self):
        parsed = self.module._parse_next_phase_spec(
            "se gap bloqueante → Camada de Construção de Automação; senão → BenchUIX"
        )
        self.assertIsNone(parsed["next_phase_id"])
        self.assertEqual(
            parsed["next_phase_candidates"],
            ["Camada de Construção de Automação", "BenchUIX"],
        )
        self.assertTrue(parsed["next_phase_requires_operator_decision"])
        self.assertEqual(parsed["condition"], "gap bloqueante")

    def test_missing_phase_block_fails_closed(self):
        self.assertIsNone(self.module._find_roadmap_phase_block("PHASE_DOES_NOT_EXIST"))
        self.assertIsNone(self.module._get_transition_row("PHASE_DOES_NOT_EXIST", "pass"))


if __name__ == "__main__":
    unittest.main()
