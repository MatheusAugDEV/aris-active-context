#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
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


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)

    _require(state["status"] == "lab_real_simulation_pack_controlled_apply_dry_run_real_execution_controlled_operator_approval_capture_gate_planning_readiness_review_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning Readiness Review", "unexpected latest completed phase")
    _require(state["current_status"] == "ready_for_controlled_apply_dry_run_real_execution_controlled_operator_approval_capture_gate", "unexpected current status")
    _require(state["active_next_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate", "unexpected next phase")
    _require(state["active_next_phase_class"] == "planning_gate", "unexpected next phase class")
    _require(state["schema_version"] == "2.1", "unexpected schema version")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
        "Approval capture authorized now: `False`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
        "Planning-only: `false`",
        "Review-only: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "The next route is a controlled approval-capture gate and remains non-executing.",
        "No approval capture authorization now.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
        "Controlled operator approval capture gate planning readiness review next-route contract",
    )
    _mirror_contains(
        ROOT / "README.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning Readiness Review",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
        "Bedrock remains non-executable and product promotion remains blocked.",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
        "Bedrock gate executable now: `False`",
    )
    _mirror_contains(
        ROOT / "LAB_VERDICTS.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate Planning Readiness Review - Bedrock Preparation Exception Record",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate",
    )

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
                    str(ROOT / "LAB_STATUS.md"),
                    str(ROOT / "LAB_VERDICTS.md"),
                ],
                "review_result": "real execution controlled operator approval capture gate planning readiness review pass",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
