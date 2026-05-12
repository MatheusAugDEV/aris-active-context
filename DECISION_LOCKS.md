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
- F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline.

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
