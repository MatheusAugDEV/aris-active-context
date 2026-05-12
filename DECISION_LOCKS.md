# DECISION_LOCKS

- Official V6 naming stays on the PDF path F1-F29 only.
- Obsidian is query-first, read-only, derived, and never authorizing.
- No bulk Obsidian read.
- No network.
- No dependency install.
- No runtime mutation.
- No vault write.
- Chat context, Codex status, commit text, placeholder, instructions, schema, marker, contract, checklist, evidence manifest, awaiting marker, and awaiting contract do not count as authorization.
- F32 owns MCP read-only configuration, controlled apply planning, activation planning, smoke validation, zero-write/no-bulk-read validation, and closure before F33.
- F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline; F33.KR2 may resume under Lab contract without product authorization.

## ARIS-LAB-A0 Authority Lock

- F33 is temporarily paused for ARIS Lab foundation.
- F33.KR2 remains preserved as the paused resume point.
- The ARIS Lab governs promotion, demotion, and obsolescence decisions.
- The ARIS Bedrock Gate is deterministic, auditable, versioned, non-LLM, and evidence-based.
- No capability may move from ARIS Project to ARIS Produto without a Bedrock Gate pass.
- F44 is reinterpreted as ARIS Lab hardening, red-team expansion, and benchmark maturity.
## ARIS-LAB-A1 Capability Taxonomy Lock

- The ARIS Lab capability taxonomy is canonical, declarative, and versioned.
- The Project to Product boundary remains blocked until a Bedrock Gate pass exists.
- No capability may reach produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.
## ARIS-LAB-A1 Capability Taxonomy Lock

- The ARIS Lab capability taxonomy is canonical, declarative, and versioned.
- The Project to Product boundary remains blocked until a Bedrock Gate pass exists.
- No capability may reach produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.
## F32.Z13O Planning Lock

- Status: `f32_future_mcp_readonly_configuration_controlled_apply_final_authorization_planning_gate_passed`.
- Z13O is planning-only and does not authorize real apply, real config write, MCP activation, or real Obsidian access.
- real apply allowed now: `False`
- real config write allowed now: `False`
- MCP activation allowed now: `False`
- real Obsidian access allowed now: `False`
- vault write allowed: `False`
- bulk Obsidian read allowed: `False`
- network allowed: `False`
- dependency installation allowed: `False`
- runtime mutation allowed: `False`

## F32.Z13O-Review Review Lock

- Status: `f32_future_mcp_readonly_configuration_controlled_apply_final_authorization_planning_review_gate_passed`.
- F32.Z13O-Review is review-only and does not authorize real apply, real config write, MCP activation, or real Obsidian access.
- real apply allowed now: `False`
- real config write allowed now: `False`
- MCP activation allowed now: `False`
- real Obsidian access allowed now: `False`
- vault write allowed: `False`
- bulk Obsidian read allowed: `False`
- network allowed: `False`
- dependency installation allowed: `False`
- runtime mutation allowed: `False`

## F32.Z13P Intake Lock

- F32.Z13P is evidence-intake-only and must not execute apply.
- Chat context, Codex status, commit text, placeholder, instructions, schema, marker, contract, checklist, evidence manifest, awaiting marker, and awaiting contract do not count as authorization.
- `NEXT_ACTION.md` is the only source for the next step.

## F32.RESEARCH-P0 Research Lock

- Research artifacts do not authorize implementation.
- External research reports are advisory only.
- No third-party project pattern enters ARIS without gate, test, and security review.

## F32.RESEARCH-P1G Research Lock

- F32.RESEARCH-P1G is external_advisory_research only.
- Raw Gemini input is preserved, but claims and patterns remain advisory-only.
- No implementation or roadmap mutation follows from P1G without cross-model comparison and primary-source verification.

## F32.RESEARCH-P1K Research Lock

- F32.RESEARCH-P1K is external_advisory_research only.
- Raw Kimi input is preserved, but claims and patterns remain advisory-only.
- No implementation or roadmap mutation follows from P1K without cross-model comparison and primary-source verification.

## F32.RESEARCH-P1C Research Lock

- F32.RESEARCH-P1C is external_advisory_research only.
- Raw Claude input is preserved, but claims, patterns, risk signals, and candidate roadmap remain advisory-only.
- No implementation or roadmap mutation follows from P1C without cross-model comparison and primary-source verification.

## F32.RESEARCH-P2 Research Lock

- F32.RESEARCH-P2 synthesis is advisory-only and does not authorize implementation.
- F32.RESEARCH-P2 does not mutate the operational roadmap.
- Only elite candidates may proceed to F32.RESEARCH-P3 impact analysis.
- External research remains advisory until verified and accepted through review gates.

## F32.RESEARCH-P2G Research Lock

- F32.RESEARCH-P2G is external_unverified evidence intake only; no architectural decision, roadmap mutation, or implementation follows without cross-model comparison and review gates.
- Gemini Research 2 is preserved for comparison, but not as source-of-truth.

## F32.RESEARCH-P2GPT Research Lock

- F32.RESEARCH-P2GPT is external_unverified evidence intake only; no architectural decision, roadmap mutation, or implementation follows without cross-model comparison and review gates.
- GPT Research 2 is preserved for comparison, but not as source-of-truth.

## F32.RESEARCH-P2H Research Lock

- F32.RESEARCH-P2H consolidates external_unverified research inputs only; it does not authorize architecture decisions, roadmap mutation, or implementation.
- Mandatory Gemini and GPT inputs are validated, while optional sources remain missing unless officially found in `artifacts/f32/research/`.

## F32.RESEARCH-P3 Research Lock

- Status: `roadmap_impact_analysis_passed_candidate_delta_ready`.
- F32.RESEARCH-P3 is advisory roadmap impact analysis only.
- The roadmap delta is candidate-only and does not change the canonical roadmap.
- Architecture decision allowed: `False`.
- Roadmap change allowed: `False`.
- Implementation allowed: `False`.
- Technology integration allowed: `False`.
- Runtime, frontend, audio, action runtime, MCP activation, network, dependency install, and Obsidian bulk read remain blocked.
- External claims remain `external_unverified` unless later validated with primary sources.

## F32.RESEARCH-P4 Research Lock

- Status: `canonical_roadmap_delta_review_passed`.
- F32.RESEARCH-P4 approves only a candidate canonical roadmap delta.
- The current canonical roadmap is not replaced in this phase.
- F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline.
- F32.Z13P remains the next operational action.
- No implementation, runtime mutation, frontend mutation, audio mutation, action runtime mutation, MCP activation, network use, dependency installation, or Obsidian bulk read is authorized.

## F32.RESEARCH-P5 Research Lock

- Status: `canonical_roadmap_supersession_materialization_passed`.
- F32.RESEARCH-P5 materializes only canonical roadmap documentation and archive state.
- `ROADMAP_CANONICAL_F33_F50.md` is the only active canonical roadmap.
- `ROADMAP_F30_F50.md` is superseded/tombstone only.
- F32.Z13P remains the next operational action.
- F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline.
- No implementation, runtime mutation, frontend mutation, audio mutation, action runtime mutation, MCP activation, network use, dependency installation, or Obsidian bulk read is authorized.

## Canonical Action Runtime Chain Locks

- Action Registry is the source-of-truth for actions.
- Tool schema is derived-only and never authoritative.
- Typed plan and typed approval are mandatory before execution.
- Immutable hashed plan and deterministic preview are mandatory before side effects.
- Side effects require sidecar isolation, append-only ledger evidence, and rollback or compensation coverage.
- MCP write/command, auto-run, continuous learning/auto-retraining, and external vector DB as mandatory base remain prohibited.

## F32.Z13P Intake Review Lock

- Status: `f32_future_mcp_readonly_configuration_controlled_apply_final_human_authorization_evidence_intake_ready`.
- F32.Z13P remains evidence-intake-only and does not authorize apply.
- Evidence status: `valid_dedicated_authorization_evidence`.
- Human authorization evidence may be recorded for future review, but it does not authorize real apply in this phase.
- No real apply, no real config write, no MCP activation, no real Obsidian access, no vault write, no bulk Obsidian read, no network, no dependency install, no runtime mutation, and no implementation are authorized.

## F32.Z13Q Review Lock

- Status: `f32_future_mcp_readonly_configuration_controlled_apply_final_human_authorization_evidence_review_gate_passed`.
- F32.Z13Q is review-only and does not authorize apply.
- source_phase_checked: `True`.
- intake_artifacts_found: `True`.
- dedicated_authorization_evidence_found: `True`.
- dedicated_authorization_evidence_valid: `True`.
- evidence_review_passed: `True`.
- Evidence status: `valid_dedicated_authorization_evidence`.
- No real apply, no real config write, no MCP activation, no real Obsidian access, no vault write, no bulk Obsidian read, no network, no dependency install, no runtime mutation, and no implementation are authorized.
- Next phase recommendation: `F32.Z13P/R1 — Final Human Authorization Evidence Recovery`.

## F32.Z13P/R1 Recovery Lock

- Status: `f32_future_mcp_readonly_configuration_final_human_authorization_evidence_recovery_passed`.
- F32.Z13P/R1 is recovery-only and does not authorize apply.
- anchor_phase: `F32.Z13Q`.
- Evidence status: `valid_dedicated_authorization_evidence`.
- source_phase_checked: `True`.
- intake_artifacts_found: `True`.
- z13p_intake_found: `True`.
- z13q_review_found: `True`.
- dedicated_authorization_evidence_found: `True`.
- dedicated_authorization_evidence_valid: `True`.
- evidence_review_passed: `True`.
- evidence_chain_recovered: `True`.
- evidence_chain_consistent: `True`.
- stale_or_conflicting_context_found: `False`.
- stale_or_conflicting_context_repaired: `False`.
- recovery_manifest_created: `True`.
- recovery_report_created: `True`.
- No real apply, no real config write, no MCP activation, no real Obsidian access, no vault write, no bulk Obsidian read, no network, no dependency install, no runtime mutation, and no implementation are authorized.
- Next phase recommendation: `F32.Z13S — Final Human Authorization Evidence Closure Gate`.

## F32.Z13S Closure Lock

- Status: `f32_future_mcp_readonly_configuration_final_human_authorization_evidence_closure_gate_passed`.
- F32.Z13S is closure-only and does not authorize apply.
- anchor_phase: `F32.Z13P/R1`.
- Evidence status: `valid_dedicated_authorization_evidence`.
- source_phase_checked: `True`.
- intake_artifacts_found: `True`.
- z13p_intake_found: `True`.
- z13q_review_found: `True`.
- z13p_r1_recovery_found: `True`.
- dedicated_authorization_evidence_found: `True`.
- dedicated_authorization_evidence_valid: `True`.
- evidence_chain_recovered: `True`.
- evidence_chain_consistent: `True`.
- evidence_chain_closure_ready: `True`.
- evidence_closure_passed: `True`.
- f32_evidence_chain_closed: `True`.
- f32_ready_for_next_conservative_gate: `True`.
- f33_start_allowed: `False`.
- stale_or_conflicting_context_found: `False`.
- stale_or_conflicting_context_repaired: `False`.
- closure_manifest_created: `True`.
- closure_report_created: `True`.
- No real apply, no real config write, no MCP activation, no real Obsidian access, no vault write, no bulk Obsidian read, no network, no dependency install, no runtime mutation, and no implementation are authorized.
- Next phase recommendation: `F32.Z13T — Final F32 Closure Transition Gate`.

## F32.Z13T Transition Lock

- Status: `f32_future_mcp_readonly_configuration_final_f32_closure_transition_gate_passed`.
- F32.Z13T is transition-only and does not authorize apply.
- anchor_phase: `F32.Z13S`.
- source_phase_checked: `True`.
- z13p_intake_found: `True`.
- z13q_review_found: `True`.
- z13p_r1_recovery_found: `True`.
- z13s_closure_found: `True`.
- dedicated_authorization_evidence_found: `True`.
- dedicated_authorization_evidence_valid: `True`.
- evidence_chain_closed: `True`.
- evidence_chain_consistent: `True`.
- mcp_readonly_configuration_scope_reviewed: `True`.
- controlled_apply_planning_scope_reviewed: `True`.
- activation_planning_scope_reviewed: `True`.
- smoke_validation_scope_reviewed: `True`.
- zero_write_no_bulk_read_scope_reviewed: `True`.
- roadmap_canonical_f33_reserved_reviewed: `True`.
- f32_scope_reviewed: `True`.
- active_context_consistent: `True`.
- decision_locks_consistent: `True`.
- f32_closure_transition_ready: `True`.
- f32_ready_for_final_closure_gate: `True`.
- f32_closed: `False`.
- f33_start_allowed: `False`.
- apply_allowed_now: `False`.
- real_apply_allowed_now: `False`.
- config_write_allowed_now: `False`.
- real_config_write_allowed_now: `False`.
- mcp_activation_allowed_now: `False`.
- real_obsidian_access_allowed_now: `False`.
- vault_write_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F32.Z13T/R1 — Final F32 Closure Gate`.

## F32.Z13T/R1 Final Closure Lock

- Status: `f32_future_mcp_readonly_configuration_final_f32_closure_gate_passed`.
- F32.Z13T/R1 is closure-only and does not authorize apply.
- anchor_phase: `F32.Z13T`.
- source_phase_checked: `True`.
- z13p_intake_found: `True`.
- z13q_review_found: `True`.
- z13p_r1_recovery_found: `True`.
- z13s_closure_found: `True`.
- z13t_transition_found: `True`.
- dedicated_authorization_evidence_found: `True`.
- dedicated_authorization_evidence_valid: `True`.
- evidence_chain_closed: `True`.
- evidence_chain_consistent: `True`.
- mcp_readonly_configuration_scope_reviewed: `True`.
- controlled_apply_planning_scope_reviewed: `True`.
- activation_planning_scope_reviewed: `True`.
- smoke_validation_scope_reviewed: `True`.
- zero_write_no_bulk_read_scope_reviewed: `True`.
- roadmap_canonical_f33_reserved_reviewed: `True`.
- f32_scope_reviewed: `True`.
- active_context_consistent: `True`.
- decision_locks_consistent: `True`.
- formal_closure_criteria_complete: `True`.
- formal_closure_blockers: `[]`.
- f32_closed: `True`.
- f33_unblocked_for_next_phase: `True`.
- f33_start_allowed_now: `False`.
- f33_start_allowed: `False`.
- apply_allowed_now: `False`.
- real_apply_allowed_now: `False`.
- config_write_allowed_now: `False`.
- real_config_write_allowed_now: `False`.
- mcp_activation_allowed_now: `False`.
- real_obsidian_access_allowed_now: `False`.
- vault_write_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- f33_reserved_scope: `SQLite Memory, FTS5, Provenance & Evaluation Baseline`.
- Next phase recommendation: `F33.A — SQLite Memory, FTS5, Provenance & Evaluation Baseline`.

## F33.A Charter Lock

- Status: `f33_governed_local_memory_charter_passed`.
- F33.A is charter-only and does not authorize database creation, schema apply, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F32.Z13T/R1`.
- f32_closed_verified: `True`.
- f33_next_action_verified: `True`.
- roadmap_canonical_f33_scope_verified: `True`.
- roadmap_canonical_preserved: `True`.
- f33_charter_created: `True`.
- governed_local_memory_detailing_created: `True`.
- memory_domains_defined: `True`.
- source_authority_defined: `True`.
- validity_states_defined: `True`.
- provenance_required: `True`.
- direct_llm_memory_write_allowed: `False`.
- runtime_memory_integration_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- memory_without_source_allowed: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F33.B — Governed Local Memory Charter Review Gate`.

## F33.B Review Lock

- Status: `f33_governed_local_memory_charter_review_gate_passed`.
- F33.B is review-only and does not authorize database creation, schema apply, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F33.A — Governed Local Memory Charter`.
- source_phase_checked: `True`.
- f32_closed_verified: `True`.
- f33a_summary_found: `True`.
- f33a_plan_found: `True`.
- f33a_status_verified: `True`.
- canonical_f33_scope_verified: `True`.
- memory_domains_reviewed: `True`.
- source_authority_reviewed: `True`.
- validity_states_reviewed: `True`.
- provenance_requirement_reviewed: `True`.
- forbidden_operations_preserved: `True`.
- blocker_count: `0`.
- warning_count: `0`.
- review_passed: `True`.
- direct_llm_memory_write_allowed: `False`.
- runtime_memory_integration_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- memory_without_source_allowed: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F33.C — Governed Local Memory Technical Planning Gate`.

## F33.RESEARCH-SP0 Similar Projects Reference Library Intake Lock

- F33.RESEARCH-SP0 is external_unverified/advisory-only research intake and does not authorize implementation, roadmap mutation, dependency installation, runtime mutation, MCP activation, or next-action replacement.
- No external claim becomes verified here without primary-source validation.
- Missing operator raw input must fail deterministically and must not be treated as authorization.

## F33.RESEARCH-SP0/R1 Similar Projects Intake Recovery Closure Lock

- F33.RESEARCH-SP0/R1 is recovery/closure-only for the Similar Projects Reference Library and does not authorize implementation, roadmap mutation, dependency installation, runtime mutation, DB/schema/FTS5 creation, MCP activation, Obsidian access, or network use.
- The library remains external_unverified/advisory-only.
- Principal NEXT_ACTION is preserved and must not be replaced by this recovery.

## F33.C Planning Lock

- Status: `f33_governed_local_memory_technical_planning_gate_ready`.
- F33.C is planning-only and does not authorize database creation, schema apply, FTS5 table creation, runtime integration, ingestion, dependency selection, or implementation.
- anchor_phase: `F33.B — Governed Local Memory Charter Review Gate`.
- f33b_status_verified: `True`.
- f33b_review_passed_verified: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- technical_plan_created: `True`.
- schema_plan_created: `True`.
- policy_matrix_created: `True`.
- next_phase_contract_created: `True`.
- memory_domains_planned: `True`.
- source_authority_planned: `True`.
- validity_states_planned: `True`.
- provenance_required: `True`.
- source_fk_required_in_future_schema: `True`.
- ttl_policy_planned: `True`.
- supersession_policy_planned: `True`.
- pii_redaction_policy_planned: `True`.
- contradiction_check_policy_planned: `True`.
- write_gate_policy_planned: `True`.
- read_path_policy_planned: `True`.
- audit_ledger_policy_planned: `True`.
- similar_projects_consulted: `True`.
- similar_projects_advisory_only: `True`.
- similar_projects_used_for_decision: `False`.
- similar_projects_primary_source_verification_required: `True`.
- similar_projects_start_of_phase_rule_planned: `True`.
- direct_llm_memory_write_allowed: `False`.
- runtime_memory_integration_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- memory_without_source_allowed: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F33.D — Governed Local Memory Technical Planning Review Gate`.

## Similar Projects Advisory Rule

- At the start of each new phase, consult the Similar Projects Reference Library as advisory-only research.
- Similar Projects must never become source-of-truth or implementation authorization.
- Claims from Similar Projects require primary-source verification before technical use.

## F33.RULE-P0 Prompt Compact Contract Lock

- Status: `f33_rule_p0_aris_phase_prompt_compact_contract_ready`.
- `ARIS_PHASE_PROMPT_CONTRACT_V2` is the compact prompt contract for future ARIS phases.
- Future prompts may reference named guards instead of repeating full prohibition blocks, but safety, tests, runner artifacts, active-context updates, and source-of-truth precedence remain mandatory.
- Similar Projects Reference Library must be consulted at the start of every new ARIS phase as advisory-only research for risks, patterns, antipatterns, and future verification candidates.
- Similar Projects remains advisory-only and does not authorize implementation, roadmap mutation, dependency authority, runtime authority, DB/schema/FTS5 creation, MCP activation, Obsidian bulk read, or network access.
- Chat instructions alone do not override active-context.

## F33.D Review Lock

- Status: `f33_governed_local_memory_technical_planning_review_gate_passed`.
- F33.D is review-only and does not authorize database creation, schema apply, FTS5 table creation, real memory ingestion, runtime integration, or implementation.
- anchor_phase: `F33.C — Governed Local Memory Technical Planning Gate`.
- source_phase_checked: `True`.
- f33c_status_verified: `True`.
- f33c_planning_passed_verified: `True`.
- f33b_anchor_verified: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- schema_plan_reviewed: `True`.
- schema_plan_declarative_only_verified: `True`.
- schema_entities_reviewed: `True`.
- source_link_required_verified: `True`.
- provenance_required_verified: `True`.
- fts5_plan_reviewed: `True`.
- fts5_real_creation_blocked_verified: `True`.
- policy_matrix_reviewed: `True`.
- write_gate_policy_reviewed: `True`.
- read_gate_policy_reviewed: `True`.
- source_authority_policy_reviewed: `True`.
- ttl_policy_reviewed: `True`.
- supersession_policy_reviewed: `True`.
- pii_redaction_policy_reviewed: `True`.
- contradiction_check_policy_reviewed: `True`.
- audit_ledger_policy_reviewed: `True`.
- no_direct_llm_write_verified: `True`.
- no_continuous_learning_verified: `True`.
- no_auto_retraining_verified: `True`.
- no_external_vector_db_requirement_verified: `True`.
- similar_projects_consulted: `True`.
- similar_projects_advisory_only: `True`.
- similar_projects_used_for_decision: `False`.
- similar_projects_primary_source_verification_required: `True`.
- blocker_count: `0`.
- warning_count: `0`.
- review_passed: `True`.
- implementation_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- runtime_memory_integration_allowed_now: `False`.
- direct_llm_memory_write_allowed: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- Next phase recommendation: `F33.E — Governed Local Memory Schema Contract Gate`.

## F33.E Schema Contract Lock

- Status: `f33_governed_local_memory_schema_contract_gate_ready`.
- F33.E is contract-only and does not authorize database creation, schema apply, migration execution, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F33.D`.
- source_phase_checked: `True`.
- f33d_status_verified: `True`.
- f33d_review_passed_verified: `True`.
- f33c_schema_plan_found: `True`.
- f33c_policy_matrix_found: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- schema_contract_created: `True`.
- field_catalog_created: `True`.
- constraints_matrix_created: `True`.
- migration_safety_contract_created: `True`.
- source_link_required_verified: `True`.
- provenance_required_verified: `True`.
- validity_fields_required_verified: `True`.
- redaction_fields_planned: `True`.
- contradiction_fields_planned: `True`.
- audit_fields_planned: `True`.
- fts5_contract_planned: `True`.
- fts5_real_creation_blocked_verified: `True`.
- migration_apply_blocked_verified: `True`.
- direct_llm_memory_write_allowed: `False`.
- runtime_memory_integration_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- sqlite_migration_allowed_now: `False`.
- sqlite_connect_allowed_now: `False`.
- db_file_creation_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- fts5_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- memory_without_source_allowed: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F33.F — Governed Local Memory Schema Contract Review Gate`.

## F33.F Schema Contract Review Lock

- Status: `f33_governed_local_memory_schema_contract_review_gate_passed`.
- F33.F is review-only and does not authorize database creation, schema apply, migration execution, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F33.E`.
- source_phase_checked: `True`.
- f33e_status_verified: `True`.
- f33e_contract_passed_verified: `True`.
- f33d_anchor_verified: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- schema_contract_reviewed: `True`.
- field_catalog_reviewed: `True`.
- constraints_matrix_reviewed: `True`.
- migration_safety_contract_reviewed: `True`.
- required_entities_reviewed: `True`.
- required_fields_reviewed: `True`.
- source_link_required_verified: `True`.
- provenance_required_verified: `True`.
- validity_fields_required_verified: `True`.
- redaction_fields_reviewed: `True`.
- contradiction_fields_reviewed: `True`.
- audit_fields_reviewed: `True`.
- fts5_contract_reviewed: `True`.
- fts5_real_creation_blocked_verified: `True`.
- migration_apply_blocked_verified: `True`.
- sqlite_connect_blocked_verified: `True`.
- db_file_creation_blocked_verified: `True`.
- direct_llm_memory_write_allowed: `False`.
- runtime_memory_integration_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- sqlite_migration_allowed_now: `False`.
- sqlite_connect_allowed_now: `False`.
- db_file_creation_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- fts5_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- memory_without_source_allowed: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- implementation_allowed_now: `False`.
- Next phase recommendation: `F33.G — Governed Local Memory SQLite Dry-Run Plan Gate`.

## F33.G SQLite Dry-Run Plan Lock

- Status: `f33_governed_local_memory_sqlite_dry_run_plan_gate_ready`.
- F33.G is plan-only and does not authorize database creation, sqlite connect, schema apply, migration execution, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F33.F`.
- source_phase_checked: `True`.
- f33f_status_verified: `True`.
- f33f_review_passed_verified: `True`.
- f33f_anchor_verified: `True`.
- f33e_schema_contract_found: `True`.
- f33e_migration_safety_contract_found: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- dry_run_plan_created: `True`.
- sql_render_plan_created: `True`.
- abort_matrix_created: `True`.
- rollback_plan_created: `True`.
- ledger_preview_created: `True`.
- target_paths_planned: `True`.
- db_file_creation_blocked_verified: `True`.
- sqlite_connect_blocked_verified: `True`.
- schema_apply_blocked_verified: `True`.
- migration_execution_blocked_verified: `True`.
- fts5_creation_blocked_verified: `True`.
- ingestion_blocked_verified: `True`.
- runtime_integration_blocked_verified: `True`.
- backup_required_for_future_apply: `True`.
- rollback_required_for_future_apply: `True`.
- ledger_required_for_future_apply: `True`.
- deterministic_preflight_required: `True`.
- implementation_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_connect_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- sqlite_migration_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- runtime_memory_integration_allowed_now: `False`.
- direct_llm_memory_write_allowed: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- Next phase recommendation: `F33.H — Governed Local Memory SQLite Dry-Run Plan Review Gate`.

## F33.H SQLite Dry-Run Plan Review Lock

- Status: `f33_governed_local_memory_sqlite_dry_run_plan_review_gate_passed`.
- F33.H is review-only and does not authorize database creation, sqlite connect, schema apply, migration execution, FTS5 table creation, runtime integration, or ingestion.
- anchor_phase: `F33.G`.
- source_phase_checked: `True`.
- f33g_status_verified: `True`.
- f33g_planning_passed_verified: `True`.
- f33f_anchor_verified: `True`.
- f32_closed_verified: `True`.
- canonical_f33_scope_verified: `True`.
- dry_run_plan_reviewed: `True`.
- sql_render_plan_reviewed: `True`.
- abort_matrix_reviewed: `True`.
- rollback_plan_reviewed: `True`.
- ledger_preview_reviewed: `True`.
- target_paths_reviewed: `True`.
- no_db_file_created_verified: `True`.
- rendered_sql_artifact_only_verified: `True`.
- sqlite_connect_blocked_verified: `True`.
- schema_apply_blocked_verified: `True`.
- migration_execution_blocked_verified: `True`.
- fts5_creation_blocked_verified: `True`.
- ingestion_blocked_verified: `True`.
- runtime_integration_blocked_verified: `True`.
- human_authorization_future_required_verified: `True`.
- deterministic_preflight_required_verified: `True`.
- implementation_allowed_now: `False`.
- sqlite_database_creation_allowed_now: `False`.
- sqlite_connect_allowed_now: `False`.
- sqlite_schema_apply_allowed_now: `False`.
- sqlite_migration_allowed_now: `False`.
- fts5_table_creation_allowed_now: `False`.
- real_memory_ingestion_allowed_now: `False`.
- runtime_memory_integration_allowed_now: `False`.
- direct_llm_memory_write_allowed: `False`.
- external_vector_db_required: `False`.
- continuous_learning_allowed_now: `False`.
- auto_retraining_allowed_now: `False`.
- obsidian_real_access_allowed_now: `False`.
- bulk_obsidian_read_allowed_now: `False`.
- network_allowed_now: `False`.
- dependency_install_allowed_now: `False`.
- runtime_mutation_allowed_now: `False`.
- Next phase recommendation: `F33.I — Governed Local Memory SQLite Controlled Dry-Run Preparation Gate`.

## F33.I Controlled Dry-Run Preparation Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_preparation_gate_ready`.
- F33.I is preparation-only and does not authorize execution, SQLite connect, schema apply, migration execution, FTS5 creation, runtime integration, or ingestion.
- anchor_phase: `F33.H`.
- current_phase_execution_allowed: `False`.
- current_phase_db_creation_allowed: `False`.
- current_phase_sqlite_connect_allowed: `False`.
- current_phase_schema_apply_allowed: `False`.
- current_phase_fts5_creation_allowed: `False`.
- future_operator_confirmation_required: `True`.
- future_human_authorization_required: `True`.
- future_preflight_required: `True`.
- future_rollback_required: `True`.
- future_ledger_required: `True`.
- future_no_db_precheck_required: `True`.
- future_dry_run_execution_allowed_now: `False`.
- Next phase recommendation: `F33.J — Governed Local Memory SQLite Controlled Dry-Run Preparation Review Gate`.

## Operator-facing Phase Explanation Rule Lock

- PROMPT_CONTRACT.md includes the operator-facing phase explanation rule.
- The rule is operator-facing only and does not weaken guards or authorize implementation.
- The rule must state what the phase is, what it does, what it does not do, why it matters, and one-sentence summary.

## F33.J Controlled Dry-Run Preparation Review Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_preparation_review_gate_passed`.
- F33.J is review-only and does not authorize execution, SQLite connect, schema apply, migration execution, FTS5 creation, runtime integration, or ingestion.
- anchor_phase: `F33.I`.
- current_phase_execution_allowed: `False`.
- current_phase_db_creation_allowed: `False`.
- current_phase_sqlite_connect_allowed: `False`.
- current_phase_schema_apply_allowed: `False`.
- current_phase_fts5_creation_allowed: `False`.
- future_operator_confirmation_required: `True`.
- future_human_authorization_required: `True`.
- future_preflight_required: `True`.
- future_rollback_required: `True`.
- future_ledger_required: `True`.
- future_no_db_precheck_required: `True`.
- future_dry_run_execution_allowed_now: `False`.
- Next phase recommendation: `F33.K — Governed Local Memory SQLite Controlled Dry-Run Authorization Gate`.

## F33.K Controlled Dry-Run Authorization Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_authorization_required`.
- F33.K is authorization-only and does not execute the dry-run, create a SQLite database, call sqlite3.connect, apply schema, run migrations, create FTS5, ingest memory, or integrate runtime.
- anchor_phase: `F33.J`.
- dedicated_authorization_evidence_path: `artifacts/f33/f33_governed_local_memory_sqlite_controlled_dry_run_authorization_statement.json`.
- dedicated_authorization_evidence_found: `False`.
- dedicated_authorization_evidence_valid: `False`.
- human_authorization_granted: `False`.
- current_phase_execution_allowed: `False`.
- current_phase_db_creation_allowed: `False`.
- current_phase_sqlite_connect_allowed: `False`.
- current_phase_schema_apply_allowed: `False`.
- current_phase_fts5_creation_allowed: `False`.
- future_dry_run_execution_allowed_next_phase: `False`.
- Next phase recommendation: `F33.KH — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Intake`.

## F33.K Controlled Dry-Run Authorization Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_authorization_required`.
- F33.K is authorization-only and does not execute the dry-run, create a SQLite database, open a SQLite connection, apply schema, run migrations, create FTS5, ingest memory, or integrate runtime.
- anchor_phase: `F33.J`.
- dedicated_authorization_evidence_path: `artifacts/f33/f33_governed_local_memory_sqlite_controlled_dry_run_authorization_statement.json`.
- dedicated_authorization_evidence_found: `False`.
- dedicated_authorization_evidence_valid: `False`.
- human_authorization_granted: `False`.
- current_phase_execution_allowed: `False`.
- current_phase_db_creation_allowed: `False`.
- current_phase_sqlite_connect_allowed: `False`.
- current_phase_schema_apply_allowed: `False`.
- current_phase_fts5_creation_allowed: `False`.
- future_dry_run_execution_allowed_next_phase: `False`.
- Next phase recommendation: `F33.KH — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Intake`.


## F33.KH Intake Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_human_authorization_evidence_intake_ready`.
- Anchor phase: `F33.K — Governed Local Memory SQLite Controlled Dry-Run Authorization Gate`.
- F33.K status verified: `True`.
- F33.K authorization-required state verified: `True`.
- Dedicated authorization evidence found: `False`.
- Dedicated authorization evidence valid: `False`.
- Authorization template created: `True`.
- Operator instructions created: `True`.
- Intake requirements created: `True`.
- Final authorization statement created: `False`.
- Templates, placeholders, prompt text, and chat context do not count as authorization.
- No runtime integration, memory ingestion, Obsidian real access, MCP activation, network access, dependency installation, production use, or runtime mutation is authorized.
- Next phase recommendation: `F33.KR — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Review Gate`.


## F33.KR Review Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_human_authorization_evidence_review_pending`.
- Anchor phase: `F33.KH — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Intake`.
- F33.KH status verified: `True`.
- F33.K authorization-required state verified: `True`.
- Authorization template reviewed: `True`.
- Operator instructions reviewed: `True`.
- Intake requirements reviewed: `True`.
- Placeholder reviewed: `True`.
- Evidence schema reviewed: `True`.
- Final authorization statement found: `False`.
- Final authorization statement valid: `False`.
- Human authorization granted: `False`.
- Templates, placeholders, operator instructions, chat context, prompt text, prior phase success, Codex status, and commit text do not count as authorization.
- No runtime integration, memory ingestion, Obsidian real access, MCP activation, network access, dependency installation, production use, or runtime mutation is authorized.
- Next phase recommendation: `F33.KS — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Submission`.


## F33.KS Submission Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_human_authorization_submission_required`.
- Anchor phase: `F33.KR — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Review Gate`.
- Final authorization statement absent before submission: `True`.
- Operator submission found: `False`.
- Operator submission valid: `False`.
- Final authorization statement created: `False`.
- Submission passed: `False`.
- Templates, placeholders, prompt text, and chat context do not count as authorization.
- No runtime integration, memory ingestion, Obsidian real access, MCP activation, network access, dependency installation, production use, or runtime mutation is authorized.
- Next phase recommendation: `F33.KS/R1 — Human Authorization Evidence Submission Recovery`.

## F33.KS/R1 Recovery Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_human_authorization_submission_recovered`.
- This phase is recovery-only and does not authorize the governed local memory SQLite controlled dry-run.
- operator_submission_found: `True`.
- operator_submission_valid: `True`.
- final_authorization_statement_created: `True`.
- No runtime integration, ingestion, network, Obsidian, MCP, or production use is authorized.

## F33.KR2 Recheck Lock

- Status: `f33_governed_local_memory_sqlite_controlled_dry_run_human_authorization_evidence_review_recheck_passed`.
- Anchor phase: `F33.KS/R1 — Human Authorization Evidence Submission Recovery`.
- Source phase checked: `True`.
- Source chain consistent: `True`.
- Final authorization statement found: `True`.
- Final authorization statement valid: `True`.
- Operator submission found: `True`.
- Operator submission valid: `True`.
- Dedicated authorization evidence valid: `True`.
- No real SQLite DB creation, sqlite connect, schema apply, migration execution, FTS5 creation, memory ingestion, runtime integration, Obsidian real access, MCP activation, network access, dependency installation, vault write, direct LLM memory write, or runtime mutation is authorized.
- Next phase recommendation: `F33.L — Governed Local Memory SQLite Controlled Dry-Run Execution Plan Gate`.

## ARIS-LAB-A2 Evidence Contract Lock

- Evidence packages and hash-chain refs do not authorize product on their own.
- No capability may move to produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.

## ARIS-LAB-A3 Suite Registry Lock

- Suite registry and evaluation skeleton do not authorize product on their own.
- No suite or capability may move to produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.

## ARIS-LAB-A4 Scoring and Bedrock Gate Lock

- The scoring model is declarative, versioned, and contract-only.
- The Bedrock Gate decision schema and contract are deterministic, non-LLM, and non-bypassable.
- No capability may move to produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.

## ARIS-LAB-A5 Regression and Demotion Lock

- The regression policy is declarative and blocks promotion on detected regression.
- Demotion, quarantine, deprecation, supersession, and obsolescence remain contract-only in A5.
- No capability may move to produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.
## ARIS-LAB-A6 Foundation Review Lock

- Status: `aris_lab_foundation_review_passed`.
- The ARIS Lab foundation review gate validates A0-A5 without promoting anything to product.
- Bedrock Gate remains required for product and is not executable yet.
- No capability may move to produto without Bedrock Gate evidence and the required contract chain.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- F33.KR2 remains preserved as the paused resume point.

## ARIS-LAB-B0 Integration Backlog Lock

- Status: `aris_lab_integration_backlog_ready_f33_resume_allowed`.
- The Lab integration backlog authorizes F33.KR2 to resume only under the Lab phase-to-phase contract.
- F33.KR2 resume does not authorize product promotion or any runtime mutation outside the gate scope.
- F33.KR2 compliance contract is required before any Lab review recheck.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- Runtime, DB, schema, FTS5, network, dependency install, action runtime, MCP activation, Obsidian, vault write, and bulk read remain blocked.

## ARIS-LAB-B0/R1 Operational Completion Supersession Lock

- Status: `aris_lab_operational_completion_supersession_ready`.
- The operator has temporarily deferred F33.KR2 to complete the minimal operational Lab.
- F33.KR2 remains preserved as the paused resume point.
- B1-B5 are required before F33 resume.
- C1-C5 are required before product promotion candidate use.
- Bedrock Gate executable now: `False`.
- Product promotion allowed now: `False`.
- Runtime, DB, schema, FTS5, network, dependency install, action runtime, MCP activation, Obsidian, vault write, and bulk read remain blocked.
- F44 remains reinterpreted as lab hardening and maturity.
- Runtime, DB, schema, FTS5, network, dependency, action, MCP, Obsidian, vault, and bulk-read remain blocked.
## ARIS-LAB-BEDROCK-FULL Executable Bedrock Gate Lock

- Status: `aris_lab_bedrock_full_ready`.
- Bedrock Gate executable now: `True` for artifact/evidence decisions only.
- Bedrock Gate scope: `artifact_and_evidence_decision_only`.
- Product state mutation allowed by gate: `False`.
- Product promotion allowed now: `False`.
- Runtime, DB, schema, FTS5, network, dependency install, action runtime, MCP activation, Obsidian, vault write, and bulk read remain blocked.
- F33.KR2 remains the preserved resume point.
## F33.KR2-BEDROCK Evidence Recheck Lock

- Status: `f33kr2_bedrock_evidence_recheck_passed`.
- The Bedrock recheck only authorizes artifact/evidence decisions, never product promotion.
- F33.L is the next principal phase under the Lab contract.
- F33.KR2 evidence chain remains preserved.
- Bedrock Gate executable now: `True` for artifact/evidence decisions only.
- Product promotion allowed now: `False`.
- Runtime, DB, schema, FTS5, network, dependency install, action runtime, MCP activation, Obsidian, vault write, and bulk read remain blocked.
## F33.L-BEDROCK Execution Plan Lock

- Status: `f33l_bedrock_sqlite_controlled_dry_run_execution_plan_ready`.
- F33.L-BEDROCK is artifact/evidence-only and does not authorize real SQLite execution.
- Future controlled dry-run execution stays blocked until F33.M.
- Product promotion remains blocked.
- Runtime mutation remains blocked.
- No SQLite database creation, schema apply, FTS5 creation, real ingestion, network, dependency install, MCP activation, Obsidian access, vault write, or bulk Obsidian read is authorized.
- F33.M is the next principal phase under the Lab contract.
