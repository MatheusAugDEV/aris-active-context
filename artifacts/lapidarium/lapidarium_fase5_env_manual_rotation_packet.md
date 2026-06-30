# Lapidarium Fase 5 - Manual Env Rotation Packet

This packet was created without reading or printing `.env`.

## Scope

- F5-016 / `.env`
- Manual secret-rotation guidance only
- No runtime execution, no product integration, no Bedrock, no history rewrite

## Checklist

1. Identify which providers, services, or deployment targets use the project secrets without opening `.env`.
2. Rotate the exposed keys and tokens in the external provider dashboards.
3. Update the local `.env` file manually.
4. Invalidate or revoke the old credentials after replacement.
5. Verify the application only in a future authorized smoke-test phase.
6. Never commit `.env` to git.

## Recorded state

- `.env` exists: yes
- `.env` ignore status confirmed: yes
- `.env` content read by Codex: no
- rotation executed by Codex: no

## Note

This packet is a manual operator checklist only. It does not reveal secret values and does not authorize any runtime action.
