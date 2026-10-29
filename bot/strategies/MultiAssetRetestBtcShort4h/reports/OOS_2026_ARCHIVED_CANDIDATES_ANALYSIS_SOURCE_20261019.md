# Comparación ampliada2026 — análisis reproducible

Cuatro grupos máximo8snapshots porjob, secuenciales: nominalN204/N503/P604+K1001; nominalC504/K1005+N204/K1001; estrésN204/N503/P604+K1001; estrésC504/K1005+N204/K1001. Referencias repetidas en análisis no son corridas adicionales ni muestras independientes. Sólo sesionesK1001definitivas conPAXGcompleto.

Puertas congeladas; identidad económica descriptiva porhashsinUUID a8decimales, no equivalenciauniversal. Resta mejortrade es aritmética sobre recorridosfijos, no backtestsintrade. Meses/Qdeequity, octubre/Q4parciales. Se reconcilian cantidades ejecutadas portrade; campos raw de posiciónabierta pueden ser preliquidaciónfrontera y no se interpretan como exposiciónfinal.

```python
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

# Initialize Jesse models before helpers in a standalone analysis process.
import jesse.models
from jesse import helpers as jh

out = Path("output")
out.mkdir(exist_ok=True)
strategies = {"K1001": "CapitalR12K1001R2A6", "N204": "CapitalR12N204R2A6",
              "N503": "OosN503R2A6", "P604": "OosP604R2A6",
              "C504": "OosC504R2A6", "K1005": "OosK1005R2A6"}
data = {p.stem: json.loads(p.read_text()) for p in Path("inputs").glob("*.json") if p.name != "manifest.json"}
rows, monthly, quarterly, signatures = [], [], [], {}

def entry_key(t):
    return (t["symbol"], t["type"], int(t["opened_at"]), round(float(t["entry_price"]), 8))

for label, d in sorted(data.items()):
    candidate, portfolio, cost = label.split("_")
    summary, m = d["summary"], d["metrics"]
    f = summary["form"]
    assert summary["session_status"] == "finished"
    assert f["start_date"] == "2026-01-01" and f["finish_date"] == "2026-10-19"
    ex = f["config"]["exchange"]
    assert ex["balance"] == 10000 and ex["futures_leverage"] == 3 and ex["futures_leverage_mode"] == "isolated"
    assert ex["fee"] == (.00045 if cost == "N" else .00095)
    assert f["config"]["warm_up_candles"] == 240 and not f["fast_mode"] and f["debug_mode"]
    assert [r["strategy"] for r in f["routes"]] == [strategies[candidate], "CapitalR12PaxgR2A6", "CapitalR12Spy" + portfolio + "R2A6"]
    trades = d["trades"]
    net = math.fsum(float(t["PNL"]) for t in trades)
    fees = math.fsum(float(t["fee"]) for t in trades)
    wins = math.fsum(max(0, float(t["PNL"])) for t in trades)
    losses = -math.fsum(min(0, float(t["PNL"])) for t in trades)
    pf = wins / losses if losses else None
    # One cent is the accounting reconciliation tolerance used in prior audits.
    assert abs(net - float(m["net_profit"])) < .01
    assert abs(10000 + net - float(m["finishing_balance"])) < .01
    assert len(trades) == m["total"]
    series = next(s for s in d["equity_curve"] if s["name"] == "Portfolio")
    curve = pd.DataFrame(series["data"]).sort_values("time").drop_duplicates("time", keep="last")
    curve["date"] = pd.to_datetime(curve["time"], unit="s", utc=True)
    s = curve.set_index("date")["value"].astype(float)
    peak = s.cummax()
    usd = peak - s
    gap = float(s.iloc[-1]) - float(m["finishing_balance"])
    assert abs(gap) < .01
    assert all(int(t["closed_at"]) <= 1792368000000 and int(t["closed_at"]) >= int(t["opened_at"]) for t in trades)
    # Engine open-position metrics may precede forced boundary liquidation.
    # Reconcile the executed entry/exit quantities on each recorded closed trade.
    for trade in trades:
        executed = [o for o in trade["orders"] if o["status"] == "EXECUTED"]
        signed_qty = math.fsum((1 if o["side"].lower() == "buy" else -1) * abs(float(o["filled_qty"])) for o in executed)
        assert abs(signed_qty) < 1e-7
    by = {}
    for t in trades:
        a = by.setdefault(t["symbol"], {"net": 0.0, "fees": 0.0, "trades": 0})
        a["net"] += float(t["PNL"])
        a["fees"] += float(t["fee"])
        a["trades"] += 1
    gates = {"positive_net": net > 0, "pf_ge_1_2": pf is not None and pf >= 1.2,
             "dd_ge_minus25": float(m["max_drawdown"]) >= -25, "trades_ge_20": len(trades) >= 20}
    tm = {entry_key(t): t for t in trades}
    assert len(tm) == len(trades)
    signatures[label] = tm
    # Hash excludes random database UUIDs; eight decimals expose economic identities
    # at a precision much finer than the one-cent accounting reconciliation.
    economic = sorted((t["symbol"], t["type"], int(t["opened_at"]), int(t["closed_at"]),
                       *[round(float(t[k]), 8) for k in ["entry_price", "exit_price", "qty", "fee", "PNL"]]) for t in trades)
    row = {"case": label, "candidate": candidate, "portfolio": portfolio, "cost": cost,
           "net": net, "balance": m["finishing_balance"], "return_pct": m["net_profit_percentage"],
           "dd_pct": m["max_drawdown"], "pf": pf, "trades": len(trades), "fees": fees,
           "sharpe": m["sharpe_ratio"], "max_underwater_days": m["max_underwater_period"],
           "terminal_gap": gap, "reported_preterminal_open_trades": m["total_open_trades"],
           "boundary_closes": sum(int(t["closed_at"]) == 1792368000000 for t in trades),
           "max_drawdown_usdt": float(usd.max()),
           "max_usdt_dd_date": usd.idxmax().isoformat(), "gates": gates,
           "nominal_pass": all(gates.values()) if cost == "N" else None,
           "stress_positive": net > 0 if cost == "F95" else None, "by_symbol": by,
           "economic_hash_8dec": hashlib.sha256(json.dumps(economic, separators=(",", ":")).encode()).hexdigest(),
           "engine_metrics": m, "first_equity_date": s.index[0].isoformat(),
           "last_equity_date": s.index[-1].isoformat()}
    for rule, dest, key in [("ME", monthly, "month"), ("QE", quarterly, "quarter")]:
        prior = 10000.0
        for dt, value in s.resample(rule).last().items():
            period = dt.strftime("%Y-%m") if key == "month" else f"{dt.year}Q{dt.quarter}"
            dest.append({"case": label, key: period, "start_equity": prior, "end_equity": float(value),
                         "profit": float(value - prior), "return_pct": float(100 * (value / prior - 1)),
                         "partial": dt.month == 10 if key == "month" else dt.quarter == 4})
            prior = value
    mr = [x for x in monthly if x["case"] == label]
    qr = [x for x in quarterly if x["case"] == label and not x["partial"]]
    row["positive_months"] = sum(x["profit"] > 0 for x in mr)
    row["calendar_months"] = len(mr)
    row["positive_full_quarters"] = sum(x["profit"] > 0 for x in qr)
    row["full_quarters"] = len(qr)
    row["best_month"] = max(mr, key=lambda x: x["return_pct"])
    row["worst_month"] = min(mr, key=lambda x: x["return_pct"])
    row["best_trade"] = max((float(t["PNL"]) for t in trades), default=0)
    row["net_excluding_best_trade_arithmetic"] = net - row["best_trade"]
    rows.append(row)

indexed = {row["case"]: row for row in rows}
for row in rows:
    row["comparisons"] = {}
    for reference in ["K1001", "N204"]:
        key = f'{reference}_{row["portfolio"]}_{row["cost"]}'
        if key not in indexed:
            continue
        ref = indexed[key]
        a, b = signatures[row["case"]], signatures[key]
        common = a.keys() & b.keys()
        changed_exits = sum(int(a[k]["closed_at"]) != int(b[k]["closed_at"]) or
                            not math.isclose(float(a[k]["exit_price"]), float(b[k]["exit_price"]), rel_tol=0, abs_tol=1e-8)
                            for k in common)
        row["comparisons"][reference] = {
            "delta_net": row["net"] - ref["net"], "delta_return_pct": row["return_pct"] - ref["return_pct"],
            "new_entries": len(a.keys() - b.keys()), "removed_entries": len(b.keys() - a.keys()),
            "common_entries": len(common), "changed_exits": changed_exits,
            "economic_identity_at_8dec": row["economic_hash_8dec"] == ref["economic_hash_8dec"]}

result = {"rows": rows, "monthly": monthly, "quarterly": quarterly}
(out / "summary.json").write_text(json.dumps(result, indent=2, allow_nan=False))
pd.DataFrame(monthly).to_csv(out / "monthly.csv", index=False)
pd.DataFrame(quarterly).to_csv(out / "quarterly.csv", index=False)
jh.debug(json.dumps([{k: v for k, v in r.items() if k != "engine_metrics"} for r in rows], allow_nan=False))

```
