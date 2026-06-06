## INF-FULL-01 — ARIS Infernus Full Scope Charter Gate Lock

- Latest completed phase: `ARIS Infernus Full Scope Charter Gate`
- Status: `inf_full_01_scope_charter_pass`
- Decision: `pass`
- Deferred phase: `null`
- next_phase_authorized_by_operator=false
- anti_proliferation_rule_active=true
- ci_enforcement_active=true
- gate_max_cycles=3
- gate_cycles_used=0
- auto_advance.enabled=true (governance/observability/transition_engine only, condition=ci_green_and_validator_pass)
- governance_gate_streak=0
- INF-FULL-01 is opened in JSON as a scope charter only.
- No next phase is authorized.
- No bot execution, runtime execution, product promotion, pilot authorization, Bedrock execution, secrets access, package installation, or external network execution is authorized.
- fixture_materialization_executed=true (65 files / 13 scenarios on disk).
- bot_execution_executed=true (1 deterministic nemesis log on disk, historical only).
- current_phase_bots_executed=false.
- minos_verdict_executed=true (1 deterministic Minos verdict on disk, historical only).
- purgatorium_finding_created=true (1 deterministic finding on disk, historical only).
- diagnostics and packaging remain quarantine hash-only modules until baseline freeze is recorded.

## Circuit Breaker State

governance_gate_streak=0 — preserved by the prior capability-build pass and carried into the scope-charter opening.

## Gate cycle lock

The gate cycle budget is `gate_max_cycles`. `gate_cycles_used` increments on every commit that does not change `current_phase_id`. When the budget is exhausted the validator blocks; only the operator may close, issue a terminal verdict, or extend with a justification recorded in an artifact.
