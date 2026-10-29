# N204 R4 experimental final execution QA — 2026-10-19

All four frozen recipes X401–404 completed in both B/C:8/8 finished, no session exceptions. Each pair ran only after its root ticket. No new variants, reruns, analysis jobs or2026 inspection were added by this closeout.

|Recipe|Portfolio|Session|Net USDT|Engine DD %|
|---|---|---|---|---|
|X401|B|[finished](http://localhost:9200/#/backtest/97c7fc93-a002-445a-b18d-43d33a4d31e6)|7731.929598|-7.512634|
|X401|C|[finished](http://localhost:9200/#/backtest/a2555538-0233-44d2-974c-9ab78aefe7af)|7922.545416|-8.168013|
|X402|B|[finished](http://localhost:9200/#/backtest/225f6073-dcee-4a04-856b-b0d448f9dc74)|9159.750815|-9.879783|
|X402|C|[finished](http://localhost:9200/#/backtest/277a6cf9-8801-4cb2-9306-f68f211089e2)|9330.521068|-9.855058|
|X403|B|[finished](http://localhost:9200/#/backtest/9e5f78d7-5f2f-4e2a-8a03-05226769cdb5)|7786.571305|-9.676562|
|X403|C|[finished](http://localhost:9200/#/backtest/21deebfc-94b5-48e0-9660-18fe1e206de4)|8006.997295|-10.419664|
|X404|B|[finished](http://localhost:9200/#/backtest/5c1c5772-7b01-4970-aea5-1677abd79af6)|7577.450711|-9.105497|
|X404|C|[finished](http://localhost:9200/#/backtest/b1cad85f-ba07-4931-a6e1-2d9703b53584)|7775.432430|-9.103251|

QA PASS each8sessions: exact frozen form except intended BTC class, all three saved source snapshots byteexact, expected HP26/20/80/26/2/4.2/2.25 and emptyDNA. Contract10000USDT, fee.00045/side, isolated5x, warm240, debugtrue, fastfalse, charttrue, three4h routes andthree1m feeds,2020-10-15→2025-12-31 exclusive. Sources N204 andX401–404 reread at family close and all unchanged against approved versions; original N204 immutable.

|Recipe|Events both|Occupied both|Fills both|Closes both|
|---|---|---|---|---|
|X401|17|3|9|9|
|X402|52|10|42|42|
|X403|104|19|74|74|
|X404|68|12|56|56|

C's engine summary retains open-count1/open_pl metadata preceding terminal liquidation. Executed terminal SPY market closes and final wallets are confirmed in persisted logs; root MTM/fills accounting is authoritative. Source equality preserves rules, not all economic execution opportunities: X402 retains30/31 reference BTC longs, with a supplemental short spanning the absent long's reference entry timestamp. See N204_R4_X402_OCCUPANCY_NOTE_20261019.md; no exact counterfactual opportunity cost inferred.

All four experimental nominal nets are below N204 in both B/C, failing the first frozen eligibility gate. This is an observation for this family, not an early selection among the12 overall recipes. Root performs common MTM/61–63calendar/cost overlays, eligibility/ranking and final interpretation. No promotion, OOS claim or claim of absent overfitting.

Prior source QA9f44e855f3c544368430769cf3b412b4 succeeded245checks. Independent auditor review saved separately.
