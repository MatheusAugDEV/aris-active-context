# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_SECURITY_F4_FIND_001_ENV_CONTAINMENT (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **sha_lido:** `bf0728b4e511272117133cd97497c7382174dbad`

### Status Atual

A **contenção de F4-FIND-001 foi registrada com decisão=pass** em 2026-06-30.

Resultado principal: `.env` nunca estava git-tracked — o campo `git_tracked=True` no dataset
da Fase 1 era um falso positivo do scanner. O `.gitignore` já tinha regras adequadas.
Nenhuma ação técnica de remoção foi necessária.

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Rotação de Segredos (manual, independente de fase):**
Ver `artifacts/lapidarium/lapidarium_f4_find001_rotation_checklist.md`.
- Avaliar risco de exposição do `.env` local (861 bytes)
- Rotacionar credenciais se houver risco de exposição por outros meios além do git
- Esta ação não requer prompt de fase — é responsabilidade do operador

**2. LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR (próxima fase recomendada):**
- Corrigir bug de quoting/escaping do generator da Fase 1
- Investigar também o método de detecção de `git_tracked` (que produziu o falso positivo FP-05)
- Emitir prompt explícito para iniciar
- Requer: CI green atual ✓ | validator pass ✓ | F4-FIND-001 containment registrado ✓

**3. LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_PLAN (após 4B):**
- Planejamento cirúrgico de remoção de lixo confirmado
- Requer 4B concluída e decisão do operador por item

**4. Findings pendentes de decisão do operador (não requerem nova fase imediata):**
- F4-FIND-002: Nested Git repo em `external/mcp_candidates/` — decidir submodule/vendor/remove
- F4-FIND-003: PostScript binários em `legacy/experiments/` — inspecionar antes de qualquer remoção
- F4-FIND-004: Bug do generator — coberto por Fase 4B

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
