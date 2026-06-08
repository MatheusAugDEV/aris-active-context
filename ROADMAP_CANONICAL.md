# ARIS Macro Roadmap Canonical Chain

This file is the canonical roadmap authority for active direction.
Live routing still comes from `ACTIVE_CONTEXT_STATE.json`; if this file conflicts with `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_STATE.json` wins and the drift is blocking.

## Canonical Chain

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
BenchUX valida produto real.
Crisol refina.
Bedrock decide.
```

## Active Route

Latest completed phase: IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness
Active next phase: IF-08
Active next phase class: infernus_full_execution
Standing authorization: canonroadmap approved by operator — see INFERNUS_STANDING_AUTHORIZATION.md
next_phase_authorized_by_operator: true
Real execution (waves against real systems, runtime, apply): false — requires operator execution command
W4 preflight readiness is canonical; this sync records w4_preflight_readiness=true, future_rhr_required=1.0, future_ddr_required=1.0, future_cer_required=1.0, readiness_coverage=1.0, and w4_execution_performed=false.
W4 preflight readiness is canonical; this sync records w4_execution_allowed=false, all runtime/apply/network/secret/cost/quota surfaces false, and the next step is W4 controlled execution in synthetic isolated lab only.
excludent/ remains excluded_from_context with read_by_default=false, authority=none, forensic_only.

Standing Authorization Policy
The operator approved infernus_full_canonroadmap.md. That approval is standing authorization for all Infernus FULL phases. The system reads the canonroadmap and executes the next step after each gate pass. No per-phase operator authorization gate is required.
Exception: execution of waves against real system, real apply, product promotion, Bedrock require explicit operator execution command.

## Transition Table

| current_phase_id | decision | next_phase_id | next_phase_class | advance_mode | minimum_deliverable |
|------------------|----------|---------------|------------------|--------------|---------------------|
| AC-REPAIR-01 | pass | AC-OBS-02 | observability | auto | anti_proliferation_rule_active=true in JSON |
| AC-OBS-02 | pass | AC-TRANS-03 | transition_engine | auto | assert_mirror_sync.py exists and passes |
| AC-TRANS-03 | pass | AC-CONTRACT-04 | contract | auto | minimum_deliverable enforcement in validator for all pass transitions |
| AC-CONTRACT-04 | pass | AC-BREAK-05 | circuit_breaker | auto | governance_gate_streak field in state with validator enforcement |
| AC-BREAK-05 | pass | ACB-CORE-01 | capability_build | prompt_only | acb_decision artifact exists |
| INF-MAT-01 | pass | INF-BOT-01 | bot_execution | prompt_only | at least 1 bot execution log with hash in artifacts/ |
| INF-BOT-01 | pass | INF-MINOS-01 | minos_verdict | prompt_only | minos verdict JSON with deterministic threshold results |
| INF-MINOS-01 | pass | PURG-01 | purgatorium | prompt_only | at least 1 finding record with severity and status |
| PURG-01 | pass | ACB-CORE-01 | capability_build | prompt_only | acb_decision artifact exists |
| ACB-CORE-01 | pass | ACB-CORE-02 | capability_build | prompt_only | uv.lock + pip-audit CI gate + SBOM exists |
| ACB-CORE-02 | pass | ACB-CAP-01 | capability_build | prompt_only | __all__ snapshot committed |
| ACB-CAP-01 | pass | ACB-CAP-02 | capability_build | prompt_only | FastAPI health check + auth passing |
| ACB-CAP-02 | pass | ACB-CAP-03 | capability_build | prompt_only | MCP sandbox running + STDIO banned |
| ACB-CAP-03 | pass | ACB-CAP-04 | capability_build | prompt_only | runtime public API documented |
| ACB-CAP-04 | pass | ACB-CAP-05 | capability_build | prompt_only | pilot gates defined |
| ACB-CAP-05 | pass | INF-FULL-01 | infernus_full | operator | all ACB complete + Infernus spec exists |
| INF-FULL-01 | pass | INF-FULL-02 | infernus_full | canonroadmap | scope charter decision + scope matrix + module scope manifest + charter markdown |
| INF-FULL-02 | pass | INF-FULL-03 | infernus_full | canonroadmap | infernus_full_canonroadmap.md + if00 transition/hermeticity + if01 ledger + if02 ontology/coverage + if03 oracle pack + if04 bot/permission pack |
| INF-FULL-03 | pass | INF-FULL-04 | infernus_full | canonroadmap | scenario pack + controls design + harness readiness + sandbox/cost/quota/replay/kill-switch contracts |
| INF-FULL-04 | pass | INF-FULL-05 | infernus_full | canonroadmap | if07 pre-execution review decision artifact + no bot/runtime execution attestation + scenario-count normalization evidence + validator evidence |
| INF-FULL-05 | pass | INF-FULL-06 | infernus_full_excludent_cleanup | canonroadmap | excludent policy + move manifest + only-canonroadmap-visible evidence + validator evidence |
| INF-FULL-06 | pass | INF-FULL-07 | infernus_full_execution_authorization | canonroadmap | IF-08 authorization decision artifact + no execution attestation + successor validation matrix + validator evidence |
| INF-FULL-07 | pass | IF-08 | infernus_full_execution | canonroadmap | canonroadmap standing authorization — no operator gate required before execution command |
| BENCH-01 | pass | CRISOL-01 | crisol | prompt_only | crisol refinement artifact with evidence |
| CRISOL-01 | pass | BEDROCK-01 | bedrock | operator | operator sign-off artifact |
| BEDROCK-01 | pass | null | product | operator | product promotion artifact |
