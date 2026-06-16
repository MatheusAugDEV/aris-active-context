# BENCHUIX-06 Onboarding Spec

## definição da fase

BENCHUIX-06 define o onboarding curto do dono-solo para chegar ao primeiro preview seguro em até 3 minutos, sem cadastro longo, sem billing, sem OAuth real, sem integração real e sem dado real.

## Exceção Bedrock-governed

Esta fase é uma exceção explícita de preparação para Bedrock/Product Reality Lab. Ela não produz Bedrock PASS, não declara produto pronto e não autoriza produto, piloto, runtime, integração real, secrets, billing, OAuth real, produção ou real_apply.

## tese do onboarding curto

O onboarding precisa reduzir fricção antes de aumentar configuração. O cliente deve ver valor sintético primeiro e profundidade depois.

## Objetivo

- levar o dono-solo ao primeiro preview seguro em até 3 minutos;
- evitar cadastro longo;
- eliminar campos repetidos;
- explicar o caminho com linguagem simples;
- manter tudo synthetic-only;
- preparar handoff para BENCHUIX-07.

## Pergunta principal

"o cliente chega ao primeiro valor sem cadastro longo?"

## Fluxo mínimo em até 3 minutos

1. escolher tipo de negócio;
2. declarar objetivo principal;
3. marcar canais usados;
4. escolher template inicial;
5. ver primeiro preview ou simulação segura.

## Campos permitidos

- tipo de negócio;
- objetivo principal;
- canais usados;
- volume aproximado em termos sintéticos;
- horário de operação em faixas simples;
- template preferido;
- contexto opcional curto em linguagem natural.

## Campos proibidos

- billing;
- cartão real;
- dado financeiro real;
- OAuth real;
- credencial real;
- secret;
- integração real;
- endpoint real;
- dado real de cliente;
- cadastro corporativo extenso;
- qualquer campo repetido.

## Progressive disclosure

- primeiro passo só pede o mínimo necessário para orientar;
- detalhes avançados ficam para depois do primeiro preview;
- informação opcional não pode bloquear o avanço;
- o sistema não repete pergunta já respondida.

## dados sintéticos obrigatórios

- exemplos de negócio sintéticos;
- templates sintéticos;
- métricas sintéticas;
- preview sintético;
- alertas e limites sintéticos;
- nenhum dado real para primeiro valor.

## estados obrigatórios

- `empty`
- `loading`
- `error`
- `success`
- `degraded`

## microcopy candidata

- "Comece pelo essencial."
- "Você verá um preview antes de qualquer confirmação."
- "Nada real será alterado agora."
- "Escolha um caminho simples para começar."
- "Se faltar contexto, você poderá completar depois."
- "Seu primeiro preview precisa chegar rápido, não perfeito."

## acessibilidade

- passos curtos com títulos claros;
- foco visível;
- labels legíveis e sem ambiguidade;
- progresso anunciado para leitores de tela;
- alvos de toque confortáveis;
- erro com orientação objetiva;
- loading com feedback em até 300ms;
- degraded com limitação e próximo passo.

## SLOs candidatos

- primeiro preview em até 180 segundos;
- nenhum campo repetido;
- feedback visual de carregamento em até 300ms;
- mensagem principal compreendida em até 5 segundos por etapa;
- abandono evitado por fluxo curto e progressivo.

## critérios de BLOCK

- onboarding exigir cadastro longo;
- billing aparecer antes do primeiro preview;
- OAuth real aparecer no fluxo;
- integração real ser necessária;
- dado real ser exigido;
- preview não ser sintético;
- campo repetido reaparecer;
- copy usar jargão técnico primário;
- fluxo virar onboarding corporativo;
- qualquer lock real abrir.

## anti-escopo

- não cria UI executável;
- não cria PWA;
- não cria React;
- não instala dependências;
- não toca Project_ARIS;
- não toca runtime;
- não usa secrets;
- não ativa real_apply;
- não cria produto;
- não integra serviços reais.

## Handoff

BENCHUIX-06 prepara BENCHUIX-07 com contexto mínimo de negócio, escolhas iniciais e primeiro preview sintético sem repetir respostas já dadas.
