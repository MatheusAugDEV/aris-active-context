## Bedrock evidence bundle completeness gate draft
- latest_completed_phase: `F21-CTX-BEDROCK-R13 - Bedrock Evidence Bundle Completeness Gate Draft`
- next_recommended_phase: `F21-CTX-BEDROCK-R14 - Bedrock Blocker Scan Schema Draft`
- next_gate_seen: `F21-CTX-BEDROCK-R14 - Bedrock Blocker Scan Schema Draft`
- reviewed_boundary_lock_id: `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`
- reviewed_verdict_lock_id: `BEDROCK_VERDICT_CRITERIA_DRAFT`
- reviewed_schema_lock_id: `BEDROCK_EVIDENCE_BUNDLE_SCHEMA_DRAFT`
- reviewed_boundary_status: `bedrock_gate_global_product_boundary_lock_ready`
- reviewed_verdict_status: `bedrock_verdict_criteria_draft_ready`
- reviewed_schema_status: `bedrock_evidence_bundle_schema_draft_ready`
- completeness_gate_lock: [DECISION_LOCKS.md](DECISION_LOCKS.md)
- bedrock_gate_contract: [BEDROCK_GATE.md](BEDROCK_GATE.md)
- summary_artifact: `../artifacts/f21/bedrock_evidence_bundle_completeness_gate_draft_summary.json`
- report_artifact: `../artifacts/f21/bedrock_evidence_bundle_completeness_gate_draft_report.md`
- status: `bedrock_evidence_bundle_completeness_gate_draft_ready`
- decision: `pass`
- completeness_gate_draft_created: `True`
- required_evidence_matrix_defined: `True`
- minimum_validation_rule_defined: `True`
- minimum_validation_count: `5`
- blocker_handling_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`

R13 defines the completeness threshold for future Bedrock judgment; it does not execute a Bedrock verdict or authorize product promotion.

## Bedrock evidence bundle schema draft
- latest_completed_phase: `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`
- next_recommended_phase: `F21-CTX-BEDROCK-R13 - Bedrock Evidence Bundle Completeness Gate Draft`
- next_gate_seen: `F21-CTX-BEDROCK-R13 - Bedrock Evidence Bundle Completeness Gate Draft`
- reviewed_boundary_lock_id: `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`
- reviewed_verdict_lock_id: `BEDROCK_VERDICT_CRITERIA_DRAFT`
- reviewed_boundary_status: `bedrock_gate_global_product_boundary_lock_ready`
- reviewed_verdict_status: `bedrock_verdict_criteria_draft_ready`
- bedrock_gate_contract: [BEDROCK_GATE.md](BEDROCK_GATE.md)
- decision_lock: [DECISION_LOCKS.md](DECISION_LOCKS.md)
- summary_artifact: `../artifacts/f21/bedrock_evidence_bundle_schema_draft_summary.json`
- report_artifact: `../artifacts/f21/bedrock_evidence_bundle_schema_draft_report.md`
- status: `bedrock_evidence_bundle_schema_draft_ready`
- decision: `pass`
- evidence_bundle_schema_created: `True`
- minimum_validation_classes_defined: `True`
- minimum_validation_count: `5`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`

R12 defines the minimum evidence package structure for future Bedrock verdicts; it does not execute product promotion or runtime verdicts.

## Bedrock verdict criteria draft
- latest_completed_phase: `F21-CTX-BEDROCK-R11 - Bedrock Verdict Criteria Draft`
- next_recommended_phase: `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`
- next_gate_seen: `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`
- reviewed_boundary_lock_id: `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`
- reviewed_boundary_status: `bedrock_gate_global_product_boundary_lock_ready`
- bedrock_gate_contract: [BEDROCK_GATE.md](BEDROCK_GATE.md)
- decision_lock: [DECISION_LOCKS.md](DECISION_LOCKS.md)
- status: `bedrock_verdict_criteria_draft_ready`
- decision: `pass`
- verdict_classes_defined: `True`
- critical_dimensions_defined: `True`
- absolute_blockers_defined: `True`
- evidence_minima_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`

R11 drafts the Bedrock verdict taxonomy and thresholds only; it does not execute a product verdict.

## Bedrock Gate global product boundary lock
- lock_id: `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`
- phase_id: `F21-CTX-BEDROCK-R10`
- status: `bedrock_gate_global_product_boundary_lock_ready`
- decision: `pass`
- bedrock_gate_role: `global_product_boundary`
- separates_lab_from_product: `True`
- product_promotion_requires_bedrock_verdict: `True`
- technical_pass_is_not_product_pass: `True`
- evidence_required: `True`
- decision_lock: [DECISION_LOCKS.md](DECISION_LOCKS.md)
- bedrock_gate_contract: [BEDROCK_GATE.md](BEDROCK_GATE.md)
- next_recommended_phase: `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`

This lock is the active boundary for product promotion decisions.
It sits above the historical low-risk candidate review trail below and prevents product promotion from being inferred from technical pass alone.

## Bedrock v2 low-risk candidate source verification
- latest_completed_phase: `F21-CTX-BEDROCK-R10 - Bedrock v2 Low-Risk Candidate Source Verification Gate`
- next_recommended_phase: `F21-CTX-BEDROCK-R11 - Bedrock v2 Low-Risk Candidate Context Policy Review Gate`
- next_gate_seen: `F21-CTX-BEDROCK-R11 - Bedrock v2 Low-Risk Candidate Context Policy Review Gate`
- source_r9_decision_path: `artifacts/f21/bedrock_v2_safe_candidate_review_sequencing_decision.json`
- source_r8_decision_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_review_decision.json`
- source_risk_register_path: `artifacts/f21/bedrock_v2_adoption_candidate_risk_register.json`
- r9_status: `bedrock_v2_safe_candidate_review_sequencing_passed`
- r9_decision: `pass`
- r9_verified: `True`
- r8_status: `bedrock_v2_adoption_candidate_risk_review_passed`
- r8_decision: `pass`
- r8_verified: `True`
- source_verification_matrix_created: `True`
- source_verification_hash: `eefef9503bf2688b2dc57e9130c68e39aab8d7588d817ac7e6d22bf2708fb44e`
- total_low_risk_candidates_reviewed: `15`
- verified_low_risk_candidate_count: `15`
- source_verified_for_future_review_count: `15`
- source_verification_warn_count: `0`
- source_verification_blocked_count: `0`
- candidate_adoption_allowed_now: `False`
- candidate_approval_allowed_now: `False`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

R10 keeps low-risk source verification review-only; it does not approve or adopt candidates.

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
