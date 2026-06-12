import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent


def _load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "validate_active_context_state",
        ROOT / "scripts" / "validate_active_context_state.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class Purg04ValidatorScopeRepairTests(unittest.TestCase):
    def test_current_purg_route_allows_preserved_if08_w05_historical_blocker(self):
        module = _load_validator_module()
        state = json.loads((ROOT / "ACTIVE_CONTEXT_STATE.json").read_text(encoding="utf-8"))

        self.assertTrue(module._state_preserves_if08_w05_historical_blocked(state))

        decision = json.loads(
            (PROJECT_ROOT / "artifacts/infernus/if08_w05_post_sync_review_decision_2026_06_07.json").read_text(
                encoding="utf-8"
            )
        )
        summary = json.loads(
            (PROJECT_ROOT / "artifacts/infernus/if08_w05_post_sync_review_summary_2026_06_07.json").read_text(
                encoding="utf-8"
            )
        )
        no_execution = json.loads(
            (PROJECT_ROOT / "artifacts/infernus/if08_w05_post_sync_no_execution_attestation_2026_06_07.json").read_text(
                encoding="utf-8"
            )
        )

        module._require_if08_w05_historical_blocked_payload(
            decision,
            "project post-sync decision",
            require_next_recommended_step=True,
        )
        module._require_if08_w05_historical_blocked_payload(
            summary,
            "project post-sync summary",
            require_next_recommended_step=True,
        )
        module._require_if08_w05_historical_blocked_payload(
            no_execution,
            "project post-sync no_execution",
            require_next_recommended_step=False,
        )

    def test_historical_blocker_policy_rejects_pass_payload(self):
        module = _load_validator_module()
        payload = {
            "phase_id": "IF-08-W05-POST-SYNC-REVIEW",
            "decision": "pass",
            "status": "if08_w05_post_sync_review_pass",
            "next_recommended_step": "prepare_if08_w1_context_memory_rag_preflight_readiness",
            "w1_execution_performed": False,
            "w1_execution_allowed": False,
        }

        with self.assertRaises(SystemExit):
            module._require_if08_w05_historical_blocked_payload(
                payload,
                "project post-sync decision",
                require_next_recommended_step=True,
            )
