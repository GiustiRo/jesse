# Walk-forward E1V — diagnostic ablations

Prior train selection: **SIN_CANDIDATA**. Evaluation does not change selection.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 93 | -10.94 | 0.884 | -20.77 | [dashboard](http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8) |
| H1_PF | 91 | -6.23 | 0.933 | -17.32 | [dashboard](http://localhost:9200/#/backtest/7ea4be97-2bdc-4bfd-a7d3-401b39af2a40) |
| H1_PFOI | 58 | 11.40 | 1.184 | -8.23 | [dashboard](http://localhost:9200/#/backtest/d2c228a6-1cc3-4ca4-b452-424d137c2e2d) |
| H1_POI | 59 | 8.92 | 1.142 | -8.44 | [dashboard](http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29) |
| H2_P | 38 | 4.84 | 1.106 | -16.89 | [dashboard](http://localhost:9200/#/backtest/801e04d7-eb9b-4d92-bc49-7fc2db1fe5cb) |
| H2_PF | 2 | -1.47 | 0.269 | -1.99 | [dashboard](http://localhost:9200/#/backtest/372dea0d-af5b-4c45-a712-7b199e4f35fd) |
| H2_PFOI | 0 | 0.00 | — | 0.00 | [dashboard](http://localhost:9200/#/backtest/76d2e287-1535-4574-ab52-90622ab3b3de) |
| H2_POI | 18 | -2.23 | 0.908 | -15.77 | [dashboard](http://localhost:9200/#/backtest/6ed903fb-abca-4f00-aadb-a841e8f2d45e) |
| H3_P | 176 | -27.52 | 0.842 | -42.42 | [dashboard](http://localhost:9200/#/backtest/5a8a5b98-c60d-46c7-98a1-b256e8575cbf) |
| H3_PF | 5 | 4.50 | 2.504 | -2.01 | [dashboard](http://localhost:9200/#/backtest/d79395ab-ab58-4bcc-b4b8-88a363e78bb0) |
| H3_PFOI | 2 | 2.76 | 3.807 | -1.24 | [dashboard](http://localhost:9200/#/backtest/f21f62e6-8b5e-40c0-a108-e564ccfc8562) |
| H3_POI | 125 | -2.97 | 0.976 | -20.78 | [dashboard](http://localhost:9200/#/backtest/6d688cbc-1adf-4452-a3c9-99a111221146) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "ed789043-2aa2-4714-8963-112eadbc56b8",
    "title": "MCP Backtest: WFV1 E1V H1_P",
    "trades": 93,
    "net": -1094.4420324596422,
    "net_pct": -10.94442032459641,
    "pf": 0.8836627462659472,
    "dd": -20.772017128420362,
    "gross_price": -380.19342023868455,
    "fees": 700.3356315021208,
    "funding": -13.91298071883538,
    "funding_events": 132,
    "proxy_events": 132,
    "turnover": 155.6301403338047,
    "holding_seconds": 4084800,
    "directions": {
      "short": {
        "trades": 55,
        "net": 448.5372653631755,
        "gross": 849.1955759070488,
        "fees": 415.34608368292675,
        "funding": 14.687773139053423
      },
      "long": {
        "trades": 38,
        "net": -1542.9792978228168,
        "gross": -1229.388996145734,
        "fees": 284.98954781919434,
        "funding": -28.600753857888805
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -18.059284800997176,
        "end_equity": 8194.071519900283
      },
      {
        "month": "2022-02",
        "return_pct": 1.0674295385028731,
        "end_equity": 8281.537459709749
      },
      {
        "month": "2022-03",
        "return_pct": 6.062184723145725,
        "end_equity": 8783.579558433863
      },
      {
        "month": "2022-04",
        "return_pct": -6.057471020788863,
        "end_equity": 8251.516772093797
      },
      {
        "month": "2022-05",
        "return_pct": 3.5959319004029044,
        "end_equity": 8548.235695968613
      },
      {
        "month": "2022-06",
        "return_pct": 4.18007041780879,
        "end_equity": 8905.557967540368
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8"
  },
  {
    "name": "s1",
    "session_id": "7ea4be97-2bdc-4bfd-a7d3-401b39af2a40",
    "title": "MCP Backtest: WFV1 E1V H1_PF",
    "trades": 91,
    "net": -623.1561761327953,
    "net_pct": -6.231561761327953,
    "pf": 0.932918161379094,
    "dd": -17.316246071631358,
    "gross_price": 103.4656961265693,
    "fees": 711.9419502481097,
    "funding": -14.679922011255597,
    "funding_events": 132,
    "proxy_events": 132,
    "turnover": 158.20932227735776,
    "holding_seconds": 4073400,
    "directions": {
      "short": {
        "trades": 53,
        "net": 971.323228265403,
        "gross": 1371.443614951952,
        "fees": 415.29935791698017,
        "funding": 15.178971230431477
      },
      "long": {
        "trades": 38,
        "net": -1594.479404398199,
        "gross": -1267.9779188253822,
        "fees": 296.64259233112983,
        "funding": -29.858893241687078
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -14.680638353073139,
        "end_equity": 8531.936164692686
      },
      {
        "month": "2022-02",
        "return_pct": 1.0674292713555245,
        "end_equity": 8623.008548727985
      },
      {
        "month": "2022-03",
        "return_pct": 6.06218473282798,
        "end_equity": 9145.751256479423
      },
      {
        "month": "2022-04",
        "return_pct": -5.842268052542565,
        "end_equity": 8611.431952657116
      },
      {
        "month": "2022-05",
        "return_pct": 3.595931553710119,
        "end_equity": 8921.09315146899
      },
      {
        "month": "2022-06",
        "return_pct": 5.1086863981816055,
        "end_equity": 9376.843823867197
      }
    ],
    "max_accounting_error": 7.275957614183426e-12,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/7ea4be97-2bdc-4bfd-a7d3-401b39af2a40"
  },
  {
    "name": "s2",
    "session_id": "88e7e822-cb4d-49f7-97ab-ec5743786d29",
    "title": "MCP Backtest: WFV1 E1V H1_POI",
    "trades": 59,
    "net": 892.270959608658,
    "net_pct": 8.922709596086582,
    "pf": 1.1417465005354768,
    "dd": -8.440659642267468,
    "gross_price": 1434.7033690907786,
    "fees": 534.7920857039071,
    "funding": -7.640323778212991,
    "funding_events": 91,
    "proxy_events": 91,
    "turnover": 118.84268571197933,
    "holding_seconds": 2877480,
    "directions": {
      "short": {
        "trades": 33,
        "net": 1350.5369228645134,
        "gross": 1629.218624001262,
        "fees": 298.9008819023401,
        "funding": 20.21918076559228
      },
      "long": {
        "trades": 26,
        "net": -458.2659632558559,
        "gross": -194.51525491048363,
        "fees": 235.891203801567,
        "funding": -27.85950454380526
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -5.097745856517832,
        "end_equity": 9490.225414348217
      },
      {
        "month": "2022-02",
        "return_pct": 6.744943457072483,
        "end_equity": 10130.335752494728
      },
      {
        "month": "2022-03",
        "return_pct": 9.063345310854952,
        "end_equity": 11048.483062892321
      },
      {
        "month": "2022-04",
        "return_pct": -4.017826127988499,
        "end_equity": 10604.57422364505
      },
      {
        "month": "2022-05",
        "return_pct": 2.3044086278102283,
        "end_equity": 10848.946946997265
      },
      {
        "month": "2022-06",
        "return_pct": 0.39933841342434384,
        "end_equity": 10892.270959608653
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29"
  },
  {
    "name": "s3",
    "session_id": "d2c228a6-1cc3-4ca4-b452-424d137c2e2d",
    "title": "MCP Backtest: WFV1 E1V H1_PFOI",
    "trades": 58,
    "net": 1140.0233956459927,
    "net_pct": 11.400233956459926,
    "pf": 1.1840928041841576,
    "dd": -8.23091591683709,
    "gross_price": 1684.7239811229902,
    "fees": 536.8306120342154,
    "funding": -7.869973442782157,
    "funding_events": 91,
    "proxy_events": 91,
    "turnover": 119.29569156315893,
    "holding_seconds": 2876340,
    "directions": {
      "short": {
        "trades": 32,
        "net": 1608.335143591434,
        "gross": 1883.6670103235253,
        "fees": 295.9271698535864,
        "funding": 20.59530312149535
      },
      "long": {
        "trades": 26,
        "net": -468.31174794544137,
        "gross": -198.94302920053505,
        "fees": 240.90344218062887,
        "funding": -28.46527656427749
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -3.160965129850868,
        "end_equity": 9683.903487014913
      },
      {
        "month": "2022-02",
        "return_pct": 6.744943351161026,
        "end_equity": 10337.077291395177
      },
      {
        "month": "2022-03",
        "return_pct": 9.063345267190881,
        "end_equity": 11273.962296850705
      },
      {
        "month": "2022-04",
        "return_pct": -3.7979503978827878,
        "end_equity": 10845.782800940307
      },
      {
        "month": "2022-05",
        "return_pct": 2.304408584868445,
        "end_equity": 11095.713950901361
      },
      {
        "month": "2022-06",
        "return_pct": 0.3993383836381703,
        "end_equity": 11140.023395646005
      }
    ],
    "max_accounting_error": 1.2732925824820995e-11,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/d2c228a6-1cc3-4ca4-b452-424d137c2e2d"
  },
  {
    "name": "s4",
    "session_id": "801e04d7-eb9b-4d92-bc49-7fc2db1fe5cb",
    "title": "MCP Backtest: WFV1 E1V H2_P",
    "trades": 38,
    "net": 484.17956697209485,
    "net_pct": 4.841795669720953,
    "pf": 1.1063311783690086,
    "dd": -16.885215908692697,
    "gross_price": 857.3884298682847,
    "fees": 370.47293395769594,
    "funding": -2.735928938492919,
    "funding_events": 49,
    "proxy_events": 49,
    "turnover": 82.32731865726576,
    "holding_seconds": 1575540,
    "directions": {
      "long": {
        "trades": 24,
        "net": -65.71051802291103,
        "gross": 181.50489279678874,
        "fees": 233.4646576405642,
        "funding": -13.750753179135485
      },
      "short": {
        "trades": 14,
        "net": 549.8900849950062,
        "gross": 675.8835370714957,
        "fees": 137.0082763171317,
        "funding": 11.014824240642568
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": 7.40928596597723,
        "end_equity": 10740.928596597723
      },
      {
        "month": "2022-02",
        "return_pct": 14.022540373603887,
        "end_equity": 12247.079645555605
      },
      {
        "month": "2022-03",
        "return_pct": -2.174891661974687,
        "end_equity": 11980.718931509016
      },
      {
        "month": "2022-04",
        "return_pct": 0.6740294854971962,
        "end_equity": 12061.472509681933
      },
      {
        "month": "2022-05",
        "return_pct": -6.174914804418242,
        "end_equity": 11316.686858050747
      },
      {
        "month": "2022-06",
        "return_pct": -7.3564577823976744,
        "end_equity": 10484.179566972098
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/801e04d7-eb9b-4d92-bc49-7fc2db1fe5cb"
  },
  {
    "name": "s5",
    "session_id": "372dea0d-af5b-4c45-a712-7b199e4f35fd",
    "title": "MCP Backtest: WFV1 E1V H2_PF",
    "trades": 2,
    "net": -146.5537248856458,
    "net_pct": -1.4655372488564582,
    "pf": 0.26851070577829184,
    "dd": -1.9927775196565745,
    "gross_price": -128.62718170375746,
    "fees": 17.22076979851343,
    "funding": -0.7057733833749397,
    "funding_events": 4,
    "proxy_events": 4,
    "turnover": 3.8268377330029844,
    "holding_seconds": 113700,
    "directions": {
      "long": {
        "trades": 2,
        "net": -146.5537248856458,
        "gross": -128.62718170375746,
        "fees": 17.22076979851343,
        "funding": -0.7057733833749397
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -1.4655372488564855,
        "end_equity": 9853.446275114351
      },
      {
        "month": "2022-02",
        "return_pct": 0,
        "end_equity": 9853.446275114351
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 9853.446275114351
      },
      {
        "month": "2022-04",
        "return_pct": 0,
        "end_equity": 9853.446275114351
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 9853.446275114351
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 9853.446275114351
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/372dea0d-af5b-4c45-a712-7b199e4f35fd"
  },
  {
    "name": "s10",
    "session_id": "6d688cbc-1adf-4452-a3c9-99a111221146",
    "title": "MCP Backtest: WFV1 E1V H3_POI",
    "trades": 125,
    "net": -296.92431486099116,
    "net_pct": -2.969243148609905,
    "pf": 0.9764130797779418,
    "dd": -20.784699729324373,
    "gross_price": 759.7059879847573,
    "fees": 1041.5163318187986,
    "funding": -15.113971026949065,
    "funding_events": 214,
    "proxy_events": 214,
    "turnover": 231.4480737375111,
    "holding_seconds": 6726540,
    "directions": {
      "short": {
        "trades": 65,
        "net": 847.9622640412698,
        "gross": 1346.871381527084,
        "fees": 540.149466795977,
        "funding": 41.24034931016254
      },
      "long": {
        "trades": 60,
        "net": -1144.8865789022602,
        "gross": -587.165393542327,
        "fees": 501.36686502282197,
        "funding": -56.3543203371116
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -5.439685190440868,
        "end_equity": 9456.031480955913
      },
      {
        "month": "2022-02",
        "return_pct": 2.8435391217344286,
        "end_equity": 9724.917435480418
      },
      {
        "month": "2022-03",
        "return_pct": 8.292749951686517,
        "end_equity": 10531.380521412775
      },
      {
        "month": "2022-04",
        "return_pct": -14.794756070223992,
        "end_equity": 8973.288462442672
      },
      {
        "month": "2022-05",
        "return_pct": 2.766272454810048,
        "end_equity": 9221.514069469871
      },
      {
        "month": "2022-06",
        "return_pct": 5.222153455943523,
        "end_equity": 9703.07568513901
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/6d688cbc-1adf-4452-a3c9-99a111221146"
  },
  {
    "name": "s11",
    "session_id": "f21f62e6-8b5e-40c0-a108-e564ccfc8562",
    "title": "MCP Backtest: WFV1 E1V H3_PFOI",
    "trades": 2,
    "net": 275.8694281159505,
    "net_pct": 2.7586942811595048,
    "pf": 3.806913975479934,
    "dd": -1.2395316311512805,
    "gross_price": 294.90227230336023,
    "fees": 17.68738127621011,
    "funding": -1.3454629111996814,
    "funding_events": 3,
    "proxy_events": 3,
    "turnover": 3.930529172491136,
    "holding_seconds": 109980,
    "directions": {
      "long": {
        "trades": 2,
        "net": 275.8694281159505,
        "gross": 294.90227230336023,
        "fees": 17.68738127621011,
        "funding": -1.3454629111996814
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2022-02",
        "return_pct": 3.7415153812211166,
        "end_equity": 10374.15153812211
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 10374.15153812211
      },
      {
        "month": "2022-04",
        "return_pct": -0.9473749216502347,
        "end_equity": 10275.86942811595
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 10275.86942811595
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 10275.86942811595
      }
    ],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/f21f62e6-8b5e-40c0-a108-e564ccfc8562"
  },
  {
    "name": "s6",
    "session_id": "6ed903fb-abca-4f00-aadb-a841e8f2d45e",
    "title": "MCP Backtest: WFV1 E1V H2_POI",
    "trades": 18,
    "net": -222.9135601374863,
    "net_pct": -2.229135601374868,
    "pf": 0.9084886255254537,
    "dd": -15.77038894304652,
    "gross_price": -54.7013534981341,
    "fees": 166.11750655997312,
    "funding": -2.0947000793791757,
    "funding_events": 17,
    "proxy_events": 17,
    "turnover": 36.91500145777182,
    "holding_seconds": 599820,
    "directions": {
      "short": {
        "trades": 7,
        "net": -273.0754155870932,
        "gross": -209.4492577497302,
        "fees": 64.40653705372782,
        "funding": 0.7803792163647818
      },
      "long": {
        "trades": 11,
        "net": 50.16185544960675,
        "gross": 154.7479042515957,
        "fees": 101.71096950624533,
        "funding": -2.875079295743958
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": 3.400662642512753,
        "end_equity": 10340.066264251276
      },
      {
        "month": "2022-02",
        "return_pct": 12.259043527532887,
        "end_equity": 11607.659488361583
      },
      {
        "month": "2022-03",
        "return_pct": -3.959999972833661,
        "end_equity": 11147.996175775841
      },
      {
        "month": "2022-04",
        "return_pct": -0.9763824250628939,
        "end_equity": 11039.149100368883
      },
      {
        "month": "2022-05",
        "return_pct": -5.899022011194532,
        "end_equity": 10387.947265089539
      },
      {
        "month": "2022-06",
        "return_pct": -5.880476764451137,
        "end_equity": 9777.08643986251
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/6ed903fb-abca-4f00-aadb-a841e8f2d45e"
  },
  {
    "name": "s7",
    "session_id": "76d2e287-1535-4574-ab52-90622ab3b3de",
    "title": "MCP Backtest: WFV1 E1V H2_PFOI",
    "trades": 0,
    "net": 0,
    "net_pct": 0,
    "pf": null,
    "dd": 0,
    "gross_price": 0,
    "fees": 0,
    "funding": 0,
    "funding_events": 0,
    "proxy_events": 0,
    "turnover": 0,
    "holding_seconds": 0,
    "directions": {},
    "months": [],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H2_PFOI",
    "strategy": "ResearchV1_H2_PFOI_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/76d2e287-1535-4574-ab52-90622ab3b3de"
  },
  {
    "name": "s8",
    "session_id": "5a8a5b98-c60d-46c7-98a1-b256e8575cbf",
    "title": "MCP Backtest: WFV1 E1V H3_P",
    "trades": 176,
    "net": -2752.087250259274,
    "net_pct": -27.52087250259275,
    "pf": 0.841631680042399,
    "dd": -42.42260550738369,
    "gross_price": -1346.5654648707646,
    "fees": 1378.3360810466786,
    "funding": -27.18570434183193,
    "funding_events": 288,
    "proxy_events": 288,
    "turnover": 306.2969068992623,
    "holding_seconds": 9136200,
    "directions": {
      "long": {
        "trades": 81,
        "net": -3247.234010639363,
        "gross": -2529.8061230984254,
        "fees": 639.8049744717839,
        "funding": -77.62291306915412
      },
      "short": {
        "trades": 95,
        "net": 495.1467603800892,
        "gross": 1183.2406582276608,
        "fees": 738.5311065748949,
        "funding": 50.437208727322194
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -5.400191531206799,
        "end_equity": 9459.98084687932
      },
      {
        "month": "2022-02",
        "return_pct": 13.723038298586276,
        "end_equity": 10758.177641535494
      },
      {
        "month": "2022-03",
        "return_pct": -9.852853122053261,
        "end_equity": 9698.190199905428
      },
      {
        "month": "2022-04",
        "return_pct": -16.812800643173233,
        "end_equity": 8067.652815599565
      },
      {
        "month": "2022-05",
        "return_pct": -6.611432320863697,
        "end_equity": 7534.265409813945
      },
      {
        "month": "2022-06",
        "return_pct": -3.80067125987118,
        "end_equity": 7247.912749740731
      }
    ],
    "max_accounting_error": 4.547473508864641e-12,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/5a8a5b98-c60d-46c7-98a1-b256e8575cbf"
  },
  {
    "name": "s9",
    "session_id": "d79395ab-ab58-4bcc-b4b8-88a363e78bb0",
    "title": "MCP Backtest: WFV1 E1V H3_PF",
    "trades": 5,
    "net": 449.8503569528026,
    "net_pct": 4.498503569528026,
    "pf": 2.504353316149281,
    "dd": -2.0067961366048492,
    "gross_price": 498.2637397083196,
    "fees": 43.71111588777675,
    "funding": -4.7022668677401525,
    "funding_events": 10,
    "proxy_events": 10,
    "turnover": 9.713581308394835,
    "holding_seconds": 319320,
    "directions": {
      "long": {
        "trades": 5,
        "net": 449.8503569528026,
        "gross": 498.2637397083196,
        "fees": 43.71111588777675,
        "funding": -4.7022668677401525
      }
    },
    "months": [
      {
        "month": "2022-01",
        "return_pct": -2.0067961366048492,
        "end_equity": 9799.320386339516
      },
      {
        "month": "2022-02",
        "return_pct": 5.942142914587922,
        "end_equity": 10381.610008354159
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 10381.610008354159
      },
      {
        "month": "2022-04",
        "return_pct": 0.6573195154097267,
        "end_equity": 10449.8503569528
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 10449.8503569528
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 10449.8503569528
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E1V",
    "dashboard_url": "http://localhost:9200/#/backtest/d79395ab-ab58-4bcc-b4b8-88a363e78bb0"
  }
]
```
