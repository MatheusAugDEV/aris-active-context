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
        _require(
            other_value == baseline_value,
            f"{label} drift: {baseline_path}={baseline_value!r} != {other_path}={other_value!r}",
        )


def _validate_schema_subset(value: Any, schema: dict[str, Any], path: str) -> None:
    expected_type = schema.get("type")
    if expected_type == "object":
        _require(isinstance(value, dict), f"{path} must be an object")
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for key in required:
            _require(key in value, f"{path} missing required property: {key}")
        if schema.get("additionalProperties") is False:
            extra_keys = sorted(set(value) - set(properties))
            _require(not extra_keys, f"{path} has extra properties: {extra_keys}")
        for key, child in properties.items():
            if key in value and isinstance(child, dict):
                _validate_schema_subset(value[key], child, f"{path}.{key}")
        return

    if expected_type == "array":
        _require(isinstance(value, list), f"{path} must be an array")
        min_items = schema.get("minItems")
        if min_items is not None:
            _require(len(value) >= min_items, f"{path} must have at least {min_items} items")
        if schema.get("uniqueItems"):
            _require(len(value) == len(set(value)), f"{path} must contain unique items")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                _validate_schema_subset(item, item_schema, f"{path}[{index}]")
        return

    if expected_type == "string":
        _require(isinstance(value, str), f"{path} must be a string")
    elif expected_type == "boolean":
        _require(isinstance(value, bool), f"{path} must be a boolean")

    if "enum" in schema:
        _require(value in schema["enum"], f"{path} must be one of {schema['enum']}")
    if "const" in schema:
        _require(value == schema["const"], f"{path} must equal {schema['const']!r}")


def _require_json_first(path: pathlib.Path) -> None:
    text = path.read_text(encoding="utf-8")
    _require(
        re.search(r"^\s*1\.\s+ACTIVE_CONTEXT_STATE\.json\b", text, re.MULTILINE) is not None,
        f"{path.name} must list ACTIVE_CONTEXT_STATE.json as step 1",
    )


def _require_required_files_exist(root: pathlib.Path, required_files: list[str]) -> None:
    for relpath in required_files:
        _require((root / relpath).exists(), f"required transition file missing: {relpath}")


def main() -> None:
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)
    _validate_schema_subset(state, schema, "ACTIVE_CONTEXT_STATE.json")

    _require(state["status"] == "lab_real_simulation_pack_controlled_apply_dry_run_real_execution_lab_simulation_closure_gate_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate", "unexpected latest completed phase")
    _require(state["current_status"] == "lab_simulation_route_closed_pending_post_review_routing_decision", "unexpected current status")
    _require(state["active_next_phase"] == "Lab Simulation Closure Post-Review Routing Decision", "unexpected next route")
    _require(state["active_next_phase_class"] == "review_gate_only", "unexpected next route class")
    _require(state["schema_version"] == "2.1", "unexpected schema version")
    _require(state["versioning_contract"]["current_schema_version"] == state["schema_version"], "schema_version must match versioning_contract.current_schema_version")
    _require(state["versioning_contract"]["current_active_context_version"] == state["active_context_version"], "active_context_version must match versioning_contract.current_active_context_version")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next route execution authorization must be false")
    _require(state["current_live_route"]["decision"] == state["decision"], "decision drift between top-level and current_live_route")
    _require(
        state["history_summary"]["previous_execution_phase"] == state["last_transition"]["from_phase"],
        "history_summary.previous_execution_phase must match last_transition.from_phase",
    )
    _require(state["next_action"]["phase_class"] == state["active_next_phase_class"], "next_action.phase_class must match active_next_phase_class")
    _require(state["current_live_route"]["active_next_phase_class"] == state["active_next_phase_class"], "current_live_route.active_next_phase_class must match active_next_phase_class")
    _require(state["next_action"]["review_only"] is True, "review_gate_only route must remain review_only")
    _require(state["next_action"]["execution_authorization"] is False, "review_gate_only route must not authorize execution")

    _require_required_files_exist(ROOT, state["required_files_for_transition"])

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(
        state,
        policy["active_next_phase_must_match_across"],
        "active_next_phase cross-field",
    )
    _require_paths_match(
        state,
        policy["current_status_must_match_across"],
        "current_status cross-field",
    )
    _require_paths_match(
        state,
        policy["latest_completed_phase_must_match_across"],
        "latest_completed_phase cross-field",
    )
    _require_paths_match(
        state,
        policy["status_must_match_across"],
        "status cross-field",
    )

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "ACTIVE_CONTEXT_STATE.json wins",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Six-phase route closed: `True`",
        "Previous execution phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Review-only: `true`",
        "Execution authorization: `false`",
        "Previous execution phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "Six-phase Lab Simulation route is closed.",
        "Bedrock remains non-executable and product promotion remains blocked.",
        "Last transition from: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Residual warnings register",
        "Previous execution phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "Previous execution phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
        "Last transition from: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "README.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Residual warnings remain carried forward explicitly.",
        "Previous execution phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Real Dry-Run Evidence Final Review`",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Lab Simulation route is closed and does not create phase 7.",
    )
    _mirror_contains(
        ROOT / "LAB_VERDICTS.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate - Bedrock Preparation Exception Record",
        "Lab Simulation Closure Post-Review Routing Decision",
    )
    _require_json_first(ROOT / "BOOT_PROFILE.md")
    _require_json_first(ROOT / "MANDATORY_READ_FIRST_RULES.md")
    _require_json_first(ROOT / "PROMPT_CONTRACT.md")

    print(
        json.dumps(
            {
                "decision": "pass",
                "validated_paths": [
                    str(ROOT / "CURRENT_STATE.md"),
                    str(ROOT / "NEXT_ACTION.md"),
                    str(ROOT / "DECISION_LOCKS.md"),
                    str(ROOT / "CONTEXT_INDEX.md"),
                    str(ROOT / "ARIS_PHASE_LEDGER.md"),
                    str(ROOT / "ROADMAP_CANONICAL.md"),
                    str(ROOT / "README.md"),
                    str(ROOT / "LAB_VERDICTS.md"),
                ],
                "review_result": "lab simulation closure gate pass",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
