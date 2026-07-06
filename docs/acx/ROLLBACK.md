# ACX R4 Rollback

This document records the rollback procedure for ACX-R4 manual write blocking.

1. Confirm why the hook blocked.
2. Use `ACX_DISABLE_HOOK=1` only in an emergency.
3. If R4 itself must be reverted, run `git revert <r4_commit_sha>`.
4. If the ledger and state are inconsistent, regenerate the state with `python3 tools/acx.py fold` when applicable.
5. Run `python3 tools/acx.py verify-chain --ledger .acx/ledger.jsonl`.
6. Run `python3 tools/acx_validate.py`.
7. Never delete ledger lines to perform a rollback.
8. The correct rollback for state changes is a compensating event in a later phase, not destructive ledger editing.

The bypass flag does not replace the rollback procedure. It only disables the local hook in an emergency and does not authorize destructive repair.
