# AA — Código exacto de auditoría financiera

Job: `aec51c0c1dd84dd5abaddc4346895e99`. Estado succeeded. Inputs completos INTERACTION y MAIN_EFFECTS; no nuevos motores.

```python
import json,math
import numpy as np
import pandas as pd
results={}
for name in ("INTERACTION","MAIN_EFFECTS"):
 d=json.load(open("inputs/"+name+".json"));m=d["metrics"];tr=d["trades"]
 gross=sum((t["exit_price"]-t["entry_price"])*abs(t["qty"])*(1 if t["type"]=="long" else -1) for t in tr)
 fees=sum(t["fee"] for t in tr);fund=sum(t.get("funding",0) for t in tr);net=sum(t["PNL"] for t in tr)
 errors={"gross_fee_funding_pnl":gross-fees+fund-net,"pnl_metrics":net-m["net_profit"],
         "terminal_vs_net":m["finishing_balance"]-10000-net,"funding_vs_metric":fund-m["funding"]["cashflow"]}
 assert all(abs(x)<1e-6 for x in errors.values()),errors
 losses=-sum(t["PNL"] for t in tr if t["PNL"]<0)
 pf=sum(t["PNL"] for t in tr if t["PNL"]>0)/losses if losses else None
 start=pd.Timestamp("2020-10-15",tz="UTC");finish=pd.Timestamp("2026-01-01",tz="UTC")
 cagr=(m["finishing_balance"]/10000)**(365/((finish-start).total_seconds()/86400))-1
 results[name]={"N":len(tr),"net":net,"return_pct":net/100,"cagr_pct":cagr*100,"pf":pf,
  "dd_daily_pct":m["max_drawdown"],"fee":fees,"funding":fund,"funding_applied":m["funding"]["applied"],
  "proxy_payments":m["funding"]["mark_price_proxy_count"],"errors":errors,
  "gross":gross,"finish":m["finishing_balance"],"raw_open_counter":m["total_open_trades"],
  "long_pnl":sum(t["PNL"] for t in tr if t["type"]=="long"),"short_pnl":sum(t["PNL"] for t in tr if t["type"]=="short")}
json.dump(results,open("output/audit.json","w"),indent=2)
print(json.dumps(results))

```
