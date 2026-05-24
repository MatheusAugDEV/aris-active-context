## BEDROCK_EVALUATION_INPUT_CONTRACT_DRAFT

- lock_id: `BEDROCK_EVALUATION_INPUT_CONTRACT_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R16`
- status: `bedrock_evaluation_input_contract_draft_ready`
- decision: `pass`
- draft_only: `True`
- evaluation_input_contract_created: `True`
- accepted_target_types_defined: `True`
- requested_verdict_scope_enum_defined: `True`
- input_rejection_rules_defined: `True`
- input_status_enum_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R17 - Bedrock Evaluation Request Validation Rules Draft`

Bedrock Evaluation Input Contract is policy only.
It defines the minimum valid request that a future Bedrock evaluation may accept, but it does not evaluate evidence, compute a verdict, or authorize product promotion.

## L-BEDROCK-V2-RESEARCH-PARKING
- lock_id: `L-BEDROCK-V2-RESEARCH-PARKING`
- bedrock_v2_required: `True`
- bedrock_v2_research_pending: `True`
- bedrock_v2_apply_allowed_now: `False`
- bedrock_v2_apply_deferred: `True`
- bedrock_v2_apply_plan_deferred_until_research: `True`
- bedrock_v2_diagnostic_preserved: `True`
- batch2_resume_allowed: `True`
- normal_batch2_flow_restored: `True`
- bedrock_gate_modification_allowed_now: `False`
- north_pole_modification_allowed_now: `False`
- phase_specific_gates_modification_allowed_now: `False`

D14 supersedes the immediate Bedrock v2 apply-plan route. Research must complete before Bedrock v2 apply planning resumes.

## L-BEDROCK-V2-DIAGNOSTIC-NO-APPLY
- lock_id: `L-BEDROCK-V2-DIAGNOSTIC-NO-APPLY`
- bedrock_v2_diagnostic_completed: `True`
- bedrock_v2_required: `True`
- bedrock_v2_apply_allowed_now: `False`
- bedrock_v2_apply_plan_required_next: `True`
- diagnostic_does_not_modify_bedrock_gate: `True`
- applies_to_active_context_governance: `True`
- f21_a61_status: `blocked`
- f21b_paused_track: `preserved`

D13 diagnostic evidence does not authorize automatic Bedrock v2 apply.

## L-NO-WARN-ADVANCEMENT — No-Warn Advancement Policy
- warn_advancement_allowed: `False`
- pass_required_for_next_gate: `True`
- warn_requires_repair_or_rework: `True`
- warn_cannot_close_phase: `True`
- warn_cannot_release_runtime_or_next_functional_gate: `True`
- applies_to_future_phases: `True`
- applies_to_active_context_governance: `True`
- retroactive_history_rewrite_allowed: `False`
- historical_warn_entries_preserved_as_history: `True`
# DECISION_LOCKS

# BEDROCK_EVALUATION_INPUT_CONTRACT_DRAFT

- lock_id: `BEDROCK_EVALUATION_INPUT_CONTRACT_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R16`
- status: `bedrock_evaluation_input_contract_draft_ready`
- decision: `pass`
- draft_only: `True`
- evaluation_input_contract_created: `True`
- accepted_target_types_defined: `True`
- requested_verdict_scope_enum_defined: `True`
- input_rejection_rules_defined: `True`
- input_status_enum_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R17 - Bedrock Evaluation Request Validation Rules Draft`

Bedrock Evaluation Input Contract is policy only.
It defines the minimum valid request that a future Bedrock evaluation may accept, but it does not evaluate evidence, compute a verdict, or authorize product promotion.

# BEDROCK_VERDICT_ARTIFACT_SCHEMA_DRAFT

- lock_id: `BEDROCK_VERDICT_ARTIFACT_SCHEMA_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R15`
- status: `bedrock_verdict_artifact_schema_draft_ready`
- decision: `pass`
- draft_only: `True`
- verdict_artifact_schema_created: `True`
- technical_status_separated_from_product_status: `True`
- completeness_gate_integration_defined: `True`
- blocker_scan_integration_defined: `True`
- llm_as_sole_judge_forbidden: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R16 - Bedrock Evaluation Input Contract Draft`

Bedrock Verdict Artifact is policy only.
It defines the final canonical output of a future Bedrock judgment and records how technical and product outcomes remain separated, but it does not execute a verdict.

# BEDROCK_BLOCKER_SCAN_SCHEMA_DRAFT

- lock_id: `BEDROCK_BLOCKER_SCAN_SCHEMA_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R14`
- status: `bedrock_blocker_scan_schema_draft_ready`
- decision: `pass`
- draft_only: `True`
- blocker_scan_schema_created: `True`
- canonical_blocker_count: `14`
- blocker_state_enum_defined: `True`
- blocker_severity_enum_defined: `True`
- evidence_quality_enum_defined: `True`
- waiver_policy_defined: `True`
- completeness_gate_integration_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R15 - Bedrock Verdict Artifact Schema Draft`

Bedrock Blocker Scan is policy only.
It defines how absolute blockers are represented, audited, waived, and fed into completeness and promotion blocking, but it does not execute a scanner runtime.

# BEDROCK_EVIDENCE_BUNDLE_COMPLETENESS_GATE_DRAFT

- lock_id: `BEDROCK_EVIDENCE_BUNDLE_COMPLETENESS_GATE_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R13`
- status: `bedrock_evidence_bundle_completeness_gate_draft_ready`
- decision: `pass`
- draft_only: `True`
- completeness_gate_draft_created: `True`
- required_evidence_matrix_defined: `True`
- minimum_validation_rule_defined: `True`
- minimum_validation_count: `5`
- blocker_handling_defined: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R14 - Bedrock Blocker Scan Schema Draft`

Bedrock Evidence Bundle Completeness Gate is policy only.
It defines when an evidence bundle is complete enough for product-grade judgment, but it does not execute the Bedrock runtime gate, promote product, or relax the R10 global boundary.

# BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY

- lock_id: `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`
- phase_id: `F21-CTX-BEDROCK-R10`
- status: `bedrock_gate_global_product_boundary_lock_ready`
- decision: `pass`
- bedrock_gate_role: `global_product_boundary`
- is_global_product_boundary: `True`
- separates_lab_from_product: `True`
- market_differentiator: `safety_predictability_auditability_rollback_maturity_trust`
- product_promotion_requires_bedrock_verdict: `True`
- technical_pass_is_not_product_pass: `True`
- evidence_required: `True`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R11 - Bedrock Verdict Criteria Draft`

Bedrock Gate is the mandatory global boundary between ARIS Lab / experimental / internal readiness and ARIS Produto / commercial-grade / user-facing readiness.
It must materialize evidence before any product promotion, and it may block a technically passing phase if the phase is not product-ready.
This lock wins over local phase summaries, stale memory, and subjective interpretation.

## BEDROCK_EVIDENCE_BUNDLE_SCHEMA_DRAFT

- lock_id: `BEDROCK_EVIDENCE_BUNDLE_SCHEMA_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R12`
- status: `bedrock_evidence_bundle_schema_draft_ready`
- decision: `pass`
- draft_only: `True`
- evidence_bundle_schema_created: `True`
- minimum_validation_classes_defined: `True`
- minimum_validation_count: `5`
- bundle_completeness_states_defined: `True`
- blocker_scan_schema_defined: `True`
- future_bundle_paths_proposed: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R13 - Bedrock Evidence Bundle Completeness Gate Draft`

Bedrock Evidence Bundle Schema is policy only.
It defines the minimum material evidence package required for a future Bedrock verdict, including identity, technical artifacts, validation, security, rollback, source-of-truth, completeness, and blocker scan sections.
It does not authorize product promotion or runtime execution.

## BEDROCK_VERDICT_CRITERIA_DRAFT

- lock_id: `BEDROCK_VERDICT_CRITERIA_DRAFT`
- phase_id: `F21-CTX-BEDROCK-R11`
- status: `bedrock_verdict_criteria_draft_ready`
- decision: `pass`
- draft_only: `True`
- criteria_draft_created: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- product_promotion_executed: `False`
- bedrock_runtime_gate_executed: `False`
- runtime_modified: `False`
- frontend_modified: `False`
- backend_modified: `False`
- action_runtime_modified: `False`
- voice_modified: `False`
- network_enabled: `False`
- dependencies_installed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_recommended_phase: `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`

Bedrock verdict criteria are defined as draft policy only.
This lock records the taxonomy, blocker rules, evidence minima, and future schema shape without executing any Bedrock runtime gate.
It does not authorize product promotion, runtime mutation, or commercial use.

## F21-A60 — ARIS Lean Development Protocol v0.1 Prompt Kernel Minimal Contract Implementation Readiness Gate
- latest_completed_phase: `F21-A60 — ARIS Lean Development Protocol v0.1 Prompt Kernel Minimal Contract Implementation Readiness Gate`
- status: `prompt_kernel_minimal_contract_implementation_readiness_warn`
- decision: `warn`
- reviewed_phase_id: `F21-A59`
- prompt_kernel_implementation_plan_created: `True`
- minimal_contract_implementation_readiness_reviewed: `True`
- minimal_contract_implementation_readiness_passed: `True`
- minimal_contract_implementation_readiness_score: `1.0`
- prompt_kernel_real_implementation_created: `False`
- prompt_kernel_class_created: `False`
- prompt_kernel_runtime_integration_allowed: `False`
- prompt_kernel_implementation_allowed_now: `False`
- prompt_kernel_implementation_allowed_next: `False`
- controlled_contract_implementation_allowed_next: `True`
- prompt_kernel_contracts_planned: `True`
- prompt_kernel_future_module_boundary_defined: `True`
- prompt_kernel_future_contract_objects_defined: `True`
- prompt_kernel_future_deterministic_functions_defined: `True`
- future_test_plan_ready: `True`
- future_artifact_plan_ready: `True`
- future_rollback_plan_ready: `True`
- source_precedence_contract_defined: `True`
- source_exclusion_contract_defined: `True`
- traceability_hash_plan_defined: `True`
- false_authorization_prevention_defined: `True`
- external_reference_huw_fury_catalogued: `True`
- external_reference_huw_fury_used_as_authorization: `False`
- external_reference_huw_fury_changes_sequence_now: `False`
- external_reference_huw_fury_status: `catalogued_external_reference`
- external_reference_huw_fury_source_rank: `reference_only_non_authoritative`
- external_reference_huw_fury_may_inform_future_design: `True`
- model_reasoning_policy_available: `True`
- default_model: `5.4 mini`
- default_reasoning_level: `baixo`
- recommended_model_for_phase: `5.4 normal`
- recommended_reasoning_level_for_phase: `alto`
- policy_is_advisory_not_authorization: `True`
- policy_does_not_authorize_runtime_or_implementation: `True`
- roadmap_direct_insert_allowed_now: `False`
- phase_sequence_change_allowed_now: `False`
- decision_gate_required_before_use: `True`
- root_worktree_dirty_unrelated: `True`
- root_worktree_dirty_blocks_prompt_kernel_minimal_contract_readiness: `False`
- template_library_allowed: `False`
- batch_runner_allowed: `False`
- mcp_activation_allowed: `False`
- mcp_config_write_allowed: `False`
- vault_write_allowed: `False`
- obsidian_bulk_read_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_real_action: `F21-A61 — ARIS Lean Development Protocol v0.1 Prompt Kernel Minimal Contract Controlled Implementation Gate`

This lock records the readiness gate only. It authorizes only the next controlled contract-only implementation gate and does not authorize runtime integration.

## Model / Reasoning Policy Lock

- policy_file: `MODEL_REASONING_POLICY.md`
- default_model: `5.4 mini`
- default_reasoning_level: `baixo`
- active_context_touch_default: `5.4 normal / alto`
- critical_recovery_security_roadmap_default: `5.5 / altissimo`
- escalation_required_when_phase_risk_increases: `true`
- policy_is_advisory_not_authorization: `true`

Future ARIS prompts must state the recommended model and reasoning level. `5.4 mini` remains the default, but tasks involving active-context, gates, locks, ledger, parser/gate logic, roadmap, security, Prompt Kernel, Memory Kernel, Action Runtime, Voice Runtime, external reference integration, or recovery from partial execution must be escalated according to `MODEL_REASONING_POLICY.md`.

This policy does not authorize implementation, runtime mutation, MCP, network, dependency installation, product promotion, customer real use, or production release.

## External Reference Locks — Huw Prosser / Fury SDK corpus

- external_reference_id: `ext_ref_huw_prosser_fury_2026_05`
- status: `catalogued_external_reference`
- implementation_allowed_now: `false`
- roadmap_direct_insert_allowed_now: `false`
- phase_sequence_change_allowed_now: `false`
- source_of_truth_rank: `reference_only_non_authoritative`

### L-EXTREF
External references do not authorize implementation, runtime mutation, roadmap sequence changes, product promotion, customer real use, or production release.

### L-PATTERN-FURY
Fury/Huw patterns cannot bypass `BEDROCK_GATE.md`, `NORTH_POLE.md`, phase-specific gates, permission gates, ledger, rollback, sidecar execution, active-context precedence, or source-of-truth policy.

### L-BASH-FS
Direct bash/filesystem tools are rejected as LLM tools. They may only be reconsidered through a future sidecar design with permission gate, ledger, rollback/compensation, path jail, deterministic tests, and explicit capability binding.

### L-MEMORY-PROVENANCE
Durable memory requires provenance, validity window, scope binding, revocation, audit trail, privacy policy, and source-of-truth precedence before implementation.

### L-SKILL-REGISTRY
External skills require a signed registry, hash pinning, explicit capability declaration, human/security review, and promotion gate before use.

### L-SYSTEM-PROMPT-BOUNDARY
Raw project-file injection into system prompts is rejected. Master/system/persona content must never be prefixed into user content.

### L-PARALLEL-TOOLS
Parallel tool execution remains blocked until deterministic scheduling, capability binding, plan-hash binding, and rollback/compensation are proven.

### L-VOICE-CLONING
Voice cloning remains deferred until anti-impersonation gates and audio retention/privacy policy exist.

### L-LICENSE-REUSE
External code reuse is blocked until license compatibility, source review, security review, and explicit adoption gate are completed.

## Recent immutable antecedents
- `F21-A58`: prompt kernel implementation planning created a contract-only future boundary and catalogued Huw/Fury as reference-only.
- `F21-A57`: prompt kernel plan review accepted the plan with warnings only.
- `F21-A56`: prompt kernel planning created a bounded plan and kept implementation blocked.
- `F21-A55`: post-sync closure reconciled the commit divergence and kept unrelated root dirtiness visible.
- `F21-A54C`: remote sync verification confirmed both `origin/main` refs matched local HEAD.
- `F21-A54B`: active-context hygiene repair removed stale duplicate blocks.
- `F21-A60`: prompt kernel contract readiness accepted the next controlled contract-only gate and kept runtime/template/batch blocked.
