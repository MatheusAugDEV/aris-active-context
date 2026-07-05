from __future__ import annotations

import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = Path(__file__).resolve()
SCAN_ROOTS = (ROOT / "tools", ROOT / "tests")
LEGACY_IMPORT_MARKERS = (
    "archive/superseded",
    "archive.superseded",
)
LEGACY_DYNAMIC_MARKERS = (
    "archive/superseded",
    "archive.superseded",
    "validate_active_context.py",
    "SourceFileLoader",
    "runpy",
    "importlib",
)
LEGACY_CALL_NAMES = {
    "__import__",
    "builtins.__import__",
    "importlib.import_module",
    "importlib.util.spec_from_file_location",
    "runpy.run_module",
    "runpy.run_path",
    "SourceFileLoader",
    "importlib.machinery.SourceFileLoader",
}
LEGACY_EXEC_NAMES = {"exec", "eval", "builtins.exec", "builtins.eval"}


def _dotted_name(node: ast.AST, aliases: dict[str, str]) -> str:
    if isinstance(node, ast.Name):
        return aliases.get(node.id, node.id)
    if isinstance(node, ast.Attribute):
        base = _dotted_name(node.value, aliases)
        return f"{base}.{node.attr}" if base else node.attr
    return ""


def _render(node: ast.AST | None, aliases: dict[str, str], constants: dict[str, str]) -> str:
    if node is None:
        return ""
    if isinstance(node, ast.Constant):
        return node.value if isinstance(node.value, str) else str(node.value)
    if isinstance(node, ast.Name):
        return constants.get(node.id, aliases.get(node.id, node.id))
    if isinstance(node, ast.Attribute):
        base = _render(node.value, aliases, constants)
        return f"{base}.{node.attr}" if base else node.attr
    if isinstance(node, ast.BinOp):
        left = _render(node.left, aliases, constants)
        right = _render(node.right, aliases, constants)
        if isinstance(node.op, ast.Div):
            parts = [part.strip("/") for part in (left, right) if part]
            return "/".join(part for part in parts if part)
        if isinstance(node.op, ast.Add):
            return f"{left}{right}"
        return f"{left}{right}"
    if isinstance(node, ast.JoinedStr):
        pieces: list[str] = []
        for value in node.values:
            if isinstance(value, ast.FormattedValue):
                pieces.append(_render(value.value, aliases, constants))
            else:
                pieces.append(_render(value, aliases, constants))
        return "".join(pieces)
    if isinstance(node, ast.Call):
        call_name = _dotted_name(node.func, aliases)
        if call_name.endswith("Path") or call_name == "str" or call_name.endswith(".str"):
            return _render(node.args[0], aliases, constants) if node.args else ""
        args = ",".join(_render(arg, aliases, constants) for arg in node.args)
        if args:
            return f"{call_name}({args})"
        return call_name
    if isinstance(node, ast.Tuple):
        return ",".join(_render(element, aliases, constants) for element in node.elts)
    if isinstance(node, ast.List):
        return ",".join(_render(element, aliases, constants) for element in node.elts)
    if isinstance(node, ast.Set):
        return ",".join(_render(element, aliases, constants) for element in node.elts)
    if isinstance(node, ast.Subscript):
        value = _render(node.value, aliases, constants)
        slice_value = _render(node.slice, aliases, constants)
        return f"{value}[{slice_value}]"
    return ""


def _build_aliases(tree: ast.Module) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                aliases[alias.asname or alias.name] = alias.name
        elif isinstance(node, ast.ImportFrom):
            base = "." * node.level + (node.module or "")
            for alias in node.names:
                target = f"{base}.{alias.name}" if base else alias.name
                aliases[alias.asname or alias.name] = target
    return aliases


def _build_constants(tree: ast.Module, aliases: dict[str, str]) -> dict[str, str]:
    constants: dict[str, str] = {}
    for _ in range(4):
        changed = False
        for node in tree.body:
            target: ast.AST | None = None
            value: ast.AST | None = None
            if isinstance(node, ast.Assign) and len(node.targets) == 1:
                target = node.targets[0]
                value = node.value
            elif isinstance(node, ast.AnnAssign) and node.value is not None:
                target = node.target
                value = node.value
            if isinstance(target, ast.Name) and value is not None:
                rendered = _render(value, aliases, constants)
                if rendered and constants.get(target.id) != rendered:
                    constants[target.id] = rendered
                    changed = True
        if not changed:
            break
    return constants


def _contains_legacy_markers(text: str, markers: tuple[str, ...]) -> bool:
    normalized = text.replace("\\", "/")
    return any(marker in normalized for marker in markers)


def _call_payload(node: ast.Call, aliases: dict[str, str], constants: dict[str, str]) -> str:
    parts = [_render(arg, aliases, constants) for arg in node.args]
    parts.extend(_render(keyword.value, aliases, constants) for keyword in node.keywords)
    return " ".join(part for part in parts if part)


def _call_name(node: ast.AST, aliases: dict[str, str]) -> str:
    if isinstance(node, ast.Name):
        return aliases.get(node.id, node.id)
    if isinstance(node, ast.Attribute):
        base = _call_name(node.value, aliases)
        return f"{base}.{node.attr}" if base else node.attr
    return ""


def _sys_path_target(text: str) -> bool:
    return "sys.path" in text


def _collect_violations(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    aliases = _build_aliases(tree)
    constants = _build_constants(tree, aliases)
    violations: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported = alias.name
                if _contains_legacy_markers(imported, LEGACY_IMPORT_MARKERS):
                    violations.append(f"{node.lineno}: static import {imported!r}")
        elif isinstance(node, ast.ImportFrom):
            base = "." * node.level + (node.module or "")
            for alias in node.names:
                imported = f"{base}.{alias.name}" if base else alias.name
                if _contains_legacy_markers(imported, LEGACY_IMPORT_MARKERS):
                    violations.append(f"{node.lineno}: static import {imported!r}")
        elif isinstance(node, ast.Call):
            call_name = _call_name(node.func, aliases)
            rendered_payload = _call_payload(node, aliases, constants)
            if call_name in LEGACY_CALL_NAMES or call_name.endswith("SourceFileLoader"):
                if _contains_legacy_markers(rendered_payload, LEGACY_DYNAMIC_MARKERS):
                    violations.append(f"{node.lineno}: dynamic import {call_name!r} -> {rendered_payload!r}")
            if call_name in LEGACY_EXEC_NAMES:
                if _contains_legacy_markers(rendered_payload, LEGACY_DYNAMIC_MARKERS):
                    violations.append(f"{node.lineno}: exec/eval {call_name!r} -> {rendered_payload!r}")
            if _sys_path_target(call_name):
                if _contains_legacy_markers(rendered_payload, LEGACY_DYNAMIC_MARKERS):
                    violations.append(f"{node.lineno}: sys.path call {call_name!r} -> {rendered_payload!r}")
        elif isinstance(node, ast.Assign):
            target_text = ",".join(_render(target, aliases, constants) for target in node.targets)
            if _sys_path_target(target_text):
                rendered_value = _render(node.value, aliases, constants)
                if _contains_legacy_markers(rendered_value, LEGACY_DYNAMIC_MARKERS):
                    violations.append(f"{node.lineno}: sys.path assignment -> {rendered_value!r}")
        elif isinstance(node, ast.AugAssign):
            target_text = _render(node.target, aliases, constants)
            if _sys_path_target(target_text):
                rendered_value = _render(node.value, aliases, constants)
                if _contains_legacy_markers(rendered_value, LEGACY_DYNAMIC_MARKERS):
                    violations.append(f"{node.lineno}: sys.path augmentation -> {rendered_value!r}")

    return violations


class LegacyImportQuarantineTest(unittest.TestCase):
    def test_tools_and_tests_do_not_reference_legacy_paths(self) -> None:
        violations: list[str] = []
        for scan_root in SCAN_ROOTS:
            for path in scan_root.rglob("*.py"):
                if path == SELF_PATH:
                    continue
                violations.extend(
                    f"{path.relative_to(ROOT)}: {entry}" for entry in _collect_violations(path)
                )
        self.assertEqual(violations, [], "\n".join(violations))


if __name__ == "__main__":  # pragma: no cover - unittest CLI support
    unittest.main()
