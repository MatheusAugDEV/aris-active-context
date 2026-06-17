import { StatusPill } from "../primitives/StatusPill.js";

export function PendingItem({ scenario, state }) {
  return `
    <article class="pending-item" data-component="PendingItem">
      <div>
        <p class="eyebrow">Item sensivel</p>
        <h3>${scenario.title}</h3>
        <p>${scenario.risk.plainLanguage}</p>
      </div>
      ${StatusPill(state.actionState)}
    </article>
  `;
}

