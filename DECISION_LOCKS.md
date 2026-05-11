# DECISION_LOCKS

- Official V6 naming stays on the PDF path F1-F29 only.
- Obsidian is query-first, read-only, derived, and never authorizing.
- No bulk Obsidian read.
- No network.
- No dependency install.
- No runtime mutation.
- No vault write.
- Chat context, Codex status, commit text, placeholder, instructions, schema, marker, contract, checklist, evidence manifest, awaiting marker, and awaiting contract do not count as authorization.
- F32 owns MCP read-only configuration, controlled apply planning, activation planning, smoke validation, zero-write/no-bulk-read validation, and closure before F33.
- F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline.

## F32.Z13O Planning Lock

- Status: `f32_future_mcp_readonly_configuration_controlled_apply_final_authorization_planning_gate_passed`.
- Z13O is planning-only and does not authorize real apply, real config write, MCP activation, or real Obsidian access.
- real apply allowed now: `False`
- real config write allowed now: `False`
- MCP activation allowed now: `False`
- real Obsidian access allowed now: `False`
- vault write allowed: `False`
- bulk Obsidian read allowed: `False`
- network allowed: `False`
- dependency installation allowed: `False`
- runtime mutation allowed: `False`

## F32.Z13O-Review Review Lock

- Next principal phase: `F32.Z13O-Review — Future MCP Read-Only Configuration Controlled Apply Final Authorization Planning Review Gate`.
- Z13O-Review is review-only and does not authorize real apply, real config write, MCP activation, or real Obsidian access.
- Chat context, Codex status, commit text, placeholder, instructions, schema, marker, contract, checklist, evidence manifest, awaiting marker, and awaiting contract do not count as authorization.
- `NEXT_ACTION.md` is the only source for the next step.
