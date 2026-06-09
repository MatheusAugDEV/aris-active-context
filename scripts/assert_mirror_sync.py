import json, sys, pathlib

state = json.loads(pathlib.Path("ACTIVE_CONTEXT_STATE.json").read_text())

checks = {
    "archive/derived_mirrors/CURRENT_STATE.md": [
        ("current_phase_id", state.get("current_phase_id", "")),
        ("decision", state.get("decision", "")),
    ],
    "archive/derived_mirrors/NEXT_ACTION.md": [
        ("next_phase", str(state.get("next_phase", "null"))),
    ],
    "DECISION_LOCKS.md": [
        (
            "next_phase_authorized_by_operator",
            str(state.get("next_phase_authorized_by_operator", False)).lower(),
        ),
    ],
}

failed = []
for filepath, pairs in checks.items():
    content = pathlib.Path(filepath).read_text().lower()
    for field, value in pairs:
        if value.lower() not in content:
            failed.append(f"{filepath}: missing '{value}' for field '{field}'")

if failed:
    for f in failed:
        print(f"DRIFT: {f}")
    sys.exit(1)

print("OK: mirrors in sync")
