Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Next Action

## Current Next Step
- `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Status: `ready_for_next_subphase`
- Phase class: `planning_gate`
- Planning-only: `true`
- Execution authorization: `false`
- Operator approval packet review is review-only, not execution approval.
- This is planning-only: it produces a plan artifact but does not authorize any runtime execution, real dry-run, real apply, or approval execution.
- Controlled Apply Operator Approval Packet Review passed as review-only and did not execute approval or authorize execution.
- The next phase is planning-only for controlled apply dry-run harness and does not authorize real dry-run execution.
- H4/H5/Hx not active current route.
- It does not authorize real dry-run, real apply, approval execution, runtime mutation, Debian harness execution, container/image/VM creation, or package-manager execution.

## Before Starting the Next Phase
1. Read `ACTIVE_CONTEXT_STATE.json` first.
2. Run `python3 scripts/validate_active_context_state.py` — if it fails, report drift and stop.
3. Confirm this file matches the JSON state.
4. Only then proceed with the planning phase.
