# ARIS-ROADMAP-R1 — Critical Reality Gaps Delta Pack

Status: `roadmap_r1_critical_reality_gaps_delta_planned`

Scope: roadmap/governance-only delta for `ARIS_ROADMAP_R0_F120.md`.

Production authorization: false. Runtime mutation: false. Network use: false. External-channel send: false. MCP activation: false. Backup execution: false. Update execution: false. Customer pilot authorization: false.

## Authority

This file is an active-context roadmap delta. It does not replace `ARIS_ROADMAP_R0_F120.md`; it extends the canonical roadmap with planned critical reality-gap phases. Existing `DECISION_LOCKS.md` remains authoritative for hard restrictions.

Source diagnostic: uploaded senior roadmap diagnosis identified critical gaps in fallback without LLM, customer-facing UX, backup/restore, safe update, MCP hardening, ledger anchoring, sidecar isolation, external-channel economics, and human handoff.

## R1 Global Locks

- no Z-API integration for governed pilot.
- no marketing template send without explicit opt-in.
- no sensitive data flow without specific legal basis.
- no MCP server load without approved descriptor hash pinning.
- no production update without verified rollback path.
- no pilot without off-device backup/restore plan.
- no customer-facing automated dead-end without human handoff path.

These locks are governance-level only. They do not authorize implementation, runtime execution, external-channel sends, MCP activation, backup execution, update execution, or production pilot.

## Planned roadmap insertions

### F33.A — Memory Schema Foundation

Position: immediately after F33.

STATUS: PLANNED.

Scope: define memory schema with two axes:

- temperature: `hot | warm | cold`
- type: `working | episodic | semantic | procedural`

Required fields:

- `tenant_id`
- `subject_id`
- `source_event_id`
- `provenance_hash`
- `consent_basis`
- `t_valid_start`
- `t_valid_end`
- `t_recorded`
- `t_invalidated`

Exit gate: schema published as planned artifact; no real write authorized; LGPD Art. 18/20 compatibility preserved.

### F33.B — Memory Write Pipeline Contract

Position: after F33.A.

STATUS: PLANNED.

Scope: define deterministic memory pipeline:

`extract → classify → consolidate → gate → ledger`

No memory may be written directly by an LLM without deterministic gate.

Exit gate: write-pipeline contract created; valid/invalid examples defined; self-editing memory blocked.

### F33.C — Context Progressive Disclosure & Deterministic Selection

Position: after F33.B.

STATUS: PLANNED.

Scope: define deterministic context selection for artifacts and tenant data while avoiding bulk-read. Include repo-map/PageRank/tree-sitter-style selection for code and structured index selection for domain data.

Exit gate: context selection contract created; bulk-read remains blocked; token-saving claim prohibited without measurement.

### F36.D — MCP Descriptor Hash-Pinning & Tool Poisoning Defense

Position: after F36.C.

STATUS: PLANNED.

Scope:

- descriptor hash pinning
- signed manifest allowlist
- scan of descriptors before promotion
- tool output treated as untrusted
- descriptor drift/rug-pull blocked without new approval

Exit gate: MCP server load without approved hash pinning remains prohibited; descriptor poisoning fixtures planned.

### F40.B — Ledger External Anchoring & Signing Plan

Position: after F40.

STATUS: PLANNED.

Scope: extend ledger contract with planned periodic external anchoring, signing by a key outside the main process when available, append-only preservation, and tamper-detection evidence.

Exit gate: rollback/truncate remains prohibited; ledger tamper-evidence strengthened; no real external integration authorized.

### F43.C — Enumerated Sidecar Isolation Profile

Position: after F43.B.

STATUS: PLANNED.

Scope: define mandatory sidecar isolation profile:

- rootless UID
- read-only filesystem root
- path allowlist
- egress deny-by-default
- dropped capabilities
- seccomp/AppArmor or platform equivalent
- secret redaction boundary

Exit gate: sidecar profile contract created; sidecar without enumerated profile blocked.

### F60.B — AI-Less Deterministic Fallback

Position: after F60.

STATUS: PLANNED.

Scope: create deterministic non-LLM fallback for canonical flows:

- schedule
- cancel
- view available slots
- simple FAQ
- human handoff

Exit gate: fallback flows described as FSM/rules; LLM failure cannot block a basic simulated flow.

### F78.B — Safe Update & Rollback A/B Plan

Position: after F78.

STATUS: PLANNED.

Scope:

- controlled rollout
- rollback A/B
- regression tests before promotion
- policy regression check
- previous version recoverability

Exit gate: no productive update permitted without tested rollback path.

### F80.C — Encrypted Off-Device Backup & Restore Plan

Position: after F80, or after F80.B if later materialized.

STATUS: PLANNED.

Scope:

- encrypted off-device backup
- encryption at rest
- restore drill
- planned RPO/RTO
- recovery without LLM dependency

Exit gate: real backup/restore remains unauthorized; restore plan must exist before real pilot.

### F90.B — External Channel Economics & Template Strategy

Position: after F90.

STATUS: PLANNED.

Scope:

- Cloud API direct as preferred baseline
- BSP backup only with ADR
- reject Z-API for governed pilot
- utility templates for scheduling/confirmation
- marketing templates only with explicit opt-in
- 24h free window considered in flow design

Exit gate: economic model documented; no real send authorized.

### F95.E — Customer-Facing Conversational UX

Position: after F95D and before F95E existing, or immediately before F95.F if insertion before F95E is not possible without renumbering.

STATUS: PLANNED.

Scope: WhatsApp-facing UX for the final customer/data subject:

- simple pt-BR language
- numeric confirmation when needed
- opt-out with `SAIR`/`PARAR`
- human handoff on repeated failures
- zero jargon about AI, agent, gate, or ledger

Exit gate: non-technical final-customer simulation; zero technical jargon; handoff validated.

### F95.H — Assisted SMB Onboarding

Position: after F95.G.

STATUS: PLANNED.

Scope: assisted onboarding for SMB with a wizard of at most 8 essential questions:

- service catalog
- schedules
- professionals
- confirmation/cancellation rules
- initial templates
- consent
- legal basis

Exit gate: complete simulated onboarding without requiring technical knowledge from the owner.

### F95.I — Degraded Mode & Human Handoff Gate

Position: after F95.H.

STATUS: PLANNED.

Scope: define graceful degradation for:

- LLM failure
- channel failure
- calendar failure
- low confidence
- 3 failed understanding attempts
- explicit request for attendant

Exit gate: human handoff within 30s simulated; event recorded in ledger; infinite “não entendi” loop prohibited.

## Required F95.G dependency update

`F95.G — Controlled Pilot Gate` must depend on:

- F60.B — AI-Less Deterministic Fallback
- F78.B — Safe Update & Rollback A/B Plan
- F80.C — Encrypted Off-Device Backup & Restore Plan
- F90.B — External Channel Economics & Template Strategy
- F95.E — Customer-Facing Conversational UX
- F95.I — Degraded Mode & Human Handoff Gate

No real pilot is authorized by this dependency list.

## Required F120 Final Threshold additions

The following thresholds must be added to F120 closure criteria when the main roadmap is next compact-patched:

- `ai_less_fallback_coverage=1.00`
- `customer_handoff_dead_end_count=0`
- `off_device_backup_restore_plan_exists=true`
- `safe_update_rollback_plan_exists=true`
- `mcp_descriptor_hash_pinning_policy_exists=true`
- `sidecar_isolation_profile_exists=true`
- `ledger_external_anchoring_plan_exists=true`
- `external_channel_economics_documented=true`

## Non-authorization statement

R1 is a planning delta only. It does not authorize product promotion, customer deployment, production pilot, WhatsApp send, BSP activation, MCP activation, backup execution, update execution, runtime mutation, SQLite schema apply, network use, dependency installation, or vault write.

## Next recommended phase

`ARIS-ROADMAP-R1-REVIEW — Critical Reality Gaps Delta Review Gate`
