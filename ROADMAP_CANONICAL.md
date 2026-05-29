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
   - The Plan-Only Dry-Run Commit Rehearsal Review phase has passed.
   - The Controlled Apply Operator Approval Packet Review phase has passed as review-only and did not authorize execution.
   - The Controlled Apply Dry-Run Harness Planning phase has passed and the current active next phase from `ACTIVE_CONTEXT_STATE.json` is `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review`.
   - Cross-cutting gates:
   - state_data_plane_boundary_gate
   - strict_canonical_json_gate
   - state_drift_gate
   - operator_approval_contract_gate
   - filesystem_isolation_gate
   - shadow_workspace_gate
   - saga_pivot_compensation_gate
   - atomic_commit_cas_gate
   - ledger_temporal_checkpoint_gate
   - fast_path_non_generative_router_gate
   - kv_cache_static_prefix_benchmark_gate
   - edge_golden_scenario_gate
   - debian_disposable_harness_gate
   - supply_chain_and_dependency_lock_gate
   - memory_governor_and_pq_firewall_gate
   - evidence_graph_and_compliance_compiler_gate

   - Phase sequence:
     1. Lab Real Simulation Pack Filesystem Isolation Readiness Review
     2. Lab Real Simulation Pack Shadow Workspace Dry-Run Blueprint Review
     3. Lab Real Simulation Pack Debian Disposable Harness Planning
     4. Lab Real Simulation Pack Debian Disposable Harness Readiness Review
     5. Lab Real Simulation Pack Plan-Only Dry-Run Commit Rehearsal Review
     6. Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review
     7. Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning
     8. Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review
3. ARIS Infernus Lab FULL
4. ARIS Final Crisol FULL
5. Productatization Gate
6. Primeiro Piloto Controlado
7. SIP - Sistema Imunologico Permanente

## Current Canonical Position
Roadmap current-position (derived from `ACTIVE_CONTEXT_STATE.json`):
- Strategic Reset: `PASS`
- Product Loop Demonstravel: `PASS`
- The Controlled Apply Dry-Run Harness Planning phase has passed and the active next phase is `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review`.
- `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review` is the next readiness gate and does not authorize real apply, real dry-run execution, or runtime mutation.
- Controlled Apply Dry-Run Harness Planning passed as planning-only and did not execute a real dry-run, real apply, or approval execution.
- Bedrock gate remains non-executable and product promotion remains blocked.
- Roadmap current-position stale warning status: `resolved`.
- H4/H5/Hx not active current route.

## Active vs Historical vs Amendments
Active direction:
- `ACTIVE_CONTEXT_STATE.json` is the only canonical live-state file.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical live-state validation contract.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, and `CONTEXT_INDEX.md` are derived Markdown mirrors, not independent live-state authorities.
- `ARIS_PHASE_LEDGER.md` is historical ledger only.
- This file is roadmap sequence only, not the canonical live state.

## Non-Authorization
This roadmap does not authorize:
- runtime mutation by itself
- frontend mutation by itself
- voice or audio mutation by itself
- action runtime mutation by itself
- backend mutation by itself
- network use by itself
- dependency installation by itself
- pilot, customer, or commercial use by itself
