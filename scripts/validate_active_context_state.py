#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"

EXPECTED_STATUS = "aris_infernus_lab_full_scope_attack_taxonomy_planning_gate_pass"
EXPECTED_DECISION = "pass"
EXPECTED_LATEST = "ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate"
EXPECTED_CURRENT_STATUS = "ready_for_aris_infernus_lab_full_13_bot_contract_pack_planning_gate"
EXPECTED_NEXT = "ARIS Infernus Lab FULL 13-Bot Contract Pack Planning Gate"
EXPECTED_CLASS = "planning_gate"
EXPECTED_SCHEMA_VERSION = "2.1"
EXPECTED_ROADMAP_PHRASES = [
    "Infernus revela.",
    "Purgatorium corrige.",
    "Infernus revalida.",
    "Crisol refina.",
    "Bedrock decide.",
]

ALLOWED_TOP_LEVEL_KEYS = {
    "active_context_version",
    "schema_version",
    "canonical_repository",
    "canonical_branch",
    "canonical_live_state_file",
    "canonical_schema_file",
    "markdown_files_are",
    "additional_live_state_sources_allowed",
    "status",
    "decision",
    "latest_completed_phase",
    "current_status",
    "active_next_phase",
    "active_next_phase_class",
    "versioning_contract",
    "anti_corruption_contract",
    "artifact_integrity_policy",
    "cross_field_consistency_policy",
    "required_files_for_transition",
    "completed_phases",
    "current_live_route",
    "next_action",
    "locks",
    "authorization",
    "canonicality_rules",
    "validation_policy",
    "artifact_routes",
    "history_summary",
    "last_transition",
    "required_update_policy",
    "drift_signals",
}

AUTHORIZATION_KEYS = {
    "production_authorized",
    "product_ready",
    "runtime_integration_allowed",
    "generic_action_runtime_activated",
    "real_apply_authorized",
    "real_dry_run_execution_authorized",
    "approval_execution_authorized",
    "runtime_refactor_authorized",
    "host_filesystem_mutation_authorized",
    "debian_harness_execution_authorized",
    "container_image_vm_creation_authorized",
    "package_manager_execution_authorized",
    "package_installation_authorized",
    "network_authorized_scope",
    "secrets_access_authorized",
    "external_llm_api_authorized",
    "dependency_change_authorized",
    "frontend_backend_action_runtime_audio_mutation_authorized",
}


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing required phrase: {phrase}")


def _mirror_excludes(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase not in text, f"{path.name} contains stale active-routing phrase: {phrase}")


def _artifact_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing artifact phrase: {phrase}")


def _value_at_path(data: dict[str, Any], dotted_path: str) -> Any:
    value: Any = data
    for segment in dotted_path.split("."):
        _require(isinstance(value, dict) and segment in value, f"missing path for cross-field validation: {dotted_path}")
        value = value[segment]
    return value


def _require_paths_match(state: dict[str, Any], paths: list[str], label: str) -> None:
    baseline_path = paths[0]
    baseline_value = _value_at_path(state, baseline_path)
    for other_path in paths[1:]:
        other_value = _value_at_path(state, other_path)
        _require(other_value == baseline_value, f"{label} drift: {baseline_path}={baseline_value!r} != {other_path}={other_value!r}")


def _require_json_first(path: pathlib.Path) -> None:
    text = path.read_text(encoding="utf-8")
    _require(
        re.search(r"^\s*1\.\s+ACTIVE_CONTEXT_STATE\.json\b", text, re.MULTILINE) is not None,
        f"{path.name} must list ACTIVE_CONTEXT_STATE.json as step 1",
    )


def _require_no_extra_keys(state: dict[str, Any]) -> None:
    extras = sorted(set(state) - ALLOWED_TOP_LEVEL_KEYS)
    _require(not extras, f"extra properties in ACTIVE_CONTEXT_STATE.json: {extras}")
    auth = state.get("authorization", {})
    _require(isinstance(auth, dict), "authorization must be object")
    auth_extras = sorted(set(auth) - AUTHORIZATION_KEYS)
    _require(not auth_extras, f"extra properties in authorization: {auth_extras}")


def _require_required_files_exist(state: dict[str, Any]) -> None:
    for relpath in state["required_files_for_transition"]:
        _require((ROOT / relpath).exists(), f"required file missing: {relpath}")


def main() -> None:
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)
    _require(schema.get("title") == "ARIS Active Context Canonical Live State Schema v2.1", "unexpected schema title")
    _require_no_extra_keys(state)
    _require_required_files_exist(state)

    _require(state["status"] == EXPECTED_STATUS, "unexpected status")
    _require(state["decision"] == EXPECTED_DECISION, "unexpected decision")
    _require(state["latest_completed_phase"] == EXPECTED_LATEST, "unexpected latest completed phase")
    _require(state["current_status"] == EXPECTED_CURRENT_STATUS, "unexpected current status")
    _require(state["active_next_phase"] == EXPECTED_NEXT, "unexpected next route")
    _require(state["active_next_phase_class"] == EXPECTED_CLASS, "unexpected next route class")
    _require(state["schema_version"] == EXPECTED_SCHEMA_VERSION, "unexpected schema version")
    _require(state["versioning_contract"]["current_schema_version"] == state["schema_version"], "schema_version vs versioning_contract mismatch")

    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next route execution authorization must be false")
    _require(state["next_action"]["planning_only"] is True, "next route must be planning_only")
    _require(state["next_action"]["review_only"] is False, "next route must not be review_only")
    _require(state["next_action"]["execution_authorization"] is False, "next route must not authorize execution")
    _require(state["next_action"]["operator_approval_packet_review_is_execution_approval"] is False, "operator approval packet review must not be execution approval")

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase cross-field")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status cross-field")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase cross-field")
    _require_paths_match(state, policy["status_must_match_across"], "status cross-field")
    _require(state["history_summary"]["previous_execution_phase"] == "ARIS Infernus Lab FULL Macroblock Entry Gate", "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == "ARIS Infernus Lab FULL Macroblock Entry Gate", "unexpected last transition from phase")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    roadmap_required = tuple(EXPECTED_ROADMAP_PHRASES)
    _mirror_contains(ROOT / "ROADMAP_CANONICAL.md", "ARIS Macro Roadmap Canonical Chain", *roadmap_required)
    _mirror_contains(ROOT / "CURRENT_STATE.md", "ACTIVE_CONTEXT_STATE.json wins", EXPECTED_STATUS, EXPECTED_NEXT, *roadmap_required)
    _mirror_contains(ROOT / "NEXT_ACTION.md", "ACTIVE_CONTEXT_STATE.json wins", EXPECTED_NEXT, "Planning-only: `true`", "Execution authorization: `false`", *roadmap_required)
    _mirror_contains(ROOT / "DECISION_LOCKS.md", "ACTIVE_CONTEXT_STATE.json wins", EXPECTED_NEXT, "Old R0/F120", "Bedrock remains non-executable and product promotion remains blocked.")
    _mirror_contains(ROOT / "CONTEXT_INDEX.md", "ACTIVE_CONTEXT_STATE.json wins", EXPECTED_NEXT, "ARIS_INFERNUS_FULL_SCOPE_ATTACK_TAXONOMY_GATE.md", "infernus_protocol.md", *roadmap_required)
    _mirror_contains(ROOT / "ARIS_PHASE_LEDGER.md", EXPECTED_STATUS, EXPECTED_NEXT, "Scope & Taxonomy Gate Note", *roadmap_required)
    _mirror_contains(ROOT / "README.md", EXPECTED_NEXT, "ARIS_INFERNUS_FULL_SCOPE_ATTACK_TAXONOMY_GATE.md", *roadmap_required)
    _mirror_contains(ROOT / "LAB_STATUS.md", "historical_only", "not active roadmap authority")
    _mirror_contains(ROOT / "LAB_VERDICTS.md", "historical_only", "not active roadmap authority")
    _mirror_contains(ROOT / "ARIS_ROADMAP_R0_F120.md", "not active roadmap authority", "ROADMAP_CANONICAL.md")
    _mirror_contains(ROOT / "PROJECT_CONTEXT_ARIS.md", "historical_only", "not active roadmap authority")
    _mirror_contains(ROOT / "BEDROCK_GATE.md", "Bedrock remains a future maximum decision gate", "Productization remains blocked")
    _artifact_contains(
        ROOT / "ARIS_INFERNUS_FULL_ENTRY_GATE.md",
        "ARIS Infernus Lab FULL Macroblock Entry Gate",
        "aris_infernus_lab_full_macroblock_entry_gate_pass",
        "pass",
        "Infernus revela.",
        "Purgatorium corrige.",
        "Infernus revalida.",
        "Crisol refina.",
        "Bedrock decide.",
        "Non-Execution Boundary",
        "Discovery Taxonomy",
        "Evidence Requirements",
        "Purgatorium Handoff Contract",
        "Bedrock Non-Authorization",
        "Productization Non-Authorization",
        "ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate",
    )
    _artifact_contains(
        ROOT / "ARIS_INFERNUS_FULL_SCOPE_ATTACK_TAXONOMY_GATE.md",
        "ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate",
        "aris_infernus_lab_full_scope_attack_taxonomy_planning_gate_pass",
        "pass",
        "ARIS Infernus Lab FULL Macroblock Entry Gate",
        "infernus_protocol.md",
        "Attack Taxonomy",
        "Finding Taxonomy",
        "Official 13-Bot Discovery Role Mapping",
        "Historical Function Preservation",
        "P0 Gap Resolutions",
        "Severity Model S0-S5",
        "Evidence Requirements",
        "Purgatorium Handoff Model",
        "Bedrock Impact Signals",
        "Non-Execution Boundary",
        "Productization Non-Authorization",
        "ARIS Infernus Lab FULL 13-Bot Contract Pack Planning Gate",
        "BB-UNRESOLVED-S4",
        "BB-UNRESOLVED-S5",
        "BB-NO-REPLAY-EVIDENCE",
        "BB-NO-HITL-PROOF",
        "BB-LLM-ONLY-JUDGE",
        "BB-MISSING-PROVENANCE",
        "BB-COVERAGE-GAP",
        "BB-SCHEMA-DRIFT",
        "BB-FALSE-PASS",
        "BB-ACCEPTED-RISK-AS-RESOLVED",
        "BB-PRODUCT-CLAIM-INFLATION",
        "Quimera",
        "Dúbio",
        "Elos",
        "Taipan",
        "Labirinto",
        "Vitium",
        "Gula",
        "Apep",
        "Patrono",
        "Éfeso",
        "Abzu",
        "Loop",
        "Minos",
    )
    _artifact_contains(ROOT / "infernus_protocol.md", "NON-CANONICAL_ADVISORY_RESEARCH_ONLY", "canonicity: advisory input only")

    for mirror in [ROOT / "CURRENT_STATE.md", ROOT / "NEXT_ACTION.md", ROOT / "DECISION_LOCKS.md", ROOT / "CONTEXT_INDEX.md", ROOT / "ARIS_PHASE_LEDGER.md", ROOT / "README.md", ROOT / "ROADMAP_CANONICAL.md"]:
        _mirror_excludes(mirror, "Contract Schema Enforcement Implementation Planning Gate", "ARIS-BEDROCK-C7", "R0→F120 — Canonical Governance Roadmap")

    _require_json_first(ROOT / "BOOT_PROFILE.md")
    _require_json_first(ROOT / "MANDATORY_READ_FIRST_RULES.md")
    _require_json_first(ROOT / "PROMPT_CONTRACT.md")

    print(json.dumps({
        "decision": "pass",
        "status": EXPECTED_STATUS,
        "active_next_phase": EXPECTED_NEXT,
        "latest_completed_phase": EXPECTED_LATEST,
        "canonical_roadmap": "Infernus FULL -> Purgatorium FULL -> Infernus Revalidation -> Crisol FULL -> Bedrock Gate",
        "validated_paths": [
            str(ROOT / "ACTIVE_CONTEXT_STATE.json"),
            str(ROOT / "ROADMAP_CANONICAL.md"),
            str(ROOT / "CURRENT_STATE.md"),
            str(ROOT / "NEXT_ACTION.md"),
            str(ROOT / "DECISION_LOCKS.md"),
            str(ROOT / "CONTEXT_INDEX.md"),
            str(ROOT / "ARIS_PHASE_LEDGER.md"),
            str(ROOT / "README.md"),
            str(ROOT / "ARIS_INFERNUS_FULL_ENTRY_GATE.md"),
            str(ROOT / "ARIS_INFERNUS_FULL_SCOPE_ATTACK_TAXONOMY_GATE.md"),
            str(ROOT / "infernus_protocol.md"),
            str(ROOT / "LAB_STATUS.md"),
            str(ROOT / "LAB_VERDICTS.md"),
            str(ROOT / "ARIS_ROADMAP_R0_F120.md"),
            str(ROOT / "PROJECT_CONTEXT_ARIS.md"),
            str(ROOT / "BEDROCK_GATE.md"),
        ],
        "review_result": "aris infernus lab full scope attack taxonomy planning gate pass",
    }, indent=2))


if __name__ == "__main__":
    main()
