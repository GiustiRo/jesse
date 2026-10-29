# Proposal: SPY persistent participation with inherited protection — 2026-10-18

Status: one design for parent review; no source, draft, backtest, external source, research script or analysis job created. Prospective strategy name PortfolioSpyPersistent4h. Reference remains [MultiAssetRetestBtcShort4h](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb);2026 sealed.

## Proposed role and economic uncertainty

Test whether sustained participation in the observed index price path, with existing protective management and a fixed post-exit pause, is a better SPY role than rare filtered breakout retests. SPY currently earns most of its net from one trade; this is a reason to examine participation/concentration, not evidence that unconditional long exposure is superior.

This is an economic control for entry selectivity, not new independent alpha or an anticorrelated crisis sleeve. Equity-index long participation may add risk in the same periods as BTC, especially broad selloffs. It cannot be presumed to rescue the portfolio's weak months. The available source is a price-only SPX CFD BID proxy divided by10, not native SPY ETF total return. Dividends, ETF tracking, funding, spreads and executable target-venue parity are not established here. The test can only assess the available proxy under explicit simulation limits.

## One precise recipe

Clone the complete reference independently; keep BTC long/short and PAXG unchanged and only replace SPY entry policy:
- While SPY is flat, enter MARKET at the first current, source-fresh eligible4hclose if at least7*24hours have elapsed since its last real full closure. At startup there is no artificial prior closure/cooldown.
- No breakout, EMA alignment, ADX, RSI, dip or calendar-month forecast gates for SPY. Finite/positive price, sufficient inherited ATR/share history, entry-hours and current quote validity remain data/safety prerequisites.
- On every real SPY full close, including a profitable trailing-stop close, begin the same fixed168h pause. Store closed_trade.closed_at from the documented closure hook rather than rounding to a4hboundary. No early restart based on observed subsequent price.
- No monthly rebalance, forced month-end exit or rotation. No weekday/month selection. The week-long delay is a transparent ex-ante churn buffer of one full weekly cycle, not a claimed optimum. After delay expires, unavailable data/session means waiting to the next eligible real quote.
- At entry keep the reference's actual initial stop distance stop_atr*ATR (default2ATR), computed on the same filtered SPY history and frozen from the real fill.
- Keep the exact inherited long trailing4.2ATR/default, late-trend tightening and BE rules unchanged. No profit target, partials, pyramiding or new exit criterion.

One active SPY route, never an additive second sleeve. The cooldown is necessary to make the persistent-participation policy a coherent low-churn test; it is not optimized over alternative durations if the result is negative.

## Exposure control and attribution

Retain the SAME maximum3%trade-risk budget as reference for policy comparison,8%aggregate planned risk,5xisolated,4.4gross admission, inverse-ATR share cap and90%available leveraged margin cap. Keep existing sizing reserve10bps and modeled fee0.00045 per side for EVERY order. Risk is not increased. Do not substitute1%risk/3%price-stop (~0.3xnotional) and attribute the resulting exposure reduction to a superior mechanism.

The MARKET entry price replaces the old LIMIT channel boundary, so quantity and exact cash risk must be recomputed using the existing sizing formula and CURRENT proposed entry. The ATR risk unit, budgets and caps remain fixed. Admission/reservation must occur before queuing the order and release only through normal fill/cancel lifecycle.

Same admission rules do not mean matched realized exposure: number of opportunities, holding periods, entry prices, ATR at entry and capital trajectory change. Report net and gross contributions, fees, time-in-market, realized exposure and concentration. A lower drawdown caused solely by lower exposure is not new alpha. Shared cash can alter BTC/PAXG sizes and later fills even with unchanged source rules. Do not sum independent sleeve curves or infer additive improvements.

## Hours, source gaps and causality

Re-read jesse://strategy, especially Trading Hours:
- SPY signal history remains filtered by inherited UTC Mon-Fri00:00–20:00.
- New entries retain the inherited closed-candle-open-time00:00–16:00 eligibility; this is a provider-compatible common window, not NYSE RTH or a new seasonal edge.
- A first implementation should verify current M1 quote freshness and agreement with4hclose rather than fill a MARKET from a stale post-gap aggregate. All M1 timestamps must be already closed; missing data means waiting, not fabricating a quote.
- Never gate protective exits by hours. They execute only on available source quotes; holds may span overnight/weekend and gaps can exceed intended stop loss.
- ATR/share inputs preserve the same filtered-clock conventions; do not reinterpret filtered bars as equal calendar time or invent missing holiday/session bars.

Persistent exposure will make this source/financing limitation more economically relevant than a sparse breakout policy. Positive proxy results would still need execution/cost validation; no live-readiness claim.

## Duplicate review

Read global mechanism inventory, MultiAssetSleeves4h source and SPY calendar rejection report:
- Sleeves SPY uses rising EMA120/RSI3<=20 oversold LIMIT entry, fixed EMA20target and5dexpiry. This policy has no oversold/macro gate or mean-reversion exit.
- Failed4/4calendar-turn policy only holds a narrow fixed part of each month and closes by month-day rule. This policy has no month clock or monthly liquidation/re-entry.
- Monthly cross-asset momentum rotation chooses a positive winner; this fixes the SPY role and does not select another asset.
- Existing breakout/retest, trend-both and Turtle approaches predict directional eligibility from price structure. This intentionally removes that forecast for SPY while retaining the existing protection.
- It still belongs to directional long participation with protective stops; do not market it as an unseen data source or new theory. It may simply be inferior to cash or a passive index-price path.

Source benchmark SPY buy-and-hold, if already present in stored sessions, can contextualize proxy price participation only. Do not create another independent executable portfolio or a leverage-equivalent fund by rescaling that benchmark. No external data request follows this proposal.

## First evaluation only if parent approves

One full combined clone over2020-10-15→2025-12-31exclusive, normal mode, warmup240 and benchmarks/logging coordinated with root. No implementation or run yet. Parent decides whether the economic-control value justifies this single test.

Audit entry cooldown>=168h since actual previous closure; initial-entry exception; hours/fresh quote; actual MARKET execution; shared reservation/risk/fees/full-position exits; terminal accounting and wallet reconciliation. Include blocked-cooldown/data/budget counts where recorded, not fabricated.

Economic first filter: SPY net expectancy after fees and contribution to the full portfolio, exposure/turnover, concentration top1/3/5 versus net and gross winning sum, and annual development stability. Then true V4 MTM calendar: all63months/21quarters, active/completed denominators, BTC/PAXG/SPY directional components, and negative-month sign/magnitude interactions. Final objective remains65–70%active-month positive,80%quarters,DD<=25% with useful net economics; SPY alone need not independently achieve every portfolio target.

Reject this recipe if economically negative, excessive churn/cost, catastrophic adverse complementarity, or no material portfolio regularity benefit after accounting for exposure and shared cash. A few lucky long trends or better winrate is insufficient. Do not alter pause, ATR/trailing parameters, seasonality or risk after the result. If promising, parent must predeclare subsequent stress/robustness before further tests.2020–2025 is extensively adaptive development, not OOS;2026 remains untouched.
