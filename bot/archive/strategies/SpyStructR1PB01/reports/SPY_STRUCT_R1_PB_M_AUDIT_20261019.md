# M snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "M",
    "url": "http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "n": 38,
    "net": 151.601263917207,
    "gross_before_fees": 488.3315562886869,
    "fees": 336.7302923714799,
    "pf": 1.0741227723616464,
    "sharpe": 0.10588870453443279,
    "dd_motor_pct": -7.718707541843617,
    "cagr_motor_pct": 0.28900965265155065,
    "time_exposure_pct": 15.996051556022653,
    "entry_price_notional_time": 0.1446681109984161,
    "mean_hold_hours": 192.25570175438597,
    "turnover_two_sides": 748289.5386032887,
    "total_entry_notional": 373900.60352350003,
    "net_bps_per_entry_notional": 4.054587301774139,
    "net_plus5bpsRT": -35.47112073361518,
    "net_plus10bpsRT": -222.54350538443737,
    "net_exbest": -224.72966914243096,
    "net_ex3best": -864.9054800934125,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 144.46030476585133,
        "fees": 3.2856353550544073
      },
      "2021": {
        "n": 5,
        "net": 234.68215351049327,
        "fees": 52.67854808982014
      },
      "2022": {
        "n": 6,
        "net": -412.94765746062245,
        "fees": 33.94331524034087
      },
      "2023": {
        "n": 10,
        "net": 325.2519289120951,
        "fees": 90.9032396483522
      },
      "2024": {
        "n": 10,
        "net": -145.87988688765023,
        "fees": 103.61885607926621
      },
      "2025": {
        "n": 6,
        "net": 6.034421077040099,
        "fees": 52.30069795864605
      }
    },
    "executed_order_types": {
      "MARKET": 39,
      "STOP": 37
    },
    "entry_order_types": {
      "MARKET": 38
    },
    "exit_order_types": {
      "STOP": 37,
      "MARKET": 1
    },
    "terminal_orders": [
      {
        "trade_id": "5664a1ca-00dc-4ece-9064-aeb07980f28f",
        "side": "sell",
        "type": "MARKET",
        "gross": 5.400550599999406,
        "net": -4.463883762050594,
        "fee": 9.86443436205,
        "exit_fee": 4.93343230491
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "662c49985688833746ff8da7bac9b73f829898abf69059257f4d948d5d36e48e",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "e6a0621f-8169-4474-8859-62d8ca839b75",
      "opened_at": 1604577600000.0,
      "closed_at": 1607609400000.0,
      "entry": 350.6699,
      "exit": 365.15479609028483,
      "qty": 10.200000000000001,
      "entry_notional": 3576.83298,
      "gross": 147.74594012090574,
      "fees": 3.2856353550544073,
      "net": 144.46030476585133,
      "hold_hours": 842.1666666666666,
      "net_bps_entry": 403.8776917278685,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "95226187-271a-4f43-b7cf-9b5e37b5f07e",
      "opened_at": 1612843200000.0,
      "closed_at": 1613572440000.0,
      "entry": 391.37449999999995,
      "exit": 390.68541426211965,
      "qty": 22.809,
      "entry_notional": 8926.8609705,
      "gross": -15.717356595312594,
      "fees": 8.02710206298211,
      "net": -23.744458658294704,
      "hold_hours": 202.56666666666666,
      "net_bps_entry": -26.59888928119462,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "4b70a7e5-233b-40ae-8c07-4ce1819c6a81",
      "opened_at": 1617940800000.0,
      "closed_at": 1618933920000.0,
      "entry": 410.1748,
      "exit": 413.4494018288913,
      "qty": 29.965,
      "entry_notional": 12290.887882,
      "gross": 98.1234438027277,
      "fees": 11.105954643511229,
      "net": 87.01748915921648,
      "hold_hours": 275.8666666666667,
      "net_bps_entry": 70.79837518219783,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ffefe01c-7e06-46a6-a3ec-e4bea9352b6c",
      "opened_at": 1625241600000.0,
      "closed_at": 1625736480000.0,
      "entry": 433.3751,
      "exit": 431.35318462668505,
      "qty": 34.278,
      "entry_notional": 14855.231677799999,
      "gross": -69.30721516648919,
      "fees": 13.338520263195079,
      "net": -82.64573542968427,
      "hold_hours": 137.46666666666667,
      "net_bps_entry": -55.6340939153389,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ad54ce96-3793-4098-9a2d-37ce1ebfa825",
      "opened_at": 1630396800000.0,
      "closed_at": 1630421580000.0,
      "entry": 454.2048,
      "exit": 451.60088025409726,
      "qty": 29.214000000000002,
      "entry_notional": 13269.1390272,
      "gross": -76.0709114568017,
      "fees": 11.90799321432444,
      "net": -87.97890467112613,
      "hold_hours": 6.883333333333334,
      "net_bps_entry": -66.30340106526947,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6c2a4477-a1f0-4a8d-84e5-1aa759c8e7d6",
      "opened_at": 1634616000000.0,
      "closed_at": 1636567560000.0,
      "entry": 448.5951,
      "exit": 465.96840726586606,
      "qty": 20.165,
      "entry_notional": 9045.9201915,
      "gross": 350.3327410161892,
      "fees": 8.298977905807286,
      "net": 342.03376311038187,
      "hold_hours": 542.1,
      "net_bps_entry": 378.1083138802993,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bbe68879-7b29-40ed-8765-31c1de0de92d",
      "opened_at": 1640692800000.0,
      "closed_at": 1641221460000.0,
      "entry": 480.0342,
      "exit": 475.6626499972957,
      "qty": 19.651,
      "entry_notional": 9433.1520642,
      "gross": -85.90532910314141,
      "fees": 8.451179459683585,
      "net": -94.356508562825,
      "hold_hours": 146.85,
      "net_bps_entry": -100.02648947102193,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "de832097-3502-4a36-8fba-399d44c9e297",
      "opened_at": 1647878400000.0,
      "closed_at": 1648826460000.0,
      "entry": 447.2248,
      "exit": 453.0820196035878,
      "qty": 12.222,
      "entry_notional": 5465.9815056,
      "gross": 71.58693799505,
      "fees": 4.951597477137772,
      "net": 66.63534051791223,
      "hold_hours": 263.35,
      "net_bps_entry": 121.90919499021919,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ffa7c382-a68e-4359-96bf-c21dfcc64abf",
      "opened_at": 1653897600000.0,
      "closed_at": 1654007880000.0,
      "entry": 419.2545,
      "exit": 411.6248599588101,
      "qty": 12.289,
      "entry_notional": 5152.2185505,
      "gross": -93.76064646618306,
      "fees": 4.594804404540217,
      "net": -98.35545087072327,
      "hold_hours": 30.633333333333333,
      "net_bps_entry": -190.8992211931272,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ab85cec2-1209-4cb7-afb3-eb5893be165f",
      "opened_at": 1659614400000.0,
      "closed_at": 1659707160000.0,
      "entry": 416.5054,
      "exit": 411.51916323090785,
      "qty": 17.753,
      "entry_notional": 7394.2203662,
      "gross": -88.52066136169287,
      "fees": 6.614964031967238,
      "net": -95.1356253936601,
      "hold_hours": 25.766666666666666,
      "net_bps_entry": -128.66214513775944,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6141c37d-fb6e-4b3f-a410-f11f79129e8f",
      "opened_at": 1667304000000.0,
      "closed_at": 1667314740000.0,
      "entry": 390.9733,
      "exit": 384.9763768330955,
      "qty": 15.077,
      "entry_notional": 5894.7044441,
      "gross": -90.415610587419,
      "fees": 5.264546974925661,
      "net": -95.68015756234466,
      "hold_hours": 2.9833333333333334,
      "net_bps_entry": -162.31544510787268,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "4dc2315a-3594-472e-87ee-dbbc2b621710",
      "opened_at": 1668153600000.0,
      "closed_at": 1668693480000.0,
      "entry": 398.674,
      "exit": 390.6386197853865,
      "qty": 11.448,
      "entry_notional": 4564.019952,
      "gross": -91.98903269689526,
      "fees": 4.066222892086397,
      "net": -96.05525558898167,
      "hold_hours": 149.96666666666667,
      "net_bps_entry": -210.46195371448647,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "73ace304-c12d-478a-b667-2fac3f7abf24",
      "opened_at": 1673496000000.0,
      "closed_at": 1674088080000.0,
      "entry": 396.7678,
      "exit": 392.19724641391247,
      "qty": 17.361,
      "entry_notional": 6888.285775800001,
      "gross": -79.3493808080666,
      "fees": 6.16374997685637,
      "net": -85.51313078492296,
      "hold_hours": 164.46666666666667,
      "net_bps_entry": -124.14283258303337,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5014bc3d-0d65-4e44-8adb-7dfa6873f06f",
      "opened_at": 1682697600000.0,
      "closed_at": 1683041580000.0,
      "entry": 414.3223,
      "exit": 411.4562541638049,
      "qty": 23.222,
      "entry_notional": 9621.3924506,
      "gross": -66.55531640812296,
      "fees": 8.629303313156345,
      "net": -75.1846197212793,
      "hold_hours": 95.55,
      "net_bps_entry": -78.14317949018981,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "4c5189ec-1adc-47b3-89bf-7ffa19bb67dc",
      "opened_at": 1685448000000.0,
      "closed_at": 1685473260000.0,
      "entry": 422.5967,
      "exit": 419.44010000000003,
      "qty": 25.086000000000002,
      "entry_notional": 10601.260816200001,
      "gross": -79.18646760000047,
      "fees": 9.50550082416,
      "net": -88.69196842416046,
      "hold_hours": 7.016666666666667,
      "net_bps_entry": -83.66171718804284,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1dfa27db-3200-423f-bb98-534c9f1db3e0",
      "opened_at": 1685980800000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.82769999999994,
      "exit": 437.4709,
      "qty": 23.315,
      "entry_notional": 9998.1178255,
      "gross": 201.51620800000092,
      "fees": 9.088988336549999,
      "net": 192.42721966345093,
      "hold_hours": 360.01666666666665,
      "net_bps_entry": 192.4634446422197,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "41aad0cc-58bf-439d-abb3-64921e6ead90",
      "opened_at": 1689264000000.0,
      "closed_at": 1690486680000.0,
      "entry": 449.7402,
      "exit": 454.3069085489496,
      "qty": 25.726,
      "entry_notional": 11570.0163852,
      "gross": 117.48314413027583,
      "fees": 10.465882161538623,
      "net": 107.01726196873722,
      "hold_hours": 339.6333333333333,
      "net_bps_entry": 92.49534175736373,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d79dd5bb-fdde-4a84-b2da-58e14bb63527",
      "opened_at": 1693497600000.0,
      "closed_at": 1693980480000.0,
      "entry": 452.77869999999996,
      "exit": 448.99063540628083,
      "qty": 21.555,
      "entry_notional": 9759.6448785,
      "gross": -81.65173231761582,
      "fees": 8.746937111107073,
      "net": -90.3986694287229,
      "hold_hours": 134.13333333333333,
      "net_bps_entry": -92.62495772552808,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f6e1d686-2c32-457b-b20c-f8984ed2c363",
      "opened_at": 1697083200000.0,
      "closed_at": 1697137200000.0,
      "entry": 438.6092,
      "exit": 433.81799370193175,
      "qty": 17.654,
      "entry_notional": 7743.2068168,
      "gross": -84.58395598609604,
      "fees": 6.930823354926257,
      "net": -91.5147793410223,
      "hold_hours": 15.0,
      "net_bps_entry": -118.18718201155087,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "88f6b581-c370-4390-aebc-64a28e18641b",
      "opened_at": 1699876800000.0,
      "closed_at": 1701705240000.0,
      "entry": 440.8829,
      "exit": 454.7454627095242,
      "qty": 22.151,
      "entry_notional": 9765.9971179,
      "gross": 307.06962657867007,
      "fees": 8.927578738070402,
      "net": 298.1420478405997,
      "hold_hours": 507.9,
      "net_bps_entry": 305.28582411122983,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "04727246-4448-4272-b146-dc955faec62e",
      "opened_at": 1702310400000.0,
      "closed_at": 1703102700000.0,
      "entry": 460.98470000000003,
      "exit": 471.5948268393657,
      "qty": 24.455000000000002,
      "entry_notional": 11273.380838500001,
      "gross": 259.47065185668725,
      "fees": 10.26280454798551,
      "net": 249.20784730870173,
      "hold_hours": 220.08333333333334,
      "net_bps_entry": 221.0586609986827,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a89ade45-35a5-4414-a8ab-c3655a09d468",
      "opened_at": 1703736000000.0,
      "closed_at": 1703866620000.0,
      "entry": 479.045,
      "exit": 476.2902848360642,
      "qty": 28.336000000000002,
      "entry_notional": 13574.219120000002,
      "gross": -78.05760888528494,
      "fees": 12.181671284001624,
      "net": -90.23928016928656,
      "hold_hours": 36.28333333333333,
      "net_bps_entry": -66.47843192418316,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a039a230-c4bf-4861-9d66-244280a0273b",
      "opened_at": 1706284800000.0,
      "closed_at": 1706727720000.0,
      "entry": 490.5781,
      "exit": 487.2833929545353,
      "qty": 24.356,
      "entry_notional": 11948.520203600001,
      "gross": -80.24588479933846,
      "fees": 10.717557535080298,
      "net": -90.96344233441876,
      "hold_hours": 123.03333333333333,
      "net_bps_entry": -76.12946271540147,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0dbf2975-3b93-4ef9-a412-fd566589a342",
      "opened_at": 1706846400000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.3401,
      "exit": 497.83465904825056,
      "qty": 19.981,
      "entry_notional": 9857.4285381,
      "gross": 89.80578434309427,
      "fees": 8.912098287244392,
      "net": 80.89368605584988,
      "hold_hours": 273.51666666666665,
      "net_bps_entry": 82.06367993760975,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2339b31a-2c94-45e5-a078-358b82ef39b9",
      "opened_at": 1708704000000.0,
      "closed_at": 1709056860000.0,
      "entry": 509.6641,
      "exit": 505.7652350494788,
      "qty": 21.131,
      "entry_notional": 10769.7120971,
      "gross": -82.38691526946423,
      "fees": 9.65566677551874,
      "net": -92.04258204498296,
      "hold_hours": 98.01666666666667,
      "net_bps_entry": -85.46429209539185,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "145c4e97-79e2-4ebf-a321-db6a48658eba",
      "opened_at": 1709913600000.0,
      "closed_at": 1709920380000.0,
      "entry": 518.2207,
      "exit": 513.9336185901562,
      "qty": 19.335,
      "entry_notional": 10019.7972345,
      "gross": -82.89071905932906,
      "fees": 8.980516687473303,
      "net": -91.87123574680236,
      "hold_hours": 1.8833333333333333,
      "net_bps_entry": -91.68971546696858,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6c3b54f4-fcec-47c8-b6b6-6280da463e50",
      "opened_at": 1715097600000.0,
      "closed_at": 1716490620000.0,
      "entry": 519.5671,
      "exit": 527.9046017608516,
      "qty": 19.649,
      "entry_notional": 10208.9739479,
      "gross": 163.82357209897418,
      "fees": 9.261797160554538,
      "net": 154.56177493841963,
      "hold_hours": 386.95,
      "net_bps_entry": 151.39795216169907,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "56663c25-195f-4151-a020-33a8c8482454",
      "opened_at": 1718870400000.0,
      "closed_at": 1718904600000.0,
      "entry": 550.3626,
      "exit": 547.5844835589712,
      "qty": 26.819,
      "entry_notional": 14760.1745694,
      "gross": -74.50630483195164,
      "fees": 13.25062927528562,
      "net": -87.75693410723726,
      "hold_hours": 9.5,
      "net_bps_entry": -59.45521422840771,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d26f2349-d354-4eaa-8cb6-100eb9571df0",
      "opened_at": 1720166400000.0,
      "closed_at": 1720717380000.0,
      "entry": 554.1423,
      "exit": 558.2129752324591,
      "qty": 27.491,
      "entry_notional": 15233.925969299999,
      "gross": 111.90693281553649,
      "fees": 13.76089149213699,
      "net": 98.1460413233995,
      "hold_hours": 153.05,
      "net_bps_entry": 64.42596709553875,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "93195f17-6d1a-403d-8f39-09fcd05f4854",
      "opened_at": 1724040000000.0,
      "closed_at": 1724888460000.0,
      "entry": 556.5274,
      "exit": 555.6954287097703,
      "qty": 15.241,
      "entry_notional": 8482.0341034,
      "gross": -12.680074434389098,
      "fees": 7.6281246595645245,
      "net": -20.308199093953622,
      "hold_hours": 235.68333333333334,
      "net_bps_entry": -23.942604859149455,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7e8ab061-7dc7-47e0-81d2-ddb7d647bff9",
      "opened_at": 1730952000000.0,
      "closed_at": 1731633120000.0,
      "entry": 593.3962,
      "exit": 593.0934959149074,
      "qty": 12.655000000000001,
      "entry_notional": 7509.428911000001,
      "gross": -3.8307201968473237,
      "fees": 6.75676219581142,
      "net": -10.587482392658742,
      "hold_hours": 189.2,
      "net_bps_entry": -14.098918197560844,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "652cb822-1dc0-4c7a-ab22-0f48ab89c246",
      "opened_at": 1733500800000.0,
      "closed_at": 1733758680000.0,
      "entry": 609.6117,
      "exit": 606.9570281620346,
      "qty": 26.842000000000002,
      "entry_notional": 16363.197251400003,
      "gross": -71.25670147466917,
      "fees": 14.6948120105964,
      "net": -85.95151348526556,
      "hold_hours": 71.63333333333334,
      "net_bps_entry": -52.527334459597576,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "74c0a462-13b1-44ba-b4ac-c4c54ccf3c03",
      "opened_at": 1737388800000.0,
      "closed_at": 1737421260000.0,
      "entry": 601.7926,
      "exit": 595.9026286991198,
      "qty": 14.43,
      "entry_notional": 8683.867218,
      "gross": -84.99228587170182,
      "fees": 7.777233967557732,
      "net": -92.76951983925956,
      "hold_hours": 9.016666666666667,
      "net_bps_entry": -106.82973093711757,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1b905c73-4cfa-4d09-95bc-d980790233b9",
      "opened_at": 1747396800000.0,
      "closed_at": 1747851960000.0,
      "entry": 592.9375,
      "exit": 586.9411525531616,
      "qty": 14.118,
      "entry_notional": 8371.091625000001,
      "gross": -84.65643325446581,
      "fees": 7.495887067535491,
      "net": -92.1523203220013,
      "hold_hours": 126.43333333333334,
      "net_bps_entry": -110.08399435838369,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "966e7b0e-057e-4921-8166-fd85bb6ec33b",
      "opened_at": 1749528000000.0,
      "closed_at": 1749776700000.0,
      "entry": 603.2098,
      "exit": 597.9222679220612,
      "qty": 15.487,
      "entry_notional": 9341.910172599999,
      "gross": -81.88800929103672,
      "fees": 8.370869551159032,
      "net": -90.25887884219576,
      "hold_hours": 69.08333333333333,
      "net_bps_entry": -96.61715556517207,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f86b7358-26ee-4db3-8611-0993261d58f6",
      "opened_at": 1750867200000.0,
      "closed_at": 1753821600000.0,
      "entry": 610.1352,
      "exit": 636.4563779329557,
      "qty": 14.609,
      "entry_notional": 8913.465136800001,
      "gross": 384.5260884225481,
      "fees": 8.195155362910148,
      "net": 376.33093305963797,
      "hold_hours": 820.6666666666666,
      "net_bps_entry": 422.2049756002563,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b5ddbb2a-ab98-4be8-a8f1-7ad73326bd7a",
      "opened_at": 1761652800000.0,
      "closed_at": 1761852120000.0,
      "entry": 687.9354,
      "exit": 683.2740053587016,
      "qty": 17.174,
      "entry_notional": 11814.602559599998,
      "gross": -80.05479156965703,
      "fees": 10.597117647433652,
      "net": -90.65190921709068,
      "hold_hours": 55.36666666666667,
      "net_bps_entry": -76.72869972543523,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5664a1ca-00dc-4ece-9064-aeb07980f28f",
      "opened_at": 1766505600000.0,
      "closed_at": 1767139200000.0,
      "entry": 689.2554,
      "exit": 689.5951,
      "qty": 15.898,
      "entry_notional": 10957.7823492,
      "gross": 5.400550599999406,
      "fees": 9.86443436205,
      "net": -4.463883762050594,
      "hold_hours": 176.0,
      "net_bps_entry": -4.073710920509834,
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
