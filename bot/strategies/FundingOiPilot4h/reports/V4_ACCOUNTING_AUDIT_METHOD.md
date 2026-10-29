# V4 accounting audit

Full snapshots only. Same V3 cashflow/fee/slippage accounting with explicitBTC-USDT/1h route checks. Model drawdown governs gates; terminal daily-curve drawdown separately reported. Effective funding clock normalized with retained raw provider jitter<=1000ms. Zero-trade runs may lack standard metrics/equity: labels absent_zero_trades, calendars empty, no fabricated annual evidence; empty trades/ledger/net asserted.

```python
import json, math
from pathlib import Path
from datetime import datetime, timezone
rows=[]
for path in sorted(Path("inputs").glob("s*.json")):
 d=json.load(open(path)); s=d["summary"]; m=d["metrics"]; ts=d["trades"]; cfg=s["form"]["config"]
 assert s["session_status"]=="finished"
 assert s["form"]["routes"][0]["timeframe"]=="1h"
 assert s["form"]["routes"][0]["symbol"]=="BTC-USDT"
 if "_expected" in globals():
  exp=_expected[path.stem]
  assert cfg==exp["config"] and s["form"]["routes"][0]["strategy"]==exp["strategy"]
  assert s["form"]["start_date"]==exp["start"] and s["form"]["finish_date"]==exp["finish"]
  assert s["form"]["debug_mode"] is True and s["form"]["fast_mode"] is True
  assert all(s["form"].get(k) is False for k in ("benchmark","export_csv","export_json","export_chart"))
 assert cfg["exchange"]["balance"]==10000 and cfg["exchange"]["futures_leverage"]==3
 assert cfg["exchange"]["futures_leverage_mode"]=="isolated" and cfg["warm_up_candles"]==240
 assert cfg["funding"]["dataset_id"]=="9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571"
 assert cfg["open_interest"]["dataset_id"]=="6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf"
 assert cfg["open_interest"]["max_age_ms"]==600000 and cfg["open_interest"]["allow_missing_observations"] is True
 fee=cfg["exchange"]["fee"];bps=cfg["exchange"].get("slippage_bps",0)
 ledger=m.get("funding",{}).get("ledger",[]);errors=[];gross=fees=funding=turnover=holding=0.;directions={};kinds={};adjusted=0
 for t in ts:
  sign=1 if t["type"]=="long" else -1
  g=sign*(t["exit_price"]-t["entry_price"])*t["qty"]
  trade_ledger=[x for x in ledger if x["trade_id"]==t["id"]]
  cf=math.fsum(x["cashflow"] for x in trade_ledger)
  for x in trade_ledger:
   errors.extend([abs(x["cashflow"]+x["qty"]*x["mark_price"]*x["rate_decimal"]),abs(x["qty"]-sign*t["qty"])])
   assert 0<=x["settled_at"]-x["effective_at"]<=1000
   assert t["opened_at"]<=x["effective_at"]<=t["closed_at"]
  errors.extend([abs(g-t["fee"]+cf-t["PNL"]),abs(cf-t.get("funding",0))])
  executed=[o for o in t["orders"] if o["status"]=="EXECUTED"]
  errors.append(abs(math.fsum(abs(o["filled_qty"])*o["price"]*fee for o in executed)-t["fee"]))
  for o in executed:
   turnover+=abs(o["filled_qty"])*o["price"]
   if o["reduce_only"]:kinds[o["type"]]=kinds.get(o["type"],0)+1
   if bps and o["type"] in ("MARKET","STOP"):
    slip=o["slippage"];osign=1 if o["side"]=="buy" else -1
    errors.append(abs(o["price"]-slip["reference_price"]*(1+osign*bps/10000)));assert slip["bps"]==bps;adjusted+=1
  gross+=g;fees+=t["fee"];funding+=cf;holding+=t["holding_period"]
  side=directions.setdefault(t["type"],dict(n=0,gross=0.,fees=0.,funding=0.,net=0.))
  side["n"]+=1;side["gross"]+=g;side["fees"]+=t["fee"];side["funding"]+=cf;side["net"]+=t["PNL"]
 assert set(x["trade_id"] for x in ledger)<=set(t["id"] for t in ts)
 proxy_funding=math.fsum(x["cashflow"] for x in ledger if "proxy" in x["mark_price_source"])
 exact_funding=math.fsum(x["cashflow"] for x in ledger if x["mark_price_source"]=="fundingRate.settlement_mark")
 unclassified_funding=math.fsum(x["cashflow"] for x in ledger if "proxy" not in x["mark_price_source"] and x["mark_price_source"]!="fundingRate.settlement_mark")
 funding_sources={source:dict(n=sum(x["mark_price_source"]==source for x in ledger),cashflow=math.fsum(x["cashflow"] for x in ledger if x["mark_price_source"]==source)) for source in sorted(set(x["mark_price_source"] for x in ledger))}
 pnls=[t["PNL"] for t in ts];net=math.fsum(pnls);win=math.fsum(x for x in pnls if x>0);loss=math.fsum(x for x in pnls if x<0)
 pf=win/abs(loss) if loss else None
 errors.extend([abs(net-(m.get("net_profit") or 0)),abs(fees-(m.get("fee") or 0)),abs(funding-m.get("funding",{}).get("cashflow",0))])
 if ts:errors.append(abs(10000+net-m["finishing_balance"]))
 assert max(errors,default=0)<1e-6
 assert m.get("funding",{}).get("effective_fast_mode") is False
 start=datetime.fromisoformat(s["form"]["start_date"]).replace(tzinfo=timezone.utc).timestamp()
 finish=datetime.fromisoformat(s["form"]["finish_date"]).replace(tzinfo=timezone.utc).timestamp()
 assert all(start*1000<=x["effective_at"]<finish*1000 for x in ledger)
 balances={}; full_equity=[]
 for curve in d["equity_curve"]:
  if curve["name"]=="Portfolio":
   for pt in sorted(curve["data"],key=lambda x:x["time"]):
    full_equity.append(float(pt["value"]))
    stamp=pt["time"]-61 if pt["time"]>start else pt["time"]
    month=datetime.fromtimestamp(stamp,timezone.utc).strftime("%Y-%m")
    balances[month]=pt["value"]
 curve_terminal_delta=(full_equity[-1]-(10000+net)) if full_equity else None
 terminal_month=datetime.fromtimestamp(finish-1,timezone.utc).strftime("%Y-%m")
 if terminal_month in balances:balances[terminal_month]=10000+net
 required_months=[]; cursor=datetime.fromtimestamp(start,timezone.utc).replace(day=1)
 while cursor.timestamp()<finish:
  required_months.append(cursor.strftime("%Y-%m"))
  cursor=cursor.replace(year=cursor.year+1,month=1) if cursor.month==12 else cursor.replace(month=cursor.month+1)
 if full_equity:
  assert sorted(balances)==required_months, "Incomplete calendar equity evidence"
  assert len(full_equity)==int((finish-start)/86400)+1, "Incomplete daily equity evidence"
 else:
  # Jesse omits equity/standard metrics for zero-trade runs. Keep calendars empty.
  assert not ts and net==0 and not ledger

 peak=10000.; sampled_dd=0.
 for value in full_equity+[10000+net]:
  peak=max(peak,value);sampled_dd=max(sampled_dd,100*(1-value/peak))
 prev=10000.;months=[]
 for month,balance in sorted(balances.items()):
  months.append(dict(month=month,return_pct=(balance/prev-1)*100,end_equity=balance));prev=balance
 year_balances={}
 for month,balance in sorted(balances.items()):year_balances[month[:4]]=balance
 previous=10000.;years=[]
 for year,balance in sorted(year_balances.items()):
  years.append(dict(year=int(year),return_pct=(balance/previous-1)*100,end_equity=balance,full_year=(s["form"]["start_date"]<=year+"-01-01" and s["form"]["finish_date"]>=str(int(year)+1)+"-01-01")));previous=balance
 semester_ends={}
 for month,balance in sorted(balances.items()):semester_ends[month[:4]+"H"+("1" if int(month[5:7])<=6 else "2")]=balance
 previous=10000.;semesters=[]
 for period,balance in sorted(semester_ends.items()):
  year=int(period[:4]);half=int(period[-1]);a=str(year)+("-01-01" if half==1 else "-07-01");b=(str(year)+"-07-01") if half==1 else (str(year+1)+"-01-01")
  semesters.append(dict(period=period,return_pct=(balance/previous-1)*100,end_equity=balance,full_semester=(s["form"]["start_date"]<=a and s["form"]["finish_date"]>=b)));previous=balance
 full2021to23=[y for y in years if y["year"] in (2021,2022,2023) and y["full_year"]]
 year_gate=len(full2021to23)==3 and sum(y["return_pct"]>0 for y in full2021to23)>=2
 dd=abs(m.get("max_drawdown") or 0);pf_gate=(pf is not None and pf>=1.2) or (loss==0 and win>0)
 base_gate=len(ts)>=30 and net>0 and pf_gate and dd<=25
 days=(finish-start)/86400;cagr=((10000+net)/10000)**(365/days)-1 if 10000+net>0 else -1.
 is_replay=s["form"]["start_date"]=="2024-01-01" and s["form"]["finish_date"]=="2026-01-01"
 replay_gates=None
 if is_replay and full_equity:
  assert len(semesters)==4 and all(x["full_semester"] for x in semesters)
  replay_gates=dict(net_positive=net>0,pf_ge_1_2=bool(pf_gate),dd_le_25=dd<=25,trades_ge_100=len(ts)>=100,positive_semesters_ge_3=sum(x["return_pct"]>0 for x in semesters)>=3,cagr_ge_15=cagr*100>=15)
 sensitivities=[dict(kind=kind,multiplier=k,net_usdt=net+(k-1)*component,net_pct=(net+(k-1)*component)/100,sign_flip=(net*(net+(k-1)*component)<0),fixed_quantities_not_replay=True) for kind,component in (("proxy_only",proxy_funding),("global_funding",funding)) for k in (.5,1.5)]
 rows.append(dict(session_id=s["session_id"],strategy=s["form"]["routes"][0]["strategy"],start=s["form"]["start_date"],finish=s["form"]["finish_date"],n=len(ts),net=net,net_pct=net/100,pf=pf,pf_no_losses=loss==0 and win>0,dd=-dd,cagr_pct=cagr*100,turnover=turnover/10000,gross=gross,fees=fees,funding=funding,funding_events=len(ledger),proxy_funding=proxy_funding,exact_funding=exact_funding,unclassified_funding=unclassified_funding,funding_sources=funding_sources,holding_seconds=holding,exposure=holding/(finish-start),directions=directions,exit_order_types=kinds,months=months,years=years,semesters=semesters,replay_nominal_gates=replay_gates,replay_nominal_eligible=(all(replay_gates.values()) if replay_gates is not None else None),funding_sensitivities=sensitivities,screen_year_gate=year_gate,base_eligible=bool(base_gate),screen_eligible=bool(base_gate and year_gate),positive_pnl=win,negative_pnl=loss,best_trade=max(pnls,default=None),worst_trade=min(pnls,default=None),adjusted_fills=adjusted,curve_terminal_delta=curve_terminal_delta,sampled_dd_including_terminal_pct=-sampled_dd,equity_points=len(full_equity),equity_evidence=("full_daily" if full_equity else "absent_zero_trades"),max_accounting_error=max(errors,default=0),metric_open_indicator=m.get("total_open_trades"),metric_open_pl=m.get("open_pl")))
json.dump(rows,open("output/results.json","w"),indent=2)
print(json.dumps(rows))

```
