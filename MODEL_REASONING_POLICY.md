# MODEL_REASONING_POLICY

## Purpose

This file defines the operational default for selecting Codex/agent model tier and reasoning level for ARIS prompts. It is part of `aris-active-context` and must be considered by future ARIS prompt generation, phase execution, review, recovery, and status handoff.

## Default model policy

- default_model: `5.4 mini`
- default_reasoning_level: `baixo`
- escalation_required_when_phase_risk_increases: `true`
- model_policy_overrides_chat_memory: `true`
- model_policy_is_advisory_not_authorization: `true`

`5.4 mini` is the default for low-risk, localized, bounded tasks. It must not be used automatically for high-risk ARIS gates merely because it is the default.

## Model and reasoning matrix

| Reasoning level | Preferred model | Acceptable alternative | Use when |
|---|---|---|---|
| `baixo` | `5.4 mini` | `5.4 normal` | Small isolated patch, grep, formatting, typo/doc tweak, one-file correction, narrow unit-test adjustment, low-risk text cleanup. |
| `medio` | `5.4 normal` | `5.4 mini` only for bounded/simple cases | Simple runner, small artifact/doc/test change, scoped active-context note, two-to-four-file patch with clear acceptance criteria. |
| `alto` | `5.4 normal` | `5.5` when ambiguity/risk exists | Full ARIS phase, runner + tests + artifacts, active-context update, NEXT_ACTION/DECISION_LOCKS/ledger touch, multi-file validation, nontrivial parser/gate. |
| `altissimo` | `5.5` | `5.4 normal` only if constrained and stable | Recovery from partial/broken phase, source-of-truth drift, active-context conflict, roadmap/macroblock decision, security boundary, permission gate, rollback/ledger, Prompt Kernel, Memory Kernel, Action Runtime, Voice Runtime, external reference integration, Huw/Fury-style risk review. |

## Escalation rules

Escalate from `5.4 mini` to `5.4 normal` or `5.5` when any task touches:

- `aris-active-context/CURRENT_STATE.md`
- `aris-active-context/NEXT_ACTION.md`
- `aris-active-context/DECISION_LOCKS.md`
- `aris-active-context/CONTEXT_INDEX.md`
- `aris-active-context/ARIS_PHASE_LEDGER.md`
- `aris-active-context/EXTERNAL_REFERENCES.md`
- `aris-active-context/MODEL_REASONING_POLICY.md`
- Prompt Kernel planning/review/implementation planning
- Memory Kernel
- Skill Kernel
- Action Runtime
- Sidecar Executor
- Voice Runtime
- provider/config/secrets
- permissions, gates, ledger, rollback, product/customer/production flags
- parser or validation logic that can produce false authorization or false blockage
- recovery from a partially completed Codex run
- external architectural references that could affect roadmap placement

## Hard guidance

- `5.4 mini` remains the default model.
- Do not use `5.4 mini` for recovery of a partial ARIS phase unless the patch is strictly one small known issue and the next model escalation is unavailable.
- Do not use `5.4 mini` for source-of-truth reconciliation, permission boundaries, roadmap placement, security decisions, or multi-file gate closures.
- For prompts that affect active-context, always state the recommended model and reasoning level explicitly.
- For F21-A58-like recovery, use `5.5` preferred, `5.4 normal` acceptable, `5.4 mini` not recommended.

## Prompt block template

Use this block in future ARIS prompts:

```text
Modelo recomendado:
- Preferencial: <5.4 mini | 5.4 normal | 5.5>
- Alternativa aceitável: <...>
- Não usar: <... if applicable>

Raciocínio esperado:
- <baixo | medio | alto | altissimo>

Motivo:
- <why this phase/task requires this tier>
```

## Non-authorizations

This policy does not authorize:

- implementation;
- runtime mutation;
- MCP activation;
- network access;
- dependency installation;
- product promotion;
- customer real use;
- production release;
- bypassing active-context, Bedrock, North Pole, phase-specific gates, permission gates, ledger, rollback, or sidecar constraints.

## Current standing preference

- Standard default: `5.4 mini` + `baixo` reasoning.
- ARIS phase default when active-context/gates/artifacts are touched: `5.4 normal` + `alto` reasoning.
- ARIS critical/recovery/security/roadmap default: `5.5` + `altissimo` reasoning.
