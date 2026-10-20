# Atribución SPY — E4/M

Job7dd041ee8006450387358f4df1d10676 succeeded. Costes, PnL y balances reconciliados sobre snapshots completos. E4 plazo72h desde fill con deuda de cotización; no garantía de fill exacto72h. Cq/M contrastan políticas con ocupación y selección distintas, no causalidad pura. Pares requieren entrada real común exacta; normalización por notional no elimina sesgo.

```json
{
  "metrics": {
    "AttrSpyC0": {
      "session_id": "798e6f62-979d-46a2-bf6d-b5983bcb3269",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
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
    "AttrSpyCqFreshLimit": {
      "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
      "n": 31,
      "net": 751.3477149671152,
      "gross_price": 1037.8232411744636,
      "fee": 286.47552620734854,
      "PF": 1.4930482284215572,
      "return_pct": 7.513477149671152,
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
    "AttrSpyE4Stop72h": {
      "session_id": "0c2efecc-aa4d-41c4-a9ac-832af72595a5",
      "n": 44,
      "net": -28.867539957479785,
      "gross_price": 377.560918441459,
      "fee": 406.4284583989386,
      "PF": 0.9806463373785479,
      "return_pct": -0.2886753995747979,
      "DD_engine_pct": -7.4718587007506,
      "hours_open": 2670.75,
      "fraction_time_open": 0.058476747241198106,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.05938130511605465,
      "entry_turnover_initial_equity": 45.13983955396,
      "roundtrip_turnover_initial_equity": 90.31743519976413,
      "net_bps_entry": -0.6395135703345076,
      "net_per_exposure_entry_time_measure": -0.04861385229081973,
      "max_initial_gross_equity": 1.598996585553435,
      "mean_hours": 60.69886363636364,
      "max_hours": 117.98333333333333,
      "stress5_RT_samefills": -254.66112795689014,
      "stress10_RT_samefills": -480.45471595630033,
      "net_without_top1": -215.9489723917068,
      "net_without_top3": -483.5227560627142,
      "net_without_top5": -709.8798978910851,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 34,
        "MARKET": 10
      },
      "exit_order_types": {
        "MARKET": 29,
        "STOP": 15
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Fri 04:00": 1,
        "Fri 12:00": 2,
        "Tue 09:40": 1,
        "Tue 08:02": 1,
        "Mon 12:00": 1,
        "Tue 15:20": 1,
        "Mon 16:01": 2,
        "Fri 12:33": 1,
        "Thu 12:01": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Tue 16:01": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 2,
        "Mon 19:01": 1,
        "Fri 17:01": 1,
        "Fri 06:02": 1,
        "Thu 16:06": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1,
        "Wed 15:20": 1,
        "Wed 16:00": 1,
        "Thu 08:00": 2,
        "Fri 16:04": 2,
        "Fri 14:31": 1,
        "Mon 19:16": 1,
        "Fri 16:01": 1,
        "Fri 16:06": 1,
        "Tue 18:50": 1,
        "Wed 06:01": 1,
        "Fri 08:23": 1,
        "Mon 17:08": 1,
        "Mon 05:04": 1,
        "Mon 17:25": 1,
        "Fri 14:01": 1,
        "Tue 06:20": 1,
        "Wed 16:03": 1,
        "Mon 08:01": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyMarket": {
      "session_id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
      "n": 38,
      "net": 151.6012639172099,
      "gross_price": 488.3315562886899,
      "fee": 336.73029237147995,
      "PF": 1.074122772361648,
      "return_pct": 1.516012639172099,
      "DD_engine_pct": -7.718707541843617,
      "hours_open": 7305.716666666666,
      "fraction_time_open": 0.15996051556022653,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.1446681109984161,
      "entry_turnover_initial_equity": 37.390060352350005,
      "roundtrip_turnover_initial_equity": 74.82895386032888,
      "net_bps_entry": 4.054587301774217,
      "net_per_exposure_entry_time_measure": 0.10479245417040782,
      "max_initial_gross_equity": 1.5992931529349965,
      "mean_hours": 192.25570175438597,
      "max_hours": 842.1666666666666,
      "stress5_RT_samefills": -35.47112073361228,
      "stress10_RT_samefills": -222.54350538443452,
      "net_without_top1": -224.7296691424284,
      "net_without_top3": -864.90548009341,
      "net_without_top5": -1306.5405470655624,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "MARKET": 38
      },
      "exit_order_types": {
        "STOP": 37,
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Thu 12:00": 2,
        "Tue 04:00": 3,
        "Fri 04:00": 2,
        "Fri 16:00": 6,
        "Tue 08:00": 1,
        "Tue 12:00": 4,
        "Mon 16:00": 4,
        "Mon 08:00": 1,
        "Fri 08:00": 2,
        "Thu 04:00": 4,
        "Thu 16:00": 2,
        "Mon 12:00": 1,
        "Tue 16:00": 2,
        "Thu 08:00": 1,
        "Mon 04:00": 1,
        "Fri 12:00": 1,
        "Wed 16:00": 1
      },
      "terminal_liquidations": [
        "5664a1ca-00dc-4ece-9064-aeb07980f28f"
      ],
      "engine_open_count_preterminal": 1
    }
  },
  "pairs": {
    "AttrSpyC0__AttrSpyCqFreshLimit": {
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyC0__AttrSpyE4Stop72h": {
      "common_entries": 30,
      "total_a": 31,
      "total_b": 44,
      "only_a": 1,
      "only_b": 14,
      "sum_normalized_net_a": 0.0754547199411579,
      "sum_normalized_net_b": -0.008241582644092268,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyC0__AttrSpyMarket": {
      "common_entries": 5,
      "total_a": 31,
      "total_b": 38,
      "only_a": 26,
      "only_b": 33,
      "sum_normalized_net_a": 0.0013279239275610626,
      "sum_normalized_net_b": 0.001327943725585202,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyCqFreshLimit__AttrSpyE4Stop72h": {
      "common_entries": 30,
      "total_a": 31,
      "total_b": 44,
      "only_a": 1,
      "only_b": 14,
      "sum_normalized_net_a": 0.0754547199411579,
      "sum_normalized_net_b": -0.008241582644092268,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyCqFreshLimit__AttrSpyMarket": {
      "common_entries": 5,
      "total_a": 31,
      "total_b": 38,
      "only_a": 26,
      "only_b": 33,
      "sum_normalized_net_a": 0.0013279239275610626,
      "sum_normalized_net_b": 0.001327943725585202,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyE4Stop72h__AttrSpyMarket": {
      "common_entries": 4,
      "total_a": 44,
      "total_b": 38,
      "only_a": 40,
      "only_b": 34,
      "sum_normalized_net_a": -0.02527229911866486,
      "sum_normalized_net_b": -0.020777922374283046,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    }
  }
}
```

Filas de pares individuales en artefactos pairs_*.json; enginecurve no es daily-close MTM.