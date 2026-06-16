## definição da fase

BENCHUIX-13 materializa a Tela Automações como fase candidata, synthetic-only e operacionalmente legivel da trilha BenchUIX. O objetivo e organizar as automacoes candidatas em uma lista clara, segura e auditavel.

## tese da Tela Automações

Quando o cliente entende quais automacoes existem, em que estado estao e o que pode fazer com elas, ele consegue operar com confianca sem depender de console tecnico.

## objetivo

Definir uma lista de automacoes candidatas com status visivel, erro legivel, historico acessivel, pausa e edicao candidate-only, sem runtime real, sem raw logs e sem DAG tecnico exposto.

"o cliente entende quais automações existem, em que estado estão e o que pode fazer com elas?"

## relação com BENCHUIX-12

BENCHUIX-12 definiu os estados visiveis do fluxo. BENCHUIX-13 usa esses estados para exibir proxima execucao candidata, ultima execucao ou simulacao candidata e falhas de modo compreensivel dentro da lista de automacoes.

## estrutura da lista

A lista deve mostrar cada automacao como um item legivel, com nome, objetivo curto, status atual, proxima execucao candidata, ultima execucao ou simulacao candidata, erro visivel quando existir e acoes candidatas disponiveis.

## estrutura do card/item de automação

Cada item deve conter:

- nome claro da automacao
- resumo curto do que ela faz
- status atual visivel
- proxima execucao candidata
- ultima execucao ou simulacao candidata
- idade visivel dos dados
- erro visivel quando existir
- acoes candidatas

## status de próxima execução candidata

A proxima execucao candidata precisa dizer se esta prevista, pausada, bloqueada, degradada, aguardando aprovacao ou sem data definida. O cliente nao pode depender de linguagem vaga para entender o que vem a seguir.

## status de última execução/simulação candidata

A ultima execucao ou simulacao candidata precisa indicar quando aconteceu, qual foi o estado final e se houve erro, degradacao ou bloqueio. Simulacao nao pode ser apresentada como execucao real.

## erros visíveis

Erros precisam aparecer de forma legivel, sem esconder contexto importante e sem empurrar o cliente para log cru ou console tecnico. O motivo do erro e o proximo passo seguro devem estar visiveis.

## ações candidatas

As acoes candidatas desta fase sao:

- pausar
- editar
- ver historico
- simular novamente
- duplicar, quando for compativel com o fluxo definido em BENCHUIX-09

Todas permanecem candidate-only, sem efeito real e com alteracao auditavel.

## política de alteração auditável

Toda pausa, edicao, duplicacao ou retorno para simulacao precisa aparecer como alteracao rastreavel do ponto de vista do cliente. Nenhuma mudanca importante pode parecer acontecer sozinha.

## empty state

Quando nao houver automacoes, a tela deve explicar o vazio com linguagem humana, dizer o que falta para aparecer a primeira automacao e apontar um proximo passo seguro.

## degraded behavior

Se faltar contexto para mostrar uma automacao com clareza, a lista deve marcar degradado, explicar o limite e evitar qualquer aparencia de sucesso ou normalidade.

## acessibilidade

A tela precisa manter status, erros e acoes com rotulos claros, ordem de leitura previsivel, sinais textuais e visuais combinados e navegacao compreensivel sem depender apenas de cor.

## critérios de BLOCK

Bloquear quando houver:

- erro escondido
- proxima ou ultima execucao sem status legivel
- DAG tecnico exposto como superficie primaria
- raw logs expostos como superficie primaria
- alteracao sem auditoria
- sucesso declarado sem estado que sustente sucesso
- qualquer automacao, mutacao, dado ou servico real no escopo

## anti-escopo

Esta fase nao cria UI executavel, nao cria automacao real, nao executa runtime, nao chama servico real, nao usa dado real, nao expoe console tecnico e nao autoriza produto, piloto, producao, Bedrock PASS, runtime, secrets ou real_apply.

## handoff para BENCHUIX-14

BENCHUIX-14 deve usar esta estrutura para aprofundar Historico e Comprovantes, preservando erro visivel, alteracao auditavel e separacao clara entre lista operacional e prova historica.
