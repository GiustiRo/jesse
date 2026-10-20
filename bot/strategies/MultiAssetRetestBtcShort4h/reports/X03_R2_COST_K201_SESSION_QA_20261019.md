# K201 Session QA

Ambas finished/errornull. Formularios exactos contrato,6snapshots exactos pre-run, hp defaults. 77suplementos vs79X03;91eventos gate-pass,4rechazosgate,11events_occupied. Contadores no observan todos rechazos de motor. No capacidad/margen/riesgo/lotzero limitantes; BTCnocionalquota24B/23C. C open1 en métrica preterminación tiene cierreSPY terminal log y balance22513.88; rootconciliaráfills/PNL exactos. Sin juicio calendario/fricción antes auditor root.

```json
{
  "B": {
    "dashboard_url": "http://localhost:9200/#/backtest/64e9c1ac-b90b-4d82-884d-d6f39f110b48",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR201"
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
      "total": 271,
      "total_winning_trades": 144,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 22331.56315784915,
      "win_rate": 0.5313653136531366,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5421052631578948,
      "ratio_avg_win_loss": 1.582562539902246,
      "longs_count": 81,
      "longs_percentage": 29.88929889298893,
      "shorts_percentage": 70.11070110701107,
      "shorts_count": 190,
      "fee": 1859.7036721227846,
      "net_profit": 12331.56315784912,
      "net_profit_percentage": 123.31563157849119,
      "average_win": 193.43505040775187,
      "average_loss": 122.22900866824527,
      "expectancy": 45.503923091694176,
      "expectancy_percentage": 0.45503923091694176,
      "expected_net_profit_every_100_trades": 45.503923091694176,
      "average_holding_period": 276787.9704797048,
      "average_winning_holding_period": 392177.5,
      "average_losing_holding_period": 145952.59842519686,
      "gross_profit": 27854.647258716268,
      "gross_loss": -15523.084100867149,
      "max_drawdown": -8.253965403629948,
      "max_underwater_period": 291,
      "annual_return": 16.660418848614466,
      "annualization": 365,
      "sharpe_ratio": 1.5231898882644994,
      "calmar_ratio": 2.0184745190823685,
      "sortino_ratio": 2.6594483071198165,
      "omega_ratio": 1.399284080826476,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -213.8964511172628,
      "largest_winning_trade": 1994.812336585988,
      "current_streak": -3,
      "avg_trades_per_day": 0.1424066742545855,
      "avg_trades_per_week": 0.9968467197820985,
      "avg_trades_per_month": 4.334859164309583
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
    "terminal_logs": [
      "[INFO | 2025-12-30T00:01:00] Saved daily portfolio balance: 22331.56",
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 77, \"cost_gate_rejected\": 4, \"events\": 91, \"events_occupied\": 11, \"fills\": 77}, \"recipe\": \"X03CostR201\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR201\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 22331.56"
    ]
  },
  "C": {
    "dashboard_url": "http://localhost:9200/#/backtest/78fbb206-2610-4bca-a5b1-70ca308768bc",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR201"
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
      "total": 278,
      "total_winning_trades": 146,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 22513.877531545368,
      "win_rate": 0.5251798561151079,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5421052631578948,
      "ratio_avg_win_loss": 1.6082907971022946,
      "longs_count": 88,
      "longs_percentage": 31.654676258992804,
      "shorts_percentage": 68.34532374100719,
      "shorts_count": 190,
      "fee": 1957.3088673051614,
      "net_profit": 12513.877531545357,
      "net_profit_percentage": 125.13877531545357,
      "average_win": 195.7578516747517,
      "average_loss": 121.71794555279085,
      "expectancy": 45.0139479551991,
      "expectancy_percentage": 0.450139479551991,
      "expected_net_profit_every_100_trades": 45.0139479551991,
      "average_holding_period": 289232.3741007194,
      "average_winning_holding_period": 410722.19178082194,
      "average_losing_holding_period": 154857.27272727274,
      "gross_profit": 28580.646344513745,
      "gross_loss": -16066.768812968392,
      "max_drawdown": -9.009386028595156,
      "max_underwater_period": 219,
      "annual_return": 16.8424942590216,
      "annualization": 365,
      "sharpe_ratio": 1.5121215529657197,
      "calmar_ratio": 1.8694386282888436,
      "sortino_ratio": 2.6031289895587237,
      "omega_ratio": 1.3869164394683444,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -115.06000000000131,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -216.99202075896523,
      "largest_winning_trade": 1962.3763636333701,
      "current_streak": -4,
      "avg_trades_per_day": 0.14608507543459326,
      "avg_trades_per_week": 1.0225955280421528,
      "avg_trades_per_month": 4.446829696229019
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
    "terminal_logs": [
      "[INFO | 2025-12-31T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 77, \"cost_gate_rejected\": 4, \"events\": 91, \"events_occupied\": 11, \"fills\": 77}, \"recipe\": \"X03CostR201\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 23, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 23, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR201\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -115.06(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Saved daily portfolio balance: 22513.88"
    ]
  }
}
```
