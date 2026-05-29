#!/usr/bin/env python3
"""Anti-corruption validator for ARIS active-context canonical state."""

from __future__ import annotations

import json
import pathlib
import re
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"
MIRROR_PATHS = [
    ROOT / "CURRENT_STATE.md",
    ROOT / "NEXT_ACTION.md",
    ROOT / "DECISION_LOCKS.md",
    ROOT / "CONTEXT_INDEX.md",
    ROOT / "ARIS_PHASE_LEDGER.md",
    ROOT / "ROADMAP_CANONICAL.md",
    ROOT / "README.md",
]
GOVERNANCE_CONTRACT_PATHS = [
    ROOT / "BOOT_PROFILE.md",
    ROOT / "MANDATORY_READ_FIRST_RULES.md",
    ROOT / "PROMPT_CONTRACT.md",
]


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _validate_schema(schema: dict[str, Any]) -> None:
    _require(schema.get("type") == "object", "schema must be an object")
    _require(schema.get("additionalProperties") is False, "schema must be closed")
    required = schema.get("required", [])
    props = schema.get("properties", {})
    state = _load_json(STATE_PATH)
    for key in required:
        _require(key in state, f"missing required top-level key: {key}")
        _require(key in props, f"schema missing property for key: {key}")


def _validate_const(schema_node: dict[str, Any], value: Any, path: str) -> None:
    if "const" in schema_node:
        _require(value == schema_node["const"], f"{path} must equal {schema_node['const']!r}")
    if "enum" in schema_node:
        _require(value in schema_node["enum"], f"{path} must be one of {schema_node['enum']!r}")


def _validate_node(schema_node: dict[str, Any], value: Any, path: str) -> None:
    _validate_const(schema_node, value, path)
    node_type = schema_node.get("type")
    if node_type == "object":
        _require(isinstance(value, dict), f"{path} must be an object")
        required = schema_node.get("required", [])
        props = schema_node.get("properties", {})
        for key in required:
            _require(key in value, f"{path} missing required key: {key}")
        if schema_node.get("additionalProperties") is False:
            extra_keys = set(value.keys()) - set(props.keys())
            _require(not extra_keys, f"{path} has unexpected keys: {sorted(extra_keys)!r}")
        for key, child in props.items():
            if key in value:
                _validate_node(child, value[key], f"{path}.{key}")
    elif node_type == "array":
        _require(isinstance(value, list), f"{path} must be an array")
        items_schema = schema_node.get("items")
        if items_schema is not None:
            for index, item in enumerate(value):
                _validate_node(items_schema, item, f"{path}[{index}]")
    elif node_type == "boolean":
        _require(isinstance(value, bool), f"{path} must be boolean")
    elif node_type == "string":
        _require(isinstance(value, str), f"{path} must be string")


def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing required phrase: {phrase}")


def _check_governance_contracts_json_first() -> None:
    stale_first_read_pattern = re.compile(r"^\s*1\.\s*[`\"]?CURRENT_STATE\.md[`\"]?", re.MULTILINE)
    json_first_pattern = re.compile(r"1\.\s*[`\"]?ACTIVE_CONTEXT_STATE\.json[`\"]?", re.IGNORECASE)
    for path in GOVERNANCE_CONTRACT_PATHS:
        text = path.read_text(encoding="utf-8")
        _require(not stale_first_read_pattern.search(text), f"{path.name} still starts read-first with CURRENT_STATE.md")
        _require(bool(json_first_pattern.search(text)), f"{path.name} must declare ACTIVE_CONTEXT_STATE.json as first read")


def main() -> None:
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)

    _validate_schema(schema)
    _validate_node(schema, state, "ACTIVE_CONTEXT_STATE")

    _require(state["status"] == "lab_real_simulation_pack_controlled_apply_dry_run_operator_approval_response_simulation_planning_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Planning", "unexpected latest completed phase")
    _require(state["current_status"] == "ready_for_controlled_apply_dry_run_operator_approval_response_simulation_readiness_review", "unexpected current status")
    _require(state["active_next_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review", "unexpected next phase")
    _require(state["active_next_phase_class"] == "readiness_gate", "unexpected next phase class")
    _require(state["additional_live_state_sources_allowed"] is False, "additional live state sources must be false")
    _require(state["schema_version"] == "2.1", "schema_version must remain 2.1")

    auth = state["authorization"]
    for key, value in auth.items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _require(
        state["active_next_phase"] == state["current_live_route"]["active_next_phase"] == state["next_action"]["phase"] == state["locks"]["deferred_phase"],
        "cross-field active_next_phase drift detected",
    )
    _require(
        state["latest_completed_phase"] == state["current_live_route"]["latest_completed_phase"] == state["history_summary"]["latest_execution_phase"] == state["last_transition"]["to_phase"],
        "cross-field latest_completed_phase drift detected",
    )
    _require(state["current_live_route"]["current_status"] == state["current_status"], "cross-field current_status drift detected")
    _require(state["current_live_route"]["status"] == state["status"], "cross-field status drift detected")
    _require(state["next_action"]["phase_class"] == "readiness_gate", "unexpected next_action phase_class")
    _require(state["next_action"]["planning_only"] is False, "next_action planning_only must be false")
    _require(state["next_action"]["review_only"] is True, "next_action review_only must be true")

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "Derived mirror from ACTIVE_CONTEXT_STATE.json",
        "lab_real_simulation_pack_controlled_apply_dry_run_operator_approval_response_simulation_planning_pass",
        "ready_for_controlled_apply_dry_run_operator_approval_response_simulation_readiness_review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
        "Operator Approval Response Simulation Planning executed as planning-only and consumed the reviewed request-side planning, readiness-review, and final-review artifacts as one coherent synthetic-only evidence chain.",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Derived mirror from ACTIVE_CONTEXT_STATE.json",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
        "Planning-only: `false`",
        "Review-only: `true`",
        "Execution authorization: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "current live locks are derived from ACTIVE_CONTEXT_STATE.json",
        "ACTIVE_CONTEXT_STATE.json is the only canonical live state",
        "Markdown files are non-authoritative mirrors/docs/history",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "artifact routes are derived from ACTIVE_CONTEXT_STATE.json",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Planning",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "historical ledger only",
        "ACTIVE_CONTEXT_STATE.json",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Planning",
    )
    _mirror_contains(
        ROOT / "README.md",
        "ACTIVE_CONTEXT_STATE.json is the only canonical live state",
        "Markdown drift against JSON is a blocking error",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Live routing is read from ACTIVE_CONTEXT_STATE.json",
        "roadmap sequence only, not the canonical live state",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
        "Roadmap amendment required: `True`",
    )
    _mirror_contains(
        ROOT / "LAB_VERDICTS.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Planning — Bedrock Preparation Exception Record",
        "BEDROCK_PREPARATION_EXCEPTION:",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Simulation Readiness Review",
    )

    _check_governance_contracts_json_first()

    print(
        json.dumps(
            {
                "decision": "pass",
                "validated_paths": [str(p) for p in MIRROR_PATHS] + [str(ROOT / "LAB_VERDICTS.md")] + [str(p) for p in GOVERNANCE_CONTRACT_PATHS],
                "review_result": "operator approval response simulation planning pass",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
