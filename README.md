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
- latest_completed_phase: `IF-08 W2 Controlled Execution Post-Sync Review & W3 Readiness Decision`
- latest_completed_status: `if08_w2_post_sync_review_w3_readiness_pass`
- latest_completed_project_commit_sha: `86d1ddba94c73bf78151da13b9e1dd0eaa07feb0`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w2_post_sync_review_w3_readiness_pass`
- IF-08 real execution: `false`
- W2 controlled execution verified: `true`
- W3 preparation allowed next: `true`
- W3 execution performed: `false`
- W3 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W2_POST_SYNC_REVIEW: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W2 Controlled Execution Post-Sync Review & W3 Readiness Decision`.
The W2 post-sync packet remains canonical with `w2_canonical_sync_verified=true`, `w2_far_observed=0`, `w2_ctl_observed=0`, `w3_preparation_allowed_next=true`, and `sirene_status=conditional_or_deferred_with_reason`; this sync does not authorize W3 execution or any other real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
