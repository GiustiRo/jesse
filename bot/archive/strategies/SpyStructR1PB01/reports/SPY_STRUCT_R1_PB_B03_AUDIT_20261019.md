# B03 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B03",
    "url": "http://localhost:9200/#/backtest/5017be3b-0504-4d40-a5ad-247c3be8b6ff",
    "n": 16,
    "net": 387.3134183431286,
    "gross_before_fees": 542.2349208193973,
    "fees": 154.92150247626873,
    "pf": 1.5173449872924347,
    "sharpe": 0.32576392507850943,
    "dd_motor_pct": -4.291427890215626,
    "cagr_motor_pct": 0.7315137825428808,
    "time_exposure_pct": 6.4683321655865,
    "entry_price_notional_time": 0.06429559330050777,
    "mean_hold_hours": 184.63854166666667,
    "turnover_two_sides": 344270.0055028194,
    "total_entry_notional": 171863.885291,
    "net_bps_per_entry_notional": 22.536056233532094,
    "net_plus5bpsRT": 301.24591696742374,
    "net_plus10bpsRT": 215.1784155917189,
    "net_exbest": -11.347743913807733,
    "net_ex3best": -451.82570987703315,
    "close_year_cohorts": {
      "2021": {
        "n": 2,
        "net": 199.5409502229887,
        "fees": 21.584396264979585
      },
      "2022": {
        "n": 5,
        "net": -99.97668994738513,
        "fees": 32.26039682709587
      },
      "2023": {
        "n": 2,
        "net": 126.78314326936925,
        "fees": 22.531275297975302
      },
      "2024": {
        "n": 5,
        "net": -242.6509514591279,
        "fees": 62.15632621431984
      },
      "2025": {
        "n": 2,
        "net": 403.61696625728365,
        "fees": 16.389107871898133
      }
    },
    "executed_order_types": {
      "MARKET": 16,
      "STOP": 16
    },
    "entry_order_types": {
      "MARKET": 16
    },
    "exit_order_types": {
      "STOP": 16
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "7de99ccfd1075d39fdc47febcc1988ddd3169bda4742404bd4c6724b3f59f70a",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "d8a95674-fdf5-49fe-8bc5-c436ccc1c207",
      "opened_at": 1618473600000.0,
      "closed_at": 1618933920000.0,
      "entry": 413.9042,
      "exit": 413.44940189745466,
      "qty": 30.601,
      "entry_notional": 12665.8824242,
      "gross": -13.917276735988708,
      "fees": 11.393031407248804,
      "net": -25.310308143237513,
      "hold_hours": 127.86666666666666,
      "net_bps_entry": -19.98305944706901,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e4446114-86fe-4f48-8677-4c61241fc2a4",
      "opened_at": 1635148800000.0,
      "closed_at": 1636571160000.0,
      "entry": 455.09330000000006,
      "exit": 464.6385657254694,
      "qty": 24.624,
      "entry_notional": 11206.2174192,
      "gross": 235.04262322395698,
      "fees": 10.19136485773078,
      "net": 224.8512583662262,
      "hold_hours": 395.1,
      "net_bps_entry": 200.6486666776434,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ae4abf50-a9c2-48f8-9b65-41f61c1c88b6",
      "opened_at": 1640764800000.0,
      "closed_at": 1641221460000.0,
      "entry": 479.68420000000003,
      "exit": 475.68169481767427,
      "qty": 20.764,
      "entry_notional": 9960.1627288,
      "gross": -83.10801760581126,
      "fees": 8.926747847997383,
      "net": -92.03476545380863,
      "hold_hours": 126.85,
      "net_bps_entry": -92.40287328608434,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "96015af0-81cc-47e5-9b39-8b3cee6b49ca",
      "opened_at": 1647936000000.0,
      "closed_at": 1648826460000.0,
      "entry": 446.2936,
      "exit": 453.0820196035878,
      "qty": 12.504,
      "entry_notional": 5580.4551744,
      "gross": 84.88239872326176,
      "fees": 5.060606736385467,
      "net": 79.82179198687629,
      "hold_hours": 247.35,
      "net_bps_entry": 143.03813845338982,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a18b8a5b-2a3a-4435-a02a-8e8c8f629efe",
      "opened_at": 1659672000000.0,
      "closed_at": 1659707160000.0,
      "entry": 416.1848,
      "exit": 411.3638111337837,
      "qty": 18.16,
      "entry_notional": 7557.915968,
      "gross": -87.5491578104884,
      "fees": 6.76272725018528,
      "net": -94.31188506067367,
      "hold_hours": 9.766666666666667,
      "net_bps_entry": -124.7855698052049,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "3c3ba594-1b11-4d4d-8ebf-3d47bb417dc2",
      "opened_at": 1659945600000.0,
      "closed_at": 1661122860000.0,
      "entry": 415.3836,
      "exit": 421.4433,
      "qty": 18.173000000000002,
      "entry_notional": 7548.7661628000005,
      "gross": 110.12292810000054,
      "fees": 6.843444864165001,
      "net": 103.27948323583553,
      "hold_hours": 327.01666666666665,
      "net_bps_entry": 136.81637635669844,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9a4d3b39-42a8-4f16-a702-187ca855b2c1",
      "opened_at": 1668585600000.0,
      "closed_at": 1668684540000.0,
      "entry": 400.386,
      "exit": 393.33989219904703,
      "qty": 13.066,
      "entry_notional": 5231.443476,
      "gross": -92.06444452725191,
      "fees": 4.666870128362737,
      "net": -96.73131465561464,
      "hold_hours": 27.483333333333334,
      "net_bps_entry": -184.90367926057783,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "489f9220-786d-4c6c-9df6-b86009178c3c",
      "opened_at": 1685966400000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.4111,
      "exit": 437.4709,
      "qty": 24.87,
      "entry_notional": 10654.584057,
      "gross": 225.3172259999992,
      "fees": 9.690518402999999,
      "net": 215.6267075969992,
      "hold_hours": 364.01666666666665,
      "net_bps_entry": 202.37928242288697,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6c5d01ef-2ecc-440d-a932-7694973f84aa",
      "opened_at": 1690430400000.0,
      "closed_at": 1690485960000.0,
      "entry": 457.8642,
      "exit": 455.43164311123235,
      "qty": 31.244,
      "entry_notional": 14305.509064799999,
      "gross": -76.00280743265466,
      "fees": 12.840756894975303,
      "net": -88.84356432762996,
      "hold_hours": 15.433333333333334,
      "net_bps_entry": -62.10444097109246,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9c25c8fa-53d4-4d07-8017-9f0af2f14121",
      "opened_at": 1708948800000.0,
      "closed_at": 1709194320000.0,
      "entry": 508.8096,
      "exit": 505.26923573275144,
      "qty": 22.697,
      "entry_notional": 11548.4514912,
      "gross": -80.3556477737402,
      "fees": 10.357446300581817,
      "net": -90.71309407432202,
      "hold_hours": 68.2,
      "net_bps_entry": -78.55000659044724,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "30d039c7-944b-494a-b1f0-0ae47e307d02",
      "opened_at": 1718856000000.0,
      "closed_at": 1718904720000.0,
      "entry": 549.4252,
      "exit": 546.6287053838354,
      "qty": 26.400000000000002,
      "entry_notional": 14504.825280000001,
      "gross": -73.82745786674604,
      "fees": 13.021120395959963,
      "net": -86.84857826270601,
      "hold_hours": 13.533333333333333,
      "net_bps_entry": -59.87564592209001,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7155ea21-2f68-4c58-b4a4-29cd3d5ae138",
      "opened_at": 1720152000000.0,
      "closed_at": 1720717380000.0,
      "entry": 553.6182,
      "exit": 558.2129752324591,
      "qty": 26.566,
      "entry_notional": 14707.4211012,
      "gross": 122.06479882550957,
      "fees": 13.291608150551479,
      "net": 108.77319067495809,
      "hold_hours": 157.05,
      "net_bps_entry": 73.95803106914721,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "77006022-85ca-4942-85e7-230f809a15d5",
      "opened_at": 1729252800000.0,
      "closed_at": 1729699920000.0,
      "entry": 585.4382,
      "exit": 581.5982764007666,
      "qty": 20.518,
      "entry_notional": 12012.0209876,
      "gross": -78.78755240907049,
      "fees": 10.77536449025592,
      "net": -89.56291689932641,
      "hold_hours": 124.2,
      "net_bps_entry": -74.56107260533605,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8d1906c1-1840-4125-83c0-69ee77463b66",
      "opened_at": 1733731200000.0,
      "closed_at": 1733759220000.0,
      "entry": 609.1979,
      "exit": 606.6098024836075,
      "qty": 26.888,
      "entry_notional": 16380.113135200001,
      "gross": -69.58876602076089,
      "fees": 14.710786876970658,
      "net": -84.29955289773154,
      "hold_hours": 7.783333333333333,
      "net_bps_entry": -51.46457304777477,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "70ba43bf-792a-46c8-b82f-5cfdf9859d47",
      "opened_at": 1737460800000.0,
      "closed_at": 1737957240000.0,
      "entry": 601.6122,
      "exit": 602.5149517711916,
      "qty": 13.732000000000001,
      "entry_notional": 8261.3387304,
      "gross": 12.396587322002233,
      "fees": 7.440783321654902,
      "net": 4.955804000347331,
      "hold_hours": 137.9,
      "net_bps_entry": 5.998790464929137,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e6f8469f-db87-4245-a200-3cc8ecd25838",
      "opened_at": 1750924800000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.8881,
      "exit": 636.4563779329557,
      "qty": 15.942,
      "entry_notional": 9738.7780902,
      "gross": 407.60948680717956,
      "fees": 8.94832455024323,
      "net": 398.66116225693634,
      "hold_hours": 804.6666666666666,
      "net_bps_entry": 409.35439596688593,
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
