# BTC entry E03 session registry and QA — 2026-10-19

Ticket E03; final authorized pair BtcEntryR103 B/C finished. No further runs/drafts/analysis jobs. Root owns economic MTM/fills audit. Sources remain frozen and unchanged through this report.

## B

[B](http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c)

ID 20ca6dae-a6c9-44ed-8349-5877e2d3827c; finished, error null. Snapshot3/3 pre/post byte-exact against sources. Same verified config/routes/defaults and risk/ledger, no alpha change. Debugtrue captures capacity.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR103"
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
    "total": 125,
    "total_winning_trades": 62,
    "total_losing_trades": 63,
    "starting_balance": 10000,
    "finishing_balance": 17628.672481200472,
    "win_rate": 0.496,
    "win_rate_longs": 0.5061728395061729,
    "win_rate_shorts": 0.4772727272727273,
    "ratio_avg_win_loss": 2.0125379340153313,
    "longs_count": 81,
    "longs_percentage": 64.8,
    "shorts_percentage": 35.2,
    "shorts_count": 44,
    "fee": 955.8362426050691,
    "net_profit": 7628.672481200477,
    "net_profit_percentage": 76.28672481200476,
    "average_win": 248.52138008800642,
    "average_loss": 123.48655689295109,
    "expectancy": 61.029379849603835,
    "expectancy_percentage": 0.6102937984960384,
    "expected_net_profit_every_100_trades": 61.029379849603835,
    "average_holding_period": 479454.72,
    "average_winning_holding_period": 788804.5161290322,
    "average_losing_holding_period": 175015.2380952381,
    "gross_profit": 15408.325565456398,
    "gross_loss": -7779.653084255919,
    "max_drawdown": -6.196738173157634,
    "max_underwater_period": 333,
    "annual_return": 11.487330387340267,
    "annualization": 365,
    "sharpe_ratio": 1.2230338422095441,
    "calmar_ratio": 1.8537704944675333,
    "sortino_ratio": 2.1079683333343713,
    "omega_ratio": 1.3740271738951308,
    "serenity_index": null,
    "total_open_trades": 0,
    "open_pl": 0,
    "winning_streak": 6,
    "losing_streak": 5,
    "largest_losing_trade": -171.10177290703146,
    "largest_winning_trade": 1865.0684447755175,
    "current_streak": -2,
    "avg_trades_per_day": 0.06568573535728113,
    "avg_trades_per_week": 0.4598001475009679,
    "avg_trades_per_month": 1.9994737842756376
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
          "eligible_sizing_attempts": 74,
          "margin_limited": 0,
          "notional_or_weight_limited": 10,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 10,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR103",
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
    "[INFO | 2025-12-27T20:00:00] 📈 Position opened | PAXG-USDT | LONG | Binance Perpetual Futures | Qty: 3.7319 | Entry: 4573.93",
    "[INFO | 2025-12-27T20:00:00] 📤 Order submitted | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.7319 | Price: 4534.93",
    "[INFO | 2025-12-28T00:01:00] Saved daily portfolio balance: 17773.49",
    "[INFO | 2025-12-29T00:01:00] Saved daily portfolio balance: 17685.04",
    "[INFO | 2025-12-29T00:21:00] ✅ Order executed | PAXG-USDT | Binance Perpetual Futures | SELL STOP | Qty: 3.7319 | Price: 4534.93",
    "[INFO | 2025-12-29T00:21:00] Charged 7.62 as fee. Balance for USDT on Binance Perpetual Futures changed from 17781.81 to 17774.2",
    "[INFO | 2025-12-29T00:21:00] Added realized PNL of -145.52. Balance for USDT on Binance Perpetual Futures changed from 17774.2 to 17628.67",
    "[INFO | 2025-12-29T00:21:00] 🔴 Trade closed | PAXG-USDT | LONG | Binance Perpetual Futures",
    "Qty: 3.7319 | Entry: 4573.93 | Exit: 4534.93",
    "Net PnL: -160.82 USDT (-4.71%) | Fees: 15.29 USDT",
    "[INFO | 2025-12-29T00:21:00] 🏁 Position closed | PAXG-USDT | Binance Perpetual Futures",
    "[INFO | 2025-12-29T00:21:00] cancel all remaining orders of PAXG-USDT to prepare for a fresh start...",
    "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 17628.67",
    "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 74, \"margin_limited\": 0, \"notional_or_weight_limited\": 10, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 10, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcEntryR103\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 17628.67"
  ]
}
```

## C

[C](http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823)

ID f551da25-c6c9-4a31-8ad9-7fc4f71ad823; finished, error null. Snapshot3/3 pre/post byte-exact against sources. Same verified config/routes/defaults and risk/ledger, no alpha change. Debugtrue captures capacity.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR103"
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
    "total": 132,
    "total_winning_trades": 64,
    "total_losing_trades": 68,
    "starting_balance": 10000,
    "finishing_balance": 17790.99504230247,
    "win_rate": 0.48484848484848486,
    "win_rate_longs": 0.48863636363636365,
    "win_rate_shorts": 0.4772727272727273,
    "ratio_avg_win_loss": 2.0596323183751237,
    "longs_count": 88,
    "longs_percentage": 66.66666666666666,
    "shorts_percentage": 33.33333333333334,
    "shorts_count": 44,
    "fee": 1046.067977376006,
    "net_profit": 7790.995042302462,
    "net_profit_percentage": 77.90995042302463,
    "average_win": 251.44896904792213,
    "average_loss": 122.0843967171258,
    "expectancy": 59.0226897144126,
    "expectancy_percentage": 0.590226897144126,
    "expected_net_profit_every_100_trades": 59.0226897144126,
    "average_holding_period": 494915.9090909091,
    "average_winning_holding_period": 818715,
    "average_losing_holding_period": 190163.82352941178,
    "gross_profit": 16092.734019067017,
    "gross_loss": -8301.738976764555,
    "max_drawdown": -6.9241450826447615,
    "max_underwater_period": 320,
    "annual_return": 11.683498691478956,
    "annualization": 365,
    "sharpe_ratio": 1.2159545276779535,
    "calmar_ratio": 1.6873561359601525,
    "sortino_ratio": 2.061086714418538,
    "omega_ratio": 1.3571984039913254,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": -90.92324999999983,
    "winning_streak": 6,
    "losing_streak": 5,
    "largest_losing_trade": -173.06845995193854,
    "largest_winning_trade": 1835.8760691181615,
    "current_streak": -3,
    "avg_trades_per_day": 0.06936413653728889,
    "avg_trades_per_week": 0.4855489557610222,
    "avg_trades_per_month": 2.111444316195074
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
          "eligible_sizing_attempts": 74,
          "margin_limited": 0,
          "notional_or_weight_limited": 10,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 10,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR103",
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
    "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 17824.08",
    "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 74, \"margin_limited\": 0, \"notional_or_weight_limited\": 10, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 10, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"BtcEntryR103\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
    "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -90.9232(-1.99%) because we reached the end of the backtest session.",
    "[INFO | 2025-12-31T00:00:00] 📤 Order submitted | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 33.063 | Price: 689.59",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] ✅ Order executed | SPY-USDT | Binance Perpetual Futures | SELL MARKET | Qty: 33.063 | Price: 689.59",
    "[INFO | 2025-12-31T00:00:00] Charged 10.26 as fee. Balance for USDT on Binance Perpetual Futures changed from 17892.18 to 17881.92",
    "[INFO | 2025-12-31T00:00:00] Added realized PNL of -90.92. Balance for USDT on Binance Perpetual Futures changed from 17881.92 to 17791.0",
    "[INFO | 2025-12-31T00:00:00] 🔴 Trade closed | SPY-USDT | LONG | Binance Perpetual Futures",
    "Qty: 33.063 | Entry: 692.34 | Exit: 689.59",
    "Net PnL: -111.48 USDT (-2.44%) | Fees: 20.56 USDT",
    "[INFO | 2025-12-31T00:00:00] 🏁 Position closed | SPY-USDT | Binance Perpetual Futures",
    "[INFO | 2025-12-31T00:00:00] cancel all remaining orders of SPY-USDT to prepare for a fresh start...",
    "[INFO | 2025-12-31T00:00:00] 🚫 Order canceled | SPY-USDT | Binance Perpetual Futures | SELL STOP | Qty: 33.063 | Price: 688.19",
    "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 17791.0"
  ]
}
```

C summary open1/openPL−90.92325 is pretermination; logs capture SPY boundary MARKET execution,fee/realizedPNL and finalwallet17790.995. Root reconciliation required. Bopen0. No native liquidity inference. BTC attempts long45/short74 both,10notional/weightcuts each; no risk/margin/capacityzero/lotzero. PAXG38andSPYB20/C19attempts, zero cuts. Attempts do not capture occupied signals or guaranteed fills. Hp common session defaults reported, source defaults match all3routes; perroutehptelemetry not claimed. No recipe rescued after E01/E02 results.
