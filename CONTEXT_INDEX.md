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

## Bedrock v2 diagnostic
- latest_completed_phase: `F21-CTX-D13 - Bedrock Gate v2 Operational Diagnostic and False-Positive Simulation Gate`
- reviewed_phase_id: `F21-CTX-D12`
- source_d12_status: `active_context_source_of_truth_warning_resolution_apply_passed`
- source_d12_decision: `pass`
- no_warn_policy_verified: `True`
- diagnostic_completed: `True`
- simulated_cases_count: `20`
- false_positive_cases_detected: `10`
- bedrock_v2_required: `True`
- bedrock_v2_apply_allowed_now: `False`
- bedrock_v2_apply_recommended_next: `True`
- next_recommended_phase: `F21-CTX-D14 - Bedrock Gate v2 Product-Grade Absolutization Apply Plan Gate`
- next_gate_seen: `F21-CTX-D14 - Bedrock Gate v2 Product-Grade Absolutization Apply Plan Gate`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

D13 keeps Bedrock v2 as a future apply-plan target. The current Bedrock contract was diagnosed only, not modified.

## Historical markers
- Prior D13 source-of-truth review is preserved in the ledger as historical evidence.
- D12 resolved active-context warning debt operationally and preserved removed blocks in artifacts.
- D11R created the no-warn advancement policy and kept WARN non-advancing.
