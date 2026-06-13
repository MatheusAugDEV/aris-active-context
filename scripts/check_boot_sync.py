#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import tempfile

import render_boot

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOT_PATH = ROOT / "BOOT.md"


def check_boot_sync() -> tuple[bool, str]:
    rendered = render_boot.render_boot_text().encode("utf-8")
    committed = BOOT_PATH.read_bytes() if BOOT_PATH.exists() else b""
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(rendered)
        tmp.flush()
        temp_bytes = pathlib.Path(tmp.name).read_bytes()
    if temp_bytes != committed:
        return False, "BOOT.md out of sync with STATE.json — run render_boot.py"
    return True, "BOOT.md in sync"


def assert_boot_in_sync() -> None:
    ok, message = check_boot_sync()
    if not ok:
        raise SystemExit(message)


def main() -> int:
    ok, message = check_boot_sync()
    if not ok:
        print(message)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
