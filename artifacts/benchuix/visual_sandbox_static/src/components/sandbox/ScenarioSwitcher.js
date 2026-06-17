export function ScenarioSwitcher(scenarios, activeScenarioId) {
  return `
    <div class="scenario-switcher" data-component="ScenarioSwitcher">
      ${scenarios.map((scenario) => `
        <button class="scenario-chip ${scenario.scenarioId === activeScenarioId ? "is-active" : ""}" data-scenario="${scenario.scenarioId}">
          ${scenario.shortLabel}
        </button>
      `).join("")}
    </div>
  `;
}

