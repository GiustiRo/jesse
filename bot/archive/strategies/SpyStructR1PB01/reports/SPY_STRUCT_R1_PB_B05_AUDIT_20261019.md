# B05 snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "B05",
    "url": "http://localhost:9200/#/backtest/89577f9b-3980-4808-bd3a-f850255b5fc0",
    "n": 48,
    "net": -43.45555526713462,
    "gross_before_fees": 392.32951733866776,
    "fees": 435.7850726058024,
    "pf": 0.983435366771851,
    "sharpe": 0.001525022300664274,
    "dd_motor_pct": -7.769281482707779,
    "cagr_motor_pct": -0.08349555326917502,
    "time_exposure_pct": 19.716784901033453,
    "entry_price_notional_time": 0.1835958960270239,
    "mean_hold_hours": 187.6052083333333,
    "turnover_two_sides": 968411.2724573388,
    "total_entry_notional": 484009.47147,
    "net_bps_per_entry_notional": -0.8978244813093104,
    "net_plus5bpsRT": -285.5583733814693,
    "net_plus10bpsRT": -527.661191495804,
    "net_exbest": -395.4541880852332,
    "net_ex3best": -996.6054024530423,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 168.791316391482,
        "fees": 3.5746040598531006
      },
      "2021": {
        "n": 6,
        "net": 253.87204811156442,
        "fees": 65.80509293423061
      },
      "2022": {
        "n": 8,
        "net": -224.3251944170916,
        "fees": 46.978012917765305
      },
      "2023": {
        "n": 12,
        "net": 64.57115792783776,
        "fees": 113.14012160399932
      },
      "2024": {
        "n": 12,
        "net": -78.84876907354207,
        "fees": 131.06237621937564
      },
      "2025": {
        "n": 9,
        "net": -227.5161142073851,
        "fees": 75.22486487057843
      }
    },
    "executed_order_types": {
      "MARKET": 49,
      "STOP": 47
    },
    "entry_order_types": {
      "MARKET": 48
    },
    "exit_order_types": {
      "STOP": 47,
      "MARKET": 1
    },
    "terminal_orders": [
      {
        "trade_id": "8268e7d6-939a-483a-a2d4-76468d7f7056",
        "side": "sell",
        "type": "MARKET",
        "gross": 5.296602399999756,
        "net": -4.377964248200245,
        "fee": 9.6745666482,
        "exit_fee": 4.83847505964
      }
    ],
    "metric_preterminal_open_count": 1,
    "fingerprint": "68624e7a741e6ca58413b7e231322b6281c9e0376fc7107df6ea895a469d929b",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "042ceb25-0532-49e3-b2df-50edb2dcea94",
      "opened_at": 1604649600000.0,
      "closed_at": 1607609400000.0,
      "entry": 349.6445,
      "exit": 365.15479609028483,
      "qty": 11.113,
      "entry_notional": 3885.5993285,
      "gross": 172.3659204513351,
      "fees": 3.5746040598531006,
      "net": 168.791316391482,
      "hold_hours": 822.1666666666666,
      "net_bps_entry": 434.40226879142057,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c176f98c-a9aa-4a14-a03a-8b10d14f90fb",
      "opened_at": 1612886400000.0,
      "closed_at": 1613572440000.0,
      "entry": 390.9842,
      "exit": 390.68541426211965,
      "qty": 24.756,
      "entry_notional": 9679.2048552,
      "gross": -7.396739726966189,
      "fees": 8.707955836802865,
      "net": -16.104695563769056,
      "hold_hours": 190.56666666666666,
      "net_bps_entry": -16.63844892704907,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f9bc749e-a932-47f4-9a19-8889116b4d01",
      "opened_at": 1617710400000.0,
      "closed_at": 1618933920000.0,
      "entry": 406.7642,
      "exit": 413.4494018288913,
      "qty": 27.496000000000002,
      "entry_notional": 11184.388443200001,
      "gross": 183.81630948719612,
      "fees": 10.148666938149239,
      "net": 173.6676425490469,
      "hold_hours": 339.8666666666667,
      "net_bps_entry": 155.27683380367134,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "33059e9a-1539-4226-b1be-0f4fc0568f6b",
      "opened_at": 1625558400000.0,
      "closed_at": 1625585580000.0,
      "entry": 435.0639,
      "exit": 433.2531536514576,
      "qty": 39.166000000000004,
      "entry_notional": 17039.7127074,
      "gross": -70.91969148701173,
      "fees": 15.303827575490846,
      "net": -86.22351906250258,
      "hold_hours": 7.55,
      "net_bps_entry": -50.60150986293181,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2951991f-0777-4444-9ea9-fc5e6e4d9808",
      "opened_at": 1625673600000.0,
      "closed_at": 1625734020000.0,
      "entry": 434.1145,
      "exit": 431.6657247182009,
      "qty": 31.291,
      "entry_notional": 13583.876819500001,
      "gross": -76.62462734277688,
      "fees": 12.191008055245751,
      "net": -88.81563539802262,
      "hold_hours": 16.783333333333335,
      "net_bps_entry": -65.3831277905329,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a8aa4de1-4af4-4339-aa00-c6200a9416a2",
      "opened_at": 1630425600000.0,
      "closed_at": 1631089560000.0,
      "entry": 452.6651,
      "exit": 450.23968153702623,
      "qty": 28.481,
      "entry_notional": 12892.354713100001,
      "gross": -69.07834324395662,
      "fees": 11.57203398733022,
      "net": -80.65037723128684,
      "hold_hours": 184.43333333333334,
      "net_bps_entry": -62.55674702258812,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2c47c7fa-8a5a-41a0-97d3-19bc286ef653",
      "opened_at": 1634572800000.0,
      "closed_at": 1636567560000.0,
      "entry": 447.2051,
      "exit": 465.96840726586606,
      "qty": 19.18,
      "entry_notional": 8577.393818,
      "gross": 359.8802333593103,
      "fees": 7.88160054121169,
      "net": 351.9986328180986,
      "hold_hours": 554.1,
      "net_bps_entry": 410.37946990310223,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "44a426de-5a53-4f10-b10d-57ffe37d6cab",
      "opened_at": 1640793600000.0,
      "closed_at": 1641410340000.0,
      "entry": 479.0836,
      "exit": 475.2057154297732,
      "qty": 21.775000000000002,
      "entry_notional": 10432.045390000001,
      "gross": -84.44093651668845,
      "fees": 9.350842429567491,
      "net": -93.79177894625595,
      "hold_hours": 171.31666666666666,
      "net_bps_entry": -89.90737237029596,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f391092d-76e8-4cc8-8659-c60f7212110f",
      "opened_at": 1648051200000.0,
      "closed_at": 1648826460000.0,
      "entry": 449.4148,
      "exit": 453.0820196035878,
      "qty": 14.644,
      "entry_notional": 6581.2303312,
      "gross": 53.70276387493959,
      "fees": 5.947273541823723,
      "net": 47.75549033311587,
      "hold_hours": 215.35,
      "net_bps_entry": 72.56316513755611,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1f4d5b44-d267-4ba2-935a-b9b8ad9414bc",
      "opened_at": 1653969600000.0,
      "closed_at": 1654097700000.0,
      "entry": 416.9599,
      "exit": 410.1722402461821,
      "qty": 13.695,
      "entry_notional": 5710.2658305,
      "gross": -92.9570003285362,
      "fees": 5.097408597302159,
      "net": -98.05440892583836,
      "hold_hours": 35.583333333333336,
      "net_bps_entry": -171.71601434403368,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d5090157-fa61-45b9-813a-0dd6f011f929",
      "opened_at": 1659412800000.0,
      "closed_at": 1661122860000.0,
      "entry": 410.0151,
      "exit": 421.4433,
      "qty": 16.295,
      "entry_notional": 6681.196054500001,
      "gross": 186.22251899999992,
      "fees": 6.096876582600001,
      "net": 180.12564241739992,
      "hold_hours": 475.01666666666665,
      "net_bps_entry": 269.6008932353953,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c5b82a62-769a-4d0d-955a-75bab9d823cf",
      "opened_at": 1666886400000.0,
      "closed_at": 1667417160000.0,
      "entry": 383.2009,
      "exit": 378.7789237622205,
      "qty": 13.283,
      "entry_notional": 5090.0575547,
      "gross": -58.73711036642544,
      "fees": 4.554620099565109,
      "net": -63.29173046599055,
      "hold_hours": 147.43333333333334,
      "net_bps_entry": -124.34384048869731,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "f815ae2f-67ea-490b-bea5-005036d4c094",
      "opened_at": 1668182400000.0,
      "closed_at": 1669661820000.0,
      "entry": 397.0819,
      "exit": 397.1781155432618,
      "qty": 12.138,
      "entry_notional": 4819.7801022,
      "gross": 1.167864264111813,
      "fees": 4.338327630898851,
      "net": -3.170463366787038,
      "hold_hours": 410.95,
      "net_bps_entry": -6.578024929684805,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "543195e3-af6b-4820-b4e1-3ca67308bde8",
      "opened_at": 1669910400000.0,
      "closed_at": 1669987860000.0,
      "entry": 407.8565,
      "exit": 402.5537245713193,
      "qty": 17.105,
      "entry_notional": 6976.3854325,
      "gross": -90.70397370758292,
      "fees": 6.237930101081588,
      "net": -96.9419038086645,
      "hold_hours": 21.516666666666666,
      "net_bps_entry": -138.95720749179594,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "46a5fa76-796c-41c4-82c4-959ecd1e2231",
      "opened_at": 1671033600000.0,
      "closed_at": 1671046500000.0,
      "entry": 404.2822,
      "exit": 398.1054429049801,
      "qty": 14.83,
      "entry_notional": 5995.505026,
      "gross": -91.60130771914464,
      "fees": 5.354733934926385,
      "net": -96.95604165407103,
      "hold_hours": 3.5833333333333335,
      "net_bps_entry": -161.7145532088009,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "85e35997-b2e4-4bca-b85b-acbe946bcf39",
      "opened_at": 1673539200000.0,
      "closed_at": 1674088080000.0,
      "entry": 396.7705,
      "exit": 392.19724641391247,
      "qty": 17.228,
      "entry_notional": 6835.5621740000015,
      "gross": -78.78801278111678,
      "fees": 6.116551350848499,
      "net": -84.90456413196527,
      "hold_hours": 152.46666666666667,
      "net_bps_entry": -124.2100678345249,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "398ba88d-1719-442a-acaa-e9668c22a150",
      "opened_at": 1675425600000.0,
      "closed_at": 1675679160000.0,
      "entry": 414.7925,
      "exit": 409.7800269146118,
      "qty": 17.441,
      "entry_notional": 7234.3959925,
      "gross": -87.42254308225529,
      "fees": 6.4716162488629845,
      "net": -93.89415933111827,
      "hold_hours": 70.43333333333334,
      "net_bps_entry": -129.7885261305293,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5807108e-151e-4704-bbf5-349bd23b8d8b",
      "opened_at": 1675699200000.0,
      "closed_at": 1676023320000.0,
      "entry": 411.3763,
      "exit": 406.6714499723386,
      "qty": 16.334,
      "entry_notional": 6719.4204842,
      "gross": -76.84902035182131,
      "fees": 6.01289637662168,
      "net": -82.86191672844299,
      "hold_hours": 90.03333333333333,
      "net_bps_entry": -123.3170582541812,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ca8e00ac-4bc5-41e3-8e90-3a1d00a7682d",
      "opened_at": 1686067200000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.349,
      "exit": 437.4709,
      "qty": 23.882,
      "entry_notional": 10229.830818,
      "gross": 217.849215799999,
      "fees": 9.304879883309999,
      "net": 208.544335916689,
      "hold_hours": 336.01666666666665,
      "net_bps_entry": 203.85902721845872,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fa29a9a1-959a-4d18-b054-a722905ea33d",
      "opened_at": 1688400000000.0,
      "closed_at": 1688652060000.0,
      "entry": 444.77,
      "exit": 440.9846,
      "qty": 27.632,
      "entry_notional": 12289.88464,
      "gross": -104.59817279999879,
      "fees": 11.01382699824,
      "net": -115.6119997982388,
      "hold_hours": 70.01666666666667,
      "net_bps_entry": -94.0708584212055,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1f1b380c-7840-4e61-b681-69a880c11561",
      "opened_at": 1689609600000.0,
      "closed_at": 1690486680000.0,
      "entry": 451.3014,
      "exit": 454.30610414058475,
      "qty": 29.829,
      "entry_notional": 13461.8694606,
      "gross": 89.6273198095023,
      "fees": 12.156014808454277,
      "net": 77.47130500104802,
      "hold_hours": 243.63333333333333,
      "net_bps_entry": 57.54869725025183,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "a57e0fc2-04ce-4ae4-9bfe-7d10c3dcba09",
      "opened_at": 1690891200000.0,
      "closed_at": 1690930860000.0,
      "entry": 458.2814,
      "exit": 455.3348227263674,
      "qty": 26.486,
      "entry_notional": 12138.0411604,
      "gross": -78.0430456694321,
      "fees": 10.889117673808757,
      "net": -88.93216334324086,
      "hold_hours": 11.016666666666667,
      "net_bps_entry": -73.26731073657866,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ece426df-7b32-4dc0-a513-2bb4a17d0bc9",
      "opened_at": 1693555200000.0,
      "closed_at": 1694012460000.0,
      "entry": 451.0813,
      "exit": 447.5910330259025,
      "qty": 23.052,
      "entry_notional": 10398.3261276,
      "gross": -80.45763428689497,
      "fees": 9.322287579410897,
      "net": -89.77992186630587,
      "hold_hours": 127.01666666666667,
      "net_bps_entry": -86.34074442809158,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "83c945ea-779f-430e-9734-c6df8f905baa",
      "opened_at": 1699545600000.0,
      "closed_at": 1699559100000.0,
      "entry": 437.9077,
      "exit": 434.6802389006617,
      "qty": 24.465,
      "entry_notional": 10713.4118805,
      "gross": -78.95983579531094,
      "fees": 9.60653876634211,
      "net": -88.56637456165305,
      "hold_hours": 3.75,
      "net_bps_entry": -82.66869186916728,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c326b2ea-7f64-4ff1-b9e0-4e7e9e37f115",
      "opened_at": 1699891200000.0,
      "closed_at": 1701705240000.0,
      "entry": 440.6177,
      "exit": 454.7454627095242,
      "qty": 22.127,
      "entry_notional": 9749.5478479,
      "gross": 312.60500547364245,
      "fees": 8.915265315573139,
      "net": 303.6897401580693,
      "hold_hours": 503.9,
      "net_bps_entry": 311.4911018396432,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7943133d-aacd-409c-9b07-e10c2a988100",
      "opened_at": 1702396800000.0,
      "closed_at": 1703102700000.0,
      "entry": 462.8006,
      "exit": 471.5948268393657,
      "qty": 24.913,
      "entry_notional": 11529.7513478,
      "gross": 219.09057324911737,
      "fees": 10.475366970982101,
      "net": 208.61520627813528,
      "hold_hours": 196.08333333333334,
      "net_bps_entry": 180.93643131162696,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "e58741c9-3185-4bf8-9eff-6f0bc7e6092c",
      "opened_at": 1703779200000.0,
      "closed_at": 1703866620000.0,
      "entry": 478.8962,
      "exit": 476.3435344021937,
      "qty": 29.907,
      "entry_notional": 14322.3486534,
      "gross": -76.3425700335938,
      "fees": 12.855759631544883,
      "net": -89.19832966513869,
      "hold_hours": 24.283333333333335,
      "net_bps_entry": -62.27912182822318,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "69852e66-c6fa-42b9-805b-55336ec28168",
      "opened_at": 1706025600000.0,
      "closed_at": 1706731380000.0,
      "entry": 484.78470000000004,
      "exit": 486.4875866158665,
      "qty": 25.027,
      "entry_notional": 12132.706686900001,
      "gross": 42.61814333529037,
      "fees": 10.93861418271088,
      "net": 31.67952915257949,
      "hold_hours": 196.05,
      "net_bps_entry": 26.110850587680243,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fa1f2d9d-e058-45f5-a18e-186e4c071572",
      "opened_at": 1706889600000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.67629999999997,
      "exit": 497.8346590482505,
      "qty": 20.629,
      "entry_notional": 10184.0483927,
      "gross": 85.78278880636026,
      "fees": 9.204245808392862,
      "net": 76.57854299796739,
      "hold_hours": 261.51666666666665,
      "net_bps_entry": 75.19459849862795,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7622db5a-a663-41b8-9181-a674a0cf0eb5",
      "opened_at": 1708920000000.0,
      "closed_at": 1709657040000.0,
      "entry": 508.0286,
      "exit": 507.69700205822375,
      "qty": 21.534,
      "entry_notional": 10939.887872399999,
      "gross": -7.140630078209142,
      "fees": 9.842685801624803,
      "net": -16.983315879833945,
      "hold_hours": 204.73333333333332,
      "net_bps_entry": -15.524213847457045,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "76970a2c-76e2-4172-b85d-3b618b9be1a6",
      "opened_at": 1709913600000.0,
      "closed_at": 1709920380000.0,
      "entry": 518.2207,
      "exit": 513.9336185901562,
      "qty": 19.648,
      "entry_notional": 10182.0003136,
      "gross": -84.2325755406091,
      "fees": 9.125895623246725,
      "net": -93.35847116385582,
      "hold_hours": 1.8833333333333333,
      "net_bps_entry": -91.68971546696754,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "3ef798fa-235b-4a05-9fd9-38f7f818dee6",
      "opened_at": 1710345600000.0,
      "closed_at": 1710444360000.0,
      "entry": 517.0063,
      "exit": 512.7057744393283,
      "qty": 19.43,
      "entry_notional": 10045.432409000001,
      "gross": -83.5592116438529,
      "fees": 9.003287522860267,
      "net": -92.56249916671317,
      "hold_hours": 27.433333333333334,
      "net_bps_entry": -92.14386737974931,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "fea1f300-c3c6-46c4-964b-770085b33aea",
      "opened_at": 1715184000000.0,
      "closed_at": 1716490620000.0,
      "entry": 518.878,
      "exit": 527.9046017608516,
      "qty": 21.509,
      "entry_notional": 11160.546902000002,
      "gross": 194.1531772741564,
      "fees": 10.131861141573372,
      "net": 184.02131613258302,
      "hold_hours": 362.95,
      "net_bps_entry": 164.88557213948528,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "eb86e58c-3b33-4659-8823-c2791367a374",
      "opened_at": 1718899200000.0,
      "closed_at": 1718904720000.0,
      "entry": 549.6507,
      "exit": 546.719703673569,
      "qty": 26.049,
      "entry_notional": 14317.8510843,
      "gross": -76.3495233072008,
      "fees": 12.85170869038176,
      "net": -89.20123199758255,
      "hold_hours": 1.5333333333333334,
      "net_bps_entry": -62.30071221748819,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1d778be8-80fb-41fc-91fd-7e4360926766",
      "opened_at": 1718985600000.0,
      "closed_at": 1720717380000.0,
      "entry": 546.946,
      "exit": 558.2129752324591,
      "qty": 23.846,
      "entry_notional": 13042.474316,
      "gross": 268.6722913932208,
      "fees": 11.859129415526949,
      "net": 256.8131619776939,
      "hold_hours": 481.05,
      "net_bps_entry": 196.90524647048412,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "66ac8faa-4deb-45c5-961b-24b6b58e1919",
      "opened_at": 1721131200000.0,
      "closed_at": 1721228940000.0,
      "entry": 563.8013,
      "exit": 560.0451358060824,
      "qty": 21.799,
      "entry_notional": 12290.304538699998,
      "gross": -81.88062326320869,
      "fees": 11.024427804361554,
      "net": -92.90505106757024,
      "hold_hours": 27.15,
      "net_bps_entry": -75.59214726944207,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7105073a-1c80-454a-9b0d-6c624deedbb9",
      "opened_at": 1729051200000.0,
      "closed_at": 1729706580000.0,
      "entry": 582.024,
      "exit": 579.3929032550924,
      "qty": 20.862000000000002,
      "entry_notional": 12142.184688000001,
      "gross": -54.88994029226342,
      "fees": 10.903265746068483,
      "net": -65.7932060383319,
      "hold_hours": 182.05,
      "net_bps_entry": -54.18564099371233,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "59cab413-4f05-463a-bd40-df9e1ea4bcf6",
      "opened_at": 1731412800000.0,
      "closed_at": 1731614700000.0,
      "entry": 599.33,
      "exit": 595.0883877074317,
      "qty": 19.264,
      "entry_notional": 11545.493120000001,
      "gross": -81.71041920403695,
      "fees": 10.354174119358182,
      "net": -92.06459332339513,
      "hold_hours": 56.083333333333336,
      "net_bps_entry": -79.74071992119045,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1ba79ca3-41ce-4c93-aabc-f1f6967feb20",
      "opened_at": 1733414400000.0,
      "closed_at": 1733760600000.0,
      "entry": 607.9244,
      "exit": 605.5345780607443,
      "qty": 28.977,
      "entry_notional": 17615.8253388,
      "gross": -69.2498703338133,
      "fees": 15.823080363269785,
      "net": -85.07295069708309,
      "hold_hours": 96.16666666666667,
      "net_bps_entry": -48.293479902814646,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6b2b40a4-2480-4f75-a4d5-0efb3f1cde93",
      "opened_at": 1737388800000.0,
      "closed_at": 1737421260000.0,
      "entry": 601.7926,
      "exit": 595.9026286991198,
      "qty": 14.485,
      "entry_notional": 8716.965811,
      "gross": -85.31623429325009,
      "fees": 7.806876924468036,
      "net": -93.12311121771813,
      "hold_hours": 9.016666666666667,
      "net_bps_entry": -106.8297309371174,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1ae56c9c-1920-4647-ad39-adcc08d9a583",
      "opened_at": 1737432000000.0,
      "closed_at": 1737957240000.0,
      "entry": 601.0122,
      "exit": 602.5149517711916,
      "qty": 13.239,
      "entry_notional": 7956.8005158000005,
      "gross": 19.894930698805183,
      "fees": 7.170073183034463,
      "net": 12.72485751577072,
      "hold_hours": 145.9,
      "net_bps_entry": 15.992429985523303,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "5f1b7cec-38f4-4518-90f2-a3728cad48a2",
      "opened_at": 1738080000000.0,
      "closed_at": 1738537260000.0,
      "entry": 605.1029,
      "exit": 594.9989,
      "qty": 12.76,
      "entry_notional": 7721.113004,
      "gross": -128.92703999999958,
      "fees": 6.8909845355999995,
      "net": -135.8180245355996,
      "hold_hours": 127.01666666666667,
      "net_bps_entry": -175.90472314708734,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d0e58a4b-1182-4315-857f-f67a93813dca",
      "opened_at": 1747224000000.0,
      "closed_at": 1747858320000.0,
      "entry": 588.5625,
      "exit": 583.6916038169531,
      "qty": 11.827,
      "entry_notional": 6960.9286875,
      "gross": -57.60808915689449,
      "fees": 6.2389121786293975,
      "net": -63.84700133552389,
      "hold_hours": 176.2,
      "net_bps_entry": -91.72195866648705,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d2afb954-65bd-4bef-ae7e-45e3773efc9e",
      "opened_at": 1749542400000.0,
      "closed_at": 1749779640000.0,
      "entry": 600.2342,
      "exit": 594.7242201564344,
      "qty": 14.897,
      "entry_notional": 8941.6888774,
      "gross": -82.08216972959599,
      "fees": 8.01058301328168,
      "net": -90.09275274287766,
      "hold_hours": 65.9,
      "net_bps_entry": -100.75585717434868,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "775a76ba-7fef-4ffd-8b8a-36e37b222d1d",
      "opened_at": 1751385600000.0,
      "closed_at": 1753821600000.0,
      "entry": 618.7369,
      "exit": 636.4563779329557,
      "qty": 17.34,
      "entry_notional": 10728.897846,
      "gross": 307.2557473574507,
      "fees": 9.794273147710852,
      "net": 297.46147420973983,
      "hold_hours": 676.6666666666666,
      "net_bps_entry": 277.25259246516254,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "dc4533d1-d669-4338-99ae-671cd43de555",
      "opened_at": 1755187200000.0,
      "closed_at": 1755619320000.0,
      "entry": 646.4731,
      "exit": 642.0647247705748,
      "qty": 17.944,
      "entry_notional": 11600.3133064,
      "gross": -79.10388511680503,
      "fees": 10.404685227457437,
      "net": -89.50857034426247,
      "hold_hours": 120.03333333333333,
      "net_bps_entry": -77.16047660098953,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c723a3d9-c97a-491b-879c-0d4be326ec50",
      "opened_at": 1756137600000.0,
      "closed_at": 1756803060000.0,
      "entry": 645.8059,
      "exit": 642.559770063633,
      "qty": 15.927,
      "entry_notional": 10285.750569299998,
      "gross": -51.701111496517115,
      "fees": 9.233910012196565,
      "net": -60.93502150871368,
      "hold_hours": 184.85,
      "net_bps_entry": -59.24217304139881,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8268e7d6-939a-483a-a2d4-76468d7f7056",
      "opened_at": 1766505600000.0,
      "closed_at": 1767139200000.0,
      "entry": 689.2554,
      "exit": 689.5951,
      "qty": 15.592,
      "entry_notional": 10746.8701968,
      "gross": 5.296602399999756,
      "fees": 9.6745666482,
      "net": -4.377964248200245,
      "hold_hours": 176.0,
      "net_bps_entry": -4.073710920509519,
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
