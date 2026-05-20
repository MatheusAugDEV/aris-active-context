## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_warn`
- decision: `warn`
- next_gate: `F21-A6 — Obsidian MCP Human Evidence Intake`
- reason: `hard locks, next action, current state, phase artifacts, official docs, project context, and consultive external context are ranked deterministically`
- blockers: `0`
- warnings: `0`

The next operational step is the Obsidian MCP human evidence intake gate, not product, runtime, or MCP work.
## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_ready`
- decision: `pass`
- next_gate: `F21-A6 — Obsidian MCP Human Evidence Intake`
- reason: `hard locks, next action, current state, phase artifacts, official docs, project context, and consultive external context are ranked deterministically`
- blockers: `0`
- warnings: `0`

The next operational step is the Obsidian MCP human evidence intake gate, not product, runtime, or MCP work.
## F21-A5 — Source-of-Truth Precedence Gate
- status: `source_of_truth_precedence_gate_blocked`
- decision: `blocked`
- next_gate: `F21-A6 — Obsidian MCP Human Evidence Intake`
- reason: `hard locks, next action, current state, phase artifacts, official docs, project context, and consultive external context are ranked deterministically`
- blockers: `1`
- warnings: `0`

The next operational step is the Obsidian MCP human evidence intake gate, not product, runtime, or MCP work.
## F21-A4 — Context Budget Policy Gate
- status: `context_budget_policy_gate_ready`
- decision: `pass`
- next_gate: `F21-A5 — Source-of-Truth Precedence Gate`
- reason: `summary-first, query-first, and bounded active-context tiers are formalized without measured token-saving claims`
- blockers: `0`
- warnings: `0`

The next operational step is the source-of-truth precedence gate, not product, runtime, or MCP work.
## F21-A3 — Claude Code Instruction Alignment
- status: `claude_code_instruction_alignment_ready`
- decision: `pass`
- next_gate: `F21-A4 — Context Budget Policy Gate`
- reason: `F21-A3 aligned Claude Code with active-context first, source precedence, untrusted input boundaries, and final handoff requirements; continue with F21-A4`
- blockers: `0`
- warnings: `0`

The next operational step is the context budget policy gate, not any product, runtime, or MCP path.

## F21-A2 — Codex Skill Alignment Review
- status: `codex_skill_alignment_review_warn`
- next_gate: `F21-A3 — Claude Code Instruction Alignment`
- reason: `F21-A2 aligned the Codex skill with active-context, source precedence, and untrusted input boundaries; continue with F21-A3 — Claude Code Instruction Alignment`
- blockers: `0`
- warnings: `3`

The next operational step is the Claude Code instruction alignment review, not any product, runtime, or MCP path.
## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_ready_with_warnings`
- next_gate: `F21-A2 — Codex Skill Alignment Review`
- reason: `F21-A1 closed as a warn gate; continue the active track at F21-A2`
- blockers: `none`

The next operational step is the Codex skill alignment review, not any product, runtime, or MCP path.

## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_blocked`
- next_gate: `F21-A2 — Codex Skill Alignment Review`
- reason: `F21-A1 closed as a warn gate; continue the active track at F21-A2`
- blockers: `['source_precedence_policy_undefined', 'active_context_read_first_not_verified']`

The next operational step is the Codex skill alignment review, not any product, runtime, or MCP path.

## F21-A1 — Context Source Access Policy & Untrusted Input Boundary
- status: `f21_a1_context_source_access_policy_blocked`
- next_gate: `F21-A2 — Codex Skill Alignment Review`
- reason: `F21-A1 closed as a warn gate; continue the active track at F21-A2`
- blockers: `['source_precedence_policy_undefined', 'untrusted_input_boundary_undefined', 'active_context_read_first_not_verified']`

The next operational step is the Codex skill alignment review, not any product, runtime, or MCP path.

## ARIS-CONTEXT-MACROBLOCK-CLEANUP — Next Operational Pointer
- macroblock_id: `MB1`
- macroblock_title: `Context Governance & Input Trust Boundary`
- legacy_phase_id: `F21`
- next_gate: `F21-A1 — Context Source Access Policy & Untrusted Input Boundary`
- reason: `trust boundary before memory, actions, connectors, productization, and customer-real use`
- blockers: `none for F21-A1`
- explicit_non_actions:
  - `do not start F33`
  - `do not start R0`
  - `do not start product/customer-real work`
  - `do not reopen P29`
  - `do not reopen F32`
- evidence:
  - `artifacts/context/roadmap_canonical_state_gate_decision.json`
  - `artifacts/context/roadmap_next_action_recommendation.json`
  - `docs/roadmap/roadmap_macroblocks.md`
  - `docs/roadmap/roadmap_macroblocks_r0_f120.md`
