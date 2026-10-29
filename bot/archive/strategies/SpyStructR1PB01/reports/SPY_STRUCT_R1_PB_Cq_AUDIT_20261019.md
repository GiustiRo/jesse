# Cq snapshot audit

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Complete fills/trades reconciliation; no MTM inference. Snapshot metadata and pertrade results follow.

```json
{
  "row": {
    "name": "Cq",
    "url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "n": 31,
    "net": 751.3477149671141,
    "gross_before_fees": 1037.8232411744625,
    "fees": 286.4755262073485,
    "pf": 1.4930482284215572,
    "sharpe": 0.4581998683996086,
    "dd_motor_pct": -5.2131810594609025,
    "cagr_motor_pct": 1.3992310944554776,
    "time_exposure_pct": 15.264093244584576,
    "entry_price_notional_time": 0.14148527769141334,
    "mean_hold_hours": 224.88440860215056,
    "turnover_two_sides": 636612.2804607744,
    "total_entry_notional": 317787.2286098,
    "net_bps_per_entry_notional": 23.64310605728175,
    "net_plus5bpsRT": 592.1946448519205,
    "net_plus10bpsRT": 433.04157473672694,
    "net_exbest": 349.5779967160442,
    "net_ex3best": -298.22377215887536,
    "close_year_cohorts": {
      "2020": {
        "n": 1,
        "net": 137.97951328203996,
        "fees": 3.3286263618797642
      },
      "2021": {
        "n": 3,
        "net": 335.82780322377914,
        "fees": 31.69319416469481
      },
      "2022": {
        "n": 5,
        "net": -215.40842745654246,
        "fees": 29.773738643214
      },
      "2023": {
        "n": 9,
        "net": 395.76115138960495,
        "fees": 89.11426287503907
      },
      "2024": {
        "n": 8,
        "net": -22.513406024081632,
        "fees": 87.70643620271038
      },
      "2025": {
        "n": 5,
        "net": 119.7010805523142,
        "fees": 44.85926795981045
      }
    },
    "executed_order_types": {
      "LIMIT": 24,
      "STOP": 31,
      "MARKET": 7
    },
    "entry_order_types": {
      "LIMIT": 24,
      "MARKET": 7
    },
    "exit_order_types": {
      "STOP": 31
    },
    "terminal_orders": [],
    "metric_preterminal_open_count": 0,
    "fingerprint": "ae1d1754362d5e9911268d565e97020e521167a7fa44b5cef2b2a97fd9d3d4d3",
    "audit": "passed"
  },
  "trades": [
    {
      "id": "bac9aad0-d8dc-4280-98e9-0b02d2e452d5",
      "opened_at": 1604592720000.0,
      "closed_at": 1607609400000.0,
      "entry": 351.4648,
      "exit": 365.15479609028483,
      "qty": 10.322000000000001,
      "entry_notional": 3627.8196656000005,
      "gross": 141.30813964391973,
      "fees": 3.3286263618797642,
      "net": 137.97951328203996,
      "hold_hours": 837.9666666666667,
      "net_bps_entry": 380.33729898539406,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d4d87515-b7ec-4556-9514-4ff8bfce4663",
      "opened_at": 1617940800000.0,
      "closed_at": 1618933920000.0,
      "entry": 410.1748,
      "exit": 413.44940189745466,
      "qty": 30.017,
      "entry_notional": 12312.2169716,
      "gross": 98.29372515589603,
      "fees": 11.125227450760153,
      "net": 87.16849770513588,
      "hold_hours": 275.8666666666667,
      "net_bps_entry": 70.79837685300971,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0b4b0a70-1e3c-4bb0-b040-9e441b1627ad",
      "opened_at": 1630402800000.0,
      "closed_at": 1631088420000.0,
      "entry": 453.7399,
      "exit": 451.13598025409726,
      "qty": 29.511,
      "entry_notional": 13390.318188899999,
      "gross": -76.84427562133533,
      "fees": 12.016706445980397,
      "net": -88.86098206731572,
      "hold_hours": 190.45,
      "net_bps_entry": -66.36211388985339,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "d61c0fc0-97e5-4562-9983-d8b80386e8e9",
      "opened_at": 1634630520000.0,
      "closed_at": 1636567560000.0,
      "entry": 449.2998999999999,
      "exit": 465.9684072658661,
      "qty": 20.762,
      "entry_notional": 9328.364523799999,
      "gross": 346.0715478539132,
      "fees": 8.55126026795426,
      "net": 337.52028758595895,
      "hold_hours": 538.0666666666667,
      "net_bps_entry": 361.8215033565893,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c50a9cd9-4f20-4f3b-898e-cf45911c2b04",
      "opened_at": 1640704800000.0,
      "closed_at": 1641411240000.0,
      "entry": 479.0054,
      "exit": 474.6338499972957,
      "qty": 19.837,
      "entry_notional": 9502.0301198,
      "gross": -86.7184374036442,
      "fees": 8.512803810988359,
      "net": -95.23124121463256,
      "hold_hours": 196.23333333333332,
      "net_bps_entry": -100.22199468321303,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "8145f858-7129-4e21-bdba-3359fdf95fcc",
      "opened_at": 1647878460000.0,
      "closed_at": 1648826460000.0,
      "entry": 446.8433,
      "exit": 453.0820196035878,
      "qty": 12.335,
      "entry_notional": 5511.8121055,
      "gross": 76.95460631025617,
      "fees": 4.995260467789615,
      "net": 71.95934584246655,
      "hold_hours": 263.3333333333333,
      "net_bps_entry": 130.5547875455722,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "17447076-567d-4308-a10f-8a11e3555026",
      "opened_at": 1659614460000.0,
      "closed_at": 1659707160000.0,
      "entry": 416.3448,
      "exit": 411.35856323090786,
      "qty": 18.096,
      "entry_notional": 7534.1755008,
      "gross": -90.23094057349135,
      "fees": 6.740154027461928,
      "net": -96.97109460095328,
      "hold_hours": 25.75,
      "net_bps_entry": -128.7083033712934,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "35205d4d-35cc-40fd-a5bf-5cd2debd3823",
      "opened_at": 1667310360000.0,
      "closed_at": 1667395980000.0,
      "entry": 390.1251,
      "exit": 384.1281768330955,
      "qty": 15.371,
      "entry_notional": 5996.612912099999,
      "gross": -92.17870599848811,
      "fees": 5.355471203190679,
      "net": -97.53417720167879,
      "hold_hours": 23.783333333333335,
      "net_bps_entry": -162.64877962169908,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "cdd7bf14-18c1-43dd-b9f9-d0b7d64cc828",
      "opened_at": 1668164760000.0,
      "closed_at": 1669661820000.0,
      "entry": 396.618,
      "exit": 397.17811554326187,
      "qty": 11.674,
      "entry_notional": 4630.1185319999995,
      "gross": 6.538788852039033,
      "fees": 4.170049133783418,
      "net": 2.3687397182556156,
      "hold_hours": 415.85,
      "net_bps_entry": 5.11593753353098,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "61814b23-d8db-4177-bb4c-5e03788e3702",
      "opened_at": 1682930040000.0,
      "closed_at": 1683040080000.0,
      "entry": 417.2263,
      "exit": 413.9300457491186,
      "qty": 25.096,
      "entry_notional": 10470.7112248,
      "gross": -82.72279668011834,
      "fees": 9.386414843813945,
      "net": -92.10921152393229,
      "hold_hours": 30.566666666666666,
      "net_bps_entry": -87.9684383862775,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "66f4c051-01a5-4904-ad76-c8fbfed4af16",
      "opened_at": 1685448000000.0,
      "closed_at": 1685473260000.0,
      "entry": 422.5967,
      "exit": 419.4400999999999,
      "qty": 26.01,
      "entry_notional": 10991.740167,
      "gross": -82.10316600000078,
      "fees": 9.855619725599999,
      "net": -91.95878572560078,
      "hold_hours": 7.016666666666667,
      "net_bps_entry": -83.66171718804311,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "b27cda3c-1000-4203-af2d-6797f6d4a109",
      "opened_at": 1685991660000.0,
      "closed_at": 1687276860000.0,
      "entry": 428.7527,
      "exit": 437.4709,
      "qty": 24.174,
      "entry_notional": 10364.6677698,
      "gross": 210.75376679999863,
      "fees": 9.423040187879998,
      "net": 201.33072661211864,
      "hold_hours": 357.0,
      "net_bps_entry": 194.24715879340104,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "2c1fcea7-57e2-49af-beee-b6a46d624527",
      "opened_at": 1689314520000.0,
      "closed_at": 1690486680000.0,
      "entry": 450.6334,
      "exit": 454.31735490844824,
      "qty": 27.934,
      "entry_notional": 12587.9933956,
      "gross": 102.9075964125932,
      "fees": 11.375502474425666,
      "net": 91.53209393816752,
      "hold_hours": 325.6,
      "net_bps_entry": 72.71380835817851,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0a2743d5-0c9e-4709-8aea-015f4d35e140",
      "opened_at": 1693497960000.0,
      "closed_at": 1693988160000.0,
      "entry": 452.2396,
      "exit": 448.45153585425305,
      "qty": 22.316,
      "entry_notional": 10092.178913599999,
      "gross": -84.53443947648884,
      "fees": 9.044920524475579,
      "net": -93.57936000096441,
      "hold_hours": 136.16666666666666,
      "net_bps_entry": -92.7246343947182,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6b18f10a-eaf3-466a-8298-2d68c38b8dad",
      "opened_at": 1697083200000.0,
      "closed_at": 1697137200000.0,
      "entry": 438.6092,
      "exit": 433.81798494111064,
      "qty": 18.272000000000002,
      "entry_notional": 8014.2673024000005,
      "gross": -87.54508155602616,
      "fees": 7.173445285459788,
      "net": -94.71852684148595,
      "hold_hours": 15.0,
      "net_bps_entry": -118.18738166260187,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ad16037e-02ee-4554-b1ab-e7168723c40d",
      "opened_at": 1699876920000.0,
      "closed_at": 1701705240000.0,
      "entry": 440.80959999999993,
      "exit": 454.74546270952425,
      "qty": 22.928,
      "entry_notional": 10106.8825088,
      "gross": 319.5214602039723,
      "fees": 9.239978915011788,
      "net": 310.28148128896055,
      "hold_hours": 507.8666666666667,
      "net_bps_entry": 307.0001862778165,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bfb7f7ac-e51f-4c8e-9834-1c7c801e9830",
      "opened_at": 1702310400000.0,
      "closed_at": 1703102700000.0,
      "entry": 460.98470000000003,
      "exit": 471.5948268393657,
      "qty": 25.316,
      "entry_notional": 11670.2886652,
      "gross": 268.6059710653808,
      "fees": 10.624132485659421,
      "net": 257.9818385797214,
      "hold_hours": 220.08333333333334,
      "net_bps_entry": 221.05866099868254,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "9e2530f1-1ede-485d-a956-a3254f1b94f6",
      "opened_at": 1703750400000.0,
      "closed_at": 1703866500000.0,
      "entry": 479.2623,
      "exit": 476.6132073404189,
      "qty": 30.202,
      "entry_notional": 14474.6799846,
      "gross": -80.00789650466686,
      "fees": 12.991208432712899,
      "net": -92.99910493737976,
      "hold_hours": 32.25,
      "net_bps_entry": -64.24950674994128,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "4de18e7d-a59b-4a95-af27-4db4af304d36",
      "opened_at": 1706285040000.0,
      "closed_at": 1706731380000.0,
      "entry": 490.3361,
      "exit": 487.0413929545353,
      "qty": 25.217,
      "entry_notional": 12364.8054337,
      "gross": -83.08262756548356,
      "fees": 11.090937707925532,
      "net": -94.1735652734091,
      "hold_hours": 123.98333333333333,
      "net_bps_entry": -76.16259372488075,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "eee7d2a9-690a-489d-9a3d-41d3aea5c3ad",
      "opened_at": 1706875200000.0,
      "closed_at": 1707831060000.0,
      "entry": 493.6563,
      "exit": 497.83465904825056,
      "qty": 22.400000000000002,
      "entry_notional": 11057.90112,
      "gross": 93.59524268081259,
      "fees": 9.994228867206365,
      "net": 83.60101381360623,
      "hold_hours": 265.51666666666665,
      "net_bps_entry": 75.60296742245261,
      "entry_types": {
        "MARKET": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "6737ac5d-1d45-4c86-8b8f-e242e9ac1f15",
      "opened_at": 1708704060000.0,
      "closed_at": 1709113320000.0,
      "entry": 509.45689999999996,
      "exit": 505.5580350494787,
      "qty": 21.877,
      "entry_notional": 11145.3886013,
      "gross": -85.29546852255407,
      "fees": 9.992466780334851,
      "net": -95.28793530288893,
      "hold_hours": 113.68333333333334,
      "net_bps_entry": -85.49539070515183,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "7ce018a0-6c74-47da-a5f8-ad407a465998",
      "opened_at": 1709913960000.0,
      "closed_at": 1709922900000.0,
      "entry": 516.8929,
      "exit": 512.6058185901563,
      "qty": 20.026,
      "entry_notional": 10351.297215400002,
      "gross": -85.8530923135313,
      "fees": 9.277533602318911,
      "net": -95.13062591585022,
      "hold_hours": 2.4833333333333334,
      "net_bps_entry": -91.90212969087675,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "ebf0b793-19fb-4b65-aedd-56bc496d8624",
      "opened_at": 1715107800000.0,
      "closed_at": 1716490620000.0,
      "entry": 518.7032,
      "exit": 527.9046017608516,
      "qty": 20.347,
      "entry_notional": 10554.054010400001,
      "gross": 187.22092162804802,
      "fees": 9.582898024092623,
      "net": 177.6380236039554,
      "hold_hours": 384.1166666666667,
      "net_bps_entry": 168.31259668456337,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "27c98fd6-8d7d-4c21-892a-2276d9129405",
      "opened_at": 1720167780000.0,
      "closed_at": 1720717380000.0,
      "entry": 553.9867,
      "exit": 558.2129752324591,
      "qty": 28.755,
      "entry_notional": 15929.8875585,
      "gross": 121.52654430936127,
      "fees": 14.391585747589213,
      "net": 107.13495856177205,
      "hold_hours": 152.66666666666666,
      "net_bps_entry": 67.25405824010736,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "bb1323e6-6e09-4e85-bf26-c92907d8663b",
      "opened_at": 1724043840000.0,
      "closed_at": 1724888460000.0,
      "entry": 556.2546,
      "exit": 555.7377919721578,
      "qty": 15.949,
      "entry_notional": 8871.7046154,
      "gross": -8.242571236056392,
      "fees": 7.980824996803775,
      "net": -16.223396232860168,
      "hold_hours": 234.61666666666667,
      "net_bps_entry": -18.286673121080575,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "357018f2-bbd0-4af7-b190-f038676269a8",
      "opened_at": 1733501040000.0,
      "closed_at": 1733758740000.0,
      "entry": 609.4547,
      "exit": 606.8000281620346,
      "qty": 28.13,
      "entry_notional": 17143.960711,
      "gross": -74.67591880196778,
      "fees": 15.395960476439116,
      "net": -90.0718792784069,
      "hold_hours": 71.58333333333333,
      "net_bps_entry": -52.53854742015041,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "1267c14b-764b-4d8e-bd52-e8c52199124f",
      "opened_at": 1737393900000.0,
      "closed_at": 1737957240000.0,
      "entry": 601.5126,
      "exit": 602.5149517711916,
      "qty": 15.122,
      "entry_notional": 9096.0735372,
      "gross": 15.157563483959166,
      "fees": 8.19328708704778,
      "net": 6.9642763969113854,
      "hold_hours": 156.48333333333332,
      "net_bps_entry": 7.656354545100967,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "c4bc7fe5-0b8c-4d98-90c9-66584339974a",
      "opened_at": 1747404060000.0,
      "closed_at": 1747852020000.0,
      "entry": 592.4619,
      "exit": 586.4655525531616,
      "qty": 14.943,
      "entry_notional": 8853.1581717,
      "gross": -89.60341989810695,
      "fees": 7.9275208155758525,
      "net": -97.5309407136828,
      "hold_hours": 124.43333333333334,
      "net_bps_entry": -110.1651397412622,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "228d99e4-f79e-4fd1-af1b-9b6ec44f67b2",
      "opened_at": 1749536400000.0,
      "closed_at": 1749777660000.0,
      "entry": 602.1211,
      "exit": 596.8335679220612,
      "qty": 16.395,
      "entry_notional": 9871.7754345,
      "gross": -86.68908841780649,
      "fees": 8.845587801261987,
      "net": -95.53467621906847,
      "hold_hours": 67.01666666666667,
      "net_bps_entry": -96.77557684830708,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "0aed5641-504f-417e-8159-6c3d6938c936",
      "opened_at": 1750867380000.0,
      "closed_at": 1753821600000.0,
      "entry": 609.9179,
      "exit": 636.4563785540879,
      "qty": 15.466000000000001,
      "entry_notional": 9432.9902414,
      "gross": 410.4441093175228,
      "fees": 8.674391066452886,
      "net": 401.76971825106995,
      "hold_hours": 820.6166666666667,
      "net_bps_entry": 425.91978574064666,
      "entry_types": {
        "LIMIT": 1
      },
      "exit_types": {
        "STOP": 1
      }
    },
    {
      "id": "558410f6-9c92-4af2-8c0d-7be3a5ede71e",
      "opened_at": 1761652800000.0,
      "closed_at": 1761852120000.0,
      "entry": 687.9354,
      "exit": 683.2740053587016,
      "qty": 18.181,
      "entry_notional": 12507.3535074,
      "gross": -84.74881597344393,
      "fees": 11.21848118947195,
      "net": -95.96729716291587,
      "hold_hours": 55.36666666666667,
      "net_bps_entry": -76.72869972543484,
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
