# BENCHUIX-00 Charter

## Definicao

BenchUIX e a trilha governada da camada BenchUIX para validar Product Reality Lab, UX/UI, benchmark, design system, performance, trust UX e demo readiness em modo pre-produto.

Esta camada existe apos Infernus Revalidation e antes de Crisol.

## Tese

Simples por fora, rigoroso por dentro.

Para o cliente, ARIS deve responder com clareza:

- o que vai acontecer;
- o que nao vai acontecer;
- qual risco existe;
- se precisa de confirmacao;
- o que foi feito;
- se existe comprovante;
- se da para desfazer.

Para o sistema, ARIS continua exigindo:

- permissoes;
- limites;
- evidencia;
- rollback;
- retry;
- custo;
- latencia;
- rastreabilidade;
- idempotencia;
- estado seguro;
- bloqueio quando necessario.

## Escopo Permitido

- charter da camada;
- anti-escopo absoluto;
- transition table BENCHUIX-00 ate BENCHUIX-27 com handoff para CRISOL;
- source ledger inicial de referencias estruturais;
- admission packet artifact-only;
- prova documental de que produto, runtime real e Bedrock continuam bloqueados.

## Anti-Escopo Absoluto

- produto real;
- piloto;
- Bedrock;
- real_apply;
- runtime real;
- secrets;
- cliente real;
- PSP real;
- deploy de producao;
- PWA implementada;
- React/prototipo funcional;
- alteracao de codigo de produto;
- integracao real;
- scanner, pentest, DAST ou rede externa fora de GitHub governance.

## Regras Fixas

- PROPOSER != GATE.
- Nenhum modelo declara PASS.
- PASS so existe com artifact no disco, hash, validator pass e CI terminal green.
- Produto e somente pos-Bedrock.
- Esta camada nao autoriza produto real.
- UI e mecanismo de controle, nao decoracao.
- Toda acao sensivel deve explicitar will / will-not.
- Se a UI mostra, o sistema prova. Se o sistema faz, a UI mostra.

## Relacao Com Camadas Futuras

- Crisol recebe os gaps que cruzam experiencia, consolidacao e runtime futuro.
- Cinzel permanece posterior e fora do escopo desta abertura.
- EXT-SEC 00-04 e EXT-SEC 05-06 permanecem posteriores e nao sao ativados aqui.
- Bedrock continua sendo gate maximo de decisao e nao e autorizado nesta camada.

## Gates Absolutos Pre-Bedrock

Qualquer item abaixo aberto bloqueia handoff futuro para Bedrock:

1. Tela Hoje sem dado operacional.
2. Aprovacao sem vai fazer / nao vai fazer.
3. Recibo sem verificabilidade e sem linguagem de cliente.
4. Rollback sem limite e impacto.
5. UI com jargao tecnico.
6. Core Web Vitals ausentes ou estourados no p75 mobile.
7. Falha de rede sem modo degradado.
8. Onboarding sem primeira simulacao segura em 3-5 minutos.
9. Preview tocando estado real.
10. Demo que exige explicacao arquitetural.
11. Benchmark sem tarefa real.
12. Metrica sem raw data.
13. Acao sensivel sem confirmacao explicita.
14. Admin interno acessivel ao cliente.
15. Aprovacao renderizada de cache obsoleto.

## Anti-Theater Rules

### INVALID

- benchmark sem tarefa real;
- UX sem dono-solo;
- UI bonita sem fluxo completo;
- design system sem estados de erro, falha e degraded;
- performance sem medicao mobile;
- Core Web Vitals ausentes;
- metrica sem raw data;
- SLO sem metodo de medicao;
- PASS sem artifact, hash e CI;
- persona sem fonte;
- componente fora do design system.

### BLOCK

- seguranca que depende de jargao;
- aprovacao sem vai fazer / nao vai fazer;
- evidencia que so engenheiro entende;
- rollback sem explicar limites;
- demo que exige arquitetura;
- preview que toca estado real;
- secret ou log tecnico em tela do cliente;
- rollback com reexecucao duplicavel;
- real_apply dentro da camada;
- produto real antes de Bedrock.

### WARN

- concorrente citado com fonte fraca;
- alert fatigue;
- formulario longo sem teste de abandono;
- KPI sem baseline;
- risco mostrado so por cor;
- token sem nome semantico.

## Estado Desta Fase

- artifact-only;
- no-real-exec;
- pre-produto;
- ready for operator review somente apos validacoes, commit, push e CI terminal.
