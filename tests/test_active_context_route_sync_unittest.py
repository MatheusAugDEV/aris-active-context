import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ActiveContextRouteSyncTests(unittest.TestCase):
    def _load_validator_module(self):
        spec = importlib.util.spec_from_file_location(
            "validate_active_context_state",
            ROOT / "scripts" / "validate_active_context_state.py",
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
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["scenario_count"], 13)
        self.assertEqual(state["fixture_scenario_count"], 13)
        self.assertEqual(state["current_phase_planned_scenario_count"], 16)
        self.assertEqual(state["current_phase_planned_bot_count"], 16)
        self.assertEqual(state["current_phase_mutation_family_count"], 10)
        self.assertEqual(state["current_phase_oracle_count"], 9)

    def test_current_route_tracks_if10_purgatorium_handoff_graph_sync(self):
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["latest_completed_phase"], "IF-10 Purgatorium Handoff Graph")
        self.assertEqual(state["latest_completed_status"], "if10_purgatorium_handoff_graph_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "57106d9780af7a807bd58ea6039af3a7b1b23701")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "prepare_if11_minos_final_verdict_closure",
        )
        self.assertEqual(state["next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase"], "IF-08")
        self.assertEqual(state["active_next_phase_class"], "infernus_full_execution")
        self.assertTrue(state["next_phase_authorized_by_operator"])
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
        self.assertTrue(state["latest_completed_no_execution"]["wave_executed"])
        self.assertTrue(state["latest_completed_no_execution"]["bot_executed"])
        self.assertEqual(state["latest_completed_no_execution"]["execution_scope"], "artifact_only_causal_handoff_materialization")
        self.assertEqual(state["latest_completed_no_execution"]["source_phase_verified"], "IF-09 Evidence Bundle + Vulnerability Register")
        self.assertEqual(state["latest_completed_no_execution"]["source_status_verified"], "if09_evidence_bundle_vulnerability_register_pass")
        self.assertEqual(state["latest_completed_no_execution"]["source_project_sha_verified_by_packet"], "38b16edadce15ce8f2049bb3de8538bb921e344e")
        self.assertEqual(state["latest_completed_no_execution"]["source_active_context_sha_verified_by_packet"], "767138de3fb2b0484fca6be25657e08c21107574")
        self.assertTrue(state["latest_completed_no_execution"]["if10_materialization_performed"])
        self.assertTrue(state["latest_completed_no_execution"]["purgatorium_handoff_graph_v4_materialized"])
        self.assertTrue(state["latest_completed_no_execution"]["root_cause_candidates_created"])
        self.assertTrue(state["latest_completed_no_execution"]["remediation_tracks_created"])
        self.assertTrue(state["latest_completed_no_execution"]["regression_test_plan_created"])
        self.assertTrue(state["latest_completed_no_execution"]["revalidation_wave_plan_created"])
        self.assertTrue(state["latest_completed_no_execution"]["handoff_manifest_created"])
        self.assertEqual(state["latest_completed_no_execution"]["source_root_manifest_sha256"], "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660")
        self.assertTrue(state["latest_completed_no_execution"]["source_root_manifest_reference_verified"])
        self.assertEqual(state["latest_completed_no_execution"]["validated_handoff_ids"], ["IF09-FIND-001"])
        self.assertEqual(state["latest_completed_no_execution"]["contextual_candidate_ids"], ["IF09-FIND-002"])
        self.assertEqual(state["latest_completed_no_execution"]["excluded_invalid_ids"], ["IF09-FIND-003"])
        self.assertEqual(state["latest_completed_no_execution"]["supporting_observation_ids"], ["IF09-OBS-001"])
        self.assertEqual(state["latest_completed_no_execution"]["reproduction_unit_reference"], "IF09-REPRO-001")
        self.assertEqual(state["latest_completed_no_execution"]["replay_unit_reference"], "IF09-REPLAY-001")
        self.assertEqual(state["latest_completed_no_execution"]["mutation_unit_reference"], "IF09-MUT-001")
        self.assertEqual(state["latest_completed_no_execution"]["graph_node_count"], 9)
        self.assertEqual(state["latest_completed_no_execution"]["graph_edge_count"], 8)
        self.assertEqual(state["latest_completed_no_execution"]["node_type_counts"]["finding"], 1)
        self.assertEqual(state["latest_completed_no_execution"]["edge_type_counts"]["reproduced_by"], 2)
        self.assertEqual(state["latest_completed_no_execution"]["duplicate_node_ids_count"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["duplicate_edge_ids_count"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["dangling_edges_count"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["handoff_ids_missing_tracks_count"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["invalid_findings_with_remediation_count"], 0)
        self.assertEqual(state["latest_completed_no_execution"]["candidate_findings_promoted_without_evidence_count"], 0)
        self.assertTrue(state["latest_completed_no_execution"]["graph_integrity_verified"])
        self.assertTrue(state["latest_completed_no_execution"]["macro_transition_preserved"])
        self.assertEqual(state["latest_completed_no_execution"]["current_phase_id_preserved"], "INF-FULL-07")
        self.assertEqual(state["latest_completed_no_execution"]["active_next_phase_preserved"], "IF-08")
        self.assertEqual(state["latest_completed_no_execution"]["active_next_phase_class_preserved"], "infernus_full_execution")
        self.assertTrue(state["latest_completed_no_execution"]["w6_execution_performed"])
        self.assertFalse(state["latest_completed_no_execution"]["w6_real_execution_performed"])
        self.assertFalse(state["latest_completed_no_execution"]["real_audio_capture_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["real_stt_tts_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["microphone_access_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["voice_clone_or_impersonation_allowed"])
        self.assertFalse(state["authorization"]["real_dry_run_execution_authorized"])
        self.assertFalse(state["authorization"]["real_apply_authorized"])
        self.assertFalse(state["authorization"]["runtime_integration_allowed"])

    def test_if09_validator_skips_external_project_artifacts_when_absent(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original_paths = {
                "IF09_PROJECT_DECISION_PATH": module.IF09_PROJECT_DECISION_PATH,
                "IF09_PROJECT_SUMMARY_PATH": module.IF09_PROJECT_SUMMARY_PATH,
                "IF09_PROJECT_REPORT_PATH": module.IF09_PROJECT_REPORT_PATH,
                "IF09_PROJECT_ROOT_MANIFEST_PATH": module.IF09_PROJECT_ROOT_MANIFEST_PATH,
                "IF09_PROJECT_HASH_TREE_PATH": module.IF09_PROJECT_HASH_TREE_PATH,
                "IF09_PROJECT_CUSTODY_CHAIN_PATH": module.IF09_PROJECT_CUSTODY_CHAIN_PATH,
                "IF09_PROJECT_REPLAY_DIFF_PATH": module.IF09_PROJECT_REPLAY_DIFF_PATH,
                "IF09_PROJECT_MUTATION_SURVIVAL_PATH": module.IF09_PROJECT_MUTATION_SURVIVAL_PATH,
                "IF09_PROJECT_REGISTER_PATH": module.IF09_PROJECT_REGISTER_PATH,
                "IF09_PROJECT_DOC_PATH": module.IF09_PROJECT_DOC_PATH,
            }
            try:
                for name in original_paths:
                    setattr(module, name, missing)
                module._check_if09_evidence_bundle_vulnerability_register_artifacts(state)
            finally:
                for name, value in original_paths.items():
                    setattr(module, name, value)

    def test_if10_validator_skips_external_project_artifacts_when_absent(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original_paths = {
                "IF10_PROJECT_DECISION_PATH": module.IF10_PROJECT_DECISION_PATH,
                "IF10_PROJECT_SUMMARY_PATH": module.IF10_PROJECT_SUMMARY_PATH,
                "IF10_PROJECT_REPORT_PATH": module.IF10_PROJECT_REPORT_PATH,
                "IF10_PROJECT_GRAPH_PATH": module.IF10_PROJECT_GRAPH_PATH,
                "IF10_PROJECT_ROOT_CAUSE_PATH": module.IF10_PROJECT_ROOT_CAUSE_PATH,
                "IF10_PROJECT_REMEDIATION_PATH": module.IF10_PROJECT_REMEDIATION_PATH,
                "IF10_PROJECT_REGRESSION_PATH": module.IF10_PROJECT_REGRESSION_PATH,
                "IF10_PROJECT_REVALIDATION_PATH": module.IF10_PROJECT_REVALIDATION_PATH,
                "IF10_PROJECT_HANDOFF_MANIFEST_PATH": module.IF10_PROJECT_HANDOFF_MANIFEST_PATH,
                "IF10_PROJECT_DOC_PATH": module.IF10_PROJECT_DOC_PATH,
            }
            try:
                for name in original_paths:
                    setattr(module, name, missing)
                module._check_if10_purgatorium_handoff_graph_artifacts(state)
            finally:
                for name, value in original_paths.items():
                    setattr(module, name, value)


if __name__ == "__main__":
    unittest.main()
