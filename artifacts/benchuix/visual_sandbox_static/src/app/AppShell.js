import { AppShell as VisualShell } from "../components/shell/AppShell.js";
import { renderScreen } from "./navigation.js";

export function renderApp({ state, scenario }) {
  return VisualShell({
    state,
    scenario,
    children: renderScreen({ scenario, state })
  });
}

