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

- Latest completed phase: `ARIS Infernus Nemesis Synthetic Bot Execution Log Gate`
- Active next phase: `null`
- Active next phase class: `null`
- Operator authorization required before any new phase.
- Runtime execution authorized: `false`
- Real dry-run execution authorized: `false`
- Real apply authorized: `false`
- Product promotion allowed: `false`
- Bedrock executable now: `false`

## Transition Table

| current_phase_id | decision | next_phase_id | next_phase_class        | advance_mode  | minimum_deliverable |
|------------------|----------|---------------|-------------------------|---------------|---------------------|
| AC-REPAIR-01     | pass     | AC-OBS-02     | observability           | auto          | anti_proliferation_rule_active=true in JSON |
| AC-OBS-02        | pass     | AC-TRANS-03   | transition_engine       | auto          | assert_mirror_sync.py exists and passes |
| AC-TRANS-03      | pass     | AC-CONTRACT-04 | contract               | auto          | minimum_deliverable enforcement in validator for all pass transitions |
| AC-CONTRACT-04   | pass     | AC-BREAK-05   | circuit_breaker         | auto          | governance_gate_streak field in state with validator enforcement |
| AC-BREAK-05      | pass     | INF-MAT-01    | fixture_materialization | prompt_only   | fixtures/lab_simulation/aris_infernus_lab_full/ with min 13 dirs |
| INF-MAT-01       | pass     | INF-BOT-01    | bot_execution           | prompt_only   | at least 1 bot execution log with hash in artifacts/ |
| INF-BOT-01       | pass     | INF-MINOS-01  | minos_verdict           | prompt_only   | minos verdict JSON with deterministic threshold results |
| INF-MINOS-01     | pass     | PURG-01       | purgatorium             | prompt_only   | at least 1 finding record with severity and status |
| PURG-01          | pass     | BENCH-01      | benchux                 | prompt_only   | bench results JSON with real metrics |
| BENCH-01         | pass     | CRISOL-01     | crisol                  | prompt_only   | crisol refinement artifact with evidence |
| CRISOL-01        | pass     | BEDROCK-01    | bedrock                 | operator      | operator sign-off artifact |
| BEDROCK-01       | pass     | null          | product                 | operator      | product promotion artifact |
