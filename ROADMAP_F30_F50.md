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
