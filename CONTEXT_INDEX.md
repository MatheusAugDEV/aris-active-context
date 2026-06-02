artifact routes are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Context Index

## Active Route

- Latest completed phase: `ARIS Infernus Lab FULL Controlled Fixture Materialization Apply Planning Gate`
- Previous execution phase: `ARIS Infernus Lab FULL Controlled Fixture Materialization Authorization Review Gate`
- Active next phase: `ARIS Infernus Lab FULL Controlled Fixture Materialization Apply Review Gate`
- Route class: `review_gate_only`

## Canonical Files

- Live state: `ACTIVE_CONTEXT_STATE.json`
- Schema: `ACTIVE_CONTEXT_SCHEMA.json`
- Validator: `scripts/validate_active_context_state.py`
- Roadmap authority: `ROADMAP_CANONICAL.md`
- Current state mirror: `CURRENT_STATE.md`
- Next action mirror: `NEXT_ACTION.md`
- Decision locks mirror: `DECISION_LOCKS.md`
- Ledger/history: `ARIS_PHASE_LEDGER.md`
- README: `README.md`
- Bedrock boundary: `BEDROCK_GATE.md`
- Future BenchUX plan: `benchux_plan.md`

## Current Phase Artifacts

- `ARIS_INFERNUS_FULL_CONTROLLED_FIXTURE_MATERIALIZATION_APPLY_PLANNING_GATE.md` records the planning-only apply boundary phase result.
- `artifacts/lab_simulation/aris_infernus_lab_full_controlled_fixture_materialization_apply_plan.json` records the future apply boundary, refusal conditions, proof package, and non-bypassable requirements.
- `artifacts/lab_simulation/aris_infernus_lab_full_controlled_fixture_materialization_apply_matrix.json` records the matrix of future checks, kill conditions, and non-authorization attestations.

## Future Planning References

- `benchux_plan.md` records the future `ARIS BenchUX Lab` plan. It is not an active route and does not authorize productization.

## Active Canonical Roadmap

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
BenchUX valida produto real.
Crisol refina.
Bedrock decide.
```
