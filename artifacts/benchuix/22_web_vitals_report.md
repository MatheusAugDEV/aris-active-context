## referencia advisory

Esta fase usa `web.dev` apenas como referencia tecnica advisory para Web Vitals, sem substituir o active-context canonico e sem declarar medicao real.

## LCP / INP / CLS

- LCP mede quando o maior bloco de conteudo util aparece no viewport.
- INP mede a responsividade geral observando click, tap e teclado ao longo da visita inteira.
- CLS mede a instabilidade visual causada por deslocamentos inesperados de layout.

## p75 mobile

O recorte principal desta fase e `p75 mobile`. A referencia oficial usa o percentil 75 para classificar se a maioria das visitas atinge o alvo recomendado. Desktop entra apenas como comparacao secundaria e nunca como prova principal.

## field vs lab

- Field captura experiencia real de pessoas reais, dispositivos reais e redes reais.
- Lab ajuda a diagnosticar regressao antes de publicar, mas nao substitui a experiencia em campo.
- Claim futuro de performance precisa de raw data e segmentacao explicita.

## por que Lighthouse nao mede INP diretamente em simulacao

INP depende das interacoes reais que ocorrem durante a vida inteira da pagina. Em ambiente de laboratorio, ele nao costuma ser medido com fidelidade suficiente para substituir observacao em campo.

## TBT como proxy lab, nao substituto field

TBT e util como proxy de laboratorio para bloqueio de main thread e ajuda a diagnosticar interatividade ruim. Ainda assim, ele nao substitui INP real e nao pode sustentar claim final de responsividade.

## nenhum teste real foi executado

Este pacote nao executou browser real, Lighthouse real, Playwright, axe, coleta de field data ou runtime.

## orcamento candidato, nao performance provada

Os SLOs aqui registrados sao orcamentos e limites candidate-only. Eles definem o que uma futura prova real precisara medir, mas nao demonstram que o produto ja atinge esses valores.

## advisory sources

- `web.dev/articles/vitals`
- `web.dev/articles/vitals-measurement-getting-started`
- `web.dev/articles/defining-core-web-vitals-thresholds`
- `web.dev/articles/lcp`
- `web.dev/articles/inp`
- `web.dev/articles/cls`
- `web.dev/articles/fcp`
- `web.dev/articles/tbt`
