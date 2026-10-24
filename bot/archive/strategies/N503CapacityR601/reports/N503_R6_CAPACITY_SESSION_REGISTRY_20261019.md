# R6 capacity frozen sessions — final

Ten nominal full backtests, five hypotheses, all finished with summary error null. No repairs, retries or extra fulls. Each B/C pair launched simultaneously only after explicit root ticket; maximum four global runs. Source QA311PASS. All forms/30snapshotsprechecked; all10forms/BTCsnapshots/fivecurrent sources confirmed unchanged after execution. Frozen protocol: strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FROZEN_PROTOCOL_20261019.md. 2026closed.

- [P601B](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5): `N503CapacityR601`, finished
- [P601C](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f): `N503CapacityR601`, finished
- [P602B](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096): `N503CapacityR602`, finished
- [P602C](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7): `N503CapacityR602`, finished
- [P603B](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523): `N503CapacityR603`, finished
- [P603C](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92): `N503CapacityR603`, finished
- [P604B](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52): `N503CapacityR604`, finished
- [P604C](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb): `N503CapacityR604`, finished
- [P605B](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9): `N503CapacityR605`, finished
- [P605C](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f): `N503CapacityR605`, finished

```json
[
  {
    "name": "P601B",
    "strategy": "N503CapacityR601",
    "portfolio": "B",
    "id": "7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5",
    "url": "http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR601"
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
    "status": "finished"
  },
  {
    "name": "P601C",
    "strategy": "N503CapacityR601",
    "portfolio": "C",
    "id": "4c23dbbc-ea56-4709-9835-e2e2b332214f",
    "url": "http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR601"
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
    "status": "finished"
  },
  {
    "name": "P602B",
    "strategy": "N503CapacityR602",
    "portfolio": "B",
    "id": "35c8f77f-e7fa-4c12-b9cc-8a6141192096",
    "url": "http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR602"
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
    "status": "finished"
  },
  {
    "name": "P602C",
    "strategy": "N503CapacityR602",
    "portfolio": "C",
    "id": "7df75aa0-a2c1-456e-b196-d96a9d00c3c7",
    "url": "http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR602"
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
    "status": "finished"
  },
  {
    "name": "P603B",
    "strategy": "N503CapacityR603",
    "portfolio": "B",
    "id": "b667d009-bcec-425f-8120-ac7fd24ea523",
    "url": "http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR603"
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
    "status": "finished"
  },
  {
    "name": "P603C",
    "strategy": "N503CapacityR603",
    "portfolio": "C",
    "id": "60c0e24b-cd8e-42e0-be3c-b915104fab92",
    "url": "http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR603"
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
    "status": "finished"
  },
  {
    "name": "P604B",
    "strategy": "N503CapacityR604",
    "portfolio": "B",
    "id": "bf8cf6df-8055-4e88-a52d-5cb3d12d8b52",
    "url": "http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR604"
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
    "status": "finished"
  },
  {
    "name": "P604C",
    "strategy": "N503CapacityR604",
    "portfolio": "C",
    "id": "e312a439-4afb-4be4-af3b-4d08325d47bb",
    "url": "http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR604"
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
    "status": "finished"
  },
  {
    "name": "P605B",
    "strategy": "N503CapacityR605",
    "portfolio": "B",
    "id": "49c13ad1-4802-4c9f-99f8-fffec43fdac9",
    "url": "http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR605"
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
    "status": "finished"
  },
  {
    "name": "P605C",
    "strategy": "N503CapacityR605",
    "portfolio": "C",
    "id": "12d3aae7-b298-4afc-aa6a-e46f6fc24a2f",
    "url": "http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f",
    "form": {
      "exchange": "Binance Perpetual Futures",
      "routes": [
        {
          "exchange": "Binance Perpetual Futures",
          "symbol": "BTC-USDT",
          "timeframe": "4h",
          "strategy": "N503CapacityR605"
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
    "status": "finished"
  }
]
```