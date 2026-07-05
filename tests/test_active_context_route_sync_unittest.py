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
            ROOT / "tools" / "acx_validate.py",
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
        self.assertEqual(state["phase_id"], "LAPIDARIUM_FASE_6_GUARDA_TRUE")
        self.assertEqual(state["current_phase_id"], "LAPIDARIUM_FASE_6_GUARDA_TRUE")
        self.assertEqual(state["previous_phase_id"], "LAPIDARIUM_FASE_5_SELO_TRUE")
        self.assertEqual(state["phase_class"], "governance_repair")
        self.assertEqual(state["status"], "lapidarium_fase6_guarda_true_pass")
        self.assertIsNone(state["next_phase"])
        self.assertIsNone(state["active_next_phase"])
        self.assertIsNone(state["active_next_phase_class"])
        self.assertFalse(state["next_phase_authorized_by_operator"])
        self.assertEqual(state["latest_completed_phase"], "Lapidarium True — Fase 6: Guarda")
        self.assertEqual(state["latest_completed_status"], "lapidarium_fase6_guarda_true_pass")
        self.assertIsNone(state["current_live_route"]["active_next_phase"])
        self.assertIsNone(state["current_live_route"]["active_next_phase_class"])
        self.assertEqual(state["current_live_route"]["current_status"], "lapidarium_fase6_guarda_true_pass")
        self.assertEqual(state["current_live_route"]["status"], "lapidarium_fase6_guarda_true_pass")
        self.assertEqual(state["current_live_route"]["latest_completed_phase"], "Lapidarium True — Fase 6: Guarda")
        self.assertEqual(state["current_live_route"]["latest_completed_status"], "lapidarium_fase6_guarda_true_pass")
        self.assertIsNone(state["next_action"]["phase"])
        self.assertIsNone(state["next_action"]["phase_class"])
        self.assertEqual(state["next_action"]["status"], "lapidarium_fase6_guarda_true_pass")
        self.assertFalse(state["next_action"]["planning_only"])
        self.assertFalse(state["next_action"]["review_only"])
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
