# BTC R7 — matriz final

2026cerrado; misma muestra de desarrollo2020-10-15→2025-12-31exclusiva.14nominales:2observación+6recetasB/C. N204referenceultimate;semillaN503oN204paraatribución. Puertas congeladas en BTC_R7_FROZEN_PROTOCOL_20261019.md. La diversidad de10salidas y3/5años no es prueba estadística; son controlesoperativos prefijados contra concentración. Omitirmejormes sóloaritmético,sinreplay. Overlays5/10bpsRTsobre rutas/cantidadesfijas, no mayorfeeengine. Meses full61/all63 y Q19/21; denominadormensualactivo,calendarioensummaries;positivos>0sinredondear. Elegibles: ninguno. Selección: ninguna.

|Receta|Cartera|Neto|ΔN204|Δsemilla|DDmotor%|Δ+10N204|M+5full/all|Q+5full/all|Salidas modificadas|Años Δ>0|Δsinmejormes|Gates N/MQ/+10/DD/salidas/años/sinmes|
|---|---|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---|
|[S701B](http://localhost:9200/#/backtest/a05b76ab-842f-428e-ba54-4099070ecea5)|B|13347.964135|291.349220|19.252422|-8.7816|301.685129|41/61;41/63|17/19;18/21|4|3/5|131.751761|PASS/PASS/PASS/PASS/FAIL/PASS/PASS|
|[S701C](http://localhost:9200/#/backtest/ca2c6fea-b723-4308-ba85-199535fde594)|C|13562.215143|322.772763|25.312630|-9.0542|329.066473|40/61;40/63|17/19;18/21|4|3/5|166.859738|PASS/FAIL/PASS/PASS/FAIL/PASS/PASS|
|[S702B](http://localhost:9200/#/backtest/3b464cbf-426f-4197-9646-834a8117c943)|B|12458.517360|-598.097555|-870.194353|-8.2202|-548.957627|39/61;39/63|16/19;17/21|21|3/5|-810.160881|FAIL/FAIL/FAIL/PASS/PASS/PASS/FAIL|
|[S702C](http://localhost:9200/#/backtest/9ff8c173-f3fa-459d-b467-092ec3c4924e)|C|12667.168502|-572.273878|-869.734011|-9.0515|-525.807428|38/61;38/63|17/19;18/21|21|3/5|-782.030047|FAIL/FAIL/FAIL/PASS/PASS/PASS/FAIL|
|[S703B](http://localhost:9200/#/backtest/576a3b11-dc73-46ea-938b-02088406ad52)|B|11840.239043|-1216.375872|-1488.472669|-8.9345|-1129.401331|38/60;38/62|17/19;18/21|24|1/5|-1400.399476|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|
|[S703C](http://localhost:9200/#/backtest/04acc6c2-7fb2-4e55-b4d6-7aab52722b74)|C|12033.135279|-1206.307101|-1503.767234|-9.0077|-1119.859326|37/60;37/62|17/19;18/21|24|1/5|-1385.436568|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|
|[S704B](http://localhost:9200/#/backtest/f005ba80-5b39-42f8-9ab5-97fb5568f07c)|B|12143.856484|-912.758431|-1184.855228|-9.3550|-903.822364|43/61;43/63|17/19;18/21|13|1/5|-1074.595659|FAIL/PASS/FAIL/PASS/PASS/FAIL/FAIL|
|[S704C](http://localhost:9200/#/backtest/2d941297-ac9f-4196-ac3b-3066298d6a5d)|C|12310.794249|-928.648131|-1226.108264|-9.3709|-918.617321|41/61;41/63|17/19;18/21|13|1/5|-1086.945164|FAIL/PASS/FAIL/PASS/PASS/FAIL/FAIL|
|[S705B](http://localhost:9200/#/backtest/789d5a10-e2cc-468c-8f76-f20fba9277aa)|B|11831.980546|-1224.634369|-1224.634369|-8.2633|-1173.320032|38/61;38/63|15/19;16/21|25|0/5|-1382.475083|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|
|[S705C](http://localhost:9200/#/backtest/aedc08d8-2ad7-4c62-8186-a777fe32ae25)|C|12026.165561|-1213.276819|-1213.276819|-9.0053|-1158.667392|38/61;38/63|17/19;18/21|25|0/5|-1370.182083|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|
|[S706B](http://localhost:9200/#/backtest/de7e68d4-3adb-4afe-9c62-ecb7496877a1)|B|11521.155997|-1535.458918|-1535.458918|-8.9293|-1469.071117|37/61;37/63|16/19;17/21|28|0/5|-1695.425533|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|
|[S706C](http://localhost:9200/#/backtest/f407f8a8-15b4-41cb-b756-46ced2f041b4)|C|11716.483214|-1522.959166|-1522.959166|-9.0356|-1453.766174|37/61;37/63|17/19;18/21|28|0/5|-1683.523558|FAIL/FAIL/FAIL/PASS/PASS/FAIL/FAIL|

```json
{
  "ranking": {
    "matrix": [
      {
        "id": "S701",
        "strategy": "N503ManageR701",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13347.964134693444,
            "delta": 291.3492196157804,
            "delta_seed": 19.25242187751428,
            "plus10": 11232.89487257444,
            "delta10": 301.68512902857583,
            "dd": -8.781604713439906,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 4,
            "annual_delta_MTM": {
              "2021": -89.89581828555129,
              "2022": 83.56662068032529,
              "2023": 399.37641561559394,
              "2024": 119.78760090854121,
              "2025": -221.4855993031124
            },
            "positive_years": 3,
            "best_incremental_month": 159.5974587743549,
            "delta_without_best_month": 131.7517608414255,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_exits": false,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13562.215143060492,
            "delta": 322.77276321369936,
            "delta_seed": 25.31263000108629,
            "plus10": 11332.481937376444,
            "delta10": 329.0664729960572,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 4,
            "annual_delta_MTM": {
              "2021": -79.83235145539038,
              "2022": 83.3418325769635,
              "2023": 413.45286298768224,
              "2024": 121.46865986613193,
              "2025": -215.65824076171702
            },
            "positive_years": 3,
            "best_incremental_month": 155.91302490877388,
            "delta_without_best_month": 166.8597383049255,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true,
              "modified_exits": false,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": 301.68512902857583,
        "worstDD": -9.054184091363382
      },
      {
        "id": "S702",
        "strategy": "N503ManageR702",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12458.517359615034,
            "delta": -598.0975554626293,
            "delta_seed": -870.1943532008954,
            "plus10": 10382.252116941965,
            "delta10": -548.9576266038985,
            "dd": -8.220162236587413,
            "counts": {
              "Mfull": "39/61",
              "Mall": "39/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.030952380952380953,
            "modified_exits": 21,
            "annual_delta_MTM": {
              "2021": 14.876838153766585,
              "2022": -237.65388183369396,
              "2023": 325.1581525127567,
              "2024": 106.75941197951033,
              "2025": -807.2380762749417
            },
            "positive_years": 3,
            "best_incremental_month": 212.0633257199479,
            "delta_without_best_month": -810.1608811825772,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": true,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12667.168502145854,
            "delta": -572.2738777009381,
            "delta_seed": -869.7340109135512,
            "plus10": 10477.608036379504,
            "delta10": -525.8074280008823,
            "dd": -9.051488831192911,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 21,
            "annual_delta_MTM": {
              "2021": 23.840331488836455,
              "2022": -231.08062480032095,
              "2023": 328.3775389271377,
              "2024": 108.19602411419692,
              "2025": -801.6071474307937
            },
            "positive_years": 3,
            "best_incremental_month": 209.7561688452115,
            "delta_without_best_month": -782.0300465461496,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": true,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.04682539682539688,
        "delta10": -548.9576266038985,
        "worstDD": -9.051488831192911
      },
      {
        "id": "S703",
        "strategy": "N503ManageR703",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11840.239043329439,
            "delta": -1216.375871748225,
            "delta_seed": -1488.4726694864912,
            "plus10": 9801.80841282274,
            "delta10": -1129.4013307231235,
            "dd": -8.934485482336708,
            "counts": {
              "Mfull": "38/60",
              "Mall": "38/62",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0370967741935484,
            "modified_exits": 24,
            "annual_delta_MTM": {
              "2021": -214.59944368183642,
              "2022": -256.45661356534583,
              "2023": 345.7487782479202,
              "2024": -208.16466421479345,
              "2025": -882.9039285341605
            },
            "positive_years": 1,
            "best_incremental_month": 184.0236046138798,
            "delta_without_best_month": -1400.399476362105,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12033.135279112626,
            "delta": -1206.307100734166,
            "delta_seed": -1503.767233946779,
            "plus10": 9883.556138240347,
            "delta10": -1119.8593261400401,
            "dd": -9.007698733905556,
            "counts": {
              "Mfull": "37/60",
              "Mall": "37/62",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0532258064516129,
            "modified_exits": 24,
            "annual_delta_MTM": {
              "2021": -200.36782291057534,
              "2022": -252.03388213441394,
              "2023": 346.69440086830764,
              "2024": -211.75064828848917,
              "2025": -888.8491482690006
            },
            "positive_years": 1,
            "best_incremental_month": 179.12946684243616,
            "delta_without_best_month": -1385.436567576602,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.0532258064516129,
        "delta10": -1129.4013307231235,
        "worstDD": -9.007698733905556
      },
      {
        "id": "S704",
        "strategy": "N503ManageR704",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12143.856484375285,
            "delta": -912.758430702379,
            "delta_seed": -1184.855228440645,
            "plus10": 10027.387379943882,
            "delta10": -903.8223636019811,
            "dd": -9.355006819199618,
            "counts": {
              "Mfull": "43/61",
              "Mall": "43/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.032539682539682535,
            "modified_exits": 13,
            "annual_delta_MTM": {
              "2021": -218.63739643705958,
              "2022": -147.79988951402265,
              "2023": 391.9136324697156,
              "2024": -333.613781500233,
              "2025": -604.6209957207611
            },
            "positive_years": 1,
            "best_incremental_month": 161.83722807780214,
            "delta_without_best_month": -1074.595658780181,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12310.794248954551,
            "delta": -928.6481308922412,
            "delta_seed": -1226.1082641048542,
            "plus10": 10084.798143385558,
            "delta10": -918.6173209948283,
            "dd": -9.370866588714543,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 13,
            "annual_delta_MTM": {
              "2021": -214.92002847950062,
              "2022": -147.16443539742795,
              "2023": 387.025010952917,
              "2024": -339.85341313698154,
              "2025": -613.7352648312371
            },
            "positive_years": 1,
            "best_incremental_month": 158.29703357841026,
            "delta_without_best_month": -1086.9451644706514,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.0007936507936507908,
        "delta10": -918.6173209948283,
        "worstDD": -9.370866588714543
      },
      {
        "id": "S705",
        "strategy": "N204ManageR705",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11831.980545599985,
            "delta": -1224.6343694776788,
            "delta_seed": -1224.6343694776788,
            "plus10": 9757.88971174821,
            "delta10": -1173.3200317976534,
            "dd": -8.26327860585957,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 25,
            "annual_delta_MTM": {
              "2021": -97.84545404211894,
              "2022": -409.29530967522624,
              "2023": -68.66321539565979,
              "2024": -18.448192562724216,
              "2025": -630.3821978019369
            },
            "positive_years": 0,
            "best_incremental_month": 157.84071384081835,
            "delta_without_best_month": -1382.4750833184971,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12026.165560964964,
            "delta": -1213.2768188818281,
            "delta_seed": -1213.2768188818281,
            "plus10": 9844.748072362072,
            "delta10": -1158.6673920183148,
            "dd": -9.00529828997393,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 25,
            "annual_delta_MTM": {
              "2021": -88.746213550834,
              "2022": -403.0860223126401,
              "2023": -83.72550061715265,
              "2024": -14.343486324971309,
              "2025": -623.3755960762282
            },
            "positive_years": 0,
            "best_incremental_month": 156.90526423315532,
            "delta_without_best_month": -1370.1820831149835,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.04682539682539688,
        "delta10": -1173.3200317976534,
        "worstDD": -9.00529828997393
      },
      {
        "id": "S706",
        "strategy": "N204ManageR706",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11521.15599733508,
            "delta": -1535.4589177425842,
            "delta_seed": -1535.4589177425842,
            "plus10": 9462.138626543396,
            "delta10": -1469.0711170024679,
            "dd": -8.929296380353158,
            "counts": {
              "Mfull": "37/61",
              "Mall": "37/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.0626984126984127,
            "modified_exits": 28,
            "annual_delta_MTM": {
              "2021": -320.54476014751526,
              "2022": -242.48891655352782,
              "2023": -2.785071494685326,
              "2024": -287.59404923105103,
              "2025": -682.0461203157829
            },
            "positive_years": 0,
            "best_incremental_month": 159.96661545817915,
            "delta_without_best_month": -1695.4255332007633,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 11716.483213907975,
            "delta": -1522.959165938817,
            "delta_seed": -1522.959165938817,
            "plus10": 9549.649290109015,
            "delta10": -1453.7661742713717,
            "dd": -9.035647991860984,
            "counts": {
              "Mfull": "37/61",
              "Mall": "37/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0626984126984127,
            "modified_exits": 28,
            "annual_delta_MTM": {
              "2021": -306.833144690052,
              "2022": -239.76347287699355,
              "2023": -16.514618068811615,
              "2024": -289.0255790904048,
              "2025": -670.822351212566
            },
            "positive_years": 0,
            "best_incremental_month": 160.5643925227596,
            "delta_without_best_month": -1683.5235584615766,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.0626984126984127,
        "delta10": -1469.0711170024679,
        "worstDD": -9.035647991860984
      }
    ],
    "eligible": [],
    "selected": null
  },
  "paths": {
    "O700B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 260,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 39.324442829776444,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 264,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    },
    "O700C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 267,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 39.32444282977622,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 271,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    },
    "S701B": {
      "counts": {
        "current": 266,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 256,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": true,
        "matched": 266,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 4
    },
    "S701C": {
      "counts": {
        "current": 273,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 263,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": true,
        "matched": 273,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 4
    },
    "S702B": {
      "counts": {
        "current": 265,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 239,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 21
    },
    "S702C": {
      "counts": {
        "current": 272,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 246,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 21
    },
    "S703B": {
      "counts": {
        "current": 265,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 236,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 24
    },
    "S703C": {
      "counts": {
        "current": 272,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 243,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 24
    },
    "S704B": {
      "counts": {
        "current": 273,
        "reference": 273,
        "retained": 258,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 245,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 258,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 262,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 263,
        "max_abs_economic_field_delta": 4019,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": true,
        "matched": 273,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 13
    },
    "S704C": {
      "counts": {
        "current": 280,
        "reference": 280,
        "retained": 265,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 265,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 269,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 270,
        "max_abs_economic_field_delta": 4019,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": true,
        "matched": 280,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 13
    },
    "S705B": {
      "counts": {
        "current": 275,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 248,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 261,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 25
    },
    "S705C": {
      "counts": {
        "current": 282,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 255,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 268,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 25
    },
    "S706B": {
      "counts": {
        "current": 275,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 245,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 261,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 28
    },
    "S706C": {
      "counts": {
        "current": 282,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 268,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 28
    }
  }
}
```
