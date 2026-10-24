# Proposal only: BTC long failure to progress — 2026-10-18

Status: critical predeclared design, awaiting root review. No source or draft created; no new backtest or analysis job. Reference and2026 untouched.

## Mechanism and comparison

[Reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). One independent full clone, provisionally AngleCombinedBtcNoProgress4h, would keep all original entries, long priority, sizing, reservations, BTC shorts, PAXG/SPY and existing trailing/fees unchanged. Add only a BTC-long state-dependent time invalidation.

Premise: a purchased breakout retest is expected to make directional progress. A trade that cannot deliver even one original risk-unit at a completed4h close over the first day may be a stagnant failed continuation rather than a trend worth retaining. Cutting it might reduce weak/choppy-period losses without adding a new entry generator or choosing weak calendar months retrospectively.

This is management, not independent alpha or new information. It can remove profitable slow trends, force unnecessary market exits and create earlier re-entry/cash-allocation opportunities. A higher positive-month ratio alone can be a denominator or cash-exposure effect; evaluate actual full calendar and account economics.

## Single fixed recipe

For BTC longs ONLY:
1. At actual fill, retain fill timestamp, entry and initial stop distance R from the existing plan. Initialize best_post_entry_closed4h_close=entry. Existing protective stop remains active.
2. At every ordinary4h management callback while open, update this best using only that now-completed4h closing price after the fill. Never inherit a high/close from before entry; do not use forming bars or hindsight over the eventual trade.
3. At the first4h callback with age>=24hours from actual fill, make ONE decision. Because fills can occur intrabar, actual review is24–28h after fill, not exactly24h.
4. If best_post_entry_closed4h_close < entry+R, close entire BTC long at current MARKET. If it reached entry+R, retain the original long-management policy for the rest of this trade, without further age checks. Equality passes.
5. A prior protective stop still wins through ordinary intrabar execution. No partials, pyramiding, extra orders, breakeven change, re-entry prohibition or new cooldown.

One calendar day and one initial risk unit are understandable fixed dimensions chosen before inspecting affected trades. They are not calibrated optimums. No sweep of12/24/48hours or0.5/1/2R follows a negative result.

## Difference and duplicate audit

Read MCP inventory ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md, central ORCHESTRATION_RESEARCH_LEDGER_20261018.md, and PHASE2_PROGRESS_20261018.md. Global selection is much larger than18economic runs; no clean new statistical sample is claimed. Not every legacy source was read, so absence means not found in these documented mechanisms, not an exhaustive proof.

- Existing24/48/72h controls time-limit BTC SHORTS irrespective of achieved progress. This rule is BTC LONGS only and conditional on failure to reach a closed-bar1R milestone.
- Fixed3R/5R and partial2R+runner take profits; this does not cap winners after progress.
- Monthly giveback guards use account/calendar state; this uses per-trade elapsed time and post-entry evidence, with no month labels.
- Existing short invalidation by recovering signal high uses a price level; this challenges a long trade for absence of expected progress within a fixed horizon.
- Current volume, H-L-H shorts, M1 touch/reclaim, acceptance occupancy, probabilistic four-state and RSI-replacement event/hysteresis lines concern entry generation/admission or prediction. None documents this post-entry BTC-long failure criterion.
- It still overlaps the broad trend-following/management family. Do not present it as a new economic source.

## Causality and implementation risks for review

Use actual fill time, not setup submission time. All progress closes must be strictly subsequent to entry; initial progress state starts at actual fill. Intrabar high reaching1R but closing below does NOT qualify, intentionally: the observable is sustained close progress rather than a fleeting wick. No lower-timeframe touch reconstructed from future extrema.

The original4h management clock and initial-distance definition remain fixed. On the first age-qualified callback, set a one-shot checked flag; if exit is triggered return before placing a new trailing modification. On a passed check, continue ordinary management. On_close resets per-trade state; an old flag must not infect a later trade.

A MARKET exit frees shared capacity and can change later BTC shorts and PAXG/SPY sizes/fills. It can increase turnover indirectly despite unchanged entry rules, so lower losses cannot be attributed solely to a better long classifier. Do not compare a handpicked subset of original trades and treat it as an executable portfolio.

## One evaluation and rejection criteria

Only if root approves: one full combined clone, original three4h routes, common2020-10-15→2025-12-31exclusive, normal replay, warmup240, fee0.00045 per side for every order,5xisolated,10000start; retain3%trade/8%aggregate/4.4gross limits. Benchmark/log choices coordinated with root V4.2026 remains sealed.

Archive counts of BTC long fills, age-checks, progressed/passed, forced exits and earlier normal closures where available; do not fabricate unavailable observations. Confirm executed orders, no partials, wallet/fees reconciliation and complete terminal accounting.

Compare true V4 MTM: all63months/21quarters, active and complete periods separately, annual development returns, drawdown, net BTC-long contribution, full-account return, costs, exposure, number of new trades and concentration. No claim that2024–25 is clean OOS.

Reject immediately if data/state/fill logic fails. Reject as a solution if it fails65–70%positive active months,80%positive quarters,DD<=25% and useful net economics. A small apparent gain supported by very few forced exits, a single saved outlier, worse net expectancy/cost resilience or exposure withdrawal is insufficient to promote. No threshold neighbors until a positive, auditable economic result justifies a separately reviewed robustness protocol. Do not count merely moving realization dates as an MTM improvement.

This proposal promises no outcome; if delayed continuation is important to BTC trends it should fail, and that negative result must remain recorded.


## Root clarification before implementation

The reference BTC-long component contains only31trades, not97 (97 counts all assets' longs). Forced-exit sample will be smaller still. Do not treat this as an independently powered large-sample experiment; a few lost slow trends can dominate.

R is specifically the positive price distance from the actual fill entry to the original initial protective stop, frozen at fill. It excludes fee/sizing reserves as a milestone definition; those costs remain real in portfolio accounting. Progress observations must have closed4h timestamp STRICTLY greater than actual fill timestamp. A milestone already reached is irreversible for this trade even if price later falls back below1R. First qualifying age review is the only time invalidation check.

No code/run is currently authorized; parent finishes the distinct event-short trial and accounting audit before deciding.
