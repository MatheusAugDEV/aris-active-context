## definição da fase

BENCHUIX-11 materializa a Approval Inbox como fase candidata e synthetic-only da trilha BenchUIX. Ela organiza cada pedido de aprovação em um card legível, auditável e bloqueável antes de qualquer ação sensível.

## tese da Approval Inbox

Uma aprovação só é segura quando o cliente entende o que será feito, qual é o risco, o que está permitido e o que explicitamente não será feito.

## objetivo

Definir uma caixa de aprovação que exponha risco, permissão, will/will-not e ações claras de aprovar, negar, editar ou simular novamente, sem executar nada no mundo real.

"o cliente entende exatamente o que está aprovando?"

## relação com BENCHUIX-10

BENCHUIX-10 mostrou o preview determinístico e a prova de isolamento. BENCHUIX-11 transforma esse preview em um pedido de decisão explícita, sempre apoiado por risco visível e permissão compreensível.

## estrutura do card de aprovação

Cada card deve conter:

- título da decisão
- resumo humano do que mudaria
- faixa de risco com motivo
- permissão explícita do que será autorizado
- bloco will/will-not
- origem da simulação mais recente
- ações candidatas disponíveis
- estado atual do pedido

## risco visível

Risco deve aparecer sempre acima das ações, com nível, explicação e motivo do bloqueio quando existir. Cor pode apoiar, mas nunca substituir texto, ícone e descrição do risco.

## permissão explícita

A linguagem de permissão deve dizer exatamente qual mudança o cliente libera e em quais limites. Confirmação genérica, vaga ou implícita não substitui consentimento explícito.

## will/will-not copy

Todo card deve declarar:

- o que vai acontecer se aprovado
- o que não vai acontecer mesmo com aprovação
- quais limites continuam fechados

## ações permitidas

As únicas ações candidatas desta fase são:

- aprovar
- negar
- editar
- simular novamente

Todas permanecem candidate-only, sem efeito real, sem canal externo e sem remoção de aprovação sensível.

## estados obrigatórios

Os estados obrigatórios são `empty`, `loading`, `error`, `success` e `degraded`.

## microcopy candidata

- "Voce esta aprovando uma mudanca especifica, nao uma permissao ampla."
- "Se algo estiver ambiguo, eu vou bloquear e pedir ajuste antes de seguir."
- "Nada real sera executado por este card de aprovacao."
- "Risco e limites aparecem antes da decisao para evitar aprovacao cega."
- "Se preferir, voce pode editar ou simular novamente antes de aprovar."

## acessibilidade

O card deve ser compreensível sem depender apenas de cor, precisa manter ordem de leitura clara, rotulos inequívocos para as ações e texto suficiente para leitores assistivos distinguirem risco, permissão e bloqueio.

## critérios de BLOCK

Bloquear quando houver:

- risco sem explicação
- permissão ambígua ou genérica
- ausência de will/will-not
- tentativa de aprovar por canal externo
- pedido sensível sem aprovação explícita
- tentativa de remover aprovação necessária
- ação real, integração real, billing real, OAuth real, runtime, secrets, produção ou real_apply no escopo

## anti-escopo

Esta fase não cria UI executável, não cria fluxo real de aprovação, não usa cliente real, não envia pedido por WhatsApp, e-mail, push ou qualquer canal externo e não autoriza Bedrock PASS, produto, piloto, produção, runtime, secrets ou Project_ARIS mutation.

## handoff para BENCHUIX-12

BENCHUIX-12 deve partir desta estrutura para definir follow-up operacional da inbox sem afrouxar o requisito de risco visível, permissão explícita e synthetic-only boundary.
