# BENCHUIX-24 Measurement Plan

## tese da fase

BENCHUIX-24 existe para transformar a tese de UX/UI do ARIS em um scorecard que responda a decisao de produto, nao a vaidade. O criterio central e simples: uma metrica so entra se puder mudar uma decisao concreta de produto ou de proxima fase.

## limites candidate-only

- Este pacote e candidate-only.
- Nao coleta dado real.
- Nao executa analytics real.
- Nao cria tracking real.
- Nao autoriza produto, Bedrock, runtime real, real_apply, secrets, billing, OAuth, integracoes reais ou customer data.
- Threshold candidate-only nao e prova de campo.

## como o scorecard sera usado

- Priorizar o que entra em BENCHUIX-25 como protocolo task-based.
- Distinguir metrica bloqueante de metrica apenas diagnostica.
- Forcar ligacao entre sinal observado e decisao de produto.
- Impedir que benchmark competitivo vire marketing.

## como nao sera usado

- Nao sera usado como prova de validacao em campo.
- Nao sera usado como score agregado de produto.
- Nao sera usado para promover engagement como valor por si.
- Nao sera usado para declarar ARIS pronto, validado, seguro ou superior ao mercado.

## diferenca entre sinal, metodo, threshold e decisao

- Sinal: o fenomeno observavel que importa para a tarefa.
- Metodo: como esse sinal sera medido de forma repetivel.
- Threshold: a fronteira candidate-only que aciona interpretacao inicial.
- Decisao: a mudanca de produto ou de fase que a metrica habilita.

Sem essa separacao, o scorecard degrada para numero solto ou teatro de dashboard.

## por que raw data e obrigatorio para claim futuro

Sem raw data:

- nao existe recontagem;
- nao existe segmentacao;
- nao existe auditoria de threshold;
- nao existe defesa contra cherry-picking;
- nao existe claim futuro confiavel.

Por contrato desta fase, qualquer claim futuro sem raw data e INVALID.

## como metricas conectam com BENCHUIX-23

BENCHUIX-23 mostrou onde o mercado ja tem fonte task-scoped e onde ARIS ainda depende de prova propria. BENCHUIX-24 converteu esses gaps em metricas ou manteve destinos explicitos:

- onboarding e create_automation viraram tempo para valor e tempo para automacao segura;
- dashboard e degraded mode viraram actionability e performance/clarity gates;
- mobile virou metrica de usabilidade movel sem aceitar tempo de tela;
- approval, risk e rollback viraram metricas de compreensao e confianca;
- preference vs competitor ficou diagnostica e sempre task-scoped.

## como metricas alimentam BENCHUIX-25

BENCHUIX-25 deve executar o protocolo task-based com base neste scorecard:

- cada tarefa precisa mapear para metricas obrigatorias;
- cada resposta precisa preservar raw data minima;
- thresholds calibraveis precisam justificar segmentacao futura;
- qualquer tarefa sem metodo observavel bloqueia claim posterior.

## criterios PASS/WARN/BLOCK/INVALID

- PASS: toda metrica tem sinal, metodo, threshold, artifact, raw data futura e decisao associada; vanity metric nao entra; engagement nao e valor por si; todo gap 23 tem metrica ou destino.
- WARN: threshold continua calibravel com justificativa, sample futuro, segmento e artifact de recalibracao definidos.
- BLOCK: qualquer metrica sem metodo, sem threshold, sem artifact ou sem decisao; raw data contract ausente; engagement tratado como valor por si.
- INVALID: live route aberta, Project_ARIS alterado, dado real coletado, analytics real executado, claim de produto feito, metricas de vaidade usadas como prova.
