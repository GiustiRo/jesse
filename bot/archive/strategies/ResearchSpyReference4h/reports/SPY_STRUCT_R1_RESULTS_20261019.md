# SPY Structural R1 — resultados consolidados — 2026-10-19

Se ejecutaron doce backtests nuevos, seis por cada uno de dos especialistas. La etapa anterior sólo preparó las hipótesis; estos resultados corresponden a su ejecución efectiva. Se mantuvo la matriz congelada, sin retocar reglas tras resultados. Dos slots por especialista/cuatro globales y análisis máximo dos globales.

Ventana 2020-10-15→2025-12-31 exclusiva (último día30/12). Capital10.000USDT, riesgo1%, fee0.00045/lado, 5xaislado, cap4.4. SPY4h+M1, warm240, fast/debugfalse, calendario original. Reserva0.001 sólo sizing; sin funding. 2026 continúa cerrado. Referencias Cq/M existentes sin rerun.

Resultados describen el mismo historial de desarrollo reutilizado, no evidencia fuera de muestra ni prueba de robustez. El máximo entre12 requiere validación posterior; no promoción automática. Costes5/10bpsRT y exclusiónmejores son sensibilidades estáticas de fills/PNL, no reruns con capital y ocupación recalculados.

Las nuevas selecciones alteran cantidad, sizing y ocupación: diferencias de neto no representan exclusivamente el efecto causal de un filtro sobre trades idénticos. DD motor y cierre diarioUTC no son métricas idénticas.


| Sesión | N | Neto USDT | Fees | PF | Sharpe | DD motor% | +10bpsRT | Sin mejor | Sin3mejores | Tiempo% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 31 | 751.35 | 286.48 | 1.49 | 0.46 | -5.21 | 433.04 | 349.58 | -298.22 | 15.26 |
| [M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | 38 | 151.60 | 336.73 | 1.07 | 0.11 | -7.72 | -222.54 | -224.73 | -864.91 | 16.00 |
| [BR01](http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b) | 24 | 71.82 | 209.42 | 1.06 | 0.07 | -6.70 | -160.87 | -304.57 | -836.48 | 10.04 |
| [BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810) | 16 | 874.80 | 150.59 | 2.32 | 0.72 | -3.80 | 707.47 | 455.51 | -86.36 | 8.79 |
| [BR03](http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41) | 10 | 223.87 | 89.19 | 1.59 | 0.26 | -4.39 | 124.77 | -61.24 | -309.79 | 6.05 |
| [BR04](http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f) | 7 | 628.91 | 63.13 | 5.85 | 0.66 | -2.17 | 558.77 | 221.00 | -54.56 | 4.47 |
| [BR05](http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1) | 4 | 430.81 | 36.96 | 5.78 | 0.68 | -1.83 | 389.75 | 153.90 | -90.08 | 3.45 |
| [BR06](http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da) | 4 | 179.59 | 38.81 | 2.04 | 0.31 | -2.62 | 136.46 | -93.46 | -87.89 | 1.99 |
| [PB01](http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6) | 44 | -575.41 | 401.75 | 0.78 | -0.29 | -13.10 | -1021.81 | -1048.02 | -1680.85 | 16.13 |
| [PB02](http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983) | 29 | -1007.01 | 261.33 | 0.44 | -0.74 | -14.00 | -1297.37 | -1347.23 | -1603.96 | 7.46 |
| [PB03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff) | 16 | 387.31 | 154.92 | 1.52 | 0.33 | -4.29 | 215.18 | -11.35 | -451.83 | 6.47 |
| [PB04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2) | 7 | 181.97 | 74.83 | 1.53 | 0.21 | -2.93 | 98.83 | -208.79 | -346.41 | 3.17 |
| [PB05](http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0) | 48 | -43.46 | 435.79 | 0.98 | 0.00 | -7.77 | -527.66 | -395.45 | -996.61 | 19.72 |
| [PB06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646) | 19 | 571.75 | 190.93 | 1.51 | 0.42 | -6.28 | 359.61 | -38.52 | -610.57 | 7.13 |

## Hallazgo y decisión

BR02 es la única variante que supera el neto de Cq; también reduce drawdown, rotación y exposición. Excluye la primera oportunidad Cq de cada ciclo observado, definido por cierre en mitad inferior del canal26 previo, y admite las posteriores. Censura inicial hasta reset. Mantiene retest original. Primera vs posteriores cuenta oportunidades independientemente de ocupación; no son sólo fills.

Incremento neto123.4481USDT: bruto por precio1025.3899 frente1037.8232 (−12.4334), fees150.5940 frente286.4755 (ahorro135.8815). Descomposición contable, no causal sobre operaciones idénticas. Sólo7entradas comunes frente31/16totales, y9entradas BR02 nuevas por cambios de selección/ocupación. No afirmar que se eliminaron15trades de referencia.

PF2.32vs1.49, Sharpe.718vs.458, tiempo8.7875%vs15.2641%. Coste estático10bpsRT707.47vs433.04. Sin mejor455.51vs349.58; sin3mejores−86.36vs−298.22. N16 sigue siendo escaso. BR02 no mejora en todos los años: cohortes por cierre2022−110.70,2023−67.93;2024+345.72,2025+323.35. MTM anual también negativo2022/23. El beneficio relativo cambia de signo entre periodos, no es estabilidad demostrada.

Calendario MTM completo: BR02 tiene12/61meses positivos frente15/61Cq;18meses activos frente33;9/19trimestres positivos en ambos.66.7%de meses activos positivos no debe confundirse con66.7%de todos los meses. DD diarioUTC−3.8053vs−5.2180.

BR04 tiene buena eficiencia aparente, pero sólo7operaciones; BR05/06 sólo4cadauna. No trasladar sus PF altos a una afirmación de edge. Ningún PB supera Cq. PB03/04/06 son rentables, pero los tres quedan negativos sin su mejortrade; PB06 también pierde en cohortes2024/25.

Decisión: registrar BR02 como candidata prioritaria de selección/eficiencia y mantener Cq como referencia. No promover, no abrir2026, no cambiar gestión ni mezclar variantes. Esta ronda termina con12fulls; no activar por obligación rondas2/3.

La investigación siguiente más discriminante sería analizar primeras y posteriores oportunidades dentro de los mismos episodios, incluidas las omitidas por ocupación, para separar señal de cambios de capacidad. Después, vecinos de reset predeclarados e interpretados en conjunto, sin seleccionar el máximo. Sigue siendo desarrollo reutilizado; aún requiere validación posterior limpia.

## Verificación y trazabilidad

12/12 finished, snapshots strategy_codes idénticos a fuentes revisadas. Formularios/rutas/configuración y8hiperparámetros registrados por sesión comprobados. Gestión heredada sin cambios. AST real de estado BR pasó37invariantes sintéticas, sólo QA lógico. Auditorías de fills/cantidad/fees/PNL/wallet/terminales por especialistas y MTM root conciliadas. Forced closes no acreditan ejecución nativa. Cq realmente ejecuta24LIMIT+7MARKET por política automática; BR02 11LIMIT+5MARKET. No31LIMIT puros.

Jobs análisis: PB028bb8cbb6a5484ba89cca3b7abeb27f; BR43639f36bc2c4a60911d6558528dff69. MTM PBb7ed075be282430e8ce8fd78bde752f6; BR4161d43204da46aeb06a959be1836d61. Todos succeeded. Dos fallos técnicos de salidaPB previos quedaron documentados, corregidos sin retocar estrategia ni repetir backtests.

Informes dentro del proyecto Jesse en la máquina que lo ejecuta:
- strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_FROZEN_PROTOCOL_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_STATE_QA_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_MTM_SOURCE_20261019.md
- strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_MTM_RESULTS_20261019.md
- strategies/SpyStructR1PB01/reports/SPY_STRUCT_R1_PB_FINAL_REPORT_20261019.md


## Enlaces de dashboard

[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)

Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

[M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07)

Dashboard: http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07

[BR01](http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b)

Dashboard: http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b

[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)

Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810

[BR03](http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41)

Dashboard: http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41

[BR04](http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f)

Dashboard: http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f

[BR05](http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1)

Dashboard: http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1

[BR06](http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da)

Dashboard: http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da

[PB01](http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6)

Dashboard: http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6

[PB02](http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983)

Dashboard: http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983

[PB03](http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff)

Dashboard: http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff

[PB04](http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2)

Dashboard: http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2

[PB05](http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0)

Dashboard: http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0

[PB06](http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646)

Dashboard: http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646

## Métricas exactas consolidadas

```json
[
  {
    "name": "Cq",
    "url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "n": 31,
    "net": 751.3477149671152,
    "fee": 286.47552620734854,
    "pf": 1.4930482284215572,
    "sharpe": 0.4581998683996086,
    "dd_motor": -5.2131810594609025,
    "plus10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "time_pct": 15.264093244584572,
    "notional_time": 0.14148527769141334,
    "cohorts": {
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
    }
  },
  {
    "name": "M",
    "url": "http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "n": 38,
    "net": 151.6012639172099,
    "fee": 336.73029237147995,
    "pf": 1.074122772361648,
    "sharpe": 0.10588870453443279,
    "dd_motor": -7.718707541843617,
    "plus10": -222.54350538443452,
    "exbest": -224.7296691424284,
    "ex3": -864.90548009341,
    "time_pct": 15.996051556022653,
    "notional_time": 0.1446681109984161,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": 144.46030476585108,
        "fee": 3.2856353550544073
      },
      "2021": {
        "n": 5,
        "net": 234.68215351049457,
        "fee": 52.67854808982013
      },
      "2022": {
        "n": 6,
        "net": -412.947657460623,
        "fee": 33.94331524034087
      },
      "2023": {
        "n": 10,
        "net": 325.2519289120968,
        "fee": 90.9032396483522
      },
      "2024": {
        "n": 10,
        "net": -145.8798868876506,
        "fee": 103.61885607926621
      },
      "2025": {
        "n": 6,
        "net": 6.034421077041072,
        "fee": 52.30069795864606
      }
    }
  },
  {
    "name": "BR01",
    "url": "http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b",
    "n": 24,
    "net": 71.82254556636093,
    "fee": 209.42311948805448,
    "pf": 1.056700075118146,
    "sharpe": 0.06587705134787052,
    "dd_motor": -6.697704900221568,
    "plus10": -160.8698094203663,
    "exbest": -304.56704758893335,
    "ex3": -836.4792929987366,
    "time_pct": 10.037769311613243,
    "notional_time": 0.09325670050269083,
    "cohorts": {
      "2021": {
        "n": 2,
        "net": -1.669740719287958,
        "fee": 22.82665381564336
      },
      "2022": {
        "n": 5,
        "net": -205.62835179669645,
        "fee": 28.422052764555534
      },
      "2023": {
        "n": 5,
        "net": 267.07480844473315,
        "fee": 43.26826827596431
      },
      "2024": {
        "n": 7,
        "net": -100.10449957972207,
        "fee": 72.88209316484331
      },
      "2025": {
        "n": 5,
        "net": 112.15032921733436,
        "fee": 42.02405146704797
      }
    }
  },
  {
    "name": "BR02",
    "url": "http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810",
    "n": 16,
    "net": 874.7958565504186,
    "fee": 150.5940012513908,
    "pf": 2.320269711623377,
    "sharpe": 0.7183938780138998,
    "dd_motor": -3.8005064163188162,
    "plus10": 707.4691884933177,
    "exbest": 455.51451397897824,
    "ex3": -86.35598247698874,
    "time_pct": 8.78747737490512,
    "notional_time": 0.08121036182627324,
    "cohorts": {
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
    }
  },
  {
    "name": "BR03",
    "url": "http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41",
    "n": 10,
    "net": 223.87119915761406,
    "fee": 89.19180028306832,
    "pf": 1.5903257638471178,
    "sharpe": 0.2630170740044828,
    "dd_motor": -4.392481438329177,
    "plus10": 124.76919884309369,
    "exbest": -61.23865740684636,
    "ex3": -309.78683385175583,
    "time_pct": 6.053928008407778,
    "notional_time": 0.04762433559715391,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": 168.79131639148233,
        "fee": 3.5746040598531006
      },
      "2021": {
        "n": 2,
        "net": 268.6161524958744,
        "fee": 19.27791202001215
      },
      "2022": {
        "n": 2,
        "net": -100.72028437883203,
        "fee": 12.935218434415013
      },
      "2023": {
        "n": 3,
        "net": -262.01933130244146,
        "fee": 31.481508511173928
      },
      "2024": {
        "n": 2,
        "net": 149.20334595153088,
        "fee": 21.922557257614116
      }
    }
  },
  {
    "name": "BR04",
    "url": "http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f",
    "n": 7,
    "net": 628.9148646426152,
    "fee": 63.12680740865307,
    "pf": 5.848766864542775,
    "sharpe": 0.6611886061903214,
    "dd_motor": -2.1673204184637918,
    "plus10": 558.7739675218895,
    "exbest": 221.0011224060616,
    "ex3": -54.55566604832984,
    "time_pct": 4.470134874759153,
    "notional_time": 0.04394532849820264,
    "cohorts": {
      "2022": {
        "n": 1,
        "net": 70.07919006361743,
        "fee": 5.1693320781638015
      },
      "2023": {
        "n": 1,
        "net": -90.1917512977791,
        "fee": 9.420528322361061
      },
      "2024": {
        "n": 3,
        "net": 236.04239338294934,
        "fee": 31.766761970799188
      },
      "2025": {
        "n": 2,
        "net": 412.9850324938274,
        "fee": 16.77018503732902
      }
    }
  },
  {
    "name": "BR05",
    "url": "http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1",
    "n": 4,
    "net": 430.81350793008016,
    "fee": 36.95623692905661,
    "pf": 5.782747241747338,
    "sharpe": 0.6842669387065272,
    "dd_motor": -1.8290474850964356,
    "plus10": 389.7510224533506,
    "exbest": 153.90279356307514,
    "ex3": -90.07657861774987,
    "time_pct": 3.4537572254335256,
    "notional_time": 0.026053608983243024,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": 164.5483325029549,
        "fee": 3.57618405228986
      },
      "2021": {
        "n": 1,
        "net": 276.910714367005,
        "fee": 10.713420991961534
      },
      "2023": {
        "n": 1,
        "net": -90.07657861774982,
        "fee": 12.86937260999651
      },
      "2024": {
        "n": 1,
        "net": 79.43103967787007,
        "fee": 9.797259274808704
      }
    }
  },
  {
    "name": "BR06",
    "url": "http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da",
    "n": 4,
    "net": 179.58819064449804,
    "fee": 38.814248200700334,
    "pf": 2.03562089214586,
    "sharpe": 0.3133417131115916,
    "dd_motor": -2.622662998859071,
    "plus10": 136.46124819927547,
    "exbest": -93.45644719997168,
    "ex3": -87.88560287973482,
    "time_pct": 1.9883079348397268,
    "notional_time": 0.02099137606857476,
    "cohorts": {
      "2021": {
        "n": 1,
        "net": 273.0446378444697,
        "fee": 10.539941477364826
      },
      "2023": {
        "n": 2,
        "net": -173.41113143476855,
        "fee": 18.715986848075985
      },
      "2024": {
        "n": 1,
        "net": 79.95468423479687,
        "fee": 9.558319875259524
      }
    }
  },
  {
    "name": "PB01",
    "url": "http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6",
    "n": 44,
    "net": -575.413938725543,
    "fee": 401.7542123368851,
    "pf": 0.776654430749012,
    "sharpe": -0.2901654726068019,
    "dd_motor": -13.096411840410394,
    "plus10": -1021.8075079887486,
    "exbest": -1048.0193736097106,
    "ex3": -1680.8466648408644,
    "time_pct": 16.125853914871254,
    "notional_time": 0.1518861112020365,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": 97.02437104957555,
        "fees": 3.081955249484577
      },
      "2021": {
        "n": 3,
        "net": 424.2642021595499,
        "fees": 30.48456395318073
      },
      "2022": {
        "n": 7,
        "net": -211.89999498867604,
        "fees": 43.08887623970296
      },
      "2023": {
        "n": 12,
        "net": 20.984385952450452,
        "fees": 107.57051368390636
      },
      "2024": {
        "n": 12,
        "net": -281.7089237362266,
        "fees": 137.16896633667017
      },
      "2025": {
        "n": 9,
        "net": -624.0779791622161,
        "fees": 80.35933687394028
      }
    }
  },
  {
    "name": "PB02",
    "url": "http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983",
    "n": 29,
    "net": -1007.009155528648,
    "fee": 261.32795700069244,
    "pf": 0.4384261688221961,
    "sharpe": -0.7444427328881174,
    "dd_motor": -13.995269724132719,
    "plus10": -1297.373552196084,
    "exbest": -1347.2255609083106,
    "ex3": -1603.964316465479,
    "time_pct": 7.460150639341391,
    "notional_time": 0.06950447682629166,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": -93.67371989239523,
        "fees": 5.653982464637509
      },
      "2021": {
        "n": 3,
        "net": 167.67070385884574,
        "fees": 29.787538197625416
      },
      "2022": {
        "n": 4,
        "net": 40.77492660789163,
        "fees": 21.168514330802413
      },
      "2023": {
        "n": 9,
        "net": -561.2690220169267,
        "fees": 85.29454901591954
      },
      "2024": {
        "n": 8,
        "net": -312.151868965998,
        "fees": 85.82394671385654
      },
      "2025": {
        "n": 4,
        "net": -248.36017512006552,
        "fees": 33.599426277851
      }
    }
  },
  {
    "name": "PB03",
    "url": "http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff",
    "n": 16,
    "net": 387.3134183431286,
    "fee": 154.92150247626873,
    "pf": 1.5173449872924347,
    "sharpe": 0.32576392507850943,
    "dd_motor": -4.291427890215626,
    "plus10": 215.1784155917189,
    "exbest": -11.347743913807733,
    "ex3": -451.82570987703315,
    "time_pct": 6.4683321655865,
    "notional_time": 0.06429559330050777,
    "cohorts": {
      "2021": {
        "n": 2,
        "net": 199.5409502229887,
        "fees": 21.584396264979585
      },
      "2022": {
        "n": 5,
        "net": -99.97668994738513,
        "fees": 32.26039682709587
      },
      "2023": {
        "n": 2,
        "net": 126.78314326936925,
        "fees": 22.531275297975302
      },
      "2024": {
        "n": 5,
        "net": -242.6509514591279,
        "fees": 62.15632621431984
      },
      "2025": {
        "n": 2,
        "net": 403.61696625728365,
        "fees": 16.389107871898133
      }
    }
  },
  {
    "name": "PB04",
    "url": "http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2",
    "n": 7,
    "net": 181.972022393028,
    "fee": 74.82562801146202,
    "pf": 1.5253042509470454,
    "sharpe": 0.21378551719950004,
    "dd_motor": -2.9310748574774337,
    "plus10": 98.83243571362576,
    "exbest": -208.7869364218563,
    "ex3": -346.4126210000384,
    "time_pct": 3.1664550125532784,
    "notional_time": 0.031081923279426108,
    "cohorts": {
      "2021": {
        "n": 2,
        "net": -173.81215876241498,
        "fees": 22.715166569763305
      },
      "2022": {
        "n": 1,
        "net": 100.54589871833987,
        "fees": 6.662313681660001
      },
      "2023": {
        "n": 1,
        "net": -85.49945610597477,
        "fees": 12.357440782144277
      },
      "2024": {
        "n": 2,
        "net": -50.02122027180642,
        "fees": 24.319754812413272
      },
      "2025": {
        "n": 1,
        "net": 390.7589588148843,
        "fees": 8.770952165481162
      }
    }
  },
  {
    "name": "PB05",
    "url": "http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0",
    "n": 48,
    "net": -43.45555526713462,
    "fee": 435.7850726058024,
    "pf": 0.983435366771851,
    "sharpe": 0.001525022300664274,
    "dd_motor": -7.769281482707779,
    "plus10": -527.661191495804,
    "exbest": -395.4541880852332,
    "ex3": -996.6054024530423,
    "time_pct": 19.716784901033453,
    "notional_time": 0.1835958960270239,
    "cohorts": {
      "2020": {
        "n": 1,
        "net": 168.791316391482,
        "fees": 3.5746040598531006
      },
      "2021": {
        "n": 6,
        "net": 253.87204811156442,
        "fees": 65.80509293423061
      },
      "2022": {
        "n": 8,
        "net": -224.3251944170916,
        "fees": 46.978012917765305
      },
      "2023": {
        "n": 12,
        "net": 64.57115792783776,
        "fees": 113.14012160399932
      },
      "2024": {
        "n": 12,
        "net": -78.84876907354207,
        "fees": 131.06237621937564
      },
      "2025": {
        "n": 9,
        "net": -227.5161142073851,
        "fees": 75.22486487057843
      }
    }
  },
  {
    "name": "PB06",
    "url": "http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646",
    "n": 19,
    "net": 571.7530451590001,
    "fee": 190.93038785604676,
    "pf": 1.5099082131681496,
    "sharpe": 0.4183644741082198,
    "dd_motor": -6.275390218471532,
    "plus10": 359.60816976339254,
    "exbest": -38.52495342401221,
    "ex3": -610.5712665711965,
    "time_pct": 7.127415776259706,
    "notional_time": 0.07979347810998393,
    "cohorts": {
      "2021": {
        "n": 2,
        "net": 499.259792893952,
        "fees": 18.497734784945507
      },
      "2022": {
        "n": 3,
        "net": -40.098638195967,
        "fees": 16.67368640214278
      },
      "2023": {
        "n": 5,
        "net": 718.4229378075476,
        "fees": 54.72438606813406
      },
      "2024": {
        "n": 6,
        "net": -358.1442335712496,
        "fees": 75.1566280034845
      },
      "2025": {
        "n": 3,
        "net": -247.68681377528299,
        "fees": 25.877952597339924
      }
    }
  }
]
```

Informe BR final confirmado guardado: strategies/ResearchSpyReference4h/reports/SPY_STRUCT_R1_BR_FINAL_REPORT_20261019.md. Auditoría exacta: SPY_STRUCT_R1_BR_AUDIT_20261019.md; tabla exacta: SPY_STRUCT_R1_BR_EXACT_RESULTS_20261019.md, misma carpeta.
