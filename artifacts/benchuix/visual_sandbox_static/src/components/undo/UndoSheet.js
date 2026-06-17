import { StateTouchedIndicator } from "../contract/StateTouchedIndicator.js";

export function UndoSheet({ scenario }) {
  return `
    <section class="undo-sheet" data-component="UndoSheet">
      <p class="eyebrow">Rollback / Desfazer</p>
      <h3>${scenario.rollbackOrCompensation.label}</h3>
      <p>${scenario.rollbackOrCompensation.effect}</p>
      <p>Tipo: ${scenario.rollbackOrCompensation.type}</p>
      ${StateTouchedIndicator()}
    </section>
  `;
}

