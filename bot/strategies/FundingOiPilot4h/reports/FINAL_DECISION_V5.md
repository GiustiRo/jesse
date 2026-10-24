# V5 — decisión final: sin candidata

Fecha local: 20 de octubre de 2026. Ciclo completo; auditoría independiente económica final PASS, sin discrepancias materiales. Ninguna finalista supera los requisitos nominales ni la robustez conjunta. El objetivo de 20–30% anual no se alcanzó.

## Replays continuos, 2024–2025

Cuenta inicial de 10000 USDT por variante, 2024-01-01 → 2026-01-01, 731 días; capital, historia OI y cuotas continuos. Cuatro ventanas semestrales separadas y cuatro bordes, sin reinicios de saldo.

| Variante | Neto total | CAGR 365/731 | PF | DD del motor | Trades | Semestres positivos |
|---|---:|---:|---:|---:|---:|---:|
| [Funding + OI](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) | −6,866518% | −3,489614% | 0,853912 | 17,669256% | 84 | 1/4 |
| [Funding sin OI](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) | −2,079607% | −1,043844% | 0,960575 | 14,311619% | 107 | 2/4 |

Nominal exige neto > 0, PF ≥ 1,2, DD ≤ 25%, N ≥ 100, al menos 3/4 semestres positivos y CAGR ≥ 15%; la meta orientativa es 20–30%. OI falla cinco de seis requisitos; FP falla cuatro. Tener 107 trades no compensa una expectativa negativa. No se suman operaciones entre variantes ni se reduce el umbral para aprobar N84.

Semestres del replay, por equity:

- OI: 2024 H1 −2,753076%; H2 +2,047041%; 2025 H1 −2,934627%; H2 −3,313638%.
- FP: 2024 H1 −2,717045%; H2 +0,435760%; 2025 H1 +1,379702%; H2 −1,145370%.

## Selección congelada y alcance real

Seis SCREEN de tres mecanismos nuevos. VWAP PV/PVOI fallaron neto/PF/DD. CROSS P/POI y FUNDING FP/FPOI sí fueron elegibles según N30/neto/PF/DD y al menos dos de los tres años completos 2021–2023 positivos.

El ranking prefijado priorizaba menor DD absoluto, luego PF, turnover, cantidad de features OI e ID. Con un máximo de dos finalistas, seleccionó Funding FPOI (DD 13,02295%) y FP (15,72361%) antes que CROSS P (17,69554%) y POI (22,66619%). Shortlist documentada antes de economía 2024–2025.

**CROSS no falló una confirmación futura: no fue confirmado por el límite y ranking.** CROSS P tenía CAGR de desarrollo 21,3292%, neto 90,5292% y PF1,7118; ese resultado de entrenamiento no es una aprobación histórica 2024–2025. No se cambia el ranking al observar que Funding pierde.

Las cuatro decisiones TRAIN se guardaron antes de sus evaluaciones. Ambas finalistas cumplieron N30/neto/PF/DD en C1–C4; el selector global eligió OI en los cuatro por menor DD. No se agregó CAGR o filtro anual al TRAIN. FP siguió como diagnóstico individual, sin cambiar retrospectivamente la política global.

| Corte | PF train OI | PF train FP | Elegibles | Selector |
|---|---:|---:|---|---|
| C1 |1,505844|1,362704|Ambas|OI|
| C2 |1,367147|1,267817|Ambas|OI|
| C3 |1,374710|1,264905|Ambas|OI|
| C4 |1,267955|1,234976|Ambas|OI|

El índice hipotético encadenando evaluaciones reseteadas dio −4,9980%/N83 para OI y −2,0831%/N107 para FP. **No es el replay.** La cuenta continua OI ejecutó N84 y terminó −6,8665%. La confrontación V5_REPLAY_VS_WF_ENTRY_COMPARISON.json encuentra las 83 entradas WF en replay y exactamente una extra: short 2025-01-01 04:00 UTC, stop 2025-01-03 18:45 UTC, PNL −195,5020 USDT. El replay conserva la referencia OI 2024-12-31 04:00 UTC (90681,416 frente a actual 91170,567). C3V independiente inicia sin esa observación T−24h y no hace backfill. Las 83 entradas comunes conservan precios y cierres dentro de 1e−6. La continuidad de historia cambia las condiciones iniciales; no se fuerza igualdad de trades, PNL o capital ni se reemplaza el motor por una multiplicación de retornos.

## Costes, vecinos y lag: todas las pruebas completadas

Las celdas muestran neto / DD del motor, con enlace a cada sesión.

| Escenario | OI: neto / DD | FP: neto / DD | Resultado |
|---|---:|---:|---|
| NOMINAL | [-6.8665%](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) / 17.6693% | [-2.0796%](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) / 14.3116% | Ambas rechazadas |
| S1 | [-10.1436%](http://localhost:9200/#/backtest/61c51f03-91d9-4142-8ad5-3f52f19cf4cb) / 19.6391% | [-6.6435%](http://localhost:9200/#/backtest/12b33663-1fd7-4883-bb74-519549664e21) / 17.0251% | Ambas fallan neto > 0 |
| S2 | [-10.4184%](http://localhost:9200/#/backtest/e7846d15-86e3-4c78-a5c4-c34122b0d8f5) / 20.0301% | [-7.0322%](http://localhost:9200/#/backtest/ef49d5d4-f4b7-4754-a91d-ec13cc6b51c4) / 17.4835% | Informativo; ambas negativas |
| S3 | [-16.7205%](http://localhost:9200/#/backtest/3733bd0f-ab2d-4ef8-b520-8455c1ecb44f) / 24.0812% | [-15.6613%](http://localhost:9200/#/backtest/0d37d117-ee67-4dcb-a3bf-44e16ccd32ad) / 22.9697% | Ambas fallan neto > 0 |
| R09 | [-6.0348%](http://localhost:9200/#/backtest/8d8a26f8-89dc-4afb-818e-1a9b02093d04) / 18.5177% | [-0.4087%](http://localhost:9200/#/backtest/f7c84508-165c-4788-83fc-52a9bd048e19) / 14.4059% | Ambas fallan neto > 0 |
| R11 | [-6.6011%](http://localhost:9200/#/backtest/65d8ecaa-5769-45cd-a0d1-8ce5eac88c50) / 16.2159% | [-1.3897%](http://localhost:9200/#/backtest/bd499d4f-5b7f-4ae1-882b-fac50e6becf3) / 12.5209% | Ambas fallan neto > 0 |
| A09 | [-8.7738%](http://localhost:9200/#/backtest/37f3b888-9751-4521-96a1-1711768f37f6) / 19.5419% | [-1.5062%](http://localhost:9200/#/backtest/ec1db1af-39f4-4ad3-83b7-f481566578a6) / 12.1670% | Ambas fallan neto > 0 |
| A11 | [-9.9388%](http://localhost:9200/#/backtest/26d1d710-e190-40c2-ab35-c49622e8bca7) / 18.6664% | [-5.7669%](http://localhost:9200/#/backtest/f81ccfbc-4887-419a-9a5b-2d341b75c93e) / 16.5291% | Ambas fallan neto > 0 |
| LAG4H | [-10.9430%](http://localhost:9200/#/backtest/08c43974-9ebf-4015-a3bf-f31481bcadfa) / 20.6085% | [-2.0796%](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) / 14.3116% (reuse) | Ambas fallan neto > 0 |

S1: fee 0,0009 / slip 0; S2: fee 0,00045 / slip 5 bps; S3: fee 0,0009 / slip 10 bps. S2 es informativo. S1/S3, cada uno de los cuatro vecinos y lag aplicable deben conservar neto positivo y DD ≤ 25%.

R09/R11 cambian sólo stop de 3 ATR a 2,7 / 3,3 ATR. A09/A11 cambian SMA120/C30 de precio a 108/27 y 132/33; conservan los tres pagos publicados, hold de 180 barras, ATR14 offset0, sin TP/trailing. Lag OI agrega una barra de 4h al par de observaciones: target T−4h / ref T−28h, con calidad original. No retrasa precio/funding ni amplía freshness.

Calendario idéntico al nominal en todos los escenarios. Fee estresada entra en sizing; slippage usa fills adversos del motor y puede cambiar la secuencia. No hay descuento fijo ni selección de vecino ganador. **Todos los costes y los ocho vecinos fueron negativos; lag OI también negativo.** FP sin OI reutiliza nominal para el slot lag: no es otro motor.

Se ejecutaron las 17 corridas completas incluso cuando los nominales ya fallaban N, CAGR o semestres. Ninguna prueba pendiente ni variante rescatada.

## Diagnóstico económico

| Componente, USDT | OI | FP |
|---|---:|---:|
| Bruto |−455,927688|+115,914597|
| Fees |371,879079|491,457040|
| Funding |+141,154922|+167,581792|
| Neto |−686,651845|−207,960651|

FP obtiene un pequeño bruto positivo, insuficiente para cubrir fees incluso con funding favorable. OI presenta bruto negativo y los costes agravan la pérdida. Cortos:77/84 trades OI,98/107 FP; sus netos son −553,16/−342,17 USDT. No se construyen variantes long-only ni nuevos filtros a partir de esta descomposición.

Sensibilidades proxy-only/global funding ×0,5/1,5 están en los accountings completos, con cantidades originales. No son replays ni reparan las señales. Concentración y curva comparativa: V5_V6_REPLAY_COMPARISON.json; la eliminación descriptiva de ganadores no es una estrategia alternativa.

## Verificación, presupuesto y evidencia

- **37 motores económicos nuevos +3 slots reutilizados =40 slots**: SCREEN 6, TRAIN 8/EVAL 8, REPLAY 2, COST 6, NEIGHBOR 8, LAG 2. Reusos: dos TRAIN C1 y lag FP. Tres smokes técnicos separados; 40 motores nuevos en total, todos finished/errornull.
- 412 checks iniciales core/sectores; 14 wrappers WF; 11 wrappers replay con readback exacto y 1002 checks compile/AST/hash/fixtures. Auditoría independiente global 67/67 fuentes, ocho selecciones y 12 starts de evaluación PASS.
- 17 auditorías de ejecución y nueve accountings completos de fase C; todos PASS técnicos. Los 37 resultados económicos se concilian con snapshots completos, no paginaciones parciales. Error máximo 3,64e−11 USDT, tolerancia1e−6.
- Fechas/asof/qty/fees/cap 1x/riesgo 2%/fills/callbacks/calendarios/funding/24 meses/732 puntos diarios/4 semestres revisados. Estáticos no acreditan fills del broker ni ramas que el motor no ejercitó.
- Timeouts de start conservados y recuperados leyendo el mismo ID; ninguna repetición económica. Reparación del artefacto estático a output/ documentada, sin cambios de fuente ni parámetros.
- REGISTRY_V5.json; V5_FINAL_SESSION_INVENTORY.json; V5_FINAL_ACCOUNTING_INDEX.json; V5_FUNDING_WF_FINAL_REPORT.md; V5_FUNDING_REPLAY_STRESS_FINAL_REPORT.md; V5_REPLAY_STRESS_BRANCH_SUMMARY.json; V5_REPLAY_VS_WF_ENTRY_COMPARISON.json; V5_REPLAY_STRESS_BRANCH_PROGRESS.json; nueve V5_REPLAY_*_ACCOUNTING.json; V5_REPLAY_SOURCE_VERIFICATION.json; V5_V6_WF_CALENDAR_FINAL_INDEPENDENT_AUDIT.md; V5_V6_FINAL_ECONOMIC_INDEPENDENT_AUDIT.md.

![Cuentas continuas comparadas](V5_V6_REPLAY_EQUITY.svg)

2024–2025 ya se usó en ciclos anteriores: es confirmación histórica adaptativa, no una muestra prospectiva virgen. 2026 sigue cerrado; FINISH 2026-01-01 excluye velas/funding de 2026. Sin ML/live/paper/cuentas/Pi, cambios de backend o paquetes. Conclusión: se completa V5 con evidencia negativa y ninguna candidata aprobada.
