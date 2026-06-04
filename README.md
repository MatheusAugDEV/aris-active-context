# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- `OPERATOR_PREFERENCES.md` is a priority-read prompt emission preference layer and never overrides JSON, schema, validator, Transition Table, or explicit safety locks.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Capability Build Backend Baseline Gate`
- Previous execution phase: `ARIS Capability Build Core Public API Baseline Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `0` — preserved by ACB-CAP-01 capability-build pass
- fixture_materialization_executed: `true` (65 files / 13 scenarios on disk)
- bot_execution_executed: `true` (1 deterministic nemesis log on disk)
- minos_verdict_executed: `true` (1 deterministic Minos verdict on disk)
- purgatorium_finding_created: `true` (1 deterministic finding record on disk)
- uv_lock_created_or_verified: `true` (`../uv.lock`)
- pip_audit_gate_created_or_verified: `true` (`../.github/workflows/supply-chain-baseline.yml`)
- cyclonedx_sbom_created_or_verified: `true` (`../artifacts/acb_core_01/sbom.cdx.json`)
- fastapi_health_check_passing: `true` (`../artifacts/acb_cap_01/decision.json`)
- jwt_auth_passing: `true` (`../artifacts/acb_cap_01/auth_matrix.json`)
- api_key_auth_passing: `true` (`../artifacts/acb_cap_01/auth_matrix.json`)
- slowapi_rate_limit_passing: `true` (`../artifacts/acb_cap_01/rate_limit_report.json`)

## Active Artifacts

- `artifacts/purg_01/decision.json`
- `artifacts/purg_01/summary.json`
- `artifacts/purg_01/report.md`
- `artifacts/purg_01/finding_nemesis_validator_bypass.json`
- `artifacts/decisions/acb_cap_01_operator_authorization_2026_06_03.json`
- `artifacts/decisions/acb_cap_01_project_evidence_2026_06_03.json`
- `../artifacts/acb_cap_01/decision.json`
- `../artifacts/acb_cap_01/summary.json`
- `../artifacts/acb_cap_01/report.md`
- `../artifacts/acb_cap_01/research_basis.json`
- `../artifacts/acb_cap_01/backend_contract.json`
- `../artifacts/acb_cap_01/auth_matrix.json`
- `../artifacts/acb_cap_01/rate_limit_report.json`
- `../artifacts/acb_cap_01/public_api_drift_report.json`
- `../artifacts/acb_cap_01/import_stability_report.json`
- `../.github/workflows/backend-baseline.yml`
- `../scripts/run_acb_cap_01_backend_baseline.py`
- `../tests/test_acb_cap_01_backend.py`
- `../src/aris/backend/__init__.py`
- `../src/aris/backend/app.py`
- `../src/aris/backend/auth.py`
- `../src/aris/backend/contracts.py`
- `../src/aris/backend/rate_limit.py`
- `artifacts/decisions/acb_core_01_project_evidence_2026_06_03.json`
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

## Prompt Emission Preference

- When the Transition Table says `advance_mode=prompt_only`, the previous phase is canonically PASS, CI/validator evidence is green, and no explicit manual/operator lock exists for that exact transition, the assistant should directly emit the next Codex prompt without asking for confirmation just to emit it.
- This preference does not open the next phase in JSON, does not change `next_phase`, and does not bypass `advance_mode=operator`.

## Non-Authorization

- No next phase is authorized until explicit manual operator authorization for ACB-CAP-02.
- No repair apply, runtime patch, further bot execution, further Minos execution, runtime mutation, secrets access, Bedrock, or product promotion.
- Circuit breaker streak remains 0. Governance gates are unblocked but no phase is open.
