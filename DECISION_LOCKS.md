current live locks are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Decision Locks

- Latest completed phase: `ARIS Capability Build Backend Baseline Gate`
- Status: `acb_cap_01_pass`
- Deferred phase: `null`
- next_phase_authorized_by_operator=false
- anti_proliferation_rule_active=true
- ci_enforcement_active=true
- gate_max_cycles=3
- gate_cycles_used=0
- auto_advance.enabled=true (governance/observability/transition_engine only, condition=ci_green_and_validator_pass)
- governance_gate_streak=0
- No next phase is authorized.
- ACB-CAP-02 remains closed pending explicit operator authorization.
- No repair apply, runtime patch, further bot execution, further Minos execution, runtime mutation, secrets access, Bedrock, or product promotion is authorized.
- fixture_materialization_executed=true (65 files / 13 scenarios on disk).
- bot_execution_executed=true (1 deterministic nemesis log on disk).
- minos_verdict_executed=true (1 deterministic Minos verdict on disk).
- purgatorium_finding_created=true (1 deterministic finding on disk).
- minimum_deliverable enforcement is active for pass decisions that declare a gated deliverable.

## Circuit Breaker State

governance_gate_streak=0 — preserved by ACB-CAP-01 capability-build pass. Governance gates are now
unblocked (streak < 3), but no gate is open. Next phase requires operator authorization.

## Gate cycle lock

The gate cycle budget is `gate_max_cycles`. `gate_cycles_used` increments on every commit that does not change `current_phase_id`. When the budget is exhausted the validator blocks; only the operator may close, issue a terminal verdict, or extend with a justification recorded in an artifact. The model may not extend on its own.
