#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys
import unicodedata
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PROJECT_MIRROR_ROOT = ROOT / "project_mirror"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"
ROADMAP_PATH = ROOT / "ROADMAP_CANONICAL.md"
BOOT_PATH = ROOT / "BOOT.md"
ARIS_BOOT_PATH = ROOT / "ARIS_BOOT.md"
OPERATOR_PREFERENCES_PATH = ROOT / "OPERATOR_PREFERENCES.md"
PROJECT_CHECKOUT_PRESENT = (PROJECT_ROOT / "main.py").exists() and (PROJECT_ROOT / "artifacts").exists()


def _resolve_project_relative(*parts: str) -> pathlib.Path:
    relative = pathlib.Path(*parts)
    for base in (PROJECT_ROOT, PROJECT_MIRROR_ROOT):
        candidate = base / relative
        if candidate.exists():
            return candidate
    return PROJECT_ROOT / relative

ACB_CORE_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_01_project_evidence_2026_06_03.json"
ACB_CORE_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_02_project_evidence_2026_06_03.json"
ACB_CAP_01_OPERATOR_AUTH_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_operator_authorization_2026_06_03.json"
ACB_CAP_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_project_evidence_2026_06_03.json"
ACB_CAP_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_02_project_evidence_2026_06_03.json"
ACB_CAP_03_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_03_project_evidence_2026_06_03.json"
ACB_CAP_04_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_04_project_evidence_2026_06_03.json"
ACB_CAP_05_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_evidence_2026_06_05.json"
ACB_CAP_05_RESYNC_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_sha_resync_2026_06_06.json"

PURG_PRE_ROOT = ROOT / "artifacts" / "purgatorium"
PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH = PURG_PRE_ROOT / "purg00_route_admission_no_real_execution_attestation_v2.json"
PURG_PRE_ROUTE_ADMISSION_DECISION_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_decision.json"
PURG_PRE_ROUTE_ADMISSION_SUMMARY_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_summary.json"
PURG_PRE_ROUTE_ADMISSION_REPORT_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_report.md"
PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg_pre_route_admission_no_real_execution_attestation.json"
PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_decision.json"
PURG_PRE_AUTHORITY_EXECUTION_SUMMARY_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_summary.json"
PURG_PRE_AUTHORITY_EXECUTION_REPORT_PATH = PURG_PRE_ROOT / "purg_pre_canonical_authority_execution_report.md"
PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH = PURG_PRE_ROOT / "purg_pre_handoff_source_reference_matrix.json"
PURG_PRE_NO_PURG00_ATTESTATION_PATH = PURG_PRE_ROOT / "purg_pre_no_purg00_attestation.json"
PURG_PRE_NO_REAL_EXECUTION_V2_PATH = PURG_PRE_ROOT / "purg_pre_no_real_execution_attestation_v2.json"

PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_decision.json"
PURG00_OPERATOR_REVIEW_PACKET_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_summary.json"
PURG00_OPERATOR_REVIEW_PACKET_REPORT_PATH = PURG_PRE_ROOT / "purg00_operator_review_packet_report.md"
PURG00_NOT_OPENED_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_not_opened_attestation.json"
PURG00_ROUTE_ADMISSION_DECISION_PATH = PURG_PRE_ROOT / "purg00_route_admission_decision.json"
PURG00_ROUTE_ADMISSION_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_route_admission_summary.json"
PURG00_ROUTE_ADMISSION_REPORT_PATH = PURG_PRE_ROOT / "purg00_route_admission_report.md"
PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH = PURG_PRE_ROOT / "purg00_route_admission_no_real_execution_attestation.json"
PURG00_ROUTE_ADMISSION_SCHEMA_GAP_PATH = PURG_PRE_ROOT / "purg00_route_admission_schema_gap_matrix.json"
PURG00_ROUTE_ADMISSION_VALIDATOR_GAP_PATH = PURG_PRE_ROOT / "purg00_route_admission_validator_gap_matrix.json"
PURG00_ROUTE_ADMISSION_FUTURE_PATCH_PLAN_PATH = PURG_PRE_ROOT / "purg00_route_admission_future_patch_plan.md"
PURG00_ROUTE_ADMISSION_SCHEMA_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_schema_patch_manifest.json"
PURG00_ROUTE_ADMISSION_VALIDATOR_PATCH_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_validator_patch_manifest.json"
PURG00_ROUTE_ADMISSION_LIVE_ROUTE_MUTATION_MANIFEST_PATH = PURG_PRE_ROOT / "purg00_route_admission_live_route_mutation_manifest.json"
PURG00_ROUTE_ADMISSION_ROLLBACK_PLAN_PATH = PURG_PRE_ROOT / "purg00_route_admission_rollback_plan.md"
PURG00_HANDOFF_INTAKE_DECISION_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_decision.json"
PURG00_HANDOFF_INTAKE_SUMMARY_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_summary.json"
PURG00_HANDOFF_INTAKE_REPORT_PATH = PURG_PRE_ROOT / "purg00_handoff_intake_authority_lock_report.md"
PURG00_DATA_GAP_MATRIX_PATH = PURG_PRE_ROOT / "purg00_data_gap_matrix.json"
PURG00_NO_FIX_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_no_fix_attestation.json"
PURG00_REQUIRED_SOURCE_ACCESS_MATRIX_PATH = PURG_PRE_ROOT / "purg00_required_source_access_matrix.json"
PURG00_SOURCE_PACKET_INDEX_PATH = PURG_PRE_ROOT / "purg00_source_packet_index.json"
PURG00_HANDOFF_ID_CLASSIFICATION_MATRIX_PATH = PURG_PRE_ROOT / "purg00_handoff_id_classification_matrix.json"
PURG00_SOURCE_HASH_VERIFICATION_MATRIX_PATH = PURG_PRE_ROOT / "purg00_source_hash_verification_matrix.json"
PURG00_NO_REAL_EXECUTION_ATTESTATION_PATH = PURG_PRE_ROOT / "purg00_no_real_execution_attestation.json"

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

LAPIDARIUM_TERMINAL_PHASE_ID = "LAPIDARIUM_FASE_2_ARQUITETURA_ALVO_TRUE"
LAPIDARIUM_GUARD_PHASE_ID = "LAPIDARIUM_FASE_6_GUARDA_TRUE"

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

LEGACY_TRANSITION_ROWS: dict[tuple[str, str], dict[str, Any]] = {
    ("INF-FULL-04", "pass"): {
        "current_phase_id": "INF-FULL-04",
        "decision": "pass",
        "next_phase_id": "INF-FULL-05",
        "next_phase_class": "infernus_full",
        "advance_mode": "canonroadmap",
        "minimum_deliverable": "if07 pre-execution review decision artifact + no bot/runtime execution attestation + scenario-count normalization evidence + validator evidence",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF-FULL-05"],
        "next_phase_raw": "INF-FULL-05",
    },
    ("INF-FULL-07", "pass"): {
        "current_phase_id": "INF-FULL-07",
        "decision": "pass",
        "next_phase_id": "PURG-PRE",
        "next_phase_class": "purgatorium_full_authority_materialization",
        "advance_mode": "operator",
        "minimum_deliverable": "purg_pre_route_admission_decision.json + operator review packet + schema/validator admission + no-real-exec attestation",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["PURG-PRE"],
        "next_phase_raw": "PURG-PRE",
    },
    ("PURG-PRE", "pass"): {
        "current_phase_id": "PURG-PRE",
        "decision": "pass",
        "next_phase_id": "PURG-00",
        "next_phase_class": "purgatorium_full_intake",
        "advance_mode": "operator",
        "minimum_deliverable": "purg00_route_admission_decision.json + purg00_operator_review_packet + schema/validator admission + no-real-exec attestation",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["PURG-00"],
        "next_phase_raw": "PURG-00",
    },
    ("PURG04_TRACK_A_MAIN_MERGE_EXECUTION", "pass"): {
        "current_phase_id": "PURG04_TRACK_A_MAIN_MERGE_EXECUTION",
        "decision": "pass",
        "next_phase_id": "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET",
        "next_phase_class": "purgatorium_post_merge_validation",
        "advance_mode": "operator",
        "minimum_deliverable": "purg04_track_a_post_merge_validation_packet.json + CI green or explicit CI confirmation artifact",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET"],
        "next_phase_raw": "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET",
    },
    ("PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET", "pass"): {
        "current_phase_id": "PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET",
        "decision": "pass",
        "next_phase_id": "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
        "next_phase_class": "purgatorium_route_admission",
        "advance_mode": "operator",
        "minimum_deliverable": "purg_residual_risk_carry_forward_route_opening_packet.json + route-opening operator authorization + validator evidence",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET"],
        "next_phase_raw": "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
    },
    ("PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET", "pass"): {
        "current_phase_id": "PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET",
        "decision": "pass",
        "next_phase_id": "INF_REVALIDATION_ROUTE_ADMISSION_PACKET",
        "next_phase_class": "infernus_revalidation_route_admission",
        "advance_mode": "operator",
        "minimum_deliverable": "inf_revalidation_route_admission_packet.json + required inputs + scope matrix + forbidden actions + next candidate",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF_REVALIDATION_ROUTE_ADMISSION_PACKET"],
        "next_phase_raw": "INF_REVALIDATION_ROUTE_ADMISSION_PACKET",
    },
    ("INF_REVALIDATION_ROUTE_ADMISSION_PACKET", "pass"): {
        "current_phase_id": "INF_REVALIDATION_ROUTE_ADMISSION_PACKET",
        "decision": "pass",
        "next_phase_id": "INF_REVALIDATION_READINESS_PACKET",
        "next_phase_class": "infernus_revalidation_readiness",
        "advance_mode": "operator",
        "minimum_deliverable": "inf_revalidation_readiness_packet.json + scenario scope + oracle contract + abort criteria + no-real-execution attestation",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF_REVALIDATION_READINESS_PACKET"],
        "next_phase_raw": "INF_REVALIDATION_READINESS_PACKET",
    },
    ("INF_REVALIDATION_READINESS_PACKET", "pass"): {
        "current_phase_id": "INF_REVALIDATION_READINESS_PACKET",
        "decision": "pass",
        "next_phase_id": "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET",
        "next_phase_class": "infernus_revalidation_operator_authorization",
        "advance_mode": "operator",
        "minimum_deliverable": "inf_revalidation_operator_authorization_packet.json + execution contract + safety lock matrix",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET"],
        "next_phase_raw": "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET",
    },
    ("INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET", "pass"): {
        "current_phase_id": "INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET",
        "decision": "pass",
        "next_phase_id": "INF_REVALIDATION_EXECUTION_PACKET",
        "next_phase_class": "infernus_revalidation_execution",
        "advance_mode": "operator",
        "minimum_deliverable": "inf_revalidation_execution_packet.json + deterministic oracle result + regression matrix + no-forbidden-surface attestation",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF_REVALIDATION_EXECUTION_PACKET"],
        "next_phase_raw": "INF_REVALIDATION_EXECUTION_PACKET",
    },
    ("INF_REVALIDATION_EXECUTION_PACKET", "pass"): {
        "current_phase_id": "INF_REVALIDATION_EXECUTION_PACKET",
        "decision": "pass",
        "next_phase_id": "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
        "next_phase_class": "infernus_revalidation_adjudication_or_closure",
        "advance_mode": "operator",
        "minimum_deliverable": "inf_revalidation_adjudication_closure_packet.json + evidence adjudication matrix + closure decision + no-forbidden-surface carry-forward attestation",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET"],
        "next_phase_raw": "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
    },
    ("INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET", "pass"): {
        "current_phase_id": "INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET",
        "decision": "pass",
        "next_phase_id": "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET",
        "next_phase_class": "governance_repair",
        "advance_mode": "operator",
        "minimum_deliverable": "if09_closure_milestone_sanity_packet.json + mirror sanity matrix + benchuix route candidate",
        "next_phase_requires_operator_decision": False,
        "next_phase_candidates": ["IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET"],
        "next_phase_raw": "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET",
    },
}

PROJECT_PHASE_DELIVERABLES = {
    "INF-MAT-01": lambda: (
        pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full").exists()
        and len(list(pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full").iterdir())) >= 13
    ),
    "INF-BOT-01": lambda: (
        pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json").exists()
        and bool(_load_json(pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json")).get("log_sha256"))
    ),
    "INF-MINOS-01": lambda: (
        pathlib.Path("artifacts/inf_minos_01/minos_verdict.json").exists()
        and bool(_load_json(pathlib.Path("artifacts/inf_minos_01/minos_verdict.json")).get("minos_verdict_sha256"))
    ),
    "PURG-01": lambda: (
        pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").exists()
        and bool(_load_json(pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json")).get("severity"))
        and bool(_load_json(pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json")).get("status"))
    ),
    "ACB-CORE-01": lambda: (
        ACB_CORE_01_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CORE_01_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CORE_01_EVIDENCE_PATH).get("supply_chain_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CORE_01_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in ["uv_lock_exists", "pip_audit_gate_exists", "sbom_exists", "uv_bootstrap_exists"]
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
}


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


_live = _load_json(STATE_PATH)
CURRENT_LIVE_PHASE_ID = _live.get("phase_id")
CURRENT_LIVE_PREVIOUS_PHASE_ID = _live.get("previous_phase_id")
CURRENT_LIVE_PHASE = _live.get("latest_completed_phase")
CURRENT_LIVE_STATUS = _live.get("status")
CURRENT_LIVE_CURRENT_STATUS = _live.get("current_status")
CURRENT_LIVE_SCHEMA_VERSION = _live.get("schema_version")
CURRENT_LIVE_NEXT_RECOMMENDED_STEP = _live.get("latest_completed_next_recommended_step")
CURRENT_LIVE_LATEST_COMPLETED_PROJECT_SHA = _live.get("latest_completed_project_commit_sha")
CURRENT_LIVE_LATEST_COMPLETED_CI_STATE = _live.get("latest_completed_ci_state")
CURRENT_LIVE_PREVIOUS_EXECUTION_PHASE = (_live.get("history_summary") or {}).get("previous_execution_phase")
CURRENT_LIVE_LAST_TRANSITION_FROM_PHASE = (_live.get("last_transition") or {}).get("from_phase")
CURRENT_LIVE_PHASE_CLASS = _live.get("phase_class")
CURRENT_EXPECTED_NEXT_PHASE_ID = _live.get("active_next_phase")
CURRENT_EXPECTED_NEXT_PHASE_CLASS = _live.get("active_next_phase_class")


def _require(condition: bool, message: str) -> None:
    if not condition:
        print(f"BLOCK: {message}")
        raise SystemExit(1)


def _slugify_phase_token(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", normalized).strip("_").lower()
    return slug


def _type_matches(instance: Any, expected: str) -> bool:
    if expected == "null":
        return instance is None
    if expected == "string":
        return isinstance(instance, str)
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "object":
        return isinstance(instance, dict)
    return True


def _validate_schema_node(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    base_schema = {key: value for key, value in schema.items() if key != "oneOf"}

    schema_type = base_schema.get("type")
    types = schema_type if isinstance(schema_type, list) else ([schema_type] if isinstance(schema_type, str) else [])
    if types and not any(_type_matches(instance, expected) for expected in types):
        errors.append(f"{path}: expected type {types}, got {type(instance).__name__}")
        return errors

    if "const" in base_schema and instance != base_schema["const"]:
        errors.append(f"{path}: expected const {base_schema['const']!r}, got {instance!r}")
    if "enum" in base_schema and instance not in base_schema["enum"]:
        errors.append(f"{path}: expected one of {base_schema['enum']!r}, got {instance!r}")
    if "pattern" in base_schema and isinstance(instance, str) and re.search(base_schema["pattern"], instance) is None:
        errors.append(f"{path}: string does not match pattern {base_schema['pattern']!r}")

    if isinstance(instance, dict):
        properties = base_schema.get("properties", {})
        required = base_schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        if base_schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")
        for key, child_schema in properties.items():
            if key in instance:
                errors.extend(_validate_schema_node(instance[key], child_schema, f"{path}.{key}"))
    elif isinstance(instance, list):
        if "minItems" in base_schema and len(instance) < base_schema["minItems"]:
            errors.append(f"{path}: expected at least {base_schema['minItems']} items")
        items_schema = base_schema.get("items")
        if isinstance(items_schema, dict):
            for index, value in enumerate(instance):
                errors.extend(_validate_schema_node(value, items_schema, f"{path}[{index}]"))

    if "oneOf" in schema:
        matches = 0
        sub_errors: list[str] = []
        for option in schema["oneOf"]:
            option_errors = _validate_schema_node(instance, option, path)
            if not option_errors:
                matches += 1
            else:
                sub_errors.extend(option_errors)
        if matches != 1:
            errors.append(f"{path}: oneOf expected exactly 1 match, got {matches}")
            if sub_errors:
                errors.extend(sub_errors[:3])
    return errors


def validate_schema(state: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    return _validate_schema_node(state, schema)


def _parse_roadmap_phase_blocks(roadmap_text: str | None = None) -> list[dict[str, Any]]:
    text = roadmap_text if roadmap_text is not None else ROADMAP_PATH.read_text(encoding="utf-8")
    blocks: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    header_re = re.compile(r"^##\s+(?P<ordinal>\d+)\.\s+(?P<title>.+?)\s*$")

    for line in text.splitlines():
        heading_match = header_re.match(line)
        if heading_match:
            if current is not None:
                blocks.append(current)
            current = {
                "heading": line.strip(),
                "ordinal": heading_match.group("ordinal"),
                "title": heading_match.group("title").strip(),
                "phase_id": "",
                "status": "",
                "resultado_final_esperado": "",
                "next_phase": "",
            }
            continue
        if current is None:
            continue
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.lower().startswith("phase_id:"):
            current["phase_id"] = stripped.split(":", 1)[1].strip()
        elif stripped.lower().startswith("status:"):
            current["status"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Resultado final esperado:"):
            current["resultado_final_esperado"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Próxima fase:") or stripped.startswith("Pr[oó]xima fase:"):
            current["next_phase"] = stripped.split(":", 1)[1].strip()
    if current is not None:
        blocks.append(current)
    return blocks


def _parse_roadmap_sections(text: str) -> list[dict[str, Any]]:
    return _parse_roadmap_phase_blocks(text)


def _find_roadmap_phase_block(phase_identifier: str, *, roadmap_text: str | None = None) -> dict[str, Any] | None:
    if not phase_identifier:
        return None
    needle = phase_identifier.strip()
    needle_slug = _slugify_phase_token(needle)
    for block in _parse_roadmap_phase_blocks(roadmap_text):
        candidates = [block.get("phase_id", ""), block.get("title", ""), block.get("heading", "")]
        if needle in candidates:
            return block
        if needle_slug and any(_slugify_phase_token(candidate) == needle_slug for candidate in candidates if candidate):
            return block
    return None


def _parse_next_phase_spec(next_phase_text: str) -> dict[str, Any]:
    text = next_phase_text.strip()
    conditional_match = re.match(
        r"^se\s+(?P<condition>.+?)\s*(?:→|->)\s*(?P<then>.+?)\s*(?:;|,)?\s*sen[ãa]o\s*(?:→|->)\s*(?P<else>.+?)\s*$",
        text,
        re.IGNORECASE,
    )
    if conditional_match:
        then_candidate = conditional_match.group("then").strip()
        else_candidate = conditional_match.group("else").strip()
        return {
            "next_phase_raw": text,
            "next_phase_id": None,
            "next_phase_candidates": [then_candidate, else_candidate],
            "next_phase_requires_operator_decision": True,
            "condition": conditional_match.group("condition").strip(),
            "next_phase_class": None,
            "next_phase_candidate_classes": [_slugify_phase_token(then_candidate), _slugify_phase_token(else_candidate)],
        }
    return {
        "next_phase_raw": text,
        "next_phase_id": text or None,
        "next_phase_candidates": [text] if text else [],
        "next_phase_requires_operator_decision": False,
        "condition": None,
        "next_phase_class": _slugify_phase_token(text) if text else None,
        "next_phase_candidate_classes": [_slugify_phase_token(text)] if text else [],
    }


def _roadmap_transition_row_for_block(block: dict[str, Any], decision: str) -> dict[str, Any]:
    parsed_next_phase = _parse_next_phase_spec(block.get("next_phase", ""))
    next_phase_id = parsed_next_phase["next_phase_id"]
    return {
        "current_phase_id": block.get("phase_id") or block.get("title") or block.get("heading") or "",
        "decision": decision,
        "next_phase_id": next_phase_id,
        "next_phase_class": parsed_next_phase["next_phase_class"],
        "advance_mode": "prompt_only" if next_phase_id else "operator",
        "minimum_deliverable": block.get("resultado_final_esperado", ""),
        "next_phase_requires_operator_decision": parsed_next_phase["next_phase_requires_operator_decision"],
        "next_phase_candidates": parsed_next_phase["next_phase_candidates"],
        "next_phase_raw": parsed_next_phase["next_phase_raw"],
    }


def _parse_transition_table() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for block in _parse_roadmap_phase_blocks():
        if block.get("phase_id"):
            rows.append(_roadmap_transition_row_for_block(block, "pass"))
    rows.extend(LEGACY_TRANSITION_ROWS.values())
    return rows


def _get_transition_row(current_phase_id: str, decision: str) -> dict[str, Any] | None:
    for row in _parse_transition_table():
        if row["current_phase_id"] == current_phase_id and row["decision"] == decision:
            return row
    return None


def validate_fsm_proxy(state: dict[str, Any], roadmap_text: str) -> list[str]:
    errors: list[str] = []
    sections = _parse_roadmap_phase_blocks(roadmap_text)
    by_phase_id = [section for section in sections if section["phase_id"]]
    current_phase_id = state.get("current_phase_id")
    current_matches = [section for section in by_phase_id if section["phase_id"] == current_phase_id]

    if len(current_matches) != 1:
        errors.append(
            f"FSM_PROXY #2: expected exactly one roadmap section for current_phase_id={current_phase_id!r}, got {len(current_matches)}"
        )
        return errors

    sections_by_phase = {section["phase_id"]: section for section in by_phase_id}
    current_section = current_matches[0]
    target_phase = current_section["next_phase"]
    target_section = sections_by_phase.get(target_phase)
    if target_phase and target_section and target_section["status"] != "CLOSED":
        if state.get("next_phase") == target_phase:
            return errors
        cursor = state.get("roadmap_cursor") or {}
        if (
            cursor.get("state") == "CANDIDATE"
            and cursor.get("phase_id") == target_phase
            and cursor.get("authorized_by") is None
            and state.get("next_phase") is None
        ):
            return errors
        errors.append(
            "FSM_PROXY #2: "
            f"current_phase_id={current_phase_id!r} has roadmap next_phase={target_phase!r}, "
            "but ACTIVE_CONTEXT_STATE.json next_phase is null without candidate cursor justification"
        )
    if target_phase and target_section and target_section["status"] == "CLOSED":
        errors.append(
            f"FSM_PROXY #1: current section {current_phase_id!r} points next_phase={target_phase!r} to CLOSED phase"
        )
    return errors


def validate_boot_freshness(state: dict[str, Any], boot_text: str | None = None) -> list[str]:
    if boot_text is None:
        if not BOOT_PATH.exists():
            return ["FRESHNESS: BOOT.md is missing"]
        boot_text = BOOT_PATH.read_text(encoding="utf-8")
    match = re.search(r"state_sha:\s*`([0-9a-f]{12})`", boot_text)
    if not match:
        return ["FRESHNESS: BOOT.md does not expose state_sha"]
    state_sha = hashlib.sha256(STATE_PATH.read_bytes()).hexdigest()[:12]
    if match.group(1) != state_sha:
        return [f"FRESHNESS: BOOT.md state_sha={match.group(1)} does not match current state_sha={state_sha}"]
    return []


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


def _check_minimum_deliverable(state: dict[str, Any]) -> None:
    phase_id = state.get("current_phase_id", "")
    decision = state.get("decision", "")
    if decision != "pass" or phase_id not in PROJECT_PHASE_DELIVERABLES:
        return
    if not PROJECT_PHASE_DELIVERABLES[phase_id]():
        print(f"BLOCK: {phase_id} declared pass but minimum_deliverable not met")
        raise SystemExit(1)


def _warn_boot_receipt(state: dict[str, Any]) -> None:
    _require(ARIS_BOOT_PATH.exists(), "ARIS_BOOT.md ausente da raiz")

    boot_files = state.get("last_boot_files_read", [])
    if len(boot_files) < 2 or boot_files[0] != "ACTIVE_CONTEXT_STATE.json" or boot_files[1] != "ARIS_BOOT.md":
        print(f"BLOCK: boot order incorreto em last_boot_files_read: {boot_files[:2]}")
        print("Expected: ['ACTIVE_CONTEXT_STATE.json', 'ARIS_BOOT.md']")
        raise SystemExit(1)

    for fname in BOOT_FILE_SUPERSEDED:
        if (ROOT / fname).exists():
            print(f"WARN: Arquivo superseded ainda presente na raiz: {fname}. Mover para o arquivo arquivado.")


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
        if status in pending_statuses or status != "completed":
            return "CI_PENDING"
        if conclusion in failed_conclusions or conclusion != "success":
            return "CI_FAILED"
    return "CI_GREEN_CONFIRMED"


def _check_if09_evidence_bundle_vulnerability_register_artifacts(state: dict[str, Any]) -> None:
    required_paths = [
        IF09_ACTIVE_DECISION_PATH,
        IF09_ACTIVE_SUMMARY_PATH,
        IF09_ACTIVE_REPORT_PATH,
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
    ]
    if not all(path.exists() for path in required_paths):
        return

    decision = _load_json(IF09_ACTIVE_DECISION_PATH)
    _require(decision.get("phase_id") == "IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET" or decision.get("phase_id") == "IF-09 Evidence Bundle + Vulnerability Register", "if09 decision phase_id mismatch")


def _check_if10_purgatorium_handoff_graph_artifacts(state: dict[str, Any]) -> None:
    required_paths = [
        IF10_ACTIVE_DECISION_PATH,
        IF10_ACTIVE_SUMMARY_PATH,
        IF10_ACTIVE_REPORT_PATH,
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
    ]
    if not all(path.exists() for path in required_paths):
        return

    decision = _load_json(IF10_ACTIVE_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-10 Purgatorium Handoff Graph" or decision.get("phase_id") == "IF10_Purgatorium_Handoff_Graph", "if10 decision phase_id mismatch")


def _check_if11_minos_final_verdict_closure_artifacts(state: dict[str, Any]) -> None:
    required_paths = [
        IF11_ACTIVE_DECISION_PATH,
        IF11_ACTIVE_SUMMARY_PATH,
        IF11_ACTIVE_REPORT_PATH,
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
    ]
    if not all(path.exists() for path in required_paths):
        return

    decision = _load_json(IF11_ACTIVE_DECISION_PATH)
    _require(decision.get("phase_id") == "IF-11 Minos Final Verdict + Closure" or decision.get("phase_id") == "IF11_Minos_Final_Verdict_Closure", "if11 decision phase_id mismatch")


def _check_purg_pre_canonical_authority_materialization_artifacts(state: dict[str, Any]) -> None:
    _require((ROOT / "project_mirror" / "docs" / "purgatorium_full" / "purgatorium_roadmapcanon.md").exists(), "purgatorium roadmapcanon missing")
    _require((ROOT / "excludent" / "infernus" / "roadmaps" / "infernus_full_canonroadmap.md").exists(), "infernus forensic copy missing")


def _check_purg_operator_review_packet_artifacts(state: dict[str, Any]) -> None:
    _require((ROOT / "artifacts" / "purgatorium" / "purg_operator_review_packet_decision.json").exists(), "purg operator review decision missing")
    _require((ROOT / "artifacts" / "purgatorium" / "purg_route_admission_schema_gap_matrix.json").exists(), "purg route admission schema gap matrix missing")
    _require((ROOT / "artifacts" / "purgatorium" / "purg_route_admission_validator_gap_matrix.json").exists(), "purg route admission validator gap matrix missing")
    decision = _load_json(ROOT / "artifacts" / "purgatorium" / "purg_operator_review_packet_decision.json")
    _require(decision.get("decision") == "pass", "purg operator review packet decision mismatch")
    _require(decision.get("live_route_opened") is False, "purg operator review packet must not open live route")
    _require(decision.get("candidate_promoted", False) is False, "purg operator review packet must not promote candidate")
    _require(decision.get("invalid_finding_remediated", False) is False, "purg operator review packet must not remediate finding")


def _check_purg_pre_route_admission_artifacts(state: dict[str, Any]) -> None:
    _require(PURG_PRE_ROUTE_ADMISSION_DECISION_PATH.exists(), "purg_pre_route_admission decision missing")
    _require(PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH.exists(), "purg_pre_route_admission no-real attestation missing")
    decision = _load_json(PURG_PRE_ROUTE_ADMISSION_DECISION_PATH)
    attestation = _load_json(PURG_PRE_ROUTE_ADMISSION_NO_REAL_EXECUTION_PATH)
    _require(decision.get("decision") == "pass", "purg_pre_route_admission decision must be pass")
    _require(decision.get("runtime_executed") is False, "purg_pre_route_admission must not execute runtime")
    _require(decision.get("real_apply_executed") is False, "purg_pre_route_admission must not real-apply")
    _require(decision.get("bedrock_ready") is False, "purg_pre_route_admission must not be bedrock-ready")
    _require(decision.get("product_ready") is False, "purg_pre_route_admission must not be product-ready")
    _require(decision.get("candidate_promoted", False) is False, "purg_pre_route_admission must not promote candidate")
    _require(decision.get("invalid_finding_remediated", False) is False, "purg_pre_route_admission must not remediate finding")
    _require(attestation.get("status") == "purg_pre_route_admission_pass", "purg_pre_route_admission no-real status mismatch")
    _require(attestation.get("bedrock_ready") is False, "purg_pre_route_admission no-real attestation bedrock_ready must remain false")
    _require(attestation.get("product_ready") is False, "purg_pre_route_admission no-real attestation product_ready must remain false")
    _require(attestation.get("runtime_executed") is False, "purg_pre_route_admission no-real attestation runtime_executed must remain false")
    _require(attestation.get("real_apply_executed") is False, "purg_pre_route_admission no-real attestation real_apply_executed must remain false")
    for key in ("runtime_executed", "real_apply_executed", "product_bedrock_real_apply_secrets_executed", "external_network_used_except_github_governance", "dependency_or_package_manager_used", "mcp_activated", "rag_ingestion_executed", "memory_write_executed", "socket_opened", "shell_executed", "filesystem_escape_performed", "real_cost_spent", "real_quota_consumed", "real_audio_capture_allowed", "real_stt_tts_allowed", "microphone_access_allowed", "voice_clone_or_impersonation_allowed"):
        _require(attestation.get(key) is False, f"purg_pre_route_admission no-real attestation {key} must remain false")
    report_text = PURG_PRE_ROUTE_ADMISSION_REPORT_PATH.read_text(encoding="utf-8") if PURG_PRE_ROUTE_ADMISSION_REPORT_PATH.exists() else ""
    _require("PURG-00 | pass" not in report_text, "purg_pre_route_admission report must not claim PURG-00 pass")


def _check_purg_pre_authority_execution_artifacts(state: dict[str, Any]) -> None:
    _require(PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH.exists(), "purg_pre_authority_execution decision missing")
    _require(PURG_PRE_NO_PURG00_ATTESTATION_PATH.exists(), "purg_pre no-purg00 attestation missing")
    _require(PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH.exists(), "purg_pre handoff source reference matrix missing")
    decision = _load_json(PURG_PRE_AUTHORITY_EXECUTION_DECISION_PATH)
    no_purg00 = _load_json(PURG_PRE_NO_PURG00_ATTESTATION_PATH)
    matrix = _load_json(PURG_PRE_HANDOFF_SOURCE_REFERENCE_MATRIX_PATH)
    _require(decision.get("decision") == "pass", "purg_pre authority execution decision must be pass")
    _require(decision.get("purg_pre_executed") is True, "purg_pre authority execution must record execution")
    _require(decision.get("purg_00_opened") is False, "purg_pre authority execution must not open PURG-00")
    _require(decision.get("candidate_promoted") is False, "purg_pre authority execution must not promote candidate")
    _require(decision.get("invalid_finding_remediated") is False, "purg_pre authority execution must not remediate finding")
    _require(no_purg00.get("purg_00_opened") is False, "purg_pre no-purg00 attestation must remain false")
    _require(no_purg00.get("purg_00_pass_declared") is False, "purg_pre no-purg00 attestation must remain false")
    _require(no_purg00.get("finding_fix_executed") is False, "purg_pre no-purg00 attestation must remain false")
    _require(no_purg00.get("candidate_promoted") is False, "purg_pre no-purg00 attestation must remain false")
    _require(no_purg00.get("invalid_finding_remediated") is False, "purg_pre no-purg00 attestation must remain false")
    _require(matrix.get("if09_references_verified") is True, "purg_pre handoff matrix must verify IF09 references")
    _require(matrix.get("if10_references_verified") is True, "purg_pre handoff matrix must verify IF10 references")
    _require(matrix.get("if11_references_verified") is True, "purg_pre handoff matrix must verify IF11 references")
    _require(matrix.get("candidate_promoted") is False, "purg_pre handoff matrix must not promote candidate")
    _require(matrix.get("invalid_finding_remediated") is False, "purg_pre handoff matrix must not remediate finding")


def _check_purg00_operator_review_packet_artifacts(state: dict[str, Any]) -> None:
    _require(PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH.exists(), "purg00 operator review decision missing")
    _require(PURG00_NOT_OPENED_ATTESTATION_PATH.exists(), "purg00 not-opened attestation missing")
    decision = _load_json(PURG00_OPERATOR_REVIEW_PACKET_DECISION_PATH)
    attestation = _load_json(PURG00_NOT_OPENED_ATTESTATION_PATH)
    _require(decision.get("decision") == "pass", "purg00 operator review decision must be pass")
    _require(decision.get("purg00_opened") is False, "purg00 operator review packet must not open PURG-00")
    _require(decision.get("purg00_executed") is False, "purg00 operator review packet must not execute PURG-00")
    _require(decision.get("candidate_promoted") is False, "purg00 operator review packet must not promote candidate")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 operator review packet must not remediate finding")
    _require(attestation.get("purg00_opened") is False, "purg00 not-opened attestation must remain false")
    _require(attestation.get("purg00_executed") is False, "purg00 not-opened attestation must remain false")
    _require(attestation.get("purg00_pass_declared") is False, "purg00 not-opened attestation must remain false")
    _require(attestation.get("candidate_promoted") is False, "purg00 not-opened attestation must remain false")
    _require(attestation.get("invalid_finding_remediated") is False, "purg00 not-opened attestation must remain false")


def _check_purg00_route_admission_artifacts(state: dict[str, Any]) -> None:
    _require(PURG00_ROUTE_ADMISSION_DECISION_PATH.exists(), "purg00 route admission decision missing")
    _require(PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH.exists(), "purg00 route admission no-real v2 attestation missing")
    decision = _load_json(PURG00_ROUTE_ADMISSION_DECISION_PATH)
    attestation = _load_json(PURG00_ROUTE_ADMISSION_NO_REAL_EXECUTION_V2_PATH)
    _require(decision.get("decision") == "pass", "purg00 route admission decision must be pass")
    _require(decision.get("purg00_executed") is False, "purg00 route admission must not execute PURG-00")
    _require(decision.get("purg00_intake_executed") is False, "purg00 route admission must not execute intake")
    _require(decision.get("candidate_promoted") is False, "purg00 route admission must not promote candidate")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 route admission must not remediate finding")
    _require(attestation.get("purg00_intake_executed") is False, "purg00 route admission no-real v2 must not execute intake")
    _require(attestation.get("bedrock_ready") is False, "purg00 route admission no-real v2 must not be bedrock-ready")
    _require(attestation.get("product_ready") is False, "purg00 route admission no-real v2 must not be product-ready")
    _require(attestation.get("runtime_executed") is False, "purg00 route admission no-real v2 must not execute runtime")
    _require(attestation.get("real_apply_executed") is False, "purg00 route admission no-real v2 must not real-apply")
    if "candidate_promoted" in attestation:
        _require(attestation.get("candidate_promoted") is False, "purg00 route admission no-real v2 must not promote candidate")
    if "invalid_finding_remediated" in attestation:
        _require(attestation.get("invalid_finding_remediated") is False, "purg00 route admission no-real v2 must not remediate finding")


def _check_purg00_handoff_intake_authority_lock_artifacts(state: dict[str, Any]) -> None:
    _require(PURG00_HANDOFF_INTAKE_DECISION_PATH.exists(), "purg00 handoff intake decision missing")
    _require(PURG00_DATA_GAP_MATRIX_PATH.exists(), "purg00 data gap matrix missing")
    _require(PURG00_NO_FIX_ATTESTATION_PATH.exists(), "purg00 no-fix attestation missing")
    decision = _load_json(PURG00_HANDOFF_INTAKE_DECISION_PATH)
    no_fix = _load_json(PURG00_NO_FIX_ATTESTATION_PATH)
    data_gap = _load_json(PURG00_DATA_GAP_MATRIX_PATH)
    _require(decision.get("decision") == "blocked", "purg00 handoff intake must remain blocked")
    _require(decision.get("purg00_intake_executed") is True, "purg00 handoff intake must record intake execution")
    _require(decision.get("authority_lock_created") is True, "purg00 handoff intake must create authority lock")
    _require(decision.get("finding_fix_executed") is False, "purg00 handoff intake must not execute a finding fix")
    _require(decision.get("red_reproduction_executed") is False, "purg00 handoff intake must not execute red reproduction")
    _require(decision.get("triage_executed") is False, "purg00 handoff intake must not execute triage")
    _require(decision.get("candidate_promoted") is False, "purg00 handoff intake must not promote candidate")
    _require(decision.get("invalid_finding_remediated") is False, "purg00 handoff intake must not remediate finding")
    _require(no_fix.get("finding_fix_executed") is False, "purg00 no-fix attestation must remain false")
    _require(no_fix.get("red_reproduction_executed") is False, "purg00 no-fix attestation must remain false")
    _require(no_fix.get("triage_executed") is False, "purg00 no-fix attestation must remain false")
    _require(no_fix.get("candidate_promoted") is False, "purg00 no-fix attestation must remain false")
    _require(no_fix.get("invalid_finding_remediated") is False, "purg00 no-fix attestation must remain false")
    _require(data_gap.get("purg00_decision") == "blocked", "purg00 data gap matrix decision mismatch")
    _require(data_gap.get("graph_full_detail_accessible") is False, "purg00 data gap matrix must preserve blocked graph detail access")


def run_checks() -> dict[str, Any]:
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")

    errors = []
    errors.extend(validate_schema(state, schema))
    errors.extend(validate_fsm_proxy(state, roadmap))
    errors.extend(validate_boot_freshness(state))

    return {
        "status": "pass" if not errors else "fail",
        "phase_id": state.get("current_phase_id"),
        "next_phase": state.get("next_phase"),
        "roadmap_cursor": state.get("roadmap_cursor"),
        "schema_version": state.get("schema_version"),
        "state_sha": hashlib.sha256(STATE_PATH.read_bytes()).hexdigest(),
        "errors": errors,
    }


def main() -> int:
    result = run_checks()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
