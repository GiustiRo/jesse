# Índice para agentes

Leer este archivo antes de trabajar en el repo. El detalle vive en los documentos enlazados; aquí solo está el mapa y las decisiones vigentes.

## Documentos

| Documento | Para qué |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Convenciones del framework Jesse: tests, API, typing y publicación. |
| [`bot/AGENTS.md`](bot/AGENTS.md) | Reglas generadas por Jesse para estrategias vía MCP. |
| [`LIVE_ADAPTER.md`](LIVE_ADAPTER.md) | Adapter live open source; no instalar el plugin comercial. |
| [`bot/README.md`](bot/README.md) | Proyecto ejecutable, estrategias y tab ARMAS. |
| [`bot/docs/local-research.md`](bot/docs/local-research.md) | Réplica Docker local para backtests y Monte Carlo. |
| [`bot/docs/raspberry-pi.md`](bot/docs/raspberry-pi.md) | SSH, rutas y operación de la Pi. Local y gitignored; no copiar secretos al chat ni a git. |
| [`bot/docs/socks-proxy.md`](bot/docs/socks-proxy.md) | Salida SOCKS hacia Binance. |
| [`bot/docs/multi-asset-pivot-handoff.md`](bot/docs/multi-asset-pivot-handoff.md) | Instructivo de handoff Fase 2: pivote multi-activo (`BTC` + `PAXG` + `SPY`), ejecución intra-vela y auditor mensual. |
| [`.claude/skills/jesse-strategy-tests/SKILL.md`](.claude/skills/jesse-strategy-tests/SKILL.md) | Cómo escribir tests de estrategias y del motor. |
| [`jesse/mcp/resources/funding.md`](jesse/mcp/resources/funding.md) | Funding/OI: fuentes, MCP/UI, contabilidad, supuestos temporales y límites de live. |

## Dónde trabajar

- Investigación, backtests y Monte Carlo: PC local, <http://localhost:9200>, MCP `jesse-local`.
- Live y administración de la Pi: <http://192.168.1.10:9100>, MCP `jesse-pi`, solo si la tarea lo pide.
- No copiar `.env`, volúmenes ni la base completa entre ambas. La réplica local no tiene claves y no opera.

## Decisiones vigentes

- Solo `BTC-USDT` perpetual. Una sesión por cuenta: Binance one-way netea el símbolo.
- Objetivo vivo: 5x isolated, sin piramidar. El live de la Pi puede seguir en 2x; cambiarlo a 5x antes de operar (en Binance ya está en 5x Aislado)
- Riesgo elegido: 2% por trade. Meta aceptada: 20–30% anual (Negociable).
- Fee de backtest: `0.00045` (taker VIP0 con BNB). Funding desactivado por defecto para preservar los resultados previos; la integración optativa BTC Binance se desarrolla en `feature/funding-integration`, con datasets versionados y supuestos explícitos. No confundir validación de código con autorización para operar.
- Prioridad: rentabilidad, no frecuencia.
- Timeframes: A explorar/definir.
- Candidata: A explorar/definir.
- Descartadas: ``TrendBreakout5m``, `SqueezeRelease5m`, `RangeFade5m`, `TrendPullback5m`.
- Calibrar solo con 2020–2025. El 2026-10-19 el usuario autorizó abrir 2026 para evaluar K1001: capital inicial 10.000 USDT, riesgo objetivo 2% por operación / 6% agregado y isolated 3x, carteras B/C con fee nominal y estresado. Ventana 2026-01-01 inclusiva → 2026-10-19 exclusiva. Protocolo: [`K1001_OOS_2026_10K_PROTOCOL_20261019.md`](bot/strategies/MultiAssetRetestBtcShort4h/reports/K1001_OOS_2026_10K_PROTOCOL_20261019.md). Criterios OOS: neto positivo, PF ≥ 1.2, drawdown no peor que −25% y al menos 20 trades; neto positivo bajo estrés. Esta autorización no cubre live/paper. Si 2026 se usa después para ajustar reglas, pasa a desarrollo de esa nueva versión.
- No ejecutar `jesse install-live` ni definir `LICENSE_API_TOKEN`. Estamos en un repo opensource 100% customizable!
- No commitear `.env`, `bot/docs/raspberry-pi.md` ni claves, y no imprimirlas.
