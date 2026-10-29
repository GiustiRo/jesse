# R60 SPY/PAXG: veinte contrastes de estabilidad y selección de entrada

Fecha local: 19 de octubre de 2026. **Completados los 20 backtests solicitados, diez por activo, con análisis y conciliación MTM de todos.**

PAXG MARKET mantiene una ventaja de neto frente al retest en los cinco contextos fijados antes de resultados. Esa ventaja convive con mayor exposición y drawdown, y por cohortes de operaciones cerradas empeora en 2021–2023 y mejora en 2024–2025 en todos los pares. Es evidencia de estabilidad local de la comparación; todavía no demuestra ausencia de sobreajuste o superioridad general entre regímenes.

SPY no obtiene una mejora material. Cuatro variantes reproducen exactamente la trayectoria de la referencia y la mayor diferencia positiva es 0,364237 USDT en toda la ventana. Se conserva la referencia, sin combinar parámetros ni escoger ese máximo.

## Contrato y revisión antes de ejecutar

Ventana 2020-10-15 a 2025-12-31 exclusiva; 2026 cerrado. Capital inicial aislado de 10.000 USDT por full, riesgo planificado 1%, fee 0,00045 por lado para todos los tipos, isolated 5x, cap de nocional 4,4, sin piramidado. Reserva 0,001 para sizing, no slippage ya simulado. Una ruta 4h y data route M1 del mismo activo; warmup 240; fast/debug false.

SPY conserva exactamente el calendario de su referencia: UTC Mon–Fri 00–20 para historia y barras abiertas 00–16 para entradas. PAXG sin ventana. Proxies existentes aceptados: SPX CFD BID/10 y spot PAXG. No se modificó histórico, funding, riesgo, gestión, framework o configuración global.

Diez fuentes SPY y diez PAXG autocontenidas se revisaron antes de liberar cada cola. La comparación de métodos y fuentes normalizadas fue exacta: sólo predicado de g o un default declarado, según el protocolo. Las tres bases actuales coinciden con sus fuentes de atribución previa. Se ejecutaron dos backtests por especialista y hasta cuatro globales; un análisis por especialista y hasta dos globales. No hubo optimización adaptativa ni cambios después de resultados.

Protocolo congelado: R60_SPY_PAXG_FROZEN_PROTOCOL_20261019.md. La ronda contiene veinte configuraciones controladas, no veinte ideas independientes de alpha. Las referencias existentes no se cuentan como nuevos fulls.

## PAXG: cinco pares completos

Cq intenta retest a frontera; M conserva evento y filtros, valida distancia contra la frontera original, sustituye entrada por cierre y recalcula tamaño. Las salidas originales permanecen iguales. Cada contexto altera una sola pieza; P5 amplía de ocho a diez configuraciones con EMA rápida +20%, fijada antes de resultados.

Neto en USDT. La fila central son referencias previas, no ejecuciones nuevas.

| Contexto | Retest neto | MARKET neto | Δ M−retest | Δ con +10 bps RT | DD retest / M, motor % |
|---|---:|---:|---:|---:|---|
| Centro: canal26,ADX26,EMA20 | [546.11](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | [962.13](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 416.02 | 392.56 | -6.92 / -7.65 |
| P1: canal24 | [960.04](http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26) | [1385.70](http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb) | 425.66 | 401.22 | -6.92 / -7.65 |
| P2: canal28 | [262.21](http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936) | [671.53](http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a) | 409.32 | 385.63 | -9.11 / -10.07 |
| P3: ADX24 | [324.50](http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248) | [467.98](http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c) | 143.48 | 108.62 | -8.30 / -10.38 |
| P4: ADX28 | [127.95](http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd) | [469.42](http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504) | 341.47 | 319.46 | -9.16 / -10.02 |
| P5: EMA24 | [532.93](http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e) | [948.34](http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14) | 415.41 | 391.99 | -7.05 / -7.76 |

Las cinco diferencias nuevas son positivas, entre 143,48 y 425,66 USDT. Las cinco MARKET conservan neto positivo con otros 10 bps por vuelta. Frente a su retest, aumentan tiempo abierto entre 1,35 y 1,85 puntos porcentuales y empeoran el DD del motor entre 0,71 y 2,08 puntos. No se igualó exposición retrospectivamente.

La comparación central y las diez nuevas filas presentan doce fingerprints de fills y doce curvas distintos. No son réplicas idénticas, pero tampoco doce historias de mercado independientes: reutilizan las mismas fechas y muchos episodios.

### Dependencia temporal que sigue abierta

Estas son diferencias M−retest por AÑO DE CIERRE DE OPERACIONES, no rentabilidades MTM anuales:

| Contexto | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| P1 | -18.46 | -4.21 | -93.74 | 205.33 | 336.74 |
| P2 | -18.46 | -4.21 | -85.93 | 200.21 | 317.72 |
| P3 | -1.73 | -4.25 | -301.01 | 188.90 | 261.58 |
| P4 | -7.31 | -4.27 | -86.44 | 225.21 | 214.28 |
| P5 | -18.46 | -4.25 | -93.62 | 205.09 | 326.65 |

El signo es negativo en los tres primeros años y positivo en los dos últimos en TODOS los pares. Agregar 2023–2025 como un bloque escondería que 2023 también empeora. Esto es compatible con dependencia de los movimientos de 2024–2025 y debilita una explicación de ventaja universal de ejecución.

En las intersecciones seleccionadas por created_at exacto, MARKET paga más caro y su PnL por nocional común es peor. La ventaja global mezcla oportunidades que llenan, gestión anclada al precio de entrada, tamaño y ocupación posterior. No demuestra mejor precio de fill ni un efecto causal aislado de la orden.

Las diez variantes quedan negativas al retirar las tres operaciones de mayor PnL. MARKET con ADX24/ADX28 también queda negativa sin su mejor operación; N24/N28/EMA24 siguen positivas con esa exclusión. Es concentración descriptiva, no una regla universal para descartar estrategias que capturan tendencias. Ninguna variante tuvo cierre sintético terminal o posición residual.

La política retest no garantiza orden LIMIT pura: ADX24 Cq registra 40 entradas LIMIT y una MARKET por clasificación automática cercana del motor. El resto de Cq nuevo registra sólo LIMIT; M registra MARKET. Se cobraron fees en todos los tipos.

## SPY: qué cambió y qué no aportó mejora

Referencia [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639): 31 operaciones, neto 751,3477149671152 USDT, Sharpe 0,4581998683996086 y DD del motor −5,2131810594609025%; 15/61 meses y 9/19 trimestres completos positivos.

g=(close−máxima Donchian previa)/ATR. No se combinan cambios: los primeros cuatro alteran sólo el intervalo, y los siguientes seis un único default de canal/ADX/EMA.

| Control y cambio | N | Neto | Sharpe motor | DD motor % | Neto +10 bps RT | Meses + /61 |
|---|---:|---:|---:|---:|---:|---:|
| [S01: 0.10 < g <= 1.0](http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21) | 23 | 82.95 | 0.076 | -6.65 | -152.62 | 10 |
| [S02: 0.25 < g <= 1.0](http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae) | 14 | 245.87 | 0.232 | -4.10 | 106.58 | 6 |
| [S03: 0.0 < g <= 0.50](http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e) | 30 | 743.97 | 0.460 | -6.13 | 436.60 | 15 |
| [S04: 0.0 < g <= 0.75](http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35) | 31 | 751.35 | 0.458 | -5.21 | 433.04 | 15 |
| [S05: donchian_len26→24](http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134) | 31 | 751.35 | 0.458 | -5.21 | 433.04 | 15 |
| [S06: donchian_len26→28](http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2) | 31 | 751.35 | 0.458 | -5.21 | 433.04 | 15 |
| [S07: adx_min26→24](http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60) | 39 | 597.94 | 0.338 | -8.10 | 208.53 | 17 |
| [S08: adx_min26→28](http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb) | 24 | 686.03 | 0.473 | -5.89 | 442.72 | 13 |
| [S09: ema_fast20→16](http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f) | 31 | 751.35 | 0.458 | -5.21 | 433.04 | 15 |
| [S10: ema_fast20→24](http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a) | 31 | 751.71 | 0.458 | -5.21 | 433.08 | 15 |

S04 (g<=0,75), S05 (canal24), S06 (canal28), S09 (EMA16) y Cq comparten exactamente trades, campos económicos y curva numérica. Constituyen una trayectoria observada ante perturbaciones distintas; no cinco confirmaciones independientes ni prueba de que nunca cambió un arming sin fill. Root verificó además los hiperparámetros realmente registrados, descartando que el default modificado no se hubiese aplicado.

S10 (EMA24) cambia una de las 31 entradas respecto al pareado exacto, añade sólo 0,364237 USDT y conserva 15/61 meses, 9/19 trimestres y el mismo DD diario UTC. Esa diferencia no justifica sustituir la referencia. Todas las diez variantes SPY quedan negativas al retirar sus tres mejores operaciones.

Exigir más desplazamiento mínimo de ruptura perjudica el neto: S01 gana 82,95 y ya pierde 34,83 con otros 5 bps RT; S02 gana 245,87 con sólo 14 trades y queda negativa sin su mejor trade. Limitar a 0,50 ATR queda cerca en neto pero empeora DD. ADX24 añade actividad y meses positivos, con menor neto y DD−8,10%; ADX28 reduce neto y tampoco mejora DD. Los cambios no producen una mejora conjunta convincente de retorno y riesgo.

Esta tanda aporta estabilidad local en varios parámetros, sin resolver la escasa cantidad de episodios y concentración de la referencia. Encontrar vecinos equivalentes no crea una nueva fuente de beneficio.

## Veinte filas completas y métricas comparables

CAGR/DD/Sharpe son los del motor. Tiempo abierto es porcentaje de toda la ventana. Neto y fees en USDT. Los retornos MTM por calendario se conservan en informe separado y JSON; no se interpretan cohortes de cierre como MTM.

| Activo / control | N | Neto | Fees | PF | Sharpe | CAGR % | DD motor % | Tiempo abierto % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [SPY S01](http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21) | 23 | 82.95 | 212.02 | 1.07 | 0.076 | 0.16 | -6.65 | 11.08 |
| [SPY S02](http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae) | 14 | 245.87 | 125.36 | 1.34 | 0.232 | 0.47 | -4.10 | 6.82 |
| [SPY S03](http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e) | 30 | 743.97 | 276.63 | 1.49 | 0.460 | 1.39 | -6.13 | 14.44 |
| [SPY S04](http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35) | 31 | 751.35 | 286.48 | 1.49 | 0.458 | 1.40 | -5.21 | 15.26 |
| [SPY S05](http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134) | 31 | 751.35 | 286.48 | 1.49 | 0.458 | 1.40 | -5.21 | 15.26 |
| [SPY S06](http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2) | 31 | 751.35 | 286.48 | 1.49 | 0.458 | 1.40 | -5.21 | 15.26 |
| [SPY S07](http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60) | 39 | 597.94 | 350.47 | 1.30 | 0.338 | 1.12 | -8.10 | 18.11 |
| [SPY S08](http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb) | 24 | 686.03 | 218.98 | 1.56 | 0.473 | 1.28 | -5.89 | 12.02 |
| [SPY S09](http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f) | 31 | 751.35 | 286.48 | 1.49 | 0.458 | 1.40 | -5.21 | 15.26 |
| [SPY S10](http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a) | 31 | 751.71 | 286.77 | 1.49 | 0.458 | 1.40 | -5.21 | 15.25 |
| [PAXG P1_Cq](http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26) | 36 | 960.04 | 260.41 | 1.54 | 0.366 | 1.77 | -6.92 | 13.79 |
| [PAXG P1_M](http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb) | 39 | 1385.70 | 282.41 | 1.82 | 0.503 | 2.52 | -7.65 | 15.64 |
| [PAXG P2_Cq](http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936) | 35 | 262.21 | 241.35 | 1.14 | 0.128 | 0.50 | -9.11 | 12.24 |
| [PAXG P2_M](http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a) | 38 | 671.53 | 262.68 | 1.39 | 0.281 | 1.25 | -10.07 | 14.07 |
| [PAXG P3_Cq](http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248) | 41 | 324.50 | 286.29 | 1.16 | 0.145 | 0.61 | -8.30 | 15.44 |
| [PAXG P3_M](http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c) | 46 | 467.98 | 317.66 | 1.21 | 0.194 | 0.88 | -10.38 | 17.15 |
| [PAXG P4_Cq](http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd) | 32 | 127.95 | 216.16 | 1.07 | 0.076 | 0.24 | -9.16 | 10.78 |
| [PAXG P4_M](http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504) | 35 | 469.42 | 235.97 | 1.27 | 0.211 | 0.88 | -10.02 | 12.13 |
| [PAXG P5_Cq](http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e) | 35 | 532.93 | 246.48 | 1.30 | 0.226 | 1.00 | -7.05 | 13.35 |
| [PAXG P5_M](http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14) | 38 | 948.34 | 267.56 | 1.57 | 0.372 | 1.75 | -7.76 | 15.20 |

## Calendario UTC y validación de ejecución

Root reconstruyó las veinte cuentas con el auditor MTM validado, cuatro snapshots históricos de anclaje y hasta seis objetivos por job. Son cuatro jobs completados. Todos concilian fills, fees y wallet; la curva Portfolio00:01 no se toma como cierre UTC. Los 61 meses y 19 trimestres completos se distinguen de las fronteras parciales.

PAXG MARKET tiene meses completos positivos P1..P5:17/16/17/15/17, frente16/14/16/12/15 de sus retests. Trimestres positivos:10/10/7/9/10 frente9/7/7/6/8. Mejorar el recuento no borra el DD mayor. En SPY, ADX24 aumenta meses positivos a17 pero reduce trimestres a8 y empeora retorno/DD; no se selecciona una métrica favorable aislada.

Root también cotejó las veinte fuentes ejecutadas con las revisadas y los veinte formularios: igualdad e invariantes correctos. Recuperó los hiperparámetros registrados (ocho filas incluido DNA vacío) y verificó todos contra matriz. No hubo otro backtest de referencia ni pruebas ocultas adicionales.

Los recargos de 5/10 bps RT son estáticos: mitad por lado sobre fills y cantidades congelados. No simulan nuevos rechazos, colas, impacto o decisiones de sizing bajo otra fricción. Nocional-tiempo usa precio de entrada, no marca MTM ni beta constante. Comparaciones entre políticas mantienen endógenos capital y ocupación.

## Decisión de investigación

PAXG: conservar MARKET del centro previamente identificado como candidata fija de investigación, ahora con más respaldo local frente al retest. No desplazar automáticamente a canal24 por ser el mayor neto de esta tanda. El estudio confirma el signo relativo en estos vecinos y expone dependencia temporal y concentración; no confirma ausencia de sobreajuste.

SPY: conservar referencia. No escoger EMA24 por 0,36USDT ni combinar el mejor intervalo/ADX/canal. La siguiente hipótesis para SPY debería cambiar una pieza estructural explicable del evento o su horizonte y contrastarla aisladamente, en vez de seguir buscando un número cercano que supere por poco la tabla. Esa siguiente investigación no se ejecutó en esta ronda.

Todo el período 2020–2025 sigue siendo desarrollo reutilizado y ninguna seed, vecino o máximo histórico equivale a OOS. 2026 permanece reservado. No se integra cartera, se cambia riesgo o se vuelve a BTC como si ambos activos hubieran demostrado mejoras robustas.

## Fuentes preservadas

- R60_SPY_PAXG_FROZEN_PROTOCOL_20261019.md: matriz antes de resultados.
- R60_ROOT_IMPLEMENTATION_REVIEW_20261019.md: fuentes, snapshots, formularios e hiperparámetros registrados.
- R60_MTM_SOURCE_20261019.md / R60_MTM_RESULTS_20261019.md: reconstrucción reproducible y todos los resultados exactos de calendario.
- strategies/ResearchSpyReference4h/reports/R60_SPY_FINAL_REPORT_20261019.md y R60_SPY_EXACT_RESULTS_20261019.md.
- strategies/R60PaxgN24Retest4h/reports/R60_PAXG_FINAL_REPORT_20261019.md y R60_PAXG_EXACT_TABLE_20261019.md.
- PHASE2_RESEARCH_HANDOFF_R60_20261019.md: estado de continuidad.

Sin errores económicos ni corridas pendientes. Los resúmenes de análisis se recuperaron íntegros en bloques acotados; no se usaron resultados parciales. Toda operación del proyecto se realizó mediante MCP.

## Registro de dashboards


SPY S01 — R60SpyGapMin10; sesión d404c47e-025a-4789-b1a8-b054402f6c21.

Dashboard: http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21

SPY S02 — R60SpyGapMin25; sesión cd61d362-4b1c-4793-80b7-e85a9494edae.

Dashboard: http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae

SPY S03 — R60SpyGapMax50; sesión 9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e.

Dashboard: http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e

SPY S04 — R60SpyGapMax75; sesión 89d81c40-6ccc-43c8-b3c4-3326a94a3b35.

Dashboard: http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35

SPY S05 — R60SpyN24; sesión 8bae70a3-ab31-4fc5-9905-c65023b03134.

Dashboard: http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134

SPY S06 — R60SpyN28; sesión 2327e98c-4c6d-4a70-b54d-75646cdd82c2.

Dashboard: http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2

SPY S07 — R60SpyAdx24; sesión 60d1237b-6b7a-435b-ae6d-fa1103205b60.

Dashboard: http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60

SPY S08 — R60SpyAdx28; sesión 19be9941-b9e5-4709-8ff4-29f0c5bbdefb.

Dashboard: http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb

SPY S09 — R60SpyFast16; sesión 84eb15ef-1a1d-4621-b21f-fcd09bb4989f.

Dashboard: http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f

SPY S10 — R60SpyFast24; sesión 333221fd-d6ed-462d-87eb-2eb255bbc50a.

Dashboard: http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a

PAXG P1_Cq — R60PaxgN24Retest4h; sesión 39964cd7-d0e4-4684-9261-01ccad239e26.

Dashboard: http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26

PAXG P1_M — R60PaxgN24Market4h; sesión d2fcc787-b228-49d3-be41-0c3f657fd2bb.

Dashboard: http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb

PAXG P2_Cq — R60PaxgN28Retest4h; sesión 62b6dc3e-2dc7-4612-90ca-935242ed8936.

Dashboard: http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936

PAXG P2_M — R60PaxgN28Market4h; sesión 98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a.

Dashboard: http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a

PAXG P3_Cq — R60PaxgAdx24Retest4h; sesión b51a2052-0e26-47d4-bbe3-45013f196248.

Dashboard: http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248

PAXG P3_M — R60PaxgAdx24Market4h; sesión 92ac3dc0-e141-4977-b31f-185499127c3c.

Dashboard: http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c

PAXG P4_Cq — R60PaxgAdx28Retest4h; sesión 2c562667-f6cc-498b-932b-2983bc41b7dd.

Dashboard: http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd

PAXG P4_M — R60PaxgAdx28Market4h; sesión ac0ed1df-254d-4d7d-9fc1-ce5656107504.

Dashboard: http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504

PAXG P5_Cq — R60PaxgFast24Retest4h; sesión 9a272836-5fd1-471f-b6d1-17a7d0d0b55e.

Dashboard: http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e

PAXG P5_M — R60PaxgFast24Market4h; sesión 09fa1c9a-d363-47ee-bfb9-522a9e13ba14.

Dashboard: http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14

## Datos normalizados exactos de los veinte fulls

time_open_pct está en porcentaje en ambos activos; entry_notional_time es el proxy a precio de entrada. DDmotor y DD_UTC_dayclose se mantienen separados. ex3 retira tres operaciones por mayor PnL, incluso si alguna es pérdida.

```json
[
  {
    "asset": "SPY",
    "control": "S01",
    "name": "R60SpyGapMin10",
    "session_id": "d404c47e-025a-4789-b1a8-b054402f6c21",
    "dashboard_url": "http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21",
    "change": "0.10 < g <= 1.0",
    "N": 23,
    "net": 82.9535236572004,
    "fees": 212.01672727526963,
    "PF": 1.06596462316971,
    "DDmotor": -6.654984999592428,
    "CAGR": 0.15857616602510394,
    "Sharpe": 0.07648903056030368,
    "time_open_pct": 11.080640217200912,
    "entry_notional_time": 0.09984102700401203,
    "stress5": -34.83354705128272,
    "stress10": -152.62061775976576,
    "exbest": -251.68933926337243,
    "ex3": -690.9944515622414,
    "positive_complete_months": 10,
    "active_complete_months": 27,
    "positive_complete_quarters": 6,
    "DD_UTC_dayclose": -6.700888536837479
  },
  {
    "asset": "SPY",
    "control": "S02",
    "name": "R60SpyGapMin25",
    "session_id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
    "dashboard_url": "http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae",
    "change": "0.25 < g <= 1.0",
    "N": 14,
    "net": 245.8742418595162,
    "fees": 125.36052140162752,
    "PF": 1.3446510233072277,
    "DDmotor": -4.099687568281962,
    "CAGR": 0.46697537512865317,
    "Sharpe": 0.23228570468090567,
    "time_open_pct": 6.816430197933087,
    "entry_notional_time": 0.06647236035378323,
    "stress5": 176.22950774750092,
    "stress10": 106.58477363548562,
    "exbest": -73.85444125549776,
    "ex3": -512.8090386653323,
    "positive_complete_months": 6,
    "active_complete_months": 17,
    "positive_complete_quarters": 5,
    "DD_UTC_dayclose": -4.114090027250095
  },
  {
    "asset": "SPY",
    "control": "S03",
    "name": "R60SpyGapMax50",
    "session_id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
    "dashboard_url": "http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
    "change": "0.0 < g <= 0.50",
    "N": 30,
    "net": 743.9711828862412,
    "fees": 276.63145167598293,
    "PF": 1.4896904685510277,
    "DDmotor": -6.132698354864685,
    "CAGR": 1.3858836381329676,
    "Sharpe": 0.4596199367125393,
    "time_open_pct": 14.441999474513926,
    "entry_notional_time": 0.13718877951137115,
    "stress5": 590.2870430662508,
    "stress10": 436.6029032462603,
    "exbest": 342.4612407364584,
    "ex3": -302.32269970477955,
    "positive_complete_months": 15,
    "active_complete_months": 32,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -6.137433901514077
  },
  {
    "asset": "SPY",
    "control": "S04",
    "name": "R60SpyGapMax75",
    "session_id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
    "dashboard_url": "http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
    "change": "0.0 < g <= 0.75",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "positive_complete_months": 15,
    "active_complete_months": 33,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085
  },
  {
    "asset": "SPY",
    "control": "S05",
    "name": "R60SpyN24",
    "session_id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
    "dashboard_url": "http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134",
    "change": "donchian_len26→24",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "positive_complete_months": 15,
    "active_complete_months": 33,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085
  },
  {
    "asset": "SPY",
    "control": "S06",
    "name": "R60SpyN28",
    "session_id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
    "dashboard_url": "http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2",
    "change": "donchian_len26→28",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "positive_complete_months": 15,
    "active_complete_months": 33,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085
  },
  {
    "asset": "SPY",
    "control": "S07",
    "name": "R60SpyAdx24",
    "session_id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
    "dashboard_url": "http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60",
    "change": "adx_min26→24",
    "N": 39,
    "net": 597.9379578325991,
    "fees": 350.46780701762265,
    "PF": 1.3048982927072252,
    "DDmotor": -8.096205641424326,
    "CAGR": 1.1201069472235758,
    "Sharpe": 0.3377375270170746,
    "time_open_pct": 18.105038827582177,
    "entry_notional_time": 0.1655766793706388,
    "stress5": 403.2336206005866,
    "stress10": 208.529283368574,
    "exbest": 198.3763364424717,
    "ex3": -451.92482537426145,
    "positive_complete_months": 17,
    "active_complete_months": 37,
    "positive_complete_quarters": 8,
    "DD_UTC_dayclose": -8.10084341613928
  },
  {
    "asset": "SPY",
    "control": "S08",
    "name": "R60SpyAdx28",
    "session_id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
    "dashboard_url": "http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
    "change": "adx_min26→28",
    "N": 24,
    "net": 686.0308434052209,
    "fees": 218.9783135961006,
    "PF": 1.555117092021026,
    "DDmotor": -5.892075684490239,
    "CAGR": 1.2807852033825728,
    "Sharpe": 0.47295715146124506,
    "time_open_pct": 12.023413323991358,
    "entry_notional_time": 0.113510417707401,
    "stress5": 564.3762247407205,
    "stress10": 442.7216060762202,
    "exbest": 290.36587299061233,
    "ex3": -360.3540051435342,
    "positive_complete_months": 13,
    "active_complete_months": 27,
    "positive_complete_quarters": 7,
    "DD_UTC_dayclose": -5.904842466070659
  },
  {
    "asset": "SPY",
    "control": "S09",
    "name": "R60SpyFast16",
    "session_id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
    "dashboard_url": "http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
    "change": "ema_fast20→16",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "Sharpe": 0.4581998683996086,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "positive_complete_months": 15,
    "active_complete_months": 33,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085
  },
  {
    "asset": "SPY",
    "control": "S10",
    "name": "R60SpyFast24",
    "session_id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
    "dashboard_url": "http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a",
    "change": "ema_fast20→24",
    "N": 31,
    "net": 751.7119522395761,
    "fees": 286.7708466456683,
    "PF": 1.4933836938880178,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.399889971337509,
    "Sharpe": 0.4584228742218906,
    "time_open_pct": 15.253364570561104,
    "entry_notional_time": 0.14140980381744386,
    "stress5": 592.394815214205,
    "stress10": 433.0776781888338,
    "exbest": 349.91625637837717,
    "ex3": -297.899045359473,
    "positive_complete_months": 15,
    "active_complete_months": 33,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085
  },
  {
    "asset": "PAXG",
    "control": "P1_Cq",
    "name": "R60PaxgN24Retest4h",
    "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
    "dashboard_url": "http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26",
    "N": 36,
    "net": 960.0415136226013,
    "fees": 260.41477650305654,
    "PF": 1.5382710146147627,
    "DDmotor": -6.919378335744097,
    "CAGR": 1.773820071833243,
    "Sharpe": 0.3655840693972553,
    "time_open_pct": 13.788134232498397,
    "entry_notional_time": 0.10979084109488528,
    "stress5": 815.3666377875699,
    "stress10": 670.6917619525384,
    "exbest": 322.5429607998194,
    "ex3": -717.8704338634134,
    "positive_complete_months": 16,
    "active_complete_months": 31,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -6.921781413307038
  },
  {
    "asset": "PAXG",
    "control": "P1_M",
    "name": "R60PaxgN24Market4h",
    "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
    "dashboard_url": "http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb",
    "N": 39,
    "net": 1385.701717983873,
    "fees": 282.4113203992724,
    "PF": 1.8194081220776872,
    "DDmotor": -7.64796155547669,
    "CAGR": 2.520318386957743,
    "Sharpe": 0.5028090084653423,
    "time_open_pct": 15.637626262626265,
    "entry_notional_time": 0.12339548495087554,
    "stress5": 1228.8065399842774,
    "stress10": 1071.9113619846814,
    "exbest": 761.0302938812432,
    "ex3": -266.73933747127967,
    "positive_complete_months": 17,
    "active_complete_months": 31,
    "positive_complete_quarters": 10,
    "DD_UTC_dayclose": -7.65034683398127
  },
  {
    "asset": "PAXG",
    "control": "P2_Cq",
    "name": "R60PaxgN28Retest4h",
    "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
    "dashboard_url": "http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936",
    "N": 35,
    "net": 262.207451889136,
    "fees": 241.35025060012018,
    "PF": 1.1437380198190137,
    "DDmotor": -9.106780300664042,
    "CAGR": 0.4976741004134366,
    "Sharpe": 0.12787878979034237,
    "time_open_pct": 12.241526537046772,
    "entry_notional_time": 0.08873390864561433,
    "stress5": 128.1239793335137,
    "stress10": -5.95949322210862,
    "exbest": -358.25538890520136,
    "ex3": -1165.2296933807784,
    "positive_complete_months": 14,
    "active_complete_months": 31,
    "positive_complete_quarters": 7,
    "DD_UTC_dayclose": -9.109126905714259
  },
  {
    "asset": "PAXG",
    "control": "P2_M",
    "name": "R60PaxgN28Market4h",
    "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
    "dashboard_url": "http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
    "N": 38,
    "net": 671.5315157024731,
    "fees": 262.67704587791116,
    "PF": 1.3880104453725206,
    "DDmotor": -10.069493774953775,
    "CAGR": 1.2544127318831366,
    "Sharpe": 0.28133814630238096,
    "time_open_pct": 14.070437029252062,
    "entry_notional_time": 0.10211824076675384,
    "stress5": 525.599823548078,
    "stress10": 379.6681313936829,
    "exbest": 63.24231060321131,
    "ex3": -883.844839662783,
    "positive_complete_months": 16,
    "active_complete_months": 31,
    "positive_complete_quarters": 10,
    "DD_UTC_dayclose": -10.071816509860465
  },
  {
    "asset": "PAXG",
    "control": "P3_Cq",
    "name": "R60PaxgAdx24Retest4h",
    "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
    "dashboard_url": "http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248",
    "N": 41,
    "net": 324.50220242582566,
    "fees": 286.2911119024477,
    "PF": 1.1589347242023043,
    "DDmotor": -8.302396935878553,
    "CAGR": 0.6143975204656593,
    "Sharpe": 0.14487194173342102,
    "time_open_pct": 15.444765574823382,
    "entry_notional_time": 0.1198653440549888,
    "stress5": 165.45158470224357,
    "stress10": 6.400966978661472,
    "exbest": -305.71080741499827,
    "ex3": -1125.39603669719,
    "positive_complete_months": 16,
    "active_complete_months": 38,
    "positive_complete_quarters": 7,
    "DD_UTC_dayclose": -8.304764307824941
  },
  {
    "asset": "PAXG",
    "control": "P3_M",
    "name": "R60PaxgAdx24Market4h",
    "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
    "dashboard_url": "http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c",
    "N": 46,
    "net": 467.9807271498951,
    "fees": 317.65969595929914,
    "PF": 1.213754179173589,
    "DDmotor": -10.379926008484453,
    "CAGR": 0.8810874299219007,
    "Sharpe": 0.19368089130092866,
    "time_open_pct": 17.154055000875815,
    "entry_notional_time": 0.1300939430837091,
    "stress5": 291.50311828361777,
    "stress10": 115.02550941734046,
    "exbest": -136.977933941458,
    "ex3": -1078.8795398290906,
    "positive_complete_months": 17,
    "active_complete_months": 39,
    "positive_complete_quarters": 7,
    "DD_UTC_dayclose": -10.382240725513636
  },
  {
    "asset": "PAXG",
    "control": "P4_Cq",
    "name": "R60PaxgAdx28Retest4h",
    "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
    "dashboard_url": "http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd",
    "N": 32,
    "net": 127.95384526532453,
    "fees": 216.15780743761633,
    "PF": 1.0742084531174207,
    "DDmotor": -9.15661198500345,
    "CAGR": 0.24415930646946027,
    "Sharpe": 0.07571707467587487,
    "time_open_pct": 10.781842996438378,
    "entry_notional_time": 0.07775149397424388,
    "stress5": 7.866174466648786,
    "stress10": -112.22149633202696,
    "exbest": -471.8434571438979,
    "ex3": -1188.4518360315699,
    "positive_complete_months": 12,
    "active_complete_months": 29,
    "positive_complete_quarters": 6,
    "DD_UTC_dayclose": -9.158957303540971
  },
  {
    "asset": "PAXG",
    "control": "P4_M",
    "name": "R60PaxgAdx28Market4h",
    "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
    "dashboard_url": "http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504",
    "N": 35,
    "net": 469.4248632579352,
    "fees": 235.9707304507689,
    "PF": 1.2736454475843284,
    "DDmotor": -10.016952972445935,
    "CAGR": 0.883756652770451,
    "Sharpe": 0.21055217953357508,
    "time_open_pct": 12.12770771296783,
    "entry_notional_time": 0.0869766777006371,
    "stress5": 338.330013007508,
    "stress10": 207.23516275708084,
    "exbest": -134.5701378920432,
    "ex3": -999.5568610914547,
    "positive_complete_months": 15,
    "active_complete_months": 30,
    "positive_complete_quarters": 9,
    "DD_UTC_dayclose": -10.019277064382148
  },
  {
    "asset": "PAXG",
    "control": "P5_Cq",
    "name": "R60PaxgFast24Retest4h",
    "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
    "dashboard_url": "http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
    "N": 35,
    "net": 532.9256826889153,
    "fees": 246.47614166265822,
    "PF": 1.3011636743164046,
    "DDmotor": -7.052402092339594,
    "CAGR": 1.0008332111861806,
    "Sharpe": 0.225863618840498,
    "time_open_pct": 13.348258597536056,
    "entry_notional_time": 0.10368878080407197,
    "stress5": 395.99449287632746,
    "stress10": 259.06330306373957,
    "exbest": -103.76035604665935,
    "ex3": -931.8938201030231,
    "positive_complete_months": 15,
    "active_complete_months": 31,
    "positive_complete_quarters": 8,
    "DD_UTC_dayclose": -7.054801735606542
  },
  {
    "asset": "PAXG",
    "control": "P5_M",
    "name": "R60PaxgFast24Market4h",
    "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
    "dashboard_url": "http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
    "N": 38,
    "net": 948.339108895103,
    "fees": 267.557886631587,
    "PF": 1.5666292344865935,
    "DDmotor": -7.7639248506052745,
    "CAGR": 1.7529684167542303,
    "Sharpe": 0.3723356919327944,
    "time_open_pct": 15.19610848368074,
    "entry_notional_time": 0.11694084284763914,
    "stress5": 799.6958385442213,
    "stress10": 651.0525681933395,
    "exbest": 324.4622815862381,
    "ex3": -646.900003987193,
    "positive_complete_months": 17,
    "active_complete_months": 31,
    "positive_complete_quarters": 10,
    "DD_UTC_dayclose": -7.766307133997263
  }
]
```

## Deltas PAXG exactos, centro y cinco contextos

```json
[
  {
    "context": "Center",
    "delta_net": 416.0156415820886,
    "delta_stress5": 404.28825147214366,
    "delta_stress10": 392.56086136219864,
    "delta_time_pct": 1.8477404098791368,
    "delta_notional_time": 0.013268415659594704,
    "delta_net_bps_entry_notional": 12.452024920699444,
    "delta_DD_engine": -0.7285832197325925,
    "delta_recent2023_25": 438.6872107757832,
    "cohort_deltas": {
      "2021": -18.463077777168394,
      "2022": -4.208491416526243,
      "2023": -93.74490746810318,
      "2024": 205.33480083227124,
      "2025": 327.0973174116154
    }
  },
  {
    "context": "P1",
    "delta_net": 425.6602043612718,
    "delta_stress5": 413.4399021967075,
    "delta_stress10": 401.21960003214303,
    "delta_time_pct": 1.849492030127868,
    "delta_notional_time": 0.013604643855990264,
    "delta_net_bps_entry_notional": 11.028405065177282,
    "delta_DD_engine": -0.7285832197325925,
    "delta_recent2023_25": 448.33177355496696,
    "cohort_deltas": {
      "2021": -18.463077777168394,
      "2022": -4.208491416526243,
      "2023": -93.74490746810318,
      "2024": 205.33480083227124,
      "2025": 336.74188019079884
    }
  },
  {
    "context": "P2",
    "delta_net": 409.32406381333715,
    "delta_stress5": 397.4758442145643,
    "delta_stress10": 385.62762461579155,
    "delta_time_pct": 1.8289104922052903,
    "delta_notional_time": 0.013384332121139514,
    "delta_net_bps_entry_notional": 13.258343449308857,
    "delta_DD_engine": -0.9627134742897336,
    "delta_recent2023_25": 431.99563300703164,
    "cohort_deltas": {
      "2021": -18.463077777168394,
      "2022": -4.208491416526243,
      "2023": -85.92654261147226,
      "2024": 200.2063492163959,
      "2025": 317.71582640210795
    }
  },
  {
    "context": "P3",
    "delta_net": 143.47852472406942,
    "delta_stress5": 126.0515335813742,
    "delta_stress10": 108.62454243867899,
    "delta_time_pct": 1.7092894260524325,
    "delta_notional_time": 0.010228599028720309,
    "delta_net_bps_entry_notional": 3.062671942007258,
    "delta_DD_engine": -2.0775290726059,
    "delta_recent2023_25": 149.46161044556789,
    "cohort_deltas": {
      "2021": -1.728872496658937,
      "2022": -4.2542132248398445,
      "2023": -301.013524383085,
      "2024": 188.8956274167432,
      "2025": 261.57950741191
    }
  },
  {
    "context": "P4",
    "delta_net": 341.47101799261065,
    "delta_stress5": 330.46383854085923,
    "delta_stress10": 319.4566590891078,
    "delta_time_pct": 1.3458647165294515,
    "delta_notional_time": 0.009225183726393221,
    "delta_net_bps_entry_notional": 12.596795861239185,
    "delta_DD_engine": -0.8603409874424859,
    "delta_recent2023_25": 353.0498689920664,
    "cohort_deltas": {
      "2021": -7.307235564222765,
      "2022": -4.271615435232945,
      "2023": -86.44239771131893,
      "2024": 225.21356451969723,
      "2025": 214.27870218368815
    }
  },
  {
    "context": "P5",
    "delta_net": 415.41342620618764,
    "delta_stress5": 403.7013456678938,
    "delta_stress10": 391.98926512959997,
    "delta_time_pct": 1.8478498861446848,
    "delta_notional_time": 0.013252062043567173,
    "delta_net_bps_entry_notional": 12.477855443949522,
    "delta_DD_engine": -0.7115227582656809,
    "delta_recent2023_25": 438.12169720667976,
    "cohort_deltas": {
      "2021": -18.463077777168394,
      "2022": -4.245193223323341,
      "2023": -93.62420876725817,
      "2024": 205.0945484614707,
      "2025": 326.65135751246703
    }
  }
]
```
