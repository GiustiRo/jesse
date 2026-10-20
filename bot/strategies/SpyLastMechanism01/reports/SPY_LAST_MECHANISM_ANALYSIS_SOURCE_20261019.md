# Last mechanism snapshot analysis

Initialaudit0ed613d8ea28425088dbe575ee0c5bc2 succeeded8snapshots. Followup same8inputs explicitly combines concentration exclusion with static10bps stress on RETAINED fills, so separate positive statistics are not falsely presented as a joint pass. Strategies/fills/rules unchanged; no additional fulls. Only inputs read, output written. RootMTM separately.

```python
import json, math, hashlib
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone

URLS={"MECH01":"http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592","MECH02":"http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e","MECH03":"http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea","MECH04":"http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05","MECH05":"http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862","MECH06":"http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65","Cq":"http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639","BR02":"http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810"}
OUT=Path("output")
OUT.mkdir(exist_ok=True)
START=int(datetime(2020,10,15,tzinfo=timezone.utc).timestamp()*1000)
END=int(datetime(2025,12,31,tzinfo=timezone.utc).timestamp()*1000)
SPAN=(END-START)/3600000
FEE=0.00045

def close(a,b):
    return math.isclose(float(a),float(b),rel_tol=1e-9,abs_tol=1e-7)

def dump(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,allow_nan=False),encoding="utf-8")

rows={}
allfills={}
curveprints={}
manifest=json.loads(Path("inputs/manifest.json").read_text())
manifest=manifest.get("inputs",manifest) if isinstance(manifest,dict) else manifest
for item in manifest:
    name=item["name"]
    data=json.loads(Path("inputs",name+".json").read_text())
    summary=data["summary"]
    assert summary["session_status"]=="finished", summary
    m=data["metrics"]; trades=data["trades"]
    form=summary["form"]
    assert form["start_date"]=="2020-10-15" and form["finish_date"]=="2025-12-31"
    cfg=form["config"]; ex=cfg["exchange"]
    assert cfg["warm_up_candles"]==240 and ex["balance"]==10000
    assert ex["fee"]==FEE and ex["futures_leverage"]==5 and ex["futures_leverage_mode"]=="isolated"
    assert form["fast_mode"] is False and form["debug_mode"] is False
    assert len(form["routes"])==1 and form["routes"][0]["symbol"]=="SPY-USDT"
    assert form["routes"][0]["timeframe"]=="4h"
    assert form["data_routes"]==[{"exchange":"Binance Perpetual Futures","symbol":"SPY-USDT","timeframe":"1m"}]
    pnls=[]; fees=[]; gross=[]; turns=[]; holds=[]; nt=[]; fingerprints=[]; pertrade=[]
    kinds=Counter(); entrykinds=Counter(); exitkinds=Counter(); cohorts=defaultdict(lambda:{"n":0,"net":0.0,"fees":0.0})
    terminal=[]; prev=START; fills=[]
    for t in sorted(trades,key=lambda v:v["opened_at"]):
        assert t["type"]=="long" and t["symbol"]=="SPY-USDT"
        assert START<=t["opened_at"]<=t["closed_at"]<=END
        assert t["opened_at"]>=prev, "overlapping positions"
        prev=t["closed_at"]
        orders=[o for o in t["orders"] if o["status"]=="EXECUTED"]
        buys=[o for o in orders if o["side"]=="buy"]
        sells=[o for o in orders if o["side"]=="sell"]
        assert buys and sells
        bq=math.fsum(abs(o["filled_qty"]) for o in buys)
        sq=math.fsum(abs(o["filled_qty"]) for o in sells)
        bn=math.fsum(abs(o["filled_qty"])*o["price"] for o in buys)
        sn=math.fsum(abs(o["filled_qty"])*o["price"] for o in sells)
        assert close(bq,sq) and close(bq,t["qty"])
        assert close(bn/bq,t["entry_price"]) and close(sn/sq,t["exit_price"])
        fee=FEE*(bn+sn); g=sn-bn; p=g-fee
        assert close(p,t["PNL"]) and close(fee,t["fee"])
        assert close((t["closed_at"]-t["opened_at"])/1000,t["holding_period"])
        h=(t["closed_at"]-t["opened_at"])/3600000
        pnls.append(p); gross.append(g); fees.append(fee); turns.append(bn+sn); holds.append(h); nt.append(bn*h)
        year=str(datetime.fromtimestamp(t["closed_at"]/1000,timezone.utc).year)
        cohorts[year]["n"]+=1; cohorts[year]["net"]+=p; cohorts[year]["fees"]+=fee
        entrytype=Counter(o["type"] for o in buys); exittype=Counter(o["type"] for o in sells)
        entrykinds.update(entrytype); exitkinds.update(exittype)
        for o in orders:
            kinds[o["type"]]+=1
            if o["executed_at"]==END:
                terminal.append({"trade_id":t["id"],"side":o["side"],"type":o["type"],"gross":g,"net":p,"fee":fee,"exit_fee":FEE*sn})
        fp=[t["opened_at"],t["closed_at"],t["entry_price"],t["exit_price"],bq,fee,p]
        fingerprints.append(fp)
        pertrade.append({"id":t["id"],"opened_at":t["opened_at"],"closed_at":t["closed_at"],"entry":bn/bq,"exit":sn/sq,"qty":bq,"entry_notional":bn,"gross":g,"fees":fee,"net":p,"hold_hours":h,"net_bps_entry":p/bn*10000,"entry_types":dict(entrytype),"exit_types":dict(exittype)})
        fills.append(t)
    net=math.fsum(pnls); fee=math.fsum(fees); g=math.fsum(gross)
    assert len(trades)==m["total"] and close(net,m.get("net_profit",0)) and close(fee,m.get("fee",0))
    assert close(10000+net,m["finishing_balance"])
    if m.get("total_open_trades",0):
        assert m["total_open_trades"]==1 and len(terminal)==1
        assert close(m["open_pl"],terminal[0]["gross"])
    else:
        assert close(m.get("open_pl",0),0)
    losses=-math.fsum(v for v in pnls if v<0); wins=math.fsum(v for v in pnls if v>0)
    ordered=sorted(pnls,reverse=True)
    turnover=math.fsum(turns); entrytotal=math.fsum(v["entry_notional"] for v in pertrade)
    ranked_trades=sorted(pertrade,key=lambda t:t["net"],reverse=True)
    retained3_turn=turnover-math.fsum(t["fees"]/FEE for t in ranked_trades[:3])
    retained1_turn=turnover-math.fsum(t["fees"]/FEE for t in ranked_trades[:1])
    row={"name":name,"url":URLS[name],"n":len(trades),"net":net,"gross_before_fees":g,"fees":fee,
         "pf":wins/losses if losses else None,"sharpe":m.get("sharpe_ratio"),"dd_motor_pct":m.get("max_drawdown"),"cagr_motor_pct":m.get("annual_return"),
         "time_exposure_pct":math.fsum(holds)/SPAN*100,"entry_price_notional_time":math.fsum(nt)/(10000*SPAN),
         "mean_hold_hours":math.fsum(holds)/len(holds) if holds else None,"turnover_two_sides":turnover,"total_entry_notional":entrytotal,
         "net_bps_per_entry_notional":net/entrytotal*10000 if entrytotal else None,
         "net_plus5bpsRT":net-0.00025*turnover,"net_plus10bpsRT":net-0.0005*turnover,
         "net_exbest":net-math.fsum(ordered[:1]),"net_ex3best":net-math.fsum(ordered[:3]),
         "net_exbest_plus10bpsRT":net-math.fsum(ordered[:1])-0.0005*retained1_turn,
         "net_ex3best_plus10bpsRT":net-math.fsum(ordered[:3])-0.0005*retained3_turn,
         "close_year_cohorts":dict(cohorts),"executed_order_types":dict(kinds),"entry_order_types":dict(entrykinds),"exit_order_types":dict(exitkinds),
         "terminal_orders":terminal,"metric_preterminal_open_count":m.get("total_open_trades"),"fingerprint":hashlib.sha256(json.dumps(fingerprints).encode()).hexdigest(),
         "audit":"passed"}
    dump(name+"_detail.json",{"row":row,"trades":pertrade,"hyperparameters":data["hyperparameters"]})
    rows[name]=row; allfills[name]=pertrade
    curveprints[name]=hashlib.sha256(json.dumps(data["equity_curve"]).encode()).hexdigest()

pairs={}
for a,b in [("BR02","MECH01"),("BR02","MECH02"),("BR02","MECH03"),("BR02","MECH04"),("BR02","MECH05"),("BR02","MECH06"),("MECH01","MECH02"),("MECH03","MECH04")]:
    ra=rows[a]; rb=rows[b]
    aa={t["opened_at"]:t for t in allfills[a]}; bb={t["opened_at"]:t for t in allfills[b]}
    common=set(aa)&set(bb)
    pairs[a+"_"+b]={"net_delta":rb["net"]-ra["net"],"n_delta":rb["n"]-ra["n"],"common_exact_open_timestamps":len(common),
        "common_entry_price_equal":sum(close(aa[k]["entry"],bb[k]["entry"]) for k in common),
        "common_norm_netbps_delta_sum":math.fsum(bb[k]["net_bps_entry"]-aa[k]["net_bps_entry"] for k in common),
        "notes":"Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."}
dump("summary.json",{"rows":rows,"pairs":pairs,"curve_fingerprints":curveprints,"span_hours":SPAN,
    "notes":["Cohorts are year of trade closing, not calendar MTM.","RT stress static same fills/qty, no decision or risk recalculation.","Notional-time valued at entry price, not actual MTM exposure.","Concentration exclusions are descriptive, no retrospective trading filter."]})
print(json.dumps({"audit":"passed","names":list(rows),"metrics":{n:{"N":r["n"],"net":r["net"],"DD":r["dd_motor_pct"],"plus10":r["net_plus10bpsRT"]} for n,r in rows.items()}}))

```
