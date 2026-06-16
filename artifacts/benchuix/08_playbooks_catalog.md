# BENCHUIX-08 Playbooks Catalog

## definição da fase

BENCHUIX-08 define playbooks sintéticos por vertical para que o cliente comece com atalhos úteis, seguros e compreensíveis, sem partir do zero e sem abrir automação real.

## Exceção Bedrock-governed

Esta fase é uma exceção explícita de preparação para Bedrock/Product Reality Lab. Ela não produz Bedrock PASS, não declara produto pronto e não autoriza produto, piloto, runtime, integração real, secrets, billing, OAuth real, produção ou real_apply.

## tese dos playbooks por vertical

O cliente deve receber caminhos iniciais que façam sentido para o seu tipo de negócio. O valor vem de atalhos úteis com limites claros, não de automação ampla logo no primeiro contato.

## objetivo

- reduzir o esforço de começar do zero;
- oferecer templates sintéticos de baixo risco;
- deixar claro o que ARIS vai fazer e o que não vai fazer;
- exigir aprovação para qualquer ação sensível;
- preparar handoff para BENCHUIX-09.

## pergunta principal

"o cliente começa com atalhos úteis ou do zero?"

## relação com BENCHUIX-07

BENCHUIX-07 estruturou o perfil mínimo do negócio. BENCHUIX-08 usa esse contexto para sugerir playbooks iniciais por vertical sem repetir cadastro e sem abrir integração real.

## verticais cobertas

- barbearia
- loja
- mercado
- escritorio
- agencia
- clinica_servico

## templates por vertical

### barbearia

#### Template: Agenda do Dia Prioritaria

- nome: Agenda do Dia Prioritaria
- objetivo: organizar a ordem de atendimento do dia em linguagem simples.
- quando usar: quando o dono quer visualizar encaixes, atrasos e blocos mais cheios.
- dados sintéticos mínimos: agenda sintetica do dia, duracao media por servico, blocos de horario.
- will statement: ARIS vai sugerir uma ordem simples para o dia e destacar conflitos visiveis.
- will-not statement: ARIS não vai confirmar cliente, mover agenda real ou disparar mensagem real.
- limites: no maximo 20 blocos sinteticos e 3 conflitos destacados.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas os tres horarios mais pressionados e orienta revisão manual.
- critério de bloqueio: exigir agenda real ou acionar contato real.

#### Template: Reconfirmacao de Horarios Sensiveis

- nome: Reconfirmacao de Horarios Sensiveis
- objetivo: identificar atendimentos sensiveis que pediriam reconfirmacao antes do horario.
- quando usar: quando faltas e atrasos pesam no caixa do dia.
- dados sintéticos mínimos: blocos de maior risco, janela de aviso sintetica, tipo de servico.
- will statement: ARIS vai sugerir quais horarios merecem reconfirmacao.
- will-not statement: ARIS não vai enviar mensagem real nem alterar agenda automaticamente.
- limites: no maximo 5 avisos sugeridos por rodada.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: mostra uma lista curta de horarios com maior risco e pede revisao manual.
- critério de bloqueio: permitir envio sem aprovação.

### loja

#### Template: Reposicao de Vitrine

- nome: Reposicao de Vitrine
- objetivo: sugerir o que merece voltar para a vitrine primeiro.
- quando usar: quando o dono quer priorizar itens que sumiram da frente de loja.
- dados sintéticos mínimos: categorias sinteticas, volume em vitrine, giro relativo sintetico.
- will statement: ARIS vai ordenar categorias por prioridade de reposicao.
- will-not statement: ARIS não vai baixar estoque real, emitir pedido ou falar com fornecedor.
- limites: no maximo 10 categorias e 3 prioridades criticas.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas as tres categorias mais impactadas.
- critério de bloqueio: depender de estoque real ou pedido real.

#### Template: Alerta de Ruptura Sensivel

- nome: Alerta de Ruptura Sensivel
- objetivo: sinalizar itens que merecem atenção antes de ruptura percebida.
- quando usar: quando alguns itens puxam venda e não podem sumir da vitrine.
- dados sintéticos mínimos: itens sinteticos criticos, faixa de demanda, janela de reposicao.
- will statement: ARIS vai destacar risco de ruptura e sugerir revisão.
- will-not statement: ARIS não vai comprar, reservar ou alterar inventario real.
- limites: no maximo 8 itens sensiveis por rodada.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: resume dois itens mais criticos e um proximo passo manual.
- critério de bloqueio: acionar compra ou reserva sem aprovação.

### mercado

#### Template: Pico de Corredor

- nome: Pico de Corredor
- objetivo: mostrar corredores sinteticos com maior pressao em horarios de pico.
- quando usar: quando o dono quer distribuir atenção da equipe em horarios cheios.
- dados sintéticos mínimos: fluxo sintetico por corredor, janela de pico, categorias de maior giro.
- will statement: ARIS vai sugerir foco operacional por corredor.
- will-not statement: ARIS não vai acionar equipe real nem alterar escala.
- limites: no maximo 6 corredores e 2 janelas de pico.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas o corredor mais pressionado e um lembrete simples.
- critério de bloqueio: depender de escala real ou monitoramento em tempo real.

#### Template: Pereciveis em Atenção

- nome: Pereciveis em Atenção
- objetivo: apontar lotes sinteticos que merecem revisão antes de perda.
- quando usar: quando o negocio quer evitar descarte alto em itens sensiveis.
- dados sintéticos mínimos: categoria perecivel sintetica, janela de validade simulada, faixa de giro.
- will statement: ARIS vai listar itens que pedem revisão prioritaria.
- will-not statement: ARIS não vai descartar, remarcar preço real ou alterar inventario real.
- limites: no maximo 12 itens e 3 alertas criticos.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: mostra so os tres itens com janela mais curta.
- critério de bloqueio: permitir ajuste real sem aprovação.

### escritorio

#### Template: Fila de Pendencias

- nome: Fila de Pendencias
- objetivo: priorizar pendencias administrativas do dia.
- quando usar: quando ha varias tarefas pequenas e pouca clareza do que vem primeiro.
- dados sintéticos mínimos: lista sintetica de pendencias, prazo relativo, impacto estimado.
- will statement: ARIS vai ordenar a fila por urgencia e impacto percebido.
- will-not statement: ARIS não vai enviar documento real, protocolar pedido real ou editar sistema externo.
- limites: no maximo 15 pendencias e 3 destaques.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas o topo da fila e uma justificativa curta.
- critério de bloqueio: depender de documento real ou sistema externo.

#### Template: Revisao Antes de Enviar

- nome: Revisao Antes de Enviar
- objetivo: marcar itens que precisam dupla checagem antes de qualquer envio.
- quando usar: quando erro de documento custa retrabalho ou confiança.
- dados sintéticos mínimos: tipo de entrega, prazo, nivel de sensibilidade, checklist sintetico.
- will statement: ARIS vai indicar o que merece revisão reforçada.
- will-not statement: ARIS não vai enviar e-mail real, protocolo real ou arquivo real.
- limites: no maximo 10 itens sinalizados por ciclo.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: reduz para uma checklist curta por item.
- critério de bloqueio: permitir envio sem aprovação.

### agencia

#### Template: Campanhas da Semana

- nome: Campanhas da Semana
- objetivo: resumir campanhas sinteticas que pedem atenção nesta semana.
- quando usar: quando o time quer um ponto de partida para revisar prioridades.
- dados sintéticos mínimos: campanhas sinteticas, objetivo principal, status estimado, janela da semana.
- will statement: ARIS vai destacar campanhas que merecem foco primeiro.
- will-not statement: ARIS não vai publicar, impulsionar ou alterar canal real.
- limites: no maximo 8 campanhas e 3 prioridades.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas as duas campanhas mais urgentes.
- critério de bloqueio: acionar publicacao real.

#### Template: Aprovar Conteudo Sensivel

- nome: Aprovar Conteudo Sensivel
- objetivo: sinalizar pecas ou mensagens que exigem revisão antes de qualquer uso.
- quando usar: quando ha ofertas, temas delicados ou claims que podem gerar risco.
- dados sintéticos mínimos: tipo de conteudo, claim principal, urgencia, publico sintetico.
- will statement: ARIS vai marcar conteudos que precisam do seu ok.
- will-not statement: ARIS não vai publicar, enviar ou editar peça real automaticamente.
- limites: no maximo 6 itens sensiveis por rodada.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: entrega lista curta de itens sensiveis com motivo principal.
- critério de bloqueio: permitir publicacao sem aprovação.

### clinica_servico

#### Template: Confirmacoes do Turno

- nome: Confirmacoes do Turno
- objetivo: sugerir confirmacoes sinteticas para horarios mais sensiveis do turno.
- quando usar: quando atrasos e faltas afetam a operacao diaria.
- dados sintéticos mínimos: agenda sintetica do turno, tipo de atendimento, janela de antecedencia.
- will statement: ARIS vai sugerir quais horarios merecem confirmação.
- will-not statement: ARIS não vai enviar mensagem real, alterar prontuario ou mover agenda real.
- limites: no maximo 6 confirmacoes sugeridas por turno.
- timeout: 45 segundos.
- risco inicial: medio.
- aprovação exigida ou não: sim.
- comportamento degraded: mostra apenas os tres horarios de maior risco.
- critério de bloqueio: tocar dado clinico real ou enviar sem aprovação.

#### Template: Sala e Fluxo do Dia

- nome: Sala e Fluxo do Dia
- objetivo: organizar fluxo sintetico entre salas e janelas do dia.
- quando usar: quando a equipe precisa enxergar gargalos de atendimento.
- dados sintéticos mínimos: salas sinteticas, duracao media, janelas de espera, tipo de atendimento.
- will statement: ARIS vai sugerir uma ordem simples de fluxo do dia.
- will-not statement: ARIS não vai alterar agenda real, prontuario ou chamada de paciente real.
- limites: no maximo 10 janelas sinteticas e 3 gargalos destacados.
- timeout: 30 segundos.
- risco inicial: baixo.
- aprovação exigida ou não: não.
- comportamento degraded: mostra apenas a sala mais pressionada e o horario sensivel.
- critério de bloqueio: depender de agenda real ou prontuario.

## anti-escopo

- não cria automação real;
- não cria integração real;
- não publica em canal real;
- não envia mensagem real;
- não toca Project_ARIS;
- não usa billing;
- não usa OAuth real;
- não usa secrets;
- não abre runtime, produção, produto ou real_apply.

## handoff para BENCHUIX-09

BENCHUIX-08 entrega playbooks sintéticos, limites e linguagem will/will-not para que BENCHUIX-09 estruture um studio simples sem expor DAG técnico nem permitir execução real.
