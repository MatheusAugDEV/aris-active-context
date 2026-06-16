# BENCHUIX-09 Automation Studio Simples

## definição da fase

BENCHUIX-09 define o Automation Studio Simples como editor candidato para criar automacoes por linguagem natural, revisar um plano compreensivel e permitir pausar, duplicar e editar sem expor complexidade tecnica ao cliente.

## Exceção Bedrock-governed

Esta fase e uma excecao explicita de preparacao para Bedrock/Product Reality Lab. Ela nao produz Bedrock PASS, nao declara produto pronto e nao autoriza produto, piloto, runtime, integracao real, secrets, billing, OAuth real, producao ou real_apply.

## tese do Automation Studio Simples

O cliente deve sentir que esta montando um fluxo seguro com orientacao clara, e nao programando um sistema. O rigor interno precisa aparecer como limites, revisao e confirmacao, nunca como superficie tecnica.

## objetivo

- transformar playbooks sinteticos em ponto de partida editavel;
- permitir criacao por linguagem natural sem abrir execucao real;
- mostrar proposta type-safe em linguagem humana;
- exigir revisao do plano antes de qualquer aprovacao;
- preparar handoff para BENCHUIX-10.

## pergunta principal

"o cliente consegue criar uma automação segura sem ver complexidade técnica?"

## relação com BENCHUIX-08

BENCHUIX-08 organizou os playbooks por vertical. BENCHUIX-09 usa esses playbooks como ponto de partida para criar ou ajustar uma automacao candidata sem expor DAG, schema ou runtime ao cliente.

## fluxo de criação por linguagem natural

1. O cliente descreve o objetivo em linguagem simples.
2. ARIS sugere um ponto de partida baseado no playbook da vertical ou em um fluxo vazio seguro.
3. O sistema devolve um plano resumido com gatilhos, condicoes, aprovacoes e limites em linguagem humana.
4. O cliente revisa, pausa, duplica ou edita a proposta.
5. Se houver ambiguidade ou risco sensivel, ARIS pede esclarecimento antes de seguir.

## proposta type-safe em linguagem humana

A proposta precisa ser internamente rigorosa, mas visivelmente simples. O cliente ve:

- quando a automacao pode comecar;
- o que ela vai observar;
- o que ela vai sugerir;
- o que precisa de confirmacao;
- o que nunca sera feito automaticamente nesta fase.

O cliente nao ve estrutura de DAG, schema, validator, artifact ou detalhes de runtime.

## revisão de plano

Antes de qualquer aprovacao, o plano mostra:

- objetivo resumido;
- gatilho principal;
- condicoes de seguranca;
- limites de volume e horario;
- pontos que pedem confirmacao;
- will statement;
- will-not statement;
- comportamento degraded.

## ações permitidas

As unicas acoes candidatas nesta fase sao:

- pausar;
- duplicar;
- editar.

Essas acoes reorganizam a proposta candidata e nao executam runtime real.

## ambiguidades

Quando a intencao do cliente for vaga, conflituosa ou sensivel, ARIS deve:

- pedir uma clarificacao curta;
- oferecer duas ou tres interpretacoes seguras;
- bloquear qualquer caminho que pareca acao sensivel sem aprovacao;
- preservar o rascunho anterior para evitar perda de contexto.

## will / will-not statements

- Will: ARIS vai transformar o pedido em um plano simples, revisar limites e destacar onde sua confirmacao sera necessaria.
- Will not: ARIS nao vai criar automacao real, conectar canais reais, disparar mensagens, alterar producao ou executar integracao.

## limites e validações

- sem automacao real;
- sem visual node editor;
- sem exposicao de DAG tecnico, schema ou runtime;
- sem billing, OAuth real, secrets, integracao real ou dado real de cliente;
- aprovacao obrigatoria para qualquer acao sensivel;
- linguagem curta, sem jargao tecnico na copia principal;
- fallback degraded com proximo passo seguro.

## estados obrigatórios

- empty
- loading
- error
- success
- degraded

## microcopy candidata

- "Descreva o que voce quer automatizar e eu monto um rascunho seguro."
- "Vou te mostrar o plano antes de qualquer confirmacao."
- "Se faltar contexto, eu vou te pedir so o minimo."
- "Nada real sera executado agora."
- "Voce pode pausar, duplicar ou editar este rascunho."

## acessibilidade

- uma tarefa principal por bloco;
- titulos curtos e orientados a acao;
- foco visivel e ordem consistente de navegacao;
- feedback de loading em ate 300ms;
- mensagem de erro com proximo passo objetivo;
- estado degraded com limite claro e continuidade segura;
- texto legivel sem dependencia de cor para decisao.

## critérios de BLOCK

- necessidade de automacao real para provar valor;
- exigencia de visual node editor para entendimento basico;
- plano que nao deixa claro o que sera aprovado;
- exposicao de DAG tecnico, schema, validator, artifact, ledger, hash ou runtime para explicar o fluxo;
- acao sensivel sem aprovacao;
- qualquer dependencia de billing, OAuth real, integracao real, secrets, producao ou real_apply.

## anti-escopo

- nao criar UI executavel;
- nao criar app, PWA ou prototipo real;
- nao tocar Project_ARIS;
- nao instalar dependencias;
- nao abrir runtime;
- nao criar integracao real;
- nao declarar produto pronto;
- nao declarar Bedrock PASS.

## handoff para BENCHUIX-10

BENCHUIX-10 deve usar este editor candidato para definir como aprovacoes, comprovantes e estados de revisao aparecem na experiencia sem abrir automacao real.
