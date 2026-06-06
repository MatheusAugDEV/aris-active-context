#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PROJECT_MIRROR_ROOT = ROOT / "project_mirror"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"


def _resolve_project_relative(*parts: str) -> pathlib.Path:
    relative = pathlib.Path(*parts)
    for base in (PROJECT_ROOT, PROJECT_MIRROR_ROOT):
        candidate = base / relative
        if candidate.exists():
            return candidate
    return PROJECT_ROOT / relative


ACB_CORE_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_01_project_evidence_2026_06_03.json"
ACB_CORE_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_02_project_evidence_2026_06_03.json"
ACB_CAP_01_OPERATOR_AUTH_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_operator_authorization_2026_06_03.json"
ACB_CAP_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_01_project_evidence_2026_06_03.json"
ACB_CAP_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_02_project_evidence_2026_06_03.json"
ACB_CAP_03_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_03_project_evidence_2026_06_03.json"
ACB_CAP_04_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_04_project_evidence_2026_06_03.json"
ACB_CAP_05_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_evidence_2026_06_05.json"
ACB_CAP_05_RESYNC_PATH = ROOT / "artifacts" / "decisions" / "acb_cap_05_project_sha_resync_2026_06_06.json"
OPERATOR_PREFERENCES_PATH = ROOT / "OPERATOR_PREFERENCES.md"

EXPECTED_PHASE = "ARIS Infernus FULL Chain Registration & Preparation Opening"
EXPECTED_PHASE_ID = "INF-FULL-03"
EXPECTED_PREVIOUS_PHASE = "ARIS Infernus FULL Baseline Freeze Planning"
EXPECTED_PREVIOUS_PHASE_ID = "INF-FULL-02"
EXPECTED_STATUS = "inf_full_03_chain_registration_opening_pass"
EXPECTED_DECISION = "pass"
EXPECTED_CURRENT_STATUS = "inf_full_chain_registered_preparation_open_no_execution"
EXPECTED_SCHEMA_VERSION = "2.5"
INF_FULL_02_PHASE = "ARIS Infernus FULL Baseline Freeze Planning"
INF_FULL_02_STATUS = "inf_full_02_baseline_freeze_planning_pass"
ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA = "973d49a24d58d4166acb95b40611be409c5d44df"
ACB_CAP_05_RESYNC_NEW_PROJECT_SHA = "fa8546f35ae826f8cc254d51b77ba1ea704d0a27"
ACB_CAP_05_PROJECT_DECISION_SHA = "51f1416f83e8ed488031210de688ffb5856ea004"
ACB_CAP_05_ADVANCED_SUPPLY_CHAIN_CI_URL = "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/27052210325"
INF_FULL_01_SCOPE_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_scope_charter_decision_2026_06_06.json")
INF_FULL_01_SCOPE_MATRIX_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_scope_matrix_2026_06_06.json")
INF_FULL_01_SCOPE_MANIFEST_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_01_module_scope_manifest_2026_06_06.json")
INF_FULL_01_SCOPE_CHARTER_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_01_scope_charter_2026_06_06.md")
INF_FULL_02_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_planning_decision_2026_06_06.json")
INF_FULL_02_INVENTORY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_inventory_2026_06_06.json")
INF_FULL_02_HASH_MANIFEST_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_hash_manifest_2026_06_06.json")
INF_FULL_02_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_02_baseline_freeze_summary_2026_06_06.json")
INF_FULL_02_PLANNING_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_02_baseline_freeze_planning_2026_06_06.md")
INFERNUS_FULL_CANONROADMAP_PATH = _resolve_project_relative("docs", "infernus_full", "infernus_full_canonroadmap.md")
INFERNUS_FULL_SUPERSESSION_PATH = _resolve_project_relative("artifacts", "infernus", "infernus_full_canonroadmap_supersession_2026_06_06.json")
INF_FULL_03_DECISION_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_03_opening_decision_2026_06_06.json")
INF_FULL_03_SUMMARY_PATH = _resolve_project_relative("artifacts", "infernus", "inf_full_03_opening_summary_2026_06_06.json")
INF_FULL_03_OPENING_DOC_PATH = _resolve_project_relative("docs", "infernus_full", "inf_full_03_opening_2026_06_06.md")
INFERNUS_FULL_DOCS_README_PATH = _resolve_project_relative("docs", "infernus_full", "README.md")
IF00_TRANSITION_CANDIDATE_PATH = _resolve_project_relative("artifacts", "infernus", "if00_transition_candidate.json")
IF00_HERMETICITY_PATH = _resolve_project_relative("artifacts", "infernus", "if00_lab_hermeticity_baseline.json")
IF01_LEDGER_PATH = _resolve_project_relative("artifacts", "infernus", "if01_research_evidence_ledger.jsonl")
IF02_ONTOLOGY_PATH = _resolve_project_relative("artifacts", "infernus", "if02_threat_ontology_v4.json")
IF02_COVERAGE_PATH = _resolve_project_relative("artifacts", "infernus", "if02_coverage_matrix_v4.csv")
IF03_ORACLE_PACK_PATH = _resolve_project_relative("artifacts", "infernus", "if03_oracle_metrics_contract_pack.json")
IF04_BOT_PACK_PATH = _resolve_project_relative("artifacts", "infernus", "if04_bot_contract_pack_v4.json")
IF04_PERMISSION_PATH = _resolve_project_relative("artifacts", "infernus", "if04_permission_manifest_v4.json")

GOVERNANCE_CLASSES = {
    "governance_repair", "observability",
    "transition_engine", "contract", "route"
}
CAPACITY_CLASSES = {
    "fixture_materialization", "bot_execution",
    "minos_verdict", "purgatorium", "benchux",
    "crisol", "bedrock", "product", "capability_build"
}

PHASE_DELIVERABLES = {
    "INF-MAT-01": lambda: (
        pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full").exists()
        and len(list(pathlib.Path(
            "fixtures/lab_simulation/aris_infernus_lab_full"
        ).iterdir())) >= 13
    ),
    "INF-BOT-01": lambda: (
        pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/inf_bot_01/nemesis_execution_log.json").read_text(encoding="utf-8")
            ).get("log_sha256")
        )
    ),
    "INF-MINOS-01": lambda: (
        pathlib.Path("artifacts/inf_minos_01/minos_verdict.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/inf_minos_01/minos_verdict.json").read_text(encoding="utf-8")
            ).get("minos_verdict_sha256")
        )
    ),
    "PURG-01": lambda: (
        pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").exists()
        and bool(
            json.loads(
                pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").read_text(encoding="utf-8")
            ).get("severity")
        )
        and bool(
            json.loads(
                pathlib.Path("artifacts/purg_01/finding_nemesis_validator_bypass.json").read_text(encoding="utf-8")
            ).get("status")
        )
    ),
    "ACB-CORE-01": lambda: (
        ACB_CORE_01_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CORE_01_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CORE_01_EVIDENCE_PATH).get("supply_chain_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CORE_01_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "uv_lock_exists",
                "pip_audit_gate_exists",
                "sbom_exists",
                "uv_bootstrap_exists",
            ]
        )
    ),
    "ACB-CORE-02": lambda: (
        ACB_CORE_02_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CORE_02_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CORE_02_EVIDENCE_PATH).get("core_public_api_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CORE_02_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "research_basis_exists",
                "snapshot_before_exists",
                "snapshot_after_exists",
                "import_stability_report_exists",
                "explicit_all_created_or_verified",
                "protocols_created_or_verified",
            ]
        )
    ),
    "ACB-CAP-01": lambda: (
        ACB_CAP_01_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_01_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_01_EVIDENCE_PATH).get("backend_baseline_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_01_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "fastapi_app_exists",
                "health_check_exists",
                "ready_check_exists",
                "jwt_auth_exists",
                "api_key_auth_exists",
                "tenant_isolation_exists",
                "slowapi_rate_limit_exists",
                "backend_tests_exist",
                "backend_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-02": lambda: (
        ACB_CAP_02_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_02_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_02_EVIDENCE_PATH).get("mcp_runtime_sandbox_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_02_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "mcp_runtime_package_exists",
                "stdio_ban_exists",
                "sandbox_spec_exists",
                "policy_pre_dispatch_exists",
                "kill_switch_exists",
                "rollback_contract_exists",
                "audit_event_exists",
                "mcp_runtime_tests_exist",
                "mcp_runtime_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-03": lambda: (
        ACB_CAP_03_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_03_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_03_EVIDENCE_PATH).get("runtime_public_api_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_03_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "runtime_package_exists",
                "runtime_public_api_documented",
                "runtime_public_api_contract_exists",
                "runtime_facade_exists",
                "runtime_modes_enforced",
                "runtime_policy_bridge_exists",
                "runtime_audit_hashing_exists",
                "public_api_drift_ratified",
                "runtime_tests_exist",
                "runtime_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-04": lambda: (
        ACB_CAP_04_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_04_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_04_EVIDENCE_PATH).get("product_pilot_boundary_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_04_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "product_boundary_package_exists",
                "pilot_gates_defined",
                "five_binary_gates_defined",
                "lab_to_staging_to_pilot_workflow_defined",
                "pilot_scope_contract_exists",
                "evidence_bundle_contract_exists",
                "pilot_runbook_contract_exists",
                "pilot_risk_matrix_exists",
                "non_authorization_statement_exists",
                "product_pilot_tests_exist",
                "product_pilot_artifacts_exist",
            ]
        )
    ),
    "ACB-CAP-05": lambda: (
        ACB_CAP_05_EVIDENCE_PATH.exists()
        and bool(_load_json(ACB_CAP_05_EVIDENCE_PATH).get("project_sha"))
        and _load_json(ACB_CAP_05_EVIDENCE_PATH).get("advanced_supply_chain_ci", {}).get("conclusion") == "success"
        and all(
            _load_json(ACB_CAP_05_EVIDENCE_PATH).get("deliverables", {}).get(key) is True
            for key in [
                "supply_chain_package_exists",
                "sbom_integrity_checker_exists",
                "sbom_integrity_report_exists",
                "attestation_envelope_exists",
                "offline_signature_test_verification_exists",
                "pypi_vulnerability_range_monitor_exists",
                "pypi_vulnerability_range_scan_exists",
                "aibom_prototype_exists",
                "infernus_full_spec_exists",
                "advanced_supply_chain_tests_exist",
                "advanced_supply_chain_artifacts_exist",
            ]
        )
    ),
    "INF-FULL-01": lambda: (
        True if not all(
            path.exists()
            for path in [
                INF_FULL_01_SCOPE_DECISION_PATH,
                INF_FULL_01_SCOPE_MATRIX_PATH,
                INF_FULL_01_SCOPE_MANIFEST_PATH,
                INF_FULL_01_SCOPE_CHARTER_PATH,
            ]
        ) else (
            _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("inf_full_opened") is True
            and _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("bots_executed") is False
            and _load_json(INF_FULL_01_SCOPE_DECISION_PATH).get("runtime_execution_authorized") is False
            and _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH).get("all_modules_accounted_for") is True
            and _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH).get("unresolved_modules") == []
        )
    ),
    "INF-FULL-02": lambda: (
        all(
            path.exists()
            for path in [
                INF_FULL_02_DECISION_PATH,
                INF_FULL_02_INVENTORY_PATH,
                INF_FULL_02_HASH_MANIFEST_PATH,
                INF_FULL_02_SUMMARY_PATH,
                INF_FULL_02_PLANNING_DOC_PATH,
            ]
        )
        and _load_json(INF_FULL_02_DECISION_PATH).get("minimum_deliverable_met") is True
        and _load_json(INF_FULL_02_DECISION_PATH).get("baseline_freeze_planned") is True
        and _load_json(INF_FULL_02_DECISION_PATH).get("baseline_freeze_applied") is False
        and _load_json(INF_FULL_02_SUMMARY_PATH).get("question_6_next_phase_after_inf_full_02", {}).get("canonical_next_phase") is None
    ),
    "INF-FULL-03": lambda: (
        all(
            path.exists()
            for path in [
                INFERNUS_FULL_CANONROADMAP_PATH,
                IF00_TRANSITION_CANDIDATE_PATH,
                IF00_HERMETICITY_PATH,
                IF01_LEDGER_PATH,
                IF02_ONTOLOGY_PATH,
                IF02_COVERAGE_PATH,
                IF03_ORACLE_PACK_PATH,
                IF04_BOT_PACK_PATH,
                IF04_PERMISSION_PATH,
            ]
        )
        and _load_json(IF00_TRANSITION_CANDIDATE_PATH).get("candidate_transition", {}).get("to_phase_id") == "INF-FULL-03"
        and _load_json(IF00_HERMETICITY_PATH).get("hermeticity_contract", {}).get("bots_may_run") is False
        and _load_json(IF03_ORACLE_PACK_PATH).get("planning_only") is True
        and _load_json(IF04_PERMISSION_PATH).get("capability_guards", {}).get("bot_execution_allowed") is False
    ),
}

REQUIRED_BOOT_FILES = [
    "ACTIVE_CONTEXT_STATE.json",
    "AGENT_IDENTITY.md",
    "ACTIVE_CONTEXT_SCHEMA.json",
    "scripts/validate_active_context_state.py",
    "ROADMAP_CANONICAL.md",
    "MANDATORY_READ_FIRST_RULES.md",
    "CURRENT_STATE.md",
    "NEXT_ACTION.md",
    "DECISION_LOCKS.md",
    "OPERATOR_PREFERENCES.md",
    "CONTEXT_INDEX.md",
    "ARIS_PHASE_LEDGER.md",
    "README.md",
    "PROMPT_CONTRACT.md",
    "LAB_OPERATING_CONTRACT.md",
]

EXPECTED_PRIORITY_READ_ORDER = [
    "1. ACTIVE_CONTEXT_STATE.json",
    "2. AGENT_IDENTITY.md",
    "3. ACTIVE_CONTEXT_SCHEMA.json",
    "4. scripts/validate_active_context_state.py",
    "5. ROADMAP_CANONICAL.md",
    "6. MANDATORY_READ_FIRST_RULES.md",
    "7. CURRENT_STATE.md",
    "8. NEXT_ACTION.md",
    "9. DECISION_LOCKS.md",
    "10. OPERATOR_PREFERENCES.md",
    "11. CONTEXT_INDEX.md",
    "12. ARIS_PHASE_LEDGER.md",
    "13. README.md",
    "14. PROMPT_CONTRACT.md",
    "15. LAB_OPERATING_CONTRACT.md",
]

OPERATOR_PREFERENCE_REQUIRED_PHRASES = [
    "operator sends a Codex result",
    "ritual phrase",
    "must not ask for confirmation just to send the next Codex prompt",
    "advance_mode=prompt_only",
    "ACTIVE_CONTEXT_STATE.json",
    "cannot override",
    "advance_mode=operator",
    "next_phase remains `null`",
    "ACB-CAP-05",
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


def _ordered_positions(items: list[str], required: list[str], label: str) -> list[int]:
    missing = [item for item in required if item not in items]
    _require(not missing, f"{label} missing required entries: {missing}")
    positions = [items.index(item) for item in required]
    _require(positions == sorted(positions), f"{label} has out-of-order entries for required list")
    return positions


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


def _canonical_hash_without_field(data: dict[str, Any], field: str) -> str:
    payload = dict(data)
    payload.pop(field, None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _require_paths_match(state: dict[str, Any], paths: list[str], label: str) -> None:
    baseline_value = _value_at_path(state, paths[0])
    for other_path in paths[1:]:
        _require(_value_at_path(state, other_path) == baseline_value, f"{label} drift")


def _require_files_exist(state: dict[str, Any]) -> None:
    for relative_path in state["required_files_for_transition"]:
        resolved = ROOT / relative_path
        if relative_path.startswith("../") and not resolved.exists():
            continue
        _require(resolved.exists(), f"missing required transition file: {relative_path}")


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


def _preference_allows_direct_prompt(
    *,
    advance_mode: str,
    previous_phase_pass: bool,
    ci_green: bool,
    validator_green: bool,
    manual_authorization_required: bool,
) -> bool:
    return (
        advance_mode == "prompt_only"
        and previous_phase_pass
        and ci_green
        and validator_green
        and not manual_authorization_required
    )


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
    boot_files = state.get("last_boot_files_read", [])
    missing = [f for f in REQUIRED_BOOT_FILES if f not in boot_files]
    if missing:
        print(f"BLOCK: last_boot_files_read missing: {missing}")
        print("Codex must populate last_boot_files_read before any action.")
        sys.exit(1)
    try:
        _ordered_positions(boot_files, REQUIRED_BOOT_FILES, "last_boot_files_read")
    except SystemExit as exc:
        print(f"BLOCK: {exc}")
        print("Codex must preserve the mandatory read-first order in last_boot_files_read.")
        sys.exit(1)


def _check_operator_preferences_contract(state: dict[str, Any]) -> None:
    _require(OPERATOR_PREFERENCES_PATH.exists(), "missing OPERATOR_PREFERENCES.md")

    priority_read_order = state.get("anti_corruption_contract", {}).get("canonical_read_order", [])
    _require(
        priority_read_order[: len(EXPECTED_PRIORITY_READ_ORDER)] == EXPECTED_PRIORITY_READ_ORDER,
        "canonical_read_order does not match expected operator-priority read order",
    )
    _require(
        "OPERATOR_PREFERENCES.md" in state.get("required_files_for_transition", []),
        "required_files_for_transition must include OPERATOR_PREFERENCES.md",
    )

    text = OPERATOR_PREFERENCES_PATH.read_text(encoding="utf-8")
    for phrase in OPERATOR_PREFERENCE_REQUIRED_PHRASES:
        _require(phrase in text, f"OPERATOR_PREFERENCES.md missing required phrase: {phrase}")

    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is True,
        "prompt_only direct-prompt preference logic must allow clean prompt emission",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="operator",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "operator advance_mode must never be authorized by prompt preference",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=True,
        ) is False,
        "manual authorization lock must override prompt emission preference",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=False,
            ci_green=True,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass canonical pass requirement",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=False,
            validator_green=True,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass green CI requirement",
    )
    _require(
        _preference_allows_direct_prompt(
            advance_mode="prompt_only",
            previous_phase_pass=True,
            ci_green=True,
            validator_green=False,
            manual_authorization_required=False,
        ) is False,
        "prompt emission preference must not bypass green validator requirement",
    )
    _require(state.get("next_phase") is None, "operator preference must not auto-open next_phase")
    _require(
        state.get("next_phase_authorized_by_operator") is False,
        "operator preference must not self-authorize next phase",
    )
    auth = state.get("authorization", {})
    for key in [
        "production_authorized",
        "product_ready",
        "real_apply_authorized",
        "runtime_integration_allowed",
        "secrets_access_authorized",
        "external_llm_api_authorized",
    ]:
        _require(auth.get(key) is False, f"operator preference must not override safety lock: {key}")


def _check_acb_core_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CORE_01_EVIDENCE_PATH.exists(), "missing ACB-CORE-01 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CORE_01_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CORE-01", "ACB evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB evidence repository mismatch")
    _require(evidence_data.get("project_sha") == "0e935f41830101c391905611473e52e883d36a26", "ACB evidence project_sha mismatch")
    _require(evidence_data.get("supply_chain_ci", {}).get("conclusion") == "success", "ACB evidence supply-chain CI must be success")
    _require(
        evidence_data.get("supply_chain_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26916868686",
        "ACB evidence supply-chain CI URL mismatch",
    )
    for key in [
        "uv_lock_exists",
        "pip_audit_gate_exists",
        "sbom_exists",
        "pyproject_exists",
        "validation_runner_exists",
        "test_exists",
        "uv_bootstrap_exists",
    ]:
        _require(evidence_data.get("deliverables", {}).get(key) is True, f"ACB evidence deliverable {key} must be true")
    _require(evidence_data.get("local_validation", {}).get("pass_criteria_met") is True, "ACB evidence pass_criteria_met must be true")
    _require(evidence_data.get("local_validation", {}).get("uv_version") == "0.11.18", "ACB evidence uv_version mismatch")

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_core_01"
    required_paths = [
        PROJECT_ROOT / "pyproject.toml",
        PROJECT_ROOT / "uv.lock",
        PROJECT_ROOT / ".github" / "workflows" / "supply-chain-baseline.yml",
        PROJECT_ROOT / "scripts" / "run_acb_core_01_supply_chain_validation.py",
        PROJECT_ROOT / "tests" / "test_acb_core_01_supply_chain.py",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
        artifacts_root / "dependency_inventory.json",
        artifacts_root / "sbom.cdx.json",
        artifacts_root / "supply_chain_validation.json",
        artifacts_root / "uv_bootstrap.json",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CORE-01 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    inventory_data = _load_json(artifacts_root / "dependency_inventory.json")
    sbom_data = _load_json(artifacts_root / "sbom.cdx.json")
    validation_data = _load_json(artifacts_root / "supply_chain_validation.json")
    bootstrap_data = _load_json(artifacts_root / "uv_bootstrap.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "supply-chain-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CORE-01", "ACB decision phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "PURG-01", "ACB decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "ACB decision must be pass")
    _require(decision_data.get("status") == "acb_core_01_pass", "ACB decision status mismatch")
    _require(decision_data.get("phase_class") == "capability_build", "ACB decision phase_class mismatch")
    _require(decision_data.get("uv_available") is True, "ACB decision uv_available must be true")
    _require(decision_data.get("uv_bootstrap_created") is True, "ACB decision uv_bootstrap_created must be true")
    _require(decision_data.get("uv_lock_created_or_verified") is True, "ACB decision uv_lock_created_or_verified must be true")
    _require(decision_data.get("pip_audit_gate_created_or_verified") is True, "ACB decision pip_audit_gate_created_or_verified must be true")
    _require(decision_data.get("cyclonedx_sbom_created_or_verified") is True, "ACB decision cyclonedx_sbom_created_or_verified must be true")
    _require(decision_data.get("pass_criteria_met") is True, "ACB decision pass_criteria_met must be true")
    _require(decision_data.get("next_phase") is None, "ACB decision next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "ACB decision must not authorize next phase")

    _require(summary_data.get("phase_id") == "ACB-CORE-01", "ACB summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB summary decision must be pass")
    _require(summary_data.get("status") == "acb_core_01_pass", "ACB summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB summary minimum_deliverable_met must be true")

    _require(inventory_data.get("uv_available") is True, "ACB inventory uv_available must be true")
    _require(inventory_data.get("pyproject_present") is True, "ACB inventory pyproject_present must be true")
    _require(inventory_data.get("lockfile_after") == "uv.lock", "ACB inventory lockfile_after must be uv.lock")
    _require(inventory_data.get("supply_chain_tools_detected", {}).get("uv_binary") is True, "ACB inventory must record uv binary")

    _require(sbom_data.get("bomFormat") == "CycloneDX", "ACB SBOM bomFormat must be CycloneDX")
    _require(sbom_data.get("generation_mode") in {"tool_generated", "deterministic_minimal"}, "ACB SBOM generation_mode invalid")

    _require(validation_data.get("uv_lock_exists") is True, "ACB validation uv_lock_exists must be true")
    _require(validation_data.get("pip_audit_gate_exists") is True, "ACB validation pip_audit_gate_exists must be true")
    _require(validation_data.get("sbom_exists") is True, "ACB validation sbom_exists must be true")
    _require(validation_data.get("pass_criteria_met") is True, "ACB validation pass_criteria_met must be true")

    _require(bootstrap_data.get("uv_available_after") is True, "ACB bootstrap uv_available_after must be true")
    _require(bootstrap_data.get("bootstrap_result") == "success", "ACB bootstrap_result must be success")
    _require(bool(bootstrap_data.get("uv_version_after")), "ACB bootstrap must record uv version")

    _require("uv lock --check" in workflow_text, "supply-chain workflow must check uv lock freshness")
    _require("pip-audit" in workflow_text, "supply-chain workflow must include pip-audit gate")


def _check_acb_core_02_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CORE_02_EVIDENCE_PATH.exists(), "missing ACB-CORE-02 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CORE_02_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CORE-02 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "46910e0fda3fc64a19818ad80f39813227b53922",
        "ACB-CORE-02 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("core_public_api_ci", {}).get("conclusion") == "success",
        "ACB-CORE-02 evidence core-public-api CI must be success",
    )
    _require(
        evidence_data.get("core_public_api_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26917991639",
        "ACB-CORE-02 evidence core-public-api CI URL mismatch",
    )
    for key in [
        "research_basis_exists",
        "snapshot_before_exists",
        "snapshot_after_exists",
        "import_stability_report_exists",
        "explicit_all_created_or_verified",
        "protocols_created_or_verified",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CORE-02 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CORE-02 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("package_root_detected") == "src/aris",
        "ACB-CORE-02 evidence package_root_detected mismatch",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_core_02"
    required_paths = [
        PROJECT_ROOT / "src" / "aris" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "contracts.py",
        PROJECT_ROOT / ".github" / "workflows" / "core-public-api-baseline.yml",
        PROJECT_ROOT / "scripts" / "run_acb_core_02_public_api_snapshot.py",
        PROJECT_ROOT / "tests" / "test_acb_core_02_public_api.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "public_api_snapshot_before.json",
        artifacts_root / "public_api_snapshot_after.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CORE-02 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    snapshot_before = _load_json(artifacts_root / "public_api_snapshot_before.json")
    snapshot_after = _load_json(artifacts_root / "public_api_snapshot_after.json")
    report_data = _load_json(artifacts_root / "import_stability_report.json")
    init_text = (PROJECT_ROOT / "src" / "aris" / "__init__.py").read_text(encoding="utf-8")
    contracts_text = (PROJECT_ROOT / "src" / "aris" / "contracts.py").read_text(encoding="utf-8")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "core-public-api-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 decision phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "ACB-CORE-01", "ACB-CORE-02 decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CORE-02 decision must be pass")
    _require(decision_data.get("status") == "acb_core_02_pass", "ACB-CORE-02 decision status mismatch")
    _require(decision_data.get("phase_class") == "capability_build", "ACB-CORE-02 decision phase_class mismatch")
    _require(decision_data.get("explicit_all_created_or_verified") is True, "ACB-CORE-02 decision explicit_all_created_or_verified must be true")
    _require(decision_data.get("protocols_created_or_verified") is True, "ACB-CORE-02 decision protocols_created_or_verified must be true")
    _require(decision_data.get("import_smoke_tests_passed") is True, "ACB-CORE-02 decision import_smoke_tests_passed must be true")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CORE-02 decision pass_criteria_met must be true")
    _require(decision_data.get("next_phase") is None, "ACB-CORE-02 decision next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "ACB-CORE-02 decision must not authorize next phase")

    _require(summary_data.get("phase_id") == "ACB-CORE-02", "ACB-CORE-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CORE-02 summary decision must be pass")
    _require(summary_data.get("status") == "acb_core_02_pass", "ACB-CORE-02 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CORE-02 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CORE-02 summary minimum_deliverable_met must be true")

    _require(snapshot_before.get("package_root_detected") == "src/aris", "ACB-CORE-02 snapshot_before package_root_detected mismatch")
    _require(snapshot_after.get("package_root_detected") == "src/aris", "ACB-CORE-02 snapshot_after package_root_detected mismatch")
    _require(snapshot_before.get("exported_all_symbols") == [], "ACB-CORE-02 snapshot_before exported_all_symbols must be empty")
    _require(bool(snapshot_after.get("exported_all_symbols")), "ACB-CORE-02 snapshot_after exported_all_symbols must be non-empty")
    _require("contracts" in snapshot_after.get("exported_all_symbols", []), "ACB-CORE-02 snapshot_after must export contracts")
    _require("CommandPolicyProtocol" in snapshot_after.get("exported_all_symbols", []), "ACB-CORE-02 snapshot_after must export Protocols")

    _require(report_data.get("import_smoke_tests_executed") is True, "ACB-CORE-02 import report must execute smoke tests")
    _require(report_data.get("import_smoke_tests_passed") is True, "ACB-CORE-02 import report must pass smoke tests")
    _require(report_data.get("pass_criteria_met") is True, "ACB-CORE-02 import report pass_criteria_met must be true")
    _require("contracts" in report_data.get("modules_tested", []), "ACB-CORE-02 import report must test contracts")

    _require("__all__" in init_text, "ACB-CORE-02 root __init__ must define __all__")
    _require("Protocol" in contracts_text, "ACB-CORE-02 contracts must define Protocols")
    _require("python -m pip install pytest" in workflow_text, "ACB-CORE-02 workflow must install pytest")


def _check_acb_cap_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_01_OPERATOR_AUTH_PATH.exists(), "missing ACB-CAP-01 operator authorization artifact in active-context")
    _require(ACB_CAP_01_EVIDENCE_PATH.exists(), "missing ACB-CAP-01 evidence artifact in active-context")

    operator_auth = _load_json(ACB_CAP_01_OPERATOR_AUTH_PATH)
    _require(operator_auth.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 operator authorization phase_id mismatch")
    _require(operator_auth.get("operator") == "MatheusAugDEV", "ACB-CAP-01 operator authorization operator mismatch")
    _require(operator_auth.get("authorized") is True, "ACB-CAP-01 operator authorization must be true")
    _require(operator_auth.get("constraints", {}).get("next_phase_must_remain_null") is True, "ACB-CAP-01 operator authorization must lock next_phase to null")
    _require(operator_auth.get("constraints", {}).get("server_real_allowed") is False, "ACB-CAP-01 operator authorization must keep server_real_allowed false")
    _require(operator_auth.get("constraints", {}).get("external_network_test_allowed") is False, "ACB-CAP-01 operator authorization must keep external_network_test_allowed false")
    _require(operator_auth.get("constraints", {}).get("real_secrets_allowed") is False, "ACB-CAP-01 operator authorization must keep real_secrets_allowed false")

    evidence_data = _load_json(ACB_CAP_01_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-01 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
        "ACB-CAP-01 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("backend_baseline_ci", {}).get("conclusion") == "success",
        "ACB-CAP-01 evidence backend-baseline CI must be success",
    )
    _require(
        evidence_data.get("backend_baseline_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26920310615",
        "ACB-CAP-01 evidence backend-baseline CI URL mismatch",
    )
    for key in [
        "fastapi_app_exists",
        "health_check_exists",
        "ready_check_exists",
        "jwt_auth_exists",
        "api_key_auth_exists",
        "tenant_isolation_exists",
        "slowapi_rate_limit_exists",
        "backend_tests_exist",
        "backend_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-01 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-01 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("health_check_passing") is True,
        "ACB-CAP-01 evidence health_check_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("auth_passing") is True,
        "ACB-CAP-01 evidence auth_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("rate_limit_passing") is True,
        "ACB-CAP-01 evidence rate_limit_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable") is True,
        "ACB-CAP-01 evidence public_api_stable must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_01"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "backend-baseline.yml",
        PROJECT_ROOT / "src" / "aris" / "backend" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "app.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "auth.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "backend" / "rate_limit.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_01_backend_baseline.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_01_backend.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "backend_contract.json",
        artifacts_root / "auth_matrix.json",
        artifacts_root / "rate_limit_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-01 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    backend_contract = _load_json(artifacts_root / "backend_contract.json")
    auth_matrix = _load_json(artifacts_root / "auth_matrix.json")
    rate_limit_report = _load_json(artifacts_root / "rate_limit_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "backend-baseline.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Backend Baseline Gate", "ACB-CAP-01 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_01_pass", "ACB-CAP-01 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-01 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-01 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-01 decision minimum_deliverable_met must be true")
    _require(decision_data.get("fastapi_health_check_passing") is True, "ACB-CAP-01 decision fastapi_health_check_passing must be true")
    _require(decision_data.get("auth_passing") is True, "ACB-CAP-01 decision auth_passing must be true")
    _require(decision_data.get("jwt_auth_passing") is True, "ACB-CAP-01 decision jwt_auth_passing must be true")
    _require(decision_data.get("api_key_auth_passing") is True, "ACB-CAP-01 decision api_key_auth_passing must be true")
    _require(decision_data.get("tenant_isolation_passing") is True, "ACB-CAP-01 decision tenant_isolation_passing must be true")
    _require(decision_data.get("slowapi_rate_limit_passing") is True, "ACB-CAP-01 decision slowapi_rate_limit_passing must be true")
    _require(decision_data.get("network_server_started") is False, "ACB-CAP-01 decision network_server_started must be false")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-01 decision external_network_used must be false")
    _require(decision_data.get("real_secret_used") is False, "ACB-CAP-01 decision real_secret_used must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-01 decision database_created must be false")
    _require(decision_data.get("runtime_mutation_authorized") is False, "ACB-CAP-01 decision runtime_mutation_authorized must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-01 decision product_promotion_allowed must be false")

    _require(summary_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-01 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_01_pass", "ACB-CAP-01 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-01 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-01 summary minimum_deliverable_met must be true")
    for key in [
        "fastapi_app_exists",
        "health_check_exists",
        "ready_check_exists",
        "jwt_auth_exists",
        "api_key_auth_exists",
        "tenant_isolation_exists",
        "slowapi_rate_limit_exists",
        "backend_tests_exist",
        "backend_artifacts_exist",
    ]:
        _require(summary_data.get("deliverables", {}).get(key) is True, f"ACB-CAP-01 summary deliverable {key} must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_backend_baseline_only", "ACB-CAP-01 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "uvicorn_runtime_server", "ACB-CAP-01 research_basis rejected_pattern mismatch")

    _require(backend_contract.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 backend_contract phase_id mismatch")
    _require(backend_contract.get("app_factory") == "create_app(settings: BackendSettings | None = None) -> FastAPI", "ACB-CAP-01 backend_contract app_factory mismatch")
    _require(backend_contract.get("network_server_started") is False, "ACB-CAP-01 backend_contract network_server_started must be false")
    _require(backend_contract.get("external_network_used") is False, "ACB-CAP-01 backend_contract external_network_used must be false")
    _require(backend_contract.get("database_created") is False, "ACB-CAP-01 backend_contract database_created must be false")
    endpoints = {(item.get("method"), item.get("path")): item for item in backend_contract.get("public_endpoints", [])}
    _require(("GET", "/healthz") in endpoints, "ACB-CAP-01 backend_contract must expose GET /healthz")
    _require(("GET", "/readyz") in endpoints, "ACB-CAP-01 backend_contract must expose GET /readyz")
    _require(("POST", "/api/v1/auth/token") in endpoints, "ACB-CAP-01 backend_contract must expose POST /api/v1/auth/token")
    _require(("GET", "/api/v1/tenant/me") in endpoints, "ACB-CAP-01 backend_contract must expose GET /api/v1/tenant/me")
    _require(("GET", "/api/v1/tenant/api-key-check") in endpoints, "ACB-CAP-01 backend_contract must expose GET /api/v1/tenant/api-key-check")
    _require(endpoints.get(("GET", "/api/v1/rate-limited"), {}).get("rate_limit") == "2/minute", "ACB-CAP-01 backend_contract rate limit mismatch")

    _require(auth_matrix.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 auth_matrix phase_id mismatch")
    _require(auth_matrix.get("token_issue_status") == 200, "ACB-CAP-01 auth_matrix token_issue_status mismatch")
    _require(auth_matrix.get("missing_bearer_status") == 401, "ACB-CAP-01 auth_matrix missing_bearer_status mismatch")
    _require(auth_matrix.get("invalid_api_key_status") == 401, "ACB-CAP-01 auth_matrix invalid_api_key_status mismatch")
    _require(auth_matrix.get("valid_api_key_status") == 200, "ACB-CAP-01 auth_matrix valid_api_key_status mismatch")
    _require(auth_matrix.get("cross_tenant_api_key_status") == 403, "ACB-CAP-01 auth_matrix cross_tenant_api_key_status mismatch")
    _require(auth_matrix.get("valid_jwt_status") == 200, "ACB-CAP-01 auth_matrix valid_jwt_status mismatch")
    _require(auth_matrix.get("expired_jwt_status") == 401, "ACB-CAP-01 auth_matrix expired_jwt_status mismatch")
    _require(auth_matrix.get("wrong_tenant_jwt_status") == 403, "ACB-CAP-01 auth_matrix wrong_tenant_jwt_status mismatch")
    _require(auth_matrix.get("jwt_auth_passing") is True, "ACB-CAP-01 auth_matrix jwt_auth_passing must be true")
    _require(auth_matrix.get("api_key_auth_passing") is True, "ACB-CAP-01 auth_matrix api_key_auth_passing must be true")
    _require(auth_matrix.get("tenant_isolation_passing") is True, "ACB-CAP-01 auth_matrix tenant_isolation_passing must be true")

    _require(rate_limit_report.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 rate_limit_report phase_id mismatch")
    _require(rate_limit_report.get("limit") == "2/minute", "ACB-CAP-01 rate_limit_report limit mismatch")
    _require(rate_limit_report.get("statuses") == [200, 200, 429], "ACB-CAP-01 rate_limit_report statuses mismatch")
    _require(rate_limit_report.get("slowapi_rate_limit_passing") is True, "ACB-CAP-01 rate_limit_report slowapi_rate_limit_passing must be true")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 public_api_drift phase_id mismatch")
    _require(public_api_drift.get("drift_detected") is False, "ACB-CAP-01 public_api_drift drift_detected must be false")
    _require(public_api_drift.get("public_api_stable") is True, "ACB-CAP-01 public_api_drift public_api_stable must be true")

    _require(import_report.get("phase_id") == "ACB-CAP-01", "ACB-CAP-01 import_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-01 import_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable") is True, "ACB-CAP-01 import_report public_api_stable must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-01 import_report forbidden_runtime_patterns must be empty")

    _require("name: Backend Baseline" in workflow_text, "ACB-CAP-01 workflow must be Backend Baseline")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-01 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-01 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_01_backend_baseline.py" in workflow_text, "ACB-CAP-01 workflow must validate backend baseline artifacts")
    _require("tests/test_acb_cap_01_backend.py -v" in workflow_text, "ACB-CAP-01 workflow must run backend tests")


def _check_acb_cap_02_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_02_EVIDENCE_PATH.exists(), "missing ACB-CAP-02 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_02_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-02 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b2fdc3c994342a42a84823fa15615c931f1bc00e",
        "ACB-CAP-02 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
        "ACB-CAP-02 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("mcp_runtime_sandbox_ci", {}).get("conclusion") == "success",
        "ACB-CAP-02 evidence MCP Runtime Sandbox CI must be success",
    )
    _require(
        evidence_data.get("mcp_runtime_sandbox_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26922186509",
        "ACB-CAP-02 evidence MCP Runtime Sandbox CI URL mismatch",
    )
    for key in [
        "mcp_runtime_package_exists",
        "stdio_ban_exists",
        "sandbox_spec_exists",
        "policy_pre_dispatch_exists",
        "kill_switch_exists",
        "rollback_contract_exists",
        "audit_event_exists",
        "mcp_runtime_tests_exist",
        "mcp_runtime_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-02 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-02 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("mcp_sandbox_running") is True,
        "ACB-CAP-02 evidence mcp_sandbox_running must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("stdio_banned") is True,
        "ACB-CAP-02 evidence stdio_banned must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("policy_pre_dispatch_passing") is True,
        "ACB-CAP-02 evidence policy_pre_dispatch_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("kill_switch_passing") is True,
        "ACB-CAP-02 evidence kill_switch_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("rollback_contract_passing") is True,
        "ACB-CAP-02 evidence rollback_contract_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("network_none_enforced") is True,
        "ACB-CAP-02 evidence network_none_enforced must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable") is True,
        "ACB-CAP-02 evidence public_api_stable must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_02"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "mcp-runtime-sandbox.yml",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "transport_policy.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "sandbox_spec.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "policy_engine.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "dispatcher.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "kill_switch.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "rollback.py",
        PROJECT_ROOT / "src" / "aris" / "mcp_runtime" / "audit.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_02_mcp_runtime_sandbox.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_02_mcp_runtime_sandbox.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "mcp_runtime_contract.json",
        artifacts_root / "transport_policy_matrix.json",
        artifacts_root / "sandbox_spec.json",
        artifacts_root / "policy_decision_matrix.json",
        artifacts_root / "kill_switch_matrix.json",
        artifacts_root / "rollback_contract.json",
        artifacts_root / "audit_event_sample.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-02 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "mcp_runtime_contract.json")
    transport_matrix = _load_json(artifacts_root / "transport_policy_matrix.json")
    sandbox_spec = _load_json(artifacts_root / "sandbox_spec.json")
    policy_matrix = _load_json(artifacts_root / "policy_decision_matrix.json")
    kill_switch_matrix = _load_json(artifacts_root / "kill_switch_matrix.json")
    rollback_contract = _load_json(artifacts_root / "rollback_contract.json")
    audit_event = _load_json(artifacts_root / "audit_event_sample.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "mcp-runtime-sandbox.yml").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build MCP Runtime Sandbox Gate", "ACB-CAP-02 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_02_pass", "ACB-CAP-02 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-02 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-02 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-02 decision minimum_deliverable_met must be true")
    _require(decision_data.get("mcp_sandbox_running") is True, "ACB-CAP-02 decision mcp_sandbox_running must be true")
    _require(decision_data.get("stdio_banned") is True, "ACB-CAP-02 decision stdio_banned must be true")
    _require(decision_data.get("policy_pre_dispatch_passing") is True, "ACB-CAP-02 decision policy_pre_dispatch_passing must be true")
    _require(decision_data.get("kill_switch_passing") is True, "ACB-CAP-02 decision kill_switch_passing must be true")
    _require(decision_data.get("rollback_contract_passing") is True, "ACB-CAP-02 decision rollback_contract_passing must be true")
    _require(decision_data.get("network_none_enforced") is True, "ACB-CAP-02 decision network_none_enforced must be true")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-02 decision external_network_used must be false")
    _require(decision_data.get("server_real_started") is False, "ACB-CAP-02 decision server_real_started must be false")
    _require(decision_data.get("subprocess_stdio_started") is False, "ACB-CAP-02 decision subprocess_stdio_started must be false")
    _require(decision_data.get("real_tool_execution_used") is False, "ACB-CAP-02 decision real_tool_execution_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "ACB-CAP-02 decision secrets_accessed must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-02 decision database_created must be false")
    _require(decision_data.get("runtime_productive_mutation") is False, "ACB-CAP-02 decision runtime_productive_mutation must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-02 decision product_promotion_allowed must be false")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-02 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-02 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_02_pass", "ACB-CAP-02 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-02 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-02 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_mcp_runtime_sandbox_gate_only", "ACB-CAP-02 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "stdio_transport_runtime", "ACB-CAP-02 research_basis rejected_pattern mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 contract phase_id mismatch")
    _require(contract_data.get("allowed_transport") == "streamable_http", "ACB-CAP-02 allowed_transport mismatch")
    _require(contract_data.get("banned_transport") == "stdio", "ACB-CAP-02 banned_transport mismatch")
    _require(contract_data.get("mcp_sandbox_running") is True, "ACB-CAP-02 contract mcp_sandbox_running must be true")
    _require(contract_data.get("server_real_started") is False, "ACB-CAP-02 contract server_real_started must be false")
    _require(contract_data.get("external_network_used") is False, "ACB-CAP-02 contract external_network_used must be false")
    _require(contract_data.get("real_tool_execution_used") is False, "ACB-CAP-02 contract real_tool_execution_used must be false")
    _require(contract_data.get("subprocess_stdio_started") is False, "ACB-CAP-02 contract subprocess_stdio_started must be false")

    transport_cases = {item.get("name"): item for item in transport_matrix.get("cases", [])}
    _require(transport_cases.get("stdio_blocked", {}).get("decision") == "block", "ACB-CAP-02 stdio transport must be blocked")
    _require("stdio_transport_banned" in transport_cases.get("stdio_blocked", {}).get("reasons", []), "ACB-CAP-02 stdio transport block reason mismatch")
    _require(transport_cases.get("streamable_http_allowed", {}).get("decision") == "allow", "ACB-CAP-02 streamable_http transport must be allowed")

    spec = sandbox_spec.get("spec", {})
    _require(spec.get("network_mode") == "none", "ACB-CAP-02 sandbox network_mode mismatch")
    _require(spec.get("filesystem_mode") == "read_only", "ACB-CAP-02 sandbox filesystem_mode mismatch")
    _require(spec.get("allow_write_paths") == [], "ACB-CAP-02 sandbox allow_write_paths must be empty")
    _require(spec.get("secrets_mount_allowed") is False, "ACB-CAP-02 sandbox secrets_mount_allowed must be false")
    _require(spec.get("process_secret_read_allowed") is False, "ACB-CAP-02 sandbox process_secret_read_allowed must be false")
    _require(spec.get("egress_allowed") is False, "ACB-CAP-02 sandbox egress_allowed must be false")
    _require(spec.get("host_mount_allowed") is False, "ACB-CAP-02 sandbox host_mount_allowed must be false")
    _require(sandbox_spec.get("runner_running") is True, "ACB-CAP-02 sandbox runner_running must be true")

    _require(policy_matrix.get("cases", {}).get("allowed_streamable_http", {}).get("decision") == "allow", "ACB-CAP-02 policy matrix allow case mismatch")
    _require(policy_matrix.get("cases", {}).get("stdio_blocked", {}).get("decision") == "block", "ACB-CAP-02 policy matrix stdio case mismatch")
    _require(policy_matrix.get("cases", {}).get("missing_rollback", {}).get("rollback_ready") is False, "ACB-CAP-02 policy matrix missing_rollback rollback_ready must be false")
    _require(policy_matrix.get("cases", {}).get("side_effect_with_rollback", {}).get("rollback_ready") is True, "ACB-CAP-02 policy matrix rollback-ready case mismatch")

    _require(kill_switch_matrix.get("cases", {}).get("global_disabled", {}).get("executed") is False, "ACB-CAP-02 kill switch global_disabled must not execute")
    _require(kill_switch_matrix.get("cases", {}).get("emergency_stop", {}).get("executed") is False, "ACB-CAP-02 kill switch emergency_stop must not execute")

    _require(rollback_contract.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 rollback_contract phase_id mismatch")
    _require(rollback_contract.get("missing_rollback_plan", {}).get("rollback_ready") is False, "ACB-CAP-02 rollback missing plan readiness mismatch")
    _require(rollback_contract.get("rollback_plan_ready", {}).get("rollback_ready") is True, "ACB-CAP-02 rollback ready case mismatch")

    _require(audit_event.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 audit_event phase_id mismatch")
    _require(audit_event.get("policy_decision") == "allow", "ACB-CAP-02 audit_event policy_decision mismatch")
    _require(bool(audit_event.get("audit_event_sha256")), "ACB-CAP-02 audit_event_sha256 must be non-empty")

    _require(import_report.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 import_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-02 import_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable") is True, "ACB-CAP-02 import_report public_api_stable must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-02 import_report forbidden_runtime_patterns must be empty")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-02", "ACB-CAP-02 public_api_drift phase_id mismatch")
    _require(public_api_drift.get("drift_detected") is False, "ACB-CAP-02 public_api_drift drift_detected must be false")
    _require(public_api_drift.get("public_api_stable") is True, "ACB-CAP-02 public_api_drift public_api_stable must be true")

    _require("name: MCP Runtime Sandbox" in workflow_text, "ACB-CAP-02 workflow must be MCP Runtime Sandbox")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-02 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-02 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_02_mcp_runtime_sandbox.py" in workflow_text, "ACB-CAP-02 workflow must run the sandbox artifact validator")
    _require("tests/test_acb_cap_02_mcp_runtime_sandbox.py -v" in workflow_text, "ACB-CAP-02 workflow must run MCP runtime sandbox tests")
    _require("uv lock --check" in workflow_text, "ACB-CAP-02 workflow must check uv lock freshness")


def _check_acb_cap_03_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_03_EVIDENCE_PATH.exists(), "missing ACB-CAP-03 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_03_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-03 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b1d175f8b0d1105a9d05f6ddcab082c71d6f6b3e",
        "ACB-CAP-03 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b2fdc3c994342a42a84823fa15615c931f1bc00e",
        "ACB-CAP-03 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("runtime_public_api_ci", {}).get("conclusion") == "success",
        "ACB-CAP-03 evidence Runtime Public API CI must be success",
    )
    _require(
        evidence_data.get("runtime_public_api_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26923273196",
        "ACB-CAP-03 evidence Runtime Public API CI URL mismatch",
    )
    for key in [
        "runtime_package_exists",
        "runtime_public_api_documented",
        "runtime_public_api_contract_exists",
        "runtime_facade_exists",
        "runtime_modes_enforced",
        "runtime_policy_bridge_exists",
        "runtime_audit_hashing_exists",
        "public_api_drift_ratified",
        "runtime_tests_exist",
        "runtime_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-03 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-03 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_public_api_importable") is True,
        "ACB-CAP-03 evidence runtime_public_api_importable must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_facade_passing") is True,
        "ACB-CAP-03 evidence runtime_facade_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_policy_bridge_passing") is True,
        "ACB-CAP-03 evidence runtime_policy_bridge_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("runtime_audit_hashing_passing") is True,
        "ACB-CAP-03 evidence runtime_audit_hashing_passing must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("public_api_stable_or_ratified") is True,
        "ACB-CAP-03 evidence public_api_stable_or_ratified must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_03"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "runtime-public-api.yml",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "facade.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "execution_plan.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "request.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "response.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "policy_bridge.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "audit_bridge.py",
        PROJECT_ROOT / "src" / "aris" / "runtime" / "public_api.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_03_runtime_public_api.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_03_runtime_public_api.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "runtime_public_api.md",
        artifacts_root / "runtime_public_api_contract.json",
        artifacts_root / "runtime_facade_contract.json",
        artifacts_root / "runtime_mode_matrix.json",
        artifacts_root / "runtime_policy_bridge_matrix.json",
        artifacts_root / "runtime_audit_report.json",
        artifacts_root / "public_api_snapshot_before.json",
        artifacts_root / "public_api_snapshot_after.json",
        artifacts_root / "public_api_change_report.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-03 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "runtime_public_api_contract.json")
    facade_contract = _load_json(artifacts_root / "runtime_facade_contract.json")
    mode_matrix = _load_json(artifacts_root / "runtime_mode_matrix.json")
    policy_matrix = _load_json(artifacts_root / "runtime_policy_bridge_matrix.json")
    audit_report = _load_json(artifacts_root / "runtime_audit_report.json")
    before_snapshot = _load_json(artifacts_root / "public_api_snapshot_before.json")
    after_snapshot = _load_json(artifacts_root / "public_api_snapshot_after.json")
    public_api_drift = _load_json(artifacts_root / "public_api_change_report.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "runtime-public-api.yml").read_text(encoding="utf-8")
    markdown_text = (artifacts_root / "runtime_public_api.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Runtime Top-Level Public API Gate", "ACB-CAP-03 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_03_pass", "ACB-CAP-03 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-03 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-03 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-03 decision minimum_deliverable_met must be true")
    _require(decision_data.get("runtime_public_api_documented") is True, "ACB-CAP-03 decision runtime_public_api_documented must be true")
    _require(decision_data.get("runtime_public_api_importable") is True, "ACB-CAP-03 decision runtime_public_api_importable must be true")
    _require(decision_data.get("runtime_facade_created") is True, "ACB-CAP-03 decision runtime_facade_created must be true")
    _require(decision_data.get("runtime_policy_bridge_passing") is True, "ACB-CAP-03 decision runtime_policy_bridge_passing must be true")
    _require(decision_data.get("runtime_audit_hashing_passing") is True, "ACB-CAP-03 decision runtime_audit_hashing_passing must be true")
    _require(decision_data.get("runtime_modes_enforced") is True, "ACB-CAP-03 decision runtime_modes_enforced must be true")
    _require(decision_data.get("public_api_drift_ratified") is True, "ACB-CAP-03 decision public_api_drift_ratified must be true")
    _require(decision_data.get("stdio_ban_preserved") is True, "ACB-CAP-03 decision stdio_ban_preserved must be true")
    _require(decision_data.get("mcp_policy_pre_dispatch_preserved") is True, "ACB-CAP-03 decision mcp_policy_pre_dispatch_preserved must be true")
    _require(decision_data.get("kill_switch_preserved") is True, "ACB-CAP-03 decision kill_switch_preserved must be true")
    _require(decision_data.get("rollback_contract_preserved") is True, "ACB-CAP-03 decision rollback_contract_preserved must be true")
    _require(decision_data.get("external_network_used") is False, "ACB-CAP-03 decision external_network_used must be false")
    _require(decision_data.get("server_real_started") is False, "ACB-CAP-03 decision server_real_started must be false")
    _require(decision_data.get("real_tool_execution_used") is False, "ACB-CAP-03 decision real_tool_execution_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "ACB-CAP-03 decision secrets_accessed must be false")
    _require(decision_data.get("database_created") is False, "ACB-CAP-03 decision database_created must be false")
    _require(decision_data.get("runtime_productive_activation") is False, "ACB-CAP-03 decision runtime_productive_activation must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-03 decision product_promotion_allowed must be false")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-03 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-03 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_03_pass", "ACB-CAP-03 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-03 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-03 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_runtime_public_api_gate_only", "ACB-CAP-03 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "productive_runtime_activation", "ACB-CAP-03 research_basis rejected_pattern mismatch")
    _require(research_data.get("rejected_pattern_2") == "external_network_or_tool_execution", "ACB-CAP-03 research_basis rejected_pattern_2 mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 contract phase_id mismatch")
    _require(contract_data.get("module") == "aris.runtime", "ACB-CAP-03 contract module mismatch")
    _require(
        contract_data.get("public_symbols")
        == [
            "RuntimeAuditEvent",
            "RuntimeContext",
            "RuntimeDecision",
            "RuntimeExecutionPlan",
            "RuntimeFacade",
            "RuntimeMode",
            "RuntimePolicyDecision",
            "RuntimeRequest",
            "RuntimeResponse",
            "create_runtime",
        ],
        "ACB-CAP-03 contract public_symbols mismatch",
    )
    _require(contract_data.get("root_public_api_delta", {}).get("removed_symbols") == [], "ACB-CAP-03 contract removed_symbols must be empty")
    _require(contract_data.get("root_public_api_delta", {}).get("added_symbols") == [], "ACB-CAP-03 contract added_symbols must be empty")
    _require(contract_data.get("allowed_modes") == ["contract_only", "dry_safe"], "ACB-CAP-03 contract allowed_modes mismatch")
    _require(contract_data.get("blocked_modes") == ["disabled", "productive", "real_apply", "external_tool", "networked"], "ACB-CAP-03 contract blocked_modes mismatch")

    _require(facade_contract.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 facade_contract phase_id mismatch")
    _require(facade_contract.get("safe_default_mode") == "dry_safe", "ACB-CAP-03 facade safe_default_mode mismatch")
    _require(facade_contract.get("contract_only_status") == "contract_only_ready", "ACB-CAP-03 facade contract_only_status mismatch")
    _require(facade_contract.get("safe_dispatch_status") == "completed", "ACB-CAP-03 facade safe_dispatch_status mismatch")
    _require(facade_contract.get("server_real_started") is False, "ACB-CAP-03 facade server_real_started must be false")
    _require(facade_contract.get("external_network_used") is False, "ACB-CAP-03 facade external_network_used must be false")
    _require(facade_contract.get("real_tool_execution_used") is False, "ACB-CAP-03 facade real_tool_execution_used must be false")

    _require(mode_matrix.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_mode_matrix phase_id mismatch")
    _require(mode_matrix.get("cases", {}).get("contract_only", {}).get("status") == "contract_only_ready", "ACB-CAP-03 contract_only status mismatch")
    _require(mode_matrix.get("cases", {}).get("dry_safe", {}).get("status") == "completed", "ACB-CAP-03 dry_safe status mismatch")
    _require(mode_matrix.get("cases", {}).get("productive", {}).get("allowed") is False, "ACB-CAP-03 productive mode must be blocked")
    _require(mode_matrix.get("cases", {}).get("productive", {}).get("status") == "blocked_pre_dispatch", "ACB-CAP-03 productive mode status mismatch")
    _require(mode_matrix.get("cases", {}).get("real_apply", {}).get("blocked") is True, "ACB-CAP-03 real_apply must be blocked")
    _require(mode_matrix.get("cases", {}).get("external_tool", {}).get("blocked") is True, "ACB-CAP-03 external_tool must be blocked")
    _require(mode_matrix.get("cases", {}).get("networked", {}).get("blocked") is True, "ACB-CAP-03 networked must be blocked")

    _require(policy_matrix.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_policy_bridge_matrix phase_id mismatch")
    _require(policy_matrix.get("cases", {}).get("safe_request", {}).get("decision") == "allow", "ACB-CAP-03 safe_request must allow")
    _require(policy_matrix.get("cases", {}).get("missing_tenant", {}).get("decision") == "block", "ACB-CAP-03 missing_tenant must block")
    _require("missing_tenant" in policy_matrix.get("cases", {}).get("missing_tenant", {}).get("reasons", []), "ACB-CAP-03 missing_tenant reason mismatch")
    _require(policy_matrix.get("cases", {}).get("missing_auth", {}).get("decision") == "block", "ACB-CAP-03 missing_auth must block")
    _require("missing_auth_context" in policy_matrix.get("cases", {}).get("missing_auth", {}).get("reasons", []), "ACB-CAP-03 missing_auth reason mismatch")
    _require(policy_matrix.get("cases", {}).get("productive_mode", {}).get("decision") == "block", "ACB-CAP-03 productive_mode must block")
    _require("runtime_mode_blocked:productive" in policy_matrix.get("cases", {}).get("productive_mode", {}).get("reasons", []), "ACB-CAP-03 productive_mode reason mismatch")
    _require(policy_matrix.get("cases", {}).get("stdio_transport", {}).get("decision") == "block", "ACB-CAP-03 stdio_transport must block")
    _require("stdio_transport_banned" in policy_matrix.get("cases", {}).get("stdio_transport", {}).get("reasons", []), "ACB-CAP-03 stdio_transport reason mismatch")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("decision") == "allow", "ACB-CAP-03 rollback_ready must allow")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("rollback_required") is True, "ACB-CAP-03 rollback_ready rollback_required mismatch")
    _require(policy_matrix.get("cases", {}).get("rollback_ready", {}).get("rollback_ready") is True, "ACB-CAP-03 rollback_ready rollback_ready mismatch")

    _require(audit_report.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 runtime_audit_report phase_id mismatch")
    _require(audit_report.get("hash_stable") is True, "ACB-CAP-03 runtime_audit_report hash_stable must be true")
    _require(audit_report.get("safe_audit_hash") == audit_report.get("safe_audit_hash_repeat"), "ACB-CAP-03 safe audit hash must be stable")
    _require(bool(audit_report.get("contract_only_audit_hash")), "ACB-CAP-03 contract_only_audit_hash must be non-empty")
    _require(bool(audit_report.get("blocked_stdio_audit_hash")), "ACB-CAP-03 blocked_stdio_audit_hash must be non-empty")

    _require(before_snapshot.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_snapshot_before phase_id mismatch")
    _require(before_snapshot.get("runtime_module_present") is False, "ACB-CAP-03 public_api_snapshot_before runtime_module_present must be false")
    _require(before_snapshot.get("runtime_public_symbols") == [], "ACB-CAP-03 public_api_snapshot_before runtime_public_symbols must be empty")
    _require(after_snapshot.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_snapshot_after phase_id mismatch")
    _require(after_snapshot.get("runtime_module_present") is True, "ACB-CAP-03 public_api_snapshot_after runtime_module_present must be true")
    _require(after_snapshot.get("runtime_public_symbols") == contract_data.get("public_symbols"), "ACB-CAP-03 public_api_snapshot_after runtime_public_symbols mismatch")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 public_api_change_report phase_id mismatch")
    _require(public_api_drift.get("root_removed_symbols") == [], "ACB-CAP-03 public_api_change_report root_removed_symbols must be empty")
    _require(public_api_drift.get("root_added_symbols") == [], "ACB-CAP-03 public_api_change_report root_added_symbols must be empty")
    _require(public_api_drift.get("runtime_module_added_as_submodule_only") is True, "ACB-CAP-03 public_api_change_report runtime_module_added_as_submodule_only must be true")
    _require(public_api_drift.get("delta_ratified") is True, "ACB-CAP-03 public_api_change_report delta_ratified must be true")

    _require(import_report.get("phase_id") == "ACB-CAP-03", "ACB-CAP-03 import_stability_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-03 import_stability_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable_or_ratified") is True, "ACB-CAP-03 import_stability_report public_api_stable_or_ratified must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-03 import_stability_report forbidden_runtime_patterns must be empty")

    for symbol in contract_data.get("public_symbols", []):
        _require(symbol in markdown_text, f"ACB-CAP-03 runtime_public_api.md missing public symbol: {symbol}")
    _require("## Blocked Modes" in markdown_text, "ACB-CAP-03 runtime_public_api.md must document blocked modes")
    _require("no production" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid production")
    _require("no external network" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid external network")
    _require("no real apply" in markdown_text.lower(), "ACB-CAP-03 runtime_public_api.md must forbid real apply")

    _require("name: Runtime Public API" in workflow_text, "ACB-CAP-03 workflow must be Runtime Public API")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-03 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-03 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_03_runtime_public_api.py" in workflow_text, "ACB-CAP-03 workflow must run the runtime public API artifact validator")
    _require("tests/test_acb_cap_03_runtime_public_api.py -v" in workflow_text, "ACB-CAP-03 workflow must run runtime public API tests")


def _check_acb_cap_04_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_04_EVIDENCE_PATH.exists(), "missing ACB-CAP-04 evidence artifact in active-context")

    evidence_data = _load_json(ACB_CAP_04_EVIDENCE_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-04 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == "b6044982c31e0861b481605c40bef673b249f351",
        "ACB-CAP-04 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b1d175f8b0d1105a9d05f6ddcab082c71d6f6b3e",
        "ACB-CAP-04 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("product_pilot_boundary_ci", {}).get("conclusion") == "success",
        "ACB-CAP-04 evidence Product Pilot Boundary CI must be success",
    )
    _require(
        evidence_data.get("product_pilot_boundary_ci", {}).get("url")
        == "https://github.com/MatheusAugDEV/Project-A.R.I.S/actions/runs/26924199459",
        "ACB-CAP-04 evidence Product Pilot Boundary CI URL mismatch",
    )
    for key in [
        "product_boundary_package_exists",
        "pilot_gates_defined",
        "five_binary_gates_defined",
        "lab_to_staging_to_pilot_workflow_defined",
        "pilot_scope_contract_exists",
        "evidence_bundle_contract_exists",
        "pilot_runbook_contract_exists",
        "pilot_risk_matrix_exists",
        "non_authorization_statement_exists",
        "product_pilot_tests_exist",
        "product_pilot_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-04 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-04 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_gates_defined") is True,
        "ACB-CAP-04 evidence pilot_gates_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("five_binary_gates_defined") is True,
        "ACB-CAP-04 evidence five_binary_gates_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_scope_defined") is True,
        "ACB-CAP-04 evidence pilot_scope_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("evidence_bundle_contract_defined") is True,
        "ACB-CAP-04 evidence evidence_bundle_contract_defined must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("pilot_allowed_now") is False,
        "ACB-CAP-04 evidence pilot_allowed_now must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("production_authorized") is False,
        "ACB-CAP-04 evidence production_authorized must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("product_promotion_allowed") is False,
        "ACB-CAP-04 evidence product_promotion_allowed must be false",
    )
    _require(
        evidence_data.get("local_validation", {}).get("bedrock_required_before_product") is True,
        "ACB-CAP-04 evidence bedrock_required_before_product must be true",
    )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_04"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "product-pilot-boundary.yml",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "contracts.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "gate_registry.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "pilot_gate.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "workflow.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "evidence.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "decision.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "checklist.py",
        PROJECT_ROOT / "src" / "aris" / "product_boundary" / "risk_matrix.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_04_product_pilot_boundary.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_04_product_pilot_boundary.py",
        artifacts_root / "research_basis.json",
        artifacts_root / "product_pilot_boundary_contract.json",
        artifacts_root / "pilot_gate_registry.json",
        artifacts_root / "five_gate_decision_matrix.json",
        artifacts_root / "lab_to_staging_to_pilot_workflow.json",
        artifacts_root / "pilot_scope_contract.json",
        artifacts_root / "evidence_bundle_contract.json",
        artifacts_root / "pilot_runbook_contract.md",
        artifacts_root / "pilot_risk_matrix.json",
        artifacts_root / "non_authorization_statement.json",
        artifacts_root / "import_stability_report.json",
        artifacts_root / "public_api_drift_report.json",
        artifacts_root / "decision.json",
        artifacts_root / "summary.json",
        artifacts_root / "report.md",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-04 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "decision.json")
    summary_data = _load_json(artifacts_root / "summary.json")
    research_data = _load_json(artifacts_root / "research_basis.json")
    contract_data = _load_json(artifacts_root / "product_pilot_boundary_contract.json")
    gate_registry = _load_json(artifacts_root / "pilot_gate_registry.json")
    decision_matrix = _load_json(artifacts_root / "five_gate_decision_matrix.json")
    workflow_data = _load_json(artifacts_root / "lab_to_staging_to_pilot_workflow.json")
    pilot_scope = _load_json(artifacts_root / "pilot_scope_contract.json")
    evidence_contract = _load_json(artifacts_root / "evidence_bundle_contract.json")
    risk_matrix = _load_json(artifacts_root / "pilot_risk_matrix.json")
    non_authorization = _load_json(artifacts_root / "non_authorization_statement.json")
    import_report = _load_json(artifacts_root / "import_stability_report.json")
    public_api_drift = _load_json(artifacts_root / "public_api_drift_report.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "product-pilot-boundary.yml").read_text(encoding="utf-8")
    runbook_text = (artifacts_root / "pilot_runbook_contract.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Product/Pilot Boundary Gate", "ACB-CAP-04 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_04_pass", "ACB-CAP-04 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-04 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-04 decision pass_criteria_met must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "ACB-CAP-04 decision minimum_deliverable_met must be true")
    _require(decision_data.get("pilot_gates_defined") is True, "ACB-CAP-04 decision pilot_gates_defined must be true")
    _require(decision_data.get("five_binary_gates_defined") is True, "ACB-CAP-04 decision five_binary_gates_defined must be true")
    _require(decision_data.get("lab_to_staging_to_pilot_workflow_defined") is True, "ACB-CAP-04 decision workflow flag mismatch")
    _require(decision_data.get("pilot_scope_defined") is True, "ACB-CAP-04 decision pilot_scope_defined must be true")
    _require(decision_data.get("evidence_bundle_contract_defined") is True, "ACB-CAP-04 decision evidence_bundle_contract_defined must be true")
    _require(decision_data.get("pilot_runbook_contract_defined") is True, "ACB-CAP-04 decision pilot_runbook_contract_defined must be true")
    _require(decision_data.get("pilot_risk_matrix_defined") is True, "ACB-CAP-04 decision pilot_risk_matrix_defined must be true")
    _require(decision_data.get("pilot_allowed_now") is False, "ACB-CAP-04 decision pilot_allowed_now must be false")
    _require(decision_data.get("client_real_allowed_now") is False, "ACB-CAP-04 decision client_real_allowed_now must be false")
    _require(decision_data.get("production_authorized") is False, "ACB-CAP-04 decision production_authorized must be false")
    _require(decision_data.get("commercial_use_allowed") is False, "ACB-CAP-04 decision commercial_use_allowed must be false")
    _require(decision_data.get("pricing_allowed") is False, "ACB-CAP-04 decision pricing_allowed must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "ACB-CAP-04 decision product_promotion_allowed must be false")
    _require(decision_data.get("runtime_productive_activation") is False, "ACB-CAP-04 decision runtime_productive_activation must be false")
    _require(decision_data.get("bedrock_required_before_product") is True, "ACB-CAP-04 decision bedrock_required_before_product must be true")
    _require(
        decision_data.get("project_repo_sha")
        in {
            evidence_data.get("project_sha_gate_start"),
            evidence_data.get("project_sha"),
        },
        "ACB-CAP-04 decision project_repo_sha must match gate-start or final project SHA",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "ACB-CAP-04 summary decision must be pass")
    _require(summary_data.get("status") == "acb_cap_04_pass", "ACB-CAP-04 summary status mismatch")
    _require(summary_data.get("pass_criteria_met") is True, "ACB-CAP-04 summary pass_criteria_met must be true")
    _require(summary_data.get("minimum_deliverable_met") is True, "ACB-CAP-04 summary minimum_deliverable_met must be true")

    _require(research_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 research_basis phase_id mismatch")
    _require(research_data.get("conclusion") == "proceed_with_product_pilot_boundary_gate_only", "ACB-CAP-04 research_basis conclusion mismatch")
    _require(research_data.get("rejected_pattern") == "pilot_without_evidence_hashes", "ACB-CAP-04 research_basis rejected_pattern mismatch")
    _require(research_data.get("rejected_pattern_2") == "automatic_product_promotion", "ACB-CAP-04 research_basis rejected_pattern_2 mismatch")

    _require(contract_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 contract phase_id mismatch")
    _require(contract_data.get("module") == "aris.product_boundary", "ACB-CAP-04 contract module mismatch")
    _require(contract_data.get("gate_count") == 5, "ACB-CAP-04 contract gate_count mismatch")
    _require(contract_data.get("binary_outputs_only") is True, "ACB-CAP-04 contract binary_outputs_only must be true")
    _require(contract_data.get("workflow_stages") == ["LAB", "STAGING", "PILOT_CANDIDATE", "PILOT_APPROVED"], "ACB-CAP-04 contract workflow stages mismatch")
    invariants = contract_data.get("invariants", {})
    _require(invariants.get("pilot_allowed_now") is False, "ACB-CAP-04 contract pilot_allowed_now must be false")
    _require(invariants.get("client_real_allowed_now") is False, "ACB-CAP-04 contract client_real_allowed_now must be false")
    _require(invariants.get("production_authorized") is False, "ACB-CAP-04 contract production_authorized must be false")
    _require(invariants.get("commercial_use_allowed") is False, "ACB-CAP-04 contract commercial_use_allowed must be false")
    _require(invariants.get("pricing_allowed") is False, "ACB-CAP-04 contract pricing_allowed must be false")
    _require(invariants.get("product_promotion_allowed") is False, "ACB-CAP-04 contract product_promotion_allowed must be false")
    _require(invariants.get("runtime_productive_activation") is False, "ACB-CAP-04 contract runtime_productive_activation must be false")
    _require(invariants.get("bedrock_required_before_product") is True, "ACB-CAP-04 contract bedrock_required_before_product must be true")

    _require(gate_registry.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 pilot_gate_registry phase_id mismatch")
    _require(gate_registry.get("gate_count") == 5, "ACB-CAP-04 pilot_gate_registry gate_count mismatch")
    gates = gate_registry.get("gates", [])
    _require(len(gates) == 5, "ACB-CAP-04 pilot_gate_registry must contain exactly 5 gates")
    expected_gate_ids = [
        "LAB_EVIDENCE_GATE",
        "STAGING_READINESS_GATE",
        "SAFETY_BOUNDARY_GATE",
        "OPERATIONAL_SUPPORT_GATE",
        "PILOT_APPROVAL_GATE",
    ]
    _require([gate.get("gate_id") for gate in gates] == expected_gate_ids, "ACB-CAP-04 gate ids mismatch")
    for gate in gates:
        _require(gate.get("allowed_outputs") == ["pass", "fail"], f"ACB-CAP-04 gate {gate.get('gate_id')} allowed_outputs mismatch")
        _require(gate.get("decision") in {"pass", "fail"}, f"ACB-CAP-04 gate {gate.get('gate_id')} decision must be binary")
        _require(all(output not in {"pass", "fail"} for output in gate.get("forbidden_outputs", [])), f"ACB-CAP-04 gate {gate.get('gate_id')} forbidden outputs must exclude binary values")

    _require(decision_matrix.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 five_gate_decision_matrix phase_id mismatch")
    _require(decision_matrix.get("gate_count") == 5, "ACB-CAP-04 five_gate_decision_matrix gate_count mismatch")
    matrix_cases = decision_matrix.get("cases", {})
    for case_name in ["missing_evidence", "hashless_evidence", "complete_evidence"]:
        _require(len(matrix_cases.get(case_name, [])) == 5, f"ACB-CAP-04 decision matrix case {case_name} must contain 5 gates")
    _require(all(gate.get("decision") == "fail" for gate in matrix_cases.get("missing_evidence", [])), "ACB-CAP-04 missing_evidence case must fail every gate")
    _require(all(gate.get("decision") == "fail" for gate in matrix_cases.get("hashless_evidence", [])), "ACB-CAP-04 hashless_evidence case must fail every gate")
    _require(all(gate.get("decision") == "pass" for gate in matrix_cases.get("complete_evidence", [])), "ACB-CAP-04 complete_evidence case must pass every gate")

    _require(workflow_data.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 workflow phase_id mismatch")
    _require(workflow_data.get("stages") == ["LAB", "STAGING", "PILOT_CANDIDATE", "PILOT_APPROVED"], "ACB-CAP-04 workflow stages mismatch")
    evaluations = workflow_data.get("evaluations", {})
    _require(evaluations.get("blocked_by_gate", {}).get("current_stage") == "lab", "ACB-CAP-04 workflow blocked_by_gate stage mismatch")
    _require("binary_gate_fail" in evaluations.get("blocked_by_gate", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow blocked_by_gate reasons mismatch")
    _require(evaluations.get("blocked_by_prerequisite", {}).get("current_stage") == "staging", "ACB-CAP-04 workflow blocked_by_prerequisite stage mismatch")
    _require(evaluations.get("candidate_blocked_without_approval", {}).get("current_stage") == "pilot_candidate", "ACB-CAP-04 workflow candidate_blocked_without_approval stage mismatch")
    _require("client_approval_missing" in evaluations.get("candidate_blocked_without_approval", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow must block missing client approval")
    _require("commercial_terms_missing" in evaluations.get("candidate_blocked_without_approval", {}).get("blocked_reasons", []), "ACB-CAP-04 workflow must block missing commercial terms")
    _require(evaluations.get("approval_still_blocked_in_phase_contract", {}).get("pilot_approved_allowed") is False, "ACB-CAP-04 workflow approval_still_blocked_in_phase_contract must not allow pilot")

    _require(pilot_scope.get("pilot_scope_defined") is True, "ACB-CAP-04 pilot_scope_contract pilot_scope_defined must be true")
    _require(pilot_scope.get("pilot_authorized") is False, "ACB-CAP-04 pilot_scope_contract pilot_authorized must be false")
    _require(pilot_scope.get("kill_switch_required") is True, "ACB-CAP-04 pilot_scope_contract kill_switch_required must be true")
    _require(pilot_scope.get("rollback_required") is True, "ACB-CAP-04 pilot_scope_contract rollback_required must be true")
    _require(pilot_scope.get("audit_ledger_required") is True, "ACB-CAP-04 pilot_scope_contract audit_ledger_required must be true")
    _require(pilot_scope.get("support_required") is True, "ACB-CAP-04 pilot_scope_contract support_required must be true")

    _require(evidence_contract.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 evidence_bundle_contract phase_id mismatch")
    _require(evidence_contract.get("hash_required_for_every_item") is True, "ACB-CAP-04 evidence_bundle_contract hash_required_for_every_item must be true")
    items = evidence_contract.get("items", [])
    _require(len(items) == 13, "ACB-CAP-04 evidence_bundle_contract must list 13 items")
    _require(all(item.get("hash_required") is True for item in items), "ACB-CAP-04 evidence_bundle_contract every item must require hash")

    _require(risk_matrix.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 pilot_risk_matrix phase_id mismatch")
    risks = risk_matrix.get("risks", [])
    risk_ids = {risk.get("risk_id") for risk in risks}
    _require("prompt_injection" in risk_ids, "ACB-CAP-04 risk matrix missing prompt_injection")
    _require("excessive_agency" in risk_ids, "ACB-CAP-04 risk matrix missing excessive_agency")
    _require("rollback_failure" in risk_ids, "ACB-CAP-04 risk matrix missing rollback_failure")
    _require("product_readiness_theater" in risk_ids, "ACB-CAP-04 risk matrix missing product_readiness_theater")

    _require(non_authorization.get("pilot_allowed_now") is False, "ACB-CAP-04 non_authorization_statement pilot_allowed_now must be false")
    _require(non_authorization.get("client_real_allowed_now") is False, "ACB-CAP-04 non_authorization_statement client_real_allowed_now must be false")
    _require(non_authorization.get("production_authorized") is False, "ACB-CAP-04 non_authorization_statement production_authorized must be false")
    _require(non_authorization.get("commercial_use_allowed") is False, "ACB-CAP-04 non_authorization_statement commercial_use_allowed must be false")
    _require(non_authorization.get("pricing_allowed") is False, "ACB-CAP-04 non_authorization_statement pricing_allowed must be false")
    _require(non_authorization.get("product_promotion_allowed") is False, "ACB-CAP-04 non_authorization_statement product_promotion_allowed must be false")
    _require(non_authorization.get("runtime_productive_activation") is False, "ACB-CAP-04 non_authorization_statement runtime_productive_activation must be false")
    _require(non_authorization.get("bedrock_required_before_product") is True, "ACB-CAP-04 non_authorization_statement bedrock_required_before_product must be true")
    _require(non_authorization.get("pilot_scope_defined") is True, "ACB-CAP-04 non_authorization_statement pilot_scope_defined must be true")
    _require(non_authorization.get("pilot_authorized") is False, "ACB-CAP-04 non_authorization_statement pilot_authorized must be false")

    _require(import_report.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 import_stability_report phase_id mismatch")
    _require(import_report.get("import_smoke_tests_passed") is True, "ACB-CAP-04 import_stability_report import_smoke_tests_passed must be true")
    _require(import_report.get("public_api_stable_or_ratified") is True, "ACB-CAP-04 import_stability_report public_api_stable_or_ratified must be true")
    _require(import_report.get("forbidden_runtime_patterns") == [], "ACB-CAP-04 import_stability_report forbidden_runtime_patterns must be empty")

    _require(public_api_drift.get("phase_id") == "ACB-CAP-04", "ACB-CAP-04 public_api_drift_report phase_id mismatch")
    _require(public_api_drift.get("root_removed_symbols") == [], "ACB-CAP-04 public_api_drift_report root_removed_symbols must be empty")
    _require(public_api_drift.get("root_added_symbols") == [], "ACB-CAP-04 public_api_drift_report root_added_symbols must be empty")
    _require(public_api_drift.get("product_boundary_exposed_as_submodule_only") is True, "ACB-CAP-04 public_api_drift_report product_boundary_exposed_as_submodule_only must be true")
    _require(public_api_drift.get("delta_ratified") is True, "ACB-CAP-04 public_api_drift_report delta_ratified must be true")

    _require("does not authorize" in runbook_text.lower(), "ACB-CAP-04 pilot_runbook_contract must state that it does not authorize the pilot")
    _require("operator-only" in runbook_text.lower(), "ACB-CAP-04 pilot_runbook_contract must be operator-only")

    _require("name: Product Pilot Boundary" in workflow_text, "ACB-CAP-04 workflow must be Product Pilot Boundary")
    _require("uv sync --frozen" in workflow_text, "ACB-CAP-04 workflow must run uv sync --frozen")
    _require("uv pip install --python .venv/bin/python pytest" in workflow_text, "ACB-CAP-04 workflow must install pytest via uv pip")
    _require("scripts/run_acb_cap_04_product_pilot_boundary.py" in workflow_text, "ACB-CAP-04 workflow must run the product pilot boundary artifact validator")
    _require("tests/test_acb_cap_04_product_pilot_boundary.py -v" in workflow_text, "ACB-CAP-04 workflow must run product pilot boundary tests")


def _check_acb_cap_05_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") in {"capability_build", "infernus_full"}, "phase_class must preserve capability-build baseline compatibility")
    _require(ACB_CAP_05_EVIDENCE_PATH.exists(), "missing ACB-CAP-05 evidence artifact in active-context")
    _require(ACB_CAP_05_RESYNC_PATH.exists(), "missing ACB-CAP-05 resync artifact in active-context")

    evidence_data = _load_json(ACB_CAP_05_EVIDENCE_PATH)
    resync_data = _load_json(ACB_CAP_05_RESYNC_PATH)
    _require(evidence_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 evidence phase_id mismatch")
    _require(evidence_data.get("project_repository") == "MatheusAugDEV/Project-A.R.I.S", "ACB-CAP-05 evidence repository mismatch")
    _require(
        evidence_data.get("project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA,
        "ACB-CAP-05 evidence project_sha mismatch",
    )
    _require(
        evidence_data.get("project_sha_before_resync") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA,
        "ACB-CAP-05 evidence project_sha_before_resync mismatch",
    )
    _require(
        evidence_data.get("project_sha_gate_start") == "b6044982c31e0861b481605c40bef673b249f351",
        "ACB-CAP-05 evidence project_sha_gate_start mismatch",
    )
    _require(
        evidence_data.get("advanced_supply_chain_ci", {}).get("conclusion") == "success",
        "ACB-CAP-05 evidence Advanced Supply Chain CI must be success",
    )
    _require(
        evidence_data.get("advanced_supply_chain_ci", {}).get("url")
        == ACB_CAP_05_ADVANCED_SUPPLY_CHAIN_CI_URL,
        "ACB-CAP-05 evidence Advanced Supply Chain CI URL mismatch",
    )
    _require(resync_data.get("artifact_id") == "acb_cap_05_project_sha_resync_2026_06_06", "ACB-CAP-05 resync artifact_id mismatch")
    _require(resync_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 resync phase_id mismatch")
    _require(resync_data.get("repair_type") == "project_sha_evidence_resync", "ACB-CAP-05 resync repair_type mismatch")
    _require(resync_data.get("decision") == "pass", "ACB-CAP-05 resync decision mismatch")
    _require(resync_data.get("root_cause") == "ACB-CAP-05 decision project_sha mismatch", "ACB-CAP-05 resync root_cause mismatch")
    _require(resync_data.get("previous_project_sha") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA, "ACB-CAP-05 resync previous_project_sha mismatch")
    _require(resync_data.get("new_project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA, "ACB-CAP-05 resync new_project_sha mismatch")
    _require(resync_data.get("project_decision_artifact_sha") == ACB_CAP_05_PROJECT_DECISION_SHA, "ACB-CAP-05 resync project_decision_artifact_sha mismatch")
    _require(resync_data.get("diff_classification") == "ACB_VALIDATION_ONLY", "ACB-CAP-05 resync diff_classification mismatch")
    for key in [
        "inf_full_opened",
        "next_phase_authorized_by_operator",
        "runtime_mutation_authorized",
        "product_promotion_allowed",
        "pilot_authorized",
        "bedrock_executed",
        "secret_access_attempted",
    ]:
        _require(
            resync_data.get("safety", {}).get(key) is False,
            f"ACB-CAP-05 resync safety flag {key} must be false",
        )
    _require(
        evidence_data.get("resync", {}).get("reason") == "ACB-CAP-05 decision project_sha mismatch",
        "ACB-CAP-05 evidence resync reason mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("previous_project_sha") == ACB_CAP_05_RESYNC_PREVIOUS_PROJECT_SHA,
        "ACB-CAP-05 evidence resync previous_project_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("new_project_sha") == ACB_CAP_05_RESYNC_NEW_PROJECT_SHA,
        "ACB-CAP-05 evidence resync new_project_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("project_decision_artifact_sha") == ACB_CAP_05_PROJECT_DECISION_SHA,
        "ACB-CAP-05 evidence resync project_decision_artifact_sha mismatch",
    )
    _require(
        evidence_data.get("resync", {}).get("operator_authorization_changed") is False,
        "ACB-CAP-05 evidence resync operator_authorization_changed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("inf_full_opened") is False,
        "ACB-CAP-05 evidence resync inf_full_opened must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("product_promotion_allowed") is False,
        "ACB-CAP-05 evidence resync product_promotion_allowed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("pilot_authorized") is False,
        "ACB-CAP-05 evidence resync pilot_authorized must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("bedrock_executed") is False,
        "ACB-CAP-05 evidence resync bedrock_executed must be false",
    )
    _require(
        evidence_data.get("resync", {}).get("runtime_mutation_authorized") is False,
        "ACB-CAP-05 evidence resync runtime_mutation_authorized must be false",
    )
    for key in [
        "supply_chain_package_exists",
        "sbom_integrity_checker_exists",
        "sbom_integrity_report_exists",
        "attestation_envelope_exists",
        "offline_signature_test_verification_exists",
        "pypi_vulnerability_range_monitor_exists",
        "pypi_vulnerability_range_scan_exists",
        "aibom_prototype_exists",
        "infernus_full_spec_exists",
        "advanced_supply_chain_tests_exist",
        "advanced_supply_chain_artifacts_exist",
    ]:
        _require(
            evidence_data.get("deliverables", {}).get(key) is True,
            f"ACB-CAP-05 evidence deliverable {key} must be true",
        )
    _require(
        evidence_data.get("local_validation", {}).get("pass_criteria_met") is True,
        "ACB-CAP-05 evidence pass_criteria_met must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("sbom_validation_passed") is True,
        "ACB-CAP-05 evidence sbom_validation_passed must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("attestation_verified") is True,
        "ACB-CAP-05 evidence attestation_verified must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("tamper_rejection_verified") is True,
        "ACB-CAP-05 evidence tamper_rejection_verified must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("infernus_spec_linked") is True,
        "ACB-CAP-05 evidence infernus_spec_linked must be true",
    )
    _require(
        evidence_data.get("local_validation", {}).get("bot_coverage_complete") is True,
        "ACB-CAP-05 evidence bot_coverage_complete must be true",
    )
    for key in [
        "network_attempted",
        "external_pypi_query_attempted",
        "sigstore_runtime_used",
        "pypi_upload_attempted",
        "secret_access_attempted",
        "production_signature_claimed",
        "product_promotion_allowed",
        "bedrock_executed",
        "pilot_authorized",
    ]:
        _require(
            evidence_data.get("safety", {}).get(key) is False,
            f"ACB-CAP-05 evidence safety flag {key} must be false",
        )

    artifacts_root = PROJECT_ROOT / "artifacts" / "acb_cap_05"
    required_paths = [
        PROJECT_ROOT / ".github" / "workflows" / "advanced_supply_chain.yml",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "__init__.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "sbom_integrity.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "attestation_envelope.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "pypi_vulnerability_range_monitor.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "aibom_prototype.py",
        PROJECT_ROOT / "src" / "aris" / "supply_chain" / "advanced_supply_chain_gate.py",
        PROJECT_ROOT / "scripts" / "run_acb_cap_05_advanced_supply_chain_gate.py",
        PROJECT_ROOT / "tests" / "test_acb_cap_05_advanced_supply_chain_gate.py",
        PROJECT_ROOT / "docs" / "infernus_full" / "infernus_full_execution_spec.md",
        artifacts_root / "sbom_integrity_report.json",
        artifacts_root / "attestation_envelope.json",
        artifacts_root / "pypi_vulnerability_range_scan.json",
        artifacts_root / "aibom_prototype.json",
        artifacts_root / "infernus_full_spec_linkage.json",
        artifacts_root / "advanced_supply_chain_decision.json",
        artifacts_root / "advanced_supply_chain_summary.json",
        artifacts_root / "advanced_supply_chain_report.md",
        artifacts_root / "pypi_vulnerability_ranges_fixture.json",
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if external_project_available:
        for path in required_paths:
            _require(path.exists(), f"missing ACB-CAP-05 project artifact: {path.relative_to(PROJECT_ROOT)}")

    if not external_project_available:
        return

    decision_data = _load_json(artifacts_root / "advanced_supply_chain_decision.json")
    summary_data = _load_json(artifacts_root / "advanced_supply_chain_summary.json")
    sbom_report = _load_json(artifacts_root / "sbom_integrity_report.json")
    attestation_envelope = _load_json(artifacts_root / "attestation_envelope.json")
    vulnerability_scan = _load_json(artifacts_root / "pypi_vulnerability_range_scan.json")
    aibom_prototype = _load_json(artifacts_root / "aibom_prototype.json")
    spec_linkage = _load_json(artifacts_root / "infernus_full_spec_linkage.json")
    workflow_text = (PROJECT_ROOT / ".github" / "workflows" / "advanced_supply_chain.yml").read_text(encoding="utf-8")
    spec_text = (PROJECT_ROOT / "docs" / "infernus_full" / "infernus_full_execution_spec.md").read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == "ARIS Capability Build Advanced Supply Chain Gate", "ACB-CAP-05 decision phase_name mismatch")
    _require(decision_data.get("status") == "acb_cap_05_pass", "ACB-CAP-05 decision status mismatch")
    _require(decision_data.get("decision") == "pass", "ACB-CAP-05 decision must be pass")
    _require(decision_data.get("pass_criteria_met") is True, "ACB-CAP-05 decision pass_criteria_met must be true")
    _require(decision_data.get("sbom_validation_passed") is True, "ACB-CAP-05 decision sbom_validation_passed must be true")
    _require(decision_data.get("attestation_verified") is True, "ACB-CAP-05 decision attestation_verified must be true")
    _require(decision_data.get("tamper_rejection_verified") is True, "ACB-CAP-05 decision tamper_rejection_verified must be true")
    _require(decision_data.get("infernus_spec_linked") is True, "ACB-CAP-05 decision infernus_spec_linked must be true")
    _require(decision_data.get("forbidden_import_findings") == [], "ACB-CAP-05 decision forbidden_import_findings must be empty")
    for key in [
        "network_attempted",
        "external_pypi_query_attempted",
        "sigstore_runtime_used",
        "pypi_upload_attempted",
        "secret_access_attempted",
        "production_signature_claimed",
        "product_promotion_allowed",
        "pilot_authorized",
        "bedrock_executed",
        "infernus_full_opened",
    ]:
        _require(decision_data.get(key) is False, f"ACB-CAP-05 decision {key} must be false")
    _require(
        decision_data.get("project_sha")
        == ACB_CAP_05_PROJECT_DECISION_SHA,
        "ACB-CAP-05 decision project_sha mismatch",
    )

    _require(summary_data.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 summary phase_id mismatch")
    _require(summary_data.get("offline_detection_count") == 1, "ACB-CAP-05 summary offline_detection_count mismatch")
    _require(summary_data.get("offline_unknown_count") == 15, "ACB-CAP-05 summary offline_unknown_count mismatch")
    _require(summary_data.get("forbidden_import_findings") == [], "ACB-CAP-05 summary forbidden_import_findings must be empty")
    _require(summary_data.get("tamper_rejection_verified") is True, "ACB-CAP-05 summary tamper_rejection_verified must be true")

    _require(sbom_report.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 sbom_integrity_report phase_id mismatch")
    _require(sbom_report.get("validation_passed") is True, "ACB-CAP-05 sbom_integrity_report validation_passed must be true")
    _require(sbom_report.get("complete_sbom_claimed") is False, "ACB-CAP-05 sbom_integrity_report complete_sbom_claimed must be false")
    _require(sbom_report.get("component_count") == 18, "ACB-CAP-05 sbom_integrity_report component_count mismatch")

    _require(attestation_envelope.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 attestation_envelope phase_id mismatch")
    _require(attestation_envelope.get("signature_mode") == "offline_test_hmac_not_production_signature", "ACB-CAP-05 attestation signature_mode mismatch")
    _require(attestation_envelope.get("production_signature_claimed") is False, "ACB-CAP-05 attestation production_signature_claimed must be false")
    _require(attestation_envelope.get("sigstore_runtime_used") is False, "ACB-CAP-05 attestation sigstore_runtime_used must be false")
    _require(attestation_envelope.get("pypi_upload_used") is False, "ACB-CAP-05 attestation pypi_upload_used must be false")
    _require(attestation_envelope.get("trusted_publishing_used") is False, "ACB-CAP-05 attestation trusted_publishing_used must be false")

    _require(vulnerability_scan.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 vulnerability scan phase_id mismatch")
    _require(vulnerability_scan.get("external_monitoring_allowed") is False, "ACB-CAP-05 vulnerability scan external_monitoring_allowed must be false")
    _require(len(vulnerability_scan.get("detected_by_offline_fixture", [])) == 1, "ACB-CAP-05 vulnerability scan must detect exactly 1 offline advisory")
    _require(len(vulnerability_scan.get("unknown_due_to_no_external_network", [])) == 15, "ACB-CAP-05 vulnerability scan unknown count mismatch")

    _require(aibom_prototype.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 aibom_prototype phase_id mismatch")
    _require(aibom_prototype.get("completeness") == "prototype_partial", "ACB-CAP-05 aibom_prototype completeness mismatch")
    _require(aibom_prototype.get("production_claim") is False, "ACB-CAP-05 aibom_prototype production_claim must be false")
    _require(aibom_prototype.get("spdx_conformance_claimed") is False, "ACB-CAP-05 aibom_prototype spdx_conformance_claimed must be false")
    _require(aibom_prototype.get("cyclonedx_conformance_claimed") is False, "ACB-CAP-05 aibom_prototype cyclonedx_conformance_claimed must be false")

    _require(spec_linkage.get("phase_id") == "ACB-CAP-05", "ACB-CAP-05 infernus_full_spec_linkage phase_id mismatch")
    _require(spec_linkage.get("all_required_sections_present") is True, "ACB-CAP-05 infernus_full_spec_linkage all_required_sections_present must be true")
    _require(spec_linkage.get("documented_bot_count") == 13, "ACB-CAP-05 infernus_full_spec_linkage documented_bot_count mismatch")
    _require(spec_linkage.get("bot_coverage_complete") is True, "ACB-CAP-05 infernus_full_spec_linkage bot_coverage_complete must be true")
    _require(spec_linkage.get("operator_only_open_gate") is True, "ACB-CAP-05 infernus_full_spec_linkage operator_only_open_gate must be true")
    _require(spec_linkage.get("product_or_pilot_authorized") is False, "ACB-CAP-05 infernus_full_spec_linkage product_or_pilot_authorized must be false")

    _require("name: Advanced Supply Chain" in workflow_text, "ACB-CAP-05 workflow must be Advanced Supply Chain")
    _require("python -m py_compile" in workflow_text, "ACB-CAP-05 workflow must run py_compile")
    _require("python -m unittest tests.test_acb_cap_05_advanced_supply_chain_gate -q" in workflow_text, "ACB-CAP-05 workflow must run focused unittest")
    _require("python scripts/run_acb_cap_05_advanced_supply_chain_gate.py" in workflow_text, "ACB-CAP-05 workflow must run the advanced supply chain runner")
    _require("python -m json.tool artifacts/acb_cap_05/advanced_supply_chain_decision.json" in workflow_text, "ACB-CAP-05 workflow must validate generated JSON artifacts")

    _require("## 13 Bots" in spec_text, "ACB-CAP-05 infernus spec must include 13 bots section")
    _require(
        "operator explicitly opens" in spec_text.lower() or "explicit operator authorization" in spec_text.lower(),
        "ACB-CAP-05 infernus spec must be operator-gated",
    )
    _require("must not authorize product rollout" in spec_text.lower(), "ACB-CAP-05 infernus spec must prohibit product rollout")


def _check_inf_full_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") == "infernus_full", "phase_class must be infernus_full")

    required_paths = [
        INF_FULL_01_SCOPE_DECISION_PATH,
        INF_FULL_01_SCOPE_MATRIX_PATH,
        INF_FULL_01_SCOPE_MANIFEST_PATH,
        INF_FULL_01_SCOPE_CHARTER_PATH,
    ]
    external_project_available = all(path.exists() for path in required_paths)
    if not external_project_available:
        return
    for path in required_paths:
        _require(path.exists(), f"missing INF-FULL-01 scope artifact: {path.relative_to(PROJECT_ROOT)}")

    decision_data = _load_json(INF_FULL_01_SCOPE_DECISION_PATH)
    matrix_data = _load_json(INF_FULL_01_SCOPE_MATRIX_PATH)
    manifest_data = _load_json(INF_FULL_01_SCOPE_MANIFEST_PATH)
    charter_text = INF_FULL_01_SCOPE_CHARTER_PATH.read_text(encoding="utf-8")

    _require(
        decision_data == {
            "artifact_id": "inf_full_01_scope_charter_decision_2026_06_06",
            "phase_id": "INF-FULL-01",
            "phase_name": "ARIS Infernus Full Scope Charter Gate",
            "artifact_type": "operator_authorized_scope_charter",
            "decision": "pass",
            "status": "inf_full_01_scope_charter_pass",
            "operator_authorized": True,
            "authorization_scope": "open_inf_full_01_scope_charter_only",
            "bots_executed": False,
            "runtime_execution_authorized": False,
            "product_promotion_allowed": False,
            "pilot_authorized": False,
            "bedrock_executed": False,
            "secret_access_authorized": False,
            "network_execution_authorized": False,
            "initial_scope_rule": "uncertain_modules_included_to_avoid_false_negative",
            "safe_to_execute_bots_now": False,
            "next_execution_requires_separate_gate": True,
            "scope_counts": {
                "acb_core": 5,
                "ativo_critico": 5,
                "incerto_included": 16,
                "secondary": 13,
                "quarantine_with_hash": 2,
            },
            "inf_full_opened": True,
            "next_phase": None,
            "next_phase_authorized_by_operator": False,
        },
        "INF-FULL-01 scope decision artifact mismatch",
    )

    expected_bucket_map = {
        "backend": "acb_core",
        "mcp_runtime": "acb_core",
        "runtime": "acb_core",
        "product_boundary": "acb_core",
        "supply_chain": "acb_core",
        "actions": "ativo_critico",
        "app": "ativo_critico",
        "config": "ativo_critico",
        "logging": "ativo_critico",
        "security": "ativo_critico",
        "action_runtime": "incerto_included",
        "action_runtime_contracts": "incerto_included",
        "audio": "incerto_included",
        "bedrock": "incerto_included",
        "capabilities": "incerto_included",
        "context": "incerto_included",
        "evaluation": "incerto_included",
        "intelligence": "incerto_included",
        "knowledge": "incerto_included",
        "lab": "incerto_included",
        "memory": "incerto_included",
        "persona": "incerto_included",
        "response": "incerto_included",
        "turn": "incerto_included",
        "ui": "incerto_included",
        "voice": "incerto_included",
        "cockpit": "secondary",
        "hardening_base": "secondary",
        "intents": "secondary",
        "lab_simulation": "secondary",
        "learning": "secondary",
        "model_gateway": "secondary",
        "product_loop": "secondary",
        "research": "secondary",
        "response_quality": "secondary",
        "rich_output": "secondary",
        "roadmap": "secondary",
        "sandbox": "secondary",
        "understanding": "secondary",
        "diagnostics": "quarantine_with_hash",
        "packaging": "quarantine_with_hash",
    }

    matrix_modules = matrix_data.get("modules", [])
    _require(matrix_data.get("artifact_id") == "inf_full_01_scope_matrix_2026_06_06", "INF-FULL-01 scope matrix artifact_id mismatch")
    _require(matrix_data.get("phase_id") == "INF-FULL-01", "INF-FULL-01 scope matrix phase_id mismatch")
    _require(
        matrix_data.get("scope_rule") == "uncertain_modules_included_to_avoid_false_negative",
        "INF-FULL-01 scope matrix scope_rule mismatch",
    )
    _require(len(matrix_modules) == len(expected_bucket_map), "INF-FULL-01 scope matrix module count mismatch")

    seen_modules = set()
    for item in matrix_modules:
        module = item.get("module")
        bucket = item.get("bucket")
        _require(module in expected_bucket_map, f"unexpected module in INF-FULL-01 scope matrix: {module}")
        _require(bucket == expected_bucket_map[module], f"bucket mismatch for module {module}")
        _require(isinstance(item.get("reason"), str) and item["reason"], f"missing reason for module {module}")
        _require(isinstance(item.get("risk_if_excluded"), str) and item["risk_if_excluded"], f"missing risk_if_excluded for module {module}")
        _require(isinstance(item.get("source_diagnostic_status"), str) and item["source_diagnostic_status"], f"missing source_diagnostic_status for module {module}")
        if bucket in {"acb_core", "ativo_critico", "incerto_included"}:
            _require(item.get("include_in_initial_infernus_scope") is True, f"{module} must be in initial scope")
            _require(item.get("attack_required") is True, f"{module} must require attack coverage")
            _require(item.get("include_in_secondary_scope") is False, f"{module} must not be marked as secondary")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        elif bucket == "secondary":
            _require(item.get("include_in_initial_infernus_scope") is False, f"{module} must not be in initial scope")
            _require(item.get("include_in_secondary_scope") is True, f"{module} must be in secondary scope")
            _require(item.get("attack_required") is False, f"{module} must not require initial attack")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        else:
            _require(item.get("include_in_initial_infernus_scope") is False, f"{module} must not be in initial scope")
            _require(item.get("include_in_secondary_scope") is False, f"{module} must not be in secondary scope")
            _require(item.get("attack_required") is False, f"{module} must not require initial attack")
            _require(item.get("baseline_hash_required") is True, f"{module} must require baseline hash")
        seen_modules.add(module)
    _require(seen_modules == set(expected_bucket_map), "INF-FULL-01 scope matrix module set mismatch")

    _require(
        manifest_data == {
            "artifact_id": "inf_full_01_module_scope_manifest_2026_06_06",
            "phase_id": "INF-FULL-01",
            "initial_attack_scope_modules": [
                "backend", "mcp_runtime", "runtime", "product_boundary", "supply_chain",
                "actions", "app", "config", "logging", "security",
                "action_runtime", "action_runtime_contracts", "audio", "bedrock", "capabilities",
                "context", "evaluation", "intelligence", "knowledge", "lab", "memory",
                "persona", "response", "turn", "ui", "voice",
            ],
            "secondary_scope_modules": [
                "cockpit", "hardening_base", "intents", "lab_simulation", "learning",
                "model_gateway", "product_loop", "research", "response_quality",
                "rich_output", "roadmap", "sandbox", "understanding",
            ],
            "quarantine_hash_only_modules": [
                "diagnostics", "packaging",
            ],
            "all_modules_accounted_for": True,
            "unresolved_modules": [],
            "false_negative_policy": "include_uncertain_modules_in_initial_scope",
            "baseline_freeze_requirements": {
                "all_scoped_modules_require_hashes": True,
                "quarantine_modules_require_hashes": True,
                "baseline_freeze_must_precede_attack_waves": True,
            },
            "handoff_policy": {
                "next_gate": "INF-FULL-02 Baseline Freeze Planning",
                "bots_executed": False,
                "runtime_execution_authorized": False,
                "operator_reauthorization_required_for_execution": True,
            },
            "bots_executed": False,
            "runtime_execution_authorized": False,
        },
        "INF-FULL-01 scope manifest mismatch",
    )

    for phrase in [
        "# INF-FULL-01 Scope Charter",
        "PASS — INF-FULL-01 scope charter is opened by operator authorization.",
        "This opens scope/charter only.",
        "No bots are executed.",
        "No runtime is started.",
        "Uncertain included:",
        "diagnostics, packaging.",
        "INF-FULL-02 must be Baseline Freeze Planning.",
    ]:
        _require(phrase in charter_text, f"INF-FULL-01 scope charter missing phrase: {phrase}")

    _require(state.get("current_phase_bots_executed") is False, "current_phase_bots_executed must be false")


def _check_inf_full_02_project_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_02_DECISION_PATH)
    inventory_data = _load_json(INF_FULL_02_INVENTORY_PATH)
    hash_manifest = _load_json(INF_FULL_02_HASH_MANIFEST_PATH)
    summary_data = _load_json(INF_FULL_02_SUMMARY_PATH)
    planning_text = INF_FULL_02_PLANNING_DOC_PATH.read_text(encoding="utf-8")

    _require(decision_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == INF_FULL_02_PHASE, "INF-FULL-02 decision phase_name mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-FULL-01", "INF-FULL-02 previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "INF-FULL-02 decision must be pass")
    _require(decision_data.get("status") == INF_FULL_02_STATUS, "INF-FULL-02 decision status mismatch")
    _require(decision_data.get("operator_authorization_source") == "chat_operator_said_vamos_continuar_2026_06_06", "INF-FULL-02 operator authorization source mismatch")
    _require(decision_data.get("baseline_freeze_planned") is True, "INF-FULL-02 baseline_freeze_planned must be true")
    _require(decision_data.get("baseline_freeze_applied") is False, "INF-FULL-02 baseline_freeze_applied must be false")
    _require(decision_data.get("bot_execution_allowed") is False, "INF-FULL-02 bot_execution_allowed must be false")
    _require(decision_data.get("bot_execution_executed") is False, "INF-FULL-02 bot_execution_executed must be false")
    _require(decision_data.get("runtime_execution_authorized") is False, "INF-FULL-02 runtime_execution_authorized must be false")
    _require(decision_data.get("product_ready") is False, "INF-FULL-02 product_ready must be false")
    _require(decision_data.get("bedrock_execution_authorized") is False, "INF-FULL-02 bedrock_execution_authorized must be false")
    _require(decision_data.get("external_network_authorized") is False, "INF-FULL-02 external_network_authorized must be false")
    _require(decision_data.get("secrets_access_authorized") is False, "INF-FULL-02 secrets_access_authorized must be false")
    _require(decision_data.get("minimum_deliverable_met") is True, "INF-FULL-02 minimum_deliverable_met must be true")
    _require(decision_data.get("next_phase") is None, "INF-FULL-02 next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "INF-FULL-02 next_phase_authorized_by_operator must be false")

    _require(inventory_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 inventory phase_id mismatch")
    _require(inventory_data.get("phase_name") == INF_FULL_02_PHASE, "INF-FULL-02 inventory phase_name mismatch")
    _require(inventory_data.get("classification_labels") == [
        "active_baseline_candidate",
        "historical_only",
        "quarantine_hash_only",
        "excluded_with_reason",
        "missing_expected_blocking",
    ], "INF-FULL-02 classification labels mismatch")
    _require(len(inventory_data.get("module_inventory", [])) == 41, "INF-FULL-02 module inventory count mismatch")
    quarantine = {
        item.get("module")
        for item in inventory_data.get("module_inventory", [])
        if item.get("classification") == "quarantine_hash_only"
    }
    _require(quarantine == {"diagnostics", "packaging"}, "INF-FULL-02 quarantine module set mismatch")
    _require(len(inventory_data.get("scenario_inventory", [])) == 13, "INF-FULL-02 scenario inventory count mismatch")
    _require(inventory_data.get("inventory_counts", {}).get("historical_only") == 3, "INF-FULL-02 historical count mismatch")
    _require(inventory_data.get("blocking_inventory", [{}])[0].get("classification") == "missing_expected_blocking", "INF-FULL-02 blocking inventory mismatch")

    _require(hash_manifest.get("phase_id") == "INF-FULL-02", "INF-FULL-02 hash manifest phase_id mismatch")
    _require(hash_manifest.get("hash_algorithm") == "sha256", "INF-FULL-02 hash algorithm mismatch")
    _require(hash_manifest.get("directory_hash_algorithm") == 'sha256(sorted("relative_path:file_sha256"))', "INF-FULL-02 directory hash algorithm mismatch")
    ref_paths = {entry.get("path") for entry in hash_manifest.get("reference_hashes", [])}
    for required_path in [
        "aris-active-context/ACTIVE_CONTEXT_STATE.json",
        "aris-active-context/ROADMAP_CANONICAL.md",
        "artifacts/infernus/inf_full_02_baseline_freeze_planning_decision_2026_06_06.json",
        "artifacts/infernus/inf_full_02_baseline_freeze_inventory_2026_06_06.json",
        "artifacts/infernus/inf_full_02_baseline_freeze_summary_2026_06_06.json",
        "docs/infernus_full/inf_full_02_baseline_freeze_planning_2026_06_06.md",
        "aris-active-context/artifacts/inf_bot_01/nemesis_execution_log.json",
        "aris-active-context/artifacts/inf_minos_01/minos_verdict.json",
        "aris-active-context/artifacts/purg_01/finding_nemesis_validator_bypass.json",
        "src/aris/diagnostics",
        "src/aris/packaging",
    ]:
        _require(required_path in ref_paths, f"INF-FULL-02 hash manifest missing path: {required_path}")
    _require(len(hash_manifest.get("reference_hashes", [])) >= 60, "INF-FULL-02 hash manifest is too small")

    _require(summary_data.get("phase_id") == "INF-FULL-02", "INF-FULL-02 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-02 summary decision mismatch")
    _require(summary_data.get("status") == INF_FULL_02_STATUS, "INF-FULL-02 summary status mismatch")
    _require(summary_data.get("question_6_next_phase_after_inf_full_02", {}).get("canonical_next_phase") is None, "INF-FULL-02 summary canonical_next_phase must be null")

    for phrase in [
        "baseline_freeze_planned: `true`",
        "baseline_freeze_applied: `false`",
        "No canonical successor is currently defined for INF-FULL-02 in ROADMAP_CANONICAL.md.",
        "Historical-only reference set:",
        "Quarantine hash-only modules:",
    ]:
        _require(phrase in planning_text, f"INF-FULL-02 planning doc missing phrase: {phrase}")


def _check_inf_full_03_project_artifacts(state: dict[str, Any]) -> None:
    decision_data = _load_json(INF_FULL_03_DECISION_PATH)
    summary_data = _load_json(INF_FULL_03_SUMMARY_PATH)
    transition_data = _load_json(IF00_TRANSITION_CANDIDATE_PATH)
    hermeticity_data = _load_json(IF00_HERMETICITY_PATH)
    ontology_data = _load_json(IF02_ONTOLOGY_PATH)
    oracle_data = _load_json(IF03_ORACLE_PACK_PATH)
    bot_pack_data = _load_json(IF04_BOT_PACK_PATH)
    permission_data = _load_json(IF04_PERMISSION_PATH)
    docs_readme_text = INFERNUS_FULL_DOCS_README_PATH.read_text(encoding="utf-8")
    opening_text = INF_FULL_03_OPENING_DOC_PATH.read_text(encoding="utf-8")
    canonroadmap_text = INFERNUS_FULL_CANONROADMAP_PATH.read_text(encoding="utf-8")
    ledger_lines = [line for line in IF01_LEDGER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    coverage_lines = [line for line in IF02_COVERAGE_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]

    _require(decision_data.get("phase_id") == "INF-FULL-03", "INF-FULL-03 decision phase_id mismatch")
    _require(decision_data.get("phase_name") == EXPECTED_PHASE, "INF-FULL-03 decision phase_name mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-FULL-02", "INF-FULL-03 decision previous_phase_id mismatch")
    _require(decision_data.get("decision") == "pass", "INF-FULL-03 decision must be pass")
    _require(decision_data.get("status") == EXPECTED_STATUS, "INF-FULL-03 decision status mismatch")
    _require(decision_data.get("operator_authorization_source") == "chat_operator_said_ok_autorizo_td_infernus_full_2026_06_06", "INF-FULL-03 operator authorization source mismatch")
    _require(decision_data.get("full_infernus_chain_registered") is True, "INF-FULL-03 full_infernus_chain_registered must be true")
    _require(decision_data.get("canon_roadmap_persisted") is True, "INF-FULL-03 canon_roadmap_persisted must be true")
    _require(decision_data.get("baseline_freeze_dependency_satisfied") is True, "INF-FULL-03 baseline_freeze_dependency_satisfied must be true")
    _require(decision_data.get("minimum_deliverable_met") is True, "INF-FULL-03 minimum_deliverable_met must be true")
    _require(decision_data.get("bot_execution_allowed") is False, "INF-FULL-03 bot_execution_allowed must be false")
    _require(decision_data.get("bot_execution_executed") is False, "INF-FULL-03 bot_execution_executed must be false")
    _require(decision_data.get("runtime_execution_authorized") is False, "INF-FULL-03 runtime_execution_authorized must be false")
    _require(decision_data.get("product_ready") is False, "INF-FULL-03 product_ready must be false")
    _require(decision_data.get("bedrock_execution_authorized") is False, "INF-FULL-03 bedrock_execution_authorized must be false")
    _require(decision_data.get("external_network_authorized") is False, "INF-FULL-03 external_network_authorized must be false")
    _require(decision_data.get("secrets_access_authorized") is False, "INF-FULL-03 secrets_access_authorized must be false")
    _require(decision_data.get("dependency_change_authorized") is False, "INF-FULL-03 dependency_change_authorized must be false")
    _require(decision_data.get("next_phase") is None, "INF-FULL-03 next_phase must be null")
    _require(decision_data.get("next_phase_authorized_by_operator") is False, "INF-FULL-03 next_phase_authorized_by_operator must be false")
    _require(len(decision_data.get("registered_chain_stages", [])) == 11, "INF-FULL-03 registered_chain_stages count mismatch")

    _require(summary_data.get("phase_id") == "INF-FULL-03", "INF-FULL-03 summary phase_id mismatch")
    _require(summary_data.get("decision") == "pass", "INF-FULL-03 summary decision mismatch")
    _require(summary_data.get("status") == EXPECTED_STATUS, "INF-FULL-03 summary status mismatch")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("full_chain_registered") is True, "INF-FULL-03 summary must mark full_chain_registered")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("inf_full_03_opened") is True, "INF-FULL-03 summary must mark inf_full_03_opened")
    _require(summary_data.get("operator_authorization_interpretation", {}).get("bot_execution_authorized_now") is False, "INF-FULL-03 summary bot_execution_authorized_now must be false")
    _require(summary_data.get("next_phase_after_inf_full_03", {}).get("canonical_next_phase") is None, "INF-FULL-03 summary canonical_next_phase must be null")

    _require(transition_data.get("phase_id") == "INF-FULL-03", "if00 transition candidate phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("from_phase_id") == "INF-FULL-02", "if00 transition candidate from_phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("to_phase_id") == "INF-FULL-03", "if00 transition candidate to_phase_id mismatch")
    _require(transition_data.get("candidate_transition", {}).get("advance_mode") == "operator", "if00 transition candidate advance_mode mismatch")
    _require(transition_data.get("bot_execution_authorized") is False, "if00 transition candidate bot_execution_authorized must be false")
    _require(transition_data.get("runtime_authorized") is False, "if00 transition candidate runtime_authorized must be false")

    _require(hermeticity_data.get("phase_id") == "INF-FULL-03", "if00 hermeticity phase_id mismatch")
    _require(hermeticity_data.get("decision") == "pass", "if00 hermeticity decision mismatch")
    _require(hermeticity_data.get("hermeticity_contract", {}).get("lab_runtime_started") is False, "if00 hermeticity lab_runtime_started must be false")
    _require(hermeticity_data.get("hermeticity_contract", {}).get("bots_may_run") is False, "if00 hermeticity bots_may_run must be false")
    _require(hermeticity_data.get("baseline_freeze_dependency", {}).get("baseline_freeze_planned") is True, "if00 hermeticity baseline_freeze_planned must be true")
    _require(hermeticity_data.get("baseline_freeze_dependency", {}).get("baseline_freeze_applied") is False, "if00 hermeticity baseline_freeze_applied must be false")

    _require(len(ledger_lines) >= 5, "if01 evidence ledger must contain at least 5 claims")
    _require(all(json.loads(line).get("accepted_for_inf_full_03") is True for line in ledger_lines), "if01 evidence ledger claims must all be accepted_for_inf_full_03")
    _require(any(json.loads(line).get("topic") == "transition_candidate" for line in ledger_lines), "if01 evidence ledger must contain transition_candidate")

    _require(ontology_data.get("phase_id") == "INF-FULL-03", "if02 ontology phase_id mismatch")
    _require(ontology_data.get("ontology_version") == "v4", "if02 ontology version mismatch")
    _require(ontology_data.get("planning_only") is True, "if02 ontology planning_only must be true")
    _require(len(ontology_data.get("threat_families", [])) == 8, "if02 ontology threat family count mismatch")

    _require(len(coverage_lines) >= 2, "if02 coverage matrix must contain header and rows")
    _require(coverage_lines[0] == "threat_id,threat_name,seed_bots,seed_artifacts,evidence_required,inf_full_03_status", "if02 coverage matrix header mismatch")
    _require(any("conditional_planning_only" in line for line in coverage_lines[1:]), "if02 coverage matrix must include conditional_planning_only row")

    _require(oracle_data.get("phase_id") == "INF-FULL-03", "if03 oracle pack phase_id mismatch")
    _require(oracle_data.get("planning_only") is True, "if03 oracle pack planning_only must be true")
    _require(oracle_data.get("global_oracle_rules", {}).get("deterministic_oracles_required") is True, "if03 oracle pack deterministic_oracles_required must be true")
    _require(len(oracle_data.get("metrics_contracts", [])) >= 7, "if03 oracle pack metrics_contracts count mismatch")

    _require(bot_pack_data.get("phase_id") == "INF-FULL-03", "if04 bot pack phase_id mismatch")
    _require(bot_pack_data.get("planning_only") is True, "if04 bot pack planning_only must be true")
    _require(bot_pack_data.get("bot_count_canonical") == 15, "if04 bot pack bot_count_canonical mismatch")
    _require(bot_pack_data.get("bot_count_conditional") == 1, "if04 bot pack bot_count_conditional mismatch")
    _require(any(bot.get("name") == "Minos" and bot.get("contract_status") == "registered_as_auditor_only" for bot in bot_pack_data.get("bots", [])), "if04 bot pack must register Minos as auditor only")

    _require(permission_data.get("phase_id") == "INF-FULL-03", "if04 permission manifest phase_id mismatch")
    _require(permission_data.get("planning_only") is True, "if04 permission manifest planning_only must be true")
    _require(permission_data.get("capability_guards", {}).get("bot_execution_allowed") is False, "if04 permission manifest bot_execution_allowed must be false")
    _require(permission_data.get("capability_guards", {}).get("runtime_execution_allowed") is False, "if04 permission manifest runtime_execution_allowed must be false")
    _require("execute bots" in permission_data.get("forbidden_capabilities", []), "if04 permission manifest must forbid bot execution")

    for phrase in [
        "# INF-FULL-03 Chain Registration & Preparation Opening",
        "Decision: `pass`",
        "The full planned chain is recorded as:",
        "Only `INF-FULL-03` is opened canonically here.",
        "No bot execution.",
        "No runtime start.",
        "No Bedrock execution.",
    ]:
        _require(phrase in opening_text, f"INF-FULL-03 opening doc missing phrase: {phrase}")

    for phrase in [
        "INF-FULL-02 | pass",
        "→ INF-FULL-03 | infernus_full | operator",
        "if00_transition_candidate.json",
        "if04_permission_manifest_v4.json",
        "## INF-FULL-03 não deve incluir",
        "- execution;",
        "- Bedrock;",
        "- product;",
        "- secrets;",
        "- package install;",
    ]:
        _require(phrase in canonroadmap_text, f"infernus_full_canonroadmap.md missing phrase: {phrase}")

    _require(INFERNUS_FULL_SUPERSESSION_PATH.exists(), "missing infernus_full canonroadmap supersession artifact")
    _require("docs/infernus_full/infernus_full_canonroadmap.md" in docs_readme_text, "docs/infernus_full/README.md must point to infernus_full_canonroadmap.md")
    _require("inf_full_03_opening_2026_06_06.md" in docs_readme_text, "docs/infernus_full/README.md must reference INF-FULL-03 opening doc")


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


def _check_bot_execution_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("bot_execution_executed") is True, "bot_execution_executed must be true")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must be 1")

    artifacts_root = ROOT / "artifacts/inf_bot_01"
    _require(artifacts_root.exists(), "artifacts/inf_bot_01 must exist")

    log_paths = sorted(artifacts_root.glob("*execution_log.json"))
    _require(len(log_paths) == 1, f"expected exactly 1 bot execution log, found {len(log_paths)}")
    log_path = log_paths[0]
    _require(log_path.name == "nemesis_execution_log.json", "unexpected bot execution log filename")

    log_data = _load_json(log_path)
    _require(log_data.get("bot_id") == "nemesis", "bot_id must be nemesis")
    _require(log_data.get("scenario_id") == "scenario_11_nemesis", "scenario_id must be scenario_11_nemesis")
    _require(log_data.get("mode") == "synthetic_deterministic_execution", "mode must be synthetic_deterministic_execution")
    _require(log_data.get("runtime_execution") is False, "runtime_execution must be false")
    _require(log_data.get("autonomous_execution") is False, "autonomous_execution must be false")
    _require(log_data.get("network_used") is False, "network_used must be false")
    _require(log_data.get("secrets_accessed") is False, "secrets_accessed must be false")
    _require(log_data.get("decision") == "block", "bot execution decision must be block")
    _require(log_data.get("reason") == "validator_bypass_injection_detected", "unexpected bot execution reason")
    _require(bool(log_data.get("log_sha256")), "log_sha256 must be non-empty")
    actual_log_sha256 = hashlib.sha256(log_path.read_bytes()).hexdigest()

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/inf_bot_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "INF-BOT-01", "decision.json phase_id mismatch")
    _require(decision_data.get("phase_class") == "bot_execution", "decision.json phase_class mismatch")
    _require(decision_data.get("actual_decision") == "block", "decision.json actual_decision must be block")
    _require(decision_data.get("expected_decision") == "block", "decision.json expected_decision must be block")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")
    _require(decision_data.get("execution_log_sha256") == actual_log_sha256, "decision.json execution_log_sha256 mismatch")


def _check_minos_verdict_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("minos_verdict_executed") is True, "minos_verdict_executed must be true")
    _require(state.get("minos_verdict_count") == 1, "minos_verdict_count must be 1")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must remain 1")

    artifacts_root = ROOT / "artifacts/inf_minos_01"
    _require(artifacts_root.exists(), "artifacts/inf_minos_01 must exist")

    verdict_paths = sorted(artifacts_root.glob("*verdict.json"))
    _require(len(verdict_paths) == 1, f"expected exactly 1 Minos verdict JSON, found {len(verdict_paths)}")
    verdict_path = verdict_paths[0]
    _require(verdict_path.name == "minos_verdict.json", "unexpected Minos verdict filename")

    verdict_data = _load_json(verdict_path)
    source_log_path = ROOT / "artifacts/inf_bot_01/nemesis_execution_log.json"
    source_log_sha256 = hashlib.sha256(source_log_path.read_bytes()).hexdigest()
    actual_verdict_sha256 = hashlib.sha256(verdict_path.read_bytes()).hexdigest()

    _require(verdict_data.get("phase_id") == "INF-MINOS-01", "minos_verdict phase_id mismatch")
    _require(verdict_data.get("source_phase_id") == "INF-BOT-01", "minos_verdict source_phase_id mismatch")
    _require(verdict_data.get("verdict_id") == "minos_nemesis_validator_bypass_verdict", "unexpected verdict_id")
    _require(verdict_data.get("engine") == "minos_deterministic_threshold_v1", "unexpected engine")
    _require(verdict_data.get("llm_as_judge") is False, "llm_as_judge must be false")
    _require(verdict_data.get("deterministic") is True, "deterministic must be true")
    _require(verdict_data.get("source_log_path") == "artifacts/inf_bot_01/nemesis_execution_log.json", "source_log_path mismatch")
    _require(verdict_data.get("source_log_sha256") == source_log_sha256, "source_log_sha256 mismatch")
    _require(verdict_data.get("expected_decision") == "block", "expected_decision must be block")
    _require(verdict_data.get("actual_decision") == "block", "actual_decision must be block")
    _require(verdict_data.get("verdict") == "block", "verdict must be block")
    _require(verdict_data.get("confidence_policy") == "deterministic_rules_only", "confidence_policy mismatch")
    _require(verdict_data.get("threshold_results", {}).get("identity_match") is True, "identity_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("scenario_match") is True, "scenario_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("safety_flags_clean") is True, "safety_flags_clean must be true")
    _require(verdict_data.get("threshold_results", {}).get("expected_decision_match") is True, "expected_decision_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("reason_match") is True, "reason_match must be true")
    _require(verdict_data.get("threshold_results", {}).get("runtime_absent") is True, "runtime_absent must be true")
    _require(verdict_data.get("threshold_results", {}).get("network_absent") is True, "network_absent must be true")
    _require(verdict_data.get("threshold_results", {}).get("secrets_absent") is True, "secrets_absent must be true")
    _require(bool(verdict_data.get("minos_verdict_sha256")), "minos_verdict_sha256 must be non-empty")

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/inf_minos_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "INF-MINOS-01", "decision.json phase_id mismatch")
    _require(decision_data.get("phase_class") == "minos_verdict", "decision.json phase_class mismatch")
    _require(decision_data.get("minos_verdict_executed") is True, "decision.json minos_verdict_executed must be true")
    _require(decision_data.get("minos_verdict_count") == 1, "decision.json minos_verdict_count must be 1")
    _require(decision_data.get("llm_as_judge") is False, "decision.json llm_as_judge must be false")
    _require(decision_data.get("deterministic_verdict") is True, "decision.json deterministic_verdict must be true")
    _require(decision_data.get("source_bot_id") == "nemesis", "decision.json source_bot_id mismatch")
    _require(decision_data.get("source_scenario_id") == "scenario_11_nemesis", "decision.json source_scenario_id mismatch")
    _require(decision_data.get("source_log_sha256") == source_log_sha256, "decision.json source_log_sha256 mismatch")
    _require(decision_data.get("minos_verdict_sha256") == actual_verdict_sha256, "decision.json minos_verdict_sha256 mismatch")
    _require(decision_data.get("expected_verdict") == "block", "expected_verdict must be block")
    _require(decision_data.get("actual_verdict") == "block", "actual_verdict must be block")
    _require(decision_data.get("threshold_results_all_passed") is True, "threshold_results_all_passed must be true")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")


def _check_purgatorium_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("purgatorium_finding_created") is True, "purgatorium_finding_created must be true")
    _require(state.get("finding_count") == 1, "finding_count must be 1")
    _require(state.get("bot_execution_log_count") == 1, "bot_execution_log_count must remain 1")
    _require(state.get("minos_verdict_count") == 1, "minos_verdict_count must remain 1")

    artifacts_root = ROOT / "artifacts/purg_01"
    _require(artifacts_root.exists(), "artifacts/purg_01 must exist")

    finding_paths = sorted(artifacts_root.glob("finding*.json"))
    _require(len(finding_paths) == 1, f"expected exactly 1 Purgatorium finding JSON, found {len(finding_paths)}")
    finding_path = finding_paths[0]
    _require(finding_path.name == "finding_nemesis_validator_bypass.json", "unexpected Purgatorium finding filename")

    finding_data = _load_json(finding_path)
    source_verdict_path = ROOT / "artifacts/inf_minos_01/minos_verdict.json"
    source_log_path = ROOT / "artifacts/inf_bot_01/nemesis_execution_log.json"
    fixture_input_path = ROOT / "fixtures/lab_simulation/aris_infernus_lab_full/scenario_11_nemesis/input.json"
    source_verdict_sha256 = hashlib.sha256(source_verdict_path.read_bytes()).hexdigest()
    source_log_sha256 = hashlib.sha256(source_log_path.read_bytes()).hexdigest()
    fixture_input_sha256 = hashlib.sha256(fixture_input_path.read_bytes()).hexdigest()
    canonical_finding_sha256 = _canonical_hash_without_field(finding_data, "finding_sha256")

    _require(finding_data.get("phase_id") == "PURG-01", "finding phase_id mismatch")
    _require(finding_data.get("source_phase_id") == "INF-MINOS-01", "finding source_phase_id mismatch")
    _require(finding_data.get("finding_id") == "purg_nemesis_validator_bypass_001", "unexpected finding_id")
    _require(finding_data.get("source_bot_id") == "nemesis", "source_bot_id must be nemesis")
    _require(finding_data.get("source_scenario_id") == "scenario_11_nemesis", "source_scenario_id mismatch")
    _require(finding_data.get("source_verdict_path") == "artifacts/inf_minos_01/minos_verdict.json", "source_verdict_path mismatch")
    _require(finding_data.get("source_verdict_sha256") == source_verdict_sha256, "source_verdict_sha256 mismatch")
    _require(finding_data.get("source_log_path") == "artifacts/inf_bot_01/nemesis_execution_log.json", "source_log_path mismatch")
    _require(finding_data.get("source_log_sha256") == source_log_sha256, "source_log_sha256 mismatch")
    _require(finding_data.get("attack_class") == "validator_bypass_injection", "attack_class mismatch")
    _require(finding_data.get("finding_type") == "validator_bypass_attempt", "finding_type mismatch")
    _require(finding_data.get("severity") == "S0", "severity must be S0")
    _require(finding_data.get("status") == "open", "status must be open")
    _require(finding_data.get("disposition") == "requires_repair_plan", "disposition mismatch")
    _require(finding_data.get("minos_verdict") == "block", "minos_verdict must be block")
    _require(finding_data.get("evidence_chain", {}).get("fixture_input_hash") == fixture_input_sha256, "fixture_input_hash mismatch")
    _require(finding_data.get("evidence_chain", {}).get("bot_execution_log_hash") == source_log_sha256, "bot_execution_log_hash mismatch")
    _require(finding_data.get("evidence_chain", {}).get("minos_verdict_hash") == source_verdict_sha256, "minos_verdict_hash mismatch")
    _require(finding_data.get("remediation_plan", {}).get("objective") == "harden validator/gate bypass resistance", "remediation objective mismatch")
    _require(finding_data.get("remediation_plan", {}).get("allowed_next_step") == "plan_only_repair_gate", "allowed_next_step mismatch")
    _require(finding_data.get("remediation_plan", {}).get("runtime_patch_allowed") is False, "runtime_patch_allowed must be false")
    _require(finding_data.get("remediation_plan", {}).get("apply_allowed") is False, "apply_allowed must be false")
    _require(finding_data.get("remediation_plan", {}).get("required_future_evidence") == [
        "failing_reproduction_or_negative_test",
        "validator_rule_or_gate_contract",
        "passing_test_after_repair",
        "CI_success",
    ], "required_future_evidence mismatch")
    _require(finding_data.get("finding_sha256") == canonical_finding_sha256, "finding_sha256 mismatch")

    source_verdict_data = _load_json(source_verdict_path)
    _require(source_verdict_data.get("llm_as_judge") is False, "source verdict llm_as_judge must be false")
    _require(source_verdict_data.get("deterministic") is True, "source verdict deterministic must be true")
    threshold_results = source_verdict_data.get("threshold_results", {})
    _require(all(threshold_results.get(key) is True for key in [
        "identity_match",
        "scenario_match",
        "safety_flags_clean",
        "expected_decision_match",
        "reason_match",
        "runtime_absent",
        "network_absent",
        "secrets_absent",
    ]), "all source verdict threshold_results must be true")

    decision_path = artifacts_root / "decision.json"
    _require(decision_path.exists(), "artifacts/purg_01/decision.json must exist")
    decision_data = _load_json(decision_path)
    _require(decision_data.get("phase_id") == "PURG-01", "decision.json phase_id mismatch")
    _require(decision_data.get("previous_phase_id") == "INF-MINOS-01", "decision.json previous_phase_id mismatch")
    _require(decision_data.get("phase_class") == "purgatorium", "decision.json phase_class mismatch")
    _require(decision_data.get("purgatorium_finding_created") is True, "decision.json purgatorium_finding_created must be true")
    _require(decision_data.get("finding_count") == 1, "decision.json finding_count must be 1")
    _require(decision_data.get("source_bot_id") == "nemesis", "decision.json source_bot_id mismatch")
    _require(decision_data.get("source_scenario_id") == "scenario_11_nemesis", "decision.json source_scenario_id mismatch")
    _require(decision_data.get("source_verdict_path") == "artifacts/inf_minos_01/minos_verdict.json", "decision.json source_verdict_path mismatch")
    _require(decision_data.get("source_verdict_sha256") == source_verdict_sha256, "decision.json source_verdict_sha256 mismatch")
    _require(decision_data.get("source_log_sha256") == source_log_sha256, "decision.json source_log_sha256 mismatch")
    _require(decision_data.get("finding_path") == "artifacts/purg_01/finding_nemesis_validator_bypass.json", "decision.json finding_path mismatch")
    _require(decision_data.get("finding_sha256") == canonical_finding_sha256, "decision.json finding_sha256 mismatch")
    _require(decision_data.get("severity") == "S0", "decision.json severity must be S0")
    _require(decision_data.get("finding_status") == "open", "decision.json finding_status must be open")
    _require(decision_data.get("remediation_apply_allowed") is False, "decision.json remediation_apply_allowed must be false")
    _require(decision_data.get("runtime_patch_allowed") is False, "decision.json runtime_patch_allowed must be false")
    _require(decision_data.get("llm_as_judge") is False, "decision.json llm_as_judge must be false")
    _require(decision_data.get("deterministic") is True, "decision.json deterministic must be true")
    _require(decision_data.get("runtime_execution") is False, "decision.json runtime_execution must be false")
    _require(decision_data.get("autonomous_execution") is False, "decision.json autonomous_execution must be false")
    _require(decision_data.get("network_used") is False, "decision.json network_used must be false")
    _require(decision_data.get("secrets_accessed") is False, "decision.json secrets_accessed must be false")
    _require(decision_data.get("bedrock_executed") is False, "decision.json bedrock_executed must be false")
    _require(decision_data.get("product_promotion_allowed") is False, "decision.json product_promotion_allowed must be false")
    warnings = decision_data.get("carried_forward_warnings", [])
    _require(len(warnings) == 3, "decision.json must carry exactly 3 warnings")
    _require("INF-MINOS-01 decision.json kept final_origin_main_sha as pending_post_push_verification" in warnings[0], "missing INF-MINOS-01 warning")
    _require("INF-BOT-01 decision.json kept final_origin_main_sha as pending_post_push_verification" in warnings[1], "missing INF-BOT-01 warning")
    _require("INF-MAT-01 final_origin_main_sha points to debc51e" in warnings[2], "missing INF-MAT-01 warning")


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
    _require(state["current_phase_bots_executed"] is False, "current_phase_bots_executed must be false")
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
    _check_operator_preferences_contract(state)

    # Three-layer circuit breaker (fixture_materialization not in GOVERNANCE_CLASSES, streak check is a no-op here)
    _check_governance_streak(state)
    sig = _check_gate_signature(state)
    _check_cycle_nudge(state)

    # INF-MAT-01 baseline must remain true for downstream capacity gates.
    _check_fixture_materialization(state)
    # INF-BOT-01 baseline must remain true for INF-MINOS-01.
    _check_bot_execution_artifacts(state)
    # INF-MINOS-01 baseline must remain true for PURG-01.
    _check_minos_verdict_artifacts(state)
    # PURG-01 baseline must remain true for ACB-CORE-01.
    _check_purgatorium_artifacts(state)
    # ACB-CORE-01 baseline must remain true for ACB-CORE-02.
    _check_acb_core_01_project_artifacts(state)
    # ACB-CORE-02 baseline must remain true for ACB-CAP-01.
    _check_acb_core_02_project_artifacts(state)
    # ACB-CAP-01 baseline must remain true for ACB-CAP-02.
    _check_acb_cap_01_project_artifacts(state)
    # ACB-CAP-02 baseline must remain true for ACB-CAP-03.
    _check_acb_cap_02_project_artifacts(state)
    # ACB-CAP-03 baseline must remain true for ACB-CAP-04.
    _check_acb_cap_03_project_artifacts(state)
    # ACB-CAP-04 baseline must remain true for ACB-CAP-05.
    _check_acb_cap_04_project_artifacts(state)
    # ACB-CAP-05 specific checks
    _check_acb_cap_05_project_artifacts(state)
    # INF-FULL-01 scope-charter specific checks
    _check_inf_full_01_project_artifacts(state)
    # INF-FULL-02 baseline freeze planning checks
    _check_inf_full_02_project_artifacts(state)
    # INF-FULL-03 chain registration opening checks
    _check_inf_full_03_project_artifacts(state)

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

    # Authorization: fixture_materialization_allowed remains true; all others false.
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
        "baseline_freeze_planned: `true`",
        "baseline_freeze_applied: `false`",
        "Anti-proliferation rule active: `true`",
        "CI enforcement active: `true`",
        "Gate cycles used: `0`",
        "Gate max cycles: `3`",
        "governance_gate_streak: `0`",
        "fixture_materialization_executed: `true`",
        "bot_execution_executed: `true`",
        "current_phase_bots_executed: `false`",
        "bot_execution_log_count: `1`",
        "minos_verdict_executed: `true`",
        "minos_verdict_count: `1`",
        "purgatorium_finding_created: `true`",
        "finding_count: `1`",
        "scenario_count: `13`",
        "External deliverables registered from `../artifacts/infernus/` and `../docs/infernus_full/`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Next phase: `null`",
        "INF-FULL-03 completed a planning-only chain registration and preparation opening packet.",
        "Execution authorization: `false`",
        "No canonical successor is currently defined after `INF-FULL-03` in `ROADMAP_CANONICAL.md`.",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        EXPECTED_STATUS,
        "Deferred phase: `null`",
        "next_phase_authorized_by_operator=false",
        "INF-FULL-03 is planning-only and registers the full Infernus chain plus the if00-if04 contract pack.",
        "No next phase is authorized.",
        "governance_gate_streak=0",
        "current_phase_bots_executed=false.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "OPERATOR_PREFERENCES.md",
        "artifacts/decisions/acb_cap_05_project_evidence_2026_06_05.json",
        "../artifacts/infernus/inf_full_03_opening_decision_2026_06_06.json",
        "../artifacts/infernus/if00_transition_candidate.json",
        "../artifacts/infernus/if04_permission_manifest_v4.json",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "INF-FULL-03 | ARIS Infernus FULL Chain Registration & Preparation Opening | pass",
        "INF-FULL-01 | ARIS Infernus Full Scope Charter Gate | pass",
        "ACB-CAP-05 | ARIS Capability Build Advanced Supply Chain Gate | pass",
    )
    _mirror_contains(
        ROOT / "README.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "OPERATOR_PREFERENCES.md",
        "artifacts/decisions/acb_cap_05_project_evidence_2026_06_05.json",
        "baseline_freeze_planned: `true`",
        "baseline_freeze_applied: `false`",
        "validate_active_context.yml",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "INF-FULL-03 completed as a planning-only chain registration and preparation opening package.",
        "No canonical successor is currently defined after `INF-FULL-03` in the Transition Table.",
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
        "REGRA DE PREFERÊNCIA DO OPERADOR",
        "OPERATOR_PREFERENCES.md",
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
        "bot_execution_executed": state.get("bot_execution_executed", False),
        "current_phase_bots_executed": state.get("current_phase_bots_executed", False),
        "bot_execution_log_count": state.get("bot_execution_log_count", 0),
        "minos_verdict_executed": state.get("minos_verdict_executed", False),
        "minos_verdict_count": state.get("minos_verdict_count", 0),
        "uv_lock_exists": (PROJECT_ROOT / "uv.lock").exists(),
        "acb_core_01_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_01" / "decision.json").exists(),
        "acb_core_02_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_02" / "decision.json").exists(),
        "acb_cap_01_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_cap_01" / "decision.json").exists(),
        "acb_cap_05_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_cap_05" / "advanced_supply_chain_decision.json").exists(),
        "inf_full_01_scope_artifacts_exist": INF_FULL_01_SCOPE_DECISION_PATH.exists(),
        "inf_full_03_artifacts_exist": INF_FULL_03_DECISION_PATH.exists(),
        "auto_advance_enabled": state["auto_advance"]["enabled"],
        "ci_enforcement_active": True,
        "anti_proliferation_rule_active": True,
        "fixture_materialization_executed": state.get("fixture_materialization_executed", False),
    }, indent=2))


if __name__ == "__main__":
    main()
