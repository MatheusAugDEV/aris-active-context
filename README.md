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
- latest_completed_phase: `IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision`
- latest_completed_status: `if08_w5_post_sync_review_w6_readiness_pass`
- latest_completed_project_commit_sha: `e9dfae63206523f26fce5df907945952c7351ad5`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w5_post_sync_review_w6_readiness_pass`
- IF-08 real execution: `false`
- previous_phase_verified: `IF-08 W5 Business Chaos Controlled Execution`
- W5 canonical sync verified: `true`
- W5 metrics verified: `true`
- W5 artifacts complete: `true`
- W5 safety attestation verified: `true`
- W6 readiness state: `ready_for_preparation`
- W6 preparation allowed next: `true`
- W6 execution performed: `false`
- W6 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W5_POST_SYNC_REVIEW: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W5 Controlled Execution Post-Sync Review & W6 Readiness Decision`.
The W5 post-sync review packet is canonical as `pass` with `previous_phase_verified=IF-08 W5 Business Chaos Controlled Execution`, `w5_canonical_sync_verified=true`, `w5_metrics_verified=true`, `w5_artifacts_complete=true`, `w5_safety_attestation_verified=true`, `critical_coverage_cells_passed=12/12`, `critical_coverage_completion=1.0`, `business_scenarios_blocked_or_detected=14`, `sirene_oracle_mode=synthetic_transcript_only`, `w6_readiness_state=ready_for_preparation`, `future_ttr_required=0`, `future_har_required=1.0`, `w6_execution_performed=false`, and `w6_execution_allowed=false`; this sync does not authorize any real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
