# R12 — código final de análisis

Sólo snapshots completos, diez por grupo. Además de ancla nominal L5 se compara cada perfil con original a mismo leverage y fee. Resumen JSON separado de CSV mensual para evitar truncamiento; curvas diarias y extremos parciales.

```python
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

out=Path("output")
out.mkdir(exist_ok=True)
manifest=json.loads(Path("inputs/manifest.json").read_text())
# Read all supplied snapshots rather than relying on manifest envelope shape.
paths=sorted(p for p in Path("inputs").glob("*.json") if p.name!="manifest.json")
rows=[]; annual=[]; monthly=[]; fills=[]; raw={}
fig, axes=plt.subplots(2,1,figsize=(11,7),sharex=True)
base_data=None
for p in paths:
    if p.stem=="L5":
        base_data=json.loads(p.read_text())
if base_data is None:
    raise ValueError("L5 anchor required")
base_trades=base_data["trades"]
def signature(t):
    return (t["symbol"],t["type"],int(t["opened_at"]),round(float(t["entry_price"]),7))
base_keys={signature(t) for t in base_trades}
base_map={signature(t):t for t in base_trades}
assert len(base_keys)==len(base_trades), "ambiguous anchor entry identities"
for p in paths:
    label=p.stem; d=json.loads(p.read_text()); summary=d["summary"]; m=d["metrics"]; raw[label]=m
    assert summary["session_status"]=="finished", (label,summary["session_status"])
    f=summary["form"]
    assert f["start_date"]=="2020-10-15" and f["finish_date"]=="2025-12-31"
    assert f["config"]["exchange"]["fee"] in (0.00045, 0.00095)
    leverage=f["config"]["exchange"]["futures_leverage"]
    ts=d["trades"]
    net=math.fsum(float(t["PNL"]) for t in ts)
    fee=math.fsum(float(t["fee"]) for t in ts)
    if abs(net-float(m["net_profit"]))>0.01:
        raise ValueError(("trade/engine net mismatch",label,net,m["net_profit"]))
    curve=next(s for s in d["equity_curve"] if s["name"]=="Portfolio")
    c=pd.DataFrame(curve["data"]).sort_values("time").drop_duplicates("time",keep="last")
    c["datetime"]=pd.to_datetime(c["time"],unit="s",utc=True)
    s=c.set_index("datetime")["value"].astype(float)
    dd=(s/s.cummax()-1)*100
    axes[0].plot(s.index,s.values,label=label)
    axes[1].plot(dd.index,dd.values,label=label)
    # Periods use the last available daily observation; no intraday precision is implied.
    me=s.resample("ME").last()
    prior=float(m["starting_balance"])
    for dt,value in me.items():
        if pd.isna(value): raise ValueError("missing month")
        monthly.append({"case":label,"month":dt.strftime("%Y-%m"),"return_pct":100*(value/prior-1),"equity_delta":value-prior,"partial":dt.strftime("%Y-%m") in ("2020-10","2025-12")})
        prior=value
    ye=s.resample("YE").last()
    prior=float(m["starting_balance"])
    for dt,value in ye.items():
        annual.append({"case":label,"year":dt.year,"return_pct":100*(value/prior-1),"equity_delta":value-prior,"partial":dt.year in (2020,2025)})
        prior=value
    wins=math.fsum(max(0,float(t["PNL"])) for t in ts)
    losses=-math.fsum(min(0,float(t["PNL"])) for t in ts)
    keys={signature(t) for t in ts}
    assert len(keys)==len(ts), "ambiguous entry identities"
    changed_exits=sum(1 for t in ts if signature(t) in base_map and
        (int(t["closed_at"])!=int(base_map[signature(t)]["closed_at"]) or
         abs(float(t["exit_price"])-float(base_map[signature(t)]["exit_price"]))>1e-7))
    gaps=np.diff(c["time"].to_numpy())
    rows.append({"case":label,"leverage":leverage,"engine_fee":f["config"]["exchange"]["fee"],"net":net,"return_pct":m["net_profit_percentage"],"cagr_pct":m["annual_return"],"dd_engine_pct":m["max_drawdown"],"dd_curve_pct":float(dd.min()),"calmar":m["calmar_ratio"],"sharpe":m["sharpe_ratio"],"sortino":m["sortino_ratio"],"pf":wins/losses if losses else None,"trades":len(ts),"fees":fee,"underwater_days_engine":m["max_underwater_period"],"curve_terminal":float(s.iloc[-1]),"wallet_terminal_engine":m["finishing_balance"],"terminal_gap":float(s.iloc[-1])-float(m["finishing_balance"]),"curve_points":len(s),"median_curve_step_seconds":float(np.median(gaps)) if len(gaps) else None,"removed_entry_records_vs_L5":len(base_keys-keys),"new_entry_records_vs_L5":len(keys-base_keys),"common_entries_changed_exit":changed_exits})
    by={}
    for t in ts:
        b=by.setdefault(t["symbol"],{"trades":0,"net":0.0,"fees":0.0})
        b["trades"]+=1; b["net"]+=float(t["PNL"]);b["fees"]+=float(t["fee"])
    fills.append({"case":label,"by_symbol":by,"entry_notional_sum":math.fsum(abs(float(t["qty"]))*float(t["entry_price"]) for t in ts),"entry_notional_turnover_initial_equity":math.fsum(abs(float(t["qty"]))*float(t["entry_price"]) for t in ts)/float(m["starting_balance"]), "time_weighted_entry_notional_over_initial_equity":math.fsum(abs(float(t["qty"]))*float(t["entry_price"])*float(t["holding_period"]) for t in ts)/(float(m["starting_balance"])*(pd.Timestamp(f["finish_date"],tz="UTC")-pd.Timestamp(f["start_date"],tz="UTC")).total_seconds())})
# Concentration uses observed daily-equity calendar deltas, not a rerun without trades.
for row in rows:
    ms=[x for x in monthly if x["case"]==row["case"]]
    full=[x for x in ms if not x["partial"]]
    observed_net=sum(x["equity_delta"] for x in ms)
    row.update(observed_curve_net=observed_net,
        positive_full_months=sum(x["equity_delta"]>0 for x in full),
        complete_months=len(full),
        best_observed_month_delta=max(x["equity_delta"] for x in ms),
        worst_observed_month_delta=min(x["equity_delta"] for x in ms),
        observed_net_ex_best_month=observed_net-max(x["equity_delta"] for x in ms))
# Compare capital profiles against the original at matching leverage AND fee.
snapshots={p.stem:json.loads(p.read_text()) for p in paths}
for row in rows:
    label=row["case"]
    if label.endswith("_F95"):
        reference="R1A8_L3_F95"
    elif label.endswith("_L1"):
        reference="L1"
    elif label.endswith("_L3"):
        reference="L3"
    else:
        reference=label
    target=snapshots[label]; anchor=snapshots[reference]
    assert target["summary"]["form"]["config"]["exchange"]["fee"] == anchor["summary"]["form"]["config"]["exchange"]["fee"]
    assert target["summary"]["form"]["config"]["exchange"]["futures_leverage"] == anchor["summary"]["form"]["config"]["exchange"]["futures_leverage"]
    tm={signature(t):t for t in target["trades"]}
    am={signature(t):t for t in anchor["trades"]}
    shared=set(tm)&set(am)
    row.update(same_fee_reference=reference,
        new_entries_same_fee=len(set(tm)-set(am)),
        removed_entries_same_fee=len(set(am)-set(tm)),
        changed_exits_same_fee=sum(int(tm[k]["closed_at"])!=int(am[k]["closed_at"]) or
            abs(float(tm[k]["exit_price"])-float(am[k]["exit_price"]))>1e-7 for k in shared),
        research_gate=bool(row["net"]>0 and row["pf"] is not None and row["pf"]>=1.2 and row["dd_engine_pct"]>=-25))
pd.DataFrame(rows).to_csv(out/"metrics.csv",index=False)
pd.DataFrame(annual).to_csv(out/"annual.csv",index=False)
pd.DataFrame(monthly).to_csv(out/"monthly.csv",index=False)
(out/"results.json").write_text(json.dumps({"rows":rows,"annual":annual,"monthly":monthly,"fills":fills,"engine_metrics":raw},indent=2,allow_nan=False))
(out/"summary.json").write_text(json.dumps({"rows":rows,"annual":annual,"fills":fills,"engine_metrics":raw},indent=2,allow_nan=False))
axes[0].set_title("Capital R12 — equity almacenada, USDT")
axes[0].set_ylabel("USDT");axes[1].set_ylabel("Drawdown %")
for ax in axes: ax.legend(ncol=4);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(out/"equity_drawdown.png",dpi=110);plt.close(fig)
# Calendar charts compare complete years 2021–2024; endpoints remain available in CSV.
ad=pd.DataFrame(annual); pivot=ad.pivot(index="year",columns="case",values="return_pct")
ax=pivot.plot.bar(figsize=(11,4),width=.8)
ax.set_ylabel("Retorno %");ax.set_title("R12 — retornos anuales desde equity diaria; 2020 y 2025 parciales")
ax.grid(axis="y",alpha=.2);ax.figure.tight_layout();ax.figure.savefig(out/"annual.png",dpi=110);plt.close(ax.figure)
print(json.dumps({"rows":rows,"annual":annual,"fills":fills},allow_nan=False))

```

La puerta de investigación (neto positivo/PF>=1.2/DD>=-25%) no constituye OOS ni aprobación operativa. Las diferencias de fill bajo fee mayor pueden venir de la gestión dependiente de fee; comparación de perfiles a igual fee separada.