import { StatusPill } from "../primitives/StatusPill.js";

export function TodaySummary({ scenario, state }) {
  return `
    <section class="summary-panel" data-component="TodaySummary" data-state-touched="false">
      <div>
        <p class="eyebrow">Hoje sintetico</p>
        <h2>${scenario.event.summary}</h2>
      </div>
      ${StatusPill(state.actionState)}
      <p>${scenario.event.initialState}</p>
      <p class="safe-note">Estado real tocado? nao.</p>
    </section>
  `;
}

