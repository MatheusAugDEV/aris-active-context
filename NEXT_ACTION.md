# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **sha_lido:** `62044ef1bdde4d262b1d4addde2a9bd3359e6099`

### Status Atual

A **Fase 4B foi concluída com decisão=pass** em 2026-06-30.

Resultado principal: 4 bug classes identificadas no generator inline da Fase 1. Generator
corrigido escrito em `Project_ARIS/scripts/run_lapidarium_fase1_triagem_generator.py`.
39 testes regressivos, todos passando. Dry-run executado — dataset original preservado.
`.env` corretamente retorna `git_tracked=False` no novo generator.

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Rotação de Segredos (manual, independente de fase):**
Ver `artifacts/lapidarium/lapidarium_f4_find001_rotation_checklist.md`.
- Avaliar risco de exposição do `.env` local (861 bytes)
- Rotacionar credenciais se houver risco de exposição por outros meios além do git
- Esta ação não requer prompt de fase — é responsabilidade do operador

**2. LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_PLAN (próxima fase recomendada):**
- Planejamento cirúrgico de remoção de lixo confirmado
- Requer decisão do operador por item candidato a remoção
- Fase 4B concluída ✓ | CI green ✓ | validator pass ✓

**3. Findings pendentes de decisão do operador (não requerem nova fase imediata):**
- F4-FIND-002: Nested Git repo em `external/mcp_candidates/` — decidir submodule/vendor/remove
- F4-FIND-003: PostScript binários em `legacy/experiments/` — inspecionar antes de qualquer remoção

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
