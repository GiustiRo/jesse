# Last mechanism exact results

Eight complete snapshots. Originalaudit0ed613d8ea28425088dbe575ee0c5bc2 succeeded; followupdcbbcdb9950b4a69b9e516da8f4b0b70 succeeded. Followup combinedex3+10bps is POSTHOC diagnostic, not a predeclared promotion gate; same frozen backtests and no additional fulls.

```json
{
  "rows": {
    "MECH01": {
      "name": "MECH01",
      "url": "http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592",
      "n": 12,
      "net": 1179.9815614338597,
      "gross_before_fees": 1293.1048935173326,
      "fees": 113.1233320834728,
      "pf": 4.044531891325093,
      "sharpe": 1.0083101800688141,
      "dd_motor_pct": -2.4866856144054705,
      "cagr_motor_pct": 2.162407247921605,
      "time_exposure_pct": 8.130765749985404,
      "entry_price_notional_time": 0.07654082007699883,
      "mean_hold_hours": 309.45694444444445,
      "turnover_two_sides": 251385.18240771734,
      "total_entry_notional": 125046.0387571,
      "net_bps_per_entry_notional": 94.36376978929782,
      "net_plus5bpsRT": 1117.1352658319304,
      "net_plus10bpsRT": 1054.288970230001,
      "net_exbest": 748.9160186067709,
      "net_ex3best": 200.13042443505128,
      "net_exbest_plus10bpsRT": 633.9221258370211,
      "net_ex3best_plus10bpsRT": 105.62345322528937,
      "close_year_cohorts": {
        "2020": {
          "n": 1,
          "net": 137.97951328203996,
          "fees": 3.3286263618797642
        },
        "2021": {
          "n": 1,
          "net": 337.5690574955404,
          "fees": 8.552495880169069
        },
        "2022": {
          "n": 1,
          "net": -99.22117074919896,
          "fees": 4.935835497036526
        },
        "2023": {
          "n": 4,
          "net": 115.79681277005115,
          "fees": 42.159173777076205
        },
        "2024": {
          "n": 3,
          "net": 355.414199555051,
          "fees": 35.695101490220374
        },
        "2025": {
          "n": 2,
          "net": 332.44314908037614,
          "fees": 18.45209907709086
        }
      },
      "executed_order_types": {
        "LIMIT": 9,
        "STOP": 12,
        "MARKET": 3
      },
      "entry_order_types": {
        "LIMIT": 9,
        "MARKET": 3
      },
      "exit_order_types": {
        "STOP": 12
      },
      "terminal_orders": [],
      "metric_preterminal_open_count": 0,
      "fingerprint": "10e2b181a3247255d5dbd618ad546426dc8f9619c974241631b01537a47332d6",
      "audit": "passed"
    },
    "MECH02": {
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
    "MECH03": {
      "name": "MECH03",
      "url": "http://localhost:9200/#/backtest/0bab147d-6089-416a-b4ab-e92ba35cb9ea",
      "n": 10,
      "net": 697.9686460382638,
      "gross_before_fees": 804.0369719539531,
      "fees": 106.06832591568929,
      "pf": 2.9665993185601143,
      "sharpe": 0.6732998917480437,
      "dd_motor_pct": -2.3324495156439085,
      "cagr_motor_pct": 1.3024768808721277,
      "time_exposure_pct": 5.197750627663924,
      "entry_price_notional_time": 0.05577949781836071,
      "mean_hold_hours": 237.3916666666667,
      "turnover_two_sides": 235707.39092375396,
      "total_entry_notional": 117451.6769759,
      "net_bps_per_entry_notional": 59.426026431404686,
      "net_plus5bpsRT": 639.0417983073254,
      "net_plus10bpsRT": 580.1149505763868,
      "net_exbest": 277.89820960156555,
      "net_ex3best": -237.75192905000836,
      "net_exbest_plus10bpsRT": 170.6202012937262,
      "net_ex3best_plus10bpsRT": -324.2643627287388,
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
          "n": 2,
          "net": -42.77371478205806,
          "fees": 26.250050111998476
        },
        "2025": {
          "n": 1,
          "net": 420.0704364366983,
          "fees": 9.518118438633898
        }
      },
      "executed_order_types": {
        "MARKET": 2,
        "STOP": 10,
        "LIMIT": 8
      },
      "entry_order_types": {
        "MARKET": 2,
        "LIMIT": 8
      },
      "exit_order_types": {
        "STOP": 10
      },
      "terminal_orders": [],
      "metric_preterminal_open_count": 0,
      "fingerprint": "322ee2c0153ba4844b20b843d57aade9b183536c59c32f3bfd4006f01b2d703f",
      "audit": "passed"
    },
    "MECH04": {
      "name": "MECH04",
      "url": "http://localhost:9200/#/backtest/f57f4702-b30f-4cf1-b43f-80a6d4e09e05",
      "n": 16,
      "net": 874.7958565504204,
      "gross_before_fees": 1025.389857801811,
      "fees": 150.5940012513908,
      "pf": 2.320269711623384,
      "sharpe": 0.7183938780138998,
      "dd_motor_pct": -3.8005064163188162,
      "cagr_motor_pct": 1.6215132040717561,
      "time_exposure_pct": 8.78747737490512,
      "entry_price_notional_time": 0.08121036182627324,
      "mean_hold_hours": 250.83854166666666,
      "turnover_two_sides": 334653.3361142018,
      "total_entry_notional": 166813.97312819998,
      "net_bps_per_entry_notional": 52.44140164913652,
      "net_plus5bpsRT": 791.1325225218699,
      "net_plus10bpsRT": 707.4691884933195,
      "net_exbest": 455.514513978981,
      "net_ex3best": -86.35598247698488,
      "net_exbest_plus10bpsRT": 298.5940700283137,
      "net_ex3best_plus10bpsRT": -223.07893097807187,
      "close_year_cohorts": {
        "2020": {
          "n": 1,
          "net": 137.97951328203996,
          "fees": 3.3286263618797642
        },
        "2021": {
          "n": 2,
          "net": 246.37563263516452,
          "fees": 20.26102000096626
        },
        "2022": {
          "n": 2,
          "net": -110.69546618442911,
          "fees": 11.312388365121311
        },
        "2023": {
          "n": 6,
          "net": -67.92668184187492,
          "fees": 63.022585116543596
        },
        "2024": {
          "n": 3,
          "net": 345.71519911248186,
          "fees": 34.721055221010076
        },
        "2025": {
          "n": 2,
          "net": 323.34765954703806,
          "fees": 17.94832618586981
        }
      },
      "executed_order_types": {
        "LIMIT": 11,
        "STOP": 16,
        "MARKET": 5
      },
      "entry_order_types": {
        "LIMIT": 11,
        "MARKET": 5
      },
      "exit_order_types": {
        "STOP": 16
      },
      "terminal_orders": [],
      "metric_preterminal_open_count": 0,
      "fingerprint": "e102e42a463c033a5cff19992945106a82c9f3d358f82a1bb3d749d2e309e457",
      "audit": "passed"
    },
    "MECH05": {
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
    "MECH06": {
      "name": "MECH06",
      "url": "http://localhost:9200/#/backtest/bddded48-b986-40f2-a951-6d7de7cf9c65",
      "n": 12,
      "net": 962.2141582992981,
      "gross_before_fees": 1081.4718254119934,
      "fees": 119.2576671126954,
      "pf": 3.5163421885325037,
      "sharpe": 0.8231146879007425,
      "dd_motor_pct": -2.9289574394842255,
      "cagr_motor_pct": 1.7776893671002103,
      "time_exposure_pct": 6.638020377182227,
      "entry_price_notional_time": 0.0731582633364019,
      "mean_hold_hours": 252.64305555555555,
      "turnover_two_sides": 265017.03802821203,
      "total_entry_notional": 131967.7831014,
      "net_bps_per_entry_notional": 72.91280763275095,
      "net_plus5bpsRT": 895.9598987922451,
      "net_plus10bpsRT": 829.7056392851921,
      "net_exbest": 539.5659013691004,
      "net_ex3best": 57.72954538738702,
      "net_exbest_plus10bpsRT": 417.54717055504955,
      "net_ex3best_plus10bpsRT": -42.4007423119714,
      "close_year_cohorts": {
        "2021": {
          "n": 2,
          "net": 189.58210941171166,
          "fees": 21.71813145086816
        },
        "2022": {
          "n": 2,
          "net": -108.62122192470657,
          "fees": 11.10046763786092
        },
        "2023": {
          "n": 3,
          "net": 206.81929028856132,
          "fees": 33.34712022067916
        },
        "2024": {
          "n": 3,
          "net": 348.48847477499396,
          "fees": 34.9996091098882
        },
        "2025": {
          "n": 2,
          "net": 325.9455057487378,
          "fees": 18.092338693398965
        }
      },
      "executed_order_types": {
        "MARKET": 4,
        "STOP": 12,
        "LIMIT": 8
      },
      "entry_order_types": {
        "MARKET": 4,
        "LIMIT": 8
      },
      "exit_order_types": {
        "STOP": 12
      },
      "terminal_orders": [],
      "metric_preterminal_open_count": 0,
      "fingerprint": "67c55b367685fc8041907c977ca026f1528375a1e766eb84eb8230dfd39cb190",
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
      "net_exbest_plus10bpsRT": 40.91006878171572,
      "net_ex3best_plus10bpsRT": -587.1236565565748,
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
    "BR02": {
      "name": "BR02",
      "url": "http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810",
      "n": 16,
      "net": 874.7958565504204,
      "gross_before_fees": 1025.389857801811,
      "fees": 150.5940012513908,
      "pf": 2.320269711623384,
      "sharpe": 0.7183938780138998,
      "dd_motor_pct": -3.8005064163188162,
      "cagr_motor_pct": 1.6215132040717561,
      "time_exposure_pct": 8.78747737490512,
      "entry_price_notional_time": 0.08121036182627324,
      "mean_hold_hours": 250.83854166666666,
      "turnover_two_sides": 334653.3361142018,
      "total_entry_notional": 166813.97312819998,
      "net_bps_per_entry_notional": 52.44140164913652,
      "net_plus5bpsRT": 791.1325225218699,
      "net_plus10bpsRT": 707.4691884933195,
      "net_exbest": 455.514513978981,
      "net_ex3best": -86.35598247698488,
      "net_exbest_plus10bpsRT": 298.5940700283137,
      "net_ex3best_plus10bpsRT": -223.07893097807187,
      "close_year_cohorts": {
        "2020": {
          "n": 1,
          "net": 137.97951328203996,
          "fees": 3.3286263618797642
        },
        "2021": {
          "n": 2,
          "net": 246.37563263516452,
          "fees": 20.26102000096626
        },
        "2022": {
          "n": 2,
          "net": -110.69546618442911,
          "fees": 11.312388365121311
        },
        "2023": {
          "n": 6,
          "net": -67.92668184187492,
          "fees": 63.022585116543596
        },
        "2024": {
          "n": 3,
          "net": 345.71519911248186,
          "fees": 34.721055221010076
        },
        "2025": {
          "n": 2,
          "net": 323.34765954703806,
          "fees": 17.94832618586981
        }
      },
      "executed_order_types": {
        "LIMIT": 11,
        "STOP": 16,
        "MARKET": 5
      },
      "entry_order_types": {
        "LIMIT": 11,
        "MARKET": 5
      },
      "exit_order_types": {
        "STOP": 16
      },
      "terminal_orders": [],
      "metric_preterminal_open_count": 0,
      "fingerprint": "e102e42a463c033a5cff19992945106a82c9f3d358f82a1bb3d749d2e309e457",
      "audit": "passed"
    }
  },
  "pairs": {
    "BR02_MECH01": {
      "net_delta": 305.18570488343937,
      "n_delta": -4,
      "common_exact_open_timestamps": 12,
      "common_entry_price_equal": 12,
      "common_norm_netbps_delta_sum": -9.237055564881302e-14,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "BR02_MECH02": {
      "net_delta": -104.24757320082585,
      "n_delta": -5,
      "common_exact_open_timestamps": 4,
      "common_entry_price_equal": 4,
      "common_norm_netbps_delta_sum": -8.881784197001252e-14,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "BR02_MECH03": {
      "net_delta": -176.8272105121565,
      "n_delta": -6,
      "common_exact_open_timestamps": 4,
      "common_entry_price_equal": 4,
      "common_norm_netbps_delta_sum": -8.881784197001252e-14,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "BR02_MECH04": {
      "net_delta": 0.0,
      "n_delta": 0,
      "common_exact_open_timestamps": 16,
      "common_entry_price_equal": 16,
      "common_norm_netbps_delta_sum": 0.0,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "BR02_MECH05": {
      "net_delta": 400.3677576724996,
      "n_delta": 3,
      "common_exact_open_timestamps": 3,
      "common_entry_price_equal": 3,
      "common_norm_netbps_delta_sum": -1.3571366253017914e-12,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "BR02_MECH06": {
      "net_delta": 87.41830174887775,
      "n_delta": -4,
      "common_exact_open_timestamps": 11,
      "common_entry_price_equal": 11,
      "common_norm_netbps_delta_sum": -2.064126647383091e-12,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "MECH01_MECH02": {
      "net_delta": -409.4332780842652,
      "n_delta": -1,
      "common_exact_open_timestamps": 0,
      "common_entry_price_equal": 0,
      "common_norm_netbps_delta_sum": 0.0,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    },
    "MECH03_MECH04": {
      "net_delta": 176.8272105121565,
      "n_delta": 6,
      "common_exact_open_timestamps": 4,
      "common_entry_price_equal": 4,
      "common_norm_netbps_delta_sum": 8.881784197001252e-14,
      "notes": "Selected intersection; not causal matched exposure. Exit/occupancy/capital differ."
    }
  },
  "curve_fingerprints": {
    "MECH01": "5f05acf47d07e7491edfc74eb8e37afb5187fb8f3e4affcff73030b3e57be45b",
    "MECH02": "98779ee6c80e49c775e7fc7acc2edd7371fdc9d359fbf4dc0f1e7d913d6e794c",
    "MECH03": "0c136775f80d5b6ec9e57a7488400a287824bc40c322dc55185800e7d87cb34d",
    "MECH04": "50b47a33e02537e04b75008212fbcf78f4d3f6b4d8f895fce9bda4a11c5d10b2",
    "MECH05": "67d2edfe206d71a3742dc5dbca990501dd0e5914e0991e41be28ac6bd6ac9dae",
    "MECH06": "dcb5148ffee294e9ab7874a3a558705e72a316db68320f756aa8fb05f9acac58",
    "Cq": "43cb5096a70aa8ff93d99c3cbfacb7c2991baea66bf95358bdd016fe727b5c90",
    "BR02": "50b47a33e02537e04b75008212fbcf78f4d3f6b4d8f895fce9bda4a11c5d10b2"
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
