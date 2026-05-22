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
- `F21-A54B` active-context hygiene repair keeps the root push debt visible and points to remote sync verification next.
- `F21-A54` lean runner review passed locally and recorded stale duplicate blocks as a warning.
- `F21-A53` lean runner implementation produced the minimal local acceptance runner.
- `F21-A51` validator review kept acceptance runner work blocked until implementation existed.
- `F21-A50` validator implementation stayed local and stdlib-only.
- `F21-A49` schema review prepared the validator step.

## Hygiene status
- stale_duplicate_blocks_detected: `True`
- stale_duplicate_blocks_cleaned: `True`
- root_repo_push_verified: `False`
- root_repo_push_pending: `True`
- active_context_remote_sync_verified: `False`
- nested_active_context_push_verified: `False`

## Notes
- This index is compact and intentionally excludes stale repeated blocks.
- `NORTH_POLE.md` remains the strategic north reference.
