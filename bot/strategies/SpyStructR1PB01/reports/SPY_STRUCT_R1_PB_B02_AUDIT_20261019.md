# B02 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B02",
    "url": "http://localhost:9200/#/backtest/8ee013fd-c6fa-4a29-9ab1-7aa52538c983",
    "n": 29,
    "net": -1007.009155528648,
    "gross_before_fees": -745.6811985279555,
    "fees": 261.32795700069244,
    "pf": 0.4384261688221961,
    "sharpe": -0.7444427328881174,
    "dd_motor_pct": -13.995269724132719,
    "cagr_motor_pct": -2.0152012902323047,
    "time_exposure_pct": 7.460150639341391,
    "entry_price_notional_time": 0.06950447682629166,
    "mean_hold_hours": 117.48965517241379,
    "turnover_two_sides": 580728.7933348721,
    "total_entry_notional": 290737.2372667,
    "net_bps_per_entry_notional": -34.63640106770689,
    "net_plus5bpsRT": -1152.191353862366,
    "net_plus10bpsRT": -1297.373552196084,
    "net_exbest": -1347.2255609083106,
    "net_ex3best": -1603.964316465479,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": -93.67371989239523,
        "fees": 5.653982464637509
      },
      "2021": {
        "n": 3,
        "net": 167.67070385884574,
        "fees": 29.787538197625416
      },
      "2022": {
        "n": 4,
        "net": 40.77492660789163,
        "fees": 21.168514330802413
      },
      "2023": {
        "n": 9,
        "net": -561.2690220169267,
        "fees": 85.29454901591954
      },
      "2024": {
        "n": 8,
        "net": -312.151868965998,
        "fees": 85.82394671385654
      },
      "2025": {
        "n": 4,
        "net": -248.36017512006552,
        "fees": 33.599426277851
      }
    },
    "executed_order_types": {
      "MARKET": 30,
      "STOP": 28
    },
    "entry_order_types": {
      "MARKET": 29
    },
    "exit_order_types": {
      "STOP": 28,
      "MARKET": 1
    },
    "terminal_orders": [
      {
        "trade_id": "bb02ff52-e469-4851-ae97-0acf15b0d76e",
        "side": "sell",
        "type": "MARKET",
        "gross": -14.319330000000264,
        "net": -24.540814874310264,
        "fee": 10.221484874309999,
        "exit_fee": 5.107520587904999
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "ffafcd565737ff12b67e85f16bf6c4db143a1b9e3e5b0c254963cc7e6c2afefc",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "3f6395d4-c942-4f49-888c-c3727b75b338",
      "opened_at": 1605700800000.0,
      "closed_at": 1605733200000.0,
      "entry": 361.9736,
      "exit": 356.93728155703167,
      "qty": 17.477,
      "entry_notional": 6326.2126072,
      "gross": -88.01973742775772,
      "fees": 5.653982464637509,
      "net": -93.67371989239523,
      "hold_hours": 9.0,
      "net_bps_entry": -148.07235499133103,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "95bc0e0b-7b8b-403c-84de-1dbe644d4b47",
      "opened_at": 1618891200000.0,
      "closed_at": 1618916340000.0,
      "entry": 417.0536,
      "exit": 414.3891559373136,
      "qty": 28.667,
      "entry_notional": 11955.675551200002,
      "gross": -76.3816179450314,
      "fees": 10.725736268004738,
      "net": -87.10735421303613,
      "hold_hours": 6.983333333333333,
      "net_bps_entry": -72.85857987697993,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "daeeb40a-2df8-4d71-8f9b-4529f36fed7b",
      "opened_at": 1630468800000.0,
      "closed_at": 1631088660000.0,
      "entry": 453.5054,
      "exit": 450.8740226851664,
      "qty": 28.12,
      "entry_notional": 12752.571848000001,
      "gross": -73.9943300931227,
      "fees": 11.444017214658096,
      "net": -85.43834730778079,
      "hold_hours": 172.18333333333334,
      "net_bps_entry": -66.99695428195542,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "419915f6-3e6c-429f-a949-8130297e2b82",
      "opened_at": 1634572800000.0,
      "closed_at": 1636567560000.0,
      "entry": 447.2051,
      "exit": 465.96840726586606,
      "qty": 18.538,
      "entry_notional": 8290.2881438,
      "gross": 347.8341900946252,
      "fees": 7.617784714962582,
      "net": 340.21640537966266,
      "hold_hours": 554.1,
      "net_bps_entry": 410.3794699031033,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ca95c302-aa70-4651-8b38-4696d0b32a37",
      "opened_at": 1647936000000.0,
      "closed_at": 1648826460000.0,
      "entry": 446.2936,
      "exit": 453.0820196035878,
      "qty": 12.463000000000001,
      "entry_notional": 5562.1571368,
      "gross": 84.60407351951471,
      "fees": 5.044013256203782,
      "net": 79.56006026331093,
      "hold_hours": 247.35,
      "net_bps_entry": 143.0381384533899,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "072aea45-7e49-4027-a437-661aa8c337da",
      "opened_at": 1659456000000.0,
      "closed_at": 1661122860000.0,
      "entry": 411.5545,
      "exit": 421.4433,
      "qty": 16.312,
      "entry_notional": 6713.2770040000005,
      "gross": 161.3061056000006,
      "fees": 6.11453705112,
      "net": 155.19156854888058,
      "hold_hours": 463.01666666666665,
      "net_bps_entry": 231.1711083222279,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b40b4f90-8f55-4b93-a813-51944fc27a43",
      "opened_at": 1668441600000.0,
      "closed_at": 1668690060000.0,
      "entry": 399.1501,
      "exit": 392.0945616739454,
      "qty": 13.198,
      "entry_notional": 5267.9830198,
      "gross": -93.11899482726858,
      "fees": 4.699281170147729,
      "net": -97.81827599741631,
      "hold_hours": 69.01666666666667,
      "net_bps_entry": -185.68449372323528,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "aff33d4c-a46f-45d0-baf5-d46eeea18337",
      "opened_at": 1671033600000.0,
      "closed_at": 1671046500000.0,
      "entry": 404.2822,
      "exit": 398.1054429049801,
      "qty": 14.708,
      "entry_notional": 5946.1825976,
      "gross": -90.84774335355269,
      "fees": 5.310682853330902,
      "net": -96.15842620688359,
      "hold_hours": 3.5833333333333335,
      "net_bps_entry": -161.7145532088017,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0c194fb0-1ca7-4a10-af19-d7117607d589",
      "opened_at": 1675440000000.0,
      "closed_at": 1675671840000.0,
      "entry": 416.8906,
      "exit": 411.3893749902029,
      "qty": 16.078,
      "entry_notional": 6702.7670668,
      "gross": -88.4486957075178,
      "fees": 5.992688447051616,
      "net": -94.44138415456942,
      "hold_hours": 64.4,
      "net_bps_entry": -140.89909915317574,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a13af1f4-2964-4d99-a942-ebc2b22d7124",
      "opened_at": 1682697600000.0,
      "closed_at": 1683041580000.0,
      "entry": 414.3223,
      "exit": 411.4562541638049,
      "qty": 23.55,
      "entry_notional": 9757.290165,
      "gross": -67.49537944239455,
      "fees": 8.751188227750921,
      "net": -76.24656767014547,
      "hold_hours": 95.55,
      "net_bps_entry": -78.1431794901894,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b3dcc542-c293-4647-8ec4-cb57d98cce45",
      "opened_at": 1688572800000.0,
      "closed_at": 1688632560000.0,
      "entry": 445.2962,
      "exit": 442.50283192127137,
      "qty": 27.332,
      "entry_notional": 12170.835738400001,
      "gross": -76.34833632781192,
      "fees": 10.919395413212484,
      "net": -87.2677317410244,
      "hold_hours": 16.6,
      "net_bps_entry": -71.7023330334559,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2ec7f753-334f-464d-98b5-c2c9838bd2b0",
      "opened_at": 1689336000000.0,
      "closed_at": 1690486680000.0,
      "entry": 451.2319,
      "exit": 454.30691509823964,
      "qty": 27.908,
      "entry_notional": 12592.9798652,
      "gross": 85.81752136167233,
      "fees": 11.372299763292753,
      "net": 74.44522159837958,
      "hold_hours": 319.6333333333333,
      "net_bps_entry": 59.116446143223655,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "08bc6bd4-8964-4a27-b67e-575963385372",
      "opened_at": 1693800000000.0,
      "closed_at": 1693988220000.0,
      "entry": 451.7414,
      "exit": 448.27023791849376,
      "qty": 22.947,
      "entry_notional": 10366.1099058,
      "gross": -79.65275628432391,
      "fees": 9.293655174892054,
      "net": -88.94641145921597,
      "hold_hours": 52.28333333333333,
      "net_bps_entry": -85.80500522134061,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a240f194-e2cb-4a9f-b4e6-e0e525fddc41",
      "opened_at": 1697083200000.0,
      "closed_at": 1697137200000.0,
      "entry": 438.6092,
      "exit": 433.81798494111064,
      "qty": 17.505,
      "entry_notional": 7677.8540459999995,
      "gross": -83.87021960585844,
      "fees": 6.872327042577363,
      "net": -90.7425466484358,
      "hold_hours": 15.0,
      "net_bps_entry": -118.1873816626024,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "80893f7a-1d2b-4ad2-b67a-55a628c88170",
      "opened_at": 1699444800000.0,
      "closed_at": 1699558980000.0,
      "entry": 438.0102,
      "exit": 434.76325886957164,
      "qty": 23.914,
      "entry_notional": 10474.5759228,
      "gross": -77.64735019306318,
      "fees": 9.392177022933122,
      "net": -87.0395272159963,
      "hold_hours": 31.716666666666665,
      "net_bps_entry": -83.09599152986942,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f97eb90d-c23e-4508-98f8-46871f2f2f96",
      "opened_at": 1700827200000.0,
      "closed_at": 1701176880000.0,
      "entry": 456.1779,
      "exit": 454.0940696069851,
      "qty": 32.765,
      "entry_notional": 14946.6688935,
      "gross": -68.2767028271337,
      "fees": 13.42127748787779,
      "net": -81.69798031501149,
      "hold_hours": 97.13333333333334,
      "net_bps_entry": -54.65965754452504,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "12d1f3d8-3aec-4467-bed5-a211efde1aa6",
      "opened_at": 1702872000000.0,
      "closed_at": 1703102700000.0,
      "entry": 472.51290000000006,
      "exit": 471.5948268393657,
      "qty": 21.842,
      "entry_notional": 10320.6267618,
      "gross": -20.052553974575858,
      "fees": 9.279540436331441,
      "net": -29.3320944109073,
      "hold_hours": 64.08333333333333,
      "net_bps_entry": -28.420846027951452,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5601f43f-65eb-4b62-b86c-2801ee001e62",
      "opened_at": 1706270400000.0,
      "closed_at": 1706731380000.0,
      "entry": 488.8349,
      "exit": 486.48758661586646,
      "qty": 23.078,
      "entry_notional": 11281.3318222,
      "gross": -54.17129827903409,
      "fees": 10.128821555754435,
      "net": -64.30011983478852,
      "hold_hours": 128.05,
      "net_bps_entry": -56.99692274652834,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7770f3fa-211f-4c46-9447-476289b5e4f2",
      "opened_at": 1707811200000.0,
      "closed_at": 1707831060000.0,
      "entry": 502.1729,
      "exit": 499.44061888103136,
      "qty": 25.749,
      "entry_notional": 12930.4500021,
      "gross": -70.3535065323249,
      "fees": 11.605745923950453,
      "net": -81.95925245627535,
      "hold_hours": 5.516666666666667,
      "net_bps_entry": -63.384686877072774,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "999cf62e-c33e-41bb-97b9-436694c99884",
      "opened_at": 1708574400000.0,
      "closed_at": 1709657040000.0,
      "entry": 501.88400000000007,
      "exit": 507.6970020582238,
      "qty": 18.95,
      "entry_notional": 9510.7018,
      "gross": 110.15638900333943,
      "fees": 8.609201995051503,
      "net": 101.54718700828792,
      "hold_hours": 300.73333333333335,
      "net_bps_entry": 106.77149714470904,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6b9b8acc-c218-4a52-89be-c3c9a49414c0",
      "opened_at": 1716393600000.0,
      "closed_at": 1716404580000.0,
      "entry": 532.0686,
      "exit": 529.7114242855966,
      "qty": 28.240000000000002,
      "entry_notional": 15025.617264,
      "gross": -66.56664217475009,
      "fees": 13.493100548621362,
      "net": -80.05974272337144,
      "hold_hours": 3.05,
      "net_bps_entry": -53.282165595411,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a873716d-1990-4254-b1c2-a08b48d10098",
      "opened_at": 1718856000000.0,
      "closed_at": 1718904720000.0,
      "entry": 549.4252,
      "exit": 546.6287053838354,
      "qty": 24.559,
      "entry_notional": 13493.3334868,
      "gross": -68.6791112783867,
      "fees": 12.113094538044725,
      "net": -80.79220581643142,
      "hold_hours": 13.533333333333333,
      "net_bps_entry": -59.8756459220898,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "98c793a7-30e4-47cd-8a66-c9ddfea00bb0",
      "opened_at": 1720440000000.0,
      "closed_at": 1720717380000.0,
      "entry": 556.3677,
      "exit": 558.2129752324591,
      "qty": 26.212,
      "entry_notional": 14583.5101524,
      "gross": 48.3683543932184,
      "fees": 13.146924896636948,
      "net": 35.22142949658145,
      "hold_hours": 77.05,
      "net_bps_entry": 24.151544537982907,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0a5fe8a7-9a4f-4eef-bce1-431647403787",
      "opened_at": 1727107200000.0,
      "closed_at": 1727796720000.0,
      "entry": 572.1031,
      "exit": 568.7706301196654,
      "qty": 15.214,
      "entry_notional": 8703.976563400001,
      "gross": -50.70019675941148,
      "fees": 7.810763818518266,
      "net": -58.51096057792975,
      "hold_hours": 191.53333333333333,
      "net_bps_entry": -67.2232515238688,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "93fc35b6-e6d0-4a0d-919f-cee046a9f49b",
      "opened_at": 1731513600000.0,
      "closed_at": 1731617400000.0,
      "entry": 598.7226,
      "exit": 594.2441900641345,
      "qty": 16.609,
      "entry_notional": 9944.183663400003,
      "gross": -74.381910624792,
      "fees": 8.916293437278847,
      "net": -83.29820406207085,
      "hold_hours": 28.833333333333332,
      "net_bps_entry": -83.76575381310936,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8ac4631f-3271-4ef1-9d1f-2f75ca2fea4f",
      "opened_at": 1747324800000.0,
      "closed_at": 1747858320000.0,
      "entry": 588.0746,
      "exit": 583.6916038169531,
      "qty": 12.201,
      "entry_notional": 7175.098194600001,
      "gross": -53.47693642935519,
      "fees": 6.433523753746791,
      "net": -59.91046018310198,
      "hold_hours": 148.2,
      "net_bps_entry": -83.49775648811435,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "57397459-5190-4bc0-bb39-c5c66b1a66fb",
      "opened_at": 1761652800000.0,
      "closed_at": 1761852120000.0,
      "entry": 687.9354,
      "exit": 683.2740053587016,
      "qty": 15.388,
      "entry_notional": 10585.949935199998,
      "gross": -71.72954074029803,
      "fees": 9.495076648346863,
      "net": -81.2246173886449,
      "hold_hours": 55.36666666666667,
      "net_bps_entry": -76.72869972543502,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5cbd713e-2cec-4b52-8b10-c7e3220a0e66",
      "opened_at": 1762171200000.0,
      "closed_at": 1762234920000.0,
      "entry": 686.5948,
      "exit": 680.3821706298463,
      "qty": 12.11,
      "entry_notional": 8314.663027999999,
      "gross": -75.23494167256104,
      "fees": 7.449341001447346,
      "net": -82.68428267400839,
      "hold_hours": 17.7,
      "net_bps_entry": -99.44393704900051,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bb02ff52-e469-4851-ae97-0acf15b0d76e",
      "opened_at": 1766577600000.0,
      "closed_at": 1767139200000.0,
      "entry": 690.4651,
      "exit": 689.5951,
      "qty": 16.459,
      "entry_notional": 11364.3650809,
      "gross": -14.319330000000264,
      "fees": 10.221484874309999,
      "net": -24.540814874310264,
      "hold_hours": 156.0,
      "net_bps_entry": -21.594532294246534,
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
