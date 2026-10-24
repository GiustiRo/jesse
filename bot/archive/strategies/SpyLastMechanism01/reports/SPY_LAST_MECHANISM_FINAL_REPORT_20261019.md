# SPY última ronda: seis contrastes del mecanismo BR02

Fecha local: 19 de octubre de 2026. Se completaron los seis fulls autorizados, sin modificar fuentes después de observar resultados. No quedan ejecuciones propias pendientes.

**La ronda mejora la evidencia de una selección más eficiente, pero no demuestra robustez fuera de muestra.** La segunda oportunidad exacta (MECH01), MARKET después de omitir la primera (MECH05) e inicio de rachas (MECH06) mejoran neto y DD observados frente a BR02. Sus muestras son 12, 19 y 12 operaciones. MECH04 reproduce exactamente BR02 y no constituye confirmación adicional.

## Matriz y contrato

- MECH01: sólo ordinal2 desde reset.
- MECH02: ordinal>=3.
- MECH03: sólo ordinal3.
- MECH04: ordinal2 o3.
- MECH05: ordinal>=2 original, cambiar entrada a MARKET actual, manteniendo elegibilidad inicial de frontera y recalculando sizing.
- MECH06: ordinal>=2, contando y operando sólo inicio de rachas de barras Cq calificantes consecutivas. False corta racha incluso ocupado; reset limpia prev_eligible.

Las fuentes autocontenidas SpyLastMechanism01..06 copian SpyStructR1BR02, que permanece intacta. Readback6/6 y revisión root antes de correr. Sólo predicado en before de01..04, repricing de _plan en05 y semántica de racha en before de06 difieren. Riesgo, gestión, helper fresh, ledger y cancelación permanecen originales. Root QA AST de métodos reales pasó113assertions en las12fuentes de ambos agentes, job e97c0f4493b449abba005c64ac9f4d48; es verificación lógica, no nueva evidencia económica.

Ventana 2020-10-15→2025-12-31 exclusiva;2026 cerrado. SPY4h+M1, warm240, fast/debugfalse. Calendario UTC Mon–Fri00–20 para historia y baropen00–16 para entradas. Capital aislado10.000, riesgo1%, fee0,00045 por lado en todos los tipos, isolated5x, cap4,4, reserva0,001 sólo sizing. Stop2ATR, BE2,25R, trail4,2 y tightening5R/8R. Proxies aceptados; sin datos nuevos, funding, BTC/PAXG, scripts, instalaciones, framework/config global, reinicios, live/paper/Pi o riesgo mayor.

before cuenta oportunidades antes de capital/margen/posición, también ocupado; eventos consumidos sin cola. Inicio censurado hasta reset observado al midpoint del canal26 PREVIO. MECH06 actualiza flags sólo en vela filtrada cerrada actual; quote ausente/regime/entrywindow False rompe racha según protocolo. Barras excluidas no forman observaciones. No inferir universos de oportunidades o sus outcomes desde los fills.

## Resultados económicos

Cq y BR02 son comparadores existentes, sin nuevas réplicas. Neto y PF después de fees; DD/Sharpe/CAGR del motor. Las cuentas aisladas no se suman.

|Política|N|Neto USDT|Fees|PF|Sharpe|DD motor %|Tiempo abierto %|Neto +10bps RT|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|31|751.35|286.48|1.49|0.458|-5.21|15.26|433.04|
|[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)|16|874.80|150.59|2.32|0.718|-3.80|8.79|707.47|
|[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)|12|1179.98|113.12|4.04|1.008|-2.49|8.13|1054.29|
|[MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e)|11|770.55|118.29|3.17|0.689|-2.33|5.65|639.12|
|[MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea)|10|697.97|106.07|2.97|0.673|-2.33|5.20|580.11|
|[MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05)|16|874.80|150.59|2.32|0.718|-3.80|8.79|707.47|
|[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)|19|1275.16|179.61|2.65|0.882|-3.57|11.41|1075.60|
|[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)|12|962.21|119.26|3.52|0.823|-2.93|6.64|829.71|

## Interpretación del mecanismo

**MECH01, segunda oportunidad exacta:** gana1179,98 con12 trades, Sharpe1,008 y DDmotor−2,49%. Conserva748,92 sin su mejor y200,13 sin las tres mejores operaciones. Su bruto1293,10 supera el de BR021025,39; la diferencia favorable no se explica sólo por fees menores. Las doce aperturas realizadas aparecen en BR02 al mismo precio; tamaños pueden cambiar por saldo y selección previa. Esto no equivale a intervenir sobre una cartera fija ni prueba que las segundas oportunidades omitidas siempre sean rentables.

**MECH02/03:** excluir ordinal2 conserva beneficio, pero menos neto que BR02:770,55 y697,97, con11/10 operaciones. Sóloordinal3 y todas>=3 no son idénticas; no sumar estos resultados a MECH01 para reconstruir BR02. Ocupación y saldo cambian.

**MECH04 es idéntica a BR02:** fingerprint completo de trades económicos y hash de equity_curve exactamente iguales,16/16 timestamps y precios comunes. Limitar a ordinal2/3 no cambió la trayectoria realizada. No demuestra que jamás existieran oportunidades>=4, ni sus outcomes. Entre los ocho snapshots hay siete trayectorias distintas; entre las seis nuevas, seis.

**MECH05, MARKET:** mayor neto1275,16, DDmotor−3,57%, Sharpe0,882 y19 operaciones. Mejora frente a BR02 en neto400,37 y conserva1075,60 con10bps extra. La exposición sube de8,79% a11,41%; retorno/ocupación/tamaño y gestión anclada a entry cambian. Sólo tres timestamps exactos de apertura son comunes y sus precios coinciden; no aislar la ventaja como mejor precio de ejecución sobre los mismos trades. El resultado de MARKET aquí difiere de MARKET incondicional de atribución anterior porque el generador selecciona posteriores al primer evento.

**MECH06, inicio de rachas:** neto962,21 y DDmotor−2,93% con12 trades. La mejora no desaparece al dejar de escalar ordinal en barras calificantes contiguas; esa repetición no parece indispensable para el beneficio global observado. No es atribución causal pura: redefine ordinales/eventos y cambia ocupación. Comparte11 aperturas exactas con BR02, no doce.

No seleccionar el mayor neto como una receta automáticamente aceptada ni combinar después ordinal2+MARKET+rachas: esa combinación no fue probada. Tampoco elevar riesgo para igualar ex post exposición.

## Concentración y costes

|Política|Neto +5bps RT|Sin mejor|Sin3 mejores|Sin3 mejores y +10bps RT|
|---|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|592.19|349.58|-298.22|-587.12|
|[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)|791.13|455.51|-86.36|-223.08|
|[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)|1117.14|748.92|200.13|105.62|
|[MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e)|704.83|347.63|-168.02|-268.04|
|[MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea)|639.04|277.90|-237.75|-324.26|
|[MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05)|791.13|455.51|-86.36|-223.08|
|[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)|1175.38|788.08|31.51|-136.13|
|[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)|895.96|539.57|57.73|-42.40|

El estrés predeclarado aplica2,5/5bps extra por lado sobre todos los fills, equivalente5/10bpsRT. Conserva decisiones y cantidades; reserva de sizing no representa coste de ejecución ya cobrado.

La última columna es **diagnóstico post hoc**, añadido después de ver concentración para evitar confundir dos pruebas separadas. Se fijan las tres operaciones de mayor PNL ORIGINAL y se aplica5bps por lado sólo sobre fills restantes, sin recalcular capital ni simular decisiones alternativas. No es una regla implementable para retirar ganadores, no es una condición predeclarada de promoción y no constituye un full adicional.

MECH01 conserva105,62 con ambos castigos. MECH05 y06 quedan−136,13 y−42,40 pese a seguir positivas sin tres mejores antes de recargo. MECH01 mantiene sólo nueve operaciones en ese diagnóstico; la positividad no produce significancia ni robustez certificada. Dependencia de pocos runners sigue siendo un límite de todas las muestras.

Root lanzó por separado el mismo diagnóstico conjunto casi simultáneamente, job8a1b29dc984a4638a105e0d4d236b908; sería una reproducción computacional sobre los mismos datos, no evidencia de mercado independiente. No se hicieron más estudios adaptativos.

## Mezcla temporal: cohortes de cierre, no rentabilidad MTM

|Política|2020|2021|2022|2023|2024|2025|
|---|---:|---:|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|137.98|335.83|-215.41|395.76|-22.51|119.70|
|[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)|137.98|246.38|-110.70|-67.93|345.72|323.35|
|[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)|137.98|337.57|-99.22|115.80|355.41|332.44|
|[MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e)|0.00|232.68|-12.28|100.27|26.96|422.92|
|[MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea)|0.00|232.68|-12.28|100.27|-42.77|420.07|
|[MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05)|137.98|246.38|-110.70|-67.93|345.72|323.35|
|[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)|128.87|141.77|-68.33|499.46|308.07|265.33|
|[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)|0.00|189.58|-108.62|206.82|348.49|325.95|

MECH01/05/06 presentan cohortes positivas2021/2023/2024/2025 y negativas2022; son escasos cierres, no cuatro validaciones independientes. Cero indica ningún cierre en esa cohorte, no cero retorno de calendario. No elegir años retrospectivamente.

## Calendario MTM independiente de root

Root auditó seis objetivos con reconstrucción diariaUTC y conciliación terminal, job9cb3ee898ad840b9b1e435e94a9c6408 succeeded. Estas métricas proceden de su informe, distintas de las cohortes y de DDmotor.

|Política|DD diarioUTC %|Meses completos positivos/61|Trimestres completos positivos/19|
|---|---:|---:|---:|
|[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)|−2,53243|11|8|
|[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)|−3,57427|14|10|
|[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)|−2,93375|10|9|

MECH05 registra21meses activos. MTM anual MECH05:2021+1,39965%;2022−0,66531%;2023+4,89557%;2024+2,87864%;2025parcial+2,40991%. El último período termina2025-12-30 inclusive, no año calendario completo. Octubre2020/diciembre2025 se separan de61meses/19Q completos. No interpretar Portfolio00:01 como cierreUTC ni exigir que toda señal individual cumpla objetivos de una cartera.

## Capital-tiempo y ejecución

|Política|CAGR motor %|Neto bps/entry notional|Nocional entrada-tiempo|Duración media horas|
|---|---:|---:|---:|---:|
|[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)|1.40|23.64|0.14149|224.88|
|[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)|1.62|52.44|0.08121|250.84|
|[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)|2.16|94.36|0.07654|309.46|
|[MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e)|1.43|58.83|0.06191|234.44|
|[MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea)|1.30|59.43|0.05578|237.39|
|[MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05)|1.62|52.44|0.08121|250.84|
|[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)|2.33|64.13|0.11146|274.35|
|[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)|1.78|72.91|0.07316|252.64|

Nocional entrada-tiempo=sum(entrynotional*holdinghours)/(10000*45672hours), valorado al precio de entrada, no nocionalMTM. Menor exposición no es causalmente mayor selectividad.

Tipos de entrada reales: MECH01 9LIMIT/3MARKET;MECH02 9LIMIT/2MARKET;MECH03 8LIMIT/2MARKET;MECH04 11LIMIT/5MARKET;MECH05 19MARKET;MECH06 8LIMIT/4MARKET. Cq24LIMIT/7MARKET yBR0211LIMIT/5MARKET. Smart-order convierte cercanía en MARKET; política retest no garantiza LIMITpura. Se cobraron fees a todos.

MECH05 tiene un cierre MARKET terminal forzado con gross−57,09825, net−70,01020 y fee total12,91195. El contador de posición se capturó antes del cierre y coincide open_pl; wallet final incluye comisión de salida. Las otras cinco variantes nuevas no tienen cierre terminal forzado en los trades auditados.

## Auditoría y trazabilidad

Auditor original0ed613d8ea28425088dbe575ee0c5bc2 y followupdcbbcdb9950b4a69b9e516da8f4b0b70 succeeded. Ambos usan los mismos ocho snapshots íntegros:80trades nuevos+47referencias=127. Cantidades, entry/exitVWAP, fees por notional, PNL, wallet, ausencia de solapamientos, fechas, holding y terminal conciliados. JSON resumen20.819bytes<50KB y ocho detalles separados. Sin resultados truncados o pegados en código; sólo inputs.

Reportes en strategies/SpyLastMechanism01/reports/:
- SPY_LAST_MECHANISM_FROZEN_PROTOCOL_20261019.md
- SPY_LAST_MECHANISM_IMPLEMENTATION_REVIEW_20261019.md
- SPY_LAST_MECHANISM_SESSION_MANIFEST_20261019.md
- SPY_LAST_MECHANISM_ANALYSIS_SOURCE_20261019.md
- SPY_LAST_MECHANISM_EXACT_RESULTS_20261019.md
- Ocho SPY_LAST_MECHANISM_<MECH01..06/Cq/BR02>_AUDIT_20261019.md

Se conserva el interés de MECH01 como pista de eficiencia y menor concentración, MECH05 como variante de ejecución y MECH06 como control de rachas. No se declara sustitución, operativa validada ni avance automático a BTC. La decisión central integra estabilidad y contexto; ésta es la última ronda autorizada, sin más fulls ni acceso2026.

## Dashboards

Cq

Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

BR02

Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810

MECH01

Dashboard: http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592

MECH02

Dashboard: http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e

MECH03

Dashboard: http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea

MECH04

Dashboard: http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05

MECH05

Dashboard: http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862

MECH06

Dashboard: http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65

