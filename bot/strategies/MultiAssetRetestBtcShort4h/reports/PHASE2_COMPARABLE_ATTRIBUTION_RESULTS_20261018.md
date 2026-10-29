# Fase2: atribución con reglas y contexto comparables
Todos los casos usan mismos longsLIMITretest,stop/trailing,risk3%/8%,5xisolated,capital10000,fee.00045,mismo2020-10-15 a2025-12-31exclusivo,modo normal. Las3rutas y su asignacióninverseATR se mantienen aun si un activo está deshabilitado. Esto aísla añadir actividad con contexto fijo, NO compara carteras eficientes con redistribución de capital o riesgo igualado.2026reservado.

| Caso | CAGR% | DDJesse% | Sharpe | Meses positivos/activos | Positivos/todos63 | Trimestrespositivos |
|---|---:|---:|---:|---:|---:|---:|
|BTClong|16.8112|-11.9516|1.1720|15/29=51.7241%|15/63|9/21=42.8571%|
|BTClong+short|21.7099|-13.0078|1.3239|34/56=60.7143%|34/63|14/21=66.6667%|
|3activoslong|23.6650|-14.0753|1.1812|28/55=50.9091%|28/63|14/21=66.6667%|
|3activoslong+BTCshort|28.8294|-14.8905|1.3164|33/61=54.0984%|33/63|15/21=71.4286%|

[BTClong](http://localhost:9200/#/backtest/bf52f5eb-f6fe-4491-a90e-e15d404b9de7)
[BTCambos](http://localhost:9200/#/backtest/4623d369-05e7-4714-8f3b-5c10b1726663)
[3longs](http://localhost:9200/#/backtest/11c1a0a6-afe8-4718-80b9-a35e95adf40d)
[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)

## Qué aporta cada componente
Añadirshorts aBTClong elevaCAGR4.90puntos y DD1.06puntos; positivos15→34 de63meses ytrimestres9→14de21. Dosmesesnegativos pasanpositivos,trespositivos pasanegativos;granparte del aumento de positivos viene de meses antes planos. No afirmar que corrige sistemáticamente pérdidaslong.
Añadirshorts a3longs elevaCAGR5.16puntos y DD0.82puntos; positivos28→33,trimestres14→15. Tresmesesnegativos pasanpositivos,cuatropositivos pasanegativos. De nuevo el neto se completa con meses antes planos.
AñadirPAXG/SPYlong aBTCambos elevaCAGR7.12puntos,pero DD1.88puntos y mesespositivos34→33de63. Trimestres14→15. Sietemesesnegativos pasanpositivos,nuevepositivos pasanegativos. Su beneficio individual positivo no basta para mejorarregularidad.
No se alcanzan65–70%mesesactivos/80%trimestres en ninguno.

## Exposición reconstruida al cierre diario
|Caso|Díasconposición%|Nocionalbruto/equity medio|Máximo diario|
|---|---:|---:|---:|
|BTClong|11.5607|0.08033x|1.29568x|
|BTCambos|17.1834|0.11257x|1.29561x|
|3longs|34.7346|0.57684x|4.23383x|
|Referencia|38.5707|0.60855x|4.23543x|
Muestrasal cierreUTC,cotizacionesarrastradasdurantecierre para valoración. No exposición máxima intradiaria ni riesgo efectivo alstop. Reparto conserva capacidadociosa deactivos desactivados: no recomendarBTCambos con capitalredistribuido sin otracomparación. El salto deexposición impide atribuir másretorno a diversificación por sísolo.

## Capital compartido
BTClongsolo12482.45neto,conshortsBTC12976.73long+4875.75short.3longsneto20265.50frentereferencia27461.46; diferencia7195.96,no simplemente5287.02de shorts,por cambios entamaños de longs. Countstrades31/156/97/220. No confundir PnLporpata con contribuciónmarginalcontrafactual.

## Verificación y decisión
AnálisisMCP9a54544d46e54aeaae5ff4295d7fc088 succeeded,autocontrolesMTMv3 pasaron,saldosterminalesreconciliados. Mesesde63incluyenbordesparciales. CSVmonthly_matrix.csv y cada casoenworkspace temporal. No se usó2026. No se modificóreferencia.
BTCMomentumBaseline3 esbenchmark distinto(MARKET/otrasreglas),no usarlo paraatribucióndeesta matriz.
Conservar referencia;no promoverBTConlypor60.7%ni optimizarpara65. Debencompletarse prioridadrutas ycostescon reglasfijas antes de elegirsiguientehipótesis. La debilidad deregularidad tambiénesdecombinación/asignación,longs y exposición, no solo shorts.
