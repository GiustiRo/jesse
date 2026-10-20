# SPY40 — auditoría del tercer par

Job bd94d7bf995a4afa9df061908cfdac00 succeeded. Snapshots completos reconciliados: comisión, PnL, tamaño aislado y horarios NY. Ambas hipótesis fallan el cribado económico, incluido el componente de precio previo a comisión. Las cohortes por año de cierre NO son retornos MTM.

```json
{
  "SPY40_05": {
    "session_id": "a99c090e-fa7d-4ec9-a51d-df265a0373fd",
    "n": 179,
    "net": -1185.0481445365788,
    "fees": 527.4607066365793,
    "gross_price": -657.5874378999995,
    "pf": 0.5968712537766363,
    "return_pct": -11.850481445365787,
    "cagr_engine": -2.3902831470885233,
    "dd_engine": -13.046874785397177,
    "stress5_samefills": -1478.0818704457897,
    "stress10_samefills": -1771.115596355,
    "net_bps_entry": -20.22506282071246,
    "ex_top1": -1268.1642258773284,
    "ex_top3": -1397.4110366785292,
    "ex_top5": -1509.1026894200638,
    "side": {
      "long": {
        "n": 96,
        "net": -524.173718244737,
        "fees": 332.31825561616705
      },
      "short": {
        "n": 83,
        "net": -660.8744262918418,
        "fees": 195.14245102041212
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2021": {
        "n": 6,
        "net": 31.556708041080853,
        "fees": 18.870410158920002
      },
      "2022": {
        "n": 77,
        "net": -374.0181183598229,
        "fees": 166.37213167410852
      },
      "2023": {
        "n": 5,
        "net": -87.95029256019016,
        "fees": 13.445605160189999
      },
      "2024": {
        "n": 42,
        "net": -148.25837694490988,
        "fees": 173.5564036020557
      },
      "2025": {
        "n": 49,
        "net": -606.3780647127365,
        "fees": 155.21615604130506
      }
    },
    "hours": 6202.849999999999,
    "mean_hours": 34.652793296089385,
    "max_hours": 96,
    "crossing_UTC_days": 179,
    "first_entry": "2021-12-01 21:00:00+00:00",
    "last_exit": "2025-12-15 21:00:00+00:00",
    "max_initial_gross_equity": 0.6909578884093862,
    "entry_clock_NY": {
      "16:00": 179
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  },
  "SPY40_06": {
    "session_id": "c3d874cb-ced8-4c68-8605-73335aae3a6e",
    "n": 35,
    "net": -660.1462665734974,
    "fees": 121.81486290206786,
    "gross_price": -538.3314036714295,
    "pf": 0.2997144142025045,
    "return_pct": -6.6014626657349735,
    "cagr_engine": -1.3013631212749233,
    "dd_engine": -6.63073615851606,
    "stress5_samefills": -727.8211904079797,
    "stress10_samefills": -795.4961142424618,
    "net_bps_entry": -48.90414187466227,
    "ex_top1": -733.1727099495678,
    "ex_top3": -815.8609364983087,
    "ex_top5": -863.9145105218336,
    "side": {
      "short": {
        "n": 18,
        "net": -698.5496338677058,
        "fees": 67.33919096770501
      },
      "long": {
        "n": 17,
        "net": 38.40336729420836,
        "fees": 54.47567193436286
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 1,
        "net": -26.311267783831184,
        "fees": 3.87344578383
      },
      "2021": {
        "n": 8,
        "net": -135.4090848408299,
        "fees": 30.444994869402862
      },
      "2022": {
        "n": 7,
        "net": -6.8888258902550845,
        "fees": 16.052739990255002
      },
      "2023": {
        "n": 8,
        "net": -70.70284191765587,
        "fees": 25.446538217654997
      },
      "2024": {
        "n": 8,
        "net": -261.2355941038011,
        "fees": 33.557641903800004
      },
      "2025": {
        "n": 3,
        "net": -159.59865203712434,
        "fees": 12.439502137125
      }
    },
    "hours": 2708.0666666666666,
    "mean_hours": 77.37333333333333,
    "max_hours": 125,
    "crossing_UTC_days": 35,
    "first_entry": "2020-12-09 20:30:00+00:00",
    "last_exit": "2025-08-24 23:30:00+00:00",
    "max_initial_gross_equity": 0.629061928581708,
    "entry_clock_NY": {
      "15:30": 5,
      "13:30": 23,
      "11:30": 7
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  }
}
```

Curva equity_engine.png disponible en el job. Sin rescates.