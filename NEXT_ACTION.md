# NEXT_ACTION

## Next operational gate
- current_macroblock: `MB1 — Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-A41 — Real MCP Candidate Runtime Isolation Review`
- next_gate: `F21-A42 — Real MCP Candidate Rollback Plan Review`
- reason: `runtime isolation is review-only and rollback planning is now the first remaining authorization gate`
- blocked_capabilities:
  - `candidate_approval_allowed: false`
  - `mcp_activation_allowed: false`
  - `mcp_config_write_allowed: false`
  - `vault_write_allowed: false`
  - `obsidian_bulk_read_allowed: false`
  - `network_allowed: false`
  - `dependency_install_allowed: false`
  - `runtime_mutation_allowed: false`
  - `product_promotion_allowed: false`
- note: `ACTIVE-CONTEXT-R1 removed historical next-gate blocks from NEXT_ACTION to keep the live pointer singular.`

The next operational gate is rollback plan review only. F21-A42 has not been executed.

## F21-A42 — Real MCP Candidate Rollback Plan Review
- phase_id: `F21-A42`
- status: `pending`
- note: `This is the single live phase reference retained for compatibility; the gate itself is not executed by ACTIVE-CONTEXT-R1.`
