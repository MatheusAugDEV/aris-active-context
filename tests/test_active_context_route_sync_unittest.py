import importlib.util
import json
import unittest
from pathlib import Path


class ActiveContextRouteSyncTests(unittest.TestCase):
    def _load_validator_module(self):
        spec = importlib.util.spec_from_file_location(
            "validate_active_context_state",
            Path("scripts/validate_active_context_state.py"),
        )
        module = importlib.util.module_from_spec(spec)
        self.assertIsNotNone(spec.loader)
        spec.loader.exec_module(module)
        return module

    def test_transition_table_contains_inf_full_04_canonroadmap_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF-FULL-04", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF-FULL-05")
        self.assertEqual(row["advance_mode"], "canonroadmap")

    def test_state_separates_historical_and_planned_counts(self):
        state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["scenario_count"], 13)
        self.assertEqual(state["fixture_scenario_count"], 13)
        self.assertEqual(state["current_phase_planned_scenario_count"], 16)
        self.assertEqual(state["current_phase_planned_bot_count"], 16)
        self.assertEqual(state["current_phase_mutation_family_count"], 10)
        self.assertEqual(state["current_phase_oracle_count"], 9)

    def test_current_route_tracks_if08_w4_post_sync_review_sync(self):
        state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["latest_completed_phase"], "IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision")
        self.assertEqual(state["latest_completed_status"], "if08_w4_post_sync_review_w5_readiness_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "d575b6f3c37c1ba411a2a0266efb9d04957234c0")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "prepare_if08_w5_business_chaos_preflight_readiness",
        )
        self.assertEqual(state["next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase_class"], "infernus_full_execution")
        self.assertTrue(state["next_phase_authorized_by_operator"])
        self.assertTrue(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
        self.assertTrue(state["latest_completed_no_execution"]["wave_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["bot_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["w4_execution_performed"])
        self.assertEqual(state["latest_completed_no_execution"]["execution_scope"], "synthetic_isolated_lab_only")
        self.assertEqual(state["latest_completed_no_execution"]["synthetic_attack_cases_total"], 14)
        self.assertEqual(state["latest_completed_no_execution"]["w5_readiness_state"], "ready_for_preparation")
        self.assertTrue(state["latest_completed_no_execution"]["w5_preparation_allowed_next"])
        self.assertFalse(state["latest_completed_no_execution"]["w5_execution_performed"])
        self.assertFalse(state["latest_completed_no_execution"]["w5_execution_allowed"])
        self.assertFalse(state["authorization"]["real_dry_run_execution_authorized"])
        self.assertFalse(state["authorization"]["real_apply_authorized"])
        self.assertFalse(state["authorization"]["runtime_integration_allowed"])


if __name__ == "__main__":
    unittest.main()
