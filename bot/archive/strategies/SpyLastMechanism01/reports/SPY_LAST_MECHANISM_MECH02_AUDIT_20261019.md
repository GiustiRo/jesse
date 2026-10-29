# MECH02 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH02",
    "url": "http://localhost:9200/#/backtest/0f51b89a-028a-450f-b950-b9494621139e",
    "n": 11,
    "net": 770.5482833495945,
    "gross_before_fees": 888.8344259104642,
    "fees": 118.2861425608697,
    "pf": 3.1711000022054057,
    "sharpe": 0.6891165837182842,
    "dd_motor_pct": -2.3324495156439085,
    "cagr_motor_pct": 1.4339388653358265,
    "time_exposure_pct": 5.646457348046943,
    "entry_price_notional_time": 0.061912452369650595,
    "mean_hold_hours": 234.4409090909091,
    "turnover_two_sides": 262858.0945797105,
    "total_entry_notional": 130984.63007690001,
    "net_bps_per_entry_notional": 58.827381723887136,
    "net_plus5bpsRT": 704.8337597046668,
    "net_plus10bpsRT": 639.1192360597393,
    "net_exbest": 347.6284839194916,
    "net_ex3best": -168.0216547320823,
    "net_exbest_plus10bpsRT": 226.84685930465514,
    "net_ex3best_plus10bpsRT": -268.0377047178099,
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
        "n": 3,
        "net": 26.956559535868067,
        "fees": 38.40330478829588
      },
      "2025": {
        "n": 1,
        "net": 422.9197994301029,
        "fees": 9.582680407516929
      }
    },
    "executed_order_types": {
      "MARKET": 2,
      "STOP": 11,
      "LIMIT": 9
    },
    "entry_order_types": {
      "MARKET": 2,
      "LIMIT": 9
    },
    "exit_order_types": {
      "STOP": 11
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "43e2e07ccc0913f2b77725b0a073cacdce997cbef5b0e479f49400a759b15a12",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "50e2e846-ad55-41b8-b2e6-f9049a7b506e",
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
      "id": "e6b3faa8-65a9-46dc-b2b6-fcaf969e12eb",
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
      "id": "7fa658d3-17bb-445f-8bdf-0abf32792694",
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
      "id": "af71e0ad-bcf5-4bec-8e45-5f5e1ad04efc",
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
      "id": "a9371f6b-ebcc-48ee-b744-29d1e6b04519",
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
      "id": "32bd9fde-5c9e-46e9-8add-855ae2d454e8",
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
      "id": "6a820c88-782c-4079-81f3-c0c792ef88fd",
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
      "id": "e90e73e9-d9f9-454e-8411-dec6f6ea4ddd",
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
      "id": "e2b9a4b4-7535-4b14-aa0f-c10828c838a2",
      "opened_at": 1715752860000.0,
      "closed_at": 1716490620000.0,
      "entry": 524.7267,
      "exit": 527.9315499671492,
      "qty": 25.455000000000002,
      "entry_notional": 13356.918148500003,
      "gross": 81.5794559137812,
      "fees": 12.057937088811205,
      "net": 69.52151882497,
      "hold_hours": 204.93333333333334,
      "net_bps_entry": 52.04907153883948,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2937e3d5-d026-4675-8344-9298e0d4890a",
      "opened_at": 1720458480000.0,
      "closed_at": 1720717380000.0,
      "entry": 556.6126,
      "exit": 558.2129752958742,
      "qty": 28.168,
      "entry_notional": 15678.663716800002,
      "gross": 45.079371334182724,
      "fees": 14.131083062220384,
      "net": 30.94828827196234,
      "hold_hours": 71.91666666666667,
      "net_bps_entry": 19.73911095420755,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d47a76a7-0210-42c3-ba07-f398df31cb06",
      "opened_at": 1750944840000.0,
      "closed_at": 1753821600000.0,
      "entry": 611.1179,
      "exit": 636.4563779329557,
      "qty": 17.069,
      "entry_notional": 10431.1714351,
      "gross": 432.50247983761983,
      "fees": 9.582680407516929,
      "net": 422.9197994301029,
      "hold_hours": 799.1,
      "net_bps_entry": 405.4384515309699,
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
