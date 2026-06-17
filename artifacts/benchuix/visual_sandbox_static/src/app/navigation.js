import { SCREEN_IDS } from "../domain/ids.js";
import { ApproveScreen } from "../screens/ApproveScreen.js";
import { DegradedScreen } from "../screens/DegradedScreen.js";
import { HistoryScreen } from "../screens/HistoryScreen.js";
import { RollbackScreen } from "../screens/RollbackScreen.js";
import { TodayScreen } from "../screens/TodayScreen.js";

export function renderScreen({ scenario, state }) {
  if (state.screenId === SCREEN_IDS.APPROVE) return ApproveScreen({ scenario, state });
  if (state.screenId === SCREEN_IDS.HISTORY) return HistoryScreen({ scenario, state });
  if (state.screenId === SCREEN_IDS.ROLLBACK) return RollbackScreen({ scenario, state });
  if (state.screenId === SCREEN_IDS.DEGRADED) return DegradedScreen({ scenario, state });
  return TodayScreen({ scenario, state });
}

