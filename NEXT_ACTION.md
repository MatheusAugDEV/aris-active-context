Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Next Action

## Current Next Step
- `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Correction Readiness Review`
- Status: `ready_for_next_subphase`
- Phase class: `readiness_gate`
- Planning-only: `false`
- Review-only: `true`
- Execution authorization: `false`
- Controlled Apply Dry-Run Harness Planning Correction Gate passed as planning-only and artifact-only.
- The next phase must review the correction pack without authorizing real dry-run execution or real apply.
- Dangerous flags remain false and Bedrock remains non-executable.
- Roadmap amendment required: `True`

## Before Starting the Next Phase
1. Read `ACTIVE_CONTEXT_STATE.json` first.
2. Run `python3 scripts/validate_active_context_state.py` and stop on any drift.
3. Confirm the seven corrected blockers remain explicit in the correction matrix.
4. Only then proceed with `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Correction Readiness Review`.
