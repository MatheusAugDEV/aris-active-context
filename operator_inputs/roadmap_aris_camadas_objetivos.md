# ROADMAP ARIS — CAMADAS E OBJETIVOS

> Operator input artifact. Source: operator prompt "PROMPT CLAUDE CODE — ARIS MACRO ROADMAP CANONICALIZATION + ROADMAP EXCLUDENT CLEANUP", section "Tarefa 2 — Atualizar `ROADMAP_CANONICAL.md`".
>
> Classification: operator input artifact (operator_prompt_embedded_content). Not permanent authority by itself.
> Does not override `ACTIVE_CONTEXT_STATE.json`.
> Does not override `ROADMAP_CANONICAL.md` (this document is the basis used to update it).
> Does not authorize real execution, product, Bedrock, secrets, real_apply, or runtime real.

## Cadeia macro

```text
Infernus FULL
  ↓
Purgatorium FULL
  ↓
Infernus Revalidation
  ↓
BenchUX
  ↓
Crisol
  ↓
Polimento
  ↓
EXT-SEC 00→04
  ↓
Cinzel
  ↓
EXT-SEC 05→06
  ↓
Bedrock Gate
  ↓
Produto Parte 2 / Design Partner
  ↓
EXT-SEC 07→08 contínuo
```

## Cabeçalho canônico exigido para ROADMAP_CANONICAL.md

```markdown
# ARIS ROADMAP CANONICAL — CAMADAS E OBJETIVOS

Status: MACRO_ROADMAP_CANONICAL_ACTIVE
Authority: macro roadmap authority
Live-state authority: ACTIVE_CONTEXT_STATE.json
Conflict rule: ACTIVE_CONTEXT_STATE.json > ARIS_BOOT.md > ROADMAP_CANONICAL.md > DECISION_LOCKS.md > phase-specific roadmaps > artifacts/docs > archive > excludent
Real execution authorized by this document: false
Product/Bedrock/real_apply/secrets/runtime real authorized by this document: false
```

## Camadas

### 1. Infernus FULL

- Natureza: adversarial ofensivo-controlado.
- Objetivo: revelar falhas reais do sistema sob condições adversariais controladas.
- Escopo principal: execução de waves sintéticas isoladas, geração de evidence bundle, vulnerability register, handoff graph e Minos verdict.
- Componentes/sequência interna: scope/charter, ledger/ontology/oracle/bot packs, scenario pack + harness readiness, excludent cleanup, execution authorization gate, attack waves (W0–W6), evidence bundle + vulnerability register, Purgatorium handoff graph, Minos final verdict + closure.
- Entrega esperada: evidence bundle, vulnerability register, handoff graph, Minos verdict.
- Gate de saída: Minos final verdict + closure pass, com handoff Purgatorium pronto.
- Limites explícitos: não promete segurança absoluta; não autoriza produto, Bedrock, real_apply, secrets ou runtime real.

### 2. Purgatorium FULL

- Natureza: corretiva/mitigadora.
- Objetivo: corrigir, mitigar ou colocar em quarentena os findings do Infernus.
- Escopo principal: track PURG-PRE → PURG-00 → PURG-01 → PURG-02 → PURG-03 → PURG-Sx → PURG-04 → PURG-05 → PURG-RES → PURG-EXIT.
- Componentes/sequência interna: `PURG-Sx` é track condicional, não fila obrigatória.
- Entrega esperada: findings corrigidos, mitigados ou quarentenados, com evidência registrada.
- Gate de saída: PURG-EXIT com evidência completa e sem reset pendente.
- Limites explícitos: Purgatorium não fecha finding; GREEN sem reset é inválido; residual não vira resolved.

### 3. Infernus Revalidation

- Natureza: validação adversarial pós-correção.
- Objetivo: revalidar os findings tratados pelo Purgatorium.
- Escopo principal: única camada que pode declarar `finding_closed`, `finding_regressed`, `finding_partially_mitigated`, `finding_still_open`, `new_regression_found`.
- Entrega esperada: veredito de revalidação por finding.
- Gate de saída: veredito de revalidação registrado para todos os findings em escopo.
- Limites explícitos: nenhuma outra camada pode declarar esses status de finding.

### 4. BenchUX

- Natureza: validação de produto/experiência.
- Objetivo: validar posicionamento competitivo e experiência do ARIS.
- Escopo principal: comparação com alternativas reais no momento da execução.
- Entrega esperada: relatório de benchmark comparativo de UX/posicionamento.
- Gate de saída: comparação registrada com evidência, não apenas narrativa.
- Limites explícitos: não é marketing.

### 5. Crisol

- Natureza: consolidação.
- Objetivo: consolidar o sistema completo.
- Escopo principal: remoção de contradições internas.
- Entrega esperada: sistema transformado em produto técnico coeso.
- Gate de saída: ausência de contradições internas relevantes registradas.
- Limites explícitos: não introduz capacidade nova além de consolidação.

### 6. Polimento

- Natureza: limpeza cirúrgica.
- Objetivo: preparar o repositório para EXT-SEC/SAST/SCA/secret scanning com menos ruído.
- Escopo principal: limpeza sem capacidade nova.
- Entrega esperada: repositório limpo, pronto para varreduras de segurança.
- Gate de saída: limpeza concluída sem introdução de capacidade nova.
- Limites explícitos: sem capacidade nova; sem mudança funcional.

### 7. EXT-SEC 00→04

- Natureza: programa defensivo pré-Bedrock.
- Objetivo: preparar o sistema defensivamente antes do Bedrock Gate.
- Escopo principal: artifact-first, sem sistema vivo.
- Componentes/sequência interna: source ledger primário, threat model, hardening, fixtures sintéticas, closeout.
- Entrega esperada: artifacts de segurança defensiva (ledger, threat model, hardening plan, fixtures, closeout).
- Gate de saída: closeout EXT-SEC-04 com todos os artifacts presentes.
- Limites explícitos: artifact-first; sem sistema vivo; sem runtime real.

### 8. Cinzel

- Natureza: validação de automação aplicada.
- Objetivo: validar automação útil em SMB brasileiro simulado.
- Escopo principal: mínimo 5 cenários/workflows.
- Entrega esperada: métricas de tempo, custo, aprovação, rollback, retry e artifacts.
- Gate de saída: métricas completas registradas para todos os cenários mínimos.
- Limites explícitos: ambiente simulado; sem cliente real.

### 9. EXT-SEC 05→06

- Natureza: segurança ofensiva autorizada externa.
- Objetivo: DAST autorizado / pentest externo / retest.
- Escopo principal: staging-prod isolado.
- Entrega esperada: relatório de DAST/pentest e retest.
- Gate de saída: autorização, escopo, janela, contas de teste, dados sintéticos, rollback e legal authorization todos documentados e atendidos.
- Limites explícitos: exige autorização, escopo, janela, contas de teste, dados sintéticos, rollback e legal authorization.

### 10. Bedrock Gate

- Natureza: gate máximo de decisão.
- Objetivo: decidir produto real.
- Escopo principal: não é fase de construção.
- Entrega esperada: decisão explícita de Bedrock (PASS/WARN/BLOCK/NEEDS_REVIEW/REGRESSION/OBSOLETE).
- Gate de saída: decisão explícita do operador.
- Limites explícitos: só ocorre depois de Infernus, Purgatorium, Revalidation, BenchUX, Crisol, Polimento, EXT-SEC 00→04, Cinzel e EXT-SEC 05→06.

### 11. Produto Parte 2 / Design Partner

- Natureza: comercialização controlada.
- Objetivo: primeiro uso real.
- Escopo principal: vertical, ICP, prospects, contrato, pricing, onboarding, suporte e feedback.
- Entrega esperada: design partner ativo com feedback estruturado.
- Gate de saída: onboarding e ciclo de feedback inicial documentados.
- Limites explícitos: somente após Bedrock Gate explícito.

### 12. EXT-SEC 07→08 contínuo

- Natureza: segurança contínua pós-produto.
- Objetivo: manter segurança contínua após o início de produto.
- Escopo principal: vulnerability management, retest, adversarial emulation, incident response, backup/restore drills, tenant isolation review.
- Entrega esperada: ciclo contínuo de segurança operacional documentado.
- Gate de saída: não aplicável (contínuo).
- Limites explícitos: contínuo; depende da existência de produto ativo (camada 11).

## Princípio final

```markdown
## Princípio final

O ARIS não vira produto porque parece pronto.
O ARIS vira produto quando sobreviveu a ataque,
corrigiu o que foi encontrado,
foi revalidado,
foi comparado,
foi consolidado,
foi limpo,
foi auditado,
foi demonstrado,
foi testado externamente,
e passou por decisão explícita de Bedrock.
```

## Transições macro esperadas (alto nível)

```text
INF-FULL -> PURG-FULL
PURG-FULL -> INF-REVALIDATION
INF-REVALIDATION -> BENCHUX
BENCHUX -> CRISOL
CRISOL -> POLIMENTO
POLIMENTO -> EXT-SEC-00
EXT-SEC-00 -> EXT-SEC-01
EXT-SEC-01 -> EXT-SEC-02
EXT-SEC-02 -> EXT-SEC-03
EXT-SEC-03 -> EXT-SEC-04
EXT-SEC-04 -> CINZEL
CINZEL -> EXT-SEC-05
EXT-SEC-05 -> EXT-SEC-06
EXT-SEC-06 -> BEDROCK
BEDROCK -> PRODUCT-P2-DESIGN-PARTNER
PRODUCT-P2-DESIGN-PARTNER -> EXT-SEC-07
EXT-SEC-07 -> EXT-SEC-08-CONTINUOUS
```
