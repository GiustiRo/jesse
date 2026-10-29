# Historial de investigación hasta r48 (resumen)

Resumen de todo lo ejecutado antes de r49, para el control de repetición. El detalle completo (protocolos, manifiestos, auditorías, revisiones r1–r48 del Hub) está en:

- `bot/strategies/FundingOiPilot4h/reports/` y `RESEARCH_HUB/revisions/` (se conservan en su lugar porque el panel del Hub lee esas rutas).
- `bot/archive/strategies/`: código y reportes de todas las estrategias de rondas cerradas.
- Tag git `research-archive-r48` (commit `c3b55495`): estado íntegro anterior a la limpieza, incluidos los volcados crudos de logs, records, funding y artefactos de análisis (`*_PART_NN_*.json`, ~115 MB) que se retiraron del árbol. Se recuperan con `git checkout research-archive-r48 -- <ruta>`.

Ninguna de estas cifras es una muestra independiente: todas comparten datos 2020–2025, señales y variantes. Sumando todo hay unos 650 backtests económicos.

## Línea de tiempo

| Etapa | Qué se probó | Mejor resultado | Veredicto |
|---|---|---|---|
| regime-trade (repo padre) | HMM 3 estados + LightGBM triple barrier con funding/OI, 4h | Lockbox Sharpe ~4; mes demo PF 1,10 vs 1,63 esperado | Sobreajuste. Descartado |
| Fase 1 Jesse | `BtcMomentumCore4h`: Donchian 26 4h + EMA 20/80 + ADX, BE 2,25R / trail 3R | Riesgo 5%: CAGR 58% / DD 21,9% / Sharpe 1,32 / PF 2,97, 45 trades. Riesgo 3%: CAGR 35% / DD 12,4% / Sharpe 1,38 | Descartada por frecuencia y regularidad, no por rentabilidad. Nunca evaluada en 2026 |
| Fase 2 cartera BTC+PAXG+SPY | Retest/breakout, shorts BTC, orquestación, capital R11–R13 | K1001 C: 2020–25 CAGR ~18% / DD 8,8% / PF 1,95 (1%/8%/5x); 34% / DD 13,8% a 2%/6%/3x | 2026: B −1,3% (DD 25,9%), C +10,4% gracias a un único trade SPY. Fallo conjunto |
| PAXG / SPY individuales | Fines de semana, shocks, R20/R40/R60, estructuras BR/PB, MECH | PAXG market entry PF 1,82; SPY MECH01 PF 4,0 con 12 trades | Piezas de cartera, no operativas por sí solas |
| Funding/OI V1–V6 | 209 backtests: precio + funding + OI, walk-forward | V3 CHANNEL_P CAGR 17,5% / DD 18,4%, 95 trades, todo en 2024 | Sin candidata. Funding/OI sin ventaja direccional |
| Descubrimiento BTC r10–r48 | 70 backtests: CUSUM, Kalman, saltos, AR/VAR, mechas, kNN, números redondos, relojes de volumen, estacionalidad, primera ruptura, valor de continuación (1m/4h) | N-state CAGR 26,9% / DD 25% | Sin candidata. En intradía los fees superan al bruto (R44: bruto +1.727 vs fees 6.473 USDT) |

## Lecciones que siguen vigentes

1. Las puertas r9 (CAGR ≥30%, DD ≤20%, M65, Q80) sobre un solo activo exigen un Sharpe neto ≈2. Por eso en r49 la regularidad se exige a la cartera y a cada manga se le exige ventaja ajustada por pruebas múltiples.
2. Los micro-patrones de un solo gráfico no sobreviven al fee taker de 0,045% por lado. No volver a señales de menos de 1h sin ejecución maker modelada.
3. Funding y OI no funcionan como señal de entrada. Solo se usan como freno de riesgo.
4. HMM y ML de árboles sobre 4h de un activo sobreajustan. ML solo como meta-labeling sobre una señal simple validada y con varios activos.
5. 2026 ya fue mirado (K1001 y las candidatas archivadas). Es in-sample para todo lo diseñado después del 2026-10-19.
6. Los parciales tempranos (50% en 1R) destruyen la esperanza de un sistema de tendencia. La salida que sobrevivió fue BE 2,25R / trail 3R.
7. Antes de proponer algo, buscar su antecedente en `bot/archive/strategies/` y en `RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md`.
