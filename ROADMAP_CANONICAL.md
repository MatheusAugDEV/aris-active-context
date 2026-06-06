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

- Latest completed phase: `ARIS Capability Build Advanced Supply Chain Gate`
- Active next phase: `null`
- Active next phase class: `null`
- Prompt emission continuity does not open `INF-FULL-01`; the successor remains operator-only.
- ACB decision registered: `artifacts/decisions/acb_decision_2026_06_03.json`
- ACB execution order registered: `artifacts/decisions/acb_execution_order_2026_06_03.json`
- Canonical successor after `ACB-CAP-05` is `INF-FULL-01` under `operator` once the prior PASS remains canonical and CI/validator evidence is green.
- Canonical successor after `ACB-CAP-05` is `INF-FULL-01` under `operator` mode.
- `INF-FULL-01` remains operator-only and unopened until the operator explicitly opens it.
- INF-FULL-01 remains operator-only and unopened until the operator explicitly opens it.
- Runtime execution authorized: `false`
- Real dry-run execution authorized: `false`
- Real apply authorized: `false`
- Product promotion allowed: `false`
- Bedrock executable now: `false`

## ARIS Capability Build (ACB)

Operator decision `ACB-APPROVED-2026-06-03` approved ARIS Capability Build before Infernus Full.

ACB execution order:
- `ACB-CORE-01` | `DEPENDENCY` | `uv + uv.lock + pip-audit CI gate + SBOM CycloneDX`
- `ACB-CORE-02` | `CORE` | `inventariar API publica, __all__ explicito, Protocols PEP 544`
- `ACB-CAP-01` | `BACKEND` | `FastAPI + JWT/API key por tenant + SlowAPI rate limit + health check`
- `ACB-CAP-02` | `MCP RUNTIME` | `banir STDIO, container isolado network=none, policy engine pre-dispatch, kill-switch, rollback`
- `ACB-CAP-03` | `RUNTIME TOP-LEVEL` | `consolidar logica de execucao apos MCP estavel, API publica clara`
- `ACB-CAP-04` | `PRODUCT/PILOT BOUNDARY` | `5 gates binarios PASS/FAIL antes de cliente real, workflow lab->staging->piloto executavel`
- `ACB-CAP-05` | `SUPPLY CHAIN AVANCADO` | `SBOM integridade + assinatura + monitoramento PyPI ranges vulneraveis + AIBOM prototipo`

Mandatory sequence:
`ACB-CORE-01 → ACB-CORE-02 → ACB-CAP-01 → ACB-CAP-02 → ACB-CAP-03 → ACB-CAP-04 → ACB-CAP-05 → INF-FULL-01 → PURG-FULL → INF-REVALIDATION → CRISOL → BEDROCK → PRODUTO`

Rules:
- Advanced research with Auditor Máximo standard precedes each ACB block.
- No layer skipping.
- Infernus Full starts only after ACB complete and CI green.
- `next_phase` remains `null` until an explicit canonical state transition is recorded.

## Lacunas críticas pré-Infernus Full

- Infernus Full não especificado como framework de teste — deve ser especificado antes de INF-FULL-01
- API pública do ARIS agora é definida pelo snapshot de `ACB-CORE-02` — qualquer drift futuro deve ser explicitamente ratificado antes de INF-FULL-01
- MCP SDK Python 2026 não coberto por papers — validar compatibilidade antes do ACB-CAP-02

## Transition Table

| current_phase_id | decision | next_phase_id | next_phase_class        | advance_mode  | minimum_deliverable |
|------------------|----------|---------------|-------------------------|---------------|---------------------|
| AC-REPAIR-01     | pass     | AC-OBS-02     | observability           | auto          | anti_proliferation_rule_active=true in JSON |
| AC-OBS-02        | pass     | AC-TRANS-03   | transition_engine       | auto          | assert_mirror_sync.py exists and passes |
| AC-TRANS-03      | pass     | AC-CONTRACT-04 | contract               | auto          | minimum_deliverable enforcement in validator for all pass transitions |
| AC-CONTRACT-04   | pass     | AC-BREAK-05   | circuit_breaker         | auto          | governance_gate_streak field in state with validator enforcement |
| AC-BREAK-05      | pass     | ACB-CORE-01   | capability_build        | prompt_only   | acb_decision artifact exists |
| INF-MAT-01       | pass     | INF-BOT-01    | bot_execution           | prompt_only   | at least 1 bot execution log with hash in artifacts/ |
| INF-BOT-01       | pass     | INF-MINOS-01  | minos_verdict           | prompt_only   | minos verdict JSON with deterministic threshold results |
| INF-MINOS-01     | pass     | PURG-01       | purgatorium             | prompt_only   | at least 1 finding record with severity and status |
| PURG-01          | pass     | ACB-CORE-01   | capability_build        | prompt_only   | acb_decision artifact exists |
| ACB-CORE-01      | pass     | ACB-CORE-02   | capability_build        | prompt_only   | uv.lock + pip-audit CI gate + SBOM exists |
| ACB-CORE-02      | pass     | ACB-CAP-01    | capability_build        | prompt_only   | __all__ snapshot committed |
| ACB-CAP-01       | pass     | ACB-CAP-02    | capability_build        | prompt_only   | FastAPI health check + auth passing |
| ACB-CAP-02       | pass     | ACB-CAP-03    | capability_build        | prompt_only   | MCP sandbox running + STDIO banned |
| ACB-CAP-03       | pass     | ACB-CAP-04    | capability_build        | prompt_only   | runtime public API documented |
| ACB-CAP-04       | pass     | ACB-CAP-05    | capability_build        | prompt_only   | pilot gates defined |
| ACB-CAP-05       | pass     | INF-FULL-01   | infernus_full           | operator      | all ACB complete + Infernus spec exists |
| BENCH-01         | pass     | CRISOL-01     | crisol                  | prompt_only   | crisol refinement artifact with evidence |
| CRISOL-01        | pass     | BEDROCK-01    | bedrock                 | operator      | operator sign-off artifact |
| BEDROCK-01       | pass     | null          | product                 | operator      | product promotion artifact |
