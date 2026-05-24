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

## Bedrock v2 candidate selection
- latest_completed_phase: `F21-CTX-BEDROCK-R5 - Bedrock v2 Candidate Selection Gate`
- next_recommended_phase: `F21-CTX-BEDROCK-R6 - Bedrock v2 Candidate Selection Review Gate`
- next_gate_seen: `F21-CTX-BEDROCK-R6 - Bedrock v2 Candidate Selection Review Gate`
- source_r4_decision_path: `artifacts/f21/bedrock_v2_triage_review_decision.json`
- source_triage_plan_path: `artifacts/f21/bedrock_v2_research_triage_plan.json`
- r4_status: `bedrock_v2_triage_review_passed`
- r4_decision: `pass`
- candidate_selection_manifest_created: `True`
- candidate_selection_is_not_adoption: `True`
- selection_policy_valid: `True`
- selected_candidate_count: `60`
- quarantined_candidate_count: `3`
- rejected_candidate_count: `21`
- bedrock_v2_apply_allowed_now: `False`
- bedrock_v2_apply_plan_allowed_now: `False`
- bedrock_v2_candidate_adoption_allowed_now: `False`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

R5 selects candidates only; it does not adopt them or create an apply plan.
