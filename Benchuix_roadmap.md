# BENCHUIX — Trilha Final da Camada ARIS

**Camada:** BenchUX com escopo BenchUIX
**Posição canônica:** pós-Infernus Revalidation → pré-Crisol
**Natureza:** Product Reality Lab, UX/UI, benchmark, design system, performance, trust UX e demo readiness
**Estado:** desenho de camada e execução futura controlada
**Produto real:** não autorizado
**Real apply:** não autorizado
**Secrets:** não autorizado
**Cliente real:** não autorizado
**Protótipo permitido:** sandbox-only, synthetic-only, sem conexão com runtime real mutável

---

## 0. Tese da camada

BenchUIX existe para provar se o ARIS pode ser entendido, usado, confiado, comparado e demonstrado como produto SaaS de alto padrão, sem ainda virar produto.

A tese central é:

> **Simples por fora, rigoroso por dentro.**

Para o cliente, ARIS deve ser direto:

> “O que vai acontecer? O que não vai acontecer? Qual risco existe? Precisa da minha confirmação? O que foi feito? Existe comprovante? Dá para desfazer?”

Para o sistema, ARIS continua rigoroso:

> permissões, limites, evidência, rollback, retry, custo, latência, rastreabilidade, idempotência, estado seguro e bloqueio quando necessário.

---

## 1. Princípios fixos

1. **PROPOSER ≠ GATE**
   Nenhum modelo declara PASS. A fase só fecha por operador + artifacts + hash + CI verde.

2. **Produto é pós-Bedrock**
   BenchUIX não autoriza produto, piloto, real_apply, secrets, produção ou cliente real.

3. **UI é mecanismo de controle**
   A interface não é decoração. Ela comunica permissão, limite, risco, evidência, rollback e falha.

4. **Dono-Solo é o baseline**
   O pequeno negócio com uma pessoa cuidando de tudo governa a simplicidade do produto.

5. **Progressive disclosure**
   Dono-solo vê o mínimo. Equipes maiores ganham camadas avançadas sem reescrever o produto.

6. **Anti-`phase=null`**
   Dentro da trilha BenchUIX ativa, toda fase com `decision=pass` aponta para a próxima. A última aponta para Crisol.

7. **Local repair only**
   Defeitos de artifact/schema/CI/mirror são reparados localmente. Defeitos que cruzam experiência × runtime real vão para Crisol.

8. **Will / Will-Not obrigatório**
   Toda ação sensível deve dizer claramente:

   * o que ARIS vai fazer;
   * o que ARIS não vai fazer.

9. **Se a UI mostra, o sistema prova. Se o sistema faz, a UI mostra.**
   Nunca um sem o outro.

---

## 2. Superfícies do produto

### 2.1 ARIS Client Workspace

Superfície principal do cliente.

Formato recomendado:

* web app;
* PWA;
* responsivo;
* mobile-first;
* synthetic sandbox durante BenchUIX.

Telas base:

* Hoje;
* Automações;
* Aprovar;
* Histórico / Comprovantes;
* Configurações.

### 2.2 Mobile Companion

Superfície para:

* aprovar;
* recusar;
* ver alertas;
* ver status;
* consultar comprovante;
* pausar automação.

Não é app nativo no início. É companion PWA.

### 2.3 Landing pública

Explica ARIS em 30–60 segundos.

Não mostra backstage técnico.

### 2.4 Demo sandbox

Demonstra ARIS com dados sintéticos.

Não usa dado real, secret, runtime real, PSP real ou real_apply.

### 2.5 Admin interno

Superfície isolada, invisível ao cliente.

Usada para diagnóstico, auditoria e suporte futuro.

### 2.6 Canais auxiliares

WhatsApp, e-mail e push podem avisar, mas não devem ser control-plane.

Decisão sensível sempre volta para o Workspace.

---

## 3. Modos de negócio

### Modo A — Dono-Solo

Baseline.

Perfil:

* uma pessoa cuida de tudo;
* mobile-first;
* zero TI;
* pouco tempo;
* alta sensibilidade a complexidade.

Telas:

* Hoje;
* Automações;
* Aprovar;
* Histórico;
* Configurações.

Critério central:

* primeira automação segura em até 3–5 minutos.

### Modo B — Dono + ajudante

Adiciona:

* tela mínima de equipe;
* permissões simples;
* dono aprova ações sensíveis;
* ajudante acompanha/operacionaliza.

Critério:

* delegar uma tarefa simples em até 3 minutos.

### Modo C — Equipe pequena

Adiciona:

* papéis básicos;
* gerente;
* operador;
* financeiro;
* viewer;
* aprovação em cadeia curta.

Critério:

* cadeia de aprovação com no máximo 3 passos.

### Modo D — Operação maior

Adiciona:

* RBAC avançado;
* multiunidade;
* auditoria;
* SSO/SAML futuro;
* compliance;
* relatórios avançados.

Observação:

* entra como disclosure/pós-Bedrock, não como baseline.

---

# ROADMAP FINAL BENCHUIX

---

# BLOCO 0 — Fundação da camada

## BENCHUIX-00 — Charter & Anti-escopo

**Objetivo:** definir oficialmente o que BenchUIX valida e o que ela não autoriza.

**Pergunta principal:** quais limites impedem BenchUIX de virar produto prematuro?

**Escopo:**

* charter da camada;
* anti-escopo;
* transition table 00→27;
* regra anti-phase-null;
* definição de artifacts;
* critérios de PASS/WARN/BLOCK/INVALID.

**Fora de escopo:**

* produto real;
* runtime real;
* real_apply;
* cliente real;
* Bedrock;
* secrets;
* deploy de produção.

**Artifacts:**

* `benchuix_charter.md`
* `benchuix_research_source_ledger.json`
* `benchuix_transition_table_candidate.json`

**Critério de saída:**

* escopo e anti-escopo explícitos;
* todas as fases com próximo passo definido;
* produto/Bedrock/real_apply/secrets bloqueados.

**Próxima fase:** BENCHUIX-01

---

## BENCHUIX-01 — Dono-Solo & Modos de Negócio

**Objetivo:** fixar o dono-solo como baseline da experiência.

**Pergunta principal:** o ARIS funciona para uma pessoa que cuida de tudo sozinha?

**Escopo:**

* persona dono-solo;
* modos A/B/C/D;
* matriz de progressive disclosure;
* limitações cognitivas;
* linguagem recomendada;
* complexidade escondida.

**Fora de escopo:**

* enterprise-first;
* SSO;
* compliance avançado;
* papéis complexos no baseline.

**Artifacts:**

* `benchuix_owner_solo_mode_spec.md`
* `benchuix_business_modes_matrix.json`

**Critério de saída:**

* Modo A completo;
* B/C/D apenas adicionam complexidade;
* nenhuma tela básica exige jargão técnico.

**Próxima fase:** BENCHUIX-02

---

## BENCHUIX-02 — Modelo de Acesso & Superfícies

**Objetivo:** definir como o cliente acessa o ARIS.

**Pergunta principal:** onde o cliente entra, decide, vê evidência e acompanha operação?

**Escopo:**

* Client Workspace;
* mobile companion;
* landing;
* demo sandbox;
* admin interno;
* canais auxiliares;
* fronteiras de isolamento.

**Fora de escopo:**

* app nativo inicial;
* decisão sensível por WhatsApp/e-mail;
* admin visível ao cliente;
* runtime real.

**Artifacts:**

* `benchuix_access_model.md`
* `benchuix_surface_inventory.json`
* `benchuix_surfaces_diagram.mmd`

**Critério de saída:**

* 6 superfícies separadas;
* canais auxiliares sem control-plane;
* admin isolado.

**Próxima fase:** BENCHUIX-03

---

## BENCHUIX-03 — Design System & Tokens

**Objetivo:** criar a fundação visual e interativa do ARIS.

**Pergunta principal:** a UI é consistente, controlável, acessível e preparada para risco/estado?

**Escopo:**

* design tokens em 3 níveis;
* reference tokens;
* system tokens;
* component tokens;
* dark/light por remap;
* estados;
* grid;
* spacing;
* tipografia;
* motion restrito;
* reduced motion;
* componentes básicos;
* tokens semânticos de governança.

**Fora de escopo:**

* congelar paleta final;
* branding comercial final;
* UI fora do design system.

**Artifacts:**

* `benchuix_design_system_spec.md`
* `benchuix_design_tokens_candidate.json`
* `benchuix_component_inventory.json`

**Critério de saída:**

* tema troca por remap;
* zero cor hardcoded em componente;
* todo componente possui empty/loading/error/success/degraded;
* motion essencial possui fallback.

**Próxima fase:** BENCHUIX-04

---

## BENCHUIX-04 — Service Blueprint

**Objetivo:** mapear frontstage, backstage e evidência por fluxo.

**Pergunta principal:** o que o cliente vê e o que ARIS faz por trás?

**Escopo:**

* raia do cliente;
* frontstage;
* backstage;
* suporte;
* evidência;
* falhas;
* timeouts;
* modo degradado.

**Fora de escopo:**

* implementação de runtime;
* webhooks reais;
* integrações reais.

**Artifacts:**

* `benchuix_service_blueprint.md`
* `benchuix_journey_maps.md`

**Critério de saída:**

* todo touchpoint tem backstage e evidência;
* toda jornada crítica inclui falha/timeout;
* nenhum fluxo sem dono.

**Próxima fase:** BENCHUIX-05

---

# BLOCO 1 — Entrada e ativação

## BENCHUIX-05 — Primeiro Minuto & Tela “Hoje”

**Objetivo:** definir a primeira experiência do cliente.

**Pergunta principal:** o dono entende em segundos o que o ARIS faz por ele hoje?

**Escopo:**

* tela “Hoje”;
* resumo operacional;
* aprovações pendentes;
* alertas;
* próximos passos;
* dados sintéticos no protótipo;
* regra dos 5 segundos.

**Fora de escopo:**

* dashboard avançado;
* métricas complexas;
* visão corporativa inicial.

**Artifacts:**

* `benchuix_hoje_spec.md`
* `benchuix_today_summary_card_spec.json`

**SLO:**

* tela útil em até 2s;
* LCP ≤ 2,5s p75 mobile;
* principal mensagem compreendida em até 5s.

**Critério de saída:**

* cliente entende estado atual;
* ação principal é óbvia;
* nenhuma informação crítica escondida.

**Próxima fase:** BENCHUIX-06

---

## BENCHUIX-06 — Onboarding em até 3 minutos

**Objetivo:** levar o dono à primeira simulação segura rapidamente.

**Pergunta principal:** o cliente chega ao primeiro valor sem cadastro longo?

**Escopo:**

* tipo de negócio;
* objetivo principal;
* canais usados;
* escolha de template;
* primeira simulação;
* sem reentrada de dados.

**Fora de escopo:**

* onboarding corporativo;
* billing;
* integração real;
* OAuth real.

**Artifacts:**

* `benchuix_onboarding_spec.md`
* `benchuix_time_to_first_preview_protocol.json`

**SLO:**

* primeira simulação em até 3 minutos;
* nenhum campo repetido.

**Critério de saída:**

* onboarding curto;
* valor antes de configuração profunda;
* primeiro preview sem dado real.

**Próxima fase:** BENCHUIX-07

---

## BENCHUIX-07 — Perfil do Negócio

**Objetivo:** criar o contexto mínimo do negócio.

**Pergunta principal:** quais dados mínimos permitem automação segura e útil?

**Escopo:**

* tipo de negócio;
* horário;
* canais;
* serviços/produtos;
* objetivos;
* permissões default;
* auto-save;
* perfil incremental.

**Fora de escopo:**

* cadastro extenso;
* billing;
* dados reais obrigatórios;
* integrações reais.

**Artifacts:**

* `benchuix_business_profile_form.json`
* `benchuix_business_profile_spec.md`

**Critério de saída:**

* até 3 campos iniciais;
* todo campo possui justificativa;
* auto-save preserva dados;
* default seguro por modo.

**Próxima fase:** BENCHUIX-08

---

## BENCHUIX-08 — Playbooks por Vertical

**Objetivo:** criar automações iniciais por tipo de negócio.

**Pergunta principal:** o cliente começa com atalhos úteis ou do zero?

**Escopo:**

* barbearia;
* loja;
* mercado;
* escritório;
* agência;
* clínica/serviço;
* playbooks de baixo risco;
* teto;
* timeout;
* “vai fazer / não vai fazer”.

**Fora de escopo:**

* automações reais;
* ação sensível sem aprovação;
* playbook sem limite.

**Artifacts:**

* `benchuix_playbooks_catalog.md`
* `benchuix_vertical_template_matrix.json`

**Critério de saída:**

* mínimo 5 playbooks por vertical;
* todo playbook com limite e “não vai fazer”;
* todo playbook de escrita aponta para Approval Card.

**Próxima fase:** BENCHUIX-09

---

# BLOCO 2 — Núcleo de confiança

## BENCHUIX-09 — Automation Studio Simples

**Objetivo:** permitir criação de automação sem grafo técnico.

**Pergunta principal:** o dono cria automação sem entender trigger/action/schema?

**Escopo:**

* linguagem natural;
* seleção assistida;
* proposta type-safe;
* editar;
* duplicar;
* pausar;
* revisar plano.

**Fora de escopo:**

* editor visual de nós;
* DAG técnico;
* schema visível;
* runtime visível.

**Artifacts:**

* `benchuix_automation_editor.md`
* `benchuix_create_automation_flow.json`

**Critério de saída:**

* dono-solo cria automação simples sem treinamento;
* nenhuma criação expõe jargão técnico;
* toda automação possui teto e tipo validado.

**Próxima fase:** BENCHUIX-10

---

## BENCHUIX-10 — Preview / Simulação

**Objetivo:** mostrar o que aconteceria antes de fazer.

**Pergunta principal:** o preview é 100% sem side-effect?

**Escopo:**

* simulação determinística;
* diff antes/depois;
* impacto esperado;
* risco;
* custo estimado;
* evidência esperada;
* prova de isolamento.

**Fora de escopo:**

* tocar dado real;
* chamar serviço real;
* executar ação real;
* mutar estado.

**Artifacts:**

* `benchuix_simulation_spec.md`
* `benchuix_isolation_proof.md`

**SLO:**

* preview simples em até 3s;
* feedback visível se passar de 1s.

**Critério de saída:**

* zero side-effects;
* preview compreensível;
* se tocar estado real, vira gap para Crisol.

**Próxima fase:** BENCHUIX-11

---

## BENCHUIX-11 — Approval Inbox

**Objetivo:** transformar governança em aprovação compreensível.

**Pergunta principal:** o dono aprova sabendo exatamente o que vai e não vai acontecer?

**Escopo:**

* inbox de aprovações;
* risco;
* permissão;
* limite;
* custo;
* latência;
* “vai fazer”;
* “não vai fazer”;
* aprovar;
* negar;
* editar;
* simular.

**Fora de escopo:**

* aprovação por canal externo;
* aprovação genérica;
* “tem certeza?” vazio;
* desligar aprovação sensível.

**Artifacts:**

* `benchuix_approval_inbox_spec.md`
* `benchuix_risk_taxonomy.json`
* `benchuix_permission_language_matrix.json`

**SLO:**

* abrir inbox ≤ 500ms;
* feedback após toque ≤ 100ms.

**Critério de saída:**

* toda ação sensível mostra vai/não vai;
* risco não depende só de cor;
* approval não é removível pelo usuário final.

**Próxima fase:** BENCHUIX-12

---

## BENCHUIX-12 — Estados de Execução

**Objetivo:** garantir visibilidade contínua de estado.

**Pergunta principal:** existe algum estado ambíguo?

**Escopo:**

* rascunho;
* aguardando aprovação;
* agendado;
* rodando;
* aguardando dados;
* concluído;
* falhou;
* parcial;
* rollback disponível;
* desfeito;
* pausado.

**Fora de escopo:**

* estado invisível;
* sucesso falso;
* falha escondida.

**Artifacts:**

* `benchuix_execution_state_machine.json`
* `benchuix_state_microcopy_matrix.json`

**Critério de saída:**

* todo estado tem token, texto e representação visual;
* nenhum estado crítico é ambíguo;
* idade do dado é visível.

**Próxima fase:** BENCHUIX-13

---

## BENCHUIX-13 — Tela Automações

**Objetivo:** mostrar o que está ativo, pausado, falhou ou pede atenção.

**Pergunta principal:** o dono sabe o que está rodando e consegue pausar sem medo?

**Escopo:**

* lista de automações;
* status;
* próxima execução;
* última execução;
* pausar;
* editar;
* histórico;
* erro visível.

**Fora de escopo:**

* DAG técnico;
* logs brutos;
* alteração sem auditoria.

**Artifacts:**

* `benchuix_automations_list_spec.md`

**SLO:**

* desativação refletida em até 2s.

**Critério de saída:**

* automações aparecem como frases do negócio;
* falha é visível;
* alteração é auditada.

**Próxima fase:** BENCHUIX-14

---

## BENCHUIX-14 — Histórico / Comprovantes

**Objetivo:** transformar ledger em recibo legível.

**Pergunta principal:** o dono entende o que aconteceu sem ajuda técnica?

**Escopo:**

* histórico;
* comprovantes;
* código de verificação;
* busca;
* exportação;
* permissão usada;
* custo;
* resultado;
* link para rollback.

**Fora de escopo:**

* stack trace;
* hash visível como termo primário;
* editar/apagar recibo antigo.

**Artifacts:**

* `benchuix_history_ledger_spec.md`
* `benchuix_evidence_receipt_spec.md`

**SLO:**

* busca em comprovantes ≤ 1,5s;
* abrir recibo ≤ 200ms.

**Critério de saída:**

* recibo legível por não-técnico;
* verificável;
* imutável;
* sem jargão.

**Próxima fase:** BENCHUIX-15

---

## BENCHUIX-15 — Rollback / Desfazer / Compensar

**Objetivo:** explicar e executar a noção de desfazer com honestidade.

**Pergunta principal:** o dono sabe antes se pode desfazer?

**Escopo:**

* reversível;
* compensável;
* irreversível;
* razão;
* impacto;
* confirmação reforçada;
* ação destrutiva;
* evidência do rollback.

**Fora de escopo:**

* prometer desfazer side-effect irreversível;
* rollback duplicável;
* rollback sem limite.

**Artifacts:**

* `benchuix_rollback_spec.md`
* `benchuix_recovery_decision_tree.json`

**Critério de saída:**

* toda ação declara se pode desfazer;
* cannot-undo mostra razão e compensação;
* side-effect irreversível vai para Crisol.

**Próxima fase:** BENCHUIX-16

---

# BLOCO 3 — Resiliência, acesso e segurança visível

## BENCHUIX-16 — Falhas & Modo Degradado

**Objetivo:** tornar falhas compreensíveis e seguras.

**Pergunta principal:** toda falha mostra causa, impacto e próximo passo?

**Escopo:**

* rede indisponível;
* timeout;
* dado ausente;
* permissão insuficiente;
* execução parcial;
* evidência falhou;
* estado stale;
* modo degradado;
* re-sync.

**Fora de escopo:**

* tela branca;
* spinner infinito;
* stack trace para cliente;
* falha sem ação.

**Artifacts:**

* `benchuix_failure_library.md`
* `benchuix_degraded_mode_spec.md`

**SLO:**

* aviso de degradado ≤ 300ms;
* banner de falha ≤ 300ms.

**Critério de saída:**

* toda falha explica impacto;
* sempre há próxima ação;
* estado seguro por padrão.

**Próxima fase:** BENCHUIX-17

---

## BENCHUIX-17 — Mobile Companion / PWA

**Objetivo:** adaptar ARIS ao uso real no celular.

**Pergunta principal:** aprovar e entender no celular funciona sem atrito?

**Escopo:**

* PWA;
* aprovar;
* recusar;
* alerta;
* status;
* comprovante;
* pausar;
* tela Hoje;
* service worker;
* política de cache.

**Fora de escopo:**

* app nativo;
* approval de cache stale;
* ação essencial apenas por gesto.

**Artifacts:**

* `benchuix_mobile_companion_spec.md`
* `benchuix_pwa_cache_policy.json`

**SLO:**

* first paint ≤ 1,5s;
* feedback de toque ≤ 100ms;
* degradado mobile ≤ 300ms.

**Critério de saída:**

* aprovação nunca renderiza de cache obsoleto;
* alvos ≥ 24x24px;
* uso sem zoom.

**Próxima fase:** BENCHUIX-18

---

## BENCHUIX-18 — Permissões Progressivas

**Objetivo:** mostrar limites sem parecer sistema corporativo.

**Pergunta principal:** o default é o menor privilégio útil?

**Escopo:**

* least privilege;
* “ARIS pode”;
* “ARIS não pode”;
* papéis por modo;
* limites por ação;
* suspensão de acesso.

**Fora de escopo:**

* god-mode;
* privilégio amplo por conveniência;
* enforcement client-side.

**Artifacts:**

* `benchuix_permissions_matrix.json`
* `benchuix_role_based_views.md`

**SLO:**

* remover/suspender acesso ≤ 3s.

**Critério de saída:**

* default é menor privilégio;
* limites são entendíveis;
* nenhum bypass por UI.

**Próxima fase:** BENCHUIX-19

---

## BENCHUIX-19 — Dashboard Operacional Avançado

**Objetivo:** criar command center sem poluir o modo simples.

**Pergunta principal:** o dashboard ajuda decisão ou vira ruído?

**Escopo:**

* KPIs úteis;
* aprovações;
* execuções;
* falhas;
* evidências;
* risco;
* custo;
* tempo economizado;
* saúde;
* warnings;
* audit trail;
* modo avançado.

**Fora de escopo:**

* vanity metrics;
* travar thread;
* dashboard como primeira experiência do dono-solo.

**Artifacts:**

* `benchuix_advanced_dashboard_spec.md`
* `benchuix_dashboard_widget_inventory.json`

**SLO:**

* dashboard avançado ≤ 600ms;
* mensagem principal em ≤ 5s.

**Critério de saída:**

* todo KPI tem ação associada;
* simples e avançado separados;
* sem travamento de UI.

**Próxima fase:** BENCHUIX-20

---

## BENCHUIX-20 — Microcopy & Trust Language

**Objetivo:** traduzir segurança e governança para linguagem humana.

**Pergunta principal:** todo risco é explicado sem jargão?

**Escopo:**

* termos proibidos;
* traduções;
* mensagens de risco;
* mensagens de falha;
* mensagens de permissão;
* mensagens de rollback;
* mensagens de comprovante.

**Fora de escopo:**

* runtime;
* gate;
* schema;
* artifact;
* ledger;
* tenant;
* idempotency;
* active-context;
* hash como termo primário.

**Artifacts:**

* `benchuix_ux_copy_system.md`
* `benchuix_forbidden_terms.txt`

**Critério de saída:**

* jargon-scan = 0;
* todo conceito técnico possui tradução;
* segurança não depende de jargão.

**Próxima fase:** BENCHUIX-21

---

## BENCHUIX-21 — Acessibilidade WCAG 2.2 AA

**Objetivo:** garantir uso real por pessoas reais em condições reais.

**Pergunta principal:** fluxos críticos funcionam por teclado, mobile e leitor de tela?

**Escopo:**

* foco visível;
* target size;
* teclado;
* labels;
* mensagens de status;
* help consistente;
* autenticação acessível;
* reduced motion como meta.

**Fora de escopo:**

* ação crítica só por mouse;
* decisão só por cor;
* fluxo essencial inacessível.

**Artifacts:**

* `benchuix_accessibility_wcag22_mapping.json`
* `benchuix_accessibility_audit_report.md`

**Critério de saída:**

* 100% AA aplicável em fluxo essencial;
* zero violação crítica;
* decisão operacional sem depender só de cor.

**Próxima fase:** BENCHUIX-22

---

## BENCHUIX-22 — Visual QA & Performance Budget

**Objetivo:** garantir que experiência e performance sejam mensuráveis.

**Pergunta principal:** o ARIS é rápido no mobile realista?

**Escopo:**

* Core Web Vitals;
* LCP;
* INP;
* CLS;
* TTFB;
* FCP;
* TBT;
* bundle budget;
* visual regression;
* estados;
* temas;
* p75 mobile.

**Fora de escopo:**

* média desktop como prova;
* performance sem raw data;
* Lighthouse PWA score como gate.

**Artifacts:**

* `benchuix_performance_slo_matrix.json`
* `benchuix_visual_regression_report.md`
* `benchuix_web_vitals_report.md`

**SLO:**

* LCP ≤ 2,5s;
* INP ≤ 200ms;
* CLS ≤ 0,1;
* critical path < 170KB;
* bundle < 250KB;
* TTI < 5s em 3G.

**Critério de saída:**

* SLOs passam no p75 mobile;
* todos os estados visualmente testados;
* SLO sem método = INVALID.

**Próxima fase:** BENCHUIX-23

---

# BLOCO 4 — Prova, comparação e fechamento

## BENCHUIX-23 — Benchmark Competitivo por Tarefa

**Objetivo:** comparar ARIS contra mercado em tarefas reais.

**Pergunta principal:** onde ARIS ganha, perde ou deve aprender?

**Escopo:**

* onboarding;
* criação;
* preview;
* aprovação;
* risco;
* evidência;
* rollback;
* falha;
* mobile;
* auditoria;
* dashboard;
* demo.

**Fora de escopo:**

* feature-list superficial;
* concorrente sem fonte;
* marketing comparativo.

**Artifacts:**

* `benchuix_competitive_task_matrix.md`
* `benchuix_competitor_source_ledger.json`

**Critério de saída:**

* toda comparação tem tarefa e fonte;
* todo achado tem implicação para ARIS;
* todo gap tem destino.

**Próxima fase:** BENCHUIX-24

---

## BENCHUIX-24 — Métricas BenchUIX / HEART Scorecard

**Objetivo:** transformar UX/UI em avaliação mensurável.

**Pergunta principal:** cada métrica responde a uma decisão de produto?

**Escopo:**

* time-to-first-value;
* time-to-first-safe-automation;
* task success;
* confidence-to-approve;
* evidence comprehension;
* rollback comprehension;
* anxiety reduction;
* ability-to-explain;
* mobile usability;
* accessibility pass;
* performance pass;
* preference vs competitor.

**Fora de escopo:**

* vanity metrics;
* engagement como valor por si;
* métrica sem método.

**Artifacts:**

* `benchuix_metrics_scorecard.json`
* `benchuix_measurement_plan.md`

**Critério de saída:**

* toda métrica tem meta, sinal, método, threshold e artifact;
* thresholds calibráveis são marcados como tal;
* sem raw data = INVALID.

**Próxima fase:** BENCHUIX-25

---

## BENCHUIX-25 — Protocolo de Teste de Usabilidade

**Objetivo:** provar que pessoas realistas conseguem usar.

**Pergunta principal:** o dono-solo executa tarefas críticas sem explicação técnica?

**Escopo:**

* perfis simulados/usuários futuros;
* barbearia;
* loja;
* mercado;
* escritório;
* agência;
* pessoa ansiosa com automação;
* mobile 4G;
* dados sintéticos.

**Tarefas:**

* entender Hoje;
* criar automação;
* simular;
* aprovar;
* achar comprovante;
* entender falha;
* pausar;
* entender o que ARIS não fará;
* ver se pode desfazer;
* explicar ARIS.

**Artifacts:**

* `benchuix_usability_test_protocol.md`
* `benchuix_task_success_matrix.json`
* `benchuix_usability_severity_rubric.json`

**Critério de saída:**

* protocolo executável;
* tarefas críticas definidas;
* dados sintéticos;
* sem narrativa como prova.

**Próxima fase:** BENCHUIX-26

---

## BENCHUIX-26 — Demo Sandbox de 2 Minutos

**Objetivo:** demonstrar valor sem explicar arquitetura.

**Pergunta principal:** ARIS mostra entender → usar → confiar → evidência → rollback em até 2 minutos?

**Escopo:**

* barbearia;
* mercado;
* escritório;
* dados sintéticos;
* roteiro fechado;
* sandbox;
* sem tocar estado real.

**Demos mínimas:**

1. Barbearia: bloqueio fora de horário + exceção VIP aprovada.
2. Mercado: reembolso suspeito recusado com evidência.
3. Escritório: prompt-injection em anexo interceptado.

**Fora de escopo:**

* demo com dado real;
* real_apply;
* secret;
* explicação arquitetural longa.

**Artifacts:**

* `benchuix_demo_scripts.md`
* `benchuix_demo_sandbox_spec.md`

**Critério de saída:**

* demo ≤ 2min;
* sem tocar estado real;
* valor claro;
* comprovante visível.

**Próxima fase:** BENCHUIX-27

---

## BENCHUIX-27 — Product Gap Ledger & Handoff Crisol

**Objetivo:** fechar BenchUIX e entregar gaps para Crisol.

**Pergunta principal:** todo problema tem destino e critério de fechamento?

**Escopo:**

* product gap ledger;
* anti-theater rules;
* handoff para Crisol;
* design system;
* blueprint;
* state machine;
* benchmark;
* metrics scorecard;
* demo sandbox;
* copy system.

**Fora de escopo:**

* aceitar secret/real_apply/runtime como risco aceito;
* fechar gap sem destino;
* declarar produto pronto.

**Artifacts:**

* `benchuix_product_gap_ledger.json`
* `benchuix_anti_theater_rules.json`
* `benchuix_crisol_handoff.md`

**Critério de saída:**

* todo gap tem destino;
* gaps de runtime vão para Crisol;
* secrets/produção/real_apply vão para Bedrock;
* cosméticos podem virar accepted-risk;
* next_phase aponta para Crisol.

**Próxima fase:** CRISOL

---

# 4. Gates absolutos pré-Bedrock

Qualquer item aberto abaixo bloqueia handoff para Bedrock:

1. Tela “Hoje” sem dado operacional.
2. Aprovação sem “vai fazer / não vai fazer”.
3. Recibo sem verificabilidade e sem linguagem de cliente.
4. Rollback sem limite e impacto.
5. UI com jargão técnico.
6. Core Web Vitals ausentes ou estourados no p75 mobile.
7. Falha de rede sem modo degradado.
8. Onboarding sem primeira simulação segura em 3–5 minutos.
9. Preview tocando estado real.
10. Demo que exige explicação arquitetural.
11. Benchmark sem tarefa real.
12. Métrica sem raw data.
13. Ação sensível sem confirmação explícita.
14. Admin interno acessível ao cliente.
15. Aprovação renderizada de cache obsoleto.

---

# 5. Anti-theater rules

## INVALID

* benchmark sem tarefa real;
* UX sem dono-solo;
* UI bonita sem fluxo completo;
* design system sem estados de erro/falha/degraded;
* performance sem medição mobile;
* Core Web Vitals ausentes;
* métrica sem raw data;
* SLO sem método de medição;
* PASS sem artifact/hash/CI;
* persona sem fonte;
* componente fora do design system.

## BLOCK

* segurança que depende de jargão;
* aprovação sem “vai fazer / não vai fazer”;
* evidência que só engenheiro entende;
* rollback sem explicar limites;
* demo que exige arquitetura;
* preview que toca estado real;
* secret ou log técnico em tela do cliente;
* rollback com reexecução duplicável;
* real_apply dentro da camada;
* produto real antes de Bedrock.

## WARN

* concorrente citado com fonte fraca;
* alert fatigue;
* formulário longo sem teste de abandono;
* KPI sem baseline;
* risco mostrado só por cor;
* token sem nome semântico.

---

# 6. Artifact set final

* `benchuix_charter.md`
* `benchuix_research_source_ledger.json`
* `benchuix_transition_table_candidate.json`
* `benchuix_owner_solo_mode_spec.md`
* `benchuix_business_modes_matrix.json`
* `benchuix_access_model.md`
* `benchuix_surface_inventory.json`
* `benchuix_design_system_spec.md`
* `benchuix_design_tokens_candidate.json`
* `benchuix_component_inventory.json`
* `benchuix_service_blueprint.md`
* `benchuix_journey_maps.md`
* `benchuix_hoje_spec.md`
* `benchuix_onboarding_spec.md`
* `benchuix_business_profile_form.json`
* `benchuix_playbooks_catalog.md`
* `benchuix_automation_editor.md`
* `benchuix_simulation_spec.md`
* `benchuix_isolation_proof.md`
* `benchuix_approval_inbox_spec.md`
* `benchuix_risk_taxonomy.json`
* `benchuix_execution_state_machine.json`
* `benchuix_automations_list_spec.md`
* `benchuix_history_ledger_spec.md`
* `benchuix_evidence_receipt_spec.md`
* `benchuix_rollback_spec.md`
* `benchuix_failure_library.md`
* `benchuix_mobile_companion_spec.md`
* `benchuix_permissions_matrix.json`
* `benchuix_advanced_dashboard_spec.md`
* `benchuix_ux_copy_system.md`
* `benchuix_accessibility_wcag22_mapping.json`
* `benchuix_performance_slo_matrix.json`
* `benchuix_visual_regression_report.md`
* `benchuix_competitive_task_matrix.md`
* `benchuix_metrics_scorecard.json`
* `benchuix_usability_test_protocol.md`
* `benchuix_demo_scripts.md`
* `benchuix_product_gap_ledger.json`
* `benchuix_anti_theater_rules.json`
* `benchuix_crisol_handoff.md`

---

# 7. Resultado esperado da camada

Ao final da BenchUIX, o ARIS ainda não é produto, mas deve ter provado:

1. o dono-solo entende o ARIS;
2. o dono-solo cria primeira automação segura;
3. o dono-solo aprova sabendo o que vai e não vai acontecer;
4. o dono encontra comprovante;
5. o dono entende falha;
6. o dono sabe pausar/desfazer quando possível;
7. o ARIS responde rápido no mobile;
8. a UI é acessível;
9. a UI não usa jargão técnico;
10. a experiência é comparada contra concorrentes por tarefa;
11. o design system cobre estados reais;
12. a demo mostra valor em 2 minutos;
13. todo gap tem destino;
14. Crisol recebe pacote de consolidação.

---

# 8. Transição final

```text
BENCHUIX-00
→ BENCHUIX-01
→ BENCHUIX-02
→ BENCHUIX-03
→ BENCHUIX-04
→ BENCHUIX-05
→ BENCHUIX-06
→ BENCHUIX-07
→ BENCHUIX-08
→ BENCHUIX-09
→ BENCHUIX-10
→ BENCHUIX-11
→ BENCHUIX-12
→ BENCHUIX-13
→ BENCHUIX-14
→ BENCHUIX-15
→ BENCHUIX-16
→ BENCHUIX-17
→ BENCHUIX-18
→ BENCHUIX-19
→ BENCHUIX-20
→ BENCHUIX-21
→ BENCHUIX-22
→ BENCHUIX-23
→ BENCHUIX-24
→ BENCHUIX-25
→ BENCHUIX-26
→ BENCHUIX-27
→ CRISOL
```

**Nenhuma fase com PASS termina em `null`.**

---

# 9. Frase final da camada

BenchUIX não prova que ARIS está pronto para vender.

BenchUIX prova que o ARIS foi desenhado para ser:

```text
compreensível,
simples,
rápido,
seguro,
confiável,
auditável,
demonstrável,
comparável,
e preparado para consolidação.
```

Produto real continua dependendo de:

```text
Crisol
→ Polimento
→ EXT-SEC 00→04
→ Cinzel
→ EXT-SEC 05→06
→ Bedrock
```
