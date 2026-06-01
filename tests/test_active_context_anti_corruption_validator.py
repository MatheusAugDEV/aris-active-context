#!/usr/bin/env python3
"""Anti-corruption failure-mode simulation tests for ARIS active-context.

Each test mutates a valid state and verifies the validator blocks it.
One positive test verifies the canonical valid state passes.
"""

from __future__ import annotations

import copy
import json
import pathlib
import subprocess
import sys
import tempfile
import textwrap
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
SCHEMA_PATH = ROOT / "ACTIVE_CONTEXT_SCHEMA.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate_active_context_state.py"


def _load_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _run_validator_with_state(state: dict, *, extra_files: dict[str, str] | None = None) -> tuple[int, str, str]:
    """Write a temporary state file, patch sys.argv, and run the validator subprocess."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)

        # Copy the repository layout needed by the validator
        import shutil
        for src in ROOT.iterdir():
            if src.name == ".git":
                continue
            dst = tmp_path / src.name
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        # Overwrite with our mutated state
        (tmp_path / "ACTIVE_CONTEXT_STATE.json").write_text(
            json.dumps(state, indent=2), encoding="utf-8"
        )

        # Apply any extra file overrides
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


class TestPositiveCase(unittest.TestCase):
    """The canonical state must pass the validator."""

    def test_canonical_state_passes(self) -> None:
        rc, stdout, stderr = _run_validator_with_state(_load_state())
        self.assertEqual(rc, 0, f"Validator should pass for canonical state.\nSTDOUT: {stdout}\nSTDERR: {stderr}")
        data = json.loads(stdout)
        self.assertEqual(data["decision"], "pass")


class TestExtraTopLevelProperty(unittest.TestCase):
    """Extra top-level property in ACTIVE_CONTEXT_STATE.json must block."""

    def test_extra_top_level_property_blocks(self) -> None:
        state = _load_state()
        state["__injected_extra_field__"] = "corruption"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Extra top-level property must be blocked.\n" + stderr)
        self.assertIn("extra properties", stderr.lower() + stderr, stderr)


class TestExtraNestedPropertyInAuthorization(unittest.TestCase):
    """Extra nested property in authorization must block."""

    def test_extra_auth_property_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["__injected__"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Extra auth property must be blocked.\n" + stderr)


class TestActiveNextPhaseDrift(unittest.TestCase):
    """active_next_phase different from next_action.phase must block."""

    def test_active_next_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["active_next_phase"] = "Some Other Phase"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Cross-field drift in active_next_phase must be blocked.\n" + stderr)


class TestStatusDrift(unittest.TestCase):
    """status different from current_live_route.status must block."""

    def test_status_drift_blocks(self) -> None:
        state = _load_state()
        state["status"] = "some_other_status"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Status cross-field drift must be blocked.\n" + stderr)


class TestLatestCompletedPhaseDrift(unittest.TestCase):
    """latest_completed_phase different from last_transition.to_phase must block."""

    def test_latest_completed_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["latest_completed_phase"] = "A Phase That Does Not Match"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "latest_completed_phase drift vs last_transition.to_phase must be blocked.\n" + stderr)


class TestHistorySummaryDrift(unittest.TestCase):
    """history_summary must stay aligned with live route closure continuity."""

    def test_history_summary_latest_execution_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["history_summary"]["latest_execution_phase"] = "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Execution"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(
            rc,
            0,
            "history_summary.latest_execution_phase drift must be blocked.\n" + stderr,
        )

    def test_history_summary_previous_execution_phase_drift_blocks(self) -> None:
        state = _load_state()
        state["history_summary"]["previous_execution_phase"] = (
            "Lab Real Simulation Pack Controlled Apply Dry-Run Real Execution Controlled Operator Approval Capture Gate"
        )
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(
            rc,
            0,
            "history_summary.previous_execution_phase drift must be blocked.\n" + stderr,
        )


class TestMissingRequiredTransitionFile(unittest.TestCase):
    """required_files_for_transition listing a file that doesn't exist must block."""

    def test_missing_required_file_blocks(self) -> None:
        state = _load_state()
        state["required_files_for_transition"].append("NONEXISTENT_FILE_XYZ.md")
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Missing required transition file must be blocked.\n" + stderr)


class TestBootProfileMarkdownFirst(unittest.TestCase):
    """BOOT_PROFILE.md starting with CURRENT_STATE.md before JSON must block."""

    def test_boot_profile_markdown_first_blocks(self) -> None:
        state = _load_state()
        stale_boot = textwrap.dedent("""\
            # BOOT_PROFILE

            ## Canonical Boot

            1. CURRENT_STATE.md
            2. NEXT_ACTION.md
            3. DECISION_LOCKS.md
        """)
        rc, _, stderr = _run_validator_with_state(state, extra_files={"BOOT_PROFILE.md": stale_boot})
        self.assertNotEqual(rc, 0, "BOOT_PROFILE starting with CURRENT_STATE.md must be blocked.\n" + stderr)


class TestMandatoryReadFirstNoJsonFirst(unittest.TestCase):
    """MANDATORY_READ_FIRST_RULES.md without JSON-first must block."""

    def test_mandatory_read_no_json_first_blocks(self) -> None:
        state = _load_state()
        stale_rules = textwrap.dedent("""\
            # MANDATORY_READ_FIRST_RULES

            Read-first order:

            1. CURRENT_STATE.md
            2. NEXT_ACTION.md
        """)
        rc, _, stderr = _run_validator_with_state(state, extra_files={"MANDATORY_READ_FIRST_RULES.md": stale_rules})
        self.assertNotEqual(rc, 0, "MANDATORY_READ_FIRST_RULES without JSON-first must be blocked.\n" + stderr)


class TestPromptContractWithDivergentReadFirst(unittest.TestCase):
    """PROMPT_CONTRACT.md with read-first starting from CURRENT_STATE.md must block."""

    def test_prompt_contract_markdown_first_blocks(self) -> None:
        state = _load_state()
        stale_contract = textwrap.dedent("""\
            # PROMPT_CONTRACT

            ## Mandatory read-first rule

            1. CURRENT_STATE.md
            2. NEXT_ACTION.md
        """)
        rc, _, stderr = _run_validator_with_state(state, extra_files={"PROMPT_CONTRACT.md": stale_contract})
        self.assertNotEqual(rc, 0, "PROMPT_CONTRACT starting with Markdown must be blocked.\n" + stderr)


class TestReviewGateWithReviewOnlyFalse(unittest.TestCase):
    """review_gate_only route with review_only=false must block."""

    def test_review_gate_review_only_false_blocks(self) -> None:
        state = _load_state()
        state["next_action"]["review_only"] = False
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "review_gate_only route with review_only=false must be blocked.\n" + stderr)


class TestPlanningGateWithRealAuthorizationTrue(unittest.TestCase):
    """planning_gate with any real authorization flag true must block."""

    def test_planning_gate_real_apply_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["real_apply_authorized"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "planning_gate with real_apply_authorized=true must be blocked.\n" + stderr)

    def test_planning_gate_host_mutation_blocks(self) -> None:
        state = _load_state()
        state["authorization"]["host_filesystem_mutation_authorized"] = True
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "planning_gate with host_filesystem_mutation=true must be blocked.\n" + stderr)


class TestMarkdownMirrorMissingWinsPhrase(unittest.TestCase):
    """Markdown mirror without 'ACTIVE_CONTEXT_STATE.json wins' must block."""

    def test_current_state_missing_wins_phrase_blocks(self) -> None:
        state = _load_state()
        # Remove the 'wins' phrase from CURRENT_STATE.md
        original = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
        corrupted = original.replace("ACTIVE_CONTEXT_STATE.json wins", "ACTIVE_CONTEXT_STATE.json is good")
        rc, _, stderr = _run_validator_with_state(state, extra_files={"CURRENT_STATE.md": corrupted})
        self.assertNotEqual(rc, 0, "Mirror without wins phrase must be blocked.\n" + stderr)


class TestSemanticPassButCrossFieldFail(unittest.TestCase):
    """State that passes schema structural check but fails cross-field consistency must block."""

    def test_current_live_route_status_mismatch_blocks(self) -> None:
        state = _load_state()
        # Mutate only current_live_route.status — top-level status stays correct
        state["current_live_route"]["status"] = "some_diverged_status"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "Cross-field status drift must be blocked even if schema passes.\n" + stderr)


class TestSchemaVersionWithoutVersioningContract(unittest.TestCase):
    """schema_version mismatch vs versioning_contract must block."""

    def test_schema_version_contract_mismatch_blocks(self) -> None:
        state = _load_state()
        state["versioning_contract"]["current_schema_version"] = "9.9"
        rc, _, stderr = _run_validator_with_state(state)
        self.assertNotEqual(rc, 0, "schema_version vs versioning_contract mismatch must be blocked.\n" + stderr)


if __name__ == "__main__":
    unittest.main()
