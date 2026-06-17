import { SCREEN_IDS } from "../../domain/ids.js";

export function BottomTabBar(activeScreenId) {
  const items = [
    ["Hoje", SCREEN_IDS.TODAY],
    ["Aprovar", SCREEN_IDS.APPROVE],
    ["Historico", SCREEN_IDS.HISTORY],
    ["Desfazer", SCREEN_IDS.ROLLBACK],
    ["Falha", SCREEN_IDS.DEGRADED]
  ];
  return `
    <nav class="bottom-tab-bar" aria-label="Navegacao visual">
      ${items.map(([label, screenId]) => `
        <button class="tab ${screenId === activeScreenId ? "is-active" : ""}" data-screen="${screenId}">
          ${label}
        </button>
      `).join("")}
    </nav>
  `;
}

