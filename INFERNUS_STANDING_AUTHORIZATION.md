INFERNUS STANDING AUTHORIZATION
Decisão Permanente do Operador
Data: 2026-06-06
Autoridade: Operador (MatheusAugDEV)
Escopo: Todas as fases do Infernus FULL (IF-00 a IF-08 e subsequentes)

O operador aprovou o arquivo:
project_mirror/docs/infernus_full/infernus_full_canonroadmap.md

Essa aprovação constitui AUTORIZAÇÃO STANDING para toda a sequência definida no canonroadmap.

O que isso significa
O canonroadmap é o plano de execução completo do Infernus FULL.
O operador aprovou o plano inteiro de uma vez.
Cada fase individual do Infernus não precisa de nova autorização do operador para avançar.
O sistema lê o canonroadmap e executa o próximo passo definido nele.

O que ainda requer comando explícito do operador
Execução real de waves contra o sistema de produção ou staging real.
real_apply em qualquer contexto.
Promoção de produto ou piloto.
Bedrock gate final.
Qualquer ação com efeito irreversível no mundo real fora do laboratório.

O que NÃO requer autorização do operador
Avançar de uma fase de planejamento para a próxima no canonroadmap.
Materializar artifacts de gate.
Executar CI e validações.
Escrever documentos, JSONs, relatórios de fase.
Executar bots em ambiente sintético isolado (fixtures, simulações controladas).
Qualquer coisa que o canonroadmap lista como próximo passo após um gate pass.

## IF-08 Synthetic Wave Standing Authorization

For IF-08, synthetic isolated lab waves defined by the approved Infernus canonroadmap do not require a new per-wave operator permission prompt after their preflight/readiness gates pass.

The operator has explicitly authorized W0 and has instructed the system to stop requesting repeated permissions for synthetic IF-08 waves.

The assistant and Codex must not ask for ritual authorization before each synthetic isolated IF-08 wave when:
- the wave is listed in the approved canonroadmap;
- the wave preflight/readiness gate passed;
- all required contracts, oracles, controls, evidence outputs and stop conditions are present;
- CI is terminal green;
- no hard lock is violated;
- scope remains synthetic isolated lab only.

This standing authorization does not authorize:
- production or staging real systems;
- real_apply;
- product/pilot promotion;
- Bedrock final gate;
- secrets access;
- external network;
- dependency/package-manager mutation;
- irreversible real-world actions;
- any wave or action outside the approved canonroadmap.

Regra de comportamento do agente
Quando a fase atual é infernus_full ou infernus_full_execution e a decisão é pass:

Leia o canonroadmap.
Identifique o próximo passo.
Execute o próximo passo.
NÃO pergunte ao operador.
NÃO peça autorização.
Entregue o resultado.

Se o próximo passo envolve execução real (waves, apply, produto, Bedrock):

Pare antes da execução real.
Informe o operador o que está pronto para executar.
Aguarde comando explícito de execução.

Extensão futura
Quando o Infernus estiver completo, o operador aprovará o plano da camada seguinte (Purgatorium, BenchUIX, etc.) e esse arquivo será atualizado para incluir a nova standing authorization. O padrão é o mesmo: plano aprovado = autorização standing para toda a sequência.
