# ARIS_ARCHITECTURE_OVERVIEW

## Core principle

- LLM helps, gates decide.
- Sidecar-first.
- Read-only before mutation.
- Dry-run before apply.
- Artifact before claim.
- Rollback before real action.
- Source-of-truth before memory.
- Context compactness before context mass.
- Safety before convenience.
- Observability before expansion.
- Context OS should become a derived navigation layer, not a source-of-truth replacement.

## System map

ARIS
├── Response Reliability
├── Understanding / Intent / Context
├── Evaluation / Golden Gates
├── Voice / Audio Safety
├── Action Runtime Contracts
├── Local Actions
├── Observability / Reliability Lab
├── Context OS / Obsidian / active-context
├── Cockpit / Evidence Browser
└── Packaging / Recovery / Diagnostics

## Main layers

### 1. Response Reliability
- Purpose: answer safely and consistently.
- Examples: fallback answers, provenance, quality gates.
- Safety posture: read-only.
- Status: active and matured by F20-F26.
- Risks: false confidence, hallucination, missing provenance.

### 2. Understanding / Intent
- Purpose: classify user intent and route safely.
- Examples: semantic gate, ambiguity resolution.
- Safety posture: deterministic sidecar logic.
- Status: foundation established by F14/F21.
- Risks: misclassification, over-permissive routing.

### 3. Evaluation / Golden Gates
- Purpose: prove behavior before promotion.
- Examples: proof gates, coverage matrices, golden suites.
- Safety posture: proof-before-claim.
- Status: active.
- Risks: fake coverage, untested paths.

### 4. Voice Safety
- Purpose: prevent unsafe voice execution.
- Examples: readback, confirmation, silence default-no.
- Safety posture: strongly gated.
- Status: active.
- Risks: accidental execution, destructive voice-only commands.

### 5. Action Runtime Contracts
- Purpose: safe local automation with ledger/rollback.
- Examples: permission gate, dry-run, undo, action ledger.
- Safety posture: zero-trust contracts.
- Status: active and bounded.
- Risks: side effects, rollback failure, permission drift.

### 6. Local Actions
- Purpose: controlled local automation.
- Examples: notes/calendar/file dry-run/apply planning.
- Safety posture: bounded and evidence-led.
- Status: deferred until gates allow.
- Risks: unsafe mutation, hidden impact.

### 7. Observability / Reliability
- Purpose: trace, measure, and classify failure honestly.
- Examples: benchmarks, trace graph, reliability score, latency.
- Safety posture: read-only analytics.
- Status: active.
- Risks: overclaiming coverage, missing traces.

### 8. Context OS / Obsidian / active-context
- Purpose: compact context, navigation, and decision memory.
- Examples: current state, decision locks, active-context repo.
- Safety posture: read-only, query-first, no bulk read.
- Status: critical and still under repair.
- Risks: stale context, drift, incorrect closure claims.
- The approved direction is an ARIS-owned read-only wrapper with allowlisted paths, ledgered reads, and no broad-vault access.

### 9. Cockpit / Evidence Browser
- Purpose: index and inspect evidence.
- Examples: snapshots, alias/errata linking, readiness review.
- Safety posture: sidecar read-only.
- Status: active as foundation.
- Risks: false certainty, wrong canonical mapping.

### 10. Packaging / Recovery
- Purpose: stable local deployment and recovery profiles.
- Examples: healthcheck, dependency diagnostics, archival maintenance.
- Safety posture: dry-run, no automatic install.
- Status: active.
- Risks: hidden dependency failures, unsafe recovery.

### 11. UI/orb/frontend
- Purpose: user-facing interaction and visualization.
- Examples: orb, response surfaces, warnings display.
- Safety posture: controlled and gated.
- Status: not a free mutation surface.
- Risks: unsafe rendering, behavioral mismatch.

### 12. Product/enterprise direction
- Purpose: define long-term commercial and operational direction.
- Examples: automation, compliance, auditability, hybrid local/cloud.
- Safety posture: strategic only.
- Status: aspirational, not proof of product readiness.
- Risks: premature product claims.

## Protected surfaces

- Runtime.
- Frontend.
- Action runtime.
- Audio.
- Network.
- Secrets.
- Dependencies.
- Productive execution.
- Obsidian write outside allowlist.
- Source-of-truth mutation without evidence.

## Source-of-truth hierarchy

1. Artifacts, summaries, decisions, and reports.
2. Official docs.
3. `PROJECT_CONTEXT_ARIS.md`.
4. `CURRENT_STATE.md` and `CONTEXT_INDEX.md`.
5. `aris-active-context`.
6. Obsidian as a derived navigation layer.
7. ChatGPT/Gemini/Claude memory as non-authoritative.
