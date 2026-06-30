# LAPIDARIUM FASE 5 — Cleanup Execution Report
## Authorized Minimal Safe Set

**Phase:** `LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_AUTHORIZED_MINIMAL_SAFE_SET`  
**Date:** 2026-06-30  
**Decision:** PASS  
**SHA before:** `0a64f632bd25e50c29112a4468298b72ee31af73`

---

## Summary

- 9 items authorized and removed
- 7 items not authorized — all preserved
- Precheck: PASS
- Postcheck: PASS
- Validator: pass
- CI: green
- HEAD == origin/main: ✓
- No scope escape, no secrets accessed

---

## Items Removed

| Item | Path | Type | Action |
|------|------|------|--------|
| F5-001 | `temp_audit/ambiguity_resolver_report.md` | tracked | `git rm` |
| F5-002 | `temp_audit/ambiguity_resolver_summary.json` | tracked | `git rm` |
| F5-003 | `temp_audit/ambiguity_resolution_samples.jsonl` | tracked | `git rm` |
| F5-007 | `legacy/wake/wake.py.backup` | tracked | `git rm` |
| F5-008 | `legacy/experiments/tart=always` | untracked | `rm` |
| F5-009 | `debug_audio.wav` | untracked | `rm` |
| F5-010 | `teste.wav` | untracked | `rm` |
| F5-011 | `[:alnum:] \n \` | tracked | `git rm` (via subprocess, shell=False) |
| F5-012 | `how --stat --summary 5dda82a` | tracked | `git rm` |

### F5-011 Note
Path resolved via `git ls-files -z` null-delimited output, decoded as `'[:alnum:] \\n \\'`.
Passed as exact list element to `subprocess.run(['git', 'rm', '--', name], shell=False)`.
No glob, no shell expansion, no metacharacter risk.

---

## Items Preserved (Not Authorized)

| Item | Path | Reason |
|------|------|--------|
| F5-004 | `temp_audit/f15z1` | Gate marker check pending |
| F5-005 | `temp_audit/f15z1_post_z3` | Gate marker check pending |
| F5-006 | `legacy/wake/tts.py.backup` | May be only TTS code copy |
| F5-013 | `legacy/experiments/genai` | BLOCKED — PostScript binary |
| F5-014 | `legacy/experiments/threading` | BLOCKED — PostScript binary |
| F5-015 | `external/mcp_candidates/gogogadgetbytes_smart_connections_mcp/` | BLOCKED — Nested git repo |
| F5-016 | `.env` | KEEP — correctly gitignored |

---

## Artifacts Created

1. `lapidarium_fase5_cleanup_execution_authorized_minimal_packet.json`
2. `lapidarium_fase5_cleanup_execution_precheck.json`
3. `lapidarium_fase5_cleanup_execution_actions_log.json`
4. `lapidarium_fase5_cleanup_execution_postcheck.json`
5. `lapidarium_fase5_cleanup_execution_rollback_reference.json`
6. `lapidarium_fase5_cleanup_execution_no_scope_escape_attestation.json`
7. `lapidarium_fase5_cleanup_execution_validation_evidence.json`
8. `lapidarium_fase5_cleanup_execution_report.md` (this file)

---

## Rollback

Tracked files (F5-001–003, F5-007, F5-011, F5-012) are recoverable via:

```
git checkout 0a64f632bd25e50c29112a4468298b72ee31af73 -- <path>
```

Untracked files (F5-008, F5-009, F5-010) were never in git history — not recoverable from git.

---

## Recommended Next Steps

1. **F5-006** — Review `legacy/wake/tts.py.backup` separately. Confirm if an alternate TTS code copy exists before authorizing removal.
2. **F5-004/F5-005** — Read `temp_audit/f15z1` and `temp_audit/f15z1_post_z3` content; confirm if they are gate markers or disposable.
3. **F5-013/F5-014** — Emit separate prompt for PostScript binary decision (F4-FIND-003). Confirm origin before any removal.
4. **F5-015** — Emit separate prompt for nested git repo strategy (F4-FIND-002): submodule / vendor / remove / quarantine.
5. **Secret rotation** — See `lapidarium_f4_find001_rotation_checklist.md`. Independent of cleanup phases.
