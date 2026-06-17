import { ACTION_STATES, GLOBAL_MODES, OWNER_ACTIONS, SCENARIO_IDS, SCREEN_IDS } from "./ids.js";
import { nextActionState, receiptRequiredForState } from "./stateMachine.js";

export const initialState = Object.freeze({
  screenId: SCREEN_IDS.TODAY,
  scenarioId: SCENARIO_IDS.BARBEARIA,
  actionState: ACTION_STATES.DETECTADO,
  globalMode: GLOBAL_MODES.NORMAL,
  stateTouched: false,
  generatedReceipt: false,
  isDemo: true
});

/**
 * Pure reducer for the static visual sandbox.
 * @param {typeof initialState} state
 * @param {{type:string, screenId?:string, scenarioId?:string}} action
 */
export function reducer(state, action) {
  if (action.type === OWNER_ACTIONS.OWNER_NAVIGATE) {
    return { ...state, screenId: action.screenId, stateTouched: false };
  }
  if (action.type === OWNER_ACTIONS.OWNER_SWITCH_SCENARIO) {
    return {
      ...initialState,
      scenarioId: action.scenarioId,
      stateTouched: false
    };
  }
  if (action.type === OWNER_ACTIONS.OWNER_DEGRADE) {
    return { ...state, globalMode: GLOBAL_MODES.MODO_DEGRADADO, screenId: SCREEN_IDS.DEGRADED, stateTouched: false };
  }
  if (action.type === OWNER_ACTIONS.OWNER_RECOVER) {
    return { ...state, globalMode: GLOBAL_MODES.NORMAL, screenId: SCREEN_IDS.TODAY, stateTouched: false };
  }

  const actionState = nextActionState(state.actionState, action.type, state.globalMode);
  const generatedReceipt = state.generatedReceipt || receiptRequiredForState(actionState);
  return {
    ...state,
    actionState,
    generatedReceipt,
    stateTouched: false,
    isDemo: true
  };
}

