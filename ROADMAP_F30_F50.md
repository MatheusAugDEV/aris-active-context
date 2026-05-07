# ROADMAP ARIS F30-F50

## Diretrizes gerais

O roadmap seguirá a sequência operacional F30, F31, F32 em diante.

Cada fase terá nome específico, escopo delimitado, etapas internas A/B/C/D e critério objetivo de validação.

Cada commit, artifact, documento, teste, runner e atualização de contexto deve conter a tag da fase correspondente, por exemplo: [F30.B], [F34.C], [F48.D].

Todo prompt Codex deve exigir atualização final do active-context, incluindo CURRENT_STATE.md, NEXT_ACTION.md, ARIS_PHASE_LEDGER.md e, quando aplicável, DECISION_LOCKS.md, CONTEXT_INDEX.md e README.md, com commit, push e hash final.

Ficam fora de escopo neste ciclo:
demo comercial, produto, SaaS, marketplace, enterprise real, multi-tenant real, cloud stack pesada, shell livre, browser automation real, email real, plugin externo não auditado, GraphRAG pesado, vector obrigatório e qualquer ação sem gate, ledger e rollback.

Sem demo.

## Princípios técnicos obrigatórios

### 1. Execução agnóstica de provedor

Entre F36 e F40, máquina de estados, automações, skills e capabilities devem usar schemas neutros, mock adapters e contratos independentes de provider.

Nenhum parser deve ser acoplado ao formato nativo de Claude, OpenAI, Gemini, Groq ou outro provedor antes da F41.

### 2. Rollback local por Saga e compensação

Toda mutação local deve registrar path absoluto normalizado, hash antes/depois, tamanho antes/depois, permissões antes/depois, operação aplicada, operação compensatória e estado de rollback.

File-ops devem priorizar staging e operação atômica quando aplicável.

### 3. Baseline inicial de avaliação

Antes de alterações profundas em contexto, memória ou resposta, deve existir uma linha mínima de regressão.

A F43 expandirá essa base para um laboratório completo de avaliação e confiabilidade.

### 4. Fronteira de confiança

O ARIS deve bloquear combinações inseguras entre dados privados, conteúdo não confiável e comunicação externa sem gate explícito.

### 5. Controle de memória

A memória local deve possuir TTL, stale detection, summarization, eviction e tratamento de conflito entre fatos antigos e novos.

### 6. Pente Fino sem novas features

A F48 é exclusivamente diagnóstico, varredura, correção crítica e plano de reparo.

Não deve adicionar novas funcionalidades.

## F30 — Roadmap & Phase Hygiene

Objetivo:
organizar nomenclatura, fases, artifacts e linguagem operacional.

Etapas:
F30.A — Historical-to-Canonical Mapping.
F30.B — Official Phase Naming Cleanup.
F30.C — Artifact, Warning & Residual Risk Index.
F30.D — Roadmap Publication Gate.

Validação:
active-context, ledger e roadmap sem referências operacionais conflitantes.

## F31 — Source-of-Truth & Artifact Hygiene

Objetivo:
inventariar fontes, artifacts, hashes, metadata, warning registry e rastreabilidade.

Validação:
consistência comprovada após simulação de falha, divergência ou tampering.

## F32 — Context Boundary, Obsidian/MCP & Trust Firewall

Objetivo:
separar contexto confiável e não confiável, reforçar Obsidian query-first/read-only, MCP controlado, prompt-injection gate e lethal-trifecta gate.

Validação:
prompt injection indireto bloqueado e registrado; trust-boundary lint funcional.

## F33 — SQLite Memory, FTS5 & Evaluation Baseline

Objetivo:
consolidar memória operacional em SQLite/FTS5, com baseline de avaliação, eviction e summarization.

Validação:
retrieval correto, memória obsoleta/conflitante classificada e banco sem degradação indefinida.

## F34 — Action Ledger, Concurrency & Rollback

Objetivo:
implementar ledger append-only, hash chain, atomic write, locking, Saga, compensating transactions e rollback testável.

Validação:
falhas simuladas preservam consistência e toda ação com efeito colateral possui compensação registrada antes da execução.

## F35 — Optional Vector & Semantic Layer

Objetivo:
avaliar sqlite-vec ou LanceDB apenas se houver ganho real sobre FTS5.

Validação:
ganho comprovado em casos reais ou decisão formal de adiamento.

## F36 — Lightweight State Machine & Human-in-the-Loop

Objetivo:
definir estados explícitos, approval flow, checkpoint, interrupt/resume, timeout, replay, crash recovery e kill-switch.

Validação:
aprovação executa, negação aborta, timeout mantém segurança e replay é auditável.

## F37 — Sidecar Sandbox & Isolation Boundary

Objetivo:
definir isolamento leve antes de automações e skills, bloqueando rede, segredos, paths sensíveis e execução direta no host.

Validação:
tentativa maliciosa confinada, host preservado e segredos inacessíveis.

## F38 — Capability Handles & Skill Governance

Objetivo:
definir capabilities, SkillCandidate schema, trust tier, denylist, manifests e vínculo com sandbox/ledger.

Validação:
capability não autorizada bloqueada; capability autorizada registrada com perfil de sandbox.

## F39 — Consolidated Local Automation Suite

Objetivo:
unificar notes, calendar e file-ops com dry-run, permission gate, capability, sandbox, ledger e rollback.

Validação:
cada automação é reversível em falha simulada e toda operação fora do contrato é bloqueada.

## F40 — External Security & Privacy

Objetivo:
cobrir prompt injection, secrets, dependências, SBOM, licenças, copyright, privacy checklist e supply-chain.

Validação:
auditoria sem vazamento de credenciais, bypass crítico ou dependência sem rastreio.

## F41 — Multi-Provider Model Gateway & Cost Control

Objetivo:
criar contrato único para Groq, OpenAI, Claude, Gemini e perfil local, com fallback, budget, health, redaction e circuit breaker.

Validação:
fallback funcional, budget respeitado e bloqueio contra resource amplification.

## F42 — Response Engine 2.0

Objetivo:
garantir respostas completas, factuais, não truncadas, bem formatadas, com fallback honesto, output safety e planner/executor boundary.

Validação:
respostas passam testes de completude, factualidade, renderização e proteção contra conteúdo não confiável.

## F43 — Evaluation, Reliability & Benchmark Lab

Objetivo:
expandir golden suites, regression matrix, métricas de latência, custo, failure scenarios e reliability score.

Validação:
metas mínimas atingidas, regressões detectadas e falhas classificadas.

## F44 — Operational Cockpit & Internal UI

Objetivo:
criar UI/TUI local para estado, logs, custos, warnings, traces, ledger, play/pause/stop e intervenção humana.

Validação:
painel mostra estado real e bloqueia acesso ou ação indevida.

## F45 — Rich Output & Document Intelligence

Objetivo:
suportar tabelas, cards, markdown seguro, artifact viewer, PDF/OCR controlado e anexos seguros.

Validação:
documentos extraídos com precisão, saídas renderizadas com segurança e anexos tratados como untrusted.

## F46 — Voice Safety & Multimodal Boundary

Objetivo:
reforçar wake word, readback, confirmação verbal, transcript safety, fallback textual e modos multimodais explícitos.

Validação:
comando malicioso por áudio bloqueado, modo multimodal explícito e fallback seguro em falha de áudio.

## F47 — Local Packaging & Recovery

Objetivo:
criar empacotamento local, healthcheck, low-RAM profile, dependency diagnostics, restart/recovery e backup/restore.

Validação:
execução em hardware modesto, recuperação após crash e diagnóstico de dependências ausentes.

## F48 — Pente Fino — Full ARIS System Sweep

Objetivo:
testar e auditar o ARIS inteiro: voz, respostas, contexto, memória, UI, actions, sandbox, ledger, rollback, providers, artifacts, segurança, reliability e packaging.

Validação:
casos críticos passam; falhas graves viram blockers ou plano de reparo.

## F49 — External Audit & Internal Technical Readiness

Objetivo:
submeter pacote técnico para Opus/auditor externo, validar arquitetura, riscos, segurança e coerência técnica.

Validação:
auditoria externa sem falhas críticas abertas; achados menores convertidos em backlog priorizado.

## F50 — Continuous Governance & Future Roadmap

Objetivo:
estabelecer rotina de dívida técnica, atualização de dependências, risk register, feedback interno e próximo ciclo técnico.

Validação:
backlog priorizado, rotina de manutenção definida e próximo roadmap aprovado.

## Extensão futura pós-F50

Depois de F50, a sequência operacional futura pode ser estendida com dois ciclos adicionais, sem reduzir nem fundir F30-F50:

### F51-F58 — Security & Cybersecurity Hardening Cycle

Objetivo:
endurecer o ARIS contra vazamento de dados, brechas locais, prompt injection, tool poisoning, abuso de providers, falhas de sandbox, ataques de voz/UI e riscos de supply-chain antes de iniciar um laboratório prático amplo.

F51 — Security Architecture & Threat Model
Objetivo: mapear ameaças reais do ARIS, superfícies de ataque, trust boundaries, abuse cases e security risk register.

F52 — Data Protection, Privacy & Secrets Hardening
Objetivo: proteger dados sensíveis, secrets, logs, artifacts, memória, provider redaction, PII, paths sensíveis e evitar vazamentos.

F53 — Runtime & Desktop Attack Surface Reduction
Objetivo: reduzir superfície de ataque local, incluindo permissões, subprocess, filesystem, symlink attacks, path traversal, sandbox escape e políticas do host.

F54 — Prompt Injection, Tool Poisoning & Context Attack Defense
Objetivo: reforçar defesa contra indirect prompt injection, lethal-trifecta, untrusted content, tool output boundary e memory poisoning.

F55 — Provider, Network & Cost Abuse Security
Objetivo: proteger provider keys, redaction, network policy, budget abuse, resource amplification, fallback poisoning e circuit breakers.

F56 — UI, Voice & Multimodal Security Hardening
Objetivo: endurecer comandos por voz, wake word, readback, confirmação, anexos, OCR/PDF, UI action buttons e fronteiras multimodais.

F57 — Cybersecurity Red-Team Simulation
Objetivo: simular ataques contra o ARIS, incluindo vazamento de dados, bypass de gate, ação não autorizada, prompt injection, rollback bypass, sandbox escape e provider leakage.

F58 — Security Closure & Internal Hardening Gate
Objetivo: validar correções, riscos aceitos, riscos bloqueantes, política de operação segura e readiness para o laboratório interno.

### F59-F68 — ARIS Internal Capability Lab Cycle

Objetivo:
medir capacidades reais do ARIS em ambiente local controlado, incluindo competência, segurança, velocidade, uso de CPU/RAM/disco, resposta, contexto, memória, ações, rollback, UI, voz, providers, confiabilidade e utilidade prática.

F59 — ARIS Internal Capability Lab Foundation
Objetivo: criar estrutura local do laboratório, fixtures, cenários, scoring e relatórios.

F60 — Small Task Capability Suite
Objetivo: testar tarefas pequenas como resumo, CSV, notas, resposta factual, prompt injection simples e dry-run local.

F61 — Medium Workflow Capability Suite
Objetivo: testar workflows multi-etapa com documentos, memória, aprovação, ledger e rollback.

F62 — Local Systems Simulation Lab
Objetivo: criar sistemas falsos locais, como fake CRM, fake tickets, fake calendar, fake files e fake office data.

F63 — Desktop Resource & Performance Lab
Objetivo: medir CPU, RAM, disco, startup, shutdown, artifact growth, SQLite growth e sessão longa.

F64 — Security Attack Lab
Objetivo: testar prompt injection, tool poisoning, path traversal, data exfiltration, voice attack e ações proibidas.

F65 — Automation Execution Lab
Objetivo: testar execução local controlada, rollback, compensação, falha no meio e estado final.

F66 — UI, Voice & Multimodal Lab
Objetivo: testar cockpit, resposta longa, approval UX, voz, readback, fallback textual, PDF/OCR e anexos.

F67 — Practical Utility Metrics
Objetivo: medir tempo economizado, erros evitados, retrabalho reduzido, intervenção humana e custo por tarefa.

F68 — Capability Review & Next Direction
Objetivo: decidir se o ARIS está pronto para uso operacional interno, automação vertical ou novo ciclo técnico.
