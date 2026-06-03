#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"

EXPECTED_PHASE = "ARIS Infernus Full Fixture Materialization Gate"
EXPECTED_PHASE_ID = "INF-MAT-01"
EXPECTED_PREVIOUS_PHASE = "ARIS Active-Context Circuit Breaker Gate"
EXPECTED_PREVIOUS_PHASE_ID = "AC-BREAK-05"
EXPECTED_STATUS = "inf_mat_01_pass"
EXPECTED_DECISION = "pass"
EXPECTED_CURRENT_STATUS = "awaiting_manual_operator_authorization_for_next_phase"
EXPECTED_SCHEMA_VERSION = "2.3"

GOVERNANCE_CLASSES = {
    "governance_repair", "observability",
    "transition_engine", "contract", "route"
}
CAPACITY_CLASSES = {
    "fixture_materialization", "bot_execution",
    "minos_verdict", "purgatorium", "benchux",
    "crisol", "bedrock", "product"
}

PHASE_DELIVERABLES = {
    "INF-MAT-01": lambda: (
        pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full").exists()
        and len(list(pathlib.Path(
            "fixtures/lab_simulation/aris_infernus_lab_full"
        ).iterdir())) >= 13
    ),
}

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


def _check_minimum_deliverable(state: dict[str, Any]) -> None:
    phase_id = state.get("current_phase_id", "")
    decision = state.get("decision", "")
    if decision != "pass":
        return
    if phase_id not in PHASE_DELIVERABLES:
        return
    if not PHASE_DELIVERABLES[phase_id]():
        print(f"BLOCK: {phase_id} declared pass but minimum_deliverable not met")
        sys.exit(1)


def _check_governance_streak(state: dict[str, Any]) -> None:
    streak = state.get("governance_gate_streak", 0)
    phase_class = state.get("phase_class", "")
    if phase_class not in GOVERNANCE_CLASSES:
        return
    if streak >= 3:
        print("BLOCK: governance_gate_streak >= 3.")
        print("3 governance gates consecutivos sem capacidade real.")
        print("Proximo gate obrigatorio: classe de capacidade.")
        print("Operador deve autorizar explicitamente.")
        sys.exit(1)
    if streak == 2:
        print(f"WARN: governance_gate_streak=2. Proximo gate DEVE ser capacidade.")


def _check_gate_signature(state: dict[str, Any]) -> str:
    phase_class = state.get("phase_class", "")
    locks = state.get("authorization", {})
    sig = hashlib.sha256(
        json.dumps(
            {"phase_class": phase_class, "locks": locks},
            sort_keys=True
        ).encode()
    ).hexdigest()[:16]
    seen = state.get("seen_gate_signatures", [])
    if sig in seen:
        print(f"BLOCK: gate signature {sig} ja executado anteriormente.")
        print("Este gate nao produz estado novo. Proibido repetir.")
        sys.exit(1)
    return sig


def _check_cycle_nudge(state: dict[str, Any]) -> None:
    cycles = state.get("gate_cycles_used", 0)
    max_c = state.get("gate_max_cycles", 3)
    if cycles >= max_c - 1:
        print(f"WARN: gate_cycles_used={cycles}/{max_c}.")
        print("Proximo ciclo bloqueia. Emita veredicto terminal agora.")


def _apply_streak_management(state: dict[str, Any], sig: str, decision: str) -> None:
    """Update streak and signature tracking based on phase_class and decision."""
    phase_class = state.get("phase_class", "")
    if decision != "pass":
        return
    if phase_class in CAPACITY_CLASSES:
        state["governance_gate_streak"] = 0
    elif phase_class in GOVERNANCE_CLASSES:
        state["governance_gate_streak"] = state.get("governance_gate_streak", 0) + 1
    if "seen_gate_signatures" not in state:
        state["seen_gate_signatures"] = []
    state["seen_gate_signatures"].append(sig)


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


def _check_fixture_materialization(state: dict[str, Any]) -> None:
    """INF-MAT-01 specific: verify fixture count and evidence_ref hashes."""
    fixture_count = state.get("fixture_count", 0)
    scenario_count = state.get("scenario_count", 0)
    _require(fixture_count == 65, f"fixture_count must be 65, got {fixture_count}")
    _require(scenario_count == 13, f"scenario_count must be 13, got {scenario_count}")
    _require(state.get("fixture_materialization_executed") is True, "fixture_materialization_executed must be true")
    _require(state.get("governance_gate_streak") == 0, "governance_gate_streak must be 0 after capacity gate pass")

    root = ROOT / "fixtures/lab_simulation/aris_infernus_lab_full"
    _require(root.exists(), "fixtures/lab_simulation/aris_infernus_lab_full must exist")
    dirs = [d for d in root.iterdir() if d.is_dir()]
    _require(len(dirs) >= 13, f"expected >= 13 scenario dirs, found {len(dirs)}")

    null_hashes = []
    for ref_path in sorted(root.rglob("evidence_ref.json")):
        data = json.loads(ref_path.read_text(encoding="utf-8"))
        if data.get("hash") is None:
            null_hashes.append(ref_path.parent.name)
    if null_hashes:
        print(f"BLOCK: evidence_ref.json with null hash in: {null_hashes}")
        sys.exit(1)


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

    # Circuit breaker fields
    _require("governance_gate_streak" in state, "governance_gate_streak must be present")
    _require("seen_gate_signatures" in state, "seen_gate_signatures must be present")
    _require("phase_class" in state, "phase_class must be present")

    _check_gate_ttl(state)
    _check_auto_advance(state)
    _check_next_phase_in_transition_table(state)
    _check_minimum_deliverable(state)

    # Three-layer circuit breaker (fixture_materialization not in GOVERNANCE_CLASSES, streak check is a no-op here)
    _check_governance_streak(state)
    sig = _check_gate_signature(state)
    _check_cycle_nudge(state)

    # INF-MAT-01 specific checks
    _check_fixture_materialization(state)

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

    # Authorization: fixture_materialization_allowed must be true; all others false
    auth = state["authorization"]
    for key, value in auth.items():
        if key == "network_authorized_scope":
            _require(value == "github_active_context_governance_only", "unexpected network scope")
        elif key == "fixture_materialization_allowed":
            _require(value is True, "fixture_materialization_allowed must be true for INF-MAT-01")
        else:
            _require(value is False, f"authorization flag {key} must be false")

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
        "governance_gate_streak: `0`",
        "fixture_materialization_executed: `true`",
        "scenario_count: `13`",
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
        "governance_gate_streak=0",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "artifacts/inf_mat_01/decision.json",
        "artifacts/inf_mat_01/summary.json",
        "artifacts/inf_mat_01/report.md",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "INF-MAT-01 | ARIS Infernus Full Fixture Materialization Gate | pass",
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
        "REGRA DE ENTREGÁVEL MÍNIMO",
        "REGRA DE TRANSIÇÃO",
        "REGRA DE CIRCUIT BREAKER",
        "governance_gate_streak",
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

    # Apply streak management (in-memory only — Codex writes back to JSON on next run)
    _apply_streak_management(state, sig, EXPECTED_DECISION)

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
        "governance_gate_streak": state.get("governance_gate_streak", 0),
        "phase_class": state.get("phase_class", ""),
        "fixture_count": state.get("fixture_count", 0),
        "scenario_count": state.get("scenario_count", 0),
        "auto_advance_enabled": state["auto_advance"]["enabled"],
        "ci_enforcement_active": True,
        "anti_proliferation_rule_active": True,
        "fixture_materialization_executed": state.get("fixture_materialization_executed", False),
    }, indent=2))


if __name__ == "__main__":
    main()
