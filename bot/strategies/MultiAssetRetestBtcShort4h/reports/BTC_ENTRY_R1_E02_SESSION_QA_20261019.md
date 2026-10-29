# BTC entry E02 session registry and QA — 2026-10-19

Ticket E02 only; BtcEntryR102 B/C finished. No E03 draft/run. No analysis job used; root owns economic MTM/fills audit. Frozen recipes unchanged after E01 negative result.

## B

[B](http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6)

ID 97d654d0-5917-4a26-b151-11ef396591e6; finished, error null. Pre/post snapshot equality3/3 PASS, all source defaults and risk/reservation helpers unchanged. Form settings verified before start and preserved at finish. Debugtrue records all three capacity summaries.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR102"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "PAXG-USDT",
        "timeframe": "4h",
        "strategy": "PortComparePaxgMarket4h"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "SPY-USDT",
        "timeframe": "4h",
        "strategy": "PortCompareSpySecond4h"
      }
    ],
    "data_routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "1m"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "PAXG-USDT",
        "timeframe": "1m"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "SPY-USDT",
        "timeframe": "1m"
      }
    ],
    "start_date": "2020-10-15",
    "finish_date": "2025-12-31",
    "debug_mode": true,
    "export_csv": false,
    "export_json": false,
    "export_chart": true,
    "fast_mode": false,
    "benchmark": false,
    "config": {
      "logging": {
        "order_submission": true,
        "order_cancellation": true,
        "order_execution": true,
        "position_opened": true,
        "position_increased": true,
        "position_reduced": true,
        "position_closed": true,
        "shorter_period_candles": false,
        "trading_candles": true,
        "balance_update": true
      },
      "warm_up_candles": 240,
      "exchange": {
        "name": "Binance Perpetual Futures",
        "type": "futures",
        "balance": 10000,
        "fee": 0.00045,
        "futures_leverage_mode": "isolated",
        "futures_leverage": 5
      }
    }
  },
  "metrics": {
    "total": 143,
    "total_winning_trades": 71,
    "total_losing_trades": 72,
    "starting_balance": 10000,
    "finishing_balance": 17157.30730885056,
    "win_rate": 0.4965034965034965,
    "win_rate_longs": 0.5061728395061729,
    "win_rate_shorts": 0.4838709677419355,
    "ratio_avg_win_loss": 1.9142536070094014,
    "longs_count": 81,
    "longs_percentage": 56.64335664335665,
    "shorts_percentage": 43.35664335664335,
    "shorts_count": 62,
    "fee": 936.4719605387695,
    "net_profit": 7157.307308850563,
    "net_profit_percentage": 71.57307308850562,
    "average_win": 214.37132346471523,
    "average_loss": 111.986898015892,
    "expectancy": 50.051100061892015,
    "expectancy_percentage": 0.5005110006189201,
    "expected_net_profit_every_100_trades": 50.05110006189201,
    "average_holding_period": 432530.76923076925,
    "average_winning_holding_period": 691476.338028169,
    "average_losing_holding_period": 177181.66666666666,
    "gross_profit": 15220.363965994782,
    "gross_loss": -8063.056657144223,
    "max_drawdown": -9.465609183787848,
    "max_underwater_period": 484,
    "annual_return": 10.909286108252282,
    "annualization": 365,
    "sharpe_ratio": 1.1648884268061535,
    "calmar_ratio": 1.152518120749912,
    "sortino_ratio": 2.0049379326066625,
    "omega_ratio": 1.3447262166416698,
    "serenity_index": null,
    "total_open_trades": 0,
    "open_pl": 0,
    "winning_streak": 6,
    "losing_streak": 6,
    "largest_losing_trade": -162.8965137053483,
    "largest_winning_trade": 1748.2989421460939,
    "current_streak": -2,
    "avg_trades_per_day": 0.07514448124872962,
    "avg_trades_per_week": 0.5260113687411073,
    "avg_trades_per_month": 2.2873980092113295
  },
  "hyperparameters": [
    [
      "DNA",
      ""
    ],
    [
      "donchian_len",
      26
    ],
    [
      "ema_fast",
      20
    ],
    [
      "ema_slow",
      80
    ],
    [
      "adx_min",
      26
    ],
    [
      "stop_atr",
      2
    ],
    [
      "trail_atr",
      4.2
    ],
    [
      "be_r",
      2.25
    ]
  ],
  "capacity": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 115,
          "margin_limited": 0,
          "notional_or_weight_limited": 9,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 9,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR102",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 38,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgMarket4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 20,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpySecond4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ],
  "terminal_log_tail": [
    "[INFO | 2025-12-27T20:00:00] 📈 Position opened | PAXG-USDT | LONG | Binance Perpetual Futures | Qty: 3.6322 | Entry: 4573.93",
    "[INFO | 2025-12-27T20:00:00] 📤 Order submitted | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.6322 | Price: 4534.93",
    "[INFO | 2025-12-28T00:01:00] Saved daily portfolio balance: 17298.26",
    "[INFO | 2025-12-29T00:01:00] Saved daily portfolio balance: 17212.17",
    "[INFO | 2025-12-29T00:21:00] ✅ Order executed | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.6322 | Price: 4534.93",
    "[INFO | 2025-12-29T00:21:00] Charged 7.41 as fee. Balance for USDT on Binance Perpetual Futures changed from 17306.36 to 17298.94",
    "[INFO | 2025-12-29T00:21:00] Added realized PNL of -141.64. Balance for USDT on Binance Perpetual Futures changed from 17298.94 to 17157.31",
    "[INFO | 2025-12-29T00:21:00] 🔴 Trade closed | PAXG-USDT | LONG | Binance Perpetual Futures",
    "Qty: 3.6322 | Entry: 4573.93 | Exit: 4534.93",
    "Net PnL: -156.52 USDT (-4.71%) | Fees: 14.88 USDT",
    "[INFO | 2025-12-29T00:21:00] 🏁 Position closed | PAXG-USDT | Binance Perpetual Futures",
    "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
    "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 17157.31",
    "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 115, \"margin_limited\": 0, \"notional_or_weight_limited\": 9, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 9, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcEntryR102\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 17157.31"
  ]
}
```

## C

[C](http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3)

ID a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3; finished, error null. Pre/post snapshot equality3/3 PASS, all source defaults and risk/reservation helpers unchanged. Form settings verified before start and preserved at finish. Debugtrue records all three capacity summaries.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR102"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "PAXG-USDT",
        "timeframe": "4h",
        "strategy": "PortComparePaxgMarket4h"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "SPY-USDT",
        "timeframe": "4h",
        "strategy": "PortCompareSpyMarket4h"
      }
    ],
    "data_routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "1m"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "PAXG-USDT",
        "timeframe": "1m"
      },
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "SPY-USDT",
        "timeframe": "1m"
      }
    ],
    "start_date": "2020-10-15",
    "finish_date": "2025-12-31",
    "debug_mode": true,
    "export_csv": false,
    "export_json": false,
    "export_chart": true,
    "fast_mode": false,
    "benchmark": false,
    "config": {
      "logging": {
        "order_submission": true,
        "order_cancellation": true,
        "order_execution": true,
        "position_opened": true,
        "position_increased": true,
        "position_reduced": true,
        "position_closed": true,
        "shorter_period_candles": false,
        "trading_candles": true,
        "balance_update": true
      },
      "warm_up_candles": 240,
      "exchange": {
        "name": "Binance Perpetual Futures",
        "type": "futures",
        "balance": 10000,
        "fee": 0.00045,
        "futures_leverage_mode": "isolated",
        "futures_leverage": 5
      }
    }
  },
  "metrics": {
    "total": 150,
    "total_winning_trades": 73,
    "total_losing_trades": 77,
    "starting_balance": 10000,
    "finishing_balance": 17323.182129765533,
    "win_rate": 0.4866666666666667,
    "win_rate_longs": 0.48863636363636365,
    "win_rate_shorts": 0.4838709677419355,
    "ratio_avg_win_loss": 1.9605689850025383,
    "longs_count": 88,
    "longs_percentage": 58.666666666666664,
    "shorts_percentage": 41.333333333333336,
    "shorts_count": 62,
    "fee": 1021.7414063538888,
    "net_profit": 7323.1821297655315,
    "net_profit_percentage": 73.23182129765532,
    "average_win": 217.13959844688378,
    "average_loss": 110.75335788125949,
    "expectancy": 48.82121419843691,
    "expectancy_percentage": 0.4882121419843692,
    "expected_net_profit_every_100_trades": 48.82121419843692,
    "average_holding_period": 448326.4,
    "average_winning_holding_period": 720365.7534246575,
    "average_losing_holding_period": 190418.96103896105,
    "gross_profit": 15851.190686622516,
    "gross_loss": -8528.008556856981,
    "max_drawdown": -9.15032338845,
    "max_underwater_period": 442,
    "annual_return": 11.114148937352608,
    "annualization": 365,
    "sharpe_ratio": 1.1592343806170988,
    "calmar_ratio": 1.2146181577999144,
    "sortino_ratio": 1.9610454309151848,
    "omega_ratio": 1.329919018094562,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": -88.53350000000137,
    "winning_streak": 6,
    "losing_streak": 6,
    "largest_losing_trade": -165.50180896549193,
    "largest_winning_trade": 1719.1065664887376,
    "current_streak": -3,
    "avg_trades_per_day": 0.07882288242873736,
    "avg_trades_per_week": 0.5517601770011615,
    "avg_trades_per_month": 2.3993685411307655
  },
  "hyperparameters": [
    [
      "DNA",
      ""
    ],
    [
      "donchian_len",
      26
    ],
    [
      "ema_fast",
      20
    ],
    [
      "ema_slow",
      80
    ],
    [
      "adx_min",
      26
    ],
    [
      "stop_atr",
      2
    ],
    [
      "trail_atr",
      4.2
    ],
    [
      "be_r",
      2.25
    ]
  ],
  "capacity": [
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 45,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        },
        "short": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 115,
          "margin_limited": 0,
          "notional_or_weight_limited": 9,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 9,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR102",
      "symbol": "BTC-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 38,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortComparePaxgMarket4h",
      "symbol": "PAXG-USDT",
      "trade_risk": 0.01
    },
    {
      "counts": {
        "long": {
          "capacity_zero": 0,
          "eligible_sizing_attempts": 19,
          "margin_limited": 0,
          "notional_or_weight_limited": 0,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 0,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "PortCompareSpyMarket4h",
      "symbol": "SPY-USDT",
      "trade_risk": 0.01
    }
  ],
  "terminal_log_tail": [
    "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
    "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 17355.4",
    "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 115, \"margin_limited\": 0, \"notional_or_weight_limited\": 9, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 9, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcEntryR102\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
    "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -88.5335(-1.99%) because we reached the end of the backtest session.",
    "[INFO | 2025-12-31T00:00:00] 📤 Order submitted | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 32.194 | Price: 689.59",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] ✅ Order executed | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 32.194 | Price: 689.59",
    "[INFO | 2025-12-31T00:00:00] Charged 9.99 as fee. Balance for USDT on Binance Perpetual Futures changed from 17421.71 to 17411.72",
    "[INFO | 2025-12-31T00:00:00] Added realized PNL of -88.53. Balance for USDT on Binance Perpetual Futures changed from 17411.72 to 17323.18",
    "[INFO | 2025-12-31T00:00:00] 🔴 Trade closed | SPY-USDT | LONG | Binance Perpetual Futures",
    "Qty: 32.194 | Entry: 692.34 | Exit: 689.59",
    "Net PnL: -108.55 USDT (-2.44%) | Fees: 20.02 USDT",
    "[INFO | 2025-12-31T00:00:00] 🏁 Position closed | SPY-USDT | Binance Perpetual Futures",
    "[INFO | 2025-12-31T00:00:00] cancel all remaining orders of SPY-USDT to prepare for a fresh start...",
    "[INFO | 2025-12-31T00:00:00] 🚫 Order canceled | SPY-USDT | Binance Perpetual Futures | SELL STOP | Qty: 32.194 | Price: 688.19",
    "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 17323.18"
  ]
}
```

C summary open1/openPL−88.5335 is pretermination: logs record SPY boundary SELL MARKET execution, fee/PNL and final wallet17323.18. Root reconciliation required; no native liquidity conclusion. B has open0. Capacity after gate: BTC long45/short115 attempts in both,9 shortnotional/weight cuts each; no margin/risk/zerocapacity/lotzero cuts on any route. PAXG38, SPYB20/C19 attempts. Does not measure signals while occupied or future fills. Stored hp has common session defaults; not independent per-route runtime telemetry. No parameter changed or second version created.
