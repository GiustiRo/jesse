# SPY — cierre de la última ronda exploratoria — 19/10/2026

Se completaron los doce backtests congelados: seis RESET y seis MECH, con dos especialistas y dos slots por agente. Todos terminaron sin errores. Las doce variantes fueron positivas tanto con las comisiones configuradas como con10bpsRT adicionales estáticos. Esto aporta evidencia de estabilidad descriptiva de la familia, pero varias variantes ejecutan exactamente el mismo camino y ninguna proporciona una muestra independiente ni fuera de desarrollo.

Resultado central: MECH01 (sólo segunda oportunidad del ciclo) es la candidata prioritaria para validación futura por eficiencia, menor drawdown observado y concentración. MECH05 (rupturas posteriores con entrada MARKET) es la alternativa de mayor neto histórico. Se cierra esta exploración, sin abrir otra ronda ni promover una estrategia a operación real.

## Condiciones y referencias

Capital inicial10.000USDT, riesgo presupuestado1%, fee0.00045 por lado en todos los tipos, isolated5x, cap4.4 y reserva0.001 sólo para sizing. Stop2ATR, BE2.25R, trail4.2 y tightening originales. SPY4h+M1, warmup240, fast/debugfalse; historia UTC Mon–Fri00–20 y entrada en barras abiertas00–16 exactamente como referencia. Quote M1 exacta T−60000 y precio conciliado. Órdenes pendientes una barra.

Ventana2020-10-15→2025-12-31 exclusiva: último día30/12. 2026 sigue reservado. Proxies aceptados; no se cambió la fuente ni se añadió funding. Sólo investigación mediante Jesse local MCP. Las referencias Cq/BR02 son sesiones anteriores reutilizadas, sin reruns.

## Matriz completa

| Sesión | Regla | N | Neto USDT | Fees | PF | Sharpe | DD motor% | +10bpsRT | Sin3mejores | Tiempo% |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | Referencia original | 31 | 751.35 | 286.48 | 1.49 | 0.46 | -5.21 | 433.04 | -298.22 | 15.26 |
| [BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810) | Posteriores a la primera | 16 | 874.80 | 150.59 | 2.32 | 0.72 | -3.80 | 707.47 | -86.36 | 8.79 |
| [RESET01](http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37) | Reset canal20 | 16 | 864.02 | 151.15 | 2.30 | 0.72 | -3.33 | 696.07 | -86.43 | 8.58 |
| [RESET02](http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e) | Reset canal32 | 17 | 781.90 | 163.50 | 2.04 | 0.64 | -4.16 | 600.23 | -175.69 | 8.84 |
| [RESET03](http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4) | Reset40% | 17 | 781.90 | 163.50 | 2.04 | 0.64 | -4.16 | 600.23 | -175.69 | 8.84 |
| [RESET04](http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62) | Reset60% | 16 | 864.02 | 151.15 | 2.30 | 0.72 | -3.33 | 696.07 | -86.43 | 8.58 |
| [RESET05](http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96) | Reset dos cierres | 16 | 874.80 | 150.59 | 2.32 | 0.72 | -3.80 | 707.47 | -86.36 | 8.79 |
| [RESET06](http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea) | Reset EMA20 | 15 | 657.85 | 138.97 | 2.00 | 0.58 | -4.98 | 503.44 | -254.63 | 8.01 |
| [MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592) | Sólo segunda oportunidad | 12 | 1179.98 | 113.12 | 4.04 | 1.01 | -2.49 | 1054.29 | 200.13 | 8.13 |
| [MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e) | Tercera y siguientes | 11 | 770.55 | 118.29 | 3.17 | 0.69 | -2.33 | 639.12 | -168.02 | 5.65 |
| [MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea) | Sólo tercera | 10 | 697.97 | 106.07 | 2.97 | 0.67 | -2.33 | 580.11 | -237.75 | 5.20 |
| [MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05) | Segunda o tercera | 16 | 874.80 | 150.59 | 2.32 | 0.72 | -3.80 | 707.47 | -86.36 | 8.79 |
| [MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862) | Posteriores, entrada MARKET | 19 | 1275.16 | 179.61 | 2.65 | 0.88 | -3.57 | 1075.60 | 31.51 | 11.41 |
| [MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65) | Posteriores, inicio de racha | 12 | 962.21 | 119.26 | 3.52 | 0.82 | -2.93 | 829.71 | 57.73 | 6.64 |

Los costes adicionales y quitar ganadores son sensibilidades estáticas sobre fills realizados. No reejecutan sizing, ocupación ni reinversiones. Las cifras de DD/PF/Sharpe/CAGR del motor se distinguen del auditor diario MTM. N indica trades cerrados, no unidades independientes para inferencia.

## Qué aprendimos

### La definición del reset no exige un punto exacto

Los cuatro vecinos locales (canal20/32 y umbral40/60%) conservaron entre781.90 y864.02USDT. La regla con dos cierres conservó el camino original BR02; el reset EMA20 produjo657.85USDT. Todas son positivas con10bpsRT y sin su mejor trade. Ninguna supera el neto central de BR02.

La estabilidad es limitada: todas las RESET pierden en cohortes por cierre2022 y2023, y todas quedan negativas sin sus tres mejores trades. Cinco de seis superan Cq, pero no son cinco confirmaciones independientes. Se observan cuatro caminos entre las seis RESET, uno idéntico a BR02.

### MECH01 mejora eficiencia y concentración observadas

La regla admite exactamente la segunda oportunidad Cq tras cada reset; cuenta señales antes de ocupación/sizing y no reaprovecha eventos perdidos. Conserva el retest y toda la gestión original.

N12, net1179.98USDT, PF4.04, Sharpe1.008, DDmotor−2.4867%, DD diarioUTC−2.5324%, tiempo abierto8.13%. CAGR del motor2.1624%: el beneficio11.80% es acumulado de toda la ventana, no anual. Frente a BR02 mejora305.19USDT; frente a Cq428.63USDT.

Su bruto de precio1293.10 supera1025.39 de BR02; fees113.12 son inferiores a150.59. El cambio neto frente a BR02 se descompone en bruto+267.72 y ahorro de fees37.47. Ya no es sólo ahorro de comisiones. Los doce timestamps de entrada y precios de MECH01 aparecen en BR02; cantidades/capital posteriores pueden cambiar, de modo que la descomposición no constituye un efecto causal sobre trades idénticos de tamaño fijo.

Con10bpsRT adicionales conserva1054.29USDT. Sin su mejor trade748.92; sin sus tres mejores200.13. Las cohortes por cierre son positivas en2020parcial/2021/2023/2024/2025parcial, con2022−99.22. En MTM anual también sólo2022 es negativo. Hay11/61meses completos positivos,14activos y8/19trimestres positivos: mayor porcentaje de meses activos positivos no equivale a regularidad mensual en toda la ventana.

### MECH05 aumenta el neto, con mayor concentración

Admite ordinal>=2 como BR02, pero repricia la entrada a MARKET actual antes de sizing. N19/net1275.16USDT/PF2.65/Sharpe.882/DDmotor−3.5693% y DD diario−3.5743%. CAGR2.3287%, tiempo abierto11.41%, mayor que BR02 pero menor que Cq.

Bruto1454.77 frente1025.39 de BR02; fees179.61 frente150.59. Incremento neto400.37: bruto+429.38 menos fees adicionales29.02. Sólo tres entradas coinciden exactamente con BR02: no atribuir esta diferencia únicamente al precio de ejecución, porque cambia qué órdenes se llenan y la disponibilidad posterior.

Con10bpsRT extra conserva1075.60. Sin mejor788.08; sin tres mejores31.51. Cohortes por cierre y MTM anual positivas salvo2022. MTM:14/61meses positivos,21activos y10/19Qpositivos, frente9/19 de BR02/Cq. Incluye una liquidación forzada terminal neta−70.01USDT reconciliada por fills/wallet; no se eliminó para mejorar la tabla y no acredita liquidez nativa.

### Las rachas no eliminan la pista, pero no prueban predicción causal

MECH06 sólo cuenta y opera el inicio de cada racha calificante, rompe racha ante barra retenida no calificante y conserva estado fuera de sesión. Ganó962.21 con12trades, DDmotor−2.93%; sin tres mejores57.73. Por tanto, el resultado positivo observado no requiere contar cada barra calificante contigua como otra oportunidad. Esto no demuestra que toda segunda ruptura tenga ventaja: seguimos comparando caminos con selección y ocupación endógenas.

MECH02 y03 también son positivas (770.55/697.97USDT, N11/10), pero quedan negativas sin sus tres mejores. MECH04 reproduce BR02 exactamente. No se suman sus operaciones o PNL para reconstruir BR02 ni se fabrican resultados de oportunidades omitidas. Los snapshots no permiten un estudio completo de outcomes virtuales para señales no ejecutadas.

## Diagnóstico conjunto post hoc

Tras ver los resultados separados se añadió un diagnóstico explícitamente POST HOC: excluir los tres mejores trades por neto original y después sumar10bpsRT extra sobre fills restantes. No es un nuevo full ni un criterio predeclarado.

| Sesión | Sin3mejores +10bpsRT |
|---|---:|
| Cq | −587.12 |
| BR02 | −223.08 |
| MECH01 | +105.62 |
| MECH05 | −136.13 |
| MECH06 | −42.40 |

MECH01 es la única MECH positiva bajo ese castigo conjunto. Quedan nueve trades en esa suma; no es certeza estadística ni elimina el sesgo de seleccionar entre muchas exploraciones. MECH05/06 pasan cada prueba separada, pero no la conjunta. Mantener clara esa diferencia. Fuente y resultados exactos en SPY_LAST_COMBINED_STRESS_20261019.md.

## Equivalencias y límites

Root calculó SHA256 de fills económicos y curva Portfolio excluyendo IDs. RESET01=RESET04; RESET02=RESET03; RESET05=MECH04=BR02. Hay nueve caminos exactos diferentes entre doce estrategias nuevas, ocho distintos adicionales frente a BR02. Compartir el mismo mercado e historia impide tratar incluso esos nueve como muestras independientes.

La sensibilidad del reset se ensayó sobre BR02, no se cruzó con MECH01 o MECH05. No afirmar que estas candidatas resistieron esa interacción no probada. No se combinaron variantes ganadoras después de ver resultados ni se abrió una nueva búsqueda adaptativa.

La historia2020–2025 fue reutilizada extensamente. No se llamó OOS, no se abrieron datos2026 ni se aumentó el riesgo para maquillar retorno. Mejorar métricas históricas no demuestra rentabilidad futura. Las nuevas candidatas N12/19 siguen siendo escasas y comparten muchos movimientos.

## Decisión de cierre

Objetivo de mejorar operativa histórica: sí, con más neto, menor drawdown observado y mejores diagnósticos de concentración que las referencias. Objetivo de demostrar robustez operativa suficiente para promoción: no, por tamaño de muestra, selección tras múltiples búsquedas y falta de validación limpia.

Congelar MECH01 como candidata prioritaria de selección/eficiencia y MECH05 como alternativa de entrada. Mantener Cq/BR02 como controles históricos y preservar sus fuentes. No mezclar candidatos ni sumar carteras sin comprobar solapamientos. Esta ronda cierra la exploración SPY; la siguiente fase útil es validar candidatos congelados con evidencia futura o una prueba limpia previamente definida, no continuar optimizando este historial. 2026 permanece reservado hasta decisión explícita sobre su uso.

## Auditoría y trazabilidad

12/12 finished, sin errores. Root comparó los doce snapshots strategy_codes con las fuentes revisadas, formularios/rutas/configuración y los ocho hiperparámetros registrados por sesión:12/12 iguales al contrato. Sólo before cambió, excepto el repricing de _plan MECH05. Gestión y constantes intactas.

QA lógica113assertions del AST real pasó; no es evidencia económica. Ambos especialistas conciliaron fills/cantidades/comisiones/PNL/balance y terminales en ocho inputs cada uno. Root completó MTM UTC de las doce con61meses/19Qcompletos y fronteras parciales aparte. Todos los jobs terminaron succeeded.

Jobs:
- RESET auditor c44367f60a1f4299ba8ad8af3987ce17.
- MECH auditor0ed613d8ea28425088dbe575ee0c5bc2.
- RESET MTM39c5fd2539894967886c6ac977cbfb00.
- MECH MTM9cb3ee898ad840b9b1e435e94a9c6408.
- Estado e97c0f4493b449abba005c64ac9f4d48.
- Conjunto root8a1b29dc984a4638a105e0d4d236b908; especialista dcbbcdb9950b4a69b9e516da8f4b0b70. Ambos hacen el mismo diagnóstico, no replicación de mercado.

Informes dentro del proyecto Jesse en la máquina que lo ejecuta:
- strategies/ResearchSpyReference4h/reports/SPY_LAST_FROZEN_PROTOCOL_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_STATE_QA_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_MTM_SOURCE_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_MTM_RESULTS_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_COMBINED_STRESS_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_RESET_EXACT_RESULTS_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_LAST_RESET_AUDIT_20261019.md
- strategies/SpyLastMechanism01/reports/SPY_LAST_MECHANISM_FINAL_REPORT_20261019.md
- strategies/SpyLastMechanism01/reports/SPY_LAST_MECHANISM_EXACT_RESULTS_20261019.md

## Enlaces

[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)

Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)

Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810

[RESET01](http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37)

Dashboard: http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37

[RESET02](http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e)

Dashboard: http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e

[RESET03](http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4)

Dashboard: http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4

[RESET04](http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62)

Dashboard: http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62

[RESET05](http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96)

Dashboard: http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96

[RESET06](http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea)

Dashboard: http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea

[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)

Dashboard: http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592

[MECH02](http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e)

Dashboard: http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e

[MECH03](http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea)

Dashboard: http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea

[MECH04](http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05)

Dashboard: http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05

[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)

Dashboard: http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862

[MECH06](http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65)

Dashboard: http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65


## Métricas exactas consolidadas

```json
[
  {
    "name": "Cq",
    "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
    "url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "n": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "gross_price": 1037.8232411744636,
    "pf": 1.4930482284215572,
    "sharpe": 0.4581998683996086,
    "cagr": 1.3992310944554776,
    "dd_motor": -5.2131810594609025,
    "time_pct": 15.264093244584572,
    "notional_time": 0.14148527769141334,
    "plus5": 592.1946448519213,
    "plus10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.8278032237806,
        "fee": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654456,
        "fee": 29.773738643213996
      },
      "2023": {
        "n": 9,
        "net": 395.7611513896043,
        "fee": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024080012,
        "fee": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.70108055231466,
        "fee": 44.85926795981045
      }
    },
    "entry_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "ex3_plus10": -587.123656556576,
    "mtm_dayclose_dd": -5.2179628778702085,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 33,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.45454545454545453,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.02910008869946501,
      "2022-12-31 00:00:00+00:00": -0.016735052301659392,
      "2023-12-31 00:00:00+00:00": 0.038579232068278735,
      "2024-12-31 00:00:00+00:00": -0.002113109427550386,
      "2025-12-31 00:00:00+00:00": 0.011258940845987109
    }
  },
  {
    "name": "BR02",
    "session_id": "f89d7afb-9876-4e7e-9ddf-78ff85137810",
    "url": "http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810",
    "n": 16,
    "net": 874.7958565504186,
    "fees": 150.5940012513908,
    "gross_price": 1025.3898578018095,
    "pf": 2.320269711623377,
    "sharpe": 0.7183938780138998,
    "cagr": 1.6215132040717561,
    "dd_motor": -3.8005064163188162,
    "time_pct": 8.78747737490512,
    "notional_time": 0.08121036182627324,
    "plus5": 791.1325225218683,
    "plus10": 707.4691884933177,
    "exbest": 455.51451397897824,
    "ex3": -86.35598247698874,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -67.92668184187508,
        "fee": 63.022585116543596
      },
      "2024": {
        "n": 3,
        "net": 345.7151991124811,
        "fee": 34.721055221010076
      },
      "2025": {
        "n": 2,
        "net": 323.3476595470383,
        "fee": 17.94832618586981
      }
    },
    "entry_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "ex3_plus10": -223.07893097807573,
    "mtm_dayclose_dd": -3.8052545389172465,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.006611731745005955,
      "2024-12-31 00:00:00+00:00": 0.03387460745680149,
      "2025-12-31 00:00:00+00:00": 0.03064486063997074
    }
  },
  {
    "name": "RESET01",
    "session_id": "046e8f71-8b39-40ed-843f-146e43a45a37",
    "url": "http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37",
    "n": 16,
    "net": 864.0185919364594,
    "fees": 151.15193357927205,
    "gross_price": 1015.1705255157315,
    "pf": 2.3047290194938683,
    "sharpe": 0.7169379162057065,
    "cagr": 1.6021890202592148,
    "dd_motor": -3.3324773341637193,
    "time_pct": 8.581661995679337,
    "notional_time": 0.07938756365448256,
    "plus5": 780.0452955035305,
    "plus10": 696.0719990706016,
    "exbest": 445.1392689899452,
    "ex3": -86.42566051548204,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -78.05288760523224,
        "fee": 63.63284623453318
      },
      "2024": {
        "n": 3,
        "net": 345.3692694103256,
        "fee": 34.686374777094336
      },
      "2025": {
        "n": 2,
        "net": 323.04253039859174,
        "fee": 17.93067783967722
      }
    },
    "entry_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -3.377824052233147,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.0075973791266624735,
      "2024-12-31 00:00:00+00:00": 0.03387432219110309,
      "2025-12-31 00:00:00+00:00": 0.030646358412416363
    }
  },
  {
    "name": "RESET02",
    "session_id": "12c939ee-a51b-4ae6-a323-dabd8fb7ab8e",
    "url": "http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e",
    "n": 17,
    "net": 781.8957005165089,
    "fees": 163.50290441384865,
    "gross_price": 945.3986049303578,
    "pf": 2.0439645082023326,
    "sharpe": 0.6422016638545679,
    "cagr": 1.4544274404440394,
    "dd_motor": -4.158429517385498,
    "time_pct": 8.83867577509196,
    "notional_time": 0.08164794878473322,
    "plus5": 691.0607536199263,
    "plus10": 600.2258067233438,
    "exbest": 366.1822821162883,
    "ex3": -175.68821433967867,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 7,
        "net": -155.12920566582142,
        "fee": 76.3814972916116
      },
      "2024": {
        "n": 3,
        "net": 342.7619220236606,
        "fee": 34.424424659287325
      },
      "2025": {
        "n": 2,
        "net": 320.60330442589543,
        "fee": 17.794947734982394
      }
    },
    "entry_types": {
      "LIMIT": 12,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -4.203389082350517,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.631578947368421,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.01509970258912241,
      "2024-12-31 00:00:00+00:00": 0.03387467408455569,
      "2025-12-31 00:00:00+00:00": 0.030646624937632483
    }
  },
  {
    "name": "RESET03",
    "session_id": "d66af143-2178-4453-ab95-e9f992d6a0c4",
    "url": "http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4",
    "n": 17,
    "net": 781.8957005165089,
    "fees": 163.50290441384865,
    "gross_price": 945.3986049303578,
    "pf": 2.0439645082023326,
    "sharpe": 0.6422016638545679,
    "cagr": 1.4544274404440394,
    "dd_motor": -4.158429517385498,
    "time_pct": 8.83867577509196,
    "notional_time": 0.08164794878473322,
    "plus5": 691.0607536199263,
    "plus10": 600.2258067233438,
    "exbest": 366.1822821162883,
    "ex3": -175.68821433967867,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 7,
        "net": -155.12920566582142,
        "fee": 76.3814972916116
      },
      "2024": {
        "n": 3,
        "net": 342.7619220236606,
        "fee": 34.424424659287325
      },
      "2025": {
        "n": 2,
        "net": 320.60330442589543,
        "fee": 17.794947734982394
      }
    },
    "entry_types": {
      "LIMIT": 12,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -4.203389082350517,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.631578947368421,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.01509970258912241,
      "2024-12-31 00:00:00+00:00": 0.03387467408455569,
      "2025-12-31 00:00:00+00:00": 0.030646624937632483
    }
  },
  {
    "name": "RESET04",
    "session_id": "98565a46-f7a1-45b1-9e92-54473b959d62",
    "url": "http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62",
    "n": 16,
    "net": 864.0185919364594,
    "fees": 151.15193357927205,
    "gross_price": 1015.1705255157315,
    "pf": 2.3047290194938683,
    "sharpe": 0.7169379162057065,
    "cagr": 1.6021890202592148,
    "dd_motor": -3.3324773341637193,
    "time_pct": 8.581661995679337,
    "notional_time": 0.07938756365448256,
    "plus5": 780.0452955035305,
    "plus10": 696.0719990706016,
    "exbest": 445.1392689899452,
    "ex3": -86.42566051548204,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -78.05288760523224,
        "fee": 63.63284623453318
      },
      "2024": {
        "n": 3,
        "net": 345.3692694103256,
        "fee": 34.686374777094336
      },
      "2025": {
        "n": 2,
        "net": 323.04253039859174,
        "fee": 17.93067783967722
      }
    },
    "entry_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -3.377824052233147,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.0075973791266624735,
      "2024-12-31 00:00:00+00:00": 0.03387432219110309,
      "2025-12-31 00:00:00+00:00": 0.030646358412416363
    }
  },
  {
    "name": "RESET05",
    "session_id": "492fb702-3333-4696-ae4b-9f36d52d5a96",
    "url": "http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96",
    "n": 16,
    "net": 874.7958565504186,
    "fees": 150.5940012513908,
    "gross_price": 1025.3898578018095,
    "pf": 2.320269711623377,
    "sharpe": 0.7183938780138998,
    "cagr": 1.6215132040717561,
    "dd_motor": -3.8005064163188162,
    "time_pct": 8.78747737490512,
    "notional_time": 0.08121036182627324,
    "plus5": 791.1325225218683,
    "plus10": 707.4691884933177,
    "exbest": 455.51451397897824,
    "ex3": -86.35598247698874,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -67.92668184187508,
        "fee": 63.022585116543596
      },
      "2024": {
        "n": 3,
        "net": 345.7151991124811,
        "fee": 34.721055221010076
      },
      "2025": {
        "n": 2,
        "net": 323.3476595470383,
        "fee": 17.94832618586981
      }
    },
    "entry_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -3.8052545389172465,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.006611731745005955,
      "2024-12-31 00:00:00+00:00": 0.03387460745680149,
      "2025-12-31 00:00:00+00:00": 0.03064486063997074
    }
  },
  {
    "name": "RESET06",
    "session_id": "3f71c37c-5dca-4047-8bee-8dda7478d9ea",
    "url": "http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea",
    "n": 15,
    "net": 657.849104464445,
    "fees": 138.96757730257514,
    "gross_price": 796.8166817670201,
    "pf": 2.004069673037444,
    "sharpe": 0.5845154848795305,
    "cagr": 1.2294995584035906,
    "dd_motor": -4.982064874838921,
    "time_pct": 8.005816838909324,
    "notional_time": 0.0718991966169944,
    "plus5": 580.6448948519032,
    "plus10": 503.4406852393616,
    "exbest": 246.9347953367806,
    "ex3": -254.62607856853697,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328204002,
        "fee": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516415,
        "fee": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442979,
        "fee": 11.312388365121311
      },
      "2023": {
        "n": 5,
        "net": -271.5194898927558,
        "fee": 52.44735902396904
      },
      "2024": {
        "n": 3,
        "net": 338.8147016106914,
        "fee": 34.02795347544877
      },
      "2025": {
        "n": 2,
        "net": 316.8942130137351,
        "fee": 17.590230075190014
      }
    },
    "entry_types": {
      "LIMIT": 10,
      "MARKET": 5
    },
    "mtm_dayclose_dd": -4.994774840076744,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 17,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.6470588235294118,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.026428701977387226,
      "2024-12-31 00:00:00+00:00": 0.033874220434827684,
      "2025-12-31 00:00:00+00:00": 0.03064457937784093
    }
  },
  {
    "name": "MECH01",
    "url": "http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592",
    "n": 12,
    "net": 1179.9815614338597,
    "fees": 113.1233320834728,
    "gross_price": 1293.1048935173326,
    "pf": 4.044531891325093,
    "sharpe": 1.0083101800688141,
    "cagr": 2.162407247921605,
    "dd_motor": -2.4866856144054705,
    "time_pct": 8.130765749985404,
    "notional_time": 0.07654082007699883,
    "plus5": 1117.1352658319304,
    "plus10": 1054.288970230001,
    "exbest": 748.9160186067709,
    "ex3": 200.13042443505128,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328203996,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 1,
        "net": 337.5690574955404,
        "fees": 8.552495880169069
      },
      "2022": {
        "n": 1,
        "net": -99.22117074919896,
        "fees": 4.935835497036526
      },
      "2023": {
        "n": 4,
        "net": 115.79681277005115,
        "fees": 42.159173777076205
      },
      "2024": {
        "n": 3,
        "net": 355.414199555051,
        "fees": 35.695101490220374
      },
      "2025": {
        "n": 2,
        "net": 332.44314908037614,
        "fees": 18.45209907709086
      }
    },
    "entry_types": {
      "LIMIT": 9,
      "MARKET": 3
    },
    "ex3_plus10": 105.62345322528955,
    "mtm_dayclose_dd": -2.5324294510837952,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.7857142857142857,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.033297468894396776,
      "2022-12-31 00:00:00+00:00": -0.009471692110328722,
      "2023-12-31 00:00:00+00:00": 0.011159710782616017,
      "2024-12-31 00:00:00+00:00": 0.033874379710593816,
      "2025-12-31 00:00:00+00:00": 0.030646874566655713
    }
  },
  {
    "name": "MECH02",
    "url": "http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e",
    "n": 11,
    "net": 770.5482833495945,
    "fees": 118.2861425608697,
    "gross_price": 888.8344259104642,
    "pf": 3.1711000022054057,
    "sharpe": 0.6891165837182842,
    "cagr": 1.4339388653358265,
    "dd_motor": -2.3324495156439085,
    "time_pct": 5.646457348046943,
    "notional_time": 0.061912452369650595,
    "plus5": 704.8337597046668,
    "plus10": 639.1192360597393,
    "exbest": 347.6284839194916,
    "ex3": -168.0216547320823,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 232.67786886883164,
        "fees": 20.011913226582937
      },
      "2022": {
        "n": 1,
        "net": -12.277523862229291,
        "fees": 6.33173302951528
      },
      "2023": {
        "n": 4,
        "net": 100.27157937702123,
        "fees": 43.956511108958686
      },
      "2024": {
        "n": 3,
        "net": 26.956559535868067,
        "fees": 38.40330478829588
      },
      "2025": {
        "n": 1,
        "net": 422.9197994301029,
        "fees": 9.582680407516929
      }
    },
    "entry_types": {
      "MARKET": 2,
      "LIMIT": 9
    },
    "ex3_plus10": -268.03770471781013,
    "mtm_dayclose_dd": -2.345984183826444,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 9,
      "win_months_all": 0.14754098360655737,
      "win_months_active": 0.6428571428571429,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.023267786886883135,
      "2022-12-31 00:00:00+00:00": -0.0011998348838461181,
      "2023-12-31 00:00:00+00:00": 0.009810924816268107,
      "2024-12-31 00:00:00+00:00": 0.002611899664418438,
      "2025-12-31 00:00:00+00:00": 0.04087118126509193
    }
  },
  {
    "name": "MECH03",
    "url": "http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea",
    "n": 10,
    "net": 697.9686460382638,
    "fees": 106.06832591568929,
    "gross_price": 804.0369719539531,
    "pf": 2.9665993185601143,
    "sharpe": 0.6732998917480437,
    "cagr": 1.3024768808721277,
    "dd_motor": -2.3324495156439085,
    "time_pct": 5.197750627663924,
    "notional_time": 0.05577949781836071,
    "plus5": 639.0417983073254,
    "plus10": 580.1149505763868,
    "exbest": 277.89820960156555,
    "ex3": -237.75192905000836,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 232.67786886883164,
        "fees": 20.011913226582937
      },
      "2022": {
        "n": 1,
        "net": -12.277523862229291,
        "fees": 6.33173302951528
      },
      "2023": {
        "n": 4,
        "net": 100.27157937702123,
        "fees": 43.956511108958686
      },
      "2024": {
        "n": 2,
        "net": -42.77371478205806,
        "fees": 26.250050111998476
      },
      "2025": {
        "n": 1,
        "net": 420.0704364366983,
        "fees": 9.518118438633898
      }
    },
    "entry_types": {
      "MARKET": 2,
      "LIMIT": 8
    },
    "ex3_plus10": -324.2643627287401,
    "mtm_dayclose_dd": -2.345984183826444,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 13,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.6153846153846154,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.023267786886883135,
      "2022-12-31 00:00:00+00:00": -0.0011998348838461181,
      "2023-12-31 00:00:00+00:00": 0.009810924816268107,
      "2024-12-31 00:00:00+00:00": -0.004144469962367503,
      "2025-12-31 00:00:00+00:00": 0.04087123922323621
    }
  },
  {
    "name": "MECH04",
    "url": "http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05",
    "n": 16,
    "net": 874.7958565504204,
    "fees": 150.5940012513908,
    "gross_price": 1025.389857801811,
    "pf": 2.320269711623384,
    "sharpe": 0.7183938780138998,
    "cagr": 1.6215132040717561,
    "dd_motor": -3.8005064163188162,
    "time_pct": 8.78747737490512,
    "notional_time": 0.08121036182627324,
    "plus5": 791.1325225218699,
    "plus10": 707.4691884933195,
    "exbest": 455.514513978981,
    "ex3": -86.35598247698488,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328203996,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516452,
        "fees": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442911,
        "fees": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -67.92668184187492,
        "fees": 63.022585116543596
      },
      "2024": {
        "n": 3,
        "net": 345.71519911248186,
        "fees": 34.721055221010076
      },
      "2025": {
        "n": 2,
        "net": 323.34765954703806,
        "fees": 17.94832618586981
      }
    },
    "entry_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "ex3_plus10": -223.07893097807573,
    "mtm_dayclose_dd": -3.8052545389172687,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.006611731745005955,
      "2024-12-31 00:00:00+00:00": 0.03387460745680149,
      "2025-12-31 00:00:00+00:00": 0.03064486063997074
    }
  },
  {
    "name": "MECH05",
    "url": "http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862",
    "n": 19,
    "net": 1275.16361422292,
    "fees": 179.6110200655598,
    "gross_price": 1454.7746342884798,
    "pf": 2.6547989447750973,
    "sharpe": 0.8824390732454782,
    "cagr": 2.3286604902763797,
    "dd_motor": -3.5693369150006315,
    "time_pct": 11.413265604017049,
    "notional_time": 0.11145537781293709,
    "plus5": 1175.3797141864977,
    "plus10": 1075.5958141500757,
    "exbest": 788.0828023924619,
    "ex3": 31.514430560207984,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 128.87328631389613,
        "fees": 3.3320653378432827
      },
      "2021": {
        "n": 3,
        "net": 141.76836222930348,
        "fees": 28.37809778742753
      },
      "2022": {
        "n": 2,
        "net": -68.33202768816221,
        "fees": 10.063353768336079
      },
      "2023": {
        "n": 6,
        "net": 499.46072488189895,
        "fees": 61.22685344828858
      },
      "2024": {
        "n": 4,
        "net": 308.0657071133023,
        "fees": 44.95854738784551
      },
      "2025": {
        "n": 3,
        "net": 265.32756137268126,
        "fees": 31.652102335818824
      }
    },
    "entry_types": {
      "MARKET": 19
    },
    "ex3_plus10": -136.13410899186948,
    "mtm_dayclose_dd": -3.5742676350636216,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 21,
      "positive_months": 14,
      "win_months_all": 0.22950819672131148,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0.012887328631389527,
      "2021-12-31 00:00:00+00:00": 0.013996459252863191,
      "2022-12-31 00:00:00+00:00": -0.006653141062306855,
      "2023-12-31 00:00:00+00:00": 0.048955652537825856,
      "2024-12-31 00:00:00+00:00": 0.028786424784009945,
      "2025-12-31 00:00:00+00:00": 0.024099138270455178
    }
  },
  {
    "name": "MECH06",
    "url": "http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65",
    "n": 12,
    "net": 962.2141582992981,
    "fees": 119.2576671126954,
    "gross_price": 1081.4718254119934,
    "pf": 3.5163421885325037,
    "sharpe": 0.8231146879007425,
    "cagr": 1.7776893671002103,
    "dd_motor": -2.9289574394842255,
    "time_pct": 6.638020377182227,
    "notional_time": 0.0731582633364019,
    "plus5": 895.9598987922451,
    "plus10": 829.7056392851921,
    "exbest": 539.5659013691004,
    "ex3": 57.72954538738702,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 189.58210941171166,
        "fees": 21.71813145086816
      },
      "2022": {
        "n": 2,
        "net": -108.62122192470657,
        "fees": 11.10046763786092
      },
      "2023": {
        "n": 3,
        "net": 206.81929028856132,
        "fees": 33.34712022067916
      },
      "2024": {
        "n": 3,
        "net": 348.48847477499396,
        "fees": 34.9996091098882
      },
      "2025": {
        "n": 2,
        "net": 325.9455057487378,
        "fees": 18.092338693398965
      }
    },
    "entry_types": {
      "MARKET": 4,
      "LIMIT": 8
    },
    "ex3_plus10": -42.40074231197333,
    "mtm_dayclose_dd": -2.933748671548664,
    "complete_calendar": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 10,
      "win_months_all": 0.16393442622950818,
      "win_months_active": 0.7142857142857143,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "mtm_year_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.018958210941171005,
      "2022-12-31 00:00:00+00:00": -0.010660027149138607,
      "2023-12-31 00:00:00+00:00": 0.020515831040002874,
      "2024-12-31 00:00:00+00:00": 0.03387402031857434,
      "2025-12-31 00:00:00+00:00": 0.030644722918932388
    }
  }
]
```

Confirmación de cierre: informe del especialista RESET guardado en strategies/ResearchSpyReference4h/reports/SPY_LAST_RESET_FINAL_REPORT_20261019.md (10221bytes). Ambos especialistas confirmaron cero backtests o análisis propios pendientes. La ronda termina aquí.
