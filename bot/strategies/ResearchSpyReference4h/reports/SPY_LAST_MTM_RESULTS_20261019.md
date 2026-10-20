# SPY última ronda — MTM y equivalencias exactas

Doce variantes conciliadas contra wallet. MECH job `9cb3ee898ad840b9b1e435e94a9c6408`; RESET `39c5fd2539894967886c6ac977cbfb00`, ambos succeeded. Artefactos calendar_audit.json y path_fingerprints.json más CSV de equity diario, retornos mensuales y contribuciones. Fuente SPY_LAST_MTM_SOURCE_20261019.md.

Nueve trayectorias económicas y Portfolio diferentes entre doce implementaciones; grupos duplicados RESET01=RESET04, RESET02=RESET03, RESET05=MECH04 (esta última también esBR02, confirmado por auditor del especialista). No son doce muestras independientes; las nueve trayectorias tampoco lo son al compartir activo e historia.

Los denominadores completos son61meses/19Q. Las fronteras parciales aparecen aparte en JSON. No sustituir meses activos por todos los meses. DD diarioUTC no es DDmotor ni intradiario. Llevar última marca en cierres sólo permite valoración, no ejecución. Liquidaciones terminales conciliadas no prueban liquidez real.

## MTM exacto

```json
[
  {
    "name": "RESET01",
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
      -0.01725170328140535
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.026281556546199236
    ],
    "daily_close_drawdown_pct": -3.377824052233147,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.0075973791266624735,
      "2024-12-31 00:00:00+00:00": 0.03387432219110309,
      "2025-12-31 00:00:00+00:00": 0.030646358412416363
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "RESET02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.631578947368421,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 19,
    "win_months_all": 0.19047619047619047,
    "win_months_active": 0.631578947368421,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.017251862082575897
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.03460125865436736
    ],
    "daily_close_drawdown_pct": -4.203389082350517,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.01509970258912241,
      "2024-12-31 00:00:00+00:00": 0.03387467408455569,
      "2025-12-31 00:00:00+00:00": 0.030646624937632483
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "RESET03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 12,
      "win_months_all": 0.19672131147540983,
      "win_months_active": 0.631578947368421,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 19,
    "win_months_all": 0.19047619047619047,
    "win_months_active": 0.631578947368421,
    "win_quarters": 0.47619047619047616,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.017251862082575897
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.03460125865436736
    ],
    "daily_close_drawdown_pct": -4.203389082350517,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.01509970258912241,
      "2024-12-31 00:00:00+00:00": 0.03387467408455569,
      "2025-12-31 00:00:00+00:00": 0.030646624937632483
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "RESET04",
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
      -0.01725170328140535
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.026281556546199236
    ],
    "daily_close_drawdown_pct": -3.377824052233147,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.0075973791266624735,
      "2024-12-31 00:00:00+00:00": 0.03387432219110309,
      "2025-12-31 00:00:00+00:00": 0.030646358412416363
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "RESET05",
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
    "name": "RESET06",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 17,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.6470588235294118,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 17,
    "win_months_all": 0.1746031746031746,
    "win_months_active": 0.6470588235294118,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2023-12-31 00:00:00+00:00",
      -0.01725159846674007
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.026281607928279493
    ],
    "daily_close_drawdown_pct": -4.994774840076744,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.024302242109720096,
      "2022-12-31 00:00:00+00:00": -0.010659830545948767,
      "2023-12-31 00:00:00+00:00": -0.026428701977387226,
      "2024-12-31 00:00:00+00:00": 0.033874220434827684,
      "2025-12-31 00:00:00+00:00": 0.03064457937784093
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "MECH01",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 11,
      "win_months_all": 0.18032786885245902,
      "win_months_active": 0.7857142857142857,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 14,
    "win_months_all": 0.1746031746031746,
    "win_months_active": 0.7857142857142857,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.009471692110328722
    ],
    "worst_quarter": [
      "2023-12-31 00:00:00+00:00",
      -0.017761942357884863
    ],
    "daily_close_drawdown_pct": -2.5324294510837952,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.01379795132820405,
      "2021-12-31 00:00:00+00:00": 0.033297468894396776,
      "2022-12-31 00:00:00+00:00": -0.009471692110328722,
      "2023-12-31 00:00:00+00:00": 0.011159710782616017,
      "2024-12-31 00:00:00+00:00": 0.033874379710593816,
      "2025-12-31 00:00:00+00:00": 0.030646874566655713
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "MECH02",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 9,
      "win_months_all": 0.14754098360655737,
      "win_months_active": 0.6428571428571429,
      "quarters_total": 19,
      "positive_quarters": 8,
      "win_quarters": 0.42105263157894735
    },
    "months_total": 63,
    "months_active": 14,
    "win_months_all": 0.14285714285714285,
    "win_months_active": 0.6428571428571429,
    "win_quarters": 0.38095238095238093,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.008979251610723438
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.008705081424618455
    ],
    "daily_close_drawdown_pct": -2.345984183826444,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.023267786886883135,
      "2022-12-31 00:00:00+00:00": -0.0011998348838461181,
      "2023-12-31 00:00:00+00:00": 0.009810924816268107,
      "2024-12-31 00:00:00+00:00": 0.002611899664418438,
      "2025-12-31 00:00:00+00:00": 0.04087118126509193
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "MECH03",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 13,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.6153846153846154,
      "quarters_total": 19,
      "positive_quarters": 7,
      "win_quarters": 0.3684210526315789
    },
    "months_total": 63,
    "months_active": 13,
    "win_months_all": 0.12698412698412698,
    "win_months_active": 0.6153846153846154,
    "win_quarters": 0.3333333333333333,
    "worst_month": [
      "2023-05-31 00:00:00+00:00",
      -0.008979251610723438
    ],
    "worst_quarter": [
      "2021-06-30 00:00:00+00:00",
      -0.008705081424618455
    ],
    "daily_close_drawdown_pct": -2.345984183826444,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.023267786886883135,
      "2022-12-31 00:00:00+00:00": -0.0011998348838461181,
      "2023-12-31 00:00:00+00:00": 0.009810924816268107,
      "2024-12-31 00:00:00+00:00": -0.004144469962367503,
      "2025-12-31 00:00:00+00:00": 0.04087123922323621
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "MECH04",
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
    "daily_close_drawdown_pct": -3.8052545389172687,
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
    "name": "MECH05",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 21,
      "positive_months": 14,
      "win_months_all": 0.22950819672131148,
      "win_months_active": 0.6666666666666666,
      "quarters_total": 19,
      "positive_quarters": 10,
      "win_quarters": 0.5263157894736842
    },
    "months_total": 63,
    "months_active": 22,
    "win_months_all": 0.2222222222222222,
    "win_months_active": 0.6363636363636364,
    "win_quarters": 0.5238095238095238,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.009471393376186854
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.009471393376186854
    ],
    "daily_close_drawdown_pct": -3.5742676350636216,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0.012887328631389527,
      "2021-12-31 00:00:00+00:00": 0.013996459252863191,
      "2022-12-31 00:00:00+00:00": -0.006653141062306855,
      "2023-12-31 00:00:00+00:00": 0.048955652537825856,
      "2024-12-31 00:00:00+00:00": 0.028786424784009945,
      "2025-12-31 00:00:00+00:00": 0.024099138270455178
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 1,
      "boundary_liquidations_reconciled": 1,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "MECH06",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 14,
      "positive_months": 10,
      "win_months_all": 0.16393442622950818,
      "win_months_active": 0.7142857142857143,
      "quarters_total": 19,
      "positive_quarters": 9,
      "win_quarters": 0.47368421052631576
    },
    "months_total": 63,
    "months_active": 14,
    "win_months_all": 0.15873015873015872,
    "win_months_active": 0.7142857142857143,
    "win_quarters": 0.42857142857142855,
    "worst_month": [
      "2022-11-30 00:00:00+00:00",
      -0.009471528240724947
    ],
    "worst_quarter": [
      "2022-12-31 00:00:00+00:00",
      -0.009471528240724947
    ],
    "daily_close_drawdown_pct": -2.933748671548664,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.018958210941171005,
      "2022-12-31 00:00:00+00:00": -0.010660027149138607,
      "2023-12-31 00:00:00+00:00": 0.020515831040002874,
      "2024-12-31 00:00:00+00:00": 0.03387402031857434,
      "2025-12-31 00:00:00+00:00": 0.030644722918932388
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

## Hashes exactos

```json
{
  "RESET01": {
    "economic_path_sha256": "4292e65b837bc7a0057e32a2b34f67d20623251b7df20538dfdef6d576415776",
    "portfolio_curve_sha256": "9bd6ce3315b59cbdb5b46f9c4ced1ff3689aeb0bb8a1feb52c4f950bc6453295",
    "n": 16
  },
  "RESET02": {
    "economic_path_sha256": "fb1f2b5643f9c1472290df4788d1ea2138f2253acd1a86c1e6a728efadbae436",
    "portfolio_curve_sha256": "1659e17b393d88deac8cf8c08a35696fcf8a81588718ad8cd05f1ff219b3a3da",
    "n": 17
  },
  "RESET03": {
    "economic_path_sha256": "fb1f2b5643f9c1472290df4788d1ea2138f2253acd1a86c1e6a728efadbae436",
    "portfolio_curve_sha256": "1659e17b393d88deac8cf8c08a35696fcf8a81588718ad8cd05f1ff219b3a3da",
    "n": 17
  },
  "RESET04": {
    "economic_path_sha256": "4292e65b837bc7a0057e32a2b34f67d20623251b7df20538dfdef6d576415776",
    "portfolio_curve_sha256": "9bd6ce3315b59cbdb5b46f9c4ced1ff3689aeb0bb8a1feb52c4f950bc6453295",
    "n": 16
  },
  "RESET05": {
    "economic_path_sha256": "70d7da39ab685a48946bdf4b96c4f0df7646efdcb26840ad5a20b4814a229995",
    "portfolio_curve_sha256": "7b54105fc9279c9ab1f09ea866c20d6563941ad9eba98c375e6841332a183dd6",
    "n": 16
  },
  "RESET06": {
    "economic_path_sha256": "4ce7685949694fff827b2b82d2a89974e6afffd8fe43df612fc835007907c31d",
    "portfolio_curve_sha256": "3ab1a67406fa8d15f8a9d616556c0a9b5e1c19ea9d3f1749c27758501f38eb0e",
    "n": 15
  },
  "MECH01": {
    "economic_path_sha256": "bb7d4cc03a97c1aa3a2b314632b53ed5fccf7e0d9e778997985703ca9c9c8ccf",
    "portfolio_curve_sha256": "86e09803c370132a2efa37126a0eed7bb485f9fac7524b5874b63e88023ebc49",
    "n": 12
  },
  "MECH02": {
    "economic_path_sha256": "944ca85d690d24e790cffb4d6c19781f06206bd1a4501415ea49754c24a44216",
    "portfolio_curve_sha256": "72fddabfc37879262af263ab79be1c9dc02c46e81510048f32733d9c6abd92d8",
    "n": 11
  },
  "MECH03": {
    "economic_path_sha256": "e07a00b5e6e3610dc10c54f3b219baa369733e509be4e47fcbb42303118ea002",
    "portfolio_curve_sha256": "0b9194b4a497b9a8e732a9109ab00496e95e74da1427b81079fbe38077d0bc6d",
    "n": 10
  },
  "MECH04": {
    "economic_path_sha256": "70d7da39ab685a48946bdf4b96c4f0df7646efdcb26840ad5a20b4814a229995",
    "portfolio_curve_sha256": "7b54105fc9279c9ab1f09ea866c20d6563941ad9eba98c375e6841332a183dd6",
    "n": 16
  },
  "MECH05": {
    "economic_path_sha256": "3a68eff9a3f565f648803fa045e1f05ed63b4adaab0792622ab0d30612df1710",
    "portfolio_curve_sha256": "dd35010a345535c54f69a1cd38144f09d38a879dd66d29b56921973e5c712de3",
    "n": 19
  },
  "MECH06": {
    "economic_path_sha256": "21660ea22f90c1873431741599156e28dfc75ae55c6d491243c36b72ca45a238",
    "portfolio_curve_sha256": "8e669f91462c94e240b4255e929479679151d32acd65126d177b04912aa100e2",
    "n": 12
  }
}
```
