#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
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
        self.assertEqual(data["latest_completed_phase"], "ARIS Infernus Lab FULL Controlled Fixture Materialization Apply Planning Gate")
        self.assertEqual(data["active_next_phase"], "ARIS Infernus Lab FULL Controlled Fixture Materialization Apply Review Gate")
        self.assertIn("Purgatorium FULL", data["canonical_roadmap"])
        self.assertIn("BenchUX Lab", data["canonical_roadmap"])
        self.assertIn("Crisol FULL", data["canonical_roadmap"])


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

    def test_latest_completed_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["latest_completed_phase"] = "Different Completed Phase"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "latest completed phase drift must be blocked.\n" + stderr)


class TestAuthorizationGuards(unittest.TestCase):
    def test_real_apply_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["real_apply_authorized"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "real apply authorization must be blocked.\n" + stderr)

    def test_host_mutation_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["host_filesystem_mutation_authorized"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "host mutation authorization must be blocked.\n" + stderr)


class TestRoadmapGuards(unittest.TestCase):
    def test_stale_microphase_phrase_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "ROADMAP_CANONICAL.md").read_text(encoding="utf-8")
        stale = original + "\nARIS Infernus Lab FULL Contract Schema Enforcement Implementation Planning Gate\n"
        rc, _, stderr = _run_validator_with_state(state, extra_files={"ROADMAP_CANONICAL.md": stale})
        self.assertNotEqual(rc, 0, "stale microphase phrase must be blocked.\n" + stderr)

    def test_missing_purgatorium_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "ROADMAP_CANONICAL.md").read_text(encoding="utf-8")
        corrupted = original.replace("Purgatorium corrige.", "Correction placeholder.")
        rc, _, stderr = _run_validator_with_state(state, extra_files={"ROADMAP_CANONICAL.md": corrupted})
        self.assertNotEqual(rc, 0, "missing Purgatorium phrase must be blocked.\n" + stderr)

    def test_missing_crisol_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "ROADMAP_CANONICAL.md").read_text(encoding="utf-8")
        corrupted = original.replace("Crisol refina.", "Final refinement placeholder.")
        rc, _, stderr = _run_validator_with_state(state, extra_files={"ROADMAP_CANONICAL.md": corrupted})
        self.assertNotEqual(rc, 0, "missing Crisol phrase must be blocked.\n" + stderr)


class TestMirrorGuards(unittest.TestCase):
    def test_current_state_without_json_wins_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
        corrupted = original.replace("ACTIVE_CONTEXT_STATE.json wins", "ACTIVE_CONTEXT_STATE.json is preferred")
        rc, _, stderr = _run_validator_with_state(state, extra_files={"CURRENT_STATE.md": corrupted})
        self.assertNotEqual(rc, 0, "mirror without JSON-wins phrase must be blocked.\n" + stderr)

    def test_minos_artifact_without_llm_boundary_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "ARIS_INFERNUS_FULL_MINOS_VERDICT_SCHEMA_PLANNING_GATE.md").read_text(encoding="utf-8")
        corrupted = original.replace(
            "No LLM-as-judge verdict authorization.",
            "LLM verdict review available.",
        )
        rc, _, stderr = _run_validator_with_state(
            state,
            extra_files={"ARIS_INFERNUS_FULL_MINOS_VERDICT_SCHEMA_PLANNING_GATE.md": corrupted},
        )
        self.assertNotEqual(rc, 0, "minos artifact without llm boundary must be blocked.\n" + stderr)

    def test_current_state_without_authorization_false_record_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
        corrupted = original.replace(
            "`real_apply_authorized=false`, `apply_execution_allowed=false`, `fixture_materialization_allowed=false`, and `future_apply_gate_required=true` remain locked now.",
            "Apply boundary omitted.",
        )
        rc, _, stderr = _run_validator_with_state(state, extra_files={"CURRENT_STATE.md": corrupted})
        self.assertNotEqual(rc, 0, "current state without apply boundary record must be blocked.\n" + stderr)

    def test_apply_planning_artifact_without_future_human_approval_phrase_blocks(self) -> None:
        state = _load_state()
        original = (ROOT / "ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_APPLY_PLANNING_GATE.md").read_text(encoding="utf-8")
        corrupted = original.replace(
            "Human approval collected now: `False`.",
            "Human approval collected now: `True`.",
        )
        rc, _, stderr = _run_validator_with_state(
            state,
            extra_files={"ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_APPLY_PLANNING_GATE.md": corrupted},
        )
        self.assertNotEqual(rc, 0, "apply planning artifact without future-only human approval phrase must be blocked.\n" + stderr)


if __name__ == "__main__":
    unittest.main()
