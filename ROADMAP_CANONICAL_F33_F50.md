# ROADMAP CANONICAL F33-F50

Status: CANONICAL / ACTIVE
Activated in: F32.RESEARCH-P5
Date: 2026-05-11
Supersedes: ROADMAP_F30_F50.md
Operational next action remains: ARIS-LAB-A0 — Temporary F33 Pause, Bedrock Lab Authority Charter & F44 Roadmap Amendment

## Activation Guardrails

- This is the only active canonical roadmap file.
- ROADMAP_F30_F50.md is superseded and retained only as a tombstone plus archive pointer.
- F32 scope is still active; publication of this roadmap does not authorize F33 execution before formal F32 closure or deferral with integrity.
- F33 remains reserved as SQLite Memory, FTS5, Provenance & Evaluation Baseline.
- No runtime, frontend, audio, action runtime, MCP, network, or dependency mutation is authorized by this document.

## Global Action Runtime Chain Locks

- Action Registry is the source-of-truth for actions.
- Tool schemas are derived artifacts and never the authority layer.
- Typed plan plus typed approval are mandatory before execution.
- Immutable hashed plan plus deterministic preview are mandatory before side effects.
- Side effects require sidecar isolation, append-only ledger evidence, and rollback or compensation coverage.
- MCP write/command, auto-run, continuous learning/auto-retraining, and external vector DB as mandatory base remain prohibited.

## F33 — SQLite Memory, FTS5, Provenance & Evaluation Baseline

Scope:
- Trusted local memory with SQLite and FTS5.
- Mandatory provenance for stored facts.
- Validity window, stale detection, TTL, and fact-conflict handling.
- Evaluation baseline for retrieval quality.

Prohibited:
- External vector DB as mandatory base.
- Continuous learning.
- Auto-retraining.
- Memory without source attribution.

## F34 — Typed Plan Schema, Action Registry & Permission Gate

Scope:
- Action Registry as source-of-truth.
- Tool schema derived from the registry, never source-of-truth.
- Typed plan contract.
- Permission modes and blast-radius review.
- Typed approval flow.

Prohibited:
- Auto-run.
- Direct dynamic tool calling.
- Generic approval without typed contract.

## F35 — Immutable Plan, Dry-Run Executor & Preview Contract

Scope:
- Immutable hashed plan.
- Deterministic preview.
- Dry-run without side effects.
- Mutation gate only after approval.

Prohibited:
- Execution without preview.
- Mutable plan after approval.
- Dry-run with real write side effects.

## F36 — Append-Only Ledger, Deterministic Replay & Gate Decision Audit

Scope:
- Append-only ledger with hash chain.
- Intent, plan, gate, approval, execution, and observation records.
- Deterministic decision replay.
- Forensic report generation.

Prohibited:
- Ledger overwrite.
- Loose logs as sole evidence.
- Ledger without redaction.

## F37 — Rollback, Saga Compensation & Recovery UX

Scope:
- Classify actions as reversible, compensable, or irreversible.
- Mandatory rollback plan.
- Saga compensation model.
- Recovery preview.

Prohibited:
- Mutable action without rollback or compensation.

## F38 — Sidecar Executor, Isolation Boundary & Kill-Switch

Scope:
- Side effects outside the main process.
- Sidecar process boundary.
- Timeout, path allowlist, and crash isolation.
- Kill-switch and quarantine.
- Default-deny egress.

Prohibited:
- Free shell.
- Subprocess without wrapper.
- Open network by default.
- Firecracker or gVisor as immediate requirement.

## F39 — Capability Handles, Skill Governance & MCP Hash-Pinned Registry

Scope:
- Capability handle contract.
- SkillCandidate schema.
- Trust tiers.
- MCP read-only registry.
- Hash-pinned registry and reapproval gate.

Dependencies:
- F32 must be formally closed or deferred with integrity before any real MCP or capability work.

Prohibited:
- MCP write or command mode.
- Hot-loaded skills.
- Marketplace plugin as core.
- Trust by tool name alone.

## F40 — Consolidated Local Automation Suite

Scope:
- Notes, calendar, and file operations under the new pipeline.
- Plan to dry-run to permission to sidecar to ledger to rollback execution path.

Prohibited:
- Real browser automation.
- Real email.
- Real external automation.
- Action without ledger.

## F41 — Internal & External Security Foundation

Scope:
- Secret boundary baseline.
- Dependency integrity baseline.
- Prompt and tool injection baseline.
- Initial SBOM.

Notes:
- Deep threat modeling, full license hardening, and external audit stay for F49.

Prohibited:
- Turn F41 into a giant blocking phase.

## F42 — Multi-Provider Model Gateway, Secret Boundary & Cost Control

Scope:
- Provider-neutral contract.
- Secret boundary.
- Fallback and circuit breaker.
- Budget and cost controls.
- Output normalization.
- Provider health checks.

Prohibited:
- API key in action runtime.
- Provider-specific logic scattered across the system.

## F43 — Response Engine 2.0, Evidence Audit & Cross-Model Review

Scope:
- Answer completeness.
- Anti-truncation behavior.
- Evidence-to-claim audit.
- Factuality and fallback policy.
- Advisory cross-model review.
- Local-only reviewer path.
- Reviewer bias mitigation.

Prohibited:
- Plausible unsupported success.
- Self-review as sole validation.
- Cross-model review as executor.

## F44 — ARIS Lab Hardening, Red-Team Expansion & Benchmark Maturity

Scope:
- expand golden suites
- expand red-team suites
- benchmark at scale
- validate Bedrock Gate under accumulated phase-to-phase evidence
- audit evaluation theater risk
- test demotion and obsolescence in practice
- harden Lab governance
- mature reliability score

Prohibited:
- treating F44 as initial Lab creation
- release without suites
- invented benchmark
- bypassing Bedrock Gate

## F45 — Operational Cockpit, Audit UI & Runtime Visibility

Scope:
- Status dashboard.
- Action preview.
- Permission and blast-radius panel.
- Ledger viewer.
- Rollback and replay timeline.
- Memory, model, and voice panels.

Prohibited:
- UI as source-of-truth.
- Button that bypasses a gate.

## F46 — Rich Output, Document Intelligence & Safe Attachments

Scope:
- Safe markdown.
- Tables and cards.
- Artifact viewer.
- Controlled PDF and OCR.
- Attachment trust boundary.
- Document extraction evaluation.

Prohibited:
- Execute attachment content.
- Treat PDF as source-of-truth without validation.

## F47 — Voice State Machine, Multimodal Boundary & Confirmation UX

Scope:
- Voice state machine.
- Transcript safety.
- Command preview.
- Readback and confirmation.
- Barge-in and interruption handling.
- TTS fallback.

Notes:
- Local STT and TTS remain deferred until a future benchmark and gate justify them.

Prohibited:
- Implicit permission by voice.
- Transcript-triggered execution without confirmation.

## F48 — Local Packaging, Recovery Profiles & Deployment Readiness

Scope:
- Local packaging.
- Healthcheck.
- Low-RAM profile.
- Dependency diagnostics.
- Restart and recovery.
- Backup and restore.

Prohibited:
- Mandatory cloud path.
- Packaging that hides failures.

## F49 — Full System Sweep, Chaos Drills & External Technical Audit

Scope:
- Full system sweep.
- Chaos and failure drills.
- Security red-team.
- External audit package.
- Final risk register.
- Repair backlog.

Prohibited:
- Closure with critical blocker.
- Narrative-only audit.

## F50 — Continuous Governance, Productization & Next Roadmap Cycle

Scope:
- Continuous governance policy.
- Maintenance cadence.
- Productization backlog.
- Enterprise readiness backlog.
- Next roadmap proposal.
- Canonical closure gate.

Prohibited:
- Parallel roadmap creation.
- Treat backlog as authorization.
