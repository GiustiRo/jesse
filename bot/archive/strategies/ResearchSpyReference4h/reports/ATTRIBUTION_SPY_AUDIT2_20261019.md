# Atribución SPY — E2/E3

Jobc709e58bece04efb9f03e970c330589b succeeded. Snapshot completo reconcilia fees, PnL y balance; entradas comunes sólo idéntico timestamp/lado. E2 ocho operaciones con runner terminal dominante; E3 una operación mantenida desde2020 hasta engineend. Beneficio de exposición persistente observado, sin prueba de alpha. DDmotor y entry-notional×tiempo no equivalen a MTMUTC; root audita marks por separado.

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
    "AttrSpyE2NoTrail": {
      "session_id": "069cb46d-09a5-4c8e-b164-f9c2d1061691",
      "n": 8,
      "net": 4889.748865865099,
      "gross_price": 4947.176771684557,
      "fee": 57.427905819458054,
      "PF": 11.776888992472053,
      "return_pct": 48.89748865865099,
      "DD_engine_pct": -20.724256024947575,
      "hours_open": 39256.76666666667,
      "fraction_time_open": 0.859536842412565,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.5908738437924608,
      "entry_turnover_initial_equity": 6.1335195858,
      "roundtrip_turnover_initial_equity": 12.761756848768457,
      "net_bps_entry": 797.2174536110697,
      "net_per_exposure_entry_time_measure": 0.8275453241390357,
      "max_initial_gross_equity": 1.0811869529887856,
      "mean_hours": 4907.095833333334,
      "max_hours": 18683.966666666667,
      "stress5_RT_samefills": 4857.844473743178,
      "stress10_RT_samefills": 4825.940081621257,
      "net_without_top1": -450.6854868412511,
      "net_without_top3": -453.7254553963321,
      "net_without_top5": -277.6676027629819,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "LIMIT": 6,
        "MARKET": 2
      },
      "exit_order_types": {
        "STOP": 7,
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1,
        "Tue 13:46": 1,
        "Fri 11:06": 1,
        "Mon 08:34": 1,
        "Tue 12:00": 1,
        "Mon 19:01": 1,
        "Thu 04:00": 1,
        "Mon 12:02": 1
      },
      "terminal_liquidations": [
        "731cb360-87a7-4b14-86c0-354387db999f"
      ],
      "engine_open_count_preterminal": 1
    },
    "AttrSpyE3InitialStop": {
      "session_id": "1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
      "n": 1,
      "net": 3485.34533747049,
      "gross_price": 3490.1809566,
      "fee": 4.83561912951,
      "PF": null,
      "return_pct": 34.8534533747049,
      "DD_engine_pct": -11.060009660496705,
      "hours_open": 45151.8,
      "fraction_time_open": 0.9886100893326327,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.3586499123691498,
      "entry_turnover_initial_equity": 0.36278196656000006,
      "roundtrip_turnover_initial_equity": 1.07458202878,
      "net_bps_entry": 9607.272849087589,
      "net_per_exposure_entry_time_measure": 0.971795954011863,
      "max_initial_gross_equity": 0.36278196656000006,
      "mean_hours": 45151.8,
      "max_hours": 45151.8,
      "stress5_RT_samefills": 3482.65888239854,
      "stress10_RT_samefills": 3479.97242732659,
      "net_without_top1": 0,
      "net_without_top3": 0,
      "net_without_top5": 0,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2025": {
          "n": 1,
          "net": 3485.34533747049,
          "fee": 4.83561912951
        }
      },
      "entry_order_types": {
        "LIMIT": 1
      },
      "exit_order_types": {
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Thu 16:12": 1
      },
      "terminal_liquidations": [
        "fc6a2e15-d569-492a-a6a7-a9cbf4403b8a"
      ],
      "engine_open_count_preterminal": 1
    }
  },
  "pairs": {
    "AttrSpyC0__AttrSpyE2NoTrail": {
      "common_entries": 8,
      "total_a": 31,
      "total_b": 8,
      "only_a": 23,
      "only_b": 0,
      "sum_normalized_net_a": 0.04342342647315204,
      "sum_normalized_net_b": 0.4972808795559603,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyC0__AttrSpyE3InitialStop": {
      "common_entries": 1,
      "total_a": 31,
      "total_b": 1,
      "only_a": 30,
      "only_b": 0,
      "sum_normalized_net_a": 0.03803372989853942,
      "sum_normalized_net_b": 0.9607272849087589,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyE2NoTrail__AttrSpyE3InitialStop": {
      "common_entries": 1,
      "total_a": 8,
      "total_b": 1,
      "only_a": 7,
      "only_b": 0,
      "sum_normalized_net_a": 0.00022449375000009808,
      "sum_normalized_net_b": 0.9607272849087589,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    }
  }
}
```

Filas individuales por par en pares_*.json del job (nombre de artefacto con prefijo pairs_). Ningún cambio de parámetros.