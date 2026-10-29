# Código literal A, snapshotV3

```python
EXPECTED_NAMES = ["A_ACCEPTED","A_CLOSE_ONLY"]
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
