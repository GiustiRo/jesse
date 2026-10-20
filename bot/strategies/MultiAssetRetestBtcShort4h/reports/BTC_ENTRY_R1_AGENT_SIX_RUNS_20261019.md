# BTC entry R1 six-run agent report — 2026-10-19

Three frozen additive short-entry gates separately in B/C, exactly six economic full runs, all finished without exceptions. Controls reused, no retuning, combinations, retries, independent sleeves or2026. Account10000sharedUSDT/1%trade/8%aggregate/isolated5x/gross4.4/fee.00045eachside/alltypes/reserve.001sizingonly. Six4h/threeM1 formulations from common protocol, fastfalse/debugtrue/charttrue/warm240. Development2020-10-15→2025-12-31exclusive, not clean OOS.

|Recipe|Portfolio/session|NetUSDT|CAGR%|DDengine%|Sharpe|N|Shorts|FeesUSDT|PFenginegross|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
|E01|[B](http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6)|8869.02621438|12.95082784|-7.51217863|1.29804484|202|121|1311.94072375|1.77882767|
|E01|[C](http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a)|9028.41756286|13.13320955|-8.16801280|1.28889854|209|121|1402.99678910|1.75816762|
|E02|[B](http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6)|7157.30730885|10.90928611|-9.46560918|1.16488843|143|62|936.47196054|1.88766675|
|E02|[C](http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3)|7323.18212977|11.11414894|-9.15032339|1.15923438|150|62|1021.74140635|1.85872125|
|E03|[B](http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c)|7628.67248120|11.48733039|-6.19673817|1.22303384|125|44|955.83624261|1.98059289|
|E03|[C](http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823)|7790.99504230|11.68349869|-6.92414508|1.21595453|132|44|1046.06797738|1.93847748|

PF column is engine aggregate gross_profit/abs(gross_loss), subject to root executed-fill reconciliation. No calendar acceptance can be derived from these rows. Relative to controls, all six have lower engine net/CAGR and Sharpe. E03 lowers engine DD with fewer shorts; this alone does not establish improved regularity or a useful net benefit.

E01directionalvolume: D>U across6closed4hreturns. E02distributeddecline: positive sum downside and maximum share<=half. E03downsidefloor: original target>=30prior4hlow, signalexcluded. Each modifies only _short_plan with added _entry_gate; original long signals, stop/target/72h, sizing/reservations/lifecycle preserved. Byte normalization checked on actual MCP readbacks, and root independently approved before tickets. No mutable state or future data in helpers.

18/18 strategy snapshots checked exact against contemporaneous frozen sources before and after runs. All forms retain10k/.00045/isolated5x/warm240/debugtrue/fastfalse/charttrue, same dates/routes. Eight stored hp entries identical session defaults; source declarations identical allroutes.18capacityJSON records captured: BTC long attempts45each; shortattempts206/115/74 forE01/E02/E03, shortcuts B19/C18,9/9,10/10 respectively. No observedrisk/margin/capacityzero/lotzero cuts anywhere. PAXG38/SPYB20/C19attempts. Counters start only after gate at flat sizing; no inference of missed occupied opportunities or future fills.

EachC summary reports one preterminalSPYposition; final logs show boundaryMARKET execution and finalwallet, preserved for rootaudit rather than deleting trade. B summariesopen0. Engine counters alone do not prove residual exposure; execution reconciliation remains root responsibility. No native tokenized execution/funding/spread proof.

Root notified E01audit: completeactivepositiveB36/57,C37/57;Q15/19and16/19; shortnet+10bps245.15/234.29 versusbaseline522/516. This supports discardingE01 unchanged, not revising gates. FullMTM/cost/concentration/perroute and E02/E03 audit remain root-owned; agent did not duplicate analysis.

QA reports BTC_ENTRY_R1_IMPLEMENTATION_REVIEW_20261019.md and BTC_ENTRY_R1_E01/E02/E03_SESSION_QA_20261019.md under this same reportfolder preserve forms/metrics/capacity. Nothing promoted; no new hypotheses or runs requested. PAXG/SPY and originals untouched.
