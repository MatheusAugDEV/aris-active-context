# BENCHUIX-27E File Preview Compatibility Report

## observed defect

The operator runbook from BENCHUIX-27D instructed a direct local file open, but the existing preview entry used `type=module` plus ESM imports. That can leave the browser on a blank screen when the file is opened through `file://`.

## why file:// plus type=module and imports can fail

The current `index.html` points to `src/App.js` as a module entry. That file then depends on a chain of imported modules. In a direct local-file context, browsers can reject or partially fail module loading and the root never renders.

## why no local server was used

This phase stays inside the existing guardrail from 27D: no localhost, no preview execution by Codex and no server setup. The fix therefore had to remain artifact-only and compatible with direct file open.

## why no npm or package manager was used

The source pack is still candidate-only, synthetic-only and no-build. Adding a package manager or build step would violate the boundary already established by BENCHUIX-27B and BENCHUIX-27D.

## new file to open

The operator should now open:

- `artifacts/benchuix/visual_sandbox_static/index_file_preview.html`

This file contains inline CSS and inline JS, removes module loading for the preview surface and keeps the synthetic ARIS Visual Sandbox auditable in one file.

## what remains out of scope

- no browser execution by Codex
- no localhost
- no npm, pnpm or yarn
- no package manifest
- no node_modules
- no backend or API
- no real data
- no runtime or product execution
- no CRISOL admission
