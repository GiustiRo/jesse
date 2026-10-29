# K203 Session QA

Ambas finished/errornull. Forms exactos contrato y6snapshots exactos pre-run. Hp defaults ylogs terminal verificados. Detalle abajo. Métrica open1C preterminación no residual: log cierraSPY al final; root concilia exactamente. Root auditaMTM/fricción; no variar receta después del neto inferior.

```json
{
  "B": {
    "dashboard_url": "http://localhost:9200/#/backtest/e43169c8-8280-46ff-916c-c69bfcde5f5b",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR203"
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
      "total": 248,
      "total_winning_trades": 126,
      "total_losing_trades": 122,
      "starting_balance": 10000,
      "finishing_balance": 18667.91617763922,
      "win_rate": 0.5080645161290323,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5089820359281437,
      "ratio_avg_win_loss": 1.5775992104528833,
      "longs_count": 81,
      "longs_percentage": 32.66129032258064,
      "shorts_percentage": 67.33870967741936,
      "shorts_count": 167,
      "fee": 1529.8410742612766,
      "net_profit": 8667.916177639248,
      "net_profit_percentage": 86.67916177639249,
      "average_win": 178.10553386113915,
      "average_loss": 112.8965663021663,
      "expectancy": 34.95127490983566,
      "expectancy_percentage": 0.3495127490983566,
      "expected_net_profit_every_100_trades": 34.95127490983566,
      "average_holding_period": 293384.03225806454,
      "average_winning_holding_period": 430701.4285714286,
      "average_losing_holding_period": 151564.4262295082,
      "gross_profit": 22441.297266503534,
      "gross_loss": -13773.38108886429,
      "max_drawdown": -8.152415579386386,
      "max_underwater_period": 333,
      "annual_return": 12.718924888920235,
      "annualization": 365,
      "sharpe_ratio": 1.2305579086848062,
      "calmar_ratio": 1.5601418702305117,
      "sortino_ratio": 2.0787012831119775,
      "omega_ratio": 1.3188087345123425,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -178.96852108666505,
      "largest_winning_trade": 1852.0940555944703,
      "current_streak": -2,
      "avg_trades_per_day": 0.1303204989488458,
      "avg_trades_per_week": 0.9122434926419205,
      "avg_trades_per_month": 3.9669559880028658
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 49, \"confirmation_occupied\": 14, \"confirmation_rejected\": 31, \"confirmed_events\": 50, \"events\": 95, \"events_occupied\": 11, \"fills\": 49}, \"recipe\": \"X03CostR203\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 250, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR203\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  "C": {
    "dashboard_url": "http://localhost:9200/#/backtest/078d9516-3490-480c-9490-29d97ee7e223",
    "status": "finished",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03CostR203"
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
      "total": 255,
      "total_winning_trades": 128,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 18837.35521563915,
      "win_rate": 0.5019607843137255,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5089820359281437,
      "ratio_avg_win_loss": 1.6064803509722128,
      "longs_count": 88,
      "longs_percentage": 34.509803921568626,
      "shorts_percentage": 65.49019607843138,
      "shorts_count": 167,
      "fee": 1619.9258647865295,
      "net_profit": 8837.35521563912,
      "net_profit_percentage": 88.3735521563912,
      "average_win": 180.5561555201371,
      "average_loss": 112.39238339321598,
      "expectancy": 34.65629496329067,
      "expectancy_percentage": 0.3465629496329067,
      "expected_net_profit_every_100_trades": 34.65629496329067,
      "average_holding_period": 306495.29411764705,
      "average_winning_holding_period": 451252.03125,
      "average_losing_holding_period": 160598.74015748032,
      "gross_profit": 23111.18790657755,
      "gross_loss": -14273.832690938429,
      "max_drawdown": -8.242300488478238,
      "max_underwater_period": 255,
      "annual_return": 12.914440485659885,
      "annualization": 365,
      "sharpe_ratio": 1.225254420503355,
      "calmar_ratio": 1.5668490251857168,
      "sortino_ratio": 2.0412187284851533,
      "omega_ratio": 1.309668333480675,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -96.27200000000084,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -181.94380052612527,
      "largest_winning_trade": 1822.9016799371145,
      "current_streak": -3,
      "avg_trades_per_day": 0.13399890012885352,
      "avg_trades_per_week": 0.9379923009019746,
      "avg_trades_per_month": 4.078926519922301
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
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 49, \"confirmation_occupied\": 14, \"confirmation_rejected\": 31, \"confirmed_events\": 50, \"events\": 95, \"events_occupied\": 11, \"fills\": 49}, \"recipe\": \"X03CostR203\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 250, \"margin_limited\": 0, \"notional_or_weight_limited\": 19, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 19, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03CostR203\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating PAXG-USDT...",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] Terminating SPY-USDT...",
      "[INFO | 2025-12-31T00:00:00] Closed open Binance Perpetual Futures-SPY-USDT position at 689.5951 with PNL: -96.272(-1.99%) because we reached the end of the backtest session.",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  }
}
```
