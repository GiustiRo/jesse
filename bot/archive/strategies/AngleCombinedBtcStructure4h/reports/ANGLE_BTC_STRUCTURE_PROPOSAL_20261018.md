# Propuesta previa — BTC short por estructura H–L–H confirmada
18/10/2026. Propietario: orch_shorts. Nombre reservado: AngleCombinedBtcStructure4h. **Protocolo aprobado e implementado para revisión de fuente; sin borrador/run.** Fuente guardada y releída vía MCP. COT/VIX/funding y descargadores quedan archivados por rechazo humano, no por falsación económica; no se usan.

## Hipótesis y alcance
En la combinada ganadora, sustituir **solamente RSI3<=20** de la elegibilidad short BTC por una ruptura fresca de soporte después de un máximo menor confirmado. Una recuperación incapaz de superar el máximo anterior seguida por pérdida del mínimo intermedio describe demanda que falla; no infiere flujos ni liquidaciones reales a partir de OHLC. Es otra lectura de continuación bajista dentro del régimen ascendente original, no prueba de edge independiente.

Base exacta: [MultiAssetRetestBtcShort4h](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), fuente releída con MCP. Longs BTC, PAXG y SPY, horarios, prioridades, reservas, capital y gestión quedan textualmente iguales. No se busca un nuevo standalone ni se añade otra ruta BTC.

## Definición causal única, sin ZigZag retrospectivo
En cada decisión BTC4h, usar exclusivamente las últimas **60 velas cerradas (10 días)** para estructura local. Se conserva el mínimo140 del short original para EMA/ATR. Root escogió60 antes de implementación/resultados; no hubo barrido. Extremos locales simétricos de **dos barras a cada lado**: un máximo exige high estrictamente mayor que los cuatro vecinos; un mínimo exige low estrictamente menor. Empates no forman pivot. Un candidato que simultáneamente sea máximo y mínimo se descarta por ambigüedad de orden intrabar. Los últimos dos centros aún no confirmados no se utilizan.

Ordenar los pivots confirmados por timestamp. Si varios pivots consecutivos son del mismo tipo, conservar el más extremo (máximo más alto o mínimo más bajo); en igualdad conservar el primero. Esa compresión usa sólo pivots ya confirmados y se recalcula en la decisión actual, nunca cambia una orden pasada.

Exigir que los últimos tres eventos alternados sean **H1–L1–H2**, con timestamps H1<L1<H2 y H2<H1. La estructura H2 debe estar confirmada **antes de la barra que rompe**: índiceH2+2<índice de la última barra cerrada. El último cierre c[t] debe ser menor que L1, el previo c[t−1] mayor o igual, y ningún cierre desde la barra siguiente a L1 hasta t−1 puede haber sido menor que L1. Así se prueba la primera pérdida por cierre de ese soporte; no un cruce repetido después de ver el trade. Las mechas aisladas no equivalen a pérdida por cierre.

Si H2 se confirma en la propia barra de ruptura, se rechaza esa oportunidad. No se entra en el centro histórico de H2. No se rellenan pivots iniciales ni futuros; si el patrón no cabe completo en memoria60, no hay señal.

## Todo lo demás del short permanece original
EMA120[-1]>EMA120[-10] y precio>EMA120−ATR; ningún filtro nuevo de EMA/ADX/volumen. Tras el cierre que rompe, STOP futuro en min(low de la señal, close−0,25ATR). Stop ligado a EMA20 con distancia1–3ATR y misma protección mínima por fees; TP1,5ATR y salida72h. Se conserva vencimiento original de una barra para orden pendiente, sin nueva caducidad de posición, RSI alternativo, R mínimo, invalidación por reclaim o latch.

Fill real ancla stop/TP como en referencia. Se conserva long priority, single entry/full exit, riesgo máximo3% por trade/8% agregado, gross4,4x,5xaislado, fee0,00045 por lado incluso LIMIT y reserva original para sizing. Los gaps no garantizan esos límites como pérdida máxima.

Conservar reglas no garantiza mismos longs realizados: una nueva ocupación BTC y el capital posterior pueden cambiar cantidades u oportunidades. Ésa es interacción a medir, no motivo para tocar longs o los otros activos.

## Inventario y solapamientos explícitos
Releídos ledger central y diagnóstico, además de fuentes MCP: baseline, MultiAssetBtcPullbackShort4h, PullbackShort, RejectShort, RallyFade, Crisis, RiskOff, TrendBoth, OrchLateralFailedRange, OrchShortDailyPullback y QuietChannel. BtcTrendMaster se omite por HTTP500 legado.

- Baseline y Pullback: sobreventaRSI3, no secuencia confirmada H–L–H.
- RejectShort/DailyPullback: rechazo de EMA en régimen bajista, con swing corto para stop; no soporte intermedio después de máximo menor confirmado dentro del régimen ascendente.
- Crisis/RiskOff/QuietChannel/TrendBoth: ruptura de canal y contexto tendencial/volatilidad; compartimos familia de continuación, pero no sustituimos simplemente largo de canal/timeframe.
- FailedRange/RallyFade: retorno dentro de rango o exceso hacia media; aquí se vende pérdida de soporte después de recuperación fallida, no se compra una ruptura bajista fallida.
- RewardRisk, expiry24/48, Reclaim y OneFill ya fallaron o no regularizaron. Ninguno se reactiva.

No se afirma que el inventario pruebe novedad universal. La aportación material concreta es la secuencia causal precio–confirmación–ruptura como reemplazo de sobreventa.

## Revisión y evaluación antes de correr
Root aprobó implementar esta receta con memoria60 y confirmación estricta anterior a ruptura; la fuente queda ahora para revisión adicional antes de cualquier ejecución. Invariantes previstos: pivots y confirmaciones<=decisión, orden H1<L1<H2, memoria finita y primera ruptura verificable. Fuente de estrategia implementada sólo tras aprobación de protocolo; no scripts, fuentes externas, borradores ni backtests.

Una prueba económica combinada, si se autoriza, usará ventana común 2020-10-15→2025-12-31 exclusivo y modo normal. Cualquier smoke breve será técnico, de fechas predeclaradas por root, sin escoger la mejor ventana ni recalibrar por cero trades. 2026 sellado.

Evaluar cuenta completa y atribución short BTC frente a referencia: fills/cohortes, neto/costes, exposición, DD, contribución temporal y efecto sobre los longs sin cambios de reglas. V4 MTM, todos los63meses/21quarters y períodos completos; meses activos no sustituyen calendario. No usar promedios de duración final como filtros. Si reduce muestra o rentabilidad sin regularizar, se descarta sin barrer pivots1/2/3, memoria, stops o umbrales. Mantener65–70% y80%; esta propuesta no promete alcanzarlos ni convierte desarrollo visto en OOS.


## Comprobación de implementación previa a ejecución
Fuente: strategies/AngleCombinedBtcStructure4h/__init__.py, guardada por write_strategy y readback exacto. create_strategy primero informó strategy_exists porque la carpeta de reportes ya existía; listado MCP confirmó que sólo contenía nuestro informe y write_strategy creó la fuente sin tocar archivos ajenos.

Normalización verificó identidad exacta con el baseline tras retirar exclusivamente helper estructural y revertir nombre/docstrings, cálculo RSI3 y su condición. Así se comprueba que PAXG/SPY/longs BTC, ATR/EMA/macrorégimen, sizing, exits y contabilidad no cambiaron. No se ejecutó código para inferir rendimiento ni se creó sesión.

El helper procesa centros2..n−3, ignora empates/ambigüedad high+low, colapsa consecutivos por extremo conocido y exige últimos H–L–H. Comprueba h2_index+2<última barra, cross por cierre y ausencia de cierres previos bajo soporte; un assert repite la invariante temporal al devolver señal. No hay estado dependiente de PnL/fill ni pivots futuros. Espera revisión root de fuente antes de draft o run.
