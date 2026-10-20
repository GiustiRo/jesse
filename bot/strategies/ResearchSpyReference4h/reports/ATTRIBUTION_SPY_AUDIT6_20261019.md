# Atribución SPY — U02/U03

Job3db36a3cb29e46b69a47c551d5d3b785 succeeded, reconciliados costes/PnL/balances y tamaños. Semillas predefinidas, sin selección posterior. Retorno y exposición difieren; no se usa una semilla ganadora como evidencia representativa. Pares condicionales por timestamp real de fill; cohortes de cierre no son MTM.

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
    "AttrSpyU02": {
      "session_id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
      "n": 70,
      "net": 2572.1409833508283,
      "gross_price": 3147.689175878884,
      "fee": 575.5481925280554,
      "PF": 1.6407248804879624,
      "return_pct": 25.721409833508286,
      "DD_engine_pct": -5.493244162762901,
      "hours_open": 14612.616666666667,
      "fraction_time_open": 0.31994694050329886,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.2605476399199419,
      "entry_turnover_initial_equity": 63.79241471099,
      "roundtrip_turnover_initial_equity": 127.89959833956789,
      "net_bps_entry": 40.32048316408543,
      "net_per_exposure_entry_time_measure": 0.9872056350773956,
      "max_initial_gross_equity": 1.6472629528153622,
      "mean_hours": 208.75166666666667,
      "max_hours": 974.1,
      "stress5_RT_samefills": 2252.3919875019083,
      "stress10_RT_samefills": 1932.6429916529887,
      "net_without_top1": 2005.5306829129077,
      "net_without_top3": 959.5942650886718,
      "net_without_top5": -24.460416754159723,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "MARKET": 70
      },
      "exit_order_types": {
        "STOP": 70
      },
      "entry_clock_UTC": {
        "Thu 08:00": 3,
        "Thu 04:00": 3,
        "Tue 04:00": 4,
        "Mon 12:00": 8,
        "Mon 16:00": 3,
        "Thu 12:00": 7,
        "Fri 04:00": 5,
        "Fri 16:00": 5,
        "Wed 04:00": 3,
        "Fri 12:00": 1,
        "Tue 08:00": 4,
        "Thu 16:00": 1,
        "Mon 04:00": 4,
        "Tue 16:00": 4,
        "Wed 12:00": 2,
        "Tue 12:00": 3,
        "Fri 08:00": 3,
        "Mon 08:00": 4,
        "Wed 16:00": 2,
        "Wed 08:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyU03": {
      "session_id": "63dd9d81-c7bf-417b-823f-728977051fd8",
      "n": 74,
      "net": -440.27560690769474,
      "gross_price": 140.49435155449498,
      "fee": 580.7699584621895,
      "PF": 0.9008425504447655,
      "return_pct": -4.402756069076948,
      "DD_engine_pct": -14.787161148432038,
      "hours_open": 12211.766666666666,
      "fraction_time_open": 0.2673797220762539,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.2281749269603607,
      "entry_turnover_initial_equity": 64.52297066711002,
      "roundtrip_turnover_initial_equity": 129.05999076937547,
      "net_bps_entry": -6.823548301568223,
      "net_per_exposure_entry_time_measure": -0.19295529652308416,
      "max_initial_gross_equity": 1.3578716028398357,
      "mean_hours": 165.0238738738739,
      "max_hours": 870.1666666666666,
      "stress5_RT_samefills": -762.925583831133,
      "stress10_RT_samefills": -1085.5755607545716,
      "net_without_top1": -1050.492371257966,
      "net_without_top3": -2029.0513462937815,
      "net_without_top5": -2675.7578819256432,
      "closed_trade_year_cohorts_NOT_MTM": {
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
      "entry_order_types": {
        "MARKET": 74
      },
      "exit_order_types": {
        "STOP": 74
      },
      "entry_clock_UTC": {
        "Wed 08:00": 4,
        "Thu 04:00": 3,
        "Mon 16:00": 7,
        "Fri 08:00": 4,
        "Fri 04:00": 5,
        "Thu 12:00": 3,
        "Mon 08:00": 4,
        "Wed 04:00": 6,
        "Mon 04:00": 2,
        "Tue 16:00": 2,
        "Fri 16:00": 1,
        "Thu 08:00": 4,
        "Tue 08:00": 4,
        "Thu 16:00": 2,
        "Tue 04:00": 5,
        "Mon 12:00": 4,
        "Tue 12:00": 2,
        "Wed 16:00": 2,
        "Wed 12:00": 7,
        "Fri 12:00": 3
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    }
  },
  "pairs": {
    "AttrSpyC0__AttrSpyU02": {
      "common_entries": 1,
      "total_a": 31,
      "total_b": 70,
      "only_a": 30,
      "only_b": 69,
      "sum_normalized_net_a": -0.008366171718804436,
      "sum_normalized_net_b": -0.008366171718804301,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyC0__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 31,
      "total_b": 74,
      "only_a": 31,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU02__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 70,
      "total_b": 74,
      "only_a": 70,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    }
  }
}
```

Artefactos individuales de pares y curva samplingmotor preservados en job.