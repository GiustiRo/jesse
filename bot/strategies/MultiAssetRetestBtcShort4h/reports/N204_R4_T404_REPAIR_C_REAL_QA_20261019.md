# T404 C repaired real execution acceptance

PASS: technical dust repair closes at TP2 execution time; economic family selection remains with root. Raw C run is quarantined and superseded only by this reviewed repair.

http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0

Dust original trade opened1646280000000. TP2 and third MARKET dust fill7e-18 both executed1646405340000; closed_at1646405340000, not48h. Original STOP now actually fills1646410260000→1646432880000, PNL103.66831650981452. Total net improvement versus raw includes downstream state and is not asserted equal to this one trade. No price/threshold change.

```json
{
  "url": "http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0",
  "summary": {
    "action": "get_session_results",
    "status": "success",
    "session_type": "backtest",
    "session_id": "ef7502ca-94d8-40ae-91fa-90df6d396fc0",
    "session_status": "finished",
    "title": "MCP Backtest: N204 R4 T404 precision repair C",
    "description": "T404samefrozenpartial1R/2R prices;ONLYsub-lotremainingguard .001lot logs+sweepssamecallback. Rawquarantinedfornumericdustoccupation. MustproveactualtinyfillTP2sameclock/flat beforeaccepting.10k1%8%5x4.4fee.00045warm240debugtruefastfalse,2020-10-15→2025-12-31exclusive;2026closed. DRAFTONLYrootretryticketrequired.",
    "description_truncated": false,
    "created_at": 1792432386000,
    "updated_at": 1792432695000,
    "execution_duration": 174.34,
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N204ExitR404"
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
    "error": null,
    "has_chart_data": true,
    "has_charts_image": true,
    "sections": {
      "trades": {
        "count": 280
      },
      "equity_curve": {
        "series": [
          {
            "name": "Portfolio",
            "points": 1904
          }
        ]
      },
      "hyperparameters": {
        "count": 8
      },
      "logs": {
        "log_size_bytes": 1024986
      }
    },
    "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace.",
    "dashboard_url": "http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0"
  },
  "dustTrade": {
    "id": "01b6043c-8f95-4c58-bac3-925d212eafe5",
    "strategy_name": "N204ExitR404",
    "symbol": "BTC-USDT",
    "exchange": "Binance Perpetual Futures",
    "type": "short",
    "entry_price": 43312.7,
    "exit_price": 41341.59018862801,
    "qty": 0.08600000000000001,
    "opened_at": 1646280000000,
    "closed_at": 1646405340000,
    "fee": 3.276121030299904,
    "size": 3724.8922000000002,
    "PNL": 166.23932274769086,
    "PNL_percentage": 22.314648830332708,
    "holding_period": 125340,
    "orders": [
      {
        "id": "73a9e2eb-f2a2-480b-bfe9-532035c802a2",
        "trade_id": "01b6043c-8f95-4c58-bac3-925d212eafe5",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "sell",
        "type": "MARKET",
        "qty": -0.08600000000000001,
        "filled_qty": -0.08600000000000001,
        "price": 43312.7,
        "status": "EXECUTED",
        "created_at": 1646280000000,
        "canceled_at": null,
        "executed_at": 1646280000000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": false,
        "submitted_via": null,
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      },
      {
        "id": "066547e2-bc5d-4c26-a615-59b287a753e2",
        "trade_id": "01b6043c-8f95-4c58-bac3-925d212eafe5",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "buy",
        "type": "LIMIT",
        "qty": 0.043000000000000003,
        "filled_qty": 0.043000000000000003,
        "price": 41998.626792418676,
        "status": "EXECUTED",
        "created_at": 1646280000000,
        "canceled_at": null,
        "executed_at": 1646340300000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": true,
        "submitted_via": "take-profit",
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      },
      {
        "id": "79cb8147-be0b-4011-bcc6-91f6fbe1b26f",
        "trade_id": "01b6043c-8f95-4c58-bac3-925d212eafe5",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "buy",
        "type": "LIMIT",
        "qty": 0.043000000000000003,
        "filled_qty": 0.043000000000000003,
        "price": 40684.553584837355,
        "status": "EXECUTED",
        "created_at": 1646280000000,
        "canceled_at": null,
        "executed_at": 1646405340000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": true,
        "submitted_via": "take-profit",
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      },
      {
        "id": "568f056a-00fa-4dc4-ae70-8d74e327d4cf",
        "trade_id": "01b6043c-8f95-4c58-bac3-925d212eafe5",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "buy",
        "type": "MARKET",
        "qty": 7e-18,
        "filled_qty": 7e-18,
        "price": 40684.553584837355,
        "status": "EXECUTED",
        "created_at": 1646405340000,
        "canceled_at": null,
        "executed_at": 1646405340000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": true,
        "submitted_via": "take-profit",
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      }
    ]
  },
  "actualFollowingTrade": {
    "id": "24dbcd16-cceb-46db-8a8c-5bf52bccf862",
    "strategy_name": "N204ExitR404",
    "symbol": "BTC-USDT",
    "exchange": "Binance Perpetual Futures",
    "type": "short",
    "entry_price": 40426.867771282145,
    "exit_price": 38820.474398975006,
    "qty": 0.066,
    "opened_at": 1646410260000,
    "closed_at": 1646432880000,
    "fee": 2.3536460624566375,
    "size": 2668.1732729046216,
    "PNL": 103.66831650981452,
    "PNL_percentage": 19.426833624819146,
    "holding_period": 22620,
    "orders": [
      {
        "id": "fed4b0cf-f80e-4a99-92b0-db7f9cce8202",
        "trade_id": "24dbcd16-cceb-46db-8a8c-5bf52bccf862",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "sell",
        "type": "STOP",
        "qty": -0.066,
        "filled_qty": -0.066,
        "price": 40426.867771282145,
        "status": "EXECUTED",
        "created_at": 1646409600000,
        "canceled_at": null,
        "executed_at": 1646410260000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": false,
        "submitted_via": null,
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      },
      {
        "id": "e7cef2ac-3d36-4aa4-9c6e-2ccc1e8dec0b",
        "trade_id": "24dbcd16-cceb-46db-8a8c-5bf52bccf862",
        "session_id": null,
        "exchange_id": null,
        "symbol": "BTC-USDT",
        "side": "buy",
        "type": "LIMIT",
        "qty": 0.066,
        "filled_qty": 0.066,
        "price": 38820.474398975006,
        "status": "EXECUTED",
        "created_at": 1646410260000,
        "canceled_at": null,
        "executed_at": 1646432880000,
        "exchange": "Binance Perpetual Futures",
        "reduce_only": true,
        "submitted_via": "take-profit",
        "jesse_submitted": true,
        "order_exist_in_exchange": true,
        "updated_at": null,
        "session_mode": null
      }
    ]
  },
  "qaLogs": [
    "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 79, \"events\": 96, \"events_occupied\": 14, \"fills\": 79}, \"recipe\": \"T404\"}",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 275, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ExitR404\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}",
    "[INFO | 2022-03-04T14:49:00] ==> N204_T404_DUST_SWEEP {\"price\": 40684.553584837355, \"qty\": 7e-18, \"reason\": \"sub_lot_after_reduction\", \"time\": 1646405340000}"
  ],
  "dustLogExcerpt": [
    "[INFO | 2022-03-03T04:00:00] 📤 Order submitted | BTC-USDT | Binance Perpetual Futures | BUY LIMIT | Qty: 0.043000000000000003 | Price: 40684.55",
    "[INFO | 2022-03-03T20:45:00] ✅ Order executed | BTC-USDT | Binance Perpetual Futures | BUY LIMIT | Qty: 0.043000000000000003 | Price: 41998.62",
    "[INFO | 2022-03-03T20:45:00] Charged 0.81 as fee. Balance for USDT on Binance Perpetual Futures changed from 12133.03 to 12132.22",
    "[INFO | 2022-03-03T20:45:00] Added realized PNL of 56.51. Balance for USDT on Binance Perpetual Futures changed from 12132.22 to 12188.72",
    "[INFO | 2022-03-03T20:45:00] ➖ Position reduced | BTC-USDT | Binance Perpetual Futures | Qty: -0.04300000000000001",
    "[INFO | 2022-03-03T20:45:00] 🚫 Order canceled | BTC-USDT | Binance Perpetual Futures | BUY STOP | Qty: 0.08600000000000001 | Price: 44626.77",
    "[INFO | 2022-03-03T20:45:00] 📤 Order submitted | BTC-USDT | Binance Perpetual Futures | BUY STOP | Qty: 0.04300000000000001 | Price: 44626.77",
    "[INFO | 2022-03-04T00:01:00] Saved daily portfolio balance: 12227.38",
    "[INFO | 2022-03-04T14:49:00] ✅ Order executed | BTC-USDT | Binance Perpetual Futures | BUY LIMIT | Qty: 0.043000000000000003 | Price: 40684.55",
    "[INFO | 2022-03-04T14:49:00] Charged 0.79 as fee. Balance for USDT on Binance Perpetual Futures changed from 12188.72 to 12187.93",
    "[INFO | 2022-03-04T14:49:00] Added realized PNL of 113.01. Balance for USDT on Binance Perpetual Futures changed from 12187.93 to 12300.94",
    "[INFO | 2022-03-04T14:49:00] ➖ Position reduced | BTC-USDT | Binance Perpetual Futures | Qty: -7e-18",
    "[INFO | 2022-03-04T14:49:00] ==> N204_T404_DUST_SWEEP {\"price\": 40684.553584837355, \"qty\": 7e-18, \"reason\": \"sub_lot_after_reduction\", \"time\": 1646405340000}",
    "[INFO | 2022-03-04T14:49:00] 📤 Order submitted | BTC-USDT | Binance Perpetual Futures | BUY MARKET | Qty: 7e-18 | Price: 40684.55",
    "[INFO | 2022-03-04T14:49:00] ✅ Order executed | BTC-USDT | Binance Perpetual Futures | BUY MARKET | Qty: 7e-18 | Price: 40684.55",
    "[INFO | 2022-03-04T14:49:00] Charged 0.0 as fee. Balance for USDT on Binance Perpetual Futures changed from 12300.94 to 12300.94",
    "[INFO | 2022-03-04T14:49:00] Added realized PNL of 0.0. Balance for USDT on Binance Perpetual Futures changed from 12300.94 to 12300.94",
    "[INFO | 2022-03-04T14:49:00] 🟢 Trade closed | BTC-USDT | SHORT | Binance Perpetual Futures",
    "Qty: 0.08600000000000001 | Entry: 43312.69 | Exit: 41341.59",
    "Net PnL: +166.24 USDT (+22.31%) | Fees: 3.27 USDT",
    "[INFO | 2022-03-04T14:49:00] 🏁 Position closed | BTC-USDT | Binance Perpetual Futures",
    "[INFO | 2022-03-04T14:49:00] cancel all remaining orders of BTC-USDT to prepare for a fresh start...",
    "[INFO | 2022-03-04T14:49:00] 🚫 Order canceled | BTC-USDT | Binance Perpetual Futures | BUY STOP | Qty: 0.04300000000000001 | Price: 44626.77",
    "[INFO | 2022-03-04T16:00:00] 📤 Order submitted | BTC-USDT | Binance Perpetual Futures | SELL STOP | Qty: 0.066 | Price: 40426.86",
    "[INFO | 2022-03-04T16:11:00] ✅ Order executed | BTC-USDT | Binance Perpetual Futures | SELL STOP | Qty: 0.066 | Price: 40426.86",
    "[INFO | 2022-03-04T16:11:00] Charged 1.2 as fee. Balance for USDT on Binance Perpetual Futures changed from 12300.94 to 12299.74"
  ]
}
```
