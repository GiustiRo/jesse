# BTC R9 — cierre final de investigación

R9 completada:20nuevosbacktests,20auditorías PASS y terminal reconciliado,60snapshots exactos y44fuentes históricas/nuevas preservadas exactas.10jobs financieros más3jobs incertidumbre y1descriptivoconcentración K1/K2.2026cerrado; desarrollo2020-10-15→2025-12-31exclusivo, no OOS.

## Y902

Diagnóstico operativo prefijado de comisiones y vecinos favorable. Ventaja N204 a igualfee: nominal+389.62/+440.91,fee.00070+526.64/+508.24,fee.00095+588.17/+616.44USDT. TP1.8Rqueda+27.97/+54.09,TP2.2R+296.03/+324.33sobreN204 nominal. No se elige mejor vecino;2R siguefijo. Rentabilidad absoluta cae confee,lascurvas/sizing/BEpuedencambiar,estos tests no representan slippage real ni liquidez.

Todos losIC95%primarios de diferencia media mensual conbootstrap circular6meses10000seed9022026incluyen0. Muestra61mesescompletos primaria y63incluidos secundaria; B/Ccorrelacionadas,indicessimulaciónidénticosentrefees. Ningún ajuste por todas las búsquedas previas. No prueba anti-sobreajuste ni promoción automática.

## Exploración K

K1001 mínimo conjunto:net13619.21/13854.33,+172.98/+173.98vsY902,DD−8.82/−8.78,42/63 y43/63meses positivos con+5overlay,frente41/63y42/63Y902. Sólo5entradascambiadas. Sinmejormes vsN204 incl+155.35/+216.43,full61−41.76/+21.57. Se retiene candidata positiva con pocos cambios; todavía sinvalidaciónpropia hastaR10autorizada posteriormente.

K1005 trailinghighprev tras cierre1R:net13844.91/14103.94,+398.67/+423.59vsY902,46suppfills y5salidas modificadas;24actualizacionesstop NOson24tradesdistintos. Sinmejormes vsN204 incl+376.79/+461.79,full+184.35/+273.70,4/5bloquesanualesincluidosfavorables. Mejor neto nominal entreKperoDD-9.7072/-9.6427%; noheredavalidaciónY902. Retener investigación, sin promoción.

K1002bufferbody:net10640.89/10831.16,sólo20suppfills;demasiadasoportunidadesperdidas. K1003primera4hadversa:10934.01/11124.49,23salidasgestión;K1004reclamoancla:12407.21/12654.85,11salidasgestión. Reducen neto; no retocados.

## Incidente y recuperación

MCP respondió noJSON en verificaciónfinal:todospararon. Recuperación autorizada por usuario; comprobados estados existentes sin duplicarbacktests. El mismatchsnapshot K1001 eraformatoclaves de Jesse (classname antes,exchange-symboldespués), contenido exacto enlas3rutas. No corrupción demostrada. Leerlistlimit2evitaenviartrades/equitycompletos para revisarfuentes. Se cerróK1005existente y auditoríaspendientes.

Después,usuarioautorizólimpieza conservadora:13workspacesR8terminados eliminados tras13archivospermanentes. Fuentes/sesiones/trades/velas/informes intactos;diariosCSV/figurasderivadasreproducibles. ManifiestoMCP_CLEANUP_TRACE_MANIFEST_20261019.md. Causalidadentretamaño yfallo noestablecida; máximosnuevos2backtests/1analysis,consultaspequeñas.

## Evidencia

- BTC_R9_FINAL_MANIFEST_20261019.md
- BTC_R9_RESULTS_MATRIX_20261019.md y10BTC_R9_AUDIT_<batch>...
- BTC_R9_UNCERTAINTY_RESULTS_20261019.md/códigoSOURCE
- BTC_R9_K_FAMILY_FINAL_RESULTS_20261019.md
- BTC_R9_INDEPENDENT_FINAL_REVIEW_20261019.md:339checksPASS
- Protocolo,addendumK,fuentesQA230/TP63,guardTPfísico registradoantesresultados.

## Evaluación completa

```json
{
  "cost_resilience_diagnostic_pass": true,
  "tp_neighbours_diagnostic_pass": true,
  "combined_operational_diagnostic_favorable": true,
  "definition": "Frozen R9 operational diagnostic, not statistical significance or promotion. TP neighbours never candidates.",
  "fees": [
    {
      "level": "F70",
      "rows": [
        {
          "portfolio": "B",
          "net": 10793.949438932308,
          "reference_net": 10267.311379187322,
          "delta": 526.6380597449861,
          "dd": -9.93268724082509,
          "BTC_delta": 460.5495175708111
        },
        {
          "portfolio": "C",
          "net": 10917.180154275862,
          "reference_net": 10408.935273900946,
          "delta": 508.24488037491574,
          "dd": -9.913586199276425,
          "BTC_delta": 413.7536553537775
        }
      ]
    },
    {
      "level": "F95",
      "rows": [
        {
          "portfolio": "B",
          "net": 9570.519836457781,
          "reference_net": 8982.353704810395,
          "delta": 588.1661316473856,
          "dd": -10.15422406719626,
          "BTC_delta": 525.7155239215072
        },
        {
          "portfolio": "C",
          "net": 9606.619794398342,
          "reference_net": 8990.183159887889,
          "delta": 616.4366345104536,
          "dd": -10.155985801505906,
          "BTC_delta": 524.8393622676213
        }
      ]
    }
  ],
  "neighbours": [
    {
      "level": "T18",
      "rows": [
        {
          "portfolio": "B",
          "net": 13084.58365842148,
          "delta_N204": 27.96874334381573,
          "delta_Y902": -361.65086715374673,
          "dd": -9.689827780952676
        },
        {
          "portfolio": "C",
          "net": 13293.527709995118,
          "delta_N204": 54.08533014832574,
          "delta_Y902": -386.8214608912658,
          "dd": -9.631263736672778
        }
      ]
    },
    {
      "level": "T22",
      "rows": [
        {
          "portfolio": "B",
          "net": 13352.641093027976,
          "delta_N204": 296.02617795031256,
          "delta_Y902": -93.5934325472499,
          "dd": -9.68491487224954
        },
        {
          "portfolio": "C",
          "net": 13563.774551598133,
          "delta_N204": 324.33217175134087,
          "delta_Y902": -116.57461928825069,
          "dd": -9.628355502758978
        }
      ]
    }
  ],
  "uncertainty": [
    {
      "level": "nominal",
      "primary_full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 3.0972497939606525,
            "observed_total_USDT": 188.9322374315998,
            "ci95_percentile_mean_USDT_month": [
              -18.461644962167256,
              27.300595334617128
            ],
            "fraction_bootstrap_means_gt_zero": 0.5884,
            "positive_delta_months": 27,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 409.38018865441336,
            "delta_omitting_best_month_arithmetic_USDT": -220.44795122281357,
            "year_delta_USDT": {
              "2020": -32.97982371443686,
              "2021": 21.225657331864568,
              "2022": 154.22912855232062,
              "2023": 287.4741597636712,
              "2024": -73.08507298060067,
              "2025": -167.93181152121906
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 221.91206114603665,
              "2021": 167.70658009973522,
              "2022": 34.70310887927917,
              "2023": -98.54192233207141,
              "2024": 262.01731041220046,
              "2025": 356.86404895281885
            }
          },
          "C": {
            "observed_mean_USDT_month": 3.9562404386252026,
            "observed_total_USDT": 241.33066675613736,
            "ci95_percentile_mean_USDT_month": [
              -17.530692280914852,
              27.64878181288945
            ],
            "fraction_bootstrap_means_gt_zero": 0.6215,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.58164502733234,
            "delta_omitting_best_month_arithmetic_USDT": -159.25097827119498,
            "year_delta_USDT": {
              "2020": -32.98046405748573,
              "2021": 25.93716357273661,
              "2022": 148.9034131719436,
              "2023": 315.30783956492087,
              "2024": -68.1329541064515,
              "2025": -147.7043313895265
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 274.3111308136231,
              "2021": 215.39350318340075,
              "2022": 92.42725358419375,
              "2023": -73.97717280878351,
              "2024": 309.46362086258887,
              "2025": 389.03499814566385
            }
          }
        }
      },
      "secondary_included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 6.184438261866273,
            "observed_total_USDT": 389.6196104975752,
            "ci95_percentile_mean_USDT_month": [
              -13.995597783500031,
              28.44962979271072
            ],
            "fraction_bootstrap_means_gt_zero": 0.7005,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 409.38018865441336,
            "delta_omitting_best_month_arithmetic_USDT": -19.760578156838164,
            "year_delta_USDT": {
              "2020": -32.97982371443686,
              "2021": 21.225657331864568,
              "2022": 154.22912855232062,
              "2023": 287.4741597636712,
              "2024": -73.08507298060067,
              "2025": 32.75556154475635
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 422.59943421201206,
              "2021": 368.3939531657106,
              "2022": 235.39048194525458,
              "2023": 102.145450733904,
              "2024": 462.70468347817587,
              "2025": 356.86404895281885
            }
          },
          "C": {
            "observed_mean_USDT_month": 6.998520492691958,
            "observed_total_USDT": 440.9067910395934,
            "ci95_percentile_mean_USDT_month": [
              -12.990043241773694,
              28.823737025734072
            ],
            "fraction_bootstrap_means_gt_zero": 0.7358,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.58164502733234,
            "delta_omitting_best_month_arithmetic_USDT": 40.32514601226103,
            "year_delta_USDT": {
              "2020": -32.98046405748573,
              "2021": 25.93716357273661,
              "2022": 148.9034131719436,
              "2023": 315.30783956492087,
              "2024": -68.1329541064515,
              "2025": 51.87179289392952
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 473.8872550970791,
              "2021": 414.96962746685676,
              "2022": 292.00337786764976,
              "2023": 125.5989514746725,
              "2024": 509.0397451460449,
              "2025": 389.03499814566385
            }
          }
        }
      }
    },
    {
      "level": "F70",
      "primary_full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 5.725115623867467,
            "observed_total_USDT": 349.23205305591546,
            "ci95_percentile_mean_USDT_month": [
              -14.473294331667992,
              28.580223225555887
            ],
            "fraction_bootstrap_means_gt_zero": 0.6861,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.0685127057204,
            "delta_omitting_best_month_arithmetic_USDT": -50.836459649804965,
            "year_delta_USDT": {
              "2020": -31.73123376250078,
              "2021": 45.660599801045464,
              "2022": 170.10405793982864,
              "2023": 313.8709212801805,
              "2024": -34.04164772965305,
              "2025": -114.6306444729853
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 380.96328681841624,
              "2021": 303.57145325487,
              "2022": 179.12799511608682,
              "2023": 35.361131775734975,
              "2024": 383.2737007855685,
              "2025": 463.86269752890075
            }
          },
          "C": {
            "observed_mean_USDT_month": 5.425626951898997,
            "observed_total_USDT": 330.9632440658388,
            "ci95_percentile_mean_USDT_month": [
              -14.861155680133633,
              27.894518808260994
            ],
            "fraction_bootstrap_means_gt_zero": 0.6777,
            "positive_delta_months": 28,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.7897367463156,
            "delta_omitting_best_month_arithmetic_USDT": -62.826492680476804,
            "year_delta_USDT": {
              "2020": -28.923563857602858,
              "2021": 26.12168760300301,
              "2022": 166.06137293689062,
              "2023": 335.2334431373256,
              "2024": -34.50926226997581,
              "2025": -133.02043348380175
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 359.88680792344167,
              "2021": 304.8415564628358,
              "2022": 164.9018711289482,
              "2023": -4.270199071486786,
              "2024": 365.4725063358146,
              "2025": 463.98367754964056
            }
          }
        }
      },
      "secondary_included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 8.35933428166662,
            "observed_total_USDT": 526.638059744997,
            "ci95_percentile_mean_USDT_month": [
              -10.772111865404026,
              29.440652708444023
            ],
            "fraction_bootstrap_means_gt_zero": 0.7829,
            "positive_delta_months": 31,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 400.0685127057204,
            "delta_omitting_best_month_arithmetic_USDT": 126.56954703927659,
            "year_delta_USDT": {
              "2020": -31.73123376250078,
              "2021": 45.660599801045464,
              "2022": 170.10405793982864,
              "2023": 313.8709212801805,
              "2024": -34.04164772965305,
              "2025": 62.775362216096255
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 558.3692935074978,
              "2021": 480.97745994395154,
              "2022": 356.5340018051684,
              "2023": 212.76713846481653,
              "2024": 560.6797074746501,
              "2025": 463.86269752890075
            }
          },
          "C": {
            "observed_mean_USDT_month": 8.067379053569889,
            "observed_total_USDT": 508.244880374903,
            "ci95_percentile_mean_USDT_month": [
              -10.968305182075092,
              28.95891980795132
            ],
            "fraction_bootstrap_means_gt_zero": 0.7802,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.7897367463156,
            "delta_omitting_best_month_arithmetic_USDT": 114.4551436285874,
            "year_delta_USDT": {
              "2020": -28.923563857602858,
              "2021": 26.12168760300301,
              "2022": 166.06137293689062,
              "2023": 335.2334431373256,
              "2024": -34.50926226997581,
              "2025": 44.261202825262444
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 537.1684442325059,
              "2021": 482.1231927719,
              "2022": 342.1835074380124,
              "2023": 173.0114372375774,
              "2024": 542.7541426448788,
              "2025": 463.98367754964056
            }
          }
        }
      }
    },
    {
      "level": "F95",
      "primary_full61": {
        "months": 61,
        "period_start": "2020-11",
        "period_last": "2025-11",
        "indices_sha256": "b016a45fd86e96cdca1a1ae5ae1e9dfe7e348ec1c7aaf7477ab849c06d7fba64",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 6.852541806546842,
            "observed_total_USDT": 418.00505019935736,
            "ci95_percentile_mean_USDT_month": [
              -12.815780307570055,
              29.144849976911324
            ],
            "fraction_bootstrap_means_gt_zero": 0.7293,
            "positive_delta_months": 29,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.312404021799,
            "delta_omitting_best_month_arithmetic_USDT": 24.692646177558345,
            "year_delta_USDT": {
              "2020": -27.273064877230354,
              "2021": 40.29017471694533,
              "2022": 190.52052043074036,
              "2023": 339.62310783658904,
              "2024": -23.070198451443503,
              "2025": -102.08548945624352
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 445.2781150765877,
              "2021": 377.714875482412,
              "2022": 227.484529768617,
              "2023": 78.38194236276831,
              "2024": 441.07524865080086,
              "2025": 520.0905396556009
            }
          },
          "C": {
            "observed_mean_USDT_month": 7.370821106775469,
            "observed_total_USDT": 449.6200875133036,
            "ci95_percentile_mean_USDT_month": [
              -12.381813987208616,
              29.370157543822952
            ],
            "fraction_bootstrap_means_gt_zero": 0.7477,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 384.85027873193394,
            "delta_omitting_best_month_arithmetic_USDT": 64.76980878136965,
            "year_delta_USDT": {
              "2020": -28.621076137931595,
              "2021": 46.37759523836576,
              "2022": 187.26796634474704,
              "2023": 359.39469808471586,
              "2024": -24.06544229000974,
              "2025": -90.73365372658373
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 478.2411636512352,
              "2021": 403.24249227493783,
              "2022": 262.35212116855655,
              "2023": 90.22538942858773,
              "2024": 473.68552980331333,
              "2025": 540.3537412398873
            }
          }
        }
      },
      "secondary_included63": {
        "months": 63,
        "period_start": "2020-10",
        "period_last": "2025-12",
        "indices_sha256": "e6d7a98b9c4994150f67df18af69acd7414dfb2592b836ffc35a9ac8046a0a96",
        "portfolio": {
          "B": {
            "observed_mean_USDT_month": 9.33597034360915,
            "observed_total_USDT": 588.1661316473765,
            "ci95_percentile_mean_USDT_month": [
              -9.194416192184264,
              29.935087801304803
            ],
            "fraction_bootstrap_means_gt_zero": 0.8175,
            "positive_delta_months": 30,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 393.312404021799,
            "delta_omitting_best_month_arithmetic_USDT": 194.85372762557745,
            "year_delta_USDT": {
              "2020": -27.273064877230354,
              "2021": 40.29017471694533,
              "2022": 190.52052043074036,
              "2023": 339.62310783658904,
              "2024": -23.070198451443503,
              "2025": 68.07559199177558
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 615.4391965246068,
              "2021": 547.8759569304311,
              "2022": 397.6456112166361,
              "2023": 248.54302381078742,
              "2024": 611.23633009882,
              "2025": 520.0905396556009
            }
          },
          "C": {
            "observed_mean_USDT_month": 9.784708484292914,
            "observed_total_USDT": 616.4366345104536,
            "ci95_percentile_mean_USDT_month": [
              -8.678941843031119,
              30.223927752737783
            ],
            "fraction_bootstrap_means_gt_zero": 0.8345,
            "positive_delta_months": 31,
            "best_incremental_month": "2022-01",
            "best_incremental_month_delta_USDT": 384.85027873193394,
            "delta_omitting_best_month_arithmetic_USDT": 231.58635577851965,
            "year_delta_USDT": {
              "2020": -28.621076137931595,
              "2021": 46.37759523836576,
              "2022": 187.26796634474704,
              "2023": 359.39469808471586,
              "2024": -24.06544229000974,
              "2025": 76.08289327056627
            },
            "delta_omitting_each_year_arithmetic_USDT": {
              "2020": 645.0577106483852,
              "2021": 570.0590392720878,
              "2022": 429.16866816570655,
              "2023": 257.04193642573773,
              "2024": 640.5020768004633,
              "2025": 540.3537412398873
            }
          }
        }
      }
    }
  ],
  "exploration": [
    {
      "id": "K1001",
      "rows": [
        {
          "name": "K1001C",
          "url": "http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c",
          "role": "exploration",
          "fee": 0.00045,
          "net": 13854.325570277431,
          "dd": -8.7767634975779,
          "reference": "N204C",
          "delta_reference": 614.8831904306389,
          "plus10": 11772.95646334888,
          "months_nominal_calendar": "44/63",
          "months_plus5_active": "43/62",
          "months_plus5_calendar": "43/63",
          "quarters_plus5": "18/21",
          "diversity": {
            "entry_changes": 5,
            "matched_exit_changes": 0
          },
          "metadata_ok": true,
          "supplement_fills": 45,
          "types": {
            "STOP": 44,
            "MARKET": 1
          },
          "delta_Y902": 173.97639939104738,
          "delta_plus10_Y902": 177.95783537059106,
          "screen": {
            "nominal_better_Y902": true,
            "cost10_atleast_Y902": true,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": false,
            "metadata": true,
            "calendar_full_and_included": true,
            "positive_at_least3_year_blocks": true,
            "without_best_incremental_month": true
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": 614.8831904306353,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.45457841226744
              },
              "delta_without_best_month": 216.42861201836786,
              "annual_delta_2021_2025": {
                "2021": -6.923773029629956,
                "2022": 145.92853106626535,
                "2023": 304.75646447744657,
                "2024": 128.23006810496372,
                "2025": 75.87236386907898
              },
              "positive_year_blocks": 4,
              "omission_each_year": {
                "2020": 647.8636544881247,
                "2021": 621.8069634602653,
                "2022": 468.95465936436995,
                "2023": 310.1267259531887,
                "2024": 486.6531223256716,
                "2025": 539.0108265615563
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": 420.0240145886564,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.45457841226744
              },
              "delta_without_best_month": 21.56943617638899,
              "annual_delta_2021_2025": {
                "2021": -6.923773029629956,
                "2022": 145.92853106626535,
                "2023": 304.75646447744657,
                "2024": 128.23006810496372,
                "2025": -118.98681197289989
              },
              "positive_year_blocks": 3,
              "omission_each_year": {
                "2020": 453.0044786461458,
                "2021": 426.9477876182864,
                "2022": 274.0954835223911,
                "2023": 115.26755011120986,
                "2024": 291.7939464836927,
                "2025": 539.0108265615563
              }
            }
          }
        },
        {
          "name": "K1001B",
          "url": "http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a",
          "role": "exploration",
          "fee": 0.00045,
          "net": 13619.213769007947,
          "dd": -8.823109449257238,
          "reference": "N204B",
          "delta_reference": 562.5988539302834,
          "plus10": 11654.854398540218,
          "months_nominal_calendar": "43/63",
          "months_plus5_active": "42/62",
          "months_plus5_calendar": "42/63",
          "quarters_plus5": "17/21",
          "diversity": {
            "entry_changes": 5,
            "matched_exit_changes": 0
          },
          "metadata_ok": true,
          "supplement_fills": 45,
          "types": {
            "STOP": 44,
            "MARKET": 1
          },
          "delta_Y902": 172.97924343272098,
          "delta_plus10_Y902": 177.54397244958454,
          "screen": {
            "nominal_better_Y902": true,
            "cost10_atleast_Y902": true,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": false,
            "metadata": true,
            "calendar_full_and_included": true,
            "positive_at_least3_year_blocks": true,
            "without_best_incremental_month": true
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": 562.5988539302925,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.25312203934664
              },
              "delta_without_best_month": 155.3457318909459,
              "annual_delta_2021_2025": {
                "2021": -13.611822798809953,
                "2022": 145.07019137744828,
                "2023": 276.7929084147563,
                "2024": 125.80796117706268,
                "2025": 61.519439474272076
              },
              "positive_year_blocks": 4,
              "omission_each_year": {
                "2020": 595.5786776447294,
                "2021": 576.2106767291025,
                "2022": 417.52866255284425,
                "2023": 285.8059455155362,
                "2024": 436.79089275322985,
                "2025": 501.07941445602046
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": 365.4948239994883,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.25312203934664
              },
              "delta_without_best_month": -41.758298039858346,
              "annual_delta_2021_2025": {
                "2021": -13.611822798809953,
                "2022": 145.07019137744828,
                "2023": 276.7929084147563,
                "2024": 125.80796117706268,
                "2025": -135.58459045653217
              },
              "positive_year_blocks": 3,
              "omission_each_year": {
                "2020": 398.47464771392515,
                "2021": 379.10664679829824,
                "2022": 220.42463262204,
                "2023": 88.70191558473198,
                "2024": 239.6868628224256,
                "2025": 501.07941445602046
              }
            }
          }
        }
      ],
      "all_screens_both": false
    },
    {
      "id": "K1002",
      "rows": [
        {
          "name": "K1002C",
          "url": "http://localhost:9200/#/backtest/36c79fa4-2e96-482d-80d3-7692b85a261d",
          "role": "exploration",
          "fee": 0.00045,
          "net": 10831.1633863388,
          "dd": -9.124985127601349,
          "reference": "N204C",
          "delta_reference": -2408.2789935079927,
          "plus10": 9014.697344259985,
          "months_nominal_calendar": "41/63",
          "months_plus5_active": "40/61",
          "months_plus5_calendar": "40/63",
          "quarters_plus5": "17/21",
          "diversity": {
            "entry_changes": 63,
            "matched_exit_changes": 0
          },
          "metadata_ok": true,
          "supplement_fills": 20,
          "types": {
            "STOP": 20
          },
          "delta_Y902": -2849.1857845475843,
          "delta_plus10_Y902": -2580.301283718305,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": false,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": true,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -2408.2789935079927,
              "best_incremental_month": {
                "month": "2025-04",
                "complete": true,
                "delta": 432.1520653207117
              },
              "delta_without_best_month": -2840.4310588287044,
              "annual_delta_2021_2025": {
                "2021": -437.8899814476881,
                "2022": -285.37035879072755,
                "2023": -373.54250719306583,
                "2024": -409.5081900043788,
                "2025": -971.144735928352
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2477.4557733642123,
                "2021": -1970.3890120603046,
                "2022": -2122.908634717265,
                "2023": -2034.7364863149269,
                "2024": -1998.770803503614,
                "2025": -1437.1342575796407
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -2685.0640007015827,
              "best_incremental_month": {
                "month": "2025-04",
                "complete": true,
                "delta": 432.1520653207117
              },
              "delta_without_best_month": -3117.2160660222944,
              "annual_delta_2021_2025": {
                "2021": -437.8899814476881,
                "2022": -285.37035879072755,
                "2023": -373.54250719306583,
                "2024": -409.5081900043788,
                "2025": -1247.929743121942
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2754.2407805578023,
                "2021": -2247.1740192538946,
                "2022": -2399.693641910855,
                "2023": -2311.521493508517,
                "2024": -2275.555810697204,
                "2025": -1437.1342575796407
              }
            }
          }
        },
        {
          "name": "K1002B",
          "url": "http://localhost:9200/#/backtest/728f638d-0f10-4b6c-9b6f-4f5533c89df9",
          "role": "exploration",
          "fee": 0.00045,
          "net": 10640.885028810893,
          "dd": -9.150118495972205,
          "reference": "N204B",
          "delta_reference": -2415.7298862667703,
          "plus10": 8932.215784904569,
          "months_nominal_calendar": "40/63",
          "months_plus5_active": "39/61",
          "months_plus5_calendar": "39/63",
          "quarters_plus5": "16/21",
          "diversity": {
            "entry_changes": 63,
            "matched_exit_changes": 0
          },
          "metadata_ok": true,
          "supplement_fills": 20,
          "types": {
            "STOP": 20
          },
          "delta_Y902": -2805.349496764333,
          "delta_plus10_Y902": -2545.094641186064,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": false,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": false,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -2415.7298862667703,
              "best_incremental_month": {
                "month": "2025-04",
                "complete": true,
                "delta": 425.7512936394487
              },
              "delta_without_best_month": -2841.481179906219,
              "annual_delta_2021_2025": {
                "2021": -450.3954586535874,
                "2022": -289.97422065679893,
                "2023": -359.5929024074885,
                "2024": -408.6194683765789,
                "2025": -976.324616028538
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2484.9066661229917,
                "2021": -1965.334427613183,
                "2022": -2125.7556656099714,
                "2023": -2056.136983859282,
                "2024": -2007.1104178901915,
                "2025": -1439.4052702382323
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -2674.5106583011475,
              "best_incremental_month": {
                "month": "2025-04",
                "complete": true,
                "delta": 425.7512936394487
              },
              "delta_without_best_month": -3100.261951940596,
              "annual_delta_2021_2025": {
                "2021": -450.3954586535874,
                "2022": -289.97422065679893,
                "2023": -359.5929024074885,
                "2024": -408.6194683765789,
                "2025": -1235.1053880629152
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2743.687438157369,
                "2021": -2224.11519964756,
                "2022": -2384.5364376443486,
                "2023": -2314.917755893659,
                "2024": -2265.8911899245686,
                "2025": -1439.4052702382323
              }
            }
          }
        }
      ],
      "all_screens_both": false
    },
    {
      "id": "K1003",
      "rows": [
        {
          "name": "K1003B",
          "url": "http://localhost:9200/#/backtest/82105bee-e22b-4ae2-a311-b369453b03e9",
          "role": "exploration",
          "fee": 0.00045,
          "net": 10934.006048245641,
          "dd": -9.08366250466932,
          "reference": "N204B",
          "delta_reference": -2122.6088668320226,
          "plus10": 9068.055851343659,
          "months_nominal_calendar": "39/63",
          "months_plus5_active": "39/62",
          "months_plus5_calendar": "39/63",
          "quarters_plus5": "15/21",
          "diversity": {
            "entry_changes": 1,
            "matched_exit_changes": 23
          },
          "metadata_ok": true,
          "supplement_fills": 47,
          "types": {
            "STOP": 46,
            "MARKET": 1
          },
          "delta_Y902": -2512.228477329585,
          "delta_plus10_Y902": -2409.254574746974,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": false,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -2122.6088668320117,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.2531220393503
              },
              "delta_without_best_month": -2529.861988871362,
              "annual_delta_2021_2025": {
                "2021": -173.6683826250828,
                "2022": -292.4583348317956,
                "2023": -622.0574951088074,
                "2024": -300.8033456312205,
                "2025": -759.4834839284667
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2148.471042125373,
                "2021": -1948.9404842069289,
                "2022": -1830.1505320002161,
                "2023": -1500.5513717232043,
                "2024": -1821.8055212007912,
                "2025": -1363.125382903545
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -2375.31952955791,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.2531220393503
              },
              "delta_without_best_month": -2782.57265159726,
              "annual_delta_2021_2025": {
                "2021": -173.6683826250828,
                "2022": -292.4583348317956,
                "2023": -622.0574951088074,
                "2024": -300.8033456312205,
                "2025": -1012.1941466543649
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2401.181704851271,
                "2021": -2201.651146932827,
                "2022": -2082.8611947261143,
                "2023": -1753.2620344491024,
                "2024": -2074.5161839266893,
                "2025": -1363.125382903545
              }
            }
          }
        },
        {
          "name": "K1003C",
          "url": "http://localhost:9200/#/backtest/00c0f043-ea8a-4d28-88be-7553442909e1",
          "role": "exploration",
          "fee": 0.00045,
          "net": 11124.487611692486,
          "dd": -9.106204367035552,
          "reference": "N204C",
          "delta_reference": -2114.9547681543063,
          "plus10": 9150.850018032812,
          "months_nominal_calendar": "40/63",
          "months_plus5_active": "40/62",
          "months_plus5_calendar": "40/63",
          "quarters_plus5": "16/21",
          "diversity": {
            "entry_changes": 1,
            "matched_exit_changes": 23
          },
          "metadata_ok": true,
          "supplement_fills": 47,
          "types": {
            "STOP": 46,
            "MARKET": 1
          },
          "delta_Y902": -2555.861559193898,
          "delta_plus10_Y902": -2444.148609945478,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": false,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -2114.954768154301,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.45457841226926
              },
              "delta_without_best_month": -2513.40934656657,
              "annual_delta_2021_2025": {
                "2021": -164.02179242447528,
                "2022": -289.57297750828184,
                "2023": -634.4533725915153,
                "2024": -297.2915111424172,
                "2025": -755.4772897809708
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2140.8169434476604,
                "2021": -1950.9329757298256,
                "2022": -1825.381790646019,
                "2023": -1480.5013955627855,
                "2024": -1817.6632570118836,
                "2025": -1359.47747837333
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -2383.792822654719,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.45457841226926
              },
              "delta_without_best_month": -2782.2474010669885,
              "annual_delta_2021_2025": {
                "2021": -164.02179242447528,
                "2022": -289.57297750828184,
                "2023": -634.4533725915153,
                "2024": -297.2915111424172,
                "2025": -1024.3153442813891
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -2409.6549979480787,
                "2021": -2219.771030230244,
                "2022": -2094.2198451464374,
                "2023": -1749.339450063204,
                "2024": -2086.501311512302,
                "2025": -1359.47747837333
              }
            }
          }
        }
      ],
      "all_screens_both": false
    },
    {
      "id": "K1004",
      "rows": [
        {
          "name": "K1004B",
          "url": "http://localhost:9200/#/backtest/a523b5c5-8a91-4dd0-b596-550405b10fe5",
          "role": "exploration",
          "fee": 0.00045,
          "net": 12407.213554150116,
          "dd": -8.827486156085962,
          "reference": "N204B",
          "delta_reference": -649.401360927548,
          "plus10": 10503.070080866262,
          "months_nominal_calendar": "42/63",
          "months_plus5_active": "39/62",
          "months_plus5_calendar": "39/63",
          "quarters_plus5": "15/21",
          "diversity": {
            "entry_changes": 1,
            "matched_exit_changes": 11
          },
          "metadata_ok": true,
          "supplement_fills": 47,
          "types": {
            "STOP": 46,
            "MARKET": 1
          },
          "delta_Y902": -1039.0209714251105,
          "delta_plus10_Y902": -974.2403452243707,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": false,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -649.4013609275426,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.2531220393503
              },
              "delta_without_best_month": -1056.6544829668928,
              "annual_delta_2021_2025": {
                "2021": -158.65169732826507,
                "2022": -115.7333662249057,
                "2023": -323.9051147012633,
                "2024": -43.38428948306682,
                "2025": -33.176402812350716
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -674.8508705498516,
                "2021": -490.7496635992775,
                "2022": -533.6679947026369,
                "2023": -325.49624622627925,
                "2024": -606.0170714444757,
                "2025": -616.2249581151918
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -871.601720906041,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 407.2531220393503
              },
              "delta_without_best_month": -1278.8548429453913,
              "annual_delta_2021_2025": {
                "2021": -158.65169732826507,
                "2022": -115.7333662249057,
                "2023": -323.9051147012633,
                "2024": -43.38428948306682,
                "2025": -255.37676279084917
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -897.0512305283501,
                "2021": -712.9500235777759,
                "2022": -755.8683546811353,
                "2023": -547.6966062047777,
                "2024": -828.2174314229742,
                "2025": -616.2249581151918
              }
            }
          }
        },
        {
          "name": "K1004C",
          "url": "http://localhost:9200/#/backtest/e32e4b65-850b-475f-9179-be61b25131d6",
          "role": "exploration",
          "fee": 0.00045,
          "net": 12654.848991258088,
          "dd": -8.803074797569233,
          "reference": "N204C",
          "delta_reference": -584.5933885887043,
          "plus10": 10636.40064061467,
          "months_nominal_calendar": "41/63",
          "months_plus5_active": "40/62",
          "months_plus5_calendar": "40/63",
          "quarters_plus5": "16/21",
          "diversity": {
            "entry_changes": 1,
            "matched_exit_changes": 11
          },
          "metadata_ok": true,
          "supplement_fills": 47,
          "types": {
            "STOP": 46,
            "MARKET": 1
          },
          "delta_Y902": -1025.5001796282959,
          "delta_plus10_Y902": -958.5979873636206,
          "screen": {
            "nominal_better_Y902": false,
            "cost10_atleast_Y902": false,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": true,
            "metadata": true,
            "calendar_full_and_included": false,
            "positive_at_least3_year_blocks": false,
            "without_best_incremental_month": false
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": -584.5933885886916,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.4545784122711
              },
              "delta_without_best_month": -983.0479670009627,
              "annual_delta_2021_2025": {
                "2021": -129.2750243544615,
                "2022": -112.01490416099477,
                "2023": -316.97671573309526,
                "2024": -43.71980599260496,
                "2025": -8.056447969844157
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -610.0428982110006,
                "2021": -455.3183642342301,
                "2022": -472.5784844276968,
                "2023": -267.61667285559633,
                "2024": -540.8735825960866,
                "2025": -576.5369406188474
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": -811.9585815309329,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 398.4545784122711
              },
              "delta_without_best_month": -1210.413159943204,
              "annual_delta_2021_2025": {
                "2021": -129.2750243544615,
                "2022": -112.01490416099477,
                "2023": -316.97671573309526,
                "2024": -43.71980599260496,
                "2025": -235.42164091208542
              },
              "positive_year_blocks": 0,
              "omission_each_year": {
                "2020": -837.4080911532419,
                "2021": -682.6835571764714,
                "2022": -699.9436773699381,
                "2023": -494.9818657978376,
                "2024": -768.2387755383279,
                "2025": -576.5369406188474
              }
            }
          }
        }
      ],
      "all_screens_both": false
    },
    {
      "id": "K1005",
      "rows": [
        {
          "name": "K1005B",
          "url": "http://localhost:9200/#/backtest/3f979db7-44e2-44c6-9b82-7c3362084f62",
          "role": "exploration",
          "fee": 0.00045,
          "net": 13844.908563261655,
          "dd": -9.707227693606168,
          "reference": "N204B",
          "delta_reference": 788.2936481839915,
          "plus10": 11851.332023217405,
          "months_nominal_calendar": "42/63",
          "months_plus5_active": "41/62",
          "months_plus5_calendar": "41/63",
          "quarters_plus5": "17/21",
          "diversity": {
            "entry_changes": 0,
            "matched_exit_changes": 5
          },
          "metadata_ok": true,
          "supplement_fills": 46,
          "types": {
            "STOP": 45,
            "MARKET": 1
          },
          "delta_Y902": 398.6740376864291,
          "delta_plus10_Y902": 374.02159712677167,
          "screen": {
            "nominal_better_Y902": true,
            "cost10_atleast_Y902": true,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": false,
            "metadata": true,
            "calendar_full_and_included": true,
            "positive_at_least3_year_blocks": true,
            "without_best_incremental_month": true
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": 788.2936481840115,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 411.5072552694801
              },
              "delta_without_best_month": 376.78639291453146,
              "annual_delta_2021_2025": {
                "2021": 185.92054987838856,
                "2022": 171.25330358753308,
                "2023": 326.7391140679865,
                "2024": -25.92356328110327,
                "2025": 163.28406764564352
              },
              "positive_year_blocks": 4,
              "omission_each_year": {
                "2020": 821.2734718984484,
                "2021": 602.373098305623,
                "2022": 617.0403445964785,
                "2023": 461.554534116025,
                "2024": 814.2172114651148,
                "2025": 625.009580538368
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": 595.8617338732511,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 411.5072552694801
              },
              "delta_without_best_month": 184.35447860377099,
              "annual_delta_2021_2025": {
                "2021": 185.92054987838856,
                "2022": 171.25330358753308,
                "2023": 326.7391140679865,
                "2024": -25.92356328110327,
                "2025": -29.14784666511696
              },
              "positive_year_blocks": 3,
              "omission_each_year": {
                "2020": 628.8415575876879,
                "2021": 409.9411839948625,
                "2022": 424.608430285718,
                "2023": 269.12261980526455,
                "2024": 621.7852971543543,
                "2025": 625.009580538368
              }
            }
          }
        },
        {
          "name": "K1005C",
          "url": "http://localhost:9200/#/backtest/8d198fc1-eae8-4a67-8258-e6fabe58756a",
          "role": "exploration",
          "fee": 0.00045,
          "net": 14103.941737074154,
          "dd": -9.642664324702643,
          "reference": "N204C",
          "delta_reference": 864.4993572273615,
          "plus10": 11989.896448856158,
          "months_nominal_calendar": "43/63",
          "months_plus5_active": "42/62",
          "months_plus5_calendar": "42/63",
          "quarters_plus5": "17/21",
          "diversity": {
            "entry_changes": 0,
            "matched_exit_changes": 5
          },
          "metadata_ok": true,
          "supplement_fills": 46,
          "types": {
            "STOP": 45,
            "MARKET": 1
          },
          "delta_Y902": 423.59256618777,
          "delta_plus10_Y902": 394.89782087786807,
          "screen": {
            "nominal_better_Y902": true,
            "cost10_atleast_Y902": true,
            "dd": true,
            "supplement_atleast30": true,
            "mechanism_changes_atleast10": false,
            "metadata": true,
            "calendar_full_and_included": true,
            "positive_at_least3_year_blocks": true,
            "without_best_incremental_month": true
          },
          "concentration": {
            "included63": {
              "months": 63,
              "delta_total_USDT": 864.499357227367,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 402.70871164239725
              },
              "delta_without_best_month": 461.79064558496975,
              "annual_delta_2021_2025": {
                "2021": 209.93214135941707,
                "2022": 169.63362039940876,
                "2023": 366.1442676881361,
                "2024": -25.329890008160874,
                "2025": 177.09968184605532
              },
              "positive_year_blocks": 4,
              "omission_each_year": {
                "2020": 897.4798212848564,
                "2021": 654.5672158679499,
                "2022": 694.8657368279582,
                "2023": 498.3550895392309,
                "2024": 889.8292472355279,
                "2025": 687.3996753813117
              }
            },
            "complete61": {
              "months": 61,
              "delta_total_USDT": 676.4073163103021,
              "best_incremental_month": {
                "month": "2022-01",
                "complete": true,
                "delta": 402.70871164239725
              },
              "delta_without_best_month": 273.6986046679049,
              "annual_delta_2021_2025": {
                "2021": 209.93214135941707,
                "2022": 169.63362039940876,
                "2023": 366.1442676881361,
                "2024": -25.329890008160874,
                "2025": -10.99235907100956
              },
              "positive_year_blocks": 3,
              "omission_each_year": {
                "2020": 709.3877803677915,
                "2021": 466.47517495088505,
                "2022": 506.77369591089337,
                "2023": 310.263048622166,
                "2024": 701.737206318463,
                "2025": 687.3996753813117
              }
            }
          }
        }
      ],
      "all_screens_both": false
    }
  ],
  "decision": "Retain Y902 as frozen research candidate; preserve N204 operational reference and report new candidates separately. No live promotion, no2026, no extra backtests."
}
```
