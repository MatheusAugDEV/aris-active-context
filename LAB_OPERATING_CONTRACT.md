# LAB_OPERATING_CONTRACT

## Purpose

ARIS Lab is the permanent validation, evaluation, regression, red-team, promotion, demotion, and obsolescence infrastructure for ARIS capabilities.

The Lab is not a future idea, not documentation-only, and not a commercial release switch. It is the operational maturity control plane between ARIS Project work and ARIS final-grade capability state.

## Core Rule

Every future ARIS phase or capability must pass through the Bedrock Gate before it can be treated as advanced, mature, final-grade, product-ready, or safe to resume dependent work.

No Codex status, chat response, commit text, placeholder, checklist, or narrative claim replaces a Bedrock Gate verdict.

## Bedrock Gate Definition

The Bedrock Gate is a deterministic, auditable, versioned, non-LLM, evidence-based decision boundary.

It evaluates artifact packs, tests, runners, ledgers, safety attestations, drift checks, regression evidence, rollback or compensation evidence when applicable, source-of-truth alignment, and dangerous-operation flags.

The gate opens only when the evidence package is sufficient.

## Required Verdicts

Allowed Bedrock verdicts:

- PASS: evidence is sufficient to advance.
- WARN: phase may advance only with explicit warnings carried forward.
- BLOCK: phase cannot advance; correction required.
- NEEDS_REVIEW: evidence is ambiguous or incomplete; human/architectural review required.
- REGRESSION: baseline worsened; correction required before advance.
- OBSOLETE: capability or phase is superseded by a later approved decision.

## Non-Negotiable Requirements

A future phase is not complete unless it has:

- read-first compliance with active-context;
- decision JSON;
- summary/report artifacts;
- tests or deterministic validation evidence;
- runner evidence when applicable;
- safety attestation;
- drift check;
- dangerous booleans verified false unless explicitly allowed by a prior gate;
- rollback/compensation evidence when side effects exist;
- regression evidence when a baseline exists;
- next-phase contract;
- Bedrock Gate verdict recorded in LAB_VERDICTS.md or linked artifacts.

## Project to Final-Grade Boundary

ARIS Project can create, test, repair, and mature capabilities.

ARIS final-grade state requires Bedrock Gate pass.

Commercial release, real customer pilot, real connector use, runtime mutation, schema apply, SQLite persistence, network use, dependency install, and product promotion are not automatically authorized by a Bedrock pass. Those require explicit scoped gates when relevant.

## Current State

- Lab control plane: active.
- Bedrock Gate: mandatory for future phase/capability advancement.
- Bedrock Gate operational scope: evidence/artifact verdicts and Lab governance.
- Product/commercial release: blocked until explicit future gate.
- F33: paused under Lab governance, not cancelled.
- F33.Z22: preserved as latest F33 operational closure anchor.
- F44: hardening, red-team expansion, benchmark maturity, audit maturity of the Lab.
- F51+: preserved as external advisory research only; not canonical, not implementation authorization.

## Immediate Enforcement

All next prompts, Codex phases, phase completions, and roadmap changes must explicitly state how the Bedrock Gate is used or why the phase is preparing Bedrock enforcement.

The next Lab phase must harden/enforce this operating contract rather than bypass it.
