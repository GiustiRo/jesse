# BTC R1 calendar friction audit

Job b103dc4be3a245e4a4c0f1b135b9a91b succeeded. Applies +5/+10bps round trip extra proportional cost to each actual entry/exit execution, retaining executed prices, timestamps, quantities and source marks; recomputes MTM and calendar returns. Not a new engine backtest, no resizing/latency/gap/funding model. Base fee .00045 per side; +5RT means extra .00025 per side, +10RT extra .0005. All fill/fee/PNL/equity reconciliations passed after overlays. Terminal open_pl is gross mark profit and retained unchanged; forced full closes still reconciled. 61complete calendar months/19quarters;63including boundary months/21quarters. Tiny monthly returns flagged separately, no silent threshold change. Conclusions: incremental net positive under costs; regularity objective fails at +5RT. Supplemental short MARKET cohort stress and exclusions included, not fixed-capital replay.

```json
{
  "assumption": "Static same executed fills, quantities, timestamps and source marks. Additional proportional cost applied at each entry/exit execution; no strategy rerun, resizing, spread/gap latency or funding model.",
  "rows": [
    {
      "name": "B",
      "extra_bps_RT": 0,
      "extra_cost": 0,
      "net": 9234.194391279196,
      "cagr_samefills_pct": 13.366850134409681,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 37,
        "win_months_all": 0.6065573770491803,
        "win_months_active": 0.6491228070175439,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 37,
        "win_months_active": 0.6271186440677966,
        "win_months_all": 0.5873015873015873,
        "quarters_total": 21,
        "positive_quarters": 17,
        "win_quarters": 0.8095238095238095
      },
      "dayclose_DD": -7.486828490893316,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.043935167167247435
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.051311512385931124,
        "2021-12-31 00:00:00+00:00": 0.150040152048192,
        "2022-12-31 00:00:00+00:00": 0.03105595985992382,
        "2023-12-31 00:00:00+00:00": 0.1717661603955667,
        "2024-12-31 00:00:00+00:00": 0.16799427204987905,
        "2025-12-31 00:00:00+00:00": 0.1273679280962139
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "B",
      "extra_bps_RT": 5,
      "extra_cost": 756.622683769078,
      "net": 8477.571707510118,
      "cagr_samefills_pct": 12.497568466467811,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 36,
        "win_months_all": 0.5901639344262295,
        "win_months_active": 0.631578947368421,
        "quarters_total": 19,
        "positive_quarters": 13,
        "win_quarters": 0.6842105263157895
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 36,
        "win_months_active": 0.6101694915254238,
        "win_months_all": 0.5714285714285714,
        "quarters_total": 21,
        "positive_quarters": 14,
        "win_quarters": 0.6666666666666666
      },
      "dayclose_DD": -7.8438080549544935,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.044983658029634666
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.049507532431819046,
        "2021-12-31 00:00:00+00:00": 0.14276433353283147,
        "2022-12-31 00:00:00+00:00": 0.02669782905098539,
        "2023-12-31 00:00:00+00:00": 0.15909617125705622,
        "2024-12-31 00:00:00+00:00": 0.15991188843950854,
        "2025-12-31 00:00:00+00:00": 0.11613196075152121
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "B",
      "extra_bps_RT": 10,
      "extra_cost": 1513.245367538156,
      "net": 7720.94902374104,
      "cagr_samefills_pct": 11.599025605732493,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 36,
        "win_months_all": 0.5901639344262295,
        "win_months_active": 0.631578947368421,
        "quarters_total": 19,
        "positive_quarters": 13,
        "win_quarters": 0.6842105263157895
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 36,
        "win_months_active": 0.6101694915254238,
        "win_months_all": 0.5714285714285714,
        "quarters_total": 21,
        "positive_quarters": 14,
        "win_quarters": 0.6666666666666666
      },
      "dayclose_DD": -8.336154353999191,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.04604230119326247
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04770355247770652,
        "2021-12-31 00:00:00+00:00": 0.1354634593980253,
        "2022-12-31 00:00:00+00:00": 0.022268549352002953,
        "2023-12-31 00:00:00+00:00": 0.14610864841796012,
        "2024-12-31 00:00:00+00:00": 0.15144147315794143,
        "2025-12-31 00:00:00+00:00": 0.10418727971518371
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "C",
      "extra_bps_RT": 0,
      "extra_cost": 0,
      "net": 9407.82622551297,
      "cagr_samefills_pct": 13.56242675878294,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6666666666666666,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 38,
        "win_months_active": 0.6440677966101694,
        "win_months_all": 0.6031746031746031,
        "quarters_total": 21,
        "positive_quarters": 17,
        "win_quarters": 0.8095238095238095
      },
      "dayclose_DD": -8.227718310465637,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.046955269279550294
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05042509079164881,
        "2021-12-31 00:00:00+00:00": 0.1289562627480143,
        "2022-12-31 00:00:00+00:00": 0.03385041284816226,
        "2023-12-31 00:00:00+00:00": 0.2156127969639383,
        "2024-12-31 00:00:00+00:00": 0.16244301612112677,
        "2025-12-31 00:00:00+00:00": 0.120237352609321
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "C",
      "extra_bps_RT": 5,
      "extra_cost": 807.6485648759723,
      "net": 8600.177660636999,
      "cagr_samefills_pct": 12.640360000728744,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6666666666666666,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 38,
        "win_months_active": 0.6440677966101694,
        "win_months_all": 0.6031746031746031,
        "quarters_total": 21,
        "positive_quarters": 16,
        "win_quarters": 0.7619047619047619
      },
      "dayclose_DD": -8.498247627607947,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.048831713699458934
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.048621051418056505,
        "2021-12-31 00:00:00+00:00": 0.12060524347201129,
        "2022-12-31 00:00:00+00:00": 0.029259247075399175,
        "2023-12-31 00:00:00+00:00": 0.20252722815327107,
        "2024-12-31 00:00:00+00:00": 0.15398222744004642,
        "2025-12-31 00:00:00+00:00": 0.10822273067436461
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "C",
      "extra_bps_RT": 10,
      "extra_cost": 1615.2971297519446,
      "net": 7792.529095761026,
      "cagr_samefills_pct": 11.685345697070382,
      "full": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6666666666666666,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "partial": {
        "months_total": 63,
        "months_active": 59,
        "positive_months": 38,
        "win_months_active": 0.6440677966101694,
        "win_months_all": 0.6031746031746031,
        "quarters_total": 21,
        "positive_quarters": 16,
        "win_quarters": 0.7619047619047619
      },
      "dayclose_DD": -8.77032768117909,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.05072097163105915
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04681701204446376,
        "2021-12-31 00:00:00+00:00": 0.11222544062178286,
        "2022-12-31 00:00:00+00:00": 0.02458295550950762,
        "2023-12-31 00:00:00+00:00": 0.1890784821453031,
        "2024-12-31 00:00:00+00:00": 0.14509257508571283,
        "2025-12-31 00:00:00+00:00": 0.09540783388774066
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03B",
      "extra_bps_RT": 0,
      "extra_cost": 0,
      "net": 11964.238131473841,
      "cagr_samefills_pct": 16.289896060619434,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 41,
        "win_months_all": 0.6721311475409836,
        "win_months_active": 0.6721311475409836,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 41,
        "win_months_active": 0.6507936507936508,
        "win_months_all": 0.6507936507936508,
        "quarters_total": 21,
        "positive_quarters": 17,
        "win_quarters": 0.8095238095238095
      },
      "dayclose_DD": -8.313517098246948,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.03866087934727458
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.044393834400308974,
        "2021-12-31 00:00:00+00:00": 0.19538541122463315,
        "2022-12-31 00:00:00+00:00": 0.09729981207045735,
        "2023-12-31 00:00:00+00:00": 0.18471075133158932,
        "2024-12-31 00:00:00+00:00": 0.14110930366617258,
        "2025-12-31 00:00:00+00:00": 0.18598449742342904
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03B",
      "extra_bps_RT": 5,
      "extra_cost": 1043.0576277989555,
      "net": 10921.180503674886,
      "cagr_samefills_pct": 15.209742380016156,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 40,
        "win_months_all": 0.6557377049180327,
        "win_months_active": 0.6557377049180327,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 40,
        "win_months_active": 0.6349206349206349,
        "win_months_all": 0.6349206349206349,
        "quarters_total": 21,
        "positive_quarters": 16,
        "win_quarters": 0.7619047619047619
      },
      "dayclose_DD": -8.561155259333397,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.03989429129023714
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.042522490982412675,
        "2021-12-31 00:00:00+00:00": 0.1871943868952155,
        "2022-12-31 00:00:00+00:00": 0.09039925971165319,
        "2023-12-31 00:00:00+00:00": 0.16741453791584693,
        "2024-12-31 00:00:00+00:00": 0.13155434771245123,
        "2025-12-31 00:00:00+00:00": 0.17352637805450755
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03B",
      "extra_bps_RT": 10,
      "extra_cost": 2086.115255597911,
      "net": 9878.12287587593,
      "cagr_samefills_pct": 14.085149900684456,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 37,
        "win_months_all": 0.6065573770491803,
        "win_months_active": 0.6065573770491803,
        "quarters_total": 19,
        "positive_quarters": 14,
        "win_quarters": 0.7368421052631579
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 37,
        "win_months_active": 0.5873015873015873,
        "win_months_all": 0.5873015873015873,
        "quarters_total": 21,
        "positive_quarters": 15,
        "win_quarters": 0.7142857142857143
      },
      "dayclose_DD": -9.289238200757977,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.04113547896187042
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.040651147564516155,
        "2021-12-31 00:00:00+00:00": 0.17897390366499266,
        "2022-12-31 00:00:00+00:00": 0.08337748734323824,
        "2023-12-31 00:00:00+00:00": 0.14958831124970895,
        "2024-12-31 00:00:00+00:00": 0.12140572590037002,
        "2025-12-31 00:00:00+00:00": 0.16006171951631765
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03C",
      "extra_bps_RT": 0,
      "extra_cost": 0,
      "net": 12135.87683397664,
      "cagr_samefills_pct": 16.4636473319147,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 42,
        "win_months_all": 0.6885245901639344,
        "win_months_active": 0.6885245901639344,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 42,
        "win_months_active": 0.6666666666666666,
        "win_months_all": 0.6666666666666666,
        "quarters_total": 21,
        "positive_quarters": 17,
        "win_quarters": 0.8095238095238095
      },
      "dayclose_DD": -9.068338000418485,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.04681257194932276
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04350741280602666,
        "2021-12-31 00:00:00+00:00": 0.17331613097535925,
        "2022-12-31 00:00:00+00:00": 0.10035814679276234,
        "2023-12-31 00:00:00+00:00": 0.2280277763588845,
        "2024-12-31 00:00:00+00:00": 0.13606292932860486,
        "2025-12-31 00:00:00+00:00": 0.17771852861184967
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03C",
      "extra_bps_RT": 5,
      "extra_cost": 1096.9324048528927,
      "net": 11038.944429123747,
      "cagr_samefills_pct": 15.333845792583523,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 40,
        "win_months_all": 0.6557377049180327,
        "win_months_active": 0.6557377049180327,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 40,
        "win_months_active": 0.6349206349206349,
        "win_months_all": 0.6349206349206349,
        "quarters_total": 21,
        "positive_quarters": 16,
        "win_quarters": 0.7619047619047619
      },
      "dayclose_DD": -9.350075493252474,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.04869409171512318
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.041636009968650134,
        "2021-12-31 00:00:00+00:00": 0.16407924144624397,
        "2022-12-31 00:00:00+00:00": 0.09328659161629327,
        "2023-12-31 00:00:00+00:00": 0.21044612243813043,
        "2024-12-31 00:00:00+00:00": 0.12603255926715007,
        "2025-12-31 00:00:00+00:00": 0.16438065856663142
      },
      "numerical_nearzero_months": {}
    },
    {
      "name": "X03C",
      "extra_bps_RT": 10,
      "extra_cost": 2193.8648097057853,
      "net": 9942.012024270854,
      "cagr_samefills_pct": 14.155387812142672,
      "full": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6229508196721312,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "partial": {
        "months_total": 63,
        "months_active": 63,
        "positive_months": 38,
        "win_months_active": 0.6031746031746031,
        "win_months_all": 0.6031746031746031,
        "quarters_total": 21,
        "positive_quarters": 16,
        "win_quarters": 0.7619047619047619
      },
      "dayclose_DD": -9.633544083781675,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.05058924688599109
      ],
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.03976460713127339,
        "2021-12-31 00:00:00+00:00": 0.15480910219665378,
        "2022-12-31 00:00:00+00:00": 0.08607584415454417,
        "2023-12-31 00:00:00+00:00": 0.19228264548306173,
        "2024-12-31 00:00:00+00:00": 0.11535959184253675,
        "2025-12-31 00:00:00+00:00": 0.14992485655167842
      },
      "numerical_nearzero_months": {}
    }
  ],
  "supplement_BTC_short_MARKET": {
    "B": {
      "n": 0,
      "net": 0,
      "fees": 0,
      "plus10": 0,
      "exbest": 0,
      "ex3": 0,
      "ex3_plus10": 0,
      "year_net": {},
      "year_plus10": {}
    },
    "C": {
      "n": 0,
      "net": 0,
      "fees": 0,
      "plus10": 0,
      "exbest": 0,
      "ex3": 0,
      "ex3_plus10": 0,
      "year_net": {},
      "year_plus10": {}
    },
    "X03B": {
      "n": 79,
      "net": 2107.7617660663623,
      "fees": 465.81581017968944,
      "plus10": 1590.1886436444843,
      "exbest": 1724.487261185343,
      "ex3": 1069.6463356660092,
      "ex3_plus10": 578.6665878103804,
      "year_net": {
        "2020": -65.09905435199995,
        "2021": 393.89799891328573,
        "2022": 856.2693321268378,
        "2023": 186.42086671713434,
        "2024": -89.88238715141927,
        "2025": 826.1550098125232
      },
      "year_plus10": {
        "2020": -66.57160363199995,
        "2021": 353.1829973234578,
        "2022": 763.2553293241624,
        "2023": 46.16911233996262,
        "2024": -180.45314950193722,
        "2025": 674.6059577908393
      }
    },
    "X03C": {
      "n": 79,
      "net": 2087.167949436408,
      "fees": 464.40193910015853,
      "plus10": 1571.165794880677,
      "exbest": 1698.7831178236474,
      "ex3": 1033.9446644103994,
      "ex3_plus10": 544.9278156245584,
      "year_net": {
        "2020": -65.09905435199995,
        "2021": 385.84530313242715,
        "2022": 842.3328739968498,
        "2023": 182.51484543477295,
        "2024": -91.04045203698251,
        "2025": 832.6144332613408
      },
      "year_plus10": {
        "2020": -66.57160363199995,
        "2021": 345.81016563586684,
        "2022": 751.0389607548072,
        "2023": 45.629047066755874,
        "2024": -183.30511126634804,
        "2025": 678.5643363215944
      }
    }
  },
  "positive_to_nonpositive_month_flips": {
    "B_cost5": [
      {
        "month": "2023-11-30 00:00:00+00:00",
        "base": 0.00014420269650439188,
        "stress": -0.0009838071056447184
      }
    ],
    "B_cost10": [
      {
        "month": "2023-11-30 00:00:00+00:00",
        "base": 0.00014420269650439188,
        "stress": -0.0021587733966582645
      }
    ],
    "C_cost5": [],
    "C_cost10": [],
    "X03B_cost5": [
      {
        "month": "2025-09-30 00:00:00+00:00",
        "base": 0.0012740638467956256,
        "stress": -0.0004815474542297915
      }
    ],
    "X03B_cost10": [
      {
        "month": "2020-11-30 00:00:00+00:00",
        "base": 0.0013502623752470466,
        "stress": -0.00021192299513395074
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "base": 0.0008813522885573466,
        "stress": -0.0005710085536103637
      },
      {
        "month": "2025-07-31 00:00:00+00:00",
        "base": 0.00286838152164659,
        "stress": -0.0016299621712975165
      },
      {
        "month": "2025-09-30 00:00:00+00:00",
        "base": 0.0012740638467956256,
        "stress": -0.0023947970064573942
      }
    ],
    "X03C_cost5": [
      {
        "month": "2020-11-30 00:00:00+00:00",
        "base": 0.00044888242643503773,
        "stress": -0.00033246392794739066
      },
      {
        "month": "2025-09-30 00:00:00+00:00",
        "base": 0.001322265825600244,
        "stress": -0.0004335574414847665
      }
    ],
    "X03C_cost10": [
      {
        "month": "2020-11-30 00:00:00+00:00",
        "base": 0.00044888242643503773,
        "stress": -0.001114418420340102
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "base": 0.0008807674414230693,
        "stress": -0.0005724218568456951
      },
      {
        "month": "2025-07-31 00:00:00+00:00",
        "base": 0.0028890612084249145,
        "stress": -0.0016079883502595482
      },
      {
        "month": "2025-09-30 00:00:00+00:00",
        "base": 0.001322265825600244,
        "stress": -0.002351639304463138
      }
    ]
  },
  "anchors": {
    "BTC-USDT": {
      "anchor_count": 47,
      "distinct_anchor_timestamps": 32,
      "scale": 1.1501999999999981,
      "max_relative_error": 1.3322676295501878e-15
    },
    "PAXG-USDT": {
      "anchor_count": 24,
      "distinct_anchor_timestamps": 15,
      "scale": 0.19228799999999985,
      "max_relative_error": 1.5543122344752192e-15
    },
    "SPY-USDT": {
      "anchor_count": 17,
      "distinct_anchor_timestamps": 16,
      "scale": 0.034843459999999944,
      "max_relative_error": 1.5543122344752192e-15
    }
  }
}
```