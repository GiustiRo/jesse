# Payoff P03 completed operational QA

BtcPayoffR103 exact frozen source and ticketP03, final pair. Both finished without errors. All six payoff fulls complete. No pending draft/run/analysis own jobs after PQA3 succeeded. No adaptive threshold or source edits after results.

NetB7599.7330/C7761.1836 below original controls; DD−6.7426/−6.7372 lower. No promotion; root full MTM/cost/concentration audit determines joint criteria. Current long management preserved, shared account may change sizes.

Final logs each:130shortopen=shortclose,53RSIneutral,112partialbars skipped,0timeout/invalid. Three capacityJSON per session,BTC216shortsizingattempts/20B19Cnotionalcuts/0riskmarginzerocuts. PQA3 independently validates53MARKET exits,4h/earliestfullpostfill timestamps and source unit stubs validateRSI>=50; no claim of recalculating every RSI value absent from snapshots.

Forms/config/3snapshots exactly verified before execution. Account10kshared,1%trade/8%aggregate,isolated5x/cap4.4,fee.00045eachside,reserve.001sizingonly,warm240/debugtrue/fastfalse/charttrue. BTC/PAXG/SPY4h+threeM1 data routes,2020-10-15→2025-12-31EXCLUSIVE,2026closed. No data/scripts/framework/globalconfig/restarts/live/Pi.

## B

[Dashboard](http://localhost:9200/#/backtest/6eea0aa5-84fa-45b1-9e44-86d1e2c29a18), finished 124.43s, no error.
```json
{
  "verification": {
    "routes": true,
    "M1": true,
    "options": true,
    "window": true,
    "config": true,
    "snapshots": true
  },
  "metrics": {
    "total": 211,
    "total_winning_trades": 98,
    "total_losing_trades": 113,
    "starting_balance": 10000,
    "finishing_balance": 17599.732996218077,
    "win_rate": 0.46445497630331756,
    "win_rate_longs": 0.5061728395061729,
    "win_rate_shorts": 0.43846153846153846,
    "ratio_avg_win_loss": 1.976148928735786,
    "longs_count": 81,
    "longs_percentage": 38.388625592417064,
    "shorts_percentage": 61.611374407582936,
    "shorts_count": 130,
    "fee": 1329.118906680693,
    "net_profit": 7599.7329962180975,
    "net_profit_percentage": 75.99732996218097,
    "average_win": 186.18548307496812,
    "average_loss": 94.21632163830775,
    "expectancy": 36.01769192520427,
    "expectancy_percentage": 0.3601769192520427,
    "expected_net_profit_every_100_trades": 36.01769192520427,
    "average_holding_period": 299267.77251184836,
    "average_winning_holding_period": 506911.8367346939,
    "average_losing_holding_period": 119187.0796460177,
    "gross_profit": 18246.177341346876,
    "gross_loss": -10646.444345128775,
    "max_drawdown": -6.742589851287828,
    "max_underwater_period": 333,
    "annual_return": 11.452203548296168,
    "annualization": 365,
    "sharpe_ratio": 1.1885557169428456,
    "calmar_ratio": 1.6984873469811914,
    "sortino_ratio": 2.033390356962189,
    "omega_ratio": 1.338066341500642,
    "serenity_index": null,
    "total_open_trades": 0,
    "open_pl": 0,
    "winning_streak": 5,
    "losing_streak": 6,
    "largest_losing_trade": -167.16839881721464,
    "largest_winning_trade": 1748.2989421460939,
    "current_streak": -2,
    "avg_trades_per_day": 0.11087752128309056,
    "avg_trades_per_week": 0.7761426489816339,
    "avg_trades_per_month": 3.3751117478572765
  }
}
```
Final logged records:
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"partial_bar_skipped": 112, "rsi_neutral": 53, "short_close": 130, "short_open": 130}, "strategy": "BtcPayoffR103"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 216, "margin_limited": 0, "notional_or_weight_limited": 20, "risk_budget_limited": 0, "sized_below_trade_target": 20, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR103", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 20, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpySecond4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```

## C

[Dashboard](http://localhost:9200/#/backtest/5652bfcb-64b2-4131-a757-3c5fcde4f886), finished 125.08s, no error.
```json
{
  "verification": {
    "routes": true,
    "M1": true,
    "options": true,
    "window": true,
    "config": true,
    "snapshots": true
  },
  "metrics": {
    "total": 218,
    "total_winning_trades": 100,
    "total_losing_trades": 118,
    "starting_balance": 10000,
    "finishing_balance": 17761.183616319846,
    "win_rate": 0.45871559633027525,
    "win_rate_longs": 0.48863636363636365,
    "win_rate_shorts": 0.43846153846153846,
    "ratio_avg_win_loss": 2.0013589722521496,
    "longs_count": 88,
    "longs_percentage": 40.36697247706422,
    "shorts_percentage": 59.63302752293578,
    "shorts_count": 130,
    "fee": 1417.7212343463568,
    "net_profit": 7761.183616319857,
    "net_profit_percentage": 77.61183616319856,
    "average_win": 189.11237340266948,
    "average_loss": 94.491980711416,
    "expectancy": 35.601759707889265,
    "expectancy_percentage": 0.35601759707889263,
    "expected_net_profit_every_100_trades": 35.601759707889265,
    "average_holding_period": 314415.4128440367,
    "average_winning_holding_period": 531692.4,
    "average_losing_holding_period": 130282.37288135593,
    "gross_profit": 18911.237340266947,
    "gross_loss": -11150.053723947089,
    "max_drawdown": -6.737234189427643,
    "max_underwater_period": 288,
    "annual_return": 11.647580052798357,
    "annualization": 365,
    "sharpe_ratio": 1.1817067693807373,
    "calmar_ratio": 1.7288370457830067,
    "sortino_ratio": 1.9885275018722546,
    "omega_ratio": 1.325110717436147,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": -90.7719999999972,
    "winning_streak": 5,
    "losing_streak": 6,
    "largest_losing_trade": -170.77963983292923,
    "largest_winning_trade": 1722.3501637839995,
    "current_streak": -3,
    "avg_trades_per_day": 0.1145559224630983,
    "avg_trades_per_week": 0.8018914572416881,
    "avg_trades_per_month": 3.4870822797767125
  }
}
```
Final logged records:
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"partial_bar_skipped": 112, "rsi_neutral": 53, "short_close": 130, "short_open": 130}, "strategy": "BtcPayoffR103"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 216, "margin_limited": 0, "notional_or_weight_limited": 19, "risk_budget_limited": 0, "sized_below_trade_target": 19, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR103", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 19, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpyMarket4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```
