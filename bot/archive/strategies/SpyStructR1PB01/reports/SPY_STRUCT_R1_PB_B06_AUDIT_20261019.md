# B06 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B06",
    "url": "http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646",
    "n": 19,
    "net": 571.7530451590001,
    "gross_before_fees": 762.6834330150468,
    "fees": 190.93038785604676,
    "pf": 1.5099082131681496,
    "sharpe": 0.4183644741082198,
    "dd_motor_pct": -6.275390218471532,
    "cagr_motor_pct": 1.0721385292109753,
    "time_exposure_pct": 7.127415776259706,
    "entry_price_notional_time": 0.07979347810998393,
    "mean_hold_hours": 171.3280701754386,
    "turnover_two_sides": 424289.75079121505,
    "total_entry_notional": 211763.53367910002,
    "net_bps_per_entry_notional": 26.99959880842455,
    "net_plus5bpsRT": 465.6806074611963,
    "net_plus10bpsRT": 359.60816976339254,
    "net_exbest": -38.52495342401221,
    "net_ex3best": -610.5712665711965,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 499.259792893952,
        "fees": 18.497734784945507
      },
      "2022": {
        "n": 3,
        "net": -40.098638195967,
        "fees": 16.67368640214278
      },
      "2023": {
        "n": 5,
        "net": 718.4229378075476,
        "fees": 54.72438606813406
      },
      "2024": {
        "n": 6,
        "net": -358.1442335712496,
        "fees": 75.1566280034845
      },
      "2025": {
        "n": 3,
        "net": -247.68681377528299,
        "fees": 25.877952597339924
      }
    },
    "executed_order_types": {
      "MARKET": 20,
      "STOP": 18
    },
    "entry_order_types": {
      "MARKET": 19
    },
    "exit_order_types": {
      "STOP": 18,
      "MARKET": 1
    },
    "terminal_orders": [
      {
        "trade_id": "b4688dcc-d5d1-44f8-a045-2718a2fe20a0",
        "side": "sell",
        "type": "MARKET",
        "gross": 5.624073200000566,
        "net": -4.6486387950994335,
        "fee": 10.2727119951,
        "exit_fee": 5.137621414020001
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "833606fd187d2ca0ea2450022d5e4b88c081103177cd68f54ef01c5c1414843c",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "112778a4-3d47-41f4-a34a-86dc27bcf447",
      "opened_at": 1617811200000.0,
      "closed_at": 1618933920000.0,
      "entry": 408.0145,
      "exit": 413.44940189745466,
      "qty": 28.562,
      "entry_notional": 11653.710149,
      "gross": 155.2316679951,
      "fees": 10.558193384697795,
      "net": 144.6734746104022,
      "hold_hours": 311.8666666666667,
      "net_bps_entry": 124.14370424582471,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5d3ee2bc-b683-4c13-87dc-6ad45fe66798",
      "opened_at": 1634572800000.0,
      "closed_at": 1636567560000.0,
      "entry": 447.2051000000001,
      "exit": 465.96840726586606,
      "qty": 19.321,
      "entry_notional": 8640.449737100002,
      "gross": 362.52585968379753,
      "fees": 7.939541400247711,
      "net": 354.5863182835498,
      "hold_hours": 554.1,
      "net_bps_entry": 410.3794699031023,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "17ce0ef9-a206-453e-a854-690bff457ee7",
      "opened_at": 1659456000000.0,
      "closed_at": 1661122860000.0,
      "entry": 411.5545,
      "exit": 421.4433,
      "qty": 16.868000000000002,
      "entry_notional": 6942.101306000001,
      "gross": 166.80427839999993,
      "fees": 6.322953100680001,
      "net": 160.48132529931993,
      "hold_hours": 463.01666666666665,
      "net_bps_entry": 231.17110832222693,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9d75b95f-feda-4e47-9477-4afb4928e8ee",
      "opened_at": 1668441600000.0,
      "closed_at": 1668690060000.0,
      "entry": 399.1501,
      "exit": 392.0945616739454,
      "qty": 13.647,
      "entry_notional": 5447.2014147,
      "gross": -96.28693153566655,
      "fees": 4.8591521540389495,
      "net": -101.1460836897055,
      "hold_hours": 69.01666666666667,
      "net_bps_entry": -185.6844937232343,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "38073b52-5f12-4b02-860e-fd183e0b0be5",
      "opened_at": 1671033600000.0,
      "closed_at": 1671046500000.0,
      "entry": 404.2822,
      "exit": 398.1054429049801,
      "qty": 15.209,
      "entry_notional": 6148.7279798,
      "gross": -93.9422986581576,
      "fees": 5.491581147423829,
      "net": -99.43387980558143,
      "hold_hours": 3.5833333333333335,
      "net_bps_entry": -161.71455320880162,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "3029bbfd-f902-4016-86be-90c961217fed",
      "opened_at": 1675440000000.0,
      "closed_at": 1675671840000.0,
      "entry": 416.8906,
      "exit": 411.3893749902029,
      "qty": 16.626,
      "entry_notional": 6931.223115600001,
      "gross": -91.46336701288692,
      "fees": 6.196942288884201,
      "net": -97.66030930177112,
      "hold_hours": 64.4,
      "net_bps_entry": -140.89909915317617,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "cab84835-7ba4-4469-bf09-10c47dfd7393",
      "opened_at": 1686067200000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.34899999999993,
      "exit": 437.4708999999999,
      "qty": 24.903000000000002,
      "entry_notional": 10667.175147,
      "gross": 227.16267569999945,
      "fees": 9.702680836365,
      "net": 217.45999486363445,
      "hold_hours": 336.01666666666665,
      "net_bps_entry": 203.8590272184592,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "dffc80b8-3e3d-46c6-a442-4081bb8c96c7",
      "opened_at": 1688572800000.0,
      "closed_at": 1688632560000.0,
      "entry": 445.2962,
      "exit": 442.5017782269619,
      "qty": 29.069,
      "entry_notional": 12944.3152378,
      "gross": -81.23104652044458,
      "fees": 11.613329743085798,
      "net": -92.84437626353038,
      "hold_hours": 16.6,
      "net_bps_entry": -71.72598515864799,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fe9ba7c5-43d5-4603-aeec-ed9b69df8dd9",
      "opened_at": 1689609600000.0,
      "closed_at": 1690486680000.0,
      "entry": 451.3014,
      "exit": 454.30690876106024,
      "qty": 31.251,
      "entry_notional": 14103.620051400001,
      "gross": 93.9251542918937,
      "fees": 12.735524365691353,
      "net": 81.18962992620236,
      "hold_hours": 243.63333333333333,
      "net_bps_entry": 57.56651812109972,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7e729ca4-8193-4464-8d99-3c33a299ef2b",
      "opened_at": 1701187200000.0,
      "closed_at": 1703101920000.0,
      "entry": 455.6923,
      "exit": 473.7430326404068,
      "qty": 34.611000000000004,
      "entry_notional": 15771.966195300001,
      "gross": 624.75390741712,
      "fees": 14.475908834107704,
      "net": 610.2779985830123,
      "hold_hours": 531.8666666666667,
      "net_bps_entry": 386.9384393969049,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8adedb9e-2808-42d4-a141-a1f231a010f9",
      "opened_at": 1706688000000.0,
      "closed_at": 1706727660000.0,
      "entry": 490.8522,
      "exit": 487.7799238034621,
      "qty": 27.919,
      "entry_notional": 13704.1025718,
      "gross": -85.77487913114055,
      "fees": 12.295093619010986,
      "net": -98.06997275015154,
      "hold_hours": 11.016666666666667,
      "net_bps_entry": -71.56249176940472,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "23217d1b-54cf-43fb-b1e0-53bfb7e6c6dd",
      "opened_at": 1707753600000.0,
      "closed_at": 1707814020000.0,
      "entry": 503.4382,
      "exit": 500.7698471658336,
      "qty": 30.575,
      "entry_notional": 15392.622964999999,
      "gross": -81.58488790463707,
      "fees": 13.81664746894291,
      "net": -95.40153537357997,
      "hold_hours": 16.783333333333335,
      "net_bps_entry": -61.97873851032769,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1edbe916-17cf-4cb7-b4b6-bebe692588cb",
      "opened_at": 1709913600000.0,
      "closed_at": 1709920380000.0,
      "entry": 518.2207,
      "exit": 513.9336185901562,
      "qty": 20.843,
      "entry_notional": 10801.274050099999,
      "gross": -89.35563782537247,
      "fees": 9.68093660806858,
      "net": -99.03657443344105,
      "hold_hours": 1.8833333333333333,
      "net_bps_entry": -91.68971546696767,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f96d8db2-404b-418e-899e-83eff43bf0cd",
      "opened_at": 1715702400000.0,
      "closed_at": 1716490620000.0,
      "entry": 522.9647,
      "exit": 527.9046017608516,
      "qty": 27.842000000000002,
      "entry_notional": 14560.383177400001,
      "gross": 137.5367448256311,
      "fees": 13.166236394831536,
      "net": 124.37050843079956,
      "hold_hours": 218.95,
      "net_bps_entry": 85.41705730920742,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e7b7d13b-300f-4e8d-af06-c9b6c9e990c7",
      "opened_at": 1731513600000.0,
      "closed_at": 1731617400000.0,
      "entry": 598.7226,
      "exit": 594.2441900641345,
      "qty": 19.61,
      "entry_notional": 11740.950186,
      "gross": -87.821618842323,
      "fees": 10.527335438920955,
      "net": -98.34895428124396,
      "hold_hours": 28.833333333333332,
      "net_bps_entry": -83.76575381310792,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "3dfe85d0-ce73-4554-a727-fe534123d9cb",
      "opened_at": 1733500800000.0,
      "closed_at": 1733758680000.0,
      "entry": 609.6117,
      "exit": 606.9570281620346,
      "qty": 28.624000000000002,
      "entry_notional": 17449.525300800004,
      "gross": -75.98732668992307,
      "fees": 15.670378473709537,
      "net": -91.6577051636326,
      "hold_hours": 71.63333333333334,
      "net_bps_entry": -52.52733445959725,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fb3544b7-a577-4cde-a231-f9a3ed4d0b0e",
      "opened_at": 1737388800000.0,
      "closed_at": 1737421260000.0,
      "entry": 601.7926,
      "exit": 595.9026286991198,
      "qty": 15.388,
      "entry_notional": 9260.3845288,
      "gross": -90.63487837794491,
      "fees": 8.293560380649925,
      "net": -98.92843875859484,
      "hold_hours": 9.016666666666667,
      "net_bps_entry": -106.82973093711736,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bfc8456d-a570-4444-aedb-33ce2bb1c9a7",
      "opened_at": 1738080000000.0,
      "closed_at": 1738537260000.0,
      "entry": 605.1029,
      "exit": 594.9989,
      "qty": 13.539,
      "entry_notional": 8192.488163099999,
      "gross": -136.79805599999872,
      "fees": 7.311680221589999,
      "net": -144.10973622158872,
      "hold_hours": 127.01666666666667,
      "net_bps_entry": -175.90472314708634,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b4688dcc-d5d1-44f8-a045-2718a2fe20a0",
      "opened_at": 1766505600000.0,
      "closed_at": 1767139200000.0,
      "entry": 689.2554,
      "exit": 689.5951,
      "qty": 16.556,
      "entry_notional": 11411.3124024,
      "gross": 5.624073200000566,
      "fees": 10.2727119951,
      "net": -4.6486387950994335,
      "hold_hours": 176.0,
      "net_bps_entry": -4.073710920508795,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "MARKET": 1
      }
    }
  ],
  "hyperparameters": [
    [
      "DNA",
      ""
    ],
    [
      "donchian_len",
      26
    ],
    [
      "ema_fast",
      20
    ],
    [
      "ema_slow",
      80
    ],
    [
      "adx_min",
      26
    ],
    [
      "stop_atr",
      2.0
    ],
    [
      "trail_atr",
      4.2
    ],
    [
      "be_r",
      2.25
    ]
  ]
}
```
