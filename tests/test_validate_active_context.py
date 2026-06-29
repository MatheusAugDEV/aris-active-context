import hashlib
import json
import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


def _load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_validator_passes():
    r = subprocess.run(
        ["python3", "scripts/validate_active_context_state.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_validator_reports_lapidarium_cursor_activation_summary():
    r = subprocess.run(
        ["python3", "scripts/validate_active_context_state.py"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    summary = json.loads(r.stdout)
    assert summary["phase_id"] == "LAPIDARIUM"
    assert summary["next_phase"] == "LAPIDARIUM_FASE_2_CONSOLIDACAO_ARQUIVOS"
    assert summary["governance_gate_streak"] == 0


def test_fixture_absence_passes():
    r = subprocess.run(
        ["python3", "scripts/assert_no_unauthorized_fixtures.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_boundary_c_schema_no_longer_requires_markdown_mirror_routes():
    schema = json.loads(Path("ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
    artifact_routes = schema["properties"]["artifact_routes"]
    properties = artifact_routes["properties"]
    required = set(artifact_routes["required"])

    for key in (
        "current_state_mirror",
        "next_action_mirror",
        "context_index_mirror",
        "phase_ledger_history",
        "anti_corruption_contract",
    ):
        assert key not in properties
        assert key not in required


class BoundaryCContractTests(unittest.TestCase):
    def test_schema_no_longer_requires_markdown_mirror_routes(self):
        schema = json.loads(Path("ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
        artifact_routes = schema["properties"]["artifact_routes"]
        properties = artifact_routes["properties"]
        required = set(artifact_routes["required"])

        for key in (
            "current_state_mirror",
            "next_action_mirror",
            "context_index_mirror",
            "phase_ledger_history",
            "anti_corruption_contract",
        ):
            self.assertNotIn(key, properties)
            self.assertNotIn(key, required)


def test_schema_covers_live_active_context_shape():
    schema = json.loads(Path("ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
    state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))

    assert state["active_context_version"] in schema["properties"]["active_context_version"]["enum"]
    assert state["schema_version"] in schema["properties"]["schema_version"]["enum"]
    assert set(state) <= set(schema["properties"])
    assert set(schema["required"]) <= set(state)

    artifact_routes = schema["properties"]["artifact_routes"]
    assert set(artifact_routes["properties"]) == set(state["artifact_routes"])
    assert set(artifact_routes["required"]) == set(state["artifact_routes"])

    versioning_contract = schema["properties"]["versioning_contract"]["properties"]
    assert set(state["versioning_contract"]) <= set(versioning_contract)


def test_benchuix_track_is_non_executable_and_ready_for_operator_review():
    state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
    benchuix_track = state["benchuix_track"]

    assert benchuix_track["status"] == "operator_review_pending"
    assert benchuix_track["roadmap_path"] == "Benchuix_roadmap.md"
    assert benchuix_track["roadmap_hash"] == "e0588eca8af0c0c083f7607cc903c06dedd6511423a838458674b50359b160e5"
    assert benchuix_track["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_track["latest_candidate_decision"] == "READY_FOR_OPERATOR_REVIEW"
    assert benchuix_track["schema_tracking_repair_required"] is True
    assert benchuix_track["schema_tracking_repair_status"] == "completed"
    assert benchuix_track["trilha_lock_active"] is True
    assert benchuix_track["operator_gate_decision"] == "accepted"
    assert benchuix_track["operator_gate_scope"] == "BENCHUIX-00_AND_00R"
    assert benchuix_track["operator_gate_commit_sha"] == "73870715dd0d74bc0757b845d34d430b70d94867"
    assert benchuix_track["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_track["standing_candidate_authorization_active"] is True
    assert benchuix_track["standing_candidate_authorization_scope"] == "BENCHUIX-08_THROUGH_CRISOL_CANDIDATE_ONLY"
    assert benchuix_track["standing_candidate_authorization_artifact"] == "artifacts/benchuix/standing_authorization_packet.json"
    assert benchuix_track["standing_candidate_authorization_real_locks_opened"] is False
    assert benchuix_track["repeated_operator_ritual_required_for_next_candidate_phases"] is False
    for key in (
        "execution_authorized",
        "product_authorized",
        "production_authorized",
        "real_apply_authorized",
        "runtime_integration_allowed",
        "secrets_access_authorized",
    ):
        assert benchuix_track[key] is False

    assert Path("artifacts/benchuix/02_access_model.md").exists()
    assert Path("artifacts/benchuix/02_surface_inventory.json").exists()
    assert Path("artifacts/benchuix/02_surfaces_diagram.mmd").exists()
    assert Path("artifacts/benchuix/03_design_system_spec.md").exists()
    assert Path("artifacts/benchuix/03_design_tokens_candidate.json").exists()
    assert Path("artifacts/benchuix/03_component_inventory.json").exists()
    assert Path("artifacts/benchuix/04_service_blueprint.md").exists()
    assert Path("artifacts/benchuix/04_journey_maps.md").exists()
    assert Path("artifacts/benchuix/05_hoje_spec.md").exists()
    assert Path("artifacts/benchuix/05_today_summary_card_spec.json").exists()
    assert Path("artifacts/benchuix/06_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/06_onboarding_spec.md").exists()
    assert Path("artifacts/benchuix/06_time_to_first_preview_protocol.json").exists()
    assert Path("artifacts/benchuix/06_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/06_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/07_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/07_business_profile_spec.md").exists()
    assert Path("artifacts/benchuix/07_business_profile_form.json").exists()
    assert Path("artifacts/benchuix/07_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/07_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/standing_authorization_packet.json").exists()
    assert Path("artifacts/benchuix/standing_authorization_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/standing_authorization_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/08_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/08_playbooks_catalog.md").exists()
    assert Path("artifacts/benchuix/08_vertical_template_matrix.json").exists()
    assert Path("artifacts/benchuix/08_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/08_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/09_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/09_automation_editor.md").exists()
    assert Path("artifacts/benchuix/09_create_automation_flow.json").exists()
    assert Path("artifacts/benchuix/09_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/09_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/10_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/10_simulation_spec.md").exists()
    assert Path("artifacts/benchuix/10_isolation_proof.md").exists()
    assert Path("artifacts/benchuix/10_preview_simulation_protocol.json").exists()
    assert Path("artifacts/benchuix/10_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/10_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/11_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/11_approval_inbox_spec.md").exists()
    assert Path("artifacts/benchuix/11_risk_taxonomy.json").exists()
    assert Path("artifacts/benchuix/11_permission_language_matrix.json").exists()
    assert Path("artifacts/benchuix/11_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/11_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/12_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/12_execution_state_machine.json").exists()
    assert Path("artifacts/benchuix/12_state_microcopy_matrix.json").exists()
    assert Path("artifacts/benchuix/12_execution_states_spec.md").exists()
    assert Path("artifacts/benchuix/12_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/12_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/13_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/13_automations_list_spec.md").exists()
    assert Path("artifacts/benchuix/13_automation_list_state_model.json").exists()
    assert Path("artifacts/benchuix/13_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/13_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/14_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/14_history_ledger_spec.md").exists()
    assert Path("artifacts/benchuix/14_evidence_receipt_spec.md").exists()
    assert Path("artifacts/benchuix/14_history_receipt_protocol.json").exists()
    assert Path("artifacts/benchuix/14_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/14_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/15_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/15_rollback_spec.md").exists()
    assert Path("artifacts/benchuix/15_recovery_decision_tree.json").exists()
    assert Path("artifacts/benchuix/15_recovery_copy_matrix.json").exists()
    assert Path("artifacts/benchuix/15_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/15_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/16_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/16_failure_library.md").exists()
    assert Path("artifacts/benchuix/16_degraded_mode_spec.md").exists()
    assert Path("artifacts/benchuix/16_failure_degraded_protocol.json").exists()
    assert Path("artifacts/benchuix/16_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/16_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/17_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/17_mobile_companion_spec.md").exists()
    assert Path("artifacts/benchuix/17_pwa_cache_policy.json").exists()
    assert Path("artifacts/benchuix/17_mobile_degraded_state_matrix.json").exists()
    assert Path("artifacts/benchuix/17_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/17_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/18_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/18_permissions_matrix.json").exists()
    assert Path("artifacts/benchuix/18_role_based_views.md").exists()
    assert Path("artifacts/benchuix/18_permission_language_matrix.json").exists()
    assert Path("artifacts/benchuix/18_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/18_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/19_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/19_advanced_dashboard_spec.md").exists()
    assert Path("artifacts/benchuix/19_dashboard_widget_inventory.json").exists()
    assert Path("artifacts/benchuix/19_actionable_kpi_matrix.json").exists()
    assert Path("artifacts/benchuix/19_dashboard_state_latency_budget.json").exists()
    assert Path("artifacts/benchuix/19_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/19_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/20_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/20_ux_copy_system.md").exists()
    assert Path("artifacts/benchuix/20_forbidden_terms.txt").exists()
    assert Path("artifacts/benchuix/20_trust_language_translation_matrix.json").exists()
    assert Path("artifacts/benchuix/20_risk_failure_permission_copy_matrix.json").exists()
    assert Path("artifacts/benchuix/20_receipt_rollback_cost_copy_examples.md").exists()
    assert Path("artifacts/benchuix/20_jargon_scan_report.json").exists()
    assert Path("artifacts/benchuix/20_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/20_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/21_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/21_accessibility_wcag22_mapping.json").exists()
    assert Path("artifacts/benchuix/21_accessibility_audit_report.md").exists()
    assert Path("artifacts/benchuix/21_critical_flow_accessibility_matrix.json").exists()
    assert Path("artifacts/benchuix/21_keyboard_screen_reader_mobile_matrix.json").exists()
    assert Path("artifacts/benchuix/21_focus_target_status_motion_matrix.json").exists()
    assert Path("artifacts/benchuix/21_accessibility_gap_severity_matrix.json").exists()
    assert Path("artifacts/benchuix/21_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/21_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/22_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/22_performance_slo_matrix.json").exists()
    assert Path("artifacts/benchuix/22_visual_regression_report.md").exists()
    assert Path("artifacts/benchuix/22_web_vitals_report.md").exists()
    assert Path("artifacts/benchuix/22_visual_state_coverage_matrix.json").exists()
    assert Path("artifacts/benchuix/22_mobile_p75_measurement_method.json").exists()
    assert Path("artifacts/benchuix/22_bundle_budget_matrix.json").exists()
    assert Path("artifacts/benchuix/22_benchuix21_gap_resolution_matrix.json").exists()
    assert Path("artifacts/benchuix/22_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/22_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/23_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/23_competitor_source_ledger.json").exists()
    assert Path("artifacts/benchuix/23_competitive_task_matrix.md").exists()
    assert Path("artifacts/benchuix/23_task_benchmark_scoring_rubric.json").exists()
    assert Path("artifacts/benchuix/23_competitor_task_coverage_matrix.json").exists()
    assert Path("artifacts/benchuix/23_aris_implication_gap_ledger.json").exists()
    assert Path("artifacts/benchuix/23_marketing_claim_filter_report.json").exists()
    assert Path("artifacts/benchuix/23_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/23_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/24_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/24_metrics_scorecard.json").exists()
    assert Path("artifacts/benchuix/24_measurement_plan.md").exists()
    assert Path("artifacts/benchuix/24_heart_to_aris_mapping.json").exists()
    assert Path("artifacts/benchuix/24_metric_thresholds_and_calibration_plan.json").exists()
    assert Path("artifacts/benchuix/24_raw_data_contract.json").exists()
    assert Path("artifacts/benchuix/24_benchuix23_gap_to_metric_matrix.json").exists()
    assert Path("artifacts/benchuix/24_vanity_metric_rejection_report.json").exists()
    assert Path("artifacts/benchuix/24_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/24_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/25_operator_opening_source.json").exists()
    assert Path("artifacts/benchuix/25_usability_test_protocol.md").exists()
    assert Path("artifacts/benchuix/25_task_success_matrix.json").exists()
    assert Path("artifacts/benchuix/25_usability_severity_rubric.json").exists()
    assert Path("artifacts/benchuix/25_participant_profile_matrix.json").exists()
    assert Path("artifacts/benchuix/25_synthetic_test_data_pack.json").exists()
    assert Path("artifacts/benchuix/25_task_scenario_script.md").exists()
    assert Path("artifacts/benchuix/25_observation_and_raw_data_schema.json").exists()
    assert Path("artifacts/benchuix/25_benchuix24_metric_to_task_matrix.json").exists()
    assert Path("artifacts/benchuix/25_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/25_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/25_operator_gate_decision.json").exists()
    assert Path("artifacts/benchuix/25_gate_blocker_reconciliation.json").exists()
    assert Path("artifacts/benchuix/25_to_26_candidate_admission_packet.json").exists()
    assert Path("artifacts/benchuix/26_candidate_opening_source.json").exists()
    assert Path("artifacts/benchuix/26_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/26_demo_scripts.md").exists()
    assert Path("artifacts/benchuix/26_demo_sandbox_spec.md").exists()
    assert Path("artifacts/benchuix/26_demo_timing_matrix.json").exists()
    assert Path("artifacts/benchuix/26_demo_synthetic_data_pack.json").exists()
    assert Path("artifacts/benchuix/26_demo_evidence_receipt_examples.json").exists()
    assert Path("artifacts/benchuix/26_demo_value_message_matrix.json").exists()
    assert Path("artifacts/benchuix/26_demo_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/26_demo_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/26_operator_gate_decision.json").exists()
    assert Path("artifacts/benchuix/26_to_27_candidate_admission_packet.json").exists()
    assert Path("artifacts/benchuix/27_candidate_opening_source.json").exists()
    assert Path("artifacts/benchuix/27_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27_product_gap_ledger.json").exists()
    assert Path("artifacts/benchuix/27_anti_theater_rules.json").exists()
    assert Path("artifacts/benchuix/27_crisol_handoff.md").exists()
    assert Path("artifacts/benchuix/27_gap_destination_matrix.json").exists()
    assert Path("artifacts/benchuix/27_benchuix_closure_summary.md").exists()
    assert Path("artifacts/benchuix/27_validation_evidence.json").exists()
    assert Path("artifacts/benchuix/27_no_real_execution_attestation_final.json").exists()
    assert Path("artifacts/benchuix/27A_visual_sandbox_contract.md").exists()
    assert Path("artifacts/benchuix/27A_visual_screen_map.json").exists()
    assert Path("artifacts/benchuix/27A_visual_state_machine.json").exists()
    assert Path("artifacts/benchuix/27A_visual_component_contract.json").exists()
    assert Path("artifacts/benchuix/27A_visual_scenario_pack.json").exists()
    assert Path("artifacts/benchuix/27A_visual_copy_contract.md").exists()
    assert Path("artifacts/benchuix/27A_visual_test_criteria.json").exists()
    assert Path("artifacts/benchuix/27A_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27A_validation_evidence.json").exists()

    benchuix_27a_validation = json.loads(Path("artifacts/benchuix/27A_validation_evidence.json").read_text(encoding="utf-8"))
    assert benchuix_27a_validation["candidate_tracking_preserved"]["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_27a_validation["candidate_tracking_preserved"]["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_27a_validation["candidate_tracking_preserved"]["next_phase"] is None
    assert benchuix_27a_validation["candidate_tracking_preserved"]["active_next_phase"] is None
    assert benchuix_27a_validation["candidate_tracking_preserved"]["crisol_admitted"] is False
    assert benchuix_27a_validation["candidate_tracking_preserved"]["live_route_opened"] is False

    benchuix_27a_no_real = json.loads(Path("artifacts/benchuix/27A_no_real_execution_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27a_no_real["Project_ARIS_changed"] is False
    assert benchuix_27a_no_real["package_manager_executed"] is False
    assert benchuix_27a_no_real["react_executable_created"] is False
    assert benchuix_27a_no_real["crisol_admitted"] is False
    assert benchuix_27a_no_real["all_real_locks_remain_false"] is True
    assert Path("artifacts/benchuix/visual_sandbox_static").is_dir()
    assert Path("artifacts/benchuix/visual_sandbox_static/README.md").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/index.html").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/App.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/domain/stateMachine.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/domain/invariants.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/components/contract/ActionContractCard.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/components/shell/SandboxBadge.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/screens/TodayScreen.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/screens/ApproveScreen.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/screens/HistoryScreen.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/screens/RollbackScreen.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/screens/DegradedScreen.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/data/scenarios/barbearia.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/data/scenarios/mercado.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/data/scenarios/escritorio.js").exists()
    assert Path("artifacts/benchuix/visual_sandbox_static/src/tests/stateMachine.test.js").exists()
    assert Path("artifacts/benchuix/27B_react_static_prototype_manifest.json").exists()
    assert Path("artifacts/benchuix/27B_static_boundary_report.md").exists()
    assert Path("artifacts/benchuix/27B_visual_static_test_plan.json").exists()
    assert Path("artifacts/benchuix/27B_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27B_validation_evidence.json").exists()
    assert not Path("artifacts/benchuix/visual_sandbox_static/package.json").exists()
    assert not Path("artifacts/benchuix/visual_sandbox_static/node_modules").exists()

    benchuix_27b_manifest = json.loads(Path("artifacts/benchuix/27B_react_static_prototype_manifest.json").read_text(encoding="utf-8"))
    assert benchuix_27b_manifest["candidate_only"] is True
    assert benchuix_27b_manifest["synthetic_only"] is True
    assert benchuix_27b_manifest["no_build"] is True
    assert benchuix_27b_manifest["package_manager_executed"] is False
    assert benchuix_27b_manifest["package_json_created"] is False
    assert benchuix_27b_manifest["node_modules_created"] is False
    assert benchuix_27b_manifest["preview_run"] is False
    assert benchuix_27b_manifest["crisol_admitted"] is False
    assert benchuix_27b_manifest["live_route_opened"] is False

    benchuix_27b_validation = json.loads(Path("artifacts/benchuix/27B_validation_evidence.json").read_text(encoding="utf-8"))
    assert benchuix_27b_validation["candidate_tracking_preserved"]["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_27b_validation["candidate_tracking_preserved"]["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_27b_validation["candidate_tracking_preserved"]["next_phase"] is None
    assert benchuix_27b_validation["candidate_tracking_preserved"]["active_next_phase"] is None

    benchuix_27b_no_real = json.loads(Path("artifacts/benchuix/27B_no_real_execution_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27b_no_real["Project_ARIS_changed"] is False
    assert benchuix_27b_no_real["runtime_executed"] is False
    assert benchuix_27b_no_real["preview_executed"] is False
    assert benchuix_27b_no_real["package_manager_executed"] is False
    assert benchuix_27b_no_real["package_json_created"] is False
    assert benchuix_27b_no_real["node_modules_created"] is False
    assert benchuix_27b_no_real["crisol_opened"] is False
    assert benchuix_27b_no_real["all_real_locks_remain_false"] is True

    assert Path("artifacts/benchuix/27C_visual_synthetic_test_matrix.json").exists()
    assert Path("artifacts/benchuix/27C_scenario_comprehension_protocol.md").exists()
    assert Path("artifacts/benchuix/27C_visual_static_coverage_audit.json").exists()
    assert Path("artifacts/benchuix/27C_visual_usability_severity_rubric.json").exists()
    assert Path("artifacts/benchuix/27C_expected_observation_schema.json").exists()
    assert Path("artifacts/benchuix/27C_visual_test_fixture_review.json").exists()
    assert Path("artifacts/benchuix/27C_preview_readiness_boundary.md").exists()
    assert Path("artifacts/benchuix/27C_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27C_validation_evidence.json").exists()

    benchuix_27c_matrix = json.loads(Path("artifacts/benchuix/27C_visual_synthetic_test_matrix.json").read_text(encoding="utf-8"))
    assert benchuix_27c_matrix["phase_id"] == "BENCHUIX-27C"
    assert benchuix_27c_matrix["candidate_only"] is True
    assert benchuix_27c_matrix["synthetic_only"] is True
    assert benchuix_27c_matrix["preview_executed"] is False
    assert benchuix_27c_matrix["browser_executed"] is False
    assert benchuix_27c_matrix["real_user_testing_executed"] is False
    assert {scenario["scenario_id"] for scenario in benchuix_27c_matrix["scenarios"]} == {
        "barbearia_after_hours_vip_exception",
        "mercado_suspected_refund_declined",
        "escritorio_attachment_intercepted",
    }
    for scenario in benchuix_27c_matrix["scenarios"]:
        assert set(scenario["required_user_understanding"]) == {
            "will_do_understood",
            "will_not_do_understood",
            "risk_understood",
            "approval_requirement_understood",
            "evidence_visible",
            "rollback_or_compensation_understood",
            "no_real_state_touched_understood",
        }

    benchuix_27c_rubric = json.loads(Path("artifacts/benchuix/27C_visual_usability_severity_rubric.json").read_text(encoding="utf-8"))
    assert set(benchuix_27c_rubric["severities"]) == {"S1_BLOCKER", "S2_MAJOR", "S3_MINOR", "S4_POLISH"}

    benchuix_27c_observation = json.loads(Path("artifacts/benchuix/27C_expected_observation_schema.json").read_text(encoding="utf-8"))
    assert benchuix_27c_observation["fixed_values"]["synthetic_only"] is True
    assert benchuix_27c_observation["fixed_values"]["real_user"] is False

    benchuix_27c_validation = json.loads(Path("artifacts/benchuix/27C_validation_evidence.json").read_text(encoding="utf-8"))
    assert benchuix_27c_validation["candidate_tracking_preserved"]["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_27c_validation["candidate_tracking_preserved"]["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_27c_validation["candidate_tracking_preserved"]["next_phase"] is None
    assert benchuix_27c_validation["candidate_tracking_preserved"]["active_next_phase"] is None
    assert benchuix_27c_validation["context_hash_scope"] == (
        "ACTIVE_CONTEXT_SCHEMA.json hash is scoped to schema.properties.benchuix_track only; "
        "ACTIVE_CONTEXT_STATE.json hash is scoped to state.properties.benchuix_track only; "
        "serialized with json.dumps(sort_keys=True, separators=(',', ':'))."
    )

    schema = json.loads(Path("ACTIVE_CONTEXT_SCHEMA.json").read_text(encoding="utf-8"))
    expected_schema_hash = hashlib.sha256(
        json.dumps(schema["properties"]["benchuix_track"], sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert benchuix_27c_validation["context_hashes"]["ACTIVE_CONTEXT_SCHEMA.json"] == expected_schema_hash

    state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))
    expected_state_hash = hashlib.sha256(
        json.dumps(state["benchuix_track"], sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert benchuix_27c_validation["context_hashes"]["ACTIVE_CONTEXT_STATE.json"] == expected_state_hash

    benchuix_27c_no_real = json.loads(Path("artifacts/benchuix/27C_no_real_execution_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27c_no_real["Project_ARIS_changed"] is False
    assert benchuix_27c_no_real["runtime_executed"] is False
    assert benchuix_27c_no_real["preview_executed"] is False
    assert benchuix_27c_no_real["browser_executed"] is False
    assert benchuix_27c_no_real["localhost_opened"] is False
    assert benchuix_27c_no_real["package_manager_executed"] is False
    assert benchuix_27c_no_real["package_json_created"] is False
    assert benchuix_27c_no_real["node_modules_created"] is False
    assert benchuix_27c_no_real["real_user_testing_executed"] is False
    assert benchuix_27c_no_real["crisol_opened"] is False
    assert benchuix_27c_no_real["all_real_locks_remain_false"] is True

    assert Path("artifacts/benchuix/27D_local_static_preview_operator_runbook.md").exists()
    assert Path("artifacts/benchuix/27D_operator_visual_observation_sheet.json").exists()
    assert Path("artifacts/benchuix/27D_preview_boundary_attestation.json").exists()
    assert Path("artifacts/benchuix/27D_static_preview_preflight_checklist.json").exists()
    assert Path("artifacts/benchuix/27D_manual_preview_result_schema.json").exists()
    assert Path("artifacts/benchuix/27D_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27D_validation_evidence.json").exists()

    benchuix_27d_observation_sheet = json.loads(Path("artifacts/benchuix/27D_operator_visual_observation_sheet.json").read_text(encoding="utf-8"))
    assert benchuix_27d_observation_sheet["phase_id"] == "BENCHUIX-27D"
    assert benchuix_27d_observation_sheet["preview_executed_by_codex"] is False
    assert {scenario["scenario_id"] for scenario in benchuix_27d_observation_sheet["scenarios"]} == {
        "barbearia_after_hours_vip_exception",
        "mercado_suspected_refund_declined",
        "escritorio_attachment_intercepted",
    }
    for scenario in benchuix_27d_observation_sheet["scenarios"]:
        assert scenario["observed_understanding"] is None
        assert scenario["notes"] is None
        assert scenario["synthetic_only"] is True
        assert scenario["real_user"] is False

    benchuix_27d_preview_boundary = json.loads(Path("artifacts/benchuix/27D_preview_boundary_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27d_preview_boundary["preview_mode"] == "manual_operator_local_file_only"
    assert benchuix_27d_preview_boundary["codex_browser_opened"] is False
    assert benchuix_27d_preview_boundary["localhost_allowed"] is False
    assert benchuix_27d_preview_boundary["package_manager_allowed"] is False
    assert benchuix_27d_preview_boundary["api_allowed"] is False
    assert benchuix_27d_preview_boundary["crisol_admitted"] is False

    benchuix_27d_preflight = json.loads(Path("artifacts/benchuix/27D_static_preview_preflight_checklist.json").read_text(encoding="utf-8"))
    assert benchuix_27d_preflight["package_json_absent"] is True
    assert benchuix_27d_preflight["node_modules_absent"] is True
    assert benchuix_27d_preflight["no_network_patterns_confirmed"] is True
    assert benchuix_27d_preflight["sandbox_badge_scan_confirmed"] is True
    assert benchuix_27d_preflight["state_touched_false_confirmed"] is True
    assert benchuix_27d_preflight["blockers"] == []

    benchuix_27d_result_schema = json.loads(Path("artifacts/benchuix/27D_manual_preview_result_schema.json").read_text(encoding="utf-8"))
    assert benchuix_27d_result_schema["fixed_values"]["no_real_data_used"] is True
    assert benchuix_27d_result_schema["fixed_values"]["no_runtime_used"] is True
    assert benchuix_27d_result_schema["fixed_values"]["no_api_used"] is True
    assert benchuix_27d_result_schema["fixed_values"]["no_product_claim"] is True

    benchuix_27d_validation = json.loads(Path("artifacts/benchuix/27D_validation_evidence.json").read_text(encoding="utf-8"))
    assert benchuix_27d_validation["candidate_tracking_preserved"]["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_27d_validation["candidate_tracking_preserved"]["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_27d_validation["candidate_tracking_preserved"]["next_phase"] is None
    assert benchuix_27d_validation["candidate_tracking_preserved"]["active_next_phase"] is None

    benchuix_27d_no_real = json.loads(Path("artifacts/benchuix/27D_no_real_execution_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27d_no_real["Project_ARIS_changed"] is False
    assert benchuix_27d_no_real["runtime_executed"] is False
    assert benchuix_27d_no_real["preview_executed_by_codex"] is False
    assert benchuix_27d_no_real["browser_executed_by_codex"] is False
    assert benchuix_27d_no_real["localhost_opened"] is False
    assert benchuix_27d_no_real["package_manager_executed"] is False
    assert benchuix_27d_no_real["package_json_created"] is False
    assert benchuix_27d_no_real["node_modules_created"] is False
    assert benchuix_27d_no_real["real_user_testing_executed"] is False
    assert benchuix_27d_no_real["crisol_opened"] is False
    assert benchuix_27d_no_real["all_real_locks_remain_false"] is True

    assert Path("artifacts/benchuix/visual_sandbox_static/index_file_preview.html").exists()
    assert Path("artifacts/benchuix/27E_file_preview_compatibility_report.md").exists()
    assert Path("artifacts/benchuix/27E_file_preview_boundary_attestation.json").exists()
    assert Path("artifacts/benchuix/27E_no_real_execution_attestation.json").exists()
    assert Path("artifacts/benchuix/27E_validation_evidence.json").exists()

    preview_file_27e = Path("artifacts/benchuix/visual_sandbox_static/index_file_preview.html").read_text(encoding="utf-8")
    assert 'type="module"' not in preview_file_27e
    assert "import " not in preview_file_27e
    assert "fetch(" not in preview_file_27e
    assert "XMLHttpRequest" not in preview_file_27e
    assert "WebSocket" not in preview_file_27e
    assert "SandboxBadge" in preview_file_27e
    assert "barbearia_after_hours_vip_exception" in preview_file_27e
    assert "mercado_suspected_refund_declined" in preview_file_27e
    assert "escritorio_attachment_intercepted" in preview_file_27e
    assert "Estado real tocado?" in preview_file_27e

    benchuix_27e_boundary = json.loads(Path("artifacts/benchuix/27E_file_preview_boundary_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27e_boundary["phase_id"] == "BENCHUIX-27E"
    assert benchuix_27e_boundary["single_file_preview_created"] is True
    assert benchuix_27e_boundary["module_imports_removed_for_preview"] is True
    assert benchuix_27e_boundary["type_module_removed_for_preview"] is True
    assert benchuix_27e_boundary["localhost_required"] is False
    assert benchuix_27e_boundary["package_manager_required"] is False
    assert benchuix_27e_boundary["crisol_admitted"] is False

    benchuix_27e_validation = json.loads(Path("artifacts/benchuix/27E_validation_evidence.json").read_text(encoding="utf-8"))
    assert benchuix_27e_validation["candidate_tracking_preserved"]["current_candidate_phase"] == "BENCHUIX-27"
    assert benchuix_27e_validation["candidate_tracking_preserved"]["candidate_next_phase_after_operator_gate"] == "CRISOL"
    assert benchuix_27e_validation["candidate_tracking_preserved"]["next_phase"] is None
    assert benchuix_27e_validation["candidate_tracking_preserved"]["active_next_phase"] is None

    benchuix_27e_no_real = json.loads(Path("artifacts/benchuix/27E_no_real_execution_attestation.json").read_text(encoding="utf-8"))
    assert benchuix_27e_no_real["Project_ARIS_changed"] is False
    assert benchuix_27e_no_real["runtime_executed"] is False
    assert benchuix_27e_no_real["preview_executed_by_codex"] is False
    assert benchuix_27e_no_real["browser_executed_by_codex"] is False
    assert benchuix_27e_no_real["localhost_opened"] is False
    assert benchuix_27e_no_real["package_manager_executed"] is False
    assert benchuix_27e_no_real["package_json_created"] is False
    assert benchuix_27e_no_real["node_modules_created"] is False
    assert benchuix_27e_no_real["real_user_testing_executed"] is False
    assert benchuix_27e_no_real["crisol_opened"] is False
    assert benchuix_27e_no_real["all_real_locks_remain_false"] is True


def test_ci_terminal_state_green_requires_all_terminal_success():
    module = _load_validator_module()
    assert (
        module.classify_ci_terminal_state(
            [
                {"status": "completed", "conclusion": "success"},
                {"status": "completed", "conclusion": "success"},
            ]
        )
        == "CI_GREEN_CONFIRMED"
    )


def test_ci_terminal_state_pending_blocks_final_pass():
    module = _load_validator_module()
    assert (
        module.classify_ci_terminal_state(
            [
                {"status": "completed", "conclusion": "success"},
                {"status": "in_progress", "conclusion": ""},
            ]
        )
        == "CI_PENDING"
    )


def test_ci_terminal_state_failed_detects_terminal_failure():
    module = _load_validator_module()
    assert (
        module.classify_ci_terminal_state(
            [
                {"status": "completed", "conclusion": "success"},
                {"status": "completed", "conclusion": "failure"},
            ]
        )
        == "CI_FAILED"
    )


def test_minimum_deliverable_blocks_inf_mat_pass_without_real_fixture_dirs():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-MAT-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-MAT-01 without fixture dirs")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_inf_bot_pass_without_log():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-BOT-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-BOT-01 without execution log")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_inf_minos_pass_without_verdict():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-MINOS-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-MINOS-01 without verdict json")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_purg_pass_without_finding():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "PURG-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block PURG-01 without finding json")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_core_01_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_01_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CORE-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CORE-01 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_core_01_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_core_01_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "0e935f41830101c391905611473e52e883d36a26",
                        "supply_chain_ci": {"conclusion": "success"},
                        "deliverables": {
                            "uv_lock_exists": True,
                            "pip_audit_gate_exists": True,
                            "sbom_exists": True,
                            "uv_bootstrap_exists": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_01_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CORE-01",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_core_02_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_02_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CORE-02",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CORE-02 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_core_02_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_core_02_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "46910e0fda3fc64a19818ad80f39813227b53922",
                        "core_public_api_ci": {"conclusion": "success"},
                        "deliverables": {
                            "research_basis_exists": True,
                            "snapshot_before_exists": True,
                            "snapshot_after_exists": True,
                            "import_stability_report_exists": True,
                            "explicit_all_created_or_verified": True,
                            "protocols_created_or_verified": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_02_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CORE-02",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_01_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_01_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-01 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_01_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_01_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
                        "backend_baseline_ci": {"conclusion": "success"},
                        "deliverables": {
                            "fastapi_app_exists": True,
                            "health_check_exists": True,
                            "ready_check_exists": True,
                            "jwt_auth_exists": True,
                            "api_key_auth_exists": True,
                            "tenant_isolation_exists": True,
                            "slowapi_rate_limit_exists": True,
                            "backend_tests_exist": True,
                            "backend_artifacts_exist": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_01_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-01",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_02_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_02_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-02",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-02 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_02_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_02_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "b2fdc3c994342a42a84823fa15615c931f1bc00e",
                        "mcp_runtime_sandbox_ci": {"conclusion": "success"},
                        "deliverables": {
                            "mcp_runtime_package_exists": True,
                            "stdio_ban_exists": True,
                            "sandbox_spec_exists": True,
                            "policy_pre_dispatch_exists": True,
                            "kill_switch_exists": True,
                            "rollback_contract_exists": True,
                            "audit_event_exists": True,
                            "mcp_runtime_tests_exist": True,
                            "mcp_runtime_artifacts_exist": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_02_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-02",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_03_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_03_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-03",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-03 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_03_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_03_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "b1d175f8b0d1105a9d05f6ddcab082c71d6f6b3e",
                        "runtime_public_api_ci": {"conclusion": "success"},
                        "deliverables": {
                            "runtime_package_exists": True,
                            "runtime_public_api_documented": True,
                            "runtime_public_api_contract_exists": True,
                            "runtime_facade_exists": True,
                            "runtime_modes_enforced": True,
                            "runtime_policy_bridge_exists": True,
                            "runtime_audit_hashing_exists": True,
                            "public_api_drift_ratified": True,
                            "runtime_tests_exist": True,
                            "runtime_artifacts_exist": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_03_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-03",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_04_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_04_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-04",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-04 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_04_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_04_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "b6044982c31e0861b481605c40bef673b249f351",
                        "product_pilot_boundary_ci": {"conclusion": "success"},
                        "deliverables": {
                            "product_boundary_package_exists": True,
                            "pilot_gates_defined": True,
                            "five_binary_gates_defined": True,
                            "lab_to_staging_to_pilot_workflow_defined": True,
                            "pilot_scope_contract_exists": True,
                            "evidence_bundle_contract_exists": True,
                            "pilot_runbook_contract_exists": True,
                            "pilot_risk_matrix_exists": True,
                            "non_authorization_statement_exists": True,
                            "product_pilot_tests_exist": True,
                            "product_pilot_artifacts_exist": True
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_04_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-04",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_05_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_05_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-05",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-05 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_05_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_05_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "973d49a24d58d4166acb95b40611be409c5d44df",
                        "advanced_supply_chain_ci": {"conclusion": "success"},
                        "deliverables": {
                            "supply_chain_package_exists": True,
                            "sbom_integrity_checker_exists": True,
                            "sbom_integrity_report_exists": True,
                            "attestation_envelope_exists": True,
                            "offline_signature_test_verification_exists": True,
                            "pypi_vulnerability_range_monitor_exists": True,
                            "pypi_vulnerability_range_scan_exists": True,
                            "aibom_prototype_exists": True,
                            "infernus_full_spec_exists": True,
                            "advanced_supply_chain_tests_exist": True,
                            "advanced_supply_chain_artifacts_exist": True
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_05_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-05",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_boot_receipt_blocks_when_operator_preferences_missing():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    try:
        module._warn_boot_receipt(
            {
                "last_boot_files_read": [
                    "ACTIVE_CONTEXT_STATE.json",
                    "AGENT_IDENTITY.md",
                    "ACTIVE_CONTEXT_SCHEMA.json",
                    "scripts/validate_active_context_state.py",
                    "ROADMAP_CANONICAL.md",
                    "MANDATORY_READ_FIRST_RULES.md",
                    "CURRENT_STATE.md",
                    "NEXT_ACTION.md",
                    "DECISION_LOCKS.md",
                ]
            }
        )
    except SystemExit as exc:
        assert exc.code == 1
    else:
        raise AssertionError("boot receipt should block when OPERATOR_PREFERENCES.md is missing")


def test_prompt_preference_allows_clean_prompt_only_transition():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is True


def test_prompt_preference_does_not_override_operator_transition():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="operator",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is False


def test_prompt_preference_does_not_override_manual_lock():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=True,
    ) is False


def test_prompt_preference_requires_previous_phase_pass():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=False,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is False


def test_prompt_preference_requires_green_ci_and_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=False,
        validator_green=True,
        manual_authorization_required=False,
    ) is False
    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=False,
        manual_authorization_required=False,
    ) is False


def test_transition_table_contains_inf_full_07_canonroadmap_successor():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    row = module._get_transition_row("INF-FULL-07", "pass")
    assert row is not None
    assert row["next_phase_id"] == "PURG-PRE"
    assert row["advance_mode"] == "operator"
    assert row["next_phase_class"] == "purgatorium_full_authority_materialization"


def test_state_separates_historical_and_planned_scenario_counts():
    state = json.loads(Path("ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))

    assert state["current_phase_id"] == "LAPIDARIUM"
    assert state["scenario_count"] == 13
    assert state["fixture_scenario_count"] == 13
    assert state["current_phase_planned_scenario_count"] == 16
    assert state["current_phase_planned_bot_count"] == 16
    assert state["current_phase_mutation_family_count"] == 10
    assert state["current_phase_oracle_count"] == 9
    assert state["next_phase"] == "LAPIDARIUM_FASE_2_CONSOLIDACAO_ARQUIVOS"
    assert state["active_next_phase"] == "LAPIDARIUM_FASE_2_CONSOLIDACAO_ARQUIVOS"
    assert state["active_next_phase_class"] == "lapidarium_remediation"
    assert state["next_phase_authorized_by_operator"] is True
    assert state["current_status"] == "lapidarium_phase_1_5_test_isolation_active"
    assert state["latest_completed_phase"] == "Lapidarium Fase 1.5 - Isolamento de Testes"
    assert state["latest_completed_status"] == "lapidarium_phase_1_5_test_isolation_active"
    assert state["latest_completed_project_commit_sha"] == "7883af5a32c629026bfc6dc15ebee4ebbcadd295"
    assert state["latest_completed_ci_state"] == "CI_GREEN_CONFIRMED"
    assert state["latest_completed_next_recommended_step"] == "Nenhuma transição definida. Aguardando instrução do operador."
    assert state["active_context_remote_main_reflects_latest_phase"] is True
    assert state["permanent_active_update_rule_installed"] is True
