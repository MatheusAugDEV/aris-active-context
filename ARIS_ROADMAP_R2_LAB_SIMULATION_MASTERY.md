# ARIS-ROADMAP-R2 — Lab Simulation Mastery & Macroblock Rebalancing

Status: `roadmap_r2_lab_simulation_mastery_planned`

Scope: Lab-only roadmap rebalancing. Productization: false. Customer pilot: false. Runtime mutation: false. Network use: false. External-channel send: false. MCP activation: false. Backup execution: false. Update execution: false.

## Purpose

R2 reorganizes ARIS from a long linear roadmap into capability macroblocks with explicit maturity levels and operational simulation gates. The goal is not to make ARIS a product now. The goal is to build ARIS like a future high-level product while validating every critical capability in lab first.

The guiding metaphor is bridge load testing:

- paper design is insufficient;
- isolated component tests prove only local behavior;
- integrated lab tests prove system composition;
- operational stress tests prove failure resistance;
- productization remains blocked until future F121+.

## Authority

R2 does not replace `ARIS_ROADMAP_R0_F120.md`. It is a roadmap architecture overlay for organizing existing and future phases into macroblocks. Existing `DECISION_LOCKS.md`, active-context, and `ARIS_ROADMAP_R0_F120.md` remain authoritative.

R2 extends R1 by turning critical reality gaps into a structured lab maturity system rather than a product plan.

## Market patterns absorbed, not copied

R2 adopts market patterns as lab references only:

- Claude Code pattern to study: lifecycle events, hooks, permission request events, compaction events, file/config/worktree events.
- Codex pattern to study: sandbox modes, approval policies, workspace boundaries, network default-deny stance.
- LangGraph pattern to study: checkpointing, time travel, thread-scoped persistence, fork/replay semantics.
- OpenHands pattern to study: conversation/workspace separation, sandboxed execution, lifecycle control, visual/API interfaces, event streams.
- SMB tools pattern to study: simple owner UX, scheduling UX, onboarding, reminders, support, pricing clarity.

ARIS rule: copy useful patterns, not dependencies; adapt them under ARIS governance, gates, ledger, rollback, and lab-only validation.

## Macroblocks

### MB1 — Governance / Bedrock

Capability: ARIS knows what is true, what is blocked, what is warning-only, and what is not authorized.

Core responsibilities:

- source-of-truth precedence
- active-context discipline
- decision locks
- warning vs blocker classification
- phase ledger continuity
- non-authorization preservation
- regression reopen policy

Current estimated maturity: `M3-LAB`.

Target before F120 closure: `M6-LAB`.

### MB2 — Context OS / Memory / Knowledge

Capability: ARIS loads the right context with bounded cost, preserves full-body read on demand, and avoids false token-saving claims.

Core responsibilities:

- BOOT/read-first flow
- active-context routing
- artifact reference-only planning
- context budget policy
- source freshness handling
- memory provenance and legal basis planning
- query-first knowledge access

Current estimated maturity: `M2.5-LAB` after P16.

Target before F120 closure: `M6-LAB`.

### MB3 — Action Runtime

Capability: ARIS transforms intent into safe, typed, authorized, auditable, reversible actions in lab.

Core responsibilities:

- Action Registry
- `risk_level`
- `rollback_action`
- TaskPlan schema
- success criteria
- dry-run executor
- permission gate
- execution authorization
- ledger events
- rollback-by-fork
- saga/compensation
- sidecar boundary
- kill-switch

Current estimated maturity: `M1.5-LAB`.

Target before F120 closure: `M6-LAB`.

### MB4 — Operational Reality Lab

Capability: ARIS remains safe and useful when components fail.

Core responsibilities:

- AI-less fallback
- degraded mode
- human handoff simulation
- stuck detection
- backup/restore simulation
- safe update/rollback simulation
- failure injection
- offline/channel failure behavior

Current estimated maturity: `M0.5-LAB`.

Target before F120 closure: `M6-LAB`.

### MB5 — Channel / Product Simulation Lab

Capability: ARIS simulates product-grade user flows without becoming a product or contacting real customers.

Core responsibilities:

- WhatsApp-like local channel simulation
- template/opt-in simulation
- final-customer UX simulation
- owner approval UX simulation
- onboarding simulation
- channel cost simulation
- no-jargon UX rules

Current estimated maturity: `M0.5-LAB`.

Target before F120 closure: `M5-LAB`.

### MB6 — Domain Simulation Lab

Capability: ARIS proves its generic architecture across realistic business domains without hardcoding.

Core responsibilities:

- domain object model
- scheduling simulation
- cancellation/rebooking simulation
- role/team simulation
- no-show simulation
- conflict prevention
- domain portability checks

Current estimated maturity: `M1.5-LAB`.

Target before F120 closure: `M6-LAB`.

### MB7 — Observability / Evaluation / Cost Lab

Capability: ARIS measures behavior, cost, quality, fallback, rollback, handoff, and failure rates in lab.

Core responsibilities:

- UsageEvent
- PermissionEvent
- RollbackEvent
- FallbackEvent
- HandoffEvent
- StuckEvent
- CostEvent
- FailureEvent
- golden trajectories
- CLEAR-style evaluation

Current estimated maturity: `M1.5-LAB`.

Target before F120 closure: `M6-LAB`.

### MB8 — Security / Isolation / Supply Chain Lab

Capability: ARIS validates security controls around sidecars, tools, descriptors, secrets, and dependencies in lab.

Core responsibilities:

- sidecar isolation profile
- egress deny-by-default
- MCP descriptor hash pinning
- signed manifest allowlist
- tool-output untrusted boundary
- secret redaction
- dependency/SBOM planning

Current estimated maturity: `M1-LAB`.

Target before F120 closure: `M6-LAB`.

### MB9 — Full ARIS Lab Gauntlet

Capability: ARIS combines all macroblocks into product-shadow simulations without real users or production deployment.

Core responsibilities:

- simulated pilot
- product-shadow environment
- multi-domain scenario packs
- operational load tests
- failure-combination tests
- lab closure report

Current estimated maturity: `M0-LAB`.

Target before F120 closure: `M6-LAB`.

## Maturity model

R2 uses lab-only maturity levels:

- `M0-LAB`: concept exists.
- `M1-LAB`: contract/schema/policy exists.
- `M2-LAB`: isolated deterministic harness exists.
- `M3-LAB`: integrated lab flow exists.
- `M4-LAB`: operational stress simulation exists.
- `M5-LAB`: full simulated pilot/product-shadow exists.
- `M6-LAB`: repeated lab gauntlet passes with rollback, observability, failure injection, and evidence bundle.
- `M7+`: intentionally reserved for future post-F120 productization tracks and not reachable in current lab-only roadmap.

## R2 non-authorization rules

- No customer pilot.
- No production deployment.
- No external-channel send.
- No real WhatsApp integration.
- No Z-API integration.
- No real payment execution.
- No real MCP activation.
- No backup execution outside simulation.
- No update execution outside simulation.
- No runtime mutation without future phase-specific authorization.
- No product claim based on lab-only evidence.

## R2 immediate outputs

R2 creates and maintains:

- `ARIS_ROADMAP_R2_LAB_SIMULATION_MASTERY.md`
- `ARIS_LAB_MACROBLOCK_MATURITY_FRAMEWORK.md`
- `ARIS_LAB_OPERATIONAL_LOAD_TEST_PLAN.md`

## Next recommended phase

`ARIS-ROADMAP-R2-REVIEW — Lab Simulation Mastery Review Gate`
