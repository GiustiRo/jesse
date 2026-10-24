# AA — contabilidad y medición final

Estado: NO_CUMPLE en ambas políticas, ninguna candidata. Dos motores ya terminados; este documento recupera auditoría existente y hace aritmética sobre63filas FINAL por cuenta. Cero nuevos análisis o backtests para elaborar el cierre. Protocolo/fuentes permanecen congelados; Hub lo publica root por separado.

Auditoría financiera: job aec51c0c1dd84dd5abaddc4346895e99 succeeded,2026-10-21T22:36:33UTC, inputs COMPLETOS INTERACTION y MAIN_EFFECTS. Artefacto audit.json recuperado por MCP. Fuente exacta ejecutada recibida de root y leída íntegra en BTC_DISCOVERY_AA_ACCOUNTING_SOURCE_20261021.md; incluida al final. El código exacto audita todos los trades, no páginas parciales.

## Resultados conciliados

| Política | Sesión | N | Bruto precioUSDT | FeesUSDT | FundingUSDT | NetoUSDT | FinalUSDT | CAGR% | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| INTERACTION | [registro](http://localhost:9200/#/backtest/7ec2626e-9767-4139-90bc-4bd4d596e755) | 1660 | 8029.855141 | 9863.837069 | -1832.645654 | -3666.627581 | 6333.372419 | -8.383626 | 0.966348 |
| MAIN_EFFECTS | [registro](http://localhost:9200/#/backtest/8b003c2c-4ca3-4cca-9c76-497e2cfa4fb4) | 1635 | 4173.687180 | 8004.707873 | -1651.518131 | -5482.538825 | 4517.461175 | -14.129759 | 0.940396 |

Bruto es suma signed(qty)×(salida−entrada), NO gross_profit del motor (suma de trades netos ganadores). PF usa PNL neto por trade. CAGR usa365días/año y duración exacta UTC2020-10-15→2026-01-01. No confundir retorno total−36,666276%/−54,825388% con CAGR.

Errores completos de conciliación, con tolerancia1e−6USDT:

```json
{
  "INTERACTION": {
    "gross_fee_funding_pnl": 8.185452315956354e-12,
    "pnl_metrics": -2.2737367544323206e-12,
    "terminal_vs_net": 3.410605131648481e-11,
    "funding_vs_metric": -6.366462912410498e-12
  },
  "MAIN_EFFECTS": {
    "gross_fee_funding_pnl": 6.366462912410498e-12,
    "pnl_metrics": -6.366462912410498e-12,
    "terminal_vs_net": -6.366462912410498e-11,
    "funding_vs_metric": -5.002220859751105e-12
  }
}
```

La identidad bruto−fees+funding=PNLsum=final−10000 pasa, igual que funding contra métrica. Ambos tienen funding.applied=true; pagos con marca proxy aplicados2591/2564, sin fingir que todas las marcas sean exactas. Precio bruto fue positivo en ambos libros y no cubrió fees+funding bajo coste nominal. Esto no justifica reducir comisiones, quitar funding o elevar riesgo.

## Terminal flat y resolución de medición

Las summaries conservan raw total_open_trades=1 y open_pl antes de liquidación final. Los logs terminales muestran cierre de la posición SHORT, BUY MARKET ejecutada, Trade closed, Position closed y cancelación del stop; después aparecen63R11_MONTH y R11_SUMMARY de stageFINAL. Se usa FINAL postfee, no PRETERMINAL. Estado final flat acreditado por secuencia/ledger; el contador preterminal no se reinterpreta como una posición real todavía abierta.

| Política | EquityPRETERMINAL | EquityFINAL postfee | DD diario motor% | DD M1+fills% | MarcasM1 | Meses completos | Q completos |
|---|---:|---:|---:|---:|---:|---:|---:|
| INTERACTION | 6336.234718 | 6333.372419 | 66.129839 | 66.857538 | 2741760 | 62 | 20 |
| MAIN_EFFECTS | 4519.502793 | 4517.461175 | 69.744501 | 71.138483 | 2741760 | 62 | 20 |

DD diario es distinto de DD M1+fills y no sustituye el gate r9. Tampoco M1 observa todos los extremos intraminuto. EquityR11=wallet+PnLabierto sin multiplicar otra vez porleverage. Fronteras UTC según fase postfunding/predecisión; no agrupación estricta de todos los eventos en [mesinicio,mesfin). Octubre2020es parcial; noviembre2020–diciembre2025son62mesescompletos.63contribuciones se suman hasta FINAL.

## Puertas vigentes, evaluadas sin redondear

| Gate | Exigido | INTERACTION | MAIN_EFFECTS |
|---|---|---:|---:|
| CAGR | >=30% | -8.383626% FALLA | -14.129759% FALLA |
| PF | >=1.2 | 0.966348 FALLA | 0.940396 FALLA |
| DD M1+fills | <=25% (objetivo20%) | 66.857538% FALLA | 71.138483% FALLA |
| M65 activos | >=65% | 28/62=45.161290% FALLA | 28/62=45.161290% FALLA |
| Q80 completos | >=80% | 8/20=40% FALLA | 6/20=30% FALLA |
| Mediana calendario | >0 | -1.659754% FALLA | -2.533340% FALLA |
| Neto sin2mejoresmeses | >0USDT | -7980.609104 FALLA | -9399.069090 FALLA |
| Npreliminar | >=100 | 1660 CUMPLE | 1635 CUMPLE |

Noperativo no acredita confianza ni potencia. Ambas políticas fallan todas las puertas económicas; sólo conteo cumple. La interacción mejora el neto frente al control en1815.911244USDT y es insuficiente. No se promoverá una mejora relativa de dos cuentas perdedoras.

## Diagnóstico matemático común

Ambas políticas registran EXACTAMENTE el mismo diagnóstico terminal:11423fitsconjuntos válidos;5707gnegativos+0cero+5716gpositivos. Media gRAW=0.005206772334007732, mediaforecastFULL=0.0011282037591482537, MAIN=0.0011196077909556073. Sin errores de agregación. Los counts sólo contienen valid11423, invalid_windowsR11=0; rangos/escalas/admisión no necesitaron fallback.

Estos resúmenes corroboran matemática común, no constituyen auditoría comparativa de cada estado de toda la trayectoria. Datos/labels/ventanas solapados y desarrollo seleccionado: no11423muestras independientes ni signo causal de liquidez. El signo varía casi por mitades y la media es positiva; no afirmar apoyo estable de la narrativa de pendiente menor. No hubo filtro por signo. Que un coeficiente salga negativo en el último fit tampoco valida la receta.

Signals7941/7914, occupied6281/6279 y entradas1660/1635. Señales ocupadas consumidas, no cola. El diagnóstico avanzó antes de hurdle/ocupación/ATR/sizing y no seleccionó trades. PNLlongINTERACTION=875.056341 yshort=-4541.683922USDT; son cortes posteriores. NOcrear long-only ni elegir gnegativa, año, celda, horario, lados o sólo desacuerdos despuésdePnL.

## Años completos2021–2025

Retorno de equity entre fronteras del mismo año; no agrupar por fecha de cierre de trades. Octubre2020 parcial y noviembre/diciembre2020 se conservan en ledger pero no se anuncian como año2020completo.

| Año | INTERACTION% | MAIN_EFFECTS% |
|---|---:|---:|
| 2021 | -8.382285 | -0.608503 |
| 2022 | 1.848672 | -19.139569 |
| 2023 | -39.001663 | -35.261959 |
| 2024 | 20.468099 | 19.044248 |
| 2025 | -24.899466 | -35.635304 |

## 51ventanas móviles12meses completas

Se toman consecutivamente12de los62mesescompletos, noviembre2020→diciembre2025:51ventanas. Retorno=equityfin/ equityinicio−1, no suma aritmética de rentabilidades, sin reinicio de capital. Ventanas solapadas descriptivas; no51OOS, folds independientes o selección de modelo. No se elige una ventana favorable para salvar el libro. Mínimo/máximo INTERACTION -45.793439%/34.333304%; MAIN -54.269535%/30.906858%.

| Primer mes | Último mes | INTERACTION% | MAIN_EFFECTS% |
|---|---|---:|---:|
| 2020-11 | 2021-10 | 31.434516 | 30.906858 |
| 2020-12 | 2021-11 | 11.714569 | 14.819981 |
| 2021-01 | 2021-12 | -8.382285 | -0.608503 |
| 2021-02 | 2022-01 | 1.000594 | 9.563643 |
| 2021-03 | 2022-02 | 4.332814 | -0.549754 |
| 2021-04 | 2022-03 | -2.987089 | -9.530150 |
| 2021-05 | 2022-04 | 0.066974 | -4.702955 |
| 2021-06 | 2022-05 | 7.287853 | -1.308743 |
| 2021-07 | 2022-06 | 16.860686 | 16.589032 |
| 2021-08 | 2022-07 | 14.252353 | 12.086316 |
| 2021-09 | 2022-08 | -2.590599 | -9.995220 |
| 2021-10 | 2022-09 | 12.006722 | 4.077658 |
| 2021-11 | 2022-10 | -0.550701 | -11.864643 |
| 2021-12 | 2022-11 | -7.437154 | -20.290408 |
| 2022-01 | 2022-12 | 1.848672 | -19.139569 |
| 2022-02 | 2023-01 | 2.964233 | -17.342675 |
| 2022-03 | 2023-02 | -9.554787 | -18.540280 |
| 2022-04 | 2023-03 | -6.897718 | -22.734663 |
| 2022-05 | 2023-04 | -14.585119 | -24.578766 |
| 2022-06 | 2023-05 | -25.279039 | -36.166999 |
| 2022-07 | 2023-06 | -43.315648 | -50.160034 |
| 2022-08 | 2023-07 | -44.154228 | -52.443013 |
| 2022-09 | 2023-08 | -42.576701 | -47.621622 |
| 2022-10 | 2023-09 | -45.793439 | -54.269535 |
| 2022-11 | 2023-10 | -44.446532 | -43.716207 |
| 2022-12 | 2023-11 | -41.086546 | -39.154992 |
| 2023-01 | 2023-12 | -39.001663 | -35.261959 |
| 2023-02 | 2024-01 | -43.894256 | -44.011779 |
| 2023-03 | 2024-02 | -25.038551 | -24.120833 |
| 2023-04 | 2024-03 | -25.272970 | -13.382951 |
| 2023-05 | 2024-04 | -37.780137 | -30.079304 |
| 2023-06 | 2024-05 | -32.480707 | -28.248867 |
| 2023-07 | 2024-06 | -25.673297 | -18.502162 |
| 2023-08 | 2024-07 | -26.412489 | -16.835845 |
| 2023-09 | 2024-08 | -14.585426 | -9.888680 |
| 2023-10 | 2024-09 | -11.146586 | 1.730619 |
| 2023-11 | 2024-10 | -2.843749 | -3.843643 |
| 2023-12 | 2024-11 | 21.486061 | 20.235774 |
| 2024-01 | 2024-12 | 20.468099 | 19.044248 |
| 2024-02 | 2025-01 | 34.333304 | 28.120131 |
| 2024-03 | 2025-02 | 1.438236 | -5.284819 |
| 2024-04 | 2025-03 | 4.457608 | -12.944087 |
| 2024-05 | 2025-04 | 7.181220 | -4.676916 |
| 2024-06 | 2025-05 | 3.629013 | 8.644695 |
| 2024-07 | 2025-06 | -0.304452 | -4.167437 |
| 2024-08 | 2025-07 | 8.361670 | 3.555195 |
| 2024-09 | 2025-08 | -2.344450 | -6.462243 |
| 2024-10 | 2025-09 | -4.479605 | -13.635481 |
| 2024-11 | 2025-10 | -13.738773 | -20.460137 |
| 2024-12 | 2025-11 | -20.838919 | -28.797702 |
| 2025-01 | 2025-12 | -24.899466 | -35.635304 |

## 63contribuciones mensuales FINAL

Todas activas; octubre2020 es el único intervalo parcial. Las62filas completas entran a mediana calendario; no se excluyen inactivos aunque en esta muestra no loshay. PNLmes incluye variaciónMTM de posiciones mantenidas según convenciónR11; no sólo tradescerrados. Se comprueba continuidad temporal y cociente de equity sin redondear, tolerancia1e−10 para retorno y1e−6USDT para neto. JSON conserva precisión completa y equidades de cada extremo.

| Mes | Completo | INTERACTION PNLUSDT | Retorno% | MAIN PNLUSDT | Retorno% |
|---|---|---:|---:|---:|---:|
| 2020-10 | no | -78.537410 | -0.785374 | -656.266214 | -6.562662 |
| 2020-11 | sí | 1438.034020 | 14.494174 | 1122.379188 | 12.012106 |
| 2020-12 | sí | 939.427540 | 8.269975 | 865.544924 | 8.269975 |
| 2021-01 | sí | -266.504746 | -2.166895 | -244.849882 | -2.160760 |
| 2021-02 | sí | 838.403473 | 6.967871 | 772.514387 | 6.967870 |
| 2021-03 | sí | 539.948521 | 4.195136 | 497.514654 | 4.195136 |
| 2021-04 | sí | 259.766189 | 1.936997 | -190.821724 | -1.544260 |
| 2021-05 | sí | 13.678930 | 0.100061 | 279.271476 | 2.295505 |
| 2021-06 | sí | 787.405044 | 5.754111 | 17.603377 | 0.141446 |
| 2021-07 | sí | -902.690841 | -6.237662 | -505.565068 | -4.056564 |
| 2021-08 | sí | 442.617552 | 3.261993 | 797.038869 | 6.665695 |
| 2021-09 | sí | -1556.807712 | -11.110890 | -1185.751101 | -9.296827 |
| 2021-10 | sí | 585.485797 | 4.700907 | 662.975391 | 5.730811 |
| 2021-11 | sí | -350.013694 | -2.684108 | -214.399322 | -1.752833 |
| 2021-12 | sí | -1422.219385 | -11.207215 | -754.484573 | -6.278378 |
| 2022-01 | sí | 884.821741 | 7.852523 | 884.406369 | 7.852522 |
| 2022-02 | sí | 1275.676692 | 10.496965 | -352.985465 | -2.905921 |
| 2022-03 | sí | -418.311968 | -3.115108 | -614.913337 | -5.213726 |
| 2022-04 | sí | 669.513545 | 5.146075 | 414.641136 | 3.709037 |
| 2022-05 | sí | 1001.808813 | 7.323328 | 688.556910 | 5.938983 |
| 2022-06 | sí | 2230.134062 | 15.190095 | 2247.952991 | 18.302214 |
| 2022-07 | sí | -1408.813500 | -8.330439 | -1127.837727 | -7.761938 |
| 2022-08 | sí | -1854.257425 | -11.960773 | -1922.988018 | -14.347953 |
| 2022-09 | sí | 301.581393 | 2.209620 | 560.804147 | 4.885250 |
| 2022-10 | sí | -981.732988 | -7.037438 | -1259.987452 | -10.464715 |
| 2022-11 | sí | -1221.991610 | -9.422830 | -1201.501614 | -11.145289 |
| 2022-12 | sí | -270.120482 | -2.299598 | -471.781023 | -4.925235 |
| 2023-01 | sí | 1036.751163 | 9.033844 | 933.405546 | 10.249239 |
| 2023-02 | sí | -367.624758 | -2.937930 | -433.015445 | -4.312698 |
| 2023-03 | sí | -32.653675 | -0.268856 | -969.805651 | -10.094297 |
| 2023-04 | sí | -428.280503 | -3.535775 | 106.571310 | 1.233799 |
| 2023-05 | sí | -714.334270 | -6.113523 | -903.996181 | -10.338206 |
| 2023-06 | sí | -1383.908098 | -12.615205 | -598.302881 | -7.631190 |
| 2023-07 | sí | -928.580351 | -9.686585 | -868.090813 | -11.987012 |
| 2023-08 | sí | -820.214585 | -9.473848 | -361.041751 | -5.664433 |
| 2023-09 | sí | -275.561793 | -3.515959 | -506.691368 | -8.426885 |
| 2023-10 | sí | -357.491115 | -4.727534 | 561.488063 | 10.197556 |
| 2023-11 | sí | -284.180644 | -3.944541 | -239.338643 | -3.944541 |
| 2023-12 | sí | 80.130151 | 1.157913 | 67.486085 | 1.157913 |
| 2024-01 | sí | 20.188283 | 0.288389 | -274.255204 | -4.651752 |
| 2024-02 | sí | 2083.847461 | 29.682148 | 1668.577274 | 29.682147 |
| 2024-03 | sí | -52.872323 | -0.580734 | 191.620878 | 2.628522 |
| 2024-04 | sí | -1781.440495 | -19.681127 | -1367.658119 | -18.280088 |
| 2024-05 | sí | 136.898103 | 1.883035 | -488.569937 | -7.990971 |
| 2024-06 | sí | -281.829526 | -3.804921 | 276.560276 | 4.916230 |
| 2024-07 | sí | -754.179932 | -10.584767 | -601.266880 | -10.187485 |
| 2024-08 | sí | 323.365426 | 5.075612 | 117.461488 | 2.215942 |
| 2024-09 | sí | 24.671501 | 0.368543 | 183.184402 | 3.380903 |
| 2024-10 | sí | 280.526831 | 4.175127 | 232.981807 | 4.159354 |
| 2024-11 | sí | 1407.577858 | 20.109610 | 1173.270117 | 20.109609 |
| 2024-12 | sí | 26.086015 | 0.310285 | 10.893169 | 0.155447 |
| 2025-01 | sí | 997.732912 | 11.831023 | 183.714272 | 2.617557 |
| 2025-02 | sí | -195.593765 | -2.073962 | -297.458062 | -4.130070 |
| 2025-03 | sí | 219.666175 | 2.378541 | -391.547998 | -5.670668 |
| 2025-04 | sí | -1662.841453 | -17.586905 | -685.170414 | -10.519644 |
| 2025-05 | sí | -116.381989 | -1.493579 | 283.681228 | 4.867493 |
| 2025-06 | sí | -572.322252 | -7.456215 | -455.705864 | -7.456216 |
| 2025-07 | sí | -199.768197 | -2.812269 | -166.852239 | -2.949977 |
| 2025-08 | sí | -366.298849 | -5.305846 | -421.128298 | -7.671943 |
| 2025-09 | sí | -119.367987 | -1.825929 | -230.454718 | -4.547188 |
| 2025-10 | sí | -380.137800 | -5.922979 | -196.962427 | -4.071476 |
| 2025-11 | sí | 617.277135 | 10.223410 | 348.950443 | 7.519423 |
| 2025-12 | sí | -321.783785 | -4.835105 | -472.143590 | -9.462545 |

SumaPnLmensual−netoauditado: INTERACTION 3.410605131648481e-11USDT; MAIN -6.366462912410498e-11USDT. EquityFINAL coincide. No se usan PRETERMINALmonth para eliminar fee final.

## Código exacto de auditoría financiera YA ejecutado

La siguiente copia es íntegra del archivo recibido/leído porMCP; NO se ha vuelto a ejecutar ni reformatear su código:

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

## Reconstrucción documental de meses/años/ventanas

La aritmética siguiente se ejecutó en functions.exec exclusivamente sobre filasR11FINAL ya leídas; sin run_analysis, datos de mercado, scripts persistentes o nuevos motores. No se confunde con el job financiero anterior. El JSON conserva las63filas FINAL y63contrapartesPRETERMINAL por cada libro juntoalapágina terminal y resúmenes; sólo FINAL entra aquí.

```javascript
// Mechanical arithmetic over the63 FINAL R11_MONTH records per account.
// No sessions, candles, strategy/model changes or analysis jobs are created.
function reconstruct(months, audit, summary) {
  if(months.length!==63) throw Error("63 FINAL months required");
  const complete=months.filter(m=>m.complete);
  if(complete.length!==62) throw Error("62 complete months required");
  let capital=10000;
  for(let i=0;i<months.length;i++){
    const m=months[i];
    if(i && m.start!==months[i-1].finish) throw Error("noncontiguous months");
    if(Math.abs((capital+m.pnl)/capital-1-m.return_fraction)>1e-10) throw Error("return mismatch");
    m.equity_start=capital; capital+=m.pnl; m.equity_finish=capital;
  }
  const sum=months.reduce((s,m)=>s+m.pnl,0);
  if(Math.abs(sum-audit.net)>1e-6||Math.abs(capital-audit.finish)>1e-6) throw Error("monthly ledger mismatch");
  const annual=[];
  for(let year=2021;year<=2025;year++){
    const mm=months.filter(m=>m.month.startsWith(String(year)));
    if(mm.length!==12||mm.some(m=>!m.complete)) throw Error("incomplete year");
    annual.push({year,months:12,equity_start:mm[0].equity_start,equity_finish:mm.at(-1).equity_finish,
      pnl:mm.reduce((s,m)=>s+m.pnl,0),return_pct:100*(mm.at(-1).equity_finish/mm[0].equity_start-1)});
  }
  const windows=[];
  for(let i=0;i+12<=complete.length;i++){
    const mm=complete.slice(i,i+12);
    windows.push({start_month:mm[0].month,finish_month:mm.at(-1).month,
      return_pct:100*(mm.at(-1).equity_finish/mm[0].equity_start-1)});
  }
  const gates={CAGR30:audit.cagr_pct>=30,PF1_2:audit.pf>=1.2,DD25:-summary.dd_m1_events*100<=25,
    M65:summary.positive_active/summary.active_months>=.65,Q80:summary.positive_quarters/summary.complete_quarters>=.8,
    median_positive:summary.median_return>0,excluding_best2_positive:summary.pnl_without_best_two>0,N100:audit.N>=100};
  return {annual,windows12m:windows,window_count:windows.length,
    window_min:Math.min(...windows.map(x=>x.return_pct)),window_max:Math.max(...windows.map(x=>x.return_pct)),
    gates,monthly_sum_error:sum-audit.net,capital_terminal_error:capital-audit.finish};
}
```

## Cierre, presupuesto y evidencia

Dos económicas completadas, cero errores/reemplazos económicos; cierre NO_CUMPLE/ninguna candidata. Preservar técnica:129checksfinales, primer fallo sólo deharnessASTResearch ycorrecciónprevia deguardparidadprecio conservados enrecibo; no sumarloscomoeconomías.

Cerrar sin vecinos de baseline42,408/360/warmup420,horizonte,normalización,interacción/grado,rank/rcond,regularización,coeficientes,signos,horarios,lados,filtros,riesgo,gestión/costes. No promover long-only de corte posterior. No abrir2026, stress o nuevosdatasets para rescatarAA. Fuentes/protocolo congelados, sin modificarHub por este agente; rootpublicará conclusión y continuidad.

Evidencia duradera: BTC_DISCOVERY_AA_ACCOUNTING_20261021.json contiene auditcode/job/artifact íntegros, summaries/formularios, página terminal observada, todosregistrosFINAL/PRETERMINAL, anuales,51ventanas/gates y fórmuladocumental. BTC_DISCOVERY_AA_FINAL_20261021.md resume veredicto. CODES/PROTOCOLO/MANIFESTyTECHNICAL_CHECK_RECEIPT conservan reglas y fuentes previas; no editar después del resultado. Sin afirmación de OOS o ejecuciónreal.
