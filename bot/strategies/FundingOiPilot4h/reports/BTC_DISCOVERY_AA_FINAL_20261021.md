# BTC Discovery AA — cierre sin candidata

[INTERACTION](http://localhost:9200/#/backtest/7ec2626e-9767-4139-90bc-4bd4d596e755) · [MAIN_EFFECTS](http://localhost:9200/#/backtest/8b003c2c-4ca3-4cca-9c76-497e2cfa4fb4).

AA preguntó si volumen relativo modifica la respuesta predictiva a un retornoBTC4h con signo, por encima de efectos principales de retorno y volumen. Dos OLS directos24h: INTERACTION añade r·v; MAIN_EFFECTS conserva intercepto,r,v. Mismos360orígenes maduros, baseline42volúmenes anteriores propio de cada origen,408filas, current407, warmup420, escalas compartidas y admisión conjunta rank4/3. No causalidad de liquidez identificada ni réplica del estudio diario de acciones. Diseño fijado antes de consultar resultadosY; fuentes/protocolo permanecen congelados.

BTC-USDT Binance Perpetual Futures, UTC[2020-10-15,2026-01-01), desarrollo histórico ampliamente reutilizado.10.000USDT,2%portrade/6%agregado/3xaislado,fee.00045porlado,fundingBTC histórico aplicado con proxiesdeclarados,slippage0. Stop2ATR14simple actual, sinTP y24hdesde fill, entradaMARKET a precioactual; R10/R11/R12ARintactos. Sinstress,riskvariants o nuevaeconomía2026.

| Política | N | NetoUSDT | CAGR% | PF | DD M1+fills% | M positivos/activos | Q positivos | Mediana mensual% | Neto sin2mejoresmeses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| INTERACTION | 1660 | -3666.627581 | -8.383626 | 0.966348 | 66.857538 | 28/62 | 8/20 | -1.659754 | -7980.609104 |
| MAIN_EFFECTS | 1635 | -5482.538825 | -14.129759 | 0.940396 | 71.138483 | 28/62 | 6/20 | -2.533340 | -9399.069090 |

**Veredicto: NO_CUMPLE en ambas; ninguna candidata.** Fallan CAGR30,PF1.2,DD25,M65,Q80,mediana positiva y neto positivo sin los dos mejores meses; sólo cumplen N100preliminar. El conteo no confiere potencia o confianza. INTERACTION mejora relativamente 1815.911244USDT al control, pero ambas cuentas pierden y superan holgadamente el riesgo tolerable. No basta mejorar a un control malo.

Precio bruto 8029.855141/4173.687180USDT; fees 9863.837069/8004.707873 y funding -1832.645654/-1651.518131. CapitalFINAL 6333.372419/4517.461175USDT. El bruto positivo no cubrió costes nominales; no retirar costes o subir exposición para salvarlo.

Años completos2021–2025, retorno de equity por fronterasR11:
- INTERACTION: 2021:-8.382285%, 2022:1.848672%, 2023:-39.001663%, 2024:20.468099%, 2025:-24.899466%.
- MAIN_EFFECTS: 2021:-0.608503%, 2022:-19.139569%, 2023:-35.261959%, 2024:19.044248%, 2025:-35.635304%.

Las51ventanas12meses completas dan mínimo/máximo -45.793439%/34.333304% y -54.269535%/30.906858%. Se solapan y son descriptivas, no51validacionesOOS ni selector retrospectivo. Todos los meses/años/ventanas están enACCOUNTING.md/.json.

Ambos diagnósticos finales son idénticos:11423fitsválidos=5707gnegativos+5716gpositivos+0cero; media gRAW0.005206772334007732, sinerroresdeagregación. No hay signo negativo sostenido acreditado ni causalidad identificada. No11423muestras independientes; igualdad de resúmenes corrobora cálculo común pero no audita cada estado de toda la trayectoria. No se filtró por signo ni se cambiará narrativa después del resultado.

Signals7941/7914, occupied6281/6279, entradas1660/1635; señales ocupadas consumidas sincola. INTERACTIONlongs suman+875.056341USDT yshorts−4541.683922USDT: es atribución posterior; no se construirá long-only, se quitará short ni se elegirán coeficientes/horarios/regímenes con ese corte.

Auditoría financiera aec51c0c1dd84dd5abaddc4346895e99 succeeded con snapshots completos; fuente exacta guardada enACCOUNTING_SOURCE ycopiada enACCOUNTING. Reconcilia bruto−fees+funding=PNLsum=final−10000 yfundingcontra métrica, error máximo menor1e−6USDT. No se repitieron analysis o motores para este cierre. La orden MARKET terminal cerró el short, canceló stop y emitióFINALpostfee en ambos. El rawcountertotal_open_trades=1 de summary espreterminal, no posiciónrealabierta alfinal.

R11registró2.741.760marcasM1,63intervaloscontiguos/62mesescompletos y20trimestres; todos62mesescompletos activos. Equitywallet+PnLabierto yfronterasUTCpostfunding/predecisiónsegúnfase. La mediana incluye mesescalendarioinactivos porregla, aunque aquí ninguno completo fueinactivo. DD M1+fills no todoslosextremosintraminuto; DDdiariomotor66.129839%/69.744501% se conserva separado. Fundingaplicado,2591/2564pagoscon marca proxy en posiciones.

Fuentes/checks previos revisados porroot e independiente; final129comprobaciones sintéticas con oráculos ystubs. Primerintentofallido sólo por predicateASTdelharness, corregido sin tocar modelo; no se suma a129ni se cuenta como economía. Versiones y guardparidadprecio→cash previasalcálculo preservados enCODES/TECHNICAL_CHECK_RECEIPT.

Presupuesto cerrado: dos ejecuciones económicas, cero errores/reemplazos económicos. Sin vecinos debaseline42,ventanas408/360,warmup420,horizonte,hurdle,grado/productos,regularización,rank/rcond,coeficientes,signos,horarios,lados,filtros,riesgo,gestión/costes. No rescatar línea con datos2026,combinacionesopaper/live. Fuentes/protocolo congelados; no se modificaHub por este agente.

Evidencias en strategies/FundingOiPilot4h/reports/: BTC_DISCOVERY_AA_ACCOUNTING_20261021.md/.json (auditoría,logsFINAL/PRETERMINAL,63meses,5años,51ventanas,gates), BTC_DISCOVERY_AA_ACCOUNTING_SOURCE_20261021.md, PROTOCOL,CODES,MANIFEST yTECHNICAL_CHECK_RECEIPT_20261021.json. El objetivo global sigue pendiente; la continuidad autónoma requiere otra pregunta material y no obliga a promover esta receta.
