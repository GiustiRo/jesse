# Walk-forward E4T — selection BEFORE evaluation

Selection: **SIN_CANDIDATA**. Frozen gates and ranking, based only on this train.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 558 | -31.89 | 0.932 | -61.60 | [dashboard](http://localhost:9200/#/backtest/32a12c2b-8c77-46b8-92b6-a905f6577c3d) |
| H1_PF | 545 | -38.28 | 0.911 | -61.35 | [dashboard](http://localhost:9200/#/backtest/2e11d184-8f0e-41d4-bbd0-36f60b08c1c8) |
| H1_PFOI | 383 | -1.16 | 0.997 | -35.46 | [dashboard](http://localhost:9200/#/backtest/3aeb8ed2-0c9b-4e79-96b5-4aea50a50f6c) |
| H1_POI | 391 | 7.33 | 1.018 | -36.56 | [dashboard](http://localhost:9200/#/backtest/34995866-f432-45ce-9611-93ae23b9b91c) |
| H2_P | 209 | -38.63 | 0.769 | -42.04 | [dashboard](http://localhost:9200/#/backtest/0277973d-e8af-4e40-8d90-47429c3d040b) |
| H2_PF | 8 | -5.07 | 0.412 | -6.27 | [dashboard](http://localhost:9200/#/backtest/713a0888-ca63-4b98-ab26-165a83f57b0d) |
| H2_PFOI | 4 | -0.70 | 0.817 | -3.03 | [dashboard](http://localhost:9200/#/backtest/e0e8d591-8633-4a09-b874-4d30d8299963) |
| H2_POI | 111 | -9.65 | 0.910 | -29.40 | [dashboard](http://localhost:9200/#/backtest/7c992620-282b-41ef-b10f-05465afdf269) |
| H3_P | 989 | -66.31 | 0.902 | -78.54 | [dashboard](http://localhost:9200/#/backtest/dedaac18-1491-478d-92dd-3ba9913efdb8) |
| H3_PF | 57 | -24.97 | 0.597 | -27.77 | [dashboard](http://localhost:9200/#/backtest/76f47461-5b27-4ca6-af5e-4e322d487e32) |
| H3_PFOI | 34 | -22.09 | 0.435 | -22.24 | [dashboard](http://localhost:9200/#/backtest/2f3bada8-e82b-4268-a59d-c3338bc359b1) |
| H3_POI | 732 | -35.14 | 0.930 | -59.66 | [dashboard](http://localhost:9200/#/backtest/18d403c9-9f86-4f3f-9253-c0d601884718) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "32a12c2b-8c77-46b8-92b6-a905f6577c3d",
    "title": "MCP Backtest: WFV1 E4T H1_P",
    "trades": 558,
    "net": -3189.1701920417427,
    "net_pct": -31.891701920417358,
    "pf": 0.9322961860129015,
    "dd": -61.59508547456305,
    "gross_price": 1068.7981259049038,
    "fees": 3757.9678770475325,
    "funding": -500.0004408991089,
    "funding_events": 917,
    "proxy_events": 917,
    "turnover": 835.1039726772283,
    "holding_seconds": 27851640,
    "directions": {
      "long": {
        "trades": 301,
        "net": -1138.55158851933,
        "gross": 1668.1404408531857,
        "fees": 2087.8038483619857,
        "funding": -718.8881810105288
      },
      "short": {
        "trades": 257,
        "net": -2050.618603522408,
        "gross": -599.3423149482832,
        "fees": 1670.1640286855438,
        "funding": 218.887740111419
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
      },
      {
        "month": "2023-01",
        "return_pct": 9.449646075002583,
        "end_equity": 6195.255243974766
      },
      {
        "month": "2023-02",
        "return_pct": 3.9444861577582424,
        "end_equity": 6439.626229511142
      },
      {
        "month": "2023-03",
        "return_pct": 11.682278533074486,
        "end_equity": 7191.921302131556
      },
      {
        "month": "2023-04",
        "return_pct": -4.716152671114216,
        "end_equity": 6852.7393135366465
      },
      {
        "month": "2023-05",
        "return_pct": -7.779433175066575,
        "end_equity": 6319.635037978547
      },
      {
        "month": "2023-06",
        "return_pct": 7.77251798605203,
        "end_equity": 6810.829807958276
      }
    ],
    "max_accounting_error": 1.9099388737231493e-11,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/32a12c2b-8c77-46b8-92b6-a905f6577c3d"
  },
  {
    "name": "s1",
    "session_id": "2e11d184-8f0e-41d4-bbd0-36f60b08c1c8",
    "title": "MCP Backtest: WFV1 E4T H1_PF",
    "trades": 545,
    "net": -3828.0532328060017,
    "net_pct": -38.28053232806002,
    "pf": 0.9113954394597384,
    "dd": -61.351792363467396,
    "gross_price": 52.86151610296287,
    "fees": 3411.0492484608326,
    "funding": -469.8655004481303,
    "funding_events": 898,
    "proxy_events": 898,
    "turnover": 758.0109441024068,
    "holding_seconds": 27258000,
    "directions": {
      "long": {
        "trades": 296,
        "net": -1727.416987339618,
        "gross": 841.7703345452499,
        "fees": 1901.2047401074058,
        "funding": -667.9825817774596
      },
      "short": {
        "trades": 249,
        "net": -2100.6362454663836,
        "gross": -788.9088184422885,
        "fees": 1509.8445083534255,
        "funding": 198.1170813293289
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
      },
      {
        "month": "2023-01",
        "return_pct": 11.661782481600923,
        "end_equity": 5752.70625653352
      },
      {
        "month": "2023-02",
        "return_pct": 1.4410476077754142,
        "end_equity": 5835.605492425643
      },
      {
        "month": "2023-03",
        "return_pct": 11.681476260683521,
        "end_equity": 6517.290362690489
      },
      {
        "month": "2023-04",
        "return_pct": -4.716152479124103,
        "end_equity": 6209.925011678745
      },
      {
        "month": "2023-05",
        "return_pct": -7.77943318272375,
        "end_equity": 5726.828044697947
      },
      {
        "month": "2023-06",
        "return_pct": 7.772517683819102,
        "end_equity": 6171.9467671940065
      }
    ],
    "max_accounting_error": 8.185452315956354e-12,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/2e11d184-8f0e-41d4-bbd0-36f60b08c1c8"
  },
  {
    "name": "s2",
    "session_id": "34995866-f432-45ce-9611-93ae23b9b91c",
    "title": "MCP Backtest: WFV1 E4T H1_POI",
    "trades": 391,
    "net": 732.6902740556077,
    "net_pct": 7.326902740556084,
    "pf": 1.0175783915451857,
    "dd": -36.55693735906337,
    "gross_price": 4653.779972240009,
    "fees": 3516.133922622011,
    "funding": -404.9557755623887,
    "funding_events": 646,
    "proxy_events": 646,
    "turnover": 781.3630939160031,
    "holding_seconds": 19898760,
    "directions": {
      "long": {
        "trades": 226,
        "net": 252.84847127414258,
        "gross": 2927.2684173838647,
        "fees": 2051.3290560234304,
        "funding": -623.0908900862929
      },
      "short": {
        "trades": 165,
        "net": 479.84180278146505,
        "gross": 1726.5115548561423,
        "fees": 1464.8048665985818,
        "funding": 218.13511452390415
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
      },
      {
        "month": "2023-01",
        "return_pct": 4.873605927433267,
        "end_equity": 10055.089517806618
      },
      {
        "month": "2023-02",
        "return_pct": 6.2602038164400575,
        "end_equity": 10684.558615546812
      },
      {
        "month": "2023-03",
        "return_pct": 2.246009444406849,
        "end_equity": 10924.534811145179
      },
      {
        "month": "2023-04",
        "return_pct": -3.781988805319758,
        "end_equity": 10511.370127554408
      },
      {
        "month": "2023-05",
        "return_pct": -3.342819111161277,
        "end_equity": 10159.994038085622
      },
      {
        "month": "2023-06",
        "return_pct": 5.636777283758221,
        "end_equity": 10732.690274055623
      }
    ],
    "max_accounting_error": 1.6370904631912708e-11,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/34995866-f432-45ce-9611-93ae23b9b91c"
  },
  {
    "name": "s3",
    "session_id": "3aeb8ed2-0c9b-4e79-96b5-4aea50a50f6c",
    "title": "MCP Backtest: WFV1 E4T H1_PFOI",
    "trades": 383,
    "net": -116.05417413228386,
    "net_pct": -1.1605417413228338,
    "pf": 0.9971312121647027,
    "dd": -35.458322558970764,
    "gross_price": 3648.1182102764556,
    "fees": 3377.3557536119356,
    "funding": -386.81663079680635,
    "funding_events": 633,
    "proxy_events": 633,
    "turnover": 750.5235008026517,
    "holding_seconds": 19490460,
    "directions": {
      "long": {
        "trades": 223,
        "net": 38.58908459094846,
        "gross": 2614.4144372235396,
        "fees": 1980.6238668483047,
        "funding": -595.2014857842889
      },
      "short": {
        "trades": 160,
        "net": -154.64325872323192,
        "gross": 1033.7037730529134,
        "fees": 1396.7318867636293,
        "funding": 208.38485498748238
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
      },
      {
        "month": "2023-01",
        "return_pct": 6.993254159082207,
        "end_equity": 9855.697047980793
      },
      {
        "month": "2023-02",
        "return_pct": 3.2725376516806293,
        "end_equity": 10178.228444711542
      },
      {
        "month": "2023-03",
        "return_pct": 2.2460094282668708,
        "end_equity": 10406.832415210303
      },
      {
        "month": "2023-04",
        "return_pct": -3.7819888170307125,
        "end_equity": 10013.247177059922
      },
      {
        "month": "2023-05",
        "return_pct": -6.558397803842697,
        "end_equity": 9356.538594106283
      },
      {
        "month": "2023-06",
        "return_pct": 5.636777174132246,
        "end_equity": 9883.94582586774
      }
    ],
    "max_accounting_error": 2.3646862246096134e-11,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/3aeb8ed2-0c9b-4e79-96b5-4aea50a50f6c"
  },
  {
    "name": "s4",
    "session_id": "0277973d-e8af-4e40-8d90-47429c3d040b",
    "title": "MCP Backtest: WFV1 E4T H2_P",
    "trades": 209,
    "net": -3863.1618014776623,
    "net_pct": -38.63161801477664,
    "pf": 0.7685729206505826,
    "dd": -42.037008618527985,
    "gross_price": -2597.641927931831,
    "fees": 1355.2431258420697,
    "funding": 89.72325229623738,
    "funding_events": 335,
    "proxy_events": 335,
    "turnover": 301.16513907601575,
    "holding_seconds": 10489500,
    "directions": {
      "short": {
        "trades": 112,
        "net": -2048.206796283189,
        "gross": -1533.6610863934318,
        "fees": 726.7215494815179,
        "funding": 212.17583959176196
      },
      "long": {
        "trades": 97,
        "net": -1814.955005194475,
        "gross": -1063.980841538399,
        "fees": 628.521576360552,
        "funding": -122.4525872955244
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
      },
      {
        "month": "2023-01",
        "return_pct": -3.939258649344002,
        "end_equity": 6368.858542133252
      },
      {
        "month": "2023-02",
        "return_pct": -6.430431631312594,
        "end_equity": 5959.313447886361
      },
      {
        "month": "2023-03",
        "return_pct": 0.5507271098904809,
        "end_equity": 5992.133002607221
      },
      {
        "month": "2023-04",
        "return_pct": -0.059718185161017345,
        "end_equity": 5988.5546095256295
      },
      {
        "month": "2023-05",
        "return_pct": 5.091656145067858,
        "end_equity": 6293.471218302286
      },
      {
        "month": "2023-06",
        "return_pct": -2.488817607117211,
        "end_equity": 6136.838198522324
      }
    ],
    "max_accounting_error": 1.3642420526593924e-11,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/0277973d-e8af-4e40-8d90-47429c3d040b"
  },
  {
    "name": "s5",
    "session_id": "713a0888-ca63-4b98-ab26-165a83f57b0d",
    "title": "MCP Backtest: WFV1 E4T H2_PF",
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
      },
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2023-02",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2023-03",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2023-04",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2023-05",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 9492.541179399137
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/713a0888-ca63-4b98-ab26-165a83f57b0d"
  },
  {
    "name": "s10",
    "session_id": "18d403c9-9f86-4f3f-9253-c0d601884718",
    "title": "MCP Backtest: WFV1 E4T H3_POI",
    "trades": 732,
    "net": -3513.9342839033325,
    "net_pct": -35.1393428390333,
    "pf": 0.9295045591568297,
    "dd": -59.66059736510242,
    "gross_price": 932.3945723595892,
    "fees": 4072.218649150979,
    "funding": -374.11020711194,
    "funding_events": 1211,
    "proxy_events": 1211,
    "turnover": 904.9374775891043,
    "holding_seconds": 38364780,
    "directions": {
      "short": {
        "trades": 339,
        "net": -1289.8633930882875,
        "gross": 215.07386115918615,
        "fees": 1833.3721184239018,
        "funding": 328.4348641764276
      },
      "long": {
        "trades": 393,
        "net": -2224.0708908150427,
        "gross": 717.3207112004047,
        "fees": 2238.8465307270762,
        "funding": -702.5450712883664
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
        "return_pct": 3.1484099640345375,
        "end_equity": 4598.168424696121
      },
      {
        "month": "2023-01",
        "return_pct": 4.49751471843991,
        "end_equity": 4804.971726375486
      },
      {
        "month": "2023-02",
        "return_pct": 3.8256117194744865,
        "end_equity": 4988.7912878571415
      },
      {
        "month": "2023-03",
        "return_pct": 11.493284833744543,
        "end_equity": 5562.167280331595
      },
      {
        "month": "2023-04",
        "return_pct": -0.5060103756280299,
        "end_equity": 5534.02213678333
      },
      {
        "month": "2023-05",
        "return_pct": 0.5408050449403845,
        "end_equity": 5563.950407687172
      },
      {
        "month": "2023-06",
        "return_pct": 16.57303248309865,
        "end_equity": 6486.065716096667
      }
    ],
    "max_accounting_error": 2.7284841053187847e-12,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/18d403c9-9f86-4f3f-9253-c0d601884718"
  },
  {
    "name": "s11",
    "session_id": "2f3bada8-e82b-4268-a59d-c3338bc359b1",
    "title": "MCP Backtest: WFV1 E4T H3_PFOI",
    "trades": 34,
    "net": -2208.709221833418,
    "net_pct": -22.087092218334185,
    "pf": 0.4353837709012337,
    "dd": -22.23841616750003,
    "gross_price": -2062.088953682371,
    "fees": 255.51092282115772,
    "funding": 108.89065467011034,
    "funding_events": 60,
    "proxy_events": 60,
    "turnover": 56.78020507136836,
    "holding_seconds": 1820580,
    "directions": {
      "long": {
        "trades": 11,
        "net": -641.1762584466592,
        "gross": -561.6212632403463,
        "fees": 86.5266604546043,
        "funding": 6.971665248291484
      },
      "short": {
        "trades": 23,
        "net": -1567.5329633867589,
        "gross": -1500.467690442025,
        "fees": 168.9842623665534,
        "funding": 101.91898942181888
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
      },
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 8112.872184436363
      },
      {
        "month": "2023-02",
        "return_pct": 0,
        "end_equity": 8112.872184436363
      },
      {
        "month": "2023-03",
        "return_pct": 0,
        "end_equity": 8112.872184436363
      },
      {
        "month": "2023-04",
        "return_pct": 0,
        "end_equity": 8112.872184436363
      },
      {
        "month": "2023-05",
        "return_pct": -3.9638416452152936,
        "end_equity": 7791.290778166586
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 7791.290778166586
      }
    ],
    "max_accounting_error": 4.547473508864641e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/2f3bada8-e82b-4268-a59d-c3338bc359b1"
  },
  {
    "name": "s6",
    "session_id": "7c992620-282b-41ef-b10f-05465afdf269",
    "title": "MCP Backtest: WFV1 E4T H2_POI",
    "trades": 111,
    "net": -964.8368051290474,
    "net_pct": -9.648368051290475,
    "pf": 0.9103792740905859,
    "dd": -29.396256910803608,
    "gross_price": -119.65894830833629,
    "fees": 914.3083430808464,
    "funding": 69.13048626013511,
    "funding_events": 178,
    "proxy_events": 178,
    "turnover": 203.17963179574363,
    "holding_seconds": 5607900,
    "directions": {
      "short": {
        "trades": 62,
        "net": -372.75454494629025,
        "gross": -16.928699842458528,
        "fees": 506.6429204389047,
        "funding": 150.81707533507307
      },
      "long": {
        "trades": 49,
        "net": -592.0822601827576,
        "gross": -102.73024846587879,
        "fees": 407.6654226419415,
        "funding": -81.68658907493787
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
      },
      {
        "month": "2023-01",
        "return_pct": -2.4435715093609645,
        "end_equity": 8772.214678117005
      },
      {
        "month": "2023-02",
        "return_pct": -2.5912127959555664,
        "end_equity": 8544.907928888944
      },
      {
        "month": "2023-03",
        "return_pct": 1.7412021372734232,
        "end_equity": 8693.692048374805
      },
      {
        "month": "2023-04",
        "return_pct": -0.002530832526792537,
        "end_equity": 8693.472025588666
      },
      {
        "month": "2023-05",
        "return_pct": 4.126800302470723,
        "end_equity": 9052.234255435867
      },
      {
        "month": "2023-06",
        "return_pct": -0.18858394605355544,
        "end_equity": 9035.163194870955
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/7c992620-282b-41ef-b10f-05465afdf269"
  },
  {
    "name": "s7",
    "session_id": "e0e8d591-8633-4a09-b874-4d30d8299963",
    "title": "MCP Backtest: WFV1 E4T H2_PFOI",
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
      },
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2023-02",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2023-03",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2023-04",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2023-05",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 9929.798900048087
      }
    ],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H2_PFOI",
    "strategy": "ResearchV1_H2_PFOI_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/e0e8d591-8633-4a09-b874-4d30d8299963"
  },
  {
    "name": "s8",
    "session_id": "dedaac18-1491-478d-92dd-3ba9913efdb8",
    "title": "MCP Backtest: WFV1 E4T H3_P",
    "trades": 989,
    "net": -6630.932047940785,
    "net_pct": -66.3093204794078,
    "pf": 0.9024473655668995,
    "dd": -78.54109243247602,
    "gross_price": -806.8898786378867,
    "fees": 5385.194167024451,
    "funding": -438.84800227844204,
    "funding_events": 1639,
    "proxy_events": 1639,
    "turnover": 1196.7098148943217,
    "holding_seconds": 51911160,
    "directions": {
      "long": {
        "trades": 508,
        "net": -3721.425353485241,
        "gross": 12.379258351857809,
        "fees": 2821.986472612502,
        "funding": -911.8181392245933
      },
      "short": {
        "trades": 481,
        "net": -2909.5066944555415,
        "gross": -819.2691369897436,
        "fees": 2563.2076944119467,
        "funding": 472.9701369461521
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
        "return_pct": -4.548773003337791,
        "end_equity": 3393.0894115268293
      },
      {
        "month": "2023-01",
        "return_pct": 5.409295839172645,
        "end_equity": 3576.6316558839576
      },
      {
        "month": "2023-02",
        "return_pct": -5.301541215063854,
        "end_equity": 3387.015054536249
      },
      {
        "month": "2023-03",
        "return_pct": 3.321980768021704,
        "end_equity": 3499.531043257943
      },
      {
        "month": "2023-04",
        "return_pct": 5.797698353617542,
        "end_equity": 3702.4232969372433
      },
      {
        "month": "2023-05",
        "return_pct": -7.82658024116113,
        "end_equity": 3412.6501667350067
      },
      {
        "month": "2023-06",
        "return_pct": -1.2770782982852613,
        "end_equity": 3369.067952059238
      }
    ],
    "max_accounting_error": 2.319211489520967e-11,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/dedaac18-1491-478d-92dd-3ba9913efdb8"
  },
  {
    "name": "s9",
    "session_id": "76f47461-5b27-4ca6-af5e-4e322d487e32",
    "title": "MCP Backtest: WFV1 E4T H3_PF",
    "trades": 57,
    "net": -2497.280367858056,
    "net_pct": -24.972803678580554,
    "pf": 0.5972167698515495,
    "dd": -27.76594054814854,
    "gross_price": -2212.9880350377234,
    "fees": 429.18181179130085,
    "funding": 144.8894789709687,
    "funding_events": 90,
    "proxy_events": 90,
    "turnover": 95.37373595362243,
    "holding_seconds": 2770200,
    "directions": {
      "short": {
        "trades": 39,
        "net": -2109.4058257765046,
        "gross": -1955.4423253394118,
        "fees": 292.56399039195213,
        "funding": 138.6004899548591
      },
      "long": {
        "trades": 18,
        "net": -387.8745420815503,
        "gross": -257.54570969831116,
        "fees": 136.61782139934868,
        "funding": 6.28898901610954
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
      },
      {
        "month": "2023-01",
        "return_pct": 0,
        "end_equity": 8105.092413832003
      },
      {
        "month": "2023-02",
        "return_pct": -1.9999999669337964,
        "end_equity": 7942.990568235409
      },
      {
        "month": "2023-03",
        "return_pct": -1.9902989996386733,
        "end_equity": 7784.901306414426
      },
      {
        "month": "2023-04",
        "return_pct": 0.8159457577985307,
        "end_equity": 7848.421878372916
      },
      {
        "month": "2023-05",
        "return_pct": -4.404735774762337,
        "end_equity": 7502.71963214195
      },
      {
        "month": "2023-06",
        "return_pct": 0,
        "end_equity": 7502.71963214195
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E4T",
    "dashboard_url": "http://localhost:9200/#/backtest/76f47461-5b27-4ca6-af5e-4e322d487e32"
  }
]
```
