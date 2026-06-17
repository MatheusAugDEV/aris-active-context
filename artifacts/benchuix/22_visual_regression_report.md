## tese da fase

BENCHUIX-22 existe para impedir que a experiencia pareca boa apenas num screenshot isolado. O pacote define orcamento visual e de performance para mobile realista, com metodo futuro de medicao e cobertura de estados que importam para decisao segura.

## limites candidate-only

Esta fase nao executa browser real, Lighthouse, Playwright, axe, field data ou runtime. O resultado e apenas um contrato documental candidate-only para orcamento, cobertura visual e metodo futuro de medicao.

## estados visuais cobertos

- normal
- loading
- stale
- failure
- partial
- blocked
- empty
- degraded
- success
- low_risk
- medium_risk
- high_risk
- insufficient_permission
- receipt_available
- receipt_unavailable
- rollback_available
- rollback_unavailable

## temas cobertos

- tema claro como baseline obrigatorio
- tema escuro apenas se a superficie vier a declara-lo; se nao existir, nao conta como gap automatico
- reduced motion como variacao obrigatoria de cobertura

## viewport mobile realista

O recorte principal da fase e mobile narrow viewport. Desktop entra como referencia secundaria e nunca como prova principal de qualidade ou velocidade.

## relacao com BENCHUIX-21

BENCHUIX-21 deixou gaps nao criticos para contraste, reflow, target size, ordem relativa da ajuda e prova visual responsiva. BENCHUIX-22 consome esses gaps como matriz de resolucao ou carry-forward, sem fingir implementacao real.

## por que screenshot unico nao e prova

Um screenshot unico nao captura loading, stale data, degradacao, foco visivel, reduced motion, mudanca de risco, retorno de pausa, disponibilidade de comprovante ou variacoes de viewport. Ele prova apenas um instante, nao o comportamento.

## por que visual QA precisa cobrir estado e nao so aparencia

No ARIS, risco, permissao, falha, stale data, comprovante e rollback alteram a leitura operacional. Se a cobertura visual ignora estado, a tela pode parecer bonita e ainda assim induzir decisao errada.

## criterios PASS/WARN/BLOCK/INVALID

PASS: todos os estados minimos estao cobertos documentalmente, SLOs possuem metodo explicito, mobile p75 e a referencia principal e nenhum gap critico fica aberto.

WARN: existe carry-forward nao critico para BENCHUIX-23 ou Crisol, mas o orcamento e a cobertura minima continuam coerentes.

BLOCK: algum SLO fica sem metodo, algum estado visual critico fica sem cobertura ou a prova passa a depender de media desktop, screenshot unico ou score de PWA.

INVALID: qualquer claim de Core Web Vitals reais passando, browser real executado, Lighthouse real executado, field data coletado, rota viva aberta, lock real aberto ou Project_ARIS alterado.
