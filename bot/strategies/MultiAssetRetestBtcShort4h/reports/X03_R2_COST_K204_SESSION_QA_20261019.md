# K204 Session QA

Ambas finished/errornull. Forms exactos contrato y6snapshots exactos pre-run. Hp defaults ylogs terminal verificados. Detalle abajo. Métrica open1C preterminación no residual: log cierraSPY al final; root concilia exactamente. Root auditaMTM/fricción; no variar receta después del resultado.

```json
{
  "B": {
    "dashboard_url": "http://localhost:9200/#/backtest/aeebb5e3-cf63-4fcf-98b9-600b394a7c6c",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR204"
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
      "total": 272,
      "total_winning_trades": 142,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 22538.614825008597,
      "win_rate": 0.5220588235294118,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5287958115183246,
      "ratio_avg_win_loss": 1.6355843079082595,
      "longs_count": 81,
      "longs_percentage": 29.77941176470588,
      "shorts_percentage": 70.22058823529412,
      "shorts_count": 191,
      "fee": 1892.355510296146,
      "net_profit": 12538.614825008604,
      "net_profit_percentage": 125.38614825008605,
      "average_win": 200.56103314288794,
      "average_loss": 122.62347600985755,
      "expectancy": 46.097848621355176,
      "expectancy_percentage": 0.4609784862135518,
      "expected_net_profit_every_100_trades": 46.09784862135518,
      "average_holding_period": 276535.3676470588,
      "average_winning_holding_period": 397661.40845070424,
      "average_losing_holding_period": 144228.46153846153,
      "gross_profit": 28479.66670629009,
      "gross_loss": -15941.051881281483,
      "max_drawdown": -8.261099190210984,
      "max_underwater_period": 291,
      "annual_return": 16.867107229604695,
      "annualization": 365,
      "sharpe_ratio": 1.522647088459778,
      "calmar_ratio": 2.041750963309026,
      "sortino_ratio": 2.676469531701654,
      "omega_ratio": 1.3996600328502597,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -215.8746512382034,
      "largest_winning_trade": 1994.812336585988,
      "current_streak": -3,
      "avg_trades_per_day": 0.14293216013744375,
      "avg_trades_per_week": 1.0005251209621062,
      "avg_trades_per_month": 4.350854954583788
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"X03CostR204\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR204\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  "C": {
    "dashboard_url": "http://localhost:9200/#/backtest/7f0315fb-2547-4df1-a181-537cd43c6d0f",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR204"
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
      "total": 279,
      "total_winning_trades": 144,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 22732.271244098858,
      "win_rate": 0.5161290322580645,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5287958115183246,
      "ratio_avg_win_loss": 1.6611421166910163,
      "longs_count": 88,
      "longs_percentage": 31.54121863799283,
      "shorts_percentage": 68.45878136200717,
      "shorts_count": 191,
      "fee": 1991.5809857359761,
      "net_profit": 12732.27124409883,
      "net_profit_percentage": 127.32271244098831,
      "average_win": 202.96742605595932,
      "average_loss": 122.18546746636528,
      "expectancy": 45.63538080322161,
      "expectancy_percentage": 0.4563538080322161,
      "expected_net_profit_every_100_trades": 45.63538080322161,
      "average_holding_period": 288941.5053763441,
      "average_winning_holding_period": 416387.5,
      "average_losing_holding_period": 152999.11111111112,
      "gross_profit": 29227.309352058142,
      "gross_loss": -16495.038107959313,
      "max_drawdown": -8.98905551217971,
      "max_underwater_period": 219,
      "annual_return": 17.059039631098784,
      "annualization": 365,
      "sharpe_ratio": 1.512707405168724,
      "calmar_ratio": 1.897756622815896,
      "sortino_ratio": 2.6221653666967772,
      "omega_ratio": 1.3876092340054111,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -116.1765000000014,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -219.08993904284455,
      "largest_winning_trade": 1962.3763636333701,
      "current_streak": -4,
      "avg_trades_per_day": 0.1466105613174515,
      "avg_trades_per_week": 1.0262739292221605,
      "avg_trades_per_month": 4.462825486503224
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"X03CostR204\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR204\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -116.1765(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  }
}
```
