# Daily bear + failed recovery — rejected first prototype
[Finished experiment](http://localhost:9200/#/backtest/79338950-d982-49ca-b9dd-dfc9926adba5).
Protocol/source frozen before execution. BTC-only4h trading plus CLOSED1Ddata,2020-10-15→2025-12-31exclusive,10k,5xisolated,fee.00045eachside,risk1%. No2026. Standalone has no inactiveotherasset capacity reservation; do not compare raw dollars/returns as sameallocation as multiassetreference.

## Result
54shorts,17wins37losses,WR31.48%,PF0.766409. Net-660.730157USDT,CAGR-1.302547%,DD-16.295516%,Sharpe-.230078,flatterminal. Commission185.804181USDT; precommissiongross-474.925976. Thus costs are not the sole reason this fails.
Averagewin127.52 vsaverageloss76.45; insufficient hitrate for payoffratio1.668.
Largestwin1339.23 is61.78% of sumpositivePNL2167.84.
First actualentry1632772980000UTCms (~2021Sep); absenceof2020trades is not a coveragefailure.

## Annual closed-trade amounts (not MTM returns)
2021-63.664374;2022+17.745468;2023-145.525532;2024-90.869239;2025partial-378.416479USDT.
The intended bear-year contribution is effectively negligible in2022. No basis to call this a hedge.
Fixedfill/fixedqty costdiagnostic: an extra10bps perroundtrip yields-867.179246;25bps yields-1176.852881. These are arithmetic diagnostics, not rerun CAGR/DD or complete fillsensitivity.

## Coverage and correctness
BTC-only withBTC1D succeeded withoutimports, resolving the former multiassetwarmup failure duePAXG's shorterhistory. No fabricatedcandles,frameworkedits orsettingsmutation.
Dailycandles explicitlycutby opentime+1D<=decisiontime. SMA200 slope compares current[-1] to[-11], exactlytenobservationintervals. Stoprelativeactualfill, postentrybestclose initializedactualfill. Fullentry/fullExit,noadding.
Complete-snapshotrun_analysis2d143828392343ceb5daa68ffbdb9aab succeeded.

## Decision
Reject this prototype, do not combine or sweep nearby thresholds to rescue it. A conventional dailybearfilter does not create a continuationedge. A different structuralpremise would need its own protocol; none launched. Reference remains frozen. RootcalendarMTM may describe periods but cannot reverse the negative standalone expectancy.