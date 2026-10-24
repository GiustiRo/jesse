# Quiet realized volatility to channel trend — single predeclared screen

Coordinator approved this bounded simplification after reviewing SqueezeRelease5m and failed-range results. It is explicitly from the already explored compression/expansion family, not a new independent edge. No sweep or parameter rescue. 2026 stays sealed.

## Hypothesis and exact causal definitions

Three unusually quiet days relative to the preceding month can precede an asymmetric downside range expansion. The entry is a future confirmation order, not a sell after retrospectively crossing a channel.

At every completed BTC hourly bar, exclude that latest signal bar for volatility. Take exactly 721 preceding hourly closes to obtain 720 log returns. Population standard deviation of their last 72 returns must be <=0.75 times population standard deviation of all 720. No annualization is needed for the ratio. No BB/Keltner, RSI, ADX, macro trend, session or volume stack.

The future SELL STOP is the lowest low of the latest 72 completed hourly bars INCLUDING the latest signal bar. Current observed close must be strictly above that level and no more than one ATR14 above it. Cancel unfilled entry after one future hour. No retrospective fills.

Initial stop is two signal-bar ATR14 above the ACTUAL fill, preserving planned distance through gaps. No target, breakeven, or arbitrary time exit. Each completed hourly callback may tighten the stop to the rolling 24-hour high, only if strictly below the old stop and strictly above actual current price. No stop can be raised. All orders remain future orders.

Standalone risk is 1% of min(wallet, equity), with aggregate planned 8%, gross admission cap 4.4x, 90% available leveraged margin, isolated 5x. Actual entry and stop commissions plus 10 bps sizing reserve enter sizing. Reserve is not applied slippage. Full entry/exit only.

## Configuration and memory

One BTC 1h route, no auxiliary timeframe route solely to inflate memory. Development 2020-10-15 to2025-12-31 exclusive, normal simulation, 10,000 USDT, 0.00045 fee per side. Only this draft receives warm_up_candles=800; no global configuration mutation.
Need 722 retained hourly candles. before() asserts this on every callback, so an unsupported warmup/buffer limit becomes a technical error rather than an invalid zero-trade verdict. No availability preflight, imports, installs or framework changes.

## Falsification and next steps

Reject if net <=0 or PF<=1, or if the sample is below 30 trades for useful inference. Inspect weak-year contribution, annual closed-PnL, true-calendar MTM, and fixed-fill +10 bps round-trip cost sensitivity. Strong profit concentration is a warning, not automatically proof of overfit for a trend sleeve; report the top-two share explicitly.
Do not combine a cost-fragile or negligible edge merely for correlation. A promising screen still needs chronological stability, nearby broad parameters and actual fixed-signal cost reruns before portfolio attribution. No win-rate requirement and no 2026.
Source must pass coordinator review before a single full normal run; coordinator reserves slot 2.
