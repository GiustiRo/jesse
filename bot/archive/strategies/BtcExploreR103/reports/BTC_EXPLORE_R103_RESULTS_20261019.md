# BTC exploration R103 X03 results — 2026-10-19

Both final fulls finished without engine error. Exact planned total:3recipes×B/C=6economic fulls, no reruns or additional recipes. Root handles portfolio MTM/fill/stress/concentration audit; no promotion by this report.

- [B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127):273trades,192shorts,net11964.238131473841USDT,fees1877.50373003812,CAGR16.289896060619434%,DD−8.253965403629948%,Sharpe1.4914641051136317.
- [C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c):280trades,192shorts,net12135.87683397664USDT,fees1974.4783287352057,CAGR16.463647331914764%,DD−9.009386028595156%,Sharpe1.4804210111104101.

Both final BTC_EXPLORE:95admissible full-setup transitions,13events_occupied,79fills,79closes. Occupied measures before-state only, not13causallyblockedtrades; engine can close and enter samebar. All79supplements closed before termination. Candidate BTCshort MARKET entry can be separated from original STOP entry because original price=min(low,price−.25ATR) strictlybelow mark. Expected split192BTCshort=79new+113original; root must verify actual entry-order types/fills, not infer from totals alone. Original125controlshort differs through occupation; original long and other assets retain signals but quantities/PNL are endogenous to account.

PORT_CAPACITY both BTC45long/276short attempts; long no recuts; short25B/24Cnotional-or-weight recuts/sizedbelowtarget. All margin/riskbudget/capacityzero/lotzero0. PAXG38long attempts both,SPY20B/19C,allrecut/zeros0. Existing counters cannot distinguish notionalvsweight sublimits or measure hypothetical signals whileoccupied. TerminalC explicit SPYMARKET liquidation recorded at sessionboundary; preterminalopen1 is not unexplained residual.

Before run complete forms exact,3snapshots each exact approved frozen source. HP8same defaults as controls.10kshared/1%trade/8%aggregate/5xisolated/cap4.4/fee.00045side/.001sizingreserve,warm240,4hthreeassets+M1threefeeds,debugtruefastfalsecharttrue,2020-10-15→2025-12-31exclusive.2026closed. No source changes after results, no more runs planned.

Preliminary economic reading: highernet/CAGR/Sharpe and morefees with worseDD than corresponding B/C controls. Regularity and friction must be assessed on actual shared-account MTM and all complete/partial denominators; this report does not call objectives achieved. B/C share data and are not independent validation.

Exact final tail evidence:
```json
{
  "B": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "53937852-34a3-48c7-ab35-fac586341127",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-27T20:00:00] 📤 Order submitted | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 4.6498 | Price: 4534.93",
      "[INFO | 2025-12-28T00:01:00] Saved daily portfolio balance: 22144.68",
      "[INFO | 2025-12-29T00:01:00] Saved daily portfolio balance: 22034.48",
      "[INFO | 2025-12-29T00:21:00] ✅ Order executed | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 4.6498 | Price: 4534.93",
      "[INFO | 2025-12-29T00:21:00] Charged 9.49 as fee. Balance for USDT on Binance Perpetual Futures changed from 22155.04 to 22145.56",
      "[INFO | 2025-12-29T00:21:00] Added realized PNL of -181.32. Balance for USDT on Binance Perpetual Futures changed from 22145.56 to 21964.24",
      "[INFO | 2025-12-29T00:21:00] 🔴 Trade closed | PAXG-USDT | LONG | Binance Perpetual Futures",
      "Qty: 4.6498 | Entry: 4573.93 | Exit: 4534.93",
      "Net PnL: -200.38 USDT (-4.71%) | Fees: 19.05 USDT",
      "[INFO | 2025-12-29T00:21:00] 🏁 Position closed | PAXG-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 21964.24",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"R103\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 276, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR103\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 21964.24"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 952992,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127"
  },
  "C": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "3935efb3-2b27-4ada-86ce-94123d7a6e2c",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 22177.04",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"R103\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 276, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR103\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -113.1295(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] 📤 Order submitted | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 41.138 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ✅ Order executed | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 41.138 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] Charged 12.77 as fee. Balance for USDT on Binance Perpetual Futures changed from 22261.77 to 22249.01",
      "[INFO | 2025-12-31T00:00:00] Added realized PNL of -113.13. Balance for USDT on Binance Perpetual Futures changed from 22249.01 to 22135.88",
      "[INFO | 2025-12-31T00:00:00] 🔴 Trade closed | SPY-USDT | LONG | Binance Perpetual Futures",
      "Qty: 41.138 | Entry: 692.34 | Exit: 689.59",
      "Net PnL: -138.71 USDT (-2.44%) | Fees: 25.58 USDT",
      "[INFO | 2025-12-31T00:00:00] 🏁 Position closed | SPY-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-31T00:00:00] cancel all remaining orders of SPY-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-31T00:00:00] 🚫 Order canceled | SPY-USDT | Binance Perpetual Futures | SELL STOP | Qty: 41.138 | Price: 688.19",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 22135.88"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 978310,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c"
  }
}
```
