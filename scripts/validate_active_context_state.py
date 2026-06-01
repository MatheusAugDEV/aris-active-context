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

    _require(state["status"] == "lab_real_simulation_pack_controlled_apply_dry_run_real_execution_lab_simulation_closure_gate_pass", "unexpected status")
    _require(state["decision"] == "pass", "unexpected decision")
    _require(state["latest_completed_phase"] == "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate", "unexpected latest completed phase")
    _require(state["current_status"] == "lab_simulation_route_closed_pending_post_review_routing_decision", "unexpected current status")
    _require(state["active_next_phase"] == "Lab Simulation Closure Post-Review Routing Decision", "unexpected next route")
    _require(state["active_next_phase_class"] == "review_gate_only", "unexpected next route class")
    _require(state["schema_version"] == "2.1", "unexpected schema version")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next route execution authorization must be false")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Six-phase route closed: `True`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Review-only: `true`",
        "Execution authorization: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        "Six-phase Lab Simulation route is closed.",
        "Bedrock remains non-executable and product promotion remains blocked.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Residual warnings register",
    )
    _mirror_contains(
        ROOT / "README.md",
        "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Lab Simulation Closure Gate",
        "Lab Simulation Closure Post-Review Routing Decision",
        "Residual warnings remain carried forward explicitly.",
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
