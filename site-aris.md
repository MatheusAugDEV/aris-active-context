# Site Oficial ARIS Runbook

## Scope

This runbook documents the correct flow for changes, commit, push, deploy, and validation of the official ARIS site / landing page.

## Canonical Repository

- Site repository: `/home/matheus/ARIS/aris-site`
- Do not use for site work: `/home/matheus/ARIS/Project_ARIS`

## Public Domains

- Primary public domain: `https://www.meetarisia.com.br`
- Non-www domain: `https://meetarisia.com.br`

## Required Flow

```bash
cd /home/matheus/ARIS/aris-site

git config user.name "MatheusAugDEV"
git config user.email "matheuscontaextra99@gmail.com"

npm run build
git status
git add .
git commit -m "<mensagem>"
git push origin main

npx vercel ls --prod
curl -sL https://www.meetarisia.com.br | grep -o '/assets/index-[^"]*'
```

## Commit Author Diagnostic

- If `git commit` is blocked, diagnose it as `BLOCKED / COMMIT_AUTHOR_REQUIRED`.
- Required local author identity:
  - `git config user.name "MatheusAugDEV"`
  - `git config user.email "matheuscontaextra99@gmail.com"`
- Do not proceed with a site commit until the author identity is set in `/home/matheus/ARIS/aris-site`.

## Operational Rules

- Work only in `/home/matheus/ARIS/aris-site` for site changes.
- Do not perform site changes from `/home/matheus/ARIS/Project_ARIS`.
- Keep the site flow separate from ARIS runtime, Bedrock, voice, backend, frontend, action runtime, provider/model gateway, and dependency workflows in `Project_ARIS`.
- Build first, then inspect `git status`, then commit, then push.
- After push, confirm production deployment visibility with `npx vercel ls --prod`.
- After deployment, confirm the live asset fingerprint on the public domain with the `curl` command above.

## Validation Notes

- `npm run build` is the required local build check before commit.
- `git status` must be reviewed before staging.
- The live asset path check is the final public validation step in this runbook.

## Safety Boundaries

- No changes to `Project_ARIS` are part of the site workflow.
- No Bedrock fixture or active-context manipulation is part of the site workflow.
- No runtime, backend, voice, action runtime, provider/model gateway, or dependency changes belong to this site runbook.
