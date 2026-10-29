# K1001 OOS 2026 — análisis reproducible definitivo

Código predefinido de métricas/puertas. Se añadió inicialización de jesse.models antes del logger tras detectar import circular en el primer job, sin cambiar cálculos ni criterios. Usar sólo los cuatro snapshots corregidos del registro CORRECTED_REGISTRY; resultados anteriores inválidos por PAXG truncado/caché.

Análisis final 3543852d0eab43d9be15e066eb7017d4 succeeded.

```python
import json, math
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

out = Path("output")
out.mkdir(exist_ok=True)
data = {p.stem: json.loads(p.read_text()) for p in Path("inputs").glob("*.json") if p.name != "manifest.json"}
rows, monthly, quarterly = [], [], []
fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
for label, d in sorted(data.items()):
    summary, m = d["summary"], d["metrics"]
    f = summary["form"]
    assert summary["session_status"] == "finished"
    assert f["start_date"] == "2026-01-01" and f["finish_date"] == "2026-10-19"
    ex = f["config"]["exchange"]
    assert ex["balance"] == 10000 and ex["futures_leverage"] == 3 and ex["futures_leverage_mode"] == "isolated"
    assert ex["fee"] == (0.00045 if label.endswith("_N") else 0.00095)
    assert f["config"]["warm_up_candles"] == 240 and not f["fast_mode"]
    assert [r["strategy"] for r in f["routes"]] == ["CapitalR12K1001R2A6", "CapitalR12PaxgR2A6", "CapitalR12Spy" + label[0] + "R2A6"]
    trades = d["trades"]
    net = math.fsum(float(t["PNL"]) for t in trades)
    fees = math.fsum(float(t["fee"]) for t in trades)
    wins = math.fsum(max(0, float(t["PNL"])) for t in trades)
    losses = -math.fsum(min(0, float(t["PNL"])) for t in trades)
    pf = wins / losses if losses else None
    assert abs(net - float(m["net_profit"])) < .01
    assert abs(10000 + net - float(m["finishing_balance"])) < .01
    assert len(trades) == m["total"]
    series = next(s for s in d["equity_curve"] if s["name"] == "Portfolio")
    curve = pd.DataFrame(series["data"]).sort_values("time").drop_duplicates("time", keep="last")
    curve["date"] = pd.to_datetime(curve["time"], unit="s", utc=True)
    s = curve.set_index("date")["value"].astype(float)
    peak = s.cummax()
    dd = (s / peak - 1) * 100
    usd = peak - s
    by = {}
    for t in trades:
        a = by.setdefault(t["symbol"], {"net": 0.0, "fees": 0.0, "trades": 0})
        a["net"] += float(t["PNL"])
        a["fees"] += float(t["fee"])
        a["trades"] += 1
    gates = {"positive_net": net > 0, "pf_ge_1_2": pf is not None and pf >= 1.2,
             "dd_ge_minus25": float(m["max_drawdown"]) >= -25, "trades_ge_20": len(trades) >= 20}
    row = {"case": label, "net": net, "balance": m["finishing_balance"], "return_pct": m["net_profit_percentage"],
           "dd_pct": m["max_drawdown"], "pf": pf, "trades": len(trades), "fees": fees,
           "sharpe": m["sharpe_ratio"], "max_underwater_days": m["max_underwater_period"],
           "terminal_equity": float(s.iloc[-1]), "terminal_gap": float(s.iloc[-1]) - float(m["finishing_balance"]),
           "max_drawdown_usdt": float(usd.max()), "max_usdt_dd_date": usd.idxmax().isoformat(),
           "gates": gates, "nominal_pass": all(gates.values()) if label.endswith("_N") else None,
           "stress_positive": net > 0 if label.endswith("_F95") else None,
           "by_symbol": by, "engine_metrics": m,
           "first_equity_date": s.index[0].isoformat(), "last_equity_date": s.index[-1].isoformat()}
    assert abs(row["terminal_gap"]) < .01
    for rule, dest, key in [("ME", monthly, "month"), ("QE", quarterly, "quarter")]:
        prior = 10000.0
        for dt, value in s.resample(rule).last().items():
            period = dt.strftime("%Y-%m") if key == "month" else str(dt.to_period("Q"))
            dest.append({"case": label, key: period, "start_equity": prior, "end_equity": float(value),
                         "profit": float(value - prior), "return_pct": float(100 * (value / prior - 1)),
                         "partial": dt.month == 10 if key == "month" else dt.quarter == 4})
            prior = value
    mr = [x for x in monthly if x["case"] == label]
    row["positive_months"] = sum(x["profit"] > 0 for x in mr)
    row["months"] = len(mr)
    row["best_month"] = max(mr, key=lambda x: x["return_pct"])
    row["worst_month"] = min(mr, key=lambda x: x["return_pct"])
    row["net_excluding_best_trade"] = net - max((float(t["PNL"]) for t in trades), default=0)
    rows.append(row)
    axes[0].plot(s.index, s, label=label)
    axes[1].plot(dd.index, dd, label=label)
for ax in axes:
    ax.legend()
    ax.grid(alpha=.2)
axes[0].set_title("K1001 OOS 2026 — 10.000 USDT, riesgo 2%/6%, 3x")
axes[0].set_ylabel("Equity USDT")
axes[1].set_ylabel("Drawdown %")
fig.tight_layout()
fig.savefig(out / "k1001_oos_2026.png", dpi=110)
plt.close(fig)
pd.DataFrame(monthly).to_csv(out / "monthly.csv", index=False)
pd.DataFrame(quarterly).to_csv(out / "quarterly.csv", index=False)
(out / "summary.json").write_text(json.dumps({"rows": rows, "monthly": monthly, "quarterly": quarterly}, indent=2, allow_nan=False))
# Project convention: all diagnostic output uses jh.debug.
# Standalone jobs must initialize models before helpers to avoid Jesse's import cycle.
import jesse.models
import jesse.helpers as jh
jh.debug(json.dumps({"rows": rows, "monthly": monthly, "quarterly": quarterly}, allow_nan=False))

```
