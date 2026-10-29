# Walk-forward E3T — selection BEFORE evaluation

Selection: **SIN_CANDIDATA**. Frozen gates and ranking, based only on this train.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 473 | -43.40 | 0.898 | -61.60 | [dashboard](http://localhost:9200/#/backtest/1f11e4be-bb91-4445-b6df-662f909ed76d) |
| H1_PF | 463 | -48.48 | 0.876 | -61.35 | [dashboard](http://localhost:9200/#/backtest/f97329c8-b084-4d4f-b102-098172629c6a) |
| H1_PFOI | 329 | -7.88 | 0.978 | -35.46 | [dashboard](http://localhost:9200/#/backtest/7aaa0d64-eb5e-4096-8dc4-5fe3058d6411) |
| H1_POI | 335 | -4.12 | 0.989 | -36.56 | [dashboard](http://localhost:9200/#/backtest/d546fc9f-90bf-45d4-85b7-fa6d29d4736f) |
| H2_P | 179 | -33.70 | 0.778 | -36.36 | [dashboard](http://localhost:9200/#/backtest/f9de72a4-6440-42f5-aca3-e418cf55ee44) |
| H2_PF | 8 | -5.07 | 0.412 | -6.27 | [dashboard](http://localhost:9200/#/backtest/097151bc-8183-4348-892c-4bbf1f07ee73) |
| H2_PFOI | 4 | -0.70 | 0.817 | -3.03 | [dashboard](http://localhost:9200/#/backtest/083ce1ce-3167-46f9-abb4-9edb7329c4f5) |
| H2_POI | 99 | -10.08 | 0.901 | -26.98 | [dashboard](http://localhost:9200/#/backtest/8bd7e5b0-9015-4292-98b9-708da3278fd5) |
| H3_P | 822 | -66.08 | 0.895 | -78.54 | [dashboard](http://localhost:9200/#/backtest/9356960c-5f31-4caa-b688-3871672fea49) |
| H3_PF | 51 | -18.95 | 0.658 | -26.08 | [dashboard](http://localhost:9200/#/backtest/732911a4-c86c-42c5-a964-79ed962f820a) |
| H3_PFOI | 32 | -18.87 | 0.474 | -22.24 | [dashboard](http://localhost:9200/#/backtest/6fa05f22-05c6-4f5a-9e88-4e8280a43912) |
| H3_POI | 615 | -54.04 | 0.881 | -59.66 | [dashboard](http://localhost:9200/#/backtest/d7b8a609-4cc9-4809-8f95-e03fd16ac691) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "1f11e4be-bb91-4445-b6df-662f909ed76d",
    "title": "MCP Backtest: WFV1 E3T H1_P",
    "trades": 473,
    "net": -4339.629714536195,
    "net_pct": -43.396297145361906,
    "pf": 0.8980333917748814,
    "dd": -61.59508547456305,
    "gross_price": -576.6432569788127,
    "fees": 3276.9525013324314,
    "funding": -486.0339562249466,
    "funding_events": 739,
    "proxy_events": 739,
    "turnover": 728.2116669627611,
    "holding_seconds": 22689420,
    "directions": {
      "long": {
        "trades": 248,
        "net": -2316.834626391273,
        "gross": 146.0860740824686,
        "fees": 1787.6642031016702,
        "funding": -675.2564973720704
      },
      "short": {
        "trades": 225,
        "net": -2022.7950881449187,
        "gross": -722.7293310612828,
        "fees": 1489.2882982307585,
        "funding": 189.2225411471227
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
      },
      {
        "month": "2022-07",
        "return_pct": 1.706814893176145,
        "end_equity": 6464.150081501953
      },
      {
        "month": "2022-08",
        "return_pct": -18.502929471363572,
        "end_equity": 5268.092950998555
      },
      {
        "month": "2022-09",
        "return_pct": -8.823108389448075,
        "end_equity": 4803.283399875079
      },
      {
        "month": "2022-10",
        "return_pct": 4.9321697127646225,
        "end_equity": 5040.189488941969
      },
      {
        "month": "2022-11",
        "return_pct": 17.324485973491477,
        "end_equity": 5913.376409991112
      },
      {
        "month": "2022-12",
        "return_pct": -4.2785391455855475,
        "end_equity": 5660.370285463821
      }
    ],
    "max_accounting_error": 1.6370904631912708e-11,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/1f11e4be-bb91-4445-b6df-662f909ed76d"
  },
  {
    "name": "s1",
    "session_id": "f97329c8-b084-4d4f-b102-098172629c6a",
    "title": "MCP Backtest: WFV1 E3T H1_PF",
    "trades": 463,
    "net": -4848.097416426776,
    "net_pct": -48.480974164267764,
    "pf": 0.876378986451595,
    "dd": -61.351792363467396,
    "gross_price": -1405.5310424599988,
    "fees": 2989.1283745225746,
    "funding": -453.4379994442003,
    "funding_events": 730,
    "proxy_events": 730,
    "turnover": 664.250749893905,
    "holding_seconds": 22375380,
    "directions": {
      "long": {
        "trades": 243,
        "net": -2802.9616837116437,
        "gross": -545.8838561039906,
        "fees": 1628.7530593787944,
        "funding": -628.3247682288572
      },
      "short": {
        "trades": 220,
        "net": -2045.1357327151322,
        "gross": -859.647186356009,
        "fees": 1360.3753151437795,
        "funding": 174.8867687846562
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
      },
      {
        "month": "2022-07",
        "return_pct": 1.7068148900354352,
        "end_equity": 6103.623697155626
      },
      {
        "month": "2022-08",
        "return_pct": -18.502929471113738,
        "end_equity": 4974.274509288736
      },
      {
        "month": "2022-09",
        "return_pct": -8.823108469616336,
        "end_equity": 4535.388873757715
      },
      {
        "month": "2022-10",
        "return_pct": 4.932169902615158,
        "end_equity": 4759.08195875575
      },
      {
        "month": "2022-11",
        "return_pct": 13.09284780772282,
        "end_equity": 5382.181316660434
      },
      {
        "month": "2022-12",
        "return_pct": -4.278539118969837,
        "end_equity": 5151.902583573232
      }
    ],
    "max_accounting_error": 8.185452315956354e-12,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/f97329c8-b084-4d4f-b102-098172629c6a"
  },
  {
    "name": "s2",
    "session_id": "d546fc9f-90bf-45d4-85b7-fa6d29d4736f",
    "title": "MCP Backtest: WFV1 E3T H1_POI",
    "trades": 335,
    "net": -412.18290447248523,
    "net_pct": -4.121829044724847,
    "pf": 0.9888425447215986,
    "dd": -36.55693735906337,
    "gross_price": 2987.2789591317137,
    "fees": 3012.3725333041953,
    "funding": -387.0893303000022,
    "funding_events": 528,
    "proxy_events": 528,
    "turnover": 669.4161185120435,
    "holding_seconds": 16474740,
    "directions": {
      "long": {
        "trades": 189,
        "net": -554.536279247686,
        "gross": 1737.9669538509545,
        "fees": 1716.1500799484115,
        "funding": -576.35315315023
      },
      "short": {
        "trades": 146,
        "net": 142.35337477520136,
        "gross": 1249.3120052807565,
        "fees": 1296.2224533557833,
        "funding": 189.2638228502278
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
      },
      {
        "month": "2022-07",
        "return_pct": -0.9229061731525601,
        "end_equity": 10054.335795946416
      },
      {
        "month": "2022-08",
        "return_pct": -5.572871314302974,
        "end_equity": 9494.020600530423
      },
      {
        "month": "2022-09",
        "return_pct": -4.195300315924078,
        "end_equity": 9095.717924282473
      },
      {
        "month": "2022-10",
        "return_pct": 7.088547734003714,
        "end_equity": 9740.472231095568
      },
      {
        "month": "2022-11",
        "return_pct": 2.750766018867945,
        "end_equity": 10008.409831305813
      },
      {
        "month": "2022-12",
        "return_pct": -4.202393215980127,
        "end_equity": 9587.81709552753
      }
    ],
    "max_accounting_error": 1.4551915228366852e-11,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/d546fc9f-90bf-45d4-85b7-fa6d29d4736f"
  },
  {
    "name": "s3",
    "session_id": "7aaa0d64-eb5e-4096-8dc4-5fe3058d6411",
    "title": "MCP Backtest: WFV1 E3T H1_PFOI",
    "trades": 329,
    "net": -788.4874374164837,
    "net_pct": -7.884874374164832,
    "pf": 0.9780903555108239,
    "dd": -35.458322558970764,
    "gross_price": 2495.286293249591,
    "fees": 2918.2495840191436,
    "funding": -365.5241466469315,
    "funding_events": 521,
    "proxy_events": 521,
    "turnover": 648.4999075598097,
    "holding_seconds": 16222800,
    "directions": {
      "long": {
        "trades": 186,
        "net": -747.3632494956416,
        "gross": 1467.8659654977848,
        "fees": 1664.1512284512496,
        "funding": -551.0779865421782
      },
      "short": {
        "trades": 143,
        "net": -41.12418792084151,
        "gross": 1027.4203277518038,
        "fees": 1254.0983555678931,
        "funding": 185.55383989524668
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
      },
      {
        "month": "2022-07",
        "return_pct": -0.9229060647827136,
        "end_equity": 10021.162699197721
      },
      {
        "month": "2022-08",
        "return_pct": -5.572871377022148,
        "end_equity": 9462.69619148931
      },
      {
        "month": "2022-09",
        "return_pct": -4.195300302472871,
        "end_equity": 9065.70766954567
      },
      {
        "month": "2022-10",
        "return_pct": 7.08854777071255,
        "end_equity": 9708.334688454568
      },
      {
        "month": "2022-11",
        "return_pct": -0.9552297273068833,
        "end_equity": 9615.597789484003
      },
      {
        "month": "2022-12",
        "return_pct": -4.2023931922608675,
        "end_equity": 9211.51256258354
      }
    ],
    "max_accounting_error": 2.3646862246096134e-11,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/7aaa0d64-eb5e-4096-8dc4-5fe3058d6411"
  },
  {
    "name": "s4",
    "session_id": "f9de72a4-6440-42f5-aca3-e418cf55ee44",
    "title": "MCP Backtest: WFV1 E3T H2_P",
    "trades": 179,
    "net": -3369.9673221502057,
    "net_pct": -33.69967322150208,
    "pf": 0.7784907498561656,
    "dd": -36.362181292124184,
    "gross_price": -2259.4306981687314,
    "fees": 1195.8319295072242,
    "funding": 85.295305525749,
    "funding_events": 269,
    "proxy_events": 269,
    "turnover": 265.74042877938354,
    "holding_seconds": 8514840,
    "directions": {
      "short": {
        "trades": 92,
        "net": -1816.5919064237937,
        "gross": -1395.4875918271134,
        "fees": 620.7926146905621,
        "funding": 199.68830009388338
      },
      "long": {
        "trades": 87,
        "net": -1553.3754157264138,
        "gross": -863.9431063416182,
        "fees": 575.039314816662,
        "funding": -114.39299456813421
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
      },
      {
        "month": "2022-07",
        "return_pct": -3.826619369196471,
        "end_equity": 7449.035052276779
      },
      {
        "month": "2022-08",
        "return_pct": -10.348043120226624,
        "end_equity": 6678.2056930263825
      },
      {
        "month": "2022-09",
        "return_pct": -4.39245609282668,
        "end_equity": 6384.868440171547
      },
      {
        "month": "2022-10",
        "return_pct": 8.294875983991169,
        "end_equity": 6914.4853590247685
      },
      {
        "month": "2022-11",
        "return_pct": -4.677685230273321,
        "end_equity": 6591.047498636256
      },
      {
        "month": "2022-12",
        "return_pct": 0.5914868497244763,
        "end_equity": 6630.032677849783
      }
    ],
    "max_accounting_error": 1.1823431123048067e-11,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/f9de72a4-6440-42f5-aca3-e418cf55ee44"
  },
  {
    "name": "s5",
    "session_id": "097151bc-8183-4348-892c-4bbf1f07ee73",
    "title": "MCP Backtest: WFV1 E3T H2_PF",
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
      },
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-08",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-09",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-11",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/097151bc-8183-4348-892c-4bbf1f07ee73"
  },
  {
    "name": "s10",
    "session_id": "d7b8a609-4cc9-4809-8f95-e03fd16ac691",
    "title": "MCP Backtest: WFV1 E3T H3_POI",
    "trades": 615,
    "net": -5404.141481825993,
    "net_pct": -54.041414818259895,
    "pf": 0.8812762362577525,
    "dd": -59.66059736510242,
    "gross_price": -1518.1722803294097,
    "fees": 3529.918545691757,
    "funding": -356.05065580482193,
    "funding_events": 943,
    "proxy_events": 943,
    "turnover": 784.4263434870562,
    "holding_seconds": 30308700,
    "directions": {
      "short": {
        "trades": 290,
        "net": -1709.5627031360273,
        "gross": -395.55200792959033,
        "fees": 1605.7407086830558,
        "funding": 291.7300134766179
      },
      "long": {
        "trades": 325,
        "net": -3694.578778689962,
        "gross": -1122.6202723998183,
        "fees": 1924.1778370087013,
        "funding": -647.7806692814391
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
      },
      {
        "month": "2022-07",
        "return_pct": -1.8372050790771421,
        "end_equity": 5456.136195835786
      },
      {
        "month": "2022-08",
        "return_pct": -12.628213367743047,
        "end_equity": 4767.123675390984
      },
      {
        "month": "2022-09",
        "return_pct": -3.064251222288783,
        "end_equity": 4621.047029899798
      },
      {
        "month": "2022-10",
        "return_pct": 1.503240249312121,
        "end_equity": 4690.512468792894
      },
      {
        "month": "2022-11",
        "return_pct": -4.960959658754394,
        "end_equity": 4457.818037427233
      },
      {
        "month": "2022-12",
        "return_pct": 3.096592987596347,
        "end_equity": 4595.85851817401
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/d7b8a609-4cc9-4809-8f95-e03fd16ac691"
  },
  {
    "name": "s11",
    "session_id": "6fa05f22-05c6-4f5a-9e88-4e8280a43912",
    "title": "MCP Backtest: WFV1 E3T H3_PFOI",
    "trades": 32,
    "net": -1887.127815563641,
    "net_pct": -18.871278155636418,
    "pf": 0.4743809294758545,
    "dd": -22.23841616750003,
    "gross_price": -1754.665156261291,
    "fees": 241.6783146814984,
    "funding": 109.21565537914759,
    "funding_events": 58,
    "proxy_events": 58,
    "turnover": 53.70629215144407,
    "holding_seconds": 1779720,
    "directions": {
      "long": {
        "trades": 10,
        "net": -478.2525286123247,
        "gross": -406.28409309726595,
        "fees": 79.60638952473009,
        "funding": 7.637954009671494
      },
      "short": {
        "trades": 22,
        "net": -1408.8752869513169,
        "gross": -1348.3810631640254,
        "fees": 162.0719251567683,
        "funding": 101.57770136947612
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
      },
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 8408.214934033564
      },
      {
        "month": "2022-08",
        "return_pct": -1.9978362461531396,
        "end_equity": 8240.23256842698
      },
      {
        "month": "2022-09",
        "return_pct": -2.882518519421984,
        "end_equity": 8002.70633859863
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 8002.70633859863
      },
      {
        "month": "2022-11",
        "return_pct": 1.3766073772616183,
        "end_equity": 8112.872184436363
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 8112.872184436363
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/6fa05f22-05c6-4f5a-9e88-4e8280a43912"
  },
  {
    "name": "s6",
    "session_id": "8bd7e5b0-9015-4292-98b9-708da3278fd5",
    "title": "MCP Backtest: WFV1 E3T H2_POI",
    "trades": 99,
    "net": -1008.0608588918077,
    "net_pct": -10.080608588918079,
    "pf": 0.9007981178066888,
    "dd": -26.981575986855844,
    "gross_price": -254.35145002043458,
    "fees": 823.8936081204218,
    "funding": 70.18419924904936,
    "funding_events": 147,
    "proxy_events": 147,
    "turnover": 183.0874684712049,
    "holding_seconds": 4694880,
    "directions": {
      "short": {
        "trades": 54,
        "net": -617.619171250513,
        "gross": -316.01466265875854,
        "fees": 446.5117923826309,
        "funding": 144.90728379087665
      },
      "long": {
        "trades": 45,
        "net": -390.44168764129483,
        "gross": 61.6632126383228,
        "fees": 377.381815737791,
        "funding": -74.72308454182725
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
      },
      {
        "month": "2022-07",
        "return_pct": -5.412014599132342,
        "end_equity": 9528.277371598264
      },
      {
        "month": "2022-08",
        "return_pct": -5.758013483004786,
        "end_equity": 8979.637875843542
      },
      {
        "month": "2022-09",
        "return_pct": -2.428289074476042,
        "end_equity": 8761.58631037692
      },
      {
        "month": "2022-10",
        "return_pct": 5.373010211630347,
        "end_equity": 9232.347237534279
      },
      {
        "month": "2022-11",
        "return_pct": -2.914513743056746,
        "end_equity": 8963.269208489623
      },
      {
        "month": "2022-12",
        "return_pct": 0.31986022010166426,
        "end_equity": 8991.939141108202
      }
    ],
    "max_accounting_error": 9.094947017729282e-12,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/8bd7e5b0-9015-4292-98b9-708da3278fd5"
  },
  {
    "name": "s7",
    "session_id": "083ce1ce-3167-46f9-abb4-9edb7329c4f5",
    "title": "MCP Backtest: WFV1 E3T H2_PFOI",
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
      },
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-08",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-09",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-11",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      }
    ],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H2_PFOI",
    "strategy": "ResearchV1_H2_PFOI_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/083ce1ce-3167-46f9-abb4-9edb7329c4f5"
  },
  {
    "name": "s8",
    "session_id": "9356960c-5f31-4caa-b688-3871672fea49",
    "title": "MCP Backtest: WFV1 E3T H3_P",
    "trades": 822,
    "net": -6608.126730911838,
    "net_pct": -66.08126730911835,
    "pf": 0.8954547175088842,
    "dd": -78.54109243247602,
    "gross_price": -1312.05216256709,
    "fees": 4876.88042022634,
    "funding": -419.1941481184038,
    "funding_events": 1269,
    "proxy_events": 1269,
    "turnover": 1083.751204494742,
    "holding_seconds": 40680000,
    "directions": {
      "long": {
        "trades": 414,
        "net": -4338.822714980309,
        "gross": -942.1538699649456,
        "fees": 2535.237385105165,
        "funding": -861.4314599101954
      },
      "short": {
        "trades": 408,
        "net": -2269.3040159315274,
        "gross": -369.8982926021429,
        "fees": 2341.643035121175,
        "funding": 442.2373117917925
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
      },
      {
        "month": "2022-07",
        "return_pct": -4.543584055134941,
        "end_equity": 3663.386044404994
      },
      {
        "month": "2022-08",
        "return_pct": -16.583968368006317,
        "end_equity": 3055.851261602912
      },
      {
        "month": "2022-09",
        "return_pct": -4.673897164758745,
        "end_equity": 2913.023916127609
      },
      {
        "month": "2022-10",
        "return_pct": 6.708166906953972,
        "end_equity": 3108.434422460936
      },
      {
        "month": "2022-11",
        "return_pct": 14.359455474117988,
        "end_equity": 3554.7886792963704
      },
      {
        "month": "2022-12",
        "return_pct": -4.582984388271383,
        "end_equity": 3391.8732690881793
      }
    ],
    "max_accounting_error": 1.77351466845721e-11,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/9356960c-5f31-4caa-b688-3871672fea49"
  },
  {
    "name": "s9",
    "session_id": "732911a4-c86c-42c5-a964-79ed962f820a",
    "title": "MCP Backtest: WFV1 E3T H3_PF",
    "trades": 51,
    "net": -1894.9075861680037,
    "net_pct": -18.949075861680033,
    "pf": 0.6575984137468075,
    "dd": -26.082483251482657,
    "gross_price": -1650.689203185582,
    "fees": 388.6053495172706,
    "funding": 144.38696653484942,
    "funding_events": 81,
    "proxy_events": 81,
    "turnover": 86.35674433717124,
    "holding_seconds": 2512140,
    "directions": {
      "short": {
        "trades": 35,
        "net": -1601.125478182179,
        "gross": -1472.4063387734907,
        "fees": 265.42176613779276,
        "funding": 136.70262672910422
      },
      "long": {
        "trades": 16,
        "net": -293.78210798582387,
        "gross": -178.28286441209121,
        "fees": 123.18358337947777,
        "funding": 7.684339805745155
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
      },
      {
        "month": "2022-07",
        "return_pct": 0,
        "end_equity": 8433.323878565358
      },
      {
        "month": "2022-08",
        "return_pct": -0.3911443004192994,
        "end_equity": 8400.337412878449
      },
      {
        "month": "2022-09",
        "return_pct": -2.882518509749099,
        "end_equity": 8158.196132070849
      },
      {
        "month": "2022-10",
        "return_pct": 0,
        "end_equity": 8158.196132070849
      },
      {
        "month": "2022-11",
        "return_pct": -0.6509247556587661,
        "end_equity": 8105.092413832003
      },
      {
        "month": "2022-12",
        "return_pct": 0,
        "end_equity": 8105.092413832003
      }
    ],
    "max_accounting_error": 7.275957614183426e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E3T",
    "dashboard_url": "http://localhost:9200/#/backtest/732911a4-c86c-42c5-a964-79ed962f820a"
  }
]
```
