# Monthly positive relative momentum — final predeclared component

Coordinator approved one design: three-calendar-month momentum, broad 10% stop, maximum 3% planned trade risk and 1x gross admission cap. No tight-stop alternative, lookback grid, or threshold rescue. This is LONG ONLY; it does not satisfy the final requirement for useful shorts.

## Selection and verified causal clock

At the first weekday 16:00 UTC callback with a prior common observation belonging to the current month, rank BTC/PAXG/SPY by price change over three calendar months. Own observations are recorded only when the latest fully closed own M1 bar ends exactly at the callback time. A common observation needs all three actual prices at that 16:00 close. No historical 4h bootstrap or invented closure candle.

Only common observation CLOSE timestamps STRICTLY BEFORE the current closed_candle_open_time qualify. The ranking never sees the partly updated current timestamp. This 16:00-CLOSE clock differs from the earlier allocation control's 16:00-OPEN/20:00-CLOSE convention.

Choose the highest score only if positive; otherwise cash, earning zero. Compare with the latest common observation at or before the exact three-calendar-month date, with maximum seven-day lag. Month-end calendar subtraction clamps the day. Exact ties use alphabetical symbol order.

Maintain warmup 240 and a small shared history containing all verified observations from the run. No framework memory change; history is retained well beyond 120 days. Missing three-month history means cash for that monthly decision, without retrying intramonth. Initial cash may extend into early 2021 and remains included in all 63 calendar months and 21 quarters.

## Rotation and state

State records common observations, actual rank time, observation/anchor, scores, target, first eligible ranking, entry-used flag, and deferred exit requests. These research fields may not be exported by session snapshots. If exact ranking time cannot be recovered through MCP, report the first actual fill and conservative startup bounds, never invent it.

Hold an unchanged winner without resizing or forced monthly round trips. If its stop fires, remain cash until the next monthly ranking. Changed target requests exits from old positions or pending orders. Each route cancels or liquidates only itself at its own fresh callback.

Requests persist until every old position/order actually disappears. The new winner enters only at its own weekday 16:00 callback strictly after actual rank time and only after all old exposure and exit debt are gone. This deliberately introduces a business-day cash gap. Runtime assertions verify historical ranking timestamps, entry after ranking, actual fill after ranking, and no overlapping rotation position.

Declare legitimate 1m data routes to prove own execution freshness: last fully closed M1 open+60000==self.time. Without it, discretionary MARKET entry/exit and monthly stop review defer. Existing protective stops still execute whenever real quotes occur. No foreign-route liquidation or stale SPY execution.

## Sizing and protection

Initial stop 10% below actual fill. Size from min(wallet,equity), actual entry/stop commissions and 10 bps sizing reserve, maximum 3% planned trade risk / 8% aggregate, cap 1x gross admission and 90% available leveraged margin. Base fee 0.00045 per side; isolated 5x account.

Initial exposure is approximately 0.2945x, not 1x. Reserve is not applied slippage. Gaps can exceed planned losses. On a later monthly review of an unchanged held winner, tighten protection toward 90% of its own fresh price only when the stop rises. Never widen it or continuously rebalance size.

## Screen

Three 4h trading routes plus their 1m freshness data routes; normal simulation, 2020-10-15 to2025-12-31 exclusive, 10,000 USDT. 2026 sealed. Source and draft require coordinator review before one run.

Assess net expectancy, CAGR/DD, trade count/turnover, startup and stop cash, annual closed-PnL, costs, concentration and true-calendar MTM. Report positive months over BOTH active and all calendar bins. Do not improve apparent regularity by excluding cash. This lower-exposure component is not promised to return 20–30% standalone.

A promising screen needs chronology, cost robustness and explicit single-route BTC integration before combining with the existing short sleeve. No conflicting BTC long/short routes.

## Prior-art check

Catalog requests explicitly used 2024–2025, never 2026 performance. Rotation matched none of 40 ranked entries; momentum matched eight single-asset descriptions, with no obvious monthly rotation. This limited search does not prove novelty. Imports require an absent LICENSE_API_TOKEN; none was imported or configured. Local MultiAssetRelative4h filters the weakest 20-bar ATR-normalized trend signal, not monthly winner/cash rotation.

## Pre-run technical review

Coordinator approved causal ranking, deferred exits and monthly entry permission. Freshness now uses binary search over ordered M1 timestamps instead of copying the full retained minute array. When the timestamp is fresh, a runtime math.isclose assertion (relative tolerance 1e-10, absolute 1e-8) verifies that the decision price equals that own minute's close. These are numerical parity tolerances, not signal parameters. No economic rule changed during review.
