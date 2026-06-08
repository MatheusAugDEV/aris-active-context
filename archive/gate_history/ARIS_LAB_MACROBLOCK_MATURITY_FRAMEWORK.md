# ARIS Lab Macroblock Maturity Framework

Status: `macroblock_maturity_framework_planned`

Scope: lab-only maturity model for ARIS macroblocks. Productization: false.

## Purpose

This framework prevents false maturity claims. A phase may pass while the overall capability remains immature. Each ARIS macroblock must be evaluated by capability maturity, not only by phase count.

## Maturity levels

### M0-LAB — Concept

The capability exists as an idea, thesis, roadmap item, or advisory research note.

Evidence allowed:

- roadmap entry
- ADR draft
- research note
- planning statement

Not allowed claims:

- implemented
- integrated
- safe under failure
- product-ready

### M1-LAB — Contract

The capability has a schema, policy, contract, or deterministic plan.

Evidence allowed:

- schema artifact
- policy artifact
- decision artifact
- contract doc
- valid/invalid examples

Not allowed claims:

- runtime working
- integrated behavior
- operational resilience

### M2-LAB — Isolated Harness

The capability has isolated deterministic tests or a runner.

Evidence allowed:

- unit tests
- runner output
- validation artifacts
- blocked invalid fixtures

Not allowed claims:

- end-to-end readiness
- operational readiness
- product-readiness

### M3-LAB — Integrated Lab Flow

The capability works with adjacent macroblocks in a bounded lab flow.

Evidence allowed:

- E2E lab runner
- integrated fixture
- ledgered simulated flow
- rollback/fallback evidence where applicable

Not allowed claims:

- high-load readiness
- real-user readiness
- production readiness

### M4-LAB — Operational Stress Simulation

The capability survives stress, fault injection, repeated interactions, and adverse inputs in simulation.

Evidence allowed:

- load simulation
- failure injection matrix
- chaos scenario report
- repeated-run determinism
- no unsafe side effect evidence

Not allowed claims:

- external customer readiness
- production readiness

### M5-LAB — Product-Shadow Simulation

The capability participates in a full simulated product environment with fake owner, fake customer, fake channel, fake data, fake costs, fake support, and real ledgered evidence.

Evidence allowed:

- simulated pilot report
- product-shadow transcript bundle
- complete simulated onboarding
- fake channel/cost/backup/update reports

Not allowed claims:

- product launched
- customer validated
- real market fit

### M6-LAB — Repeated Lab Gauntlet Pass

The capability repeatedly passes cross-macroblock gauntlets with failures, rollback, observability, evidence bundle, and no critical blockers.

Evidence allowed:

- repeated gauntlet pass report
- cross-macroblock trace bundle
- blocker_count=0
- safety invariants preserved
- reproducible rerun artifacts

Not allowed claims:

- production authorized
- customer deployment authorized
- commercial readiness authorized

### M7+ — Reserved for post-F120

M7 and above are explicitly outside the current lab-only roadmap. They require future F121+ Controlled Productization Gate or later.

## Current estimated macroblock maturity

| Macroblock | Current estimate | Target before F120 lab closure |
|---|---:|---:|
| MB1 Governance / Bedrock | M3-LAB | M6-LAB |
| MB2 Context OS / Memory / Knowledge | M2.5-LAB | M6-LAB |
| MB3 Action Runtime | M1.5-LAB | M6-LAB |
| MB4 Operational Reality Lab | M0.5-LAB | M6-LAB |
| MB5 Channel / Product Simulation Lab | M0.5-LAB | M5-LAB |
| MB6 Domain Simulation Lab | M1.5-LAB | M6-LAB |
| MB7 Observability / Evaluation / Cost Lab | M1.5-LAB | M6-LAB |
| MB8 Security / Isolation / Supply Chain Lab | M1-LAB | M6-LAB |
| MB9 Full ARIS Lab Gauntlet | M0-LAB | M6-LAB |

## Capability readiness rule

A macroblock cannot be treated as ready just because its individual phases passed. It must meet the evidence required by its maturity level.

## Pilot/product rule

No real pilot or product action is authorized by this framework. Even M6-LAB remains lab-only.

## Recommended review gates

- R2-REVIEW: validate macroblock definitions.
- R2-MATURITY-BASELINE: validate current maturity ratings.
- R2-LOAD-PLAN: validate operational load test plan.
- R2-GAUNTLET-PLAN: validate full ARIS lab gauntlet design.
