# INF-FULL-01 Scope Charter

## Verdict

PASS — INF-FULL-01 scope charter is opened by operator authorization.

## Execution Boundary

This opens scope/charter only.
No bots are executed.
No runtime is started.
No product, pilot, Bedrock, or secret access is authorized.

## Anti-loop decision

The preflight legacy diagnostic returned WARN because 16 modules were INCERTO.
A second diagnostic loop is rejected.
In Infernus, uncertainty enters scope to avoid false negatives.

## Initial Infernus scope

ACB core:
backend, mcp_runtime, runtime, product_boundary, supply_chain.

Active critical:
actions, app, config, logging, security.

Uncertain included:
action_runtime, action_runtime_contracts, audio, bedrock, capabilities, context, evaluation, intelligence, knowledge, lab, memory, persona, response, turn, ui, voice.

## Secondary scope

cockpit, hardening_base, intents, lab_simulation, learning, model_gateway, product_loop, research, response_quality, rich_output, roadmap, sandbox, understanding.

## Quarantine hash-only

diagnostics, packaging.

## Next required gate

INF-FULL-02 must be Baseline Freeze Planning.
No attack wave may run before baseline freeze records hashes for every scoped and quarantine module.
