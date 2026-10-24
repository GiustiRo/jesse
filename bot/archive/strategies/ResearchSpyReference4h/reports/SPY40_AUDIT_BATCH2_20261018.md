# SPY40 — auditoría del segundo par

Job 0bad9bcf93c64493b90f217c828bd256 succeeded. Snapshots completos: reconciliados costes, PnL, tamaño y entradas NY. Ambas recetas negativas antes de comisión también; 03 tiene muestra escasa. Cohortes de cierres no equivalen a retornos anuales MTM.

```json
{
  "SPY40_03": {
    "session_id": "817894dd-a064-4a38-be9c-990c7831e599",
    "n": 15,
    "net": -146.57774370748595,
    "fees": 55.55424526462927,
    "gross_price": -91.02349844285666,
    "pf": 0.5947548903311098,
    "return_pct": -1.4657774370748595,
    "cagr_engine": -0.2828197639073271,
    "dd_engine": -2.5608923876676903,
    "stress5_samefills": -177.44121329894668,
    "stress10_samefills": -208.30468289040738,
    "net_bps_entry": -23.791597003493667,
    "ex_top1": -207.82626228373647,
    "ex_top3": -308.12514107035634,
    "ex_top5": -351.31849648436673,
    "side": {
      "long": {
        "n": 6,
        "net": 53.10458665617033,
        "fees": 19.28345134383
      },
      "short": {
        "n": 9,
        "net": -199.68233036365632,
        "fees": 36.270793920799285
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2022": {
        "n": 6,
        "net": -3.0115471986299625,
        "fees": 16.829987598629998
      },
      "2023": {
        "n": 3,
        "net": -98.86642305861034,
        "fees": 10.075924658609999
      },
      "2024": {
        "n": 3,
        "net": -43.31878200229538,
        "fees": 14.786019902295
      },
      "2025": {
        "n": 3,
        "net": -1.3809914479502794,
        "fees": 13.862313105094287
      }
    },
    "hours": 1210.7333333333333,
    "mean_hours": 80.71555555555555,
    "max_hours": 123.5,
    "crossing_UTC_days": 15,
    "first_entry": "2022-01-10 21:00:00+00:00",
    "last_exit": "2025-11-10 21:00:00+00:00",
    "max_initial_gross_equity": 0.6984706403216595,
    "entry_clock_NY": {
      "16:00": 15
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "inconclusive_small_sample"
  },
  "SPY40_04": {
    "session_id": "7e15fa8f-eb4f-4029-af1a-6bae22f1803d",
    "n": 189,
    "net": -877.3456091592036,
    "fees": 607.6535488877764,
    "gross_price": -269.6920602714273,
    "pf": 0.7873235746196816,
    "return_pct": -8.773456091592035,
    "cagr_engine": -1.745793194204115,
    "dd_engine": -9.846061698624354,
    "stress5_samefills": -1214.9309140968574,
    "stress10_samefills": -1552.5162190345113,
    "net_bps_entry": -13.001446606757087,
    "ex_top1": -1000.7376761089429,
    "ex_top3": -1189.640666310653,
    "ex_top5": -1362.5010492102733,
    "side": {
      "long": {
        "n": 110,
        "net": -132.3541394903351,
        "fees": 361.97087236176213
      },
      "short": {
        "n": 79,
        "net": -744.9914696688688,
        "fees": 245.68267652601432
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2021": {
        "n": 32,
        "net": -428.20753206144144,
        "fees": 102.77255683287001
      },
      "2022": {
        "n": 45,
        "net": -293.37620608645716,
        "fees": 99.52146991503002
      },
      "2023": {
        "n": 23,
        "net": -132.31739233967107,
        "fees": 71.18615626824214
      },
      "2024": {
        "n": 41,
        "net": 326.3537214828357,
        "fees": 161.39245154573575
      },
      "2025": {
        "n": 48,
        "net": -349.79820015446995,
        "fees": 172.78091432589858
      }
    },
    "hours": 14372.099999999999,
    "mean_hours": 76.04285714285714,
    "max_hours": 123.5,
    "crossing_UTC_days": 189,
    "first_entry": "2021-01-28 21:00:00+00:00",
    "last_exit": "2025-12-31 00:00:00+00:00",
    "max_initial_gross_equity": 0.690389830259277,
    "entry_clock_NY": {
      "16:00": 189
    },
    "terminal_liquidations": [
      "43dba71e-a293-48cb-9f5a-b206056788e3"
    ],
    "engine_open_count_preterminal": 1,
    "classification": "fails_economic_screen"
  }
}
```

Curva equity_engine.png disponible en el job. Sin modificaciones de reglas tras resultados.