import { SandboxBadge } from "../components/shell/SandboxBadge.js";
import { ScenarioSwitcher } from "../components/sandbox/ScenarioSwitcher.js";
import { TodaySummary } from "../components/today/TodaySummary.js";
import { PendingItem } from "../components/today/PendingItem.js";
import { ActionContractCard } from "../components/contract/ActionContractCard.js";
import { contractFromScenario } from "../domain/contracts.js";
import { scenarioRegistry } from "../data/scenarioRegistry.js";

export function TodayScreen({ scenario, state }) {
  return `
    <section class="screen" data-screen="today">
      ${SandboxBadge()}
      ${ScenarioSwitcher(scenarioRegistry, state.scenarioId)}
      ${TodaySummary({ scenario, state })}
      ${PendingItem({ scenario, state })}
      ${ActionContractCard(contractFromScenario(scenario))}
    </section>
  `;
}

