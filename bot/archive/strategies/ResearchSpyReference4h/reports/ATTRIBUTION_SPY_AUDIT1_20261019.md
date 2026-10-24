# Atribución SPY — primer bloque

Job93240f69bb694960ae5c23b27b90e4a7 succeeded; C0/Cq/E1 con31 entradas comunes exactas y todos los campos de payoff/qty/cierres iguales. Misma curva económica observada y mismas métricas. Quitar BE no cambia resultado en esta muestra; no prueba que el bloque jamás se ejecutara internamente.

La política de entrada se denomina retest LIMIT por su precio planificado, pero órdenes ejecutadas constan como24LIMIT+7MARKET; se conserva semántica real del motor sin atribuir causalidad de conversiones a partir de snapshots. No describir baseline como31fills LIMIT.

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
    "AttrSpyE1NoBE": {
      "session_id": "a0e806e0-9c7e-49e2-a044-79a32763dce0",
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
    "AttrSpyC0__AttrSpyE1NoBE": {
      "common_entries": 31,
      "total_a": 31,
      "total_b": 31,
      "only_a": 0,
      "only_b": 0,
      "sum_normalized_net_a": 0.09756058604102615,
      "sum_normalized_net_b": 0.09756058604102615,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyCqFreshLimit__AttrSpyE1NoBE": {
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

Rows exactas en results.json del job; fuente en ATTRIBUTION_SPY_ANALYSIS_SOURCE_20261019.md. Cohortes por cierre no son retornos MTM. Exposición por entrada×tiempo no es mark-to-market real.