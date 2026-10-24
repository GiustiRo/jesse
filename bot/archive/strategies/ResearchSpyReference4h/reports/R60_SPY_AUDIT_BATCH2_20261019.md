# R60 SPY — lote2 completo y grupos de igualdad

Jobe16f88c74fc3409bb25b796d88f7ff6c succeeded sobre Cqexistente+S06..10+S04/S05 para comparación de trayectorias. Sin nuevosfulls. Costes/PnL/balance y tamaño reconciliados. Resumen íntegro JSON de34514bytes (<50KB), no truncado. Campos económicos completos y curva numérica exacta comparados por par; grupos repetidos no son evidencia independiente. No inferir armings rechazados ni causalidad por intersección. Cohortes cierre NO retornosMTM. Root audita dayclose aparte.

```json
{
  "metrics": {
    "Cq": {
      "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
      "CAGR_engine_pct": 1.3992310944554776,
      "Sharpe_engine": 0.4581998683996086,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6971.416666666667,
      "fraction_time_open": 0.15264093244584573,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
      "entry_turnover_initial_equity": 31.77872286098001,
      "roundtrip_turnover_initial_equity": 63.66122804607744,
      "net_bps_entry": 23.64310605728177,
      "net_per_exposure_entry_time_measure": 0.5310430365806986,
      "max_initial_gross_equity": 1.5989937330573134,
      "mean_hours": 224.88440860215056,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.1946448519213,
      "stress10_RT_samefills": 433.0415747367277,
      "net_without_top1": 349.57799671604494,
      "net_without_top3": -298.2237721588764,
      "net_without_top5": -757.536337350717,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 24,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S06": {
      "session_id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
      "CAGR_engine_pct": 1.3992310944554776,
      "Sharpe_engine": 0.4581998683996086,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6971.416666666667,
      "fraction_time_open": 0.15264093244584573,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
      "entry_turnover_initial_equity": 31.77872286098001,
      "roundtrip_turnover_initial_equity": 63.66122804607744,
      "net_bps_entry": 23.64310605728177,
      "net_per_exposure_entry_time_measure": 0.5310430365806986,
      "max_initial_gross_equity": 1.5989937330573134,
      "mean_hours": 224.88440860215056,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.1946448519213,
      "stress10_RT_samefills": 433.0415747367277,
      "net_without_top1": 349.57799671604494,
      "net_without_top3": -298.2237721588764,
      "net_without_top5": -757.536337350717,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 24,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S07": {
      "session_id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
      "n": 39,
      "net": 597.9379578325991,
      "gross_price": 948.4057648502217,
      "fee": 350.46780701762265,
      "PF": 1.3048982927072252,
      "return_pct": 5.97937957832599,
      "CAGR_engine_pct": 1.1201069472235758,
      "Sharpe_engine": 0.3377375270170746,
      "DD_engine_pct": -8.096205641424326,
      "hours_open": 8268.933333333332,
      "fraction_time_open": 0.1810503882758218,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.1655766793706388,
      "entry_turnover_initial_equity": 38.893447158159994,
      "roundtrip_turnover_initial_equity": 77.88173489280503,
      "net_bps_entry": 15.373745489853023,
      "net_per_exposure_entry_time_measure": 0.3611245014125036,
      "max_initial_gross_equity": 1.598997823764867,
      "mean_hours": 212.02393162393162,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 403.2336206005866,
      "stress10_RT_samefills": 208.529283368574,
      "net_without_top1": 198.3763364424717,
      "net_without_top3": -451.92482537426145,
      "net_without_top5": -995.1841837724453,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 137.97951328204002,
          "fee": 3.3286263618797642
        },
        "2021": {
          "n": 5,
          "net": 530.5196353485741,
          "fee": 46.31573518160858
        },
        "2022": {
          "n": 7,
          "net": -347.13703384618935,
          "fee": 43.86384649054997
        },
        "2023": {
          "n": 11,
          "net": 203.19320101426078,
          "fee": 103.96390267245903
        },
        "2024": {
          "n": 9,
          "net": 48.48226908108998,
          "fee": 96.92647166184433
        },
        "2025": {
          "n": 6,
          "net": 24.900372952823645,
          "fee": 56.06922464928094
        }
      },
      "entry_order_types": {
        "LIMIT": 32,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 39
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 08:01": 1,
        "Fri 12:06": 1,
        "Fri 07:02": 1,
        "Tue 08:57": 1,
        "Tue 08:02": 1,
        "Tue 07:44": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Mon 16:17": 1,
        "Thu 16:10": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 06:06": 1,
        "Mon 08:34": 1,
        "Fri 16:00": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Thu 08:02": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Thu 14:32": 1,
        "Fri 16:06": 1,
        "Tue 12:06": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1,
        "Fri 09:38": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S08": {
      "session_id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
      "n": 24,
      "net": 686.0308434052209,
      "gross_price": 905.0091570013215,
      "fee": 218.9783135961006,
      "PF": 1.555117092021026,
      "return_pct": 6.860308434052209,
      "CAGR_engine_pct": 1.2807852033825728,
      "Sharpe_engine": 0.47295715146124506,
      "DD_engine_pct": -5.892075684490239,
      "hours_open": 5491.333333333333,
      "fraction_time_open": 0.12023413323991358,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.113510417707401,
      "entry_turnover_initial_equity": 24.28567327505,
      "roundtrip_turnover_initial_equity": 48.661847465800136,
      "net_bps_entry": 28.248376548407986,
      "net_per_exposure_entry_time_measure": 0.6043769878229344,
      "max_initial_gross_equity": 1.5989913508475446,
      "mean_hours": 228.80555555555554,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 564.3762247407205,
      "stress10_RT_samefills": 442.7216060762202,
      "net_without_top1": 290.36587299061233,
      "net_without_top3": -360.3540051435342,
      "net_without_top5": -732.1203419936227,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 137.97951328204002,
          "fee": 3.3286263618797642
        },
        "2021": {
          "n": 2,
          "net": 427.64749313911625,
          "fee": 19.751448193079487
        },
        "2022": {
          "n": 5,
          "net": -400.45703000137615,
          "fee": 32.0045898020403
        },
        "2023": {
          "n": 7,
          "net": 231.8844849968417,
          "fee": 68.59311195120661
        },
        "2024": {
          "n": 6,
          "net": 83.80710197659216,
          "fee": 70.5014641882642
        },
        "2025": {
          "n": 3,
          "net": 205.16928001200694,
          "fee": 24.799073099630235
        }
      },
      "entry_order_types": {
        "LIMIT": 19,
        "MARKET": 5
      },
      "exit_order_types": {
        "STOP": 24
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Fri 12:33": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Tue 16:01": 1,
        "Tue 12:00": 1,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Wed 16:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Thu 16:48": 1,
        "Fri 08:23": 1,
        "Fri 14:01": 1,
        "Wed 16:10": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S09": {
      "session_id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
      "CAGR_engine_pct": 1.3992310944554776,
      "Sharpe_engine": 0.4581998683996086,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6971.416666666667,
      "fraction_time_open": 0.15264093244584573,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
      "entry_turnover_initial_equity": 31.77872286098001,
      "roundtrip_turnover_initial_equity": 63.66122804607744,
      "net_bps_entry": 23.64310605728177,
      "net_per_exposure_entry_time_measure": 0.5310430365806986,
      "max_initial_gross_equity": 1.5989937330573134,
      "mean_hours": 224.88440860215056,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.1946448519213,
      "stress10_RT_samefills": 433.0415747367277,
      "net_without_top1": 349.57799671604494,
      "net_without_top3": -298.2237721588764,
      "net_without_top5": -757.536337350717,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 24,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S10": {
      "session_id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
      "n": 31,
      "net": 751.7119522395761,
      "gross_price": 1038.4827988852448,
      "fee": 286.7708466456683,
      "PF": 1.4933836938880178,
      "return_pct": 7.517119522395761,
      "CAGR_engine_pct": 1.399889971337509,
      "Sharpe_engine": 0.4584228742218906,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6966.516666666666,
      "fraction_time_open": 0.15253364570561104,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14140980381744386,
      "entry_turnover_initial_equity": 31.811503265130007,
      "roundtrip_turnover_initial_equity": 63.726854810148524,
      "net_bps_entry": 23.630192700247548,
      "net_per_exposure_entry_time_measure": 0.5315840429352519,
      "max_initial_gross_equity": 1.5989988513462066,
      "mean_hours": 224.72634408602153,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.394815214205,
      "stress10_RT_samefills": 433.0776781888338,
      "net_without_top1": 349.91625637837717,
      "net_without_top3": -297.899045359473,
      "net_without_top5": -757.2218010173673,
      "closed_trade_year_cohorts_NOT_MTM": {
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
          "net": 396.09988130755266,
          "fee": 89.40507957741823
        },
        "2024": {
          "n": 8,
          "net": -22.5085097573902,
          "fee": 87.70929772822687
        },
        "2025": {
          "n": 5,
          "net": 119.72169164013778,
          "fee": 44.86091017023466
        }
      },
      "entry_order_types": {
        "LIMIT": 25,
        "MARKET": 6
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 08:30": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S04": {
      "session_id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
      "CAGR_engine_pct": 1.3992310944554776,
      "Sharpe_engine": 0.4581998683996086,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6971.416666666667,
      "fraction_time_open": 0.15264093244584573,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
      "entry_turnover_initial_equity": 31.77872286098001,
      "roundtrip_turnover_initial_equity": 63.66122804607744,
      "net_bps_entry": 23.64310605728177,
      "net_per_exposure_entry_time_measure": 0.5310430365806986,
      "max_initial_gross_equity": 1.5989937330573134,
      "mean_hours": 224.88440860215056,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.1946448519213,
      "stress10_RT_samefills": 433.0415747367277,
      "net_without_top1": 349.57799671604494,
      "net_without_top3": -298.2237721588764,
      "net_without_top5": -757.536337350717,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 24,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S05": {
      "session_id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
      "CAGR_engine_pct": 1.3992310944554776,
      "Sharpe_engine": 0.4581998683996086,
      "DD_engine_pct": -5.2131810594609025,
      "hours_open": 6971.416666666667,
      "fraction_time_open": 0.15264093244584573,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.14148527769141334,
      "entry_turnover_initial_equity": 31.77872286098001,
      "roundtrip_turnover_initial_equity": 63.66122804607744,
      "net_bps_entry": 23.64310605728177,
      "net_per_exposure_entry_time_measure": 0.5310430365806986,
      "max_initial_gross_equity": 1.5989937330573134,
      "mean_hours": 224.88440860215056,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 592.1946448519213,
      "stress10_RT_samefills": 433.0415747367277,
      "net_without_top1": 349.57799671604494,
      "net_without_top3": -298.2237721588764,
      "net_without_top5": -757.536337350717,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 24,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 31
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Mon 16:00": 1,
        "Thu 08:00": 1,
        "Fri 16:04": 2,
        "Fri 12:00": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    }
  },
  "pairs": {
    "Cq__S06": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S07": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 26,
      "total_a": 31,
      "total_b": 39,
      "only_a": 5,
      "only_b": 13,
      "sum_normalized_net_a": 0.0988574386150907,
      "sum_normalized_net_b": 0.09885743859037492,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S08": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 19,
      "total_a": 31,
      "total_b": 24,
      "only_a": 12,
      "only_b": 5,
      "sum_normalized_net_a": 0.09451806615145833,
      "sum_normalized_net_b": 0.09451806513352962,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S09": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S10": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 30,
      "total_a": 31,
      "total_b": 31,
      "only_a": 1,
      "only_b": 1,
      "sum_normalized_net_a": 0.10937932420728634,
      "sum_normalized_net_b": 0.10937932420728606,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S04": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S05": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S07": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 26,
      "total_a": 31,
      "total_b": 39,
      "only_a": 5,
      "only_b": 13,
      "sum_normalized_net_a": 0.0988574386150907,
      "sum_normalized_net_b": 0.09885743859037492,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S08": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 19,
      "total_a": 31,
      "total_b": 24,
      "only_a": 12,
      "only_b": 5,
      "sum_normalized_net_a": 0.09451806615145833,
      "sum_normalized_net_b": 0.09451806513352962,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S09": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S10": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 30,
      "total_a": 31,
      "total_b": 31,
      "only_a": 1,
      "only_b": 1,
      "sum_normalized_net_a": 0.10937932420728634,
      "sum_normalized_net_b": 0.10937932420728606,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S04": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S06__S05": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S07__S08": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 16,
      "total_a": 39,
      "total_b": 24,
      "only_a": 23,
      "only_b": 8,
      "sum_normalized_net_a": 0.10600996698027762,
      "sum_normalized_net_b": 0.10600996598706514,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S07__S09": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 26,
      "total_a": 39,
      "total_b": 31,
      "only_a": 13,
      "only_b": 5,
      "sum_normalized_net_a": 0.09885743859037492,
      "sum_normalized_net_b": 0.0988574386150907,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S07__S10": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 25,
      "total_a": 39,
      "total_b": 31,
      "only_a": 14,
      "only_b": 6,
      "sum_normalized_net_a": 0.11067617675663512,
      "sum_normalized_net_b": 0.11067617678135065,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S07__S04": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 26,
      "total_a": 39,
      "total_b": 31,
      "only_a": 13,
      "only_b": 5,
      "sum_normalized_net_a": 0.09885743859037492,
      "sum_normalized_net_b": 0.0988574386150907,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S07__S05": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 26,
      "total_a": 39,
      "total_b": 31,
      "only_a": 13,
      "only_b": 5,
      "sum_normalized_net_a": 0.09885743859037492,
      "sum_normalized_net_b": 0.0988574386150907,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S08__S09": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 19,
      "total_a": 24,
      "total_b": 31,
      "only_a": 5,
      "only_b": 12,
      "sum_normalized_net_a": 0.09451806513352962,
      "sum_normalized_net_b": 0.09451806615145833,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S08__S10": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 18,
      "total_a": 24,
      "total_b": 31,
      "only_a": 6,
      "only_b": 13,
      "sum_normalized_net_a": 0.10633680329978981,
      "sum_normalized_net_b": 0.10633680431771815,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S08__S04": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 19,
      "total_a": 24,
      "total_b": 31,
      "only_a": 5,
      "only_b": 12,
      "sum_normalized_net_a": 0.09451806513352962,
      "sum_normalized_net_b": 0.09451806615145833,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S08__S05": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 19,
      "total_a": 24,
      "total_b": 31,
      "only_a": 5,
      "only_b": 12,
      "sum_normalized_net_a": 0.09451806513352962,
      "sum_normalized_net_b": 0.09451806615145833,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S09__S10": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 30,
      "total_a": 31,
      "total_b": 31,
      "only_a": 1,
      "only_b": 1,
      "sum_normalized_net_a": 0.10937932420728634,
      "sum_normalized_net_b": 0.10937932420728606,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S09__S04": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S09__S05": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S10__S04": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 30,
      "total_a": 31,
      "total_b": 31,
      "only_a": 1,
      "only_b": 1,
      "sum_normalized_net_a": 0.10937932420728606,
      "sum_normalized_net_b": 0.10937932420728634,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S10__S05": {
      "full_trade_economic_path_equal": false,
      "equity_curve_exact_equal": false,
      "common_entries": 30,
      "total_a": 31,
      "total_b": 31,
      "only_a": 1,
      "only_b": 1,
      "sum_normalized_net_a": 0.10937932420728606,
      "sum_normalized_net_b": 0.10937932420728634,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S04__S05": {
      "full_trade_economic_path_equal": true,
      "equity_curve_exact_equal": true,
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    }
  }
}
```

Pares completos individuales pairs_*.json; fuente R60_SPY_PATH_IDENTITY_ANALYSIS_ADDENDUM_20261019.md. Dashboards:

S06

Dashboard: http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2

S07

Dashboard: http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60

S08

Dashboard: http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb

S09

Dashboard: http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f

S10

Dashboard: http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a

S04

Dashboard: http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35

S05

Dashboard: http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134
