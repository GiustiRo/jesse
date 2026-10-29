# B04 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B04",
    "url": "http://localhost:9200/#/backtest/89463730-ef5f-47ad-abd3-5e1a19f3c3c2",
    "n": 7,
    "net": 181.972022393028,
    "gross_before_fees": 256.79765040449,
    "fees": 74.82562801146202,
    "pf": 1.5253042509470454,
    "sharpe": 0.21378551719950004,
    "dd_motor_pct": -2.9310748574774337,
    "cagr_motor_pct": 0.3464879762923312,
    "time_exposure_pct": 3.1664550125532784,
    "entry_price_notional_time": 0.031081923279426108,
    "mean_hold_hours": 206.59761904761905,
    "turnover_two_sides": 166279.1733588045,
    "total_entry_notional": 83011.1878542,
    "net_bps_per_entry_notional": 21.92138518878224,
    "net_plus5bpsRT": 140.4022290533269,
    "net_plus10bpsRT": 98.83243571362576,
    "net_exbest": -208.7869364218563,
    "net_ex3best": -346.4126210000384,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": -173.81215876241498,
        "fees": 22.715166569763305
      },
      "2022": {
        "n": 1,
        "net": 100.54589871833987,
        "fees": 6.662313681660001
      },
      "2023": {
        "n": 1,
        "net": -85.49945610597477,
        "fees": 12.357440782144277
      },
      "2024": {
        "n": 2,
        "net": -50.02122027180642,
        "fees": 24.319754812413272
      },
      "2025": {
        "n": 1,
        "net": 390.7589588148843,
        "fees": 8.770952165481162
      }
    },
    "executed_order_types": {
      "MARKET": 7,
      "STOP": 7
    },
    "entry_order_types": {
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 7
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "5b196b5f542e97a97e333e402c37555e386cd6f37fdbb523040399660b3f17a6",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "e12193ec-f0de-4a36-83dd-83f358780ad1",
      "opened_at": 1618574400000.0,
      "closed_at": 1618915440000.0,
      "entry": 417.2133,
      "exit": 414.78358784556247,
      "qty": 31.043,
      "entry_notional": 12951.5524719,
      "gross": -75.42555441020522,
      "fees": 11.622455725225407,
      "net": -87.04801013543063,
      "hold_hours": 94.73333333333333,
      "net_bps_entry": -67.21048331795906,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ea315c8c-0d61-480a-8b45-b79fb468f1f9",
      "opened_at": 1636459200000.0,
      "closed_at": 1636470300000.0,
      "entry": 470.2754,
      "exit": 467.39695510736635,
      "qty": 26.289,
      "entry_notional": 12363.0699906,
      "gross": -75.67143778244645,
      "fees": 11.0927108445379,
      "net": -86.76414862698435,
      "hold_hours": 3.0833333333333335,
      "net_bps_entry": -70.18009984005077,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c6a5d176-5481-43a6-a99c-2099319ad3d6",
      "opened_at": 1659945600000.0,
      "closed_at": 1661122860000.0,
      "entry": 415.3836,
      "exit": 421.4433,
      "qty": 17.692,
      "entry_notional": 7348.9666512,
      "gross": 107.20821239999987,
      "fees": 6.662313681660001,
      "net": 100.54589871833987,
      "hold_hours": 327.01666666666665,
      "net_bps_entry": 136.8163763566976,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "08c441e1-8541-4f19-bd99-ea599bc6b7bb",
      "opened_at": 1690430400000.0,
      "closed_at": 1690485960000.0,
      "entry": 457.8642,
      "exit": 455.43164661022246,
      "qty": 30.068,
      "entry_notional": 13767.0607656,
      "gross": -73.14201532383049,
      "fees": 12.357440782144277,
      "net": -85.49945610597477,
      "hold_hours": 15.433333333333334,
      "net_bps_entry": -62.10436458565926,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8c4c7679-8ae8-4147-b929-e1d9036848f0",
      "opened_at": 1720440000000.0,
      "closed_at": 1720717380000.0,
      "entry": 556.3677,
      "exit": 558.2129752324591,
      "qty": 27.595,
      "entry_notional": 15352.9666815,
      "gross": 50.92037003971018,
      "fees": 13.840584179867868,
      "net": 37.07978585984231,
      "hold_hours": 77.05,
      "net_bps_entry": 24.15154453798344,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9d3e5d20-52d0-48a7-b87c-e9f1d627f2df",
      "opened_at": 1729252800000.0,
      "closed_at": 1729699920000.0,
      "entry": 585.4382,
      "exit": 581.5982764007666,
      "qty": 19.954,
      "entry_notional": 11681.8338428,
      "gross": -76.62183549910333,
      "fees": 10.479170632545404,
      "net": -87.10100613164873,
      "hold_hours": 124.2,
      "net_bps_entry": -74.56107260533645,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9f9b4cc5-8d76-4c1b-a47f-bee7c13591a4",
      "opened_at": 1750924800000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.8881,
      "exit": 636.4563779329557,
      "qty": 15.626,
      "entry_notional": 9545.7374506,
      "gross": 399.52991098036546,
      "fees": 8.770952165481162,
      "net": 390.7589588148843,
      "hold_hours": 804.6666666666666,
      "net_bps_entry": 409.35439596688576,
      "entry_types": {
        "MARKET": 1
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
