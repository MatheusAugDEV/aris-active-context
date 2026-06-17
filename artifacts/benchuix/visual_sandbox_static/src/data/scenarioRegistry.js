import { barbeariaScenario } from "./scenarios/barbearia.js";
import { mercadoScenario } from "./scenarios/mercado.js";
import { escritorioScenario } from "./scenarios/escritorio.js";

export const scenarioRegistry = Object.freeze([
  barbeariaScenario,
  mercadoScenario,
  escritorioScenario
]);

export function getScenarioById(scenarioId) {
  return scenarioRegistry.find((scenario) => scenario.scenarioId === scenarioId) || scenarioRegistry[0];
}

