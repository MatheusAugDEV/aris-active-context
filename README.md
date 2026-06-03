# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Infernus Full Fixture Materialization Gate`
- Previous execution phase: `ARIS Active-Context Circuit Breaker Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `0` — reset by INF-MAT-01 capacity gate pass
- fixture_materialization_executed: `true` (65 files / 13 scenarios on disk)

## Active Artifacts

- `artifacts/inf_mat_01/decision.json`
- `artifacts/inf_mat_01/summary.json`
- `artifacts/inf_mat_01/report.md`
- `fixtures/lab_simulation/aris_infernus_lab_full/` (13 dirs, 65 files)
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

- No next phase is authorized until explicit manual operator authorization for INF-BOT-01.
- No bot execution, runtime mutation, secrets access, Bedrock, or product promotion.
- Circuit breaker streak reset to 0. Governance gates unblocked but no phase is open.
