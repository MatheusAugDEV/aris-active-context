import { renderApp } from "./app/AppShell.js";
import { createScenarioDriver } from "./app/ScenarioDriver.js";

const root = document.getElementById("aris-visual-sandbox-root");
let driver;

function render(state, scenario, dispatch) {
  root.innerHTML = renderApp({ state, scenario });
  driver.bind(root);
  window.__ARIS_VISUAL_SANDBOX_STATE__ = {
    scenarioId: state.scenarioId,
    actionState: state.actionState,
    globalMode: state.globalMode,
    stateTouched: false,
    isDemo: true
  };
}

driver = createScenarioDriver(render);
driver.start(root);
