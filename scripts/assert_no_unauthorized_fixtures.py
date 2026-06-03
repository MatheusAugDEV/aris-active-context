import json, sys, pathlib

state = json.loads(pathlib.Path("ACTIVE_CONTEXT_STATE.json").read_text())
fixtures_allowed = state.get("authorization", {}).get("fixture_materialization_allowed", False)
root = pathlib.Path("fixtures/lab_simulation/aris_infernus_lab_full")

existe = root.exists() and any(root.rglob("*"))
if existe and not fixtures_allowed:
    print("BLOCK: fixtures reais existem mas fixture_materialization_allowed=false")
    sys.exit(1)
if not existe and fixtures_allowed:
    print("WARN: materializacao autorizada mas nenhuma fixture criada")
    sys.exit(0)
print("OK")
