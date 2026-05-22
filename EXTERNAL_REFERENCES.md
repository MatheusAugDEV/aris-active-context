# EXTERNAL_REFERENCES

## ext_ref_huw_prosser_fury_2026_05

- status: `catalogued_external_reference`
- source_type: `external_architectural_reference`
- primary_source: `Huw Prosser public GitHub corpus / Fury SDK Tier-1 report`
- catalogued_date: `2026-05-22`
- implementation_allowed_now: `false`
- roadmap_direct_insert_allowed_now: `false`
- phase_sequence_change_allowed_now: `false`
- roadmap_mutation_allowed: `bounded_macroblock_mapping_only`
- macroblock_mapping_required: `true`
- decision_gate_required_before_use: `true`
- source_of_truth_rank: `reference_only_non_authoritative`
- next_action_changed: `false`

### Strategic value

The reference corpus has medium-high strategic value as an ergonomics and architecture reference for future ARIS subsystems, especially agent harness, history management, memory scoping, skills, STT/TTS, VAD, tool schemas, streaming events, and local assistant UX.

### Primary mapping

| Extracted pattern | ARIS placement | Macroblock class | Decision |
|---|---|---|---|
| Raw JSONL transcript preservation | Ledger / Audit / Context OS | Governance & Audit | `ADOPT_AS_PRINCIPLE_WITH_GATES` |
| Static history fallback | Active Context / Context Compression | Context OS | `ADOPT_AS_PRINCIPLE` |
| LLM history compaction with raw preservation | Prompt Kernel / Context Compression | Context OS | `ADAPT_WITH_GATES` |
| Tool JSON Schema + parameter pruning | Tool Harness / Action Registry | Tool Subsystem | `ADOPT_AS_PRINCIPLE_WITH_SCHEMA_VERSIONING` |
| Memory scope primitive | Memory Kernel | Memory Subsystem future | `ADAPT_WITH_GATES` |
| SKILL.md convention | Skill Kernel | Skill Subsystem future | `ADAPT_WITH_GATES` |
| Runner async interruption | UI / Action Runtime | Action Subsystem | `ADAPT_WITH_GATES` |
| STT/TTS local-first | Voice Runtime | Voice Subsystem | `ADAPT_WITH_GATES` |
| VAD-gated capture | Voice Runtime / UX | Voice Subsystem | `STUDY_MORE` |
| Tool UI emit events | UI Observability | Observability | `ADAPT_WITH_GATES` |
| Parallel tool execution | Action Runtime | Action Subsystem | `DEFER` |
| Voice cloning reference audio | Voice Runtime | Voice Subsystem | `DEFER` |
| Direct shell execution | Sidecar Executor only as rejected direct pattern | Action Subsystem | `REJECT_DIRECT_IMPLEMENTATION` |
| Filesystem tools without jail | Sidecar Executor only as rejected direct pattern | Action Subsystem | `REJECT_DIRECT_IMPLEMENTATION` |
| SOUL.md raw system prompt injection | Active Context / Prompt Kernel | Context OS | `REJECT` |
| Master/system prompt prefixed into user content | Prompt Kernel security boundary | Prompt Subsystem | `REJECT` |
| Mutable history as direct operation | Ledger / Audit | Governance & Audit | `REJECT_DIRECT_INTERFACE` |

### Required locks before any future use

- External references do not authorize implementation.
- Huw/Fury patterns cannot bypass `BEDROCK_GATE.md`, `NORTH_POLE.md`, phase-specific gates, permission gates, ledger, rollback, sidecar execution, or source-of-truth precedence.
- Direct bash/filesystem tools are rejected as LLM tools and may only be reconsidered through sidecar execution, permission gate, ledger, rollback, path jail, capability binding, and deterministic tests.
- Durable memory requires provenance, validity window, scope binding, revocation, audit trail, and privacy policy before implementation.
- External skills require signed registry, hash pinning, explicit capability declaration, human/security review, and promotion gate.
- Raw project-file injection into system prompts is rejected.
- Master/system/persona content must never be prefixed into user content.
- Parallel tool execution remains blocked until deterministic scheduling, capability binding, and rollback/compensation are proven.
- Voice cloning remains deferred until anti-impersonation gates and audio retention policy exist.
- Code reuse remains blocked until license compatibility and full source review are verified.

### Roadmap placement policy

This reference may inform future design only when the active macroblock explicitly touches the relevant subsystem. It must not reorder the current F21 Prompt Kernel sequence. Any use must be revalidated in the relevant phase with explicit artifacts and tests.

### Explicit non-authorizations

- prompt_kernel_implementation_allowed_now: `false`
- template_library_allowed_now: `false`
- batch_runner_allowed_now: `false`
- tool_harness_implementation_allowed_now: `false`
- memory_kernel_implementation_allowed_now: `false`
- skill_kernel_implementation_allowed_now: `false`
- voice_runtime_change_allowed_now: `false`
- action_runtime_change_allowed_now: `false`
- mcp_activation_allowed_now: `false`
- runtime_mutation_allowed_now: `false`
- product_promotion_allowed_now: `false`
- customer_real_use_allowed_now: `false`
- production_release_allowed_now: `false`
