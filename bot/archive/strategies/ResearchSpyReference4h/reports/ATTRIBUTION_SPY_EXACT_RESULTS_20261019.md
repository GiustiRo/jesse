# Atribución SPY —17 filas exactas para consolidación

Todos los17 backtests finished, snapshots completos reconciliados por run_analysis. DDmotor/CAGR en porcentaje según motor; timeexposure es fracción temporal de ventana; entrynotionaltime=sum(entryprice×abs(qty)×hold_ms)/(10000×window_ms), aproximación a precio de entrada, NO MTM. Stress5/10 añade5/10bpsRT sobre mismosfills/sizes; cohortes por cierre NO retornos MTM. PFnull enE3 expresa ausencia de pérdidas observadas en un solo trade, no potencia infinita. Controls predefinidos, semillas no seleccionadas.

```json
[
  {
    "id": "798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "control": "C0",
    "name": "AttrSpyC0",
    "dashboard_url": "http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "N": 31,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
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
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
    "control": "Cq",
    "name": "AttrSpyCqFreshLimit",
    "dashboard_url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "N": 31,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
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
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "control": "E1",
    "name": "AttrSpyE1NoBE",
    "dashboard_url": "http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "N": 31,
    "timeexposure": 0.15264093244584573,
    "entrynotionaltime": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "cohorts_closing_trades_NOT_MTM": {
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
    "mean_hours": 224.88440860215056,
    "max_hours": 837.9666666666667,
    "entry_turnover_initial_equity": 31.77872286098001,
    "roundtrip_turnover_initial_equity": 63.66122804607744,
    "net_bps_entry": 23.64310605728177,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "control": "E2",
    "name": "AttrSpyE2NoTrail",
    "dashboard_url": "http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "net": 4889.748865865099,
    "fees": 57.427905819458054,
    "PF": 11.776888992472053,
    "DDmotor": -20.724256024947575,
    "CAGR": 7.934483102177947,
    "N": 8,
    "timeexposure": 0.859536842412565,
    "entrynotionaltime": 0.5908738437924608,
    "stress5": 4857.844473743178,
    "stress10": 4825.940081621257,
    "exbest": -450.6854868412511,
    "ex3": -453.7254553963321,
    "cohorts_closing_trades_NOT_MTM": {
      "2022": {
        "n": 3,
        "net": -187.99235532052916,
        "fee": 12.42438996214873
      },
      "2023": {
        "n": 4,
        "net": -262.69313152072164,
        "fee": 34.06176356365932
      },
      "2025": {
        "n": 1,
        "net": 5340.43435270635,
        "fee": 10.941752293650001
      }
    },
    "mean_hours": 4907.095833333334,
    "max_hours": 18683.966666666667,
    "entry_turnover_initial_equity": 6.1335195858,
    "roundtrip_turnover_initial_equity": 12.761756848768457,
    "net_bps_entry": 797.2174536110697,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "LIMIT": 6,
      "MARKET": 2
    },
    "exit_order_types": {
      "STOP": 7,
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  },
  {
    "id": "1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "control": "E3",
    "name": "AttrSpyE3InitialStop",
    "dashboard_url": "http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "net": 3485.34533747049,
    "fees": 4.83561912951,
    "PF": null,
    "DDmotor": -11.060009660496705,
    "CAGR": 5.902901610981659,
    "N": 1,
    "timeexposure": 0.9886100893326327,
    "entrynotionaltime": 0.3586499123691498,
    "stress5": 3482.65888239854,
    "stress10": 3479.97242732659,
    "exbest": 0,
    "ex3": 0,
    "cohorts_closing_trades_NOT_MTM": {
      "2025": {
        "n": 1,
        "net": 3485.34533747049,
        "fee": 4.83561912951
      }
    },
    "mean_hours": 45151.8,
    "max_hours": 45151.8,
    "entry_turnover_initial_equity": 0.36278196656000006,
    "roundtrip_turnover_initial_equity": 1.07458202878,
    "net_bps_entry": 9607.272849087589,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "LIMIT": 1
    },
    "exit_order_types": {
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  },
  {
    "id": "0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "control": "E4",
    "name": "AttrSpyE4Stop72h",
    "dashboard_url": "http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "net": -28.867539957479785,
    "fees": 406.4284583989386,
    "PF": 0.9806463373785479,
    "DDmotor": -7.4718587007506,
    "CAGR": -0.05543334143435219,
    "N": 44,
    "timeexposure": 0.058476747241198106,
    "entrynotionaltime": 0.05938130511605465,
    "stress5": -254.66112795689014,
    "stress10": -480.45471595630033,
    "exbest": -215.9489723917068,
    "ex3": -483.5227560627142,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 26.039345991489554,
        "fee": 3.2782306085100004
      },
      "2021": {
        "n": 6,
        "net": 209.7220152445956,
        "fee": 61.643415955410006
      },
      "2022": {
        "n": 7,
        "net": -156.17598975300376,
        "fee": 38.86040881712886
      },
      "2023": {
        "n": 11,
        "net": -287.6358666864437,
        "fee": 110.59897304518144
      },
      "2024": {
        "n": 13,
        "net": 81.13991510628415,
        "fee": 141.23875015793888
      },
      "2025": {
        "n": 6,
        "net": 98.04304013959845,
        "fee": 50.80867981476946
      }
    },
    "mean_hours": 60.69886363636364,
    "max_hours": 117.98333333333333,
    "entry_turnover_initial_equity": 45.13983955396,
    "roundtrip_turnover_initial_equity": 90.31743519976413,
    "net_bps_entry": -0.6395135703345076,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "LIMIT": 34,
      "MARKET": 10
    },
    "exit_order_types": {
      "MARKET": 29,
      "STOP": 15
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "control": "M",
    "name": "AttrSpyMarket",
    "dashboard_url": "http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "net": 151.6012639172099,
    "fees": 336.73029237147995,
    "PF": 1.074122772361648,
    "DDmotor": -7.718707541843617,
    "CAGR": 0.28900965265155065,
    "N": 38,
    "timeexposure": 0.15996051556022653,
    "entrynotionaltime": 0.1446681109984161,
    "stress5": -35.47112073361228,
    "stress10": -222.54350538443452,
    "exbest": -224.7296691424284,
    "ex3": -864.90548009341,
    "cohorts_closing_trades_NOT_MTM": {
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
    },
    "mean_hours": 192.25570175438597,
    "max_hours": 842.1666666666666,
    "entry_turnover_initial_equity": 37.390060352350005,
    "roundtrip_turnover_initial_equity": 74.82895386032888,
    "net_bps_entry": 4.054587301774217,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "MARKET": 38
    },
    "exit_order_types": {
      "STOP": 37,
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  },
  {
    "id": "83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "control": "R01",
    "name": "AttrSpyR01",
    "dashboard_url": "http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "net": -81.60081391564947,
    "fees": 111.34571187400127,
    "PF": 0.8749054563501013,
    "DDmotor": -4.932604907914506,
    "CAGR": -0.15703098268418092,
    "N": 11,
    "timeexposure": 0.043761677468324864,
    "entrynotionaltime": 0.03730957274807745,
    "stress5": -143.45954273453907,
    "stress10": -205.3182715534287,
    "exbest": -293.7253850607877,
    "ex3": -582.4585689585219,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 168.79131639148233,
        "fee": 3.5746040598531006
      },
      "2021": {
        "n": 2,
        "net": 32.17664901745039,
        "fee": 24.600899852491473
      },
      "2022": {
        "n": 1,
        "net": -93.53347295188989,
        "fee": 7.588225023242109
      },
      "2023": {
        "n": 5,
        "net": -8.704614518796092,
        "fee": 56.99794337516536
      },
      "2024": {
        "n": 2,
        "net": -180.3306918538962,
        "fee": 18.584039563249206
      }
    },
    "mean_hours": 181.69848484848487,
    "max_hours": 822.1666666666666,
    "entry_turnover_initial_equity": 12.37025851888,
    "roundtrip_turnover_initial_equity": 24.743491527555832,
    "net_bps_entry": -6.5965326263074395,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 11
    },
    "exit_order_types": {
      "STOP": 11
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "control": "R02",
    "name": "AttrSpyR02",
    "dashboard_url": "http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "net": 1054.7187970764467,
    "fees": 133.5756319487213,
    "PF": 2.9998802602602157,
    "DDmotor": -3.2489130528813193,
    "CAGR": 1.941860175438448,
    "N": 13,
    "timeexposure": 0.061050534244175864,
    "entrynotionaltime": 0.06322744806499223,
    "stress5": 980.5101126604901,
    "stress10": 906.3014282445337,
    "exbest": 517.1645402448297,
    "ex3": -167.29651607237975,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 2,
        "net": 513.384189900414,
        "fee": 17.92400678941042
      },
      "2022": {
        "n": 2,
        "net": 142.17493275326405,
        "fee": 11.989097976748505
      },
      "2023": {
        "n": 4,
        "net": 676.3404909230329,
        "fee": 44.64688774368002
      },
      "2024": {
        "n": 4,
        "net": -236.2084088427781,
        "fee": 51.37663478595442
      },
      "2025": {
        "n": 1,
        "net": -40.97240765748627,
        "fee": 7.639004652927948
      }
    },
    "mean_hours": 214.48461538461538,
    "max_hours": 566.1,
    "entry_turnover_initial_equity": 14.782322161739998,
    "roundtrip_turnover_initial_equity": 29.683473766382516,
    "net_bps_entry": 71.3500074978949,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 13
    },
    "exit_order_types": {
      "STOP": 13
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "control": "R03",
    "name": "AttrSpyR03",
    "dashboard_url": "http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "net": 153.75236671948676,
    "fees": 145.44455054663976,
    "PF": 1.1755046430877696,
    "DDmotor": -5.546613627792163,
    "CAGR": 0.29308530234914976,
    "N": 16,
    "timeexposure": 0.0611096514275705,
    "entrynotionaltime": 0.05947272629465539,
    "stress5": 72.94983863802037,
    "stress10": -7.852689443446081,
    "exbest": -276.5115457456816,
    "ex3": -647.7774062496329,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 3,
        "net": 219.5424666053639,
        "fee": 30.265958261370027
      },
      "2022": {
        "n": 3,
        "net": 52.867882487434585,
        "fee": 17.189810725685902
      },
      "2023": {
        "n": 5,
        "net": 118.59284374369355,
        "fee": 49.85814617339269
      },
      "2024": {
        "n": 3,
        "net": -53.66485280241129,
        "fee": 28.19129766212687
      },
      "2025": {
        "n": 2,
        "net": -183.5859733145939,
        "fee": 19.93933772406426
      }
    },
    "mean_hours": 174.4375,
    "max_hours": 655.9,
    "entry_turnover_initial_equity": 16.14554577043,
    "roundtrip_turnover_initial_equity": 32.32101123258661,
    "net_bps_entry": 9.522896835180314,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 16
    },
    "exit_order_types": {
      "STOP": 16
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "a657dc36-13bd-440f-a423-917ab3caeb8c",
    "control": "R04",
    "name": "AttrSpyR04",
    "dashboard_url": "http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c",
    "net": -348.5522602051562,
    "fees": 138.5202226466887,
    "PF": 0.6337677065518231,
    "DDmotor": -6.36507763263131,
    "CAGR": -0.6781506913298374,
    "N": 16,
    "timeexposure": 0.04999635079114848,
    "entrynotionaltime": 0.0494161538196295,
    "stress5": -425.50793945331657,
    "stress10": -502.4636187014769,
    "exbest": -595.0770116026313,
    "ex3": -879.0400706838409,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 1,
        "net": -87.53574379017371,
        "fee": 11.183231415431367
      },
      "2022": {
        "n": 3,
        "net": -103.60912490261549,
        "fee": 16.54516014454887
      },
      "2023": {
        "n": 4,
        "net": -37.84200265865744,
        "fee": 36.797028561676356
      },
      "2024": {
        "n": 5,
        "net": -193.6776157233023,
        "fee": 45.618157614100866
      },
      "2025": {
        "n": 3,
        "net": 74.11222686959277,
        "fee": 28.376644910931233
      }
    },
    "mean_hours": 142.71458333333334,
    "max_hours": 679.9666666666667,
    "entry_turnover_initial_equity": 15.40163745151,
    "roundtrip_turnover_initial_equity": 30.782271699264157,
    "net_bps_entry": -22.630857355429022,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 16
    },
    "exit_order_types": {
      "STOP": 16
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "control": "R05",
    "name": "AttrSpyR05",
    "dashboard_url": "http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "net": 143.1550705133505,
    "fees": 92.06246981327698,
    "PF": 1.4271005507452341,
    "DDmotor": -3.172735630771384,
    "CAGR": 0.2730000721026027,
    "N": 9,
    "timeexposure": 0.037578822911192855,
    "entrynotionaltime": 0.0412426233964772,
    "stress5": 92.00925395041884,
    "stress10": 40.863437387487146,
    "exbest": -156.39841665561738,
    "ex3": -310.33598206014244,
    "cohorts_closing_trades_NOT_MTM": {
      "2021": {
        "n": 2,
        "net": 258.6540164324854,
        "fee": 22.1566212339599
      },
      "2023": {
        "n": 4,
        "net": -197.05126433626992,
        "fee": 40.84671927921433
      },
      "2024": {
        "n": 1,
        "net": 24.842865786257544,
        "fee": 9.983253560285942
      },
      "2025": {
        "n": 2,
        "net": 56.70945263087748,
        "fee": 19.07587573981681
      }
    },
    "mean_hours": 190.7,
    "max_hours": 518.1,
    "entry_turnover_initial_equity": 10.217402435570001,
    "roundtrip_turnover_initial_equity": 20.45832662517266,
    "net_bps_entry": 14.010906530898943,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "MARKET": 9
    },
    "exit_order_types": {
      "STOP": 8,
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  },
  {
    "id": "da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "control": "U01",
    "name": "AttrSpyU01",
    "dashboard_url": "http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "net": 1874.981553550459,
    "fees": 644.7764810969313,
    "PF": 1.4081758729933123,
    "DDmotor": -11.630293408060766,
    "CAGR": 3.3510228184844726,
    "N": 72,
    "timeexposure": 0.30974046826647983,
    "entrynotionaltime": 0.26339021303636406,
    "stress5": 1516.7723973854968,
    "stress10": 1158.5632412205346,
    "exbest": 1036.1887244199975,
    "ex3": -216.22479047230763,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 168.79131639148233,
        "fee": 3.5746040598531006
      },
      "2021": {
        "n": 11,
        "net": 667.5123662181792,
        "fee": 86.12348444678923
      },
      "2022": {
        "n": 14,
        "net": 566.2761995069535,
        "fee": 72.37452116244124
      },
      "2023": {
        "n": 12,
        "net": 1427.4810650632614,
        "fee": 130.246140694571
      },
      "2024": {
        "n": 18,
        "net": -1044.8584835174588,
        "fee": 211.99855944596786
      },
      "2025": {
        "n": 16,
        "net": 89.77908988804113,
        "fee": 140.45917128730892
      }
    },
    "mean_hours": 196.4787037037037,
    "max_hours": 862.9166666666666,
    "entry_turnover_initial_equity": 71.51584333126,
    "roundtrip_turnover_initial_equity": 143.28366246598475,
    "net_bps_entry": 26.217708779096416,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "MARKET": 72
    },
    "exit_order_types": {
      "STOP": 71,
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  },
  {
    "id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
    "control": "U02",
    "name": "AttrSpyU02",
    "dashboard_url": "http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b",
    "net": 2572.1409833508283,
    "fees": 575.5481925280554,
    "PF": 1.6407248804879624,
    "DDmotor": -5.493244162762901,
    "CAGR": 4.4881242819657,
    "N": 70,
    "timeexposure": 0.31994694050329886,
    "entrynotionaltime": 0.2605476399199419,
    "stress5": 2252.3919875019083,
    "stress10": 1932.6429916529887,
    "exbest": 2005.5306829129077,
    "ex3": 959.5942650886718,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 22.87548955378361,
        "fee": 7.34693468032535
      },
      "2021": {
        "n": 12,
        "net": 703.1149467662979,
        "fee": 93.41472079159105
      },
      "2022": {
        "n": 12,
        "net": -160.8586197508117,
        "fee": 67.14035124088052
      },
      "2023": {
        "n": 16,
        "net": 533.4561286188031,
        "fee": 138.97121450675652
      },
      "2024": {
        "n": 14,
        "net": 1340.2552945944208,
        "fee": 133.58314860732077
      },
      "2025": {
        "n": 15,
        "net": 133.29774356833505,
        "fee": 135.0918227011813
      }
    },
    "mean_hours": 208.75166666666667,
    "max_hours": 974.1,
    "entry_turnover_initial_equity": 63.79241471099,
    "roundtrip_turnover_initial_equity": 127.89959833956789,
    "net_bps_entry": 40.32048316408543,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 70
    },
    "exit_order_types": {
      "STOP": 70
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "63dd9d81-c7bf-417b-823f-728977051fd8",
    "control": "U03",
    "name": "AttrSpyU03",
    "dashboard_url": "http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8",
    "net": -440.27560690769474,
    "fees": 580.7699584621895,
    "PF": 0.9008425504447655,
    "DDmotor": -14.787161148432038,
    "CAGR": -0.8598948861797129,
    "N": 74,
    "timeexposure": 0.2673797220762539,
    "entrynotionaltime": 0.2281749269603607,
    "stress5": -762.925583831133,
    "stress10": -1085.5755607545716,
    "exbest": -1050.492371257966,
    "ex3": -2029.0513462937815,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": 309.4219660632779,
        "fee": 3.2929018880180827
      },
      "2021": {
        "n": 16,
        "net": 571.5593222133468,
        "fee": 127.9767386767005
      },
      "2022": {
        "n": 17,
        "net": -784.684385785174,
        "fee": 94.72499574865355
      },
      "2023": {
        "n": 16,
        "net": 116.3945247435512,
        "fee": 143.34163632363024
      },
      "2024": {
        "n": 13,
        "net": -61.59589831361469,
        "fee": 121.45753048723812
      },
      "2025": {
        "n": 11,
        "net": -591.3711358290823,
        "fee": 89.97615533794898
      }
    },
    "mean_hours": 165.0238738738739,
    "max_hours": 870.1666666666666,
    "entry_turnover_initial_equity": 64.52297066711002,
    "roundtrip_turnover_initial_equity": 129.05999076937547,
    "net_bps_entry": -6.823548301568223,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 74
    },
    "exit_order_types": {
      "STOP": 74
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "4ac55781-679a-4d6d-a79a-320f162147b2",
    "control": "U04",
    "name": "AttrSpyU04",
    "dashboard_url": "http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2",
    "net": -1075.4610284377702,
    "fees": 538.870086556073,
    "PF": 0.7409558002321476,
    "DDmotor": -18.079394862500987,
    "CAGR": -2.1586953401382947,
    "N": 79,
    "timeexposure": 0.2590223039645005,
    "entrynotionaltime": 0.1822818730405191,
    "stress5": -1374.8332987466995,
    "stress10": -1674.2055690556292,
    "exbest": -1413.3304284421129,
    "ex3": -1973.5582185412673,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 4,
        "net": 301.1891491753476,
        "fee": 26.020701424259823
      },
      "2021": {
        "n": 16,
        "net": -861.8818616427093,
        "fee": 133.93886975555077
      },
      "2022": {
        "n": 19,
        "net": -550.0410616466902,
        "fee": 86.15350279455656
      },
      "2023": {
        "n": 14,
        "net": 241.2840583054148,
        "fee": 105.41329842695956
      },
      "2024": {
        "n": 15,
        "net": -289.9450852269973,
        "fee": 117.30496002695999
      },
      "2025": {
        "n": 11,
        "net": 83.93377259786406,
        "fee": 70.03875412778655
      }
    },
    "mean_hours": 149.7476793248945,
    "max_hours": 656.4666666666667,
    "entry_turnover_initial_equity": 59.90128360888001,
    "roundtrip_turnover_initial_equity": 119.7489081235718,
    "net_bps_entry": -17.953889526974002,
    "terminal_liquidations": 0,
    "entry_order_types": {
      "MARKET": 79
    },
    "exit_order_types": {
      "STOP": 79
    },
    "engine_open_count_preterminal": 0
  },
  {
    "id": "37c6ae11-78b0-49c6-9b58-4c9190542841",
    "control": "U05",
    "name": "AttrSpyU05",
    "dashboard_url": "http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841",
    "net": 75.7426645169086,
    "fees": 499.6762652877322,
    "PF": 1.0200818630649156,
    "DDmotor": -16.98244814676453,
    "CAGR": 0.14483362605641759,
    "N": 70,
    "timeexposure": 0.26611125707946515,
    "entrynotionaltime": 0.2103348483911586,
    "stress5": -201.85526064294223,
    "stress10": -479.45318580279366,
    "exbest": -305.6646422200623,
    "ex3": -995.5594235388447,
    "cohorts_closing_trades_NOT_MTM": {
      "2020": {
        "n": 2,
        "net": -167.61224639513162,
        "fee": 14.450341180313332
      },
      "2021": {
        "n": 12,
        "net": 841.3276411019285,
        "fee": 97.3064295509638
      },
      "2022": {
        "n": 17,
        "net": -659.5436362726308,
        "fee": 80.59640256868323
      },
      "2023": {
        "n": 14,
        "net": -461.57438645627406,
        "fee": 113.61266328322213
      },
      "2024": {
        "n": 13,
        "net": 84.57493780062475,
        "fee": 110.86948800387205
      },
      "2025": {
        "n": 12,
        "net": 438.570354738392,
        "fee": 82.84094070067756
      }
    },
    "mean_hours": 173.6261904761905,
    "max_hours": 653.7166666666667,
    "entry_turnover_initial_equity": 55.49081408547999,
    "roundtrip_turnover_initial_equity": 111.03917006394049,
    "net_bps_entry": 1.364958610991577,
    "terminal_liquidations": 1,
    "entry_order_types": {
      "MARKET": 70
    },
    "exit_order_types": {
      "STOP": 69,
      "MARKET": 1
    },
    "engine_open_count_preterminal": 1
  }
]
```