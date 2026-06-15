#!/usr/bin/env python3
# ARCHIVED from tests/ during AC-TRANS-03. Superseded by tests/test_validate_active_context.py.
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"


def _load_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _run_validator_with_state(state: dict, *, extra_files: dict[str, str] | None = None) -> tuple[int, str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        import shutil
        for src in ROOT.iterdir():
            if src.name == ".git":
                continue
            dst = tmp_path / src.name
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        (tmp_path / "ACTIVE_CONTEXT_STATE.json").write_text(json.dumps(state, indent=2), encoding="utf-8")
        subprocess.run(
            [sys.executable, str(tmp_path / "scripts" / "render_boot.py")],
            check=True,
            cwd=tmp,
            capture_output=True,
            text=True,
        )

        if extra_files:
            for relpath, content in extra_files.items():
                target = tmp_path / relpath
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")

        result = subprocess.run(
            [sys.executable, str(tmp_path / "scripts" / "validate_active_context_state.py")],
            capture_output=True,
            text=True,
            cwd=tmp,
        )
        return result.returncode, result.stdout, result.stderr


class TestCanonicalState(unittest.TestCase):
    def test_canonical_state_passes(self) -> None:
        rc, stdout, stderr = _run_validator_with_state(_load_state())
        self.assertEqual(rc, 0, f"Validator should pass.\nSTDOUT: {stdout}\nSTDERR: {stderr}")
        data = json.loads(stdout)
        self.assertEqual(data["decision"], "pass")


class TestCrossFieldDrift(unittest.TestCase):
    def test_active_next_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["active_next_phase"] = "Different Phase"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "active_next_phase drift must be blocked.\n" + stderr)

    def test_status_drift_blocks(self) -> None:
        state = _load_state()
        state["current_live_route"]["status"] = "different_status"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "status drift must be blocked.\n" + stderr)


class TestAuthorizationGuards(unittest.TestCase):
    def test_real_apply_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["real_apply_authorized"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "real apply authorization must be blocked.\n" + stderr)


if __name__ == "__main__":
    unittest.main()
