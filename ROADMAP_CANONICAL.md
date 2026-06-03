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

- Latest completed phase: `ARIS Active-Context Transition Engine & Autonomous Loop Gate`
- Active next phase: `null`
- Active next phase class: `null`
- Operator authorization required before any new phase.
- Runtime execution authorized: `false`
- Real dry-run execution authorized: `false`
- Real apply authorized: `false`
- Product promotion allowed: `false`
- Bedrock executable now: `false`

## Transition Table

| current_phase_id | decision | next_phase_id | next_phase_class        | advance_mode  |
|------------------|----------|---------------|-------------------------|---------------|
| AC-REPAIR-01     | pass     | AC-OBS-02     | observability           | auto          |
| AC-OBS-02        | pass     | AC-TRANS-03   | transition_engine       | auto          |
| AC-TRANS-03      | pass     | INF-MAT-01    | fixture_materialization | prompt_only   |
| INF-MAT-01       | pass     | INF-BOT-01    | bot_execution           | prompt_only   |
| INF-BOT-01       | pass     | INF-MINOS-01  | minos_verdict           | prompt_only   |
| INF-MINOS-01     | pass     | PURG-01       | purgatorium             | prompt_only   |
| PURG-01          | pass     | BENCH-01      | benchux                 | prompt_only   |
| BENCH-01         | pass     | CRISOL-01     | crisol                  | prompt_only   |
| CRISOL-01        | pass     | BEDROCK-01    | bedrock                 | operator      |
| BEDROCK-01       | pass     | null          | product                 | operator      |
