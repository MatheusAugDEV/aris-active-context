INF-FULL-07 — IF-08 W1 Context/Memory/RAG Controlled Execution Sincronizado

current_phase: INF-FULL-07
status: inf_full_07_if08_authorization_gate_pass
current_status: if08_w1_context_memory_rag_controlled_execution_pass
decision: pass
latest_completed_phase: IF-08 W1 Context/Memory/RAG Controlled Execution
latest_completed_status: if08_w1_context_memory_rag_controlled_execution_pass
latest_completed_project_commit_sha: 1d0f51584e082d1f3f7c270df89d567a96066711
latest_completed_ci_state: CI_GREEN_CONFIRMED
next_phase: IF-08
active_next_phase: IF-08
active_next_phase_class: infernus_full_execution
next_phase_authorized_by_operator: true
standing_authorization: canonroadmap aprovado pelo operador
active_context_remote_main_reflects_if08_w1_context_memory_rag_controlled_execution: true
permanent_active_update_rule_installed: true
execution_authorized: false

O que fazer agora
Leia project_mirror/docs/infernus_full/infernus_full_canonroadmap.md.
Confirme que o último pacote sincronizado foi `IF-08 W1 Context/Memory/RAG Controlled Execution`.
Não reexecutar a execução controlada W1 nesta fase.
Este sync já registra `CIR=1.0` com `10/10` violações de integridade de contexto bloqueadas.
O proximo prompt deve executar o post-sync review canônico de W1.
O proximo passo recomendado neste estado e `post_sync_review_if08_w1_context_memory_rag_controlled_execution`.
Não emitir próximo prompt canônico se `aris-active-context/main` não refletir este resultado final.
Única coisa que requer comando do operador
Antes de executar waves reais contra o sistema: informe o operador e aguarde o comando de execução.
Também requer comando explícito do operador qualquer passo que toque produção/staging real, real_apply, produto/piloto, Bedrock, secrets, rede externa, dependências/package manager ou ação irreversível fora do laboratório.
Locks de execução real
IF-08 waves reais: false — aguardando comando de execução
runtime: false
real apply: false
produto: false
Bedrock: false
secrets: false
MCP: false
RAG ingestion: false
memory write: false
Esses locks não precisam ser reconfirmados. Estão no JSON. Não os mencione a cada ciclo.
