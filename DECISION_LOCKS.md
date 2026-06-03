current live locks are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Decision Locks

- Latest completed phase: `ARIS Active-Context Transition Engine & Autonomous Loop Gate`
- Status: `ac_trans_03_pass`
- Deferred phase: `null`
- next_phase_authorized_by_operator=false
- anti_proliferation_rule_active=true
- ci_enforcement_active=true
- gate_max_cycles=3
- gate_cycles_used=0
- auto_advance.enabled=true (governance/observability/transition_engine only, condition=ci_green_and_validator_pass)
- No next phase is authorized.
- No runtime execution, fixture materialization, bot activity, or runtime mutation is authorized.

## Gate cycle lock

The gate cycle budget is `gate_max_cycles`. `gate_cycles_used` increments on every commit that does not change `current_phase_id`. When the budget is exhausted the validator blocks; only the operator may close, issue a terminal verdict, or extend with a justification recorded in an artifact. The model may not extend on its own.
