# BENCHUIX-27 — Operator Acceptance Decision Packet

**Status:** `CANDIDATE_ONLY`

Este pacote organiza a decisão manual do operador sobre o candidato `BENCHUIX-27`.
Ele consolida critérios de aceite, WARN, retrabalho e bloqueio sobre o preview estável já empacotado no v17.

**Stable preview URL:** `http://127.0.0.1:8123/artifacts/benchuix/drafts/barbearia_dashboard_latest.html`

**Comando local:**

```bash
cd /home/matheus/ARIS/Project_ARIS/aris-active-context
python3 -m http.server 8123
```

## Decisões Possíveis

- `ACCEPT`
- `ACCEPT_WITH_WARN`
- `REJECT_FOR_REWORK`
- `BLOCKED`

## O Que Revisar Primeiro

Revise primeiro a leitura principal do dashboard como operador real:

1. `Hoje` como superfície de decisão imediata.
2. `Agenda` em `Dia` e `Semana`.
3. `Disponibilidade` em viewport móvel.
4. `Estimativa do dia` versus `Hoje`.
5. `Ajuda` como suporte operacional local.

Depois confirme se a evidência continua acessível sem quebrar a leitura principal.

## Critérios Para `ACCEPT`

Escolha `ACCEPT` apenas se todos os itens abaixo forem verdadeiros:

- O preview latest abre localmente sem erro funcional relevante.
- A leitura visual geral parece pronta para revisão candidata futura em `CRISOL`.
- Não há overflow horizontal em `320`, `375`, `480`, `768` e `1024`.
- `Hoje`, `Agenda`, `Disponibilidade`, `Aprovações`, `Estimativa do dia`, `Configurações` e `Ajuda` permanecem compreensíveis.
- Os comportamentos preservados de v4-v16 continuam presentes.
- A evidência continua acessível após a simplificação por disclosure.
- O estado visual transmite confiança suficiente para avaliação externa futura, ainda sem produto.
- Não existe must-fix crítico antes de qualquer preparação candidata futura.

## Critérios Para `ACCEPT_WITH_WARN`

Escolha `ACCEPT_WITH_WARN` se o candidato estiver utilizável para avanço documental futuro, mas ainda houver ressalvas não-bloqueantes:

- Existe ruído visual, densidade excessiva ou microcopy que merece ajuste.
- Existe fricção menor em mobile, navegação, disclosure ou ajuda, sem comprometer o fluxo principal.
- Existe inconsistência estética ou de clareza que não invalida o entendimento operacional.
- O operador aceitaria seguir para preparação futura de `CRISOL`, desde que os WARNs fiquem registrados.

## Critérios Para `REJECT_FOR_REWORK`

Escolha `REJECT_FOR_REWORK` se houver falhas que exigem retrabalho visual específico antes de nova avaliação:

- A leitura principal do dashboard ficou confusa ou hierarquicamente fraca.
- Há regressão perceptível em comportamento preservado de v4-v16.
- Mobile, agenda, disclosures ou ajuda perderam legibilidade operacional.
- A confiança visual caiu a ponto de o candidato não sustentar uma revisão séria futura.
- Existem must-fix claros e concretos que precisam de prompt de retrabalho dedicado.

## Critérios Para `BLOCKED`

Escolha `BLOCKED` se a decisão não puder ser tomada de forma responsável nesta fase:

- O preview não abre ou não pode ser revisado localmente.
- Há ausência de evidência suficiente para julgar o candidato.
- Existe dúvida estrutural que impede decidir entre aceite e retrabalho.
- Existe blocker externo, técnico ou operacional que precisa ser registrado antes de continuar.

## Checklist Rápido Do Operador

- Abrir o preview latest localmente.
- Confirmar leitura principal de `Hoje`.
- Confirmar `Agenda` em `Dia`.
- Confirmar `Agenda` em `Semana`.
- Confirmar navegação móvel em `Disponibilidade`.
- Confirmar coerência entre `Hoje` e `Estimativa do dia`.
- Confirmar controles em dark e light theme.
- Confirmar cenários `normal`, `onboarding`, `empty` e `failure`.
- Confirmar `Ajuda` com busca, filtro e expansão.
- Registrar decisão manual usando o formulário v18.

## O Que Ignorar Nesta Fase

Ignore explicitamente nesta fase:

- qualquer transição real para `CRISOL`
- qualquer aceite canônico
- produto, produção, piloto, Bedrock ou `real_apply`
- qualquer integração live, runtime externo, credencial ou superfície de execução
- discussão de rollout real

## Próximo Passo Condicional

### Se `ACCEPT`

Preparar um pacote candidato para futura transição documental para `CRISOL`, sem aplicar a transição nesta fase.

### Se `ACCEPT_WITH_WARN`

Registrar os WARNs aceitos e decidir se devem ser corrigidos antes da preparação futura para `CRISOL`.

### Se `REJECT_FOR_REWORK`

Abrir um prompt de retrabalho visual específico, com escopo restrito aos problemas observados.

### Se `BLOCKED`

Parar e registrar o blocker de forma explícita antes de qualquer nova movimentação.

## Observação De Escopo

Este pacote prepara a decisão do operador. Ele não decide pelo operador e não inicia `CRISOL`.

## Declaração Explícita

Este pacote não altera estado canônico e não autoriza execução real.
