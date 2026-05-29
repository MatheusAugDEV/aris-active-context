Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Next Action

## Current Next Step
- `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Request Simulation Final Review Gate`
- Status: `ready_for_next_subphase`
- Phase class: `review_gate_only`
- Planning-only: `false`
- Review-only: `true`
- Execution authorization: `false`
- Operator Approval Request Simulation Readiness Review passed as review-only and verified that the synthetic plan and schema remain non-contacting, non-capturing, non-authorizing, and false-approval resistant.
- The next phase must perform a final review gate over that reviewed synthetic pack while keeping real operator contact, approval capture, and execution authorization disabled.
- Dangerous flags remain false and Bedrock remains non-executable.
- Roadmap amendment required: `True`

## Before Starting the Next Phase
1. Read `ACTIVE_CONTEXT_STATE.json` first.
2. Run `python3 scripts/validate_active_context_state.py` and stop on any drift.
3. Confirm the reviewed synthetic pack remains synthetic-only, does not contact a real operator, and keeps all dangerous flags false.
4. Only then proceed with `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Request Simulation Final Review Gate`.
