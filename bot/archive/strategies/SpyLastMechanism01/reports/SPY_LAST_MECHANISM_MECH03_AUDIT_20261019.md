# MECH03 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH03",
    "url": "http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea",
    "n": 10,
    "net": 697.9686460382638,
    "gross_before_fees": 804.0369719539531,
    "fees": 106.06832591568929,
    "pf": 2.9665993185601143,
    "sharpe": 0.6732998917480437,
    "dd_motor_pct": -2.3324495156439085,
    "cagr_motor_pct": 1.3024768808721277,
    "time_exposure_pct": 5.197750627663924,
    "entry_price_notional_time": 0.05577949781836071,
    "mean_hold_hours": 237.3916666666667,
    "turnover_two_sides": 235707.39092375396,
    "total_entry_notional": 117451.6769759,
    "net_bps_per_entry_notional": 59.426026431404686,
    "net_plus5bpsRT": 639.0417983073254,
    "net_plus10bpsRT": 580.1149505763868,
    "net_exbest": 277.89820960156555,
    "net_ex3best": -237.75192905000836,
    "net_exbest_plus10bpsRT": 170.6202012937262,
    "net_ex3best_plus10bpsRT": -324.2643627287388,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 232.67786886883164,
        "fees": 20.011913226582937
      },
      "2022": {
        "n": 1,
        "net": -12.277523862229291,
        "fees": 6.33173302951528
      },
      "2023": {
        "n": 4,
        "net": 100.27157937702123,
        "fees": 43.956511108958686
      },
      "2024": {
        "n": 2,
        "net": -42.77371478205806,
        "fees": 26.250050111998476
      },
      "2025": {
        "n": 1,
        "net": 420.0704364366983,
        "fees": 9.518118438633898
      }
    },
    "executed_order_types": {
      "MARKET": 2,
      "STOP": 10,
      "LIMIT": 8
    },
    "entry_order_types": {
      "MARKET": 2,
      "LIMIT": 8
    },
    "exit_order_types": {
      "STOP": 10
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "322ee2c0153ba4844b20b843d57aade9b183536c59c32f3bfd4006f01b2d703f",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "b9f21367-accc-4e1f-94e5-524e004acd1e",
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
      "id": "8e641339-5c3c-4bd7-acf3-9b2c9c2115c1",
      "opened_at": 1634654760000.0,
      "closed_at": 1636567560000.0,
      "entry": 449.84990000000005,
      "exit": 465.9688706336104,
      "qty": 20.356,
      "entry_notional": 9157.144564400001,
      "gross": 328.11776621777244,
      "fees": 8.389083102757999,
      "net": 319.72868311501446,
      "hold_hours": 531.3333333333334,
      "net_bps_entry": 349.157623172201,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f6cdbdcf-8e70-41f7-b0a1-a28d565e6658",
      "opened_at": 1648211580000.0,
      "closed_at": 1648826460000.0,
      "entry": 453.4651,
      "exit": 453.0820196035878,
      "qty": 15.521,
      "entry_notional": 7038.231817100001,
      "gross": -5.94579083271401,
      "fees": 6.33173302951528,
      "net": -12.277523862229291,
      "hold_hours": 170.8,
      "net_bps_entry": -17.444045864474045,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ea69d63e-25aa-45f4-88de-366d5d0d19f7",
      "opened_at": 1682930040000.0,
      "closed_at": 1683040080000.0,
      "entry": 417.2263,
      "exit": 413.9300457491186,
      "qty": 25.004,
      "entry_notional": 10432.3264052,
      "gross": -82.41954128903672,
      "fees": 9.352004971099932,
      "net": -91.77154626013665,
      "hold_hours": 30.566666666666666,
      "net_bps_entry": -87.96843838627697,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d9f6ad93-de56-45d4-ba50-9e62910b474d",
      "opened_at": 1686330060000.0,
      "closed_at": 1687276860000.0,
      "entry": 429.6583,
      "exit": 437.4709,
      "qty": 26.396,
      "entry_notional": 11341.2604868,
      "gross": 206.22138959999938,
      "fees": 10.299934063439999,
      "net": 195.9214555365594,
      "hold_hours": 263.0,
      "net_bps_entry": 172.75104100165126,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c486e700-863e-4408-9036-c952b9e85989",
      "opened_at": 1689357720000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.9436,
      "exit": 454.3069075768155,
      "qty": 29.236,
      "entry_notional": 13183.7870896,
      "gross": 98.3296603157778,
      "fees": 11.9096567277821,
      "net": 86.4200035879957,
      "hold_hours": 313.6,
      "net_bps_entry": 65.55021178714871,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bfc7815c-3404-47e9-aa48-66a676d2e674",
      "opened_at": 1703088000000.0,
      "closed_at": 1703101800000.0,
      "entry": 477.248,
      "exit": 474.55601278065035,
      "qty": 28.939,
      "entry_notional": 13811.079872,
      "gross": -77.90341814076055,
      "fees": 12.394915346636658,
      "net": -90.2983334873972,
      "hold_hours": 3.8333333333333335,
      "net_bps_entry": -65.38108122194284,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9e25be4f-e48e-4aad-8e61-3e9249e6e901",
      "opened_at": 1707489060000.0,
      "closed_at": 1707831180000.0,
      "entry": 499.87420000000003,
      "exit": 497.6214726866414,
      "qty": 27.211000000000002,
      "entry_notional": 13602.076856200001,
      "gross": -61.29896292379999,
      "fees": 12.21428463726429,
      "net": -73.51324756106428,
      "hold_hours": 95.03333333333333,
      "net_bps_entry": -54.045605195618336,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "929d4da9-0090-42c0-b30e-72a0c6fd4456",
      "opened_at": 1720458480000.0,
      "closed_at": 1720717380000.0,
      "entry": 556.6126,
      "exit": 558.2129752324591,
      "qty": 27.978,
      "entry_notional": 15572.907322800002,
      "gross": 44.7752982537404,
      "fees": 14.035765474734186,
      "net": 30.73953277900622,
      "hold_hours": 71.91666666666667,
      "net_bps_entry": 19.739109815417088,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "51f2bdca-52cb-4f29-8cff-d66ec288be2d",
      "opened_at": 1750944840000.0,
      "closed_at": 1753821600000.0,
      "entry": 611.1179,
      "exit": 636.4563779329557,
      "qty": 16.954,
      "entry_notional": 10360.892876599999,
      "gross": 429.5885548753322,
      "fees": 9.518118438633898,
      "net": 420.0704364366983,
      "hold_hours": 799.1,
      "net_bps_entry": 405.4384515309721,
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
