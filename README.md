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
- latest_completed_phase: `IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision`
- latest_completed_status: `if08_w4_post_sync_review_w5_readiness_pass`
- latest_completed_project_commit_sha: `d575b6f3c37c1ba411a2a0266efb9d04957234c0`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w4_post_sync_review_w5_readiness_pass`
- IF-08 real execution: `false`
- W4 preflight readiness: `true`
- W4 execution performed: `true`
- W4 execution allowed: `false`
- W5 readiness state: `ready_for_preparation`
- W5 preparation allowed next: `true`
- W5 execution performed: `false`
- W5 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W4_POST_SYNC_REVIEW: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W4 Controlled Execution Post-Sync Review & W5 Readiness Decision`.
The W4 post-sync review packet is canonical with `w4_execution_performed=true`, `w4_execution_allowed=false`, `synthetic_attack_cases_total=14`, `rollback_honesty_checks=6/6`, `duplicate_detection_checks=5/5`, `cost_enforcement_checks=3/3`, `RHR=DDR=CER=1.0`, `w5_readiness_state=ready_for_preparation`, `w5_preparation_allowed_next=true`, `w5_execution_performed=false`, and `w5_execution_allowed=false`; this sync does not authorize any real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
