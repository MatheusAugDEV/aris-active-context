#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HASH_ALGORITHM = "sha256"
DEFAULT_CANONICALIZATION_VERSION = "acx-ledger-canonical-v1"


class LedgerError(RuntimeError):
    pass


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def _event_hash(event: dict[str, Any]) -> str:
    material = dict(event)
    material.pop("event_sha256", None)
    return hashlib.sha256(_canonical_json_bytes(material)).hexdigest()


def _state_hash_from_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _resolve_relative_path(path_value: str, *, relative_to: Path = ROOT) -> Path:
    candidate = Path(path_value)
    return candidate if candidate.is_absolute() else (relative_to / candidate).resolve()


def _load_ledger(ledger_path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not ledger_path.exists():
        return []
    entries: list[tuple[int, dict[str, Any]]] = []
    with ledger_path.open("r", encoding="utf-8", newline="") as handle:
        for lineno, raw_line in enumerate(handle, 1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise LedgerError(f"line {lineno}: invalid JSON: {exc.msg}") from exc
            if not isinstance(event, dict):
                raise LedgerError(f"line {lineno}: event must be a JSON object")
            entries.append((lineno, event))
    return entries


def _ensure_field(
    event: dict[str, Any],
    name: str,
    value: Any,
    *,
    conflict_label: str | None = None,
) -> None:
    if name not in event or event[name] is None:
        event[name] = value
        return
    if event[name] != value:
        label = conflict_label or name
        raise LedgerError(f"{label} conflict: expected {value!r}, got {event[name]!r}")


def _normalize_event_for_append(event: dict[str, Any], previous_hash: str | None) -> dict[str, Any]:
    normalized = dict(event)
    normalized.setdefault("hash_algorithm", DEFAULT_HASH_ALGORITHM)
    normalized.setdefault("canonicalization_version", DEFAULT_CANONICALIZATION_VERSION)

    if normalized["hash_algorithm"] != DEFAULT_HASH_ALGORITHM:
        raise LedgerError(
            f"hash_algorithm must be {DEFAULT_HASH_ALGORITHM!r}, got {normalized['hash_algorithm']!r}"
        )
    if normalized["canonicalization_version"] != DEFAULT_CANONICALIZATION_VERSION:
        raise LedgerError(
            "canonicalization_version must be "
            f"{DEFAULT_CANONICALIZATION_VERSION!r}, got {normalized['canonicalization_version']!r}"
        )

    _ensure_field(normalized, "prev_sha256", previous_hash)
    _ensure_field(normalized, "ledger_head_hash", previous_hash)

    payload = normalized.get("payload")
    if normalized.get("event_type") == "genesis":
        if not isinstance(payload, dict):
            raise LedgerError("genesis payload must be a JSON object")
        baseline_path = payload.get("baseline_state_path")
        if baseline_path is None:
            raise LedgerError("genesis payload missing baseline_state_path")
        if not isinstance(baseline_path, str):
            raise LedgerError("genesis payload baseline_state_path must be a string")
        resolved = _resolve_relative_path(baseline_path)
        state_bytes = _read_bytes(resolved)
        state_hash = _state_hash_from_bytes(state_bytes)
        _ensure_field(normalized, "state_blob_hash", state_hash)
    else:
        if "state_blob_hash" not in normalized:
            normalized["state_blob_hash"] = None

    computed_hash = _event_hash(normalized)
    _ensure_field(normalized, "event_sha256", computed_hash, conflict_label="event_sha256")
    return normalized


def _validate_event_record(
    event: dict[str, Any],
    *,
    line_no: int,
    previous_hash: str | None,
    check_baseline: bool,
) -> str:
    if event.get("hash_algorithm") != DEFAULT_HASH_ALGORITHM:
        raise LedgerError(
            f"line {line_no}: hash_algorithm must be {DEFAULT_HASH_ALGORITHM!r}"
        )
    if event.get("canonicalization_version") != DEFAULT_CANONICALIZATION_VERSION:
        raise LedgerError(
            f"line {line_no}: canonicalization_version must be {DEFAULT_CANONICALIZATION_VERSION!r}"
        )

    if event.get("prev_sha256") != previous_hash:
        raise LedgerError(
            f"line {line_no}: prev_sha256 mismatch: expected {previous_hash!r}, "
            f"got {event.get('prev_sha256')!r}"
        )
    if event.get("ledger_head_hash") != previous_hash:
        raise LedgerError(
            f"line {line_no}: ledger_head_hash mismatch: expected {previous_hash!r}, "
            f"got {event.get('ledger_head_hash')!r}"
        )

    computed_hash = _event_hash(event)
    if event.get("event_sha256") != computed_hash:
        raise LedgerError(
            f"line {line_no}: event_sha256 mismatch: expected {computed_hash!r}, "
            f"got {event.get('event_sha256')!r}"
        )

    if check_baseline and event.get("event_type") == "genesis":
        payload = event.get("payload")
        if not isinstance(payload, dict):
            raise LedgerError(f"line {line_no}: genesis payload must be a JSON object")
        baseline_path = payload.get("baseline_state_path")
        if not isinstance(baseline_path, str):
            raise LedgerError(
                f"line {line_no}: genesis payload baseline_state_path must be a string"
            )
        resolved = _resolve_relative_path(baseline_path)
        state_hash = _state_hash_from_bytes(_read_bytes(resolved))
        if event.get("state_blob_hash") != state_hash:
            raise LedgerError(
                f"line {line_no}: state_blob_hash mismatch: expected {state_hash!r}, "
                f"got {event.get('state_blob_hash')!r}"
            )

    return computed_hash


def append_event(event_path: Path, ledger_path: Path) -> None:
    event = _load_json(event_path)
    if not isinstance(event, dict):
        raise LedgerError("event input must be a JSON object")

    entries = _load_ledger(ledger_path)
    previous_hash = entries[-1][1]["event_sha256"] if entries else None
    normalized = _normalize_event_for_append(event, previous_hash)

    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    with ledger_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
        handle.write("\n")


def verify_chain(ledger_path: Path) -> None:
    entries = _load_ledger(ledger_path)
    previous_hash = None
    for line_no, event in entries:
        previous_hash = _validate_event_record(
            event,
            line_no=line_no,
            previous_hash=previous_hash,
            check_baseline=True,
        )


def _fold_genesis_state(event: dict[str, Any]) -> bytes:
    payload = event.get("payload")
    if not isinstance(payload, dict):
        raise LedgerError("genesis payload must be a JSON object")

    baseline_path = payload.get("baseline_state_path")
    if isinstance(baseline_path, str):
        resolved = _resolve_relative_path(baseline_path)
        state_bytes = _read_bytes(resolved)
        expected_hash = event.get("state_blob_hash")
        if expected_hash is not None and _state_hash_from_bytes(state_bytes) != expected_hash:
            raise LedgerError(
                "genesis baseline state hash mismatch: "
                f"expected {expected_hash!r}"
            )
        return state_bytes

    baseline_state = payload.get("baseline_state")
    if baseline_state is not None:
        return json.dumps(
            baseline_state,
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        ).encode("utf-8") + b"\n"

    raise LedgerError("genesis payload missing baseline_state_path or baseline_state")


def fold(ledger_path: Path, out_path: Path) -> None:
    entries = _load_ledger(ledger_path)
    if not entries:
        raise LedgerError("ledger is empty")

    previous_hash = None
    folded_state: bytes | None = None
    for line_no, event in entries:
        previous_hash = _validate_event_record(
            event,
            line_no=line_no,
            previous_hash=previous_hash,
            check_baseline=True,
        )
        event_type = event.get("event_type")
        if event_type == "genesis":
            folded_state = _fold_genesis_state(event)
        elif event_type == "violation_advisory":
            continue
        else:
            raise LedgerError(
                f"line {line_no}: unsupported state-mutating event type {event_type!r}"
            )

    if folded_state is None:
        raise LedgerError("ledger does not contain a genesis event")

    _write_bytes(out_path, folded_state)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="acx.py")
    subparsers = parser.add_subparsers(dest="command", required=True)

    event_parser = subparsers.add_parser("event")
    event_subparsers = event_parser.add_subparsers(dest="event_command", required=True)
    append_parser = event_subparsers.add_parser("append")
    append_parser.add_argument("event_json", type=Path)
    append_parser.add_argument("--ledger", required=True, type=Path)

    fold_parser = subparsers.add_parser("fold")
    fold_parser.add_argument("--ledger", required=True, type=Path)
    fold_parser.add_argument("--out", required=True, type=Path)

    verify_parser = subparsers.add_parser("verify-chain")
    verify_parser.add_argument("--ledger", required=True, type=Path)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "event" and args.event_command == "append":
            append_event(args.event_json, args.ledger)
        elif args.command == "fold":
            fold(args.ledger, args.out)
        elif args.command == "verify-chain":
            verify_chain(args.ledger)
        else:  # pragma: no cover - argparse prevents this
            raise LedgerError(f"unsupported command: {args.command}")
    except LedgerError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
