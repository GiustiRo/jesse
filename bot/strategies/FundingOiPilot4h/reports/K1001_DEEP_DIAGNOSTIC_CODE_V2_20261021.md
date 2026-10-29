# K1001 — diagnóstico: segunda versión de extracción

Primer job f34e727ae87643b5a6b0f310daf5417d falló por KeyError dashboard_url al componer metadatos del informe. La summary interna del snapshot no contiene ese campo, aunque la respuestaMCP sí lo devuelve. No faltan filas económicas; no se modifica el universo o algoritmo. Se conserva fuente original en K1001_DEEP_DIAGNOSTIC_CODE_20261021.md y fallo íntegro en el recibo final. Única corrección: dashboard_url opcional en snapshot, URL autoritativa se conserva desde la respuestaMCP externa. Todas las aserciones financieras/identidad y los192trades se conservan. No nueva corrida económica.

```python
import json, math, hashlib
from datetime import datetime, timezone

data = json.load(open("inputs/K1001.json"))
metrics = data["metrics"]
trades = data["trades"]
summary = data["summary"]
EXPECTED_SESSION = "94ec00b5-7541-4e9a-b685-a98160e1abd4"
assert summary["session_id"] == EXPECTED_SESSION
assert summary["session_status"] == "finished"
assert len(trades) == 192
assert len({t["id"] for t in trades}) == len(trades)

def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)

def utc_year(timestamp):
    assert number(timestamp)
    return datetime.fromtimestamp(timestamp/1000, timezone.utc).year

def initial_stop_evidence(trade):
    # Price of an executed STOP may be its gap execution price. Without an
    # explicitly exported original submitted trigger, do NOT call it initial SL.
    # No branch label or realized outcome is used to choose an order.
    candidates = []
    for order in trade.get("orders", []):
        if (order.get("reduce_only") is not True
                or order.get("submitted_via") != "stop-loss"
                or order.get("type") != "STOP"
                or order.get("created_at") != trade["opened_at"]):
            continue
        trigger = order.get("submitted_price")
        if not number(trigger) or trigger <= 0:
            continue
        if (not number(order.get("qty"))
                or abs(abs(order["qty"])-abs(trade["qty"])) > 1e-8):
            continue
        if order.get("side") != ("sell" if trade["type"] == "long" else "buy"):
            continue
        candidates.append(order)
    if len(candidates) != 1:
        return {
            "available": False, "reason": "no_unique_exported_initial_trigger",
            "initial_stop": None, "distance": None,
            "price_risk": None, "stop_plus_fees_risk": None,
            "source_order_id": None,
        }
    order = candidates[0]
    stop = float(order["submitted_price"])
    direction = 1 if trade["type"] == "long" else -1
    distance = direction*(trade["entry_price"]-stop)
    if not number(distance) or distance <= 0:
        return {
            "available": False, "reason": "initial_trigger_wrong_side",
            "initial_stop": None, "distance": None,
            "price_risk": None, "stop_plus_fees_risk": None,
            "source_order_id": order.get("id"),
        }
    quantity = abs(trade["qty"])
    return {
        "available": True, "reason": "explicit_initial_submitted_trigger",
        "initial_stop": stop, "distance": distance,
        "price_risk": quantity*distance,
        "stop_plus_fees_risk": quantity*(distance+.00045*(trade["entry_price"]+stop)),
        "source_order_id": order["id"],
    }

def group_rows(rows):
    net = math.fsum(t["net"] for t in rows)
    gross = math.fsum(t["gross_price"] for t in rows)
    fees = math.fsum(t["fee"] for t in rows)
    missing = [t["trade_id"] for t in rows if not t["funding_present"]]
    funding_observed = math.fsum(t["funding"] for t in rows if t["funding_present"])
    losses = -math.fsum(t["net"] for t in rows if t["net"] < 0)
    winners = math.fsum(t["net"] for t in rows if t["net"] > 0)
    return {
        "N": len(rows), "gross_price": gross, "fee": fees, "net": net,
        "funding_observed_fields": funding_observed,
        "funding_missing_field_count": len(missing),
        "funding_missing_trade_ids": missing,
        "positive_trades": sum(t["net"] > 0 for t in rows),
        "negative_trades": sum(t["net"] < 0 for t in rows),
        "zero_trades": sum(t["net"] == 0 for t in rows),
        "pf_net": winners/losses if losses else None,
        "holding_seconds": math.fsum(t["holding_period"] for t in rows),
    }

records = []
for t in trades:
    assert t["symbol"] == "BTC-USDT" and t["type"] in ("long", "short")
    assert all(number(t.get(k)) for k in
               ("entry_price", "exit_price", "qty", "fee", "PNL", "opened_at", "closed_at", "holding_period"))
    assert t["entry_price"] > 0 and t["exit_price"] > 0 and abs(t["qty"]) > 0
    assert t["fee"] >= 0 and t["closed_at"] >= t["opened_at"]
    funding_present = "funding" in t
    assert not funding_present or number(t["funding"])
    direction = 1 if t["type"] == "long" else -1
    gross = (t["exit_price"]-t["entry_price"])*abs(t["qty"])*direction
    # Never infer missing funding from residual PNL or fabricate a zero payment.
    error = gross-t["fee"]+t["funding"]-t["PNL"] if funding_present else None
    assert error is None or abs(error) < 1e-6
    evidence = initial_stop_evidence(t)
    orders = [{
        key: order.get(key) for key in
        ("id", "trade_id", "side", "type", "qty", "price", "submitted_price",
         "status", "created_at", "executed_at", "canceled_at", "reduce_only", "submitted_via")
    } for order in t.get("orders", [])]
    records.append({
        "session_id": EXPECTED_SESSION, "trade_id": t["id"], "origin": None,
        "origin_status": "AWAITING_UNIQUE_R16_LEGACY_OPEN_JOIN",
        "symbol": t["symbol"], "side": t["type"],
        "opened_at": t["opened_at"], "closed_at": t["closed_at"],
        "entry_year_utc": utc_year(t["opened_at"]),
        "close_year_utc": utc_year(t["closed_at"]),
        "entry_price": t["entry_price"], "exit_price": t["exit_price"],
        "qty_abs": abs(t["qty"]), "holding_period": t["holding_period"],
        "gross_price": gross, "fee": t["fee"], "funding_present": funding_present,
        "funding": t["funding"] if funding_present else None,
        "net": t["PNL"], "reconciliation_error_if_funding_present": error,
        "initial_stop_evidence": evidence, "exported_orders": orders,
    })
records.sort(key=lambda x: (x["opened_at"], x["trade_id"]))
overall = group_rows(records)
assert abs(overall["net"]-metrics["net_profit"]) < 1e-6
assert abs(metrics["finishing_balance"]-10000-overall["net"]) < 1e-6
assert abs(overall["fee"]-metrics["fee"]) < 1e-6
# Annual buckets are closed-trade/entry cohorts, not annual MTM returns.
cohorts = {}
for axis in ("entry_year_utc", "close_year_utc"):
    cohorts[axis] = {}
    for year in range(2020, 2026):
        cohorts[axis][str(year)] = {
            side: group_rows([r for r in records if r[axis] == year and (side == "ALL" or r["side"] == side)])
            for side in ("ALL", "long", "short")
        }

result = {
    "status": "DESCRIPTIVE_METADATA_EXTRACT",
    "session_id": EXPECTED_SESSION, "dashboard_url": summary.get("dashboard_url"), "dashboard_url_note": "Optional snapshot metadata; authoritative URL is recorded from the MCP summary outside this analysis",
    "N": len(records), "overall": overall, "yearly_cohorts": cohorts,
    "initial_stop_evidence_available": sum(r["initial_stop_evidence"]["available"] for r in records),
    "origin_assignment": "NONE; root must join complete R16_LEGACY_OPEN logs with unique identity",
    "funding_note": "Missing trade funding fields remain null; observed-field sums are not certified total funding until ledger verification.",
    "limits": "Historical 2% per-trade K1001 book; not new 1%/2/3% lines, standalone CAGR/DD, full MTM attribution, MFE/MAE, censored signals or causal effects.",
}
# Deterministic chunks keep every192 records readable under the artifact128K limit.
# This is transport partitioning, never sampling or selecting economic subsets.
parts = []
for start in range(0, len(records), 64):
    part = records[start:start+64]
    filename = "k1001_trade_metadata_part_" + str(start//64+1) + ".json"
    text = json.dumps(part, separators=(",", ":"), allow_nan=False)
    assert len(text) < 128000
    open("output/"+filename, "w").write(text)
    parts.append({"path": filename, "offset": start, "N": len(part),
                  "sha256_utf8": hashlib.sha256(text.encode()).hexdigest()})
assert sum(p["N"] for p in parts) == 192
result["metadata_parts"] = parts
json.dump(records, open("output/k1001_trade_metadata.json", "w"), indent=2, allow_nan=False)
json.dump(result, open("output/k1001_diagnostic_summary.json", "w"), indent=2, allow_nan=False)
print(json.dumps({"status": result["status"], "N": len(records),
    "net": overall["net"], "funding_missing_fields": overall["funding_missing_field_count"],
    "initial_stop_evidence_available": result["initial_stop_evidence_available"]}, allow_nan=False))

```
