# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_PLAN (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **sha_lido:** `7310ebbb77a4e39887dddf7e40c4c65e332aa242`

### Status Atual

A **Fase 5 foi concluída com decisão=pass** em 2026-06-30.

Resultado principal: Plano de cleanup criado. 16 candidatos inventariados.
Nenhum arquivo removido, movido ou alterado. Cada item tem decisão, risco,
comando proposto e rollback. 3 itens bloqueados aguardam decisão do operador.

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Revisar `lapidarium_fase5_operator_approval_matrix.json`:**
Para cada item aprovado, emitir prompt explícito com item_id e ação autorizada.
Uma fase futura de cleanup real (`LAPIDARIUM_FASE_5_CLEANUP_EXECUTION`) será
iniciada apenas com itens autorizados em escopo.

**2. OPERADOR — Decisões de itens BLOQUEADOS (separadas, por finding):**
- **F4-FIND-002** (`F5-015`): Nested Git repo em `external/mcp_candidates/` —
  escolher estratégia: submodule / vendor / remove / quarantine
- **F4-FIND-003** (`F5-013`, `F5-014`): PostScript binários em `legacy/experiments/` —
  confirmar origem e intenção antes de qualquer remoção (ação irreversível)

**3. OPERADOR — Checkpoint files em `temp_audit/` (`F5-004`, `F5-005`):**
Ler conteúdo de `temp_audit/f15z1` e `temp_audit/f15z1_post_z3` e confirmar
se são seguras para remoção (arquivos de 120B — possíveis gate markers).

**4. OPERADOR — Rotação de Segredos (independente de fase):**
Ver `artifacts/lapidarium/lapidarium_f4_find001_rotation_checklist.md`.
`.env` está corretamente gitignored — avaliação de risco é responsabilidade do operador.

---

### Aguardando Instrução

Todos os locks reais permanecem `false`. Nenhuma ação de cleanup, runtime ou produto
será iniciada sem instrução explícita do operador.

---

## Historical Appendix

`HISTORICAL_ONLY`
`SUPERSEDED_BY_LAPIDARIUM_FASE4_AND_F4_FIND001_CONTAINMENT`
`NOT_CURRENT_STATE`

Referências a IF09/next_phase=null e P15–P19 são históricas e superseded.
