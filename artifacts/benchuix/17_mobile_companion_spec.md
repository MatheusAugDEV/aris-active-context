## definição da fase

BENCHUIX-17 materializa Mobile Companion / PWA como fase candidata, mobile-first e synthetic-only da trilha BenchUIX. O foco e adaptar Hoje, Aprovar, Comprovantes e Pausar para uso frequente no celular sem depender de produto executavel.

## tese mobile companion / PWA

O mobile companion precisa reduzir friccao sem reduzir controle. O celular pode ser a superficie mais rapida para decidir, revisar e pausar, mas nunca pode esconder risco, stale data ou limite operacional.

## objetivo

Definir uma experiencia mobile companion / PWA candidate-only para Hoje, Aprovar, Comprovantes e Pausar, com politica de cache, estado degradado mobile e bloqueio explicito de aprovacao quando os dados estiverem stale ou incompletos.

"o dono consegue operar o essencial no celular sem perder controle?"

## relação com BENCHUIX-05, 11, 14 e 16

BENCHUIX-05 definiu Hoje como primeira leitura util. BENCHUIX-11 definiu a Approval Inbox com risco, permissao e will/will-not. BENCHUIX-14 definiu Historico / Comprovantes legiveis. BENCHUIX-16 proibiu falha opaca e exigiu degradacao explicada. BENCHUIX-17 comprime esses contratos para a superficie mobile sem vender cache como verdade ou offline como garantia real.

## experiência mobile para Hoje

Hoje mobile deve abrir com resumo curto, prioridade visivel, proximo passo seguro e sinal claro de stale ou degradado quando houver. O dono precisa entender em poucos segundos o que requer atencao e o que continua apenas para consulta.

## experiência mobile para Aprovar

Aprovar mobile deve mostrar risco, permissao, will/will-not e origem da simulacao antes do CTA. Se a informacao estiver stale, incompleta ou degradada, a aprovacao precisa ser bloqueada e a tela deve redirecionar para atualizar, revisar historico ou simular novamente.

## experiência mobile para Comprovantes

Comprovantes mobile deve priorizar leitura rapida, codigo de verificacao copiavel, evento associado, idade do registro e contexto do que ocorreu. O historico pode ficar disponivel em modo de leitura mesmo quando partes da experiencia estiverem degradadas, desde que o limite seja explicado.

## experiência mobile para Pausar

Pausar mobile deve ser uma acao controlada, com escopo legivel, texto de confirmacao e alternativa textual ao gesto. O dono precisa entender o que sera pausado, o que continua funcionando e qual o proximo passo para revisar ou retomar depois.

## regras de layout mobile

- priorizar uma coluna unica;
- manter CTA principal ao alcance visual sem competir com alertas;
- preservar ordem: contexto, risco ou limite, acao, fallback;
- evitar cards densos que exijam leitura lateral;
- manter banners de stale e degradado acima das acoes sensiveis.

## regras de legibilidade

Texto principal precisa ser escaneavel, com titulo curto, subtitulo explicativo e labels inequívocos. Datas, idade do cache e estado atual precisam aparecer em linguagem humana e com contraste suficiente.

## regras contra gesture-only essential action

Nenhuma acao essencial pode existir apenas por swipe, long press ou gesto escondido. Aprovar, revisar comprovante e pausar precisam ter botao, label textual e alternativa acessivel para leitor assistivo.

## estado degradado mobile

Modo degradado mobile deve preservar o minimo confiavel: contexto atual, ultimo dado confiavel, aviso de limitacao e proximo passo seguro. Ele nao pode parecer sucesso, nao pode esconder bloqueio de aprovacao e nao pode prender o cliente em loading indefinido.

## cache/stale data UX

Cache nesta fase e apenas candidato e serve para continuidade de leitura, nao para prometer offline real. Toda visao cacheada precisa exibir quando foi atualizada pela ultima vez, qual parte pode estar stale e quais acoes foram reduzidas por seguranca. Aprovacao com cache stale ou dados incompletos deve ser bloqueada.

## microcopy candidata

- "Mostrando a ultima versao disponivel no celular."
- "Estes dados podem estar desatualizados; revise antes de decidir."
- "Aprovacao bloqueada ate atualizar as informacoes."
- "Voce ainda pode revisar comprovantes e pausar com seguranca."
- "Se preferir, atualize ou consulte o historico relacionado."

## acessibilidade

A experiencia mobile precisa manter foco visivel, ordem de leitura clara, alvo de toque confortavel, texto alternativo para icones e sinais que nao dependam apenas de cor, vibracao ou gesto. Alertas de stale, bloqueio e degradado precisam ser anunciaveis por leitores assistivos.

## critérios de BLOCK

Bloquear quando houver:

- aprovacao permitida com cache stale;
- aprovacao permitida com dado incompleto;
- acao essencial apenas por gesto;
- stale ou degradado sem explicacao;
- offline ou cache vendido como garantia real;
- white screen, spinner infinito ou stack trace para cliente;
- qualquer app nativo, PWA executavel, service worker real, cache real, runtime real ou dado real no escopo.

## anti-escopo

Esta fase nao cria app nativo, nao cria PWA executavel, nao cria UI executavel, nao cria service worker real, nao cria cache real, nao executa runtime, nao executa acao real, nao usa cliente real, nao instala dependencias, nao usa OAuth real, nao cria billing, nao integra servico real e nao autoriza produto, piloto, producao, Bedrock PASS, secrets ou real_apply.

## handoff para BENCHUIX-18

BENCHUIX-18 deve usar esta base mobile para definir permissoes progressivas, visoes por papel e suspensao de acesso sem quebrar o bloqueio de stale approval, a legibilidade mobile e a exigencia de alternativa textual para acoes essenciais.
