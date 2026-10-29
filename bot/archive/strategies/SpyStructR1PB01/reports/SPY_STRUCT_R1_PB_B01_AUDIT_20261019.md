# B01 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B01",
    "url": "http://localhost:9200/#/backtest/c301e870-ad6a-40c3-9f57-45aee52856b6",
    "n": 44,
    "net": -575.413938725543,
    "gross_before_fees": -173.65972638865787,
    "fees": 401.7542123368851,
    "pf": 0.776654430749012,
    "sharpe": -0.2901654726068019,
    "dd_motor_pct": -13.096411840410394,
    "cagr_motor_pct": -1.1302481881073412,
    "time_exposure_pct": 16.125853914871254,
    "entry_price_notional_time": 0.1518861112020365,
    "mean_hold_hours": 167.38636363636363,
    "turnover_two_sides": 892787.1385264114,
    "total_entry_notional": 446480.3991264,
    "net_bps_per_entry_notional": -12.887776033425409,
    "net_plus5bpsRT": -798.6107233571458,
    "net_plus10bpsRT": -1021.8075079887486,
    "net_exbest": -1048.0193736097106,
    "net_ex3best": -1680.8466648408644,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 97.02437104957555,
        "fees": 3.081955249484577
      },
      "2021": {
        "n": 3,
        "net": 424.2642021595499,
        "fees": 30.48456395318073
      },
      "2022": {
        "n": 7,
        "net": -211.89999498867604,
        "fees": 43.08887623970296
      },
      "2023": {
        "n": 12,
        "net": 20.984385952450452,
        "fees": 107.57051368390636
      },
      "2024": {
        "n": 12,
        "net": -281.7089237362266,
        "fees": 137.16896633667017
      },
      "2025": {
        "n": 9,
        "net": -624.0779791622161,
        "fees": 80.35933687394028
      }
    },
    "executed_order_types": {
      "MARKET": 45,
      "STOP": 43
    },
    "entry_order_types": {
      "MARKET": 44
    },
    "exit_order_types": {
      "STOP": 43,
      "MARKET": 1
    },
    "terminal_orders": [
      {
        "trade_id": "c99c44fb-4967-4e59-bab2-b1f485acc267",
        "side": "sell",
        "type": "MARKET",
        "gross": 27.95315069999924,
        "net": 18.63695606452424,
        "fee": 9.316194635475,
        "exit_fee": 4.664386776644999
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "e2afcb9d7c4c920060e8234862ac410496a301c856e740fa927fdd7e0ebe155b",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "0a706cc3-44a3-4995-99f0-d4897c80149f",
      "opened_at": 1604995200000.0,
      "closed_at": 1607609400000.0,
      "entry": 354.6339,
      "exit": 365.15479609028483,
      "qty": 9.515,
      "entry_notional": 3374.3415585000002,
      "gross": 100.10632629906013,
      "fees": 3.081955249484577,
      "net": 97.02437104957555,
      "hold_hours": 726.1666666666666,
      "net_bps_entry": 287.5357143534275,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "774ae267-bf85-483e-9467-528ba855804a",
      "opened_at": 1617782400000.0,
      "closed_at": 1618933920000.0,
      "entry": 407.5548,
      "exit": 413.44940189745466,
      "qty": 28.628,
      "entry_notional": 11667.4788144,
      "gross": 168.75066312033232,
      "fees": 10.57666873136415,
      "net": 158.17399438896817,
      "hold_hours": 319.8666666666667,
      "net_bps_entry": 135.56827220783111,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "de7bd930-c49f-42b8-8f5c-a54632be657d",
      "opened_at": 1630468800000.0,
      "closed_at": 1631088660000.0,
      "entry": 453.5054,
      "exit": 450.8740226851664,
      "qty": 29.368000000000002,
      "entry_notional": 13318.5465872,
      "gross": -77.2782889820337,
      "fees": 11.951916698438085,
      "net": -89.23020568047178,
      "hold_hours": 172.18333333333334,
      "net_bps_entry": -66.99695428195437,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5efb52ed-3a06-4230-936d-81c0d6426b8e",
      "opened_at": 1634572800000.0,
      "closed_at": 1636567560000.0,
      "entry": 447.2051,
      "exit": 465.968407265866,
      "qty": 19.361,
      "entry_notional": 8658.3379411,
      "gross": 363.27639197443204,
      "fees": 7.955978523378494,
      "net": 355.3204134510535,
      "hold_hours": 554.1,
      "net_bps_entry": 410.3794699031021,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fb726013-32c6-4d76-b8c0-69652953225d",
      "opened_at": 1640937600000.0,
      "closed_at": 1641411600000.0,
      "entry": 477.5499,
      "exit": 474.09776916075975,
      "qty": 24.142,
      "entry_notional": 11529.0096858,
      "gross": -83.34134272093797,
      "fees": 10.338605112995577,
      "net": -93.67994783393355,
      "hold_hours": 131.66666666666666,
      "net_bps_entry": -81.2558497104195,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "806e8572-3e6d-4485-b1a5-98de604e5674",
      "opened_at": 1647936000000.0,
      "closed_at": 1648826460000.0,
      "entry": 446.2936,
      "exit": 453.0820196035878,
      "qty": 12.9,
      "entry_notional": 5757.187440000001,
      "gross": 87.5706128862821,
      "fees": 5.220875471798827,
      "net": 82.34973741448329,
      "hold_hours": 247.35,
      "net_bps_entry": 143.0381384533891,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c9af559e-94c3-4879-b5c0-b18c1bc4a713",
      "opened_at": 1659456000000.0,
      "closed_at": 1661122860000.0,
      "entry": 411.5545,
      "exit": 421.4433,
      "qty": 16.885,
      "entry_notional": 6949.097732500001,
      "gross": 166.97238800000014,
      "fees": 6.329325533850001,
      "net": 160.64306246615013,
      "hold_hours": 463.01666666666665,
      "net_bps_entry": 231.1711083222272,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c325c538-ac6c-49b8-b32f-42ba57e6d6f6",
      "opened_at": 1666886400000.0,
      "closed_at": 1667417160000.0,
      "entry": 383.2009,
      "exit": 378.7789237622205,
      "qty": 13.552,
      "entry_notional": 5193.1385967999995,
      "gross": -59.92662197438767,
      "fees": 4.646857757231525,
      "net": -64.5734797316192,
      "hold_hours": 147.43333333333334,
      "net_bps_entry": -124.34384048869644,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d5188601-36a7-4bd7-82e9-e696a93f1393",
      "opened_at": 1668441600000.0,
      "closed_at": 1668690060000.0,
      "entry": 399.1501,
      "exit": 392.0945616739454,
      "qty": 13.578,
      "entry_notional": 5419.6600578,
      "gross": -95.80009939116917,
      "fees": 4.834584007293973,
      "net": -100.63468339846314,
      "hold_hours": 69.01666666666667,
      "net_bps_entry": -185.684493723235,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d0d07138-b11d-462f-bd6c-8287fc4fdeb8",
      "opened_at": 1669910400000.0,
      "closed_at": 1669987860000.0,
      "entry": 407.8565,
      "exit": 402.5537245713193,
      "qty": 17.291,
      "entry_notional": 7052.2467415,
      "gross": -91.69028993731717,
      "fees": 6.305761436878207,
      "net": -97.99605137419539,
      "hold_hours": 21.516666666666666,
      "net_bps_entry": -138.95720749179546,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1dc60823-c320-4148-9f66-8462250f545f",
      "opened_at": 1671033600000.0,
      "closed_at": 1671046500000.0,
      "entry": 404.2822,
      "exit": 398.1054429049801,
      "qty": 14.991,
      "entry_notional": 6060.5944602,
      "gross": -92.59576561144331,
      "fees": 5.41286691965485,
      "net": -98.00863253109816,
      "hold_hours": 3.5833333333333335,
      "net_bps_entry": -161.71455320880168,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6dce1b97-9221-4064-8a90-120d9628c9b3",
      "opened_at": 1675440000000.0,
      "closed_at": 1675671840000.0,
      "entry": 416.8906,
      "exit": 411.3893749902029,
      "qty": 16.387,
      "entry_notional": 6831.5862622,
      "gross": -90.14857423554531,
      "fees": 6.107860777574005,
      "net": -96.25643501311932,
      "hold_hours": 64.4,
      "net_bps_entry": -140.89909915317605,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5e30b130-2cef-4293-a8a1-019456886796",
      "opened_at": 1675699200000.0,
      "closed_at": 1676023320000.0,
      "entry": 411.3763,
      "exit": 406.6714499723386,
      "qty": 16.65,
      "entry_notional": 6849.415395,
      "gross": -78.33575296056279,
      "fees": 6.129222766667747,
      "net": -84.46497572723054,
      "hold_hours": 90.03333333333333,
      "net_bps_entry": -123.3170582541819,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1d5f5cba-0fa9-4a84-ae0e-ba26a6e9cba3",
      "opened_at": 1682697600000.0,
      "closed_at": 1683041580000.0,
      "entry": 414.3223,
      "exit": 411.4562541638049,
      "qty": 23.805,
      "entry_notional": 9862.9423515,
      "gross": -68.22622113062425,
      "fees": 8.845946316841218,
      "net": -77.07216744746547,
      "hold_hours": 95.55,
      "net_bps_entry": -78.14317949018935,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2e5f9651-7364-41d8-a445-5f46b3e8478a",
      "opened_at": 1686312000000.0,
      "closed_at": 1687253820000.0,
      "entry": 428.8887,
      "exit": 439.0924701318884,
      "qty": 28.279,
      "entry_notional": 12128.5435473,
      "gross": 288.5524155596722,
      "fees": 11.045537779571852,
      "net": 277.50687778010035,
      "hold_hours": 261.6166666666667,
      "net_bps_entry": 228.80478327661828,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "af346ef6-e4e2-4f70-94f4-50b69a935e2f",
      "opened_at": 1688572800000.0,
      "closed_at": 1688632560000.0,
      "entry": 445.2962,
      "exit": 442.50283192127137,
      "qty": 28.39,
      "entry_notional": 12641.959118,
      "gross": -79.3037197551057,
      "fees": 11.342076532310204,
      "net": -90.6457962874159,
      "hold_hours": 16.6,
      "net_bps_entry": -71.70233303345499,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "970c80a2-ebf7-4351-aa0b-7db6ca8ed551",
      "opened_at": 1689336000000.0,
      "closed_at": 1690486680000.0,
      "entry": 451.2319,
      "exit": 454.30691509823964,
      "qty": 28.989,
      "entry_notional": 13080.7615491,
      "gross": 89.14161268286989,
      "fees": 11.81279911989729,
      "net": 77.3288135629726,
      "hold_hours": 319.6333333333333,
      "net_bps_entry": 59.116446143224046,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "19f82668-2664-4766-bbd2-131f06f3f5c0",
      "opened_at": 1690790400000.0,
      "closed_at": 1690966320000.0,
      "entry": 457.7129,
      "exit": 454.5754344585128,
      "qty": 25.752,
      "entry_notional": 11787.022600799999,
      "gross": -80.79601262437791,
      "fees": 10.571962135039028,
      "net": -91.36797475941694,
      "hold_hours": 48.86666666666667,
      "net_bps_entry": -77.51573731029895,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "27479fc8-8538-4f56-8f73-1adea32d6dd2",
      "opened_at": 1693800000000.0,
      "closed_at": 1693988220000.0,
      "entry": 451.7414,
      "exit": 448.27023791849376,
      "qty": 23.624,
      "entry_notional": 10671.9388336,
      "gross": -82.00273301350353,
      "fees": 9.567843720383923,
      "net": -91.57057673388745,
      "hold_hours": 52.28333333333333,
      "net_bps_entry": -85.80500522134051,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0557fdd4-5a9b-40c8-9418-9ed8b30ba71b",
      "opened_at": 1697083200000.0,
      "closed_at": 1697137200000.0,
      "entry": 438.6092,
      "exit": 433.81798494111064,
      "qty": 18.022000000000002,
      "entry_notional": 7904.615002400001,
      "gross": -86.3472777913039,
      "fees": 7.075297227153914,
      "net": -93.4225750184578,
      "hold_hours": 15.0,
      "net_bps_entry": -118.18738166260194,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0a2d5a4e-2347-4c42-8782-f7469c1905e2",
      "opened_at": 1697169600000.0,
      "closed_at": 1697662140000.0,
      "entry": 435.4266,
      "exit": 430.4345629004954,
      "qty": 17.258,
      "entry_notional": 7514.5922628,
      "gross": -86.15257626325092,
      "fees": 6.724364377201537,
      "net": -92.87694064045246,
      "hold_hours": 136.81666666666666,
      "net_bps_entry": -123.59544921715518,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c7cf41eb-d076-4ef2-875b-318e2ec5874f",
      "opened_at": 1699444800000.0,
      "closed_at": 1699558980000.0,
      "entry": 438.0102,
      "exit": 434.76325886957164,
      "qty": 24.392,
      "entry_notional": 10683.9447984,
      "gross": -79.19938805340826,
      "fees": 9.579910593935967,
      "net": -88.77929864734422,
      "hold_hours": 31.716666666666665,
      "net_bps_entry": -83.09599152986974,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b8b20636-8792-418b-99f1-79469862caff",
      "opened_at": 1700121600000.0,
      "closed_at": 1703102040000.0,
      "entry": 450.0376,
      "exit": 472.8385249347052,
      "qty": 21.112000000000002,
      "entry_notional": 9501.1938112,
      "gross": 481.37312722149727,
      "fees": 8.767692337329674,
      "net": 472.6054348841676,
      "hold_hours": 827.9,
      "net_bps_entry": 497.41689757666103,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "23311bec-9cbb-4a45-a983-a6bc1c761da5",
      "opened_at": 1706169600000.0,
      "closed_at": 1706731380000.0,
      "entry": 487.2873000000001,
      "exit": 486.48758661586646,
      "qty": 25.391000000000002,
      "entry_notional": 12372.711834300002,
      "gross": -20.305522536535136,
      "fees": 11.12630316572856,
      "net": -31.431825702263694,
      "hold_hours": 156.05,
      "net_bps_entry": -25.404152398609533,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1b83d2c7-2ccb-4077-8ccf-e01458a66988",
      "opened_at": 1707811200000.0,
      "closed_at": 1707831060000.0,
      "entry": 502.1729,
      "exit": 499.44061888103136,
      "qty": 27.946,
      "entry_notional": 14033.723863400002,
      "gross": -76.35632815069948,
      "fees": 12.595991129392186,
      "net": -88.95231928009167,
      "hold_hours": 5.516666666666667,
      "net_bps_entry": -63.38468687707302,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8d75a185-5811-4c7b-89e4-16fac2f323c0",
      "opened_at": 1708574400000.0,
      "closed_at": 1709657040000.0,
      "entry": 501.884,
      "exit": 507.6970020582237,
      "qty": 20.567,
      "entry_notional": 10322.248228,
      "gross": 119.55601333148661,
      "fees": 9.34382361119917,
      "net": 110.21218972028744,
      "hold_hours": 300.73333333333335,
      "net_bps_entry": 106.77149714470849,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0c254052-2ec2-4452-b29b-8f096d91fc6a",
      "opened_at": 1715673600000.0,
      "closed_at": 1716490620000.0,
      "entry": 522.091,
      "exit": 527.9046017608516,
      "qty": 27.926000000000002,
      "entry_notional": 14579.913266000001,
      "gross": 162.35064277354286,
      "fees": 13.194979728648097,
      "net": 149.15566304489477,
      "hold_hours": 226.95,
      "net_bps_entry": 102.3021607355663,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "60092dac-bd15-4904-b923-0023485c389d",
      "opened_at": 1718856000000.0,
      "closed_at": 1718904720000.0,
      "entry": 549.4252,
      "exit": 546.6287053838354,
      "qty": 27.27,
      "entry_notional": 14982.825204,
      "gross": -76.26040818281035,
      "fees": 13.450225499917735,
      "net": -89.71063368272809,
      "hold_hours": 13.533333333333333,
      "net_bps_entry": -59.87564592209073,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "25abe842-1593-4c83-9207-513b709089ac",
      "opened_at": 1718942400000.0,
      "closed_at": 1719262920000.0,
      "entry": 547.6823,
      "exit": 544.4673287131116,
      "qty": 24.399,
      "entry_notional": 13362.900437700002,
      "gross": -78.44208442879244,
      "fees": 11.991311455937044,
      "net": -90.43339588472949,
      "hold_hours": 89.03333333333333,
      "net_bps_entry": -67.67497543392213,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "927cee7f-9101-442d-ad1a-f4153b05b851",
      "opened_at": 1720440000000.0,
      "closed_at": 1720717380000.0,
      "entry": 556.3677,
      "exit": 558.2129752324591,
      "qty": 28.851,
      "entry_notional": 16051.7645127,
      "gross": 53.23803573167788,
      "fees": 14.470545177509255,
      "net": 38.76749055416863,
      "hold_hours": 77.05,
      "net_bps_entry": 24.15154453798283,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "da30c375-f4f4-4405-b4b5-ef9a8d4d4f65",
      "opened_at": 1720771200000.0,
      "closed_at": 1721233620000.0,
      "entry": 558.9879,
      "exit": 559.6167613875,
      "qty": 25.502,
      "entry_notional": 14255.309425799998,
      "gross": 16.037223104025543,
      "fees": 12.83699523361681,
      "net": 3.2002278704087335,
      "hold_hours": 128.45,
      "net_bps_entry": 2.244937500000382,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "85509f17-c1dc-410e-9e68-bbf5ba756a2a",
      "opened_at": 1724385600000.0,
      "closed_at": 1724888460000.0,
      "entry": 558.8134,
      "exit": 555.6954287097703,
      "qty": 17.672,
      "entry_notional": 9875.3504048,
      "gross": -55.100788640937026,
      "fees": 8.863020009431578,
      "net": -63.963808650368605,
      "hold_hours": 139.68333333333334,
      "net_bps_entry": -64.77117877182205,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b8f3b54b-b01c-4c17-8258-8e94471d3292",
      "opened_at": 1727107200000.0,
      "closed_at": 1727796720000.0,
      "entry": 572.1031,
      "exit": 568.7706050899465,
      "qty": 16.647000000000002,
      "entry_notional": 9523.800305700002,
      "gross": -55.476042767662875,
      "fees": 8.546456055884553,
      "net": -64.02249882354742,
      "hold_hours": 191.53333333333333,
      "net_bps_entry": -67.22368883063403,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7d3de696-f0f2-430e-80cf-5a02923923c7",
      "opened_at": 1729051200000.0,
      "closed_at": 1729706580000.0,
      "entry": 582.024,
      "exit": 579.3929032269996,
      "qty": 20.415,
      "entry_notional": 11882.01996,
      "gross": -53.71384062080324,
      "fees": 10.669646735720638,
      "net": -64.38348735652387,
      "hold_hours": 182.05,
      "net_bps_entry": -54.18564147616856,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a216a6a4-4394-466e-8f13-b52c30a3a3b1",
      "opened_at": 1731398400000.0,
      "closed_at": 1731605580000.0,
      "entry": 599.8327,
      "exit": 595.5597329270975,
      "qty": 18.738,
      "entry_notional": 11239.665132600001,
      "gross": -80.06685701204879,
      "fees": 10.079668533684577,
      "net": -90.14652554573337,
      "hold_hours": 57.55,
      "net_bps_entry": -80.20392465632145,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "574af2ee-c9bf-4f1e-b6d7-48347ca3d1ae",
      "opened_at": 1737633600000.0,
      "closed_at": 1737955800000.0,
      "entry": 607.6754,
      "exit": 602.9368709780489,
      "qty": 17.057,
      "entry_notional": 10365.119297799998,
      "gross": -80.82508952741955,
      "fees": 9.292236077732658,
      "net": -90.1173256051522,
      "hold_hours": 89.5,
      "net_bps_entry": -86.94287351258914,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a4425598-6a16-46aa-ac41-e8fb6f4b5060",
      "opened_at": 1747324800000.0,
      "closed_at": 1747858320000.0,
      "entry": 588.0746,
      "exit": 583.6916038169531,
      "qty": 13.148,
      "entry_notional": 7732.0048408,
      "gross": -57.62763381470086,
      "fees": 6.932871921503385,
      "net": -64.56050573620425,
      "hold_hours": 148.2,
      "net_bps_entry": -83.4977564881147,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7b0a2094-0c1f-4625-bbcc-cda3e823b367",
      "opened_at": 1749715200000.0,
      "closed_at": 1749778380000.0,
      "entry": 601.2003999999998,
      "exit": 595.5104337378314,
      "qty": 14.486,
      "entry_notional": 8708.988994399999,
      "gross": -82.42485127377404,
      "fees": 7.8009989118868,
      "net": -90.22585018566083,
      "hold_hours": 17.55,
      "net_bps_entry": -103.60083155883801,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2e013b55-9ea9-4a8c-bdef-7c3dffd76f4b",
      "opened_at": 1751644800000.0,
      "closed_at": 1751916120000.0,
      "entry": 624.2154,
      "exit": 620.2051593990782,
      "qty": 18.873,
      "entry_notional": 11780.817244200001,
      "gross": -75.68527086119866,
      "fees": 10.568677147892462,
      "net": -86.25394800909112,
      "hold_hours": 75.36666666666666,
      "net_bps_entry": -73.21558956493969,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "874867de-7b4b-496c-8cdc-9158d64b0eb8",
      "opened_at": 1755172800000.0,
      "closed_at": 1755619320000.0,
      "entry": 646.2984,
      "exit": 642.1979959144973,
      "qty": 18.243000000000002,
      "entry_notional": 11790.421711200002,
      "gross": -74.80367173182822,
      "fees": 10.577717887800679,
      "net": -85.38138961962889,
      "hold_hours": 124.03333333333333,
      "net_bps_entry": -72.41589123018652,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "87006cda-0de0-4727-acfb-35084b679cd3",
      "opened_at": 1756108800000.0,
      "closed_at": 1756803060000.0,
      "entry": 645.7672,
      "exit": 642.559770063633,
      "qty": 14.513,
      "entry_notional": 9372.0193736,
      "gross": -46.54943066649503,
      "fees": 8.413870192440077,
      "net": -54.963300858935106,
      "hold_hours": 192.85,
      "net_bps_entry": -58.64616649615662,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "af53f253-6c88-4669-86bb-bdf3618c3710",
      "opened_at": 1761652800000.0,
      "closed_at": 1761852120000.0,
      "entry": 687.9354,
      "exit": 683.2740053587016,
      "qty": 16.051000000000002,
      "entry_notional": 11042.0511054,
      "gross": -74.82004538747788,
      "fees": 9.904176974435634,
      "net": -84.7242223619135,
      "hold_hours": 55.36666666666667,
      "net_bps_entry": -76.72869972543417,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9051b9d7-e8b0-427a-8a4a-b57f95ac32c4",
      "opened_at": 1761883200000.0,
      "closed_at": 1762234860000.0,
      "entry": 686.9745,
      "exit": 680.5428370222944,
      "qty": 12.273,
      "entry_notional": 8431.2380385,
      "gross": -78.935799725381,
      "fees": 7.552593124773577,
      "net": -86.48839285015458,
      "hold_hours": 97.68333333333334,
      "net_bps_entry": -102.58089316802365,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c99c44fb-4967-4e59-bab2-b1f485acc267",
      "opened_at": 1766491200000.0,
      "closed_at": 1767139200000.0,
      "entry": 687.7354,
      "exit": 689.5951,
      "qty": 15.031,
      "entry_notional": 10337.3507974,
      "gross": 27.95315069999924,
      "fees": 9.316194635475,
      "net": 18.63695606452424,
      "hold_hours": 180.0,
      "net_bps_entry": 18.028754590791017,
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
