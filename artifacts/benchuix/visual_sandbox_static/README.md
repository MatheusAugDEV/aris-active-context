# ARIS Visual Sandbox Static Prototype

This artifact is `BENCHUIX-27B`, a candidate-only source pack derived from `BENCHUIX-27A`.

It is a synthetic visual sandbox. It is not a product, not a runtime, not a pilot, not a backend, not an API, not an auth surface and not a database. It uses local synthetic fixtures only and does not execute real automation.

Boundary:

- candidate-only and synthetic-only;
- no real customer, payment, schedule, document, auth or integration data;
- no backend, API, database or auth provider;
- no package manager is required, including npm;
- no package manifest is created;
- no dependency folder is created;
- no local preview was run in this phase;
- no localhost or browser execution is required by this packet;
- no CRISOL admission;
- no live route opening;
- no product-ready claim;
- future visualization requires a separate explicit gate.

The source uses static JavaScript modules with JSDoc-style contracts. It is intentionally no-build: the files are auditable as source artifacts and must not be promoted as a deployed product.

`MODO_DEGRADADO` is modeled as an orthogonal global mode. It blocks owner approval, owner override and owner undo while leaving the current action state intact.

