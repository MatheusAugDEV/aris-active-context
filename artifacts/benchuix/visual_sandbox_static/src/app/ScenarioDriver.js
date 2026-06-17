import { getScenarioById } from "../data/scenarioRegistry.js";
import { initialState, reducer } from "../domain/state.js";
import { navigate, switchScenario } from "../domain/events.js";
import { OWNER_ACTIONS } from "../domain/ids.js";

export function createScenarioDriver(render) {
  let currentState = initialState;

  function dispatch(action) {
    currentState = reducer(currentState, action);
    render(currentState, getScenarioById(currentState.scenarioId), dispatch);
  }

  function bind(root) {
    root.querySelectorAll("[data-screen]").forEach((button) => {
      button.addEventListener("click", () => dispatch(navigate(button.dataset.screen)));
    });
    root.querySelectorAll("[data-scenario]").forEach((button) => {
      button.addEventListener("click", () => dispatch(switchScenario(button.dataset.scenario)));
    });
    root.querySelectorAll("[data-action]").forEach((button) => {
      button.addEventListener("click", () => dispatch({ type: OWNER_ACTIONS[button.dataset.action] || button.dataset.action }));
    });
  }

  return {
    start(root) {
      render(currentState, getScenarioById(currentState.scenarioId), dispatch);
      bind(root);
    },
    bind
  };
}

