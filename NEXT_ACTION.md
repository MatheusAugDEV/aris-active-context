Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Next Action

## Current Next Step
- `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning Correction Gate`
- Status: `ready_for_next_subphase`
- Phase class: `planning_gate`
- Planning-only: `true`
- Review-only: `false`
- Execution authorization: `false`
- Controlled Apply Dry-Run Harness Readiness Review completed with decision `blocked`.
- Dangerous flags remain false and Bedrock remains non-executable.
- Roadmap amendment required: `True`
- This next phase does not authorize real dry-run execution or real apply.
- It does not authorize approval execution, runtime mutation, Debian harness execution, container/image/VM creation, package-manager execution, secrets access, external LLM/API usage, or dependency change.

## Before Starting the Next Phase
1. Read `ACTIVE_CONTEXT_STATE.json` first.
2. Run `python3 scripts/validate_active_context_state.py` and stop on any drift.
3. Confirm the readiness review blockers/warnings are carried forward explicitly.
4. Only then proceed with `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning Correction Gate`.
