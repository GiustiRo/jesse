# BTC R7 — control de observación

O700B/C reproducen económicamente N503B/C:264/271operaciones, todos lostiempos/tipos/precios/cantidades/fees/PNLidénticos, tolerancia1e-7 ydifmáxima0. Nuevas corridascontrol no añaden evidencia de ventaja. Auditorfills/wallet/terminal/MTMpassed.375contextosR,11418decisiones,82eventosN503,11ocupados,67fills/closesambas. R es preparación técnica: no afirmar375entradas ejecutables. Log de observación queda en sesiones sin borrar informes previos. Registro no altera originales;noeventoscontrafactuales.

- [O700B](http://localhost:9200/#/backtest/8d6837b4-51a5-4128-91f8-a8c7608c5e74)
- [O700C](http://localhost:9200/#/backtest/8210a2a5-1376-457d-b096-1baccacd5d1a)

```json
{
  "paths": {
    "O700B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 260,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 39.324442829776444,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 264,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    },
    "O700C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 267,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 39.32444282977622,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 271,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    }
  },
  "logs": {
    "O700B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_R7_OBSERVER_COUNTS {\"context\": 375, \"decisions\": 11418, \"source_event\": 82, \"source_occupied\": 11}",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"N503\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ObserveR700\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "O700C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_R7_OBSERVER_COUNTS {\"context\": 375, \"decisions\": 11418, \"source_event\": 82, \"source_occupied\": 11}",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"N503\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ObserveR700\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  }
}
```
