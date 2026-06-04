import json
import importlib.util
import os
import subprocess
import tempfile
from pathlib import Path


def test_validator_passes():
    r = subprocess.run(
        ["python3", "scripts/validate_active_context_state.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_fixture_absence_passes():
    r = subprocess.run(
        ["python3", "scripts/assert_no_unauthorized_fixtures.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_mirror_sync_passes():
    r = subprocess.run(
        ["python3", "scripts/assert_mirror_sync.py"],
        capture_output=True, text=True
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_minimum_deliverable_blocks_inf_mat_pass_without_real_fixture_dirs():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-MAT-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-MAT-01 without fixture dirs")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_inf_bot_pass_without_log():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-BOT-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-BOT-01 without execution log")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_inf_minos_pass_without_verdict():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "INF-MINOS-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block INF-MINOS-01 without verdict json")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_purg_pass_without_finding():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "PURG-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block PURG-01 without finding json")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_core_01_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_01_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CORE-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CORE-01 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_core_01_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_core_01_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "0e935f41830101c391905611473e52e883d36a26",
                        "supply_chain_ci": {"conclusion": "success"},
                        "deliverables": {
                            "uv_lock_exists": True,
                            "pip_audit_gate_exists": True,
                            "sbom_exists": True,
                            "uv_bootstrap_exists": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_01_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CORE-01",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_core_02_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_02_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CORE-02",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CORE-02 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_core_02_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_core_02_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "46910e0fda3fc64a19818ad80f39813227b53922",
                        "core_public_api_ci": {"conclusion": "success"},
                        "deliverables": {
                            "research_basis_exists": True,
                            "snapshot_before_exists": True,
                            "snapshot_after_exists": True,
                            "import_stability_report_exists": True,
                            "explicit_all_created_or_verified": True,
                            "protocols_created_or_verified": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CORE_02_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CORE-02",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_01_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_01_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-01",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-01 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_01_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_01_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "68ca2a07fc0ee1afad22d967619e05f35ccf52b1",
                        "backend_baseline_ci": {"conclusion": "success"},
                        "deliverables": {
                            "fastapi_app_exists": True,
                            "health_check_exists": True,
                            "ready_check_exists": True,
                            "jwt_auth_exists": True,
                            "api_key_auth_exists": True,
                            "tenant_isolation_exists": True,
                            "slowapi_rate_limit_exists": True,
                            "backend_tests_exist": True,
                            "backend_artifacts_exist": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_01_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-01",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_blocks_acb_cap_02_pass_without_project_deliverables():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_02_EVIDENCE_PATH = Path(tmp) / "missing_evidence.json"
            try:
                module._check_minimum_deliverable(
                    {
                        "current_phase_id": "ACB-CAP-02",
                        "decision": "pass",
                    }
                )
            except SystemExit as exc:
                assert exc.code == 1
            else:
                raise AssertionError("minimum deliverable check should block ACB-CAP-02 without project deliverables")
        finally:
            os.chdir(cwd)


def test_minimum_deliverable_allows_acb_cap_02_with_evidence_artifact_only():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path.cwd()
        try:
            os.chdir(tmp)
            evidence_path = Path(tmp) / "acb_cap_02_evidence.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "project_sha": "b2fdc3c994342a42a84823fa15615c931f1bc00e",
                        "mcp_runtime_sandbox_ci": {"conclusion": "success"},
                        "deliverables": {
                            "mcp_runtime_package_exists": True,
                            "stdio_ban_exists": True,
                            "sandbox_spec_exists": True,
                            "policy_pre_dispatch_exists": True,
                            "kill_switch_exists": True,
                            "rollback_contract_exists": True,
                            "audit_event_exists": True,
                            "mcp_runtime_tests_exist": True,
                            "mcp_runtime_artifacts_exist": True,
                        },
                    }
                ),
                encoding="utf-8",
            )
            module.PROJECT_ROOT = Path(tmp)
            module.ACB_CAP_02_EVIDENCE_PATH = evidence_path
            module._check_minimum_deliverable(
                {
                    "current_phase_id": "ACB-CAP-02",
                    "decision": "pass",
                }
            )
        finally:
            os.chdir(cwd)


def test_boot_receipt_blocks_when_operator_preferences_missing():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    try:
        module._warn_boot_receipt(
            {
                "last_boot_files_read": [
                    "ACTIVE_CONTEXT_STATE.json",
                    "AGENT_IDENTITY.md",
                    "ACTIVE_CONTEXT_SCHEMA.json",
                    "scripts/validate_active_context_state.py",
                    "ROADMAP_CANONICAL.md",
                    "MANDATORY_READ_FIRST_RULES.md",
                    "CURRENT_STATE.md",
                    "NEXT_ACTION.md",
                    "DECISION_LOCKS.md",
                ]
            }
        )
    except SystemExit as exc:
        assert exc.code == 1
    else:
        raise AssertionError("boot receipt should block when OPERATOR_PREFERENCES.md is missing")


def test_prompt_preference_allows_clean_prompt_only_transition():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is True


def test_prompt_preference_does_not_override_operator_transition():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="operator",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is False


def test_prompt_preference_does_not_override_manual_lock():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=True,
    ) is False


def test_prompt_preference_requires_previous_phase_pass():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=False,
        ci_green=True,
        validator_green=True,
        manual_authorization_required=False,
    ) is False


def test_prompt_preference_requires_green_ci_and_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        Path("scripts/validate_active_context_state.py"),
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=False,
        validator_green=True,
        manual_authorization_required=False,
    ) is False
    assert module._preference_allows_direct_prompt(
        advance_mode="prompt_only",
        previous_phase_pass=True,
        ci_green=True,
        validator_green=False,
        manual_authorization_required=False,
    ) is False
