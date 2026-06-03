import json, sys, pathlib

state = json.loads(pathlib.Path("ACTIVE_CONTEXT_STATE.json").read_text())

checks = {
    "CURRENT_STATE.md": [
        ("current_phase", state.get("current_phase", "")),
        ("decision", state.get("decision", "")),
    ],
    "NEXT_ACTION.md": [
        ("next_phase", str(state.get("next_phase", "null"))),
    ],
    "DECISION_LOCKS.md": [
        ("authorization_granted", str(state.get("authorization", {}).get("authorization_granted", False)).lower()),
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
