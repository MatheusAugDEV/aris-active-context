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

    def test_current_route_tracks_if08_w5_post_sync_review_sync(self):
        state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["latest_completed_phase"], "IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision")
        self.assertEqual(state["latest_completed_status"], "if08_w5_post_sync_review_w6_readiness_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "e9dfae63206523f26fce5df907945952c7351ad5")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "prepare_if08_w6_final_audit_preflight_readiness",
        )
        self.assertEqual(state["next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase_class"], "infernus_full_execution")
        self.assertTrue(state["next_phase_authorized_by_operator"])
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
        self.assertFalse(state["latest_completed_no_execution"]["wave_executed"])
        self.assertFalse(state["latest_completed_no_execution"]["bot_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["w5_canonical_sync_verified"])
        self.assertTrue(state["latest_completed_no_execution"]["w5_metrics_verified"])
        self.assertTrue(state["latest_completed_no_execution"]["w5_artifacts_complete"])
        self.assertTrue(state["latest_completed_no_execution"]["w5_safety_attestation_verified"])
        self.assertEqual(state["latest_completed_no_execution"]["execution_scope"], "post_sync_review_only")
        self.assertEqual(state["latest_completed_no_execution"]["source_project_sha_verified_by_packet"], "5eb32158153bc5ff3db87d33c3c625f5b0df80fa")
        self.assertEqual(state["latest_completed_no_execution"]["source_active_context_sha_verified_by_packet"], "a89f90c691965a104c99964f3b256d08758605af")
        self.assertEqual(state["latest_completed_no_execution"]["previous_phase_verified"], "IF-08 W5 Business Chaos Controlled Execution")
        self.assertEqual(state["latest_completed_no_execution"]["previous_status_verified"], "if08_w5_business_chaos_controlled_execution_pass")
        self.assertEqual(state["latest_completed_no_execution"]["sirene_oracle_mode"], "synthetic_transcript_only")
        self.assertEqual(state["latest_completed_no_execution"]["w6_readiness_state"], "ready_for_preparation")
        self.assertTrue(state["latest_completed_no_execution"]["w6_preparation_allowed_next"])
        self.assertFalse(state["latest_completed_no_execution"]["w6_execution_performed"])
        self.assertFalse(state["latest_completed_no_execution"]["w6_execution_allowed"])
        self.assertEqual(state["latest_completed_no_execution"]["future_ttr_required"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["future_har_required"], 1.0)
        self.assertTrue(state["latest_completed_no_execution"]["minos_mechanical_required"])
        self.assertTrue(state["latest_completed_no_execution"]["minos_semantic_required"])
        self.assertTrue(state["latest_completed_no_execution"]["anti_theater_review_required"])
        self.assertEqual(state["latest_completed_no_execution"]["executor_bot_count"], 14)
        self.assertEqual(state["latest_completed_no_execution"]["synthetic_domain_count"], 7)
        self.assertEqual(state["latest_completed_no_execution"]["critical_coverage_cells_total"], 12)
        self.assertEqual(state["latest_completed_no_execution"]["critical_coverage_cells_passed"], 12)
        self.assertEqual(state["latest_completed_no_execution"]["critical_coverage_completion"], 1.0)
        self.assertEqual(state["latest_completed_no_execution"]["readiness_coverage"], 1.0)
        self.assertEqual(state["latest_completed_no_execution"]["business_scenarios_total"], 14)
        self.assertEqual(state["latest_completed_no_execution"]["business_scenarios_blocked_or_detected"], 14)
        self.assertFalse(state["latest_completed_no_execution"]["real_audio_capture_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["real_stt_tts_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["microphone_access_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["voice_clone_or_impersonation_allowed"])
        self.assertFalse(state["authorization"]["real_dry_run_execution_authorized"])
        self.assertFalse(state["authorization"]["real_apply_authorized"])
        self.assertFalse(state["authorization"]["runtime_integration_allowed"])


if __name__ == "__main__":
    unittest.main()
