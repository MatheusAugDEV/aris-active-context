# BENCHUIX-02 Access Model

## Definicao da Fase

BENCHUIX-02 define como o ARIS e acessado pelo cliente, pelo prospect, pelo sandbox e pela equipe interna, sem misturar superficies e sem abrir runtime real.

## Tese da Fase

- ARIS Client Workspace e a superficie principal.
- Web/PWA e a primeira superficie recomendada.
- Mobile Companion existe para aprovar, acompanhar status, ver alertas, consultar comprovantes e pausar.
- Landing publica explica valor e encaminha para sandbox ou onboarding.
- Demo Sandbox usa somente dados sinteticos.
- Internal Admin e isolado e invisivel ao cliente.
- WhatsApp, e-mail e push podem notificar e deep-linkar, mas nunca viram control-plane.
- Nenhuma superficie autoriza produto, runtime, secrets, real_apply ou producao.

## Regras de Boundary

- Cliente nao ve Internal Admin.
- Prospect nao ve dado operacional real.
- Demo Sandbox nao usa dado real.
- Mobile Companion nao faz criacao complexa.
- Canais auxiliares nao tomam decisao sensivel.
- Admin nao contamina tela cliente.
- Nenhuma superficie toca PSP real, secret ou runtime real nesta camada.

## Superficies

### ARIS_CLIENT_WORKSPACE

- Quem usa: cliente final em Modo A/B/C; direcao futura para Modo D sem poluir o baseline.
- Objetivo: ser a superficie principal para acompanhar operacao, revisar aprovacoes, consultar comprovantes e ajustar configuracoes seguras.
- Telas permitidas: Hoje, Automacoes, Aprovar, Historico / Comprovantes, Configuracoes.
- Acoes permitidas: ver resumo do dia, simular, revisar risco, aprovar, recusar, pausar, retomar, consultar historico, abrir comprovante, editar preferencias seguras.
- Acoes proibidas: admin interno, jargao tecnico, configuracao corporativa avancada como baseline, runtime tecnico, real_apply, acesso a secret, operacao de PSP real.
- Dados permitidos: status sintetico, previsao, recibo sintetico, risco traduzido para cliente, historico de acoes, configuracao de experiencia.
- Dados proibidos: secret, stack trace, token, log tecnico bruto, dado real de PSP, payload tecnico, credencial, jargao de active-context.
- Relacao com Modo A/B/C/D: baseline para A; disclosure progressivo para B/C; D apenas como direcao futura pos-Bedrock sem mudar a experiencia base.
- Riscos: dashboard virar tela corporativa, mistura com admin, decisao sensivel sem will/will-not, linguagem tecnica aparecer.
- Mitigacao: telas minimas, copy anti-jargao, aprovacao explicita, isolamento de admin, progressive disclosure.
- Invariantes protegidas: simplicidade do Dono-Solo, no-real-exec, sem admin visivel, sem runtime real, sem secrets, sem produto.
- Relacao com Crisol/Bedrock: gaps que exigirem consolidacao entre experiencia e runtime futuro vao para Crisol; produto real e expansao maior ficam pos-Bedrock.
- Criterios de BLOCK: admin aparecer, linguagem tecnica dominar fluxo principal, acao sensivel sem contexto, tela exigir dado real.

### MOBILE_COMPANION

- Quem usa: cliente mobile-first e ajudante autorizado para consulta e aprovacao limitada.
- Objetivo: permitir resposta rapida a alertas, aprovacoes, status, comprovantes e pausa sem exigir escritorio ou fluxo complexo.
- Telas permitidas: caixa de alertas, fila de aprovacao, status resumido, comprovantes recentes, pausa de automacao.
- Acoes permitidas: aprovar, recusar, ver alerta, ver status, ver comprovante, pausar, deep-linkar para Workspace quando a decisao exigir mais contexto.
- Acoes proibidas: criacao complexa, admin, runtime tecnico, configuracao corporativa avancada, real_apply, edicao estrutural de fluxo.
- Dados permitidos: resumo sintetico, comprovante sintetico, alerta, risco resumido, status, contexto de aprovacao.
- Dados proibidos: secret, dado real, payload tecnico, runtime log, configuracao de admin, credencial.
- Relacao com Modo A/B/C/D: essencial para A; util para B/C; complementar para D.
- Riscos: aprovacao sem contexto suficiente, sobrecarga de notificacao, tentativa de usar mobile para criacao pesada.
- Mitigacao: deep-link obrigatorio para decisao sensivel complexa, escopo curto de acao, copy direta, sem edicao estrutural.
- Invariantes protegidas: mobile nao substitui Workspace para casos complexos, sem admin, sem runtime real, sem produto, sem secrets.
- Relacao com Crisol/Bedrock: requisitos de cache, sincronizacao e degradacao real sao consolidados em Crisol; app nativo e pos-fase apropriada e ainda pre-Bedrock.
- Criterios de BLOCK: mobile permitir criacao complexa, admin, aprovacao sem contexto, ou exposicao de linguagem tecnica.

### PUBLIC_LANDING

- Quem usa: prospect, cliente em descoberta e operador comercial em demonstracao inicial.
- Objetivo: explicar valor do ARIS em 30-60 segundos e conduzir para Demo Sandbox ou onboarding futuro.
- Telas permitidas: hero, proposta de valor, exemplos sinteticos, prova de confianca, CTA para sandbox, FAQ nao tecnica.
- Acoes permitidas: explorar proposta de valor, iniciar demo sandbox, solicitar onboarding futuro, comparar antes/depois sintetico.
- Acoes proibidas: aprovar acao, operar automacao, exibir dado operacional real, mostrar backstage tecnico, mostrar admin, executar qualquer fluxo de control-plane.
- Dados permitidos: exemplos sinteticos, copy de valor, casos ilustrativos, limites declarados, linguagem de confianca.
- Dados proibidos: dado operacional real, comprovante real, log, secret, runtime detail, metricas operacionais reais.
- Relacao com Modo A/B/C/D: entrada comum para todos os modos; baseline narrativo favorece Modo A.
- Riscos: marketing prometer mais do que a camada prova, landing virar painel, vazamento de detalhe tecnico.
- Mitigacao: CTA claro para sandbox, exemplos sinteticos, copy sem jargao, separacao total do control-plane.
- Invariantes protegidas: landing nao decide, nao toca dado real, nao expande escopo para produto.
- Relacao com Crisol/Bedrock: claims que dependerem de runtime ou consolidacao operacional devem ser revalidadas em Crisol e Bedrock.
- Criterios de BLOCK: landing mostrar dado real, operar controle, ou depender de arquitetura para convencer.

### DEMO_SANDBOX

- Quem usa: prospect, cliente em avaliacao e equipe interna em demonstracao controlada.
- Objetivo: demonstrar o ARIS com dados sinteticos e comportamento seguro antes de qualquer produto real.
- Telas permitidas: jornada guiada, exemplos sinteticos, preview, aprovacao simulada, comprovante sintetico, estados de falha sinteticos.
- Acoes permitidas: navegar cenarios sinteticos, simular decisao, ver before/after sintetico, testar entendimento de comprovante, explorar limites.
- Acoes proibidas: real_apply, dado real, PSP real, secret, runtime real, webhook real, integracao real, credencial real.
- Dados permitidos: dataset sintetico, cenarios roteirizados, riscos sinteticos, comprovantes sinteticos, efeitos simulados.
- Dados proibidos: dado real de cliente, conta real, PSP real, secret, token, log de producao, runtime mutavel.
- Relacao com Modo A/B/C/D: demonstra baseline de A e disclosure de B/C; D somente como direcao futura controlada.
- Riscos: prospect confundir sandbox com produto real, vazamento de dado real, demo depender de explicacao arquitetural.
- Mitigacao: labeling synthetic-only, trilhas roteirizadas, isolamento explicito, proibicao de dado real, no-real-exec por design.
- Invariantes protegidas: sandbox nao toca runtime real, nao toca secret, nao toca PSP real, nao prova produto real.
- Relacao com Crisol/Bedrock: qualquer necessidade de integrar comportamento de demo a runtime futuro vai para Crisol; Bedrock continua fechado para produto.
- Criterios de BLOCK: qualquer dado real aparecer, qualquer runtime real ser tocado, ou a demo exigir backstage tecnico para funcionar.

### INTERNAL_ADMIN

- Quem usa: equipe interna autorizada para diagnostico, auditoria e suporte futuro.
- Objetivo: manter uma superficie separada para investigacao, auditoria e suporte sem contaminar o cliente.
- Telas permitidas: auditoria interna, diagnostico sintetico, suporte, trilha de eventos sintetica, configuracao interna nao exposta.
- Acoes permitidas: revisar diagnostico sintetico, acompanhar suporte, anotar contexto interno, preparar suporte futuro.
- Acoes proibidas: aparecer no Client Workspace, ficar disponivel em Mobile Companion, usar dado real nesta camada, abrir runtime real, real_apply, expor secret ao cliente.
- Dados permitidos: evidencias sinteticas, notas internas, classificacao de suporte, contexto de auditoria sintetico.
- Dados proibidos: surfaces client-facing, secret, conta real, credencial de producao, PSP real, dado operacional real do cliente.
- Relacao com Modo A/B/C/D: nao e superficie do cliente em A/B/C; em D aparece apenas como direcao futura interna e nunca como tela do cliente.
- Riscos: contaminacao de UI cliente, privilegio excessivo, dependencia de detalhe tecnico no fluxo do cliente.
- Mitigacao: isolamento de acesso, sem links a partir do Workspace, nomenclatura interna separada, zero mistura de navegacao.
- Invariantes protegidas: cliente nao ve admin, admin nao vira atalho de decisao cliente, sem runtime real, sem produto.
- Relacao com Crisol/Bedrock: consolidacao de suporte operacional e visibilidade real so pode ser tratada em Crisol/Bedrock quando houver gate.
- Criterios de BLOCK: admin aparecer ao cliente, surfaces compartilharem navegacao, ou admin depender de dado real nesta camada.

### AUXILIARY_CHANNELS

- Quem usa: cliente e prospect como recebedores de notificacao; sistema futuro como emissor controlado.
- Objetivo: avisar e redirecionar para a superficie correta sem transformar canal em lugar de decisao.
- Telas permitidas: nao possui telas proprias; usa mensagens, cards curtos e deep links.
- Acoes permitidas: notificar, lembrar, informar status, enviar recibo resumido, deep-linkar para Workspace ou Mobile Companion.
- Acoes proibidas: aprovar no corpo da mensagem, recusar no corpo da mensagem, executar acao sensivel no canal, mostrar admin, expor detalhe tecnico ou secret.
- Dados permitidos: resumo curto, alerta, CTA com deep link, status alto nivel, identificador humano de comprovante.
- Dados proibidos: payload tecnico, credencial, dado real sensivel, secret, token, controle de runtime, aprovacao inline.
- Relacao com Modo A/B/C/D: suporte transversal a todos os modos; especialmente util para A e B.
- Riscos: canal virar pseudo-control-plane, engenharia social por mensagem, contexto insuficiente para decisao.
- Mitigacao: proibicao de aprovacao inline, deep-link obrigatorio, copy curta, zero dado sensivel, reforco de superficie oficial.
- Invariantes protegidas: canais apenas notificam, nao executam, nao aprovam, nao tocam runtime real nem produto.
- Relacao com Crisol/Bedrock: integracoes reais de mensageria e politicas operacionais futuras so vao para Crisol/Bedrock com gate proprio.
- Criterios de BLOCK: canal aprovar, executar, ou expor dado sensivel ou admin.

## Decisao de Camada

- Workspace e a superficie principal e control-plane do cliente.
- Mobile Companion complementa o Workspace, nunca substitui decisao complexa.
- Landing e sandbox ficam fora do control-plane.
- Admin permanece isolado.
- Canais auxiliares so notificam e deep-linkam.
- Nenhuma superficie abre runtime, produto, secrets, real_apply ou producao.
