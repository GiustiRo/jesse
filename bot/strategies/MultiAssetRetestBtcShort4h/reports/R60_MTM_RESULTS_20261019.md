# R60: resultados de auditoría MTM UTC

20 nuevos fulls y 20 reconstrucciones MTM terminadas. Todos los terminales concilian con fills, cantidades, fees y wallet. Las tres referencias se conservan de la auditoría de atribución previa, sobre la misma ventana y fuentes, y sus summaries se volvieron a leer; no se cuentan como nuevos fulls.

Método: cierres diarios UTC, derecho inclusivo; precios buyhold reescalados contra fills MARKET a medianoche de los mismos históricos proxy, al menos dos timestamps por mercado. Se mantiene el último mark observado durante cierres sólo para valorar; no implica ejecución posible. No se usa Portfolio00:01 como cierre diario UTC. Fuente completa R60_MTM_SOURCE_20261019.md.

Ventana2020-10-15→2025-12-31exclusiva, 2026 cerrado. Hay61 meses y19 trimestres completos; octubre2020 y diciembre2025 son parciales y se conservan por separado en JSON. Capital10.000USDT/riesgo1%/fee.00045porlado/isolated5x/cap4.4.

| Sesión | Meses + / 61 | Meses activos completos | Trimestres + / 19 | DD diario UTC % |
|---|---:|---:|---:|---:|
| [SPY_Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 15 | 33 | 9 | -5.217963 |
| [PAXG_Cq](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | 15 | 31 | 8 | -6.921781 |
| [PAXG_M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 17 | 31 | 10 | -7.650347 |
| [PAXG_P1_Cq](http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26) | 16 | 31 | 9 | -6.921781 |
| [PAXG_P1_M](http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb) | 17 | 31 | 10 | -7.650347 |
| [PAXG_P2_Cq](http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936) | 14 | 31 | 7 | -9.109127 |
| [PAXG_P2_M](http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a) | 16 | 31 | 10 | -10.071817 |
| [PAXG_P3_Cq](http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248) | 16 | 38 | 7 | -8.304764 |
| [PAXG_P3_M](http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c) | 17 | 39 | 7 | -10.382241 |
| [PAXG_P4_Cq](http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd) | 12 | 29 | 6 | -9.158957 |
| [PAXG_P4_M](http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504) | 15 | 30 | 9 | -10.019277 |
| [PAXG_P5_Cq](http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e) | 15 | 31 | 8 | -7.054802 |
| [PAXG_P5_M](http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14) | 17 | 31 | 10 | -7.766307 |
| [SPY_S01](http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21) | 10 | 27 | 6 | -6.700889 |
| [SPY_S02](http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae) | 6 | 17 | 5 | -4.114090 |
| [SPY_S03](http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e) | 15 | 32 | 9 | -6.137434 |
| [SPY_S04](http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35) | 15 | 33 | 9 | -5.217963 |
| [SPY_S05](http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134) | 15 | 33 | 9 | -5.217963 |
| [SPY_S06](http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2) | 15 | 33 | 9 | -5.217963 |
| [SPY_S07](http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60) | 17 | 37 | 8 | -8.100843 |
| [SPY_S08](http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb) | 13 | 27 | 7 | -5.904842 |
| [SPY_S09](http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f) | 15 | 33 | 9 | -5.217963 |
| [SPY_S10](http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a) | 15 | 33 | 9 | -5.217963 |

## Inputs y cuatro jobs reproducibles

```json
{
  "anchors": [
    {
      "session_type": "backtest",
      "session_id": "2e943276-7815-4280-96c8-d634d2dab817",
      "name": "benchmarks"
    },
    {
      "session_type": "backtest",
      "session_id": "b6f5562e-2144-4a54-9d27-108155680338",
      "name": "fade"
    },
    {
      "session_type": "backtest",
      "session_id": "5c8e7296-fdc3-46a6-8663-ff00ff0b1d20",
      "name": "reject"
    },
    {
      "session_type": "backtest",
      "session_id": "262fb59f-2b20-4247-aa9a-e7823cc3c930",
      "name": "sleeves"
    }
  ],
  "jobs": [
    {
      "job_id": "ebeb3affd2674b159a86ed94d8b75d4f",
      "targets": [
        {
          "name": "SPY_S01",
          "session_id": "d404c47e-025a-4789-b1a8-b054402f6c21",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S02",
          "session_id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S03",
          "session_id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S04",
          "session_id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "92e484ab29674927a04fb584a9a7061b",
      "targets": [
        {
          "name": "SPY_S05",
          "session_id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S06",
          "session_id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S07",
          "session_id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S08",
          "session_id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P1_Cq",
          "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P1_M",
          "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "593f56f26e054d73909df8a18d456bbe",
      "targets": [
        {
          "name": "SPY_S09",
          "session_id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
          "session_type": "backtest"
        },
        {
          "name": "SPY_S10",
          "session_id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P2_Cq",
          "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P2_M",
          "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "1e8860ec430e4aeb80d75c84d1d5e83a",
      "targets": [
        {
          "name": "PAXG_P3_Cq",
          "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P3_M",
          "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P4_Cq",
          "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P4_M",
          "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P5_Cq",
          "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_P5_M",
          "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
          "session_type": "backtest"
        }
      ]
    }
  ]
}
```

## Nuevos resultados exactos

```json
[
  {
    "name": "PAXG_P1_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 16,
      "win_months_all": 0.26229508196721313,
      "win_months_active": 0.5161290322580645,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.25396825396825395,
    "win_months_active": 0.5,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.018216868637475403
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.02148456266846943
    ],
    "daily_close_drawdown_pct": -6.921781413307038,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.02274690715946248,
      "2022-12-31 00:00:00+00:00": -0.008894893241745416,
      "2023-12-31 00:00:00+00:00": -0.005746087470991701,
      "2024-12-31 00:00:00+00:00": 0.051329013324179495,
      "2025-12-31 00:00:00+00:00": 0.0799285374334584
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P1_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.5483870967741935,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.53125,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.020288305947785412
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018852176706430135
    ],
    "daily_close_drawdown_pct": -7.65034683398127,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
      "2021-12-31 00:00:00+00:00": -0.024064578119711633,
      "2022-12-31 00:00:00+00:00": -0.009342100970716194,
      "2023-12-31 00:00:00+00:00": -0.015437450362151273,
      "2024-12-31 00:00:00+00:00": 0.07348604181087892,
      "2025-12-31 00:00:00+00:00": 0.11212642436365794
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P2_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 14,
      "win_months_all": 0.22950819672131148,
      "win_months_active": 0.45161290322580644,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.2222222222222222,
    "win_months_active": 0.4375,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.01821719817402845
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.021484382916591382
    ],
    "daily_close_drawdown_pct": -9.109126905714259,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.02274690715946248,
      "2022-12-31 00:00:00+00:00": -0.008894893241745416,
      "2023-12-31 00:00:00+00:00": -0.03230694618044805,
      "2024-12-31 00:00:00+00:00": 0.0513284394058644,
      "2025-12-31 00:00:00+00:00": 0.03892340534937899
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P2_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 16,
      "win_months_all": 0.26229508196721313,
      "win_months_active": 0.5161290322580645,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.25396825396825395,
    "win_months_active": 0.5,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.020288153417003296
    ],
    "worst_quarter": [
      "2023-03-31 00:00:00+00:00",
      -0.026702424707448325
    ],
    "daily_close_drawdown_pct": -10.071816509860465,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
      "2021-12-31 00:00:00+00:00": -0.024064578119711633,
      "2022-12-31 00:00:00+00:00": -0.009342100970716194,
      "2023-12-31 00:00:00+00:00": -0.041253333654970636,
      "2024-12-31 00:00:00+00:00": 0.07348663884749462,
      "2025-12-31 00:00:00+00:00": 0.07043502995467077
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P3_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 38,
      "positive_months": 16,
      "win_months_all": 0.26229508196721313,
      "win_months_active": 0.42105263157894735,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 39,
    "win_months_all": 0.25396825396825395,
    "win_months_active": 0.41025641025641024,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2025-09-30 00:00:00+00:00",
      -0.018056713342347264
    ],
    "worst_quarter": [
      "2025-09-30 00:00:00+00:00",
      -0.024528008387547873
    ],
    "daily_close_drawdown_pct": -8.304764307824941,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209761,
      "2021-12-31 00:00:00+00:00": -0.03450444787795903,
      "2022-12-31 00:00:00+00:00": -0.018069670728712794,
      "2023-12-31 00:00:00+00:00": 0.00415707077428773,
      "2024-12-31 00:00:00+00:00": 0.05132846183058626,
      "2025-12-31 00:00:00+00:00": 0.029066975540072315
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P3_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 39,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.4358974358974359,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 40,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.425,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.0200333738231111
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018852176706430135
    ],
    "daily_close_drawdown_pct": -10.382240725513636,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.001892533884274794,
      "2021-12-31 00:00:00+00:00": -0.034158177515287824,
      "2022-12-31 00:00:00+00:00": -0.018512533963294664,
      "2023-12-31 00:00:00+00:00": -0.027534095138975534,
      "2024-12-31 00:00:00+00:00": 0.07348655807322912,
      "2025-12-31 00:00:00+00:00": 0.055796006050243596
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P4_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 29,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.41379310344827586,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 30,
    "win_months_all": 0.19047619047619047,
    "win_months_active": 0.4,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2025-09-30 00:00:00+00:00",
      -0.018056557358158476
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.021484725195040966
    ],
    "daily_close_drawdown_pct": -9.158957303540971,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209761,
      "2021-12-31 00:00:00+00:00": -0.0318802152976434,
      "2022-12-31 00:00:00+00:00": -0.008895081732313237,
      "2023-12-31 00:00:00+00:00": -0.02371299557340034,
      "2024-12-31 00:00:00+00:00": 0.040609382974877706,
      "2025-12-31 00:00:00+00:00": 0.0364617639651299
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P4_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.5,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 31,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.4838709677419355,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.019680826774524984
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018852176706430135
    ],
    "daily_close_drawdown_pct": -10.019277064382148,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.001892533884274794,
      "2021-12-31 00:00:00+00:00": -0.03208931732066089,
      "2022-12-31 00:00:00+00:00": -0.009342274049184418,
      "2023-12-31 00:00:00+00:00": -0.032739591985538996,
      "2024-12-31 00:00:00+00:00": 0.0652743226055601,
      "2025-12-31 00:00:00+00:00": 0.05764007845913155
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P5_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.4838709677419355,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.46875,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.018217217224297144
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.021484782227233157
    ],
    "daily_close_drawdown_pct": -7.054801735606542,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209761,
      "2021-12-31 00:00:00+00:00": -0.02274690715946226,
      "2022-12-31 00:00:00+00:00": -0.010132840250292707,
      "2023-12-31 00:00:00+00:00": -0.005746246263316768,
      "2024-12-31 00:00:00+00:00": 0.051326740371807844,
      "2025-12-31 00:00:00+00:00": 0.03914378505791105
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_P5_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.5483870967741935,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.53125,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.02028831591158986
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018852176706430135
    ],
    "daily_close_drawdown_pct": -7.766307133997263,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.001892533884274794,
      "2021-12-31 00:00:00+00:00": -0.02406457811971141,
      "2022-12-31 00:00:00+00:00": -0.01058613912162032,
      "2023-12-31 00:00:00+00:00": -0.015437340546487266,
      "2024-12-31 00:00:00+00:00": 0.07348592165460688,
      "2025-12-31 00:00:00+00:00": 0.07075057212184643
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 27,
      "positive_months": 10,
      "win_months_all": 0.16393442622950818,
      "win_months_active": 0.37037037037037035,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 27,
    "win_months_all": 0.15873015873015872,
    "win_months_active": 0.37037037037037035,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2024-02-29 00:00:00+00:00",
      -0.016012477711352613
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.033505835718280474
    ],
    "daily_close_drawdown_pct": -6.700888536837479,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.02032719376586023,
      "2022-12-31 00:00:00+00:00": -0.007525971679981147,
      "2023-12-31 00:00:00+00:00": -0.008369379639570185,
      "2024-12-31 00:00:00+00:00": -0.015516458613753059,
      "2025-12-31 00:00:00+00:00": 0.006049512569999305
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 17,
      "positive_months": 6,
      "win_months_all": 0.09836065573770492,
      "win_months_active": 0.35294117647058826,
      "quarters_total": 19,
      "positive_quarters": 5,
      "win_quarters": 0.2631578947368421
    },
    "months_total": 63,
    "months_active": 17,
    "win_months_all": 0.09523809523809523,
    "win_months_active": 0.35294117647058826,
    "win_quarters": 0.23809523809523808,
    "worst_month": [
      "2022-03-31 00:00:00+00:00",
      -0.009284792478782
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.016076751871418216
    ],
    "daily_close_drawdown_pct": -4.114090027250095,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.019295137763168047,
      "2022-12-31 00:00:00+00:00": -0.02351140317618361,
      "2023-12-31 00:00:00+00:00": 0.010142393440560893,
      "2024-12-31 00:00:00+00:00": 0.003645594166293842,
      "2025-12-31 00:00:00+00:00": 0.015357338611493354
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 32,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.46875,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.46875,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.01880291153749558
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.01880291153749558
    ],
    "daily_close_drawdown_pct": -6.137433901514077,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.02910008869946501,
      "2022-12-31 00:00:00+00:00": -0.02627322525844411,
      "2023-12-31 00:00:00+00:00": 0.038579261012404054,
      "2024-12-31 00:00:00+00:00": 0.006968227270612193,
      "2025-12-31 00:00:00+00:00": 0.011261059500341064
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S04",
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
  },
  {
    "name": "SPY_S05",
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
  },
  {
    "name": "SPY_S06",
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
  },
  {
    "name": "SPY_S07",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 37,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.4594594594594595,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 37,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.4594594594594595,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.02675210488441515
    ],
    "worst_quarter": [
      "2022-09-30 00:00:00+00:00",
      -0.02160839150382665
    ],
    "daily_close_drawdown_pct": -8.10084341613928,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.04960193168421578,
      "2022-12-31 00:00:00+00:00": -0.030024009311931832,
      "2023-12-31 00:00:00+00:00": 0.01968666526322216,
      "2024-12-31 00:00:00+00:00": 0.004606585991174139,
      "2025-12-31 00:00:00+00:00": 0.002355082231848993
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S08",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 27,
      "positive_months": 13,
      "win_months_all": 0.21311475409836064,
      "win_months_active": 0.48148148148148145,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 27,
    "win_months_all": 0.20634920634920634,
    "win_months_active": 0.48148148148148145,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.018802966694093648
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.018802966694093648
    ],
    "daily_close_drawdown_pct": -5.904842466070659,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.03812177891620805,
      "2022-12-31 00:00:00+00:00": -0.034138325555732596,
      "2023-12-31 00:00:00+00:00": 0.022811668229330895,
      "2024-12-31 00:00:00+00:00": 0.008060658168868917,
      "2025-12-31 00:00:00+00:00": 0.019575612059280267
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_S09",
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
  },
  {
    "name": "SPY_S10",
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
      -0.01886484526125476
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
      "2023-12-31 00:00:00+00:00": 0.038612251833021194,
      "2024-12-31 00:00:00+00:00": -0.0021125826979314644,
      "2025-12-31 00:00:00+00:00": 0.011260515548420669
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

## Referencias reutilizadas, no nuevas ejecuciones

```json
[
  {
    "name": "SPY_Cq",
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
  },
  {
    "name": "PAXG_Cq",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.4838709677419355,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.46875,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.018217049938348606
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.02148456266846943
    ],
    "daily_close_drawdown_pct": -6.921781413307038,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.02274690715946248,
      "2022-12-31 00:00:00+00:00": -0.008894893241745416,
      "2023-12-31 00:00:00+00:00": -0.005746087470991701,
      "2024-12-31 00:00:00+00:00": 0.051329013324179495,
      "2025-12-31 00:00:00+00:00": 0.03914257549642297
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 31,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.5483870967741935,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 32,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.53125,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2025-12-31 00:00:00+00:00",
      -0.02028800226220051
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018852176706430135
    ],
    "daily_close_drawdown_pct": -7.65034683398127,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0018925338842750161,
      "2021-12-31 00:00:00+00:00": -0.024064578119711633,
      "2022-12-31 00:00:00+00:00": -0.009342100970716194,
      "2023-12-31 00:00:00+00:00": -0.015437450362151273,
      "2024-12-31 00:00:00+00:00": 0.07348604181087892,
      "2025-12-31 00:00:00+00:00": 0.0707526450013436
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
