# Auditoría económica independiente final V5/V6 — PASS FINAL

Autor: /root/audit. **PASS de integridad y cierre del alcance; ninguna candidata aprobada.** Revisados los25runs únicos de faseC, los inventarios finales y las decisiones consolidadas. Sin motores/jobs nuevos, cambios de fuentes productivas niREGISTRY.

## Resultado económico

| Nominal | N | Neto% | PF | DDabs% | CAGR%731d | Semestres+ |
|---|---:|---:|---:|---:|---:|---:|
| [V5 OI](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) | 84 | -6.866518 | 0.853912 | 17.669256 | -3.489614 | 1/4 |
| [V5 FP](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) | 107 | -2.079607 | 0.960575 | 14.311619 | -1.043844 | 2/4 |
| [V6 EFFICIENCY_P](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127) | 44 | 0.278594 | 1.006229 | 17.553569 | 0.139010 | 1/4 |

Gates nominales intactos: neto>0/PF≥1,2/DD≤25/N≥100/3de4semestres positivos/CAGR≥15%. V5OI falla cinco de seis; FP falla cuatro; V6 falla cuatro. Meta20–30%anual no alcanzada. No se suman trades ni se redondean criterios para promover.

V5:17corridas únicas de faseC, todas negativas, incluidos seis costes/ocho vecinos/lagOI. S1/S3 y todos los vecinos requeridos fallan neto>0. LagOI N87/net−10,942969%/DD20,608490%. FPsinOI reutiliza nominal para lag.

V6:8corridas únicas; S1/S3/R09/R11/A11 fallan neto>0. A09 pasa sólo neto/DD con+10,328758%,N50,CAGR5,030435%; no sustituye nominal ni cambia el calendario. Lag sinOI reutiliza nominal. S2informativo en ambas versiones. Robustez conjunta rechazada.

## Contraste final

Los25summaries fueron consultados primero, todosfinished/errornull. Config exacta nominal uoverlay de coste: S1fee.0009/slip0,S2fee.00045/slip5,S3fee.0009/slip10. Warmup240,10000,isolated3x,cap1x,risk2%stop+dosfees,datasets históricos,debug/fast solicitadostrue yfast efectivo false, exports/benchmarkfalse,4h/BTC-USDT/ventana2024Jan→2026Jan. N/neto/DD/fees/funding/saldo coinciden con filas completas de17archivos contables (9V5+8V6).

Reproducidos gross−fees+funding, partición exacta/proxy/desconocida, error<1e−6,24meses/732puntos diarios/4semestres y gates. CAGR usa365/731 sobre10000iniciales, incluido2025inactivo deV6. No se usan PNL de cierres para atribuir retorno semestral. Fee entra en sizing/fills del motor, no haircut posterior; planes/callbacks se apoyan en pruebas congeladas y auditorías completas de owners.

Calendarios inmutables: V5ambas ON enC1–C4; selectorOIenlos4. V6ON/ON/OFF/OFF porTRAIN;2024H1/H2separados y2025cash, cuatroFORCE_BOUNDARIES. No reabrirC4 por diagnóstico positivo. Vecinos/costes/lag conservan calendario nominal.

La diferencia OIWF83/replay84 está sustentada porV5_REPLAY_VS_WF_ENTRY_COMPARISON.json:83entradas comunes,sin faltantes ni diferencias materiales deprecio/cierre,una extra short2025-01-01 04:00UTC,PNL−195,502023USDT. Replay conserva referenciaOI24h previa;C3Vindependiente inicializa historia sinbackfill. Capital/qty/PNL siguen diferentes; esa entrada no permite atribuir automáticamente toda diferencia de rendimiento aOI.

## Inventario y presupuesto conciliados

| Ciclo | Económicas nuevas | Reusos | Slots | Técnicas únicas | Nuevas totales |
|---|---:|---:|---:|---:|---:|
| V5 |37|3|40|3|40|
| V6 |21|2|23|3|24|
| Nuevas V5/V6 |58|5|63|6|64|

64IDs globales únicos, todosfinished;58IDs económicos coinciden exactamente entre inventarios/registries/índices financieros.25faseC únicos=17V5+8V6;27slots con dos lags sinOI reutilizados.17slots económicosV6quedanunused,sin rellenar. AcumuladoV1–V6:209económicas/233slots/24reusos/23intentos técnicos. Las sesiones no son muestras independientes.

Errores financieros máximos del índice completo:V53.637978807091713e-11USDT/V62.9103830456733704e-11USDT, debajo1e−6. Evidencia owner:V5 17auditorías,74562barras/1621planes/37281SHA/68bordes;V6ocho auditorías/8126checks. El índice contiene37/21rows únicos completos y el inventario40/24sesiones.

## Decisiones y límites

FINAL_DECISION_V5.md,FINAL_DECISION_V6.md,consolidado yhandoff coinciden en ninguna candidata, objetivo no logrado, sin promoción deA09 niCROSS. **CROSSP/OI fueronSCREENeligible, excluidas por rankingDD/cap2; confirmación futura UNCONFIRMED, no FAILED.** No se ejecutó economía2024–25 paraCROSS.

Auditoría previa independiente de67fuentes/8selecciones/12starts conservada conPASS ysin incertidumbre material. Este pase no repitió hashes ni streams de logs. Las filas financieras proceden de snapshots completos; aquí se contrastaron contra summaries yse recalcularon identidades/gates agregados. Ledger/órdenes/equity completos ylogs/planes permanecen respaldados por auditorías originales separadas. Mocks no acreditan fillsbroker o ramas no ejercitadas.

2024–25 es confirmación histórica adaptada/reutilizada, **no prospectiva niOOSvirgen**.2026cerrado: todas ventanasfinish≤2026-01-01exclusive,fundingefectivo<finish. Un cierreTfinish basado enúltima vela2025no abre datos2026. Sin nuevos motores/jobs/paquetes/ML/live/paper/Pi/frameworkchanges.

No se detectaron discrepancias materiales. Las etiquetas pendientes en dosregistries/cuatroreportes son el marcador administrativo deliberado previo aestePASS. Root puede retirarlas ymarcar completo el trabajo autorizado; no requiere otro cálculo, cambio decriterios ni prueba económica. La rentabilidad objetivo sigue no alcanzada.

JSON acompañante:25checks por sesión, conteos/IDsets, comparación deíndices/matrices, gates y referencias. Fuentes principales:V5/V6_FINAL_SESSION_INVENTORY.json,V5/V6_FINAL_ACCOUNTING_INDEX.json,RESEARCH_COUNTS_V1_V6_20261020.json,V5_V6_ROOT_CLOSING_PROOF.json yaccountings referenciados.
