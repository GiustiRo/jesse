# Original signal-high invalidation — initial result
Development2020-10-15→2025-12-31exclusive,4h,normal,allthreeassets,basefee.2026sealed.
[Experiment](http://localhost:9200/#/backtest/2168b24e-632b-4dca-be9c-48677c7b5a58), [reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Protocol saved before execution. Only short change: later closed bar above original signal high fully liquidates; original stop,target,72h retained.

Finished222trades97long125short,terminalflat.CAGR27.28529777%,DD-15.00475203%,Sharpe1.26170834,net25178.893996USDT.
Reference28.82938670%/-14.89050602%/1.31642812/net27461.463375.
Shortnet3500.495844,PF1.230215,WR52%,fee1481.410328;reference5287.019403/PF1.360236/55.28%.
Annual CLOSED shortPNL2020partial-207.03,2021-410.91,2022+2084.32,2023+871.20,2024-341.25,2025partial+1504.16. These are closed-PnL not calendarMTMreturns.
Long97tradesnet21678.398152;longrules unchanged but capital/different reservations affectsize.

## Nonredundancy and visibility
Requested diagnostic: count originalsignalhigh below initialhardstop. Strategy emits jh.debug per shortfill; MCP logs explicitly reports available=false/no logfile even terminal. Therefore that exactcount is unavailable; no filesystem workaround performed.
Complete stored executedexitorders show46STOP,64LIMIT,15MARKET. Ten MARKET exits occur before72h and away from terminalday. Given the code's only non-timeout liquidation path is high-reclaim, this demonstrates the new condition fires and is not wholly redundant. Their combinedclosedPNL=-2163.362892; this is NOT a causal estimate of saving/cost vs holding to originalexit. Some reference trades become overlapping/differententries when capital is freed.
Analysis88d7635a77f7408184dbff2b0d552da2(component) and986aafaf9b0a4f0ca049af4e54f08fb0(exitclassification) succeeded.

Initial decision: do not promote; reward/DD/Sharpe and short economics deteriorate. Root true-calendar MTM still pending at report time. No arbitrary buffer sweep or timing optimization. Originalreference unchanged.