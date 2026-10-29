"""Resolve July M1 source conflicts against HistData's own BID tick archive.

No database writes. A repair is accepted only if every unambiguous M1 bar has
the same OHLC as aggregation of the vendor ticks; no arbitrary duplicate wins.
"""
import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
import pandas as pd
import jesse.models
from jesse import helpers as jh

ROOT = Path(__file__).resolve().parent / "data" / "histdata"


def read_csv_zip(path, **kwargs):
    with zipfile.ZipFile(path) as z:
        names = [name for name in z.namelist() if name.lower().endswith(".csv")]
        if len(names) != 1 or z.testzip() is not None:
            raise ValueError("Invalid source ZIP")
        with z.open(names[0]) as fh:
            return pd.read_csv(fh, **kwargs)


def main():
    ticks = read_csv_zip(ROOT / "SPXUSD_T_202607.zip", header=None,
                         names=["local_time", "bid", "ask", "volume"])
    local = pd.to_datetime(ticks.pop("local_time"), format="%Y%m%d %H%M%S%f", errors="raise")
    ticks["time"] = local.dt.tz_localize("Etc/GMT+5").dt.tz_convert("UTC")
    backwards = int((ticks["time"].diff().dt.total_seconds() < 0).sum())
    # Stable time sorting retains vendor order among equal-time observations.
    ticks = ticks.sort_values("time", kind="stable")
    if not np.isfinite(ticks["bid"].to_numpy()).all() or (ticks["bid"] <= 0).any():
        raise ValueError("Invalid BID ticks")
    ticks["timestamp"] = ticks["time"].astype("int64") // 60000000000 * 60000
    bars = ticks.groupby("timestamp")["bid"].agg(["first", "max", "min", "last"]).rename(
        columns={"first": "open", "max": "high", "min": "low", "last": "close"}) / 10
    bars["volume"] = 0.0
    source = read_csv_zip(ROOT / "SPXUSD_M1_202607.zip", sep=";", header=None,
                         names=["local_time", "open", "high", "low", "close", "volume"])
    dates = pd.to_datetime(source.pop("local_time"), format="%Y%m%d %H%M%S", errors="raise")
    source["timestamp"] = dates.dt.tz_localize("Etc/GMT+5").dt.tz_convert("UTC").astype("int64") // 1000000
    columns = ["open", "high", "low", "close"]
    source[columns] /= 10.0
    ambiguous = source["timestamp"].duplicated(keep=False)
    conflicts = sorted(int(t) for t in source.loc[ambiguous, "timestamp"].unique())
    clean = source.loc[~ambiguous].set_index("timestamp")
    common = clean.index.intersection(bars.index)
    missing = clean.index.difference(bars.index)
    mismatch = ~np.isclose(clean.loc[common, columns].to_numpy(),
                           bars.loc[common, columns].to_numpy(), rtol=0, atol=1e-8).all(axis=1)
    report = {"tick_rows": len(ticks), "tick_backwards_observations": backwards,
              "unambiguous_m1_rows": len(clean), "missing_tick_minutes": len(missing),
              "mismatched_unambiguous_minutes": int(mismatch.sum()), "conflict_minutes": conflicts,
              "mismatch_samples": [int(t) for t in common[mismatch][:10]],
              "reconstructed_conflicts": bars.loc[conflicts].reset_index().to_dict("records"),
              "tick_zip_sha256": hashlib.sha256((ROOT / "SPXUSD_T_202607.zip").read_bytes()).hexdigest()}
    (ROOT / "SPXUSD_202607_tick_audit.json").write_text(json.dumps(report, indent=2))
    jh.debug(report)
    if len(missing) or mismatch.any() or len(conflicts) != 6:
        raise ValueError("Tick archive did not exactly validate the unambiguous M1 bars")
    repaired = pd.concat([clean, bars.loc[conflicts]]).sort_index()
    if repaired.index.duplicated().any():
        raise ValueError("Repair did not produce unique minute bars")
    repaired.reset_index()[["timestamp", "open", "high", "low", "close", "volume"]].to_csv(
        ROOT / "SPXUSD_202607_tick_verified.csv", index=False, float_format="%.6f")
    jh.debug({"status": "six source conflicts resolved from vendor BID ticks", "rows": len(repaired)})


if __name__ == "__main__":
    main()
