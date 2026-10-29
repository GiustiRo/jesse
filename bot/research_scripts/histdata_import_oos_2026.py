"""Import authorized SPX 2026 data after validating the same-source tick repair.

Uses Jesse's research.store_candles; never replaces historical rows or mixes
native Binance SPY data. No strategy parameters, settings, or live sessions change.
"""
import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
import pandas as pd
import jesse.models
from jesse import helpers as jh
from jesse import research
from jesse.models.Candle import Candle

ROOT = Path(__file__).resolve().parent / "data" / "histdata"
START = 1767225600000
FINISH = 1792368000000
EXCHANGE = "Binance Perpetual Futures"
SYMBOL = "SPY-USDT"


def main():
    assert pd.Timestamp(START, unit="ms", tz="UTC") == pd.Timestamp("2026-01-01", tz="UTC")
    assert pd.Timestamp(FINISH, unit="ms", tz="UTC") == pd.Timestamp("2026-10-19", tz="UTC")
    audit = json.loads((ROOT / "SPXUSD_202607_tick_audit.json").read_text())
    if audit["missing_tick_minutes"] or audit["mismatched_unambiguous_minutes"] or len(audit["conflict_minutes"]) != 6:
        raise ValueError("July source repair has not passed the tick audit")
    if hashlib.sha256((ROOT / "SPXUSD_T_202607.zip").read_bytes()).hexdigest() != audit["tick_zip_sha256"]:
        raise ValueError("Tick archive changed since its audit")
    frames, archives = [], []
    for period in range(202601, 202611):
        path = ROOT / f"SPXUSD_M1_{period}.zip"
        if period == 202607:
            frame = pd.read_csv(ROOT / "SPXUSD_202607_tick_verified.csv")
        else:
            with zipfile.ZipFile(path) as z:
                names = [name for name in z.namelist() if name.lower().endswith(".csv")]
                if len(names) != 1 or z.testzip() is not None:
                    raise ValueError("Invalid vendor archive")
                with z.open(names[0]) as fh:
                    frame = pd.read_csv(fh, sep=";", header=None,
                                        names=["local_time", "open", "high", "low", "close", "volume"])
            local = pd.to_datetime(frame.pop("local_time"), format="%Y%m%d %H%M%S", errors="raise")
            frame.insert(0, "timestamp", local.dt.tz_localize("Etc/GMT+5").dt.tz_convert("UTC").astype("int64") // 1000000)
            frame[["open", "high", "low", "close"]] /= 10
        frame = frame.loc[(frame["timestamp"] >= START) & (frame["timestamp"] < FINISH)].copy()
        frame = frame.drop_duplicates().sort_values("timestamp", kind="stable")
        if frame.empty or frame["timestamp"].duplicated().any():
            raise ValueError(f"Empty or conflicting archive {period}")
        archives.append({"period": period, "rows": len(frame),
                         "zip_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        frames.append(frame)
    combined = pd.concat(frames, ignore_index=True)
    if (np.diff(combined["timestamp"]) <= 0).any() or (combined["timestamp"] % 60000 != 0).any():
        raise ValueError("Overlapping or non-minute source data")
    columns = ["timestamp", "open", "close", "high", "low", "volume"]
    values = combined[columns].to_numpy(dtype=float)
    if not np.isfinite(values).all() or (combined[["open", "close", "high", "low"]] <= 0).any().any():
        raise ValueError("Invalid source prices")
    if ((combined["high"] < combined[["open", "close", "low"]].max(axis=1)).any()
            or (combined["low"] > combined[["open", "close", "high"]].min(axis=1)).any()
            or (combined["volume"] != 0).any()):
        raise ValueError("Invalid OHLC/volume semantics")
    base = (Candle.exchange == EXCHANGE) & (Candle.symbol == SYMBOL) & (Candle.timeframe == "1m")
    historical = Candle.select().where(base & (Candle.timestamp < START)).count()
    existing = list(Candle.select(Candle.timestamp, Candle.open, Candle.close, Candle.high, Candle.low, Candle.volume)
                    .where(base & (Candle.timestamp >= START) & (Candle.timestamp < FINISH)).dicts())
    indexed = combined.set_index("timestamp")
    for row in existing:
        timestamp = row["timestamp"]
        if timestamp not in indexed.index or not np.allclose(
                indexed.loc[timestamp, ["open", "close", "high", "low", "volume"]].to_numpy(dtype=float),
                [row[key] for key in columns[1:]], rtol=0, atol=1e-8):
            raise ValueError("Existing 2026 target data conflicts with validated HistData source")
    existing_times = {row["timestamp"] for row in existing}
    new = combined.loc[~combined["timestamp"].isin(existing_times), columns].to_numpy(dtype=float)
    if len(new):
        # The API validates its first pair; use the actual consecutive source minutes.
        if len(new) < 2 or new[1, 0] - new[0, 0] != 60000:
            raise ValueError("The remaining source does not begin with two consecutive real minutes")
        research.store_candles(new, EXCHANGE, SYMBOL)
    after = Candle.select().where(base & (Candle.timestamp >= START) & (Candle.timestamp < FINISH)).count()
    if after != len(combined) or Candle.select().where(base & (Candle.timestamp < START)).count() != historical:
        raise ValueError("Post-import counts did not reconcile")
    dates = pd.to_datetime(combined["timestamp"], unit="ms", utc=True)
    output = ROOT / "SPXUSD_div10_1m_2026_OOS_20261019.csv"
    combined[["timestamp", "open", "high", "low", "close", "volume"]].to_csv(output, index=False, float_format="%.6f")
    manifest = {"source": "HistData SPX/USD M1 BID /10, EST fixed UTC-5",
                "start_inclusive": "2026-01-01", "finish_exclusive": "2026-10-19",
                "rows": len(combined), "new_rows": len(new), "existing_rows_retained": len(existing),
                "historical_rows_unchanged": historical, "first_utc": dates.iloc[0].isoformat(),
                "last_utc": dates.iloc[-1].isoformat(), "archives": archives,
                "tick_repair": audit, "csv_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "monthly_rows": combined.groupby(dates.dt.strftime("%Y-%m")).size().to_dict(),
                "status": "imported_same_source; original gaps retained; engine coverage check pending"}
    output.with_suffix(".csv.manifest.json").write_text(json.dumps(manifest, indent=2))
    jh.debug(manifest)


if __name__ == "__main__":
    main()
