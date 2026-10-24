# Orchestrated short research round 1 — predeclared protocol
Date: 2026-10-18. Exploratory development only, 2026 sealed.
Reference frozen: [BTC/PAXG/SPY longs + BTC shorts](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
All long entry/exit methods, inverse-ATR per-asset capacity and shared risk unchanged. Signal fee fixed .00045 for eligibility/breakeven, actual fees retained for sizing. Both variants use all three 4h routes, 2020-10-15 to 2025-12-31 exclusive, normal simulation. No partial exits/pyramiding. Planned trade risk <=3%, aggregate <=8%, 4.4x admission notional, 5x isolated. Gaps can exceed stop risk.

## Hypothesis A: economically balanced continuation (OrchShortRewardRisk4h)
Original short target remains 1.5ATR and initial stop remains EMA20-entry, 1–3ATR. Require planned target less entry/exit commission >= planned stop distance plus stop commissions (1R net hurdle). Hurdle uses fixed SIGNAL_FEE so cost stress cannot silently change eligibility. No parameter search: threshold 1 follows equal net reward/loss, not empirical tuning.
Potential benefit: removes adverse asymmetry requiring high precision. Failure risk: discards profitable wide-stop continuations; fewer active months; close stop subset may be noisier. Does not manufacture entry fills or promise gap execution at plan price.

## Hypothesis B: falsifiable price invalidation (OrchShortReclaimExit4h)
Keep original short entry/stop/target/72h cap. Record the original signal candle high at planning. After actual fill, a future closed 4h bar above that high liquidates the full short at observed close. Hard protective stop remains active throughout. No final-trade-duration or future MFE filters.
Potential benefit: cuts failed breakdowns using observable price reversal rather than an arbitrary faster timer (24/48h already failed). Failure risk: temporary reclaim precedes subsequent profitable fall, added churn/cost.

## Predeclared decisions
First compare short net PnL/PF, trade count, full portfolio CAGR/DD and true-calendar MTM monthly/quarterly signs against the frozen reference. Primary research goal stays 65–70% active positive months, 80% quarters, DD no worse than -25%, economically useful return. A one-bin gain with meaningful return/DD deterioration is not promotion. Both variants may be rejected. Do not select solely on winrate.
If a variant is promising, require chronological subperiod consistency, nearby economically justified settings and fixed-signal higher-cost checks before combination/promotion. No claim of clean OOS on 2020–2025; all development has been observed. No parameter sweep, no MC-independent portfolio certificate. Root controls MTM auditor and compute slots.