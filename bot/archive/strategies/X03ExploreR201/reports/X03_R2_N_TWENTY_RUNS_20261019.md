# X03 R2 N201–N210 — ten recipes / twenty completed backtests

All ten predeclared recipes implemented independently, and each B/C pair executed only upon its own root ticket. All20 finished without errors. No retuning, reruns for economic rescue or further variants.2026 remained closed. Development2020-10-15→2025-12-31exclusive is intensively reused, not OOS.

Account10000USDTshared,1%trade/8%aggregate,isolated5x,cap4.4,reserve.001sizingonly,fee.00045side. BTC/PAXG/SPY4h and3M1;warm240/debugtrue/fastfalse/charttrue. B SPYSecond, C SPYMarket, PAXGMarket fixed. Every pair has exact form and six byte-identical captured strategy snapshots verified before execution, persisted in its own Nxxx_PREFLIGHT_20261019.md. All HP defaults unchanged. Individual Nxxx_SESSION_QA_20261019.md persist summaries/hp/taildiagnostics.

QA2247checks finalsource job5fc7620485cc4584aca7791a2242ff6a succeeded; initial2237 jobbd88c663d4e44b9aba69b924bd6a710f succeeded before root-requested terminate diagnostic-label correction. Code and exact final hashes: X03_R2_N_QA_SOURCE_20261019.md and X03_R2_N_SOURCE_QA_20261019.md in this report folder. ATRstub8 synthetic tests check logic/causality, not historical indicators/fills. At closure, all10sources and original BtcExploreR103 readback remained byte-identical to frozen versions; no framework/default/config/live/paper/Pi/package/research_scripts/data changes.

## Engine outcomes — full ledger

|Recipe|Portfolio / session|NetUSDT|CAGR%|DDengine%|Trades|Supplementfills|
|---|---|---:|---:|---:|---:|---:|
|N201|[B](http://localhost:9200/#/backtest/e2c44291-d4cc-4470-9be5-1b2ca512f79d)|10288.952940|14.533660|-8.362852|236|31|
|N201|[C](http://localhost:9200/#/backtest/f962075c-470c-4f67-a689-2a1f8d587ba8)|10489.858483|14.750325|-8.391013|243|31|
|N202|[B](http://localhost:9200/#/backtest/6f8665d3-07ab-4078-bfa8-0eae564bee0e)|10288.952940|14.533660|-8.362852|236|31|
|N202|[C](http://localhost:9200/#/backtest/4fa5d789-4d70-4bee-a6ed-5161a12b10ea)|10489.858483|14.750325|-8.391013|243|31|
|N203|[B](http://localhost:9200/#/backtest/823e74e9-de38-42fa-8c12-d270c4a94270)|11276.470756|15.582460|-9.589264|267|67|
|N203|[C](http://localhost:9200/#/backtest/21493c44-9a9e-40ad-92d8-21890820005c)|11459.657944|15.772671|-9.616784|274|67|
|N204|[B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142)|13056.614915|17.377556|-8.776801|273|79|
|N204|[C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794)|13239.442380|17.555506|-9.057884|280|79|
|N205|[B](http://localhost:9200/#/backtest/68393588-b760-493b-a1ce-8408efdb5bc1)|11579.674908|15.896580|-8.253965|265|69|
|N205|[C](http://localhost:9200/#/backtest/b4c8031c-c6ab-4894-a8d8-1fbab90ae158)|11757.692625|16.079348|-9.009386|272|69|
|N206|[B](http://localhost:9200/#/backtest/ad66e70a-19f3-4fc1-9b29-41872d2bb3ca)|9932.413408|14.144847|-7.501935|210|6|
|N206|[C](http://localhost:9200/#/backtest/648513dd-889a-4bdb-8136-42030b2ebec7)|10117.288201|14.347152|-8.175348|217|6|
|N207|[B](http://localhost:9200/#/backtest/02345430-75b6-477c-91f6-05f9785b2dcd)|12260.420705|16.589044|-8.253965|257|63|
|N207|[C](http://localhost:9200/#/backtest/95363515-d414-4476-a00e-694e4dcde0f6)|12460.722696|16.789533|-9.009386|264|63|
|N208|[B](http://localhost:9200/#/backtest/6fce2f2b-a2b8-4e38-a155-aa0432aaeb24)|10137.325259|14.368988|-9.752996|278|82|
|N208|[C](http://localhost:9200/#/backtest/575aaa80-c0c4-4fdf-9bdd-56eae64404f4)|10314.619504|14.561437|-8.982165|285|82|
|N209|[B](http://localhost:9200/#/backtest/36bd7b1b-064f-4f63-bb3f-885b8560d98a)|9725.621799|13.916754|-8.650316|277|80|
|N209|[C](http://localhost:9200/#/backtest/83b55ed3-4f9f-4932-a3ce-956254f2503f)|9912.920404|14.123428|-8.995979|284|80|
|N210|[B](http://localhost:9200/#/backtest/377d51ab-6fd6-4bcf-b5ee-db55279e18cc)|11463.506045|15.776653|-8.225809|273|79|
|N210|[C](http://localhost:9200/#/backtest/c65f077c-4ea0-417a-b885-92116b7327d8)|11600.222246|15.917737|-9.061540|280|79|

Engine net alone is not the acceptance criterion. Root owns complete fee/fill/wallet/MTM calendars, cost overlays, displacement, exposure and eligibility/selection. No candidate promoted by this report. N204 andN207 exceed baselineX03 nominal net in both portfolios; the rest are lower. Do not infer cost robustness or regularity from that ordering. N206 only6supplements is a sparse sample; retained without relaxing its rule. B/C share BTC/data and are not independent confirmations.

N201/N202 engine metrics and supplemental counters coincide economically; B path ratios differ only at floating rounding1e−14. They are two separately predeclared source mechanisms but may be empirically redundant on continuous OHLCV: ifO=Cprev andTR=range then their formulas equal. Exact candle/fill/path identity remains root-audit responsibility. Ten recipes do not imply ten unique realized paths, independent evidence or ten independent edges. No replacement recipe created after observing coincidence.

N208–N210 keep X03 entry eligibility while exits change subsequent occupancy/capital and thus realized entries/sizes. Long original rules are preserved, not a guarantee of identical quantities or fills. Before state advances while occupied; occupied counter is state at callback, not automatic rejection. All logs use distinctN201..N210 recipe labels. Capacity flags show notional/volatility-share quantity cuts; no margin/aggregate-risk/capacity-zero/lotzero recorded in these tail counters. Counts describe sizing attempts that reach sizing, not all potential signals while occupied.

C engine metrics list one preterminal open trade/negative openPL for all ten pairs. This is an audit item for engine forced terminal liquidation and fees, not a residual-live-position claim; root reconciles final fills/wallet. Tail logs are partial diagnostics only and cannot prove all order modification/cancellation histories.

All twenty exact numeric records:

```json
[
  {
    "recipe": "N201",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/e2c44291-d4cc-4470-9be5-1b2ca512f79d",
    "status": "finished",
    "net": 10288.952940209103,
    "cagr": 14.533660412228745,
    "dd": -8.362851534638803,
    "total": 236,
    "fees": 1536.189243561853,
    "pf": 1.7728286024529605,
    "sharpe": 1.3821616308225806,
    "counts": {
      "closes": 31,
      "events": 36,
      "events_occupied": 3,
      "fills": 31
    }
  },
  {
    "recipe": "N201",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/f962075c-470c-4f67-a689-2a1f8d587ba8",
    "status": "finished",
    "net": 10489.858482860902,
    "cagr": 14.750325301103228,
    "dd": -8.391012861823388,
    "total": 243,
    "fees": 1630.5166432593442,
    "pf": 1.7579414270153415,
    "sharpe": 1.3760634215413368,
    "counts": {
      "closes": 31,
      "events": 36,
      "events_occupied": 3,
      "fills": 31
    }
  },
  {
    "recipe": "N202",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/6f8665d3-07ab-4078-bfa8-0eae564bee0e",
    "status": "finished",
    "net": 10288.952940209103,
    "cagr": 14.533660412228722,
    "dd": -8.362851534638816,
    "total": 236,
    "fees": 1536.189243561853,
    "pf": 1.7728286024529605,
    "sharpe": 1.3821616308225801,
    "counts": {
      "closes": 31,
      "events": 36,
      "events_occupied": 3,
      "fills": 31
    }
  },
  {
    "recipe": "N202",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/4fa5d789-4d70-4bee-a6ed-5161a12b10ea",
    "status": "finished",
    "net": 10489.858482860902,
    "cagr": 14.750325301103228,
    "dd": -8.391012861823388,
    "total": 243,
    "fees": 1630.5166432593442,
    "pf": 1.7579414270153415,
    "sharpe": 1.3760634215413368,
    "counts": {
      "closes": 31,
      "events": 36,
      "events_occupied": 3,
      "fills": 31
    }
  },
  {
    "recipe": "N203",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/823e74e9-de38-42fa-8c12-d270c4a94270",
    "status": "finished",
    "net": 11276.470756050338,
    "cagr": 15.582460156964917,
    "dd": -9.589263708358075,
    "total": 267,
    "fees": 1834.0296751446594,
    "pf": 1.7240476792966726,
    "sharpe": 1.4357789107272072,
    "counts": {
      "closes": 67,
      "events": 78,
      "events_occupied": 10,
      "fills": 67
    }
  },
  {
    "recipe": "N203",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/21493c44-9a9e-40ad-92d8-21890820005c",
    "status": "finished",
    "net": 11459.657943660866,
    "cagr": 15.772671184304832,
    "dd": -9.616784296106252,
    "total": 274,
    "fees": 1932.2481818050487,
    "pf": 1.709900073260976,
    "sharpe": 1.425086426545418,
    "counts": {
      "closes": 67,
      "events": 78,
      "events_occupied": 10,
      "fills": 67
    }
  },
  {
    "recipe": "N204",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142",
    "status": "finished",
    "net": 13056.614915077666,
    "cagr": 17.37755605244038,
    "dd": -8.77680090479469,
    "total": 273,
    "fees": 1912.86465437862,
    "pf": 1.8217438748916535,
    "sharpe": 1.582686191771496,
    "counts": {
      "closes": 79,
      "events": 96,
      "events_occupied": 14,
      "fills": 79
    }
  },
  {
    "recipe": "N204",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794",
    "status": "finished",
    "net": 13239.442379846789,
    "cagr": 17.555505981887354,
    "dd": -9.057883731399553,
    "total": 280,
    "fees": 2012.4242239197674,
    "pf": 1.8050568929499937,
    "sharpe": 1.569754072854379,
    "counts": {
      "closes": 79,
      "events": 96,
      "events_occupied": 14,
      "fills": 79
    }
  },
  {
    "recipe": "N205",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/68393588-b760-493b-a1ce-8408efdb5bc1",
    "status": "finished",
    "net": 11579.6749084668,
    "cagr": 15.896579559794866,
    "dd": -8.253965403629948,
    "total": 265,
    "fees": 1775.631374353798,
    "pf": 1.7841208500973407,
    "sharpe": 1.4671254045703075,
    "counts": {
      "closes": 69,
      "events": 82,
      "events_occupied": 10,
      "fills": 69
    }
  },
  {
    "recipe": "N205",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/b4c8031c-c6ab-4894-a8d8-1fbab90ae158",
    "status": "finished",
    "net": 11757.692624669096,
    "cagr": 16.079347512042318,
    "dd": -9.009386028595156,
    "total": 272,
    "fees": 1870.5323646733837,
    "pf": 1.7687028289961577,
    "sharpe": 1.4572995985466797,
    "counts": {
      "closes": 69,
      "events": 82,
      "events_occupied": 10,
      "fills": 69
    }
  },
  {
    "recipe": "N206",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/ad66e70a-19f3-4fc1-9b29-41872d2bb3ca",
    "status": "finished",
    "net": 9932.413407937414,
    "cagr": 14.144846986320703,
    "dd": -7.50193458375742,
    "total": 210,
    "fees": 1424.695009773542,
    "pf": 1.8281727576952729,
    "sharpe": 1.3891021068217058,
    "counts": {
      "closes": 6,
      "events": 6,
      "events_occupied": 0,
      "fills": 6
    }
  },
  {
    "recipe": "N206",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/648513dd-889a-4bdb-8136-42030b2ebec7",
    "status": "finished",
    "net": 10117.288200511588,
    "cagr": 14.347151913149236,
    "dd": -8.175348080148082,
    "total": 217,
    "fees": 1519.7208802298528,
    "pf": 1.8067200935992218,
    "sharpe": 1.3802067637469817,
    "counts": {
      "closes": 6,
      "events": 6,
      "events_occupied": 0,
      "fills": 6
    }
  },
  {
    "recipe": "N207",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/02345430-75b6-477c-91f6-05f9785b2dcd",
    "status": "finished",
    "net": 12260.420705074419,
    "cagr": 16.589043684007997,
    "dd": -8.253965403629948,
    "total": 257,
    "fees": 1790.6208879792866,
    "pf": 1.8311655090760708,
    "sharpe": 1.5464458191718584,
    "counts": {
      "closes": 63,
      "events": 74,
      "events_occupied": 8,
      "fills": 63
    }
  },
  {
    "recipe": "N207",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/95363515-d414-4476-a00e-694e4dcde0f6",
    "status": "finished",
    "net": 12460.722695969744,
    "cagr": 16.789532534874763,
    "dd": -9.009386028595156,
    "total": 264,
    "fees": 1891.349461415248,
    "pf": 1.813141834395206,
    "sharpe": 1.5367385281639394,
    "counts": {
      "closes": 63,
      "events": 74,
      "events_occupied": 8,
      "fills": 63
    }
  },
  {
    "recipe": "N208",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/6fce2f2b-a2b8-4e38-a155-aa0432aaeb24",
    "status": "finished",
    "net": 10137.32525881614,
    "cagr": 14.36898771899533,
    "dd": -9.75299552452704,
    "total": 278,
    "fees": 1815.6116787016272,
    "pf": 1.6781123456346703,
    "sharpe": 1.3551672501793792,
    "counts": {
      "closes": 82,
      "events": 95,
      "events_occupied": 9,
      "fills": 82
    }
  },
  {
    "recipe": "N208",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/575aaa80-c0c4-4fdf-9bdd-56eae64404f4",
    "status": "finished",
    "net": 10314.619504108192,
    "cagr": 14.56143664942935,
    "dd": -8.982165317340007,
    "total": 285,
    "fees": 1907.5999105754881,
    "pf": 1.6667430801152443,
    "sharpe": 1.3482811637017598,
    "counts": {
      "closes": 82,
      "events": 95,
      "events_occupied": 9,
      "fills": 82
    }
  },
  {
    "recipe": "N209",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/36bd7b1b-064f-4f63-bb3f-885b8560d98a",
    "status": "finished",
    "net": 9725.621798823497,
    "cagr": 13.91675409254811,
    "dd": -8.650316296359284,
    "total": 277,
    "fees": 1775.1352361299794,
    "pf": 1.6576930197700173,
    "sharpe": 1.3178017344862538,
    "counts": {
      "closes": 80,
      "events": 95,
      "events_occupied": 13,
      "fills": 80
    }
  },
  {
    "recipe": "N209",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/83b55ed3-4f9f-4932-a3ce-956254f2503f",
    "status": "finished",
    "net": 9912.920404237298,
    "cagr": 14.123427898973361,
    "dd": -8.995979060451642,
    "total": 284,
    "fees": 1867.277930428022,
    "pf": 1.6476512368999379,
    "sharpe": 1.313435073343553,
    "counts": {
      "closes": 80,
      "events": 95,
      "events_occupied": 13,
      "fills": 80
    }
  },
  {
    "recipe": "N210",
    "portfolio": "B",
    "url": "http://localhost:9200/#/backtest/377d51ab-6fd6-4bcf-b5ee-db55279e18cc",
    "status": "finished",
    "net": 11463.50604538265,
    "cagr": 15.77665273647626,
    "dd": -8.225809059616463,
    "total": 273,
    "fees": 1844.756605685027,
    "pf": 1.7399265393812613,
    "sharpe": 1.4534643130818696,
    "counts": {
      "closes": 79,
      "events": 95,
      "events_occupied": 13,
      "fills": 79
    }
  },
  {
    "recipe": "N210",
    "portfolio": "C",
    "url": "http://localhost:9200/#/backtest/c65f077c-4ea0-417a-b885-92116b7327d8",
    "status": "finished",
    "net": 11600.222245945082,
    "cagr": 15.91773725286263,
    "dd": -9.061539998308,
    "total": 280,
    "fees": 1937.9860893684772,
    "pf": 1.7242221158994568,
    "sharpe": 1.44022816928927,
    "counts": {
      "closes": 79,
      "events": 95,
      "events_occupied": 13,
      "fills": 79
    }
  }
]
```
