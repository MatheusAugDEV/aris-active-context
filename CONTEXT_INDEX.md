## ARIS-CONTEXT-P10 — Context Compression Candidate Validation Harness
when_to_use: Validate ordered compression candidates and risk boundaries without rewriting live files.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_compression_candidate_validation_harness_report.md
- artifacts/context/context_compression_candidate_matrix.json
- artifacts/context/context_compression_candidate_order.json
- artifacts/context/context_compression_risk_register.json
notes:
- validation only; no compression or routing is introduced
- next recommended phase: `ARIS-CONTEXT-P11 — Artifact Reference-Only Compression Plan`
## ARIS-CONTEXT-P9 — Context Compression Candidate Plan
when_to_use: Review the ordered compression candidates and estimated reductions without rewriting live context files.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_compression_candidate_plan_report.md
- artifacts/context/context_compression_candidate_matrix.json
- artifacts/context/context_compression_candidate_order.json
- artifacts/context/context_compression_risk_register.json
notes:
- plan only; no compression or routing is introduced
- next recommended phase: `ARIS-CONTEXT-P10 — Context Compression Candidate Validation Harness`
## ARIS-CONTEXT-P8 — Context Budget Policy Validation Harness
- status: `context_budget_policy_validation_harness_warn`
- budget policy validation harness created: `True`
- policy status: `draft_only`
- enforcement enabled: `False`
- warning only: `True`
- hard blocks enabled: `False`
- context routing enabled: `False`
- hot path current approx tokens: `20223`
- hot path target tokens: `6000`
- hot path warn tokens: `8000`
- hot path hard ceiling tokens: `12000`
- next phase recommendation: `ARIS-CONTEXT-P9 — Context Compression Candidate Plan`

This phase validates the draft budget policy only; it does not enable enforcement, routing, or prompt behavior changes.

## ARIS-CONTEXT-P7 — Context Budget Policy Draft
when_to_use: Review the draft budget policy, per-set budgets, and file recommendations without enabling enforcement.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_budget_policy_draft.json
- artifacts/context/context_budget_policy_draft_summary.json
- artifacts/context/context_budget_policy_context_set_budgets.json
- artifacts/context/context_budget_policy_file_recommendations.json
notes:
- warning-only draft; no enforcement or routing is introduced
- next recommended phase: `ARIS-CONTEXT-P8 — Context Budget Policy Validation Harness`
## ARIS-CONTEXT-P6 — Context Manifest Validation Harness
when_to_use: Validate the draft context manifest and its context sets without activating routing or frontmatter.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_manifest_draft.json
- artifacts/context/context_manifest_draft_schema.json
- artifacts/context/context_manifest_context_sets.json
- artifacts/context/context_manifest_validation_result.json
notes:
- validation only; no routing or frontmatter application is introduced
- next recommended phase: `ARIS-CONTEXT-P7 — Context Budget Policy Draft`
## ARIS-CONTEXT-P6 — Context Manifest Validation Harness
when_to_use: Validate the draft context manifest and its context sets without activating routing or frontmatter.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_manifest_draft.json
- artifacts/context/context_manifest_draft_schema.json
- artifacts/context/context_manifest_context_sets.json
- artifacts/context/context_manifest_validation_result.json
notes:
- validation only; no routing or frontmatter application is introduced
- next recommended phase: `Repair missing or invalid P5 manifest inputs and rerun P6`
## ARIS-CONTEXT-P5 — Context Manifest Draft
when_to_use: Use to inspect draft context sets, compare artifact references, and review the manifest draft without changing runtime behavior.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_manifest_draft.json
- artifacts/context/context_manifest_draft_schema.json
- artifacts/context/context_manifest_context_sets.json
- artifacts/context/context_manifest_validation_result.json
notes:
- draft only; no routing or frontmatter application is introduced
- next recommended phase: `ARIS-CONTEXT-P6 — Context Manifest Validation Harness`
## ARIS-CONTEXT-P4 — Active Context Frontmatter Validation Harness
when_to_use: Use to validate the draft frontmatter contract and synthetic fixtures before any apply gate.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/active_context_frontmatter_validation_harness_decision.json
- artifacts/context/active_context_frontmatter_validation_harness_summary.json
- artifacts/context/active_context_frontmatter_validation_results.json
- artifacts/context/active_context_frontmatter_validation_samples.json
- docs/research/active_context_frontmatter_validation_harness.md
notes:
- validation only; no live frontmatter is applied
- next recommended phase: `ARIS-CONTEXT-P5 — Context Manifest Draft`
## ARIS-CONTEXT-P3 — Active Context Frontmatter Contract Draft
when_to_use: Use to review the draft frontmatter contract and file classification matrix before any apply harness.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/active_context_frontmatter_contract_draft_decision.json
- artifacts/context/active_context_frontmatter_contract_draft_summary.json
- artifacts/context/active_context_frontmatter_contract_schema.json
- artifacts/context/active_context_frontmatter_classification_matrix.json
- docs/research/active_context_frontmatter_contract_draft.md
notes:
- draft only; no live frontmatter is applied
- next recommended phase: `ARIS-CONTEXT-P4 — Active Context Frontmatter Validation Harness`
## ARIS-CONTEXT-P2 — Context OS Token Economy Baseline Diagnostic
when_to_use: Use to measure current context file size, classify hot/warm/cold/artifact recommendations, and establish a deterministic baseline without changing behavior.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
- artifacts/context/context_os_token_economy_baseline_diagnostic_decision.json
- artifacts/context/context_os_token_economy_baseline_diagnostic_summary.json
- artifacts/context/context_os_token_economy_baseline_file_metrics.json
notes:
- diagnostic only; no frontmatter, manifest, or budget enforcement is introduced
- next recommended phase: `ARIS-CONTEXT-P3 — Active Context Frontmatter Contract Draft`

## ARIS-CONTEXT-P1 — BOOT.md Read-First Entry Point Contract
when_to_use: Use BOOT.md first as the lightweight entry point, then continue into active-context for authoritative state.
read_first:
- BOOT.md
- aris-active-context/CURRENT_STATE.md
- aris-active-context/NEXT_ACTION.md
- aris-active-context/DECISION_LOCKS.md
- aris-active-context/CONTEXT_INDEX.md
- aris-active-context/ARIS_PHASE_LEDGER.md
notes:
- BOOT.md is an entry point only and never outranks active-context or artifacts.
- advisory research remains advisory-only.
- next recommended phase: `ARIS-CONTEXT-P2 — Context OS Token Economy Baseline Diagnostic`
# CONTEXT_INDEX

## ARIS-CONTEXT-P0 — External Context Economy Research Ingestion & Claim Matrix
when_to_use: Use to review the advisory-only context-economy research intake and claim matrix without authorizing implementation.
read_first:
- CURRENT_STATE.md
- NEXT_ACTION.md
- DECISION_LOCKS.md
- CONTEXT_INDEX.md
- ARIS_PHASE_LEDGER.md
- artifacts/context/context_economy_research_ingestion_decision.json
- artifacts/context/context_economy_research_ingestion_summary.json
- artifacts/context/context_economy_claim_matrix.json
- artifacts/context/context_economy_research_ingestion_report.md
- docs/research/context_economy_research_ingestion.md
- docs/research/context_economy_external_research_intake.md
notes:
- advisory-only research does not change authoritative runtime state
- active-context sync is still recommended before P1 in this workspace

## ARIS-ROADMAP-R0 Governance Foundation
when_to_use: Use to establish the auditable governance foundation before C7 and any later Lab or roadmap continuation.
read_first:
- ARIS_ROADMAP_R0_F120.md
- artifacts/roadmap/r0_governance_foundation_decision.json
- artifacts/roadmap/r0_governance_foundation_summary.json
- artifacts/roadmap/r0_governance_foundation_report.md
- artifacts/roadmap/roadmap_machine_validation_report.json
- docs/roadmap/aris_roadmap_r0_governance_foundation.md
notes:
- active-context outranks memory, chat, history, and summaries.
- NEXT_ACTION governs the next operational step.
- DECISION_LOCKS governs hard restrictions.
- next recommended phase: `ARIS-BEDROCK-C7 — Evidence Pack Completeness Evaluator`

Current Bedrock note:

- Official V6 is closed and the ARIS Lab authority layer is now active after reconciliation.
- F33.Z22 remains preserved as the latest closed F33 operational phase.
- Latest completed phase: `ARIS-BEDROCK-C6 — Read-First & Source-of-Truth Compliance Evaluator`
- C6 created the Read-First & Source-of-Truth Compliance Evaluator, read-first contract, source-of-truth contract, and valid/invalid compliance examples.
- Next principal phase: `ARIS-BEDROCK-C7 — Evidence Pack Completeness Evaluator`
- C6 kept the Bedrock engine unimplemented and non-executable.
- Bedrock executable engine readiness: `45/100`
- Bedrock Gate remains declared but non-executable.
- B7 -> B8 -> B9 -> B10 -> B11 -> B12 -> B13 -> B14 -> B15 -> B16 -> B17 -> B18 -> B19 remains review-only and non-authorizing.
- The Lab governance score is recorded at 100/100 and the governance plan is closed for the Lab track.
- F33.RM-F51-P0/R1 remains external advisory research only and does not authorize product promotion or override the Lab contract.
- Historical irregularities were found in older LAB_VERDICTS sections and treated as warning only.
- F44 interpretation: `hardening/maturity of existing Lab`

Current Bedrock note:

- Official V6 is closed and the ARIS Lab authority layer is now active after reconciliation.
- F33.Z22 remains preserved as the latest closed F33 operational phase.
- Latest completed phase: `ARIS-BEDROCK-C5 — Completion Doctrine Evaluator`
- C5 created the Completion Doctrine Evaluator and validated completion safety deterministically.
- Next principal phase: `ARIS-BEDROCK-C6 — Read-First & Source-of-Truth Compliance Evaluator`
- C5 kept the Bedrock engine unimplemented and non-executable.
- Bedrock executable engine readiness: `40/100`
- Bedrock Gate remains declared but non-executable.
- B7 -> B8 -> B9 -> B10 -> B11 -> B12 -> B13 -> B14 -> B15 -> B16 -> B17 -> B18 -> B19 remains review-only and non-authorizing.
- The Lab governance score is recorded at 100/100 and the governance plan is closed for the Lab track.
- F33.RM-F51-P0/R1 remains external advisory research only and does not authorize product promotion or override the Lab contract.
- Historical irregularities were found in older LAB_VERDICTS sections and treated as warning only.
- F44 interpretation: `hardening/maturity of existing Lab`

- Latest completed phase: `ARIS-BEDROCK-C4 — Dangerous Flags Evaluator`
- Next principal phase: `ARIS-BEDROCK-C5 — Completion Doctrine Evaluator`
- Lab governance remains 100/100 and Bedrock execution remains non-executable.

- Latest completed phase: `ARIS-BEDROCK-C3 — Decision/Summary Schema Validator`
- Next principal phase: `ARIS-BEDROCK-C4 — Dangerous Flags Evaluator`
- Lab governance remains 100/100 and Bedrock execution remains non-executable.

- Latest completed phase: `ARIS-BEDROCK-C2 — Artifact Loader & Hash Manifest`
- Next principal phase: `ARIS-BEDROCK-C3 — Decision/Summary Schema Validator`
- Lab governance remains 100/100 and Bedrock execution remains non-executable.

## Recent ARIS-LAB B19 review references

- [docs/aris_lab/aris_lab_b19_bedrock_decisions_contract_schema_consolidation_readiness_review_gate.md](../docs/aris_lab/aris_lab_b19_bedrock_decisions_contract_schema_consolidation_readiness_review_gate.md)
- [artifacts/aris_lab/aris_lab_b19_decision.json](../artifacts/aris_lab/aris_lab_b19_decision.json)
- [artifacts/aris_lab/aris_lab_b19_summary.json](../artifacts/aris_lab/aris_lab_b19_summary.json)
- [artifacts/aris_lab/aris_lab_b19_report.md](../artifacts/aris_lab/aris_lab_b19_report.md)
- [artifacts/aris_lab/aris_lab_b19_b18_readiness_review_matrix.json](../artifacts/aris_lab/aris_lab_b19_b18_readiness_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b19_chain_readiness_review_record.json](../artifacts/aris_lab/aris_lab_b19_chain_readiness_review_record.json)
- [artifacts/aris_lab/aris_lab_b19_chain_textual_drift_readiness_review.json](../artifacts/aris_lab/aris_lab_b19_chain_textual_drift_readiness_review.json)
- [artifacts/aris_lab/aris_lab_b19_phase_narrative_rule_readiness_review.json](../artifacts/aris_lab/aris_lab_b19_phase_narrative_rule_readiness_review.json)
- [artifacts/aris_lab/aris_lab_b19_non_authorization_readiness_review_matrix.json](../artifacts/aris_lab/aris_lab_b19_non_authorization_readiness_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b19_evidence_link_readiness_review_matrix.json](../artifacts/aris_lab/aris_lab_b19_evidence_link_readiness_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b19_historical_warning_readiness_review.json](../artifacts/aris_lab/aris_lab_b19_historical_warning_readiness_review.json)
- [artifacts/aris_lab/aris_lab_b19_drift_check.json](../artifacts/aris_lab/aris_lab_b19_drift_check.json)
- [artifacts/aris_lab/aris_lab_b19_safety_attestation.json](../artifacts/aris_lab/aris_lab_b19_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b19_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b19_next_phase_contract.json)

## Recent ARIS-LAB B17 review references

- [docs/aris_lab/aris_lab_b16_bedrock_decisions_contract_schema_consolidation_readiness_gate.md](../docs/aris_lab/aris_lab_b16_bedrock_decisions_contract_schema_consolidation_readiness_gate.md)
- [artifacts/aris_lab/aris_lab_b17_decision.json](../artifacts/aris_lab/aris_lab_b17_decision.json)
- [artifacts/aris_lab/aris_lab_b17_summary.json](../artifacts/aris_lab/aris_lab_b17_summary.json)
- [artifacts/aris_lab/aris_lab_b17_report.md](../artifacts/aris_lab/aris_lab_b17_report.md)
- [artifacts/aris_lab/aris_lab_b17_b16_readiness_review_closure_matrix.json](../artifacts/aris_lab/aris_lab_b17_b16_readiness_review_closure_matrix.json)
- [artifacts/aris_lab/aris_lab_b17_phase_narrative_rule_closure_review.json](../artifacts/aris_lab/aris_lab_b17_phase_narrative_rule_closure_review.json)
- [artifacts/aris_lab/aris_lab_b17_chain_readiness_closure_record.json](../artifacts/aris_lab/aris_lab_b17_chain_readiness_closure_record.json)
- [artifacts/aris_lab/aris_lab_b17_non_authorization_closure_matrix.json](../artifacts/aris_lab/aris_lab_b17_non_authorization_closure_matrix.json)
- [artifacts/aris_lab/aris_lab_b17_evidence_link_closure_matrix.json](../artifacts/aris_lab/aris_lab_b17_evidence_link_closure_matrix.json)
- [artifacts/aris_lab/aris_lab_b17_historical_warning_closure_review.json](../artifacts/aris_lab/aris_lab_b17_historical_warning_closure_review.json)
- [artifacts/aris_lab/aris_lab_b17_drift_check.json](../artifacts/aris_lab/aris_lab_b17_drift_check.json)
- [artifacts/aris_lab/aris_lab_b17_safety_attestation.json](../artifacts/aris_lab/aris_lab_b17_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b17_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b17_next_phase_contract.json)

## Recent ARIS-LAB B16 review references

- [docs/aris_lab/aris_lab_b16_bedrock_decisions_contract_schema_consolidation_readiness_gate.md](../docs/aris_lab/aris_lab_b16_bedrock_decisions_contract_schema_consolidation_readiness_gate.md)
- [artifacts/aris_lab/aris_lab_b16_decision.json](../artifacts/aris_lab/aris_lab_b16_decision.json)
- [artifacts/aris_lab/aris_lab_b16_summary.json](../artifacts/aris_lab/aris_lab_b16_summary.json)
- [artifacts/aris_lab/aris_lab_b16_report.md](../artifacts/aris_lab/aris_lab_b16_report.md)
- [artifacts/aris_lab/aris_lab_b16_b15_readiness_review_matrix.json](../artifacts/aris_lab/aris_lab_b16_b15_readiness_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b16_phase_narrative_rule_readiness.json](../artifacts/aris_lab/aris_lab_b16_phase_narrative_rule_readiness.json)
- [artifacts/aris_lab/aris_lab_b16_chain_readiness_record.json](../artifacts/aris_lab/aris_lab_b16_chain_readiness_record.json)
- [artifacts/aris_lab/aris_lab_b16_non_authorization_readiness_matrix.json](../artifacts/aris_lab/aris_lab_b16_non_authorization_readiness_matrix.json)
- [artifacts/aris_lab/aris_lab_b16_evidence_link_readiness_matrix.json](../artifacts/aris_lab/aris_lab_b16_evidence_link_readiness_matrix.json)
- [artifacts/aris_lab/aris_lab_b16_historical_warning_readiness.json](../artifacts/aris_lab/aris_lab_b16_historical_warning_readiness.json)
- [artifacts/aris_lab/aris_lab_b16_drift_check.json](../artifacts/aris_lab/aris_lab_b16_drift_check.json)
- [artifacts/aris_lab/aris_lab_b16_safety_attestation.json](../artifacts/aris_lab/aris_lab_b16_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b16_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b16_next_phase_contract.json)

## Recent ARIS-LAB B15 review references

- [docs/aris_lab/aris_lab_b15_bedrock_decisions_contract_schema_consolidation_readiness_gate.md](../docs/aris_lab/aris_lab_b15_bedrock_decisions_contract_schema_consolidation_readiness_gate.md)
- [artifacts/aris_lab/aris_lab_b15_decision.json](../artifacts/aris_lab/aris_lab_b15_decision.json)
- [artifacts/aris_lab/aris_lab_b15_summary.json](../artifacts/aris_lab/aris_lab_b15_summary.json)
- [artifacts/aris_lab/aris_lab_b15_report.md](../artifacts/aris_lab/aris_lab_b15_report.md)
- [artifacts/aris_lab/aris_lab_b15_b14_readiness_review_matrix.json](../artifacts/aris_lab/aris_lab_b15_b14_readiness_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b15_phase_narrative_rule_readiness.json](../artifacts/aris_lab/aris_lab_b15_phase_narrative_rule_readiness.json)
- [artifacts/aris_lab/aris_lab_b15_chain_readiness_record.json](../artifacts/aris_lab/aris_lab_b15_chain_readiness_record.json)
- [artifacts/aris_lab/aris_lab_b15_non_authorization_readiness_matrix.json](../artifacts/aris_lab/aris_lab_b15_non_authorization_readiness_matrix.json)
- [artifacts/aris_lab/aris_lab_b15_evidence_link_readiness_matrix.json](../artifacts/aris_lab/aris_lab_b15_evidence_link_readiness_matrix.json)
- [artifacts/aris_lab/aris_lab_b15_historical_warning_readiness.json](../artifacts/aris_lab/aris_lab_b15_historical_warning_readiness.json)
- [artifacts/aris_lab/aris_lab_b15_drift_check.json](../artifacts/aris_lab/aris_lab_b15_drift_check.json)
- [artifacts/aris_lab/aris_lab_b15_safety_attestation.json](../artifacts/aris_lab/aris_lab_b15_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b15_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b15_next_phase_contract.json)

## Recent ARIS-LAB B14 review references

- [docs/aris_lab/aris_lab_b14_bedrock_decisions_contract_schema_consolidation_review_closure_gate.md](../docs/aris_lab/aris_lab_b14_bedrock_decisions_contract_schema_consolidation_review_closure_gate.md)
- [artifacts/aris_lab/aris_lab_b14_decision.json](../artifacts/aris_lab/aris_lab_b14_decision.json)
- [artifacts/aris_lab/aris_lab_b14_summary.json](../artifacts/aris_lab/aris_lab_b14_summary.json)
- [artifacts/aris_lab/aris_lab_b14_report.md](../artifacts/aris_lab/aris_lab_b14_report.md)
- [artifacts/aris_lab/aris_lab_b14_b13_closure_review_matrix.json](../artifacts/aris_lab/aris_lab_b14_b13_closure_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b14_chain_closure_record.json](../artifacts/aris_lab/aris_lab_b14_chain_closure_record.json)
- [artifacts/aris_lab/aris_lab_b14_artifact_closure_review_matrix.json](../artifacts/aris_lab/aris_lab_b14_artifact_closure_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b14_schema_contract_closure_review_matrix.json](../artifacts/aris_lab/aris_lab_b14_schema_contract_closure_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b14_non_authorization_closure_review_matrix.json](../artifacts/aris_lab/aris_lab_b14_non_authorization_closure_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b14_evidence_link_closure_review_matrix.json](../artifacts/aris_lab/aris_lab_b14_evidence_link_closure_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b14_historical_warning_closure_review.json](../artifacts/aris_lab/aris_lab_b14_historical_warning_closure_review.json)
- [artifacts/aris_lab/aris_lab_b14_phase_narrative_rule_record.json](../artifacts/aris_lab/aris_lab_b14_phase_narrative_rule_record.json)
- [artifacts/aris_lab/aris_lab_b14_prompt_contract_update_record.json](../artifacts/aris_lab/aris_lab_b14_prompt_contract_update_record.json)
- [artifacts/aris_lab/aris_lab_b14_drift_check.json](../artifacts/aris_lab/aris_lab_b14_drift_check.json)
- [artifacts/aris_lab/aris_lab_b14_safety_attestation.json](../artifacts/aris_lab/aris_lab_b14_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b14_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b14_next_phase_contract.json)

## Recent ARIS-LAB B13 review references

- [docs/aris_lab/aris_lab_b13_bedrock_decisions_contract_schema_consolidation_review_gate.md](../docs/aris_lab/aris_lab_b13_bedrock_decisions_contract_schema_consolidation_review_gate.md)
- [artifacts/aris_lab/aris_lab_b13_decision.json](../artifacts/aris_lab/aris_lab_b13_decision.json)
- [artifacts/aris_lab/aris_lab_b13_summary.json](../artifacts/aris_lab/aris_lab_b13_summary.json)
- [artifacts/aris_lab/aris_lab_b13_report.md](../artifacts/aris_lab/aris_lab_b13_report.md)
- [artifacts/aris_lab/aris_lab_b13_b12_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b13_b12_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b13_chain_consolidation_review_record.json](../artifacts/aris_lab/aris_lab_b13_chain_consolidation_review_record.json)
- [artifacts/aris_lab/aris_lab_b13_artifact_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b13_artifact_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b13_schema_contract_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b13_schema_contract_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b13_non_authorization_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b13_non_authorization_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b13_evidence_link_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b13_evidence_link_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b13_historical_warning_review.json](../artifacts/aris_lab/aris_lab_b13_historical_warning_review.json)
- [artifacts/aris_lab/aris_lab_b13_drift_check.json](../artifacts/aris_lab/aris_lab_b13_drift_check.json)
- [artifacts/aris_lab/aris_lab_b13_safety_attestation.json](../artifacts/aris_lab/aris_lab_b13_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b13_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b13_next_phase_contract.json)

## Recent ARIS-LAB B12 review references

- [docs/aris_lab/aris_lab_b12_bedrock_decisions_contract_schema_review_consolidation_gate.md](../docs/aris_lab/aris_lab_b12_bedrock_decisions_contract_schema_review_consolidation_gate.md)
- [artifacts/aris_lab/aris_lab_b12_decision.json](../artifacts/aris_lab/aris_lab_b12_decision.json)
- [artifacts/aris_lab/aris_lab_b12_summary.json](../artifacts/aris_lab/aris_lab_b12_summary.json)
- [artifacts/aris_lab/aris_lab_b12_report.md](../artifacts/aris_lab/aris_lab_b12_report.md)
- [artifacts/aris_lab/aris_lab_b12_b11_consolidation_review_matrix.json](../artifacts/aris_lab/aris_lab_b12_b11_consolidation_review_matrix.json)
- [artifacts/aris_lab/aris_lab_b12_chain_consolidation_record.json](../artifacts/aris_lab/aris_lab_b12_chain_consolidation_record.json)
- [artifacts/aris_lab/aris_lab_b12_artifact_consolidation_matrix.json](../artifacts/aris_lab/aris_lab_b12_artifact_consolidation_matrix.json)
- [artifacts/aris_lab/aris_lab_b12_schema_contract_consolidation_matrix.json](../artifacts/aris_lab/aris_lab_b12_schema_contract_consolidation_matrix.json)
- [artifacts/aris_lab/aris_lab_b12_non_authorization_consolidation_matrix.json](../artifacts/aris_lab/aris_lab_b12_non_authorization_consolidation_matrix.json)
- [artifacts/aris_lab/aris_lab_b12_evidence_link_consolidation_matrix.json](../artifacts/aris_lab/aris_lab_b12_evidence_link_consolidation_matrix.json)
- [artifacts/aris_lab/aris_lab_b12_historical_warning_consolidation.json](../artifacts/aris_lab/aris_lab_b12_historical_warning_consolidation.json)
- [artifacts/aris_lab/aris_lab_b12_drift_check.json](../artifacts/aris_lab/aris_lab_b12_drift_check.json)
- [artifacts/aris_lab/aris_lab_b12_safety_attestation.json](../artifacts/aris_lab/aris_lab_b12_safety_attestation.json)
- [artifacts/aris_lab/aris_lab_b12_next_phase_contract.json](../artifacts/aris_lab/aris_lab_b12_next_phase_contract.json)

## ARIS-CONTEXT-P0 — External Context Economy Research Ingestion & Claim Matrix
when_to_use: Use to review the advisory-only context-economy research intake and claim matrix without authorizing implementation.
read_first:
- CURRENT_STATE.md
- NEXT_ACTION.md
- DECISION_LOCKS.md
- CONTEXT_INDEX.md
- ARIS_PHASE_LEDGER.md
- artifacts/context/context_economy_research_ingestion_decision.json
- artifacts/context/context_economy_research_ingestion_summary.json
- artifacts/context/context_economy_claim_matrix.json
- artifacts/context/context_economy_research_ingestion_report.md
- docs/research/context_economy_research_ingestion.md
- docs/research/context_economy_external_research_intake.md
notes:
- advisory-only research does not change authoritative runtime state
- active-context sync is still recommended before P1 in this workspace

# CONTEXT_INDEX

## Current operational state

- Latest completed phase: `ARIS-BEDROCK-C6 — Read-First & Source-of-Truth Compliance Evaluator`.
- Canonical roadmap: `ARIS_ROADMAP_R0_F120.md`.
- Roadmap status: `PASS by conservative review`.
- Next authorized phase: `ARIS-ROADMAP-R0 — Governance Foundation`.
- `ARIS-BEDROCK-C7` is blocked until `R0 = PASS`.
- F33 remains paused.
- F51+ remains advisory-only.
- Bedrock Gate remains declared but non-executable.

## Read in this order

1. [CURRENT_STATE.md](CURRENT_STATE.md)
2. [NEXT_ACTION.md](NEXT_ACTION.md)
3. [DECISION_LOCKS.md](DECISION_LOCKS.md)
4. [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
5. [ARIS_ROADMAP_R0_F120.md](ARIS_ROADMAP_R0_F120.md)
6. [MANDATORY_READ_FIRST_RULES.md](MANDATORY_READ_FIRST_RULES.md)
7. [LAB_OPERATING_CONTRACT.md](LAB_OPERATING_CONTRACT.md)
8. [LAB_STATUS.md](LAB_STATUS.md)
9. [LAB_VERDICTS.md](LAB_VERDICTS.md)
10. [README.md](README.md)
11. [OPERATOR_PREFERENCES.md](OPERATOR_PREFERENCES.md)
12. [PROMPT_CONTRACT.md](PROMPT_CONTRACT.md)

## Roadmap source-of-truth

- Active canonical roadmap: [ARIS_ROADMAP_R0_F120.md](ARIS_ROADMAP_R0_F120.md)
- Superseded roadmap: [ROADMAP_CANONICAL_F33_F50.md](ROADMAP_CANONICAL_F33_F50.md)
- Tombstone-only roadmap: [ROADMAP_F30_F50.md](ROADMAP_F30_F50.md)
- Historical archive roadmap material remains in `archive/` and is not the default read path.

## Current Lab / Bedrock priority references

- [MANDATORY_READ_FIRST_RULES.md](MANDATORY_READ_FIRST_RULES.md)
- [LAB_OPERATING_CONTRACT.md](LAB_OPERATING_CONTRACT.md)
- [LAB_STATUS.md](LAB_STATUS.md)
- [LAB_VERDICTS.md](LAB_VERDICTS.md)
- [PROMPT_CONTRACT.md](PROMPT_CONTRACT.md)

## Non-authorization summary

Product promotion remains false. Runtime mutation, SQLite schema apply, SQLite connect, FTS5 creation, network, dependency install, MCP activation, Obsidian bulk-read, and Vault write remain blocked.
