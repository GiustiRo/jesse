# K1001 — protocolo mínimo de diagnóstico de registros

Fecha: 2026-10-21. Estado: código propuesto para revisión root; NO ejecutado. Sin nuevas estrategias, drafts, motores, velas, importaciones o comparaciones de derivados.

## Alcance y riesgo

Universo único: [K1001 BTC aislado histórico](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4),192trades,UTC[2020-10-15,2026-01-01),10.000USDT,2%poroperación histórica/6%global/3xaislado,fee.00045porlado,fundinghistóricoON yslippage0. N204 queda fuera del primer análisis mínimo: no hace falta para exportar identidad yatribución delKactual. No comparar retrospectivamente derivados.

El usuario autorizó NUEVA línea futura BTC conriesgototal2%: dosoperativas1%cada o tres2/3%cada,sobremismaequitytotal,sinredistribuir automáticamente cupoinactivo;límiteglobal6%/aislado3x. Este acuerdo no cambia los trades históricos ni permite reetiquetar sus resultados como si hubiesen usado ese reparto. Sólo BTC-USDT;USDC,simultaneidad/cuentas/hedge/importaciones requieren definición operativa separada. Funding sigue como coste de ledger, sin señalnueva.

## Entrada y ejecución futura

Un único input run_analysis:
```json
[{"session_type":"backtest","session_id":"94ec00b5-7541-4e9a-b685-a98160e1abd4","name":"K1001"}]
```

El snapshot completo suministra summary/metrics/trades/equity/hyperparameters. Código sólo lee inputs/K1001.json y escribe output/. Ninguna lectura delproyecto,base dedatos,credenciales,red o precio; tampoco jobs anidados. No se ejecutará hasta revisión root del protocolo y código. El código exacto se guarda en K1001_DEEP_DIAGNOSTIC_CODE_20261021.md.

Salidas:
- output/k1001_trade_metadata.json: archivo completo de192filas de identidad,tiempos,side,entry/exit/qty,gross/fee/funding/net,órdenes exportadas y evidencia de stopinicial si existe. origin queda null.
- output/k1001_trade_metadata_part_1.json a part_3.json: partición mecánica de64registros, JSONcompacto<128000caracteres porparte, sin muestreo. Leer estaspartes porMCP evita el límite128K dellector deartefactos; elresumen registraoffset,N ySHA256UTF8 de cada parte. La unión root exige192IDúnicos y cobertura completa de las3partes.
- output/k1001_diagnostic_summary.json: resumen global y cohortespor añoUTCdeapertura/cierre2020–2025, ALL/long/short;2020 parcial, ningún retornoMTM anual porcomponente.

PNL/feesglobales se verifican contra metrics y final−10000. Funding ausente en untrade conserva null yflag; suma de campos presentes no se vende como ledgercompleto. Se reportan IDsfaltantes para cotejo posterior con movimientos vinculados. Nunca inferir funding cero delresiduo.

## Evidencia de riesgo inicial

No inferir distanciainicial de la pérdida final. Para usar un STOP inicial exportado se exige único reduce_only,submitted_via=stop-loss,tipoSTOP,created_at=opened_at,mismalado/qtyy campo submitted_price explícito positivo. Se toma triggeroriginal, NO price de ejecución que puede haber sufrido gap. Si el snapshot no exporta submitted_price, evidencia unavailable/null; no se cae a precioSLrealizado, duración, TPausente o PnL.

Se exportan price_risk y stop_plus_fees_risk sólo cuando la evidencia existe. No son actual_loss de R16: este último además incluye reserva.001 de sizing. Tampoco riesgo máximo garantizado, saldoalentrar o rendimiento independiente. Los logsR16_LEGACY_OPEN aportarán después distance/actual_loss/risk_budget autoritativos, al unir por identidad.

## Unión de origen en root y límites

Root puede recuperar porMCP logs bounded/completos y unirlos enJavaScript alartefacto192, sin incrustarloscomoarrays en elharness. Usar TODOSlosR16_LEGACY_OPEN, con matchúnico opened_at+lado+qty+entry_price, y comprobación de R16_LEGACY_CLOSE/closed_at/net. No deduciroriginporoutcome,STOP,tamaño,duración o barrerasfaltantes. Duplicados/ausentes→UNATTRIBUTED; no forcejoin. Validar192filas,31LONG_RUNNER/116CORE_SHORT/45SUPPLEMENT y ledger neto10650.419092/4686.298492/9191.971407USDT con precisión completa delreciboP. Si unjoinnoesúnico, deteneratribucióncompleta yreportarlo.

El job no recibe ni requiere un mapa embebido. Root conserva recibos de páginasMCP, maparesultante y códigoJS exacto para reproducibilidad. No hace falta modificar fuentes ni construir undisfrazdebacktest para recuperar origin.

Despuésdeljoin, pueden cruzarse cohortespororigen×año yconcentración/exposiciónREALIZADA. PNLpor año de cierre oapertura no es rentabilidadMTManualdelcomponente. Long está identificadocomorunnerpordiseño; shorts siguen agregadoshasta mapa, sinmezclarCOREysuplemento.

313planes,121cancelaciones y82eventos de suplemento ya acreditados NO son eluniverso completo de setups. No transformar82−45 en37tradescensuradosporocupación. El contadoroccupiedno se emitió; logs ytrades permiten describirposición/pendientes realizados, no qué habría ganado una rama liberada.

## Interpretación prefijada y control de alcance

El primerjobproduce registros descriptivos; no optimiza entradas,salidas,umbral,régimen,gestión,riesgo oasignación. PF de grupos es descriptivo y queda null sin pérdidas; Npequeño/cerotrades no generaedgeprobado. No postular3estrategias rentables porque elledgerhistórico de3componentes sea positivo. No reportarCAGR/DD/M65standalone niMFE/MAE sin datos que lo sostengan.

El bloque creativo continúa como propuesta documental independiente deldiagnóstico, sin rescatar lados/meses observados. Decisiones posteriores de divisiónoperativa necesitan contrato de ejecución/gestión/riesgo ypresupuesto predefinidos; no están implementadas aquí.

Reutilizar Pcontabilidad/telemetríacomoancla. Guardarcode exacto,job,inputs/recibos/artefactos yjoinJS después de aprobación; máximo1analysisglobal coordinado. Hoy:0jobs. El código no declaraN204controlohabilitación de nuevaeconomía2026.

## Precisión de secuencia vigente

Primero comprender K1001 mediante preguntas y respuestas sobre sus registros; luego se debatirán experimentos. Este diagnóstico estadístico de evidencia existente es la fase actual permitida; no autoriza nuevas corridas de estrategias. El mapa de origen usa etiquetas REALES R16_LEGACY_OPEN/R16_LEGACY_CLOSE/R16_LEGACY_STATS. Root recuperará todas las páginas del log de753219bytes y hará el join mecánico con las192filas exportadas; ningún array de logs se incrusta en el códigoanalysis. K1001 es el único input de este primer diagnóstico.
