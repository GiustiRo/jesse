# BTC intrabar acceptance — result and limitations — 2026-10-18

[Combined acceptance run](http://localhost:9200/#/backtest/b1c63c4c-ddc9-40d9-b289-d01915073041), compared with the immutable [reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

## Verdict

Not an accepted candidate: it fails the65–70% positive active months and80% positive quarters objectives. The fixed intrabar gate reduces drawdown and produces a small, profitable short sample, but calendar regularity is insufficient and2022 deteriorates. Do not grid occupancy thresholds, increase risk, or promote21shorts on winrate alone. No further acceptance test is authorized.

## Validated operational effect

The run finishes without error and with zero open-position counter. Final logs verify327 baseline structural/distance candidates,327exact contiguousM1 windows and327matching aggregate4h close/high/low checks. The gate rejects300 and accepts27;21short positions actually fill. Acceptance is only admission before portfolio sizing and STOP execution, not a guarantee of an order/fill. There are no missing/parity-invalid candidate windows. Thus the new observable is accessible and causal under this dataset.

Logs2025 alone:52candidates,52validcoverage/parity,48rejected,4accepted and4shortfills. Diagnostics use helpers.debug and remain in the session logs.

Source scope was checked by mechanically removing the added imports, class/docstring rename, diagnostic hooks and the single gate: the remainder exactly equals the original12917-character baseline. No other economic rule was changed. Longs/PAXG/SPY nevertheless change cash PnL through the shared cash and compounding path; they are not fixed independent sleeves.

## Overall performance and components

Stored engine metrics:118trades=97long+21short; finalbalance33326.3298 from10000; net23326.3298; fees3169.1625; annualreturn25.9714%; maximumdrawdown−13.72495%; overallWR48.3051%, longWR44.3299%, shortWR66.6667%.

Root analysis46be126036194c67857c0f30fdce3982/V4 verifies:
- BTCshort:21trades, net2138.669524, fees258.959008, grosspricePnL2397.628532,PF2.27837,WR66.6667%.
- BTClong net13598.72514;SPYlong3473.11536;PAXGlong4115.81976.
- The profitable short cohort is only21observations; correlated/regime-dependent trades and development selection preclude a robustness conclusion.

## True MTM regularity from Root V4

All calendar months:34/63positive=53.9683%.
Active months:34/60positive=56.6667%.
Calendar quarters:15/21positive=71.4286%, matching the reference count rather than meeting80%.

For complete periods:34/61calendar monthspositive=55.74%;34/58active monthspositive=58.62%;14/19quarterspositive=73.68%.

Relative to reference it rescues5months and spoils4. This small net change is insufficient.2022MTM becomes−5.056% versus reference+2.674%; worstquarter−6.017% versus−4.236%. These results weigh against judging the lower headline drawdown/shortprofitfactor in isolation. Annual comparisons remain development diagnostics, not clean OOS evidence.

## Research bookkeeping

One economic change and one run, no tuning. Root V4+components succeeded under46be126036194c67857c0f30fdce3982. Child component-only analysisa940680d01b2483c940651e437d909e7 had already been submitted immediately before the root warning against duplication; it creates no new hypothesis or backtest, and no additional jobs were submitted afterward. Root results are the accounting authority here.

2026 remains reserved, no external data imported, no research scripts or framework changes. Reference source remains intact. The causal probability recipe is separately closed as genuine economic abstention; its zero trades were not used to choose this gate's fixed partitions.
