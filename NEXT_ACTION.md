# NEXT_ACTION

## Next operational gate
- current_macroblock: `MB1 - Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-CTX-D1 - Active Context Operating System Full Diagnostic Gate`
- next_gate: `F21-CTX-D2 - Active Context Operating System Reform Design Gate`
- reason: `The active-context OS diagnostic is complete with warnings; the next safe step is design-only reform planning before any F21-A61 implementation.`
- blocked_capabilities:
  - `f21_a61_allowed_next: false`
  - `prompt_kernel_implementation_allowed: false`
  - `candidate_approval_allowed: false`
  - `automatic_activation_allowed: false`
  - `mcp_activation_allowed: false`
  - `mcp_config_write_allowed: false`
  - `vault_write_allowed: false`
  - `obsidian_bulk_read_allowed: false`
  - `network_allowed: false`
  - `dependency_install_allowed: false`
  - `runtime_mutation_allowed: false`
  - `frontend_mutation_allowed: false`
  - `audio_mutation_allowed: false`
  - `action_runtime_mutation_allowed: false`
  - `product_promotion_allowed: false`

The next operational gate is design-only. It may propose the active-context reform architecture but must not compact, rewrite, implement Prompt Kernel, mutate runtime, activate MCP, install dependencies, or change external-reference authority.
