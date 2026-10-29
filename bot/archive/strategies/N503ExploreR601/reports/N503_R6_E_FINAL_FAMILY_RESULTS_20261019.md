# N503 R6 — exploración E601..605, resultados finales

Cinco hipótesis congeladas desde N503; diez backtests nominales B/C finalizados sin errores. Se ejecutaron de a dos con ticket root, máximo cuatro globales. **Ninguna mejora el neto de N204 ni de N503 en ambas carteras; no se promociona sustituta.** No se hicieron verificaciones fee/target de esta familia ni rescates adicionales. 2026 cerrado incluso a inspección.

Referencias [N204B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142)13.056,614915USDT y[N204C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794)13.239,442380. Semilla exploratoria[N503B](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)13.328,711713 y[N503C](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)13.536,902513, no promovida.

## Mecánicas

ER original0<ER<=1/3 inalterado; único gate añadido al setup completo, latchavanzaocupado/pending,sincola. MARKET,d ySLoriginal,TP2R/48h; originaleslong/STOPshortprioritarios.

|Receta|Único gate|Suplementos fills/closes por cartera|Eventos / ocupados|
|---|---|---:|---:|
|E601|V trigger>medianaVde12barrasprevias; transferencia explícita R2N207 a N503|53/53|62/5|
|E602|Mecha superior de s positiva y>=cuerpo ymechainferior|24/24|29/4|
|E603|C_t<O_s: reversión compuesta móvil8h|60/60|75/11|
|E604|C_t−mínimoLowW48h>=2d, objetivooriginal cabe antes del soporte|1/1|1/0|
|E605|Cierre finalM1<minLowprimeros180M1 de t; cobertura exacta240M1|29/29|37/6|

Los conteos se verificaron en logs terminales B/C y son iguales entre ambas carteras. No inferir que los suplementos añadidos a un gate sean necesariamente subconjunto de fills semilla: el latch modificado y ocupación pueden añadir entradas en otros instantes. E604 sólo una operación; E60224 yE60529, insuficientes para conclusiones generales del mecanismo.

## Métricas nominales de cartera

|Sesión/dashboard|NetoUSDT|Trades|Sharpe motor|DDmotor%|
|---|---:|---:|---:|---:|
|[E601B](http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc)|12139.275231|250|1.544148|-8.773183|
|[E601C](http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359)|12329.381307|257|1.532994|-9.054184|
|[E602B](http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136)|12229.552825|226|1.569232|-7.465113|
|[E602C](http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040)|12426.752530|233|1.556931|-8.168013|
|[E603B](http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867)|12378.550859|258|1.539725|-8.234413|
|[E603C](http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe)|12551.137809|265|1.526245|-9.054184|
|[E604B](http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e)|9055.465020|207|1.303941|-8.268783|
|[E604C](http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b)|9206.394154|214|1.294211|-8.280447|
|[E605B](http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6)|11674.378424|229|1.509616|-7.462808|
|[E605C](http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826)|11883.704693|236|1.498025|-8.168013|

E603 es la más cercana en neto de esta familia, aún−678,06/−688,30USDT frenteN204. E602 yE605 reducenDD en ambas carteras, con una caída del neto: tradeoff exploratorio que no supera el contrato. E604 filtro restrictivo con una sola operación del suplemento, no evidencia contra soporte en general.

## Costes, regularidad y puerta

|Sesión|Semilla|Neto|ΔN204|Δsemilla|DDmotor%|Neto+10|Δ+10N204|+5 Mactivos full/all|+5 Mcalendario full/all|+5 Q full/all|Puertas N/MQ/+10/DD|
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
|[E601B](http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc)|N503|12139.275231|-917.339684|-1189.436481|-8.7732|10198.375215|-732.834529|39/60;39/62|39/61;39/63|15/19;16/21|FAIL/FAIL/FAIL/PASS|
|[E601C](http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359)|N503|12329.381307|-910.061073|-1207.521206|-9.0542|10276.913143|-726.502322|39/60;39/62|39/61;39/63|16/19;17/21|FAIL/FAIL/FAIL/PASS|
|[E602B](http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136)|N503|12229.552825|-827.062090|-1099.158887|-7.4651|10443.208020|-488.001724|41/59;41/61|41/61;41/63|15/19;16/21|FAIL/FAIL/FAIL/PASS|
|[E602C](http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040)|N503|12426.752530|-812.689849|-1110.149983|-8.1680|10530.080653|-473.334812|42/59;42/61|42/61;42/63|16/19;17/21|FAIL/PASS/FAIL/PASS|
|[E603B](http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867)|N503|12378.550859|-678.064056|-950.160853|-8.2344|10403.780451|-527.429293|41/61;41/63|41/61;41/63|17/19;18/21|FAIL/PASS/FAIL/PASS|
|[E603C](http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe)|N503|12551.137809|-688.304571|-985.764704|-9.0542|10467.165629|-536.249836|40/61;40/63|40/61;40/63|17/19;18/21|FAIL/FAIL/FAIL/PASS|
|[E604B](http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e)|N503|9055.465020|-4001.149895|-4273.246693|-8.2688|7541.712173|-3389.497571|36/57;36/59|36/61;36/63|13/19;14/21|FAIL/FAIL/FAIL/PASS|
|[E604C](http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b)|N503|9206.394154|-4033.048226|-4330.508359|-8.2804|7591.526558|-3411.888907|38/57;38/59|38/61;38/63|15/19;16/21|FAIL/FAIL/FAIL/PASS|
|[E605B](http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6)|N503|11674.378424|-1382.236491|-1654.333289|-7.4628|9928.724925|-1002.484819|41/59;41/61|41/61;41/63|16/19;17/21|FAIL/PASS/FAIL/PASS|
|[E605C](http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826)|N503|11883.704693|-1355.737687|-1653.197821|-8.1680|10026.747960|-976.667504|42/59;42/61|42/61;42/63|15/19;16/21|FAIL/FAIL/FAIL/PASS|

Columnas de matriz: sesión,semilla,neto,deltaN204,deltasemilla,DDmotor,neto+10bpsRT,delta+10N204,+5mesesactivosfull/all,+5mesescalendariofull/all,+5Qfull/all,puertasnominal/MQ/+10/DD. Todas diez fallan nominal y overlay+10 frenteN204; ninguna elegible aun cuando algunas pasan regularidad. Denominadores activos distinguidos de calendario61/63; trimestres19/21. Overlay conserva precios/cantidades/tiempos, no rerun o slippagepuro. Root confirmó auditorías financieras pasadas,31largosoriginales con tiempos preservados; no afirmar cantidades/PNLoriginales idénticos.

## E605 cobertura observable

En AMBAS carteras, log N503_R6_M1:115evaluaciones,46valid_pass,69valid_fail. clock_missing=0,corrupt=0,close_mismatch=0 (claves ausentes: contador nunca incrementado). Las115 sólo ocurren después de satisfacerse N204+ER por short-circuit, no equivalen a todos los instantes de mercado.46condicionesTrue no son46eventos: latch ygeometría reducen a37eventos;6ocupados y29fills/closes. IdentidadCúltimoM1=C4h exacta; 240minutos contiguos cerrados yOHLCVválido, vol0admitido. La hipótesis fue observable en esas115evaluaciones: el resultado inferior no procede de cobertura faltante/mismatch registrado.

## QA, preservación y límites

196comprobacionessintéticasPASS(jobc93ea284cfff4f98883ebb99b7943f0f); previas194PASS(job5d43e8e4530140119ca8d5f7a975dcba). Revisiónroot solicitó shape guard para M1vacío1D/2D: cambio sóloE605 antes de cualquierE605full; ambosdrafts refrescados. No reparaciones ni reruns económicos. Readback final5/5fuentesbyteidéntico. Métodos protegidos/imports/constantes/ER/risk/sizing/HP preservados; before sólo nuevo ANDgate, labels yhelper; E605observacionallog. E601..604sinmutacionestrasfreeze.

Ventana2020-10-15→2025-12-31EXCLUSIVA, último día2025-12-30.10000shared,1%trade/8%total,isolated5x,nopyramid,cap4.4,reserva.001sizing,fee.00045/lado;3rutasBTC/PAXG/SPY4h+3feeds1m,w240debugtruefastfalsecharttrue. PAXGfeeBEoriginal,SPYBSecond/CMarket. No2026, live/paper/funding/imports/framework/config global ni research_scripts.

Se revisaron de manera independiente las cinco fuentes P601..605 sin hallazgosaccionables; informe enlazado abajo. Esa revisión de código no es otra reconstrucción del MTM. Muestra muy reutilizada y selección múltiple; no pruebaanti-sobreajuste/OOS. No promoveralfa aisladopor resultadoscartera ni perseguirunmesespecífico. N204referenciacongelada;N503exploratoria intacta. Ceroejecucionesadicionalesautorizadasenestafamilia.

## Evidencia

- [Freeze](../../MultiAssetRetestBtcShort4h/reports/N503_R6_FROZEN_PROTOCOL_20261019.md).
- [Matrizroot](../../MultiAssetRetestBtcShort4h/reports/N503_R6_RESULTS_MATRIX_20261019.md).
- [QA](N503_R6_E_IMPLEMENTATION_QA_20261019.md).
- [Harness](N503_R6_E_SOURCE_QA_HARNESS_20261019.md).
- [Registry10](N503_R6_E_DRAFT_REGISTRY_20261019.md).
- [Revisión independienteCapacity](N503_R6_INDEPENDENT_CAPACITY_SOURCE_REVIEW_20261019.md).

Recomendación: conservar resultados negativos; no nuevascombinaciones o umbralesposthoc. ConcluirjuntoalaramaCapacitybajolaspuertascongeladas; cualquier nueva ronda exige otra hipótesis/protocolo previo.
