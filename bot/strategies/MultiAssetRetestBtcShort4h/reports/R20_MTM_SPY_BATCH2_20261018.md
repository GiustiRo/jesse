# R20: auditoría MTM SPY07/08/09

Análisis266bb0fcee334fb28b5e9ed5b7d278b6 succeeded; misma metodología V4 de fills y cierre UTC del batch1,16anclasSPY error2.22e−15. Terminal reconciliado enlos3. 04/10sin fillsymétricasno se fabrican ratios. Ventana2020-10-15 a2025-12-31exclusiva,2026cerrado; desarrollo seleccionado, no OOS. DD a cierre diario no reemplaza motor. Los objetivos de regularidad corresponden al portfolio.

```json
[
  {
    "name": "spy07",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 9,
      "positive_months": 4,
      "win_months_all": 0.06557377049180328,
      "win_months_active": 0.4444444444444444,
      "quarters_total": 19,
      "positive_quarters": 2,
      "win_quarters": 0.10526315789473684
    },
    "months_total": 63,
    "months_active": 10,
    "win_months_all": 0.07936507936507936,
    "win_months_active": 0.5,
    "win_quarters": 0.14285714285714285,
    "worst_month": [
      "2025-03-31 00:00:00+00:00",
      -0.015587611710946359
    ],
    "worst_quarter": [
      "2024-09-30 00:00:00+00:00",
      -0.009654613695917025
    ],
    "daily_close_drawdown_pct": -3.203934776091688,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0.02224275486872096,
      "2022-12-31 00:00:00+00:00": 0,
      "2023-12-31 00:00:00+00:00": 0,
      "2024-12-31 00:00:00+00:00": -0.011401554227219113,
      "2025-12-31 00:00:00+00:00": -0.0028447343022851568
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy08",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 11,
      "positive_months": 7,
      "win_months_all": 0.11475409836065574,
      "win_months_active": 0.6363636363636364,
      "quarters_total": 19,
      "positive_quarters": 3,
      "win_quarters": 0.15789473684210525
    },
    "months_total": 63,
    "months_active": 11,
    "win_months_all": 0.1111111111111111,
    "win_months_active": 0.6363636363636364,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2025-04-30 00:00:00+00:00",
      -0.009752908535062832
    ],
    "worst_quarter": [
      "2025-06-30 00:00:00+00:00",
      -0.009752908535062832
    ],
    "daily_close_drawdown_pct": -2.9830735665379082,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": 0,
      "2022-12-31 00:00:00+00:00": 0.02344894310436696,
      "2023-12-31 00:00:00+00:00": 0,
      "2024-12-31 00:00:00+00:00": -0.007330770694847333,
      "2025-12-31 00:00:00+00:00": -0.017833092471986167
    },
    "terminal_reconciles": true,
    "terminal_diagnostics": {
      "pretermination_open_counter": 0,
      "boundary_liquidations_reconciled": 0,
      "boundary_close_is_execution_liquidity_proof": false
    }
  },
  {
    "name": "spy09",
    "method": "UTC day-close MTM from executed fills, right-edge inclusive",
    "partial_boundary_periods_included": true,
    "complete_periods": {
      "months_total": 61,
      "months_active": 19,
      "positive_months": 8,
      "win_months_all": 0.13114754098360656,
      "win_months_active": 0.42105263157894735,
      "quarters_total": 19,
      "positive_quarters": 4,
      "win_quarters": 0.21052631578947367
    },
    "months_total": 63,
    "months_active": 19,
    "win_months_all": 0.12698412698412698,
    "win_months_active": 0.42105263157894735,
    "win_quarters": 0.19047619047619047,
    "worst_month": [
      "2022-10-31 00:00:00+00:00",
      -0.009785093596315297
    ],
    "worst_quarter": [
      "2022-03-31 00:00:00+00:00",
      -0.014727473742082164
    ],
    "daily_close_drawdown_pct": -4.093583380704691,
    "mtm_route_contribution_correlation": {
      "SPY-USDT": {
        "SPY-USDT": 1
      }
    },
    "yearly_returns": {
      "2020-12-31 00:00:00+00:00": 0,
      "2021-12-31 00:00:00+00:00": -0.009794056244725846,
      "2022-12-31 00:00:00+00:00": -0.02436845762939399,
      "2023-12-31 00:00:00+00:00": 0.007262696356386211,
      "2024-12-31 00:00:00+00:00": -0.006216401966395169,
      "2025-12-31 00:00:00+00:00": 0.011986965229874746
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
