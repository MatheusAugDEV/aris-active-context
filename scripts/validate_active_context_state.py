#!/usr/bin/env python3
"""Anti-corruption validator for ARIS active-context canonical state.

Guards enforced:
  AC-JSON-FIRST | FAIL-CLOSED-ON-DRIFT | MIRRORS-ARE-NON-AUTHORITATIVE
  STRUCTURAL-SCHEMA-NOT-SNAPSHOT | VALIDATOR-ANTI-CORRUPTION
  ARTIFACT-EXISTENCE-CHECK | CROSS-FIELD-CONSISTENCY
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
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

RESULT: dict[str, Any] = {
    "decision": "pass",
    "validated_files": [],
    "checked_artifacts": [],
    "missing_artifacts": [],
    "mirror_drift_count": 0,
    "cross_field_checks": [],
    "extra_property_checks": [],
    "version_contract_status": "unknown",
    "failure_mode_simulations_passed": [],
    "warnings": [],
    "errors": [],
}


# ---------------------------------------------------------------------------
# Core utilities
# ---------------------------------------------------------------------------

def _load_json(path: pathlib.Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _fail(f"{path.name} is not valid JSON: {exc}")
    except FileNotFoundError:
        _fail(f"{path.name} not found")


def _fail(message: str) -> None:
    RESULT["decision"] = "blocked"
    RESULT["errors"].append(message)
    print(json.dumps(RESULT, indent=2), file=sys.stderr)
    sys.exit(1)


def _warn(message: str) -> None:
    RESULT["warnings"].append(message)


def _require(condition: bool, message: str) -> None:
    if not condition:
        _fail(message)


# ---------------------------------------------------------------------------
# Schema structural validation (type/enum/required/additionalProperties)
# ---------------------------------------------------------------------------

def _validate_node(schema_node: dict[str, Any], value: Any, path: str) -> None:
    """Recursively validate value against schema_node."""
    if "const" in schema_node:
        _require(value == schema_node["const"], f"{path}: must equal {schema_node['const']!r}, got {value!r}")

    if "enum" in schema_node:
        _require(value in schema_node["enum"], f"{path}: must be one of {schema_node['enum']!r}, got {value!r}")

    node_type = schema_node.get("type")
    if node_type == "object":
        _require(isinstance(value, dict), f"{path}: must be an object")
        props = schema_node.get("properties", {})
        required = schema_node.get("required", [])

        for key in required:
            _require(key in value, f"{path}: missing required key '{key}'")

        # ANTI-CORRUPTION: enforce additionalProperties:false by checking for extra keys
        if schema_node.get("additionalProperties") is False:
            extra_keys = set(value.keys()) - set(props.keys())
            check = {
                "path": path,
                "extra_keys": sorted(extra_keys),
                "status": "pass" if not extra_keys else "blocked"
            }
            RESULT["extra_property_checks"].append(check)
            _require(
                not extra_keys,
                f"{path}: extra properties not allowed by schema: {sorted(extra_keys)}"
            )

        for key, child_schema in props.items():
            if key in value:
                _validate_node(child_schema, value[key], f"{path}.{key}")

    elif node_type == "array":
        _require(isinstance(value, list), f"{path}: must be an array")
        min_items = schema_node.get("minItems")
        if min_items is not None:
            _require(len(value) >= min_items, f"{path}: must have at least {min_items} items, got {len(value)}")
        if schema_node.get("uniqueItems"):
            _require(len(value) == len(set(value)), f"{path}: items must be unique")
        items_schema = schema_node.get("items")
        if items_schema is not None:
            for i, item in enumerate(value):
                _validate_node(items_schema, item, f"{path}[{i}]")

    elif node_type == "boolean":
        _require(isinstance(value, bool), f"{path}: must be boolean, got {type(value).__name__}")

    elif node_type == "string":
        _require(isinstance(value, str), f"{path}: must be string, got {type(value).__name__}")


# ---------------------------------------------------------------------------
# Cross-field consistency checks
# ---------------------------------------------------------------------------

def _cross_field(state: dict[str, Any]) -> None:
    """Enforce that redundant fields are consistent across the document."""
    checks = [
        # (description, value_a_path, value_b_path)
        (
            "active_next_phase vs current_live_route.active_next_phase",
            state.get("active_next_phase"),
            state.get("current_live_route", {}).get("active_next_phase"),
        ),
        (
            "active_next_phase vs next_action.phase",
            state.get("active_next_phase"),
            state.get("next_action", {}).get("phase"),
        ),
        (
            "active_next_phase vs locks.deferred_phase",
            state.get("active_next_phase"),
            state.get("locks", {}).get("deferred_phase"),
        ),
        (
            "latest_completed_phase vs current_live_route.latest_completed_phase",
            state.get("latest_completed_phase"),
            state.get("current_live_route", {}).get("latest_completed_phase"),
        ),
        (
            "latest_completed_phase vs history_summary.latest_execution_phase",
            state.get("latest_completed_phase"),
            state.get("history_summary", {}).get("latest_execution_phase"),
        ),
        (
            "latest_completed_phase vs last_transition.to_phase",
            state.get("latest_completed_phase"),
            state.get("last_transition", {}).get("to_phase"),
        ),
        (
            "status vs current_live_route.status",
            state.get("status"),
            state.get("current_live_route", {}).get("status"),
        ),
        (
            "current_status vs current_live_route.current_status",
            state.get("current_status"),
            state.get("current_live_route", {}).get("current_status"),
        ),
    ]

    for description, val_a, val_b in checks:
        ok = (val_a == val_b)
        RESULT["cross_field_checks"].append({
            "check": description,
            "status": "pass" if ok else "blocked",
            "values": [val_a, val_b],
        })
        _require(ok, f"Cross-field drift: {description} — '{val_a}' != '{val_b}'")


# ---------------------------------------------------------------------------
# Authorization invariant checks
# ---------------------------------------------------------------------------

def _check_authorization(state: dict[str, Any]) -> None:
    auth = state.get("authorization", {})
    network_scope = auth.get("network_authorized_scope", "")
    _require(
        network_scope == "github_active_context_governance_only",
        f"authorization.network_authorized_scope must be 'github_active_context_governance_only', got {network_scope!r}"
    )

    # planning_gate constraint: no real execution flags may be true
    phase_class = state.get("active_next_phase_class")
    planning_only = state.get("next_action", {}).get("planning_only", False)

    if phase_class == "planning_gate":
        _require(
            planning_only is True,
            "active_next_phase_class is 'planning_gate' but next_action.planning_only is not true"
        )
        _require(
            state.get("next_action", {}).get("execution_authorization") is False,
            "active_next_phase_class is 'planning_gate' but next_action.execution_authorization is true"
        )
        dangerous_flags = [
            "real_apply_authorized",
            "real_dry_run_execution_authorized",
            "approval_execution_authorized",
            "runtime_refactor_authorized",
            "host_filesystem_mutation_authorized",
            "debian_harness_execution_authorized",
            "container_image_vm_creation_authorized",
        ]
        for flag in dangerous_flags:
            _require(
                auth.get(flag) is False,
                f"planning_gate active but authorization.{flag} is true — blocked"
            )


# ---------------------------------------------------------------------------
# Required transition file existence check
# ---------------------------------------------------------------------------

def _check_required_files(state: dict[str, Any]) -> None:
    required = state.get("required_files_for_transition", [])
    for filename in required:
        path = ROOT / filename
        exists = path.exists()
        RESULT["checked_artifacts"].append({
            "file": filename,
            "exists": exists,
            "classification": "required_for_transition",
        })
        _require(exists, f"required_files_for_transition: '{filename}' does not exist")


# ---------------------------------------------------------------------------
# Artifact routes existence check
# ---------------------------------------------------------------------------

def _check_artifact_routes(state: dict[str, Any]) -> None:
    routes = state.get("artifact_routes", {})
    policy = state.get("artifact_integrity_policy", {})
    classified_prefixes = policy.get("classified_artifact_prefixes", {})

    for key, filepath in routes.items():
        path = ROOT / filepath
        if path.exists():
            RESULT["checked_artifacts"].append({"route_key": key, "file": filepath, "exists": True})
        else:
            # Check if it's classified
            classified = any(filepath.startswith(prefix) for prefix in classified_prefixes)
            RESULT["missing_artifacts"].append({
                "route_key": key,
                "file": filepath,
                "classified": classified,
            })
            if not classified:
                _fail(f"artifact_routes['{key}'] = '{filepath}' does not exist and is not classified in artifact_integrity_policy")


# ---------------------------------------------------------------------------
# Markdown mirror phrase checks
# ---------------------------------------------------------------------------

def _mirror_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            RESULT["mirror_drift_count"] += 1
            _fail(f"{path.name}: missing required phrase: {phrase!r}")


def _mirror_not_contains(path: pathlib.Path, *phrases: str) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase in text:
            RESULT["mirror_drift_count"] += 1
            _fail(f"{path.name}: contains stale live text: {phrase!r}")


def _check_mirrors(state: dict[str, Any]) -> None:
    active_next_phase = state["active_next_phase"]
    latest_completed = state["latest_completed_phase"]
    current_status = state["current_status"]
    status = state["status"]

    # All mirrors must carry the anti-corruption header
    for mirror in MIRROR_PATHS:
        if not mirror.exists():
            _fail(f"Mirror file not found: {mirror.name}")
        _mirror_contains(
            mirror,
            "ACTIVE_CONTEXT_STATE.json wins",
        )

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "Derived mirror from ACTIVE_CONTEXT_STATE.json",
        status,
        current_status,
        active_next_phase,
    )

    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Derived mirror from ACTIVE_CONTEXT_STATE.json",
        active_next_phase,
        "planning-only",
        "does not authorize real dry-run execution",
    )

    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "current live locks are derived from ACTIVE_CONTEXT_STATE.json",
        "ACTIVE_CONTEXT_STATE.json is the only canonical live state",
        active_next_phase,
    )

    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "artifact routes are derived from ACTIVE_CONTEXT_STATE.json",
        active_next_phase,
    )

    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "historical ledger only",
        "ACTIVE_CONTEXT_STATE.json",
        latest_completed,
    )

    _mirror_contains(
        ROOT / "README.md",
        "ACTIVE_CONTEXT_STATE.json is the only canonical live state",
        "Markdown drift against",
        "blocking error",
        "Read ACTIVE_CONTEXT_STATE.json first",
    )

    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Live routing is read from ACTIVE_CONTEXT_STATE.json",
        "roadmap sequence only, not the canonical live state",
        active_next_phase,
    )


# ---------------------------------------------------------------------------
# Governance contract JSON-first enforcement
# ---------------------------------------------------------------------------

def _check_governance_contracts_json_first() -> None:
    """Verify that BOOT_PROFILE, MANDATORY_READ_FIRST_RULES, PROMPT_CONTRACT
    declare ACTIVE_CONTEXT_STATE.json as the first read, not a Markdown file."""

    stale_first_read_pattern = re.compile(
        r"^\s*1\.\s*[`\"]?CURRENT_STATE\.md[`\"]?",
        re.MULTILINE,
    )
    json_first_pattern = re.compile(
        r"1\.\s*[`\"]?ACTIVE_CONTEXT_STATE\.json[`\"]?",
        re.IGNORECASE,
    )

    for path in GOVERNANCE_CONTRACT_PATHS:
        if not path.exists():
            _fail(f"Governance contract not found: {path.name}")
        text = path.read_text(encoding="utf-8")

        if stale_first_read_pattern.search(text):
            _fail(
                f"{path.name}: read-first list still starts with CURRENT_STATE.md before ACTIVE_CONTEXT_STATE.json — blocked"
            )

        if not json_first_pattern.search(text):
            _fail(
                f"{path.name}: does not declare ACTIVE_CONTEXT_STATE.json as first read — blocked"
            )


# ---------------------------------------------------------------------------
# Versioning contract check
# ---------------------------------------------------------------------------

def _check_version_contract(state: dict[str, Any]) -> None:
    vc = state.get("versioning_contract", {})
    schema_v = state.get("schema_version")
    ctx_v = state.get("active_context_version")

    declared_schema_v = vc.get("current_schema_version")
    declared_ctx_v = vc.get("current_active_context_version")

    ok = (
        schema_v == declared_schema_v
        and ctx_v == declared_ctx_v
        and vc.get("increment_schema_version_when")
        and vc.get("increment_active_context_version_when")
    )
    RESULT["version_contract_status"] = "pass" if ok else "blocked"
    _require(ok, (
        f"Version contract mismatch: schema_version={schema_v!r} declared={declared_schema_v!r}, "
        f"active_context_version={ctx_v!r} declared={declared_ctx_v!r}"
    ))


# ---------------------------------------------------------------------------
# Stale phrase check across mirrors
# ---------------------------------------------------------------------------

FORBIDDEN_STALE_PHRASES = [
    "ready_for_plan_only_dry_run_commit_rehearsal_review",
    "Active next phase: `Lab Real Simulation Pack Plan-Only Dry-Run Commit Rehearsal Review`",
    "Active next phase: `Lab Real Simulation Pack Debian Disposable Harness Readiness Review`",
    "Active next phase: `Lab Real Simulation Pack Debian Disposable Harness Planning`",
    "Active next phase: `Lab Real Simulation Pack Shadow Workspace Dry-Run Blueprint Review`",
]

def _check_stale_phrases() -> None:
    for path in MIRROR_PATHS:
        if not path.exists():
            continue
        if path.name == "ARIS_PHASE_LEDGER.md":
            continue  # ledger may contain historical entries
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_STALE_PHRASES:
            if phrase in text:
                RESULT["mirror_drift_count"] += 1
                _fail(f"{path.name}: contains stale live text: {phrase!r}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # Step A: Parse JSON files
    state = _load_json(STATE_PATH)
    schema = _load_json(SCHEMA_PATH)
    RESULT["validated_files"].extend([str(STATE_PATH), str(SCHEMA_PATH)])

    # Step B: Structural schema validation (including extra-property enforcement)
    _require(schema.get("type") == "object", "schema top-level must be type:object")
    _require(schema.get("additionalProperties") is False, "schema top-level must be additionalProperties:false")
    _validate_node(schema, state, "ACTIVE_CONTEXT_STATE")

    # Step C: Version contract
    _check_version_contract(state)

    # Step D: Cross-field consistency
    _cross_field(state)

    # Step E: Authorization invariants and planning_gate rules
    _check_authorization(state)

    # Step F: Required transition files existence
    _check_required_files(state)

    # Step G: Artifact routes existence (with classification fallback)
    _check_artifact_routes(state)

    # Step H: Markdown mirror checks
    _check_mirrors(state)

    # Step I: Stale phrase guard
    _check_stale_phrases()

    # Step J: Governance contracts declare JSON-first
    _check_governance_contracts_json_first()
    for p in GOVERNANCE_CONTRACT_PATHS:
        RESULT["validated_files"].append(str(p))

    for p in MIRROR_PATHS:
        RESULT["validated_files"].append(str(p))

    print(json.dumps(RESULT, indent=2))


if __name__ == "__main__":
    main()
