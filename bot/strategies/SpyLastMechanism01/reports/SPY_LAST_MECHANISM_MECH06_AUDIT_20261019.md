# MECH06 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH06",
    "url": "http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65",
    "n": 12,
    "net": 962.2141582992981,
    "gross_before_fees": 1081.4718254119934,
    "fees": 119.2576671126954,
    "pf": 3.5163421885325037,
    "sharpe": 0.8231146879007425,
    "dd_motor_pct": -2.9289574394842255,
    "cagr_motor_pct": 1.7776893671002103,
    "time_exposure_pct": 6.638020377182227,
    "entry_price_notional_time": 0.0731582633364019,
    "mean_hold_hours": 252.64305555555555,
    "turnover_two_sides": 265017.03802821203,
    "total_entry_notional": 131967.7831014,
    "net_bps_per_entry_notional": 72.91280763275095,
    "net_plus5bpsRT": 895.9598987922451,
    "net_plus10bpsRT": 829.7056392851921,
    "net_exbest": 539.5659013691004,
    "net_ex3best": 57.72954538738702,
    "net_exbest_plus10bpsRT": 417.54717055504955,
    "net_ex3best_plus10bpsRT": -42.4007423119714,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 189.58210941171166,
        "fees": 21.71813145086816
      },
      "2022": {
        "n": 2,
        "net": -108.62122192470657,
        "fees": 11.10046763786092
      },
      "2023": {
        "n": 3,
        "net": 206.81929028856132,
        "fees": 33.34712022067916
      },
      "2024": {
        "n": 3,
        "net": 348.48847477499396,
        "fees": 34.9996091098882
      },
      "2025": {
        "n": 2,
        "net": 325.9455057487378,
        "fees": 18.092338693398965
      }
    },
    "executed_order_types": {
      "MARKET": 4,
      "STOP": 12,
      "LIMIT": 8
    },
    "entry_order_types": {
      "MARKET": 4,
      "LIMIT": 8
    },
    "exit_order_types": {
      "STOP": 12
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "67c55b367685fc8041907c977ca026f1528375a1e766eb84eb8230dfd39cb190",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "c813affe-ea26-4fdd-811f-7a2ff3ac3979",
      "opened_at": 1618574400000.0,
      "closed_at": 1618915440000.0,
      "entry": 417.2133,
      "exit": 414.78358784556247,
      "qty": 31.044,
      "entry_notional": 12951.9696852,
      "gross": -75.42798412235788,
      "fees": 11.622830123824938,
      "net": -87.05081424618282,
      "hold_hours": 94.73333333333333,
      "net_bps_entry": -67.21048331795768,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2683456c-0341-4e93-a394-988a1d6ed6a5",
      "opened_at": 1634885460000.0,
      "closed_at": 1636567560000.0,
      "entry": 454.2099,
      "exit": 465.9706967590212,
      "qty": 24.38,
      "entry_notional": 11073.637362,
      "gross": 286.7282249849377,
      "fees": 10.095301327043222,
      "net": 276.6329236578945,
      "hold_hours": 467.25,
      "net_bps_entry": 249.81215712118285,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "df55669b-f408-4fd5-a767-8592123f631b",
      "opened_at": 1648211580000.0,
      "closed_at": 1648826460000.0,
      "entry": 453.4651,
      "exit": 453.0820196035878,
      "qty": 15.456,
      "entry_notional": 7008.7565856,
      "gross": -5.920890606947069,
      "fees": 6.305216526266873,
      "net": -12.226107133213942,
      "hold_hours": 170.8,
      "net_bps_entry": -17.444045864473832,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0792a943-48d3-4247-90e0-973d8b3e4cff",
      "opened_at": 1668528060000.0,
      "closed_at": 1668682380000.0,
      "entry": 400.8845,
      "exit": 394.05123900187255,
      "qty": 13.405000000000001,
      "entry_notional": 5373.856722500001,
      "gross": -91.59986367989859,
      "fees": 4.795251111594046,
      "net": -96.39511479149263,
      "hold_hours": 42.86666666666667,
      "net_bps_entry": -179.37790262976742,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "43e8175f-3034-4de5-a5cc-b31671512c0e",
      "opened_at": 1685991660000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.7527,
      "exit": 437.4708999999999,
      "qty": 24.639,
      "entry_notional": 10564.0377753,
      "gross": 214.80772979999892,
      "fees": 9.60429747618,
      "net": 205.20343232381893,
      "hold_hours": 357.0,
      "net_bps_entry": 194.24715879340135,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5c70623b-e1b2-4f0b-ada2-ea7fe243d8bb",
      "opened_at": 1689314520000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.6334,
      "exit": 454.31735508442654,
      "qty": 27.963,
      "entry_notional": 12601.0617642,
      "gross": 103.01443602582003,
      "fees": 11.387312083991619,
      "net": 91.62712394182842,
      "hold_hours": 325.6,
      "net_bps_entry": 72.71381226155391,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "10f9e2bc-3870-4022-97a8-9aeffedde775",
      "opened_at": 1703088000000.0,
      "closed_at": 1703101800000.0,
      "entry": 477.248,
      "exit": 474.55601278065035,
      "qty": 28.847,
      "entry_notional": 13767.173056,
      "gross": -77.6557553165785,
      "fees": 12.355510660507539,
      "net": -90.01126597708604,
      "hold_hours": 3.8333333333333335,
      "net_bps_entry": -65.38108122194149,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7e731c97-7d1d-4a53-9bb0-e775652ca4a0",
      "opened_at": 1706875200000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.65630000000004,
      "exit": 497.83465904825056,
      "qty": 21.823,
      "entry_notional": 10773.0614349,
      "gross": 91.18432950997158,
      "fees": 9.736788239689487,
      "net": 81.44754127028209,
      "hold_hours": 265.51666666666665,
      "net_bps_entry": 75.6029674224522,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "4e5fff78-dc56-42b8-91e3-349261443d0d",
      "opened_at": 1715273280000.0,
      "closed_at": 1716490620000.0,
      "entry": 520.0111,
      "exit": 527.9046017608516,
      "qty": 23.134,
      "entry_notional": 12029.936787400002,
      "gross": 182.60826973553958,
      "fees": 10.909116830040993,
      "net": 171.69915290549858,
      "hold_hours": 338.15,
      "net_bps_entry": 142.72656285719972,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2a166aa6-171b-434c-8d6d-5adf01e93bc0",
      "opened_at": 1720195200000.0,
      "closed_at": 1720717380000.0,
      "entry": 554.3867,
      "exit": 558.2129752324591,
      "qty": 28.669,
      "entry_notional": 15893.7123023,
      "gross": 109.69548463937099,
      "fees": 14.353704040157718,
      "net": 95.34178059921327,
      "hold_hours": 145.05,
      "net_bps_entry": 59.98710608686193,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "aa44076d-4776-4072-abf2-4d7ead6e7853",
      "opened_at": 1749658200000.0,
      "closed_at": 1749718980000.0,
      "entry": 604.7239,
      "exit": 599.2100154819894,
      "qty": 15.969000000000001,
      "entry_notional": 9656.8359591,
      "gross": -88.05122186811059,
      "fees": 8.65152931334935,
      "net": -96.70275118145994,
      "hold_hours": 16.883333333333333,
      "net_bps_entry": -100.13916731218086,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d7ef83fe-4a67-48d0-8214-f77e99d47e49",
      "opened_at": 1750927080000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.7689,
      "exit": 636.4563779329557,
      "qty": 16.821,
      "entry_notional": 10273.743666900002,
      "gross": 432.0890663102473,
      "fees": 9.440809380049613,
      "net": 422.6482569301977,
      "hold_hours": 804.0333333333333,
      "net_bps_entry": 411.3868037139061,
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
