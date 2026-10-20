# Monthly three-month momentum rotation — completed, not approved

[Finished experiment](http://localhost:9200/#/backtest/56937ae5-e005-4d70-931d-c9d1e5215b42).
One predeclared recipe; 2020-10-15 to 2025-12-31 exclusive, normal engine, three 4h routes plus 1m freshness data routes, warmup 240, 10,000 USDT, isolated 5x, fee 0.00045 per side. No 2026, alternative stop, momentum lookback grid or rescue threshold.

## Result and actual exposure

28 closed longs: 16 BTC, seven PAXG and five SPY. Closed net **+2,235.727115 USDT**, fees **80.049136**; displayed CAGR **3.945958%**, engine drawdown **-22.895877%**, Sharpe **0.412308**. Average holding period about 46.8 days.

Entry notional divided by the flat starting wallet of each trade ranges from **0.289325x to 0.294536x**. The 1x admission ceiling does not mean a 1x portfolio. The broad 10% stop is sized to the approved 3% planned risk ceiling including costs. No overlapping closed positions were found.

First verified actual fill: **2021-02-03 16:00 UTC**. Every stored entry is labeled 16:00 UTC. Initial October 2020 through January 2021 calendar bins therefore remain cash, including the partial first bin. Do not remove them to improve regularity. first_eligible_rank exists in shared state but is not exported in the standard snapshot; do not invent its exact timestamp from the first fill.

All runtime guards completed: selection uses strictly old common observations, entry and actual fill follow ranking, old exposure must be flat, and each fresh M1 timestamp must agree numerically with the own decision price. Only actual, verified common 16:00 observations accumulated; no 4h bootstrap was assumed fresh.

## Terminal-counter interpretation and reconciliation

Metrics report total_open_trades=1 and open_pl=422.55635. **These describe the pre-termination position, not proof of an unclosed final residual.** Coordinator framework inspection identified that the counter is incremented before terminal liquidation.

The final stored trade is PAXG, quantity 0.895, entry 3,888.41, executed full MARKET exit 4,360.54 at 2025-12-31 00:00 UTC. Gross PnL is exactly 422.55635; net PnL 419.234085 after 3.322265 commissions. Thus the displayed open_pl matches that position's gross value before its verified close.

All 28 closed PnLs sum to 2,235.727115173373. Starting 10,000 plus that sum equals the displayed finishing balance 12,235.727115173384 within floating tolerance; closed commissions equal the displayed fee. No counter was edited and no stale SPY terminal fill was forced. The coordinator's terminal-aware V4 audit accepted this specific case after matching the pre-termination count and gross PnL to the executed full terminal PAXG close, and independently reconciling fills, fees and actual wallet. No original metric was changed and no rerun hid the flag. A synthetic terminal close does not prove tradability of other assets.

## Components and temporal evidence

Closed-trade net contribution, not isolated-account returns:
- BTC: +1,554.63 USDT, 16 trades, PF 1.620.
- PAXG: +793.93, seven trades, PF 3.703.
- SPY: -112.84, five trades, PF 0.769.

Annual CLOSED PnL, not year-end MTM returns:
2021 +824.73; 2022 -531.09; 2023 -943.49; 2024 +1,909.30; 2025 +976.27 USDT. Early/late calendar bins remain partial where applicable. Small component samples and weak closed-PnL years limit confidence.

The top two winners account for 44.33% of gross positive closed PnL. That is a concentration warning, not automatic proof of overfit for a slow trend strategy.

## Costs and decision

Holding fills and quantities fixed, an extra 10 bps per complete round trip leaves closed net +2,146.78 USDT; 25 bps leaves +2,013.37. These are arithmetic cost diagnostics, not rerun CAGR/DD. Lower turnover improves commission headroom, but funding and native instrument parity remain unvalidated.

Complete-snapshot analysis **b3c7c2ddf0844171880da1ca30d60d1b** succeeded. Stored terminal orders were also read through MCP.

Not approved. Positive closed net and cost headroom are insufficient against a 22.9% drawdown, low return, modest sample and inconsistent temporal contribution. This long-only screen does not satisfy useful short participation. The final coordinator calendar assessment below confirms rejection; do not infer monthly consistency from trade closure dates. No parameter or risk increase is proposed to rescue this recipe. Reference remains unchanged.

## Final terminal-aware V4 calendar audit

The coordinator's bounded audit passes execution/fees/actual-wallet reconciliation and distinguishes the pre-termination counter from a true residual position. The PAXG synthetic terminal close remains explicitly labeled.

| Calendar measure | All bins, including partial edges | Complete bins only |
|---|---:|---:|
| Positive active months | 31 / 55 = **56.3636%** | 30 / 54 = **55.5556%** |
| Positive months over all calendar months | 31 / 63 = **49.2063%** | 30 / 61 = **49.1803%** |
| Positive quarters | 10 / 21 = **47.6190%** | 9 / 19 = **47.3684%** |

Worst month **-3.8617%**; worst quarter **-7.9199%**; drawdown on daily closing equity **-22.85525%**.

Yearly MTM returns, distinct from the closed-trade amounts above: 2020 partial **0%**, 2021 **+8.2473%**, 2022 **-4.2258%**, 2023 **-4.0664%**, 2024 **+12.4203%**, 2025 partial **+9.4331%**.

**Final decision: reject this recipe.** Both active-month and quarter objectives fail, and including cash reveals positive returns in fewer than half of calendar months. No momentum lookback, stop or risk adjustment follows these observations. First-fill/startup differences from the reference remain visible; this was a lower-exposure long-only component screen, not a claim to satisfy the final long/short portfolio.
