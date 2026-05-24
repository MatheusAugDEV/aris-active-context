# Site Official ARIS Runbook
- Canonical file: `site-aris.md`
- Scope: official ARIS site / landing page workflow
- Repository: `/home/matheus/ARIS/aris-site`
- Public domains: `https://www.meetarisia.com.br` and `https://meetarisia.com.br`
- Use this runbook for build, commit, push, Vercel, and live asset validation steps.

## F21-CTX-BEDROCK-R29 - Validation Runner Controlled Execution Plan
R29 defines how R30 will execute the deterministic Bedrock request-validation runner against the real materialized fixture tree in dry-run mode.
It intentionally chooses a dedicated R30 script so implementation smoke and real-tree execution remain separate.
The plan keeps execution dry-run only, with no Bedrock verdict, no product/commercial approval, no runtime/network access, and no fixture mutation.
The planned write scope for R30 stays inside `artifacts/bedrock/runner/` only.

## R28 — Validation Runner Controlled Implementation Review Gate
R28 reviews the controlled implementation of the Bedrock request-validation runner.
It checks the module, script, tests, smoke path, import safety, deterministic rules, and fixture-tree protection, but it does not execute the real fixture tree or emit a Bedrock verdict.

## R27 — Validation Runner Controlled Implementation
R27 implements the controlled Bedrock request-validation runner in a stdlib-only form.
It creates the module, script, and tests, runs only a temporary smoke tree, and keeps the materialized Bedrock tree untouched.

## R26 — Validation Runner Controlled Implementation Plan
R26 defines the controlled implementation plan for the future Bedrock request-validation runner.
It is still plan-only: no code, no runner execution, no product/commercial allowance, and no fixture-tree mutation.

## Bedrock Evaluation Request Validation Runner Dry-Run Plan Review Gate
R25 reviews the R24 runner plan and confirms it is safe and complete enough for a future controlled implementation phase.
It is a plan review only: no runner is implemented, no fixtures are executed, and no Bedrock verdict is emitted.

## Bedrock Evaluation Request Validation Runner Dry-Run Plan
R24 defines the future deterministic runner that will compare actual request-validation results against the expected dry-run fixtures.
It is plan-only: the runner is not implemented, no fixtures are executed, and no Bedrock verdict is emitted.

## Bedrock Evaluation Request Fixture Controlled Materialization Review Gate
R23 reviews the controlled fixture tree and confirms it is safe and coherent for a future runner dry-run phase.
It validates the materialized manifest, pairings, counts, non-execution guarantees, and safety scan results, but it does not create a runner or execute Bedrock.

## Bedrock Evaluation Request Fixture Controlled Materialization
R22 materializes the controlled fixture tree only: manifest, 22 input fixtures, and 22 expected fixtures.
It does not create a runner, execute Bedrock, or authorize product promotion.

## Bedrock Evaluation Request Fixture Materialization Dry-Run Gate
R21 validates whether the future fixture materialization can proceed safely.
It is a readiness gate only: no fixture files are created, no runner exists yet, and no Bedrock evaluation is executed.

## Bedrock Evaluation Request Fixture Materialization Plan
R20 defines the safe plan for creating the future dry-run fixture files from the manifesto.
It keeps materialization separate from execution, and it does not create fixtures, runners, or Bedrock verdicts.

## Bedrock Evaluation Request Fixture Manifest Draft
R19 defines the canonical manifest for future dry-run fixtures that will test request-validation rules.
It lists the fixtures, priorities, coverage targets, and expected outcomes, but it does not materialize fixtures or run any Bedrock evaluation.

## Bedrock Evaluation Request Dry-Run Fixture Schema Draft
- R18 defines the schema for simulated fixtures that test request-validation rules.
- Fixtures represent valid, invalid, incomplete, ambiguous, lab-only, product-blocked, and commercial-blocked requests.
- Fixtures are dry-run only: they do not execute Bedrock, do not mutate runtime, and do not create real verdicts.
- The schema keeps fixtures small, auditable, and deterministic for a future runner.

## Bedrock Evaluation Request Validation Rules Draft
- R17 defines deterministic rules for deciding whether a Bedrock evaluation request may start.
- It validates identity, target, scope, source state, evidence references, source-of-truth, boundary assertions, risk, human review, non-goals, and rejection reasons.
- It does not run completeness, blocker, or verdict logic.
- It does not imply product pass.

## Bedrock Evaluation Input Contract Draft
- R16 defines the minimum valid request a future Bedrock evaluation must receive before any judgment can start.
- It is the input layer that sits in front of R12 through R15.
- The contract requires request identity, target identity, scope, source repositories, source commits, branch, worktree state, requested output artifacts, evidence references, risk references, human review references, and boundary assertions.
- The draft prevents Bedrock from starting on ambiguous, underspecified, stale, or improperly scoped requests.
- It does not execute a verdict, promote product, or mutate runtime.

## Strategic Orientation
- `NORTH_POLE.md` is the mandatory strategic guide for ARIS direction, excellence criteria, and decision quality.
- It complements, but does not replace, `DECISION_LOCKS.md`.

## Bedrock Gate boundary
- Bedrock Gate is the official separator between ARIS Lab / experimental / internal readiness and ARIS Produto / commercial-grade / user-facing readiness.
- A technical pass is not a product pass; promotion requires an explicit Bedrock verdict backed by evidence.
- The active lock is `BEDROCK_GATE_IS_GLOBAL_PRODUCT_BOUNDARY`, and the drafted criteria live in `BEDROCK_GATE.md`.
- The next recommended phase is `F21-CTX-BEDROCK-R12 - Bedrock Evidence Bundle Schema Draft`.

## Bedrock Verdict Criteria Draft
- R11 formalizes the verdict classes, critical dimensions, absolute blockers, and evidence minima for Bedrock.
- R11 does not execute the Bedrock runtime gate and does not authorize product promotion.
- The draft preserves the R10 global product boundary and prepares the schema needed for the future evidence bundle.

## Bedrock Evidence Bundle Schema Draft
- R12 formalizes the minimum material evidence package a future Bedrock verdict must receive.
- The schema covers identity, technical artifacts, validation, security, privacy, runtime boundaries, rollback, source-of-truth, completeness, and blocker scan material.
- R12 does not execute the Bedrock runtime gate and does not promote product.

## Bedrock Evidence Bundle Completeness Gate Draft
- R13 formalizes the deterministic threshold for deciding whether an evidence bundle is complete enough for Bedrock judgment.
- It classifies bundles as complete, incomplete, insufficient, contradictory, stale, invalid, or blocked for promotion.
- R13 does not execute the Bedrock runtime gate and does not promote product.

## Bedrock Blocker Scan Schema Draft
- R14 formalizes the internal schema used to represent the 14 canonical Bedrock blockers.
- It defines blocker states, severity, evidence quality, waiver policy, and the link to completeness gating.
- R14 does not execute a scanner runtime and does not promote product.

## Bedrock Verdict Artifact Schema Draft
- R15 formalizes the final canonical artifact emitted by future Bedrock judgments.
- It separates technical status from product boundary decision and ties the verdict back to the bundle, completeness and blocker scan.
- R15 does not execute a verdict and does not promote product.

**F21-A14 - MCP Candidate Human Evidence Authorization Review**
status: `mcp_candidate_human_evidence_authorization_review_warn`
decision: `warn`
authorization review classification: `authorization_review_not_ready_missing_real_evidence`
manual completion required: `True`
ready for authorization review: `False`
evidence present: `False`
pending fields: `11`
context index live block repaired: `True`
proxima fase recomendada: `F21-A15 — MCP Candidate Human Evidence Authorization Evidence Intake`
the authorization review does not authorize MCP activation without real human evidence
legacy evidence remains historical and is not used as active input
**F21-A13 - MCP Candidate Human Evidence Manual Completion Intake**
status: `mcp_candidate_human_evidence_manual_completion_intake_warn`
decision: `warn`
manual completion intake classification: `placeholder_manual_completion_intake`
manual completion required: `True`
ready for authorization review: `False`
manual completion intake hash: `sha256:ca20303ba1f2b1202c98750929652c1ff808ecdd4fd4c7e2cbbd5128b229285f`
pending fields: `11`
context index live block repaired: `True`
proxima fase recomendada: `F21-A14 — MCP Candidate Human Evidence Authorization Review`
the intake packet is manual-only and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A12 - MCP Candidate Human Evidence Manual Completion Packet**
status: `mcp_candidate_human_evidence_manual_completion_packet_warn`
decision: `warn`
manual completion packet classification: `placeholder_manual_completion_packet`
manual completion required: `True`
ready for authorization review: `False`
manual completion packet hash: `sha256:8429ceab941008819c5ea729ab40a05a019490fcda87a64d03ea0421189840dd`
pending fields: `11`
context index live block repaired: `True`
proxima fase recomendada: `F21-A13 — MCP Candidate Human Evidence Manual Completion Intake`
the packet is manual-only and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A11 - MCP Candidate Human Evidence Completion Review Gate**
status: `mcp_candidate_human_evidence_completion_review_gate_warn`
decision: `warn`
completion review classification: `placeholder_completion_reviewed`
manual completion required: `True`
ready for authorization review: `False`
completed candidate hash: `sha256:8592276f5d418e9ecc003f1b7d2617d8111d418b4d88cb1ed4f358504b49be1c`
pending fields: `11`
pending package: `artifacts/f21/mcp_candidate_human_evidence_completion_review_pending_package.json`
proxima fase recomendada: `F21-A12 — MCP Candidate Human Evidence Manual Completion Packet`
the review gate preserves placeholders and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A11 - MCP Candidate Human Evidence Completion Review Gate**
status: `mcp_candidate_human_evidence_completion_review_gate_warn`
decision: `warn`
completion review classification: `rejected_sensitive_or_unsafe`
manual completion required: `True`
ready for authorization review: `False`
completed candidate hash: `sha256:8592276f5d418e9ecc003f1b7d2617d8111d418b4d88cb1ed4f358504b49be1c`
pending fields: `11`
pending package: `artifacts/f21/mcp_candidate_human_evidence_completion_review_pending_package.json`
proxima fase recomendada: `F21-A12 — MCP Candidate Human Evidence Manual Completion Packet`
the review gate preserves placeholders and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A11 - MCP Candidate Human Evidence Completion Review Gate**
status: `mcp_candidate_human_evidence_completion_review_gate_blocked`
decision: `blocked`
completion review classification: `rejected_sensitive_or_unsafe`
manual completion required: `True`
ready for authorization review: `False`
completed candidate hash: `sha256:8592276f5d418e9ecc003f1b7d2617d8111d418b4d88cb1ed4f358504b49be1c`
pending fields: `11`
pending package: `artifacts/f21/mcp_candidate_human_evidence_completion_review_pending_package.json`
proxima fase recomendada: `F21-A12 — MCP Candidate Human Evidence Manual Completion Packet`
the review gate preserves placeholders and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A10 - MCP Candidate Human Evidence Completion Apply**
status: `mcp_candidate_human_evidence_completion_apply_warn`
decision: `warn`
completion apply classification: `placeholder_completion_applied`
manual completion required: `True`
ready for authorization review: `False`
completed candidate hash: `sha256:8592276f5d418e9ecc003f1b7d2617d8111d418b4d88cb1ed4f358504b49be1c`
pending fields: `11`
proxima fase recomendada: `F21-A11 — MCP Candidate Human Evidence Completion Review Gate`
the completed candidate preserves placeholders and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A9 - MCP Candidate Human Evidence Completion Review**
status: `mcp_candidate_human_evidence_completion_review_warn`
decision: `warn`
active submission present: `True`
active submission uses placeholders: `True`
completion classification: `placeholder_incomplete`
proxima fase recomendada: `F21-A10 — MCP Candidate Human Evidence Completion Apply`
active submission remains review-only and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A8R - Active-Context Push & Handoff Reconciliation Gate**
status: `f21a8r_active_context_push_handoff_reconciliation_gate_ready`
decision: `pass`
root repo commit: `30cecee44bf291a2963b6d085473f76b3b1fe705`
active-context commit: `a5141c6831fab356e62b67d4ea0a21578189c05d`
remote sync verified: `True`
proxima fase recomendada: `F21-A9 — MCP Candidate Human Evidence Completion Review`
active-context is synchronized and still points to F21-A9
**F21-A8 - MCP Candidate Human Evidence Submission Apply**
status: `mcp_candidate_human_evidence_submission_apply_warn`
decision: `warn`
active submission created: `True`
active submission uses placeholders: `True`
legacy evidence detected: `True`
proxima fase recomendada: `F21-A9 — MCP Candidate Human Evidence Completion Review`
active submission is review-only and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
**F21-A7 - MCP Candidate Evidence Review Gate**
status: `mcp_candidate_evidence_review_gate_warn`
decision: `warn`
candidate evidence classification: `missing`
active submission present: `False`
legacy evidence detected: `True`
proxima fase recomendada: `F21-A8 — MCP Candidate Human Evidence Submission Apply`
active submission is review-only and does not authorize MCP activation
legacy evidence remains historical and is not used as active input
## Current snapshot
- Latest completed phase: `F21-A6 — Obsidian MCP Human Evidence Intake`
- Status: `obsidian_mcp_human_evidence_intake_warn`
- Decision: `warn`
- Human evidence classification: `missing`
- Human evidence hash: `sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Blocker count: `0`
- Warning count: `3`
- Next recommended phase: `F21-A7 — MCP Candidate Evidence Review Gate`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A6 — Obsidian MCP Human Evidence Intake`
- Status: `obsidian_mcp_human_evidence_intake_blocked`
- Decision: `blocked`
- Human evidence classification: `rejected_sensitive_or_unsafe`
- Human evidence hash: `sha256:19bb985d2f2fe2a9a32e45cf59e7a1b0615cefa1bbd117dc1f34d657e88647d8`
- Blocker count: `2`
- Warning count: `2`
- Next recommended phase: `F21-A7 — MCP Candidate Evidence Review Gate`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A5 — Source-of-Truth Precedence Gate`
- Status: `source_of_truth_precedence_gate_warn`
- Decision: `warn`
- Blocker count: `0`
- Warning count: `0`
- Next recommended phase: `F21-A6 — Obsidian MCP Human Evidence Intake`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A5 — Source-of-Truth Precedence Gate`
- Status: `source_of_truth_precedence_gate_ready`
- Decision: `pass`
- Blocker count: `0`
- Warning count: `0`
- Next recommended phase: `F21-A6 — Obsidian MCP Human Evidence Intake`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A5 — Source-of-Truth Precedence Gate`
- Status: `source_of_truth_precedence_gate_blocked`
- Decision: `blocked`
- Blocker count: `1`
- Warning count: `0`
- Next recommended phase: `F21-A6 — Obsidian MCP Human Evidence Intake`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A4 — Context Budget Policy Gate`
- Status: `context_budget_policy_gate_ready`
- Decision: `pass`
- Blocker count: `0`
- Warning count: `0`
- Next recommended phase: `F21-A5 — Source-of-Truth Precedence Gate`

- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved
## Current snapshot
- Latest completed phase: `F21-A3 — Claude Code Instruction Alignment`
- Status: `claude_code_instruction_alignment_ready`
- Decision: `pass`
- Blocker count: `0`
- Warning count: `0`
- Next recommended phase: `F21-A4 — Context Budget Policy Gate`

- runtime/product/network/MCP/Obsidian/vault remain blocked
- active-context final update, commit hash, and push reporting are explicit
- historical snapshots below remain preserved

## Current snapshot
- Latest completed phase: `F21-A1 — Context Source Access Policy & Untrusted Input Boundary`
- Status: `f21_a1_context_source_access_policy_ready_with_warnings`
- Decision: `warn`
- Blocker count: `0`
- Warning count: `4`
- Next recommended phase: `F21-A2 — Codex Skill Alignment Review`

- runtime/product/network/MCP/Obsidian/vault remain blocked
- historical snapshots below remain preserved

## Current snapshot
- Latest completed phase: `F21-A1 — Context Source Access Policy & Untrusted Input Boundary`
- Status: `f21_a1_context_source_access_policy_blocked`
- Decision: `blocked`
- Blocker count: `2`
- Warning count: `4`
- Next recommended phase: `F21-A2 — Codex Skill Alignment Review`

- runtime/product/network/MCP/Obsidian/vault remain blocked
- historical snapshots below remain preserved

## Current snapshot
- Latest completed phase: `F21-A1 — Context Source Access Policy & Untrusted Input Boundary`
- Status: `f21_a1_context_source_access_policy_blocked`
- Decision: `blocked`
- Blocker count: `3`
- Warning count: `4`
- Next recommended phase: `F21-A2 — Codex Skill Alignment Review`

- runtime/product/network/MCP/Obsidian/vault remain blocked
- historical snapshots below remain preserved

## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P26 — Artifact Reference-Only Controlled Apply Final Authorization Gate`
- Status: `artifact_reference_only_controlled_apply_final_authorization_warn`
- Final authorization class: `final_authorization_granted_for_controlled_apply_next_phase_with_warnings`
- Final authorization granted: `True`
- Controlled apply authorized for next phase: `True`
- P25 final review verified: `True`
- Human decision kind: `APPROVE`
- Request id: `ARIS-P23-5bb468e12b5dcdbf`
- Request hash: `f20b42bc3f19635147e9008dbc0a28a77e224c4a93278c840ac84797dd200914`
- Warning count: `13`
- Blocker count: `0`
- Historical duplicate status warning: `True`
- Next authorized phase: `ARIS-CONTEXT-P27 — Artifact Reference-Only Controlled Apply Execution Preflight Gate`

- runtime/product/network/MCP/Obsidian/vault remain blocked and apply is still not executed here
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P25 — Artifact Reference-Only Controlled Apply Human Authorization Final Review Gate`
- Status: `artifact_reference_only_controlled_apply_human_authorization_final_review_warn`
- Human authorization final review class: `human_authorization_final_review_passed_with_warnings`
- Human authorization final review passed: `True`
- Human decision kind: `APPROVE`
- Request id: `ARIS-P23-5bb468e12b5dcdbf`
- Request hash: `f20b42bc3f19635147e9008dbc0a28a77e224c4a93278c840ac84797dd200914`
- Warning count: `13`
- Blocker count: `0`
- Next authorized phase: `ARIS-CONTEXT-P26 — Artifact Reference-Only Controlled Apply Final Authorization Gate`

- runtime/product/network/MCP/Obsidian/vault remain blocked
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P24-H1 — Artifact Reference-Only Controlled Apply Human Decision Submission`
- Status: `artifact_reference_only_controlled_apply_human_decision_submission_warn`
- Human decision submission class: `human_decision_submission_ready_for_final_review`
- Human decision present: `True`
- Human decision submitted: `True`
- Human decision valid: `True`
- Human decision kind: `APPROVE`
- Human decision operator name: `Matheus Augusto`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P25 — Artifact Reference-Only Controlled Apply Human Authorization Final Review Gate`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P24 — Artifact Reference-Only Controlled Apply Human Authorization Decision Intake Gate`
- Status: `artifact_reference_only_controlled_apply_human_authorization_decision_intake_warn`
- Human authorization decision intake class: `human_authorization_decision_intake_pending_submission`
- Human authorization request created: `True`
- Human authorization request status: `PENDING_NOT_SUBMITTED`
- Human authorization request submitted: `False`
- Human decision present: `False`
- Human decision valid: `False`
- Human decision kind: `PENDING`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P24-H1 — Artifact Reference-Only Controlled Apply Human Decision Submission`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P23 — Artifact Reference-Only Controlled Apply Human Authorization Request Gate`
- Status: `artifact_reference_only_controlled_apply_human_authorization_request_warn`
- Human authorization request class: `human_authorization_request_ready_with_warnings`
- Human authorization request created: `True`
- Human authorization request status: `PENDING_NOT_SUBMITTED`
- Human authorization request submitted: `False`
- Human authorization present: `False`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P24 — Artifact Reference-Only Controlled Apply Human Authorization Decision Intake Gate`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P22 — Artifact Reference-Only Controlled Apply Authorization Package Review Gate`
- Status: `artifact_reference_only_controlled_apply_authorization_package_review_warn`
- Authorization package review class: `authorization_package_review_passed_with_warnings`
- Authorization package review passed: `True`
- Authorization granted now: `False`
- Human authorization required: `True`
- Human authorization present: `False`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P23 — Artifact Reference-Only Controlled Apply Human Authorization Request Gate`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P21 — Artifact Reference-Only Controlled Apply Authorization Package`
- Status: `artifact_reference_only_controlled_apply_authorization_package_warn`
- Authorization package class: `authorization_package_ready_with_warnings`
- Authorization package created: `True`
- Authorization granted now: `False`
- Human authorization required: `True`
- Human authorization present: `False`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P22 — Artifact Reference-Only Controlled Apply Authorization Package Review Gate`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P20 — Artifact Reference-Only Controlled Apply Final Readiness Gate`
- Status: `artifact_reference_only_controlled_apply_final_readiness_gate_warn`
- Final readiness class: `ready_with_warnings_for_controlled_apply_authorization_package`
- Readiness for future authorization package: `True`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P21 — Artifact Reference-Only Controlled Apply Authorization Package`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P20 — Artifact Reference-Only Controlled Apply Final Readiness Gate`
- Status: `artifact_reference_only_controlled_apply_final_readiness_gate_blocked`
- Final readiness class: `blocked_before_authorization_package`
- Readiness for future authorization package: `False`
- Controlled apply allowed now: `False`
- Real apply allowed now: `False`
- Live context rewrite allowed now: `False`
- Bedrock verdict: `WARN`
- Next authorized phase: `ARIS-CONTEXT-P20-R1 — Artifact Reference-Only Controlled Apply Final Readiness Repair Review`

Runtime, product promotion, network, MCP, Obsidian bulk read, and vault write remain blocked.
## Current snapshot
- Latest completed phase: `ARIS-CONTEXT-P19 — Artifact Reference-Only Controlled Apply Dry-Run Validation Harness`.
- Next authorized phase: `ARIS-CONTEXT-P20 — Artifact Reference-Only Controlled Apply Final Readiness Gate`.
- P18 dry-run verified: `True`.
- Real apply remains false: `False`.
- Bedrock verdict: `WARN` with preparation exception `True`.
- Product promotion remains false.
- Runtime mutation, network use, dependency install, MCP activation, Obsidian bulk read, and Vault write remain blocked.
# aris-active-context

Compact, read-first ARIS context entrypoint.

Current governance note:

- BOOT.md read-first entry point contract is materialized and is now the lightweight handoff point before P2.
- Canonical roadmap anchor: `ARIS_ROADMAP_R0_F120.md`
- Next recommended phase: `ARIS-CONTEXT-P2 — Context OS Token Economy Baseline Diagnostic`

Read order:
1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `ARIS_ROADMAP_R0_F120.md`
7. `OPERATOR_PREFERENCES.md`
8. `PROMPT_CONTRACT.md`

## Current snapshot

- Latest completed phase: `ARIS-CONTEXT-P1 — BOOT.md Read-First Entry Point Contract`.
- Canonical roadmap: `ARIS_ROADMAP_R0_F120.md`.
- Roadmap status: `PASS by conservative review`.
- Next authorized phase: `ARIS-CONTEXT-P2 — Context OS Token Economy Baseline Diagnostic`.
- `ARIS-BEDROCK-C7` remains blocked until `R0 = PASS`.
- Bedrock executable engine readiness: `45/100`.
- Bedrock Gate remains declared but non-executable.
- F33 remains paused under Lab governance.
- F51+ remains advisory-only.
- Product promotion remains false.
- Runtime mutation, SQLite schema apply, SQLite connect, FTS5 creation, network, dependency install, MCP activation, Obsidian bulk-read, and Vault write remain blocked.

## Roadmap rule

F120 closes Lab Mastery only. F120 does not authorize production. Any real productization requires future `F121+ Controlled Productization Gate`.

## Rules

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
# aris-active-context

Compact, read-first ARIS context entrypoint.

Current governance note:

- R0 governance foundation is materialized and is now the active handoff point before C7.
- Canonical roadmap anchor: `ARIS_ROADMAP_R0_F120.md`
- Next recommended phase: `ARIS-BEDROCK-C7 — Evidence Pack Completeness Evaluator`

Read order:
1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `ARIS_ROADMAP_R0_F120.md`
7. `OPERATOR_PREFERENCES.md`
8. `PROMPT_CONTRACT.md`

## Current snapshot

- Latest completed phase: `ARIS-BEDROCK-C6 — Read-First & Source-of-Truth Compliance Evaluator`.
- Canonical roadmap: `ARIS_ROADMAP_R0_F120.md`.
- Roadmap status: `PASS by conservative review`.
- Next authorized phase: `ARIS-ROADMAP-R0 — Governance Foundation`.
- `ARIS-BEDROCK-C7` is blocked until `R0 = PASS`.
- Bedrock executable engine readiness: `45/100`.
- Bedrock Gate remains declared but non-executable.
- F33 remains paused under Lab governance.
- F51+ remains advisory-only.
- Product promotion remains false.
- Runtime mutation, SQLite schema apply, SQLite connect, FTS5 creation, network, dependency install, MCP activation, Obsidian bulk-read, and Vault write remain blocked.

## Roadmap rule

F120 closes Lab Mastery only. F120 does not authorize production. Any real productization requires future `F121+ Controlled Productization Gate`.

## Rules

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
