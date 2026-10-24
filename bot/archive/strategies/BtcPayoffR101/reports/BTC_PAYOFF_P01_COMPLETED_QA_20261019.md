# BTC Payoff P01 completed sessions — operational QA

Frozen BtcPayoffR101 in shared B/C. Both finished without errors; no adaptive source edits after starting. Only inherited terminate comment corrected before draft creation to state debug=true runner persistence; all three sources readback frozen before P01. Baseline controls reused, never rerun. P02 has no ticket/draft/run.

Sources passed actual compile/AST and causal method stubs101/101 (job1a560d1ce7e840f39c8fa5aa73fdef1b succeeded). Detailed reproducible report BTC_PAYOFF_R1_AST_STUB_QA_20261019.md in this folder. Root source review approved actual3sources before P01. Long branch and18methods identical to original.

B/C net9186.89/9342.08 versus controls9234.19/9407.83; DD−6.9796/−7.0143 versus−7.50/−8.17. Net slightly lower, DD lower. No improvement or acceptance declared before root full MTM/cost/concentration audit. C engine total_open_trades1 is preterminal metadata; final boundary reconciliation delegated to root rather than interpreting it as an unclosed terminal trade.

Each source snapshot was read from draft and exactly matched actual BTC/PAXG/SPY source before run. Route order BTC/PAXG/SPY4h, three M1 auxiliary routes; shared10k,.00045fee,isolated5x,warm240,debugtrue/fastfalse/charttrue,2020-10-15→2025-12-31exclusive confirmed. No2026, funding/data/scripts/framework/global config/restarts/live/Pi.

Final log counters match both sides:379EMAstopchanges,111partialentrybars skipped,127shortopens=127shortcloses,1timeout, no invalid_closed_bar events. These counters establish what strategy recorded, not independent reconstruction of every indicator value. B/C capacity logs include BTC/PAXG/SPY; BTC213eligible sizingattempts,19B/18C notional-weightcuts, zero risk/margin/zero-capacity cuts. Other routes unchanged. Full per-event chronology not asserted from final-page summaries; requested distinct snapshot order QA slot from root, pending.

## P01 B

[Dashboard](http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528); status finished, duration156.05s, errornull.

Form readback checks:
```json
{
  "form": true,
  "debug": true,
  "fast": true,
  "chart": true,
  "window": true,
  "warm": true,
  "account": true,
  "snapshots": true
}
```

Stored engine metrics (not MTM calendar acceptance):
```json
{
  "total": 208,
  "total_winning_trades": 105,
  "total_losing_trades": 103,
  "starting_balance": 10000,
  "finishing_balance": 19186.892322591506,
  "win_rate": 0.5048076923076923,
  "win_rate_longs": 0.5061728395061729,
  "win_rate_shorts": 0.5039370078740157,
  "ratio_avg_win_loss": 1.7907949565093269,
  "longs_count": 81,
  "longs_percentage": 38.94230769230769,
  "shorts_percentage": 61.05769230769231,
  "shorts_count": 127,
  "fee": 1379.7261171150242,
  "net_profit": 9186.892322591513,
  "net_profit_percentage": 91.86892322591514,
  "average_win": 193.47487940247262,
  "average_loss": 108.03854383172927,
  "expectancy": 44.16775155092073,
  "expectancy_percentage": 0.44167751550920725,
  "expected_net_profit_every_100_trades": 44.16775155092073,
  "average_holding_period": 311896.73076923075,
  "average_winning_holding_period": 485305.71428571426,
  "average_losing_holding_period": 135120.58252427186,
  "gross_profit": 20314.862337259627,
  "gross_loss": -11127.970014668115,
  "max_drawdown": -6.979598747156956,
  "max_underwater_period": 292,
  "annual_return": 13.313322467772526,
  "annualization": 365,
  "sharpe_ratio": 1.3470778681063797,
  "calmar_ratio": 1.9074624416189434,
  "sortino_ratio": 2.320871673611376,
  "omega_ratio": 1.3843338561778,
  "serenity_index": null,
  "total_open_trades": 0,
  "open_pl": 0,
  "winning_streak": 7,
  "losing_streak": 7,
  "largest_losing_trade": -182.16543707358787,
  "largest_winning_trade": 1839.1196664134234,
  "current_streak": -2,
  "avg_trades_per_day": 0.1093010636345158,
  "avg_trades_per_week": 0.7651074454416107,
  "avg_trades_per_month": 3.3271243770346612
}
```

Bounded final logs page, exact records (not stitched logs or full per-event audit):
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"ema_stop": 379, "partial_bar_skipped": 111, "short_close": 127, "short_open": 127, "timeout": 1}, "strategy": "BtcPayoffR101"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 213, "margin_limited": 0, "notional_or_weight_limited": 19, "risk_budget_limited": 0, "sized_below_trade_target": 19, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR101", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 20, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpySecond4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```

## P01 C

[Dashboard](http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee); status finished, duration144.45s, errornull.

Form readback checks:
```json
{
  "form": true,
  "debug": true,
  "fast": true,
  "chart": true,
  "window": true,
  "warm": true,
  "account": true,
  "snapshots": true
}
```

Stored engine metrics (not MTM calendar acceptance):
```json
{
  "total": 215,
  "total_winning_trades": 107,
  "total_losing_trades": 108,
  "starting_balance": 10000,
  "finishing_balance": 19342.080514331345,
  "win_rate": 0.49767441860465117,
  "win_rate_longs": 0.48863636363636365,
  "win_rate_shorts": 0.5039370078740157,
  "ratio_avg_win_loss": 1.8177941932641435,
  "longs_count": 88,
  "longs_percentage": 40.93023255813954,
  "shorts_percentage": 59.06976744186046,
  "shorts_count": 127,
  "fee": 1473.086073342319,
  "net_profit": 9342.080514331377,
  "net_profit_percentage": 93.42080514331379,
  "average_win": 196.3144351420287,
  "average_loss": 107.99596338764533,
  "expectancy": 43.451537275959886,
  "expectancy_percentage": 0.4345153727595989,
  "expected_net_profit_every_100_trades": 43.451537275959886,
  "average_holding_period": 326844.5581395349,
  "average_winning_holding_period": 508868.97196261684,
  "average_losing_holding_period": 146505.55555555556,
  "gross_profit": 21005.644560197074,
  "gross_loss": -11663.564045865696,
  "max_drawdown": -7.014321226210174,
  "max_underwater_period": 223,
  "annual_return": 13.488538642223546,
  "annualization": 365,
  "sharpe_ratio": 1.3357741258053553,
  "calmar_ratio": 1.922999846631116,
  "sortino_ratio": 2.2625016007712304,
  "omega_ratio": 1.3685463874506036,
  "serenity_index": null,
  "total_open_trades": 1,
  "open_pl": -98.85150000000067,
  "winning_streak": 7,
  "losing_streak": 7,
  "largest_losing_trade": -184.8685822213889,
  "largest_winning_trade": 1809.9272907560674,
  "current_streak": -3,
  "avg_trades_per_day": 0.11297946481452356,
  "avg_trades_per_week": 0.7908562537016649,
  "avg_trades_per_month": 3.439094908954097
}
```

Bounded final logs page, exact records (not stitched logs or full per-event audit):
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"ema_stop": 379, "partial_bar_skipped": 111, "short_close": 127, "short_open": 127, "timeout": 1}, "strategy": "BtcPayoffR101"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 213, "margin_limited": 0, "notional_or_weight_limited": 18, "risk_budget_limited": 0, "sized_below_trade_target": 18, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR101", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 19, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpyMarket4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```

