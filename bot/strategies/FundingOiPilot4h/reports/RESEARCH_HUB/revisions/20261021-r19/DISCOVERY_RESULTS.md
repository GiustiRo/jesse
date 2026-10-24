# BTC Discovery S — cierre

Pregunta material: KNN20/cosenoL2 sobre seis retornos frente a GLOBAL de los mismos360orígenes, aprendiendo dos payoffs fee-only con stop2ATR/noTP24h. Cambio de target respectoR, no ablación causal pura ni evidenciaOOS. Antecedente Angle de labels monetarios preservado sin relajar sus gates.

Ventana[2020-10-15,2026-01-01)UTC,10k,2%/6%/3xaislado,fee.00045/lado,slippage0,funding históricoBTC ON/aplicado/verificado con proxiesdeclarados. Neto real incluye fees y funding; labels sólo fees por nocional, no neto completo ni órdenes contrafactuales ejecutadas.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Q positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/97da0472-42e2-4f1a-b5be-b63f02e44318)|1643|-7.729306|0.967591|61.601500|28/62|7/20|-0.693118|-6553.473222|
|[GLOBAL](http://localhost:9200/#/backtest/1709388d-cc36-411b-bac0-7102b3fceb7e)|902|-2.061120|0.984002|45.289492|22/51|8/20|0.000000|-5221.973347|

KNN: bruto precio 8033.446762119682; fees 9937.80305348834; funding -1522.7381478642626; neto -3427.094439232939; capital final 6572.905560767034. Años completos {"2021":13.76937060504475,"2022":-32.731322578714504,"2023":-24.641796751558466,"2024":10.815320884566093,"2025":-22.00274004431979}; peor/mejor12m -40.72059174553348/35.95913156432082%.

GLOBAL: bruto precio 6014.539956064877; fees 5097.655771779939; funding -1946.3559332292652; neto -1029.471748944319; capital final 8970.528251055617. Años completos {"2021":-16.528798692063063,"2022":11.31917374924667,"2023":-19.46630366742482,"2024":-3.062729372668871,"2025":-5.675761671102153}; peor/mejor12m -26.973113346761224/28.5827735700936%.

Verificación real: en ambas recetas11424decisiones4h,360orígenesválidosmínimo/máximo,11783paresmaduroscalculados,4100857cachehits,11423purges,0featureinvalid/0missinglabels. Cada path1440M1exactoscerrados/deadline24h; esto acredita cobertura de esta ejecución, no ventaja predictiva. Forecasterfee-only no representa funding/margen y puede diferir del fill real; gestiónrealheredada desdeopened_at sin modificar.

Medición63intervalos/62meses completos/20trimestres,2741760M1marks cada cuenta,0invalidwindows; PRETERMINAL=finalsinposiciónabierta. DD M1+fills, no todos extremosintraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos. Ventanas12m solapadas, no independientes.

Auditoría financiera dbe601b37bc44b4fb350504abba12147 succeeded de snapshots completos: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. N>=100 es suficiencia operativa preliminar, no confianza. Checktécnico suppliedsource/sintéticos1a13343c98ea41adbf0ee4bb6d97ab74,1900PASS primerintento; padres sin cambios. Dos económicos completos,0fallos/reemplazos/backtests técnicos.

Decisión: NO_CUMPLE,ninguna candidata. Se cierra S sin vecinos deK/d/lookback/horizonte/distancia/hurdle/signo/costlabels/fundinglabels/stop/shrink ni selección retrospectiva long-only. Bruto positivo no cubre costos. Sin estrés/riesgo nuevo/2026/live/paper/imports.

Continuidad: T, faseUTC4h frente a driftGLOBAL, protocolo fijado antesdelresultadoS. Todavía requiere recibos técnicos, manifiesto y preflightantesmotores. Objetivoeconómiconoalcanzado; continuarautónomamente.
