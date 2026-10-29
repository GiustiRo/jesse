# R8 experimental draft registry

All10drafts, no run yet. Config10000/.00045isolated5x,warm240/debugtrue/fastfalse/charttrue. BTC/PAXG/SPY4h and3M1feeds; SL1RTP2R48h;2026closed.

## X801B

Dashboard: http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f

Session: f660ef63-d7c6-4792-9f21-06c1d7ebd85f

```json
{
  "name": "X801B",
  "id": "f660ef63-d7c6-4792-9f21-06c1d7ebd85f",
  "url": "http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f",
  "strategy": "BTCExploreR801",
  "portfolio": "B",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR801"
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
  "verified": true
}
```

## X801C

Dashboard: http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660

Session: 4e432aac-71c2-4023-a978-6d8a618aa660

```json
{
  "name": "X801C",
  "id": "4e432aac-71c2-4023-a978-6d8a618aa660",
  "url": "http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660",
  "strategy": "BTCExploreR801",
  "portfolio": "C",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR801"
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
  "verified": true
}
```

## X802B

Dashboard: http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3

Session: 261696a9-33ee-4504-a310-b8a44c63dcd3

```json
{
  "name": "X802B",
  "id": "261696a9-33ee-4504-a310-b8a44c63dcd3",
  "url": "http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3",
  "strategy": "BTCExploreR802",
  "portfolio": "B",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR802"
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
  "verified": true
}
```

## X802C

Dashboard: http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e

Session: 07a45656-81e2-4fd8-9851-3aa16a782c2e

```json
{
  "name": "X802C",
  "id": "07a45656-81e2-4fd8-9851-3aa16a782c2e",
  "url": "http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e",
  "strategy": "BTCExploreR802",
  "portfolio": "C",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR802"
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
  "verified": true
}
```

## X803B

Dashboard: http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf

Session: 5208fe79-c420-4328-b5dd-1a67177f1ccf

```json
{
  "name": "X803B",
  "id": "5208fe79-c420-4328-b5dd-1a67177f1ccf",
  "url": "http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf",
  "strategy": "BTCExploreR803",
  "portfolio": "B",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR803"
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
  "verified": true
}
```

## X803C

Dashboard: http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757

Session: a86de192-2f0d-4b34-a4ae-ce4f686d4757

```json
{
  "name": "X803C",
  "id": "a86de192-2f0d-4b34-a4ae-ce4f686d4757",
  "url": "http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757",
  "strategy": "BTCExploreR803",
  "portfolio": "C",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR803"
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
  "verified": true
}
```

## X804B

Dashboard: http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9

Session: ed50a692-6ce7-4014-baea-eb7b6b5acad9

```json
{
  "name": "X804B",
  "id": "ed50a692-6ce7-4014-baea-eb7b6b5acad9",
  "url": "http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9",
  "strategy": "BTCExploreR804",
  "portfolio": "B",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR804"
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
  "verified": true
}
```

## X804C

Dashboard: http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d

Session: 09421154-a313-480c-9ab0-6c28cdcf810d

```json
{
  "name": "X804C",
  "id": "09421154-a313-480c-9ab0-6c28cdcf810d",
  "url": "http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d",
  "strategy": "BTCExploreR804",
  "portfolio": "C",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR804"
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
  "verified": true
}
```

## X805B

Dashboard: http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8

Session: 22b632fe-7fa2-450a-9f34-47c6e13efec8

```json
{
  "name": "X805B",
  "id": "22b632fe-7fa2-450a-9f34-47c6e13efec8",
  "url": "http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8",
  "strategy": "BTCExploreR805",
  "portfolio": "B",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR805"
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
  "verified": true
}
```

## X805C

Dashboard: http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41

Session: 69c41479-2763-4150-ad60-68e1fd605b41

```json
{
  "name": "X805C",
  "id": "69c41479-2763-4150-ad60-68e1fd605b41",
  "url": "http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41",
  "strategy": "BTCExploreR805",
  "portfolio": "C",
  "form": {
    "exchange": "Binance Perpetual Futures",
    "routes": [
      {
        "exchange": "Binance Perpetual Futures",
        "symbol": "BTC-USDT",
        "timeframe": "4h",
        "strategy": "BTCExploreR805"
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
  "verified": true
}
```