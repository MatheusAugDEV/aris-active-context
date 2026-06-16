## definição da fase

BENCHUIX-14 materializa Historico / Comprovantes como fase candidata, synthetic-only e auditavel da trilha BenchUIX. O objetivo e mostrar o que aconteceu de modo legivel, sem exigir leitura de material tecnico.

## tese do histórico/comprovantes

Quando o cliente consegue revisar eventos e comprovantes com linguagem humana, ele entende o que ocorreu, o que foi decidido e o que ainda pode ser revertido sem depender de console ou equipe tecnica.

## objetivo

Definir uma experiencia de historico e comprovantes que mostre eventos, recibos, codigo de verificacao, busca, exportacao candidate-only e link para rollback ou compensacao futura sem parecer execucao real ou prova juridica final.

"o cliente consegue provar o que aconteceu sem ler material técnico?"

## relação com BENCHUIX-13

BENCHUIX-13 definiu a lista operacional de automacoes e o link para historico. BENCHUIX-14 aprofunda esse link, transformando cada evento relevante em historico legivel e comprovante imutavel.

## estrutura da visão de histórico

A visao de historico deve organizar eventos em ordem clara, com filtros simples, resumo do que ocorreu, estado associado, impacto resumido e acesso ao comprovante correspondente quando existir.

## categorias de evento

As categorias minimas devem cobrir:

- simulacao realizada
- aprovacao ou recusa registrada
- pausa candidata aplicada
- edicao candidata registrada
- degradacao ou falha relevante
- referencia futura de rollback ou compensacao

## busca

A busca deve aceitar linguagem simples por nome da automacao, periodo, categoria de evento, estado e codigo de verificacao. O cliente nao pode depender de identificador tecnico para localizar um comprovante.

## exportação candidate-only

Exportacao nesta fase existe apenas como capacidade candidata e synthetic-only. Ela deve deixar claro que gera uma copia de consulta e nao uma prova real emitida por sistema produtivo.

## link para rollback/compensação

O historico pode apontar para um link de rollback ou compensacao futura quando houver relacao com o evento. Esse link e apenas referencial nesta fase e nao executa rollback real.

## política de imutabilidade de comprovantes

Comprovantes antigos devem ser imutaveis: podem ser lidos, buscados, exportados em modo candidato e relacionados a eventos futuros, mas nao podem ser editados nem deletados.

## política contra stack trace como visão primária

Falhas historicas precisam ser explicadas em linguagem humana, com causa resumida e proximo passo seguro. Material tecnico aprofundado pode existir em camada interna, mas nunca como visao primaria do cliente.

## política contra hash como termo primário

O cliente deve ver codigo de verificacao legivel e descricao clara do evento. Impressao tecnica interna pode existir como apoio de auditoria, mas nao deve virar o termo principal da experiencia.

## estados obrigatórios

Os estados obrigatorios desta fase sao:

- empty
- loading
- error
- success
- degraded

## acessibilidade

Historico e comprovantes precisam ter ordem de leitura previsivel, filtros compreensiveis, rotulos claros, texto suficiente para leitores de tela e combinacao de sinais textuais e visuais sem depender apenas de cor.

## critérios de BLOCK

Bloquear quando houver:

- comprovante antigo editavel ou deletavel
- stack trace como visao primaria
- hash como termo primario para o cliente
- exportacao apresentada como prova real
- codigo de verificacao ilegivel ou enganoso
- link de rollback que pareca executar acao real
- falha historica escondida
- qualquer mutacao, dado ou servico real no escopo

## anti-escopo

Esta fase nao cria UI executavel, nao executa runtime, nao executa rollback real, nao cria acao real, nao usa dado real, nao exporta prova real, nao expoe stack trace como superficie primaria e nao autoriza produto, piloto, producao, Bedrock PASS, runtime, secrets ou real_apply.

## handoff para BENCHUIX-15

BENCHUIX-15 deve usar este historico para detalhar rollback, desfazer e compensar, preservando a imutabilidade dos comprovantes, a leitura humana do evento e a separacao entre referencia e execucao real.
