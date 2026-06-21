# Naming Notes

Esta nota existe apenas como referência documental para reduzir ambiguidade de leitura humana. Ela não cria fase, não altera roteamento e não substitui nenhuma fonte canônica de estado.

## Distinção entre os dois usos de `IF09`

| Identificador | Namespace | O que é | Como o `09` foi derivado | Observação |
| --- | --- | --- | --- | --- |
| `IF09-FIND-001` | Findings de segurança | Finding de segurança do Infernus FULL | Numeração do próprio finding | Pertence à linha de findings do Infernus FULL. |
| `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET` | `phase_id` de active-context | Fase documental pós-`INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET` | Derivado do finding que a fase fecha | Não significa "9ª fase" do Infernus FULL. |

## Nota de interpretação

- Os dois identificadores compartilham o prefixo `IF09`, mas pertencem a namespaces distintos e não relacionados por sequência de fases.
- No caso de `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET`, o `09` referencia o finding fechado, não uma fase numerada do Infernus FULL.
- Para leitura humana, trate `IF09-FIND-001` como finding e `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET` como identificador técnico de fase documental.
- Não existe uma "INF-FULL-09" implícita por causa desse nome. A leitura correta continua sendo a linha canônica já registrada no projeto.

## Autoridade

Este arquivo é referência. Não é autoridade. Em caso de qualquer conflito, `ACTIVE_CONTEXT_STATE.json` vence sempre.

## Boot e consulta

Este arquivo não está no `boot_read_order` de `ARIS_BOOT.md` e não precisa ser lido a cada boot. É material de consulta sob demanda.
