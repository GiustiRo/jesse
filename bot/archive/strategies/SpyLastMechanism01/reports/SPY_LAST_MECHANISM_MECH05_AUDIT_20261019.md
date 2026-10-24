# MECH05 complete snapshot audit

Auditor dcbbcdb9950b4a69b9e516da8f4b0b70 passed. Quantity/fillfees/PNL/wallet/terminal reconciled. Combined exclusion+stress is posthoc diagnostic; not a new policy or new full.

```json
{
  "row": {
    "name": "MECH05",
    "url": "http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862",
    "n": 19,
    "net": 1275.16361422292,
    "gross_before_fees": 1454.7746342884798,
    "fees": 179.6110200655598,
    "pf": 2.6547989447750973,
    "sharpe": 0.8824390732454782,
    "dd_motor_pct": -3.5693369150006315,
    "cagr_motor_pct": 2.3286604902763797,
    "time_exposure_pct": 11.413265604017049,
    "entry_price_notional_time": 0.11145537781293709,
    "mean_hold_hours": 274.35087719298247,
    "turnover_two_sides": 399135.60014568846,
    "total_entry_notional": 198840.4127557,
    "net_bps_per_entry_notional": 64.13000237479973,
    "net_plus5bpsRT": 1175.3797141864977,
    "net_plus10bpsRT": 1075.5958141500757,
    "net_exbest": 788.0828023924619,
    "net_ex3best": 31.514430560207984,
    "net_exbest_plus10bpsRT": 600.245547197728,
    "net_ex3best_plus10bpsRT": -136.13410899187053,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 128.87328631389613,
        "fees": 3.3320653378432827
      },
      "2021": {
        "n": 3,
        "net": 141.76836222930348,
        "fees": 28.37809778742753
      },
      "2022": {
        "n": 2,
        "net": -68.33202768816221,
        "fees": 10.063353768336079
      },
      "2023": {
        "n": 6,
        "net": 499.46072488189895,
        "fees": 61.22685344828858
      },
      "2024": {
        "n": 4,
        "net": 308.0657071133023,
        "fees": 44.95854738784551
      },
      "2025": {
        "n": 3,
        "net": 265.32756137268126,
        "fees": 31.652102335818824
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
        "trade_id": "f0bc07fa-7900-444d-a024-453374fa1fb0",
        "side": "sell",
        "type": "MARKET",
        "gross": -57.0982499999991,
        "net": -70.01020096766909,
        "fee": 12.91195096767,
        "exit_fee": 6.443128377585
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "11792763736fe6fff525af7e98ac7482de1c0ae9b866e013a453745115611508",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "96b3f675-36d8-4c02-939c-6984a2437141",
      "opened_at": 1604592000000.0,
      "closed_at": 1607609400000.0,
      "entry": 352.3442,
      "exit": 365.15479609028483,
      "qty": 10.32,
      "entry_notional": 3636.192144,
      "gross": 132.20535165173942,
      "fees": 3.3320653378432827,
      "net": 128.87328631389613,
      "hold_hours": 838.1666666666666,
      "net_bps_entry": 354.41825186973983,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "11083ac6-e366-4923-bfa7-9d1867e39af2",
      "opened_at": 1612929600000.0,
      "closed_at": 1612971780000.0,
      "entry": 392.5551,
      "exit": 389.25413722646675,
      "qty": 25.038,
      "entry_notional": 9828.7945938,
      "gross": -82.64950592372406,
      "fees": 8.808722856754324,
      "net": -91.4582287804784,
      "hold_hours": 11.716666666666667,
      "net_bps_entry": -93.05131764394609,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c9f076d3-a9e7-4561-a2ed-9507f4015f07",
      "opened_at": 1618502400000.0,
      "closed_at": 1618933860000.0,
      "entry": 416.1333,
      "exit": 413.5686418679511,
      "qty": 29.925,
      "entry_notional": 12452.789002500002,
      "gross": -76.74739460156525,
      "fees": 11.172973774679296,
      "net": -87.92036837624454,
      "hold_hours": 119.85,
      "net_bps_entry": -70.60295357015508,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "155ba681-be07-4187-8097-69835158122e",
      "opened_at": 1634630400000.0,
      "closed_at": 1636567560000.0,
      "entry": 449.7945,
      "exit": 465.96840726586606,
      "qty": 20.375,
      "entry_notional": 9164.5629375,
      "gross": 329.5433605420203,
      "fees": 8.39640115599391,
      "net": 321.1469593860264,
      "hold_hours": 538.1,
      "net_bps_entry": 350.4225586928339,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "18565f72-2112-4df1-ac6a-edcee7a5c8dd",
      "opened_at": 1647964800000.0,
      "closed_at": 1648826460000.0,
      "entry": 450.3948,
      "exit": 453.08201960358775,
      "qty": 12.813,
      "entry_notional": 5770.9085724,
      "gross": 34.431344780770814,
      "fees": 5.209311820311346,
      "net": 29.22203296045947,
      "hold_hours": 239.35,
      "net_bps_entry": 50.63679764433807,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "96db0a98-5494-4105-a531-7727c58ab2d2",
      "opened_at": 1668528000000.0,
      "closed_at": 1668682380000.0,
      "entry": 400.9826,
      "exit": 394.14933900187253,
      "qty": 13.566,
      "entry_notional": 5439.7299516,
      "gross": -92.70001870059696,
      "fees": 4.854041948024731,
      "net": -97.55406064862169,
      "hold_hours": 42.88333333333333,
      "net_bps_entry": -179.33621984291312,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5289a553-3457-42fe-881a-fb350f75407c",
      "opened_at": 1682913600000.0,
      "closed_at": 1683040260000.0,
      "entry": 417.2004,
      "exit": 413.7543415711971,
      "qty": 24.078,
      "entry_notional": 10045.3512312,
      "gross": -82.97419484871716,
      "fees": 9.003477720398077,
      "net": -91.97767256911524,
      "hold_hours": 35.18333333333333,
      "net_bps_entry": -91.56242569542064,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "aa6b5673-694f-4906-ac93-f3832ad3d1b6",
      "opened_at": 1685980800000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.8277,
      "exit": 437.4709,
      "qty": 24.71,
      "entry_notional": 10596.332467,
      "gross": 213.57347200000004,
      "fees": 9.6328072827,
      "net": 203.94066471730002,
      "hold_hours": 360.01666666666665,
      "net_bps_entry": 192.46344464221878,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "01dc2b69-b2d2-4a98-a54c-75633fd89d1d",
      "opened_at": 1689307200000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.7106999999999,
      "exit": 454.30690876106024,
      "qty": 28.038,
      "entry_notional": 12637.026606599999,
      "gross": 100.83050124260808,
      "fees": 11.418697671499173,
      "net": 89.4118035711089,
      "hold_hours": 327.6333333333333,
      "net_bps_entry": 70.75383027555816,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8c60fe8d-eed0-4459-a9a6-f23fbca4c233",
      "opened_at": 1697097600000.0,
      "closed_at": 1697135220000.0,
      "entry": 439.42569999999995,
      "exit": 434.8486002931144,
      "qty": 19.23,
      "entry_notional": 8450.156211,
      "gross": -88.0176273634097,
      "fees": 7.565532657586465,
      "net": -95.58316002099616,
      "hold_hours": 10.45,
      "net_bps_entry": -113.11407462097645,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "3a6822ad-5e97-4231-9de3-31dcf4c7309b",
      "opened_at": 1700496000000.0,
      "closed_at": 1703102040000.0,
      "entry": 453.1962,
      "exit": 472.8385249347052,
      "qty": 25.335,
      "entry_notional": 11481.725727,
      "gross": 497.6383022207574,
      "fees": 10.557490390299339,
      "net": 487.08081183045806,
      "hold_hours": 723.9,
      "net_bps_entry": 424.2226503330043,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1c79c848-23f2-4bf7-9d9d-6aaf0c578239",
      "opened_at": 1703750400000.0,
      "closed_at": 1703866500000.0,
      "entry": 479.2623,
      "exit": 476.6132073404189,
      "qty": 30.336000000000002,
      "entry_notional": 14538.9011328,
      "gross": -80.36287492105112,
      "fees": 13.048847725805526,
      "net": -93.41172264685665,
      "hold_hours": 32.25,
      "net_bps_entry": -64.24950674994155,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c8ff6479-5dbf-4cab-a884-2da17d991f4e",
      "opened_at": 1706875200000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.6563,
      "exit": 497.83465904825056,
      "qty": 22.7,
      "entry_notional": 11205.99801,
      "gross": 94.84875039528742,
      "fees": 10.128080146677878,
      "net": 84.72067024860955,
      "hold_hours": 265.51666666666665,
      "net_bps_entry": 75.60296742245232,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "898f15a7-a199-4a9b-9a8e-86da6c4a7cea",
      "opened_at": 1715270400000.0,
      "closed_at": 1716490620000.0,
      "entry": 520.4976,
      "exit": 527.9046017608516,
      "qty": 24.060000000000002,
      "entry_notional": 12523.172256000002,
      "gross": 178.2124623660893,
      "fees": 11.351050638464741,
      "net": 166.86141172762456,
      "hold_hours": 338.95,
      "net_bps_entry": 133.24212772660638,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0239e614-fe39-4167-a95f-19f65a4af6a6",
      "opened_at": 1720195200000.0,
      "closed_at": 1720717380000.0,
      "entry": 554.3867,
      "exit": 558.2129752324591,
      "qty": 29.79,
      "entry_notional": 16515.179793,
      "gross": 113.98473917495721,
      "fees": 14.914954946328729,
      "net": 99.06978422862848,
      "hold_hours": 145.05,
      "net_bps_entry": 59.98710608686165,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8e11413f-ecae-4c2c-8b2d-a06e0bd17a3f",
      "opened_at": 1724083200000.0,
      "closed_at": 1724888460000.0,
      "entry": 557.6857,
      "exit": 555.6954287097703,
      "qty": 17.094,
      "entry_notional": 9533.0793558,
      "gross": -34.02169743518607,
      "fees": 8.564461656374167,
      "net": -42.58615909156023,
      "hold_hours": 223.68333333333334,
      "net_bps_entry": -44.67198635627687,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0b9ea504-dace-4a76-8e27-9365106902f4",
      "opened_at": 1749657600000.0,
      "closed_at": 1749669480000.0,
      "entry": 605.6622,
      "exit": 600.1483154819895,
      "qty": 16.525,
      "entry_notional": 10008.567855,
      "gross": -91.11694166012421,
      "fees": 8.966708445752944,
      "net": -100.08365010587715,
      "hold_hours": 3.3,
      "net_bps_entry": -99.9979732923309,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "083e27ba-c570-4a12-9ca7-b69656cba274",
      "opened_at": 1750924800000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.8881,
      "exit": 636.4563779329557,
      "qty": 17.412,
      "entry_notional": 10636.7835972,
      "gross": 445.1948553686234,
      "fees": 9.77344292239588,
      "net": 435.4214124462275,
      "hold_hours": 804.6666666666666,
      "net_bps_entry": 409.35439596688497,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f0bc07fa-7900-444d-a024-453374fa1fb0",
      "opened_at": 1766592000000.0,
      "closed_at": 1767139200000.0,
      "entry": 692.3451,
      "exit": 689.5951,
      "qty": 20.763,
      "entry_notional": 14375.1613113,
      "gross": -57.0982499999991,
      "fees": 12.91195096767,
      "net": -70.01020096766909,
      "hold_hours": 152.0,
      "net_bps_entry": -48.70220197990795,
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
