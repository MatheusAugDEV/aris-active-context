import { ActionContractCard } from "../contract/ActionContractCard.js";
import { DecisionBar } from "./DecisionBar.js";
import { contractFromScenario } from "../../domain/contracts.js";

export function ApprovalPanel({ scenario, state }) {
  return `
    <section class="approval-panel" data-component="ApprovalPanel">
      ${ActionContractCard(contractFromScenario(scenario))}
      <div class="decision-copy">
        <h3>Decisao sintetica</h3>
        <p>Leia o contrato antes de decidir. A decisao fica apenas na historia visual.</p>
      </div>
      ${DecisionBar({ scenario, globalMode: state.globalMode })}
    </section>
  `;
}

