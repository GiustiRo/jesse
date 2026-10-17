from __future__ import annotations

import numpy as np

from jesse.modes.import_candles_mode.drivers.Binance.binance_utils import timeframe_to_interval
from jesse.services import candle_service
from jesse.store import store

from jesse_live.binance import BinanceFuturesClient


def klines_to_array(rows: list) -> np.ndarray:
    if not rows:
        return np.zeros((0, 6))
    return np.array(
        [
            [int(row[0]), float(row[1]), float(row[4]), float(row[2]), float(row[3]), float(row[5])]
            for row in rows
        ],
        dtype=np.float64,
    )


def closed_klines(client: BinanceFuturesClient, symbol: str, timeframe: str, limit: int = 500) -> np.ndarray:
    rows = client.klines(symbol, timeframe_to_interval(timeframe), limit=limit)
    candles = klines_to_array(rows)
    if len(candles) > 1:
        return candles[:-1]
    return candles


def inject_native_candles(exchange: str, symbol: str, timeframe: str, candles: np.ndarray) -> None:
    if candles is None or len(candles) == 0:
        return
    candle_service.batch_add_candle(candles, exchange, symbol, timeframe, with_generation=False)


def last_timestamp(exchange: str, symbol: str, timeframe: str) -> int | None:
    arr = store.candles.get_storage(exchange, symbol, timeframe)
    array, index = arr.snapshot()
    if index < 0:
        return None
    return int(array[index, 0])
