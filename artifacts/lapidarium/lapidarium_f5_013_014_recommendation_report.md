# F5-013 / F5-014 PostScript Binary Review

## Decision

`BLOCKED`

## Summary

`legacy/experiments/genai` and `legacy/experiments/threading` are large untracked files that are also ignored by `.gitignore`. Both are identified as PostScript DSC Level 3.0 documents created by ImageMagick.

## Evidence

- `F5-013` is `20,919,684` bytes.
- `F5-014` is `6,976,967` bytes.
- Both files show `%!PS-Adobe-3.0` headers and `%%Creator: (ImageMagick)`.
- Both files have no live references in `src`, `tests`, `docs`, `.github`, or top-level markdown.
- Governance references exist in `artifacts/lapidarium/` and the active-context mirrors.

## Why Blocked

The files are not needed by runtime or product code, but the original source and intent are still unconfirmed. Removing them would be irreversible at the filesystem level because they are not tracked in git history.

## Recommendation

Keep both items blocked until the operator explicitly confirms:

1. What created the files.
2. Whether the content is still needed.
3. Whether a backup is required before any removal or quarantine.
