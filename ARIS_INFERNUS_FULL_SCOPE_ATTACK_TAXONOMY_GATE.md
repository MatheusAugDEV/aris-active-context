# ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate

## Phase Name

`ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate`

## Status

`aris_infernus_lab_full_scope_attack_taxonomy_planning_gate_pass`

## Decision

`pass`

## Source Phase Reviewed

`ARIS Infernus Lab FULL Macroblock Entry Gate`

## Advisory Source Used

`infernus_protocol.md`

Classification: non-canonical advisory input only. It informs planning design and does not replace `ACTIVE_CONTEXT_STATE.json`, `ROADMAP_CANONICAL.md`, implementation evidence, or PASS evidence.

## Macrochain Position

Macroblock `1` planning gate inside the canonical chain:

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
Crisol refina.
Bedrock decide.
```

This gate does not execute Infernus. It locks the planning contract for what future Infernus phases will attack, how findings will be classified, which discovery roles own each domain, what evidence is required, and how findings flow into `Purgatorium FULL`.

## Scope Statement

This phase canonizes planning-level scope only for `ARIS Infernus Lab FULL`:

- attack taxonomy at macro level
- finding taxonomy at macro level
- official 13-bot discovery role mapping
- historical function preservation without resurrecting superseded bots
- P0 planning gap resolutions needed before bot contracts
- severity model `S0-S5`
- required future evidence shape
- `Purgatorium FULL` handoff structure
- machine-readable Bedrock impact signal names
- explicit non-execution and non-productization boundaries

## Explicit Non-Scope

This phase does not authorize and does not include:

- bot implementation
- bot execution
- attack execution
- scenario execution
- harness creation
- harness execution
- real dry-run
- real apply
- sandbox apply
- runtime mutation
- frontend mutation
- backend mutation
- action-runtime mutation
- audio mutation
- product code mutation
- package installation
- dependency changes
- secrets access
- external API use
- external LLM use
- Bedrock execution
- Bedrock PASS
- product promotion
- pilot
- production
- commercial launch
- customer readiness

Future Infernus phases may attack only under later explicit gates.

## Attack Taxonomy

### 1. Prompt and Policy Manipulation

- Description: direct and indirect prompt injection, role confusion, unsafe instruction override, malicious content steering, and policy bypass pressure.
- Primary bot owners: `Taipan`, `Quimera`
- Secondary bot owners: `Apep`, `Dúbio`
- Expected finding categories: `prompt_injection`, `indirect_prompt_injection`, `tool_misuse`, `false_pass`, `false_consent`
- Evidence requirements: scenario manifest, payload trace, policy-decision evidence, tool invocation trace, before/after context references, severity rationale
- Purgatorium handoff implications: tighten policy boundaries, input sanitation, approval semantics, and denial-path correctness
- Bedrock impact if severe: `BB-UNRESOLVED-S4`, `BB-UNRESOLVED-S5`, `BB-FALSE-PASS`, `BB-NO-HITL-PROOF`

### 2. Tool and Integration Abuse

- Description: misuse of tools, connectors, registries, handoffs, and integration boundaries beyond declared contracts.
- Primary bot owners: `Elos`, `Taipan`
- Secondary bot owners: `Patrono`, `Apep`
- Expected finding categories: `tool_misuse`, `permission_bypass`, `privilege_escalation`, `trace_coverage_gap`
- Evidence requirements: dependency graph, registry snapshot, tool allowlist trace, handoff trace, event-order log, contract conformance evidence
- Purgatorium handoff implications: fix registry/allowlist drift, execution-order contract gaps, and integration guardrails
- Bedrock impact if severe: `BB-COVERAGE-GAP`, `BB-FALSE-PASS`, `BB-MISSING-PROVENANCE`

### 3. Privilege and Secret Compromise

- Description: overbroad permissions, confused deputy behavior, secret exposure, unauthorized capability reuse, and scope boundary failure.
- Primary bot owners: `Apep`, `Taipan`
- Secondary bot owners: `Patrono`, `Éfeso`
- Expected finding categories: `secret_exposure`, `permission_bypass`, `privilege_escalation`, `lab_product_boundary_leak`
- Evidence requirements: capability audit, permission scope report, secret-canary result, session-boundary evidence, invariant break report
- Purgatorium handoff implications: permission redesign, scoping correction, kill-switch hardening, and provenance hardening
- Bedrock impact if severe: `BB-UNRESOLVED-S4`, `BB-UNRESOLVED-S5`, `BB-MISSING-PROVENANCE`

### 4. Runtime/Autonomy Failure

- Description: loops, deadlocks, partial completion treated as success, crashes, unsafe retry behavior, and broken recovery.
- Primary bot owners: `Labirinto`, `Vitium`
- Secondary bot owners: `Gula`, `Loop`
- Expected finding categories: `rollback_failure`, `compensation_failure`, `replay_nondeterminism`, `false_pass`, `resource_exhaustion`
- Evidence requirements: trajectory log, state transition graph, recovery evidence, compensation result, concurrency trace, determinism evidence
- Purgatorium handoff implications: recovery contract repair, rollback/compensation hardening, bounded autonomy constraints
- Bedrock impact if severe: `BB-UNRESOLVED-S4`, `BB-NO-REPLAY-EVIDENCE`, `BB-FALSE-PASS`

### 5. Evidence/Source-of-Truth Failure

- Description: markdown beating JSON, advisory treated as canonical, missing provenance, stale source hierarchy, and evidence bundles without hash discipline.
- Primary bot owners: `Éfeso`, `Minos`
- Secondary bot owners: `Abzu`, `Elos`
- Expected finding categories: `source_of_truth_drift`, `evidence_gap`, `ledger_gap`, `accepted_risk_as_resolved`, `bedrock_boundary_inflation`
- Evidence requirements: source-authority report, hash manifest, schema compliance evidence, evidence-verdict packet, provenance chain
- Purgatorium handoff implications: source hierarchy repair, artifact hashing fixes, evidence closure rules
- Bedrock impact if severe: `BB-MISSING-PROVENANCE`, `BB-SCHEMA-DRIFT`, `BB-LLM-ONLY-JUDGE`, `BB-FALSE-PASS`

### 6. Replay/Regression Failure

- Description: flaky pass, nondeterministic replay, mutation blindness, eval rot, and missing idempotency proof.
- Primary bot owners: `Loop`, `Minos`
- Secondary bot owners: `Labirinto`, `Abzu`
- Expected finding categories: `replay_nondeterminism`, `false_pass`, `trace_coverage_gap`, `accepted_risk_as_resolved`
- Evidence requirements: replay result, mutation report, determinism check, idempotency proof, model/cache versioning, evidence audit
- Purgatorium handoff implications: replay contract fixes, stable oracles, deterministic evidence normalization
- Bedrock impact if severe: `BB-NO-REPLAY-EVIDENCE`, `BB-FALSE-PASS`, `BB-COVERAGE-GAP`

### 7. UX/HITL Failure

- Description: ambiguity, approval fatigue, unsafe confirmations, poor risk comprehension, overblocking, and underblocking.
- Primary bot owners: `Dúbio`, `Patrono`
- Secondary bot owners: `Quimera`, `Minos`
- Expected finding categories: `approval_fatigue`, `false_consent`, `overblocking`, `underblocking`, `false_readiness`
- Evidence requirements: consent trace, approval packet reference, protection-balance report, guardrail log, approval UX metrics
- Purgatorium handoff implications: approval packet redesign, HITL risk disclosure improvement, guardrail threshold repair
- Bedrock impact if severe: `BB-NO-HITL-PROOF`, `BB-FALSE-PASS`, `BB-PRODUCT-CLAIM-INFLATION`

### 8. Product/Bedrock Boundary Failure

- Description: lab signals being sold as product maturity, Bedrock inflation, commercial-readiness theater, and product claims without chain completion.
- Primary bot owners: `Éfeso`, `Minos`
- Secondary bot owners: `Patrono`, `Quimera`
- Expected finding categories: `lab_product_boundary_leak`, `bedrock_boundary_inflation`, `false_readiness`, `accepted_risk_as_resolved`
- Evidence requirements: lab-product boundary check, evidence-verdict packet, claim-to-evidence map, provenance and approval references
- Purgatorium handoff implications: claim discipline correction, boundary messaging repair, signal-gating hardening
- Bedrock impact if severe: `BB-PRODUCT-CLAIM-INFLATION`, `BB-FALSE-PASS`, `BB-MISSING-PROVENANCE`

### 9. Cost/Resource Exhaustion

- Description: token explosion, retry storms, latency spikes, quota burn, cache misuse, and runaway observability cost.
- Primary bot owners: `Gula`
- Secondary bot owners: `Labirinto`, `Loop`
- Expected finding categories: `resource_exhaustion`, `false_readiness`, `trace_coverage_gap`
- Evidence requirements: token breakdown, cost report, quota trace, cache efficiency report, burn-rate report, resource budget reference
- Purgatorium handoff implications: budget guardrails, retry policy repair, quota-aware execution constraints
- Bedrock impact if severe: `BB-UNRESOLVED-S4`, `BB-COVERAGE-GAP`

### 10. Memory/Context/Provenance Corruption

- Description: stale memory, context poisoning, compression loss, missing TTL, provenance breaks, and source mismatch.
- Primary bot owners: `Abzu`
- Secondary bot owners: `Loop`, `Éfeso`, `Quimera`
- Expected finding categories: `stale_memory`, `context_poisoning`, `source_of_truth_drift`, `evidence_gap`, `false_pass`
- Evidence requirements: memory audit, provenance chain, TTL compliance report, decision-lock diff, replay evidence for memory-sensitive scenarios
- Purgatorium handoff implications: memory lifecycle repair, TTL policy correction, provenance hardening, summarization constraints
- Bedrock impact if severe: `BB-MISSING-PROVENANCE`, `BB-FALSE-PASS`, `BB-SCHEMA-DRIFT`

### 11. Rollback/Compensation Failure

- Description: rollback gaps, compensation failure, partial side effects without ledger visibility, and non-equivalent recovery.
- Primary bot owners: `Vitium`
- Secondary bot owners: `Loop`, `Elos`, `Apep`
- Expected finding categories: `rollback_failure`, `compensation_failure`, `ledger_gap`, `replay_nondeterminism`
- Evidence requirements: system state before/after, rollback or compensation result, ledger integrity report, retest evidence
- Purgatorium handoff implications: compensation contract repair, rollback path redesign, ledger and recovery proof hardening
- Bedrock impact if severe: `BB-UNRESOLVED-S4`, `BB-NO-REPLAY-EVIDENCE`, `BB-FALSE-PASS`

### 12. Observability/Trace Coverage Failure

- Description: missing critical-path traces, unverifiable decisions, incomplete audit paths, and evidence bundles without trace coverage.
- Primary bot owners: `Elos`, `Minos`
- Secondary bot owners: `Gula`, `Éfeso`
- Expected finding categories: `trace_coverage_gap`, `evidence_gap`, `ledger_gap`, `false_pass`
- Evidence requirements: trace coverage report, event-order log, ledger references, evidence completeness score, deterministic audit packet
- Purgatorium handoff implications: trace instrumentation correction, audit path closure, evidence completeness enforcement
- Bedrock impact if severe: `BB-COVERAGE-GAP`, `BB-MISSING-PROVENANCE`, `BB-FALSE-PASS`

## Finding Taxonomy

| Category | Definition | Severity Range | Primary Bot Owner | Required Evidence | Purgatorium Route | Bedrock Consequence |
| --- | --- | --- | --- | --- | --- | --- |
| `prompt_injection` | Direct malicious instruction attempts that override policy or safe flow. | `S2-S5` | `Taipan` | attack scenario, payload log, policy decision ref, tool trace | policy and prompt-boundary repair | `BB-UNRESOLVED-S4`, `BB-UNRESOLVED-S5` |
| `indirect_prompt_injection` | Malicious instructions carried through retrieved or external content. | `S2-S5` | `Taipan` | content source ref, provenance, policy trace, scenario manifest | retrieval and tool-gating repair | `BB-UNRESOLVED-S4`, `BB-MISSING-PROVENANCE` |
| `tool_misuse` | Tool usage outside declared contract, allowlist, or intent boundary. | `S2-S5` | `Elos` | tool invocation trace, registry snapshot, event-order log | contract and registry correction | `BB-FALSE-PASS`, `BB-COVERAGE-GAP` |
| `permission_bypass` | Execution path that bypasses required approval or scope validation. | `S3-S5` | `Apep` | capability audit, permission scope report, approval packet ref | permission and invariant repair | `BB-UNRESOLVED-S4`, `BB-UNRESOLVED-S5` |
| `secret_exposure` | Secret, canary, or sensitive token leakage through response or tooling. | `S4-S5` | `Taipan` | canary report, egress log, trace ref, provenance | secret handling and egress hardening | `BB-UNRESOLVED-S5` |
| `privilege_escalation` | Escalation beyond valid scope, session, or capability boundary. | `S4-S5` | `Apep` | escalation trace, session-boundary test, invariant break report | capability and session isolation repair | `BB-UNRESOLVED-S5` |
| `source_of_truth_drift` | Decision path where lower-authority artifacts override canonical state. | `S3-S5` | `Éfeso` | source authority report, version drift report, provenance | authority and sync repair | `BB-SCHEMA-DRIFT`, `BB-MISSING-PROVENANCE` |
| `stale_memory` | Expired or invalid memory influences current decision or action. | `S2-S4` | `Abzu` | memory audit, TTL report, decision-lock diff | TTL and memory lifecycle correction | `BB-FALSE-PASS`, `BB-MISSING-PROVENANCE` |
| `context_poisoning` | Malicious or invalid context corrupts current reasoning or routing. | `S2-S5` | `Abzu` | provenance chain, poisoning test, trace ref | context hygiene and provenance repair | `BB-FALSE-PASS`, `BB-SCHEMA-DRIFT` |
| `ledger_gap` | Side effects, recovery, or decisions are not traceable in the ledger. | `S2-S4` | `Elos` | ledger ref, event-order log, integrity report | ledger contract and append repair | `BB-COVERAGE-GAP` |
| `evidence_gap` | Finding or verdict lacks required evidence, hash, provenance, or trace. | `S2-S5` | `Minos` | evidence-verdict packet, hash verification report, completeness score | evidence contract hardening | `BB-MISSING-PROVENANCE`, `BB-FALSE-PASS` |
| `rollback_failure` | Rollback path fails to restore or compensate safely. | `S3-S5` | `Vitium` | before/after state, rollback result, recovery attempt | rollback contract repair | `BB-UNRESOLVED-S4`, `BB-NO-REPLAY-EVIDENCE` |
| `compensation_failure` | Compensation exists nominally but does not safely cover partial side effects. | `S3-S5` | `Vitium` | compensation result, ledger evidence, retest need | compensation model repair | `BB-UNRESOLVED-S4`, `BB-FALSE-PASS` |
| `replay_nondeterminism` | Same scenario cannot be replayed deterministically or normalized equivalently. | `S2-S4` | `Loop` | replay result, determinism check, normalized hash | replay and oracle stabilization | `BB-NO-REPLAY-EVIDENCE` |
| `false_pass` | System is reported as passing despite invalid evidence or unmet gate conditions. | `S3-S5` | `Minos` | deterministic audit packet, severity rollup, provenance | verdict and gate hardening | `BB-FALSE-PASS` |
| `false_readiness` | Planning, review, or partial maturity is represented as operational readiness. | `S2-S5` | `Minos` | claim-to-evidence map, approval refs, readiness criteria | boundary and messaging repair | `BB-PRODUCT-CLAIM-INFLATION`, `BB-FALSE-PASS` |
| `accepted_risk_as_resolved` | Residual risk is mislabeled as resolved instead of managed. | `S2-S5` | `Minos` | residual risk policy, owner, expiry, compensating controls | residual classification repair | `BB-ACCEPTED-RISK-AS-RESOLVED` |
| `approval_fatigue` | Repeated or noisy approvals degrade operator attention and judgment quality. | `S1-S3` | `Patrono` | approval UX metrics, consent trace, guardrail log | approval UX and guardrail repair | `BB-NO-HITL-PROOF` when severe |
| `false_consent` | Consent captured without adequate scope, reversibility, or risk comprehension. | `S2-S5` | `Dúbio` | approval packet ref, clarification expected, consent trace | HITL semantics repair | `BB-NO-HITL-PROOF` |
| `overblocking` | Safe actions are blocked beyond acceptable protection thresholds. | `S1-S3` | `Patrono` | false-positive matrix, guardrail log, UX evidence | guardrail threshold tuning | `BB-COVERAGE-GAP` if systemic |
| `underblocking` | Dangerous actions are allowed without sufficient protection. | `S3-S5` | `Patrono` | false-negative matrix, dangerous action evidence, trace | guardrail hardening | `BB-UNRESOLVED-S4`, `BB-UNRESOLVED-S5` |
| `resource_exhaustion` | Cost, token, quota, latency, or retry growth exceeds safe operating budget. | `S1-S4` | `Gula` | token breakdown, cost report, burn-rate report, quota trace | budget and retry policy repair | `BB-COVERAGE-GAP`, `BB-UNRESOLVED-S4` if critical |
| `trace_coverage_gap` | Critical path lacks enough trace coverage for deterministic audit. | `S2-S4` | `Elos` | trace coverage report, event-order log, completeness score | trace instrumentation and evidence closure | `BB-COVERAGE-GAP` |
| `lab_product_boundary_leak` | Lab-only signals or artifacts are treated as product or commercial proof. | `S3-S5` | `Éfeso` | lab-product boundary check, claim map, provenance | boundary messaging and approval repair | `BB-PRODUCT-CLAIM-INFLATION` |
| `bedrock_boundary_inflation` | Technical or planning evidence is misrepresented as Bedrock approval. | `S3-S5` | `Minos` | evidence audit packet, approval refs, claim map | Bedrock boundary hardening | `BB-PRODUCT-CLAIM-INFLATION`, `BB-FALSE-PASS` |

## Official 13-Bot Discovery Role Mapping

### 1. Quimera

- Validated discovery role: composite-failure hunter for at least two interacting subsystems
- Primary domains: multi-layer failure composition, prompt-plus-context failure, permission-plus-ledger failure, runtime-plus-UX divergence
- Secondary domains: ambiguous cross-domain residuals, compound readiness failure
- Non-scope: single-layer failures, vague un-decomposed findings
- Required future contract areas: composite scenario schema, subsystem decomposition rules, owner-bot map
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: produce one composite finding plus required sub-findings routed to responsible owners

### 2. Dúbio

- Validated discovery role: ambiguity, intent-resolution, and false-consent analyst
- Primary domains: approval ambiguity, weak authorization packets, unclear intent, false consent
- Secondary domains: UX misunderstanding, clarification failure
- Non-scope: generic guardrail calibration
- Required future contract areas: approval packet schema, clarification oracle, consent trace evidence
- Likely severity range: `S1-S5`
- Purgatorium handoff responsibility: route HITL and approval semantics defects to correction owners

### 3. Elos

- Validated discovery role: handoff and dependency-chain auditor
- Primary domains: planner-to-executor sequencing, tool contract conformance, registry consistency, critical-path traces
- Secondary domains: evidence routing, ledger consistency
- Non-scope: adversarial exploitation as primary attack method
- Required future contract areas: handoff trace schema, registry snapshot format, trace coverage field
- Likely severity range: `S1-S4`
- Purgatorium handoff responsibility: route contract, sequencing, and trace failures to integration correction work

### 4. Taipan

- Validated discovery role: direct adversarial red-team attacker
- Primary domains: direct and indirect injection, tool misuse, exfiltration, policy bypass, malicious content
- Secondary domains: social engineering and hostile payload shaping
- Non-scope: deep invariant ownership
- Required future contract areas: attack scenario schema, payload log format, secret-canary reporting
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: route exploitation findings to policy, tooling, and permission correction owners

### 5. Labirinto

- Validated discovery role: long-trajectory, concurrency, and goal-drift breaker
- Primary domains: loops, race conditions, deadlocks, partial completion, silent drift
- Secondary domains: multi-step replay sensitivity
- Non-scope: direct prompt exploitation
- Required future contract areas: trajectory log, concurrency trace, goal-drift oracle
- Likely severity range: `S2-S4`
- Purgatorium handoff responsibility: route workflow and autonomy failure findings to bounded-execution correction work

### 6. Vitium

- Validated discovery role: technical fault-injection and recovery verifier
- Primary domains: crashes, disk/resource faults, interrupted ledger operations, rollback and compensation failure
- Secondary domains: stale locks and recovery equivalence
- Non-scope: business-level approval semantics
- Required future contract areas: fault scenario schema, recovery result evidence, compensation proof format
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: route recovery and compensation defects to system-hardening fixes

### 7. Gula

- Validated discovery role: economic and resource exhaustion auditor
- Primary domains: token cost, burn-rate, quota, retry storm, latency, resource budget failure
- Secondary domains: cache misuse, observability overhead
- Non-scope: permission policy decisions
- Required future contract areas: resource budget artifact, burn-rate report, token/cost telemetry schema
- Likely severity range: `S1-S4`
- Purgatorium handoff responsibility: route budget and efficiency defects to resource-governance fixes

### 8. Apep

- Validated discovery role: invariant, capability, privilege, and isolation attacker
- Primary domains: stale authorization, expired permissions, cross-session leakage, privilege escalation, kill-switch failure, sandbox escape
- Secondary domains: scope confusion and boundary collapse
- Non-scope: pure product-claim inflation
- Required future contract areas: capability audit schema, permission-scope report, session-boundary tests
- Likely severity range: `S3-S5`
- Purgatorium handoff responsibility: route invariant and isolation defects to permission and boundary correction work

### 9. Patrono

- Validated discovery role: protection-balance auditor
- Primary domains: overblocking, underblocking, approval fatigue, unsafe confirmations, guardrail false positives/negatives
- Secondary domains: operator-friction analysis
- Non-scope: final evidence auditing
- Required future contract areas: guardrail matrix, protection-balance report, approval UX metrics
- Likely severity range: `S1-S5`
- Purgatorium handoff responsibility: route guardrail balance defects to approval and protection tuning work

### 10. Éfeso

- Validated discovery role: source-of-truth and lab-product boundary guardian
- Primary domains: canonical-source hierarchy, artifact provenance, advisory-vs-canonical separation, lab/product boundary ownership
- Secondary domains: historical route contamination and claim inflation detection
- Non-scope: direct red-team prompt attacks
- Required future contract areas: source authority report, lab-product boundary check, hash manifest
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: route provenance, authority, and boundary defects to governance correction work

### 11. Abzu

- Validated discovery role: memory, context, retrieval, and provenance lifecycle attacker
- Primary domains: stale memory, TTL loss, context poisoning, compression distortion, weak provenance
- Secondary domains: source mismatch and retrieval aging
- Non-scope: final replay judgment
- Required future contract areas: memory audit, TTL compliance report, provenance chain, decision-lock diff
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: route memory lifecycle and provenance defects to context correction work

### 12. Loop

- Validated discovery role: replay, mutation, idempotency, and regression generator
- Primary domains: replay evidence, mutation testing, deterministic reruns, idempotency proof, flaky pass detection
- Secondary domains: memory-sensitive replay and regression drift
- Non-scope: final verdicting
- Required future contract areas: replay result schema, mutation report, determinism check, normalized hash rules
- Likely severity range: `S1-S4`
- Purgatorium handoff responsibility: route reproducibility failures to replay and oracle correction work; provide retest evidence to later phases

### 13. Minos

- Validated discovery role: deterministic evidence auditor
- Primary domains: missing evidence, missing provenance, false PASS, severity downgrade, accepted-risk misclassification, Bedrock inflation
- Secondary domains: trace completeness and residual-risk classification
- Non-scope: execution, replay, fixing, or Bedrock decision
- Required future contract areas: evidence verdict packet, completeness scoring, deterministic ruleset hash, machine-readable boundary signals
- Likely severity range: `S2-S5`
- Purgatorium handoff responsibility: route evidence-quality and classification defects to correction owners while auditing closure packets

## Historical Function Preservation

Historical functions remain preserved as subdomains only. They do not restore superseded core bot names or routes.

| Historical Function | Preserved Current Ownership |
| --- | --- |
| Hermes: tool or connector routing | `Elos` |
| Mnemosyne: memory lifecycle | `Abzu` + `Loop` |
| Hephaestus: sandbox or build isolation | `Apep` + `Vitium` + `Elos` |
| Janus: lab-product boundary | `Éfeso` |
| Orpheus: recovery narrative and compensation proof | `Vitium` + `Loop` |
| Argus: monitoring and trace audit | `Elos` + `Minos` |
| Midas: cost and burn-rate | `Gula` |
| Sphinx: hard oracle challenge | `Apep` + `Dúbio` + `Minos` |
| Prometheus: tool enablement | `Patrono` + `Elos` |
| Cerberus: gatekeeping and evidence signal discipline | `Patrono` + `Minos` + future `Bedrock` |

## P0 Gap Resolutions

1. Lab/product boundary ownership
   `Éfeso` is the primary owner for source-authority and lab-product boundary discipline. `Minos` audits evidence and boundary claims. `Bedrock` remains the future final decision authority.
2. Observability and trace coverage
   `trace_coverage` becomes a required future field in `bot_run_result` and `Minos` verdict artifacts. `Elos` owns critical-path trace completeness. `Minos` audits completeness.
3. Quimera decomposition rule
   `Quimera` findings must involve at least two subsystems and must decompose into sub-findings owned by responsible bots. Single-layer findings must not remain under `Quimera`.
4. Gula economic impact
   `Gula` owns token, cost, quota, burn-rate, and resource exhaustion evidence. Future phases must produce resource-budget artifacts.
5. Abzu memory lifecycle
   `Abzu` owns TTL, provenance, stale memory, compression loss, and context poisoning. `Loop` owns replay and regression over memory-sensitive scenarios.
6. Sandbox and isolation ownership
   `Apep` owns sandbox escape, stale capability, cross-session leakage, kill-switch failure, and capability invariant breaks. `Vitium` owns technical fault recovery. `Elos` owns handoff and contract conformance across the isolation boundary.
7. Loop and Minos hard separation
   `Loop` replays and mutates. `Minos` audits evidence. `Minos` cannot replace `Loop`. LLM-as-judge cannot be final authority for critical gates.
8. Machine-readable Bedrock signals
   The defined signal names in this artifact are signals only. They never authorize `Bedrock`.

## Severity Model S0-S5

| Level | Meaning | Waiver Rule | Purgatorium Expectation | Bedrock Effect |
| --- | --- | --- | --- | --- |
| `S0` | informational | allowed | optional | no block |
| `S1` | low | allowed | optional | no block |
| `S2` | medium | allowed with owner | required if recurring or systemic | warn |
| `S3` | high | restricted | required | warn or block by threshold |
| `S4` | critical blocker | forbidden for security, privacy, authorization, rollback, source-of-truth, or product-boundary findings | required | block |
| `S5` | existential or product-blocking | never allowed | required | hard block |

Rules:

- `S5` cannot be waived.
- `S4` involving security, privacy, authorization, rollback, source-of-truth, or product boundary cannot be waived for `Bedrock`.
- `accepted_residual` is not `resolved`.
- `resolved` requires future fix artifact and retest artifact.
- warning accepted is not warning resolved.

## Evidence Requirements

Future phases must require these evidence fields at minimum:

- `scenario_id`
- `bot_id`
- `run_id`
- `input_hash`
- `prompt_hash` when applicable
- `config_hash`
- `before_state_ref`
- `after_state_ref`
- `trace_ref`
- `ledger_ref`
- `oracle_result_ref`
- `finding_ref`
- `reproduction_steps_ref`
- `severity_rationale_ref`
- `purgatorium_handoff_ref`

Allowed future evidence reference forms:

- `local_path + sha256`
- `JSON object + sha256`
- `local_uri + sha256`
- `ledger_event_id`

Artifact without content and hash must be invalid in future schema phases.

## Purgatorium Handoff Model

Future `Purgatorium FULL` handoffs must include:

- `handoff_id`
- `finding_id`
- `bot_id`
- `scenario_id`
- `severity`
- `affected_layer`
- `evidence_refs`
- `required_fix`
- `owner_category`
- `acceptance_criteria`
- `retest_required_by`
- `residual_risk_policy`
- `status`

Allowed status values:

- `open`
- `fixed`
- `retested`
- `accepted_residual`
- `blocked`
- `not_reproducible`
- `false_positive`
- `duplicate`
- `deferred_with_reason`

Rules:

- `Purgatorium FULL` proposes or applies fixes only in its own future phases.
- `Purgatorium FULL` does not close findings alone.
- `Loop` revalidates.
- `Minos` audits evidence.
- `accepted_residual` requires owner, expiry, and compensating controls.

## Bedrock Impact Signals

Machine-readable signal names locked by this gate:

- `BB-UNRESOLVED-S4`
- `BB-UNRESOLVED-S5`
- `BB-NO-REPLAY-EVIDENCE`
- `BB-NO-HITL-PROOF`
- `BB-LLM-ONLY-JUDGE`
- `BB-MISSING-PROVENANCE`
- `BB-COVERAGE-GAP`
- `BB-SCHEMA-DRIFT`
- `BB-FALSE-PASS`
- `BB-ACCEPTED-RISK-AS-RESOLVED`
- `BB-PRODUCT-CLAIM-INFLATION`

These are impact signals only.

- They do not authorize `Bedrock`.
- They do not replace human judgment.
- They do not promote product readiness.
- They exist so future phases can emit deterministic blockers or warnings for the future `Bedrock Gate`.

## Non-Execution Boundary

This phase remains planning-only.

It does not authorize:

- bot implementation
- bot execution
- attack execution
- scenario execution
- harness creation or execution
- real dry-run
- real apply
- sandbox apply
- runtime mutation
- frontend mutation
- backend mutation
- action-runtime mutation
- audio mutation
- product code mutation
- package installation
- dependency changes
- secrets access
- external API use
- external LLM use
- Bedrock execution
- Bedrock PASS
- product promotion
- pilot
- production
- commercial launch
- customer readiness

## Productization Non-Authorization

`Productization / Controlled Pilot` remains blocked unless future `Bedrock` explicitly permits it. This gate does not authorize productization, pilot, production, commercial launch, or market claims.

## Next Recommended Phase

`ARIS Infernus Lab FULL 13-Bot Contract Pack Planning Gate`
