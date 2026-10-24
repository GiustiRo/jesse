# Auditoría prevista de único MARKET nativo

Se ejecutará sólo tras completar el único motor aprobado. Exporta todos los trades en partes<48.000caracteres y summary<50.000con whitelist de metadatafunding, evitando el artifact gigantesco de la auditoría anterior. Verifica todas las entradas reales MARKET concreated_at=executed_at=opened_at yprecioigualentry; no toma order_kindcomo prueba. Ledger completo de pagos y trazas se recuperará porMCP y unirá mecánicamente. Reutiliza control previamente auditado, sin nueva réplica.

```python
import json, math, sys, platform, hashlib
from datetime import datetime, timezone
results = {}
for name in ("MARKET",):
    path = "inputs/" + name + ".json"
    raw = open(path, "rb").read()
    data = json.loads(raw)
    summary, metrics, trades = data["summary"], data["metrics"], data["trades"]
    assert summary["session_status"] == "finished"
    assert len({t["id"] for t in trades}) == len(trades)
    assert metrics["total_open_trades"] == 0
    rows = []
    for t in trades:
        assert t["symbol"] == "BTC-USDT"
        assert t["type"] in ("long", "short")
        assert all(math.isfinite(float(t[k])) for k in
            ("entry_price","exit_price","qty","fee","PNL","opened_at","closed_at","holding_period"))
        assert t["entry_price"] > 0 and t["exit_price"] > 0 and abs(t["qty"]) > 0
        assert t["closed_at"] >= t["opened_at"] and t["fee"] >= 0
        direction = 1 if t["type"] == "long" else -1
        gross = direction*(t["exit_price"]-t["entry_price"])*abs(t["qty"])
        expected_fee = .00045*abs(t["qty"])*(t["entry_price"]+t["exit_price"])
        assert abs(expected_fee-t["fee"]) < 1e-6
        present = "funding" in t
        if present:
            assert math.isfinite(t["funding"])
            assert abs(gross-t["fee"]+t["funding"]-t["PNL"]) < 1e-6
        rows.append(dict(trade_id=t["id"], side=t["type"], opened_at=t["opened_at"],
            closed_at=t["closed_at"], entry=t["entry_price"], exit=t["exit_price"],
            qty=abs(t["qty"]), fee=t["fee"], gross=gross, net=t["PNL"],
            funding_present=present, funding=t.get("funding"),
            holding_period=t["holding_period"], orders=t.get("orders", [])))
    assert all(r["side"] == "long" for r in rows)
    for row in rows:
        entries = [o for o in row["orders"] if o.get("status") == "EXECUTED" and not o.get("reduce_only") and o.get("side") == "buy"]
        assert len(entries) == 1
        entry = entries[0]
        assert entry["type"] == "MARKET"
        assert entry["executed_at"] == entry["created_at"] == row["opened_at"]
        assert abs(entry["price"]-row["entry"]) < 1e-7
    net = math.fsum(r["net"] for r in rows)
    fee = math.fsum(r["fee"] for r in rows)
    gross = math.fsum(r["gross"] for r in rows)
    assert abs(net-metrics["net_profit"]) < 1e-6
    assert abs(fee-metrics["fee"]) < 1e-6
    assert abs(metrics["finishing_balance"]-10000-net) < 1e-6
    assert metrics["funding"]["applied"] is True
    assert metrics["funding"]["dataset_id"] == "9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571"
    # Missing per-trade funding is NOT assumed zero. Root joins the complete
    # persisted payment ledger by trade_id before accepting full reconciliation.
    missing = [r["trade_id"] for r in rows if not r["funding_present"]]
    losses = -math.fsum(r["net"] for r in rows if r["net"] < 0)
    winners = math.fsum(r["net"] for r in rows if r["net"] > 0)
    window_days = (datetime(2026,1,1,tzinfo=timezone.utc)-datetime(2020,10,15,tzinfo=timezone.utc)).total_seconds()/86400
    cagr = (metrics["finishing_balance"]/10000)**(365/window_days)-1
    pieces = []
    current = []
    for row in rows:
        trial = current + [row]
        if len(json.dumps(trial,separators=(",",":"))) > 48000 and current:
            pieces.append(current)
            current = [row]
        else:
            current = trial
    if current:
        pieces.append(current)
    exports = []
    for i, piece in enumerate(pieces):
        filename = name + "_trades_" + str(i) + ".json"
        content = json.dumps(piece, separators=(",",":"), allow_nan=False)
        assert len(content) < 60000, "one trade exceeds bounded transport"
        open("output/"+filename,"w").write(content)
        exports.append(dict(path="output/"+filename, count=len(piece),
            characters=len(content), sha256=hashlib.sha256(content.encode()).hexdigest()))
    results[name] = dict(session_id=summary["session_id"], N=len(rows), net=net, gross=gross,
        fee=fee, funding_metrics={k: metrics["funding"].get(k) for k in ("mode","dataset_id","cashflow","event_count","settlements_processed","mark_price_proxy_count","status","applied","scope","effective_fast_mode","boundary_policy","publication_delay_ms")}, funding_missing_trade_ids=missing,
        funding_observed_fields=math.fsum(r["funding"] for r in rows if r["funding_present"]),
        finish=metrics["finishing_balance"], cagr_pct=100*cagr,
        pf_net=winners/losses if losses else None, daily_dd_pct=metrics["max_drawdown"],
        snapshot_sha256=hashlib.sha256(raw).hexdigest(), exports=exports)
runtime = dict(python=sys.version, implementation=platform.python_implementation())
out = dict(status="SNAPSHOT_ACCOUNTING_PENDING_FULL_PAYMENT_LEDGER_AND_LOGS",
           runtime=runtime, scenarios=results)
encoded_summary = json.dumps(out,indent=2,allow_nan=False)
assert len(encoded_summary) < 50000, "summary must remain bounded"
open("output/snapshot_accounting.json","w").write(encoded_summary)
print(json.dumps({k:dict(N=v["N"],net=v["net"],parts=len(v["exports"]),
    missing_funding=len(v["funding_missing_trade_ids"])) for k,v in results.items()}))

```
