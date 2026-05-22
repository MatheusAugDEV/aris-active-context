# READ_PROFILE

## Levels
- `boot_minimal`: read only the four boot files.
- `phase_local`: add the current phase artifacts, report, and the files touched by the current gate.
- `evidence_expanded`: add the smallest supporting gate or source-of-truth docs needed to validate a claim.
- `source_of_truth_validation`: use authoritative docs, ledger, or policies only when a claim must be checked.
- `forbidden_bulk_read`: archive-wide, docs-wide, or Obsidian bulk reads; not permitted.

## Rules
- Start with active-context, then phase artifacts, then source-of-truth docs only when required.
- Query-first for Obsidian and docs; never use Vault-wide or docs-wide dumps by default.
- Keep archive and historical corpus reads off by default.
- Keep `DECISION_LOCKS.md` authoritative for boundaries and do not let this profile override it.
- Keep `F21B` preserved and `F21-A61` blocked.

## Compatibility
- This profile is compatible with D3/D4 and does not authorize implementation by itself.
- This profile narrows reading; it does not expand authority.
