# MECH04 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH04",
    "url": "http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05",
    "n": 16,
    "net": 874.7958565504204,
    "gross_before_fees": 1025.389857801811,
    "fees": 150.5940012513908,
    "pf": 2.320269711623384,
    "sharpe": 0.7183938780138998,
    "dd_motor_pct": -3.8005064163188162,
    "cagr_motor_pct": 1.6215132040717561,
    "time_exposure_pct": 8.78747737490512,
    "entry_price_notional_time": 0.08121036182627324,
    "mean_hold_hours": 250.83854166666666,
    "turnover_two_sides": 334653.3361142018,
    "total_entry_notional": 166813.97312819998,
    "net_bps_per_entry_notional": 52.44140164913652,
    "net_plus5bpsRT": 791.1325225218699,
    "net_plus10bpsRT": 707.4691884933195,
    "net_exbest": 455.514513978981,
    "net_ex3best": -86.35598247698488,
    "net_exbest_plus10bpsRT": 298.5940700283137,
    "net_ex3best_plus10bpsRT": -223.07893097807187,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328203996,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 2,
        "net": 246.37563263516452,
        "fees": 20.26102000096626
      },
      "2022": {
        "n": 2,
        "net": -110.69546618442911,
        "fees": 11.312388365121311
      },
      "2023": {
        "n": 6,
        "net": -67.92668184187492,
        "fees": 63.022585116543596
      },
      "2024": {
        "n": 3,
        "net": 345.71519911248186,
        "fees": 34.721055221010076
      },
      "2025": {
        "n": 2,
        "net": 323.34765954703806,
        "fees": 17.94832618586981
      }
    },
    "executed_order_types": {
      "LIMIT": 11,
      "STOP": 16,
      "MARKET": 5
    },
    "entry_order_types": {
      "LIMIT": 11,
      "MARKET": 5
    },
    "exit_order_types": {
      "STOP": 16
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "e102e42a463c033a5cff19992945106a82c9f3d358f82a1bb3d749d2e309e457",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "407edcfe-a72a-4630-9fba-a55d19cfd97a",
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
      "id": "1b6af3d3-d9d8-4035-9429-77c8543675ac",
      "opened_at": 1618574400000.0,
      "closed_at": 1618915440000.0,
      "entry": 417.2133,
      "exit": 414.78358784556247,
      "qty": 31.472,
      "entry_notional": 13130.5369776,
      "gross": -76.46790092445735,
      "fees": 11.783072724423995,
      "net": -88.25097364888134,
      "hold_hours": 94.73333333333333,
      "net_bps_entry": -67.21048331795784,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "67385cfb-1b86-4f38-b867-37b229e3e356",
      "opened_at": 1634630520000.0,
      "closed_at": 1636567560000.0,
      "entry": 449.2998999999999,
      "exit": 465.96840726586606,
      "qty": 20.584,
      "entry_notional": 9248.389141599999,
      "gross": 343.1045535605881,
      "fees": 8.477947276542263,
      "net": 334.62660628404586,
      "hold_hours": 538.0666666666667,
      "net_bps_entry": 361.8215033565883,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "89f9c53b-21f9-4bf6-af02-8b754064a36e",
      "opened_at": 1648211580000.0,
      "closed_at": 1648826460000.0,
      "entry": 453.4651,
      "exit": 453.0820196035878,
      "qty": 15.751,
      "entry_notional": 7142.5287901,
      "gross": -6.033899323888363,
      "fees": 6.42556065639425,
      "net": -12.459459980282613,
      "hold_hours": 170.8,
      "net_bps_entry": -17.444045864473402,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2dc7f366-5a4d-446f-b127-d71b858350c8",
      "opened_at": 1668528060000.0,
      "closed_at": 1668682380000.0,
      "entry": 400.8845,
      "exit": 394.0512390018725,
      "qty": 13.661,
      "entry_notional": 5476.4831545,
      "gross": -93.34917849541944,
      "fees": 4.88682770872706,
      "net": -98.23600620414649,
      "hold_hours": 42.86666666666667,
      "net_bps_entry": -179.37790262976785,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0c945ac1-07b7-4b31-b838-0cf637c4c0bd",
      "opened_at": 1682930040000.0,
      "closed_at": 1683040080000.0,
      "entry": 417.2263,
      "exit": 413.9300457491186,
      "qty": 25.134,
      "entry_notional": 10486.565824199999,
      "gross": -82.84805434165173,
      "fees": 9.400627617326256,
      "net": -92.24868195897798,
      "hold_hours": 30.566666666666666,
      "net_bps_entry": -87.96843838627738,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "215ceec0-d589-4861-bf47-a438984555e4",
      "opened_at": 1685991660000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.7527,
      "exit": 437.47090000000003,
      "qty": 24.884,
      "entry_notional": 10669.0821868,
      "gross": 216.94368880000002,
      "fees": 9.69979862808,
      "net": 207.24389017192001,
      "hold_hours": 357.0,
      "net_bps_entry": 194.24715879340235,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "60ddf1de-b3a9-4d22-80c9-6123de67955f",
      "opened_at": 1689314520000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.6334,
      "exit": 454.31735508442654,
      "qty": 28.241,
      "entry_notional": 12726.337849399999,
      "gross": 104.03857553929083,
      "fees": 11.50052142345268,
      "net": 92.53805411583815,
      "hold_hours": 325.6,
      "net_bps_entry": 72.7138122615541,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "05597e38-6ff1-46ac-925b-16becd9cb697",
      "opened_at": 1697099400000.0,
      "closed_at": 1697135760000.0,
      "entry": 438.8596999999999,
      "exit": 434.28260029311434,
      "qty": 19.377,
      "entry_notional": 8503.784406899998,
      "gross": -88.69046102032189,
      "fees": 7.613495258750854,
      "net": -96.30395627907275,
      "hold_hours": 10.1,
      "net_bps_entry": -113.24835117048758,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c7e63d71-cf42-44cb-a36e-81dc8d91b144",
      "opened_at": 1703088000000.0,
      "closed_at": 1703101800000.0,
      "entry": 477.248,
      "exit": 474.55601278065035,
      "qty": 28.867,
      "entry_notional": 13776.718016,
      "gross": -77.70959506096733,
      "fees": 12.364076896622564,
      "net": -90.0736719575899,
      "hold_hours": 3.8333333333333335,
      "net_bps_entry": -65.38108122194282,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a6cedcfc-f882-42c4-b3cc-f3f35f5669f9",
      "opened_at": 1703750400000.0,
      "closed_at": 1703866500000.0,
      "entry": 479.2623,
      "exit": 476.61320734041885,
      "qty": 28.93,
      "entry_notional": 13865.058339,
      "gross": -76.63825064168122,
      "fees": 12.444065292311242,
      "net": -89.08231593399246,
      "hold_hours": 32.25,
      "net_bps_entry": -64.24950674994233,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8edc82cc-17ba-4ea1-b245-87127ab98b05",
      "opened_at": 1706875200000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.65629999999993,
      "exit": 497.83465904825056,
      "qty": 21.649,
      "entry_notional": 10687.1652387,
      "gross": 90.45729503557777,
      "fees": 9.65915449759601,
      "net": 80.79814053798177,
      "hold_hours": 265.51666666666665,
      "net_bps_entry": 75.60296742245389,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a607ed65-13d0-42b7-a0c4-bd18067ea366",
      "opened_at": 1715273280000.0,
      "closed_at": 1716490620000.0,
      "entry": 520.0111,
      "exit": 527.9046017608516,
      "qty": 22.95,
      "entry_notional": 11934.254745,
      "gross": 181.15586541154335,
      "fees": 10.822349409935194,
      "net": 170.33351600160816,
      "hold_hours": 338.15,
      "net_bps_entry": 142.72656285720015,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e2ef72db-903e-497d-9fd6-16f1af96d194",
      "opened_at": 1720195200000.0,
      "closed_at": 1720717380000.0,
      "entry": 554.3867,
      "exit": 558.2129752324591,
      "qty": 28.441,
      "entry_notional": 15767.3121347,
      "gross": 108.82309388637077,
      "fees": 14.239551313478866,
      "net": 94.5835425728919,
      "hold_hours": 145.05,
      "net_bps_entry": 59.98710608686223,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d429c1f3-65fb-4249-aabb-fac72c7524ef",
      "opened_at": 1749658200000.0,
      "closed_at": 1749718980000.0,
      "entry": 604.7239,
      "exit": 599.2100154819894,
      "qty": 15.842,
      "entry_notional": 9580.0360238,
      "gross": -87.35095853432176,
      "fees": 8.582724490079555,
      "net": -95.93368302440132,
      "hold_hours": 16.883333333333333,
      "net_bps_entry": -100.13916731217931,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "df5799bb-2b96-4922-bd79-46aaf5c579f6",
      "opened_at": 1750927080000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.7689,
      "exit": 636.4563779329557,
      "qty": 16.687,
      "entry_notional": 10191.900634300002,
      "gross": 428.6469442672296,
      "fees": 9.365601695790254,
      "net": 419.2813425714394,
      "hold_hours": 804.0333333333333,
      "net_bps_entry": 411.3868037139045,
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
