# SPY C0 — paridad exacta confirmada

[C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) y [referencia](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2). Job bd025776037f4d36865689f7b27312b8 succeeded sobre ambos snapshots completos. Fuente ATTRIBUTION_SPY_PARITY_SOURCE_20261019.md.

```json
{"parity_pass": true, "trades": 31, "net": 751.3477149671152, "fees": 286.47552620734854, "maxdiff": {"opened_at": 0.0, "closed_at": 0.0, "entry_price": 0.0, "exit_price": 0.0, "qty": 0.0, "PNL": 0.0, "fee": 0.0, "holding_period": 0.0}, "executed_orders_equal": true, "equitycurve_equal": true}
```

31 trades económicamente idénticos: timestamps entrada/salida, precios, cantidad, PnL, fee, duración con diferencia cero; órdenes ejecutadas por campos económicos iguales; curva completa exacta; net751.3477149671152, fees286.47552620734854, balancefinal10751.34771496711. No se usan UUID como criterio. Este control reproduce la referencia, no agrega evidencia de alpha. Otras16 esperan liberación root tras revisión de este resultado.