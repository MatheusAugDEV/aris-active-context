current live locks are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Decision Locks

- Latest completed phase: `ARIS Active-Context Circuit Breaker Gate`
- Status: `ac_break_05_pass`
- Deferred phase: `null`
- next_phase_authorized_by_operator=false
- anti_proliferation_rule_active=true
- ci_enforcement_active=true
- gate_max_cycles=3
- gate_cycles_used=0
- auto_advance.enabled=true (governance/observability/transition_engine only, condition=ci_green_and_validator_pass)
- governance_gate_streak=4
- No next phase is authorized.
- Next governance gate: BLOCKED (streak >= 3 → validator exits(1))
- No runtime execution, fixture materialization, bot activity, or runtime mutation is authorized.
- minimum_deliverable enforcement is active for pass decisions that declare a gated deliverable.

## Circuit Breaker Lock

governance_gate_streak=4. Any gate with phase_class in {governance_repair, observability,
transition_engine, contract, route} will be blocked by the validator before any state mutation.
Unique unlock: INF-MAT-01 (fixture_materialization) pass resets streak to 0.
The model cannot override, waive, or manually reset the streak counter.

## Gate cycle lock

The gate cycle budget is `gate_max_cycles`. `gate_cycles_used` increments on every commit that does not change `current_phase_id`. When the budget is exhausted the validator blocks; only the operator may close, issue a terminal verdict, or extend with a justification recorded in an artifact. The model may not extend on its own.
