# READ_PROFILE

## Levels
- `boot_minimal`: read only the canonical boot files.
- `phase_local`: add the current phase artifacts, report, and the files touched by the current gate.
- `evidence_expanded`: add the smallest supporting gate or source-of-truth docs needed to validate a claim.
- `historical_audit_only`: consult preserved historical files only when an audit question requires them.
- `forbidden_bulk_read`: archive-wide, docs-wide, or Obsidian bulk reads; not permitted.

## Rules
- Start with the active-context canonical files, then phase artifacts, then source-of-truth docs only when required.
- Query-first for Obsidian and docs; never use Vault-wide or docs-wide dumps by default.
- Keep archive and historical corpus reads off by default.
- Keep `DECISION_LOCKS.md` authoritative for boundaries and do not let this profile override it.
- Treat legacy Bedrock, Lab, and roadmap-overlay files as historical audit material unless a later canonical gate explicitly reactivates them.
- `archive/LAB_STATUS.md`, `archive/LAB_VERDICTS.md`, `archive/PROJECT_CONTEXT_ARIS.md`, and `archive/ARIS_ROADMAP_R0_F120.md` are archived historical-only residue; they are not part of any boot or mandatory read sequence.
- Keep Product Loop L1.15 as closed evidence and H0 as materialized design-only evidence.

## Compatibility
- This profile narrows reading; it does not expand authority.
- This profile does not authorize implementation by itself.
