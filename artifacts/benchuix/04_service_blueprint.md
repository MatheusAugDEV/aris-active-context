# BENCHUIX-04 Service Blueprint

## Definição da fase

BENCHUIX-04 define a ponte entre experiência visível e mecanismos de confiança. Cada toque do cliente deve ter frontstage, backstage, suporte, evidência, falha prevista e limite de escopo.

## Tese

"Todo touchpoint client-facing precisa ter evidence lane. Se o cliente vê, o sistema precisa provar. Se o sistema faz, o cliente precisa entender."

## Regras de boundary obrigatórias

- Preview/simulação nunca toca estado real.
- Aprovação sensível nunca ocorre fora do Workspace/Companion.
- Demo Sandbox usa dados sintéticos.
- Evidence Receipt não pode virar log técnico.
- Rollback não pode prometer desfazer side-effect irreversível.
- Failure Card não pode expor stack trace.
- Internal Admin não aparece para cliente.
- Canais auxiliares não executam ação.
- Qualquer gap de experiência × runtime real vai para Crisol.
- Qualquer gap de secrets/produção/Bedrock vai para Bedrock.

## Raias obrigatórias

- `Cliente / Dono-Solo`
- `Frontstage / UI`
- `Backstage / Sistema`
- `Support / Policy`
- `Evidence Lane`
- `Failure / Timeout`
- `Boundary / Destination`

## FLOW_01_FIRST_OPEN_TODAY

- objetivo do cliente: entender o que importa agora em poucos segundos.
- gatilho: primeira abertura do ARIS Client Workspace no dia.
- telas/componentes envolvidos: `ARIS_CLIENT_WORKSPACE`, `APP_SHELL`, `TOP_BAR`, `TODAY_SUMMARY_CARD`, `SIDE_OR_BOTTOM_NAV`, `EMPTY_STATE`.
- dados permitidos: status sintético, resumo do dia, alertas visíveis, aprovações pendentes.
- dados proibidos: stack trace, secret, payload técnico, dado real de PSP.
- o que ARIS vai mostrar: resumo claro, próximos passos, alertas acionáveis.
- o que ARIS não vai mostrar: dashboard corporativo, internals de runtime, admin.
- evidência gerada ou esperada: abertura contextual registrada como evidência leve de navegação e estado atual.
- falha esperada: indisponibilidade parcial da síntese.
- timeout esperado: atraso curto de carregamento com fallback para skeleton e mensagem de estado.
- comportamento degradado: mostrar dados mínimos e banner de limitação sem prometer precisão total.
- critério de BLOCK: tela Hoje exigir leitura técnica ou misturar backstage bruto.
- invariantes protegidas: densidade cognitiva, compressão de contexto, isolamento.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Abre o ARIS para saber o que precisa fazer hoje | `TODAY_SUMMARY_CARD` resume pendências, risco e próximos passos | Sistema monta visão sintética a partir de sinais permitidos e sem tocar estado real mutável | Policy exige linguagem humana e baseline Modo A | Recibo leve de estado carregado e timestamp visível | `LOADING_SKELETON` vira `DEGRADED_MODE_BANNER` se a síntese atrasar | Gap de síntese local vai para `local_repair`; qualquer dependência de runtime real vai para `Crisol` |

## FLOW_02_ONBOARDING_TO_FIRST_SAFE_SIMULATION

- objetivo do cliente: sair do onboarding com primeira simulação segura entendível.
- gatilho: entrada guiada após descoberta inicial ou sandbox.
- telas/componentes envolvidos: `PUBLIC_LANDING`, `DEMO_SANDBOX`, `TEMPLATE_CARD`, `BUSINESS_PROFILE_FORM`, `SIMULATION_PREVIEW`, `WILL_WILL_NOT_BLOCK`.
- dados permitidos: perfil incremental, exemplos sintéticos, parâmetros de simulação.
- dados proibidos: credenciais reais, integração real, secrets.
- o que ARIS vai mostrar: caminho curto, template recomendado, prévia segura, limites explícitos.
- o que ARIS não vai mostrar: exigência de OAuth real, integração viva, complexidade técnica.
- evidência gerada ou esperada: prova de que uma simulação sintética foi preparada.
- falha esperada: perfil insuficiente para simulação útil.
- timeout esperado: espera moderada para geração da prévia com texto de progresso.
- comportamento degradado: usar template padrão e reduzir personalização.
- critério de BLOCK: onboarding exigir dado real antes da primeira simulação.
- invariantes protegidas: isolamento, determinismo, autonomia.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Escolhe um playbook e informa o mínimo necessário | `BUSINESS_PROFILE_FORM` progressivo leva a `SIMULATION_PREVIEW` | Sistema compõe cenário sintético determinístico | Policy proíbe integração real e exige primeira simulação segura | Evidência de simulação preparada com parâmetros sintéticos | Falha cai em `ERROR_RECOVERY_PANEL`; timeout leva a template padrão | Ajustes de cópia e fluxo ficam em `local_repair`; qualquer necessidade de integrar runtime real vai para `Crisol` |

## FLOW_03_CREATE_AUTOMATION

- objetivo do cliente: configurar uma automação simples sem sobrecarga cognitiva.
- gatilho: escolha de template ou criação guiada.
- telas/componentes envolvidos: `ARIS_CLIENT_WORKSPACE`, `TEMPLATE_CARD`, `AUTOMATION_CARD`, `PERMISSION_SUMMARY`, `COST_TIME_ESTIMATE`.
- dados permitidos: template, objetivo, limites, frequência sintética.
- dados proibidos: schema bruto, DAG técnico, tokens, secrets.
- o que ARIS vai mostrar: objetivo, limites, risco, estimativa e permissões.
- o que ARIS não vai mostrar: editor técnico, runtime técnico, DDL.
- evidência gerada ou esperada: rascunho rastreável da automação proposta.
- falha esperada: conflito de configuração mínima ou permissão limitada.
- timeout esperado: cálculo de estimativa demora e cai para resumo.
- comportamento degradado: mostrar criação resumida com menos detalhe visual.
- critério de BLOCK: criação depender de jargão técnico ou revelar internals.
- invariantes protegidas: type-safety, governança, modularidade.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Monta uma automação simples a partir de um template | `AUTOMATION_CARD` e `PERMISSION_SUMMARY` deixam o escopo claro | Sistema estrutura proposta tipada e limitada | Policy reforça least privilege e antijargão | Rascunho e estimativa ficam vinculados ao fluxo de criação | Conflitos de permissão aparecem sem stack trace | Problemas de modelagem local ficam em `local_repair`; qualquer lacuna entre experiência e execução futura vai para `Crisol` |

## FLOW_04_SIMULATE_PREVIEW

- objetivo do cliente: ver o before/after antes de qualquer aprovação.
- gatilho: ação de simular na automação criada.
- telas/componentes envolvidos: `SIMULATION_PREVIEW`, `RISK_BADGE`, `COST_TIME_ESTIMATE`, `WILL_WILL_NOT_BLOCK`.
- dados permitidos: dados sintéticos, diff previsto, estimativa, risco.
- dados proibidos: mutação real, dado real, log técnico bruto.
- o que ARIS vai mostrar: resultado esperado, limites, o que vai fazer e o que não vai fazer.
- o que ARIS não vai mostrar: side effects reais, payload de produção.
- evidência gerada ou esperada: recibo de simulação com zero side effects.
- falha esperada: prévia incompleta ou parâmetros insuficientes.
- timeout esperado: simulação demora e mostra estado de espera honesto.
- comportamento degradado: resumo textual do impacto sem diff detalhado.
- critério de BLOCK: preview tocar estado real ou esconder incerteza.
- invariantes protegidas: determinismo, isolamento, regressão.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Pede para simular antes de decidir | `SIMULATION_PREVIEW` mostra before/after e `WILL_WILL_NOT_BLOCK` | Sistema calcula cenário sintético sem side effect | Policy exige `zero_side_effects_required` | Evidência de simulação marcada como não mutante | Timeout vira mensagem clara de limitação e retry seguro | Qualquer indício de tocar estado real é `BLOCK` e vai para `Crisol`; secrets ou produção iriam para `Bedrock` |

## FLOW_05_APPROVE_SENSITIVE_ACTION

- objetivo do cliente: aprovar uma ação sensível com contexto suficiente.
- gatilho: ação que exige confirmação explícita.
- telas/componentes envolvidos: `APPROVAL_CARD`, `WILL_WILL_NOT_BLOCK`, `RISK_BADGE`, `MOBILE_APPROVAL_SHEET`, `PERMISSION_SUMMARY`.
- dados permitidos: escopo da ação, risco, permissão, impacto, comprovante esperado.
- dados proibidos: aprovação por canal auxiliar, stack trace, segredo, ação inline em WhatsApp.
- o que ARIS vai mostrar: vai fazer, não vai fazer, risco por texto, permissão e impacto.
- o que ARIS não vai mostrar: confirmação genérica vazia, runtime internals, admin.
- evidência gerada ou esperada: recibo de aprovação com contexto e timestamp.
- falha esperada: contexto stale, permissão insuficiente, risco sem explicação.
- timeout esperado: expiração da decisão e necessidade de revalidar contexto.
- comportamento degradado: redirecionar do mobile para workspace quando faltarem detalhes.
- critério de BLOCK: aprovação sem `vai fazer / não vai fazer` ou fora do Workspace/Companion.
- invariantes protegidas: governança, sincronismo, rastreabilidade.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Revisa e aprova uma ação sensível | `APPROVAL_CARD` ou `MOBILE_APPROVAL_SHEET` exige confirmação explícita | Sistema valida contexto fresco e permissões antes de aceitar a decisão | Policy proíbe canais auxiliares como control-plane | Recibo de aprovação com risco, escopo e horário | Cache stale, expiração ou risco incompleto abortam aprovação | Problemas de UX/local copy ficam em `local_repair`; lacunas entre decisão e runtime futuro vão para `Crisol`; secrets/produção iriam para `Bedrock` |

## FLOW_06_EXECUTION_STATUS

- objetivo do cliente: saber se algo está rodando, pausado, parcial ou falhou.
- gatilho: consulta de status após aprovação ou automação ativa.
- telas/componentes envolvidos: `AUTOMATION_CARD`, `EXECUTION_TIMELINE`, `RISK_BADGE`, `DEGRADED_MODE_BANNER`, `TOAST_STATUS_MESSAGE`.
- dados permitidos: status sintético, última atualização, linha do tempo humanizada.
- dados proibidos: logs brutos, stack traces como conteúdo principal, internals de runtime.
- o que ARIS vai mostrar: estado legível, última atualização, próximos passos.
- o que ARIS não vai mostrar: terminal output, trace técnico.
- evidência gerada ou esperada: histórico legível do estado e mudanças visíveis.
- falha esperada: status parcial, dado atrasado, linha do tempo incompleta.
- timeout esperado: estado indeterminado acima do esperado vira explicação visível.
- comportamento degradado: banner informa limitação e mantém último estado confiável conhecido.
- critério de BLOCK: estado invisível ou falso sucesso.
- invariantes protegidas: rastreabilidade, resiliência, compressão de contexto.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Consulta o andamento da automação | `EXECUTION_TIMELINE` e `AUTOMATION_CARD` traduzem o estado | Sistema consolida mudanças em linguagem humana | Policy proíbe falso sucesso e estado invisível | Timeline e recibos associados tornam o estado auditável | Timeout vira estado parcial ou degradado explícito | Problemas de visibilidade local ficam em `local_repair`; gaps de acoplamento com runtime vão para `Crisol` |

## FLOW_07_EVIDENCE_RECEIPT

- objetivo do cliente: encontrar e confiar em um comprovante legível.
- gatilho: ação concluída, aprovação registrada ou simulação salva.
- telas/componentes envolvidos: `EVIDENCE_RECEIPT`, `EXECUTION_TIMELINE`, `TOAST_STATUS_MESSAGE`.
- dados permitidos: referência verificável, resumo da ação, data, escopo.
- dados proibidos: log técnico bruto, secret, hash cru como linguagem principal.
- o que ARIS vai mostrar: comprovante verificável, contexto e referência humana.
- o que ARIS não vai mostrar: dump técnico, stack trace, segredos.
- evidência gerada ou esperada: recibo verificável persistente.
- falha esperada: evidência indisponível ou ainda pendente.
- timeout esperado: atraso de persistência explicitado ao cliente.
- comportamento degradado: mostrar status pendente e instrução de rechecagem.
- critério de BLOCK: Evidence Receipt não pode virar log técnico.
- invariantes protegidas: rastreabilidade, governança, autoavaliação.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Abre um comprovante para confirmar o que aconteceu | `EVIDENCE_RECEIPT` mostra referência legível e verificável | Sistema liga recibo ao evento e ao contexto da ação | Policy exige prova legível ao cliente | Evidence Lane é o centro desse fluxo | Pendente ou indisponível gera explicação honesta | Lacunas de apresentação local ficam em `local_repair`; necessidades de auditoria real profunda vão para `Crisol` |

## FLOW_08_PAUSE_AUTOMATION

- objetivo do cliente: interromper temporariamente a automação com segurança.
- gatilho: intenção de pausar a execução futura.
- telas/componentes envolvidos: `AUTOMATION_CARD`, `MOBILE_APPROVAL_SHEET`, `TOAST_STATUS_MESSAGE`, `EXECUTION_TIMELINE`.
- dados permitidos: status atual, escopo da pausa, duração sugerida.
- dados proibidos: comandos técnicos, runtime internals, execução por canal auxiliar.
- o que ARIS vai mostrar: o que será pausado, o que continuará, como retomar.
- o que ARIS não vai mostrar: jargão de scheduler, internals de fila.
- evidência gerada ou esperada: recibo da pausa e atualização da timeline.
- falha esperada: pausa conflita com estado atual ou contexto stale.
- timeout esperado: confirmação não chega a tempo e a pausa precisa ser revalidada.
- comportamento degradado: manter última configuração conhecida e instruir retry seguro.
- critério de BLOCK: pausa ambígua ou execução fora da superfície oficial.
- invariantes protegidas: idempotência, sincronismo, autonomia.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Pausa a automação para recuperar controle | UI explica escopo da pausa antes de confirmar | Sistema registra intenção de pausa sem expor complexidade técnica | Policy exige superfícies oficiais e contexto fresco | Pausa gera evidência e atualização de histórico | Falha de confirmação ou timeout força revalidação | Problemas de fluxo ficam em `local_repair`; conflitos entre UX e comportamento futuro vão para `Crisol` |

## FLOW_09_ROLLBACK_OR_COMPENSATION

- objetivo do cliente: entender se pode desfazer, compensar ou apenas registrar limite.
- gatilho: necessidade de reverter uma ação ou reduzir impacto.
- telas/componentes envolvidos: `ROLLBACK_COMPENSATION_CARD`, `EVIDENCE_RECEIPT`, `FAILURE_EXPLANATION_CARD`, `WILL_WILL_NOT_BLOCK`.
- dados permitidos: tipo de reversão, limite, impacto, referência do efeito anterior.
- dados proibidos: promessa de desfazer irreversível, detalhes técnicos incompreensíveis.
- o que ARIS vai mostrar: pode desfazer, não pode desfazer, compensação disponível, impacto esperado.
- o que ARIS não vai mostrar: promessa falsa de reversão total, internals de compensação técnica.
- evidência gerada ou esperada: recibo de rollback ou de decisão de compensação.
- falha esperada: ação irreversível ou compensação indisponível.
- timeout esperado: avaliação do caminho de reversão leva a fallback explicativo.
- comportamento degradado: mostrar limite e encaminhar para decisão assistida.
- critério de BLOCK: Rollback não pode prometer desfazer side-effect irreversível.
- invariantes protegidas: idempotência, governança, rastreabilidade.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Procura desfazer ou compensar um efeito indesejado | `ROLLBACK_COMPENSATION_CARD` diferencia reversível, compensável e irreversível | Sistema classifica o tipo de retorno permitido | Policy proíbe prometer undo impossível | Evidência registra o caminho escolhido e seus limites | Irreversível vira explicação honesta com próximos passos | Ajustes de copy ficam em `local_repair`; qualquer dependência de side-effect real e compensação viva vai para `Crisol`; produção iria para `Bedrock` |

## FLOW_10_FAILURE_DEGRADED_MODE

- objetivo do cliente: entender a falha e continuar com segurança mínima.
- gatilho: erro crítico, serviço parcial ou indisponibilidade.
- telas/componentes envolvidos: `FAILURE_EXPLANATION_CARD`, `DEGRADED_MODE_BANNER`, `ERROR_RECOVERY_PANEL`, `TOAST_STATUS_MESSAGE`.
- dados permitidos: erro humanizado, impacto, próximos passos, funções ainda disponíveis.
- dados proibidos: stack trace, segredos, terminal output.
- o que ARIS vai mostrar: o que falhou, o que ainda funciona, o que fazer agora.
- o que ARIS não vai mostrar: stack trace, dump técnico, blame interno.
- evidência gerada ou esperada: marcação de falha e estado degradado com rastreio do evento.
- falha esperada: timeout de serviço, recuperação parcial, indisponibilidade de comprovante.
- timeout esperado: tempo máximo explícito antes de cair para recovery panel.
- comportamento degradado: manter rotas seguras, bloquear o que ficou inseguro e informar limites.
- critério de BLOCK: fluxo de falha sem próximo passo ou com exposição técnica.
- invariantes protegidas: resiliência, modularidade, roteamento.

| Cliente / Dono-Solo | Frontstage / UI | Backstage / Sistema | Support / Policy | Evidence Lane | Failure / Timeout | Boundary / Destination |
| --- | --- | --- | --- | --- | --- | --- |
| Enfrenta uma falha e precisa saber como seguir | `FAILURE_EXPLANATION_CARD` e `DEGRADED_MODE_BANNER` explicam limites | Sistema entra em modo degradado e desativa o que ficou inseguro | Policy proíbe stack trace e exige próximo passo claro | Falha e estado degradado ficam visíveis na evidence lane | Timeout fecha o ciclo para recovery panel e guidance seguro | Problemas de apresentação ficam em `local_repair`; qualquer gap entre experiência e runtime real vai para `Crisol`; secrets/produção/Bedrock vão para `Bedrock` |
