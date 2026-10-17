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
| [`.claude/skills/jesse-strategy-tests/SKILL.md`](.claude/skills/jesse-strategy-tests/SKILL.md) | Cómo escribir tests de estrategias y del motor. |

## Dónde trabajar

- Investigación, backtests y Monte Carlo: PC local, <http://localhost:9200>, MCP `jesse-local`.
- Live y administración de la Pi: <http://192.168.1.10:9100>, MCP `jesse-pi`, solo si la tarea lo pide.
- No copiar `.env`, volúmenes ni la base completa entre ambas. La réplica local no tiene claves y no opera.

## Decisiones vigentes

- Solo `BTC-USDT` perpetual. Una sesión por cuenta: Binance one-way netea el símbolo.
- Objetivo vivo: 5x isolated, sin piramidar. El live de la Pi puede seguir en 2x; cambiarlo a 5x antes de operar (en Binance ya está en 5x Aislado)
- Riesgo elegido: 2% por trade. Meta aceptada: 20–30% anual (Negociable).
- Fee de backtest: `0.00045` (taker VIP0 con BNB). Funding fuera para no complejizar.
- Prioridad: rentabilidad, no frecuencia.
- Timeframes: A explorar/definir.
- Candidata: A explorar/definir.
- Descartadas: ``TrendBreakout5m``, `SqueezeRelease5m`, `RangeFade5m`, `TrendPullback5m`.
- Calibrar solo con 2020–2025. 2026 está reservado. Criterios OOS fijados: PF ≥ 1.2, drawdown no peor que −25% y unos 20 trades.
- No ejecutar `jesse install-live` ni definir `LICENSE_API_TOKEN`. Estamos en un repo opensource 100% customizable!
- No commitear `.env`, `bot/docs/raspberry-pi.md` ni claves, y no imprimirlas.
