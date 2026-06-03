# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Active-Context Circuit Breaker Gate`
- Previous execution phase: `ARIS Active-Context Phase Contract Hardening Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `4` — next governance gate is **BLOCKED**
- Only valid next gate: `INF-MAT-01` (fixture_materialization)

## Active Artifacts

- `artifacts/ac_break_05/decision.json`
- `artifacts/ac_break_05/summary.json`
- `artifacts/ac_break_05/report.md`
- `artifacts/ac_contract_04/decision.json`
- `artifacts/ac_contract_04/summary.json`
- `artifacts/ac_contract_04/report.md`
- `artifacts/ac_trans_03/decision.json`
- `artifacts/ac_trans_03/summary.json`
- `artifacts/ac_trans_03/report.md`
- `artifacts/ac_obs_02/decision.json`
- `artifacts/ac_obs_02/summary.json`
- `artifacts/ac_obs_02/report.md`
- `artifacts/ac_repair_01/decision.json`
- `artifacts/ac_repair_01/summary.json`
- `artifacts/ac_repair_01/report.md`
- `.github/workflows/validate_active_context.yml`

## CI

validate_active_context.yml runs on every push and PR to main.

## Non-Authorization

- No next phase is authorized until explicit manual operator authorization for INF-MAT-01.
- No real execution, no bot activation, and no runtime mutation.
- No real fixture materialization.
- No Bedrock PASS or product promotion.
- Circuit breaker active: governance_gate_streak=4 blocks all governance-class gates.
