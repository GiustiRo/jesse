# Atribución SPY/PAXG: auditoría MTM a cierre diario UTC

Se completaron las 34 sesiones y las 34 auditorías. Todos los terminales concilian con fills, comisiones y wallet. Ventana 2020-10-15 a 2025-12-31 exclusiva; 2026 cerrado. Capital inicial 10.000 USDT por activo, riesgo planificado 1%, comisión 0,00045 por lado.

Las valoraciones usan precios diarios del mismo histórico proxy, reescalados mediante fills MARKET a medianoche y verificados contra al menos dos timestamps distintos por mercado. La curva Portfolio de las 00:01 no se usa como cierre diario UTC. Se mantiene el último mark observado durante cierres sólo para valoración. Las liquidaciones del motor al límite final se concilian, pero no prueban liquidez ejecutable en ese instante.

La ventana contiene 61 meses y 19 trimestres completos. Octubre de 2020 y diciembre de 2025 son parciales. La tabla usa únicamente periodos completos; el JSON también conserva las fronteras parciales para continuidad. Un mes activo puede contener largos periodos sin exposición; no equivale a estar invertido todo el mes.

| Sesión | Meses positivos / 61 | Meses activos completos | Trimestres positivos / 19 | DD diario UTC % | Cierres terminales conciliados |
|---|---:|---:|---:|---:|---:|
| [PAXG_C0](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673) | 15 | 31 | 8 | -6.922 | 0 |
| [PAXG_Cq](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | 15 | 31 | 8 | -6.922 | 0 |
| [PAXG_E1](http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b) | 15 | 31 | 8 | -7.407 | 0 |
| [PAXG_E2](http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc) | 22 | 37 | 9 | -10.674 | 1 |
| [PAXG_E3](http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242) | 19 | 37 | 6 | -14.748 | 1 |
| [PAXG_E4](http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837) | 11 | 30 | 6 | -6.294 | 0 |
| [PAXG_M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 17 | 31 | 10 | -7.650 | 0 |
| [PAXG_R01](http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1) | 11 | 30 | 4 | -8.422 | 0 |
| [PAXG_R02](http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c) | 10 | 28 | 7 | -8.680 | 0 |
| [PAXG_R03](http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796) | 17 | 30 | 7 | -7.274 | 0 |
| [PAXG_R04](http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4) | 12 | 24 | 8 | -4.488 | 0 |
| [PAXG_R05](http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8) | 12 | 32 | 6 | -12.311 | 0 |
| [PAXG_U01](http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd) | 32 | 61 | 10 | -14.109 | 0 |
| [PAXG_U02](http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62) | 26 | 59 | 8 | -18.419 | 0 |
| [PAXG_U03](http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d) | 30 | 60 | 10 | -19.108 | 0 |
| [PAXG_U04](http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a) | 29 | 60 | 9 | -21.694 | 0 |
| [PAXG_U05](http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b) | 28 | 60 | 12 | -9.734 | 0 |
| [SPY_C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) | 15 | 33 | 9 | -5.218 | 0 |
| [SPY_Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 15 | 33 | 9 | -5.218 | 0 |
| [SPY_E1](http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0) | 15 | 33 | 9 | -5.218 | 0 |
| [SPY_E2](http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691) | 35 | 57 | 12 | -20.721 | 1 |
| [SPY_E3](http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2) | 40 | 61 | 14 | -11.047 | 1 |
| [SPY_E4](http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5) | 16 | 30 | 9 | -7.469 | 0 |
| [SPY_M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | 15 | 39 | 9 | -7.723 | 1 |
| [SPY_R01](http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41) | 4 | 11 | 2 | -5.313 | 0 |
| [SPY_R02](http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0) | 7 | 12 | 6 | -3.249 | 0 |
| [SPY_R03](http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9) | 9 | 23 | 6 | -5.536 | 0 |
| [SPY_R04](http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c) | 5 | 19 | 4 | -6.364 | 0 |
| [SPY_R05](http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e) | 5 | 9 | 4 | -3.171 | 1 |
| [SPY_U01](http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8) | 29 | 55 | 12 | -11.616 | 1 |
| [SPY_U02](http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b) | 27 | 53 | 12 | -5.579 | 0 |
| [SPY_U03](http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8) | 24 | 56 | 9 | -14.774 | 0 |
| [SPY_U04](http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2) | 20 | 55 | 6 | -18.078 | 0 |
| [SPY_U05](http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841) | 23 | 49 | 11 | -16.982 | 1 |

Fuente completa: ATTRIBUTION_MTM_SOURCE_20261019.md. Se ejecutó inline en run_analysis, con cuatro snapshots de anclaje y hasta seis objetivos por lote. No se ejecutaron scripts del proyecto ni se consultó la base de datos desde análisis.

## Lotes e inputs reproducibles

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
      "job_id": "c530fe6341484b0594ff07c39c6f60fd",
      "targets": [
        {
          "name": "SPY_C0",
          "session_type": "backtest",
          "session_id": "798e6f62-979d-46a2-bf6d-b5983bcb3269"
        },
        {
          "name": "SPY_Cq",
          "session_type": "backtest",
          "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639"
        },
        {
          "name": "SPY_E1",
          "session_type": "backtest",
          "session_id": "a0e806e0-9c7e-49e2-a044-79a32763dce0"
        },
        {
          "name": "PAXG_C0",
          "session_type": "backtest",
          "session_id": "69c90bb0-e2b4-4c6a-a562-edd95399e673"
        }
      ]
    },
    {
      "job_id": "f0a27b5ab32c48e9a16edfe927e96b05",
      "targets": [
        {
          "name": "SPY_E2",
          "session_id": "069cb46d-09a5-4c8e-b164-f9c2d1061691",
          "session_type": "backtest"
        },
        {
          "name": "SPY_E3",
          "session_id": "1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
          "session_type": "backtest"
        },
        {
          "name": "SPY_E4",
          "session_id": "0c2efecc-aa4d-41c4-a9ac-832af72595a5",
          "session_type": "backtest"
        },
        {
          "name": "SPY_M",
          "session_id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_Cq",
          "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_E1",
          "session_id": "4cc65389-4537-4e5a-a4f2-1b008214bb1b",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "55af97e948f34a208cf6d5a6512c56f1",
      "targets": [
        {
          "name": "SPY_R01",
          "session_id": "83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
          "session_type": "backtest"
        },
        {
          "name": "SPY_R02",
          "session_id": "c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
          "session_type": "backtest"
        },
        {
          "name": "SPY_R03",
          "session_id": "205744ff-a7cd-46e8-893b-17e9ebf31fa9",
          "session_type": "backtest"
        },
        {
          "name": "SPY_R04",
          "session_id": "a657dc36-13bd-440f-a423-917ab3caeb8c",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_E2",
          "session_id": "4175efce-ac59-4c16-b23a-278fb6c9b8bc",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_E3",
          "session_id": "831637c7-ade9-4be6-a15b-d568cd5d9242",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "47ed019909d6459b844255000d109fae",
      "targets": [
        {
          "name": "SPY_R05",
          "session_id": "ee7ee861-0137-4d13-a95d-837cb2a3e97e",
          "session_type": "backtest"
        },
        {
          "name": "SPY_U01",
          "session_id": "da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
          "session_type": "backtest"
        },
        {
          "name": "SPY_U02",
          "session_id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
          "session_type": "backtest"
        },
        {
          "name": "SPY_U03",
          "session_id": "63dd9d81-c7bf-417b-823f-728977051fd8",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_E4",
          "session_id": "573cca4f-01b7-4be4-9af3-e64d9a50c837",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_M",
          "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "107e46fda34a48bda73df2e43079ab02",
      "targets": [
        {
          "name": "SPY_U04",
          "session_id": "4ac55781-679a-4d6d-a79a-320f162147b2",
          "session_type": "backtest"
        },
        {
          "name": "SPY_U05",
          "session_id": "37c6ae11-78b0-49c6-9b58-4c9190542841",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_R01",
          "session_id": "fa518c27-144f-4af4-837c-b00c837110b1",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_R02",
          "session_id": "a8e6461e-2b14-4130-b9f6-0989a4483c8c",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_R03",
          "session_id": "0e7552b8-3491-4925-b230-f31c89b92796",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_R04",
          "session_id": "0edfce4f-695a-4213-8426-304b9af6d5a4",
          "session_type": "backtest"
        }
      ]
    },
    {
      "job_id": "13504bb012ae4a4f8d58f131aabb610b",
      "targets": [
        {
          "name": "PAXG_R05",
          "session_id": "cfff7109-04c5-4420-8a90-fc19ceec6ef8",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_U01",
          "session_id": "6cc08024-0aa2-4cdf-a666-25f4351681bd",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_U02",
          "session_id": "4d938a9b-653e-4226-9a1c-899b689e6b62",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_U03",
          "session_id": "e572d0cc-9a77-4998-b2ae-ec335daadf7d",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_U04",
          "session_id": "f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
          "session_type": "backtest"
        },
        {
          "name": "PAXG_U05",
          "session_id": "54613844-7e5d-4911-9342-071f65e0922b",
          "session_type": "backtest"
        }
      ]
    }
  ]
}
```

## Resultados exactos

```json
[
  {
    "name": "PAXG_C0",
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
    "name": "PAXG_E1",
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
      -0.018217340932878745
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.021484473821350547
    ],
    "daily_close_drawdown_pct": -7.406692973003759,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.02783779199863845,
      "2022-12-31 00:00:00+00:00": -0.00889499339509947,
      "2023-12-31 00:00:00+00:00": -0.005746161809683681,
      "2024-12-31 00:00:00+00:00": 0.0513278376957198,
      "2025-12-31 00:00:00+00:00": 0.03914365236513584
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_E2",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 37,
      "positive_months": 22,
      "win_months_all": 0.36065573770491804,
      "win_months_active": 0.5945945945945946,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 38,
    "win_months_all": 0.36507936507936506,
    "win_months_active": 0.6052631578947368,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2024-11-30 00:00:00+00:00",
      -0.024490744700614298
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018854409870361133
    ],
    "daily_close_drawdown_pct": -10.674452139731105,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.03890229787484267,
      "2022-12-31 00:00:00+00:00": -0.018578463494411612,
      "2023-12-31 00:00:00+00:00": -0.026363322519107668,
      "2024-12-31 00:00:00+00:00": 0.13534054459710254,
      "2025-12-31 00:00:00+00:00": 0.3705887139416817
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_E3",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 37,
      "positive_months": 19,
      "win_months_all": 0.3114754098360656,
      "win_months_active": 0.5135135135135135,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 38,
    "win_months_all": 0.31746031746031744,
    "win_months_active": 0.5263157894736842,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2023-02-28 00:00:00+00:00",
      -0.02986995898344824
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.01885424057890739
    ],
    "daily_close_drawdown_pct": -14.747724796307693,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.002430923667209983,
      "2021-12-31 00:00:00+00:00": -0.057096927698631283,
      "2022-12-31 00:00:00+00:00": -0.02771080360990874,
      "2023-12-31 00:00:00+00:00": -0.04413171430261231,
      "2024-12-31 00:00:00+00:00": 0.13534065968714404,
      "2025-12-31 00:00:00+00:00": 0.37058899151379077
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_E4",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.36666666666666664,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 31,
    "win_months_all": 0.1746031746031746,
    "win_months_active": 0.3548387096774194,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2025-02-28 00:00:00+00:00",
      -0.018763549136318836
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018854390952645628
    ],
    "daily_close_drawdown_pct": -6.293534846043114,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.002692195844399947,
      "2021-12-31 00:00:00+00:00": -0.024861477455814573,
      "2022-12-31 00:00:00+00:00": -0.009629617214476194,
      "2023-12-31 00:00:00+00:00": -0.02480286435709811,
      "2024-12-31 00:00:00+00:00": 0.04610253404225717,
      "2025-12-31 00:00:00+00:00": -0.02035204841834992
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
  },
  {
    "name": "PAXG_R01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.36666666666666664,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 31,
    "win_months_all": 0.19047619047619047,
    "win_months_active": 0.3870967741935484,
    "win_quarters": 0.23809523809523808,
    "worst_month": [
      "2021-05-31 00:00:00+00:00",
      -0.012397622566036937
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.018945669735106696
    ],
    "daily_close_drawdown_pct": -8.421614424806378,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.04481948642144451,
      "2022-12-31 00:00:00+00:00": -0.0102872423790219,
      "2023-12-31 00:00:00+00:00": 0.018847820159858975,
      "2024-12-31 00:00:00+00:00": 0.00023233725060345378,
      "2025-12-31 00:00:00+00:00": 0.0493042024612822
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_R02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 28,
      "positive_months": 10,
      "win_months_all": 0.16393442622950818,
      "win_months_active": 0.35714285714285715,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 29,
    "win_months_all": 0.1746031746031746,
    "win_months_active": 0.3793103448275862,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2024-04-30 00:00:00+00:00",
      -0.019123402254934363
    ],
    "worst_quarter": [
      "2024-06-30 00:00:00+00:00",
      -0.019123402254934363
    ],
    "daily_close_drawdown_pct": -8.680467236789092,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.010846381738760624,
      "2021-12-31 00:00:00+00:00": -0.007779488332966378,
      "2022-12-31 00:00:00+00:00": 0.02464169765989288,
      "2023-12-31 00:00:00+00:00": -0.010003301869873304,
      "2024-12-31 00:00:00+00:00": -0.04098446123502919,
      "2025-12-31 00:00:00+00:00": 0.03123367394073795
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_R03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.5666666666666667,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 31,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.5483870967741935,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2025-04-30 00:00:00+00:00",
      -0.013898208224916053
    ],
    "worst_quarter": [
      "2025-06-30 00:00:00+00:00",
      -0.02321793066939737
    ],
    "daily_close_drawdown_pct": -7.2736771785766425,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.029632545045599534,
      "2022-12-31 00:00:00+00:00": -0.018286170214161457,
      "2023-12-31 00:00:00+00:00": 0.03916364267861283,
      "2024-12-31 00:00:00+00:00": 0.061670082565212114,
      "2025-12-31 00:00:00+00:00": 0.0341922431606676
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_R04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 24,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.5,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 25,
    "win_months_all": 0.20634920634920634,
    "win_months_active": 0.52,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2023-07-31 00:00:00+00:00",
      -0.018074479103163732
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.023040459870774188
    ],
    "daily_close_drawdown_pct": -4.48836597574277,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.004444443139090204,
      "2022-12-31 00:00:00+00:00": -0.018283654085210488,
      "2023-12-31 00:00:00+00:00": 0.027840072901222923,
      "2024-12-31 00:00:00+00:00": 0.06864263915856261,
      "2025-12-31 00:00:00+00:00": 0.03890683674461237
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_R05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 32,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.375,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 33,
    "win_months_all": 0.20634920634920634,
    "win_months_active": 0.3939393939393939,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2023-09-30 00:00:00+00:00",
      -0.014256451328876873
    ],
    "worst_quarter": [
      "2024-12-31 00:00:00+00:00",
      -0.018275608709441227
    ],
    "daily_close_drawdown_pct": -12.31074513108734,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.001493534841749744,
      "2021-12-31 00:00:00+00:00": 0.016970331493477264,
      "2022-12-31 00:00:00+00:00": -0.035534752009311,
      "2023-12-31 00:00:00+00:00": -0.03072584562333769,
      "2024-12-31 00:00:00+00:00": -0.03276929387599348,
      "2025-12-31 00:00:00+00:00": 0.09433669579378168
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_U01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 32,
      "win_months_all": 0.5245901639344263,
      "win_months_active": 0.5245901639344263,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 63,
    "win_months_all": 0.5238095238095238,
    "win_months_active": 0.5238095238095238,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2021-06-30 00:00:00+00:00",
      -0.031997117323229185
    ],
    "worst_quarter": [
      "2023-06-30 00:00:00+00:00",
      -0.03568908211922761
    ],
    "daily_close_drawdown_pct": -14.10930869633047,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.035361821148869654,
      "2021-12-31 00:00:00+00:00": -0.0660226550889218,
      "2022-12-31 00:00:00+00:00": -0.009035095051934894,
      "2023-12-31 00:00:00+00:00": 0.04887958951950999,
      "2024-12-31 00:00:00+00:00": 0.17942678942504253,
      "2025-12-31 00:00:00+00:00": 0.16818624075581168
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_U02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 59,
      "positive_months": 26,
      "win_months_all": 0.4262295081967213,
      "win_months_active": 0.4406779661016949,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 61,
    "win_months_all": 0.42857142857142855,
    "win_months_active": 0.4426229508196721,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.03192769436358178
    ],
    "worst_quarter": [
      "2023-06-30 00:00:00+00:00",
      -0.049508508602362444
    ],
    "daily_close_drawdown_pct": -18.418622808332085,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.008494726870673874,
      "2021-12-31 00:00:00+00:00": -0.0431207847002798,
      "2022-12-31 00:00:00+00:00": -0.015758523968678384,
      "2023-12-31 00:00:00+00:00": -0.04054539122194656,
      "2024-12-31 00:00:00+00:00": -0.06663945925287762,
      "2025-12-31 00:00:00+00:00": 0.20027613850060688
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_U03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 60,
      "positive_months": 30,
      "win_months_all": 0.4918032786885246,
      "win_months_active": 0.5,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 62,
    "win_months_all": 0.47619047619047616,
    "win_months_active": 0.4838709677419355,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2021-06-30 00:00:00+00:00",
      -0.051943949835866254
    ],
    "worst_quarter": [
      "2023-06-30 00:00:00+00:00",
      -0.0623891633926158
    ],
    "daily_close_drawdown_pct": -19.108228105716208,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.014606561813999885,
      "2021-12-31 00:00:00+00:00": -0.08166392579525217,
      "2022-12-31 00:00:00+00:00": -0.08413738942739857,
      "2023-12-31 00:00:00+00:00": 0.16397728794836364,
      "2024-12-31 00:00:00+00:00": 0.10247948611314128,
      "2025-12-31 00:00:00+00:00": 0.18575828746241263
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_U04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 60,
      "positive_months": 29,
      "win_months_all": 0.47540983606557374,
      "win_months_active": 0.48333333333333334,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 62,
    "win_months_all": 0.47619047619047616,
    "win_months_active": 0.4838709677419355,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2025-06-30 00:00:00+00:00",
      -0.03072440582425129
    ],
    "worst_quarter": [
      "2022-09-30 00:00:00+00:00",
      -0.06722618368923816
    ],
    "daily_close_drawdown_pct": -21.694133630144496,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.00016752114737639268,
      "2021-12-31 00:00:00+00:00": -0.04300294361059276,
      "2022-12-31 00:00:00+00:00": -0.0843195708733605,
      "2023-12-31 00:00:00+00:00": 0.03140746808244321,
      "2024-12-31 00:00:00+00:00": 0.09938759229757443,
      "2025-12-31 00:00:00+00:00": 0.17395585431077087
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PAXG_U05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 60,
      "positive_months": 28,
      "win_months_all": 0.45901639344262296,
      "win_months_active": 0.4666666666666667,
      "quarters_total": 19,
      "positive_quarters": 12,
      "win_quarters": 0.631578947368421
    },
    "months_total": 63,
    "months_active": 62,
    "win_months_all": 0.4603174603174603,
    "win_months_active": 0.46774193548387094,
    "win_quarters": 0.6190476190476191,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.027126991438533143
    ],
    "worst_quarter": [
      "2023-06-30 00:00:00+00:00",
      -0.04877689518173767
    ],
    "daily_close_drawdown_pct": -9.733970566358085,
    "mtm_route_contribution_correlation": {
      "PAXG-USDT": {
        "PAXG-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.013348785527393714,
      "2021-12-31 00:00:00+00:00": -0.003921832665427782,
      "2022-12-31 00:00:00+00:00": 0.027652032894610823,
      "2023-12-31 00:00:00+00:00": 0.023298237841997915,
      "2024-12-31 00:00:00+00:00": 0.12025462064336812,
      "2025-12-31 00:00:00+00:00": 0.19829849488197904
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_C0",
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
    "name": "SPY_E1",
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
    "name": "SPY_E2",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 57,
      "positive_months": 35,
      "win_months_all": 0.5737704918032787,
      "win_months_active": 0.6140350877192983,
      "quarters_total": 19,
      "positive_quarters": 12,
      "win_quarters": 0.631578947368421
    },
    "months_total": 63,
    "months_active": 58,
    "win_months_all": 0.5714285714285714,
    "win_months_active": 0.6206896551724138,
    "win_quarters": 0.6666666666666666,
    "worst_month": [
      "2025-03-31 00:00:00+00:00",
      -0.058483595547000555
    ],
    "worst_quarter": [
      "2022-06-30 00:00:00+00:00",
      -0.07209362746121839
    ],
    "daily_close_drawdown_pct": -20.72094358027037,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.024557009135047547,
      "2021-12-31 00:00:00+00:00": 0.10250873246054448,
      "2022-12-31 00:00:00+00:00": -0.13136022630302258,
      "2023-12-31 00:00:00+00:00": 0.05148723321980064,
      "2024-12-31 00:00:00+00:00": 0.233557944307752,
      "2025-12-31 00:00:00+00:00": 0.16994632195046444
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_E3",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 61,
      "positive_months": 40,
      "win_months_all": 0.6557377049180327,
      "win_months_active": 0.6557377049180327,
      "quarters_total": 19,
      "positive_quarters": 14,
      "win_quarters": 0.7368421052631579
    },
    "months_total": 63,
    "months_active": 62,
    "win_months_all": 0.6507936507936508,
    "win_months_active": 0.6612903225806451,
    "win_quarters": 0.7619047619047619,
    "worst_month": [
      "2022-04-30 00:00:00+00:00",
      -0.03739814183883827
    ],
    "worst_quarter": [
      "2022-06-30 00:00:00+00:00",
      -0.07209362746121839
    ],
    "daily_close_drawdown_pct": -11.046906465285566,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.024557009135047547,
      "2021-12-31 00:00:00+00:00": 0.10250873246054448,
      "2022-12-31 00:00:00+00:00": -0.08466807860160974,
      "2023-12-31 00:00:00+00:00": 0.09204403430392794,
      "2024-12-31 00:00:00+00:00": 0.1024101599968592,
      "2025-12-31 00:00:00+00:00": 0.08338280828652644
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_E4",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 16,
      "win_months_all": 0.26229508196721313,
      "win_months_active": 0.5333333333333333,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 30,
    "win_months_all": 0.25396825396825395,
    "win_months_active": 0.5333333333333333,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.018022997909986738
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.018022997909986738
    ],
    "daily_close_drawdown_pct": -7.468516914185863,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0026039345991490936,
      "2021-12-31 00:00:00+00:00": 0.020917733115463966,
      "2022-12-31 00:00:00+00:00": -0.015257877185810287,
      "2023-12-31 00:00:00+00:00": -0.02853647804801729,
      "2024-12-31 00:00:00+00:00": 0.008286390270551891,
      "2025-12-31 00:00:00+00:00": 0.009930330413290278
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_M",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 39,
      "positive_months": 15,
      "win_months_all": 0.2459016393442623,
      "win_months_active": 0.38461538461538464,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 40,
    "win_months_all": 0.23809523809523808,
    "win_months_active": 0.375,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.021166658853697617
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.01887544107043493
    ],
    "daily_close_drawdown_pct": -7.723363450254761,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.014446030476585214,
      "2021-12-31 00:00:00+00:00": 0.017154887421644505,
      "2022-12-31 00:00:00+00:00": -0.034141881991372025,
      "2023-12-31 00:00:00+00:00": 0.03263551790955099,
      "2024-12-31 00:00:00+00:00": -0.014174866830556021,
      "2025-12-31 00:00:00+00:00": 0.0005947840244431291
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_R01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 11,
      "positive_months": 4,
      "win_months_all": 0.06557377049180328,
      "win_months_active": 0.36363636363636365,
      "quarters_total": 19,
      "positive_quarters": 2,
      "win_quarters": 0.10526315789473684
    },
    "months_total": 63,
    "months_active": 11,
    "win_months_all": 0.06349206349206349,
    "win_months_active": 0.36363636363636365,
    "win_quarters": 0.14285714285714285,
    "worst_month": [
      "2022-08-31 00:00:00+00:00",
      -0.009169078196212044
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.017272076116690127
    ],
    "daily_close_drawdown_pct": -5.31258150346231,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.016879131639148115,
      "2021-12-31 00:00:00+00:00": 0.003164255024644236,
      "2022-12-31 00:00:00+00:00": -0.009169078196212044,
      "2023-12-31 00:00:00+00:00": -0.0008612090956703344,
      "2024-12-31 00:00:00+00:00": -0.01785676951790205,
      "2025-12-31 00:00:00+00:00": 0
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_R02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 12,
      "positive_months": 7,
      "win_months_all": 0.11475409836065574,
      "win_months_active": 0.5833333333333334,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 12,
    "win_months_all": 0.1111111111111111,
    "win_months_active": 0.5833333333333334,
    "win_quarters": 0.2857142857142857,
    "worst_month": [
      "2024-02-29 00:00:00+00:00",
      -0.01708137068988025
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.01708137068988025
    ],
    "daily_close_drawdown_pct": -3.248913052881297,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.051338418990041434,
      "2022-12-31 00:00:00+00:00": 0.013523231928482371,
      "2023-12-31 00:00:00+00:00": 0.0634730175242646,
      "2024-12-31 00:00:00+00:00": -0.020844555361201555,
      "2025-12-31 00:00:00+00:00": -0.003692641305663269
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_R03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 23,
      "positive_months": 9,
      "win_months_all": 0.14754098360655737,
      "win_months_active": 0.391304347826087,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 23,
    "win_months_all": 0.14285714285714285,
    "win_months_active": 0.391304347826087,
    "win_quarters": 0.2857142857142857,
    "worst_month": [
      "2025-10-31 00:00:00+00:00",
      -0.015980961597637955
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.017938562147956194
    ],
    "daily_close_drawdown_pct": -5.536279910759556,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.021954246660536247,
      "2022-12-31 00:00:00+00:00": 0.005173214227563561,
      "2023-12-31 00:00:00+00:00": 0.011544792284720495,
      "2024-12-31 00:00:00+00:00": -0.005164549736584312,
      "2025-12-31 00:00:00+00:00": -0.017759501263841626
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_R04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 5,
      "win_months_all": 0.08196721311475409,
      "win_months_active": 0.2631578947368421,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 19,
    "win_months_all": 0.07936507936507936,
    "win_months_active": 0.2631578947368421,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2024-10-31 00:00:00+00:00",
      -0.010450871034237585
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.014847718528612774
    ],
    "daily_close_drawdown_pct": -6.364185580100134,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.008753574379017248,
      "2022-12-31 00:00:00+00:00": -0.010452408424848403,
      "2023-12-31 00:00:00+00:00": -0.0038579428640839186,
      "2024-12-31 00:00:00+00:00": -0.019821651365449555,
      "2025-12-31 00:00:00+00:00": 0.007738292844557071
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_R05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 9,
      "positive_months": 5,
      "win_months_all": 0.08196721311475409,
      "win_months_active": 0.5555555555555556,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 10,
    "win_months_all": 0.07936507936507936,
    "win_months_active": 0.5,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2023-02-28 00:00:00+00:00",
      -0.009256970820865407
    ],
    "worst_quarter": [
      "2023-03-31 00:00:00+00:00",
      -0.009256970820865407
    ],
    "daily_close_drawdown_pct": -3.1705927902179742,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.025865401643248687,
      "2022-12-31 00:00:00+00:00": 0,
      "2023-12-31 00:00:00+00:00": -0.019208296139106795,
      "2024-12-31 00:00:00+00:00": 0.002469076388558644,
      "2025-12-31 00:00:00+00:00": 0.005622342575300809
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_U01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 55,
      "positive_months": 29,
      "win_months_all": 0.47540983606557374,
      "win_months_active": 0.5272727272727272,
      "quarters_total": 19,
      "positive_quarters": 12,
      "win_quarters": 0.631578947368421
    },
    "months_total": 63,
    "months_active": 56,
    "win_months_all": 0.4603174603174603,
    "win_months_active": 0.5178571428571429,
    "win_quarters": 0.6190476190476191,
    "worst_month": [
      "2024-04-30 00:00:00+00:00",
      -0.029672809154923874
    ],
    "worst_quarter": [
      "2024-12-31 00:00:00+00:00",
      -0.033017883663585934
    ],
    "daily_close_drawdown_pct": -11.61565814692982,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.027461571791044026,
      "2021-12-31 00:00:00+00:00": 0.05466753989836315,
      "2022-12-31 00:00:00+00:00": 0.05225732095490487,
      "2023-12-31 00:00:00+00:00": 0.12518930626410874,
      "2024-12-31 00:00:00+00:00": -0.08143831021684456,
      "2025-12-31 00:00:00+00:00": 0.0076179505752962395
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_U02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 53,
      "positive_months": 27,
      "win_months_all": 0.4426229508196721,
      "win_months_active": 0.5094339622641509,
      "quarters_total": 19,
      "positive_quarters": 12,
      "win_quarters": 0.631578947368421
    },
    "months_total": 63,
    "months_active": 54,
    "win_months_all": 0.42857142857142855,
    "win_months_active": 0.5,
    "win_quarters": 0.6666666666666666,
    "worst_month": [
      "2024-04-30 00:00:00+00:00",
      -0.03183048005371858
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.033528723961775975
    ],
    "daily_close_drawdown_pct": -5.578679310841405,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.0022875489553784156,
      "2021-12-31 00:00:00+00:00": 0.07015102078232038,
      "2022-12-31 00:00:00+00:00": -0.013766843000245443,
      "2023-12-31 00:00:00+00:00": 0.0491817387630713,
      "2024-12-31 00:00:00+00:00": 0.12075908225563992,
      "2025-12-31 00:00:00+00:00": 0.01071624917194991
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_U03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 56,
      "positive_months": 24,
      "win_months_all": 0.39344262295081966,
      "win_months_active": 0.42857142857142855,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 57,
    "win_months_all": 0.38095238095238093,
    "win_months_active": 0.42105263157894735,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-08-31 00:00:00+00:00",
      -0.031863125108096746
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.05789517080990869
    ],
    "daily_close_drawdown_pct": -14.774425567617278,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.030942196606327688,
      "2021-12-31 00:00:00+00:00": 0.08475654451449799,
      "2022-12-31 00:00:00+00:00": -0.09719175074514763,
      "2023-12-31 00:00:00+00:00": 0.01152843719511032,
      "2024-12-31 00:00:00+00:00": -0.011573238853110235,
      "2025-12-31 00:00:00+00:00": -0.052976695114507644
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_U04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 55,
      "positive_months": 20,
      "win_months_all": 0.32786885245901637,
      "win_months_active": 0.36363636363636365,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 56,
    "win_months_all": 0.31746031746031744,
    "win_months_active": 0.35714285714285715,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2021-09-30 00:00:00+00:00",
      -0.04362306022814111
    ],
    "worst_quarter": [
      "2021-09-30 00:00:00+00:00",
      -0.04210413350067965
    ],
    "daily_close_drawdown_pct": -18.07843793686279,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.03011891491753471,
      "2021-12-31 00:00:00+00:00": -0.0657014166920249,
      "2022-12-31 00:00:00+00:00": -0.07112299901088726,
      "2023-12-31 00:00:00+00:00": 0.021329063680240345,
      "2024-12-31 00:00:00+00:00": -0.031755488574331525,
      "2025-12-31 00:00:00+00:00": 0.009494120674871542
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "SPY_U05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 49,
      "positive_months": 23,
      "win_months_all": 0.3770491803278688,
      "win_months_active": 0.46938775510204084,
      "quarters_total": 19,
      "positive_quarters": 11,
      "win_quarters": 0.5789473684210527
    },
    "months_total": 63,
    "months_active": 51,
    "win_months_all": 0.38095238095238093,
    "win_months_active": 0.47058823529411764,
    "win_quarters": 0.5714285714285714,
    "worst_month": [
      "2022-12-31 00:00:00+00:00",
      -0.033067729364404164
    ],
    "worst_quarter": [
      "2024-06-30 00:00:00+00:00",
      -0.04738996663352668
    ],
    "daily_close_drawdown_pct": -16.98190577412436,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.016761224639513017,
      "2021-12-31 00:00:00+00:00": 0.08556697133852054,
      "2022-12-31 00:00:00+00:00": -0.06179138302673004,
      "2023-12-31 00:00:00+00:00": -0.046092118009412486,
      "2024-12-31 00:00:00+00:00": 0.008853606459822139,
      "2025-12-31 00:00:00+00:00": 0.0455081989447661
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  }
]
```
