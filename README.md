# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- `OPERATOR_PREFERENCES.md` is a priority-read prompt emission preference layer and never overrides JSON, schema, validator, Transition Table, or explicit safety locks.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Capability Build Runtime Top-Level Public API Gate`
- Previous execution phase: `ARIS Capability Build MCP Runtime Sandbox Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `0` — preserved by ACB-CAP-03 capability-build pass
- fixture_materialization_executed: `true` (65 files / 13 scenarios on disk)
- bot_execution_executed: `true` (1 deterministic nemesis log on disk)
- minos_verdict_executed: `true` (1 deterministic Minos verdict on disk)
- purgatorium_finding_created: `true` (1 deterministic finding record on disk)
- uv_lock_created_or_verified: `true` (`../uv.lock`)
- pip_audit_gate_created_or_verified: `true` (`../.github/workflows/supply-chain-baseline.yml`)
- cyclonedx_sbom_created_or_verified: `true` (`../artifacts/acb_core_01/sbom.cdx.json`)
- runtime_public_api_documented: `true` (`../artifacts/acb_cap_03/runtime_public_api.md`)
- runtime_public_api_importable: `true` (`../artifacts/acb_cap_03/decision.json`)
- runtime_modes_enforced: `true` (`../artifacts/acb_cap_03/decision.json`)
- policy_pre_dispatch_passing: `true` (`../artifacts/acb_cap_03/decision.json`)
- kill_switch_passing: `true` (`../artifacts/acb_cap_03/decision.json`)
- rollback_contract_passing: `true` (`../artifacts/acb_cap_03/decision.json`)

## Active Artifacts

- `artifacts/decisions/acb_cap_03_project_evidence_2026_06_03.json`
- `../artifacts/acb_cap_03/decision.json`
- `../artifacts/acb_cap_03/summary.json`
- `../artifacts/acb_cap_03/report.md`
- `../artifacts/acb_cap_03/research_basis.json`
- `../artifacts/acb_cap_03/runtime_public_api.md`
- `../artifacts/acb_cap_03/runtime_public_api_contract.json`
- `../artifacts/acb_cap_03/runtime_facade_contract.json`
- `../artifacts/acb_cap_03/runtime_mode_matrix.json`
- `../artifacts/acb_cap_03/runtime_policy_bridge_matrix.json`
- `../artifacts/acb_cap_03/runtime_audit_report.json`
- `../artifacts/acb_cap_03/public_api_snapshot_before.json`
- `../artifacts/acb_cap_03/public_api_snapshot_after.json`
- `../artifacts/acb_cap_03/public_api_change_report.json`
- `../artifacts/acb_cap_03/import_stability_report.json`
- `../.github/workflows/runtime-public-api.yml`
- `.github/workflows/validate_active_context.yml`

## CI

validate_active_context.yml runs on every push and PR to main.

## Prompt Emission Preference

- When the Transition Table says `advance_mode=prompt_only`, the previous phase is canonically PASS, CI/validator evidence is green, and no explicit manual/operator lock exists for that exact transition, the assistant should directly emit the next Codex prompt without asking for confirmation just to emit it.
- When the operator sends a Codex result for a canonically PASS gate, the assistant may use that result as the continuity signal to validate and directly emit the next `prompt_only` Codex prompt; no ritual phrase such as `autorizo` is required.
- This preference does not open the next phase in JSON, does not change `next_phase`, and does not bypass `advance_mode=operator`.

## Non-Authorization

- No next phase is opened automatically by this preference; `ACB-CAP-04` remains unopened in JSON until a future canonical state transition is recorded.
- No repair apply, runtime patch, further bot execution, further Minos execution, runtime mutation, secrets access, Bedrock, or product promotion.
- Circuit breaker streak remains 0. Governance gates are unblocked but no phase is open.
