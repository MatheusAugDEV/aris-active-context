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
- latest_completed_phase: `IF-08 W5 Business Chaos Preflight Gap Repair`
- latest_completed_status: `if08_w5_business_chaos_preflight_gap_repair_pass`
- latest_completed_project_commit_sha: `0c9921503418da9883bcc9288178bd3f05e0cd8c`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w5_business_chaos_preflight_gap_repair_pass`
- IF-08 real execution: `false`
- W5 preflight readiness: `true`
- W5 readiness state: `ready_for_controlled_execution_preparation`
- W5 preparation allowed next: `true`
- W5 execution performed: `false`
- W5 execution allowed: `false`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W5_BUSINESS_CHAOS_PREFLIGHT_GAP_REPAIR: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W5 Business Chaos Preflight Gap Repair`.
The W5 gap-repair packet is canonical as `pass` with `previous_blocked_phase=IF-08 W5 Business Chaos Preflight Readiness`, `repaired_blocker_id=sirene_conditional_or_deferred_with_reason`, `repaired_critical_cell=W5-CRIT-012`, `sirene_oracle_mode=synthetic_transcript_only`, `critical_coverage_cells_ready=12/12`, `readiness_coverage=1.0`, `w5_execution_performed=false`, and `w5_execution_allowed=false`; this sync does not authorize any real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.
