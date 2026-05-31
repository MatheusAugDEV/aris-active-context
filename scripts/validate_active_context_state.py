#!/usr/bin/env python3
"""Anti-corruption validator for ARIS active-context canonical state."""

from __future__ import annotations

import json
import pathlib
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
    ROOT / "LAB_STATUS.md",
    ROOT / "LAB_VERDICTS.md",
]


def _load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _validate_schema(schema: dict[str, Any]) -> None:
    _require(schema.get("type") == "object", "schema must be an object")
    _require(schema.get("additionalProperties") is False, "schema must be closed")


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
    elif node_type == "boolean":
        _require(isinstance(value, bool), f"{path} must be boolean")
    elif node_type == "string":
        _require(isinstance(value, str), f"{path} must be string")


def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        _require(phrase in text, f"{path.name} missing required phrase: {phrase}")


def main() -> None:
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)

    _validate_schema(schema)
    _validate_node(schema, state, "ACTIVE_CONTEXT_STATE")

    _require(state["status"] == "lab_real_simulation_pack_controlled_apply_dry_run_real_execution_approval_capture_planning_readiness_review_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Approval Capture Planning Readiness Review", "unexpected latest completed phase")
    _require(state["current_status"] == "ready_for_controlled_apply_dry_run_real_execution_controlled_operator_approval_capture_gate_planning", "unexpected current status")
    _require(state["active_next_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning", "unexpected next phase")
    _require(state["active_next_phase_class"] == "planning_gate", "unexpected next phase class")
    _require(state["schema_version"] == "2.1", "unexpected schema version")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Approval Capture Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
        "Approval capture authorized now: `False`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
        "Planning-only: `true`",
        "Review-only: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "The next route is planning-only and non-authorizing.",
        "No approval capture authorization now.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Approval Capture Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
        "Approval capture planning readiness review next-route contract",
    )
    _mirror_contains(
        ROOT / "README.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Approval Capture Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
        "Bedrock remains non-executable and product promotion remains blocked.",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
        "Bedrock gate executable now: `False`",
    )
    _mirror_contains(
        ROOT / "LAB_VERDICTS.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Approval Capture Planning Readiness Review - Bedrock Preparation Exception Record",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning",
    )

    print(
        json.dumps(
            {
                "decision": "pass",
                "validated_paths": [str(path) for path in MIRROR_PATHS],
                "review_result": "real execution approval capture planning readiness review pass",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
