# ARIS Active Context

## Canonical State

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- `project_mirror/docs/infernus_full/infernus_full_canonroadmap.md` is the canonical Infernus FULL roadmap.
- `OPERATOR_PREFERENCES.md` is a priority-read prompt emission preference layer and never overrides JSON, schema, validator, Transition Table, or explicit safety locks.
- Markdown drift against JSON is a blocking error.
- `excludent/` remains excluded_from_context and is NOT read by default. See EXCLUDENT_POLICY.md.

## Current Phase

- phase_id: `INF-FULL-07`
- latest_completed_phase: `IF-08 W3 Runtime/Tool/MCP/Sandbox Preflight Readiness`
- latest_completed_status: `if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_pass`
- latest_completed_project_commit_sha: `d9406a4507ce78d2512101963b76e2836b6ee712`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w3_runtime_tool_mcp_sandbox_preflight_readiness_pass`
- IF-08 real execution: `false`
- W3 preflight readiness: `true`
- W3 execution performed: `false`
- W3 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W3_RUNTIME_TOOL_MCP_SANDBOX_PREFLIGHT_READINESS: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W3 Runtime/Tool/MCP/Sandbox Preflight Readiness`.
The W3 preflight packet remains canonical with `w3_preflight_readiness=true`, `readiness_coverage=1.0`, `future_ser_required=0`, `future_rca_required=1.0`, and `sirene_status=conditional_or_deferred_with_reason`; this sync does not authorize real execution or any other real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
