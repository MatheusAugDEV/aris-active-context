# BEDROCK_GATE — Chão Inviolável do ARIS

## Função
O Bedrock Gate é a primeira camada obrigatória de aprovação de qualquer fase, arquitetura, prompt Codex, feature, refactor, roadmap ou decisão operacional do ARIS.

Ele responde uma pergunta simples:

> Esta decisão viola alguma fundação inviolável do ARIS?

Se a resposta for sim, o resultado deve ser `BLOCKED`, mesmo que testes locais, artifacts, revisão humana ou gates específicos da fase pareçam passar.

## Ordem obrigatória de aprovação
Toda fase futura deve ser avaliada nesta ordem:

1. `BEDROCK_GATE`
2. `NORTH_POLE_ALIGNMENT`
3. `PHASE_SPECIFIC_GATES`
4. `ACTIVE_CONTEXT_UPDATE`
5. `COMMIT_PUSH_HASH_FINAL`

Nenhum gate posterior pode compensar falha no Bedrock Gate.

## Regras invioláveis
Uma fase, prompt ou alteração deve ser bloqueada se:

- mentir sobre capacidade, evidência, execução real, teste real ou status de produção;
- promover produto, cliente real, venda ou produção sem gate futuro explícito;
- alterar runtime, frontend, backend, action runtime, rede, áudio, Obsidian, MCP ou dependências fora do escopo autorizado;
- ativar MCP, escrever config MCP, escrever no vault, fazer bulk-read de Obsidian ou liberar rede sem gate explícito;
- instalar dependências, executar scripts externos, expor segredos ou ler ambiente fora de allowlist autorizada;
- burlar `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `NORTH_POLE.md` ou source-of-truth oficial;
- tratar chat, intenção, roadmap conceitual, prompt ou memória como autorização materializada;
- transformar WARN em PASS sem evidência objetiva;
- avançar fase sem atualizar active-context quando a fase exige materialização;
- remover controle crítico para reduzir atrito sem mecanismo equivalente de segurança;
- criar automação real sem plano, permissão, ledger e rollback/compensação quando aplicável.

## Resultado
- `PASS`: nenhuma fundação violada.
- `WARN`: fundação preservada, mas há dívida ou ambiguidade controlada que precisa ser registrada.
- `BLOCKED`: fundação violada ou evidência insuficiente para provar preservação.
- `INVALID`: a fase não prova o que afirma provar.

## Relação com NORTH_POLE
O Bedrock Gate é o chão. O North Pole é o norte.

O Bedrock Gate impede dano, mentira, bypass e ativação indevida. O North Pole exige excelência, simplicidade, eficiência, valor e vitória técnica/produto.

Uma fase só pode passar se preservar o chão e aproximar o ARIS do norte.

## Status operacional
Este contrato não autoriza implementação, runtime mutation, rede, MCP, vault write, dependency install, product promotion ou cliente real.

A próxima ação operacional continua sendo definida exclusivamente por `NEXT_ACTION.md`.
