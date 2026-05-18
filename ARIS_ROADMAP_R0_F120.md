# ARIS Roadmap R0→F120 — Canonical Governance Roadmap v2.1

Status: PASS by conservative review. Scope: Lab Mastery roadmap. Production authorization: false.

Next authorized phase: `ARIS-ROADMAP-R0 — Governance Foundation`.

C7 is blocked until R0 PASS. F33 remains paused. F51+ remains advisory-only. F120 means Lab Mastery Closure, not production.

## Global rule

No phase from R0, C6-C14, or F33-F120 authorizes production, customer deployment, SaaS launch, payment execution, external-channel sends, runtime production mutation, MCP activation, DB/schema apply, or network use. Any release requires future F121+ Controlled Productization Gate.

## Global phase template

Every phase inherits: fase_id, nome, camada, objetivo, prerequisitos_hard, artifact_primario, artifacts_secundarios, done_mensuravel, thresholds, gate_entrada, authority_policy, adr_obrigatorio, waiver_elegivel, nao_autorizacao, owasp_asi_coverage, regulatory_mapping.

## Global closure thresholds

blocker_count=0; primary_artifact_exists=true; artifact_schema_validation_rate=1.00; required_tests_pass_rate=1.00; protected_surface_mutation_count=0; unauthorized_real_effect_count=0; known_unclassified_gap_count=0; research_evidence_generated_before_implementation=true when adr_obrigatorio=true.

If a required threshold fails: phase is BLOCKED, phase_issue.json is created, affected closed phase becomes reopened_by_regression through regression_issue.json, hotfix and old+new retest are required, and waiver cannot authorize production.

## R0 — Governance Foundation

Creates the auditable governance foundation before C7/F33/F51+ continuation. Primary artifact: `artifacts/roadmap/r0_governance_foundation_decision.json`. Secondary artifacts: phase_template_schema, gate_authority_policy, waiver_policy, architecture_decision_record_schema, research_decision_matrix_schema, gate_threshold_failure_policy, regression_reopen_authority_policy, regulatory_scope_declaration, roadmap_machine_validation_report. Done: required_r0_artifact_coverage=1.00; schema_validation_rate=1.00; roadmap_machine_validation_rate=1.00; missing_governance_artifacts=0; blocker_count=0.

## C6-C14 — Bedrock Gate Engine

- C6 — Read-First & Source-of-Truth Compliance Evaluator — `bedrock_c6_read_first_sot_evaluator.json` — read_first_compliance=1.00; source_of_truth_conflict_count=0.
- C7 — Warning vs Blocker Classifier — `bedrock_c7_warning_blocker_classifier.json` — classification_accuracy_on_fixtures=1.00; unclassified_gap_count=0.
- C8 — Bedrock Verdict Composition Engine — `bedrock_c8_verdict_composition_engine.json` — verdict_composition_fixture_pass_rate=1.00; false_pass_count=0.
- C9 — Adversarial Phase Package Fixtures — `bedrock_c9_adversarial_fixtures.json` — adversarial_false_pass_count=0; dangerous_claim_detection=1.00.
- C10 — Controlled Bedrock CLI Runner — `bedrock_c10_cli_runner_contract.json` — cli_determinism_rate=1.00; runtime_mutation_count=0.
- C11 — Bedrock Report Generator — `bedrock_c11_report_generator.json` — report_evidence_link_coverage=1.00; missing_report_field_count=0.
- C12 — Bedrock Integration Dry-Run — `bedrock_c12_integration_dry_run.json` — dry_run_integration_pass_rate=1.00; enforcement_real_count=0.
- C13 — Bedrock Enforcement Simulation Gate — `bedrock_c13_enforcement_simulation.json` — known_bad_phase_block_rate=1.00; known_good_phase_pass_rate=1.00.
- C14 — Bedrock Final Closure Gate — `bedrock_c14_final_closure_gate.json` — bedrock_executable=true; blocker_count=0; bedrock_false_pass_count=0.

## F33-F50 — Foundational Contracts Layer

- F33 — Local Memory/Search/Evaluation Baseline Contract — `f33_memory_eval_baseline_contract.json`.
- F34 — Action Registry Contract Foundation — `f34_action_registry_contract.json`; `f34_action_slo_baseline.json`.
- F35 — Typed Action Plan Schema — `f35_typed_action_plan_schema.json`.
- F36 — Security Precheck & Policy Boundary — `f36_security_precheck_boundary.json`.
- F36.B — MCP Security Gateway Contract — `f36b_mcp_security_gateway_contract.json`.
- F36.C — Semantic Intent Classifier Contract — `f36c_semantic_intent_classifier_contract.json`.
- F37 — Permission Gate Contract — `f37_permission_gate_contract.json`; `quorum_approval_policy.json`.
- F38 — Dry-Run Contract — `f38_dry_run_contract.json`.
- F39 — Execution Authorization Contract — `f39_execution_authorization_contract.json`.
- F40 — Ledger Contract Foundation — `f40_ledger_contract.json`.
- F41 — Replay/Rollback Contract — `f41_replay_rollback_contract.json`.
- F42 — Saga & Compensation Contract — `f42_saga_compensation_contract.json`.
- F43 — Sidecar Boundary Contract — `f43_sidecar_boundary_contract.json`.
- F43.B — Execution Ring Policy Contract — `f43b_execution_ring_policy.json`.
- F44 — Kill-Switch & Safety Stop Contract — `f44_kill_switch_contract.json`.
- F45 — Capability Handle Contract — `f45_capability_handle_contract.json`.
- F45.B — Agent Identity Contract, DID-Based — `f45b_agent_identity_contract.json`.
- F46 — Observation Model Contract — `f46_observation_model_contract.json`.
- F47 — Runtime Mode Matrix — `f47_runtime_mode_matrix.json`.
- F48 — Runtime Scaffold Contract — `f48_runtime_scaffold_contract.json`.
- F49 — Core Runtime Integration Dry-Run Plan — `f49_runtime_integration_dry_run_plan.json`.
- F50 — Foundational Contracts Closure Gate — `f50_foundational_contracts_closure.json`.

## F51-F65 — Runtime Hardening Layer

Refinements: F34→F52, F37→F55, F38→F56, F40→F57, F43→F59.

- F51 — Action Runtime Constitution Hardening — `f51_runtime_constitution_hardening.json`.
- F52 — Action Registry Runtime Hardening — `f52_action_registry_hardening.json`.
- F53 — Tool Schema Projection Hardening — `f53_tool_schema_projection_hardening.json`.
- F54 — Policy Engine Hardening — `f54_policy_engine_hardening.json`.
- F55 — Permission Abuse & Quorum Hardening — `f55_permission_abuse_quorum_hardening.json`.
- F56 — Dry-Run Executor Hardening — `f56_dry_run_executor_hardening.json`.
- F57 — Ledger Integrity Hardening — `f57_ledger_integrity_hardening.json`.
- F58 — Rollback/Compensation Hardening — `f58_rollback_compensation_hardening.json`.
- F59 — Sidecar Runtime Hardening — `f59_sidecar_runtime_hardening.json`.
- F60 — First Lab-Controlled Local Action Simulation — `f60_first_lab_action_simulation.json`.
- F61 — External API Simulation Harness — `f61_external_api_simulation_harness.json`.
- F62 — External Channel Simulation Harness — `f62_external_channel_simulation_harness.json`.
- F63 — Runtime Cockpit Lab Console — `f63_runtime_cockpit_lab_console.json`.
- F64 — Security Red-Team Base Suite — `f64_security_red_team_base_suite.json`.
- F64.B — OWASP Agentic ASI01-ASI10 Coverage Gate — `f64b_owasp_agentic_coverage_matrix.json`.
- F65 — Runtime Hardening Closure Gate — `f65_runtime_hardening_closure.json`.

## F66-F80 — Enterprise Governance Layer

- F66 — Agent Evaluation Framework — `f66_agent_evaluation_framework.json`.
- F66.B — CLEAR Evaluation Baseline — `f66b_clear_evaluation_baseline.json`.
- F67 — Golden Trajectory Regression — `f67_golden_trajectory_regression.json`.
- F68 — Drift Detection — `f68_drift_detection.json`.
- F69 — Enterprise Multi-Tenant Isolation — `f69_multi_tenant_isolation.json`.
- F69.B — Multi-Tenant Concurrency Stress Lab — `f69b_multi_tenant_concurrency_stress_lab.json`.
- F70 — RBAC Runtime Cockpit — `f70_rbac_cockpit.json`.
- F71 — Compliance Export Evidence — `f71_compliance_export_evidence.json`.
- F71.B — EU AI Act Article 9-17 Evidence Track — `f71b_eu_ai_act_article_9_17_mapping.json`.
- F71.C — ISO/IEC 42001 Control Mapping Gate — `f71c_iso42001_control_mapping.json`.
- F72 — Long-Term Memory Governance — `f72_memory_governance.json`.
- F73 — Memory Scoping & Right-to-Be-Forgotten — `f73_memory_forgetting_scope.json`.
- F74 — Multi-Agent Trust Boundaries — `f74_multi_agent_trust_boundaries.json`.
- F74.B — Behavioral Trust Scoring Lab — `f74b_behavioral_trust_scoring_lab.json`.
- F74.C — Agent-to-Agent Communication Security Contract — `f74c_a2a_communication_security_contract.json`.
- F75 — Cross-Agent Capability Delegation Lab — `f75_cross_agent_delegation_lab.json`.
- F76 — Model Versioning & Provider Failover — `f76_model_provider_governance.json`.
- F77 — Prompt Versioning with Hash & Ledger — `f77_prompt_versioning_ledger.json`.
- F78 — SBOM + AIBOM + Dependency Scanning — `f78_sbom_aibom_dependency_scanning.json`.
- F79 — Secret Rotation Planning & Simulation — `f79_secret_rotation_simulation.json`.
- F80 — Enterprise Governance Closure Gate — `f80_enterprise_governance_closure.json`.

## F81-F86 — Operational Maturity Layer

- F81 — SRE Runbook for Governed Automation Platforms — `f81_sre_runbook_registry.json`.
- F82 — AI Agent Incident Response Framework — `f82_incident_response_framework.json`.
- F83 — Continuous Chaos Engineering Protocol — `f83_chaos_protocol.json`.
- F84 — Cost Attribution Engine — `f84_cost_attribution_engine.json`.
- F85 — LLM Capacity Planning Framework — `f85_llm_capacity_planning.json`.
- F86 — Usage Anomaly Detection & Alerting — `f86_usage_anomaly_detection.json`.
- F86.G — Operational Maturity Block Closure Gate — `f86g_operational_maturity_closure_gate.json`.

## F87-F94 — Domain Simulation Pack

Parametrizable; no domain hardcode. Use entity, agent, slot, channel, transaction, domain.

- F87 — Secure Domain CRM Lab — `f87_secure_domain_crm_lab.json`.
- F88 — Generic Scheduling Conflict Prevention Lab — `f88_generic_scheduling_lab.json`.
- F89 — Controlled Financial Action Simulation Lab — `f89_financial_action_simulation_lab.json`.
- F90 — External Notification Channel Governance Lab — `f90_notification_channel_lab.json`.
- F91 — Team/Role Domain RBAC Simulation Lab — `f91_team_role_rbac_lab.json`.
- F92 — Consent-Based Data Onboarding Framework — `f92_consent_onboarding_framework.json`.
- F93 — Auditable Operational Reporting Framework — `f93_auditable_reporting_framework.json`.
- F94 — Legacy Data Import Safety Framework — `f94_legacy_import_safety_framework.json`.
- F94.G — Domain Simulation Pack Closure Gate — `f94g_domain_simulation_pack_closure_gate.json`.

## F95A-F95E — Domain Simulation Integration Gate

- F95A — Domain Simulation Scenario Assembly Gate — `f95a_scenario_assembly_gate.json`.
- F95B — E2E Dry-Run Execution Gate — `f95b_e2e_dry_run_execution_gate.json`.
- F95C — Rollback/Compensation Verification Gate — `f95c_rollback_compensation_gate.json`.
- F95D — Simulation Evidence Bundle Export Gate — `f95d_simulation_evidence_bundle_gate.json`.
- F95E — Domain Simulation Closure Gate — `f95e_domain_simulation_closure_gate.json`.

## F96-F114 — Lab Mastery & Simulation Gauntlet

Rule: F96 PASS is a hard prerequisite for F97-F114.

- F96 — Closed Phase Regression Reopen Protocol — `f96_regression_reopen_protocol.json`.
- F97 — Lab Scenario Registry — `f97_lab_scenario_registry.json`.
- F98 — Synthetic Domain Data Generator — `f98_synthetic_data_generator.json`.
- F99 — End-to-End Simulation Harness — `f99_e2e_simulation_harness.json`; prerequisites: F96, F97, F98.
- F100 — Action Scenario Matrix — `f100_action_scenario_matrix.json`.
- F101 — Permission Abuse Simulation — `f101_permission_abuse_simulation.json`.
- F102 — Ledger Forensics Simulation — `f102_ledger_forensics_simulation.json`.
- F103 — Rollback/Compensation Gauntlet — `f103_rollback_compensation_gauntlet.json`.
- F104 — Concurrent Actions Simulation — `f104_concurrent_actions_simulation.json`.
- F105 — Malicious Input Simulation — `f105_malicious_input_simulation.json`.
- F106 — Provider and Model Failure Lab — `f106_provider_model_failure_lab.json`.
- F107 — Memory Corruption and Forgetting Lab — `f107_memory_corruption_forgetting_lab.json`.
- F108 — Multi-Agent Attack Lab — `f108_multi_agent_attack_lab.json`.
- F109 — Cost Explosion Simulation — `f109_cost_explosion_simulation.json`.
- F110 — UX Decision Simulation — `f110_ux_decision_simulation.json`; `f110_approval_clarity_rubric.json`.
- F111 — Operational Incident Drill — `f111_operational_incident_drill.json`.
- F112 — Backup, Restore and Replay Lab — `f112_backup_restore_replay_lab.json`.
- F113 — Domain Portability Lab — `f113_domain_portability_lab.json`.
- F114 — Security Regression Suite — `f114_security_regression_suite.json`; `f114_sandbox_escape_regression_report.json`.
- F114.G — Lab Mastery Gauntlet Closure Gate — `f114g_lab_mastery_gauntlet_closure_gate.json`.

## F115 — External Action SDK Contract & Review Lab

Prerequisite: F114.G PASS. Primary artifact: `f115_external_action_sdk_contract_review_lab.json`. This phase does not authorize marketplace, plugin deployment, external developer onboarding, hot-load, or productive external action.

## F116A-F116E — Evidence Bundle Certification

- F116A — Evidence Inventory Gate — `f116a_evidence_inventory_gate.json`.
- F116B — Evidence Integrity Hash Gate — `f116b_evidence_integrity_hash_gate.json`.
- F116C — Evidence Completeness Gate — `f116c_evidence_completeness_gate.json`; depends on F116A inventory.
- F116D — Evidence Replayability Gate — `f116d_evidence_replayability_gate.json`.
- F116E — Evidence Certification Closure Gate — `f116e_evidence_certification_closure_gate.json`.

## F117-F120 — Lab Mastery Closure

- F117 — Lab Scorecard Gate — `f117_lab_scorecard_gate.json`; `f117_scorecard_methodology.json`.
- F118 — False Completion Attack Gate — `f118_false_completion_attack_gate.json`.
- F119 — Pre-Productization Simulation Review — `f119_pre_productization_simulation_review.json`.
- F120 — Lab Mastery Closure Gate — `f120_lab_mastery_closure_gate.json`.

## F120 Final Thresholds

blocker_count=0; critical_security_failure_count=0; real_effect_count=0; simulation_pass_rate>=0.99; ledger_coverage=1.00; rollback_compensation_coverage=1.00; evidence_bundle_completeness=1.00; false_completion_bypass_count=0; domain_hardcode_count=0; known_unclassified_gap_count=0; owasp_agentic_asi_coverage=1.00; eu_ai_act_article_coverage=1.00; iso42001_clause_mapping_coverage=1.00; anonymous_agent_call_count=0; mcp_unauthenticated_call_count=0; high_risk_single_approver_count=0; unlogged_trust_decay_count=0; untraced_tool_call_count=0; goal_hijacking_undetected_count=0; clear_lab_to_production_gap_documented=true; aibom_completeness=1.00.

## OWASP Agentic ASI01-ASI10 Coverage

ASI01 Goal Hijacking: F36.C, F64.B, F105, F118. ASI02 Tool Misuse: F36.B, F53, F64.B, F105. ASI03 Identity Abuse: F45.B, F69, F70, F74, F108. ASI04 Supply Chain Risk: F78, F115. ASI05 Code Execution Risk: F43, F43.B, F59, F114. ASI06 Memory Poisoning: F72, F73, F107. ASI07 Insecure Communications: F36.B, F62, F74.C, F90, F105. ASI08 Cascading Failures: F44, F83, F106, F111. ASI09 Human-Agent Trust Exploitation: F37, F55, F64.B, F101, F110. ASI10 Rogue Agents: F45.B, F74, F74.B, F74.C, F108.

## EU AI Act Art. 9-17 Coverage

Art.9: R0, F64.B, F82, F117, F120. Art.10: F71.B, F72, F73, F92. Art.11: R0, F71, F116A-F116E. Art.12: F40, F57, F71.B, F102. Art.13: F71.B, F93, F110. Art.14: F37, F55, F70, F110. Art.15: F66, F66.B, F83, F114. Art.17: R0, F81, F82, F117, F120.

## ISO/IEC 42001 Coverage

AI Management System: R0, F71.C, F117, F120. Impact Assessment: F66.B, F71.B, F82. Control Selection: R0, F64.B, F71.C. Monitoring Loop: F68, F83, F86, F117. Documentation/Evidence: F71, F116A-F116E. Continuous Improvement: F96, F118, F119.

## Final Statement

F120 closes Lab Mastery. F120 does not authorize production. The next stage after F120 is F121+ Controlled Productization Gate, outside this roadmap.
