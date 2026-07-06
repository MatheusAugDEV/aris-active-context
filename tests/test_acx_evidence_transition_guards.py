from __future__ import annotations

import hashlib
import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
CURRENT_HEAD = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
).stdout.strip()


def _load_acx_module():
    spec = importlib.util.spec_from_file_location("acx_r5_transition_guard_test", TOOLS)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load tools/acx.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ACX = _load_acx_module()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _bundle(**overrides: object) -> dict[str, object]:
    artifacts = [
        {
            "path": "tools/acx.py",
            "sha256": _sha256(TOOLS),
        },
        {
            "path": "tests/test_acx_evidence_transition_guards.py",
            "sha256": _sha256(Path(__file__)),
        },
    ]
    payload: dict[str, object] = {
        "phase_id": "ACX-R5",
        "from_phase": "ACX-R4",
        "to_phase": "ACX-R5",
        "mode": "advisory",
        "transition_rules_version": ACX.TRANSITION_RULES_VERSION,
        "head_before": CURRENT_HEAD,
        "head_after": CURRENT_HEAD,
        "git_status_before": "",
        "git_status_after": "",
        "files_read": [
            "ACTIVE_CONTEXT_STATE.json",
            "ACTIVE_CONTEXT_SCHEMA.json",
            "tools/acx.py",
            "docs/acx/ROLLBACK.md",
        ],
        "files_changed": [],
        "commands": [
            "git rev-parse HEAD",
            "git status --porcelain",
            "python3 tools/acx_validate.py",
        ],
        "artifacts": artifacts,
        "rollback_plan": "No rollback required for advisory-only validation evidence.",
        "limitations": [
            "advisory only",
            "no runtime",
            "no hard blocking",
        ],
    }
    payload.update(overrides)
    return payload


class ACXEvidenceTransitionGuardsTest(unittest.TestCase):
    def test_valid_transition_evidence_is_accepted_in_advisory_mode(self) -> None:
        bundle = _bundle()
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)
        self.assertEqual(errors, [])
        self.assertTrue(ACX.can_transition("ACX-R4", "ACX-R5", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD))

    def test_invalid_transition_is_rejected_by_pure_can_transition(self) -> None:
        bundle = _bundle(to_phase="ACX-R6")
        self.assertFalse(
            ACX.can_transition("ACX-R4", "ACX-R6", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD)
        )

    def test_incomplete_evidence_is_rejected(self) -> None:
        bundle = _bundle()
        bundle.pop("rollback_plan")
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)
        self.assertTrue(errors)
        self.assertFalse(ACX.can_transition("ACX-R4", "ACX-R5", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD))

    def test_stale_bundle_is_rejected_when_head_differs(self) -> None:
        bundle = _bundle()
        stale_head = "0" * 64
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=stale_head)
        self.assertIn("stale bundle: head_before does not match current HEAD", errors)
        self.assertFalse(ACX.can_transition("ACX-R4", "ACX-R5", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=stale_head))

    def test_read_only_evidence_rejected_if_git_status_is_dirty(self) -> None:
        bundle = _bundle(
            git_status_before=" M authority_manifest.json",
            git_status_after=" M authority_manifest.json",
        )
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)
        self.assertTrue(any("read-only evidence must have empty git_status_before and git_status_after" in error for error in errors))
        self.assertFalse(ACX.can_transition("ACX-R4", "ACX-R5", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD))

    def test_report_text_containing_pass_generates_advisory_violation_data(self) -> None:
        violations = ACX.scan_advisory_report_prose(
            "READY for review, PASS to the next step, DONE after approval.",
            phase_id="ACX-R5",
            from_phase="ACX-R4",
            to_phase="ACX-R5",
        )
        matched_tokens = {violation["payload"]["matched_token"] for violation in violations}
        self.assertIn("PASS", matched_tokens)
        self.assertIn("DONE", matched_tokens)
        self.assertIn("READY", matched_tokens)
        self.assertTrue(all(violation["event_type"] == "violation_advisory" for violation in violations))

    def test_pass_like_prose_does_not_alter_transition_authority(self) -> None:
        bundle = _bundle(report_text="PASS READY APROVADO")
        violations = ACX.scan_advisory_report_prose(
            bundle["report_text"],
            phase_id="ACX-R5",
            from_phase="ACX-R4",
            to_phase="ACX-R5",
        )
        self.assertTrue(violations)
        self.assertTrue(
            ACX.can_transition("ACX-R4", "ACX-R5", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD)
        )

    def test_advisory_violation_does_not_mutate_canonical_state(self) -> None:
        before = STATE_PATH.read_bytes()
        ACX.scan_advisory_report_prose(
            "PASS READY APPROVED",
            phase_id="ACX-R5",
            from_phase="ACX-R4",
            to_phase="ACX-R5",
        )
        after = STATE_PATH.read_bytes()
        self.assertEqual(before, after)

    def test_hard_mode_is_not_enabled_by_default(self) -> None:
        self.assertEqual(ACX.current_acx_mode(), "advisory")
        self.assertFalse(ACX.hard_mode_enabled())
        self.assertNotEqual(os.environ.get("ACX_MODE"), "hard")

    def test_transition_rule_version_is_explicit(self) -> None:
        bundle = _bundle()
        self.assertEqual(ACX.TRANSITION_RULES_VERSION, "acx-r5-advisory-v1")
        self.assertEqual(bundle["transition_rules_version"], ACX.TRANSITION_RULES_VERSION)
        self.assertEqual(ACX.ADVISORY_TRANSITION_RULES["transition_rules_version"], ACX.TRANSITION_RULES_VERSION)

    def test_artifact_sha256_validation_works_for_listed_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            artifact_path = root / "artifact.txt"
            artifact_path.write_text("artifact body\n", encoding="utf-8")
            good_hash = hashlib.sha256(artifact_path.read_bytes()).hexdigest()

            good_errors = ACX.validate_transition_artifacts(
                [{"path": str(artifact_path), "sha256": good_hash}],
                root=root,
            )
            self.assertEqual(good_errors, [])

            bad_errors = ACX.validate_transition_artifacts(
                [{"path": str(artifact_path), "sha256": "0" * 64}],
                root=root,
            )
            self.assertTrue(bad_errors)
            self.assertIn("sha256 mismatch", bad_errors[0])


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
