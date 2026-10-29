# Fuente del diagnóstico V1
Lectura exclusiva de inputs/ y escritura en output/. No ejecuta backtests. Los grupos de mercado se infieren por duración y límite del fold; no son razones explícitas.

```python
import json, math, statistics
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
records=[]; sources=[]; maxerr=0.
for p in sorted(Path("inputs").glob("s*.json")):
 d=json.load(open(p)); s=d["summary"]; ts=d["trades"]
 strategy=s["form"]["routes"][0]["strategy"]; parts=strategy.split("_")
 config="_".join(parts[1:3]); stage=parts[3]; period="2020-2021" if stage=="E1T" else "2022-2023"
 assert stage=="E1T" or stage in ("E1V","E2V","E3V","E4V")
 finish=datetime.fromisoformat(s["form"]["finish_date"]).replace(tzinfo=timezone.utc).timestamp()*1000
 ledger=d["metrics"].get("funding",{}).get("ledger",[])
 sources.append(dict(config=config,stage=stage,session_id=s["session_id"],trades=len(ts),start=s["form"]["start_date"],finish=s["form"]["finish_date"]))
 for t in ts:
  sign=1 if t["type"]=="long" else -1
  gross=(t["exit_price"]-t["entry_price"])*t["qty"]*sign
  fee=t["fee"]; fund=math.fsum(x["cashflow"] for x in ledger if x["trade_id"]==t["id"])
  err=abs(gross-fee+fund-t["PNL"]); maxerr=max(maxerr,err); assert err<1e-6
  executed=[o for o in t["orders"] if o["status"]=="EXECUTED"]
  exits=[o for o in executed if o["reduce_only"]]
  assert exits
  kinds=sorted(set(o["type"] for o in exits))
  # Only resting STOP/LIMIT exits are directly identified; MARKET motive is inferred.
  if kinds==["STOP"]: reason="stop_order"
  elif kinds==["LIMIT"]: reason="target_order"
  elif kinds==["MARKET"] and t["holding_period"]>=86400: reason="market_24h_inferred"
  elif kinds==["MARKET"] and finish-60000<=t["closed_at"]<=finish: reason="market_fold_end_inferred"
  else: reason="ambiguous_"+"_".join(kinds)
  notional=abs(t["qty"]*t["entry_price"])
  records.append(dict(config=config,stage=stage,period=period,session_id=s["session_id"],trade_id=t["id"],direction=t["type"],
   reason=reason,gross=gross,fees=fee,funding=fund,net=t["PNL"],holding_h=t["holding_period"]/3600,
   gross_bps=gross/notional*10000,fee_bps=fee/notional*10000,funding_bps=fund/notional*10000,net_bps=t["PNL"]/notional*10000,
   positive_price_negative_net=int(gross>0 and t["PNL"]<=0)))
def stats(rs):
 n=len(rs); vals=[r["net"] for r in rs]; wins=[x for x in vals if x>0]; losses=[x for x in vals if x<0]
 out=dict(n=n,gross=math.fsum(r["gross"] for r in rs),fees=math.fsum(r["fees"] for r in rs),funding=math.fsum(r["funding"] for r in rs),
  net=math.fsum(vals),pf=math.fsum(wins)/abs(math.fsum(losses)) if losses else None,
  win_pct=100*len(wins)/n if n else None,
  mean_net=math.fsum(vals)/n if n else None,
  median_hold_h=statistics.median(r["holding_h"] for r in rs) if n else None,
  positive_price_negative_net=sum(r["positive_price_negative_net"] for r in rs))
 for field in ("gross_bps","fee_bps","funding_bps","net_bps"):
  out["mean_"+field]=statistics.mean(r[field] for r in rs) if n else None
 return out
groups={}
for r in records:
 groups.setdefault((r["config"],r["period"]),[]).append(r)
results=[]
# Include zero-trade configurations, with null rates and PF.
for config,period in sorted(set((s["config"],"2020-2021" if s["stage"]=="E1T" else "2022-2023") for s in sources)):
 rs=groups.get((config,period),[])
 results.append(dict(config=config,period=period,**stats(rs),
  directions={k:stats([r for r in rs if r["direction"]==k]) for k in ("long","short")},
  exits={k:stats([r for r in rs if r["reason"]==k]) for k in sorted(set(r["reason"] for r in rs))},
  folds={s["stage"]:stats([r for r in rs if r["stage"]==s["stage"]]) for s in sources if s["config"]==config and ("2020-2021" if s["stage"]=="E1T" else "2022-2023")==period}))
out=dict(results=results,sources=sources,max_accounting_error=maxerr,trade_records=len(records))
json.dump(out,open("output/diagnostic.json","w"),indent=2)
json.dump(records,open("output/trades.json","w"),indent=2)
print(json.dumps(out))

```
