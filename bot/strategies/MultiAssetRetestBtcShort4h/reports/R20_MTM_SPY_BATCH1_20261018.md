# R20: auditoría MTM SPY, primera tanda

Análisis `272eb9c53aca4bb5aae4e3b08c1a1b6b`, terminal succeeded. Órdenes ejecutadas reconciliadas con balance final; precios diarios recuperados de benchmark histórico mediante21/12/15 anclas BTC/PAXG/SPY (error máximo2e−15). La curva Portfolio00:01 no se usa como cierre diario. Ventana2020-10-15 a2025-12-31exclusiva;2026cerrado. Todos estos periodos son desarrollo reutilizado.

|Modelo|Meses completos activos|Meses completos+|%+ activos|Trimestres completos+|DD cierre diario|
|---|---:|---:|---:|---:|---:|
|spy01|28/61|14/61|50.0%|7/19|-3.279%|
|spy02|28/61|15/61|53.6%|9/19|-2.526%|
|spy03|21/61|12/61|57.1%|8/19|-2.284%|
|spy05|14/61|8/61|57.1%|4/19|-3.799%|
|spy06|4/61|4/61|100.0%|2/19|-0.804%|
|spy_base|33/61|15/61|45.5%|9/19|-5.218%|

Ningún porcentaje aislado se interpreta como cumplir los objetivos del portfolio. SPY06 tiene solo dos operaciones: cuatro meses positivos durante su tenencia no crean cuatro observaciones independientes. SPY02 tiene2024/2025negativos; SPY03 sigue inconcluso por25trades. DD diario es otra frecuencia de medición, no reemplaza el DD reportado por motor.

## Resultados completos

```json
[
  {
    "name": "spy01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 28,
      "positive_months": 14,
      "win_months_all": 0.22950819672131148,
      "win_months_active": 0.5,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 29,
    "win_months_all": 0.2222222222222222,
    "win_months_active": 0.4827586206896552,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2025-04-30 00:00:00+00:00",
      -0.015464459244166395
    ],
    "worst_quarter": [
      "2025-06-30 00:00:00+00:00",
      -0.017700064631619772
    ],
    "daily_close_drawdown_pct": -3.2785416389339184,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.007861898291193103,
      "2021-12-31 00:00:00+00:00": -0.003498839824767508,
      "2022-12-31 00:00:00+00:00": 0.00026750061165969896,
      "2023-12-31 00:00:00+00:00": -0.0022743874153969834,
      "2024-12-31 00:00:00+00:00": -0.015619021633592078,
      "2025-12-31 00:00:00+00:00": -0.006466100377815143
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 28,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.5357142857142857,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 28,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.5357142857142857,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2025-11-30 00:00:00+00:00",
      -0.009921365659880665
    ],
    "worst_quarter": [
      "2022-03-31 00:00:00+00:00",
      -0.009725903031146621
    ],
    "daily_close_drawdown_pct": -2.526183370254609,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.004573889415264043,
      "2021-12-31 00:00:00+00:00": 0.008395028804304427,
      "2022-12-31 00:00:00+00:00": 0.012412135888912212,
      "2023-12-31 00:00:00+00:00": 0.007294371156687962,
      "2024-12-31 00:00:00+00:00": -0.0027382969676559288,
      "2025-12-31 00:00:00+00:00": -0.0032862984689842056
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 21,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.5714285714285714,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 22,
    "win_months_all": 0.20634920634920634,
    "win_months_active": 0.5909090909090909,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2022-04-30 00:00:00+00:00",
      -0.009649590430234056
    ],
    "worst_quarter": [
      "2022-06-30 00:00:00+00:00",
      -0.011970272411222282
    ],
    "daily_close_drawdown_pct": -2.284216132918615,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0012270838474719437,
      "2021-12-31 00:00:00+00:00": 0.004433247825021969,
      "2022-12-31 00:00:00+00:00": -0.01522150933509725,
      "2023-12-31 00:00:00+00:00": 0.008666794252795817,
      "2024-12-31 00:00:00+00:00": -0.006613809935527959,
      "2025-12-31 00:00:00+00:00": 0.021529187622424617
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.5714285714285714,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 14,
    "win_months_all": 0.12698412698412698,
    "win_months_active": 0.5714285714285714,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2023-10-31 00:00:00+00:00",
      -0.01760100521363983
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.02073631980912205
    ],
    "daily_close_drawdown_pct": -3.7986597184254567,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0,
      "2022-12-31 00:00:00+00:00": 0.02479851732619398,
      "2023-12-31 00:00:00+00:00": -0.023260819485132367,
      "2024-12-31 00:00:00+00:00": 0,
      "2025-12-31 00:00:00+00:00": -0.006869340959847814
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy06",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 4,
      "positive_months": 4,
      "win_months_all": 0.06557377049180328,
      "win_months_active": 1,
      "quarters_total": 19,
      "positive_quarters": 2,
      "win_quarters": 0.10526315789473684
    },
    "months_total": 63,
    "months_active": 4,
    "win_months_all": 0.06349206349206349,
    "win_months_active": 1,
    "win_quarters": 0.09523809523809523,
    "worst_month": [
      "2020-10-31 00:00:00+00:00",
      0
    ],
    "worst_quarter": [
      "2020-12-31 00:00:00+00:00",
      0
    ],
    "daily_close_drawdown_pct": -0.8036537007220956,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0,
      "2022-12-31 00:00:00+00:00": 0,
      "2023-12-31 00:00:00+00:00": 0.007683993794216359,
      "2024-12-31 00:00:00+00:00": 0,
      "2025-12-31 00:00:00+00:00": 0.004550445642293788
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy_base",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 33,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.45454545454545453,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 33,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.45454545454545453,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.017943150704153754
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.01886503599679934
    ],
    "daily_close_drawdown_pct": -5.2179628778702085,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.02910008869946501,
      "2022-12-31 00:00:00+00:00": -0.016735052301659392,
      "2023-12-31 00:00:00+00:00": 0.038579232068278735,
      "2024-12-31 00:00:00+00:00": -0.002113109427550386,
      "2025-12-31 00:00:00+00:00": 0.011258940845987109
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  }
]
```
