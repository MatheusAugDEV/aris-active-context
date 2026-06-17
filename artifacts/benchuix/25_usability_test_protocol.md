# BENCHUIX-25 Usability Test Protocol

## tese da fase

Esta fase define um protocolo task-based para verificar, em ambiente futuro e ainda nao executado, se perfis realistas conseguem completar tarefas criticas do ARIS sem explicacao tecnica e sem depender de narrativa do facilitador.

Pergunta central: o dono-solo executa tarefas criticas sem explicacao tecnica?

## limites candidate-only

- Candidate-only e artifact-only.
- Nenhuma sessao real e executada nesta fase.
- Nenhum usuario real e recrutado nesta fase.
- Nenhum dado real, PII, audio, video, tela ou telemetria real pode ser coletado.
- `Project_ARIS` permanece intocado.
- `phase_id/current_phase_id` vivo permanece `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET`.
- `next_phase=null` e `active_next_phase=null` permanecem intactos.

## perfis simulados/futuros

- `barbearia_owner_solo`: dono que opera agenda, pagamentos e equipe curta no celular.
- `loja_owner_operator`: dono-operador que alterna desktop no caixa e celular no estoque.
- `mercado_small_team`: pequena equipe que depende de aprovacao curta e visibilidade de falhas.
- `escritorio_admin`: administrativo que precisa prova, historico e baixa ambiguidade.
- `agencia_operator`: operador com varias contas e risco de contexto cruzado.
- `automation_anxious_user`: perfil com medo de automacao aprovar algo errado.
- `mobile_4g_user`: usuario em contexto curto, rede limitada e tela pequena.

## tarefas criticas

- Entender Hoje.
- Criar automacao.
- Simular antes de agir.
- Aprovar com entendimento de risco.
- Achar comprovante.
- Entender falha.
- Pausar automacao.
- Entender o que ARIS nao fara.
- Ver se pode desfazer.
- Explicar ARIS para outra pessoa.

## ambiente esperado

- Workspace sintetico, sem runtime real.
- Dados sinteticos por vertical, sem PII.
- Facilitar em desktop e mobile 4G.
- O facilitador so le o cenario e registra observacao.
- Nenhum rastro desta fase pode ser tratado como validacao em campo.

## instrucoes do facilitador

- Ler o cenario exatamente como escrito.
- Nao explicar arquitetura, regra interna, permissao ou onde clicar.
- Se o participante pedir ajuda, repetir a meta da tarefa no maximo uma vez.
- Registrar comportamentos observaveis antes de registrar interpretacao.
- Encerrar a tarefa quando houver sucesso claro, abandono ou risco inseguro.

## regras anti-leading

- Nao usar perguntas do tipo "voce entendeu?" como evidencia principal.
- Nao sugerir caminho, componente, tela, ordem ou CTA.
- Nao validar resposta parcial com reforco positivo.
- Nao converter hesitacao em "normal" sem evidencia.
- Nao reformular risco de maneira mais simples que a propria interface.

## protocolo think-aloud

- Think-aloud e convite, nao obrigacao.
- Registrar trechos curtos ligados ao momento observavel da tarefa.
- Fala nao substitui comportamento.
- Quando fala e comportamento divergirem, o comportamento observavel prevalece.
- O facilitador nao deve pedir justificativa tecnica longa durante a execucao.

## o que observar

- Tempo de inicio ao fim.
- Primeira direcao tomada e desvios.
- Hesitacoes, releituras e voltas.
- Pedido de ajuda.
- Interpretacao de risco, will/will-not e limites.
- Encontrabilidade de comprovante, falha, pausa e rollback.
- Capacidade de explicar o ARIS sem jargao tecnico.

## o que registrar

- Resultado da tarefa segundo a taxonomia fixa.
- `wrong_turn_count`.
- Marcadores de hesitacao.
- Se houve risco de aprovacao insegura.
- Se recibo, falha, pausa e rollback foram compreendidos.
- Trecho curto de explain-back do participante.
- Notas do observador com evidencia concreta.

## como tratar hesitacao, erro, abandono e pedido de ajuda

- Hesitacao relevante vira evidencia quando houver releitura, pausa prolongada, retorno ou verbalizacao de duvida.
- Erro conta quando o participante entra em caminho que nao avanca a meta da tarefa.
- Abandono conta quando o participante para, pede para encerrar ou diz que nao faria sem ajuda externa.
- Pedido de ajuda conta mesmo se a tarefa terminar depois.
- Sucesso com risco inseguro nunca vira sucesso completo.

## como mapear observacao para severidade

- `CRITICAL`: aprovacao insegura, impossibilidade de concluir tarefa essencial, ou entendimento invertido de will/will-not.
- `HIGH`: conclusao so com ajuda substancial, ou entendimento incompleto de risco, rollback ou comprovante.
- `MEDIUM`: conclusao com hesitacao relevante, releitura repetida ou retrabalho.
- `LOW`: atrito pequeno, linguagem ajustavel, sem risco de decisao errada.

## placeholders futuros de consentimento e privacidade

- Consentimento futuro: se a fase for autorizada mais adiante, o protocolo devera usar termo separado, escopo de captura explicito e opt-out.
- Privacidade futura: qualquer coleta autorizada depois deve continuar sem PII por padrao, com retencao curta e vinculada a tarefa.
- Nesta fase esses itens sao placeholders documentais e nao autorizam coleta real.

## como o protocolo alimenta BENCHUIX-26

- Exporta matriz de sucesso por tarefa.
- Exporta rubrica de severidade por achado.
- Exporta schema de observacao e raw data futuro.
- Exporta mapeamento de tarefas para metricas de `BENCHUIX-24`.
- Entrega backlog objetivo para sintese de findings e priorizacao em `BENCHUIX-26`.

## criterios PASS/WARN/BLOCK/INVALID

- PASS: protocolo executavel definido, 10 tarefas criticas cobertas, perfis e dados sinteticos definidos, metricas de `BENCHUIX-24` mapeadas, locks reais preservados, validator e unittest passam.
- WARN: alguma tarefa ou perfil depende de refinamento futuro, mas tem destino explicito em `BENCHUIX-26` e nao quebra o protocolo.
- BLOCK: faltar tarefa critica, rubrica de severidade sem destino, dados sinteticos insuficientes ou metrica de `BENCHUIX-24` sem mapeamento/destino.
- INVALID: abrir rota viva, tocar `Project_ARIS`, executar sessao real, usar dado real/PII ou declarar usabilidade validada.
