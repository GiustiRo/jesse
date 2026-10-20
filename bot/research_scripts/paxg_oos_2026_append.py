"""Append missing 2026 PAXG Spot candles to the existing research futures proxy.

The historical proxy is already Binance Spot. Require exact overlapping OHLCV
and a complete minute clock before storing only missing rows through Oct 18.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import jesse.models
from jesse import helpers as jh
from jesse import research
from jesse.models.Candle import Candle

START = 1767225600000
FINISH = 1792368000000
SYMBOL = "PAXG-USDT"
SOURCE = "Binance Spot"
TARGET = "Binance Perpetual Futures"
COLUMNS = ["timestamp", "open", "close", "high", "low", "volume"]


def read(exchange):
    query = (Candle.select(Candle.timestamp, Candle.open, Candle.close, Candle.high, Candle.low, Candle.volume)
             .where((Candle.exchange == exchange) & (Candle.symbol == SYMBOL) & (Candle.timeframe == "1m")
                    & (Candle.timestamp >= START) & (Candle.timestamp < FINISH))
             .order_by(Candle.timestamp).dicts())
    return pd.DataFrame(list(query), columns=COLUMNS)


def main():
    source, target = read(SOURCE), read(TARGET)
    expected = np.arange(START, FINISH, 60000, dtype=np.int64)
    if len(source) != len(expected) or not np.array_equal(source["timestamp"].to_numpy(), expected):
        raise ValueError("Source PAXG minute clock is not complete for the frozen OOS window")
    if not np.isfinite(source[COLUMNS].to_numpy(dtype=float)).all():
        raise ValueError("Non-finite source data")
    if (source[["open", "close", "high", "low"]] <= 0).any().any() or (source["volume"] < 0).any():
        raise ValueError("Invalid source prices or volumes")
    if ((source["high"] < source[["open", "close", "low"]].max(axis=1)).any()
            or (source["low"] > source[["open", "close", "high"]].min(axis=1)).any()):
        raise ValueError("Invalid source OHLC")
    indexed = source.set_index("timestamp")
    original = target.set_index("timestamp")
    if len(target) and (not original.index.isin(indexed.index).all() or not np.allclose(
            original[COLUMNS[1:]].to_numpy(dtype=float),
            indexed.loc[original.index, COLUMNS[1:]].to_numpy(dtype=float), rtol=0, atol=1e-8)):
        raise ValueError("Existing PAXG proxy does not exactly match Spot on the overlap")
    predicate = (Candle.exchange == TARGET) & (Candle.symbol == SYMBOL) & (Candle.timeframe == "1m") & (Candle.timestamp < START)
    historical_before = Candle.select().where(predicate).count()
    missing = source.loc[~source["timestamp"].isin(target["timestamp"]), COLUMNS].to_numpy(dtype=float)
    jh.debug({"source_rows": len(source), "overlap_verified": len(target), "new_rows": len(missing)})
    if len(missing):
        if len(missing) < 2 or missing[1, 0] - missing[0, 0] != 60000:
            raise ValueError("Missing rows do not begin with consecutive real source minutes")
        research.store_candles(missing, TARGET, SYMBOL)
    after = read(TARGET)
    if len(after) != len(source) or not np.allclose(after[COLUMNS].to_numpy(dtype=float),
                                                  source[COLUMNS].to_numpy(dtype=float), rtol=0, atol=1e-8):
        raise ValueError("Post-import target is not identical to the source")
    if Candle.select().where(predicate).count() != historical_before:
        raise ValueError("Historical row count changed")
    report = {"source": SOURCE, "target": TARGET, "symbol": SYMBOL, "start_inclusive": "2026-01-01",
              "finish_exclusive": "2026-10-19", "source_rows": len(source), "overlap_verified": len(target),
              "added_rows": len(missing), "historical_rows_unchanged": historical_before,
              "first_utc": pd.Timestamp(int(source["timestamp"].iloc[0]), unit="ms", tz="UTC").isoformat(),
              "last_utc": pd.Timestamp(int(source["timestamp"].iloc[-1]), unit="ms", tz="UTC").isoformat(),
              "status": "complete_minute_clock_and_exact_same_source_parity"}
    Path("research_scripts/data/histdata/PAXG_2026_patch_manifest.json").write_text(json.dumps(report, indent=2))
    jh.debug(report)


if __name__ == "__main__":
    main()
