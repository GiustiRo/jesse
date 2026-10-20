# X03 R2 — validation family execution QA

Seven frozen sensitivity/stress recipes X03ValidR201..207 completed in B/C:14full backtests finished, no stopped/cancelled/failed runs. Each pair launched concurrently only after its root ticket. No extra recipes, parameter selection or reruns. All14forms preserve10000USDT/.00045per side/5xisolated/warm240/debugtrue/fastfalse/charttrue/4h and3M1routes/2020-10-15→2025-12-31exclusive. Risk1%trade/8%aggregate/cap4.4/.001sizingreserve preserved in source. C explicit perpetual_futures/annualization365 fields copied per draft; global configuration untouched.

42route snapshots matched frozen sources, HP defaults26/20/80/26/2/4.2/2.25 with emptyDNA, and terminal logs checked. Final MCP readback of all7sources matches QAembedded bytes and originalBtcExploreR103 remains identical. Root performs complete executed fills/MTM/calendar/terminal reconciliation, so raw terminal open counters are not treated as residuals. C has final SPY MARKET close in each session's terminal logs.

Source QA156PASS in11b3b51b8d2e4f8395c622b1ac986b0c:84ASTidentity checks for inherited management/risk/helpers;48controlledOFATchecks;18delayedstatechecks;6horizonchecks. Priorb8b02f7f4e924618bf28ec30ed2f4f1f failed because synthetic fake omittedsymbol; only fake changed. Controlled ATR/API stubs verify invariants, not historical indicators, liquidity or edge.

V207strongtimingstress counters reconcile in both portfolios:95sourceevents=78due+17occupied/pendingexpiries;78due=76fills/closes+2originalpriority overrides. No missing-clock/invalid-clock count appeared. Event geometryD/TP frozen atsource, due exactlynext4hclose, protection relative actualfill,48hdeadline fromfill. This is a coarse decision-delay stress, not a model of minute latency. The changed occupancy path permits one additional original BTC long; unchanged long rules do not imply unchanged retained fills.

Only nocional/volshare quota cuts were recorded in BTCshort sizing; no zero capacity/lot-rounding/riskaggregate/margin-limit counts. These counters describe plans reaching sizing and cannot count all signals while occupied. Deferred events and occupied counts are distinct.

## Engine matrix, descriptive only

| Variant | Change | NetoB | NetoC | DDmotorB | DDmotorC |
|---|---|---:|---:|---:|---:|
| V201 | horizon8 | 9748.31 | 9928.66 | -10.77% | -10.70% |
| V202 | horizon16 | 12393.83 | 12614.45 | -7.51% | -7.70% |
| V203 | TP1.5R | 11525.62 | 11733.80 | -8.21% | -9.03% |
| V204 | TP2.5R | 12701.16 | 12906.32 | -8.24% | -9.00% |
| V205 | hold24h | 9992.67 | 10184.26 | -8.70% | -8.99% |
| V206 | hold72h | 11516.32 | 11692.92 | -8.22% | -9.04% |
| V207 | delay4h | 8453.33 | 8588.88 | -9.11% | -9.30% |

All six OFAT neighbors retain a nominal positive portfolio increment vs no-X03 controls, but the lower-horizon and shorter-hold outcomes vary materially. Delay4h falls below no-X03 controls even nominally. Cost/calendar robustness is judged from root's audited full matrix, not raw portfolio profit or selecting the best parameter. V201+10 incremental friction failure remains in the record without recalibration. All neighbors/stress cases are excluded from economic winner selection.

No2026inspection, live/paper/Pi/restart/installation/funding/newdata/research_scripts, framework changes or global config changes. Baseline bootstrap and actualfee bootstrap reports are conditional descriptions; no confirmatory pvalues or claims of nooverfit.
