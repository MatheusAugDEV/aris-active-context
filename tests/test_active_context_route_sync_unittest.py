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

    def test_current_route_tracks_inf_revalidation_execution_packet_sync(self):
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["phase_id"], "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET")
        self.assertEqual(state["current_phase_id"], "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET")
        self.assertEqual(state["previous_phase_id"], "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET")
        self.assertEqual(state["phase_class"], "governance_repair")
        self.assertEqual(state["latest_completed_phase"], "IF09 Closure Milestone Mirror Sanity Packet")
        self.assertEqual(state["latest_completed_status"], "if09_closure_milestone_mirror_sanity_pass")
        self.assertEqual(state["latest_completed_project_commit_sha"], "7883af5a32c629026bfc6dc15ebee4ebbcadd295")
        self.assertEqual(
            state["latest_completed_next_recommended_step"],
            "Nenhuma transição definida. Aguardando instrução do operador.",
        )
        self.assertIsNone(state["next_phase"])
        self.assertIsNone(state["active_next_phase"])
        self.assertIsNone(state["active_next_phase_class"])
        self.assertFalse(state["next_phase_authorized_by_operator"])
        self.assertTrue(state["route_amendment_authorized_by_operator"])
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
        self.assertEqual(state["decision"], "pass")
        self.assertEqual(state["status"], "if09_closure_milestone_mirror_sanity_pass")
        self.assertEqual(state["target_finding_id"], "IF09-FIND-001")
        self.assertEqual(state["target_finding_status"], "closed")
        self.assertTrue(state["finding_closed"])
        self.assertTrue(state["remediation_proven"])
        self.assertEqual(
            state["closure_basis"],
            "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface",
        )
        self.assertEqual(state["current_live_route"]["decision"], "pass")
        self.assertEqual(state["current_live_route"]["status"], "if09_closure_milestone_mirror_sanity_pass")
        self.assertIsNone(state["current_live_route"]["active_next_phase"])
        self.assertIsNone(state["current_live_route"]["active_next_phase_class"])
        self.assertFalse(state["current_live_route"]["next_phase_execution_authorization"])
        self.assertIsNone(state["next_action"]["phase"])
        self.assertIsNone(state["next_action"]["phase_class"])
        self.assertIn("Nenhuma transição definida. Aguardando instrução do operador.", state["next_action"]["notes"][-1])
        self.assertEqual(
            state["purg00_source_gap_terminal_blocker"]["status"],
            "purg00_source_gap_terminal_blocker_operator_source_required",
        )
        self.assertTrue(state["purg00_source_gap_terminal_blocker"]["repeated_search_prevented"])
        self.assertEqual(
            state["purg00_route_amendment_terminal_wait_state"]["status"],
            "purg00_route_amendment_terminal_wait_state_operator_source_required",
        )
        self.assertTrue(state["purg00_route_amendment_terminal_wait_state"]["live_route_closed"])
        self.assertFalse(state["purg00_route_amendment_terminal_wait_state"]["purg01_open_authorized"])
        self.assertTrue(state["purg00_route_amendment_terminal_wait_state"]["source_packet_supplied"])
        self.assertTrue(state["purg00_route_amendment_terminal_wait_state"]["source_packet_validated"])
        self.assertEqual(
            state["purg00_operator_source_packet_intake"]["status"],
            "purg00_operator_source_packet_intake_pass",
        )
        self.assertTrue(state["purg00_operator_source_packet_intake"]["source_packet_validated"])
        self.assertEqual(
            state["purg00_operator_source_packet_intake"]["source_packet_sha256"],
            "6f616556d0a31ebba8e0bd647ccfd014f1955127856cc20d2deee2f6d7111e72",
        )
        self.assertFalse(state["purg00_operator_source_packet_intake"]["purg01_open_authorized"])
        self.assertEqual(
            state["purg01_route_admission_review"]["status"],
            "purg01_route_admission_review_pass",
        )
        self.assertEqual(
            state["purg01_route_admission_review"]["candidate_phase"],
            "PURG-01",
        )
        self.assertEqual(
            state["purg01_route_admission_review"]["candidate_phase_class"],
            "purgatorium_route_admission",
        )
        self.assertFalse(state["purg01_route_admission_review"]["purg01_open_authorized"])
        self.assertEqual(
            state["purg01_route_admission"]["status"],
            "purg01_route_admission_pass",
        )
        self.assertTrue(state["purg01_route_admission"]["operator_authorized"])
        self.assertTrue(state["purg01_route_admission"]["purg01_open_authorized"])
        self.assertFalse(state["purg01_route_admission"]["purg01_triage_authorized"])
        self.assertFalse(state["purg01_route_admission"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_triage_readiness_review"]["status"],
            "purg01_triage_readiness_review_pass",
        )
        self.assertTrue(state["purg01_triage_readiness_review"]["triage_planning_candidate_created"])
        self.assertFalse(state["purg01_triage_readiness_review"]["purg01_triage_authorized"])
        self.assertFalse(state["purg01_triage_readiness_review"]["triage_execution_authorized"])
        self.assertFalse(state["purg01_triage_readiness_review"]["finding_fix_authorized"])
        self.assertFalse(state["purg01_triage_readiness_review"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_triage_readiness_review"]["candidate_next_step"],
            "prepare_purg01_triage_planning_gate",
        )
        self.assertEqual(
            state["purg01_triage_readiness_review"]["next_recommended_step"],
            "prepare_purg01_triage_planning_gate",
        )
        self.assertEqual(
            state["purg01_triage_planning_gate"]["status"],
            "purg01_triage_planning_gate_pass",
        )
        self.assertEqual(
            state["purg01_triage_planning_gate"]["target_finding_id"],
            "IF09-FIND-001",
        )
        self.assertTrue(state["purg01_triage_planning_gate"]["triage_plan_created"])
        self.assertTrue(state["purg01_triage_planning_gate"]["triage_authorization_request_candidate_created"])
        self.assertFalse(state["purg01_triage_planning_gate"]["purg01_triage_authorized"])
        self.assertFalse(state["purg01_triage_planning_gate"]["triage_execution_authorized"])
        self.assertFalse(state["purg01_triage_planning_gate"]["finding_fix_authorized"])
        self.assertFalse(state["purg01_triage_planning_gate"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_triage_planning_gate"]["next_recommended_step"],
            "request_operator_authorization_for_purg01_triage",
        )
        self.assertEqual(
            state["purg01_triage_authorization_gate"]["status"],
            "purg01_triage_authorization_gate_pass",
        )
        self.assertTrue(state["purg01_triage_authorization_gate"]["operator_authorized"])
        self.assertEqual(
            state["purg01_triage_authorization_gate"]["operator_authorization_text"],
            "Autorizo PURG-01 triage.",
        )
        self.assertEqual(
            state["purg01_triage_authorization_gate"]["operator_authorization_scope"],
            "purg01_triage_authorization_only_not_fix_not_real_execution",
        )
        self.assertTrue(state["purg01_triage_authorization_gate"]["purg01_triage_authorized"])
        self.assertFalse(state["purg01_triage_authorization_gate"]["triage_execution_authorized"])
        self.assertFalse(state["purg01_triage_authorization_gate"]["finding_fix_authorized"])
        self.assertFalse(state["purg01_triage_authorization_gate"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_triage_authorization_gate"]["next_recommended_step"],
            "prepare_purg01_controlled_triage_execution_gate",
        )
        self.assertEqual(
            state["purg01_controlled_triage_execution_gate"]["status"],
            "purg01_controlled_triage_execution_gate_pass",
        )
        self.assertEqual(
            state["purg01_controlled_triage_execution_gate"]["required_fields_missing"],
            [],
        )
        self.assertEqual(
            state["purg01_controlled_triage_execution_gate"]["next_recommended_step"],
            "execute_purg01_controlled_triage_artifact_only",
        )
        self.assertTrue(state["purg01_controlled_triage_execution_gate"]["purg01_triage_authorized"])
        self.assertFalse(state["purg01_controlled_triage_execution_gate"]["triage_execution_authorized"])
        self.assertFalse(state["purg01_controlled_triage_execution_gate"]["finding_fix_authorized"])
        self.assertFalse(state["purg01_controlled_triage_execution_gate"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_controlled_triage_artifact_only_execution"]["status"],
            "purg01_controlled_triage_artifact_only_execution_pass",
        )
        self.assertEqual(
            state["purg01_controlled_triage_artifact_only_execution"]["execution_mode"],
            "artifact_only",
        )
        self.assertFalse(state["purg01_controlled_triage_artifact_only_execution"]["triage_execution_real"])
        self.assertFalse(state["purg01_controlled_triage_artifact_only_execution"]["finding_fix_executed"])
        self.assertFalse(state["purg01_controlled_triage_artifact_only_execution"]["remediation_apply_executed"])
        self.assertFalse(state["purg01_controlled_triage_artifact_only_execution"]["real_execution_authorized"])
        self.assertEqual(
            state["purg01_controlled_triage_artifact_only_execution"]["next_recommended_step_preserved"],
            "execute_purg01_controlled_triage_artifact_only",
        )
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
            "purgatorium_full_intake",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_route_admission",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_full_intake",
            schema["properties"]["current_live_route"]["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_route_admission",
            schema["properties"]["current_live_route"]["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_full_intake",
            schema["properties"]["next_action"]["properties"]["phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_route_admission",
            schema["properties"]["next_action"]["properties"]["phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_track_a_main_merge_execution",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "purgatorium_post_merge_validation",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn(
            "infernus_revalidation_adjudication_or_closure",
            schema["properties"]["active_next_phase_class"]["enum"],
        )
        self.assertIn("route_amendment_authorized_by_operator", schema["properties"])
        self.assertIn("repeat_source_search_without_new_primary_source_forbidden", schema["properties"])
        self.assertIn("purg00_route_amendment_terminal_wait_state", schema["properties"])
        self.assertIn("purg00_operator_source_packet_intake", schema["properties"])
        self.assertIn("purg01_route_admission_review", schema["properties"])
        self.assertIn("purg01_route_admission", schema["properties"])
        self.assertIn("purg01_triage_readiness_review", schema["properties"])
        self.assertIn("purg01_triage_planning_gate", schema["properties"])
        self.assertIn("purg01_triage_authorization_gate", schema["properties"])
        self.assertIn("purg01_controlled_triage_execution_gate", schema["properties"])
        self.assertIn("purg01_controlled_triage_artifact_only_execution", schema["properties"])
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_7_change_summary"]["type"], "string")
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_8_change_summary"]["type"], "string")
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_9_change_summary"]["type"], "string")
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_10_change_summary"]["type"], "string")
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_11_change_summary"]["type"], "string")
        self.assertEqual(schema["properties"]["versioning_contract"]["properties"]["schema_3_12_change_summary"]["type"], "string")

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

    def test_purg_pre_authority_execution_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_pre_canonical_authority_execution_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg_pre_no_purg00_attestation.json").exists())
        module._check_purg_pre_authority_execution_artifacts(state)

    def test_purg00_operator_review_packet_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_operator_review_packet_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_not_opened_attestation.json").exists())
        module._check_purg00_operator_review_packet_artifacts(state)

    def test_transition_table_contains_purg_pre_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("PURG-PRE", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "PURG-00")
        self.assertEqual(row["next_phase_class"], "purgatorium_full_intake")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_purg04_track_a_main_merge_execution_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("PURG04_TRACK_A_MAIN_MERGE_EXECUTION", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET")
        self.assertEqual(row["next_phase_class"], "purgatorium_post_merge_validation")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_purg04_track_a_post_merge_validation_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET")
        self.assertEqual(row["next_phase_class"], "purgatorium_route_admission")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_purg_residual_risk_carry_forward_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF_REVALIDATION_ROUTE_ADMISSION_PACKET")
        self.assertEqual(row["next_phase_class"], "infernus_revalidation_route_admission")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_inf_revalidation_route_admission_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF_REVALIDATION_READINESS_PACKET")
        self.assertEqual(row["next_phase_class"], "infernus_revalidation_readiness")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_inf_revalidation_readiness_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF_REVALIDATION_READINESS_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET")
        self.assertEqual(row["next_phase_class"], "infernus_revalidation_operator_authorization")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_inf_revalidation_operator_authorization_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF_REVALIDATION_EXECUTION_PACKET")
        self.assertEqual(row["next_phase_class"], "infernus_revalidation_execution")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_inf_revalidation_execution_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF_REVALIDATION_EXECUTION_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET")
        self.assertEqual(row["next_phase_class"], "infernus_revalidation_adjudication_or_closure")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_contains_if09_closure_mirror_sanity_successor(self):
        module = self._load_validator_module()
        row = module._get_transition_row("INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "pass")
        self.assertIsNotNone(row)
        self.assertEqual(row["next_phase_id"], "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET")
        self.assertEqual(row["next_phase_class"], "governance_repair")
        self.assertEqual(row["advance_mode"], "operator")

    def test_transition_table_has_no_successor_for_if09_closure_mirror_sanity_packet(self):
        module = self._load_validator_module()
        self.assertIsNone(module._get_transition_row("IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET", "pass"))

    def test_purg00_route_admission_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_no_real_execution_attestation_v2.json").exists())
        module._check_purg00_route_admission_artifacts(state)

    def test_purg00_handoff_intake_artifacts_validate(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_handoff_intake_authority_lock_decision.json").exists())
        self.assertTrue((ROOT / "artifacts" / "purgatorium" / "purg00_data_gap_matrix.json").exists())
        module._check_purg00_handoff_intake_authority_lock_artifacts(state)

    def test_purg00_handoff_intake_validator_skips_external_project_hash_recheck_when_absent(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original_paths = {
                "IF09_PROJECT_ROOT_MANIFEST_PATH": module.IF09_PROJECT_ROOT_MANIFEST_PATH,
                "IF10_PROJECT_GRAPH_PATH": module.IF10_PROJECT_GRAPH_PATH,
            }
            try:
                for name in original_paths:
                    setattr(module, name, missing)
                module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                for name, value in original_paths.items():
                    setattr(module, name, value)

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

    def test_authority_execution_validator_requires_decision_artifact(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original = module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH
            try:
                module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = missing
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_authority_execution_artifacts(state)
            finally:
                module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = original

    def test_authority_execution_validator_rejects_purg00_opened(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            attestation = json.loads((ROOT / "artifacts" / "purgatorium" / "purg_pre_no_purg00_attestation.json").read_text(encoding="utf-8"))
            attestation["purg_00_opened"] = True
            temp_path = Path(tmpdir) / "attestation.json"
            temp_path.write_text(json.dumps(attestation), encoding="utf-8")
            original = module.PURG_PRE_NO_PURG00_ATTESTATION_PATH
            try:
                module.PURG_PRE_NO_PURG00_ATTESTATION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_authority_execution_artifacts(state)
            finally:
                module.PURG_PRE_NO_PURG00_ATTESTATION_PATH = original

    def test_authority_execution_validator_rejects_candidate_promotion(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg_pre_canonical_authority_execution_decision.json").read_text(encoding="utf-8"))
            decision["candidate_promoted"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH
            try:
                module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_authority_execution_artifacts(state)
            finally:
                module.PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = original

    def test_authority_execution_validator_rejects_invalid_finding_remediation(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            matrix = json.loads((ROOT / "artifacts" / "purgatorium" / "purg_pre_handoff_source_reference_matrix.json").read_text(encoding="utf-8"))
            matrix["invalid_finding_remediated"] = True
            temp_path = Path(tmpdir) / "matrix.json"
            temp_path.write_text(json.dumps(matrix), encoding="utf-8")
            original = module.PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH
            try:
                module.PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg_pre_authority_execution_artifacts(state)
            finally:
                module.PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH = original

    def test_purg00_operator_review_validator_requires_decision_artifact(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original = module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH
            try:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = missing
                with self.assertRaises(SystemExit):
                    module._check_purg00_operator_review_packet_artifacts(state)
            finally:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = original

    def test_purg00_operator_review_validator_rejects_purg00_opened(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            attestation = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_not_opened_attestation.json").read_text(encoding="utf-8"))
            attestation["purg00_opened"] = True
            temp_path = Path(tmpdir) / "attestation.json"
            temp_path.write_text(json.dumps(attestation), encoding="utf-8")
            original = module.PURG00_NOT_OPENED_ATTESTATION_PATH
            try:
                module.PURG00_NOT_OPENED_ATTESTATION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_operator_review_packet_artifacts(state)
            finally:
                module.PURG00_NOT_OPENED_ATTESTATION_PATH = original

    def test_purg00_operator_review_validator_rejects_candidate_promotion(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_operator_review_packet_decision.json").read_text(encoding="utf-8"))
            decision["candidate_promoted"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH
            try:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_operator_review_packet_artifacts(state)
            finally:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = original

    def test_purg00_operator_review_validator_rejects_invalid_finding_remediation(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_operator_review_packet_decision.json").read_text(encoding="utf-8"))
            decision["invalid_finding_remediated"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH
            try:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_operator_review_packet_artifacts(state)
            finally:
                module.PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = original

    def test_purg00_route_admission_validator_requires_decision_artifact(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original = module.PURG00_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = missing
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = original

    def test_purg00_route_admission_validator_rejects_purg00_executed(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_decision.json").read_text(encoding="utf-8"))
            decision["purg00_executed"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = original

    def test_purg00_route_admission_validator_rejects_purg00_intake_executed(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            attestation = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_no_real_execution_attestation_v2.json").read_text(encoding="utf-8"))
            attestation["purg00_intake_executed"] = True
            temp_path = Path(tmpdir) / "attestation.json"
            temp_path.write_text(json.dumps(attestation), encoding="utf-8")
            original = module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = original

    def test_purg00_route_admission_validator_rejects_bedrock_or_product_ready(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            attestation = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_no_real_execution_attestation_v2.json").read_text(encoding="utf-8"))
            attestation["bedrock_ready"] = True
            temp_path = Path(tmpdir) / "attestation.json"
            temp_path.write_text(json.dumps(attestation), encoding="utf-8")
            original = module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = original

    def test_purg00_route_admission_validator_rejects_candidate_promotion(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_decision.json").read_text(encoding="utf-8"))
            decision["candidate_promoted"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = original

    def test_purg00_route_admission_validator_rejects_invalid_finding_remediation(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_route_admission_decision.json").read_text(encoding="utf-8"))
            decision["invalid_finding_remediated"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_ROUTE_ADMISSION_DECISION_PATH
            try:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_route_admission_artifacts(state)
            finally:
                module.PURG00_ROUTE_ADMISSION_DECISION_PATH = original

    def test_purg00_handoff_intake_validator_requires_decision_artifact(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            original = module.PURG00_HANDOFF_INTAKE_DECISION_PATH
            try:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = missing
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = original

    def test_purg00_handoff_intake_validator_rejects_finding_fix(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_handoff_intake_authority_lock_decision.json").read_text(encoding="utf-8"))
            decision["finding_fix_executed"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_HANDOFF_INTAKE_DECISION_PATH
            try:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = original

    def test_purg00_handoff_intake_validator_rejects_red_reproduction(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            no_fix = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_no_fix_attestation.json").read_text(encoding="utf-8"))
            no_fix["red_reproduction_executed"] = True
            temp_path = Path(tmpdir) / "no_fix.json"
            temp_path.write_text(json.dumps(no_fix), encoding="utf-8")
            original = module.PURG00_NO_FIX_ATTESTATION_PATH
            try:
                module.PURG00_NO_FIX_ATTESTATION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_NO_FIX_ATTESTATION_PATH = original

    def test_purg00_handoff_intake_validator_rejects_triage_execution(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            no_fix = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_no_fix_attestation.json").read_text(encoding="utf-8"))
            no_fix["triage_executed"] = True
            temp_path = Path(tmpdir) / "no_fix.json"
            temp_path.write_text(json.dumps(no_fix), encoding="utf-8")
            original = module.PURG00_NO_FIX_ATTESTATION_PATH
            try:
                module.PURG00_NO_FIX_ATTESTATION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_NO_FIX_ATTESTATION_PATH = original

    def test_purg00_handoff_intake_validator_rejects_candidate_promotion(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_handoff_intake_authority_lock_decision.json").read_text(encoding="utf-8"))
            decision["candidate_promoted"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_HANDOFF_INTAKE_DECISION_PATH
            try:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = original

    def test_purg00_handoff_intake_validator_rejects_invalid_finding_remediation(self):
        module = self._load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmpdir:
            decision = json.loads((ROOT / "artifacts" / "purgatorium" / "purg00_handoff_intake_authority_lock_decision.json").read_text(encoding="utf-8"))
            decision["invalid_finding_remediated"] = True
            temp_path = Path(tmpdir) / "decision.json"
            temp_path.write_text(json.dumps(decision), encoding="utf-8")
            original = module.PURG00_HANDOFF_INTAKE_DECISION_PATH
            try:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = temp_path
                with self.assertRaises(SystemExit):
                    module._check_purg00_handoff_intake_authority_lock_artifacts(state)
            finally:
                module.PURG00_HANDOFF_INTAKE_DECISION_PATH = original


if __name__ == "__main__":
    unittest.main()
