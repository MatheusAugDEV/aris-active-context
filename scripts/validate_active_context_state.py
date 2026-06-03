#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"
ACB_CORE_01_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_01_project_evidence_2026_06_03.json"
ACB_CORE_02_EVIDENCE_PATH = ROOT / "artifacts" / "decisions" / "acb_core_02_project_evidence_2026_06_03.json"

EXPECTED_PHASE = "ARIS Capability Build Core Public API Baseline Gate"
EXPECTED_PHASE_ID = "ACB-CORE-02"
EXPECTED_PREVIOUS_PHASE = "ARIS Capability Build Dependency Foundation Gate"
EXPECTED_PREVIOUS_PHASE_ID = "ACB-CORE-01"
EXPECTED_STATUS = "acb_core_02_pass"
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
    )
}

REQUIRED_BOOT_FILES = [
    "ACTIVE_CONTEXT_STATE.json",
    "AGENT_IDENTITY.md",
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
    boot_files = state.get("last_boot_files_read", [])
    missing = [f for f in REQUIRED_BOOT_FILES if f not in boot_files]
    if missing:
        print(f"BLOCK: last_boot_files_read missing: {missing}")
        print("Codex must populate last_boot_files_read before any action.")
        sys.exit(1)


def _check_acb_core_01_project_artifacts(state: dict[str, Any]) -> None:
    _require(state.get("phase_class") == "capability_build", "phase_class must be capability_build")
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
    _require(state.get("phase_class") == "capability_build", "phase_class must be capability_build")
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
    # ACB-CORE-02 specific checks
    _check_acb_core_02_project_artifacts(state)

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
        "Anti-proliferation rule active: `true`",
        "CI enforcement active: `true`",
        "Gate cycles used: `0`",
        "Gate max cycles: `3`",
        "governance_gate_streak: `0`",
        "fixture_materialization_executed: `true`",
        "bot_execution_executed: `true`",
        "bot_execution_log_count: `1`",
        "minos_verdict_executed: `true`",
        "minos_verdict_count: `1`",
        "purgatorium_finding_created: `true`",
        "finding_count: `1`",
        "scenario_count: `13`",
        "External deliverables registered from `../artifacts/acb_core_02/`",
    )
    _mirror_contains(
        ROOT / "NEXT_ACTION.md",
        "Next phase: `null`",
        "Awaiting manual operator authorization.",
        "Execution authorization: `false`",
        "ACB-CAP-01 remains closed.",
    )
    _mirror_contains(
        ROOT / "DECISION_LOCKS.md",
        EXPECTED_STATUS,
        "Deferred phase: `null`",
        "next_phase_authorized_by_operator=false",
        "No next phase is authorized.",
        "governance_gate_streak=0",
        "ACB-CAP-01 remains closed pending explicit operator authorization.",
    )
    _mirror_contains(
        ROOT / "CONTEXT_INDEX.md",
        "artifacts/decisions/acb_core_02_project_evidence_2026_06_03.json",
        "../artifacts/acb_core_02/decision.json",
        "../artifacts/acb_core_02/summary.json",
        "../artifacts/acb_core_02/report.md",
        "../artifacts/acb_core_02/public_api_snapshot_after.json",
    )
    _mirror_contains(
        ROOT / "ARIS_PHASE_LEDGER.md",
        "ACB-CORE-02 | ARIS Capability Build Core Public API Baseline Gate | pass",
        "ACB-CORE-01 | ARIS Capability Build Dependency Foundation Gate | pass",
    )
    _mirror_contains(
        ROOT / "README.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "uv_lock_created_or_verified: `true`",
        "artifacts/decisions/acb_core_02_project_evidence_2026_06_03.json",
        "explicit_all_created_or_verified: `true`",
        "validate_active_context.yml",
    )
    _mirror_contains(
        ROOT / "ROADMAP_CANONICAL.md",
        EXPECTED_PHASE,
        "Active next phase: `null`",
        "Operator authorization required before any new phase.",
        "`ACB-CAP-01` is not opened automatically after `ACB-CORE-02`.",
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
        "bot_execution_executed": state.get("bot_execution_executed", False),
        "bot_execution_log_count": state.get("bot_execution_log_count", 0),
        "minos_verdict_executed": state.get("minos_verdict_executed", False),
        "minos_verdict_count": state.get("minos_verdict_count", 0),
        "uv_lock_exists": (PROJECT_ROOT / "uv.lock").exists(),
        "acb_core_01_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_01" / "decision.json").exists(),
        "acb_core_02_artifacts_exist": (PROJECT_ROOT / "artifacts" / "acb_core_02" / "decision.json").exists(),
        "auto_advance_enabled": state["auto_advance"]["enabled"],
        "ci_enforcement_active": True,
        "anti_proliferation_rule_active": True,
        "fixture_materialization_executed": state.get("fixture_materialization_executed", False),
    }, indent=2))


if __name__ == "__main__":
    main()
