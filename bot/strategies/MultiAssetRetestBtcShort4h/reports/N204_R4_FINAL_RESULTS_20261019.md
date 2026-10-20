# BTC N204 — resultados finales de la investigación R4

La ronda no encontró un reemplazo elegible para N204. Se completaron doce hipótesis, cuatro de entradas, cuatro de salidas y cuatro experimentales. Las doce reducen el neto nominal de la cartera frente a N204 tanto en B como en C. Se conserva N204 como referencia de investigación y no se promueve ninguna receta.

2026 permaneció cerrado, incluso a inspección. La ventana usada fue 2020-10-15 → 2025-12-31 exclusiva, con último día de precios 2025-12-30. Es una muestra de desarrollo intensamente reutilizada; esta búsqueda no es OOS ni demuestra ausencia de sobreajuste.

## Resultado económico

Referencias: [N204 B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) y [N204 C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794). Neto nominal: **13.056,61 / 13.239,44 USDT**. Cuenta inicial compartida de 10.000 USDT. Los números siguientes son del conjunto BTC/PAXG/SPY, después de comisiones nominales, no un supuesto alfa aislado de BTC.

|Hipótesis|Neto B, USDT — sesión|Neto C, USDT — sesión|Diferencia frente a N204, B / C|
|---|---:|---:|---:|
|E401 — Descenso de dos días UTC completos|[12.978,15](http://localhost:9200/#/backtest/a7f6ad5a-2cad-472b-a64d-04891efe2bb9)|[13.170,12](http://localhost:9200/#/backtest/31212719-83db-441c-9ee3-47831a918911)|-78,47 / -69,32|
|E402 — Presión vendedora en ambas mitades del patrón|[9807,36](http://localhost:9200/#/backtest/3c3ce364-65cc-4884-aa65-2a352376f1db)|[10.034,74](http://localhost:9200/#/backtest/8af24c45-cc64-4849-979d-7f257b791495)|-3249,25 / -3204,70|
|E403 — Mínimo descendente dentro del patrón|[10.603,42](http://localhost:9200/#/backtest/60611316-45f2-41de-81ab-fea3da810395)|[10.801,21](http://localhost:9200/#/backtest/8f1f15a5-aa3a-482e-a17d-1b1866cb52fe)|-2453,19 / -2438,23|
|E404 — Dominio del volumen de las velas con presión negativa|[11.945,57](http://localhost:9200/#/backtest/41656a8c-f89d-4066-825e-18fbf0716652)|[12.129,88](http://localhost:9200/#/backtest/a89b7159-58e9-4b23-ac39-976d2dbb96b5)|-1111,04 / -1109,56|
|T401 — Salida ante tres mínimos crecientes y ruptura alcista|[12.132,73](http://localhost:9200/#/backtest/6380d800-6891-4e12-9594-0d426aca366b)|[12.323,27](http://localhost:9200/#/backtest/51d79034-9d7e-44e8-aed9-084f8ea95538)|-923,89 / -916,17|
|T402 — Salida sin progreso favorable en seis velas completas|[12.217,28](http://localhost:9200/#/backtest/53d8a9f6-0c62-4f67-b2ba-8e098a09856f)|[12.440,76](http://localhost:9200/#/backtest/acf3f8be-7d9d-4b33-82f2-03024940fabc)|-839,34 / -798,68|
|T403 — Salida al recuperar la entrada tras adversidad de 0,5R|[12.996,09](http://localhost:9200/#/backtest/9014f7d9-fa7e-4af7-94b7-dc98940f21b8)|[13.175,12](http://localhost:9200/#/backtest/bd5f78dd-b730-48ad-ab01-e4c3f4726d29)|-60,53 / -64,32|
|T404 — Mitad a 1R y remanente a 2R, con precisión corregida|[11.712,87](http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333)|[11.877,89](http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0)|-1343,74 / -1361,56|
|X401 — Máximo menor confirmado y ruptura de soporte|[7731,93](http://localhost:9200/#/backtest/97c7fc93-a002-445a-b18d-43d33a4d31e6)|[7922,55](http://localhost:9200/#/backtest/a2555538-0233-44d2-974c-9ab78aefe7af)|-5324,69 / -5316,90|
|X402 — Fallo de aceptación por encima de un rango|[9159,75](http://localhost:9200/#/backtest/225f6073-dcee-4a04-856b-b0d448f9dc74)|[9330,52](http://localhost:9200/#/backtest/277a6cf9-8801-4cb2-9306-f68f211089e2)|-3896,86 / -3908,92|
|X403 — Dos velas interiores y ruptura de la vela madre|[7786,57](http://localhost:9200/#/backtest/9e5f78d7-5f2f-4e2a-8a03-05226769cdb5)|[8007,00](http://localhost:9200/#/backtest/21deebfc-94b5-48e0-9660-18fe1e206de4)|-5270,04 / -5232,45|
|X404 — Invalidación inmediata de un intervalo alcista sin solapamiento|[7577,45](http://localhost:9200/#/backtest/5c1c5772-7b01-4970-aea5-1677abd79af6)|[7775,43](http://localhost:9200/#/backtest/b1cad85f-ba07-4931-a6e1-2d9703b53584)|-5479,16 / -5464,01|

El más cercano, T403, pierde 60,53 / 64,32 USDT. Tampoco mejora el neto bajo overlay de +10 bps RT. En B baja de 16/19 a 15/19 trimestres completos positivos bajo +5 bps, y de 17/21 a 16/21 incluyendo los parciales. No es una mejora de regularidad.

E401 reduce el drawdown nominal a −8,34% / −8,28% y mejora ligeramente el neto estático con +10 bps, pero pierde neto nominal y falla la regularidad trimestral. E404 mejora algunas proporciones mensuales: bajo +5 bps B tiene 42/59 meses activos completos y 42/61 activos incluidos; C, 41/59 y 41/61. Sin embargo pierde unos 1.110 USDT por cartera, y B falla la regularidad trimestral. Ninguna compensación se convierte retrospectivamente en un criterio nuevo.

Las cuatro sustituciones experimentales del suplemento también pierden neto. X401 sólo produjo nueve suplementos por cartera: su resultado desfavorable no permite concluir que la idea sea universalmente inválida. Ninguna rama se rescató con otros parámetros, filtros combinados ni nuevas variantes.

La [matriz completa](N204_R4_RESULTS_MATRIX_20261019.md) conserva neto, +10, drawdown, meses activos y de calendario, trimestres, puertas y diagnósticos de recorridos para las24 sesiones válidas.

## Contrato y decisión congelados

Se mantuvieron los 10.000 USDT compartidos, riesgo de 1% por operación y 8% agregado, isolated5x, cap4,4, reserva0,001 sólo para sizing y sin piramidación. BTC/PAXG/SPY4h con tres feeds1m, warmup240, debug=true, fast=false y chart=true. PAXG mantiene PortComparePaxgMarket4h con su BE dependiente de fee original. B usa SPY Second; C, SPY Market. N204 y las fuentes anteriores permanecen intactas. Las nuevas clases son autocontenidas.

Fee nominal0,00045 por lado, 9bpsRT. Los overlays añaden5/10bpsRT por cada fill real conservando precio, cantidad y momento: no son reruns ni slippage puro. Se auditaron órdenes ejecutadas, cantidades, fees, PNL, wallet y liquidación terminal; el MTM diario UTC valora cada remanente de los parciales. El drawdown del motor y el de cierres diarios se distinguen.

Para ser elegible se exigía, en ambas carteras: neto nominal mayor a N204; al overlay+5, al menos65% de meses activos y80% de trimestres positivos tanto completos como incluidos; neto+10 no inferior; y DDmotor no peor que−25%. Se comparó sin redondear. El ranking predefinido sólo aplica a elegibles: mínimo margen de regularidad, mínimo incremento neto+10, menor peorDD e ID.

La selección es vacía. Por ello no correspondían los dos reruns con fee0,00070 ni los cuatro vecinos de target0,9/1,1. No se ejecutaron y no se eligió un segundo candidato.

Mantener N204 tampoco resuelve el objetivo de costes reales: las referencias previas [B con fee0,00070](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f) y [C con fee0,00070](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960), auditadas en R3, tenían39/61 meses completos positivos y39/63 incluidos en ambas. Son63,93% /61,90%, inferiores al65%. Se citan como antecedentes, no como pruebas nuevas ni como equivalentes a un overlay.

## Qué aportó el diagnóstico de N204

El observador reprodujo exactamente las273/280 operaciones de las referencias, incluidos fills, cantidades, fechas, precios, fees y PNL: máximoΔPNL0. Se recuperaron79 trayectorias del suplemento en cada cartera y se unieron por entrada a los trades reales; se verificaron también cierre, precio y cantidad. No se detectaron huecos entre los minutos elegibles. Son79 eventos compartidos por B/C, no158 observaciones independientes.

Hay19 objetivos2R,21 stops1R y39 cierres48h. Son42 operaciones positivas netas y37 no positivas. La MFE mediana observada es0,777R, frente a1,519R entre ganadoras y0,316R entre no positivas. La MAE mediana es0,583R. Las excursiones son cotas inferiores: se excluyen minutos parciales de entrada/salida y se desconoce el orden intraminuto.

Los horizontes6/12/24h sólo tienen74/66/51 supervivientes observables;5/13/28 operaciones habían cerrado. Clasificar por resultado final y condicionar a supervivencia es retrospectivo, no una regla disponible en la entrada. Ningún umbral de T se escogió después de ver el diagnóstico.

En T404 corregida se verificaron79 suplementos y34 operaciones con parciales por cartera:19 recorridos TP1→TP2 y15 TP1→timeout;21 stops y24 timeouts sin parcial. En esta muestra no apareció TP1→SL. El reparto de beneficios recortó las operaciones que llegaban a2R sin rescatar aquellas que acababan en el stop. Es una descripción de estas ejecuciones, no una ley para otros mercados o periodos.

Las reglas originales conservaron su código y prioridad, pero su ejecución puede desplazarse por ocupación: X402 y X404 retienen30/31 entradas largas BTC de N204. El resultado completo de cartera incluye esos efectos y el capital compartido; no se atribuye toda diferencia al suplemento por separado.

## Reparaciones técnicas y conteo transparente

Se realizaron **30 backtests**:24 originales de variantes +2 reruns T404 por precisión +2 diagnósticos originales +2 reruns de diagnóstico por corte de logs. La matriz definitiva tiene24 resultados válidos:22 originales y2 T404 reparados. Los dos T404 raw se conservan apartados. No son treinta hipótesis.

La API cortaba las líneas largas del journal cerca de2000caracteres. Se cambió únicamente su formato a una fila compacta por línea, sin modificar observación ni reglas, y se repitió B/C. Paridad económica exacta y79 filas completas confirmadas.

En [T404 raw C](http://localhost:9200/#/backtest/1eb1db8f-a2cc-466e-aba4-4c3e111911b7) quedó un residuo7e−18 después del TP2. Su valor era despreciable, pero mantuvo ocupada la ruta hasta48h y bloqueó un short original. Que la contabilidad cuadrara no probaba que la estrategia hubiera quedado plana.

La única reparación fue el guard0<qty<0,001 dentro del callback del suplemento: registrar y liquidar residuos menores al lote, sin mover entradas, objetivos, stop o deadline. QA41PASS y dos revisiones de fuente; un fallo previo del fixture está documentado. En [T404 corregida C](http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0), TP2 y el cierre del residuo ocurren realmente en1646405340000, y closed_at coincide. Reaparece el STOP original abierto1646410260000. B conserva exactamente el neto anterior; C sube de11.692,96 a11.877,89 por el recorrido corregido. Sigue perdiendo frente a N204.

No se modificó el framework, no hubo ejecución live/paper, instalaciones, funding ni nuevos datos.

## Cierre y continuación

Se cierra R4 sin reemplazo ni combinación de ganadores. El avance es una comparación reproducible de doce hipótesis, un diagnóstico de trayectorias y la detección de un defecto material de estado tras parciales. No es una mejora económica ni una nueva validación contra sobreajuste.

Antes de otra búsqueda sobre esta misma muestra, conviene formular una hipótesis distinta y un criterio falsable que atienda la regularidad bajo costes reales. Repetir filtros hasta conseguir un neto mayor aumentaría la presión de selección. N204 queda congelada y2026 sigue sin abrir. No se inició otra ronda.

## Evidencia y handoff

- [Protocolo anterior a resultados](N204_R4_FROZEN_PROTOCOL_20261019.md).
- [Matriz de24 resultados válidos](N204_R4_RESULTS_MATRIX_20261019.md).
- [Registro de30 sesiones, fuentes y QA](N204_R4_FINAL_SESSION_REGISTRY_20261019.md).
- [Código reproducible del auditor y ranking](N204_R4_AUDITOR_SOURCE_20261019.md).
- [Diagnóstico validado y límites](N204_R4_PATH_DIAGNOSTIC_INTERPRETATION_20261019.md).
- [Cuarentena T404 raw](N204_R4_T404_DUST_QUARANTINE_20261019.md).
- [QA real de reparación T404](N204_R4_T404_REPAIR_C_REAL_QA_20261019.md).
- [Familia de salidas](N204_R4_EXIT_FAMILY_FINAL_20261019.md).
- [Familia experimental](N204_R4_X_FINAL_QA_20261019.md).
- [Revisión independiente final de las24 filas](N204_R4_INDEPENDENT_FINAL_REVIEW_20261019.md).
- [Revisión independiente de fuentes y trayectorias](../../N204EntryR401/reports/N204_R4_INDEPENDENT_SOURCE_PATH_REVIEW_20261019.md).

Las auditorías por lote están en N204_R4_AUDIT_<lote>_20261019.md; T404_REPAIRED es autoritativo para la receta parcial, y T404 preserva el raw. Todos los backtests y trabajos de auditoría terminaron; no quedaron ejecuciones activas.
