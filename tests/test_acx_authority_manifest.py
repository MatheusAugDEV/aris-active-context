from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "acx.py"
RENDER_BOOT_MODULE = ROOT / "scripts" / "render_boot.py"


def _run(args: list[str], *, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOLS), *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def _load_render_boot_module():
    spec = importlib.util.spec_from_file_location("acx_render_boot_test", RENDER_BOOT_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load scripts/render_boot.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _render_boot_for_root(root: Path) -> str:
    module = _load_render_boot_module()
    module.ROOT = root
    module.STATE_PATH = root / "ACTIVE_CONTEXT_STATE.json"
    module.ROADMAP_PATH = root / "ROADMAP_CANONICAL.md"
    module.BOOT_PATH = root / "BOOT.md"
    module.MODEL_REASONING_POLICY_PATH = root / "MODEL_REASONING_POLICY.md"
    return module.render_boot_text()


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def _scan_exclusions() -> list[dict[str, str]]:
    return [
        {
            "path": "artifacts/acx/r3_authority_manifest_evidence.json",
            "reason": "Self-generated advisory evidence; excluded from scan to avoid evidence recursion.",
            "scope": "repo-self-reference-advisory",
        },
        {
            "path": "authority_manifest.json",
            "reason": "Self-generated advisory output; excluded from scan to avoid manifest recursion.",
            "scope": "repo-self-reference-advisory",
        },
    ]


class ACXAuthorityManifestTest(unittest.TestCase):
    def test_authority_manifest_generates_and_classifies_known_paths(self) -> None:
        manifest_path = ROOT / "authority_manifest.json"
        result = _run(["authority", "manifest", "--out", str(manifest_path)])
        self.assertEqual(result.returncode, 0, result.stderr)

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["mode"], "advisory")
        self.assertEqual(manifest["generated_by"], "tools/acx.py authority manifest")
        self.assertEqual(
            manifest["entries"]["ACTIVE_CONTEXT_STATE.json"]["class"],
            "canonical_live",
        )
        self.assertEqual(manifest["entries"]["BOOT.md"]["class"], "derived_render")
        self.assertEqual(
            manifest["entries"]["archive/superseded/OPERATOR_PREFERENCES.md"]["class"],
            "archived_forbidden",
        )
        self.assertEqual(manifest["entries"]["CURRENT_STATE.md"]["class"], "derived_render")
        self.assertEqual(manifest["entries"]["README.md"]["class"], "doc_support")
        self.assertEqual(manifest["scan_exclusions"], _scan_exclusions())

        check = _run(["authority", "check", "--manifest", str(manifest_path)])
        self.assertEqual(check.returncode, 0, check.stderr)

    def test_authority_check_rejects_missing_class(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "foo.txt").write_text("hello\n", encoding="utf-8")
            manifest_path = root / "authority_manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "manifest_version": "1",
                        "mode": "advisory",
                        "generated_by": "tools/acx.py authority manifest",
                        "source_of_truth_note": "test fixture",
                        "scan_exclusions": _scan_exclusions(),
                        "classes": {
                            "canonical_live": [],
                            "derived_render": [],
                            "doc_support": [],
                            "archived_forbidden": [],
                        },
                        "entries": {
                            "foo.txt": {
                                "reason": "fixture",
                                "source_rule": "fixture",
                            }
                        },
                    },
                    sort_keys=True,
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            result = _run(["--root", str(root), "authority", "check", "--manifest", str(manifest_path)])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("manifest entry missing class", result.stderr)

    def test_authority_check_rejects_invalid_class(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "foo.txt").write_text("hello\n", encoding="utf-8")
            manifest_path = root / "authority_manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "manifest_version": "1",
                        "mode": "advisory",
                        "generated_by": "tools/acx.py authority manifest",
                        "source_of_truth_note": "test fixture",
                        "scan_exclusions": _scan_exclusions(),
                        "classes": {
                            "canonical_live": [],
                            "derived_render": [],
                            "doc_support": [],
                            "archived_forbidden": [],
                        },
                        "entries": {
                            "foo.txt": {
                                "class": "bogus",
                                "reason": "fixture",
                                "source_rule": "fixture",
                            }
                        },
                    },
                    sort_keys=True,
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            result = _run(["--root", str(root), "authority", "check", "--manifest", str(manifest_path)])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("invalid class", result.stderr)

    def test_render_check_reports_missing_generator_as_advisory(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            shutil.copy2(ROOT / "ACTIVE_CONTEXT_STATE.json", root / "ACTIVE_CONTEXT_STATE.json")
            shutil.copy2(ROOT / "ROADMAP_CANONICAL.md", root / "ROADMAP_CANONICAL.md")
            _write_text(root / "CURRENT_STATE.md", "# CURRENT_STATE\n\nmirror\n")
            _write_text(root / "BOOT.md", _render_boot_for_root(root))

            manifest_path = root / "authority_manifest.json"
            manifest_result = _run(["--root", str(root), "authority", "manifest", "--out", str(manifest_path)])
            self.assertEqual(manifest_result.returncode, 0, manifest_result.stderr)

            check_result = _run(
                ["--root", str(root), "render", "--check", "--manifest", str(manifest_path)]
            )
            self.assertEqual(check_result.returncode, 0, check_result.stderr)
            self.assertIn("render_generator_missing", check_result.stdout)

    def test_render_check_detects_boot_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            shutil.copy2(ROOT / "ACTIVE_CONTEXT_STATE.json", root / "ACTIVE_CONTEXT_STATE.json")
            shutil.copy2(ROOT / "ROADMAP_CANONICAL.md", root / "ROADMAP_CANONICAL.md")
            _write_text(root / "CURRENT_STATE.md", "# CURRENT_STATE\n\nmirror\n")
            _write_text(root / "BOOT.md", _render_boot_for_root(root))

            manifest_path = root / "authority_manifest.json"
            manifest_result = _run(["--root", str(root), "authority", "manifest", "--out", str(manifest_path)])
            self.assertEqual(manifest_result.returncode, 0, manifest_result.stderr)

            _write_text(root / "BOOT.md", "# BOOT\n\nSTALE\n")
            drift_result = _run(["--root", str(root), "render", "--check", "--manifest", str(manifest_path)])
            self.assertNotEqual(drift_result.returncode, 0)
            self.assertIn("BOOT.md drift detected", drift_result.stderr)


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
