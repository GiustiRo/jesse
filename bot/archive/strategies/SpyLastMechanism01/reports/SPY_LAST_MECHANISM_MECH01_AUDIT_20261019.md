# MECH01 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH01",
    "url": "http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592",
    "n": 12,
    "net": 1179.9815614338597,
    "gross_before_fees": 1293.1048935173326,
    "fees": 113.1233320834728,
    "pf": 4.044531891325093,
    "sharpe": 1.0083101800688141,
    "dd_motor_pct": -2.4866856144054705,
    "cagr_motor_pct": 2.162407247921605,
    "time_exposure_pct": 8.130765749985404,
    "entry_price_notional_time": 0.07654082007699883,
    "mean_hold_hours": 309.45694444444445,
    "turnover_two_sides": 251385.18240771734,
    "total_entry_notional": 125046.0387571,
    "net_bps_per_entry_notional": 94.36376978929782,
    "net_plus5bpsRT": 1117.1352658319304,
    "net_plus10bpsRT": 1054.288970230001,
    "net_exbest": 748.9160186067709,
    "net_ex3best": 200.13042443505128,
    "net_exbest_plus10bpsRT": 633.9221258370211,
    "net_ex3best_plus10bpsRT": 105.62345322528937,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328203996,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 1,
        "net": 337.5690574955404,
        "fees": 8.552495880169069
      },
      "2022": {
        "n": 1,
        "net": -99.22117074919896,
        "fees": 4.935835497036526
      },
      "2023": {
        "n": 4,
        "net": 115.79681277005115,
        "fees": 42.159173777076205
      },
      "2024": {
        "n": 3,
        "net": 355.414199555051,
        "fees": 35.695101490220374
      },
      "2025": {
        "n": 2,
        "net": 332.44314908037614,
        "fees": 18.45209907709086
      }
    },
    "executed_order_types": {
      "LIMIT": 9,
      "STOP": 12,
      "MARKET": 3
    },
    "entry_order_types": {
      "LIMIT": 9,
      "MARKET": 3
    },
    "exit_order_types": {
      "STOP": 12
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "10e2b181a3247255d5dbd618ad546426dc8f9619c974241631b01537a47332d6",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "2fd9d76d-dbfc-43c1-9f4c-8406d4310463",
      "opened_at": 1604592720000.0,
      "closed_at": 1607609400000.0,
      "entry": 351.4648,
      "exit": 365.15479609028483,
      "qty": 10.322000000000001,
      "entry_notional": 3627.8196656000005,
      "gross": 141.30813964391973,
      "fees": 3.3286263618797642,
      "net": 137.97951328203996,
      "hold_hours": 837.9666666666667,
      "net_bps_entry": 380.33729898539406,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "00904b69-905c-4c76-9d8b-40a2707905f8",
      "opened_at": 1634630520000.0,
      "closed_at": 1636567560000.0,
      "entry": 449.2998999999999,
      "exit": 465.96840726586606,
      "qty": 20.765,
      "entry_notional": 9329.7124235,
      "gross": 346.1215533757095,
      "fees": 8.552495880169069,
      "net": 337.5690574955404,
      "hold_hours": 538.0666666666667,
      "net_bps_entry": 361.8215033565878,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d6e8ee34-fcab-40a0-ab6b-ad4ce0b02031",
      "opened_at": 1668528060000.0,
      "closed_at": 1668682380000.0,
      "entry": 400.8845,
      "exit": 394.05123900187255,
      "qty": 13.798,
      "entry_notional": 5531.404331,
      "gross": -94.28533525216244,
      "fees": 4.935835497036526,
      "net": -99.22117074919896,
      "hold_hours": 42.86666666666667,
      "net_bps_entry": -179.37790262976705,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "de1867a5-ffeb-48bd-97fb-e41cb84ac2d2",
      "opened_at": 1685991660000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.7527,
      "exit": 437.4709,
      "qty": 25.361,
      "entry_notional": 10873.5972247,
      "gross": 221.1022701999991,
      "fees": 9.88573352382,
      "net": 211.21653667617912,
      "hold_hours": 357.0,
      "net_bps_entry": 194.24715879340152,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "40c0c1c3-ae6d-4fe5-82eb-cddc2268042d",
      "opened_at": 1689314520000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.6334,
      "exit": 454.31735508442654,
      "qty": 28.782,
      "entry_notional": 12970.1305188,
      "gross": 106.03159523996328,
      "fees": 11.720831684777982,
      "net": 94.3107635551853,
      "hold_hours": 325.6,
      "net_bps_entry": 72.71381226155229,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2806177b-8284-4b49-be07-37e5bf7e2332",
      "opened_at": 1697099400000.0,
      "closed_at": 1697135760000.0,
      "entry": 438.8597,
      "exit": 434.28260029311446,
      "qty": 19.748,
      "entry_notional": 8666.6013556,
      "gross": -90.38856501157534,
      "fees": 7.75926636578479,
      "net": -98.14783137736013,
      "hold_hours": 10.1,
      "net_bps_entry": -113.2483511704863,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "79ab08d9-77e0-4ec5-9f6c-e70d3f1aeb63",
      "opened_at": 1703750400000.0,
      "closed_at": 1703866500000.0,
      "entry": 479.2623,
      "exit": 476.6132073404189,
      "qty": 29.742,
      "entry_notional": 14254.2193266,
      "gross": -78.78931388125966,
      "fees": 12.793342202693433,
      "net": -91.5826560839531,
      "hold_hours": 32.25,
      "net_bps_entry": -64.24950674994135,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e5c9f032-61f2-4d34-8cd3-0e4bb1a50fd5",
      "opened_at": 1706875200000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.65629999999993,
      "exit": 497.83465904825056,
      "qty": 22.256,
      "entry_notional": 10986.814612799999,
      "gross": 92.99355897786518,
      "fees": 9.929980253060037,
      "net": 83.06357872480514,
      "hold_hours": 265.51666666666665,
      "net_bps_entry": 75.60296742245323,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "995b4d84-e0b6-45c0-9008-094523f60783",
      "opened_at": 1715273280000.0,
      "closed_at": 1716490620000.0,
      "entry": 520.0111,
      "exit": 527.9046017608516,
      "qty": 23.594,
      "entry_notional": 12269.141893400001,
      "gross": 186.2392805455329,
      "fees": 11.126035380305492,
      "net": 175.1132451652274,
      "hold_hours": 338.15,
      "net_bps_entry": 142.72656285720106,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "584921a2-26f9-418b-8f12-b275070c4b0f",
      "opened_at": 1720195200000.0,
      "closed_at": 1720717380000.0,
      "entry": 554.3867,
      "exit": 558.2129752324591,
      "qty": 29.239,
      "entry_notional": 16209.7127213,
      "gross": 111.87646152187335,
      "fees": 14.639085856854843,
      "net": 97.2373756650185,
      "hold_hours": 145.05,
      "net_bps_entry": 59.98710608686233,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a59ebce8-b013-41c7-b714-cdcd47271fa0",
      "opened_at": 1749658200000.0,
      "closed_at": 1749718980000.0,
      "entry": 604.7239,
      "exit": 599.2100154819894,
      "qty": 16.286,
      "entry_notional": 9848.5334354,
      "gross": -89.7991232603199,
      "fees": 8.823270486392856,
      "net": -98.62239374671276,
      "hold_hours": 16.883333333333333,
      "net_bps_entry": -100.13916731218082,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "da5a55de-43e8-4d0e-a16f-e5ea4a39dbaf",
      "opened_at": 1750927080000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.7689,
      "exit": 636.4563779329557,
      "qty": 17.156,
      "entry_notional": 10478.3512484,
      "gross": 440.6943714177869,
      "fees": 9.628828590698005,
      "net": 431.0655428270889,
      "hold_hours": 804.0333333333333,
      "net_bps_entry": 411.38680371390564,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
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
