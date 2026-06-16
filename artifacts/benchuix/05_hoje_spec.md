# BENCHUIX-05 Hoje Spec

## Definição da fase

BENCHUIX-05 define a primeira experiência do ARIS no Client Workspace. A tela “Hoje” é o ponto inicial do dono-solo e deve responder rapidamente: o que precisa da minha atenção, o que o ARIS já sabe, o que precisa da minha confirmação e qual é o próximo passo seguro.

## Tese

A tela Hoje é o oposto de um dashboard corporativo. Ela mostra pouca coisa, mas a coisa certa.

## Objetivo da tela Hoje

- orientar o dono-solo em até 5 segundos;
- mostrar pendências relevantes;
- mostrar aprovações necessárias;
- mostrar alertas e falhas sem pânico;
- mostrar comprovantes recentes quando útil;
- mostrar estado degradado quando houver limitação;
- evitar jargão técnico;
- evitar densidade corporativa;
- não executar nada.

## Navegação mínima do Modo A

- Hoje
- Automações
- Aprovar
- Histórico / Comprovantes
- Configurações

## Componentes permitidos nesta fase

- `APP_SHELL`
- `TOP_BAR`
- `SIDE_OR_BOTTOM_NAV`
- `TODAY_SUMMARY_CARD`
- `RISK_BADGE`
- `APPROVAL_CARD`
- `EVIDENCE_RECEIPT`
- `FAILURE_EXPLANATION_CARD`
- `DEGRADED_MODE_BANNER`
- `EMPTY_STATE`
- `LOADING_SKELETON`
- `TOAST_STATUS_MESSAGE`

## O que a tela deve mostrar

- saudação e contexto simples;
- resumo do dia;
- pendências de aprovação;
- alertas ou falhas relevantes;
- automações que precisam de atenção;
- comprovantes recentes ou link para histórico;
- próximo passo recomendado;
- estado degradado quando houver limitação;
- dados sintéticos em toda a primeira experiência.

## O que a tela não deve mostrar

- runtime;
- gate;
- schema;
- validator;
- artifact;
- ledger;
- tenant;
- idempotency;
- hash;
- oracle;
- CI;
- real_apply;
- active-context;
- stack trace;
- dado real;
- PSP real;
- admin;
- payload técnico;
- JSON;
- dashboard corporativo como primeira tela.

## Dados permitidos

- dados sintéticos;
- status sintético;
- aprovações sintéticas;
- alertas sintéticos;
- comprovantes sintéticos;
- métricas candidatas não reais.

## Dados proibidos

- cliente real;
- dado financeiro real;
- PSP real;
- secret;
- endpoint real;
- runtime real;
- produção.

## Estados obrigatórios

- `empty`
- `loading`
- `error`
- `success`
- `degraded`

## SLOs candidatos

- tela Hoje útil em até 2s;
- LCP candidato ≤ 2,5s p75 mobile;
- principal mensagem compreendida em até 5 segundos;
- feedback visual para carregamento em até 300ms;
- nenhum layout crítico pode depender de dado real.

## Linguagem e comportamento

- a mensagem principal precisa ser compreendida em até 5 segundos;
- alertas não podem soar como pânico quando houver alternativa segura;
- comprovantes recentes aparecem como prova útil, não como despejo técnico;
- estado degradado precisa explicar limitação e caminho seguro;
- nenhuma ação sensível é executada diretamente desta fase.

## Critérios de BLOCK

- a tela exige jargão técnico;
- informação crítica fica escondida;
- Hoje vira dashboard corporativo;
- primeiro estado exige dado real;
- estado de erro mostra stack trace;
- estado degradado não explica limitação;
- ação sensível é executada a partir da tela;
- admin aparece para cliente;
- real_apply, secrets, runtime ou produto aparecem no escopo.

## Anti-escopo

- não cria onboarding;
- não cria playbooks;
- não cria Automation Studio;
- não cria protótipo;
- não cria PWA;
- não cria React;
- não instala dependências;
- não toca runtime;
- não usa secrets;
- não ativa real_apply;
- não cria produto.

## Handoff

BENCHUIX-05 prepara:

- BENCHUIX-06 Onboarding;
- BENCHUIX-09 Automation Studio;
- BENCHUIX-11 Approval Inbox;
- BENCHUIX-14 Histórico / Comprovantes;
- BENCHUIX-16 Falhas / Modo Degradado.
