import {
  arisCanPropose,
  arisCannotAutoApproveSensitiveAction,
  degradedBlocksOwnerControls,
  refusalOrBlockGeneratesReceipt,
  receiptsAreDemoOnly,
  stateTouchedAlwaysFalse
} from "../domain/invariants.js";
import { scenarioRegistry } from "../data/scenarioRegistry.js";

export const invariant_results = Object.freeze({
  aris_can_propose: arisCanPropose(),
  aris_cannot_auto_approve: arisCannotAutoApproveSensitiveAction(),
  degraded_blocks_owner_controls: degradedBlocksOwnerControls(),
  refusal_or_block_generates_receipt: refusalOrBlockGeneratesReceipt(),
  state_touched_always_false: stateTouchedAlwaysFalse(scenarioRegistry),
  receipts_are_demo_only: receiptsAreDemoOnly(scenarioRegistry)
});

