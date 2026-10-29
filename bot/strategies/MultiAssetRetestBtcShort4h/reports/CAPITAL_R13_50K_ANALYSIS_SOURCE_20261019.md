# R13 — análisis de ocho snapshots completos

Cuatro corridas50k y cuatro anclas10k, emparejadas por cartera y fee. DD absoluto y porcentual pueden ocurrir en episodios distintos: se preservan fechas y pico correspondiente. Equity diaria, extremos2020/2025 parciales. No es una proyección futura.

```python
import json, math
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
out=Path("output");out.mkdir(exist_ok=True)
data={p.stem:json.loads(p.read_text()) for p in Path("inputs").glob("*.json") if p.name!="manifest.json"}
rows=[];annual=[];monthly=[]
fig,axes=plt.subplots(2,1,figsize=(11,7),sharex=True)
def sig(t):
    return (t["symbol"],t["type"],int(t["opened_at"]),round(float(t["entry_price"]),7))
for label,d in sorted(data.items()):
    summary=d["summary"];f=summary["form"];m=d["metrics"]
    assert summary["session_status"]=="finished"
    assert f["start_date"]=="2020-10-15" and f["finish_date"]=="2025-12-31"
    assert f["config"]["exchange"]["futures_leverage"]==3
    capital=float(m["starting_balance"])
    assert capital in (10000,50000)
    trades=d["trades"];net=math.fsum(float(t["PNL"]) for t in trades)
    assert abs(net-float(m["net_profit"]))<0.01
    assert abs(capital+net-float(m["finishing_balance"]))<0.01
    series=next(s for s in d["equity_curve"] if s["name"]=="Portfolio")
    curve=pd.DataFrame(series["data"]).sort_values("time").drop_duplicates("time",keep="last")
    curve["date"]=pd.to_datetime(curve["time"],unit="s",utc=True)
    s=curve.set_index("date")["value"].astype(float)
    peak=s.cummax();dd=(s/peak-1)*100;usd=peak-s
    percent_trough=dd.idxmin();usd_trough=usd.idxmax()
    ratio_key=label.replace("_50k","_10k")
    base=data[ratio_key];bm=base["metrics"]
    tm={sig(t):t for t in trades};am={sig(t):t for t in base["trades"]}
    assert len(tm)==len(trades) and len(am)==len(base["trades"])
    shared=set(tm)&set(am)
    fees=math.fsum(float(t["fee"]) for t in trades)
    wins=math.fsum(max(0,float(t["PNL"])) for t in trades)
    losses=-math.fsum(min(0,float(t["PNL"])) for t in trades)
    by={}
    for t in trades:
        a=by.setdefault(t["symbol"],{"net":0.0,"fees":0.0,"trades":0})
        a["net"]+=float(t["PNL"]);a["fees"]+=float(t["fee"]);a["trades"]+=1
    row={"case":label,"capital":capital,"fee_rate":f["config"]["exchange"]["fee"],
        "net":net,"final_balance":m["finishing_balance"],"return_pct":m["net_profit_percentage"],
        "cagr_pct":m["annual_return"],"dd_pct":m["max_drawdown"],"calmar":m["calmar_ratio"],
        "sharpe":m["sharpe_ratio"],"pf":wins/losses if losses else None,"trades":len(trades),"fees":fees,
        "max_underwater_days":m["max_underwater_period"],"terminal_gap":float(s.iloc[-1])-float(m["finishing_balance"]),
        "max_drawdown_usdt":float(usd.max()),"max_drawdown_usdt_date":usd_trough.isoformat(),
        "percent_dd_trough_date":percent_trough.isoformat(),"peak_at_percent_dd":float(peak.loc[percent_trough]),
        "usdt_loss_at_percent_dd":float(usd.loc[percent_trough]),
        "net_minus_scaled_10k":net-(capital/10000)*float(bm["net_profit"]),
        "new_entries_vs_10k":len(set(tm)-set(am)),"removed_entries_vs_10k":len(set(am)-set(tm)),
        "changed_exits_vs_10k":sum(int(tm[k]["closed_at"])!=int(am[k]["closed_at"]) or abs(float(tm[k]["exit_price"])-float(am[k]["exit_price"]))>1e-7 for k in shared),
        "by_symbol":by,"engine_metrics":m}
    rows.append(row)
    for rule,dest,key in [("YE",annual,"year"),("ME",monthly,"month")]:
        prior=capital
        for dt,value in s.resample(rule).last().items():
            record={"case":label,key:dt.year if key=="year" else dt.strftime("%Y-%m"),
                "start_equity":prior,"end_equity":value,"profit":value-prior,"return_pct":100*(value/prior-1),
                "partial":dt.year in (2020,2025) if key=="year" else dt.strftime("%Y-%m") in ("2020-10","2025-12")}
            dest.append(record);prior=value
    if capital==50000:
        axes[0].plot(s.index,s,label=label);axes[1].plot(dd.index,dd,label=label)
pd.DataFrame(annual).to_csv(out/"annual.csv",index=False)
pd.DataFrame(monthly).to_csv(out/"monthly.csv",index=False)
(out/"summary.json").write_text(json.dumps({"rows":rows,"annual":annual},indent=2,allow_nan=False))
for ax in axes:ax.legend();ax.grid(alpha=.2)
axes[0].set_ylabel("USDT");axes[1].set_ylabel("Drawdown %")
axes[0].set_title("K1001 — 50.000 USDT, riesgo 2%/6%, 3x")
fig.tight_layout();fig.savefig(out/"equity_50k.png",dpi=110);plt.close(fig)
print(json.dumps([{k:v for k,v in r.items() if k not in ("engine_metrics","by_symbol")} for r in rows],allow_nan=False))

```