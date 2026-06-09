# EXCLUDENT POLICY

`excludent/` is the logical exclusion zone of ARIS.

Files under `excludent/` are not active context, not active roadmap, not source-of-truth,
not evidence for current routing, not prompt input, not boot input, and not decision authority.

## Rules

1. Do not read `excludent/` during normal boot.
2. Do not include `excludent/` in mandatory read-first paths.
3. Do not derive `next_phase` from `excludent/`.
4. Do not derive authorization from `excludent/`.
5. Do not include `excludent/` in context packs.
6. Do not cite `excludent/` as active evidence.
7. Do not use `excludent/` to repair current route.
8. Only inspect `excludent/` when the operator explicitly requests forensic review.

## Status

`excludent/` means:

- logically dead;
- superseded;
- not operational;
- not canonical;
- not visible as active project direction.

## Difference from archive/

```
archive/:
  historical auditable material that may be consulted when explicitly relevant.

excludent/:
  dead/annulled material, no default reading, no authority, no context,
  no route, and no operational use.
```

## Allowed use

Only forensic audit by explicit operator request.

## Forbidden use

Any automatic or default reading.

## Post-IF11 supersession

After IF-11, `project_mirror/docs/infernus_full/infernus_full_canonroadmap.md` is no longer active direction.
It must be treated as superseded stub only, with forensic content retained under:
`excludent/infernus/roadmaps/infernus_full_canonroadmap.md`

The active post-Infernus technical roadmap document is:
`project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`

This supersession changes document authority only. It does not open live route, does not authorize execution, and does not override `ACTIVE_CONTEXT_STATE.json` or `ROADMAP_CANONICAL.md`.
