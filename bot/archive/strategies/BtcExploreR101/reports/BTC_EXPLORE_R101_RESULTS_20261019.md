# BTC explore R101 X01 results and logs — 2026-10-19

Both fulls finished without engine exception. No recipe changes or reruns. Root's economic MTM/fill audit remains separate.

- [B](http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8):206 trades,net9234.194391279196USDT,fees1361.9208307843405,CAGR13.366850134409681%,DD−7.496635153613385%,Sharpe1.3239806209896494.
- [C](http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb):213 trades,net9407.82622551297USDT,fees1453.76741677675,CAGR13.562426758782898%,DD−8.168012803517177%,Sharpe1.3154302129959166.

BTC_EXPLORE final counts={} in BOTH; no events reached the complete admissible-event counter, no supplemental fills/closes recorded. Metrics match original controls, with only floating precision differences in Sharpe. This is zero incremental benefit, not a new independent confirmation of baseline. Counters do not identify whether volume, candle geometry, stop geometry or validation rejected candidates; do not claim rare market events or total missing input as a proven cause. No threshold or source changed to obtain events.

Three draft strategy snapshots verified exact against approved sources for both sessions; complete form readbacks exact. Hyperparameter declarations unchanged; root has independent snapshots/forms PASS. Normal motor,debugtrue,charttrue,fastfalse,warm240,4hthreeassets+M1threefeeds,10kshared/1%trade/8%aggregate/5xisolated/cap4.4/.00045side/.001sizingreserve.2020-10-15→2025-12-31exclusive,2026closed.

PORT_CAPACITY final:
- BTC both:45long/212short sizing attempts; long no recuts; short19B/18C notional-or-weight recuts and sized_below_trade_target; no margin/risk-budget/capacityzero/lotzero.
- PAXG both38long attempts, no recuts/zeros.
- SPY B20long/C19long attempts, no recuts/zeros.

These are attempts while flat without pending, not events while occupied, fills or counterfactual opportunities. Nocional/peso sublimits are not separable in existing counter. TerminalC reports pre-liquidation SPY open1; tail explicitly records forced MARKET liquidation and fee/PNL at boundary, like control. Root fill/MTM auditor handles reconciliation; do not delete it.

Tail log evidence retained below as exact JSON from Jesse MCP; last20 lines include complete final counters for each session. No need to page historical logs for absent supplement because complete-event counter itself is empty.

```json
{
  "B": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "77a80211-701a-4af4-9fb6-b77130b7b4c8",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-27T20:00:00] 📤 Order submitted | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 4.0718000000000005 | Price: 4534.93",
      "[INFO | 2025-12-28T00:01:00] Saved daily portfolio balance: 19392.2",
      "[INFO | 2025-12-29T00:01:00] Saved daily portfolio balance: 19295.7",
      "[INFO | 2025-12-29T00:21:00] ✅ Order executed | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 4.0718000000000005 | Price: 4534.93",
      "[INFO | 2025-12-29T00:21:00] Charged 8.31 as fee. Balance for USDT on Binance Perpetual Futures changed from 19401.28 to 19392.97",
      "[INFO | 2025-12-29T00:21:00] Added realized PNL of -158.78. Balance for USDT on Binance Perpetual Futures changed from 19392.97 to 19234.19",
      "[INFO | 2025-12-29T00:21:00] 🔴 Trade closed | PAXG-USDT | LONG | Binance Perpetual Futures",
      "Qty: 4.0718000000000005 | Entry: 4573.93 | Exit: 4534.93",
      "Net PnL: -175.47 USDT (-4.71%) | Fees: 16.69 USDT",
      "[INFO | 2025-12-29T00:21:00] 🏁 Position closed | PAXG-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 19234.19",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {}, \"recipe\": \"R101\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 212, \"margin_limited\": 0, \"notional_or_weight_limited\": 19, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 19, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR101\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 19234.19"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 816055,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8"
  },
  "C": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "9b5cbe51-91ee-4361-b080-c28c0cd38fdb",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 19443.92",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {}, \"recipe\": \"R101\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 212, \"margin_limited\": 0, \"notional_or_weight_limited\": 18, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 18, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR101\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -99.187(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] 📤 Order submitted | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 36.068 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ✅ Order executed | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 36.068 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] Charged 11.19 as fee. Balance for USDT on Binance Perpetual Futures changed from 19518.21 to 19507.01",
      "[INFO | 2025-12-31T00:00:00] Added realized PNL of -99.19. Balance for USDT on Binance Perpetual Futures changed from 19507.01 to 19407.83",
      "[INFO | 2025-12-31T00:00:00] 🔴 Trade closed | SPY-USDT | LONG | Binance Perpetual Futures",
      "Qty: 36.068 | Entry: 692.34 | Exit: 689.59",
      "Net PnL: -121.62 USDT (-2.44%) | Fees: 22.42 USDT",
      "[INFO | 2025-12-31T00:00:00] 🏁 Position closed | SPY-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-31T00:00:00] cancel all remaining orders of SPY-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-31T00:00:00] 🚫 Order canceled | SPY-USDT | Binance Perpetual Futures | SELL STOP | Qty: 36.068 | Price: 688.19",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 19407.83"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 839050,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb"
  }
}
```
