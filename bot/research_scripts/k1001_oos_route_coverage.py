"""Audit the observed 2026 route data before accepting OOS metrics.

Read-only candle-quality checks; no backtest, settings, or strategy changes.
Missing tails and frozen data must be reported even if the engine finishes.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import jesse.models
from jesse import helpers as jh
from jesse.models.Candle import Candle

START = 1767225600000
FINISH = 1792368000000


def main():
    report = []
    for symbol in ["BTC-USDT", "PAXG-USDT", "SPY-USDT"]:
        query = (Candle.select(Candle.timestamp, Candle.open, Candle.close, Candle.high, Candle.low, Candle.volume)
                 .where((Candle.exchange == "Binance Perpetual Futures") & (Candle.symbol == symbol)
                        & (Candle.timeframe == "1m") & (Candle.timestamp >= START) & (Candle.timestamp < FINISH))
                 .order_by(Candle.timestamp).dicts())
        df = pd.DataFrame(list(query))
        if df.empty:
            report.append({"symbol": symbol, "rows": 0})
            continue
        dates = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
        df["month"] = dates.dt.strftime("%Y-%m")
        months = []
        for month, group in df.groupby("month"):
            months.append({"month": month, "rows": len(group), "distinct_closes": int(group["close"].nunique()),
                           "min_low": float(group["low"].min()), "max_high": float(group["high"].max()),
                           "first_utc": pd.Timestamp(int(group["timestamp"].iloc[0]), unit="ms", tz="UTC").isoformat(),
                           "last_utc": pd.Timestamp(int(group["timestamp"].iloc[-1]), unit="ms", tz="UTC").isoformat()})
        report.append({"symbol": symbol, "rows": len(df), "first_utc": dates.iloc[0].isoformat(),
                       "last_utc": dates.iloc[-1].isoformat(), "monthly": months,
                       "gaps_over_one_minute": int((np.diff(df["timestamp"]) > 60000).sum()),
                       "largest_gap_minutes": float(np.diff(df["timestamp"]).max() / 60000)})
    path = Path("research_scripts/data/histdata/K1001_2026_all_route_coverage.json")
    path.write_text(json.dumps(report, indent=2))
    jh.debug(report)


if __name__ == "__main__":
    main()
