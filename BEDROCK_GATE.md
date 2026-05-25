# BEDROCK_GATE_FULL_VERDICT_CONTROLLED_EXECUTION
- lock_id: `BEDROCK_GATE_FULL_VERDICT_CONTROLLED_EXECUTION`
- phase_id: `F21-CTX-BEDROCK-R60`
- status: `bedrock_gate_full_verdict_controlled_execution_pass`
- decision: `pass`
- source_review_phase: `F21-CTX-BEDROCK-R58`
- source_review_status: `bedrock_gate_evidence_bundle_final_reconciliation_review_gate_pass`
- source_review_decision: `pass`
- source_reconciliation_phase: `F21-CTX-BEDROCK-R57`
- source_reconciliation_status: `bedrock_gate_evidence_bundle_final_reconciliation_controlled_execution_pass`
- source_reconciliation_decision: `pass`
- source_plan_phase: `F21-CTX-BEDROCK-R56`
- source_plan_status: `bedrock_gate_evidence_bundle_final_reconciliation_plan_ready`
- source_plan_decision: `pass`
- evidence_bundle_complete_reviewed: `True`
- evidence_bundle_complete_review_passed: `True`
- evidence_bundle_complete: `True`
- evidence_bundle_reviewed: `True`
- full_verdict_plan_created: `True`
- verdict_schema_created: `True`
- verdict_input_contract_created: `True`
- verdict_boundary_matrix_created: `True`
- r60_execution_plan_created: `True`
- full_verdict_executed: `True`
- full_verdict_result: `scope_limited_pass`
- selected_verdict_class: `scope_limited_pass`
- technical_gate_status: `scope_limited`
- product_boundary_status: `not_authorized`
- commercial_boundary_status: `not_authorized`
- runtime_boundary_status: `not_authorized`
- client_readiness_status: `not_authorized`
- pricing_readiness_status: `not_authorized`
- bedrock_real_execution_status: `not_authorized`
- full_verdict_execution_allowed_next: `False`
- evidence_classes_complete_or_warning_complete: `10`
- complete_evidence_class_count: `9`
- warning_complete_evidence_class_count: `1`
- blocked_evidence_class_count: `0`
- incomplete_evidence_class_count: `0`
- review_findings_count: `10`
- accepted_findings_count: `9`
- warning_findings_count: `1`
- blocker_findings_count: `0`
- gaps_resolved_count: `4`
- unresolved_gaps_count: `0`
- planned_pending_execution_gap_count: `0`
- source_of_truth_conflicts_detected: `False`
- boundary_risks_detected: `False`
- site_claims_risks_detected: `False`
- blocker_count: `0`
- warning_count: `3`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- production_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- site_marketing_claims_limited: `True`
- site_claims_warning_complete_preserved: `True`
- warning_complete_site_claims_preserved: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- component_pass_is_not_full_gate_pass_preserved: `True`
- evidence_bundle_complete_is_not_full_gate_pass_preserved: `True`
- full_verdict_plan_is_not_full_verdict_preserved: `True`
- global_product_boundary_preserved: `True`
- final_reconciliation_allowed_next: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R61 - Bedrock Gate Full Verdict Review Gate`
- lock principles:
  - `R60 executes the full verdict in a scope-limited technical mode only.`
  - `Evidence bundle complete remains distinct from full Bedrock Gate pass.`
  - `Warning-complete site claims remain non-product and non-commercial.`
  - `Bedrock Gate remains the primary product boundary; technical pass is not product pass.`
  - `R61 is the first review gate after execution and before any closure movement.`
- warnings:
  - `R59 is plan-only and does not execute the full verdict.`
  - `Evidence bundle complete remains distinct from product, commercial, runtime, and production readiness.`
  - `Warning-complete site claims remain controlled-development only and must not be promoted.`
- blockers: `[]`


# BEDROCK_GATE_HUMAN_REVIEW_EVIDENCE_MATERIALIZATION_CONTROLLED_EXECUTION
- phase_id: `F21-CTX-BEDROCK-R54`
- status: `bedrock_gate_human_review_evidence_materialization_controlled_execution_pass`
- decision: `pass`
- source_review_gate_phase: `F21-CTX-BEDROCK-R51`
- source_review_gate_status: `bedrock_gate_evidence_bundle_redry_run_review_gate_warn`
- source_review_gate_decision: `warn`
- source_command_telemetry_phase: `F21-CTX-BEDROCK-R52`
- source_command_telemetry_status: `bedrock_gate_command_telemetry_evidence_controlled_execution_pass`
- source_command_telemetry_decision: `pass`
- source_blocker_scan_phase: `F21-CTX-BEDROCK-R53`
- source_blocker_scan_status: `bedrock_gate_dedicated_blocker_scan_controlled_execution_pass`
- source_blocker_scan_decision: `pass`
- human_review_evidence_materialized: `True`
- human_review_materialization_gap_resolved: `True`
- blocker_count: `0`
- warning_count: `756`
- findings_count: `756`
- source_item_count: `10`
- validated_source_item_count: `10`
- gaps_resolved_count: `3`
- unresolved_gaps_count: `1`
- evidence_bundle_complete: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- production_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R55 - Bedrock Gate Site Claims Full Audit Controlled Execution`
- lock principles:
  - `Human review evidence must be traceable to repository sources and ledger decisions.`
  - `No signature, approval, or human review completion may be invented.`
  - `LLM is support only and cannot replace human review for critical movement.`
  - `Product or commercial claims remain forbidden until the Evidence Bundle is complete and the final review gates pass.`
  - `Bedrock Gate remains the primary product gate; technical pass is not product pass.`


# BEDROCK_GATE_COMMAND_TELEMETRY_EVIDENCE_CONTROLLED_EXECUTION
- phase_id: `F21-CTX-BEDROCK-R52`
- status: `bedrock_gate_command_telemetry_evidence_controlled_execution_pass`
- decision: `pass`
- command_telemetry_evidence_created: `True`
- command_telemetry_executed: `True`
- test_command_telemetry_gap_resolved: `True`
- gaps_resolved_count: `1`
- unresolved_gaps_count: `3`
- planned_pending_execution_gap_count: `3`
- evidence_bundle_complete: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- site_marketing_claims_limited: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- component_pass_is_not_full_gate_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- recommended_next_phase: `F21-CTX-BEDROCK-R53 - Bedrock Gate Dedicated Blocker Scan Controlled Execution`


# BEDROCK_GATE_R51_REVIEW_GATE
- phase_id: `F21-CTX-BEDROCK-R51`
- status: `bedrock_gate_evidence_bundle_redry_run_review_gate_warn`
- decision: `warn`
- review_passed: `True`
- findings_count: `8`
- warning_count: `5`
- blocker_count: `0`
- r49r_ledger_warning_carried_forward: `True`
- evidence_bundle_complete: `False`
- product_promotion_allowed: `False`
- commercial_use_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R52 - Bedrock Gate Command Telemetry Evidence Controlled Execution`


# BEDROCK_GATE_R50_CONTROLLED_EXECUTION
- phase_id: `F21-CTX-BEDROCK-R50`
- status: `bedrock_gate_evidence_bundle_redry_run_controlled_execution_warn`
- decision: `warn`
- source_reconciliation_phase: `F21-CTX-BEDROCK-R49R`
- source_redry_run_plan_phase: `F21-CTX-BEDROCK-R49`
- redry_run_executed: `True`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- real_collection_executed: `False`
- planned_pending_execution_gap_count: `4`
- r49r_ledger_warning_carried_forward: `True`
- recommended_next_phase: `F21-CTX-BEDROCK-R51 - Bedrock Gate Evidence Bundle Re-Dry-Run Review Gate`


# BEDROCK_GATE_R49_ROOT_PACKAGE_RECONCILIATION
- lock_id: `BEDROCK_GATE_R49_ROOT_PACKAGE_RECONCILIATION`
- phase_id: `F21-CTX-BEDROCK-R49R`
- status: `bedrock_gate_r49_root_package_reconciled`
- decision: `pass`
- recovery_gate_created: `True`
- r49_root_package_missing_before: `True`
- r49_package_materialized: `True`
- r49_artifacts_created: `True`
- ledger_warning_recorded: `True`
- recommended_next_phase: `F21-CTX-BEDROCK-R50 - Bedrock Gate Evidence Bundle Re-Dry-Run Controlled Execution`


# BEDROCK_GATE_EVIDENCE_BUNDLE_REDRY_RUN_PLAN
- lock_id: `BEDROCK_GATE_EVIDENCE_BUNDLE_REDRY_RUN_PLAN`
- phase_id: `F21-CTX-BEDROCK-R49`
- status: `bedrock_gate_evidence_bundle_redry_run_plan_ready`
- decision: `pass`
- source_site_claims_plan_phase: `F21-CTX-BEDROCK-R48`
- source_gap_plan_phase: `F21-CTX-BEDROCK-R44`
- redry_run_plan_created: `True`
- redry_run_executed: `False`
- gap_reclassification_created: `True`
- gaps_reclassified_count: `4`
- gaps_resolved_count: `0`
- planned_pending_execution_gap_count: `4`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R50 - Bedrock Gate Evidence Bundle Re-Dry-Run Controlled Execution`


# BEDROCK_GATE_SITE_CLAIMS_AUDIT_GATE_PLAN
- lock_id: `BEDROCK_GATE_SITE_CLAIMS_AUDIT_GATE_PLAN`
- phase_id: `F21-CTX-BEDROCK-R48`
- status: `bedrock_gate_site_claims_audit_gate_plan_ready`
- decision: `pass`
- source_gap_plan_phase: `F21-CTX-BEDROCK-R44`
- source_human_review_phase: `F21-CTX-BEDROCK-R47`
- target_gap_id: `site_claims_full_audit_gap`
- site_claims_audit_gate_defined: `True`
- site_claims_schema_created: `True`
- site_claims_matrix_created: `True`
- site_claims_audit_executed: `False`
- site_claims_clean_certification_created: `False`
- site_copy_modified: `False`
- aris_site_modified: `False`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- gap_remediation_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R49 - Bedrock Gate Evidence Bundle Re-Dry-Run Plan`


# BEDROCK_GATE_HUMAN_REVIEW_EVIDENCE_PACKAGE_PLAN
- lock_id: `BEDROCK_GATE_HUMAN_REVIEW_EVIDENCE_PACKAGE_PLAN`
- phase_id: `F21-CTX-BEDROCK-R47`
- status: `bedrock_gate_human_review_evidence_package_plan_ready`
- decision: `pass`
- source_gap_plan_phase: `F21-CTX-BEDROCK-R44`
- source_blocker_scan_phase: `F21-CTX-BEDROCK-R46`
- target_gap_id: `human_review_materialization_gap`
- human_review_evidence_package_defined: `True`
- human_review_complete: `False`
- human_approval_materialized: `False`
- risk_accepted: `False`
- critical_blocker_overridden: `False`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- gap_remediation_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R48 - Bedrock Gate Site Claims Audit Gate Plan`


# BEDROCK_GATE_DEDICATED_BLOCKER_SCAN_SUBGATE_PLAN
- lock_id: `BEDROCK_GATE_DEDICATED_BLOCKER_SCAN_SUBGATE_PLAN`
- phase_id: `F21-CTX-BEDROCK-R46`
- status: `bedrock_gate_dedicated_blocker_scan_subgate_plan_ready`
- decision: `pass`
- source_gap_plan_phase: `F21-CTX-BEDROCK-R44`
- source_command_telemetry_phase: `F21-CTX-BEDROCK-R45`
- target_gap_id: `dedicated_blocker_scan_gap`
- dedicated_blocker_scan_subgate_defined: `True`
- blocker_scan_schema_created: `True`
- blocker_scan_matrix_created: `True`
- dedicated_blocker_scan_executed: `False`
- blocker_free_certification_created: `False`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- gap_remediation_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R47 - Bedrock Gate Human Review Evidence Package Plan`


# BEDROCK_GATE_COMMAND_TELEMETRY_EVIDENCE_PLAN
- lock_id: `BEDROCK_GATE_COMMAND_TELEMETRY_EVIDENCE_PLAN`
- phase_id: `F21-CTX-BEDROCK-R45`
- status: `bedrock_gate_command_telemetry_evidence_plan_ready`
- decision: `pass`
- command_telemetry_plan_created: `True`
- command_telemetry_executed: `False`
- historical_commands_reexecuted: `False`
- telemetry_artifact_created: `False`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- gap_remediation_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R46 - Bedrock Gate Dedicated Blocker Scan Subgate Plan`


# BEDROCK_GATE_EVIDENCE_BUNDLE_GAP_REMEDIATION_PLAN
- lock_id: `BEDROCK_GATE_EVIDENCE_BUNDLE_GAP_REMEDIATION_PLAN`
- phase_id: `F21-CTX-BEDROCK-R44`
- status: `bedrock_gate_evidence_bundle_gap_remediation_plan_ready`
- decision: `pass`
- gap_remediation_plan_created: `True`
- gap_remediation_executed: `False`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- recommended_next_phase: `F21-CTX-BEDROCK-R45 - Bedrock Gate Command Telemetry Evidence Plan`


# F21-CTX-BEDROCK-R43 - Bedrock Gate Evidence Bundle Dry-Run Review Gate
- status: `bedrock_gate_evidence_bundle_dry_run_review_warn_valid`
- decision: `warn`
- source_dry_run_phase: `F21-CTX-BEDROCK-R42`
- dry_run_confirmed: `True`
- dry_run_warn_is_valid: `True`
- dry_run_warn_requires_gap_plan: `True`
- evidence_bundle_complete: `False`
- evidence_collection_executed: `False`
- real_collection_executed: `False`
- gap_review_count: `4`
- accepted_gap_count: `4`
- recommended_next_phase: `F21-CTX-BEDROCK-R44 - Bedrock Gate Evidence Bundle Gap Remediation Plan`


# F21-CTX-BEDROCK-R42 - Bedrock Gate Evidence Bundle Collection Dry-Run
- status: `bedrock_gate_evidence_bundle_collection_dry_run_ready_warn`
- decision: `warn`
- source collection plan phase: `F21-CTX-BEDROCK-R41`
- dry_run_collection_executed: `True`
- evidence_collection_executed: `False`
- evidence_bundle_complete: `False`
- evidence_classes_evaluated: `10`
- evidence_classes_passed: `source_of_truth_evidence`, `source_artifacts`, `boundary_evidence`, `runner_evidence`, `fixture_evidence`, `closure_evidence`
- evidence_classes_warned: `test_evidence`, `blocker_evidence`, `human_review_evidence`, `site_claims_evidence`
- evidence_classes_blocked: `[]`
- recommended_next_phase: `F21-CTX-BEDROCK-R43 - Bedrock Gate Evidence Bundle Dry-Run Review Gate`
- plan purpose: `Executar um dry-run determinístico da coleta do Evidence Bundle usando a matriz/checklist R41 e os artifacts existentes, sem realizar coleta real nem autorizar produto, comercial, runtime ou Bedrock real.`


# F21-CTX-BEDROCK-R41 - Bedrock Gate Evidence Bundle Collection Plan
- status: `bedrock_gate_evidence_bundle_collection_plan_ready`
- decision: `pass`
- source subgate definition phase: `F21-CTX-BEDROCK-R40`
- collection plan created: `True`
- collection plan matrix created: `True`
- collection plan checklist created: `True`
- evidence bundle complete: `False`
- evidence collection executed: `False`
- evidence class count: `10`
- allowed outputs: `collection_plan_created`, `collection_plan_matrix_created`, `collection_plan_checklist_created`
- forbidden outputs: `evidence_bundle_complete`, `full_bedrock_gate_pass`, `product_pass`, `commercial_approval`, `client_readiness`, `pricing_readiness`, `runtime_activation`, `bedrock_real_execution`, `product_promotion`
- planned future phase: `F21-CTX-BEDROCK-R42 - Bedrock Gate Evidence Bundle Collection Dry-Run`
- plan purpose: `Plano determinístico de coleta e aplicação futura do Evidence Bundle, com matriz de fontes, artefatos, validações, critérios de aceitação/rejeição e ordem segura de execução.`


# F21-CTX-BEDROCK-R40 - Bedrock Gate Evidence Bundle Subgate Definition
- status: `bedrock_gate_evidence_bundle_subgate_definition_ready`
- decision: `pass`
- source charter phase: `F21-CTX-BEDROCK-R39`
- evidence bundle subgate defined: `True`
- evidence bundle schema created: `True`
- evidence bundle matrix created: `True`
- evidence bundle complete: `False`
- evidence collection executed: `False`
- evidence class count: `10`
- allowed outputs: `evidence_bundle_subgate_defined`, `evidence_bundle_schema_ready`, `evidence_bundle_collection_ready_for_future_phase`
- forbidden outputs: `evidence_bundle_complete`, `full_bedrock_gate_pass`, `product_pass`, `commercial_approval`, `client_readiness`, `pricing_readiness`, `runtime_activation`, `bedrock_real_execution`, `product_promotion`
- next phase policy: `F21-CTX-BEDROCK-R41 - Bedrock Gate Evidence Bundle Collection Plan`
- subgate purpose: `Subgate do Bedrock Gate responsável por especificar, validar e consolidar o pacote mínimo de evidências materializadas necessário para qualquer avanço de estado técnico, componente, claim ou trilha dentro do ARIS.`


# F21-CTX-BEDROCK-R39 - Bedrock Gate Full Definition Charter
- latest_completed_phase: `F21-CTX-BEDROCK-R39 - Bedrock Gate Full Definition Charter`
- phase_id: `F21-CTX-BEDROCK-R39`
- status: `bedrock_gate_full_definition_charter_ready`
- decision: `pass`
- source_inventory_phase: `F21-CTX-BEDROCK-R38`
- source_inventory_status: `bedrock_gate_remaining_scope_inventory_ready`
- source_inventory_decision: `pass`
- charter_created: `True`
- charter_schema_created: `True`
- charter_matrix_created: `True`
- bedrock_gate_defined: `True`
- charter_component_count: `16`
- subgate_count: `14`
- required_evidence_class_count: `10`
- request_validation_subgate_status: `component_closed_technical`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- site_marketing_claims_limited: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- component_pass_is_not_full_gate_pass_preserved: `True`
- global_product_boundary_preserved: `True`
- decision_locks_updated: `True`
- boundary_matrix_created: `True`
- allowed outputs: `charter_created`, `full_definition_ready_for_subgate_planning`, `component_pass_acknowledged`
- forbidden outputs: `full_bedrock_gate_pass`, `product_pass`, `commercial_approval`, `client_readiness`, `pricing_readiness`, `runtime_activation`, `bedrock_real_execution`, `product_promotion`
- warning count: `5`
- blocker count: `0`
- warnings:
  - `R38 confirms the runner track closure and the remaining scope inventory.`
  - `R38 does not define the full Bedrock Gate, only the remaining scope that needs formal chartering.`
  - `This charter defines the gate; it does not authorize product, commercial, runtime, or real Bedrock readiness.`
  - `Evidence bundle, blocker scan, source-of-truth consistency, safety boundary, and human review remain pending definition.`
  - `Site claims remain limited to controlled-development language and cannot imply readiness or certification.`
- blockers:
  - `[]`
- recommended_next_phase: `F21-CTX-BEDROCK-R40 - Bedrock Gate Evidence Bundle Subgate Definition`
- gate purpose: `Gate principal do ARIS para decidir se uma capacidade, trilha, componente ou claim pode avançar de estado técnico para estado mais forte, sempre por evidência materializada, boundaries explícitas, blockers determinísticos, source-of-truth consistente e revisão humana quando aplicável.`
- next phase policy: `F21-CTX-BEDROCK-R40 - Bedrock Gate Evidence Bundle Subgate Definition`


# F21-CTX-BEDROCK-R38 - Bedrock Gate Remaining Scope Inventory
- latest_completed_phase: `F21-CTX-BEDROCK-R38 - Bedrock Gate Remaining Scope Inventory`
- phase_id: `F21-CTX-BEDROCK-R38`
- status: `bedrock_gate_remaining_scope_inventory_ready`
- decision: `pass`
- source_boundary_phase: `F21-CTX-BEDROCK-R37`
- source_boundary_status: `bedrock_gate_closure_boundary_consolidated`
- source_boundary_decision: `pass`
- inventory_created: `True`
- inventory_item_count: `16`
- closed_component_count: `1`
- pending_component_count: `9`
- forbidden_future_component_count: `6`
- request_validation_runner_closed_technical: `True`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- site_marketing_claims_limited: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- closure_pass_is_not_commercial_approval_preserved: `True`
- global_product_boundary_preserved: `True`
- boundary_matrix_created: `True`
- decision_locks_updated: `True`
- warning_count: `4`
- blocker_count: `0`
- warnings:
  - `R36 and R37 establish technical closure and boundary consolidation only; they do not authorize a full Bedrock Gate pass.`
  - `The remaining Bedrock Gate scope is still undefined in several places and requires explicit future gating.`
  - `Product, commercial, client, pricing, runtime, and Bedrock real execution remain forbidden.`
  - `Site claims remain limited to controlled-development language and cannot imply readiness or certification.`
- blockers:
  - `[]`
- recommended_next_phase: `F21-CTX-BEDROCK-R39 - Bedrock Gate Full Definition Charter`

# F21-CTX-BEDROCK-R37 - Bedrock Gate Closure Boundary Consolidation
- latest_completed_phase: `F21-CTX-BEDROCK-R37 - Bedrock Gate Closure Boundary Consolidation`
- phase_id: `F21-CTX-BEDROCK-R37`
- status: `bedrock_gate_closure_boundary_consolidated`
- decision: `pass`
- source_closure_phase: `F21-CTX-BEDROCK-R36`
- source_closure_status: `bedrock_evaluation_request_validation_runner_closure_passed`
- source_closure_decision: `pass`
- boundary_consolidation_created: `True`
- bedrock_gate_importance_preserved: `True`
- request_validation_runner_technical_closure_accepted: `True`
- full_bedrock_gate_pass_allowed: `False`
- product_pass_allowed: `False`
- commercial_approval_allowed: `False`
- client_readiness_allowed: `False`
- pricing_readiness_allowed: `False`
- runtime_activation_allowed: `False`
- bedrock_real_execution_allowed: `False`
- product_promotion_allowed: `False`
- site_marketing_claims_limited: `True`
- technical_pass_is_not_product_pass_preserved: `True`
- closure_pass_is_not_product_pass_preserved: `True`
- closure_pass_is_not_commercial_approval_preserved: `True`
- global_product_boundary_preserved: `True`
- boundary_matrix_created: `True`
- decision_locks_updated: `True`
- warning_count: `4`
- blocker_count: `0`
- warnings:
  - `R36 is a technical closure only; it does not authorize product or commercial readiness.`
  - `A Bedrock Gate component pass does not equal a full Bedrock Gate pass.`
  - `Product, commercial, client, pricing, runtime, and Bedrock real execution remain false.`
  - `Site marketing claims remain limited and cannot claim readiness or certification.`
- blockers:
  - `[]`
- recommended_next_phase: `F21-CTX-BEDROCK-R38 - Bedrock Gate Remaining Scope Inventory`

# Bedrock Evaluation Request Validation Runner Closure Gate
R36 closes the validation runner track as a technical pass only after the verified R30-R35 chain.
It does not reexecute the runner, does not authorize product or commercial readiness, and does not change any protected surfaces.

### Closure outcome
- `bedrock_evaluation_request_validation_runner_closure_passed`
- `closure_pass_is_not_product_pass=true`
- `closure_pass_is_not_commercial_approval=true`
- `technical_pass_is_not_product_pass_preserved=true`
- `global_product_boundary_preserved=true`
- `product_promotion_allowed=false`
- `commercial_use_allowed=false`
- `client_delivery_allowed=false`
- `pricing_allowed=false`
- `bedrock_runtime_gate_executed=false`
- `product_promotion_executed=false`

### Next phase
- `F21-CTX-BEDROCK-R37 - Bedrock Gate Closure Boundary Consolidation`

# Bedrock Evaluation Request Validation Runner Controlled Re-Execution
R34 re-executed the repaired runner against the real fixture tree and matched all 22 fixtures.
It preserved the tree hashes and count before and after, wrote official runner artifacts only under `artifacts/bedrock/runner/`, and kept product/commercial/runtime boundaries false.

### Re-execution outcome
- `runner_controlled_reexecution_passed`
- `fixtures_loaded=22`
- `fixtures_evaluated=22`
- `expected_files_loaded=22`
- `matched_fixture_count=22`
- `mismatched_fixture_count=0`
- `runner_executed_against_real_fixture_tree=true`
- `runner_artifacts_written=true`
- `fixture_tree_preserved=true`
- `fixture_tree_modified=false`
- `product_promotion_allowed_in_any_actual=false`
- `commercial_use_allowed_in_any_actual=false`
- `runner_execution_allowed_in_any_actual=false`
- `bedrock_runtime_gate_executed=false`
- `product_promotion_executed=false`

### Next phase
- `F21-CTX-BEDROCK-R35 - Bedrock Evaluation Request Validation Runner Re-Execution Review Gate`

# Bedrock Evaluation Request Validation Runner Targeted Mismatch Repair
R33 applies the targeted repair plan to the runner code only.
It repairs the 12 known semantic mismatches, preserves the real fixture tree, and does not execute a controlled re-run against the real tree.

### Repair outcome
- `runner_targeted_mismatch_repair_implemented`
- `planned_repair_count=12`
- `implemented_repair_count=12`
- `targeted_fixture_count=12`
- `repair_implementation_executed=true`
- `controlled_real_fixture_rerun_executed=false`
- `runner_validation_still_requires_r34=true`
- `product_promotion_allowed=false`
- `commercial_use_allowed=false`
- `bedrock_runtime_gate_executed=false`
- `runner_execution_allowed=false`

### Next phase
- `F21-CTX-BEDROCK-R34 - Bedrock Evaluation Request Validation Runner Controlled Re-Execution`

# Bedrock Evaluation Request Validation Runner Controlled Execution
R30 executed the deterministic runner against the real materialized fixture tree in dry-run mode only.
The run preserved the manifest hash, file-list hash, and content hash, and kept the fixture tree at 45 JSON files before and after execution.
It wrote official runner artifacts only under `artifacts/bedrock/runner/`.
It did not emit a Bedrock verdict, did not promote product, did not use network, and did not mutate the fixture tree.

### Execution outcome
- `runner_controlled_execution_failed`
- 22 fixtures loaded
- 22 fixtures evaluated
- 22 expected files loaded
- 10 fixtures matched
- 12 fixtures mismatched
- product/commercial allowed remained false
- runner execution allowed remained false
- tree preservation hashes matched before/after

### Next phase
- `F21-CTX-BEDROCK-R31 - Bedrock Evaluation Request Validation Runner Controlled Execution Review Gate`

# Bedrock Evaluation Request Validation Runner Controlled Execution Plan
R29 defines how the future controlled execution phase will run the deterministic runner against the real materialized fixture tree in dry-run mode.
It selects a dedicated R30 script to keep implementation smoke separate from real-tree execution planning.
It does not execute the runner, it does not emit a Bedrock verdict, and it does not allow product/commercial approval, runtime access, network access, or fixture mutation.

### Planned execution contract
- read `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`
- evaluate the 22 input/expected pairs materialized in R22 and reviewed in R23
- keep `dry_run_only=true`
- keep `allow_real_bedrock=false`
- keep `allow_runtime_access=false`
- keep `allow_network=false`
- keep `allow_fixture_mutation=false`
- keep `allow_product_promotion=false`
- keep `allow_commercial_use=false`

### Planned execution strategy
- use a dedicated R30 script: `scripts/run_f21_ctx_bedrock_r30_evaluation_request_validation_runner_controlled_execution.py`
- keep outputs inside `artifacts/bedrock/runner/`
- preserve the fixture tree hash and count before and after execution
- treat mismatches as controlled failures, not product signals

### Next phase
- `F21-CTX-BEDROCK-R30 - Bedrock Evaluation Request Validation Runner Controlled Execution`

# Bedrock Evaluation Request Validation Runner Controlled Implementation Review Gate
R28 reviews the controlled implementation of the Bedrock request-validation runner.
It confirms the module, script, and tests exist; the code is deterministic and stdlib-only; the smoke path stayed temporary; and the real fixture tree was not executed or modified.

### Review outcome
- `runner_controlled_implementation_review_passed`
- module, script, and tests exist
- import safety review passed
- guard review passed
- deterministic rules review passed
- mismatch policy review passed
- test review passed
- script smoke review passed
- real fixture tree preserved
- no Bedrock verdict emitted

### Next phase
- `F21-CTX-BEDROCK-R29 - Bedrock Evaluation Request Validation Runner Controlled Execution Plan`

# Bedrock Evaluation Request Validation Runner Controlled Implementation
R27 implements the deterministic runner in a controlled, stdlib-only form.
It creates the module, script, and tests, runs only a temporary smoke tree, and does not execute the materialized Bedrock tree.

### Implementation outcome
- `runner_controlled_implementation_ready`
- module, script, and tests created
- temporary fixture smoke used
- real fixture tree preserved
- no Bedrock verdict emitted
- no product/commercial allowance

### Next phase
- `F21-CTX-BEDROCK-R28 - Bedrock Evaluation Request Validation Runner Controlled Implementation Review Gate`

# Bedrock Evaluation Request Validation Runner Controlled Implementation Plan
R26 defines the exact controlled implementation plan for the future runner.
It specifies the module paths, runner API, deterministic rules, non-execution enforcement, test plan, artifact write policy, and rollback/cleanup policy, but it does not implement code or execute a runner.

### Planned implementation contract
- future module path: `src/aris/bedrock/evaluation_request_validation_runner.py`
- future script path: `scripts/run_f21_ctx_bedrock_r27_evaluation_request_validation_runner_dry_run.py`
- future test path: `tests/test_f21_ctx_bedrock_r27_evaluation_request_validation_runner_dry_run.py`
- future artifact paths under `artifacts/bedrock/runner/`

### Planned runner API
- `EvaluationRequestValidationRunner`
- `load_manifest(path)`
- `load_fixture_pair(fixture_id)`
- `validate_fixture_tree()`
- `validate_non_execution_guarantee(fixture)`
- `evaluate_request_against_r17_rules(fixture)`
- `compare_actual_to_expected(actual, expected)`
- `run_dry_run()`
- `write_runner_artifacts(result)`

### Deterministic execution plan
- manifest load
- fixture count validation
- unique ID validation
- input/expected loading
- pairing validation
- non-execution guarantee validation
- R17 rule classification
- actual vs expected comparison
- mismatch recording
- pass/warn/fail consolidation
- preserve false product/commercial/runner flags

### Enforcement and blocking
- no runtime access
- no network access
- no LLM-as-judge
- no fixture mutation
- no product/commercial allowance
- no real Bedrock verdict
- no writing outside `artifacts/bedrock/runner/`

### Future implementation gates
- `F21-CTX-BEDROCK-R27 - Bedrock Evaluation Request Validation Runner Controlled Implementation`
- `F21-CTX-BEDROCK-R28 - Bedrock Evaluation Request Validation Runner Controlled Implementation Review Gate`
- `F21-CTX-BEDROCK-R29 - Bedrock Evaluation Request Validation Runner Controlled Execution Plan`

### Next phase
- `F21-CTX-BEDROCK-R27 - Bedrock Evaluation Request Validation Runner Controlled Implementation`

# BEDROCK_GATE — Chão Inviolável do ARIS

## Bedrock Evaluation Request Validation Runner Controlled Execution Review Gate
R32 creates the mismatch repair plan from the validated R30/R31 evidence and does not modify the runner.
It preserves the failure state, classifies the 12 mismatches, and prepares R33 for targeted repair only.

### Plan outcome
- `runner_mismatch_repair_plan_ready`
- `r31_failure_confirmed`
- `repair_plan_created`
- `repair_implementation_executed=false`
- `runner_validation_still_failing=true`
- `planned_repair_count=12`
- `affected_fixture_count=12`
- `product_promotion_allowed=false`
- `commercial_use_allowed=false`
- `bedrock_runtime_gate_executed=false`
- `runner_execution_allowed=false`

### Next phase
- `F21-CTX-BEDROCK-R33 - Bedrock Evaluation Request Validation Runner Targeted Mismatch Repair`

## Bedrock Evaluation Request Validation Runner Controlled Execution Review Gate
R31 reviews the R30 controlled execution evidence and confirms the failure is a valid semantic mismatch failure rather than a safety violation.
It does not repair the runner, does not promote product, and does not change the fixture tree.

### Review outcome
- `runner_controlled_execution_review_failed_valid`
- R30 failure confirmed as real
- failure cause is mismatch-driven, not safety-driven
- fixture tree preservation intact
- R32 must be a mismatch repair plan

### Next phase
- `F21-CTX-BEDROCK-R32 - Bedrock Evaluation Request Validation Runner Mismatch Repair Plan`

## Bedrock Evaluation Request Validation Runner Dry-Run Plan Review Gate
R25 reviews the R24 runner plan and confirms it is safe and complete enough to allow a future controlled implementation plan.
It checks boundaries, algorithm coverage, schemas, mismatch policy, and fixture-tree protection, but it does not implement or execute a runner.

### Review outcome
- `runner_dry_run_plan_review_passed`
- R24 plan found and verified
- boundary review passed
- algorithm review passed
- schema review passed
- mismatch policy review passed
- fixture tree preserved
- no runner implementation or execution

### Next phase
- `F21-CTX-BEDROCK-R26 - Bedrock Evaluation Request Validation Runner Controlled Implementation Plan`

## Bedrock Evaluation Request Validation Runner Dry-Run Plan
R24 plans the future deterministic runner dry-run that will compare actual request-validation output against the expected fixture files.
It defines purpose, boundaries, inputs, algorithm, output schemas, mismatch policy, artifact paths, and risk blocks for implementation, but it does not implement or execute a runner.

### Planned runner contract
- read `fixture_manifest.json`
- load the 22 input fixtures
- load the 22 expected files
- apply R17 deterministic rules
- compare actual vs expected
- generate dry-run summary/report artifacts
- keep product/commercial/runner false throughout

### Implementation blocks
- R23 must be passed and reviewed
- fixture tree must remain consistent
- expected files must not declare product/commercial true
- runner must not write into the fixture tree
- runner must not import runtime or access network
- runner must not use LLM-as-judge
- runner must not create a real Bedrock verdict

### Next phase
- `F21-CTX-BEDROCK-R25 - Bedrock Evaluation Request Validation Runner Dry-Run Plan Review Gate`

## Bedrock Evaluation Request Fixture Controlled Materialization Review Gate
R23 reviews the controlled fixture tree materialized in R22 and confirms that it is safe and coherent for a future runner dry-run phase.
It checks tree integrity, manifest consistency, input/expected pairing, positive/negative coverage, non-execution invariants, and safety scan results.
It does not create a runner, validate real requests, or execute Bedrock.

### Review outcome
- `fixture_materialization_review_passed`
- 45 JSON files reviewed
- 22 input fixtures reviewed
- 22 expected fixtures reviewed
- 5 positive fixtures reviewed
- 17 negative fixtures reviewed
- product/commercial allowed is false in every fixture
- runner execution is false in every fixture
- non-execution guarantees preserved
- no runtime, frontend, backend, action runtime, voice, network, or dependency mutation

### Next phase
- `F21-CTX-BEDROCK-R24 - Bedrock Evaluation Request Validation Runner Dry-Run Plan`

# Bedrock Evaluation Request Fixture Controlled Materialization
R22 materializes the controlled fixture tree only.
It writes the manifest plus 22 input fixtures and 22 expected fixtures, but it does not create a runner, execute Bedrock, or authorize product promotion.

### Materialized tree
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`

### Materialization guarantees
- 22 fixtures materialized
- 5 positive fixtures materialized
- 17 negative fixtures materialized
- product/commercial allowed is false in every expected file
- runner execution is false in every expected file
- non-execution guarantees preserved
- no runtime, frontend, backend, action runtime, voice, network, or dependency mutation

### Next phase
- `F21-CTX-BEDROCK-R23 - Bedrock Evaluation Request Fixture Controlled Materialization Review Gate`

## Bedrock Evaluation Request Fixture Materialization Dry-Run Gate
Este gate dry-run valida se a materialização futura dos 22 fixtures Bedrock pode prosseguir com segurança.
Ele não materializa fixtures reais, não cria runner, não executa Bedrock real e não valida requests reais.

### Manifest readiness
- manifesto R19 existe e está coerente
- `fixture_count=22`
- `positive_fixture_count=5`
- `negative_fixture_count=17`
- IDs únicos planejados
- categorias válidas
- expected outcome rules preservadas
- nenhum fixture planejado permite `product/commercial allowed=true`

### Plan readiness
- paths futuros definidos
- batches definidos
- templates definidos
- validações futuras definidas
- bloqueios definidos
- materialização ainda não executada
- `fixtures_materialized=false`

### Dry-run materialization preview
O gate registra uma prévia determinística com:
- 22 fixture IDs
- batch de cada fixture
- path futuro planejado para input
- path futuro planejado para expected
- expected validation status
- expected rejection IDs
- product/commercial flags esperadas como false
- non-execution guarantee

### Readiness decision
Status possíveis:
- `fixture_materialization_dry_run_ready`
- `fixture_materialization_dry_run_warn`
- `fixture_materialization_dry_run_blocked`

Condições para `ready`:
- R18, R19 e R20 presentes ou suficientemente refletidos no active-context
- 22 fixtures planejados
- 5 positivos
- 17 negativos
- nenhum fixture com expected product/commercial true
- todos negativos com rejection ID planejado
- paths futuros dentro de `artifacts/bedrock/fixtures/evaluation_requests/`
- templates de input/expected definidos
- non-execution invariants preservadas
- nenhuma materialização real feita no R21

Condições para `warn`:
- lacuna documental menor, mas sem risco de product pass falso
- fixture coverage incompleta em uma dimensão não crítica
- report precisa de revisão antes de materializar

Condições para `blocked`:
- fixture count divergente
- IDs duplicados
- product/commercial allowed true
- negativo sem rejection ID
- path fora do diretório permitido
- runner execution enabled
- rede/runtime/dependency/mutação real envolvida
- active-context não lido
- R19/R20 ausentes ou contraditórios

### Validation checklist
- count check
- unique ID check
- category check
- batch assignment check
- future path check
- expected result check
- negative rejection ID check
- product/commercial false check
- non-execution guarantee check
- protected sources unchanged check
- no fixture tree created check

### Output esperado
Campos mínimos do summary:
- `phase`
- `status`
- `decision`
- `dry_run_gate_created`
- `fixtures_materialized`
- `fixture_tree_created`
- `fixture_count_previewed`
- `positive_fixture_count_previewed`
- `negative_fixture_count_previewed`
- `duplicate_fixture_ids_detected`
- `invalid_fixture_paths_detected`
- `product_promotion_allowed_in_any_fixture`
- `commercial_use_allowed_in_any_fixture`
- `negative_fixture_without_rejection_id_detected`
- `runner_execution_allowed`
- `runtime_modified`
- `frontend_modified`
- `backend_modified`
- `action_runtime_modified`
- `voice_modified`
- `network_enabled`
- `dependencies_installed`
- `next_recommended_phase`

### Artifact report
O report R21 deve incluir:
- objetivo do R21
- relação com R18/R19/R20
- preview dos batches
- principais checks
- decisão final
- bloqueios preservados
- próxima fase

### Relação com R16-R20
- R18 define schema de fixtures
- R19 define manifesto
- R20 define materialization plan
- R21 valida dry-run readiness para materialização
- R21 não materializa fixtures
- R21 não cria runner
- R21 não executa Bedrock real

### Boundary statement
R21 é um gate dry-run apenas.
Ele autoriza apenas o próximo passo de materialização controlada, nunca execução real ou product pass.

## Plano de materialização controlada de fixtures dry-run
Este plano define como os 22 fixtures futuros do manifesto serão materializados com segurança em uma fase posterior.
Ele não materializa fixtures reais, não cria runner, não executa validação real e não autoriza Bedrock product pass.

### Objetivo da materialização
Materialização futura significa criar arquivos JSON pequenos, auditáveis e determinísticos para cada fixture listado no manifesto R19.
Materialização não é execução.
Materialização não valida request real.
Materialização não cria Evidence Bundle real.
Materialização não cria Verdict Artifact real.
Materialização não altera runtime.
Materialização não permite produto.

### Estratégia de materialização
Sequência planejada:
- confirmar manifesto R19
- criar diretório futuro de fixtures
- criar `fixture_manifest.json`
- criar `<fixture_id>.json` para cada input fixture
- criar `<fixture_id>_expected.json` para cada expected result
- validar JSON syntax
- validar IDs únicos
- validar categorias contra schema R18
- validar expected statuses contra R17
- validar que product/commercial allowed são sempre false
- validar non-execution invariants
- gerar summary/report da materialização

### Paths futuros
Os caminhos futuros propostos são:
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`
- `artifacts/bedrock/fixtures/evaluation_requests/materialization_summary.json`
- `artifacts/bedrock/fixtures/evaluation_requests/materialization_report.md`

R20 não cria essa árvore ainda.

### Ordem de materialização
Primeiro batch positivo:
- `valid_lab_continuation_partial_evidence`
- `valid_technical_readiness_no_product_pass`
- `valid_product_candidate_with_conditions`
- `valid_safety_blocker_review_partial_evidence`
- `valid_evidence_completeness_review_no_product_pass`

Segundo batch crítico negativo:
- `invalid_product_promotion_without_evidence_bundle`
- `invalid_product_promotion_without_blocker_scan`
- `invalid_product_promotion_without_human_review`
- `invalid_runtime_change_without_boundary_evidence`
- `invalid_real_mutation_without_rollback_evidence`
- `invalid_llm_as_sole_judge_requested`
- `invalid_attempt_to_skip_completeness_gate`
- `invalid_attempt_to_skip_blocker_scan`
- `invalid_attempt_to_promote_lab_only_to_product`

Terceiro batch estrutural negativo:
- `invalid_missing_target_id`
- `invalid_missing_target_type`
- `invalid_target_type_unknown`
- `invalid_missing_source_commit`
- `invalid_source_of_truth_contradictory`
- `invalid_dirty_worktree_without_notes`
- `invalid_commercial_delivery_without_risk_register`
- `invalid_commercial_delivery_without_known_limits`

### Templates futuros
Template mínimo de `<fixture_id>.json`:
- `fixture_id`
- `fixture_schema_version`
- `fixture_category`
- `fixture_priority`
- `input_request`
- `mock_source_state`
- `mock_evidence_references`
- `mock_source_of_truth_state`
- `mock_boundary_state`
- `mock_risk_state`
- `mock_human_review_state`
- `mock_non_goal_assertions`
- `non_execution_guarantee`

Template mínimo de `<fixture_id>_expected.json`:
- `fixture_id`
- `expected_validation_status`
- `expected_rejection_ids`
- `expected_warning_ids`
- `expected_lab_continuation_allowed`
- `expected_product_promotion_allowed`
- `expected_commercial_use_allowed`
- `expected_validation_layers`
- `expected_required_remediations`
- `expected_next_allowed_scope`
- `expected_blocked_scope`
- `human_review_required`
- `runner_execution_allowed`

Regras:
- `expected_product_promotion_allowed` deve ser false em todos os fixtures
- `expected_commercial_use_allowed` deve ser false em todos os fixtures
- `runner_execution_allowed` deve ser false no plano R20

### Validações futuras planejadas
- JSON syntax para todos os arquivos
- fixture IDs únicos
- fixture count = 22
- positive count = 5
- negative count = 17
- categorias válidas
- expected statuses válidos
- rejection IDs presentes nos negativos
- product/commercial allowed sempre false
- non-execution guarantee presente em todos
- nenhum segredo real
- nenhuma rede
- nenhuma referência a runtime produtivo
- paths dentro de `artifacts/bedrock/fixtures/evaluation_requests`
- manifesto cobre todos os fixtures

### Bloqueios da futura materialização
- manifesto R19 ausente
- schema R18 ausente
- fixture ID duplicado
- expected result ausente
- fixture positivo declarando product pass
- fixture negativo sem rejection ID
- qualquer fixture com `commercial_use_allowed=true`
- qualquer fixture com `product_promotion_allowed=true`
- qualquer fixture com `runner_execution_allowed=true`
- fixture usando segredo real
- fixture exigindo rede
- fixture apontando para mutação real
- fixture fora do path permitido
- active-context não lido

### Relação com runner futuro
- R20 só planeja materialização
- fase futura pode materializar fixtures
- fase posterior poderá criar runner dry-run
- runner futuro deverá ler fixture + expected, aplicar R17 e comparar output
- runner futuro deve permanecer deterministic-only
- runner futuro não pode executar Bedrock real nem emitir product verdict

### R20 boundary statement
R20 define o plano de materialização apenas.
Ele não materializa fixtures reais, não cria runner e não executa Bedrock.

## Draft do manifesto de fixtures dry-run de request
Este draft define o manifesto canônico dos fixtures simulados que serão usados futuramente para testar as regras de validação do request sem executar o Bedrock real.
Ele não materializa fixtures reais, não valida requests reais, não promove produto e não cria veredito real.

### Identidade do manifesto
Campos obrigatórios:
- `manifest_id`
- `manifest_schema_version`
- `bedrock_gate_version`
- `created_for_phase`
- `created_at`
- `created_by`
- `fixture_schema_version`
- `validation_rules_version`
- `input_contract_version`
- `fixture_count`
- `positive_fixture_count`
- `negative_fixture_count`
- `coverage_targets`
- `non_execution_guarantee`

### Estrutura de cada fixture
Cada fixture do manifesto deve ter:
- `fixture_id`
- `fixture_name`
- `fixture_category`
- `fixture_priority`
- `target_type`
- `requested_verdict_scope`
- `expected_validation_status`
- `expected_rejection_ids`
- `expected_warning_ids`
- `expected_lab_continuation_allowed`
- `expected_product_promotion_allowed`
- `expected_commercial_use_allowed`
- `covered_validation_layers`
- `covered_rejection_rules`
- `covered_target_rules`
- `covered_scope_rules`
- `requires_human_review_mock`
- `requires_rollback_mock`
- `requires_boundary_mock`
- `requires_evidence_bundle_mock`
- `requires_blocker_scan_mock`
- `future_fixture_path`
- `future_expected_path`

### Prioridades
As prioridades canônicas são:
- `critical`
- `high`
- `medium`
- `low`

Regras:
- fixtures que cobrem product promotion indevida devem ser `critical`
- fixtures que cobrem commercial delivery indevida devem ser `critical`
- fixtures que cobrem runtime/network/action runtime/real mutation sem rollback devem ser `critical`
- fixtures positivos Lab-only podem ser `medium` ou `high`
- fixtures de documentação/cobertura complementar podem ser `low`

### Conjunto mínimo de fixtures
O manifesto define 22 fixtures no total, com 5 positivos e 17 negativos.

Positivos:
- `valid_lab_continuation_partial_evidence`
- `valid_technical_readiness_no_product_pass`
- `valid_product_candidate_with_conditions`
- `valid_safety_blocker_review_partial_evidence`
- `valid_evidence_completeness_review_no_product_pass`

Negativos:
- `invalid_missing_target_id`
- `invalid_missing_target_type`
- `invalid_target_type_unknown`
- `invalid_missing_source_commit`
- `invalid_product_promotion_without_evidence_bundle`
- `invalid_product_promotion_without_blocker_scan`
- `invalid_product_promotion_without_human_review`
- `invalid_runtime_change_without_boundary_evidence`
- `invalid_real_mutation_without_rollback_evidence`
- `invalid_commercial_delivery_without_risk_register`
- `invalid_commercial_delivery_without_known_limits`
- `invalid_source_of_truth_contradictory`
- `invalid_dirty_worktree_without_notes`
- `invalid_llm_as_sole_judge_requested`
- `invalid_attempt_to_skip_completeness_gate`
- `invalid_attempt_to_skip_blocker_scan`
- `invalid_attempt_to_promote_lab_only_to_product`

### Coverage matrix
O manifesto deve cobrir:
- todas as validation layers do R17
- todos os requested scopes do R16/R17
- todos os target types do R16/R17/R15
- todas as hard-block rejection rules canônicas
- as invariantes de nao execucao

### Expected outcome rules
Regras obrigatórias:
- nenhum fixture pode declarar `expected_product_promotion_allowed=true`
- nenhum fixture pode declarar `expected_commercial_use_allowed=true`
- fixtures positivos podem ser aceitos para Bedrock evaluation, mas nunca como product pass
- fixtures Lab-only devem manter product promotion false
- fixtures negativos devem ter ao menos um rejection ID
- commercial delivery sem human review, risk register ou known limits deve ser blocked
- runtime/action runtime/network/real mutation sem boundary ou rollback deve ser blocked
- LLM-as-sole-judge deve ser blocked
- attempts to skip completeness gate or blocker scan devem ser blocked

### Future runner relation
Um runner determinístico futuro deve:
- ler o manifesto
- carregar um fixture por vez
- aplicar as regras do R17
- comparar a saida com o esperado
- permanecer dry-run only
- não executar runtime
- não chamar rede
- não criar veredito real
- emitir apenas artifact de dry-run

### Future paths
Os caminhos futuros propostos são:
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`

R19 define o manifesto apenas.
Ele não materializa os fixtures, não executa runner e não avalia Bedrock.

## Draft de schema de dry-run fixtures de validação de request
Este draft define fixtures simulados para testar as regras de validação do request sem executar o Bedrock real.
Ele não valida requests reais, não promove produto e não cria veredito real.

### Identidade do fixture
Campos obrigatórios:
- `fixture_id`
- `fixture_schema_version`
- `bedrock_gate_version`
- `fixture_name`
- `fixture_description`
- `fixture_category`
- `target_type`
- `requested_verdict_scope`
- `expected_validation_status`
- `expected_rejection_ids`
- `expected_warning_ids`
- `expected_lab_continuation_allowed`
- `expected_product_promotion_allowed`
- `expected_commercial_use_allowed`
- `created_for_phase`
- `source_phase`
- `non_execution_guarantee`

### Categorias de fixture
Categorize fixtures as:
- `valid_lab_only_request`
- `valid_technical_readiness_request`
- `valid_product_candidate_request_with_conditions`
- `invalid_missing_target`
- `invalid_missing_source_commit`
- `invalid_product_scope_without_evidence_bundle`
- `invalid_product_scope_without_blocker_scan`
- `invalid_product_scope_without_human_review`
- `invalid_runtime_change_without_boundary_evidence`
- `invalid_real_mutation_without_rollback_evidence`
- `ambiguous_target_request`
- `stale_source_of_truth_request`
- `contradictory_source_of_truth_request`
- `dirty_worktree_without_notes_request`
- `llm_as_sole_judge_requested`
- `attempt_to_skip_completeness_gate`
- `attempt_to_skip_blocker_scan`
- `attempt_to_promote_lab_only_result_to_product`
- `commercial_scope_without_risk_register`
- `commercial_scope_without_known_limits`

### Fixture payload structure
Cada fixture deve conter:
- `input_request`
- `mock_source_state`
- `mock_evidence_references`
- `mock_source_of_truth_state`
- `mock_boundary_state`
- `mock_risk_state`
- `mock_human_review_state`
- `mock_non_goal_assertions`
- `expected_validation_result`
- `expected_remediations`
- `expected_next_allowed_scope`
- `expected_blocked_scope`

### Input request
Use the R16 request fields:
- `evaluation_request_id`
- `request_schema_version`
- `bedrock_gate_version`
- `requested_at`
- `requested_by`
- `request_reason`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `requested_verdict_scope`
- `requested_output_artifacts`
- `source_repositories`
- `source_commits`
- `source_branch`
- `worktree_state`

### Expected validation result
Each fixture must declare:
- `validation_status`
- `accepted_for_bedrock_evaluation`
- `accepted_for_lab_only`
- `accepted_for_product_scope`
- `accepted_for_commercial_scope`
- `rejection_reasons`
- `warning_reasons`
- `missing_inputs`
- `required_remediations`
- `required_next_artifacts`
- `human_review_required`
- `next_recommended_phase`

Positive fixtures must preserve the rule that a valid request does not imply Product Ready.

### Positive fixture classes
- lab continuation request valid with partial evidence
- technical readiness request valid without product pass
- product candidate request valid with conditions
- safety blocker review valid with partial evidence
- evidence completeness review valid without product pass

### Negative fixture classes
- target absent
- target_type invalid
- source commit absent
- product promotion without Evidence Bundle
- product promotion without blocker scan
- commercial delivery without human review
- runtime change without boundary evidence
- real mutation without rollback evidence
- source-of-truth contradictory
- LLM-as-sole-judge attempt
- completeness gate skip attempt
- Lab-only to product promotion attempt

### Fixture invariants
- no runtime execution
- no network call
- no real file mutation
- no real verdict creation
- no real Evidence Bundle creation
- no frontend/backend/action runtime/voice mutation
- no dependency installation
- no secret use
- no Obsidian bulk-read
- small and auditable
- usable by a future deterministic runner

### Relationship to R16 and R17
- R16 defines the request contract.
- R17 defines the request validation rules.
- R18 defines dry-run fixtures for testing those rules.
- R18 does not execute validation real or substitute the real Bedrock stack.

### Future fixture paths
Proposed future paths:
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`

R18 does not create the future tree yet; it only defines the schema.

## Draft de regras de validação da solicitação de avaliação
Este draft define as regras determinísticas que validam uma solicitação Bedrock antes de qualquer completeness gate, blocker scan ou verdict futuro.
Ele não executa o Bedrock real, não promove produto e não substitui R16.

### Camadas de validação
As camadas obrigatórias são:
- `identity_validation`
- `target_validation`
- `scope_validation`
- `source_state_validation`
- `evidence_reference_validation`
- `source_of_truth_validation`
- `boundary_validation`
- `risk_validation`
- `human_review_validation`
- `non_goal_validation`
- `rejection_reason_validation`

Cada camada deve registrar objetivo, campos exigidos, critérios de aprovação, critérios de rejeição, status possível e remediação mínima.

### Estados de validação
Estados canônicos:
- `input_valid`
- `input_incomplete`
- `input_invalid`
- `input_ambiguous`
- `input_stale`
- `input_contradictory`
- `input_product_scope_blocked`
- `input_requires_human_review`
- `input_lab_only_allowed`

### Regras por escopo
- `lab_continuation_only`: aceita evidência parcial, mas marca `product_promotion_allowed=false`.
- `technical_readiness_only`: nunca emite product pass.
- `product_candidate_review`: exige evidence bundle referenciado; lacunas documentadas podem existir.
- `product_promotion_review`: exige evidence bundle, completeness gate e blocker scan.
- `commercial_delivery_review`: exige evidence bundle completo, blocker scan completo, human review explícita, risk register e known limits.
- `runtime_change_review`: exige boundary evidence e rollback/recovery evidence.
- `safety_blocker_review`: pode iniciar com evidência parcial, mas nunca libera produto sozinho.
- `evidence_completeness_review`: valida completude, não produto.

### Regras por target type
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change` exigem boundary evidence.
- Mudanças mutantes reais exigem rollback/recovery evidence.
- Candidatos produto exigem Evidence Bundle, blocker scan, source-of-truth atualizado e human review.
- Candidatos comerciais exigem risk register, known limits, UX evidence, cost/performance evidence e human review.
- `phase`, `capability` e `macroblock` podem ser Lab-only se o escopo for limitado.

### Rejeições hard-block
Rejeições canônicas:
- `missing_target_id`
- `missing_target_type`
- `invalid_target_type`
- `missing_requested_scope`
- `invalid_requested_scope`
- `missing_source_commit`
- `missing_source_repository`
- `missing_active_context_read_evidence`
- `stale_or_contradictory_source_of_truth`
- `dirty_worktree_without_notes`
- `product_scope_without_evidence_bundle`
- `product_scope_without_blocker_scan`
- `product_scope_without_human_review`
- `runtime_change_without_boundary_evidence`
- `real_mutation_without_rollback_evidence`
- `commercial_scope_without_known_limits`
- `commercial_scope_without_risk_register`
- `llm_as_sole_judge_requested`
- `attempt_to_skip_completeness_gate`
- `attempt_to_skip_blocker_scan`
- `attempt_to_use_memory_against_active_context`
- `attempt_to_promote_lab_only_result_to_product`

### Source-of-truth validation
Request validation must prove:
- active-context was read;
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `CONTEXT_INDEX.md`, `ARIS_PHASE_LEDGER.md` were considered;
- `BEDROCK_GATE.md` was considered;
- stale/conflicting context was recorded;
- Obsidian was either not used or explicitly not used;
- stale memory was not used against active source-of-truth.

### Worktree and repo state validation
Request validation must record:
- branch
- commit
- remote status
- dirty worktree
- staged changes
- unrelated changes preserved
- source repo separated from active-context repo
- push status

Worktree dirtiness does not automatically block Lab, but blocks product-grade unless scoped notes exist and diffs are bounded.

### Future output schema
Future validation output should contain:
- `phase`
- `evaluation_request_id`
- `request_schema_version`
- `target_id`
- `target_type`
- `requested_verdict_scope`
- `validation_status`
- `validation_layers`
- `accepted_for_bedrock_evaluation`
- `accepted_for_lab_only`
- `accepted_for_product_scope`
- `rejection_reasons`
- `warning_reasons`
- `missing_inputs`
- `required_remediations`
- `required_next_artifacts`
- `human_review_required`
- `next_recommended_phase`

### Relation to R10-R16
- R16 defines the contract of the request.
- R17 defines the deterministic validation rules for that request.
- R17 decides whether evaluation may start.
- R17 does not run completeness, blocker scan, or verdict artifact logic.
- R17 does not imply product pass.

## Draft de contrato de entrada da avaliação
Este draft define o formato mínimo de uma solicitação Bedrock válida antes que qualquer avaliação futura possa começar.
Ele não executa a avaliação, não promove produto e não substitui as camadas R12 a R15.

### Identidade da solicitação
Campos obrigatórios:
- `evaluation_request_id`
- `request_schema_version`
- `bedrock_gate_version`
- `requested_at`
- `requested_by`
- `request_reason`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `requested_verdict_scope`
- `requested_output_artifacts`
- `source_repositories`
- `source_commits`
- `source_branch`
- `worktree_state`

### Tipos de alvo aceitos
O contrato consolida os `target_type` canônicos de R12/R13/R15:
- `phase`
- `capability`
- `macroblock`
- `runtime_change`
- `frontend_change`
- `backend_change`
- `action_runtime_change`
- `voice_change`
- `network_change`
- `product_release_candidate`
- `commercial_delivery_candidate`

Regras por classe:
- `phase`, `capability`, `macroblock`: podem pedir `lab_continuation_only`, `technical_readiness_only` e `evidence_completeness_review`; promoção de produto exige bundle completo, completeness e blocker scan quando aplicável.
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change`: exigem boundary evidence, rollback/recovery evidence, source-of-truth references e human review para escopo product-grade.
- `product_release_candidate`, `commercial_delivery_candidate`: exigem bundle completo, completeness gate completo, blocker scan completo e human review explícita; não podem ser tratados como lab-only.

### Escopos de veredito aceitos
`requested_verdict_scope` deve ser um destes valores:
- `lab_continuation_only`
- `technical_readiness_only`
- `product_candidate_review`
- `product_promotion_review`
- `commercial_delivery_review`
- `runtime_change_review`
- `safety_blocker_review`
- `evidence_completeness_review`

Regras:
- `product_promotion_review` exige Evidence Bundle completo.
- `commercial_delivery_review` exige Evidence Bundle completo, blocker scan completo e human review explícita.
- `runtime_change_review` exige boundary evidence e rollback/recovery evidence.
- `safety_blocker_review` pode começar com evidência parcial, mas não pode liberar produto sem completude.
- `lab_continuation_only` nunca deve ser confundido com product pass.

### Inputs obrigatórios
Todo request deve referenciar:
- `target_identity`
- `requested_scope`
- `evidence_bundle_reference`
- `technical_artifact_references`
- `source_of_truth_references`
- `validation_references`
- `risk_references`
- `blocker_scan_reference`
- `human_review_reference`
- `known_limitations`
- `dirty_worktree_notes`
- `protected_sources_assertion`
- `non_goal_assertions`

### Regras de rejeição
O request deve ser rejeitado antes do início da avaliação se:
- o target estiver ausente ou ambíguo;
- o `target_type` for inválido;
- faltar source commit;
- faltar Evidence Bundle para escopo product-grade;
- faltar blocker scan para escopo product-grade;
- o active-context não tiver sido lido;
- houver source-of-truth contraditório sem reconciliação;
- o worktree estiver sujo sem nota;
- houver tentativa de promover produto com evidência parcial;
- houver tentativa de pular completeness gate;
- houver tentativa de pular blocker scan;
- houver tentativa de usar LLM como juiz único;
- houver tentativa de usar memória histórica contra active-context;
- houver tentativa de avaliar mutação real sem rollback;
- houver tentativa de avaliar comercialmente sem human review.

### Input status
Estados possíveis:
- `input_valid`: a solicitação pode iniciar a avaliação futura, mas não implica product pass.
- `input_incomplete`: faltam campos ou referências obrigatórias; pode permitir continuidade Lab, não produto.
- `input_invalid`: o request quebra o contrato, está malformado ou impossível de auditar.
- `input_ambiguous`: o alvo, escopo ou pedido não estão suficientemente definidos.
- `input_stale`: o request referencia estado ou evidência ultrapassados.
- `input_contradictory`: a solicitação contradiz source-of-truth ou evidência materializada.
- `input_product_scope_blocked`: há bloqueio absoluto ou falta de evidência para escopo product-grade.
- `input_requires_human_review`: a avaliação só pode prosseguir com revisão humana explícita.
- `input_lab_only_allowed`: apenas continuidade Lab é permitida.

### Segurança e boundaries
Os campos booleanos a seguir devem sempre ser acompanhados de evidência referenciável, nunca apenas declaração:
- `runtime_modified`
- `frontend_modified`
- `backend_modified`
- `action_runtime_modified`
- `voice_modified`
- `network_enabled`
- `dependencies_installed`
- `productive_path_changed`
- `product_promotion_requested`
- `commercial_use_requested`
- `human_review_required`
- `rollback_required`
- `bedrock_runtime_gate_requested`

Regras:
- declaração booleana sem evidência não basta para escopo product-grade;
- qualquer mutação real exige rollback/recovery evidence;
- qualquer uso comercial exige human review explícita;
- qualquer mudança em runtime, produto ou boundary exige evidência de fronteira.

### Relação com R12-R15
- R12 define o Evidence Bundle.
- R13 define se o Evidence Bundle está completo.
- R14 define blocker scan.
- R15 define o artefato final de veredito.
- R16 apenas valida se a solicitação pode iniciar a avaliação.
- Um request válido não implica Evidence Bundle completo.
- Um request válido não implica Product Ready.

### Futuro artifact path
Proposta para fases futuras:
- `artifacts/bedrock/evaluation_inputs/<target_id>_bedrock_evaluation_input.json`
- `artifacts/bedrock/evaluation_inputs/<target_id>_bedrock_evaluation_input_report.md`

R16 não cria essa árvore agora; apenas documenta o contrato de entrada.

## Função
O Bedrock Gate é a primeira camada obrigatória de aprovação de qualquer fase, arquitetura, prompt Codex, feature, refactor, roadmap ou decisão operacional do ARIS.

Ele responde uma pergunta simples:

> Esta decisão viola alguma fundação inviolável do ARIS?

Se a resposta for sim, o resultado deve ser `BLOCKED`, mesmo que testes locais, artifacts, revisão humana ou gates específicos da fase pareçam passar.

## Ordem obrigatória de aprovação
Toda fase futura deve ser avaliada nesta ordem:

1. `BEDROCK_GATE`
2. `NORTH_POLE_ALIGNMENT`
3. `PHASE_SPECIFIC_GATES`
4. `ACTIVE_CONTEXT_UPDATE`
5. `COMMIT_PUSH_HASH_FINAL`

Nenhum gate posterior pode compensar falha no Bedrock Gate.

## Regras invioláveis
Uma fase, prompt ou alteração deve ser bloqueada se:

- mentir sobre capacidade, evidência, execução real, teste real ou status de produção;
- promover produto, cliente real, venda ou produção sem gate futuro explícito;
- alterar runtime, frontend, backend, action runtime, rede, áudio, Obsidian, MCP ou dependências fora do escopo autorizado;
- ativar MCP, escrever config MCP, escrever no vault, fazer bulk-read de Obsidian ou liberar rede sem gate explícito;
- instalar dependências, executar scripts externos, expor segredos ou ler ambiente fora de allowlist autorizada;
- burlar `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `NORTH_POLE.md` ou source-of-truth oficial;
- tratar chat, intenção, roadmap conceitual, prompt ou memória como autorização materializada;
- transformar WARN em PASS sem evidência objetiva;
- avançar fase sem atualizar active-context quando a fase exige materialização;
- remover controle crítico para reduzir atrito sem mecanismo equivalente de segurança;
- criar automação real sem plano, permissão, ledger e rollback/compensação quando aplicável.

## Resultado
- `PASS`: nenhuma fundação violada.
- `WARN`: fundação preservada, mas há dívida ou ambiguidade controlada que precisa ser registrada.
- `BLOCKED`: fundação violada ou evidência insuficiente para provar preservação.
- `INVALID`: a fase não prova o que afirma provar.

## Draft de critérios de veredito
Este draft define como um futuro veredito Bedrock deve ser classificado.
Ele não executa o gate, não autoriza promoção e não substitui evidência materializada.

### Classes de veredito
- `INVALID`: a alegação não é sustentada por evidência, ou a fonte de verdade está contraditória.
- `BLOCKED`: existe um bloqueio absoluto ou ausência de evidência essencial.
- `LAB_ONLY_PASS`: a entrega é válida no laboratório, mas não pode ser promovida a produto.
- `TECHNICAL_PASS_PRODUCT_FAIL`: os testes técnicos passam, mas a prontidão de produto falha.
- `BEDROCK_WARN`: a entrega não tem bloqueio absoluto, mas ainda carrega dívida ou ambiguidade relevante.
- `PRODUCT_CANDIDATE`: a entrega pode entrar em piloto controlado ou pré-produção limitada.
- `PRODUCT_READY`: a entrega atende o mínimo confiável para produto, operação e auditoria.
- `EXCELLENT_PRODUCT_READY`: a entrega excede o mínimo de produto com robustez, clareza e diferenciação evidentes.

### Escala por dimensão
Cada dimensão recebe nota de `0` a `5`.
- `0`: ausente, contraditória ou impossível de provar.
- `1`: muito fraca, só observada em laboratório.
- `2`: parcial, com lacunas relevantes.
- `3`: aceitável, mas ainda não produto-ready.
- `4`: forte, consistente e auditável.
- `5`: excelente, robusta e pronta para uso comercial.

### Dimensões avaliadas
Bedrock avalia, no mínimo:
- Segurança.
- Privacidade e segredos.
- Determinismo.
- Evidência e auditabilidade.
- Testes e reprodutibilidade.
- Rollback, compensação e recuperação.
- Observabilidade.
- Isolation de falhas.
- Qualidade de resposta e comportamento.
- UX e clareza para usuário final.
- Performance e custo operacional.
- Manutenibilidade.
- Documentação e source-of-truth.
- Compatibilidade com roadmap e macroblocos.
- Prontidão comercial e de produto.
- Risco de regressão.
- Risco de automação indevida.
- Dependências externas.
- Fronteiras de runtime, frontend, backend, action runtime, voz e rede.

### Critérios bloqueantes absolutos
Os seguintes achados impedem `PRODUCT_READY`, mesmo com testes locais aprovados:
- segredo exposto.
- rede ativada sem gate explícito.
- runtime produtivo alterado sem autorização.
- ação real sem dry-run, permissão, ledger e rollback.
- ausência de evidência materializada.
- testes críticos ausentes.
- source-of-truth contraditório.
- rollback inexistente para mutação real.
- comportamento não reproduzível.
- resposta truncada ou falsa em caso crítico.
- dependência externa não pinada ou não revisada.
- Obsidian ou contexto lidos em bulk sem necessidade e sem gate.
- LLM-as-judge em decisão crítica sem mitigação determinística.
- falha de isolamento entre Lab e Produto.

### Evidência mínima por classe
- `LAB_ONLY_PASS`: testes locais, artefato-resumo e ausência de bloqueadores absolutos.
- `TECHNICAL_PASS_PRODUCT_FAIL`: testes passam, mas faltam UX, rollback, observabilidade, documentação ou evidência comercial.
- `BEDROCK_WARN`: evidência suficiente para manter a entrega no lab, mas insuficiente para promoção.
- `PRODUCT_CANDIDATE`: safety, testes, docs, rollback, observabilidade e isolamento básicos presentes; ainda requer piloto controlado.
- `PRODUCT_READY`: evidência completa, isolamento de falhas, rollback, documentação, ledger, UX mínima, custo conhecido e operação reproduzível.
- `EXCELLENT_PRODUCT_READY`: tudo do nível `PRODUCT_READY`, mais regressão baixa, UX excelente, diferenciação clara e operação exemplar.

### Relação com fases e entregas
- Uma fase pode ter `pass` no artefato local e ainda receber `LAB_ONLY_PASS` ou `TECHNICAL_PASS_PRODUCT_FAIL` no Bedrock.
- Uma capacidade ou macrobloco pode ser tecnicamente viável e ainda assim não estar pronto para produto.
- Uma entrega comercial só pode subir de classe quando a evidência materializada cobre as dimensões críticas do target.
- Mudanças em runtime, frontend, backend, action runtime, voz ou rede exigem prova específica de isolamento e rollback.

### Estrutura futura de artefato Bedrock
Um futuro artefato de veredito Bedrock deve conter, no mínimo:
- `phase`
- `target_type`
- `target_id`
- `technical_status`
- `bedrock_verdict`
- `product_boundary_decision`
- `evidence_bundle`
- `blocking_findings`
- `warning_findings`
- `score_by_dimension`
- `required_remediations`
- `product_promotion_allowed`
- `lab_continuation_allowed`
- `commercial_use_allowed`
- `runtime_change_allowed`
- `rollback_required`
- `human_review_required`
- `next_recommended_phase`

### Posicionamento de produto
Bedrock é o mecanismo que transforma o ARIS de um projeto técnico em um produto confiável, vendável e auditável.
Esse posicionamento é operacional, não promocional: ele depende de evidência, isolamento, rollback e veredito explícito.

## Draft de schema do Evidence Bundle
Este draft define o pacote mínimo de evidências que o Bedrock deve receber antes de emitir qualquer veredito sério.
Ele não executa o gate, não promove produto e não materializa bundles reais.

### Identidade do bundle
Campos obrigatórios:
- `bundle_id`
- `bundle_version`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `created_at`
- `created_by`
- `source_repositories`
- `source_commits`
- `bedrock_schema_version`
- `intended_bedrock_verdict_scope`

Tipos mínimos de `target_type`:
- `phase`
- `capability`
- `macroblock`
- `runtime_change`
- `frontend_change`
- `backend_change`
- `action_runtime_change`
- `voice_change`
- `network_change`
- `product_release_candidate`
- `commercial_delivery_candidate`

### Seções obrigatórias
Todo bundle deve conter:
- `technical_artifacts`
- `test_evidence`
- `security_evidence`
- `privacy_and_secret_evidence`
- `runtime_boundary_evidence`
- `rollback_and_recovery_evidence`
- `observability_evidence`
- `ux_evidence`
- `documentation_evidence`
- `source_of_truth_evidence`
- `dependency_evidence`
- `performance_and_cost_evidence`
- `risk_register`
- `known_limits`
- `human_review_evidence`
- `bedrock_blocker_scan`

### Technical artifacts
`technical_artifacts` deve apontar para:
- summaries JSON
- reports MD
- decision files
- ledger entries
- docs touched
- source files touched
- tests touched
- scripts/runners touched
- generated artifacts
- commit hashes
- push status
- dirty worktree notes
- unrelated changes preserved

### Test evidence
`test_evidence` must expose at least five independent validation classes for relevant bundles.
Minimum validation classes:
- unit tests
- runner execution
- JSON/schema validation
- diff/static validation
- source-of-truth reread validation

Additional applicable validation classes:
- negative/safety tests
- regression tests
- build/typecheck/lint
- manual smoke checklist

Validation rule:
- A product-relevant bundle must include at least `5` distinct validation classes.
- More validations can be attached, but fewer than `5` makes the bundle insufficient for product-grade judgment.

### Security and privacy evidence
`security_evidence` and `privacy_and_secret_evidence` must prove:
- segredos não expostos
- rede não ativada indevidamente
- dependências não instaladas indevidamente
- ausência de shell/subprocess perigoso quando aplicável
- ausência de bulk-read indevido
- egress controlado
- logs sem dados sensíveis
- permissões explícitas para mutações reais
- provider/model gateway boundaries respeitadas

### Runtime boundary evidence
The bundle must carry boolean claims plus evidence references for:
- `runtime_modified`
- `frontend_modified`
- `backend_modified`
- `action_runtime_modified`
- `voice_modified`
- `network_enabled`
- `dependencies_installed`
- `productive_path_changed`
- `commercial_use_allowed`
- `product_promotion_executed`

These fields are not assertions by themselves; each must point at evidence in the bundle.

### Rollback and recovery evidence
`rollback_and_recovery_evidence` must include:
- rollback plan
- rollback tested
- compensation plan
- previous state preserved
- ledger entry
- restore path
- failure mode recovery
- irreversible operation flag

### Source-of-truth evidence
`source_of_truth_evidence` must point to:
- active-context lido
- summaries usados
- docs usados
- Obsidian usado ou não usado
- stale conflicts detected
- precedence aplicada
- arquivos atualizados
- próxima ação registrada
- ledger atualizado

### Bundle completeness rules
`bundle_completeness` must resolve to one of:
- `complete`
- `incomplete`
- `insufficient`
- `contradictory`
- `stale`
- `invalid`
- `product_promotion_blocked`

Rule:
- `incomplete` may allow Lab continuation.
- `incomplete` never allows product promotion.
- `invalid`, `contradictory`, `stale`, and `insufficient` must block product-grade judgment until repaired.

### Blocker scan
`bedrock_blocker_scan` must be an array of objects with:
- `blocker_id`
- `description`
- `status`
- `evidence`
- `severity`
- `blocks_product_ready`
- `required_remediation`

The scan must inherit the absolute blockers from the verdict criteria draft and surface any failure as evidence-backed status, not opinion.

### Future artifact names
Future bundles should follow:
- `artifacts/bedrock/evidence_bundles/<target_id>_evidence_bundle.json`
- `artifacts/bedrock/evidence_bundles/<target_id>_evidence_bundle_report.md`

This draft does not create that tree yet. It only defines the shape.

## Draft de gate de completude do Evidence Bundle
Este draft define a regra deterministica que decide se um bundle do R12 e suficiente para julgamento Bedrock.
Ele nao executa o Bedrock real, nao promove produto e nao substitui o veredito de R11.

### Classes de completude
- `COMPLETE`: identidade valida, secoes obrigatorias presentes, matriz minima atendida, validacoes independentes suficientes e sem bloqueio absoluto ativo. Permite julgamento Bedrock, mas nao garante `PRODUCT_READY`.
- `INCOMPLETE`: ha partes faltando, mas a entrega ainda pode continuar no lab. Bloqueia promocao produto.
- `INSUFFICIENT`: existe evidenca parcial, porem ela nao sustenta julgamento product-grade. Bloqueia novo veredito ate evidencias adicionais.
- `CONTRADICTORY`: o bundle conflita com source-of-truth, commits, ledger, ou artefatos previos. Bloqueia julgamento ate reconciliacao.
- `STALE`: a evidenca relevante esta desatualizada, substituida ou nao corresponde ao estado atual. Bloqueia julgamento ate refresh.
- `INVALID`: identidade, schema, referencia ou auditabilidade quebradas. Bloqueia julgamento por definicao.
- `PRODUCT_PROMOTION_BLOCKED`: um bloqueador absoluto do R11 esta ativo; promocao produto e proibida ate remediacao explicita.

### Required evidence matrix
The matrix below defines the minimum evidence expectations per target type.

- `phase`, `capability`, `macroblock`:
  - tests: `yes`
  - rollback: `only if the bundle claims a mutation path`
  - human_review: `yes`
  - ux_evidence: `only if user-facing`
  - security/privacy: `yes` when the target crosses trust boundaries
  - dependency_evidence: `only if dependencies are touched or referenced`
  - runtime_boundary_evidence: `only if runtime boundaries are touched`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `only if the bundle makes performance or cost claims`
  - lab_only: `yes`
  - product_ready_candidate: `yes`, but only with full product evidence
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change`:
  - tests: `yes`
  - rollback: `yes`
  - human_review: `yes`
  - ux_evidence: `yes` for frontend and voice, optional otherwise if user-facing
  - security/privacy: `yes`
  - dependency_evidence: `yes` when touched or transitively affected
  - runtime_boundary_evidence: `yes`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `yes`
  - lab_only: `yes`
  - product_ready_candidate: `yes`
- `product_release_candidate`, `commercial_delivery_candidate`:
  - tests: `yes`
  - rollback: `yes`
  - human_review: `yes`
  - ux_evidence: `yes`
  - security/privacy: `yes`
  - dependency_evidence: `yes`
  - runtime_boundary_evidence: `yes`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `yes`
  - lab_only: `no`
  - product_ready_candidate: `yes`

### Minimum validation rule
- A relevant bundle must contain at least `5` independent validation classes.
- Independent means the classes observe different failure surfaces; duplicate reruns of the same check do not count twice.
- Valid classes can include `json.tool`, `git diff --check`, `git status`, unit test, runner execution, build, lint, smoke, negative test, regression test, or source-of-truth reread, but each bundle must name the classes explicitly.
- For product-relevant bundles, at least one validation class must cover security/privacy or runtime boundary risk.
- For bundles involving real mutation, at least one validation class must cover rollback or compensation.

### Evidence scoring without LLM-as-judge
- Scores are derived from evidence references, not from model opinion.
- The model may summarize or classify, but it cannot be the sole authority for a critical Bedrock decision.
- A critical gate requires deterministic criteria, machine-checkable artifacts, or explicit human review.
- Missing evidence counts against the bundle.
- Contradictory evidence blocks the bundle.

### Completeness decision algorithm draft
1. Validate bundle identity and schema version.
2. Validate target type and target scope are allowed.
3. Validate the required sections from the R12 schema.
4. Validate the required evidence matrix for the target type.
5. Count independent validation classes and confirm the minimum of `5`.
6. Scan for blocker findings from the R11 absolute blocker set.
7. Detect contradictions across source-of-truth, commits, ledger, and artifacts.
8. Detect stale evidence or evidence superseded by newer material.
9. Detect evidence that cannot be audited or reproduced.
10. Determine `completeness_class`.
11. Determine whether `bedrock_verdict_allowed`.
12. Determine whether `product_promotion_allowed`, `lab_continuation_allowed`, and `commercial_use_allowed`.
13. Emit required remediations for missing, stale, contradictory, or blocked evidence.

### Blocker handling
Each R11 absolute blocker must behave as follows:
- `secret exposed`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the target is fully quarantined and the secret is not on a product path; required remediation is secret removal and rotation.
- `network activated without gate`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the network path is lab-only and explicitly gated; required remediation is gate insertion or network disablement.
- `runtime product altered without authorization`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the change is reverted or confined to a non-product path; required remediation is authorization or revert.
- `real action without dry-run, permission, ledger, rollback`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the action is never promoted and stays isolated; required remediation is dry-run, permission, ledger, and rollback.
- `absence of evidence`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the bundle is explicitly lab-only and the missing evidence is non-critical; required remediation is evidence materialization.
- `critical tests absent`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the target is lab-only and tests are not relevant; required remediation is test coverage or explicit rationale.
- `source-of-truth contradictory`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only after reconciliation; required remediation is source-of-truth repair.
- `rollback nonexistent for real mutation`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if no real mutation occurred; required remediation is rollback or compensation design.
- `behavior non-reproducible`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the behavior is explicitly exploratory; required remediation is reproducibility evidence.
- `response truncated or false for critical case`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the case is non-critical and clearly labeled; required remediation is corrected behavior and verification.
- `dependency external not pinned or reviewed`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the dependency is not on the promotion path; required remediation is pinning and review.
- `Obsidian/context bulk-read`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the bundle does not rely on that read and the violation is repaired; required remediation is query-first repair.
- `LLM-as-judge without deterministic mitigation`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the critical decision is moved to deterministic criteria or human review; required remediation is deterministic mitigation.
- `failure of isolation between Lab and Product`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the path is proven lab-only and isolation is restored; required remediation is boundary repair.

### Future output schema
Future completeness-gate output should contain at least:
- `phase`
- `target_id`
- `target_type`
- `bundle_id`
- `bundle_version`
- `schema_version`
- `completeness_class`
- `bedrock_verdict_allowed`
- `product_promotion_allowed`
- `lab_continuation_allowed`
- `commercial_use_allowed`
- `minimum_validation_count`
- `validation_classes_detected`
- `missing_required_sections`
- `missing_required_evidence`
- `blocking_findings`
- `warning_findings`
- `stale_findings`
- `contradiction_findings`
- `invalid_schema_findings`
- `required_remediations`
- `next_recommended_phase`

### Relation with R11 and R12
- R11 defines what Bedrock judges.
- R12 defines what evidence must exist.
- R13 defines whether that evidence is complete enough for judgment.
- R13 still does not execute the Bedrock runtime gate.

## Draft de schema do blocker scan
Este draft define como o Bedrock representa, valida e materializa blockers absolutos de forma auditavel.
Ele nao executa scanner runtime real, nao promove produto e nao altera o R10 global boundary.

### Identidade do scan
Campos obrigatorios do future blocker scan:
- `scan_id`
- `scan_version`
- `schema_version`
- `target_id`
- `target_type`
- `target_phase`
- `bundle_id`
- `created_at`
- `created_by`
- `source_commits`
- `scan_scope`
- `scan_mode`
- `bedrock_gate_version`

### Estados por blocker
Cada blocker deve usar exatamente um destes estados:
- `not_applicable`: exige justificativa e escopo claro.
- `not_detected`: exige evidencia verificavel.
- `detected`: bloqueia `PRODUCT_READY` e ativa bloqueio de promocao para target product-grade.
- `suspected`: bloqueia `PRODUCT_READY` ate verificacao.
- `unknown`: bloqueia `PRODUCT_READY` quando a evidencia deveria existir.
- `unverified`: bloqueia `PRODUCT_READY` para target product-grade.
- `remediated_pending_verification`: continua bloqueando produto ate validacao.
- `waived_with_human_approval`: exige review humano, escopo, prazo e justificativa; nunca pode bypassar segredo exposto, rede indevida, acao real sem permissao/ledger/rollback, ou falha de isolamento Lab/Produto.

### Severidades
Cada blocker usa uma severidade desta lista:
- `critical`
- `high`
- `medium`
- `low`
- `informational`

Regras de severidade:
- Todos os 14 blockers absolutos do R11 sao `critical` ou `high`.
- `critical detected` gera `PRODUCT_PROMOTION_BLOCKED`.
- `high detected` bloqueia `PRODUCT_READY` e `commercial_use_allowed`.
- Severidade nao pode ser reduzida por opiniao do modelo.
- Reducao de severidade exige evidencia materializada ou human review explicita.

### Canonical blocker catalog
Os 14 IDs canonicos e estaveis sao:
- `secret_exposed`: title=`Secret exposed`; description=`Secret, token, credential or private key exposed in artifact, log, prompt or output.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when exposure reaches a product path; required_evidence=`secret scan, redaction proof, scope check`; required_remediation=`remove exposure, rotate secret, scrub artifacts`; verification_method=`secret scan plus manual artifact review`; waiver_allowed=`False`; waiver_constraints=`non-waivable`.
- `network_enabled_without_gate`: title=`Network enabled without gate`; description=`Network path activated without explicit gate, scope or approval.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when network reaches product path; required_evidence=`gate proof, egress control, scope isolation`; required_remediation=`insert gate or disable network`; verification_method=`runtime/config review plus validation`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product paths`.
- `productive_runtime_modified_without_authorization`: title=`Productive runtime modified without authorization`; description=`Runtime prod path changed without explicit permission and ledgered approval.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the change touches product path; required_evidence=`authorization record, diff, scope proof`; required_remediation=`authorize or revert`; verification_method=`diff plus decision ledger review`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product runtime`.
- `real_action_without_dry_run_permission_ledger_rollback`: title=`Real action without dry-run, permission, ledger, rollback`; description=`Real mutation attempted or claimed without dry-run, permission, ledger and rollback/compensation.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the action is real or promoted; required_evidence=`dry-run record, permission, ledger entry, rollback plan`; required_remediation=`add dry-run, permission, ledger and rollback`; verification_method=`execution ledger review plus rollback proof`; waiver_allowed=`False`; waiver_constraints=`non-waivable for real action`.
- `materialized_evidence_missing`: title=`Materialized evidence missing`; description=`Required evidence exists only as assertion or is absent.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only when lab-only and non-critical; required_evidence=`materialized artifacts, traceable refs`; required_remediation=`materialize evidence bundle`; verification_method=`artifact presence review`; waiver_allowed=`True`; waiver_constraints=`requires human review, scope and TTL`.
- `critical_tests_missing`: title=`Critical tests missing`; description=`Critical validation classes are absent for the claimed target.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only for lab-only exploratory work; required_evidence=`test plan, test results, coverage map`; required_remediation=`add critical tests or narrow claim`; verification_method=`test inventory review`; waiver_allowed=`True`; waiver_constraints=`requires human review and explicit lab-only scope`.
- `source_of_truth_contradictory`: title=`Source of truth contradictory`; description=`Artifacts, ledger or current state conflict with source-of-truth.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` until reconciliation; required_evidence=`conflict trace, precedence decision, reconciled state`; required_remediation=`reconcile source-of-truth`; verification_method=`cross-file reconciliation review`; waiver_allowed=`True`; waiver_constraints=`requires explicit reconciliation plan`.
- `rollback_missing_for_real_mutation`: title=`Rollback missing for real mutation`; description=`A real mutation path lacks a viable rollback or compensation path.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if no real mutation occurred; required_evidence=`rollback plan, restore path, compensation plan`; required_remediation=`design or prove rollback`; verification_method=`rollback evidence review`; waiver_allowed=`True`; waiver_constraints=`must not cover real mutation`.
- `non_reproducible_behavior`: title=`Non reproducible behavior`; description=`The behavior cannot be reproduced under the stated inputs, state and scope.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only for exploratory lab cases; required_evidence=`repro steps, rerun proof, environment notes`; required_remediation=`add reproducibility evidence`; verification_method=`rerun validation plus artifact comparison`; waiver_allowed=`True`; waiver_constraints=`requires explicit lab-only scope`.
- `critical_response_truncated_or_false`: title=`Critical response truncated or false`; description=`Critical case received a truncated or false response or summary.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the case is not product-critical and is clearly labeled; required_evidence=`full response trace, comparison, failure example`; required_remediation=`correct response path and verify`; verification_method=`case review plus comparison`; waiver_allowed=`True`; waiver_constraints=`requires non-critical scope and human review`.
- `external_dependency_unpinned_or_unreviewed`: title=`External dependency unpinned or unreviewed`; description=`Dependency is not pinned or not reviewed for the promotion path.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only when dependency is not on the promotion path; required_evidence=`pin, review record, dependency inventory`; required_remediation=`pin and review dependency`; verification_method=`dependency audit`; waiver_allowed=`True`; waiver_constraints=`requires explicit risk acceptance`.
- `obsidian_or_context_bulk_read_violation`: title=`Obsidian or context bulk read violation`; description=`Bulk-read of Obsidian or context occurred outside query-first rules.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the violation is repaired and isolated from product path; required_evidence=`query log, scope, read trace`; required_remediation=`repair query-first discipline`; verification_method=`read-path audit`; waiver_allowed=`True`; waiver_constraints=`requires source-of-truth repair and no product-path reuse`.
- `llm_as_judge_for_critical_gate_without_deterministic_mitigation`: title=`LLM as judge without deterministic mitigation`; description=`Critical decision relied on model opinion without deterministic guardrails or human review.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the critical decision is moved to deterministic criteria or explicit human review; required_evidence=`deterministic criteria, human review trace`; required_remediation=`add deterministic mitigation`; verification_method=`decision trace review`; waiver_allowed=`True`; waiver_constraints=`cannot waive away deterministic mitigation requirement`.
- `lab_product_isolation_failure`: title=`Lab product isolation failure`; description=`Isolation between lab and product paths failed or is not provable.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the failure touches product boundary; required_evidence=`isolation proof, boundary trace, path separation`; required_remediation=`repair isolation boundary`; verification_method=`boundary audit`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product promotion`.

### Blocker entry fields
Every blocker scan item must include:
- `status`
- `severity`
- `evidence_refs`
- `evidence_quality`
- `source_paths_checked`
- `commands_or_validations_used`
- `findings`
- `remediation_required`
- `remediation_owner`
- `verification_required`
- `blocks_product_ready`
- `blocks_commercial_use`
- `lab_continuation_allowed`
- `human_review_required`
- `waiver_status`
- `waiver_reason`
- `waiver_approved_by`
- `last_verified_at`

### Evidence quality
Evidence quality must be one of:
- `materialized`
- `partial`
- `declarative_only`
- `missing`
- `contradictory`
- `stale`
- `not_auditable`

Rules:
- `materialized` is preferred for product.
- `declarative_only` is not enough for `PRODUCT_READY`.
- `missing`, `contradictory`, `stale`, and `not_auditable` block product when tied to an absolute blocker.
- `partial` may allow Lab, but not product, unless the target is explicitly lab-only and safe.

### Waiver policy
- Waiver is an exception, not the default path.
- Waiver requires explicit human review, scope, TTL and justification.
- Waiver cannot release commercial use if the blocker involves secret exposure, real mutation without ledger/rollback, network indevida, or Lab/Product isolation failure.
- Waiver does not turn missing evidence into valid evidence.
- Waiver must appear in the Evidence Bundle and in the future Bedrock Verdict Artifact.

### Integration with completeness gate
- Any `detected`, `suspected`, `unknown` or `unverified` blocker on a target product-grade path must affect `completeness_class`.
- A critical active blocker yields `PRODUCT_PROMOTION_BLOCKED`.
- A high active blocker blocks `PRODUCT_READY` and `commercial_use_allowed`.
- A blocker scan that is incomplete, contradictory, stale or invalid can move the bundle to `INSUFFICIENT`, `CONTRADICTORY`, `STALE` or `INVALID`.
- A clean blocker scan only removes one class of block; it never guarantees `PRODUCT_READY`.

### Future output schema
Future blocker scan output should contain at least:
- `phase`
- `target_id`
- `target_type`
- `bundle_id`
- `scan_id`
- `scan_status`
- `scan_completeness`
- `blocker_count`
- `detected_blockers`
- `suspected_blockers`
- `unknown_blockers`
- `waived_blockers`
- `critical_blockers`
- `high_blockers`
- `product_promotion_blocked`
- `commercial_use_allowed`
- `lab_continuation_allowed`
- `required_remediations`
- `human_review_required`
- `next_recommended_phase`

### Relation with R11, R12 and R13
- R11 defines the absolute blockers.
- R12 requires `bedrock_blocker_scan` as a mandatory Evidence Bundle section.
- R13 determines whether blocker findings collapse completeness into `PRODUCT_PROMOTION_BLOCKED`, `INSUFFICIENT`, `INVALID`, `CONTRADICTORY` or `STALE`.
- R14 defines the internal blocker scan schema used by future Bedrock evidence.
- R14 still does not execute a scanner runtime.

## Draft de schema do Bedrock Verdict Artifact
Este draft define o artefato final canonical que um futuro Bedrock verdict deve produzir.
Ele conecta R10, R11, R12, R13 e R14 em uma saida auditavel, reproduzivel e separada de qualquer pass tecnico local.

### Identidade do veredito
Campos obrigatorios:
- `verdict_id`
- `verdict_schema_version`
- `bedrock_gate_version`
- `phase`
- `target_id`
- `target_type`
- `target_phase`
- `target_scope`
- `evaluated_at`
- `evaluated_by`
- `source_repositories`
- `source_commits`
- `evidence_bundle_id`
- `blocker_scan_id`
- `completeness_gate_id`
- `verdict_artifact_paths`

### Status tecnico separado do status produto
O artifact deve manter:
- `technical_status`
- `technical_decision`
- `technical_pass`
- `bedrock_verdict`
- `product_boundary_decision`
- `product_promotion_allowed`
- `commercial_use_allowed`
- `lab_continuation_allowed`
- `runtime_change_allowed`
- `frontend_change_allowed`
- `backend_change_allowed`
- `action_runtime_change_allowed`
- `voice_change_allowed`
- `network_change_allowed`

Regra:
- `technical_pass=true` nunca implica automaticamente `product_promotion_allowed=true`.

### Verdict classes herdadas do R11
As classes de veredito sao:
- `INVALID`
- `BLOCKED`
- `LAB_ONLY_PASS`
- `TECHNICAL_PASS_PRODUCT_FAIL`
- `BEDROCK_WARN`
- `PRODUCT_CANDIDATE`
- `PRODUCT_READY`
- `EXCELLENT_PRODUCT_READY`

Cada classe deve aparecer em `bedrock_verdict` e deve ser acompanhada pelo minimo de campos seguintes:
- `INVALID`: `technical_status`, `final_bedrock_decision`, `known_limits`, `residual_risks`, `blocked_next_scope`
- `BLOCKED`: `technical_status`, `blocking_findings`, `required_remediations`, `product_boundary_decision`, `blocked_next_scope`
- `LAB_ONLY_PASS`: `technical_status`, `lab_continuation_allowed`, `product_promotion_allowed`, `allowed_next_scope`
- `TECHNICAL_PASS_PRODUCT_FAIL`: `technical_status`, `technical_pass`, `product_boundary_decision`, `required_remediations`
- `BEDROCK_WARN`: `technical_status`, `warning_findings`, `required_remediations`, `re_evaluation_required`
- `PRODUCT_CANDIDATE`: `technical_status`, `product_boundary_decision`, `promotion_class`, `human_review_required`, `required_remediations`
- `PRODUCT_READY`: `technical_status`, `product_promotion_allowed`, `commercial_use_allowed`, `blocker_scan_status`, `evidence_completeness_class`
- `EXCELLENT_PRODUCT_READY`: `technical_status`, `product_promotion_allowed`, `commercial_use_allowed`, `score_by_dimension`, `dimension_confidence`, `dimension_risk_level`

### Relation with completeness gate
Campos obrigatorios:
- `evidence_completeness_class`
- `evidence_bundle_complete`
- `missing_required_sections`
- `missing_required_evidence`
- `validation_classes_detected`
- `minimum_validation_count`
- `minimum_validation_rule_passed`
- `completeness_findings`
- `completeness_required_remediations`

Rules:
- If `evidence_completeness_class` is not `COMPLETE`, the artifact cannot allow product promotion.
- `INCOMPLETE` may allow Lab continuation.
- `INSUFFICIENT`, `INVALID`, `CONTRADICTORY`, `STALE` and `PRODUCT_PROMOTION_BLOCKED` block product-grade judgment.

### Relation with blocker scan
Campos obrigatorios:
- `blocker_scan_status`
- `blocker_scan_completeness`
- `canonical_blocker_count`
- `detected_blockers`
- `suspected_blockers`
- `unknown_blockers`
- `unverified_blockers`
- `waived_blockers`
- `critical_blockers`
- `high_blockers`
- `blocking_findings`
- `blocker_required_remediations`

Rules:
- Any critical blocker active blocks `PRODUCT_READY`.
- Waiver cannot release commercial use where R14 forbids it.
- A clean scan removes one class of block but does not guarantee `PRODUCT_READY`.

### Score and dimension summary
The artifact must expose:
- `score_by_dimension`
- `dimension_findings`
- `dimension_evidence_refs`
- `dimension_confidence`
- `dimension_risk_level`

Dimensions inherited from R11:
- segurança
- privacidade/segredos
- determinismo
- evidência/auditabilidade
- testes/reprodutibilidade
- rollback/recuperação
- observabilidade
- failure isolation
- qualidade de resposta/comportamento
- UX
- performance/custo
- manutenibilidade
- documentação/source-of-truth
- roadmap/macroblocos
- prontidão comercial/produto
- risco de regressão
- risco de automação indevida
- dependências externas
- boundaries de runtime/frontend/backend/action runtime/voz/rede

Rule:
- Score must be derived from materialized evidence, validations or explicit human review.
- LLM may summarize, but cannot be the sole judge in a critical gate.

### Final decision
Campos obrigatorios:
- `final_bedrock_decision`
- `final_product_boundary_decision`
- `promotion_class`
- `allowed_next_scope`
- `blocked_next_scope`
- `required_remediations`
- `recommended_next_phase`
- `human_review_required`
- `re_evaluation_required`
- `expires_at_or_stale_after`
- `known_limits`
- `residual_risks`

Suggested decision values:
- `invalid_artifact`
- `blocked_before_verdict`
- `lab_continuation_allowed`
- `technical_pass_product_blocked`
- `product_candidate_with_conditions`
- `product_ready_allowed`
- `excellent_product_ready_allowed`

### Auditability and traceability
The artifact must record:
- `input_artifacts`
- `input_reports`
- `input_summaries`
- `input_commits`
- `commands_executed`
- `validations_executed`
- `files_changed`
- `protected_sources_not_modified`
- `dirty_worktree_notes`
- `context_usage_report`
- `source_of_truth_precedence_applied`
- `stale_context_conflicts_detected`
- `obsidian_usage`
- `human_approvals`
- `ledger_entries`

### Future artifact names
Future verdict artifacts should follow:
- `artifacts/bedrock/verdicts/<target_id>_bedrock_verdict.json`
- `artifacts/bedrock/verdicts/<target_id>_bedrock_verdict_report.md`

This draft does not create that tree yet. It only defines the shape.

### Relation with R10 through R14
- R10 defines the global role of Bedrock.
- R11 defines verdict classes and blockers.
- R12 defines the Evidence Bundle.
- R13 defines bundle completeness.
- R14 defines blocker scan structure.
- R15 defines the final verdict artifact.
- R15 still does not execute a real judgment.

## Relação com NORTH_POLE
O Bedrock Gate é o chão. O North Pole é o norte.

O Bedrock Gate impede dano, mentira, bypass e ativação indevida. O North Pole exige excelência, simplicidade, eficiência, valor e vitória técnica/produto.

Uma fase só pode passar se preservar o chão e aproximar o ARIS do norte.

## Status operacional
Este contrato não autoriza implementação, runtime mutation, rede, MCP, vault write, dependency install, product promotion ou cliente real.

A próxima ação operacional continua sendo definida exclusivamente por `NEXT_ACTION.md`.
