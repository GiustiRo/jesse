# SPY40 — auditoría del primer par

Job 803b4e9b71814d7ead7ad52460db9e7f succeeded. Comisión exacta de ambas piernas, PnL, equity de tamaño y horario reconciliados en snapshots completos. Sin operaciones en 01: las métricas de rentabilidad/riesgo no están disponibles; sumas vacías no representan resultados económicos observados ni permiten inferir qué condición bloqueó la entrada. En 02 el componente de precio ya es negativo antes de comisión. Las cohortes anuales siguientes agrupan cierres y NO son retornos MTM anuales.

```json
{
  "SPY40_01": {
    "session_id": "3441ac21-d65a-48f4-9f2d-4a025b474c1c",
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
  },
  "SPY40_02": {
    "session_id": "47206fe5-b8e0-4650-a7dc-23d0f7949e24",
    "n": 58,
    "net": -263.4227688825447,
    "fees": 201.0090058682593,
    "gross_price": -62.41376301428547,
    "pf": 0.7977661491371285,
    "return_pct": -2.6342276888254466,
    "cagr_engine": -0.5107165835812166,
    "dd_engine": -5.301502827463356,
    "stress5_samefills": -375.09443880935527,
    "stress10_samefills": -486.766108736166,
    "net_bps_entry": -11.802090112434268,
    "ex_top1": -414.9191662487052,
    "ex_top3": -594.2884122706556,
    "ex_top5": -763.5242430890646,
    "side": {
      "long": {
        "n": 29,
        "net": 7.046808331719433,
        "fees": 104.98654328256642
      },
      "short": {
        "n": 29,
        "net": -270.46957721426406,
        "fees": 96.02246258569286
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 3,
        "net": 65.48733657696567,
        "fees": 8.261446123035
      },
      "2021": {
        "n": 9,
        "net": -9.542465084949576,
        "fees": 37.47395628495
      },
      "2022": {
        "n": 17,
        "net": -89.16258525499188,
        "fees": 37.85219624070643
      },
      "2023": {
        "n": 7,
        "net": -222.00852247259851,
        "fees": 25.376367215455716
      },
      "2024": {
        "n": 11,
        "net": 96.12222054235636,
        "fees": 44.74115390050072
      },
      "2025": {
        "n": 11,
        "net": -104.31875318932673,
        "fees": 47.303886103611426
      }
    },
    "hours": 4362.966666666667,
    "mean_hours": 75.22356321839081,
    "max_hours": 99.5,
    "crossing_UTC_days": 58,
    "first_entry": "2020-11-09 21:00:00+00:00",
    "last_exit": "2025-12-26 21:00:00+00:00",
    "max_initial_gross_equity": 0.6990444334373674,
    "entry_clock_NY": {
      "16:00": 58
    },
    "terminal_liquidations": [],
    "engine_open_count_preterminal": 0,
    "classification": "fails_economic_screen"
  }
}
```

Curva disponible como equity_engine.png en job; sampling del motor, no cierre UTC. Ningún parámetro modificado.