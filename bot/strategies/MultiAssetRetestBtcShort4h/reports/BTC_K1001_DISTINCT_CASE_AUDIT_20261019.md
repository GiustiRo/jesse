# K1001 — auditoría de casos discordantes frente a Y902

Nueva auditoría descriptiva solicitada al preguntar si puede declararse ganadora. Sin nuevos backtests y sin inspeccionar2026. Job79b396d478a34632841fcaf67dc032f2,8inputs completos(4anclas+4sesiones). Reutiliza auditor financiero conciliado y produce descomposición desde paths completos. El conteo anterior de5cambios era una distancia simétrica de registros de entrada:3registros previos ausentes y2nuevos. Dos son las mismas señales con fillretrasado. Por tanto corresponden a3situaciones distintas (2retrasos+1no fill), no5casos independientes. EnB/Cson las mismas situaciones, no6pruebasindependientes.

La conciliación separada de metadata de logs completos empareja45suplementos actuales contra46Y902 poranchor/distanciacongelados1e-7yventana fill≤4h, sin colisiones. Sólo2pares cambian fill y1no tiene fill enK1001. El análisis financiero emparejó los registros discordantes por símbolo/lado/bucket4hinclusiverightedge; se comprobó que susidentidades coinciden exactamente conla metadata. No se identifica STOPoriginal por tipo.

|Componente descriptivo|B USDT|C USDT|
|---|---:|---:|
|Dos entradas retrasadas|-34.84|-30.21|
|Una entrada perdedora evitada|170.46|172.99|
|Cantidades distintas en recorridos retenidos|37.35|31.20|
|Total K1001−Y902|172.98|173.98|

Los240/247recorridos retenidos tienen mismo precio de entrada/salida yfecha de salida;su diferencia procede numéricamente de cantidades. Eso es compatible conefectos posteriores de capital/capacidad, pero no identifica causalidad única ni es una simulación de capital contrafactual. Para pares cambiados se separa resultado porunidad al tamaño viejo y componente de cantidad sobre recorrido nuevo. No atribuir toda lacantidad inmediata a capital, porque precioplanificado también afecta sizing. Todos los componentes suman eldelta financiero dentro1e-7.

La pérdida evitada ocurrió en julio2024 y explica casi toda la ventaja;las otras dos entradas fueron retrasadas en2021. El mecanismo es plausible (exigir pérdida de soporte de dosvelas), pero losdatos no bastan para afirmar ausencia desobreajuste. La reiteracióndel caso enfees/TPvecinos no crea nuevos casos. Esta precisión reemplaza cualquierlectura previa de'5operaciones' como5situacionesdistintas; la distanciaoperativa5 de losgatesR9 se conserva como metricadefinida,no se retoca retrospectivamente.

```json
{
  "financial": {
    "B": {
      "old_n": 243,
      "new_n": 242,
      "net_delta": 172.97924343272098,
      "old_entry_records_removed": 3,
      "new_entry_records_added": 2,
      "changed_fill_pairs": [
        {
          "old": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1636574460000,
            "close": 1636761600000,
            "entry": 66625,
            "exit": 64156.08000000001,
            "qty": 0.04,
            "net": 96.40274055999964,
            "fee": 2.3540594400000003,
            "entry_type": "STOP"
          },
          "new": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1636577460000,
            "close": 1636761600000,
            "entry": 65850,
            "exit": 64156.08000000001,
            "qty": 0.04,
            "net": 65.41669055999964,
            "fee": 2.34010944,
            "entry_type": "STOP"
          },
          "net_delta": -30.986050000000006,
          "path_effect_at_old_qty": -30.986050000000006,
          "qty_component_on_new_path": 0
        },
        {
          "old": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1638390240000,
            "close": 1638562740000,
            "entry": 57055.55,
            "exit": 53153.36388607492,
            "qty": 0.059000000000000004,
            "net": 227.30293405790462,
            "fee": 2.9260466636752893,
            "entry_type": "STOP"
          },
          "new": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1638390300000,
            "close": 1638562740000,
            "entry": 57033.29,
            "exit": 53131.10388607492,
            "qty": 0.058,
            "net": 223.4515039272283,
            "fee": 2.8752906804265557,
            "entry_type": "STOP"
          },
          "net_delta": -3.8514301306763343,
          "path_effect_at_old_qty": 0.001182006000021829,
          "qty_component_on_new_path": -3.852612136676356
        }
      ],
      "omitted_entries": [
        {
          "symbol": "BTC-USDT",
          "side": "short",
          "open": 1720815360000,
          "close": 1720864560000,
          "entry": 57446.1,
          "exit": 58656.552115019724,
          "qty": 0.135,
          "net": -170.46427164365036,
          "fee": 7.053236115987448,
          "entry_type": "STOP"
        }
      ],
      "added_entries": [],
      "distinct_discordant_cases": 3,
      "arithmetic_components_USDT": {
        "paired_changed_entries": -34.83748013067634,
        "omitted_old_entries": 170.46427164365036,
        "added_new_entries": 0,
        "retained_entries_delta": 37.35245191974604
      },
      "retained": {
        "count": 240,
        "changed_price_or_exit_paths": 0,
        "path_effect_at_old_qty": 5.338840480817453e-12,
        "quantity_component": 37.35245191974071,
        "by_symbol": {
          "BTC-USDT": 26.446258648173014,
          "PAXG-USDT": 7.6431524397075155,
          "SPY-USDT": 3.26304083186551
        }
      }
    },
    "C": {
      "old_n": 250,
      "new_n": 249,
      "net_delta": 173.97639939104738,
      "old_entry_records_removed": 3,
      "new_entry_records_added": 2,
      "changed_fill_pairs": [
        {
          "old": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1636574460000,
            "close": 1636761600000,
            "entry": 66625,
            "exit": 64156.08,
            "qty": 0.039,
            "net": 93.99267204599992,
            "fee": 2.2952079540000003,
            "entry_type": "STOP"
          },
          "new": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1636577460000,
            "close": 1636761600000,
            "entry": 65850,
            "exit": 64156.08,
            "qty": 0.039,
            "net": 63.78127329599994,
            "fee": 2.281606704,
            "entry_type": "STOP"
          },
          "net_delta": -30.211398749999987,
          "path_effect_at_old_qty": -30.211398749999987,
          "qty_component_on_new_path": 0
        },
        {
          "old": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1638390240000,
            "close": 1638562740000,
            "entry": 57055.55,
            "exit": 53153.36388607492,
            "qty": 0.057,
            "net": 219.59774985255194,
            "fee": 2.8268586411778216,
            "entry_type": "STOP"
          },
          "new": {
            "symbol": "BTC-USDT",
            "side": "short",
            "open": 1638390300000,
            "close": 1638562740000,
            "entry": 57033.29,
            "exit": 53131.10388607492,
            "qty": 0.057,
            "net": 219.59889179055193,
            "fee": 2.8257167031778216,
            "entry_type": "STOP"
          },
          "net_delta": 0.0011419379999892953,
          "path_effect_at_old_qty": 0.0011419379999892953,
          "qty_component_on_new_path": 0
        }
      ],
      "omitted_entries": [
        {
          "symbol": "BTC-USDT",
          "side": "short",
          "open": 1720815360000,
          "close": 1720864560000,
          "entry": 57446.1,
          "exit": 58656.552115019724,
          "qty": 0.137,
          "net": -172.98966826059333,
          "fee": 7.157728502890966,
          "entry_type": "STOP"
        }
      ],
      "added_entries": [],
      "distinct_discordant_cases": 3,
      "arithmetic_components_USDT": {
        "paired_changed_entries": -30.210256811999997,
        "omitted_old_entries": 172.98966826059333,
        "added_new_entries": 0,
        "retained_entries_delta": 31.196987942445098
      },
      "retained": {
        "count": 247,
        "changed_price_or_exit_paths": 0,
        "path_effect_at_old_qty": 1.1526335441658375e-12,
        "quantity_component": 31.196987942443947,
        "by_symbol": {
          "BTC-USDT": 22.644729243849795,
          "PAXG-USDT": 8.406417346756566,
          "SPY-USDT": 0.14584135183874025
        }
      }
    }
  },
  "metadata": {
    "B": {
      "old_fills": 46,
      "new_fills": 45,
      "matched_same_geometry": 45,
      "changed_executed_pairs": [
        {
          "old": {
            "open": 1636574460000,
            "entry": 66625,
            "qty": 0.04,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 66625,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "new": {
            "open": 1636577460000,
            "entry": 65850,
            "qty": 0.04,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 65850,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "changed": true,
          "request_changed": true
        },
        {
          "old": {
            "open": 1638390240000,
            "entry": 57055.55,
            "qty": 0.059000000000000004,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 57055.55,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "new": {
            "open": 1638390300000,
            "entry": 57033.29,
            "qty": 0.058,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 57033.29,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "changed": true,
          "request_changed": true
        }
      ],
      "requested_price_changed_pairs": [
        {
          "old": {
            "open": 1636574460000,
            "entry": 66625,
            "qty": 0.04,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 66625,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "new": {
            "open": 1636577460000,
            "entry": 65850,
            "qty": 0.04,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 65850,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "changed": true,
          "request_changed": true
        },
        {
          "old": {
            "open": 1638390240000,
            "entry": 57055.55,
            "qty": 0.059000000000000004,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 57055.55,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "new": {
            "open": 1638390300000,
            "entry": 57033.29,
            "qty": 0.058,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 57033.29,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "changed": true,
          "request_changed": true
        }
      ],
      "removed": [
        {
          "open": 1720815360000,
          "entry": 57446.1,
          "qty": 0.135,
          "entry_type": "STOP",
          "recipe": "Y902",
          "requested_entry": 57446.1,
          "signal_anchor": 57744.138910250564,
          "distance": 1210.4521150197252,
          "target_distance": 2420.9042300394503
        }
      ],
      "added": [],
      "changed_signal_clusters": 3
    },
    "C": {
      "old_fills": 46,
      "new_fills": 45,
      "matched_same_geometry": 45,
      "changed_executed_pairs": [
        {
          "old": {
            "open": 1636574460000,
            "entry": 66625,
            "qty": 0.039,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 66625,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "new": {
            "open": 1636577460000,
            "entry": 65850,
            "qty": 0.039,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 65850,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "changed": true,
          "request_changed": true
        },
        {
          "old": {
            "open": 1638390240000,
            "entry": 57055.55,
            "qty": 0.057,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 57055.55,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "new": {
            "open": 1638390300000,
            "entry": 57033.29,
            "qty": 0.057,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 57033.29,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "changed": true,
          "request_changed": true
        }
      ],
      "requested_price_changed_pairs": [
        {
          "old": {
            "open": 1636574460000,
            "entry": 66625,
            "qty": 0.039,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 66625,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "new": {
            "open": 1636577460000,
            "entry": 65850,
            "qty": 0.039,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 65850,
            "signal_anchor": 67532.61405315765,
            "distance": 2783.7481237306056,
            "target_distance": 5567.496247461211
          },
          "changed": true,
          "request_changed": true
        },
        {
          "old": {
            "open": 1638390240000,
            "entry": 57055.55,
            "qty": 0.057,
            "entry_type": "STOP",
            "recipe": "Y902",
            "requested_entry": 57055.55,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "new": {
            "open": 1638390300000,
            "entry": 57033.29,
            "qty": 0.057,
            "entry_type": "STOP",
            "recipe": "K1001",
            "requested_entry": 57033.29,
            "signal_anchor": 57570.00685110087,
            "distance": 1951.0930569625416,
            "target_distance": 3902.186113925083
          },
          "changed": true,
          "request_changed": true
        }
      ],
      "removed": [
        {
          "open": 1720815360000,
          "entry": 57446.1,
          "qty": 0.137,
          "entry_type": "STOP",
          "recipe": "Y902",
          "requested_entry": 57446.1,
          "signal_anchor": 57744.138910250564,
          "distance": 1210.4521150197252,
          "target_distance": 2420.9042300394503
        }
      ],
      "added": [],
      "changed_signal_clusters": 3
    }
  }
}
```

## Extensión de análisis añadida al auditor R8 preservado

```python

# Descriptive decomposition: complete executed paths, not a capital counterfactual.
out={}
for p in ("B","C"):
    old=json.loads(Path("output/Y902"+p+"_path.json").read_text())
    new=json.loads(Path("output/K1001"+p+"_path.json").read_text())
    key=lambda t:(t["symbol"],t["side"],t["entry_type"],t["open"])
    om={key(t):t for t in old};nm={key(t):t for t in new}
    removed=[t for k,t in om.items() if k not in nm]
    added=[t for k,t in nm.items() if k not in om]
    bucket=lambda t:(t["symbol"],t["side"],(t["open"]-1)//14400000)
    used=set();paired=[];unpaired_old=[]
    for o in removed:
        hits=[(i,n) for i,n in enumerate(added) if bucket(o)==bucket(n)]
        if len(hits)>1: raise ValueError("Ambiguous unmatched fill bucket")
        if not hits: unpaired_old.append(o);continue
        i,n=hits[0]
        if i in used: raise ValueError("Nonbijective unmatched bucket")
        used.add(i)
        at_old_qty=n["net"]/n["qty"]*o["qty"]
        paired.append({"old":o,"new":n,"net_delta":n["net"]-o["net"],"path_effect_at_old_qty":at_old_qty-o["net"],"qty_component_on_new_path":n["net"]-at_old_qty})
    unpaired_new=[n for i,n in enumerate(added) if i not in used]
    kept=[]
    for k,o in om.items():
        if k not in nm: continue
        n=nm[k];at_old_qty=n["net"]/n["qty"]*o["qty"]
        kept.append({"symbol":n["symbol"],"side":n["side"],"open":n["open"],"same_price_path":abs(n["entry"]-o["entry"])<1e-7 and abs(n["exit"]-o["exit"])<1e-7 and n["close"]==o["close"],"net_delta":n["net"]-o["net"],"path_effect_at_old_qty":at_old_qty-o["net"],"qty_component":n["net"]-at_old_qty})
    delta=sum(t["net"] for t in new)-sum(t["net"] for t in old)
    parts={"paired_changed_entries":sum(t["net_delta"] for t in paired),"omitted_old_entries":-sum(t["net"] for t in unpaired_old),"added_new_entries":sum(t["net"] for t in unpaired_new),"retained_entries_delta":sum(t["net_delta"] for t in kept)}
    if not np.isclose(sum(parts.values()),delta,atol=1e-7,rtol=0): raise ValueError("decomposition mismatch")
    out[p]={"old_n":len(old),"new_n":len(new),"net_delta":delta,"old_entry_records_removed":len(removed),"new_entry_records_added":len(added),"changed_fill_pairs":paired,"omitted_entries":unpaired_old,"added_entries":unpaired_new,"distinct_discordant_cases":len(paired)+len(unpaired_old)+len(unpaired_new),"arithmetic_components_USDT":parts,"retained":{"count":len(kept),"changed_price_or_exit_paths":sum(not t["same_price_path"] for t in kept),"path_effect_at_old_qty":sum(t["path_effect_at_old_qty"] for t in kept),"quantity_component":sum(t["qty_component"] for t in kept),"by_symbol":{s:sum(t["net_delta"] for t in kept if t["symbol"]==s) for s in sorted({t["symbol"] for t in kept})}}}
Path("output/K1001_discordant_case_audit.json").write_text(json.dumps(out,indent=2,allow_nan=False))
print("CASE_AUDIT_SAVED")

```
