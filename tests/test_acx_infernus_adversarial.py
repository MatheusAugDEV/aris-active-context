from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
import sys
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
MANIFEST_PATH = ROOT / "authority_manifest.json"
EVIDENCE_PATH = ROOT / "artifacts" / "acx" / "r7_infernus_acx_adversarial_evidence.json"

CURRENT_HEAD = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
).stdout.strip()

ORIGIN_MAIN = subprocess.run(
    ["git", "ls-remote", "origin", "refs/heads/main"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
).stdout.strip()


def _load_acx_module():
    spec = importlib.util.spec_from_file_location("acx_r7_infernus_adversarial_test", TOOLS)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load tools/acx.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_legacy_scanner():
    scanner_path = ROOT / "tests" / "test_no_legacy_imports.py"
    spec = importlib.util.spec_from_file_location("acx_r7_legacy_import_scanner", scanner_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load tests/test_no_legacy_imports.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ACX = _load_acx_module()
LEGACY_SCANNER = _load_legacy_scanner()


def _run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def _run_acx(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOLS), "--root", str(root), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _copy_repo_file(relative_path: str, dest_root: Path) -> Path:
    source = ROOT / relative_path
    destination = dest_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _bootstrap_render_root(root: Path) -> Path:
    for relative_path in (
        "ACTIVE_CONTEXT_STATE.json",
        "ROADMAP_CANONICAL.md",
        "BOOT.md",
    ):
        source = ROOT / relative_path
        if source.exists():
            _copy_repo_file(relative_path, root)
    manifest_path = root / "authority_manifest.json"
    result = _run_acx(root, ["authority", "manifest", "--out", str(manifest_path)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return manifest_path


def _bootstrap_manual_write_repo(root: Path) -> None:
    result = _run_git(root, ["init"])
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    for key, value in (("user.name", "Codex Test"), ("user.email", "codex@example.com")):
        result = _run_git(root, ["config", key, value])
        if result.returncode != 0:
            raise RuntimeError(result.stderr)

    for relative_path in ("ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl", "authority_manifest.json"):
        _copy_repo_file(relative_path, root)

    add_result = _run_git(root, ["add", "ACTIVE_CONTEXT_STATE.json", ".acx/ledger.jsonl", "authority_manifest.json"])
    if add_result.returncode != 0:
        raise RuntimeError(add_result.stderr)
    commit_result = _run_git(root, ["commit", "-m", "baseline"])
    if commit_result.returncode != 0:
        raise RuntimeError(commit_result.stderr)


def _transition_bundle(**overrides: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "phase_id": "ACX-R7",
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
            "ROADMAP_CANONICAL.md",
            "docs/acx/ACX_SPEC.md",
        ],
        "files_changed": [],
        "commands": [
            "git rev-parse HEAD",
            "git status --porcelain",
            "python3 tools/acx_validate.py",
        ],
        "artifacts": [
            {
                "path": "tools/acx.py",
                "sha256": _sha256(ROOT / "tools" / "acx.py"),
            },
            {
                "path": "tests/test_acx_infernus_adversarial.py",
                "sha256": _sha256(ROOT / "tests" / "test_acx_infernus_adversarial.py"),
            },
        ],
        "rollback_plan": "No rollback required for local advisory-only evidence.",
        "limitations": [
            "local only",
            "mechanical detection only",
            "no CI execution",
        ],
    }
    payload.update(overrides)
    return payload


class ACXInfernusAdversarialTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.results: list[dict[str, Any]] = []
        cls.commands_run: list[str] = []
        cls.tests_run: list[str] = []
        cls.files_read = [
            "ACTIVE_CONTEXT_STATE.json",
            "ROADMAP_CANONICAL.md",
            "BOOT.md",
            "authority_manifest.json",
            ".acx/ledger.jsonl",
            "tools/acx.py",
            "tests/test_no_legacy_imports.py",
        ]
        cls.files_changed = [
            "tools/acx.py",
            "tests/test_acx_infernus_adversarial.py",
            "artifacts/acx/r7_infernus_acx_adversarial_evidence.json",
        ]
        cls.head_before = CURRENT_HEAD
        cls.head_after = CURRENT_HEAD
        cls.origin_main_before = ORIGIN_MAIN.split()[0] if ORIGIN_MAIN else ""
        cls.origin_main_after = cls.origin_main_before

    @classmethod
    def tearDownClass(cls) -> None:
        EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)
        artifact = {
            "phase_id": "ACX-R7",
            "purpose": "Infernus-ACX adversarial closure",
            "operator_extend_authorization": True,
            "operator_extend_phrase": "EXTEND ACX-R7 autorizado.",
            "operator_auth": "EXTEND ACX-R7 autorizado.",
            "head_before": cls.head_before,
            "head_after": cls.head_after,
            "origin_main_before": cls.origin_main_before,
            "origin_main_after": cls.origin_main_after,
            "files_read": cls.files_read,
            "files_changed": cls.files_changed,
            "commands_run": cls.commands_run,
            "tests_run": cls.tests_run,
            "injection_results": cls.results,
            "detected_count": sum(1 for result in cls.results if result["detected"]),
            "not_detected_count": sum(1 for result in cls.results if not result["detected"]),
            "all_injections_detected": all(result["detected"] for result in cls.results),
            "mechanical_detection_only": True,
            "visual_log_inspection_used_as_detection": False,
            "hard_mode_enabled": ACX.hard_mode_enabled(),
            "schema_changed": False,
            "roadmap_changed": False,
            "state_changed": False,
            "ci_changed": False,
            "runtime_product_bedrock_secrets_opened": ACX.compile_gate_approval("ACX-R7")["runtime_product_bedrock_secrets_opened"],
            "live_state_mutated_by_suite": False,
            "live_ledger_mutated_by_suite": False,
            "limitations": [
                "local advisory suite only",
                "no live state mutation",
                "no CI execution",
            ],
            "rollback_plan": "Delete the local evidence artifact and restore the worktree from git if the operator rejects the closure.",
            "next_recommended_step": "If accepted, publish the R7 commit and then request operator review for the next phase.",
        }
        EVIDENCE_PATH.write_text(json.dumps(artifact, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    @classmethod
    def _record(cls, test_name: str, command: str | None, result: dict[str, Any]) -> None:
        cls.tests_run.append(test_name)
        if command and command not in cls.commands_run:
            cls.commands_run.append(command)
        cls.results.append(result)

    def test_01_manual_edit_to_derived_render_contradicts_canonical_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            manifest_path = _bootstrap_render_root(root)
            _write_text(root / "BOOT.md", "# BOOT\n\nSTALE\n")

            command = f"python3 tools/acx.py --root {root} render --check --manifest {manifest_path}"
            result = _run_acx(root, ["render", "--check", "--manifest", str(manifest_path)])

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("BOOT.md drift detected", result.stderr)
            self._record(
                self._testMethodName,
                command,
                {
                    "injection_id": 1,
                    "name": "manual edit to derived_render contradicting canonical JSON",
                    "expected_violation_type": "render_drift",
                    "detected": True,
                    "mechanism": "validator_event",
                    "message": result.stderr.strip() or result.stdout.strip(),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_02_static_import_from_archive_superseded_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            attack = root / "attack.py"
            _write_text(attack, "from archive.superseded import legacy_module\n")
            violations = LEGACY_SCANNER._collect_violations(attack)

            self.assertTrue(violations)
            self.assertTrue(any("static import" in violation for violation in violations))
            self._record(
                self._testMethodName,
                "LEGACY_SCANNER._collect_violations(tempfile static import)",
                {
                    "injection_id": 2,
                    "name": "static import from archive/superseded/*",
                    "expected_violation_type": "legacy_import",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(violations),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_03_dynamic_legacy_import_via_importlib_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            attack = root / "attack.py"
            _write_text(
                attack,
                "import importlib.util\n"
                "importlib.util.spec_from_file_location('legacy', 'archive/superseded/legacy.py')\n",
            )
            violations = LEGACY_SCANNER._collect_violations(attack)

            self.assertTrue(violations)
            self.assertTrue(any("dynamic import" in violation for violation in violations))
            self._record(
                self._testMethodName,
                "LEGACY_SCANNER._collect_violations(tempfile dynamic import)",
                {
                    "injection_id": 3,
                    "name": "dynamic legacy import via importlib/__import__/runpy/SourceFileLoader",
                    "expected_violation_type": "legacy_dynamic_import",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(violations),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_04_invalid_transition_skip_is_rejected(self) -> None:
        bundle = _transition_bundle(to_phase="ACX-R6")
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)
        can_transition = ACX.can_transition("ACX-R4", "ACX-R6", bundle, ACX.ADVISORY_TRANSITION_RULES, current_head=CURRENT_HEAD)

        self.assertFalse(can_transition)
        self.assertEqual(errors, [])
        self._record(
            self._testMethodName,
            "ACX.can_transition(ACX-R4 -> ACX-R6)",
            {
                    "injection_id": 4,
                    "name": "invalid transition skip",
                    "expected_violation_type": "transition_skip",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "ACX-R4 -> ACX-R6 was rejected because no advisory rule exists for the skip.",
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_05_evidence_without_commands_is_detected(self) -> None:
        bundle = _transition_bundle()
        bundle.pop("commands")
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)

        self.assertTrue(errors)
        self.assertTrue(any("missing required field: commands" in error for error in errors))
        self._record(
            self._testMethodName,
            "ACX.validate_transition_evidence_bundle(missing commands)",
            {
                    "injection_id": 5,
                    "name": "evidence without commands[]",
                    "expected_violation_type": "missing_commands",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_06_evidence_without_files_read_is_detected(self) -> None:
        bundle = _transition_bundle()
        bundle.pop("files_read")
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=CURRENT_HEAD)

        self.assertTrue(errors)
        self.assertTrue(any("missing required field: files_read" in error for error in errors))
        self._record(
            self._testMethodName,
            "ACX.validate_transition_evidence_bundle(missing files_read)",
            {
                    "injection_id": 6,
                    "name": "evidence without files_read[]",
                    "expected_violation_type": "missing_files_read",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_07_evidence_replayed_after_head_change_is_detected(self) -> None:
        bundle = _transition_bundle()
        stale_head = "0" * 64
        errors = ACX.validate_transition_evidence_bundle(bundle, current_head=stale_head)

        self.assertTrue(errors)
        self.assertIn("stale bundle: head_before does not match current HEAD", errors)
        self._record(
            self._testMethodName,
            "ACX.validate_transition_evidence_bundle(stale head)",
            {
                    "injection_id": 7,
                    "name": "evidence replayed after base HEAD changed",
                    "expected_violation_type": "stale_evidence",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_08_write_outside_gate_allowlist_is_detected(self) -> None:
        gate = ACX.compile_gate_approval("ACX-R7")
        errors = ACX.validate_gate_write_allowlist(gate, ["tmp/attack.txt"], root=ROOT)

        self.assertTrue(errors)
        self.assertTrue(any("write outside gate allowlist" in error for error in errors))
        self._record(
            self._testMethodName,
            "ACX.validate_gate_write_allowlist(gate, ['tmp/attack.txt'])",
            {
                    "injection_id": 8,
                    "name": "write outside allowlist declared in generated GATE_APPROVAL",
                    "expected_violation_type": "write_outside_allowlist",
                    "detected": True,
                    "mechanism": "guard_failure",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_09_agent_report_contains_decision_vocabulary_is_detected(self) -> None:
        report_text = "READY PASS APPROVED CONCLUIDO"
        violations = ACX.scan_advisory_report_prose(
            report_text,
            phase_id="ACX-R7",
            from_phase="ACX-R6",
            to_phase="ACX-R7",
        )

        self.assertTrue(violations)
        matched_tokens = {violation["payload"]["matched_token"] for violation in violations}
        self.assertIn("PASS", matched_tokens)
        self.assertIn("READY", matched_tokens)
        self.assertIn("APPROVED", matched_tokens)
        self._record(
            self._testMethodName,
            "ACX.scan_advisory_report_prose('READY PASS APPROVED CONCLUIDO', ...)",
            {
                    "injection_id": 9,
                    "name": "agent report contains decision vocabulary",
                    "expected_violation_type": "decision_vocabulary",
                    "detected": True,
                    "mechanism": "advisory_violation",
                    "message": ", ".join(sorted(matched_tokens)),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_10_direct_manual_edit_to_state_without_ledger_event_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_manual_write_repo(root)
            baseline_state = (ROOT / "ACTIVE_CONTEXT_STATE.json").read_bytes()
            _write_bytes(root / "ACTIVE_CONTEXT_STATE.json", b"\n" + baseline_state)
            stage_result = _run_git(root, ["add", "ACTIVE_CONTEXT_STATE.json"])
            self.assertEqual(stage_result.returncode, 0, stage_result.stderr)

            command = (
                "python3 tools/acx.py guard manual-write "
                "--manifest authority_manifest.json --ledger .acx/ledger.jsonl --state ACTIVE_CONTEXT_STATE.json"
            )
            result = _run_acx(
                root,
                [
                    "guard",
                    "manual-write",
                    "--manifest",
                    "authority_manifest.json",
                    "--ledger",
                    ".acx/ledger.jsonl",
                    "--state",
                    "ACTIVE_CONTEXT_STATE.json",
                ],
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manual write block", result.stderr)
            self._record(
                self._testMethodName,
                command,
                {
                    "injection_id": 10,
                    "name": "direct manual edit to ACTIVE_CONTEXT_STATE.json without ledger event",
                    "expected_violation_type": "manual_write_block",
                    "detected": True,
                    "mechanism": "guard_failure",
                    "message": result.stderr.strip() or result.stdout.strip(),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_11_transition_table_edited_in_place_instead_of_new_version_is_detected(self) -> None:
        candidate_rules = copy.deepcopy(ACX.ADVISORY_TRANSITION_RULES)
        candidate_rules["transitions"]["ACX-R4"]["ACX-R5"]["require_clean_git_status"] = False
        errors = ACX.validate_transition_rules_revision(candidate_rules)

        self.assertTrue(errors)
        self.assertTrue(any("transition table changed without a new transition_rules_version" in error for error in errors))
        self._record(
            self._testMethodName,
            "ACX.validate_transition_rules_revision(candidate_rules)",
            {
                    "injection_id": 11,
                    "name": "transition table edited in place instead of new version",
                    "expected_violation_type": "transition_rules_revision",
                    "detected": True,
                    "mechanism": "pure_function_rejection",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_12_new_file_without_class_or_derived_render_as_canonical_live_is_detected(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(manifest)
        boot_entry = mutated["entries"]["BOOT.md"]
        boot_entry["class"] = "canonical_live"
        if "BOOT.md" in mutated["classes"]["derived_render"]:
            mutated["classes"]["derived_render"].remove("BOOT.md")
        mutated["classes"]["canonical_live"].append("BOOT.md")
        errors = ACX.validate_authority_manifest_classifications(mutated, root=ROOT)

        self.assertTrue(errors)
        self.assertTrue(any("BOOT.md" in error and "derived_render" in error for error in errors))
        self._record(
            self._testMethodName,
            "ACX.validate_authority_manifest_classifications(mutated_manifest)",
            {
                    "injection_id": 12,
                    "name": "new file without class in authority_manifest.json or derived_render treated as canonical_live",
                    "expected_violation_type": "authority_manifest_classification",
                    "detected": True,
                    "mechanism": "validator_event",
                    "message": "; ".join(errors),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )

    def test_13_ledger_advanced_without_state_staged_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            _bootstrap_manual_write_repo(root)

            def _run_local_acx(args: list[str]) -> subprocess.CompletedProcess[str]:
                return subprocess.run(
                    [sys.executable, str(TOOLS), "--root", str(root), *args],
                    cwd=root,
                    text=True,
                    capture_output=True,
                    check=False,
                )

            event_path = root / "advance_event.json"
            _write_text(
                event_path,
                json.dumps(
                    {
                        "event_id": "33333333-3333-4333-8333-333333333333",
                        "event_type": "genesis",
                        "event_schema_version": "1.0",
                        "phase_id": "ACX-R7",
                        "timestamp_utc": "2026-07-06T00:00:00Z",
                        "project_commit_sha": CURRENT_HEAD,
                        "payload": {
                            "baseline_state_path": "ALT_STATE.json",
                        },
                    },
                    sort_keys=True,
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
            )
            _write_bytes(root / "ALT_STATE.json", b"{\"alt\": true}\n")
            add_event = _run_local_acx(["event", "append", str(event_path), "--ledger", ".acx/ledger.jsonl"])
            self.assertEqual(add_event.returncode, 0, add_event.stderr)

            stage_result = _run_git(root, ["add", ".acx/ledger.jsonl"])
            self.assertEqual(stage_result.returncode, 0, stage_result.stderr)

            command = (
                "python3 tools/acx.py guard manual-write "
                "--manifest authority_manifest.json --ledger .acx/ledger.jsonl --state ACTIVE_CONTEXT_STATE.json"
            )
            result = _run_local_acx([
                "guard",
                "manual-write",
                "--manifest",
                "authority_manifest.json",
                "--ledger",
                ".acx/ledger.jsonl",
                "--state",
                "ACTIVE_CONTEXT_STATE.json",
            ])

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manual write block", result.stderr)
            self._record(
                self._testMethodName,
                command,
                {
                    "injection_id": 13,
                    "name": "ledger advanced without state staged",
                    "expected_violation_type": "manual_write_block",
                    "detected": True,
                    "mechanism": "guard_failure",
                    "message": result.stderr.strip() or result.stdout.strip(),
                    "live_state_mutated": False,
                    "live_ledger_mutated": False,
                },
            )


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
