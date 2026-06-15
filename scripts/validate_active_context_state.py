#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PROJECT_MIRROR_ROOT = ROOT / "project_mirror"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"
PROJECT_CHECKOUT_PRESENT = (PROJECT_ROOT / "main.py").exists() and (PROJECT_ROOT / "artifacts").exists()


def _resolve_project_relative(*parts: str) -> pathlib.Path:
    relative = pathlib.Path(*parts)
    for base in (PROJECT_ROOT, PROJECT_MIRROR_ROOT):
        candidate = base / relative
        if candidate.exists():
            return candidate
    return PROJECT_ROOT / relative


def _require_project_checkout_artifact(path: pathlib.Path, message: str) -> None:
    if PROJECT_CHECKOUT_PRESENT:
        _require(path.exists(), message)


ACB_CORE_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_01_project_evidence_2026_06_03.json"
ACB_CORE_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_02_project_evidence_2026_06_03.json"
ACB_CAP_01_OPERATOR_AUTH_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_operator_authorization_2026_06_03.json"
ACB_CAP_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_project_evidence_2026_06_03.json"
ACB_CAP_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_02_project_evidence_2026_06_03.json"
ACB_CAP_03_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_03_project_evidence_2026_06_03.json"
ACB_CAP_04_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_04_project_evidence_2026_06_03.json"
ACB_CAP_05_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_evidence_2026_06_05.json"
ACB_CAP_05_RESYNC_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_sha_resync_2026_06_06.json"
OPERATOR_PREFERENCES_PATH = ROOT / "archive" / "superseded" / "OPERATOR_PREFERENCES.md"
ARIS_BOOT_PATH = ROOT / "ARIS_BOOT.md"

# ── HISTORICAL POSITION CONSTANTS (DO NOT CHANGE — used by HISTORICAL_ARTIFACT checks) ──
# These values describe the state at the time historical artifacts were created.
# Changing them would break validation of immutable past artifacts.
EXPECTED_PHASE = "IF-11 Minos Final Verdict + Closure"
EXPECTED_PHASE_ID = "INF-FULL-07"
EXPECTED_PREVIOUS_PHASE = "IF-10 Purgatorium Handoff Graph"
EXPECTED_PREVIOUS_PHASE_ID = "INF-FULL-06"
EXPECTED_STATUS = "purg01_route_admission_pass"
EXPECTED_DECISION = "pass"
EXPECTED_CURRENT_STATUS = "if11_minos_final_verdict_closure_pass"
EXPECTED_SCHEMA_VERSION = "3.12"
EXPECTED_NEXT_PHASE_ID = "PURG-00"
EXPECTED_NEXT_PHASE_CLASS = "purgatorium_full_intake"
# ───────────────────────────────────────────────────────────────────────────────────────────
PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID = "PURG-01"
PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_CLASS = "purgatorium_route_admission"
PURG_PRE_LIVE_ROUTE_PHASE_ID = "PURG-PRE"
PURG_PRE_LIVE_ROUTE_PHASE_CLASS = "purgatorium_full_authority_materialization"
HISTORICAL_PRESERVED_NEXT_PHASE_ID = "IF-08"
HISTORICAL_PRESERVED_NEXT_PHASE_CLASS = "infernus_full_execution"
EXPECTED_NEXT_ACTION_STATUS = "purg01_route_admission_pass"
EXPECTED_LATEST_COMPLETED_STATUS = "if11_minos_final_verdict_closure_pass"
EXPECTED_LATEST_COMPLETED_PROJECT_SHA = "6312302ea45b72ddc310b2b33f56245be65b99dc"
EXPECTED_LATEST_COMPLETED_CI_STATE = "CI_GREEN_CONFIRMED"
EXPECTED_NEXT_RECOMMENDED_STEP = "execute_purg01_controlled_triage_artifact_only"
NO_TRANSITION_DEFINED_MESSAGE = "Nenhuma transição definida. Aguardando instrução do operador."
PURG01_REVIEW_NEXT_RECOMMENDED_STEP = "request_operator_authorization_for_purg01_route_admission"
PURG00_REQUIRED_SOURCE_PACKET_STEP = "operator_supply_purg00_required_source_packet"
ROUTE_ADMISSION_NEXT_RECOMMENDED_STEP = "execute_purg_pre_canonical_authority_materialization"
PURG00_OPERATOR_REVIEW_PACKET_NEXT_RECOMMENDED_STEP = "request_operator_authorization_for_purg00_route_admission"
EXPECTED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27177997351"
PURG_PRE_ROUTE_ADMISSION_STATUS = "purg_pre_route_admission_pass"
PURG_PRE_ROUTE_ADMISSION_OPERATOR_SOURCE = "chat_operator_pode_comecar_2026_06_09"
PURG_PRE_AUTHORITY_EXECUTION_STATUS = "purg_pre_canonical_authority_execution_pass"
PURG_PRE_AUTHORITY_EXECUTION_NEXT_RECOMMENDED_STEP = "prepare_purg00_route_admission_or_operator_review"
PURG00_OPERATOR_REVIEW_PACKET_STATUS = "purg00_operator_review_packet_pass"
PURG00_ROUTE_ADMISSION_STATUS = "purg00_route_admission_pass"
PURG00_ROUTE_ADMISSION_OPERATOR_SOURCE = "chat_operator_pode_comecar_purg00_route_admission_2026_06_09"
PURG00_ROUTE_ADMISSION_NEXT_STEP = "execute_purg00_handoff_intake_authority_lock"
PURG00_HANDOFF_INTAKE_STATUS = "purg00_handoff_intake_authority_lock_blocked"
PURG00_HANDOFF_INTAKE_DECISION = "blocked"
PURG00_HANDOFF_INTAKE_NEXT_STEP = "operator_supply_purg00_required_source_packet"
PURG00_HANDOFF_INTAKE_DATA_GAP_STATUS = "DATA_GAP_BLOCKED"
PURG00_HANDOFF_INTAKE_MISSING_FIELDS = [
    "affected files",
    "oracle id",
    "blast radius",
    "target control",
    "risk class",
    "dependency group",
]
PURG00_TERMINAL_BLOCKER_STATUS = "purg00_source_gap_terminal_blocker_operator_source_required"
PURG00_TERMINAL_BLOCKER_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_source_gap_terminal_blocker_decision.json"
PURG00_OPERATOR_REQUIRED_SOURCE_PACKET_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_required_source_packet.json"
PURG00_MISSING_FIELDS_CONTRACT_SCHEMA_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_missing_fields_contract.schema.json"
PURG00_NO_LOOP_ATTESTATION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_no_loop_attestation.json"
PURG00_NO_REAL_EXECUTION_V2_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_no_real_execution_attestation_v2.json"
PURG00_ROUTE_AMENDMENT_WAIT_STATE_STATUS = "purg00_route_amendment_terminal_wait_state_operator_source_required"
PURG00_ROUTE_AMENDMENT_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_terminal_wait_state_decision.json"
PURG00_ROUTE_AMENDMENT_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_terminal_wait_state_summary.json"
PURG00_ROUTE_AMENDMENT_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_terminal_wait_state_report.md"
PURG00_ROUTE_AMENDMENT_LIVE_STATE_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_live_state_mutation_manifest.json"
PURG00_ROUTE_AMENDMENT_VALIDATOR_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_validator_patch_manifest.json"
PURG00_ROUTE_AMENDMENT_SCHEMA_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_schema_patch_manifest.json"
PURG00_ROUTE_AMENDMENT_NO_REAL_EXECUTION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_no_real_execution_attestation.json"
PURG00_ROUTE_AMENDMENT_ROLLBACK_PLAN_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_route_amendment_rollback_plan.md"
PURG00_OPERATOR_SOURCE_PACKET_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_required_source_packet.json"
PURG00_OPERATOR_SOURCE_PACKET_INTAKE_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_intake_decision.json"
PURG00_OPERATOR_SOURCE_PACKET_INTAKE_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_intake_summary.json"
PURG00_OPERATOR_SOURCE_PACKET_INTAKE_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_intake_report.md"
PURG00_OPERATOR_SOURCE_PACKET_HASH_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_hash_verification.json"
PURG00_OPERATOR_SOURCE_PACKET_CI_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_ci_verification.json"
PURG00_OPERATOR_SOURCE_PACKET_NO_REAL_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_no_real_execution_attestation.json"
PURG00_OPERATOR_SOURCE_PACKET_NEXT_ROUTE_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg00_operator_source_packet_next_route_candidate.json"
PURG00_OPERATOR_SOURCE_PACKET_SHA = "6f616556d0a31ebba8e0bd647ccfd014f1955127856cc20d2deee2f6d7111e72"
PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA = "ff9ade875ebf47bad8c4fde0311f576d958c1625"
PURG00_OPERATOR_SOURCE_PACKET_INTAKE_STATUS = "purg00_operator_source_packet_intake_pass"
PURG01_ROUTE_ADMISSION_REVIEW_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_review_decision.json"
PURG01_ROUTE_ADMISSION_REVIEW_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_review_summary.json"
PURG01_ROUTE_ADMISSION_REVIEW_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_review_report.md"
PURG01_ROUTE_ADMISSION_READINESS_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_readiness_matrix.json"
PURG01_ROUTE_ADMISSION_LOCK_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_lock_matrix.json"
PURG01_ROUTE_ADMISSION_NO_REAL_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_no_real_execution_attestation.json"
PURG01_ROUTE_ADMISSION_CANDIDATE_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_candidate.json"
PURG01_ROUTE_ADMISSION_REVIEW_STATUS = "purg01_route_admission_review_pass"
PURG01_ROUTE_ADMISSION_SOURCE_ACTIVE_CONTEXT_SHA = "870015630f12b9db6d6df6d3427931aca47e4c00"
PURG01_ROUTE_ADMISSION_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_decision.json"
PURG01_ROUTE_ADMISSION_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_summary.json"
PURG01_ROUTE_ADMISSION_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_report.md"
PURG01_ROUTE_ADMISSION_OPERATOR_AUTH_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_operator_authorization.json"
PURG01_ROUTE_ADMISSION_LIVE_ROUTE_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_live_route_mutation_manifest.json"
PURG01_ROUTE_ADMISSION_SCHEMA_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_schema_patch_manifest.json"
PURG01_ROUTE_ADMISSION_VALIDATOR_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_validator_patch_manifest.json"
PURG01_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_no_real_execution_attestation.json"
PURG01_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_route_admission_rollback_plan.md"
PURG01_ROUTE_ADMISSION_STATUS = "purg01_route_admission_pass"
PURG01_ROUTE_ADMISSION_OPERATOR_SCOPE = "route_admission_only_not_execution"
PURG01_ROUTE_ADMISSION_OPERATOR_TEXT = "Autorizo PURG-01 route admission. autorizo toda rota purg"
PURG01_TRIAGE_READINESS_REVIEW_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_readiness_review_decision.json"
PURG01_TRIAGE_READINESS_REVIEW_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_readiness_review_summary.json"
PURG01_TRIAGE_READINESS_REVIEW_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_readiness_review_report.md"
PURG01_TRIAGE_READINESS_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_readiness_matrix.json"
PURG01_TRIAGE_LOCK_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_lock_matrix.json"
PURG01_TRIAGE_PLANNING_CANDIDATE_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_planning_candidate.json"
PURG01_TRIAGE_READINESS_REVIEW_STATUS = "purg01_triage_readiness_review_pass"
PURG01_TRIAGE_PLANNING_GATE_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_planning_gate_decision.json"
PURG01_TRIAGE_PLANNING_GATE_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_planning_gate_summary.json"
PURG01_TRIAGE_PLANNING_GATE_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_planning_gate_report.md"
PURG01_TRIAGE_PLAN_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_plan.json"
PURG01_TRIAGE_ORACLE_PLAN_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_oracle_plan.json"
PURG01_TRIAGE_EVIDENCE_REQUIREMENTS_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_evidence_requirements.json"
PURG01_TRIAGE_PLANNING_SCOPE_BOUNDARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_scope_boundary.json"
PURG01_TRIAGE_EXECUTION_LOCK_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_execution_lock_matrix.json"
PURG01_TRIAGE_PLANNING_NO_REAL_EXECUTION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_no_real_execution_attestation.json"
PURG01_TRIAGE_AUTH_REQUEST_CANDIDATE_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_request_candidate.json"
PURG01_TRIAGE_PLANNING_GATE_STATUS = "purg01_triage_planning_gate_pass"
PURG01_TRIAGE_AUTHORIZATION_GATE_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_gate_decision.json"
PURG01_TRIAGE_AUTHORIZATION_GATE_SUMMARY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_gate_summary.json"
PURG01_TRIAGE_AUTHORIZATION_GATE_REPORT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_gate_report.md"
PURG01_TRIAGE_OPERATOR_AUTH_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_operator_authorization.json"
PURG01_TRIAGE_AUTHORIZATION_SCOPE_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_scope_matrix.json"
PURG01_TRIAGE_AUTHORIZATION_LIVE_STATE_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_live_state_mutation_manifest.json"
PURG01_TRIAGE_AUTHORIZATION_VALIDATOR_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_validator_patch_manifest.json"
PURG01_TRIAGE_AUTHORIZATION_SCHEMA_MANIFEST_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_schema_patch_manifest.json"
PURG01_TRIAGE_AUTHORIZATION_NO_REAL_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_authorization_no_real_execution_attestation.json"
PURG01_TRIAGE_CONTROLLED_EXECUTION_CANDIDATE_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_triage_controlled_execution_candidate.json"
PURG01_TRIAGE_AUTHORIZATION_GATE_STATUS = "purg01_triage_authorization_gate_pass"
PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_DECISION_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_execution_gate_decision.json"
PURG01_CONTROLLED_TRIAGE_EXECUTION_PRECONDITIONS_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_execution_preconditions_matrix.json"
PURG01_CONTROLLED_TRIAGE_EXECUTION_NO_REAL_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_execution_no_real_execution_attestation.json"
PURG01_CONTROLLED_TRIAGE_EXECUTION_SOURCE_INTEGRITY_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_execution_source_integrity_report.json"
PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_STATUS = "purg01_controlled_triage_execution_gate_pass"
PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_RESULT_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_artifact_only_execution_result.json"
PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_EVIDENCE_MATRIX_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_artifact_only_evidence_matrix.json"
PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_NO_REAL_PATH = PROJECT_ROOT / "artifacts" / "purgatorium" / "purg01_controlled_triage_artifact_only_no_real_execution_attestation.json"
PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_STATUS = "purg01_controlled_triage_artifact_only_execution_pass"
PURG04_POST_MERGE_VALIDATION_OPERATOR_AUTH_PATH = ROOT / "artifacts" / "purgatorium" / "purg04_track_a_post_merge_validation_operator_authorization.json"
PURG04_POST_MERGE_VALIDATION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "purg04_track_a_post_merge_validation_packet.json"
PURG04_POST_MERGE_VALIDATION_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "purg04_track_a_post_merge_validation_no_real_execution_attestation.json"
PURG_RESIDUAL_ROUTE_OPENING_OPERATOR_AUTH_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_operator_authorization.json"
PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_packet.json"
PURG_RESIDUAL_ROUTE_OPENING_SUMMARY_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_summary.json"
PURG_RESIDUAL_ROUTE_OPENING_REPORT_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_report.md"
PURG_RESIDUAL_ROUTE_OPENING_LOCK_MATRIX_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_lock_matrix.json"
PURG_RESIDUAL_ROUTE_OPENING_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_no_real_execution_attestation.json"
PURG_RESIDUAL_ROUTE_OPENING_VALIDATION_EVIDENCE_PATH = ROOT / "artifacts" / "purgatorium" / "purg_residual_risk_carry_forward_route_opening_validation_evidence.json"
INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_admission_packet.json"
INF_REVALIDATION_REQUIRED_INPUTS_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_required_inputs.json"
INF_REVALIDATION_SCOPE_MATRIX_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_scope_matrix.json"
INF_REVALIDATION_FORBIDDEN_ACTIONS_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_forbidden_actions.json"
INF_REVALIDATION_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_next_route_candidate.json"
INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_packet.json"
INF_REVALIDATION_ROUTE_ACTIVATION_TRANSITION_ROW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_transition_row.json"
INF_REVALIDATION_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_state_update_manifest.json"
INF_REVALIDATION_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_schema_validator_evidence.json"
INF_REVALIDATION_ROUTE_ACTIVATION_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_no_real_execution_attestation.json"
INF_REVALIDATION_ROUTE_ACTIVATION_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_route_activation_next_route_candidate.json"
INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_route_activation_packet.json"
INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_TRANSITION_ROW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_route_activation_transition_row.json"
INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_route_activation_state_update_manifest.json"
INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_route_activation_schema_validator_evidence.json"
INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_route_activation_no_real_execution_attestation.json"
INF_REVALIDATION_READINESS_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_packet.json"
INF_REVALIDATION_SCENARIO_SCOPE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_scenario_scope.json"
INF_REVALIDATION_ORACLE_CONTRACT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_oracle_contract.json"
INF_REVALIDATION_ABORT_CRITERIA_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_abort_criteria.json"
INF_REVALIDATION_READINESS_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_no_real_execution_attestation.json"
INF_REVALIDATION_READINESS_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_readiness_next_route_candidate.json"
INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_operator_authorization_packet.json"
INF_REVALIDATION_EXECUTION_CONTRACT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_contract.json"
INF_REVALIDATION_SAFETY_LOCK_MATRIX_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_safety_lock_matrix.json"
INF_REVALIDATION_OPERATOR_AUTH_NO_REAL_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_operator_authorization_no_real_execution_attestation.json"
INF_REVALIDATION_OPERATOR_AUTH_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_operator_authorization_next_route_candidate.json"
INF_REVALIDATION_EXECUTION_OPERATOR_COMMAND_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_operator_command.json"
INF_REVALIDATION_EXECUTION_TRANSITION_ROW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_transition_row.json"
INF_REVALIDATION_EXECUTION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_packet.json"
INF_REVALIDATION_EXECUTION_PREFLIGHT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_preflight.json"
INF_REVALIDATION_EXECUTION_COMMAND_LOG_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_command_log.jsonl"
INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_oracle_result.json"
INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_regression_matrix.json"
INF_REVALIDATION_EXECUTION_EVIDENCE_INVENTORY_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_evidence_inventory.json"
INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_no_forbidden_surface_attestation.json"
INF_REVALIDATION_EXECUTION_SUMMARY_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_summary.json"
INF_REVALIDATION_EXECUTION_REPORT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_report.md"
INF_REVALIDATION_EXECUTION_VALIDATION_EVIDENCE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_validation_evidence.json"
INF_REVALIDATION_EXECUTION_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_execution_next_route_candidate.json"
INF_REVALIDATION_ADJUDICATION_OPERATOR_COMMAND_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_operator_command.json"
INF_REVALIDATION_ADJUDICATION_TRANSITION_ROW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_transition_row.json"
INF_REVALIDATION_ADJUDICATION_EVIDENCE_MATRIX_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_evidence_matrix.json"
INF_REVALIDATION_ADJUDICATION_ORACLE_REVIEW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_oracle_review.json"
INF_REVALIDATION_ADJUDICATION_REGRESSION_REVIEW_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_regression_review.json"
INF_REVALIDATION_ADJUDICATION_NO_FORBIDDEN_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_no_forbidden_surface_carry_forward.json"
INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_closure_packet.json"
INF_REVALIDATION_ADJUDICATION_CLOSURE_DECISION_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_closure_decision.json"
INF_REVALIDATION_ADJUDICATION_SUMMARY_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_summary.json"
INF_REVALIDATION_ADJUDICATION_REPORT_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_report.md"
INF_REVALIDATION_ADJUDICATION_VALIDATION_EVIDENCE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_validation_evidence.json"
INF_REVALIDATION_ADJUDICATION_NEXT_ROUTE_CANDIDATE_PATH = ROOT / "artifacts" / "purgatorium" / "inf_revalidation_adjudication_next_route_candidate.json"
ACTIVE_CONTEXT_ROOT = ROOT / "artifacts" / "active_context"
BENCHUX_ROOT = ROOT / "artifacts" / "benchux"
IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH = ACTIVE_CONTEXT_ROOT / "if09_closure_milestone_sanity_packet.json"
IF09_CLOSURE_MILESTONE_MIRROR_DRIFT_MATRIX_PATH = ACTIVE_CONTEXT_ROOT / "if09_closure_milestone_mirror_drift_matrix.json"
IF09_CLOSURE_MILESTONE_SUPERSEDED_NOTES_MANIFEST_PATH = ACTIVE_CONTEXT_ROOT / "if09_closure_milestone_superseded_notes_manifest.json"
IF09_CLOSURE_MILESTONE_NO_REAL_EXECUTION_ATTESTATION_PATH = ACTIVE_CONTEXT_ROOT / "if09_closure_milestone_no_real_execution_attestation.json"
IF09_CLOSURE_MILESTONE_VALIDATION_EVIDENCE_PATH = ACTIVE_CONTEXT_ROOT / "if09_closure_milestone_validation_evidence.json"
BENCHUX_ROUTE_OPENING_CANDIDATE_PATH = BENCHUX_ROOT / "benchux_route_opening_candidate.json"
BENCHUX_PRE_ROUTE_SCOPE_NOTE_PATH = BENCHUX_ROOT / "benchux_pre_route_scope_note.json"
PURG01_TRIAGE_OPERATOR_TEXT = "Autorizo PURG-01 triage."
PURG01_TRIAGE_OPERATOR_SCOPE = "purg01_triage_authorization_only_not_fix_not_real_execution"
PURG00_LIVE_ROUTE_PRESERVING_STATUSES = {
    PURG00_ROUTE_ADMISSION_STATUS,
    PURG00_HANDOFF_INTAKE_STATUS,
}
IF08_W4_PREFLIGHT_PHASE = "IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness"
IF08_W4_PREFLIGHT_STATUS = "if08_w4_replay_rollback_concurrency_cost_preflight_readiness_pass"
IF08_W4_PREFLIGHT_PROJECT_SHA = "2785b06e7a73b10675d30ed870fda7959e2e866a"
IF08_W4_PREFLIGHT_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W4_PREFLIGHT_NEXT_RECOMMENDED_STEP = "execute_if08_w4_replay_rollback_concurrency_cost_controlled_execution"
IF08_W4_PREFLIGHT_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27116116919"
IF08_W3_POST_SYNC_PHASE = "IF-08 W3 Controlled Execution Post-Sync Review & W4 Readiness Decision"
IF08_W3_POST_SYNC_STATUS = "if08_w3_post_sync_review_w4_readiness_pass"
IF08_W3_POST_SYNC_PROJECT_SHA = "aa22631ec8612646aa76fdd03ed15c3513f8ec93"
IF08_W3_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W3_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w4_replay_rollback_concurrency_cost_preflight_readiness"
IF08_W3_POST_SYNC_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27114468159"
IF08_W3_CONTROLLED_PHASE = "IF-08 W3 Runtime/Tool/MCP/Sandbox Controlled Execution"
IF08_W3_CONTROLLED_STATUS = "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_pass"
IF08_W3_CONTROLLED_PROJECT_SHA = "598dd5c8d98e8c9f89f9123e10efedf50871079b"
IF08_W3_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W3_CONTROLLED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w3_runtime_tool_mcp_sandbox_controlled_execution"
IF08_W3_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27113309069"
IF08_W3_PREFLIGHT_PHASE = "IF-08 W3 Runtime/Tool/MCP/Sandbox Preflight Readiness"
IF08_W3_PREFLIGHT_STATUS = "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_pass"
IF08_W3_PREFLIGHT_PROJECT_SHA = "d9406a4507ce78d2512101963b76e2836b6ee712"
IF08_W3_PREFLIGHT_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W3_PREFLIGHT_NEXT_RECOMMENDED_STEP = "execute_if08_w3_runtime_tool_mcp_sandbox_controlled_execution"
IF08_W3_PREFLIGHT_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27112660289"
IF08_W2_POST_SYNC_PHASE = "IF-08 W2 Controlled Execution Post-Sync Review & W3 Readiness Decision"
IF08_W2_POST_SYNC_STATUS = "if08_w2_post_sync_review_w3_readiness_pass"
IF08_W2_POST_SYNC_PROJECT_SHA = "86d1ddba94c73bf78151da13b9e1dd0eaa07feb0"
IF08_W2_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W2_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w3_runtime_tool_mcp_sandbox_preflight_readiness"
IF08_W2_POST_SYNC_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27103566160"
IF08_W2_CONTROLLED_PHASE = "IF-08 W2 Auth/HITL/Identity/Exfil Controlled Execution"
IF08_W2_CONTROLLED_STATUS = "if08_w2_auth_hitl_identity_exfil_controlled_execution_pass"
IF08_W2_CONTROLLED_PROJECT_SHA = "3ef519a5c13bb45eb8c3e2cc866cd77df29b4fb3"
IF08_W2_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W2_CONTROLLED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w2_auth_hitl_identity_exfil_controlled_execution"
IF08_W2_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27102754205"
IF08_W1_CONTROLLED_PHASE = "IF-08 W1 Context/Memory/RAG Controlled Execution"
IF08_W1_CONTROLLED_STATUS = "if08_w1_context_memory_rag_controlled_execution_pass"
IF08_W1_CONTROLLED_PROJECT_SHA = "1d0f51584e082d1f3f7c270df89d567a96066711"
IF08_W1_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W1_CONTROLLED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w1_context_memory_rag_controlled_execution"
IF08_W1_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27100836572"
IF08_W2_PREFLIGHT_PHASE = "IF-08 W2 Auth/HITL/Identity/Exfil Preflight Readiness"
IF08_W2_PREFLIGHT_STATUS = "if08_w2_auth_hitl_identity_exfil_preflight_readiness_pass"
IF08_W2_PREFLIGHT_PROJECT_SHA = "d19642cb83d996cefaf57bb2c71ed17195035103"
IF08_W2_PREFLIGHT_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W2_PREFLIGHT_NEXT_RECOMMENDED_STEP = "execute_if08_w2_auth_hitl_identity_exfil_controlled_execution"
IF08_W2_PREFLIGHT_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27102062488"
IF08_W1_POST_SYNC_PHASE = "IF-08 W1 Controlled Execution Post-Sync Review & W2 Readiness Decision"
IF08_W1_POST_SYNC_STATUS = "if08_w1_post_sync_review_w2_readiness_pass"
IF08_W1_POST_SYNC_PROJECT_SHA = "5bb8b08373aca54cf30d5451ff7655c00bee2cf7"
IF08_W1_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W1_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w2_auth_hitl_identity_exfil_preflight_readiness"
IF08_W1_POST_SYNC_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27101363788"
IF08_W1_PREFLIGHT_PHASE = "IF-08 W1 Context/Memory/RAG Preflight Readiness"
IF08_W1_PREFLIGHT_STATUS = "if08_w1_context_memory_rag_preflight_readiness_pass"
IF08_W1_PREFLIGHT_PROJECT_SHA = "9542ae6d041a2d7ed0f6d29c07145ea9cd490b5d"
IF08_W1_PREFLIGHT_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W1_PREFLIGHT_NEXT_RECOMMENDED_STEP = "execute_if08_w1_context_memory_rag_controlled_execution"
IF08_W05_POST_SYNC_PHASE = "IF-08 W0.5 Post-Sync Review & W1 Readiness Decision"
IF08_W05_POST_SYNC_STATUS = "if08_w05_post_sync_review_pass"
IF08_W05_POST_SYNC_PROJECT_SHA = "6b8dc72edc168402700c63cca076bf533bd3b65a"
IF08_W05_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W05_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w1_context_memory_rag_preflight_readiness"
IF08_W05_CONTROLLED_PHASE = "IF-08 W0.5 Controlled Ledger/Evidence Integrity Execution"
IF08_W05_CONTROLLED_STATUS = "if08_w05_controlled_ledger_evidence_integrity_execution_pass"
IF08_W05_CONTROLLED_INVALID_STATUS = "if08_w05_controlled_ledger_evidence_integrity_execution_invalid"
IF08_W05_CONTROLLED_PROJECT_SHA = "9ad30a803ffe2227551bdbe2856633eef1165047"
IF08_W05_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W05_CONTROLLED_NEXT_RECOMMENDED_STEP = "defer_next_if08_wave_prompt_until_post_sync_review"
IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_PASS = "sync_if08_w05_controlled_execution_into_active_context"
IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_INVALID = "resolve_if08_w05_integrity_drift_before_reexecution"
IF08_W05_RERUN_PHASE = "IF08_W05 Preflight Readiness Rerun"
IF08_W05_RERUN_STATUS = "if08_w05_preflight_readiness_rerun_pass"
IF08_W05_RERUN_BLOCKED_STATUS = "if08_w05_preflight_readiness_rerun_blocked"
IF08_W05_RERUN_PROJECT_SHA = "93b4ee5c6aa96869ef426331c51e5f3df76e2812"
IF08_W05_RERUN_NEXT_RECOMMENDED_STEP = "IF-08 W0.5 Controlled Ledger/Evidence Integrity Execution"
IF08_W05_RERUN_BLOCKED_NEXT_RECOMMENDED_STEP = "repair_if08_w05_preflight_readiness_rerun_inputs"
IF08_W05_SYNC_SOURCE_PHASE = "IF08_W05 Minos Mechanical Alias Normalization"
IF08_W05_SYNC_SOURCE_STATUS = "if08_w05_minos_mechanical_alias_normalization_packet_ready"
IF08_W05_SYNC_SOURCE_PROJECT_SHA = "f05ff031a95625da4d09c1c8bb648cc81ed3a97f"
IF08_W05_SYNC_NEXT_RECOMMENDED_STEP = "rerun_if08_w05_preflight_readiness"
ROUTE_SYNC_SOURCE_PHASE_ID = "INF-FULL-04"
ROUTE_SYNC_DERIVED_NEXT_PHASE_ID = "INF-FULL-05"
ROUTE_SYNC_DERIVED_NEXT_PHASE_CLASS = "review_gate_only"
ROUTE_SYNC_DERIVED_NEXT_PHASE_ADVANCE_MODE = "prompt_only"
EXPECTED_CURRENT_SUCCESSOR_ADVANCE_MODE = "operator"
ROUTE_SYNC_DERIVED_NEXT_PHASE_NAME = "ARIS Infernus FULL Pre-Execution Review Gate"
INF_FULL_02_PHASE = "ARIS Infernus FULL Baseline Freeze Planning"
INF_FULL_02_STATUS = "inf_full_02_baseline_freeze_planning_pass"
INF_FULL_03_PHASE = "ARIS Infernus FULL Chain Registration & Preparation Opening"
INF_FULL_03_STATUS = "inf_full_03_chain_registration_opening_pass"
INF_FULL_04_STATUS = "inf_full_04_scenario_pack_harness_readiness_pass"
INF_FULL_04_DECISION_PHASE_NAME = "Scenario Pack & Harness Readiness Gate"
INF_FULL_05_DECISION_PHASE_NAME = "ARIS Infernus FULL Pre-Execution Review Gate"
ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA = "973d49a24d58d4166acb95b40611be409c5d44df"
ACB_CAP_05_RESYNC_NEW_PROJECT_SHA = "fa8546f35ae826f8cc254d51b77ba1ea704d0a27"
ACB_CAP_05_PROJECT_DECISION_SHA = "51f1416f83e8ed488031210de688ffb5856ea004"
ACB_CAP_05_ADVANCED_SUPPLY_CHAIN_CI_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27052210325"
INF_FULL_01_SCOPE_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_scope_charter_decision_2026_06_06.json")
INF_FULL_01_SCOPE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_scope_matrix_2026_06_06.json")
INF_FULL_01_SCOPE_MANIFEST_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_module_scope_manifest_2026_06_06.json")
INF_FULL_01_SCOPE_CHARTER_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_01_scope_charter_2026_06_06.md")
INF_FULL_02_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_planning_decision_2026_06_06.json")
INF_FULL_02_INVENTORY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_inventory_2026_06_06.json")
INF_FULL_02_HASH_MANIFEST_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_hash_manifest_2026_06_06.json")
INF_FULL_02_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_summary_2026_06_06.json")
INF_FULL_02_PLANNING_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_02_baseline_freeze_planning_2026_06_06.md")
INFERNUS_FULL_CANONROADMAP_PATH = _resolve_project_relative("docs", "infernus_full", "infernus_full_canonroadmap.md")
INFERNUS_FULL_SUPERSESSION_PATH = _resolve_project_relative("artifacts", "infernus", "infernus_full_canonroadmap_supersession_2026_06_06.json")
INF_FULL_03_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_03_opening_decision_2026_06_06.json")
INF_FULL_03_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_03_opening_summary_2026_06_06.json")
INF_FULL_03_OPENING_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_03_opening_2026_06_06.md")
INFERNUS_FULL_DOCS_README_PATH = _resolve_project_relative("docs", "infernus_full", "README.md")
IF00_TRANSITION_CANDIDATE_PATH = _resolve_project_relative("artifacts", "infernus", "if00_transition_candidate.json")
IF00_HERMETICITY_PATH = _resolve_project_relative("artifacts", "infernus", "if00_lab_hermeticity_baseline.json")
IF01_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if01_research_evidence_ledger.jsonl")
IF02_ONTOLOGY_PATH = _resolve_project_relative("artifacts", "infernus", "if02_threat_ontology_v4.json")
IF02_COVERAGE_PATH = _resolve_project_relative("artifacts", "infernus", "if02_coverage_matrix_v4.csv")
IF03_ORACLE_PACK_PATH = _resolve_project_relative("artifacts", "infernus", "if03_oracle_metrics_contract_pack.json")
IF04_BOT_PACK_PATH = _resolve_project_relative("artifacts", "infernus", "if04_bot_contract_pack_v4.json")
IF04_PERMISSION_PATH = _resolve_project_relative("artifacts", "infernus", "if04_permission_manifest_v4.json")
INF_FULL_OPERATOR_STANDING_AUTH_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_operator_standing_authorization_policy_2026_06_06.json")
IF05_SCENARIO_PACK_PATH = _resolve_project_relative("artifacts", "infernus", "if05_scenario_pack_manifest_v4.json")
IF05_CONTROLS_DESIGN_PATH = _resolve_project_relative("artifacts", "infernus", "if05_controls_design_v4.json")
IF05_ORACLE_MAPPING_PATH = _resolve_project_relative("artifacts", "infernus", "if05_scenario_oracle_mapping_v4.json")
IF05_MUTATION_REGISTRY_PATH = _resolve_project_relative("artifacts", "infernus", "if05_mutation_family_registry_v4.json")
IF06_HARNESS_READINESS_PATH = _resolve_project_relative("artifacts", "infernus", "if06_harness_readiness_decision.json")
IF06_SANDBOX_CONTRACT_PATH = _resolve_project_relative("artifacts", "infernus", "if06_sandbox_contract.json")
IF06_COST_QUOTA_PATH = _resolve_project_relative("artifacts", "infernus", "if06_cost_quota_manifest.json")
IF06_REPLAY_POLICY_PATH = _resolve_project_relative("artifacts", "infernus", "if06_replay_policy.json")
IF06_KILL_SWITCH_PATH = _resolve_project_relative("artifacts", "infernus", "if06_kill_switch_policy.json")
INF_FULL_04_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_04_decision_2026_06_06.json")
INF_FULL_04_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_04_summary_2026_06_06.json")
INF_FULL_04_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_04_scenario_pack_harness_readiness_2026_06_06.md")
IF07_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if07_pre_execution_review_decision_2026_06_06.json")
IF07_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if07_no_execution_attestation_2026_06_06.json")
IF07_SCENARIO_NORMALIZATION_PATH = _resolve_project_relative("artifacts", "infernus", "if07_scenario_count_normalization_evidence_2026_06_06.json")
IF07_VALIDATOR_EVIDENCE_PATH = _resolve_project_relative("artifacts", "infernus", "if07_validator_evidence_2026_06_06.json")
INF_FULL_05_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_05_pre_execution_review_summary_2026_06_06.json")
INF_FULL_05_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_05_pre_execution_review_report_2026_06_06.md")
INF_FULL_05_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_05_pre_execution_review_2026_06_06.md")
INF_FULL_06_IF08_AUTH_ROOT = ROOT / "artifacts" / "inf_full_06_if08_authorization"
INF_FULL_06_IF08_DECISION_PATH = INF_FULL_06_IF08_AUTH_ROOT / "decision.json"
INF_FULL_06_IF08_SUCCESSOR_MATRIX_PATH = INF_FULL_06_IF08_AUTH_ROOT / "successor_validation_matrix.json"
INF_FULL_06_IF08_NO_EXECUTION_PATH = INF_FULL_06_IF08_AUTH_ROOT / "no_execution_attestation.json"
INF_FULL_06_IF08_SUMMARY_PATH = INF_FULL_06_IF08_AUTH_ROOT / "summary.json"
INF_FULL_06_IF08_REPORT_PATH = INF_FULL_06_IF08_AUTH_ROOT / "report.md"
INF_FULL_07_IF08_AUTH_ROOT = ROOT / "artifacts" / "inf_full_07_if08_authorization"
INF_FULL_07_IF08_DECISION_PATH = INF_FULL_07_IF08_AUTH_ROOT / "decision.json"
INF_FULL_07_IF08_SUCCESSOR_MATRIX_PATH = INF_FULL_07_IF08_AUTH_ROOT / "successor_validation_matrix.json"
INF_FULL_07_IF08_NO_EXECUTION_PATH = INF_FULL_07_IF08_AUTH_ROOT / "no_execution_attestation.json"
INF_FULL_07_IF08_VALIDATOR_EVIDENCE_PATH = INF_FULL_07_IF08_AUTH_ROOT / "validator_evidence.json"
INF_FULL_07_IF08_SUMMARY_PATH = INF_FULL_07_IF08_AUTH_ROOT / "summary.json"
INF_FULL_07_IF08_REPORT_PATH = INF_FULL_07_IF08_AUTH_ROOT / "report.md"
IF08_W05_ALIAS_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_minos_mechanical_alias_normalization_decision_2026_06_06.json")
IF08_W05_ALIAS_OVERLAY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_minos_mechanical_alias_overlay_2026_06_06.json")
IF08_W05_ALIAS_GAP_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_minos_mechanical_alias_gap_resolution_matrix_2026_06_06.json")
IF08_W05_ALIAS_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_minos_mechanical_alias_no_execution_attestation_2026_06_06.json")
IF08_W05_ALIAS_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_minos_mechanical_alias_summary_2026_06_06.json")
IF08_W05_ALIAS_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w05_minos_mechanical_alias_normalization_2026_06_06.md")
IF08_W05_PROJECT_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_active_context_sync_rule_decision_2026_06_07.json")
IF08_W05_PROJECT_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_active_context_sync_rule_summary_2026_06_07.json")
IF08_W05_PROJECT_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_active_context_sync_rule_report_2026_06_07.md")
IF08_W05_PROJECT_SYNC_CI_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_active_context_sync_rule_ci_matrix_2026_06_07.json")
IF08_W05_PROJECT_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_active_context_sync_rule_no_execution_attestation_2026_06_07.json")
ACTIVE_CONTEXT_SYNC_RULE_ROOT = ROOT / "artifacts" / "active_context_sync_rule"
ACTIVE_CONTEXT_SYNC_RULE_DECISION_PATH = ACTIVE_CONTEXT_SYNC_RULE_ROOT / "decision.json"
ACTIVE_CONTEXT_SYNC_RULE_SUMMARY_PATH = ACTIVE_CONTEXT_SYNC_RULE_ROOT / "summary.json"
ACTIVE_CONTEXT_SYNC_RULE_REPORT_PATH = ACTIVE_CONTEXT_SYNC_RULE_ROOT / "report.md"
IF08_W05_RERUN_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_preflight_readiness_rerun_decision_2026_06_07.json")
IF08_W05_RERUN_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_preflight_readiness_rerun_summary_2026_06_07.json")
IF08_W05_RERUN_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_preflight_readiness_rerun_report_2026_06_07.md")
IF08_W05_RERUN_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_preflight_readiness_rerun_matrix_2026_06_07.json")
IF08_W05_RERUN_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_preflight_readiness_rerun_no_execution_attestation_2026_06_07.json")
IF08_W05_RERUN_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w05_preflight_readiness_rerun_2026_06_07.md")
IF08_W05_RERUN_ROOT = ROOT / "artifacts" / "if08_w05_preflight_readiness_rerun"
IF08_W05_RERUN_ACTIVE_DECISION_PATH = IF08_W05_RERUN_ROOT / "decision.json"
IF08_W05_RERUN_ACTIVE_SUMMARY_PATH = IF08_W05_RERUN_ROOT / "summary.json"
IF08_W05_RERUN_ACTIVE_REPORT_PATH = IF08_W05_RERUN_ROOT / "report.md"
IF08_W05_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_controlled_execution_decision_2026_06_07.json")
IF08_W05_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_summary_2026_06_07.json")
IF08_W05_CONTROLLED_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_detection_matrix_2026_06_07.json")
IF08_W05_CONTROLLED_HASH_CHAIN_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_hash_chain_manifest_2026_06_07.json")
IF08_W05_CONTROLLED_CUSTODY_CHAIN_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_custody_chain_2026_06_07.jsonl")
IF08_W05_CONTROLLED_BOUNDARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_boundary_attestation_2026_06_07.json")
IF08_W05_CONTROLLED_BUNDLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_evidence_bundle_manifest_2026_06_07.json")
IF08_W05_CONTROLLED_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_execution_ledger_2026_06_07.jsonl")
IF08_W05_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w05_controlled_execution_2026_06_07.md")
IF08_W05_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w05_controlled_execution"
IF08_W05_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W05_CONTROLLED_ROOT / "decision.json"
IF08_W05_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W05_CONTROLLED_ROOT / "summary.json"
IF08_W05_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W05_CONTROLLED_ROOT / "report.md"
IF08_W05_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_post_sync_review_decision_2026_06_07.json")
IF08_W05_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_post_sync_review_summary_2026_06_07.json")
IF08_W05_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_post_sync_review_report_2026_06_07.md")
IF08_W1_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_readiness_matrix_2026_06_07.json")
IF08_W05_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w05_post_sync_no_execution_attestation_2026_06_07.json")
IF08_W05_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w05_post_sync_review_2026_06_07.md")
IF08_W05_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w05_post_sync_review"
IF08_W05_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W05_POST_SYNC_ROOT / "decision.json"
IF08_W05_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W05_POST_SYNC_ROOT / "summary.json"
IF08_W05_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W05_POST_SYNC_ROOT / "report.md"
IF08_W1_PREFLIGHT_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_preflight_readiness_decision_2026_06_07.json")
IF08_W1_PREFLIGHT_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_preflight_readiness_summary_2026_06_07.json")
IF08_W1_PREFLIGHT_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_preflight_readiness_report_2026_06_07.md")
IF08_W1_PREFLIGHT_ATTACK_SURFACE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_attack_surface_matrix_2026_06_07.json")
IF08_W1_PREFLIGHT_ORACLE_CONTRACT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_oracle_contract_2026_06_07.json")
IF08_W1_PREFLIGHT_FIXTURE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_fixture_readiness_matrix_2026_06_07.json")
IF08_W1_PREFLIGHT_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_no_execution_attestation_2026_06_07.json")
IF08_W1_PREFLIGHT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w1_context_memory_rag_preflight_readiness_2026_06_07.md")
IF08_W1_PREFLIGHT_ROOT = ROOT / "artifacts" / "if08_w1_context_memory_rag_preflight_readiness"
IF08_W1_PREFLIGHT_ACTIVE_DECISION_PATH = IF08_W1_PREFLIGHT_ROOT / "decision.json"
IF08_W1_PREFLIGHT_ACTIVE_SUMMARY_PATH = IF08_W1_PREFLIGHT_ROOT / "summary.json"
IF08_W1_PREFLIGHT_ACTIVE_REPORT_PATH = IF08_W1_PREFLIGHT_ROOT / "report.md"
IF08_W1_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_controlled_execution_decision_2026_06_07.json")
IF08_W1_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_controlled_execution_summary_2026_06_07.json")
IF08_W1_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_memory_rag_controlled_execution_report_2026_06_07.md")
IF08_W1_CONTROLLED_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_integrity_detection_matrix_2026_06_07.json")
IF08_W1_CONTROLLED_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_context_oracle_results_2026_06_07.json")
IF08_W1_CONTROLLED_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_execution_ledger_2026_06_07.jsonl")
IF08_W1_CONTROLLED_BUNDLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_evidence_bundle_manifest_2026_06_07.json")
IF08_W1_CONTROLLED_NO_REAL_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_no_real_execution_attestation_2026_06_07.json")
IF08_W1_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w1_context_memory_rag_controlled_execution_2026_06_07.md")
IF08_W1_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w1_context_memory_rag_controlled_execution"
IF08_W1_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W1_CONTROLLED_ROOT / "decision.json"
IF08_W1_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W1_CONTROLLED_ROOT / "summary.json"
IF08_W1_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W1_CONTROLLED_ROOT / "report.md"
IF08_W1_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_post_sync_review_decision_2026_06_07.json")
IF08_W1_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_post_sync_review_summary_2026_06_07.json")
IF08_W1_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_post_sync_review_report_2026_06_07.md")
IF08_W2_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_readiness_matrix_2026_06_07.json")
IF08_W1_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w1_post_sync_no_execution_attestation_2026_06_07.json")
IF08_W1_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w1_post_sync_review_2026_06_07.md")
IF08_W1_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w1_post_sync_review"
IF08_W1_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W1_POST_SYNC_ROOT / "decision.json"
IF08_W1_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W1_POST_SYNC_ROOT / "summary.json"
IF08_W1_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W1_POST_SYNC_ROOT / "report.md"
IF08_W2_PREFLIGHT_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_preflight_readiness_decision_2026_06_07.json")
IF08_W2_PREFLIGHT_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_preflight_readiness_summary_2026_06_07.json")
IF08_W2_PREFLIGHT_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_preflight_readiness_report_2026_06_07.md")
IF08_W2_PREFLIGHT_ATTACK_SURFACE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_attack_surface_matrix_2026_06_07.json")
IF08_W2_PREFLIGHT_ORACLE_CONTRACT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_oracle_contract_2026_06_07.json")
IF08_W2_PREFLIGHT_FIXTURE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_fixture_readiness_matrix_2026_06_07.json")
IF08_W2_PREFLIGHT_STOP_CONDITION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_stop_condition_matrix_2026_06_07.json")
IF08_W2_PREFLIGHT_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_no_execution_attestation_2026_06_07.json")
IF08_W2_PREFLIGHT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w2_auth_hitl_identity_exfil_preflight_readiness_2026_06_07.md")
IF08_W2_PREFLIGHT_ROOT = ROOT / "artifacts" / "if08_w2_auth_hitl_identity_exfil_preflight_readiness"
IF08_W2_PREFLIGHT_ACTIVE_DECISION_PATH = IF08_W2_PREFLIGHT_ROOT / "decision.json"
IF08_W2_PREFLIGHT_ACTIVE_SUMMARY_PATH = IF08_W2_PREFLIGHT_ROOT / "summary.json"
IF08_W2_PREFLIGHT_ACTIVE_REPORT_PATH = IF08_W2_PREFLIGHT_ROOT / "report.md"
IF08_W2_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_controlled_execution_decision_2026_06_07.json")
IF08_W2_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_controlled_execution_summary_2026_06_07.json")
IF08_W2_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_hitl_identity_exfil_controlled_execution_report_2026_06_07.md")
IF08_W2_CONTROLLED_AUTH_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_auth_detection_matrix_2026_06_07.json")
IF08_W2_CONTROLLED_EXFIL_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_exfil_detection_matrix_2026_06_07.json")
IF08_W2_CONTROLLED_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_oracle_results_2026_06_07.json")
IF08_W2_CONTROLLED_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_execution_ledger_2026_06_07.jsonl")
IF08_W2_CONTROLLED_BUNDLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_evidence_bundle_manifest_2026_06_07.json")
IF08_W2_CONTROLLED_NO_REAL_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_no_real_execution_attestation_2026_06_07.json")
IF08_W2_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w2_auth_hitl_identity_exfil_controlled_execution_2026_06_07.md")
IF08_W2_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w2_auth_hitl_identity_exfil_controlled_execution"
IF08_W2_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W2_CONTROLLED_ROOT / "decision.json"
IF08_W2_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W2_CONTROLLED_ROOT / "summary.json"
IF08_W2_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W2_CONTROLLED_ROOT / "report.md"
IF08_W2_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_post_sync_review_decision_2026_06_07.json")
IF08_W2_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_post_sync_review_summary_2026_06_07.json")
IF08_W2_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_post_sync_review_report_2026_06_07.md")
IF08_W3_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_readiness_matrix_2026_06_07.json")
IF08_W2_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w2_post_sync_no_execution_attestation_2026_06_07.json")
IF08_W2_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w2_post_sync_review_2026_06_07.md")
IF08_W2_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w2_post_sync_review"
IF08_W2_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W2_POST_SYNC_ROOT / "decision.json"
IF08_W2_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W2_POST_SYNC_ROOT / "summary.json"
IF08_W2_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W2_POST_SYNC_ROOT / "report.md"
IF08_W3_PREFLIGHT_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_decision_2026_06_07.json")
IF08_W3_PREFLIGHT_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_summary_2026_06_07.json")
IF08_W3_PREFLIGHT_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_report_2026_06_07.md")
IF08_W3_PREFLIGHT_ATTACK_SURFACE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_attack_surface_matrix_2026_06_07.json")
IF08_W3_PREFLIGHT_ORACLE_CONTRACT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_oracle_contract_2026_06_07.json")
IF08_W3_PREFLIGHT_FIXTURE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_fixture_readiness_matrix_2026_06_07.json")
IF08_W3_PREFLIGHT_STOP_CONDITION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_stop_condition_matrix_2026_06_07.json")
IF08_W3_PREFLIGHT_SIRENE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_sirene_conditionality_matrix_2026_06_07.json")
IF08_W3_PREFLIGHT_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_no_execution_attestation_2026_06_07.json")
IF08_W3_PREFLIGHT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_2026_06_07.md")
IF08_W3_PREFLIGHT_ROOT = ROOT / "artifacts" / "if08_w3_runtime_tool_mcp_sandbox_preflight_readiness"
IF08_W3_PREFLIGHT_ACTIVE_DECISION_PATH = IF08_W3_PREFLIGHT_ROOT / "decision.json"
IF08_W3_PREFLIGHT_ACTIVE_SUMMARY_PATH = IF08_W3_PREFLIGHT_ROOT / "summary.json"
IF08_W3_PREFLIGHT_ACTIVE_REPORT_PATH = IF08_W3_PREFLIGHT_ROOT / "report.md"
IF08_W3_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_decision_2026_06_07.json")
IF08_W3_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_summary_2026_06_07.json")
IF08_W3_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_report_2026_06_07.md")
IF08_W3_CONTROLLED_RUNTIME_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_runtime_sandbox_detection_matrix_2026_06_07.json")
IF08_W3_CONTROLLED_TOOL_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_tool_mcp_detection_matrix_2026_06_07.json")
IF08_W3_CONTROLLED_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_oracle_results_2026_06_07.json")
IF08_W3_CONTROLLED_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_execution_ledger_2026_06_07.jsonl")
IF08_W3_CONTROLLED_BUNDLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_evidence_bundle_manifest_2026_06_07.json")
IF08_W3_CONTROLLED_SIRENE_RECORD_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_sirene_conditional_execution_record_2026_06_07.json")
IF08_W3_CONTROLLED_NO_REAL_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_no_real_execution_attestation_2026_06_07.json")
IF08_W3_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_2026_06_07.md")
IF08_W3_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w3_runtime_tool_mcp_sandbox_controlled_execution"
IF08_W3_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W3_CONTROLLED_ROOT / "decision.json"
IF08_W3_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W3_CONTROLLED_ROOT / "summary.json"
IF08_W3_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W3_CONTROLLED_ROOT / "report.md"
IF08_W3_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_post_sync_review_decision_2026_06_07.json")
IF08_W3_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_post_sync_review_summary_2026_06_07.json")
IF08_W3_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_post_sync_review_report_2026_06_07.md")
IF08_W4_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_readiness_matrix_2026_06_07.json")
IF08_W3_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w3_post_sync_no_execution_attestation_2026_06_07.json")
IF08_W3_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w3_post_sync_review_2026_06_07.md")
IF08_W3_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w3_post_sync_review"
IF08_W3_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W3_POST_SYNC_ROOT / "decision.json"
IF08_W3_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W3_POST_SYNC_ROOT / "summary.json"
IF08_W3_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W3_POST_SYNC_ROOT / "report.md"
IF08_W4_PREFLIGHT_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_preflight_readiness_decision_2026_06_07.json")
IF08_W4_PREFLIGHT_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_preflight_readiness_summary_2026_06_07.json")
IF08_W4_PREFLIGHT_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_preflight_readiness_report_2026_06_07.md")
IF08_W4_PREFLIGHT_ATTACK_SURFACE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_attack_surface_matrix_2026_06_07.json")
IF08_W4_PREFLIGHT_ROLLBACK_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_rollback_oracle_contract_2026_06_07.json")
IF08_W4_PREFLIGHT_CONCURRENCY_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_concurrency_oracle_contract_2026_06_07.json")
IF08_W4_PREFLIGHT_COST_ORACLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_cost_quota_oracle_contract_2026_06_07.json")
IF08_W4_PREFLIGHT_FIXTURE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_fixture_readiness_matrix_2026_06_07.json")
IF08_W4_PREFLIGHT_STOP_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_stop_condition_matrix_2026_06_07.json")
IF08_W4_PREFLIGHT_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_no_execution_attestation_2026_06_07.json")
IF08_W4_PREFLIGHT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w4_replay_rollback_concurrency_cost_preflight_readiness_2026_06_07.md")
IF08_W4_PREFLIGHT_ROOT = ROOT / "artifacts" / "if08_w4_replay_rollback_concurrency_cost_preflight_readiness"
IF08_W4_PREFLIGHT_ACTIVE_DECISION_PATH = IF08_W4_PREFLIGHT_ROOT / "decision.json"
IF08_W4_PREFLIGHT_ACTIVE_SUMMARY_PATH = IF08_W4_PREFLIGHT_ROOT / "summary.json"
IF08_W4_PREFLIGHT_ACTIVE_REPORT_PATH = IF08_W4_PREFLIGHT_ROOT / "report.md"
IF08_W4_CONTROLLED_PHASE = "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution"
IF08_W4_CONTROLLED_STATUS = "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass"
IF08_W4_CONTROLLED_PROJECT_SHA = "c65888a2f587c35b4e38b16b50b917233bac8fa3"
IF08_W4_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W4_CONTROLLED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution"
IF08_W4_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27156460042"
IF08_W4_POST_SYNC_PHASE = "IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision"
IF08_W4_POST_SYNC_STATUS = "if08_w4_post_sync_review_w5_readiness_pass"
IF08_W4_POST_SYNC_PROJECT_SHA = "d575b6f3c37c1ba411a2a0266efb9d04957234c0"
IF08_W4_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W4_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w5_business_chaos_preflight_readiness"
IF08_W4_POST_SYNC_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27159174070"
IF08_W4_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_controlled_execution_decision_2026_06_08.json")
IF08_W4_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_controlled_execution_summary_2026_06_08.json")
IF08_W4_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_controlled_execution_report_2026_06_08.md")
IF08_W4_CONTROLLED_LOG_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_controlled_execution_log_2026_06_08.jsonl")
IF08_W4_CONTROLLED_METRICS_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_metrics_2026_06_08.json")
IF08_W4_CONTROLLED_SAFETY_ATTESTATION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_replay_rollback_concurrency_cost_safety_attestation_2026_06_08.json")
IF08_W4_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w4_replay_rollback_concurrency_cost_controlled_execution_2026_06_08.md")
IF08_W4_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w4_replay_rollback_concurrency_cost_controlled_execution"
IF08_W4_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W4_CONTROLLED_ROOT / "decision.json"
IF08_W4_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W4_CONTROLLED_ROOT / "summary.json"
IF08_W4_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W4_CONTROLLED_ROOT / "report.md"
IF08_W4_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_post_sync_review_decision_2026_06_08.json")
IF08_W4_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_post_sync_review_summary_2026_06_08.json")
IF08_W4_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_post_sync_review_report_2026_06_08.md")
IF08_W5_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_readiness_matrix_2026_06_08.json")
IF08_W4_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w4_post_sync_no_execution_attestation_2026_06_08.json")
IF08_W4_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w4_post_sync_review_2026_06_08.md")
IF08_W4_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w4_post_sync_review"
IF08_W4_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W4_POST_SYNC_ROOT / "decision.json"
IF08_W4_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W4_POST_SYNC_ROOT / "summary.json"
IF08_W4_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W4_POST_SYNC_ROOT / "report.md"
IF08_W5_CONTROLLED_PHASE = "IF-08 W5 Business Chaos Controlled Execution"
IF08_W5_CONTROLLED_STATUS = "if08_w5_business_chaos_controlled_execution_pass"
IF08_W5_CONTROLLED_PROJECT_SHA = "5eb32158153bc5ff3db87d33c3c625f5b0df80fa"
IF08_W5_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W5_CONTROLLED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w5_business_chaos_controlled_execution"
IF08_W5_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27165976764"
IF08_W5_CONTROLLED_SOURCE_PROJECT_SHA = "0c9921503418da9883bcc9288178bd3f05e0cd8c"
IF08_W5_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA = "d1a351db479165af42d387d7300aa4ba7daa4a0a"
IF08_W5_CONTROLLED_PREVIOUS_PHASE = "IF-08 W5 Business Chaos Preflight Gap Repair"
IF08_W5_CONTROLLED_PREVIOUS_STATUS = "if08_w5_business_chaos_preflight_gap_repair_pass"
IF08_W5_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_decision_2026_06_08.json")
IF08_W5_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_summary_2026_06_08.json")
IF08_W5_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_report_2026_06_08.md")
IF08_W5_CONTROLLED_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_ledger_2026_06_08.jsonl")
IF08_W5_CONTROLLED_DOMAIN_RESULTS_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_domain_results_2026_06_08.json")
IF08_W5_CONTROLLED_BOT_RESULTS_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_bot_results_2026_06_08.json")
IF08_W5_CONTROLLED_COVERAGE_RESULTS_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_critical_coverage_results_2026_06_08.json")
IF08_W5_CONTROLLED_ORACLE_RESULTS_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_oracle_results_2026_06_08.json")
IF08_W5_CONTROLLED_SAFETY_ATTESTATION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_safety_attestation_2026_06_08.json")
IF08_W5_CONTROLLED_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_business_chaos_controlled_execution_no_real_execution_attestation_2026_06_08.json")
IF08_W5_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w5_business_chaos_controlled_execution_2026_06_08.md")
IF08_W5_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w5_business_chaos_controlled_execution"
IF08_W5_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W5_CONTROLLED_ROOT / "decision.json"
IF08_W5_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W5_CONTROLLED_ROOT / "summary.json"
IF08_W5_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W5_CONTROLLED_ROOT / "report.md"
IF08_W5_POST_SYNC_PHASE = "IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision"
IF08_W5_POST_SYNC_STATUS = "if08_w5_post_sync_review_w6_readiness_pass"
IF08_W5_POST_SYNC_PROJECT_SHA = "e9dfae63206523f26fce5df907945952c7351ad5"
IF08_W5_POST_SYNC_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W5_POST_SYNC_NEXT_RECOMMENDED_STEP = "prepare_if08_w6_final_audit_preflight_readiness"
IF08_W5_POST_SYNC_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27167943439"
IF08_W5_POST_SYNC_SOURCE_PROJECT_SHA = "5eb32158153bc5ff3db87d33c3c625f5b0df80fa"
IF08_W5_POST_SYNC_SOURCE_ACTIVE_CONTEXT_SHA = "a89f90c691965a104c99964f3b256d08758605af"
IF08_W5_POST_SYNC_PREVIOUS_PHASE = "IF-08 W5 Business Chaos Controlled Execution"
IF08_W5_POST_SYNC_PREVIOUS_STATUS = "if08_w5_business_chaos_controlled_execution_pass"
IF08_W5_POST_SYNC_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_post_sync_review_decision_2026_06_08.json")
IF08_W5_POST_SYNC_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_post_sync_review_summary_2026_06_08.json")
IF08_W5_POST_SYNC_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_post_sync_review_report_2026_06_08.md")
IF08_W6_READINESS_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_readiness_matrix_2026_06_08.json")
IF08_W5_POST_SYNC_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w5_post_sync_no_execution_attestation_2026_06_08.json")
IF08_W5_POST_SYNC_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w5_post_sync_review_2026_06_08.md")
IF08_W5_POST_SYNC_ROOT = ROOT / "artifacts" / "if08_w5_post_sync_review"
IF08_W5_POST_SYNC_ACTIVE_DECISION_PATH = IF08_W5_POST_SYNC_ROOT / "decision.json"
IF08_W5_POST_SYNC_ACTIVE_SUMMARY_PATH = IF08_W5_POST_SYNC_ROOT / "summary.json"
IF08_W5_POST_SYNC_ACTIVE_REPORT_PATH = IF08_W5_POST_SYNC_ROOT / "report.md"
IF08_W6_PREFLIGHT_PHASE = "IF-08 W6 Final Audit Preflight Readiness"
IF08_W6_PREFLIGHT_STATUS = "if08_w6_final_audit_preflight_readiness_pass"
IF08_W6_PREFLIGHT_PROJECT_SHA = "0358de95c7fb80d06871a20ae46b8fbc3174c5d7"
IF08_W6_PREFLIGHT_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W6_PREFLIGHT_NEXT_RECOMMENDED_STEP = "execute_if08_w6_final_audit_controlled_execution"
IF08_W6_PREFLIGHT_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27171819900"
IF08_W6_PREFLIGHT_SOURCE_PROJECT_SHA = "e9dfae63206523f26fce5df907945952c7351ad5"
IF08_W6_PREFLIGHT_SOURCE_ACTIVE_CONTEXT_SHA = "fabb8b29bedf0222975f54e1c8e496fd72336689"
IF08_W6_PREFLIGHT_PREVIOUS_PHASE = "IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision"
IF08_W6_PREFLIGHT_PREVIOUS_STATUS = "if08_w5_post_sync_review_w6_readiness_pass"
IF08_W6_PREFLIGHT_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_preflight_readiness_decision_2026_06_08.json")
IF08_W6_PREFLIGHT_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_preflight_readiness_summary_2026_06_08.json")
IF08_W6_PREFLIGHT_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_preflight_readiness_report_2026_06_08.md")
IF08_W6_MINOS_MECHANICAL_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_minos_mechanical_readiness_matrix_2026_06_08.json")
IF08_W6_MINOS_SEMANTIC_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_minos_semantic_readiness_matrix_2026_06_08.json")
IF08_W6_THRESHOLD_CONTRACT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_ttr_har_threshold_contract_2026_06_08.json")
IF08_W6_STOP_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_stop_condition_matrix_2026_06_08.json")
IF08_W6_NO_EXECUTION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_no_execution_attestation_2026_06_08.json")
IF08_W6_PREFLIGHT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w6_final_audit_preflight_readiness_2026_06_08.md")
IF08_W6_PREFLIGHT_ROOT = ROOT / "artifacts" / "if08_w6_final_audit_preflight_readiness"
IF08_W6_PREFLIGHT_ACTIVE_DECISION_PATH = IF08_W6_PREFLIGHT_ROOT / "decision.json"
IF08_W6_PREFLIGHT_ACTIVE_SUMMARY_PATH = IF08_W6_PREFLIGHT_ROOT / "summary.json"
IF08_W6_PREFLIGHT_ACTIVE_REPORT_PATH = IF08_W6_PREFLIGHT_ROOT / "report.md"
IF08_W6_CONTROLLED_PHASE = "IF-08 W6 Final Audit Controlled Execution"
IF08_W6_CONTROLLED_STATUS = "if08_w6_final_audit_controlled_execution_pass"
IF08_W6_CONTROLLED_PROJECT_SHA = "eae468c79687474de086c984b55a3f7ff47d73f7"
IF08_W6_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W6_CONTROLLED_NEXT_RECOMMENDED_STEP = "prepare_if09_evidence_bundle_vulnerability_register"
IF08_W6_CONTROLLED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27173423800"
IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA = "0358de95fd78c41fad2e257fec399d85e74193ce"
IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA = "36f4891c33d6a81eae74df1cfa5d3717cd6b4bc5"
IF08_W6_CONTROLLED_RECORDED_DRIFT_SHA = "0358de95c7fb80d06871a20ae46b8fbc3174c5d7"
IF08_W6_CONTROLLED_PREVIOUS_PHASE = "IF-08 W6 Final Audit Preflight Readiness"
IF08_W6_CONTROLLED_PREVIOUS_STATUS = "if08_w6_final_audit_preflight_readiness_pass"
IF08_W6_CONTROLLED_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_decision.json")
IF08_W6_CONTROLLED_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_summary.json")
IF08_W6_CONTROLLED_REPORT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_report.md")
IF08_W6_CONTROLLED_EVIDENCE_BUNDLE_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_evidence_bundle.json")
IF08_W6_CONTROLLED_MINOS_VERDICT_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_minos_verdict.json")
IF08_W6_CONTROLLED_SAFETY_ATTESTATION_PATH = _resolve_project_relative("artifacts", "infernus", "if08_w6_final_audit_controlled_execution_safety_attestation.json")
IF08_W6_CONTROLLED_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if08_w6_final_audit_controlled_execution.md")
IF08_W6_CONTROLLED_ROOT = ROOT / "artifacts" / "if08_w6_final_audit_controlled_execution"
IF08_W6_CONTROLLED_ACTIVE_DECISION_PATH = IF08_W6_CONTROLLED_ROOT / "decision.json"
IF08_W6_CONTROLLED_ACTIVE_SUMMARY_PATH = IF08_W6_CONTROLLED_ROOT / "summary.json"
IF08_W6_CONTROLLED_ACTIVE_REPORT_PATH = IF08_W6_CONTROLLED_ROOT / "report.md"
IF09_PHASE = "IF-09 Evidence Bundle + Vulnerability Register"
IF09_STATUS = "if09_evidence_bundle_vulnerability_register_pass"
IF09_PROJECT_SHA = "38b16edadce15ce8f2049bb3de8538bb921e344e"
IF09_PROJECT_CI_STATE = "CI_GREEN_CONFIRMED"
IF09_NEXT_RECOMMENDED_STEP = "prepare_if10_purgatorium_handoff_graph"
IF09_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27175174232"
IF09_SOURCE_PHASE = "IF-08 W6 Final Audit Controlled Execution"
IF09_SOURCE_STATUS = "if08_w6_final_audit_controlled_execution_pass"
IF09_SOURCE_PROJECT_SHA = "eae468c79687474de086c984b55a3f7ff47d73f7"
IF09_SOURCE_ACTIVE_CONTEXT_SHA = "373558e7360a8372f368a330a2d41cc28fc18033"
IF09_ROOT_MANIFEST_SHA = "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660"
IF09_ROOT = ROOT / "artifacts" / "if09_evidence_bundle_vulnerability_register"
IF09_ACTIVE_DECISION_PATH = IF09_ROOT / "decision.json"
IF09_ACTIVE_SUMMARY_PATH = IF09_ROOT / "summary.json"
IF09_ACTIVE_REPORT_PATH = IF09_ROOT / "report.md"
IF09_PROJECT_ROOT = _resolve_project_relative("artifacts", "infernus", "if09_evidence_bundle_vulnerability_register")
IF09_PROJECT_DECISION_PATH = IF09_PROJECT_ROOT / "decision.json"
IF09_PROJECT_SUMMARY_PATH = IF09_PROJECT_ROOT / "summary.json"
IF09_PROJECT_REPORT_PATH = IF09_PROJECT_ROOT / "report.md"
IF09_PROJECT_ROOT_MANIFEST_PATH = IF09_PROJECT_ROOT / "evidence_bundle_v4" / "root_manifest.json"
IF09_PROJECT_HASH_TREE_PATH = IF09_PROJECT_ROOT / "evidence_bundle_v4" / "hash_tree.json"
IF09_PROJECT_CUSTODY_CHAIN_PATH = IF09_PROJECT_ROOT / "evidence_bundle_v4" / "custody_chain.jsonl"
IF09_PROJECT_REPLAY_DIFF_PATH = IF09_PROJECT_ROOT / "evidence_bundle_v4" / "replay_diff_report.json"
IF09_PROJECT_MUTATION_SURVIVAL_PATH = IF09_PROJECT_ROOT / "evidence_bundle_v4" / "mutation_survival_report.json"
IF09_PROJECT_REGISTER_PATH = IF09_PROJECT_ROOT / "vuln_register_v4.jsonl"
IF09_PROJECT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if09_evidence_bundle_vulnerability_register.md")
IF10_PHASE = "IF-10 Purgatorium Handoff Graph"
IF10_STATUS = "if10_purgatorium_handoff_graph_pass"
IF10_PROJECT_SHA = "57106d9780af7a807bd58ea6039af3a7b1b23701"
IF10_PROJECT_CI_STATE = "CI_GREEN_CONFIRMED"
IF10_NEXT_RECOMMENDED_STEP = "prepare_if11_minos_final_verdict_closure"
IF10_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27176578203"
IF10_SOURCE_PHASE = "IF-09 Evidence Bundle + Vulnerability Register"
IF10_SOURCE_STATUS = "if09_evidence_bundle_vulnerability_register_pass"
IF10_SOURCE_PROJECT_SHA = "38b16edadce15ce8f2049bb3de8538bb921e344e"
IF10_SOURCE_ACTIVE_CONTEXT_SHA = "767138de3fb2b0484fca6be25657e08c21107574"
IF10_SOURCE_ROOT_MANIFEST_SHA = "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660"
IF10_GRAPH_SHA = "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1"
IF10_ROOT = ROOT / "artifacts" / "if10_purgatorium_handoff_graph"
IF10_ACTIVE_DECISION_PATH = IF10_ROOT / "decision.json"
IF10_ACTIVE_SUMMARY_PATH = IF10_ROOT / "summary.json"
IF10_ACTIVE_REPORT_PATH = IF10_ROOT / "report.md"
IF10_PROJECT_ROOT = _resolve_project_relative("artifacts", "infernus", "if10_purgatorium_handoff_graph")
IF10_PROJECT_DECISION_PATH = IF10_PROJECT_ROOT / "decision.json"
IF10_PROJECT_SUMMARY_PATH = IF10_PROJECT_ROOT / "summary.json"
IF10_PROJECT_REPORT_PATH = IF10_PROJECT_ROOT / "report.md"
IF10_PROJECT_GRAPH_PATH = IF10_PROJECT_ROOT / "purgatorium_handoff_graph_v4.json"
IF10_PROJECT_ROOT_CAUSE_PATH = IF10_PROJECT_ROOT / "root_cause_candidates.json"
IF10_PROJECT_REMEDIATION_PATH = IF10_PROJECT_ROOT / "remediation_tracks.json"
IF10_PROJECT_REGRESSION_PATH = IF10_PROJECT_ROOT / "regression_test_plan.json"
IF10_PROJECT_REVALIDATION_PATH = IF10_PROJECT_ROOT / "revalidation_wave_plan.json"
IF10_PROJECT_HANDOFF_MANIFEST_PATH = IF10_PROJECT_ROOT / "handoff_manifest.json"
IF10_PROJECT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if10_purgatorium_handoff_graph.md")
IF11_PHASE = "IF-11 Minos Final Verdict + Closure"
IF11_STATUS = "if11_minos_final_verdict_closure_pass"
IF11_PROJECT_SHA = "6312302ea45b72ddc310b2b33f56245be65b99dc"
IF11_PROJECT_CI_STATE = "CI_GREEN_CONFIRMED"
IF11_NEXT_RECOMMENDED_STEP = "prepare_purgatorium_handoff_or_operator_review"
IF11_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27177997351"
IF11_SOURCE_PHASE = "IF-10 Purgatorium Handoff Graph"
IF11_SOURCE_STATUS = "if10_purgatorium_handoff_graph_pass"
IF11_SOURCE_PROJECT_SHA = "57106d9780af7a807bd58ea6039af3a7b1b23701"
IF11_SOURCE_ACTIVE_CONTEXT_PRE_SYNC_SHA = "767138de3fb2b0484fca6be25657e08c21107574"
IF11_SOURCE_ACTIVE_CONTEXT_SYNC_SHA = "7755a1506e6981d3f1c5b3534c7217112a12b960"
IF11_SOURCE_ROOT_MANIFEST_SHA = "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660"
IF11_SOURCE_GRAPH_SHA = "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1"
IF11_ROOT = ROOT / "artifacts" / "if11_minos_final_verdict_closure"
IF11_ACTIVE_DECISION_PATH = IF11_ROOT / "decision.json"
IF11_ACTIVE_SUMMARY_PATH = IF11_ROOT / "summary.json"
IF11_ACTIVE_REPORT_PATH = IF11_ROOT / "report.md"
IF11_PROJECT_ROOT = _resolve_project_relative("artifacts", "infernus", "if11_minos_final_verdict_closure")
IF11_PROJECT_DECISION_PATH = IF11_PROJECT_ROOT / "decision.json"
IF11_PROJECT_SUMMARY_PATH = IF11_PROJECT_ROOT / "summary.json"
IF11_PROJECT_REPORT_PATH = IF11_PROJECT_ROOT / "report.md"
IF11_PROJECT_MECHANICAL_PATH = IF11_PROJECT_ROOT / "minos_mechanical_report_v4.json"
IF11_PROJECT_SEMANTIC_PATH = IF11_PROJECT_ROOT / "minos_semantic_report_v4.md"
IF11_PROJECT_OPERATOR_COSIGNATURE_PATH = IF11_PROJECT_ROOT / "operator_cosignature.json"
IF11_PROJECT_ANTI_THEATER_PATH = IF11_PROJECT_ROOT / "anti_theater_meta_audit_v4.json"
IF11_PROJECT_CLOSURE_PATH = IF11_PROJECT_ROOT / "infernus_closure_v4.json"
IF11_PROJECT_MANIFEST_PATH = IF11_PROJECT_ROOT / "closure_manifest.json"
IF11_PROJECT_FINAL_EVIDENCE_PATH = IF11_PROJECT_ROOT / "final_evidence_index.json"
IF11_PROJECT_READINESS_PATH = IF11_PROJECT_ROOT / "purgatorium_readiness_summary.json"
IF11_PROJECT_BOUNDARY_PATH = IF11_PROJECT_ROOT / "next_phase_boundary.json"
IF11_PROJECT_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "if11_minos_final_verdict_closure.md")
PURG_PRE_ROOT = ROOT / "artifacts" / "purgatorium"
PURG_PRE_DECISION_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_materialization_decision.json"
PURG_PRE_SUMMARY_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_materialization_summary.json"
PURG_PRE_REPORT_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_materialization_report.md"
PURG_PRE_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg_pre_no_real_execution_attestation.json"
PURG_PRE_EXCLUDENT_MANIFEST_PATH = PURG_PRE_ROOT / "purg_pre_infernus_canonroadmap_excludent_manifest.json"
PURG_PRE_ROUTE_OPENING_CANDIDATE_PATH = PURG_PRE_ROOT / "purg_pre_route_opening_candidate.json"
PURG_OPERATOR_REVIEW_DECISION_PATH = PURG_PRE_ROOT / "purg_operator_review_packet_decision.json"
PURG_OPERATOR_REVIEW_SUMMARY_PATH = PURG_PRE_ROOT / "purg_operator_review_packet_summary.json"
PURG_OPERATOR_REVIEW_REPORT_PATH = PURG_PRE_ROOT / "purg_operator_review_packet_report.md"
PURG_OPERATOR_REVIEW_SCHEMA_GAP_PATH = PURG_PRE_ROOT / "purg_route_admission_schema_gap_matrix.json"
PURG_OPERATOR_REVIEW_VALIDATOR_GAP_PATH = PURG_PRE_ROOT / "purg_route_admission_validator_gap_matrix.json"
PURG_OPERATOR_REVIEW_FUTURE_PATCH_PLAN_PATH = PURG_PRE_ROOT / "purg_route_admission_future_patch_plan.md"
PURG_OPERATOR_REVIEW_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg_route_admission_no_real_execution_attestation.json"
PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_decision.json"
PURG_PRE_ROUTE_ADMISSION_SUMMARY_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_summary.json"
PURG_PRE_ROUTE_ADMISSION_REPORT_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_report.md"
PURG_PRE_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_schema_patch_manifest.json"
PURG_PRE_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_validator_patch_manifest.json"
PURG_PRE_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_live_route_mutation_manifest.json"
PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_no_real_execution_attestation.json"
PURG_PRE_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_rollback_plan.md"
PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_decision.json"
PURG_PRE_AUTHORITY_EXECUTION_SUMMARY_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_summary.json"
PURG_PRE_AUTHORITY_EXECUTION_REPORT_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_report.md"
PURG_PRE_AUTHORITY_SOURCE_INDEX_PATH = PURG_PRE_ROOT / "purg_pre_authority_source_index.json"
PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH = PURG_PRE_ROOT / "purg_pre_handoff_source_reference_matrix.json"
PURG_PRE_NO_PURG00_ATTESTATION_PATH = PURG_PRE_ROOT / "purg_pre_no_purg00_attestation.json"
PURG_PRE_NO_REAL_EXECUTION_V2_PATH = PURG_PRE_ROOT / "purg_pre_no_real_execution_attestation_v2.json"
PURG_PRE_FUTURE_PURG00_CANDIDATE_PATH = PURG_PRE_ROOT / "purg_pre_future_purg00_admission_candidate.json"
PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_decision.json"
PURG00_OPERATOR_REVIEW_PACKET_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_summary.json"
PURG00_OPERATOR_REVIEW_PACKET_REPORT_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_report.md"
PURG00_ROUTE_ADMISSION_SCHEMA_GAP_PATH = PURG_PRE_ROOT / "purg00_route_admission_schema_gap_matrix.json"
PURG00_ROUTE_ADMISSION_VALIDATOR_GAP_PATH = PURG_PRE_ROOT / "purg00_route_admission_validator_gap_matrix.json"
PURG00_ROUTE_ADMISSION_FUTURE_PATCH_PLAN_PATH = PURG_PRE_ROOT / "purg00_route_admission_future_patch_plan.md"
PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg00_route_admission_no_real_execution_attestation.json"
PURG00_REQUIRED_SOURCE_ACCESS_MATRIX_PATH = PURG_PRE_ROOT / "purg00_required_source_access_matrix.json"
PURG00_NOT_OPENED_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_not_opened_attestation.json"
PURG00_ROUTE_ADMISSION_DECISION_PATH = PURG_PRE_ROOT / "purg00_route_admission_decision.json"
PURG00_ROUTE_ADMISSION_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_route_admission_summary.json"
PURG00_ROUTE_ADMISSION_REPORT_PATH = PURG_PRE_ROOT / "purg00_route_admission_report.md"
PURG00_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_schema_patch_manifest.json"
PURG00_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_validator_patch_manifest.json"
PURG00_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_live_route_mutation_manifest.json"
PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = PURG_PRE_ROOT / "purg00_route_admission_no_real_execution_attestation_v2.json"
PURG00_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH = PURG_PRE_ROOT / "purg00_route_admission_rollback_plan.md"
PURG00_HANDOFF_INTAKE_DECISION_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_decision.json"
PURG00_HANDOFF_INTAKE_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_summary.json"
PURG00_HANDOFF_INTAKE_REPORT_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_report.md"
PURG00_SOURCE_PACKET_INDEX_PATH = PURG_PRE_ROOT / "purg00_source_packet_index.json"
PURG00_HANDOFF_ID_CLASSIFICATION_MATRIX_PATH = PURG_PRE_ROOT / "purg00_handoff_id_classification_matrix.json"
PURG00_SOURCE_HASH_VERIFICATION_MATRIX_PATH = PURG_PRE_ROOT / "purg00_source_hash_verification_matrix.json"
PURG00_DATA_GAP_MATRIX_PATH = PURG_PRE_ROOT / "purg00_data_gap_matrix.json"
PURG00_NO_FIX_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_no_fix_attestation.json"
PURG00_NO_REAL_EXECUTION_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_no_real_execution_attestation.json"
PURG00_FUTURE_PURG01_TRIAGE_CANDIDATE_PATH = PURG_PRE_ROOT / "purg00_future_purg01_triage_candidate.json"
PURG00_INTAKE_DECISION_PATH = PURG_PRE_ROOT / "purg00_intake_decision.json"
PURGATORIUM_ROADMAP_PATH = ROOT / "project_mirror" / "docs" / "purgatorium_full" / "purgatorium_roadmapcanon.md"
INFERNUS_CANONROADMAP_STUB_PATH = ROOT / "project_mirror" / "docs" / "infernus_full" / "infernus_full_canonroadmap.md"
INFERNUS_CANONROADMAP_FORENSIC_PATH = ROOT / "excludent" / "infernus" / "roadmaps" / "infernus_full_canonroadmap.md"
CI_TERMINAL_REPORTING_RULE_ROOT = ROOT / "artifacts" / "ci_terminal_reporting_rule"
CI_TERMINAL_REPORTING_RULE_DECISION_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "decision.json"
CI_TERMINAL_REPORTING_RULE_SUMMARY_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "summary.json"
CI_TERMINAL_REPORTING_RULE_REPORT_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "report.md"
INFERNUS_STANDING_AUTHORIZATION_PATH = ROOT / "INFERNUS_STANDING_AUTHORIZATION.md"
INF_FULL_ROUTE_SYNC_DECISION_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "decision.json"
INF_FULL_ROUTE_SYNC_SUMMARY_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "summary.json"
INF_FULL_ROUTE_SYNC_REPORT_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "report.md"
INF_FULL_ROUTE_SYNC_WORKSPACE_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "workspace_hygiene_snapshot.txt"
PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH = ROOT / "artifacts" / "purgatorium" / "purg04_track_a_main_merge_execution_result.json"
PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH = ROOT / "artifacts" / "purgatorium" / "purg04_track_a_post_merge_validation_packet.json"

GOVERNANCE_CLASSES = {
    "governance_repair", "observability",
    "transition_engine", "contract", "route",
    "purgatorium_track_a_main_merge_execution",
    "purgatorium_post_merge_validation",
    "infernus_revalidation_route_admission",
    "infernus_revalidation_readiness",
    "infernus_revalidation_operator_authorization",
    "infernus_revalidation_execution",
    "infernus_revalidation_adjudication_or_closure",
}
CAPACITY_CLASSES = {
    "fixture_materialization", "bot_execution",
    "minos_verdict", "purgatorium", "benchux",
    "crisol", "bedrock", "product", "capability_build"
}

PHASE_DELIVERABLES = {
    "INF-MAT-01": lambda: (
        pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full").exists()
        and len(list(pathlib.Path(
            "fixtures/lab_simulation/aris_infernus_lab_full"
        ).iterdir())) >= 13
    ),
    "INF-BOT-01": lambda: (
        pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json").read_text(encoding="utf-8")
            ).get("log_sha256")
        )
    ),
    "INF-MINOS-01": lambda: (
        pathlib.Path("artifacts/inf_minos_01/minos_verdict.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/inf_minos_01/minos_verdict.json").read_text(encoding="utf-8")
            ).get("minos_verdict_sha256")
        )
    ),
    "PURG-01": lambda: (
        pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").read_text(encoding="utf-8")
            ).get("severity")
        )
        and bool(
            json.loads(
                pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").read_text(encoding="utf-8")
            ).get("status")
        )
    ),
    "PURG04_TRACK_A_MAIN_MERGE_EXECUTION": lambda: (
        PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH.exists()
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("artifact_type") == "track_a_main_merge_execution_result"
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("phase") == "PURG04_TRACK_A_MAIN_MERGE_EXECUTION"
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("diff_scope_allowed") is True
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("forbidden_paths_touched") == []
        and bool(_load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("merge_commit_sha"))
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("merge_executed") is True
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("project_aris_main_changed") is True
        and _load_json(PURG04_TRACK_A_MAIN_MERGE_EXECUTION_RESULT_PATH).get("project_aris_ci_state") == "CI_GREEN_CONFIRMED"
    ),
    "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET": lambda: (
        PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH.exists()
        and _load_json(PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH).get("phase_id") == "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET"
        and _load_json(PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH).get("post_merge_validation_passed") is True
        and (
            _load_json(PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH).get("project_aris_ci_state") == "CI_GREEN_CONFIRMED"
            or bool(_load_json(PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET_PATH).get("explicit_ci_confirmation_artifact"))
        )
    ),
    "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET": lambda: (
        PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH.exists()
        and _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH).get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET"
        and _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH).get("decision") == "pass"
        and _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH).get("live_route_opened") is True
        and _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH).get("new_live_phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET"
        and _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH).get("new_live_next_phase") is None
    ),
    "INF_REVALIDATION_ROUTE_ADMISSION_PACKET": lambda: (
        INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH.exists()
        and INF_REVALIDATION_REQUIRED_INPUTS_PATH.exists()
        and INF_REVALIDATION_SCOPE_MATRIX_PATH.exists()
        and INF_REVALIDATION_FORBIDDEN_ACTIONS_PATH.exists()
        and INF_REVALIDATION_NEXT_ROUTE_CANDIDATE_PATH.exists()
        and INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH.exists()
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET"
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("status") == "inf_revalidation_route_admission_opened"
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("selected_branch") == "TRACK_REVALIDATION_FIRST"
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("revalidation_executed") is False
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("finding_closed") is False
        and _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH).get("remediation_proven") is False
        and _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH).get("state_advanced") is True
        and _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH).get("target_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET"
    ),
    "INF_REVALIDATION_READINESS_PACKET": lambda: (
        INF_REVALIDATION_READINESS_PACKET_PATH.exists()
        and INF_REVALIDATION_SCENARIO_SCOPE_PATH.exists()
        and INF_REVALIDATION_ORACLE_CONTRACT_PATH.exists()
        and INF_REVALIDATION_ABORT_CRITERIA_PATH.exists()
        and INF_REVALIDATION_READINESS_NO_REAL_PATH.exists()
        and INF_REVALIDATION_READINESS_NEXT_ROUTE_CANDIDATE_PATH.exists()
        and INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH.exists()
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("phase_id") == "INF_REVALIDATION_READINESS_PACKET"
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("status") == "inf_revalidation_readiness_opened"
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("execution_authorized") is False
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("revalidation_executed") is False
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("finding_closed") is False
        and _load_json(INF_REVALIDATION_READINESS_PACKET_PATH).get("remediation_proven") is False
        and _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH).get("state_advanced") is True
        and _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH).get("target_phase_id") == "INF_REVALIDATION_READINESS_PACKET"
    ),
    "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET": lambda: (
        INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH.exists()
        and INF_REVALIDATION_EXECUTION_CONTRACT_PATH.exists()
        and INF_REVALIDATION_SAFETY_LOCK_MATRIX_PATH.exists()
        and INF_REVALIDATION_OPERATOR_AUTH_NO_REAL_PATH.exists()
        and INF_REVALIDATION_OPERATOR_AUTH_NEXT_ROUTE_CANDIDATE_PATH.exists()
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET"
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("status") == "inf_revalidation_operator_authorization_pass"
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("operator_authorized") is True
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("revalidation_executed_now") is False
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("finding_closed") is False
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH).get("remediation_proven") is False
        and _load_json(INF_REVALIDATION_OPERATOR_AUTH_NEXT_ROUTE_CANDIDATE_PATH).get("candidate_next_gate") == "INF_REVALIDATION_EXECUTION_PACKET"
    ),
    "INF_REVALIDATION_EXECUTION_PACKET": lambda: (
        INF_REVALIDATION_EXECUTION_PACKET_PATH.exists()
        and INF_REVALIDATION_EXECUTION_OPERATOR_COMMAND_PATH.exists()
        and INF_REVALIDATION_EXECUTION_TRANSITION_ROW_PATH.exists()
        and INF_REVALIDATION_EXECUTION_PREFLIGHT_PATH.exists()
        and INF_REVALIDATION_EXECUTION_COMMAND_LOG_PATH.exists()
        and INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH.exists()
        and INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH.exists()
        and INF_REVALIDATION_EXECUTION_EVIDENCE_INVENTORY_PATH.exists()
        and INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH.exists()
        and INF_REVALIDATION_EXECUTION_SUMMARY_PATH.exists()
        and INF_REVALIDATION_EXECUTION_VALIDATION_EVIDENCE_PATH.exists()
        and INF_REVALIDATION_EXECUTION_NEXT_ROUTE_CANDIDATE_PATH.exists()
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("phase_id") == "INF_REVALIDATION_EXECUTION_PACKET"
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("status") == "inf_revalidation_execution_pass"
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("oracle_result") == "pass"
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("finding_closure_candidate") is True
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("finding_closed") is False
        and _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH).get("remediation_proven") is False
        and _load_json(INF_REVALIDATION_EXECUTION_NEXT_ROUTE_CANDIDATE_PATH).get("candidate_next_gate") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET"
    ),
    "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET": lambda: (
        INF_REVALIDATION_ADJUDICATION_OPERATOR_COMMAND_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_TRANSITION_ROW_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_EVIDENCE_MATRIX_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_ORACLE_REVIEW_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_REGRESSION_REVIEW_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_NO_FORBIDDEN_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_CLOSURE_DECISION_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_SUMMARY_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_REPORT_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_VALIDATION_EVIDENCE_PATH.exists()
        and INF_REVALIDATION_ADJUDICATION_NEXT_ROUTE_CANDIDATE_PATH.exists()
        and _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH).get("phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET"
        and _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH).get("status") == "inf_revalidation_adjudication_closure_pass"
        and _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH).get("finding_closed") is True
        and _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH).get("remediation_proven") is True
        and _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH).get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface"
        and _load_json(INF_REVALIDATION_ADJUDICATION_NEXT_ROUTE_CANDIDATE_PATH).get("candidate_next_gate") is None
    ),
    "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET": lambda: (
        IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH.exists()
        and IF09_CLOSURE_MILESTONE_MIRROR_DRIFT_MATRIX_PATH.exists()
        and IF09_CLOSURE_MILESTONE_SUPERSEDED_NOTES_MANIFEST_PATH.exists()
        and IF09_CLOSURE_MILESTONE_NO_REAL_EXECUTION_ATTESTATION_PATH.exists()
        and IF09_CLOSURE_MILESTONE_VALIDATION_EVIDENCE_PATH.exists()
        and BENCHUX_ROUTE_OPENING_CANDIDATE_PATH.exists()
        and BENCHUX_PRE_ROUTE_SCOPE_NOTE_PATH.exists()
        and _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH).get("phase_id") == "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET"
        and _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH).get("status") == "if09_closure_milestone_mirror_sanity_pass"
        and _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH).get("target_finding_status") == "closed"
        and _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH).get("finding_closed") is True
        and _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH).get("remediation_proven") is True
        and _load_json(BENCHUX_ROUTE_OPENING_CANDIDATE_PATH).get("candidate_next_gate") == "BENCHUX_ROUTE_OPENING_PACKET"
        and _load_json(BENCHUX_ROUTE_OPENING_CANDIDATE_PATH).get("candidate_only") is True
        and _load_json(BENCHUX_ROUTE_OPENING_CANDIDATE_PATH).get("state_advanced") is False
    ),
    "ACB-CORE-01": lambda: (
        ACB_CORE_01_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CORE_01_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CORE_01_EVIDENCE_PATH).get("supply_chain_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CORE_01_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "uv_lock_exists",
                "pip_audit_gate_exists",
                "sbom_exists",
                "uv_bootstrap_exists",
            ]
        )
    ),
    "ACB-CORE-02": lambda: (
        ACB_CORE_02_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CORE_02_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CORE_02_EVIDENCE_PATH).get("core_public_api_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CORE_02_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "research_basis_exists",
                "snapshot_before_exists",
                "snapshot_after_exists",
                "import_stability_report_exists",
                "explicit_all_created_or_verified",
                "protocols_created_or_verified",
            ]
        )
    ),
    "ACB-CAP-01": lambda: (
        ACB_CAP_01_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_01_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_01_EVIDENCE_PATH).get("backend_baseline_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_01_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "fastapi_app_exists",
                "health_check_exists",
                "ready_check_exists",
                "jwt_auth_exists",
                "api_key_auth_exists",
                "tenant_isolation_exists",
                "slowapi_rate_limit_exists",
                "backend_tests_exist",
                "backend_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-02": lambda: (
        ACB_CAP_02_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_02_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_02_EVIDENCE_PATH).get("mcp_runtime_sandbox_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_02_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "mcp_runtime_package_exists",
                "stdio_ban_exists",
                "sandbox_spec_exists",
                "policy_pre_dispatch_exists",
                "kill_switch_exists",
                "rollback_contract_exists",
                "audit_event_exists",
                "mcp_runtime_tests_exist",
                "mcp_runtime_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-03": lambda: (
        ACB_CAP_03_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_03_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_03_EVIDENCE_PATH).get("runtime_public_api_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_03_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "runtime_package_exists",
                "runtime_public_api_documented",
                "runtime_public_api_contract_exists",
                "runtime_facade_exists",
                "runtime_modes_enforced",
                "runtime_policy_bridge_exists",
                "runtime_audit_hashing_exists",
                "public_api_drift_ratified",
                "runtime_tests_exist",
                "runtime_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-04": lambda: (
        ACB_CAP_04_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_04_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_04_EVIDENCE_PATH).get("product_pilot_boundary_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_04_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "product_boundary_package_exists",
                "pilot_gates_defined",
                "five_binary_gates_defined",
                "lab_to_staging_to_pilot_workflow_defined",
                "pilot_scope_contract_exists",
                "evidence_bundle_contract_exists",
                "pilot_runbook_contract_exists",
                "pilot_risk_matrix_exists",
                "non_authorization_statement_exists",
                "product_pilot_tests_exist",
                "product_pilot_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-05": lambda: (
        ACB_CAP_05_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_05_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_05_EVIDENCE_PATH).get("advanced_supply_chain_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_05_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "supply_chain_package_exists",
                "sbom_integrity_checker_exists",
                "sbom_integrity_report_exists",
                "attestation_envelope_exists",
                "offline_signature_test_verification_exists",
                "pypi_vulnerability_range_monitor_exists",
                "pypi_vulnerability_range_scan_exists",
                "aibom_prototype_exists",
                "infernus_full_spec_exists",
                "advanced_supply_chain_tests_exist",
                "advanced_supply_chain_artifacts_exist",
            ]
        )
    ),
    "INF-FULL-01": lambda: (
        True if not all(
            path.exists()
            for path in [
                INF_FULL_01_SCOPE_DECISION_PATH,
                INF_FULL_01_SCOPE_MATRIX_PATH,
                INF_FULL_01_SCOPE_MANIFEST_PATH,
                INF_FULL_01_SCOPE_CHARTER_PATH,
            ]
        ) else (
            _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("inf_full_opened") is True
            and _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("bots_executed") is False
            and _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("runtime_execution_authorized") is False
            and _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH).get("all_modules_accounted_for") is True
            and _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH).get("unresolved_modules") == []
        )
    ),
    "INF-FULL-02": lambda: (
        all(
            path.exists()
            for path in [
                INF_FULL_02_DECISION_PATH,
                INF_FULL_02_INVENTORY_PATH,
                INF_FULL_02_HASH_MANIFEST_PATH,
                INF_FULL_02_SUMMARY_PATH,
                INF_FULL_02_PLANNING_DOC_PATH,
            ]
        )
        and _load_json(INF_FULL_02_DECISION_PATH).get("minimum_deliverable_met") is True
        and _load_json(INF_FULL_02_DECISION_PATH).get("baseline_freeze_planned") is True
        and _load_json(INF_FULL_02_DECISION_PATH).get("baseline_freeze_applied") is False
        and _load_json(INF_FULL_02_SUMMARY_PATH).get("question_6_next_phase_after_inf_full_02", {}).get("canonical_next_phase") is None
    ),
    "INF-FULL-03": lambda: (
        all(
            path.exists()
            for path in [
                INFERNUS_FULL_CANONROADMAP_PATH,
                IF00_TRANSITION_CANDIDATE_PATH,
                IF00_HERMETICITY_PATH,
                IF01_LEDGER_PATH,
                IF02_ONTOLOGY_PATH,
                IF02_COVERAGE_PATH,
                IF03_ORACLE_PACK_PATH,
                IF04_BOT_PACK_PATH,
                IF04_PERMISSION_PATH,
            ]
        )
        and _load_json(IF00_TRANSITION_CANDIDATE_PATH).get("candidate_transition", {}).get("to_phase_id") == "INF-FULL-03"
        and _load_json(IF00_HERMETICITY_PATH).get("hermeticity_contract", {}).get("bots_may_run") is False
        and _load_json(IF03_ORACLE_PACK_PATH).get("planning_only") is True
        and _load_json(IF04_PERMISSION_PATH).get("capability_guards", {}).get("bot_execution_allowed") is False
    ),
    "INF-FULL-04": lambda: (
        all(
            path.exists()
            for path in [
                INF_FULL_OPERATOR_STANDING_AUTH_PATH,
                IF05_SCENARIO_PACK_PATH,
                IF05_CONTROLS_DESIGN_PATH,
                IF05_ORACLE_MAPPING_PATH,
                IF05_MUTATION_REGISTRY_PATH,
                IF06_HARNESS_READINESS_PATH,
                IF06_SANDBOX_CONTRACT_PATH,
                IF06_COST_QUOTA_PATH,
                IF06_REPLAY_POLICY_PATH,
                IF06_KILL_SWITCH_PATH,
                INF_FULL_04_DECISION_PATH,
                INF_FULL_04_SUMMARY_PATH,
                INF_FULL_04_DOC_PATH,
            ]
        )
        and _load_json(INF_FULL_OPERATOR_STANDING_AUTH_PATH).get("authorizes_pre_execution_gates_without_reasking_operator") is True
        and _load_json(IF05_SCENARIO_PACK_PATH).get("total_bots_covered") == 16
        and _load_json(IF06_HARNESS_READINESS_PATH).get("ready_for_inf_full_05_dry_run_evidence_simulation") is True
        and _load_json(INF_FULL_04_DECISION_PATH).get("minimum_deliverable_met") is True
    ),
    "INF-FULL-05": lambda: (
        all(
            path.exists()
            for path in [
                IF07_DECISION_PATH,
                IF07_NO_EXECUTION_PATH,
                IF07_SCENARIO_NORMALIZATION_PATH,
                IF07_VALIDATOR_EVIDENCE_PATH,
                INF_FULL_05_SUMMARY_PATH,
                INF_FULL_05_REPORT_PATH,
                INF_FULL_05_DOC_PATH,
            ]
        )
        and _load_json(IF07_DECISION_PATH).get("minimum_deliverable_satisfied") is True
        and _load_json(IF07_DECISION_PATH).get("historical_dry_run_naming_drift_interpreted_as_authorization") is False
        and _load_json(IF07_NO_EXECUTION_PATH).get("bot_execution_attempted") is False
        and _load_json(IF07_SCENARIO_NORMALIZATION_PATH).get("current_phase_planned_scenario_count") == 16
    ),
    "INF-FULL-07": lambda: (
        all(
            path.exists()
            for path in [
                INF_FULL_07_IF08_DECISION_PATH,
                INF_FULL_07_IF08_SUCCESSOR_MATRIX_PATH,
                INF_FULL_07_IF08_NO_EXECUTION_PATH,
                INF_FULL_07_IF08_VALIDATOR_EVIDENCE_PATH,
                INF_FULL_07_IF08_SUMMARY_PATH,
                INF_FULL_07_IF08_REPORT_PATH,
            ]
        )
        and _load_json(INF_FULL_07_IF08_DECISION_PATH).get("decision") == "pass"
        and _load_json(INF_FULL_07_IF08_DECISION_PATH).get("minimum_deliverable_satisfied") is True
        and _load_json(INF_FULL_07_IF08_NO_EXECUTION_PATH).get("if08_execution_attempted") is False
        and _load_json(INF_FULL_07_IF08_SUCCESSOR_MATRIX_PATH).get("transition_table_duplicate_after") is False
    ),
}

REQUIRED_BOOT_FILES = [
    "ACTIVE_CONTEXT_STATE.json",
    "ARIS_BOOT.md",
]

EXPECTED_PRIORITY_READ_ORDER = [
    "1. ACTIVE_CONTEXT_STATE.json",
    "2. ARIS_BOOT.md",
    "3. ROADMAP_CANONICAL.md (sob demanda — transição de fase)",
    "4. DECISION_LOCKS.md (sob demanda — locks de execução)",
    "5. LAB_OPERATING_CONTRACT.md (sob demanda — lab/Bedrock)",
    "6. INFERNUS_STANDING_AUTHORIZATION.md (sob demanda — fases Infernus)",
    "7. EXCLUDENT_POLICY.md (sob demanda — excludent/)",
    "8. BEDROCK_GATE.md (sob demanda — produto/Bedrock)",
]

BOOT_FILE_SUPERSEDED = [
    "AGENT_IDENTITY.md",
    "MANDATORY_READ_FIRST_RULES.md",
    "OPERATOR_PREFERENCES.md",
    "PROMPT_CONTRACT.md",
    "BOOT_PROFILE.md",
    "READ_PROFILE.md",
    "NORTH_POLE.md",
    "HANDOFF_RESPONSE_POLICY.md",
    "MODEL_REASONING_POLICY.md",
    "ACTIVE_CONTEXT_ANTI_CORRUPTION_CONTRACT.md",
    "ROADMAP_AMENDMENT_PROTOCOL.md",
]

OPERATOR_PREFERENCE_REQUIRED_PHRASES = [
    "operator sends a Codex result",
    "ritual phrase",
    "must not ask for confirmation just to send the next Codex prompt",
    "must not ask for repeated confirmation for the next pre-execution gates",
    "advance_mode=prompt_only",
    "ACTIVE_CONTEXT_STATE.json",
    "cannot override",
    "advance_mode=operator",
    "next_phase remains `null`",
    "ACB-CAP-05",
]

EXPECTED_FIXTURE_ASSERTION = """import json, sys, pathlib

state = json.loads(pathlib.Path("ACTIVE_CONTEXT_STATE.json").read_text())
fixtures_allowed = state.get("authorization", {}).get("fixture_materialization_allowed", False)
root = pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full")

existe = root.exists() and any(root.rglob("*"))
if existe and not fixtures_allowed:
    print("BLOCK: fixtures reais existem mas fixture_materialization_allowed=false")
    sys.exit(1)
if not existe and fixtures_allowed:
    print("WARN: materializacao autorizada mas nenhuma fixture criada")
    sys.exit(0)
print("OK")
"""

EXPECTED_WORKFLOW = """name: validate-active-context
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - name: Validar estado canonico
        run: python scripts/validate_active_context_state.py
      - name: Provar ausencia de fixture nao-autorizada
        run: python scripts/assert_no_unauthorized_fixtures.py
"""


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _ordered_positions(items: list[str], required: list[str], label: str) -> list[int]:
    missing = [item for item in required if item not in items]
    _require(not missing, f"{label} missing required entries: {missing}")
    positions = [items.index(item) for item in required]
    _require(positions == sorted(positions), f"{label} has out-of-order entries for required list")
    return positions


def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing required phrase: {phrase}")


FORBIDDEN_EXECUTION_FLAGS = (
    "runtime_executed",
    "real_apply_executed",
    "product_bedrock_real_apply_secrets_executed",
    "external_network_used_except_github_governance",
    "dependency_or_package_manager_used",
    "mcp_activated",
    "rag_ingestion_executed",
    "memory_write_executed",
    "socket_opened",
    "shell_executed",
    "filesystem_escape_performed",
    "real_cost_spent",
    "real_quota_consumed",
    "real_audio_capture_allowed",
    "real_stt_tts_allowed",
    "microphone_access_allowed",
    "voice_clone_or_impersonation_allowed",
)


def _require_forbidden_flags_false(payload: dict[str, Any], label: str) -> None:
    for key in FORBIDDEN_EXECUTION_FLAGS:
        _require(payload.get(key) is False, f"{label} {key} mismatch")


def _require_sha256_matches_if_accessible(path: pathlib.Path, expected_sha256: str, label: str) -> None:
    if not path.exists():
        return
    _require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_sha256, f"{label} physical sha mismatch")


def _check_forbidden_route_claims() -> None:
    _require(EXPECTED_PHASE != "PURG-00", "latest completed phase cannot be PURG-00 here")
    _require(EXPECTED_LATEST_COMPLETED_STATUS not in {"purg_00_pass", "purg00_pass"}, "latest completed status cannot be PURG-00 pass here")


def _value_at_path(data: dict[str, Any], dotted_path: str) -> Any:
    value: Any = data
    for segment in dotted_path.split("."):
        _require(isinstance(value, dict) and segment in value, f"missing path: {dotted_path}")
        value = value[segment]
    return value


def _canonical_hash_without_field(data: dict[str, Any], field: str) -> str:
    payload = dict(data)
    payload.pop(field, None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _require_paths_match(state: dict[str, Any], paths: list[str], label: str) -> None:
    baseline_value = _value_at_path(state, paths[0])
    for other_path in paths[1:]:
        _require(_value_at_path(state, other_path) == baseline_value, f"{label} drift")


def _require_files_exist(state: dict[str, Any]) -> None:
    # required_files_for_transition was removed in the active-context compaction refactor.
    # Layer 0 boot files (ACTIVE_CONTEXT_STATE.json + ARIS_BOOT.md) are verified in _warn_boot_receipt.
    # Layer 1 reference files are verified individually where relevant.
    pass


def _check_gate_ttl(state: dict[str, Any]) -> None:
    gate_opened_at = state["gate_opened_at"]
    gate_max_cycles = state["gate_max_cycles"]
    gate_cycles_used = state["gate_cycles_used"]
    _require(isinstance(gate_opened_at, str) and gate_opened_at != "", "gate_opened_at must be a non-empty ISO date string")
    _require(isinstance(gate_max_cycles, int), "gate_max_cycles must be an integer")
    _require(isinstance(gate_cycles_used, int), "gate_cycles_used must be an integer")
    _require(gate_cycles_used >= 0, "gate_cycles_used must be non-negative")
    if gate_cycles_used >= gate_max_cycles:
        raise SystemExit("BLOCK: gate cycle budget exhausted. Operator must close or extend.")


def _check_auto_advance(state: dict[str, Any]) -> None:
    auto = state["auto_advance"]
    _require(isinstance(auto.get("enabled"), bool), "auto_advance.enabled must be boolean")
    _require(isinstance(auto.get("allowed_phase_classes"), list), "auto_advance.allowed_phase_classes must be a list")
    _require(isinstance(auto.get("blocked_phase_classes"), list), "auto_advance.blocked_phase_classes must be a list")
    _require(isinstance(auto.get("condition"), str) and auto["condition"] != "", "auto_advance.condition must be a non-empty string")
    overlap = set(auto["allowed_phase_classes"]) & set(auto["blocked_phase_classes"])
    _require(not overlap, f"auto_advance phase classes overlap: {sorted(overlap)}")


def _preference_allows_direct_prompt(
    *,
    advance_mode: str,
    previous_phase_pass: bool,
    ci_green: bool,
    validator_green: bool,
    manual_authorization_required: bool,
) -> bool:
    return (
        advance_mode == "prompt_only"
        and previous_phase_pass
        and ci_green
        and validator_green
        and not manual_authorization_required
    )


def classify_ci_terminal_state(workflows: list[dict[str, Any]]) -> str:
    if not workflows:
        raise ValueError("at least one workflow is required")

    pending_statuses = {"queued", "waiting", "requested", "in_progress"}
    failed_conclusions = {"failure", "cancelled", "timed_out", "action_required", "startup_failure", "stale"}

    for workflow in workflows:
        status = workflow.get("status")
        conclusion = workflow.get("conclusion")
        if status in pending_statuses:
            return "CI_PENDING"
        if status != "completed":
            return "CI_PENDING"
        if conclusion in failed_conclusions:
            return "CI_FAILED"
        if conclusion != "success":
            return "CI_FAILED"

    return "CI_GREEN_CONFIRMED"


def _parse_transition_table() -> list[dict[str, str]]:
    roadmap_text = (ROOT / "ROADMAP_CANONICAL.md").read_text(encoding="utf-8")
    rows: list[dict[str, str]] = []
    in_table = False
    for line in roadmap_text.splitlines():
        if line.startswith("## Transition Table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table or not line.strip().startswith("|"):
            continue
        if set(line.replace("|", "").replace("-", "").strip()) == set():
            continue
        parts = [part.strip() for part in line.split("|")[1:-1]]
        if len(parts) != 6 or parts[0] == "current_phase_id":
            continue
        rows.append(
            {
                "current_phase_id": parts[0],
                "decision": parts[1],
                "next_phase_id": parts[2],
                "next_phase_class": parts[3],
                "advance_mode": parts[4],
                "minimum_deliverable": parts[5],
            }
        )
    return rows


def _get_transition_row(current_phase_id: str, decision: str) -> dict[str, str] | None:
    for row in _parse_transition_table():
        if row["current_phase_id"] == current_phase_id and row["decision"] == decision:
            return row
    return None


def _load_live_position() -> dict[str, str]:
    state = _load_json(STATE_PATH)
    transition_row = _get_transition_row(state.get("current_phase_id", ""), state.get("decision", ""))
    next_action = state.get("next_action") or {}
    history_summary = state.get("history_summary") or {}
    last_transition = state.get("last_transition") or {}
    active_next_phase = state.get("active_next_phase", "")
    active_next_phase_class = state.get("active_next_phase_class", "")
    if transition_row is not None:
        active_next_phase = active_next_phase or transition_row.get("next_phase_id", "")
        active_next_phase_class = active_next_phase_class or transition_row.get("next_phase_class", "")
    return {
        "phase_id": state.get("phase_id", ""),
        "current_phase_id": state.get("current_phase_id", ""),
        "previous_phase_id": state.get("previous_phase_id", ""),
        "status": state.get("status", ""),
        "current_status": state.get("current_status", ""),
        "latest_completed_phase": state.get("latest_completed_phase", ""),
        "latest_completed_status": state.get("latest_completed_status", ""),
        "schema_version": state.get("schema_version", ""),
        "active_next_phase": active_next_phase,
        "active_next_phase_class": active_next_phase_class,
        "phase_class": state.get("phase_class", ""),
        "latest_completed_next_recommended_step": state.get("latest_completed_next_recommended_step", ""),
        "latest_completed_project_commit_sha": state.get("latest_completed_project_commit_sha", ""),
        "latest_completed_ci_state": state.get("latest_completed_ci_state", ""),
        "previous_execution_phase": history_summary.get("previous_execution_phase", ""),
        "last_transition_from_phase": last_transition.get("from_phase", ""),
        "next_action_phase": next_action.get("phase", ""),
        "next_action_phase_class": next_action.get("phase_class", ""),
        "next_action_status": next_action.get("status", ""),
    }


# ── CURRENT LIVE POSITION (derived from STATE.json at startup) ──────────────
# DO NOT HARDCODE VALUES HERE. Edit STATE.json + regenerate BOOT.md instead.
_live = _load_live_position()
CURRENT_LIVE_PHASE_ID = _live["phase_id"]
CURRENT_LIVE_PREVIOUS_PHASE_ID = _live["previous_phase_id"]
CURRENT_LIVE_PHASE = _live["latest_completed_phase"]
CURRENT_LIVE_STATUS = _live["status"]
CURRENT_LIVE_CURRENT_STATUS = _live["current_status"]
CURRENT_LIVE_SCHEMA_VERSION = _live["schema_version"]
CURRENT_LIVE_NEXT_RECOMMENDED_STEP = _live["latest_completed_next_recommended_step"]
CURRENT_LIVE_LATEST_COMPLETED_PROJECT_SHA = _live["latest_completed_project_commit_sha"]
CURRENT_LIVE_LATEST_COMPLETED_CI_STATE = _live["latest_completed_ci_state"]
CURRENT_LIVE_PREVIOUS_EXECUTION_PHASE = _live["previous_execution_phase"]
CURRENT_LIVE_LAST_TRANSITION_FROM_PHASE = _live["last_transition_from_phase"]
CURRENT_LIVE_NEXT_ACTION_NOTE = (
    NO_TRANSITION_DEFINED_MESSAGE
    if _live["active_next_phase"] is None
    else f"Next: {_live['active_next_phase']}"
)
CURRENT_LIVE_PHASE_CLASS = _live["phase_class"]
CURRENT_EXPECTED_NEXT_PHASE_ID = _live["active_next_phase"]
CURRENT_EXPECTED_NEXT_PHASE_CLASS = _live["active_next_phase_class"]
# ─────────────────────────────────────────────────────────────────────────────


def _check_next_phase_in_transition_table(state: dict[str, Any]) -> None:
    row = _get_transition_row(state.get("current_phase_id", ""), state.get("decision", ""))
    if (
        state.get("current_phase_id") == CURRENT_LIVE_PHASE_ID
        and state.get("decision") == EXPECTED_DECISION
        and state.get("status") == CURRENT_LIVE_STATUS
        and row is None
    ):
        row = {
            "next_phase_id": CURRENT_EXPECTED_NEXT_PHASE_ID,
            "next_phase_class": CURRENT_EXPECTED_NEXT_PHASE_CLASS,
        }
    if state.get("status") in PURG00_LIVE_ROUTE_PRESERVING_STATUSES:
        row = _get_transition_row(PURG_PRE_LIVE_ROUTE_PHASE_ID, "pass")
        _require(row is not None, "BLOCK: PURG-PRE route successor must exist in Transition Table")
    if state.get("status") == PURG01_ROUTE_ADMISSION_STATUS:
        row = _get_transition_row(EXPECTED_NEXT_PHASE_ID, "pass")
        _require(row is not None, "BLOCK: PURG-00 route successor must exist in Transition Table")
    if row is None:
        _require(state.get("next_phase") is None, "BLOCK: terminal phase without successor must keep next_phase null")
        _require(state.get("active_next_phase") is None, "BLOCK: terminal phase without successor must keep active_next_phase null")
        return
    next_phase = state.get("next_phase")
    _require(next_phase == row["next_phase_id"], f"BLOCK: next_phase '{next_phase}' must match Transition Table '{row['next_phase_id']}'")
    _require(state.get("active_next_phase") == row["next_phase_id"], "BLOCK: active_next_phase must match Transition Table next phase")
    _require(
        state.get("active_next_phase_class") == row["next_phase_class"],
        "BLOCK: active_next_phase_class must match Transition Table next phase class",
    )


def _check_schema_state_contract(state: dict[str, Any]) -> None:
    schema = _load_json(SCHEMA_PATH)
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))

    _require(
        state.get("active_context_version") in properties.get("active_context_version", {}).get("enum", []),
        "ACTIVE_CONTEXT_SCHEMA.json active_context_version enum must include the live state version",
    )
    _require(
        state.get("schema_version") in properties.get("schema_version", {}).get("enum", []),
        "ACTIVE_CONTEXT_SCHEMA.json schema_version enum must include the live state schema_version",
    )

    missing_state_keys = sorted(set(state) - set(properties))
    _require(not missing_state_keys, f"ACTIVE_CONTEXT_SCHEMA.json missing live state properties: {missing_state_keys}")

    missing_required = sorted(required - set(state))
    _require(not missing_required, f"ACTIVE_CONTEXT_SCHEMA.json requires keys absent from live state: {missing_required}")

    artifact_routes_schema = properties.get("artifact_routes", {})
    artifact_route_properties = artifact_routes_schema.get("properties", {})
    artifact_route_required = set(artifact_routes_schema.get("required", []))
    live_artifact_routes = state.get("artifact_routes", {})

    _require(
        set(artifact_route_properties) == set(live_artifact_routes),
        "ACTIVE_CONTEXT_SCHEMA.json artifact_routes keys must match the live state exactly",
    )
    _require(
        artifact_route_required == set(live_artifact_routes),
        "ACTIVE_CONTEXT_SCHEMA.json artifact_routes required keys must match the live state exactly",
    )
    for key, value in live_artifact_routes.items():
        _require(
            artifact_route_properties.get(key, {}).get("const") == value,
            f"ACTIVE_CONTEXT_SCHEMA.json artifact_routes.{key} const mismatch",
        )

    versioning_contract = state.get("versioning_contract", {})
    versioning_properties = properties.get("versioning_contract", {}).get("properties", {})
    missing_versioning_keys = sorted(set(versioning_contract) - set(versioning_properties))
    _require(
        not missing_versioning_keys,
        f"ACTIVE_CONTEXT_SCHEMA.json versioning_contract missing live keys: {missing_versioning_keys}",
    )
    _require(
        versioning_contract.get("current_active_context_version") == state.get("active_context_version"),
        "versioning_contract.current_active_context_version must match active_context_version",
    )
    _require(
        versioning_contract.get("current_schema_version") == state.get("schema_version"),
        "versioning_contract.current_schema_version must match schema_version",
    )

    benchuix_track = state.get("benchuix_track")
    if benchuix_track is not None:
        _require(benchuix_track.get("status") == "operator_review_pending", "benchuix_track.status mismatch")
        _require(benchuix_track.get("roadmap_path") == "Benchuix_roadmap.md", "benchuix_track.roadmap_path mismatch")
        _require(benchuix_track.get("roadmap_hash") == "e0588eca8af0c0c083f7607cc903c06dedd6511423a838458674b50359b160e5", "benchuix_track.roadmap_hash mismatch")
        _require(benchuix_track.get("current_candidate_phase") == "BENCHUIX-00", "benchuix_track.current_candidate_phase mismatch")
        _require(benchuix_track.get("latest_candidate_decision") == "READY_FOR_OPERATOR_REVIEW", "benchuix_track.latest_candidate_decision mismatch")
        _require(benchuix_track.get("schema_tracking_repair_required") is True, "benchuix_track.schema_tracking_repair_required mismatch")
        _require(benchuix_track.get("schema_tracking_repair_status") == "completed", "benchuix_track.schema_tracking_repair_status mismatch")
        _require(benchuix_track.get("admission_commit_sha") == "89443c9c80df69568da0c7c2efdb0a72b6e371af", "benchuix_track.admission_commit_sha mismatch")
        _require(benchuix_track.get("admission_ci_state") == "CI_GREEN_CONFIRMED", "benchuix_track.admission_ci_state mismatch")
        _require(benchuix_track.get("admission_github_actions_run_id") == "27582515556", "benchuix_track.admission_github_actions_run_id mismatch")
        _require(benchuix_track.get("transition_table_artifact") == "artifacts/benchuix/00_transition_table.json", "benchuix_track.transition_table_artifact mismatch")
        _require(benchuix_track.get("admission_packet_artifact") == "artifacts/benchuix/00_admission_packet.json", "benchuix_track.admission_packet_artifact mismatch")
        _require(benchuix_track.get("no_real_execution_attestation_artifact") == "artifacts/benchuix/00_no_real_execution_attestation.json", "benchuix_track.no_real_execution_attestation_artifact mismatch")
        _require(benchuix_track.get("trilha_lock_active") is True, "benchuix_track.trilha_lock_active mismatch")
        _require(benchuix_track.get("candidate_next_phase_after_operator_gate") == "BENCHUIX-01", "benchuix_track.candidate_next_phase_after_operator_gate mismatch")
        for key in (
            "execution_authorized",
            "product_authorized",
            "production_authorized",
            "real_apply_authorized",
            "runtime_integration_allowed",
            "secrets_access_authorized",
        ):
            _require(benchuix_track.get(key) is False, f"benchuix_track.{key} must be false")
        _require((ROOT / benchuix_track["roadmap_path"]).exists(), "benchuix_track roadmap_path missing on disk")
        _require((ROOT / benchuix_track["transition_table_artifact"]).exists(), "benchuix_track transition_table_artifact missing on disk")
        _require((ROOT / benchuix_track["admission_packet_artifact"]).exists(), "benchuix_track admission_packet_artifact missing on disk")
        _require((ROOT / benchuix_track["no_real_execution_attestation_artifact"]).exists(), "benchuix_track no_real_execution_attestation_artifact missing on disk")


def _check_minimum_deliverable(state: dict[str, Any]) -> None:
    phase_id = state.get("current_phase_id", "")
    decision = state.get("decision", "")
    if decision != "pass":
        return
    if phase_id not in PHASE_DELIVERABLES:
        return
    if not PHASE_DELIVERABLES[phase_id]():
        print(f"BLOCK: {phase_id} declared pass but minimum_deliverable not met")
        sys.exit(1)


def _check_governance_streak(state: dict[str, Any]) -> None:
    streak = state.get("governance_gate_streak", 0)
    phase_class = state.get("phase_class", "")
    if phase_class not in GOVERNANCE_CLASSES:
        return
    if streak >= 3:
        print("BLOCK: governance_gate_streak >= 3.")
        print("3 governance gates consecutivos sem capacidade real.")
        print("Proximo gate obrigatorio: classe de capacidade.")
        print("Operador deve autorizar explicitamente.")
        sys.exit(1)
    if streak == 2:
        print("WARN: governance_gate_streak=2. Proximo gate DEVE ser capacidade.")


def _check_purg04_track_a_post_merge_validation_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET":
        return

    operator_auth = _load_json(PURG04_POST_MERGE_VALIDATION_OPERATOR_AUTH_PATH)
    _require(
        operator_auth.get("operator_authorization_text") == "Autorizo PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET.",
        "post-merge validation operator authorization text mismatch",
    )
    _require(
        operator_auth.get("authorization_scope") == "post_merge_validation_packet_only",
        "post-merge validation operator authorization scope mismatch",
    )
    _require(operator_auth.get("project_aris_mutation_authorized") is False, "post-merge validation must not authorize Project_ARIS mutation")
    _require(operator_auth.get("finding_close_authorized") is False, "post-merge validation must not authorize finding close")

    packet = _load_json(PURG04_POST_MERGE_VALIDATION_PACKET_PATH)
    _require(packet.get("artifact_id") == "purg04_track_a_post_merge_validation_packet", "post-merge validation artifact_id mismatch")
    _require(packet.get("phase_id") == "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET", "post-merge validation phase_id mismatch")
    _require(
        packet.get("source_merge_execution_artifact") == "artifacts/purgatorium/purg04_track_a_main_merge_execution_result.json",
        "post-merge validation source_merge_execution_artifact mismatch",
    )
    _require(
        packet.get("source_sync_repair_artifact") == "artifacts/purgatorium/purg04_active_context_canonical_sync_repair_after_track_a_main_merge.json",
        "post-merge validation source_sync_repair_artifact mismatch",
    )
    _require(packet.get("project_merge_commit") == "7883af5a32c629026bfc6dc15ebee4ebbcadd295", "post-merge validation merge commit mismatch")
    _require(packet.get("patch_commit") == "1e9a04a02846f3261ae72d0c95fbee6b0163b45b", "post-merge validation patch commit mismatch")
    _require(packet.get("project_ci_state") == "CI_GREEN_CONFIRMED", "post-merge validation project ci mismatch")
    _require(packet.get("forbidden_paths_touched") == [], "post-merge validation forbidden_paths_touched mismatch")
    _require(packet.get("post_merge_validation_passed") is True, "post-merge validation must pass")
    _require(packet.get("project_aris_changed") is False, "post-merge validation must not change Project_ARIS")
    _require(packet.get("runtime_executed") is False, "post-merge validation runtime_executed must be false")
    _require(packet.get("real_apply_executed") is False, "post-merge validation real_apply_executed must be false")
    _require(
        packet.get("product_bedrock_real_apply_secrets_executed") is False,
        "post-merge validation product_bedrock_real_apply_secrets_executed must be false",
    )
    _require(
        packet.get("dependency_or_package_manager_used") is False,
        "post-merge validation dependency_or_package_manager_used must be false",
    )
    _require(packet.get("finding_closed") is False, "post-merge validation finding_closed must be false")
    _require(packet.get("remediation_proven") is False, "post-merge validation remediation_proven must be false")
    _require(packet.get("decision") == "pass", "post-merge validation decision mismatch")
    _require(
        packet.get("recommended_next_step") == NO_TRANSITION_DEFINED_MESSAGE,
        "post-merge validation recommended_next_step mismatch",
    )

    no_real = _load_json(PURG04_POST_MERGE_VALIDATION_NO_REAL_PATH)
    _require(
        no_real.get("phase_id") == "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET",
        "post-merge validation no-real-execution phase_id mismatch",
    )
    for key in (
        "project_aris_changed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "secrets_accessed",
    ):
        _require(no_real.get(key) is False, f"post-merge validation no-real-execution {key} must be false")


def _check_purg_residual_risk_carry_forward_route_opening_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET":
        return

    _require(PURG_RESIDUAL_ROUTE_OPENING_REPORT_PATH.exists(), "missing residual route-opening report")

    operator_auth = _load_json(PURG_RESIDUAL_ROUTE_OPENING_OPERATOR_AUTH_PATH)
    _require(
        operator_auth.get("operator_authorization_text")
        == "AUTHORIZE_ROUTE_OPENING_PACKET_FOR_PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
        "residual route-opening operator authorization text mismatch",
    )
    _require(
        operator_auth.get("authorization_scope")
        == "route_opening_packet_for_purg_residual_risk_carry_forward_only",
        "residual route-opening operator authorization scope mismatch",
    )
    _require(operator_auth.get("route_opening_only") is True, "residual route-opening must remain route-opening only")
    for key in (
        "project_aris_mutation_authorized",
        "finding_close_authorized",
        "remediation_proven_override_authorized",
        "runtime_authorized",
        "real_apply_authorized",
        "production_authorized",
        "product_authorized",
        "bedrock_authorized",
        "secrets_authorized",
        "dependency_or_package_manager_authorized",
        "proof_loop_execution_authorized",
    ):
        _require(operator_auth.get(key) is False, f"residual route-opening operator authorization {key} must be false")

    packet = _load_json(PURG_RESIDUAL_ROUTE_OPENING_PACKET_PATH)
    _require(packet.get("artifact_id") == "purg_residual_risk_carry_forward_route_opening_packet", "residual route-opening artifact_id mismatch")
    _require(packet.get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening phase_id mismatch")
    _require(packet.get("authorization_artifact") == "artifacts/purgatorium/purg_residual_risk_carry_forward_route_opening_operator_authorization.json", "residual route-opening authorization artifact mismatch")
    _require(packet.get("source_candidate_next_gate") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening candidate_next_gate mismatch")
    _require(packet.get("operator_authorized") is True, "residual route-opening must be operator authorized")
    _require(packet.get("candidate_chain_verified") is True, "residual route-opening candidate chain must be verified")
    _require(packet.get("live_route_opened") is True, "residual route-opening must open the live route")
    _require(packet.get("state_advanced") is True, "residual route-opening must advance state")
    _require(packet.get("previous_live_phase_id") == "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET", "residual route-opening previous_live_phase_id mismatch")
    _require(packet.get("new_live_phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening new_live_phase_id mismatch")
    _require(packet.get("new_live_phase_class") == "purgatorium_route_admission", "residual route-opening new_live_phase_class mismatch")
    _require(packet.get("new_live_status") == "purg_residual_risk_carry_forward_route_opening_pass", "residual route-opening new_live_status mismatch")
    _require(packet.get("new_live_next_phase") is None, "residual route-opening new_live_next_phase must be null")
    _require(packet.get("new_live_active_next_phase") is None, "residual route-opening new_live_active_next_phase must be null")
    _require(packet.get("latest_completed_project_commit_sha") == "7883af5a32c629026bfc6dc15ebee4ebbcadd295", "residual route-opening latest_completed_project_commit_sha mismatch")
    _require(packet.get("latest_completed_ci_state") == "CI_GREEN_CONFIRMED", "residual route-opening latest_completed_ci_state mismatch")
    _require(packet.get("recommended_next_step") == NO_TRANSITION_DEFINED_MESSAGE, "residual route-opening recommended_next_step mismatch")
    _require(packet.get("project_aris_changed") is False, "residual route-opening must not change Project_ARIS")
    _require(packet.get("project_aris_tests_executed") is False, "residual route-opening must not execute Project_ARIS tests")
    _require(packet.get("proof_loop_executed") is False, "residual route-opening proof_loop_executed must be false")
    _require(packet.get("runtime_executed") is False, "residual route-opening runtime_executed must be false")
    _require(packet.get("real_apply_executed") is False, "residual route-opening real_apply_executed must be false")
    _require(packet.get("finding_closed") is False, "residual route-opening finding_closed must be false")
    _require(packet.get("remediation_proven") is False, "residual route-opening remediation_proven must be false")
    _require(packet.get("decision") == "pass", "residual route-opening decision mismatch")

    summary = _load_json(PURG_RESIDUAL_ROUTE_OPENING_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening summary phase_id mismatch")
    _require(summary.get("status") == "purg_residual_risk_carry_forward_route_opening_pass", "residual route-opening summary status mismatch")
    _require(summary.get("live_route_opened") is True, "residual route-opening summary must report live_route_opened=true")
    _require(summary.get("next_phase") is None, "residual route-opening summary next_phase must be null")
    _require(summary.get("active_next_phase") is None, "residual route-opening summary active_next_phase must be null")

    lock_matrix = _load_json(PURG_RESIDUAL_ROUTE_OPENING_LOCK_MATRIX_PATH)
    _require(lock_matrix.get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening lock matrix phase_id mismatch")
    for key in (
        "project_aris_mutation_authorized",
        "project_aris_tests_authorized",
        "proof_loop_execution_authorized",
        "runtime_authorized",
        "real_apply_authorized",
        "production_authorized",
        "product_authorized",
        "bedrock_authorized",
        "secrets_authorized",
        "dependency_or_package_manager_authorized",
        "finding_close_authorized",
        "remediation_override_authorized",
    ):
        _require(lock_matrix.get(key) is False, f"residual route-opening lock matrix {key} must be false")

    no_real = _load_json(PURG_RESIDUAL_ROUTE_OPENING_NO_REAL_PATH)
    _require(no_real.get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "residual route-opening no-real phase_id mismatch")
    for key in (
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "secrets_accessed",
    ):
        _require(no_real.get(key) is False, f"residual route-opening no-real {key} must be false")

    validation_evidence = _load_json(PURG_RESIDUAL_ROUTE_OPENING_VALIDATION_EVIDENCE_PATH)
    _require(
        validation_evidence.get("phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
        "residual route-opening validation evidence phase_id mismatch",
    )
    _require(
        validation_evidence.get("status") == "purg_residual_risk_carry_forward_route_opening_pass",
        "residual route-opening validation evidence status mismatch",
    )


def _check_inf_revalidation_route_activation_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "INF_REVALIDATION_ROUTE_ADMISSION_PACKET":
        return

    for path in (
        INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH,
        INF_REVALIDATION_REQUIRED_INPUTS_PATH,
        INF_REVALIDATION_SCOPE_MATRIX_PATH,
        INF_REVALIDATION_FORBIDDEN_ACTIONS_PATH,
        INF_REVALIDATION_NEXT_ROUTE_CANDIDATE_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_TRANSITION_ROW_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_NO_REAL_PATH,
        INF_REVALIDATION_ROUTE_ACTIVATION_NEXT_ROUTE_CANDIDATE_PATH,
    ):
        _require(path.exists(), f"missing INF revalidation route activation artifact: {path}")

    route_packet = _load_json(INF_REVALIDATION_ROUTE_ADMISSION_PACKET_PATH)
    _require(route_packet.get("artifact_id") == "inf_revalidation_route_admission_packet", "INF route admission artifact_id mismatch")
    _require(route_packet.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF route admission phase_id mismatch")
    _require(route_packet.get("phase_class") == "infernus_revalidation_route_admission", "INF route admission phase_class mismatch")
    _require(route_packet.get("status") == "inf_revalidation_route_admission_opened", "INF route admission status mismatch")
    _require(route_packet.get("selected_branch") == "TRACK_REVALIDATION_FIRST", "INF route admission selected_branch mismatch")
    _require(route_packet.get("source_activation_decision") == "artifacts/purgatorium/purg_remaining_roadmap_activation_decision_packet.json", "INF route admission source_activation_decision mismatch")
    _require(route_packet.get("source_activation_packet") == "artifacts/purgatorium/inf_revalidation_route_activation_packet.json", "INF route admission source_activation_packet mismatch")
    _require(route_packet.get("previous_live_phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "INF route admission previous_live_phase_id mismatch")
    _require(route_packet.get("next_phase") is None, "INF route admission next_phase must be null")
    _require(route_packet.get("active_next_phase") is None, "INF route admission active_next_phase must be null")
    _require(route_packet.get("finding_id") == "IF09-FIND-001", "INF route admission finding_id mismatch")
    for key in (
        "operator_authorized",
        "route_activation_only",
        "state_advanced",
        "required_inputs_recorded",
        "scope_matrix_recorded",
        "forbidden_actions_recorded",
    ):
        _require(route_packet.get(key) is True, f"INF route admission {key} must be true")
    for key in (
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "revalidation_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(route_packet.get(key) is False, f"INF route admission {key} must be false")
    _require(route_packet.get("decision") == "pass", "INF route admission decision mismatch")

    required_inputs = _load_json(INF_REVALIDATION_REQUIRED_INPUTS_PATH)
    _require(required_inputs.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF required inputs phase_id mismatch")
    _require(required_inputs.get("selected_branch") == "TRACK_REVALIDATION_FIRST", "INF required inputs selected_branch mismatch")
    _require(required_inputs.get("operator_authorized_route_activation") is True, "INF required inputs operator authorization mismatch")

    scope_matrix = _load_json(INF_REVALIDATION_SCOPE_MATRIX_PATH)
    _require(scope_matrix.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF scope matrix phase_id mismatch")
    _require(scope_matrix.get("route_activation_only") is True, "INF scope matrix route_activation_only mismatch")
    _require(scope_matrix.get("revalidation_execution_in_scope") is False, "INF scope matrix revalidation_execution_in_scope must be false")

    forbidden_actions = _load_json(INF_REVALIDATION_FORBIDDEN_ACTIONS_PATH)
    _require(forbidden_actions.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF forbidden actions phase_id mismatch")
    for key in (
        "project_aris_mutation_forbidden",
        "project_aris_tests_forbidden",
        "proof_loop_execution_forbidden",
        "revalidation_execution_forbidden",
        "runtime_forbidden",
        "real_apply_forbidden",
        "finding_close_forbidden",
        "remediation_proven_override_forbidden",
        "product_forbidden",
        "bedrock_forbidden",
        "secrets_forbidden",
        "dependency_or_package_manager_forbidden",
    ):
        _require(forbidden_actions.get(key) is True, f"INF forbidden actions {key} must be true")

    next_candidate = _load_json(INF_REVALIDATION_NEXT_ROUTE_CANDIDATE_PATH)
    _require(next_candidate.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF next route candidate phase_id mismatch")
    _require(next_candidate.get("candidate_next_gate") == "INF_REVALIDATION_READINESS_PACKET", "INF next route candidate gate mismatch")
    _require(next_candidate.get("candidate_only") is True, "INF next route candidate candidate_only must be true")
    _require(next_candidate.get("state_advanced") is False, "INF next route candidate state_advanced must be false")
    _require(next_candidate.get("next_phase_preserved") is None, "INF next route candidate next_phase_preserved must be null")
    _require(next_candidate.get("active_next_phase_preserved") is None, "INF next route candidate active_next_phase_preserved must be null")

    activation_packet = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_PACKET_PATH)
    _require(activation_packet.get("artifact_id") == "inf_revalidation_route_activation_packet", "INF activation packet artifact_id mismatch")
    _require(activation_packet.get("phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_ACTIVATION_PACKET", "INF activation packet phase_id mismatch")
    _require(activation_packet.get("source_current_phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "INF activation packet source_current_phase_id mismatch")
    _require(activation_packet.get("selected_branch") == "TRACK_REVALIDATION_FIRST", "INF activation packet selected_branch mismatch")
    _require(activation_packet.get("source_activation_decision") == "artifacts/purgatorium/purg_remaining_roadmap_activation_decision_packet.json", "INF activation packet source activation decision mismatch")
    _require(activation_packet.get("target_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF activation packet target_phase_id mismatch")
    _require(activation_packet.get("target_phase_class") == "infernus_revalidation_route_admission", "INF activation packet target_phase_class mismatch")
    for key in (
        "operator_authorized",
        "route_activation_only",
        "state_advanced",
    ):
        _require(activation_packet.get(key) is True, f"INF activation packet {key} must be true")
    for key in (
        "revalidation_executed",
        "project_aris_changed",
        "project_aris_tests_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(activation_packet.get(key) is False, f"INF activation packet {key} must be false")
    _require(activation_packet.get("decision") == "pass", "INF activation packet decision mismatch")

    transition_row = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_TRANSITION_ROW_PATH)
    _require(transition_row.get("row_applied_to_live_transition_table") is True, "INF transition row must be applied to the live Transition Table")
    _require(transition_row.get("current_phase_id") == "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "INF transition row current_phase_id mismatch")
    _require(transition_row.get("next_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF transition row next_phase_id mismatch")
    _require(transition_row.get("next_phase_class") == "infernus_revalidation_route_admission", "INF transition row next_phase_class mismatch")

    state_manifest = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH)
    _require(state_manifest.get("new_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF state update manifest new_phase_id mismatch")
    _require(state_manifest.get("new_status") == "inf_revalidation_route_admission_opened", "INF state update manifest new_status mismatch")

    schema_validator_evidence = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH)
    _require(schema_validator_evidence.get("schema_updated") is True, "INF schema/validator evidence schema_updated must be true")
    _require(schema_validator_evidence.get("validator_updated") is True, "INF schema/validator evidence validator_updated must be true")

    no_real = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_NO_REAL_PATH)
    for key in (
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "revalidation_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
        "product_bedrock_real_apply_secrets_executed",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_real.get(key) is False, f"INF route activation no-real {key} must be false")

    activation_next_candidate = _load_json(INF_REVALIDATION_ROUTE_ACTIVATION_NEXT_ROUTE_CANDIDATE_PATH)
    _require(activation_next_candidate.get("candidate_next_gate") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF activation next route candidate gate mismatch")
    _require(activation_next_candidate.get("candidate_only") is False, "INF activation next route candidate candidate_only must be false")
    _require(activation_next_candidate.get("state_advanced") is True, "INF activation next route candidate state_advanced must be true")
    _require(activation_next_candidate.get("next_phase_preserved") is None, "INF activation next route candidate next_phase_preserved must be null")
    _require(activation_next_candidate.get("active_next_phase_preserved") is None, "INF activation next route candidate active_next_phase_preserved must be null")
    _require(activation_next_candidate.get("decision") == "pass", "INF activation next route candidate decision mismatch")


def _check_inf_revalidation_readiness_activation_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "INF_REVALIDATION_READINESS_PACKET":
        return

    for path in (
        INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH,
        INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_TRANSITION_ROW_PATH,
        INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH,
        INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH,
        INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_NO_REAL_PATH,
        INF_REVALIDATION_READINESS_PACKET_PATH,
        INF_REVALIDATION_SCENARIO_SCOPE_PATH,
        INF_REVALIDATION_ORACLE_CONTRACT_PATH,
        INF_REVALIDATION_ABORT_CRITERIA_PATH,
        INF_REVALIDATION_READINESS_NO_REAL_PATH,
        INF_REVALIDATION_READINESS_NEXT_ROUTE_CANDIDATE_PATH,
    ):
        _require(path.exists(), f"missing INF revalidation readiness artifact: {path}")

    activation_packet = _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET_PATH)
    _require(activation_packet.get("artifact_id") == "inf_revalidation_readiness_route_activation_packet", "INF readiness activation artifact_id mismatch")
    _require(activation_packet.get("phase_id") == "INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_PACKET", "INF readiness activation phase_id mismatch")
    _require(activation_packet.get("source_current_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF readiness activation source_current_phase_id mismatch")
    _require(activation_packet.get("source_candidate_next_gate") == "INF_REVALIDATION_READINESS_PACKET", "INF readiness activation source_candidate_next_gate mismatch")
    _require(activation_packet.get("target_phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF readiness activation target_phase_id mismatch")
    _require(activation_packet.get("target_phase_class") == "infernus_revalidation_readiness", "INF readiness activation target_phase_class mismatch")
    for key in ("operator_authorized", "route_activation_only", "state_advanced"):
        _require(activation_packet.get(key) is True, f"INF readiness activation {key} must be true")
    for key in (
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "revalidation_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(activation_packet.get(key) is False, f"INF readiness activation {key} must be false")
    _require(activation_packet.get("decision") == "pass", "INF readiness activation decision mismatch")

    transition_row = _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_TRANSITION_ROW_PATH)
    _require(transition_row.get("row_applied_to_live_transition_table") is True, "INF readiness transition row must be applied")
    _require(transition_row.get("current_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF readiness transition row current_phase_id mismatch")
    _require(transition_row.get("next_phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF readiness transition row next_phase_id mismatch")
    _require(transition_row.get("next_phase_class") == "infernus_revalidation_readiness", "INF readiness transition row next_phase_class mismatch")

    state_manifest = _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_STATE_UPDATE_MANIFEST_PATH)
    _require(state_manifest.get("new_phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF readiness state update manifest new_phase_id mismatch")
    _require(state_manifest.get("new_status") == "inf_revalidation_readiness_opened", "INF readiness state update manifest new_status mismatch")

    schema_validator_evidence = _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_SCHEMA_VALIDATOR_EVIDENCE_PATH)
    _require(schema_validator_evidence.get("schema_updated") is True, "INF readiness schema/validator evidence schema_updated must be true")
    _require(schema_validator_evidence.get("validator_updated") is True, "INF readiness schema/validator evidence validator_updated must be true")

    route_packet = _load_json(INF_REVALIDATION_READINESS_PACKET_PATH)
    _require(route_packet.get("artifact_id") == "inf_revalidation_readiness_packet", "INF readiness packet artifact_id mismatch")
    _require(route_packet.get("phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF readiness packet phase_id mismatch")
    _require(route_packet.get("phase_class") == "infernus_revalidation_readiness", "INF readiness packet phase_class mismatch")
    _require(route_packet.get("status") == "inf_revalidation_readiness_opened", "INF readiness packet status mismatch")
    _require(route_packet.get("previous_live_phase_id") == "INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "INF readiness packet previous_live_phase_id mismatch")
    _require(route_packet.get("source_activation_packet") == "artifacts/purgatorium/inf_revalidation_readiness_route_activation_packet.json", "INF readiness packet source_activation_packet mismatch")
    _require(route_packet.get("finding_id") == "IF09-FIND-001", "INF readiness packet finding_id mismatch")
    _require(route_packet.get("execution_authorized") is False, "INF readiness packet execution_authorized must be false")
    _require(route_packet.get("oracle_defined") is True, "INF readiness packet oracle_defined must be true")
    _require(route_packet.get("abort_criteria_defined") is True, "INF readiness packet abort_criteria_defined must be true")
    _require(route_packet.get("next_phase") is None, "INF readiness packet next_phase must be null")
    _require(route_packet.get("active_next_phase") is None, "INF readiness packet active_next_phase must be null")
    for key in (
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "revalidation_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(route_packet.get(key) is False, f"INF readiness packet {key} must be false")
    _require(route_packet.get("decision") == "pass", "INF readiness packet decision mismatch")

    scenario_scope = _load_json(INF_REVALIDATION_SCENARIO_SCOPE_PATH)
    _require(scenario_scope.get("phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF scenario scope phase_id mismatch")
    _require(scenario_scope.get("finding_id") == "IF09-FIND-001", "INF scenario scope finding_id mismatch")
    _require(scenario_scope.get("execution_authorized") is False, "INF scenario scope execution_authorized must be false")

    oracle_contract = _load_json(INF_REVALIDATION_ORACLE_CONTRACT_PATH)
    _require(oracle_contract.get("phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF oracle contract phase_id mismatch")
    _require(oracle_contract.get("deterministic_oracle_defined") is True, "INF oracle contract deterministic_oracle_defined must be true")
    _require(oracle_contract.get("execution_authorized") is False, "INF oracle contract execution_authorized must be false")

    abort_criteria = _load_json(INF_REVALIDATION_ABORT_CRITERIA_PATH)
    _require(abort_criteria.get("phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF abort criteria phase_id mismatch")
    _require(abort_criteria.get("execution_authorized") is False, "INF abort criteria execution_authorized must be false")

    no_real_activation = _load_json(INF_REVALIDATION_READINESS_ROUTE_ACTIVATION_NO_REAL_PATH)
    no_real_readiness = _load_json(INF_REVALIDATION_READINESS_NO_REAL_PATH)
    for payload, label in (
        (no_real_activation, "INF readiness activation no-real"),
        (no_real_readiness, "INF readiness packet no-real"),
    ):
        for key in (
            "project_aris_changed",
            "project_aris_tests_executed",
            "proof_loop_executed",
            "revalidation_executed",
            "runtime_executed",
            "real_apply_executed",
            "finding_closed",
            "remediation_proven",
            "product_bedrock_real_apply_secrets_executed",
            "dependency_or_package_manager_used",
            "mcp_activated",
            "rag_ingestion_executed",
            "memory_write_executed",
        ):
            _require(payload.get(key) is False, f"{label} {key} must be false")

    next_candidate = _load_json(INF_REVALIDATION_READINESS_NEXT_ROUTE_CANDIDATE_PATH)
    _require(next_candidate.get("candidate_next_gate") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF readiness next route candidate gate mismatch")
    _require(next_candidate.get("candidate_only") is True, "INF readiness next route candidate candidate_only must be true")
    _require(next_candidate.get("state_advanced") is False, "INF readiness next route candidate state_advanced must be false")
    _require(next_candidate.get("next_phase_preserved") is None, "INF readiness next route candidate next_phase_preserved must be null")
    _require(next_candidate.get("active_next_phase_preserved") is None, "INF readiness next route candidate active_next_phase_preserved must be null")
    _require(next_candidate.get("decision") == "pass", "INF readiness next route candidate decision mismatch")


def _check_inf_revalidation_operator_authorization_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET":
        return

    for path in (
        INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH,
        INF_REVALIDATION_EXECUTION_CONTRACT_PATH,
        INF_REVALIDATION_SAFETY_LOCK_MATRIX_PATH,
        INF_REVALIDATION_OPERATOR_AUTH_NO_REAL_PATH,
        INF_REVALIDATION_OPERATOR_AUTH_NEXT_ROUTE_CANDIDATE_PATH,
        INF_REVALIDATION_READINESS_PACKET_PATH,
        INF_REVALIDATION_SCENARIO_SCOPE_PATH,
        INF_REVALIDATION_ORACLE_CONTRACT_PATH,
        INF_REVALIDATION_ABORT_CRITERIA_PATH,
    ):
        _require(path.exists(), f"missing INF revalidation operator authorization artifact: {path}")

    auth_packet = _load_json(INF_REVALIDATION_OPERATOR_AUTH_PACKET_PATH)
    _require(auth_packet.get("artifact_id") == "inf_revalidation_operator_authorization_packet", "INF operator auth artifact_id mismatch")
    _require(auth_packet.get("phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF operator auth phase_id mismatch")
    _require(auth_packet.get("phase_class") == "infernus_revalidation_operator_authorization", "INF operator auth phase_class mismatch")
    _require(auth_packet.get("status") == "inf_revalidation_operator_authorization_pass", "INF operator auth status mismatch")
    _require(auth_packet.get("previous_live_phase_id") == "INF_REVALIDATION_READINESS_PACKET", "INF operator auth previous_live_phase_id mismatch")
    _require(auth_packet.get("source_readiness_packet") == "artifacts/purgatorium/inf_revalidation_readiness_packet.json", "INF operator auth source_readiness_packet mismatch")
    _require(auth_packet.get("target_finding_id") == "IF09-FIND-001", "INF operator auth target_finding_id mismatch")
    _require(auth_packet.get("operator_authorized") is True, "INF operator auth operator_authorized must be true")
    _require(auth_packet.get("authorization_scope") == "future_controlled_infernus_revalidation_execution_only", "INF operator auth authorization_scope mismatch")
    _require(auth_packet.get("authorized_future_gate") == "INF_REVALIDATION_EXECUTION_PACKET", "INF operator auth authorized_future_gate mismatch")
    for key in (
        "execution_contract_created",
        "safety_lock_matrix_created",
    ):
        _require(auth_packet.get(key) is True, f"INF operator auth {key} must be true")
    for key in (
        "revalidation_executed_now",
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(auth_packet.get(key) is False, f"INF operator auth {key} must be false")
    _require(auth_packet.get("decision") == "pass", "INF operator auth decision mismatch")

    execution_contract = _load_json(INF_REVALIDATION_EXECUTION_CONTRACT_PATH)
    _require(execution_contract.get("phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF execution contract phase_id mismatch")
    _require(execution_contract.get("target_finding_id") == "IF09-FIND-001", "INF execution contract target_finding_id mismatch")
    _require(execution_contract.get("source_readiness_packet") == "artifacts/purgatorium/inf_revalidation_readiness_packet.json", "INF execution contract readiness source mismatch")
    _require(execution_contract.get("scenario_scope_source") == "artifacts/purgatorium/inf_revalidation_scenario_scope.json", "INF execution contract scenario scope source mismatch")
    _require(execution_contract.get("oracle_source") == "artifacts/purgatorium/inf_revalidation_oracle_contract.json", "INF execution contract oracle source mismatch")
    _require(execution_contract.get("abort_criteria_source") == "artifacts/purgatorium/inf_revalidation_abort_criteria.json", "INF execution contract abort criteria source mismatch")
    _require(execution_contract.get("execution_requires_next_gate") is True, "INF execution contract execution_requires_next_gate must be true")
    _require(execution_contract.get("next_required_gate") == "INF_REVALIDATION_EXECUTION_PACKET", "INF execution contract next_required_gate mismatch")
    _require(execution_contract.get("no_secrets_no_product_no_bedrock") is True, "INF execution contract no_secrets_no_product_no_bedrock must be true")

    safety_lock_matrix = _load_json(INF_REVALIDATION_SAFETY_LOCK_MATRIX_PATH)
    _require(safety_lock_matrix.get("phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF safety lock matrix phase_id mismatch")
    _require(safety_lock_matrix.get("target_finding_id") == "IF09-FIND-001", "INF safety lock matrix target_finding_id mismatch")
    _require(safety_lock_matrix.get("execution_authorized_now") is False, "INF safety lock matrix execution_authorized_now must be false")
    _require(safety_lock_matrix.get("authorized_future_gate") == "INF_REVALIDATION_EXECUTION_PACKET", "INF safety lock matrix authorized_future_gate mismatch")
    _require(safety_lock_matrix.get("future_execution_authorized_for_next_gate_only") is True, "INF safety lock matrix future_execution_authorized_for_next_gate_only must be true")
    for key in (
        "project_aris_mutation_allowed_now",
        "project_aris_tests_allowed_now",
        "proof_loop_execution_allowed_now",
        "runtime_allowed_now",
        "real_apply_allowed_now",
        "product_ready",
        "bedrock_ready",
        "secrets_allowed_now",
        "dependency_package_manager_allowed_now",
        "finding_closed",
        "remediation_proven",
    ):
        _require(safety_lock_matrix.get(key) is False, f"INF safety lock matrix {key} must be false")
    _require(safety_lock_matrix.get("IF09-FIND-001") == "open", "INF safety lock matrix finding status mismatch")

    no_real = _load_json(INF_REVALIDATION_OPERATOR_AUTH_NO_REAL_PATH)
    for key in (
        "revalidation_executed",
        "project_aris_changed",
        "project_aris_tests_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
        "product_bedrock_real_apply_secrets_executed",
        "dependency_or_package_manager_used",
    ):
        _require(no_real.get(key) is False, f"INF operator auth no-real {key} must be false")

    next_candidate = _load_json(INF_REVALIDATION_OPERATOR_AUTH_NEXT_ROUTE_CANDIDATE_PATH)
    _require(next_candidate.get("phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF operator auth next route candidate phase_id mismatch")
    _require(next_candidate.get("candidate_next_gate") == "INF_REVALIDATION_EXECUTION_PACKET", "INF operator auth next route candidate gate mismatch")
    _require(next_candidate.get("candidate_only") is True, "INF operator auth next route candidate candidate_only must be true")
    _require(next_candidate.get("state_advanced") is False, "INF operator auth next route candidate state_advanced must be false")
    _require(next_candidate.get("next_phase_preserved") is None, "INF operator auth next route candidate next_phase_preserved must be null")
    _require(next_candidate.get("active_next_phase_preserved") is None, "INF operator auth next route candidate active_next_phase_preserved must be null")
    _require(next_candidate.get("decision") == "pass", "INF operator auth next route candidate decision mismatch")


def _check_inf_revalidation_execution_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "INF_REVALIDATION_EXECUTION_PACKET":
        return

    for path in (
        INF_REVALIDATION_EXECUTION_OPERATOR_COMMAND_PATH,
        INF_REVALIDATION_EXECUTION_TRANSITION_ROW_PATH,
        INF_REVALIDATION_EXECUTION_PACKET_PATH,
        INF_REVALIDATION_EXECUTION_PREFLIGHT_PATH,
        INF_REVALIDATION_EXECUTION_COMMAND_LOG_PATH,
        INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH,
        INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH,
        INF_REVALIDATION_EXECUTION_EVIDENCE_INVENTORY_PATH,
        INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH,
        INF_REVALIDATION_EXECUTION_SUMMARY_PATH,
        INF_REVALIDATION_EXECUTION_REPORT_PATH,
        INF_REVALIDATION_EXECUTION_VALIDATION_EVIDENCE_PATH,
        INF_REVALIDATION_EXECUTION_NEXT_ROUTE_CANDIDATE_PATH,
        INF_REVALIDATION_EXECUTION_CONTRACT_PATH,
        INF_REVALIDATION_SAFETY_LOCK_MATRIX_PATH,
        INF_REVALIDATION_SCENARIO_SCOPE_PATH,
        INF_REVALIDATION_ORACLE_CONTRACT_PATH,
        INF_REVALIDATION_ABORT_CRITERIA_PATH,
    ):
        _require(path.exists(), f"missing INF revalidation execution artifact: {path}")

    operator_command = _load_json(INF_REVALIDATION_EXECUTION_OPERATOR_COMMAND_PATH)
    _require(operator_command.get("phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF execution operator command phase_id mismatch")
    _require(operator_command.get("operator_command_text") == "execucao logo", "INF execution operator command text mismatch")
    _require(operator_command.get("interpreted_as") == "explicit_operator_execution_command_for_INF_REVALIDATION_EXECUTION_PACKET", "INF execution operator command interpretation mismatch")
    for key in (
        "project_mutation_authorized",
        "global_test_suite_authorized",
        "runtime_authorized",
        "real_apply_authorized",
        "product_authorized",
        "bedrock_authorized",
        "secrets_authorized",
    ):
        _require(operator_command.get(key) is False, f"INF execution operator command {key} must be false")

    transition_row = _load_json(INF_REVALIDATION_EXECUTION_TRANSITION_ROW_PATH)
    _require(transition_row.get("current_phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF execution transition row current_phase_id mismatch")
    _require(transition_row.get("next_phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF execution transition row next_phase_id mismatch")
    _require(transition_row.get("next_phase_class") == "infernus_revalidation_execution", "INF execution transition row next_phase_class mismatch")
    _require(transition_row.get("advance_mode") == "operator", "INF execution transition row advance_mode mismatch")
    _require(transition_row.get("unlocked_by_operator_command") is True, "INF execution transition row unlock mismatch")

    preflight = _load_json(INF_REVALIDATION_EXECUTION_PREFLIGHT_PATH)
    _require(preflight.get("current_phase_id_before_execution") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF execution preflight current_phase_id mismatch")
    _require(preflight.get("current_status_before_execution") == "inf_revalidation_operator_authorization_pass", "INF execution preflight status mismatch")
    _require(preflight.get("target_commit_sha") == "7883af5a32c629026bfc6dc15ebee4ebbcadd295", "INF execution preflight target commit mismatch")
    _require(preflight.get("workspace_head_matches_target") is False, "INF execution preflight workspace_head_matches_target must be false")
    _require(preflight.get("authoritative_execution_surface") == "read_only_git_archive_snapshot", "INF execution preflight authoritative surface mismatch")
    _require(preflight.get("focused_runner_available") is True, "INF execution preflight focused_runner_available mismatch")
    _require(preflight.get("forbidden_commands_required") is False, "INF execution preflight forbidden_commands_required mismatch")
    _require(preflight.get("decision") == "pass", "INF execution preflight decision mismatch")

    packet = _load_json(INF_REVALIDATION_EXECUTION_PACKET_PATH)
    _require(packet.get("artifact_id") == "inf_revalidation_execution_packet", "INF execution packet artifact_id mismatch")
    _require(packet.get("phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF execution packet phase_id mismatch")
    _require(packet.get("phase_class") == "infernus_revalidation_execution", "INF execution packet phase_class mismatch")
    _require(packet.get("status") == "inf_revalidation_execution_pass", "INF execution packet status mismatch")
    _require(packet.get("decision") == "pass", "INF execution packet decision mismatch")
    _require(packet.get("previous_live_phase_id") == "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "INF execution packet previous_live_phase_id mismatch")
    _require(packet.get("target_finding_id") == "IF09-FIND-001", "INF execution packet target_finding_id mismatch")
    _require(packet.get("target_commit_sha") == "7883af5a32c629026bfc6dc15ebee4ebbcadd295", "INF execution packet target_commit_sha mismatch")
    _require(packet.get("oracle_result") == "pass", "INF execution packet oracle_result mismatch")
    _require(packet.get("finding_closure_candidate") is True, "INF execution packet finding_closure_candidate mismatch")
    _require(packet.get("project_aris_changed") is False, "INF execution packet project_aris_changed must be false")
    _require(packet.get("project_aris_tests_executed") is True, "INF execution packet project_aris_tests_executed must be true")
    for key in (
        "global_test_suite_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "finding_closed",
        "remediation_proven",
    ):
        _require(packet.get(key) is False, f"INF execution packet {key} must be false")
    _require(packet.get("candidate_next_gate") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF execution packet candidate_next_gate mismatch")
    _require(packet.get("next_phase_preserved") is None, "INF execution packet next_phase_preserved must be null")
    _require(packet.get("active_next_phase_preserved") is None, "INF execution packet active_next_phase_preserved must be null")

    oracle = _load_json(INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH)
    _require(oracle.get("oracle_id") == "INF_REVALIDATION_IF09_TRACK_A_ACCEPTED_LINEAGE_ORACLE_001", "INF execution oracle_id mismatch")
    _require(oracle.get("oracle_result") == "pass", "INF execution oracle_result mismatch")
    _require(oracle.get("if09_failure_reproduced") is False, "INF execution oracle IF09 reproduction mismatch")
    _require(oracle.get("tracked_lineage_regression_detected") is False, "INF execution oracle regression mismatch")
    _require(oracle.get("workspace_head_commit_mismatch_detected") is True, "INF execution oracle workspace_head_commit_mismatch_detected mismatch")

    regression = _load_json(INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH)
    _require(regression.get("total_modules") == 5, "INF execution regression total_modules mismatch")
    _require(regression.get("total_tests") == 19, "INF execution regression total_tests mismatch")
    _require(regression.get("failures") == 0, "INF execution regression failures mismatch")
    _require(regression.get("errors") == 0, "INF execution regression errors mismatch")

    no_forbidden = _load_json(INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH)
    for key in (
        "project_aris_mutated",
        "global_test_suite_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "product_executed",
        "bedrock_executed",
        "secrets_accessed",
        "package_manager_executed",
        "dependency_changed",
        "production_authorized",
        "product_ready",
        "runtime_integration_allowed",
        "secrets_access_authorized",
        "finding_closed",
        "remediation_proven",
    ):
        _require(no_forbidden.get(key) is False, f"INF execution no-forbidden {key} must be false")

    next_candidate = _load_json(INF_REVALIDATION_EXECUTION_NEXT_ROUTE_CANDIDATE_PATH)
    _require(next_candidate.get("phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF execution next route candidate phase_id mismatch")
    _require(next_candidate.get("candidate_next_gate") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF execution next route candidate gate mismatch")
    _require(next_candidate.get("candidate_only") is True, "INF execution next route candidate candidate_only mismatch")
    _require(next_candidate.get("state_advanced") is False, "INF execution next route candidate state_advanced mismatch")

    command_log_lines = [line for line in INF_REVALIDATION_EXECUTION_COMMAND_LOG_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    _require(len(command_log_lines) >= 3, "INF execution command log must contain at least three events")


def _check_inf_revalidation_adjudication_or_closure_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET":
        return

    for path in (
        INF_REVALIDATION_ADJUDICATION_OPERATOR_COMMAND_PATH,
        INF_REVALIDATION_ADJUDICATION_TRANSITION_ROW_PATH,
        INF_REVALIDATION_ADJUDICATION_EVIDENCE_MATRIX_PATH,
        INF_REVALIDATION_ADJUDICATION_ORACLE_REVIEW_PATH,
        INF_REVALIDATION_ADJUDICATION_REGRESSION_REVIEW_PATH,
        INF_REVALIDATION_ADJUDICATION_NO_FORBIDDEN_PATH,
        INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH,
        INF_REVALIDATION_ADJUDICATION_CLOSURE_DECISION_PATH,
        INF_REVALIDATION_ADJUDICATION_SUMMARY_PATH,
        INF_REVALIDATION_ADJUDICATION_REPORT_PATH,
        INF_REVALIDATION_ADJUDICATION_VALIDATION_EVIDENCE_PATH,
        INF_REVALIDATION_ADJUDICATION_NEXT_ROUTE_CANDIDATE_PATH,
        INF_REVALIDATION_EXECUTION_PACKET_PATH,
        INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH,
        INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH,
        INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH,
    ):
        _require(path.exists(), f"missing INF revalidation adjudication artifact: {path}")

    operator_command = _load_json(INF_REVALIDATION_ADJUDICATION_OPERATOR_COMMAND_PATH)
    _require(operator_command.get("phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication operator command phase_id mismatch")
    _require(operator_command.get("operator_command_text") == "abrir adjudicação/closure do INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication operator command text mismatch")
    _require(operator_command.get("interpreted_as") == "explicit_operator_route_opening_for_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication operator command interpretation mismatch")
    for key in (
        "project_mutation_authorized",
        "project_aris_tests_authorized",
        "runtime_authorized",
        "real_apply_authorized",
        "product_authorized",
        "bedrock_authorized",
        "secrets_authorized",
        "package_manager_authorized",
    ):
        _require(operator_command.get(key) is False, f"INF adjudication operator command {key} must be false")

    transition_row = _load_json(INF_REVALIDATION_ADJUDICATION_TRANSITION_ROW_PATH)
    _require(transition_row.get("current_phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF adjudication transition row current_phase_id mismatch")
    _require(transition_row.get("next_phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication transition row next_phase_id mismatch")
    _require(transition_row.get("next_phase_class") == "infernus_revalidation_adjudication_or_closure", "INF adjudication transition row next_phase_class mismatch")
    _require(transition_row.get("advance_mode") == "operator", "INF adjudication transition row advance_mode mismatch")
    _require(transition_row.get("unlocked_by_operator_command") is True, "INF adjudication transition row unlock mismatch")

    evidence_matrix = _load_json(INF_REVALIDATION_ADJUDICATION_EVIDENCE_MATRIX_PATH)
    _require(evidence_matrix.get("target_finding_id") == "IF09-FIND-001", "INF adjudication evidence matrix target_finding_id mismatch")
    _require(evidence_matrix.get("all_closure_criteria_satisfied") is True, "INF adjudication evidence matrix all_closure_criteria_satisfied mismatch")
    _require(evidence_matrix.get("finding_status_after_adjudication") == "closed", "INF adjudication evidence matrix finding_status_after_adjudication mismatch")

    oracle_review = _load_json(INF_REVALIDATION_ADJUDICATION_ORACLE_REVIEW_PATH)
    _require(oracle_review.get("oracle_result") == "pass", "INF adjudication oracle review oracle_result mismatch")
    _require(oracle_review.get("runner_result") == "pass", "INF adjudication oracle review runner_result mismatch")
    _require(oracle_review.get("runner_exit_code") == 0, "INF adjudication oracle review runner_exit_code mismatch")
    _require(oracle_review.get("tests_run_count") == 19, "INF adjudication oracle review tests_run_count mismatch")
    _require(oracle_review.get("if09_failure_reproduced") is False, "INF adjudication oracle review IF09 reproduction mismatch")
    _require(oracle_review.get("tracked_lineage_regression_detected") is False, "INF adjudication oracle review regression mismatch")
    _require(oracle_review.get("finding_closure_candidate") is True, "INF adjudication oracle review closure candidate mismatch")

    regression_review = _load_json(INF_REVALIDATION_ADJUDICATION_REGRESSION_REVIEW_PATH)
    _require(regression_review.get("total_tests") == 19, "INF adjudication regression review total_tests mismatch")
    _require(regression_review.get("failures") == 0, "INF adjudication regression review failures mismatch")
    _require(regression_review.get("errors") == 0, "INF adjudication regression review errors mismatch")
    _require(regression_review.get("if09_regression_detected") is False, "INF adjudication regression review IF09 regression mismatch")
    _require(regression_review.get("tracked_lineage_regression_detected") is False, "INF adjudication regression review tracked_lineage_regression_detected mismatch")

    no_forbidden = _load_json(INF_REVALIDATION_ADJUDICATION_NO_FORBIDDEN_PATH)
    for key in (
        "project_aris_mutated",
        "project_aris_main_workspace_touched",
        "global_test_suite_executed",
        "proof_loop_executed",
        "runtime_executed",
        "real_apply_executed",
        "product_executed",
        "bedrock_executed",
        "secrets_accessed",
        "package_manager_executed",
        "dependency_changed",
        "production_authorized",
        "product_ready",
        "runtime_integration_allowed",
        "secrets_access_authorized",
    ):
        _require(no_forbidden.get(key) is False, f"INF adjudication no-forbidden {key} must be false")
    _require(no_forbidden.get("finding_closed") is True, "INF adjudication no-forbidden finding_closed mismatch")
    _require(no_forbidden.get("remediation_proven") is True, "INF adjudication no-forbidden remediation_proven mismatch")

    closure_packet = _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH)
    _require(closure_packet.get("phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication closure packet phase_id mismatch")
    _require(closure_packet.get("phase_class") == "infernus_revalidation_adjudication_or_closure", "INF adjudication closure packet phase_class mismatch")
    _require(closure_packet.get("status") == "inf_revalidation_adjudication_closure_pass", "INF adjudication closure packet status mismatch")
    _require(closure_packet.get("decision") == "pass", "INF adjudication closure packet decision mismatch")
    _require(closure_packet.get("previous_live_phase_id") == "INF_REVALIDATION_EXECUTION_PACKET", "INF adjudication closure packet previous_live_phase_id mismatch")
    _require(closure_packet.get("target_finding_id") == "IF09-FIND-001", "INF adjudication closure packet target_finding_id mismatch")
    _require(closure_packet.get("finding_status") == "closed", "INF adjudication closure packet finding_status mismatch")
    _require(closure_packet.get("finding_closed") is True, "INF adjudication closure packet finding_closed mismatch")
    _require(closure_packet.get("remediation_proven") is True, "INF adjudication closure packet remediation_proven mismatch")
    _require(closure_packet.get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface", "INF adjudication closure packet closure_basis mismatch")
    _require(closure_packet.get("candidate_next_gate") is None, "INF adjudication closure packet candidate_next_gate must be null")
    _require(closure_packet.get("next_phase_preserved") is None, "INF adjudication closure packet next_phase_preserved must be null")
    _require(closure_packet.get("active_next_phase_preserved") is None, "INF adjudication closure packet active_next_phase_preserved must be null")

    closure_decision = _load_json(INF_REVALIDATION_ADJUDICATION_CLOSURE_DECISION_PATH)
    _require(closure_decision.get("decision") == "pass", "INF adjudication closure decision mismatch")
    _require(closure_decision.get("status") == "inf_revalidation_adjudication_closure_pass", "INF adjudication closure decision status mismatch")
    _require(closure_decision.get("finding_status") == "closed", "INF adjudication closure decision finding_status mismatch")
    _require(closure_decision.get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface", "INF adjudication closure decision closure_basis mismatch")

    summary = _load_json(INF_REVALIDATION_ADJUDICATION_SUMMARY_PATH)
    _require(summary.get("decision") == "pass", "INF adjudication summary decision mismatch")
    _require(summary.get("finding_closed") is True, "INF adjudication summary finding_closed mismatch")
    _require(summary.get("remediation_proven") is True, "INF adjudication summary remediation_proven mismatch")

    next_candidate = _load_json(INF_REVALIDATION_ADJUDICATION_NEXT_ROUTE_CANDIDATE_PATH)
    _require(next_candidate.get("phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "INF adjudication next route candidate phase_id mismatch")
    _require(next_candidate.get("candidate_next_gate") is None, "INF adjudication next route candidate candidate_next_gate must be null")
    _require(next_candidate.get("candidate_only") is True, "INF adjudication next route candidate candidate_only mismatch")
    _require(next_candidate.get("state_advanced") is False, "INF adjudication next route candidate state_advanced mismatch")
    _require(next_candidate.get("finding_closed") is True, "INF adjudication next route candidate finding_closed mismatch")
    _require(next_candidate.get("remediation_proven") is True, "INF adjudication next route candidate remediation_proven mismatch")

    _require(state.get("phase_class") == "infernus_revalidation_adjudication_or_closure", "live state phase_class mismatch for INF adjudication")
    _require(state.get("status") == "inf_revalidation_adjudication_closure_pass", "live state status mismatch for INF adjudication")
    _require(state.get("decision") == "pass", "live state decision mismatch for INF adjudication")
    _require(state.get("target_finding_id") == "IF09-FIND-001", "live state target_finding_id mismatch for INF adjudication")
    _require(state.get("target_finding_status") == "closed", "live state target_finding_status mismatch for INF adjudication")
    _require(state.get("finding_closed") is True, "live state finding_closed mismatch for INF adjudication")
    _require(state.get("remediation_proven") is True, "live state remediation_proven mismatch for INF adjudication")
    _require(state.get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface", "live state closure_basis mismatch for INF adjudication")


def _check_if09_closure_milestone_mirror_sanity_artifacts(state: dict[str, Any]) -> None:
    if state.get("current_phase_id") != "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET":
        return

    for path in (
        IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH,
        IF09_CLOSURE_MILESTONE_MIRROR_DRIFT_MATRIX_PATH,
        IF09_CLOSURE_MILESTONE_SUPERSEDED_NOTES_MANIFEST_PATH,
        IF09_CLOSURE_MILESTONE_NO_REAL_EXECUTION_ATTESTATION_PATH,
        IF09_CLOSURE_MILESTONE_VALIDATION_EVIDENCE_PATH,
        BENCHUX_ROUTE_OPENING_CANDIDATE_PATH,
        BENCHUX_PRE_ROUTE_SCOPE_NOTE_PATH,
        INF_REVALIDATION_ADJUDICATION_CLOSURE_PACKET_PATH,
        INF_REVALIDATION_EXECUTION_ORACLE_RESULT_PATH,
        INF_REVALIDATION_EXECUTION_REGRESSION_MATRIX_PATH,
        INF_REVALIDATION_EXECUTION_NO_FORBIDDEN_PATH,
    ):
        _require(path.exists(), f"missing IF09 closure milestone artifact: {path}")

    sanity_packet = _load_json(IF09_CLOSURE_MILESTONE_SANITY_PACKET_PATH)
    _require(sanity_packet.get("phase_id") == "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET", "IF09 closure sanity packet phase_id mismatch")
    _require(sanity_packet.get("phase_class") == "governance_repair", "IF09 closure sanity packet phase_class mismatch")
    _require(sanity_packet.get("status") == "if09_closure_milestone_mirror_sanity_pass", "IF09 closure sanity packet status mismatch")
    _require(sanity_packet.get("decision") == "pass", "IF09 closure sanity packet decision mismatch")
    _require(sanity_packet.get("previous_live_phase_id") == "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "IF09 closure sanity packet previous_live_phase_id mismatch")
    _require(sanity_packet.get("target_finding_id") == "IF09-FIND-001", "IF09 closure sanity packet target_finding_id mismatch")
    _require(sanity_packet.get("target_finding_status") == "closed", "IF09 closure sanity packet target_finding_status mismatch")
    _require(sanity_packet.get("finding_closed") is True, "IF09 closure sanity packet finding_closed mismatch")
    _require(sanity_packet.get("remediation_proven") is True, "IF09 closure sanity packet remediation_proven mismatch")
    _require(sanity_packet.get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface", "IF09 closure sanity packet closure_basis mismatch")
    _require(sanity_packet.get("benchux_candidate_next_gate") == "BENCHUX_ROUTE_OPENING_PACKET", "IF09 closure sanity packet benchux_candidate_next_gate mismatch")
    _require(sanity_packet.get("next_phase_preserved") is None, "IF09 closure sanity packet next_phase_preserved must be null")
    _require(sanity_packet.get("active_next_phase_preserved") is None, "IF09 closure sanity packet active_next_phase_preserved must be null")

    drift_matrix = _load_json(IF09_CLOSURE_MILESTONE_MIRROR_DRIFT_MATRIX_PATH)
    _require(drift_matrix.get("finding_status_preserved") == "closed", "IF09 closure drift matrix finding_status_preserved mismatch")
    _require(drift_matrix.get("finding_closed_preserved") is True, "IF09 closure drift matrix finding_closed_preserved mismatch")
    _require(drift_matrix.get("remediation_proven_preserved") is True, "IF09 closure drift matrix remediation_proven_preserved mismatch")
    _require(drift_matrix.get("historical_labels_applied") is True, "IF09 closure drift matrix historical_labels_applied mismatch")
    _require(drift_matrix.get("benchux_live_route_activated") is False, "IF09 closure drift matrix benchux_live_route_activated mismatch")

    superseded_manifest = _load_json(IF09_CLOSURE_MILESTONE_SUPERSEDED_NOTES_MANIFEST_PATH)
    _require(superseded_manifest.get("historical_label") == "HISTORICAL_ONLY", "IF09 closure superseded manifest historical_label mismatch")
    _require(superseded_manifest.get("superseded_label") == "SUPERSEDED_BY_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "IF09 closure superseded manifest superseded_label mismatch")
    _require(superseded_manifest.get("not_current_state_label") == "NOT_CURRENT_STATE", "IF09 closure superseded manifest not_current_state_label mismatch")

    no_real = _load_json(IF09_CLOSURE_MILESTONE_NO_REAL_EXECUTION_ATTESTATION_PATH)
    for key in (
        "project_aris_mutated",
        "project_aris_tests_executed",
        "revalidation_runner_executed",
        "bot_execution_triggered",
        "runtime_executed",
        "real_apply_executed",
        "product_executed",
        "bedrock_executed",
        "secrets_accessed",
        "package_manager_executed",
        "dependency_changed",
        "benchux_live_route_activated",
        "production_authorized",
        "product_ready",
        "runtime_integration_allowed",
        "secrets_access_authorized",
    ):
        _require(no_real.get(key) is False, f"IF09 closure no-real {key} must be false")
    _require(no_real.get("finding_closed") is True, "IF09 closure no-real finding_closed mismatch")
    _require(no_real.get("remediation_proven") is True, "IF09 closure no-real remediation_proven mismatch")

    benchux_candidate = _load_json(BENCHUX_ROUTE_OPENING_CANDIDATE_PATH)
    _require(benchux_candidate.get("candidate_next_gate") == "BENCHUX_ROUTE_OPENING_PACKET", "BenchUX candidate gate mismatch")
    _require(benchux_candidate.get("candidate_only") is True, "BenchUX candidate candidate_only mismatch")
    _require(benchux_candidate.get("state_advanced") is False, "BenchUX candidate state_advanced mismatch")
    _require(benchux_candidate.get("next_phase_preserved") is None, "BenchUX candidate next_phase_preserved must be null")
    _require(benchux_candidate.get("active_next_phase_preserved") is None, "BenchUX candidate active_next_phase_preserved must be null")
    for key in (
        "benchux_execution_authorized",
        "product_authorized",
        "bedrock_authorized",
        "real_apply_authorized",
        "runtime_authorized",
        "secrets_authorized",
    ):
        _require(benchux_candidate.get(key) is False, f"BenchUX candidate {key} must be false")
    _require(benchux_candidate.get("purpose") == "prepare_operator_decision_to_open_BenchUX_after_IF09_closure", "BenchUX candidate purpose mismatch")

    benchux_scope = _load_json(BENCHUX_PRE_ROUTE_SCOPE_NOTE_PATH)
    _require(benchux_scope.get("phase_id") == "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET", "BenchUX scope note phase_id mismatch")
    _require(benchux_scope.get("candidate_next_gate") == "BENCHUX_ROUTE_OPENING_PACKET", "BenchUX scope note candidate_next_gate mismatch")
    _require(benchux_scope.get("benchux_live_route_activated") is False, "BenchUX scope note benchux_live_route_activated mismatch")

    _require(state.get("phase_class") == "governance_repair", "live state phase_class mismatch for IF09 closure sanity")
    _require(state.get("status") == "if09_closure_milestone_mirror_sanity_pass", "live state status mismatch for IF09 closure sanity")
    _require(state.get("decision") == "pass", "live state decision mismatch for IF09 closure sanity")
    _require(state.get("target_finding_id") == "IF09-FIND-001", "live state target_finding_id mismatch for IF09 closure sanity")
    _require(state.get("target_finding_status") == "closed", "live state target_finding_status mismatch for IF09 closure sanity")
    _require(state.get("finding_closed") is True, "live state finding_closed mismatch for IF09 closure sanity")
    _require(state.get("remediation_proven") is True, "live state remediation_proven mismatch for IF09 closure sanity")
    _require(state.get("closure_basis") == "deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface", "live state closure_basis mismatch for IF09 closure sanity")


def _check_gate_signature(state: dict[str, Any]) -> str:
    phase_class = state.get("phase_class", "")
    locks = state.get("authorization", {})
    sig = hashlib.sha256(
        json.dumps(
            {"phase_class": phase_class, "locks": locks},
            sort_keys=True
        ).encode()
    ).hexdigest()[:16]
    seen = state.get("seen_gate_signatures", [])
    if sig in seen:
        print(f"BLOCK: gate signature {sig} ja executado anteriormente.")
        print("Este gate nao produz estado novo. Proibido repetir.")
        sys.exit(1)
    return sig


def _check_cycle_nudge(state: dict[str, Any]) -> None:
    cycles = state.get("gate_cycles_used", 0)
    max_c = state.get("gate_max_cycles", 3)
    if cycles >= max_c - 1:
        print(f"WARN: gate_cycles_used={cycles}/{max_c}.")
        print("Proximo ciclo bloqueia. Emita veredicto terminal agora.")


def _apply_streak_management(state: dict[str, Any], sig: str, decision: str) -> None:
    """Update streak and signature tracking based on phase_class and decision."""
    phase_class = state.get("phase_class", "")
    if decision != "pass":
        return
    if phase_class in CAPACITY_CLASSES:
        state["governance_gate_streak"] = 0
    elif phase_class in GOVERNANCE_CLASSES:
        state["governance_gate_streak"] = state.get("governance_gate_streak", 0) + 1
    if "seen_gate_signatures" not in state:
        state["seen_gate_signatures"] = []
    state["seen_gate_signatures"].append(sig)


def _warn_boot_receipt(state: dict[str, Any]) -> None:
    # Check ARIS_BOOT.md exists in root — blocking
    _require(ARIS_BOOT_PATH.exists(), "ARIS_BOOT.md ausente da raiz")

    boot_files = state.get("last_boot_files_read", [])
    # Verify boot order: [0] must be ACTIVE_CONTEXT_STATE.json, [1] must be ARIS_BOOT.md
    if len(boot_files) < 2 or boot_files[0] != "ACTIVE_CONTEXT_STATE.json" or boot_files[1] != "ARIS_BOOT.md":
        print(f"BLOCK: boot order incorreto em last_boot_files_read: {boot_files[:2]}")
        print("Expected: ['ACTIVE_CONTEXT_STATE.json', 'ARIS_BOOT.md']")
        sys.exit(1)

    # WARN (non-blocking): check superseded files are not in root
    for fname in BOOT_FILE_SUPERSEDED:
        if (ROOT / fname).exists():
            print(f"WARN: Arquivo superseded ainda presente na raiz: {fname}. Mover para archive/superseded/")

    # WARN (non-blocking): check archive subdirs exist
    for subdir in ["superseded", "gate_history", "derived_mirrors"]:
        if not (ROOT / "archive" / subdir).is_dir():
            print(f"WARN: archive/{subdir}/ não existe como diretório")


def _check_operator_preferences_contract(state: dict[str, Any]) -> None:
    priority_read_order = state.get("anti_corruption_contract", {}).get("canonical_read_order", [])
    _require(
        priority_read_order[: len(EXPECTED_PRIORITY_READ_ORDER)] == EXPECTED_PRIORITY_READ_ORDER,
        "canonical_read_order does not match expected operator-priority read order",
    )

    anti_corruption_contract_file = state.get("anti_corruption_contract", {}).get("anti_corruption_contract_file", "")
    _require(
        anti_corruption_contract_file == "ARIS_BOOT.md",
        f"anti_corruption_contract_file must be 'ARIS_BOOT.md', got: {anti_corruption_contract_file!r}",
    )

    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is True,
        "prompt_only direct-prompt preference logic must allow clean prompt emission",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="operator",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "operator advance_mode must never be authorized by prompt preference",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=True,
        ) is False,
        "manual authorization lock must override prompt emission preference",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=False,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass canonical pass requirement",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=False,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass green CI requirement",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=False,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass green validator requirement",
    )
    transition_row = _get_transition_row(state.get("current_phase_id", ""), state.get("decision", ""))
    if (
        state.get("current_phase_id") == CURRENT_LIVE_PHASE_ID
        and state.get("decision") == EXPECTED_DECISION
        and state.get("status") == CURRENT_LIVE_STATUS
    ):
        transition_row = {
            "next_phase_id": CURRENT_EXPECTED_NEXT_PHASE_ID,
            "next_phase_class": CURRENT_EXPECTED_NEXT_PHASE_CLASS,
            "advance_mode": EXPECTED_CURRENT_SUCCESSOR_ADVANCE_MODE,
        }
    if state.get("status") in PURG00_LIVE_ROUTE_PRESERVING_STATUSES:
        transition_row = _get_transition_row(PURG_PRE_LIVE_ROUTE_PHASE_ID, "pass")
    if state.get("status") == PURG01_ROUTE_ADMISSION_STATUS:
        transition_row = _get_transition_row(EXPECTED_NEXT_PHASE_ID, "pass")
    if transition_row is None:
        _require(state.get("next_phase") is None, "terminal phase must keep next_phase null when there is no successor row")
        _require(state.get("active_next_phase") is None, "terminal phase must keep active_next_phase null when there is no successor row")
        _require(
            state.get("next_phase_authorized_by_operator") is False,
            "terminal wait-state must not declare a live next phase authorization",
        )
    else:
        _require(
            transition_row.get("advance_mode") == EXPECTED_CURRENT_SUCCESSOR_ADVANCE_MODE,
            "unexpected advance_mode for current infernus successor",
        )
        _require(state.get("next_phase") == transition_row.get("next_phase_id"), "next_phase must match successor row")
        _require(
            state.get("active_next_phase_class") == transition_row.get("next_phase_class"),
            "active_next_phase_class must match successor row",
        )
        expected_next_phase_authorized = not (
            state.get("current_phase_id") == CURRENT_LIVE_PHASE_ID
            and state.get("status") == CURRENT_LIVE_STATUS
        )
        _require(
            state.get("next_phase_authorized_by_operator") is expected_next_phase_authorized,
            (
                "standing authorization must mark next phase as operator-authorized via canonroadmap approval"
                if expected_next_phase_authorized
                else "reconciled PURG-04 live route must keep next_phase_authorized_by_operator false"
            ),
        )
    auth = state.get("authorization", {})
    for key in [
        "production_authorized",
        "product_ready",
        "real_apply_authorized",
        "runtime_integration_allowed",
        "secrets_access_authorized",
        "external_llm_api_authorized",
    ]:
        _require(auth.get(key) is False, f"operator preference must not override safety lock: {key}")


def _check_ci_terminal_reporting_rule() -> None:
    for path in [
        CI_TERMINAL_REPORTING_RULE_DECISION_PATH,
        CI_TERMINAL_REPORTING_RULE_SUMMARY_PATH,
        CI_TERMINAL_REPORTING_RULE_REPORT_PATH,
    ]:
        _require(path.exists(), f"missing CI terminal reporting rule artifact: {path}")

    decision_data = _load_json(CI_TERMINAL_REPORTING_RULE_DECISION_PATH)
    summary_data = _load_json(CI_TERMINAL_REPORTING_RULE_SUMMARY_PATH)

    _require(decision_data.get("artifact_id") == "ci_terminal_reporting_rule", "CI rule artifact_id mismatch")
    _require(decision_data.get("decision") == "pass", "CI rule decision must be pass")
    _require(
        decision_data.get("status") == "ci_terminal_reporting_rule_materialized",
        "CI rule status mismatch",
    )
    _require(decision_data.get("final_report_allowed_with_pending_ci") is False, "CI rule pending-final flag mismatch")
    _require(
        decision_data.get("ci_green_confirmed_requires_all_terminal_success") is True,
        "CI rule green-confirmed requirement mismatch",
    )
    _require(
        decision_data.get("ci_failed_requires_terminal_failure_evidence") is True,
        "CI rule failed-evidence requirement mismatch",
    )
    _require(decision_data.get("ci_pending_is_interim_only") is True, "CI rule pending-interim flag mismatch")
    _require(
        decision_data.get("phase_advance_allowed_with_pending_ci") is False,
        "CI rule must block phase advance with pending CI",
    )
    _require(
        decision_data.get("next_prompt_allowed_with_pending_ci") is False,
        "CI rule must block next prompt with pending CI",
    )
    _require(
        decision_data.get("local_validation_overrides_remote_ci") is False,
        "CI rule must forbid local override of remote CI",
    )
    _require(
        summary_data.get("terminal_states") == ["CI_GREEN_CONFIRMED", "CI_FAILED", "CI_PENDING"],
        "CI rule summary terminal states mismatch",
    )

    _mirror_contains(
        ROOT / "ARIS_BOOT.md",
        "CI_GREEN_CONFIRMED",
        "CI_FAILED",
        "CI_PENDING",
    )

    _require(
        classify_ci_terminal_state(
            [{"status": "completed", "conclusion": "success"}]
        ) == "CI_GREEN_CONFIRMED",
        "CI terminal-state classifier must allow all-success terminal green",
    )
    _require(
        classify_ci_terminal_state(
            [{"status": "in_progress", "conclusion": ""}]
        ) == "CI_PENDING",
        "CI terminal-state classifier must keep in-progress reports pending",
    )
    _require(
        classify_ci_terminal_state(
            [{"status": "completed", "conclusion": "failure"}]
        ) == "CI_FAILED",
        "CI terminal-state classifier must fail terminal failures",
    )


def _check_acb_core_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CORE_01_EVIDENCE_PATH.exists(), "missing ACB-CORE-01 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CORE_01_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CORE-01", "ACB evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB evidence repository mismatch")
    _require(evidence_data.get("project_sha") == "0e935f41830101c391905611473e52e883d36a26", "ACB evidence project_sha mismatch")
    _require(evidence_data.get("supply_chain_ci", {}).get("conclusion") == "success", "ACB evidence supply-chain CI must be success")
    _require(
        evidence_data.get("supply_chain_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26916868686",
        "ACB evidence supply-chain CI URL mismatch",
    )
    for key in [
        "uv_lock_exists",
        "pip_audit_gate_exists",
        "sbom_exists",
        "pyproject_exists",
        "validation_runner_exists",
        "test_exists",
        "uv_bootstrap_exists",
    ]:
        _require(evidence_data.get("deliverables", {}).get(key) is True, f"ACB evidence deliverable {key} must be true")
    _require(evidence_data.get("local_validation", {}).get("pass_criteria_met") is True, "ACB evidence pass_criteria_met must be true")
    _require(evidence_data.get("local_validation", {}).get("uv_version") == "0.11.18", "ACB evidence uv_version mismatch")

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_core_01"
    required_paths = [
        PROJECT_ROOT / "pyproject.toml",
        PROJECT_ROOT / "uv.lock",
        PROJECT_ROOT / ".github" / "workflows" / "supply-chain-baseline.yml",
        PROJECT_ROOT / "scripts" / "run_acb_core_01_supply_chain_validation.py",
        PROJECT_ROOT / "tests" / "test_acb_core_01_supply_chain.py",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
        artifacts_root / "dependency_inventory.json",
        artifacts_root / "sbom.cdx.json",
        artifacts_root / "supply_chain_validation.json",
        artifacts_root / "uv_bootstrap.json",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CORE-01 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    inventory_data = _load_json(artifacts_root / "dependency_inventory.json")
    sbom_data = _load_json(artifacts_root / "sbom.cdx.json")
    validation_data = _load_json(artifacts_root / "supply_chain_validation.json")
    bootstrap_data = _load_json(artifacts_root / "uv_bootstrap.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "supply-chain-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CORE-01", "ACB decision phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "PURG-01", "ACB decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "ACB decision must be pass")
    _require(decision_data.get("status") == "acb_core_01_pass", "ACB decision status mismatch")
    _require(decision_data.get("phase_class") == "capability_build", "ACB decision phase_class mismatch")
    _require(decision_data.get("uv_available") is True, "ACB decision uv_available must be true")
    _require(decision_data.get("uv_bootstrap_created") is True, "ACB decision uv_bootstrap_created must be true")
    _require(decision_data.get("uv_lock_created_or_verified") is True, "ACB decision uv_lock_created_or_verified must be true")
    _require(decision_data.get("pip_audit_gate_created_or_verified") is True, "ACB decision pip_audit_gate_created_or_verified must be true")
    _require(decision_data.get("cyclonedx_sbom_created_or_verified") is True, "ACB decision cyclonedx_sbom_created_or_verified must be true")
    _require(decision_data.get("pass_criteria_met") is True, "ACB decision pass_criteria_met must be true")
    _require(decision_data.get("next_phase") is None, "ACB decision next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "ACB decision must not authorize next phase")

    _require(summary_data.get("phase_id") == "ACB-CORE-01", "ACB summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB summary decision must be pass")
    _require(summary_data.get("status") == "acb_core_01_pass", "ACB summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB summary minimum_deliverable_met must be true")

    _require(inventory_data.get("uv_available") is True, "ACB inventory uv_available must be true")
    _require(inventory_data.get("pyproject_present") is True, "ACB inventory pyproject_present must be true")
    _require(inventory_data.get("lockfile_after") == "uv.lock", "ACB inventory lockfile_after must be uv.lock")
    _require(inventory_data.get("supply_chain_tools_detected", {}).get("uv_binary") is True, "ACB inventory must record uv binary")

    _require(sbom_data.get("bomFormat") == "CycloneDX", "ACB SBOM bomFormat must be CycloneDX")
    _require(sbom_data.get("generation_mode") in {"tool_generated", "deterministic_minimal"}, "ACB SBOM generation_mode invalid")

    _require(validation_data.get("uv_lock_exists") is True, "ACB validation uv_lock_exists must be true")
    _require(validation_data.get("pip_audit_gate_exists") is True, "ACB validation pip_audit_gate_exists must be true")
    _require(validation_data.get("sbom_exists") is True, "ACB validation sbom_exists must be true")
    _require(validation_data.get("pass_criteria_met") is True, "ACB validation pass_criteria_met must be true")

    _require(bootstrap_data.get("uv_available_after") is True, "ACB bootstrap uv_available_after must be true")
    _require(bootstrap_data.get("bootstrap_result") == "success", "ACB bootstrap_result must be success")
    _require(bool(bootstrap_data.get("uv_version_after")), "ACB bootstrap must record uv version")

    _require("uv lock --check" in workflow_text, "supply-chain workflow must check uv lock freshness")
    _require("pip-audit" in workflow_text, "supply-chain workflow must include pip-audit gate")


def _check_acb_core_02_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CORE_02_EVIDENCE_PATH.exists(), "missing ACB-CORE-02 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CORE_02_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CORE-02 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "46910e0fda3fc64a19818ad80f39813227b53922",
        "ACB-CORE-02 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("core_public_api_ci", {}).get("conclusion") == "success",
        "ACB-CORE-02 evidence core-public-api CI must be success",
    )
    _require(
        evidence_data.get("core_public_api_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26917991639",
        "ACB-CORE-02 evidence core-public-api CI URL mismatch",
    )
    for key in [
        "research_basis_exists",
        "snapshot_before_exists",
        "snapshot_after_exists",
        "import_stability_report_exists",
        "explicit_all_created_or_verified",
        "protocols_created_or_verified",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CORE-02 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CORE-02 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("package_root_detected") == "src/aris",
        "ACB-CORE-02 evidence package_root_detected mismatch",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_core_02"
    required_paths = [
        PROJECT_ROOT / "src" / "aris" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "contracts.py",
        PROJECT_ROOT / ".github" / "workflows" / "core-public-api-baseline.yml",
        PROJECT_ROOT / "scripts" / "run_acb_core_02_public_api_snapshot.py",
        PROJECT_ROOT / "tests" / "test_acb_core_02_public_api.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "public_api_snapshot_before.json",
        artifacts_root / "public_api_snapshot_after.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CORE-02 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    snapshot_before = _load_json(artifacts_root / "public_api_snapshot_before.json")
    snapshot_after = _load_json(artifacts_root / "public_api_snapshot_after.json")
    report_data = _load_json(artifacts_root / "import_stability_report.json")
    init_text = (PROJECT_ROOT / "src" / "aris" / "__init__.py").read_text(encoding="utf-8")
    contracts_text = (PROJECT_ROOT / "src" / "aris" / "contracts.py").read_text(encoding="utf-8")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "core-public-api-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 decision phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "ACB-CORE-01", "ACB-CORE-02 decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CORE-02 decision must be pass")
    _require(decision_data.get("status") == "acb_core_02_pass", "ACB-CORE-02 decision status mismatch")
    _require(decision_data.get("phase_class") == "capability_build", "ACB-CORE-02 decision phase_class mismatch")
    _require(decision_data.get("explicit_all_created_or_verified") is True, "ACB-CORE-02 decision explicit_all_created_or_verified must be true")
    _require(decision_data.get("protocols_created_or_verified") is True, "ACB-CORE-02 decision protocols_created_or_verified must be true")
    _require(decision_data.get("import_smoke_tests_passed") is True, "ACB-CORE-02 decision import_smoke_tests_passed must be true")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CORE-02 decision pass_criteria_met must be true")
    _require(decision_data.get("next_phase") is None, "ACB-CORE-02 decision next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "ACB-CORE-02 decision must not authorize next phase")

    _require(summary_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CORE-02 summary decision must be pass")
    _require(summary_data.get("status") == "acb_core_02_pass", "ACB-CORE-02 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CORE-02 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CORE-02 summary minimum_deliverable_met must be true")

    _require(snapshot_before.get("package_root_detected") == "src/aris", "ACB-CORE-02 snapshot_before package_root_detected mismatch")
    _require(snapshot_after.get("package_root_detected") == "src/aris", "ACB-CORE-02 snapshot_after package_root_detected mismatch")
    _require(snapshot_before.get("exported_all_symbols") == [], "ACB-CORE-02 snapshot_before exported_all_symbols must be empty")
    _require(bool(snapshot_after.get("exported_all_symbols")), "ACB-CORE-02 snapshot_after exported_all_symbols must be non-empty")
    _require("contracts" in snapshot_after.get("exported_all_symbols", []), "ACB-CORE-02 snapshot_after must export contracts")
    _require("CommandPolicyProtocol" in snapshot_after.get("exported_all_symbols", []), "ACB-CORE-02 snapshot_after must export Protocols")

    _require(report_data.get("import_smoke_tests_executed") is True, "ACB-CORE-02 import report must execute smoke tests")
    _require(report_data.get("import_smoke_tests_passed") is True, "ACB-CORE-02 import report must pass smoke tests")
    _require(report_data.get("pass_criteria_met") is True, "ACB-CORE-02 import report pass_criteria_met must be true")
    _require("contracts" in report_data.get("modules_tested", []), "ACB-CORE-02 import report must test contracts")

    _require("__all__" in init_text, "ACB-CORE-02 root __init__ must define __all__")
    _require("Protocol" in contracts_text, "ACB-CORE-02 contracts must define Protocols")
    _require("python -m pip install pytest" in workflow_text, "ACB-CORE-02 workflow must install pytest")


def _check_acb_cap_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_01_OPERATOR_AUTH_PATH.exists(), "missing ACB-CAP-01 operator authorization artifact in active-context")
    _require(ACB_CAP_01_EVIDENCE_PATH.exists(), "missing ACB-CAP-01 evidence artifact in active-context")

    operator_auth = _load_json(ACB_CAP_01_OPERATOR_AUTH_PATH)
    _require(operator_auth.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 operator authorization phase_id mismatch")
    _require(operator_auth.get("operator") == "MatheusAugDEV", "ACB-CAP-01 operator authorization operator mismatch")
    _require(operator_auth.get("authorized") is True, "ACB-CAP-01 operator authorization must be true")
    _require(operator_auth.get("constraints", {}).get("next_phase_must_remain_null") is True, "ACB-CAP-01 operator authorization must lock next_phase to null")
    _require(operator_auth.get("constraints", {}).get("server_real_allowed") is False, "ACB-CAP-01 operator authorization must keep server_real_allowed false")
    _require(operator_auth.get("constraints", {}).get("external_network_test_allowed") is False, "ACB-CAP-01 operator authorization must keep external_network_test_allowed false")
    _require(operator_auth.get("constraints", {}).get("real_secrets_allowed") is False, "ACB-CAP-01 operator authorization must keep real_secrets_allowed false")

    evidence_data = _load_json(ACB_CAP_01_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-01 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
        "ACB-CAP-01 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("backend_baseline_ci", {}).get("conclusion") == "success",
        "ACB-CAP-01 evidence backend-baseline CI must be success",
    )
    _require(
        evidence_data.get("backend_baseline_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26920310615",
        "ACB-CAP-01 evidence backend-baseline CI URL mismatch",
    )
    for key in [
        "fastapi_app_exists",
        "health_check_exists",
        "ready_check_exists",
        "jwt_auth_exists",
        "api_key_auth_exists",
        "tenant_isolation_exists",
        "slowapi_rate_limit_exists",
        "backend_tests_exist",
        "backend_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-01 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-01 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("health_check_passing") is True,
        "ACB-CAP-01 evidence health_check_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("auth_passing") is True,
        "ACB-CAP-01 evidence auth_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("rate_limit_passing") is True,
        "ACB-CAP-01 evidence rate_limit_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable") is True,
        "ACB-CAP-01 evidence public_api_stable must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_01"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "backend-baseline.yml",
        PROJECT_ROOT / "src" / "aris" / "backend" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "app.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "auth.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "rate_limit.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_01_backend_baseline.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_01_backend.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "backend_contract.json",
        artifacts_root / "auth_matrix.json",
        artifacts_root / "rate_limit_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-01 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    backend_contract = _load_json(artifacts_root / "backend_contract.json")
    auth_matrix = _load_json(artifacts_root / "auth_matrix.json")
    rate_limit_report = _load_json(artifacts_root / "rate_limit_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "backend-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Backend Baseline Gate", "ACB-CAP-01 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_01_pass", "ACB-CAP-01 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-01 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-01 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-01 decision minimum_deliverable_met must be true")
    _require(decision_data.get("fastapi_health_check_passing") is True, "ACB-CAP-01 decision fastapi_health_check_passing must be true")
    _require(decision_data.get("auth_passing") is True, "ACB-CAP-01 decision auth_passing must be true")
    _require(decision_data.get("jwt_auth_passing") is True, "ACB-CAP-01 decision jwt_auth_passing must be true")
    _require(decision_data.get("api_key_auth_passing") is True, "ACB-CAP-01 decision api_key_auth_passing must be true")
    _require(decision_data.get("tenant_isolation_passing") is True, "ACB-CAP-01 decision tenant_isolation_passing must be true")
    _require(decision_data.get("slowapi_rate_limit_passing") is True, "ACB-CAP-01 decision slowapi_rate_limit_passing must be true")
    _require(decision_data.get("network_server_started") is False, "ACB-CAP-01 decision network_server_started must be false")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-01 decision external_network_used must be false")
    _require(decision_data.get("real_secret_used") is False, "ACB-CAP-01 decision real_secret_used must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-01 decision database_created must be false")
    _require(decision_data.get("runtime_mutation_authorized") is False, "ACB-CAP-01 decision runtime_mutation_authorized must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-01 decision product_promotion_allowed must be false")

    _require(summary_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-01 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_01_pass", "ACB-CAP-01 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-01 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-01 summary minimum_deliverable_met must be true")
    for key in [
        "fastapi_app_exists",
        "health_check_exists",
        "ready_check_exists",
        "jwt_auth_exists",
        "api_key_auth_exists",
        "tenant_isolation_exists",
        "slowapi_rate_limit_exists",
        "backend_tests_exist",
        "backend_artifacts_exist",
    ]:
        _require(summary_data.get("deliverables", {}).get(key) is True, f"ACB-CAP-01 summary deliverable {key} must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_backend_baseline_only", "ACB-CAP-01 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "uvicorn_runtime_server", "ACB-CAP-01 research_basis rejected_pattern mismatch")

    _require(backend_contract.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 backend_contract phase_id mismatch")
    _require(backend_contract.get("app_factory") == "create_app(settings: BackendSettings | None = None) -> FastAPI", "ACB-CAP-01 backend_contract app_factory mismatch")
    _require(backend_contract.get("network_server_started") is False, "ACB-CAP-01 backend_contract network_server_started must be false")
    _require(backend_contract.get("external_network_used") is False, "ACB-CAP-01 backend_contract external_network_used must be false")
    _require(backend_contract.get("database_created") is False, "ACB-CAP-01 backend_contract database_created must be false")
    endpoints = {(item.get("method"), item.get("path")): item for item in backend_contract.get("public_endpoints", [])}
    _require(("GET", "/healthz") in endpoints, "ACB-CAP-01 backend_contract must expose GET /healthz")
    _require(("GET", "/readyz") in endpoints, "ACB-CAP-01 backend_contract must expose GET /readyz")
    _require(("POST", "/api/v1/auth/token") in endpoints, "ACB-CAP-01 backend_contract must expose POST /api/v1/auth/token")
    _require(("GET", "/api/v1/tenant/me") in endpoints, "ACB-CAP-01 backend_contract must expose GET /api/v1/tenant/me")
    _require(("GET", "/api/v1/tenant/api-key-check") in endpoints, "ACB-CAP-01 backend_contract must expose GET /api/v1/tenant/api-key-check")
    _require(endpoints.get(("GET", "/api/v1/rate-limited"), {}).get("rate_limit") == "2/minute", "ACB-CAP-01 backend_contract rate limit mismatch")

    _require(auth_matrix.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 auth_matrix phase_id mismatch")
    _require(auth_matrix.get("token_issue_status") == 200, "ACB-CAP-01 auth_matrix token_issue_status mismatch")
    _require(auth_matrix.get("missing_bearer_status") == 401, "ACB-CAP-01 auth_matrix missing_bearer_status mismatch")
    _require(auth_matrix.get("invalid_api_key_status") == 401, "ACB-CAP-01 auth_matrix invalid_api_key_status mismatch")
    _require(auth_matrix.get("valid_api_key_status") == 200, "ACB-CAP-01 auth_matrix valid_api_key_status mismatch")
    _require(auth_matrix.get("cross_tenant_api_key_status") == 403, "ACB-CAP-01 auth_matrix cross_tenant_api_key_status mismatch")
    _require(auth_matrix.get("valid_jwt_status") == 200, "ACB-CAP-01 auth_matrix valid_jwt_status mismatch")
    _require(auth_matrix.get("expired_jwt_status") == 401, "ACB-CAP-01 auth_matrix expired_jwt_status mismatch")
    _require(auth_matrix.get("wrong_tenant_jwt_status") == 403, "ACB-CAP-01 auth_matrix wrong_tenant_jwt_status mismatch")
    _require(auth_matrix.get("jwt_auth_passing") is True, "ACB-CAP-01 auth_matrix jwt_auth_passing must be true")
    _require(auth_matrix.get("api_key_auth_passing") is True, "ACB-CAP-01 auth_matrix api_key_auth_passing must be true")
    _require(auth_matrix.get("tenant_isolation_passing") is True, "ACB-CAP-01 auth_matrix tenant_isolation_passing must be true")

    _require(rate_limit_report.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 rate_limit_report phase_id mismatch")
    _require(rate_limit_report.get("limit") == "2/minute", "ACB-CAP-01 rate_limit_report limit mismatch")
    _require(rate_limit_report.get("statuses") == [200, 200, 429], "ACB-CAP-01 rate_limit_report statuses mismatch")
    _require(rate_limit_report.get("slowapi_rate_limit_passing") is True, "ACB-CAP-01 rate_limit_report slowapi_rate_limit_passing must be true")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 public_api_drift phase_id mismatch")
    _require(public_api_drift.get("drift_detected") is False, "ACB-CAP-01 public_api_drift drift_detected must be false")
    _require(public_api_drift.get("public_api_stable") is True, "ACB-CAP-01 public_api_drift public_api_stable must be true")

    _require(import_report.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 import_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-01 import_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable") is True, "ACB-CAP-01 import_report public_api_stable must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-01 import_report forbidden_runtime_patterns must be empty")

    _require("name: Backend Baseline" in workflow_text, "ACB-CAP-01 workflow must be Backend Baseline")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-01 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-01 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_01_backend_baseline.py" in workflow_text, "ACB-CAP-01 workflow must validate backend baseline artifacts")
    _require("tests/test_acb_cap_01_backend.py -v" in workflow_text, "ACB-CAP-01 workflow must run backend tests")


def _check_acb_cap_02_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_02_EVIDENCE_PATH.exists(), "missing ACB-CAP-02 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_02_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-02 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b2fdc3c994342a42a84823fa15615c931f1bc00e",
        "ACB-CAP-02 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
        "ACB-CAP-02 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("mcp_runtime_sandbox_ci", {}).get("conclusion") == "success",
        "ACB-CAP-02 evidence MCP Runtime Sandbox CI must be success",
    )
    _require(
        evidence_data.get("mcp_runtime_sandbox_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26922186509",
        "ACB-CAP-02 evidence MCP Runtime Sandbox CI URL mismatch",
    )
    for key in [
        "mcp_runtime_package_exists",
        "stdio_ban_exists",
        "sandbox_spec_exists",
        "policy_pre_dispatch_exists",
        "kill_switch_exists",
        "rollback_contract_exists",
        "audit_event_exists",
        "mcp_runtime_tests_exist",
        "mcp_runtime_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-02 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-02 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("mcp_sandbox_running") is True,
        "ACB-CAP-02 evidence mcp_sandbox_running must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("stdio_banned") is True,
        "ACB-CAP-02 evidence stdio_banned must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("policy_pre_dispatch_passing") is True,
        "ACB-CAP-02 evidence policy_pre_dispatch_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("kill_switch_passing") is True,
        "ACB-CAP-02 evidence kill_switch_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("rollback_contract_passing") is True,
        "ACB-CAP-02 evidence rollback_contract_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("network_none_enforced") is True,
        "ACB-CAP-02 evidence network_none_enforced must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable") is True,
        "ACB-CAP-02 evidence public_api_stable must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_02"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "mcp-runtime-sandbox.yml",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "transport_policy.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "sandbox_spec.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "policy_engine.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "dispatcher.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "kill_switch.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "rollback.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "audit.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_02_mcp_runtime_sandbox.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_02_mcp_runtime_sandbox.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "mcp_runtime_contract.json",
        artifacts_root / "transport_policy_matrix.json",
        artifacts_root / "sandbox_spec.json",
        artifacts_root / "policy_decision_matrix.json",
        artifacts_root / "kill_switch_matrix.json",
        artifacts_root / "rollback_contract.json",
        artifacts_root / "audit_event_sample.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-02 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "mcp_runtime_contract.json")
    transport_matrix = _load_json(artifacts_root / "transport_policy_matrix.json")
    sandbox_spec = _load_json(artifacts_root / "sandbox_spec.json")
    policy_matrix = _load_json(artifacts_root / "policy_decision_matrix.json")
    kill_switch_matrix = _load_json(artifacts_root / "kill_switch_matrix.json")
    rollback_contract = _load_json(artifacts_root / "rollback_contract.json")
    audit_event = _load_json(artifacts_root / "audit_event_sample.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "mcp-runtime-sandbox.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build MCP Runtime Sandbox Gate", "ACB-CAP-02 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_02_pass", "ACB-CAP-02 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-02 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-02 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-02 decision minimum_deliverable_met must be true")
    _require(decision_data.get("mcp_sandbox_running") is True, "ACB-CAP-02 decision mcp_sandbox_running must be true")
    _require(decision_data.get("stdio_banned") is True, "ACB-CAP-02 decision stdio_banned must be true")
    _require(decision_data.get("policy_pre_dispatch_passing") is True, "ACB-CAP-02 decision policy_pre_dispatch_passing must be true")
    _require(decision_data.get("kill_switch_passing") is True, "ACB-CAP-02 decision kill_switch_passing must be true")
    _require(decision_data.get("rollback_contract_passing") is True, "ACB-CAP-02 decision rollback_contract_passing must be true")
    _require(decision_data.get("network_none_enforced") is True, "ACB-CAP-02 decision network_none_enforced must be true")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-02 decision external_network_used must be false")
    _require(decision_data.get("server_real_started") is False, "ACB-CAP-02 decision server_real_started must be false")
    _require(decision_data.get("subprocess_stdio_started") is False, "ACB-CAP-02 decision subprocess_stdio_started must be false")
    _require(decision_data.get("real_tool_execution_used") is False, "ACB-CAP-02 decision real_tool_execution_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "ACB-CAP-02 decision secrets_accessed must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-02 decision database_created must be false")
    _require(decision_data.get("runtime_productive_mutation") is False, "ACB-CAP-02 decision runtime_productive_mutation must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-02 decision product_promotion_allowed must be false")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-02 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-02 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_02_pass", "ACB-CAP-02 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-02 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-02 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_mcp_runtime_sandbox_gate_only", "ACB-CAP-02 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "stdio_transport_runtime", "ACB-CAP-02 research_basis rejected_pattern mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 contract phase_id mismatch")
    _require(contract_data.get("allowed_transport") == "streamable_http", "ACB-CAP-02 allowed_transport mismatch")
    _require(contract_data.get("banned_transport") == "stdio", "ACB-CAP-02 banned_transport mismatch")
    _require(contract_data.get("mcp_sandbox_running") is True, "ACB-CAP-02 contract mcp_sandbox_running must be true")
    _require(contract_data.get("server_real_started") is False, "ACB-CAP-02 contract server_real_started must be false")
    _require(contract_data.get("external_network_used") is False, "ACB-CAP-02 contract external_network_used must be false")
    _require(contract_data.get("real_tool_execution_used") is False, "ACB-CAP-02 contract real_tool_execution_used must be false")
    _require(contract_data.get("subprocess_stdio_started") is False, "ACB-CAP-02 contract subprocess_stdio_started must be false")

    transport_cases = {item.get("name"): item for item in transport_matrix.get("cases", [])}
    _require(transport_cases.get("stdio_blocked", {}).get("decision") == "block", "ACB-CAP-02 stdio transport must be blocked")
    _require("stdio_transport_banned" in transport_cases.get("stdio_blocked", {}).get("reasons", []), "ACB-CAP-02 stdio transport block reason mismatch")
    _require(transport_cases.get("streamable_http_allowed", {}).get("decision") == "allow", "ACB-CAP-02 streamable_http transport must be allowed")

    spec = sandbox_spec.get("spec", {})
    _require(spec.get("network_mode") == "none", "ACB-CAP-02 sandbox network_mode mismatch")
    _require(spec.get("filesystem_mode") == "read_only", "ACB-CAP-02 sandbox filesystem_mode mismatch")
    _require(spec.get("allow_write_paths") == [], "ACB-CAP-02 sandbox allow_write_paths must be empty")
    _require(spec.get("secrets_mount_allowed") is False, "ACB-CAP-02 sandbox secrets_mount_allowed must be false")
    _require(spec.get("process_secret_read_allowed") is False, "ACB-CAP-02 sandbox process_secret_read_allowed must be false")
    _require(spec.get("egress_allowed") is False, "ACB-CAP-02 sandbox egress_allowed must be false")
    _require(spec.get("host_mount_allowed") is False, "ACB-CAP-02 sandbox host_mount_allowed must be false")
    _require(sandbox_spec.get("runner_running") is True, "ACB-CAP-02 sandbox runner_running must be true")

    _require(policy_matrix.get("cases", {}).get("allowed_streamable_http", {}).get("decision") == "allow", "ACB-CAP-02 policy matrix allow case mismatch")
    _require(policy_matrix.get("cases", {}).get("stdio_blocked", {}).get("decision") == "block", "ACB-CAP-02 policy matrix stdio case mismatch")
    _require(policy_matrix.get("cases", {}).get("missing_rollback", {}).get("rollback_ready") is False, "ACB-CAP-02 policy matrix missing_rollback rollback_ready must be false")
    _require(policy_matrix.get("cases", {}).get("side_effect_with_rollback", {}).get("rollback_ready") is True, "ACB-CAP-02 policy matrix rollback-ready case mismatch")

    _require(kill_switch_matrix.get("cases", {}).get("global_disabled", {}).get("executed") is False, "ACB-CAP-02 kill switch global_disabled must not execute")
    _require(kill_switch_matrix.get("cases", {}).get("emergency_stop", {}).get("executed") is False, "ACB-CAP-02 kill switch emergency_stop must not execute")

    _require(rollback_contract.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 rollback_contract phase_id mismatch")
    _require(rollback_contract.get("missing_rollback_plan", {}).get("rollback_ready") is False, "ACB-CAP-02 rollback missing plan readiness mismatch")
    _require(rollback_contract.get("rollback_plan_ready", {}).get("rollback_ready") is True, "ACB-CAP-02 rollback ready case mismatch")

    _require(audit_event.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 audit_event phase_id mismatch")
    _require(audit_event.get("policy_decision") == "allow", "ACB-CAP-02 audit_event policy_decision mismatch")
    _require(bool(audit_event.get("audit_event_sha256")), "ACB-CAP-02 audit_event_sha256 must be non-empty")

    _require(import_report.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 import_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-02 import_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable") is True, "ACB-CAP-02 import_report public_api_stable must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-02 import_report forbidden_runtime_patterns must be empty")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 public_api_drift phase_id mismatch")
    _require(public_api_drift.get("drift_detected") is False, "ACB-CAP-02 public_api_drift drift_detected must be false")
    _require(public_api_drift.get("public_api_stable") is True, "ACB-CAP-02 public_api_drift public_api_stable must be true")

    _require("name: MCP Runtime Sandbox" in workflow_text, "ACB-CAP-02 workflow must be MCP Runtime Sandbox")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-02 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-02 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_02_mcp_runtime_sandbox.py" in workflow_text, "ACB-CAP-02 workflow must run the sandbox artifact validator")
    _require("tests/test_acb_cap_02_mcp_runtime_sandbox.py -v" in workflow_text, "ACB-CAP-02 workflow must run MCP runtime sandbox tests")
    _require("uv lock --check" in workflow_text, "ACB-CAP-02 workflow must check uv lock freshness")


def _check_acb_cap_03_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_03_EVIDENCE_PATH.exists(), "missing ACB-CAP-03 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_03_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-03 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b1d175f8b0d1105a9d05f6ddcab082c71d6f6b3e",
        "ACB-CAP-03 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b2fdc3c994342a42a84823fa15615c931f1bc00e",
        "ACB-CAP-03 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("runtime_public_api_ci", {}).get("conclusion") == "success",
        "ACB-CAP-03 evidence Runtime Public API CI must be success",
    )
    _require(
        evidence_data.get("runtime_public_api_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26923273196",
        "ACB-CAP-03 evidence Runtime Public API CI URL mismatch",
    )
    for key in [
        "runtime_package_exists",
        "runtime_public_api_documented",
        "runtime_public_api_contract_exists",
        "runtime_facade_exists",
        "runtime_modes_enforced",
        "runtime_policy_bridge_exists",
        "runtime_audit_hashing_exists",
        "public_api_drift_ratified",
        "runtime_tests_exist",
        "runtime_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-03 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-03 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_public_api_importable") is True,
        "ACB-CAP-03 evidence runtime_public_api_importable must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_facade_passing") is True,
        "ACB-CAP-03 evidence runtime_facade_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_policy_bridge_passing") is True,
        "ACB-CAP-03 evidence runtime_policy_bridge_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_audit_hashing_passing") is True,
        "ACB-CAP-03 evidence runtime_audit_hashing_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable_or_ratified") is True,
        "ACB-CAP-03 evidence public_api_stable_or_ratified must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_03"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "runtime-public-api.yml",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "facade.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "execution_plan.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "request.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "response.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "policy_bridge.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "audit_bridge.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "public_api.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_03_runtime_public_api.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_03_runtime_public_api.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "runtime_public_api.md",
        artifacts_root / "runtime_public_api_contract.json",
        artifacts_root / "runtime_facade_contract.json",
        artifacts_root / "runtime_mode_matrix.json",
        artifacts_root / "runtime_policy_bridge_matrix.json",
        artifacts_root / "runtime_audit_report.json",
        artifacts_root / "public_api_snapshot_before.json",
        artifacts_root / "public_api_snapshot_after.json",
        artifacts_root / "public_api_change_report.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-03 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "runtime_public_api_contract.json")
    facade_contract = _load_json(artifacts_root / "runtime_facade_contract.json")
    mode_matrix = _load_json(artifacts_root / "runtime_mode_matrix.json")
    policy_matrix = _load_json(artifacts_root / "runtime_policy_bridge_matrix.json")
    audit_report = _load_json(artifacts_root / "runtime_audit_report.json")
    before_snapshot = _load_json(artifacts_root / "public_api_snapshot_before.json")
    after_snapshot = _load_json(artifacts_root / "public_api_snapshot_after.json")
    public_api_drift = _load_json(artifacts_root / "public_api_change_report.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "runtime-public-api.yml").read_text(encoding="utf-8")
    markdown_text = (artifacts_root / "runtime_public_api.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Runtime Top-Level Public API Gate", "ACB-CAP-03 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_03_pass", "ACB-CAP-03 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-03 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-03 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-03 decision minimum_deliverable_met must be true")
    _require(decision_data.get("runtime_public_api_documented") is True, "ACB-CAP-03 decision runtime_public_api_documented must be true")
    _require(decision_data.get("runtime_public_api_importable") is True, "ACB-CAP-03 decision runtime_public_api_importable must be true")
    _require(decision_data.get("runtime_facade_created") is True, "ACB-CAP-03 decision runtime_facade_created must be true")
    _require(decision_data.get("runtime_policy_bridge_passing") is True, "ACB-CAP-03 decision runtime_policy_bridge_passing must be true")
    _require(decision_data.get("runtime_audit_hashing_passing") is True, "ACB-CAP-03 decision runtime_audit_hashing_passing must be true")
    _require(decision_data.get("runtime_modes_enforced") is True, "ACB-CAP-03 decision runtime_modes_enforced must be true")
    _require(decision_data.get("public_api_drift_ratified") is True, "ACB-CAP-03 decision public_api_drift_ratified must be true")
    _require(decision_data.get("stdio_ban_preserved") is True, "ACB-CAP-03 decision stdio_ban_preserved must be true")
    _require(decision_data.get("mcp_policy_pre_dispatch_preserved") is True, "ACB-CAP-03 decision mcp_policy_pre_dispatch_preserved must be true")
    _require(decision_data.get("kill_switch_preserved") is True, "ACB-CAP-03 decision kill_switch_preserved must be true")
    _require(decision_data.get("rollback_contract_preserved") is True, "ACB-CAP-03 decision rollback_contract_preserved must be true")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-03 decision external_network_used must be false")
    _require(decision_data.get("server_real_started") is False, "ACB-CAP-03 decision server_real_started must be false")
    _require(decision_data.get("real_tool_execution_used") is False, "ACB-CAP-03 decision real_tool_execution_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "ACB-CAP-03 decision secrets_accessed must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-03 decision database_created must be false")
    _require(decision_data.get("runtime_productive_activation") is False, "ACB-CAP-03 decision runtime_productive_activation must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-03 decision product_promotion_allowed must be false")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-03 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-03 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_03_pass", "ACB-CAP-03 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-03 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-03 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_runtime_public_api_gate_only", "ACB-CAP-03 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "productive_runtime_activation", "ACB-CAP-03 research_basis rejected_pattern mismatch")
    _require(research_data.get("rejected_pattern_2") == "external_network_or_tool_execution", "ACB-CAP-03 research_basis rejected_pattern_2 mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 contract phase_id mismatch")
    _require(contract_data.get("module") == "aris.runtime", "ACB-CAP-03 contract module mismatch")
    _require(
        contract_data.get("public_symbols")
        == [
            "RuntimeAuditEvent",
            "RuntimeContext",
            "RuntimeDecision",
            "RuntimeExecutionPlan",
            "RuntimeFacade",
            "RuntimeMode",
            "RuntimePolicyDecision",
            "RuntimeRequest",
            "RuntimeResponse",
            "create_runtime",
        ],
        "ACB-CAP-03 contract public_symbols mismatch",
    )
    _require(contract_data.get("root_public_api_delta", {}).get("removed_symbols") == [], "ACB-CAP-03 contract removed_symbols must be empty")
    _require(contract_data.get("root_public_api_delta", {}).get("added_symbols") == [], "ACB-CAP-03 contract added_symbols must be empty")
    _require(contract_data.get("allowed_modes") == ["contract_only", "dry_safe"], "ACB-CAP-03 contract allowed_modes mismatch")
    _require(contract_data.get("blocked_modes") == ["disabled", "productive", "real_apply", "external_tool", "networked"], "ACB-CAP-03 contract blocked_modes mismatch")

    _require(facade_contract.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 facade_contract phase_id mismatch")
    _require(facade_contract.get("safe_default_mode") == "dry_safe", "ACB-CAP-03 facade safe_default_mode mismatch")
    _require(facade_contract.get("contract_only_status") == "contract_only_ready", "ACB-CAP-03 facade contract_only_status mismatch")
    _require(facade_contract.get("safe_dispatch_status") == "completed", "ACB-CAP-03 facade safe_dispatch_status mismatch")
    _require(facade_contract.get("server_real_started") is False, "ACB-CAP-03 facade server_real_started must be false")
    _require(facade_contract.get("external_network_used") is False, "ACB-CAP-03 facade external_network_used must be false")
    _require(facade_contract.get("real_tool_execution_used") is False, "ACB-CAP-03 facade real_tool_execution_used must be false")

    _require(mode_matrix.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_mode_matrix phase_id mismatch")
    _require(mode_matrix.get("cases", {}).get("contract_only", {}).get("status") == "contract_only_ready", "ACB-CAP-03 contract_only status mismatch")
    _require(mode_matrix.get("cases", {}).get("dry_safe", {}).get("status") == "completed", "ACB-CAP-03 dry_safe status mismatch")
    _require(mode_matrix.get("cases", {}).get("productive", {}).get("allowed") is False, "ACB-CAP-03 productive mode must be blocked")
    _require(mode_matrix.get("cases", {}).get("productive", {}).get("status") == "blocked_pre_dispatch", "ACB-CAP-03 productive mode status mismatch")
    _require(mode_matrix.get("cases", {}).get("real_apply", {}).get("blocked") is True, "ACB-CAP-03 real_apply must be blocked")
    _require(mode_matrix.get("cases", {}).get("external_tool", {}).get("blocked") is True, "ACB-CAP-03 external_tool must be blocked")
    _require(mode_matrix.get("cases", {}).get("networked", {}).get("blocked") is True, "ACB-CAP-03 networked must be blocked")

    _require(policy_matrix.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_policy_bridge_matrix phase_id mismatch")
    _require(policy_matrix.get("cases", {}).get("safe_request", {}).get("decision") == "allow", "ACB-CAP-03 safe_request must allow")
    _require(policy_matrix.get("cases", {}).get("missing_tenant", {}).get("decision") == "block", "ACB-CAP-03 missing_tenant must block")
    _require("missing_tenant" in policy_matrix.get("cases", {}).get("missing_tenant", {}).get("reasons", []), "ACB-CAP-03 missing_tenant reason mismatch")
    _require(policy_matrix.get("cases", {}).get("missing_auth", {}).get("decision") == "block", "ACB-CAP-03 missing_auth must block")
    _require("missing_auth_context" in policy_matrix.get("cases", {}).get("missing_auth", {}).get("reasons", []), "ACB-CAP-03 missing_auth reason mismatch")
    _require(policy_matrix.get("cases", {}).get("productive_mode", {}).get("decision") == "block", "ACB-CAP-03 productive_mode must block")
    _require("runtime_mode_blocked:productive" in policy_matrix.get("cases", {}).get("productive_mode", {}).get("reasons", []), "ACB-CAP-03 productive_mode reason mismatch")
    _require(policy_matrix.get("cases", {}).get("stdio_transport", {}).get("decision") == "block", "ACB-CAP-03 stdio_transport must block")
    _require("stdio_transport_banned" in policy_matrix.get("cases", {}).get("stdio_transport", {}).get("reasons", []), "ACB-CAP-03 stdio_transport reason mismatch")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("decision") == "allow", "ACB-CAP-03 rollback_ready must allow")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("rollback_required") is True, "ACB-CAP-03 rollback_ready rollback_required mismatch")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("rollback_ready") is True, "ACB-CAP-03 rollback_ready rollback_ready mismatch")

    _require(audit_report.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_audit_report phase_id mismatch")
    _require(audit_report.get("hash_stable") is True, "ACB-CAP-03 runtime_audit_report hash_stable must be true")
    _require(audit_report.get("safe_audit_hash") == audit_report.get("safe_audit_hash_repeat"), "ACB-CAP-03 safe audit hash must be stable")
    _require(bool(audit_report.get("contract_only_audit_hash")), "ACB-CAP-03 contract_only_audit_hash must be non-empty")
    _require(bool(audit_report.get("blocked_stdio_audit_hash")), "ACB-CAP-03 blocked_stdio_audit_hash must be non-empty")

    _require(before_snapshot.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_snapshot_before phase_id mismatch")
    _require(before_snapshot.get("runtime_module_present") is False, "ACB-CAP-03 public_api_snapshot_before runtime_module_present must be false")
    _require(before_snapshot.get("runtime_public_symbols") == [], "ACB-CAP-03 public_api_snapshot_before runtime_public_symbols must be empty")
    _require(after_snapshot.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_snapshot_after phase_id mismatch")
    _require(after_snapshot.get("runtime_module_present") is True, "ACB-CAP-03 public_api_snapshot_after runtime_module_present must be true")
    _require(after_snapshot.get("runtime_public_symbols") == contract_data.get("public_symbols"), "ACB-CAP-03 public_api_snapshot_after runtime_public_symbols mismatch")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_change_report phase_id mismatch")
    _require(public_api_drift.get("root_removed_symbols") == [], "ACB-CAP-03 public_api_change_report root_removed_symbols must be empty")
    _require(public_api_drift.get("root_added_symbols") == [], "ACB-CAP-03 public_api_change_report root_added_symbols must be empty")
    _require(public_api_drift.get("runtime_module_added_as_submodule_only") is True, "ACB-CAP-03 public_api_change_report runtime_module_added_as_submodule_only must be true")
    _require(public_api_drift.get("delta_ratified") is True, "ACB-CAP-03 public_api_change_report delta_ratified must be true")

    _require(import_report.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 import_stability_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-03 import_stability_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable_or_ratified") is True, "ACB-CAP-03 import_stability_report public_api_stable_or_ratified must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-03 import_stability_report forbidden_runtime_patterns must be empty")

    for symbol in contract_data.get("public_symbols", []):
        _require(symbol in markdown_text, f"ACB-CAP-03 runtime_public_api.md missing public symbol: {symbol}")
    _require("## Blocked Modes" in markdown_text, "ACB-CAP-03 runtime_public_api.md must document blocked modes")
    _require("no production" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid production")
    _require("no external network" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid external network")
    _require("no real apply" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid real apply")

    _require("name: Runtime Public API" in workflow_text, "ACB-CAP-03 workflow must be Runtime Public API")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-03 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-03 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_03_runtime_public_api.py" in workflow_text, "ACB-CAP-03 workflow must run the runtime public API artifact validator")
    _require("tests/test_acb_cap_03_runtime_public_api.py -v" in workflow_text, "ACB-CAP-03 workflow must run runtime public API tests")


def _check_acb_cap_04_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_04_EVIDENCE_PATH.exists(), "missing ACB-CAP-04 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_04_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-04 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b6044982c31e0861b481605c40bef673b249f351",
        "ACB-CAP-04 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b1d175f8b0d1105a9d05f6ddcab082c71d6f6b3e",
        "ACB-CAP-04 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("product_pilot_boundary_ci", {}).get("conclusion") == "success",
        "ACB-CAP-04 evidence Product Pilot Boundary CI must be success",
    )
    _require(
        evidence_data.get("product_pilot_boundary_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26924199459",
        "ACB-CAP-04 evidence Product Pilot Boundary CI URL mismatch",
    )
    for key in [
        "product_boundary_package_exists",
        "pilot_gates_defined",
        "five_binary_gates_defined",
        "lab_to_staging_to_pilot_workflow_defined",
        "pilot_scope_contract_exists",
        "evidence_bundle_contract_exists",
        "pilot_runbook_contract_exists",
        "pilot_risk_matrix_exists",
        "non_authorization_statement_exists",
        "product_pilot_tests_exist",
        "product_pilot_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-04 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-04 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_gates_defined") is True,
        "ACB-CAP-04 evidence pilot_gates_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("five_binary_gates_defined") is True,
        "ACB-CAP-04 evidence five_binary_gates_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_scope_defined") is True,
        "ACB-CAP-04 evidence pilot_scope_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("evidence_bundle_contract_defined") is True,
        "ACB-CAP-04 evidence evidence_bundle_contract_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_allowed_now") is False,
        "ACB-CAP-04 evidence pilot_allowed_now must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("production_authorized") is False,
        "ACB-CAP-04 evidence production_authorized must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("product_promotion_allowed") is False,
        "ACB-CAP-04 evidence product_promotion_allowed must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("bedrock_required_before_product") is True,
        "ACB-CAP-04 evidence bedrock_required_before_product must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_04"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "product-pilot-boundary.yml",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "gate_registry.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "pilot_gate.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "workflow.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "evidence.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "decision.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "checklist.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "risk_matrix.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_04_product_pilot_boundary.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_04_product_pilot_boundary.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "product_pilot_boundary_contract.json",
        artifacts_root / "pilot_gate_registry.json",
        artifacts_root / "five_gate_decision_matrix.json",
        artifacts_root / "lab_to_staging_to_pilot_workflow.json",
        artifacts_root / "pilot_scope_contract.json",
        artifacts_root / "evidence_bundle_contract.json",
        artifacts_root / "pilot_runbook_contract.md",
        artifacts_root / "pilot_risk_matrix.json",
        artifacts_root / "non_authorization_statement.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-04 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "product_pilot_boundary_contract.json")
    gate_registry = _load_json(artifacts_root / "pilot_gate_registry.json")
    decision_matrix = _load_json(artifacts_root / "five_gate_decision_matrix.json")
    workflow_data = _load_json(artifacts_root / "lab_to_staging_to_pilot_workflow.json")
    pilot_scope = _load_json(artifacts_root / "pilot_scope_contract.json")
    evidence_contract = _load_json(artifacts_root / "evidence_bundle_contract.json")
    risk_matrix = _load_json(artifacts_root / "pilot_risk_matrix.json")
    non_authorization = _load_json(artifacts_root / "non_authorization_statement.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "product-pilot-boundary.yml").read_text(encoding="utf-8")
    runbook_text = (artifacts_root / "pilot_runbook_contract.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Product/Pilot Boundary Gate", "ACB-CAP-04 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_04_pass", "ACB-CAP-04 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-04 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-04 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-04 decision minimum_deliverable_met must be true")
    _require(decision_data.get("pilot_gates_defined") is True, "ACB-CAP-04 decision pilot_gates_defined must be true")
    _require(decision_data.get("five_binary_gates_defined") is True, "ACB-CAP-04 decision five_binary_gates_defined must be true")
    _require(decision_data.get("lab_to_staging_to_pilot_workflow_defined") is True, "ACB-CAP-04 decision workflow flag mismatch")
    _require(decision_data.get("pilot_scope_defined") is True, "ACB-CAP-04 decision pilot_scope_defined must be true")
    _require(decision_data.get("evidence_bundle_contract_defined") is True, "ACB-CAP-04 decision evidence_bundle_contract_defined must be true")
    _require(decision_data.get("pilot_runbook_contract_defined") is True, "ACB-CAP-04 decision pilot_runbook_contract_defined must be true")
    _require(decision_data.get("pilot_risk_matrix_defined") is True, "ACB-CAP-04 decision pilot_risk_matrix_defined must be true")
    _require(decision_data.get("pilot_allowed_now") is False, "ACB-CAP-04 decision pilot_allowed_now must be false")
    _require(decision_data.get("client_real_allowed_now") is False, "ACB-CAP-04 decision client_real_allowed_now must be false")
    _require(decision_data.get("production_authorized") is False, "ACB-CAP-04 decision production_authorized must be false")
    _require(decision_data.get("commercial_use_allowed") is False, "ACB-CAP-04 decision commercial_use_allowed must be false")
    _require(decision_data.get("pricing_allowed") is False, "ACB-CAP-04 decision pricing_allowed must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-04 decision product_promotion_allowed must be false")
    _require(decision_data.get("runtime_productive_activation") is False, "ACB-CAP-04 decision runtime_productive_activation must be false")
    _require(decision_data.get("bedrock_required_before_product") is True, "ACB-CAP-04 decision bedrock_required_before_product must be true")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-04 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-04 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_04_pass", "ACB-CAP-04 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-04 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-04 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_product_pilot_boundary_gate_only", "ACB-CAP-04 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "pilot_without_evidence_hashes", "ACB-CAP-04 research_basis rejected_pattern mismatch")
    _require(research_data.get("rejected_pattern_2") == "automatic_product_promotion", "ACB-CAP-04 research_basis rejected_pattern_2 mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 contract phase_id mismatch")
    _require(contract_data.get("module") == "aris.product_boundary", "ACB-CAP-04 contract module mismatch")
    _require(contract_data.get("gate_count") == 5, "ACB-CAP-04 contract gate_count mismatch")
    _require(contract_data.get("binary_outputs_only") is True, "ACB-CAP-04 contract binary_outputs_only must be true")
    _require(contract_data.get("workflow_stages") == ["LAB", "STAGING", "PILOT_CANDIDATE", "PILOT_APPROVED"], "ACB-CAP-04 contract workflow stages mismatch")
    invariants = contract_data.get("invariants", {})
    _require(invariants.get("pilot_allowed_now") is False, "ACB-CAP-04 contract pilot_allowed_now must be false")
    _require(invariants.get("client_real_allowed_now") is False, "ACB-CAP-04 contract client_real_allowed_now must be false")
    _require(invariants.get("production_authorized") is False, "ACB-CAP-04 contract production_authorized must be false")
    _require(invariants.get("commercial_use_allowed") is False, "ACB-CAP-04 contract commercial_use_allowed must be false")
    _require(invariants.get("pricing_allowed") is False, "ACB-CAP-04 contract pricing_allowed must be false")
    _require(invariants.get("product_promotion_allowed") is False, "ACB-CAP-04 contract product_promotion_allowed must be false")
    _require(invariants.get("runtime_productive_activation") is False, "ACB-CAP-04 contract runtime_productive_activation must be false")
    _require(invariants.get("bedrock_required_before_product") is True, "ACB-CAP-04 contract bedrock_required_before_product must be true")

    _require(gate_registry.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 pilot_gate_registry phase_id mismatch")
    _require(gate_registry.get("gate_count") == 5, "ACB-CAP-04 pilot_gate_registry gate_count mismatch")
    gates = gate_registry.get("gates", [])
    _require(len(gates) == 5, "ACB-CAP-04 pilot_gate_registry must contain exactly 5 gates")
    expected_gate_ids = [
        "LAB_EVIDENCE_GATE",
        "STAGING_READINESS_GATE",
        "SAFETY_BOUNDARY_GATE",
        "OPERATIONAL_SUPPORT_GATE",
        "PILOT_APPROVAL_GATE",
    ]
    _require([gate.get("gate_id") for gate in gates] == expected_gate_ids, "ACB-CAP-04 gate ids mismatch")
    for gate in gates:
        _require(gate.get("allowed_outputs") == ["pass", "fail"], f"ACB-CAP-04 gate {gate.get('gate_id')} allowed_outputs mismatch")
        _require(gate.get("decision") in {"pass", "fail"}, f"ACB-CAP-04 gate {gate.get('gate_id')} decision must be binary")
        _require(all(output not in {"pass", "fail"} for output in gate.get("forbidden_outputs", [])), f"ACB-CAP-04 gate {gate.get('gate_id')} forbidden outputs must exclude binary values")

    _require(decision_matrix.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 five_gate_decision_matrix phase_id mismatch")
    _require(decision_matrix.get("gate_count") == 5, "ACB-CAP-04 five_gate_decision_matrix gate_count mismatch")
    matrix_cases = decision_matrix.get("cases", {})
    for case_name in ["missing_evidence", "hashless_evidence", "complete_evidence"]:
        _require(len(matrix_cases.get(case_name, [])) == 5, f"ACB-CAP-04 decision matrix case {case_name} must contain 5 gates")
    _require(all(gate.get("decision") == "fail" for gate in matrix_cases.get("missing_evidence", [])), "ACB-CAP-04 missing_evidence case must fail every gate")
    _require(all(gate.get("decision") == "fail" for gate in matrix_cases.get("hashless_evidence", [])), "ACB-CAP-04 hashless_evidence case must fail every gate")
    _require(all(gate.get("decision") == "pass" for gate in matrix_cases.get("complete_evidence", [])), "ACB-CAP-04 complete_evidence case must pass every gate")

    _require(workflow_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 workflow phase_id mismatch")
    _require(workflow_data.get("stages") == ["LAB", "STAGING", "PILOT_CANDIDATE", "PILOT_APPROVED"], "ACB-CAP-04 workflow stages mismatch")
    evaluations = workflow_data.get("evaluations", {})
    _require(evaluations.get("blocked_by_gate", {}).get("current_stage") == "lab", "ACB-CAP-04 workflow blocked_by_gate stage mismatch")
    _require("binary_gate_fail" in evaluations.get("blocked_by_gate", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow blocked_by_gate reasons mismatch")
    _require(evaluations.get("blocked_by_prerequisite", {}).get("current_stage") == "staging", "ACB-CAP-04 workflow blocked_by_prerequisite stage mismatch")
    _require(evaluations.get("candidate_blocked_without_approval", {}).get("current_stage") == "pilot_candidate", "ACB-CAP-04 workflow candidate_blocked_without_approval stage mismatch")
    _require("client_approval_missing" in evaluations.get("candidate_blocked_without_approval", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow must block missing client approval")
    _require("commercial_terms_missing" in evaluations.get("candidate_blocked_without_approval", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow must block missing commercial terms")
    _require(evaluations.get("approval_still_blocked_in_phase_contract", {}).get("pilot_approved_allowed") is False, "ACB-CAP-04 workflow approval_still_blocked_in_phase_contract must not allow pilot")

    _require(pilot_scope.get("pilot_scope_defined") is True, "ACB-CAP-04 pilot_scope_contract pilot_scope_defined must be true")
    _require(pilot_scope.get("pilot_authorized") is False, "ACB-CAP-04 pilot_scope_contract pilot_authorized must be false")
    _require(pilot_scope.get("kill_switch_required") is True, "ACB-CAP-04 pilot_scope_contract kill_switch_required must be true")
    _require(pilot_scope.get("rollback_required") is True, "ACB-CAP-04 pilot_scope_contract rollback_required must be true")
    _require(pilot_scope.get("audit_ledger_required") is True, "ACB-CAP-04 pilot_scope_contract audit_ledger_required must be true")
    _require(pilot_scope.get("support_required") is True, "ACB-CAP-04 pilot_scope_contract support_required must be true")

    _require(evidence_contract.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 evidence_bundle_contract phase_id mismatch")
    _require(evidence_contract.get("hash_required_for_every_item") is True, "ACB-CAP-04 evidence_bundle_contract hash_required_for_every_item must be true")
    items = evidence_contract.get("items", [])
    _require(len(items) == 13, "ACB-CAP-04 evidence_bundle_contract must list 13 items")
    _require(all(item.get("hash_required") is True for item in items), "ACB-CAP-04 evidence_bundle_contract every item must require hash")

    _require(risk_matrix.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 pilot_risk_matrix phase_id mismatch")
    risks = risk_matrix.get("risks", [])
    risk_ids = {risk.get("risk_id") for risk in risks}
    _require("prompt_injection" in risk_ids, "ACB-CAP-04 risk matrix missing prompt_injection")
    _require("excessive_agency" in risk_ids, "ACB-CAP-04 risk matrix missing excessive_agency")
    _require("rollback_failure" in risk_ids, "ACB-CAP-04 risk matrix missing rollback_failure")
    _require("product_readiness_theater" in risk_ids, "ACB-CAP-04 risk matrix missing product_readiness_theater")

    _require(non_authorization.get("pilot_allowed_now") is False, "ACB-CAP-04 non_authorization_statement pilot_allowed_now must be false")
    _require(non_authorization.get("client_real_allowed_now") is False, "ACB-CAP-04 non_authorization_statement client_real_allowed_now must be false")
    _require(non_authorization.get("production_authorized") is False, "ACB-CAP-04 non_authorization_statement production_authorized must be false")
    _require(non_authorization.get("commercial_use_allowed") is False, "ACB-CAP-04 non_authorization_statement commercial_use_allowed must be false")
    _require(non_authorization.get("pricing_allowed") is False, "ACB-CAP-04 non_authorization_statement pricing_allowed must be false")
    _require(non_authorization.get("product_promotion_allowed") is False, "ACB-CAP-04 non_authorization_statement product_promotion_allowed must be false")
    _require(non_authorization.get("runtime_productive_activation") is False, "ACB-CAP-04 non_authorization_statement runtime_productive_activation must be false")
    _require(non_authorization.get("bedrock_required_before_product") is True, "ACB-CAP-04 non_authorization_statement bedrock_required_before_product must be true")
    _require(non_authorization.get("pilot_scope_defined") is True, "ACB-CAP-04 non_authorization_statement pilot_scope_defined must be true")
    _require(non_authorization.get("pilot_authorized") is False, "ACB-CAP-04 non_authorization_statement pilot_authorized must be false")

    _require(import_report.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 import_stability_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-04 import_stability_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable_or_ratified") is True, "ACB-CAP-04 import_stability_report public_api_stable_or_ratified must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-04 import_stability_report forbidden_runtime_patterns must be empty")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 public_api_drift_report phase_id mismatch")
    _require(public_api_drift.get("root_removed_symbols") == [], "ACB-CAP-04 public_api_drift_report root_removed_symbols must be empty")
    _require(public_api_drift.get("root_added_symbols") == [], "ACB-CAP-04 public_api_drift_report root_added_symbols must be empty")
    _require(public_api_drift.get("product_boundary_exposed_as_submodule_only") is True, "ACB-CAP-04 public_api_drift_report product_boundary_exposed_as_submodule_only must be true")
    _require(public_api_drift.get("delta_ratified") is True, "ACB-CAP-04 public_api_drift_report delta_ratified must be true")

    _require("does not authorize" in runbook_text.lower(), "ACB-CAP-04 pilot_runbook_contract must state that it does not authorize the pilot")
    _require("operator-only" in runbook_text.lower(), "ACB-CAP-04 pilot_runbook_contract must be operator-only")

    _require("name: Product Pilot Boundary" in workflow_text, "ACB-CAP-04 workflow must be Product Pilot Boundary")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-04 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-04 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_04_product_pilot_boundary.py" in workflow_text, "ACB-CAP-04 workflow must run the product pilot boundary artifact validator")
    _require("tests/test_acb_cap_04_product_pilot_boundary.py -v" in workflow_text, "ACB-CAP-04 workflow must run product pilot boundary tests")


def _check_acb_cap_05_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full", CURRENT_LIVE_PHASE_CLASS}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_05_EVIDENCE_PATH.exists(), "missing ACB-CAP-05 evidence artifact in active-context")
    _require(ACB_CAP_05_RESYNC_PATH.exists(), "missing ACB-CAP-05 resync artifact in active-context")

    evidence_data = _load_json(ACB_CAP_05_EVIDENCE_PATH)
    resync_data = _load_json(ACB_CAP_05_RESYNC_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-05 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA,
        "ACB-CAP-05 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_before_resync") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA,
        "ACB-CAP-05 evidence project_sha_before_resync mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b6044982c31e0861b481605c40bef673b249f351",
        "ACB-CAP-05 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("advanced_supply_chain_ci", {}).get("conclusion") == "success",
        "ACB-CAP-05 evidence Advanced Supply Chain CI must be success",
    )
    _require(
        evidence_data.get("advanced_supply_chain_ci", {}).get("url")
        == ACB_CAP_05_ADVANCED_SUPPLY_CHAIN_CI_URL,
        "ACB-CAP-05 evidence Advanced Supply Chain CI URL mismatch",
    )
    _require(resync_data.get("artifact_id") == "acb_cap_05_project_sha_resync_2026_06_06", "ACB-CAP-05 resync artifact_id mismatch")
    _require(resync_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 resync phase_id mismatch")
    _require(resync_data.get("repair_type") == "project_sha_evidence_resync", "ACB-CAP-05 resync repair_type mismatch")
    _require(resync_data.get("decision") == "pass", "ACB-CAP-05 resync decision mismatch")
    _require(resync_data.get("root_cause") == "ACB-CAP-05 decision project_sha mismatch", "ACB-CAP-05 resync root_cause mismatch")
    _require(resync_data.get("previous_project_sha") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA, "ACB-CAP-05 resync previous_project_sha mismatch")
    _require(resync_data.get("new_project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA, "ACB-CAP-05 resync new_project_sha mismatch")
    _require(resync_data.get("project_decision_artifact_sha") == ACB_CAP_05_PROJECT_DECISION_SHA, "ACB-CAP-05 resync project_decision_artifact_sha mismatch")
    _require(resync_data.get("diff_classification") == "ACB_VALIDATION_ONLY", "ACB-CAP-05 resync diff_classification mismatch")
    for key in [
        "inf_full_opened",
        "next_phase_authorized_by_operator",
        "runtime_mutation_authorized",
        "product_promotion_allowed",
        "pilot_authorized",
        "bedrock_executed",
        "secret_access_attempted",
    ]:
        _require(
            resync_data.get("safety", {}).get(key) is False,
            f"ACB-CAP-05 resync safety flag {key} must be false",
        )
    _require(
        evidence_data.get("resync", {}).get("reason") == "ACB-CAP-05 decision project_sha mismatch",
        "ACB-CAP-05 evidence resync reason mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("previous_project_sha") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA,
        "ACB-CAP-05 evidence resync previous_project_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("new_project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA,
        "ACB-CAP-05 evidence resync new_project_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("project_decision_artifact_sha") == ACB_CAP_05_PROJECT_DECISION_SHA,
        "ACB-CAP-05 evidence resync project_decision_artifact_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("operator_authorization_changed") is False,
        "ACB-CAP-05 evidence resync operator_authorization_changed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("inf_full_opened") is False,
        "ACB-CAP-05 evidence resync inf_full_opened must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("product_promotion_allowed") is False,
        "ACB-CAP-05 evidence resync product_promotion_allowed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("pilot_authorized") is False,
        "ACB-CAP-05 evidence resync pilot_authorized must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("bedrock_executed") is False,
        "ACB-CAP-05 evidence resync bedrock_executed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("runtime_mutation_authorized") is False,
        "ACB-CAP-05 evidence resync runtime_mutation_authorized must be false",
    )
    for key in [
        "supply_chain_package_exists",
        "sbom_integrity_checker_exists",
        "sbom_integrity_report_exists",
        "attestation_envelope_exists",
        "offline_signature_test_verification_exists",
        "pypi_vulnerability_range_monitor_exists",
        "pypi_vulnerability_range_scan_exists",
        "aibom_prototype_exists",
        "infernus_full_spec_exists",
        "advanced_supply_chain_tests_exist",
        "advanced_supply_chain_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-05 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-05 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("sbom_validation_passed") is True,
        "ACB-CAP-05 evidence sbom_validation_passed must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("attestation_verified") is True,
        "ACB-CAP-05 evidence attestation_verified must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("tamper_rejection_verified") is True,
        "ACB-CAP-05 evidence tamper_rejection_verified must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("infernus_spec_linked") is True,
        "ACB-CAP-05 evidence infernus_spec_linked must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("bot_coverage_complete") is True,
        "ACB-CAP-05 evidence bot_coverage_complete must be true",
    )
    for key in [
        "network_attempted",
        "external_pypi_query_attempted",
        "sigstore_runtime_used",
        "pypi_upload_attempted",
        "secret_access_attempted",
        "production_signature_claimed",
        "product_promotion_allowed",
        "bedrock_executed",
        "pilot_authorized",
    ]:
        _require(
            evidence_data.get("safety", {}).get(key) is False,
            f"ACB-CAP-05 evidence safety flag {key} must be false",
        )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_05"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "advanced_supply_chain.yml",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "sbom_integrity.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "attestation_envelope.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "pypi_vulnerability_range_monitor.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "aibom_prototype.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "advanced_supply_chain_gate.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_05_advanced_supply_chain_gate.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_05_advanced_supply_chain_gate.py",
        PROJECT_ROOT / "docs" / "infernus_full" / "infernus_full_execution_spec.md",
        artifacts_root / "sbom_integrity_report.json",
        artifacts_root / "attestation_envelope.json",
        artifacts_root / "pypi_vulnerability_range_scan.json",
        artifacts_root / "aibom_prototype.json",
        artifacts_root / "infernus_full_spec_linkage.json",
        artifacts_root / "advanced_supply_chain_decision.json",
        artifacts_root / "advanced_supply_chain_summary.json",
        artifacts_root / "advanced_supply_chain_report.md",
        artifacts_root / "pypi_vulnerability_ranges_fixture.json",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-05 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "advanced_supply_chain_decision.json")
    summary_data = _load_json(artifacts_root / "advanced_supply_chain_summary.json")
    sbom_report = _load_json(artifacts_root / "sbom_integrity_report.json")
    attestation_envelope = _load_json(artifacts_root / "attestation_envelope.json")
    vulnerability_scan = _load_json(artifacts_root / "pypi_vulnerability_range_scan.json")
    aibom_prototype = _load_json(artifacts_root / "aibom_prototype.json")
    spec_linkage = _load_json(artifacts_root / "infernus_full_spec_linkage.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "advanced_supply_chain.yml").read_text(encoding="utf-8")
    spec_text = (PROJECT_ROOT / "docs" / "infernus_full" / "infernus_full_execution_spec.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Advanced Supply Chain Gate", "ACB-CAP-05 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_05_pass", "ACB-CAP-05 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-05 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-05 decision pass_criteria_met must be true")
    _require(decision_data.get("sbom_validation_passed") is True, "ACB-CAP-05 decision sbom_validation_passed must be true")
    _require(decision_data.get("attestation_verified") is True, "ACB-CAP-05 decision attestation_verified must be true")
    _require(decision_data.get("tamper_rejection_verified") is True, "ACB-CAP-05 decision tamper_rejection_verified must be true")
    _require(decision_data.get("infernus_spec_linked") is True, "ACB-CAP-05 decision infernus_spec_linked must be true")
    _require(decision_data.get("forbidden_import_findings") == [], "ACB-CAP-05 decision forbidden_import_findings must be empty")
    for key in [
        "network_attempted",
        "external_pypi_query_attempted",
        "sigstore_runtime_used",
        "pypi_upload_attempted",
        "secret_access_attempted",
        "production_signature_claimed",
        "product_promotion_allowed",
        "pilot_authorized",
        "bedrock_executed",
        "infernus_full_opened",
    ]:
        _require(decision_data.get(key) is False, f"ACB-CAP-05 decision {key} must be false")
    _require(bool(decision_data.get("project_sha")), "ACB-CAP-05 decision project_sha must be non-empty")

    _require(summary_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 summary phase_id mismatch")
    _require(summary_data.get("offline_detection_count") == 1, "ACB-CAP-05 summary offline_detection_count mismatch")
    _require(summary_data.get("offline_unknown_count") == 15, "ACB-CAP-05 summary offline_unknown_count mismatch")
    _require(summary_data.get("forbidden_import_findings") == [], "ACB-CAP-05 summary forbidden_import_findings must be empty")
    _require(summary_data.get("tamper_rejection_verified") is True, "ACB-CAP-05 summary tamper_rejection_verified must be true")

    _require(sbom_report.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 sbom_integrity_report phase_id mismatch")
    _require(sbom_report.get("validation_passed") is True, "ACB-CAP-05 sbom_integrity_report validation_passed must be true")
    _require(sbom_report.get("complete_sbom_claimed") is False, "ACB-CAP-05 sbom_integrity_report complete_sbom_claimed must be false")
    _require(sbom_report.get("component_count") == 18, "ACB-CAP-05 sbom_integrity_report component_count mismatch")

    _require(attestation_envelope.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 attestation_envelope phase_id mismatch")
    _require(attestation_envelope.get("signature_mode") == "offline_test_hmac_not_production_signature", "ACB-CAP-05 attestation signature_mode mismatch")
    _require(attestation_envelope.get("production_signature_claimed") is False, "ACB-CAP-05 attestation production_signature_claimed must be false")
    _require(attestation_envelope.get("sigstore_runtime_used") is False, "ACB-CAP-05 attestation sigstore_runtime_used must be false")
    _require(attestation_envelope.get("pypi_upload_used") is False, "ACB-CAP-05 attestation pypi_upload_used must be false")
    _require(attestation_envelope.get("trusted_publishing_used") is False, "ACB-CAP-05 attestation trusted_publishing_used must be false")

    _require(vulnerability_scan.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 vulnerability scan phase_id mismatch")
    _require(vulnerability_scan.get("external_monitoring_allowed") is False, "ACB-CAP-05 vulnerability scan external_monitoring_allowed must be false")
    _require(len(vulnerability_scan.get("detected_by_offline_fixture", [])) == 1, "ACB-CAP-05 vulnerability scan must detect exactly 1 offline advisory")
    _require(len(vulnerability_scan.get("unknown_due_to_no_external_network", [])) == 15, "ACB-CAP-05 vulnerability scan unknown count mismatch")

    _require(aibom_prototype.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 aibom_prototype phase_id mismatch")
    _require(aibom_prototype.get("completeness") == "prototype_partial", "ACB-CAP-05 aibom_prototype completeness mismatch")
    _require(aibom_prototype.get("production_claim") is False, "ACB-CAP-05 aibom_prototype production_claim must be false")
    _require(aibom_prototype.get("spdx_conformance_claimed") is False, "ACB-CAP-05 aibom_prototype spdx_conformance_claimed must be false")
    _require(aibom_prototype.get("cyclonedx_conformance_claimed") is False, "ACB-CAP-05 aibom_prototype cyclonedx_conformance_claimed must be false")

    _require(spec_linkage.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 infernus_full_spec_linkage phase_id mismatch")
    _require(spec_linkage.get("all_required_sections_present") is True, "ACB-CAP-05 infernus_full_spec_linkage all_required_sections_present must be true")
    _require(spec_linkage.get("documented_bot_count") == 13, "ACB-CAP-05 infernus_full_spec_linkage documented_bot_count mismatch")
    _require(spec_linkage.get("bot_coverage_complete") is True, "ACB-CAP-05 infernus_full_spec_linkage bot_coverage_complete must be true")
    _require(spec_linkage.get("operator_only_open_gate") is True, "ACB-CAP-05 infernus_full_spec_linkage operator_only_open_gate must be true")
    _require(spec_linkage.get("product_or_pilot_authorized") is False, "ACB-CAP-05 infernus_full_spec_linkage product_or_pilot_authorized must be false")

    _require("name: Advanced Supply Chain" in workflow_text, "ACB-CAP-05 workflow must be Advanced Supply Chain")
    _require("python -m py_compile" in workflow_text, "ACB-CAP-05 workflow must run py_compile")
    _require("python -m unittest tests.test_acb_cap_05_advanced_supply_chain_gate -q" in workflow_text, "ACB-CAP-05 workflow must run focused unittest")
    _require("python scripts/run_acb_cap_05_advanced_supply_chain_gate.py" in workflow_text, "ACB-CAP-05 workflow must run the advanced supply chain runner")
    _require("python -m json.tool artifacts/acb_cap_05/advanced_supply_chain_decision.json" in workflow_text, "ACB-CAP-05 workflow must validate generated JSON artifacts")

    _require("## 13 Bots" in spec_text, "ACB-CAP-05 infernus spec must include 13 bots section")
    _require(
        "operator explicitly opens" in spec_text.lower() or "explicit operator authorization" in spec_text.lower(),
        "ACB-CAP-05 infernus spec must be operator-gated",
    )
    _require("must not authorize product rollout" in spec_text.lower(), "ACB-CAP-05 infernus spec must prohibit product rollout")


def _check_inf_full_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(
        state.get("phase_class") in {"infernus_full", CURRENT_LIVE_PHASE_CLASS},
        "phase_class must remain compatible with infernus_full lineage",
    )

    required_paths = [
        INF_FULL_01_SCOPE_DECISION_PATH,
        INF_FULL_01_SCOPE_MATRIX_PATH,
        INF_FULL_01_SCOPE_MANIFEST_PATH,
        INF_FULL_01_SCOPE_CHARTER_PATH,
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if not external_project_available:
        return
    for path in required_paths:
        _require(path.exists(), f"missing INF-FULL-01 scope artifact: {path.relative_to(PROJECT_ROOT)}")

    decision_data = _load_json(INF_FULL_01_SCOPE_DECISION_PATH)
    matrix_data = _load_json(INF_FULL_01_SCOPE_MATRIX_PATH)
    manifest_data = _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH)
    charter_text = INF_FULL_01_SCOPE_CHARTER_PATH.read_text(encoding="utf-8")

    _require(
        decision_data == {
            "artifact_id": "inf_full_01_scope_charter_decision_2026_06_06",
            "phase_id": "INF-FULL-01",
            "phase_name": "ARIS Infernus Full Scope Charter Gate",
            "artifact_type": "operator_authorized_scope_charter",
            "decision": "pass",
            "status": "inf_full_01_scope_charter_pass",
            "operator_authorized": True,
            "authorization_scope": "open_inf_full_01_scope_charter_only",
            "bots_executed": False,
            "runtime_execution_authorized": False,
            "product_promotion_allowed": False,
            "pilot_authorized": False,
            "bedrock_executed": False,
            "secret_access_authorized": False,
            "network_execution_authorized": False,
            "initial_scope_rule": "uncertain_modules_included_to_avoid_false_negative",
            "safe_to_execute_bots_now": False,
            "next_execution_requires_separate_gate": True,
            "scope_counts": {
                "acb_core": 5,
                "ativo_critico": 5,
                "incerto_included": 16,
                "secondary": 13,
                "quarantine_with_hash": 2,
            },
            "inf_full_opened": True,
            "next_phase": None,
            "next_phase_authorized_by_operator": False,
        },
        "INF-FULL-01 scope decision artifact mismatch",
    )

    expected_bucket_map = {
        "backend": "acb_core",
        "mcp_runtime": "acb_core",
        "runtime": "acb_core",
        "product_boundary": "acb_core",
        "supply_chain": "acb_core",
        "actions": "ativo_critico",
        "app": "ativo_critico",
        "config": "ativo_critico",
        "logging": "ativo_critico",
        "security": "ativo_critico",
        "action_runtime": "incerto_included",
        "action_runtime_contracts": "incerto_included",
        "audio": "incerto_included",
        "bedrock": "incerto_included",
        "capabilities": "incerto_included",
        "context": "incerto_included",
        "evaluation": "incerto_included",
        "intelligence": "incerto_included",
        "knowledge": "incerto_included",
        "lab": "incerto_included",
        "memory": "incerto_included",
        "persona": "incerto_included",
        "response": "incerto_included",
        "turn": "incerto_included",
        "ui": "incerto_included",
        "voice": "incerto_included",
        "cockpit": "secondary",
        "hardening_base": "secondary",
        "intents": "secondary",
        "lab_simulation": "secondary",
        "learning": "secondary",
        "model_gateway": "secondary",
        "product_loop": "secondary",
        "research": "secondary",
        "response_quality": "secondary",
        "rich_output": "secondary",
        "roadmap": "secondary",
        "sandbox": "secondary",
        "understanding": "secondary",
        "diagnostics": "quarantine_with_hash",
        "packaging": "quarantine_with_hash",
    }

    matrix_modules = matrix_data.get("modules", [])
    _require(matrix_data.get("artifact_id") == "inf_full_01_scope_matrix_2026_06_06", "INF-FULL-01 scope matrix artifact_id mismatch")
    _require(matrix_data.get("phase_id") == "INF-FULL-01", "INF-FULL-01 scope matrix phase_id mismatch")
    _require(
        matrix_data.get("scope_rule") == "uncertain_modules_included_to_avoid_false_negative",
        "INF-FULL-01 scope matrix scope_rule mismatch",
    )
    _require(len(matrix_modules) == len(expected_bucket_map), "INF-FULL-01 scope matrix module count mismatch")

    seen_modules = set()
    for item in matrix_modules:
        module = item.get("module")
        bucket = item.get("bucket")
        _require(module in expected_bucket_map, f"unexpected module in INF-FULL-01 scope matrix: {module}")
        _require(bucket == expected_bucket_map[module], f"bucket mismatch for module {module}")
        _require(isinstance(item.get("reason"), str) and item["reason"], f"missing reason for module {module}")
        _require(isinstance(item.get("risk_if_excluded"), str) and item["risk_if_excluded"], f"missing risk_if_excluded for module {module}")
        _require(isinstance(item.get("source_diagnostic_status"), str) and item["source_diagnostic_status"], f"missing source_diagnostic_status for module {module}")
        if bucket in {"acb_core", "ativo_critico", "incerto_included"}:
            _require(item.get("include_in_initial_infernus_scope") is True, f"{module} must be in initial scope")
            _require(item.get("attack_required") is True, f"{module} must require attack coverage")
            _require(item.get("include_in_secondary_scope") is False, f"{module} must not be marked as secondary")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        elif bucket == "secondary":
            _require(item.get("include_in_initial_infernus_scope") is False, f"{module} must not be in initial scope")
            _require(item.get("include_in_secondary_scope") is True, f"{module} must be in secondary scope")
            _require(item.get("attack_required") is False, f"{module} must not require initial attack")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        else:
            _require(item.get("include_in_initial_infernus_scope") is False, f"{module} must not be in initial scope")
            _require(item.get("include_in_secondary_scope") is False, f"{module} must not be in secondary scope")
            _require(item.get("attack_required") is False, f"{module} must not require initial attack")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        seen_modules.add(module)
    _require(seen_modules == set(expected_bucket_map), "INF-FULL-01 scope matrix module set mismatch")

    _require(
        manifest_data == {
            "artifact_id": "inf_full_01_module_scope_manifest_2026_06_06",
            "phase_id": "INF-FULL-01",
            "initial_attack_scope_modules": [
                "backend", "mcp_runtime", "runtime", "product_boundary", "supply_chain",
                "actions", "app", "config", "logging", "security",
                "action_runtime", "action_runtime_contracts", "audio", "bedrock", "capabilities",
                "context", "evaluation", "intelligence", "knowledge", "lab", "memory",
                "persona", "response", "turn", "ui", "voice",
            ],
            "secondary_scope_modules": [
                "cockpit", "hardening_base", "intents", "lab_simulation", "learning",
                "model_gateway", "product_loop", "research", "response_quality",
                "rich_output", "roadmap", "sandbox", "understanding",
            ],
            "quarantine_hash_only_modules": [
                "diagnostics", "packaging",
            ],
            "all_modules_accounted_for": True,
            "unresolved_modules": [],
            "false_negative_policy": "include_uncertain_modules_in_initial_scope",
            "baseline_freeze_requirements": {
                "all_scoped_modules_require_hashes": True,
                "quarantine_modules_require_hashes": True,
                "baseline_freeze_must_precede_attack_waves": True,
            },
            "handoff_policy": {
                "next_gate": "INF-FULL-02 Baseline Freeze Planning",
                "bots_executed": False,
                "runtime_execution_authorized": False,
                "operator_reauthorization_required_for_execution": True,
            },
            "bots_executed": False,
            "runtime_execution_authorized": False,
        },
        "INF-FULL-01 scope manifest mismatch",
    )

    for phrase in [
        "# INF-FULL-01 Scope Charter",
        "PASS — INF-FULL-01 scope charter is opened by operator authorization.",
        "This opens scope/charter only.",
        "No bots are executed.",
        "No runtime is started.",
        "Uncertain included:",
        "diagnostics, packaging.",
        "INF-FULL-02 must be Baseline Freeze Planning.",
    ]:
        _require(phrase in charter_text, f"INF-FULL-01 scope charter missing phrase: {phrase}")

    _require(state.get("current_phase_bots_executed") is False, "current_phase_bots_executed must be false")


def _check_inf_full_02_project_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_02_DECISION_PATH)
    inventory_data = _load_json(INF_FULL_02_INVENTORY_PATH)
    hash_manifest = _load_json(INF_FULL_02_HASH_MANIFEST_PATH)
    summary_data = _load_json(INF_FULL_02_SUMMARY_PATH)
    planning_text = INF_FULL_02_PLANNING_DOC_PATH.read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == INF_FULL_02_PHASE, "INF-FULL-02 decision phase_name mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-FULL-01", "INF-FULL-02 previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "INF-FULL-02 decision must be pass")
    _require(decision_data.get("status") == INF_FULL_02_STATUS, "INF-FULL-02 decision status mismatch")
    _require(decision_data.get("operator_authorization_source") == "chat_operator_said_vamos_continuar_2026_06_06", "INF-FULL-02 operator authorization source mismatch")
    _require(decision_data.get("baseline_freeze_planned") is True, "INF-FULL-02 baseline_freeze_planned must be true")
    _require(decision_data.get("baseline_freeze_applied") is False, "INF-FULL-02 baseline_freeze_applied must be false")
    _require(decision_data.get("bot_execution_allowed") is False, "INF-FULL-02 bot_execution_allowed must be false")
    _require(decision_data.get("bot_execution_executed") is False, "INF-FULL-02 bot_execution_executed must be false")
    _require(decision_data.get("runtime_execution_authorized") is False, "INF-FULL-02 runtime_execution_authorized must be false")
    _require(decision_data.get("product_ready") is False, "INF-FULL-02 product_ready must be false")
    _require(decision_data.get("bedrock_execution_authorized") is False, "INF-FULL-02 bedrock_execution_authorized must be false")
    _require(decision_data.get("external_network_authorized") is False, "INF-FULL-02 external_network_authorized must be false")
    _require(decision_data.get("secrets_access_authorized") is False, "INF-FULL-02 secrets_access_authorized must be false")
    _require(decision_data.get("minimum_deliverable_met") is True, "INF-FULL-02 minimum_deliverable_met must be true")
    _require(decision_data.get("next_phase") is None, "INF-FULL-02 next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "INF-FULL-02 next_phase_authorized_by_operator must be false")

    _require(inventory_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 inventory phase_id mismatch")
    _require(inventory_data.get("phase_name") == INF_FULL_02_PHASE, "INF-FULL-02 inventory phase_name mismatch")
    _require(inventory_data.get("classification_labels") == [
        "active_baseline_candidate",
        "historical_only",
        "quarantine_hash_only",
        "excluded_with_reason",
        "missing_expected_blocking",
    ], "INF-FULL-02 classification labels mismatch")
    _require(len(inventory_data.get("module_inventory", [])) == 41, "INF-FULL-02 module inventory count mismatch")
    quarantine = {
        item.get("module")
        for item in inventory_data.get("module_inventory", [])
        if item.get("classification") == "quarantine_hash_only"
    }
    _require(quarantine == {"diagnostics", "packaging"}, "INF-FULL-02 quarantine module set mismatch")
    _require(len(inventory_data.get("scenario_inventory", [])) == 13, "INF-FULL-02 scenario inventory count mismatch")
    _require(inventory_data.get("inventory_counts", {}).get("historical_only") == 3, "INF-FULL-02 historical count mismatch")
    _require(inventory_data.get("blocking_inventory", [{}])[0].get("classification") == "missing_expected_blocking", "INF-FULL-02 blocking inventory mismatch")

    _require(hash_manifest.get("phase_id") == "INF-FULL-02", "INF-FULL-02 hash manifest phase_id mismatch")
    _require(hash_manifest.get("hash_algorithm") == "sha256", "INF-FULL-02 hash algorithm mismatch")
    _require(hash_manifest.get("directory_hash_algorithm") == 'sha256(sorted("relative_path:file_sha256"))', "INF-FULL-02 directory hash algorithm mismatch")
    ref_paths = {entry.get("path") for entry in hash_manifest.get("reference_hashes", [])}
    for required_path in [
        "aris-active-context/ACTIVE_CONTEXT_STATE.json",
        "aris-active-context/ROADMAP_CANONICAL.md",
        "artifacts/infernus/inf_full_02_baseline_freeze_planning_decision_2026_06_06.json",
        "artifacts/infernus/inf_full_02_baseline_freeze_inventory_2026_06_06.json",
        "artifacts/infernus/inf_full_02_baseline_freeze_summary_2026_06_06.json",
        "docs/infernus_full/inf_full_02_baseline_freeze_planning_2026_06_06.md",
        "aris-active-context/artifacts/inf_bot_01/nemesis_execution_log.json",
        "aris-active-context/artifacts/inf_minos_01/minos_verdict.json",
        "aris-active-context/artifacts/purg_01/finding_nemesis_validator_bypass.json",
        "src/aris/diagnostics",
        "src/aris/packaging",
    ]:
        _require(required_path in ref_paths, f"INF-FULL-02 hash manifest missing path: {required_path}")
    _require(len(hash_manifest.get("reference_hashes", [])) >= 60, "INF-FULL-02 hash manifest is too small")

    _require(summary_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-02 summary decision mismatch")
    _require(summary_data.get("status") == INF_FULL_02_STATUS, "INF-FULL-02 summary status mismatch")
    _require(summary_data.get("question_6_next_phase_after_inf_full_02", {}).get("canonical_next_phase") is None, "INF-FULL-02 summary canonical_next_phase must be null")

    for phrase in [
        "baseline_freeze_planned: `true`",
        "baseline_freeze_applied: `false`",
        "No canonical successor is currently defined for INF-FULL-02 in ROADMAP_CANONICAL.md.",
        "Historical-only reference set:",
        "Quarantine hash-only modules:",
    ]:
        _require(phrase in planning_text, f"INF-FULL-02 planning doc missing phrase: {phrase}")


def _check_inf_full_03_project_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_03_DECISION_PATH)
    summary_data = _load_json(INF_FULL_03_SUMMARY_PATH)
    transition_data = _load_json(IF00_TRANSITION_CANDIDATE_PATH)
    hermeticity_data = _load_json(IF00_HERMETICITY_PATH)
    ontology_data = _load_json(IF02_ONTOLOGY_PATH)
    oracle_data = _load_json(IF03_ORACLE_PACK_PATH)
    bot_pack_data = _load_json(IF04_BOT_PACK_PATH)
    permission_data = _load_json(IF04_PERMISSION_PATH)
    docs_readme_text = INFERNUS_FULL_DOCS_README_PATH.read_text(encoding="utf-8")
    opening_text = INF_FULL_03_OPENING_DOC_PATH.read_text(encoding="utf-8")
    historical_canonroadmap_path = (
        INFERNUS_CANONROADMAP_FORENSIC_PATH
        if INFERNUS_CANONROADMAP_FORENSIC_PATH.exists()
        else INFERNUS_FULL_CANONROADMAP_PATH
    )
    canonroadmap_text = historical_canonroadmap_path.read_text(encoding="utf-8")
    ledger_lines = [line for line in IF01_LEDGER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    coverage_lines = [line for line in IF02_COVERAGE_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]

    _require(decision_data.get("phase_id") == "INF-FULL-03", "INF-FULL-03 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == INF_FULL_03_PHASE, "INF-FULL-03 decision phase_name mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-FULL-02", "INF-FULL-03 decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "INF-FULL-03 decision must be pass")
    _require(decision_data.get("status") == INF_FULL_03_STATUS, "INF-FULL-03 decision status mismatch")
    _require(decision_data.get("operator_authorization_source") == "chat_operator_said_ok_autorizo_td_infernus_full_2026_06_06", "INF-FULL-03 operator authorization source mismatch")
    _require(decision_data.get("full_infernus_chain_registered") is True, "INF-FULL-03 full_infernus_chain_registered must be true")
    _require(decision_data.get("canon_roadmap_persisted") is True, "INF-FULL-03 canon_roadmap_persisted must be true")
    _require(decision_data.get("baseline_freeze_dependency_satisfied") is True, "INF-FULL-03 baseline_freeze_dependency_satisfied must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "INF-FULL-03 minimum_deliverable_met must be true")
    _require(decision_data.get("bot_execution_allowed") is False, "INF-FULL-03 bot_execution_allowed must be false")
    _require(decision_data.get("bot_execution_executed") is False, "INF-FULL-03 bot_execution_executed must be false")
    _require(decision_data.get("runtime_execution_authorized") is False, "INF-FULL-03 runtime_execution_authorized must be false")
    _require(decision_data.get("product_ready") is False, "INF-FULL-03 product_ready must be false")
    _require(decision_data.get("bedrock_execution_authorized") is False, "INF-FULL-03 bedrock_execution_authorized must be false")
    _require(decision_data.get("external_network_authorized") is False, "INF-FULL-03 external_network_authorized must be false")
    _require(decision_data.get("secrets_access_authorized") is False, "INF-FULL-03 secrets_access_authorized must be false")
    _require(decision_data.get("dependency_change_authorized") is False, "INF-FULL-03 dependency_change_authorized must be false")
    _require(decision_data.get("next_phase") is None, "INF-FULL-03 next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "INF-FULL-03 next_phase_authorized_by_operator must be false")
    _require(len(decision_data.get("registered_chain_stages", [])) == 11, "INF-FULL-03 registered_chain_stages count mismatch")

    _require(summary_data.get("phase_id") == "INF-FULL-03", "INF-FULL-03 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-03 summary decision mismatch")
    _require(summary_data.get("status") == INF_FULL_03_STATUS, "INF-FULL-03 summary status mismatch")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("full_chain_registered") is True, "INF-FULL-03 summary must mark full_chain_registered")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("inf_full_03_opened") is True, "INF-FULL-03 summary must mark inf_full_03_opened")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("bot_execution_authorized_now") is False, "INF-FULL-03 summary bot_execution_authorized_now must be false")
    _require(summary_data.get("next_phase_after_inf_full_03", {}).get("canonical_next_phase") is None, "INF-FULL-03 summary canonical_next_phase must be null")

    _require(transition_data.get("phase_id") == "INF-FULL-03", "if00 transition candidate phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("from_phase_id") == "INF-FULL-02", "if00 transition candidate from_phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("to_phase_id") == "INF-FULL-03", "if00 transition candidate to_phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("advance_mode") == "operator", "if00 transition candidate advance_mode mismatch")
    _require(transition_data.get("bot_execution_authorized") is False, "if00 transition candidate bot_execution_authorized must be false")
    _require(transition_data.get("runtime_authorized") is False, "if00 transition candidate runtime_authorized must be false")

    _require(hermeticity_data.get("phase_id") == "INF-FULL-03", "if00 hermeticity phase_id mismatch")
    _require(hermeticity_data.get("decision") == "pass", "if00 hermeticity decision mismatch")
    _require(hermeticity_data.get("hermeticity_contract", {}).get("lab_runtime_started") is False, "if00 hermeticity lab_runtime_started must be false")
    _require(hermeticity_data.get("hermeticity_contract", {}).get("bots_may_run") is False, "if00 hermeticity bots_may_run must be false")
    _require(hermeticity_data.get("baseline_freeze_dependency", {}).get("baseline_freeze_planned") is True, "if00 hermeticity baseline_freeze_planned must be true")
    _require(hermeticity_data.get("baseline_freeze_dependency", {}).get("baseline_freeze_applied") is False, "if00 hermeticity baseline_freeze_applied must be false")

    _require(len(ledger_lines) >= 5, "if01 evidence ledger must contain at least 5 claims")
    _require(all(json.loads(line).get("accepted_for_inf_full_03") is True for line in ledger_lines), "if01 evidence ledger claims must all be accepted_for_inf_full_03")
    _require(any(json.loads(line).get("topic") == "transition_candidate" for line in ledger_lines), "if01 evidence ledger must contain transition_candidate")

    _require(ontology_data.get("phase_id") == "INF-FULL-03", "if02 ontology phase_id mismatch")
    _require(ontology_data.get("ontology_version") == "v4", "if02 ontology version mismatch")
    _require(ontology_data.get("planning_only") is True, "if02 ontology planning_only must be true")
    _require(len(ontology_data.get("threat_families", [])) == 8, "if02 ontology threat family count mismatch")

    _require(len(coverage_lines) >= 2, "if02 coverage matrix must contain header and rows")
    _require(coverage_lines[0] == "threat_id,threat_name,seed_bots,seed_artifacts,evidence_required,inf_full_03_status", "if02 coverage matrix header mismatch")
    _require(any("conditional_planning_only" in line for line in coverage_lines[1:]), "if02 coverage matrix must include conditional_planning_only row")

    _require(oracle_data.get("phase_id") == "INF-FULL-03", "if03 oracle pack phase_id mismatch")
    _require(oracle_data.get("planning_only") is True, "if03 oracle pack planning_only must be true")
    _require(oracle_data.get("global_oracle_rules", {}).get("deterministic_oracles_required") is True, "if03 oracle pack deterministic_oracles_required must be true")
    _require(len(oracle_data.get("metrics_contracts", [])) >= 7, "if03 oracle pack metrics_contracts count mismatch")

    _require(bot_pack_data.get("phase_id") == "INF-FULL-03", "if04 bot pack phase_id mismatch")
    _require(bot_pack_data.get("planning_only") is True, "if04 bot pack planning_only must be true")
    _require(bot_pack_data.get("bot_count_canonical") == 15, "if04 bot pack bot_count_canonical mismatch")
    _require(bot_pack_data.get("bot_count_conditional") == 1, "if04 bot pack bot_count_conditional mismatch")
    _require(any(bot.get("name") == "Minos" and bot.get("contract_status") == "registered_as_auditor_only" for bot in bot_pack_data.get("bots", [])), "if04 bot pack must register Minos as auditor only")

    _require(permission_data.get("phase_id") == "INF-FULL-03", "if04 permission manifest phase_id mismatch")
    _require(permission_data.get("planning_only") is True, "if04 permission manifest planning_only must be true")
    _require(permission_data.get("capability_guards", {}).get("bot_execution_allowed") is False, "if04 permission manifest bot_execution_allowed must be false")
    _require(permission_data.get("capability_guards", {}).get("runtime_execution_allowed") is False, "if04 permission manifest runtime_execution_allowed must be false")
    _require("execute bots" in permission_data.get("forbidden_capabilities", []), "if04 permission manifest must forbid bot execution")

    for phrase in [
        "# INF-FULL-03 Chain Registration & Preparation Opening",
        "Decision: `pass`",
        "The full planned chain is recorded as:",
        "Only `INF-FULL-03` is opened canonically here.",
        "No bot execution.",
        "No runtime start.",
        "No Bedrock execution.",
    ]:
        _require(phrase in opening_text, f"INF-FULL-03 opening doc missing phrase: {phrase}")

    for phrase in [
        "INF-FULL-02 | pass",
        "→ INF-FULL-03 | infernus_full | operator",
        "if00_transition_candidate.json",
        "if04_permission_manifest_v4.json",
        "## INF-FULL-03 não deve incluir",
        "- execution;",
        "- Bedrock;",
        "- product;",
        "- secrets;",
        "- package install;",
    ]:
        _require(phrase in canonroadmap_text, f"infernus_full_canonroadmap.md missing phrase: {phrase}")

    _require(INFERNUS_FULL_SUPERSESSION_PATH.exists(), "missing infernus_full canonroadmap supersession artifact")
    _require("docs/infernus_full/infernus_full_canonroadmap.md" in docs_readme_text, "docs/infernus_full/README.md must point to infernus_full_canonroadmap.md")
    _require("inf_full_03_opening_2026_06_06.md" in docs_readme_text, "docs/infernus_full/README.md must reference INF-FULL-03 opening doc")


def _check_inf_full_04_project_artifacts(state: dict[str, Any]) -> None:
    standing_auth = _load_json(INF_FULL_OPERATOR_STANDING_AUTH_PATH)
    scenario_manifest = _load_json(IF05_SCENARIO_PACK_PATH)
    controls_design = _load_json(IF05_CONTROLS_DESIGN_PATH)
    oracle_mapping = _load_json(IF05_ORACLE_MAPPING_PATH)
    mutation_registry = _load_json(IF05_MUTATION_REGISTRY_PATH)
    harness_decision = _load_json(IF06_HARNESS_READINESS_PATH)
    sandbox_contract = _load_json(IF06_SANDBOX_CONTRACT_PATH)
    cost_quota = _load_json(IF06_COST_QUOTA_PATH)
    replay_policy = _load_json(IF06_REPLAY_POLICY_PATH)
    kill_switch = _load_json(IF06_KILL_SWITCH_PATH)
    decision_data = _load_json(INF_FULL_04_DECISION_PATH)
    summary_data = _load_json(INF_FULL_04_SUMMARY_PATH)
    docs_readme_text = INFERNUS_FULL_DOCS_README_PATH.read_text(encoding="utf-8")
    doc_text = INF_FULL_04_DOC_PATH.read_text(encoding="utf-8")

    _require(standing_auth.get("artifact_id") == "inf_full_operator_standing_authorization_policy_2026_06_06", "standing auth artifact_id mismatch")
    _require(standing_auth.get("operator_statement") == "ok, autorizo td infernus full", "standing auth operator_statement mismatch")
    _require(standing_auth.get("standing_authorization_scope") == "infernus_full_pre_execution_gated_sequence", "standing auth scope mismatch")
    _require(standing_auth.get("authorizes_pre_execution_gates_without_reasking_operator") is True, "standing auth must allow pre-execution gates")
    _require(standing_auth.get("authorizes_transition_table_updates_for_pre_execution_sequence") is True, "standing auth must allow pre-execution Transition Table updates")
    for key in [
        "authorizes_bot_execution",
        "authorizes_runtime_execution",
        "authorizes_attack_waves",
        "authorizes_real_dry_run",
        "authorizes_real_apply",
        "authorizes_product_promotion",
        "authorizes_bedrock_execution",
        "authorizes_secret_access",
        "authorizes_dependency_installation",
    ]:
        _require(standing_auth.get(key) is False, f"standing auth {key} must be false")

    _require(scenario_manifest.get("phase_id") == "INF-FULL-04", "if05 scenario manifest phase_id mismatch")
    _require(scenario_manifest.get("decision") == "pass", "if05 scenario manifest decision mismatch")
    _require(scenario_manifest.get("planning_only") is True, "if05 scenario manifest planning_only must be true")
    _require(scenario_manifest.get("total_bots_covered") == 16, "if05 scenario manifest total_bots_covered mismatch")
    _require(scenario_manifest.get("total_scenarios_planned") == 16, "if05 scenario manifest total_scenarios_planned mismatch")
    _require(scenario_manifest.get("waves_covered") == ["W-1", "W0", "W0.5", "W1", "W2", "W3", "W4", "W5", "W6"], "if05 scenario manifest waves_covered mismatch")
    scenarios = scenario_manifest.get("scenarios", [])
    _require(len(scenarios) == 16, "if05 scenario manifest scenarios count mismatch")
    bot_ids = {scenario.get("bot_id") for scenario in scenarios}
    _require(bot_ids == {"Quimera", "Dubio", "Elos", "Taipan", "Labirinto", "Vitium", "Gula", "Apep", "Patrono", "Efeso", "Abzu", "Loop", "Minos", "Quiron", "Gorgona", "Sirene"}, "if05 scenario manifest bot coverage mismatch")
    critical_adaptive = {"Quimera", "Taipan", "Abzu", "Loop", "Minos", "Vitium", "Patrono", "Gorgona"}
    for scenario in scenarios:
        _require(isinstance(scenario.get("fixture_refs"), list) and scenario.get("fixture_refs"), f"{scenario.get('scenario_id')} missing fixture_refs")
        _require(scenario.get("positive_control", {}).get("present") is True, f"{scenario.get('scenario_id')} positive_control missing")
        _require(scenario.get("negative_control", {}).get("present") is True, f"{scenario.get('scenario_id')} negative_control missing")
        if scenario.get("bot_id") in critical_adaptive:
            _require(scenario.get("adaptive_variant", {}).get("present") is True, f"{scenario.get('scenario_id')} adaptive_variant must be true for critical bot")
    sirene = next((scenario for scenario in scenarios if scenario.get("bot_id") == "Sirene"), None)
    _require(sirene is not None, "if05 scenario manifest must include Sirene")
    _require("conditional_disabled_unless_voice_active" in sirene.get("adaptive_variant", {}).get("description", ""), "Sirene must remain conditional_disabled_unless_voice_active")

    _require(controls_design.get("phase_id") == "INF-FULL-04", "if05 controls design phase_id mismatch")
    _require(controls_design.get("decision") == "pass", "if05 controls design decision mismatch")
    _require(controls_design.get("scenario_count_planned") == 16, "if05 controls design scenario_count_planned mismatch")
    _require(controls_design.get("critical_bot_requirements", {}).get("positive_control_required") is True, "if05 controls design positive_control_required must be true")
    _require("exfiltration mutation" in controls_design.get("control_catalog", {}).get("mutation_variants", []), "if05 controls design missing exfiltration mutation")
    _require("contains real PII or secret material" in controls_design.get("invalid_scenario_criteria", []), "if05 controls design missing PII invalid criterion")

    _require(oracle_mapping.get("phase_id") == "INF-FULL-04", "if05 oracle mapping phase_id mismatch")
    _require(oracle_mapping.get("mapping_count") == 16, "if05 oracle mapping count mismatch")
    mappings = oracle_mapping.get("mappings", [])
    _require(len(mappings) == 16, "if05 oracle mapping rows mismatch")
    _require(all(mapping.get("llm_text_output_allowed_as_sole_oracle") is False for mapping in mappings), "if05 oracle mapping must forbid LLM-only oracle")
    _require({mapping.get("scenario_id") for mapping in mappings} == {scenario.get("scenario_id") for scenario in scenarios}, "if05 oracle mapping scenario_id set mismatch")

    _require(mutation_registry.get("phase_id") == "INF-FULL-04", "if05 mutation registry phase_id mismatch")
    _require(mutation_registry.get("family_count") == 10, "if05 mutation registry family_count mismatch")
    _require(all(family.get("execution_now") is False for family in mutation_registry.get("families", [])), "if05 mutation registry families must all be non-executable")

    _require(harness_decision.get("artifact_id") == "if06_harness_readiness_decision", "if06 harness artifact_id mismatch")
    _require(harness_decision.get("phase_id") == "INF-FULL-04", "if06 harness phase_id mismatch")
    _require(harness_decision.get("readiness_scope") == "future_simulation_only", "if06 harness readiness_scope mismatch")
    _require(harness_decision.get("ready_for_inf_full_05_dry_run_evidence_simulation") is True, "if06 harness ready_for_inf_full_05_dry_run_evidence_simulation must be true")
    for key in ["bot_execution_allowed", "runtime_execution_allowed", "real_dry_run_allowed", "real_apply_allowed"]:
        _require(harness_decision.get(key) is False, f"if06 harness {key} must be false")

    _require(sandbox_contract.get("phase_id") == "INF-FULL-04", "if06 sandbox phase_id mismatch")
    _require(sandbox_contract.get("network_policy", {}).get("allowed_scope") == "github_active_context_governance_only", "if06 sandbox network scope mismatch")
    _require(sandbox_contract.get("process_policy", {}).get("runtime_start_allowed") is False, "if06 sandbox runtime_start_allowed must be false")
    _require(sandbox_contract.get("secret_access_policy", {}).get("allowed") is False, "if06 sandbox secret access must be false")

    _require(cost_quota.get("phase_id") == "INF-FULL-04", "if06 cost quota phase_id mismatch")
    _require(cost_quota.get("per_bot_limits", {}).get("Gula", {}).get("max_cost_units") == 6, "if06 cost quota Gula max_cost_units mismatch")
    _require(cost_quota.get("per_wave_limits", {}).get("W6", {}).get("max_retry_count") == 0, "if06 cost quota W6 max_retry_count mismatch")

    _require(replay_policy.get("phase_id") == "INF-FULL-04", "if06 replay policy phase_id mismatch")
    _require(replay_policy.get("execution_now") is False, "if06 replay policy execution_now must be false")
    _require(replay_policy.get("input_hash", {}).get("algorithm") == "sha256", "if06 replay policy input hash algorithm mismatch")

    _require(kill_switch.get("phase_id") == "INF-FULL-04", "if06 kill switch phase_id mismatch")
    _require(len(kill_switch.get("triggers", [])) == 7, "if06 kill switch triggers count mismatch")
    _require(any(trigger.get("trigger_id") == "KS-COST" for trigger in kill_switch.get("triggers", [])), "if06 kill switch must include KS-COST")

    _require(decision_data.get("phase_id") == "INF-FULL-04", "INF-FULL-04 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == INF_FULL_04_DECISION_PHASE_NAME, "INF-FULL-04 decision phase_name mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-FULL-03", "INF-FULL-04 decision previous_phase_id mismatch")
    _require(decision_data.get("status") == INF_FULL_04_STATUS, "INF-FULL-04 decision status mismatch")
    _require(decision_data.get("minimum_deliverable_met") is True, "INF-FULL-04 decision minimum_deliverable_met must be true")
    for key in [
        "bot_execution_allowed",
        "current_phase_bots_executed",
        "runtime_execution_authorized",
        "real_dry_run_authorized",
        "real_apply_authorized",
        "bedrock_authorized",
        "product_authorized",
        "secrets_access_authorized",
        "dependency_installation_authorized",
    ]:
        _require(decision_data.get(key) is False, f"INF-FULL-04 decision {key} must be false")
    _require(decision_data.get("next_phase") is None, "INF-FULL-04 decision next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "INF-FULL-04 decision next_phase_authorized_by_operator must be false")

    _require(summary_data.get("phase_id") == "INF-FULL-04", "INF-FULL-04 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-04 summary decision mismatch")
    _require(summary_data.get("status") == INF_FULL_04_STATUS, "INF-FULL-04 summary status mismatch")
    _require(summary_data.get("total_bots_covered") == 16, "INF-FULL-04 summary total_bots_covered mismatch")
    _require(summary_data.get("total_scenarios_planned") == 16, "INF-FULL-04 summary total_scenarios_planned mismatch")
    _require(len(summary_data.get("mutation_families_created", [])) == 10, "INF-FULL-04 summary mutation_families_created count mismatch")
    _require(summary_data.get("locks_preserved", {}).get("bot_execution_allowed") is False, "INF-FULL-04 summary bot_execution_allowed lock mismatch")

    for phrase in [
        "# INF-FULL-04 Scenario Pack & Harness Readiness Gate",
        "This gate is pre-execution only.",
        "Total bots covered: `16`",
        "Total scenarios planned: `16`",
        "First bot execution still requires separate explicit authorization.",
        "Probable next step if later formalized: `INF-FULL-05 Dry-Run Evidence Simulation Gate`.",
    ]:
        _require(phrase in doc_text, f"INF-FULL-04 doc missing phrase: {phrase}")

    _require("inf_full_04_scenario_pack_harness_readiness_2026_06_06.md" in docs_readme_text, "docs/infernus_full/README.md must reference INF-FULL-04 doc")
    _require("if06_harness_readiness_decision.json" in docs_readme_text, "docs/infernus_full/README.md must reference IF06 harness decision")


def _check_inf_full_route_sync_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_ROUTE_SYNC_DECISION_PATH)
    summary_data = _load_json(INF_FULL_ROUTE_SYNC_SUMMARY_PATH)
    report_text = INF_FULL_ROUTE_SYNC_REPORT_PATH.read_text(encoding="utf-8")
    workspace_text = INF_FULL_ROUTE_SYNC_WORKSPACE_PATH.read_text(encoding="utf-8")
    transition_row = _get_transition_row(ROUTE_SYNC_SOURCE_PHASE_ID, "pass")
    _require(transition_row is not None, "missing INF-FULL-04/pass Transition Table row")

    _require(decision_data.get("phase_id") == "INF-FULL-04-ROUTE-SYNC", "route sync decision phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "route sync decision must be pass")
    _require(decision_data.get("status") == "inf_full_04_route_sync_to_05_pass", "route sync decision status mismatch")
    _require(decision_data.get("repair_type") == "route_sync", "route sync decision repair_type mismatch")
    _require(decision_data.get("source_phase") == ROUTE_SYNC_SOURCE_PHASE_ID, "route sync decision source_phase mismatch")
    _require(decision_data.get("derived_next_phase") == ROUTE_SYNC_DERIVED_NEXT_PHASE_ID, "route sync decision derived_next_phase mismatch")
    _require(decision_data.get("transition_table_updated") is True, "route sync decision transition_table_updated must be true")
    _require(decision_data.get("active_context_next_phase_updated") is True, "route sync decision active_context_next_phase_updated must be true")
    _require(decision_data.get("markdown_mirrors_updated") is True, "route sync decision markdown_mirrors_updated must be true")
    _require(decision_data.get("validator_updated") is True, "route sync decision validator_updated must be true")
    _require(decision_data.get("scenario_count_ambiguity_resolved") is True, "route sync decision scenario_count_ambiguity_resolved must be true")
    for key in [
        "execution_authorized",
        "bot_execution_authorized",
        "runtime_execution_authorized",
        "real_dry_run_authorized",
        "real_apply_authorized",
        "product_promotion_authorized",
        "pilot_authorized",
        "bedrock_authorized",
        "secrets_access_authorized",
        "dependency_mutation_authorized",
    ]:
        _require(decision_data.get(key) is False, f"route sync decision {key} must be false")

    _require(summary_data.get("source_phase") == ROUTE_SYNC_SOURCE_PHASE_ID, "route sync summary source_phase mismatch")
    _require(summary_data.get("derived_next_phase") == ROUTE_SYNC_DERIVED_NEXT_PHASE_ID, "route sync summary derived_next_phase mismatch")
    _require(summary_data.get("derived_next_phase_name") == ROUTE_SYNC_DERIVED_NEXT_PHASE_NAME, "route sync summary derived_next_phase_name mismatch")
    _require(summary_data.get("source_block_id") == "IF-07", "route sync summary source_block_id mismatch")
    _require(summary_data.get("source_block_name") == "Pre-Execution Review Gate", "route sync summary source_block_name mismatch")
    _require(summary_data.get("advance_mode") == ROUTE_SYNC_DERIVED_NEXT_PHASE_ADVANCE_MODE, "route sync summary advance_mode mismatch")
    _require(summary_data.get("scenario_count_historical") == 13, "route sync summary scenario_count_historical mismatch")
    _require(summary_data.get("planned_scenario_count") == 16, "route sync summary planned_scenario_count mismatch")
    _require(summary_data.get("planned_bot_count") == 16, "route sync summary planned_bot_count mismatch")
    _require(summary_data.get("mutation_family_count") == 10, "route sync summary mutation_family_count mismatch")
    _require(summary_data.get("oracle_count") == 9, "route sync summary oracle_count mismatch")
    _require(summary_data.get("execution_authorization") is False, "route sync summary execution_authorization must be false")
    _require(summary_data.get("route_sync_fix_applied") is True, "route sync summary route_sync_fix_applied must be true")

    for phrase in [
        "# INF-FULL-04 Route Sync Repair",
        "Derived next phase: `INF-FULL-05`",
        "Source block in saved canonroadmap: `IF-07 — Pre-Execution Review Gate`",
        "This repair does not authorize bot execution, runtime execution, dry-run real, or apply real.",
    ]:
        _require(phrase in report_text, f"route sync report missing phrase: {phrase}")

    for phrase in [
        "BEFORE: Project_ARIS git status --short",
        "BEFORE: aris-active-context git status --short",
        "AFTER: Project_ARIS git status --short",
        "AFTER: aris-active-context git status --short",
    ]:
        _require(phrase in workspace_text, f"workspace hygiene snapshot missing phrase: {phrase}")

    _require(
        transition_row["minimum_deliverable"] == "if07 pre-execution review decision artifact + no bot/runtime execution attestation + scenario-count normalization evidence + validator evidence",
        "Transition Table minimum deliverable mismatch for INF-FULL-05",
    )


def _check_inf_full_05_project_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(IF07_DECISION_PATH)
    no_execution = _load_json(IF07_NO_EXECUTION_PATH)
    normalization = _load_json(IF07_SCENARIO_NORMALIZATION_PATH)
    validator_evidence = _load_json(IF07_VALIDATOR_EVIDENCE_PATH)
    summary_data = _load_json(INF_FULL_05_SUMMARY_PATH)
    report_text = INF_FULL_05_REPORT_PATH.read_text(encoding="utf-8")
    doc_text = INF_FULL_05_DOC_PATH.read_text(encoding="utf-8")
    docs_readme_text = INFERNUS_FULL_DOCS_README_PATH.read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "INF-FULL-05", "IF07 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == INF_FULL_05_DECISION_PHASE_NAME, "IF07 decision phase_name mismatch")
    _require(decision_data.get("status") == "inf_full_05_pre_execution_review_gate_pass", "IF07 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "IF07 decision decision mismatch")
    _require(decision_data.get("review_only") is True, "IF07 decision review_only must be true")
    _require(decision_data.get("pre_execution_only") is True, "IF07 decision pre_execution_only must be true")
    _require(decision_data.get("minimum_deliverable_satisfied") is True, "IF07 decision minimum_deliverable_satisfied must be true")
    _require(decision_data.get("historical_dry_run_naming_drift_interpreted_as_authorization") is False, "IF07 decision naming-drift interpretation must be false")
    _require(decision_data.get("next_phase_from_transition_table") is None, "IF07 decision next_phase_from_transition_table must be null")
    _require(decision_data.get("next_phase_invented") is False, "IF07 decision next_phase_invented must be false")

    for key in [
        "current_phase_bots_executed",
        "bot_execution_authorized",
        "runtime_execution_authorized",
        "real_dry_run_authorized",
        "real_apply_authorized",
        "product_promotion_authorized",
        "pilot_authorized",
        "bedrock_authorized",
        "secrets_access_authorized",
        "dependency_mutation_authorized",
    ]:
        _require(decision_data.get(key) is False, f"IF07 decision {key} must be false")

    for key in [
        "bot_execution_attempted",
        "runtime_execution_attempted",
        "real_dry_run_attempted",
        "real_apply_attempted",
        "bedrock_attempted",
        "product_promotion_attempted",
        "pilot_attempted",
        "secrets_access_attempted",
        "dependency_installation_attempted",
        "network_use_outside_github_governance_attempted",
        "fixture_mutation_attempted",
        "backend_frontend_runtime_audio_mutation_attempted",
    ]:
        _require(no_execution.get(key) is False, f"IF07 no-execution {key} must be false")
    _require(
        no_execution.get("evidence_basis") == ["git diff scoped files", "grep checks", "validation commands", "active-context locks"],
        "IF07 no-execution evidence_basis mismatch",
    )

    _require(normalization.get("scenario_count") == 13, "IF07 normalization scenario_count mismatch")
    _require(normalization.get("fixture_scenario_count") == 13, "IF07 normalization fixture_scenario_count mismatch")
    _require(normalization.get("current_phase_planned_scenario_count") == 16, "IF07 normalization planned scenario count mismatch")
    _require(normalization.get("current_phase_planned_bot_count") == 16, "IF07 normalization planned bot count mismatch")
    _require(normalization.get("current_phase_mutation_family_count") == 10, "IF07 normalization mutation family count mismatch")
    _require(normalization.get("current_phase_oracle_count") == 9, "IF07 normalization oracle count mismatch")
    _require(normalization.get("if06_naming_drift", {}).get("interpreted_as_execution_authorization") is False, "IF07 normalization naming drift mismatch")

    _require(validator_evidence.get("python_files_changed") is True, "IF07 validator evidence python_files_changed must be true")
    _require(validator_evidence.get("new_tests_required") is True, "IF07 validator evidence new_tests_required must be true")
    _require(validator_evidence.get("ci_reference", {}).get("project_aris_head_before") == "dcedffed590ce47d6251cd284a6d431a97fe08e2", "IF07 validator evidence project SHA before mismatch")
    _require(validator_evidence.get("ci_reference", {}).get("active_context_head_before") == "ef95a5f8610f02c6c51d5fcb4d59920bd37cf0ef", "IF07 validator evidence active-context SHA before mismatch")

    _require(summary_data.get("phase_id") == "INF-FULL-05", "INF-FULL-05 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-05 summary decision mismatch")
    _require(summary_data.get("status") == "inf_full_05_pre_execution_review_gate_pass", "INF-FULL-05 summary status mismatch")
    _require(summary_data.get("minimum_deliverable_satisfied") is True, "INF-FULL-05 summary minimum deliverable mismatch")
    _require(summary_data.get("next_phase") is None, "INF-FULL-05 summary next_phase must be null")

    for phrase in [
        "# INF-FULL-05 — Pre-Execution Review Gate",
        "## Decision",
        "## Scope",
        "## Canonical Input State",
        "## Minimum Deliverable Satisfaction",
        "## No-Execution Attestation",
        "## Scenario Count Normalization",
        "## IF06 Naming Drift Handling",
        "## Validator Evidence",
        "## CI Evidence",
        "## Safety Locks Preserved",
        "## Active-Context Update",
        "## Next Phase Handling",
        "No successor is emitted unless `ROADMAP_CANONICAL.md` contains an explicit `INF-FULL-05` transition row.",
    ]:
        _require(phrase in report_text, f"INF-FULL-05 report missing phrase: {phrase}")
        _require(phrase in doc_text, f"INF-FULL-05 doc missing phrase: {phrase}")

    _require("inf_full_05_pre_execution_review_2026_06_06.md" in docs_readme_text, "docs/infernus_full/README.md must reference INF-FULL-05 doc")
    _require("if07_pre_execution_review_decision_2026_06_06.json" in docs_readme_text, "docs/infernus_full/README.md must reference IF07 decision")
    _require("inf_full_05_pre_execution_review_report_2026_06_06.md" in docs_readme_text, "docs/infernus_full/README.md must reference INF-FULL-05 report")


def _check_inf_full_07_if08_authorization_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_07_IF08_DECISION_PATH)
    successor_data = _load_json(INF_FULL_07_IF08_SUCCESSOR_MATRIX_PATH)
    no_execution = _load_json(INF_FULL_07_IF08_NO_EXECUTION_PATH)
    validator_evidence = _load_json(INF_FULL_07_IF08_VALIDATOR_EVIDENCE_PATH)
    summary_data = _load_json(INF_FULL_07_IF08_SUMMARY_PATH)
    report_text = INF_FULL_07_IF08_REPORT_PATH.read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "INF-FULL-07", "IF08 authorization decision phase_id mismatch")
    _require(
        decision_data.get("phase_name") == "IF-08 Attack Waves Execution Authorization Gate Materialization",
        "IF08 authorization phase_name mismatch",
    )
    _require(decision_data.get("decision") == "pass", "IF08 authorization decision must be pass")
    _require(decision_data.get("status") == "inf_full_07_if08_authorization_gate_pass", "IF08 authorization status mismatch")
    _require(decision_data.get("source_phase_id") == "INF-FULL-06", "IF08 authorization source_phase_id mismatch")
    _require(
        decision_data.get("source_phase_status") == "inf_full_06_excludent_quarantine_gate_pass",
        "IF08 authorization source_phase_status mismatch",
    )
    _require(decision_data.get("mapped_infernus_block") == "IF-08", "IF08 authorization block mismatch")
    _require(decision_data.get("mapped_infernus_block_name") == "Attack Waves Execution", "IF08 authorization block name mismatch")
    _require(decision_data.get("canonroadmap_successor_confirmed") is True, "IF08 authorization canonroadmap_successor_confirmed must be true")
    _require(decision_data.get("canonroadmap_successor") == "IF-08", "IF08 authorization canonroadmap successor mismatch")
    _require(decision_data.get("transition_table_duplicate_resolved") is True, "transition_table_duplicate_resolved must be true")
    _require(
        decision_data.get("old_duplicate_row_classification") == "superseded_by_inf_full_06_to_inf_full_07_authorization_route",
        "old duplicate row classification mismatch",
    )
    _require(decision_data.get("excludent_policy_enforced") is True, "excludent policy enforcement mismatch")
    _require(decision_data.get("excludent_read_by_default_allowed") is False, "excludent_read_by_default_allowed must be false")
    _require(decision_data.get("only_canonroadmap_visible_as_active") is True, "only_canonroadmap_visible_as_active must be true")
    _require(decision_data.get("f21_route_used") is False, "IF08 authorization f21_route_used must be false")
    _require(
        decision_data.get("f21_route_classification") == "excludent_or_historical_residual_route_noise",
        "IF08 authorization f21 classification mismatch",
    )
    _require(decision_data.get("execution_authorized_in_this_phase") is False, "execution_authorized_in_this_phase must be false")
    _require(decision_data.get("if08_executed") is False, "IF08 authorization if08_executed must be false")
    _require(decision_data.get("waves_executed") == [], "IF08 authorization waves_executed must be empty")
    _require(decision_data.get("minimum_deliverable_satisfied") is True, "minimum_deliverable_satisfied must be true")
    for key in [
        "if08_execution_authorized",
        "waves_execution_authorized",
        "bot_execution_authorized",
        "runtime_execution_authorized",
        "real_dry_run_authorized",
        "real_apply_authorized",
        "product_promotion_authorized",
        "pilot_authorized",
        "bedrock_authorized",
        "secrets_access_authorized",
        "dependency_mutation_authorized",
    ]:
        _require(decision_data.get(key) is False, f"IF08 authorization decision {key} must be false")

    _require(successor_data.get("source_phase") == "INF-FULL-06", "successor matrix source_phase mismatch")
    _require(successor_data.get("source_phase_passed") is True, "source_phase_passed must be true")
    _require(
        successor_data.get("source_phase_status") == "inf_full_06_excludent_quarantine_gate_pass",
        "successor matrix source phase status mismatch",
    )
    _require(successor_data.get("active_next_phase_before") is None, "active_next_phase_before must be null")
    _require(successor_data.get("next_phase_before") is None, "next_phase_before must be null")
    _require(successor_data.get("excludent_created") is True, "excludent_created must be true")
    _require(successor_data.get("excludent_read_by_default_allowed") is False, "successor matrix excludent_read_by_default_allowed must be false")
    _require(successor_data.get("only_canonroadmap_visible_as_active") is True, "only_canonroadmap_visible_as_active must be true")
    _require(
        successor_data.get("canonroadmap_file") == "project_mirror/docs/infernus_full/infernus_full_canonroadmap.md",
        "successor matrix canonroadmap_file mismatch",
    )
    _require(successor_data.get("canonroadmap_next_block_after_if07") == "IF-08", "canonroadmap_next_block_after_if07 mismatch")
    _require(successor_data.get("if08_name") == "Attack Waves Execution", "if08_name mismatch")
    _require(successor_data.get("if08_zone") == "execution_future", "if08_zone mismatch")
    _require(successor_data.get("if08_type") == "EXECUTION", "if08_type mismatch")
    _require(successor_data.get("if08_operator_authorization_required") is True, "if08_operator_authorization_required mismatch")
    _require(successor_data.get("if08_transition_table_entry_required") is True, "if08_transition_table_entry_required mismatch")
    _require(successor_data.get("if08_runtime_allowed") == "only_if_authorized", "if08_runtime_allowed mismatch")
    _require(successor_data.get("if08_bot_execution_allowed") == "only_if_authorized", "if08_bot_execution_allowed mismatch")
    _require(
        successor_data.get("safe_current_gate") == "INF-FULL-07 — IF-08 Attack Waves Execution Authorization Gate Materialization",
        "safe_current_gate mismatch",
    )
    _require(successor_data.get("if08_execution_allowed_now") is False, "if08_execution_allowed_now must be false")
    _require(successor_data.get("waves_execution_allowed_now") is False, "waves_execution_allowed_now must be false")
    _require(successor_data.get("f21_route_valid_for_current_infernus_flow") is False, "f21_route_valid_for_current_infernus_flow must be false")
    _require(successor_data.get("transition_table_duplicate_before") is True, "transition_table_duplicate_before must be true")
    _require(successor_data.get("transition_table_duplicate_after") is False, "transition_table_duplicate_after must be false")
    _require(
        successor_data.get("verdict") == "valid_successor_requires_authorization_gate",
        "successor matrix verdict mismatch",
    )

    inf_full_05_rows = [
        row for row in _parse_transition_table()
        if row["current_phase_id"] == "INF-FULL-05" and row["decision"] == "pass"
    ]
    _require(len(inf_full_05_rows) == 1, "Transition Table must contain exactly one active INF-FULL-05 -> INF-FULL-06 row")
    _require(
        inf_full_05_rows[0]["next_phase_class"] == "infernus_full_excludent_cleanup",
        "INF-FULL-05 active row must remain infernus_full_excludent_cleanup",
    )
    inf_full_06_row = _get_transition_row("INF-FULL-06", "pass")
    _require(inf_full_06_row is not None, "INF-FULL-06 -> INF-FULL-07 row missing")
    _require(inf_full_06_row["next_phase_id"] == "INF-FULL-07", "INF-FULL-06 row next_phase_id mismatch")
    _require(
        inf_full_06_row["next_phase_class"] == "infernus_full_execution_authorization",
        "INF-FULL-06 row next_phase_class mismatch",
    )
    _require(inf_full_06_row["advance_mode"] == "canonroadmap", "INF-FULL-06 row advance_mode mismatch")

    _require(no_execution.get("phase_id") == "INF-FULL-07", "IF08 no-execution phase_id mismatch")
    for key in [
        "if08_execution_attempted",
        "waves_execution_attempted",
        "bot_execution_attempted",
        "runtime_execution_attempted",
        "real_dry_run_attempted",
        "real_apply_attempted",
        "bedrock_attempted",
        "product_promotion_attempted",
        "pilot_attempted",
        "secrets_access_attempted",
        "dependency_installation_attempted",
        "network_use_outside_github_governance_attempted",
        "excludent_read_as_context_attempted",
    ]:
        _require(no_execution.get(key) is False, f"IF08 no-execution {key} must be false")

    _require(validator_evidence.get("phase_id") == "INF-FULL-07", "validator evidence phase_id mismatch")
    for key in [
        "json_tool_passed",
        "active_context_validator_passed",
        "assert_mirror_sync_passed",
        "py_compile_passed",
        "pytest_passed",
        "ci_green_confirmed",
        "excludent_read_rule_validated",
        "safety_grep_passed",
    ]:
        _require(validator_evidence.get(key) is True, f"validator evidence {key} must be true")
    for key in [
        "project_aris_head",
        "project_aris_origin_main",
        "active_context_head",
        "active_context_origin_main",
    ]:
        _require(isinstance(validator_evidence.get(key), str), f"validator evidence {key} must be a string")

    _require(summary_data.get("phase_id") == "INF-FULL-07", "IF08 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "IF08 summary decision mismatch")
    _require(summary_data.get("status") == "inf_full_07_if08_authorization_gate_pass", "IF08 summary status mismatch")
    _require(summary_data.get("source_phase_id") == "INF-FULL-06", "IF08 summary source_phase_id mismatch")
    _require(summary_data.get("mapped_infernus_block") == "IF-08", "IF08 summary mapped_infernus_block mismatch")
    _require(summary_data.get("transition_duplicate_resolved") is True, "IF08 summary transition_duplicate_resolved mismatch")
    _require(summary_data.get("active_context_updated") is True, "IF08 summary active_context_updated must be true")
    _require(summary_data.get("markdown_mirrors_updated") is True, "IF08 summary markdown_mirrors_updated must be true")
    _require(summary_data.get("execution_authorization") is False, "IF08 summary execution_authorization must be false")
    _require(summary_data.get("next_phase_after") is None, "IF08 summary next_phase_after must be null")

    for phrase in [
        "# INF-FULL-07 — IF-08 Attack Waves Execution Authorization Gate Materialization",
        "## Decision",
        "## Canonical Input",
        "## Transition Table Duplicate Resolution",
        "## Excludent Enforcement",
        "## IF-08 Mapping Validation",
        "## Authorization Scope",
        "## No-Execution Attestation",
        "## Validator Evidence",
        "## CI Evidence",
        "## Safety Locks",
        "## Active-Context Update",
        "## Next Phase Handling",
    ]:
        _require(phrase in report_text, f"IF08 authorization report missing phrase: {phrase}")


def _check_inf_full_06_excludent_quarantine_artifacts(state: dict[str, Any]) -> None:
    """INF-FULL-06: verify excludent quarantine gate artifacts."""
    decision_path = _resolve_project_relative("artifacts", "infernus", "inf_full_06_excludent_quarantine_decision_2026_06_06.json")
    inventory_path = _resolve_project_relative("artifacts", "infernus", "inf_full_06_excludent_inventory_2026_06_06.json")
    manifest_path = _resolve_project_relative("artifacts", "infernus", "inf_full_06_excludent_move_manifest_2026_06_06.json")
    summary_path = _resolve_project_relative("artifacts", "infernus", "inf_full_06_excludent_quarantine_summary_2026_06_06.json")
    report_path = _resolve_project_relative("artifacts", "infernus", "inf_full_06_excludent_quarantine_report_2026_06_06.md")
    artifact_pack_present = all(
        path.exists()
        for path in [decision_path, inventory_path, manifest_path, summary_path, report_path]
    )

    if artifact_pack_present:
        decision_data = _load_json(decision_path)
        _require(decision_data.get("phase_id") == "INF-FULL-06", "excludent decision phase_id mismatch")
        _require(decision_data.get("decision") == "pass", "excludent decision must be pass")
        _require(decision_data.get("status") == "inf_full_06_excludent_quarantine_gate_pass", "excludent decision status mismatch")
        _require(decision_data.get("excludent_created") is True, "excludent_created must be true")
        _require(decision_data.get("excludent_policy_created") is True, "excludent_policy_created must be true")
        _require(decision_data.get("excludent_read_by_default_allowed") is False, "excludent_read_by_default_allowed must be false")
        for key in [
            "if08_execution_authorized",
            "waves_execution_authorized",
            "bot_execution_authorized",
            "runtime_execution_authorized",
            "real_dry_run_authorized",
            "real_apply_authorized",
            "product_promotion_authorized",
            "pilot_authorized",
            "bedrock_authorized",
            "secrets_access_authorized",
            "dependency_mutation_authorized",
        ]:
            _require(decision_data.get(key) is False, f"excludent decision {key} must be false")

        manifest_data = _load_json(manifest_path)
        _require(
            manifest_data.get("active_canonical_roadmap", {}).get("path") == "docs/infernus_full/infernus_full_canonroadmap.md",
            "manifest active_canonical_roadmap path mismatch",
        )
        _require(len(manifest_data.get("moved_to_excludent", [])) >= 2, "manifest must record at least 2 files moved to excludent")
        _require(manifest_data.get("delete_policy") == "physical_delete_not_allowed_without_hash_manifest", "manifest delete policy mismatch")

    # Verify excludent dir exists in active-context
    excludent_dir = ROOT / "excludent"
    _require(excludent_dir.exists(), "excludent/ directory must exist in active-context repo")
    excludent_policy = ROOT / "EXCLUDENT_POLICY.md"
    _require(excludent_policy.exists(), "EXCLUDENT_POLICY.md must exist in active-context repo")

    # Verify ARIS_BOOT.md has excludent rule (MANDATORY_READ_FIRST_RULES.md superseded by ARIS_BOOT.md)
    aris_boot = (ROOT / "ARIS_BOOT.md").read_text(encoding="utf-8")
    _require("excludent" in aris_boot, "ARIS_BOOT.md must contain excludent rule")
    _require("excluded_from_context" in aris_boot or "Arquivos em excludent/" in aris_boot, "ARIS_BOOT.md must describe excludent policy")


def _check_scenario_count_resolution(state: dict[str, Any]) -> None:
    _require(state.get("scenario_count") == 13, "scenario_count must preserve historical fixture value 13")
    _require(state.get("fixture_scenario_count") == 13, "fixture_scenario_count must be 13")
    _require(state.get("current_phase_planned_scenario_count") == 16, "current_phase_planned_scenario_count must be 16")
    _require(state.get("current_phase_planned_bot_count") == 16, "current_phase_planned_bot_count must be 16")
    _require(state.get("current_phase_mutation_family_count") == 10, "current_phase_mutation_family_count must be 10")
    _require(state.get("current_phase_oracle_count") == 9, "current_phase_oracle_count must be 9")


def _check_fixture_materialization(state: dict[str, Any]) -> None:
    """INF-MAT-01 specific: verify fixture count and evidence_ref hashes."""
    fixture_count = state.get("fixture_count", 0)
    scenario_count = state.get("scenario_count", 0)
    fixture_scenario_count = state.get("fixture_scenario_count", 0)
    _require(fixture_count == 65, f"fixture_count must be 65, got {fixture_count}")
    _require(scenario_count == 13, f"scenario_count must be 13, got {scenario_count}")
    _require(fixture_scenario_count == 13, f"fixture_scenario_count must be 13, got {fixture_scenario_count}")
    _require(state.get("fixture_materialization_executed") is True, "fixture_materialization_executed must be true")
    _require(state.get("governance_gate_streak") == 0, "governance_gate_streak must be 0 after capacity gate pass")

    root = ROOT / "fixtures/lab_simulation/aris_infernus_lab_full"
    _require(root.exists(), "fixtures/lab_simulation/aris_infernus_lab_full must exist")
    dirs = [d for d in root.iterdir() if d.is_dir()]
    _require(len(dirs) >= 13, f"expected >= 13 scenario dirs, found {len(dirs)}")

    null_hashes = []
    for ref_path in sorted(root.rglob("evidence_ref.json")):
        data = json.loads(ref_path.read_text(encoding="utf-8"))
        if data.get("hash") is None:
            null_hashes.append(ref_path.parent.name)
    if null_hashes:
        print(f"BLOCK: evidence_ref.json with null hash in: {null_hashes}")
        sys.exit(1)


def _check_bot_execution_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("bot_execution_executed") is True, "bot_execution_executed must be true")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must be 1")

    artifacts_root = ROOT / "artifacts/inf_bot_01"
    _require(artifacts_root.exists(), "artifacts/inf_bot_01 must exist")

    log_paths = sorted(artifacts_root.glob("*execution_log.json"))
    _require(len(log_paths) == 1, f"expected exactly 1 bot execution log, found {len(log_paths)}")
    log_path = log_paths[0]
    _require(log_path.name == "nemesis_execution_log.json", "unexpected bot execution log filename")

    log_data = _load_json(log_path)
    _require(log_data.get("bot_id") == "nemesis", "bot_id must be nemesis")
    _require(log_data.get("scenario_id") == "scenario_11_nemesis", "scenario_id must be scenario_11_nemesis")
    _require(log_data.get("mode") == "synthetic_deterministic_execution", "mode must be synthetic_deterministic_execution")
    _require(log_data.get("runtime_execution") is False, "runtime_execution must be false")
    _require(log_data.get("autonomous_execution") is False, "autonomous_execution must be false")
    _require(log_data.get("network_used") is False, "network_used must be false")
    _require(log_data.get("secrets_accessed") is False, "secrets_accessed must be false")
    _require(log_data.get("decision") == "block", "bot execution decision must be block")
    _require(log_data.get("reason") == "validator_bypass_injection_detected", "unexpected bot execution reason")
    _require(bool(log_data.get("log_sha256")), "log_sha256 must be non-empty")
    actual_log_sha256 = hashlib.sha256(log_path.read_bytes()).hexdigest()

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/inf_bot_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "INF-BOT-01", "decision.json phase_id mismatch")
    _require(decision_data.get("phase_class") == "bot_execution", "decision.json phase_class mismatch")
    _require(decision_data.get("actual_decision") == "block", "decision.json actual_decision must be block")
    _require(decision_data.get("expected_decision") == "block", "decision.json expected_decision must be block")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")
    _require(decision_data.get("execution_log_sha256") == actual_log_sha256, "decision.json execution_log_sha256 mismatch")


def _check_minos_verdict_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("minos_verdict_executed") is True, "minos_verdict_executed must be true")
    _require(state.get("minos_verdict_count") == 1, "minos_verdict_count must be 1")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must remain 1")

    artifacts_root = ROOT / "artifacts/inf_minos_01"
    _require(artifacts_root.exists(), "artifacts/inf_minos_01 must exist")

    verdict_paths = sorted(artifacts_root.glob("*verdict.json"))
    _require(len(verdict_paths) == 1, f"expected exactly 1 Minos verdict JSON, found {len(verdict_paths)}")
    verdict_path = verdict_paths[0]
    _require(verdict_path.name == "minos_verdict.json", "unexpected Minos verdict filename")

    verdict_data = _load_json(verdict_path)
    source_log_path = ROOT / "artifacts/inf_bot_01/nemesis_execution_log.json"
    source_log_sha256 = hashlib.sha256(source_log_path.read_bytes()).hexdigest()
    actual_verdict_sha256 = hashlib.sha256(verdict_path.read_bytes()).hexdigest()

    _require(verdict_data.get("phase_id") == "INF-MINOS-01", "minos_verdict phase_id mismatch")
    _require(verdict_data.get("source_phase_id") == "INF-BOT-01", "minos_verdict source_phase_id mismatch")
    _require(verdict_data.get("verdict_id") == "minos_nemesis_validator_bypass_verdict", "unexpected verdict_id")
    _require(verdict_data.get("engine") == "minos_deterministic_threshold_v1", "unexpected engine")
    _require(verdict_data.get("llm_as_judge") is False, "llm_as_judge must be false")
    _require(verdict_data.get("deterministic") is True, "deterministic must be true")
    _require(verdict_data.get("source_log_path") == "artifacts/inf_bot_01/nemesis_execution_log.json", "source_log_path mismatch")
    _require(verdict_data.get("source_log_sha256") == source_log_sha256, "source_log_sha256 mismatch")
    _require(verdict_data.get("expected_decision") == "block", "expected_decision must be block")
    _require(verdict_data.get("actual_decision") == "block", "actual_decision must be block")
    _require(verdict_data.get("verdict") == "block", "verdict must be block")
    _require(verdict_data.get("confidence_policy") == "deterministic_rules_only", "confidence_policy mismatch")
    _require(verdict_data.get("threshold_results", {}).get("identity_match") is True, "identity_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("scenario_match") is True, "scenario_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("safety_flags_clean") is True, "safety_flags_clean must be true")
    _require(verdict_data.get("threshold_results", {}).get("expected_decision_match") is True, "expected_decision_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("reason_match") is True, "reason_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("runtime_absent") is True, "runtime_absent must be true")
    _require(verdict_data.get("threshold_results", {}).get("network_absent") is True, "network_absent must be true")
    _require(verdict_data.get("threshold_results", {}).get("secrets_absent") is True, "secrets_absent must be true")
    _require(bool(verdict_data.get("minos_verdict_sha256")), "minos_verdict_sha256 must be non-empty")

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/inf_minos_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "INF-MINOS-01", "decision.json phase_id mismatch")
    _require(decision_data.get("phase_class") == "minos_verdict", "decision.json phase_class mismatch")
    _require(decision_data.get("minos_verdict_executed") is True, "decision.json minos_verdict_executed must be true")
    _require(decision_data.get("minos_verdict_count") == 1, "decision.json minos_verdict_count must be 1")
    _require(decision_data.get("llm_as_judge") is False, "decision.json llm_as_judge must be false")
    _require(decision_data.get("deterministic_verdict") is True, "decision.json deterministic_verdict must be true")
    _require(decision_data.get("source_bot_id") == "nemesis", "decision.json source_bot_id mismatch")
    _require(decision_data.get("source_scenario_id") == "scenario_11_nemesis", "decision.json source_scenario_id mismatch")
    _require(decision_data.get("source_log_sha256") == source_log_sha256, "decision.json source_log_sha256 mismatch")
    _require(decision_data.get("minos_verdict_sha256") == actual_verdict_sha256, "decision.json minos_verdict_sha256 mismatch")
    _require(decision_data.get("expected_verdict") == "block", "expected_verdict must be block")
    _require(decision_data.get("actual_verdict") == "block", "actual_verdict must be block")
    _require(decision_data.get("threshold_results_all_passed") is True, "threshold_results_all_passed must be true")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")


def _check_purgatorium_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("purgatorium_finding_created") is True, "purgatorium_finding_created must be true")
    _require(state.get("finding_count") == 1, "finding_count must be 1")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must remain 1")
    _require(state.get("minos_verdict_count") == 1, "minos_verdict_count must remain 1")

    artifacts_root = ROOT / "artifacts/purg_01"
    _require(artifacts_root.exists(), "artifacts/purg_01 must exist")

    finding_paths = sorted(artifacts_root.glob("finding*.json"))
    _require(len(finding_paths) == 1, f"expected exactly 1 Purgatorium finding JSON, found {len(finding_paths)}")
    finding_path = finding_paths[0]
    _require(finding_path.name == "finding_nemesis_validator_bypass.json", "unexpected Purgatorium finding filename")

    finding_data = _load_json(finding_path)
    source_verdict_path = ROOT / "artifacts/inf_minos_01/minos_verdict.json"
    source_log_path = ROOT / "artifacts/inf_bot_01/nemesis_execution_log.json"
    fixture_input_path = ROOT / "fixtures/lab_simulation/aris_infernus_lab_full/scenario_11_nemesis/input.json"
    source_verdict_sha256 = hashlib.sha256(source_verdict_path.read_bytes()).hexdigest()
    source_log_sha256 = hashlib.sha256(source_log_path.read_bytes()).hexdigest()
    fixture_input_sha256 = hashlib.sha256(fixture_input_path.read_bytes()).hexdigest()
    canonical_finding_sha256 = _canonical_hash_without_field(finding_data, "finding_sha256")

    _require(finding_data.get("phase_id") == "PURG-01", "finding phase_id mismatch")
    _require(finding_data.get("source_phase_id") == "INF-MINOS-01", "finding source_phase_id mismatch")
    _require(finding_data.get("finding_id") == "purg_nemesis_validator_bypass_001", "unexpected finding_id")
    _require(finding_data.get("source_bot_id") == "nemesis", "source_bot_id must be nemesis")
    _require(finding_data.get("source_scenario_id") == "scenario_11_nemesis", "source_scenario_id mismatch")
    _require(finding_data.get("source_verdict_path") == "artifacts/inf_minos_01/minos_verdict.json", "source_verdict_path mismatch")
    _require(finding_data.get("source_verdict_sha256") == source_verdict_sha256, "source_verdict_sha256 mismatch")
    _require(finding_data.get("source_log_path") == "artifacts/inf_bot_01/nemesis_execution_log.json", "source_log_path mismatch")
    _require(finding_data.get("source_log_sha256") == source_log_sha256, "source_log_sha256 mismatch")
    _require(finding_data.get("attack_class") == "validator_bypass_injection", "attack_class mismatch")
    _require(finding_data.get("finding_type") == "validator_bypass_attempt", "finding_type mismatch")
    _require(finding_data.get("severity") == "S0", "severity must be S0")
    _require(finding_data.get("status") == "open", "status must be open")
    _require(finding_data.get("disposition") == "requires_repair_plan", "disposition mismatch")
    _require(finding_data.get("minos_verdict") == "block", "minos_verdict must be block")
    _require(finding_data.get("evidence_chain", {}).get("fixture_input_hash") == fixture_input_sha256, "fixture_input_hash mismatch")
    _require(finding_data.get("evidence_chain", {}).get("bot_execution_log_hash") == source_log_sha256, "bot_execution_log_hash mismatch")
    _require(finding_data.get("evidence_chain", {}).get("minos_verdict_hash") == source_verdict_sha256, "minos_verdict_hash mismatch")
    _require(finding_data.get("remediation_plan", {}).get("objective") == "harden validator/gate bypass resistance", "remediation objective mismatch")
    _require(finding_data.get("remediation_plan", {}).get("allowed_next_step") == "plan_only_repair_gate", "allowed_next_step mismatch")
    _require(finding_data.get("remediation_plan", {}).get("runtime_patch_allowed") is False, "runtime_patch_allowed must be false")
    _require(finding_data.get("remediation_plan", {}).get("apply_allowed") is False, "apply_allowed must be false")
    _require(finding_data.get("remediation_plan", {}).get("required_future_evidence") == [
        "failing_reproduction_or_negative_test",
        "validator_rule_or_gate_contract",
        "passing_test_after_repair",
        "CI_success",
    ], "required_future_evidence mismatch")
    _require(finding_data.get("finding_sha256") == canonical_finding_sha256, "finding_sha256 mismatch")

    source_verdict_data = _load_json(source_verdict_path)
    _require(source_verdict_data.get("llm_as_judge") is False, "source verdict llm_as_judge must be false")
    _require(source_verdict_data.get("deterministic") is True, "source verdict deterministic must be true")
    threshold_results = source_verdict_data.get("threshold_results", {})
    _require(all(threshold_results.get(key) is True for key in [
        "identity_match",
        "scenario_match",
        "safety_flags_clean",
        "expected_decision_match",
        "reason_match",
        "runtime_absent",
        "network_absent",
        "secrets_absent",
    ]), "all source verdict threshold_results must be true")

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/purg_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "PURG-01", "decision.json phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-MINOS-01", "decision.json previous_phase_id mismatch")
    _require(decision_data.get("phase_class") == "purgatorium", "decision.json phase_class mismatch")
    _require(decision_data.get("purgatorium_finding_created") is True, "decision.json purgatorium_finding_created must be true")
    _require(decision_data.get("finding_count") == 1, "decision.json finding_count must be 1")
    _require(decision_data.get("source_bot_id") == "nemesis", "decision.json source_bot_id mismatch")
    _require(decision_data.get("source_scenario_id") == "scenario_11_nemesis", "decision.json source_scenario_id mismatch")
    _require(decision_data.get("source_verdict_path") == "artifacts/inf_minos_01/minos_verdict.json", "decision.json source_verdict_path mismatch")
    _require(decision_data.get("source_verdict_sha256") == source_verdict_sha256, "decision.json source_verdict_sha256 mismatch")
    _require(decision_data.get("source_log_sha256") == source_log_sha256, "decision.json source_log_sha256 mismatch")
    _require(decision_data.get("finding_path") == "artifacts/purg_01/finding_nemesis_validator_bypass.json", "decision.json finding_path mismatch")
    _require(decision_data.get("finding_sha256") == canonical_finding_sha256, "decision.json finding_sha256 mismatch")
    _require(decision_data.get("severity") == "S0", "decision.json severity must be S0")
    _require(decision_data.get("finding_status") == "open", "decision.json finding_status must be open")
    _require(decision_data.get("remediation_apply_allowed") is False, "decision.json remediation_apply_allowed must be false")
    _require(decision_data.get("runtime_patch_allowed") is False, "decision.json runtime_patch_allowed must be false")
    _require(decision_data.get("llm_as_judge") is False, "decision.json llm_as_judge must be false")
    _require(decision_data.get("deterministic") is True, "decision.json deterministic must be true")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")
    _require(decision_data.get("bedrock_executed") is False, "decision.json bedrock_executed must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "decision.json product_promotion_allowed must be false")
    warnings = decision_data.get("carried_forward_warnings", [])
    _require(len(warnings) == 3, "decision.json must carry exactly 3 warnings")
    _require("INF-MINOS-01 decision.json kept final_origin_main_sha as pending_post_push_verification" in warnings[0], "missing INF-MINOS-01 warning")
    _require("INF-BOT-01 decision.json kept final_origin_main_sha as pending_post_push_verification" in warnings[1], "missing INF-BOT-01 warning")
    _require("INF-MAT-01 final_origin_main_sha points to debc51e" in warnings[2], "missing INF-MAT-01 warning")


def _check_if08_w05_active_context_sync_artifacts(state: dict[str, Any]) -> None:
    for path in (
        ACTIVE_CONTEXT_SYNC_RULE_DECISION_PATH,
        ACTIVE_CONTEXT_SYNC_RULE_SUMMARY_PATH,
        ACTIVE_CONTEXT_SYNC_RULE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W0.5 active-context sync artifact: {path}")

    active_sync_decision = _load_json(ACTIVE_CONTEXT_SYNC_RULE_DECISION_PATH)
    _require(active_sync_decision.get("phase_id") == "IF08_W05_ACTIVE_CONTEXT_SYNC_RULE", "active-context sync decision phase_id mismatch")
    _require(active_sync_decision.get("decision") == "pass", "active-context sync decision must be pass")
    _require(active_sync_decision.get("status") == "if08_w05_active_context_sync_rule_pass", "active-context sync decision status mismatch")
    _require(active_sync_decision.get("active_context_sync_applied") is True, "active-context sync decision must mark sync applied")
    _require(active_sync_decision.get("permanent_active_update_rule_installed") is True, "active-context sync decision must mark permanent rule installed")

    external_project_paths = (
        IF08_W05_ALIAS_DECISION_PATH,
        IF08_W05_ALIAS_OVERLAY_PATH,
        IF08_W05_ALIAS_GAP_MATRIX_PATH,
        IF08_W05_ALIAS_NO_EXECUTION_PATH,
        IF08_W05_ALIAS_SUMMARY_PATH,
        IF08_W05_ALIAS_DOC_PATH,
        IF08_W05_PROJECT_SYNC_DECISION_PATH,
        IF08_W05_PROJECT_SYNC_SUMMARY_PATH,
        IF08_W05_PROJECT_SYNC_REPORT_PATH,
        IF08_W05_PROJECT_SYNC_CI_MATRIX_PATH,
        IF08_W05_PROJECT_SYNC_NO_EXECUTION_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        _require(active_sync_decision.get("source_reported_project_sha") == IF08_W05_SYNC_SOURCE_PROJECT_SHA, "standalone active-context validation still requires recorded source project sha")
        _require(active_sync_decision.get("source_reported_phase_status") == IF08_W05_SYNC_SOURCE_STATUS, "standalone active-context validation still requires recorded source project status")
        return

    alias_decision = _load_json(IF08_W05_ALIAS_DECISION_PATH)
    _require(alias_decision.get("decision") == "pass", "IF08 W0.5 alias decision must be pass")
    _require(alias_decision.get("status") == IF08_W05_SYNC_SOURCE_STATUS, "IF08 W0.5 alias decision status mismatch")
    _require(alias_decision.get("required_next_action") == IF08_W05_SYNC_NEXT_RECOMMENDED_STEP, "IF08 W0.5 alias decision next action mismatch")
    _require(alias_decision.get("wave_executed") is False, "IF08 W0.5 alias decision must keep wave_executed=false")
    _require(alias_decision.get("bot_executed") is False, "IF08 W0.5 alias decision must keep bot_executed=false")

    alias_summary = _load_json(IF08_W05_ALIAS_SUMMARY_PATH)
    _require(alias_summary.get("status") == IF08_W05_SYNC_SOURCE_STATUS, "IF08 W0.5 alias summary status mismatch")
    _require(alias_summary.get("required_next_action") == IF08_W05_SYNC_NEXT_RECOMMENDED_STEP, "IF08 W0.5 alias summary next action mismatch")
    _require(alias_summary.get("alias_scope_missing_w05_resolved") is True, "IF08 W0.5 alias summary must resolve W0.5 scope gap")

    sync_decision = _load_json(IF08_W05_PROJECT_SYNC_DECISION_PATH)
    _require(sync_decision.get("phase_id") == "IF08_W05_ACTIVE_CONTEXT_SYNC_RULE", "project sync decision phase_id mismatch")
    _require(sync_decision.get("decision") == "pass", "project sync decision must be pass")
    _require(sync_decision.get("status") == "if08_w05_active_context_sync_rule_pass", "project sync decision status mismatch")
    _require(sync_decision.get("source_reported_phase_status") == IF08_W05_SYNC_SOURCE_STATUS, "project sync decision source status mismatch")
    _require(sync_decision.get("source_reported_project_sha") == IF08_W05_SYNC_SOURCE_PROJECT_SHA, "project sync decision project sha mismatch")
    _require(sync_decision.get("project_origin_main_sha_verified") is True, "project sync decision must verify origin/main sha")
    _require(sync_decision.get("project_ci_green_confirmed") is True, "project sync decision must confirm green CI")
    _require(sync_decision.get("active_context_sync_required") is True, "project sync decision must mark sync required")
    _require(sync_decision.get("active_context_sync_applied") is True, "project sync decision must mark sync applied")
    _require(sync_decision.get("validator_enforces_or_documents_active_sync_rule") is True, "project sync decision must record validator/docs enforcement")
    _require(sync_decision.get("next_recommended_step") == IF08_W05_SYNC_NEXT_RECOMMENDED_STEP, "project sync decision next step mismatch")

    no_execution = sync_decision.get("no_execution", {})
    for key in (
        "rerun_if08_w05_preflight_readiness_executed",
        "wave_executed",
        "bot_executed",
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(no_execution.get(key) is False, f"project sync decision no_execution.{key} must be false")


def _check_if08_w05_preflight_rerun_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W05_RERUN_ACTIVE_DECISION_PATH,
        IF08_W05_RERUN_ACTIVE_SUMMARY_PATH,
        IF08_W05_RERUN_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W0.5 preflight rerun active-context artifact: {path}")

    active_decision = _load_json(IF08_W05_RERUN_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF08_W05_PREFLIGHT_READINESS_RERUN", "active rerun decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active rerun decision must be pass")
    _require(active_decision.get("status") == IF08_W05_RERUN_STATUS, "active rerun decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W05_RERUN_PROJECT_SHA, "active rerun decision project sha mismatch")
    _require(active_decision.get("source_latest_completed_phase") == IF08_W05_SYNC_SOURCE_PHASE, "active rerun decision source phase mismatch")
    _require(active_decision.get("source_latest_completed_status") == IF08_W05_SYNC_SOURCE_STATUS, "active rerun decision source status mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active rerun decision must verify project origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active rerun decision must confirm project green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active rerun decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active rerun decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w05_preflight_readiness_rerun") is True, "active rerun decision must confirm remote reflection")
    _require(active_decision.get("next_recommended_step") == IF08_W05_RERUN_NEXT_RECOMMENDED_STEP, "active rerun decision next step mismatch")
    no_execution = active_decision.get("no_execution", {})
    for key in (
        "wave_executed",
        "bot_executed",
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(no_execution.get(key) is False, f"active rerun decision no_execution.{key} must be false")

    external_project_paths = (
        IF08_W05_RERUN_DECISION_PATH,
        IF08_W05_RERUN_SUMMARY_PATH,
        IF08_W05_RERUN_REPORT_PATH,
        IF08_W05_RERUN_MATRIX_PATH,
        IF08_W05_RERUN_NO_EXECUTION_PATH,
        IF08_W05_RERUN_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        _require(active_decision.get("source_project_sha") == IF08_W05_RERUN_PROJECT_SHA, "standalone rerun validation still requires recorded project sha")
        _require(active_decision.get("status") == IF08_W05_RERUN_STATUS, "standalone rerun validation still requires recorded rerun status")
        return

    rerun_decision = _load_json(IF08_W05_RERUN_DECISION_PATH)
    rerun_decision_value = rerun_decision.get("decision")
    _require(rerun_decision.get("phase_id") == "IF08_W05_PREFLIGHT_READINESS_RERUN", "project rerun decision phase_id mismatch")
    _require(rerun_decision_value in {"pass", "blocked"}, "project rerun decision must be pass or blocked")
    expected_rerun_status = IF08_W05_RERUN_STATUS if rerun_decision_value == "pass" else IF08_W05_RERUN_BLOCKED_STATUS
    _require(rerun_decision.get("status") == expected_rerun_status, "project rerun decision status mismatch")
    if rerun_decision_value == "pass":
        _require(rerun_decision.get("source_latest_completed_phase") == IF08_W05_SYNC_SOURCE_PHASE, "project rerun decision source phase mismatch")
        _require(rerun_decision.get("source_latest_completed_status") == IF08_W05_SYNC_SOURCE_STATUS, "project rerun decision source status mismatch")
        _require(rerun_decision.get("source_project_sha") == IF08_W05_SYNC_SOURCE_PROJECT_SHA, "project rerun decision source project sha mismatch")
        _require(rerun_decision.get("ready_for_next_recommended_step") is True, "project rerun decision must be ready for next step")
        _require(rerun_decision.get("next_recommended_step") == IF08_W05_RERUN_NEXT_RECOMMENDED_STEP, "project rerun decision next step mismatch")
    else:
        _require(bool(rerun_decision.get("source_latest_completed_phase")), "project blocked rerun decision source phase must be present")
        _require(bool(rerun_decision.get("source_latest_completed_status")), "project blocked rerun decision source status must be present")
        _require(bool(rerun_decision.get("source_project_sha")), "project blocked rerun decision source project sha must be present")
        _require(rerun_decision.get("ready_for_next_recommended_step") is False, "project blocked rerun decision must not be ready for next step")
        _require(rerun_decision.get("next_recommended_step") == IF08_W05_RERUN_BLOCKED_NEXT_RECOMMENDED_STEP, "project blocked rerun decision next step mismatch")
        _require(bool(rerun_decision.get("unresolved_mismatches")), "project blocked rerun decision must document unresolved_mismatches")
    active_update = rerun_decision.get("active_context_update", {})
    _require(active_update.get("required") is True, "project rerun decision active_context_update.required must be true")
    _require(active_update.get("applied") is True, "project rerun decision active_context_update.applied must be true")
    _require(active_update.get("remote_main_verified") is True, "project rerun decision active_context_update.remote_main_verified must be true")

    rerun_summary = _load_json(IF08_W05_RERUN_SUMMARY_PATH)
    rerun_summary_decision = rerun_summary.get("decision")
    _require(rerun_summary_decision in {"pass", "blocked"}, "project rerun summary must be pass or blocked")
    expected_rerun_summary_status = IF08_W05_RERUN_STATUS if rerun_summary_decision == "pass" else IF08_W05_RERUN_BLOCKED_STATUS
    _require(rerun_summary.get("status") == expected_rerun_summary_status, "project rerun summary status mismatch")
    if rerun_summary_decision == "pass":
        _require(rerun_summary.get("next_recommended_step") == IF08_W05_RERUN_NEXT_RECOMMENDED_STEP, "project rerun summary next step mismatch")
        _require(rerun_summary.get("unresolved_mismatch_count") == 0, "project rerun summary unresolved mismatch count must be zero")
    else:
        _require(rerun_summary.get("next_recommended_step") == IF08_W05_RERUN_BLOCKED_NEXT_RECOMMENDED_STEP, "project blocked rerun summary next step mismatch")
        _require(int(rerun_summary.get("unresolved_mismatch_count", 0)) > 0, "project blocked rerun summary unresolved mismatch count must be positive")

    rerun_no_execution = _load_json(IF08_W05_RERUN_NO_EXECUTION_PATH)
    for key in (
        "wave_executed",
        "bot_executed",
        "runtime_executed",
        "product_or_bedrock_executed",
        "real_apply_executed",
        "secrets_accessed",
        "dependency_or_package_manager_used",
        "external_network_used_except_github_governance",
    ):
        _require(rerun_no_execution.get(key) is False, f"project rerun no_execution.{key} must be false")


def _check_if08_w05_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W05_CONTROLLED_ACTIVE_DECISION_PATH,
        IF08_W05_CONTROLLED_ACTIVE_SUMMARY_PATH,
        IF08_W05_CONTROLLED_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W0.5 controlled execution active-context artifact: {path}")

    active_decision = _load_json(IF08_W05_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "active controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W05_CONTROLLED_STATUS, "active controlled decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "active controlled decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "active controlled decision ci state mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active controlled decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active controlled decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w05_controlled_execution") is True, "active controlled decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W05_CONTROLLED_PHASE, "active controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W05_CONTROLLED_STATUS, "active controlled decision latest status mismatch")
    _require(active_decision.get("tamper_attempts_expected") == 4, "active controlled decision tamper_attempts_expected must be 4")
    _require(active_decision.get("tamper_attempts_detected") == 4, "active controlled decision tamper_attempts_detected must be 4")
    _require(active_decision.get("ter_result") == 1.0, "active controlled decision ter_result must be 1.0")
    _require(active_decision.get("synthetic_isolated_lab_only") is True, "active controlled decision must be synthetic isolated lab only")
    _require(active_decision.get("bedrock_preparation_exception") is True, "active controlled decision must mark bedrock exception")
    _require(active_decision.get("next_recommended_step") == IF08_W05_CONTROLLED_NEXT_RECOMMENDED_STEP, "active controlled decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in ("w05_executed", "wave_executed", "bot_executed"):
        _require(active_outcome.get(key) is True, f"active controlled decision execution_outcome.{key} must be true")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(active_outcome.get(key) is False, f"active controlled decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W05_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "active controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W05_CONTROLLED_STATUS, "active controlled summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W05_CONTROLLED_PHASE, "active controlled summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W05_CONTROLLED_STATUS, "active controlled summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "active controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "active controlled summary ci state mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active controlled summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w05_controlled_execution") is True, "active controlled summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active controlled summary must preserve permanent rule")
    _require(active_summary.get("tamper_attempts_expected") == 4, "active controlled summary tamper_attempts_expected must be 4")
    _require(active_summary.get("tamper_attempts_detected") == 4, "active controlled summary tamper_attempts_detected must be 4")
    _require(active_summary.get("ter_result") == 1.0, "active controlled summary ter_result must be 1.0")
    _require(active_summary.get("next_recommended_step") == IF08_W05_CONTROLLED_NEXT_RECOMMENDED_STEP, "active controlled summary next step mismatch")

    _mirror_contains(
        IF08_W05_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W0.5 Controlled Ledger/Evidence Integrity Execution",
        IF08_W05_CONTROLLED_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w05_controlled_execution: `true`",
        "next_recommended_step: `defer_next_if08_wave_prompt_until_post_sync_review`",
    )

    external_project_paths = (
        IF08_W05_CONTROLLED_DECISION_PATH,
        IF08_W05_CONTROLLED_SUMMARY_PATH,
        IF08_W05_CONTROLLED_MATRIX_PATH,
        IF08_W05_CONTROLLED_HASH_CHAIN_PATH,
        IF08_W05_CONTROLLED_CUSTODY_CHAIN_PATH,
        IF08_W05_CONTROLLED_BOUNDARY_PATH,
        IF08_W05_CONTROLLED_BUNDLE_PATH,
        IF08_W05_CONTROLLED_LEDGER_PATH,
        IF08_W05_CONTROLLED_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W05_CONTROLLED_DECISION_PATH)
    valid_decisions = {"pass", "invalid"}
    decision_value = decision.get("decision")
    _require(decision.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "project controlled decision phase_id mismatch")
    _require(
        decision_value in valid_decisions,
        "project controlled decision must be pass or invalid",
    )
    expected_decision_status = (
        IF08_W05_CONTROLLED_STATUS
        if decision_value == "pass"
        else IF08_W05_CONTROLLED_INVALID_STATUS
    )
    _require(decision.get("status") == expected_decision_status, "project controlled decision status mismatch")
    _require(decision.get("wave_id") == "W0.5", "project controlled decision wave_id mismatch")
    if decision_value == "pass":
        _require(decision.get("wave_name") == "Ledger/evidence integrity", "project controlled decision wave_name mismatch")
        _require(decision.get("execution_scope") == "synthetic_isolated_lab_only", "project controlled decision execution_scope mismatch")
        _require(decision.get("tamper_attempts_expected") == 4, "project controlled decision tamper_attempts_expected must be 4")
        _require(decision.get("tamper_attempts_detected") == 4, "project controlled decision tamper_attempts_detected must be 4")
        _require(decision.get("ter_result") == 1.0, "project controlled decision ter_result must be 1.0")
        _require(decision.get("required_ter") == 1.0, "project controlled decision required_ter must be 1.0")
        _require(decision.get("hash_chain_valid_clean") is True, "project controlled decision hash_chain_valid_clean must be true")
        _require(decision.get("custody_chain_valid_clean") is True, "project controlled decision custody_chain_valid_clean must be true")
        _require(decision.get("provenance_baseline_valid") is True, "project controlled decision provenance_baseline_valid must be true")
        _require(decision.get("ledger_order_baseline_valid") is True, "project controlled decision ledger_order_baseline_valid must be true")
        _require(decision.get("bedrock_preparation_exception") is True, "project controlled decision bedrock_preparation_exception must be true")
        _require(decision.get("active_context_update_required") is True, "project controlled decision active_context_update_required must be true")
        _require(decision.get("canonical_sync_blocked_by_guard") == "NO-EXTERNAL-NETWORK-EXCEPT-GITHUB-GOVERNANCE", "project controlled decision guard mismatch")
        _require(decision.get("next_wave_authorized") is False, "project controlled decision next_wave_authorized must be false")
        _require(decision.get("required_next_action") == IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_PASS, "project controlled decision next action mismatch")
    else:
        _require(bool(decision.get("blocking_findings")), "project controlled invalid decision must document blocking_findings")
        _require(decision.get("required_next_action") == IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_INVALID, "project controlled invalid decision next action mismatch")

    summary = _load_json(IF08_W05_CONTROLLED_SUMMARY_PATH)
    summary_decision = summary.get("decision")
    _require(summary.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "project controlled summary phase_id mismatch")
    _require(summary_decision in valid_decisions, "project controlled summary must be pass or invalid")
    expected_summary_status = (
        IF08_W05_CONTROLLED_STATUS
        if summary_decision == "pass"
        else IF08_W05_CONTROLLED_INVALID_STATUS
    )
    _require(summary.get("status") == expected_summary_status, "project controlled summary status mismatch")
    if summary_decision == "pass":
        _require(summary.get("tamper_attempts_expected") == 4, "project controlled summary tamper_attempts_expected must be 4")
        _require(summary.get("tamper_attempts_detected") == 4, "project controlled summary tamper_attempts_detected must be 4")
        _require(summary.get("ter_result") == 1.0, "project controlled summary ter_result must be 1.0")
        _require(summary.get("hash_chain_valid_clean") is True, "project controlled summary hash_chain_valid_clean must be true")
        _require(summary.get("custody_chain_valid_clean") is True, "project controlled summary custody_chain_valid_clean must be true")
        _require(summary.get("active_context_update_applied") is False, "project controlled summary active_context_update_applied must remain false before sync record")
        _require(summary.get("canonical_sync_performed") is False, "project controlled summary canonical_sync_performed must remain false before sync record")
        _require(summary.get("required_next_action") == IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_PASS, "project controlled summary next action mismatch")
    else:
        _require(bool(summary.get("blocking_findings")), "project controlled invalid summary must document blocking_findings")
        _require(summary.get("required_next_action") == IF08_W05_CONTROLLED_PROJECT_NEXT_ACTION_INVALID, "project controlled invalid summary next action mismatch")

    matrix = _load_json(IF08_W05_CONTROLLED_MATRIX_PATH)
    _require(matrix.get("expected_tamper_attempts") == 4, "project controlled matrix expected_tamper_attempts must be 4")
    _require(matrix.get("detected_tamper_attempts") == 4, "project controlled matrix detected_tamper_attempts must be 4")
    _require(matrix.get("ter_result") == 1.0, "project controlled matrix ter_result must be 1.0")
    for attempt in matrix.get("attempts", []):
        _require(attempt.get("detected") is True, f"project controlled matrix attempt {attempt.get('attempt_id')} must be detected")

    hash_chain = _load_json(IF08_W05_CONTROLLED_HASH_CHAIN_PATH)
    _require(hash_chain.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "project controlled hash chain phase_id mismatch")
    _require(hash_chain.get("wave_id") == "W0.5", "project controlled hash chain wave_id mismatch")
    _require(hash_chain.get("entry_count") == 25, "project controlled hash chain entry_count must be 25")
    _require(hash_chain.get("source_record_count") == 25, "project controlled hash chain source_record_count must be 25")
    _require(hash_chain.get("clean_hash_chain_valid") is True, "project controlled hash chain clean_hash_chain_valid must be true")
    _require(bool(hash_chain.get("hash_chain_root_sha256")), "project controlled hash chain root sha must be present")

    custody_lines = [line for line in IF08_W05_CONTROLLED_CUSTODY_CHAIN_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    _require(len(custody_lines) > 0, "project controlled custody chain must not be empty")
    for line in custody_lines:
        _require(isinstance(json.loads(line), dict), "project controlled custody chain lines must be JSON objects")

    ledger_lines = [line for line in IF08_W05_CONTROLLED_LEDGER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    _require(len(ledger_lines) > 0, "project controlled execution ledger must not be empty")
    ledger_entry = json.loads(ledger_lines[-1])
    _require(
        ledger_entry.get("status") in {IF08_W05_CONTROLLED_STATUS, IF08_W05_CONTROLLED_INVALID_STATUS},
        "project controlled execution ledger status mismatch",
    )


def _state_preserves_if08_w05_historical_blocked(state: dict[str, Any]) -> bool:
    current_live_route = state.get("current_live_route", {})
    return (
        state.get("next_phase") == CURRENT_EXPECTED_NEXT_PHASE_ID
        and state.get("active_next_phase") == CURRENT_EXPECTED_NEXT_PHASE_ID
        and state.get("status") == CURRENT_LIVE_STATUS
        and state.get("current_status") == CURRENT_LIVE_CURRENT_STATUS
        and state.get("latest_completed_phase") == CURRENT_LIVE_PHASE
        and state.get("latest_completed_status") == CURRENT_LIVE_STATUS
        and current_live_route.get("active_next_phase") == CURRENT_EXPECTED_NEXT_PHASE_ID
        and current_live_route.get("status") == CURRENT_LIVE_STATUS
        and current_live_route.get("current_status") == CURRENT_LIVE_CURRENT_STATUS
        and current_live_route.get("latest_completed_phase") == CURRENT_LIVE_PHASE
        and current_live_route.get("latest_completed_status") == CURRENT_LIVE_STATUS
    )


def _require_if08_w05_historical_blocked_payload(
    payload: dict[str, Any],
    label: str,
    *,
    require_next_recommended_step: bool,
) -> None:
    _require(payload.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", f"{label} phase_id mismatch")
    _require(payload.get("decision") == "blocked", f"{label} must remain blocked historical artifact")
    status = payload.get("status")
    _require(
        isinstance(status, str) and status.startswith("if08_w05_post_sync_review") and "blocked" in status,
        f"{label} status must remain blocked historical post-sync review",
    )
    if require_next_recommended_step:
        _require(bool(payload.get("next_recommended_step")), f"{label} next_recommended_step must be present")
    if "w1_execution_performed" in payload:
        _require(payload.get("w1_execution_performed") is False, f"{label} w1_execution_performed must remain false")
    if "w1_execution_allowed" in payload:
        _require(payload.get("w1_execution_allowed") is False, f"{label} w1_execution_allowed must remain false")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "dependency_or_package_manager_used",
        "external_network_used_except_github_governance",
        "finding_closed",
        "remediation_proven",
    ):
        if key in payload:
            _require(payload.get(key) is False, f"{label} {key} must remain false")


def _check_if08_w05_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W05_POST_SYNC_ACTIVE_DECISION_PATH,
        IF08_W05_POST_SYNC_ACTIVE_SUMMARY_PATH,
        IF08_W05_POST_SYNC_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W0.5 post-sync review active-context artifact: {path}")

    active_decision = _load_json(IF08_W05_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "active post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W05_POST_SYNC_STATUS, "active post-sync decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W05_POST_SYNC_PROJECT_SHA, "active post-sync decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W05_POST_SYNC_CI_STATE, "active post-sync decision ci state mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active post-sync decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active post-sync decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w05_post_sync_review") is True, "active post-sync decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W05_POST_SYNC_PHASE, "active post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W05_POST_SYNC_STATUS, "active post-sync decision latest status mismatch")
    _require(active_decision.get("w05_ter") == 1.0, "active post-sync decision w05_ter must be 1.0")
    _require(active_decision.get("w05_tamper_attempts_expected") == 4, "active post-sync decision tamper_attempts_expected must be 4")
    _require(active_decision.get("w05_tamper_attempts_detected") == 4, "active post-sync decision tamper_attempts_detected must be 4")
    _require(active_decision.get("w1_readiness_state") == "ready_for_preparation", "active post-sync decision readiness state mismatch")
    _require(active_decision.get("w1_preparation_allowed_next") is True, "active post-sync decision must allow next preparation")
    _require(active_decision.get("w1_execution_performed") is False, "active post-sync decision must keep w1_execution_performed false")
    _require(active_decision.get("w1_execution_allowed") is False, "active post-sync decision must keep w1_execution_allowed false")
    _require(active_decision.get("next_recommended_step") == IF08_W05_POST_SYNC_NEXT_RECOMMENDED_STEP, "active post-sync decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    _require(active_outcome.get("w05_executed") is True, "active post-sync decision execution_outcome.w05_executed must be true")
    _require(active_outcome.get("w1_execution_performed") is False, "active post-sync decision execution_outcome.w1_execution_performed must be false")
    _require(active_outcome.get("w1_execution_allowed") is False, "active post-sync decision execution_outcome.w1_execution_allowed must be false")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(active_outcome.get(key) is False, f"active post-sync decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W05_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "active post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W05_POST_SYNC_STATUS, "active post-sync summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W05_POST_SYNC_PHASE, "active post-sync summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W05_POST_SYNC_STATUS, "active post-sync summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W05_POST_SYNC_PROJECT_SHA, "active post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W05_POST_SYNC_CI_STATE, "active post-sync summary ci state mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active post-sync summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w05_post_sync_review") is True, "active post-sync summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active post-sync summary must preserve permanent rule")
    _require(active_summary.get("w05_ter") == 1.0, "active post-sync summary w05_ter must be 1.0")
    _require(active_summary.get("w05_tamper_attempts_expected") == 4, "active post-sync summary tamper_attempts_expected must be 4")
    _require(active_summary.get("w05_tamper_attempts_detected") == 4, "active post-sync summary tamper_attempts_detected must be 4")
    _require(active_summary.get("w1_readiness_state") == "ready_for_preparation", "active post-sync summary readiness state mismatch")
    _require(active_summary.get("w1_preparation_allowed_next") is True, "active post-sync summary must allow next preparation")
    _require(active_summary.get("w1_execution_allowed") is False, "active post-sync summary must keep execution disallowed")
    _require(active_summary.get("next_recommended_step") == IF08_W05_POST_SYNC_NEXT_RECOMMENDED_STEP, "active post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W05_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W0.5 Post-Sync Review & W1 Readiness Decision",
        IF08_W05_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w05_post_sync_review: `true`",
        "next_recommended_step: `prepare_if08_w1_context_memory_rag_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W05_POST_SYNC_DECISION_PATH,
        IF08_W05_POST_SYNC_SUMMARY_PATH,
        IF08_W05_POST_SYNC_REPORT_PATH,
        IF08_W1_READINESS_MATRIX_PATH,
        IF08_W05_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W05_POST_SYNC_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W05_POST_SYNC_DECISION_PATH)
    summary = _load_json(IF08_W05_POST_SYNC_SUMMARY_PATH)
    no_execution = _load_json(IF08_W05_POST_SYNC_NO_EXECUTION_PATH)
    if _state_preserves_if08_w05_historical_blocked(state):
        _require_if08_w05_historical_blocked_payload(
            decision,
            "project post-sync decision",
            require_next_recommended_step=True,
        )
        _require(decision.get("source_phase") == IF08_W05_CONTROLLED_PHASE, "project post-sync decision source phase mismatch")
        _require(decision.get("source_status") == IF08_W05_CONTROLLED_STATUS, "project post-sync decision source status mismatch")
        _require(decision.get("source_project_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "project post-sync decision source project sha mismatch")
        _require(decision.get("source_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "project post-sync decision source ci state mismatch")
        _require(decision.get("w05_ter") == 1.0, "project post-sync decision w05_ter must be 1.0")
        _require(decision.get("w05_tamper_attempts_expected") == 4, "project post-sync decision tamper_attempts_expected must be 4")
        _require(decision.get("w05_tamper_attempts_detected") == 4, "project post-sync decision tamper_attempts_detected must be 4")
        _require(decision.get("w05_canonical_sync_verified") is False, "project post-sync decision historical blocked policy requires w05_canonical_sync_verified=false")
        _require(decision.get("w1_preparation_allowed_next") is False, "project post-sync decision historical blocked policy requires w1_preparation_allowed_next=false")
        _require(isinstance(decision.get("blocking_findings"), list) and len(decision["blocking_findings"]) > 0, "project post-sync decision historical blocked policy requires blocking_findings")

        _require_if08_w05_historical_blocked_payload(
            summary,
            "project post-sync summary",
            require_next_recommended_step=True,
        )
        _require(summary.get("source_phase") == IF08_W05_CONTROLLED_PHASE, "project post-sync summary source phase mismatch")
        _require(summary.get("source_status") == IF08_W05_CONTROLLED_STATUS, "project post-sync summary source status mismatch")
        _require(summary.get("source_project_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "project post-sync summary source project sha mismatch")
        _require(summary.get("source_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "project post-sync summary source ci state mismatch")
        _require(summary.get("w05_ter") == 1.0, "project post-sync summary w05_ter must be 1.0")
        _require(summary.get("w05_tamper_attempts_expected") == 4, "project post-sync summary tamper_attempts_expected must be 4")
        _require(summary.get("w05_tamper_attempts_detected") == 4, "project post-sync summary tamper_attempts_detected must be 4")
        _require(summary.get("w05_canonical_sync_verified") is False, "project post-sync summary historical blocked policy requires w05_canonical_sync_verified=false")
        _require(summary.get("w1_readiness_state") == "blocked", "project post-sync summary historical blocked policy requires w1_readiness_state=blocked")
        _require(summary.get("w1_preparation_allowed_next") is False, "project post-sync summary historical blocked policy requires w1_preparation_allowed_next=false")
        _require(summary.get("blocking_findings_count") == 4, "project post-sync summary blocking_findings_count must remain 4")

        _require_if08_w05_historical_blocked_payload(
            no_execution,
            "project post-sync no_execution",
            require_next_recommended_step=False,
        )
        for key in (
            "active_context_state_mutated",
            "git_commit_attempted",
            "git_push_attempted",
        ):
            _require(no_execution.get(key) is False, f"project post-sync no_execution.{key} must be false")
        return

    _require(decision.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "project post-sync decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project post-sync decision must be pass")
    _require(decision.get("status") == IF08_W05_POST_SYNC_STATUS, "project post-sync decision status mismatch")
    _require(decision.get("source_phase") == IF08_W05_CONTROLLED_PHASE, "project post-sync decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W05_CONTROLLED_STATUS, "project post-sync decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "project post-sync decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "project post-sync decision source ci state mismatch")
    _require(decision.get("w05_ter") == 1.0, "project post-sync decision w05_ter must be 1.0")
    _require(decision.get("w05_tamper_attempts_expected") == 4, "project post-sync decision tamper_attempts_expected must be 4")
    _require(decision.get("w05_tamper_attempts_detected") == 4, "project post-sync decision tamper_attempts_detected must be 4")
    _require(decision.get("w05_canonical_sync_verified") is True, "project post-sync decision must verify canonical sync")
    _require(decision.get("w1_execution_performed") is False, "project post-sync decision w1_execution_performed must be false")
    _require(decision.get("w1_preparation_allowed_next") is True, "project post-sync decision must allow next preparation")
    _require(decision.get("w1_execution_allowed") is False, "project post-sync decision w1_execution_allowed must be false")
    _require(decision.get("runtime_executed") is False, "project post-sync decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project post-sync decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project post-sync decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project post-sync decision secrets_accessed must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project post-sync decision dependency_or_package_manager_used must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project post-sync decision external_network_used_except_github_governance must be false")
    _require(decision.get("next_recommended_step") == IF08_W05_POST_SYNC_NEXT_RECOMMENDED_STEP, "project post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project post-sync decision blocking_findings must be empty")

    _require(summary.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "project post-sync summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project post-sync summary must be pass")
    _require(summary.get("status") == IF08_W05_POST_SYNC_STATUS, "project post-sync summary status mismatch")
    _require(summary.get("source_phase") == IF08_W05_CONTROLLED_PHASE, "project post-sync summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W05_CONTROLLED_STATUS, "project post-sync summary source status mismatch")
    _require(summary.get("source_project_sha") == IF08_W05_CONTROLLED_PROJECT_SHA, "project post-sync summary source project sha mismatch")
    _require(summary.get("source_ci_state") == IF08_W05_CONTROLLED_CI_STATE, "project post-sync summary source ci state mismatch")
    _require(summary.get("w05_ter") == 1.0, "project post-sync summary w05_ter must be 1.0")
    _require(summary.get("w05_tamper_attempts_expected") == 4, "project post-sync summary tamper_attempts_expected must be 4")
    _require(summary.get("w05_tamper_attempts_detected") == 4, "project post-sync summary tamper_attempts_detected must be 4")
    _require(summary.get("w05_canonical_sync_verified") is True, "project post-sync summary must verify canonical sync")
    _require(summary.get("w1_readiness_state") == "ready_for_preparation", "project post-sync summary readiness state mismatch")
    _require(summary.get("w1_preparation_allowed_next") is True, "project post-sync summary must allow next preparation")
    _require(summary.get("w1_execution_allowed") is False, "project post-sync summary execution allowed must remain false")
    _require(summary.get("next_recommended_step") == IF08_W05_POST_SYNC_NEXT_RECOMMENDED_STEP, "project post-sync summary next step mismatch")

    readiness = _load_json(IF08_W1_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "project w1 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W1", "project w1 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Context/memory/RAG", "project w1 readiness wave_name mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project w1 readiness state mismatch")
    _require(readiness.get("w1_execution_performed") is False, "project w1 readiness must keep execution false")
    _require(readiness.get("w1_preparation_allowed_next") is True, "project w1 readiness must allow next preparation")
    _require(readiness.get("w1_execution_allowed") is False, "project w1 readiness must keep execution disallowed")
    _require(readiness.get("w1_execution_artifacts_unchanged") is True, "project w1 readiness must keep historical artifacts unchanged")

    _require(no_execution.get("phase_id") == "IF-08-W05-POST-SYNC-REVIEW", "project post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W05_POST_SYNC_STATUS, "project post-sync no_execution status mismatch")
    _require(no_execution.get("w1_execution_performed") is False, "project post-sync no_execution must keep execution false")
    _require(no_execution.get("w1_execution_allowed") is False, "project post-sync no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "dependency_or_package_manager_used",
        "external_network_used_except_github_governance",
        "active_context_state_mutated",
        "git_commit_attempted",
        "git_push_attempted",
        ):
        _require(no_execution.get(key) is False, f"project post-sync no_execution.{key} must be false")


def _check_if08_w1_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W1_CONTROLLED_ACTIVE_DECISION_PATH,
        IF08_W1_CONTROLLED_ACTIVE_SUMMARY_PATH,
        IF08_W1_CONTROLLED_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W1 controlled execution active-context artifact: {path}")

    active_decision = _load_json(IF08_W1_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "active W1 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W1 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W1_CONTROLLED_STATUS, "active W1 controlled decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W1_CONTROLLED_PROJECT_SHA, "active W1 controlled decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W1_CONTROLLED_CI_STATE, "active W1 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W1_CONTROLLED_PROJECT_CI_RUN_URL, "active W1 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W1 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W1 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W1 controlled decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W1 controlled decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w1_context_memory_rag_controlled_execution") is True, "active W1 controlled decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W1_CONTROLLED_PHASE, "active W1 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W1_CONTROLLED_STATUS, "active W1 controlled decision latest status mismatch")
    _require(active_decision.get("context_integrity_violations_expected") == 10, "active W1 controlled decision expected violations must be 10")
    _require(active_decision.get("context_integrity_violations_blocked") == 10, "active W1 controlled decision blocked violations must be 10")
    _require(active_decision.get("cir_observed") == 1.0, "active W1 controlled decision cir_observed must be 1.0")
    _require(active_decision.get("w1_execution_performed") is True, "active W1 controlled decision must record execution performed")
    _require(active_decision.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W1 controlled decision wave_executed mismatch")
    _require(active_decision.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W1 controlled decision bot_executed mismatch")
    _require(active_decision.get("w1_execution_allowed") is False, "active W1 controlled decision must keep w1_execution_allowed false")
    _require(active_decision.get("next_recommended_step") == IF08_W1_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W1 controlled decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W1 controlled decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W1_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "active W1 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W1 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W1_CONTROLLED_STATUS, "active W1 controlled summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W1_CONTROLLED_PHASE, "active W1 controlled summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W1_CONTROLLED_STATUS, "active W1 controlled summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W1_CONTROLLED_PROJECT_SHA, "active W1 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W1_CONTROLLED_CI_STATE, "active W1 controlled summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W1_CONTROLLED_PROJECT_CI_RUN_URL, "active W1 controlled summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W1 controlled summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w1_context_memory_rag_controlled_execution") is True, "active W1 controlled summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W1 controlled summary must preserve permanent rule")
    _require(active_summary.get("context_integrity_violations_expected") == 10, "active W1 controlled summary expected violations must be 10")
    _require(active_summary.get("context_integrity_violations_blocked") == 10, "active W1 controlled summary blocked violations must be 10")
    _require(active_summary.get("cir_observed") == 1.0, "active W1 controlled summary cir_observed must be 1.0")
    _require(active_summary.get("w1_execution_performed") is True, "active W1 controlled summary must record execution performed")
    _require(active_summary.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W1 controlled summary wave_executed mismatch")
    _require(active_summary.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W1 controlled summary bot_executed mismatch")
    _require(active_summary.get("next_recommended_step") == IF08_W1_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W1 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W1_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W1 Context/Memory/RAG Controlled Execution",
        IF08_W1_CONTROLLED_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w1_context_memory_rag_controlled_execution: `true`",
        "w1_execution_performed: `true_synthetic_isolated_lab_only`",
        "next_recommended_step: `post_sync_review_if08_w1_context_memory_rag_controlled_execution`",
    )

    external_project_paths = (
        IF08_W1_CONTROLLED_DECISION_PATH,
        IF08_W1_CONTROLLED_SUMMARY_PATH,
        IF08_W1_CONTROLLED_REPORT_PATH,
        IF08_W1_CONTROLLED_MATRIX_PATH,
        IF08_W1_CONTROLLED_ORACLE_PATH,
        IF08_W1_CONTROLLED_LEDGER_PATH,
        IF08_W1_CONTROLLED_BUNDLE_PATH,
        IF08_W1_CONTROLLED_NO_REAL_EXECUTION_PATH,
        IF08_W1_CONTROLLED_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W1_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W1 controlled decision must be pass")
    _require(decision.get("status") == IF08_W1_CONTROLLED_STATUS, "project W1 controlled decision status mismatch")
    _require(decision.get("source_phase") == IF08_W1_PREFLIGHT_PHASE, "project W1 controlled decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W1_PREFLIGHT_STATUS, "project W1 controlled decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W1_PREFLIGHT_PROJECT_SHA, "project W1 controlled decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W1_PREFLIGHT_CI_STATE, "project W1 controlled decision source ci state mismatch")
    _require(decision.get("w1_wave", {}).get("wave_id") == "W1", "project W1 controlled decision wave_id mismatch")
    _require(decision.get("context_integrity_violations_expected") == 10, "project W1 controlled decision expected violations must be 10")
    _require(decision.get("context_integrity_violations_blocked") == 10, "project W1 controlled decision blocked violations must be 10")
    _require(decision.get("cir_required") == 1.0, "project W1 controlled decision cir_required must be 1.0")
    _require(decision.get("cir_observed") == 1.0, "project W1 controlled decision cir_observed must be 1.0")
    _require(decision.get("undetected_context_integrity_violations") == [], "project W1 controlled decision undetected violations must be empty")
    _require(decision.get("detection_matrix_created") is True, "project W1 controlled decision must create detection matrix")
    _require(decision.get("oracle_results_created") is True, "project W1 controlled decision must create oracle results")
    _require(decision.get("execution_ledger_created") is True, "project W1 controlled decision must create execution ledger")
    _require(decision.get("evidence_bundle_manifest_created") is True, "project W1 controlled decision must create evidence manifest")
    _require(decision.get("no_real_execution_attestation_created") is True, "project W1 controlled decision must create no real execution attestation")
    _require(decision.get("runtime_executed") is False, "project W1 controlled decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W1 controlled decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W1 controlled decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W1 controlled decision secrets_accessed must be false")
    _require(decision.get("mcp_activated") is False, "project W1 controlled decision mcp_activated must be false")
    _require(decision.get("rag_ingestion_executed") is False, "project W1 controlled decision rag_ingestion_executed must be false")
    _require(decision.get("memory_write_executed") is False, "project W1 controlled decision memory_write_executed must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W1 controlled decision external_network_used_except_github_governance must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W1 controlled decision dependency_or_package_manager_used must be false")
    _require(decision.get("next_recommended_step") == "sync_if08_w1_context_memory_rag_controlled_execution_into_active_context", "project W1 controlled decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W1 controlled decision blocking_findings must be empty")

    summary = _load_json(IF08_W1_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W1 controlled summary must be pass")
    _require(summary.get("status") == IF08_W1_CONTROLLED_STATUS, "project W1 controlled summary status mismatch")
    _require(summary.get("source_phase") == IF08_W1_PREFLIGHT_PHASE, "project W1 controlled summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W1_PREFLIGHT_STATUS, "project W1 controlled summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W1_PREFLIGHT_PROJECT_SHA, "project W1 controlled summary project sha mismatch")
    _require(summary.get("project_ci_state") == IF08_W1_PREFLIGHT_CI_STATE, "project W1 controlled summary ci state mismatch")
    _require(summary.get("context_integrity_violations_expected") == 10, "project W1 controlled summary expected violations must be 10")
    _require(summary.get("context_integrity_violations_blocked") == 10, "project W1 controlled summary blocked violations must be 10")
    _require(summary.get("cir_required") == 1.0, "project W1 controlled summary cir_required must be 1.0")
    _require(summary.get("cir_observed") == 1.0, "project W1 controlled summary cir_observed must be 1.0")
    _require(summary.get("undetected_context_integrity_violations") == [], "project W1 controlled summary undetected violations must be empty")
    _require(summary.get("next_recommended_step") == "sync_if08_w1_context_memory_rag_controlled_execution_into_active_context", "project W1 controlled summary next step mismatch")

    matrix = _load_json(IF08_W1_CONTROLLED_MATRIX_PATH)
    _require(matrix.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled matrix phase_id mismatch")
    _require(matrix.get("wave_id") == "W1", "project W1 controlled matrix wave_id mismatch")
    _require(matrix.get("context_integrity_violations_expected") == 10, "project W1 controlled matrix expected violations must be 10")
    _require(matrix.get("context_integrity_violations_blocked") == 10, "project W1 controlled matrix blocked violations must be 10")
    _require(matrix.get("cir_observed") == 1.0, "project W1 controlled matrix cir_observed must be 1.0")
    _require(len(matrix.get("scenarios", [])) == 10, "project W1 controlled matrix must contain 10 scenarios")
    _require(all(row.get("blocked") is True for row in matrix.get("scenarios", [])), "project W1 controlled matrix must block every scenario")

    oracle = _load_json(IF08_W1_CONTROLLED_ORACLE_PATH)
    _require(oracle.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled oracle phase_id mismatch")
    _require(len(oracle.get("oracles", [])) == 10, "project W1 controlled oracle must contain 10 rows")

    ledger = _load_jsonl(IF08_W1_CONTROLLED_LEDGER_PATH)
    _require(ledger[0].get("event_type") == "phase_start", "project W1 controlled ledger must start with phase_start")
    _require(ledger[-1].get("event_type") == "phase_verdict", "project W1 controlled ledger must end with phase_verdict")
    _require(ledger[-1].get("cir_observed") == 1.0, "project W1 controlled ledger cir_observed must be 1.0")

    bundle = _load_json(IF08_W1_CONTROLLED_BUNDLE_PATH)
    _require(bundle.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled bundle phase_id mismatch")
    _require(bundle.get("entry_count") == len(bundle.get("entries", [])), "project W1 controlled bundle entry_count mismatch")
    _require(bundle.get("entry_count", 0) >= 8, "project W1 controlled bundle must contain at least 8 entries")

    no_real_execution = _load_json(IF08_W1_CONTROLLED_NO_REAL_EXECUTION_PATH)
    _require(no_real_execution.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-CONTROLLED-EXECUTION", "project W1 controlled no real execution phase_id mismatch")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(no_real_execution.get(key) is False, f"project W1 controlled no real execution {key} must be false")


def _check_if08_w1_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W1_POST_SYNC_ACTIVE_DECISION_PATH,
        IF08_W1_POST_SYNC_ACTIVE_SUMMARY_PATH,
        IF08_W1_POST_SYNC_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W1 post-sync review active-context artifact: {path}")

    active_decision = _load_json(IF08_W1_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "active W1 post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W1 post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W1_POST_SYNC_STATUS, "active W1 post-sync decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W1_POST_SYNC_PROJECT_SHA, "active W1 post-sync decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W1_POST_SYNC_CI_STATE, "active W1 post-sync decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W1_POST_SYNC_PROJECT_CI_RUN_URL, "active W1 post-sync decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W1 post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W1 post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W1 post-sync decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W1 post-sync decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w1_post_sync_review") is True, "active W1 post-sync decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W1_POST_SYNC_PHASE, "active W1 post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W1_POST_SYNC_STATUS, "active W1 post-sync decision latest status mismatch")
    _require(active_decision.get("w1_canonical_sync_verified") is True, "active W1 post-sync decision must verify W1 canonical sync")
    _require(active_decision.get("w1_cir_observed") == 1.0, "active W1 post-sync decision w1_cir_observed must be 1.0")
    _require(active_decision.get("w1_context_integrity_violations_expected") == 10, "active W1 post-sync decision expected violations must be 10")
    _require(active_decision.get("w1_context_integrity_violations_blocked") == 10, "active W1 post-sync decision blocked violations must be 10")
    _require(active_decision.get("w1_undetected_violations") == [], "active W1 post-sync decision undetected violations must be empty")
    _require(active_decision.get("w1_synthetic_isolated_only") is True, "active W1 post-sync decision must preserve synthetic isolated only")
    _require(active_decision.get("w2_readiness_state") == "ready_for_preparation", "active W1 post-sync decision readiness state mismatch")
    _require(active_decision.get("w2_preparation_allowed_next") is True, "active W1 post-sync decision must allow W2 preparation")
    _require(active_decision.get("w2_execution_performed") is False, "active W1 post-sync decision w2_execution_performed must be false")
    _require(active_decision.get("w2_execution_allowed") is False, "active W1 post-sync decision w2_execution_allowed must be false")
    _require(active_decision.get("future_far_required") == 0, "active W1 post-sync decision future_far_required must be 0")
    _require(active_decision.get("future_ctl_required") == 0, "active W1 post-sync decision future_ctl_required must be 0")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W1 post-sync decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 8, "active W1 post-sync decision required_preflight_checks must be 8")
    _require(active_decision.get("ready_preflight_checks") == 8, "active W1 post-sync decision ready_preflight_checks must be 8")
    _require(active_decision.get("next_recommended_step") == IF08_W1_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W1 post-sync decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W1 post-sync decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W1_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "active W1 post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W1 post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W1_POST_SYNC_STATUS, "active W1 post-sync summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W1_POST_SYNC_PHASE, "active W1 post-sync summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W1_POST_SYNC_STATUS, "active W1 post-sync summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W1_POST_SYNC_PROJECT_SHA, "active W1 post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W1_POST_SYNC_CI_STATE, "active W1 post-sync summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W1_POST_SYNC_PROJECT_CI_RUN_URL, "active W1 post-sync summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W1 post-sync summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w1_post_sync_review") is True, "active W1 post-sync summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W1 post-sync summary must preserve permanent rule")
    _require(active_summary.get("w1_canonical_sync_verified") is True, "active W1 post-sync summary must verify W1 canonical sync")
    _require(active_summary.get("w1_cir_observed") == 1.0, "active W1 post-sync summary w1_cir_observed must be 1.0")
    _require(active_summary.get("w2_readiness_state") == "ready_for_preparation", "active W1 post-sync summary readiness state mismatch")
    _require(active_summary.get("w2_preparation_allowed_next") is True, "active W1 post-sync summary must allow W2 preparation")
    _require(active_summary.get("w2_execution_allowed") is False, "active W1 post-sync summary must keep execution disallowed")
    _require(active_summary.get("future_far_required") == 0, "active W1 post-sync summary future_far_required must be 0")
    _require(active_summary.get("future_ctl_required") == 0, "active W1 post-sync summary future_ctl_required must be 0")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W1 post-sync summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 8, "active W1 post-sync summary required_preflight_checks must be 8")
    _require(active_summary.get("ready_preflight_checks") == 8, "active W1 post-sync summary ready_preflight_checks must be 8")
    _require(active_summary.get("next_recommended_step") == IF08_W1_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W1 post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W1_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W1 Controlled Execution Post-Sync Review & W2 Readiness Decision",
        IF08_W1_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w1_post_sync_review: `true`",
        "w1_canonical_sync_verified: `true`",
        "w2_preparation_allowed_next: `true`",
        "next_recommended_step: `prepare_if08_w2_auth_hitl_identity_exfil_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W1_POST_SYNC_DECISION_PATH,
        IF08_W1_POST_SYNC_SUMMARY_PATH,
        IF08_W1_POST_SYNC_REPORT_PATH,
        IF08_W2_READINESS_MATRIX_PATH,
        IF08_W1_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W1_POST_SYNC_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W1_POST_SYNC_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "project W1 post-sync decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W1 post-sync decision must be pass")
    _require(decision.get("status") == IF08_W1_POST_SYNC_STATUS, "project W1 post-sync decision status mismatch")
    _require(decision.get("source_phase") == IF08_W1_CONTROLLED_PHASE, "project W1 post-sync decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W1_CONTROLLED_STATUS, "project W1 post-sync decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W1_CONTROLLED_PROJECT_SHA, "project W1 post-sync decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W1_CONTROLLED_CI_STATE, "project W1 post-sync decision source ci state mismatch")
    _require(decision.get("w1_canonical_sync_verified") is True, "project W1 post-sync decision must verify W1 canonical sync")
    _require(decision.get("w1_cir_observed") == 1.0, "project W1 post-sync decision w1_cir_observed must be 1.0")
    _require(decision.get("w1_context_integrity_violations_expected") == 10, "project W1 post-sync decision expected violations must be 10")
    _require(decision.get("w1_context_integrity_violations_blocked") == 10, "project W1 post-sync decision blocked violations must be 10")
    _require(decision.get("w1_undetected_violations") == [], "project W1 post-sync decision undetected violations must be empty")
    _require(decision.get("w1_synthetic_isolated_only") is True, "project W1 post-sync decision must preserve synthetic isolated only")
    _require(decision.get("w2_readiness_state") == "ready_for_preparation", "project W1 post-sync decision readiness state mismatch")
    _require(decision.get("w2_preparation_allowed_next") is True, "project W1 post-sync decision must allow W2 preparation")
    _require(decision.get("w2_execution_performed") is False, "project W1 post-sync decision w2_execution_performed must be false")
    _require(decision.get("w2_execution_allowed") is False, "project W1 post-sync decision w2_execution_allowed must be false")
    _require(decision.get("future_far_required") == 0, "project W1 post-sync decision future_far_required must be 0")
    _require(decision.get("future_ctl_required") == 0, "project W1 post-sync decision future_ctl_required must be 0")
    _require(decision.get("readiness_coverage") == 1.0, "project W1 post-sync decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 8, "project W1 post-sync decision required_preflight_checks must be 8")
    _require(decision.get("ready_preflight_checks") == 8, "project W1 post-sync decision ready_preflight_checks must be 8")
    _require(decision.get("runtime_executed") is False, "project W1 post-sync decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W1 post-sync decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W1 post-sync decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W1 post-sync decision secrets_accessed must be false")
    _require(decision.get("mcp_activated") is False, "project W1 post-sync decision mcp_activated must be false")
    _require(decision.get("rag_ingestion_executed") is False, "project W1 post-sync decision rag_ingestion_executed must be false")
    _require(decision.get("memory_write_executed") is False, "project W1 post-sync decision memory_write_executed must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W1 post-sync decision external_network_used_except_github_governance must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W1 post-sync decision dependency_or_package_manager_used must be false")
    _require(decision.get("next_recommended_step") == IF08_W1_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W1 post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W1 post-sync decision blocking_findings must be empty")

    summary = _load_json(IF08_W1_POST_SYNC_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "project W1 post-sync summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W1 post-sync summary must be pass")
    _require(summary.get("status") == IF08_W1_POST_SYNC_STATUS, "project W1 post-sync summary status mismatch")
    _require(summary.get("source_phase") == IF08_W1_CONTROLLED_PHASE, "project W1 post-sync summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W1_CONTROLLED_STATUS, "project W1 post-sync summary source status mismatch")
    _require(summary.get("source_project_sha") == IF08_W1_CONTROLLED_PROJECT_SHA, "project W1 post-sync summary source project sha mismatch")
    _require(summary.get("source_ci_state") == IF08_W1_CONTROLLED_CI_STATE, "project W1 post-sync summary source ci state mismatch")
    _require(summary.get("w1_canonical_sync_verified") is True, "project W1 post-sync summary must verify W1 canonical sync")
    _require(summary.get("w1_cir_observed") == 1.0, "project W1 post-sync summary w1_cir_observed must be 1.0")
    _require(summary.get("w2_readiness_state") == "ready_for_preparation", "project W1 post-sync summary readiness state mismatch")
    _require(summary.get("w2_preparation_allowed_next") is True, "project W1 post-sync summary must allow W2 preparation")
    _require(summary.get("w2_execution_allowed") is False, "project W1 post-sync summary execution allowed must remain false")
    _require(summary.get("future_far_required") == 0, "project W1 post-sync summary future_far_required must be 0")
    _require(summary.get("future_ctl_required") == 0, "project W1 post-sync summary future_ctl_required must be 0")
    _require(summary.get("readiness_coverage") == 1.0, "project W1 post-sync summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 8, "project W1 post-sync summary required_preflight_checks must be 8")
    _require(summary.get("ready_preflight_checks") == 8, "project W1 post-sync summary ready_preflight_checks must be 8")
    _require(summary.get("next_recommended_step") == IF08_W1_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W1 post-sync summary next step mismatch")

    readiness = _load_json(IF08_W2_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "project W2 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W2", "project W2 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Auth/HITL/identity/exfil", "project W2 readiness wave_name mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project W2 readiness state mismatch")
    _require(readiness.get("w2_execution_performed") is False, "project W2 readiness must keep execution false")
    _require(readiness.get("w2_execution_allowed") is False, "project W2 readiness must keep execution disallowed")
    _require(readiness.get("future_far_required") == 0, "project W2 readiness future_far_required must be 0")
    _require(readiness.get("future_ctl_required") == 0, "project W2 readiness future_ctl_required must be 0")
    _require(readiness.get("readiness_coverage") == 1.0, "project W2 readiness readiness_coverage must be 1.0")
    _require(readiness.get("required_preflight_checks") == 8, "project W2 readiness required_preflight_checks must be 8")
    _require(readiness.get("ready_preflight_checks") == 8, "project W2 readiness ready_preflight_checks must be 8")
    checks = {item.get("check_id"): item.get("passed") for item in readiness.get("checks", [])}
    _require(checks.get("w2_execution_not_performed") is True, "project W2 readiness must keep execution not performed")
    _require(checks.get("w2_execution_not_allowed") is True, "project W2 readiness must keep execution not allowed")
    _require(checks.get("next_step_points_to_w2_preflight_preparation") is True, "project W2 readiness must point to W2 preflight preparation")

    no_execution = _load_json(IF08_W1_POST_SYNC_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W1-POST-SYNC-REVIEW", "project W1 post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W1 post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W1_POST_SYNC_STATUS, "project W1 post-sync no_execution status mismatch")
    _require(no_execution.get("w2_execution_performed") is False, "project W1 post-sync no_execution must keep execution false")
    _require(no_execution.get("w2_execution_allowed") is False, "project W1 post-sync no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_execution.get(key) is False, f"project W1 post-sync no_execution.{key} must be false")


def _check_if08_w2_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W2_CONTROLLED_ACTIVE_DECISION_PATH,
        IF08_W2_CONTROLLED_ACTIVE_SUMMARY_PATH,
        IF08_W2_CONTROLLED_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W2 controlled active-context artifact: {path}")

    active_decision = _load_json(IF08_W2_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "active W2 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W2 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W2_CONTROLLED_STATUS, "active W2 controlled decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W2_CONTROLLED_PROJECT_SHA, "active W2 controlled decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W2_CONTROLLED_CI_STATE, "active W2 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W2_CONTROLLED_PROJECT_CI_RUN_URL, "active W2 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W2 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W2 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W2 controlled decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W2 controlled decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_controlled_execution") is True, "active W2 controlled decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W2_CONTROLLED_PHASE, "active W2 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W2_CONTROLLED_STATUS, "active W2 controlled decision latest status mismatch")
    _require(active_decision.get("attack_attempts_expected") == 12, "active W2 controlled decision attack_attempts_expected must be 12")
    _require(active_decision.get("attack_attempts_blocked") == 12, "active W2 controlled decision attack_attempts_blocked must be 12")
    _require(active_decision.get("far_observed") == 0, "active W2 controlled decision far_observed must be 0")
    _require(active_decision.get("ctl_observed") == 0, "active W2 controlled decision ctl_observed must be 0")
    _require(active_decision.get("false_approval_acceptance_count") == 0, "active W2 controlled decision false_approval_acceptance_count must be 0")
    _require(active_decision.get("confidential_token_or_tenant_leak_count") == 0, "active W2 controlled decision confidential_token_or_tenant_leak_count must be 0")
    _require(active_decision.get("w2_execution_performed") is True, "active W2 controlled decision must record execution performed")
    _require(active_decision.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W2 controlled decision wave_executed mismatch")
    _require(active_decision.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W2 controlled decision bot_executed mismatch")
    _require(active_decision.get("w2_execution_allowed") is False, "active W2 controlled decision must keep execution disallowed")
    _require(active_decision.get("next_recommended_step") == IF08_W2_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W2 controlled decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W2 controlled decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W2_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "active W2 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W2 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W2_CONTROLLED_STATUS, "active W2 controlled summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W2_CONTROLLED_PHASE, "active W2 controlled summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W2_CONTROLLED_STATUS, "active W2 controlled summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W2_CONTROLLED_PROJECT_SHA, "active W2 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W2_CONTROLLED_CI_STATE, "active W2 controlled summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W2_CONTROLLED_PROJECT_CI_RUN_URL, "active W2 controlled summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W2 controlled summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_controlled_execution") is True, "active W2 controlled summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W2 controlled summary must preserve permanent rule")
    _require(active_summary.get("attack_attempts_expected") == 12, "active W2 controlled summary attack_attempts_expected must be 12")
    _require(active_summary.get("attack_attempts_blocked") == 12, "active W2 controlled summary attack_attempts_blocked must be 12")
    _require(active_summary.get("far_observed") == 0, "active W2 controlled summary far_observed must be 0")
    _require(active_summary.get("ctl_observed") == 0, "active W2 controlled summary ctl_observed must be 0")
    _require(active_summary.get("false_approval_acceptance_count") == 0, "active W2 controlled summary false_approval_acceptance_count must be 0")
    _require(active_summary.get("confidential_token_or_tenant_leak_count") == 0, "active W2 controlled summary confidential_token_or_tenant_leak_count must be 0")
    _require(active_summary.get("w2_execution_performed") is True, "active W2 controlled summary must record execution performed")
    _require(active_summary.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W2 controlled summary wave_executed mismatch")
    _require(active_summary.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W2 controlled summary bot_executed mismatch")
    _require(active_summary.get("next_recommended_step") == IF08_W2_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W2 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W2_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W2 Auth/HITL/Identity/Exfil Controlled Execution",
        IF08_W2_CONTROLLED_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_controlled_execution: `true`",
        "w2_execution_performed: `true_synthetic_isolated_lab_only`",
        "next_recommended_step: `post_sync_review_if08_w2_auth_hitl_identity_exfil_controlled_execution`",
    )

    external_project_paths = (
        IF08_W2_CONTROLLED_DECISION_PATH,
        IF08_W2_CONTROLLED_SUMMARY_PATH,
        IF08_W2_CONTROLLED_REPORT_PATH,
        IF08_W2_CONTROLLED_AUTH_MATRIX_PATH,
        IF08_W2_CONTROLLED_EXFIL_MATRIX_PATH,
        IF08_W2_CONTROLLED_ORACLE_PATH,
        IF08_W2_CONTROLLED_LEDGER_PATH,
        IF08_W2_CONTROLLED_BUNDLE_PATH,
        IF08_W2_CONTROLLED_NO_REAL_EXECUTION_PATH,
        IF08_W2_CONTROLLED_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W2_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W2 controlled decision must be pass")
    _require(decision.get("status") == IF08_W2_CONTROLLED_STATUS, "project W2 controlled decision status mismatch")
    _require(decision.get("source_phase") == IF08_W2_PREFLIGHT_PHASE, "project W2 controlled decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W2_PREFLIGHT_STATUS, "project W2 controlled decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W2_PREFLIGHT_PROJECT_SHA, "project W2 controlled decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W2_PREFLIGHT_CI_STATE, "project W2 controlled decision source ci state mismatch")
    _require(decision.get("w2_wave", {}).get("wave_id") == "W2", "project W2 controlled decision wave_id mismatch")
    _require(decision.get("attack_attempts_expected") == 12, "project W2 controlled decision attack_attempts_expected must be 12")
    _require(decision.get("attack_attempts_blocked") == 12, "project W2 controlled decision attack_attempts_blocked must be 12")
    _require(decision.get("undetected_attack_attempts") == [], "project W2 controlled decision undetected_attack_attempts must be empty")
    _require(decision.get("false_approval_attempt_count") == 9, "project W2 controlled decision false_approval_attempt_count must be 9")
    _require(decision.get("false_approval_acceptance_count") == 0, "project W2 controlled decision false_approval_acceptance_count must be 0")
    _require(decision.get("far_required") == 0, "project W2 controlled decision far_required must be 0")
    _require(decision.get("far_observed") == 0.0, "project W2 controlled decision far_observed must be 0.0")
    _require(decision.get("confidential_token_or_tenant_leak_count") == 0, "project W2 controlled decision confidential_token_or_tenant_leak_count must be 0")
    _require(decision.get("ctl_required") == 0, "project W2 controlled decision ctl_required must be 0")
    _require(decision.get("ctl_observed") == 0, "project W2 controlled decision ctl_observed must be 0")
    _require(len(decision.get("w2_bots_executed", [])) == 4, "project W2 controlled decision must list 4 W2 bots")
    _require(decision.get("synthetic_isolated_lab_only") is True, "project W2 controlled decision must preserve synthetic isolated only")
    _require(decision.get("auth_detection_matrix_created") is True, "project W2 controlled decision must create auth detection matrix")
    _require(decision.get("exfil_detection_matrix_created") is True, "project W2 controlled decision must create exfil detection matrix")
    _require(decision.get("oracle_results_created") is True, "project W2 controlled decision must create oracle results")
    _require(decision.get("execution_ledger_created") is True, "project W2 controlled decision must create execution ledger")
    _require(decision.get("evidence_bundle_manifest_created") is True, "project W2 controlled decision must create evidence bundle manifest")
    _require(decision.get("no_real_execution_attestation_created") is True, "project W2 controlled decision must create no real execution attestation")
    _require(decision.get("runtime_executed") is False, "project W2 controlled decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W2 controlled decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W2 controlled decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W2 controlled decision secrets_accessed must be false")
    _require(decision.get("mcp_activated") is False, "project W2 controlled decision mcp_activated must be false")
    _require(decision.get("rag_ingestion_executed") is False, "project W2 controlled decision rag_ingestion_executed must be false")
    _require(decision.get("memory_write_executed") is False, "project W2 controlled decision memory_write_executed must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W2 controlled decision external_network_used_except_github_governance must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W2 controlled decision dependency_or_package_manager_used must be false")
    _require(decision.get("next_recommended_step") == "sync_if08_w2_auth_hitl_identity_exfil_controlled_execution_into_active_context", "project W2 controlled decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W2 controlled decision blocking_findings must be empty")

    summary = _load_json(IF08_W2_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W2 controlled summary must be pass")
    _require(summary.get("status") == IF08_W2_CONTROLLED_STATUS, "project W2 controlled summary status mismatch")
    _require(summary.get("source_phase") == IF08_W2_PREFLIGHT_PHASE, "project W2 controlled summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W2_PREFLIGHT_STATUS, "project W2 controlled summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W2_PREFLIGHT_PROJECT_SHA, "project W2 controlled summary project sha mismatch")
    _require(summary.get("project_ci_state") == IF08_W2_PREFLIGHT_CI_STATE, "project W2 controlled summary ci state mismatch")
    _require(summary.get("attack_attempts_expected") == 12, "project W2 controlled summary attack_attempts_expected must be 12")
    _require(summary.get("attack_attempts_blocked") == 12, "project W2 controlled summary attack_attempts_blocked must be 12")
    _require(summary.get("far_required") == 0, "project W2 controlled summary far_required must be 0")
    _require(summary.get("far_observed") == 0.0, "project W2 controlled summary far_observed must be 0.0")
    _require(summary.get("ctl_required") == 0, "project W2 controlled summary ctl_required must be 0")
    _require(summary.get("ctl_observed") == 0, "project W2 controlled summary ctl_observed must be 0")
    _require(summary.get("false_approval_attempt_count") == 9, "project W2 controlled summary false_approval_attempt_count must be 9")
    _require(summary.get("false_approval_acceptance_count") == 0, "project W2 controlled summary false_approval_acceptance_count must be 0")
    _require(summary.get("confidential_token_or_tenant_leak_count") == 0, "project W2 controlled summary confidential_token_or_tenant_leak_count must be 0")
    _require(summary.get("undetected_attack_attempts") == [], "project W2 controlled summary undetected_attack_attempts must be empty")
    _require(len(summary.get("w2_bots_executed", [])) == 4, "project W2 controlled summary must list 4 W2 bots")
    _require(summary.get("next_recommended_step") == "sync_if08_w2_auth_hitl_identity_exfil_controlled_execution_into_active_context", "project W2 controlled summary next step mismatch")

    auth_matrix = _load_json(IF08_W2_CONTROLLED_AUTH_MATRIX_PATH)
    _require(auth_matrix.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled auth matrix phase_id mismatch")
    _require(auth_matrix.get("false_approval_attempt_count") == 9, "project W2 controlled auth matrix false_approval_attempt_count must be 9")
    _require(auth_matrix.get("false_approval_acceptance_count") == 0, "project W2 controlled auth matrix false_approval_acceptance_count must be 0")
    _require(auth_matrix.get("far_observed") == 0.0, "project W2 controlled auth matrix far_observed must be 0.0")
    _require(len(auth_matrix.get("rows", [])) == 9, "project W2 controlled auth matrix must contain 9 rows")
    _require(all(row.get("blocked") is True for row in auth_matrix.get("rows", [])), "project W2 controlled auth matrix must block every row")

    exfil_matrix = _load_json(IF08_W2_CONTROLLED_EXFIL_MATRIX_PATH)
    _require(exfil_matrix.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled exfil matrix phase_id mismatch")
    _require(exfil_matrix.get("confidential_token_or_tenant_leak_count") == 0, "project W2 controlled exfil matrix confidential_token_or_tenant_leak_count must be 0")
    _require(exfil_matrix.get("ctl_observed") == 0, "project W2 controlled exfil matrix ctl_observed must be 0")
    _require(len(exfil_matrix.get("rows", [])) == 3, "project W2 controlled exfil matrix must contain 3 rows")
    _require(all(row.get("blocked") is True for row in exfil_matrix.get("rows", [])), "project W2 controlled exfil matrix must block every row")

    oracle = _load_json(IF08_W2_CONTROLLED_ORACLE_PATH)
    _require(oracle.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled oracle phase_id mismatch")
    _require(len(oracle.get("oracles", [])) == 12, "project W2 controlled oracle must contain 12 rows")

    ledger = _load_jsonl(IF08_W2_CONTROLLED_LEDGER_PATH)
    _require(ledger[0].get("event_type") == "phase_start", "project W2 controlled ledger must start with phase_start")
    _require(ledger[-1].get("event_type") == "phase_verdict", "project W2 controlled ledger must end with phase_verdict")
    _require(ledger[-1].get("far_observed") == 0.0, "project W2 controlled ledger far_observed must be 0.0")
    _require(ledger[-1].get("ctl_observed") == 0, "project W2 controlled ledger ctl_observed must be 0")

    bundle = _load_json(IF08_W2_CONTROLLED_BUNDLE_PATH)
    _require(bundle.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled bundle phase_id mismatch")
    _require(bundle.get("entry_count") == len(bundle.get("entries", [])), "project W2 controlled bundle entry_count mismatch")
    _require(bundle.get("entry_count", 0) >= 9, "project W2 controlled bundle must contain at least 9 entries")

    no_real_execution = _load_json(IF08_W2_CONTROLLED_NO_REAL_EXECUTION_PATH)
    _require(no_real_execution.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-CONTROLLED-EXECUTION", "project W2 controlled no real execution phase_id mismatch")
    _require(no_real_execution.get("w2_execution_performed") is True, "project W2 controlled no real execution must record execution performed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(no_real_execution.get(key) is False, f"project W2 controlled no real execution {key} must be false")


def _check_if08_w3_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W3_CONTROLLED_ACTIVE_DECISION_PATH,
        IF08_W3_CONTROLLED_ACTIVE_SUMMARY_PATH,
        IF08_W3_CONTROLLED_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W3 controlled active-context artifact: {path}")

    active_decision = _load_json(IF08_W3_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "active W3 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W3 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W3_CONTROLLED_STATUS, "active W3 controlled decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W3_CONTROLLED_PROJECT_SHA, "active W3 controlled decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W3_CONTROLLED_CI_STATE, "active W3 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W3_CONTROLLED_PROJECT_CI_RUN_URL, "active W3 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W3 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W3 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W3 controlled decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W3 controlled decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_controlled_execution") is True, "active W3 controlled decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W3_CONTROLLED_PHASE, "active W3 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W3_CONTROLLED_STATUS, "active W3 controlled decision latest status mismatch")
    _require(active_decision.get("attack_attempts_expected") == 13, "active W3 controlled decision attack_attempts_expected must be 13")
    _require(active_decision.get("attack_attempts_blocked") == 13, "active W3 controlled decision attack_attempts_blocked must be 13")
    _require(active_decision.get("ser_observed") == 0, "active W3 controlled decision ser_observed must be 0")
    _require(active_decision.get("rca_observed") == 1.0, "active W3 controlled decision rca_observed must be 1.0")
    _require(active_decision.get("sandbox_escape_attempt_count") == 3, "active W3 controlled decision sandbox_escape_attempt_count must be 3")
    _require(active_decision.get("sandbox_escape_count") == 0, "active W3 controlled decision sandbox_escape_count must be 0")
    _require(active_decision.get("runtime_containment_checks_required") == 13, "active W3 controlled decision runtime_containment_checks_required must be 13")
    _require(active_decision.get("runtime_containment_checks_passed") == 13, "active W3 controlled decision runtime_containment_checks_passed must be 13")
    _require(active_decision.get("sirene_status") == "conditional_or_deferred_with_reason", "active W3 controlled decision sirene_status mismatch")
    _require(bool(active_decision.get("sirene_reason")), "active W3 controlled decision sirene_reason missing")
    _require(active_decision.get("w3_execution_performed") is True, "active W3 controlled decision must record execution performed")
    _require(active_decision.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W3 controlled decision wave_executed mismatch")
    _require(active_decision.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W3 controlled decision bot_executed mismatch")
    _require(active_decision.get("w3_execution_allowed") is False, "active W3 controlled decision must keep execution disallowed")
    _require(active_decision.get("next_recommended_step") == IF08_W3_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W3 controlled decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
    ):
        _require(active_outcome.get(key) is False, f"active W3 controlled decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W3_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "active W3 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W3 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W3_CONTROLLED_STATUS, "active W3 controlled summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W3_CONTROLLED_PHASE, "active W3 controlled summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W3_CONTROLLED_STATUS, "active W3 controlled summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W3_CONTROLLED_PROJECT_SHA, "active W3 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W3_CONTROLLED_CI_STATE, "active W3 controlled summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W3_CONTROLLED_PROJECT_CI_RUN_URL, "active W3 controlled summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W3 controlled summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_controlled_execution") is True, "active W3 controlled summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W3 controlled summary must preserve permanent rule")
    _require(active_summary.get("attack_attempts_expected") == 13, "active W3 controlled summary attack_attempts_expected must be 13")
    _require(active_summary.get("attack_attempts_blocked") == 13, "active W3 controlled summary attack_attempts_blocked must be 13")
    _require(active_summary.get("ser_observed") == 0, "active W3 controlled summary ser_observed must be 0")
    _require(active_summary.get("rca_observed") == 1.0, "active W3 controlled summary rca_observed must be 1.0")
    _require(active_summary.get("w3_execution_performed") is True, "active W3 controlled summary must record execution performed")
    _require(active_summary.get("wave_executed") == "true_synthetic_isolated_lab_only", "active W3 controlled summary wave_executed mismatch")
    _require(active_summary.get("bot_executed") == "true_synthetic_isolated_lab_only", "active W3 controlled summary bot_executed mismatch")
    _require(active_summary.get("sirene_status") == "conditional_or_deferred_with_reason", "active W3 controlled summary sirene_status mismatch")
    _require(active_summary.get("next_recommended_step") == IF08_W3_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W3 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W3_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W3 Runtime/Tool/MCP/Sandbox Controlled Execution",
        IF08_W3_CONTROLLED_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_controlled_execution: `true`",
        "w3_execution_performed: `true_synthetic_isolated_lab_only`",
        "next_recommended_step: `post_sync_review_if08_w3_runtime_tool_mcp_sandbox_controlled_execution`",
    )

    external_project_paths = (
        IF08_W3_CONTROLLED_DECISION_PATH,
        IF08_W3_CONTROLLED_SUMMARY_PATH,
        IF08_W3_CONTROLLED_REPORT_PATH,
        IF08_W3_CONTROLLED_RUNTIME_MATRIX_PATH,
        IF08_W3_CONTROLLED_TOOL_MATRIX_PATH,
        IF08_W3_CONTROLLED_ORACLE_PATH,
        IF08_W3_CONTROLLED_LEDGER_PATH,
        IF08_W3_CONTROLLED_BUNDLE_PATH,
        IF08_W3_CONTROLLED_SIRENE_RECORD_PATH,
        IF08_W3_CONTROLLED_NO_REAL_EXECUTION_PATH,
        IF08_W3_CONTROLLED_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W3_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W3 controlled decision must be pass")
    _require(decision.get("status") == IF08_W3_CONTROLLED_STATUS, "project W3 controlled decision status mismatch")
    _require(decision.get("source_phase") == IF08_W3_PREFLIGHT_PHASE, "project W3 controlled decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W3_PREFLIGHT_STATUS, "project W3 controlled decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W3_PREFLIGHT_PROJECT_SHA, "project W3 controlled decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W3_PREFLIGHT_CI_STATE, "project W3 controlled decision source ci state mismatch")
    _require(decision.get("w3_wave", {}).get("wave_id") == "W3", "project W3 controlled decision wave_id mismatch")
    _require(decision.get("attack_attempts_expected") == 13, "project W3 controlled decision attack_attempts_expected must be 13")
    _require(decision.get("attack_attempts_blocked") == 13, "project W3 controlled decision attack_attempts_blocked must be 13")
    _require(decision.get("undetected_runtime_sandbox_attacks") == [], "project W3 controlled decision undetected_runtime_sandbox_attacks must be empty")
    _require(decision.get("sandbox_escape_attempt_count") == 3, "project W3 controlled decision sandbox_escape_attempt_count must be 3")
    _require(decision.get("sandbox_escape_count") == 0, "project W3 controlled decision sandbox_escape_count must be 0")
    _require(decision.get("ser_required") == 0, "project W3 controlled decision ser_required must be 0")
    _require(decision.get("ser_observed") == 0.0, "project W3 controlled decision ser_observed must be 0.0")
    _require(decision.get("runtime_containment_checks_required") == 13, "project W3 controlled decision runtime_containment_checks_required must be 13")
    _require(decision.get("runtime_containment_checks_passed") == 13, "project W3 controlled decision runtime_containment_checks_passed must be 13")
    _require(decision.get("rca_required") == 1.0, "project W3 controlled decision rca_required must be 1.0")
    _require(decision.get("rca_observed") == 1.0, "project W3 controlled decision rca_observed must be 1.0")
    _require(len(decision.get("w3_bots_executed", [])) == 4, "project W3 controlled decision must list 4 W3 bots")
    _require(decision.get("w3_execution_performed") is True, "project W3 controlled decision must record execution performed")
    _require(decision.get("synthetic_isolated_lab_only") is True, "project W3 controlled decision must preserve synthetic isolated only")
    _require(decision.get("runtime_sandbox_detection_matrix_created") is True, "project W3 controlled decision must create runtime matrix")
    _require(decision.get("tool_mcp_detection_matrix_created") is True, "project W3 controlled decision must create tool matrix")
    _require(decision.get("oracle_results_created") is True, "project W3 controlled decision must create oracle results")
    _require(decision.get("execution_ledger_created") is True, "project W3 controlled decision must create execution ledger")
    _require(decision.get("evidence_bundle_manifest_created") is True, "project W3 controlled decision must create evidence bundle manifest")
    _require(decision.get("sirene_conditional_execution_record_created") is True, "project W3 controlled decision must create Sirene record")
    _require(decision.get("no_real_execution_attestation_created") is True, "project W3 controlled decision must create no real execution attestation")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(decision.get(key) is False, f"project W3 controlled decision {key} must be false")
    _require(decision.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 controlled decision sirene_status mismatch")
    _require(bool(decision.get("sirene_reason")), "project W3 controlled decision sirene_reason missing")
    _require(decision.get("next_recommended_step") == "post_sync_review_if08_w3_runtime_tool_mcp_sandbox_controlled_execution", "project W3 controlled decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W3 controlled decision blocking_findings must be empty")

    summary = _load_json(IF08_W3_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W3 controlled summary must be pass")
    _require(summary.get("status") == IF08_W3_CONTROLLED_STATUS, "project W3 controlled summary status mismatch")
    _require(summary.get("source_phase") == IF08_W3_PREFLIGHT_PHASE, "project W3 controlled summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W3_PREFLIGHT_STATUS, "project W3 controlled summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W3_PREFLIGHT_PROJECT_SHA, "project W3 controlled summary source project sha mismatch")
    _require(summary.get("project_ci_state") == IF08_W3_PREFLIGHT_CI_STATE, "project W3 controlled summary ci state mismatch")
    _require(summary.get("attack_attempts_expected") == 13, "project W3 controlled summary attack_attempts_expected must be 13")
    _require(summary.get("attack_attempts_blocked") == 13, "project W3 controlled summary attack_attempts_blocked must be 13")
    _require(summary.get("ser_required") == 0, "project W3 controlled summary ser_required must be 0")
    _require(summary.get("ser_observed") == 0.0, "project W3 controlled summary ser_observed must be 0.0")
    _require(summary.get("rca_required") == 1.0, "project W3 controlled summary rca_required must be 1.0")
    _require(summary.get("rca_observed") == 1.0, "project W3 controlled summary rca_observed must be 1.0")
    _require(summary.get("undetected_runtime_sandbox_attacks") == [], "project W3 controlled summary undetected_runtime_sandbox_attacks must be empty")
    _require(len(summary.get("w3_bots_executed", [])) == 4, "project W3 controlled summary must list 4 W3 bots")
    _require(summary.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 controlled summary sirene_status mismatch")
    _require(summary.get("next_recommended_step") == "post_sync_review_if08_w3_runtime_tool_mcp_sandbox_controlled_execution", "project W3 controlled summary next step mismatch")

    runtime_matrix = _load_json(IF08_W3_CONTROLLED_RUNTIME_MATRIX_PATH)
    _require(runtime_matrix.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled runtime matrix phase_id mismatch")
    _require(runtime_matrix.get("sandbox_escape_attempt_count") == 3, "project W3 controlled runtime matrix sandbox_escape_attempt_count must be 3")
    _require(runtime_matrix.get("sandbox_escape_count") == 0, "project W3 controlled runtime matrix sandbox_escape_count must be 0")
    _require(runtime_matrix.get("ser_observed") == 0.0, "project W3 controlled runtime matrix ser_observed must be 0.0")
    _require(runtime_matrix.get("rca_observed") == 1.0, "project W3 controlled runtime matrix rca_observed must be 1.0")
    _require(len(runtime_matrix.get("rows", [])) == 6, "project W3 controlled runtime matrix must contain 6 rows")
    _require(all(row.get("blocked") is True for row in runtime_matrix.get("rows", [])), "project W3 controlled runtime matrix must block every row")

    tool_matrix = _load_json(IF08_W3_CONTROLLED_TOOL_MATRIX_PATH)
    _require(tool_matrix.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled tool matrix phase_id mismatch")
    _require(tool_matrix.get("tool_or_mcp_attack_attempts") == 7, "project W3 controlled tool matrix must contain 7 attempts")
    _require(tool_matrix.get("tool_or_mcp_attack_blocked") == 7, "project W3 controlled tool matrix must block all 7 attempts")
    _require(len(tool_matrix.get("rows", [])) == 7, "project W3 controlled tool matrix must contain 7 rows")
    _require(all(row.get("blocked") is True for row in tool_matrix.get("rows", [])), "project W3 controlled tool matrix must block every row")

    oracle = _load_json(IF08_W3_CONTROLLED_ORACLE_PATH)
    _require(oracle.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled oracle phase_id mismatch")
    _require(len(oracle.get("oracles", [])) == 13, "project W3 controlled oracle must contain 13 rows")

    ledger = _load_jsonl(IF08_W3_CONTROLLED_LEDGER_PATH)
    _require(ledger[0].get("event_type") == "phase_start", "project W3 controlled ledger must start with phase_start")
    _require(ledger[-1].get("event_type") == "phase_verdict", "project W3 controlled ledger must end with phase_verdict")
    _require(ledger[-1].get("ser_observed") == 0.0, "project W3 controlled ledger ser_observed must be 0.0")
    _require(ledger[-1].get("rca_observed") == 1.0, "project W3 controlled ledger rca_observed must be 1.0")

    bundle = _load_json(IF08_W3_CONTROLLED_BUNDLE_PATH)
    _require(bundle.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled bundle phase_id mismatch")
    _require(bundle.get("entry_count") == len(bundle.get("entries", [])), "project W3 controlled bundle entry_count mismatch")
    _require(bundle.get("entry_count", 0) >= 10, "project W3 controlled bundle must contain at least 10 entries")

    sirene_record = _load_json(IF08_W3_CONTROLLED_SIRENE_RECORD_PATH)
    _require(sirene_record.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled sirene record phase_id mismatch")
    _require(sirene_record.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 controlled sirene record status mismatch")
    _require(bool(sirene_record.get("sirene_reason")), "project W3 controlled sirene record reason missing")
    _require(sirene_record.get("audio_oracle_pack_active") is False, "project W3 controlled sirene record audio_oracle_pack_active must be false")
    _require(sirene_record.get("execution_performed") is False, "project W3 controlled sirene record execution_performed must be false")

    no_real_execution = _load_json(IF08_W3_CONTROLLED_NO_REAL_EXECUTION_PATH)
    _require(no_real_execution.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-CONTROLLED-EXECUTION", "project W3 controlled no real execution phase_id mismatch")
    _require(no_real_execution.get("w3_execution_performed") is True, "project W3 controlled no real execution must record execution performed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(no_real_execution.get(key) is False, f"project W3 controlled no real execution {key} must be false")


def _check_if08_w3_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W3_POST_SYNC_ACTIVE_DECISION_PATH,
        IF08_W3_POST_SYNC_ACTIVE_SUMMARY_PATH,
        IF08_W3_POST_SYNC_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W3 post-sync review active-context artifact: {path}")

    active_decision = _load_json(IF08_W3_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "active W3 post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W3 post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W3_POST_SYNC_STATUS, "active W3 post-sync decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W3_POST_SYNC_PROJECT_SHA, "active W3 post-sync decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W3_POST_SYNC_CI_STATE, "active W3 post-sync decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W3_POST_SYNC_PROJECT_CI_RUN_URL, "active W3 post-sync decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W3 post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W3 post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W3 post-sync decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W3 post-sync decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w3_post_sync_review") is True, "active W3 post-sync decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W3_POST_SYNC_PHASE, "active W3 post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W3_POST_SYNC_STATUS, "active W3 post-sync decision latest status mismatch")
    _require(active_decision.get("w3_canonical_sync_verified") is True, "active W3 post-sync decision must verify W3 canonical sync")
    _require(active_decision.get("w3_ser_observed") == 0, "active W3 post-sync decision w3_ser_observed must be 0")
    _require(active_decision.get("w3_rca_observed") == 1.0, "active W3 post-sync decision w3_rca_observed must be 1.0")
    _require(active_decision.get("w3_attack_attempts_expected") == 13, "active W3 post-sync decision expected attacks must be 13")
    _require(active_decision.get("w3_attack_attempts_blocked") == 13, "active W3 post-sync decision blocked attacks must be 13")
    _require(active_decision.get("w3_undetected_runtime_sandbox_attacks") == [], "active W3 post-sync decision undetected attacks must be empty")
    _require(active_decision.get("w3_synthetic_isolated_only") is True, "active W3 post-sync decision must preserve synthetic isolated only")
    _require(active_decision.get("w4_readiness_state") == "ready_for_preparation", "active W3 post-sync decision readiness state mismatch")
    _require(active_decision.get("w4_preparation_allowed_next") is True, "active W3 post-sync decision must allow W4 preparation")
    _require(active_decision.get("w4_execution_performed") is False, "active W3 post-sync decision w4_execution_performed must be false")
    _require(active_decision.get("w4_execution_allowed") is False, "active W3 post-sync decision w4_execution_allowed must be false")
    _require(active_decision.get("future_rhr_required") == 1.0, "active W3 post-sync decision future_rhr_required must be 1.0")
    _require(active_decision.get("future_ddr_required") == 1.0, "active W3 post-sync decision future_ddr_required must be 1.0")
    _require(active_decision.get("future_cer_required") == 1.0, "active W3 post-sync decision future_cer_required must be 1.0")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W3 post-sync decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 12, "active W3 post-sync decision required_preflight_checks must be 12")
    _require(active_decision.get("ready_preflight_checks") == 12, "active W3 post-sync decision ready_preflight_checks must be 12")
    _require(active_decision.get("next_recommended_step") == IF08_W3_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W3 post-sync decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
    ):
        _require(active_outcome.get(key) is False, f"active W3 post-sync decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W3_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "active W3 post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W3 post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W3_POST_SYNC_STATUS, "active W3 post-sync summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W3_POST_SYNC_PHASE, "active W3 post-sync summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W3_POST_SYNC_STATUS, "active W3 post-sync summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W3_POST_SYNC_PROJECT_SHA, "active W3 post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W3_POST_SYNC_CI_STATE, "active W3 post-sync summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W3_POST_SYNC_PROJECT_CI_RUN_URL, "active W3 post-sync summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W3 post-sync summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w3_post_sync_review") is True, "active W3 post-sync summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W3 post-sync summary must preserve permanent rule")
    _require(active_summary.get("w3_canonical_sync_verified") is True, "active W3 post-sync summary must verify W3 canonical sync")
    _require(active_summary.get("w3_ser_observed") == 0, "active W3 post-sync summary w3_ser_observed must be 0")
    _require(active_summary.get("w3_rca_observed") == 1.0, "active W3 post-sync summary w3_rca_observed must be 1.0")
    _require(active_summary.get("w4_readiness_state") == "ready_for_preparation", "active W3 post-sync summary readiness state mismatch")
    _require(active_summary.get("w4_preparation_allowed_next") is True, "active W3 post-sync summary must allow W4 preparation")
    _require(active_summary.get("w4_execution_performed") is False, "active W3 post-sync summary must keep execution false")
    _require(active_summary.get("w4_execution_allowed") is False, "active W3 post-sync summary must keep execution disallowed")
    _require(active_summary.get("future_rhr_required") == 1.0, "active W3 post-sync summary future_rhr_required must be 1.0")
    _require(active_summary.get("future_ddr_required") == 1.0, "active W3 post-sync summary future_ddr_required must be 1.0")
    _require(active_summary.get("future_cer_required") == 1.0, "active W3 post-sync summary future_cer_required must be 1.0")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W3 post-sync summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 12, "active W3 post-sync summary required_preflight_checks must be 12")
    _require(active_summary.get("ready_preflight_checks") == 12, "active W3 post-sync summary ready_preflight_checks must be 12")
    _require(active_summary.get("next_recommended_step") == IF08_W3_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W3 post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W3_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W3 Controlled Execution Post-Sync Review & W4 Readiness Decision",
        IF08_W3_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w3_post_sync_review: `true`",
        "w4_preparation_allowed_next: `true`",
        "next_recommended_step: `prepare_if08_w4_replay_rollback_concurrency_cost_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W3_POST_SYNC_DECISION_PATH,
        IF08_W3_POST_SYNC_SUMMARY_PATH,
        IF08_W3_POST_SYNC_REPORT_PATH,
        IF08_W4_READINESS_MATRIX_PATH,
        IF08_W3_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W3_POST_SYNC_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W3_POST_SYNC_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "project W3 post-sync decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W3 post-sync decision must be pass")
    _require(decision.get("status") == IF08_W3_POST_SYNC_STATUS, "project W3 post-sync decision status mismatch")
    _require(decision.get("source_phase") == IF08_W3_CONTROLLED_PHASE, "project W3 post-sync decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W3_CONTROLLED_STATUS, "project W3 post-sync decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W3_CONTROLLED_PROJECT_SHA, "project W3 post-sync decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W3_CONTROLLED_CI_STATE, "project W3 post-sync decision source ci state mismatch")
    _require(decision.get("w3_canonical_sync_verified") is True, "project W3 post-sync decision must verify W3 canonical sync")
    _require(decision.get("w3_ser_observed") == 0, "project W3 post-sync decision w3_ser_observed must be 0")
    _require(decision.get("w3_rca_observed") == 1.0, "project W3 post-sync decision w3_rca_observed must be 1.0")
    _require(decision.get("w3_attack_attempts_expected") == 13, "project W3 post-sync decision expected attacks must be 13")
    _require(decision.get("w3_attack_attempts_blocked") == 13, "project W3 post-sync decision blocked attacks must be 13")
    _require(decision.get("w3_undetected_runtime_sandbox_attacks") == [], "project W3 post-sync decision undetected attacks must be empty")
    _require(decision.get("w3_synthetic_isolated_only") is True, "project W3 post-sync decision must preserve synthetic isolated only")
    _require(decision.get("w4_readiness_state") == "ready_for_preparation", "project W3 post-sync decision readiness state mismatch")
    _require(decision.get("w4_preparation_allowed_next") is True, "project W3 post-sync decision must allow W4 preparation")
    _require(decision.get("w4_execution_performed") is False, "project W3 post-sync decision w4_execution_performed must be false")
    _require(decision.get("w4_execution_allowed") is False, "project W3 post-sync decision w4_execution_allowed must be false")
    _require(decision.get("future_rhr_required") == 1.0, "project W3 post-sync decision future_rhr_required must be 1.0")
    _require(decision.get("future_ddr_required") == 1.0, "project W3 post-sync decision future_ddr_required must be 1.0")
    _require(decision.get("future_cer_required") == 1.0, "project W3 post-sync decision future_cer_required must be 1.0")
    _require(decision.get("readiness_coverage") == 1.0, "project W3 post-sync decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 12, "project W3 post-sync decision required_preflight_checks must be 12")
    _require(decision.get("ready_preflight_checks") == 12, "project W3 post-sync decision ready_preflight_checks must be 12")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(decision.get(key) is False, f"project W3 post-sync decision {key} must be false")
    _require(decision.get("next_recommended_step") == IF08_W3_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W3 post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W3 post-sync decision blocking_findings must be empty")
    _require(
        decision.get("warnings") == ["naming_pattern_preserved_as_2026_06_07_for_repo_consistency"],
        "project W3 post-sync decision warnings mismatch",
    )

    summary = _load_json(IF08_W3_POST_SYNC_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "project W3 post-sync summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W3 post-sync summary must be pass")
    _require(summary.get("status") == IF08_W3_POST_SYNC_STATUS, "project W3 post-sync summary status mismatch")
    _require(summary.get("source_phase") == IF08_W3_CONTROLLED_PHASE, "project W3 post-sync summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W3_CONTROLLED_STATUS, "project W3 post-sync summary source status mismatch")
    _require(summary.get("source_project_sha") == IF08_W3_CONTROLLED_PROJECT_SHA, "project W3 post-sync summary source project sha mismatch")
    _require(summary.get("source_ci_state") == IF08_W3_CONTROLLED_CI_STATE, "project W3 post-sync summary ci state mismatch")
    _require(summary.get("w3_canonical_sync_verified") is True, "project W3 post-sync summary must verify W3 canonical sync")
    _require(summary.get("w3_ser_observed") == 0, "project W3 post-sync summary w3_ser_observed must be 0")
    _require(summary.get("w3_rca_observed") == 1.0, "project W3 post-sync summary w3_rca_observed must be 1.0")
    _require(summary.get("w4_readiness_state") == "ready_for_preparation", "project W3 post-sync summary readiness state mismatch")
    _require(summary.get("w4_preparation_allowed_next") is True, "project W3 post-sync summary must allow W4 preparation")
    _require(summary.get("w4_execution_performed") is False, "project W3 post-sync summary execution performed must remain false")
    _require(summary.get("w4_execution_allowed") is False, "project W3 post-sync summary execution allowed must remain false")
    _require(summary.get("future_rhr_required") == 1.0, "project W3 post-sync summary future_rhr_required must be 1.0")
    _require(summary.get("future_ddr_required") == 1.0, "project W3 post-sync summary future_ddr_required must be 1.0")
    _require(summary.get("future_cer_required") == 1.0, "project W3 post-sync summary future_cer_required must be 1.0")
    _require(summary.get("readiness_coverage") == 1.0, "project W3 post-sync summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 12, "project W3 post-sync summary required_preflight_checks must be 12")
    _require(summary.get("ready_preflight_checks") == 12, "project W3 post-sync summary ready_preflight_checks must be 12")
    _require(summary.get("next_recommended_step") == IF08_W3_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W3 post-sync summary next step mismatch")

    readiness = _load_json(IF08_W4_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "project W4 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W4", "project W4 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Replay/rollback/concurrency/cost", "project W4 readiness wave_name mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project W4 readiness state mismatch")
    _require(readiness.get("future_rhr_required") == 1.0, "project W4 readiness future_rhr_required must be 1.0")
    _require(readiness.get("future_ddr_required") == 1.0, "project W4 readiness future_ddr_required must be 1.0")
    _require(readiness.get("future_cer_required") == 1.0, "project W4 readiness future_cer_required must be 1.0")
    _require(readiness.get("readiness_coverage") == 1.0, "project W4 readiness readiness_coverage must be 1.0")
    _require(readiness.get("required_preflight_checks") == 12, "project W4 readiness required_preflight_checks must be 12")
    _require(readiness.get("ready_preflight_checks") == 12, "project W4 readiness ready_preflight_checks must be 12")
    _require(readiness.get("w4_execution_performed") is False, "project W4 readiness must keep execution false")
    _require(readiness.get("w4_execution_allowed") is False, "project W4 readiness must keep execution disallowed")
    checks = {item.get("check_id"): item.get("passed") for item in readiness.get("checks", [])}
    _require(checks.get("w4_execution_not_performed") is True, "project W4 readiness must keep execution not performed")
    _require(checks.get("w4_execution_not_allowed") is True, "project W4 readiness must keep execution not allowed")

    no_execution = _load_json(IF08_W3_POST_SYNC_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W3-POST-SYNC-REVIEW", "project W3 post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W3 post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W3_POST_SYNC_STATUS, "project W3 post-sync no_execution status mismatch")
    _require(no_execution.get("w4_execution_performed") is False, "project W3 post-sync no_execution must keep execution false")
    _require(no_execution.get("w4_execution_allowed") is False, "project W3 post-sync no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
    ):
        _require(no_execution.get(key) is False, f"project W3 post-sync no_execution.{key} must be false")


def _check_if08_w4_preflight_readiness_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W4_PREFLIGHT_ACTIVE_DECISION_PATH,
        IF08_W4_PREFLIGHT_ACTIVE_SUMMARY_PATH,
        IF08_W4_PREFLIGHT_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W4 preflight active-context artifact: {path}")

    active_decision = _load_json(IF08_W4_PREFLIGHT_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W4-PREFLIGHT-READINESS", "active W4 preflight decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W4 preflight decision must be pass")
    _require(active_decision.get("status") == IF08_W4_PREFLIGHT_STATUS, "active W4 preflight decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W4_PREFLIGHT_PROJECT_SHA, "active W4 preflight decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W4_PREFLIGHT_CI_STATE, "active W4 preflight decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W4_PREFLIGHT_PROJECT_CI_RUN_URL, "active W4 preflight decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W4 preflight decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W4 preflight decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W4 preflight decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w4_preflight_readiness") is True, "active W4 preflight decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W4 preflight decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W4_PREFLIGHT_PHASE, "active W4 preflight decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W4_PREFLIGHT_STATUS, "active W4 preflight decision latest status mismatch")
    _require(active_decision.get("w4_preflight_readiness") is True, "active W4 preflight decision must mark readiness true")
    _require(active_decision.get("w4_execution_performed") is False, "active W4 preflight decision w4_execution_performed must be false")
    _require(active_decision.get("w4_execution_allowed") is False, "active W4 preflight decision w4_execution_allowed must be false")
    _require(active_decision.get("future_rhr_required") == 1.0, "active W4 preflight decision future_rhr_required must be 1.0")
    _require(active_decision.get("future_ddr_required") == 1.0, "active W4 preflight decision future_ddr_required must be 1.0")
    _require(active_decision.get("future_cer_required") == 1.0, "active W4 preflight decision future_cer_required must be 1.0")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W4 preflight decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 12, "active W4 preflight decision required_preflight_checks must be 12")
    _require(active_decision.get("ready_preflight_checks") == 12, "active W4 preflight decision ready_preflight_checks must be 12")
    _require(active_decision.get("next_recommended_step") == IF08_W4_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W4 preflight decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_outcome.get(key) is False, f"active W4 preflight decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W4_PREFLIGHT_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W4-PREFLIGHT-READINESS", "active W4 preflight summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W4 preflight summary must be pass")
    _require(active_summary.get("status") == IF08_W4_PREFLIGHT_STATUS, "active W4 preflight summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W4_PREFLIGHT_PHASE, "active W4 preflight summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W4_PREFLIGHT_STATUS, "active W4 preflight summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W4_PREFLIGHT_PROJECT_SHA, "active W4 preflight summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W4_PREFLIGHT_CI_STATE, "active W4 preflight summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W4_PREFLIGHT_PROJECT_CI_RUN_URL, "active W4 preflight summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W4 preflight summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w4_preflight_readiness") is True, "active W4 preflight summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W4 preflight summary must preserve permanent rule")
    _require(active_summary.get("w4_preflight_readiness") is True, "active W4 preflight summary readiness mismatch")
    _require(active_summary.get("w4_execution_performed") is False, "active W4 preflight summary must keep execution false")
    _require(active_summary.get("w4_execution_allowed") is False, "active W4 preflight summary must keep execution disallowed")
    _require(active_summary.get("future_rhr_required") == 1.0, "active W4 preflight summary future_rhr_required must be 1.0")
    _require(active_summary.get("future_ddr_required") == 1.0, "active W4 preflight summary future_ddr_required must be 1.0")
    _require(active_summary.get("future_cer_required") == 1.0, "active W4 preflight summary future_cer_required must be 1.0")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W4 preflight summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 12, "active W4 preflight summary required_preflight_checks must be 12")
    _require(active_summary.get("ready_preflight_checks") == 12, "active W4 preflight summary ready_preflight_checks must be 12")
    _require(active_summary.get("next_recommended_step") == IF08_W4_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W4 preflight summary next step mismatch")

    _mirror_contains(
        IF08_W4_PREFLIGHT_ACTIVE_REPORT_PATH,
        "IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness",
        IF08_W4_PREFLIGHT_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w4_preflight_readiness: `true`",
        "w4_preflight_readiness: `true`",
        "next_recommended_step: `execute_if08_w4_replay_rollback_concurrency_cost_controlled_execution`",
    )

    external_project_paths = (
        IF08_W4_PREFLIGHT_DECISION_PATH,
        IF08_W4_PREFLIGHT_SUMMARY_PATH,
        IF08_W4_PREFLIGHT_REPORT_PATH,
        IF08_W4_PREFLIGHT_ATTACK_SURFACE_PATH,
        IF08_W4_PREFLIGHT_ROLLBACK_ORACLE_PATH,
        IF08_W4_PREFLIGHT_CONCURRENCY_ORACLE_PATH,
        IF08_W4_PREFLIGHT_COST_ORACLE_PATH,
        IF08_W4_PREFLIGHT_FIXTURE_MATRIX_PATH,
        IF08_W4_PREFLIGHT_STOP_MATRIX_PATH,
        IF08_W4_PREFLIGHT_NO_EXECUTION_PATH,
        IF08_W4_PREFLIGHT_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W4_PREFLIGHT_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-PREFLIGHT-READINESS", "project W4 preflight decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W4 preflight decision must be pass")
    _require(decision.get("status") == IF08_W4_PREFLIGHT_STATUS, "project W4 preflight decision status mismatch")
    _require(decision.get("source_phase") == IF08_W3_POST_SYNC_PHASE, "project W4 preflight decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W3_POST_SYNC_STATUS, "project W4 preflight decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W3_POST_SYNC_PROJECT_SHA, "project W4 preflight decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W3_POST_SYNC_CI_STATE, "project W4 preflight decision source ci state mismatch")
    _require(decision.get("w4_preflight_readiness") is True, "project W4 preflight decision must mark readiness true")
    _require(decision.get("w4_execution_performed") is False, "project W4 preflight decision must keep execution false")
    _require(decision.get("w4_execution_allowed") is False, "project W4 preflight decision must keep execution disallowed")
    _require(decision.get("future_rhr_required") == 1.0, "project W4 preflight decision future_rhr_required must be 1.0")
    _require(decision.get("future_ddr_required") == 1.0, "project W4 preflight decision future_ddr_required must be 1.0")
    _require(decision.get("future_cer_required") == 1.0, "project W4 preflight decision future_cer_required must be 1.0")
    _require(decision.get("readiness_coverage") == 1.0, "project W4 preflight decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 12, "project W4 preflight decision required_preflight_checks must be 12")
    _require(decision.get("ready_preflight_checks") == 12, "project W4 preflight decision ready_preflight_checks must be 12")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(decision.get(key) is False, f"project W4 preflight decision {key} must be false")
    _require(decision.get("next_recommended_step") == IF08_W4_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W4 preflight decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W4 preflight decision blocking_findings must be empty")

    summary = _load_json(IF08_W4_PREFLIGHT_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-PREFLIGHT-READINESS", "project W4 preflight summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W4 preflight summary must be pass")
    _require(summary.get("status") == IF08_W4_PREFLIGHT_STATUS, "project W4 preflight summary status mismatch")
    _require(summary.get("source_phase") == IF08_W3_POST_SYNC_PHASE, "project W4 preflight summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W3_POST_SYNC_STATUS, "project W4 preflight summary source status mismatch")
    _require(summary.get("source_project_sha") == IF08_W3_POST_SYNC_PROJECT_SHA, "project W4 preflight summary source project sha mismatch")
    _require(summary.get("source_ci_state") == IF08_W3_POST_SYNC_CI_STATE, "project W4 preflight summary source ci state mismatch")
    _require(summary.get("w4_preflight_readiness") is True, "project W4 preflight summary must mark readiness true")
    _require(summary.get("future_rhr_required") == 1.0, "project W4 preflight summary future_rhr_required must be 1.0")
    _require(summary.get("future_ddr_required") == 1.0, "project W4 preflight summary future_ddr_required must be 1.0")
    _require(summary.get("future_cer_required") == 1.0, "project W4 preflight summary future_cer_required must be 1.0")
    _require(summary.get("readiness_coverage") == 1.0, "project W4 preflight summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 12, "project W4 preflight summary required_preflight_checks must be 12")
    _require(summary.get("ready_preflight_checks") == 12, "project W4 preflight summary ready_preflight_checks must be 12")
    _require(summary.get("next_recommended_step") == IF08_W4_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W4 preflight summary next step mismatch")

    attack_surface = _load_json(IF08_W4_PREFLIGHT_ATTACK_SURFACE_PATH)
    _require(attack_surface.get("wave_id") == "W4", "project W4 preflight attack surface wave_id mismatch")
    _require(attack_surface.get("wave_name") == "Replay/rollback/concurrency/cost", "project W4 preflight attack surface wave_name mismatch")
    _require(len(attack_surface.get("attack_vectors", [])) == 12, "project W4 preflight attack vector count mismatch")

    rollback_oracle = _load_json(IF08_W4_PREFLIGHT_ROLLBACK_ORACLE_PATH)
    concurrency_oracle = _load_json(IF08_W4_PREFLIGHT_CONCURRENCY_ORACLE_PATH)
    cost_oracle = _load_json(IF08_W4_PREFLIGHT_COST_ORACLE_PATH)
    _require(rollback_oracle.get("metric_required") == 1.0, "project W4 preflight rollback oracle metric mismatch")
    _require(concurrency_oracle.get("metric_required") == 1.0, "project W4 preflight concurrency oracle metric mismatch")
    _require(cost_oracle.get("metric_required") == 1.0, "project W4 preflight cost oracle metric mismatch")

    fixture_matrix = _load_json(IF08_W4_PREFLIGHT_FIXTURE_MATRIX_PATH)
    _require(fixture_matrix.get("all_fixture_definitions_ready") is True, "project W4 preflight fixture readiness mismatch")
    _require(fixture_matrix.get("execution_materialized_now") is False, "project W4 preflight fixture execution must remain false")

    stop_matrix = _load_json(IF08_W4_PREFLIGHT_STOP_MATRIX_PATH)
    _require(stop_matrix.get("all_stop_conditions_defined") is True, "project W4 preflight stop conditions mismatch")
    _require(len(stop_matrix.get("rows", [])) == 12, "project W4 preflight stop row count mismatch")

    no_execution = _load_json(IF08_W4_PREFLIGHT_NO_EXECUTION_PATH)
    _require(no_execution.get("w4_execution_performed") is False, "project W4 preflight no_execution must keep execution false")
    _require(no_execution.get("w4_execution_allowed") is False, "project W4 preflight no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(no_execution.get(key) is False, f"project W4 preflight no_execution.{key} must be false")


def _check_if08_w4_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W4_CONTROLLED_ACTIVE_DECISION_PATH,
        IF08_W4_CONTROLLED_ACTIVE_SUMMARY_PATH,
        IF08_W4_CONTROLLED_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W4 controlled active-context artifact: {path}")

    active_decision = _load_json(IF08_W4_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W4-CONTROLLED-EXECUTION", "active W4 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W4 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W4_CONTROLLED_STATUS, "active W4 controlled decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W4_CONTROLLED_PROJECT_SHA, "active W4 controlled decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W4_CONTROLLED_CI_STATE, "active W4 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W4_CONTROLLED_PROJECT_CI_RUN_URL, "active W4 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W4 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W4 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W4 controlled decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w4_controlled_execution") is True, "active W4 controlled decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W4 controlled decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W4_CONTROLLED_PHASE, "active W4 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W4_CONTROLLED_STATUS, "active W4 controlled decision latest status mismatch")
    _require(active_decision.get("w4_preflight_readiness") is True, "active W4 controlled decision must keep readiness true")
    _require(active_decision.get("w4_execution_performed") is True, "active W4 controlled decision must record execution performed")
    _require(active_decision.get("w4_execution_allowed") is False, "active W4 controlled decision must keep execution disallowed")
    _require(active_decision.get("future_rhr_required") == 1.0, "active W4 controlled decision future_rhr_required must be 1.0")
    _require(active_decision.get("future_ddr_required") == 1.0, "active W4 controlled decision future_ddr_required must be 1.0")
    _require(active_decision.get("future_cer_required") == 1.0, "active W4 controlled decision future_cer_required must be 1.0")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W4 controlled decision readiness_coverage must be 1.0")
    _require(active_decision.get("synthetic_attack_cases_total") == 14, "active W4 controlled decision synthetic_attack_cases_total must be 14")
    _require(active_decision.get("synthetic_attack_cases_passed") == 14, "active W4 controlled decision synthetic_attack_cases_passed must be 14")
    _require(active_decision.get("synthetic_attack_cases_blocked_or_detected") == 14, "active W4 controlled decision synthetic_attack_cases_blocked_or_detected must be 14")
    _require(active_decision.get("rollback_honesty_checks_required") == 6, "active W4 controlled decision rollback_honesty_checks_required must be 6")
    _require(active_decision.get("rollback_honesty_checks_passed") == 6, "active W4 controlled decision rollback_honesty_checks_passed must be 6")
    _require(active_decision.get("duplicate_detection_checks_required") == 5, "active W4 controlled decision duplicate_detection_checks_required must be 5")
    _require(active_decision.get("duplicate_detection_checks_passed") == 5, "active W4 controlled decision duplicate_detection_checks_passed must be 5")
    _require(active_decision.get("cost_enforcement_checks_required") == 3, "active W4 controlled decision cost_enforcement_checks_required must be 3")
    _require(active_decision.get("cost_enforcement_checks_passed") == 3, "active W4 controlled decision cost_enforcement_checks_passed must be 3")
    _require(active_decision.get("rhr_observed") == 1.0, "active W4 controlled decision rhr_observed must be 1.0")
    _require(active_decision.get("ddr_observed") == 1.0, "active W4 controlled decision ddr_observed must be 1.0")
    _require(active_decision.get("cer_observed") == 1.0, "active W4 controlled decision cer_observed must be 1.0")
    _require(active_decision.get("next_recommended_step") == IF08_W4_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W4 controlled decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_outcome.get(key) is False, f"active W4 controlled decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W4_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W4-CONTROLLED-EXECUTION", "active W4 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W4 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W4_CONTROLLED_STATUS, "active W4 controlled summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W4_CONTROLLED_PHASE, "active W4 controlled summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W4_CONTROLLED_STATUS, "active W4 controlled summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W4_CONTROLLED_PROJECT_SHA, "active W4 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W4_CONTROLLED_CI_STATE, "active W4 controlled summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W4_CONTROLLED_PROJECT_CI_RUN_URL, "active W4 controlled summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W4 controlled summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w4_controlled_execution") is True, "active W4 controlled summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W4 controlled summary must preserve permanent rule")
    _require(active_summary.get("w4_preflight_readiness") is True, "active W4 controlled summary readiness mismatch")
    _require(active_summary.get("w4_execution_performed") is True, "active W4 controlled summary must record execution performed")
    _require(active_summary.get("w4_execution_allowed") is False, "active W4 controlled summary must keep execution disallowed")
    _require(active_summary.get("synthetic_attack_cases_total") == 14, "active W4 controlled summary synthetic_attack_cases_total must be 14")
    _require(active_summary.get("synthetic_attack_cases_passed") == 14, "active W4 controlled summary synthetic_attack_cases_passed must be 14")
    _require(active_summary.get("synthetic_attack_cases_blocked_or_detected") == 14, "active W4 controlled summary synthetic_attack_cases_blocked_or_detected must be 14")
    _require(active_summary.get("rollback_honesty_checks_required") == 6, "active W4 controlled summary rollback_honesty_checks_required must be 6")
    _require(active_summary.get("rollback_honesty_checks_passed") == 6, "active W4 controlled summary rollback_honesty_checks_passed must be 6")
    _require(active_summary.get("duplicate_detection_checks_required") == 5, "active W4 controlled summary duplicate_detection_checks_required must be 5")
    _require(active_summary.get("duplicate_detection_checks_passed") == 5, "active W4 controlled summary duplicate_detection_checks_passed must be 5")
    _require(active_summary.get("cost_enforcement_checks_required") == 3, "active W4 controlled summary cost_enforcement_checks_required must be 3")
    _require(active_summary.get("cost_enforcement_checks_passed") == 3, "active W4 controlled summary cost_enforcement_checks_passed must be 3")
    _require(active_summary.get("rhr_observed") == 1.0, "active W4 controlled summary rhr_observed must be 1.0")
    _require(active_summary.get("ddr_observed") == 1.0, "active W4 controlled summary ddr_observed must be 1.0")
    _require(active_summary.get("cer_observed") == 1.0, "active W4 controlled summary cer_observed must be 1.0")
    _require(active_summary.get("next_recommended_step") == IF08_W4_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W4 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W4_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution",
        IF08_W4_CONTROLLED_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w4_controlled_execution: `true`",
        "w4_execution_performed: `true`",
        "synthetic_attack_cases_total: `14`",
        "rollback_honesty_checks: `6/6`",
        "duplicate_detection_checks: `5/5`",
        "cost_enforcement_checks: `3/3`",
        "next_recommended_step: `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`",
    )

    external_project_paths = (
        IF08_W4_CONTROLLED_DECISION_PATH,
        IF08_W4_CONTROLLED_SUMMARY_PATH,
        IF08_W4_CONTROLLED_REPORT_PATH,
        IF08_W4_CONTROLLED_LOG_PATH,
        IF08_W4_CONTROLLED_METRICS_PATH,
        IF08_W4_CONTROLLED_SAFETY_ATTESTATION_PATH,
        IF08_W4_CONTROLLED_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W4_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-CONTROLLED-EXECUTION", "project W4 controlled decision phase_id mismatch")
    _require(decision.get("phase_name") == IF08_W4_CONTROLLED_PHASE, "project W4 controlled decision phase_name mismatch")
    _require(decision.get("decision") == "pass", "project W4 controlled decision must be pass")
    _require(decision.get("status") == IF08_W4_CONTROLLED_STATUS, "project W4 controlled decision status mismatch")
    _require(decision.get("source_phase") == IF08_W4_PREFLIGHT_PHASE, "project W4 controlled decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W4_PREFLIGHT_STATUS, "project W4 controlled decision source status mismatch")
    _require(decision.get("source_ci_state") == IF08_W4_PREFLIGHT_CI_STATE, "project W4 controlled decision source ci state mismatch")
    _require(decision.get("input_project_commit_sha") == IF08_W4_PREFLIGHT_PROJECT_SHA, "project W4 controlled decision input project sha mismatch")
    _require(decision.get("execution_scope") == "synthetic_isolated_lab_only", "project W4 controlled decision execution_scope mismatch")
    _require(decision.get("w4_execution_performed") is True, "project W4 controlled decision must record execution performed")
    _require(decision.get("wave_executed") == "W4", "project W4 controlled decision wave_executed mismatch")
    _require(decision.get("bot_executed") is True, "project W4 controlled decision bot_executed must be true")
    _require(len(decision.get("bots_executed", [])) == 4, "project W4 controlled decision must list 4 bots")
    _require(decision.get("synthetic_attack_cases_total") == 14, "project W4 controlled decision synthetic_attack_cases_total must be 14")
    _require(decision.get("synthetic_attack_cases_passed") == 14, "project W4 controlled decision synthetic_attack_cases_passed must be 14")
    _require(decision.get("synthetic_attack_cases_blocked_or_detected") == 14, "project W4 controlled decision synthetic_attack_cases_blocked_or_detected must be 14")
    _require(decision.get("rollback_honesty_checks_required") == 6, "project W4 controlled decision rollback_honesty_checks_required must be 6")
    _require(decision.get("rollback_honesty_checks_passed") == 6, "project W4 controlled decision rollback_honesty_checks_passed must be 6")
    _require(decision.get("duplicate_detection_checks_required") == 5, "project W4 controlled decision duplicate_detection_checks_required must be 5")
    _require(decision.get("duplicate_detection_checks_passed") == 5, "project W4 controlled decision duplicate_detection_checks_passed must be 5")
    _require(decision.get("cost_enforcement_checks_required") == 3, "project W4 controlled decision cost_enforcement_checks_required must be 3")
    _require(decision.get("cost_enforcement_checks_passed") == 3, "project W4 controlled decision cost_enforcement_checks_passed must be 3")
    _require(decision.get("rhr_observed") == 1.0, "project W4 controlled decision rhr_observed must be 1.0")
    _require(decision.get("ddr_observed") == 1.0, "project W4 controlled decision ddr_observed must be 1.0")
    _require(decision.get("cer_observed") == 1.0, "project W4 controlled decision cer_observed must be 1.0")
    _require(decision.get("findings_created_count") == 0, "project W4 controlled decision findings_created_count must be 0")
    _require(decision.get("finding_candidates") == [], "project W4 controlled decision finding_candidates must be empty")
    _require(decision.get("next_recommended_step") == IF08_W4_CONTROLLED_NEXT_RECOMMENDED_STEP, "project W4 controlled decision next step mismatch")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(decision.get(key) is False, f"project W4 controlled decision {key} must be false")

    summary = _load_json(IF08_W4_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-CONTROLLED-EXECUTION", "project W4 controlled summary phase_id mismatch")
    _require(summary.get("phase_name") == IF08_W4_CONTROLLED_PHASE, "project W4 controlled summary phase_name mismatch")
    _require(summary.get("decision") == "pass", "project W4 controlled summary must be pass")
    _require(summary.get("status") == IF08_W4_CONTROLLED_STATUS, "project W4 controlled summary status mismatch")
    _require(summary.get("input_project_commit_sha") == IF08_W4_PREFLIGHT_PROJECT_SHA, "project W4 controlled summary input project sha mismatch")
    _require(summary.get("execution_scope") == "synthetic_isolated_lab_only", "project W4 controlled summary execution_scope mismatch")
    _require(summary.get("wave_executed") == "W4", "project W4 controlled summary wave_executed mismatch")
    _require(len(summary.get("bots_executed", [])) == 4, "project W4 controlled summary must list 4 bots")
    _require(summary.get("synthetic_attack_cases_total") == 14, "project W4 controlled summary synthetic_attack_cases_total must be 14")
    _require(summary.get("synthetic_attack_cases_passed") == 14, "project W4 controlled summary synthetic_attack_cases_passed must be 14")
    _require(summary.get("synthetic_attack_cases_blocked_or_detected") == 14, "project W4 controlled summary synthetic_attack_cases_blocked_or_detected must be 14")
    _require(summary.get("rollback_honesty_checks_required") == 6, "project W4 controlled summary rollback_honesty_checks_required must be 6")
    _require(summary.get("rollback_honesty_checks_passed") == 6, "project W4 controlled summary rollback_honesty_checks_passed must be 6")
    _require(summary.get("duplicate_detection_checks_required") == 5, "project W4 controlled summary duplicate_detection_checks_required must be 5")
    _require(summary.get("duplicate_detection_checks_passed") == 5, "project W4 controlled summary duplicate_detection_checks_passed must be 5")
    _require(summary.get("cost_enforcement_checks_required") == 3, "project W4 controlled summary cost_enforcement_checks_required must be 3")
    _require(summary.get("cost_enforcement_checks_passed") == 3, "project W4 controlled summary cost_enforcement_checks_passed must be 3")
    _require(summary.get("rhr_observed") == 1.0, "project W4 controlled summary rhr_observed must be 1.0")
    _require(summary.get("ddr_observed") == 1.0, "project W4 controlled summary ddr_observed must be 1.0")
    _require(summary.get("cer_observed") == 1.0, "project W4 controlled summary cer_observed must be 1.0")
    _require(summary.get("next_recommended_step") == IF08_W4_CONTROLLED_NEXT_RECOMMENDED_STEP, "project W4 controlled summary next step mismatch")

    metrics = _load_json(IF08_W4_CONTROLLED_METRICS_PATH)
    _require(metrics.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-CONTROLLED-EXECUTION", "project W4 metrics phase_id mismatch")
    _require(metrics.get("wave_id") == "W4", "project W4 metrics wave_id mismatch")
    _require(metrics.get("wave_name") == "Replay/rollback/concurrency/cost", "project W4 metrics wave_name mismatch")
    _require(metrics.get("cost_enforcement_checks_required") == 3, "project W4 metrics cost_enforcement_checks_required must be 3")
    _require(metrics.get("cost_enforcement_checks_passed") == 3, "project W4 metrics cost_enforcement_checks_passed must be 3")
    _require(metrics.get("cer_observed") == 1.0, "project W4 metrics cer_observed must be 1.0")
    _require(metrics.get("real_cost_spent") is False, "project W4 metrics real_cost_spent must be false")
    _require(metrics.get("real_quota_consumed") is False, "project W4 metrics real_quota_consumed must be false")
    _require(len(metrics.get("rows", [])) == 3, "project W4 metrics must contain 3 rows")
    _require(all(row.get("scenario_passed") is True for row in metrics.get("rows", [])), "project W4 metrics rows must all pass")
    _require(all(row.get("blocked_or_detected") is True for row in metrics.get("rows", [])), "project W4 metrics rows must all block or detect")

    log_rows = _load_jsonl(IF08_W4_CONTROLLED_LOG_PATH)
    _require(log_rows[0].get("event_type") == "phase_start", "project W4 log must start with phase_start")
    _require(log_rows[-1].get("event_type") == "phase_verdict", "project W4 log must end with phase_verdict")
    _require(len(log_rows) == 16, "project W4 log must contain 16 rows")
    scenario_rows = [row for row in log_rows if row.get("event_type") == "scenario_result"]
    _require(len(scenario_rows) == 14, "project W4 log must contain 14 scenario_result rows")
    _require(all(row.get("blocked_or_detected") is True for row in scenario_rows), "project W4 log scenario_result rows must all block or detect")
    _require(log_rows[-1].get("rhr_observed") == 1.0, "project W4 log rhr_observed must be 1.0")
    _require(log_rows[-1].get("ddr_observed") == 1.0, "project W4 log ddr_observed must be 1.0")
    _require(log_rows[-1].get("cer_observed") == 1.0, "project W4 log cer_observed must be 1.0")

    safety = _load_json(IF08_W4_CONTROLLED_SAFETY_ATTESTATION_PATH)
    _require(safety.get("phase_id") == "IF-08-W4-REPLAY-ROLLBACK-CONCURRENCY-COST-CONTROLLED-EXECUTION", "project W4 safety attestation phase_id mismatch")
    _require(safety.get("execution_scope") == "synthetic_isolated_lab_only", "project W4 safety attestation execution_scope mismatch")
    _require(safety.get("deterministic_output_contract") is True, "project W4 safety attestation deterministic_output_contract must be true")
    _require(len(safety.get("json_outputs_expected", [])) == 4, "project W4 safety attestation json_outputs_expected must contain 4 entries")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "filesystem_escape_performed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(safety.get(key) is False, f"project W4 safety attestation {key} must be false")

    _mirror_contains(
        IF08_W4_CONTROLLED_REPORT_PATH,
        "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution",
        "execution_scope: `synthetic_isolated_lab_only`",
        "synthetic_attack_cases_total: `14`",
        "rollback_honesty_checks: `6/6`",
        "duplicate_detection_checks: `5/5`",
        "cost_enforcement_checks: `3/3`",
        "next_recommended_step: `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`",
    )
    _mirror_contains(
        IF08_W4_CONTROLLED_DOC_PATH,
        "execution_scope=synthetic_isolated_lab_only",
        "w4_execution_performed=true",
        "RHR=1.0, DDR=1.0, CER=1.0",
        "denial_of_wallet_attack",
    )


def _check_if08_w2_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W2_POST_SYNC_ACTIVE_DECISION_PATH,
        IF08_W2_POST_SYNC_ACTIVE_SUMMARY_PATH,
        IF08_W2_POST_SYNC_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W2 post-sync review active-context artifact: {path}")

    active_decision = _load_json(IF08_W2_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "active W2 post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W2 post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W2_POST_SYNC_STATUS, "active W2 post-sync decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W2_POST_SYNC_PROJECT_SHA, "active W2 post-sync decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W2_POST_SYNC_CI_STATE, "active W2 post-sync decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W2_POST_SYNC_PROJECT_CI_RUN_URL, "active W2 post-sync decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W2 post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W2 post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W2 post-sync decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W2 post-sync decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w2_post_sync_review") is True, "active W2 post-sync decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W2_POST_SYNC_PHASE, "active W2 post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W2_POST_SYNC_STATUS, "active W2 post-sync decision latest status mismatch")
    _require(active_decision.get("w2_canonical_sync_verified") is True, "active W2 post-sync decision must verify W2 canonical sync")
    _require(active_decision.get("w2_far_observed") == 0, "active W2 post-sync decision w2_far_observed must be 0")
    _require(active_decision.get("w2_ctl_observed") == 0, "active W2 post-sync decision w2_ctl_observed must be 0")
    _require(active_decision.get("w2_attack_attempts_expected") == 12, "active W2 post-sync decision expected attacks must be 12")
    _require(active_decision.get("w2_attack_attempts_blocked") == 12, "active W2 post-sync decision blocked attacks must be 12")
    _require(active_decision.get("w2_undetected_attacks") == [], "active W2 post-sync decision undetected attacks must be empty")
    _require(active_decision.get("w2_synthetic_isolated_only") is True, "active W2 post-sync decision must preserve synthetic isolated only")
    _require(active_decision.get("w3_readiness_state") == "ready_for_preparation", "active W2 post-sync decision readiness state mismatch")
    _require(active_decision.get("w3_preparation_allowed_next") is True, "active W2 post-sync decision must allow W3 preparation")
    _require(active_decision.get("w3_execution_performed") is False, "active W2 post-sync decision w3_execution_performed must be false")
    _require(active_decision.get("w3_execution_allowed") is False, "active W2 post-sync decision w3_execution_allowed must be false")
    _require(active_decision.get("future_ser_required") == 0, "active W2 post-sync decision future_ser_required must be 0")
    _require(active_decision.get("future_rca_required") == 1.0, "active W2 post-sync decision future_rca_required must be 1.0")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W2 post-sync decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 8, "active W2 post-sync decision required_preflight_checks must be 8")
    _require(active_decision.get("ready_preflight_checks") == 8, "active W2 post-sync decision ready_preflight_checks must be 8")
    _require(active_decision.get("sirene_status") == "conditional_or_deferred_with_reason", "active W2 post-sync decision sirene_status mismatch")
    _require(active_decision.get("next_recommended_step") == IF08_W2_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W2 post-sync decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W2 post-sync decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W2_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "active W2 post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W2 post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W2_POST_SYNC_STATUS, "active W2 post-sync summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W2_POST_SYNC_PHASE, "active W2 post-sync summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W2_POST_SYNC_STATUS, "active W2 post-sync summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W2_POST_SYNC_PROJECT_SHA, "active W2 post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W2_POST_SYNC_CI_STATE, "active W2 post-sync summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W2_POST_SYNC_PROJECT_CI_RUN_URL, "active W2 post-sync summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W2 post-sync summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w2_post_sync_review") is True, "active W2 post-sync summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W2 post-sync summary must preserve permanent rule")
    _require(active_summary.get("w2_canonical_sync_verified") is True, "active W2 post-sync summary must verify W2 canonical sync")
    _require(active_summary.get("w2_far_observed") == 0, "active W2 post-sync summary w2_far_observed must be 0")
    _require(active_summary.get("w2_ctl_observed") == 0, "active W2 post-sync summary w2_ctl_observed must be 0")
    _require(active_summary.get("w3_readiness_state") == "ready_for_preparation", "active W2 post-sync summary readiness state mismatch")
    _require(active_summary.get("w3_preparation_allowed_next") is True, "active W2 post-sync summary must allow W3 preparation")
    _require(active_summary.get("w3_execution_performed") is False, "active W2 post-sync summary must keep execution false")
    _require(active_summary.get("w3_execution_allowed") is False, "active W2 post-sync summary must keep execution disallowed")
    _require(active_summary.get("future_ser_required") == 0, "active W2 post-sync summary future_ser_required must be 0")
    _require(active_summary.get("future_rca_required") == 1.0, "active W2 post-sync summary future_rca_required must be 1.0")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W2 post-sync summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 8, "active W2 post-sync summary required_preflight_checks must be 8")
    _require(active_summary.get("ready_preflight_checks") == 8, "active W2 post-sync summary ready_preflight_checks must be 8")
    _require(active_summary.get("sirene_status") == "conditional_or_deferred_with_reason", "active W2 post-sync summary sirene_status mismatch")
    _require(active_summary.get("next_recommended_step") == IF08_W2_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W2 post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W2_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W2 Controlled Execution Post-Sync Review & W3 Readiness Decision",
        IF08_W2_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w2_post_sync_review: `true`",
        "w3_preparation_allowed_next: `true`",
        "next_recommended_step: `prepare_if08_w3_runtime_tool_mcp_sandbox_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W2_POST_SYNC_DECISION_PATH,
        IF08_W2_POST_SYNC_SUMMARY_PATH,
        IF08_W2_POST_SYNC_REPORT_PATH,
        IF08_W3_READINESS_MATRIX_PATH,
        IF08_W2_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W2_POST_SYNC_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W2_POST_SYNC_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "project W2 post-sync decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W2 post-sync decision must be pass")
    _require(decision.get("status") == IF08_W2_POST_SYNC_STATUS, "project W2 post-sync decision status mismatch")
    _require(decision.get("source_phase") == IF08_W2_CONTROLLED_PHASE, "project W2 post-sync decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W2_CONTROLLED_STATUS, "project W2 post-sync decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W2_CONTROLLED_PROJECT_SHA, "project W2 post-sync decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W2_CONTROLLED_CI_STATE, "project W2 post-sync decision source ci state mismatch")
    _require(decision.get("w2_canonical_sync_verified") is True, "project W2 post-sync decision must verify W2 canonical sync")
    _require(decision.get("w2_far_observed") == 0, "project W2 post-sync decision w2_far_observed must be 0")
    _require(decision.get("w2_ctl_observed") == 0, "project W2 post-sync decision w2_ctl_observed must be 0")
    _require(decision.get("w2_attack_attempts_expected") == 12, "project W2 post-sync decision expected attacks must be 12")
    _require(decision.get("w2_attack_attempts_blocked") == 12, "project W2 post-sync decision blocked attacks must be 12")
    _require(decision.get("w2_undetected_attacks") == [], "project W2 post-sync decision undetected attacks must be empty")
    _require(decision.get("w2_synthetic_isolated_only") is True, "project W2 post-sync decision must preserve synthetic isolated only")
    _require(decision.get("w3_readiness_state") == "ready_for_preparation", "project W2 post-sync decision readiness state mismatch")
    _require(decision.get("w3_preparation_allowed_next") is True, "project W2 post-sync decision must allow W3 preparation")
    _require(decision.get("w3_execution_performed") is False, "project W2 post-sync decision w3_execution_performed must be false")
    _require(decision.get("w3_execution_allowed") is False, "project W2 post-sync decision w3_execution_allowed must be false")
    _require(decision.get("future_ser_required") == 0, "project W2 post-sync decision future_ser_required must be 0")
    _require(decision.get("future_rca_required") == 1.0, "project W2 post-sync decision future_rca_required must be 1.0")
    _require(decision.get("readiness_coverage") == 1.0, "project W2 post-sync decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 8, "project W2 post-sync decision required_preflight_checks must be 8")
    _require(decision.get("ready_preflight_checks") == 8, "project W2 post-sync decision ready_preflight_checks must be 8")
    _require(decision.get("sirene_status") == "conditional_or_deferred_with_reason", "project W2 post-sync decision sirene_status mismatch")
    _require(decision.get("runtime_executed") is False, "project W2 post-sync decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W2 post-sync decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W2 post-sync decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W2 post-sync decision secrets_accessed must be false")
    _require(decision.get("mcp_activated") is False, "project W2 post-sync decision mcp_activated must be false")
    _require(decision.get("rag_ingestion_executed") is False, "project W2 post-sync decision rag_ingestion_executed must be false")
    _require(decision.get("memory_write_executed") is False, "project W2 post-sync decision memory_write_executed must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W2 post-sync decision external_network_used_except_github_governance must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W2 post-sync decision dependency_or_package_manager_used must be false")
    _require(decision.get("next_recommended_step") == IF08_W2_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W2 post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W2 post-sync decision blocking_findings must be empty")
    _require(
        decision.get("warnings") == ["sirene_audio_oracle_not_ready_so_status_is_conditional_or_deferred_with_reason"],
        "project W2 post-sync decision warnings mismatch",
    )

    summary = _load_json(IF08_W2_POST_SYNC_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "project W2 post-sync summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W2 post-sync summary must be pass")
    _require(summary.get("status") == IF08_W2_POST_SYNC_STATUS, "project W2 post-sync summary status mismatch")
    _require(summary.get("source_phase") == IF08_W2_CONTROLLED_PHASE, "project W2 post-sync summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W2_CONTROLLED_STATUS, "project W2 post-sync summary source status mismatch")
    _require(summary.get("source_project_sha") == IF08_W2_CONTROLLED_PROJECT_SHA, "project W2 post-sync summary project sha mismatch")
    _require(summary.get("source_ci_state") == IF08_W2_CONTROLLED_CI_STATE, "project W2 post-sync summary ci state mismatch")
    _require(summary.get("w2_canonical_sync_verified") is True, "project W2 post-sync summary must verify W2 canonical sync")
    _require(summary.get("w2_far_observed") == 0, "project W2 post-sync summary w2_far_observed must be 0")
    _require(summary.get("w2_ctl_observed") == 0, "project W2 post-sync summary w2_ctl_observed must be 0")
    _require(summary.get("w3_readiness_state") == "ready_for_preparation", "project W2 post-sync summary readiness state mismatch")
    _require(summary.get("w3_preparation_allowed_next") is True, "project W2 post-sync summary must allow W3 preparation")
    _require(summary.get("w3_execution_performed") is False, "project W2 post-sync summary execution performed must remain false")
    _require(summary.get("w3_execution_allowed") is False, "project W2 post-sync summary execution allowed must remain false")
    _require(summary.get("future_ser_required") == 0, "project W2 post-sync summary future_ser_required must be 0")
    _require(summary.get("future_rca_required") == 1.0, "project W2 post-sync summary future_rca_required must be 1.0")
    _require(summary.get("readiness_coverage") == 1.0, "project W2 post-sync summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 8, "project W2 post-sync summary required_preflight_checks must be 8")
    _require(summary.get("ready_preflight_checks") == 8, "project W2 post-sync summary ready_preflight_checks must be 8")
    _require(summary.get("sirene_status") == "conditional_or_deferred_with_reason", "project W2 post-sync summary sirene_status mismatch")
    _require(summary.get("next_recommended_step") == IF08_W2_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W2 post-sync summary next step mismatch")

    readiness = _load_json(IF08_W3_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "project W3 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W3", "project W3 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Runtime/tool/MCP/sandbox", "project W3 readiness wave_name mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project W3 readiness state mismatch")
    _require(readiness.get("future_ser_required") == 0, "project W3 readiness future_ser_required must be 0")
    _require(readiness.get("future_rca_required") == 1.0, "project W3 readiness future_rca_required must be 1.0")
    _require(readiness.get("readiness_coverage") == 1.0, "project W3 readiness readiness_coverage must be 1.0")
    _require(readiness.get("required_preflight_checks") == 8, "project W3 readiness required_preflight_checks must be 8")
    _require(readiness.get("ready_preflight_checks") == 8, "project W3 readiness ready_preflight_checks must be 8")
    _require(readiness.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 readiness sirene_status mismatch")
    _require(readiness.get("w3_execution_performed") is False, "project W3 readiness must keep execution false")
    _require(readiness.get("w3_execution_allowed") is False, "project W3 readiness must keep execution disallowed")
    checks = {item.get("check_id"): item.get("passed") for item in readiness.get("checks", [])}
    _require(checks.get("w3_execution_not_performed") is True, "project W3 readiness must keep execution not performed")
    _require(checks.get("w3_execution_not_allowed") is True, "project W3 readiness must keep execution not allowed")

    no_execution = _load_json(IF08_W2_POST_SYNC_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W2-POST-SYNC-REVIEW", "project W2 post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W2 post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W2_POST_SYNC_STATUS, "project W2 post-sync no_execution status mismatch")
    _require(no_execution.get("w3_execution_performed") is False, "project W2 post-sync no_execution must keep execution false")
    _require(no_execution.get("w3_execution_allowed") is False, "project W2 post-sync no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_execution.get(key) is False, f"project W2 post-sync no_execution.{key} must be false")


def _check_if08_w3_preflight_readiness_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W3_PREFLIGHT_ACTIVE_DECISION_PATH,
        IF08_W3_PREFLIGHT_ACTIVE_SUMMARY_PATH,
        IF08_W3_PREFLIGHT_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W3 preflight active-context artifact: {path}")

    active_decision = _load_json(IF08_W3_PREFLIGHT_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-PREFLIGHT-READINESS", "active W3 preflight decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W3 preflight decision must be pass")
    _require(active_decision.get("status") == IF08_W3_PREFLIGHT_STATUS, "active W3 preflight decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W3_PREFLIGHT_PROJECT_SHA, "active W3 preflight decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W3_PREFLIGHT_CI_STATE, "active W3 preflight decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W3_PREFLIGHT_PROJECT_CI_RUN_URL, "active W3 preflight decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W3 preflight decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W3 preflight decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W3 preflight decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W3 preflight decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_preflight_readiness") is True, "active W3 preflight decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W3_PREFLIGHT_PHASE, "active W3 preflight decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W3_PREFLIGHT_STATUS, "active W3 preflight decision latest status mismatch")
    _require(active_decision.get("w3_preflight_readiness") is True, "active W3 preflight decision must keep preflight readiness true")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W3 preflight decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 13, "active W3 preflight decision required_preflight_checks must be 13")
    _require(active_decision.get("ready_preflight_checks") == 13, "active W3 preflight decision ready_preflight_checks must be 13")
    _require(active_decision.get("future_ser_required") == 0, "active W3 preflight decision future_ser_required must be 0")
    _require(active_decision.get("future_rca_required") == 1.0, "active W3 preflight decision future_rca_required must be 1.0")
    _require(active_decision.get("sirene_status") == "conditional_or_deferred_with_reason", "active W3 preflight decision sirene_status mismatch")
    _require(bool(active_decision.get("sirene_reason")), "active W3 preflight decision sirene_reason missing")
    _require(active_decision.get("w3_execution_performed") is False, "active W3 preflight decision w3_execution_performed must be false")
    _require(active_decision.get("w3_execution_allowed") is False, "active W3 preflight decision w3_execution_allowed must be false")
    _require(active_decision.get("next_recommended_step") == IF08_W3_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W3 preflight decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W3 preflight decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W3_PREFLIGHT_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-PREFLIGHT-READINESS", "active W3 preflight summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W3 preflight summary must be pass")
    _require(active_summary.get("status") == IF08_W3_PREFLIGHT_STATUS, "active W3 preflight summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W3_PREFLIGHT_PHASE, "active W3 preflight summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W3_PREFLIGHT_STATUS, "active W3 preflight summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W3_PREFLIGHT_PROJECT_SHA, "active W3 preflight summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W3_PREFLIGHT_CI_STATE, "active W3 preflight summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W3_PREFLIGHT_PROJECT_CI_RUN_URL, "active W3 preflight summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W3 preflight summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_preflight_readiness") is True, "active W3 preflight summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W3 preflight summary must preserve permanent rule")
    _require(active_summary.get("w3_preflight_readiness") is True, "active W3 preflight summary must keep preflight readiness true")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W3 preflight summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 13, "active W3 preflight summary required_preflight_checks must be 13")
    _require(active_summary.get("ready_preflight_checks") == 13, "active W3 preflight summary ready_preflight_checks must be 13")
    _require(active_summary.get("future_ser_required") == 0, "active W3 preflight summary future_ser_required must be 0")
    _require(active_summary.get("future_rca_required") == 1.0, "active W3 preflight summary future_rca_required must be 1.0")
    _require(active_summary.get("sirene_status") == "conditional_or_deferred_with_reason", "active W3 preflight summary sirene_status mismatch")
    _require(active_summary.get("w3_execution_allowed") is False, "active W3 preflight summary must keep execution disallowed")
    _require(active_summary.get("next_recommended_step") == IF08_W3_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W3 preflight summary next step mismatch")

    _mirror_contains(
        IF08_W3_PREFLIGHT_ACTIVE_REPORT_PATH,
        "IF-08 W3 Runtime/Tool/MCP/Sandbox Preflight Readiness",
        IF08_W3_PREFLIGHT_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w3_runtime_tool_mcp_sandbox_preflight_readiness: `true`",
        "readiness_coverage: `1.0`",
        "next_recommended_step: `execute_if08_w3_runtime_tool_mcp_sandbox_controlled_execution`",
    )

    external_project_paths = (
        IF08_W3_PREFLIGHT_DECISION_PATH,
        IF08_W3_PREFLIGHT_SUMMARY_PATH,
        IF08_W3_PREFLIGHT_REPORT_PATH,
        IF08_W3_PREFLIGHT_ATTACK_SURFACE_PATH,
        IF08_W3_PREFLIGHT_ORACLE_CONTRACT_PATH,
        IF08_W3_PREFLIGHT_FIXTURE_MATRIX_PATH,
        IF08_W3_PREFLIGHT_STOP_CONDITION_PATH,
        IF08_W3_PREFLIGHT_SIRENE_MATRIX_PATH,
        IF08_W3_PREFLIGHT_NO_EXECUTION_PATH,
        IF08_W3_PREFLIGHT_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W3_PREFLIGHT_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-PREFLIGHT-READINESS", "project W3 preflight decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W3 preflight decision must be pass")
    _require(decision.get("status") == IF08_W3_PREFLIGHT_STATUS, "project W3 preflight decision status mismatch")
    _require(decision.get("source_phase") == IF08_W2_POST_SYNC_PHASE, "project W3 preflight decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W2_POST_SYNC_STATUS, "project W3 preflight decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W2_POST_SYNC_PROJECT_SHA, "project W3 preflight decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W2_POST_SYNC_CI_STATE, "project W3 preflight decision source ci state mismatch")
    _require(decision.get("w3_preflight_readiness") is True, "project W3 preflight decision must keep preflight readiness true")
    _require(decision.get("w3_execution_performed") is False, "project W3 preflight decision w3_execution_performed must be false")
    _require(decision.get("w3_execution_allowed") is False, "project W3 preflight decision w3_execution_allowed must be false")
    _require(decision.get("future_ser_required") == 0, "project W3 preflight decision future_ser_required must be 0")
    _require(decision.get("future_rca_required") == 1.0, "project W3 preflight decision future_rca_required must be 1.0")
    _require(decision.get("readiness_coverage") == 1.0, "project W3 preflight decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 13, "project W3 preflight decision required_preflight_checks must be 13")
    _require(decision.get("ready_preflight_checks") == 13, "project W3 preflight decision ready_preflight_checks must be 13")
    _require(decision.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 preflight decision sirene_status mismatch")
    _require(bool(decision.get("sirene_reason")), "project W3 preflight decision sirene_reason missing")
    _require(decision.get("attack_surface_matrix_created") is True, "project W3 preflight decision attack_surface_matrix_created must be true")
    _require(decision.get("oracle_contract_created") is True, "project W3 preflight decision oracle_contract_created must be true")
    _require(decision.get("fixture_readiness_matrix_created") is True, "project W3 preflight decision fixture_readiness_matrix_created must be true")
    _require(decision.get("stop_condition_matrix_created") is True, "project W3 preflight decision stop_condition_matrix_created must be true")
    _require(decision.get("sirene_conditionality_matrix_created") is True, "project W3 preflight decision sirene_conditionality_matrix_created must be true")
    _require(decision.get("no_execution_attestation_created") is True, "project W3 preflight decision no_execution_attestation_created must be true")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
    ):
        _require(decision.get(key) is False, f"project W3 preflight decision {key} must be false")
    _require(decision.get("next_recommended_step") == IF08_W3_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W3 preflight decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W3 preflight decision blocking_findings must be empty")

    summary = _load_json(IF08_W3_PREFLIGHT_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-PREFLIGHT-READINESS", "project W3 preflight summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W3 preflight summary must be pass")
    _require(summary.get("status") == IF08_W3_PREFLIGHT_STATUS, "project W3 preflight summary status mismatch")
    _require(summary.get("source_phase") == IF08_W2_POST_SYNC_PHASE, "project W3 preflight summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W2_POST_SYNC_STATUS, "project W3 preflight summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W2_POST_SYNC_PROJECT_SHA, "project W3 preflight summary source project sha mismatch")
    _require(summary.get("w3_wave_id") == "W3", "project W3 preflight summary wave_id mismatch")
    _require(summary.get("readiness_coverage") == 1.0, "project W3 preflight summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 13, "project W3 preflight summary required_preflight_checks must be 13")
    _require(summary.get("ready_preflight_checks") == 13, "project W3 preflight summary ready_preflight_checks must be 13")
    _require(summary.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 preflight summary sirene_status mismatch")
    _require(summary.get("next_recommended_step") == IF08_W3_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W3 preflight summary next step mismatch")

    attack_surface = _load_json(IF08_W3_PREFLIGHT_ATTACK_SURFACE_PATH)
    _require(attack_surface.get("wave_id") == "W3", "project W3 preflight attack_surface wave_id mismatch")
    _require(attack_surface.get("wave_name") == "Runtime/tool/MCP/sandbox", "project W3 preflight attack_surface wave_name mismatch")
    _require(len(attack_surface.get("attack_vectors", [])) == 12, "project W3 preflight attack_surface vector count mismatch")

    oracle_contract = _load_json(IF08_W3_PREFLIGHT_ORACLE_CONTRACT_PATH)
    _require(oracle_contract.get("future_ser_required") == 0, "project W3 preflight oracle future_ser_required must be 0")
    _require(oracle_contract.get("future_rca_required") == 1.0, "project W3 preflight oracle future_rca_required must be 1.0")

    fixture_matrix = _load_json(IF08_W3_PREFLIGHT_FIXTURE_MATRIX_PATH)
    _require(fixture_matrix.get("all_fixture_definitions_ready") is True, "project W3 preflight fixture matrix must be ready")
    _require(fixture_matrix.get("execution_materialized_now") is False, "project W3 preflight fixture matrix must not materialize execution")

    stop_matrix = _load_json(IF08_W3_PREFLIGHT_STOP_CONDITION_PATH)
    _require(stop_matrix.get("all_stop_conditions_defined") is True, "project W3 preflight stop matrix must define all stop conditions")
    _require(len(stop_matrix.get("rows", [])) == 12, "project W3 preflight stop matrix row count mismatch")

    sirene_matrix = _load_json(IF08_W3_PREFLIGHT_SIRENE_MATRIX_PATH)
    _require(sirene_matrix.get("sirene_status") == "conditional_or_deferred_with_reason", "project W3 preflight sirene matrix status mismatch")
    _require(bool(sirene_matrix.get("sirene_reason")), "project W3 preflight sirene matrix reason missing")
    _require(sirene_matrix.get("audio_scope_active") is False, "project W3 preflight sirene matrix audio_scope_active must be false")
    _require(sirene_matrix.get("audio_oracle_pack_ready_now") is False, "project W3 preflight sirene matrix audio_oracle_pack_ready_now must be false")

    no_execution = _load_json(IF08_W3_PREFLIGHT_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W3-RUNTIME-TOOL-MCP-SANDBOX-PREFLIGHT-READINESS", "project W3 preflight no_execution phase_id mismatch")
    _require(no_execution.get("w3_execution_performed") is False, "project W3 preflight no_execution must keep execution false")
    _require(no_execution.get("w3_execution_allowed") is False, "project W3 preflight no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_execution.get(key) is False, f"project W3 preflight no_execution.{key} must be false")


def _check_if08_w2_preflight_readiness_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W2_PREFLIGHT_ACTIVE_DECISION_PATH,
        IF08_W2_PREFLIGHT_ACTIVE_SUMMARY_PATH,
        IF08_W2_PREFLIGHT_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W2 preflight active-context artifact: {path}")

    active_decision = _load_json(IF08_W2_PREFLIGHT_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "active W2 preflight decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W2 preflight decision must be pass")
    _require(active_decision.get("status") == IF08_W2_PREFLIGHT_STATUS, "active W2 preflight decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W2_PREFLIGHT_PROJECT_SHA, "active W2 preflight decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W2_PREFLIGHT_CI_STATE, "active W2 preflight decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W2_PREFLIGHT_PROJECT_CI_RUN_URL, "active W2 preflight decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W2 preflight decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W2 preflight decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W2 preflight decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W2 preflight decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_preflight_readiness") is True, "active W2 preflight decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W2_PREFLIGHT_PHASE, "active W2 preflight decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W2_PREFLIGHT_STATUS, "active W2 preflight decision latest status mismatch")
    _require(active_decision.get("w2_preflight_readiness") is True, "active W2 preflight decision must keep readiness true")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W2 preflight decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 12, "active W2 preflight decision required_preflight_checks must be 12")
    _require(active_decision.get("ready_preflight_checks") == 12, "active W2 preflight decision ready_preflight_checks must be 12")
    _require(active_decision.get("future_far_required") == 0, "active W2 preflight decision future_far_required must be 0")
    _require(active_decision.get("future_ctl_required") == 0, "active W2 preflight decision future_ctl_required must be 0")
    _require(active_decision.get("w2_execution_performed") is False, "active W2 preflight decision must keep w2_execution_performed false")
    _require(active_decision.get("w2_execution_allowed") is False, "active W2 preflight decision must keep w2_execution_allowed false")
    _require(active_decision.get("next_recommended_step") == IF08_W2_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W2 preflight decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W2 preflight decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W2_PREFLIGHT_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "active W2 preflight summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W2 preflight summary must be pass")
    _require(active_summary.get("status") == IF08_W2_PREFLIGHT_STATUS, "active W2 preflight summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W2_PREFLIGHT_PHASE, "active W2 preflight summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W2_PREFLIGHT_STATUS, "active W2 preflight summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W2_PREFLIGHT_PROJECT_SHA, "active W2 preflight summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W2_PREFLIGHT_CI_STATE, "active W2 preflight summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W2_PREFLIGHT_PROJECT_CI_RUN_URL, "active W2 preflight summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W2 preflight summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_preflight_readiness") is True, "active W2 preflight summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W2 preflight summary must preserve permanent rule")
    _require(active_summary.get("w2_preflight_readiness") is True, "active W2 preflight summary must keep readiness true")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W2 preflight summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 12, "active W2 preflight summary required_preflight_checks must be 12")
    _require(active_summary.get("ready_preflight_checks") == 12, "active W2 preflight summary ready_preflight_checks must be 12")
    _require(active_summary.get("future_far_required") == 0, "active W2 preflight summary future_far_required must be 0")
    _require(active_summary.get("future_ctl_required") == 0, "active W2 preflight summary future_ctl_required must be 0")
    _require(active_summary.get("w2_execution_allowed") is False, "active W2 preflight summary must keep execution disallowed")
    _require(active_summary.get("next_recommended_step") == IF08_W2_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W2 preflight summary next step mismatch")

    _mirror_contains(
        IF08_W2_PREFLIGHT_ACTIVE_REPORT_PATH,
        "IF-08 W2 Auth/HITL/Identity/Exfil Preflight Readiness",
        IF08_W2_PREFLIGHT_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w2_auth_hitl_identity_exfil_preflight_readiness: `true`",
        "ready_preflight_checks: `12/12`",
        "next_recommended_step: `execute_if08_w2_auth_hitl_identity_exfil_controlled_execution`",
    )

    external_project_paths = (
        IF08_W2_PREFLIGHT_DECISION_PATH,
        IF08_W2_PREFLIGHT_SUMMARY_PATH,
        IF08_W2_PREFLIGHT_REPORT_PATH,
        IF08_W2_PREFLIGHT_ATTACK_SURFACE_PATH,
        IF08_W2_PREFLIGHT_ORACLE_CONTRACT_PATH,
        IF08_W2_PREFLIGHT_FIXTURE_MATRIX_PATH,
        IF08_W2_PREFLIGHT_STOP_CONDITION_PATH,
        IF08_W2_PREFLIGHT_NO_EXECUTION_PATH,
        IF08_W2_PREFLIGHT_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W2_PREFLIGHT_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W2 preflight decision must be pass")
    _require(decision.get("status") == IF08_W2_PREFLIGHT_STATUS, "project W2 preflight decision status mismatch")
    _require(decision.get("source_phase") == IF08_W1_POST_SYNC_PHASE, "project W2 preflight decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W1_POST_SYNC_STATUS, "project W2 preflight decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W1_POST_SYNC_PROJECT_SHA, "project W2 preflight decision source project sha mismatch")
    _require(decision.get("w2_wave", {}).get("wave_id") == "W2", "project W2 preflight decision wave_id mismatch")
    _require(decision.get("w2_wave", {}).get("wave_name") == "Auth/HITL/identity/exfil", "project W2 preflight decision wave_name mismatch")
    _require(decision.get("w2_preflight_readiness") is True, "project W2 preflight decision must keep readiness true")
    _require(decision.get("readiness_coverage") == 1.0, "project W2 preflight decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 12, "project W2 preflight decision required_preflight_checks must be 12")
    _require(decision.get("ready_preflight_checks") == 12, "project W2 preflight decision ready_preflight_checks must be 12")
    _require(decision.get("future_far_required") == 0, "project W2 preflight decision future_far_required must be 0")
    _require(decision.get("future_ctl_required") == 0, "project W2 preflight decision future_ctl_required must be 0")
    _require(decision.get("attack_surface_matrix_created") is True, "project W2 preflight decision must create attack surface matrix")
    _require(decision.get("oracle_contract_created") is True, "project W2 preflight decision must create oracle contract")
    _require(decision.get("fixture_readiness_matrix_created") is True, "project W2 preflight decision must create fixture matrix")
    _require(decision.get("stop_condition_matrix_created") is True, "project W2 preflight decision must create stop condition matrix")
    _require(decision.get("no_execution_attestation_created") is True, "project W2 preflight decision must create no_execution attestation")
    _require(decision.get("w2_execution_performed") is False, "project W2 preflight decision w2_execution_performed must be false")
    _require(decision.get("w2_execution_allowed") is False, "project W2 preflight decision w2_execution_allowed must be false")
    _require(decision.get("runtime_executed") is False, "project W2 preflight decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W2 preflight decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W2 preflight decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W2 preflight decision secrets_accessed must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W2 preflight decision dependency_or_package_manager_used must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W2 preflight decision external_network_used_except_github_governance must be false")
    _require(decision.get("blocking_findings") == [], "project W2 preflight decision blocking_findings must be empty")
    _require(decision.get("next_recommended_step") == IF08_W2_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W2 preflight decision next step mismatch")
    _require(len(decision.get("w2_bots", [])) == 4, "project W2 preflight decision must list 4 W2 bots")

    summary = _load_json(IF08_W2_PREFLIGHT_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W2 preflight summary must be pass")
    _require(summary.get("status") == IF08_W2_PREFLIGHT_STATUS, "project W2 preflight summary status mismatch")
    _require(summary.get("source_phase") == IF08_W1_POST_SYNC_PHASE, "project W2 preflight summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W1_POST_SYNC_STATUS, "project W2 preflight summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W1_POST_SYNC_PROJECT_SHA, "project W2 preflight summary source project sha mismatch")
    _require(summary.get("w2_wave_id") == "W2", "project W2 preflight summary wave_id mismatch")
    _require(summary.get("w2_wave_name") == "Auth/HITL/identity/exfil", "project W2 preflight summary wave_name mismatch")
    _require(summary.get("w2_preflight_readiness") is True, "project W2 preflight summary must keep readiness true")
    _require(summary.get("readiness_coverage") == 1.0, "project W2 preflight summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 12, "project W2 preflight summary required_preflight_checks must be 12")
    _require(summary.get("ready_preflight_checks") == 12, "project W2 preflight summary ready_preflight_checks must be 12")
    _require(summary.get("future_far_required") == 0, "project W2 preflight summary future_far_required must be 0")
    _require(summary.get("future_ctl_required") == 0, "project W2 preflight summary future_ctl_required must be 0")
    _require(summary.get("next_recommended_step") == IF08_W2_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W2 preflight summary next step mismatch")
    _require(len(summary.get("w2_bots", [])) == 4, "project W2 preflight summary must list 4 W2 bots")

    attack_surface = _load_json(IF08_W2_PREFLIGHT_ATTACK_SURFACE_PATH)
    _require(attack_surface.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight attack surface phase_id mismatch")
    _require(attack_surface.get("wave_id") == "W2", "project W2 preflight attack surface wave_id mismatch")
    _require(attack_surface.get("future_far_required") == 0, "project W2 preflight attack surface future_far_required must be 0")
    _require(attack_surface.get("future_ctl_required") == 0, "project W2 preflight attack surface future_ctl_required must be 0")
    _require(len(attack_surface.get("attack_vectors", [])) == 10, "project W2 preflight attack surface must contain 10 vectors")

    oracle_contract = _load_json(IF08_W2_PREFLIGHT_ORACLE_CONTRACT_PATH)
    _require(oracle_contract.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight oracle contract phase_id mismatch")
    _require(oracle_contract.get("future_far_required") == 0, "project W2 preflight oracle contract future_far_required must be 0")
    _require(oracle_contract.get("future_ctl_required") == 0, "project W2 preflight oracle contract future_ctl_required must be 0")
    _require(oracle_contract.get("source_priority_stack_preserved") is True, "project W2 preflight oracle contract must preserve source priority stack")
    _require(len(oracle_contract.get("future_oracles", [])) == 10, "project W2 preflight oracle contract must contain 10 future oracles")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("runtime_execution_allowed") is False, "project W2 preflight oracle contract runtime_execution_allowed must be false")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("mcp_runtime_activation_allowed") is False, "project W2 preflight oracle contract mcp_runtime_activation_allowed must be false")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("memory_write_allowed") is False, "project W2 preflight oracle contract memory_write_allowed must be false")

    fixture_matrix = _load_json(IF08_W2_PREFLIGHT_FIXTURE_MATRIX_PATH)
    _require(fixture_matrix.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight fixture matrix phase_id mismatch")
    _require(fixture_matrix.get("wave_id") == "W2", "project W2 preflight fixture matrix wave_id mismatch")
    _require(fixture_matrix.get("all_fixture_definitions_ready") is True, "project W2 preflight fixture matrix must be ready")
    _require(fixture_matrix.get("execution_materialized_now") is False, "project W2 preflight fixture matrix execution_materialized_now must be false")
    _require(len(fixture_matrix.get("bots", [])) == 4, "project W2 preflight fixture matrix must contain 4 bot rows")
    _require(all(row.get("preflight_definition_ready") is True for row in fixture_matrix.get("bots", [])), "project W2 preflight fixture matrix must keep every bot ready")

    stop_conditions = _load_json(IF08_W2_PREFLIGHT_STOP_CONDITION_PATH)
    _require(stop_conditions.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight stop condition phase_id mismatch")
    _require(stop_conditions.get("all_stop_conditions_defined") is True, "project W2 preflight stop conditions must all be defined")
    _require(len(stop_conditions.get("rows", [])) == 10, "project W2 preflight stop conditions must contain 10 rows")
    _require(all(row.get("hard_stop") is True for row in stop_conditions.get("rows", [])), "project W2 preflight stop conditions must mark every row as hard_stop")
    _require(all(row.get("execution_now") is False for row in stop_conditions.get("rows", [])), "project W2 preflight stop conditions must keep execution_now false")

    no_execution = _load_json(IF08_W2_PREFLIGHT_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W2-AUTH-HITL-IDENTITY-EXFIL-PREFLIGHT-READINESS", "project W2 preflight no_execution phase_id mismatch")
    _require(no_execution.get("w2_execution_performed") is False, "project W2 preflight no_execution must keep execution false")
    _require(no_execution.get("w2_execution_allowed") is False, "project W2 preflight no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "dependency_or_package_manager_used",
        "external_network_used_except_github_governance",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_execution.get(key) is False, f"project W2 preflight no_execution.{key} must be false")


def _check_if08_w1_preflight_readiness_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W1_PREFLIGHT_ACTIVE_DECISION_PATH,
        IF08_W1_PREFLIGHT_ACTIVE_SUMMARY_PATH,
        IF08_W1_PREFLIGHT_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W1 preflight active-context artifact: {path}")

    active_decision = _load_json(IF08_W1_PREFLIGHT_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "active W1 preflight decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W1 preflight decision must be pass")
    _require(active_decision.get("status") == IF08_W1_PREFLIGHT_STATUS, "active W1 preflight decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W1_PREFLIGHT_PROJECT_SHA, "active W1 preflight decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W1_PREFLIGHT_CI_STATE, "active W1 preflight decision ci state mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W1 preflight decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W1 preflight decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W1 preflight decision must mark sync applied")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W1 preflight decision must preserve permanent rule")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w1_context_memory_rag_preflight_readiness") is True, "active W1 preflight decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W1_PREFLIGHT_PHASE, "active W1 preflight decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W1_PREFLIGHT_STATUS, "active W1 preflight decision latest status mismatch")
    _require(active_decision.get("w1_preflight_readiness") is True, "active W1 preflight decision must keep readiness true")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W1 preflight decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 10, "active W1 preflight decision required_preflight_checks must be 10")
    _require(active_decision.get("ready_preflight_checks") == 10, "active W1 preflight decision ready_preflight_checks must be 10")
    _require(active_decision.get("future_cir_required") == 1.0, "active W1 preflight decision future_cir_required must be 1.0")
    _require(active_decision.get("w1_execution_performed") is False, "active W1 preflight decision must keep w1_execution_performed false")
    _require(active_decision.get("w1_execution_allowed") is False, "active W1 preflight decision must keep w1_execution_allowed false")
    _require(active_decision.get("next_recommended_step") == IF08_W1_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W1 preflight decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(active_outcome.get(key) is False, f"active W1 preflight decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W1_PREFLIGHT_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "active W1 preflight summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W1 preflight summary must be pass")
    _require(active_summary.get("status") == IF08_W1_PREFLIGHT_STATUS, "active W1 preflight summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W1_PREFLIGHT_PHASE, "active W1 preflight summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W1_PREFLIGHT_STATUS, "active W1 preflight summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W1_PREFLIGHT_PROJECT_SHA, "active W1 preflight summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W1_PREFLIGHT_CI_STATE, "active W1 preflight summary ci state mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W1 preflight summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w1_context_memory_rag_preflight_readiness") is True, "active W1 preflight summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W1 preflight summary must preserve permanent rule")
    _require(active_summary.get("w1_preflight_readiness") is True, "active W1 preflight summary must keep readiness true")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W1 preflight summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 10, "active W1 preflight summary required_preflight_checks must be 10")
    _require(active_summary.get("ready_preflight_checks") == 10, "active W1 preflight summary ready_preflight_checks must be 10")
    _require(active_summary.get("future_cir_required") == 1.0, "active W1 preflight summary future_cir_required must be 1.0")
    _require(active_summary.get("w1_execution_allowed") is False, "active W1 preflight summary must keep execution disallowed")
    _require(active_summary.get("next_recommended_step") == IF08_W1_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W1 preflight summary next step mismatch")

    _mirror_contains(
        IF08_W1_PREFLIGHT_ACTIVE_REPORT_PATH,
        "IF-08 W1 Context/Memory/RAG Preflight Readiness",
        IF08_W1_PREFLIGHT_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w1_context_memory_rag_preflight_readiness: `true`",
        "next_recommended_step: `execute_if08_w1_context_memory_rag_controlled_execution`",
    )

    external_project_paths = (
        IF08_W1_PREFLIGHT_DECISION_PATH,
        IF08_W1_PREFLIGHT_SUMMARY_PATH,
        IF08_W1_PREFLIGHT_REPORT_PATH,
        IF08_W1_PREFLIGHT_ATTACK_SURFACE_PATH,
        IF08_W1_PREFLIGHT_ORACLE_CONTRACT_PATH,
        IF08_W1_PREFLIGHT_FIXTURE_MATRIX_PATH,
        IF08_W1_PREFLIGHT_NO_EXECUTION_PATH,
        IF08_W1_PREFLIGHT_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W1_PREFLIGHT_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W1 preflight decision must be pass")
    _require(decision.get("status") == IF08_W1_PREFLIGHT_STATUS, "project W1 preflight decision status mismatch")
    _require(decision.get("source_phase") == IF08_W05_POST_SYNC_PHASE, "project W1 preflight decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W05_POST_SYNC_STATUS, "project W1 preflight decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W05_POST_SYNC_PROJECT_SHA, "project W1 preflight decision source project sha mismatch")
    _require(decision.get("source_ci_state") == IF08_W05_POST_SYNC_CI_STATE, "project W1 preflight decision source ci state mismatch")
    _require(decision.get("w1_wave", {}).get("wave_id") == "W1", "project W1 preflight decision wave_id mismatch")
    _require(decision.get("w1_wave", {}).get("wave_name") == "Context/memory/RAG", "project W1 preflight decision wave_name mismatch")
    _require(decision.get("w1_preflight_readiness") is True, "project W1 preflight decision must keep readiness true")
    _require(decision.get("readiness_coverage") == 1.0, "project W1 preflight decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 10, "project W1 preflight decision required_preflight_checks must be 10")
    _require(decision.get("ready_preflight_checks") == 10, "project W1 preflight decision ready_preflight_checks must be 10")
    _require(decision.get("future_cir_required") == 1.0, "project W1 preflight decision future_cir_required must be 1.0")
    _require(decision.get("attack_surface_matrix_created") is True, "project W1 preflight decision must create attack surface matrix")
    _require(decision.get("oracle_contract_created") is True, "project W1 preflight decision must create oracle contract")
    _require(decision.get("fixture_readiness_matrix_created") is True, "project W1 preflight decision must create fixture matrix")
    _require(decision.get("no_execution_attestation_created") is True, "project W1 preflight decision must create no_execution attestation")
    _require(decision.get("w1_execution_performed") is False, "project W1 preflight decision w1_execution_performed must be false")
    _require(decision.get("w1_execution_allowed") is False, "project W1 preflight decision w1_execution_allowed must be false")
    _require(decision.get("runtime_executed") is False, "project W1 preflight decision runtime_executed must be false")
    _require(decision.get("real_apply_executed") is False, "project W1 preflight decision real_apply_executed must be false")
    _require(decision.get("product_or_bedrock_executed") is False, "project W1 preflight decision product_or_bedrock_executed must be false")
    _require(decision.get("secrets_accessed") is False, "project W1 preflight decision secrets_accessed must be false")
    _require(decision.get("dependency_or_package_manager_used") is False, "project W1 preflight decision dependency_or_package_manager_used must be false")
    _require(decision.get("external_network_used_except_github_governance") is False, "project W1 preflight decision external_network_used_except_github_governance must be false")
    _require(decision.get("blocking_findings") == [], "project W1 preflight decision blocking_findings must be empty")
    _require(decision.get("next_recommended_step") == IF08_W1_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W1 preflight decision next step mismatch")

    summary = _load_json(IF08_W1_PREFLIGHT_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W1 preflight summary must be pass")
    _require(summary.get("status") == IF08_W1_PREFLIGHT_STATUS, "project W1 preflight summary status mismatch")
    _require(summary.get("source_phase") == IF08_W05_POST_SYNC_PHASE, "project W1 preflight summary source phase mismatch")
    _require(summary.get("source_status") == IF08_W05_POST_SYNC_STATUS, "project W1 preflight summary source status mismatch")
    _require(summary.get("project_commit_sha") == IF08_W05_POST_SYNC_PROJECT_SHA, "project W1 preflight summary source project sha mismatch")
    _require(summary.get("project_ci_state") == IF08_W05_POST_SYNC_CI_STATE, "project W1 preflight summary source ci state mismatch")
    _require(summary.get("w1_wave_id") == "W1", "project W1 preflight summary wave_id mismatch")
    _require(summary.get("w1_preflight_readiness") is True, "project W1 preflight summary must keep readiness true")
    _require(summary.get("readiness_coverage") == 1.0, "project W1 preflight summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 10, "project W1 preflight summary required_preflight_checks must be 10")
    _require(summary.get("ready_preflight_checks") == 10, "project W1 preflight summary ready_preflight_checks must be 10")
    _require(summary.get("future_cir_required") == 1.0, "project W1 preflight summary future_cir_required must be 1.0")
    _require(summary.get("next_recommended_step") == IF08_W1_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W1 preflight summary next step mismatch")

    attack_surface = _load_json(IF08_W1_PREFLIGHT_ATTACK_SURFACE_PATH)
    _require(attack_surface.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight attack surface phase_id mismatch")
    _require(attack_surface.get("wave_id") == "W1", "project W1 preflight attack surface wave_id mismatch")
    _require(attack_surface.get("future_cir_required") == 1.0, "project W1 preflight attack surface future_cir_required must be 1.0")
    _require(len(attack_surface.get("attack_vectors", [])) == 8, "project W1 preflight attack surface must contain 8 vectors")

    oracle_contract = _load_json(IF08_W1_PREFLIGHT_ORACLE_CONTRACT_PATH)
    _require(oracle_contract.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight oracle contract phase_id mismatch")
    _require(oracle_contract.get("future_cir_required") == 1.0, "project W1 preflight oracle contract future_cir_required must be 1.0")
    _require(oracle_contract.get("source_priority_stack_preserved") is True, "project W1 preflight oracle contract must preserve source priority stack")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("runtime_execution_allowed") is False, "project W1 preflight oracle contract runtime_execution_allowed must be false")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("mcp_runtime_activation_allowed") is False, "project W1 preflight oracle contract mcp_runtime_activation_allowed must be false")
    _require(oracle_contract.get("forbidden_execution_surfaces", {}).get("rag_ingestion_allowed") is False, "project W1 preflight oracle contract rag_ingestion_allowed must be false")

    fixture_matrix = _load_json(IF08_W1_PREFLIGHT_FIXTURE_MATRIX_PATH)
    _require(fixture_matrix.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight fixture matrix phase_id mismatch")
    _require(fixture_matrix.get("wave_id") == "W1", "project W1 preflight fixture matrix wave_id mismatch")
    _require(fixture_matrix.get("all_fixture_definitions_ready") is True, "project W1 preflight fixture matrix must be ready")
    _require(fixture_matrix.get("execution_materialized_now") is False, "project W1 preflight fixture matrix execution_materialized_now must be false")
    _require(len(fixture_matrix.get("bots", [])) == 3, "project W1 preflight fixture matrix must contain 3 bot rows")

    no_execution = _load_json(IF08_W1_PREFLIGHT_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W1-CONTEXT-MEMORY-RAG-PREFLIGHT-READINESS", "project W1 preflight no_execution phase_id mismatch")
    _require(no_execution.get("w1_execution_performed") is False, "project W1 preflight no_execution must keep execution false")
    _require(no_execution.get("w1_execution_allowed") is False, "project W1 preflight no_execution must keep execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_or_bedrock_executed",
        "secrets_accessed",
        "dependency_or_package_manager_used",
        "external_network_used_except_github_governance",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
    ):
        _require(no_execution.get(key) is False, f"project W1 preflight no_execution.{key} must be false")


def _check_if08_w4_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF08_W4_POST_SYNC_ACTIVE_DECISION_PATH,
        IF08_W4_POST_SYNC_ACTIVE_SUMMARY_PATH,
        IF08_W4_POST_SYNC_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF08 W4 post-sync review active-context artifact: {path}")

    active_decision = _load_json(IF08_W4_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "active W4 post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W4 post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W4_POST_SYNC_STATUS, "active W4 post-sync decision status mismatch")
    _require(active_decision.get("source_project_sha") == IF08_W4_POST_SYNC_PROJECT_SHA, "active W4 post-sync decision project sha mismatch")
    _require(active_decision.get("source_project_ci_state") == IF08_W4_POST_SYNC_CI_STATE, "active W4 post-sync decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W4_POST_SYNC_PROJECT_CI_RUN_URL, "active W4 post-sync decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W4 post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W4 post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active W4 post-sync decision pre-sync phase id mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF08_W4_CONTROLLED_STATUS, "active W4 post-sync decision pre-sync current status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == "474cc539098fb5af5fec552d6eddef0d73d30c42", "active W4 post-sync decision pre-sync sha mismatch")
    _require(active_decision.get("active_context_sync_applied") is True, "active W4 post-sync decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w4_post_sync_review") is True, "active W4 post-sync decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W4 post-sync decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W4_POST_SYNC_PHASE, "active W4 post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W4_POST_SYNC_STATUS, "active W4 post-sync decision latest status mismatch")
    _require(active_decision.get("w4_canonical_sync_verified") is True, "active W4 post-sync decision must verify W4 canonical sync")
    _require(active_decision.get("validator_sync_repair_verified") is True, "active W4 post-sync decision must verify validator sync repair")
    _require(active_decision.get("w4_execution_performed") is True, "active W4 post-sync decision must preserve W4 execution")
    _require(active_decision.get("w4_execution_allowed") is False, "active W4 post-sync decision must keep execution disallowed")
    _require(active_decision.get("w4_execution_scope") == "synthetic_isolated_lab_only", "active W4 post-sync decision execution scope mismatch")
    _require(active_decision.get("synthetic_attack_cases_total") == 14, "active W4 post-sync decision synthetic_attack_cases_total must be 14")
    _require(active_decision.get("rollback_honesty_checks_required") == 6, "active W4 post-sync decision rollback_honesty_checks_required must be 6")
    _require(active_decision.get("rollback_honesty_checks_passed") == 6, "active W4 post-sync decision rollback_honesty_checks_passed must be 6")
    _require(active_decision.get("duplicate_detection_checks_required") == 5, "active W4 post-sync decision duplicate_detection_checks_required must be 5")
    _require(active_decision.get("duplicate_detection_checks_passed") == 5, "active W4 post-sync decision duplicate_detection_checks_passed must be 5")
    _require(active_decision.get("cost_enforcement_checks_required") == 3, "active W4 post-sync decision cost_enforcement_checks_required must be 3")
    _require(active_decision.get("cost_enforcement_checks_passed") == 3, "active W4 post-sync decision cost_enforcement_checks_passed must be 3")
    _require(active_decision.get("rhr_observed") == 1.0, "active W4 post-sync decision rhr_observed must be 1.0")
    _require(active_decision.get("ddr_observed") == 1.0, "active W4 post-sync decision ddr_observed must be 1.0")
    _require(active_decision.get("cer_observed") == 1.0, "active W4 post-sync decision cer_observed must be 1.0")
    _require(active_decision.get("w5_readiness_state") == "ready_for_preparation", "active W4 post-sync decision readiness state mismatch")
    _require(active_decision.get("w5_preparation_allowed_next") is True, "active W4 post-sync decision must allow W5 preparation")
    _require(active_decision.get("w5_execution_performed") is False, "active W4 post-sync decision must keep W5 execution false")
    _require(active_decision.get("w5_execution_allowed") is False, "active W4 post-sync decision must keep W5 execution disallowed")
    _require(active_decision.get("next_recommended_step") == IF08_W4_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W4 post-sync decision next step mismatch")
    active_outcome = active_decision.get("execution_outcome", {})
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_outcome.get(key) is False, f"active W4 post-sync decision execution_outcome.{key} must be false")

    active_summary = _load_json(IF08_W4_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "active W4 post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W4 post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W4_POST_SYNC_STATUS, "active W4 post-sync summary status mismatch")
    _require(active_summary.get("latest_completed_phase") == IF08_W4_POST_SYNC_PHASE, "active W4 post-sync summary latest phase mismatch")
    _require(active_summary.get("latest_completed_status") == IF08_W4_POST_SYNC_STATUS, "active W4 post-sync summary latest status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W4_POST_SYNC_PROJECT_SHA, "active W4 post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W4_POST_SYNC_CI_STATE, "active W4 post-sync summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W4_POST_SYNC_PROJECT_CI_RUN_URL, "active W4 post-sync summary ci url mismatch")
    _require(active_summary.get("active_context_sync_applied") is True, "active W4 post-sync summary must mark sync applied")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w4_post_sync_review") is True, "active W4 post-sync summary must confirm remote reflection")
    _require(active_summary.get("permanent_active_update_rule_installed") is True, "active W4 post-sync summary must preserve permanent rule")
    _require(active_summary.get("w4_canonical_sync_verified") is True, "active W4 post-sync summary must verify W4 canonical sync")
    _require(active_summary.get("validator_sync_repair_verified") is True, "active W4 post-sync summary must verify validator sync repair")
    _require(active_summary.get("w4_execution_performed") is True, "active W4 post-sync summary must preserve W4 execution")
    _require(active_summary.get("w4_execution_allowed") is False, "active W4 post-sync summary must keep execution disallowed")
    _require(active_summary.get("w4_execution_scope") == "synthetic_isolated_lab_only", "active W4 post-sync summary execution scope mismatch")
    _require(active_summary.get("synthetic_attack_cases_total") == 14, "active W4 post-sync summary synthetic_attack_cases_total must be 14")
    _require(active_summary.get("rollback_honesty_checks_required") == 6, "active W4 post-sync summary rollback_honesty_checks_required must be 6")
    _require(active_summary.get("rollback_honesty_checks_passed") == 6, "active W4 post-sync summary rollback_honesty_checks_passed must be 6")
    _require(active_summary.get("duplicate_detection_checks_required") == 5, "active W4 post-sync summary duplicate_detection_checks_required must be 5")
    _require(active_summary.get("duplicate_detection_checks_passed") == 5, "active W4 post-sync summary duplicate_detection_checks_passed must be 5")
    _require(active_summary.get("cost_enforcement_checks_required") == 3, "active W4 post-sync summary cost_enforcement_checks_required must be 3")
    _require(active_summary.get("cost_enforcement_checks_passed") == 3, "active W4 post-sync summary cost_enforcement_checks_passed must be 3")
    _require(active_summary.get("rhr_observed") == 1.0, "active W4 post-sync summary rhr_observed must be 1.0")
    _require(active_summary.get("ddr_observed") == 1.0, "active W4 post-sync summary ddr_observed must be 1.0")
    _require(active_summary.get("cer_observed") == 1.0, "active W4 post-sync summary cer_observed must be 1.0")
    _require(active_summary.get("w5_readiness_state") == "ready_for_preparation", "active W4 post-sync summary readiness state mismatch")
    _require(active_summary.get("w5_preparation_allowed_next") is True, "active W4 post-sync summary must allow W5 preparation")
    _require(active_summary.get("w5_execution_performed") is False, "active W4 post-sync summary must keep W5 execution false")
    _require(active_summary.get("w5_execution_allowed") is False, "active W4 post-sync summary must keep W5 execution disallowed")
    _require(active_summary.get("next_recommended_step") == IF08_W4_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W4 post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W4_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision",
        IF08_W4_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w4_post_sync_review: `true`",
        "w4_execution_scope: `synthetic_isolated_lab_only`",
        "synthetic_attack_cases_total: `14`",
        "rollback_honesty_checks: `6/6`",
        "duplicate_detection_checks: `5/5`",
        "cost_enforcement_checks: `3/3`",
        "w5_readiness_state: `ready_for_preparation`",
        "w5_preparation_allowed_next: `true`",
        "w5_execution_performed: `false`",
        "w5_execution_allowed: `false`",
        "next_recommended_step: `prepare_if08_w5_business_chaos_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W4_POST_SYNC_DECISION_PATH,
        IF08_W4_POST_SYNC_SUMMARY_PATH,
        IF08_W4_POST_SYNC_REPORT_PATH,
        IF08_W5_READINESS_MATRIX_PATH,
        IF08_W4_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W4_POST_SYNC_DOC_PATH,
    )
    external_available = all(path.exists() for path in external_project_paths)
    if not external_available:
        return

    decision = _load_json(IF08_W4_POST_SYNC_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "project W4 post-sync decision phase_id mismatch")
    _require(decision.get("phase_name") == IF08_W4_POST_SYNC_PHASE, "project W4 post-sync decision phase_name mismatch")
    _require(decision.get("decision") == "pass", "project W4 post-sync decision must be pass")
    _require(decision.get("status") == IF08_W4_POST_SYNC_STATUS, "project W4 post-sync decision status mismatch")
    _require(decision.get("source_phase") == IF08_W4_CONTROLLED_PHASE, "project W4 post-sync decision source phase mismatch")
    _require(decision.get("source_status") == IF08_W4_CONTROLLED_STATUS, "project W4 post-sync decision source status mismatch")
    _require(decision.get("source_project_sha") == IF08_W4_CONTROLLED_PROJECT_SHA, "project W4 post-sync decision source project sha mismatch")
    _require(decision.get("source_project_ci_state") == IF08_W4_CONTROLLED_CI_STATE, "project W4 post-sync decision source ci state mismatch")
    _require(decision.get("source_active_context_sha") == "474cc539098fb5af5fec552d6eddef0d73d30c42", "project W4 post-sync decision source active-context sha mismatch")
    _require(decision.get("w4_canonical_sync_verified") is True, "project W4 post-sync decision must verify W4 canonical sync")
    _require(decision.get("validator_sync_repair_verified") is True, "project W4 post-sync decision must verify validator sync repair")
    _require(decision.get("w4_metrics_verified") is True, "project W4 post-sync decision must verify W4 metrics")
    _require(decision.get("synthetic_attack_cases_total") == 14, "project W4 post-sync decision synthetic_attack_cases_total must be 14")
    _require(decision.get("rollback_honesty_checks") == "6/6", "project W4 post-sync decision rollback_honesty_checks mismatch")
    _require(decision.get("duplicate_detection_checks") == "5/5", "project W4 post-sync decision duplicate_detection_checks mismatch")
    _require(decision.get("cost_enforcement_checks") == "3/3", "project W4 post-sync decision cost_enforcement_checks mismatch")
    _require(decision.get("rhr_observed") == 1.0, "project W4 post-sync decision rhr_observed must be 1.0")
    _require(decision.get("ddr_observed") == 1.0, "project W4 post-sync decision ddr_observed must be 1.0")
    _require(decision.get("cer_observed") == 1.0, "project W4 post-sync decision cer_observed must be 1.0")
    _require(decision.get("w4_execution_scope") == "synthetic_isolated_lab_only", "project W4 post-sync decision execution scope mismatch")
    _require(decision.get("w5_readiness_state") == "ready_for_preparation", "project W4 post-sync decision readiness state mismatch")
    _require(decision.get("w5_preparation_allowed_next") is True, "project W4 post-sync decision must allow W5 preparation")
    _require(decision.get("w5_execution_performed") is False, "project W4 post-sync decision must keep W5 execution false")
    _require(decision.get("w5_execution_allowed") is False, "project W4 post-sync decision must keep W5 execution disallowed")
    _require(decision.get("next_recommended_step") == IF08_W4_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W4 post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W4 post-sync decision blocking_findings must be empty")
    _require(decision.get("invalid_findings") == [], "project W4 post-sync decision invalid_findings must be empty")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(decision.get(key) is False, f"project W4 post-sync decision {key} must be false")

    summary = _load_json(IF08_W4_POST_SYNC_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "project W4 post-sync summary phase_id mismatch")
    _require(summary.get("phase_name") == IF08_W4_POST_SYNC_PHASE, "project W4 post-sync summary phase_name mismatch")
    _require(summary.get("decision") == "pass", "project W4 post-sync summary must be pass")
    _require(summary.get("status") == IF08_W4_POST_SYNC_STATUS, "project W4 post-sync summary status mismatch")
    _require(summary.get("source_project_sha") == IF08_W4_CONTROLLED_PROJECT_SHA, "project W4 post-sync summary source project sha mismatch")
    _require(summary.get("source_project_ci_state") == IF08_W4_CONTROLLED_CI_STATE, "project W4 post-sync summary source ci state mismatch")
    _require(summary.get("source_active_context_sha") == "474cc539098fb5af5fec552d6eddef0d73d30c42", "project W4 post-sync summary source active-context sha mismatch")
    _require(summary.get("w4_canonical_sync_verified") is True, "project W4 post-sync summary must verify W4 canonical sync")
    _require(summary.get("validator_sync_repair_verified") is True, "project W4 post-sync summary must verify validator sync repair")
    _require(summary.get("w4_metrics_verified") is True, "project W4 post-sync summary must verify W4 metrics")
    _require(summary.get("synthetic_attack_cases_total") == 14, "project W4 post-sync summary synthetic_attack_cases_total must be 14")
    _require(summary.get("rollback_honesty_checks") == "6/6", "project W4 post-sync summary rollback_honesty_checks mismatch")
    _require(summary.get("duplicate_detection_checks") == "5/5", "project W4 post-sync summary duplicate_detection_checks mismatch")
    _require(summary.get("cost_enforcement_checks") == "3/3", "project W4 post-sync summary cost_enforcement_checks mismatch")
    _require(summary.get("w5_readiness_state") == "ready_for_preparation", "project W4 post-sync summary readiness state mismatch")
    _require(summary.get("w5_preparation_allowed_next") is True, "project W4 post-sync summary must allow W5 preparation")
    _require(summary.get("w5_execution_performed") is False, "project W4 post-sync summary must keep W5 execution false")
    _require(summary.get("w5_execution_allowed") is False, "project W4 post-sync summary must keep W5 execution disallowed")
    _require(summary.get("next_recommended_step") == IF08_W4_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W4 post-sync summary next step mismatch")

    readiness = _load_json(IF08_W5_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "project W5 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W5", "project W5 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Business chaos", "project W5 readiness wave_name mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project W5 readiness state mismatch")
    _require(readiness.get("w5_preparation_allowed_next") is True, "project W5 readiness must allow preparation")
    _require(readiness.get("w5_execution_performed") is False, "project W5 readiness must keep execution false")
    _require(readiness.get("w5_execution_allowed") is False, "project W5 readiness must keep execution disallowed")
    checks = {item.get("check_id"): item.get("passed") for item in readiness.get("checks", [])}
    for key in (
        "w4_controlled_execution_pass_confirmed",
        "w4_active_context_sync_confirmed",
        "validator_sync_repair_pass_confirmed",
        "w4_metrics_verified",
        "no_real_execution_surfaces",
        "no_blocking_findings_open",
        "w4_expected_artifacts_exist",
        "w5_preflight_not_executed",
        "w5_wave_contract_known",
    ):
        _require(checks.get(key) is True, f"project W5 readiness check {key} must be true")

    no_execution = _load_json(IF08_W4_POST_SYNC_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W4-POST-SYNC-REVIEW", "project W4 post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W4 post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W4_POST_SYNC_STATUS, "project W4 post-sync no_execution status mismatch")
    _require(no_execution.get("w5_execution_performed") is False, "project W4 post-sync no_execution must keep W5 execution false")
    _require(no_execution.get("w5_execution_allowed") is False, "project W4 post-sync no_execution must keep W5 execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(no_execution.get(key) is False, f"project W4 post-sync no_execution.{key} must be false")

    _mirror_contains(
        IF08_W4_POST_SYNC_REPORT_PATH,
        "IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision",
        "w4_canonical_sync_verified: `true`",
        "validator_sync_repair_verified: `true`",
        "w4_metrics_verified: `true`",
        "w5_readiness_state: `ready_for_preparation`",
        "w5_preparation_allowed_next: `true`",
        "w5_preflight_not_executed_yet: `true`",
        "real_quota_consumed: `false`",
        "next_recommended_step: `prepare_if08_w5_business_chaos_preflight_readiness`",
    )
    _mirror_contains(
        IF08_W4_POST_SYNC_DOC_PATH,
        "IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision",
        "ready_for_preparation",
        "prepare_if08_w5_business_chaos_preflight_readiness",
    )


def _check_if08_w5_business_chaos_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    _require(IF08_W5_CONTROLLED_ACTIVE_DECISION_PATH.exists(), "missing active IF08 W5 controlled decision artifact")
    _require(IF08_W5_CONTROLLED_ACTIVE_SUMMARY_PATH.exists(), "missing active IF08 W5 controlled summary artifact")
    _require(IF08_W5_CONTROLLED_ACTIVE_REPORT_PATH.exists(), "missing active IF08 W5 controlled report artifact")

    active_decision = _load_json(IF08_W5_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W5-BUSINESS-CHAOS-CONTROLLED-EXECUTION", "active W5 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W5 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W5_CONTROLLED_STATUS, "active W5 controlled decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF08_W5_CONTROLLED_PROJECT_SHA, "active W5 controlled decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF08_W5_CONTROLLED_CI_STATE, "active W5 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W5_CONTROLLED_PROJECT_CI_RUN_URL, "active W5 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W5 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W5 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_sync_applied") is True, "active W5 controlled decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w5_business_chaos_controlled_execution") is True, "active W5 controlled decision must confirm remote reflection")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W5_CONTROLLED_PHASE, "active W5 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W5_CONTROLLED_STATUS, "active W5 controlled decision latest status mismatch")
    _require(active_decision.get("previous_phase_verified") == IF08_W5_CONTROLLED_PREVIOUS_PHASE, "active W5 controlled decision previous phase mismatch")
    _require(active_decision.get("previous_status_verified") == IF08_W5_CONTROLLED_PREVIOUS_STATUS, "active W5 controlled decision previous status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF08_W5_CONTROLLED_SOURCE_PROJECT_SHA, "active W5 controlled decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF08_W5_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "active W5 controlled decision source active-context sha mismatch")
    _require(active_decision.get("execution_scope") == "synthetic_isolated_lab_only", "active W5 controlled decision execution_scope mismatch")
    _require(active_decision.get("w5_preflight_readiness_verified") is True, "active W5 controlled decision must preserve preflight readiness")
    _require(active_decision.get("w5_gap_repair_verified") is True, "active W5 controlled decision must preserve gap repair")
    _require(active_decision.get("w5_execution_performed") is True, "active W5 controlled decision must record execution performed")
    _require(active_decision.get("w5_execution_allowed") is False, "active W5 controlled decision must keep execution disallowed")
    _require(active_decision.get("executor_bot_count") == 14, "active W5 controlled decision executor_bot_count must be 14")
    _require(active_decision.get("synthetic_domain_count") == 7, "active W5 controlled decision synthetic_domain_count must be 7")
    _require(active_decision.get("critical_coverage_cells_total") == 12, "active W5 controlled decision critical_coverage_cells_total must be 12")
    _require(active_decision.get("critical_coverage_cells_passed") == 12, "active W5 controlled decision critical_coverage_cells_passed must be 12")
    _require(active_decision.get("critical_coverage_completion") == 1.0, "active W5 controlled decision critical_coverage_completion must be 1.0")
    _require(active_decision.get("business_scenarios_total") == 14, "active W5 controlled decision business_scenarios_total must be 14")
    _require(active_decision.get("business_scenarios_passed") == 14, "active W5 controlled decision business_scenarios_passed must be 14")
    _require(active_decision.get("business_scenarios_blocked_or_detected") == 14, "active W5 controlled decision business_scenarios_blocked_or_detected must be 14")
    _require(active_decision.get("sirene_oracle_mode") == "synthetic_transcript_only", "active W5 controlled decision sirene_oracle_mode mismatch")
    _require(active_decision.get("evidence_units_complete") is True, "active W5 controlled decision evidence_units_complete must be true")
    _require(active_decision.get("stop_conditions_respected") is True, "active W5 controlled decision stop_conditions_respected must be true")
    _require(active_decision.get("next_recommended_step") == IF08_W5_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W5 controlled decision next step mismatch")
    for key in (
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_decision.get(key) is False, f"active W5 controlled decision {key} must be false")

    active_summary = _load_json(IF08_W5_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W5-BUSINESS-CHAOS-CONTROLLED-EXECUTION", "active W5 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W5 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W5_CONTROLLED_STATUS, "active W5 controlled summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W5_CONTROLLED_PROJECT_SHA, "active W5 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W5_CONTROLLED_CI_STATE, "active W5 controlled summary ci state mismatch")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w5_business_chaos_controlled_execution") is True, "active W5 controlled summary must confirm remote reflection")
    _require(active_summary.get("previous_phase_verified") == IF08_W5_CONTROLLED_PREVIOUS_PHASE, "active W5 controlled summary previous phase mismatch")
    _require(active_summary.get("previous_status_verified") == IF08_W5_CONTROLLED_PREVIOUS_STATUS, "active W5 controlled summary previous status mismatch")
    _require(active_summary.get("execution_scope") == "synthetic_isolated_lab_only", "active W5 controlled summary execution_scope mismatch")
    _require(active_summary.get("w5_execution_performed") is True, "active W5 controlled summary must record execution performed")
    _require(active_summary.get("w5_execution_allowed") is False, "active W5 controlled summary must keep execution disallowed")
    _require(active_summary.get("executor_bot_count") == 14, "active W5 controlled summary executor_bot_count must be 14")
    _require(active_summary.get("synthetic_domain_count") == 7, "active W5 controlled summary synthetic_domain_count must be 7")
    _require(active_summary.get("critical_coverage_cells_passed") == 12, "active W5 controlled summary critical_coverage_cells_passed must be 12")
    _require(active_summary.get("critical_coverage_completion") == 1.0, "active W5 controlled summary critical_coverage_completion must be 1.0")
    _require(active_summary.get("next_recommended_step") == IF08_W5_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W5 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W5_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W5 Business Chaos Controlled Execution",
        "project_commit_sha: `5eb32158153bc5ff3db87d33c3c625f5b0df80fa`",
        "execution_scope: `synthetic_isolated_lab_only`",
        "w5_execution_performed: `true`",
        "critical_coverage_cells_passed: `12`",
        "critical_coverage_completion: `1.0`",
        "business_scenarios_blocked_or_detected: `14`",
        "post_sync_review_if08_w5_business_chaos_controlled_execution",
    )

    external_project_paths = (
        IF08_W5_CONTROLLED_DECISION_PATH,
        IF08_W5_CONTROLLED_SUMMARY_PATH,
        IF08_W5_CONTROLLED_REPORT_PATH,
        IF08_W5_CONTROLLED_LEDGER_PATH,
        IF08_W5_CONTROLLED_DOMAIN_RESULTS_PATH,
        IF08_W5_CONTROLLED_BOT_RESULTS_PATH,
        IF08_W5_CONTROLLED_COVERAGE_RESULTS_PATH,
        IF08_W5_CONTROLLED_ORACLE_RESULTS_PATH,
        IF08_W5_CONTROLLED_SAFETY_ATTESTATION_PATH,
        IF08_W5_CONTROLLED_NO_EXECUTION_PATH,
        IF08_W5_CONTROLLED_DOC_PATH,
    )
    if not all(path.exists() for path in external_project_paths):
        return

    decision = _load_json(IF08_W5_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W5-BUSINESS-CHAOS-CONTROLLED-EXECUTION", "project W5 controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W5 controlled decision must be pass")
    _require(decision.get("status") == IF08_W5_CONTROLLED_STATUS, "project W5 controlled decision status mismatch")
    _require(decision.get("source_active_context_sha") == IF08_W5_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "project W5 controlled decision source active-context sha mismatch")
    _require(decision.get("source_project_sha") == IF08_W5_CONTROLLED_SOURCE_PROJECT_SHA, "project W5 controlled decision source project sha mismatch")
    _require(decision.get("previous_phase_verified") == IF08_W5_CONTROLLED_PREVIOUS_PHASE, "project W5 controlled decision previous phase mismatch")
    _require(decision.get("previous_status_verified") == IF08_W5_CONTROLLED_PREVIOUS_STATUS, "project W5 controlled decision previous status mismatch")
    _require(decision.get("execution_scope") == "synthetic_isolated_lab_only", "project W5 controlled decision execution_scope mismatch")
    _require(decision.get("w5_preflight_readiness_verified") is True, "project W5 controlled decision must preserve preflight readiness")
    _require(decision.get("w5_gap_repair_verified") is True, "project W5 controlled decision must preserve gap repair")
    _require(decision.get("w5_execution_performed") is True, "project W5 controlled decision must record execution performed")
    _require(decision.get("w5_execution_allowed") is False, "project W5 controlled decision must keep execution disallowed")
    _require(decision.get("executor_bot_count") == 14, "project W5 controlled decision executor_bot_count must be 14")
    _require(decision.get("synthetic_domain_count") == 7, "project W5 controlled decision synthetic_domain_count must be 7")
    _require(decision.get("critical_coverage_cells_total") == 12, "project W5 controlled decision critical_coverage_cells_total must be 12")
    _require(decision.get("critical_coverage_cells_passed") == 12, "project W5 controlled decision critical_coverage_cells_passed must be 12")
    _require(decision.get("critical_coverage_completion") == 1.0, "project W5 controlled decision critical_coverage_completion must be 1.0")
    _require(decision.get("business_scenarios_total") == 14, "project W5 controlled decision business_scenarios_total must be 14")
    _require(decision.get("business_scenarios_blocked_or_detected") == 14, "project W5 controlled decision business_scenarios_blocked_or_detected must be 14")
    _require(decision.get("sirene_oracle_mode") == "synthetic_transcript_only", "project W5 controlled decision sirene_oracle_mode mismatch")
    _require(decision.get("blocking_findings") == [], "project W5 controlled decision blocking_findings must be empty")
    _require(decision.get("invalid_findings") == [], "project W5 controlled decision invalid_findings must be empty")
    _require(decision.get("next_recommended_step") == IF08_W5_CONTROLLED_NEXT_RECOMMENDED_STEP, "project W5 controlled decision next step mismatch")

    summary = _load_json(IF08_W5_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("decision") == "pass", "project W5 controlled summary must be pass")
    _require(summary.get("status") == IF08_W5_CONTROLLED_STATUS, "project W5 controlled summary status mismatch")
    _require(summary.get("source_project_sha") == IF08_W5_CONTROLLED_SOURCE_PROJECT_SHA, "project W5 controlled summary source project sha mismatch")
    _require(summary.get("source_active_context_sha") == IF08_W5_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "project W5 controlled summary source active-context sha mismatch")
    _require(summary.get("execution_scope") == "synthetic_isolated_lab_only", "project W5 controlled summary execution_scope mismatch")
    _require(summary.get("executor_bot_count") == 14, "project W5 controlled summary executor_bot_count must be 14")
    _require(summary.get("critical_coverage_completion") == 1.0, "project W5 controlled summary critical_coverage_completion must be 1.0")
    _require(summary.get("next_recommended_step") == IF08_W5_CONTROLLED_NEXT_RECOMMENDED_STEP, "project W5 controlled summary next step mismatch")

    domain_results = _load_json(IF08_W5_CONTROLLED_DOMAIN_RESULTS_PATH)
    _require(domain_results.get("phase_name") == IF08_W5_CONTROLLED_PHASE, "project W5 domain results phase_name mismatch")
    _require(domain_results.get("synthetic_domain_count") == 7, "project W5 domain results synthetic_domain_count must be 7")
    _require(len(domain_results.get("rows", [])) == 7, "project W5 domain results rows must be 7")

    bot_results = _load_json(IF08_W5_CONTROLLED_BOT_RESULTS_PATH)
    _require(bot_results.get("phase_name") == IF08_W5_CONTROLLED_PHASE, "project W5 bot results phase_name mismatch")
    _require(bot_results.get("executor_bot_count") == 14, "project W5 bot results executor_bot_count must be 14")
    _require(len(bot_results.get("rows", [])) == 14, "project W5 bot results rows must be 14")

    coverage = _load_json(IF08_W5_CONTROLLED_COVERAGE_RESULTS_PATH)
    _require(coverage.get("critical_coverage_cells_total") == 12, "project W5 coverage total mismatch")
    _require(coverage.get("critical_coverage_cells_passed") == 12, "project W5 coverage passed mismatch")
    _require(coverage.get("critical_coverage_completion") == 1.0, "project W5 coverage completion mismatch")

    oracle = _load_json(IF08_W5_CONTROLLED_ORACLE_RESULTS_PATH)
    _require(oracle.get("critical_coverage_completion") == 1.0, "project W5 oracle completion mismatch")
    for key in (
        "unauthorized_action_count",
        "false_approval_acceptance_count",
        "runtime_escape_count",
        "secret_or_tenant_leak_count",
        "real_audio_capture_count",
        "real_stt_tts_call_count",
        "mcp_real_activation_count",
        "memory_write_count",
        "external_network_call_count",
    ):
        _require(oracle.get(key) == 0, f"project W5 oracle {key} mismatch")
    _require(oracle.get("sirene_oracle_mode") == "synthetic_transcript_only", "project W5 oracle sirene_oracle_mode mismatch")

    safety = _load_json(IF08_W5_CONTROLLED_SAFETY_ATTESTATION_PATH)
    _require(safety.get("status") == IF08_W5_CONTROLLED_STATUS, "project W5 safety attestation status mismatch")
    _require(safety.get("deterministic_output_contract") is True, "project W5 safety attestation deterministic_output_contract mismatch")
    _require(len(safety.get("artifact_hashes", {})) == 10, "project W5 safety attestation artifact hash count mismatch")

    no_execution = _load_json(IF08_W5_CONTROLLED_NO_EXECUTION_PATH)
    _require(no_execution.get("status") == IF08_W5_CONTROLLED_STATUS, "project W5 no_execution status mismatch")
    _require(no_execution.get("decision") == "pass", "project W5 no_execution decision mismatch")
    _require(no_execution.get("w5_execution_performed") is True, "project W5 no_execution must record execution performed")
    _require(no_execution.get("w5_execution_allowed") is False, "project W5 no_execution must keep execution disallowed")

    _mirror_contains(
        IF08_W5_CONTROLLED_REPORT_PATH,
        "IF-08 W5 Business Chaos Controlled Execution",
        "Decision: pass",
        "Status: if08_w5_business_chaos_controlled_execution_pass",
        "Critical coverage: 12/12",
        "Business scenarios blocked or detected: 14",
        "synthetic_isolated_lab_only",
        "post_sync_review_if08_w5_business_chaos_controlled_execution",
    )
    _mirror_contains(
        IF08_W5_CONTROLLED_DOC_PATH,
        "IF-08 W5 Business Chaos Controlled Execution",
        "decision: pass",
        "post_sync_review_if08_w5_business_chaos_controlled_execution",
    )


def _check_if08_w5_post_sync_review_artifacts(state: dict[str, Any]) -> None:
    _require(IF08_W5_POST_SYNC_ACTIVE_DECISION_PATH.exists(), "missing active IF08 W5 post-sync decision artifact")
    _require(IF08_W5_POST_SYNC_ACTIVE_SUMMARY_PATH.exists(), "missing active IF08 W5 post-sync summary artifact")
    _require(IF08_W5_POST_SYNC_ACTIVE_REPORT_PATH.exists(), "missing active IF08 W5 post-sync report artifact")

    active_decision = _load_json(IF08_W5_POST_SYNC_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "active W5 post-sync decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W5 post-sync decision must be pass")
    _require(active_decision.get("status") == IF08_W5_POST_SYNC_STATUS, "active W5 post-sync decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF08_W5_POST_SYNC_PROJECT_SHA, "active W5 post-sync decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF08_W5_POST_SYNC_CI_STATE, "active W5 post-sync decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W5_POST_SYNC_PROJECT_CI_RUN_URL, "active W5 post-sync decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W5 post-sync decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W5 post-sync decision must confirm green CI")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active W5 post-sync decision pre-sync phase id mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF08_W5_CONTROLLED_STATUS, "active W5 post-sync decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF08_W5_POST_SYNC_SOURCE_ACTIVE_CONTEXT_SHA, "active W5 post-sync decision pre-sync sha mismatch")
    _require(active_decision.get("active_context_sync_applied") is True, "active W5 post-sync decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w5_post_sync_review") is True, "active W5 post-sync decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W5 post-sync decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W5_POST_SYNC_PHASE, "active W5 post-sync decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W5_POST_SYNC_STATUS, "active W5 post-sync decision latest status mismatch")
    _require(active_decision.get("previous_phase_verified") == IF08_W5_POST_SYNC_PREVIOUS_PHASE, "active W5 post-sync decision previous phase mismatch")
    _require(active_decision.get("previous_status_verified") == IF08_W5_POST_SYNC_PREVIOUS_STATUS, "active W5 post-sync decision previous status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF08_W5_POST_SYNC_SOURCE_PROJECT_SHA, "active W5 post-sync decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF08_W5_POST_SYNC_SOURCE_ACTIVE_CONTEXT_SHA, "active W5 post-sync decision source active-context sha mismatch")
    _require(active_decision.get("w5_canonical_sync_verified") is True, "active W5 post-sync decision must verify W5 canonical sync")
    _require(active_decision.get("w5_metrics_verified") is True, "active W5 post-sync decision must verify W5 metrics")
    _require(active_decision.get("w5_artifacts_complete") is True, "active W5 post-sync decision must verify W5 artifacts")
    _require(active_decision.get("w5_safety_attestation_verified") is True, "active W5 post-sync decision must verify W5 safety attestation")
    _require(active_decision.get("critical_coverage_cells_total") == 12, "active W5 post-sync decision critical_coverage_cells_total must be 12")
    _require(active_decision.get("critical_coverage_cells_passed") == 12, "active W5 post-sync decision critical_coverage_cells_passed must be 12")
    _require(active_decision.get("critical_coverage_completion") == 1.0, "active W5 post-sync decision critical_coverage_completion must be 1.0")
    _require(active_decision.get("business_scenarios_total") == 14, "active W5 post-sync decision business_scenarios_total must be 14")
    _require(active_decision.get("business_scenarios_passed") == 14, "active W5 post-sync decision business_scenarios_passed must be 14")
    _require(active_decision.get("business_scenarios_blocked_or_detected") == 14, "active W5 post-sync decision business_scenarios_blocked_or_detected must be 14")
    _require(active_decision.get("sirene_oracle_mode") == "synthetic_transcript_only", "active W5 post-sync decision sirene_oracle_mode mismatch")
    _require(active_decision.get("execution_scope") == "post_sync_review_only", "active W5 post-sync decision execution_scope mismatch")
    _require(active_decision.get("w6_readiness_state") == "ready_for_preparation", "active W5 post-sync decision readiness state mismatch")
    _require(active_decision.get("w6_preparation_allowed_next") is True, "active W5 post-sync decision must allow W6 preparation")
    _require(active_decision.get("w6_execution_performed") is False, "active W5 post-sync decision must keep W6 execution false")
    _require(active_decision.get("w6_execution_allowed") is False, "active W5 post-sync decision must keep W6 execution disallowed")
    _require(active_decision.get("future_ttr_required") == 0, "active W5 post-sync decision future_ttr_required must be 0")
    _require(active_decision.get("future_har_required") == 1.0, "active W5 post-sync decision future_har_required must be 1.0")
    _require(active_decision.get("minos_mechanical_required") is True, "active W5 post-sync decision minos_mechanical_required must be true")
    _require(active_decision.get("minos_semantic_required") is True, "active W5 post-sync decision minos_semantic_required must be true")
    _require(active_decision.get("anti_theater_review_required") is True, "active W5 post-sync decision anti_theater_review_required must be true")
    _require(active_decision.get("next_recommended_step") == IF08_W5_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W5 post-sync decision next step mismatch")
    for key in (
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_decision.get(key) is False, f"active W5 post-sync decision {key} must be false")

    active_summary = _load_json(IF08_W5_POST_SYNC_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "active W5 post-sync summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W5 post-sync summary must be pass")
    _require(active_summary.get("status") == IF08_W5_POST_SYNC_STATUS, "active W5 post-sync summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W5_POST_SYNC_PROJECT_SHA, "active W5 post-sync summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W5_POST_SYNC_CI_STATE, "active W5 post-sync summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W5_POST_SYNC_PROJECT_CI_RUN_URL, "active W5 post-sync summary ci url mismatch")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w5_post_sync_review") is True, "active W5 post-sync summary must confirm remote reflection")
    _require(active_summary.get("previous_phase_verified") == IF08_W5_POST_SYNC_PREVIOUS_PHASE, "active W5 post-sync summary previous phase mismatch")
    _require(active_summary.get("previous_status_verified") == IF08_W5_POST_SYNC_PREVIOUS_STATUS, "active W5 post-sync summary previous status mismatch")
    _require(active_summary.get("w5_canonical_sync_verified") is True, "active W5 post-sync summary must verify W5 canonical sync")
    _require(active_summary.get("w5_metrics_verified") is True, "active W5 post-sync summary must verify W5 metrics")
    _require(active_summary.get("w5_artifacts_complete") is True, "active W5 post-sync summary must verify W5 artifacts")
    _require(active_summary.get("w5_safety_attestation_verified") is True, "active W5 post-sync summary must verify W5 safety attestation")
    _require(active_summary.get("critical_coverage_cells_total") == 12, "active W5 post-sync summary critical_coverage_cells_total must be 12")
    _require(active_summary.get("critical_coverage_cells_passed") == 12, "active W5 post-sync summary critical_coverage_cells_passed must be 12")
    _require(active_summary.get("critical_coverage_completion") == 1.0, "active W5 post-sync summary critical_coverage_completion must be 1.0")
    _require(active_summary.get("business_scenarios_total") == 14, "active W5 post-sync summary business_scenarios_total must be 14")
    _require(active_summary.get("business_scenarios_blocked_or_detected") == 14, "active W5 post-sync summary business_scenarios_blocked_or_detected must be 14")
    _require(active_summary.get("sirene_oracle_mode") == "synthetic_transcript_only", "active W5 post-sync summary sirene_oracle_mode mismatch")
    _require(active_summary.get("execution_scope") == "post_sync_review_only", "active W5 post-sync summary execution_scope mismatch")
    _require(active_summary.get("w6_readiness_state") == "ready_for_preparation", "active W5 post-sync summary readiness state mismatch")
    _require(active_summary.get("w6_preparation_allowed_next") is True, "active W5 post-sync summary must allow W6 preparation")
    _require(active_summary.get("w6_execution_performed") is False, "active W5 post-sync summary must keep W6 execution false")
    _require(active_summary.get("w6_execution_allowed") is False, "active W5 post-sync summary must keep W6 execution disallowed")
    _require(active_summary.get("future_ttr_required") == 0, "active W5 post-sync summary future_ttr_required must be 0")
    _require(active_summary.get("future_har_required") == 1.0, "active W5 post-sync summary future_har_required must be 1.0")
    _require(active_summary.get("minos_mechanical_required") is True, "active W5 post-sync summary minos_mechanical_required must be true")
    _require(active_summary.get("minos_semantic_required") is True, "active W5 post-sync summary minos_semantic_required must be true")
    _require(active_summary.get("anti_theater_review_required") is True, "active W5 post-sync summary anti_theater_review_required must be true")
    _require(active_summary.get("next_recommended_step") == IF08_W5_POST_SYNC_NEXT_RECOMMENDED_STEP, "active W5 post-sync summary next step mismatch")

    _mirror_contains(
        IF08_W5_POST_SYNC_ACTIVE_REPORT_PATH,
        "IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision",
        IF08_W5_POST_SYNC_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w5_post_sync_review: `true`",
        "previous_phase_verified: `IF-08 W5 Business Chaos Controlled Execution`",
        "w5_canonical_sync_verified: `true`",
        "critical_coverage_cells_passed: `12`",
        "business_scenarios_blocked_or_detected: `14`",
        "execution_scope: `post_sync_review_only`",
        "w6_readiness_state: `ready_for_preparation`",
        "future_ttr_required: `0`",
        "future_har_required: `1.0`",
        "next_recommended_step: `prepare_if08_w6_final_audit_preflight_readiness`",
    )

    external_project_paths = (
        IF08_W5_POST_SYNC_DECISION_PATH,
        IF08_W5_POST_SYNC_SUMMARY_PATH,
        IF08_W5_POST_SYNC_REPORT_PATH,
        IF08_W6_READINESS_MATRIX_PATH,
        IF08_W5_POST_SYNC_NO_EXECUTION_PATH,
        IF08_W5_POST_SYNC_DOC_PATH,
    )
    if not all(path.exists() for path in external_project_paths):
        return

    decision = _load_json(IF08_W5_POST_SYNC_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "project W5 post-sync decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W5 post-sync decision must be pass")
    _require(decision.get("status") == IF08_W5_POST_SYNC_STATUS, "project W5 post-sync decision status mismatch")
    _require(decision.get("source_active_context_sha") == IF08_W5_POST_SYNC_SOURCE_ACTIVE_CONTEXT_SHA, "project W5 post-sync decision source active-context sha mismatch")
    _require(decision.get("source_project_sha") == IF08_W5_POST_SYNC_SOURCE_PROJECT_SHA, "project W5 post-sync decision source project sha mismatch")
    _require(decision.get("previous_phase_verified") == IF08_W5_POST_SYNC_PREVIOUS_PHASE, "project W5 post-sync decision previous phase mismatch")
    _require(decision.get("previous_status_verified") == IF08_W5_POST_SYNC_PREVIOUS_STATUS, "project W5 post-sync decision previous status mismatch")
    _require(decision.get("w5_canonical_sync_verified") is True, "project W5 post-sync decision must verify W5 canonical sync")
    _require(decision.get("w5_metrics_verified") is True, "project W5 post-sync decision must verify W5 metrics")
    _require(decision.get("w5_artifacts_complete") is True, "project W5 post-sync decision must verify W5 artifacts")
    _require(decision.get("w5_safety_attestation_verified") is True, "project W5 post-sync decision must verify W5 safety attestation")
    _require(decision.get("critical_coverage_cells_total") == 12, "project W5 post-sync decision critical_coverage_cells_total must be 12")
    _require(decision.get("critical_coverage_cells_passed") == 12, "project W5 post-sync decision critical_coverage_cells_passed must be 12")
    _require(decision.get("critical_coverage_completion") == 1.0, "project W5 post-sync decision critical_coverage_completion must be 1.0")
    _require(decision.get("business_scenarios_total") == 14, "project W5 post-sync decision business_scenarios_total must be 14")
    _require(decision.get("business_scenarios_blocked_or_detected") == 14, "project W5 post-sync decision business_scenarios_blocked_or_detected must be 14")
    _require(decision.get("sirene_oracle_mode") == "synthetic_transcript_only", "project W5 post-sync decision sirene_oracle_mode mismatch")
    _require(decision.get("w6_readiness_state") == "ready_for_preparation", "project W5 post-sync decision readiness state mismatch")
    _require(decision.get("w6_preparation_allowed_next") is True, "project W5 post-sync decision must allow W6 preparation")
    _require(decision.get("w6_execution_performed") is False, "project W5 post-sync decision must keep W6 execution false")
    _require(decision.get("w6_execution_allowed") is False, "project W5 post-sync decision must keep W6 execution disallowed")
    _require(decision.get("future_ttr_required") == 0, "project W5 post-sync decision future_ttr_required must be 0")
    _require(decision.get("future_har_required") == 1.0, "project W5 post-sync decision future_har_required must be 1.0")
    _require(decision.get("minos_mechanical_required") is True, "project W5 post-sync decision minos_mechanical_required must be true")
    _require(decision.get("minos_semantic_required") is True, "project W5 post-sync decision minos_semantic_required must be true")
    _require(decision.get("anti_theater_review_required") is True, "project W5 post-sync decision anti_theater_review_required must be true")
    _require(decision.get("execution_scope") == "post_sync_review_only", "project W5 post-sync decision execution_scope mismatch")
    _require(decision.get("next_recommended_step") == IF08_W5_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W5 post-sync decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W5 post-sync decision blocking_findings must be empty")
    _require(decision.get("invalid_findings") == [], "project W5 post-sync decision invalid_findings must be empty")
    for key in (
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(decision.get(key) is False, f"project W5 post-sync decision {key} must be false")

    summary = _load_json(IF08_W5_POST_SYNC_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "project W5 post-sync summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W5 post-sync summary must be pass")
    _require(summary.get("status") == IF08_W5_POST_SYNC_STATUS, "project W5 post-sync summary status mismatch")
    _require(summary.get("source_project_sha") == IF08_W5_POST_SYNC_SOURCE_PROJECT_SHA, "project W5 post-sync summary source project sha mismatch")
    _require(summary.get("source_active_context_sha") == IF08_W5_POST_SYNC_SOURCE_ACTIVE_CONTEXT_SHA, "project W5 post-sync summary source active-context sha mismatch")
    _require(summary.get("w5_canonical_sync_verified") is True, "project W5 post-sync summary must verify W5 canonical sync")
    _require(summary.get("w5_metrics_verified") is True, "project W5 post-sync summary must verify W5 metrics")
    _require(summary.get("w5_artifacts_complete") is True, "project W5 post-sync summary must verify W5 artifacts")
    _require(summary.get("w5_safety_attestation_verified") is True, "project W5 post-sync summary must verify W5 safety attestation")
    _require(summary.get("critical_coverage_cells_total") == 12, "project W5 post-sync summary critical_coverage_cells_total must be 12")
    _require(summary.get("critical_coverage_cells_passed") == 12, "project W5 post-sync summary critical_coverage_cells_passed must be 12")
    _require(summary.get("critical_coverage_completion") == 1.0, "project W5 post-sync summary critical_coverage_completion must be 1.0")
    _require(summary.get("business_scenarios_total") == 14, "project W5 post-sync summary business_scenarios_total must be 14")
    _require(summary.get("business_scenarios_blocked_or_detected") == 14, "project W5 post-sync summary business_scenarios_blocked_or_detected must be 14")
    _require(summary.get("sirene_oracle_mode") == "synthetic_transcript_only", "project W5 post-sync summary sirene_oracle_mode mismatch")
    _require(summary.get("w6_readiness_state") == "ready_for_preparation", "project W5 post-sync summary readiness state mismatch")
    _require(summary.get("w6_preparation_allowed_next") is True, "project W5 post-sync summary must allow W6 preparation")
    _require(summary.get("w6_execution_performed") is False, "project W5 post-sync summary must keep W6 execution false")
    _require(summary.get("w6_execution_allowed") is False, "project W5 post-sync summary must keep W6 execution disallowed")
    _require(summary.get("future_ttr_required") == 0, "project W5 post-sync summary future_ttr_required must be 0")
    _require(summary.get("future_har_required") == 1.0, "project W5 post-sync summary future_har_required must be 1.0")
    _require(summary.get("minos_mechanical_required") is True, "project W5 post-sync summary minos_mechanical_required must be true")
    _require(summary.get("minos_semantic_required") is True, "project W5 post-sync summary minos_semantic_required must be true")
    _require(summary.get("anti_theater_review_required") is True, "project W5 post-sync summary anti_theater_review_required must be true")
    _require(summary.get("execution_scope") == "post_sync_review_only", "project W5 post-sync summary execution_scope mismatch")
    _require(summary.get("next_recommended_step") == IF08_W5_POST_SYNC_NEXT_RECOMMENDED_STEP, "project W5 post-sync summary next step mismatch")

    readiness = _load_json(IF08_W6_READINESS_MATRIX_PATH)
    _require(readiness.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "project W6 readiness phase_id mismatch")
    _require(readiness.get("wave_id") == "W6", "project W6 readiness wave_id mismatch")
    _require(readiness.get("wave_name") == "Final audit", "project W6 readiness wave_name mismatch")
    _require(readiness.get("wave_objective") == "anti-theater final", "project W6 readiness objective mismatch")
    _require(readiness.get("readiness_state") == "ready_for_preparation", "project W6 readiness state mismatch")
    _require(readiness.get("w6_preparation_allowed_next") is True, "project W6 readiness must allow preparation")
    _require(readiness.get("w6_execution_performed") is False, "project W6 readiness must keep execution false")
    _require(readiness.get("w6_execution_allowed") is False, "project W6 readiness must keep execution disallowed")
    _require(readiness.get("future_ttr_required") == 0, "project W6 readiness future_ttr_required must be 0")
    _require(readiness.get("future_har_required") == 1.0, "project W6 readiness future_har_required must be 1.0")
    _require(readiness.get("minos_mechanical_required") is True, "project W6 readiness minos_mechanical_required must be true")
    _require(readiness.get("minos_semantic_required") is True, "project W6 readiness minos_semantic_required must be true")
    _require(readiness.get("anti_theater_review_required") is True, "project W6 readiness anti_theater_review_required must be true")
    checks = {item.get("check_id"): item.get("passed") for item in readiness.get("checks", [])}
    for key in (
        "w5_controlled_execution_pass_canonical",
        "w5_active_context_sync_verified",
        "w5_artifacts_exist_and_parse",
        "w5_safety_locks_preserved",
        "w5_coverage_complete",
        "w5_evidence_units_complete",
        "w5_stop_conditions_respected",
        "minos_mechanical_contract_or_requirement_declared",
        "minos_semantic_contract_or_requirement_declared",
        "future_ttr_and_har_declared",
        "w6_execution_flags_false",
    ):
        _require(checks.get(key) is True, f"project W6 readiness check {key} must be true")

    no_execution = _load_json(IF08_W5_POST_SYNC_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W5-POST-SYNC-REVIEW", "project W5 post-sync no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W5 post-sync no_execution must be pass")
    _require(no_execution.get("status") == IF08_W5_POST_SYNC_STATUS, "project W5 post-sync no_execution status mismatch")
    _require(no_execution.get("execution_scope") == "post_sync_review_only", "project W5 post-sync no_execution execution_scope mismatch")
    _require(no_execution.get("w6_execution_performed") is False, "project W5 post-sync no_execution must keep W6 execution false")
    _require(no_execution.get("w6_execution_allowed") is False, "project W5 post-sync no_execution must keep W6 execution disallowed")
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(no_execution.get(key) is False, f"project W5 post-sync no_execution.{key} must be false")

    _mirror_contains(
        IF08_W5_POST_SYNC_REPORT_PATH,
        "IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision",
        "Decision: pass",
        "Status: if08_w5_post_sync_review_w6_readiness_pass",
        "source_active_context_sha: `a89f90c691965a104c99964f3b256d08758605af`",
        "source_project_sha: `5eb32158153bc5ff3db87d33c3c625f5b0df80fa`",
        "W5 canonical sync verified: `true`",
        "Critical coverage: `12/12`",
        "Business scenarios blocked or detected: `14`",
        "W6 readiness state: `ready_for_preparation`",
        "future_ttr_required: `0`",
        "future_har_required: `1.0`",
        "next_recommended_step: `prepare_if08_w6_final_audit_preflight_readiness`",
    )
    _mirror_contains(
        IF08_W5_POST_SYNC_DOC_PATH,
        "IF-08 W5 Post-Sync Review",
        "decision: pass",
        "w6_readiness_state: ready_for_preparation",
        "next_recommended_step: prepare_if08_w6_final_audit_preflight_readiness",
    )


def _check_if08_w6_final_audit_preflight_artifacts(state: dict[str, Any]) -> None:
    _require(IF08_W6_PREFLIGHT_ACTIVE_DECISION_PATH.exists(), "missing active IF08 W6 preflight decision artifact")
    _require(IF08_W6_PREFLIGHT_ACTIVE_SUMMARY_PATH.exists(), "missing active IF08 W6 preflight summary artifact")
    _require(IF08_W6_PREFLIGHT_ACTIVE_REPORT_PATH.exists(), "missing active IF08 W6 preflight report artifact")

    active_decision = _load_json(IF08_W6_PREFLIGHT_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W6-FINAL-AUDIT-PREFLIGHT-READINESS", "active W6 preflight decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W6 preflight decision must be pass")
    _require(active_decision.get("status") == IF08_W6_PREFLIGHT_STATUS, "active W6 preflight decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF08_W6_PREFLIGHT_PROJECT_SHA, "active W6 preflight decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF08_W6_PREFLIGHT_CI_STATE, "active W6 preflight decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W6_PREFLIGHT_PROJECT_CI_RUN_URL, "active W6 preflight decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W6 preflight decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W6 preflight decision must confirm green CI")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active W6 preflight decision pre-sync phase id mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF08_W6_PREFLIGHT_PREVIOUS_STATUS, "active W6 preflight decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF08_W6_PREFLIGHT_SOURCE_ACTIVE_CONTEXT_SHA, "active W6 preflight decision pre-sync sha mismatch")
    _require(active_decision.get("active_context_sync_applied") is True, "active W6 preflight decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w6_final_audit_preflight_readiness") is True, "active W6 preflight decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W6 preflight decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W6_PREFLIGHT_PHASE, "active W6 preflight decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W6_PREFLIGHT_STATUS, "active W6 preflight decision latest status mismatch")
    _require(active_decision.get("previous_phase_verified") == IF08_W6_PREFLIGHT_PREVIOUS_PHASE, "active W6 preflight decision previous phase mismatch")
    _require(active_decision.get("previous_status_verified") == IF08_W6_PREFLIGHT_PREVIOUS_STATUS, "active W6 preflight decision previous status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF08_W6_PREFLIGHT_SOURCE_PROJECT_SHA, "active W6 preflight decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF08_W6_PREFLIGHT_SOURCE_ACTIVE_CONTEXT_SHA, "active W6 preflight decision source active-context sha mismatch")
    _require(active_decision.get("w5_post_sync_review_verified") is True, "active W6 preflight decision must verify W5 post-sync review")
    _require(active_decision.get("w5_metrics_verified") is True, "active W6 preflight decision must verify W5 metrics")
    _require(active_decision.get("w5_artifacts_complete") is True, "active W6 preflight decision must verify W5 artifacts")
    _require(active_decision.get("w5_safety_attestation_verified") is True, "active W6 preflight decision must verify W5 safety attestation")
    _require(active_decision.get("w6_preflight_readiness") is True, "active W6 preflight decision must verify W6 preflight readiness")
    _require(active_decision.get("readiness_coverage") == 1.0, "active W6 preflight decision readiness_coverage must be 1.0")
    _require(active_decision.get("required_preflight_checks") == 10, "active W6 preflight decision required_preflight_checks must be 10")
    _require(active_decision.get("ready_preflight_checks") == 10, "active W6 preflight decision ready_preflight_checks must be 10")
    _require(active_decision.get("execution_scope") == "preflight_readiness_only", "active W6 preflight decision execution_scope mismatch")
    _require(active_decision.get("w6_readiness_state") == "ready_for_controlled_execution", "active W6 preflight decision readiness state mismatch")
    _require(active_decision.get("w6_preparation_allowed_next") is True, "active W6 preflight decision must allow next step")
    _require(active_decision.get("w6_execution_performed") is False, "active W6 preflight decision must keep W6 execution false")
    _require(active_decision.get("w6_execution_allowed") is False, "active W6 preflight decision must keep W6 execution disallowed")
    _require(active_decision.get("future_ttr_required") == 0, "active W6 preflight decision future_ttr_required must be 0")
    _require(active_decision.get("future_har_required") == 1.0, "active W6 preflight decision future_har_required must be 1.0")
    _require(active_decision.get("minos_mechanical_required") is True, "active W6 preflight decision minos_mechanical_required must be true")
    _require(active_decision.get("minos_semantic_required") is True, "active W6 preflight decision minos_semantic_required must be true")
    _require(active_decision.get("minos_mechanical_readiness") is True, "active W6 preflight decision minos_mechanical_readiness must be true")
    _require(active_decision.get("minos_semantic_readiness") is True, "active W6 preflight decision minos_semantic_readiness must be true")
    _require(active_decision.get("anti_theater_review_required") is True, "active W6 preflight decision anti_theater_review_required must be true")
    _require(active_decision.get("ttr_har_threshold_contract_created") is True, "active W6 preflight decision threshold contract must be true")
    _require(active_decision.get("stop_condition_matrix_created") is True, "active W6 preflight decision stop condition matrix must be true")
    _require(active_decision.get("no_execution_attestation_created") is True, "active W6 preflight decision no_execution attestation must be true")
    _require(active_decision.get("next_recommended_step") == IF08_W6_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W6 preflight decision next step mismatch")
    for key in (
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_decision.get(key) is False, f"active W6 preflight decision {key} must be false")

    active_summary = _load_json(IF08_W6_PREFLIGHT_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W6-FINAL-AUDIT-PREFLIGHT-READINESS", "active W6 preflight summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W6 preflight summary must be pass")
    _require(active_summary.get("status") == IF08_W6_PREFLIGHT_STATUS, "active W6 preflight summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W6_PREFLIGHT_PROJECT_SHA, "active W6 preflight summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W6_PREFLIGHT_CI_STATE, "active W6 preflight summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W6_PREFLIGHT_PROJECT_CI_RUN_URL, "active W6 preflight summary ci url mismatch")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w6_final_audit_preflight_readiness") is True, "active W6 preflight summary must confirm remote reflection")
    _require(active_summary.get("previous_phase_verified") == IF08_W6_PREFLIGHT_PREVIOUS_PHASE, "active W6 preflight summary previous phase mismatch")
    _require(active_summary.get("previous_status_verified") == IF08_W6_PREFLIGHT_PREVIOUS_STATUS, "active W6 preflight summary previous status mismatch")
    _require(active_summary.get("w5_post_sync_review_verified") is True, "active W6 preflight summary must verify W5 post-sync review")
    _require(active_summary.get("w5_metrics_verified") is True, "active W6 preflight summary must verify W5 metrics")
    _require(active_summary.get("w5_artifacts_complete") is True, "active W6 preflight summary must verify W5 artifacts")
    _require(active_summary.get("w5_safety_attestation_verified") is True, "active W6 preflight summary must verify W5 safety attestation")
    _require(active_summary.get("w6_preflight_readiness") is True, "active W6 preflight summary must verify W6 preflight readiness")
    _require(active_summary.get("readiness_coverage") == 1.0, "active W6 preflight summary readiness_coverage must be 1.0")
    _require(active_summary.get("required_preflight_checks") == 10, "active W6 preflight summary required_preflight_checks must be 10")
    _require(active_summary.get("ready_preflight_checks") == 10, "active W6 preflight summary ready_preflight_checks must be 10")
    _require(active_summary.get("execution_scope") == "preflight_readiness_only", "active W6 preflight summary execution_scope mismatch")
    _require(active_summary.get("w6_readiness_state") == "ready_for_controlled_execution", "active W6 preflight summary readiness state mismatch")
    _require(active_summary.get("w6_preparation_allowed_next") is True, "active W6 preflight summary must allow next step")
    _require(active_summary.get("w6_execution_performed") is False, "active W6 preflight summary must keep W6 execution false")
    _require(active_summary.get("w6_execution_allowed") is False, "active W6 preflight summary must keep W6 execution disallowed")
    _require(active_summary.get("future_ttr_required") == 0, "active W6 preflight summary future_ttr_required must be 0")
    _require(active_summary.get("future_har_required") == 1.0, "active W6 preflight summary future_har_required must be 1.0")
    _require(active_summary.get("minos_mechanical_required") is True, "active W6 preflight summary minos_mechanical_required must be true")
    _require(active_summary.get("minos_semantic_required") is True, "active W6 preflight summary minos_semantic_required must be true")
    _require(active_summary.get("minos_mechanical_readiness") is True, "active W6 preflight summary minos_mechanical_readiness must be true")
    _require(active_summary.get("minos_semantic_readiness") is True, "active W6 preflight summary minos_semantic_readiness must be true")
    _require(active_summary.get("anti_theater_review_required") is True, "active W6 preflight summary anti_theater_review_required must be true")
    _require(active_summary.get("next_recommended_step") == IF08_W6_PREFLIGHT_NEXT_RECOMMENDED_STEP, "active W6 preflight summary next step mismatch")

    _mirror_contains(
        IF08_W6_PREFLIGHT_ACTIVE_REPORT_PATH,
        "IF-08 W6 Final Audit Preflight Readiness",
        IF08_W6_PREFLIGHT_PROJECT_SHA,
        "CI_GREEN_CONFIRMED",
        "active_context_remote_main_reflects_if08_w6_final_audit_preflight_readiness: `true`",
        "previous_phase_verified: `IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision`",
        "w6_preflight_readiness: `true`",
        "readiness_coverage: `1.0`",
        "w6_readiness_state: `ready_for_controlled_execution`",
        "future_ttr_required: `0`",
        "future_har_required: `1.0`",
        "next_recommended_step: `execute_if08_w6_final_audit_controlled_execution`",
    )

    external_project_paths = (
        IF08_W6_PREFLIGHT_DECISION_PATH,
        IF08_W6_PREFLIGHT_SUMMARY_PATH,
        IF08_W6_PREFLIGHT_REPORT_PATH,
        IF08_W6_MINOS_MECHANICAL_PATH,
        IF08_W6_MINOS_SEMANTIC_PATH,
        IF08_W6_THRESHOLD_CONTRACT_PATH,
        IF08_W6_STOP_MATRIX_PATH,
        IF08_W6_NO_EXECUTION_PATH,
        IF08_W6_PREFLIGHT_DOC_PATH,
    )
    if not all(path.exists() for path in external_project_paths):
        return

    decision = _load_json(IF08_W6_PREFLIGHT_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-08-W6-FINAL-AUDIT-PREFLIGHT-READINESS", "project W6 preflight decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W6 preflight decision must be pass")
    _require(decision.get("status") == IF08_W6_PREFLIGHT_STATUS, "project W6 preflight decision status mismatch")
    _require(decision.get("source_active_context_sha") == IF08_W6_PREFLIGHT_SOURCE_ACTIVE_CONTEXT_SHA, "project W6 preflight decision source active-context sha mismatch")
    _require(decision.get("source_project_sha") == IF08_W6_PREFLIGHT_SOURCE_PROJECT_SHA, "project W6 preflight decision source project sha mismatch")
    _require(decision.get("previous_phase_verified") == IF08_W6_PREFLIGHT_PREVIOUS_PHASE, "project W6 preflight decision previous phase mismatch")
    _require(decision.get("previous_status_verified") == IF08_W6_PREFLIGHT_PREVIOUS_STATUS, "project W6 preflight decision previous status mismatch")
    _require(decision.get("w5_post_sync_review_verified") is True, "project W6 preflight decision must verify W5 post-sync review")
    _require(decision.get("w5_metrics_verified") is True, "project W6 preflight decision must verify W5 metrics")
    _require(decision.get("w5_artifacts_complete") is True, "project W6 preflight decision must verify W5 artifacts")
    _require(decision.get("w5_safety_attestation_verified") is True, "project W6 preflight decision must verify W5 safety attestation")
    _require(decision.get("w6_preflight_readiness") is True, "project W6 preflight decision must verify W6 preflight readiness")
    _require(decision.get("readiness_coverage") == 1.0, "project W6 preflight decision readiness_coverage must be 1.0")
    _require(decision.get("required_preflight_checks") == 10, "project W6 preflight decision required_preflight_checks must be 10")
    _require(decision.get("ready_preflight_checks") == 10, "project W6 preflight decision ready_preflight_checks must be 10")
    _require(decision.get("execution_scope") == "preflight_readiness_only", "project W6 preflight decision execution_scope mismatch")
    _require(decision.get("w6_readiness_state") == "ready_for_controlled_execution", "project W6 preflight decision readiness state mismatch")
    _require(decision.get("w6_preparation_allowed_next") is True, "project W6 preflight decision must allow next step")
    _require(decision.get("w6_execution_performed") is False, "project W6 preflight decision must keep W6 execution false")
    _require(decision.get("w6_execution_allowed") is False, "project W6 preflight decision must keep W6 execution disallowed")
    _require(decision.get("future_ttr_required") == 0, "project W6 preflight decision future_ttr_required must be 0")
    _require(decision.get("future_har_required") == 1.0, "project W6 preflight decision future_har_required must be 1.0")
    _require(decision.get("minos_mechanical_required") is True, "project W6 preflight decision minos_mechanical_required must be true")
    _require(decision.get("minos_semantic_required") is True, "project W6 preflight decision minos_semantic_required must be true")
    _require(decision.get("minos_mechanical_readiness") is True, "project W6 preflight decision minos_mechanical_readiness must be true")
    _require(decision.get("minos_semantic_readiness") is True, "project W6 preflight decision minos_semantic_readiness must be true")
    _require(decision.get("anti_theater_review_required") is True, "project W6 preflight decision anti_theater_review_required must be true")
    _require(decision.get("ttr_har_threshold_contract_created") is True, "project W6 preflight decision threshold contract must be true")
    _require(decision.get("stop_condition_matrix_created") is True, "project W6 preflight decision stop condition matrix must be true")
    _require(decision.get("no_execution_attestation_created") is True, "project W6 preflight decision no_execution attestation must be true")
    _require(decision.get("next_recommended_step") == IF08_W6_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W6 preflight decision next step mismatch")
    _require(decision.get("blocking_findings") == [], "project W6 preflight decision blocking_findings must be empty")
    _require(decision.get("invalid_findings") == [], "project W6 preflight decision invalid_findings must be empty")

    summary = _load_json(IF08_W6_PREFLIGHT_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W6-FINAL-AUDIT-PREFLIGHT-READINESS", "project W6 preflight summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project W6 preflight summary must be pass")
    _require(summary.get("status") == IF08_W6_PREFLIGHT_STATUS, "project W6 preflight summary status mismatch")
    _require(summary.get("source_project_sha") == IF08_W6_PREFLIGHT_SOURCE_PROJECT_SHA, "project W6 preflight summary source project sha mismatch")
    _require(summary.get("source_active_context_sha") == IF08_W6_PREFLIGHT_SOURCE_ACTIVE_CONTEXT_SHA, "project W6 preflight summary source active-context sha mismatch")
    _require(summary.get("w6_preflight_readiness") is True, "project W6 preflight summary must verify W6 preflight readiness")
    _require(summary.get("readiness_coverage") == 1.0, "project W6 preflight summary readiness_coverage must be 1.0")
    _require(summary.get("required_preflight_checks") == 10, "project W6 preflight summary required_preflight_checks must be 10")
    _require(summary.get("ready_preflight_checks") == 10, "project W6 preflight summary ready_preflight_checks must be 10")
    _require(summary.get("w6_readiness_state") == "ready_for_controlled_execution", "project W6 preflight summary readiness state mismatch")
    _require(summary.get("next_recommended_step") == IF08_W6_PREFLIGHT_NEXT_RECOMMENDED_STEP, "project W6 preflight summary next step mismatch")

    mechanical = _load_json(IF08_W6_MINOS_MECHANICAL_PATH)
    _require(mechanical.get("bot_name") == "Minos-Mechanical", "project W6 mechanical matrix bot_name mismatch")
    _require(mechanical.get("readiness_state") == "ready", "project W6 mechanical matrix readiness_state mismatch")
    _require(mechanical.get("ready_for_controlled_execution") is True, "project W6 mechanical matrix must be ready")
    _require(mechanical.get("future_execution_now") is False, "project W6 mechanical matrix future_execution_now must be false")

    semantic = _load_json(IF08_W6_MINOS_SEMANTIC_PATH)
    _require(semantic.get("bot_name") == "Minos-Semantic", "project W6 semantic matrix bot_name mismatch")
    _require(semantic.get("readiness_state") == "ready", "project W6 semantic matrix readiness_state mismatch")
    _require(semantic.get("ready_for_controlled_execution") is True, "project W6 semantic matrix must be ready")
    _require(semantic.get("future_execution_now") is False, "project W6 semantic matrix future_execution_now must be false")

    threshold = _load_json(IF08_W6_THRESHOLD_CONTRACT_PATH)
    _require(threshold.get("future_ttr_required") == 0, "project W6 threshold contract future_ttr_required must be 0")
    _require(threshold.get("future_har_required") == 1.0, "project W6 threshold contract future_har_required must be 1.0")
    _require(threshold.get("threshold_contract_ready") is True, "project W6 threshold contract must be ready")
    _require(threshold.get("ttr_har_threshold_contract_created") is True, "project W6 threshold contract must be created")

    stop_matrix = _load_json(IF08_W6_STOP_MATRIX_PATH)
    _require(stop_matrix.get("stop_condition_matrix_created") is True, "project W6 stop matrix must be created")
    _require(len(stop_matrix.get("stop_conditions", [])) == 5, "project W6 stop matrix must contain 5 stop conditions")

    no_execution = _load_json(IF08_W6_NO_EXECUTION_PATH)
    _require(no_execution.get("phase_id") == "IF-08-W6-FINAL-AUDIT-PREFLIGHT-READINESS", "project W6 no_execution phase_id mismatch")
    _require(no_execution.get("decision") == "pass", "project W6 no_execution must be pass")
    _require(no_execution.get("status") == IF08_W6_PREFLIGHT_STATUS, "project W6 no_execution status mismatch")
    _require(no_execution.get("execution_scope") == "preflight_readiness_only", "project W6 no_execution execution_scope mismatch")
    _require(no_execution.get("w6_execution_performed") is False, "project W6 no_execution must keep W6 execution false")
    _require(no_execution.get("w6_execution_allowed") is False, "project W6 no_execution must keep W6 execution disallowed")

    _mirror_contains(
        IF08_W6_PREFLIGHT_REPORT_PATH,
        "IF-08 W6 Final Audit Preflight Readiness",
        "Decision: pass",
        "Status: if08_w6_final_audit_preflight_readiness_pass",
        "source_active_context_sha: `fabb8b29bedf0222975f54e1c8e496fd72336689`",
        "source_project_sha: `e9dfae63206523f26fce5df907945952c7351ad5`",
        "Minos-Mechanical readiness: `true`",
        "Minos-Semantic readiness: `true`",
        "TTR/HAR contract ready: `true`",
        "Readiness coverage: `1.000000`",
        "next_recommended_step: `execute_if08_w6_final_audit_controlled_execution`",
    )
    _mirror_contains(
        IF08_W6_PREFLIGHT_DOC_PATH,
        "IF-08 W6 Final Audit Preflight Readiness",
        "Decision: pass",
        "Readiness coverage: 1.000000",
        "Next recommended step: execute_if08_w6_final_audit_controlled_execution",
    )


def _check_if08_w6_final_audit_controlled_execution_artifacts(state: dict[str, Any]) -> None:
    _require(IF08_W6_CONTROLLED_ACTIVE_DECISION_PATH.exists(), "missing active IF08 W6 controlled decision artifact")
    _require(IF08_W6_CONTROLLED_ACTIVE_SUMMARY_PATH.exists(), "missing active IF08 W6 controlled summary artifact")
    _require(IF08_W6_CONTROLLED_ACTIVE_REPORT_PATH.exists(), "missing active IF08 W6 controlled report artifact")

    active_decision = _load_json(IF08_W6_CONTROLLED_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-08-W6-FINAL-AUDIT-CONTROLLED-EXECUTION", "active W6 controlled decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active W6 controlled decision must be pass")
    _require(active_decision.get("status") == IF08_W6_CONTROLLED_STATUS, "active W6 controlled decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF08_W6_CONTROLLED_PROJECT_SHA, "active W6 controlled decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF08_W6_CONTROLLED_CI_STATE, "active W6 controlled decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF08_W6_CONTROLLED_PROJECT_CI_RUN_URL, "active W6 controlled decision ci url mismatch")
    _require(active_decision.get("project_origin_main_sha_verified") is True, "active W6 controlled decision must verify origin/main sha")
    _require(active_decision.get("project_ci_green_confirmed") is True, "active W6 controlled decision must confirm green CI")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active W6 controlled decision pre-sync phase id mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "active W6 controlled decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "active W6 controlled decision pre-sync sha mismatch")
    _require(active_decision.get("active_context_sync_applied") is True, "active W6 controlled decision must mark sync applied")
    _require(active_decision.get("active_context_remote_main_reflects_if08_w6_final_audit_controlled_execution") is True, "active W6 controlled decision must confirm remote reflection")
    _require(active_decision.get("permanent_active_update_rule_installed") is True, "active W6 controlled decision must preserve permanent rule")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF08_W6_CONTROLLED_PHASE, "active W6 controlled decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF08_W6_CONTROLLED_STATUS, "active W6 controlled decision latest status mismatch")
    _require(active_decision.get("previous_phase_verified") == IF08_W6_CONTROLLED_PREVIOUS_PHASE, "active W6 controlled decision previous phase mismatch")
    _require(active_decision.get("previous_status_verified") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "active W6 controlled decision previous status mismatch")
    _require(active_decision.get("source_preflight_status") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "active W6 controlled decision source preflight status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA, "active W6 controlled decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "active W6 controlled decision source active-context sha mismatch")
    _require(active_decision.get("source_project_sha_recorded_in_active_context") == IF08_W6_CONTROLLED_RECORDED_DRIFT_SHA, "active W6 controlled decision recorded drift sha mismatch")
    _require(active_decision.get("source_project_sha_drift_recorded") is True, "active W6 controlled decision must record drift")
    _require(active_decision.get("source_project_sha_drift_resolved_via_primary_refs") is True, "active W6 controlled decision must resolve drift via primary refs")
    _require(active_decision.get("w6_canonical_sync_verified") is True, "active W6 controlled decision must verify canonical sync")
    _require(active_decision.get("execution_scope") == "synthetic_isolated_lab_only", "active W6 controlled decision execution_scope mismatch")
    _require(active_decision.get("w6_preflight_readiness") is True, "active W6 controlled decision must verify W6 preflight readiness")
    _require(active_decision.get("preflight_readiness_verified") is True, "active W6 controlled decision must preserve preflight verification")
    _require(active_decision.get("w6_execution_performed") is True, "active W6 controlled decision must record execution performed")
    _require(active_decision.get("w6_execution_allowed") is False, "active W6 controlled decision must keep execution disallowed")
    _require(active_decision.get("w6_real_execution_performed") is False, "active W6 controlled decision must keep real execution false")
    _require(active_decision.get("ttr_required") == 0, "active W6 controlled decision ttr_required must be 0")
    _require(active_decision.get("ttr_observed") == 0, "active W6 controlled decision ttr_observed must be 0")
    _require(active_decision.get("har_required") == 1.0, "active W6 controlled decision har_required must be 1.0")
    _require(active_decision.get("har_observed") == 1.0, "active W6 controlled decision har_observed must be 1.0")
    _require(active_decision.get("minos_mechanical_readiness") is True, "active W6 controlled decision minos_mechanical_readiness must be true")
    _require(active_decision.get("minos_semantic_readiness") is True, "active W6 controlled decision minos_semantic_readiness must be true")
    _require(active_decision.get("anti_theater_review_passed") is True, "active W6 controlled decision anti_theater_review_passed must be true")
    _require(active_decision.get("critical_coverage_cells_total") == 12, "active W6 controlled decision critical_coverage_cells_total must be 12")
    _require(active_decision.get("critical_coverage_cells_passed") == 12, "active W6 controlled decision critical_coverage_cells_passed must be 12")
    _require(active_decision.get("critical_coverage_completion") == 1.0, "active W6 controlled decision critical_coverage_completion must be 1.0")
    _require(active_decision.get("business_scenarios_total") == 14, "active W6 controlled decision business_scenarios_total must be 14")
    _require(active_decision.get("business_scenarios_passed") == 14, "active W6 controlled decision business_scenarios_passed must be 14")
    _require(active_decision.get("business_scenarios_blocked_or_detected") == 14, "active W6 controlled decision business_scenarios_blocked_or_detected must be 14")
    _require(active_decision.get("evidence_units_complete") is True, "active W6 controlled decision evidence_units_complete must be true")
    _require(active_decision.get("stop_conditions_respected") is True, "active W6 controlled decision stop_conditions_respected must be true")
    _require(active_decision.get("next_recommended_step") == IF08_W6_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W6 controlled decision next step mismatch")
    for key in (
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(active_decision.get(key) is False, f"active W6 controlled decision {key} must be false")

    active_summary = _load_json(IF08_W6_CONTROLLED_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("phase_id") == "IF-08-W6-FINAL-AUDIT-CONTROLLED-EXECUTION", "active W6 controlled summary phase_id mismatch")
    _require(active_summary.get("decision") == "pass", "active W6 controlled summary must be pass")
    _require(active_summary.get("status") == IF08_W6_CONTROLLED_STATUS, "active W6 controlled summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF08_W6_CONTROLLED_PROJECT_SHA, "active W6 controlled summary project sha mismatch")
    _require(active_summary.get("project_ci_state") == IF08_W6_CONTROLLED_CI_STATE, "active W6 controlled summary ci state mismatch")
    _require(active_summary.get("project_ci_run_url") == IF08_W6_CONTROLLED_PROJECT_CI_RUN_URL, "active W6 controlled summary ci url mismatch")
    _require(active_summary.get("active_context_remote_main_reflects_if08_w6_final_audit_controlled_execution") is True, "active W6 controlled summary must confirm remote reflection")
    _require(active_summary.get("previous_phase_verified") == IF08_W6_CONTROLLED_PREVIOUS_PHASE, "active W6 controlled summary previous phase mismatch")
    _require(active_summary.get("previous_status_verified") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "active W6 controlled summary previous status mismatch")
    _require(active_summary.get("source_preflight_status") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "active W6 controlled summary source preflight status mismatch")
    _require(active_summary.get("source_project_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA, "active W6 controlled summary source project sha mismatch")
    _require(active_summary.get("source_active_context_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "active W6 controlled summary source active-context sha mismatch")
    _require(active_summary.get("source_project_sha_drift_recorded") is True, "active W6 controlled summary must record drift")
    _require(active_summary.get("execution_scope") == "synthetic_isolated_lab_only", "active W6 controlled summary execution_scope mismatch")
    _require(active_summary.get("w6_preflight_readiness") is True, "active W6 controlled summary must verify W6 preflight readiness")
    _require(active_summary.get("preflight_readiness_verified") is True, "active W6 controlled summary must preserve preflight verification")
    _require(active_summary.get("w6_execution_performed") is True, "active W6 controlled summary must record execution performed")
    _require(active_summary.get("w6_execution_allowed") is False, "active W6 controlled summary must keep execution disallowed")
    _require(active_summary.get("w6_real_execution_performed") is False, "active W6 controlled summary must keep real execution false")
    _require(active_summary.get("ttr_observed") == 0, "active W6 controlled summary ttr_observed must be 0")
    _require(active_summary.get("har_observed") == 1.0, "active W6 controlled summary har_observed must be 1.0")
    _require(active_summary.get("minos_mechanical_readiness") is True, "active W6 controlled summary minos_mechanical_readiness must be true")
    _require(active_summary.get("minos_semantic_readiness") is True, "active W6 controlled summary minos_semantic_readiness must be true")
    _require(active_summary.get("anti_theater_review_passed") is True, "active W6 controlled summary anti_theater_review_passed must be true")
    _require(active_summary.get("critical_coverage_completion") == 1.0, "active W6 controlled summary critical_coverage_completion must be 1.0")
    _require(active_summary.get("evidence_units_complete") is True, "active W6 controlled summary evidence_units_complete must be true")
    _require(active_summary.get("stop_conditions_respected") is True, "active W6 controlled summary stop_conditions_respected must be true")
    _require(active_summary.get("next_recommended_step") == IF08_W6_CONTROLLED_NEXT_RECOMMENDED_STEP, "active W6 controlled summary next step mismatch")

    _mirror_contains(
        IF08_W6_CONTROLLED_ACTIVE_REPORT_PATH,
        "IF-08 W6 Final Audit Controlled Execution Sync",
        "if08_w6_final_audit_controlled_execution_pass",
        "project_commit_sha: `eae468c79687474de086c984b55a3f7ff47d73f7`",
        "source_project_sha_drift_recorded: `true`",
        "execution_scope: `synthetic_isolated_lab_only`",
        "ttr_observed: `0`",
        "har_observed: `1.0`",
        "anti_theater_review_passed: `true`",
        "next_recommended_step: `prepare_if09_evidence_bundle_vulnerability_register`",
    )

    external_project_paths = (
        IF08_W6_CONTROLLED_DECISION_PATH,
        IF08_W6_CONTROLLED_SUMMARY_PATH,
        IF08_W6_CONTROLLED_REPORT_PATH,
        IF08_W6_CONTROLLED_EVIDENCE_BUNDLE_PATH,
        IF08_W6_CONTROLLED_MINOS_VERDICT_PATH,
        IF08_W6_CONTROLLED_SAFETY_ATTESTATION_PATH,
        IF08_W6_CONTROLLED_DOC_PATH,
    )
    if not all(path.exists() for path in external_project_paths):
        return

    decision = _load_json(IF08_W6_CONTROLLED_DECISION_PATH)
    _require(decision.get("phase") == IF08_W6_CONTROLLED_PHASE, "project W6 controlled decision phase mismatch")
    _require(decision.get("phase_id") == "IF-08-W6-FINAL-AUDIT-CONTROLLED-EXECUTION", "project W6 controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project W6 controlled decision must be pass")
    _require(decision.get("status") == IF08_W6_CONTROLLED_STATUS, "project W6 controlled decision status mismatch")
    _require(decision.get("source_preflight_status") == IF08_W6_CONTROLLED_PREVIOUS_STATUS, "project W6 controlled decision source preflight status mismatch")
    _require(decision.get("source_project_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA, "project W6 controlled decision source project sha mismatch")
    _require(decision.get("source_active_context_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "project W6 controlled decision source active-context sha mismatch")
    _require(decision.get("source_project_sha_recorded_in_active_context") == IF08_W6_CONTROLLED_RECORDED_DRIFT_SHA, "project W6 controlled decision recorded drift sha mismatch")
    _require(decision.get("source_project_sha_drift_recorded") is True, "project W6 controlled decision must record drift")
    _require(decision.get("execution_scope") == "synthetic_isolated_lab_only", "project W6 controlled decision execution_scope mismatch")
    _require(decision.get("w6_execution_performed") == "true_synthetic_isolated_lab_only", "project W6 controlled decision execution marker mismatch")
    _require(decision.get("w6_real_execution_performed") is False, "project W6 controlled decision must keep real execution false")
    _require(decision.get("ttr_required") == 0, "project W6 controlled decision ttr_required must be 0")
    _require(decision.get("ttr_observed") == 0, "project W6 controlled decision ttr_observed must be 0")
    _require(decision.get("har_required") == 1.0, "project W6 controlled decision har_required must be 1.0")
    _require(decision.get("har_observed") == 1.0, "project W6 controlled decision har_observed must be 1.0")
    _require(decision.get("minos_mechanical_readiness") is True, "project W6 controlled decision minos_mechanical_readiness must be true")
    _require(decision.get("minos_semantic_readiness") is True, "project W6 controlled decision minos_semantic_readiness must be true")
    _require(decision.get("anti_theater_review_passed") is True, "project W6 controlled decision anti_theater_review_passed must be true")
    _require(decision.get("evidence_units_complete") is True, "project W6 controlled decision evidence_units_complete must be true")
    _require(decision.get("stop_conditions_respected") is True, "project W6 controlled decision stop_conditions_respected must be true")
    _require(decision.get("blocking_findings") == [], "project W6 controlled decision blocking_findings must be empty")
    _require(decision.get("next_recommended_step") == "post_sync_review_if08_w6_final_audit_controlled_execution", "project W6 controlled decision next step mismatch")

    summary = _load_json(IF08_W6_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase") == IF08_W6_CONTROLLED_PHASE, "project W6 controlled summary phase mismatch")
    _require(summary.get("status") == IF08_W6_CONTROLLED_STATUS, "project W6 controlled summary status mismatch")
    _require(summary.get("source_project_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA, "project W6 controlled summary source project sha mismatch")
    _require(summary.get("source_active_context_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "project W6 controlled summary source active-context sha mismatch")
    _require(summary.get("source_project_sha_drift_recorded") is True, "project W6 controlled summary must record drift")
    _require(summary.get("execution_scope") == "synthetic_isolated_lab_only", "project W6 controlled summary execution_scope mismatch")
    _require(summary.get("w6_execution_performed") == "true_synthetic_isolated_lab_only", "project W6 controlled summary execution marker mismatch")
    _require(summary.get("ttr_observed") == 0, "project W6 controlled summary ttr_observed must be 0")
    _require(summary.get("har_observed") == 1.0, "project W6 controlled summary har_observed must be 1.0")
    _require(summary.get("anti_theater_review_passed") is True, "project W6 controlled summary anti_theater_review_passed must be true")
    _require(summary.get("next_recommended_step") == "post_sync_review_if08_w6_final_audit_controlled_execution", "project W6 controlled summary next step mismatch")

    evidence_bundle = _load_json(IF08_W6_CONTROLLED_EVIDENCE_BUNDLE_PATH)
    _require(evidence_bundle.get("phase") == IF08_W6_CONTROLLED_PHASE, "project W6 controlled evidence bundle phase mismatch")
    _require(evidence_bundle.get("status") == IF08_W6_CONTROLLED_STATUS, "project W6 controlled evidence bundle status mismatch")
    _require(evidence_bundle.get("source_project_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_PROJECT_SHA, "project W6 controlled evidence bundle source project sha mismatch")
    _require(evidence_bundle.get("source_active_context_sha_verified_by_packet") == IF08_W6_CONTROLLED_SOURCE_ACTIVE_CONTEXT_SHA, "project W6 controlled evidence bundle source active-context sha mismatch")
    _require(evidence_bundle.get("source_project_sha_drift_recorded") is True, "project W6 controlled evidence bundle must record drift")
    _require(evidence_bundle.get("evidence_units_complete") is True, "project W6 controlled evidence bundle evidence_units_complete must be true")
    _require(evidence_bundle.get("stop_conditions_respected") is True, "project W6 controlled evidence bundle stop_conditions_respected must be true")
    _require(len(evidence_bundle.get("material_output_hashes", {})) == 6, "project W6 controlled evidence bundle hash count mismatch")

    minos = _load_json(IF08_W6_CONTROLLED_MINOS_VERDICT_PATH)
    _require(minos.get("phase") == IF08_W6_CONTROLLED_PHASE, "project W6 controlled minos phase mismatch")
    _require(minos.get("status") == IF08_W6_CONTROLLED_STATUS, "project W6 controlled minos status mismatch")
    _require(minos.get("ttr_observed") == 0, "project W6 controlled minos ttr_observed must be 0")
    _require(minos.get("har_observed") == 1.0, "project W6 controlled minos har_observed must be 1.0")
    _require(minos.get("anti_theater_review_passed") is True, "project W6 controlled minos anti_theater_review_passed must be true")

    safety = _load_json(IF08_W6_CONTROLLED_SAFETY_ATTESTATION_PATH)
    _require(safety.get("phase") == IF08_W6_CONTROLLED_PHASE, "project W6 controlled safety phase mismatch")
    _require(safety.get("status") == IF08_W6_CONTROLLED_STATUS, "project W6 controlled safety status mismatch")
    _require(safety.get("preserved_hard_locks") is True, "project W6 controlled safety must preserve hard locks")
    _require(len(safety.get("artifact_hashes", {})) == 5, "project W6 controlled safety artifact hash count mismatch")

    _mirror_contains(
        IF08_W6_CONTROLLED_REPORT_PATH,
        "IF-08 W6 Final Audit Controlled Execution",
        "Status: if08_w6_final_audit_controlled_execution_pass",
        "Execution scope: synthetic_isolated_lab_only",
        "TTR required/observed: 0/0",
        "HAR required/observed: 1.0/1.0",
        "Next recommended step: post_sync_review_if08_w6_final_audit_controlled_execution",
    )
    _mirror_contains(
        IF08_W6_CONTROLLED_DOC_PATH,
        "IF-08 W6 Final Audit Controlled Execution",
        "decision: pass",
        "next_recommended_step: post_sync_review_if08_w6_final_audit_controlled_execution",
    )


def _check_if09_evidence_bundle_vulnerability_register_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF09_ACTIVE_DECISION_PATH,
        IF09_ACTIVE_SUMMARY_PATH,
        IF09_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF09 active-context artifact: {path}")

    external_project_paths = (
        IF09_PROJECT_DECISION_PATH,
        IF09_PROJECT_SUMMARY_PATH,
        IF09_PROJECT_REPORT_PATH,
        IF09_PROJECT_ROOT_MANIFEST_PATH,
        IF09_PROJECT_HASH_TREE_PATH,
        IF09_PROJECT_CUSTODY_CHAIN_PATH,
        IF09_PROJECT_REPLAY_DIFF_PATH,
        IF09_PROJECT_MUTATION_SURVIVAL_PATH,
        IF09_PROJECT_REGISTER_PATH,
        IF09_PROJECT_DOC_PATH,
    )
    external_project_available = all(path.exists() for path in external_project_paths)

    active_decision = _load_json(IF09_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-09-EVIDENCE-BUNDLE-VULNERABILITY-REGISTER", "active IF09 decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active IF09 decision must be pass")
    _require(active_decision.get("status") == IF09_STATUS, "active IF09 decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF09_PROJECT_SHA, "active IF09 decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF09_PROJECT_CI_STATE, "active IF09 decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF09_PROJECT_CI_RUN_URL, "active IF09 decision ci url mismatch")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active IF09 decision pre-sync phase mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF09_SOURCE_STATUS, "active IF09 decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF09_SOURCE_ACTIVE_CONTEXT_SHA, "active IF09 decision pre-sync sha mismatch")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF09_PHASE, "active IF09 decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF09_STATUS, "active IF09 decision latest status mismatch")
    _require(active_decision.get("source_phase_verified") == IF09_SOURCE_PHASE, "active IF09 decision source phase mismatch")
    _require(active_decision.get("source_status_verified") == IF09_SOURCE_STATUS, "active IF09 decision source status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF09_SOURCE_PROJECT_SHA, "active IF09 decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF09_SOURCE_ACTIVE_CONTEXT_SHA, "active IF09 decision source active-context sha mismatch")
    _require(active_decision.get("root_manifest_sha256") == IF09_ROOT_MANIFEST_SHA, "active IF09 decision root manifest sha mismatch")
    _require(active_decision.get("validated_findings_total") == 1, "active IF09 decision validated_findings_total mismatch")
    _require(active_decision.get("finding_candidates_total") == 1, "active IF09 decision finding_candidates_total mismatch")
    _require(active_decision.get("invalid_findings_total") == 1, "active IF09 decision invalid_findings_total mismatch")
    _require(active_decision.get("observations_total") == 1, "active IF09 decision observations_total mismatch")
    _require(active_decision.get("reproduction_units_total") == 1, "active IF09 decision reproduction_units_total mismatch")
    _require(active_decision.get("replay_units_total") == 2, "active IF09 decision replay_units_total mismatch")
    _require(active_decision.get("mutation_units_total") == 2, "active IF09 decision mutation_units_total mismatch")
    _require(active_decision.get("evidence_units_total") == 7, "active IF09 decision evidence_units_total mismatch")
    _require(active_decision.get("findings_total") == 16, "active IF09 decision findings_total mismatch")
    _require(active_decision.get("purgatorium_handoff_required_ids") == ["IF09-FIND-001"], "active IF09 decision handoff ids mismatch")
    _require(active_decision.get("macro_transition_preserved") is True, "active IF09 decision macro_transition_preserved mismatch")
    _require(active_decision.get("current_phase_id_preserved") == EXPECTED_PHASE_ID, "active IF09 decision current_phase_id_preserved mismatch")
    _require(active_decision.get("active_next_phase_preserved") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "active IF09 decision active_next_phase_preserved mismatch")
    _require(active_decision.get("active_next_phase_class_preserved") == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "active IF09 decision active_next_phase_class_preserved mismatch")
    _require(active_decision.get("next_recommended_step") == IF09_NEXT_RECOMMENDED_STEP, "active IF09 decision next step mismatch")

    active_summary = _load_json(IF09_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("status") == IF09_STATUS, "active IF09 summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF09_PROJECT_SHA, "active IF09 summary project sha mismatch")
    _require(active_summary.get("project_ci_run_url") == IF09_PROJECT_CI_RUN_URL, "active IF09 summary ci url mismatch")
    _require(active_summary.get("root_manifest_sha256") == IF09_ROOT_MANIFEST_SHA, "active IF09 summary root manifest sha mismatch")
    _require(active_summary.get("next_recommended_step") == IF09_NEXT_RECOMMENDED_STEP, "active IF09 summary next step mismatch")

    if not external_project_available:
        _mirror_contains(
            IF09_ACTIVE_REPORT_PATH,
            "IF-09 Evidence Bundle + Vulnerability Register Sync",
            "status: `if09_evidence_bundle_vulnerability_register_pass`",
            "project_commit_sha: `38b16edadce15ce8f2049bb3de8538bb921e344e`",
            "next_recommended_step: `prepare_if10_purgatorium_handoff_graph`",
        )
        return

    decision = _load_json(IF09_PROJECT_DECISION_PATH)
    _require(decision.get("phase") == IF09_PHASE, "project IF09 decision phase mismatch")
    _require(decision.get("status") == IF09_STATUS, "project IF09 decision status mismatch")
    _require(decision.get("source_phase") == IF09_SOURCE_PHASE, "project IF09 decision source phase mismatch")
    _require(decision.get("source_status") == IF09_SOURCE_STATUS, "project IF09 decision source status mismatch")
    _require(decision.get("source_project_sha_verified_by_packet") == IF09_SOURCE_PROJECT_SHA, "project IF09 decision source project sha mismatch")
    _require(decision.get("source_active_context_sha_verified_by_packet") == IF09_SOURCE_ACTIVE_CONTEXT_SHA, "project IF09 decision source active-context sha mismatch")
    _require(decision.get("root_manifest_sha256") == IF09_ROOT_MANIFEST_SHA, "project IF09 decision root manifest sha mismatch")
    _require(decision.get("next_recommended_step") == IF09_NEXT_RECOMMENDED_STEP, "project IF09 decision next step mismatch")

    summary = _load_json(IF09_PROJECT_SUMMARY_PATH)
    _require(summary.get("status") == IF09_STATUS, "project IF09 summary status mismatch")
    _require(summary.get("root_manifest_sha256") == IF09_ROOT_MANIFEST_SHA, "project IF09 summary root manifest sha mismatch")

    root_manifest = _load_json(IF09_PROJECT_ROOT_MANIFEST_PATH)
    _require(root_manifest.get("status") == IF09_STATUS, "project IF09 root manifest status mismatch")
    _require(root_manifest.get("root_manifest_references_all_bundle_files") is True, "project IF09 root manifest reference mismatch")
    _require(root_manifest.get("hash_tree_covers_all_evidence_units") is True, "project IF09 root manifest evidence coverage mismatch")
    _require(root_manifest.get("validated_findings_total") == 1, "project IF09 root manifest validated_findings_total mismatch")
    _require(root_manifest.get("evidence_units_total") == 7, "project IF09 root manifest evidence_units_total mismatch")

    hash_tree = _load_json(IF09_PROJECT_HASH_TREE_PATH)
    _require(hash_tree.get("phase_id") == "IF-09-EVIDENCE-BUNDLE-VULNERABILITY-REGISTER", "project IF09 hash tree phase_id mismatch")
    _require(hash_tree.get("covers_all_evidence_units") is True, "project IF09 hash tree coverage mismatch")
    _require(hash_tree.get("leaf_count") == 7, "project IF09 hash tree leaf count mismatch")

    replay = _load_json(IF09_PROJECT_REPLAY_DIFF_PATH)
    _require(len(replay.get("replay_units", [])) == 2, "project IF09 replay unit count mismatch")

    mutation = _load_json(IF09_PROJECT_MUTATION_SURVIVAL_PATH)
    _require(len(mutation.get("mutation_units", [])) == 2, "project IF09 mutation unit count mismatch")

    register_lines = [line for line in IF09_PROJECT_REGISTER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    _require(len(register_lines) == 16, "project IF09 register line count mismatch")

    _mirror_contains(
        IF09_ACTIVE_REPORT_PATH,
        "IF-09 Evidence Bundle + Vulnerability Register Sync",
        "status: `if09_evidence_bundle_vulnerability_register_pass`",
        "project_commit_sha: `38b16edadce15ce8f2049bb3de8538bb921e344e`",
        "next_recommended_step: `prepare_if10_purgatorium_handoff_graph`",
    )


def _check_if10_purgatorium_handoff_graph_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF10_ACTIVE_DECISION_PATH,
        IF10_ACTIVE_SUMMARY_PATH,
        IF10_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF10 active-context artifact: {path}")

    external_project_paths = (
        IF10_PROJECT_DECISION_PATH,
        IF10_PROJECT_SUMMARY_PATH,
        IF10_PROJECT_REPORT_PATH,
        IF10_PROJECT_GRAPH_PATH,
        IF10_PROJECT_ROOT_CAUSE_PATH,
        IF10_PROJECT_REMEDIATION_PATH,
        IF10_PROJECT_REGRESSION_PATH,
        IF10_PROJECT_REVALIDATION_PATH,
        IF10_PROJECT_HANDOFF_MANIFEST_PATH,
        IF10_PROJECT_DOC_PATH,
    )
    external_project_available = all(path.exists() for path in external_project_paths)

    active_decision = _load_json(IF10_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-10-PURGATORIUM-HANDOFF-GRAPH", "active IF10 decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active IF10 decision must be pass")
    _require(active_decision.get("status") == IF10_STATUS, "active IF10 decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF10_PROJECT_SHA, "active IF10 decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF10_PROJECT_CI_STATE, "active IF10 decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF10_PROJECT_CI_RUN_URL, "active IF10 decision ci url mismatch")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active IF10 decision pre-sync phase mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF10_SOURCE_STATUS, "active IF10 decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF10_SOURCE_ACTIVE_CONTEXT_SHA, "active IF10 decision pre-sync sha mismatch")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF10_PHASE, "active IF10 decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF10_STATUS, "active IF10 decision latest status mismatch")
    _require(active_decision.get("source_phase_verified") == IF10_SOURCE_PHASE, "active IF10 decision source phase mismatch")
    _require(active_decision.get("source_status_verified") == IF10_SOURCE_STATUS, "active IF10 decision source status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF10_SOURCE_PROJECT_SHA, "active IF10 decision source project sha mismatch")
    _require(active_decision.get("source_active_context_sha_verified_by_packet") == IF10_SOURCE_ACTIVE_CONTEXT_SHA, "active IF10 decision source active-context sha mismatch")
    _require(active_decision.get("source_root_manifest_sha256") == IF10_SOURCE_ROOT_MANIFEST_SHA, "active IF10 decision source root manifest sha mismatch")
    _require(active_decision.get("graph_sha256") == IF10_GRAPH_SHA, "active IF10 decision graph sha mismatch")
    _require(active_decision.get("validated_handoff_ids") == ["IF09-FIND-001"], "active IF10 decision handoff ids mismatch")
    _require(active_decision.get("contextual_candidate_ids") == ["IF09-FIND-002"], "active IF10 decision contextual candidate ids mismatch")
    _require(active_decision.get("excluded_invalid_ids") == ["IF09-FIND-003"], "active IF10 decision excluded invalid ids mismatch")
    _require(active_decision.get("supporting_observation_ids") == ["IF09-OBS-001"], "active IF10 decision supporting observation ids mismatch")
    _require(active_decision.get("node_count") == 9, "active IF10 decision node_count mismatch")
    _require(active_decision.get("edge_count") == 8, "active IF10 decision edge_count mismatch")
    _require(active_decision.get("root_manifest_reference_verified") is True, "active IF10 decision root manifest reference mismatch")
    _require(active_decision.get("reproduction_unit_reference") == "IF09-REPRO-001", "active IF10 decision reproduction unit mismatch")
    _require(active_decision.get("replay_unit_reference") == "IF09-REPLAY-001", "active IF10 decision replay unit mismatch")
    _require(active_decision.get("mutation_unit_reference") == "IF09-MUT-001", "active IF10 decision mutation unit mismatch")
    _require(active_decision.get("next_recommended_step") == IF10_NEXT_RECOMMENDED_STEP, "active IF10 decision next step mismatch")

    active_summary = _load_json(IF10_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("status") == IF10_STATUS, "active IF10 summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF10_PROJECT_SHA, "active IF10 summary project sha mismatch")
    _require(active_summary.get("project_ci_run_url") == IF10_PROJECT_CI_RUN_URL, "active IF10 summary ci url mismatch")
    _require(active_summary.get("source_root_manifest_sha256") == IF10_SOURCE_ROOT_MANIFEST_SHA, "active IF10 summary source root manifest sha mismatch")
    _require(active_summary.get("validated_handoff_ids") == ["IF09-FIND-001"], "active IF10 summary handoff ids mismatch")
    _require(active_summary.get("node_count") == 9, "active IF10 summary node_count mismatch")
    _require(active_summary.get("edge_count") == 8, "active IF10 summary edge_count mismatch")
    _require(active_summary.get("next_recommended_step") == IF10_NEXT_RECOMMENDED_STEP, "active IF10 summary next step mismatch")

    _mirror_contains(
        IF10_ACTIVE_REPORT_PATH,
        "IF-10 Purgatorium Handoff Graph Sync",
        "status: `if10_purgatorium_handoff_graph_pass`",
        "project_commit_sha: `57106d9780af7a807bd58ea6039af3a7b1b23701`",
        "next_recommended_step: `prepare_if11_minos_final_verdict_closure`",
    )

    if not external_project_available:
        return

    decision = _load_json(IF10_PROJECT_DECISION_PATH)
    _require(decision.get("phase") == IF10_PHASE, "project IF10 decision phase mismatch")
    _require(decision.get("status") == IF10_STATUS, "project IF10 decision status mismatch")
    _require(decision.get("source_phase") == IF10_SOURCE_PHASE, "project IF10 decision source phase mismatch")
    _require(decision.get("source_status") == IF10_SOURCE_STATUS, "project IF10 decision source status mismatch")
    _require(decision.get("source_project_sha") == IF10_SOURCE_PROJECT_SHA, "project IF10 decision source project sha mismatch")
    _require(decision.get("source_root_manifest_sha256") == IF10_SOURCE_ROOT_MANIFEST_SHA, "project IF10 decision source root manifest sha mismatch")
    _require(decision.get("graph_sha256") == IF10_GRAPH_SHA, "project IF10 decision graph sha mismatch")
    _require(decision.get("validated_handoff_ids") == ["IF09-FIND-001"], "project IF10 decision handoff ids mismatch")
    _require(decision.get("node_count") == 9, "project IF10 decision node_count mismatch")
    _require(decision.get("edge_count") == 8, "project IF10 decision edge_count mismatch")
    _require(decision.get("duplicate_node_ids") == [], "project IF10 decision duplicate node ids mismatch")
    _require(decision.get("dangling_edges") == [], "project IF10 decision dangling edges mismatch")
    _require(decision.get("next_recommended_step") == IF10_NEXT_RECOMMENDED_STEP, "project IF10 decision next step mismatch")

    summary = _load_json(IF10_PROJECT_SUMMARY_PATH)
    _require(summary.get("status") == IF10_STATUS, "project IF10 summary status mismatch")
    _require(summary.get("source_root_manifest_sha256") == IF10_SOURCE_ROOT_MANIFEST_SHA, "project IF10 summary source root manifest sha mismatch")
    _require(summary.get("validated_handoff_ids") == ["IF09-FIND-001"], "project IF10 summary handoff ids mismatch")
    _require(summary.get("node_count") == 9, "project IF10 summary node_count mismatch")
    _require(summary.get("edge_count") == 8, "project IF10 summary edge_count mismatch")

    graph = _load_json(IF10_PROJECT_GRAPH_PATH)
    _require(graph.get("graph_id") == "if10_purgatorium_handoff_graph_v4", "project IF10 graph_id mismatch")
    _require(graph.get("source_phase") == IF10_SOURCE_PHASE, "project IF10 graph source phase mismatch")
    _require(graph.get("source_status") == IF10_SOURCE_STATUS, "project IF10 graph source status mismatch")
    _require(graph.get("source_project_sha") == IF10_SOURCE_PROJECT_SHA, "project IF10 graph source project sha mismatch")
    _require(graph.get("source_root_manifest_sha256") == IF10_SOURCE_ROOT_MANIFEST_SHA, "project IF10 graph source root manifest sha mismatch")
    _require(graph.get("handoff_required_ids") == ["IF09-FIND-001"], "project IF10 graph handoff ids mismatch")
    _require(graph.get("root_manifest_reference_verified") is True, "project IF10 graph root manifest reference mismatch")
    _require(len(graph.get("nodes", [])) == 9, "project IF10 graph node count mismatch")
    _require(len(graph.get("edges", [])) == 8, "project IF10 graph edge count mismatch")

    root_cause = _load_json(IF10_PROJECT_ROOT_CAUSE_PATH)
    _require(len(root_cause.get("candidates", [])) == 1, "project IF10 root cause candidate count mismatch")
    remediation = _load_json(IF10_PROJECT_REMEDIATION_PATH)
    _require(len(remediation.get("tracks", [])) == 1, "project IF10 remediation track count mismatch")
    regression = _load_json(IF10_PROJECT_REGRESSION_PATH)
    _require(len(regression.get("plans", [])) == 1, "project IF10 regression plan count mismatch")
    revalidation = _load_json(IF10_PROJECT_REVALIDATION_PATH)
    _require(len(revalidation.get("waves", [])) == 1, "project IF10 revalidation wave count mismatch")
    handoff_manifest = _load_json(IF10_PROJECT_HANDOFF_MANIFEST_PATH)
    _require(handoff_manifest.get("handoff_required_ids") == ["IF09-FIND-001"], "project IF10 handoff manifest ids mismatch")


def _check_if11_minos_final_verdict_closure_artifacts(state: dict[str, Any]) -> None:
    for path in (
        IF11_ACTIVE_DECISION_PATH,
        IF11_ACTIVE_SUMMARY_PATH,
        IF11_ACTIVE_REPORT_PATH,
    ):
        _require(path.exists(), f"missing IF11 active-context artifact: {path}")

    external_project_paths = (
        IF11_PROJECT_DECISION_PATH,
        IF11_PROJECT_SUMMARY_PATH,
        IF11_PROJECT_REPORT_PATH,
        IF11_PROJECT_MECHANICAL_PATH,
        IF11_PROJECT_SEMANTIC_PATH,
        IF11_PROJECT_OPERATOR_COSIGNATURE_PATH,
        IF11_PROJECT_ANTI_THEATER_PATH,
        IF11_PROJECT_CLOSURE_PATH,
        IF11_PROJECT_MANIFEST_PATH,
        IF11_PROJECT_FINAL_EVIDENCE_PATH,
        IF11_PROJECT_READINESS_PATH,
        IF11_PROJECT_BOUNDARY_PATH,
        IF11_PROJECT_DOC_PATH,
    )
    external_project_available = all(path.exists() for path in external_project_paths)

    active_decision = _load_json(IF11_ACTIVE_DECISION_PATH)
    _require(active_decision.get("phase_id") == "IF-11-MINOS-FINAL-VERDICT-CLOSURE", "active IF11 decision phase_id mismatch")
    _require(active_decision.get("decision") == "pass", "active IF11 decision must be pass")
    _require(active_decision.get("status") == IF11_STATUS, "active IF11 decision status mismatch")
    _require(active_decision.get("project_commit_sha") == IF11_PROJECT_SHA, "active IF11 decision project sha mismatch")
    _require(active_decision.get("project_ci_state") == IF11_PROJECT_CI_STATE, "active IF11 decision ci state mismatch")
    _require(active_decision.get("project_ci_run_url") == IF11_PROJECT_CI_RUN_URL, "active IF11 decision ci url mismatch")
    _require(active_decision.get("active_context_pre_sync_phase_id") == EXPECTED_PHASE_ID, "active IF11 decision pre-sync phase mismatch")
    _require(active_decision.get("active_context_pre_sync_current_status") == IF11_SOURCE_STATUS, "active IF11 decision pre-sync status mismatch")
    _require(active_decision.get("active_context_pre_sync_sha") == IF11_SOURCE_ACTIVE_CONTEXT_SYNC_SHA, "active IF11 decision pre-sync sha mismatch")
    _require(active_decision.get("latest_completed_phase_after_sync") == IF11_PHASE, "active IF11 decision latest phase mismatch")
    _require(active_decision.get("latest_completed_status_after_sync") == IF11_STATUS, "active IF11 decision latest status mismatch")
    _require(active_decision.get("source_phase_verified") == IF11_SOURCE_PHASE, "active IF11 decision source phase mismatch")
    _require(active_decision.get("source_status_verified") == IF11_SOURCE_STATUS, "active IF11 decision source status mismatch")
    _require(active_decision.get("source_project_sha_verified_by_packet") == IF11_SOURCE_PROJECT_SHA, "active IF11 decision source project sha mismatch")
    _require(active_decision.get("source_active_context_pre_sync_sha_verified_by_packet") == IF11_SOURCE_ACTIVE_CONTEXT_PRE_SYNC_SHA, "active IF11 decision source pre-sync sha mismatch")
    _require(active_decision.get("source_active_context_sync_sha_verified_by_packet") == IF11_SOURCE_ACTIVE_CONTEXT_SYNC_SHA, "active IF11 decision source sync sha mismatch")
    _require(active_decision.get("source_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "active IF11 decision source root manifest sha mismatch")
    _require(active_decision.get("source_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "active IF11 decision source graph sha mismatch")
    _require(active_decision.get("validated_handoff_ids") == ["IF09-FIND-001"], "active IF11 decision handoff ids mismatch")
    _require(active_decision.get("contextual_candidate_ids") == ["IF09-FIND-002"], "active IF11 decision contextual candidate ids mismatch")
    _require(active_decision.get("excluded_invalid_ids") == ["IF09-FIND-003"], "active IF11 decision excluded invalid ids mismatch")
    _require(active_decision.get("supporting_observation_ids") == ["IF09-OBS-001"], "active IF11 decision supporting observation ids mismatch")
    _require(active_decision.get("minos_mechanical_verdict") == "pass", "active IF11 decision mechanical verdict mismatch")
    _require(active_decision.get("minos_semantic_verdict") == "pass", "active IF11 decision semantic verdict mismatch")
    _require(active_decision.get("anti_theater_verdict") == "pass", "active IF11 decision anti-theater verdict mismatch")
    _require(active_decision.get("operator_cosignature_status") == "pending_operator_review", "active IF11 decision cosignature mismatch")
    _require(active_decision.get("infernus_closure_status") == "closed_with_purgatorium_handoff_ready", "active IF11 decision closure status mismatch")
    _require(active_decision.get("purgatorium_handoff_ready") is True, "active IF11 decision handoff readiness mismatch")
    _require(active_decision.get("real_execution_authorized") is False, "active IF11 decision real_execution_authorized mismatch")
    _require(active_decision.get("next_recommended_step") == IF11_NEXT_RECOMMENDED_STEP, "active IF11 decision next step mismatch")

    active_summary = _load_json(IF11_ACTIVE_SUMMARY_PATH)
    _require(active_summary.get("status") == IF11_STATUS, "active IF11 summary status mismatch")
    _require(active_summary.get("project_commit_sha") == IF11_PROJECT_SHA, "active IF11 summary project sha mismatch")
    _require(active_summary.get("project_ci_run_url") == IF11_PROJECT_CI_RUN_URL, "active IF11 summary ci url mismatch")
    _require(active_summary.get("source_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "active IF11 summary source root manifest sha mismatch")
    _require(active_summary.get("source_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "active IF11 summary source graph sha mismatch")
    _require(active_summary.get("validated_handoff_ids") == ["IF09-FIND-001"], "active IF11 summary handoff ids mismatch")
    _require(active_summary.get("minos_mechanical_verdict") == "pass", "active IF11 summary mechanical verdict mismatch")
    _require(active_summary.get("minos_semantic_verdict") == "pass", "active IF11 summary semantic verdict mismatch")
    _require(active_summary.get("anti_theater_verdict") == "pass", "active IF11 summary anti-theater verdict mismatch")
    _require(active_summary.get("operator_cosignature_status") == "pending_operator_review", "active IF11 summary cosignature mismatch")
    _require(active_summary.get("infernus_closure_status") == "closed_with_purgatorium_handoff_ready", "active IF11 summary closure status mismatch")
    _require(active_summary.get("purgatorium_handoff_ready") is True, "active IF11 summary handoff readiness mismatch")
    _require(active_summary.get("next_recommended_step") == IF11_NEXT_RECOMMENDED_STEP, "active IF11 summary next step mismatch")

    _mirror_contains(
        IF11_ACTIVE_REPORT_PATH,
        "IF-11 Minos Final Verdict + Closure Sync",
        "status: `if11_minos_final_verdict_closure_pass`",
        "project_commit_sha: `6312302ea45b72ddc310b2b33f56245be65b99dc`",
        "next_recommended_step: `prepare_purgatorium_handoff_or_operator_review`",
    )

    if not external_project_available:
        return

    decision = _load_json(IF11_PROJECT_DECISION_PATH)
    _require(decision.get("phase") == IF11_PHASE, "project IF11 decision phase mismatch")
    _require(decision.get("status") == IF11_STATUS, "project IF11 decision status mismatch")
    _require(decision.get("source_phase") == IF11_SOURCE_PHASE, "project IF11 decision source phase mismatch")
    _require(decision.get("source_status") == IF11_SOURCE_STATUS, "project IF11 decision source status mismatch")
    _require(decision.get("source_project_sha") == IF11_SOURCE_PROJECT_SHA, "project IF11 decision source project sha mismatch")
    _require(decision.get("source_active_context_pre_sync_sha") == IF11_SOURCE_ACTIVE_CONTEXT_PRE_SYNC_SHA, "project IF11 decision source pre-sync sha mismatch")
    _require(decision.get("source_active_context_sync_sha") == IF11_SOURCE_ACTIVE_CONTEXT_SYNC_SHA, "project IF11 decision source sync sha mismatch")
    _require(decision.get("source_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "project IF11 decision source root manifest sha mismatch")
    _require(decision.get("source_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "project IF11 decision source graph sha mismatch")
    _require(decision.get("validated_handoff_ids") == ["IF09-FIND-001"], "project IF11 decision handoff ids mismatch")
    _require(decision.get("minos_mechanical_verdict") == "pass", "project IF11 decision mechanical verdict mismatch")
    _require(decision.get("minos_semantic_verdict") == "pass", "project IF11 decision semantic verdict mismatch")
    _require(decision.get("anti_theater_verdict") == "pass", "project IF11 decision anti-theater verdict mismatch")
    _require(decision.get("operator_cosignature_status") == "pending_operator_review", "project IF11 decision cosignature mismatch")
    _require(decision.get("infernus_closure_status") == "closed_with_purgatorium_handoff_ready", "project IF11 decision closure status mismatch")
    _require(decision.get("purgatorium_handoff_ready") is True, "project IF11 decision handoff readiness mismatch")
    _require(decision.get("real_execution_authorized") is False, "project IF11 decision real execution authorization mismatch")
    _require(decision.get("next_recommended_step") == IF11_NEXT_RECOMMENDED_STEP, "project IF11 decision next step mismatch")

    summary = _load_json(IF11_PROJECT_SUMMARY_PATH)
    _require(summary.get("status") == IF11_STATUS, "project IF11 summary status mismatch")
    _require(summary.get("source_phase") == IF11_SOURCE_PHASE, "project IF11 summary source phase mismatch")
    _require(summary.get("source_status") == IF11_SOURCE_STATUS, "project IF11 summary source status mismatch")
    _require(summary.get("source_project_sha") == IF11_SOURCE_PROJECT_SHA, "project IF11 summary source project sha mismatch")
    _require(summary.get("source_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "project IF11 summary source root manifest sha mismatch")
    _require(summary.get("source_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "project IF11 summary source graph sha mismatch")
    _require(summary.get("minos_mechanical_verdict") == "pass", "project IF11 summary mechanical verdict mismatch")
    _require(summary.get("minos_semantic_verdict") == "pass", "project IF11 summary semantic verdict mismatch")
    _require(summary.get("anti_theater_verdict") == "pass", "project IF11 summary anti-theater verdict mismatch")
    _require(summary.get("operator_cosignature_status") == "pending_operator_review", "project IF11 summary cosignature mismatch")
    _require(summary.get("infernus_closure_status") == "closed_with_purgatorium_handoff_ready", "project IF11 summary closure status mismatch")
    _require(summary.get("purgatorium_handoff_ready") is True, "project IF11 summary handoff readiness mismatch")

    cosignature = _load_json(IF11_PROJECT_OPERATOR_COSIGNATURE_PATH)
    _require(cosignature.get("operator_cosignature_status") == "pending_operator_review", "project IF11 cosignature status mismatch")
    _require(cosignature.get("operator_execution_authorization") is False, "project IF11 cosignature execution authorization mismatch")
    _require(cosignature.get("product_authorization") is False, "project IF11 cosignature product authorization mismatch")
    _require(cosignature.get("bedrock_authorization") is False, "project IF11 cosignature bedrock authorization mismatch")

    closure = _load_json(IF11_PROJECT_CLOSURE_PATH)
    _require(closure.get("closure_status") == "closed_with_purgatorium_handoff_ready", "project IF11 closure status mismatch")
    _require(closure.get("minos_mechanical_verdict") == "pass", "project IF11 closure mechanical verdict mismatch")
    _require(closure.get("minos_semantic_verdict") == "pass", "project IF11 closure semantic verdict mismatch")
    _require(closure.get("anti_theater_verdict") == "pass", "project IF11 closure anti-theater verdict mismatch")
    _require(closure.get("operator_cosignature_status") == "pending_operator_review", "project IF11 closure cosignature mismatch")
    _require(closure.get("purgatorium_handoff_ready") is True, "project IF11 closure readiness mismatch")
    _require(closure.get("real_execution_authorized") is False, "project IF11 closure execution authorization mismatch")
    _require(closure.get("next_recommended_step") == IF11_NEXT_RECOMMENDED_STEP, "project IF11 closure next step mismatch")

    readiness = _load_json(IF11_PROJECT_READINESS_PATH)
    _require(readiness.get("purgatorium_handoff_ready") is True, "project IF11 readiness mismatch")
    _require(readiness.get("correction_implemented") is False, "project IF11 readiness correction mismatch")
    _require(readiness.get("finding_resolved") is False, "project IF11 readiness finding resolution mismatch")

    boundary = _load_json(IF11_PROJECT_BOUNDARY_PATH)
    _require(boundary.get("next_recommended_step") == IF11_NEXT_RECOMMENDED_STEP, "project IF11 boundary next step mismatch")
    _require(boundary.get("real_execution_authorized") is False, "project IF11 boundary execution authorization mismatch")
    _require(boundary.get("bedrock_ready") is False, "project IF11 boundary bedrock readiness mismatch")
    _require(boundary.get("product_ready") is False, "project IF11 boundary product readiness mismatch")


def _check_purg_pre_canonical_authority_materialization_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG_PRE_DECISION_PATH,
        PURG_PRE_SUMMARY_PATH,
        PURG_PRE_REPORT_PATH,
        PURG_PRE_NO_REAL_EXECUTION_PATH,
        PURG_PRE_EXCLUDENT_MANIFEST_PATH,
        PURG_PRE_ROUTE_OPENING_CANDIDATE_PATH,
        PURGATORIUM_ROADMAP_PATH,
        INFERNUS_CANONROADMAP_STUB_PATH,
        INFERNUS_CANONROADMAP_FORENSIC_PATH,
    ):
        _require(path.exists(), f"missing PURG-PRE authority artifact: {path}")

    decision = _load_json(PURG_PRE_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-PRE-CANONICAL-AUTHORITY-MATERIALIZATION", "purg_pre decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "purg_pre decision must be pass")
    _require(decision.get("status") == "purg_pre_canonical_authority_materialization_pass", "purg_pre decision status mismatch")
    _require(decision.get("does_not_advance_phase") is True, "purg_pre decision must preserve latest completed phase")
    _require(decision.get("latest_completed_phase_preserved") == IF11_PHASE, "purg_pre decision preserved phase mismatch")
    _require(decision.get("latest_completed_status_preserved") == IF11_STATUS, "purg_pre decision preserved status mismatch")
    _require(decision.get("live_route_opened") is False, "purg_pre decision must not claim live route opened")
    _require(decision.get("route_opening_candidate_created") is True, "purg_pre decision route candidate mismatch")
    _require(decision.get("live_route_preserved_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "purg_pre decision preserved next phase mismatch")
    _require(decision.get("live_route_preserved_next_phase_class") == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "purg_pre decision preserved next phase class mismatch")
    _require(decision.get("requested_next_phase_candidate") == "PURG-PRE", "purg_pre decision requested next phase mismatch")
    _require(decision.get("requested_next_phase_class_candidate") == "purgatorium_full_authority_materialization", "purg_pre decision requested phase class mismatch")
    _require(decision.get("schema_allows_purg_pre_live_route") is False, "purg_pre decision schema flag mismatch")
    _require(decision.get("validator_allows_purg_pre_live_route") is False, "purg_pre decision validator flag mismatch")
    _require(decision.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "purg_pre decision active roadmap mismatch")
    _require(decision.get("forensic_infernus_copy_path") == "excludent/infernus/roadmaps/infernus_full_canonroadmap.md", "purg_pre decision forensic path mismatch")
    _require(decision.get("superseded_infernus_stub_path") == "project_mirror/docs/infernus_full/infernus_full_canonroadmap.md", "purg_pre decision stub path mismatch")
    _require(decision.get("runtime_executed") is False, "purg_pre decision runtime_executed mismatch")
    _require(decision.get("real_apply_executed") is False, "purg_pre decision real_apply_executed mismatch")
    _require(decision.get("product_bedrock_real_apply_secrets_executed") is False, "purg_pre decision real surface mismatch")

    summary = _load_json(PURG_PRE_SUMMARY_PATH)
    _require(summary.get("decision") == "pass", "purg_pre summary decision mismatch")
    _require(summary.get("does_not_advance_phase") is True, "purg_pre summary preserve-phase mismatch")
    _require(summary.get("live_route_opened") is False, "purg_pre summary live route mismatch")
    _require(summary.get("route_opening_candidate_created") is True, "purg_pre summary route candidate mismatch")
    _require(summary.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "purg_pre summary active roadmap mismatch")

    no_real_execution = _load_json(PURG_PRE_NO_REAL_EXECUTION_PATH)
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
    ):
        _require(no_real_execution.get(key) is False, f"purg_pre no_real_execution {key} mismatch")

    excludent_manifest = _load_json(PURG_PRE_EXCLUDENT_MANIFEST_PATH)
    _require(excludent_manifest.get("decision") == "pass", "purg_pre excludent manifest decision mismatch")
    _require(excludent_manifest.get("classification") == "excluded_from_context", "purg_pre excludent manifest classification mismatch")
    _require(excludent_manifest.get("read_by_default") is False, "purg_pre excludent manifest read_by_default mismatch")
    _require(excludent_manifest.get("authority") == "none", "purg_pre excludent manifest authority mismatch")
    _require(excludent_manifest.get("use") == "forensic_only", "purg_pre excludent manifest use mismatch")
    _require(excludent_manifest.get("superseded_by") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "purg_pre excludent manifest superseded_by mismatch")

    route_candidate = _load_json(PURG_PRE_ROUTE_OPENING_CANDIDATE_PATH)
    _require(route_candidate.get("phase_id") == "PURG-PRE", "purg_pre route candidate phase_id mismatch")
    _require(route_candidate.get("status") == "route_opening_candidate_created", "purg_pre route candidate status mismatch")
    _require(route_candidate.get("live_route_opened") is False, "purg_pre route candidate live route mismatch")
    _require(route_candidate.get("schema_allows_live_route_mutation") is False, "purg_pre route candidate schema mismatch")
    _require(route_candidate.get("validator_allows_live_route_mutation") is False, "purg_pre route candidate validator mismatch")
    _require(route_candidate.get("preserved_live_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "purg_pre route candidate preserved next phase mismatch")
    _require(route_candidate.get("preserved_live_next_phase_class") == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "purg_pre route candidate preserved next phase class mismatch")

    _mirror_contains(
        PURGATORIUM_ROADMAP_PATH,
        "# PURGATORIUM — CANON ROADMAP",
        "OPERATOR_APPROVED_CANONROADMAP_FOR_PURGATORIUM_FULL",
        "Purgatorium não pode fechar.",
        "PURG-PRE  — Canonical Authority Materialization & Route Opening",
    )
    _mirror_contains(
        INFERNUS_CANONROADMAP_STUB_PATH,
        "classification: excluded_from_context",
        "superseded_by: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
        "forensic copy of the full Infernus canonroadmap",
    )
    _mirror_contains(
        INFERNUS_CANONROADMAP_FORENSIC_PATH,
        "classification: excluded_from_context",
        "superseded_by: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
        "# INFERNUS FULL — CANON ROADMAP",
    )
    _mirror_contains(
        PURG_PRE_REPORT_PATH,
        "decision: `pass`",
        "route_opening_candidate_created: `true`",
        "live_route_opened: `false`",
        "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
    )


def _check_purg_operator_review_packet_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG_OPERATOR_REVIEW_DECISION_PATH,
        PURG_OPERATOR_REVIEW_SUMMARY_PATH,
        PURG_OPERATOR_REVIEW_REPORT_PATH,
        PURG_OPERATOR_REVIEW_SCHEMA_GAP_PATH,
        PURG_OPERATOR_REVIEW_VALIDATOR_GAP_PATH,
        PURG_OPERATOR_REVIEW_FUTURE_PATCH_PLAN_PATH,
        PURG_OPERATOR_REVIEW_NO_REAL_EXECUTION_PATH,
    ):
        _require(path.exists(), f"missing PURG operator review artifact: {path}")

    decision = _load_json(PURG_OPERATOR_REVIEW_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-OPERATOR-REVIEW-PACKET", "purg operator review decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "purg operator review decision must be pass")
    _require(decision.get("status") == "purg_operator_review_packet_pass", "purg operator review decision status mismatch")
    _require(decision.get("does_not_advance_phase") is True, "purg operator review must not advance phase")
    _require(decision.get("live_route_opened") is False, "purg operator review must not open live route")
    _require(decision.get("live_route_preserved_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "purg operator review preserved next phase mismatch")
    _require(decision.get("live_route_preserved_next_phase_class") == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "purg operator review preserved next phase class mismatch")
    _require(decision.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "purg operator review active roadmap mismatch")
    _require(decision.get("route_opening_candidate_source") == "artifacts/purgatorium/purg_pre_route_opening_candidate.json", "purg operator review candidate source mismatch")
    _require(decision.get("schema_gap_matrix_created") is True, "purg operator review schema gap flag mismatch")
    _require(decision.get("validator_gap_matrix_created") is True, "purg operator review validator gap flag mismatch")
    _require(decision.get("future_patch_plan_created") is True, "purg operator review future patch flag mismatch")
    _require(decision.get("operator_review_packet_created") is True, "purg operator review packet flag mismatch")
    _require(decision.get("runtime_executed") is False, "purg operator review runtime_executed mismatch")
    _require(decision.get("real_apply_executed") is False, "purg operator review real_apply_executed mismatch")
    _require(decision.get("product_bedrock_real_apply_secrets_executed") is False, "purg operator review real surface mismatch")

    summary = _load_json(PURG_OPERATOR_REVIEW_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-OPERATOR-REVIEW-PACKET", "purg operator review summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "purg operator review summary decision mismatch")
    _require(summary.get("status") == "purg_operator_review_packet_pass", "purg operator review summary status mismatch")
    _require(summary.get("live_route_opened") is False, "purg operator review summary live route mismatch")
    _require(summary.get("future_patch_plan_created") is True, "purg operator review summary future patch flag mismatch")

    schema_gap = _load_json(PURG_OPERATOR_REVIEW_SCHEMA_GAP_PATH)
    _require(schema_gap.get("requested_phase") == "PURG-PRE", "purg schema gap requested_phase mismatch")
    _require(schema_gap.get("requested_phase_class") == "purgatorium_full_authority_materialization", "purg schema gap requested_phase_class mismatch")
    _require(schema_gap.get("current_schema_accepts_phase") is False, "purg schema gap current_schema_accepts_phase mismatch")
    _require(schema_gap.get("current_schema_accepts_phase_class") is False, "purg schema gap current_schema_accepts_phase_class mismatch")
    _require(schema_gap.get("operator_decision_required") is True, "purg schema gap operator_decision_required mismatch")
    _require("active_next_phase_class" in schema_gap.get("required_schema_change", ""), "purg schema gap required_schema_change mismatch")

    validator_gap = _load_json(PURG_OPERATOR_REVIEW_VALIDATOR_GAP_PATH)
    _require(validator_gap.get("current_validator_enforces") == "INF-FULL-07 -> IF-08", "purg validator gap current enforcement mismatch")
    _require(validator_gap.get("requested_transition") == "INF-FULL-07 -> PURG-PRE", "purg validator gap requested transition mismatch")
    _require(validator_gap.get("validator_accepts_requested_transition") is False, "purg validator gap acceptance mismatch")
    _require("EXPECTED_NEXT_PHASE_ID" in validator_gap.get("required_validator_change", ""), "purg validator gap required change mismatch")
    _require(isinstance(validator_gap.get("tests_required_before_acceptance"), list), "purg validator gap tests list missing")
    _require("tests/test_active_context_route_sync_unittest.py::test_purg_operator_review_packet_artifacts_validate" in validator_gap.get("tests_required_before_acceptance", []), "purg validator gap tests list mismatch")

    no_real_execution = _load_json(PURG_OPERATOR_REVIEW_NO_REAL_EXECUTION_PATH)
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
        "real_audio_capture_allowed",
        "real_stt_tts_allowed",
        "microphone_access_allowed",
        "voice_clone_or_impersonation_allowed",
    ):
        _require(no_real_execution.get(key) is False, f"purg operator review no_real_execution {key} mismatch")

    _mirror_contains(
        PURG_OPERATOR_REVIEW_REPORT_PATH,
        "VERDICT",
        "PASS",
        "WHAT CHANGED IN PURG-PRE",
        "WHY LIVE ROUTE IS NOT OPEN",
        "WHAT WOULD BE REQUIRED TO OPEN PURG-PRE LATER",
        "SAFETY LOCKS",
        "DO NOT DO YET",
        "JSON > roadmap.",
        "all hard locks remain false",
    )
    _mirror_contains(
        PURG_OPERATOR_REVIEW_FUTURE_PATCH_PLAN_PATH,
        "PATCH PLAN ONLY - DO NOT APPLY IN THIS PHASE",
        "1. schema enum change needed",
        "2. validator transition rule change needed",
        "3. ROADMAP_CANONICAL Transition Table row needed",
        "4. ACTIVE_CONTEXT_STATE live route mutation needed",
        "5. mirror sync needed",
        "6. tests needed",
        "7. CI green required",
        "8. rollback plan",
    )


def _check_purg_pre_route_admission_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG_PRE_ROUTE_ADMISSION_DECISION_PATH,
        PURG_PRE_ROUTE_ADMISSION_SUMMARY_PATH,
        PURG_PRE_ROUTE_ADMISSION_REPORT_PATH,
        PURG_PRE_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH,
        PURG_PRE_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH,
        PURG_PRE_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH,
        PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH,
        PURG_PRE_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH,
    ):
        _require(path.exists(), f"missing PURG-PRE route admission artifact: {path}")

    decision = _load_json(PURG_PRE_ROUTE_ADMISSION_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-PRE-ROUTE-ADMISSION", "route admission decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "route admission decision must be pass")
    _require(decision.get("status") == PURG_PRE_ROUTE_ADMISSION_STATUS, "route admission decision status mismatch")
    _require(decision.get("does_not_execute_purg_pre") is True, "route admission must not execute PURG-PRE")
    _require(decision.get("does_not_open_purg_00") is True, "route admission must not open PURG-00")
    _require(decision.get("operator_authorization_source") == PURG_PRE_ROUTE_ADMISSION_OPERATOR_SOURCE, "route admission operator authorization mismatch")
    _require(decision.get("latest_completed_phase_preserved") == IF11_PHASE, "route admission preserved phase mismatch")
    _require(decision.get("latest_completed_status_preserved") == IF11_STATUS, "route admission preserved status mismatch")
    _require(decision.get("previous_live_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "route admission previous next phase mismatch")
    _require(decision.get("previous_live_next_phase_class") == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "route admission previous next phase class mismatch")
    _require(decision.get("new_live_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "route admission new next phase mismatch")
    _require(decision.get("new_live_next_phase_class") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "route admission new next phase class mismatch")
    _require(decision.get("live_route_opened") is True, "route admission must open live route")
    _require(decision.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "route admission active roadmap mismatch")
    _require(decision.get("operator_review_packet_source") == "artifacts/purgatorium/purg_operator_review_packet_decision.json", "route admission operator review packet mismatch")
    _require(decision.get("schema_patch_applied") is True, "route admission schema patch flag mismatch")
    _require(decision.get("validator_patch_applied") is True, "route admission validator patch flag mismatch")
    _require(decision.get("transition_table_patch_applied") is True, "route admission transition table patch flag mismatch")
    _require(decision.get("active_context_live_route_mutation_applied") is True, "route admission live route mutation flag mismatch")
    _require(decision.get("mirrors_updated") is True, "route admission mirrors_updated mismatch")
    _require(decision.get("tests_updated") is True, "route admission tests_updated mismatch")
    _require(decision.get("future_next_step") == ROUTE_ADMISSION_NEXT_RECOMMENDED_STEP, "route admission future next step mismatch")
    _require(decision.get("bedrock_ready") is False, "route admission decision bedrock_ready mismatch")
    _require(decision.get("product_ready") is False, "route admission decision product_ready mismatch")
    _require_forbidden_flags_false(decision, "route admission decision")

    summary = _load_json(PURG_PRE_ROUTE_ADMISSION_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-PRE-ROUTE-ADMISSION", "route admission summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "route admission summary decision mismatch")
    _require(summary.get("status") == PURG_PRE_ROUTE_ADMISSION_STATUS, "route admission summary status mismatch")
    _require(summary.get("live_route_opened") is True, "route admission summary live route mismatch")
    _require(summary.get("new_live_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "route admission summary next phase mismatch")
    _require(summary.get("future_next_step") == ROUTE_ADMISSION_NEXT_RECOMMENDED_STEP, "route admission summary next step mismatch")

    schema_manifest = _load_json(PURG_PRE_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH)
    _require(schema_manifest.get("old_schema_version") == "3.1", "route admission schema manifest old version mismatch")
    _require(schema_manifest.get("new_schema_version") == "3.2", "route admission schema manifest new version mismatch")
    _require(schema_manifest.get("admitted_phase_class") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "route admission schema manifest phase class mismatch")
    _require(schema_manifest.get("schema_patch_applied") is True, "route admission schema manifest applied mismatch")

    validator_manifest = _load_json(PURG_PRE_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH)
    _require(validator_manifest.get("previous_expected_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "route admission validator manifest previous next phase mismatch")
    _require(validator_manifest.get("new_expected_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "route admission validator manifest new next phase mismatch")
    _require(validator_manifest.get("new_expected_next_phase_class") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "route admission validator manifest new next phase class mismatch")
    _require(validator_manifest.get("validator_patch_applied") is True, "route admission validator manifest applied mismatch")
    _require("purg_pre_route_admission_decision.json" in validator_manifest.get("required_artifacts", []), "route admission validator manifest required_artifacts mismatch")

    live_route_manifest = _load_json(PURG_PRE_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH)
    _require(live_route_manifest.get("previous_live_next_phase") == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "route admission live route manifest previous next phase mismatch")
    _require(live_route_manifest.get("new_live_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "route admission live route manifest new next phase mismatch")
    _require(live_route_manifest.get("new_live_next_phase_class") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "route admission live route manifest next phase class mismatch")
    _require(live_route_manifest.get("latest_completed_phase_preserved") == IF11_PHASE, "route admission live route manifest preserved phase mismatch")
    _require(live_route_manifest.get("next_recommended_step_after_mutation") == ROUTE_ADMISSION_NEXT_RECOMMENDED_STEP, "route admission live route manifest next step mismatch")

    no_real_execution = _load_json(PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH)
    _require(no_real_execution.get("does_not_execute_purg_pre") is True, "route admission no_real_execution does_not_execute_purg_pre mismatch")
    _require(no_real_execution.get("does_not_open_purg_00") is True, "route admission no_real_execution does_not_open_purg_00 mismatch")
    _require(no_real_execution.get("bedrock_ready") is False, "route admission no_real_execution bedrock_ready mismatch")
    _require(no_real_execution.get("product_ready") is False, "route admission no_real_execution product_ready mismatch")
    _require_forbidden_flags_false(no_real_execution, "route admission no_real_execution")

    _mirror_contains(
        PURG_PRE_ROUTE_ADMISSION_REPORT_PATH,
        "# PURG-PRE Route Admission",
        "## VERDICT",
        "PASS",
        "## AUTHORIZATION",
        "pode começar",
        "## WHAT CHANGED",
        "## WHAT DID NOT CHANGE",
        "## WHY THIS IS SAFE",
        "## NEXT STEP",
        "execute_purg_pre_canonical_authority_materialization",
        "## HARD LOCKS",
    )
    _mirror_contains(
        PURG_PRE_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH,
        "If route admission creates drift:",
        "restore active_next_phase/next_phase to IF-08;",
        "restore active_next_phase_class to infernus_full_execution;",
        "restore validator expected route;",
        "report CANONICAL_ROUTE_ADMISSION_ROLLBACK_COMPLETE.",
    )

    route_admission_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            PURG_PRE_ROUTE_ADMISSION_DECISION_PATH,
            PURG_PRE_ROUTE_ADMISSION_SUMMARY_PATH,
            PURG_PRE_ROUTE_ADMISSION_REPORT_PATH,
        )
    )
    _require("finding_closed" not in route_admission_text, "route admission must not claim finding_closed")
    _require("\"phase_id\": \"PURG-00\"" not in route_admission_text, "route admission must not declare PURG-00")
    _require("PURG-00 | pass" not in route_admission_text, "route admission must not declare PURG-00 pass")


def _check_purg_pre_authority_execution_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH,
        PURG_PRE_AUTHORITY_EXECUTION_SUMMARY_PATH,
        PURG_PRE_AUTHORITY_EXECUTION_REPORT_PATH,
        PURG_PRE_AUTHORITY_SOURCE_INDEX_PATH,
        PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH,
        PURG_PRE_NO_PURG00_ATTESTATION_PATH,
        PURG_PRE_NO_REAL_EXECUTION_V2_PATH,
        PURG_PRE_FUTURE_PURG00_CANDIDATE_PATH,
    ):
        _require(path.exists(), f"missing PURG-PRE authority execution artifact: {path}")

    decision = _load_json(PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-PRE-CANONICAL-AUTHORITY-EXECUTION", "authority execution decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "authority execution decision must be pass")
    _require(decision.get("status") == PURG_PRE_AUTHORITY_EXECUTION_STATUS, "authority execution decision status mismatch")
    _require(decision.get("route_admission_source") == "artifacts/purgatorium/purg_pre_route_admission_decision.json", "authority execution route_admission_source mismatch")
    _require(decision.get("active_next_phase_verified") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "authority execution active_next_phase_verified mismatch")
    _require(decision.get("active_next_phase_class_verified") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "authority execution active_next_phase_class_verified mismatch")
    _require(decision.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "authority execution roadmap mismatch")
    _require(decision.get("infernus_canonroadmap_status_verified") == "superseded_excludent_forensic_only", "authority execution infernus status mismatch")
    _require(decision.get("if09_if10_if11_handoff_references_verified") is True, "authority execution handoff references mismatch")
    _require(decision.get("purg_pre_executed") is True, "authority execution purg_pre_executed mismatch")
    _require(decision.get("purg_00_opened") is False, "authority execution purg_00_opened mismatch")
    _require(decision.get("purg_00_pass_declared") is False, "authority execution purg_00_pass_declared mismatch")
    _require(decision.get("finding_fix_executed") is False, "authority execution finding_fix_executed mismatch")
    _require(decision.get("candidate_promoted") is False, "authority execution candidate_promoted mismatch")
    _require(decision.get("invalid_finding_remediated") is False, "authority execution invalid_finding_remediated mismatch")
    _require(decision.get("future_purg00_admission_candidate_created") is True, "authority execution future candidate flag mismatch")
    _require_forbidden_flags_false(decision, "authority execution decision")

    summary = _load_json(PURG_PRE_AUTHORITY_EXECUTION_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-PRE-CANONICAL-AUTHORITY-EXECUTION", "authority execution summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "authority execution summary decision mismatch")
    _require(summary.get("status") == PURG_PRE_AUTHORITY_EXECUTION_STATUS, "authority execution summary status mismatch")
    _require(summary.get("purg_pre_executed") is True, "authority execution summary purg_pre_executed mismatch")
    _require(summary.get("purg_00_opened") is False, "authority execution summary purg_00_opened mismatch")
    _require(summary.get("next_recommended_step") == PURG_PRE_AUTHORITY_EXECUTION_NEXT_RECOMMENDED_STEP, "authority execution summary next step mismatch")

    source_index = _load_json(PURG_PRE_AUTHORITY_SOURCE_INDEX_PATH)
    _require(source_index.get("active_context_state") == "ACTIVE_CONTEXT_STATE.json", "authority source index active_context_state mismatch")
    _require(source_index.get("purgatorium_roadmap") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "authority source index roadmap mismatch")
    _require(source_index.get("route_admission_decision") == "artifacts/purgatorium/purg_pre_route_admission_decision.json", "authority source index route admission mismatch")
    _require(source_index.get("operator_review_packet") == "artifacts/purgatorium/purg_operator_review_packet_decision.json", "authority source index operator review mismatch")
    _require(source_index.get("if09_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "authority source index if09 root manifest mismatch")
    _require(source_index.get("if10_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "authority source index if10 graph mismatch")
    _require(source_index.get("validated_handoff_ids") == ["IF09-FIND-001"], "authority source index validated_handoff_ids mismatch")
    _require(source_index.get("contextual_candidate_ids") == ["IF09-FIND-002"], "authority source index contextual_candidate_ids mismatch")
    _require(source_index.get("excluded_invalid_ids") == ["IF09-FIND-003"], "authority source index excluded_invalid_ids mismatch")
    _require(source_index.get("supporting_observation_ids") == ["IF09-OBS-001"], "authority source index supporting_observation_ids mismatch")

    handoff_matrix = _load_json(PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH)
    _require(handoff_matrix.get("if09_references_verified") is True, "authority handoff matrix if09 mismatch")
    _require(handoff_matrix.get("if10_references_verified") is True, "authority handoff matrix if10 mismatch")
    _require(handoff_matrix.get("if11_references_verified") is True, "authority handoff matrix if11 mismatch")
    _require(handoff_matrix.get("validated_handoff_ids") == ["IF09-FIND-001"], "authority handoff matrix validated_handoff_ids mismatch")
    _require(handoff_matrix.get("candidate_promoted") is False, "authority handoff matrix candidate_promoted mismatch")
    _require(handoff_matrix.get("invalid_finding_remediated") is False, "authority handoff matrix invalid_finding_remediated mismatch")

    no_purg00 = _load_json(PURG_PRE_NO_PURG00_ATTESTATION_PATH)
    _require(no_purg00.get("purg_00_opened") is False, "authority no_purg00 purg_00_opened mismatch")
    _require(no_purg00.get("purg_00_pass_declared") is False, "authority no_purg00 purg_00_pass_declared mismatch")
    _require(no_purg00.get("finding_fix_executed") is False, "authority no_purg00 finding_fix_executed mismatch")
    _require(no_purg00.get("candidate_promoted") is False, "authority no_purg00 candidate_promoted mismatch")
    _require(no_purg00.get("invalid_finding_remediated") is False, "authority no_purg00 invalid_finding_remediated mismatch")

    no_real_execution_v2 = _load_json(PURG_PRE_NO_REAL_EXECUTION_V2_PATH)
    _require(no_real_execution_v2.get("purg_pre_executed") is True, "authority no_real_execution_v2 purg_pre_executed mismatch")
    _require(no_real_execution_v2.get("purg_00_opened") is False, "authority no_real_execution_v2 purg_00_opened mismatch")
    _require(no_real_execution_v2.get("bedrock_ready") is False, "authority no_real_execution_v2 bedrock_ready mismatch")
    _require(no_real_execution_v2.get("product_ready") is False, "authority no_real_execution_v2 product_ready mismatch")
    _require_forbidden_flags_false(no_real_execution_v2, "authority no_real_execution_v2")

    future_candidate = _load_json(PURG_PRE_FUTURE_PURG00_CANDIDATE_PATH)
    _require(future_candidate.get("candidate_phase") == "PURG-00", "authority future candidate phase mismatch")
    _require(future_candidate.get("candidate_phase_class") == "purgatorium_full_intake", "authority future candidate phase_class mismatch")
    _require(future_candidate.get("status") == "candidate_only_not_opened", "authority future candidate status mismatch")
    _require(future_candidate.get("requires_transition_table_row") is True, "authority future candidate requires_transition_table_row mismatch")
    _require(future_candidate.get("requires_operator_authorization") is True, "authority future candidate requires_operator_authorization mismatch")
    _require(future_candidate.get("requires_schema_validator_admission") is True, "authority future candidate requires_schema_validator_admission mismatch")
    _require(future_candidate.get("requires_no_real_execution_attestation") is True, "authority future candidate requires_no_real_execution_attestation mismatch")
    _require(future_candidate.get("purg_00_opened_now") is False, "authority future candidate purg_00_opened_now mismatch")
    _require("separate route admission" in future_candidate.get("reason", ""), "authority future candidate reason mismatch")

    _mirror_contains(
        PURG_PRE_AUTHORITY_EXECUTION_REPORT_PATH,
        "# PURG-PRE Canonical Authority Execution",
        "## VERDICT",
        "PASS",
        "## WHAT THIS PHASE EXECUTES",
        "Only PURG-PRE authority/materialization verification.",
        "## WHAT WAS VERIFIED",
        "## WHAT WAS NOT DONE",
        "## NEXT STEP CANDIDATE",
        "Future PURG-00 admission",
        "## HARD LOCKS",
    )

    authority_execution_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH,
            PURG_PRE_AUTHORITY_EXECUTION_SUMMARY_PATH,
            PURG_PRE_AUTHORITY_EXECUTION_REPORT_PATH,
            PURG_PRE_NO_PURG00_ATTESTATION_PATH,
            PURG_PRE_FUTURE_PURG00_CANDIDATE_PATH,
        )
    )
    _require("finding_closed" not in authority_execution_text, "authority execution must not claim finding_closed")
    _require("\"purg_00_opened\": true" not in authority_execution_text, "authority execution must not open PURG-00")
    _require("PURG-00 | pass" not in authority_execution_text, "authority execution must not declare PURG-00 pass")


def _check_purg00_operator_review_packet_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH,
        PURG00_OPERATOR_REVIEW_PACKET_SUMMARY_PATH,
        PURG00_OPERATOR_REVIEW_PACKET_REPORT_PATH,
        PURG00_ROUTE_ADMISSION_SCHEMA_GAP_PATH,
        PURG00_ROUTE_ADMISSION_VALIDATOR_GAP_PATH,
        PURG00_ROUTE_ADMISSION_FUTURE_PATCH_PLAN_PATH,
        PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH,
        PURG00_REQUIRED_SOURCE_ACCESS_MATRIX_PATH,
        PURG00_NOT_OPENED_ATTESTATION_PATH,
    ):
        _require(path.exists(), f"missing PURG-00 operator review artifact: {path}")

    decision = _load_json(PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-00-OPERATOR-REVIEW-PACKET", "purg00 operator review decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "purg00 operator review decision must be pass")
    _require(decision.get("status") == PURG00_OPERATOR_REVIEW_PACKET_STATUS, "purg00 operator review decision status mismatch")
    _require(decision.get("does_not_advance_phase") is True, "purg00 operator review must not advance phase")
    _require(decision.get("purg_pre_execution_source") == "artifacts/purgatorium/purg_pre_canonical_authority_execution_decision.json", "purg00 operator review source mismatch")
    _require(decision.get("future_purg00_candidate_source") == "artifacts/purgatorium/purg_pre_future_purg00_admission_candidate.json", "purg00 operator review future source mismatch")
    _require(decision.get("live_route_opened") is False, "purg00 operator review live_route_opened mismatch")
    _require(decision.get("purg00_opened") is False, "purg00 operator review purg00_opened mismatch")
    _require(decision.get("purg00_executed") is False, "purg00 operator review purg00_executed mismatch")
    _require(decision.get("purg00_pass_declared") is False, "purg00 operator review purg00_pass_declared mismatch")
    _require(decision.get("future_route_admission_still_required") is True, "purg00 operator review future route admission flag mismatch")
    _require(decision.get("requested_next_phase_candidate") == "PURG-00", "purg00 operator review requested_next_phase_candidate mismatch")
    _require(decision.get("requested_next_phase_class_candidate") == "purgatorium_full_intake", "purg00 operator review requested_next_phase_class_candidate mismatch")
    _require(decision.get("schema_gap_matrix_created") is True, "purg00 operator review schema_gap_matrix_created mismatch")
    _require(decision.get("validator_gap_matrix_created") is True, "purg00 operator review validator_gap_matrix_created mismatch")
    _require(decision.get("future_patch_plan_created") is True, "purg00 operator review future_patch_plan_created mismatch")
    _require(decision.get("required_source_access_matrix_created") is True, "purg00 operator review required_source_access_matrix_created mismatch")
    _require(decision.get("operator_review_packet_created") is True, "purg00 operator review operator_review_packet_created mismatch")
    _require(decision.get("finding_fix_executed") is False, "purg00 operator review finding_fix_executed mismatch")
    _require(decision.get("candidate_promoted") is False, "purg00 operator review candidate_promoted mismatch")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 operator review invalid_finding_remediated mismatch")
    _require_forbidden_flags_false(decision, "purg00 operator review decision")

    summary = _load_json(PURG00_OPERATOR_REVIEW_PACKET_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-00-OPERATOR-REVIEW-PACKET", "purg00 operator review summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "purg00 operator review summary decision mismatch")
    _require(summary.get("status") == PURG00_OPERATOR_REVIEW_PACKET_STATUS, "purg00 operator review summary status mismatch")
    _require(summary.get("does_not_advance_phase") is True, "purg00 operator review summary does_not_advance_phase mismatch")
    _require(summary.get("purg00_opened") is False, "purg00 operator review summary purg00_opened mismatch")
    _require(summary.get("purg00_executed") is False, "purg00 operator review summary purg00_executed mismatch")
    _require(summary.get("next_recommended_step") == PURG00_OPERATOR_REVIEW_PACKET_NEXT_RECOMMENDED_STEP, "purg00 operator review summary next step mismatch")

    schema_gap = _load_json(PURG00_ROUTE_ADMISSION_SCHEMA_GAP_PATH)
    _require(schema_gap.get("requested_phase") == "PURG-00", "purg00 schema gap requested_phase mismatch")
    _require(schema_gap.get("requested_phase_class") == "purgatorium_full_intake", "purg00 schema gap requested_phase_class mismatch")
    _require(schema_gap.get("current_schema_accepts_phase") is False, "purg00 schema gap current_schema_accepts_phase mismatch")
    _require(schema_gap.get("current_schema_accepts_phase_class") is False, "purg00 schema gap current_schema_accepts_phase_class mismatch")
    _require("purgatorium_full_intake" in schema_gap.get("required_schema_change", ""), "purg00 schema gap required_schema_change mismatch")
    _require(schema_gap.get("operator_decision_required") is True, "purg00 schema gap operator_decision_required mismatch")

    validator_gap = _load_json(PURG00_ROUTE_ADMISSION_VALIDATOR_GAP_PATH)
    _require(validator_gap.get("current_validator_enforces") == "PURG-PRE remains the live route after authority execution", "purg00 validator gap current_validator_enforces mismatch")
    _require(validator_gap.get("requested_transition") == "PURG-PRE -> PURG-00", "purg00 validator gap requested_transition mismatch")
    _require(validator_gap.get("validator_accepts_requested_transition") is False, "purg00 validator gap validator_accepts_requested_transition mismatch")
    _require("PURG-00 route-admission artifact validation" in validator_gap.get("required_validator_change", ""), "purg00 validator gap required_validator_change mismatch")
    _require(
        validator_gap.get("tests_required_before_acceptance")
        == [
            "validate ACTIVE_CONTEXT_STATE.json",
            "validate ACTIVE_CONTEXT_SCHEMA.json",
            "validate no-real-exec attestation",
            "validate PURG-00 not opened in review packet",
            "validate IF09-FIND-002 not promoted",
            "validate IF09-FIND-003 not remediated",
        ],
        "purg00 validator gap tests_required_before_acceptance mismatch",
    )

    no_real_execution = _load_json(PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH)
    _require(no_real_execution.get("phase_id") == "PURG-00-OPERATOR-REVIEW-PACKET", "purg00 no_real_execution phase_id mismatch")
    _require(no_real_execution.get("status") == PURG00_OPERATOR_REVIEW_PACKET_STATUS, "purg00 no_real_execution status mismatch")
    _require(no_real_execution.get("live_route_opened") is False, "purg00 no_real_execution live_route_opened mismatch")
    _require(no_real_execution.get("purg00_opened") is False, "purg00 no_real_execution purg00_opened mismatch")
    _require(no_real_execution.get("purg00_executed") is False, "purg00 no_real_execution purg00_executed mismatch")
    _require(no_real_execution.get("bedrock_ready") is False, "purg00 no_real_execution bedrock_ready mismatch")
    _require(no_real_execution.get("product_ready") is False, "purg00 no_real_execution product_ready mismatch")
    _require_forbidden_flags_false(no_real_execution, "purg00 no_real_execution")

    required_sources = _load_json(PURG00_REQUIRED_SOURCE_ACCESS_MATRIX_PATH)
    _require(
        required_sources.get("required_for_future_purg00")
        == [
            {
                "source": "ACTIVE_CONTEXT_STATE.json",
                "required": True,
                "purpose": "live state authority",
            },
            {
                "source": "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
                "required": True,
                "purpose": "Purgatorium doctrine and phase contract",
            },
            {
                "source": "IF09 evidence bundle/root manifest",
                "required": True,
                "known_hash": IF11_SOURCE_ROOT_MANIFEST_SHA,
                "purpose": "finding and evidence source",
            },
            {
                "source": "IF10 purgatorium handoff graph",
                "required": True,
                "known_hash": IF11_SOURCE_GRAPH_SHA,
                "purpose": "finding detail, root cause candidates, remediation track, regression/revalidation plan",
            },
            {
                "source": "IF11 closure packet",
                "required": True,
                "purpose": "Minos final verdict and closure boundary",
            },
        ],
        "purg00 required source matrix mismatch",
    )
    _require(required_sources.get("future_blocker_if_missing") == "DATA_GAP_BLOCKED", "purg00 required source blocker mismatch")
    _require(required_sources.get("purg00_must_not_infer_missing_graph_details") is True, "purg00 required source infer_missing_graph_details mismatch")

    not_opened = _load_json(PURG00_NOT_OPENED_ATTESTATION_PATH)
    _require(not_opened.get("phase_id") == "PURG-00-OPERATOR-REVIEW-PACKET", "purg00 not_opened phase_id mismatch")
    _require(not_opened.get("status") == PURG00_OPERATOR_REVIEW_PACKET_STATUS, "purg00 not_opened status mismatch")
    _require(not_opened.get("purg00_opened") is False, "purg00 not_opened purg00_opened mismatch")
    _require(not_opened.get("purg00_executed") is False, "purg00 not_opened purg00_executed mismatch")
    _require(not_opened.get("purg00_pass_declared") is False, "purg00 not_opened purg00_pass_declared mismatch")
    _require(not_opened.get("future_route_admission_still_required") is True, "purg00 not_opened future_route_admission_still_required mismatch")
    _require(not_opened.get("finding_fix_executed") is False, "purg00 not_opened finding_fix_executed mismatch")
    _require(not_opened.get("candidate_promoted") is False, "purg00 not_opened candidate_promoted mismatch")
    _require(not_opened.get("invalid_finding_remediated") is False, "purg00 not_opened invalid_finding_remediated mismatch")

    _mirror_contains(
        PURG00_OPERATOR_REVIEW_PACKET_REPORT_PATH,
        "# PURG-00 Operator Review Packet",
        "## VERDICT",
        "PASS",
        "## WHAT THIS PHASE DOES",
        "Prepares operator review and route admission plan for PURG-00.",
        "## WHAT PURG-00 WOULD DO LATER",
        "## WHY PURG-00 IS NOT OPEN YET",
        "## REQUIRED SOURCES",
        "## RISKS",
        "## WHAT WAS NOT DONE",
        "## NEXT STEP",
        "## HARD LOCKS",
    )
    _mirror_contains(
        PURG00_ROUTE_ADMISSION_FUTURE_PATCH_PLAN_PATH,
        "PATCH PLAN ONLY — DO NOT APPLY IN THIS PHASE",
        "1. Add purgatorium_full_intake to schema live-route phase-class enums.",
        "2. Add ROADMAP_CANONICAL Transition Table row for PURG-PRE | pass | PURG-00.",
        "3. Add validator route rule for PURG-PRE -> PURG-00.",
        "4. Add artifact requirements for PURG-00 route admission.",
        "5. Mutate ACTIVE_CONTEXT_STATE.json only in a dedicated route-admission phase.",
        "10. Rollback restores PURG-PRE as live route.",
    )
    purg00_review_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH,
            PURG00_OPERATOR_REVIEW_PACKET_SUMMARY_PATH,
            PURG00_OPERATOR_REVIEW_PACKET_REPORT_PATH,
            PURG00_NOT_OPENED_ATTESTATION_PATH,
            PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH,
        )
    )
    _require("finding_closed" not in purg00_review_text, "purg00 operator review must not claim finding_closed")
    _require("\"purg00_opened\": true" not in purg00_review_text, "purg00 operator review must not open PURG-00")
    _require("\"purg_00_opened\": true" not in purg00_review_text, "purg00 operator review must not open PURG-00 via legacy key")
    _require("PURG-00 | pass" not in purg00_review_text, "purg00 operator review must not declare PURG-00 pass")


def _check_purg00_route_admission_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG00_ROUTE_ADMISSION_DECISION_PATH,
        PURG00_ROUTE_ADMISSION_SUMMARY_PATH,
        PURG00_ROUTE_ADMISSION_REPORT_PATH,
        PURG00_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH,
        PURG00_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH,
        PURG00_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH,
        PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH,
        PURG00_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH,
    ):
        _require(path.exists(), f"missing PURG-00 route admission artifact: {path}")

    decision = _load_json(PURG00_ROUTE_ADMISSION_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-00-ROUTE-ADMISSION", "purg00 route admission decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "purg00 route admission decision must be pass")
    _require(decision.get("status") == PURG00_ROUTE_ADMISSION_STATUS, "purg00 route admission decision status mismatch")
    _require(decision.get("does_not_execute_purg00") is True, "purg00 route admission does_not_execute_purg00 mismatch")
    _require(decision.get("does_not_execute_intake") is True, "purg00 route admission does_not_execute_intake mismatch")
    _require(decision.get("operator_authorization_source") == PURG00_ROUTE_ADMISSION_OPERATOR_SOURCE, "purg00 route admission operator authorization mismatch")
    _require(decision.get("previous_live_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "purg00 route admission previous_live_next_phase mismatch")
    _require(decision.get("previous_live_next_phase_class") == PURG_PRE_LIVE_ROUTE_PHASE_CLASS, "purg00 route admission previous_live_next_phase_class mismatch")
    _require(decision.get("new_live_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route admission new_live_next_phase mismatch")
    _require(decision.get("new_live_next_phase_class") == EXPECTED_NEXT_PHASE_CLASS, "purg00 route admission new_live_next_phase_class mismatch")
    _require(decision.get("live_route_opened") is True, "purg00 route admission live_route_opened mismatch")
    _require(decision.get("purg00_opened") is True, "purg00 route admission purg00_opened mismatch")
    _require(decision.get("purg00_executed") is False, "purg00 route admission purg00_executed mismatch")
    _require(decision.get("purg00_intake_executed") is False, "purg00 route admission purg00_intake_executed mismatch")
    _require(decision.get("purg00_pass_declared") is False, "purg00 route admission purg00_pass_declared mismatch")
    _require(decision.get("technical_direction_active_document") == "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md", "purg00 route admission roadmap mismatch")
    _require(decision.get("operator_review_packet_source") == "artifacts/purgatorium/purg00_operator_review_packet_decision.json", "purg00 route admission operator review packet mismatch")
    _require(decision.get("required_source_access_matrix_source") == "artifacts/purgatorium/purg00_required_source_access_matrix.json", "purg00 route admission required source access matrix mismatch")
    _require(decision.get("schema_patch_applied") is True, "purg00 route admission schema_patch_applied mismatch")
    _require(decision.get("validator_patch_applied") is True, "purg00 route admission validator_patch_applied mismatch")
    _require(decision.get("transition_table_patch_applied") is True, "purg00 route admission transition_table_patch_applied mismatch")
    _require(decision.get("active_context_live_route_mutation_applied") is True, "purg00 route admission active_context_live_route_mutation_applied mismatch")
    _require(decision.get("mirrors_updated") is True, "purg00 route admission mirrors_updated mismatch")
    _require(decision.get("tests_updated") is True, "purg00 route admission tests_updated mismatch")
    _require(decision.get("future_next_step") == PURG00_ROUTE_ADMISSION_NEXT_STEP, "purg00 route admission future_next_step mismatch")
    _require(decision.get("finding_fix_executed") is False, "purg00 route admission finding_fix_executed mismatch")
    _require(decision.get("candidate_promoted") is False, "purg00 route admission candidate_promoted mismatch")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 route admission invalid_finding_remediated mismatch")
    _require(decision.get("bedrock_ready") is False, "purg00 route admission bedrock_ready mismatch")
    _require(decision.get("product_ready") is False, "purg00 route admission product_ready mismatch")
    _require_forbidden_flags_false(decision, "purg00 route admission decision")

    summary = _load_json(PURG00_ROUTE_ADMISSION_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-00-ROUTE-ADMISSION", "purg00 route admission summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "purg00 route admission summary decision mismatch")
    _require(summary.get("status") == PURG00_ROUTE_ADMISSION_STATUS, "purg00 route admission summary status mismatch")
    _require(summary.get("live_route_opened") is True, "purg00 route admission summary live_route_opened mismatch")
    _require(summary.get("new_live_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route admission summary new_live_next_phase mismatch")
    _require(summary.get("future_next_step") == PURG00_ROUTE_ADMISSION_NEXT_STEP, "purg00 route admission summary future_next_step mismatch")

    schema_manifest = _load_json(PURG00_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH)
    _require(schema_manifest.get("old_schema_version") == "3.2", "purg00 route admission schema manifest old_schema_version mismatch")
    _require(schema_manifest.get("new_schema_version") == "3.3", "purg00 route admission schema manifest new_schema_version mismatch")
    _require(schema_manifest.get("admitted_phase_class") == EXPECTED_NEXT_PHASE_CLASS, "purg00 route admission schema manifest admitted_phase_class mismatch")
    _require(schema_manifest.get("schema_patch_applied") is True, "purg00 route admission schema manifest schema_patch_applied mismatch")

    validator_manifest = _load_json(PURG00_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH)
    _require(validator_manifest.get("previous_expected_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "purg00 route admission validator manifest previous_expected_next_phase mismatch")
    _require(validator_manifest.get("new_expected_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route admission validator manifest new_expected_next_phase mismatch")
    _require(validator_manifest.get("new_expected_next_phase_class") == EXPECTED_NEXT_PHASE_CLASS, "purg00 route admission validator manifest new_expected_next_phase_class mismatch")
    _require(validator_manifest.get("validator_patch_applied") is True, "purg00 route admission validator manifest validator_patch_applied mismatch")
    _require("purg00_route_admission_decision.json" in validator_manifest.get("required_artifacts", []), "purg00 route admission validator manifest required_artifacts mismatch")

    live_route_manifest = _load_json(PURG00_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH)
    _require(live_route_manifest.get("previous_live_next_phase") == PURG_PRE_LIVE_ROUTE_PHASE_ID, "purg00 route admission live route manifest previous_live_next_phase mismatch")
    _require(live_route_manifest.get("new_live_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route admission live route manifest new_live_next_phase mismatch")
    _require(live_route_manifest.get("new_live_next_phase_class") == EXPECTED_NEXT_PHASE_CLASS, "purg00 route admission live route manifest new_live_next_phase_class mismatch")
    _require(live_route_manifest.get("latest_completed_phase_preserved") == IF11_PHASE, "purg00 route admission live route manifest latest_completed_phase_preserved mismatch")
    _require(live_route_manifest.get("next_recommended_step_after_mutation") == PURG00_ROUTE_ADMISSION_NEXT_STEP, "purg00 route admission live route manifest next_recommended_step_after_mutation mismatch")

    no_real_execution = _load_json(PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH)
    _require(no_real_execution.get("phase_id") == "PURG-00-ROUTE-ADMISSION", "purg00 route admission no_real_execution phase_id mismatch")
    _require(no_real_execution.get("status") == PURG00_ROUTE_ADMISSION_STATUS, "purg00 route admission no_real_execution status mismatch")
    _require(no_real_execution.get("purg00_opened") is True, "purg00 route admission no_real_execution purg00_opened mismatch")
    _require(no_real_execution.get("purg00_executed") is False, "purg00 route admission no_real_execution purg00_executed mismatch")
    _require(no_real_execution.get("purg00_intake_executed") is False, "purg00 route admission no_real_execution purg00_intake_executed mismatch")
    _require(no_real_execution.get("bedrock_ready") is False, "purg00 route admission no_real_execution bedrock_ready mismatch")
    _require(no_real_execution.get("product_ready") is False, "purg00 route admission no_real_execution product_ready mismatch")
    _require_forbidden_flags_false(no_real_execution, "purg00 route admission no_real_execution")

    if PURG00_INTAKE_DECISION_PATH.exists():
        purg00_intake = _load_json(PURG00_INTAKE_DECISION_PATH)
        _require(purg00_intake.get("decision") != "pass", "purg00 intake decision must not exist as pass during route admission")

    _mirror_contains(
        PURG00_ROUTE_ADMISSION_REPORT_PATH,
        "# PURG-00 Route Admission",
        "## VERDICT",
        "PASS",
        "## AUTHORIZATION",
        "pode começar PURG-00 route admission",
        "## WHAT CHANGED",
        "## WHAT DID NOT CHANGE",
        "## WHY THIS IS SAFE",
        "## NEXT STEP",
        "execute_purg00_handoff_intake_authority_lock",
        "## HARD LOCKS",
    )
    _mirror_contains(
        PURG00_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH,
        "If PURG-00 route admission creates drift:",
        "restore active_next_phase/next_phase to PURG-PRE;",
        "restore active_next_phase_class to purgatorium_full_authority_materialization;",
        "restore validator expected route;",
        "report PURG00_ROUTE_ADMISSION_ROLLBACK_COMPLETE.",
    )

    route_admission_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            PURG00_ROUTE_ADMISSION_DECISION_PATH,
            PURG00_ROUTE_ADMISSION_SUMMARY_PATH,
            PURG00_ROUTE_ADMISSION_REPORT_PATH,
            PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH,
        )
    )
    _require("finding_closed" not in route_admission_text, "purg00 route admission must not claim finding_closed")
    _require("\"purg00_executed\": true" not in route_admission_text, "purg00 route admission must not execute PURG-00")
    _require("\"purg00_intake_executed\": true" not in route_admission_text, "purg00 route admission must not execute PURG-00 intake")
    _require("\"purg00_pass_declared\": true" not in route_admission_text, "purg00 route admission must not declare PURG-00 pass")


def _check_purg00_handoff_intake_authority_lock_artifacts(state: dict[str, Any]) -> None:
    for path in (
        PURG00_HANDOFF_INTAKE_DECISION_PATH,
        PURG00_HANDOFF_INTAKE_SUMMARY_PATH,
        PURG00_HANDOFF_INTAKE_REPORT_PATH,
        PURG00_SOURCE_PACKET_INDEX_PATH,
        PURG00_HANDOFF_ID_CLASSIFICATION_MATRIX_PATH,
        PURG00_SOURCE_HASH_VERIFICATION_MATRIX_PATH,
        PURG00_DATA_GAP_MATRIX_PATH,
        PURG00_NO_FIX_ATTESTATION_PATH,
        PURG00_NO_REAL_EXECUTION_ATTESTATION_PATH,
        PURG00_FUTURE_PURG01_TRIAGE_CANDIDATE_PATH,
    ):
        _require(path.exists(), f"missing PURG-00 handoff intake artifact: {path}")

    decision = _load_json(PURG00_HANDOFF_INTAKE_DECISION_PATH)
    _require(decision.get("phase_id") == "PURG-00-HANDOFF-INTAKE-AUTHORITY-LOCK", "purg00 handoff intake decision phase_id mismatch")
    _require(decision.get("decision") == PURG00_HANDOFF_INTAKE_DECISION, "purg00 handoff intake decision mismatch")
    _require(decision.get("status") == PURG00_HANDOFF_INTAKE_STATUS, "purg00 handoff intake status mismatch")
    _require(decision.get("route_admission_source") == "artifacts/purgatorium/purg00_route_admission_decision.json", "purg00 handoff intake route_admission_source mismatch")
    _require(decision.get("active_next_phase_verified") == EXPECTED_NEXT_PHASE_ID, "purg00 handoff intake active_next_phase_verified mismatch")
    _require(decision.get("active_next_phase_class_verified") == EXPECTED_NEXT_PHASE_CLASS, "purg00 handoff intake active_next_phase_class_verified mismatch")
    _require(decision.get("latest_completed_phase_preserved") == EXPECTED_PHASE, "purg00 handoff intake latest_completed_phase_preserved mismatch")
    _require(decision.get("latest_completed_status_preserved") == EXPECTED_LATEST_COMPLETED_STATUS, "purg00 handoff intake latest_completed_status_preserved mismatch")
    _require(decision.get("purg00_intake_executed") is True, "purg00 handoff intake purg00_intake_executed mismatch")
    _require(decision.get("authority_lock_created") is True, "purg00 handoff intake authority_lock_created mismatch")
    _require(decision.get("source_packet_index_created") is True, "purg00 handoff intake source_packet_index_created mismatch")
    _require(decision.get("handoff_id_classification_matrix_created") is True, "purg00 handoff intake handoff_id_classification_matrix_created mismatch")
    _require(decision.get("source_hash_verification_matrix_created") is True, "purg00 handoff intake source_hash_verification_matrix_created mismatch")
    _require(decision.get("data_gap_matrix_created") is True, "purg00 handoff intake data_gap_matrix_created mismatch")
    _require(decision.get("future_purg01_triage_candidate_created") is True, "purg00 handoff intake future_purg01_triage_candidate_created mismatch")
    _require(decision.get("if09_root_manifest_verified") is True, "purg00 handoff intake if09_root_manifest_verified mismatch")
    _require(decision.get("if10_graph_verified") is True, "purg00 handoff intake if10_graph_verified mismatch")
    _require(decision.get("if11_closure_boundary_verified") is True, "purg00 handoff intake if11_closure_boundary_verified mismatch")
    _require(decision.get("graph_full_detail_accessible") is False, "purg00 handoff intake graph_full_detail_accessible mismatch")
    _require(decision.get("data_gap_status") == PURG00_HANDOFF_INTAKE_DATA_GAP_STATUS, "purg00 handoff intake data_gap_status mismatch")
    _require(decision.get("missing_required_fields") == PURG00_HANDOFF_INTAKE_MISSING_FIELDS, "purg00 handoff intake missing_required_fields mismatch")
    _require(decision.get("validated_handoff_ids") == ["IF09-FIND-001"], "purg00 handoff intake validated_handoff_ids mismatch")
    _require(decision.get("contextual_candidate_ids") == ["IF09-FIND-002"], "purg00 handoff intake contextual_candidate_ids mismatch")
    _require(decision.get("excluded_invalid_ids") == ["IF09-FIND-003"], "purg00 handoff intake excluded_invalid_ids mismatch")
    _require(decision.get("supporting_observation_ids") == ["IF09-OBS-001"], "purg00 handoff intake supporting_observation_ids mismatch")
    _require(decision.get("candidate_promoted") is False, "purg00 handoff intake candidate_promoted mismatch")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 handoff intake invalid_finding_remediated mismatch")
    _require(decision.get("finding_fix_executed") is False, "purg00 handoff intake finding_fix_executed mismatch")
    _require(decision.get("red_reproduction_executed") is False, "purg00 handoff intake red_reproduction_executed mismatch")
    _require(decision.get("triage_executed") is False, "purg00 handoff intake triage_executed mismatch")
    _require(decision.get("remediation_plan_created") is False, "purg00 handoff intake remediation_plan_created mismatch")
    _require(decision.get("dependency_dag_final_created") is False, "purg00 handoff intake dependency_dag_final_created mismatch")
    _require(decision.get("finding_closed") is False, "purg00 handoff intake finding_closed mismatch")
    _require(decision.get("product_ready") is False, "purg00 handoff intake product_ready mismatch")
    _require(decision.get("bedrock_ready") is False, "purg00 handoff intake bedrock_ready mismatch")
    _require_forbidden_flags_false(decision, "purg00 handoff intake decision")

    summary = _load_json(PURG00_HANDOFF_INTAKE_SUMMARY_PATH)
    _require(summary.get("phase_id") == "PURG-00-HANDOFF-INTAKE-AUTHORITY-LOCK", "purg00 handoff intake summary phase_id mismatch")
    _require(summary.get("decision") == PURG00_HANDOFF_INTAKE_DECISION, "purg00 handoff intake summary decision mismatch")
    _require(summary.get("status") == PURG00_HANDOFF_INTAKE_STATUS, "purg00 handoff intake summary status mismatch")
    _require(summary.get("purg00_intake_executed") is True, "purg00 handoff intake summary purg00_intake_executed mismatch")
    _require(summary.get("authority_lock_created") is True, "purg00 handoff intake summary authority_lock_created mismatch")
    _require(summary.get("data_gap_status") == PURG00_HANDOFF_INTAKE_DATA_GAP_STATUS, "purg00 handoff intake summary data_gap_status mismatch")
    _require(summary.get("next_recommended_step") == PURG00_HANDOFF_INTAKE_NEXT_STEP, "purg00 handoff intake summary next_recommended_step mismatch")

    source_packet_index = _load_json(PURG00_SOURCE_PACKET_INDEX_PATH)
    _require(source_packet_index.get("index_policy") == "primary_source_packet_only_no_inference", "purg00 source packet index policy mismatch")
    _require(source_packet_index.get("graph_file_accessible") is True, "purg00 source packet index graph_file_accessible mismatch")
    _require(source_packet_index.get("graph_full_detail_accessible") is False, "purg00 source packet index graph_full_detail_accessible mismatch")
    packets = source_packet_index.get("packets", [])
    _require(len(packets) == 8, "purg00 source packet index packets length mismatch")
    _require(all(packet.get("accessible") is True for packet in packets), "purg00 source packet index accessible mismatch")

    classification = _load_json(PURG00_HANDOFF_ID_CLASSIFICATION_MATRIX_PATH)
    _require(classification.get("classification_policy") == "source_of_truth_from_IF10_handoff_graph_and_ACTIVE_CONTEXT_STATE", "purg00 handoff classification policy mismatch")
    ids = classification.get("ids", [])
    _require(len(ids) == 4, "purg00 handoff classification ids length mismatch")
    _require(ids[0].get("id") == "IF09-FIND-001" and ids[0].get("class") == "validated_handoff", "purg00 handoff classification IF09-FIND-001 mismatch")
    _require(ids[1].get("id") == "IF09-FIND-002" and ids[1].get("promoted") is False, "purg00 handoff classification IF09-FIND-002 mismatch")
    _require(ids[2].get("id") == "IF09-FIND-003" and ids[2].get("remediated") is False, "purg00 handoff classification IF09-FIND-003 mismatch")
    _require(ids[3].get("id") == "IF09-OBS-001" and ids[3].get("finding") is False, "purg00 handoff classification IF09-OBS-001 mismatch")

    hash_matrix = _load_json(PURG00_SOURCE_HASH_VERIFICATION_MATRIX_PATH)
    _require(hash_matrix.get("if09_root_manifest_sha256_observed") == "3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660", "purg00 source hash IF09 observed mismatch")
    _require(hash_matrix.get("if10_graph_sha256_observed") == "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1", "purg00 source hash IF10 observed mismatch")
    _require(hash_matrix.get("if09_root_manifest_verified") is True, "purg00 source hash IF09 verified mismatch")
    _require(hash_matrix.get("if10_graph_verified") is True, "purg00 source hash IF10 verified mismatch")
    _require(hash_matrix.get("if11_closure_boundary_verified") is True, "purg00 source hash IF11 boundary mismatch")
    _require(hash_matrix.get("hash_mismatch_count") == 0, "purg00 source hash mismatch_count mismatch")
    _require(hash_matrix.get("verification_status") == "pass", "purg00 source hash verification_status mismatch")
    _require_sha256_matches_if_accessible(
        IF09_PROJECT_ROOT_MANIFEST_PATH,
        hash_matrix["if09_root_manifest_sha256_observed"],
        "purg00 source hash IF09",
    )
    _require_sha256_matches_if_accessible(
        IF10_PROJECT_GRAPH_PATH,
        hash_matrix["if10_graph_sha256_observed"],
        "purg00 source hash IF10",
    )

    data_gap = _load_json(PURG00_DATA_GAP_MATRIX_PATH)
    _require(data_gap.get("data_gap_policy") == "do_not_infer_missing_graph_details", "purg00 data gap policy mismatch")
    _require(data_gap.get("graph_full_detail_accessible") is False, "purg00 data gap graph_full_detail_accessible mismatch")
    _require(data_gap.get("missing_required_fields") == PURG00_HANDOFF_INTAKE_MISSING_FIELDS, "purg00 data gap missing_required_fields mismatch")
    _require(data_gap.get("future_purg01_status") == PURG00_HANDOFF_INTAKE_DATA_GAP_STATUS, "purg00 data gap future_purg01_status mismatch")
    _require(data_gap.get("purg00_decision") == "blocked", "purg00 data gap purg00_decision mismatch")

    no_fix = _load_json(PURG00_NO_FIX_ATTESTATION_PATH)
    _require(no_fix.get("status") == PURG00_HANDOFF_INTAKE_STATUS, "purg00 no fix status mismatch")
    _require(no_fix.get("finding_fix_executed") is False, "purg00 no fix finding_fix_executed mismatch")
    _require(no_fix.get("red_reproduction_executed") is False, "purg00 no fix red_reproduction_executed mismatch")
    _require(no_fix.get("triage_executed") is False, "purg00 no fix triage_executed mismatch")
    _require(no_fix.get("remediation_plan_created") is False, "purg00 no fix remediation_plan_created mismatch")
    _require(no_fix.get("dependency_dag_final_created") is False, "purg00 no fix dependency_dag_final_created mismatch")
    _require(no_fix.get("candidate_promoted") is False, "purg00 no fix candidate_promoted mismatch")
    _require(no_fix.get("invalid_finding_remediated") is False, "purg00 no fix invalid_finding_remediated mismatch")
    _require(no_fix.get("finding_closed") is False, "purg00 no fix finding_closed mismatch")
    _require(no_fix.get("product_ready") is False, "purg00 no fix product_ready mismatch")
    _require(no_fix.get("bedrock_ready") is False, "purg00 no fix bedrock_ready mismatch")

    no_real = _load_json(PURG00_NO_REAL_EXECUTION_ATTESTATION_PATH)
    _require(no_real.get("status") == PURG00_HANDOFF_INTAKE_STATUS, "purg00 no real execution status mismatch")
    _require(no_real.get("purg00_intake_executed") is True, "purg00 no real execution purg00_intake_executed mismatch")
    _require_forbidden_flags_false(no_real, "purg00 no real execution attestation")

    future_candidate = _load_json(PURG00_FUTURE_PURG01_TRIAGE_CANDIDATE_PATH)
    _require(future_candidate.get("candidate_phase") == "PURG-01", "purg00 future candidate phase mismatch")
    _require(future_candidate.get("candidate_phase_class") == "purgatorium_full_triage", "purg00 future candidate phase class mismatch")
    _require(future_candidate.get("status") == "candidate_only_not_opened", "purg00 future candidate status mismatch")
    _require(future_candidate.get("requires_transition_table_row") is True, "purg00 future candidate requires_transition_table_row mismatch")
    _require(future_candidate.get("requires_operator_authorization") is True, "purg00 future candidate requires_operator_authorization mismatch")
    _require(future_candidate.get("requires_schema_validator_admission") is True, "purg00 future candidate requires_schema_validator_admission mismatch")
    _require(future_candidate.get("requires_graph_full_detail_access") is True, "purg00 future candidate requires_graph_full_detail_access mismatch")
    _require(future_candidate.get("requires_no_real_execution_attestation") is True, "purg00 future candidate requires_no_real_execution_attestation mismatch")
    _require(future_candidate.get("purg01_opened_now") is False, "purg00 future candidate purg01_opened_now mismatch")
    _require(future_candidate.get("data_gap_status") == PURG00_HANDOFF_INTAKE_DATA_GAP_STATUS, "purg00 future candidate data_gap_status mismatch")

    _mirror_contains(
        PURG00_HANDOFF_INTAKE_REPORT_PATH,
        "# PURG-00 Handoff Intake / Authority Lock",
        "## VERDICT",
        "BLOCKED",
        "## WHAT THIS PHASE DOES",
        "## WHAT WAS VERIFIED",
        "## ID CLASSIFICATION",
        "## DATA GAPS",
        "DATA_GAP_BLOCKED",
        "## WHAT WAS NOT DONE",
        "## NEXT STEP CANDIDATE",
        "## HARD LOCKS",
    )

    handoff_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            PURG00_HANDOFF_INTAKE_DECISION_PATH,
            PURG00_HANDOFF_INTAKE_SUMMARY_PATH,
            PURG00_HANDOFF_INTAKE_REPORT_PATH,
            PURG00_NO_FIX_ATTESTATION_PATH,
            PURG00_NO_REAL_EXECUTION_ATTESTATION_PATH,
        )
    )
    _require("\"candidate_promoted\": true" not in handoff_text, "purg00 handoff intake must not promote candidate")
    _require("\"invalid_finding_remediated\": true" not in handoff_text, "purg00 handoff intake must not remediate invalid finding")
    _require("\"finding_fix_executed\": true" not in handoff_text, "purg00 handoff intake must not fix finding")
    _require("\"red_reproduction_executed\": true" not in handoff_text, "purg00 handoff intake must not reproduce RED")
    _require("\"triage_executed\": true" not in handoff_text, "purg00 handoff intake must not execute triage")
    _require("\"dependency_dag_final_created\": true" not in handoff_text, "purg00 handoff intake must not create dependency dag")
    _require("\"remediation_plan_created\": true" not in handoff_text, "purg00 handoff intake must not create remediation plan")
    _require("\"finding_closed\": true" not in handoff_text, "purg00 handoff intake must not close finding")


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)

    _require(state["phase_id"] == CURRENT_LIVE_PHASE_ID, "unexpected phase_id")
    _require(state["current_phase_id"] == CURRENT_LIVE_PHASE_ID, "unexpected current_phase_id")
    _require(state["previous_phase_id"] == CURRENT_LIVE_PREVIOUS_PHASE_ID, "unexpected previous_phase_id")
    _require(state["status"] == CURRENT_LIVE_STATUS, "unexpected status")
    _require(state["decision"] == EXPECTED_DECISION, "unexpected decision")
    _require(state["latest_completed_phase"] == CURRENT_LIVE_PHASE, "unexpected latest completed phase")
    _require(state["latest_completed_status"] == CURRENT_LIVE_STATUS, "unexpected latest completed status")
    _require(state["current_status"] == CURRENT_LIVE_CURRENT_STATUS, "unexpected current status")
    _require(state["schema_version"] == CURRENT_LIVE_SCHEMA_VERSION, "unexpected schema version")
    _require(state["latest_completed_project_commit_sha"] == CURRENT_LIVE_LATEST_COMPLETED_PROJECT_SHA, "unexpected latest completed project sha")
    _require(state["latest_completed_ci_state"] == CURRENT_LIVE_LATEST_COMPLETED_CI_STATE, "unexpected latest completed ci state")
    _require(state["latest_completed_next_recommended_step"] == CURRENT_LIVE_NEXT_RECOMMENDED_STEP, "unexpected latest completed next step")
    blocker = state.get("purg00_source_gap_terminal_blocker")
    _require(isinstance(blocker, dict), "purg00_source_gap_terminal_blocker must exist")
    _require(blocker.get("decision") == "blocked", "purg00_source_gap_terminal_blocker decision mismatch")
    _require(blocker.get("status") == PURG00_TERMINAL_BLOCKER_STATUS, "purg00_source_gap_terminal_blocker status mismatch")
    _require(blocker.get("previous_gap_artifacts_verified") is True, "purg00_source_gap_terminal_blocker must verify previous artifacts")
    _require(blocker.get("repeated_search_prevented") is True, "purg00_source_gap_terminal_blocker repeated_search_prevented mismatch")
    _require(
        blocker.get("repeat_source_search_without_new_primary_source_forbidden") is True,
        "purg00_source_gap_terminal_blocker must forbid repeated search without new primary source",
    )
    _require(
        blocker.get("missing_required_fields_remaining") == [
            "affected_files",
            "oracle_id",
            "blast_radius",
            "target_control",
            "risk_class",
            "dependency_group",
        ],
        "purg00_source_gap_terminal_blocker missing fields mismatch",
    )
    _require(
        blocker.get("next_recommended_step") == PURG00_REQUIRED_SOURCE_PACKET_STEP,
        "purg00_source_gap_terminal_blocker next step mismatch",
    )
    _require(blocker.get("source_root_manifest_sha256") == IF11_SOURCE_ROOT_MANIFEST_SHA, "terminal blocker root manifest sha mismatch")
    _require(blocker.get("source_graph_sha256") == IF11_SOURCE_GRAPH_SHA, "terminal blocker graph sha mismatch")
    _require(
        blocker.get("operator_required_source_packet") == "artifacts/purgatorium/purg00_operator_required_source_packet.json",
        "terminal blocker operator packet path mismatch",
    )
    _require_project_checkout_artifact(
        PURG00_TERMINAL_BLOCKER_DECISION_PATH,
        "missing purg00 terminal blocker decision artifact",
    )
    _require_project_checkout_artifact(
        PURG00_OPERATOR_REQUIRED_SOURCE_PACKET_PATH,
        "missing purg00 operator required source packet",
    )
    _require_project_checkout_artifact(
        PURG00_MISSING_FIELDS_CONTRACT_SCHEMA_PATH,
        "missing purg00 missing fields contract schema",
    )
    _require_project_checkout_artifact(
        PURG00_NO_LOOP_ATTESTATION_PATH,
        "missing purg00 no-loop attestation",
    )
    _require_project_checkout_artifact(
        PURG00_NO_REAL_EXECUTION_V2_PATH,
        "missing purg00 no real execution attestation v2",
    )
    wait_state = state.get("purg00_route_amendment_terminal_wait_state")
    _require(isinstance(wait_state, dict), "purg00_route_amendment_terminal_wait_state must exist")
    _require(wait_state.get("decision") == "blocked", "purg00_route_amendment_terminal_wait_state decision mismatch")
    _require(wait_state.get("status") == PURG00_ROUTE_AMENDMENT_WAIT_STATE_STATUS, "purg00 route amendment wait-state status mismatch")
    _require(wait_state.get("route_amendment_authorized_by_operator") is True, "purg00 route amendment operator authorization mismatch")
    _require(
        wait_state.get("repeat_source_search_without_new_primary_source_forbidden") is True,
        "purg00 route amendment must preserve repeat-source-search prohibition",
    )
    _require(wait_state.get("previous_live_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route amendment previous_live_next_phase mismatch")
    _require(wait_state.get("previous_live_next_phase_class") == EXPECTED_NEXT_PHASE_CLASS, "purg00 route amendment previous_live_next_phase_class mismatch")
    _require(wait_state.get("new_live_next_phase") is None, "purg00 route amendment new_live_next_phase must be null")
    _require(wait_state.get("new_live_next_phase_class") is None, "purg00 route amendment new_live_next_phase_class must be null")
    _require(wait_state.get("live_route_closed") is True, "purg00 route amendment live_route_closed mismatch")
    _require(wait_state.get("purg00_unresolved") is True, "purg00 route amendment purg00_unresolved mismatch")
    _require(wait_state.get("purg01_open_authorized") is False, "purg00 route amendment purg01_open_authorized mismatch")
    _require(
        wait_state.get("operator_required_source_packet") == "artifacts/purgatorium/purg00_operator_required_source_packet.json",
        "purg00 route amendment operator_required_source_packet mismatch",
    )
    _require(
        wait_state.get("route_amendment_decision_artifact") == "artifacts/purgatorium/purg00_route_amendment_terminal_wait_state_decision.json",
        "purg00 route amendment decision artifact path mismatch",
    )
    _require(wait_state.get("next_recommended_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg00 route amendment next step mismatch")
    _require(wait_state.get("source_packet_supplied") is True, "purg00 route amendment source_packet_supplied mismatch")
    _require(wait_state.get("source_packet_validated") is True, "purg00 route amendment source_packet_validated mismatch")
    _require(wait_state.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg00 route amendment source_packet_sha256 mismatch")
    _require(wait_state.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg00 route amendment source_packet_project_commit_sha mismatch")
    _require(wait_state.get("source_packet_project_ci_state") == "CI_GREEN_CONFIRMED", "purg00 route amendment source_packet_project_ci_state mismatch")
    _require(wait_state.get("real_execution_authorized") is False, "purg00 route amendment real_execution_authorized mismatch")
    for path, message in (
        (PURG00_ROUTE_AMENDMENT_DECISION_PATH, "missing purg00 route amendment decision artifact"),
        (PURG00_ROUTE_AMENDMENT_SUMMARY_PATH, "missing purg00 route amendment summary artifact"),
        (PURG00_ROUTE_AMENDMENT_REPORT_PATH, "missing purg00 route amendment report artifact"),
        (PURG00_ROUTE_AMENDMENT_LIVE_STATE_MANIFEST_PATH, "missing purg00 route amendment live-state manifest"),
        (PURG00_ROUTE_AMENDMENT_VALIDATOR_MANIFEST_PATH, "missing purg00 route amendment validator manifest"),
        (PURG00_ROUTE_AMENDMENT_SCHEMA_MANIFEST_PATH, "missing purg00 route amendment schema manifest"),
        (PURG00_ROUTE_AMENDMENT_NO_REAL_EXECUTION_PATH, "missing purg00 route amendment no-real-execution attestation"),
        (PURG00_ROUTE_AMENDMENT_ROLLBACK_PLAN_PATH, "missing purg00 route amendment rollback plan"),
    ):
        _require_project_checkout_artifact(path, message)
    if PROJECT_CHECKOUT_PRESENT:
        route_amendment_decision = _load_json(PURG00_ROUTE_AMENDMENT_DECISION_PATH)
        _require(route_amendment_decision.get("phase_id") == "PURG-00-ROUTE-AMENDMENT-TERMINAL-WAIT-STATE", "purg00 route amendment decision phase_id mismatch")
        _require(route_amendment_decision.get("decision") == "blocked", "purg00 route amendment decision mismatch")
        _require(route_amendment_decision.get("status") == PURG00_ROUTE_AMENDMENT_WAIT_STATE_STATUS, "purg00 route amendment decision status mismatch")
        _require(route_amendment_decision.get("new_live_next_phase") is None, "purg00 route amendment decision new_live_next_phase mismatch")
        _require(route_amendment_decision.get("purg01_open_authorized") is False, "purg00 route amendment decision purg01_open_authorized mismatch")
        route_amendment_summary = _load_json(PURG00_ROUTE_AMENDMENT_SUMMARY_PATH)
        _require(route_amendment_summary.get("live_route_closed") is True, "purg00 route amendment summary live_route_closed mismatch")
        _require(route_amendment_summary.get("next_phase") is None, "purg00 route amendment summary next_phase mismatch")
        _require(route_amendment_summary.get("next_recommended_step") == PURG00_REQUIRED_SOURCE_PACKET_STEP, "purg00 route amendment summary next step mismatch")
        route_amendment_live_state = _load_json(PURG00_ROUTE_AMENDMENT_LIVE_STATE_MANIFEST_PATH)
        _require(route_amendment_live_state.get("previous_live_next_phase") == EXPECTED_NEXT_PHASE_ID, "purg00 route amendment live-state previous_live_next_phase mismatch")
        _require(route_amendment_live_state.get("new_live_next_phase") is None, "purg00 route amendment live-state new_live_next_phase mismatch")
        _require(len(route_amendment_live_state.get("registered_artifacts", [])) == 7, "purg00 route amendment live-state registered_artifacts mismatch")
        route_amendment_validator = _load_json(PURG00_ROUTE_AMENDMENT_VALIDATOR_MANIFEST_PATH)
        _require(route_amendment_validator.get("validator_patch_applied") is True, "purg00 route amendment validator manifest mismatch")
        _require(route_amendment_validator.get("new_expected_live_next_phase") is None, "purg00 route amendment validator manifest new_expected_live_next_phase mismatch")
        route_amendment_schema = _load_json(PURG00_ROUTE_AMENDMENT_SCHEMA_MANIFEST_PATH)
        _require(route_amendment_schema.get("old_schema_version") == "3.3", "purg00 route amendment schema manifest old_schema_version mismatch")
        _require(route_amendment_schema.get("new_schema_version") == "3.4", "purg00 route amendment schema manifest new_schema_version mismatch")
        route_amendment_no_real = _load_json(PURG00_ROUTE_AMENDMENT_NO_REAL_EXECUTION_PATH)
        _require(route_amendment_no_real.get("purg01_opened") is False, "purg00 route amendment no-real-execution purg01_opened mismatch")
        _require_forbidden_flags_false(route_amendment_no_real, "purg00 route amendment no real execution attestation")
    intake = state.get("purg00_operator_source_packet_intake")
    _require(isinstance(intake, dict), "purg00_operator_source_packet_intake must exist")
    _require(intake.get("decision") == "pass", "purg00 operator source packet intake decision mismatch")
    _require(intake.get("status") == PURG00_OPERATOR_SOURCE_PACKET_INTAKE_STATUS, "purg00 operator source packet intake status mismatch")
    _require(intake.get("source_packet_supplied") is True, "purg00 operator source packet intake source_packet_supplied mismatch")
    _require(intake.get("source_packet_validated") is True, "purg00 operator source packet intake source_packet_validated mismatch")
    _require(
        intake.get("source_packet_path") == "artifacts/purgatorium/purg00_operator_required_source_packet.json",
        "purg00 operator source packet intake path mismatch",
    )
    _require(intake.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg00 operator source packet intake sha mismatch")
    _require(intake.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg00 operator source packet intake project sha mismatch")
    _require(intake.get("source_packet_project_ci_state") == "CI_GREEN_CONFIRMED", "purg00 operator source packet intake ci state mismatch")
    _require(intake.get("finding_id") == "IF09-FIND-001", "purg00 operator source packet intake finding_id mismatch")
    _require(
        intake.get("required_fields_validated") == [
            "affected_files",
            "oracle_id",
            "blast_radius",
            "target_control",
            "risk_class",
            "dependency_group",
        ],
        "purg00 operator source packet intake required_fields_validated mismatch",
    )
    _require(intake.get("purg01_open_authorized") is False, "purg00 operator source packet intake purg01_open_authorized mismatch")
    _require(intake.get("real_execution_authorized") is False, "purg00 operator source packet intake real_execution_authorized mismatch")
    _require(intake.get("next_recommended_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg00 operator source packet intake next step mismatch")
    review = state.get("purg01_route_admission_review")
    _require(isinstance(review, dict), "purg01_route_admission_review must exist")
    _require(review.get("decision") == "pass", "purg01 route admission review decision mismatch")
    _require(review.get("status") == PURG01_ROUTE_ADMISSION_REVIEW_STATUS, "purg01 route admission review status mismatch")
    _require(review.get("review_scope") == "admission_only_no_triage_no_execution", "purg01 route admission review scope mismatch")
    _require(
        review.get("source_packet_path") == "artifacts/purgatorium/purg00_operator_required_source_packet.json",
        "purg01 route admission review source packet path mismatch",
    )
    _require(review.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 route admission review sha mismatch")
    _require(review.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg01 route admission review project sha mismatch")
    _require(review.get("source_packet_project_ci_state") == "CI_GREEN_CONFIRMED", "purg01 route admission review ci state mismatch")
    _require(
        review.get("source_active_context_commit_sha") == PURG01_ROUTE_ADMISSION_SOURCE_ACTIVE_CONTEXT_SHA,
        "purg01 route admission review active-context sha mismatch",
    )
    _require(review.get("finding_id") == "IF09-FIND-001", "purg01 route admission review finding_id mismatch")
    extracted = review.get("source_packet_fields_extracted")
    _require(isinstance(extracted, dict), "purg01 route admission review extracted fields must exist")
    _require(
        extracted.get("affected_files")
        == [
            "artifacts/infernus/if09_evidence_bundle_vulnerability_register/vuln_register_v4.jsonl",
            "artifacts/infernus/if10_purgatorium_handoff_graph/purgatorium_handoff_graph_v4.json",
            "artifacts/infernus/if10_purgatorium_handoff_graph/handoff_manifest.json",
            "artifacts/purgatorium/purg00_source_data_gap_resolution.json",
            "artifacts/purgatorium/purg00_required_fields_extraction_manifest.json",
        ],
        "purg01 route admission review affected_files mismatch",
    )
    for key, value in (
        ("oracle_id", "PURG00-SOURCE-PACKET-COMPLETENESS-ORACLE-001"),
        ("blast_radius", "purgatorium_handoff_metadata_only_no_runtime_no_product"),
        ("target_control", "purgatorium_handoff_required_field_completeness"),
        ("risk_class", "governance_source_data_gap"),
        ("dependency_group", "if09_if10_if11_purgatorium_handoff_artifacts"),
    ):
        _require(extracted.get(key) == value, f"purg01 route admission review {key} mismatch")
    _require(review.get("live_route_preserved_blocked") is True, "purg01 route admission review live_route_preserved_blocked mismatch")
    _require(review.get("next_phase_remains_null") is True, "purg01 route admission review next_phase_remains_null mismatch")
    _require(review.get("active_next_phase_remains_null") is True, "purg01 route admission review active_next_phase_remains_null mismatch")
    _require(review.get("purg01_open_authorized") is False, "purg01 route admission review purg01_open_authorized mismatch")
    _require(review.get("real_execution_authorized") is False, "purg01 route admission review real_execution_authorized mismatch")
    _require(review.get("candidate_phase") == "PURG-01", "purg01 route admission review candidate_phase mismatch")
    _require(review.get("candidate_phase_class") == "purgatorium_route_admission", "purg01 route admission review candidate_phase_class mismatch")
    _require(review.get("candidate_next_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg01 route admission review candidate_next_step mismatch")
    _require(review.get("next_recommended_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg01 route admission review next step mismatch")
    route_admission = state.get("purg01_route_admission")
    _require(isinstance(route_admission, dict), "purg01_route_admission must exist")
    _require(route_admission.get("decision") == "pass", "purg01 route admission decision mismatch")
    _require(route_admission.get("status") == PURG01_ROUTE_ADMISSION_STATUS, "purg01 route admission status mismatch")
    _require(route_admission.get("operator_authorized") is True, "purg01 route admission operator_authorized mismatch")
    _require(
        route_admission.get("operator_authorization_scope") == PURG01_ROUTE_ADMISSION_OPERATOR_SCOPE,
        "purg01 route admission operator_authorization_scope mismatch",
    )
    _require(
        route_admission.get("source_authorization_text") == PURG01_ROUTE_ADMISSION_OPERATOR_TEXT,
        "purg01 route admission source_authorization_text mismatch",
    )
    _require(route_admission.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 route admission source_packet_sha256 mismatch")
    _require(route_admission.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg01 route admission source_packet_project_commit_sha mismatch")
    _require(route_admission.get("review_project_commit_sha") == "e7b9993896b94618d0d01b4a80c260e301871ac4", "purg01 route admission review_project_commit_sha mismatch")
    _require(route_admission.get("review_active_context_commit_sha") == "ae7b59579f25f95900ed370b1d42f028166b0e5e", "purg01 route admission review_active_context_commit_sha mismatch")
    _require(route_admission.get("purg01_open_authorized") is True, "purg01 route admission purg01_open_authorized mismatch")
    _require(route_admission.get("purg01_triage_authorized") is False, "purg01 route admission purg01_triage_authorized mismatch")
    _require(route_admission.get("real_execution_authorized") is False, "purg01 route admission real_execution_authorized mismatch")
    _require(route_admission.get("next_phase_execution_authorization") is False, "purg01 route admission next_phase_execution_authorization mismatch")
    _require(
        route_admission.get("new_live_next_phase") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID,
        "purg01 route admission new_live_next_phase mismatch",
    )
    _require(
        route_admission.get("new_live_next_phase_class") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_CLASS,
        "purg01 route admission new_live_next_phase_class mismatch",
    )
    _require(route_admission.get("next_recommended_step") == "prepare_purg01_triage_readiness_review", "purg01 route admission next step mismatch")
    triage_review = state.get("purg01_triage_readiness_review")
    _require(isinstance(triage_review, dict), "purg01_triage_readiness_review must exist")
    _require(triage_review.get("decision") == "pass", "purg01 triage readiness review decision mismatch")
    _require(triage_review.get("status") == PURG01_TRIAGE_READINESS_REVIEW_STATUS, "purg01 triage readiness review status mismatch")
    _require(triage_review.get("review_scope") == "readiness_only_no_triage_no_execution", "purg01 triage readiness review scope mismatch")
    _require(triage_review.get("source_packet_path") == "artifacts/purgatorium/purg00_operator_required_source_packet.json", "purg01 triage readiness review source_packet_path mismatch")
    _require(triage_review.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 triage readiness review source_packet_sha256 mismatch")
    _require(triage_review.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg01 triage readiness review source_packet_project_commit_sha mismatch")
    _require(triage_review.get("route_admission_project_commit_sha") == "01b46702ebd1654eb2c217c3a77576e109b4254b", "purg01 triage readiness review route_admission_project_commit_sha mismatch")
    _require(triage_review.get("route_admission_active_context_commit_sha") == "0afe5229c2e25f0b07d4b91f1eacfdff20d81e57", "purg01 triage readiness review route_admission_active_context_commit_sha mismatch")
    _require(triage_review.get("triage_planning_candidate_created") is True, "purg01 triage readiness review triage_planning_candidate_created mismatch")
    _require(triage_review.get("purg01_triage_authorized") is False, "purg01 triage readiness review purg01_triage_authorized mismatch")
    _require(triage_review.get("triage_execution_authorized") is False, "purg01 triage readiness review triage_execution_authorized mismatch")
    _require(triage_review.get("finding_fix_authorized") is False, "purg01 triage readiness review finding_fix_authorized mismatch")
    _require(triage_review.get("real_execution_authorized") is False, "purg01 triage readiness review real_execution_authorized mismatch")
    _require(triage_review.get("candidate_next_step") == "prepare_purg01_triage_planning_gate", "purg01 triage readiness review candidate_next_step mismatch")
    _require(triage_review.get("next_recommended_step") == "prepare_purg01_triage_planning_gate", "purg01 triage readiness review next_recommended_step mismatch")
    planning_gate = state.get("purg01_triage_planning_gate")
    _require(isinstance(planning_gate, dict), "purg01_triage_planning_gate must exist")
    _require(planning_gate.get("decision") == "pass", "purg01 triage planning gate decision mismatch")
    _require(planning_gate.get("status") == PURG01_TRIAGE_PLANNING_GATE_STATUS, "purg01 triage planning gate status mismatch")
    _require(planning_gate.get("planning_scope") == "triage_planning_only_no_execution", "purg01 triage planning gate planning_scope mismatch")
    _require(planning_gate.get("target_finding_id") == "IF09-FIND-001", "purg01 triage planning gate target_finding_id mismatch")
    _require(planning_gate.get("source_packet_path") == "artifacts/purgatorium/purg00_operator_required_source_packet.json", "purg01 triage planning gate source_packet_path mismatch")
    _require(planning_gate.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 triage planning gate source_packet_sha256 mismatch")
    _require(planning_gate.get("source_packet_project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg01 triage planning gate source_packet_project_commit_sha mismatch")
    _require(planning_gate.get("readiness_review_project_commit_sha") == "82c2d6fabb076fdf23f0bac554eeb417e0a7a359", "purg01 triage planning gate readiness_review_project_commit_sha mismatch")
    _require(planning_gate.get("readiness_review_active_context_commit_sha") == "f8fa1d15685f85aeefdf4801386b58f97496a258", "purg01 triage planning gate readiness_review_active_context_commit_sha mismatch")
    _require(planning_gate.get("triage_plan_created") is True, "purg01 triage planning gate triage_plan_created mismatch")
    _require(planning_gate.get("triage_authorization_request_candidate_created") is True, "purg01 triage planning gate triage_authorization_request_candidate_created mismatch")
    _require(planning_gate.get("purg01_triage_authorized") is False, "purg01 triage planning gate purg01_triage_authorized mismatch")
    _require(planning_gate.get("triage_execution_authorized") is False, "purg01 triage planning gate triage_execution_authorized mismatch")
    _require(planning_gate.get("finding_fix_authorized") is False, "purg01 triage planning gate finding_fix_authorized mismatch")
    _require(planning_gate.get("real_execution_authorized") is False, "purg01 triage planning gate real_execution_authorized mismatch")
    _require(planning_gate.get("next_recommended_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage planning gate next_recommended_step mismatch")
    auth_gate = state.get("purg01_triage_authorization_gate")
    _require(isinstance(auth_gate, dict), "purg01_triage_authorization_gate must exist")
    _require(auth_gate.get("decision") == "pass", "purg01 triage authorization gate decision mismatch")
    _require(auth_gate.get("status") == PURG01_TRIAGE_AUTHORIZATION_GATE_STATUS, "purg01 triage authorization gate status mismatch")
    _require(auth_gate.get("operator_authorized") is True, "purg01 triage authorization gate operator_authorized mismatch")
    _require(auth_gate.get("operator_authorization_text") == PURG01_TRIAGE_OPERATOR_TEXT, "purg01 triage authorization gate operator_authorization_text mismatch")
    _require(auth_gate.get("operator_authorization_scope") == PURG01_TRIAGE_OPERATOR_SCOPE, "purg01 triage authorization gate operator_authorization_scope mismatch")
    _require(auth_gate.get("target_finding_id") == "IF09-FIND-001", "purg01 triage authorization gate target_finding_id mismatch")
    _require(auth_gate.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 triage authorization gate source_packet_sha256 mismatch")
    _require(auth_gate.get("planning_gate_project_commit_sha") == "2bfefac900c6c3e7c3f016b7a790570587e57fbb", "purg01 triage authorization gate planning_gate_project_commit_sha mismatch")
    _require(auth_gate.get("planning_gate_active_context_commit_sha") == "c8ee8c8225e74ffa8ba56aae916343fcd3d55b0d", "purg01 triage authorization gate planning_gate_active_context_commit_sha mismatch")
    _require(auth_gate.get("purg01_triage_authorized") is True, "purg01 triage authorization gate purg01_triage_authorized mismatch")
    _require(auth_gate.get("triage_execution_authorized") is False, "purg01 triage authorization gate triage_execution_authorized mismatch")
    _require(auth_gate.get("finding_fix_authorized") is False, "purg01 triage authorization gate finding_fix_authorized mismatch")
    _require(auth_gate.get("real_execution_authorized") is False, "purg01 triage authorization gate real_execution_authorized mismatch")
    _require(auth_gate.get("next_recommended_step") == "prepare_purg01_controlled_triage_execution_gate", "purg01 triage authorization gate next_recommended_step mismatch")
    controlled_gate = state.get("purg01_controlled_triage_execution_gate")
    _require(isinstance(controlled_gate, dict), "purg01_controlled_triage_execution_gate must exist")
    _require(controlled_gate.get("decision") == "pass", "purg01 controlled triage execution gate decision mismatch")
    _require(controlled_gate.get("status") == PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_STATUS, "purg01 controlled triage execution gate status mismatch")
    _require(controlled_gate.get("gate_scope") == "artifact_only_readiness_for_controlled_triage", "purg01 controlled triage execution gate scope mismatch")
    _require(controlled_gate.get("finding_id") == "IF09-FIND-001", "purg01 controlled triage execution gate finding_id mismatch")
    _require(controlled_gate.get("source_packet_path") == "artifacts/purgatorium/purg00_operator_required_source_packet.json", "purg01 controlled triage execution gate source_packet_path mismatch")
    _require(controlled_gate.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 controlled triage execution gate source_packet_sha256 mismatch")
    _require(controlled_gate.get("source_graph_sha256") == "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1", "purg01 controlled triage execution gate source_graph_sha256 mismatch")
    _require(controlled_gate.get("source_manifest_sha256") == "b558f97564d14e31f6a4961e5f3e6393b69dbf33bd6a3f4e549b7cf14cdb3bb8", "purg01 controlled triage execution gate source_manifest_sha256 mismatch")
    _require(
        controlled_gate.get("required_fields_present")
        == [
            "finding_id",
            "severity",
            "affected_layer",
            "affected_files",
            "source_bot",
            "source_wave",
            "oracle_id",
            "root_cause_candidate",
            "blast_radius",
            "target_control",
            "reproduction_unit",
            "replay_units",
            "mutation_units",
            "risk_class",
            "dependency_group",
        ],
        "purg01 controlled triage execution gate required_fields_present mismatch",
    )
    _require(controlled_gate.get("required_fields_missing") == [], "purg01 controlled triage execution gate required_fields_missing mismatch")
    _require(controlled_gate.get("validated_handoff_ids") == ["IF09-FIND-001"], "purg01 controlled triage execution gate validated_handoff_ids mismatch")
    _require(controlled_gate.get("contextual_candidate_ids") == ["IF09-FIND-002"], "purg01 controlled triage execution gate contextual_candidate_ids mismatch")
    _require(controlled_gate.get("excluded_invalid_ids") == ["IF09-FIND-003"], "purg01 controlled triage execution gate excluded_invalid_ids mismatch")
    _require(controlled_gate.get("purg01_triage_authorized") is True, "purg01 controlled triage execution gate purg01_triage_authorized mismatch")
    _require(controlled_gate.get("triage_execution_authorized") is False, "purg01 controlled triage execution gate triage_execution_authorized mismatch")
    _require(controlled_gate.get("finding_fix_authorized") is False, "purg01 controlled triage execution gate finding_fix_authorized mismatch")
    _require(controlled_gate.get("real_execution_authorized") is False, "purg01 controlled triage execution gate real_execution_authorized mismatch")
    _require(controlled_gate.get("runtime_allowed") is False, "purg01 controlled triage execution gate runtime_allowed mismatch")
    _require(controlled_gate.get("real_apply_allowed") is False, "purg01 controlled triage execution gate real_apply_allowed mismatch")
    _require(controlled_gate.get("product_bedrock_real_apply_secrets_allowed") is False, "purg01 controlled triage execution gate product_bedrock_real_apply_secrets_allowed mismatch")
    _require(controlled_gate.get("next_recommended_step") == EXPECTED_NEXT_RECOMMENDED_STEP, "purg01 controlled triage execution gate next_recommended_step mismatch")
    artifact_only = state.get("purg01_controlled_triage_artifact_only_execution")
    _require(isinstance(artifact_only, dict), "purg01_controlled_triage_artifact_only_execution must exist")
    _require(artifact_only.get("decision") == "pass", "purg01 controlled triage artifact-only execution decision mismatch")
    _require(artifact_only.get("status") == PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_STATUS, "purg01 controlled triage artifact-only execution status mismatch")
    _require(artifact_only.get("target_finding_id") == "IF09-FIND-001", "purg01 controlled triage artifact-only execution target_finding_id mismatch")
    _require(artifact_only.get("execution_mode") == "artifact_only", "purg01 controlled triage artifact-only execution mode mismatch")
    _require(artifact_only.get("triage_execution_real") is False, "purg01 controlled triage artifact-only execution triage_execution_real mismatch")
    _require(artifact_only.get("finding_fix_executed") is False, "purg01 controlled triage artifact-only execution finding_fix_executed mismatch")
    _require(artifact_only.get("remediation_apply_executed") is False, "purg01 controlled triage artifact-only execution remediation_apply_executed mismatch")
    _require(artifact_only.get("real_execution_authorized") is False, "purg01 controlled triage artifact-only execution real_execution_authorized mismatch")
    _require(artifact_only.get("runtime_allowed") is False, "purg01 controlled triage artifact-only execution runtime_allowed mismatch")
    _require(artifact_only.get("real_apply_allowed") is False, "purg01 controlled triage artifact-only execution real_apply_allowed mismatch")
    _require(artifact_only.get("product_bedrock_real_apply_secrets_allowed") is False, "purg01 controlled triage artifact-only execution product_bedrock_real_apply_secrets_allowed mismatch")
    _require(artifact_only.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 controlled triage artifact-only execution source_packet_sha256 mismatch")
    _require(artifact_only.get("if10_graph_sha256") == "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1", "purg01 controlled triage artifact-only execution if10_graph_sha256 mismatch")
    _require(artifact_only.get("if10_manifest_sha256") == "b558f97564d14e31f6a4961e5f3e6393b69dbf33bd6a3f4e549b7cf14cdb3bb8", "purg01 controlled triage artifact-only execution if10_manifest_sha256 mismatch")
    _require(artifact_only.get("execution_result_artifact") == "artifacts/purgatorium/purg01_controlled_triage_artifact_only_execution_result.json", "purg01 controlled triage artifact-only execution result artifact mismatch")
    _require(artifact_only.get("evidence_matrix_artifact") == "artifacts/purgatorium/purg01_controlled_triage_artifact_only_evidence_matrix.json", "purg01 controlled triage artifact-only execution evidence matrix artifact mismatch")
    _require(artifact_only.get("no_real_execution_attestation_artifact") == "artifacts/purgatorium/purg01_controlled_triage_artifact_only_no_real_execution_attestation.json", "purg01 controlled triage artifact-only execution no real attestation artifact mismatch")
    _require(artifact_only.get("verdict") == "pass", "purg01 controlled triage artifact-only execution verdict mismatch")
    _require(artifact_only.get("next_recommended_step_preserved") == EXPECTED_NEXT_RECOMMENDED_STEP, "purg01 controlled triage artifact-only execution next_recommended_step_preserved mismatch")
    if PROJECT_CHECKOUT_PRESENT:
        packet = _load_json(PURG00_OPERATOR_SOURCE_PACKET_PATH)
        _require(packet.get("packet_id") == "purg00_operator_required_source_packet", "purg00 operator source packet packet_id mismatch")
        _require(packet.get("decision") == "operator_source_supplied", "purg00 operator source packet decision mismatch")
        _require(packet.get("applies_to", {}).get("phase") == "PURG-00", "purg00 operator source packet phase mismatch")
        _require(packet.get("applies_to", {}).get("finding_id") == "IF09-FIND-001", "purg00 operator source packet finding_id mismatch")
        required_fields = packet.get("required_fields", {})
        _require(isinstance(required_fields.get("affected_files"), list) and len(required_fields["affected_files"]) > 0, "purg00 operator source packet affected_files mismatch")
        for key in ("oracle_id", "blast_radius", "target_control", "risk_class", "dependency_group"):
            _require(bool(required_fields.get(key)), f"purg00 operator source packet {key} mismatch")
        forbidden = packet.get("forbidden", {})
        for key in ("inferred_fields", "purg01_opened", "triage_executed", "finding_fix_executed", "real_execution_authorized"):
            _require(forbidden.get(key) is False, f"purg00 operator source packet forbidden flag {key} mismatch")
        _require(hashlib.sha256(PURG00_OPERATOR_SOURCE_PACKET_PATH.read_bytes()).hexdigest() == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg00 operator source packet sha mismatch")
        for path in (
            PURG00_OPERATOR_SOURCE_PACKET_INTAKE_DECISION_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_INTAKE_SUMMARY_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_INTAKE_REPORT_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_HASH_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_CI_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_NO_REAL_PATH,
            PURG00_OPERATOR_SOURCE_PACKET_NEXT_ROUTE_PATH,
        ):
            _require(path.exists(), f"missing purg00 operator source packet intake artifact: {path}")
        intake_decision = _load_json(PURG00_OPERATOR_SOURCE_PACKET_INTAKE_DECISION_PATH)
        _require(intake_decision.get("status") == PURG00_OPERATOR_SOURCE_PACKET_INTAKE_STATUS, "purg00 operator source packet intake decision status mismatch")
        intake_hash = _load_json(PURG00_OPERATOR_SOURCE_PACKET_HASH_PATH)
        _require(intake_hash.get("sha_match") is True, "purg00 operator source packet hash verification mismatch")
        intake_ci = _load_json(PURG00_OPERATOR_SOURCE_PACKET_CI_PATH)
        _require(intake_ci.get("project_commit_sha") == PURG00_OPERATOR_SOURCE_PACKET_PROJECT_SHA, "purg00 operator source packet ci project sha mismatch")
        _require(intake_ci.get("project_ci_state") == "CI_GREEN_CONFIRMED", "purg00 operator source packet ci state mismatch")
        _require(len(intake_ci.get("runs", [])) == 9, "purg00 operator source packet ci runs mismatch")
        for path in (
            PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_DECISION_PATH,
            PURG01_CONTROLLED_TRIAGE_EXECUTION_PRECONDITIONS_PATH,
            PURG01_CONTROLLED_TRIAGE_EXECUTION_NO_REAL_PATH,
            PURG01_CONTROLLED_TRIAGE_EXECUTION_SOURCE_INTEGRITY_PATH,
        ):
            _require(path.exists(), f"missing purg01 controlled triage execution artifact: {path}")
        controlled_decision = _load_json(PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_DECISION_PATH)
        _require(controlled_decision.get("status") == PURG01_CONTROLLED_TRIAGE_EXECUTION_GATE_STATUS, "purg01 controlled triage execution decision status mismatch")
        _require(controlled_decision.get("decision") == "pass", "purg01 controlled triage execution decision mismatch")
        _require(controlled_decision.get("next_recommended_step_candidate") == EXPECTED_NEXT_RECOMMENDED_STEP, "purg01 controlled triage execution decision next step mismatch")
        controlled_matrix = _load_json(PURG01_CONTROLLED_TRIAGE_EXECUTION_PRECONDITIONS_PATH)
        _require(controlled_matrix.get("decision") == "pass", "purg01 controlled triage execution preconditions decision mismatch")
        _require(controlled_matrix.get("required_fields_missing") == [], "purg01 controlled triage execution preconditions required_fields_missing mismatch")
        controlled_no_real = _load_json(PURG01_CONTROLLED_TRIAGE_EXECUTION_NO_REAL_PATH)
        _require(controlled_no_real.get("no_real_execution_attestation") is True, "purg01 controlled triage execution no-real attestation mismatch")
        controlled_integrity = _load_json(PURG01_CONTROLLED_TRIAGE_EXECUTION_SOURCE_INTEGRITY_PATH)
        _require(controlled_integrity.get("decision") == "pass", "purg01 controlled triage execution source integrity decision mismatch")
        _require(controlled_integrity.get("finding_classification_verification", {}).get("validated_handoff_ids") == ["IF09-FIND-001"], "purg01 controlled triage execution source integrity validated_handoff_ids mismatch")
        artifact_only_result = _load_json(PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_RESULT_PATH)
        _require(artifact_only_result.get("phase") == "PURG-01", "purg01 controlled triage artifact-only result phase mismatch")
        _require(artifact_only_result.get("target_finding_id") == "IF09-FIND-001", "purg01 controlled triage artifact-only result target_finding_id mismatch")
        _require(artifact_only_result.get("execution_mode") == "artifact_only", "purg01 controlled triage artifact-only result execution_mode mismatch")
        _require(artifact_only_result.get("triage_execution_real") is False, "purg01 controlled triage artifact-only result triage_execution_real mismatch")
        _require(artifact_only_result.get("finding_fix_executed") is False, "purg01 controlled triage artifact-only result finding_fix_executed mismatch")
        _require(artifact_only_result.get("remediation_apply_executed") is False, "purg01 controlled triage artifact-only result remediation_apply_executed mismatch")
        _require(artifact_only_result.get("real_execution_authorized") is False, "purg01 controlled triage artifact-only result real_execution_authorized mismatch")
        _require(artifact_only_result.get("source_packet_sha256") == PURG00_OPERATOR_SOURCE_PACKET_SHA, "purg01 controlled triage artifact-only result source_packet_sha256 mismatch")
        _require(artifact_only_result.get("if10_graph_sha256") == "c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1", "purg01 controlled triage artifact-only result if10_graph_sha256 mismatch")
        checks = artifact_only_result.get("deterministic_checks")
        _require(isinstance(checks, list) and len(checks) >= 5, "purg01 controlled triage artifact-only result deterministic_checks mismatch")
        for check in checks:
            _require(isinstance(check, dict), "purg01 controlled triage artifact-only check must be object")
            _require(check.get("status") == "pass", "purg01 controlled triage artifact-only deterministic check status mismatch")
            _require(bool(check.get("evidence")), "purg01 controlled triage artifact-only deterministic check evidence mismatch")
        _require(artifact_only_result.get("verdict") == "pass", "purg01 controlled triage artifact-only result verdict mismatch")
        evidence_matrix = _load_json(PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_EVIDENCE_MATRIX_PATH)
        entries = evidence_matrix.get("evidence_matrix")
        _require(isinstance(entries, list) and len(entries) >= 8, "purg01 controlled triage artifact-only evidence matrix entries mismatch")
        for entry in entries:
            _require(isinstance(entry, dict), "purg01 controlled triage artifact-only evidence matrix entry must be object")
            _require(bool(entry.get("source_artifact_path")), "purg01 controlled triage artifact-only evidence matrix source_artifact_path mismatch")
            _require(bool(entry.get("observed_sha256")), "purg01 controlled triage artifact-only evidence matrix observed_sha256 mismatch")
            _require(entry.get("status") == "pass", "purg01 controlled triage artifact-only evidence matrix status mismatch")
            _require(bool(entry.get("excerpt_or_field_verified")), "purg01 controlled triage artifact-only evidence matrix excerpt mismatch")
            _require(entry.get("inference_used") is False, "purg01 controlled triage artifact-only evidence matrix inference_used mismatch")
        artifact_only_no_real = _load_json(PURG01_CONTROLLED_TRIAGE_ARTIFACT_ONLY_NO_REAL_PATH)
        for key in (
            "runtime_executed",
            "real_apply_executed",
            "product_bedrock_real_apply_secrets_executed",
            "external_network_used_except_github_governance",
            "dependency_or_package_manager_used",
            "mcp_activated",
            "rag_ingestion_executed",
            "memory_write_executed",
            "socket_opened",
            "real_cost_spent",
            "real_quota_consumed",
        ):
            _require(artifact_only_no_real.get(key) is False, f"purg01 controlled triage artifact-only no real {key} mismatch")
        intake_no_real = _load_json(PURG00_OPERATOR_SOURCE_PACKET_NO_REAL_PATH)
        _require_forbidden_flags_false(intake_no_real, "purg00 operator source packet no real execution attestation")
        _require(intake_no_real.get("purg01_opened") is False, "purg00 operator source packet no real execution purg01_opened mismatch")
        intake_next_route = _load_json(PURG00_OPERATOR_SOURCE_PACKET_NEXT_ROUTE_PATH)
        _require(intake_next_route.get("candidate_phase") == "PURG-01", "purg00 operator source packet next route candidate phase mismatch")
        _require(intake_next_route.get("purg01_opened_now") is False, "purg00 operator source packet next route candidate purg01_opened_now mismatch")
        for path in (
            PURG01_ROUTE_ADMISSION_REVIEW_DECISION_PATH,
            PURG01_ROUTE_ADMISSION_REVIEW_SUMMARY_PATH,
            PURG01_ROUTE_ADMISSION_REVIEW_REPORT_PATH,
            PURG01_ROUTE_ADMISSION_READINESS_MATRIX_PATH,
            PURG01_ROUTE_ADMISSION_LOCK_MATRIX_PATH,
            PURG01_ROUTE_ADMISSION_NO_REAL_PATH,
            PURG01_ROUTE_ADMISSION_CANDIDATE_PATH,
        ):
            _require(path.exists(), f"missing purg01 route admission review artifact: {path}")
        review_decision = _load_json(PURG01_ROUTE_ADMISSION_REVIEW_DECISION_PATH)
        _require(review_decision.get("status") == PURG01_ROUTE_ADMISSION_REVIEW_STATUS, "purg01 route admission decision status mismatch")
        _require(review_decision.get("candidate_next_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg01 route admission review decision next step mismatch")
        review_summary = _load_json(PURG01_ROUTE_ADMISSION_REVIEW_SUMMARY_PATH)
        _require(review_summary.get("status") == PURG01_ROUTE_ADMISSION_REVIEW_STATUS, "purg01 route admission summary status mismatch")
        _require(review_summary.get("next_phase") is None, "purg01 route admission summary next_phase mismatch")
        readiness_matrix = _load_json(PURG01_ROUTE_ADMISSION_READINESS_MATRIX_PATH)
        _require(readiness_matrix.get("checks", {}).get("required_fields_complete") is True, "purg01 route admission readiness required_fields_complete mismatch")
        _require(readiness_matrix.get("checks", {}).get("candidate_route_is_review_only") is True, "purg01 route admission readiness review-only mismatch")
        lock_matrix = _load_json(PURG01_ROUTE_ADMISSION_LOCK_MATRIX_PATH)
        _require(lock_matrix.get("locks", {}).get("purg01_open_authorized") is False, "purg01 route admission lock matrix purg01_open_authorized mismatch")
        _require(lock_matrix.get("locks", {}).get("real_execution_authorized") is False, "purg01 route admission lock matrix real_execution_authorized mismatch")
        review_no_real = _load_json(PURG01_ROUTE_ADMISSION_NO_REAL_PATH)
        _require_forbidden_flags_false(review_no_real, "purg01 route admission no real execution attestation")
        _require(review_no_real.get("purg01_opened") is False, "purg01 route admission no real execution purg01_opened mismatch")
        review_candidate = _load_json(PURG01_ROUTE_ADMISSION_CANDIDATE_PATH)
        _require(review_candidate.get("candidate_phase") == "PURG-01", "purg01 route admission candidate phase mismatch")
        _require(review_candidate.get("candidate_phase_class") == "purgatorium_route_admission", "purg01 route admission candidate phase class mismatch")
        _require(review_candidate.get("candidate_next_step") == PURG01_REVIEW_NEXT_RECOMMENDED_STEP, "purg01 route admission review candidate next step mismatch")
        _require(review_candidate.get("purg01_opened_now") is False, "purg01 route admission candidate purg01_opened_now mismatch")
        for path in (
            PURG01_ROUTE_ADMISSION_DECISION_PATH,
            PURG01_ROUTE_ADMISSION_SUMMARY_PATH,
            PURG01_ROUTE_ADMISSION_REPORT_PATH,
            PURG01_ROUTE_ADMISSION_OPERATOR_AUTH_PATH,
            PURG01_ROUTE_ADMISSION_LIVE_ROUTE_MANIFEST_PATH,
            PURG01_ROUTE_ADMISSION_SCHEMA_MANIFEST_PATH,
            PURG01_ROUTE_ADMISSION_VALIDATOR_MANIFEST_PATH,
            PURG01_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH,
            PURG01_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH,
        ):
            _require(path.exists(), f"missing purg01 route admission artifact: {path}")
        route_decision = _load_json(PURG01_ROUTE_ADMISSION_DECISION_PATH)
        _require(route_decision.get("status") == PURG01_ROUTE_ADMISSION_STATUS, "purg01 route admission decision status mismatch")
        _require(
            route_decision.get("new_live_next_phase") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID,
            "purg01 route admission decision new_live_next_phase mismatch",
        )
        _require(
            route_decision.get("new_live_next_phase_class") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_CLASS,
            "purg01 route admission decision new_live_next_phase_class mismatch",
        )
        _require(route_decision.get("future_next_step") == "prepare_purg01_triage_readiness_review", "purg01 route admission decision future_next_step mismatch")
        route_summary = _load_json(PURG01_ROUTE_ADMISSION_SUMMARY_PATH)
        _require(route_summary.get("status") == PURG01_ROUTE_ADMISSION_STATUS, "purg01 route admission summary status mismatch")
        _require(
            route_summary.get("new_live_next_phase") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID,
            "purg01 route admission summary new_live_next_phase mismatch",
        )
        operator_auth = _load_json(PURG01_ROUTE_ADMISSION_OPERATOR_AUTH_PATH)
        _require(operator_auth.get("operator_authorization_scope") == PURG01_ROUTE_ADMISSION_OPERATOR_SCOPE, "purg01 route admission operator auth scope mismatch")
        _require(operator_auth.get("purg01_open_authorized") is True, "purg01 route admission operator auth purg01_open_authorized mismatch")
        _require(operator_auth.get("purg01_triage_authorized") is False, "purg01 route admission operator auth purg01_triage_authorized mismatch")
        live_route_manifest = _load_json(PURG01_ROUTE_ADMISSION_LIVE_ROUTE_MANIFEST_PATH)
        _require(live_route_manifest.get("previous_live_next_phase") is None, "purg01 route admission live route previous_live_next_phase mismatch")
        _require(
            live_route_manifest.get("new_live_next_phase") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID,
            "purg01 route admission live route new_live_next_phase mismatch",
        )
        schema_manifest = _load_json(PURG01_ROUTE_ADMISSION_SCHEMA_MANIFEST_PATH)
        _require(schema_manifest.get("old_schema_version") == "3.6", "purg01 route admission schema manifest old_schema_version mismatch")
        _require(schema_manifest.get("new_schema_version") == "3.7", "purg01 route admission schema manifest new_schema_version mismatch")
        validator_manifest = _load_json(PURG01_ROUTE_ADMISSION_VALIDATOR_MANIFEST_PATH)
        _require(validator_manifest.get("previous_expected_next_phase") is None, "purg01 route admission validator manifest previous_expected_next_phase mismatch")
        _require(
            validator_manifest.get("new_expected_next_phase") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_ID,
            "purg01 route admission validator manifest new_expected_next_phase mismatch",
        )
        _require(
            validator_manifest.get("new_expected_next_phase_class") == PURG01_ROUTE_ADMISSION_HISTORICAL_NEXT_PHASE_CLASS,
            "purg01 route admission validator manifest new_expected_next_phase_class mismatch",
        )
        route_no_real = _load_json(PURG01_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH)
        _require(route_no_real.get("status") == PURG01_ROUTE_ADMISSION_STATUS, "purg01 route admission no_real_execution status mismatch")
        _require(route_no_real.get("purg01_open_authorized") is True, "purg01 route admission no_real_execution purg01_open_authorized mismatch")
        _require(route_no_real.get("purg01_triage_authorized") is False, "purg01 route admission no_real_execution purg01_triage_authorized mismatch")
        _require(route_no_real.get("real_execution_authorized") is False, "purg01 route admission no_real_execution real_execution_authorized mismatch")
        _require_forbidden_flags_false(route_no_real, "purg01 route admission no real execution attestation")
        for path in (
            PURG01_TRIAGE_READINESS_REVIEW_DECISION_PATH,
            PURG01_TRIAGE_READINESS_REVIEW_SUMMARY_PATH,
            PURG01_TRIAGE_READINESS_REVIEW_REPORT_PATH,
            PURG01_TRIAGE_READINESS_MATRIX_PATH,
            PURG01_TRIAGE_LOCK_MATRIX_PATH,
            PURG01_TRIAGE_PLANNING_CANDIDATE_PATH,
        ):
            _require(path.exists(), f"missing purg01 triage readiness artifact: {path}")
        triage_decision = _load_json(PURG01_TRIAGE_READINESS_REVIEW_DECISION_PATH)
        _require(triage_decision.get("status") == PURG01_TRIAGE_READINESS_REVIEW_STATUS, "purg01 triage readiness decision status mismatch")
        _require(triage_decision.get("candidate_next_step") == "prepare_purg01_triage_planning_gate", "purg01 triage readiness decision candidate_next_step mismatch")
        triage_summary = _load_json(PURG01_TRIAGE_READINESS_REVIEW_SUMMARY_PATH)
        _require(triage_summary.get("status") == PURG01_TRIAGE_READINESS_REVIEW_STATUS, "purg01 triage readiness summary status mismatch")
        triage_matrix = _load_json(PURG01_TRIAGE_READINESS_MATRIX_PATH)
        _require(triage_matrix.get("checks", {}).get("planning_candidate_only") is True, "purg01 triage readiness matrix planning_candidate_only mismatch")
        triage_lock_matrix = _load_json(PURG01_TRIAGE_LOCK_MATRIX_PATH)
        _require(triage_lock_matrix.get("locks", {}).get("purg01_triage_authorized") is False, "purg01 triage lock matrix purg01_triage_authorized mismatch")
        _require(triage_lock_matrix.get("locks", {}).get("finding_fix_authorized") is False, "purg01 triage lock matrix finding_fix_authorized mismatch")
        triage_candidate = _load_json(PURG01_TRIAGE_PLANNING_CANDIDATE_PATH)
        _require(triage_candidate.get("candidate_next_step") == "prepare_purg01_triage_planning_gate", "purg01 triage planning candidate next step mismatch")
        _require(triage_candidate.get("triage_execution_authorized") is False, "purg01 triage planning candidate triage_execution_authorized mismatch")
        for path in (
            PURG01_TRIAGE_PLANNING_GATE_DECISION_PATH,
            PURG01_TRIAGE_PLANNING_GATE_SUMMARY_PATH,
            PURG01_TRIAGE_PLANNING_GATE_REPORT_PATH,
            PURG01_TRIAGE_PLAN_PATH,
            PURG01_TRIAGE_ORACLE_PLAN_PATH,
            PURG01_TRIAGE_EVIDENCE_REQUIREMENTS_PATH,
            PURG01_TRIAGE_PLANNING_SCOPE_BOUNDARY_PATH,
            PURG01_TRIAGE_EXECUTION_LOCK_MATRIX_PATH,
            PURG01_TRIAGE_PLANNING_NO_REAL_EXECUTION_PATH,
            PURG01_TRIAGE_AUTH_REQUEST_CANDIDATE_PATH,
        ):
            _require(path.exists(), f"missing purg01 triage planning gate artifact: {path}")
        planning_decision = _load_json(PURG01_TRIAGE_PLANNING_GATE_DECISION_PATH)
        _require(planning_decision.get("status") == PURG01_TRIAGE_PLANNING_GATE_STATUS, "purg01 triage planning gate decision status mismatch")
        _require(planning_decision.get("target_finding_id") == "IF09-FIND-001", "purg01 triage planning gate decision target_finding_id mismatch")
        _require(planning_decision.get("next_recommended_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage planning gate decision next_recommended_step mismatch")
        planning_summary = _load_json(PURG01_TRIAGE_PLANNING_GATE_SUMMARY_PATH)
        _require(planning_summary.get("status") == PURG01_TRIAGE_PLANNING_GATE_STATUS, "purg01 triage planning gate summary status mismatch")
        triage_plan = _load_json(PURG01_TRIAGE_PLAN_PATH)
        _require(triage_plan.get("planning_only") is True, "purg01 triage plan planning_only mismatch")
        _require(triage_plan.get("target_finding_id") == "IF09-FIND-001", "purg01 triage plan target_finding_id mismatch")
        _require(triage_plan.get("next_recommended_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage plan next_recommended_step mismatch")
        triage_oracle_plan = _load_json(PURG01_TRIAGE_ORACLE_PLAN_PATH)
        _require(triage_oracle_plan.get("primary_source_packet_oracle_id") == "PURG00-SOURCE-PACKET-COMPLETENESS-ORACLE-001", "purg01 triage oracle plan primary_source_packet_oracle_id mismatch")
        triage_evidence_requirements = _load_json(PURG01_TRIAGE_EVIDENCE_REQUIREMENTS_PATH)
        _require("artifacts/purgatorium/purg00_operator_required_source_packet.json" in triage_evidence_requirements.get("required_source_artifacts", []), "purg01 triage evidence requirements source packet missing")
        triage_scope = _load_json(PURG01_TRIAGE_PLANNING_SCOPE_BOUNDARY_PATH)
        _require(triage_scope.get("allowed_next_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage planning scope boundary allowed_next_step mismatch")
        triage_execution_lock_matrix = _load_json(PURG01_TRIAGE_EXECUTION_LOCK_MATRIX_PATH)
        _require(triage_execution_lock_matrix.get("locks", {}).get("triage_execution_authorized") is False, "purg01 triage execution lock matrix triage_execution_authorized mismatch")
        _require(triage_execution_lock_matrix.get("locks", {}).get("finding_fix_authorized") is False, "purg01 triage execution lock matrix finding_fix_authorized mismatch")
        triage_no_real = _load_json(PURG01_TRIAGE_PLANNING_NO_REAL_EXECUTION_PATH)
        _require(triage_no_real.get("status") == PURG01_TRIAGE_PLANNING_GATE_STATUS, "purg01 triage planning no_real_execution status mismatch")
        _require(triage_no_real.get("purg01_triage_authorized") is False, "purg01 triage planning no_real_execution purg01_triage_authorized mismatch")
        _require(triage_no_real.get("triage_execution_authorized") is False, "purg01 triage planning no_real_execution triage_execution_authorized mismatch")
        _require(triage_no_real.get("finding_fix_authorized") is False, "purg01 triage planning no_real_execution finding_fix_authorized mismatch")
        _require_forbidden_flags_false(triage_no_real, "purg01 triage planning no real execution attestation")
        triage_auth_candidate = _load_json(PURG01_TRIAGE_AUTH_REQUEST_CANDIDATE_PATH)
        _require(triage_auth_candidate.get("candidate_next_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage authorization request candidate next step mismatch")
        _require(triage_auth_candidate.get("authorized_now") is False, "purg01 triage authorization request candidate authorized_now mismatch")
        for path in (
            PURG01_TRIAGE_AUTHORIZATION_GATE_DECISION_PATH,
            PURG01_TRIAGE_AUTHORIZATION_GATE_SUMMARY_PATH,
            PURG01_TRIAGE_AUTHORIZATION_GATE_REPORT_PATH,
            PURG01_TRIAGE_OPERATOR_AUTH_PATH,
            PURG01_TRIAGE_AUTHORIZATION_SCOPE_MATRIX_PATH,
            PURG01_TRIAGE_AUTHORIZATION_LIVE_STATE_MANIFEST_PATH,
            PURG01_TRIAGE_AUTHORIZATION_VALIDATOR_MANIFEST_PATH,
            PURG01_TRIAGE_AUTHORIZATION_SCHEMA_MANIFEST_PATH,
            PURG01_TRIAGE_AUTHORIZATION_NO_REAL_PATH,
            PURG01_TRIAGE_CONTROLLED_EXECUTION_CANDIDATE_PATH,
        ):
            _require(path.exists(), f"missing purg01 triage authorization gate artifact: {path}")
        auth_decision = _load_json(PURG01_TRIAGE_AUTHORIZATION_GATE_DECISION_PATH)
        _require(auth_decision.get("status") == PURG01_TRIAGE_AUTHORIZATION_GATE_STATUS, "purg01 triage authorization gate decision status mismatch")
        _require(auth_decision.get("operator_authorization_text") == PURG01_TRIAGE_OPERATOR_TEXT, "purg01 triage authorization gate decision operator_authorization_text mismatch")
        _require(auth_decision.get("operator_authorization_scope") == PURG01_TRIAGE_OPERATOR_SCOPE, "purg01 triage authorization gate decision operator_authorization_scope mismatch")
        _require(auth_decision.get("purg01_triage_authorized") is True, "purg01 triage authorization gate decision purg01_triage_authorized mismatch")
        _require(auth_decision.get("next_recommended_step") == "prepare_purg01_controlled_triage_execution_gate", "purg01 triage authorization gate decision next_recommended_step mismatch")
        auth_summary = _load_json(PURG01_TRIAGE_AUTHORIZATION_GATE_SUMMARY_PATH)
        _require(auth_summary.get("status") == PURG01_TRIAGE_AUTHORIZATION_GATE_STATUS, "purg01 triage authorization gate summary status mismatch")
        auth_operator = _load_json(PURG01_TRIAGE_OPERATOR_AUTH_PATH)
        _require(auth_operator.get("operator_authorization_text") == PURG01_TRIAGE_OPERATOR_TEXT, "purg01 triage operator authorization text mismatch")
        _require(auth_operator.get("operator_authorization_scope") == PURG01_TRIAGE_OPERATOR_SCOPE, "purg01 triage operator authorization scope mismatch")
        _require(auth_operator.get("purg01_triage_authorized") is True, "purg01 triage operator authorization purg01_triage_authorized mismatch")
        auth_scope_matrix = _load_json(PURG01_TRIAGE_AUTHORIZATION_SCOPE_MATRIX_PATH)
        _require(auth_scope_matrix.get("forbidden", {}).get("finding_fix") is False, "purg01 triage authorization scope matrix finding_fix mismatch")
        _require(auth_scope_matrix.get("forbidden", {}).get("remediation_apply") is False, "purg01 triage authorization scope matrix remediation_apply mismatch")
        auth_live_state_manifest = _load_json(PURG01_TRIAGE_AUTHORIZATION_LIVE_STATE_MANIFEST_PATH)
        _require(auth_live_state_manifest.get("previous_purg01_triage_authorized") is False, "purg01 triage authorization live state previous_purg01_triage_authorized mismatch")
        _require(auth_live_state_manifest.get("new_purg01_triage_authorized") is True, "purg01 triage authorization live state new_purg01_triage_authorized mismatch")
        _require(auth_live_state_manifest.get("next_recommended_step_after_mutation") == "prepare_purg01_controlled_triage_execution_gate", "purg01 triage authorization live state next_recommended_step_after_mutation mismatch")
        auth_validator_manifest = _load_json(PURG01_TRIAGE_AUTHORIZATION_VALIDATOR_MANIFEST_PATH)
        _require(auth_validator_manifest.get("previous_expected_next_step") == "request_operator_authorization_for_purg01_triage", "purg01 triage authorization validator manifest previous_expected_next_step mismatch")
        _require(auth_validator_manifest.get("new_expected_next_step") == "prepare_purg01_controlled_triage_execution_gate", "purg01 triage authorization validator manifest new_expected_next_step mismatch")
        auth_schema_manifest = _load_json(PURG01_TRIAGE_AUTHORIZATION_SCHEMA_MANIFEST_PATH)
        _require(auth_schema_manifest.get("old_schema_version") == "3.9", "purg01 triage authorization schema manifest old_schema_version mismatch")
        _require(auth_schema_manifest.get("new_schema_version") == "3.10", "purg01 triage authorization schema manifest new_schema_version mismatch")
        auth_no_real = _load_json(PURG01_TRIAGE_AUTHORIZATION_NO_REAL_PATH)
        _require(auth_no_real.get("status") == PURG01_TRIAGE_AUTHORIZATION_GATE_STATUS, "purg01 triage authorization no_real_execution status mismatch")
        _require(auth_no_real.get("purg01_triage_authorized") is True, "purg01 triage authorization no_real_execution purg01_triage_authorized mismatch")
        _require(auth_no_real.get("triage_execution_authorized") is False, "purg01 triage authorization no_real_execution triage_execution_authorized mismatch")
        _require(auth_no_real.get("finding_fix_authorized") is False, "purg01 triage authorization no_real_execution finding_fix_authorized mismatch")
        _require(auth_no_real.get("finding_fix_executed") is False, "purg01 triage authorization no_real_execution finding_fix_executed mismatch")
        _require(auth_no_real.get("remediation_apply_executed") is False, "purg01 triage authorization no_real_execution remediation_apply_executed mismatch")
        _require_forbidden_flags_false(auth_no_real, "purg01 triage authorization no real execution attestation")
        controlled_candidate = _load_json(PURG01_TRIAGE_CONTROLLED_EXECUTION_CANDIDATE_PATH)
        _require(controlled_candidate.get("candidate_next_step") == "prepare_purg01_controlled_triage_execution_gate", "purg01 triage controlled execution candidate next step mismatch")
        _require(controlled_candidate.get("purg01_triage_authorized") is True, "purg01 triage controlled execution candidate purg01_triage_authorized mismatch")
        _require(controlled_candidate.get("authorized_now") is False, "purg01 triage controlled execution candidate authorized_now mismatch")
    _require(state["active_context_remote_main_reflects_latest_phase"] is True, "active_context_remote_main_reflects_latest_phase must be true")
    _require(state["permanent_active_update_rule_installed"] is True, "permanent_active_update_rule_installed must be true")
    _require(state["current_phase_bots_executed"] is False, "current_phase_bots_executed must be false")
    _require(state.get("route_amendment_authorized_by_operator") is True, "route_amendment_authorized_by_operator must be true")
    _require(
        state.get("repeat_source_search_without_new_primary_source_forbidden") is True,
        "repeat_source_search_without_new_primary_source_forbidden must be true",
    )
    _require(state["next_phase"] == CURRENT_EXPECTED_NEXT_PHASE_ID, "next_phase must match the current live route")
    _require(state["active_next_phase"] == CURRENT_EXPECTED_NEXT_PHASE_ID, "active_next_phase must match the current live route")
    _require(state["active_next_phase_class"] == CURRENT_EXPECTED_NEXT_PHASE_CLASS, "active_next_phase_class mismatch after live route reconciliation")
    _require(
        state["next_phase_authorized_by_operator"] is False,
        "next phase authorization must remain false until a separate operator merge decision",
    )
    _require(state["anti_proliferation_rule_active"] is True, "anti_proliferation_rule_active must be true")
    _require(state["ci_enforcement_active"] is True, "ci_enforcement_active must be true")

    # Circuit breaker fields
    _require("governance_gate_streak" in state, "governance_gate_streak must be present")
    _require("seen_gate_signatures" in state, "seen_gate_signatures must be present")
    _require("phase_class" in state, "phase_class must be present")
    _check_schema_state_contract(state)

    _check_gate_ttl(state)
    _check_auto_advance(state)
    _check_next_phase_in_transition_table(state)
    _check_minimum_deliverable(state)
    _check_operator_preferences_contract(state)
    _check_ci_terminal_reporting_rule()

    # Three-layer circuit breaker (fixture_materialization not in GOVERNANCE_CLASSES, streak check is a no-op here)
    _check_governance_streak(state)
    sig = _check_gate_signature(state)
    _check_cycle_nudge(state)

    # INF-MAT-01 baseline must remain true for downstream capacity gates.
    _check_fixture_materialization(state)
    # INF-BOT-01 baseline must remain true for INF-MINOS-01.
    _check_bot_execution_artifacts(state)
    # INF-MINOS-01 baseline must remain true for PURG-01.
    _check_minos_verdict_artifacts(state)
    # PURG-01 baseline must remain true for ACB-CORE-01.
    _check_purgatorium_artifacts(state)
    # ACB-CORE-01 baseline must remain true for ACB-CORE-02.
    _check_acb_core_01_project_artifacts(state)
    # ACB-CORE-02 baseline must remain true for ACB-CAP-01.
    _check_acb_core_02_project_artifacts(state)
    # ACB-CAP-01 baseline must remain true for ACB-CAP-02.
    _check_acb_cap_01_project_artifacts(state)
    # ACB-CAP-02 baseline must remain true for ACB-CAP-03.
    _check_acb_cap_02_project_artifacts(state)
    # ACB-CAP-03 baseline must remain true for ACB-CAP-04.
    _check_acb_cap_03_project_artifacts(state)
    # ACB-CAP-04 baseline must remain true for ACB-CAP-05.
    _check_acb_cap_04_project_artifacts(state)
    # ACB-CAP-05 specific checks
    _check_acb_cap_05_project_artifacts(state)
    # INF-FULL-01 scope-charter specific checks
    _check_inf_full_01_project_artifacts(state)
    # INF-FULL-02 baseline freeze planning checks
    _check_inf_full_02_project_artifacts(state)
    # INF-FULL-03 chain registration opening checks
    _check_inf_full_03_project_artifacts(state)
    # INF-FULL-04 scenario pack and harness readiness checks
    _check_inf_full_04_project_artifacts(state)
    # Route sync repair checks
    _check_inf_full_route_sync_artifacts(state)
    # INF-FULL-05 pre-execution review checks
    _check_inf_full_05_project_artifacts(state)
    # INF-FULL-06 excludent quarantine gate checks
    _check_inf_full_06_excludent_quarantine_artifacts(state)
    # INF-FULL-07 IF-08 authorization materialization checks
    _check_inf_full_07_if08_authorization_artifacts(state)
    # IF08 W0.5 active-context sync rule checks
    _check_if08_w05_active_context_sync_artifacts(state)
    # IF08 W0.5 controlled execution checks
    _check_if08_w05_controlled_execution_artifacts(state)
    # IF08 W0.5 post-sync review checks
    _check_if08_w05_post_sync_review_artifacts(state)
    # IF08 W1 controlled execution checks
    _check_if08_w1_controlled_execution_artifacts(state)
    # IF08 W1 post-sync review checks
    _check_if08_w1_post_sync_review_artifacts(state)
    # IF08 W2 auth/HITL/identity/exfil controlled execution checks
    _check_if08_w2_controlled_execution_artifacts(state)
    # IF08 W2 post-sync review checks
    _check_if08_w2_post_sync_review_artifacts(state)
    # IF08 W4 replay/rollback/concurrency/cost preflight readiness checks
    _check_if08_w4_preflight_readiness_artifacts(state)
    # IF08 W4 replay/rollback/concurrency/cost controlled execution checks
    _check_if08_w4_controlled_execution_artifacts(state)
    # IF08 W4 post-sync review and W5 readiness checks
    _check_if08_w4_post_sync_review_artifacts(state)
    # IF08 W5 business chaos controlled execution sync checks
    _check_if08_w5_business_chaos_controlled_execution_artifacts(state)
    # IF08 W5 post-sync review and W6 readiness checks
    _check_if08_w5_post_sync_review_artifacts(state)
    # IF08 W6 final audit controlled execution checks
    _check_if08_w6_final_audit_controlled_execution_artifacts(state)
    # IF09 evidence bundle and vulnerability register checks
    _check_if09_evidence_bundle_vulnerability_register_artifacts(state)
    # IF10 purgatorium handoff graph checks
    _check_if10_purgatorium_handoff_graph_artifacts(state)
    # IF11 minos final verdict closure checks
    _check_if11_minos_final_verdict_closure_artifacts(state)
    # PURG-PRE canonical authority materialization checks
    _check_purg_pre_canonical_authority_materialization_artifacts(state)
    # PURG operator review packet checks
    _check_purg_operator_review_packet_artifacts(state)
    # PURG-PRE route admission checks
    _check_purg_pre_route_admission_artifacts(state)
    # PURG-PRE authority execution checks
    _check_purg_pre_authority_execution_artifacts(state)
    _check_purg00_operator_review_packet_artifacts(state)
    _check_purg00_route_admission_artifacts(state)
    _check_purg00_handoff_intake_authority_lock_artifacts(state)
    # IF08 W3 post-sync review checks
    _check_if08_w3_post_sync_review_artifacts(state)
    # IF08 W3 runtime/tool/MCP/sandbox controlled execution checks
    _check_if08_w3_controlled_execution_artifacts(state)
    # IF08 W3 runtime/tool/MCP/sandbox preflight readiness checks
    _check_if08_w3_preflight_readiness_artifacts(state)
    # IF08 W2 auth/HITL/identity/exfil preflight readiness checks
    _check_if08_w2_preflight_readiness_artifacts(state)
    # IF08 W1 context/memory/RAG preflight readiness checks
    _check_if08_w1_preflight_readiness_artifacts(state)
    # IF08 W0.5 preflight rerun checks
    _check_if08_w05_preflight_rerun_artifacts(state)
    # Historical 13 vs planned 16 normalization checks
    _check_scenario_count_resolution(state)
    _check_purg04_track_a_post_merge_validation_artifacts(state)
    _check_purg_residual_risk_carry_forward_route_opening_artifacts(state)
    _check_inf_revalidation_route_activation_artifacts(state)
    _check_inf_revalidation_readiness_activation_artifacts(state)
    _check_inf_revalidation_operator_authorization_artifacts(state)
    _check_inf_revalidation_execution_artifacts(state)
    _check_inf_revalidation_adjudication_or_closure_artifacts(state)
    _check_if09_closure_milestone_mirror_sanity_artifacts(state)

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase")
    _require_paths_match(state, policy["latest_completed_status_must_match_across"], "latest_completed_status")
    _require_paths_match(state, policy["status_must_match_across"], "status")

    _require(state["current_live_route"]["active_next_phase"] == CURRENT_EXPECTED_NEXT_PHASE_ID, "current live route next phase mismatch")
    _require(state["current_live_route"]["active_next_phase_class"] == CURRENT_EXPECTED_NEXT_PHASE_CLASS, "current live route next phase class mismatch")
    _require(state["current_live_route"]["current_status"] == CURRENT_LIVE_CURRENT_STATUS, "current live route status mismatch")
    _require(state["current_live_route"]["decision"] == EXPECTED_DECISION, "current live route decision mismatch")
    _require(state["current_live_route"]["status"] == CURRENT_LIVE_STATUS, "current live route status mismatch")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next phase execution authorization must be false")
    _require(
        state["current_live_route"]["latest_completed_next_recommended_step"] == CURRENT_LIVE_NEXT_RECOMMENDED_STEP,
        "current live route next step mismatch",
    )

    _require(state["next_action"]["phase"] == CURRENT_EXPECTED_NEXT_PHASE_ID, "next_action.phase mismatch")
    _require(state["next_action"]["phase_class"] == CURRENT_EXPECTED_NEXT_PHASE_CLASS, "next_action.phase_class mismatch")
    _require(state["next_action"]["planning_only"] is False, "next_action.planning_only must be false")
    _require(state["next_action"]["review_only"] is False, "next_action.review_only must be false")
    _require(state["next_action"]["execution_authorization"] is False, "next_action.execution_authorization must be false")
    _require(state["next_action"]["status"] == CURRENT_LIVE_STATUS, "next_action.status mismatch")
    _require(
        CURRENT_LIVE_NEXT_ACTION_NOTE in state["next_action"]["notes"],
        "next_action.notes must mention the exact next phase or terminal wait state",
    )
    _require(state["latest_completed_no_execution"]["wave_executed"] is False, "latest_completed_no_execution.wave_executed mismatch")
    _require(state["latest_completed_no_execution"]["bot_executed"] is False, "latest_completed_no_execution.bot_executed mismatch")
    _require(state["latest_completed_no_execution"]["source_phase_verified"] == IF11_SOURCE_PHASE, "latest_completed_no_execution.source_phase_verified mismatch")
    _require(state["latest_completed_no_execution"]["source_status_verified"] == IF11_SOURCE_STATUS, "latest_completed_no_execution.source_status_verified mismatch")
    _require(state["latest_completed_no_execution"]["source_project_sha_verified_by_packet"] == IF11_SOURCE_PROJECT_SHA, "latest_completed_no_execution.source_project_sha_verified_by_packet mismatch")
    _require(state["latest_completed_no_execution"]["source_active_context_pre_sync_sha_verified_by_packet"] == IF11_SOURCE_ACTIVE_CONTEXT_PRE_SYNC_SHA, "latest_completed_no_execution.source_active_context_pre_sync_sha_verified_by_packet mismatch")
    _require(state["latest_completed_no_execution"]["source_active_context_sync_sha_verified_by_packet"] == IF11_SOURCE_ACTIVE_CONTEXT_SYNC_SHA, "latest_completed_no_execution.source_active_context_sync_sha_verified_by_packet mismatch")
    _require(state["latest_completed_no_execution"]["if11_materialization_performed"] is True, "latest_completed_no_execution.if11_materialization_performed mismatch")
    _require(state["latest_completed_no_execution"]["minos_mechanical_report_created"] is True, "latest_completed_no_execution.minos_mechanical_report_created mismatch")
    _require(state["latest_completed_no_execution"]["minos_semantic_report_created"] is True, "latest_completed_no_execution.minos_semantic_report_created mismatch")
    _require(state["latest_completed_no_execution"]["operator_cosignature_created"] is True, "latest_completed_no_execution.operator_cosignature_created mismatch")
    _require(state["latest_completed_no_execution"]["anti_theater_meta_audit_created"] is True, "latest_completed_no_execution.anti_theater_meta_audit_created mismatch")
    _require(state["latest_completed_no_execution"]["infernus_closure_created"] is True, "latest_completed_no_execution.infernus_closure_created mismatch")
    _require(state["latest_completed_no_execution"]["closure_manifest_created"] is True, "latest_completed_no_execution.closure_manifest_created mismatch")
    _require(state["latest_completed_no_execution"]["final_evidence_index_created"] is True, "latest_completed_no_execution.final_evidence_index_created mismatch")
    _require(state["latest_completed_no_execution"]["purgatorium_readiness_summary_created"] is True, "latest_completed_no_execution.purgatorium_readiness_summary_created mismatch")
    _require(state["latest_completed_no_execution"]["next_phase_boundary_created"] is True, "latest_completed_no_execution.next_phase_boundary_created mismatch")
    _require(state["latest_completed_no_execution"]["source_root_manifest_sha256"] == IF11_SOURCE_ROOT_MANIFEST_SHA, "latest_completed_no_execution.source_root_manifest_sha256 mismatch")
    _require(state["latest_completed_no_execution"]["source_graph_sha256"] == IF11_SOURCE_GRAPH_SHA, "latest_completed_no_execution.source_graph_sha256 mismatch")
    _require(state["latest_completed_no_execution"]["validated_handoff_ids"] == ["IF09-FIND-001"], "latest_completed_no_execution.validated_handoff_ids mismatch")
    _require(state["latest_completed_no_execution"]["contextual_candidate_ids"] == ["IF09-FIND-002"], "latest_completed_no_execution.contextual_candidate_ids mismatch")
    _require(state["latest_completed_no_execution"]["excluded_invalid_ids"] == ["IF09-FIND-003"], "latest_completed_no_execution.excluded_invalid_ids mismatch")
    _require(state["latest_completed_no_execution"]["supporting_observation_ids"] == ["IF09-OBS-001"], "latest_completed_no_execution.supporting_observation_ids mismatch")
    _require(state["latest_completed_no_execution"]["minos_mechanical_verdict"] == "pass", "latest_completed_no_execution.minos_mechanical_verdict mismatch")
    _require(state["latest_completed_no_execution"]["minos_semantic_verdict"] == "pass", "latest_completed_no_execution.minos_semantic_verdict mismatch")
    _require(state["latest_completed_no_execution"]["anti_theater_verdict"] == "pass", "latest_completed_no_execution.anti_theater_verdict mismatch")
    _require(state["latest_completed_no_execution"]["operator_cosignature_status"] == "pending_operator_review", "latest_completed_no_execution.operator_cosignature_status mismatch")
    _require(state["latest_completed_no_execution"]["infernus_closure_status"] == "closed_with_purgatorium_handoff_ready", "latest_completed_no_execution.infernus_closure_status mismatch")
    _require(state["latest_completed_no_execution"]["purgatorium_handoff_ready"] is True, "latest_completed_no_execution.purgatorium_handoff_ready mismatch")
    _require(state["latest_completed_no_execution"]["bedrock_ready"] is False, "latest_completed_no_execution.bedrock_ready mismatch")
    _require(state["latest_completed_no_execution"]["product_ready"] is False, "latest_completed_no_execution.product_ready mismatch")
    _require(state["latest_completed_no_execution"]["real_execution_authorized"] is False, "latest_completed_no_execution.real_execution_authorized mismatch")
    _require(state["latest_completed_no_execution"]["macro_transition_preserved"] is True, "latest_completed_no_execution.macro_transition_preserved mismatch")
    _require(state["latest_completed_no_execution"]["current_phase_id_preserved"] == EXPECTED_PHASE_ID, "latest_completed_no_execution.current_phase_id_preserved mismatch")
    _require(state["latest_completed_no_execution"]["active_next_phase_preserved"] == HISTORICAL_PRESERVED_NEXT_PHASE_ID, "latest_completed_no_execution.active_next_phase_preserved mismatch")
    _require(state["latest_completed_no_execution"]["active_next_phase_class_preserved"] == HISTORICAL_PRESERVED_NEXT_PHASE_CLASS, "latest_completed_no_execution.active_next_phase_class_preserved mismatch")
    _require(state["latest_completed_no_execution"]["real_audio_capture_allowed"] is False, "latest_completed_no_execution.real_audio_capture_allowed must be false")
    _require(state["latest_completed_no_execution"]["real_stt_tts_allowed"] is False, "latest_completed_no_execution.real_stt_tts_allowed must be false")
    _require(state["latest_completed_no_execution"]["microphone_access_allowed"] is False, "latest_completed_no_execution.microphone_access_allowed must be false")
    _require(state["latest_completed_no_execution"]["voice_clone_or_impersonation_allowed"] is False, "latest_completed_no_execution.voice_clone_or_impersonation_allowed must be false")
    _require(state["latest_completed_no_execution"]["execution_scope"] == "artifact_only_final_verdict_closure", "latest_completed_no_execution.execution_scope mismatch")
    _require(state["latest_completed_no_execution"]["blocking_findings_count"] == 0, "latest_completed_no_execution.blocking_findings_count mismatch")
    _require(
        state["latest_completed_no_execution"]["warnings"]
        == [
            "operator_cosignature_pending_review_not_execution_authorization",
            "purgatorium_handoff_ready_does_not_mean_finding_resolved",
        ],
        "latest_completed_no_execution.warnings mismatch",
    )
    for key in (
        "runtime_executed",
        "real_apply_executed",
        "product_bedrock_real_apply_secrets_executed",
        "external_network_used_except_github_governance",
        "dependency_or_package_manager_used",
        "mcp_activated",
        "rag_ingestion_executed",
        "memory_write_executed",
        "socket_opened",
        "shell_executed",
        "filesystem_escape_performed",
        "real_cost_spent",
        "real_quota_consumed",
    ):
        _require(state["latest_completed_no_execution"][key] is False, f"latest_completed_no_execution.{key} must be false")

    _require(state["locks"]["deferred_phase"] == CURRENT_EXPECTED_NEXT_PHASE_ID, "locks.deferred_phase mismatch")
    if CURRENT_EXPECTED_NEXT_PHASE_ID is None:
        _require(
            NO_TRANSITION_DEFINED_MESSAGE in state["locks"]["deferred_phase_reason"],
            "locks.deferred_phase_reason must mention terminal no-transition wait state",
        )
    else:
        _require(
            CURRENT_EXPECTED_NEXT_PHASE_ID in state["locks"]["deferred_phase_reason"],
            "locks.deferred_phase_reason must mention the exact next phase",
        )
    _check_forbidden_route_claims()
    _require(state["history_summary"]["latest_execution_phase"] == CURRENT_LIVE_PHASE, "unexpected latest execution phase")
    _require(state["history_summary"]["latest_execution_status"] == CURRENT_LIVE_STATUS, "unexpected latest execution status")
    _require(state["history_summary"]["previous_execution_phase"] == CURRENT_LIVE_PREVIOUS_EXECUTION_PHASE, "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == CURRENT_LIVE_LAST_TRANSITION_FROM_PHASE, "unexpected last transition from phase")
    _require(state["last_transition"]["to_phase"] == CURRENT_LIVE_PHASE, "unexpected last transition to phase")
    _require(state["last_transition"]["to_status"] == CURRENT_LIVE_STATUS, "unexpected last transition to_status")
    _require(state["last_transition"]["decision"] == "pass", "unexpected last transition decision")

    # Authorization: fixture_materialization_allowed remains true; all others false.
    auth = state["authorization"]
    for key, value in auth.items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        elif key == "fixture_materialization_allowed":
            _require(value is True, "fixture_materialization_allowed must be true for INF-MAT-01")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _require_files_exist(state)
    _require(INFERNUS_STANDING_AUTHORIZATION_PATH.exists(), "missing INFERNUS_STANDING_AUTHORIZATION.md")

    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "purg01_route_admission_pass",
        "Latest completed phase: `IF-11 Minos Final Verdict + Closure`",
        "latest_completed_status=if11_minos_final_verdict_closure_pass",
        "active_context_remote_main_reflects_if11_minos_final_verdict_closure=true",
        "permanent_active_update_rule_installed=true",
        "PURG-PRE authority execution = true",
        "PURG-00 operator review packet = true",
        "PURG-00 route admission = true",
        "PURG-00 intake authority lock = true",
        "live_route_opened=true",
        "route_amendment_authorized_by_operator=true",
        "operator_source_packet_supplied=true",
        "operator_source_packet_validated=true",
        "operator_source_packet_project_commit_sha=ff9ade875ebf47bad8c4fde0311f576d958c1625",
        "purg01_route_admission_review_status=purg01_route_admission_review_pass",
        "purg01_route_admission_candidate_phase=PURG-01",
        "purg01_route_admission_candidate_phase_class=purgatorium_route_admission",
        "purg01_route_admission_operator_authorized=true",
        "purg01_open_authorized=true",
        "purg01_triage_authorized=true",
        "purg01_triage_readiness_review_status=purg01_triage_readiness_review_pass",
        "purg01_triage_planning_candidate_created=true",
        "purg01_triage_planning_gate_status=purg01_triage_planning_gate_pass",
        "purg01_triage_authorization_gate_status=purg01_triage_authorization_gate_pass",
        "triage_plan_created=true",
        "triage_authorization_request_candidate_created=true",
        "triage_execution_authorized=false",
        "finding_fix_authorized=false",
        "purg01_controlled_triage_execution_gate_status=purg01_controlled_triage_execution_gate_pass",
        "next_route_candidate=execute_purg01_controlled_triage_artifact_only",
        "PURG-00 real execution = false",
        "future waves real execution = false",
        "execute_purg01_controlled_triage_artifact_only",
        "INFERNUS_STANDING_AUTHORIZATION.md",
    )
    _mirror_contains(
        ROOT / "README.md",
        "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET",
        "ACTIVE_CONTEXT_STATE.json",
        "ARIS_BOOT.md",
        "INFERNUS_STANDING_AUTHORIZATION.md",
        "if09_closure_milestone_mirror_sanity_pass",
        "latest_completed_phase: IF09 Closure Milestone Mirror Sanity Packet",
        "next_phase: null",
        "technical_roadmap_post_infernus: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
        "Merge to Project_ARIS main: executed",
        "IF09-FIND-001 closed",
        "BENCHUX_ROUTE_OPENING_PACKET",
        "Todos execution_locks: false",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## PURG04 Track A Main Merge Execution",
        "purg04_track_a_main_merge_execution_pass",
        "7883af5a32c629026bfc6dc15ebee4ebbcadd295",
        "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET",
        "## PURG04 Active-Context Canonical Sync Repair After Track A Main Merge",
        "purg04_active_context_canonical_sync_repair_pass",
        "Project_ARIS changed during this sync repair: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## IF09 Closure Milestone Mirror Sanity Packet",
        "if09_closure_milestone_mirror_sanity_pass",
        "if09_closure_milestone_sanity_packet.json",
        "phase_id=current_phase_id=IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET",
        "BENCHUX_ROUTE_OPENING_PACKET",
        "HISTORICAL_ONLY",
        "SUPERSEDED_BY_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
        "NOT_CURRENT_STATE",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## INF Revalidation Adjudication Or Closure Packet",
        "inf_revalidation_adjudication_closure_pass",
        "inf_revalidation_adjudication_closure_packet.json",
        "phase_id=current_phase_id=INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
        "IF09-FIND-001` closed",
        "`remediation_proven=true`",
        "`finding_closed=true`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## INF Revalidation Execution Packet",
        "inf_revalidation_execution_pass",
        "inf_revalidation_execution_packet.json",
        "inf_revalidation_execution_oracle_result.json",
        "phase_id=current_phase_id=INF_REVALIDATION_EXECUTION_PACKET",
        "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
        "IF09-FIND-001` remains open",
        "`remediation_proven=false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## INF Revalidation Operator Authorization Packet",
        "inf_revalidation_operator_authorization_pass",
        "inf_revalidation_operator_authorization_packet.json",
        "inf_revalidation_execution_contract.json",
        "inf_revalidation_safety_lock_matrix.json",
        "phase_id=current_phase_id=INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET",
        "next_phase=null",
        "active_next_phase=null",
        "INF_REVALIDATION_EXECUTION_PACKET",
        "IF09-FIND-001` remains open",
        "`remediation_proven=false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## INF Revalidation Readiness Route Activation Packet",
        "inf_revalidation_readiness_opened",
        "inf_revalidation_readiness_route_activation_packet.json",
        "inf_revalidation_readiness_packet.json",
        "phase_id=current_phase_id=INF_REVALIDATION_READINESS_PACKET",
        "next_phase=null",
        "active_next_phase=null",
        "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET",
        "IF09-FIND-001` remains open",
        "`remediation_proven=false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## INF Revalidation Route Activation / Amendment Packet",
        "inf_revalidation_route_admission_opened",
        "inf_revalidation_route_activation_packet.json",
        "inf_revalidation_route_admission_packet.json",
        "phase_id=current_phase_id=INF_REVALIDATION_ROUTE_ADMISSION_PACKET",
        "next_phase=null",
        "active_next_phase=null",
        "TRACK_REVALIDATION_FIRST",
        "IF09-FIND-001` remains open",
        "`remediation_proven=false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## PURG Residual Risk Carry-Forward Packet Route Opening",
        "purg_residual_risk_carry_forward_route_opening_pass",
        "purg_residual_risk_carry_forward_route_opening_operator_authorization.json",
        "purg_residual_risk_carry_forward_route_opening_packet.json",
        "phase_id=current_phase_id=PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
        "next_phase=null",
        "active_next_phase=null",
        "IF09-FIND-001` remains open",
        "`remediation_proven=false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "## PURG04 Track A Post-Merge Validation Packet",
        "purg04_track_a_post_merge_validation_packet_pass",
        "purg04_track_a_post_merge_validation_operator_authorization.json",
        "purg04_track_a_post_merge_validation_packet.json",
        NO_TRANSITION_DEFINED_MESSAGE,
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Latest completed phase: IF09 Closure Milestone Mirror Sanity Packet",
        "Active next phase: null",
        "Active next phase class: null",
        "Standing authorization: canonroadmap approved by operator",
        "Post-Infernus technical direction document: `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`",
        "PURG-PRE route opening candidate: `artifacts/purgatorium/purg_pre_route_opening_candidate.json`",
        "Live route terminalized by: `purg00_route_amendment_terminal_wait_state_operator_source_required`",
        "PURG-PRE canonical authority execution verified by: `purg_pre_canonical_authority_execution_pass`",
        "PURG-00 operator review packet prepared by: `purg00_operator_review_packet_pass`",
        "PURG-00 route admitted by: `purg00_route_admission_pass`",
        "PURG-00 handoff intake / authority lock status: `purg00_handoff_intake_authority_lock_blocked`",
        "PURG-00 route amendment terminal wait-state status: `purg00_route_amendment_terminal_wait_state_operator_source_required`",
        "PURG-00 operator source packet intake: `purg00_operator_source_packet_intake_pass`",
        "PURG-01 route admission review: `purg01_route_admission_review_pass`",
        "PURG-01 route admitted by: `purg01_route_admission_pass`",
        "PURG-01 triage readiness review: `purg01_triage_readiness_review_pass`",
        "PURG-01 triage planning gate: `purg01_triage_planning_gate_pass`",
        "PURG-01 triage authorization gate: `purg01_triage_authorization_gate_pass`",
        "PURG-01 controlled triage execution gate: `purg01_controlled_triage_execution_gate_pass`",
        "PURG-00 execution: false",
        "PURG-00 intake executed: true",
        "Future PURG-01 triage readiness: CONTROLLED_EXECUTION_GATE_PASS",
        "PURG-01 triage authorized: true",
        "Operator primary source packet supplied and validated: true",
        "Next non-execution step: `execute_purg01_controlled_triage_artifact_only`",
        "Real execution (waves against real systems, runtime, apply): false",
        "BENCHUX_ROUTE_OPENING_PACKET",
        "W4 post-sync review remains historical and preserved the controlled execution closure with w4_execution_performed=true, execution_scope=synthetic_isolated_lab_only, synthetic_attack_cases_total=14, rollback_honesty_checks=6/6, duplicate_detection_checks=5/5, cost_enforcement_checks=3/3, and RHR=DDR=CER=1.0.",
        "IF10 purgatorium handoff graph remains the canonical source packet for this sync with source_project_sha_verified_by_packet=57106d9780af7a807bd58ea6039af3a7b1b23701, source_active_context_sync_sha_verified_by_packet=7755a1506e6981d3f1c5b3534c7217112a12b960, source_root_manifest_sha256=3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660, source_graph_sha256=c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1, validated_handoff_ids=[IF09-FIND-001], contextual_candidate_ids=[IF09-FIND-002], excluded_invalid_ids=[IF09-FIND-003], and supporting_observation_ids=[IF09-OBS-001].",
        "IF11 minos final verdict closure is canonical as pass; this PURG sync keeps the validated operator source packet from project commit ff9ade875ebf47bad8c4fde0311f576d958c1625 with packet sha256=6f616556d0a31ebba8e0bd647ccfd014f1955127856cc20d2deee2f6d7111e72 and CI_GREEN_CONFIRMED, keeps PURG-01 admitted through route-admission-only authority, records explicit operator authorization for PURG-01 triage using the planning-gate project commit 2bfefac900c6c3e7c3f016b7a790570587e57fbb and active-context commit c8ee8c8225e74ffa8ba56aae916343fcd3d55b0d, records the controlled triage execution gate as pass from the operator packet plus IF10 handoff graph evidence, keeps triage execution unopened, and limits the next move to execute_purg01_controlled_triage_artifact_only without authorizing any real execution surface.",
        "| INF-FULL-05 | pass | INF-FULL-06 | infernus_full_excludent_cleanup | canonroadmap |",
        "| INF-FULL-06 | pass | INF-FULL-07 | infernus_full_execution_authorization | canonroadmap |",
        "| INF-FULL-04 | pass | INF-FULL-05 | infernus_full | canonroadmap |",
        "| INF-FULL-07 | pass | PURG-PRE | purgatorium_full_authority_materialization | operator | purg_pre_route_admission_decision.json + operator review packet + schema/validator admission + no-real-exec attestation |",
        "| PURG-PRE | pass | PURG-00 | purgatorium_full_intake | operator | purg00_route_admission_decision.json + purg00_operator_review_packet + schema/validator admission + no-real-exec attestation |",
        "| PURG-00 | pass | PURG-01 | purgatorium_route_admission | operator | purg01_route_admission_decision.json + operator authorization + no-real-exec attestation + validator evidence |",
        "| INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET | pass | INF_REVALIDATION_EXECUTION_PACKET | infernus_revalidation_execution | operator | inf_revalidation_execution_packet.json + deterministic oracle result + regression matrix + no-forbidden-surface attestation |",
        "| INF_REVALIDATION_EXECUTION_PACKET | pass | INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET | infernus_revalidation_adjudication_or_closure | operator | inf_revalidation_adjudication_closure_packet.json + evidence adjudication matrix + closure decision + no-forbidden-surface carry-forward attestation |",
        "| INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET | pass | IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET | governance_repair | operator | if09_closure_milestone_sanity_packet.json + mirror sanity matrix + benchux route candidate |",
    )
    _mirror_contains(
        ROOT / "EXCLUDENT_POLICY.md",
        "project_mirror/docs/infernus_full/infernus_full_canonroadmap.md",
        "excludent/infernus/roadmaps/infernus_full_canonroadmap.md",
        "project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md",
        "This supersession changes document authority only.",
    )
    _mirror_contains(
        ROOT / "ARIS_BOOT.md",
        "INFERNUS_STANDING_AUTHORIZATION.md",
        "Gate que só reafirma locks do gate anterior: PROIBIDO.",
        "governance_gate_streak",
        "Nunca emita relatório final com CI pendente.",
        "Nenhum PASS é canônico enquanto aris-active-context/main não refletir",
        "Resposta sem SHA no topo = INVALID",
        "PASS só existe: CI terminal green + validator pass + artifact no disco",
    )

    fixture_assertion_path = ROOT / "scripts/assert_no_unauthorized_fixtures.py"
    workflow_path = ROOT / ".github/workflows/validate_active_context.yml"
    _require(fixture_assertion_path.read_text(encoding="utf-8") == EXPECTED_FIXTURE_ASSERTION, "unexpected fixture assertion script content")
    _require(workflow_path.read_text(encoding="utf-8") == EXPECTED_WORKFLOW, "unexpected workflow content")

    _warn_boot_receipt(state)
    from check_boot_sync import assert_boot_in_sync
    assert_boot_in_sync()

    print(json.dumps({
        "decision": EXPECTED_DECISION,
        "status": CURRENT_LIVE_STATUS,
        "phase_id": CURRENT_LIVE_PHASE_ID,
        "previous_phase_id": CURRENT_LIVE_PREVIOUS_PHASE_ID,
        "latest_completed_phase": CURRENT_LIVE_PHASE,
        "latest_completed_status": CURRENT_LIVE_STATUS,
        "next_phase": CURRENT_EXPECTED_NEXT_PHASE_ID,
        "gate_opened_at": state["gate_opened_at"],
        "gate_max_cycles": state["gate_max_cycles"],
        "gate_cycles_used": state["gate_cycles_used"],
        "governance_gate_streak": state.get("governance_gate_streak", 0),
        "phase_class": state.get("phase_class", ""),
        "fixture_count": state.get("fixture_count", 0),
        "scenario_count": state.get("scenario_count", 0),
        "fixture_scenario_count": state.get("fixture_scenario_count", 0),
        "current_phase_planned_scenario_count": state.get("current_phase_planned_scenario_count", 0),
        "current_phase_planned_bot_count": state.get("current_phase_planned_bot_count", 0),
        "current_phase_mutation_family_count": state.get("current_phase_mutation_family_count", 0),
        "current_phase_oracle_count": state.get("current_phase_oracle_count", 0),
        "bot_execution_executed": state.get("bot_execution_executed", False),
        "current_phase_bots_executed": state.get("current_phase_bots_executed", False),
        "bot_execution_log_count": state.get("bot_execution_log_count", 0),
        "minos_verdict_executed": state.get("minos_verdict_executed", False),
        "minos_verdict_count": state.get("minos_verdict_count", 0),
        "uv_lock_exists": (PROJECT_ROOT / "uv.lock").exists(),
        "acb_core_01_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_01" / "decision.json").exists(),
        "acb_core_02_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_02" / "decision.json").exists(),
        "acb_cap_01_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_cap_01" / "decision.json").exists(),
        "acb_cap_05_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_cap_05" / "advanced_supply_chain_decision.json").exists(),
        "inf_full_01_scope_artifacts_exist": INF_FULL_01_SCOPE_DECISION_PATH.exists(),
        "inf_full_03_artifacts_exist": INF_FULL_03_DECISION_PATH.exists(),
        "inf_full_04_artifacts_exist": INF_FULL_04_DECISION_PATH.exists(),
        "inf_full_route_sync_artifacts_exist": INF_FULL_ROUTE_SYNC_DECISION_PATH.exists(),
        "auto_advance_enabled": state["auto_advance"]["enabled"],
        "ci_enforcement_active": True,
        "anti_proliferation_rule_active": True,
        "fixture_materialization_executed": state.get("fixture_materialization_executed", False),
    }, indent=2))


if __name__ == "__main__":
    main()
