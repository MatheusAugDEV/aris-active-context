# BENCHUIX-23 Competitive Task Matrix

Este documento e candidate-only. Ele compara tarefas com base em fonte oficial primaria ou gap oficial registrado. Nao declara vencedor global. Toda conclusao abaixo vale apenas nesta tarefa, com esta fonte e com esta limitação.

## onboarding
Definicao: quanto esforco inicial uma pessoa gasta para sair do zero e entrar em um fluxo util.
Por que importa para ARIS: se o primeiro minuto for tecnico demais, o posicionamento owner-solo quebra cedo.
Comparaveis: Zapier, Make, n8n, Microsoft Power Automate, Airtable AI.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Blank Zap e draft salvo reduzem friccao de entrada. | `ZAPIER_QUICKSTART` |
| Make | Primeiro scenario e ensinavel, mas assume mais mentalidade de builder. | `MAKE_CREATE_SCENARIO` |
| n8n | Cloud ajuda a comecar, mas self-hosted explicita dependencia tecnica. | `N8N_CHOOSE_N8N` |
| Microsoft Power Automate | A documentacao prova amplitude, mas nao um owner-solo fast path. | `POWER_AUTOMATE_OVERVIEW` |
| Airtable AI | Automations e AI assistida ajudam a iniciar sem sair do produto. | `AIRTABLE_AUTOMATIONS` |

Evidencia de fonte: a comparacao usa quick starts e overviews oficiais; nenhum tempo exato foi tratado como provado.
Onde ARIS ganha: a tese de 3 minutos continua plausivel se o fluxo ficar mais curto que a entrada enterprise.
Onde ARIS perde: ainda nao ha prova comparativa de first-time value tao concreta quanto o blank Zap.
Onde ARIS deve aprender: draft seguro, caminho inicial direto e remocao de jargao tecnico.
Gap destination: `BENCHUIX-24`
Conclusao limitada: nesta tarefa, Zapier e Airtable oferecem baseline oficial forte; ARIS ainda precisa provar a mesma clareza sem depender de narrativa.

## create_automation
Definicao: criar uma automacao nova com o menor numero de decisoes tecnicas expostas.
Por que importa para ARIS: a criacao e o momento em que simplicidade por fora encontra rigor por dentro.
Comparaveis: Zapier, Make, n8n, Microsoft Power Automate, HubSpot Breeze, Airtable AI, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Editor de trigger e action favorece criacao rapida. | `ZAPIER_QUICKSTART` |
| Make | Scenarios e API confirmam poder de composicao e gestao. | `MAKE_SCENARIOS_API` |
| n8n | Canvas explicito e publish controlado favorecem poder tecnico. | `N8N_CREATE_WORKFLOW` |
| Power Automate | Approval flow demonstra construcao guiada dentro de flow. | `POWER_AUTOMATE_APPROVALS` |
| HubSpot Breeze | Run Agent dentro de workflow prova integracao de AI ao fluxo. | `HUBSPOT_RUN_AGENT_WORKFLOWS` |
| Airtable AI | Generate with AI prova criacao assistida em automations. | `AIRTABLE_GENERATE_WITH_AI` |
| Salesforce Agentforce | Build, test and supervise indica amplitude alta, mas em linguagem enterprise. | `SALESFORCE_AGENTFORCE_OVERVIEW` |

Evidencia de fonte: as fontes mostram criacao, mas variam muito entre builder-first e business-first.
Onde ARIS ganha: o anti-node-editor e a linguagem natural continuam bem posicionados para owner-solo.
Onde ARIS perde: ainda nao existe artifact proprio provando que a criacao em ARIS sera tao objetiva quanto o melhor quickstart do mercado.
Onde ARIS deve aprender: disclosure progressivo para modo avancado sem poluir o baseline.
Gap destination: `BENCHUIX-24`
Conclusao limitada: nesta tarefa, o mercado ja oferece varias formas de criar; a diferenca de ARIS depende de reduzir ambiguidade, nao de igualar breadth.

## preview_simulation
Definicao: ver o que acontecera antes de tocar estado real.
Por que importa para ARIS: preview deterministico e um dos nucleos de confianca do produto.
Comparaveis: Zapier, n8n, Microsoft Power Automate, Airtable AI, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Test mode existe, mas e connector-specific, nao um preview universal. | `ZAPIER_TEST_MODE` |
| n8n | Manual execution enquanto workflow esta inactive cria teste forte de builder. | `N8N_EXECUTIONS` |
| Power Automate | Run history e monitoring sao fortes, mas depois da execucao. | `POWER_AUTOMATE_RUN_HISTORY` |
| Airtable AI | History e versioning existem; preview deterministico nao foi provado. | `AIRTABLE_AUTOMATIONS` |
| Salesforce Agentforce | Testing Center prova simulacao e sandbox oficial. | `SALESFORCE_TESTING_CENTER` |

Evidencia de fonte: nenhuma fonte verificada provou o mesmo contrato de before/after diff orientado a owner-solo que ARIS pretende.
Onde ARIS ganha: ha espaco real para diferenciar com preview unificado e mais legivel.
Onde ARIS perde: Salesforce ja prova tooling serio de simulacao e teste.
Onde ARIS deve aprender: separar teste de builder e preview de decisao para nao virar laboratorio tecnico.
Gap destination: `BENCHUIX-26`
Conclusao limitada: nesta tarefa, ARIS pode ganhar se mantiver preview deterministico e curto; isso ainda e candidate-only, nao prova implementada.

## approval
Definicao: parar, revisar e decidir antes de uma acao sensivel seguir.
Por que importa para ARIS: sem aprovacao confiavel, a promessa de autonomia segura colapsa.
Comparaveis: Zapier, n8n, Microsoft Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Human in the Loop pausa o fluxo para review e aprovacao. | `ZAPIER_HITL_APPROVAL` |
| n8n | HITL de tool calls permite aprovar ou negar antes da acao. | `N8N_HITL_APPROVAL` |
| Power Automate | Approval action e nativa e madura, inclusive com mobile. | `POWER_AUTOMATE_APPROVALS` |
| Airtable AI | Mobile interfaces provam approve or reject em contexto de interface. | `AIRTABLE_MOBILE_INTERFACES` |
| HubSpot Breeze | Approvals cobrem records, content e outros ativos. | `HUBSPOT_APPROVALS` |
| Salesforce Agentforce | Advanced approvals provam cadeias mais complexas. | `SALESFORCE_ADVANCED_APPROVALS` |

Evidencia de fonte: a existencia do gate esta bem provada no mercado; o diferencial muda para contexto e clareza.
Onde ARIS ganha: a tese will / will-not e de menor carga cognitiva ainda e forte.
Onde ARIS perde: concorrentes enterprise ja mostram amplitude de superficie e canais.
Onde ARIS deve aprender: contexto suficiente sem transformar a decisao em painel corporativo.
Gap destination: `BENCHUIX-25`
Conclusao limitada: nesta tarefa, paridade mecanica nao basta; ARIS so avanca se a aprovacao for mais compreensivel e nao apenas mais bonita.

## risk_explanation
Definicao: explicar risco, impacto e limite de interpretacao antes da decisao.
Por que importa para ARIS: aprovacao sem explicacao e teatro de seguranca.
Comparaveis: Zapier, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | O gate existe, mas a fonte nao prova linguagem forte de risco. | `ZAPIER_HITL_APPROVAL` |
| n8n | O gate existe, mas a fonte e tecnica e nao owner-facing. | `N8N_HITL_APPROVAL` |
| Power Automate | Approval action prova fluxo, nao prova semantica de risco. | `POWER_AUTOMATE_APPROVALS` |
| Airtable AI | Interfaces moveis provam acao, nao explicacao de risco. | `AIRTABLE_MOBILE_INTERFACES` |
| HubSpot Breeze | Approvals provam revisao, nao taxonomia de risco. | `HUBSPOT_APPROVALS` |
| Salesforce Agentforce | Logs e supervisao provam observabilidade, nao copy de risco ao operador. | `SALESFORCE_EVENT_LOGS` |

Evidencia de fonte: aqui o gap e quase universal nas fontes oficiais verificadas.
Onde ARIS ganha: se preservar linguagem explicita de risco, impacto e o que nao fara.
Onde ARIS perde: ainda nao existe benchmark proprio materializado para provar essa superioridade task-by-task.
Onde ARIS deve aprender: nao confundir log, audit trail ou approval gate com explicacao humana suficiente.
Gap destination: `BENCHUIX-27`
Conclusao limitada: nesta tarefa, o mercado verificado prova gates, nao prova boa explicacao; ARIS tem oportunidade real, mas ainda sem implementacao.

## evidence_receipt
Definicao: encontrar e entender prova do que ocorreu.
Por que importa para ARIS: historico sem leitura rapida nao gera confianca operacional.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | History mostra runs, filtros, status e task usage. | `ZAPIER_HISTORY` |
| Make | History exportavel e fulltext search ajudam investigacao. | `MAKE_SCENARIO_HISTORY` |
| n8n | Executions sao fortes para builder, fracos como recibo owner-facing. | `N8N_EXECUTIONS` |
| Power Automate | FlowRun expande status, duracao, owner e erro em escala. | `POWER_AUTOMATE_RUN_HISTORY` |
| Airtable AI | History e audit logs sustentam revisao e exportacao. | `AIRTABLE_AUDIT_LOGS` |
| HubSpot Breeze | Audit logs, summarize e analyze tab dao boa trilha de revisao. | `HUBSPOT_AUDIT_LOGS` |
| Salesforce Agentforce | Event logs e audit dashboards provam rastreio, nao recibo simples. | `SALESFORCE_EVENT_LOGS` |

Evidencia de fonte: todos os fortes aqui tendem para telemetria ou auditoria, nao para comprovante amigavel.
Onde ARIS ganha: pode transformar trace em recibo humano sem perder prova.
Onde ARIS perde: os concorrentes enterprise ja possuem profundidade operacional maior.
Onde ARIS deve aprender: separar prova para suporte, prova para auditoria e prova para dono-solo.
Gap destination: `BENCHUIX-27`
Conclusao limitada: nesta tarefa, ARIS nao precisa vencer em profundidade bruta; precisa vencer em legibilidade sem sacrificar lastro.

## rollback_undo_compensate
Definicao: deixar claro o que pode desfazer, o que so pode compensar e o que e irreversivel.
Por que importa para ARIS: prometer undo falso destrói confianca.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Replay e forte, mas nao equivale a undo honesto. | `ZAPIER_REPLAY` |
| Make | History e replay ajudam suporte, nao provam compensacao semantica. | `MAKE_SCENARIO_HISTORY` |
| n8n | Export/import ajuda change control, nao prova reversao de efeito. | `N8N_EXPORT_IMPORT` |
| Power Automate | Run metadata e audit ajudam diagnostico, nao undo de negocio. | `POWER_AUTOMATE_RUN_HISTORY` |
| Airtable AI | Version history prova governanca de configuracao. | `AIRTABLE_AUTOMATIONS` |
| HubSpot Breeze | Revision history prova revert de workflow, nao compensacao de efeito. | `HUBSPOT_WORKFLOW_REVISION_HISTORY` |
| Salesforce Agentforce | Nenhuma fonte verificada provou rollback honesto por tarefa. | `SALESFORCE_ADVANCED_APPROVALS` |

Evidencia de fonte: os concorrentes verificados tendem a provar replay, revert de configuracao ou log, nao honestidade sobre efeito externo.
Onde ARIS ganha: esta e uma das areas mais promissoras para diferenciação real.
Onde ARIS perde: ainda nao existe prova propria implementada; existe apenas tese documental forte.
Onde ARIS deve aprender: rotular melhor a fronteira entre rerun, revert de configuracao e compensacao.
Gap destination: `BENCHUIX-26`
Conclusao limitada: nesta tarefa, a vantagem potencial de ARIS depende de manter a honestidade do vocabulário e torna-la visivel no demo.

## failure_degraded_mode
Definicao: explicar falha, estado degradado e proximo passo util.
Por que importa para ARIS: erro sem orientacao vira abandono.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Run history e statuses ajudam triagem de falha. | `ZAPIER_HISTORY` |
| Make | History, details e fulltext search criam baseline forte de investigacao. | `MAKE_SCENARIO_HISTORY` |
| n8n | Executions ajudam o builder, nao provam UX de degradacao ao dono-solo. | `N8N_EXECUTIONS` |
| Power Automate | Run history e analytics sustentam troubleshooting forte. | `POWER_AUTOMATE_RUN_HISTORY` |
| Airtable AI | History e troubleshooting auxiliam revisao, nao explicam degradacao por task. | `AIRTABLE_AUTOMATIONS` |
| HubSpot Breeze | Audit logs ajudam revisar atividade, nao o estado degradado da tarefa. | `HUBSPOT_AUDIT_LOGS` |
| Salesforce Agentforce | Event logs e supervisao provam observabilidade forte. | `SALESFORCE_EVENT_LOGS` |

Evidencia de fonte: a maior parte do mercado verificado prova inspectability, nao necessariamente clareza de degraded state.
Onde ARIS ganha: se transformar falha em orientacao de decisao, nao apenas em trilha tecnica.
Onde ARIS perde: ainda falta prova de que a implementacao futura vai manter a mesma profundidade de investigacao dos players enterprise.
Onde ARIS deve aprender: combinar estado visual, causa provavel e proximo passo seguro.
Gap destination: `BENCHUIX-24`
Conclusao limitada: nesta tarefa, observabilidade existe no mercado; a oportunidade de ARIS esta em traduzir observabilidade em acao humana clara.

## mobile
Definicao: agir, revisar e aprovar com seguranca em superficie movel.
Por que importa para ARIS: o dono-solo opera fora da mesa.
Comparaveis: Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce, mais gaps oficiais de Zapier, Make e n8n.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Power Automate | Push e approve or reject mobile ja sao oficiais. | `POWER_AUTOMATE_MOBILE_APPROVALS` |
| Airtable AI | Mobile interfaces documentam acao imediata e approve or reject. | `AIRTABLE_MOBILE_INTERFACES` |
| HubSpot Breeze | Mobile approvals cobrem aprovar, cancelar e pedir mudancas. | `HUBSPOT_MOBILE_APPROVALS` |
| Salesforce Agentforce | Ajudante movel existe, mas a fonte e mais enterprise do que owner-solo. | `SALESFORCE_MOBILE_AGENTFORCE` |
| Zapier | limitação por source gap: nenhuma superficie movel oficial forte foi verificada. | `ZAPIER_MOBILE_OFFICIAL_GAP` |
| Make | limitação por source gap: nenhum documento atual forte foi verificado. | `MAKE_MOBILE_OFFICIAL_GAP` |
| n8n | limitação por source gap: nenhuma superficie oficial movel forte foi verificada. | `N8N_MOBILE_OFFICIAL_GAP` |

Evidencia de fonte: ha concorrentes com fonte mobile forte e outros onde seria irresponsavel inventar.
Onde ARIS ganha: mobile companion pode continuar focado em aprovar, pausar, recibo e falha sem virar app corporativo genérico.
Onde ARIS perde: os concorrentes com fonte mobile oficial ja materializam a acao movel, enquanto ARIS ainda esta em nivel candidate-only.
Onde ARIS deve aprender: reduzir passos e manter contexto de risco em telas pequenas.
Gap destination: `BENCHUIX-25`
Conclusao limitada: nesta tarefa, ARIS precisa provar mobile seguro; ate la, a comparacao vale como pressao de design, nao como claim de mercado.

## auditability
Definicao: rastrear quem fez o que, quando e com qual contexto.
Por que importa para ARIS: confianca de produto nao sobrevive sem trilha de auditoria futura.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | History e filtros dao boa trilha de runs. | `ZAPIER_HISTORY` |
| Make | History, changelog e export CSV sustentam governanca forte. | `MAKE_SCENARIO_HISTORY` |
| n8n | Execution history e util, mas mais builder-centric. | `N8N_EXECUTIONS` |
| Power Automate | Purview e FlowRun em Dataverse elevam a profundidade de auditoria. | `POWER_AUTOMATE_ACTIVITY_LOGS` |
| Airtable AI | Audit log search, detail e API sao oficiais. | `AIRTABLE_AUDIT_LOGS` |
| HubSpot Breeze | Audit logs e employee access history sao fortes. | `HUBSPOT_AUDIT_LOGS` |
| Salesforce Agentforce | Enhanced event logs e audit dashboards provam rastreabilidade ampla. | `SALESFORCE_EVENT_LOGS` |

Evidencia de fonte: os melhores exemplos verificados sao enterprise e admin-heavy.
Onde ARIS ganha: pode converter parte dessa profundidade em prova mais legivel para o usuario final.
Onde ARIS perde: ainda nao ha caminho runtime-grade autorizado para igualar audit depth.
Onde ARIS deve aprender: separar audit trail futuro de comprovante futuro sem confundir um com o outro.
Gap destination: `CRISOL`
Conclusao limitada: nesta tarefa, o mercado enterprise esta na frente em profundidade; ARIS precisa decidir qual profundidade futura e essencial ao seu posicionamento.

## dashboard
Definicao: transformar atividade e risco em sinais acionaveis.
Por que importa para ARIS: dashboard sem proximo passo vira vanity.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | History e task usage ajudam, mas nao provam advanced dashboard owner-first. | `ZAPIER_HISTORY` |
| Make | Per-scenario history e forte, dashboard amplo nao foi verificado. | `MAKE_SCENARIO_HISTORY` |
| n8n | Evaluations trazem qualidade ao builder, nao dashboard owner-solo. | `N8N_EVALUATIONS` |
| Power Automate | Admin analytics cobrem runs, usage, errors e tipos de flow. | `POWER_AUTOMATE_ANALYTICS` |
| Airtable AI | Admin audit reports existem, mas operator dashboard nao foi provado. | `AIRTABLE_AUDIT_LOGS` |
| HubSpot Breeze | Analyze tab com totais e charts ja existe. | `HUBSPOT_AUDIT_LOGS` |
| Salesforce Agentforce | Audit and feedback dashboards existem em superficie oficial. | `SALESFORCE_AUDIT_DASHBOARDS` |

Evidencia de fonte: os dashboards verificados mais fortes tendem para admin/reporting, nao para decisao owner-solo.
Onde ARIS ganha: a tese de actionable dashboard continua correta se focar risco, prova, excecao e proximo passo.
Onde ARIS perde: o pacote atual ainda e conceitual; concorrentes oficiais ja mostram analytics de producao ou auditoria.
Onde ARIS deve aprender: transformar visualizacao em triagem operacional mensuravel.
Gap destination: `BENCHUIX-24`
Conclusao limitada: nesta tarefa, ARIS nao precisa competir em breadth; precisa competir em acao certa por tela.

## demo
Definicao: mostrar valor rapidamente sem tocar estado real.
Por que importa para ARIS: demo e a forma mais visivel de converter curiosidade em confianca.
Comparaveis: Zapier, Make, n8n, Power Automate, Airtable AI, HubSpot Breeze, Salesforce Agentforce.

| Competidor | Comparacao por criterio | Fonte |
| --- | --- | --- |
| Zapier | Connector test mode permite demonstracao sem dinheiro real. | `ZAPIER_TEST_MODE` |
| Make | Primeiro scenario funciona como walkthrough de valor. | `MAKE_CREATE_SCENARIO` |
| n8n | Manual execution permite demonstracao antes de publicar. | `N8N_EXECUTIONS` |
| Power Automate | Tutorial de approval serve como demo funcional, mas nao como sandbox curto. | `POWER_AUTOMATE_APPROVALS` |
| Airtable AI | Generate with AI demonstra assistencia em workflow e conteudo. | `AIRTABLE_GENERATE_WITH_AI` |
| HubSpot Breeze | A breadth do overview ajuda demo comercial, nao um trust script fechado. | `HUBSPOT_BREEZE_OVERVIEW` |
| Salesforce Agentforce | Testing Center e ambiente forte para demonstração e simulacao. | `SALESFORCE_TESTING_CENTER` |

Evidencia de fonte: varios concorrentes provam demos ou testes seguros, mas poucos articulam a jornada entender -> confiar -> evidência -> rollback em um fluxo curto.
Onde ARIS ganha: pode orquestrar valor com menos explicacao arquitetural e mais prova de decisao segura.
Onde ARIS perde: Salesforce ja prova tooling de demo/teste mais maduro, e Zapier prova test mode pragmatico.
Onde ARIS deve aprender: um sandbox fechado, repetivel e com fronteira clara entre teste e estado real.
Gap destination: `BENCHUIX-26`
Conclusao limitada: nesta tarefa, ARIS tem espaco se o demo for curto, sintético e centrado em confiança; isso ainda precisa ser materializado.
