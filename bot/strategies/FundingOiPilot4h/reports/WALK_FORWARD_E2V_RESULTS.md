# Walk-forward E2V — diagnostic ablations

Prior train selection: **SIN_CANDIDATA**. Evaluation does not change selection.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 96 | -10.94 | 0.865 | -29.11 | [dashboard](http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7) |
| H1_PF | 95 | -14.15 | 0.825 | -29.11 | [dashboard](http://localhost:9200/#/backtest/a5d0a2ec-2c93-438a-b8e1-c4904c9effc8) |
| H1_PFOI | 63 | -8.93 | 0.843 | -14.33 | [dashboard](http://localhost:9200/#/backtest/90be152d-6530-4e40-9bac-8067ccd169db) |
| H1_POI | 64 | -5.52 | 0.904 | -14.33 | [dashboard](http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f) |
| H2_P | 37 | -14.40 | 0.551 | -18.54 | [dashboard](http://localhost:9200/#/backtest/5a46a1f1-df6e-41ba-a8de-495e07a1421a) |
| H2_PF | 0 | 0.00 | — | 0.00 | [dashboard](http://localhost:9200/#/backtest/cce04e8d-ad70-4052-86c4-517d366d6edd) |
| H2_PFOI | 0 | 0.00 | — | 0.00 | [dashboard](http://localhost:9200/#/backtest/21c23ca0-a816-4416-b0bc-c5b67c0f6772) |
| H2_POI | 25 | -10.74 | 0.510 | -14.05 | [dashboard](http://localhost:9200/#/backtest/bb3ade90-a481-4f9e-beeb-4f715d9a32e4) |
| H3_P | 170 | -11.62 | 0.904 | -26.66 | [dashboard](http://localhost:9200/#/backtest/0a64060d-6f97-4f56-bdd0-323aace59405) |
| H3_PF | 6 | -3.89 | 0.433 | -5.53 | [dashboard](http://localhost:9200/#/backtest/ebc60c54-a190-465a-9584-5702df136796) |
| H3_PFOI | 4 | -3.51 | 0.272 | -4.91 | [dashboard](http://localhost:9200/#/backtest/2ee58971-a2f6-4249-9e8a-454006769816) |
| H3_POI | 125 | -17.31 | 0.838 | -28.43 | [dashboard](http://localhost:9200/#/backtest/241076dd-c905-4237-a1aa-3ddf2a405fa8) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "5ba6d867-c4ca-477a-bd8f-25353a8a9eb7",
    "title": "MCP Backtest: WFV1 E2V H1_P",
    "trades": 96,
    "net": -1093.9841102975547,
    "net_pct": -10.939841102975542,
    "pf": 0.8651657875469272,
    "dd": -29.107236699108483,
    "gross_price": -355.8911986907274,
    "fees": 733.9789696879255,
    "funding": -4.113941918900645,
    "funding_events": 186,
    "proxy_events": 186,
    "turnover": 163.10643770842796,
    "holding_seconds": 5591880,
    "directions": {
      "long": {
        "trades": 47,
        "net": -1532.6466878465344,
        "gross": -1129.209835653721,
        "fees": 364.3799010648157,
        "funding": -39.056951127997884
      },
      "short": {
        "trades": 49,
        "net": 438.66257754898027,
        "gross": 773.3186369629931,
        "fees": 369.59906862310993,
        "funding": 34.943009209097255
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": 1.7068147867647987,
        "end_equity": 10170.681478676479
      },
      {
        "month": "2022-08",
        "return_pct": -18.50292947428742,
        "end_equity": 8288.807457622557
      },
      {
        "month": "2022-09",
        "return_pct": -8.823108568943884,
        "end_equity": 7557.476976565802
      },
      {
        "month": "2022-10",
        "return_pct": 4.9321698985779205,
        "end_equity": 7930.2245810959375
      },
      {
        "month": "2022-11",
        "return_pct": 17.324486250346062,
        "end_equity": 9304.095248269467
      },
      {
        "month": "2022-12",
        "return_pct": -4.278539158775829,
        "end_equity": 8906.015889702456
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7"
  },
  {
    "name": "s1",
    "session_id": "a5d0a2ec-2c93-438a-b8e1-c4904c9effc8",
    "title": "MCP Backtest: WFV1 E2V H1_PF",
    "trades": 95,
    "net": -1415.2046549890206,
    "net_pct": -14.152046549890196,
    "pf": 0.8245225395864223,
    "dd": -29.107236699108483,
    "gross_price": -690.4237225024292,
    "fees": 720.6278619082802,
    "funding": -4.153070578310087,
    "funding_events": 186,
    "proxy_events": 186,
    "turnover": 160.1395248685067,
    "holding_seconds": 5588820,
    "directions": {
      "long": {
        "trades": 47,
        "net": -1534.6129741155246,
        "gross": -1134.0240477086008,
        "fees": 361.87265012843767,
        "funding": -38.71627627848656
      },
      "short": {
        "trades": 48,
        "net": 119.40831912650515,
        "gross": 443.6003252061716,
        "fees": 358.75521177984257,
        "funding": 34.563205700176475
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": 1.7068147867647987,
        "end_equity": 10170.681478676479
      },
      {
        "month": "2022-08",
        "return_pct": -18.50292947428742,
        "end_equity": 8288.807457622557
      },
      {
        "month": "2022-09",
        "return_pct": -8.823108568943884,
        "end_equity": 7557.476976565802
      },
      {
        "month": "2022-10",
        "return_pct": 4.9321698985779205,
        "end_equity": 7930.2245810959375
      },
      {
        "month": "2022-11",
        "return_pct": 13.092848178665562,
        "end_equity": 8968.516845726046
      },
      {
        "month": "2022-12",
        "return_pct": -4.27853910870355,
        "end_equity": 8584.79534501099
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/a5d0a2ec-2c93-438a-b8e1-c4904c9effc8"
  },
  {
    "name": "s2",
    "session_id": "2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f",
    "title": "MCP Backtest: WFV1 E2V H1_POI",
    "trades": 64,
    "net": -552.0058976105167,
    "net_pct": -5.520058976105165,
    "pf": 0.9036396345613238,
    "dd": -14.333539345113444,
    "gross_price": -5.004771831123449,
    "fees": 529.9317111936653,
    "funding": -17.06941458572778,
    "funding_events": 123,
    "proxy_events": 123,
    "turnover": 117.76260248748127,
    "holding_seconds": 3815160,
    "directions": {
      "long": {
        "trades": 39,
        "net": -587.7311210078211,
        "gross": -225.51362980342384,
        "fees": 324.7800669358247,
        "funding": -37.437424268572144
      },
      "short": {
        "trades": 25,
        "net": 35.72522339730389,
        "gross": 220.50885797230043,
        "fees": 205.1516442578407,
        "funding": 20.368009682844367
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -0.9229063319362241,
        "end_equity": 9907.709366806377
      },
      {
        "month": "2022-08",
        "return_pct": -5.572871290295389,
        "end_equity": 9355.565475977717
      },
      {
        "month": "2022-09",
        "return_pct": -4.195300308271454,
        "end_equity": 8963.071408723486
      },
      {
        "month": "2022-10",
        "return_pct": 7.088547699268499,
        "end_equity": 9598.423000850347
      },
      {
        "month": "2022-11",
        "return_pct": 2.750766046738695,
        "end_equity": 9862.453161780097
      },
      {
        "month": "2022-12",
        "return_pct": -4.202393183440023,
        "end_equity": 9447.994102389484
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f"
  },
  {
    "name": "s3",
    "session_id": "90be152d-6530-4e40-9bac-8067ccd169db",
    "title": "MCP Backtest: WFV1 E2V H1_PFOI",
    "trades": 63,
    "net": -892.7744079594493,
    "net_pct": -8.927744079594492,
    "pf": 0.8428313543322111,
    "dd": -14.333539345113444,
    "gross_price": -358.3006618138445,
    "fees": 517.3780277859541,
    "funding": -17.09571835965065,
    "funding_events": 123,
    "proxy_events": 123,
    "turnover": 114.97289506354537,
    "holding_seconds": 3812100,
    "directions": {
      "long": {
        "trades": 39,
        "net": -587.0547569490003,
        "gross": -226.87766854694382,
        "fees": 322.97446434364787,
        "funding": -37.20262405840841
      },
      "short": {
        "trades": 24,
        "net": -305.7196510104493,
        "gross": -131.4229932669006,
        "fees": 194.4035634423064,
        "funding": 20.10690569875775
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -0.9229063319362241,
        "end_equity": 9907.709366806377
      },
      {
        "month": "2022-08",
        "return_pct": -5.572871290295389,
        "end_equity": 9355.565475977717
      },
      {
        "month": "2022-09",
        "return_pct": -4.195300308271454,
        "end_equity": 8963.071408723486
      },
      {
        "month": "2022-10",
        "return_pct": 7.088547699268499,
        "end_equity": 9598.423000850347
      },
      {
        "month": "2022-11",
        "return_pct": -0.9552296793592929,
        "end_equity": 9506.736015595776
      },
      {
        "month": "2022-12",
        "return_pct": -4.202393154704465,
        "end_equity": 9107.225592040555
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/90be152d-6530-4e40-9bac-8067ccd169db"
  },
  {
    "name": "s4",
    "session_id": "5a46a1f1-df6e-41ba-a8de-495e07a1421a",
    "title": "MCP Backtest: WFV1 E2V H2_P",
    "trades": 37,
    "net": -1440.0637210989898,
    "net_pct": -14.4006372109899,
    "pf": 0.5512372068183057,
    "dd": -18.538110942348986,
    "gross_price": -1159.574782513465,
    "fees": 288.1459750054447,
    "funding": 7.657036419919582,
    "funding_events": 69,
    "proxy_events": 69,
    "turnover": 64.03243889009885,
    "holding_seconds": 2184180,
    "directions": {
      "short": {
        "trades": 20,
        "net": -470.8621029568947,
        "gross": -331.9313571248613,
        "fees": 157.5005499913612,
        "funding": 18.569804159327806
      },
      "long": {
        "trades": 17,
        "net": -969.2016181420954,
        "gross": -827.6434253886038,
        "fees": 130.64542501408354,
        "funding": -10.912767739408224
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -3.8266195125471136,
        "end_equity": 9617.338048745289
      },
      {
        "month": "2022-08",
        "return_pct": -10.348043220561632,
        "end_equity": 8622.131750793607
      },
      {
        "month": "2022-09",
        "return_pct": -4.392456162670255,
        "end_equity": 8243.408393352325
      },
      {
        "month": "2022-10",
        "return_pct": 8.294875909871058,
        "end_equity": 8927.188890324796
      },
      {
        "month": "2022-11",
        "return_pct": -4.677685227898609,
        "end_equity": 8509.603094335467
      },
      {
        "month": "2022-12",
        "return_pct": 0.5914868649872451,
        "end_equity": 8559.93627890101
      }
    ],
    "max_accounting_error": 2.2737367544323206e-13,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/5a46a1f1-df6e-41ba-a8de-495e07a1421a"
  },
  {
    "name": "s5",
    "session_id": "cce04e8d-ad70-4052-86c4-517d366d6edd",
    "title": "MCP Backtest: WFV1 E2V H2_PF",
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
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/cce04e8d-ad70-4052-86c4-517d366d6edd"
  },
  {
    "name": "s10",
    "session_id": "241076dd-c905-4237-a1aa-3ddf2a405fa8",
    "title": "MCP Backtest: WFV1 E2V H3_POI",
    "trades": 125,
    "net": -1731.4688722987057,
    "net_pct": -17.31468872298707,
    "pf": 0.8383203268569924,
    "dd": -28.434956321970827,
    "gross_price": -766.0658194245244,
    "fees": 962.1041702201791,
    "funding": -3.2988826540025693,
    "funding_events": 238,
    "proxy_events": 238,
    "turnover": 213.80092671559538,
    "holding_seconds": 7432920,
    "directions": {
      "short": {
        "trades": 65,
        "net": -1931.3961006644593,
        "gross": -1475.8116741570975,
        "fees": 499.77269961550877,
        "funding": 44.18827310814671
      },
      "long": {
        "trades": 60,
        "net": 199.92722836575265,
        "gross": 709.7458547325726,
        "fees": 462.33147060467036,
        "funding": -47.48715576214929
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -1.8372049899915144,
        "end_equity": 9816.279501000849
      },
      {
        "month": "2022-08",
        "return_pct": -12.628213627973006,
        "end_equity": 8576.658755295539
      },
      {
        "month": "2022-09",
        "return_pct": -3.0642510850821036,
        "end_equity": 8313.848396322606
      },
      {
        "month": "2022-10",
        "return_pct": 1.5032404056188442,
        "end_equity": 8438.825524678023
      },
      {
        "month": "2022-11",
        "return_pct": -4.960959337588211,
        "end_equity": 8020.178821828731
      },
      {
        "month": "2022-12",
        "return_pct": 3.0965931232930677,
        "end_equity": 8268.531127701286
      }
    ],
    "max_accounting_error": 9.094947017729282e-12,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/241076dd-c905-4237-a1aa-3ddf2a405fa8"
  },
  {
    "name": "s11",
    "session_id": "2ee58971-a2f6-4249-9e8a-454006769816",
    "title": "MCP Backtest: WFV1 E2V H3_PFOI",
    "trades": 4,
    "net": -351.25500090734806,
    "net_pct": -3.5125500090734807,
    "pf": 0.2716732625850586,
    "dd": -4.9071098577300525,
    "gross_price": -321.18243644465656,
    "fees": 33.48687273491231,
    "funding": 3.4143082722207896,
    "funding_events": 9,
    "proxy_events": 9,
    "turnover": 7.441527274424958,
    "holding_seconds": 294420,
    "directions": {
      "long": {
        "trades": 1,
        "net": -199.7836275132457,
        "gross": -191.4700101935383,
        "fees": 8.529988954122206,
        "funding": 0.21637163441478663
      },
      "short": {
        "trades": 3,
        "net": -151.47137339410236,
        "gross": -129.71242625111827,
        "fees": 24.956883780790104,
        "funding": 3.197936637806003
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2022-08",
        "return_pct": -1.9978362751324807,
        "end_equity": 9800.216372486751
      },
      {
        "month": "2022-09",
        "return_pct": -2.8825185260528463,
        "end_equity": 9517.723319956556
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 9517.723319956556
      },
      {
        "month": "2022-11",
        "return_pct": 1.3766073537919254,
        "end_equity": 9648.744999092647
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 9648.744999092647
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/2ee58971-a2f6-4249-9e8a-454006769816"
  },
  {
    "name": "s6",
    "session_id": "bb3ade90-a481-4f9e-beeb-4f715d9a32e4",
    "title": "MCP Backtest: WFV1 E2V H2_POI",
    "trades": 25,
    "net": -1073.6287868147442,
    "net_pct": -10.736287868147443,
    "pf": 0.509679870785506,
    "dd": -14.048791230074142,
    "gross_price": -877.4966499443434,
    "fees": 199.3365015172324,
    "funding": 3.2043646468315505,
    "funding_events": 46,
    "proxy_events": 46,
    "turnover": 44.297000337162764,
    "holding_seconds": 1462860,
    "directions": {
      "short": {
        "trades": 14,
        "net": -741.318455186069,
        "gross": -639.8500983209398,
        "fees": 112.60742009114561,
        "funding": 11.139063226016466
      },
      "long": {
        "trades": 11,
        "net": -332.3103316286754,
        "gross": -237.64655162340367,
        "fees": 86.72908142608676,
        "funding": -7.934698579184918
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -5.412014603924886,
        "end_equity": 9458.798539607511
      },
      {
        "month": "2022-08",
        "return_pct": -5.75801349802183,
        "end_equity": 8914.159642946219
      },
      {
        "month": "2022-09",
        "return_pct": -2.428289068821987,
        "end_equity": 8697.698078759215
      },
      {
        "month": "2022-10",
        "return_pct": 5.373010259862521,
        "end_equity": 9165.026288902813
      },
      {
        "month": "2022-11",
        "return_pct": -2.91451374978845,
        "end_equity": 8897.910337541014
      },
      {
        "month": "2022-12",
        "return_pct": 0.3198602207100443,
        "end_equity": 8926.371213185255
      }
    ],
    "max_accounting_error": 4.440892098500626e-16,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/bb3ade90-a481-4f9e-beeb-4f715d9a32e4"
  },
  {
    "name": "s7",
    "session_id": "21c23ca0-a816-4416-b0bc-c5b67c0f6772",
    "title": "MCP Backtest: WFV1 E2V H2_PFOI",
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
    "strategy": "ResearchV1_H2_PFOI_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/21c23ca0-a816-4416-b0bc-c5b67c0f6772"
  },
  {
    "name": "s8",
    "session_id": "0a64060d-6f97-4f56-bdd0-323aace59405",
    "title": "MCP Backtest: WFV1 E2V H3_P",
    "trades": 170,
    "net": -1161.8360202611543,
    "net_pct": -11.618360202611536,
    "pf": 0.9037309362598267,
    "dd": -26.65936437399703,
    "gross_price": 113.60634955316584,
    "fees": 1271.113303929706,
    "funding": -4.329065884613038,
    "funding_events": 362,
    "proxy_events": 362,
    "turnover": 282.46962309549014,
    "holding_seconds": 10956300,
    "directions": {
      "short": {
        "trades": 91,
        "net": -150.9793931578892,
        "gross": 469.76300151346584,
        "fees": 685.0143951934416,
        "funding": 64.27200052208599
      },
      "long": {
        "trades": 79,
        "net": -1010.8566271032645,
        "gross": -356.1566519603006,
        "fees": 586.0989087362649,
        "funding": -68.60106640669902
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": -4.543584139414037,
        "end_equity": 9545.641586058597
      },
      {
        "month": "2022-08",
        "return_pct": -16.58396857700066,
        "end_equity": 7962.595384953531
      },
      {
        "month": "2022-09",
        "return_pct": -4.673897204250199,
        "end_equity": 7590.431861870432
      },
      {
        "month": "2022-10",
        "return_pct": 6.7081670721296005,
        "end_equity": 8099.610712660858
      },
      {
        "month": "2022-11",
        "return_pct": 14.35945595406254,
        "end_equity": 9262.670745395924
      },
      {
        "month": "2022-12",
        "return_pct": -4.5829845119787045,
        "end_equity": 8838.163979738847
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/0a64060d-6f97-4f56-bdd0-323aace59405"
  },
  {
    "name": "s9",
    "session_id": "ebc60c54-a190-465a-9584-5702df136796",
    "title": "MCP Backtest: WFV1 E2V H3_PF",
    "trades": 6,
    "net": -389.2077108846124,
    "net_pct": -3.8920771088461246,
    "pf": 0.4329079729484097,
    "dd": -5.526093017051825,
    "gross_price": -343.03134314848126,
    "fees": 51.09435894942555,
    "funding": 4.917991213294389,
    "funding_events": 12,
    "proxy_events": 12,
    "turnover": 11.354301988761232,
    "holding_seconds": 388020,
    "directions": {
      "long": {
        "trades": 3,
        "net": -235.25304670625948,
        "gross": -211.19235243108304,
        "fees": 25.72832037751241,
        "funding": 1.6676261023359422
      },
      "short": {
        "trades": 3,
        "net": -153.95466417835286,
        "gross": -131.8389907173982,
        "fees": 25.36603857191313,
        "funding": 3.2503651109584464
      }
    },
    "months": [
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2022-08",
        "return_pct": -0.39114430367579445,
        "end_equity": 9960.88556963242
      },
      {
        "month": "2022-09",
        "return_pct": -2.8825185482060256,
        "end_equity": 9673.76119552219
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 9673.76119552219
      },
      {
        "month": "2022-11",
        "return_pct": -0.6509247554709607,
        "end_equity": 9610.792289115392
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 9610.792289115392
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E2V",
    "dashboard_url": "http://localhost:9200/#/backtest/ebc60c54-a190-465a-9584-5702df136796"
  }
]
```
