# X03 R2 — validation sessions

Seven frozen tests × B/C=14 finished without errors; sensitivity excluded from economic selection. QA156PASS. All completed forms, HP and42route snapshots checked. Root owns full fills/MTM/cost/calendar audit. Engine pretermination open counters with executed terminal closes do not alone imply residual. No 2026 data.

```json
[
  {
    "variant": "V201",
    "portfolio": "B",
    "id": "dc09487b-eb8a-44c3-97c4-4b2acfeab83f",
    "url": "http://localhost:9200/#/backtest/dc09487b-eb8a-44c3-97c4-4b2acfeab83f",
    "status": "finished",
    "metrics": {
      "total": 294,
      "total_winning_trades": 144,
      "total_losing_trades": 150,
      "starting_balance": 10000,
      "finishing_balance": 19748.306765324753,
      "win_rate": 0.4897959183673469,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.4835680751173709,
      "ratio_avg_win_loss": 1.5892680382856197,
      "longs_count": 81,
      "longs_percentage": 27.55102040816326,
      "shorts_percentage": 72.44897959183675,
      "shorts_count": 213,
      "fee": 1966.4067278846208,
      "net_profit": 9748.306765324742,
      "net_profit_percentage": 97.48306765324742,
      "average_win": 196.47138985085266,
      "average_loss": 123.62382248798693,
      "expectancy": 33.157506004505926,
      "expectancy_percentage": 0.33157506004505927,
      "expected_net_profit_every_100_trades": 33.157506004505926,
      "average_holding_period": 260131.22448979592,
      "average_winning_holding_period": 392618.75,
      "average_losing_holding_period": 132943.2,
      "gross_profit": 28291.88013852278,
      "gross_loss": -18543.57337319804,
      "max_drawdown": -10.769248655750928,
      "max_underwater_period": 301,
      "annual_return": 13.941869913831928,
      "annualization": 365,
      "sharpe_ratio": 1.2720340903848035,
      "calmar_ratio": 1.2946000560946074,
      "sortino_ratio": 2.163703973757444,
      "omega_ratio": 1.3121105654242473,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 8,
      "losing_streak": 7,
      "largest_losing_trade": -193.12057259133536,
      "largest_winning_trade": 2020.7611149480822,
      "current_streak": -4,
      "avg_trades_per_day": 0.15449284956032525,
      "avg_trades_per_week": 1.0814499469222767,
      "avg_trades_per_month": 4.7027623406163
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR201"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 100, \"events\": 128, \"events_occupied\": 23, \"fills\": 100}, \"recipe\": \"V201\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 296, \"margin_limited\": 0, \"notional_or_weight_limited\": 28, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 28, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR201\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V201",
    "portfolio": "C",
    "id": "7f1c089a-2751-43fc-989d-8922c09d92a5",
    "url": "http://localhost:9200/#/backtest/7f1c089a-2751-43fc-989d-8922c09d92a5",
    "status": "finished",
    "metrics": {
      "total": 301,
      "total_winning_trades": 146,
      "total_losing_trades": 155,
      "starting_balance": 10000,
      "finishing_balance": 19928.659299442552,
      "win_rate": 0.4850498338870432,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.4835680751173709,
      "ratio_avg_win_loss": 1.6134841996519105,
      "longs_count": 88,
      "longs_percentage": 29.2358803986711,
      "shorts_percentage": 70.7641196013289,
      "shorts_count": 213,
      "fee": 2064.2278019928135,
      "net_profit": 9928.659299442543,
      "net_profit_percentage": 99.28659299442543,
      "average_win": 198.83324747139454,
      "average_loss": 123.2322247185875,
      "expectancy": 32.98557906791543,
      "expectancy_percentage": 0.3298557906791543,
      "expected_net_profit_every_100_trades": 32.98557906791543,
      "average_holding_period": 272012.0930232558,
      "average_winning_holding_period": 411157.397260274,
      "average_losing_holding_period": 140946.1935483871,
      "gross_profit": 29029.654130823605,
      "gross_loss": -19100.994831381064,
      "max_drawdown": -10.6994668447837,
      "max_underwater_period": 220,
      "annual_return": 14.140723254859267,
      "annualization": 365,
      "sharpe_ratio": 1.2642622075433985,
      "calmar_ratio": 1.3216287745920048,
      "sortino_ratio": 2.1190155242636703,
      "omega_ratio": 1.3040123155652155,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -102.92425000000003,
      "winning_streak": 8,
      "losing_streak": 7,
      "largest_losing_trade": -195.62863197563843,
      "largest_winning_trade": 1988.3251419954643,
      "current_streak": -5,
      "avg_trades_per_day": 0.15817125074033297,
      "avg_trades_per_week": 1.1071987551823308,
      "avg_trades_per_month": 4.814732872535736
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR201"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 100, \"events\": 128, \"events_occupied\": 23, \"fills\": 100}, \"recipe\": \"V201\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 296, \"margin_limited\": 0, \"notional_or_weight_limited\": 27, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 27, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR201\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V202",
    "portfolio": "B",
    "id": "ad180c10-f055-4b12-8432-e369caac8c3a",
    "url": "http://localhost:9200/#/backtest/ad180c10-f055-4b12-8432-e369caac8c3a",
    "status": "finished",
    "metrics": {
      "total": 252,
      "total_winning_trades": 135,
      "total_losing_trades": 117,
      "starting_balance": 10000,
      "finishing_balance": 22393.82808244988,
      "win_rate": 0.5357142857142857,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5497076023391813,
      "ratio_avg_win_loss": 1.6285248775232104,
      "longs_count": 81,
      "longs_percentage": 32.142857142857146,
      "shorts_percentage": 67.85714285714286,
      "shorts_count": 171,
      "fee": 1733.0263447826792,
      "net_profit": 12393.828082449887,
      "net_profit_percentage": 123.93828082449888,
      "average_win": 196.24199215371254,
      "average_loss": 120.50291331881458,
      "expectancy": 49.18185747003923,
      "expectancy_percentage": 0.49181857470039236,
      "expected_net_profit_every_100_trades": 49.18185747003923,
      "average_holding_period": 290767.85714285716,
      "average_winning_holding_period": 410489.3333333333,
      "average_losing_holding_period": 152627.6923076923,
      "gross_profit": 26492.668940751195,
      "gross_loss": -14098.840858301306,
      "max_drawdown": -7.5141067541671935,
      "max_underwater_period": 292,
      "annual_return": 16.72273680062457,
      "annualization": 365,
      "sharpe_ratio": 1.552495487450195,
      "calmar_ratio": 2.2255122728127907,
      "sortino_ratio": 2.6997748639815824,
      "omega_ratio": 1.417323687391202,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -209.58659725146723,
      "largest_winning_trade": 1926.6967933854908,
      "current_streak": -3,
      "avg_trades_per_day": 0.13242244248027876,
      "avg_trades_per_week": 0.9269570973619513,
      "avg_trades_per_month": 4.0309391490996855
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR202"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 57, \"events\": 73, \"events_occupied\": 13, \"fills\": 57}, \"recipe\": \"V202\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 254, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR202\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V202",
    "portfolio": "C",
    "id": "7895cfd4-60e8-4813-86a3-31c5a4345666",
    "url": "http://localhost:9200/#/backtest/7895cfd4-60e8-4813-86a3-31c5a4345666",
    "status": "finished",
    "metrics": {
      "total": 259,
      "total_winning_trades": 137,
      "total_losing_trades": 122,
      "starting_balance": 10000,
      "finishing_balance": 22614.45054740168,
      "win_rate": 0.528957528957529,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5497076023391813,
      "ratio_avg_win_loss": 1.6569880654488627,
      "longs_count": 88,
      "longs_percentage": 33.97683397683397,
      "shorts_percentage": 66.02316602316603,
      "shorts_count": 171,
      "fee": 1832.8882994650048,
      "net_profit": 12614.450547401677,
      "net_profit_percentage": 126.14450547401677,
      "average_win": 199.05264755390132,
      "average_loss": 120.12919809412135,
      "expectancy": 48.70444226796016,
      "expectancy_percentage": 0.4870444226796016,
      "expected_net_profit_every_100_trades": 48.70444226796016,
      "average_holding_period": 303747.3359073359,
      "average_winning_holding_period": 429984.96350364963,
      "average_losing_holding_period": 161988.68852459016,
      "gross_profit": 27270.21271488448,
      "gross_loss": -14655.762167482804,
      "max_drawdown": -7.701482653717651,
      "max_underwater_period": 223,
      "annual_return": 16.94242600899716,
      "annualization": 365,
      "sharpe_ratio": 1.5425914436154662,
      "calmar_ratio": 2.199891471653024,
      "sortino_ratio": 2.641425240210545,
      "omega_ratio": 1.4027876013704539,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -115.9509999999973,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -212.98431273296745,
      "largest_winning_trade": 1897.5044177281347,
      "current_streak": -4,
      "avg_trades_per_day": 0.13610084366028652,
      "avg_trades_per_week": 0.9527059056220056,
      "avg_trades_per_month": 4.1429096810191215
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR202"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 57, \"events\": 73, \"events_occupied\": 13, \"fills\": 57}, \"recipe\": \"V202\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 254, \"margin_limited\": 0, \"notional_or_weight_limited\": 19, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 19, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR202\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V203",
    "portfolio": "B",
    "id": "282ac385-0a2d-4793-9a80-038232c399d9",
    "url": "http://localhost:9200/#/backtest/282ac385-0a2d-4793-9a80-038232c399d9",
    "status": "finished",
    "metrics": {
      "total": 276,
      "total_winning_trades": 146,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 21525.62084841026,
      "win_rate": 0.5289855072463768,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5384615384615384,
      "ratio_avg_win_loss": 1.5363034184605695,
      "longs_count": 81,
      "longs_percentage": 29.347826086956523,
      "shorts_percentage": 70.65217391304347,
      "shorts_count": 195,
      "fee": 1892.452594651545,
      "net_profit": 11525.620848410243,
      "net_profit_percentage": 115.25620848410243,
      "average_win": 187.7708859800029,
      "average_loss": 122.22252695900136,
      "expectancy": 41.75949582757336,
      "expectancy_percentage": 0.4175949582757336,
      "expected_net_profit_every_100_trades": 41.75949582757336,
      "average_holding_period": 269537.39130434784,
      "average_winning_holding_period": 381402.7397260274,
      "average_losing_holding_period": 143904,
      "gross_profit": 27414.549353080423,
      "gross_loss": -15888.928504670177,
      "max_drawdown": -8.213630745429445,
      "max_underwater_period": 325,
      "annual_return": 15.840841973670727,
      "annualization": 365,
      "sharpe_ratio": 1.4696217038547552,
      "calmar_ratio": 1.9286041051316456,
      "sortino_ratio": 2.534021514030235,
      "omega_ratio": 1.3821935521626387,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -206.18318090506514,
      "largest_winning_trade": 2027.2483095386058,
      "current_streak": -3,
      "avg_trades_per_day": 0.14503410366887676,
      "avg_trades_per_week": 1.0152387256821374,
      "avg_trades_per_month": 4.414838115680609
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR203"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"V203\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 282, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR203\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V203",
    "portfolio": "C",
    "id": "e039907b-67a5-4531-8ffe-14842cc4fd01",
    "url": "http://localhost:9200/#/backtest/e039907b-67a5-4531-8ffe-14842cc4fd01",
    "status": "finished",
    "metrics": {
      "total": 283,
      "total_winning_trades": 148,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 21733.799358576503,
      "win_rate": 0.5229681978798587,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5384615384615384,
      "ratio_avg_win_loss": 1.5628863024605228,
      "longs_count": 88,
      "longs_percentage": 31.09540636042403,
      "shorts_percentage": 68.90459363957598,
      "shorts_count": 195,
      "fee": 1991.4525344584379,
      "net_profit": 11733.799358576493,
      "net_profit_percentage": 117.33799358576493,
      "average_win": 190.41774114009027,
      "average_loss": 121.83723207523605,
      "expectancy": 41.462188546206704,
      "expectancy_percentage": 0.414621885462067,
      "expected_net_profit_every_100_trades": 41.462188546206704,
      "average_holding_period": 281941.27208480565,
      "average_winning_holding_period": 399842.4324324324,
      "average_losing_holding_period": 152686.66666666666,
      "gross_profit": 28181.82568873336,
      "gross_loss": -16448.026330156867,
      "max_drawdown": -9.03097656487648,
      "max_underwater_period": 191,
      "annual_return": 16.05488705737621,
      "annualization": 365,
      "sharpe_ratio": 1.4615197124176413,
      "calmar_ratio": 1.7777575815906015,
      "sortino_ratio": 2.485247053135979,
      "omega_ratio": 1.370967764831443,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -111.07250000000204,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -209.47828081833217,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14871250484888449,
      "avg_trades_per_week": 1.0409875339421915,
      "avg_trades_per_month": 4.526808647600044
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR203"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"V203\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 282, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR203\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V204",
    "portfolio": "B",
    "id": "ef335fc4-a08a-47b5-ba2f-d29e5b9159fa",
    "url": "http://localhost:9200/#/backtest/ef335fc4-a08a-47b5-ba2f-d29e5b9159fa",
    "status": "finished",
    "metrics": {
      "total": 272,
      "total_winning_trades": 142,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 22701.158448965478,
      "win_rate": 0.5220588235294118,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5287958115183246,
      "ratio_avg_win_loss": 1.6413736470029392,
      "longs_count": 81,
      "longs_percentage": 29.77941176470588,
      "shorts_percentage": 70.22058823529412,
      "shorts_count": 191,
      "fee": 1901.9480724556008,
      "net_profit": 12701.158448965438,
      "net_profit_percentage": 127.01158448965437,
      "average_win": 202.25403889600716,
      "average_loss": 123.22242364821213,
      "expectancy": 46.69543547413766,
      "expectancy_percentage": 0.46695435474137664,
      "expected_net_profit_every_100_trades": 46.69543547413767,
      "average_holding_period": 277023.5294117647,
      "average_winning_holding_period": 398596.4788732394,
      "average_losing_holding_period": 144228.46153846153,
      "gross_profit": 28720.073523233015,
      "gross_loss": -16018.915074267577,
      "max_drawdown": -8.240289584499838,
      "max_underwater_period": 291,
      "annual_return": 17.028293139842088,
      "annualization": 365,
      "sharpe_ratio": 1.5348307140516815,
      "calmar_ratio": 2.0664678061645643,
      "sortino_ratio": 2.700703663631281,
      "omega_ratio": 1.403276137586107,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -217.43098735640734,
      "largest_winning_trade": 2011.030323062297,
      "current_streak": -3,
      "avg_trades_per_day": 0.14293216013744375,
      "avg_trades_per_week": 1.0005251209621062,
      "avg_trades_per_month": 4.350854954583788
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR204"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"V204\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR204\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V204",
    "portfolio": "C",
    "id": "798a0f06-6005-4bea-bebc-dc22a89093dd",
    "url": "http://localhost:9200/#/backtest/798a0f06-6005-4bea-bebc-dc22a89093dd",
    "status": "finished",
    "metrics": {
      "total": 279,
      "total_winning_trades": 144,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 22906.3218001932,
      "win_rate": 0.5161290322580645,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5287958115183246,
      "ratio_avg_win_loss": 1.6673361363950163,
      "longs_count": 88,
      "longs_percentage": 31.54121863799283,
      "shorts_percentage": 68.45878136200717,
      "shorts_count": 191,
      "fee": 2001.9541166683687,
      "net_profit": 12906.321800193182,
      "net_profit_percentage": 129.0632180019318,
      "average_win": 204.7565471311136,
      "average_loss": 122.80459990138651,
      "expectancy": 46.25921792183935,
      "expectancy_percentage": 0.4625921792183936,
      "expected_net_profit_every_100_trades": 46.25921792183936,
      "average_holding_period": 289417.4193548387,
      "average_winning_holding_period": 417309.5833333333,
      "average_losing_holding_period": 152999.11111111112,
      "gross_profit": 29484.942786880358,
      "gross_loss": -16578.62098668718,
      "max_drawdown": -8.99776600090566,
      "max_underwater_period": 219,
      "annual_return": 17.230416425872352,
      "annualization": 365,
      "sharpe_ratio": 1.5243421444414555,
      "calmar_ratio": 1.9149660509217559,
      "sortino_ratio": 2.6447531420386303,
      "omega_ratio": 1.3911098866370777,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -117.06749999999738,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -220.78309591869282,
      "largest_winning_trade": 1978.594350109679,
      "current_streak": -4,
      "avg_trades_per_day": 0.1466105613174515,
      "avg_trades_per_week": 1.0262739292221605,
      "avg_trades_per_month": 4.462825486503224
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR204"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 95, \"events_occupied\": 13, \"fills\": 79}, \"recipe\": \"V204\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 274, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR204\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V205",
    "portfolio": "B",
    "id": "e6e91629-fb28-4a05-ac74-2329ee932bfe",
    "url": "http://localhost:9200/#/backtest/e6e91629-fb28-4a05-ac74-2329ee932bfe",
    "status": "finished",
    "metrics": {
      "total": 278,
      "total_winning_trades": 141,
      "total_losing_trades": 137,
      "starting_balance": 10000,
      "finishing_balance": 19992.668912063047,
      "win_rate": 0.5071942446043165,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.5076142131979695,
      "ratio_avg_win_loss": 1.6289531389483844,
      "longs_count": 81,
      "longs_percentage": 29.136690647482016,
      "shorts_percentage": 70.86330935251799,
      "shorts_count": 197,
      "fee": 1800.6882645260532,
      "net_profit": 9992.668912063049,
      "net_profit_percentage": 99.92668912063048,
      "average_win": 175.62763471678917,
      "average_loss": 107.81625972995788,
      "expectancy": 35.94485220166562,
      "expectancy_percentage": 0.35944852201665617,
      "expected_net_profit_every_100_trades": 35.94485220166562,
      "average_holding_period": 258183.6690647482,
      "average_winning_holding_period": 383214.4680851064,
      "average_losing_holding_period": 129502.33576642336,
      "gross_profit": 24763.496495067273,
      "gross_loss": -14770.82758300423,
      "max_drawdown": -8.696777717518078,
      "max_underwater_period": 334,
      "annual_return": 14.210949403037754,
      "annualization": 365,
      "sharpe_ratio": 1.3444871570140557,
      "calmar_ratio": 1.6340476742796792,
      "sortino_ratio": 2.314906673717804,
      "omega_ratio": 1.3526005929949165,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -191.4863511881061,
      "largest_winning_trade": 1936.4275852712763,
      "current_streak": -3,
      "avg_trades_per_day": 0.14608507543459326,
      "avg_trades_per_week": 1.0225955280421528,
      "avg_trades_per_month": 4.446829696229019
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR205"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 95, \"events_occupied\": 12, \"fills\": 80}, \"recipe\": \"V205\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 282, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR205\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V205",
    "portfolio": "C",
    "id": "608630f0-127d-4330-9a43-34f94b25ac72",
    "url": "http://localhost:9200/#/backtest/608630f0-127d-4330-9a43-34f94b25ac72",
    "status": "finished",
    "metrics": {
      "total": 285,
      "total_winning_trades": 143,
      "total_losing_trades": 142,
      "starting_balance": 10000,
      "finishing_balance": 20184.260042281625,
      "win_rate": 0.5017543859649123,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.5076142131979695,
      "ratio_avg_win_loss": 1.6544154561777242,
      "longs_count": 88,
      "longs_percentage": 30.87719298245614,
      "shorts_percentage": 69.12280701754386,
      "shorts_count": 197,
      "fee": 1893.1966612257747,
      "net_profit": 10184.260042281641,
      "net_profit_percentage": 101.8426004228164,
      "average_win": 178.1427997542311,
      "average_loss": 107.67718537023524,
      "expectancy": 35.73424576239174,
      "expectancy_percentage": 0.35734245762391736,
      "expected_net_profit_every_100_trades": 35.73424576239174,
      "average_holding_period": 270779.36842105264,
      "average_winning_holding_period": 402273.56643356645,
      "average_losing_holding_period": 138359.15492957746,
      "gross_profit": 25474.420364855047,
      "gross_loss": -15290.160322573403,
      "max_drawdown": -8.989091027797668,
      "max_underwater_period": 215,
      "annual_return": 14.420067229807266,
      "annualization": 365,
      "sharpe_ratio": 1.3400725749813454,
      "calmar_ratio": 1.6041741245266028,
      "sortino_ratio": 2.2739758506984327,
      "omega_ratio": 1.3426421157233517,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -103.1552499999998,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -194.54201477549557,
      "largest_winning_trade": 1903.9916123186583,
      "current_streak": -4,
      "avg_trades_per_day": 0.149763476614601,
      "avg_trades_per_week": 1.048344336302207,
      "avg_trades_per_month": 4.5588002281484545
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR205"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 95, \"events_occupied\": 12, \"fills\": 80}, \"recipe\": \"V205\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 282, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR205\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V206",
    "portfolio": "B",
    "id": "046eb445-5e0a-413f-aec9-2498a6a3cb38",
    "url": "http://localhost:9200/#/backtest/046eb445-5e0a-413f-aec9-2498a6a3cb38",
    "status": "finished",
    "metrics": {
      "total": 267,
      "total_winning_trades": 136,
      "total_losing_trades": 131,
      "starting_balance": 10000,
      "finishing_balance": 21516.320164100747,
      "win_rate": 0.5093632958801498,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.510752688172043,
      "ratio_avg_win_loss": 1.6580544641931934,
      "longs_count": 81,
      "longs_percentage": 30.337078651685395,
      "shorts_percentage": 69.6629213483146,
      "shorts_count": 186,
      "fee": 1812.185842705271,
      "net_profit": 11516.32016410076,
      "net_profit_percentage": 115.16320164100759,
      "average_win": 202.06999090274118,
      "average_loss": 121.87174502803086,
      "expectancy": 43.13228525880435,
      "expectancy_percentage": 0.43132285258804354,
      "expected_net_profit_every_100_trades": 43.13228525880435,
      "average_holding_period": 289344.9438202247,
      "average_winning_holding_period": 418365.4411764706,
      "average_losing_holding_period": 155400,
      "gross_profit": 27481.5187627728,
      "gross_loss": -15965.198598672043,
      "max_drawdown": -8.215762925591497,
      "max_underwater_period": 300,
      "annual_return": 15.831240213808485,
      "annualization": 365,
      "sharpe_ratio": 1.4460389243473863,
      "calmar_ratio": 1.926934888115544,
      "sortino_ratio": 2.5102953895795355,
      "omega_ratio": 1.3713131376089134,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -206.0805653368319,
      "largest_winning_trade": 1959.1327663381085,
      "current_streak": -3,
      "avg_trades_per_day": 0.1403047307231525,
      "avg_trades_per_week": 0.9821331150620675,
      "avg_trades_per_month": 4.270876003212762
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR206"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 78, \"events\": 95, \"events_occupied\": 15, \"fills\": 78}, \"recipe\": \"V206\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 268, \"margin_limited\": 0, \"notional_or_weight_limited\": 25, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 25, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR206\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V206",
    "portfolio": "C",
    "id": "79037f88-5dcd-4c0e-814f-38ad77b5e6af",
    "url": "http://localhost:9200/#/backtest/79037f88-5dcd-4c0e-814f-38ad77b5e6af",
    "status": "finished",
    "metrics": {
      "total": 274,
      "total_winning_trades": 138,
      "total_losing_trades": 136,
      "starting_balance": 10000,
      "finishing_balance": 21692.917987921242,
      "win_rate": 0.5036496350364964,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.510752688172043,
      "ratio_avg_win_loss": 1.683509744307966,
      "longs_count": 88,
      "longs_percentage": 32.11678832116788,
      "shorts_percentage": 67.88321167883211,
      "shorts_count": 186,
      "fee": 1908.7610317880149,
      "net_profit": 11692.917987921257,
      "net_profit_percentage": 116.92917987921257,
      "average_win": 204.36309668552786,
      "average_loss": 121.39109819618812,
      "expectancy": 42.67488316759586,
      "expectancy_percentage": 0.42674883167595856,
      "expected_net_profit_every_100_trades": 42.67488316759586,
      "average_holding_period": 301650.2189781022,
      "average_winning_holding_period": 437605.652173913,
      "average_losing_holding_period": 163695.4411764706,
      "gross_profit": 28202.107342602845,
      "gross_loss": -16509.189354681585,
      "max_drawdown": -9.036230298563074,
      "max_underwater_period": 220,
      "annual_return": 16.012984776315587,
      "annualization": 365,
      "sharpe_ratio": 1.4357447164593675,
      "calmar_ratio": 1.7720868378998644,
      "sortino_ratio": 2.4574316857389507,
      "omega_ratio": 1.35994156184938,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -110.86624999999913,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -209.08492114010477,
      "largest_winning_trade": 1926.6967933854908,
      "current_streak": -4,
      "avg_trades_per_day": 0.14398313190316026,
      "avg_trades_per_week": 1.0078819233221217,
      "avg_trades_per_month": 4.382846535132199
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR206"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 78, \"events\": 95, \"events_occupied\": 15, \"fills\": 78}, \"recipe\": \"V206\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 268, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR206\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V207",
    "portfolio": "B",
    "id": "37a6818d-37d3-4ffc-b821-f6ed69a1e459",
    "url": "http://localhost:9200/#/backtest/37a6818d-37d3-4ffc-b821-f6ed69a1e459",
    "status": "finished",
    "metrics": {
      "total": 272,
      "total_winning_trades": 141,
      "total_losing_trades": 131,
      "starting_balance": 10000,
      "finishing_balance": 18453.32651147767,
      "win_rate": 0.5183823529411765,
      "win_rate_longs": 0.4878048780487805,
      "win_rate_shorts": 0.531578947368421,
      "ratio_avg_win_loss": 1.4997396523057391,
      "longs_count": 82,
      "longs_percentage": 30.14705882352941,
      "shorts_percentage": 69.8529411764706,
      "shorts_count": 190,
      "fee": 1605.0213145971513,
      "net_profit": 8453.326511477682,
      "net_profit_percentage": 84.53326511477682,
      "average_win": 157.55991097943297,
      "average_loss": 105.05817508872039,
      "expectancy": 31.07840629219735,
      "expectancy_percentage": 0.3107840629219735,
      "expected_net_profit_every_100_trades": 31.078406292197354,
      "average_holding_period": 272477.64705882355,
      "average_winning_holding_period": 390171.06382978725,
      "average_losing_holding_period": 145800,
      "gross_profit": 22215.94744810005,
      "gross_loss": -13762.62093662237,
      "max_drawdown": -9.107769510949959,
      "max_underwater_period": 291,
      "annual_return": 12.469240955610793,
      "annualization": 365,
      "sharpe_ratio": 1.1967129796142293,
      "calmar_ratio": 1.3690773510044862,
      "sortino_ratio": 2.000959339184492,
      "omega_ratio": 1.3021453505969847,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -176.73251282212863,
      "largest_winning_trade": 1709.3757746029523,
      "current_streak": -3,
      "avg_trades_per_day": 0.14293216013744375,
      "avg_trades_per_week": 1.0005251209621062,
      "avg_trades_per_month": 4.350854954583788
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR207"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 76, \"delay_due\": 78, \"delay_occupied_or_pending\": 17, \"delay_original_priority\": 2, \"events\": 95, \"events_occupied\": 16, \"fills\": 76}, \"recipe\": \"V207\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 48, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 24, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 24, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR207\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  {
    "variant": "V207",
    "portfolio": "C",
    "id": "cfda043d-15dc-4443-9655-fbabf6fae45b",
    "url": "http://localhost:9200/#/backtest/cfda043d-15dc-4443-9655-fbabf6fae45b",
    "status": "finished",
    "metrics": {
      "total": 279,
      "total_winning_trades": 143,
      "total_losing_trades": 136,
      "starting_balance": 10000,
      "finishing_balance": 18588.878495063724,
      "win_rate": 0.5125448028673835,
      "win_rate_longs": 0.47191011235955055,
      "win_rate_shorts": 0.531578947368421,
      "ratio_avg_win_loss": 1.5253768029289747,
      "longs_count": 89,
      "longs_percentage": 31.899641577060933,
      "shorts_percentage": 68.10035842293907,
      "shorts_count": 190,
      "fee": 1687.1038493964206,
      "net_profit": 8588.878495063736,
      "net_profit_percentage": 85.88878495063736,
      "average_win": 159.52093307349637,
      "average_loss": 104.57805098857534,
      "expectancy": 30.78451073499545,
      "expectancy_percentage": 0.30784510734995446,
      "expected_net_profit_every_100_trades": 30.784510734995447,
      "average_holding_period": 284985.59139784944,
      "average_winning_holding_period": 409132.8671328671,
      "average_losing_holding_period": 154448.38235294117,
      "gross_profit": 22811.49342950998,
      "gross_loss": -14222.614934446246,
      "max_drawdown": -9.303970041493237,
      "max_underwater_period": 303,
      "annual_return": 12.627232440395009,
      "annualization": 365,
      "sharpe_ratio": 1.1899904103557868,
      "calmar_ratio": 1.3571875644569902,
      "sortino_ratio": 1.9691225985599197,
      "omega_ratio": 1.2931976554247437,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -95.00150000000212,
      "winning_streak": 7,
      "losing_streak": 5,
      "largest_losing_trade": -179.1325769458058,
      "largest_winning_trade": 1680.1833989455965,
      "current_streak": -4,
      "avg_trades_per_day": 0.1466105613174515,
      "avg_trades_per_week": 1.0262739292221605,
      "avg_trades_per_month": 4.462825486503224
    },
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "X03ValidR207"
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
    "hp": [
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
    "diagnostics": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 76, \"delay_due\": 78, \"delay_occupied_or_pending\": 17, \"delay_original_priority\": 2, \"events\": 95, \"events_occupied\": 16, \"fills\": 76}, \"recipe\": \"V207\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 48, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 23, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 23, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"X03ValidR207\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  }
]
```
