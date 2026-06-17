# BENCHUIX-27D Local Static Preview Operator Runbook

## objective

Allow the operator to inspect the ARIS Visual Sandbox manually as a local static file while preserving the candidate-only, synthetic-only and non-product boundary.

## preview mode declaration

- This preview is manual.
- This preview is local.
- This preview is synthetic.
- This preview is candidate-only.
- Codex does not execute the browser in this phase.

## file to open

Open this file directly in the browser from the local filesystem:

- `artifacts/benchuix/visual_sandbox_static/index_file_preview.html`

Preferred instruction:

- Open the HTML file directly by local file path.

## prohibited instructions

- Do not run `npm`.
- Do not run `pnpm`.
- Do not run `yarn`.
- Do not run any local server.
- Do not open `localhost`.
- Do not connect API or backend.
- Do not use real data.
- Do not log in.
- Do not publish any deploy.

## screens to verify

- Hoje
- Aprovar
- Historico / Comprovantes
- Rollback / Desfazer
- Falha / Modo degradado

## scenarios to verify

- barbearia
- mercado
- escritorio

## observation questions

1. O que ARIS vai fazer?
2. O que ARIS nao vai fazer?
3. Qual risco existe?
4. Precisa aprovacao?
5. Qual evidencia aparece?
6. Da para desfazer ou compensar?
7. Esta claro que nenhum estado real foi tocado?

## stop criteria

Stop the preview immediately:

- if it looks like a real product;
- if SandboxBadge is missing;
- if the UI asks for API, backend or login;
- if any real data appears;
- if the UI suggests real execution.

## operator notes

- The preview is only for controlled visual inspection.
- The preview does not admit CRISOL.
- The preview does not open a live route.
- The preview does not authorize runtime, backend, secrets or product execution.
