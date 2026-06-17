import { OWNER_ACTIONS } from "./ids.js";

export const EVENTS = Object.freeze({
  propose: { type: OWNER_ACTIONS.OWNER_PROPOSE },
  approve: { type: OWNER_ACTIONS.OWNER_APPROVE },
  refuse: { type: OWNER_ACTIONS.OWNER_REFUSE },
  block: { type: OWNER_ACTIONS.OWNER_BLOCK },
  receipt: { type: OWNER_ACTIONS.OWNER_RECEIPT },
  undo: { type: OWNER_ACTIONS.OWNER_UNDO },
  override: { type: OWNER_ACTIONS.OWNER_OVERRIDE },
  degrade: { type: OWNER_ACTIONS.OWNER_DEGRADE },
  recover: { type: OWNER_ACTIONS.OWNER_RECOVER }
});

export function navigate(screenId) {
  return { type: OWNER_ACTIONS.OWNER_NAVIGATE, screenId };
}

export function switchScenario(scenarioId) {
  return { type: OWNER_ACTIONS.OWNER_SWITCH_SCENARIO, scenarioId };
}

