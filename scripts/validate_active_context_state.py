#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"

EXPECTED_PHASE = "ARIS Active-Context Transition Engine & Autonomous Loop Gate"
EXPECTED_PHASE_ID = "AC-TRANS-03"
EXPECTED_PREVIOUS_PHASE = "ARIS Active-Context Observability & Drift Prevention Gate"
EXPECTED_PREVIOUS_PHASE_ID = "AC-OBS-02"
EXPECTED_STATUS = "ac_trans_03_pass"
EXPECTED_DECISION = "pass"
EXPECTED_CURRENT_STATUS = "awaiting_manual_operator_authorization_for_next_phase"
EXPECTED_SCHEMA_VERSION = "2.3"

REQUIRED_BOOT_FILES = [
    "ACTIVE_CONTEXT_STATE.json",
    "ACTIVE_CONTEXT_SCHEMA.json",
    "ROADMAP_CANONICAL.md",
    "MANDATORY_READ_FIRST_RULES.md",
    "DECISION_LOCKS.md",
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
        _require(isinstance(value, dict) and segment in value, f"missing path: {dotted_path}")
        value = value[segment]
    return value


def _require_paths_match(state: dict[str, Any], paths: list[str], label: str) -> None:
    baseline_value = _value_at_path(state, paths[0])
    for other_path in paths[1:]:
        _require(_value_at_path(state, other_path) == baseline_value, f"{label} drift")


def _require_files_exist(state: dict[str, Any]) -> None:
    for relative_path in state["required_files_for_transition"]:
        _require((ROOT / relative_path).exists(), f"missing required transition file: {relative_path}")


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


def _check_next_phase_in_transition_table(state: dict[str, Any]) -> None:
    next_phase = state.get("next_phase")
    if next_phase is None:
        return
    roadmap_path = ROOT / "ROADMAP_CANONICAL.md"
    roadmap_text = roadmap_path.read_text(encoding="utf-8")
    in_table = False
    found = False
    for line in roadmap_text.split("\n"):
        if "## Transition Table" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("#"):
            break
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) >= 4 and cols[3] == next_phase:
            found = True
            break
    _require(found, f"BLOCK: next_phase '{next_phase}' not in Transition Table")


def _warn_boot_receipt(state: dict[str, Any]) -> None:
    boot = state.get("last_boot_files_read", [])
    if not isinstance(boot, list):
        print("WARN: last_boot_files_read is not a list", file=sys.stderr)
        return
    missing = [name for name in REQUIRED_BOOT_FILES if name not in boot]
    if missing:
        print(
            "WARN: last_boot_files_read is missing required boot files: " + ", ".join(missing)
            + " (Codex populates this; warning only, not blocking).",
            file=sys.stderr,
        )


def main() -> None:
    state = _load_json(STATE_PATH)
    _load_json(SCHEMA_PATH)

    _require(state["phase_id"] == EXPECTED_PHASE_ID, "unexpected phase_id")
    _require(state["current_phase_id"] == EXPECTED_PHASE_ID, "unexpected current_phase_id")
    _require(state["previous_phase_id"] == EXPECTED_PREVIOUS_PHASE_ID, "unexpected previous_phase_id")
    _require(state["status"] == EXPECTED_STATUS, "unexpected status")
    _require(state["decision"] == EXPECTED_DECISION, "unexpected decision")
    _require(state["latest_completed_phase"] == EXPECTED_PHASE, "unexpected latest completed phase")
    _require(state["current_status"] == EXPECTED_CURRENT_STATUS, "unexpected current status")
    _require(state["schema_version"] == EXPECTED_SCHEMA_VERSION, "unexpected schema version")
    _require(state["next_phase"] is None, "next_phase must be null")
    _require(state["active_next_phase"] is None, "active_next_phase must be null")
    _require(state["active_next_phase_class"] is None, "active_next_phase_class must be null")
    _require(state["next_phase_authorized_by_operator"] is False, "next phase must not be operator-authorized")
    _require(state["anti_proliferation_rule_active"] is True, "anti_proliferation_rule_active must be true")
    _require(state["ci_enforcement_active"] is True, "ci_enforcement_active must be true")

    _check_gate_ttl(state)
    _check_auto_advance(state)
    _check_next_phase_in_transition_table(state)

    policy = state["cross_field_consistency_policy"]
    _require_paths_match(state, policy["active_next_phase_must_match_across"], "active_next_phase")
    _require_paths_match(state, policy["current_status_must_match_across"], "current_status")
    _require_paths_match(state, policy["latest_completed_phase_must_match_across"], "latest_completed_phase")
    _require_paths_match(state, policy["status_must_match_across"], "status")

    _require(state["current_live_route"]["active_next_phase"] is None, "current live route next phase must be null")
    _require(state["current_live_route"]["active_next_phase_class"] is None, "current live route next phase class must be null")
    _require(state["current_live_route"]["current_status"] == EXPECTED_CURRENT_STATUS, "current live route status mismatch")
    _require(state["current_live_route"]["next_phase_execution_authorization"] is False, "next phase execution authorization must be false")

    _require(state["next_action"]["phase"] is None, "next_action.phase must be null")
    _require(state["next_action"]["phase_class"] is None, "next_action.phase_class must be null")
    _require(state["next_action"]["planning_only"] is False, "next_action.planning_only must be false")
    _require(state["next_action"]["review_only"] is False, "next_action.review_only must be false")
    _require(state["next_action"]["execution_authorization"] is False, "next_action.execution_authorization must be false")

    _require(state["locks"]["deferred_phase"] is None, "locks.deferred_phase must be null")
    _require(state["history_summary"]["previous_execution_phase"] == EXPECTED_PREVIOUS_PHASE, "unexpected previous execution phase")
    _require(state["last_transition"]["from_phase"] == EXPECTED_PREVIOUS_PHASE, "unexpected last transition from phase")
    _require(state["last_transition"]["to_phase"] == EXPECTED_PHASE, "unexpected last transition to phase")

    for key, value in state["authorization"].items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        else:
            _require(value is False, f"authorization flag {key} must be false")
    _require(state["authorization"].get("fixture_materialization_allowed", False) is False, "fixture materialization must remain unauthorized")

    _require_files_exist(state)

    _mirror_contains(
        ROOT / "CURRENT_STATE.md",
        "ACTIVE_CONTEXT_STATE.json wins",
        EXPECTED_STATUS,
        EXPECTED_PHASE_ID,
        "Next phase: `null`",
        "Anti-proliferation rule active: `true`",
        "CI enforcement active: `true`",
        "Gate cycles used: `0`",
        "Gate max cycles: `3`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Next phase: `null`",
        "Awaiting manual operator authorization.",
        "Execution authorization: `false`",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        EXPECTED_STATUS,
        "Deferred phase: `null`",
        "next_phase_authorized_by_operator=false",
        "No next phase is authorized.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "artifacts/ac_trans_03/decision.json",
        "artifacts/ac_trans_03/summary.json",
        "artifacts/ac_trans_03/report.md",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "AC-TRANS-03 | ARIS Active-Context Transition Engine & Autonomous Loop Gate | pass",
        EXPECTED_PREVIOUS_PHASE_ID,
    )
    _mirror_contains(
        ROOT / "README.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "validate_active_context.yml",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "Operator authorization required before any new phase.",
    )
    _mirror_contains(
        ROOT / "MANDATORY_READ_FIRST_RULES.md",
        "REGRA ANTI-PROLIFERAÇÃO DE GATES",
        "Gate que apenas reafirma locks do gate anterior é PROIBIDO.",
        "Planning e Review do mesmo passo colapsam em UM gate",
        "REGRA DE CICLO DE GATE",
        "REGRA DE AUTO-ADVANCE",
        "REGRA DE TRANSIÇÃO",
    )
    _mirror_contains(
        ROOT / "PROMPT_CONTRACT.md",
        "REGRA ANTI-PROLIFERAÇÃO DE GATES",
        "Toda resposta do revisor abre com SHA resolvido de origin/main lido naquele turno.",
        "Sem SHA citado: resposta é INVALID por construção.",
        "POST-COMMIT VERIFICATION",
        "The model never self-reports PASS. The CI reports PASS.",
    )

    fixture_assertion_path = ROOT / "scripts/assert_no_unauthorized_fixtures.py"
    workflow_path = ROOT / ".github/workflows/validate_active_context.yml"
    _require(fixture_assertion_path.read_text(encoding="utf-8") == EXPECTED_FIXTURE_ASSERTION, "unexpected fixture assertion script content")
    _require(workflow_path.read_text(encoding="utf-8") == EXPECTED_WORKFLOW, "unexpected workflow content")

    _warn_boot_receipt(state)

    print(json.dumps({
        "decision": "pass",
        "status": EXPECTED_STATUS,
        "phase_id": EXPECTED_PHASE_ID,
        "previous_phase_id": EXPECTED_PREVIOUS_PHASE_ID,
        "latest_completed_phase": EXPECTED_PHASE,
        "next_phase": None,
        "gate_opened_at": state["gate_opened_at"],
        "gate_max_cycles": state["gate_max_cycles"],
        "gate_cycles_used": state["gate_cycles_used"],
        "auto_advance_enabled": state["auto_advance"]["enabled"],
        "ci_enforcement_active": True,
        "anti_proliferation_rule_active": True
    }, indent=2))


if __name__ == "__main__":
    main()
