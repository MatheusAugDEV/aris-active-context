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
- latest_completed_phase: `IF-08 W5 Business Chaos Preflight Readiness`
- latest_completed_status: `if08_w5_business_chaos_preflight_readiness_blocked`
- latest_completed_project_commit_sha: `108ea32fa3a2f9b444f59b49818f5f7f7d6bc60c`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w5_business_chaos_preflight_readiness_blocked`
- IF-08 real execution: `false`
- W5 preflight readiness: `false`
- W5 readiness state: `blocked`
- W5 preparation allowed next: `false`
- W5 execution performed: `false`
- W5 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W5_BUSINESS_CHAOS_PREFLIGHT_READINESS: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W5 Business Chaos Preflight Readiness`.
The W5 preflight packet is canonical as `blocked` with `eligible_executor_bot_count=13`, `conditional_or_deferred_bot_count=1`, `synthetic_domain_count=7`, `critical_coverage_cells_ready=11/12`, `readiness_coverage=0.916667`, `blocker_id=sirene_conditional_or_deferred_with_reason`, `w5_execution_performed=false`, and `w5_execution_allowed=false`; this sync does not authorize any real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
