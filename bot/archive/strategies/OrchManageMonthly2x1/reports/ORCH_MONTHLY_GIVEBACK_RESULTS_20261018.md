# Monthly giveback guard — paired result: reject

The two proportional neighbors were declared before execution; no thresholds changed after observing results. All runs use 2020-10-15 to 2025-12-31 exclusive, three 4h assets, normal simulation, 10,000 USDT, isolated 5x, and 0.045% fees per side. Original alpha, 3%/8% planned risk limits, and inverse-ATR allocation remain unchanged. **2026 stays sealed.**

| Case | CAGR | Engine DD | Sharpe | Longs / shorts | Net USDT |
|---|---:|---:|---:|---:|---:|
| [Reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) | 28.8294% | -14.8905% | 1.31643 | 97 / 123 | 27,461.46 |
| [Arm 2%, floor 1%](http://localhost:9200/#/backtest/ace2ad08-48bf-4326-9602-3a8e71b2fb18) | 7.6727% | -12.5829% | 0.64155 | 61 / 67 | 4,702.43 |
| [Arm 4%, floor 2%](http://localhost:9200/#/backtest/5437d456-3483-42a8-b354-c287451875f4) | 2.8895% | -14.1106% | 0.28509 | 71 / 82 | 1,601.12 |

All sessions finished with no open positions.

## Components

- 2%/1%: longs net +2,497.99 USDT, PF 1.385; shorts +2,204.44, PF 1.538.
- 4%/2%: longs net +1,080.70, PF 1.154; shorts +520.42, PF 1.098.
- Reference: longs +22,174.44, PF 1.999; shorts +5,287.02, PF 1.360.

Unchanged alpha does not imply identical fills or quantities: the guard changes actual exits, entry permissions, and subsequent capital.

## Execution and calendar limitations

Shared state records UTC month, baseline, armed/locked flags, and pending exit requests. Only before() resets calendar state. Requests survive rollover and block every new entry until all requested routes are actually flat without pending entries. on_open_position() honors old requests after rollover.

Each position closes from its own quote callback. BTC never invokes a stale SPY liquidation. Existing pending orders can fill before their next cancellation callback; they retain protection and join the deferred exit queue. Four-hour monitoring, gaps, and SPY closures make the floor approximate rather than guaranteed.

Estimated liquidation equity deducts only future closing fees plus a 0.0005 closing-impact reserve. Entry fees are not deducted twice. The reserve is an estimate, not applied slippage.

Stored orders show 29 / 30 long MARKET exits before the final observed UTC date versus one in the reference, and seven / seven short MARKET exits before 72 hours versus zero. Therefore management changed execution, rather than merely relabeling monthly realization. The reference also has one long MARKET exit: do not uniquely attribute every MARKET exit to the guard. These counts do not measure causal savings against hypothetical unchanged positions.

Complete-snapshot analyses succeeded:
- 60380e940c2840b49f0ada410bd2face: initial 2%/1% components.
- 607aefc078674d78a2213e9243877c5a: paired components.
- af84b429625646c489039e0542e29e48: exit classification, excluding 2025-12-30 explicitly.

## Decision

Reject both guards economically. CAGR falls to 7.67% / 2.89% with modest drawdown improvement. This is consistent with truncating beneficial trends and blocking reentries; the precise causal share of each mechanism has not been isolated.

Do not promote even if monthly signs improve. The final coordinator V4 calendar figures are recorded below. No months are removed or relabeled; original consistency targets remain. No additional floors, thresholds, or grids will be explored to rescue this pair. The reference remains unchanged.

## Final calendar MTM audit — coordinator V4

The coordinator's V4 audit confirms **31 / 60 active months positive (51.667%)**, **31 / 63 total months positive (49.206%)**, and **12 / 21 quarters positive (57.143%)** for the 2%/1% guard. No months were removed from the full-calendar denominator. These fail both consistency targets and are below the frozen reference's previously recorded consistency. Together with the CAGR collapse, this reinforces rejection. The 4%/2% calendar audit is recorded separately in its own report; do not apply these figures to that neighbor.
