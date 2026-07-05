import importlib.util
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_validator_module():
    spec = importlib.util.spec_from_file_location("acx_validate", ROOT / "tools" / "acx_validate.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ACXValidateTests(unittest.TestCase):
    def setUp(self):
        self.module = _load_validator_module()
        self.state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.schema = json.loads((ROOT / "ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
        self.roadmap = (ROOT / "ROADMAP_CANONICAL.md").read_text(encoding="utf-8")
        self.boot = (ROOT / "BOOT.md").read_text(encoding="utf-8")

    def test_schema_accepts_current_state_with_roadmap_cursor(self):
        errors = self.module.validate_schema(self.state, self.schema)
        self.assertEqual(errors, [])
        self.assertEqual(self.state["roadmap_cursor"]["state"], "CANDIDATE")
        self.assertEqual(self.state["roadmap_cursor"]["phase_id"], "DIAGNOSTICO_AUTOMACAO_GATE")
        self.assertIsNone(self.state["roadmap_cursor"]["authorized_by"])

    def test_fsm_proxy_accepts_current_lapidarium_route(self):
        sections = self.module._parse_roadmap_sections(self.roadmap)
        active = [section for section in sections if section["phase_id"] == self.state["current_phase_id"]]
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0]["status"], "CLOSED")
        self.assertEqual(active[0]["next_phase"], "DIAGNOSTICO_AUTOMACAO_GATE")

        errors = self.module.validate_fsm_proxy(self.state, self.roadmap)
        self.assertEqual(errors, [])

    def test_fsm_proxy_rejects_null_next_phase_without_cursor(self):
        state = json.loads(json.dumps(self.state))
        state.pop("roadmap_cursor", None)
        state["next_phase"] = None
        errors = self.module.validate_fsm_proxy(state, self.roadmap)
        self.assertTrue(any("FSM_PROXY #2" in error for error in errors))

    def test_boot_freshness_matches_state_sha(self):
        errors = self.module.validate_boot_freshness(self.state, self.boot)
        self.assertEqual(errors, [])

    def test_cli_passes_current_repo(self):
        result = subprocess.run(
            ["python3", str(ROOT / "tools" / "acx_validate.py")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "pass")
        self.assertEqual(payload["phase_id"], "LAPIDARIUM_FASE_6_GUARDA_TRUE")
        self.assertEqual(payload["roadmap_cursor"]["state"], "CANDIDATE")


if __name__ == "__main__":
    unittest.main()
