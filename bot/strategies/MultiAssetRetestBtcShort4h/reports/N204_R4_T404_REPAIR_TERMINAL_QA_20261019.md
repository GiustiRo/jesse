# T404 repaired pair terminal QA

Both technical retries finished with null errors. No further variants or runs. Raw sessions remain quarantined; C raw occupancy was economically contaminated. Source repair is exclusively the reviewed sub-lot guard in on_reduced_position. Failed fixture QA and corrected 41-check PASS are recorded in N204_R4_T404_DUST_REPAIR_QA_20261019.md. Synthetic QA did not establish engine flush; the C retry now establishes same execution timestamp empirically.

B http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333

C http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0

B net11712.87444845289 equals raw B; C net11877.886947496418,280trades. Both79supplement fills/closes,96events14occupied. BTC quota22B/21C, other capacity/risk/margin/zero-lot counters0. Root owns full MTM/fill/parity audit5d8dcd979f684680a2d250850251d039; no duplicate analysis.

C real dust/order evidence is complete in N204_R4_T404_REPAIR_C_REAL_QA_20261019.md. Third MARKET7e-18, TP2 and closed_at all1646405340000; actual following original STOP filled1646410260000. Full net change includes downstream shared-state effects and is not assigned to one trade alone.

```json
{
  "B": {
    "url": "http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333",
    "status": "finished",
    "error": null,
    "exception": null,
    "formUnchanged": true,
    "snapshots": [
      {
        "strategy": "N204ExitR404",
        "equalReviewed": true
      },
      {
        "strategy": "PortComparePaxgMarket4h",
        "equalReviewed": true
      },
      {
        "strategy": "PortCompareSpySecond4h",
        "equalReviewed": true
      }
    ],
    "metrics": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 21712.874448452865,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5294793637096438,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1853.5247628864831,
      "net_profit": 11712.87444845289,
      "net_profit_percentage": 117.12874448452891,
      "average_win": 186.02137146958833,
      "average_loss": 121.62398256777175,
      "expectancy": 42.90430200898492,
      "expectancy_percentage": 0.4290430200898492,
      "expected_net_profit_every_100_trades": 42.90430200898492,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 27159.120234559898,
      "gross_loss": -15446.245786107012,
      "max_drawdown": -8.785751847777611,
      "max_underwater_period": 292,
      "annual_return": 16.033447565475466,
      "annualization": 365,
      "sharpe_ratio": 1.5045324378771978,
      "calmar_ratio": 1.8249374490961963,
      "sortino_ratio": 2.600502693485516,
      "omega_ratio": 1.3940816941855112,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -207.97325248424482,
      "largest_winning_trade": 1994.812336585988,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "hyperparameters": {
      "action": "get_session_results",
      "status": "success",
      "session_type": "backtest",
      "session_id": "58c9d1be-26e6-4da5-b601-3d84128b3333",
      "session_status": "finished",
      "section": "hyperparameters",
      "items": [
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
      "offset": 0,
      "limit": 500,
      "returned": 8,
      "total": 8,
      "next_offset": null,
      "has_more": false,
      "truncated_by_size": false,
      "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
      "dashboard_url": "http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333"
    },
    "qaLogs": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 96, \"events_occupied\": 14, \"fills\": 79}, \"recipe\": \"T404\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 275, \"margin_limited\": 0, \"notional_or_weight_limited\": 22, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 22, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ExitR404\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  "C": {
    "url": "http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0",
    "status": "finished",
    "error": null,
    "exception": null,
    "formUnchanged": true,
    "snapshots": [
      {
        "strategy": "N204ExitR404",
        "equalReviewed": true
      },
      {
        "strategy": "PortComparePaxgMarket4h",
        "equalReviewed": true
      },
      {
        "strategy": "PortCompareSpyMarket4h",
        "equalReviewed": true
      }
    ],
    "metrics": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 21877.886947496456,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.554180996594301,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 1949.8314950966296,
      "net_profit": 11877.886947496418,
      "net_profit_percentage": 118.77886947496417,
      "average_win": 188.33518190842705,
      "average_loss": 121.17969677993015,
      "expectancy": 42.421024812487225,
      "expectancy_percentage": 0.42421024812487224,
      "expected_net_profit_every_100_trades": 42.421024812487225,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 27873.6069224472,
      "gross_loss": -15995.71997495078,
      "max_drawdown": -9.070557567484483,
      "max_underwater_period": 215,
      "annual_return": 16.202066793044743,
      "annualization": 365,
      "sharpe_ratio": 1.4914869510243944,
      "calmar_ratio": 1.7862261137203748,
      "sortino_ratio": 2.540209659557544,
      "omega_ratio": 1.380922885926227,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -111.80949999999939,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -210.86359098948074,
      "largest_winning_trade": 1959.1327663381085,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "hyperparameters": {
      "action": "get_session_results",
      "status": "success",
      "session_type": "backtest",
      "session_id": "ef7502ca-94d8-40ae-91fa-90df6d396fc0",
      "session_status": "finished",
      "section": "hyperparameters",
      "items": [
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
      "offset": 0,
      "limit": 500,
      "returned": 8,
      "total": 8,
      "next_offset": null,
      "has_more": false,
      "truncated_by_size": false,
      "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
      "dashboard_url": "http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0"
    },
    "qaLogs": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 96, \"events_occupied\": 14, \"fills\": 79}, \"recipe\": \"T404\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 275, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ExitR404\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2022-03-04T14:49:00] ==> N204_T404_DUST_SWEEP {\"price\": 40684.553584837355, \"qty\": 7e-18, \"reason\": \"sub_lot_after_reduction\", \"time\": 1646405340000}"
    ]
  }
}
```
