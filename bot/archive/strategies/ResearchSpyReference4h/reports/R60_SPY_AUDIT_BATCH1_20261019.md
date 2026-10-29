# R60 SPY — lote1 completo

Job50bf614e29144b658757ad2d275e77ca succeeded sobre Cqexistente+S01..S05. Costes/PnL/balance y tamaño reconciliados. Resumen íntegro JSON de21366bytes (<50KB), no truncado. Datos de cohortes por cierre NO retornosMTM; root audita dayclose aparte. Comparaciones de pares por filltimestamp exacto son condicionales a ocupación, no causales. No parámetros cambiados tras resultados.

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
    "S01": {
      "session_id": "d404c47e-025a-4789-b1a8-b054402f6c21",
      "n": 23,
      "net": 82.9535236572004,
      "gross_price": 294.97025093247,
      "fee": 212.01672727526963,
      "PF": 1.06596462316971,
      "return_pct": 0.829535236572004,
      "CAGR_engine_pct": 0.15857616602510394,
      "Sharpe_engine": 0.07648903056030368,
      "DD_engine_pct": -6.654984999592428,
      "hours_open": 5060.75,
      "fraction_time_open": 0.11080640217200911,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.09984102700401203,
      "entry_turnover_initial_equity": 23.54266562915,
      "roundtrip_turnover_initial_equity": 47.11482828339325,
      "net_bps_entry": 3.5235399832756924,
      "net_per_exposure_entry_time_measure": 0.08308560733641793,
      "max_initial_gross_equity": 1.5990052596773574,
      "mean_hours": 220.0326086956522,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": -34.83354705128272,
      "stress10_RT_samefills": -152.62061775976576,
      "net_without_top1": -251.68933926337243,
      "net_without_top3": -690.9944515622414,
      "net_without_top5": -996.179126689415,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 137.97951328204002,
          "fee": 3.3286263618797642
        },
        "2021": {
          "n": 2,
          "net": 246.54068155404738,
          "fee": 20.392452668440114
        },
        "2022": {
          "n": 4,
          "net": -118.313081514564,
          "fee": 22.925577513149364
        },
        "2023": {
          "n": 6,
          "net": -85.92178478984678,
          "fee": 61.77352323935228
        },
        "2024": {
          "n": 7,
          "net": -157.96197597635802,
          "fee": 77.75021022473177
        },
        "2025": {
          "n": 3,
          "net": 60.63017110188187,
          "fee": 25.84633726771632
        }
      },
      "entry_order_types": {
        "LIMIT": 23
      },
      "exit_order_types": {
        "STOP": 23
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Fri 17:01": 1,
        "Fri 18:02": 1,
        "Thu 16:06": 1,
        "Thu 08:30": 1,
        "Wed 15:20": 1,
        "Fri 16:04": 2,
        "Fri 14:31": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Fri 08:23": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 08:43": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S02": {
      "session_id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
      "n": 14,
      "net": 245.8742418595162,
      "gross_price": 371.23476326114366,
      "fee": 125.36052140162752,
      "PF": 1.3446510233072277,
      "return_pct": 2.458742418595162,
      "CAGR_engine_pct": 0.46697537512865317,
      "Sharpe_engine": 0.23228570468090567,
      "DD_engine_pct": -4.099687568281962,
      "hours_open": 3113.2,
      "fraction_time_open": 0.06816430197933088,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.06647236035378323,
      "entry_turnover_initial_equity": 13.91038508424,
      "roundtrip_turnover_initial_equity": 27.85789364480612,
      "net_bps_entry": 17.675588444929787,
      "net_per_exposure_entry_time_measure": 0.3698894405899074,
      "max_initial_gross_equity": 1.5197306613658572,
      "mean_hours": 222.37142857142857,
      "max_hours": 683.25,
      "stress5_RT_samefills": 176.22950774750092,
      "stress10_RT_samefills": 106.58477363548562,
      "net_without_top1": -73.85444125549776,
      "net_without_top3": -512.8090386653323,
      "net_without_top5": -711.102457632164,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2021": {
          "n": 2,
          "net": 232.82492507750962,
          "fee": 20.141113353764077
        },
        "2022": {
          "n": 4,
          "net": -279.5241368405673,
          "fee": 24.043099005974433
        },
        "2023": {
          "n": 2,
          "net": 100.95029262654408,
          "fee": 18.973196111221995
        },
        "2024": {
          "n": 4,
          "net": 36.653719086849826,
          "fee": 43.527720320823455
        },
        "2025": {
          "n": 2,
          "net": 154.9694419091799,
          "fee": 18.675392609843563
        }
      },
      "entry_order_types": {
        "LIMIT": 14
      },
      "exit_order_types": {
        "STOP": 14
      },
      "entry_clock_UTC": {
        "Tue 09:40": 1,
        "Tue 14:46": 1,
        "Tue 15:20": 1,
        "Tue 16:23": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Fri 17:01": 1,
        "Thu 16:06": 1,
        "Fri 14:31": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Mon 17:08": 1,
        "Tue 06:20": 1,
        "Wed 08:43": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "S03": {
      "session_id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
      "n": 30,
      "net": 743.9711828862412,
      "gross_price": 1020.6026345622242,
      "fee": 276.63145167598293,
      "PF": 1.4896904685510277,
      "return_pct": 7.4397118288624124,
      "CAGR_engine_pct": 1.3858836381329676,
      "Sharpe_engine": 0.4596199367125393,
      "DD_engine_pct": -6.132698354864685,
      "hours_open": 6595.95,
      "fraction_time_open": 0.14441999474513925,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.13718877951137115,
      "entry_turnover_initial_equity": 30.68579783227,
      "roundtrip_turnover_initial_equity": 61.473655927996234,
      "net_bps_entry": 24.244804940475145,
      "net_per_exposure_entry_time_measure": 0.5422973989097817,
      "max_initial_gross_equity": 1.5989575762900328,
      "mean_hours": 219.865,
      "max_hours": 837.9666666666667,
      "stress5_RT_samefills": 590.2870430662508,
      "stress10_RT_samefills": 436.6029032462603,
      "net_without_top1": 342.4612407364584,
      "net_without_top3": -302.32269970477955,
      "net_without_top5": -757.1897552588923,
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
          "net": -314.92014410268337,
          "fee": 30.436143613609914
        },
        "2023": {
          "n": 9,
          "net": 391.9223598197066,
          "fee": 88.25015752215383
        },
        "2024": {
          "n": 7,
          "net": 73.5204387094704,
          "fee": 78.09488095358837
        },
        "2025": {
          "n": 5,
          "net": 119.64121195392713,
          "fee": 44.828449060056286
        }
      },
      "entry_order_types": {
        "LIMIT": 23,
        "MARKET": 7
      },
      "exit_order_types": {
        "STOP": 30
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
        "Tue 16:01": 1,
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
    "Cq__S01": {
      "common_entries": 17,
      "total_a": 31,
      "total_b": 23,
      "only_a": 14,
      "only_b": 6,
      "sum_normalized_net_a": 0.009043084323936747,
      "sum_normalized_net_b": 0.009035816816777405,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S02": {
      "common_entries": 8,
      "total_a": 31,
      "total_b": 14,
      "only_a": 23,
      "only_b": 6,
      "sum_normalized_net_a": -0.04372066949105738,
      "sum_normalized_net_b": -0.04372084239251278,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S03": {
      "common_entries": 29,
      "total_a": 31,
      "total_b": 30,
      "only_a": 2,
      "only_b": 1,
      "sum_normalized_net_a": 0.1062392052567606,
      "sum_normalized_net_b": 0.10623920525676107,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "Cq__S04": {
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
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S01__S02": {
      "common_entries": 11,
      "total_a": 23,
      "total_b": 14,
      "only_a": 12,
      "only_b": 3,
      "sum_normalized_net_a": -0.00987419310032732,
      "sum_normalized_net_b": -0.009874193100327548,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S01__S03": {
      "common_entries": 15,
      "total_a": 23,
      "total_b": 30,
      "only_a": 8,
      "only_b": 15,
      "sum_normalized_net_a": 0.01771460794384886,
      "sum_normalized_net_b": 0.01772170353967109,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S01__S04": {
      "common_entries": 17,
      "total_a": 23,
      "total_b": 31,
      "only_a": 6,
      "only_b": 14,
      "sum_normalized_net_a": 0.009035816816777405,
      "sum_normalized_net_b": 0.009043084323936747,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S01__S05": {
      "common_entries": 17,
      "total_a": 23,
      "total_b": 31,
      "only_a": 6,
      "only_b": 14,
      "sum_normalized_net_a": 0.009035816816777405,
      "sum_normalized_net_b": 0.009043084323936747,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S02__S03": {
      "common_entries": 6,
      "total_a": 14,
      "total_b": 30,
      "only_a": 8,
      "only_b": 24,
      "sum_normalized_net_a": -0.03504205126544119,
      "sum_normalized_net_b": -0.03504205027532278,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S02__S04": {
      "common_entries": 8,
      "total_a": 14,
      "total_b": 31,
      "only_a": 6,
      "only_b": 23,
      "sum_normalized_net_a": -0.04372084239251278,
      "sum_normalized_net_b": -0.04372066949105738,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S02__S05": {
      "common_entries": 8,
      "total_a": 14,
      "total_b": 31,
      "only_a": 6,
      "only_b": 23,
      "sum_normalized_net_a": -0.04372084239251278,
      "sum_normalized_net_b": -0.04372066949105738,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S03__S04": {
      "common_entries": 29,
      "total_a": 30,
      "total_b": 31,
      "only_a": 1,
      "only_b": 2,
      "sum_normalized_net_a": 0.10623920525676107,
      "sum_normalized_net_b": 0.1062392052567606,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S03__S05": {
      "common_entries": 29,
      "total_a": 30,
      "total_b": 31,
      "only_a": 1,
      "only_b": 2,
      "sum_normalized_net_a": 0.10623920525676107,
      "sum_normalized_net_b": 0.1062392052567606,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "S04__S05": {
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

Artefactos pares completos individuales pairs_*.json; curva samplingmotor equity_engine.png. Fuente R60_SPY_ANALYSIS_SOURCE_20261019.md. Dashboards por sesión:

S01

Dashboard: http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21

S02

Dashboard: http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae

S03

Dashboard: http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e

S04

Dashboard: http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35

S05

Dashboard: http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134
