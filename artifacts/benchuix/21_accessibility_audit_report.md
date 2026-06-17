## tese da fase

BENCHUIX-21 existe para impedir que o ARIS pareca claro apenas para quem usa mouse, tela grande e leitura visual. O pacote define o comportamento minimo esperado para teclado, mobile, leitor de tela, foco visivel, status anunciavel e reduced motion nos fluxos criticos.

## limites da auditoria documental

Esta fase nao executa browser real, leitor de tela real, axe, Lighthouse ou teste runtime. Ela registra mapeamento candidate-only, cobranca documental e destino de gaps para validacao futura.

## escopo synthetic-only

O pacote vale apenas como auditoria documental synthetic-only. Nao declara conformidade real WCAG 2.2 AA, nao declara produto acessivel e nao abre rota viva.

## fluxos criticos avaliados

- Hoje
- Aprovar
- Negar
- Ver risco
- Ver permissao
- Ver comprovante
- Ver rollback/desfazer/compensar
- Pausar automacao
- Ver falha
- Ver dado atrasado
- Abrir ajuda contextual

## achados por teclado

- Todos os fluxos essenciais receberam caminho documental por teclado, com foco inicial, foco apos acao e saida segura por tab, shift+tab e escape quando houver camada sobreposta.
- Fluxos de aprovar, negar, ver ajuda e desfazer exigem ausencia explicita de keyboard trap.
- A ordem de foco foi ancorada em contexto, impacto, decisao e saida segura para evitar confirmacao sem leitura.

## achados por leitor de tela

- Botoes primarios precisam manter label in name, especialmente Aprovar, Negar, Pausar e Abrir ajuda.
- Status de falha, stale data, permissao e comprovante precisam ser anunciaveis sem roubar foco.
- Ajuda contextual precisa ser descobrivel por nome acessivel e papel coerente, sem depender so de icone.

## achados por mobile

- Fluxos essenciais exigem target minimo de 24x24 CSS px ou espacamento equivalente.
- Hoje, aprovar, comprovante e pausa de automacao nao podem depender de tabela densa como primeira visao.
- A CTA principal precisa permanecer alcancavel sem zoom obrigatorio e sem orientacao unica.

## achados por foco/target/status/reduced motion

- Foco visivel e nao obscurecido entram como requisito transversal para todos os fluxos com decisao.
- Mensagens de status precisam ter fallback textual e via anunciacao assistiva.
- Reduced motion foi tratado como exigencia de prudencia desta trilha: animacao nao pode ser necessaria para entender estado, risco ou falha.

## decisoes que nao podem depender so de cor

- Aprovar vs negar.
- Risco baixo, medio e alto.
- Permissao insuficiente.
- Falha bloqueante.
- Dado atrasado.
- Comprovante indisponivel.

## gaps que devem ir para BENCHUIX-22 ou Crisol

- BENCHUIX-22 deve validar contraste, reflow, foco nao obscurecido e target size em layout real responsivo.
- Crisol deve absorver gaps que dependam de nome, papel, valor, status annunciation ou autenticacao real implementada.
- Nenhum gap desta fase ficou classificado como CRITICAL aberto em fluxo essencial candidate-only.

## criterios PASS/WARN/BLOCK/INVALID

PASS: todos os fluxos essenciais possuem requisitos documentais cobrindo teclado, mobile e leitor de tela, com zero violacao critica aberta e sem decisao so por cor.

WARN: existe gap nao critico com destino explicito para BENCHUIX-22 ou Crisol, mas a leitura operacional continua segura no nivel documental.

BLOCK: um fluxo essencial fica impossivel por teclado, mobile ou leitor de tela; foco some; existe keyboard trap; ou status critico deixa de ser anunciavel.

INVALID: qualquer claim de conformidade real WCAG, produto acessivel pronto, browser/axe/Lighthouse executado, rota viva aberta, Project_ARIS alterado ou lock real aberto.
