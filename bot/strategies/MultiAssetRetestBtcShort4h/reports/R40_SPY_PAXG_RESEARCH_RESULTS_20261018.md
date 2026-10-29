# R40 SPY/PAXG: veinte escenarios nuevos, cierre consolidado

Fecha local:18 de octubre de2026; ejecuciones del19 de octubreUTC.

**Los veinte backtests terminaron: dieciocho recetas pierden y dos no operan. No se demuestra una mejora robusta para ninguno de los dos activos.** PAXG: diez negativas; SPY: ocho negativas y dos sin exposición. Ninguna candidata justifica sensibilidad económica adicional, integración o sustitución de referencia. El objetivo de mejorar ambos activos sigue pendiente.

## Diseño, código y contrato

Son diez escenarios por activo fijados antes de resultados: filtros de ciclo y estado latente, estacionalidad aprendida, espectro, mechas, tendencia adaptativa, centros de rango, contexto diario/semanal, recuperación de excursiones, detector CUSUM, relación beta entre activos, variación intradiaria, ocupación, organización ordinal, modelos por segmentos y duración de rachas, subasta semanal, densidad de cierres y presión de barreras. Las formulaciones comparten familias; no son veinte mecanismos o replicaciones independientes.

Matrices y adendas preceden a resultados de cada receta. Root revisó motor y diez señales de ambos especialistas; readbacks completos y comparación de plantillas. Correcciones técnicas previas a ejecución:62precios para sesenta retornos anteriores; label estacional close-to-close, continuidad y noventa muestras por franja; TP Kalman absoluto; partición intradiaria SPY de trece incrementos que suma el retorno cash; deudas persistentes de salida. Todo queda en R40_ROOT_IMPLEMENTATION_REVIEW_20261018.md y documentos por activo.

Root volvió a leer las veinte summaries y verificó estados finished, ausencia de errores y formularios:2020-10-15 a2025-12-31 EXCLUSIVA,10.000USDT,fee0,00045 por lado,5x aislado, modo normal y debugfalse. Riesgo planificado1%, techo nocional4,4x, sin piramidado. Reserva10bps sólo para sizing. Las veinte fuentes revisadas coinciden exactamente con strategy_codes de sus sesiones al cierre.

Se usaron los proxies aceptados y datos existentes; sin funding, volumen supuesto, fuentes nuevas, scripts de investigación, instalaciones, cambios de framework o live/paper. BTC y2026 no se tocaron. Dos backtests por especialista/cuatro globales y un análisis por especialista/dos globales. Se conservaron recetas, lados y períodos después de observar sus pérdidas.

## Todos los resultados

Capital aislado por sesión. No sumar netos o curvas para fingir una cartera. Antes de fees significa neto más comisión de esos mismos fills y tamaños; no equivale a una nueva simulación sin costes ni al campo gross_profit. PF es el cociente de ganancias/pérdidas netas por trade. DD es el reportado por motor. Sin operaciones deja métricas económicas ausentes, no riesgo o retorno demostrados de cero.

|Escenario y sesión|Operaciones|Antes de fees USDT|Fees USDT|Neto USDT|PF|DD motor %|
|---|---:|---:|---:|---:|---:|---:|
|[PAXG40-01 · KalmanInnovation4h](http://localhost:9200/#/backtest/3db140a6-e6a4-4f41-b8f3-c79537cedc47)|1393|5919.30|9586.18|-3666.88|0.864|-45.955|
|[PAXG40-02 · LearnedSeason4h](http://localhost:9200/#/backtest/6ac794c8-450c-446d-8db8-b2b1b65e8091)|3645|-500.30|8775.54|-9275.84|0.443|-92.939|
|[PAXG40-03 · SpectralProjection4h](http://localhost:9200/#/backtest/a62ef27f-e5d3-42ab-b877-f762891a1a50)|136|-838.02|884.15|-1722.17|0.527|-19.275|
|[PAXG40-04 · WickBalance4h](http://localhost:9200/#/backtest/b2aaf16b-e9fe-43cc-9a72-bdf189f3ae66)|304|31.66|1825.55|-1793.89|0.791|-20.443|
|[PAXG40-05 · KamaHysteresis4h](http://localhost:9200/#/backtest/32f7e55f-2dca-476d-87f2-4037bb97c71d)|332|-426.36|1335.75|-1762.10|0.802|-26.450|
|[PAXG40-06 · RangeCenterLead4h](http://localhost:9200/#/backtest/a7ca74dc-e111-40fa-8162-f1500eb87f38)|192|1252.82|1413.28|-160.46|0.976|-10.932|
|[PAXG40-07 · WeeklyDailyPullback4h](http://localhost:9200/#/backtest/08061fce-e885-4526-b668-5094344a6644)|161|-599.51|465.71|-1065.22|0.720|-16.821|
|[PAXG40-08 · DrawdownRecovery4h](http://localhost:9200/#/backtest/14455aed-0be2-43e2-83de-28df5dc840b8)|120|-574.45|761.81|-1336.25|0.711|-23.660|
|[PAXG40-09 · CusumDrift4h](http://localhost:9200/#/backtest/4622a9da-cfc0-45c5-a223-44aad68e1ce0)|283|-613.11|1544.04|-2157.15|0.769|-33.270|
|[PAXG40-10 · BetaResidual1h](http://localhost:9200/#/backtest/da3e6ee6-b6f6-4764-a5aa-724d604ab75f)|87|-1819.53|529.80|-2349.33|0.493|-26.851|
|[SPY40-01 · CausalCycle2h](http://localhost:9200/#/backtest/3441ac21-d65a-48f4-9f2d-4a025b474c1c)|0|—|—|Sin operaciones|—|—|
|[SPY40-02 · JumpComponentFade](http://localhost:9200/#/backtest/47206fe5-b8e0-4650-a7dc-23d0f7949e24)|58|-62.41|201.01|-263.42|0.798|-5.302|
|[SPY40-03 · OccupationFlip](http://localhost:9200/#/backtest/817894dd-a064-4a38-be9c-990c7831e599)|15|-91.02|55.55|-146.58|0.595|-2.561|
|[SPY40-04 · OrdinalEntropy](http://localhost:9200/#/backtest/7e15fa8f-eb4f-4029-af1a-6bae22f1803d)|189|-269.69|607.65|-877.35|0.787|-9.846|
|[SPY40-05 · SegmentedResponse](http://localhost:9200/#/backtest/a99c090e-fa7d-4ec9-a51d-df265a0373fd)|179|-657.59|527.46|-1185.05|0.597|-13.047|
|[SPY40-06 · RangeCloseInformation](http://localhost:9200/#/backtest/c3d874cb-ced8-4c68-8605-73335aae3a6e)|35|-538.33|121.81|-660.15|0.300|-6.631|
|[SPY40-07 · RunDurationResponse](http://localhost:9200/#/backtest/fcd709dc-c844-4d40-8e9a-35497ac3681f)|68|-232.60|220.44|-453.03|0.578|-5.280|
|[SPY40-08 · WeeklyAuctionRepair](http://localhost:9200/#/backtest/79ce393c-4c56-46ae-a1b0-9410a5da2fc8)|0|—|—|Sin operaciones|—|—|
|[SPY40-09 · CloseDensityReversion](http://localhost:9200/#/backtest/816a9466-705c-4149-a705-b466911dca5f)|249|611.98|830.74|-218.75|0.952|-9.487|
|[SPY40-10 · RepeatedBarrierPressure](http://localhost:9200/#/backtest/9446bc74-046a-42fb-a65b-531828ea8758)|11|2.05|35.13|-33.08|0.840|-1.543|

PAXG auditó6.653 operaciones distribuidas entre diez simulaciones, con87–3.645 por receta. SPY auditó804 operaciones en ocho recetas;03/10 tienen15/11 y son negativas con muestra escasa. La suma7.457 es un recuento contable entre políticas alternativas, no una muestra independiente de oportunidades. En esta tanda no hubo ganancias netas.

## Qué aprendimos

Trece de las dieciocho recetas con exposición pierden también antes de fees. Las otras cinco no cubren la tarifa aceptada: PAXG01/04/06 y SPY09/10. El problema observado no se explica únicamente por comisión. No se eligió un año, lado o política de menor pérdida para declarar éxito.

En PAXG, tres ventajas brutas alcanzan aproximadamente5,56/0,16/7,98bps por nocional de entrada, frente a unos9bps de comisiónRT. Más participación tampoco mejoró la expectativa: KAMA tuvo71,63% de tiempo con posición, Kalman43,45% y contexto diario/semanal39,62%, todos negativos. Tiempo expuesto no equivale a capital nocional medio o retorno sobre capital desplegado.

SPY09 gana611,98USDT por precio pero paga830,74; SPY10 apenas gana2,05 antes de35,13 de fees. El largo de09 gana554,35 y el corto pierde773,10: son cortes posteriores al resultado, no autorización para promover un long-only. Los otros seis escenarios con operaciones pierden por precio antes de fees. SPY08, de baja frecuencia prevista, no genera entradas y sus estados no están exportados.

Los recargos estáticos5/10bpsRT aplican2,5/5bps por lado a todos los fills y empeoran las recetas. Mantienen cantidades y decisiones; no simulan nueva trayectoria de capital o ejecución. No se interpreta un recargo contable que deja saldo teórico negativo como una nueva cuenta que habría podido continuar operando.

## Hallazgo técnico separado: normalización del filtro de ciclo

El [ciclo SPY40-01](http://localhost:9200/#/backtest/3441ac21-d65a-48f4-9f2d-4a025b474c1c) no opera. Root comprobó el indicador nativo con señales artificiales, sin velas reales y sin modificar la receta. Una onda de amplitud5 y periodo20 normaliza aproximadamente entre−1 y+1 con nivel0 y longitud240; al añadir un nivel constante500, el BP bruto sigue cercano a±5 pero su normalizado queda alrededor de−0,084/+0,075. Con1000observaciones esa diferencia desaparece en el caso probado.

Esto demuestra sensibilidad al arranque/nivel en ese ejemplo y cuestiona asumir una amplitud normalizada cercana a±1 con cualquier ventana. En la fuente local inspeccionada, el wrapper escalar recorta historia según warmup; el formulario conserva240. La prueba nativa de1000puntos no demuestra que el wrapper escalar use toda esa historia. No se hizo introspección de archivos remotos ni cambios de framework.

El diagnóstico no identifica qué gate bloqueó las entradas reales, porque los snapshots no guardan estados del indicador. SPY01 queda sin evidencia económica; no es una refutación de todos los ciclos. Se conserva la receta congelada y el resultado original. Los dos diagnósticos sintéticos adicionales no cuentan como nuevas primarias ni backtests. Fuente, salidas y límites en R40_BANDPASS_SYNTHETIC_DIAGNOSTIC_20261018.md.

## Auditoría y criterio de cierre

Dos análisis PAXG y cinco SPY de snapshots completos conciliaron cantidades, fees por fill, PnL, wallet, solapamientos y terminales. Todos terminaron succeeded. También terminaron succeeded los dos diagnósticos sintéticos root. Root verificó los nueve estados por MCP; no queda análisis propio ejecutándose.

No se calculó nuevo MTM o cartera compartida al no aparecer candidata y no informar regularidad mensual. Las cohortes por año de cierre se etiquetan como tales; no se trata Portfolio00:01 como cierre UTC. Los objetivos mensuales/trimestrales pertenecen a cartera. Duraciones reales y deudas por quotes ausentes están documentadas: no se fabrican fills en la hora nominal. Los snapshots no prueban cada oportunidad rechazada o motivo de espera.

Cribado previo: neto>0,PF≥1,2,unas30operaciones yDD no peor que−25%. Ninguna receta pasa. No se bajan esos filtros ni se abre2026 para encontrar aprobación. Todo2020–2025 sigue siendo desarrollo ampliamente seleccionado; una matriz predeclarada ahora no lo vuelve OOS limpio.

## Referencias que siguen vigentes

|Comparador aislado1%|Operaciones|NetoUSDT|PF|DDmotor%|
|---|---:|---:|---:|---:|
|[SPY retest](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|31|751.35|1.493|−5.213|
|[PAXG retest](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c)|35|546.11|1.308|−6.919|
|[PAXG fin de semana0,75](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c)|60|764.04|1.732|−2.991|

Son comparaciones de políticas con exposición y payoff distintos, no ensayos aleatorizados. El fin de semana sigue siendo un descubrimiento experimental anterior, sin sustitución aceptada; su cuenta compartida previa no alcanzó la mejora de regularidad. La [referencia original de cartera](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) permanece inmutable.

Entre R20 y R40 se ejecutaron cuarenta primarias nuevas: cuatro positivas, treinta y dos negativas y cuatro sin exposición. Las cuatro positivas pertenecen a R20 y no demostraron mejora robusta. Es selección adicional a los diecisiete fulls previos y al inventario más antiguo, no cuarenta observaciones independientes.

## Continuación que aportaría información

Permanecemos en investigación de SPY/PAXG, sin avanzar de fase. La revisión crítica de PAXG plantea una pregunta más dirigida: ¿cuánto aporta seleccionar entradas en la referencia frente a exposición long y gestión que captura pocos runners? Un contraste posterior debe conservar gestión y restricciones y comparar oportunidades de riesgo/exposición razonablemente equivalentes, con presupuesto y abandono fijados antes de resultados. No basta un shuffle de los trades realizados: conserva sus payoffs y no representa entradas alternativas.

Los snapshots actuales no contienen el universo completo de oportunidades rechazadas. No inferirlo de los fills ni prometer que una nueva colección de indicadores resolverá el problema. También conviene resolver la semántica de inicialización del filtro mediante pruebas sintéticas antes de otra prueba económica de ciclo. Estas son preguntas posteriores, no reglas modificadas o nuevos backtests ejecutados en esta tanda.

## Índice de evidencias persistentes

Dentro del proyecto en la máquina que ejecuta Jesse:
- strategies/MultiAssetRetestBtcShort4h/reports/R40_SPY_PAXG_STAGE_PROTOCOL_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/R40_ROOT_IMPLEMENTATION_REVIEW_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/R40_BANDPASS_SYNTHETIC_DIAGNOSTIC_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY40_MATRIX_PROTOCOL_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY40_IMPLEMENTATION_REVIEW_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY40_FINAL_RESULTS_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY40_RESULTS_DATA_20261018.md
- strategies/ResearchSpyReference4h/reports/SPY40_ANALYSIS_SOURCE_20261018.md
- strategies/R20PaxgARResponse4h/reports/R40_PAXG_TEN_EXPERIMENTS_PROTOCOL_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_IMPLEMENTATION_REVIEW_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_FINAL_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_BATCH1_AUDIT_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_BATCH2_AUDIT_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_ANALYSIS_SOURCE_20261018.md
- strategies/R40PaxgKalmanInnovation4h/reports/PAXG_R20_R40_CRITICAL_REVIEW_20261018.md

### Jobs verificados

```json
[
  {
    "id": "cf816b2073384def8a7883458bc592ed",
    "status": "succeeded"
  },
  {
    "id": "86c6c77a0a3849b2802c5f25a4123724",
    "status": "succeeded"
  },
  {
    "id": "803b4e9b71814d7ead7ad52460db9e7f",
    "status": "succeeded"
  },
  {
    "id": "0bad9bcf93c64493b90f217c828bd256",
    "status": "succeeded"
  },
  {
    "id": "bd94d7bf995a4afa9df061908cfdac00",
    "status": "succeeded"
  },
  {
    "id": "4aee4d320ebe4536841c70c9c9a26b29",
    "status": "succeeded"
  },
  {
    "id": "0a9d9f3a20a7475ea9f1bdb98dbee0e8",
    "status": "succeeded"
  },
  {
    "id": "a5d0af5c5fcc41eaaf5e69b9f216607e",
    "status": "succeeded"
  },
  {
    "id": "0401e478bc9a40a3aba6457a4a18f0cf",
    "status": "succeeded"
  }
]
```
