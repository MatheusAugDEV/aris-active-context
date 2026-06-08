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
- latest_completed_phase: `IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness`
- latest_completed_status: `if08_w4_replay_rollback_concurrency_cost_preflight_readiness_pass`
- latest_completed_project_commit_sha: `2785b06e7a73b10675d30ed870fda7959e2e866a`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w4_replay_rollback_concurrency_cost_preflight_readiness_pass`
- IF-08 real execution: `false`
- W4 preflight readiness: `true`
- W4 execution performed: `false`
- W4 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W4_PREFLIGHT_READINESS: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W4 Replay/Rollback/Concurrency/Cost Preflight Readiness`.
The W4 preflight readiness packet is canonical with `w4_preflight_readiness=true`, `readiness_coverage=1.0`, `required_preflight_checks=12`, `ready_preflight_checks=12`, and `w4_execution_performed=false`; this sync does not authorize real W4 execution or any other real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
