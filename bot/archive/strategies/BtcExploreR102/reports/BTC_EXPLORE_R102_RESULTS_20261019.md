# BTC exploration R102 X02 results — 2026-10-19

Both fulls finished without error. No parameter/source changes or retries. Root economic fills/MTM/stress audit remains separate.

- [B](http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae):177trades,96shorts,net6279.083616318992USDT,fees992.0681378845384,CAGR9.797167550579267%,DD−12.849105796809901%,Sharpe1.0133144051032732.
- [C](http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4):184trades,96shorts,net6418.732360311473USDT,fees1076.8329267206336,CAGR9.977200480009628%,DD−9.55488219794496%,Sharpe1.011265320542193.

Replaced short generator only. All96BTCshort are R102 and reconcile with final fills96/closes96 in BOTH.144admissible transition events;49observed occupied at before in each. Do not infer144−49=95fillable or49blocked: engine can close an existing position and enter fresh same-bar signal. Before state advances even occupied; vars not cleared by order reset, independently checked by root framework review. No queues or reattempts of persistent true states.

PORT_CAPACITY: BTC45long/96short sizing attempts, all budget/margin/notional/zero counters0; PAXG38long; SPY B20/C19long, all recut/zero counters0. No observed capacity suppression at sizing. Attempts are not potential fills while occupied. C has explicit forced SPY boundary closure in tail; pretermination open1 is not unexplained residual.

Full form readbacks exact,3snapshots each exact approved source. HP both DNAempty/donchian26/fast20/slow80/ADX26/stop2/trail4.2/BE2.25.10kshared/1%trade/8%aggregate/5xisolated/cap4.4/fee.00045side/.001reserveonly,warm240,4h+M1,debugtruefastfalsecharttrue.2020-10-15→2025-12-31exclusive.2026untouched.

Immediate result inferior to B/C controls in total net,CAGR and DD. This does not meet incremental economic purpose; no attempts to rescue windows,ratio or payoff. Final regularity and friction handled by root audit over same shared account.

Exact final tail evidence:
```json
{
  "B": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "56c48468-10dd-489e-b921-fa948dbd34ae",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-27T20:00:00] 📤 Order submitted | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.4462 | Price: 4534.93",
      "[INFO | 2025-12-28T00:01:00] Saved daily portfolio balance: 16412.81",
      "[INFO | 2025-12-29T00:01:00] Saved daily portfolio balance: 16331.14",
      "[INFO | 2025-12-29T00:21:00] ✅ Order executed | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.4462 | Price: 4534.93",
      "[INFO | 2025-12-29T00:21:00] Charged 7.03 as fee. Balance for USDT on Binance Perpetual Futures changed from 16420.5 to 16413.47",
      "[INFO | 2025-12-29T00:21:00] Added realized PNL of -134.38. Balance for USDT on Binance Perpetual Futures changed from 16413.47 to 16279.08",
      "[INFO | 2025-12-29T00:21:00] 🔴 Trade closed | PAXG-USDT | LONG | Binance Perpetual Futures",
      "Qty: 3.4462 | Entry: 4573.93 | Exit: 4534.93",
      "Net PnL: -148.51 USDT (-4.71%) | Fees: 14.12 USDT",
      "[INFO | 2025-12-29T00:21:00] 🏁 Position closed | PAXG-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 16279.08",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 96, \"events\": 144, \"events_occupied\": 49, \"fills\": 96}, \"recipe\": \"R102\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 96, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR102\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 16279.08"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 762905,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae"
  },
  "C": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "dd5b6e8d-6207-4e01-9bce-8a18c5d416e4",
    "session_status": "finished",
    "section": "logs",
    "available": true,
    "items": [
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 16449.38",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 96, \"events\": 144, \"events_occupied\": 49, \"fills\": 96}, \"recipe\": \"R102\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 96, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcExploreR102\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -84.2353(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] 📤 Order submitted | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 30.631 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ✅ Order executed | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 30.631 | Price: 689.59",
      "[INFO | 2025-12-31T00:00:00] Charged 9.51 as fee. Balance for USDT on Binance Perpetual Futures changed from 16512.47 to 16502.97",
      "[INFO | 2025-12-31T00:00:00] Added realized PNL of -84.24. Balance for USDT on Binance Perpetual Futures changed from 16502.97 to 16418.73",
      "[INFO | 2025-12-31T00:00:00] 🔴 Trade closed | SPY-USDT | LONG | Binance Perpetual Futures",
      "Qty: 30.631 | Entry: 692.34 | Exit: 689.59",
      "Net PnL: -103.28 USDT (-2.44%) | Fees: 19.04 USDT",
      "[INFO | 2025-12-31T00:00:00] 🏁 Position closed | SPY-USDT | Binance Perpetual Futures",
      "[INFO | 2025-12-31T00:00:00] cancel all remaining orders of SPY-USDT to prepare for a fresh start...",
      "[INFO | 2025-12-31T00:00:00] 🚫 Order canceled | SPY-USDT | Binance Perpetual Futures | SELL STOP | Qty: 30.631 | Price: 688.19",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 16418.73"
    ],
    "offset": 0,
    "limit": 20,
    "returned": 20,
    "total": null,
    "next_offset": 20,
    "has_more": true,
    "truncated_by_size": false,
    "order": "offset counts entries back from the newest; each page is oldest first",
    "log_size_bytes": 785872,
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4"
  }
}
```
