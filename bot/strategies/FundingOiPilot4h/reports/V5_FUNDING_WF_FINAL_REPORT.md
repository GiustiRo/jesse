# V5 Funding Trend — cuatro semestres completados

C1–C4 terminaron sin error de motor. En los cuatro cortes ambas finalistas fueron elegibles por TRAIN nominal; el ranking por menorDD eligió OI siempre. SELECTION_V5_C1..C4.json se guardaron antes de sus evaluaciones; los calendarios individuales contienen los cuatro semestres separados, definidos por TRAIN ysin alteración porPNL futuro. No se inició replay desde esta rama.

| Fold | OI trades | OI neto% seleccionado | FP trades | FP neto% diagnóstico |
|---|---:|---:|---:|---:|
| C1 | [14](http://localhost:9200/#/backtest/f9c5a6f5-e7f7-45f8-9cd4-c7f51bd977f0) | -2.756309 | [18](http://localhost:9200/#/backtest/b3a5c7e3-99b2-4540-a928-6927af51a602) | -2.720469 |
| C2 | [17](http://localhost:9200/#/backtest/6b6726e1-aea7-4b64-824d-a1cd2234fab9) | 2.047040 | [22](http://localhost:9200/#/backtest/b9581488-fa1a-4fb0-ad8a-925aaa434c80) | 0.435760 |
| C3 | [29](http://localhost:9200/#/backtest/13962ea9-197d-49b2-bb9a-69c6c7e7c038) | -0.983972 | [37](http://localhost:9200/#/backtest/14598ad7-2ac2-47e6-ba71-c7e9af290a55) | 1.379702 |
| C4 | [23](http://localhost:9200/#/backtest/82032d8e-1310-4dd7-acac-6f2688c3b738) | -3.313639 | [30](http://localhost:9200/#/backtest/579ef0bc-f58e-43d3-8be8-858c5744512c) | -1.145369 |

El selector OI suma83trades únicos,1/4semestres positivos yPF0.891599 sobre sesiones reseteadas. Su índice reescalado desde10000 termina9500.196030 (−4.998040%,CAGR−2.527633%). FP diagnóstico suma107trades,2/4semestres positivos,PF0.961694 eíndice9791.694750 (−2.083052%,CAGR−1.045583%). Índice significa reinversión proporcional al comienzo del siguiente semestre sobre curvas/capitales que cada motor dimensionó desde10000; NO es replay de cuenta continua. PF ysumasUSDT corresponden a sesiones reseteadas; no se mezclan trains solapados ni se reasigna el selector aFP. La evidencia de confirmación es desfavorable. La siguiente fase, si corresponde al protocolo global, permanece responsabilidad de root yno modifica estos resultados.

## Integridad y trazabilidad

Cada eval tuvo configuración nominal completa,fuenteswrappers inmutables yprotección3ATR/hold180barras4h. Todos los logs,publicaciones trío/SHA,planes/entradas/salidas,cuotasUTC,OI24h ybuckets de esta rama fueron revisados. C3/C4train también acreditan1maximum_hold real por cuenta. Cierre final se concilia después de counters: C1unforzado porcuenta,C2/C3/C4evalsinforzado. Metadataopen_pl/open_trades precierre no se interpreta como exposición residual.

Fullsnapshot deC1yC2train fue aprobado centralmente. Desdeautonomíaextendida se usó códigoexactoV5_V6_ACCOUNTING_CODE.json con_expectedconfig/ruta/fechas/timeframe ydatoscompletosinputs/→output/. Archivosduraderos:

- V5_C2V_ACCOUNTING_BRANCH.json,jobf7de9687311a4a099005e4571edb980c.
- V5_C3T_ACCOUNTING_BRANCH.json,job51a38cc26f48446fbc7d2baf07895743.
- V5_C3V_ACCOUNTING_BRANCH.json,job4b8c4b0ad6d34fd790ba3c686a129909.
- V5_C4T_ACCOUNTING_BRANCH.json,jobe71cdfe483354b22a853bf6759d4c835.
- V5_C4V_ACCOUNTING_BRANCH.json,job2bd9330ca47343579c7153aa1dd9693e.

TodosPASS, máxima desviación2.91e−11USDT; cada archivo conserva rowscompletos,calendarios,expected,manifiesto/job. GatesTRAIN sóloN30/net/PF/DD, sinannual/CAGRextra. El resultado deeval no cambia elegibilidad individual previa. AuditoríasAUDIT_<wrapper>.json guardan todosbuckets,manifiestos/muestras yrefs aENTRY_EVIDENCE por40trades como máximo. Se verificaron todosSHA pero no se duplican todaspublicaciones enlos JSON; permanecen enlogs originales. Ventanas deprecio verificadas porcontextos yfuentes/checks; no afirmar reconstrucción independiente decandles desde logs.

## Ejecución autorizada y límites

DesdeC2eval se conservó exactamenteUNmotorV5 porvez yUNjob propio máximo,segundo motorparaV6. Timeouts dearranque FP_C1V yFP_C4T devolvieron readtimeout10s; laslecturas recuperaron mismosesiones running→finished,sinreintentarstarts. Rawcompleto ytimestamps preservados. No cambiosdestrategia/datasets/gates,mainregistry,cuentas,2026 ni jobs ajenos.2024–25esreserva internareutilizada, noOOSvirgen.

V5_WF_BRANCH_SUMMARY.json resume loscuatrofolds,selecciones,IDs/URLs,convenciones,calendarios elegibles yjobs. V5_WF_BRANCH_PROGRESS.json conserva prerun/rawstart/estados/audits yV5_FUTURE_TRAIN_DRAFTS.json conserva la creación/readback de loscuatrotrains yausados. Reportes poretapa V5_C{1..4}_FUNDING_{TRAIN,EVAL}_REPORT.md (C1trainse reutilizóSCREEN). Rama terminada,ningúnmotor/jobactivo ysin nuevas sesiones propias autorizadas.
