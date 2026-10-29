# Walk-forward E3V — diagnostic ablations

Prior train selection: **SIN_CANDIDATA**. Evaluation does not change selection.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 85 | 20.32 | 1.253 | -17.38 | [dashboard](http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382) |
| H1_PF | 82 | 19.80 | 1.256 | -17.38 | [dashboard](http://localhost:9200/#/backtest/75a05170-6a21-461d-ae17-a87c8d7cca30) |
| H1_PFOI | 54 | 7.30 | 1.151 | -15.29 | [dashboard](http://localhost:9200/#/backtest/0910f976-03e3-4d8f-a9f3-1f654b41f853) |
| H1_POI | 56 | 11.94 | 1.242 | -12.37 | [dashboard](http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0) |
| H2_P | 30 | -7.44 | 0.667 | -13.08 | [dashboard](http://localhost:9200/#/backtest/201fc419-1e0c-4245-baa2-79a5bf7df80a) |
| H2_PF | 0 | 0.00 | — | 0.00 | [dashboard](http://localhost:9200/#/backtest/9e719e69-81e6-43b5-b814-5bc0d02e1ee2) |
| H2_PFOI | 0 | 0.00 | — | 0.00 | [dashboard](http://localhost:9200/#/backtest/6b6cbe4e-c30e-4c77-a34f-d93dc6cfe833) |
| H2_POI | 12 | 0.48 | 1.072 | -6.10 | [dashboard](http://localhost:9200/#/backtest/ba6a2f8a-6bff-4c29-b4d4-83fe3808b578) |
| H3_P | 168 | -1.32 | 0.991 | -18.38 | [dashboard](http://localhost:9200/#/backtest/8bf944d4-de4b-450a-ba9d-2aee9399d84e) |
| H3_PF | 6 | -7.43 | 0.095 | -7.43 | [dashboard](http://localhost:9200/#/backtest/c7abf3e9-0f5f-4c07-b4b4-20249105fcd6) |
| H3_PFOI | 2 | -3.96 | 0.000 | -3.96 | [dashboard](http://localhost:9200/#/backtest/c6f6d185-d860-49b3-ab78-0fdd630f5dd3) |
| H3_POI | 117 | 40.19 | 1.430 | -11.26 | [dashboard](http://localhost:9200/#/backtest/fec06767-c58f-4c48-889d-96fb2840bad4) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "853089c6-86ed-4e36-a30e-833b61c5b382",
    "title": "MCP Backtest: WFV1 E3V H1_P",
    "trades": 85,
    "net": 2032.481024938302,
    "net_pct": 20.32481024938302,
    "pf": 1.2531034261743548,
    "dd": -17.382653180633735,
    "gross_price": 2906.950078796026,
    "fees": 849.7949004014007,
    "funding": -24.674153456325346,
    "funding_events": 178,
    "proxy_events": 178,
    "turnover": 188.84331120031126,
    "holding_seconds": 5162220,
    "directions": {
      "long": {
        "trades": 53,
        "net": 2081.6359731894822,
        "gross": 2688.966083522441,
        "fees": 530.2473724835164,
        "funding": -77.08273784944384
      },
      "short": {
        "trades": 32,
        "net": -49.15494825117986,
        "gross": 217.98399527358592,
        "fees": 319.5475279178843,
        "funding": 52.40858439311851
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 9.449646086723341,
        "end_equity": 10944.964608672333
      },
      {
        "month": "2023-02",
        "return_pct": 3.9444860589090025,
        "end_equity": 11376.687211813938
      },
      {
        "month": "2023-03",
        "return_pct": 11.682278607557306,
        "end_equity": 12705.743508208387
      },
      {
        "month": "2023-04",
        "return_pct": -4.7161525903056,
        "end_equity": 12106.521256628432
      },
      {
        "month": "2023-05",
        "return_pct": -7.779433224234533,
        "end_equity": 11164.702519691264
      },
      {
        "month": "2023-06",
        "return_pct": 7.772517930652723,
        "end_equity": 12032.481024938303
      }
    ],
    "max_accounting_error": 3.552713678800501e-15,
    "eligible": true,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382"
  },
  {
    "name": "s1",
    "session_id": "75a05170-6a21-461d-ae17-a87c8d7cca30",
    "title": "MCP Backtest: WFV1 E3V H1_PF",
    "trades": 82,
    "net": 1979.9368810159024,
    "net_pct": 19.79936881015903,
    "pf": 1.2558827801228285,
    "dd": -17.38265320849468,
    "gross_price": 2830.7844512757515,
    "fees": 818.9612899040997,
    "funding": -31.886280355747587,
    "funding_events": 168,
    "proxy_events": 168,
    "turnover": 181.99139775646657,
    "holding_seconds": 4882620,
    "directions": {
      "long": {
        "trades": 53,
        "net": 2087.665060273547,
        "gross": 2693.4791106817274,
        "fees": 528.8370245223417,
        "funding": -76.97702588583755
      },
      "short": {
        "trades": 29,
        "net": -107.72817925764402,
        "gross": 137.30534059402402,
        "fees": 290.124265381758,
        "funding": 45.09074553008997
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 11.661782645725015,
        "end_equity": 11166.178264572502
      },
      {
        "month": "2023-02",
        "return_pct": 1.4410475414111446,
        "end_equity": 11327.088201923709
      },
      {
        "month": "2023-03",
        "return_pct": 11.6814763370942,
        "end_equity": 12650.259329913215
      },
      {
        "month": "2023-04",
        "return_pct": -4.716152602917301,
        "end_equity": 12053.653795249724
      },
      {
        "month": "2023-05",
        "return_pct": -7.779433213223297,
        "end_equity": 11115.947848495116
      },
      {
        "month": "2023-06",
        "return_pct": 7.772517866191175,
        "end_equity": 11979.936881015892
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": true,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/75a05170-6a21-461d-ae17-a87c8d7cca30"
  },
  {
    "name": "s2",
    "session_id": "22f19971-2e43-4987-b915-8a8504dea4f0",
    "title": "MCP Backtest: WFV1 E3V H1_POI",
    "trades": 56,
    "net": 1194.0916093886894,
    "net_pct": 11.940916093886893,
    "pf": 1.2415890733982684,
    "dd": -12.372376759584524,
    "gross_price": 1738.1443686302882,
    "fees": 525.418230623422,
    "funding": -18.634528618176727,
    "funding_events": 118,
    "proxy_events": 118,
    "turnover": 116.7596068052049,
    "holding_seconds": 3424020,
    "directions": {
      "long": {
        "trades": 37,
        "net": 842.0944487560015,
        "gross": 1240.4298663757415,
        "fees": 349.58841248109945,
        "funding": -48.74700513864054
      },
      "short": {
        "trades": 19,
        "net": 351.9971606326877,
        "gross": 497.71450225454646,
        "fees": 175.8298181423226,
        "funding": 30.112476520463808
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 4.873606028766941,
        "end_equity": 10487.360602876694
      },
      {
        "month": "2023-02",
        "return_pct": 6.260203758903482,
        "end_equity": 11143.890745547744
      },
      {
        "month": "2023-03",
        "return_pct": 2.2460094900739858,
        "end_equity": 11394.183589256223
      },
      {
        "month": "2023-04",
        "return_pct": -3.781988741401421,
        "end_equity": 10963.256848735944
      },
      {
        "month": "2023-05",
        "return_pct": -3.342819066822933,
        "end_equity": 10596.775008451628
      },
      {
        "month": "2023-06",
        "return_pct": 5.636777231380941,
        "end_equity": 11194.091609388695
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": true,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0"
  },
  {
    "name": "s3",
    "session_id": "0910f976-03e3-4d8f-a9f3-1f654b41f853",
    "title": "MCP Backtest: WFV1 E3V H1_PFOI",
    "trades": 54,
    "net": 729.9922355593997,
    "net_pct": 7.299922355594002,
    "pf": 1.150569367900105,
    "dd": -15.287561311665554,
    "gross_price": 1251.5120732335672,
    "fees": 498.4047585667698,
    "funding": -23.115079107398056,
    "funding_events": 112,
    "proxy_events": 112,
    "turnover": 110.75661301483765,
    "holding_seconds": 3267660,
    "directions": {
      "long": {
        "trades": 37,
        "net": 853.22831306378,
        "gross": 1244.6907738781488,
        "fees": 343.5620763852757,
        "funding": -47.900384429093506
      },
      "short": {
        "trades": 17,
        "net": -123.23607750438045,
        "gross": 6.821299355417871,
        "fees": 154.84268218149384,
        "funding": 24.78530532169546
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 6.9932541636599455,
        "end_equity": 10699.325416365995
      },
      {
        "month": "2023-02",
        "return_pct": 3.2725375521203803,
        "end_equity": 11049.464858440133
      },
      {
        "month": "2023-03",
        "return_pct": 2.2460094618452553,
        "end_equity": 11297.636884643965
      },
      {
        "month": "2023-04",
        "return_pct": -3.781988755263088,
        "end_equity": 10870.361528056275
      },
      {
        "month": "2023-05",
        "return_pct": -6.558397816604044,
        "end_equity": 10157.439974943267
      },
      {
        "month": "2023-06",
        "return_pct": 5.636777200047671,
        "end_equity": 10729.992235559397
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/0910f976-03e3-4d8f-a9f3-1f654b41f853"
  },
  {
    "name": "s4",
    "session_id": "201fc419-1e0c-4245-baa2-79a5bf7df80a",
    "title": "MCP Backtest: WFV1 E3V H2_P",
    "trades": 30,
    "net": -743.8794220613149,
    "net_pct": -7.438794220613149,
    "pf": 0.6665617701124303,
    "dd": -13.078318641014764,
    "gross_price": -510.12001644802626,
    "fees": 240.43802539618247,
    "funding": 6.678619782893367,
    "funding_events": 66,
    "proxy_events": 66,
    "turnover": 53.43067231026276,
    "holding_seconds": 1974660,
    "directions": {
      "long": {
        "trades": 10,
        "net": -394.5374093256469,
        "gross": -301.71455666320713,
        "fees": 80.66666400665254,
        "funding": -12.156188655787057
      },
      "short": {
        "trades": 20,
        "net": -349.34201273566794,
        "gross": -208.40545978481876,
        "fees": 159.77136138952986,
        "funding": 18.834808438680426
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": -3.9392586491302617,
        "end_equity": 9606.074135086974
      },
      {
        "month": "2023-02",
        "return_pct": -6.430431708774509,
        "end_equity": 8988.362097935955
      },
      {
        "month": "2023-03",
        "return_pct": 0.5507270722897584,
        "end_equity": 9037.86344136472
      },
      {
        "month": "2023-04",
        "return_pct": -0.05971816642882377,
        "end_equity": 9032.466195033196
      },
      {
        "month": "2023-05",
        "return_pct": 5.091656116559018,
        "end_equity": 9492.368312528728
      },
      {
        "month": "2023-06",
        "return_pct": -2.4888176144432506,
        "end_equity": 9256.120577938684
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/201fc419-1e0c-4245-baa2-79a5bf7df80a"
  },
  {
    "name": "s5",
    "session_id": "9e719e69-81e6-43b5-b814-5bc0d02e1ee2",
    "title": "MCP Backtest: WFV1 E3V H2_PF",
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
    "strategy": "ResearchV1_H2_PF_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/9e719e69-81e6-43b5-b814-5bc0d02e1ee2"
  },
  {
    "name": "s10",
    "session_id": "fec06767-c58f-4c48-889d-96fb2840bad4",
    "title": "MCP Backtest: WFV1 E3V H3_POI",
    "trades": 117,
    "net": 4018.7012469797005,
    "net_pct": 40.18701246979701,
    "pf": 1.4296408262019105,
    "dd": -11.263812678837738,
    "gross_price": 5231.914857678969,
    "fees": 1172.1317034632482,
    "funding": -41.0819072360218,
    "funding_events": 267,
    "proxy_events": 267,
    "turnover": 260.47371188072174,
    "holding_seconds": 8041680,
    "directions": {
      "long": {
        "trades": 68,
        "net": 3117.2983367616953,
        "gross": 3916.8999222257867,
        "fees": 680.1368928749569,
        "funding": -119.46469258913443
      },
      "short": {
        "trades": 49,
        "net": 901.4029102180048,
        "gross": 1315.0149354531832,
        "fees": 491.99481058829167,
        "funding": 78.38278535311264
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 3.8525755642039528,
        "end_equity": 10385.257556420396
      },
      {
        "month": "2023-02",
        "return_pct": 3.825611756387426,
        "end_equity": 10782.557190429929
      },
      {
        "month": "2023-03",
        "return_pct": 11.493285082253157,
        "end_equity": 12021.827227483027
      },
      {
        "month": "2023-04",
        "return_pct": -0.5060103558985118,
        "end_equity": 11960.995536743736
      },
      {
        "month": "2023-05",
        "return_pct": 0.5408049692068762,
        "end_equity": 12025.68119497306
      },
      {
        "month": "2023-06",
        "return_pct": 16.57303249349178,
        "end_equity": 14018.701246979675
      }
    ],
    "max_accounting_error": 2.546585164964199e-11,
    "eligible": true,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/fec06767-c58f-4c48-889d-96fb2840bad4"
  },
  {
    "name": "s11",
    "session_id": "c6f6d185-d860-49b3-ab78-0fdd630f5dd3",
    "title": "MCP Backtest: WFV1 E3V H3_PFOI",
    "trades": 2,
    "net": -396.3841677073916,
    "net_pct": -3.9638416770739164,
    "pf": 0,
    "dd": -3.963841677073887,
    "gross_price": -378.93337021536126,
    "fees": 17.050198668913367,
    "funding": -0.4005988231169505,
    "funding_events": 2,
    "proxy_events": 2,
    "turnover": 3.788933037536304,
    "holding_seconds": 40860,
    "directions": {
      "long": {
        "trades": 1,
        "net": -200.82127064417128,
        "gross": -191.4700081941604,
        "fees": 8.529988865049827,
        "funding": -0.8212735849610201
      },
      "short": {
        "trades": 1,
        "net": -195.5628970632203,
        "gross": -187.46336202120085,
        "fees": 8.520209803863539,
        "funding": 0.4206747618440696
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2023-02",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2023-03",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2023-04",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2023-05",
        "return_pct": -3.963841677073887,
        "end_equity": 9603.615832292611
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 9603.615832292611
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/c6f6d185-d860-49b3-ab78-0fdd630f5dd3"
  },
  {
    "name": "s6",
    "session_id": "ba6a2f8a-6bff-4c29-b4d4-83fe3808b578",
    "title": "MCP Backtest: WFV1 E3V H2_POI",
    "trades": 12,
    "net": 48.069784287469204,
    "net_pct": 0.4806978428746921,
    "pf": 1.071555118583118,
    "dd": -6.095157774423421,
    "gross_price": 149.7925012729737,
    "fees": 100.55087519937047,
    "funding": -1.1718417861341142,
    "funding_events": 31,
    "proxy_events": 31,
    "turnover": 22.34463893319344,
    "holding_seconds": 913020,
    "directions": {
      "short": {
        "trades": 8,
        "net": 272.31571278485023,
        "gross": 332.6156500612956,
        "fees": 66.87225881849281,
        "funding": 6.57232154204749
      },
      "long": {
        "trades": 4,
        "net": -224.24592849738107,
        "gross": -182.8231487883218,
        "fees": 33.678616380877656,
        "funding": -7.744163328181604
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": -2.443571506669684,
        "end_equity": 9755.642849333031
      },
      {
        "month": "2023-02",
        "return_pct": -2.5912128006295054,
        "end_equity": 9502.853383037416
      },
      {
        "month": "2023-03",
        "return_pct": 1.7412021529671362,
        "end_equity": 9668.317270736174
      },
      {
        "month": "2023-04",
        "return_pct": -0.002530834137881577,
        "end_equity": 9668.072581662127
      },
      {
        "month": "2023-05",
        "return_pct": 4.126800332070024,
        "end_equity": 10067.054633066931
      },
      {
        "month": "2023-06",
        "return_pct": -0.1885839450706861,
        "end_equity": 10048.069784287472
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/ba6a2f8a-6bff-4c29-b4d4-83fe3808b578"
  },
  {
    "name": "s7",
    "session_id": "6b6cbe4e-c30e-4c77-a34f-d93dc6cfe833",
    "title": "MCP Backtest: WFV1 E3V H2_PFOI",
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
    "strategy": "ResearchV1_H2_PFOI_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/6b6cbe4e-c30e-4c77-a34f-d93dc6cfe833"
  },
  {
    "name": "s8",
    "session_id": "8bf944d4-de4b-450a-ba9d-2aee9399d84e",
    "title": "MCP Backtest: WFV1 E3V H3_P",
    "trades": 168,
    "net": -131.7491559567097,
    "net_pct": -1.3174915595671035,
    "pf": 0.9905424565471671,
    "dd": -18.381901925307954,
    "gross_price": 1423.8977327199118,
    "fees": 1496.9126881493773,
    "funding": -58.73420052724393,
    "funding_events": 371,
    "proxy_events": 371,
    "turnover": 332.6472640331951,
    "holding_seconds": 11274360,
    "directions": {
      "short": {
        "trades": 74,
        "net": -1914.1018183326623,
        "gross": -1346.482520869123,
        "fees": 657.5392474455991,
        "funding": 89.91994998206101
      },
      "long": {
        "trades": 94,
        "net": 1782.3526623759521,
        "gross": 2770.3802535890377,
        "fees": 839.3734407037776,
        "funding": -148.65415050930494
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 4.762203778100482,
        "end_equity": 10476.220377810048
      },
      {
        "month": "2023-02",
        "return_pct": -5.3015411172681155,
        "end_equity": 9920.819246944828
      },
      {
        "month": "2023-03",
        "return_pct": 3.3219812305869567,
        "end_equity": 10250.387000248793
      },
      {
        "month": "2023-04",
        "return_pct": 5.797698292436992,
        "end_equity": 10844.6735123304
      },
      {
        "month": "2023-05",
        "return_pct": -7.826580351004786,
        "end_equity": 9995.90642608373
      },
      {
        "month": "2023-06",
        "return_pct": -1.2770786019698388,
        "end_equity": 9868.250844043287
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/8bf944d4-de4b-450a-ba9d-2aee9399d84e"
  },
  {
    "name": "s9",
    "session_id": "c7abf3e9-0f5f-4c07-b4b4-20249105fcd6",
    "title": "MCP Backtest: WFV1 E3V H3_PF",
    "trades": 6,
    "net": -743.2028478859625,
    "net_pct": -7.432028478859625,
    "pf": 0.09539151124516712,
    "dd": -7.432028478859676,
    "gross_price": -693.7599203116627,
    "fees": 50.06292349502956,
    "funding": 0.6199959207297139,
    "funding_events": 9,
    "proxy_events": 9,
    "turnover": 11.12509411000657,
    "holding_seconds": 258060,
    "directions": {
      "short": {
        "trades": 4,
        "net": -627.1123378635135,
        "gross": -595.9660416866827,
        "fees": 33.4878650568057,
        "funding": 2.3415688799748082
      },
      "long": {
        "trades": 2,
        "net": -116.09051002244885,
        "gross": -97.7938786249799,
        "fees": 16.575058438223856,
        "funding": -1.7215729592450941
      }
    },
    "months": [
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2023-02",
        "return_pct": -1.9999999518284128,
        "end_equity": 9800.000004817159
      },
      {
        "month": "2023-03",
        "return_pct": -1.990299000493767,
        "end_equity": 9604.950702672893
      },
      {
        "month": "2023-04",
        "return_pct": 0.8159457700730455,
        "end_equity": 9683.321891648953
      },
      {
        "month": "2023-05",
        "return_pct": -4.404735733330945,
        "end_equity": 9256.797152114033
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 9256.797152114033
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E3V",
    "dashboard_url": "http://localhost:9200/#/backtest/c7abf3e9-0f5f-4c07-b4b4-20249105fcd6"
  }
]
```
