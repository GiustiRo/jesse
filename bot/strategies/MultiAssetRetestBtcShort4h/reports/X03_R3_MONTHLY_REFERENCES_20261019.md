# X03 R3 — diagnóstico mensual final

2026 cerrado. Desarrollo2020-10-15→2025-12-31exclusivo. MTM UTC diario,61meses completos y63con fronteras. Los tres niveles se separan sin cambiar los objetivos65%/80%:
1. Bruto aritmético fijo = MTM neto del mes + comisiones ejecutadas en ese mes.
2. Neto base = resultado después de la comisión propia de esa run (.00045 o.00070lado).
3. Neto overlay = base menos otros5/10bpsRT sobre turnover de fills fijos.

El bruto conserva cantidades y decisiones inducidas por la comisión; no equivale a una reejecución sin costes ni a alpha de precio puro. Los fills a midnight se asignan al borde derecho inclusivo anterior. Todas las rutas concilian el neto terminal.

Con comisión elevada y gestión original, N204 tiene20meses brutos negativos y43brutos positivos en ambas carteras. Cuatro positivos brutos pasan a negativos al cobrar la comisión propia: quedan39/63positivos. Al añadir OTROS5bpsRT, pasan a no positivos otros dos B y uno C. La fricción determina varios cruces relevantes para la meta65%, pero no explica los20meses ya brutos negativos. No llamar a los24negativos netos “pérdidas de precio antes de toda comisión”.

Los cuatro meses absorbidos por la comisión propia son:
- B:2023-11,2024-07,2025-01,2025-07.
- C:2020-11,2024-07,2025-01,2025-07.

En nominal, N204 mantiene el número de meses positivos de X03: rescata2022-06y2023-08, pero pierde2022-08y2025-04. Su neto mejora, mientras la suma monetaria de meses negativos empeora. Además, los positivos brutos fijos bajan44→43. No atribuir mejor rentabilidad a una mejora general de frecuencia mensual.

| Sesión | Positivos brutos fijos | Negativos brutos fijos | Positivos absorbidos por fee propio | Positivos netos base / +5 / +10 | Suma meses netos negativos USDT |
|---|---:|---:|---:|---|---:|
| [X03N_B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) | 44 | 19 | 3 | 41 / 40 / 37 | -3649.22 |
| [X03N_C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) | 44 | 19 | 2 | 42 / 40 / 38 | -3993.02 |
| [N204N_B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) | 43 | 20 | 2 | 41 / 41 / 38 | -4029.52 |
| [N204N_C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794) | 43 | 20 | 1 | 42 / 41 / 39 | -4383.96 |
| [X03S_B](http://localhost:9200/#/backtest/1277ad3f-21b3-41d7-9c04-9485dec1f907) | 44 | 19 | 6 | 38 / 36 / 35 | -3808.01 |
| [X03S_C](http://localhost:9200/#/backtest/24e0fc97-92d3-4b55-8c19-afc149e9f993) | 44 | 19 | 6 | 38 / 37 / 35 | -4110.03 |
| [N204S_B](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f) | 43 | 20 | 4 | 39 / 37 / 36 | -4154.08 |
| [N204S_C](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960) | 43 | 20 | 4 | 39 / 38 / 36 | -4456.59 |

Las categorías primarias siguen disjuntas y sin redondear: base<0,base=0,0<base<=coste+5,coste+5<base<=coste+10,base>coste+10. El presupuesto propio de cada mes evita un umbral arbitrario de “ganancia pequeña”. Con turnover cero puede existir MTM de una posición abierta; el coste de equilibrio por turnover se deja sin estimar.

Se conservaron los primeros análisis REF_NOM/REF_STRESS. Las ampliaciones REF_NOM_GROSS/REF_STRESS_GROSS sólo añaden la identidad de bruto y fee propio, manteniendo matrices, reglas, umbrales y resultados base. Los resúmenes siguientes incluyen61y63meses, todas las pérdidas y los meses que cambian de signo. Las504filas de salida (8sesiones×63) no son observaciones independientes: comparten mercados, fechas y BTC.

## Resúmenes exactos
```json
{
  "sessions": {
    "X03N_B": {
      "fee_engine_per_side": 0.00045,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 12807.674667223238,
          "mean_month_USDT": 209.96187979054488,
          "median_month_USDT": 86.6316993171622,
          "sum_positive_months": 15613.457263093216,
          "sum_negative_months": -2805.7825958699777,
          "worst_month": "2021-04",
          "worst_month_USDT": -439.95609088365563,
          "best3_share_positive_mtm": 0.25402465668376517,
          "class_counts": {
            "loss_base": 20,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 3,
            "positive_above_cost10": 37
          },
          "positive_months": 41,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 17,
            "zero_months": 0,
            "net_before_actual_fees": 14622.68272208839,
            "fee_total": 1815.0080548651536,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 0.498972904679853,
                "fee": 34.124166012192894,
                "net": -33.62519310751304
              },
              {
                "month": "2023-11",
                "gross": 24.059232570957903,
                "fee": 36.68244713327593,
                "net": -12.623214562318026
              },
              {
                "month": "2024-07",
                "gross": 16.880309801084145,
                "fee": 59.5315732718529,
                "net": -42.651263470768754
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 3,
            "BTC-USDT__SPY-USDT": 0,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 40,
              "extra_cost": 1008.3378082584189,
              "flip_months": [
                {
                  "month": "2025-09",
                  "base": 28.29424791598649,
                  "extra": 38.54783155561936,
                  "after": -10.253583639634599
                }
              ],
              "already_negative_months": 20,
              "already_negative_base_sum": -2805.7825958699777,
              "already_negative_after_sum": -3084.4542664913624
            },
            "10": {
              "positive_months": 37,
              "extra_cost": 2016.6756165168379,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 13.2448703715163,
                  "extra": 15.322029364651105,
                  "after": -2.0771589931355265
                },
                {
                  "month": "2023-03",
                  "base": 13.858301862945154,
                  "extra": 22.53914631700162,
                  "after": -8.68084445405293
                },
                {
                  "month": "2025-07",
                  "base": 62.2998334448348,
                  "extra": 94.97461891309726,
                  "after": -32.67478546826169
                },
                {
                  "month": "2025-09",
                  "base": 28.29424791598649,
                  "extra": 77.09566311123872,
                  "after": -48.80141519525205
                }
              ],
              "already_negative_months": 20,
              "already_negative_base_sum": -2805.7825958699777,
              "already_negative_after_sum": -3363.1259371127526
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 11964.238131473845,
          "mean_month_USDT": 189.9085417694261,
          "median_month_USDT": 71.6696908160593,
          "sum_positive_months": 15613.457263093216,
          "sum_negative_months": -3649.219131619371,
          "worst_month": "2025-12",
          "worst_month_USDT": -652.5452055298738,
          "best3_share_positive_mtm": 0.25402465668376517,
          "class_counts": {
            "loss_base": 22,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 3,
            "positive_above_cost10": 37
          },
          "positive_months": 41,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 19,
            "zero_months": 0,
            "net_before_actual_fees": 13841.741861511964,
            "fee_total": 1877.5037300381193,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 0.498972904679853,
                "fee": 34.124166012192894,
                "net": -33.62519310751304
              },
              {
                "month": "2023-11",
                "gross": 24.059232570957903,
                "fee": 36.68244713327593,
                "net": -12.623214562318026
              },
              {
                "month": "2024-07",
                "gross": 16.880309801084145,
                "fee": 59.5315732718529,
                "net": -42.651263470768754
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 0,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 40,
              "extra_cost": 1043.0576277989555,
              "flip_months": [
                {
                  "month": "2025-09",
                  "base": 28.29424791598649,
                  "extra": 38.54783155561936,
                  "after": -10.253583639634599
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3649.219131619371,
              "already_negative_after_sum": -3962.6106217812885
            },
            "10": {
              "positive_months": 37,
              "extra_cost": 2086.115255597911,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 13.2448703715163,
                  "extra": 15.322029364651105,
                  "after": -2.0771589931355265
                },
                {
                  "month": "2023-03",
                  "base": 13.858301862945154,
                  "extra": 22.53914631700162,
                  "after": -8.68084445405293
                },
                {
                  "month": "2025-07",
                  "base": 62.2998334448348,
                  "extra": 94.97461891309726,
                  "after": -32.67478546826169
                },
                {
                  "month": "2025-09",
                  "base": 28.29424791598649,
                  "extra": 77.09566311123872,
                  "after": -48.80141519525205
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3649.219131619371,
              "already_negative_after_sum": -4276.00211194322
            }
          }
        }
      }
    },
    "X03N_C": {
      "fee_engine_per_side": 0.00045,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 13127.099099269251,
          "mean_month_USDT": 215.19834588965986,
          "median_month_USDT": 103.69791230040028,
          "sum_positive_months": 16128.895764676554,
          "sum_negative_months": -3001.7966654073025,
          "worst_month": "2021-04",
          "worst_month_USDT": -527.8092918106595,
          "best3_share_positive_mtm": 0.24620329966651672,
          "class_counts": {
            "loss_base": 19,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 38
          },
          "positive_months": 42,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 17,
            "zero_months": 0,
            "net_before_actual_fees": 15012.725916701878,
            "fee_total": 1885.6268174326253,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 0.42729481908455114,
                "fee": 33.23541982733141,
                "net": -32.80812500824686
              },
              {
                "month": "2024-07",
                "gross": 16.35024387827921,
                "fee": 60.64972836673892,
                "net": -44.29948448845971
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 3,
            "BTC-USDT__SPY-USDT": 2,
            "PAXG-USDT__SPY-USDT": 2
          },
          "stress": {
            "5": {
              "positive_months": 40,
              "extra_cost": 1047.5704541292369,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 7.663043166025551,
                  "after": -3.259906665171002
                },
                {
                  "month": "2025-09",
                  "base": 29.7825797601472,
                  "extra": 39.13493485052834,
                  "after": -9.352355090384663
                }
              ],
              "already_negative_months": 19,
              "already_negative_base_sum": -3001.7966654073025,
              "already_negative_after_sum": -3271.7746164083183
            },
            "10": {
              "positive_months": 38,
              "extra_cost": 2095.1409082584737,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 15.326086332051101,
                  "after": -10.922949831196092
                },
                {
                  "month": "2023-03",
                  "base": 13.61998762496114,
                  "extra": 22.160580833496283,
                  "after": -8.54059320853412
                },
                {
                  "month": "2025-07",
                  "base": 63.64757267807363,
                  "extra": 96.26395842948037,
                  "after": -32.61638575140387
                },
                {
                  "month": "2025-09",
                  "base": 29.7825797601472,
                  "extra": 78.26986970105668,
                  "after": -48.48728994090925
                }
              ],
              "already_negative_months": 19,
              "already_negative_base_sum": -3001.7966654073025,
              "already_negative_after_sum": -3541.7525674093213
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 12135.876833976647,
          "mean_month_USDT": 192.63296561867693,
          "median_month_USDT": 71.41557964976164,
          "sum_positive_months": 16128.895764676554,
          "sum_negative_months": -3993.0189306999073,
          "worst_month": "2025-12",
          "worst_month_USDT": -800.3309350730851,
          "best3_share_positive_mtm": 0.24620329966651672,
          "class_counts": {
            "loss_base": 21,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 38
          },
          "positive_months": 42,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 19,
            "zero_months": 0,
            "net_before_actual_fees": 14110.355162711856,
            "fee_total": 1974.478328735205,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 0.42729481908455114,
                "fee": 33.23541982733141,
                "net": -32.80812500824686
              },
              {
                "month": "2024-07",
                "gross": 16.35024387827921,
                "fee": 60.64972836673892,
                "net": -44.29948448845971
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 3,
            "PAXG-USDT__SPY-USDT": 3
          },
          "stress": {
            "5": {
              "positive_months": 40,
              "extra_cost": 1096.9324048528922,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 7.663043166025551,
                  "after": -3.259906665171002
                },
                {
                  "month": "2025-09",
                  "base": 29.7825797601472,
                  "extra": 39.13493485052834,
                  "after": -9.352355090384663
                }
              ],
              "already_negative_months": 21,
              "already_negative_base_sum": -3993.0189306999073,
              "already_negative_after_sum": -4312.3588324245775
            },
            "10": {
              "positive_months": 38,
              "extra_cost": 2193.8648097057844,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 15.326086332051101,
                  "after": -10.922949831196092
                },
                {
                  "month": "2023-03",
                  "base": 13.61998762496114,
                  "extra": 22.160580833496283,
                  "after": -8.54059320853412
                },
                {
                  "month": "2025-07",
                  "base": 63.64757267807363,
                  "extra": 96.26395842948037,
                  "after": -32.61638575140387
                },
                {
                  "month": "2025-09",
                  "base": 29.7825797601472,
                  "extra": 78.26986970105668,
                  "after": -48.48728994090925
                }
              ],
              "already_negative_months": 21,
              "already_negative_base_sum": -3993.0189306999073,
              "already_negative_after_sum": -4631.698734149237
            }
          }
        }
      }
    },
    "N204N_B": {
      "fee_engine_per_side": 0.00045,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 13933.73364004092,
          "mean_month_USDT": 228.4218629514905,
          "median_month_USDT": 121.92033358681874,
          "sum_positive_months": 17086.134072517405,
          "sum_negative_months": -3152.400432476483,
          "worst_month": "2021-04",
          "worst_month_USDT": -442.16390420529206,
          "best3_share_positive_mtm": 0.262037027656764,
          "class_counts": {
            "loss_base": 20,
            "zero_base": 0,
            "positive_within_cost5": 0,
            "positive_between_cost5_cost10": 3,
            "positive_above_cost10": 38
          },
          "positive_months": 41,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 18,
            "zero_months": 0,
            "net_before_actual_fees": 15781.263772721062,
            "fee_total": 1847.5301326801448,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-11",
                "gross": 24.49123002367884,
                "fee": 37.74105009674855,
                "net": -13.249820073069714
              },
              {
                "month": "2024-07",
                "gross": 17.2997066907472,
                "fee": 61.202017253569295,
                "net": -43.902310562822095
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 3,
            "BTC-USDT__SPY-USDT": 1,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 41,
              "extra_cost": 1026.4056292667467,
              "flip_months": [],
              "already_negative_months": 20,
              "already_negative_base_sum": -3152.400432476483,
              "already_negative_after_sum": -3449.9353589002403
            },
            "10": {
              "positive_months": 38,
              "extra_cost": 2052.8112585334934,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 13.2448703715163,
                  "extra": 15.322029364651105,
                  "after": -2.0771589931355265
                },
                {
                  "month": "2023-03",
                  "base": 14.939004388501417,
                  "extra": 23.17821860165033,
                  "after": -8.239214213148443
                },
                {
                  "month": "2025-07",
                  "base": 64.56481556220388,
                  "extra": 98.86817466851848,
                  "after": -34.30335910631766
                }
              ],
              "already_negative_months": 20,
              "already_negative_base_sum": -3152.400432476483,
              "already_negative_after_sum": -3747.4702853240033
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 13056.614915077651,
          "mean_month_USDT": 207.24785579488335,
          "median_month_USDT": 120.87705794912108,
          "sum_positive_months": 17086.134072517405,
          "sum_negative_months": -4029.5191574397522,
          "worst_month": "2025-12",
          "worst_month_USDT": -686.2273947437498,
          "best3_share_positive_mtm": 0.262037027656764,
          "class_counts": {
            "loss_base": 22,
            "zero_base": 0,
            "positive_within_cost5": 0,
            "positive_between_cost5_cost10": 3,
            "positive_above_cost10": 38
          },
          "positive_months": 41,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 20,
            "zero_months": 0,
            "net_before_actual_fees": 14969.479569456267,
            "fee_total": 1912.8646543786206,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-11",
                "gross": 24.49123002367884,
                "fee": 37.74105009674855,
                "net": -13.249820073069714
              },
              {
                "month": "2024-07",
                "gross": 17.2997066907472,
                "fee": 61.202017253569295,
                "net": -43.902310562822095
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 1,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 41,
              "extra_cost": 1062.7025857659,
              "flip_months": [],
              "already_negative_months": 22,
              "already_negative_base_sum": -4029.5191574397522,
              "already_negative_after_sum": -4363.35104036265
            },
            "10": {
              "positive_months": 38,
              "extra_cost": 2125.4051715318,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 13.2448703715163,
                  "extra": 15.322029364651105,
                  "after": -2.0771589931355265
                },
                {
                  "month": "2023-03",
                  "base": 14.939004388501417,
                  "extra": 23.17821860165033,
                  "after": -8.239214213148443
                },
                {
                  "month": "2025-07",
                  "base": 64.56481556220388,
                  "extra": 98.86817466851848,
                  "after": -34.30335910631766
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -4029.5191574397522,
              "already_negative_after_sum": -4697.182923285569
            }
          }
        }
      }
    },
    "N204N_C": {
      "fee_engine_per_side": 0.00045,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 14271.632445789683,
          "mean_month_USDT": 233.96118763589644,
          "median_month_USDT": 117.97775767288476,
          "sum_positive_months": 17623.398758617495,
          "sum_negative_months": -3351.7663128278127,
          "worst_month": "2021-04",
          "worst_month_USDT": -535.731854244912,
          "best3_share_positive_mtm": 0.2517075352412049,
          "class_counts": {
            "loss_base": 19,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 39
          },
          "positive_months": 42,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 18,
            "zero_months": 0,
            "net_before_actual_fees": 16191.05516375506,
            "fee_total": 1919.4227179653772,
            "fee_absorbed_positive_months": [
              {
                "month": "2024-07",
                "gross": 18.094170407644604,
                "fee": 62.27876003033966,
                "net": -44.18458962269506
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 3,
            "BTC-USDT__SPY-USDT": 3,
            "PAXG-USDT__SPY-USDT": 2
          },
          "stress": {
            "5": {
              "positive_months": 41,
              "extra_cost": 1066.3459544252096,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 7.663043166025551,
                  "after": -3.259906665171002
                }
              ],
              "already_negative_months": 19,
              "already_negative_base_sum": -3351.7663128278127,
              "already_negative_after_sum": -3640.9210912642593
            },
            "10": {
              "positive_months": 39,
              "extra_cost": 2132.691908850419,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 15.326086332051101,
                  "after": -10.922949831196092
                },
                {
                  "month": "2023-03",
                  "base": 14.784095545142918,
                  "extra": 22.791599596757678,
                  "after": -8.007504051618525
                },
                {
                  "month": "2025-07",
                  "base": 64.9006060700558,
                  "extra": 100.28060771244697,
                  "after": -35.38000164238838
                }
              ],
              "already_negative_months": 19,
              "already_negative_base_sum": -3351.7663128278127,
              "already_negative_after_sum": -3930.0758697007095
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 13239.442379846794,
          "mean_month_USDT": 210.14987904518722,
          "median_month_USDT": 107.68933411272155,
          "sum_positive_months": 17623.398758617495,
          "sum_negative_months": -4383.956378770701,
          "worst_month": "2025-12",
          "worst_month_USDT": -841.2987357233687,
          "best3_share_positive_mtm": 0.2517075352412049,
          "class_counts": {
            "loss_base": 21,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 39
          },
          "positive_months": 42,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 20,
            "zero_months": 0,
            "net_before_actual_fees": 15251.866603766563,
            "fee_total": 2012.4242239197672,
            "fee_absorbed_positive_months": [
              {
                "month": "2024-07",
                "gross": 18.094170407644604,
                "fee": 62.27876003033966,
                "net": -44.18458962269506
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 4,
            "PAXG-USDT__SPY-USDT": 3
          },
          "stress": {
            "5": {
              "positive_months": 41,
              "extra_cost": 1118.0134577332042,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 7.663043166025551,
                  "after": -3.259906665171002
                }
              ],
              "already_negative_months": 21,
              "already_negative_base_sum": -4383.956378770701,
              "already_negative_after_sum": -4724.778660515143
            },
            "10": {
              "positive_months": 39,
              "extra_cost": 2236.0269154664084,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 4.403136500855908,
                  "extra": 15.326086332051101,
                  "after": -10.922949831196092
                },
                {
                  "month": "2023-03",
                  "base": 14.784095545142918,
                  "extra": 22.791599596757678,
                  "after": -8.007504051618525
                },
                {
                  "month": "2025-07",
                  "base": 64.9006060700558,
                  "extra": 100.28060771244697,
                  "after": -35.38000164238838
                }
              ],
              "already_negative_months": 21,
              "already_negative_base_sum": -4383.956378770701,
              "already_negative_after_sum": -5065.600942259587
            }
          }
        }
      }
    },
    "X03S_B": {
      "fee_engine_per_side": 0.0007,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 10120.640721982367,
          "mean_month_USDT": 165.9121429833175,
          "median_month_USDT": 65.59128733454418,
          "sum_positive_months": 13152.160424841519,
          "sum_negative_months": -3031.519702859152,
          "worst_month": "2021-04",
          "worst_month_USDT": -441.0139329197209,
          "best3_share_positive_mtm": 0.2809772717867331,
          "class_counts": {
            "loss_base": 23,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 1,
            "positive_above_cost10": 35
          },
          "positive_months": 38,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 17,
            "zero_months": 0,
            "net_before_actual_fees": 12731.192982072282,
            "fee_total": 2610.552260089917,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 1.1818525125504777,
                "fee": 49.15220054324121,
                "net": -47.97034803069073
              },
              {
                "month": "2023-11",
                "gross": 16.121910758828328,
                "fee": 54.16942365188219,
                "net": -38.04751289305386
              },
              {
                "month": "2024-07",
                "gross": 3.153678611336673,
                "fee": 84.45760868858919,
                "net": -81.30393007725252
              },
              {
                "month": "2025-01",
                "gross": 41.16252158754972,
                "fee": 83.44651162335097,
                "net": -42.28399003580125
              },
              {
                "month": "2025-07",
                "gross": 101.68088343286733,
                "fee": 116.00293033196219,
                "net": -14.322046899094858
              },
              {
                "month": "2025-09",
                "gross": 74.41906735699438,
                "fee": 93.10489847638807,
                "net": -18.685831119393697
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 0,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 36,
              "extra_cost": 932.3400928892565,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 7.5512853297571345,
                  "after": -3.7371985477020644
                },
                {
                  "month": "2023-03",
                  "base": 5.949442052493396,
                  "extra": 10.568659485878683,
                  "after": -4.619217433382801
                }
              ],
              "already_negative_months": 23,
              "already_negative_base_sum": -3031.519702859152,
              "already_negative_after_sum": -3397.6123160993757
            },
            "10": {
              "positive_months": 35,
              "extra_cost": 1864.680185778513,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 15.102570659514269,
                  "after": -11.288483877460749
                },
                {
                  "month": "2023-03",
                  "base": 5.949442052493396,
                  "extra": 21.137318971757367,
                  "after": -15.187876919262635
                },
                {
                  "month": "2025-11",
                  "base": 19.524011652745685,
                  "extra": 19.793741159638124,
                  "after": -0.2697295068974199
                }
              ],
              "already_negative_months": 23,
              "already_negative_base_sum": -3031.519702859152,
              "already_negative_after_sum": -3763.704929339616
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 9344.147577013511,
          "mean_month_USDT": 148.31980280973826,
          "median_month_USDT": 53.78174846000002,
          "sum_positive_months": 13152.160424841519,
          "sum_negative_months": -3808.0128478280076,
          "worst_month": "2025-12",
          "worst_month_USDT": -585.2661889760457,
          "best3_share_positive_mtm": 0.2809772717867331,
          "class_counts": {
            "loss_base": 25,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 1,
            "positive_above_cost10": 35
          },
          "positive_months": 38,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 19,
            "zero_months": 0,
            "net_before_actual_fees": 12038.850036585925,
            "fee_total": 2694.7024595724147,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-08",
                "gross": 1.1818525125504777,
                "fee": 49.15220054324121,
                "net": -47.97034803069073
              },
              {
                "month": "2023-11",
                "gross": 16.121910758828328,
                "fee": 54.16942365188219,
                "net": -38.04751289305386
              },
              {
                "month": "2024-07",
                "gross": 3.153678611336673,
                "fee": 84.45760868858919,
                "net": -81.30393007725252
              },
              {
                "month": "2025-01",
                "gross": 41.16252158754972,
                "fee": 83.44651162335097,
                "net": -42.28399003580125
              },
              {
                "month": "2025-07",
                "gross": 101.68088343286733,
                "fee": 116.00293033196219,
                "net": -14.322046899094858
              },
              {
                "month": "2025-09",
                "gross": 74.41906735699438,
                "fee": 93.10489847638807,
                "net": -18.685831119393697
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 5,
            "BTC-USDT__SPY-USDT": 0,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 36,
              "extra_cost": 962.393735561577,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 7.5512853297571345,
                  "after": -3.7371985477020644
                },
                {
                  "month": "2023-03",
                  "base": 5.949442052493396,
                  "extra": 10.568659485878683,
                  "after": -4.619217433382801
                }
              ],
              "already_negative_months": 25,
              "already_negative_base_sum": -3808.0128478280076,
              "already_negative_after_sum": -4204.159103740547
            },
            "10": {
              "positive_months": 35,
              "extra_cost": 1924.787471123154,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 15.102570659514269,
                  "after": -11.288483877460749
                },
                {
                  "month": "2023-03",
                  "base": 5.949442052493396,
                  "extra": 21.137318971757367,
                  "after": -15.187876919262635
                },
                {
                  "month": "2025-11",
                  "base": 19.524011652745685,
                  "extra": 19.793741159638124,
                  "after": -0.2697295068974199
                }
              ],
              "already_negative_months": 25,
              "already_negative_base_sum": -3808.0128478280076,
              "already_negative_after_sum": -4600.305359653108
            }
          }
        }
      }
    },
    "X03S_C": {
      "fee_engine_per_side": 0.0007,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 10330.53841176333,
          "mean_month_USDT": 169.35308871743163,
          "median_month_USDT": 64.67794597272405,
          "sum_positive_months": 13530.901924263044,
          "sum_negative_months": -3200.3635124997145,
          "worst_month": "2021-04",
          "worst_month_USDT": -531.4561846383112,
          "best3_share_positive_mtm": 0.2637508515969742,
          "class_counts": {
            "loss_base": 23,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 35
          },
          "positive_months": 38,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 17,
            "zero_months": 0,
            "net_before_actual_fees": 13035.658233500806,
            "fee_total": 2705.119821737475,
            "fee_absorbed_positive_months": [
              {
                "month": "2020-11",
                "gross": 16.729229204772615,
                "fee": 21.1282214876804,
                "net": -4.398992282907784
              },
              {
                "month": "2023-08",
                "gross": 1.1580520932881342,
                "fee": 47.8788201835347,
                "net": -46.720768090246565
              },
              {
                "month": "2024-07",
                "gross": 2.5362559417134065,
                "fee": 85.70278529353332,
                "net": -83.16652935181992
              },
              {
                "month": "2025-01",
                "gross": 40.856091812225316,
                "fee": 84.48174290076128,
                "net": -43.62565108853596
              },
              {
                "month": "2025-07",
                "gross": 105.63223680055859,
                "fee": 116.84770406755894,
                "net": -11.21546726700035
              },
              {
                "month": "2025-09",
                "gross": 74.37840883950922,
                "fee": 93.97695642650216,
                "net": -19.598547586992936
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 2,
            "PAXG-USDT__SPY-USDT": 2
          },
          "stress": {
            "5": {
              "positive_months": 37,
              "extra_cost": 966.1142220490982,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 5.7255462456287205,
                  "extra": 10.387430265513327,
                  "after": -4.661884019884383
                }
              ],
              "already_negative_months": 23,
              "already_negative_base_sum": -3200.3635124997145,
              "already_negative_after_sum": -3566.3191032316336
            },
            "10": {
              "positive_months": 35,
              "extra_cost": 1932.2284440981964,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 5.7255462456287205,
                  "extra": 20.774860531026654,
                  "after": -15.049314285397486
                },
                {
                  "month": "2024-08",
                  "base": 38.4765326613433,
                  "extra": 41.63926785537235,
                  "after": -3.162735194029665
                },
                {
                  "month": "2025-11",
                  "base": 19.727672856111894,
                  "extra": 20.001901203270346,
                  "after": -0.27422834715616773
                }
              ],
              "already_negative_months": 23,
              "already_negative_base_sum": -3200.3635124997145,
              "already_negative_after_sum": -3932.2746939635745
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 9420.86700257421,
          "mean_month_USDT": 149.53757146943192,
          "median_month_USDT": 52.95726771151385,
          "sum_positive_months": 13530.901924263044,
          "sum_negative_months": -4110.0349216888335,
          "worst_month": "2025-12",
          "worst_month_USDT": -718.444453196309,
          "best3_share_positive_mtm": 0.2637508515969742,
          "class_counts": {
            "loss_base": 25,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 35
          },
          "positive_months": 38,
          "gross_fixed_path": {
            "positive_months": 44,
            "negative_months": 19,
            "zero_months": 0,
            "net_before_actual_fees": 12243.822061228417,
            "fee_total": 2822.9550586542045,
            "fee_absorbed_positive_months": [
              {
                "month": "2020-11",
                "gross": 16.729229204772615,
                "fee": 21.1282214876804,
                "net": -4.398992282907784
              },
              {
                "month": "2023-08",
                "gross": 1.1580520932881342,
                "fee": 47.8788201835347,
                "net": -46.720768090246565
              },
              {
                "month": "2024-07",
                "gross": 2.5362559417134065,
                "fee": 85.70278529353332,
                "net": -83.16652935181992
              },
              {
                "month": "2025-01",
                "gross": 40.856091812225316,
                "fee": 84.48174290076128,
                "net": -43.62565108853596
              },
              {
                "month": "2025-07",
                "gross": 105.63223680055859,
                "fee": 116.84770406755894,
                "net": -11.21546726700035
              },
              {
                "month": "2025-09",
                "gross": 74.37840883950922,
                "fee": 93.97695642650216,
                "net": -19.598547586992936
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 5,
            "BTC-USDT__SPY-USDT": 3,
            "PAXG-USDT__SPY-USDT": 3
          },
          "stress": {
            "5": {
              "positive_months": 37,
              "extra_cost": 1008.1982352336446,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 5.7255462456287205,
                  "extra": 10.387430265513327,
                  "after": -4.661884019884383
                }
              ],
              "already_negative_months": 25,
              "already_negative_base_sum": -4110.0349216888335,
              "already_negative_after_sum": -4518.0745256053
            },
            "10": {
              "positive_months": 35,
              "extra_cost": 2016.3964704672892,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 5.7255462456287205,
                  "extra": 20.774860531026654,
                  "after": -15.049314285397486
                },
                {
                  "month": "2024-08",
                  "base": 38.4765326613433,
                  "extra": 41.63926785537235,
                  "after": -3.162735194029665
                },
                {
                  "month": "2025-11",
                  "base": 19.727672856111894,
                  "extra": 20.001901203270346,
                  "after": -0.27422834715616773
                }
              ],
              "already_negative_months": 25,
              "already_negative_base_sum": -4110.0349216888335,
              "already_negative_after_sum": -4926.114129521789
            }
          }
        }
      }
    },
    "N204S_B": {
      "fee_engine_per_side": 0.0007,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 11071.711833302797,
          "mean_month_USDT": 181.50347267709503,
          "median_month_USDT": 100.96146950946422,
          "sum_positive_months": 14421.394842716363,
          "sum_negative_months": -3349.6830094135657,
          "worst_month": "2021-04",
          "worst_month_USDT": -445.47930970248126,
          "best3_share_positive_mtm": 0.28914186684103627,
          "class_counts": {
            "loss_base": 22,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 1,
            "positive_above_cost10": 36
          },
          "positive_months": 39,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 18,
            "zero_months": 0,
            "net_before_actual_fees": 13724.054406731108,
            "fee_total": 2652.3425734283137,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-11",
                "gross": 17.176187851565956,
                "fee": 55.61630460125674,
                "net": -38.44011674969079
              },
              {
                "month": "2024-07",
                "gross": 3.3618287716446247,
                "fee": 86.56097869107104,
                "net": -83.19914991942642
              },
              {
                "month": "2025-01",
                "gross": 39.22003773922478,
                "fee": 87.59192154295596,
                "net": -48.37188380373118
              },
              {
                "month": "2025-07",
                "gross": 105.98434373720455,
                "fee": 120.30027403465728,
                "net": -14.315930297452724
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 1,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 37,
              "extra_cost": 947.2652047958264,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 7.5512853297571345,
                  "after": -3.7371985477020644
                },
                {
                  "month": "2023-03",
                  "base": 5.985234502499225,
                  "extra": 10.854322426989034,
                  "after": -4.869087924487758
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3349.6830094135657,
              "already_negative_after_sum": -3701.898029332584
            },
            "10": {
              "positive_months": 36,
              "extra_cost": 1894.5304095916529,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 15.102570659514269,
                  "after": -11.288483877460749
                },
                {
                  "month": "2023-03",
                  "base": 5.985234502499225,
                  "extra": 21.70864485397807,
                  "after": -15.72341035147474
                },
                {
                  "month": "2025-11",
                  "base": 20.455592572368914,
                  "extra": 20.737955647239254,
                  "after": -0.28236307486804435
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3349.6830094135657,
              "already_negative_after_sum": -4054.113049251604
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 10267.311379187311,
          "mean_month_USDT": 162.9731964950367,
          "median_month_USDT": 97.55541860999983,
          "sum_positive_months": 14421.394842716363,
          "sum_negative_months": -4154.083463529052,
          "worst_month": "2025-12",
          "worst_month_USDT": -613.1734981226764,
          "best3_share_positive_mtm": 0.28914186684103627,
          "class_counts": {
            "loss_base": 24,
            "zero_base": 0,
            "positive_within_cost5": 2,
            "positive_between_cost5_cost10": 1,
            "positive_above_cost10": 36
          },
          "positive_months": 39,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 20,
            "zero_months": 0,
            "net_before_actual_fees": 13007.318032983745,
            "fee_total": 2740.006653796435,
            "fee_absorbed_positive_months": [
              {
                "month": "2023-11",
                "gross": 17.176187851565956,
                "fee": 55.61630460125674,
                "net": -38.44011674969079
              },
              {
                "month": "2024-07",
                "gross": 3.3618287716446247,
                "fee": 86.56097869107104,
                "net": -83.19914991942642
              },
              {
                "month": "2025-01",
                "gross": 39.22003773922478,
                "fee": 87.59192154295596,
                "net": -48.37188380373118
              },
              {
                "month": "2025-07",
                "gross": 105.98434373720455,
                "fee": 120.30027403465728,
                "net": -14.315930297452724
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 5,
            "BTC-USDT__SPY-USDT": 1,
            "PAXG-USDT__SPY-USDT": 0
          },
          "stress": {
            "5": {
              "positive_months": 37,
              "extra_cost": 978.5738049272983,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 7.5512853297571345,
                  "after": -3.7371985477020644
                },
                {
                  "month": "2023-03",
                  "base": 5.985234502499225,
                  "extra": 10.854322426989034,
                  "after": -4.869087924487758
                }
              ],
              "already_negative_months": 24,
              "already_negative_base_sum": -4154.083463529052,
              "already_negative_after_sum": -4537.6070835795435
            },
            "10": {
              "positive_months": 36,
              "extra_cost": 1957.1476098545966,
              "flip_months": [
                {
                  "month": "2020-11",
                  "base": 3.814086782054801,
                  "extra": 15.102570659514269,
                  "after": -11.288483877460749
                },
                {
                  "month": "2023-03",
                  "base": 5.985234502499225,
                  "extra": 21.70864485397807,
                  "after": -15.72341035147474
                },
                {
                  "month": "2025-11",
                  "base": 20.455592572368914,
                  "extra": 20.737955647239254,
                  "after": -0.28236307486804435
                }
              ],
              "already_negative_months": 24,
              "already_negative_base_sum": -4154.083463529052,
              "already_negative_after_sum": -4921.130703630035
            }
          }
        }
      }
    },
    "N204S_C": {
      "fee_engine_per_side": 0.0007,
      "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
      "samples": {
        "full61": {
          "months": 61,
          "net_mtm": 11354.430075336684,
          "mean_month_USDT": 186.1381979563391,
          "median_month_USDT": 98.12091019376385,
          "sum_positive_months": 14865.529548222756,
          "sum_negative_months": -3511.0994728860715,
          "worst_month": "2021-04",
          "worst_month_USDT": -536.9502774176508,
          "best3_share_positive_mtm": 0.27369056878359765,
          "class_counts": {
            "loss_base": 22,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 36
          },
          "positive_months": 39,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 18,
            "zero_months": 0,
            "net_before_actual_fees": 14109.104813026246,
            "fee_total": 2754.674737689565,
            "fee_absorbed_positive_months": [
              {
                "month": "2020-11",
                "gross": 16.729229204772615,
                "fee": 21.1282214876804,
                "net": -4.398992282907784
              },
              {
                "month": "2024-07",
                "gross": 3.1801833836104976,
                "fee": 88.08393386428703,
                "net": -84.90375048067654
              },
              {
                "month": "2025-01",
                "gross": 42.42810060895755,
                "fee": 88.66051236521781,
                "net": -46.23241175626026
              },
              {
                "month": "2025-07",
                "gross": 111.03377869723289,
                "fee": 121.73731171965727,
                "net": -10.70353302242438
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 4,
            "BTC-USDT__SPY-USDT": 3,
            "PAXG-USDT__SPY-USDT": 2
          },
          "stress": {
            "5": {
              "positive_months": 38,
              "extra_cost": 983.812406317702,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 4.456319338087269,
                  "extra": 10.69440562047399,
                  "after": -6.2380862823883945
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3511.0994728860715,
              "already_negative_after_sum": -3863.5387748819594
            },
            "10": {
              "positive_months": 36,
              "extra_cost": 1967.624812635404,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 4.456319338087269,
                  "extra": 21.38881124094798,
                  "after": -16.93249190286224
                },
                {
                  "month": "2024-08",
                  "base": 32.848526737554494,
                  "extra": 44.20367054459383,
                  "after": -11.355143807038985
                },
                {
                  "month": "2025-11",
                  "base": 20.727732179690065,
                  "extra": 21.01897151515045,
                  "after": -0.29123933545997716
                }
              ],
              "already_negative_months": 22,
              "already_negative_base_sum": -3511.0994728860715,
              "already_negative_after_sum": -4215.978076877858
            }
          }
        },
        "included63": {
          "months": 63,
          "net_mtm": 10408.935273900952,
          "mean_month_USDT": 165.22119482382465,
          "median_month_USDT": 66.70557393565832,
          "sum_positive_months": 14865.529548222756,
          "sum_negative_months": -4456.594274321804,
          "worst_month": "2025-12",
          "worst_month_USDT": -754.2678454429224,
          "best3_share_positive_mtm": 0.27369056878359765,
          "class_counts": {
            "loss_base": 24,
            "zero_base": 0,
            "positive_within_cost5": 1,
            "positive_between_cost5_cost10": 2,
            "positive_above_cost10": 36
          },
          "positive_months": 39,
          "gross_fixed_path": {
            "positive_months": 43,
            "negative_months": 20,
            "zero_months": 0,
            "net_before_actual_fees": 13286.843019108419,
            "fee_total": 2877.9077452074694,
            "fee_absorbed_positive_months": [
              {
                "month": "2020-11",
                "gross": 16.729229204772615,
                "fee": 21.1282214876804,
                "net": -4.398992282907784
              },
              {
                "month": "2024-07",
                "gross": 3.1801833836104976,
                "fee": 88.08393386428703,
                "net": -84.90375048067654
              },
              {
                "month": "2025-01",
                "gross": 42.42810060895755,
                "fee": 88.66051236521781,
                "net": -46.23241175626026
              },
              {
                "month": "2025-07",
                "gross": 111.03377869723289,
                "fee": 121.73731171965727,
                "net": -10.70353302242438
              }
            ]
          },
          "co_loss_counts": {
            "BTC-USDT__PAXG-USDT": 5,
            "BTC-USDT__SPY-USDT": 4,
            "PAXG-USDT__SPY-USDT": 3
          },
          "stress": {
            "5": {
              "positive_months": 38,
              "extra_cost": 1027.8241947169536,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 4.456319338087269,
                  "extra": 10.69440562047399,
                  "after": -6.2380862823883945
                }
              ],
              "already_negative_months": 24,
              "already_negative_base_sum": -4456.594274321804,
              "already_negative_after_sum": -4853.045364716945
            },
            "10": {
              "positive_months": 36,
              "extra_cost": 2055.648389433907,
              "flip_months": [
                {
                  "month": "2023-03",
                  "base": 4.456319338087269,
                  "extra": 21.38881124094798,
                  "after": -16.93249190286224
                },
                {
                  "month": "2024-08",
                  "base": 32.848526737554494,
                  "extra": 44.20367054459383,
                  "after": -11.355143807038985
                },
                {
                  "month": "2025-11",
                  "base": 20.727732179690065,
                  "extra": 21.01897151515045,
                  "after": -0.29123933545997716
                }
              ],
              "already_negative_months": 24,
              "already_negative_base_sum": -4456.594274321804,
              "already_negative_after_sum": -5249.496455112096
            }
          }
        }
      }
    }
  },
  "paired_nominal": {
    "X03N_B__N204N_B": {
      "delta": 1092.376783603806,
      "months_improve": 37,
      "rescued_negative_to_positive": [
        "2022-06",
        "2023-08"
      ],
      "lost_positive_to_nonpositive": [
        "2022-08",
        "2025-04"
      ]
    },
    "X03N_C__N204N_C": {
      "delta": 1103.5655458701476,
      "months_improve": 40,
      "rescued_negative_to_positive": [
        "2022-06",
        "2023-08"
      ],
      "lost_positive_to_nonpositive": [
        "2022-08",
        "2025-04"
      ]
    }
  },
  "paired_stress": {
    "X03S_B__N204S_B": {
      "delta": 923.1638021737999,
      "months_improve": 37,
      "rescued_negative_to_positive": [
        "2022-06",
        "2023-08",
        "2025-09"
      ],
      "lost_positive_to_nonpositive": [
        "2022-08",
        "2025-04"
      ]
    },
    "X03S_C__N204S_C": {
      "delta": 988.0682713267415,
      "months_improve": 38,
      "rescued_negative_to_positive": [
        "2022-06",
        "2023-08",
        "2025-09"
      ],
      "lost_positive_to_nonpositive": [
        "2022-08",
        "2025-04"
      ]
    }
  }
}
```
