# Walk-forward E1T — selection BEFORE evaluation

Selection: **SIN_CANDIDATA**. Frozen gates and ranking, based only on this train.

| ID | Trades | Net % | PF | DD % | Session |
|---|---:|---:|---:|---:|---|
| H1_P | 284 | -28.63 | 0.907 | -42.72 | [dashboard](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770) |
| H1_PF | 277 | -36.00 | 0.873 | -45.25 | [dashboard](http://localhost:9200/#/backtest/d3ea7127-8add-4952-8143-bf4c26f69958) |
| H1_PFOI | 208 | -9.21 | 0.963 | -34.14 | [dashboard](http://localhost:9200/#/backtest/279d4b93-7932-41a8-9b38-14077469675d) |
| H1_POI | 212 | -6.83 | 0.973 | -33.94 | [dashboard](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644) |
| H2_P | 104 | -26.12 | 0.721 | -33.99 | [dashboard](http://localhost:9200/#/backtest/232577e2-4517-4257-a069-53217d2c6da8) |
| H2_PF | 6 | -3.66 | 0.453 | -6.27 | [dashboard](http://localhost:9200/#/backtest/969b42d2-0136-488e-915c-0065bc61f839) |
| H2_PFOI | 4 | -0.70 | 0.817 | -3.03 | [dashboard](http://localhost:9200/#/backtest/91ad7aa1-3553-44d3-ad00-64777281ce3b) |
| H2_POI | 56 | 3.03 | 1.056 | -15.26 | [dashboard](http://localhost:9200/#/backtest/e7506dac-942f-4cf0-bae7-8608d184490f) |
| H3_P | 476 | -47.05 | 0.905 | -63.28 | [dashboard](http://localhost:9200/#/backtest/db1f164b-17e3-4dac-8580-bbcdcf6815e9) |
| H3_PF | 40 | -19.30 | 0.591 | -26.08 | [dashboard](http://localhost:9200/#/backtest/8b0c6493-efad-40e5-bb12-97a89a821bbb) |
| H3_PFOI | 26 | -18.18 | 0.415 | -22.24 | [dashboard](http://localhost:9200/#/backtest/18c9272f-edd7-481e-8d8b-2a056e136adc) |
| H3_POI | 364 | -42.63 | 0.868 | -48.44 | [dashboard](http://localhost:9200/#/backtest/fdb13394-9dd1-40bf-b0f4-e5136d6c8115) |

All accounting assertions passed within1e-6USDT; sources/config/datasets in registry. Monthly data use stored daily equity samples: UTC00:00/00:01 samples are labeled as the preceding day (61-second shift, initial balance unchanged). Month boundaries are approximate up to one minute; final close belongs to final requested month. Not an intraminute account replay. No2026.

```json
[
  {
    "name": "s0",
    "session_id": "16f2c940-30b1-4bb2-95cb-f25614e88770",
    "title": "MCP Backtest: WFV1 E1T H1_P",
    "trades": 284,
    "net": -2863.2539342278883,
    "net_pct": -28.63253934227886,
    "pf": 0.9067001412450454,
    "dd": -42.718124250199786,
    "gross_price": -79.11610271198262,
    "fees": 2310.6479019426765,
    "funding": -473.4899295732259,
    "funding_events": 421,
    "proxy_events": 421,
    "turnover": 513.4773115428169,
    "holding_seconds": 13012740,
    "directions": {
      "long": {
        "trades": 163,
        "net": -241.54974418802271,
        "gross": 1741.1583534379674,
        "fees": 1352.6865429039415,
        "funding": -630.0215547220477
      },
      "short": {
        "trades": 121,
        "net": -2621.704190039865,
        "gross": -1820.274456149951,
        "fees": 957.9613590387346,
        "funding": 156.53162514882158
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
      }
    ],
    "max_accounting_error": 7.275957614183426e-12,
    "eligible": false,
    "id": "H1_P",
    "strategy": "ResearchV1_H1_P_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770"
  },
  {
    "name": "s1",
    "session_id": "d3ea7127-8add-4952-8143-bf4c26f69958",
    "title": "MCP Backtest: WFV1 E1T H1_PF",
    "trades": 277,
    "net": -3599.9847458224795,
    "net_pct": -35.999847458224785,
    "pf": 0.873383717623907,
    "dd": -45.252507574734025,
    "gross_price": -1057.4126011679216,
    "fees": 2101.0216560149806,
    "funding": -441.5504886395763,
    "funding_events": 412,
    "proxy_events": 412,
    "turnover": 466.893701336662,
    "holding_seconds": 12713160,
    "directions": {
      "long": {
        "trades": 158,
        "net": -861.5413577589682,
        "gross": 946.1738209897595,
        "fees": 1221.7345376762203,
        "funding": -585.9806410725049
      },
      "short": {
        "trades": 119,
        "net": -2738.4433880635106,
        "gross": -2003.5864221576805,
        "fees": 879.2871183387592,
        "funding": 144.4301524329286
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
      }
    ],
    "max_accounting_error": 8.185452315956354e-12,
    "eligible": false,
    "id": "H1_PF",
    "strategy": "ResearchV1_H1_PF_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/d3ea7127-8add-4952-8143-bf4c26f69958"
  },
  {
    "name": "s2",
    "session_id": "032ec154-d3a3-4aea-b2a0-e4334b705644",
    "title": "MCP Backtest: WFV1 E1T H1_POI",
    "trades": 212,
    "net": -683.3090112483685,
    "net_pct": -6.833090112483683,
    "pf": 0.9729536127280853,
    "dd": -33.938030246411785,
    "gross_price": 1655.6890205945363,
    "fees": 1976.3489836831197,
    "funding": -362.6490481597834,
    "funding_events": 314,
    "proxy_events": 314,
    "turnover": 439.1886630406928,
    "holding_seconds": 9782100,
    "directions": {
      "long": {
        "trades": 124,
        "net": 468.8450718590682,
        "gross": 2148.041891961262,
        "fees": 1166.7909754605291,
        "funding": -512.4058446416661
      },
      "short": {
        "trades": 88,
        "net": -1152.154083107436,
        "gross": -492.352871366728,
        "fees": 809.5580082225904,
        "funding": 149.75679648188256
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
      }
    ],
    "max_accounting_error": 1.4551915228366852e-11,
    "eligible": false,
    "id": "H1_POI",
    "strategy": "ResearchV1_H1_POI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644"
  },
  {
    "name": "s3",
    "session_id": "279d4b93-7932-41a8-9b38-14077469675d",
    "title": "MCP Backtest: WFV1 E1T H1_PFOI",
    "trades": 208,
    "net": -920.566491279046,
    "net_pct": -9.205664912790459,
    "pf": 0.9626092366471086,
    "dd": -34.13818372278813,
    "gross_price": 1328.0559552754332,
    "fees": 1907.5352718455902,
    "funding": -341.08717470889167,
    "funding_events": 307,
    "proxy_events": 307,
    "turnover": 423.89672707679745,
    "holding_seconds": 9534360,
    "directions": {
      "long": {
        "trades": 121,
        "net": 271.61441642116046,
        "gross": 1877.9706139541304,
        "fees": 1118.7517013006188,
        "funding": -487.6044962323518
      },
      "short": {
        "trades": 87,
        "net": -1192.1809077002063,
        "gross": -549.914658678696,
        "fees": 788.7835705449706,
        "funding": 146.51732152346005
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
      }
    ],
    "max_accounting_error": 5.093170329928398e-11,
    "eligible": false,
    "id": "H1_PFOI",
    "strategy": "ResearchV1_H1_PFOI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/279d4b93-7932-41a8-9b38-14077469675d"
  },
  {
    "name": "s4",
    "session_id": "232577e2-4517-4257-a069-53217d2c6da8",
    "title": "MCP Backtest: WFV1 E1T H2_P",
    "trades": 104,
    "net": -2612.275630436136,
    "net_pct": -26.12275630436137,
    "pf": 0.7210353511450345,
    "dd": -33.993214928322956,
    "gross_price": -1994.7059689883656,
    "fees": 698.9554972728916,
    "funding": 81.38583582512084,
    "funding_events": 151,
    "proxy_events": 151,
    "turnover": 155.3234438384205,
    "holding_seconds": 4755120,
    "directions": {
      "short": {
        "trades": 58,
        "net": -1858.1329651148312,
        "gross": -1637.716877066538,
        "fees": 397.58384109751546,
        "funding": 177.1677530492233
      },
      "long": {
        "trades": 46,
        "net": -754.1426653213059,
        "gross": -356.98909192182816,
        "fees": 301.37165617537585,
        "funding": -95.78191722410236
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
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_P",
    "strategy": "ResearchV1_H2_P_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/232577e2-4517-4257-a069-53217d2c6da8"
  },
  {
    "name": "s5",
    "session_id": "969b42d2-0136-488e-915c-0065bc61f839",
    "title": "MCP Backtest: WFV1 E1T H2_PF",
    "trades": 6,
    "net": -366.27296071296394,
    "net_pct": -3.6627296071296396,
    "pf": 0.453144281019228,
    "dd": -6.27208213923951,
    "gross_price": -371.6086007803864,
    "fees": 50.12155891598955,
    "funding": 55.45719898341196,
    "funding_events": 11,
    "proxy_events": 11,
    "turnover": 11.138124203553236,
    "holding_seconds": 311460,
    "directions": {
      "short": {
        "trades": 5,
        "net": -173.61979368589832,
        "gross": -187.02876088916582,
        "fees": 41.8985270488357,
        "funding": 55.3074942521032
      },
      "long": {
        "trades": 1,
        "net": -192.65316702706568,
        "gross": -184.5798398912206,
        "fees": 8.22303186715385,
        "funding": 0.14970473130876277
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
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H2_PF",
    "strategy": "ResearchV1_H2_PF_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/969b42d2-0136-488e-915c-0065bc61f839"
  },
  {
    "name": "s10",
    "session_id": "fdb13394-9dd1-40bf-b0f4-e5136d6c8115",
    "title": "MCP Backtest: WFV1 E1T H3_POI",
    "trades": 364,
    "net": -4263.225401544619,
    "net_pct": -42.63225401544616,
    "pf": 0.8682016541002815,
    "dd": -48.44065613336287,
    "gross_price": -1525.7211907113247,
    "fees": 2393.5986076766403,
    "funding": -343.9056031566511,
    "funding_events": 488,
    "proxy_events": 488,
    "turnover": 531.9108017059195,
    "holding_seconds": 16062840,
    "directions": {
      "short": {
        "trades": 160,
        "net": -1121.7856400689811,
        "gross": -346.79243337416216,
        "fees": 1018.5383831418881,
        "funding": 243.54517644706948
      },
      "long": {
        "trades": 204,
        "net": -3141.4397614756344,
        "gross": -1178.9287573371623,
        "fees": 1375.0602245347518,
        "funding": -587.4507796037204
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
      }
    ],
    "max_accounting_error": 7.275957614183426e-12,
    "eligible": false,
    "id": "H3_POI",
    "strategy": "ResearchV1_H3_POI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/fdb13394-9dd1-40bf-b0f4-e5136d6c8115"
  },
  {
    "name": "s11",
    "session_id": "18c9272f-edd7-481e-8d8b-2a056e136adc",
    "title": "MCP Backtest: WFV1 E1T H3_PFOI",
    "trades": 26,
    "net": -1817.5148225758605,
    "net_pct": -18.175148225758612,
    "pf": 0.4145297997321422,
    "dd": -22.23841616750003,
    "gross_price": -1725.9114185649726,
    "fees": 199.0491586043957,
    "funding": 107.44575459350733,
    "funding_events": 46,
    "proxy_events": 46,
    "turnover": 44.23314635653236,
    "holding_seconds": 1375320,
    "directions": {
      "long": {
        "trades": 7,
        "net": -535.9999196151618,
        "gross": -486.5953488296262,
        "fees": 57.96151791152093,
        "funding": 8.556947125985388
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
      }
    ],
    "max_accounting_error": 1.8189894035458565e-12,
    "eligible": false,
    "id": "H3_PFOI",
    "strategy": "ResearchV1_H3_PFOI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/18c9272f-edd7-481e-8d8b-2a056e136adc"
  },
  {
    "name": "s6",
    "session_id": "e7506dac-942f-4cf0-bae7-8608d184490f",
    "title": "MCP Backtest: WFV1 E1T H2_POI",
    "trades": 56,
    "net": 303.12481544278285,
    "net_pct": 3.0312481544278276,
    "pf": 1.0556577425785647,
    "dd": -15.258958654858013,
    "gross_price": 685.9502798791266,
    "fees": 451.9399572515067,
    "funding": 69.11449281516317,
    "funding_events": 84,
    "proxy_events": 84,
    "turnover": 100.43110161144592,
    "holding_seconds": 2632200,
    "directions": {
      "short": {
        "trades": 33,
        "net": 410.4975901993212,
        "gross": 544.3335903866648,
        "fees": 266.71836526220903,
        "funding": 132.88236507486556
      },
      "long": {
        "trades": 23,
        "net": -107.37277475653869,
        "gross": 141.6166894924613,
        "fees": 185.22159198929768,
        "funding": -63.76787225970237
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
      }
    ],
    "max_accounting_error": 3.637978807091713e-12,
    "eligible": false,
    "id": "H2_POI",
    "strategy": "ResearchV1_H2_POI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/e7506dac-942f-4cf0-bae7-8608d184490f"
  },
  {
    "name": "s7",
    "session_id": "91ad7aa1-3553-44d3-ad00-64777281ce3b",
    "title": "MCP Backtest: WFV1 E1T H2_PFOI",
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
      }
    ],
    "max_accounting_error": 0,
    "eligible": false,
    "id": "H2_PFOI",
    "strategy": "ResearchV1_H2_PFOI_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/91ad7aa1-3553-44d3-ad00-64777281ce3b"
  },
  {
    "name": "s8",
    "session_id": "db1f164b-17e3-4dac-8580-bbcdcf6815e9",
    "title": "MCP Backtest: WFV1 E1T H3_P",
    "trades": 476,
    "net": -4705.016572824229,
    "net_pct": -47.05016572824226,
    "pf": 0.9047087699318614,
    "dd": -63.2789679696164,
    "gross_price": -642.6473211023558,
    "fees": 3659.2312794342083,
    "funding": -403.1379722876617,
    "funding_events": 619,
    "proxy_events": 619,
    "turnover": 813.1625065409346,
    "holding_seconds": 20587500,
    "directions": {
      "long": {
        "trades": 254,
        "net": -2231.4754591085903,
        "gross": 534.0585296278,
        "fees": 1971.5311589051817,
        "funding": -794.0028298312034
      },
      "short": {
        "trades": 222,
        "net": -2473.541113715639,
        "gross": -1176.7058507301545,
        "fees": 1687.700120529025,
        "funding": 390.86485754354226
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
      }
    ],
    "max_accounting_error": 2.546585164964199e-11,
    "eligible": false,
    "id": "H3_P",
    "strategy": "ResearchV1_H3_P_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/db1f164b-17e3-4dac-8580-bbcdcf6815e9"
  },
  {
    "name": "s9",
    "session_id": "8b0c6493-efad-40e5-bb12-97a89a821bbb",
    "title": "MCP Backtest: WFV1 E1T H3_PF",
    "trades": 40,
    "net": -1929.7180379574445,
    "net_pct": -19.297180379574446,
    "pf": 0.5906447064666384,
    "dd": -26.082483251482657,
    "gross_price": -1763.5126462730009,
    "fees": 310.23971895374666,
    "funding": 144.03432726930276,
    "funding_events": 59,
    "proxy_events": 59,
    "turnover": 68.94215976749925,
    "holding_seconds": 1804800,
    "directions": {
      "short": {
        "trades": 32,
        "net": -1471.2905252991736,
        "gross": -1361.2222493903323,
        "fees": 244.0297644979462,
        "funding": 133.9614885891045
      },
      "long": {
        "trades": 8,
        "net": -458.4275126582705,
        "gross": -402.2903968826682,
        "fees": 66.20995445580041,
        "funding": 10.072838680198245
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
      }
    ],
    "max_accounting_error": 5.4569682106375694e-12,
    "eligible": false,
    "id": "H3_PF",
    "strategy": "ResearchV1_H3_PF_E1T",
    "dashboard_url": "http://localhost:9200/#/backtest/8b0c6493-efad-40e5-bb12-97a89a821bbb"
  }
]
```
