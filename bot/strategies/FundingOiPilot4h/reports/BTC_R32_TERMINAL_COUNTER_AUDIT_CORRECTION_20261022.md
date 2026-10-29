# R32 snapshot V3 y join V3 — semántica de cierre terminal

Primer analysisjob C c0eaa8de292749a089867db7b104001f falló antes de exportar: el auditor exigía metrics.total_open_trades==0. Fallo del supuesto del auditor, no de motor. Conservados código/job/output; cero reruns económicos.

Lectura read-only del framework: Strategy._terminate() incrementa store.app.total_open_trades y total_open_pl cuando encuentra posición abierta, ANTES de crear cierre MARKET forzado; backtest ejecuta esa cola antes de finalizar balances/outputs. metrics.trades() copia esos contadores. Por tanto1 significa posición encontrada abierta antes del cierre terminal, no cuenta final de posiciones sin cerrar. Ambos C tienen PRETERMINALopens−closes1, cierre nativoT=FINISH y FINALopens=closes=N/equitypostfee. Esas pruebas serán cruzadas contra cada trade y orden, no suponer flat sólo desdecontador.

V3snapshot permite0/1 y exige timestamps de TODAS operaciones cerradas dentro de ventana. JoinV3 exige m.total=N, contadorpreterminal coincide con diferencia opens-closes PRETERMINAL y, si1, FINALexiste y exactamenteuntrade cierra FINISH, bruto=preterminalopenPL. Conserva todaslas demás conciliaciones, incluidoledger FINALpostfees/órdenes ejecutadas. No altera estrategia, configuración, precio o criterios. Los campos nativos se reportarán con semántica correcta.

Fuentes framework leídas: jesse/strategies/Strategy.py:1413–1454; jesse/services/metrics.py:393–394; jesse/modes/backtest_mode.py:1968–1981. No cambios.

## Fallo conservado
```json
{
  "action": "get_analysis_job",
  "status": "success",
  "job": {
    "id": "c0eaa8de292749a089867db7b104001f",
    "kind": "analysis",
    "workspace": "storage/mcp/analysis/c0eaa8de292749a089867db7b104001f",
    "inputs": [
      {
        "name": "C_INSIDE",
        "file": "inputs/C_INSIDE.json",
        "session_type": "backtest",
        "session_id": "6510739f-6c8d-45b4-904f-67395c95cca0",
        "session_status": "finished",
        "title": "MCP Backtest: R32 C | C_INSIDE | cuota1% | 24h sinTP",
        "size_bytes": 1322722
      },
      {
        "name": "C_CLOSE_ONLY",
        "file": "inputs/C_CLOSE_ONLY.json",
        "session_type": "backtest",
        "session_id": "175b17fe-58e2-456d-ad0c-44f8cd799755",
        "session_status": "finished",
        "title": "MCP Backtest: R32 C | C_CLOSE_ONLY | cuota1% | 24h sinTP",
        "size_bytes": 3028565
      }
    ],
    "status": "failed",
    "pid": 2401,
    "exit_code": 1,
    "started_at": "2026-10-22T12:28:22+00:00",
    "finished_at": "2026-10-22T12:28:22+00:00",
    "timeout_minutes": 3,
    "output_truncated": false,
    "expires_at": "2026-10-23T12:28:22+00:00",
    "lifetime": "Deleted when a later analysis starts, once 24 hours have passed since it finished (expires_at), or earlier when finished jobs exceed the 50-job or 2 GiB caps (oldest first)."
  },
  "artifacts": [],
  "artifacts_truncated": false,
  "output": "Traceback (most recent call last):\n  File \"/src/bot/storage/mcp/analysis/c0eaa8de292749a089867db7b104001f/analysis.py\", line 15, in <module>\n    assert metrics[\"total_open_trades\"]==0\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError\n",
  "output_lines_returned": 5,
  "earlier_output_omitted": false,
  "output_truncated": false,
  "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace."
}
```

## Snapshot corregido
```python
import json, math
from pathlib import Path
Path("output").mkdir(exist_ok=True)
manifest={}
assert len(EXPECTED_NAMES) == 2 and len(set(EXPECTED_NAMES)) == 2
for name in EXPECTED_NAMES:
    # run_analysis also creates inputs/manifest.json; only declared snapshots
    # are financial inputs. Names are injected explicitly by the caller.
    path = Path("inputs", name + ".json")
    assert path.is_file(), name
    snap=json.loads(path.read_text())
    summary,metrics,trades=snap["summary"],snap["metrics"],snap["trades"]
    assert summary["session_status"]=="finished"
    assert metrics["total_open_trades"] in (0, 1)
    # Jesse counts positions found open BEFORE its forced terminal close.
    # Actual final closure is verified from closed native trades and R32 logs.
    seen=set();rows=[]
    for t in trades:
        tid=t["id"]
        assert tid not in seen
        seen.add(tid)
        assert 1602720000000 < t["opened_at"] <= t["closed_at"] <= 1767225600000
        side=t["type"]
        assert side in ("long","short") and t["symbol"]=="BTC-USDT"
        qty=abs(float(t["qty"]));entry=float(t["entry_price"]);exit=float(t["exit_price"])
        fee=float(t["fee"]);net=float(t["PNL"])
        assert qty>0 and entry>0 and exit>0 and fee>=0
        direction=1 if side=="long" else -1
        gross=direction*(exit-entry)*qty
        assert abs(fee-.00045*qty*(entry+exit))<1e-6
        orders=[o for o in t.get("orders",[]) if o.get("status")=="EXECUTED"]
        ent=[o for o in orders if not o.get("reduce_only") and o.get("side")==("buy" if direction==1 else "sell")]
        assert len(ent)==1
        order=ent[0]
        assert order["type"]=="MARKET"
        assert order["executed_at"]==order["created_at"]==t["opened_at"]
        assert t["opened_at"]%14400000==0
        assert abs(float(order["price"])-entry)<1e-7
        present="funding" in t
        funding=float(t["funding"]) if present else None
        if present:
            assert math.isfinite(funding) and abs(gross-fee+funding-net)<1e-6
        rows.append(dict(trade_id=tid,side=side,opened_at=t["opened_at"],closed_at=t["closed_at"],
            entry=entry,exit=exit,qty=qty,fee=fee,gross=gross,net=net,
            funding_present=present,funding=funding,holding_period=t["holding_period"],orders=orders))
    parts=[];chunk=[]
    for row in rows:
        candidate=chunk+[row]
        if len(json.dumps(candidate,separators=(",",":")))>47000 and chunk:
            outfile=f"{name}_trades_{len(parts)}.json"
            payload=json.dumps(chunk,separators=(",",":"));assert len(payload)<48000
            Path("output",outfile).write_text(payload);parts.append({"path":outfile,"N":len(chunk),"chars":len(payload)});chunk=[row]
        else:chunk=candidate
    if chunk or not parts:
        outfile=f"{name}_trades_{len(parts)}.json";payload=json.dumps(chunk,separators=(",",":"));assert len(payload)<48000
        Path("output",outfile).write_text(payload);parts.append({"path":outfile,"N":len(chunk),"chars":len(payload)})
    funding=metrics.get("funding",{})
    meta={k:funding[k] for k in ("mode","dataset_id","status","applied","cashflow","event_count","mark_price_proxy_count","boundary_policy") if k in funding}
    manifest[name]={"N":len(rows),"net":math.fsum(r["net"] for r in rows),"gross":math.fsum(r["gross"] for r in rows),"fees":math.fsum(r["fee"] for r in rows),"funding_present":sum(r["funding_present"] for r in rows),"funding_metadata":meta,"parts":parts,"status":"SNAPSHOT_NATIVE_ORDER_AND_FEE_CHECK_PASS"}
payload=json.dumps(manifest,indent=2);assert len(payload)<48000
Path("output/manifest.json").write_text(payload)
print(json.dumps({"status":"PASS","N":{k:v["N"] for k,v in manifest.items()},"manifest_chars":len(payload)}))

```

## Join corregido
```javascript
function auditR32(name,summary,rows,logPages,fundPages) {
 const fail=m=>{throw Error(name+": "+m);};
 const near=(a,b,m,tol=1e-6)=>{if(!Number.isFinite(a)||!Number.isFinite(b)||Math.abs(a-b)>=tol)fail(m+" "+a+" vs "+b);};
 const sum=a=>a.reduce((x,y)=>x+y,0);
 const uniq=(a,key,m)=>{const map=new Map();for(const x of a){const k=key(x);if(map.has(k))fail(m+" duplicate "+k);map.set(k,x);}return map;};
 const parse=label=>[...logPages].reverse().flatMap(p=>p.items).flatMap(line=>{
   const i=line.indexOf(label+" ");if(i<0)return [];
   const t=line.slice(i+label.length+1);if(t.endsWith(" [line cut]"))fail("critical log truncated "+label);
   return [JSON.parse(t)];
 });
 const opens=parse("R32_OPEN"),closes=parse("R32_CLOSE"),plans=parse("R32_PLAN"),
   ownAll=parse("R32_SUMMARY"),r11All=parse("R11_SUMMARY"),monthsAll=parse("R11_MONTH");
 const stage=r11All.some(x=>x.stage==="FINAL")?"FINAL":"PRETERMINAL";
 const latest=(xs,label)=>{const a=xs.filter(x=>x.stage===stage);if(a.length!==1)fail(label+" stage count");return a[0];};
 const own=latest(ownAll,"R32"),r11=latest(r11All,"R11"),m=summary.metrics,N=rows.length;
 if(summary.session_status!=="finished"||![0,1].includes(m.total_open_trades)||m.total!==N)fail("session or terminal count");
 const preOwn=ownAll.filter(x=>x.stage==="PRETERMINAL");if(preOwn.length!==1||preOwn[0].opens-preOwn[0].closes!==m.total_open_trades)fail("preterminal open counter");
 if(m.total_open_trades===1){if(stage!=="FINAL")fail("missing post-close FINAL");const terminal=rows.filter(t=>t.closed_at===1767225600000);if(terminal.length!==1)fail("terminal closed trade");near(terminal[0].gross,m.open_pl,"preterminal open PL");}
 if(opens.length!==N||closes.length!==N||plans.length!==N||own.opens!==N||own.closes!==N||own.plans!==N)fail("native fill coverage");
 if(r11.minute_marks!==2741760||r11.invalid_windows!==0||r11.entries!==N)fail("M1 observer coverage");
 near(r11.equity,m.finishing_balance,"terminal equity");
 near(own.net,m.net_profit,"own ledger");
 if(own.risk_total!==.01||own.redistribution!==false||own.capital_denominator!=="total BTC wallet")fail("risk contract");
 const byOpen=uniq(opens,x=>x.opened_at,"open"),byClose=uniq(closes,x=>x.time,"close"),byPlan=uniq(plans,x=>x.time,"plan"),byId=uniq(rows,x=>x.trade_id,"trade");
 const payments=fundPages.flatMap(p=>p.items);uniq(payments,x=>x.trade_id+"|"+x.settled_at,"funding");
 if(m.funding.mode!=="historical"||!m.funding.applied||m.funding.dataset_id!=="9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571")fail("funding contract");
 if(payments.length!==m.funding.event_count)fail("payment count");
 const byFunding=new Map();
 for(const p of payments){const t=byId.get(p.trade_id);if(!t)fail("orphan funding");
   if(p.symbol!=="BTC-USDT")fail("fund symbol");
   if(!Number.isFinite(p.effective_at)||!(p.effective_at>t.opened_at&&p.effective_at<=t.closed_at&&p.effective_at<1767225600000))fail("fund effective clock outside trade/window");
   near(p.qty,(t.side==="long"?1:-1)*t.qty,"fund qty");
   near(p.cashflow,-p.qty*p.mark_price*p.rate_decimal,"fund formula");
   byFunding.set(p.trade_id,(byFunding.get(p.trade_id)||0)+p.cashflow);}
 near(sum(payments.map(p=>p.cashflow)),m.funding.cashflow,"fund ledger");
 let missingVerified=0;const sides={long:{N:0,net:0},short:{N:0,net:0}};
 for(const t of rows){
   const o=byOpen.get(t.opened_at),p=byPlan.get(t.opened_at),c=byClose.get(t.closed_at);
   if(!o||!p||!c)fail("missing exact lifecycle");
   if(o.label!==own.label||p.label!==own.label||c.label!==own.label||o.signal_at!==t.opened_at||o.time!==t.opened_at)fail("identity");
   const dir=t.side==="long"?1:-1;if(o.direction!==dir||p.direction!==dir)fail("side");
   near(o.entry,t.entry,"entry");near(p.entry,t.entry,"plan entry");near(o.qty,t.qty,"qty",1e-8);near(p.qty,t.qty,"plan qty",1e-8);
   near(o.distance,p.distance,"D");near(c.net,t.net,"close net");
   if(!(o.distance>0&&o.risk_budget>0))fail("geometry");
   near(o.stop,t.entry-dir*o.distance,"initial stop");
   near(o.risk_budget,p.risk_budget,"budget");
   const loss=t.qty*(o.distance+.00045*(t.entry+o.stop)+.001*t.entry);
   if(loss>o.risk_budget+1e-6)fail("risk budget");
   near(loss,p.planned_loss,"planned reserve risk");
   if(Math.abs(t.qty/.001-Math.round(t.qty/.001))>1e-7)fail("lot");
   if(o.hold_hours!==own.hold_hours)fail("horizon");
   if(own.tp_r===null){if(o.target_distance!==null)fail("unexpected target");}
   else near(o.target_distance,own.tp_r*o.distance,"target");
   const entries=t.orders.filter(x=>x.status==="EXECUTED"&&!x.reduce_only&&x.side===(dir===1?"buy":"sell"));
   const exits=t.orders.filter(x=>x.status==="EXECUTED"&&x.reduce_only&&x.side===(dir===1?"sell":"buy"));
   if(entries.length!==1||exits.length!==1)fail("executed order cardinality");
   if(entries[0].type!=="MARKET"||entries[0].created_at!==t.opened_at||entries[0].executed_at!==t.opened_at)fail("actual MARKET");
   near(entries[0].price,t.entry,"native entry price");near(Math.abs(entries[0].qty),t.qty,"native entry qty",1e-8);
   if(entries[0].filled_qty!==undefined)near(Math.abs(entries[0].filled_qty),t.qty,"entry filled qty",1e-8);
   near(exits[0].price,t.exit,"exit price");near(Math.abs(exits[0].qty),t.qty,"exit qty",1e-8);
   const f=byFunding.get(t.trade_id)||0;
   if(t.funding_present)near(t.funding,f,"trade funding");else{if(byFunding.has(t.trade_id))fail("missing field with payment");missingVerified++;}
   near(t.gross-t.fee+f,t.net,"gross-fee+fund");
   near(.00045*t.qty*(t.entry+t.exit),t.fee,"fee");
   t.opening_log=o;t.plan_log=p;t.funding_verified=f;t.R_net=t.net/(t.qty*o.distance);
   sides[t.side].N++;sides[t.side].net+=t.net;
 }
 if(sides.long.N!==own.long_opens||sides.short.N!==own.short_opens)fail("side ledger");
 const months=monthsAll.filter(x=>x.stage===stage).sort((a,b)=>a.start-b.start);uniq(months,x=>x.month,"month");
 if(months.length!==63||months.filter(x=>x.complete).length!==62)fail("month coverage");
 near(sum(months.map(x=>x.pnl)),m.net_profit,"monthly net");
 let chained=10000,previousFinish=1602720000000;for(const x of months){if(x.start!==previousFinish||!(x.finish>x.start))fail("monthly clock continuity");near(x.pnl,chained*x.return_fraction,"monthly chained return");chained+=x.pnl;previousFinish=x.finish;}if(previousFinish!==1767225600000)fail("monthly final clock");near(chained,m.finishing_balance,"monthly chained final");
 const complete=months.filter(x=>x.complete),active=complete.filter(x=>x.active),positive=active.filter(x=>x.pnl>0).length;
 if(positive!==r11.positive_active||active.length!==r11.active_months)fail("active summary");
 const qs=new Map();for(const x of complete){const k=x.month.slice(0,4)+"Q"+(Math.floor((Number(x.month.slice(5))-1)/3)+1);if(!qs.has(k))qs.set(k,[]);qs.get(k).push(x);}
 const fullQ=[...qs.values()].filter(x=>x.length===3),positiveQ=fullQ.filter(x=>sum(x.map(y=>y.pnl))>0).length;
 if(fullQ.length!==20||r11.positive_quarters!==positiveQ)fail("quarter summary");
 const rets=complete.map(x=>x.return_fraction).sort((a,b)=>a-b);near((rets[30]+rets[31])/2,r11.median_return,"monthly median",1e-12);
 near(sum(months.map(x=>x.pnl))-sum([...months].sort((a,b)=>b.pnl-a.pnl).slice(0,2).map(x=>x.pnl)),r11.pnl_without_best_two,"top2 arithmetic");
 near(sum(rows.map(t=>t.net)),m.net_profit,"net");
 near(m.finishing_balance-10000,m.net_profit,"final cash");
 const annual={};for(let y=2021;y<=2025;y++){const a=complete.filter(x=>x.month.startsWith(String(y)));if(a.length!==12)fail("annual coverage");annual[y]=100*(a.reduce((v,x)=>v*(1+x.return_fraction),1)-1);}
 const rolling=[];for(let j=0;j+12<=complete.length;j++){const a=complete.slice(j,j+12);rolling.push({start:a[0].month,finish:a[11].month,return_pct:100*(a.reduce((v,x)=>v*(1+x.return_fraction),1)-1)});}
 const losses=-sum(rows.filter(t=>t.net<0).map(t=>t.net)),profits=sum(rows.filter(t=>t.net>0).map(t=>t.net)),pf=losses>0?profits/losses:null,cagr=100*((m.finishing_balance/10000)**(365/1904)-1);
 const gates={CAGR30:cagr>=30,PF1_2:losses>0?pf>=1.2:profits>0,DD25:-r11.dd_m1_events<=.25,M65:active.length>0&&positive/active.length>=.65,Q80:positiveQ/20>=.8,median_positive:r11.median_return>0,without_best_two_positive:r11.pnl_without_best_two>0,N100:N>=100};
 return {status:"FULL_ACCOUNTING_AND_NATIVE_GEOMETRY_PASS",name,session_id:summary.session_id,dashboard_url:summary.dashboard_url,N,net:m.net_profit,finish:m.finishing_balance,cagr_pct:cagr,pf,pf_no_losses:losses===0&&profits>0,dd_m1_pct:-100*r11.dd_m1_events,positive_active:positive,active_months:active.length,positive_active_pct:active.length?100*positive/active.length:null,positive_quarters:positiveQ,median_calendar_month_pct:100*r11.median_return,pnl_without_best_two:r11.pnl_without_best_two,sides,annual_pct:annual,rolling12:rolling,gates,economic_all_gates:Object.values(gates).every(Boolean),funding:m.funding,missing_fields_zero_verified:missingVerified,own,r11,months,plans,records:rows,limits:["Alternative accounts, not joint book","Observed adaptive historical development, not OOS","No intraminute DD or observed-path trace claim","N100 not statistical power"]};
}
```
