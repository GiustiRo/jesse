# Walk-forward E2T — selection BEFORE evaluation

Selection: **SIN_CANDIDATA**. Frozen gates and ranking, based only on this train.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 377 | -36.44 | 0.903 | -53.73 | [dashboard](http://localhost:9200/#/backtest/8042b1d6-268a-4c60-9545-1147b44f9851) |
| H1_PF | 368 | -39.99 | 0.884 | -53.85 | [dashboard](http://localhost:9200/#/backtest/98a15e51-90f1-4b4d-a5a6-2ed42f6c36e0) |
| H1_PFOI | 266 | 1.15 | 1.004 | -35.46 | [dashboard](http://localhost:9200/#/backtest/2ecc415d-5070-405d-b941-e1329a9524e6) |
| H1_POI | 271 | 1.48 | 1.005 | -36.56 | [dashboard](http://localhost:9200/#/backtest/aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b) |
| H2_P | 142 | -22.55 | 0.823 | -33.99 | [dashboard](http://localhost:9200/#/backtest/58662d33-5a67-4db4-8b66-58172bfb052e) |
| H2_PF | 8 | -5.07 | 0.412 | -6.27 | [dashboard](http://localhost:9200/#/backtest/cdaa5c6b-6406-4049-9ac1-18b803045e2a) |
| H2_PFOI | 4 | -0.70 | 0.817 | -3.03 | [dashboard](http://localhost:9200/#/backtest/2e436b8e-0c9a-4a57-a3a0-6116aa5618e1) |
| H2_POI | 74 | 0.73 | 1.009 | -15.77 | [dashboard](http://localhost:9200/#/backtest/79742595-c37a-45f7-9f90-c913759abe87) |
| H3_P | 652 | -61.62 | 0.895 | -73.25 | [dashboard](http://localhost:9200/#/backtest/eef318bf-6b93-4de2-9cef-f8512d472011) |
| H3_PF | 45 | -15.67 | 0.684 | -26.08 | [dashboard](http://localhost:9200/#/backtest/2be7a6c4-381b-4353-a473-b6a29b3d6892) |
| H3_PFOI | 28 | -15.92 | 0.500 | -22.24 | [dashboard](http://localhost:9200/#/backtest/2e2b071a-f85f-42ba-9f5d-13107abd5723) |
| H3_POI | 490 | -44.42 | 0.888 | -54.66 | [dashboard](http://localhost:9200/#/backtest/0a4a627c-d324-4a0d-9697-e939375859cb) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "8042b1d6-268a-4c60-9545-1147b44f9851",
    "title": "MCP Backtest: WFV1 E2T H1_P",
    "trades": 377,
    "net": -3644.329450006557,
    "net_pct": -36.443294500065534,
    "pf": 0.9025648540405262,
    "dd": -53.72707108828833,
    "gross_price": -350.4505277904502,
    "fees": 2810.459651987178,
    "funding": -483.4192702289262,
    "funding_events": 553,
    "proxy_events": 553,
    "turnover": 624.5465893304831,
    "holding_seconds": 17097540,
    "directions": {
      "long": {
        "trades": 201,
        "net": -1342.734890366592,
        "gross": 863.7746397354103,
        "fees": 1556.0763440290693,
        "funding": -650.4331860729328
      },
      "short": {
        "trades": 176,
        "net": -2301.5945596399633,
        "gross": -1214.2251675258617,
        "fees": 1254.383307958107,
        "funding": 167.01391584400568
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -1.40572463394385,
        "end_equity": 9859.427536605615
      },
      {
        "month": "2020-10",
        "return_pct": 2.6580452469685545,
        "end_equity": 10121.49558162067
      },
      {
        "month": "2020-11",
        "return_pct": 19.503158593771563,
        "end_equity": 12095.506916965729
      },
      {
        "month": "2020-12",
        "return_pct": -3.7641856920571093,
        "end_equity": 11640.209576215528
      },
      {
        "month": "2021-01",
        "return_pct": 4.283990822103534,
        "end_equity": 12138.875086134218
      },
      {
        "month": "2021-02",
        "return_pct": -18.595399677378655,
        "end_equity": 9881.602747529818
      },
      {
        "month": "2021-03",
        "return_pct": 7.397018634385533,
        "end_equity": 10612.54674414055
      },
      {
        "month": "2021-04",
        "return_pct": -4.455932584937083,
        "end_equity": 10139.658815676712
      },
      {
        "month": "2021-05",
        "return_pct": -17.414879050648757,
        "end_equity": 8373.849496778168
      },
      {
        "month": "2021-06",
        "return_pct": 0.26548140195099545,
        "end_equity": 8396.080509819481
      },
      {
        "month": "2021-07",
        "return_pct": 2.380576783698718,
        "end_equity": 8595.955653176898
      },
      {
        "month": "2021-08",
        "return_pct": -10.893499086512593,
        "end_equity": 7659.555302621045
      },
      {
        "month": "2021-09",
        "return_pct": -3.424742602868225,
        "end_equity": 7397.2352489819295
      },
      {
        "month": "2021-10",
        "return_pct": 7.708505504468421,
        "end_equity": 7967.45153532818
      },
      {
        "month": "2021-11",
        "return_pct": 2.0421596096258154,
        "end_equity": 8130.159612499165
      },
      {
        "month": "2021-12",
        "return_pct": -12.218868928474535,
        "end_equity": 7136.7460657721185
      },
      {
        "month": "2022-01",
        "return_pct": -18.059284653604678,
        "end_equity": 5847.900778749398
      },
      {
        "month": "2022-02",
        "return_pct": 1.0674289224561262,
        "end_equity": 5910.322963018307
      },
      {
        "month": "2022-03",
        "return_pct": 6.06218483516987,
        "end_equity": 6268.617665391965
      },
      {
        "month": "2022-04",
        "return_pct": -6.0574711187165065,
        "end_equity": 5888.897960768086
      },
      {
        "month": "2022-05",
        "return_pct": 3.5959316613001446,
        "end_equity": 6100.658707041004
      },
      {
        "month": "2022-06",
        "return_pct": 4.18007063168655,
        "end_equity": 6355.670549993454
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/8042b1d6-268a-4c60-9545-1147b44f9851"
  },
  {
    "name": "s1",
    "session_id": "98a15e51-90f1-4b4d-a5a6-2ed42f6c36e0",
    "title": "MCP Backtest: WFV1 E2T H1_PF",
    "trades": 368,
    "net": -3998.8055827381854,
    "net_pct": -39.988055827381864,
    "pf": 0.8836796729730344,
    "dd": -53.84533705851522,
    "gross_price": -991.1943347451006,
    "fees": 2556.66558685494,
    "funding": -450.9456611381475,
    "funding_events": 544,
    "proxy_events": 544,
    "turnover": 568.147908189986,
    "holding_seconds": 16786560,
    "directions": {
      "long": {
        "trades": 196,
        "net": -1882.010606736019,
        "gross": 134.66601943886974,
        "fees": 1411.5862478765137,
        "funding": -605.090378298373
      },
      "short": {
        "trades": 172,
        "net": -2116.794976002168,
        "gross": -1125.8603541839702,
        "fees": 1145.079338978423,
        "funding": 154.14471716022496
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -5.594658707881406,
        "end_equity": 9440.53412921186
      },
      {
        "month": "2020-10",
        "return_pct": -1.8874316601321772,
        "end_equity": 9262.35049917153
      },
      {
        "month": "2020-11",
        "return_pct": 21.941998393257343,
        "end_equity": 11294.695296877611
      },
      {
        "month": "2020-12",
        "return_pct": -3.7641856468644597,
        "end_equity": 10869.54199765547
      },
      {
        "month": "2021-01",
        "return_pct": 6.412235495806806,
        "end_equity": 11566.522627860762
      },
      {
        "month": "2021-02",
        "return_pct": -18.595399571307425,
        "end_equity": 9415.681528704366
      },
      {
        "month": "2021-03",
        "return_pct": 5.984803180805831,
        "end_equity": 9979.191536328812
      },
      {
        "month": "2021-04",
        "return_pct": -4.455932535151586,
        "end_equity": 9534.525493916442
      },
      {
        "month": "2021-05",
        "return_pct": -17.414878995498096,
        "end_equity": 7874.099416355977
      },
      {
        "month": "2021-06",
        "return_pct": -2.4359643831581956,
        "end_equity": 7682.289159079078
      },
      {
        "month": "2021-07",
        "return_pct": 2.3805768077900913,
        "end_equity": 7865.171953107487
      },
      {
        "month": "2021-08",
        "return_pct": -7.219464400281106,
        "end_equity": 7297.348663931998
      },
      {
        "month": "2021-09",
        "return_pct": -9.095559263867559,
        "end_equity": 6633.613991513016
      },
      {
        "month": "2021-10",
        "return_pct": 7.708505379678288,
        "end_equity": 7144.966482915888
      },
      {
        "month": "2021-11",
        "return_pct": 2.0421594937440446,
        "end_equity": 7290.878094271585
      },
      {
        "month": "2021-12",
        "return_pct": -12.218868956182439,
        "end_equity": 6400.015254177529
      },
      {
        "month": "2022-01",
        "return_pct": -14.680638252085455,
        "end_equity": 5460.4521666334385
      },
      {
        "month": "2022-02",
        "return_pct": 1.0674292480840508,
        "end_equity": 5518.738630137723
      },
      {
        "month": "2022-03",
        "return_pct": 6.0621849847772635,
        "end_equity": 5853.294774723034
      },
      {
        "month": "2022-04",
        "return_pct": -5.842267665629819,
        "end_equity": 5511.32962672539
      },
      {
        "month": "2022-05",
        "return_pct": 3.5959320289083774,
        "end_equity": 5709.513293991525
      },
      {
        "month": "2022-06",
        "return_pct": 5.1086862969082825,
        "end_equity": 6001.194417261827
      }
    ],
    "max_accounting_error": 1.1823431123048067e-11,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/98a15e51-90f1-4b4d-a5a6-2ed42f6c36e0"
  },
  {
    "name": "s2",
    "session_id": "aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b",
    "title": "MCP Backtest: WFV1 E2T H1_POI",
    "trades": 271,
    "net": 147.99224280630492,
    "net_pct": 1.479922428063053,
    "pf": 1.0047541537792426,
    "dd": -36.55693735906337,
    "gross_price": 2992.357787589996,
    "fees": 2474.5982430627623,
    "funding": -369.7673017209287,
    "funding_events": 405,
    "proxy_events": 405,
    "turnover": 549.9107206806134,
    "holding_seconds": 12659580,
    "directions": {
      "long": {
        "trades": 150,
        "net": 41.892812304613074,
        "gross": 1966.8180161769537,
        "fees": 1386.5635198077835,
        "funding": -538.3616840645597
      },
      "short": {
        "trades": 121,
        "net": 106.0994305016923,
        "gross": 1025.539771413039,
        "fees": 1088.0347232549777,
        "funding": 168.59438234363077
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -3.0542561664167467,
        "end_equity": 9694.574383358326
      },
      {
        "month": "2020-10",
        "return_pct": 4.734662507817822,
        "end_equity": 10153.579761979703
      },
      {
        "month": "2020-11",
        "return_pct": 14.5146932589012,
        "end_equity": 11627.340719228927
      },
      {
        "month": "2020-12",
        "return_pct": 5.175105932001012,
        "end_equity": 12229.067918523713
      },
      {
        "month": "2021-01",
        "return_pct": 13.061134642371464,
        "end_equity": 13826.322944869149
      },
      {
        "month": "2021-02",
        "return_pct": -16.1541173832791,
        "end_equity": 11592.802506563736
      },
      {
        "month": "2021-03",
        "return_pct": -1.5306917797608732,
        "end_equity": 11415.352431551852
      },
      {
        "month": "2021-04",
        "return_pct": -7.137608651791016,
        "end_equity": 10600.56924876497
      },
      {
        "month": "2021-05",
        "return_pct": -1.3813157235102014,
        "end_equity": 10454.141918950192
      },
      {
        "month": "2021-06",
        "return_pct": 3.081261059006102,
        "end_equity": 10776.261322952038
      },
      {
        "month": "2021-07",
        "return_pct": -3.683591686979759,
        "end_equity": 10379.307856692561
      },
      {
        "month": "2021-08",
        "return_pct": -3.384517364356765,
        "end_equity": 10028.018379982756
      },
      {
        "month": "2021-09",
        "return_pct": -5.787861144720274,
        "end_equity": 9447.610600582326
      },
      {
        "month": "2021-10",
        "return_pct": 9.378969599067833,
        "end_equity": 10333.699126649251
      },
      {
        "month": "2021-11",
        "return_pct": 0.13585566209319833,
        "end_equity": 10347.73804201648
      },
      {
        "month": "2021-12",
        "return_pct": -9.963984873586075,
        "end_equity": 9316.690988751647
      },
      {
        "month": "2022-01",
        "return_pct": -5.097745922600905,
        "end_equity": 8841.749753751234
      },
      {
        "month": "2022-02",
        "return_pct": 6.744943165192807,
        "end_equity": 9438.120749450329
      },
      {
        "month": "2022-03",
        "return_pct": 9.063345383687604,
        "end_equity": 10293.530230702498
      },
      {
        "month": "2022-04",
        "return_pct": -4.017826132064284,
        "end_equity": 9879.954083181396
      },
      {
        "month": "2022-05",
        "return_pct": 2.304408610889963,
        "end_equity": 10107.628595826201
      },
      {
        "month": "2022-06",
        "return_pct": 0.3993384461790095,
        "end_equity": 10147.992242806318
      }
    ],
    "max_accounting_error": 1.2732925824820995e-11,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b"
  },
  {
    "name": "s3",
    "session_id": "2ecc415d-5070-405d-b941-e1329a9524e6",
    "title": "MCP Backtest: WFV1 E2T H1_PFOI",
    "trades": 266,
    "net": 114.5101265789517,
    "net_pct": 1.145101265789525,
    "pf": 1.0037863676483518,
    "dd": -35.458322558970764,
    "gross_price": 2857.689844755804,
    "fees": 2394.9470531933694,
    "funding": -348.2326649834828,
    "funding_events": 398,
    "proxy_events": 398,
    "turnover": 532.210456265193,
    "holding_seconds": 12410700,
    "directions": {
      "long": {
        "trades": 147,
        "net": -153.58614283132724,
        "gross": 1697.3415907636395,
        "fees": 1337.4783788831323,
        "funding": -513.4493547118358
      },
      "short": {
        "trades": 119,
        "net": 268.09626941027904,
        "gross": 1160.3482539921627,
        "fees": 1057.4686743102377,
        "funding": 165.21668972835286
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -3.6511409355468483,
        "end_equity": 9634.885906445315
      },
      {
        "month": "2020-10",
        "return_pct": 3.011920613798491,
        "end_equity": 9925.081021177508
      },
      {
        "month": "2020-11",
        "return_pct": 14.514693263262735,
        "end_equity": 11365.676087531729
      },
      {
        "month": "2020-12",
        "return_pct": 5.175105976552885,
        "end_equity": 11953.861870013225
      },
      {
        "month": "2021-01",
        "return_pct": 13.06113472631074,
        "end_equity": 13515.17187385274
      },
      {
        "month": "2021-02",
        "return_pct": -16.154117351998064,
        "end_equity": 11331.915149026332
      },
      {
        "month": "2021-03",
        "return_pct": 1.2606421923931688,
        "end_equity": 11474.77005260115
      },
      {
        "month": "2021-04",
        "return_pct": -7.137608823195174,
        "end_equity": 10655.745852885333
      },
      {
        "month": "2021-05",
        "return_pct": -1.3813157620904737,
        "end_equity": 10508.556355851126
      },
      {
        "month": "2021-06",
        "return_pct": 0.30395030925731703,
        "end_equity": 10540.497145393216
      },
      {
        "month": "2021-07",
        "return_pct": -3.683591526548269,
        "end_equity": 10152.228285689449
      },
      {
        "month": "2021-08",
        "return_pct": -1.4224406969495562,
        "end_equity": 10007.818858906578
      },
      {
        "month": "2021-09",
        "return_pct": -8.00174118528344,
        "end_equity": 9207.019095524887
      },
      {
        "month": "2021-10",
        "return_pct": 9.378969569304175,
        "end_equity": 10070.542614734191
      },
      {
        "month": "2021-11",
        "return_pct": 0.13585600340588755,
        "end_equity": 10084.224051451856
      },
      {
        "month": "2021-12",
        "return_pct": -9.96398471121026,
        "end_equity": 9079.433508721006
      },
      {
        "month": "2022-01",
        "return_pct": -3.160965328427612,
        "end_equity": 8792.435763492696
      },
      {
        "month": "2022-02",
        "return_pct": 6.744943335362774,
        "end_equity": 9385.48057353845
      },
      {
        "month": "2022-03",
        "return_pct": 9.063345149433765,
        "end_equity": 10236.119071851295
      },
      {
        "month": "2022-04",
        "return_pct": -3.7979503863095565,
        "end_equity": 9847.356348018813
      },
      {
        "month": "2022-05",
        "return_pct": 2.304408422418347,
        "end_equity": 10074.279657088107
      },
      {
        "month": "2022-06",
        "return_pct": 0.39933842279797904,
        "end_equity": 10114.51012657898
      }
    ],
    "max_accounting_error": 2.9103830456733704e-11,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/2ecc415d-5070-405d-b941-e1329a9524e6"
  },
  {
    "name": "s4",
    "session_id": "58662d33-5a67-4db4-8b66-58172bfb052e",
    "title": "MCP Backtest: WFV1 E2T H2_P",
    "trades": 142,
    "net": -2254.577094598953,
    "net_pct": -22.545770945989553,
    "pf": 0.8228673623894968,
    "dd": -33.993214928322956,
    "gross_price": -1361.2910148940675,
    "fees": 972.6506866727515,
    "funding": 79.36460696786465,
    "funding_events": 200,
    "proxy_events": 200,
    "turnover": 216.14459703838932,
    "holding_seconds": 6330660,
    "directions": {
      "short": {
        "trades": 72,
        "net": -1451.889308383312,
        "gross": -1138.3927316848103,
        "fees": 498.80177817609706,
        "funding": 185.30520147759694
      },
      "long": {
        "trades": 70,
        "net": -802.6877862156427,
        "gross": -222.89828320925724,
        "fees": 473.84890849665396,
        "funding": -105.94059450973216
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -3.8139877451223714,
        "end_equity": 9618.601225487762
      },
      {
        "month": "2020-10",
        "return_pct": 0.34520055179356746,
        "end_equity": 9651.804689992969
      },
      {
        "month": "2020-11",
        "return_pct": -2.578610926384417,
        "end_equity": 9402.922199663526
      },
      {
        "month": "2020-12",
        "return_pct": -6.230204510108839,
        "end_equity": 8817.100916698064
      },
      {
        "month": "2021-01",
        "return_pct": -6.104722437587351,
        "end_equity": 8278.841378691677
      },
      {
        "month": "2021-02",
        "return_pct": -13.884565801479553,
        "end_equity": 7129.360199867114
      },
      {
        "month": "2021-03",
        "return_pct": 3.2493657133501497,
        "end_equity": 7361.019185782828
      },
      {
        "month": "2021-04",
        "return_pct": -4.698957474842425,
        "end_equity": 7015.1280245279
      },
      {
        "month": "2021-05",
        "return_pct": 17.54322379512685,
        "end_equity": 8245.807633385491
      },
      {
        "month": "2021-06",
        "return_pct": -9.898395787195735,
        "end_equity": 7429.604957982197
      },
      {
        "month": "2021-07",
        "return_pct": -4.617176432628178,
        "end_equity": 7086.5669888248685
      },
      {
        "month": "2021-08",
        "return_pct": 5.962488417838174,
        "end_equity": 7509.102724755895
      },
      {
        "month": "2021-09",
        "return_pct": -0.7194811799013601,
        "end_equity": 7455.076143871816
      },
      {
        "month": "2021-10",
        "return_pct": -6.931751390697127,
        "end_equity": 6938.308799591452
      },
      {
        "month": "2021-11",
        "return_pct": -2.4572905096782005,
        "end_equity": 6767.814395926924
      },
      {
        "month": "2021-12",
        "return_pct": 9.15967751730924,
        "end_equity": 7387.724369563861
      },
      {
        "month": "2022-01",
        "return_pct": 7.409286032092521,
        "end_equity": 7935.101999367452
      },
      {
        "month": "2022-02",
        "return_pct": 14.022540299706488,
        "end_equity": 9047.804875051568
      },
      {
        "month": "2022-03",
        "return_pct": -2.17489155270868,
        "end_equity": 8851.024931118507
      },
      {
        "month": "2022-04",
        "return_pct": 0.6740295400862184,
        "end_equity": 8910.683453754642
      },
      {
        "month": "2022-05",
        "return_pct": -6.174914784865415,
        "end_equity": 8360.45634373619
      },
      {
        "month": "2022-06",
        "return_pct": -7.356457746423728,
        "end_equity": 7745.422905401036
      }
    ],
    "max_accounting_error": 1.0913936421275139e-11,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/58662d33-5a67-4db4-8b66-58172bfb052e"
  },
  {
    "name": "s5",
    "session_id": "cdaa5c6b-6406-4049-9ac1-18b803045e2a",
    "title": "MCP Backtest: WFV1 E2T H2_PF",
    "trades": 8,
    "net": -507.45882060085745,
    "net_pct": -5.074588206008575,
    "pf": 0.41184066320865065,
    "dd": -6.27208213923951,
    "gross_price": -495.52451792489546,
    "fees": 66.71157882222575,
    "funding": 54.77727614626373,
    "funding_events": 15,
    "proxy_events": 15,
    "turnover": 14.824795293827945,
    "holding_seconds": 425160,
    "directions": {
      "short": {
        "trades": 5,
        "net": -173.61979368589832,
        "gross": -187.02876088916582,
        "fees": 41.8985270488357,
        "funding": 55.3074942521032
      },
      "long": {
        "trades": 3,
        "net": -333.83902691495916,
        "gross": -308.49575703572964,
        "fees": 24.81305177339004,
        "funding": -0.5302181058394736
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2020-10",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2020-11",
        "return_pct": -1.0016838305843212,
        "end_equity": 9899.831616941568
      },
      {
        "month": "2020-12",
        "return_pct": 0,
        "end_equity": 9899.831616941568
      },
      {
        "month": "2021-01",
        "return_pct": -1.9999999928468126,
        "end_equity": 9701.83498531089
      },
      {
        "month": "2021-02",
        "return_pct": -1.8446170628055092,
        "end_equity": 9522.873281766611
      },
      {
        "month": "2021-03",
        "return_pct": 0,
        "end_equity": 9522.873281766611
      },
      {
        "month": "2021-04",
        "return_pct": 1.2314612199727737,
        "end_equity": 9640.143773258716
      },
      {
        "month": "2021-05",
        "return_pct": 0,
        "end_equity": 9640.143773258716
      },
      {
        "month": "2021-06",
        "return_pct": -1.9984470310647762,
        "end_equity": 9447.490606231651
      },
      {
        "month": "2021-07",
        "return_pct": 0,
        "end_equity": 9447.490606231651
      },
      {
        "month": "2021-08",
        "return_pct": 1.9712793673754891,
        "end_equity": 9633.727039287034
      },
      {
        "month": "2021-09",
        "return_pct": 0,
        "end_equity": 9633.727039287034
      },
      {
        "month": "2021-10",
        "return_pct": 0,
        "end_equity": 9633.727039287034
      },
      {
        "month": "2021-11",
        "return_pct": 0,
        "end_equity": 9633.727039287034
      },
      {
        "month": "2021-12",
        "return_pct": 0,
        "end_equity": 9633.727039287034
      },
      {
        "month": "2022-01",
        "return_pct": -1.465537266232797,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-02",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-04",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/cdaa5c6b-6406-4049-9ac1-18b803045e2a"
  },
  {
    "name": "s10",
    "session_id": "0a4a627c-d324-4a0d-9697-e939375859cb",
    "title": "MCP Backtest: WFV1 E2T H3_POI",
    "trades": 490,
    "net": -4441.747303312751,
    "net_pct": -44.417473033127465,
    "pf": 0.887738680668636,
    "dd": -54.65983010656925,
    "gross_price": -1092.3735077428312,
    "fees": 2995.1567419814346,
    "funding": -354.217053588482,
    "funding_events": 705,
    "proxy_events": 705,
    "turnover": 665.5903871069838,
    "holding_seconds": 22875780,
    "directions": {
      "short": {
        "trades": 225,
        "net": -636.0439367145173,
        "gross": 424.74142469308634,
        "fees": 1327.9544163607693,
        "funding": 267.16905495316615
      },
      "long": {
        "trades": 265,
        "net": -3805.7033665982285,
        "gross": -1517.1149324359171,
        "fees": 1667.202325620664,
        "funding": -621.3861085416476
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -8.896321967651055,
        "end_equity": 9110.367803234894
      },
      {
        "month": "2020-10",
        "return_pct": -3.308273122501737,
        "end_equity": 8808.971953839422
      },
      {
        "month": "2020-11",
        "return_pct": -1.8710544246878347,
        "end_equity": 8644.1512943276
      },
      {
        "month": "2020-12",
        "return_pct": -0.8650739731787538,
        "end_equity": 8569.372991278176
      },
      {
        "month": "2021-01",
        "return_pct": 13.953787489111868,
        "end_equity": 9765.125087630482
      },
      {
        "month": "2021-02",
        "return_pct": -7.772001159299613,
        "end_equity": 9006.179452612783
      },
      {
        "month": "2021-03",
        "return_pct": -4.628455143234844,
        "end_equity": 8589.332476529367
      },
      {
        "month": "2021-04",
        "return_pct": -10.05506862173402,
        "end_equity": 7725.669201865453
      },
      {
        "month": "2021-05",
        "return_pct": -16.94198818818822,
        "end_equity": 6416.787238226913
      },
      {
        "month": "2021-06",
        "return_pct": 14.274125671732051,
        "end_equity": 7332.727512699088
      },
      {
        "month": "2021-07",
        "return_pct": 2.837464436508297,
        "end_equity": 7540.791048097984
      },
      {
        "month": "2021-08",
        "return_pct": -13.339406775750085,
        "end_equity": 6534.8942560828455
      },
      {
        "month": "2021-09",
        "return_pct": -6.506061397756701,
        "end_equity": 6109.730023503619
      },
      {
        "month": "2021-10",
        "return_pct": 3.4970261306954464,
        "end_equity": 6323.3888789404855
      },
      {
        "month": "2021-11",
        "return_pct": -8.294780748677544,
        "end_equity": 5798.877635546113
      },
      {
        "month": "2021-12",
        "return_pct": -1.070949259388465,
        "end_equity": 5736.7745984553885
      },
      {
        "month": "2022-01",
        "return_pct": -5.578696298264541,
        "end_equity": 5416.737366291577
      },
      {
        "month": "2022-02",
        "return_pct": 2.8435389793924015,
        "end_equity": 5570.764404713392
      },
      {
        "month": "2022-03",
        "return_pct": 8.29275001206453,
        "end_equity": 6032.733970557349
      },
      {
        "month": "2022-04",
        "return_pct": -14.794755813205496,
        "end_equity": 5140.205710753093
      },
      {
        "month": "2022-05",
        "return_pct": 2.7662721115555122,
        "end_equity": 5282.39778780624
      },
      {
        "month": "2022-06",
        "return_pct": 5.222153271338326,
        "end_equity": 5558.2526966872665
      }
    ],
    "max_accounting_error": 1.7280399333685637e-11,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/0a4a627c-d324-4a0d-9697-e939375859cb"
  },
  {
    "name": "s11",
    "session_id": "2e2b071a-f85f-42ba-9f5d-13107abd5723",
    "title": "MCP Backtest: WFV1 E2T H3_PFOI",
    "trades": 28,
    "net": -1591.7850659664393,
    "net_pct": -15.917850659664397,
    "pf": 0.5001910384312138,
    "dd": -22.23841616750003,
    "gross_price": -1484.6080652549724,
    "fees": 213.521832270521,
    "funding": 106.34483155905363,
    "funding_events": 49,
    "proxy_events": 49,
    "turnover": 47.449296060115756,
    "holding_seconds": 1485300,
    "directions": {
      "long": {
        "trades": 9,
        "net": -310.27016300574064,
        "gross": -245.29199551962597,
        "fees": 72.43419157764623,
        "funding": 7.456024091531687
      },
      "short": {
        "trades": 19,
        "net": -1281.5149029606991,
        "gross": -1239.3160697353467,
        "fees": 141.08764069287477,
        "funding": 98.88880746752196
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -3.339130428177739,
        "end_equity": 9666.086957182226
      },
      {
        "month": "2020-10",
        "return_pct": 0.19818144628820367,
        "end_equity": 9685.243348113445
      },
      {
        "month": "2020-11",
        "return_pct": -2.384025133073109,
        "end_equity": 9454.344712495129
      },
      {
        "month": "2020-12",
        "return_pct": -3.914164871189174,
        "end_equity": 9084.286072957513
      },
      {
        "month": "2021-01",
        "return_pct": -1.9999999953350778,
        "end_equity": 8902.600351922138
      },
      {
        "month": "2021-02",
        "return_pct": 0,
        "end_equity": 8902.600351922138
      },
      {
        "month": "2021-03",
        "return_pct": 1.3811685628720705,
        "end_equity": 9025.560269261025
      },
      {
        "month": "2021-04",
        "return_pct": -0.07846366685307915,
        "end_equity": 9018.478483719728
      },
      {
        "month": "2021-05",
        "return_pct": -4.362199710827563,
        "end_equity": 8625.07444138186
      },
      {
        "month": "2021-06",
        "return_pct": -2.003200023759988,
        "end_equity": 8452.296948122781
      },
      {
        "month": "2021-07",
        "return_pct": 0,
        "end_equity": 8452.296948122781
      },
      {
        "month": "2021-08",
        "return_pct": -2.870853587204125,
        "end_equity": 8209.643877986453
      },
      {
        "month": "2021-09",
        "return_pct": -1.99999995251825,
        "end_equity": 8045.4510043248065
      },
      {
        "month": "2021-10",
        "return_pct": -1.9573834754230024,
        "end_equity": 7887.970675842898
      },
      {
        "month": "2021-11",
        "return_pct": -1.3140571290744862,
        "end_equity": 7784.3182348376795
      },
      {
        "month": "2021-12",
        "return_pct": 5.114987987059916,
        "end_equity": 8182.4851774241415
      },
      {
        "month": "2022-01",
        "return_pct": 0,
        "end_equity": 8182.4851774241415
      },
      {
        "month": "2022-02",
        "return_pct": 3.741515455603639,
        "end_equity": 8488.634124989943
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 8488.634124989943
      },
      {
        "month": "2022-04",
        "return_pct": -0.9473749224228056,
        "end_equity": 8408.214934033564
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 8408.214934033564
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 8408.214934033564
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/2e2b071a-f85f-42ba-9f5d-13107abd5723"
  },
  {
    "name": "s6",
    "session_id": "79742595-c37a-45f7-9f90-c913759abe87",
    "title": "MCP Backtest: WFV1 E2T H2_POI",
    "trades": 74,
    "net": 73.45418259732509,
    "net_pct": 0.7345418259732486,
    "pf": 1.0092325767761905,
    "dd": -15.770388952424918,
    "gross_price": 629.5907824194759,
    "fees": 623.0928970336446,
    "funding": 66.95629721149402,
    "funding_events": 101,
    "proxy_events": 101,
    "turnover": 138.4650882296988,
    "holding_seconds": 3232020,
    "directions": {
      "short": {
        "trades": 40,
        "net": 129.14457822459335,
        "gross": 328.5354027174684,
        "fees": 333.0772239935391,
        "funding": 133.6863995006641
      },
      "long": {
        "trades": 34,
        "net": -55.69039562726891,
        "gross": 301.05537970200623,
        "fees": 290.0156730401056,
        "funding": -66.73010228917006
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -1.6657635117595548,
        "end_equity": 9833.423648824044
      },
      {
        "month": "2020-10",
        "return_pct": 1.7368878964939993,
        "end_equity": 10004.219193991446
      },
      {
        "month": "2020-11",
        "return_pct": 0.4154257526599814,
        "end_equity": 10045.77929687584
      },
      {
        "month": "2020-12",
        "return_pct": -1.8733075201315286,
        "end_equity": 9857.59095785165
      },
      {
        "month": "2021-01",
        "return_pct": 0,
        "end_equity": 9857.59095785165
      },
      {
        "month": "2021-02",
        "return_pct": -5.731570154579324,
        "end_equity": 9292.596216550914
      },
      {
        "month": "2021-03",
        "return_pct": -0.335124056100744,
        "end_equity": 9261.454491192944
      },
      {
        "month": "2021-04",
        "return_pct": -5.355313483521806,
        "end_equity": 8765.474570055852
      },
      {
        "month": "2021-05",
        "return_pct": 11.258371057481288,
        "end_equity": 9752.324222101903
      },
      {
        "month": "2021-06",
        "return_pct": -4.301352016262139,
        "end_equity": 9332.842427542102
      },
      {
        "month": "2021-07",
        "return_pct": -5.65829887595195,
        "end_equity": 8804.76230937012
      },
      {
        "month": "2021-08",
        "return_pct": 8.82267974507862,
        "end_equity": 9581.578290241234
      },
      {
        "month": "2021-09",
        "return_pct": -2.338342014270278,
        "end_equity": 9357.528219450323
      },
      {
        "month": "2021-10",
        "return_pct": -3.120063509434179,
        "end_equity": 9065.567396090248
      },
      {
        "month": "2021-11",
        "return_pct": 2.2704290531787796,
        "end_equity": 9271.394672086584
      },
      {
        "month": "2021-12",
        "return_pct": 11.12810078576889,
        "end_equity": 10303.124815442787
      },
      {
        "month": "2022-01",
        "return_pct": 3.4006625983554084,
        "end_equity": 10653.499327503425
      },
      {
        "month": "2022-02",
        "return_pct": 12.259043481766096,
        "end_equity": 11959.516442391729
      },
      {
        "month": "2022-03",
        "return_pct": -3.9599999141677777,
        "end_equity": 11485.919601538135
      },
      {
        "month": "2022-04",
        "return_pct": -0.9763824955999811,
        "end_equity": 11373.773093090029
      },
      {
        "month": "2022-05",
        "return_pct": -5.899021989425279,
        "end_equity": 10702.831717301313
      },
      {
        "month": "2022-06",
        "return_pct": -5.880476787153199,
        "end_equity": 10073.45418259734
      }
    ],
    "max_accounting_error": 1.4551915228366852e-11,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/79742595-c37a-45f7-9f90-c913759abe87"
  },
  {
    "name": "s7",
    "session_id": "2e436b8e-0c9a-4a57-a3a0-6116aa5618e1",
    "title": "MCP Backtest: WFV1 E2T H2_PFOI",
    "trades": 4,
    "net": -70.20109995191402,
    "net_pct": -0.7020109995191401,
    "pf": 0.816724369914171,
    "dd": -3.027923653046327,
    "gross_price": -84.87444064455042,
    "fees": 33.87004145546798,
    "funding": 48.543382148104385,
    "funding_events": 8,
    "proxy_events": 8,
    "turnover": 7.526675878992883,
    "holding_seconds": 224040,
    "directions": {
      "short": {
        "trades": 3,
        "net": 128.37284643214662,
        "gross": 105.37806231580016,
        "fees": 25.394292448584388,
        "funding": 48.38907656493082
      },
      "long": {
        "trades": 1,
        "net": -198.57394638406063,
        "gross": -190.2525029603506,
        "fees": 8.475749006883591,
        "funding": 0.15430558317356952
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2020-10",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2020-11",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2020-12",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2021-01",
        "return_pct": 0,
        "end_equity": 10000
      },
      {
        "month": "2021-02",
        "return_pct": -1.8446170281293583,
        "end_equity": 9815.538297187064
      },
      {
        "month": "2021-03",
        "return_pct": 0,
        "end_equity": 9815.538297187064
      },
      {
        "month": "2021-04",
        "return_pct": 1.231461164976233,
        "end_equity": 9936.412839450291
      },
      {
        "month": "2021-05",
        "return_pct": 0,
        "end_equity": 9936.412839450291
      },
      {
        "month": "2021-06",
        "return_pct": -1.998447020998051,
        "end_equity": 9737.83889306623
      },
      {
        "month": "2021-07",
        "return_pct": 0,
        "end_equity": 9737.83889306623
      },
      {
        "month": "2021-08",
        "return_pct": 1.9712793473975143,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2021-09",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2021-10",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2021-11",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2021-12",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-01",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-02",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-04",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      }
    ],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H2_PFOI",
    "strategy": "ResearchV1_H2_PFOI_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/2e436b8e-0c9a-4a57-a3a0-6116aa5618e1"
  },
  {
    "name": "s8",
    "session_id": "eef318bf-6b93-4de2-9cef-f8512d472011",
    "title": "MCP Backtest: WFV1 E2T H3_P",
    "trades": 652,
    "net": -6162.242204315608,
    "net_pct": -61.62242204315606,
    "pf": 0.8948003177105238,
    "dd": -73.25031050254,
    "gross_price": -1355.6515164782286,
    "fees": 4389.0579302451715,
    "funding": -417.532757592204,
    "funding_events": 907,
    "proxy_events": 907,
    "turnover": 975.3462067211503,
    "holding_seconds": 29723700,
    "directions": {
      "long": {
        "trades": 335,
        "net": -3950.8804322457686,
        "gross": -805.4695760235226,
        "fees": 2310.3068234437064,
        "funding": -835.1040327785361
      },
      "short": {
        "trades": 317,
        "net": -2211.3617720698385,
        "gross": -550.181940454703,
        "fees": 2078.7511068014683,
        "funding": 417.5712751863326
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": -9.169040705866715,
        "end_equity": 9083.095929413328
      },
      {
        "month": "2020-10",
        "return_pct": -3.73272384052854,
        "end_equity": 8744.04904219804
      },
      {
        "month": "2020-11",
        "return_pct": 20.504546677887703,
        "end_equity": 10536.976659592929
      },
      {
        "month": "2020-12",
        "return_pct": -5.057962118889048,
        "end_equity": 10004.020371674538
      },
      {
        "month": "2021-01",
        "return_pct": 28.979146473951943,
        "end_equity": 12903.100088466095
      },
      {
        "month": "2021-02",
        "return_pct": -3.290347255933501,
        "end_equity": 12478.543288774898
      },
      {
        "month": "2021-03",
        "return_pct": -5.5406532119708025,
        "end_equity": 11787.150479238224
      },
      {
        "month": "2021-04",
        "return_pct": -4.946082391650997,
        "end_equity": 11204.148304907216
      },
      {
        "month": "2021-05",
        "return_pct": -23.9417212745763,
        "end_equity": 8521.682346556165
      },
      {
        "month": "2021-06",
        "return_pct": 0.5977478673048653,
        "end_equity": 8572.620521041199
      },
      {
        "month": "2021-07",
        "return_pct": 3.2881380073720656,
        "end_equity": 8854.500114621333
      },
      {
        "month": "2021-08",
        "return_pct": -27.116470246095183,
        "end_equity": 6453.472225599576
      },
      {
        "month": "2021-09",
        "return_pct": -1.0004299361155877,
        "end_equity": 6388.909757535773
      },
      {
        "month": "2021-10",
        "return_pct": -11.105280162113129,
        "end_equity": 5679.4034296568425
      },
      {
        "month": "2021-11",
        "return_pct": -8.76690447787719,
        "end_equity": 5181.495556065546
      },
      {
        "month": "2021-12",
        "return_pct": 2.1902531784939727,
        "end_equity": 5294.983427175796
      },
      {
        "month": "2022-01",
        "return_pct": -5.40019181034086,
        "end_equity": 5009.044165782543
      },
      {
        "month": "2022-02",
        "return_pct": 13.723037138172556,
        "end_equity": 5696.437156920347
      },
      {
        "month": "2022-03",
        "return_pct": -9.852852841430149,
        "end_equity": 5135.175586644437
      },
      {
        "month": "2022-04",
        "return_pct": -16.812799918075893,
        "end_equity": 4271.808789820028
      },
      {
        "month": "2022-05",
        "return_pct": -6.611432200745016,
        "end_equity": 3989.381047935611
      },
      {
        "month": "2022-06",
        "return_pct": -3.8006710923154996,
        "end_equity": 3837.7577956844093
      }
    ],
    "max_accounting_error": 1.77351466845721e-11,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/eef318bf-6b93-4de2-9cef-f8512d472011"
  },
  {
    "name": "s9",
    "session_id": "2be7a6c4-381b-4353-a473-b6a29b3d6892",
    "title": "MCP Backtest: WFV1 E2T H3_PF",
    "trades": 45,
    "net": -1566.6761214346482,
    "net_pct": -15.666761214346478,
    "pf": 0.6838427272489667,
    "dd": -26.082483251482657,
    "gross_price": -1361.399764618081,
    "fees": 345.51582211050913,
    "funding": 140.23946529394235,
    "funding_events": 69,
    "proxy_events": 69,
    "turnover": 76.78129380233534,
    "holding_seconds": 2124120,
    "directions": {
      "short": {
        "trades": 32,
        "net": -1471.2905252991736,
        "gross": -1361.2222493903323,
        "fees": 244.0297644979462,
        "funding": 133.9614885891045
      },
      "long": {
        "trades": 13,
        "net": -95.38559613547372,
        "gross": -0.1775152277486427,
        "fees": 101.48605761256282,
        "funding": 6.277976704837816
      }
    },
    "months": [
      {
        "month": "2020-09",
        "return_pct": 0.2932970173397331,
        "end_equity": 10029.329701733974
      },
      {
        "month": "2020-10",
        "return_pct": 0.198181484773019,
        "end_equity": 10049.205976249652
      },
      {
        "month": "2020-11",
        "return_pct": -4.62286673336717,
        "end_equity": 9584.644576206061
      },
      {
        "month": "2020-12",
        "return_pct": -0.2664517325947302,
        "end_equity": 9559.106124669714
      },
      {
        "month": "2021-01",
        "return_pct": -5.79877098896281,
        "end_equity": 9004.7954519082
      },
      {
        "month": "2021-02",
        "return_pct": -1.9999999959949832,
        "end_equity": 8824.69954323068
      },
      {
        "month": "2021-03",
        "return_pct": 1.381168686012213,
        "end_equity": 8946.583529956444
      },
      {
        "month": "2021-04",
        "return_pct": -2.076894298323728,
        "end_equity": 8760.77244672801
      },
      {
        "month": "2021-05",
        "return_pct": -6.234536281754188,
        "end_equity": 8214.578909974827
      },
      {
        "month": "2021-06",
        "return_pct": -3.9537519819914047,
        "end_equity": 7889.79483350945
      },
      {
        "month": "2021-07",
        "return_pct": 1.0104647164887126,
        "end_equity": 7969.518426505411
      },
      {
        "month": "2021-08",
        "return_pct": 2.454366641590222,
        "end_equity": 8165.119628260945
      },
      {
        "month": "2021-09",
        "return_pct": -2.816771131836293,
        "end_equity": 7935.126895692192
      },
      {
        "month": "2021-10",
        "return_pct": -1.957383503856458,
        "end_equity": 7779.806030825836
      },
      {
        "month": "2021-11",
        "return_pct": -1.3140571710938298,
        "end_equity": 7677.574931780579
      },
      {
        "month": "2021-12",
        "return_pct": 5.114987919380742,
        "end_equity": 8070.281962042561
      },
      {
        "month": "2022-01",
        "return_pct": -2.0067961889905894,
        "end_equity": 7908.327851187496
      },
      {
        "month": "2022-02",
        "return_pct": 5.942142866065314,
        "end_equity": 8378.25199042189
      },
      {
        "month": "2022-03",
        "return_pct": 0,
        "end_equity": 8378.25199042189
      },
      {
        "month": "2022-04",
        "return_pct": 0.6573195483547956,
        "end_equity": 8433.323878565358
      },
      {
        "month": "2022-05",
        "return_pct": 0,
        "end_equity": 8433.323878565358
      },
      {
        "month": "2022-06",
        "return_pct": 0,
        "end_equity": 8433.323878565358
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E2T",
    "dashboard_url": "http://localhost:9200/#/backtest/2be7a6c4-381b-4353-a473-b6a29b3d6892"
  }
]
```
