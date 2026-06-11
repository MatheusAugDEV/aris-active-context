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

## Roadmap classification rule

- `ROADMAP_CANONICAL.md` is the only macro roadmap authority. Exactly one such file may exist.
- Any other roadmap that attempts to define a global ARIS macro sequence outside `ROADMAP_CANONICAL.md` is `macro_roadmap_duplicate_or_conflict` and must move to `excludent/roadmaps/superseded/YYYY_MM_DD/<original_path_slug>.md` with a move manifest (old path, new path, hash before/after, reason).
- Phase- or subsystem-specific roadmaps (e.g. `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`) may remain outside `excludent/` if they are explicitly subordinate: they must declare that they do not override `ACTIVE_CONTEXT_STATE.json` or `ROADMAP_CANONICAL.md` and do not authorize real execution, product, Bedrock, secrets, real_apply, or runtime real by themselves.
- `excludent/` is never an active source for roadmap content, classification, or routing — including for already-classified roadmap files moved there.
