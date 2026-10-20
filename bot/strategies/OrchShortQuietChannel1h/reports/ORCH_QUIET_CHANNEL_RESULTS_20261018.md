# Quiet-to-channel short — rejected single screen

[Finished BTC hourly run](http://localhost:9200/#/backtest/c4514079-275c-4586-b773-ea464d5cf1bf).
Development: 2020-10-15 to 2025-12-31 exclusive, normal engine, 800 hourly warmup, no auxiliary data routes, 10,000 USDT, isolated 5x, 0.00045 fee per side, 1% planned risk. **2026 remains sealed.**

## Frozen hypothesis

Prior 72-hour realized log-return volatility <=0.75 of prior 720-hour volatility, excluding the latest closed signal bar. Future STOP at the lowest low of the latest 72 completed hourly bars, including that signal bar; one-hour order expiry. Initial protection 2 ATR from actual fill, subsequently tightened by a 24-hour high channel. No BB/Keltner, macro stack, RSI, target, breakeven or time exit.

The protocol and coordinator source review preceded this single run. No threshold changes followed results. The concentration criterion was clarified before results as a warning rather than automatic rejection, recognizing normal trend convexity.

## Outcome

- 123 shorts; terminal flat.
- Net **-239.928772 USDT**; PF **0.967721**.
- CAGR **-0.464717%**; engine drawdown **-26.660449%**; Sharpe **-0.001736**.
- Win rate 24.39%; average winner approximately 3x average loser.
- Commissions **778.630375 USDT**. Before commissions, fixed-fill PnL was +538.701603.
- Largest winner: 17.46% of gross positive PnL; top two: 27.35%. Concentration is not the principal rejection reason.

Annual CLOSED-trade net amounts, not calendar MTM returns:
2020 partial -182.08; 2021 +92.30; 2022 +727.09; 2023 -1,399.85; 2024 -425.31; 2025 partial +947.92 USDT.

The 2022 contribution is positive, but cannot justify adding a negative, cost-fragile component by itself. No claim of hedging or calendar complementarity is supported by these amounts.

## Cost and memory checks

With the same fills and quantities, an additional 10 bps per complete round trip leaves -1,105.073633 USDT; 25 bps leaves -2,402.790925. These are arithmetic sensitivity diagnostics, not full reruns, CAGR or drawdown estimates.

The strategy's >=722 retained-candle assertion passed on every callback throughout the complete window with warmup 800. No artificial 4h data route, global settings changes, imports, installations or framework edits were required.

Complete-snapshot analysis 1fee8761163d40729bc64b651cde7ddd succeeded.

## Decision

Reject. Both net expectancy and drawdown fail the predeclared screen despite sufficient trade count. The simplified compression mechanism does not survive base costs in this sample. No ratio/channel grid or timeframe rescue. The coordinator's final V4 calendar audit is recorded below and reinforces the economic failure.

Reference remains unchanged. No further runs or analyses remain active in this line.

## Final coordinator V4 calendar audit

19 / 53 active months positive (**35.8491%**), 19 / 63 total months positive (**30.1587%**), and 8 / 21 quarters positive (**38.0952%**). Worst month **-3.9159%**; drawdown on daily closing equity **-26.7081%**. Fills and final wallet reconciled. Coordinator analysis **ecf95de9edc94cb4a8a49241ca6e4ece**; no repeat analysis was needed. Every consistency target is missed. Final status: reject.
