# One filled short per RSI episode — first controlled result

[Finished experiment](http://localhost:9200/#/backtest/74b84b33-2030-4b9c-ba19-03a18ef68420), [frozen reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Normal full development window, 2020-10-15 to2025-12-31 exclusive, three 4h routes, shared 10,000 USDT, isolated 5x, fee 0.00045 per side, original 3%/8% planned risk and allocation. **2026 remains sealed.**

## Isolated change and selection history

Starting source Phase2FixedFeeRules4h reproduces the reference at base fees. Added only a closed-RSI3 episode latch: reset above 20 in before() even with an open position, consumed only by an actual short fill, gating only short planning. Cancelling an unfilled order never consumes it. Source normalization verified all other economic code unchanged. The runtime duplicate-fill assertion completed without error.

This was an adaptive development choice made after viewing existing results, not independent validation. It was not justified by final holding-time averages. The earlier 24/48-hour expiry variants already existed and were not rerun.

## Whole-account outcome

| Measure | Reference | One fill per episode |
|---|---:|---:|
| CAGR | 28.8294% | 29.3552% |
| Engine drawdown | -14.8905% | -14.9034% |
| Sharpe | 1.31643 | 1.33806 |
| Closed net USDT | 27,461.46 | 28,265.46 |
| Long / short count | 97 / 123 | 97 / 119 |

Experiment pre-termination open counter is zero. Total fees 4,694.91 USDT. The drawdown does not improve. The small return improvement is not a claim that the portfolio meets the consistency objective.

## Attribution and cohort comparison

Short net +5,343.75 versus +5,287.02 in the reference: only **+56.73 USDT**. Short PF 1.3712 versus 1.3602.
Long net +22,921.71 versus +22,174.44: **+747.27 USDT**, despite unchanged long rules and 97 long entries, reflecting the shared capital and sizing path.

Of the observed trades, 215 match by symbol, direction and entry timestamp and retain exactly the same entry/exit prices and exit timestamps. Five original shorts disappear and one new short appears. Of the five missing original trades, three were losers and two winners. Do not describe all excluded continuations as bad, or interpret their historical dollar PnLs as an exact causal decomposition when subsequent quantities changed.

Annual CLOSED short PnL, not annual MTM returns:
2020 partial -56.94; 2021 -516.84; 2022 +2,324.80; 2023 +1,840.48; 2024 +622.34; 2025 partial +1,129.91 USDT.
In particular, the 2024–2025 short contribution is smaller than in the reference. Whole-sample account improvement does not demonstrate stable short improvement across periods.

## Cost diagnostic

With fixed fills and quantities, an extra 10 bps per complete round trip leaves account net +23,048.89 and short net +3,698.49 USDT. At 25 bps, account +15,224.03 and shorts +1,230.61. These are arithmetic diagnostics, not full cost reruns or stressed CAGR/DD. Effective-fee reruns would retain the fixed signal-fee rules and the same episode definition.

Complete-snapshot comparison **8a8c51e8e22b455c8baa65f644d94a21** succeeded.

## Status

Coordinator V4 calendar MTM has completed and is recorded below. No new cooldown, RSI level, maximum-hold grid or parameter rescue. Reference stays frozen. A small improvement concentrated in a few omitted entries is insufficient to declare a robust advantage or completion of phase2.

## Final coordinator V4 audit — no promotion

Fills, fees and actual wallet reconcile. Calendar counts are **exactly the same as the frozen reference**:

| Measure | All bins, including partial edges | Complete bins only |
|---|---:|---:|
| Positive active months | 33 / 61 = **54.0984%** | 33 / 59 = **55.9322%** |
| Positive months over all calendar months | 33 / 63 = **52.3810%** | 33 / 61 = **54.0984%** |
| Positive quarters | 15 / 21 = **71.4286%** | 14 / 19 = **73.6842%** |

Worst month **-7.0180%**; daily-closing equity drawdown **-14.8913%**.

The marginal CAGR increase therefore does not solve the consistency objective. Most incremental account profit comes from the changed capital path of unchanged longs (+747.27 USDT), not a substantial improvement in short alpha (+56.73). The reference is not replaced. No additional cooldowns, RSI thresholds or effective-cost reruns are justified by this screen. Preserve this result as a bounded management control, not a new validated candidate. No repeat analysis was launched.
