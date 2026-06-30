# F4-FIND-001 — Rotation Checklist (Manual — Operator Only)

> **Fase:** LAPIDARIUM_SECURITY_F4_FIND_001_ENV_CONTAINMENT
> **Data:** 2026-06-30
> **Finding:** F4-FIND-001 — `.env` identificado como `seems_source_genuine` com `git_tracked=True`

## Resultado da Contenção Técnica

**O `.env` NÃO estava git-tracked.** A verificação direta com `git ls-files -- .env` e
`git log --all --diff-filter=A -- .env` confirmaram que o arquivo nunca foi commitado.
O campo `git_tracked=True` no dataset da Fase 1 foi um falso positivo do scanner.

O `.gitignore` já contém regras adequadas (linha 1: `.env`, linha 6: `*.env`).
Nenhuma ação técnica de `git rm --cached` foi necessária.

---

## Ações Manuais Pendentes para o Operador

### 1. Avaliar Risco de Exposição

- [ ] O arquivo `.env` contém credenciais reais? (verificar localmente SEM imprimir no chat)
- [ ] O arquivo `.env` foi compartilhado por outros meios além do git? (email, Slack, pastebin, etc.)
- [ ] O arquivo `.env` foi acessado por outros sistemas ou processos?
- [ ] Existem logs ou backups que possam ter capturado os valores?

### 2. Identificar Serviços (sem colar valores no chat)

Para cada chave/token/senha no `.env` local, identificar o serviço correspondente:
- [ ] APIs de LLM (Anthropic, OpenAI, etc.)
- [ ] Serviços de banco de dados
- [ ] Serviços de armazenamento
- [ ] APIs de terceiros
- [ ] Chaves de autenticação/assinatura

### 3. Rotacionar Credenciais (se risco de exposição for avaliado como presente)

Para cada serviço identificado:
- [ ] Acessar console/dashboard do provedor
- [ ] Gerar nova chave/token/senha
- [ ] Revogar a chave antiga IMEDIATAMENTE após gerar a nova
- [ ] Atualizar o `.env` local com os novos valores
- [ ] Atualizar quaisquer secrets de ambiente seguro (GitHub Secrets, Vault, etc.)
- [ ] Validar funcionamento da aplicação localmente com os novos valores

### 4. Validar Cobertura do `.gitignore`

- [x] `.env` na linha 1 do `.gitignore` — JÁ CONFIRMADO
- [x] `*.env` na linha 6 do `.gitignore` — JÁ CONFIRMADO
- [x] `.env.example` com negação `!.env.example` — JÁ CONFIRMADO
- [ ] Verificar se `.env.example` tem os nomes corretos das variáveis sem os valores reais

### 5. Decisão Sobre Limpeza de Histórico

Como `.env` nunca foi commitado (confirmado nesta fase), **limpeza de histórico Git NÃO é necessária.**

Se em algum momento futuro for descoberto que `.env` foi commitado em algum branch ou
stash não verificado:
- [ ] Documentar o commit SHA
- [ ] Abrir fase separada para `git filter-repo` ou BFG Repo Cleaner
- [ ] Coordenar com todos os colaboradores antes de reescrever histórico
- [ ] Fazer force push coordenado (requer autorização explícita do operador)

### 6. Verificação Final

- [ ] `git ls-files -- .env` retorna vazio em todos os repos
- [ ] `git check-ignore -v .env` confirma regra ativa
- [ ] Aplicação funciona com novas credenciais
- [ ] Nenhuma credencial antiga ainda ativa nos provedores

---

## Nota de Falso Positivo no Dataset

O campo `git_tracked=True` para `.env` no dataset `fase1_triagem_classificacao.json`
(gerado em 2026-06-26 do commit `a1f433f4d285850bcd628c1bc5f619f85f78ef33`) foi
identificado como **falso positivo do scanner**. Este é um indicativo adicional de que
o bug do generator da Fase 1 (F4-FIND-004) pode afetar outros campos além de quoting —
o `LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR` deve investigar o método de
detecção de `git_tracked`.

---

*Este checklist é para uso manual do operador. Nenhum valor de segredo deve ser
inserido em chats, artifacts ou commits.*
