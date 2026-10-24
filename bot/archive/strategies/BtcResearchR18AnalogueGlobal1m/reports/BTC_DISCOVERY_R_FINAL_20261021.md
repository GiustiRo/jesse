# BTC Discovery R — cierre

Pregunta: similitud de seis retornos normalizados L2, KNN20 coseno frente a media global de los mismos 360 orígenes maduros, para pronosticar retorno de precio a24h. Protocolo previo, dos corridas completas, ninguna sustitución económica.

Ventana UTC [2020-10-15,2026-01-01), desarrollo reutilizado. Capital10000; riesgo2%/6%/aislado3x; comisión taker0.00045 por lado; funding histórico aplicado y reconciliado, con marcas proxy declaradas; slippage0. Neto=fees+funding modelados. Stop2ATR14simple, sinTP, timeout24h. No estrés ni variantes de riesgo.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/e9f4b1d0-277a-4ef7-b10d-c72365d1809e)|1751|-18.963571|0.941229|83.138366|25/62|7/20|-0.707490|-10656.139018|
|[GLOBAL](http://localhost:9200/#/backtest/ca8c8f66-8fe0-460a-a3ac-142c565b4961)|1265|-6.824291|0.962141|57.175057|22/58|8/20|-1.773945|-7173.250998|

KNN: bruto precio 4701.021658605742; comisiones 9948.266673171467; funding -1413.6015183596885; neto -6660.846532925419; equity final 3339.1534670745136. Años completos: {"2021":16.63716600808669,"2022":-22.378583620187133,"2023":-28.484899927751172,"2024":-46.389541736351866,"2025":-25.94236968672027}. Peor ventana móvil12m -46.90821269679664%; mejor 64.84593144335804%.

GLOBAL: bruto precio 5849.171266847794; comisiones 7018.0481513692275; funding -1914.8927447151261; neto -3083.769629236552; equity final 6916.230370763464. Años completos: {"2021":-7.939920017396518,"2022":-18.40805561046753,"2023":-19.45835468464412,"2024":9.187526351732078,"2025":-19.14598573194839}. Peor ventana móvil12m -37.62939107167723%; mejor 40.855837110551164%.

Auditoría financiera de snapshots completos: job f16a68a6f6cd49108af72f2fc0fa458c succeeded; errores de reconciliación <1e-6. No totales inferidos de páginas parciales. Telemetría63filas mensuales/62meses completos/20trimestres,2741760marcas M1 por receta,0ventanas inválidas. GLOBAL usa FINAL tras liquidación terminal; contador rawopen1 es metadato previo, no exposición final. DD observa M1+fills, no todos extremos intraminuto. Frontera mensual por fase postfunding/predecisión. Ventanas móviles solapadas, no OOS ni muestras independientes.

Chequeo técnico final1169PASS, job98cb30b8d9ac40a292e01402524fef09; primer intento tuvo SyntaxError del fake harness, corregido antes de economía. N>=100 sólo suficiencia operativa preliminar, no potencia estadística.

Decisión: ninguna candidata. Se cierra R sin ajustar K, dimensión, lookback, horizonte, distancia, hurdle ni signo. El beneficio bruto no cubre costos base. Otra pregunta material puede estudiar utilidad realizable con stop, preservando modelo y parámetros; requiere protocolo y revisión de antecedentes antes de implementación. No es aprobación ni ejecución de S.
