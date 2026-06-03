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
