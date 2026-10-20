# Caducidad de shorts: controles24/48h frente a72h
Hipótesis y criterios fijados antes de correr en strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_SHORT_TIME_EXIT_PROTOCOL_20261018.md.
Se modificó únicamente caducidadshort72→24/48h; longs/entradas/stops/targets/riesgo intactos. Evaluacióncada4h,duraciónfinalpuedesuperar el umbral. Referencia congelada;2026reservado.

| Salida short | CAGR % | DD Jesse % | Shorts netos USDT | Winrate shorts % | Meses activos positivos % | Trimestres positivos % |
|---|---:|---:|---:|---:|---:|---:|
|72h referencia|28.8294|-14.8905|5287.02|55.2846|54.0984|71.4286|
|24h|26.2184|-16.2880|2813.75|51.1628|55.7377|66.6667|
|48h|27.6810|-14.9067|4243.72|52.3810|54.0984|66.6667|

[Referencia72h](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb),[24h](http://localhost:9200/#/backtest/e474571a-bcad-47a9-b650-4ab14cc5029e),[48h](http://localhost:9200/#/backtest/13c71d3e-17fe-44f2-8ce5-95f466ccda22).

## Decisión
No adoptar ninguna.24h mejora solo un mes (34/61frente33/61),pero empeora retorno/DD ytrimestres.48h no mejora meses y empeora trimestres con menor retorno. Ninguna cumple65–70%/80%. Ambas ganan en shorts,pero eso no basta. No extender búsqueda a12/16/20/28h para encontrarunmáximo ni promover por winrate>51%.
No se corren costes adicionales de estas variantes: no superaron la primera condición de mejora estructural del conjunto. Los controles de coste de la referencia ya están documentados.

## Interacciones
97longs en todos;123/129/126shorts para72/24/48h. Longs netos22174.44/20854.67/21509.08 aunque sus reglas no cambien: capital/reservas/tamaños interactúan en cuenta compartida. No restar hipotéticos trades largos en duración del backtest original.
La correlación por duración final fue descriptiva, no causal. Estos reruns invalidan que simplemente cerrar antes resuelva el problema.

## Verificación
Parámetros de sesión10000capital,5xaislado,fee.00045,3%/8%riesgo,3rutas4h,mismoperíodo2020-10-15 a2025-12-31 exclusivo,modo normal. Saldo terminal33668.42/35752.80 para24/48h,0abiertas.
AnálisisMTMv3 job d4c191d90e0d4ef685c07609553293a6 succeeded,autocontrolespasaron y saldosreconciliados.63meses/61activos,incluyebordesparciales. DDcierrediario-16.3201%/-14.8946% para24/48h; diferente al muestreoJesse de tabla. No hay simulaciones activas.

## Próxima hipótesis a considerar
La distancia al stopshort se liga aEMA20 y admite1–3ATR,pero objetivo fijo1.5ATR. Esto produce relaciones premio/riesgo planificadas diferentes entre señales. Una próxima prueba controlada puede exigir recompensa/riesgo mínima previa a entrada o ligar objetivo a riesgo inicial, uno por vez. No asumir que ambas mejorarán, no calibrar un umbral fino mirando el resultado. Mantener controles por períodos/costes/vecindarios antes de aceptar.

Además, auditar concentración dePAXG/SPYlongs y su aportación a meses malos, pues no todo déficit de regularidad viene de shorts. No perseguir51%winrate como sustituto de expectativa neta.
