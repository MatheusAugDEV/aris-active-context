import { SandboxBadge } from "../components/shell/SandboxBadge.js";
import { DegradedBanner } from "../components/shell/DegradedBanner.js";
import { ActionContractCard } from "../components/contract/ActionContractCard.js";
import { contractFromScenario } from "../domain/contracts.js";

export function DegradedScreen({ scenario }) {
  return `
    <section class="screen degraded-screen" data-screen="degraded" data-component="DegradedScreen">
      ${SandboxBadge()}
      ${DegradedBanner(scenario)}
      <div class="degraded-copy">
        <h2>Nao e seguro mostrar decisao agora</h2>
        <p>Apenas comprovantes e proximos passos seguros ficam visiveis.</p>
      </div>
      ${ActionContractCard(contractFromScenario(scenario))}
    </section>
  `;
}

