# Roadmap Canonico ARIS V1.2

## Purpose
This file is the active roadmap authority for ARIS after active-context canonicalization. It defines the canonical macrostructure, the non-negotiable locks, the invariants, the pre-pilot gaps, and the distinction between active direction, preserved history, and future amendments. Live routing is read from ACTIVE_CONTEXT_STATE.json; this file is roadmap sequence only, not the canonical live state.

## Official Phrase
ARIS nao promete automacao. ARIS prova automacao.

## Canonical Macrostructure
0. Strategic Reset
1. Product Loop Demonstravel
2. Hardening Base H0-H7
2.5. Lab Real Simulation Pack
2.6. Tier-1 Runtime Safety Remediation Track
   - Scope: formalize Tier-1 runtime safety blockers before any operator review escalation, real dry-run, or real apply.
   - This track is plan-only and does not authorize runtime execution, operator approval, or productization.
   - The Controlled Apply Dry-Run Harness Planning phase has passed.
   - The Controlled Apply Dry-Run Harness Readiness Review phase completed with decision `blocked` and remains historical evidence.
   - The Controlled Apply Dry-Run Harness Planning Correction Gate has passed as planning-only.
   - The Controlled Apply Dry-Run Harness Correction Readiness Review has passed as review-only.
   - The Controlled Apply Dry-Run Execution Authorization Planning phase has passed as planning-only.
   - The Controlled Apply Dry-Run Execution Authorization Planning Readiness Review has passed as review-only.
   - The Controlled Apply Dry-Run Operator Authorization Packet Planning phase has passed as planning-only.
   - The Controlled Apply Dry-Run Operator Authorization Packet Readiness Review has passed as review-only.
   - The Controlled Apply Dry-Run Operator Authorization Packet Final Review Gate has passed as review-only.
   - Roadmap amendment required: `True`
   - Explicit amendment: before any future route can reach real approval-facing or execution-facing behavior, the active route now requires `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Request Simulation Planning`.
3. ARIS Infernus Lab FULL
4. ARIS Final Crisol FULL
5. Productatization Gate
6. Primeiro Piloto Controlado
7. SIP - Sistema Imunologico Permanente

## Current Canonical Position
Roadmap current-position (derived from `ACTIVE_CONTEXT_STATE.json`):
- Operator authorization packet final review re-verified the future packet remains default-not-requested, placeholder-only, and non-authorizing, and advanced only to approval-request simulation planning.
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Request Simulation Planning`
- Bedrock gate remains non-executable and product promotion remains blocked.
- H4/H5/Hx not active current route.

## Active vs Historical vs Amendments
Active direction:
- `ACTIVE_CONTEXT_STATE.json` is the only canonical live-state file.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical live-state validation contract.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, and `CONTEXT_INDEX.md` are derived Markdown mirrors, not independent live-state authorities.
- `ARIS_PHASE_LEDGER.md` is historical ledger only.
- This file is roadmap sequence only, not the canonical live state.
- Any future phase insertion here must be treated as an explicit amendment, never as a silent route rewrite.
