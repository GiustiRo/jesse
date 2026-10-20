# R6 capacity terminal journals — final

All ten family sessions finished with summary error null. Terminal counters from newest20 log entries per session, not full-log statistics. Veto counters include occupied contexts and do not equal avoided fills. R/G readiness does not imply affordable original orders. Releases are supplemental decisions, never synthetic original fills. P6017veto/66suppfills; P6020veto/67suppfills; P60313releases/67suppfills; P6044releases/67suppfills; P6050releases/67suppfills. Root confirmed exact economic parity P602/P605 toN503,264/271trades and economicfielddelta0. Absence of release does not identify which internal condition failed without further counters. No source change or extra rerun was used to fit these results.

- [P601B](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5)
- [P601C](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f)
- [P602B](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096)
- [P602C](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7)
- [P603B](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523)
- [P603C](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92)
- [P604B](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52)
- [P604C](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb)
- [P605B](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9)
- [P605C](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f)

```json
{
  "P601B": {
    "url": "http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_accepted\": 75, \"capacity_veto\": 7, \"closes\": 66, \"events\": 82, \"events_occupied\": 11, \"fills\": 66}, \"recipe\": \"P601\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR601\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P601C": {
    "url": "http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_accepted\": 75, \"capacity_veto\": 7, \"closes\": 66, \"events\": 82, \"events_occupied\": 11, \"fills\": 66}, \"recipe\": \"P601\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR601\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P602B": {
    "url": "http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_accepted\": 82, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P602\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR602\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P602C": {
    "url": "http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_accepted\": 82, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P602\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR602\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P603B": {
    "url": "http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_release\": 13, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P603\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 279, \"margin_limited\": 0, \"notional_or_weight_limited\": 23, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 23, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR603\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P603C": {
    "url": "http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_release\": 13, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P603\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 279, \"margin_limited\": 0, \"notional_or_weight_limited\": 22, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 22, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR603\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P604B": {
    "url": "http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_release\": 4, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P604\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 271, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR604\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P604C": {
    "url": "http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"capacity_release\": 4, \"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P604\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 271, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR604\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P605B": {
    "url": "http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P605\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR605\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  },
  "P605C": {
    "url": "http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f",
    "items": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"P605\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503CapacityR605\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "tailOnly": true
  }
}
```

## Final source/form readback
```json
[
  {
    "name": "P601B",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P601C",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P602B",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P602C",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P603B",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P603C",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P604B",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P604C",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P605B",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  },
  {
    "name": "P605C",
    "status": "finished",
    "form": true,
    "BTCsnapshot": true,
    "currentSource": true
  }
]
```