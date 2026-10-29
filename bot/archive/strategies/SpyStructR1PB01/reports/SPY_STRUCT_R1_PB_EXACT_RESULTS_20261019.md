# PB exact results

Job028bb8cbb6a5484ba89cca3b7abeb27f succeeded. Eight complete snapshots, no truncation. URLs from verified MCP metadata.

```json
{
  "rows": {
    "B01": {
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
    "B02": {
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
    "B03": {
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
    "B04": {
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
    "B05": {
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
    "B06": {
      "name": "B06",
      "url": "http://localhost:9200/#/backtest/1dfe0426-3bfd-4835-ad45-ccfd11b58646",
      "n": 19,
      "net": 571.7530451590001,
      "gross_before_fees": 762.6834330150468,
      "fees": 190.93038785604676,
      "pf": 1.5099082131681496,
      "sharpe": 0.4183644741082198,
      "dd_motor_pct": -6.275390218471532,
      "cagr_motor_pct": 1.0721385292109753,
      "time_exposure_pct": 7.127415776259706,
      "entry_price_notional_time": 0.07979347810998393,
      "mean_hold_hours": 171.3280701754386,
      "turnover_two_sides": 424289.75079121505,
      "total_entry_notional": 211763.53367910002,
      "net_bps_per_entry_notional": 26.99959880842455,
      "net_plus5bpsRT": 465.6806074611963,
      "net_plus10bpsRT": 359.60816976339254,
      "net_exbest": -38.52495342401221,
      "net_ex3best": -610.5712665711965,
      "close_year_cohorts": {
        "2021": {
          "n": 2,
          "net": 499.259792893952,
          "fees": 18.497734784945507
        },
        "2022": {
          "n": 3,
          "net": -40.098638195967,
          "fees": 16.67368640214278
        },
        "2023": {
          "n": 5,
          "net": 718.4229378075476,
          "fees": 54.72438606813406
        },
        "2024": {
          "n": 6,
          "net": -358.1442335712496,
          "fees": 75.1566280034845
        },
        "2025": {
          "n": 3,
          "net": -247.68681377528299,
          "fees": 25.877952597339924
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
          "trade_id": "b4688dcc-d5d1-44f8-a045-2718a2fe20a0",
          "side": "sell",
          "type": "MARKET",
          "gross": 5.624073200000566,
          "net": -4.6486387950994335,
          "fee": 10.2727119951,
          "exit_fee": 5.137621414020001
        }
      ],
      "metric_preterminal_open_count": 1,
      "fingerprint": "833606fd187d2ca0ea2450022d5e4b88c081103177cd68f54ef01c5c1414843c",
      "audit": "passed"
    },
    "Cq": {
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
    "M": {
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
    }
  },
  "pairs": {
    "B01_B02": {
      "net_delta": -431.595216803105,
      "n_delta": -15,
      "common_exact_open_timestamps": 20,
      "common_entry_price_equal": 20,
      "common_norm_netbps_delta_sum": 0.00043730676657105505,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "B03_B04": {
      "net_delta": -205.3413959501006,
      "n_delta": -9,
      "common_exact_open_timestamps": 4,
      "common_entry_price_equal": 4,
      "common_norm_netbps_delta_sum": 7.638543177534984e-05,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "B05_B06": {
      "net_delta": 615.2086004261347,
      "n_delta": -29,
      "common_exact_open_timestamps": 8,
      "common_entry_price_equal": 8,
      "common_norm_netbps_delta_sum": 0.017820870849355686,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    }
  },
  "span_hours": 45672.0,
  "notes": [
    "Cohorts are year of trade closing, not calendar MTM.",
    "RT stress static same fills/qty, no decision or risk recalculation.",
    "Notional-time valued at entry price, not actual MTM exposure.",
    "Concentration exclusions are descriptive, no retrospective trading filter."
  ]
}
```
