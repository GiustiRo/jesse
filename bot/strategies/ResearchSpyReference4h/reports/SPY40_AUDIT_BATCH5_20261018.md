# SPY40 — auditoría del quinto par

Job 0a9d9f3a20a7475ea9f1bdb98dbee0e8 succeeded. Snapshots completos: costes de ambas piernas, PnL, tamaño y horarios reconciliados. 09 obtiene ganancia bruta de precio, absorbida por comisión base; 10 sólo once operaciones y ganancia bruta mínima, sin evidencia suficiente. Ninguna cumple neto positivo. Cohortes por cierre NO equivalen a retornos MTM.

```json
{
  "SPY40_09": {
    "session_id": "816a9466-705c-4149-a705-b466911dca5f",
    "n": 249,
    "net": -218.75218484996412,
    "fees": 830.7357037356858,
    "gross_price": 611.9835188857217,
    "pf": 0.9515960283751922,
    "return_pct": -2.1875218484996415,
    "cagr_engine": -0.4233305548071553,
    "dd_engine": -9.486826059508823,
    "stress5_samefills": -680.2720202586784,
    "stress10_samefills": -1141.7918556673926,
    "net_bps_entry": -2.371524405330394,
    "ex_top1": -411.64557997835436,
    "ex_top3": -626.490017639649,
    "ex_top5": -808.5251392115439,
    "side": {
      "short": {
        "n": 128,
        "net": -773.0993500055096,
        "fees": 451.1161543197984
      },
      "long": {
        "n": 121,
        "net": 554.3471651555456,
        "fees": 379.6195494158872
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 3,
        "net": -31.55824051012858,
        "fees": 10.82077871013
      },
      "2021": {
        "n": 37,
        "net": 108.09612881220583,
        "fees": 127.177475487795
      },
      "2022": {
        "n": 68,
        "net": 111.19237918086263,
        "fees": 157.62411416913747
      },
      "2023": {
        "n": 29,
        "net": -66.47291597962976,
        "fees": 105.27536119391355
      },
      "2024": {
        "n": 57,
        "net": -454.3933524188372,
        "fees": 234.7881930116968
      },
      "2025": {
        "n": 55,
        "net": 114.38381606556305,
        "fees": 195.04978116301288
      }
    },
    "hours": 12545.150000000001,
    "mean_hours": 50.382128514056234,
    "max_hours": 105.5,
    "crossing_UTC_days": 233,
    "first_entry": "2020-12-02 15:00:00+00:00",
    "last_exit": "2025-12-25 23:30:00+00:00",
    "max_initial_gross_equity": 0.6964159197863687,
    "entry_clock_NY": {
      "10:00": 249
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  },
  "SPY40_10": {
    "session_id": "9446bc74-046a-42fb-a65b-531828ea8758",
    "n": 11,
    "net": -33.07617062300339,
    "fees": 35.12814666586071,
    "gross_price": 2.051976042857329,
    "pf": 0.8403098081142294,
    "return_pct": -0.3307617062300339,
    "cagr_engine": -0.06352585958364632,
    "dd_engine": -1.5428379940458314,
    "stress5_samefills": -52.59180765959269,
    "stress10_samefills": -72.10744469618197,
    "net_bps_entry": -8.485982858186391,
    "ex_top1": -70.10237117924842,
    "ex_top3": -142.04840366036342,
    "ex_top5": -195.6575429234636,
    "side": {
      "long": {
        "n": 9,
        "net": 25.67573277063994,
        "fees": 29.205712629359997
      },
      "short": {
        "n": 2,
        "net": -58.75190339364334,
        "fees": 5.922434036500714
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2021": {
        "n": 4,
        "net": -91.05576277191325,
        "fees": 12.444513014770713
      },
      "2022": {
        "n": 1,
        "net": -17.0367637432503,
        "fees": 2.45333474325
      },
      "2023": {
        "n": 1,
        "net": 37.02620055624504,
        "fees": 2.2494441437550003
      },
      "2024": {
        "n": 3,
        "net": 10.443449468995205,
        "fees": 10.971135031005
      },
      "2025": {
        "n": 2,
        "net": 27.546705866919915,
        "fees": 7.00971973308
      }
    },
    "hours": 1251.5,
    "mean_hours": 113.77272727272727,
    "max_hours": 124,
    "crossing_UTC_days": 11,
    "first_entry": "2021-03-10 18:30:00+00:00",
    "last_exit": "2025-12-08 18:30:00+00:00",
    "max_initial_gross_equity": 0.4840210384029625,
    "entry_clock_NY": {
      "13:30": 3,
      "15:30": 4,
      "11:30": 4
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  }
}
```

Curva equity_engine.png disponible en el job. Reglas sin cambios.