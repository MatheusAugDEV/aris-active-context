# Hygiene Report — Semana de 2026-08-10

**Rotina:** Revisão semanal canônica (segunda-feira 09:00)
**Executado em:** 2026-08-10
**Branch de revisão:** `claude/beautiful-noether-jlhcqp`
**Main HEAD:** `3129f71556367bccde3e83e507556d66723a9260`

---

## Resultado Geral: RUÍDO DETECTADO — Revisão Operador Necessária

Três achados abaixo. Nenhuma ação destrutiva foi tomada. Nenhum lock alterado.

---

## ACHADO 1 — CRÍTICO: Acúmulo de 30 PRs abertos sem merge (desde 2026-06-29)

**Tipo:** Ruído estrutural / acúmulo de automação

### Situação

Existem **30 PRs abertos** direcionando para `main`, criados entre 2026-06-29 e 2026-08-07.
Nenhum foi mesclado. O main está congelado no SHA `3129f71556367bccde3e83e507556d66723a9260` desde pelo menos 2026-07-06.

### Distribuição

| Tipo | Quantidade | Faixa de datas |
|---|---|---|
| Daily doctor (mirror/drift cleanup) | 24 | 2026-06-30 → 2026-08-07 |
| Weekly hygiene | 6 | 2026-06-29, 07-06, 07-13, 07-20, 07-27, 08-03 |

PRs enumerados: #2–#31 (todos open, todos com 0 comentários visíveis).

### Por que isso importa

- A lista de PRs do repositório está ilegível: qualquer nova atividade relevante do operador se perde no ruído.
- Cada PR criou um branch separado — há **25+ ramos remotos** sem uso aparente além de suportar um PR estagnado.
- Os PRs de "daily doctor" repetem-se todos os dias mesmo com main congelado. Se os branches não contêm mudanças reais sobre main, os PRs são vazios por construção.
- O padrão continuará criando novos PRs enquanto as rotinas automatizadas rodarem.

### Ação Recomendada (requer decisão do operador)

Opção A — **Fechar os PRs stale em lote**: Qualquer PR cujo head branch não traga diff real sobre main pode ser fechado sem risco. Os branches podem ser deletados após fechamento.

Opção B — **Revisar e mesclar**: Se algum PR traz mudança documental real, revisar e mesclar. Os demais, fechar.

Opção C — **Ajustar a rotina**: Configurar as rotinas automatizadas para criar PRs apenas quando houver diff real, ou para fechar o PR anterior antes de abrir um novo.

**Este relatório não fecha nem mescla nenhum PR.** A decisão e a execução são do operador.

---

## ACHADO 2 — MÉDIO: README.md com duplo cabeçalho "## Current snapshot"

**Tipo:** Drift de mirror / ruído documental

### Situação

O `README.md` possui **dois blocos `## Current snapshot`** consecutivos antes do cabeçalho `# aris-active-context`:

1. **Bloco 1 (atual):** Descreve `Lapidarium True — Fase 6: Guarda`, CI_GREEN_CONFIRMED, candidate DIAGNOSTICO_AUTOMACAO_GATE — **correto e atual** (alinhado com ACTIVE_CONTEXT_STATE.json).

2. **Bloco 2 (stale):** Descreve `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET` como "Latest completed phase" — **histórico e superseded**. Esta fase foi concluída antes do ciclo Lapidarium.

### Impacto

Qualquer agente ou operador que leia o README vê dois "Current snapshot" conflitantes antes de atingir o corpo principal. O Bloco 2 contradiz o Bloco 1 e o JSON canônico — é drift por definição.

### Ação Recomendada

Remover ou mover o Bloco 2 para a seção `## Historical Appendix` já existente no README.
Esta é uma correção documental segura e reversível (1-3 linhas). Pode ser incluída neste PR mediante confirmação do operador.

---

## ACHADO 3 — BAIXO: DECISION_LOCKS.md excedeu 251K caracteres

**Tipo:** Crescimento não controlado de artefato

### Situação

A leitura inline do `DECISION_LOCKS.md` foi rejeitada por exceder o limite de tokens do MCP (`251,924 caracteres`). O arquivo cresceu ao longo das fases acumulando locks e evidências.

### Impacto

- Agentes automatizados que precisem ler DECISION_LOCKS.md podem falhar ou receber leitura parcial.
- Não é possível garantir integridade da leitura em contextos de tamanho limitado.

### Ação Recomendada

Revisar a política de `DECISION_LOCKS.md`: seções históricas (`CLOSED`) poderiam ser movidas para um arquivo companion em `archive/gate_history/` ou `artifacts/governance/`, mantendo em DECISION_LOCKS.md apenas os locks ativos e os mais recentes. Esta mudança exige decisão explícita do operador e não está no escopo deste relatório.

---

## Estado dos Arquivos Canônicos

| Arquivo | Estado | Nota |
|---|---|---|
| `ACTIVE_CONTEXT_STATE.json` | OK — não lido diretamente (é autoridade) | Indireto via mirrors |
| `CURRENT_STATE.md` | OK | Última atualização 2026-07-01 (consistente com main congelado) |
| `NEXT_ACTION.md` | OK | Última atualização 2026-07-01 (consistente) |
| `ROADMAP_CANONICAL.md` | OK | LAPIDARIUM CLOSED, DIAGNOSTICO_AUTOMACAO_GATE CANDIDATE |
| `README.md` | DRIFT — duplo snapshot header | Ver Achado 2 |
| `DECISION_LOCKS.md` | ATENÇÃO — 251K chars | Ver Achado 3 |

---

## Estado das Fases (main)

- **Fase viva:** `LAPIDARIUM_FASE_6_GUARDA_TRUE` (CLOSED)
- **Candidata:** `DIAGNOSTICO_AUTOMACAO_GATE` (não autorizada)
- **Locks de runtime:** todos `false` — conforme esperado
- **next_phase:** `null` — aguardando instrução explícita do operador

---

## O Que Este Relatório NÃO Faz

- Não fecha, merges nem altera nenhum PR
- Não deletou nenhum branch
- Não alterou `archive/`, `excludent/`, locks reais, `DECISION_LOCKS.md`, `ACTIVE_CONTEXT_STATE.json`
- Não abriu `next_phase`
- Não tocou `Project_ARIS`

---

## Próximo Passo Sugerido ao Operador

1. **Decidir sobre os 30 PRs abertos** (Achado 1) — fechar stale, mesclar se houver conteúdo.
2. **Autorizar ou rejeitar** a remoção do Bloco 2 stale do README (Achado 2) — pode ser feito neste PR se aprovado.
3. **Tomar nota** do tamanho de DECISION_LOCKS.md para planejamento futuro.
