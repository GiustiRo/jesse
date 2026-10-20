# SPY Structural R1 — auditoría MTM

Las doce variantes concilian contra wallet. Jobs PB `b7ed075be282430e8ce8fd78bde752f6` y BR `4161d43204da46aeb06a959be1836d61`, ambos succeeded. Cada job conserva `calendar_audit.json` y CSV mensuales, contribuciones y equity por variante. Fuente en SPY_STRUCT_R1_MTM_SOURCE_20261019.md.

SPY tiene 19 fills MARKET en 16 timestamps ancla; error relativo máximo 1.78e-15. Los otros símbolos sólo aportan controles históricos de valoración y no fueron investigados en esta ronda.

Denominadores comparables: 61 meses y 19 trimestres completos. Los 63 meses y 21 trimestres que incluyen fronteras parciales se informan aparte. El drawdown usa cierre diario UTC. Se lleva la última marca durante cierres para valoración; esto no permite ejecutar allí. Las liquidaciones terminales conciliadas no prueban liquidez real.

```json
[
  {
    "name": "BR01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 27,
      "positive_months": 9,
      "win_months_all": 0.14754098360655737,
      "win_months_active": 0.3333333333333333,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 27,
    "win_months_all": 0.14285714285714285,
    "win_months_active": 0.3333333333333333,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2022-08-31 00:00:00+00:00",
      -0.009278789146616173
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.026571153556522398
    ],
    "daily_close_drawdown_pct": -6.824837786974003,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.004062982368620016,
      "2022-12-31 00:00:00+00:00": -0.016734820162239594,
      "2023-12-31 00:00:00+00:00": 0.027272841649619073,
      "2024-12-31 00:00:00+00:00": -0.009950966349105528,
      "2025-12-31 00:00:00+00:00": 0.011260443795854336
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "BR02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 18,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 18,
    "win_months_all": 0.19047619047619047,
    "win_months_active": 0.6666666666666666,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.017251603569075846
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.026281354202079332
    ],
    "daily_close_drawdown_pct": -3.8052545389172465,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.006611731745005955,
      "2024-12-31 00:00:00+00:00": 0.03387460745680149,
      "2025-12-31 00:00:00+00:00": 0.03064486063997074
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "BR03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 13,
      "positive_months": 6,
      "win_months_all": 0.09836065573770492,
      "win_months_active": 0.46153846153846156,
      "quarters_total": 19,
      "positive_quarters": 3,
      "win_quarters": 0.15789473684210525
    },
    "months_total": 63,
    "months_active": 13,
    "win_months_all": 0.09523809523809523,
    "win_months_active": 0.46153846153846156,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.00862824264748474
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.017165926173766333
    ],
    "daily_close_drawdown_pct": -4.415446777914589,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.016879131639148115,
      "2021-12-31 00:00:00+00:00": 0.021097608382974364,
      "2022-12-31 00:00:00+00:00": -0.004491941946593858,
      "2023-12-31 00:00:00+00:00": -0.025348482219247792,
      "2024-12-31 00:00:00+00:00": 0.01480975334626522,
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
    "name": "BR04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 9,
      "positive_months": 6,
      "win_months_all": 0.09836065573770492,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 9,
    "win_months_all": 0.09523809523809523,
    "win_months_active": 0.6666666666666666,
    "win_quarters": 0.2857142857142857,
    "worst_month": [
      "2023-09-30 00:00:00+00:00",
      -0.008956409338545468
    ],
    "worst_quarter": [
      "2023-09-30 00:00:00+00:00",
      -0.008956409338545468
    ],
    "daily_close_drawdown_pct": -2.1637473463862023,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0,
      "2022-12-31 00:00:00+00:00": 0.0070079190063616625,
      "2023-12-31 00:00:00+00:00": -0.008956409338545468,
      "2024-12-31 00:00:00+00:00": 0.02365180918434695,
      "2025-12-31 00:00:00+00:00": 0.04042559407506818
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "BR05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 6,
      "positive_months": 5,
      "win_months_all": 0.08196721311475409,
      "win_months_active": 0.8333333333333334,
      "quarters_total": 19,
      "positive_quarters": 2,
      "win_quarters": 0.10526315789473684
    },
    "months_total": 63,
    "months_active": 6,
    "win_months_all": 0.07936507936507936,
    "win_months_active": 0.8333333333333334,
    "win_quarters": 0.14285714285714285,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.008626819126849261
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.008626819126849261
    ],
    "daily_close_drawdown_pct": -1.852637552113734,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.016454833250295398,
      "2021-12-31 00:00:00+00:00": 0.027242795774951922,
      "2022-12-31 00:00:00+00:00": 0,
      "2023-12-31 00:00:00+00:00": -0.008626819126849261,
      "2024-12-31 00:00:00+00:00": 0.007673471627725803,
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
    "name": "BR06",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 5,
      "positive_months": 3,
      "win_months_all": 0.04918032786885246,
      "win_months_active": 0.6,
      "quarters_total": 19,
      "positive_quarters": 2,
      "win_quarters": 0.10526315789473684
    },
    "months_total": 63,
    "months_active": 5,
    "win_months_all": 0.047619047619047616,
    "win_months_active": 0.6,
    "win_quarters": 0.09523809523809523,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.008626791462859384
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.008626791462859384
    ],
    "daily_close_drawdown_pct": -2.6460592477332012,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.027304463784447064,
      "2022-12-31 00:00:00+00:00": 0,
      "2023-12-31 00:00:00+00:00": -0.016880208112397987,
      "2024-12-31 00:00:00+00:00": 0.007916592635173636,
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
    "name": "PB01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 42,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.40476190476190477,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 43,
    "win_months_all": 0.2857142857142857,
    "win_months_active": 0.4186046511627907,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.020992252308142167
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.033851217250082666
    ],
    "daily_close_drawdown_pct": -13.10187509702595,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.009702437104957662,
      "2021-12-31 00:00:00+00:00": 0.040581272080096875,
      "2022-12-31 00:00:00+00:00": -0.018786534982897618,
      "2023-12-31 00:00:00+00:00": 0.0020354636740320675,
      "2024-12-31 00:00:00+00:00": -0.02726996641004431,
      "2025-12-31 00:00:00+00:00": -0.06210556713319049
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PB02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 30,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.26666666666666666,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 31,
    "win_months_all": 0.12698412698412698,
    "win_months_active": 0.25806451612903225,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2023-11-30 00:00:00+00:00",
      -0.017303620282308696
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.02934392442228162
    ],
    "daily_close_drawdown_pct": -14.000676339588535,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": -0.009367371989239426,
      "2021-12-31 00:00:00+00:00": 0.016925618954782173,
      "2022-12-31 00:00:00+00:00": 0.004047542070221732,
      "2023-12-31 00:00:00+00:00": -0.055490032496941954,
      "2024-12-31 00:00:00+00:00": -0.032674074902920736,
      "2025-12-31 00:00:00+00:00": -0.026874877341370174
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PB03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 9,
      "win_months_all": 0.14754098360655737,
      "win_months_active": 0.47368421052631576,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 19,
    "win_months_all": 0.14285714285714285,
    "win_months_active": 0.47368421052631576,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.009486907666097943
    ],
    "worst_quarter": [
      "2024-12-31 00:00:00+00:00",
      -0.01711656030096964
    ],
    "daily_close_drawdown_pct": -4.683094434836144,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.01427211385950189,
      "2022-12-31 00:00:00+00:00": -0.004254960550497233,
      "2023-12-31 00:00:00+00:00": 0.012553328044858647,
      "2024-12-31 00:00:00+00:00": -0.023728017627781317,
      "2025-12-31 00:00:00+00:00": 0.04042760797008804
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PB04",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 8,
      "positive_months": 4,
      "win_months_all": 0.06557377049180328,
      "win_months_active": 0.5,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 8,
    "win_months_all": 0.06349206349206349,
    "win_months_active": 0.5,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2024-10-31 00:00:00+00:00",
      -0.008817395915638016
    ],
    "worst_quarter": [
      "2024-12-31 00:00:00+00:00",
      -0.008817395915638016
    ],
    "daily_close_drawdown_pct": -2.9379356647549315,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.017381215876241418,
      "2022-12-31 00:00:00+00:00": 0.010232442157922073,
      "2023-12-31 00:00:00+00:00": -0.008613050208230444,
      "2024-12-31 00:00:00+00:00": -0.005082819779414716,
      "2025-12-31 00:00:00+00:00": 0.03990914672957624
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PB05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 43,
      "positive_months": 17,
      "win_months_all": 0.2786885245901639,
      "win_months_active": 0.3953488372093023,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 44,
    "win_months_all": 0.2698412698412698,
    "win_months_active": 0.38636363636363635,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2024-03-31 00:00:00+00:00",
      -0.020679558145326626
    ],
    "worst_quarter": [
      "2023-03-31 00:00:00+00:00",
      -0.025657184124275978
    ],
    "daily_close_drawdown_pct": -7.762997600045207,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.016879131639148115,
      "2021-12-31 00:00:00+00:00": 0.020392750842648466,
      "2022-12-31 00:00:00+00:00": -0.017137626811106532,
      "2023-12-31 00:00:00+00:00": 0.00633153724174762,
      "2024-12-31 00:00:00+00:00": -0.007682886650699716,
      "2025-12-31 00:00:00+00:00": -0.022340412538852994
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "PB06",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.42105263157894735,
      "quarters_total": 19,
      "positive_quarters": 6,
      "win_quarters": 0.3157894736842105
    },
    "months_total": 63,
    "months_active": 20,
    "win_months_all": 0.12698412698412698,
    "win_months_active": 0.4,
    "win_quarters": 0.2857142857142857,
    "worst_month": [
      "2025-01-31 00:00:00+00:00",
      -0.01132432044814402
    ],
    "worst_quarter": [
      "2024-03-31 00:00:00+00:00",
      -0.026169168591028247
    ],
    "daily_close_drawdown_pct": -6.275390218471443,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.04992597928939513,
      "2022-12-31 00:00:00+00:00": -0.0038191871605183225,
      "2023-12-31 00:00:00+00:00": 0.06868838974575397,
      "2024-12-31 00:00:00+00:00": -0.032041291803958205,
      "2025-12-31 00:00:00+00:00": -0.022892757573836353
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
