# K202 Session QA

Ambas finished/errornull. Forms exactos contrato y6snapshots exactos pre-run. Hp defaults ylogs terminal verificados. Detalle abajo. Métrica open1C preterminación no residual: log cierraSPY al final; root concilia exactamente. Root auditaMTM/fricción; no variar receta después del neto inferior.

```json
{
  "B": {
    "dashboard_url": "http://localhost:9200/#/backtest/e86d1b9c-c1d1-4ec4-81a8-ae8318bf6162",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR202"
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
      "total": 236,
      "total_winning_trades": 121,
      "total_losing_trades": 115,
      "starting_balance": 10000,
      "finishing_balance": 18837.166239332328,
      "win_rate": 0.5127118644067796,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5161290322580645,
      "ratio_avg_win_loss": 1.5712342377534743,
      "longs_count": 81,
      "longs_percentage": 34.32203389830508,
      "shorts_percentage": 65.67796610169492,
      "shorts_count": 155,
      "fee": 1551.4988184882168,
      "net_profit": 8837.166239332335,
      "net_profit_percentage": 88.37166239332335,
      "average_win": 184.84264702381756,
      "average_loss": 117.64168739608337,
      "expectancy": 37.44561965818786,
      "expectancy_percentage": 0.3744561965818786,
      "expected_net_profit_every_100_trades": 37.44561965818786,
      "average_holding_period": 296282.7966101695,
      "average_winning_holding_period": 439546.6115702479,
      "average_losing_holding_period": 145544.34782608695,
      "gross_profit": 22365.960289881925,
      "gross_loss": -13528.794050549588,
      "max_drawdown": -8.1552347835,
      "max_underwater_period": 292,
      "annual_return": 12.914223219167265,
      "annualization": 365,
      "sharpe_ratio": 1.2576454440828797,
      "calmar_ratio": 1.5835501444171596,
      "sortino_ratio": 2.1530576621544637,
      "omega_ratio": 1.335254761324786,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -181.32159290903724,
      "largest_winning_trade": 1839.1196664134234,
      "current_streak": -3,
      "avg_trades_per_day": 0.12401466835454679,
      "avg_trades_per_week": 0.8681026784818275,
      "avg_trades_per_month": 3.7750065047124046
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 33, \"events\": 60, \"events_occupied\": 7, \"fills\": 33}, \"recipe\": \"X03CostR202\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 259, \"margin_limited\": 0, \"notional_or_weight_limited\": 27, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 27, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR202\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  "C": {
    "dashboard_url": "http://localhost:9200/#/backtest/48794472-4f2a-4c60-8b2c-0786de70e0d7",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR202"
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
      "total": 243,
      "total_winning_trades": 123,
      "total_losing_trades": 120,
      "starting_balance": 10000,
      "finishing_balance": 19032.181354353397,
      "win_rate": 0.5061728395061729,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5161290322580645,
      "ratio_avg_win_loss": 1.6029276899156772,
      "longs_count": 88,
      "longs_percentage": 36.21399176954733,
      "shorts_percentage": 63.78600823045267,
      "shorts_count": 155,
      "fee": 1643.332525673009,
      "net_profit": 9032.181354353384,
      "net_profit_percentage": 90.32181354353385,
      "average_win": 187.63496280800547,
      "average_loss": 117.05765892526075,
      "expectancy": 37.16947059404684,
      "expectancy_percentage": 0.37169470594046844,
      "expected_net_profit_every_100_trades": 37.16947059404684,
      "average_holding_period": 309958.02469135803,
      "average_winning_holding_period": 460788.7804878049,
      "average_losing_holding_period": 155356.5,
      "gross_profit": 23079.100425384673,
      "gross_loss": -14046.91907103129,
      "max_drawdown": -8.162172788448018,
      "max_underwater_period": 223,
      "annual_return": 13.137501278535368,
      "annualization": 365,
      "sharpe_ratio": 1.2548061504736063,
      "calmar_ratio": 1.609559319441138,
      "sortino_ratio": 2.116391708492958,
      "omega_ratio": 1.3252631380652524,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -97.26749999999811,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -184.8685822213889,
      "largest_winning_trade": 1809.9272907560674,
      "current_streak": -4,
      "avg_trades_per_day": 0.12769306953455453,
      "avg_trades_per_week": 0.8938514867418818,
      "avg_trades_per_month": 3.88697703663184
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 33, \"events\": 60, \"events_occupied\": 7, \"fills\": 33}, \"recipe\": \"X03CostR202\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 259, \"margin_limited\": 0, \"notional_or_weight_limited\": 26, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 26, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR202\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -97.2675(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  }
}
```
