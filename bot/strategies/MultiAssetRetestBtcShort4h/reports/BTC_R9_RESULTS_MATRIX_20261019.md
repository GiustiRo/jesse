# BTC R9 — matriz final

2026 cerrado. Fee engine por lado explícito; +5/+10 son overlays ADICIONALES al fee de esa fila, sobre fills/cantidades fijos. F70 se compara N70 y F95 con N95 a fee iguales. N95 es referencia nueva y su Δ frente a N204 nominal refleja cambiofee, no una variante ganadora. TPvecinos son sensibilidad, no candidatos seleccionables. Exploraciones Kse comparan conY902 yN204nominales y no se promocionan automáticamente. Denominadores activos/calendar se muestran por separado. Una fuente protegida no garantiza idénticas ejecuciones por ocupación/capital. No OOS ni pruebaanti-overfit.

|Prueba|Fee por lado|Neto USDT|DD motor%|Referencia de Δ|Δneto|M positivos nominal/calendario|M +5 activos / calendario|Q+5|Suplfills|
|---|---:|---:|---:|---|---:|---|---|---|---:|
|[F70B](http://localhost:9200/#/backtest/c20f22a8-38bf-4ad3-99d0-2d583d91d81c)|0.0007|10793.949439|-9.9327|N70B|526.638060|39/63|38/62 / 38/63|16/21|46|
|[F70C](http://localhost:9200/#/backtest/2297b82f-5db7-457a-8d46-9b53465dde7d)|0.0007|10917.180154|-9.9136|N70C|508.244880|40/63|39/62 / 39/63|17/21|46|
|[F95B](http://localhost:9200/#/backtest/2b1ef237-1c48-40a9-84b3-d939ab99a3ba)|0.00095|9570.519836|-10.1542|N95B|588.166132|38/63|35/62 / 35/63|16/21|46|
|[F95C](http://localhost:9200/#/backtest/26f5560f-8db8-45f4-8203-1d0612658136)|0.00095|9606.619794|-10.1560|N95C|616.436635|39/63|36/62 / 36/63|17/21|46|
|[N95B](http://localhost:9200/#/backtest/9b7b99b1-a5a1-440d-98f5-aa1c45a1108c)|0.00095|8982.353705|-9.2940|N204B|-4074.261210|37/63|36/63 / 36/63|14/21|pendiente|
|[N95C](http://localhost:9200/#/backtest/b1399fa4-5495-43c1-bc45-3bc6d1b3da7b)|0.00095|8990.183160|-9.2996|N204C|-4249.259220|38/63|36/63 / 36/63|16/21|pendiente|
|[T18B](http://localhost:9200/#/backtest/3723e918-e830-4697-abb4-7f9e2d0f172a)|0.00045|13084.583658|-9.6898|N204B|27.968743|40/63|40/62 / 40/63|16/21|46|
|[T18C](http://localhost:9200/#/backtest/07e4ce1e-e76b-410c-903e-156864907ea5)|0.00045|13293.527710|-9.6313|N204C|54.085330|42/63|41/62 / 41/63|17/21|46|
|[T22B](http://localhost:9200/#/backtest/826b451d-5836-4385-b421-ad63b64f1a76)|0.00045|13352.641093|-9.6849|N204B|296.026178|41/63|41/62 / 41/63|17/21|46|
|[T22C](http://localhost:9200/#/backtest/dc26f343-496f-4fea-9394-0ef595e8e65a)|0.00045|13563.774552|-9.6284|N204C|324.332172|42/63|41/62 / 41/63|17/21|46|
|[K1001C](http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c)|0.00045|13854.325570|-8.7768|N204C|614.883190|44/63|43/62 / 43/63|18/21|45|
|[K1001B](http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a)|0.00045|13619.213769|-8.8231|N204B|562.598854|43/63|42/62 / 42/63|17/21|45|
|[K1002C](http://localhost:9200/#/backtest/36c79fa4-2e96-482d-80d3-7692b85a261d)|0.00045|10831.163386|-9.1250|N204C|-2408.278994|41/63|40/61 / 40/63|17/21|20|
|[K1002B](http://localhost:9200/#/backtest/728f638d-0f10-4b6c-9b6f-4f5533c89df9)|0.00045|10640.885029|-9.1501|N204B|-2415.729886|40/63|39/61 / 39/63|16/21|20|
|[K1003B](http://localhost:9200/#/backtest/82105bee-e22b-4ae2-a311-b369453b03e9)|0.00045|10934.006048|-9.0837|N204B|-2122.608867|39/63|39/62 / 39/63|15/21|47|
|[K1003C](http://localhost:9200/#/backtest/00c0f043-ea8a-4d28-88be-7553442909e1)|0.00045|11124.487612|-9.1062|N204C|-2114.954768|40/63|40/62 / 40/63|16/21|47|
|[K1004B](http://localhost:9200/#/backtest/a523b5c5-8a91-4dd0-b596-550405b10fe5)|0.00045|12407.213554|-8.8275|N204B|-649.401361|42/63|39/62 / 39/63|15/21|47|
|[K1004C](http://localhost:9200/#/backtest/e32e4b65-850b-475f-9179-be61b25131d6)|0.00045|12654.848991|-8.8031|N204C|-584.593389|41/63|40/62 / 40/63|16/21|47|
|[K1005B](http://localhost:9200/#/backtest/3f979db7-44e2-44c6-9b82-7c3362084f62)|0.00045|13844.908563|-9.7072|N204B|788.293648|42/63|41/62 / 41/63|17/21|46|
|[K1005C](http://localhost:9200/#/backtest/8d198fc1-eae8-4a67-8258-e6fabe58756a)|0.00045|14103.941737|-9.6427|N204C|864.499357|43/63|42/62 / 42/63|17/21|46|

```json
[
  {
    "name": "F70B",
    "url": "http://localhost:9200/#/backtest/c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
    "role": "validation",
    "fee": 0.0007,
    "net": 10793.949438932308,
    "dd": -9.93268724082509,
    "reference": "N70B",
    "delta_reference": 526.6380597449861,
    "plus10": 8972.57951391615,
    "months_nominal_calendar": "39/63",
    "months_plus5_active": "38/62",
    "months_plus5_calendar": "38/63",
    "quarters_plus5": "16/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 0
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "F70C",
    "url": "http://localhost:9200/#/backtest/2297b82f-5db7-457a-8d46-9b53465dde7d",
    "role": "validation",
    "fee": 0.0007,
    "net": 10917.180154275862,
    "dd": -9.913586199276425,
    "reference": "N70C",
    "delta_reference": 508.24488037491574,
    "plus10": 8994.68753674732,
    "months_nominal_calendar": "40/63",
    "months_plus5_active": "39/62",
    "months_plus5_calendar": "39/63",
    "quarters_plus5": "17/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 0
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "F95B",
    "url": "http://localhost:9200/#/backtest/2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
    "role": "validation",
    "fee": 0.00095,
    "net": 9570.519836457781,
    "dd": -10.15422406719626,
    "reference": "N95B",
    "delta_reference": 588.1661316473856,
    "plus10": 7872.909250648957,
    "months_nominal_calendar": "38/63",
    "months_plus5_active": "35/62",
    "months_plus5_calendar": "35/63",
    "quarters_plus5": "16/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 0
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "F95C",
    "url": "http://localhost:9200/#/backtest/26f5560f-8db8-45f4-8203-1d0612658136",
    "role": "validation",
    "fee": 0.00095,
    "net": 9606.619794398342,
    "dd": -10.155985801505906,
    "reference": "N95C",
    "delta_reference": 616.4366345104536,
    "plus10": 7819.773983281466,
    "months_nominal_calendar": "39/63",
    "months_plus5_active": "36/62",
    "months_plus5_calendar": "36/63",
    "quarters_plus5": "17/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 0
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "N95B",
    "url": "http://localhost:9200/#/backtest/9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
    "role": "validation",
    "fee": 0.00095,
    "net": 8982.353704810395,
    "dd": -9.293966954619359,
    "reference": "N204B",
    "delta_reference": -4074.2612102672683,
    "plus10": 7159.65960422322,
    "months_nominal_calendar": "37/63",
    "months_plus5_active": "36/63",
    "months_plus5_calendar": "36/63",
    "quarters_plus5": "14/21",
    "diversity": null,
    "metadata_ok": true,
    "types": null,
    "concentration": null
  },
  {
    "name": "N95C",
    "url": "http://localhost:9200/#/backtest/b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
    "role": "validation",
    "fee": 0.00095,
    "net": 8990.183159887889,
    "dd": -9.299593157290131,
    "reference": "N204C",
    "delta_reference": -4249.2592199589035,
    "plus10": 7083.602479481224,
    "months_nominal_calendar": "38/63",
    "months_plus5_active": "36/63",
    "months_plus5_calendar": "36/63",
    "quarters_plus5": "16/21",
    "diversity": null,
    "metadata_ok": true,
    "types": null,
    "concentration": null
  },
  {
    "name": "T18B",
    "url": "http://localhost:9200/#/backtest/3723e918-e830-4697-abb4-7f9e2d0f172a",
    "role": "validation",
    "fee": 0.00045,
    "net": 13084.58365842148,
    "dd": -9.689827780952676,
    "reference": "N204B",
    "delta_reference": 27.96874334381573,
    "plus10": 11128.7582928346,
    "months_nominal_calendar": "40/63",
    "months_plus5_active": "40/62",
    "months_plus5_calendar": "40/63",
    "quarters_plus5": "16/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 15
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "T18C",
    "url": "http://localhost:9200/#/backtest/07e4ce1e-e76b-410c-903e-156864907ea5",
    "role": "validation",
    "fee": 0.00045,
    "net": 13293.527709995118,
    "dd": -9.631263736672778,
    "reference": "N204C",
    "delta_reference": 54.08533014832574,
    "plus10": 11223.640683973257,
    "months_nominal_calendar": "42/63",
    "months_plus5_active": "41/62",
    "months_plus5_calendar": "41/63",
    "quarters_plus5": "17/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 15
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "T22B",
    "url": "http://localhost:9200/#/backtest/826b451d-5836-4385-b421-ad63b64f1a76",
    "role": "validation",
    "fee": 0.00045,
    "net": 13352.641093027976,
    "dd": -9.68491487224954,
    "reference": "N204B",
    "delta_reference": 296.02617795031256,
    "plus10": 11398.948346271964,
    "months_nominal_calendar": "41/63",
    "months_plus5_active": "41/62",
    "months_plus5_calendar": "41/63",
    "quarters_plus5": "17/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 14
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
  {
    "name": "T22C",
    "url": "http://localhost:9200/#/backtest/dc26f343-496f-4fea-9394-0ef595e8e65a",
    "role": "validation",
    "fee": 0.00045,
    "net": 13563.774551598133,
    "dd": -9.628355502758978,
    "reference": "N204C",
    "delta_reference": 324.33217175134087,
    "plus10": 11494.971551922697,
    "months_nominal_calendar": "42/63",
    "months_plus5_active": "41/62",
    "months_plus5_calendar": "41/63",
    "quarters_plus5": "17/21",
    "diversity": {
      "entry_changes": 0,
      "matched_exit_changes": 14
    },
    "metadata_ok": true,
    "supplement_fills": 46,
    "types": {
      "STOP": 45,
      "MARKET": 1
    },
    "concentration": null
  },
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
  },
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
  },
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
  },
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
  },
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
]
```
