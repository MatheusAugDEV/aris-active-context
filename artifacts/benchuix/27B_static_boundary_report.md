# BENCHUIX-27B Static Boundary Report

## scope

BENCHUIX-27B materializes ARIS Visual Sandbox as a static source pack under `artifacts/benchuix/visual_sandbox_static/`. It remains candidate-only and synthetic-only.

## why there is no package manager

The packet is designed for auditability before productization. A package manager would create dependency resolution, lockfile, install and supply-chain questions that are outside this phase. No dependency folder or package manifest is needed to inspect the source.

## why there is no backend or API

The goal is to validate the visual contract from BENCHUIX-27A, not to prove integration behavior. State lives in memory, fixtures are local and every receipt is synthetic. A backend or API would imply runtime behavior, tenant boundary, auth and data obligations that are explicitly out of scope.

## why MODO_DEGRADADO is orthogonal

`MODO_DEGRADADO` is a global sandbox mode instead of an action state. The action can remain `AGUARDANDO_APROVACAO`, `BLOQUEADO_AUTO` or `COMPROVANTE_GERADO` while the global mode blocks owner approval, override and undo. This prevents a failure mode from erasing the action history.

## why JS/ESM plus JSDoc-style contracts

The source pack uses plain JavaScript modules so it can stay no-build and readable without a TypeScript compile step. JSDoc-style comments document the state and event contracts without creating a build pipeline.

## confusion risks mitigated

- Persistent `SandboxBadge` on every screen.
- `stateTouched: false` in fixtures, reducer output and receipts.
- `isDemo: true` on receipt examples.
- Decision labels avoid execution-like commands.
- README states that future visualization requires a separate gate.
- No dependency install, no local preview and no public deploy are performed.

## remaining limits

- This is not field usability evidence.
- This is not production copy validation.
- This is not runtime integration proof.
- This is not CRISOL admission.
- This is not a product-ready artifact.
- Any future browser preview needs a separate explicit gate.

