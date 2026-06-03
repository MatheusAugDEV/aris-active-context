# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Capability Build Dependency Foundation Gate`
- Previous execution phase: `ARIS Purgatorium Finding Record Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `0` — preserved by INF-BOT-01 capacity gate pass
- fixture_materialization_executed: `true` (65 files / 13 scenarios on disk)
- bot_execution_executed: `true` (1 deterministic nemesis log on disk)
- minos_verdict_executed: `true` (1 deterministic Minos verdict on disk)
- purgatorium_finding_created: `true` (1 deterministic finding record on disk)
- uv_lock_created_or_verified: `true` (`../uv.lock`)
- pip_audit_gate_created_or_verified: `true` (`../.github/workflows/supply-chain-baseline.yml`)
- cyclonedx_sbom_created_or_verified: `true` (`../artifacts/acb_core_01/sbom.cdx.json`)

## Active Artifacts

- `artifacts/purg_01/decision.json`
- `artifacts/purg_01/summary.json`
- `artifacts/purg_01/report.md`
- `artifacts/purg_01/finding_nemesis_validator_bypass.json`
- `../artifacts/acb_core_01/decision.json`
- `../artifacts/acb_core_01/summary.json`
- `../artifacts/acb_core_01/report.md`
- `../artifacts/acb_core_01/dependency_inventory.json`
- `../artifacts/acb_core_01/sbom.cdx.json`
- `../artifacts/acb_core_01/supply_chain_validation.json`
- `../artifacts/acb_core_01/uv_bootstrap.json`
- `../.github/workflows/supply-chain-baseline.yml`
- `../pyproject.toml`
- `../uv.lock`
- `artifacts/inf_minos_01/decision.json`
- `artifacts/inf_minos_01/summary.json`
- `artifacts/inf_minos_01/report.md`
- `artifacts/inf_minos_01/minos_verdict.json`
- `artifacts/inf_bot_01/decision.json`
- `artifacts/inf_bot_01/summary.json`
- `artifacts/inf_bot_01/report.md`
- `artifacts/inf_bot_01/nemesis_execution_log.json`
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

- No next phase is authorized until explicit manual operator authorization for ACB-CORE-02.
- No repair apply, runtime patch, further bot execution, further Minos execution, runtime mutation, secrets access, Bedrock, or product promotion.
- Circuit breaker streak remains 0. Governance gates are unblocked but no phase is open.
