## Bedrock v2 safe candidate review sequencing
- latest_completed_phase: `F21-CTX-BEDROCK-R9 - Bedrock v2 Safe Candidate Review Sequencing Gate`
- next_recommended_phase: `F21-CTX-BEDROCK-R10 - Bedrock v2 Low-Risk Candidate Source Verification Gate`
- next_gate_seen: `F21-CTX-BEDROCK-R10 - Bedrock v2 Low-Risk Candidate Source Verification Gate`
- source_r8_decision_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_review_decision.json`
- source_risk_register_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_review_decision.json`
- r8_status: `bedrock_v2_adoption_candidate_risk_review_passed`
- r8_decision: `pass`
- r8_verified: `True`
- sequencing_hash: `233b06d525de2bcc80542adfa4353afbb90289f3b330cb77b2792686671b33b6`
- sequencing_lane_count: `4`
- total_candidates_reviewed: `60`
- reviewable_candidate_count: `50`
- blocked_not_reviewable_count: `10`
- low_context_policy_review_count: `15`
- medium_design_review_count: `15`
- high_security_or_source_review_count: `20`
- blocked_for_adoption_count: `10`
- candidate_adoption_allowed_now: `False`
- candidate_approval_allowed_now: `False`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

R9 keeps safe candidate sequencing review-only; it does not approve candidates.

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

## Bedrock v2 adoption candidate risk review
- latest_completed_phase: `F21-CTX-BEDROCK-R8 - Bedrock v2 Adoption Candidate Risk Review Gate`
- next_recommended_phase: `F21-CTX-BEDROCK-R9 - Bedrock v2 Safe Candidate Review Sequencing Gate`
- next_gate_seen: `F21-CTX-BEDROCK-R9 - Bedrock v2 Safe Candidate Review Sequencing Gate`
- source_r7_decision_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_decision.json`
- source_risk_register_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_register.json`
- r7_status: `bedrock_v2_adoption_candidate_risk_passed`
- r7_decision: `pass`
- risk_register_reviewed: `True`
- risk_register_schema_valid: `True`
- risk_counts_match: `True`
- total_candidates_reviewed: `60`
- low_context_policy_risk_count: `15`
- medium_design_risk_count: `15`
- high_security_or_source_risk_count: `20`
- blocked_for_adoption_risk_count: `10`
- candidate_approval_allowed_now: `False`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

R8 reviews the risk register only; it does not approve candidates.
