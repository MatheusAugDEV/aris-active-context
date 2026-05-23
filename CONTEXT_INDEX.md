# CONTEXT_INDEX

## Live pointers
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [NEXT_ACTION.md](NEXT_ACTION.md)
- [DECISION_LOCKS.md](DECISION_LOCKS.md)
- [EXTERNAL_REFERENCES.md](EXTERNAL_REFERENCES.md)
- [MODEL_REASONING_POLICY.md](MODEL_REASONING_POLICY.md)
- [HANDOFF_RESPONSE_POLICY.md](HANDOFF_RESPONSE_POLICY.md)
- [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
- [BEDROCK_GATE.md](BEDROCK_GATE.md)
- [NORTH_POLE.md](NORTH_POLE.md)
- [PHASE_SPECIFIC_GATES.md](PHASE_SPECIFIC_GATES.md)

## Active Context Profiles
- [BOOT_PROFILE.md](BOOT_PROFILE.md)
- [READ_PROFILE.md](READ_PROFILE.md)

## Batch 2 review
- latest_completed_phase: `F21-CTX-D13 - Active Context OS Reform Batch 2 Source-of-Truth Warning Resolution Review Gate`
- reviewed_phase_id: `F21-CTX-D12`
- source_d12_status: `active_context_source_of_truth_warning_resolution_apply_passed`
- source_d12_decision: `pass`
- source_d12_warning_count: `0`
- source_d12_blocker_count: `0`
- no_warn_policy_verified: `True`
- warning_resolution_review_passed: `True`
- current_state_compaction_verified: `True`
- next_action_compaction_verified: `True`
- context_index_alignment_verified: `True`
- ledger_deduplication_verified: `True`
- removed_blocks_artifact_verified: `True`
- hashes_artifact_verified: `True`
- removed_block_count_verified: `9`
- next_recommended_phase: `F21-CTX-D14 - Active Context OS Reform Batch 2 Closure Gate`
- next_gate_seen: `F21-CTX-D14 - Active Context OS Reform Batch 2 Closure Gate`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

D13 keeps the index compact and routes the next step to closure after reviewing D12.

## Historical markers
- D12 resolved warnings operationally and preserved removed blocks in artifacts.
- D11R created the no-warn advancement policy and kept WARN non-advancing.
- D11 remains historical warning-state evidence only.
- D10 remains historical closure-state evidence only.
