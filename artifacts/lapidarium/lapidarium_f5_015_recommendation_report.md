# F5-015 Nested Git Repository Review

## Decision

`QUARANTINE`

## Why

- The nested repo is a third-party GitHub project with its own remote origin.
- The current checkout is a detached snapshot at `b8c39ae`, while local `main` and `origin/main` are at `24481f8`.
- Project_ARIS references the snapshot in 31 governance/test files, so removal would break read-only audit flows.
- There is no evidence of product/runtime consumption from Project_ARIS.
- The nested repo is already isolated under `external/mcp_candidates` and is ignored by the parent `.gitignore`.

## Files really used in the nested repo

- `src/index.ts`
- `src/security.ts`
- `src/data.ts`
- `src/tools.ts`
- `src/search.ts`
- `src/embeddings.ts`
- `package.json`
- `package-lock.json`
- `server.json`
- `tsconfig.json`
- `README.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `.gitignore`

## Risk summary

- Supply chain risk: medium-high
- Removal risk: high
- Runtime dependency: no
- Governance/test dependency: yes

## Recommendation

Keep the repo quarantined and read-only. If Project_ARIS ever needs to consume it as an operational dependency, convert it explicitly to a submodule or vendorized dependency with an explicit policy and commit pin.
