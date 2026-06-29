# BOOT

GERADO — NAO EDITE A MAO

## CARIMBO

- state_sha: `b5b786d82447`
- schema_version: `3.29`

## AVISO DE STALE

- Se este state_sha nao bate com sha256(STATE.json), rode `python3 scripts/render_boot.py`.

## ONDE ESTOU

- camada: `Unknown`
- phase_id: `LAPIDARIUM`
- status: `lapidarium_fase_2_nomenclatura_pass`
- decision: `pass`
- resumo: Lapidarium Fase 2 - Nomenclatura Aplicação; aguardando LAPIDARIUM_FASE_3_LIMPEZA_CACHE_GERADO sem autorizacao de execucao.

## MAPA

  Infernus FULL
  Purgatorium FULL
  Infernus Revalidation
  Diagnóstico de Automação (+ Camada de Construção condicional)
  BenchUX
  Cinzel-mínimo
  Crisol
  EXT-SEC 00→04
  Cinzel completo
  EXT-SEC 05→06
  Bedrock Gate
  Produto Parte 2 / Design Partner
  EXT-SEC 07→08 contínuo

## PROXIMO PASSO

- active_next_phase: `LAPIDARIUM_FASE_3_LIMPEZA_CACHE_GERADO`
- next_phase_class: `lapidarium_remediation`
- advance_mode: `operator`
- travas relevantes:
  - next_phase_authorized_by_operator=True
  - next_phase_execution_authorization=False
  - operator_approval_packet_review_is_execution_approval=False
  - real_apply_authorized=False
  - runtime_integration_allowed=False
  - production_authorized=False
  - product_ready=False
  - secrets_access_authorized=False
  - deferred_phase_reason=Nenhuma transição definida. Aguardando instrução do operador. ROADMAP_CANONICAL.md não define sucessor para LAPIDARIUM_FASE_3_LIMPEZA_CACHE_GERADO.

## REGRAS DE AGORA

- TODO R2: mover para RULES/ por phase_class.
- JSON vence tudo; markdown que contradiz = drift, pare e reporte.
- Proximo passo so da Transition Table; nao inferir de nome de arquivo nem historico.
- Sem execucao real/runtime/produto/Bedrock/secrets sem lock=true.
- Self-report nao e PASS; PASS = artifact + hash + CI verde + validator.
- excludent/ e archive/ nao sao fonte; forensic-only.
- Fase que muda fato canonico atualiza STATE.json primeiro.

## LEI DE ATUALIZACAO

- Atualize `ACTIVE_CONTEXT_STATE.json` primeiro.
- Regenere `BOOT.md` com `python3 scripts/render_boot.py`.
- Rode `python3 scripts/validate_active_context_state.py`.
- Commit e push apenas com BOOT sincronizado; o hook recusa drift.

## DISCIPLINA DE LEITURA

- Leia so esta pagina no boot inicial.
- Nao leia `archive/` nem `excludent/` como fonte.
- Docs profundos so quando o passo atual apontar explicitamente para eles.

## DOCS PROFUNDOS

- `ROADMAP_CANONICAL.md`
- `ACTIVE_CONTEXT_STATE.json`
- `artifacts/`
- `scripts/validate_active_context_state.py`
