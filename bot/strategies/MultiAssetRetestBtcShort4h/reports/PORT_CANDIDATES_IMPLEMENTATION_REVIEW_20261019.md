# Portfolio — revisión de seis fuentes antes de correr

Las seis copias fueron creadas y leídas de vuelta por MCP con igualdad exacta. Al quitar clase, imports de diagnóstico, dos llamadas a _record_capacity y métodos de diagnóstico, la fuente vuelve byte por byte a su base, salvo TRADE_RISK de la copiaBTC1% en vez3%. No cambiaron señales/salidas ni calendario. _ledger/_committed/_capital/_volatility_share son idénticos en las seis bases y usan shared_vars phase2_reservations. Mismo orden de rutasBTC/PAXG/SPY.

```json
[
  {
    "name": "PortCompareBtc4h",
    "base": "MultiAssetRetestBtcShort4h",
    "normalized_identical": true
  },
  {
    "name": "PortComparePaxgRetest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "normalized_identical": true
  },
  {
    "name": "PortComparePaxgMarket4h",
    "base": "AttrPaxgMMarketSignal4h",
    "normalized_identical": true
  },
  {
    "name": "PortCompareSpyRetest4h",
    "base": "AttrSpyCqFreshLimit",
    "normalized_identical": true
  },
  {
    "name": "PortCompareSpySecond4h",
    "base": "SpyLastMechanism01",
    "normalized_identical": true
  },
  {
    "name": "PortCompareSpyMarket4h",
    "base": "SpyLastMechanism05",
    "normalized_identical": true
  }
]
```

## Diagnóstico añadido a todas por igual

Una llamada inmediatamente antes del floor de qty de cada plan long/short, sin usar sus resultados para decisiones. Registro de long usa margin_room existente; short observa la misma expresión de margen existente. terminate está soportado por el framework; se usa después del cierre final. No se cambió framework. Cuenta planes calificados al llegar a sizing, no oportunidades virtuales ocupadas.

```python

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        # One compact persisted record per route, after engine final liquidation.
        # jh.debug logs even with strategy debug_mode disabled; no decision is changed.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

```
