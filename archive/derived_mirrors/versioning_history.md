# ARIS Active Context — Versioning History Archive

Arquivado em: 2026-06-08
Motivo: compaction refactor schema 3.0 — summaries 2.1 a 2.10 removidos do JSON ativo.
Autoridade: ACTIVE_CONTEXT_STATE.json (campo versioning_contract) é a fonte viva;
este arquivo é registro histórico imutável.

---

## schema_2_1_change_summary

Structural schema remains valid. This transition advances the live route from the explicit operator authorization grant review gate to the explicit operator authorization readiness closure gate after consolidating the packet/request/grant chain as future-only, non-authorizing, non-executing, and non-materializing.

## schema_2_2_change_summary

AC-REPAIR-01 activates anti-proliferation governance, requires reviewer SHA disclosure, adds CI fixture absence enforcement, and moves the canonical live route to a null next-phase state pending manual operator authorization.

## schema_2_3_change_summary

AC-OBS-02 adds gate TTL fields (gate_opened_at, gate_max_cycles, gate_cycles_used), an auto_advance policy object, a previous_phase_id field, and a last_boot_files_read receipt; it adds mirror sync enforcement and boot-receipt warnings to the validator. No execution, fixture, bot, or runtime authorization is granted. AC-TRANS-03 installs the Transition Table, autonomous loop handler, REGRA DE TRANSICAO, updates the validator with Transition Table enforcement, refreshes the test suite, and advances state to AC-TRANS-03. AC-CONTRACT-04 adds minimum_deliverable to every transition row, adds validator enforcement for gated deliverables, and blocks prompt_only pass declarations that lack real on-disk capability. AC-BREAK-05 installs three-layer circuit breaker: governance_gate_streak counter, gate signature deduplication, and cycle nudge. INF-MAT-01 materializes 13 synthetic bot fixture scenarios (65 files) on disk, resets governance_gate_streak to 0, and confirms fixture_materialization_allowed=true. INF-BOT-01 records one deterministic nemesis execution log with block verdict and enforces bot log safety fields in the validator. INF-MINOS-01 records one deterministic Minos verdict JSON derived from the nemesis execution log, enforces threshold_results, and keeps PURG-01 closed. PURG-01 creates one deterministic Purgatorium finding record from the existing Minos verdict, enforces a finding deliverable with severity/status and remediation locks, and keeps BENCH-01 closed. ACB-CORE-01 advances the live route only after traced uv bootstrap, uv.lock, pip-audit CI gate, and CycloneDX SBOM evidence exist in Project_ARIS. ACB-CORE-02 advances the live route only after explicit root __all__ baseline artifacts, Protocol exports, import smoke tests, and dedicated core-public-api CI evidence exist in Project_ARIS. OPERATOR_PREFERENCES.md is elevated into the priority read path immediately after DECISION_LOCKS, but remains subordinate to ACTIVE_CONTEXT_STATE.json, the schema, validator, Transition Table, and explicit operator/manual authorization locks.

## schema_2_4_change_summary

INF-FULL-01 opens as an operator-authorized scope charter only. The validator now enforces a scope-charter decision artifact, a scope matrix, a module scope manifest, and a charter markdown in Project_ARIS; it also requires all modules to be accounted for, unresolved_modules to remain empty, inf_full_opened=true, and all execution/product/pilot/Bedrock flags to remain false. current_phase_bots_executed is added because bot_execution_executed is historical-only. INF-FULL-02 advances the live route to a planning-only baseline freeze package, requires decision/inventory/hash-manifest/summary markdown deliverables, freezes scoped module and scenario references by hash, marks historical bot/minos/purg artifacts as reference-only, and keeps next_phase null because no Transition Table successor row exists yet.

## schema_2_5_change_summary

INF-FULL-03 materializes the canon-roadmap successor after explicit operator authorization. The Transition Table now includes INF-FULL-02 -> INF-FULL-03, the validator enforces if00-if04 minimum deliverables plus INF-FULL-03 opening decision/summary markdown artifacts, and the live route advances to a planning-only chain registration and preparation opening package while keeping all bot/runtime/product/Bedrock/secret/dependency execution flags false and next_phase null because no successor row exists after INF-FULL-03.

## schema_2_6_change_summary

INF-FULL-04 consumes the standing pre-execution operator authorization for the Infernus FULL gated sequence. The Transition Table now includes INF-FULL-03 -> INF-FULL-04 as prompt_only, the validator enforces the standing authorization policy plus IF-05 and IF-06 deliverables, and the live route advances to a planning-only scenario pack and harness readiness package while keeping all bot/runtime/product/Bedrock/secret/dependency execution flags false and next_phase null because no successor row exists after INF-FULL-04.

## schema_2_7_change_summary

INF-FULL route sync repair materializes the saved canonroadmap successor after INF-FULL-04 without opening execution. The Transition Table now includes INF-FULL-04 -> INF-FULL-05 as prompt_only and maps the saved IF-07 Pre-Execution Review Gate into the canonical INF-FULL sequence. The validator now allows a non-null prompt-only next_phase for infernus_full when a Transition Table row exists and standing pre-execution authorization remains execution-false. Scenario ambiguity is normalized by preserving scenario_count=13 as historical fixture count while adding explicit current-phase planned counts for scenarios, bots, mutation families, and oracle families.

## schema_2_8_change_summary

INF-FULL-05 closes the pre-execution review gate after IF07 deliverables are materialized. The validator now enforces the IF07 decision, no-execution attestation, scenario-count normalization evidence, and validator evidence artifacts, and it allows infernus_full to end in a terminal null-next-phase state when no explicit INF-FULL-05 successor row exists in the Transition Table.

## schema_2_9_change_summary

INF-FULL-05 now materializes the explicit IF-08 successor route without authorizing execution. The Transition Table includes INF-FULL-05 -> INF-FULL-06 as prompt_only, active_next_phase and next_phase advance to INF-FULL-06 with active_next_phase_class=infernus_full_execution_authorization, and the validator enforces an IF-08 authorization package consisting of decision, successor validation matrix, no-execution attestation, summary, and report artifacts while preserving all execution, bot, runtime, Bedrock, product, secrets, dependency, dry-run, and apply locks as false.

## schema_2_10_change_summary

INF-FULL-06 creates the excludent/ structural layer as the logical exclusion zone. EXCLUDENT_POLICY.md is materialized in both repos, old Infernus roadmaps (infernus_full_roadmap_v1.md, infernus_full_execution_spec.md) are moved to excludent/infernus/roadmaps/ with SHA manifest, MANDATORY_READ_FIRST_RULES.md gains the EXCLUDENT RULE, CONTEXT_INDEX.md registers excludent=excluded_from_context, and only infernus_full_canonroadmap.md remains visible as active roadmap authority. No execution, bot, runtime, Bedrock, product, secrets, or dependency mutation is authorized.

## schema_2_12_change_summary

INF-FULL-07 declares IF-08 as next phase with standing authorization from canonroadmap approval. next_phase and active_next_phase advance from null to IF-08. next_phase_authorized_by_operator=true because the canonroadmap is the operator standing authorization. Execution locks remain false. The system does not need per-phase operator authorization for infernus_full phases - canonroadmap approval is sufficient.

## schema_2_13_change_summary

Adds latest-completed execution status tracking, explicit no-execution sync evidence, and the permanent rule that active-context remote main must reflect every canonical phase result before PASS or next-prompt emission.

## schema_2_13_change_summary (top-level field, also archived)

Adds latest-completed execution status and no-execution sync evidence, plus a permanent active-context remote-main sync rule after every canonical phase result.
