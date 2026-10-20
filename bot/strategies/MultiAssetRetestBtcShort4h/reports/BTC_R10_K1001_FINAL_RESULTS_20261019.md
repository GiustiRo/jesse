# K1001 — validación R10 completada
Fecha local: 19 de octubre de 2026, America/Montevideo.

## Resultado
K1001 pasa el diagnóstico operativo prefijado de comisiones y vecinos. Se conserva como candidata de investigación congelada. La mejora frente a Y902 sobrevive a las comisiones reales del motor y a ambos objetivos vecinos; no se eligió el mejor parámetro. El beneficio incremental depende de cinco entradas modificadas y se concentra casi íntegramente en julio de 2024. Todos los intervalos primarios de incertidumbre incluyen cero. No se afirma ausencia de sobreajuste ni se reemplaza automáticamente N204 como referencia operativa.

Se completaron ocho nuevos backtests, cuatro auditorías financieras y tres análisis descriptivos de incertidumbre. Todos los targets reconciliaron cantidades, fills, fees, PNL, wallet, cierre terminal y MTM. Veinticuatro snapshots y 46 fuentes preservadas quedaron exactos. Máximo dos backtests globales y un análisis simultáneo. 2026 permaneció cerrado incluso a inspección.

## Prueba de comisiones endógenas
|Fee por lado|Neto K1001 B/C|Δ vs Y902 B/C|Δ vs N204 B/C|
|---|---:|---:|---:|
|0.045%|13619.21 / 13854.33|172.98 / 173.98|562.60 / 614.88|
|0.070%|10921.35 / 11062.11|127.40 / 144.93|654.04 / 653.18|
|0.095%|9697.64 / 9762.80|127.12 / 156.18|715.29 / 772.62|

Se compara cada candidata con N204 y Y902 al mismo fee, misma cartera B/C y ventana. Pagar más comisiones reduce el neto absoluto. Las diferencias incluyen los efectos reales del fee sobre sizing, capital, filtros y BE de PAXG. No son pruebas de liquidez, slippage, rechazo o latencia. Los overlays +5/+10 de las matrices son otra cosa: coste adicional sobre cantidades/recorridos fijos.

## Vecinos del objetivo
|Objetivo suplemento|Neto K1001 B/C|Δ vs N204 B/C|Δ vs Y902 al mismo TP B/C|
|---|---:|---:|---:|
|1.8R|13256.82 / 13466.39|200.20 / 226.95|172.24 / 172.87|
|2.2R|13540.35 / 13757.39|483.73 / 517.95|187.70 / 193.62|

El control 2R original sigue congelado. Variar a 1.8R reduce su ventaja frente al propio K1001 2R en 362.39/387.93 USDT; variar a 2.2R, en 78.87/96.93. La ventaja sobre N204 permanece en los tres objetivos. La estabilidad alrededor del parámetro no agrega nuevas operaciones nominales independientes: son repeticiones modificadas de la misma historia.

## Incertidumbre y concentración incremental
|Fee|Comparador primario|Media incremento USDT/mes B/C (61 completos)|IC95% media B|IC95% media C|Sin mejor mes,63 incluidos B/C|
|---|---|---:|---|---|---:|
|nominal|Y902|2.894 / 2.929|-1.449 a 9.459|-1.250 a 9.393|4.27 / 3.25|
|F70|Y902|2.132 / 2.442|-1.440 a 7.883|-1.246 a 8.322|-33.66 / -17.83|
|F95|Y902|2.128 / 2.632|-1.354 a 7.718|-1.144 a 8.547|-24.38 / -0.15|

Primario K1001 frente a Y902; secundario K1001 frente a N204. Bootstrap pareado circular, bloques de seis meses, 10000 réplicas, seed9022026 y mismos índices entre B/C, comparadores y niveles de fee. Los 61 meses completos son primarios; los 63 incluidos, secundarios. IC de percentiles del 95% para diferencia media mensual en USDT. La fracción de réplicas positivas no es probabilidad de ventaja real. No hay ajuste por todas las búsquedas anteriores ni validación fuera de muestra.

En nominal, julio de 2024 aporta 168.71/170.73 USDT de los 172.98/173.98 totales de ventaja frente a Y902. Al descontarlo aritméticamente quedan +4.27/+3.25; con fee0.070%, −33.66/−17.83; con0.095%, −24.38/−0.15. Omitir todo2024 nominal deja −25.91/−22.39. Son diagnósticos aritméticos, no una nueva simulación con diferente capital. No se añadieron reglas para rescatar ese mes ni se relajó el protocolo.

Frente a N204 las cifras son más favorables porque incorporan la mejora previa de Y902. No atribuir todo ese salto al mínimo conjunto de K1001. La comparación incremental revela la limitación de muestra.

## Qué se retiene
K1001 es una candidata razonable para continuar investigando por su equilibrio: menor drawdown y un mes positivo adicional bajo +5bps respecto a Y902 en cada cartera, con mejora de PF y resultados bajo fees mayores. El número de casos modificados sigue siendo cinco. Para aumentar confianza hace falta evidencia realmente nueva; más barridos de esta misma muestra no la crean.

K1005 produjo mayor neto nominal y menor concentración monetaria frente a N204, pero sólo cambió cinco salidas. No heredó esta validación propia de K1001 ni la de Y902; permanece separada, sin más backtests en R10.

## Cierre de R9 y limpieza
R9 quedó completada con20/20corridas auditadas; resultados e informe final guardados. El fallo MCP se recuperó comprobando corridas existentes, sin duplicarlas. La discrepancia de snapshot era una representación por classname versus exchange-symbol, con código idéntico.

Se archivaron permanentemente13workspaces temporales R8 antes de eliminarlos. Auditorías, MTM mensual, paths, código, manifiestos y originales en sesiones quedaron preservados; los CSV/figuras derivados son reproducibles. No se borraron estrategias, sesiones, trades, velas ni informes. Inventario temporal65.51MiB y archivos permanentes6.02MiB; saldo aproximado59.50MiB del inventario, sin medición de disco libre ni causalidad demostrada del error. Durante esta continuación las consultas MCP respondieron; no se declara arreglado un fallo intermitente por esa observación.

## Evidencia
- BTC_R10_K1001_FROZEN_VALIDATION_20261019.md
- BTC_R10_K1001_RESULTS_MATRIX_20261019.md — ocho casos con URLs y métricas completas
- BTC_R10_K1001_FINAL_MANIFEST_20261019.md
- BTC_R10_AUDIT_K170/K195/K118/K122_20261019.md y sus SLEEVE_IDENTIFICATION
- BTC_R10_K1001_TP_SOURCE_QA_20261019.md —63comprobaciones sintéticas, no prueba estadística
- BTC_R10_UNCERTAINTY_SOURCE_20261019.md y BTC_R10_UNCERTAINTY_RESULTS_20261019.md
- MCP_CLEANUP_TRACE_MANIFEST_20261019.md y13ARCHIVE_R8_...permanentes
- BTC_TODAY_PROGRESS_ALL_METRICS_20261019.md —94sesiones únicas creadas hoy verificadas, seis hitos, descartes, controles,45métricas del motor y auditorías adicionales en siete archivos JSON.

## Evaluación reproducible
```json
{
  "frozen_operational_cost_test_vsN204": true,
  "cost_retention_vs_Y902": true,
  "frozen_tp_neighbour_diagnostic": true,
  "fees": [
    {
      "level": "K170",
      "rows": [
        {
          "portfolio": "B",
          "net": 10921.347327857897,
          "dd": -9.085333006504248,
          "delta_N204": 654.0359486705747,
          "delta_Y902": 127.39788892558863
        },
        {
          "portfolio": "C",
          "net": 11062.114149208523,
          "dd": -9.055907224278215,
          "delta_N204": 653.1788753075762,
          "delta_Y902": 144.93399493266043
        }
      ]
    },
    {
      "level": "K195",
      "rows": [
        {
          "portfolio": "B",
          "net": 9697.641826632267,
          "dd": -9.296608221980684,
          "delta_N204": 715.2881218218718,
          "delta_Y902": 127.1219901744862
        },
        {
          "portfolio": "C",
          "net": 9762.803908226633,
          "dd": -9.28545641066888,
          "delta_N204": 772.6207483387443,
          "delta_Y902": 156.18411382829072
        }
      ]
    }
  ],
  "neighbours": [
    {
      "level": "K118",
      "rows": [
        {
          "portfolio": "B",
          "net": 13256.819212769862,
          "delta_N204": 200.20429769219845,
          "delta_Y902_matchingTP": 172.23555434838272,
          "delta_K1001_2R": -362.394556238085,
          "dd": -8.823158391912777
        },
        {
          "portfolio": "C",
          "net": 13466.394171058037,
          "delta_N204": 226.9517912112442,
          "delta_Y902_matchingTP": 172.86646106291846,
          "delta_K1001_2R": -387.93139921939473,
          "dd": -8.78969880958006
        }
      ]
    },
    {
      "level": "K122",
      "rows": [
        {
          "portfolio": "B",
          "net": 13540.345605905915,
          "delta_N204": 483.7306908282517,
          "delta_Y902_matchingTP": 187.70451287793912,
          "delta_K1001_2R": -78.86816310203176,
          "dd": -8.830470725245565
        },
        {
          "portfolio": "C",
          "net": 13757.392237377382,
          "delta_N204": 517.9498575305897,
          "delta_Y902_matchingTP": 193.61768577924886,
          "delta_K1001_2R": -96.93333290004921,
          "dd": -8.776441996440386
        }
      ]
    }
  ],
  "primary_ci_all_include_zero": true,
  "uncertainty": [
    {
      "fee_level": "nominal",
      "seed": 9022026,
      "replicates": 10000,
      "circular_block_months": 6,
      "comparisons": {
        "K1001_vs_Y902": {
          "role": "primary",
          "candidate": "K1001",
          "reference": "Y902",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.894468632260527,
                  "observed_total_USDT": 176.56258656789214,
                  "ci95_percentile_mean_USDT_month": [
                    -1.449051948705625,
                    9.458610385383803
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8139,
                  "positive_delta_months": 27,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 168.7063773271766,
                  "delta_omitting_best_month_arithmetic_USDT": 7.856209240715543,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -34.83748013067634,
                    "2022": -9.158937174870516,
                    "2023": -10.681251348914884,
                    "2024": 198.89303415766335,
                    "2025": 32.34722106469053
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 176.56258656789214,
                    "2021": 211.40006669856848,
                    "2022": 185.72152374276266,
                    "2023": 187.24383791680702,
                    "2024": -22.33044758977121,
                    "2025": 144.2153655032016
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.9293991447953944,
                  "observed_total_USDT": 178.69334783251907,
                  "ci95_percentile_mean_USDT_month": [
                    -1.2501886592151117,
                    9.393369160303982
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8221,
                  "positive_delta_months": 24,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 170.7298142755717,
                  "delta_omitting_best_month_arithmetic_USDT": 7.963533556947368,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -32.86093660237202,
                    "2022": -2.9748821056764427,
                    "2023": -10.551375087474298,
                    "2024": 196.36302221141523,
                    "2025": 28.7175194166266
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 178.69334783251907,
                    "2021": 211.5542844348911,
                    "2022": 181.6682299381955,
                    "2023": 189.24472291999336,
                    "2024": -17.66967437889616,
                    "2025": 149.97582841589247
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.7457022767097414,
                  "observed_total_USDT": 172.9792434327137,
                  "ci95_percentile_mean_USDT_month": [
                    -1.4857375459661153,
                    9.141056757731802
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8049,
                  "positive_delta_months": 27,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 168.7063773271766,
                  "delta_omitting_best_month_arithmetic_USDT": 4.272866105537105,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -34.83748013067634,
                    "2022": -9.158937174870516,
                    "2023": -10.681251348914884,
                    "2024": 198.89303415766335,
                    "2025": 28.76387792951209
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 172.9792434327137,
                    "2021": 207.81672356339004,
                    "2022": 182.13818060758422,
                    "2023": 183.66049478162859,
                    "2024": -25.91379072494965,
                    "2025": 144.2153655032016
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.7615301490641575,
                  "observed_total_USDT": 173.97639939104192,
                  "ci95_percentile_mean_USDT_month": [
                    -1.312855668540439,
                    9.061830767791541
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8092,
                  "positive_delta_months": 24,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 170.7298142755717,
                  "delta_omitting_best_month_arithmetic_USDT": 3.246585115470225,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -32.86093660237202,
                    "2022": -2.9748821056764427,
                    "2023": -10.551375087474298,
                    "2024": 196.36302221141523,
                    "2025": 24.000570975149458
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 173.97639939104192,
                    "2021": 206.83733599341394,
                    "2022": 176.95128149671837,
                    "2023": 184.52777447851622,
                    "2024": -22.386622820373304,
                    "2025": 149.97582841589247
                  }
                }
              }
            }
          }
        },
        "K1001_vs_N204": {
          "role": "secondary",
          "candidate": "K1001",
          "reference": "N204",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 5.991718426221179,
                  "observed_total_USDT": 365.4948239994919,
                  "ci95_percentile_mean_USDT_month": [
                    -14.516881142707138,
                    28.6444244703024
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.6942,
                  "positive_delta_months": 28,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 407.25312203934845,
                  "delta_omitting_best_month_arithmetic_USDT": -41.75829803985653,
                  "year_delta_USDT": {
                    "2020": -32.97982371443686,
                    "2021": -13.611822798811772,
                    "2022": 145.0701913774501,
                    "2023": 276.7929084147563,
                    "2024": 125.80796117706268,
                    "2025": -135.58459045652853
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 398.4746477139288,
                    "2021": 379.1066467983037,
                    "2022": 220.42463262204183,
                    "2023": 88.70191558473562,
                    "2024": 239.68686282242925,
                    "2025": 501.07941445602046
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 6.8856395834205975,
                  "observed_total_USDT": 420.0240145886564,
                  "ci95_percentile_mean_USDT_month": [
                    -13.204085891400945,
                    29.00400965678242
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7274,
                  "positive_delta_months": 29,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 398.45457841226926,
                  "delta_omitting_best_month_arithmetic_USDT": 21.56943617638717,
                  "year_delta_USDT": {
                    "2020": -32.98046405748573,
                    "2021": -6.923773029635413,
                    "2022": 145.92853106626717,
                    "2023": 304.75646447744657,
                    "2024": 128.23006810496372,
                    "2025": -118.98681197289989
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 453.00447864614216,
                    "2021": 426.94778761829184,
                    "2022": 274.09548352238926,
                    "2023": 115.26755011120986,
                    "2024": 291.7939464836927,
                    "2025": 539.0108265615563
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 8.930140538576014,
                  "observed_total_USDT": 562.5988539302889,
                  "ci95_percentile_mean_USDT_month": [
                    -10.093505092573187,
                    29.64669779320763
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.803,
                  "positive_delta_months": 29,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 407.25312203934845,
                  "delta_omitting_best_month_arithmetic_USDT": 155.34573189094044,
                  "year_delta_USDT": {
                    "2020": -32.97982371443686,
                    "2021": -13.611822798811772,
                    "2022": 145.0701913774501,
                    "2023": 276.7929084147563,
                    "2024": 125.80796117706268,
                    "2025": 61.51943947426844
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 595.5786776447258,
                    "2021": 576.2106767291007,
                    "2022": 417.5286625528388,
                    "2023": 285.8059455155326,
                    "2024": 436.7908927532262,
                    "2025": 501.07941445602046
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 9.760050641756116,
                  "observed_total_USDT": 614.8831904306353,
                  "ci95_percentile_mean_USDT_month": [
                    -8.9174155076187,
                    29.812432393181425
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8378,
                  "positive_delta_months": 30,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 398.45457841226926,
                  "delta_omitting_best_month_arithmetic_USDT": 216.42861201836604,
                  "year_delta_USDT": {
                    "2020": -32.98046405748573,
                    "2021": -6.923773029635413,
                    "2022": 145.92853106626717,
                    "2023": 304.75646447744657,
                    "2024": 128.23006810496372,
                    "2025": 75.87236386907898
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 647.863654488121,
                    "2021": 621.8069634602707,
                    "2022": 468.9546593643681,
                    "2023": 310.1267259531887,
                    "2024": 486.6531223256716,
                    "2025": 539.0108265615563
                  }
                }
              }
            }
          }
        }
      },
      "audits": {
        "N204B": {
          "name": "N204B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 41,
            "win_months_all": 0.6721311475409836,
            "win_months_active": 0.6721311475409836,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.6507936507936508,
          "win_months_active": 0.6507936507936508,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.038363339801451346
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03892475898116354
          ],
          "daily_close_drawdown_pct": -8.767001235283322,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.07155623932051774,
              "SPY-USDT": -0.044465817759826935
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.07155623932051774,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.036221631169714885
            },
            "SPY-USDT": {
              "BTC-USDT": -0.044465817759826935,
              "PAXG-USDT": -0.036221631169714885,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.044393834400308974,
            "2021-12-31 00:00:00+00:00": 0.20526646535936122,
            "2022-12-31 00:00:00+00:00": 0.10834108700431222,
            "2023-12-31 00:00:00+00:00": 0.1957195771013449,
            "2024-12-31 00:00:00+00:00": 0.16693816310374676,
            "2025-12-31 00:00:00+00:00": 0.1843977062028026
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "N204C": {
          "name": "N204C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 42,
            "win_months_all": 0.6885245901639344,
            "win_months_active": 0.6885245901639344,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.6666666666666666,
          "win_months_active": 0.6666666666666666,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.046908056267221165
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.04756286766151652
          ],
          "daily_close_drawdown_pct": -9.116483595648194,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.07197005104132922,
              "SPY-USDT": -0.027676293072568095
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.07197005104132922,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.019618927714605973
            },
            "SPY-USDT": {
              "BTC-USDT": -0.027676293072568095,
              "PAXG-USDT": 0.019618927714605973,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04350741280602666,
            "2021-12-31 00:00:00+00:00": 0.1829381961996599,
            "2022-12-31 00:00:00+00:00": 0.11156549325981024,
            "2023-12-31 00:00:00+00:00": 0.23934621951238078,
            "2024-12-31 00:00:00+00:00": 0.1614791972366636,
            "2025-12-31 00:00:00+00:00": 0.17660034423036675
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902B": {
          "name": "Y902B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 42,
            "win_months_all": 0.6885245901639344,
            "win_months_active": 0.7,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6666666666666666,
          "win_months_active": 0.6774193548387096,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03864759352480418
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.029834818684366105
          ],
          "daily_close_drawdown_pct": -9.684509247343975,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.11840400005480689,
              "SPY-USDT": -0.060131609315366825
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.11840400005480689,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.03604179963433085
            },
            "SPY-USDT": {
              "BTC-USDT": -0.060131609315366825,
              "PAXG-USDT": -0.03604179963433085,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04109585202886534,
            "2021-12-31 00:00:00+00:00": 0.2079554885765169,
            "2022-12-31 00:00:00+00:00": 0.12070613973951572,
            "2023-12-31 00:00:00+00:00": 0.21413802037221719,
            "2024-12-31 00:00:00+00:00": 0.15847277269441817,
            "2025-12-31 00:00:00+00:00": 0.1827305525050913
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902C": {
          "name": "Y902C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 43,
            "win_months_all": 0.7049180327868853,
            "win_months_active": 0.7166666666666667,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6825396825396826,
          "win_months_active": 0.6935483870967742,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04691767454945284
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03799927530095615
          ],
          "daily_close_drawdown_pct": -9.627684656189272,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.11810829226435761,
              "SPY-USDT": -0.09749501174089902
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.11810829226435761,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.020145322737922546
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09749501174089902,
              "PAXG-USDT": 0.020145322737922546,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04020936640027806,
            "2021-12-31 00:00:00+00:00": 0.1860116688302591,
            "2022-12-31 00:00:00+00:00": 0.12369884401606512,
            "2023-12-31 00:00:00+00:00": 0.25964143568722764,
            "2024-12-31 00:00:00+00:00": 0.15335000549508826,
            "2025-12-31 00:00:00+00:00": 0.1757646142427156
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001B": {
          "name": "K1001B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 43,
            "win_months_all": 0.7049180327868853,
            "win_months_active": 0.7166666666666667,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6825396825396826,
          "win_months_active": 0.6935483870967742,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03864759352480418
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.029834818684366105
          ],
          "daily_close_drawdown_pct": -8.813370029673173,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.115888986253931,
              "SPY-USDT": -0.05545370865875357
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.115888986253931,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.03604534854691037
            },
            "SPY-USDT": {
              "BTC-USDT": -0.05545370865875357,
              "PAXG-USDT": -0.03604534854691037,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04109585202886534,
            "2021-12-31 00:00:00+00:00": 0.20460925680902076,
            "2022-12-31 00:00:00+00:00": 0.1203111325381947,
            "2023-12-31 00:00:00+00:00": 0.2140483443686969,
            "2024-12-31 00:00:00+00:00": 0.17064101474328153,
            "2025-12-31 00:00:00+00:00": 0.182851311747513
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001C": {
          "name": "K1001C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 44,
            "win_months_all": 0.7213114754098361,
            "win_months_active": 0.7333333333333333,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6984126984126984,
          "win_months_active": 0.7096774193548387,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04691767454945284
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03799927530095615
          ],
          "daily_close_drawdown_pct": -8.774326461196647,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.11647914983405412,
              "SPY-USDT": -0.09417283536168991
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.11647914983405412,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.02014452947742552
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09417283536168991,
              "PAXG-USDT": 0.02014452947742552,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04020936640027806,
            "2021-12-31 00:00:00+00:00": 0.18285259935215104,
            "2022-12-31 00:00:00+00:00": 0.12378743025229832,
            "2023-12-31 00:00:00+00:00": 0.25955125778452737,
            "2024-12-31 00:00:00+00:00": 0.165033233470121,
            "2025-12-31 00:00:00+00:00": 0.17564830911872442
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        }
      },
      "anchors": {
        "BTC-USDT": {
          "anchor_count": 69,
          "distinct_anchor_timestamps": 35,
          "scale": 1.1501999999999981,
          "max_relative_error": 1.3322676295501878e-15
        },
        "PAXG-USDT": {
          "anchor_count": 30,
          "distinct_anchor_timestamps": 15,
          "scale": 0.19228799999999985,
          "max_relative_error": 1.5543122344752192e-15
        },
        "SPY-USDT": {
          "anchor_count": 18,
          "distinct_anchor_timestamps": 16,
          "scale": 0.03484345999999994,
          "max_relative_error": 1.7763568394002505e-15
        }
      },
      "sessions": {
        "N204B": {
          "session_id": "bc5aaba6-2746-4e90-b0de-7b7955b66142",
          "fee_per_side": 0.00045,
          "net": 13056.614915077666,
          "title": "MCP Backtest: X03 R2 N204 B — positive-pressure cohort VWAP"
        },
        "N204C": {
          "session_id": "6dead093-4663-4da9-ac62-c2ad9f9bb794",
          "fee_per_side": 0.00045,
          "net": 13239.442379846789,
          "title": "MCP Backtest: X03 R2 N204 C — positive-pressure cohort VWAP"
        },
        "Y902B": {
          "session_id": "cb305a17-1312-463e-bbf1-c8173dfae22c",
          "fee_per_side": 0.00045,
          "net": 13446.23452557522,
          "title": "MCP Backtest: BTC R8 Y902B creative frozen"
        },
        "Y902C": {
          "session_id": "b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff",
          "fee_per_side": 0.00045,
          "net": 13680.349170886388,
          "title": "MCP Backtest: BTC R8 Y902C creative frozen"
        },
        "K1001B": {
          "session_id": "10be7d01-51f7-480c-9b6c-8b653da82c5a",
          "fee_per_side": 0.00045,
          "net": 13619.21376900794,
          "title": "MCP Backtest: R9 K1001B Y902 one mechanism"
        },
        "K1001C": {
          "session_id": "08d01428-7abe-410a-bf7d-f8c8d46aa35c",
          "fee_per_side": 0.00045,
          "net": 13854.325570277424,
          "title": "MCP Backtest: R9 K1001C Y902 one mechanism"
        }
      },
      "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
    },
    {
      "fee_level": "F70",
      "seed": 9022026,
      "replicates": 10000,
      "circular_block_months": 6,
      "comparisons": {
        "K1001_vs_Y902": {
          "role": "primary",
          "candidate": "K1001",
          "reference": "Y902",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.1322542233643675,
                  "observed_total_USDT": 130.06750762522643,
                  "ci95_percentile_mean_USDT_month": [
                    -1.440017036341977,
                    7.8830275956810425
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7063,
                  "positive_delta_months": 24,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 161.05473062081728,
                  "delta_omitting_best_month_arithmetic_USDT": -30.987222995590855,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -31.67202715408166,
                    "2022": -1.8355130094441847,
                    "2023": -6.486969895369839,
                    "2024": 165.21016921658156,
                    "2025": 4.851848467540549
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 130.06750762522643,
                    "2021": 161.7395347793081,
                    "2022": 131.9030206346706,
                    "2023": 136.55447752059627,
                    "2024": -35.142661591355136,
                    "2025": 125.21565915768588
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.4415790997037057,
                  "observed_total_USDT": 148.93632508192604,
                  "ci95_percentile_mean_USDT_month": [
                    -1.2458057705443308,
                    8.321593516646033
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7681,
                  "positive_delta_months": 25,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 162.7638465753953,
                  "delta_omitting_best_month_arithmetic_USDT": -13.827521493469249,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.20209731599971,
                    "2022": -3.770469157894695,
                    "2023": -7.186357776106888,
                    "2024": 167.48219903971767,
                    "2025": 22.613050292209664
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 148.93632508192604,
                    "2021": 179.13842239792575,
                    "2022": 152.70679423982074,
                    "2023": 156.12268285803293,
                    "2024": -18.545873957791628,
                    "2025": 126.32327478971638
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.022188713104639,
                  "observed_total_USDT": 127.39788892559227,
                  "ci95_percentile_mean_USDT_month": [
                    -1.4450084478800038,
                    7.59939448901986
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.6898,
                  "positive_delta_months": 24,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 161.05473062081728,
                  "delta_omitting_best_month_arithmetic_USDT": -33.65684169522501,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -31.67202715408166,
                    "2022": -1.8355130094441847,
                    "2023": -6.486969895369839,
                    "2024": 165.21016921658156,
                    "2025": 2.1822297679063922
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 127.39788892559227,
                    "2021": 159.06991607967393,
                    "2022": 129.23340193503645,
                    "2023": 133.8848588209621,
                    "2024": -37.81228029098929,
                    "2025": 125.21565915768588
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.300539602105663,
                  "observed_total_USDT": 144.9339949326568,
                  "ci95_percentile_mean_USDT_month": [
                    -1.2950472300093239,
                    8.018543529907754
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7483,
                  "positive_delta_months": 25,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 162.7638465753953,
                  "delta_omitting_best_month_arithmetic_USDT": -17.829851642738504,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.20209731599971,
                    "2022": -3.770469157894695,
                    "2023": -7.186357776106888,
                    "2024": 167.48219903971767,
                    "2025": 18.61072014294041
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 144.9339949326568,
                    "2021": 175.1360922486565,
                    "2022": 148.70446409055148,
                    "2023": 152.12035270876368,
                    "2024": -22.548204107060883,
                    "2025": 126.32327478971638
                  }
                }
              }
            }
          }
        },
        "K1001_vs_N204": {
          "role": "secondary",
          "candidate": "K1001",
          "reference": "N204",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 7.857369847231834,
                  "observed_total_USDT": 479.2995606811419,
                  "ci95_percentile_mean_USDT_month": [
                    -11.48878331130139,
                    29.309857071302716
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.764,
                  "positive_delta_months": 29,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 400.0685127057186,
                  "delta_omitting_best_month_arithmetic_USDT": 79.23104797542328,
                  "year_delta_USDT": {
                    "2020": -31.73123376250078,
                    "2021": 13.988572646963803,
                    "2022": 168.26854493038445,
                    "2023": 307.38395138481064,
                    "2024": 131.1685214869285,
                    "2025": -109.77879600544475
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 511.03079444364266,
                    "2021": 465.3109880341781,
                    "2022": 311.03101575075743,
                    "2023": 171.91560929633124,
                    "2024": 348.1310391942134,
                    "2025": 589.0783566865866
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 7.867206051602702,
                  "observed_total_USDT": 479.89956914776485,
                  "ci95_percentile_mean_USDT_month": [
                    -11.232547066017997,
                    28.840337090745415
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7712,
                  "positive_delta_months": 29,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 391.6854081324964,
                  "delta_omitting_best_month_arithmetic_USDT": 88.21416101526847,
                  "year_delta_USDT": {
                    "2020": -28.923563857602858,
                    "2021": -4.080409712996698,
                    "2022": 162.29090377899593,
                    "2023": 328.0470853612187,
                    "2024": 132.97293676974186,
                    "2025": -110.40738319159209
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 508.8231330053677,
                    "2021": 483.97997886076155,
                    "2022": 317.6086653687689,
                    "2023": 151.85248378654614,
                    "2024": 346.926632378023,
                    "2025": 590.3069523393569
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 10.381522994771258,
                  "observed_total_USDT": 654.0359486705893,
                  "ci95_percentile_mean_USDT_month": [
                    -7.606645313563973,
                    30.086094449182404
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8585,
                  "positive_delta_months": 30,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 400.0685127057186,
                  "delta_omitting_best_month_arithmetic_USDT": 253.96743596487067,
                  "year_delta_USDT": {
                    "2020": -31.73123376250078,
                    "2021": 13.988572646963803,
                    "2022": 168.26854493038445,
                    "2023": 307.38395138481064,
                    "2024": 131.1685214869285,
                    "2025": 64.95759198400265
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 685.76718243309,
                    "2021": 640.0473760236255,
                    "2022": 485.7674037402048,
                    "2023": 346.65199728577863,
                    "2024": 522.8674271836608,
                    "2025": 589.0783566865866
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 10.367918655675552,
                  "observed_total_USDT": 653.1788753075598,
                  "ci95_percentile_mean_USDT_month": [
                    -7.334272427633265,
                    29.62502886448148
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8636,
                  "positive_delta_months": 30,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 391.6854081324964,
                  "delta_omitting_best_month_arithmetic_USDT": 261.4934671750634,
                  "year_delta_USDT": {
                    "2020": -28.923563857602858,
                    "2021": -4.080409712996698,
                    "2022": 162.29090377899593,
                    "2023": 328.0470853612187,
                    "2024": 132.97293676974186,
                    "2025": 62.87192296820285
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 682.1024391651627,
                    "2021": 657.2592850205565,
                    "2022": 490.88797152856387,
                    "2023": 325.1317899463411,
                    "2024": 520.2059385378179,
                    "2025": 590.3069523393569
                  }
                }
              }
            }
          }
        }
      },
      "audits": {
        "N204B": {
          "name": "N204B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.639344262295082,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6190476190476191,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.038848358930312465
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03999068035568787
          ],
          "daily_close_drawdown_pct": -9.016913649811187,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.05686964789050526,
              "SPY-USDT": -0.04147158152763939
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.05686964789050526,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.014546551320336236
            },
            "SPY-USDT": {
              "BTC-USDT": -0.04147158152763939,
              "PAXG-USDT": -0.014546551320336236,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04176490528852406,
            "2021-12-31 00:00:00+00:00": 0.19293771742976462,
            "2022-12-31 00:00:00+00:00": 0.09627479171191311,
            "2023-12-31 00:00:00+00:00": 0.17010613650971895,
            "2024-12-31 00:00:00+00:00": 0.1476817377857611,
            "2025-12-31 00:00:00+00:00": 0.10775186795994296
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "N204C": {
          "name": "N204C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.639344262295082,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6190476190476191,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.047251327773334295
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.04816889094485366
          ],
          "daily_close_drawdown_pct": -9.129358487210226,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.05689878151177862,
              "SPY-USDT": -0.02630385139288716
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.05689878151177862,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.051030089284193746
            },
            "SPY-USDT": {
              "BTC-USDT": -0.02630385139288716,
              "PAXG-USDT": 0.051030089284193746,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04066056152449837,
            "2021-12-31 00:00:00+00:00": 0.17303460717258634,
            "2022-12-31 00:00:00+00:00": 0.09933372295964626,
            "2023-12-31 00:00:00+00:00": 0.20948307076791073,
            "2024-12-31 00:00:00+00:00": 0.14209026334265262,
            "2025-12-31 00:00:00+00:00": 0.10095775196807155
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902B": {
          "name": "Y902B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.65,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6290322580645161,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03888659189731081
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.030451527729527417
          ],
          "daily_close_drawdown_pct": -9.923047650902461,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10595059634836346,
              "SPY-USDT": -0.05885082162933863
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10595059634836346,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.014310818094433752
            },
            "SPY-USDT": {
              "BTC-USDT": -0.05885082162933863,
              "PAXG-USDT": -0.014310818094433752,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03859178191227408,
            "2021-12-31 00:00:00+00:00": 0.19792357929736681,
            "2022-12-31 00:00:00+00:00": 0.10983927548507899,
            "2023-12-31 00:00:00+00:00": 0.19056989340064479,
            "2024-12-31 00:00:00+00:00": 0.14113817299290132,
            "2025-12-31 00:00:00+00:00": 0.1084338218840859
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902C": {
          "name": "Y902C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 40,
            "win_months_all": 0.6557377049180327,
            "win_months_active": 0.6666666666666666,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6349206349206349,
          "win_months_active": 0.6451612903225806,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04730147962280684
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03894627094830605
          ],
          "daily_close_drawdown_pct": -9.910800423988098,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10574946115703875,
              "SPY-USDT": -0.09982191619623061
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10574946115703875,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.05167426692483106
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09982191619623061,
              "PAXG-USDT": 0.05167426692483106,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03776820513873802,
            "2021-12-31 00:00:00+00:00": 0.17603397301931434,
            "2022-12-31 00:00:00+00:00": 0.11296308942708433,
            "2023-12-31 00:00:00+00:00": 0.23164530857531296,
            "2024-12-31 00:00:00+00:00": 0.1357936399299018,
            "2025-12-31 00:00:00+00:00": 0.10082189127555097
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001B": {
          "name": "K1001B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 40,
            "win_months_all": 0.6557377049180327,
            "win_months_active": 0.6666666666666666,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6349206349206349,
          "win_months_active": 0.6451612903225806,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03888659189731081
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.030451527729527417
          ],
          "daily_close_drawdown_pct": -9.07556919478677,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10249422179335252,
              "SPY-USDT": -0.05532097256829756
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10249422179335252,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.014308405375482896
            },
            "SPY-USDT": {
              "BTC-USDT": -0.05532097256829756,
              "PAXG-USDT": -0.014308405375482896,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03859178191227408,
            "2021-12-31 00:00:00+00:00": 0.19487406285542397,
            "2022-12-31 00:00:00+00:00": 0.10997169591531142,
            "2023-12-31 00:00:00+00:00": 0.19056252900850068,
            "2024-12-31 00:00:00+00:00": 0.151556461086507,
            "2025-12-31 00:00:00+00:00": 0.10783041182031727
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001C": {
          "name": "K1001C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 41,
            "win_months_all": 0.6721311475409836,
            "win_months_active": 0.6833333333333333,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6507936507936508,
          "win_months_active": 0.6612903225806451,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04730147962280684
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03894627094830605
          ],
          "daily_close_drawdown_pct": -9.05306136808578,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10213839924496018,
              "SPY-USDT": -0.09683905734982227
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10213839924496018,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.051676460265234196
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09683905734982227,
              "PAXG-USDT": 0.051676460265234196,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03776820513873802,
            "2021-12-31 00:00:00+00:00": 0.17312367983761479,
            "2022-12-31 00:00:00+00:00": 0.11293362187628975,
            "2023-12-31 00:00:00+00:00": 0.23169573429990842,
            "2024-12-31 00:00:00+00:00": 0.14616434400321077,
            "2025-12-31 00:00:00+00:00": 0.1011290141958221
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        }
      },
      "anchors": {
        "BTC-USDT": {
          "anchor_count": 69,
          "distinct_anchor_timestamps": 35,
          "scale": 1.1501999999999981,
          "max_relative_error": 1.3322676295501878e-15
        },
        "PAXG-USDT": {
          "anchor_count": 30,
          "distinct_anchor_timestamps": 15,
          "scale": 0.19228799999999985,
          "max_relative_error": 1.5543122344752192e-15
        },
        "SPY-USDT": {
          "anchor_count": 18,
          "distinct_anchor_timestamps": 16,
          "scale": 0.03484345999999994,
          "max_relative_error": 1.7763568394002505e-15
        }
      },
      "sessions": {
        "N204B": {
          "session_id": "9a6c7c24-8847-42d1-aadb-206f21723c1f",
          "fee_per_side": 0.0007,
          "net": 10267.311379187326,
          "title": "MCP Backtest: X03 R2 CONF5 B — selected N204 engine-fee confirmation"
        },
        "N204C": {
          "session_id": "541d2bf4-ffca-4f2d-969b-c25165e7b960",
          "fee_per_side": 0.0007,
          "net": 10408.935273900948,
          "title": "MCP Backtest: X03 R2 CONF5 C — selected N204 engine-fee confirmation"
        },
        "Y902B": {
          "session_id": "c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
          "fee_per_side": 0.0007,
          "net": 10793.949438932308,
          "title": "MCP Backtest: BTC R9 F70B validation"
        },
        "Y902C": {
          "session_id": "2297b82f-5db7-457a-8d46-9b53465dde7d",
          "fee_per_side": 0.0007,
          "net": 10917.180154275862,
          "title": "MCP Backtest: BTC R9 F70C validation"
        },
        "K1001B": {
          "session_id": "4d403a37-8248-4346-8da5-708b68bdf00b",
          "fee_per_side": 0.0007,
          "net": 10921.347327857895,
          "title": "MCP Backtest: BTC R10 K170B validation"
        },
        "K1001C": {
          "session_id": "3c84ed42-1d2a-4cf6-bd29-0daba6830eb9",
          "fee_per_side": 0.0007,
          "net": 11062.114149208526,
          "title": "MCP Backtest: BTC R10 K170C validation"
        }
      },
      "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
    },
    {
      "fee_level": "F95",
      "seed": 9022026,
      "replicates": 10000,
      "circular_block_months": 6,
      "comparisons": {
        "K1001_vs_Y902": {
          "role": "primary",
          "candidate": "K1001",
          "reference": "Y902",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.128061039537584,
                  "observed_total_USDT": 129.81172341179263,
                  "ci95_percentile_mean_USDT_month": [
                    -1.3538259930503,
                    7.718481480756962
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7229,
                  "positive_delta_months": 27,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 151.50043942632874,
                  "delta_omitting_best_month_arithmetic_USDT": -21.688716014536112,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.193917786000384,
                    "2022": -5.0581992201914545,
                    "2023": -7.47664895375965,
                    "2024": 159.09377713929098,
                    "2025": 13.446712232453137
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 129.81172341179263,
                    "2021": 160.005641197793,
                    "2022": 134.86992263198408,
                    "2023": 137.28837236555228,
                    "2024": -29.28205372749835,
                    "2025": 116.36501117933949
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.6320264824409874,
                  "observed_total_USDT": 160.55361542890023,
                  "ci95_percentile_mean_USDT_month": [
                    -1.144132531501091,
                    8.547028328678277
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8088,
                  "positive_delta_months": 20,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 156.33020812871473,
                  "delta_omitting_best_month_arithmetic_USDT": 4.2234073001854995,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.18146699550016,
                    "2022": -3.3999357883840275,
                    "2023": -6.266811481473269,
                    "2024": 181.17556133210564,
                    "2025": 19.22626836215204
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 160.55361542890023,
                    "2021": 190.7350824244004,
                    "2022": 163.95355121728426,
                    "2023": 166.8204269103735,
                    "2024": -20.621945903205415,
                    "2025": 141.3273470667482
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 2.017809367849074,
                  "observed_total_USDT": 127.12199017449166,
                  "ci95_percentile_mean_USDT_month": [
                    -1.3518885912376974,
                    7.454533193264929
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.709,
                  "positive_delta_months": 27,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 151.50043942632874,
                  "delta_omitting_best_month_arithmetic_USDT": -24.378449251837083,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.193917786000384,
                    "2022": -5.0581992201914545,
                    "2023": -7.47664895375965,
                    "2024": 159.09377713929098,
                    "2025": 10.756978995152167
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 127.12199017449166,
                    "2021": 157.31590796049204,
                    "2022": 132.1801893946831,
                    "2023": 134.5986391282513,
                    "2024": -31.97178696479932,
                    "2025": 116.36501117933949
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 2.4791129179091453,
                  "observed_total_USDT": 156.18411382827617,
                  "ci95_percentile_mean_USDT_month": [
                    -1.1937762467725954,
                    8.256958345933162
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.7915,
                  "positive_delta_months": 20,
                  "best_incremental_month": "2024-07",
                  "best_incremental_month_delta_USDT": 156.33020812871473,
                  "delta_omitting_best_month_arithmetic_USDT": -0.14609430043856264,
                  "year_delta_USDT": {
                    "2020": 0,
                    "2021": -30.18146699550016,
                    "2022": -3.3999357883840275,
                    "2023": -6.266811481473269,
                    "2024": 181.17556133210564,
                    "2025": 14.856766761527979
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 156.18411382827617,
                    "2021": 186.36558082377633,
                    "2022": 159.5840496166602,
                    "2023": 162.45092530974944,
                    "2024": -24.991447503829477,
                    "2025": 141.3273470667482
                  }
                }
              }
            }
          }
        },
        "K1001_vs_N204": {
          "role": "secondary",
          "candidate": "K1001",
          "reference": "N204",
          "samples": {
            "full61": {
              "months": 61,
              "period_start": "2020-11",
              "period_last": "2025-11",
              "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 8.980602846084427,
                  "observed_total_USDT": 547.81677361115,
                  "ci95_percentile_mean_USDT_month": [
                    -9.734417931286467,
                    29.79767449871671
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8053,
                  "positive_delta_months": 29,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 393.312404021799,
                  "delta_omitting_best_month_arithmetic_USDT": 154.50436958935097,
                  "year_delta_USDT": {
                    "2020": -27.273064877230354,
                    "2021": 10.096256930944946,
                    "2022": 185.4623212105489,
                    "2023": 332.1464588828294,
                    "2024": 136.02357868784748,
                    "2025": -88.63877722379038
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 575.0898384883803,
                    "2021": 537.720516680205,
                    "2022": 362.3544524006011,
                    "2023": 215.6703147283206,
                    "2024": 411.7931949233025,
                    "2025": 636.4555508349404
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 10.002847589216456,
                  "observed_total_USDT": 610.1737029422038,
                  "ci95_percentile_mean_USDT_month": [
                    -8.728892097250853,
                    30.65005135976861
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8379,
                  "positive_delta_months": 31,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 384.85027873193394,
                  "delta_omitting_best_month_arithmetic_USDT": 225.32342421026988,
                  "year_delta_USDT": {
                    "2020": -28.621076137931595,
                    "2021": 16.196128242865598,
                    "2022": 183.868030556363,
                    "2023": 353.1278866032426,
                    "2024": 157.1101190420959,
                    "2025": -71.50738536443168
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 638.7947790801354,
                    "2021": 593.9775746993382,
                    "2022": 426.3056723858408,
                    "2023": 257.04581633896123,
                    "2024": 453.0635839001079,
                    "2025": 681.6810883066355
                  }
                }
              }
            },
            "included63": {
              "months": 63,
              "period_start": "2020-10",
              "period_last": "2025-12",
              "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
              "portfolio": {
                "B": {
                  "observed_mean_USDT_month": 11.353779711458223,
                  "observed_total_USDT": 715.2881218218681,
                  "ci95_percentile_mean_USDT_month": [
                    -6.115041888434288,
                    30.47516537477695
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.8886,
                  "positive_delta_months": 30,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 393.312404021799,
                  "delta_omitting_best_month_arithmetic_USDT": 321.9757178000691,
                  "year_delta_USDT": {
                    "2020": -27.273064877230354,
                    "2021": 10.096256930944946,
                    "2022": 185.4623212105489,
                    "2023": 332.1464588828294,
                    "2024": 136.02357868784748,
                    "2025": 78.83257098692775
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 742.5611866990985,
                    "2021": 705.1918648909232,
                    "2022": 529.8258006113192,
                    "2023": 383.1416629390387,
                    "2024": 579.2645431340206,
                    "2025": 636.4555508349404
                  }
                },
                "C": {
                  "observed_mean_USDT_month": 12.26382140220206,
                  "observed_total_USDT": 772.6207483387298,
                  "ci95_percentile_mean_USDT_month": [
                    -5.124238906000594,
                    31.018108952284518
                  ],
                  "fraction_bootstrap_means_gt_zero": 0.9099,
                  "positive_delta_months": 32,
                  "best_incremental_month": "2022-01",
                  "best_incremental_month_delta_USDT": 384.85027873193394,
                  "delta_omitting_best_month_arithmetic_USDT": 387.7704696067958,
                  "year_delta_USDT": {
                    "2020": -28.621076137931595,
                    "2021": 16.196128242865598,
                    "2022": 183.868030556363,
                    "2023": 353.1278866032426,
                    "2024": 157.1101190420959,
                    "2025": 90.93966003209425
                  },
                  "delta_omitting_each_year_arithmetic_USDT": {
                    "2020": 801.2418244766613,
                    "2021": 756.4246200958642,
                    "2022": 588.7527177823667,
                    "2023": 419.49286173548717,
                    "2024": 615.5106292966339,
                    "2025": 681.6810883066355
                  }
                }
              }
            }
          }
        }
      },
      "audits": {
        "N204B": {
          "name": "N204B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 37,
            "win_months_all": 0.6065573770491803,
            "win_months_active": 0.6065573770491803,
            "quarters_total": 19,
            "positive_quarters": 15,
            "win_quarters": 0.7894736842105263
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "win_quarters": 0.7619047619047619,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.039177614971507624
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.040580995764218475
          ],
          "daily_close_drawdown_pct": -9.284247101760801,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.06456741856734934,
              "SPY-USDT": -0.03704472643804317
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.06456741856734934,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.009909162333127218
            },
            "SPY-USDT": {
              "BTC-USDT": -0.03704472643804317,
              "PAXG-USDT": -0.009909162333127218,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03917120743685154,
            "2021-12-31 00:00:00+00:00": 0.18226255985092954,
            "2022-12-31 00:00:00+00:00": 0.08494277200116374,
            "2023-12-31 00:00:00+00:00": 0.15735921423311794,
            "2024-12-31 00:00:00+00:00": 0.13102442223929756,
            "2025-12-31 00:00:00+00:00": 0.08793270537370224
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "N204C": {
          "name": "N204C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 38,
            "win_months_all": 0.6229508196721312,
            "win_months_active": 0.6229508196721312,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 63,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6031746031746031,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.047444595864295835
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.04901335504001203
          ],
          "daily_close_drawdown_pct": -9.29660052880006,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.06479800663884741,
              "SPY-USDT": -0.028522694598703876
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.06479800663884741,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.058163460598454716
            },
            "SPY-USDT": {
              "BTC-USDT": -0.028522694598703876,
              "PAXG-USDT": 0.058163460598454716,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03836464211546797,
            "2021-12-31 00:00:00+00:00": 0.1606428666411599,
            "2022-12-31 00:00:00+00:00": 0.08723104746736565,
            "2023-12-31 00:00:00+00:00": 0.19334999293717647,
            "2024-12-31 00:00:00+00:00": 0.12429216776288565,
            "2025-12-31 00:00:00+00:00": 0.0802189450336841
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902B": {
          "name": "Y902B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 38,
            "win_months_all": 0.6229508196721312,
            "win_months_active": 0.6333333333333333,
            "quarters_total": 19,
            "positive_quarters": 15,
            "win_quarters": 0.7894736842105263
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6129032258064516,
          "win_quarters": 0.7619047619047619,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03909808977169993
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.0312089025654253
          ],
          "daily_close_drawdown_pct": -10.144603562492161,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.11042183773758557,
              "SPY-USDT": -0.05754639784646144
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.11042183773758557,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.009669708328863337
            },
            "SPY-USDT": {
              "BTC-USDT": -0.05754639784646144,
              "PAXG-USDT": -0.009669708328863337,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.036443900949128416,
            "2021-12-31 00:00:00+00:00": 0.1866295143281571,
            "2022-12-31 00:00:00+00:00": 0.10034391625772643,
            "2023-12-31 00:00:00+00:00": 0.1800886834754405,
            "2024-12-31 00:00:00+00:00": 0.12512350108974468,
            "2025-12-31 00:00:00+00:00": 0.08917615998801698
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "Y902C": {
          "name": "Y902C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.65,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6290322580645161,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.047586678082081835
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03976554950208122
          ],
          "daily_close_drawdown_pct": -10.153041319267441,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.11064020338315861,
              "SPY-USDT": -0.09713904185748701
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.11064020338315861,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.05880584220069957
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09713904185748701,
              "PAXG-USDT": 0.05880584220069957,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03550253450167484,
            "2021-12-31 00:00:00+00:00": 0.16556563266606883,
            "2022-12-31 00:00:00+00:00": 0.10261856446688156,
            "2023-12-31 00:00:00+00:00": 0.21737711308949392,
            "2024-12-31 00:00:00+00:00": 0.11847653396699953,
            "2025-12-31 00:00:00+00:00": 0.08202555415813517
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001B": {
          "name": "K1001B",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.65,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6290322580645161,
          "win_quarters": 0.8095238095238095,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03909808977169993
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.0312089025654253
          ],
          "daily_close_drawdown_pct": -9.286857227035073,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10725971083710116,
              "SPY-USDT": -0.05441863889540199
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10725971083710116,
              "PAXG-USDT": 1,
              "SPY-USDT": -0.00966811519804639
            },
            "SPY-USDT": {
              "BTC-USDT": -0.05441863889540199,
              "PAXG-USDT": -0.00966811519804639,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.036443900949128416,
            "2021-12-31 00:00:00+00:00": 0.18371629174482673,
            "2022-12-31 00:00:00+00:00": 0.10017858112159428,
            "2023-12-31 00:00:00+00:00": 0.180005102582234,
            "2024-12-31 00:00:00+00:00": 0.13544796161227102,
            "2025-12-31 00:00:00+00:00": 0.08919717207401479
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 0,
            "boundary_liquidations_reconciled": 0,
            "boundary_close_is_execution_liquidity_proof": false
          }
        },
        "K1001C": {
          "name": "K1001C",
          "method": "UTC day-close MTM from executed fills, right-edge inclusive",
          "partial_boundary_periods_included": true,
          "complete_periods": {
            "months_total": 61,
            "months_active": 60,
            "positive_months": 40,
            "win_months_all": 0.6557377049180327,
            "win_months_active": 0.6666666666666666,
            "quarters_total": 19,
            "positive_quarters": 17,
            "win_quarters": 0.8947368421052632
          },
          "months_total": 63,
          "months_active": 62,
          "win_months_all": 0.6349206349206349,
          "win_months_active": 0.6451612903225806,
          "win_quarters": 0.8571428571428571,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.047586678082081835
          ],
          "worst_quarter": [
            "2021-06-30 00:00:00+00:00",
            -0.03976554950208122
          ],
          "daily_close_drawdown_pct": -9.28244889552733,
          "mtm_route_contribution_correlation": {
            "BTC-USDT": {
              "BTC-USDT": 1,
              "PAXG-USDT": -0.10718021550939845,
              "SPY-USDT": -0.09435957649064235
            },
            "PAXG-USDT": {
              "BTC-USDT": -0.10718021550939845,
              "PAXG-USDT": 1,
              "SPY-USDT": 0.05880714774953814
            },
            "SPY-USDT": {
              "BTC-USDT": -0.09435957649064235,
              "PAXG-USDT": 0.05880714774953814,
              "SPY-USDT": 1
            }
          },
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03550253450167484,
            "2021-12-31 00:00:00+00:00": 0.16265096408826318,
            "2022-12-31 00:00:00+00:00": 0.1025934170355769,
            "2023-12-31 00:00:00+00:00": 0.21745493314082354,
            "2024-12-31 00:00:00+00:00": 0.12997931169976074,
            "2025-12-31 00:00:00+00:00": 0.0822043067980962
          },
          "terminal_reconciles": true,
          "terminal_diagnostics": {
            "pretermination_open_counter": 1,
            "boundary_liquidations_reconciled": 1,
            "boundary_close_is_execution_liquidity_proof": false
          }
        }
      },
      "anchors": {
        "BTC-USDT": {
          "anchor_count": 69,
          "distinct_anchor_timestamps": 35,
          "scale": 1.1501999999999981,
          "max_relative_error": 1.3322676295501878e-15
        },
        "PAXG-USDT": {
          "anchor_count": 30,
          "distinct_anchor_timestamps": 15,
          "scale": 0.19228799999999985,
          "max_relative_error": 1.5543122344752192e-15
        },
        "SPY-USDT": {
          "anchor_count": 18,
          "distinct_anchor_timestamps": 16,
          "scale": 0.03484345999999994,
          "max_relative_error": 1.7763568394002505e-15
        }
      },
      "sessions": {
        "N204B": {
          "session_id": "9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
          "fee_per_side": 0.00095,
          "net": 8982.353704810404,
          "title": "MCP Backtest: BTC R9 N95B validation"
        },
        "N204C": {
          "session_id": "b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
          "fee_per_side": 0.00095,
          "net": 8990.183159887889,
          "title": "MCP Backtest: BTC R9 N95C validation"
        },
        "Y902B": {
          "session_id": "2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
          "fee_per_side": 0.00095,
          "net": 9570.519836457781,
          "title": "MCP Backtest: BTC R9 F95B validation"
        },
        "Y902C": {
          "session_id": "26f5560f-8db8-45f4-8203-1d0612658136",
          "fee_per_side": 0.00095,
          "net": 9606.619794398339,
          "title": "MCP Backtest: BTC R9 F95C validation"
        },
        "K1001B": {
          "session_id": "03ff99f8-aabc-400d-a570-13f77c1e8495",
          "fee_per_side": 0.00095,
          "net": 9697.641826632269,
          "title": "MCP Backtest: BTC R10 K195B validation"
        },
        "K1001C": {
          "session_id": "002a9700-0279-4a8f-a103-ddaab681878c",
          "fee_per_side": 0.00095,
          "net": 9762.803908226635,
          "title": "MCP Backtest: BTC R10 K195C validation"
        }
      },
      "limitations": "Reused development sample; descriptive conditional resampling, not probability of true edge, OOS, selection correction or replay of capital."
    }
  ],
  "mechanism_sample": "Only5entrieschangedperportfolioatnominalversusY902; fee/TP repeats are not new independent cases.",
  "decision": "Keep K1001 as a frozen research candidate, with favorable operational fee/TP diagnostics but strong incremental concentration in July2024 and unresolved statistical uncertainty. No deployment or claim of no overfit. K1005 separately retained, not own-fee validated.",
  "closed_2026": true
}
```


## Revisión final independiente y verificación de la tabla

Revisión independiente R10:199comprobaciones PASS, guardadas en BTC_R10_K1001_INDEPENDENT_FINAL_REVIEW_20261019.md. Verificó comparadores fee/TP,8filas/24snapshots/46fuentes y metadatos. La puerta mensual65% NOera requisito de aceptación bajo fees elevados enR10; no se afirma que la regularidad mensual se mantenga intacta con todos los costes. Las tablas publican calendarios y activos para cada caso. Esta revisión comprueba consistencia técnica y de interpretación, no ausencia de sobreajuste.

La consolidación de94sesiones pasó la comparación deconteo,neto,drawdown,Sharpe,CAGR,fees ybalances con los resúmenes originales, dentro1e-7. Cada motor aporta45campos y cada auditor terminal está conciliado. Hay49resúmenes con contadorrawopen distinto de0; son campos históricos/preterminales delmotor y no se usaron para inventar posiciones residuales. Ver BTC_TODAY_METRICS_TRANSCRIPTION_CHECKS_20261019.md.
