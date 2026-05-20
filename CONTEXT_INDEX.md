## Live operational references
- current_macroblock: `MB1 — Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-A15 — MCP Candidate Human Evidence Authorization Evidence Intake`
- latest_status: `mcp_candidate_human_evidence_authorization_evidence_intake_warn`
- latest_decision: `warn`
- next_operational_gate: `F21-A16 — MCP Candidate Human Evidence Authorization Evidence Validation`
- template_created: `true`
- ready_for_authorization_review: `false`
- candidate_approval_allowed: `false`
- mcp_activation_allowed: `false`
- context_index_live_block_stale_detected: `true`
- context_index_live_block_repaired: `true`

The live operational references pointer has been repaired to the F21-A14/F21-A15 boundary and the A15 intake is indexed below.

## F21-A15 MCP Candidate Human Evidence Authorization Evidence Intake References
- phase_id: `F21-A15`
- phase_doc: `docs/fase21/f21a_a15_mcp_candidate_human_evidence_authorization_evidence_intake.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_report.md`
- intake_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake.json`
- intake_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake.md`
- template_json_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_intake_template.json`
- template_md_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_intake_template.md`
- next_recommended_phase: `F21-A16 — MCP Candidate Human Evidence Authorization Evidence Validation`
- authorization_evidence_intake_hash: `sha256:9e8fb93cee7efa23b459df6dd3d6cde54e892721ae36d75acc3cc8612d69cbc8`

## F21-A15 Notes
- The authorization evidence intake materializes a safe template when no real evidence exists.
- Pending fields remain explicit and human-completable; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A14 MCP Candidate Human Evidence Authorization Review References
- phase_id: `F21-A14`
- phase_doc: `docs/fase21/f21a_a14_mcp_candidate_human_evidence_authorization_review.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_report.md`
- manual_completion_input_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_input.json`
- next_recommended_phase: `F21-A15 — MCP Candidate Human Evidence Authorization Evidence Intake`
- manual_completion_input_hash: `None`

## F21-A14 Notes
- The authorization review remains manual-review-only.
- Real human evidence is required before any authorization review can be promoted.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A13 MCP Candidate Human Evidence Manual Completion Intake References
- phase_id: `F21-A13`
- phase_doc: `docs/fase21/f21a_a13_mcp_candidate_human_evidence_manual_completion_intake.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_intake_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_intake_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_intake_report.md`
- intake_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_intake.json`
- intake_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_intake.md`
- next_recommended_phase: `F21-A14 — MCP Candidate Human Evidence Authorization Review`
- manual_completion_intake_hash: `sha256:ca20303ba1f2b1202c98750929652c1ff808ecdd4fd4c7e2cbbd5128b229285f`

## F21-A13 Notes
- The intake packet is a manual completion scaffold and remains manual-review-only.
- Pending fields are grouped for human completion without inventing real evidence.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A12 MCP Candidate Human Evidence Manual Completion Packet References
- phase_id: `F21-A12`
- phase_doc: `docs/fase21/f21a_a12_mcp_candidate_human_evidence_manual_completion_packet.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_packet_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_packet_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_packet_report.md`
- packet_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_packet.json`
- packet_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_manual_completion_packet.md`
- next_recommended_phase: `F21-A13 — MCP Candidate Human Evidence Manual Completion Intake`
- manual_completion_packet_hash: `sha256:8429ceab941008819c5ea729ab40a05a019490fcda87a64d03ea0421189840dd`

## F21-A12 Notes
- The packet is a manual completion scaffold and remains manual-review-only.
- Pending fields are grouped for human completion without inventing real evidence.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A11 MCP Candidate Human Evidence Completion Review Gate References
- phase_id: `F21-A11`
- phase_doc: `docs/fase21/f21a_a11_mcp_candidate_human_evidence_completion_review_gate.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_review_gate.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_review_gate_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_review_gate_report.md`
- pending_package_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_review_pending_package.json`
- pending_package_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_review_pending_package.md`
- next_recommended_phase: `F21-A12 — MCP Candidate Human Evidence Manual Completion Packet`

## F21-A11 Notes
- The completed candidate remains placeholder-safe and manual-review-only.
- Pending fields are catalogued for human completion without inventing real evidence.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.
## F21-A10 MCP Candidate Human Evidence Completion Apply References
- phase_id: `F21-A10`
- phase_doc: `docs/fase21/f21a_a10_mcp_candidate_human_evidence_completion_apply.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_apply.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_apply_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_apply_report.md`
- completed_candidate_artifact: `artifacts/f21/obsidian_mcp_human_evidence_submission_completed_candidate.json`
- pending_fields_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_pending_fields.json`
- pending_fields_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_completion_pending_fields.md`

## Live notes

- The active submission remains placeholder/manual and is still review-only.
- Legacy evidence remains historical and does not override the active submission path.
- MCP activation remains blocked.
- Runtime/product/customer-real work remains blocked.
- NEXT_ACTION remains F21-A11 and does not point to MB8/MB9.

## Active governance references

- source_of_truth_policy: `docs/architecture/source_of_truth_policy.md`
- roadmap_macroblocks: `docs/roadmap/roadmap_macroblocks.md`
- roadmap_r0_f120: `docs/roadmap/roadmap_macroblocks_r0_f120.md`
- active_context_current_state: `CURRENT_STATE.md`
- active_context_next_action: `NEXT_ACTION.md`
- active_context_decision_locks: `DECISION_LOCKS.md`
- active_context_phase_ledger: `ARIS_PHASE_LEDGER.md`

## Future roadmap concept recorded

- concept_id: `MB8_MB9_INFERNUS_FINAL_CONCEPT`
- MB8: `ARIS Infernus Lab — Os 13 Pecados Capitais do ARIS`
- MB9: `ARIS Final Crisol — Evidence Certification, False-Completion Defense & Pre-Productization Gate`
- decision: `ADOTAR_COM_GATES`
- concept_status: `PASS with documented WARNs`
- implementation_allowed_now: `false`
- bot_implementation_allowed_now: `false`
- harness_implementation_allowed_now: `false`
- productization_allowed_now: `false`

## 13 Pecados Capitais index

| ID | Codename | Technical bot |
|---|---|---|
| BOT-001 | `Quimera` | Normal User Bot |
| BOT-002 | `Dúbio` | Ambiguous / Changing Intent Bot |
| BOT-003 | `Elos` | Policy-Infeasible Request Bot |
| BOT-004 | `Taipan` | Adversarial Injection Bot |
| BOT-005 | `Labirinto` | Trajectory Hazard Bot |
| BOT-006 | `Vitium` | Offline / Provider Failure Bot |
| BOT-007 | `Gula` | Cost / Unbounded Consumption Bot |
| BOT-008 | `Apep` | False Completion Attacker Bot |
| BOT-009 | `Patrono` | Business Owner / Operator Bot |
| BOT-010 | `Éfeso` | Long-Horizon Drift Bot |
| BOT-011 | `Abzu` | Internal Privacy Leak Bot |
| BOT-012 | `Loop` | Replay & Mutation Reviewer Bot |
| BOT-013 | `Minos` | Auditor / Evidence Verifier Bot |

## Required future implementation research references

- deterministic_metric_for_efeso_long_horizon_drift: `pending`
- deterministic_sensitive_data_scanner_for_abzu: `pending`
- replay_policy_bit_exact_vs_semantic_equivalence_for_loop: `pending`
- gula_envelope_calibration_from_quimera_baseline: `pending`
