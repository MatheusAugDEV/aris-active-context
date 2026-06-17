import { BottomTabBar } from "./BottomTabBar.js";
import { SandboxBadge } from "./SandboxBadge.js";
import { DegradedBanner } from "./DegradedBanner.js";
import { GLOBAL_MODES } from "../../domain/ids.js";

export function AppShell({ state, scenario, children }) {
  const degraded = state.globalMode === GLOBAL_MODES.MODO_DEGRADADO ? DegradedBanner(scenario) : "";
  return `
    <main class="app-shell" data-component="AppShell" data-state-touched="false">
      <header class="topbar">
        <div>
          <p class="eyebrow">ARIS Visual Sandbox</p>
          <h1>${scenario.title}</h1>
        </div>
        ${SandboxBadge()}
      </header>
      ${degraded}
      <section class="workspace">
        ${children}
      </section>
      ${BottomTabBar(state.screenId)}
    </main>
  `;
}

