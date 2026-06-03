import subprocess


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
