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
OPERATOR_PREFERENCES_PATH = ROOT / "OPERATOR_PREFERENCES.md"

EXPECTED_PHASE = "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution"
EXPECTED_PHASE_ID = "INF-FULL-07"
EXPECTED_PREVIOUS_PHASE = "IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness"
EXPECTED_PREVIOUS_PHASE_ID = "INF-FULL-06"
EXPECTED_STATUS = "inf_full_07_if08_authorization_gate_pass"
EXPECTED_DECISION = "pass"
EXPECTED_CURRENT_STATUS = "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass"
EXPECTED_SCHEMA_VERSION = "2.13"
EXPECTED_NEXT_PHASE_ID = "IF-08"
EXPECTED_NEXT_PHASE_CLASS = "infernus_full_execution"
EXPECTED_NEXT_ACTION_STATUS = "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass"
EXPECTED_LATEST_COMPLETED_STATUS = "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass"
EXPECTED_LATEST_COMPLETED_PROJECT_SHA = "c65888a2f587c35b4e38b16b50b917233bac8fa3"
EXPECTED_LATEST_COMPLETED_CI_STATE = "CI_GREEN_CONFIRMED"
EXPECTED_NEXT_RECOMMENDED_STEP = "post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution"
EXPECTED_PROJECT_CI_RUN_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27156460042"
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
IF08_W05_CONTROLLED_PROJECT_SHA = "9ad30a803ffe2227551bdbe2856633eef1165047"
IF08_W05_CONTROLLED_CI_STATE = "CI_GREEN_CONFIRMED"
IF08_W05_CONTROLLED_NEXT_RECOMMENDED_STEP = "defer_next_if08_wave_prompt_until_post_sync_review"
IF08_W05_RERUN_PHASE = "IF08_W05 Preflight Readiness Rerun"
IF08_W05_RERUN_STATUS = "if08_w05_preflight_readiness_rerun_pass"
IF08_W05_RERUN_PROJECT_SHA = "93b4ee5c6aa96869ef426331c51e5f3df76e2812"
IF08_W05_RERUN_NEXT_RECOMMENDED_STEP = "IF-08 W0.5 Controlled Ledger/Evidence Integrity Execution"
IF08_W05_SYNC_SOURCE_PHASE = "IF08_W05 Minos Mechanical Alias Normalization"
IF08_W05_SYNC_SOURCE_STATUS = "if08_w05_minos_mechanical_alias_normalization_packet_ready"
IF08_W05_SYNC_SOURCE_PROJECT_SHA = "f05ff031a95625da4d09c1c8bb648cc81ed3a97f"
IF08_W05_SYNC_NEXT_RECOMMENDED_STEP = "rerun_if08_w05_preflight_readiness"
ROUTE_SYNC_SOURCE_PHASE_ID = "INF-FULL-04"
ROUTE_SYNC_DERIVED_NEXT_PHASE_ID = "INF-FULL-05"
ROUTE_SYNC_DERIVED_NEXT_PHASE_CLASS = "review_gate_only"
ROUTE_SYNC_DERIVED_NEXT_PHASE_ADVANCE_MODE = "prompt_only"
EXPECTED_CURRENT_SUCCESSOR_ADVANCE_MODE = "canonroadmap"
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
CI_TERMINAL_REPORTING_RULE_ROOT = ROOT / "artifacts" / "ci_terminal_reporting_rule"
CI_TERMINAL_REPORTING_RULE_DECISION_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "decision.json"
CI_TERMINAL_REPORTING_RULE_SUMMARY_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "summary.json"
CI_TERMINAL_REPORTING_RULE_REPORT_PATH = CI_TERMINAL_REPORTING_RULE_ROOT / "report.md"
INFERNUS_STANDING_AUTHORIZATION_PATH = ROOT / "INFERNUS_STANDING_AUTHORIZATION.md"
INF_FULL_ROUTE_SYNC_DECISION_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "decision.json"
INF_FULL_ROUTE_SYNC_SUMMARY_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "summary.json"
INF_FULL_ROUTE_SYNC_REPORT_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "report.md"
INF_FULL_ROUTE_SYNC_WORKSPACE_PATH = ROOT / "artifacts" / "inf_full_route_sync_04_to_05" / "workspace_hygiene_snapshot.txt"

GOVERNANCE_CLASSES = {
    "governance_repair", "observability",
    "transition_engine", "contract", "route"
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
    "AGENT_IDENTITY.md",
    "ACTIVE_CONTEXT_SCHEMA.json",
    "scripts/validate_active_context_state.py",
    "ROADMAP_CANONICAL.md",
    "MANDATORY_READ_FIRST_RULES.md",
    "CURRENT_STATE.md",
    "NEXT_ACTION.md",
    "DECISION_LOCKS.md",
    "OPERATOR_PREFERENCES.md",
    "CONTEXT_INDEX.md",
    "ARIS_PHASE_LEDGER.md",
    "README.md",
    "PROMPT_CONTRACT.md",
    "LAB_OPERATING_CONTRACT.md",
    "EXCLUDENT_POLICY.md",
    "INFERNUS_STANDING_AUTHORIZATION.md",
    "project_mirror/docs/infernus_full/infernus_full_canonroadmap.md",
]

EXPECTED_PRIORITY_READ_ORDER = [
    "1. ACTIVE_CONTEXT_STATE.json",
    "2. AGENT_IDENTITY.md",
    "3. ACTIVE_CONTEXT_SCHEMA.json",
    "4. scripts/validate_active_context_state.py",
    "5. ROADMAP_CANONICAL.md",
    "6. MANDATORY_READ_FIRST_RULES.md",
    "7. CURRENT_STATE.md",
    "8. NEXT_ACTION.md",
    "9. DECISION_LOCKS.md",
    "10. OPERATOR_PREFERENCES.md",
    "11. CONTEXT_INDEX.md",
    "12. ARIS_PHASE_LEDGER.md",
    "13. README.md",
    "14. PROMPT_CONTRACT.md",
    "15. LAB_OPERATING_CONTRACT.md",
    "16. EXCLUDENT_POLICY.md",
    "17. INFERNUS_STANDING_AUTHORIZATION.md",
    "18. project_mirror/docs/infernus_full/infernus_full_canonroadmap.md",
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
    # Files listed in required_files_for_transition are historical records.
    # Files moved to archive/ or excludent/ by an authorized operator cleanup gate
    # are still considered present — the record is audit trail, not a live path assertion.
    _ARCHIVED_ROOTS = [
        ROOT / "archive",
        ROOT / "excludent",
    ]

    for relative_path in state["required_files_for_transition"]:
        resolved = ROOT / relative_path
        if relative_path.startswith("../") and not resolved.exists():
            continue
        if resolved.exists():
            continue
        # Check if the file was moved to an archive or excludent subtree.
        filename = pathlib.Path(relative_path).name
        found_in_archive = any(
            list(archive_root.rglob(filename))
            for archive_root in _ARCHIVED_ROOTS
            if archive_root.exists()
        )
        if found_in_archive:
            continue
        _require(False, f"missing required transition file: {relative_path}")


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


def _check_next_phase_in_transition_table(state: dict[str, Any]) -> None:
    row = _get_transition_row(state.get("current_phase_id", ""), state.get("decision", ""))
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
        print(f"WARN: governance_gate_streak=2. Proximo gate DEVE ser capacidade.")


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
    boot_files = state.get("last_boot_files_read", [])
    missing = [f for f in REQUIRED_BOOT_FILES if f not in boot_files]
    if missing:
        print(f"BLOCK: last_boot_files_read missing: {missing}")
        print("Codex must populate last_boot_files_read before any action.")
        sys.exit(1)
    try:
        _ordered_positions(boot_files, REQUIRED_BOOT_FILES, "last_boot_files_read")
    except SystemExit as exc:
        print(f"BLOCK: {exc}")
        print("Codex must preserve the mandatory read-first order in last_boot_files_read.")
        sys.exit(1)


def _check_operator_preferences_contract(state: dict[str, Any]) -> None:
    _require(OPERATOR_PREFERENCES_PATH.exists(), "missing OPERATOR_PREFERENCES.md")

    priority_read_order = state.get("anti_corruption_contract", {}).get("canonical_read_order", [])
    _require(
        priority_read_order[: len(EXPECTED_PRIORITY_READ_ORDER)] == EXPECTED_PRIORITY_READ_ORDER,
        "canonical_read_order does not match expected operator-priority read order",
    )
    _require(
        "OPERATOR_PREFERENCES.md" in state.get("required_files_for_transition", []),
        "required_files_for_transition must include OPERATOR_PREFERENCES.md",
    )

    text = OPERATOR_PREFERENCES_PATH.read_text(encoding="utf-8")
    for phrase in OPERATOR_PREFERENCE_REQUIRED_PHRASES:
        _require(phrase in text, f"OPERATOR_PREFERENCES.md missing required phrase: {phrase}")

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
    if transition_row is None:
        _require(state.get("next_phase") is None, "terminal phase must keep next_phase null when there is no successor row")
        _require(state.get("active_next_phase") is None, "terminal phase must keep active_next_phase null when there is no successor row")
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
    _require(
        state.get("next_phase_authorized_by_operator") is True,
        "standing authorization must mark next phase as operator-authorized via canonroadmap approval",
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
        ROOT / "MANDATORY_READ_FIRST_RULES.md",
        "## CI TERMINAL-STATE REPORTING RULE",
        "CI_GREEN_CONFIRMED",
        "CI_FAILED",
        "CI_PENDING",
    )
    _mirror_contains(
        ROOT / "PROMPT_CONTRACT.md",
        "## Required CI output discipline",
        "Decision: pass",
        "CI_PENDING",
    )
    _mirror_contains(
        ROOT / "AGENT_IDENTITY.md",
        "Pending CI means CI_PENDING, not PASS.",
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
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
    _require(state.get("phase_class") == "infernus_full", "phase_class must be infernus_full")

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
    canonroadmap_text = INFERNUS_FULL_CANONROADMAP_PATH.read_text(encoding="utf-8")
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
    transition_row = _get_transition_row(ROUTE_SYNC_SOURCE_PHASE_ID, EXPECTED_DECISION)
    _require(transition_row is not None, "missing INF-FULL-04 Transition Table row")

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
    _require(decision_data.get("decision") == EXPECTED_DECISION, "IF07 decision decision mismatch")
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
    _require(summary_data.get("decision") == EXPECTED_DECISION, "INF-FULL-05 summary decision mismatch")
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

    # Verify MANDATORY_READ_FIRST_RULES.md has excludent rule
    mandatory_rules = (ROOT / "MANDATORY_READ_FIRST_RULES.md").read_text(encoding="utf-8")
    _require("EXCLUDENT RULE" in mandatory_rules, "MANDATORY_READ_FIRST_RULES.md must contain EXCLUDENT RULE")
    _require("excluded_from_context" in mandatory_rules, "MANDATORY_READ_FIRST_RULES.md must contain excluded_from_context")


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
    _require(rerun_decision.get("phase_id") == "IF08_W05_PREFLIGHT_READINESS_RERUN", "project rerun decision phase_id mismatch")
    _require(rerun_decision.get("decision") == "pass", "project rerun decision must be pass")
    _require(rerun_decision.get("status") == IF08_W05_RERUN_STATUS, "project rerun decision status mismatch")
    _require(rerun_decision.get("source_latest_completed_phase") == IF08_W05_SYNC_SOURCE_PHASE, "project rerun decision source phase mismatch")
    _require(rerun_decision.get("source_latest_completed_status") == IF08_W05_SYNC_SOURCE_STATUS, "project rerun decision source status mismatch")
    _require(rerun_decision.get("source_project_sha") == IF08_W05_SYNC_SOURCE_PROJECT_SHA, "project rerun decision source project sha mismatch")
    _require(rerun_decision.get("ready_for_next_recommended_step") is True, "project rerun decision must be ready for next step")
    _require(rerun_decision.get("next_recommended_step") == IF08_W05_RERUN_NEXT_RECOMMENDED_STEP, "project rerun decision next step mismatch")
    active_update = rerun_decision.get("active_context_update", {})
    _require(active_update.get("required") is True, "project rerun decision active_context_update.required must be true")
    _require(active_update.get("applied") is True, "project rerun decision active_context_update.applied must be true")
    _require(active_update.get("remote_main_verified") is True, "project rerun decision active_context_update.remote_main_verified must be true")

    rerun_summary = _load_json(IF08_W05_RERUN_SUMMARY_PATH)
    _require(rerun_summary.get("status") == IF08_W05_RERUN_STATUS, "project rerun summary status mismatch")
    _require(rerun_summary.get("next_recommended_step") == IF08_W05_RERUN_NEXT_RECOMMENDED_STEP, "project rerun summary next step mismatch")
    _require(rerun_summary.get("unresolved_mismatch_count") == 0, "project rerun summary unresolved mismatch count must be zero")

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
    _require(decision.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "project controlled decision phase_id mismatch")
    _require(decision.get("decision") == "pass", "project controlled decision must be pass")
    _require(decision.get("status") == IF08_W05_CONTROLLED_STATUS, "project controlled decision status mismatch")
    _require(decision.get("wave_id") == "W0.5", "project controlled decision wave_id mismatch")
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
    _require(decision.get("required_next_action") == "sync_if08_w05_controlled_execution_into_active_context", "project controlled decision next action mismatch")

    summary = _load_json(IF08_W05_CONTROLLED_SUMMARY_PATH)
    _require(summary.get("phase_id") == "IF-08-W05-CONTROLLED-EXECUTION", "project controlled summary phase_id mismatch")
    _require(summary.get("decision") == "pass", "project controlled summary must be pass")
    _require(summary.get("status") == IF08_W05_CONTROLLED_STATUS, "project controlled summary status mismatch")
    _require(summary.get("tamper_attempts_expected") == 4, "project controlled summary tamper_attempts_expected must be 4")
    _require(summary.get("tamper_attempts_detected") == 4, "project controlled summary tamper_attempts_detected must be 4")
    _require(summary.get("ter_result") == 1.0, "project controlled summary ter_result must be 1.0")
    _require(summary.get("hash_chain_valid_clean") is True, "project controlled summary hash_chain_valid_clean must be true")
    _require(summary.get("custody_chain_valid_clean") is True, "project controlled summary custody_chain_valid_clean must be true")
    _require(summary.get("active_context_update_applied") is False, "project controlled summary active_context_update_applied must remain false before sync record")
    _require(summary.get("canonical_sync_performed") is False, "project controlled summary canonical_sync_performed must remain false before sync record")
    _require(summary.get("required_next_action") == "sync_if08_w05_controlled_execution_into_active_context", "project controlled summary next action mismatch")

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
    _require(ledger_entry.get("status") == IF08_W05_CONTROLLED_STATUS, "project controlled execution ledger status mismatch")


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

    summary = _load_json(IF08_W05_POST_SYNC_SUMMARY_PATH)
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

    no_execution = _load_json(IF08_W05_POST_SYNC_NO_EXECUTION_PATH)
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


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)

    _require(state["phase_id"] == EXPECTED_PHASE_ID, "unexpected phase_id")
    _require(state["current_phase_id"] == EXPECTED_PHASE_ID, "unexpected current_phase_id")
    _require(state["previous_phase_id"] == EXPECTED_PREVIOUS_PHASE_ID, "unexpected previous_phase_id")
    _require(state["status"] == EXPECTED_STATUS, "unexpected status")
    _require(state["decision"] == EXPECTED_DECISION, "unexpected decision")
    _require(state["latest_completed_phase"] == EXPECTED_PHASE, "unexpected latest completed phase")
    _require(state["latest_completed_status"] == EXPECTED_LATEST_COMPLETED_STATUS, "unexpected latest completed status")
    _require(state["current_status"] == EXPECTED_CURRENT_STATUS, "unexpected current status")
    _require(state["schema_version"] == EXPECTED_SCHEMA_VERSION, "unexpected schema version")
    _require(state["latest_completed_project_commit_sha"] == EXPECTED_LATEST_COMPLETED_PROJECT_SHA, "unexpected latest completed project sha")
    _require(state["latest_completed_ci_state"] == EXPECTED_LATEST_COMPLETED_CI_STATE, "unexpected latest completed ci state")
    _require(state["latest_completed_next_recommended_step"] == EXPECTED_NEXT_RECOMMENDED_STEP, "unexpected latest completed next step")
    _require(state["active_context_remote_main_reflects_latest_phase"] is True, "active_context_remote_main_reflects_latest_phase must be true")
    _require(state["permanent_active_update_rule_installed"] is True, "permanent_active_update_rule_installed must be true")
    _require(state["current_phase_bots_executed"] is False, "current_phase_bots_executed must be false")
    _require(state["next_phase"] == EXPECTED_NEXT_PHASE_ID, "next_phase must declare IF-08 as standing-authorized successor")
    _require(state["active_next_phase"] == EXPECTED_NEXT_PHASE_ID, "active_next_phase must declare IF-08 as standing-authorized successor")
    _require(state["active_next_phase_class"] == EXPECTED_NEXT_PHASE_CLASS, "active_next_phase_class must declare infernus_full_execution")
    _require(state["next_phase_authorized_by_operator"] is True, "next phase must be operator-authorized through standing canonroadmap approval")
    _require(state["anti_proliferation_rule_active"] is True, "anti_proliferation_rule_active must be true")
    _require(state["ci_enforcement_active"] is True, "ci_enforcement_active must be true")

    # Circuit breaker fields
    _require("governance_gate_streak" in state, "governance_gate_streak must be present")
    _require("seen_gate_signatures" in state, "seen_gate_signatures must be present")
    _require("phase_class" in state, "phase_class must be present")

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

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase")
    _require_paths_match(state, policy["latest_completed_status_must_match_across"], "latest_completed_status")
    _require_paths_match(state, policy["status_must_match_across"], "status")

    _require(state["current_live_route"]["active_next_phase"] == EXPECTED_NEXT_PHASE_ID, "current live route next phase must be IF-08")
    _require(state["current_live_route"]["active_next_phase_class"] == EXPECTED_NEXT_PHASE_CLASS, "current live route next phase class mismatch")
    _require(state["current_live_route"]["current_status"] == EXPECTED_CURRENT_STATUS, "current live route status mismatch")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next phase execution authorization must be false")

    _require(state["next_action"]["phase"] == EXPECTED_NEXT_PHASE_ID, "next_action.phase mismatch")
    _require(state["next_action"]["phase_class"] == EXPECTED_NEXT_PHASE_CLASS, "next_action.phase_class mismatch")
    _require(state["next_action"]["planning_only"] is False, "next_action.planning_only must be false")
    _require(state["next_action"]["review_only"] is True, "next_action.review_only must be true")
    _require(state["next_action"]["execution_authorization"] is False, "next_action.execution_authorization must be false")
    _require(state["next_action"]["status"] == EXPECTED_NEXT_ACTION_STATUS, "next_action.status mismatch")
    _require(state["latest_completed_no_execution"]["wave_executed"] is True, "latest_completed_no_execution.wave_executed mismatch")
    _require(state["latest_completed_no_execution"]["bot_executed"] is True, "latest_completed_no_execution.bot_executed mismatch")
    _require(state["latest_completed_no_execution"]["w4_preflight_readiness"] is True, "latest_completed_no_execution.w4_preflight_readiness must be true")
    _require(state["latest_completed_no_execution"]["w4_execution_performed"] is True, "latest_completed_no_execution.w4_execution_performed must be true")
    _require(state["latest_completed_no_execution"]["w4_execution_allowed"] is False, "latest_completed_no_execution.w4_execution_allowed must be false")
    _require(state["latest_completed_no_execution"]["future_rhr_required"] == 1.0, "latest_completed_no_execution.future_rhr_required must be 1.0")
    _require(state["latest_completed_no_execution"]["future_ddr_required"] == 1.0, "latest_completed_no_execution.future_ddr_required must be 1.0")
    _require(state["latest_completed_no_execution"]["future_cer_required"] == 1.0, "latest_completed_no_execution.future_cer_required must be 1.0")
    _require(state["latest_completed_no_execution"]["readiness_coverage"] == 1.0, "latest_completed_no_execution.readiness_coverage must be 1.0")
    _require(state["latest_completed_no_execution"]["required_preflight_checks"] == 12, "latest_completed_no_execution.required_preflight_checks must be 12")
    _require(state["latest_completed_no_execution"]["ready_preflight_checks"] == 12, "latest_completed_no_execution.ready_preflight_checks must be 12")
    _require(state["latest_completed_no_execution"]["synthetic_attack_cases_total"] == 14, "latest_completed_no_execution.synthetic_attack_cases_total must be 14")
    _require(state["latest_completed_no_execution"]["synthetic_attack_cases_passed"] == 14, "latest_completed_no_execution.synthetic_attack_cases_passed must be 14")
    _require(state["latest_completed_no_execution"]["synthetic_attack_cases_blocked_or_detected"] == 14, "latest_completed_no_execution.synthetic_attack_cases_blocked_or_detected must be 14")
    _require(state["latest_completed_no_execution"]["rollback_honesty_checks_required"] == 6, "latest_completed_no_execution.rollback_honesty_checks_required must be 6")
    _require(state["latest_completed_no_execution"]["rollback_honesty_checks_passed"] == 6, "latest_completed_no_execution.rollback_honesty_checks_passed must be 6")
    _require(state["latest_completed_no_execution"]["duplicate_detection_checks_required"] == 5, "latest_completed_no_execution.duplicate_detection_checks_required must be 5")
    _require(state["latest_completed_no_execution"]["duplicate_detection_checks_passed"] == 5, "latest_completed_no_execution.duplicate_detection_checks_passed must be 5")
    _require(state["latest_completed_no_execution"]["cost_enforcement_checks_required"] == 3, "latest_completed_no_execution.cost_enforcement_checks_required must be 3")
    _require(state["latest_completed_no_execution"]["cost_enforcement_checks_passed"] == 3, "latest_completed_no_execution.cost_enforcement_checks_passed must be 3")
    _require(state["latest_completed_no_execution"]["rhr_observed"] == 1.0, "latest_completed_no_execution.rhr_observed must be 1.0")
    _require(state["latest_completed_no_execution"]["ddr_observed"] == 1.0, "latest_completed_no_execution.ddr_observed must be 1.0")
    _require(state["latest_completed_no_execution"]["cer_observed"] == 1.0, "latest_completed_no_execution.cer_observed must be 1.0")
    _require(state["latest_completed_no_execution"]["execution_scope"] == "synthetic_isolated_lab_only", "latest_completed_no_execution.execution_scope must be synthetic_isolated_lab_only")
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

    _require(state["locks"]["deferred_phase"] == EXPECTED_NEXT_PHASE_ID, "locks.deferred_phase must point to IF-08")
    _require(
        EXPECTED_NEXT_RECOMMENDED_STEP in state["locks"]["deferred_phase_reason"],
        "locks.deferred_phase_reason must mention the exact next recommended step",
    )
    _require(state["history_summary"]["previous_execution_phase"] == EXPECTED_PREVIOUS_PHASE, "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == EXPECTED_PREVIOUS_PHASE, "unexpected last transition from phase")
    _require(state["last_transition"]["to_phase"] == EXPECTED_PHASE, "unexpected last transition to phase")
    _require(state["last_transition"]["to_status"] == EXPECTED_LATEST_COMPLETED_STATUS, "unexpected last transition to_status")

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
        ROOT / "CURRENT_STATE.md",
        "ACTIVE_CONTEXT_STATE.json wins",
        "inf_full_07_if08_authorization_gate_pass",
        "INF-FULL-07",
        "latest_completed_phase: `IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution`",
        "latest_completed_status: `if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass`",
        "Next phase: `IF-08`",
        "Active next phase class: `infernus_full_execution`",
        "next_phase_authorized_by_operator: `true`",
        "ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W4_CONTROLLED_EXECUTION: `true`",
        "PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`",
        "Anti-proliferation rule active: `true`",
        "CI enforcement active: `true`",
        "governance_gate_streak: `0`",
        "latest_completed_project_commit_sha: `c65888a2f587c35b4e38b16b50b917233bac8fa3`",
        "latest_completed_ci_state: `CI_GREEN_CONFIRMED`",
        "next_recommended_step: `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "INF-FULL-07 — IF-08 W4 Controlled Execution Sincronizado",
        "next_phase: IF-08",
        "active_next_phase_class: infernus_full_execution",
        "next_phase_authorized_by_operator: true",
        "latest_completed_status: if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass",
        "Este sync ja registra o packet canonico de controlled execution da W4 com `w4_preflight_readiness=true`, `w4_execution_performed=true`, `w4_execution_allowed=false`, `future_rhr_required=1.0`, `future_ddr_required=1.0`, `future_cer_required=1.0`, `rollback_honesty_checks=6/6`, `duplicate_detection_checks=5/5`, `cost_enforcement_checks=3/3` e `RHR=DDR=CER=1.0`.",
        "O proximo prompt deve executar apenas o post-sync review canonico da W4.",
        "O proximo passo recomendado neste estado e `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`.",
        "IF-08 waves reais: false",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass",
        "Latest completed phase: `IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution`",
        "latest_completed_status=if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass",
        "active_context_remote_main_reflects_if08_w4_controlled_execution=true",
        "permanent_active_update_rule_installed=true",
        "IF-08 real execution = false",
        "future waves real execution = false",
        "post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution",
        "INFERNUS_STANDING_AUTHORIZATION.md",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "OPERATOR_PREFERENCES.md",
        "artifacts/if08_w4_replay_rollback_concurrency_cost_controlled_execution/decision.json",
        "artifacts/infernus/if08_w4_replay_rollback_concurrency_cost_controlled_execution_decision_2026_06_08.json",
        "artifacts/infernus/if08_w4_replay_rollback_concurrency_cost_metrics_2026_06_08.json",
        "artifacts/infernus/if08_w4_replay_rollback_concurrency_cost_safety_attestation_2026_06_08.json",
        "docs/infernus_full/if08_w4_replay_rollback_concurrency_cost_controlled_execution_2026_06_08.md",
        "artifacts/if08_w3_post_sync_review/decision.json",
        "artifacts/infernus/if08_w3_post_sync_review_decision_2026_06_07.json",
        "artifacts/infernus/if08_w4_readiness_matrix_2026_06_07.json",
        "artifacts/if08_w3_runtime_tool_mcp_sandbox_controlled_execution/decision.json",
        "artifacts/infernus/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_decision_2026_06_07.json",
        "artifacts/infernus/if08_w3_runtime_sandbox_detection_matrix_2026_06_07.json",
        "artifacts/infernus/if08_w3_sirene_conditional_execution_record_2026_06_07.json",
        "docs/infernus_full/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_2026_06_07.md",
        "artifacts/if08_w1_context_memory_rag_controlled_execution/decision.json",
        "artifacts/infernus/if08_w1_context_memory_rag_controlled_execution_decision_2026_06_07.json",
        "artifacts/infernus/if08_w1_context_integrity_detection_matrix_2026_06_07.json",
        "docs/infernus_full/if08_w1_context_memory_rag_controlled_execution_2026_06_07.md",
        "artifacts/if08_w1_context_memory_rag_preflight_readiness/decision.json",
        "artifacts/infernus/if08_w1_context_memory_rag_preflight_readiness_decision_2026_06_07.json",
        "artifacts/if08_w05_controlled_execution/decision.json",
        "artifacts/infernus/if08_w05_controlled_execution_decision_2026_06_07.json",
        "artifacts/infernus/if08_w05_evidence_bundle_manifest_2026_06_07.json",
        "next_phase: `IF-08`",
        "active_next_phase_class: `infernus_full_execution`",
        "next_phase_authorized_by_operator: `true`",
        "INFERNUS_STANDING_AUTHORIZATION.md",
        "excludent/",
        "excluded_from_context",
        "read_by_default = false",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution | pass",
        "if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass",
        "project_commit_sha: `c65888a2f587c35b4e38b16b50b917233bac8fa3`",
        "next_recommended_step: `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`",
        "IF-08 W3 Runtime/Tool/MCP/Sandbox Controlled Execution | pass",
        "if08_w3_runtime_tool_mcp_sandbox_controlled_execution_pass",
        "project_commit_sha: `598dd5c8d98e8c9f89f9123e10efedf50871079b`",
        "next_recommended_step: `post_sync_review_if08_w3_runtime_tool_mcp_sandbox_controlled_execution`",
        "IF-08 W1 Context/Memory/RAG Controlled Execution | pass",
        "if08_w1_context_memory_rag_controlled_execution_pass",
        "project_commit_sha: `1d0f51584e082d1f3f7c270df89d567a96066711`",
        "next_recommended_step: `post_sync_review_if08_w1_context_memory_rag_controlled_execution`",
        "IF-08 W1 Context/Memory/RAG Preflight Readiness | pass",
        "IF-08 W0.5 Controlled Ledger/Evidence Integrity Execution | pass",
        "if08_w05_controlled_ledger_evidence_integrity_execution_pass",
        "next_phase: `IF-08`",
        "active_next_phase_class: `infernus_full_execution`",
        "next_phase_authorized_by_operator: `true`",
        "INF-FULL-06 | ARIS Infernus FULL Excludent Quarantine Gate | pass",
        "INF-FULL-05 | ARIS Infernus FULL Pre-Execution Review Gate | pass",
        "INF-FULL-04 | ARIS Infernus FULL Scenario Pack & Harness Readiness Gate | pass",
        "INF-FULL-01 | ARIS Infernus Full Scope Charter Gate | pass",
        "ACB-CAP-05 | ARIS Capability Build Advanced Supply Chain Gate | pass",
    )
    _mirror_contains(
        ROOT / "README.md",
        "INF-FULL-07",
        "latest_completed_phase: `IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution`",
        "latest_completed_status: `if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass`",
        "Active next phase: `IF-08`",
        "active_next_phase_class: `infernus_full_execution`",
        "next_phase_authorized_by_operator: `true`",
        "INFERNUS_STANDING_AUTHORIZATION.md",
        "IF-08 real execution: `false`",
        "ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W4_CONTROLLED_EXECUTION: `true`",
        "PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Latest completed phase: IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution",
        "Active next phase: IF-08",
        "Active next phase class: infernus_full_execution",
        "Standing authorization: canonroadmap approved by operator",
        "Real execution (waves against real systems, runtime, apply): false",
        "W4 controlled execution is canonical; this sync records w4_execution_allowed=false, rollback_honesty_checks=6/6, duplicate_detection_checks=5/5, cost_enforcement_checks=3/3, RHR=DDR=CER=1.0, all runtime/apply/network/secret/cost/quota surfaces false, and the next step is W4 post-sync review.",
        "| INF-FULL-05 | pass | INF-FULL-06 | infernus_full_excludent_cleanup | canonroadmap |",
        "| INF-FULL-06 | pass | INF-FULL-07 | infernus_full_execution_authorization | canonroadmap |",
        "| INF-FULL-04 | pass | INF-FULL-05 | infernus_full | canonroadmap |",
        "| INF-FULL-07 | pass | IF-08 | infernus_full_execution | canonroadmap |",
    )
    _mirror_contains(
        ROOT / "MANDATORY_READ_FIRST_RULES.md",
        "REGRA ZERO: Canonroadmap é Standing Authorization para Infernus",
        "NÃO pergunte ao operador se pode avançar.",
        "INFERNUS_STANDING_AUTHORIZATION.md",
        "REGRA ANTI-PROLIFERAÇÃO DE GATES",
        "Gate que apenas reafirma locks do gate anterior é PROIBIDO.",
        "Planning e Review do mesmo passo colapsam em UM gate",
        "REGRA DE CICLO DE GATE",
        "REGRA DE AUTO-ADVANCE",
        "REGRA DE ENTREGÁVEL MÍNIMO",
        "REGRA DE TRANSIÇÃO",
        "REGRA DE CIRCUIT BREAKER",
        "governance_gate_streak",
        "REGRA DE PREFERÊNCIA DO OPERADOR",
        "OPERATOR_PREFERENCES.md",
        "REGRA PERMANENTE — ACTIVE-CONTEXT UPDATE REQUIRED AFTER EVERY PHASE",
    )
    _mirror_contains(
        ROOT / "PROMPT_CONTRACT.md",
        "REGRA ANTI-PROLIFERAÇÃO DE GATES",
        "Toda resposta do revisor abre com SHA resolvido de origin/main lido naquele turno.",
        "Sem SHA citado: resposta é INVALID por construção.",
        "POST-COMMIT VERIFICATION",
        "The model never self-reports PASS. The CI reports PASS.",
        "Every Codex prompt that can produce a phase result must require active-context update as a blocking deliverable.",
    )

    fixture_assertion_path = ROOT / "scripts/assert_no_unauthorized_fixtures.py"
    workflow_path = ROOT / ".github/workflows/validate_active_context.yml"
    _require(fixture_assertion_path.read_text(encoding="utf-8") == EXPECTED_FIXTURE_ASSERTION, "unexpected fixture assertion script content")
    _require(workflow_path.read_text(encoding="utf-8") == EXPECTED_WORKFLOW, "unexpected workflow content")

    _warn_boot_receipt(state)

    # Apply streak management (in-memory only — Codex writes back to JSON on next run)
    _apply_streak_management(state, sig, EXPECTED_DECISION)

    print(json.dumps({
        "decision": "pass",
        "status": EXPECTED_STATUS,
        "phase_id": EXPECTED_PHASE_ID,
        "previous_phase_id": EXPECTED_PREVIOUS_PHASE_ID,
        "latest_completed_phase": EXPECTED_PHASE,
        "latest_completed_status": EXPECTED_LATEST_COMPLETED_STATUS,
        "next_phase": EXPECTED_NEXT_PHASE_ID,
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
