# INF-FULL-07 — Estado Atual

- phase_id: `INF-FULL-07`
- status: `inf_full_07_if08_authorization_gate_pass`
- current_status: `if08_w3_post_sync_review_w4_readiness_pass`
- latest_completed_phase: `IF-08 W3 Controlled Execution Post-Sync Review & W4 Readiness Decision`
- latest_completed_status: `if08_w3_post_sync_review_w4_readiness_pass`
- next_phase: `IF-08`
- active_next_phase_class: `infernus_full_execution`
- next_phase_authorized_by_operator: `true`
- standing_authorization: `INFERNUS_STANDING_AUTHORIZATION.md`
- active_context_remote_main_reflects_if08_w3_post_sync_review: `true`
- permanent_active_update_rule_installed: `true`
- execution_authorization: `false`

Referências ativas desta fase:

- `artifacts/if08_w3_post_sync_review/decision.json`
- `artifacts/if08_w3_post_sync_review/summary.json`
- `artifacts/if08_w3_post_sync_review/report.md`
- `artifacts/infernus/if08_w3_post_sync_review_decision_2026_06_07.json`
- `artifacts/infernus/if08_w3_post_sync_review_summary_2026_06_07.json`
- `artifacts/infernus/if08_w3_post_sync_review_report_2026_06_07.md`
- `artifacts/infernus/if08_w4_readiness_matrix_2026_06_07.json`
- `artifacts/infernus/if08_w3_post_sync_no_execution_attestation_2026_06_07.json`
- `docs/infernus_full/if08_w3_post_sync_review_2026_06_07.md`
- `artifacts/if08_w3_runtime_tool_mcp_sandbox_controlled_execution/decision.json`
- `artifacts/if08_w3_runtime_tool_mcp_sandbox_controlled_execution/summary.json`
- `artifacts/if08_w3_runtime_tool_mcp_sandbox_controlled_execution/report.md`
- `artifacts/infernus/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_decision_2026_06_07.json`
- `artifacts/infernus/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_summary_2026_06_07.json`
- `artifacts/infernus/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_report_2026_06_07.md`
- `artifacts/infernus/if08_w3_runtime_sandbox_detection_matrix_2026_06_07.json`
- `artifacts/infernus/if08_w3_tool_mcp_detection_matrix_2026_06_07.json`
- `artifacts/infernus/if08_w3_oracle_results_2026_06_07.json`
- `artifacts/infernus/if08_w3_evidence_bundle_manifest_2026_06_07.json`
- `artifacts/infernus/if08_w3_sirene_conditional_execution_record_2026_06_07.json`
- `artifacts/infernus/if08_w3_no_real_execution_attestation_2026_06_07.json`
- `docs/infernus_full/if08_w3_runtime_tool_mcp_sandbox_controlled_execution_2026_06_07.md`
- `artifacts/if08_w2_post_sync_review/decision.json`
- `artifacts/infernus/if08_w2_post_sync_review_decision_2026_06_07.json`
- `artifacts/if08_w1_post_sync_review/decision.json`
- `artifacts/infernus/if08_w1_post_sync_review_decision_2026_06_07.json`
- `artifacts/if08_w1_context_memory_rag_controlled_execution/decision.json`
- `artifacts/infernus/if08_w1_context_memory_rag_controlled_execution_decision_2026_06_07.json`
- `artifacts/infernus/if08_w1_context_integrity_detection_matrix_2026_06_07.json`
- `docs/infernus_full/if08_w1_context_memory_rag_controlled_execution_2026_06_07.md`
- `artifacts/if08_w1_context_memory_rag_preflight_readiness/decision.json`
- `artifacts/infernus/if08_w1_context_memory_rag_preflight_readiness_decision_2026_06_07.json`
- `artifacts/if08_w05_controlled_execution/decision.json`
- `artifacts/infernus/if08_w05_controlled_execution_decision_2026_06_07.json`
- `artifacts/infernus/if08_w05_evidence_bundle_manifest_2026_06_07.json`
- `INFERNUS_STANDING_AUTHORIZATION.md`
- `project_mirror/docs/infernus_full/infernus_full_canonroadmap.md`
- `EXCLUDENT_POLICY.md`
- `OPERATOR_PREFERENCES.md`
- `MANDATORY_READ_FIRST_RULES.md`
- `PROMPT_CONTRACT.md`

---

# CONTEXT_INDEX

## Zona Excludent

- `excludent/` = `excluded_from_context`
- `read_by_default` = `false`
- read_by_default = false
- `authority` = `none`
- `use` = `forensic_only`
- Política: `EXCLUDENT_POLICY.md`
- Roadmap canônico ativo do Infernus: `project_mirror/docs/infernus_full/infernus_full_canonroadmap.md`

## Live Pointers

- `CURRENT_STATE.md`
- `NEXT_ACTION.md`
- `DECISION_LOCKS.md`
- `EXTERNAL_REFERENCES.md`
- `MODEL_REASONING_POLICY.md`
- `HANDOFF_RESPONSE_POLICY.md`
- `ARIS_PHASE_LEDGER.md`
- `BEDROCK_GATE.md`
- `NORTH_POLE.md`
- `PHASE_SPECIFIC_GATES.md`

## Perfis de Contexto

- `BOOT_PROFILE.md` — boot canônico de quatro arquivos.
- `READ_PROFILE.md` — permissões de leitura em camadas.

## Política de Modelo e Raciocínio

- policy_file: `MODEL_REASONING_POLICY.md`
- default_model: `5.4 mini`
- default_reasoning_level: `baixo`
- active_context_touch_default: `5.4 normal / alto`
- critical_recovery_security_roadmap_default: `5.5 / altissimo`
- policy_is_advisory_not_authorization: `true`
- Consultar `MODEL_REASONING_POLICY.md` ao gerar prompts futuros do ARIS para declarar tier e reasoning de forma compacta.

## Política de Handoff

- policy_file: `HANDOFF_RESPONSE_POLICY.md`
- default_handoff_style: `compact`
- artifact_detail_is_source_of_truth: `true`
- chat_handoff_should_not_duplicate_artifacts: `true`
- Consultar `HANDOFF_RESPONSE_POLICY.md` antes do handoff final de fase. Evidência detalhada vai em artifacts, não no chat.

## Referência Externa

- `ext_ref_huw_prosser_fury_2026_05`: referência arquitetural externa catalogada para decisões futuras de Prompt Kernel, Context Compression, Memory Kernel, Skill Kernel, Tool Harness, Voice Runtime, UI Observability e Action Runtime.
- status: `catalogued_external_reference`
- implementation_allowed_now: `false`
- source_of_truth_rank: `reference_only_non_authoritative`

## Notas

- JSON vence Markdown sempre. Drift de Markdown contra JSON é erro bloqueante.
- F21, F32, F33 = ruído histórico. Não definem rota ativa. Não leia como autoridade.
- `archive/` = trilha de auditoria. Nunca autoridade de roteamento.
- `excludent/` = excluído do contexto. Não leia por padrão.
- IF-08 synthetic isolated waves inherit standing authorization after preflight pass; hard-lock exceptions remain explicit.
- `NORTH_POLE.md` é a referência estratégica norte.
- `BEDROCK_GATE.md` define os critérios de promoção para produto.
- Referências externas são contexto consultivo apenas. Não autorizam implementação, mudança de sequência de roadmap, mutação de runtime, MCP, promoção de produto, uso real de cliente ou release de produção.
- The W3 post-sync review packet is canonical; the next canonical step is W4 preflight readiness and no real execution surface is authorized.
