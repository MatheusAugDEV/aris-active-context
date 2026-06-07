INF-FULL-07 — IF-08 é a Próxima Fase

current_phase: INF-FULL-07
status: inf_full_07_if08_authorization_gate_pass
decision: pass
next_phase: IF-08
active_next_phase: IF-08
active_next_phase_class: infernus_full_execution
next_phase_authorized_by_operator: true
standing_authorization: canonroadmap aprovado pelo operador
execution_authorized: false

O que fazer agora
Leia project_mirror/docs/infernus_full/infernus_full_canonroadmap.md.
Identifique o que IF-08 — Attack Waves Execution requer.
Execute o primeiro passo de IF-08.
Após este policy repair, o próximo passo operacional é `IF-08 W0 Controlled Plan-Only Execution`.
W0 já foi explicitamente autorizado pelo operador para escopo `plan-only`, `synthetic isolated lab`, `no side effects`.
Não pedir nova frase ritual de autorização para W0 ou para waves sintéticas isoladas subsequentes quando o preflight passar, o CI estiver verde e nenhum hard lock for violado.
NÃO pergunte ao operador.
NÃO aguarde autorização.
Única coisa que requer comando do operador
Antes de executar waves reais contra o sistema: informe o operador e aguarde o comando de execução.
Também requer comando explícito do operador qualquer passo que toque produção/staging real, real_apply, produto/piloto, Bedrock, secrets, rede externa, dependências/package manager ou ação irreversível fora do laboratório.
Tudo que é preparação, fixtures, artifacts, planejamento: execute.
Locks de execução real
IF-08 waves: false — aguardando comando de execução
runtime: false
real apply: false
produto: false
Bedrock: false
secrets: false
Esses locks não precisam ser reconfirmados. Estão no JSON. Não os mencione a cada ciclo.
