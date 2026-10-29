# BTC entry E01 session registry and QA — 2026-10-19

Ticket E01 only; BtcEntryR101 B/C finished. No E02 drafts/runs. No analysis jobs used. Root owns MTM/fills/cost/concentration/per-route economic audit; these are engine summaries and implementation/session checks, not acceptance.

## B

[B](http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6)

ID: 9de1ae4d-ef15-4d8f-9022-20ee1a830ec6. Status finished; error null. Snapshot3/3 byte-exact against sources both before and after run. Dates exclusive2025-12-31 and all routes/settings unchanged from verified draft. Stored form and summaries below.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR101"
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
    "total": 202,
    "total_winning_trades": 107,
    "total_losing_trades": 95,
    "starting_balance": 10000,
    "finishing_balance": 18869.026214379483,
    "win_rate": 0.5297029702970297,
    "win_rate_longs": 0.5061728395061729,
    "win_rate_shorts": 0.5454545454545454,
    "ratio_avg_win_loss": 1.5793329793632145,
    "longs_count": 81,
    "longs_percentage": 40.099009900990104,
    "shorts_percentage": 59.900990099009896,
    "shorts_count": 121,
    "fee": 1311.9407237537362,
    "net_profit": 8869.02621437949,
    "net_profit_percentage": 88.6902621437949,
    "average_win": 189.3148423470539,
    "average_loss": 119.8701254395292,
    "expectancy": 43.90607036821532,
    "expectancy_percentage": 0.43906070368215316,
    "expected_net_profit_every_100_trades": 43.90607036821532,
    "average_holding_period": 328226.1386138614,
    "average_winning_holding_period": 480481.68224299065,
    "average_losing_holding_period": 156738.31578947368,
    "gross_profit": 20256.688131134768,
    "gross_loss": -11387.661916755274,
    "max_drawdown": -7.512178630122179,
    "max_underwater_period": 291,
    "annual_return": 12.950827844275281,
    "annualization": 365,
    "sharpe_ratio": 1.2980448365292816,
    "calmar_ratio": 1.7239776211318136,
    "sortino_ratio": 2.2126102209089513,
    "omega_ratio": 1.3633717205704499,
    "serenity_index": null,
    "total_open_trades": 0,
    "open_pl": 0,
    "winning_streak": 7,
    "losing_streak": 5,
    "largest_losing_trade": -179.21320229381465,
    "largest_winning_trade": 1832.6324718228998,
    "current_streak": -2,
    "avg_trades_per_day": 0.10614814833736631,
    "avg_trades_per_week": 0.7430370383615642,
    "avg_trades_per_month": 3.2311496353894307
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
          "eligible_sizing_attempts": 206,
          "margin_limited": 0,
          "notional_or_weight_limited": 19,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 19,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR101",
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
  "log_size_bytes": 808302
}
```

## C

[C](http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a)

ID: 1a62497a-7609-4bfd-9153-15c8640cf67a. Status finished; error null. Snapshot3/3 byte-exact against sources both before and after run. Dates exclusive2025-12-31 and all routes/settings unchanged from verified draft. Stored form and summaries below.

```json
{
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BtcEntryR101"
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
    "total": 209,
    "total_winning_trades": 109,
    "total_losing_trades": 100,
    "starting_balance": 10000,
    "finishing_balance": 19028.417562861017,
    "win_rate": 0.5215311004784688,
    "win_rate_longs": 0.48863636363636365,
    "win_rate_shorts": 0.5454545454545454,
    "ratio_avg_win_loss": 1.612997820805192,
    "longs_count": 88,
    "longs_percentage": 42.10526315789473,
    "shorts_percentage": 57.89473684210527,
    "shorts_count": 121,
    "fee": 1402.9967891035176,
    "net_profit": 9028.417562861003,
    "net_profit_percentage": 90.28417562861003,
    "average_win": 192.07913105503042,
    "average_loss": 119.0820772213731,
    "expectancy": 43.19817015722967,
    "expectancy_percentage": 0.43198170157229665,
    "expected_net_profit_every_100_trades": 43.19817015722967,
    "average_holding_period": 343056.17224880384,
    "average_winning_holding_period": 503701.1009174312,
    "average_losing_holding_period": 167953.2,
    "gross_profit": 20936.625284998314,
    "gross_loss": -11908.20772213731,
    "max_drawdown": -8.168012803517167,
    "max_underwater_period": 261,
    "annual_return": 13.133209548881176,
    "annualization": 365,
    "sharpe_ratio": 1.28889853670307,
    "calmar_ratio": 1.607883075700614,
    "sortino_ratio": 2.1619346375613597,
    "omega_ratio": 1.3493638487194548,
    "serenity_index": null,
    "total_open_trades": 1,
    "open_pl": -97.24825000000055,
    "winning_streak": 7,
    "losing_streak": 5,
    "largest_losing_trade": -181.789179990066,
    "largest_winning_trade": 1800.1964988702819,
    "current_streak": -3,
    "avg_trades_per_day": 0.10982654951737406,
    "avg_trades_per_week": 0.7687858466216184,
    "avg_trades_per_month": 3.343120167308866
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
          "eligible_sizing_attempts": 206,
          "margin_limited": 0,
          "notional_or_weight_limited": 18,
          "risk_budget_limited": 0,
          "sized_below_trade_target": 18,
          "zero_after_lot_rounding": 0
        }
      },
      "notional_cap": 4.4,
      "portfolio_risk": 0.08,
      "strategy": "BtcEntryR101",
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
  "log_size_bytes": 830371
}
```

Terminal note: engine summary total_open_trades=1/open_pl=-97.24825 is pretermination. Logs explicitly record SPY boundary liquidation at2025-12-31T00:00:00, SELL MARKET executed, fee10.97, realizedPNL−97.25 and final wallet19028.42. Root fills/MTM reconciliation still required; this is not evidence of native liquidity.

Capacity interpretation: BTC sizing attempts long45/short206 in each; short notional_or_weight cuts B19/C18. No risk/margin/zero-capacity/lot-zero cuts observed, nor any PAXG/SPY cut. Attempts cover only baseline-qualified plans reaching sizing after gate, not all eligible price opportunities while occupied; no attempt−trade counterfactual. Six capacityJSON records captured across pair. Same8 stored hp entries (DNA empty plus7 defaults) verify the reported session hyperparameters; source snapshots verify all three source default declarations, not independent per-route runtime hp telemetry.
