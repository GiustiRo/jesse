# X03 R3 — FIXED_STRESS_C

2026 cerrado; muestra de desarrollo2020-10-15→2025-12-31 exclusiva. Auditoría de fills, cantidades, fees,PNL,wallet yterminal, con MTM UTC diario. Costes+5/+10 adicionales al fee de CADA sesión, sobre recorridos y cantidades fijos; no confundir overlays de sesiones ya estresadas con el estrés original. Monthclassallcalendar, denominadores activos se conservan en auditoría.

## [X03S_C](http://localhost:9200/#/backtest/24e0fc97-92d3-4b55-8c19-afc149e9f993)

```json
{
  "audit": {
    "n": 281,
    "net": 9420.86700257421,
    "gross_before_fees": 12243.822061228415,
    "fees": 2822.955058654205,
    "pf_from_trades": 1.604434823255587,
    "PF_engine": 1.604434823255587,
    "sharpe_engine": 1.2694773916600763,
    "cagr_engine": 13.577058547625608,
    "dd_engine": -9.11705774767928,
    "plus5_samefills": 8412.668767340567,
    "plus10_samefills": 7404.470532106922,
    "exbest": 7580.611974560343,
    "ex3best": 5524.286931909799,
    "ex3best_plus10_samefills": 3531.6575805612556,
    "time_any_position_pct": 40.63864804110469,
    "entry_notional_time_initial_equity": 0.42720444808738434,
    "entry_turnover_initial_equity": 201.44347933684247,
    "two_side_turnover_initial_equity": 403.27929409345796,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4527.497139739902,
        "fees": 209.7573835162794,
        "plus10": 4377.670437228276,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.050926860703593375
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 2564.95186689775,
        "fees": 1595.2820648531895,
        "plus10": 1425.4646777169005,
        "time_open_pct": 10.7327246452969,
        "entry_notional_time_initial_equity": 0.05552799089298232
      },
      "PAXG-USDT:long": {
        "n": 39,
        "net": 690.703235113072,
        "fees": 637.7989040283991,
        "plus10": 235.1325893785011,
        "time_open_pct": 14.987300753196706,
        "entry_notional_time_initial_equity": 0.16759458160255972
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1637.7147608234877,
        "fees": 380.1167062563359,
        "plus10": 1366.2028277832478,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.15315501488824884
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7092.449006637652,
        "fees": 1805.0394483694686
      },
      "PAXG-USDT": {
        "n": 39,
        "net": 690.703235113072,
        "fees": 637.7989040283991
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1637.7147608234877,
        "fees": 380.1167062563359
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 372.19241733108896,
        "by_symbol": {
          "BTC-USDT": 250.9675097666189,
          "PAXG-USDT": 0,
          "SPY-USDT": 121.22490756447006
        }
      },
      "2021": {
        "n": 55,
        "net": 1726.4844070370918,
        "by_symbol": {
          "BTC-USDT": 1833.1927345196793,
          "PAXG-USDT": -246.57232874365363,
          "SPY-USDT": 139.86400126106543
        }
      },
      "2022": {
        "n": 42,
        "net": 1071.8222756026807,
        "by_symbol": {
          "BTC-USDT": 1282.3440246828923,
          "PAXG-USDT": -121.12180792737098,
          "SPY-USDT": -89.39994115284043
        }
      },
      "2023": {
        "n": 57,
        "net": 2613.255142712228,
        "by_symbol": {
          "BTC-USDT": 2253.888188496869,
          "PAXG-USDT": -284.4918736061375,
          "SPY-USDT": 643.8588278214961
        }
      },
      "2024": {
        "n": 57,
        "net": 1845.9021772544972,
        "by_symbol": {
          "BTC-USDT": 387.4126464855991,
          "PAXG-USDT": 1060.276026358474,
          "SPY-USDT": 398.21350441042466
        }
      },
      "2025": {
        "n": 58,
        "net": 1791.210582636627,
        "by_symbol": {
          "BTC-USDT": 1084.6439026859953,
          "PAXG-USDT": 282.6132190317603,
          "SPY-USDT": 423.9534609188719
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 141,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3748.5515483913864,
        "fees": 178.87783198626437,
        "gross": 3927.429380377651,
        "plus10": 3620.7816684011977,
        "exbest": 1908.2965203775354,
        "ex3": 62.23146398849161,
        "ex3_plus10": -47.72565012338089,
        "year_net": {
          "2020": 472.3208559184019,
          "2021": 1513.22272474593,
          "2022": -169.502311686705,
          "2023": 1763.4035885822886,
          "2024": 585.4621100597587,
          "2025": -416.35541922828736
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 778.9455913485173,
        "fees": 30.879551530014975,
        "gross": 809.8251428785322,
        "plus10": 756.888768827078,
        "exbest": 188.86188125806942,
        "ex3": -142.40469087584782,
        "ex3_plus10": -150.4801013177192,
        "year_net": {
          "2021": 331.26657213391724,
          "2025": 447.6790192146001
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1668.9975620322837,
        "fees": 667.3616772904744,
        "gross": 2336.359239322758,
        "plus10": 1192.3106496819457,
        "exbest": 1335.0677295665964,
        "ex3": 753.6818918029458,
        "ex3_plus10": 300.6578468103403,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 358.14034551391774,
          "2022": 747.4556294311359,
          "2023": 113.08913142270819,
          "2024": -137.16725118590506,
          "2025": 653.3150358424277
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 895.9543048654656,
        "fees": 927.9203875627163,
        "gross": 1823.8746924281825,
        "plus10": 233.15402803495465,
        "exbest": 713.5702038550132,
        "ex3": 367.31038527224973,
        "ex3_plus10": -259.90976556474084,
        "year_net": {
          "2020": -155.51801715978297,
          "2021": -369.43690787408514,
          "2022": 704.3907069384613,
          "2023": 377.3954684918728,
          "2024": -60.88221238825497,
          "2025": 400.00526685725487
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 39,
        "net": 690.703235113072,
        "fees": 637.7989040283991,
        "gross": 1328.5021391414705,
        "plus10": 235.1325893785011,
        "exbest": -247.33445021249375,
        "ex3": -1225.7920609421135,
        "ex3_plus10": -1655.2854555128417,
        "year_net": {
          "2021": -246.57232874365363,
          "2022": -121.12180792737098,
          "2023": -284.4918736061375,
          "2024": 1060.276026358474,
          "2025": 282.6132190317603
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 19,
        "net": 1637.7147608234877,
        "fees": 380.1167062563359,
        "gross": 2017.8314670798236,
        "plus10": 1366.2028277832478,
        "exbest": 912.7890201063799,
        "ex3": -83.88410022460394,
        "ex3_plus10": -311.10725258694515,
        "year_net": {
          "2020": 121.22490756447006,
          "2021": 139.86400126106543,
          "2022": -89.39994115284043,
          "2023": 643.8588278214961,
          "2024": 398.21350441042466,
          "2025": 423.9534609188719
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4737.254523256182,
        "exbest": 2687.242111726054,
        "ex3best": 841.1770553370079,
        "ex3best_plus10": 709.1631187036968,
        "years": {
          "2020": {
            "n": 3,
            "net": 472.3208559184019,
            "plus10": 464.1181085672969
          },
          "2021": {
            "n": 6,
            "net": 1844.4892968798472,
            "plus10": 1829.7989343276208
          },
          "2022": {
            "n": 4,
            "net": -169.502311686705,
            "plus10": -179.80228651324023
          },
          "2023": {
            "n": 4,
            "net": 1763.4035885822886,
            "plus10": 1737.6990484098767
          },
          "2024": {
            "n": 8,
            "net": 585.4621100597587,
            "plus10": 543.3258336112151
          },
          "2025": {
            "n": 6,
            "net": 31.323599986312786,
            "plus10": -17.469201174493037
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4160.233931750938,
        "exbest": 2231.0220344320524,
        "ex3best": 1649.6361966684062,
        "ex3best_plus10": 533.8118748452843,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.35334615178294,
            "plus10": -242.62881617121303
          },
          "2021": {
            "n": 40,
            "net": -11.296562360167314,
            "plus10": -120.80472390156868
          },
          "2022": {
            "n": 33,
            "net": 1451.846336369599,
            "plus10": 1310.7809605913048
          },
          "2023": {
            "n": 40,
            "net": 490.4845999145818,
            "plus10": 183.99801205350138
          },
          "2024": {
            "n": 38,
            "net": -198.04946357415972,
            "plus10": -435.52193336800144
          },
          "2025": {
            "n": 33,
            "net": 1053.3203026996832,
            "plus10": 729.6411785128752
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1328.502139141471,
        "exbest": -247.33445021249375,
        "ex3best": -1225.7920609421135,
        "ex3best_plus10": -1655.2854555128417,
        "years": {
          "2021": {
            "n": 6,
            "net": -246.5723287436536,
            "plus10": -287.34158002317747
          },
          "2022": {
            "n": 3,
            "net": -121.12180792737098,
            "plus10": -144.66075318508769
          },
          "2023": {
            "n": 7,
            "net": -284.4918736061375,
            "plus10": -382.80727334915457
          },
          "2024": {
            "n": 7,
            "net": 1060.276026358474,
            "plus10": 988.0766368726545
          },
          "2025": {
            "n": 16,
            "net": 282.6132190317602,
            "plus10": 61.86555906326612
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2017.8314670798245,
        "exbest": 912.7890201063799,
        "ex3best": -83.88410022460394,
        "ex3best_plus10": -311.10725258694515,
        "years": {
          "2020": {
            "n": 1,
            "net": 121.22490756447006,
            "plus10": 117.69158375822344
          },
          "2021": {
            "n": 3,
            "net": 139.86400126106543,
            "plus10": 107.85882440283417
          },
          "2022": {
            "n": 2,
            "net": -89.39994115284043,
            "plus10": -102.33343329616434
          },
          "2023": {
            "n": 6,
            "net": 643.8588278214962,
            "plus10": 548.7303694350148
          },
          "2024": {
            "n": 4,
            "net": 398.21350441042466,
            "plus10": 328.6434409287823
          },
          "2025": {
            "n": 3,
            "net": 423.95346091887194,
            "plus10": 365.61204255455755
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "X03S_C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6229508196721312,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6031746031746031,
      "win_months_active": 0.6031746031746031,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.047311848174169224
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.04845538838798524
      ],
      "daily_close_drawdown_pct": -9.175022500339015,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.05727662159388638,
          "SPY-USDT": -0.02829735818484261
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.05727662159388638,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.0516164506852687
        },
        "SPY-USDT": {
          "BTC-USDT": -0.02829735818484261,
          "PAXG-USDT": 0.0516164506852687,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04066056152449837,
        "2021-12-31 00:00:00+00:00": 0.16259588108580036,
        "2022-12-31 00:00:00+00:00": 0.08859004097405943,
        "2023-12-31 00:00:00+00:00": 0.19841732062515494,
        "2024-12-31 00:00:00+00:00": 0.11694950066206222,
        "2025-12-31 00:00:00+00:00": 0.10160212655142398
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.08773417645753848,
        "SPY-USDT": -0.04534061725969086
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.08773417645753848,
        "PAXG-USDT": 1,
        "SPY-USDT": 0.010162272814254148
      },
      "SPY-USDT": {
        "BTC-USDT": -0.04534061725969086,
        "PAXG-USDT": 0.010162272814254148,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 21,
        "both_negative_and_portfolio_negative": 2
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.047311848174169224,
        "contributions": {
          "BTC-USDT": -0.029662734774357727,
          "PAXG-USDT": -0.009069377396257053,
          "SPY-USDT": -0.008579736003554463
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.03167488765685966,
        "contributions": {
          "BTC-USDT": -0.03167488765685959,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.01969364611834601,
        "contributions": {
          "BTC-USDT": -0.01969364611834592,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-06-30 00:00:00+00:00",
        "portfolio_return": -0.019356297022470437,
        "contributions": {
          "BTC-USDT": -0.01935629702247039,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01646694281433514,
        "contributions": {
          "BTC-USDT": -0.015358512746994681,
          "PAXG-USDT": -0.008585067560674687,
          "SPY-USDT": 0.007476637493334177
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.016373487394033104,
        "contributions": {
          "BTC-USDT": -0.007312213945083112,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.00906127344895007
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.015234170072185527,
        "contributions": {
          "BTC-USDT": -0.015234170072185494,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.01078537683661851,
        "contributions": {
          "BTC-USDT": -0.001248942105531313,
          "PAXG-USDT": -0.00953643473108728,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.010373287310565527,
        "contributions": {
          "BTC-USDT": -0.010373287310565478,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006571439354684294,
        "contributions": {
          "BTC-USDT": 0.0028563610297716586,
          "PAXG-USDT": -0.009427800384455908,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -9.175022500339015,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -764.56011019558,
        "PAXG-USDT": -203.9317532580503,
        "SPY-USDT": -96.37657241516268
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8412.668767340569,
        "extra_cost": 1008.1982352336447,
        "samefills_cagr_pct": 12.421669825974856,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 37,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -9.449933666624833,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.0491361660181876
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03882275471258412,
          "2021-12-31 00:00:00+00:00": 0.15358318089399936,
          "2022-12-31 00:00:00+00:00": 0.08160289727772208,
          "2023-12-31 00:00:00+00:00": 0.18133871073650676,
          "2024-12-31 00:00:00+00:00": 0.10679273398678846,
          "2025-12-31 00:00:00+00:00": 0.08647013875835419
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 7404.470532106925,
        "extra_cost": 2016.3964704672894,
        "samefills_cagr_pct": 11.213965447939444,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 35,
          "win_months_all": 0.5737704918032787,
          "win_months_active": 0.5737704918032787,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 35,
          "win_months_all": 0.5555555555555556,
          "win_months_active": 0.5555555555555556,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -9.726505686828023,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.05097350075290685
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.036984947900670084,
          "2021-12-31 00:00:00+00:00": 0.1445385350084063,
          "2022-12-31 00:00:00+00:00": 0.07448036084741205,
          "2023-12-31 00:00:00+00:00": 0.16370054587374772,
          "2024-12-31 00:00:00+00:00": 0.09599026087107432,
          "2025-12-31 00:00:00+00:00": 0.07006837531374344
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00",
          "2024-08-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 10330.53841176333,
        "mean_month_USDT": 169.35308871743163,
        "median_month_USDT": 64.67794597272405,
        "sum_positive_months": 13530.901924263044,
        "sum_negative_months": -3200.3635124997145,
        "worst_month": "2021-04",
        "worst_month_USDT": -531.4561846383112,
        "best3_share_positive_mtm": 0.2637508515969742,
        "class_counts": {
          "loss_base": 23,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 35
        },
        "positive_months": 38,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 17,
          "zero_months": 0,
          "net_before_actual_fees": 13035.658233500806,
          "fee_total": 2705.119821737475,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2023-08",
              "gross": 1.1580520932881342,
              "fee": 47.8788201835347,
              "net": -46.720768090246565
            },
            {
              "month": "2024-07",
              "gross": 2.5362559417134065,
              "fee": 85.70278529353332,
              "net": -83.16652935181992
            },
            {
              "month": "2025-01",
              "gross": 40.856091812225316,
              "fee": 84.48174290076128,
              "net": -43.62565108853596
            },
            {
              "month": "2025-07",
              "gross": 105.63223680055859,
              "fee": 116.84770406755894,
              "net": -11.21546726700035
            },
            {
              "month": "2025-09",
              "gross": 74.37840883950922,
              "fee": 93.97695642650216,
              "net": -19.598547586992936
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 2,
          "PAXG-USDT__SPY-USDT": 2
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 966.1142220490982,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.7255462456287205,
                "extra": 10.387430265513327,
                "after": -4.661884019884383
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -3200.3635124997145,
            "already_negative_after_sum": -3566.3191032316336
          },
          "10": {
            "positive_months": 35,
            "extra_cost": 1932.2284440981964,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.7255462456287205,
                "extra": 20.774860531026654,
                "after": -15.049314285397486
              },
              {
                "month": "2024-08",
                "base": 38.4765326613433,
                "extra": 41.63926785537235,
                "after": -3.162735194029665
              },
              {
                "month": "2025-11",
                "base": 19.727672856111894,
                "extra": 20.001901203270346,
                "after": -0.27422834715616773
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -3200.3635124997145,
            "already_negative_after_sum": -3932.2746939635745
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 9420.86700257421,
        "mean_month_USDT": 149.53757146943192,
        "median_month_USDT": 52.95726771151385,
        "sum_positive_months": 13530.901924263044,
        "sum_negative_months": -4110.0349216888335,
        "worst_month": "2025-12",
        "worst_month_USDT": -718.444453196309,
        "best3_share_positive_mtm": 0.2637508515969742,
        "class_counts": {
          "loss_base": 25,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 35
        },
        "positive_months": 38,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 12243.822061228417,
          "fee_total": 2822.9550586542045,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2023-08",
              "gross": 1.1580520932881342,
              "fee": 47.8788201835347,
              "net": -46.720768090246565
            },
            {
              "month": "2024-07",
              "gross": 2.5362559417134065,
              "fee": 85.70278529353332,
              "net": -83.16652935181992
            },
            {
              "month": "2025-01",
              "gross": 40.856091812225316,
              "fee": 84.48174290076128,
              "net": -43.62565108853596
            },
            {
              "month": "2025-07",
              "gross": 105.63223680055859,
              "fee": 116.84770406755894,
              "net": -11.21546726700035
            },
            {
              "month": "2025-09",
              "gross": 74.37840883950922,
              "fee": 93.97695642650216,
              "net": -19.598547586992936
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 3,
          "PAXG-USDT__SPY-USDT": 3
        },
        "stress": {
          "5": {
            "positive_months": 37,
            "extra_cost": 1008.1982352336446,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.7255462456287205,
                "extra": 10.387430265513327,
                "after": -4.661884019884383
              }
            ],
            "already_negative_months": 25,
            "already_negative_base_sum": -4110.0349216888335,
            "already_negative_after_sum": -4518.0745256053
          },
          "10": {
            "positive_months": 35,
            "extra_cost": 2016.3964704672892,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.7255462456287205,
                "extra": 20.774860531026654,
                "after": -15.049314285397486
              },
              {
                "month": "2024-08",
                "base": 38.4765326613433,
                "extra": 41.63926785537235,
                "after": -3.162735194029665
              },
              {
                "month": "2025-11",
                "base": 19.727672856111894,
                "extra": 20.001901203270346,
                "after": -0.27422834715616773
              }
            ],
            "already_negative_months": 25,
            "already_negative_base_sum": -4110.0349216888335,
            "already_negative_after_sum": -4926.114129521789
          }
        }
      }
    }
  }
}
```

## [N204S_C](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960)

```json
{
  "audit": {
    "n": 281,
    "net": 10408.935273900946,
    "gross_before_fees": 13286.843019108415,
    "fees": 2877.90774520747,
    "pf_from_trades": 1.6628341875414363,
    "PF_engine": 1.6628341875414359,
    "sharpe_engine": 1.3630557226109576,
    "cagr_engine": 14.663261754546442,
    "dd_engine": -9.071459738684062,
    "plus5_samefills": 9381.111079183998,
    "plus10_samefills": 8353.286884467045,
    "exbest": 8533.104138139905,
    "ex3best": 6382.120853140386,
    "ex3best_plus10_samefills": 4351.016235757295,
    "time_any_position_pct": 40.74162871489461,
    "entry_notional_time_initial_equity": 0.44173427565650125,
    "entry_turnover_initial_equity": 205.39933054502913,
    "two_side_turnover_initial_equity": 411.1296778867812,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4608.956639397828,
        "fees": 216.51915467985435,
        "plus10": 4454.30010034079,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.0524880101684026
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3380.8895378591387,
        "fees": 1607.4479880800914,
        "plus10": 2232.7124035162165,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.05758415624381493
      },
      "PAXG-USDT:long": {
        "n": 39,
        "net": 734.7939909370685,
        "fees": 662.0862479047893,
        "plus10": 261.8752424336473,
        "time_open_pct": 14.987300753196706,
        "entry_notional_time_initial_equity": 0.17383206331370013
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1684.295105706913,
        "fees": 391.85435454273477,
        "plus10": 1404.3991381763883,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.15783004593058358
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7989.846177256968,
        "fees": 1823.9671427599455
      },
      "PAXG-USDT": {
        "n": 39,
        "net": 734.7939909370685,
        "fees": 662.0862479047893
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1684.295105706913,
        "fees": 391.85435454273477
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 372.19241733108896,
        "by_symbol": {
          "BTC-USDT": 250.9675097666189,
          "PAXG-USDT": 0,
          "SPY-USDT": 121.22490756447006
        }
      },
      "2021": {
        "n": 53,
        "net": 1835.1161125478463,
        "by_symbol": {
          "BTC-USDT": 1944.281493692324,
          "PAXG-USDT": -249.70512292052695,
          "SPY-USDT": 140.53974177604937
        }
      },
      "2022": {
        "n": 46,
        "net": 1212.5974035899158,
        "by_symbol": {
          "BTC-USDT": 1426.0179302366296,
          "PAXG-USDT": -121.82682218194017,
          "SPY-USDT": -91.59370446477361
        }
      },
      "2023": {
        "n": 56,
        "net": 2811.2431043595534,
        "by_symbol": {
          "BTC-USDT": 2445.3732606635294,
          "PAXG-USDT": -294.86055391361873,
          "SPY-USDT": 660.7303976096429
        }
      },
      "2024": {
        "n": 56,
        "net": 2306.2882411388764,
        "by_symbol": {
          "BTC-USDT": 789.5296985556918,
          "PAXG-USDT": 1103.9707349197297,
          "SPY-USDT": 412.78780766345466
        }
      },
      "2025": {
        "n": 58,
        "net": 1871.4979949336685,
        "by_symbol": {
          "BTC-USDT": 1133.6762843421743,
          "PAXG-USDT": 297.21575503342467,
          "SPY-USDT": 440.6059555580698
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 141,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3811.17663515121,
        "fees": 184.5162619419652,
        "gross": 3995.692897093175,
        "plus10": 3679.3793051926637,
        "exbest": 1935.3454993901673,
        "ex3": 30.423213668229863,
        "ex3_plus10": -83.09555558708311,
        "year_net": {
          "2020": 472.3208559184019,
          "2021": 1528.7938021690584,
          "2022": -177.7837769932911,
          "2023": 1796.0808065479562,
          "2024": 625.40115119403,
          "2025": -433.63620368494543
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 797.7800042466181,
        "fees": 32.002892737889155,
        "gross": 829.7828969845073,
        "plus10": 774.9207951481258,
        "exbest": 185.00076684499913,
        "ex3": -149.3512611624733,
        "ex3_plus10": -157.82059406492377,
        "year_net": {
          "2021": 334.3520280074724,
          "2025": 463.42797623914566
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 2408.927749880736,
        "fees": 657.3259419916893,
        "gross": 3066.253691872424,
        "plus10": 1939.409219886671,
        "exbest": 2059.8192886666047,
        "ex3": 1443.9258851735638,
        "ex3_plus10": 999.348186165456,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 559.5990889746455,
          "2022": 905.3715183440643,
          "2023": 257.1515315145007,
          "2024": 73.51419930267099,
          "2025": 679.1267407368537
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 971.9617879784042,
        "fees": 950.1220460884022,
        "gross": 1922.0838340668051,
        "plus10": 293.3031836295452,
        "exbest": 784.3860330497283,
        "ex3": 419.89021169907903,
        "ex3_plus10": -221.57705904238478,
        "year_net": {
          "2020": -155.51801715978297,
          "2021": -478.4634254588524,
          "2022": 698.4301888858562,
          "2023": 392.14092260107213,
          "2024": 90.61434805899125,
          "2025": 424.7577710511199
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 39,
        "net": 734.7939909370685,
        "fees": 662.0862479047893,
        "gross": 1396.8802388418578,
        "plus10": 261.8752424336473,
        "exbest": -239.04470740457788,
        "ex3": -1267.6559177830068,
        "ex3_plus10": -1713.2695193291977,
        "year_net": {
          "2021": -249.70512292052695,
          "2022": -121.82682218194017,
          "2023": -294.86055391361873,
          "2024": 1103.9707349197297,
          "2025": 297.21575503342467
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 19,
        "net": 1684.295105706913,
        "fees": 391.85435454273477,
        "gross": 2076.149460249648,
        "plus10": 1404.3991381763883,
        "exbest": 928.9943467277697,
        "ex3": -89.25470711406385,
        "ex3_plus10": -323.55487675335434,
        "year_net": {
          "2020": 121.22490756447006,
          "2021": 140.53974177604937,
          "2022": -91.59370446477361,
          "2023": 660.7303976096429,
          "2024": 412.78780766345466,
          "2025": 440.6059555580698
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4825.475794077683,
        "exbest": 2733.1255036367857,
        "ex3best": 828.2032179148478,
        "ex3best_plus10": 691.8252395610426,
        "years": {
          "2020": {
            "n": 3,
            "net": 472.3208559184019,
            "plus10": 464.1181085672969
          },
          "2021": {
            "n": 6,
            "net": 1863.1458301765308,
            "plus10": 1848.3004537379356
          },
          "2022": {
            "n": 4,
            "net": -177.7837769932911,
            "plus10": -188.3715565504845
          },
          "2023": {
            "n": 4,
            "net": 1796.0808065479562,
            "plus10": 1769.6028796958858
          },
          "2024": {
            "n": 8,
            "net": 625.40115119403,
            "plus10": 581.7830787677344
          },
          "2025": {
            "n": 6,
            "net": 29.791772554200264,
            "plus10": -21.132863877579126
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4988.337525939234,
        "exbest": 3031.781076645,
        "ex3best": 2415.8876731519586,
        "ex3best_plus10": 1292.6513697949963,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.35334615178294,
            "plus10": -242.62881617121303
          },
          "2021": {
            "n": 38,
            "net": 81.13566351579303,
            "plus10": -25.942809510309658
          },
          "2022": {
            "n": 37,
            "net": 1603.8017072299203,
            "plus10": 1446.7124082979878
          },
          "2023": {
            "n": 39,
            "net": 649.2924541155729,
            "plus10": 345.35280837581837
          },
          "2024": {
            "n": 37,
            "net": 164.1285473616619,
            "plus10": -70.9856917367029
          },
          "2025": {
            "n": 33,
            "net": 1103.8845117879737,
            "plus10": 780.2045042606363
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1396.8802388418562,
        "exbest": -239.04470740457788,
        "ex3best": -1267.6559177830068,
        "ex3best_plus10": -1713.2695193291977,
        "years": {
          "2021": {
            "n": 6,
            "net": -249.70512292052695,
            "plus10": -290.8655357200264
          },
          "2022": {
            "n": 3,
            "net": -121.82682218194017,
            "plus10": -145.74299018845375
          },
          "2023": {
            "n": 7,
            "net": -294.86055391361873,
            "plus10": -395.87320409178665
          },
          "2024": {
            "n": 7,
            "net": 1103.9707349197297,
            "plus10": 1028.9011825656216
          },
          "2025": {
            "n": 16,
            "net": 297.2157550334248,
            "plus10": 65.45578986829264
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2076.149460249648,
        "exbest": 928.9943467277697,
        "ex3best": -89.25470711406385,
        "ex3best_plus10": -323.55487675335434,
        "years": {
          "2020": {
            "n": 1,
            "net": 121.22490756447006,
            "plus10": 117.69158375822344
          },
          "2021": {
            "n": 3,
            "net": 140.53974177604937,
            "plus10": 108.2108861630322
          },
          "2022": {
            "n": 2,
            "net": -91.59370446477361,
            "plus10": -104.81334146103862
          },
          "2023": {
            "n": 6,
            "net": 660.7303976096428,
            "plus10": 562.7762153933868
          },
          "2024": {
            "n": 4,
            "net": 412.7878076634547,
            "plus10": 340.9225055516446
          },
          "2025": {
            "n": 3,
            "net": 440.6059555580698,
            "plus10": 379.61128877114
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "N204S_C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.639344262295082,
        "quarters_total": 19,
        "positive_quarters": 17,
        "win_quarters": 0.8947368421052632
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6190476190476191,
      "win_quarters": 0.8571428571428571,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.047251327773334295
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.04816889094485366
      ],
      "daily_close_drawdown_pct": -9.129358487210226,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.05689878151177862,
          "SPY-USDT": -0.02630385139288716
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.05689878151177862,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.051030089284193746
        },
        "SPY-USDT": {
          "BTC-USDT": -0.02630385139288716,
          "PAXG-USDT": 0.051030089284193746,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04066056152449837,
        "2021-12-31 00:00:00+00:00": 0.17303460717258634,
        "2022-12-31 00:00:00+00:00": 0.09933372295964626,
        "2023-12-31 00:00:00+00:00": 0.20948307076791073,
        "2024-12-31 00:00:00+00:00": 0.14209026334265262,
        "2025-12-31 00:00:00+00:00": 0.10095775196807155
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.0867858760694634,
        "SPY-USDT": -0.042954144713252304
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.0867858760694634,
        "PAXG-USDT": 1,
        "SPY-USDT": 0.009634342465466387
      },
      "SPY-USDT": {
        "BTC-USDT": -0.042954144713252304,
        "PAXG-USDT": 0.009634342465466387,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 3,
        "both_nonzero": 21,
        "both_negative_and_portfolio_negative": 3
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.047251327773334295,
        "contributions": {
          "BTC-USDT": -0.029601924535286622,
          "PAXG-USDT": -0.009069501288115286,
          "SPY-USDT": -0.008579901949932356
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.031928316618499375,
        "contributions": {
          "BTC-USDT": -0.03192831661849937,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.024528557006199492,
        "contributions": {
          "BTC-USDT": -0.02452855700619958,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.016443029664176767,
        "contributions": {
          "BTC-USDT": -0.015334525730574908,
          "PAXG-USDT": -0.008585372737624853,
          "SPY-USDT": 0.007476868804022884
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.016411135468538895,
        "contributions": {
          "BTC-USDT": -0.007349791976192332,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009061343492346613
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.015658989725591654,
        "contributions": {
          "BTC-USDT": -0.006310888616271645,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009348101109319955
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.014675488679451787,
        "contributions": {
          "BTC-USDT": -0.014675488679451882,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.01340841578924179,
        "contributions": {
          "BTC-USDT": -0.01340841578924167,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010574006342403686,
        "contributions": {
          "BTC-USDT": -0.0010376783223828199,
          "PAXG-USDT": -0.009536328020020881,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.010277739078524584,
        "contributions": {
          "BTC-USDT": -0.01027773907852455,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -9.129358487210226,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -767.8289454562587,
        "PAXG-USDT": -206.31067186266483,
        "SPY-USDT": -97.49949788357696
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9381.111079183995,
        "extra_cost": 1027.8241947169538,
        "samefills_cagr_pct": 13.532427459425932,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6229508196721312,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 38,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6031746031746031,
          "quarters_total": 21,
          "positive_quarters": 17,
          "win_quarters": 0.8095238095238095
        },
        "daily_close_drawdown_pct": -9.735263159936236,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04907366078057429
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03882275471258412,
          "2021-12-31 00:00:00+00:00": 0.1641154514080494,
          "2022-12-31 00:00:00+00:00": 0.0918036988584987,
          "2023-12-31 00:00:00+00:00": 0.19287249232583603,
          "2024-12-31 00:00:00+00:00": 0.13291912270008632,
          "2025-12-31 00:00:00+00:00": 0.0861846734747711
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8353.286884467041,
        "extra_cost": 2055.6483894339076,
        "samefills_cagr_pct": 12.352037956614303,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 36,
          "win_months_all": 0.5714285714285714,
          "win_months_active": 0.5714285714285714,
          "quarters_total": 21,
          "positive_quarters": 16,
          "win_quarters": 0.7619047619047619
        },
        "daily_close_drawdown_pct": -10.527091550826007,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.05090876526736787
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.036984947900670084,
          "2021-12-31 00:00:00+00:00": 0.1551646815197898,
          "2022-12-31 00:00:00+00:00": 0.08413008515363551,
          "2023-12-31 00:00:00+00:00": 0.17570778206427606,
          "2024-12-31 00:00:00+00:00": 0.1231697768898421,
          "2025-12-31 00:00:00+00:00": 0.07021565779277728
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00",
          "2024-08-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 11354.430075336684,
        "mean_month_USDT": 186.1381979563391,
        "median_month_USDT": 98.12091019376385,
        "sum_positive_months": 14865.529548222756,
        "sum_negative_months": -3511.0994728860715,
        "worst_month": "2021-04",
        "worst_month_USDT": -536.9502774176508,
        "best3_share_positive_mtm": 0.27369056878359765,
        "class_counts": {
          "loss_base": 22,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 18,
          "zero_months": 0,
          "net_before_actual_fees": 14109.104813026246,
          "fee_total": 2754.674737689565,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2024-07",
              "gross": 3.1801833836104976,
              "fee": 88.08393386428703,
              "net": -84.90375048067654
            },
            {
              "month": "2025-01",
              "gross": 42.42810060895755,
              "fee": 88.66051236521781,
              "net": -46.23241175626026
            },
            {
              "month": "2025-07",
              "gross": 111.03377869723289,
              "fee": 121.73731171965727,
              "net": -10.70353302242438
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 3,
          "PAXG-USDT__SPY-USDT": 2
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 983.812406317702,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 4.456319338087269,
                "extra": 10.69440562047399,
                "after": -6.2380862823883945
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3511.0994728860715,
            "already_negative_after_sum": -3863.5387748819594
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1967.624812635404,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 4.456319338087269,
                "extra": 21.38881124094798,
                "after": -16.93249190286224
              },
              {
                "month": "2024-08",
                "base": 32.848526737554494,
                "extra": 44.20367054459383,
                "after": -11.355143807038985
              },
              {
                "month": "2025-11",
                "base": 20.727732179690065,
                "extra": 21.01897151515045,
                "after": -0.29123933545997716
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3511.0994728860715,
            "already_negative_after_sum": -4215.978076877858
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 10408.935273900952,
        "mean_month_USDT": 165.22119482382465,
        "median_month_USDT": 66.70557393565832,
        "sum_positive_months": 14865.529548222756,
        "sum_negative_months": -4456.594274321804,
        "worst_month": "2025-12",
        "worst_month_USDT": -754.2678454429224,
        "best3_share_positive_mtm": 0.27369056878359765,
        "class_counts": {
          "loss_base": 24,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 20,
          "zero_months": 0,
          "net_before_actual_fees": 13286.843019108419,
          "fee_total": 2877.9077452074694,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2024-07",
              "gross": 3.1801833836104976,
              "fee": 88.08393386428703,
              "net": -84.90375048067654
            },
            {
              "month": "2025-01",
              "gross": 42.42810060895755,
              "fee": 88.66051236521781,
              "net": -46.23241175626026
            },
            {
              "month": "2025-07",
              "gross": 111.03377869723289,
              "fee": 121.73731171965727,
              "net": -10.70353302242438
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 4,
          "PAXG-USDT__SPY-USDT": 3
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 1027.8241947169536,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 4.456319338087269,
                "extra": 10.69440562047399,
                "after": -6.2380862823883945
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4456.594274321804,
            "already_negative_after_sum": -4853.045364716945
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 2055.648389433907,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 4.456319338087269,
                "extra": 21.38881124094798,
                "after": -16.93249190286224
              },
              {
                "month": "2024-08",
                "base": 32.848526737554494,
                "extra": 44.20367054459383,
                "after": -11.355143807038985
              },
              {
                "month": "2025-11",
                "base": 20.727732179690065,
                "extra": 21.01897151515045,
                "after": -0.29123933545997716
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4456.594274321804,
            "already_negative_after_sum": -5249.496455112096
          }
        }
      }
    }
  }
}
```

## [FBS0_C](http://localhost:9200/#/backtest/b97e3a45-d5df-4bc5-97c1-cb9ab56fdd18)

```json
{
  "audit": {
    "n": 280,
    "net": 10264.855981669974,
    "gross_before_fees": 13101.02364642363,
    "fees": 2836.1676647536547,
    "pf_from_trades": 1.6522801778747167,
    "PF_engine": 1.6522801778747171,
    "sharpe_engine": 1.3516254630678104,
    "cagr_engine": 14.507556935887212,
    "dd_engine": -9.125162489847172,
    "plus5_samefills": 9251.938958543667,
    "plus10_samefills": 8239.021935417368,
    "exbest": 8427.835145269473,
    "ex3best": 6293.5993539624415,
    "ex3best_plus10_samefills": 4300.00998059472,
    "time_any_position_pct": 40.85402434752146,
    "entry_notional_time_initial_equity": 0.435718917694343,
    "entry_turnover_initial_equity": 202.34841715356052,
    "two_side_turnover_initial_equity": 405.16680925052196,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4522.992176602221,
        "fees": 211.58726704054996,
        "plus10": 4371.858414430401,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05138020681837559
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 2589.709060798657,
        "fees": 1610.928045409202,
        "plus10": 1439.0461712206543,
        "time_open_pct": 10.7327246452969,
        "entry_notional_time_initial_equity": 0.056057878883306815
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1498.6774098313472,
        "fees": 630.6344839142218,
        "plus10": 1048.224207035474,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17365030779575405
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1653.4773344377513,
        "fees": 383.0178683896792,
        "plus10": 1379.8931427308373,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.1546305241969067
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 7112.701237400878,
        "fees": 1822.5153124497517
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1498.6774098313472,
        "fees": 630.6344839142218
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1653.4773344377513,
        "fees": 383.0178683896792
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 372.19241733108896,
        "by_symbol": {
          "BTC-USDT": 250.9675097666189,
          "PAXG-USDT": 0,
          "SPY-USDT": 121.22490756447006
        }
      },
      "2021": {
        "n": 55,
        "net": 1704.5666670083704,
        "by_symbol": {
          "BTC-USDT": 1814.6966131812558,
          "PAXG-USDT": -249.6049214803109,
          "SPY-USDT": 139.4749753074252
        }
      },
      "2022": {
        "n": 42,
        "net": 1068.9953005200496,
        "by_symbol": {
          "BTC-USDT": 1279.1368704131542,
          "PAXG-USDT": -120.91195469518041,
          "SPY-USDT": -89.22961519792419
        }
      },
      "2023": {
        "n": 57,
        "net": 2598.203770508793,
        "by_symbol": {
          "BTC-USDT": 2249.869773275224,
          "PAXG-USDT": -294.01676216758506,
          "SPY-USDT": 642.3507594011537
        }
      },
      "2024": {
        "n": 57,
        "net": 1845.5730467584456,
        "by_symbol": {
          "BTC-USDT": 390.83949955346986,
          "PAXG-USDT": 1057.5559027533143,
          "SPY-USDT": 397.1776444516621
        }
      },
      "2025": {
        "n": 57,
        "net": 2675.3247795432308,
        "by_symbol": {
          "BTC-USDT": 1127.1909712111578,
          "PAXG-USDT": 1105.655145421109,
          "SPY-USDT": 442.47866291096415
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 140,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3721.351057942534,
        "fees": 180.2748352252174,
        "gross": 3901.6258931677535,
        "plus10": 3592.5833184959506,
        "exbest": 1884.330221542064,
        "ex3": 53.749797048001284,
        "ex3_plus10": -57.270595825534315,
        "year_net": {
          "2020": 472.3208559184019,
          "2021": 1497.7380928509492,
          "2022": -169.07765388218843,
          "2023": 1760.2266278609836,
          "2024": 587.2497699310755,
          "2025": -427.1066347366873
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 801.6411186596883,
        "fees": 31.312431815332516,
        "gross": 832.9535504750208,
        "plus10": 779.2750959344509,
        "exbest": 188.86188125806942,
        "ex3": -142.40469087584782,
        "ex3_plus10": -150.4801013177192,
        "year_net": {
          "2021": 331.26657213391724,
          "2025": 470.37454652577117
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 1697.6522224163527,
        "fees": 674.6600083364731,
        "gross": 2372.312230752826,
        "plus10": 1215.7522164617292,
        "exbest": 1348.5437612022256,
        "ex3": 754.9033766851471,
        "ex3_plus10": 297.44142486975875,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 360.4341852248144,
          "2022": 744.467065843629,
          "2023": 114.52082188191757,
          "2024": -138.8872470559051,
          "2025": 682.9527255138968
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 892.0568383823038,
        "fees": 936.2680370727296,
        "gross": 1828.3248754550336,
        "plus10": 223.29395475892557,
        "exbest": 705.6991078362817,
        "ex3": 350.9653503969371,
        "ex3_plus10": -276.76788028816975,
        "year_net": {
          "2020": -155.51801715978297,
          "2021": -374.74223702842505,
          "2022": 703.7474584517133,
          "2023": 375.1223235323226,
          "2024": -57.52302332170132,
          "2025": 400.9703339081773
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1498.6774098313472,
        "fees": 630.6344839142218,
        "gross": 2129.311893745568,
        "plus10": 1048.224207035474,
        "exbest": 482.7289758492808,
        "ex3": -1100.7994075538763,
        "ex3_plus10": -1517.883170132905,
        "year_net": {
          "2021": -249.6049214803109,
          "2022": -120.91195469518041,
          "2023": -294.01676216758506,
          "2024": 1057.5559027533143,
          "2025": 1105.655145421109
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 19,
        "net": 1653.4773344377513,
        "fees": 383.0178683896792,
        "gross": 2036.49520282743,
        "plus10": 1379.8931427308373,
        "exbest": 896.9418186186879,
        "ex3": -97.36599075275223,
        "ex3_plus10": -325.9240090354738,
        "year_net": {
          "2020": 121.22490756447006,
          "2021": 139.4749753074252,
          "2022": -89.22961519792419,
          "2023": 642.3507594011537,
          "2024": 397.1776444516621,
          "2025": 442.47866291096415
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4734.579443642772,
        "exbest": 2685.9713402017537,
        "ex3best": 855.3909157076887,
        "ex3best_plus10": 722.0045001089157,
        "years": {
          "2020": {
            "n": 3,
            "net": 472.3208559184019,
            "plus10": 464.1181085672969
          },
          "2021": {
            "n": 6,
            "net": 1829.0046649848664,
            "plus10": 1814.3609103741467
          },
          "2022": {
            "n": 4,
            "net": -169.07765388218843,
            "plus10": -179.35472500503334
          },
          "2023": {
            "n": 4,
            "net": 1760.2266278609836,
            "plus10": 1734.5674690358758
          },
          "2024": {
            "n": 8,
            "net": 587.2497699310754,
            "plus10": 545.2210045103157
          },
          "2025": {
            "n": 6,
            "net": 43.26791178908391,
            "plus10": -7.0543530521996445
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 4200.637106207852,
        "exbest": 2240.600599584521,
        "ex3best": 1646.9602150674475,
        "ex3best_plus10": 520.7353796286792,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.35334615178294,
            "plus10": -242.62881617121303
          },
          "2021": {
            "n": 40,
            "net": -14.308051803610539,
            "plus10": -123.64515887498149
          },
          "2022": {
            "n": 33,
            "net": 1448.2145242953434,
            "plus10": 1307.4370103604763
          },
          "2023": {
            "n": 40,
            "net": 489.64314541424125,
            "plus10": 183.7524739703465
          },
          "2024": {
            "n": 38,
            "net": -196.41027037760642,
            "plus10": -433.06437352097777
          },
          "2025": {
            "n": 33,
            "net": 1083.923059422075,
            "plus10": 747.1950354570041
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2129.31189374557,
        "exbest": 482.7289758492808,
        "ex3best": -1100.7994075538763,
        "ex3best_plus10": -1517.883170132905,
        "years": {
          "2021": {
            "n": 6,
            "net": -249.6049214803109,
            "plus10": -290.3009302847339
          },
          "2022": {
            "n": 3,
            "net": -120.91195469518043,
            "plus10": -144.40840683433024
          },
          "2023": {
            "n": 7,
            "net": -294.01676216758506,
            "plus10": -392.1147893054979
          },
          "2024": {
            "n": 7,
            "net": 1057.555902753314,
            "plus10": 985.5463719303616
          },
          "2025": {
            "n": 15,
            "net": 1105.6551454211094,
            "plus10": 889.5019615296742
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2036.4952028274301,
        "exbest": 896.9418186186879,
        "ex3best": -97.36599075275223,
        "ex3best_plus10": -325.9240090354738,
        "years": {
          "2020": {
            "n": 1,
            "net": 121.22490756447006,
            "plus10": 117.69158375822344
          },
          "2021": {
            "n": 3,
            "net": 139.47497530742518,
            "plus10": 107.5203235427362
          },
          "2022": {
            "n": 2,
            "net": -89.22961519792419,
            "plus10": -102.13988690191803
          },
          "2023": {
            "n": 6,
            "net": 642.3507594011536,
            "plus10": 547.4333868879938
          },
          "2024": {
            "n": 4,
            "net": 397.1776444516621,
            "plus10": 327.7891350136297
          },
          "2025": {
            "n": 3,
            "net": 442.4786629109642,
            "plus10": 381.59860043017216
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "FBS0_C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.639344262295082,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6190476190476191,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.04737466283125247
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.04829565874417174
      ],
      "daily_close_drawdown_pct": -9.18323791816814,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.08563829686239892,
          "SPY-USDT": -0.026619775826347173
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.08563829686239892,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.02710920702196206
        },
        "SPY-USDT": {
          "BTC-USDT": -0.026619775826347173,
          "PAXG-USDT": 0.02710920702196206,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04066056152449837,
        "2021-12-31 00:00:00+00:00": 0.16048974380731917,
        "2022-12-31 00:00:00+00:00": 0.08851673640706048,
        "2023-12-31 00:00:00+00:00": 0.19764584781085293,
        "2024-12-31 00:00:00+00:00": 0.11722420934719957,
        "2025-12-31 00:00:00+00:00": 0.15209756012256692
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.11472886705601758,
        "SPY-USDT": -0.04361082269574867
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.11472886705601758,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.010958642402650768
      },
      "SPY-USDT": {
        "BTC-USDT": -0.04361082269574867,
        "PAXG-USDT": -0.010958642402650768,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 21,
        "both_negative_and_portfolio_negative": 2
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.04737466283125247,
        "contributions": {
          "BTC-USDT": -0.029727161078618333,
          "PAXG-USDT": -0.009068494068715691,
          "SPY-USDT": -0.008579007683918444
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.03173483321412596,
        "contributions": {
          "BTC-USDT": -0.031734833214126026,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.019671637742808334,
        "contributions": {
          "BTC-USDT": -0.01967163774280843,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-06-30 00:00:00+00:00",
        "portfolio_return": -0.019392184217471242,
        "contributions": {
          "BTC-USDT": -0.019392184217471242,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.0170902913791382,
        "contributions": {
          "BTC-USDT": -0.015326572464390124,
          "PAXG-USDT": -0.009240558272233598,
          "SPY-USDT": 0.007476839357485608
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.01633746571379391,
        "contributions": {
          "BTC-USDT": -0.007276308378612438,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009061157335181532
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.015298077767728069,
        "contributions": {
          "BTC-USDT": -0.015298077767728154,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010569602458030736,
        "contributions": {
          "BTC-USDT": -0.0010332181881468918,
          "PAXG-USDT": -0.009536384269884035,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.010392113471866637,
        "contributions": {
          "BTC-USDT": -0.01039211347186657,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006521330009230497,
        "contributions": {
          "BTC-USDT": 0.0029066348128611707,
          "PAXG-USDT": -0.00942796482209171,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -9.18323791816814,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -764.1287812876992,
        "PAXG-USDT": -203.4726272922518,
        "SPY-USDT": -96.15953640025911
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9251.938958543673,
        "extra_cost": 1012.9170231263057,
        "samefills_cagr_pct": 13.386902689662694,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 38,
          "win_months_all": 0.6229508196721312,
          "win_months_active": 0.6229508196721312,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 38,
          "win_months_all": 0.6031746031746031,
          "win_months_active": 0.6031746031746031,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -9.458034856771214,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04920095190025309
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03882275471258412,
          "2021-12-31 00:00:00+00:00": 0.15148975110147922,
          "2022-12-31 00:00:00+00:00": 0.08153065853913977,
          "2023-12-31 00:00:00+00:00": 0.18055844839345347,
          "2024-12-31 00:00:00+00:00": 0.10708566639654804,
          "2025-12-31 00:00:00+00:00": 0.13858481829400282
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 8239.021935417366,
        "extra_cost": 2025.8340462526114,
        "samefills_cagr_pct": 12.217535700815297,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 36,
          "win_months_all": 0.5714285714285714,
          "win_months_active": 0.5714285714285714,
          "quarters_total": 21,
          "positive_quarters": 15,
          "win_quarters": 0.7142857142857143
        },
        "daily_close_drawdown_pct": -9.73449288274667,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.051040275548047576
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.036984947900670084,
          "2021-12-31 00:00:00+00:00": 0.1424578577437825,
          "2022-12-31 00:00:00+00:00": 0.07440916338315495,
          "2023-12-31 00:00:00+00:00": 0.16291111300470518,
          "2024-12-31 00:00:00+00:00": 0.09630214495669476,
          "2025-12-31 00:00:00+00:00": 0.12393815782053075
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00",
          "2024-08-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 11204.948079683774,
        "mean_month_USDT": 183.68767343743892,
        "median_month_USDT": 64.29760830087434,
        "sum_positive_months": 14367.305795020378,
        "sum_negative_months": -3162.357715336604,
        "worst_month": "2021-04",
        "worst_month_USDT": -531.0084549185412,
        "best3_share_positive_mtm": 0.2496156902070823,
        "class_counts": {
          "loss_base": 22,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 17,
          "zero_months": 0,
          "net_before_actual_fees": 13918.685972624005,
          "fee_total": 2713.7378929402284,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2023-08",
              "gross": 1.1101744269497544,
              "fee": 47.76970647790114,
              "net": -46.659532050951384
            },
            {
              "month": "2024-07",
              "gross": 4.526681413282276,
              "fee": 85.39609264232728,
              "net": -80.869411229045
            },
            {
              "month": "2025-07",
              "gross": 107.8457255737496,
              "fee": 122.08841961794062,
              "net": -14.242694044191012
            },
            {
              "month": "2025-09",
              "gross": 78.82169391065182,
              "fee": 98.12717064191602,
              "net": -19.305476731264207
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 2,
          "PAXG-USDT__SPY-USDT": 2
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 969.19210462151,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.98585561714026,
                "extra": 10.375441500720852,
                "after": -4.3895858835803665
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3162.357715336604,
            "already_negative_after_sum": -3500.852648916678
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 1938.38420924302,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.98585561714026,
                "extra": 20.750883001441704,
                "after": -14.765027384302812
              },
              {
                "month": "2024-08",
                "base": 37.59764118075145,
                "extra": 41.520242978042425,
                "after": -3.922601797290554
              },
              {
                "month": "2025-11",
                "base": 20.582465681342,
                "extra": 20.870553400220828,
                "after": -0.28808771887997864
              }
            ],
            "already_negative_months": 22,
            "already_negative_base_sum": -3162.357715336604,
            "already_negative_after_sum": -3839.3475824967463
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 10264.855981669985,
        "mean_month_USDT": 162.9342219312696,
        "median_month_USDT": 62.02240072301174,
        "sum_positive_months": 14367.305795020378,
        "sum_negative_months": -4102.449813350393,
        "worst_month": "2025-12",
        "worst_month_USDT": -748.865142020979,
        "best3_share_positive_mtm": 0.2496156902070823,
        "class_counts": {
          "loss_base": 24,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 36
        },
        "positive_months": 39,
        "gross_fixed_path": {
          "positive_months": 44,
          "negative_months": 19,
          "zero_months": 0,
          "net_before_actual_fees": 13101.023646423642,
          "fee_total": 2836.1676647536538,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2023-08",
              "gross": 1.1101744269497544,
              "fee": 47.76970647790114,
              "net": -46.659532050951384
            },
            {
              "month": "2024-07",
              "gross": 4.526681413282276,
              "fee": 85.39609264232728,
              "net": -80.869411229045
            },
            {
              "month": "2025-07",
              "gross": 107.8457255737496,
              "fee": 122.08841961794062,
              "net": -14.242694044191012
            },
            {
              "month": "2025-09",
              "gross": 78.82169391065182,
              "fee": 98.12717064191602,
              "net": -19.305476731264207
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 3,
          "PAXG-USDT__SPY-USDT": 3
        },
        "stress": {
          "5": {
            "positive_months": 38,
            "extra_cost": 1012.9170231263047,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.98585561714026,
                "extra": 10.375441500720852,
                "after": -4.3895858835803665
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4102.449813350393,
            "already_negative_after_sum": -4484.669665435265
          },
          "10": {
            "positive_months": 36,
            "extra_cost": 2025.8340462526094,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.98585561714026,
                "extra": 20.750883001441704,
                "after": -14.765027384302812
              },
              {
                "month": "2024-08",
                "base": 37.59764118075145,
                "extra": 41.520242978042425,
                "after": -3.922601797290554
              },
              {
                "month": "2025-11",
                "base": 20.582465681342,
                "extra": 20.870553400220828,
                "after": -0.28808771887997864
              }
            ],
            "already_negative_months": 24,
            "already_negative_base_sum": -4102.449813350393,
            "already_negative_after_sum": -4866.8895175201305
          }
        }
      }
    }
  }
}
```

## [FBS1_C](http://localhost:9200/#/backtest/2fd1c355-c50b-4851-921b-3e6432925b31)

```json
{
  "audit": {
    "n": 280,
    "net": 11327.398215793477,
    "gross_before_fees": 14222.633724943997,
    "fees": 2895.2355091505187,
    "pf_from_trades": 1.7131523794803165,
    "PF_engine": 1.7131523794803158,
    "sharpe_engine": 1.4476220564178297,
    "cagr_engine": 15.635472715307008,
    "dd_engine": -9.073366848682463,
    "plus5_samefills": 10293.385533954006,
    "plus10_samefills": 9259.37285211453,
    "exbest": 9451.567080032417,
    "ex3best": 7204.964255763914,
    "ex3best_plus10_samefills": 5170.544664705815,
    "time_any_position_pct": 40.95700502131138,
    "entry_notional_time_initial_equity": 0.4513959773815755,
    "entry_turnover_initial_equity": 206.59472985092188,
    "two_side_turnover_initial_equity": 413.6050727357884,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4629.604230395661,
        "fees": 218.76654736843489,
        "plus10": 4473.342410846781,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.0531064559938135
      },
      "BTC-USDT:short": {
        "n": 192,
        "net": 3407.830995807233,
        "fees": 1625.4206969415018,
        "plus10": 2246.8162122775884,
        "time_open_pct": 10.848623518421206,
        "entry_notional_time_initial_equity": 0.05823405762117116
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1586.687773464193,
        "fees": 655.5497903722855,
        "plus10": 1118.4379231982753,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.1804418984728868
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1703.2752161263834,
        "fees": 395.4984744682962,
        "plus10": 1420.7763057918862,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.15961356529370418
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 223,
        "net": 8037.435226202897,
        "fees": 1844.1872443099371
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1586.687773464193,
        "fees": 655.5497903722855
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1703.2752161263834,
        "fees": 395.4984744682962
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 12,
        "net": 372.19241733108896,
        "by_symbol": {
          "BTC-USDT": 250.9675097666189,
          "PAXG-USDT": 0,
          "SPY-USDT": 121.22490756447006
        }
      },
      "2021": {
        "n": 53,
        "net": 1831.5698044541034,
        "by_symbol": {
          "BTC-USDT": 1944.281493692324,
          "PAXG-USDT": -253.20878945972424,
          "SPY-USDT": 140.49710022150344
        }
      },
      "2022": {
        "n": 46,
        "net": 1212.127546750994,
        "by_symbol": {
          "BTC-USDT": 1425.4858465464147,
          "PAXG-USDT": -121.7933254541046,
          "SPY-USDT": -91.56497434131595
        }
      },
      "2023": {
        "n": 56,
        "net": 2799.532563021905,
        "by_symbol": {
          "BTC-USDT": 2444.4159763413354,
          "PAXG-USDT": -305.12864266070267,
          "SPY-USDT": 660.2452293412706
        }
      },
      "2024": {
        "n": 56,
        "net": 2300.4363417762484,
        "by_symbol": {
          "BTC-USDT": 785.1871262335046,
          "PAXG-USDT": 1102.870597589963,
          "SPY-USDT": 412.3786179527805
        }
      },
      "2025": {
        "n": 57,
        "net": 2811.5395424591325,
        "by_symbol": {
          "BTC-USDT": 1187.0972736226968,
          "PAXG-USDT": 1163.947933448762,
          "SPY-USDT": 460.49433538767505
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 140,
      "STOP": 113
    },
    "audit": "passed",
    "entry_type_groups": {
      "BTC-USDT:long:LIMIT": {
        "n": 27,
        "net": 3801.5635230674825,
        "fees": 186.18648091678898,
        "gross": 3987.7500039842707,
        "plus10": 3668.5731795554902,
        "exbest": 1925.7323873064404,
        "ex3": 20.810101584502462,
        "ex3_plus10": -93.90168122425601,
        "year_net": {
          "2020": 472.3208559184019,
          "2021": 1528.7938021690584,
          "2022": -177.7837769932911,
          "2023": 1797.2189099726272,
          "2024": 625.40115119403,
          "2025": -444.3874191933438
        }
      },
      "BTC-USDT:long:MARKET": {
        "n": 4,
        "net": 828.0407073281796,
        "fees": 32.58006645164588,
        "gross": 860.6207737798254,
        "plus10": 804.7692312912897,
        "exbest": 185.00076684499913,
        "ex3": -149.3512611624733,
        "ex3_plus10": -157.82059406492377,
        "year_net": {
          "2021": 334.3520280074724,
          "2025": 493.68867932070714
        }
      },
      "BTC-USDT:short:MARKET": {
        "n": 79,
        "net": 2434.6034500918313,
        "fees": 665.2066433505905,
        "gross": 3099.810093442421,
        "plus10": 1959.4558476985515,
        "exbest": 2070.31636012926,
        "ex3": 1444.6680279384275,
        "ex3_plus10": 995.2283700729035,
        "year_net": {
          "2020": -65.83532899199996,
          "2021": 559.5990889746455,
          "2022": 904.8394346538494,
          "2023": 256.98624252437924,
          "2024": 69.62807749785259,
          "2025": 709.3859354331039
        }
      },
      "BTC-USDT:short:STOP": {
        "n": 113,
        "net": 973.2275457154014,
        "fees": 960.2140535909125,
        "gross": 1933.441599306313,
        "plus10": 287.3603645790357,
        "exbest": 777.1256201081467,
        "ex3": 409.2817301792738,
        "ex3_plus10": -233.7609105659136,
        "year_net": {
          "2020": -155.51801715978297,
          "2021": -478.4634254588524,
          "2022": 698.4301888858562,
          "2023": 390.2108238443292,
          "2024": 90.15789754162245,
          "2025": 428.4100780622291
        }
      },
      "PAXG-USDT:long:MARKET": {
        "n": 38,
        "net": 1586.687773464193,
        "fees": 655.5497903722855,
        "gross": 2242.237563836478,
        "plus10": 1118.4379231982753,
        "exbest": 517.2295358535587,
        "ex3": -1137.842685398771,
        "ex3_plus10": -1571.067535535167,
        "year_net": {
          "2021": -253.20878945972424,
          "2022": -121.7933254541046,
          "2023": -305.12864266070267,
          "2024": 1102.870597589963,
          "2025": 1163.947933448762
        }
      },
      "SPY-USDT:long:MARKET": {
        "n": 19,
        "net": 1703.2752161263834,
        "fees": 395.4984744682962,
        "gross": 2098.7736905946795,
        "plus10": 1420.7763057918862,
        "exbest": 913.8951683654449,
        "ex3": -103.56136774119457,
        "ex3_plus10": -339.62368628990816,
        "year_net": {
          "2020": 121.22490756447006,
          "2021": 140.49710022150344,
          "2022": -91.56497434131595,
          "2023": 660.2452293412706,
          "2024": 412.3786179527805,
          "2025": 460.49433538767505
        }
      }
    },
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4848.370777764097,
        "exbest": 2753.7730946346196,
        "ex3best": 848.8508089126824,
        "ex3best_plus10": 710.8675500670336,
        "years": {
          "2020": {
            "n": 3,
            "net": 472.3208559184019,
            "plus10": 464.1181085672969
          },
          "2021": {
            "n": 6,
            "net": 1863.1458301765308,
            "plus10": 1848.3004537379356
          },
          "2022": {
            "n": 4,
            "net": -177.7837769932911,
            "plus10": -188.3715565504845
          },
          "2023": {
            "n": 4,
            "net": 1797.2189099726272,
            "plus10": 1770.7682330437908
          },
          "2024": {
            "n": 8,
            "net": 625.40115119403,
            "plus10": 581.7830787677344
          },
          "2025": {
            "n": 6,
            "net": 49.30126012736329,
            "plus10": -3.2559067194930265
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 5033.251692748738,
        "exbest": 3043.543905844658,
        "ex3best": 2417.8955736538246,
        "ex3best_plus10": 1282.5887346519253,
        "years": {
          "2020": {
            "n": 8,
            "net": -221.35334615178294,
            "plus10": -242.62881617121303
          },
          "2021": {
            "n": 38,
            "net": 81.13566351579303,
            "plus10": -25.942809510309658
          },
          "2022": {
            "n": 37,
            "net": 1603.2696235397057,
            "plus10": 1446.1998549946572
          },
          "2023": {
            "n": 39,
            "net": 647.1970663687088,
            "plus10": 343.50034848739693
          },
          "2024": {
            "n": 37,
            "net": 159.78597503947447,
            "plus10": -74.87313616979779
          },
          "2025": {
            "n": 33,
            "net": 1137.7960134953332,
            "plus10": 800.560770646855
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2242.2375638364797,
        "exbest": 517.2295358535587,
        "ex3best": -1137.842685398771,
        "ex3best_plus10": -1571.067535535167,
        "years": {
          "2021": {
            "n": 6,
            "net": -253.20878945972424,
            "plus10": -294.35614129127646
          },
          "2022": {
            "n": 3,
            "net": -121.7933254541046,
            "plus10": -145.7028639683375
          },
          "2023": {
            "n": 7,
            "net": -305.1286426607027,
            "plus10": -406.07752255529863
          },
          "2024": {
            "n": 7,
            "net": 1102.8705975899627,
            "plus10": 1027.8760432030967
          },
          "2025": {
            "n": 15,
            "net": 1163.947933448762,
            "plus10": 936.6984078100904
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2098.7736905946795,
        "exbest": 913.8951683654449,
        "ex3best": -103.56136774119457,
        "ex3best_plus10": -339.62368628990816,
        "years": {
          "2020": {
            "n": 1,
            "net": 121.22490756447006,
            "plus10": 117.69158375822344
          },
          "2021": {
            "n": 3,
            "net": 140.49710022150344,
            "plus10": 108.17911642993863
          },
          "2022": {
            "n": 2,
            "net": -91.56497434131595,
            "plus10": -104.78081655409424
          },
          "2023": {
            "n": 6,
            "net": 660.2452293412707,
            "plus10": 562.35180696994
          },
          "2024": {
            "n": 4,
            "net": 412.3786179527804,
            "plus10": 340.58486875576614
          },
          "2025": {
            "n": 3,
            "net": 460.49433538767505,
            "plus10": 396.7497464321123
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "FBS1_C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 61,
        "positive_months": 40,
        "win_months_all": 0.6557377049180327,
        "win_months_active": 0.6557377049180327,
        "quarters_total": 19,
        "positive_quarters": 17,
        "win_quarters": 0.8947368421052632
      },
      "months_total": 63,
      "months_active": 63,
      "win_months_all": 0.6349206349206349,
      "win_months_active": 0.6349206349206349,
      "win_quarters": 0.8571428571428571,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.04726016438055314
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.0481752878366144
      ],
      "daily_close_drawdown_pct": -9.131282739617841,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.08399940838599211,
          "SPY-USDT": -0.02645349531324453
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.08399940838599211,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.0266712045291525
        },
        "SPY-USDT": {
          "BTC-USDT": -0.02645349531324453,
          "PAXG-USDT": 0.0266712045291525,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.04066056152449837,
        "2021-12-31 00:00:00+00:00": 0.1726938324545988,
        "2022-12-31 00:00:00+00:00": 0.09932408750042687,
        "2023-12-31 00:00:00+00:00": 0.20867289544876466,
        "2024-12-31 00:00:00+00:00": 0.14186718635747098,
        "2025-12-31 00:00:00+00:00": 0.1518449450312651
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.1124975717284623,
        "SPY-USDT": -0.0430953546355447
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.1124975717284623,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.011351522458866182
      },
      "SPY-USDT": {
        "BTC-USDT": -0.0430953546355447,
        "PAXG-USDT": -0.011351522458866182,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 3
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 3,
        "both_nonzero": 21,
        "both_negative_and_portfolio_negative": 3
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.04726016438055314,
        "contributions": {
          "BTC-USDT": -0.02961117775487074,
          "PAXG-USDT": -0.009069171540947376,
          "SPY-USDT": -0.008579815084734994
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.03193794720537635,
        "contributions": {
          "BTC-USDT": -0.031937947205376245,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.024566454164622775,
        "contributions": {
          "BTC-USDT": -0.02456645416462273,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.017102540274664957,
        "contributions": {
          "BTC-USDT": -0.015338908318119649,
          "PAXG-USDT": -0.009240403211139576,
          "SPY-USDT": 0.007476771254594337
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.016397223762752322,
        "contributions": {
          "BTC-USDT": -0.007335924041824024,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009061299720928328
        }
      },
      {
        "month": "2023-10-31 00:00:00+00:00",
        "portfolio_return": -0.01565707300476804,
        "contributions": {
          "BTC-USDT": -0.006308779235052314,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009348293769715814
        }
      },
      {
        "month": "2022-01-31 00:00:00+00:00",
        "portfolio_return": -0.014679753249945526,
        "contributions": {
          "BTC-USDT": -0.014679753249945617,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.013412124151445881,
        "contributions": {
          "BTC-USDT": -0.013412124151445865,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-05-31 00:00:00+00:00",
        "portfolio_return": -0.010574547975109594,
        "contributions": {
          "BTC-USDT": -0.0010380123160521671,
          "PAXG-USDT": -0.00953653565905755,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.010287707057175077,
        "contributions": {
          "BTC-USDT": -0.010287707057175124,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -9.131282739617841,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -767.8289454562587,
        "PAXG-USDT": -206.24374573108227,
        "SPY-USDT": -97.4680433886634
      }
    },
    "engine_fee_per_side": 0.0007,
    "cost_calendar": {
      "5": {
        "extra_bps_RT": 5,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 10293.385533953999,
        "extra_cost": 1034.0126818394713,
        "samefills_cagr_pct": 14.538459372704015,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 39,
          "win_months_all": 0.6190476190476191,
          "win_months_active": 0.6190476190476191,
          "quarters_total": 21,
          "positive_quarters": 17,
          "win_quarters": 0.8095238095238095
        },
        "daily_close_drawdown_pct": -9.736925282609931,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.04908281043035423
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.03882275471258412,
          "2021-12-31 00:00:00+00:00": 0.16377522573595926,
          "2022-12-31 00:00:00+00:00": 0.09179291154725311,
          "2023-12-31 00:00:00+00:00": 0.19205852658356393,
          "2024-12-31 00:00:00+00:00": 0.1326972834369562,
          "2025-12-31 00:00:00+00:00": 0.13865520741506643
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00"
        ]
      },
      "10": {
        "extra_bps_RT": 10,
        "engine_fee_basis_per_side": 0.0007,
        "samefills_net": 9259.372852114528,
        "extra_cost": 2068.0253636789425,
        "samefills_cagr_pct": 13.395299050138586,
        "complete_periods": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_periods": {
          "months_total": 63,
          "months_active": 63,
          "positive_months": 37,
          "win_months_all": 0.5873015873015873,
          "win_months_active": 0.5873015873015873,
          "quarters_total": 21,
          "positive_quarters": 16,
          "win_quarters": 0.7619047619047619
        },
        "daily_close_drawdown_pct": -10.528901933182711,
        "worst_month": [
          "2021-04-30 00:00:00+00:00",
          -0.05091823331020584
        ],
        "yearly_returns": {
          "2020-12-31 00:00:00+00:00": 0.036984947900670084,
          "2021-12-31 00:00:00+00:00": 0.15482500683970168,
          "2022-12-31 00:00:00+00:00": 0.08411809683561877,
          "2023-12-31 00:00:00+00:00": 0.17488979925340087,
          "2024-12-31 00:00:00+00:00": 0.12294894399816103,
          "2025-12-31 00:00:00+00:00": 0.12439723917200252
        },
        "nearzero_months": {},
        "positive_to_nonpositive_months": [
          "2023-03-31 00:00:00+00:00",
          "2024-08-31 00:00:00+00:00",
          "2025-11-30 00:00:00+00:00"
        ]
      }
    }
  },
  "month_diagnostics": {
    "fee_engine_per_side": 0.0007,
    "notes": "Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.",
    "samples": {
      "full61": {
        "months": 61,
        "net_mtm": 12306.79435876261,
        "mean_month_USDT": 201.7507271928297,
        "median_month_USDT": 104.05528201025481,
        "sum_positive_months": 15789.25431710453,
        "sum_negative_months": -3482.4599583419204,
        "worst_month": "2021-04",
        "worst_month_USDT": -536.8828706570421,
        "best3_share_positive_mtm": 0.25762189677870684,
        "class_counts": {
          "loss_base": 21,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 37
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 18,
          "zero_months": 0,
          "net_before_actual_fees": 15073.726683843866,
          "fee_total": 2766.9323250812563,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2024-07",
              "gross": 4.052229199821582,
              "fee": 87.95232274267734,
              "net": -83.90009354285576
            },
            {
              "month": "2025-07",
              "gross": 114.93165200171006,
              "fee": 127.33522610633099,
              "net": -12.40357410462093
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 4,
          "BTC-USDT__SPY-USDT": 3,
          "PAXG-USDT__SPY-USDT": 2
        },
        "stress": {
          "5": {
            "positive_months": 39,
            "extra_cost": 988.1901161004486,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.634164651539322,
                "extra": 10.678950313087181,
                "after": -5.044785661550122
              }
            ],
            "already_negative_months": 21,
            "already_negative_base_sum": -3482.4599583419204,
            "already_negative_after_sum": -3805.907011064901
          },
          "10": {
            "positive_months": 37,
            "extra_cost": 1976.3802322008971,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.634164651539322,
                "extra": 21.357900626174363,
                "after": -15.723735974635929
              },
              {
                "month": "2024-08",
                "base": 33.0711189512258,
                "extra": 44.182181841808706,
                "after": -11.111062890584435
              },
              {
                "month": "2025-11",
                "base": 21.660753627740633,
                "extra": 21.96505941640535,
                "after": -0.30430578866798896
              }
            ],
            "already_negative_months": 21,
            "already_negative_base_sum": -3482.4599583419204,
            "already_negative_after_sum": -4129.354063787887
          }
        }
      },
      "included63": {
        "months": 63,
        "net_mtm": 11327.398215793459,
        "mean_month_USDT": 179.79997167926126,
        "median_month_USDT": 98.40890194785607,
        "sum_positive_months": 15789.25431710453,
        "sum_negative_months": -4461.856101311072,
        "worst_month": "2025-12",
        "worst_month_USDT": -788.1691869763417,
        "best3_share_positive_mtm": 0.25762189677870684,
        "class_counts": {
          "loss_base": 23,
          "zero_base": 0,
          "positive_within_cost5": 1,
          "positive_between_cost5_cost10": 2,
          "positive_above_cost10": 37
        },
        "positive_months": 40,
        "gross_fixed_path": {
          "positive_months": 43,
          "negative_months": 20,
          "zero_months": 0,
          "net_before_actual_fees": 14222.633724943978,
          "fee_total": 2895.2355091505196,
          "fee_absorbed_positive_months": [
            {
              "month": "2020-11",
              "gross": 16.729229204772615,
              "fee": 21.1282214876804,
              "net": -4.398992282907784
            },
            {
              "month": "2024-07",
              "gross": 4.052229199821582,
              "fee": 87.95232274267734,
              "net": -83.90009354285576
            },
            {
              "month": "2025-07",
              "gross": 114.93165200171006,
              "fee": 127.33522610633099,
              "net": -12.40357410462093
            }
          ]
        },
        "co_loss_counts": {
          "BTC-USDT__PAXG-USDT": 5,
          "BTC-USDT__SPY-USDT": 4,
          "PAXG-USDT__SPY-USDT": 3
        },
        "stress": {
          "5": {
            "positive_months": 39,
            "extra_cost": 1034.0126818394713,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.634164651539322,
                "extra": 10.678950313087181,
                "after": -5.044785661550122
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -4461.856101311072,
            "already_negative_after_sum": -4831.12571977307
          },
          "10": {
            "positive_months": 37,
            "extra_cost": 2068.0253636789425,
            "flip_months": [
              {
                "month": "2023-03",
                "base": 5.634164651539322,
                "extra": 21.357900626174363,
                "after": -15.723735974635929
              },
              {
                "month": "2024-08",
                "base": 33.0711189512258,
                "extra": 44.182181841808706,
                "after": -11.111062890584435
              },
              {
                "month": "2025-11",
                "base": 21.660753627740633,
                "extra": 21.96505941640535,
                "after": -0.30430578866798896
              }
            ],
            "already_negative_months": 23,
            "already_negative_base_sum": -4461.856101311072,
            "already_negative_after_sum": -5200.395338235079
          }
        }
      }
    }
  }
}
```

## Comparaciones por mes
```json
{
  "X03S_C__N204S_C": {
    "delta": 988.0682713267415,
    "months_improve": 38,
    "rescued_negative_to_positive": [
      "2022-06",
      "2023-08",
      "2025-09"
    ],
    "lost_positive_to_nonpositive": [
      "2022-08",
      "2025-04"
    ]
  }
}
```