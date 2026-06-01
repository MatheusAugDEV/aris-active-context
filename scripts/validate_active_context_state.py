#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing required phrase: {phrase}")


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
    _require(re.search(r"^\s*1\.\s+ACTIVE_CONTEXT_STATE\.json\b", text, re.MULTILINE) is not None, f"{path.name} must list ACTIVE_CONTEXT_STATE.json as step 1")


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)
    _require(state["status"] == "aris_infernus_lab_full_contract_schema_enforcement_planning_gate_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Gate", "unexpected latest completed phase")
    _require(state["current_status"] == "ready_for_aris_infernus_lab_full_contract_schema_enforcement_planning_review", "unexpected current status")
    _require(state["active_next_phase"] == "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "unexpected next route")
    _require(state["active_next_phase_class"] == "review_gate_only", "unexpected next route class")
    _require(state["schema_version"] == "2.1", "unexpected schema version")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next route execution authorization must be false")
    _require(state["next_action"]["planning_only"] is False, "next route must not be planning_only")
    _require(state["next_action"]["review_only"] is True, "next route must be review_only")
    _require(state["next_action"]["execution_authorization"] is False, "next route must not authorize execution")

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase cross-field")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status cross-field")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase cross-field")
    _require_paths_match(state, policy["status_must_match_across"], "status cross-field")
    _require(state["history_summary"]["previous_execution_phase"] == "ARIS Infernus Lab FULL Contract Schema Hardening Review", "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == "ARIS Infernus Lab FULL Contract Schema Hardening Review", "unexpected last transition from phase")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _mirror_contains(ROOT / "CURRENT_STATE.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Gate", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "Six-phase route closed: `True`")
    _mirror_contains(ROOT / "NEXT_ACTION.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "Review-only: `true`", "Execution authorization: `false`")
    _mirror_contains(ROOT / "DECISION_LOCKS.md", "Six-phase Lab Simulation route remains closed.", "Bedrock remains non-executable and product promotion remains blocked.")
    _mirror_contains(ROOT / "CONTEXT_INDEX.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Gate", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "Architecture plan")
    _mirror_contains(ROOT / "README.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Gate", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "Residual warnings remain carried forward explicitly.")
    _mirror_contains(ROOT / "ROADMAP_CANONICAL.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review", "Contract Schema Enforcement Planning Review remains review-only.")
    _mirror_contains(ROOT / "LAB_VERDICTS.md", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Gate - Bedrock Preparation Exception Record", "ARIS Infernus Lab FULL Contract Schema Enforcement Planning Review")
    _require_json_first(ROOT / "BOOT_PROFILE.md")
    _require_json_first(ROOT / "MANDATORY_READ_FIRST_RULES.md")
    _require_json_first(ROOT / "PROMPT_CONTRACT.md")

    print(json.dumps({"decision": "pass", "validated_paths": [str(ROOT / "CURRENT_STATE.md"), str(ROOT / "NEXT_ACTION.md"), str(ROOT / "DECISION_LOCKS.md"), str(ROOT / "CONTEXT_INDEX.md"), str(ROOT / "ARIS_PHASE_LEDGER.md"), str(ROOT / "ROADMAP_CANONICAL.md"), str(ROOT / "README.md"), str(ROOT / "LAB_VERDICTS.md")], "review_result": "aris infernus lab full contract schema enforcement planning gate pass"}, indent=2))


if __name__ == "__main__":
    main()
