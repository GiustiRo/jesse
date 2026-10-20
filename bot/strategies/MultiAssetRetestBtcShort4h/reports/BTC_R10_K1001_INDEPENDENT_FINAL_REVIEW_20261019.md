# R10 — dictamen independiente final K1001

## Conclusión

Las ocho corridas y las comparaciones publicadas son coherentes con el protocolo congelado. Se cumple el diagnóstico operativo de estabilidad de costes y vecinos TP. K1001 merece conservarse como candidata de investigación congelada; esta conclusión no es aprobación automática ni prueba de ausencia de sobreajuste. La muestra incremental de cinco entradas y la concentración en julio2024 continúan siendo las limitaciones principales.

199 comprobaciones PASS sobre la matriz, cuatro informes financieros, referencias emparejadas, métricas motor, metadata, periodos, bootstrap y manifiesto. Cero nuevos jobs, backtests o cambios de fuente durante esta revisión final. La reconstrucciónMTM de los tres niveles se realizó antes en los tres jobs de incertidumbre autorizados, con cuatroanclas y seis targets cadauno.

## Pruebas operativas y comparadores

Fee.00070:K1 mejoraN204+654.04/+653.18USDT yY902+127.40/+144.93. Fee.00095:mejoraN204+715.29/+772.62 yY902+127.12/+156.18. Comparaciones aMISMOfee, B/C separados;DDmotorentre−9.06%y−9.30%, porencimadel límite−25%. Se recalcularon los diferenciales desde netos de referencias guardados, coinciden con bootstrap. Es resistencia relativa favorable; pagar másfee reduce el neto absoluto. Feeengine afecta sizing, capital, BEPAXG y ocupación; no es slippage puro ni prueba de liquidez/latencia/rechazos.

TP1.8R:neto13256.82/13466.39;ΔN204+200.20/+226.95;ΔY902TP1.8R+172.24/+172.87. TP2.2R:neto13540.35/13757.39;ΔN204+483.73/+517.95;ΔY902TP2.2R+187.70/+193.62. AmbosvecinosnetpositivoysuperanN204enambas, satisfacen diagnóstico prefijado. Son controles no seleccionables: mantener2R congelado, no elegirvecino ni afirmar gridTP×fee. Losdiferenciales contraY902usan vecinoscorrespondientes; no confundir conY9022R. Ambosvecinos quedan por debajo deK1nominal2R, sin implicar que2Rse haya vuelto a optimizar.

El criterio R10 de costes usa retención de neto yDD, no exige que toda combinación de feeengine+overlay conserve65%meses. Lasfilasestresadasmásoverlay+5 no superan todasese65%:K170incl39/62y40/62;K19536/62y37/62. Full/included ycalendario/activosse verificaron contraauditorías. No describir la estabilidad favorable como regularidad intacta bajo todosloscostes, ni convertir esaobservación en nuevo gateposthoc.

## Incertidumbre y concentración

Los seis IC95%primarios61meses K1vsY902incluyencero; también los seis secundarios K1vsN204. Mismos índices porB/C, comparadores yfees: circular6meses,10000,seed9022026. HashesidénticosR9/R10. Fracción de réplicas positivas no es probabilidad de edge ni corrección por búsqueda acumulada. B/C no son evidencia independiente.

Ennominal63,la ventajaK1vsY902+172.98/+173.98se reduce a+4.27/+3.25aldescontar el mejor mesincrementaljulio2024. Confee70queda−33.66/−17.83;confee95−24.38/−0.15. Omitir2024deja diferencial primario negativoambas carterasenlos tresfees. Estas restas son contabilidad descriptiva sobrecarteras registradas, sin replay decapital; no son una estrategia ejecutada sinelmes o sin2024. No se propone un filtro para esasfechas.

CincoentradasmodificadasnominalesfrenteY902siguen siendo pocas aunque se repita la mismamuestra confees yTPvecinos. Validar nuevamente no aporta nuevastrayectorias de mercado ni levanta automáticamente el mínimo de diez cambiosdelR9. El progreso acumulado contraN204espositivo,pero la comparación primaria contraY902revela la concentración del refinamientoK1. K1005permanece hallazgo separado sinheredar estaspruebas.

## Evidencia y trazabilidad

Se releyeron protocoloBTC_R10_K1001_FROZEN_VALIDATION_20261019.md,matrizBTC_R10_K1001_RESULTS_MATRIX_20261019.md,manifiestoBTC_R10_K1001_FINAL_MANIFEST_20261019.md ycuatroreportesBTC_R10_AUDIT_K170/K195/K118/K122_20261019.md dentrode strategies/MultiAssetRetestBtcShort4h/reports/. Cadaauditoría declara auditpassed/MTMterminaltrue; conciliadas neto/fees/turnoveroverlay ymétricasmotor,connullpreservado. Los contadores open_trades/open_pl históricos puedenserpreterminales, no residualsinexplicar.

Manifiesto:8fullsfinished,4jobsfinancierossucceeded,8formularios/24snapshots y46readbacksfuenteexactossegúnregistro;metadata45suplementos identificados44STOP+1MARKETporfila. STOP noidentificacortooriginal. Revisión delregistro,nolecturadirecta nueva de46fuentesenestecierre. Concurrenciamáxima2fulls/1analysissegúnmanifiesto;sinextras niretuning. RecuperaciónMCP autorizada antesdereanudar; limpieza sólo workspaces previamente archivadossegúnmanifestcentral,fuentes/sesionespreservadas.

Muestra2020-10-15→2025-12-31exclusiva,últimosprecios2025-12-30,2025parcial.2026cerradoinclusoinspección. Código y prioridades preservados no garantizan todaslas operaciones ni cantidades iguales debido acapital/ocupación. La tabla94sesionesdelroot es trazabilidad de ejecución y métricas, no94confirmaciones independientes: preservar distinción controles/duplicados/exploración/validación yfee/TP comparables. Esta revisión no auditóindividualmente esas94filas.

Incertidumbre reproducible: BTC_R10_UNCERTAINTY_SOURCE_20261019.md yBTC_R10_UNCERTAINTY_RESULTS_20261019.md, tresjobs06d54a66948049e6859e98945dbc9063/682a5aebf0314aa982c542b1b6b6ff77/775b60fa9ff24d18bfe5466991dac050. DieciochotargetMTMreconstruidos;66checksnuméricos/hash/triánguloprevios, sin repetir bootstrapparaseleccionarresultado.

## Sesiones

- K170B: http://localhost:9200/#/backtest/4d403a37-8248-4346-8da5-708b68bdf00b
- K170C: http://localhost:9200/#/backtest/3c84ed42-1d2a-4cf6-bd29-0daba6830eb9
- K195B: http://localhost:9200/#/backtest/03ff99f8-aabc-400d-a570-13f77c1e8495
- K195C: http://localhost:9200/#/backtest/002a9700-0279-4a8f-a103-ddaab681878c
- K118B: http://localhost:9200/#/backtest/e989cc4d-480c-4851-a7ab-3a289877d3b7
- K118C: http://localhost:9200/#/backtest/f8e610f4-d2f3-413a-ae75-3aadbdceff6a
- K122B: http://localhost:9200/#/backtest/48c209a0-4ce7-466d-97c5-bf2e404a21c3
- K122C: http://localhost:9200/#/backtest/b39efb8b-8535-42cc-8151-018661c0d336

## Comprobaciones de cierre

```json
[
  {
    "name": "eightUniqueRows",
    "pass": true
  },
  {
    "name": "K170B:feeMatched",
    "pass": true
  },
  {
    "name": "K170B:targetR",
    "pass": true
  },
  {
    "name": "K170B:deltaN204",
    "pass": true
  },
  {
    "name": "K170B:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K170B:auditFinance",
    "pass": true
  },
  {
    "name": "K170B:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K170B:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K170B:DD",
    "pass": true
  },
  {
    "name": "K170B:counts",
    "pass": true
  },
  {
    "name": "K170B:metadata",
    "pass": true
  },
  {
    "name": "K170B:overlays",
    "pass": true
  },
  {
    "name": "K170B:monthFullActive",
    "pass": true
  },
  {
    "name": "K170B:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K170B:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K170B:quarterIncluded",
    "pass": true
  },
  {
    "name": "K170B:nullPreserved",
    "pass": true
  },
  {
    "name": "K170B:operationalCostCondition",
    "pass": true
  },
  {
    "name": "K170B:deltaOwnBootstrapMatches",
    "pass": true
  },
  {
    "name": "K170C:feeMatched",
    "pass": true
  },
  {
    "name": "K170C:targetR",
    "pass": true
  },
  {
    "name": "K170C:deltaN204",
    "pass": true
  },
  {
    "name": "K170C:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K170C:auditFinance",
    "pass": true
  },
  {
    "name": "K170C:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K170C:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K170C:DD",
    "pass": true
  },
  {
    "name": "K170C:counts",
    "pass": true
  },
  {
    "name": "K170C:metadata",
    "pass": true
  },
  {
    "name": "K170C:overlays",
    "pass": true
  },
  {
    "name": "K170C:monthFullActive",
    "pass": true
  },
  {
    "name": "K170C:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K170C:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K170C:quarterIncluded",
    "pass": true
  },
  {
    "name": "K170C:nullPreserved",
    "pass": true
  },
  {
    "name": "K170C:operationalCostCondition",
    "pass": true
  },
  {
    "name": "K170C:deltaOwnBootstrapMatches",
    "pass": true
  },
  {
    "name": "K195B:feeMatched",
    "pass": true
  },
  {
    "name": "K195B:targetR",
    "pass": true
  },
  {
    "name": "K195B:deltaN204",
    "pass": true
  },
  {
    "name": "K195B:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K195B:auditFinance",
    "pass": true
  },
  {
    "name": "K195B:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K195B:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K195B:DD",
    "pass": true
  },
  {
    "name": "K195B:counts",
    "pass": true
  },
  {
    "name": "K195B:metadata",
    "pass": true
  },
  {
    "name": "K195B:overlays",
    "pass": true
  },
  {
    "name": "K195B:monthFullActive",
    "pass": true
  },
  {
    "name": "K195B:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K195B:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K195B:quarterIncluded",
    "pass": true
  },
  {
    "name": "K195B:nullPreserved",
    "pass": true
  },
  {
    "name": "K195B:operationalCostCondition",
    "pass": true
  },
  {
    "name": "K195B:deltaOwnBootstrapMatches",
    "pass": true
  },
  {
    "name": "K195C:feeMatched",
    "pass": true
  },
  {
    "name": "K195C:targetR",
    "pass": true
  },
  {
    "name": "K195C:deltaN204",
    "pass": true
  },
  {
    "name": "K195C:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K195C:auditFinance",
    "pass": true
  },
  {
    "name": "K195C:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K195C:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K195C:DD",
    "pass": true
  },
  {
    "name": "K195C:counts",
    "pass": true
  },
  {
    "name": "K195C:metadata",
    "pass": true
  },
  {
    "name": "K195C:overlays",
    "pass": true
  },
  {
    "name": "K195C:monthFullActive",
    "pass": true
  },
  {
    "name": "K195C:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K195C:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K195C:quarterIncluded",
    "pass": true
  },
  {
    "name": "K195C:nullPreserved",
    "pass": true
  },
  {
    "name": "K195C:operationalCostCondition",
    "pass": true
  },
  {
    "name": "K195C:deltaOwnBootstrapMatches",
    "pass": true
  },
  {
    "name": "K118B:feeMatched",
    "pass": true
  },
  {
    "name": "K118B:targetR",
    "pass": true
  },
  {
    "name": "K118B:deltaN204",
    "pass": true
  },
  {
    "name": "K118B:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K118B:auditFinance",
    "pass": true
  },
  {
    "name": "K118B:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K118B:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K118B:DD",
    "pass": true
  },
  {
    "name": "K118B:counts",
    "pass": true
  },
  {
    "name": "K118B:metadata",
    "pass": true
  },
  {
    "name": "K118B:overlays",
    "pass": true
  },
  {
    "name": "K118B:monthFullActive",
    "pass": true
  },
  {
    "name": "K118B:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K118B:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K118B:quarterIncluded",
    "pass": true
  },
  {
    "name": "K118B:nullPreserved",
    "pass": true
  },
  {
    "name": "K118B:deltaOriginal2R",
    "pass": true
  },
  {
    "name": "K118C:feeMatched",
    "pass": true
  },
  {
    "name": "K118C:targetR",
    "pass": true
  },
  {
    "name": "K118C:deltaN204",
    "pass": true
  },
  {
    "name": "K118C:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K118C:auditFinance",
    "pass": true
  },
  {
    "name": "K118C:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K118C:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K118C:DD",
    "pass": true
  },
  {
    "name": "K118C:counts",
    "pass": true
  },
  {
    "name": "K118C:metadata",
    "pass": true
  },
  {
    "name": "K118C:overlays",
    "pass": true
  },
  {
    "name": "K118C:monthFullActive",
    "pass": true
  },
  {
    "name": "K118C:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K118C:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K118C:quarterIncluded",
    "pass": true
  },
  {
    "name": "K118C:nullPreserved",
    "pass": true
  },
  {
    "name": "K118C:deltaOriginal2R",
    "pass": true
  },
  {
    "name": "K122B:feeMatched",
    "pass": true
  },
  {
    "name": "K122B:targetR",
    "pass": true
  },
  {
    "name": "K122B:deltaN204",
    "pass": true
  },
  {
    "name": "K122B:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K122B:auditFinance",
    "pass": true
  },
  {
    "name": "K122B:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K122B:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K122B:DD",
    "pass": true
  },
  {
    "name": "K122B:counts",
    "pass": true
  },
  {
    "name": "K122B:metadata",
    "pass": true
  },
  {
    "name": "K122B:overlays",
    "pass": true
  },
  {
    "name": "K122B:monthFullActive",
    "pass": true
  },
  {
    "name": "K122B:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K122B:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K122B:quarterIncluded",
    "pass": true
  },
  {
    "name": "K122B:nullPreserved",
    "pass": true
  },
  {
    "name": "K122B:deltaOriginal2R",
    "pass": true
  },
  {
    "name": "K122C:feeMatched",
    "pass": true
  },
  {
    "name": "K122C:targetR",
    "pass": true
  },
  {
    "name": "K122C:deltaN204",
    "pass": true
  },
  {
    "name": "K122C:deltaY902Matched",
    "pass": true
  },
  {
    "name": "K122C:auditFinance",
    "pass": true
  },
  {
    "name": "K122C:netMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K122C:feeMatchesEngineAndAudit",
    "pass": true
  },
  {
    "name": "K122C:DD",
    "pass": true
  },
  {
    "name": "K122C:counts",
    "pass": true
  },
  {
    "name": "K122C:metadata",
    "pass": true
  },
  {
    "name": "K122C:overlays",
    "pass": true
  },
  {
    "name": "K122C:monthFullActive",
    "pass": true
  },
  {
    "name": "K122C:monthIncludedActive",
    "pass": true
  },
  {
    "name": "K122C:monthIncludedCalendar",
    "pass": true
  },
  {
    "name": "K122C:quarterIncluded",
    "pass": true
  },
  {
    "name": "K122C:nullPreserved",
    "pass": true
  },
  {
    "name": "K122C:deltaOriginal2R",
    "pass": true
  },
  {
    "name": "B:twoNeighboursPositive",
    "pass": true
  },
  {
    "name": "B:atLeastOneNeighbourDeltaN204",
    "pass": true
  },
  {
    "name": "C:twoNeighboursPositive",
    "pass": true
  },
  {
    "name": "C:atLeastOneNeighbourDeltaN204",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_Y902included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "nominalK1001_vs_N204included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_Y902included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F70K1001_vs_N204included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_Y902included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204full61B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204full61B:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204full61C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204full61C:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204included63B:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204included63B:indicesPaired",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204included63C:CIContainsZero",
    "pass": true
  },
  {
    "name": "F95K1001_vs_N204included63C:indicesPaired",
    "pass": true
  },
  {
    "name": "manifest8Rows",
    "pass": true
  },
  {
    "name": "manifest24Snapshots",
    "pass": true
  },
  {
    "name": "manifest46ExactSources",
    "pass": true
  },
  {
    "name": "manifest4Audits",
    "pass": true
  },
  {
    "name": "manifestConcurrency",
    "pass": true
  },
  {
    "name": "manifestFrozenEvaluation",
    "pass": true
  }
]
```
