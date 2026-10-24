# V6 EFFICIENCY — screening y auditoría de ejecución

Las dos sesiones nominales [P](http://localhost:9200/#/backtest/8c8a2a0b-f3f9-4494-a557-7fbd2c5e0dd1) y [POI](http://localhost:9200/#/backtest/ea02b35f-28ba-480a-a0b5-bac3a5772b3c) terminaron sin error. Cubren el período continuo del 1 de septiembre de2020 al 1 de enero de2024, BTC-USDT4h y capital inicial10.000USDT. Son dos cuentas independientes, no una cartera combinada.

| Variante | Trades | Neto del período registrado | Drawdown registrado | Decisiones |
|---|---:|---:|---:|---:|
| P |148|+40,016599%|−21,869573%|7.302|
| POI |119|+11,339260%|−30,780642%|7.302|

Estos retornos corresponden a40meses, no a un año. POI falla el límite de drawdown de25%. P requiere todavía los gates de PF y años positivos y la conciliación financiera central; este informe no determina shortlist ni promoción.

## Ejecución y fuentes

Se utilizaron los drafts ya preparados, con un único arranque porID y el prerun persistido antes de cada llamada. El arranque POI devolvió un timeoutHTTP10s: se guardó el raw y se leyó el mismoID, que confirmó running; no se repitió el arranque. Los dos motores terminaron y fueron liberados antes de estas auditorías. No se crearon analysisjobs ni se modificó código, configuración nominal o registro global.

Las configuraciones terminadas coinciden exactamente con REGISTRY_V6: timeframe4h,240velaswarmup,fee0,00045/slippage0,isolated3x,funding históricoON ydatasets exactos. El tamaño no utiliza el multiplicador de leverage. Debug/fast solicitados true; fast efectivo false por funding.

Se recorrieron todos los logs:16páginas y3.041líneas paraP,14páginas y2.698líneas paraPOI. Máximos1.096/1.095caracteres, por debajo de1.900. También se leyeron los148/119trades completos con sus órdenes, en dos páginas por variante. Los raws completos quedaron en los shards V6_EFFICIENCY_P_SCREEN_LOGS_01..05/TRADES_01..02 y POI_LOGS_01..04/TRADES_01.

La auditoría técnica pasa para ambos:3.272aserciones estructuralesP y2.843POI. Por sesión hay40meses y155buckets de dirección; incluyen dos buckets con0barras y sólo un cierre, que no necesitan feature_reasons. No se tratan como datos ausentes ni como nuevas señales.

## Señales, planes y cierres

El flujo puro de features es idéntico en ambas variantes:297setups y7.005decisiones sin cruce. Los26cierres de entrada y las ventanas independientes actual/previa de25 tienen timestamps exactos; las desigualdades de cruce coinciden con umbral0,35. La normalización numérica registrada concilia.

Los267planes pasan ATR14aritmética/15OHLCactuales,distancia2,5ATRcongelada,stopdesdefill,riesgo2%confees,capnocional1x,floor8 yfundingasof. Todos los fills coinciden exactamente con el precio de su orden de entrada y las cantidades; la comparación con el entry_price reconstruido del trade usa tolerancia absoluta1e−8, explicada abajo. Hay como máximo una entrada por díaUTC y ninguna entrada comparte timestamp con un cierre anterior.

EnP se ejecutaron148setups y149quedaron bloqueados por posición. EnPOI hubo119entradas,108bloqueos por posición,67rechazos por OI no creciente,dos por inicialización y uno por referencia inválida. Las119entradasPOI tienen OI positivo/fresco con currentT y referencia exactaT−24h, disponibilidadasumida+6min yfreshness10min en su reloj original.

| Variante | Stops | Salidas por eficiencia | Máximo60barras | Cierre final forzado |
|---|---:|---:|---:|---:|
| P |53|91|4|0|
| POI |51|65|3|0|

Todos los callbacks y órdenes de cierre concilian con sus trades. Las salidas indicadoras son MARKET posteriores al fill, con E<=0long oE>=0short y25cierres válidos. Los siete máximos holding ocurrieron exactamente60×4h=240h después de la apertura. Los stops ejecutados coinciden con la protección inicial; no hubo objetivosLIMIT ni trailing. No se ejercieron cierres de calendario, invalid_after_fill o cierre final forzado en estos screenings.

Los contadores suman7.302barras y148/119entradas/cierres, sin diferencias por liquidación posterior al resumen. La resolución de fees, ledger de funding, curva equity, PF, años y drawdown corresponde al full-snapshotaudit de root.

## Precisión y límites

Una primera pasada del auditor falló por estado local de registro no conservado entre turnos; se leyó el registro real porMCP. Otra asumió feature_reasons en buckets creados sólo al cerrar una dirección: se aceptó el mapa vacío cuando bars=0, exactamente como el núcleo congelado. Son reparaciones del auditor, no del modelo ni del backtest.

La igualdad estricta entre logfill y entry_price del trade detectó19casosP y14POI con diferencias de hasta7,27596e−12unidades de precio. La orden ejecutada conserva exactamente elfill y las cantidades coinciden: es precisión delVWAP reconstruido. Se guardaron los fallos y diferencias en V6_EFFICIENCY_ENTRY_VWAP_FLOAT_DIAGNOSTIC.json y se cambió sólo la comparación de evidencia a1e−8 absoluto. Ninguna desigualdad de señal, sizing o fuente cambió.

Los hashes de ventanas quedan registrados, pero los raws de logs no contienen los26/25OHLC completos; no se afirma reconstrucción histórica independiente de velas. Las pruebas puras y el snapshot de fuentes cubren construcción causal y prefijos. OI sigue retrospectivo sin certificaciónPIT; funding conserva fuentesproxy. Un resultado nominal positivo no acredita supervivencia a fricción o parámetros vecinos.

No se consultaron resultados económicosV6 de2024–2025 ni2026; no se inició ninguna fase adicional. Root conserva selección y decisión económica.

## Evidencia

AUDIT_ResearchV6EfficiencyP4h_SCREEN.json y AUDIT_ResearchV6EfficiencyOi4h_SCREEN.json guardan grupos de aserciones, planes, salidas indicadoras, cierres, todos los buckets y manifiestos de raws. V6_EFFICIENCY_SCREEN_COUNTERS.json resume la cobertura; V6_EFFICIENCY_PROGRESS.json preserva fuentes, drafts, preruns, arranques y estados.
