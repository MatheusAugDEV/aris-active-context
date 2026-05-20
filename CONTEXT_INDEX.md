## F21-A27 Real MCP Candidate Evidence Resolution References
- phase_id: `F21-A27`
- next_real_action: `F21-A28 — Real MCP Candidate Selection Intake`
- resolution_hash: `sha256:bf2cc2db0316514fc72271946cbaf568c353ff3859815dffe2062bab38504096`
- selection_template_hash: `sha256:341cbbfdfa392b6b9047f3cb7c3f6be90a79ab93fbcaf42c2ba60ec427632d78`
- selection_input_hash: `sha256:e46f3eceb3bd88fc6e16327af41d0a856faa2fb42b1a09312aa8daa0bb306980`

The loop is resolved by selecting a real candidate intake path, not by authorizing MCP activation.

## F21-A27 Real MCP Candidate Evidence Resolution References
- phase_id: `F21-A27`
- next_real_action: `F21-A28 — Real MCP Candidate Selection Intake`
- resolution_hash: `sha256:0efac3c35844fb70cda4d8d40f84e24b107bd35424089448ace755f3e5629fc6`
- selection_template_hash: `sha256:341cbbfdfa392b6b9047f3cb7c3f6be90a79ab93fbcaf42c2ba60ec427632d78`
- selection_input_hash: `sha256:e46f3eceb3bd88fc6e16327af41d0a856faa2fb42b1a09312aa8daa0bb306980`

The loop is resolved by selecting a real candidate intake path, not by authorizing MCP activation.

## F21-A26 MCP Candidate Human Evidence Authorization Review References
- phase_id: `F21-A26`
- next_real_action: `Pause MCP track and return to next context/lab gate`
- review_record_hash: `sha256:b19e7998d004caa9a4f6031c9a19b0af83e67bba79b4968d7ba9e0e8b57dcb18`
- closure_hash: `sha256:e9a894be55ba5c13c2c32d5b271377551c80655394c8e3feeb7e098437d71559`

The evidence loop is closed without authorizing MCP activation.

## F21-A25 MCP Candidate Human Evidence Authorization Evidence Repair Review References
- phase_id: `F21-A25`
- next_recommended_phase: `F21-A26 — MCP Candidate Human Evidence Authorization Review`
- review_record_hash: `sha256:78db4bf1c59393a678f02bf57922b01985f62ae697091d7045f29d4e85050340`

The repair review confirms the pending input is insufficient and does not authorize MCP activation.

## F21-A24 MCP Candidate Human Evidence Authorization Evidence Repair References
- phase_id: `F21-A24`
- next_recommended_phase: `F21-A25 — MCP Candidate Human Evidence Authorization Evidence Repair Review`
- repair_hash: `sha256:c97bc32cbed315a562c88d43910d6829a23dfabb6c5a2367ae4c565ca040740f`

The input is pending human review and does not authorize MCP activation.

## Live operational references
- current_macroblock: `MB1 — Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-A23 — MCP Candidate Human Evidence Authorization Evidence Validation`
- latest_status: `mcp_candidate_human_evidence_authorization_evidence_validation_warn`
- latest_decision: `warn`
- next_operational_gate: `F21-A24 — MCP Candidate Human Evidence Authorization Evidence Repair`
- validation_created: `true`
- evidence_present: `false`
- ready_for_authorization_review: `false`
- candidate_approval_allowed: `false`
- mcp_activation_allowed: `false`
- context_index_live_block_stale_detected: `true`
- context_index_live_block_repaired: `true`

The live operational references pointer has been repaired to the F21-A22/F21-A23 boundary and the A23 validation is indexed below.

## F21-A23 MCP Candidate Human Evidence Authorization Evidence Validation References
- phase_id: `F21-A23`
- phase_doc: `docs/fase21/f21a_a23_mcp_candidate_human_evidence_authorization_evidence_validation.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_a23_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_a23_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_a23_report.md`
- validation_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_a23.json`
- validation_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_a23.md`
- next_recommended_phase: `F21-A24 — MCP Candidate Human Evidence Authorization Evidence Repair`
- validation_hash: `sha256:fc81e970b83fad823fc2c6dd08134a6c25d9837bf580d52ee462f8c44425e418`

## F21-A23 Notes
- Validation only confirms whether real human evidence exists after the intake.
- Missing evidence stays a conservative warning and does not authorize MCP activation.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A22 MCP Candidate Human Evidence Authorization Evidence Intake References
- phase_id: `F21-A22`
- phase_doc: `docs/fase21/f21a_a22_mcp_candidate_human_evidence_authorization_evidence_intake.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22_report.md`
- intake_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22.json`
- intake_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22.md`
- template_json_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_intake_a22_template.json`
- template_md_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_intake_a22_template.md`
- checklist_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22_checklist.json`
- checklist_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_intake_a22_checklist.md`
- next_recommended_phase: `F21-A23 — MCP Candidate Human Evidence Authorization Evidence Validation`
- authorization_evidence_intake_hash: `sha256:126b6cdd25173947d28ac3ef4aa9cc65b2412acc329076b987b736d02f7dca4f`

## F21-A22 Notes
- The authorization evidence intake materializes a safe template and checklist when no real evidence exists.
- Pending fields remain explicit and human-completable; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A21 MCP Candidate Human Evidence Authorization Review References
- phase_id: `F21-A21`
- phase_doc: `docs/fase21/f21a_a21_mcp_candidate_human_evidence_authorization_review.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_a21_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_a21_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_a21_report.md`
- review_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_a21.json`
- review_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_review_a21.md`
- next_recommended_phase: `F21-A22 — MCP Candidate Human Evidence Authorization Evidence Intake`
- authorization_review_hash: `sha256:706943fceacacd953ec8c4f94c0dc9fb359fec5928e5232645ef753db5ab1750`

## F21-A21 Notes
- The authorization review remains conservative and review-only.
- Real human evidence is required before authorization review can be promoted.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A20 MCP Candidate Human Evidence Authorization Evidence Repair Apply Review References
- phase_id: `F21-A20`
- phase_doc: `docs/fase21/f21a_a20_mcp_candidate_human_evidence_authorization_evidence_repair_apply_review.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_review_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_review_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_review_report.md`
- review_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_review.json`
- review_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_review.md`
- next_recommended_phase: `F21-A21 — MCP Candidate Human Evidence Authorization Review`
- review_record_hash: `sha256:91bab0b7b8247e83e87c6ee24049878944c422e222b47139de6a960415da83f3`

## F21-A20 Notes
- The repair apply review confirms the scaffold remains safe for manual completion.
- Placeholders remain placeholders; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A19 MCP Candidate Human Evidence Authorization Evidence Repair Apply References
- phase_id: `F21-A19`
- phase_doc: `docs/fase21/f21a_a19_mcp_candidate_human_evidence_authorization_evidence_repair_apply.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_report.md`
- apply_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply.json`
- apply_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply.md`
- manifest_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_manifest.json`
- manifest_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_manifest.md`
- checklist_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_checklist.json`
- checklist_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_apply_checklist.md`
- next_recommended_phase: `F21-A20 — MCP Candidate Human Evidence Authorization Evidence Repair Apply Review`
- repair_apply_hash: `sha256:e8105caf073277f7a4c09e0b7992e38bf0e4c3e8606e549c3b292648edeed2a6`

## F21-A19 Notes
- The repair apply confirms the scaffold remains safe for manual completion.
- Placeholders remain placeholders; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A18 MCP Candidate Human Evidence Authorization Evidence Repair Review References
- phase_id: `F21-A18`
- phase_doc: `docs/fase21/f21a_a18_mcp_candidate_human_evidence_authorization_evidence_repair_review.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_review_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_review_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_review_report.md`
- review_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_review.json`
- review_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_review.md`
- next_recommended_phase: `F21-A19 — MCP Candidate Human Evidence Authorization Evidence Repair Apply`
- review_record_hash: `sha256:94ce2fa577a4f683ef4d2009861e9400739b339ca9d1371ba982314ad124666e`

## F21-A18 Notes
- The repair review confirms the package remains a safe manual-completion scaffold.
- Placeholders remain placeholders; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A17 MCP Candidate Human Evidence Authorization Evidence Repair References
- phase_id: `F21-A17`
- phase_doc: `docs/fase21/f21a_a17_mcp_candidate_human_evidence_authorization_evidence_repair.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_report.md`
- repair_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair.json`
- repair_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair.md`
- repair_checklist_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_checklist.json`
- repair_checklist_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_repair_checklist.md`
- template_json_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_repair_template.json`
- template_md_artifact: `artifacts/f21/templates/mcp_candidate_human_evidence_authorization_evidence_repair_template.md`
- next_recommended_phase: `F21-A18 — MCP Candidate Human Evidence Authorization Evidence Repair Review`
- repair_package_hash: `sha256:242e84bd6ded687957c0ffa2d5caebd79a3d5c7e58e821a6d858daf6867e0d0c`

## F21-A17 Notes
- The repair package makes missing evidence explicit and actionable.
- Pending fields remain human-completable; no evidence is invented.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

## F21-A16 MCP Candidate Human Evidence Authorization Evidence Validation References
- phase_id: `F21-A16`
- phase_doc: `docs/fase21/f21a_a16_mcp_candidate_human_evidence_authorization_evidence_validation.md`
- decision_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_decision.json`
- summary_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_summary.json`
- report_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation_report.md`
- validation_json_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation.json`
- validation_md_artifact: `artifacts/f21/mcp_candidate_human_evidence_authorization_evidence_validation.md`
- next_recommended_phase: `F21-A17 — MCP Candidate Human Evidence Authorization Evidence Repair`
- validation_record_hash: `sha256:06f22a2c15405ae8d9a479b4a198c9b2361758b45f9af9bc0e40c3bd4b96bd0f`

## F21-A16 Notes
- Validation only confirms whether real human evidence exists and is safe enough for review.
- Missing evidence stays a conservative warning and does not authorize MCP activation.
- Legacy evidence remains historical only and is not used as active input.
- MCP activation remains blocked.

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
