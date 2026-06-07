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
- latest_completed_phase: `IF-08 W1 Context/Memory/RAG Controlled Execution`
- latest_completed_status: `if08_w1_context_memory_rag_controlled_execution_pass`
- latest_completed_project_commit_sha: `1d0f51584e082d1f3f7c270df89d567a96066711`
- latest_completed_ci_state: `CI_GREEN_CONFIRMED`
- active_next_phase: `IF-08`
- Active next phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- current_status: `if08_w1_context_memory_rag_controlled_execution_pass`
- IF-08 real execution: `false`
- W1 controlled execution: `true_synthetic_isolated_lab_only`
- All execution locks: `false`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- ACTIVE_CONTEXT_REMOTE_MAIN_REFLECTS_IF08_W1_CONTEXT_MEMORY_RAG_CONTROLLED_EXECUTION: `true`
- PERMANENT_ACTIVE_UPDATE_RULE_INSTALLED: `true`

## What This Means

INF-FULL-07 remains the canonical current phase, while the latest verified operational packet is `IF-08 W1 Context/Memory/RAG Controlled Execution`.
The W1 controlled packet remains canonical with `cir_observed=1.0`; this sync records synthetic isolated execution only and does not authorize any real execution surface.
No PASS, next prompt, or handoff is canonical unless `MatheusAugDEV/aris-active-context/main` reflects the same result already verified in Project repo.
Do NOT execute real waves, real apply, product promotion, or Bedrock without explicit operator execution command.

## Boot Read Order

1. ACTIVE_CONTEXT_STATE.json
2. AGENT_IDENTITY.md
3. ACTIVE_CONTEXT_SCHEMA.json
4. scripts/validate_active_context_state.py
5. ROADMAP_CANONICAL.md
6. MANDATORY_READ_FIRST_RULES.md
7. CURRENT_STATE.md
8. NEXT_ACTION.md
9. DECISION_LOCKS.md
10. OPERATOR_PREFERENCES.md
11. CONTEXT_INDEX.md
12. ARIS_PHASE_LEDGER.md
13. README.md
14. PROMPT_CONTRACT.md
15. LAB_OPERATING_CONTRACT.md
16. EXCLUDENT_POLICY.md
17. INFERNUS_STANDING_AUTHORIZATION.md
18. project_mirror/docs/infernus_full/infernus_full_canonroadmap.md

## Do NOT read

- `excludent/` (excluded from context by policy)
- `archive/` (historical only, never active routing authority)
- `ARIS_INFERNUS_FULL_*_GATE.md` files (completed phases, moved to archive)
