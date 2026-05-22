# CONTEXT_INDEX

## Live pointers
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [NEXT_ACTION.md](NEXT_ACTION.md)
- [DECISION_LOCKS.md](DECISION_LOCKS.md)
- [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
- [BEDROCK_GATE.md](BEDROCK_GATE.md)
- [NORTH_POLE.md](NORTH_POLE.md)
- [PHASE_SPECIFIC_GATES.md](PHASE_SPECIFIC_GATES.md)

## Recent phase references
- `F21-A54C` remote sync verification confirms both `origin/main` refs match local HEAD.
- `F21-A54B` hygiene repair compacted the active-context and kept the root push debt visible.
- `F21-A54` lean runner review passed locally and recorded stale duplicate blocks as a warning.
- `F21-A53` lean runner implementation produced the minimal local acceptance runner.

## Hygiene status
- active_context_remote_sync_verified: `True`
- root_repo_push_verified: `True`
- root_repo_push_pending: `False`
- nested_active_context_push_verified: `True`
- root_repo_worktree_dirty_unrelated: `True`

## Notes
- This index is compact and intentionally excludes stale repeated blocks.
- `NORTH_POLE.md` remains the strategic north reference.
