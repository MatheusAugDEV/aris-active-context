# BENCHUIX-10 Preview / Simulacao

## definição da fase

BENCHUIX-10 define um preview deterministico, synthetic-only e isolado para que o cliente veja o resultado esperado de uma automacao candidata antes de qualquer aprovacao.

## Exceção Bedrock-governed

Esta fase e uma excecao explicita de preparacao para Bedrock/Product Reality Lab. Ela nao produz Bedrock PASS, nao declara produto pronto e nao autoriza produto, piloto, runtime, integracao real, secrets, billing, OAuth real, producao ou real_apply.

## tese do preview/simulação

O cliente precisa entender o que aconteceria antes de aprovar. O preview deve traduzir impacto, diff, risco, custo e limites em linguagem humana sem tocar nada real.

## objetivo

- materializar um preview legivel antes de qualquer aprovacao;
- mostrar diff antes/depois em linguagem humana;
- estimar impacto, risco e custo de forma candidata;
- provar isolamento total da simulacao;
- preparar handoff para BENCHUIX-11.

## pergunta principal

"o cliente entende o que aconteceria antes de aprovar?"

## relação com BENCHUIX-09

BENCHUIX-09 estruturou a automacao candidata e o plano revisavel. BENCHUIX-10 recebe essa automacao candidata e a transforma em preview deterministico, sem tocar dado real, servico real, acao real ou estado real.

## fluxo do preview determinístico

1. A automacao candidata entra no modo preview.
2. O sistema gera um cenario sintetico controlado com entradas minimas e limites declarados.
3. O preview monta um antes/depois legivel, com impacto esperado e pontos de aprovacao.
4. O cliente revisa custo, risco, isolamento e comportamento degraded.
5. Se o preview nao for legivel ou parecer ambiguo, a fase bloqueia.

## diff antes/depois

O diff candidato mostra:

- como a situacao estava antes;
- o que mudaria no plano sugerido;
- quais itens ficariam apenas sinalizados;
- quais itens exigiriam confirmacao;
- o que continuaria sem alteracao.

O diff e textual, resumido e sem schema, hash, artifact, validator ou runtime na copy principal.

## estimativa de impacto

O preview deve indicar:

- alcance estimado da automacao candidata;
- quantidade de itens sinalizados ou priorizados;
- janelas de tempo afetadas;
- possiveis ganhos de foco, clareza ou evitacao de erro.

## estimativa de risco

O preview deve indicar:

- nivel candidato de risco;
- quais condicoes aumentam o risco;
- onde a aprovacao humana continua obrigatoria;
- quando a simulacao deve bloquear por incerteza ou sensibilidade.

## estimativa de custo

O preview deve indicar:

- custo relativo candidato em linguagem simples;
- quando a automacao parece leve, media ou custosa;
- quais fatores aumentam custo percebido;
- quando o cliente deve simplificar antes de seguir.

## prova de isolamento

Toda simulacao deve declarar que:

- usa apenas entradas sinteticas;
- nao le dado real;
- nao chama servico real;
- nao executa acao real;
- nao muta estado real;
- nao abre runtime.

## limites e timeouts

- preview deterministico apenas;
- tempo maximo candidato de 30 segundos para preview simples;
- tempo maximo candidato de 45 segundos para preview com diff mais amplo;
- fallback degraded quando faltar contexto sintetico suficiente;
- bloqueio imediato se o preview depender de dado, servico ou estado real.

## estados obrigatórios

- empty
- loading
- error
- success
- degraded

## microcopy candidata

- "Nada real sera alterado neste preview."
- "Vou te mostrar o que mudaria antes de qualquer aprovacao."
- "Se algo estiver ambiguo, eu vou bloquear e te pedir ajuste."
- "Este resultado e uma simulacao isolada."
- "Voce esta vendo impacto esperado, nao execucao real."

## acessibilidade

- resumo principal antes de detalhes;
- diff legivel por blocos curtos;
- hierarquia visual clara entre antes, depois, impacto e risco;
- feedback de loading em ate 300ms;
- erro com motivo e proximo passo objetivo;
- degraded com explicacao curta e limite seguro;
- nenhuma informacao critica dependente apenas de cor.

## critérios de BLOCK

- preview ilegivel para um dono-solo;
- diff sem clareza do antes/depois;
- risco sem explicacao;
- custo sem linguagem humana;
- ausencia de prova de isolamento;
- necessidade de dado real, servico real, acao real, mutacao de estado, secrets, producao ou real_apply;
- aprovacao sem preview legivel.

## anti-escopo

- nao tocar Project_ARIS;
- nao tocar dado real;
- nao chamar servico real;
- nao executar acao real;
- nao mutar estado real;
- nao criar UI executavel;
- nao criar app, PWA ou prototipo real;
- nao instalar dependencias;
- nao declarar produto pronto;
- nao declarar Bedrock PASS.

## handoff para BENCHUIX-11

BENCHUIX-11 deve usar este preview para definir como a Approval Inbox mostra risco, impacto, limites e decisao sem permitir aprovacao cega.
