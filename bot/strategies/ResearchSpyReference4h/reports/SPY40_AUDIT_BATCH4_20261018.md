# SPY40 — auditoría del cuarto par

Job 4aee4d320ebe4536841c70c9c9a26b29 succeeded. Snapshots completos: comisión, PnL, tamaño y entradas NY reconciliados. 07 negativa también antes de comisión; 08 sin operaciones ni métricas económicas disponibles. Ningún conteo interno conservado permite inferir por qué no hubo fills en 08. Cohortes por cierre no equivalen a retornos anuales MTM.

```json
{
  "SPY40_07": {
    "session_id": "fcd709dc-c844-4d40-8e9a-35497ac3681f",
    "n": 68,
    "net": -453.0308982029518,
    "fees": 220.4350634458093,
    "gross_price": -232.59583475714243,
    "pf": 0.5778512929877893,
    "return_pct": -4.530308982029518,
    "cagr_engine": -0.8852802123613501,
    "dd_engine": -5.280261484441562,
    "stress5_samefills": -575.4948223395123,
    "stress10_samefills": -697.9587464760732,
    "net_bps_entry": -18.50134532644926,
    "ex_top1": -503.1720229090722,
    "ex_top3": -593.5034526298926,
    "ex_top5": -662.0867628453677,
    "side": {
      "long": {
        "n": 43,
        "net": -202.35576218684625,
        "fees": 150.14609972970425
      },
      "short": {
        "n": 25,
        "net": -250.67513601610548,
        "fees": 70.28896371610499
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2022": {
        "n": 21,
        "net": -81.52387073861449,
        "fees": 46.638637638615
      },
      "2023": {
        "n": 25,
        "net": -243.71642341671443,
        "fees": 84.331107716715
      },
      "2024": {
        "n": 19,
        "net": -95.28906288246804,
        "fees": 80.10248522532429
      },
      "2025": {
        "n": 3,
        "net": -32.50154116515474,
        "fees": 9.362832865155
      }
    },
    "hours": 2801.766666666667,
    "mean_hours": 41.20245098039215,
    "max_hours": 96,
    "crossing_UTC_days": 68,
    "first_entry": "2022-04-12 20:00:00+00:00",
    "last_exit": "2025-02-07 21:00:00+00:00",
    "max_initial_gross_equity": 0.6303031087920363,
    "entry_clock_NY": {
      "16:00": 68
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  },
  "SPY40_08": {
    "session_id": "79ce393c-4c56-46ae-a1b0-9410a5da2fc8",
    "n": 0,
    "net": 0,
    "fees": 0,
    "gross_price": 0,
    "pf": null,
    "return_pct": null,
    "cagr_engine": null,
    "dd_engine": null,
    "stress5_samefills": 0,
    "stress10_samefills": 0,
    "net_bps_entry": null,
    "ex_top1": null,
    "ex_top3": null,
    "ex_top5": null,
    "side": {},
    "closed_trade_year_cohorts_NOT_MTM": {},
    "hours": 0,
    "mean_hours": 0,
    "max_hours": 0,
    "crossing_UTC_days": 0,
    "first_entry": null,
    "last_exit": null,
    "max_initial_gross_equity": 0,
    "entry_clock_NY": {},
    "terminal_liquidations": [],
    "engine_open_count_preterminal": null,
    "classification": "no_trades"
  }
}
```

Curva equity_engine.png disponible en el job. Sin cambios de reglas.