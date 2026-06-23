# Onboarding First Access

## O que a tela é

Uma camada local de boas-vindas mostrada antes do dashboard sandbox da barbearia.
Ela apresenta o ARIS com leitura curta, visual escuro premium, marca centralizada e duas saídas simples: `Começar` ou `pular`.

## Quando aparece

A tela aparece quando `localStorage["aris_benchuix_onboarding_seen_v1"] !== "true"`.
Esse é o estado de primeiro acesso deste navegador para o preview sandbox.

## Quando não aparece

A tela não aparece quando a chave local já foi gravada como `true`.
Nesse caso o usuário entra direto no dashboard.

## Como o usuário entra no dashboard

- `Começar` grava `aris_benchuix_onboarding_seen_v1 = "true"` e revela o dashboard.
- `pular` grava `aris_benchuix_onboarding_seen_v1 = "true"` e revela o dashboard.

## Como rever a tela

Em `Meu Negócio` existe a ação local `Ver boas-vindas novamente`.
Ela limpa a chave de `localStorage` e recarrega o preview local para reabrir o first access pelo mesmo caminho real do boot do dashboard.

## Por que isso melhora a primeira experiência

A entrada deixa o primeiro contato mais claro e mais calmo.
O usuário vê primeiro a promessa central do painel, entende que continua no controle e só então mergulha na rotina operacional.
Isso reduz ruído de primeira leitura sem transformar o preview em landing page.

## Por que isso não é produto real

- A experiência é candidate-only.
- Tudo permanece sandbox-only e synthetic-only.
- Não há backend, rede, integração externa, segredo, cobrança ou runtime real.
- O comportamento existe apenas dentro do HTML local do draft BenchUIX.
