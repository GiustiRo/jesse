# Payoff P02 completed operational QA

BtcPayoffR102 frozen source unchanged. Ticket P02 authorized both fulls, now finished without error. No P03 draft/run. Root audit handles MTM/cost/concentration and full economic decision; no duplicated analysis. Baseline entries and long runner preserved in source, realized trajectories may change.

Net B8658.4851/C8829.6182 and DD−7.8686/−8.7171 deteriorate versus their controls. Not promoted. Final debug logs each show22BE milestone latches=22BE replacements,110partialbars skipped,6timeouts,126shortfills=126shortcloses,zeroinvalidbar. These are exact logged counters, not full reconstruction of every milestone indicator. Expected capital/capacity diagnostics persisted for all3routes. C preterminal total_open_trades1 requires root boundary reconciliation; not interpreted as final exposure.

Contract: account10k shared,1%trade/8%aggregate,isolated5x/cap4.4,fee.00045allordereachside,reserve.001sizingonly,no pyramiding. Window2020-10-15→2025-12-31EXCLUSIVE;2026closed,normalengine/debugtrue/charttrue/warm240;BTC/PAXG/SPY4h in fixed order plus3M1routes. No data/globalconfig/framework/restart/live/Pi/scripts.

## B

[Dashboard](http://localhost:9200/#/backtest/85a2fe07-0f26-4271-88d0-4ebdcd8814f1), finished 136.55s, no error. Forms/config and three exact snapshots verified before start.
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
    "total": 207,
    "total_winning_trades": 110,
    "total_losing_trades": 97,
    "starting_balance": 10000,
    "finishing_balance": 18658.485109663725,
    "win_rate": 0.5314009661835749,
    "win_rate_longs": 0.5061728395061729,
    "win_rate_shorts": 0.5476190476190477,
    "ratio_avg_win_loss": 1.5522979298105462,
    "longs_count": 81,
    "longs_percentage": 39.130434782608695,
    "shorts_percentage": 60.869565217391305,
    "shorts_count": 126,
    "fee": 1334.3280665250018,
    "net_profit": 8658.485109663754,
    "net_profit_percentage": 86.58485109663754,
    "average_win": 182.23787521034387,
    "average_loss": 117.39877488117601,
    "expectancy": 41.828430481467414,
    "expectancy_percentage": 0.4182843048146741,
    "expected_net_profit_every_100_trades": 41.82843048146741,
    "average_holding_period": 319563.1884057971,
    "average_winning_holding_period": 467951.45454545453,
    "average_losing_holding_period": 151287.8350515464,
    "gross_profit": 20046.166273137827,
    "gross_loss": -11387.681163474073,
    "max_drawdown": -7.868585143766871,
    "max_underwater_period": 291,
    "annual_return": 12.708000312003609,
    "annualization": 365,
    "sharpe_ratio": 1.2683015465144638,
    "calmar_ratio": 1.6150299043367788,
    "sortino_ratio": 2.1698670100944657,
    "omega_ratio": 1.3540713818886179,
    "serenity_index": null,
    "total_open_trades": 0,
    "open_pl": 0,
    "winning_streak": 7,
    "losing_streak": 6,
    "largest_losing_trade": -177.14867595996336,
    "largest_winning_trade": 1774.2477205081877,
    "current_streak": -2,
    "avg_trades_per_day": 0.10877557775165757,
    "avg_trades_per_week": 0.761429044261603,
    "avg_trades_per_month": 3.3111285867604563
  }
}
```
Final logged records:
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"be_latch": 22, "be_stop": 22, "partial_bar_skipped": 110, "short_close": 126, "short_open": 126, "timeout": 6}, "strategy": "BtcPayoffR102"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 213, "margin_limited": 0, "notional_or_weight_limited": 19, "risk_budget_limited": 0, "sized_below_trade_target": 19, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR102", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 20, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpySecond4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```

## C

[Dashboard](http://localhost:9200/#/backtest/b91112c0-e3f3-4c31-8dea-abf184cf2d40), finished 136.67s, no error. Forms/config and three exact snapshots verified before start.
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
    "total": 214,
    "total_winning_trades": 112,
    "total_losing_trades": 102,
    "starting_balance": 10000,
    "finishing_balance": 18829.618167865407,
    "win_rate": 0.5233644859813084,
    "win_rate_longs": 0.48863636363636365,
    "win_rate_shorts": 0.5476190476190477,
    "ratio_avg_win_loss": 1.5866279561691692,
    "longs_count": 88,
    "longs_percentage": 41.1214953271028,
    "shorts_percentage": 58.8785046728972,
    "shorts_count": 126,
    "fee": 1424.2506500071324,
    "net_profit": 8829.61816786541,
    "net_profit_percentage": 88.29618167865411,
    "average_win": 185.05796090484984,
    "average_loss": 116.63601424978208,
    "expectancy": 41.25989798067946,
    "expectancy_percentage": 0.4125989798067946,
    "expected_net_profit_every_100_trades": 41.25989798067946,
    "average_holding_period": 334330.09345794393,
    "average_winning_holding_period": 490772.6785714286,
    "average_losing_holding_period": 162550,
    "gross_profit": 20726.491621343182,
    "gross_loss": -11896.873453477772,
    "max_drawdown": -8.717095860718715,
    "max_underwater_period": 359,
    "annual_return": 12.90554374342172,
    "annualization": 365,
    "sharpe_ratio": 1.261578306917611,
    "calmar_ratio": 1.4804866149949247,
    "sortino_ratio": 2.125174435262881,
    "omega_ratio": 1.341158681347799,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": -96.2307499999988,
    "winning_streak": 7,
    "losing_streak": 6,
    "largest_losing_trade": -181.32159290903724,
    "largest_winning_trade": 1745.055344850832,
    "current_streak": -3,
    "avg_trades_per_day": 0.11245397893166531,
    "avg_trades_per_week": 0.7871778525216572,
    "avg_trades_per_month": 3.4230991186798922
  }
}
```
Final logged records:
```
[INFO | 2025-12-31T00:00:00] ==> BTC_PAYOFF_SUMMARY {"counts": {"be_latch": 22, "be_stop": 22, "partial_bar_skipped": 110, "short_close": 126, "short_open": 126, "timeout": 6}, "strategy": "BtcPayoffR102"}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 45, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}, "short": {"capacity_zero": 0, "eligible_sizing_attempts": 213, "margin_limited": 0, "notional_or_weight_limited": 18, "risk_budget_limited": 0, "sized_below_trade_target": 18, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "BtcPayoffR102", "symbol": "BTC-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 38, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortComparePaxgMarket4h", "symbol": "PAXG-USDT", "trade_risk": 0.01}
[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {"counts": {"long": {"capacity_zero": 0, "eligible_sizing_attempts": 19, "margin_limited": 0, "notional_or_weight_limited": 0, "risk_budget_limited": 0, "sized_below_trade_target": 0, "zero_after_lot_rounding": 0}}, "notional_cap": 4.4, "portfolio_risk": 0.08, "strategy": "PortCompareSpyMarket4h", "symbol": "SPY-USDT", "trade_risk": 0.01}
```
