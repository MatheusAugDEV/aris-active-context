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

    def test_current_route_tracks_if08_w4_controlled_execution_sync(self):
        state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["latest_completed_phase"], "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution")
        self.assertEqual(state["latest_completed_status"], "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "c65888a2f587c35b4e38b16b50b917233bac8fa3")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution",
        )
        self.assertEqual(state["next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase_class"], "infernus_full_execution")
        self.assertTrue(state["next_phase_authorized_by_operator"])
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertTrue(state["next_action"]["review_only"])
        self.assertTrue(state["latest_completed_no_execution"]["wave_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["bot_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["w4_execution_performed"])
        self.assertEqual(state["latest_completed_no_execution"]["execution_scope"], "synthetic_isolated_lab_only")
        self.assertEqual(state["latest_completed_no_execution"]["synthetic_attack_cases_total"], 14)
        self.assertFalse(state["authorization"]["real_dry_run_execution_authorized"])
        self.assertFalse(state["authorization"]["real_apply_authorized"])
        self.assertFalse(state["authorization"]["runtime_integration_allowed"])


if __name__ == "__main__":
    unittest.main()
