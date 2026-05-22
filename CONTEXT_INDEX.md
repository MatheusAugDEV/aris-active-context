# CONTEXT_INDEX

## Live pointers
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [NEXT_ACTION.md](NEXT_ACTION.md)
- [DECISION_LOCKS.md](DECISION_LOCKS.md)
- [EXTERNAL_REFERENCES.md](EXTERNAL_REFERENCES.md)
- [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
- [BEDROCK_GATE.md](BEDROCK_GATE.md)
- [NORTH_POLE.md](NORTH_POLE.md)
- [PHASE_SPECIFIC_GATES.md](PHASE_SPECIFIC_GATES.md)
- [EXTERNAL_REFERENCES.md](EXTERNAL_REFERENCES.md)

## Recent phase references
- `F21-A58` planned the future Prompt Kernel v0.1 implementation boundary and kept runtime implementation blocked.
- `F21-A57` reviewed the Prompt Kernel v0.1 plan and kept implementation blocked.
- `F21-A56` created the Prompt Kernel v0.1 plan only and keeps implementation blocked until review.
- `F21-A55` post-sync closure reconciles the root commit divergence and keeps unrelated dirty work visible.
- `F21-A54C` remote sync verification confirmed both `origin/main` refs matched local HEAD.
- `F21-A54B` hygiene repair compacted the active-context and kept the root push debt visible.
- `F21-A54` lean runner review passed locally and recorded stale duplicate blocks as a warning.

## External reference index
- `ext_ref_huw_prosser_fury_2026_05`: catalogued external architectural reference for future Prompt Kernel, Context Compression, Memory Kernel, Skill Kernel, Tool Harness, Voice Runtime, UI Observability, and Action Runtime decisions.
- status: `catalogued_external_reference`
- implementation_allowed_now: `false`
- roadmap_direct_insert_allowed_now: `false`
- phase_sequence_change_allowed_now: `false`
- macroblock_mapping_required: `true`
- decision_gate_required_before_use: `true`
- source_of_truth_rank: `reference_only_non_authoritative`

## Hygiene status
- active_context_remote_sync_verified: `True`
- root_repo_push_verified: `True`
- root_repo_push_pending: `False`
- nested_active_context_push_verified: `True`
- root_worktree_dirty_unrelated: `True`
- prompt_kernel_planning_allowed_now: `False`
- prompt_kernel_implementation_allowed_now: `False`
- prompt_kernel_runtime_integration_allowed: `False`

## Notes
- This index is compact and intentionally excludes stale repeated blocks.
- External references are catalogued and reference-only, never authoritative for implementation.
- `NORTH_POLE.md` remains the strategic north reference.
- External references are advisory context only and do not authorize implementation, roadmap sequence changes, runtime mutation, MCP, product promotion, customer real use, or production release.
