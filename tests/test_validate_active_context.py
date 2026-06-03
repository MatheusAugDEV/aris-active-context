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
