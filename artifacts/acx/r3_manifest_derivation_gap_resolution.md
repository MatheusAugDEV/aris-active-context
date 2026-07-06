# ACX-R3 Manifest Derivation Gap Resolution

## Diagnóstico

**DIAGNÓSTICO A**

O caminho de geração agora deriva explicitamente de `artifact_integrity_policy` em `ACTIVE_CONTEXT_STATE.json`. A leitura ocorre em `_load_artifact_integrity_policy(root)` e é injetada em `_build_authority_manifest(root)` e `validate_authority_manifest_classifications(...)`.

## Evidência da derivação

- O `grep -n "authority_manifest\|artifact_integrity_policy" tools/acx.py` mostrou a presença da política e sua leitura explícita:
  - `tools/acx.py:280-285` carrega `artifact_integrity_policy` de `ACTIVE_CONTEXT_STATE.json`.
  - `tools/acx.py:418-425` passa a política carregada para `_classify_authority_path(...)` durante a geração do manifesto.
  - `tools/acx.py:586-590` usa a mesma política na verificação do manifesto.
- `tools/acx.py:310-343` classifica `archive/` e `artifacts/` a partir de `classified_artifact_prefixes` da política viva.

## Linha exata que prova a derivação

- `tools/acx.py:280-285`:
  - `_load_artifact_integrity_policy(root)` lê `artifact_integrity_policy` de `ACTIVE_CONTEXT_STATE.json`.
- `tools/acx.py:418-425`:
  - `_build_authority_manifest(root)` carrega `artifact_policy = _load_artifact_integrity_policy(root)` e injeta esse objeto em `_classify_authority_path(...)`.
- `tools/acx.py:586-590`:
  - `validate_authority_manifest_classifications(...)` usa a mesma política viva para verificar as classificações.

## Resultado

- `authority_manifest.json` foi regenerado pelo script e não por edição manual.
- A derivação agora é rastreável até `artifact_integrity_policy` no estado canônico.

## Testes executados

- `python3 -m py_compile tools/acx.py` -> ok
- `python3 tools/acx.py authority manifest --out authority_manifest.json` -> ok
- `python3 -m unittest tests.test_acx_authority_manifest -q` -> 5 testes, ok
- `python3 -m unittest tests.test_acx_infernus_adversarial -q` -> 13 testes, ok

## Conclusão técnica

O gap original era um gap de rastreabilidade na revisão anterior; o código agora prova a derivação a partir de `artifact_integrity_policy` no estado canônico.
