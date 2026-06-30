# LAPIDARIUM FASE 4 — Revisão de Código Genuíno

> **Fonte primária:** `ACTIVE_CONTEXT_STATE.json`
> **Data:** 2026-06-30
> **Fase:** `LAPIDARIUM_FASE_4_REVISAO_CODIGO_GENUINO`
> **Modo:** READ-ONLY — nenhum arquivo foi deletado, movido ou modificado.

---

## 1. Contagens

| Métrica | Valor |
|---|---|
| Base `seems_source_genuine` | 3.880 |
| Excluídos via exclusion list v2 | 5 |
| **Sanitizados para revisão** | **3.875** |

---

## 2. Classificação do Conjunto Sanitizado

| Categoria | Count | % | Avaliação |
|---|---|---|---|
| A — Código Fonte Genuíno (src/, frontend/) | 933 | 24,1% | **KEEP** |
| B — Testes Genuínos (tests/) | 1.072 | 27,7% | **KEEP** |
| C — Documentação Legítima (docs/) | 937 | 24,2% | **KEEP** |
| D — Scripts de Governança (scripts/) | 866 | 22,4% | **KEEP** |
| E — Config/Infra (pyproject.toml, uv.lock) | 4 | 0,1% | **KEEP** |
| F — Binários/Assets | 4 | 0,1% | **KEEP** (PNG assets) |
| G — Legado/Histórico (legacy/) | 15 | 0,4% | **OPERATOR REVIEW** |
| H — Tooling Oculto (.claude, .agents, .github) | 28 | 0,7% | **KEEP** (exceto .env — ver F4-FIND-001) |
| I — Temporário de Auditoria (temp_audit/) | 2 | 0,1% | **SCHEDULE REMOVAL** |
| J — Suspeitos / Revisão (external/, *.wav) | 14 | 0,4% | **OPERATOR REVIEW** |
| **Total** | **3.875** | **100%** | |

**Código genuíno de alta confiança (A+B+C+D): 3.808 entradas = 98,3%**

---

## 3. Achados Críticos

### F4-FIND-001 — SEGURANÇA: `.env` Rastreado no Git `[ALTA]`

O arquivo `.env` (861 bytes, ASCII text) está git-tracked e aparece em `seems_source_genuine`.
Segredos NÃO devem ser commitados. **Requer ação imediata do operador independente das fases Lapidarium:**
- Remover do tracking: `git rm --cached .env`
- Adicionar ao `.gitignore`
- Rotar todos os segredos contidos

**Esta fase não executa essa remoção.**

---

### F4-FIND-002 — SUPPLY CHAIN: Repo Git Aninhado em `external/` `[MÉDIO]`

`external/mcp_candidates/gogogadgetbytes_smart_connections_mcp/source/` contém um repo Git
completo com `.git/` interno (não é submodule declarado no `.gitmodules`). Inclui:
- 6 arquivos TypeScript (MCP server)
- package.json, tsconfig.json, README, CONTRIBUTING, LICENSE

O operador deve decidir: declarar como submodule, vendor, ou remover.
**Esta fase não executa nenhuma dessas ações.**

---

### F4-FIND-003 — BINÁRIOS SUSPEITOS: PostScript em `legacy/experiments/` `[MÉDIO]`

Dois arquivos sem extensão são PostScript documents de grande porte:
- `legacy/experiments/genai`: 20,9 MB PostScript DSC Level 3.0
- `legacy/experiments/threading`: 7,0 MB PostScript DSC Level 3.0

O padrão (nome de experimento, conteúdo binário grande, não é código Python) é similar
ao dos 2 weird files acidentais já conhecidos (`[:alnum:] \n \` e `how --stat --summary 5dda82a`),
mas o formato difere (PostScript vs ASCII overstrike). **Requer inspeção do operador
antes de qualquer remoção.** Não foram incluídos na exclusion list v2 pois não passaram
pelos mesmos heurísticos A-E.

---

### F4-FIND-004 — RISCO DE GENERATOR: Bug de Quoting na Fase 1 `[MÉDIO]`

O generator do dataset `fase1_triagem_classificacao.json` tem um bug de quoting/escaping
que produziu 2 artifacts acidentais (shell output com tamanho idêntico de 15.915 bytes)
em um único commit (`baf7977b`). O bug não foi corrigido. **Regenerar o dataset sem
corrigir o generator pode reintroduzir os mesmos ou novos artifacts corrompidos.**

Recomendação: executar `LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR` antes
de qualquer uso do dataset para cleanup automático.

---

## 4. Itens com Risco Adicional

| Item | Tipo | Risco | Ação |
|---|---|---|---|
| `legacy/experiments/tart=always` | UTF-8 com escape sequences, nome=arg CLI | Possível shell output acidental | Operator inspect before removal |
| `debug_audio.wav` | `data` type (não RIFF válido), 265 KB | Debug artifact possivelmente corrompido | Operator review |
| `teste.wav` | RIFF WAV válido (8-bit PCM, 8kHz, mono) | Teste de áudio de dev | Operator review |
| `legacy/wake/tts.py.backup` | Backup explícito | Lixo histórico | Remove após operator auth |
| `legacy/wake/wake.py.backup` | Backup explícito | Lixo histórico | Remove após operator auth |
| `temp_audit/` (2 arquivos) | Audit artifacts temporários | Lixo derivado | Schedule removal após auth |

---

## 5. Próximas Ações Recomendadas

1. **IMEDIATO — SEGURANÇA:** Operador remediar `.env` git-tracked (F4-FIND-001). Independente das fases.
2. **FASE 4B:** `LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR` — corrigir bug de quoting do generator antes de cleanup automático.
3. **FASE 5:** Planejar remoção cirúrgica do lixo confirmado (`temp_audit/`, backups, itens legacy suspeitos) após revisão e autorização do operador por item.
4. **SUPPLY CHAIN:** Resolver situação do repo externo aninhado em `external/` (F4-FIND-002).

---

## 6. Confirmações Obrigatórias

| Item | Status |
|---|---|
| Fase 4 executada como read-only | ✓ CONFIRMADO |
| `Project_ARIS` não alterado | ✓ CONFIRMADO |
| Nenhum cleanup/deletion/move executado | ✓ CONFIRMADO |
| Todos os locks reais permaneceram false | ✓ CONFIRMADO |
| Exclusion list v2 aplicada (5 entradas) | ✓ CONFIRMADO |
| Contagem sanitizada = 3.875 | ✓ CONFIRMADO |
| Validator decision = pass | ✓ CONFIRMADO |

---

## 7. Artifacts Produzidos

- `artifacts/lapidarium/lapidarium_fase4_revisao_codigo_genuino_packet.json`
- `artifacts/lapidarium/lapidarium_fase4_sanitized_input_manifest.json`
- `artifacts/lapidarium/lapidarium_fase4_review_classification_matrix.json`
- `artifacts/lapidarium/lapidarium_fase4_risk_and_false_positive_register.json`
- `artifacts/lapidarium/lapidarium_fase4_no_real_execution_attestation.json`
- `artifacts/lapidarium/lapidarium_fase4_validation_evidence.json`
- `artifacts/lapidarium/lapidarium_fase4_report.md` ← este arquivo

---

*Source of truth: `ACTIVE_CONTEXT_STATE.json`. Este relatório é mirror derivado.*
