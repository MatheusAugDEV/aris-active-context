## definicao da fase

BENCHUIX-19 materializa um dashboard operacional avancado candidate-only, synthetic-only e separado do baseline dono-solo. O dashboard existe como command center opcional para operacao maior, nunca como primeira experiencia.

## tese do dashboard

Dashboard bom reduz tempo de decisao. Dashboard ruim transforma o operador em leitor de painel. Nesta fase, cada bloco do dashboard so entra se habilitar uma acao clara, limitar interpretacao e preservar o foco da thread principal.

## pergunta central

"o dashboard ajuda decisao operacional ou vira ruido?"

## modo simples vs modo avancado

O modo simples continua priorizando Hoje, Aprovar e Historico para dono-solo. O modo avancado so aparece quando a operacao ja precisa ver fila, risco, custo, warnings e auditoria em paralelo. O simples responde "o que exige minha atencao agora?". O avancado responde "onde a operacao esta degradando e qual acao corrige isso?".

## principios de anti-ruido

- nenhum KPI sem acao associada;
- nenhum numero sem limite de interpretacao;
- nenhum bloco pode empurrar o dono-solo para uma experiencia corporativa por padrao;
- warning sem proximo passo vira ruido e deve ser bloqueado;
- detalhe tecnico profundo nao pode competir com a mensagem operacional principal;
- a thread principal nunca pode depender do carregamento completo do dashboard avancado.

## composicao da tela

O dashboard avancado e composto por uma faixa superior com mensagem principal e estado operacional, seguida por widgets de fila e risco, depois blocos de custo e evidencias, e por fim warnings e audit trail. A ordem e:

1. mensagem principal e saude operacional;
2. aprovacoes pendentes e execucoes em andamento;
3. falhas e riscos;
4. evidencias, custo e tempo economizado;
5. warnings e audit trail.

## widgets operacionais obrigatorios

- aprovacoes pendentes com CTA para revisar fila;
- execucoes com CTA para abrir lista filtrada;
- falhas com CTA para revisar causa mais recente;
- evidencias com CTA para abrir comprovantes recentes;
- risco com CTA para revisar automacoes em observacao;
- custo com CTA para abrir guardrails e teto estimado;
- tempo economizado com CTA para revisar base de estimativa;
- saude operacional com CTA para ver fatores degradantes;
- warnings com CTA para priorizar bloqueios ou stale data;
- audit trail com CTA para abrir eventos recentes.

## loading, stale, vazio, erro, parcial e degradado

Loading: skeletons curtos e mensagem principal prioritaria.

Stale: mostrar idade do dado e limitar acoes que dependem de frescor.

Vazio: explicar que nao existe sinal acionavel, nao que "nao ha nada".

Erro: explicar o que nao foi carregado e qual fallback continua seguro.

Parcial: manter widgets confiaveis visiveis e marcar os ausentes como indisponiveis.

Degradado: reduzir o dashboard a mensagem principal, saude operacional, warnings e link para historico.

## progressive disclosure

Modo simples nunca recebe estes widgets por default. O avancado pode ser aberto por papel com contexto suficiente, mas cada widget ainda expande em camadas: resumo curto, detalhe relevante, depois historico ou comprovante. Nada abre com jargao ou dumping de logs.

## exemplos de linguagem para o usuario

- "Ha 3 aprovacoes aguardando revisao explicita."
- "Duas automacoes estao com falha repetida e pedem revisao."
- "O custo estimado desta janela continua dentro do teto candidato."
- "Os dados deste painel estao atrasados ha 4 minutos; usamos o ultimo snapshot seguro."
- "Mostramos primeiro o que pede decisao. O restante fica disponivel sob demanda."

## criterios de PASS/WARN/BLOCK/INVALID

PASS: todo KPI habilita acao clara, simples e avancado permanecem separados, latencia e degradacao segura estao definidas e nao ha dashboard como experiencia inicial.

WARN: algum KPI depende de proxy synthetic-only com interpretacao limitada e precisa follow-up em BENCHUIX-20.

BLOCK: dashboard depende de runtime real, dado real, vanity metric, thread blocking ou mistura simples com avancado sem boundary explicito.

INVALID: qualquer claim de produto pronto, Bedrock pronto, seguranca final, live route aberto, integracao real ou mutacao de Project_ARIS.

## anti-escopo

Esta fase nao cria UI real, nao conecta dado real, nao toca billing real, nao usa OAuth real, nao cria dashboard executavel, nao abre live route, nao promove produto, nao autoriza runtime real, nao instala dependencia e nao muda Project_ARIS.

## handoff para BENCHUIX-20

BENCHUIX-20 deve transformar este dashboard avancado em linguagem de confianca ainda mais humana, com microcopy consistente para stale, warning, custo, risco, falha e comprovante sem virar painel tecnico.
