# BTC intrabar acceptance: predeclared protocol — 2026-10-18

## Scope and immutable comparison

A full independent clone, AngleCombinedBtcAcceptance4h, of MultiAssetRetestBtcShort4h. Reference session: [baseline](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Reference source is unchanged. No other agents' source is incorporated. All BTC long, PAXG and SPY rules and risk reservations remain identical; the sole economic change is an extra admission gate for existing BTC short candidates. This is a continuation refinement, not a distinct independent edge or new external information.

## Economic hypothesis and fixed rule

A depressed price accepted for much of a completed selloff bar may be less likely to recover immediately than a brief late plunge. Four-hour OHLC and RSI do not identify how long minute closes occupied a price region. They can be identical for paths with different occupancy. Occupancy nevertheless overlaps strongly with continuation and does not identify order flow, liquidations, or an economic cause by itself.

First require every existing short structural and distance rule unchanged, including RSI3<=20. Then, using ONLY the most recent completed 4h candle and its 240 completed M1 candles:
- define lower-third boundary = low4h + (high4h-low4h)/3;
- count M1 closes <= that boundary;
- admit the existing short order only if count>=120 out of240.

Third and half are natural geometric/time partitions fixed before any outcome comparison. They are not parameters to optimize. No grid or alternative threshold follows a negative result. Zero range rejects. Long priority, entry STOP price, 1.5ATR profit target, EMA-based short stop, 72h expiry, long trailing exits, risk, fees, and reservations are inherited unchanged.

## Causality and validity

At callback time t require M1 timestamps exactly candle_open + arange(240)*60000, and candle_open+4h=t, with all timestamps<t. Finite positive OHLC is mandatory; no gap fill. Verify aggregate M1 last close, maximum high and minimum low against current closed4h candle. np.allclose rtol1e-10/atol1e-8 is solely a floating representation tolerance. The final extrema are observed at decision time; no claim that their levels were available earlier inside that same bar.

Coverage/parity invalidity rejects that candidate and increments diagnostics. If any baseline structural candidate exists but NONE has valid coverage and aggregate parity, termination raises ACCEPTANCE_NO_VALID_M1_WINDOWS: no technical failure may masquerade as a useful zero-trade gate.

Annual and final cumulative diagnostics through jesse.helpers.debug: baseline_structure_candidates, valid/invalid_m1_coverage, valid/invalid_4h_parity, zero_range, gate_accepted/rejected, short_positions_filled. Sparse absent counters mean zero, not unavailable. Annual counters reset at year transition; final totals are cumulative. Filled positions can occur after a candidate/year boundary and are distinct from accepted signals. Candidates count structural/distance eligibility before portfolio budget/quantity; accepted signals are not guaranteed fills. Logs require debug=True in the reviewed draft. No data/strategy output files are written by the strategy.

## One evaluation, no tuning

Parent review required before run. Single common-window run: Binance Perpetual Futures, BTC-USDT/PAXG-USDT/SPY-USDT4h all with this clone; 2020-10-15 inclusive to2025-12-31 exclusive; normal mode; warmup240; benchmarkTrue; debugTrue; initialcash10000; fee0.00045 per side for every order type;5xisolated. Existing3%trade/8%aggregate/4.4gross admission limits retained, never raised for return targets. Existing10bps sizing reserve is not simulated execution slippage. No exact STOP parity or live execution claim.

Inspect diagnostics first. If valid, compare actual net returns, effective costs, number of short fills, exposure, drawdown and full MTM calendar regularity to immutable reference. Root V4 auditor handles terminal positions and real fees. Compare annual development results without calling2024–25 clean OOS; all2020–25 is development.2026 remains untouched. Do not select assets or years after observing winners, and do not rank solely by winrate. Lower trade count without meaningful net expectancy/portfolio regularity improvement is not success. A promising overall result still needs subsequent robustness/cost controls; this one trial cannot establish robustness.

No unconditional probability control, new data, scripts, framework changes, live/paper or further variants are authorized by this protocol.
