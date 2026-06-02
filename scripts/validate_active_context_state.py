#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"

EXPECTED_STATUS = "aris_infernus_lab_full_controlled_fixture_materialization_authorization_planning_gate_pass"
EXPECTED_DECISION = "pass"
EXPECTED_LATEST = "ARIS Infernus Lab FULL Controlled Fixture Materialization Authorization Planning Gate"
EXPECTED_CURRENT_STATUS = "ready_for_aris_infernus_lab_full_controlled_fixture_materialization_authorization_review_gate"
EXPECTED_NEXT = "ARIS Infernus Lab FULL Controlled Fixture Materialization Authorization Review Gate"
EXPECTED_CLASS = "review_gate_only"
EXPECTED_SCHEMA_VERSION = "2.1"
EXPECTED_ROADMAP_PHRASES = ['Infernus revela.', 'Purgatorium corrige.', 'Infernus revalida.', 'BenchUX valida produto real.', 'Crisol refina.', 'Bedrock decide.']


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
        _require(phrase not in text, f"{path.name} contains stale phrase: {phrase}")


def _value_at_path(data: dict[str, Any], dotted_path: str) -> Any:
    value: Any = data
    for segment in dotted_path.split("."):
        _require(isinstance(value, dict) and segment in value, f"missing path: {dotted_path}")
        value = value[segment]
    return value


def _require_paths_match(state: dict[str, Any], paths: list[str], label: str) -> None:
    baseline_path = paths[0]
    baseline_value = _value_at_path(state, baseline_path)
    for other_path in paths[1:]:
        _require(_value_at_path(state, other_path) == baseline_value, f"{label} drift")


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)
    _require(state["status"] == EXPECTED_STATUS, "unexpected status")
    _require(state["decision"] == EXPECTED_DECISION, "unexpected decision")
    _require(state["latest_completed_phase"] == EXPECTED_LATEST, "unexpected latest completed phase")
    _require(state["current_status"] == EXPECTED_CURRENT_STATUS, "unexpected current status")
    _require(state["active_next_phase"] == EXPECTED_NEXT, "unexpected next route")
    _require(state["active_next_phase_class"] == EXPECTED_CLASS, "unexpected next route class")
    _require(state["schema_version"] == EXPECTED_SCHEMA_VERSION, "unexpected schema version")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next route execution authorization must be false")
    _require(state["next_action"]["planning_only"] is False, "next route must not remain planning-only")
    _require(state["next_action"]["review_only"] is True, "next route must remain review-only")
    _require(state["next_action"]["execution_authorization"] is False, "next route must not authorize execution")

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase")
    _require_paths_match(state, policy["status_must_match_across"], "status")
    _require(state["history_summary"]["previous_execution_phase"] == "ARIS Infernus Lab FULL Fixture Materialization Review Gate", "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == "ARIS Infernus Lab FULL Fixture Materialization Review Gate", "unexpected last transition from phase")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    roadmap_required = tuple(EXPECTED_ROADMAP_PHRASES)
    _mirror_contains(ROOT / "ROADMAP_CANONICAL.md", EXPECTED_LATEST, EXPECTED_NEXT, *roadmap_required)
    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "ACTIVE_CONTEXT_STATE.json wins",
        EXPECTED_STATUS,
        EXPECTED_NEXT,
        "authorization_granted=false",
        "fixture_materialization_allowed=false",
        "future_authorization_gate_required=true",
        "human_approval_collected_now=false",
        "No real fixture files were materialized",
        *roadmap_required,
    )
    _mirror_contains(ROOT / "NEXT_ACTION.md", "ACTIVE_CONTEXT_STATE.json wins", EXPECTED_NEXT, "Planning-only: `false`", "Review-only: `true`", "Execution authorization: `false`", *roadmap_required)
    _mirror_contains(ROOT / "DECISION_LOCKS.md", EXPECTED_NEXT, "Authorization planning keeps `authorization_granted=false`, `fixture_materialization_allowed=false`, and future human approval requirements non-bypassable.", "Bedrock remains non-executable and product promotion remains blocked.")
    _mirror_contains(ROOT / "CONTEXT_INDEX.md", EXPECTED_NEXT, "ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_AUTHORIZATION_PLANNING_GATE.md", "aris_infernus_lab_full_controlled_fixture_materialization_authorization_matrix.json")
    _mirror_contains(ROOT / "ARIS_PHASE_LEDGER.md", EXPECTED_STATUS, EXPECTED_NEXT, "Controlled Fixture Materialization Authorization Planning Gate Note", *roadmap_required)
    _mirror_contains(ROOT / "README.md", EXPECTED_LATEST, EXPECTED_NEXT, "ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_AUTHORIZATION_PLANNING_GATE.md")
    _mirror_contains(ROOT / "BEDROCK_GATE.md", EXPECTED_LATEST, EXPECTED_NEXT, "Productization remains blocked")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_MINOS_VERDICT_SCHEMA_PLANNING_GATE.md", "No LLM-as-judge verdict authorization.")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_BEDROCK_BOUNDARY_SIGNAL_SCHEMA_PLANNING_GATE.md", "ARIS Infernus Lab FULL Schema Pack Closure Review Gate", "No Bedrock execution or Bedrock PASS.")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_SCHEMA_PACK_CLOSURE_REVIEW_GATE.md", "ARIS Infernus Lab FULL Schema Pack Closure Review Gate", "ARIS Infernus Lab FULL Scenario Manifest Dataset Planning Gate", "Correct semantics: `review_gate_only`")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_SCENARIO_MANIFEST_DATASET_PLANNING_GATE.md", "ARIS Infernus Lab FULL Scenario Manifest Dataset Planning Gate", "WRN-SIGNAL-REF-NORMALIZATION", "No Bedrock execution or Bedrock PASS.")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_SCENARIO_MANIFEST_DATASET_REVIEW_GATE.md", "ARIS Infernus Lab FULL Scenario Manifest Dataset Review Gate", "The three prior warnings remain resolved", "No fixture materialization.")
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_FIXTURE_MATERIALIZATION_PLANNING_GATE.md", "ARIS Infernus Lab FULL Fixture Materialization Planning Gate", "No real fixture materialization.", "Future gate required: `true`.")
    _mirror_contains(
        ROOT / "ARIS_INFERNUS_FULL_FIXTURE_MATERIALIZATION_REVIEW_GATE.md",
        "ARIS Infernus Lab FULL Fixture Materialization Review Gate",
        "ARIS Infernus Lab FULL Controlled Fixture Materialization Authorization Planning Gate",
        "The planning gate boundaries remained intact under review.",
        "No real fixture materialization.",
    )
    _mirror_contains(ROOT / "ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_AUTHORIZATION_PLANNING_GATE.md", EXPECTED_LATEST, EXPECTED_NEXT, "Authorization granted: `False`.", "Human approval collected now: `False`.")
    _mirror_contains(ROOT / "infernus_protocol.md", "NON-CANONICAL_ADVISORY_RESEARCH_ONLY", "advisory input only")

    stale_route_lines = (
        "- Active next phase: `ARIS Infernus Lab FULL Macroblock Entry Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Evidence Bundle Schema Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Finding & Purgatorium Handoff Schema Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Minos Verdict Schema Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Bedrock Boundary Signal Schema Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Schema Pack Closure Review Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Scenario Manifest Dataset Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Scenario Manifest Dataset Review Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Fixture Materialization Planning Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Fixture Materialization Review Gate`",
        "- Active next phase: `ARIS Infernus Lab FULL Controlled Fixture Materialization Authorization Planning Gate`",
        "Scenario manifest dataset review gate next; no Bedrock authorization yet.",
        "Fixture materialization planning gate next; no Bedrock authorization yet.",
        "Fixture materialization review gate next; no Bedrock authorization yet.",
        "Controlled fixture materialization authorization planning gate next; no Bedrock authorization yet.",
        "Contract Schema Enforcement Implementation Planning Gate",
    )
    for path in [ROOT / "ROADMAP_CANONICAL.md", ROOT / "BEDROCK_GATE.md"]:
        _mirror_excludes(path, *stale_route_lines)

    print(json.dumps({
        "decision": "pass",
        "status": EXPECTED_STATUS,
        "latest_completed_phase": EXPECTED_LATEST,
        "active_next_phase": EXPECTED_NEXT,
        "canonical_roadmap": [
            "Infernus FULL",
            "Purgatorium FULL",
            "Infernus Revalidation",
            "BenchUX Lab",
            "Crisol FULL",
            "Bedrock Gate",
            "Productization / Controlled Pilot",
        ],
        "review_result": "aris infernus lab full controlled fixture materialization authorization planning gate pass"
    }, indent=2))


if __name__ == "__main__":
    main()
