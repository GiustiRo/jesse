# V6 — decisión final: sin candidata

Fecha local: 20 de octubre de 2026. Ciclo completo; auditoría independiente económica final PASS, sin discrepancias materiales. Objetivo del 20–30% anual no alcanzado. Ninguna variante se aprueba ni se habilita para trading.

## Resultado nominal continuo

[Replay Efficiency P](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127), cuenta inicial de 10000 USDT,2024-01-01→2026-01-01,731 días, capital continuo:

- Neto: **+0,278594%**; saldo final de 10027,85940464 USDT.
- CAGR 365/731: **+0,139010%**; PF **1,006229**; DD del motor **17,553569%**.
- **44 operaciones**, frente a 100 exigidas; **1/4 semestres positivos**, frente a 3 exigidos.
- Cumple neto > 0 y DD≤25%; falla PF≥1,2,N≥100,3 semestres positivos yCAGR≥15%. Meta orientativa20–30% tampoco se aproxima.

El denominador delCAGR incluye 2025 en efectivo. No se anualiza sólo el año activo ni se suman las 46 operaciones diagnósticas de los semestres inhabilitados.

## Screening y decisiones previas

Seis screenings de tres mecanismos nuevos, dos variantes cada uno. Sólo EFFICIENCY_P pasó N ≥ 30/neto/PF/DD y 2/3 años completos 2021–2023 positivos. EFFICIENCY_POI yNR7 fallaron PF/DD; deleveraging ambas variantes fallaron neto/PF/DD. Shortlist única congelada enFROZEN_SHORTLIST_V6.md antes de economía2024–2025.

| Corte | N de train | PF de train | DD de train | Calendario individual | Diagnóstico del semestre |
|---|---:|---:|---:|---|---:|
| C1 |148|1,247768|21,869573%|ON|+9,207450%|
| C2 |167|1,288431|21,869573%|ON|−8,176050%|
| C3 |192|1,180278|21,869573%|OFF porPF|−16,662574%|
| C4 |216|1,064928|31,494458%|OFF porPF/DD|+7,732447%|

Cada SELECTION_V6_Cn.json precede el start de su evaluación. Train sólo exige N ≥ 30/neto/PF/DD, sin añadir CAGR o filtros anuales. C1 reutiliza SCREEN exacto. C4 sigue OFF aunque su diagnóstico posterior resulte positivo. Calendario congelado en V6_REPLAY_CALENDAR.json: 2024 H1/H2 separados; 2025 sin exposición; cuatro bordes forzados,10000continuos sin reinicio de capital/historia. Saldo en 2025 constante dentro de tolerancia contable.

Semestres del replay: 2024 H1+9,207450%; 2024 H2−8,176050%; 2025 H1/H2~0%. El último residuo aritmético (~1e−13%) no constituye actividad económica.

## Robustez completa, calendario fijo

| Escenario | N | Neto | PF | DD del motor | Decisión |
|---|---:|---:|---:|---:|---|
| [NOMINAL](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127) | 44 | 0.2786% | 1.0062 | 17.5536% | Rechazado,4/6requisitos fallan |
| [S1](http://localhost:9200/#/backtest/f10942a7-0c80-4824-a972-7d3b284b05cf) | 44 | -1.9203% | 0.9570 | 18.6276% | Falla neto>0 |
| [S2](http://localhost:9200/#/backtest/445894c0-a830-45f8-8214-fe1454fc56ce) | 45 | -4.0276% | 0.9153 | 20.8753% | Informativo, negativo |
| [S3](http://localhost:9200/#/backtest/b7019ab0-8ade-4606-997f-1ccbfd618cc6) | 45 | -7.8957% | 0.8360 | 23.1713% | Falla neto>0 |
| [R09](http://localhost:9200/#/backtest/22d643fb-40aa-4425-b2b6-34c4e7df062c) | 45 | -0.4546% | 0.9910 | 20.2235% | Falla neto>0 |
| [R11](http://localhost:9200/#/backtest/f140ce43-60a0-49d1-a390-2e89f722b78a) | 44 | -0.5059% | 0.9877 | 16.4359% | Falla neto>0 |
| [A09](http://localhost:9200/#/backtest/90239e02-4fc6-420a-80f5-b9a57d843138) | 50 | 10.3288% | 1.2190 | 14.8855% | Pasa neto/DD; no promoción |
| [A11](http://localhost:9200/#/backtest/67851216-8941-4fbe-a0ea-ee8ff6bf5e63) | 41 | -2.5714% | 0.9371 | 19.8583% | Falla neto>0 |

S1: fee0,0009 / slip 0; S2: fee0,00045 / slip 5 bps; S3: fee0,0009 / slip 10 bps. R09/R11: stop2,25/2,75ATR; A09/A11: umbral0,315/0,385. Nominal: stop2,5ATR / umbral0,35 / hold de 60 barras, sin TP/trailing. Todos mantienen calendario y config restantes; nuevas cantidades/fills/capital en cada motor.

S1/S3, cada vecino y lag aplicable deben conservar neto>0/DD≤25. **Robustez conjunta falla** en S1/S3/R09/R11/A11. A09 pasa sólo ese gate local, pero no reemplaza al nominal: su CAGR 5,0304% / N50 tampoco cumplen los requisitos nominales. Lag sin OI reutiliza nominal; no genera otra sesión.

Costes entran en sizing: primera cantidad nominal de 0,14083594 BTC frente a 0,13695228 con fee doble. Slippage cambia también la secuencia (45 trades frente a 44), no es un descuento contable aplicado después. Evidencia: V6_REPLAY_COST_QUANTITY_COMPARISON.json.

## Diagnóstico contable y concentración

Bruto 508,137162 − fees 235,338240 − funding 244,939517 = neto 27,859405 USDT. Ledger de 532 cashflows, todos con mark exacto fundingRate.settlement_mark, sin proxy ni fuente desconocida en este replay.

Con cantidades fijas, multiplicar funding global × 0,5 deja +1,503292%; × 1,5 cambia el signo a −0,946104%. Sensibilidad proxy-only no cambia este replay porque no haymarksproxy. Son sensibilidades descriptivas, no nuevas ejecuciones.

Largos: 26 trades/neto+1007,36 USDT y cortos: 18/neto−979,50: se compensan casi totalmente. No se construye ni se promueve una variante long-only a partir de esta descomposición. Los cinco mejores trades representan el 77,15% del PNL positivo; excluir el mejor deja −909,42 USDT con cantidades fijas (diagnóstico, no estrategia).

## Verificación y presupuesto

- **21 motores económicos nuevos + 2 slots reutilizados = 23 slots**: SCREEN 6, TRAIN 4/EVAL 4, REPLAY 1, COST 3, NEIGHBOR 4, LAG 1. Reusos: C1 train y lag sin OI. Los 17 slots económicos restantes no se reasignan a tuning. Tres smokes técnicos separados;24 motores nuevos en total, todosfinished/errornull.
- 338 checks iniciales de core/sectores, 7 wrappers WF verificados, 5 wrappers de replay/readback y 606 checks. Auditoría independiente global: 67/67 fuentes y 8 selecciones/12 starts de evaluación PASS.
- Ocho replays/escenarios con snapshots completos y logs separados; 8126 verificaciones de ejecución PASS. Error contable máximo de fase C: 2,91e−11 USDT, tolerancia de 1e−6. Capital/fees/funding/qty/asof/24 meses/732 puntos diarios/4 semestres conciliados.
- Smokes y estáticos acreditan sólo las ramas ejercitadas. Cierres de borde con posición no observados en un motor no se dan por probados sólo por mocks.
- Starts con timeout guardados y recuperados por lectura del mismo ID; sin start duplicado. Ninguna modificación de fuentes congeladas, paquetes, framework o backend.

## Evidencia y límites

REGISTRY_V6.json;V6_FINAL_SESSION_INVENTORY.json;V6_WF_FINAL_REPORT.md;V6_REPLAY_STRESS_FINAL_REPORT.md;V6_REPLAY_STRESS_ROWS.json;V6_REPLAY_CONSISTENCY_AUDIT.json;V6_REPLAY_SOURCE_VERIFICATION.json;V5_V6_WF_CALENDAR_FINAL_INDEPENDENT_AUDIT.md;V5_V6_FINAL_ECONOMIC_INDEPENDENT_AUDIT.md;V5_V6_REPLAY_COMPARISON.json.

![Comparación de cuentas continuas](V5_V6_REPLAY_EQUITY.svg)

2024–2025 fue examinado en ciclos previos: esta confirmación histórica adaptativa no constituye una muestra prospectiva virgen ni demuestra rentabilidad futura. 2026 permanece cerrado; finish 2026-01-01 excluye velas/funding de 2026. No ML/live/paper/cuentas/Pi. La investigación V6 está completa y su conclusión económica es negativa; el resultado positivo de un vecino no cambia esa decisión.
