## F21-A6 — Obsidian MCP Human Evidence Intake
- status: `obsidian_mcp_human_evidence_intake_warn`
- decision: `warn`
- human_evidence_present: `False`
- human_evidence_classification: `missing`
- human_evidence_hash: `sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- human_decision_kind: `PENDING`
- evidence_schema_defined: `True`
- required_fields_defined: `True`
- forbidden_fields_defined: `True`
- redaction_policy_defined: `True`
- template_created: `True`
- f21_a5_warning_reconciled: `True`
- f21_a5_warning_count_snapshot_mismatch: `True`
- blocker_count: `0`
- warning_count: `3`
- next_recommended_phase: `F21-A7 — MCP Candidate Evidence Review Gate`

Human evidence intake is review-only and does not authorize MCP activation.
## F21-A6 — Obsidian MCP Human Evidence Intake
- status: `obsidian_mcp_human_evidence_intake_blocked`
- decision: `blocked`
- human_evidence_present: `True`
- human_evidence_classification: `rejected_sensitive_or_unsafe`
- human_evidence_hash: `sha256:19bb985d2f2fe2a9a32e45cf59e7a1b0615cefa1bbd117dc1f34d657e88647d8`
- human_decision_kind: `PENDING`
- evidence_schema_defined: `True`
- required_fields_defined: `True`
- forbidden_fields_defined: `True`
- redaction_policy_defined: `True`
- template_created: `True`
- f21_a5_warning_reconciled: `True`
- f21_a5_warning_count_snapshot_mismatch: `True`
- blocker_count: `2`
- warning_count: `2`
- next_recommended_phase: `F21-A7 — MCP Candidate Evidence Review Gate`

Human evidence intake is review-only and does not authorize MCP activation.
## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_warn`
- decision: `warn`
- phase_id: `F21-A5`
- macroblock_id: `MB1`
- source_of_truth_precedence_defined: `True`
- hard_locks_ranked_first: `True`
- next_action_ranked_operational_first: `True`
- current_state_ranked_live_state: `True`
- phase_artifacts_ranked_evidence: `True`
- official_docs_ranked_below_artifacts: `True`
- project_context_non_override: `True`
- obsidian_consultive_only: `True`
- chat_memory_non_authoritative: `True`
- external_input_untrusted: `True`
- context_index_reference_only: `True`
- phase_ledger_historical_only: `True`
- stale_roadmap_cannot_override: `True`
- readme_history_cannot_override: `True`
- conflict_resolution_policy_defined: `True`
- conflict_cases_evaluated: `7`
- unresolved_conflict_blocks: `False`
- token_saving_claim_allowed: `False`
- token_saving_measured: `not_measured`
- token_saving_evidence: `none`
- blocker_count: `0`
- warning_count: `0`
proxima fase recomendada: `F21-A6 — Obsidian MCP Human Evidence Intake`

Hard locks outrank lower tiers and active-context remains live.
## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_ready`
- decision: `pass`
- phase_id: `F21-A5`
- macroblock_id: `MB1`
- source_of_truth_precedence_defined: `True`
- hard_locks_ranked_first: `True`
- next_action_ranked_operational_first: `True`
- current_state_ranked_live_state: `True`
- phase_artifacts_ranked_evidence: `True`
- official_docs_ranked_below_artifacts: `True`
- project_context_non_override: `True`
- obsidian_consultive_only: `True`
- chat_memory_non_authoritative: `True`
- external_input_untrusted: `True`
- context_index_reference_only: `True`
- phase_ledger_historical_only: `True`
- stale_roadmap_cannot_override: `True`
- readme_history_cannot_override: `True`
- conflict_resolution_policy_defined: `True`
- conflict_cases_evaluated: `7`
- unresolved_conflict_blocks: `False`
- token_saving_claim_allowed: `False`
- token_saving_measured: `not_measured`
- token_saving_evidence: `none`
- blocker_count: `0`
- warning_count: `0`
proxima fase recomendada: `F21-A6 — Obsidian MCP Human Evidence Intake`

Hard locks outrank lower tiers and active-context remains live.
## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_blocked`
- decision: `blocked`
- phase_id: `F21-A5`
- macroblock_id: `MB1`
- source_of_truth_precedence_defined: `False`
- hard_locks_ranked_first: `True`
- next_action_ranked_operational_first: `True`
- current_state_ranked_live_state: `True`
- phase_artifacts_ranked_evidence: `True`
- official_docs_ranked_below_artifacts: `True`
- project_context_non_override: `True`
- obsidian_consultive_only: `True`
- chat_memory_non_authoritative: `True`
- external_input_untrusted: `True`
- context_index_reference_only: `True`
- phase_ledger_historical_only: `True`
- stale_roadmap_cannot_override: `True`
- readme_history_cannot_override: `True`
- conflict_resolution_policy_defined: `True`
- conflict_cases_evaluated: `7`
- unresolved_conflict_blocks: `True`
- token_saving_claim_allowed: `False`
- token_saving_measured: `not_measured`
- token_saving_evidence: `none`
- blocker_count: `1`
- warning_count: `0`
proxima fase recomendada: `F21-A6 — Obsidian MCP Human Evidence Intake`

Hard locks outrank lower tiers and active-context remains live.
## F21-A4 — Context Budget Policy Gate
- status: `context_budget_policy_gate_ready`
- decision: `pass`
- phase_id: `F21-A4`
- macroblock_id: `MB1`
- context_budget_policy_defined: `True`
- active_context_required: `True`
- decision_locks_required: `True`
- next_action_required: `True`
- summary_first_policy_defined: `True`
- query_first_policy_defined: `True`
- docs_targeted_only: `True`
- archive_bulk_read_blocked: `True`
- chat_memory_non_authoritative: `True`
- external_input_untrusted: `True`
- full_source_read_requires_reason: `True`
- token_saving_claim_allowed: `False`
- token_saving_measured: `not_measured`
- token_saving_evidence: `none`
- blocker_count: `0`
- warning_count: `0`
- next_recommended_phase: `F21-A5 — Source-of-Truth Precedence Gate`

F21-A4 formalizes the context budget policy without claiming measured savings.
## F21-A3 — Claude Code Instruction Alignment
- status: `claude_code_instruction_alignment_ready`
- decision: `pass`
- phase_id: `F21-A3`
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- f21_a1_verified: `True`
- f21_a2_verified: `True`
- claude_md_found: `True`
- claude_md_modified: `True`
- claude_code_alignment_verified: `True`
- agents_md_alignment_verified: `True`
- codex_skill_alignment_verified: `True`
- active_context_read_first_required: `True`
- source_precedence_enforced: `True`
- untrusted_input_boundary_enforced: `True`
- obsidian_query_first_only: `True`
- bulk_read_blocked: `True`
- token_saving_claim_without_evidence_blocked: `True`
- context_usage_report_required: `True`
- final_active_context_update_required: `True`
- commit_push_hash_required: `True`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- f21b_start_allowed: `False`
- f33_start_allowed: `False`
- r0_start_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- mcp_activation_allowed: `False`
- vault_write_allowed: `False`
- blocker_count: `0`
- warning_count: `0`
- next_recommended_phase: `F21-A4 — Context Budget Policy Gate`

F21-A3 aligns Claude Code instructions with the active-context contract, source precedence, and final handoff requirements without promoting runtime, product, or customer-real execution.

## F21-A2 — Codex Skill Alignment Review
- status: `codex_skill_alignment_review_warn`
- decision: `warn`
- phase_id: `F21-A2`
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- f21_a1_verified: `True`
- active_context_read_first_required: `True`
- source_precedence_enforced: `True`
- untrusted_input_boundary_enforced: `True`
- obsidian_query_first_only: `True`
- bulk_read_blocked: `True`
- prompt_final_active_context_update_required: `True`
- commit_push_hash_required: `True`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- f21b_start_allowed: `False`
- f33_start_allowed: `False`
- r0_start_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- mcp_activation_allowed: `False`
- vault_write_allowed: `False`
- blocker_count: `0`
- warning_count: `3`
- next_recommended_phase: `F21-A3 — Claude Code Instruction Alignment`

F21-A2 aligns the active-context boundary review to the Codex skill, the Claude contract, and the source-of-truth policy without promoting runtime, product, or customer-real execution.
## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_ready_with_warnings`
- decision: `warn`
- phase_id: `F21-A1`
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- active_context_read_first_verified: `True`
- source_precedence_policy_defined: `True`
- untrusted_input_boundary_defined: `True`
- obsidian_query_first_only: `True`
- bulk_read_blocked: `True`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- f33_start_allowed: `False`
- r0_start_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- mcp_activation_allowed: `False`
- vault_write_allowed: `False`
- blocker_count: `0`
- warning_count: `4`
- next_recommended_phase: `F21-A2 — Codex Skill Alignment Review`

F21-A1 is now materialized as the live context boundary gate for MB1.

## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_blocked`
- decision: `blocked`
- phase_id: `F21-A1`
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- active_context_read_first_verified: `False`
- source_precedence_policy_defined: `False`
- untrusted_input_boundary_defined: `True`
- obsidian_query_first_only: `True`
- bulk_read_blocked: `True`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- f33_start_allowed: `False`
- r0_start_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- mcp_activation_allowed: `False`
- vault_write_allowed: `False`
- blocker_count: `2`
- warning_count: `4`
- next_recommended_phase: `F21-A2 — Codex Skill Alignment Review`

F21-A1 is now materialized as the live context boundary gate for MB1.

## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_blocked`
- decision: `blocked`
- phase_id: `F21-A1`
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- active_context_read_first_verified: `False`
- source_precedence_policy_defined: `False`
- untrusted_input_boundary_defined: `False`
- obsidian_query_first_only: `True`
- bulk_read_blocked: `True`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- f33_start_allowed: `False`
- r0_start_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- mcp_activation_allowed: `False`
- vault_write_allowed: `False`
- blocker_count: `3`
- warning_count: `4`
- next_recommended_phase: `F21-A2 — Codex Skill Alignment Review`

F21-A1 is now materialized as the live context boundary gate for MB1.

## ARIS-CONTEXT-MACROBLOCK-CLEANUP — Macroblock Navigation Cleanup State
- status: `active_context_macroblock_cleanup_ready_warn`
- roadmap_navigation_model: `macroblock_first`
- macroblock_atual: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- legacy_phase_id: `F21`
- gate_atual: `F21-A1 — Context Source Access Policy & Untrusted Input Boundary`
- next_action: `F21-A1`
- ultimo_fechamento_relevante: `MB0/P29 context compaction`
- p29_closed: `true`
- p29_token_reduction: `130735`
- f32_state: `closed_tombstone`
- f33_state: `blocked`
- r0_f120_role: `Lab/Governance roadmap, not live NEXT_ACTION`
- f120_authorizes_production: `false`
- production_authorized: `false`
- customer_real_authorized: `false`
- decision_locks_modified: `false`
- preexisting_untracked_noise: `true`

## Macroblock Snapshot
- MB0: closed/stabilized
- MB1: active
- MB2: planned/paused
- MB3: blocked
- MB4: foundational/partial/planned
- MB5: future/blocked
- MB6: future/controlled
- MB7: planned
- MB8: future
- MB9: future

## Operational Summary
- where_we_are: `MB1 active; F21 live`
- what_is_next: `F21-A1`
- what_is_closed: `MB0/P29`, `F32`
- what_is_blocked: `F33`
- not_authorized: `R0-F120 production`, `customer-real use`
