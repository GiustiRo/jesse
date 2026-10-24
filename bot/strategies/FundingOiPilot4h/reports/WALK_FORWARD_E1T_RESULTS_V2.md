# Walk-forward V2: entrenamiento E1
Fecha: 2026-10-20.
Estado: E1_TRAIN_COMPLETE_SELECTION_RECORDED. Selección: **SIN_CANDIDATA**.

## Alcance
Entrenamiento [2020-09-01,2022-01-01), 16 meses. Dos backtests ATR nuevos y dos controles fijos V1 reutilizados, con fuente/config/datasets/fechas previamente verificados. Capital 10.000 USDT por sesión, aislado3x, riesgo presupuestado2% stop+fees con cap notional C, fee0,00045 por lado, slippage nominal0, funding histórico contable ON. OI sólo en POI. Las fuentes y hashes efectivos están en REGISTRY_V2.json.
No se inició ni consultó evaluación ATR E1V. Sus controles fijos ya se observaron en V1; no se afirma independencia de desarrollo. 2024–2025 y 2026 no se abrieron.

## Decisión previa a evaluación nueva
Guardada 2026-10-20T22:33:49.399Z UTC en WALK_FORWARD_E1_SELECTION_V2.md.
Gates: >=30 trades, neto>0, PF>=1,2 y absDD<=25%. Las cuatro pasan cantidad y fallan los otros tres.
No se ordenan variantes no elegibles para operar ni se flexibilizan gates por un resultado cercano a cero.
El selector E1 queda plano durante [2022-01-01,2022-07-01): retorno convencional0, sin exposición, PF indefinido. Las futuras evaluaciones de las ablaciones son investigación diagnóstica; no se incorporan como trades seleccionados.
E1 sin candidata no equivale a rechazo final V2: aún faltan E1V y E2–E4.

## Resultados de entrenamiento
| Configuración / sesión | Trades | Neto % | PF | DD motor % | Turnover / capital inicial |
|---|---:|---:|---:|---:|---:|
| [H1_FIXED_P](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770) | 284 | -28.63 | 0.907 | -42.72 | 513.48 |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644) | 212 | -6.83 | 0.973 | -33.94 | 439.19 |
| [H1_ATR_P](http://localhost:9200/#/backtest/5d77182b-2071-4056-a11f-4f7c5d5ef12f) | 263 | -12.69 | 0.928 | -31.19 | 240.56 |
| [H1_ATR_POI](http://localhost:9200/#/backtest/8e030d85-6762-42d7-91ef-546ca2a6b340) | 198 | -0.20 | 0.999 | -29.08 | 205.72 |

| Configuración | Precio bruto USDT | Fees | Funding | Neto USDT | Eventos funding |
|---|---:|---:|---:|---:|---:|
| H1_FIXED_P | -79.12 | 2310.65 | -473.49 | -2863.25 | 421 |
| H1_FIXED_POI | 1655.69 | 1976.35 | -362.65 | -683.31 | 314 |
| H1_ATR_P | 219.16 | 1082.50 | -405.17 | -1268.51 | 690 |
| H1_ATR_POI | 1227.85 | 925.74 | -322.06 | -19.94 | 521 |

ATR redujo pérdidas y DD frente al control de igual uso OI en este entrenamiento, con menos notional negociado y menores fees. No alcanzó los umbrales; no extrapolar a evaluación. La distancia y sizing asociados también cambian ocupación y entradas posteriores; no atribuir la diferencia sólo al stop entre trades idénticos.
ATR_POI ganó por precio +1.227,85, pagó925,74 de fees y322,06 de funding, terminando −19,94 USDT. Su lado long +2.072,52 y short −2.092,47 no autoriza eliminar shorts después de observar el resultado.

## Dirección
| Configuración | Dirección | N | Bruto | Fees | Funding | Neto |
|---|---|---:|---:|---:|---:|---:|
| H1_FIXED_P | long | 163 | 1741.16 | 1352.69 | -630.02 | -241.55 |
| H1_FIXED_P | short | 121 | -1820.27 | 957.96 | 156.53 | -2621.70 |
| H1_FIXED_POI | long | 124 | 2148.04 | 1166.79 | -512.41 | 468.85 |
| H1_FIXED_POI | short | 88 | -492.35 | 809.56 | 149.76 | -1152.15 |
| H1_ATR_P | long | 154 | 2227.64 | 672.35 | -573.62 | 981.66 |
| H1_ATR_P | short | 109 | -2008.47 | 410.15 | 168.45 | -2250.17 |
| H1_ATR_POI | long | 116 | 3115.10 | 570.07 | -472.52 | 2072.52 |
| H1_ATR_POI | short | 82 | -1887.25 | 355.67 | 150.46 | -2092.47 |

## Auditoría de las dos sesiones nuevas
Cada una registra2.922 decisiones4h y64 buckets (16meses × all/long/short/none). Se verificó partición exclusiva por bucket y allowed=entradas=trades; salidas concilian sin cierre forzado posterior.
ATR_P: 263 entradas y263 salidas; 263 oportunidades aceptadas. No hubo rechazo atr_invalid ni distance_invalid ni qty_invalid; ningún flag atr_invalid en oportunidades. El gate OI está apagado y sus flags informativos no bloquean.
ATR_POI: 198 entradas y198 salidas. Rechazos exclusivos OI: inicialización4, no creciente184 y stale2. Los denominadores son oportunidades de esa trayectoria; no representan el mismo conjunto que P por distinta ocupación.
Salidas ejecutadas:
- ATR_P: MARKET189, STOP55, LIMIT19.
- ATR_POI: MARKET144, STOP39, LIMIT15.
Esto ejercita ejecuciones protectoras ATR que no ocurrieron en los smokes cortos, sin errores runtime. No hubo cierre forzado al borde ni invalid_after_fill; no afirmar cobertura de esas ramas.
Auditorías completas de buckets en AUDIT_ResearchV2_H1_ATR_P_E1T.json y AUDIT_ResearchV2_H1_ATR_POI_E1T.json. Los archivos incluyen una cola de logs suficiente para todos los buckets y procedencia, no todo el histórico de entradas.
Comparación y conciliación: run_analysis 167602b5b53c43079d0778bd52dfe83c, con snapshots íntegros de las cuatro sesiones (no páginas parciales). Bruto−fees+ledger=PNL, fee sobre fills, funding por trade y saldo final conciliaron; error máximo 2.000888e-11 USDT, tolerancia1e-6.
Las dos nuevas ejecuciones motor duraron12,13 y11,39 segundos; no equivale a tiempo de pared de orquestación.
Las curvas mensuales usan el último valor diario disponible del mes con etiquetas de00:00/00:01 referidas al día previo mediante61segundos, excepto saldo inicial. Resolución diaria aproximada de borde hasta1min; no máximo drawdown intraminuto del índice. El DD arriba es métrica del motor. Se conserva la política usada en V1; no se fabrican puntos intradía.

## Meses completos
| Mes | FIXED_P % | FIXED_POI % | ATR_P % | ATR_POI % |
|---|---:|---:|---:|---:|
| 2020-09 | -1.41 | -3.05 | -4.63 | -1.47 |
| 2020-10 | 2.66 | 4.73 | 1.43 | 6.40 |
| 2020-11 | 19.50 | 14.51 | 10.92 | 7.61 |
| 2020-12 | -3.76 | 5.18 | 10.86 | 13.04 |
| 2021-01 | 4.28 | 13.06 | -0.12 | 5.67 |
| 2021-02 | -18.60 | -16.15 | -4.67 | -4.23 |
| 2021-03 | 7.40 | -1.53 | -1.69 | -3.13 |
| 2021-04 | -4.46 | -7.14 | -1.95 | -4.12 |
| 2021-05 | -17.41 | -1.38 | -8.45 | 0.99 |
| 2021-06 | 0.27 | 3.08 | -1.81 | -0.97 |
| 2021-07 | 2.38 | -3.68 | -4.66 | -5.23 |
| 2021-08 | -10.89 | -3.38 | -5.18 | -5.06 |
| 2021-09 | -3.42 | -5.79 | -2.78 | -2.16 |
| 2021-10 | 7.71 | 9.38 | 5.46 | 3.43 |
| 2021-11 | 2.04 | 0.14 | 3.19 | -1.68 |
| 2021-12 | -12.22 | -9.96 | -6.98 | -7.00 |

## Límites y continuidad
Éste es entrenamiento observado, no validación independiente. PF y DD incumplen gates incluso sin slippage. OI sigue retrospectivo sin certificación point-in-time; funding usa marcas proxy. No afirmar ejecución real, liquidez ni rentabilidad futura.
Sin cambios de reglas, código o parámetros durante este lote. No pruebas2026, instalaciones, reinicio, cuentas, Pi, ML, RST, live/paper, commit ni push.
Consumo V2: dos sesiones económicas nuevas finalizadas; los controles no se reejecutaron; cuatro smokes previos. No se usa la reserva V1 para tuning.
Próximo lote definido: dos evaluaciones ATR E1V [2022-01-01,2022-07-01) conservando la selección plana ya registrada. No elegir retrospectivamente al ganador de ese semestre para el selector.

## Fuente del análisis
Lee exclusivamente snapshots de inputs/ y escribe output/. No importa código del proyecto ni consulta DB/red.
```python
import json, math
from pathlib import Path
from datetime import datetime, timezone
rows=[]
for p in sorted(Path("inputs").glob("s*.json")):
 d=json.load(open(p)); s=d["summary"]; m=d["metrics"]; trades=d["trades"]
 assert s["session_status"]=="finished"
 assert s["form"]["start_date"]=="2020-09-01" and s["form"]["finish_date"]=="2022-01-01"
 ledger=m.get("funding",{}).get("ledger",[])
 errors=[]; stats={}; prices=fees=funding=turnover=holding=0.
 ordered=sorted(trades,key=lambda t:t["opened_at"]); capital=10000.
 pnls=[]; exit_types={}
 for t in ordered:
  sign=1 if t["type"]=="long" else -1
  gross=sign*(t["exit_price"]-t["entry_price"])*t["qty"]
  cf=math.fsum(x["cashflow"] for x in ledger if x["trade_id"]==t["id"])
  errors.extend([abs(gross-t["fee"]+cf-t["PNL"]),abs(cf-t.get("funding",0))])
  executed=[o for o in t["orders"] if o["status"]=="EXECUTED"]
  errors.append(abs(math.fsum(abs(o["filled_qty"])*o["price"]*.00045 for o in executed)-t["fee"]))
  for o in executed:
   turnover+=abs(o["filled_qty"])*o["price"]
   if o["reduce_only"]: exit_types[o["type"]]=exit_types.get(o["type"],0)+1
  prices+=gross;fees+=t["fee"];funding+=cf;holding+=t["holding_period"];pnls.append(t["PNL"])
  side=stats.setdefault(t["type"],dict(n=0,gross=0.,fees=0.,funding=0.,net=0.))
  side["n"]+=1;side["gross"]+=gross;side["fees"]+=t["fee"];side["funding"]+=cf;side["net"]+=t["PNL"]
  capital+=t["PNL"]
 net=math.fsum(pnls); positive=math.fsum(x for x in pnls if x>0);negative=math.fsum(x for x in pnls if x<0)
 pf=positive/abs(negative) if negative else None
 errors.extend([abs(net-(m.get("net_profit") or 0)),abs(fees-(m.get("fee") or 0)),abs(funding-m.get("funding",{}).get("cashflow",0))])
 if trades:errors.append(abs(10000+net-m["finishing_balance"]))
 assert max(errors,default=0)<1e-6
 dd=abs(m.get("max_drawdown") or 0)
 pf_pass=bool((pf is not None and pf>=1.2) or (negative==0 and positive>0))
 eligible=bool(len(trades)>=30 and net>0 and pf_pass and dd<=25)
 start=datetime.fromisoformat(s["form"]["start_date"]).replace(tzinfo=timezone.utc).timestamp()
 balances={}
 for curve in d["equity_curve"]:
  if curve["name"]=="Portfolio":
   for pt in sorted(curve["data"],key=lambda x:x["time"]):
    stamp=pt["time"]-61 if pt["time"]>start else pt["time"]
    month=datetime.fromtimestamp(stamp,timezone.utc).strftime("%Y-%m")
    balances[month]=pt["value"]
 previous=10000.;months=[]
 for month,b in sorted(balances.items()):
  months.append(dict(month=month,return_pct=(b/previous-1)*100,end_equity=b));previous=b
 rows.append(dict(session_id=s["session_id"],strategy=s["form"]["routes"][0]["strategy"],n=len(trades),
  net=net,net_pct=net/100,pf=pf,pf_no_losses=negative==0 and positive>0,dd=-dd,turnover=turnover/10000,
  gross_price=prices,fees=fees,funding=funding,funding_events=len(ledger),holding_seconds=holding,
  directions=stats,months=months,exit_order_types=exit_types,eligible=eligible,
  gate_failures=[name for name,passed in [("trades>=30",len(trades)>=30),("net>0",net>0),("PF>=1.2",pf_pass),("absDD<=25%",dd<=25)] if not passed],
  max_accounting_error=max(errors,default=0)))
json.dump(rows,open("output/e1_train.json","w"),indent=2)
print(json.dumps(rows))

```
