import { SandboxBadge } from "../components/shell/SandboxBadge.js";
import { ActionContractCard } from "../components/contract/ActionContractCard.js";
import { UndoSheet } from "../components/undo/UndoSheet.js";
import { contractFromScenario } from "../domain/contracts.js";

export function RollbackScreen({ scenario, state }) {
  return `
    <section class="screen" data-screen="rollback">
      ${SandboxBadge()}
      ${UndoSheet({ scenario, state })}
      ${ActionContractCard(contractFromScenario(scenario))}
    </section>
  `;
}

