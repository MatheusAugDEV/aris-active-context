Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Next Action

## Current Next Step
- `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Evidence Packaging Planning Correction Gate`
- Status: `ready_for_next_subphase`
- Phase class: `planning_gate`
- Planning-only: `true`
- Review-only: `false`
- Execution authorization: `false`
- Operator Approval Response Evidence Packaging Readiness Review blocked because the source artifact manifest does not yet cover the required evidence-packaging-planning chain.
- The next phase must remain planning-only and repair manifest coverage without changing any synthetic-only, non-authorizing, or incomplete-by-design safety boundaries.
- Dangerous flags remain false and Bedrock remains non-executable.
- Roadmap amendment required: `True`

## Before Starting the Next Phase
1. Read `ACTIVE_CONTEXT_STATE.json` first.
2. Run `python3 scripts/validate_active_context_state.py` and stop on any drift.
3. Confirm the source artifact manifest adds explicit evidence-packaging-planning chain coverage without weakening synthetic-only or non-authorizing semantics.
4. Only then proceed with `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Evidence Packaging Planning Correction Gate`.
