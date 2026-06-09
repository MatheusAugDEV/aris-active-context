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

    def test_current_route_tracks_if11_minos_final_verdict_closure_sync(self):
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["latest_completed_phase"], "IF-11 Minos Final Verdict + Closure")
        self.assertEqual(state["latest_completed_status"], "if11_minos_final_verdict_closure_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "6312302ea45b72ddc310b2b33f56245be65b99dc")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "execute_purg_pre_canonical_authority_materialization",
        )
        self.assertEqual(state["next_phase"], "PURG-PRE")
        self.assertEqual(state["active_next_phase"], "PURG-PRE")
        self.assertEqual(state["active_next_phase_class"], "purgatorium_full_authority_materialization")
        self.assertTrue(state["next_phase_authorized_by_operator"])
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
        self.assertEqual(state["status"], "purg_pre_route_admission_pass")
        self.assertFalse(state["latest_completed_no_execution"]["wave_executed"])
        self.assertFalse(state["latest_completed_no_execution"]["bot_executed"])
        self.assertEqual(state["latest_completed_no_execution"]["execution_scope"], "artifact_only_final_verdict_closure")
        self.assertEqual(state["latest_completed_no_execution"]["source_phase_verified"], "IF-10 Purgatorium Handoff Graph")
        self.assertEqual(state["latest_completed_no_execution"]["source_status_verified"], "if10_purgatorium_handoff_graph_pass")
        self.assertEqual(state["latest_completed_no_execution"]["source_project_sha_verified_by_packet"], "57106d9780af7a807bd58ea6039af3a7b1b23701")
        self.assertEqual(state["latest_completed_no_execution"]["source_active_context_pre_sync_sha_verified_by_packet"], "767138de3fb2b0484fca6be25657e08c21107574")
        self.assertEqual(state["latest_completed_no_execution"]["source_active_context_sync_sha_verified_by_packet"], "7755a1506e6981d3f1c5b3534c7217112a12b960")
        self.assertTrue(state["latest_completed_no_execution"]["if11_materialization_performed"])
        self.assertTrue(state["latest_completed_no_execution"]["minos_mechanical_report_created"])
        self.assertTrue(state["latest_completed_no_execution"]["minos_semantic_report_created"])
        self.assertTrue(state["latest_completed_no_execution"]["operator_cosignature_created"])
        self.assertTrue(state["latest_completed_no_execution"]["anti_theater_meta_audit_created"])
        self.assertTrue(state["latest_completed_no_execution"]["infernus_closure_created"])
        self.assertTrue(state["latest_completed_no_execution"]["closure_manifest_created"])
        self.assertTrue(state["latest_completed_no_execution"]["final_evidence_index_created"])
        self.assertTrue(state["latest_completed_no_execution"]["purgatorium_readiness_summary_created"])
        self.assertTrue(state["latest_completed_no_execution"]["next_phase_boundary_created"])
        self.assertEqual(state["latest_completed_no_execution"]["source_root_manifest_sha256"], "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660")
        self.assertEqual(state["latest_completed_no_execution"]["source_graph_sha256"], "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1")
        self.assertEqual(state["latest_completed_no_execution"]["validated_handoff_ids"], ["IF09-FIND-001"])
        self.assertEqual(state["latest_completed_no_execution"]["contextual_candidate_ids"], ["IF09-FIND-002"])
        self.assertEqual(state["latest_completed_no_execution"]["excluded_invalid_ids"], ["IF09-FIND-003"])
        self.assertEqual(state["latest_completed_no_execution"]["supporting_observation_ids"], ["IF09-OBS-001"])
        self.assertEqual(state["latest_completed_no_execution"]["minos_mechanical_verdict"], "pass")
        self.assertEqual(state["latest_completed_no_execution"]["minos_semantic_verdict"], "pass")
        self.assertEqual(state["latest_completed_no_execution"]["anti_theater_verdict"], "pass")
        self.assertEqual(state["latest_completed_no_execution"]["operator_cosignature_status"], "pending_operator_review")
        self.assertEqual(state["latest_completed_no_execution"]["infernus_closure_status"], "closed_with_purgatorium_handoff_ready")
        self.assertTrue(state["latest_completed_no_execution"]["purgatorium_handoff_ready"])
        self.assertFalse(state["latest_completed_no_execution"]["bedrock_ready"])
        self.assertFalse(state["latest_completed_no_execution"]["product_ready"])
        self.assertFalse(state["latest_completed_no_execution"]["real_execution_authorized"])
        self.assertTrue(state["latest_completed_no_execution"]["macro_transition_preserved"])
        self.assertEqual(state["latest_completed_no_execution"]["current_phase_id_preserved"], "INF-FULL-07")
        self.assertEqual(state["latest_completed_no_execution"]["active_next_phase_preserved"], "IF-08")
        self.assertEqual(state["latest_completed_no_execution"]["active_next_phase_class_preserved"], "infernus_full_execution")
        self.assertEqual(
            state["latest_completed_no_execution"]["warnings"],
            [
                "operator_cosignature_pending_review_not_execution_authorization",
                "purgatorium_handoff_ready_does_not_mean_finding_resolved",
            ],
        )
        self.assertEqual(state["latest_completed_no_execution"]["blocking_findings_count"], 0)
        self.assertFalse(state["latest_completed_no_execution"]["real_audio_capture_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["real_stt_tts_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["microphone_access_allowed"])
        self.assertFalse(state["latest_completed_no_execution"]["voice_clone_or_impersonation_allowed"])
        self.assertFalse(state["authorization"]["real_dry_run_execution_authorized"])
        self.assertFalse(state["authorization"]["real_apply_authorized"])
        self.assertFalse(state["authorization"]["runtime_integration_allowed"])

    def test_schema_allows_purgatorium_route_class(self):
        schema = json.loads((ROOT / "ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
        self.assertIn(
            "purgatorium_full_authority_materialization",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_full_authority_materialization",
            schema["properties"]["current_live_route"]["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_full_authority_materialization",
            schema["properties"]["next_action"]["properties"]["phase_class"]["enum"],
        )

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

    def test_if11_validator_skips_external_project_artifacts_when_absent(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original_paths = {
                "IF11_PROJECT_DECISION_PATH": module.IF11_PROJECT_DECISION_PATH,
                "IF11_PROJECT_SUMMARY_PATH": module.IF11_PROJECT_SUMMARY_PATH,
                "IF11_PROJECT_REPORT_PATH": module.IF11_PROJECT_REPORT_PATH,
                "IF11_PROJECT_MECHANICAL_PATH": module.IF11_PROJECT_MECHANICAL_PATH,
                "IF11_PROJECT_SEMANTIC_PATH": module.IF11_PROJECT_SEMANTIC_PATH,
                "IF11_PROJECT_OPERATOR_COSIGNATURE_PATH": module.IF11_PROJECT_OPERATOR_COSIGNATURE_PATH,
                "IF11_PROJECT_ANTI_THEATER_PATH": module.IF11_PROJECT_ANTI_THEATER_PATH,
                "IF11_PROJECT_CLOSURE_PATH": module.IF11_PROJECT_CLOSURE_PATH,
                "IF11_PROJECT_MANIFEST_PATH": module.IF11_PROJECT_MANIFEST_PATH,
                "IF11_PROJECT_FINAL_EVIDENCE_PATH": module.IF11_PROJECT_FINAL_EVIDENCE_PATH,
                "IF11_PROJECT_READINESS_PATH": module.IF11_PROJECT_READINESS_PATH,
                "IF11_PROJECT_BOUNDARY_PATH": module.IF11_PROJECT_BOUNDARY_PATH,
                "IF11_PROJECT_DOC_PATH": module.IF11_PROJECT_DOC_PATH,
            }
            try:
                for name in original_paths:
                    setattr(module, name, missing)
                module._check_if11_minos_final_verdict_closure_artifacts(state)
            finally:
                for name, value in original_paths.items():
                    setattr(module, name, value)

    def test_purg_pre_authority_materialization_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "project_mirror" / "docs" / "purgatorium_full" / "purgatorium_roadmapcanon.md").exists())
        self.assertTrue((ROOT / "excludent" / "infernus" / "roadmaps" / "infernus_full_canonroadmap.md").exists())
        module._check_purg_pre_canonical_authority_materialization_artifacts(state)

    def test_purg_operator_review_packet_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_operator_review_packet_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_route_admission_schema_gap_matrix.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_route_admission_validator_gap_matrix.json").exists())
        module._check_purg_operator_review_packet_artifacts(state)

    def test_purg_pre_route_admission_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_pre_route_admission_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_pre_route_admission_no_real_execution_attestation.json").exists())
        module._check_purg_pre_route_admission_artifacts(state)

    def test_route_admission_validator_requires_decision_artifact(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original = module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = missing
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_route_admission_artifacts(state)
            finally:
                module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = original

    def test_route_admission_validator_rejects_forbidden_flag(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg_pre_route_admission_decision.json").read_text(encoding="utf-8"))
            decision["runtime_executed"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_route_admission_artifacts(state)
            finally:
                module.PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = original

    def test_route_admission_validator_rejects_bedrock_or_product_ready(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            attestation = json.loads((ROOT / "artifacts" / "purgatorium" / "purg_pre_route_admission_no_real_execution_attestation.json").read_text(encoding="utf-8"))
            attestation["bedrock_ready"] = True
            temp_path = Path(tmpdir) / "attestation.json"
            temp_path.write_text(json.dumps(attestation), encoding="utf-8")
            original = module.PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH
            try:
                module.PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_route_admission_artifacts(state)
            finally:
                module.PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = original

    def test_route_admission_validator_rejects_purg_00_pass_claim(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            report = (ROOT / "artifacts" / "purgatorium" / "purg_pre_route_admission_report.md").read_text(encoding="utf-8")
            temp_path = Path(tmpdir) / "report.md"
            temp_path.write_text(report + "\nPURG-00 | pass\n", encoding="utf-8")
            original = module.PURG_PRE_ROUTE_ADMISSION_REPORT_PATH
            try:
                module.PURG_PRE_ROUTE_ADMISSION_REPORT_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_route_admission_artifacts(state)
            finally:
                module.PURG_PRE_ROUTE_ADMISSION_REPORT_PATH = original


if __name__ == "__main__":
    unittest.main()
