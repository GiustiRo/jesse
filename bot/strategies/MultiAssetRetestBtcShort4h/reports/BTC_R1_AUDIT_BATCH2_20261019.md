# BTC R1 exact audit batch2

Job 831bac3de3cb4ff1953bd28756787b33, all six passed executed-fill + UTC daily MTM reconciliation, source scale anchors and terminal close. Full/partial denominators, static samefillcost5/10bps, concentration, perroute/co-loss included. No numerical nonzero month under1e-10 returns. Calendar MTM distinct from exit-year cohorts. Capital/sizing/occupancy endogenous; open-key matching is descriptive.

```json
{
  "E02B": {
    "n": 143,
    "net": 7157.307308850564,
    "gross_before_fees": 8093.779269389333,
    "fees": 936.4719605387694,
    "pf_from_trades": 1.8876667513564933,
    "PF_engine": 1.887666751356493,
    "sharpe_engine": 1.1648884268061535,
    "cagr_engine": 10.909286108252282,
    "dd_engine": -9.465609183787848,
    "plus5_samefills": 6637.045108551244,
    "plus10_samefills": 6116.782908251926,
    "exbest": 5409.008366704466,
    "ex3best": 3460.2591384105394,
    "ex3best_plus10_samefills": 2449.6441134161523,
    "time_any_position_pct": 32.460953465288725,
    "entry_notional_time_initial_equity": 0.31810476474759725,
    "entry_turnover_initial_equity": 103.6427781098937,
    "two_side_turnover_initial_equity": 208.1048801197264,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4538.510664720511,
        "fees": 124.48801816329771,
        "plus10": 4400.190644539067,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04727327137972208
      },
      "BTC-USDT:short": {
        "n": 62,
        "net": -344.98094046422193,
        "fees": 295.2510754631738,
        "plus10": -673.0376909788591,
        "time_open_pct": 2.705340982075086,
        "entry_notional_time_initial_equity": 0.012309535964372864
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1450.2741589333182,
        "fees": 371.90323620141055,
        "plus10": 1037.0483409317508,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.16016804916950314
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1513.5034256609547,
        "fees": 144.82963071088733,
        "plus10": 1352.581613759969,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.09835390823399913
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 93,
        "net": 4193.529724256291,
        "fees": 419.73909362647146
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1450.2741589333182,
        "fees": 371.90323620141055
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1513.5034256609547,
        "fees": 144.82963071088733
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 7,
        "net": 522.8939496617608,
        "by_symbol": {
          "BTC-USDT": 387.5478372823134,
          "PAXG-USDT": 0,
          "SPY-USDT": 135.3461123794473
        }
      },
      "2021": {
        "n": 32,
        "net": 1324.5876055883855,
        "by_symbol": {
          "BTC-USDT": 1204.7414342875168,
          "PAXG-USDT": -249.68343360792596,
          "SPY-USDT": 369.5296049087948
        }
      },
      "2022": {
        "n": 15,
        "net": 156.38647509668345,
        "by_symbol": {
          "BTC-USDT": 378.8948387179514,
          "PAXG-USDT": -109.09938522689052,
          "SPY-USDT": -113.40897839437748
        }
      },
      "2023": {
        "n": 27,
        "net": 848.3763462361028,
        "by_symbol": {
          "BTC-USDT": 914.0538757792204,
          "PAXG-USDT": -218.6495943007352,
          "SPY-USDT": 152.97206475761794
        }
      },
      "2024": {
        "n": 31,
        "net": 2651.4595665749357,
        "by_symbol": {
          "BTC-USDT": 1251.0208749984222,
          "PAXG-USDT": 944.9020922776812,
          "SPY-USDT": 455.5365992988323
        }
      },
      "2025": {
        "n": 31,
        "net": 1653.6033656926934,
        "by_symbol": {
          "BTC-USDT": 57.27086319086422,
          "PAXG-USDT": 1082.8044797911891,
          "SPY-USDT": 513.5280227106399
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 45,
      "STOP": 62
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4662.998682883808,
        "exbest": 2790.211722574416,
        "ex3best": 1043.0575088599044,
        "ex3best_plus10": 921.5147819383594,
        "years": {
          "2020": {
            "n": 3,
            "net": 493.93286905120976,
            "plus10": 485.50589647902666
          },
          "2021": {
            "n": 6,
            "net": 1925.8415240769846,
            "plus10": 1910.5013434936839
          },
          "2022": {
            "n": 4,
            "net": -164.55379210108538,
            "plus10": -174.82928517691897
          },
          "2023": {
            "n": 4,
            "net": 1686.750970737484,
            "plus10": 1663.2835865292218
          },
          "2024": {
            "n": 8,
            "net": 549.6286324225418,
            "plus10": 512.7239035783507
          },
          "2025": {
            "n": 6,
            "net": 46.9104605333751,
            "plus10": 3.0051996357043436
          }
        }
      },
      "BTC-USDT:short": {
        "gross": -49.72986500104952,
        "exbest": -515.8823863979461,
        "ex3best": -817.8081919802904,
        "ex3best_plus10": -1113.4510795524504,
        "years": {
          "2020": {
            "n": 3,
            "net": -106.38503176889635,
            "plus10": -113.57468505823947
          },
          "2021": {
            "n": 19,
            "net": -721.1000897894676,
            "plus10": -778.3206577730359
          },
          "2022": {
            "n": 7,
            "net": 543.4486308190369,
            "plus10": 513.7553503126433
          },
          "2023": {
            "n": 12,
            "net": -772.6970949582642,
            "plus10": -852.2611373847934
          },
          "2024": {
            "n": 13,
            "net": 701.3922425758805,
            "plus10": 633.4576344869789
          },
          "2025": {
            "n": 8,
            "net": 10.360402657489175,
            "plus10": -76.09419556241306
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1822.1773951347295,
        "exbest": 504.29822279868563,
        "ex3best": -850.9029686560153,
        "ex3best_plus10": -1234.5213226349779,
        "years": {
          "2021": {
            "n": 6,
            "net": -249.68343360792596,
            "plus10": -293.22432666299676
          },
          "2022": {
            "n": 3,
            "net": -109.0993852268905,
            "plus10": -133.26291152110946
          },
          "2023": {
            "n": 7,
            "net": -218.6495943007352,
            "plus10": -309.7753620990941
          },
          "2024": {
            "n": 7,
            "net": 944.9020922776814,
            "plus10": 880.3027705367589
          },
          "2025": {
            "n": 15,
            "net": 1082.804479791189,
            "plus10": 893.0081706781921
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1658.3330563718423,
        "exbest": 847.6332956504232,
        "ex3best": 209.8209615136894,
        "ex3best_plus10": 89.77982051758451,
        "years": {
          "2020": {
            "n": 1,
            "net": 135.3461123794473,
            "plus10": 131.71822567424024
          },
          "2021": {
            "n": 1,
            "net": 369.5296049087948,
            "plus10": 359.1271229625646
          },
          "2022": {
            "n": 1,
            "net": -113.40897839437748,
            "plus10": -119.67744416427675
          },
          "2023": {
            "n": 4,
            "net": 152.97206475761794,
            "plus10": 94.66349804821996
          },
          "2024": {
            "n": 3,
            "net": 455.5365992988323,
            "plus10": 404.89222982972177
          },
          "2025": {
            "n": 2,
            "net": 513.5280227106399,
            "plus10": 481.8579814094991
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "E02B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 54,
        "positive_months": 30,
        "win_months_all": 0.4918032786885246,
        "win_months_active": 0.5555555555555556,
        "quarters_total": 19,
        "positive_quarters": 14,
        "win_quarters": 0.7368421052631579
      },
      "months_total": 63,
      "months_active": 56,
      "win_months_all": 0.47619047619047616,
      "win_months_active": 0.5357142857142857,
      "win_quarters": 0.7142857142857143,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.05408334836351825
      ],
      "worst_quarter": [
        "2023-09-30 00:00:00+00:00",
        -0.025556058607349552
      ],
      "daily_close_drawdown_pct": -9.43158146523504,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07028057575463514,
          "SPY-USDT": 0.04208768473282993
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07028057575463514,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03533343065376826
        },
        "SPY-USDT": {
          "BTC-USDT": 0.04208768473282993,
          "PAXG-USDT": -0.03533343065376826,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05602854510067545,
        "2021-12-31 00:00:00+00:00": 0.12189027561946042,
        "2022-12-31 00:00:00+00:00": 0.013199976245363398,
        "2023-12-31 00:00:00+00:00": 0.07067524768610678,
        "2024-12-31 00:00:00+00:00": 0.20630323302955178,
        "2025-12-31 00:00:00+00:00": 0.1066586005354202
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.08315323111274023,
        "SPY-USDT": 0.03703578134777494
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.08315323111274023,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.046796293394259995
      },
      "SPY-USDT": {
        "BTC-USDT": 0.03703578134777494,
        "PAXG-USDT": -0.046796293394259995,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 24,
        "both_negative_and_portfolio_negative": 4
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 13,
        "both_negative_and_portfolio_negative": 0
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.05408334836351825,
        "contributions": {
          "BTC-USDT": -0.05408334836351829,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-02-28 00:00:00+00:00",
        "portfolio_return": -0.01900700599315741,
        "contributions": {
          "BTC-USDT": -0.019007005993157494,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.01711132318922548,
        "contributions": {
          "BTC-USDT": -0.007995734747569247,
          "PAXG-USDT": -0.009115588441656155,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.016770925067536968,
        "contributions": {
          "BTC-USDT": -0.016770925067537006,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.014182595420633715,
        "contributions": {
          "BTC-USDT": -0.014182595420633813,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01396265478298786,
        "contributions": {
          "BTC-USDT": -0.014077602455942391,
          "PAXG-USDT": -0.008662938599501372,
          "SPY-USDT": 0.00877788627245582
        }
      },
      {
        "month": "2021-11-30 00:00:00+00:00",
        "portfolio_return": -0.012306637512844443,
        "contributions": {
          "BTC-USDT": -0.027972432680109103,
          "PAXG-USDT": 0.007976116935655758,
          "SPY-USDT": 0.007689678231609053
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.011757570725488331,
        "contributions": {
          "BTC-USDT": -0.002819509260482512,
          "PAXG-USDT": -0.008938061465005845,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-11-30 00:00:00+00:00",
        "portfolio_return": -0.010474256582641894,
        "contributions": {
          "BTC-USDT": -0.010474256582641882,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.010432616455452681,
        "contributions": {
          "BTC-USDT": -0.0011069846339882962,
          "PAXG-USDT": -0.00932563182146438,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2023-01-16 00:00:00+00:00",
      "trough": "2024-03-05 00:00:00+00:00",
      "drawdown_pct": -9.43158146523504,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1299.6284430769365,
        "PAXG-USDT": -286.00702788110823,
        "SPY-USDT": 254.41293776895083
      }
    }
  },
  "E02C": {
    "n": 150,
    "net": 7323.182129765532,
    "gross_before_fees": 8344.92353611942,
    "fees": 1021.7414063538889,
    "pf_from_trades": 1.8587212455218867,
    "PF_engine": 1.8587212455218869,
    "sharpe_engine": 1.1592343806170988,
    "cagr_engine": 11.114148937352608,
    "dd_engine": -9.15032338845,
    "plus5_samefills": 6755.548015124483,
    "plus10_samefills": 6187.913900483433,
    "exbest": 5604.075563276804,
    "ex3best": 3620.313179765033,
    "ex3best_plus10_samefills": 2515.1207202543333,
    "time_any_position_pct": 35.03627313598412,
    "entry_notional_time_initial_equity": 0.3632971763125104,
    "entry_turnover_initial_equity": 113.10849139667577,
    "two_side_turnover_initial_equity": 227.05364585641976,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4498.778833660977,
        "fees": 125.06540023525329,
        "plus10": 4359.817277844029,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04732013336537156
      },
      "BTC-USDT:short": {
        "n": 62,
        "net": -306.1631290486939,
        "fees": 295.30958176763863,
        "plus10": -634.2848865682924,
        "time_open_pct": 2.705340982075086,
        "entry_notional_time_initial_equity": 0.012280837239939335
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1498.28426917441,
        "fees": 372.95280408836817,
        "plus10": 1083.8922646317787,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.16115329407298196
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1632.2821559788388,
        "fees": 228.41362026262863,
        "plus10": 1378.4892445759183,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.1425429116342176
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 93,
        "net": 4192.615704612284,
        "fees": 420.3749820028919
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1498.28426917441,
        "fees": 372.95280408836817
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1632.2821559788388,
        "fees": 228.41362026262863
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 7,
        "net": 513.9610424524269,
        "by_symbol": {
          "BTC-USDT": 387.5478372823134,
          "PAXG-USDT": 0,
          "SPY-USDT": 126.41320517011347
        }
      },
      "2021": {
        "n": 34,
        "net": 1106.4752585165782,
        "by_symbol": {
          "BTC-USDT": 1195.1757648705684,
          "PAXG-USDT": -246.03915542232176,
          "SPY-USDT": 157.33864906833168
        }
      },
      "2022": {
        "n": 16,
        "net": 188.9557265594362,
        "by_symbol": {
          "BTC-USDT": 374.3128776927748,
          "PAXG-USDT": -106.68158189869797,
          "SPY-USDT": -78.67556923464063
        }
      },
      "2023": {
        "n": 29,
        "net": 1309.8216945683096,
        "by_symbol": {
          "BTC-USDT": 900.5396755392304,
          "PAXG-USDT": -213.2804178635277,
          "SPY-USDT": 622.5624368926067
        }
      },
      "2024": {
        "n": 32,
        "net": 2636.1255258845767,
        "by_symbol": {
          "BTC-USDT": 1277.718122202305,
          "PAXG-USDT": 963.7927522678709,
          "SPY-USDT": 394.6146514144018
        }
      },
      "2025": {
        "n": 32,
        "net": 1567.8428817842043,
        "by_symbol": {
          "BTC-USDT": 57.32142702509283,
          "PAXG-USDT": 1100.4926720910862,
          "SPY-USDT": 410.0287826680258
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 61,
      "STOP": 62
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4623.844233896234,
        "exbest": 2779.6722671722396,
        "ex3best": 1012.8558320428411,
        "ex3best_plus10": 890.5885571531196,
        "years": {
          "2020": {
            "n": 3,
            "net": 493.93286905120976,
            "plus10": 485.50589647902666
          },
          "2021": {
            "n": 6,
            "net": 1901.767811050851,
            "plus10": 1886.619124436349
          },
          "2022": {
            "n": 4,
            "net": -162.23305282497606,
            "plus10": -172.37437189214378
          },
          "2023": {
            "n": 4,
            "net": 1658.7862692231656,
            "plus10": 1635.8115937846067
          },
          "2024": {
            "n": 8,
            "net": 561.6971170182348,
            "plus10": 524.0822501696441
          },
          "2025": {
            "n": 6,
            "net": 44.82782014249338,
            "plus10": 0.1727848665479712
          }
        }
      },
      "BTC-USDT:short": {
        "gross": -10.853547281055967,
        "exbest": -480.8907267570525,
        "ex3best": -790.5116706898602,
        "ex3best_plus10": -1085.4617229169237,
        "years": {
          "2020": {
            "n": 3,
            "net": -106.38503176889635,
            "plus10": -113.57468505823947
          },
          "2021": {
            "n": 19,
            "net": -706.5920461802825,
            "plus10": -763.0560597011117
          },
          "2022": {
            "n": 7,
            "net": 536.5459305177509,
            "plus10": 507.30435701425574
          },
          "2023": {
            "n": 12,
            "net": -758.2465936839354,
            "plus10": -836.1860985926751
          },
          "2024": {
            "n": 13,
            "net": 716.0210051840702,
            "plus10": 646.6137026927742
          },
          "2025": {
            "n": 8,
            "net": 12.493606882599408,
            "plus10": -75.38610292329588
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1871.2370732627778,
        "exbest": 536.9573992368263,
        "ex3best": -843.8395339224921,
        "ex3best_plus10": -1228.1125537204398,
        "years": {
          "2021": {
            "n": 6,
            "net": -246.03915542232178,
            "plus10": -288.9506936428098
          },
          "2022": {
            "n": 3,
            "net": -106.68158189869796,
            "plus10": -130.41476033804634
          },
          "2023": {
            "n": 7,
            "net": -213.28041786352773,
            "plus10": -302.43017864694855
          },
          "2024": {
            "n": 7,
            "net": 963.792752267871,
            "plus10": 898.031154172594
          },
          "2025": {
            "n": 15,
            "net": 1100.4926720910858,
            "plus10": 907.6567430869885
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1860.6957762414672,
        "exbest": 958.9193962189305,
        "ex3best": 7.310128521126472,
        "ex3best_plus10": -205.02445784980117,
        "years": {
          "2020": {
            "n": 1,
            "net": 126.41320517011347,
            "plus10": 122.78158400140249
          },
          "2021": {
            "n": 3,
            "net": 157.33864906833168,
            "plus10": 122.96625090422364
          },
          "2022": {
            "n": 2,
            "net": -78.67556923464063,
            "plus10": -91.35922833601893
          },
          "2023": {
            "n": 6,
            "net": 622.5624368926067,
            "plus10": 537.8591929910046
          },
          "2024": {
            "n": 4,
            "net": 394.6146514144018,
            "plus10": 330.65922289215956
          },
          "2025": {
            "n": 3,
            "net": 410.0287826680259,
            "plus10": 355.58222212314666
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "E02C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 54,
        "positive_months": 31,
        "win_months_all": 0.5081967213114754,
        "win_months_active": 0.5740740740740741,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 56,
      "win_months_all": 0.49206349206349204,
      "win_months_active": 0.5535714285714286,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.05413792132570083
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.028265045136022238
      ],
      "daily_close_drawdown_pct": -9.116166981312546,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07052395585958468,
          "SPY-USDT": -0.04031583318259282
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07052395585958468,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.02193727724937116
        },
        "SPY-USDT": {
          "BTC-USDT": -0.04031583318259282,
          "PAXG-USDT": 0.02193727724937116,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.055133589487811996,
        "2021-12-31 00:00:00+00:00": 0.10132370125851575,
        "2022-12-31 00:00:00+00:00": 0.016260639589210424,
        "2023-12-31 00:00:00+00:00": 0.1109135585909109,
        "2024-12-31 00:00:00+00:00": 0.20093624372050112,
        "2025-12-31 00:00:00+00:00": 0.09951184529302304
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
        "PAXG-USDT": -0.08340951581918432,
        "SPY-USDT": -0.04905344798703471
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.08340951581918432,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.013470029249648425
      },
      "SPY-USDT": {
        "BTC-USDT": -0.04905344798703471,
        "PAXG-USDT": -0.013470029249648425,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 24,
        "both_negative_and_portfolio_negative": 4
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 20,
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
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.05413792132570083,
        "contributions": {
          "BTC-USDT": -0.0541379213257009,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-02-28 00:00:00+00:00",
        "portfolio_return": -0.019018468274035194,
        "contributions": {
          "BTC-USDT": -0.01901846827403528,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.018919836717446348,
        "contributions": {
          "BTC-USDT": -0.0009227088903605878,
          "PAXG-USDT": -0.00932145355496028,
          "SPY-USDT": -0.008675674272125572
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017072595153634684,
        "contributions": {
          "BTC-USDT": -0.007957042516789236,
          "PAXG-USDT": -0.009115552636845332,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.016927444781997147,
        "contributions": {
          "BTC-USDT": -0.0169274447819972,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.014196491849851944,
        "contributions": {
          "BTC-USDT": -0.01419649184985188,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.014191671674381956,
        "contributions": {
          "BTC-USDT": -0.014071033568376945,
          "PAXG-USDT": -0.008662915596759269,
          "SPY-USDT": 0.008542277490754297
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.013223809781700568,
        "contributions": {
          "BTC-USDT": -0.004208480544019998,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009015329237680402
        }
      },
      {
        "month": "2021-11-30 00:00:00+00:00",
        "portfolio_return": -0.012311445392877984,
        "contributions": {
          "BTC-USDT": -0.02799163072930383,
          "PAXG-USDT": 0.007984385293263884,
          "SPY-USDT": 0.007695800043162105
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.011761731332642578,
        "contributions": {
          "BTC-USDT": -0.002823598272270587,
          "PAXG-USDT": -0.008938133060371958,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2023-01-16 00:00:00+00:00",
      "trough": "2023-11-07 00:00:00+00:00",
      "drawdown_pct": -9.116166981312546,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1097.746290256322,
        "PAXG-USDT": -305.1717816562916,
        "SPY-USDT": 137.1602553569332
      }
    }
  },
  "P02B": {
    "n": 207,
    "net": 8658.485109663763,
    "gross_before_fees": 9992.813176188765,
    "fees": 1334.3280665250022,
    "pf_from_trades": 1.7603378585480411,
    "PF_engine": 1.760337858548042,
    "sharpe_engine": 1.2683015465144638,
    "cagr_engine": 12.708000312003609,
    "dd_engine": -7.868585143766871,
    "plus5_samefills": 7917.191739372086,
    "plus10_samefills": 7175.898369080417,
    "exbest": 6884.237389155565,
    "ex3best": 4793.068655923747,
    "ex3best_plus10_samefills": 3341.923022365445,
    "time_any_position_pct": 34.274026391078415,
    "entry_notional_time_initial_equity": 0.35347482682455195,
    "entry_turnover_initial_equity": 147.9066522625462,
    "two_side_turnover_initial_equity": 296.517348116667,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4608.397976473709,
        "fees": 131.47114699956296,
        "plus10": 4462.318924251971,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04985187969317926
      },
      "BTC-USDT:short": {
        "n": 126,
        "net": 826.6288294241476,
        "fees": 649.5598007975263,
        "plus10": 104.89571742689569,
        "time_open_pct": 5.319196298242541,
        "entry_notional_time_initial_equity": 0.027750970585384952
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1613.4332804337812,
        "fees": 396.562709939568,
        "plus10": 1172.8080471675944,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17019835771603034
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1610.0250233321167,
        "fees": 156.7344087883442,
        "plus10": 1435.8756802339565,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10567361882995749
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 157,
        "net": 5435.026805897859,
        "fees": 781.0309477970897
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1613.4332804337812,
        "fees": 396.562709939568
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1610.0250233321167,
        "fees": 156.7344087883442
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 11,
        "net": 475.812630198268,
        "by_symbol": {
          "BTC-USDT": 341.763166994209,
          "PAXG-USDT": 0,
          "SPY-USDT": 134.04946320405904
        }
      },
      "2021": {
        "n": 44,
        "net": 1475.4915179331852,
        "by_symbol": {
          "BTC-USDT": 1354.2714828150533,
          "PAXG-USDT": -245.30209203305716,
          "SPY-USDT": 366.52212715118935
        }
      },
      "2022": {
        "n": 24,
        "net": 217.92091980259806,
        "by_symbol": {
          "BTC-USDT": 444.525100209163,
          "PAXG-USDT": -112.24599237753796,
          "SPY-USDT": -114.35818802902702
        }
      },
      "2023": {
        "n": 39,
        "net": 2092.275562640112,
        "by_symbol": {
          "BTC-USDT": 2171.8697714027808,
          "PAXG-USDT": -237.84256456759957,
          "SPY-USDT": 158.24835580493138
        }
      },
      "2024": {
        "n": 46,
        "net": 2287.1878175156003,
        "by_symbol": {
          "BTC-USDT": 743.8361194699144,
          "PAXG-USDT": 1046.6670377583864,
          "SPY-USDT": 496.6846602872994
        }
      },
      "2025": {
        "n": 43,
        "net": 2109.7966615739897,
        "by_symbol": {
          "BTC-USDT": 378.76116500673606,
          "PAXG-USDT": 1162.1568916535896,
          "SPY-USDT": 568.8786049136644
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 45,
      "STOP": 126
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4739.869123473271,
        "exbest": 2834.1502559655196,
        "ex3best": 1008.3471565914555,
        "ex3best_plus10": 879.541048304432,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1912.4471566233851,
            "plus10": 1897.2255098440228
          },
          "2022": {
            "n": 4,
            "net": -161.7688874750096,
            "plus10": -172.04543747877378
          },
          "2023": {
            "n": 4,
            "net": 1710.9297584045853,
            "plus10": 1686.3138496664506
          },
          "2024": {
            "n": 8,
            "net": 595.3746946128269,
            "plus10": 555.539008806908
          },
          "2025": {
            "n": 6,
            "net": 61.25015028333112,
            "plus10": 13.496920154631539
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1476.1886302216733,
        "exbest": 639.1473924670024,
        "ex3best": 285.25432254627935,
        "ex3best_plus10": -396.9564425590946,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 31,
            "net": -558.175673808332,
            "plus10": -654.5725786860158
          },
          "2022": {
            "n": 16,
            "net": 606.2939876841725,
            "plus10": 538.3302831070829
          },
          "2023": {
            "n": 24,
            "net": 460.9400129981957,
            "plus10": 290.1595278728874
          },
          "2024": {
            "n": 28,
            "net": 148.4614248570873,
            "plus10": -21.985659207754566
          },
          "2025": {
            "n": 20,
            "net": 317.51101472340497,
            "plus10": 121.60705976717017
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2009.9959903733518,
        "exbest": 603.6867250208151,
        "ex3best": -897.5599448786724,
        "ex3best_plus10": -1306.0247133230332,
        "years": {
          "2021": {
            "n": 6,
            "net": -245.3020920330572,
            "plus10": -288.53860795220425
          },
          "2022": {
            "n": 3,
            "net": -112.24599237753796,
            "plus10": -136.4181943722468
          },
          "2023": {
            "n": 7,
            "net": -237.8425645675996,
            "plus10": -334.4138393589719
          },
          "2024": {
            "n": 7,
            "net": 1046.6670377583864,
            "plus10": 976.8207946300997
          },
          "2025": {
            "n": 15,
            "net": 1162.1568916535894,
            "plus10": 955.3578942209174
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1766.7594321204601,
        "exbest": 872.369264045702,
        "ex3best": 216.66012522277356,
        "ex3best_plus10": 86.17556263859933,
        "years": {
          "2020": {
            "n": 1,
            "net": 134.04946320405904,
            "plus10": 130.45633254926236
          },
          "2021": {
            "n": 1,
            "net": 366.52212715118935,
            "plus10": 356.20430752338126
          },
          "2022": {
            "n": 1,
            "net": -114.35818802902702,
            "plus10": -120.6791195577004
          },
          "2023": {
            "n": 4,
            "net": 158.2483558049314,
            "plus10": 94.49507595109472
          },
          "2024": {
            "n": 3,
            "net": 496.68466028729944,
            "plus10": 441.6059197882312
          },
          "2025": {
            "n": 2,
            "net": 568.8786049136644,
            "plus10": 533.7931639796873
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "P02B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 37,
        "win_months_all": 0.6065573770491803,
        "win_months_active": 0.6491228070175439,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.5873015873015873,
      "win_months_active": 0.6271186440677966,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.0628228018654795
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.029776450954076328
      ],
      "daily_close_drawdown_pct": -7.896245318088457,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07182243776443935,
          "SPY-USDT": -0.05383199486396178
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07182243776443935,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03545811983945462
        },
        "SPY-USDT": {
          "BTC-USDT": -0.05383199486396178,
          "PAXG-USDT": -0.03545811983945462,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.051311512385931124,
        "2021-12-31 00:00:00+00:00": 0.13679951254487843,
        "2022-12-31 00:00:00+00:00": 0.01823407028233559,
        "2023-12-31 00:00:00+00:00": 0.1719317007418386,
        "2024-12-31 00:00:00+00:00": 0.1603749757309738,
        "2025-12-31 00:00:00+00:00": 0.12749026414945397
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.08596415383482378,
        "SPY-USDT": -0.0598984536057939
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.08596415383482378,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.04688005900263368
      },
      "SPY-USDT": {
        "BTC-USDT": -0.0598984536057939,
        "PAXG-USDT": -0.04688005900263368,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 4,
        "both_nonzero": 29,
        "both_negative_and_portfolio_negative": 4
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 14,
        "both_negative_and_portfolio_negative": 0
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.0628228018654795,
        "contributions": {
          "BTC-USDT": -0.06282280186547948,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.03848725917031115,
        "contributions": {
          "BTC-USDT": -0.02942600672212941,
          "PAXG-USDT": -0.009061252448181649,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017134261171070975,
        "contributions": {
          "BTC-USDT": -0.00801867366439825,
          "PAXG-USDT": -0.009115587506672811,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01395377087827343,
        "contributions": {
          "BTC-USDT": -0.01406864636378658,
          "PAXG-USDT": -0.008662991569721992,
          "SPY-USDT": 0.008777867055235193
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009877648608705214,
        "contributions": {
          "BTC-USDT": -0.00987764860870508,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.00919324475482064,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.00919324475482059,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.009067798770316493,
        "contributions": {
          "BTC-USDT": -0.009067798770316476,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.006854129712003831,
        "contributions": {
          "BTC-USDT": 0.0026422580637868853,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.00949638777579085
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006208455516382827,
        "contributions": {
          "BTC-USDT": 0.003203394292836037,
          "PAXG-USDT": -0.00941184980921881,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.005739701648066919,
        "contributions": {
          "BTC-USDT": -0.005739701648066918,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-10-02 00:00:00+00:00",
      "drawdown_pct": -7.896245318088457,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -601.3711949831527,
        "PAXG-USDT": -341.17669449534986,
        "SPY-USDT": 0
      }
    }
  },
  "P02C": {
    "n": 214,
    "net": 8829.618167865412,
    "gross_before_fees": 10253.868817872544,
    "fees": 1424.2506500071327,
    "pf_from_trades": 1.7421797165779118,
    "PF_engine": 1.7421797165779114,
    "sharpe_engine": 1.261578306917611,
    "cagr_engine": 12.90554374342172,
    "dd_engine": -8.717095860718715,
    "plus5_samefills": 8038.367806750336,
    "plus10_samefills": 7247.117445635259,
    "exbest": 7084.562823014586,
    "ex3best": 4957.6370567154445,
    "ex3best_plus10_samefills": 3406.7559214550124,
    "time_any_position_pct": 36.74008874875927,
    "entry_notional_time_initial_equity": 0.4023249216194893,
    "entry_turnover_initial_equity": 157.88327120996163,
    "two_side_turnover_initial_equity": 316.5001444460295,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4582.580071632149,
        "fees": 131.92477021883295,
        "plus10": 4435.996993611224,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04987396554269392
      },
      "BTC-USDT:short": {
        "n": 126,
        "net": 809.2592722570896,
        "fees": 649.665006148092,
        "plus10": 87.40926542587607,
        "time_open_pct": 5.319196298242541,
        "entry_notional_time_initial_equity": 0.027764069334471786
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1665.0417931046056,
        "fees": 397.7951834819641,
        "plus10": 1223.0471447913128,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17131547858546883
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1772.7370308715672,
        "fees": 244.86569015824344,
        "plus10": 1500.6640418068528,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.15337140815685507
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 157,
        "net": 5391.839343889236,
        "fees": 781.5897763669251
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1665.0417931046056,
        "fees": 397.7951834819641
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1772.7370308715672,
        "fees": 244.86569015824344
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 11,
        "net": 466.96506317474416,
        "by_symbol": {
          "BTC-USDT": 341.763166994209,
          "PAXG-USDT": 0,
          "SPY-USDT": 125.20189618053519
        }
      },
      "2021": {
        "n": 46,
        "net": 1262.2635509422057,
        "by_symbol": {
          "BTC-USDT": 1348.094990723558,
          "PAXG-USDT": -241.5085859243946,
          "SPY-USDT": 155.67714614304214
        }
      },
      "2022": {
        "n": 25,
        "net": 248.5804979068578,
        "by_symbol": {
          "BTC-USDT": 437.78161656031693,
          "PAXG-USDT": -109.83878948232277,
          "SPY-USDT": -79.3623291711364
        }
      },
      "2023": {
        "n": 41,
        "net": 2581.3471331747087,
        "by_symbol": {
          "BTC-USDT": 2130.153408558134,
          "PAXG-USDT": -232.12234533603143,
          "SPY-USDT": 683.3160699526065
        }
      },
      "2024": {
        "n": 47,
        "net": 2253.2635470987207,
        "by_symbol": {
          "BTC-USDT": 754.0651042039551,
          "PAXG-USDT": 1067.6620386486238,
          "SPY-USDT": 431.53640424614144
        }
      },
      "2025": {
        "n": 44,
        "net": 2017.1983755681729,
        "by_symbol": {
          "BTC-USDT": 379.98105684906443,
          "PAXG-USDT": 1180.8494751987307,
          "SPY-USDT": 456.36784352037836
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 61,
      "STOP": 126
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4714.50484185098,
        "exbest": 2837.5247267813133,
        "ex3best": 992.0594059923642,
        "ex3best_plus10": 862.6662595734795,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1901.767811050851,
            "plus10": 1886.619124436349
          },
          "2022": {
            "n": 4,
            "net": -158.8851945784798,
            "plus10": -168.93843794070355
          },
          "2023": {
            "n": 4,
            "net": 1682.7168544333476,
            "plus10": 1658.620865811251
          },
          "2024": {
            "n": 8,
            "net": 605.6812997644854,
            "plus10": 565.1598270518825
          },
          "2025": {
            "n": 6,
            "net": 61.134196937354375,
            "plus10": 12.746540993710937
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1458.9242784051823,
        "exbest": 619.2270674501872,
        "ex3best": 259.3330000676935,
        "ex3best_plus10": -422.37948184924085,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 31,
            "net": -553.6728203272926,
            "plus10": -648.5953129867897
          },
          "2022": {
            "n": 16,
            "net": 596.6668111387968,
            "plus10": 529.9080669964364
          },
          "2023": {
            "n": 24,
            "net": 447.4365541247859,
            "plus10": 279.67778175797537
          },
          "2024": {
            "n": 28,
            "net": 148.38380443946966,
            "plus10": -24.91681302224805
          },
          "2025": {
            "n": 20,
            "net": 318.84685991170994,
            "plus10": 119.97845810697655
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2062.8369765865687,
        "exbest": 639.2004260392076,
        "ex3best": -890.2935247479069,
        "ex3best_plus10": -1299.5778799703833,
        "years": {
          "2021": {
            "n": 6,
            "net": -241.5085859243946,
            "plus10": -284.111265259133
          },
          "2022": {
            "n": 3,
            "net": -109.83878948232277,
            "plus10": -133.59095516213753
          },
          "2023": {
            "n": 7,
            "net": -232.1223453360314,
            "plus10": -326.62721645536715
          },
          "2024": {
            "n": 7,
            "net": 1067.6620386486234,
            "plus10": 996.5586057845105
          },
          "2025": {
            "n": 15,
            "net": 1180.849475198731,
            "plus10": 970.8179758834397
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2017.6027210298103,
        "exbest": 1026.9540775414584,
        "ex3best": 14.779690121750093,
        "ex3best_plus10": -212.58508118279767,
        "years": {
          "2020": {
            "n": 1,
            "net": 125.20189618053519,
            "plus10": 121.60507371313459
          },
          "2021": {
            "n": 3,
            "net": 155.67714614304214,
            "plus10": 121.56214368356386
          },
          "2022": {
            "n": 2,
            "net": -79.3623291711364,
            "plus10": -92.16138532321926
          },
          "2023": {
            "n": 6,
            "net": 683.3160699526065,
            "plus10": 590.893505349859
          },
          "2024": {
            "n": 4,
            "net": 431.53640424614144,
            "plus10": 362.2403851702342
          },
          "2025": {
            "n": 3,
            "net": 456.3678435203784,
            "plus10": 396.52431921328
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "P02C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6666666666666666,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.6031746031746031,
      "win_months_active": 0.6440677966101694,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.06267375330484803
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.038435031093047245
      ],
      "daily_close_drawdown_pct": -8.744850204205523,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07180444227779112,
          "SPY-USDT": -0.09296988267213147
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07180444227779112,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.02105226077875208
        },
        "SPY-USDT": {
          "BTC-USDT": -0.09296988267213147,
          "PAXG-USDT": 0.02105226077875208,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05042509079164881,
        "2021-12-31 00:00:00+00:00": 0.11661733111089934,
        "2022-12-31 00:00:00+00:00": 0.021193252010424102,
        "2023-12-31 00:00:00+00:00": 0.21551079241891147,
        "2024-12-31 00:00:00+00:00": 0.15476608047542784,
        "2025-12-31 00:00:00+00:00": 0.11998263191669611
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
        "PAXG-USDT": -0.08594998537942798,
        "SPY-USDT": -0.10329619395197386
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.08594998537942798,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.014379259035832552
      },
      "SPY-USDT": {
        "BTC-USDT": -0.10329619395197386,
        "PAXG-USDT": -0.014379259035832552,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 3,
        "both_nonzero": 29,
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
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.06267375330484803,
        "contributions": {
          "BTC-USDT": -0.06267375330484808,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.04695054685472255,
        "contributions": {
          "BTC-USDT": -0.029385393190919436,
          "PAXG-USDT": -0.00905581075329065,
          "SPY-USDT": -0.008509342910512401
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017100506415209327,
        "contributions": {
          "BTC-USDT": -0.007984896567362204,
          "PAXG-USDT": -0.009115609847847138,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.01420330450456253,
        "contributions": {
          "BTC-USDT": -0.014082741968723136,
          "PAXG-USDT": -0.008662835463331103,
          "SPY-USDT": 0.0085422729274917
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009939752938182056,
        "contributions": {
          "BTC-USDT": -0.00993975293818209,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193300912791247,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193300912791308,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.009024612577781754,
        "contributions": {
          "BTC-USDT": -0.009024612577781749,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.0068224493115139895,
        "contributions": {
          "BTC-USDT": 0.0026743944999850023,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009496843811499152
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006204887550047555,
        "contributions": {
          "BTC-USDT": 0.0032070473591690723,
          "PAXG-USDT": -0.009411934909216726,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.005713989602996961,
        "contributions": {
          "BTC-USDT": -0.005713989602996836,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-10-02 00:00:00+00:00",
      "drawdown_pct": -8.744850204205523,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -600.8216045012573,
        "PAXG-USDT": -335.7289024885702,
        "SPY-USDT": -97.38080567520737
      }
    }
  },
  "X02B": {
    "n": 177,
    "net": 6279.083616318994,
    "gross_before_fees": 7271.151754203533,
    "fees": 992.068137884538,
    "pf_from_trades": 1.568637028231048,
    "PF_engine": 1.568637028231048,
    "sharpe_engine": 1.0133144051032732,
    "cagr_engine": 9.797167550579267,
    "dd_engine": -12.849105796809901,
    "plus5_samefills": 5727.934650827584,
    "plus10_samefills": 5176.785685336169,
    "exbest": 4391.309990476638,
    "ex3best": 2460.616706347415,
    "ex3best_plus10_samefills": 1388.7436848288398,
    "time_any_position_pct": 38.28173352017283,
    "entry_notional_time_initial_equity": 0.3469076298035487,
    "entry_turnover_initial_equity": 109.76862809021003,
    "two_side_turnover_initial_equity": 220.45958619656392,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4640.550792584122,
        "fees": 125.49447617794291,
        "plus10": 4501.11248571974,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04787360794206187
      },
      "BTC-USDT:short": {
        "n": 96,
        "net": -1319.8882706652741,
        "fees": 343.81406704662857,
        "plus10": -1701.903900717084,
        "time_open_pct": 9.50458340631751,
        "entry_notional_time_initial_equity": 0.03750550584430943
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1448.1826154390665,
        "fees": 373.4410501906333,
        "plus10": 1033.2481152272517,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.16166353319991253
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1510.2384789610787,
        "fees": 149.3185444693337,
        "plus10": 1344.3289851062636,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.09986498281726486
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 127,
        "net": 3320.6625219188486,
        "fees": 469.30854322457134
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1448.1826154390665,
        "fees": 373.4410501906333
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1510.2384789610787,
        "fees": 149.3185444693337
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 5,
        "net": 536.7360393492551,
        "by_symbol": {
          "BTC-USDT": 400.0932777944194,
          "PAXG-USDT": 0,
          "SPY-USDT": 136.6427615548356
        }
      },
      "2021": {
        "n": 28,
        "net": 1805.5840631060134,
        "by_symbol": {
          "BTC-USDT": 1679.1612852043447,
          "PAXG-USDT": -244.69997738683162,
          "SPY-USDT": 371.12275528850046
        }
      },
      "2022": {
        "n": 27,
        "net": 499.68282404396746,
        "by_symbol": {
          "BTC-USDT": 739.2997717882993,
          "PAXG-USDT": -116.81654675258854,
          "SPY-USDT": -122.80040099174335
        }
      },
      "2023": {
        "n": 36,
        "net": 906.4338292024157,
        "by_symbol": {
          "BTC-USDT": 973.9274706205995,
          "PAXG-USDT": -234.81339182898256,
          "SPY-USDT": 167.3197504107991
        }
      },
      "2024": {
        "n": 37,
        "net": 1459.2337573516345,
        "by_symbol": {
          "BTC-USDT": 9.72806158624087,
          "PAXG-USDT": 985.5611459484338,
          "SPY-USDT": 463.9445498169598
        }
      },
      "2025": {
        "n": 44,
        "net": 1071.4131032657053,
        "by_symbol": {
          "BTC-USDT": -481.5473450750568,
          "PAXG-USDT": 1058.951385459035,
          "SPY-USDT": 494.0090628817273
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 141
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4766.0452687620655,
        "exbest": 2752.777166741772,
        "ex3best": 1005.6229530272608,
        "ex3best_plus10": 883.7708280645137,
        "years": {
          "2020": {
            "n": 3,
            "net": 498.0020800122131,
            "plus10": 489.537412871994
          },
          "2021": {
            "n": 6,
            "net": 1916.7287415821268,
            "plus10": 1901.5794936197528
          },
          "2022": {
            "n": 4,
            "net": -175.67307544672303,
            "plus10": -186.61661950382538
          },
          "2023": {
            "n": 4,
            "net": 1817.928353396409,
            "plus10": 1792.679782662881
          },
          "2024": {
            "n": 8,
            "net": 543.3449889931821,
            "plus10": 506.0007772033803
          },
          "2025": {
            "n": 6,
            "net": 40.21970404691345,
            "plus10": -2.0683611344415738
          }
        }
      },
      "BTC-USDT:short": {
        "gross": -976.0742036186455,
        "exbest": -1552.5445370303603,
        "ex3best": -1995.678810278481,
        "ex3best_plus10": -2363.617612172769,
        "years": {
          "2020": {
            "n": 1,
            "net": -97.9088022177937,
            "plus10": -100.43046187205819
          },
          "2021": {
            "n": 15,
            "net": -237.56745637778155,
            "plus10": -264.91967749646705
          },
          "2022": {
            "n": 19,
            "net": 914.972847235022,
            "plus10": 861.6810402118007
          },
          "2023": {
            "n": 21,
            "net": -844.0008827758099,
            "plus10": -962.1728439346763
          },
          "2024": {
            "n": 19,
            "net": -533.6169274069414,
            "plus10": -605.1003571272711
          },
          "2025": {
            "n": 21,
            "net": -521.7670491219702,
            "plus10": -630.9616004984115
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1821.6236656296987,
        "exbest": 520.2626234691362,
        "ex3best": -851.3231973176515,
        "ex3best_plus10": -1236.8972411177024,
        "years": {
          "2021": {
            "n": 6,
            "net": -244.69997738683168,
            "plus10": -288.4258266072875
          },
          "2022": {
            "n": 3,
            "net": -116.81654675258854,
            "plus10": -142.28217891368473
          },
          "2023": {
            "n": 7,
            "net": -234.8133918289826,
            "plus10": -333.00257096367864
          },
          "2024": {
            "n": 7,
            "net": 985.5611459484336,
            "plus10": 920.1318701013283
          },
          "2025": {
            "n": 15,
            "net": 1058.9513854590355,
            "plus10": 876.8268216105739
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1659.5570234304128,
        "exbest": 869.6704590943384,
        "ex3best": 207.81160984941897,
        "ex3best_plus10": 83.36732653190148,
        "years": {
          "2020": {
            "n": 1,
            "net": 136.6427615548356,
            "plus10": 132.98011879921816
          },
          "2021": {
            "n": 1,
            "net": 371.12275528850046,
            "plus10": 360.67542519521425
          },
          "2022": {
            "n": 1,
            "net": -122.80040099174335,
            "plus10": -129.58795979921084
          },
          "2023": {
            "n": 4,
            "net": 167.31975041079906,
            "plus10": 104.50505961723647
          },
          "2024": {
            "n": 3,
            "net": 463.94454981695986,
            "plus10": 412.2144633411373
          },
          "2025": {
            "n": 2,
            "net": 494.0090628817273,
            "plus10": 463.5418779526683
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "X02B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 58,
        "positive_months": 32,
        "win_months_all": 0.5245901639344263,
        "win_months_active": 0.5517241379310345,
        "quarters_total": 19,
        "positive_quarters": 14,
        "win_quarters": 0.7368421052631579
      },
      "months_total": 63,
      "months_active": 60,
      "win_months_all": 0.5079365079365079,
      "win_months_active": 0.5333333333333333,
      "win_quarters": 0.7142857142857143,
      "worst_month": [
        "2023-03-31 00:00:00+00:00",
        -0.03709345982765344
      ],
      "worst_quarter": [
        "2023-09-30 00:00:00+00:00",
        -0.024041835430956837
      ],
      "daily_close_drawdown_pct": -12.828883108437383,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.13983846130556138,
          "SPY-USDT": 0.08380304158015749
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.13983846130556138,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.035342366755875355
        },
        "SPY-USDT": {
          "BTC-USDT": 0.08380304158015749,
          "PAXG-USDT": -0.035342366755875355,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.057415379475930006,
        "2021-12-31 00:00:00+00:00": 0.16721586824018897,
        "2022-12-31 00:00:00+00:00": 0.04048532365843949,
        "2023-12-31 00:00:00+00:00": 0.07058352457870964,
        "2024-12-31 00:00:00+00:00": 0.10613815834345486,
        "2025-12-31 00:00:00+00:00": 0.07045215125788484
      },
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    "complete_month_contribution_correlation": {
      "BTC-USDT": {
        "BTC-USDT": 1,
        "PAXG-USDT": -0.16119821259709888,
        "SPY-USDT": 0.07974493383997071
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.16119821259709888,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.046793830763717
      },
      "SPY-USDT": {
        "BTC-USDT": 0.07974493383997071,
        "PAXG-USDT": -0.046793830763717,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 7,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 7
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 1,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 1
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 0,
        "both_nonzero": 7,
        "both_negative_and_portfolio_negative": 0
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.03709345982765344,
        "contributions": {
          "BTC-USDT": -0.02812144962846725,
          "PAXG-USDT": -0.00897201019918623,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.03377482588996916,
        "contributions": {
          "BTC-USDT": -0.03377482588996924,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.02844101573155766,
        "contributions": {
          "BTC-USDT": -0.0192476917709226,
          "PAXG-USDT": -0.009193323960635179,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2025-09-30 00:00:00+00:00",
        "portfolio_return": -0.01917850520169262,
        "contributions": {
          "BTC-USDT": -0.030039668607566263,
          "PAXG-USDT": 0.010861163405873524,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.016943999649909336,
        "contributions": {
          "BTC-USDT": -0.016943999649909332,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-12-31 00:00:00+00:00",
        "portfolio_return": -0.015534135926945747,
        "contributions": {
          "BTC-USDT": -0.009691981930302209,
          "PAXG-USDT": 0.0027510326432091375,
          "SPY-USDT": -0.00859318663985272
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.014223789563078348,
        "contributions": {
          "BTC-USDT": -0.014223789563078378,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-03-31 00:00:00+00:00",
        "portfolio_return": -0.013359529545867277,
        "contributions": {
          "BTC-USDT": -0.003912581363633628,
          "PAXG-USDT": -0.009446948182233763,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.011757455182061172,
        "contributions": {
          "BTC-USDT": -0.0028193581322846087,
          "PAXG-USDT": -0.008938097049776746,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.010697023131242656,
        "contributions": {
          "BTC-USDT": -0.01069702313124265,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2023-01-16 00:00:00+00:00",
      "trough": "2024-02-05 00:00:00+00:00",
      "drawdown_pct": -12.828883108437383,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1818.1142569724852,
        "PAXG-USDT": -298.62646683525327,
        "SPY-USDT": 162.45195961583198
      }
    }
  },
  "X02C": {
    "n": 184,
    "net": 6418.732360311478,
    "gross_before_fees": 7495.565287032112,
    "fees": 1076.832926720634,
    "pf_from_trades": 1.5571249207409341,
    "PF_engine": 1.5571249207409343,
    "sharpe_engine": 1.011265320542193,
    "cagr_engine": 9.977200480009628,
    "dd_engine": -9.55488219794496,
    "plus5_samefills": 5820.491845466675,
    "plus10_samefills": 5222.251330621879,
    "exbest": 4563.394707421751,
    "ex3best": 2618.82133887378,
    "ex3best_plus10_samefills": 1452.802614632341,
    "time_any_position_pct": 40.84052227477083,
    "entry_notional_time_initial_equity": 0.39325231890409795,
    "entry_turnover_initial_equity": 119.17515532222001,
    "two_side_turnover_initial_equity": 239.29620593791861,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4579.507067028517,
        "fees": 125.90963097210029,
        "plus10": 4439.607477059514,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.04781627684106783
      },
      "BTC-USDT:short": {
        "n": 96,
        "net": -1324.63507148167,
        "fees": 342.9412476047447,
        "plus10": -1705.680902153608,
        "time_open_pct": 9.50458340631751,
        "entry_notional_time_initial_equity": 0.03743286153493461
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1495.8032958476147,
        "fees": 374.00396659399865,
        "plus10": 1080.2433329653938,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.1624988415174799
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1668.057068917011,
        "fees": 233.97808154979012,
        "plus10": 1408.0814227505773,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.14550433901061546
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 127,
        "net": 3254.871995546845,
        "fees": 468.850878576845
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1495.8032958476147,
        "fees": 374.00396659399865
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1668.057068917011,
        "fees": 233.97808154979012
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 5,
        "net": 524.9045026686482,
        "by_symbol": {
          "BTC-USDT": 397.27998850895636,
          "PAXG-USDT": 0,
          "SPY-USDT": 127.62451415969177
        }
      },
      "2021": {
        "n": 30,
        "net": 1579.8265756558183,
        "by_symbol": {
          "BTC-USDT": 1659.1486526796489,
          "PAXG-USDT": -241.0545415091372,
          "SPY-USDT": 161.73246448530668
        }
      },
      "2022": {
        "n": 28,
        "net": 526.4473376124461,
        "by_symbol": {
          "BTC-USDT": 726.7417489239285,
          "PAXG-USDT": -114.2430082349897,
          "SPY-USDT": -86.0514030764927
        }
      },
      "2023": {
        "n": 38,
        "net": 1400.261455250647,
        "by_symbol": {
          "BTC-USDT": 962.1647795806696,
          "PAXG-USDT": -229.0106203993152,
          "SPY-USDT": 667.1072960692925
        }
      },
      "2024": {
        "n": 38,
        "net": 1403.8490973985658,
        "by_symbol": {
          "BTC-USDT": -4.0102383528222845,
          "PAXG-USDT": 1005.2322590480652,
          "SPY-USDT": 402.62707670332316
        }
      },
      "2025": {
        "n": 45,
        "net": 983.4433917253468,
        "by_symbol": {
          "BTC-USDT": -486.4529357935346,
          "PAXG-USDT": 1074.879206942992,
          "SPY-USDT": 395.0171205758895
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 157
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4705.416698000618,
        "exbest": 2724.1694141387843,
        "ex3best": 977.0152004242733,
        "ex3best_plus10": 854.5136787192932,
        "years": {
          "2020": {
            "n": 3,
            "net": 495.1887907267501,
            "plus10": 486.7448375524583
          },
          "2021": {
            "n": 6,
            "net": 1897.994701342259,
            "plus10": 1883.000467266254
          },
          "2022": {
            "n": 4,
            "net": -172.7893825501933,
            "plus10": -183.5096199657552
          },
          "2023": {
            "n": 4,
            "net": 1786.4718521299098,
            "plus10": 1761.762012876181
          },
          "2024": {
            "n": 8,
            "net": 536.1914439878441,
            "plus10": 498.2964381132066
          },
          "2025": {
            "n": 6,
            "net": 36.44966139194665,
            "plus10": -6.686658782827976
          }
        }
      },
      "BTC-USDT:short": {
        "gross": -981.6938238769233,
        "exbest": -1557.291337846755,
        "ex3best": -2008.8482450168383,
        "ex3best_plus10": -2375.6221530407374,
        "years": {
          "2020": {
            "n": 1,
            "net": -97.9088022177937,
            "plus10": -100.43046187205819
          },
          "2021": {
            "n": 15,
            "net": -238.84604866261003,
            "plus10": -265.69761244323996
          },
          "2022": {
            "n": 19,
            "net": 899.531131474122,
            "plus10": 847.1019402758981
          },
          "2023": {
            "n": 21,
            "net": -824.3070725492403,
            "plus10": -939.7771368565767
          },
          "2024": {
            "n": 19,
            "net": -540.2016823406664,
            "plus10": -613.1906758347645
          },
          "2025": {
            "n": 21,
            "net": -522.9025971854809,
            "plus10": -633.6869554228672
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 1869.8072624416136,
        "exbest": 554.0032194589388,
        "ex3best": -842.8713732320019,
        "ex3best_plus10": -1228.5904588849294,
        "years": {
          "2021": {
            "n": 6,
            "net": -241.0545415091372,
            "plus10": -284.13216474984097
          },
          "2022": {
            "n": 3,
            "net": -114.24300823498972,
            "plus10": -139.25134058042767
          },
          "2023": {
            "n": 7,
            "net": -229.01062039931526,
            "plus10": -325.05054345449037
          },
          "2024": {
            "n": 7,
            "net": 1005.2322590480649,
            "plus10": 938.6146335870834
          },
          "2025": {
            "n": 15,
            "net": 1074.8792069429924,
            "plus10": 890.0627481630695
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1902.0351504668013,
        "exbest": 1021.026651639636,
        "ex3best": 24.950774811398702,
        "ex3best_plus10": -193.1449306474636,
        "years": {
          "2020": {
            "n": 1,
            "net": 127.62451415969177,
            "plus10": 123.95809428967041
          },
          "2021": {
            "n": 3,
            "net": 161.7324644853067,
            "plus10": 127.69020910574325
          },
          "2022": {
            "n": 2,
            "net": -86.0514030764927,
            "plus10": -99.60799360469215
          },
          "2023": {
            "n": 6,
            "net": 667.1072960692925,
            "plus10": 575.6703357990364
          },
          "2024": {
            "n": 4,
            "net": 402.62707670332316,
            "plus10": 337.4612016433945
          },
          "2025": {
            "n": 3,
            "net": 395.0171205758895,
            "plus10": 342.9095755174252
          }
        }
      }
    },
    "calendar_numerical_diagnostics": {
      "nonzero_month_returns_below_1e_10": {},
      "note": "Numerical zero flag only; primary >0 convention unchanged from controls."
    },
    "mtm": {
      "name": "X02C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 59,
        "positive_months": 34,
        "win_months_all": 0.5573770491803278,
        "win_months_active": 0.576271186440678,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 61,
      "win_months_all": 0.5396825396825397,
      "win_months_active": 0.5573770491803278,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2023-03-31 00:00:00+00:00",
        -0.037054510120043904
      ],
      "worst_quarter": [
        "2023-09-30 00:00:00+00:00",
        -0.024358806868825522
      ],
      "daily_close_drawdown_pct": -9.533879520237454,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.13977350072012848,
          "SPY-USDT": -0.01048086982917179
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.13977350072012848,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.0222112781795698
        },
        "SPY-USDT": {
          "BTC-USDT": -0.01048086982917179,
          "PAXG-USDT": 0.0222112781795698,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.056229984607194305,
        "2021-12-31 00:00:00+00:00": 0.14603175962914428,
        "2022-12-31 00:00:00+00:00": 0.04349103951223965,
        "2023-12-31 00:00:00+00:00": 0.11085754702695971,
        "2024-12-31 00:00:00+00:00": 0.1000502521684361,
        "2025-12-31 00:00:00+00:00": 0.06371396050484379
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
        "PAXG-USDT": -0.16114915407880093,
        "SPY-USDT": -0.020634307296048336
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.16114915407880093,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.013082917847150446
      },
      "SPY-USDT": {
        "BTC-USDT": -0.020634307296048336,
        "PAXG-USDT": -0.013082917847150446,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 7,
        "both_nonzero": 30,
        "both_negative_and_portfolio_negative": 7
      },
      "BTC-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 17,
        "both_negative_and_portfolio_negative": 2
      },
      "PAXG-USDT__SPY-USDT": {
        "both_negative": 2,
        "both_nonzero": 11,
        "both_negative_and_portfolio_negative": 2
      }
    },
    "worst_10_complete_months": [
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.037054510120043904,
        "contributions": {
          "BTC-USDT": -0.028082316852737606,
          "PAXG-USDT": -0.00897219326730639,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-01-31 00:00:00+00:00",
        "portfolio_return": -0.03372160284698611,
        "contributions": {
          "BTC-USDT": -0.03372160284698616,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.02837990079299746,
        "contributions": {
          "BTC-USDT": -0.01918666835227564,
          "PAXG-USDT": -0.009193232440721883,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2025-09-30 00:00:00+00:00",
        "portfolio_return": -0.019281342382105437,
        "contributions": {
          "BTC-USDT": -0.03014244062741861,
          "PAXG-USDT": 0.010861098245313033,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.019056751564945795,
        "contributions": {
          "BTC-USDT": -0.0010593423915535324,
          "PAXG-USDT": -0.009321541106390538,
          "SPY-USDT": -0.00867586806700173
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.017057363341099863,
        "contributions": {
          "BTC-USDT": -0.01705736334109984,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-05-31 00:00:00+00:00",
        "portfolio_return": -0.015839218694514656,
        "contributions": {
          "BTC-USDT": -0.006824003133261217,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009015215561253346
        }
      },
      {
        "month": "2022-07-31 00:00:00+00:00",
        "portfolio_return": -0.014187166274204577,
        "contributions": {
          "BTC-USDT": -0.014187166274204462,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.011756644281171624,
        "contributions": {
          "BTC-USDT": -0.0028185609479674805,
          "PAXG-USDT": -0.008938083333204186,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.010550276640181822,
        "contributions": {
          "BTC-USDT": -0.010550276640181924,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2023-01-16 00:00:00+00:00",
      "trough": "2024-02-05 00:00:00+00:00",
      "drawdown_pct": -9.533879520237454,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -1798.6938479868968,
        "PAXG-USDT": -291.7768611697553,
        "SPY-USDT": 662.139140234691
      }
    }
  }
}
```

## Execution paths
```json
{
  "E02B": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 62,
      "retainedEntries": 54,
      "displaced": [
        {
          "open": 1604319060000,
          "close": 1604348160000,
          "net": -93.72809563330067
        },
        {
          "open": 1604779380000,
          "close": 1604800080000,
          "net": -93.66643236204395
        },
        {
          "open": 1607430960000,
          "close": 1607468460000,
          "net": 92.09079099126495
        },
        {
          "open": 1607476380000,
          "close": 1607682120000,
          "net": 53.54082303935061
        },
        {
          "open": 1610726520000,
          "close": 1610755680000,
          "net": -102.44911518941483
        },
        {
          "open": 1614299520000,
          "close": 1614528180000,
          "net": 95.92148944652375
        },
        {
          "open": 1616445840000,
          "close": 1616477220000,
          "net": 90.66646201382737
        },
        {
          "open": 1617486780000,
          "close": 1617633540000,
          "net": -109.01703983406921
        },
        {
          "open": 1617797580000,
          "close": 1617906720000,
          "net": -109.30650131894329
        },
        {
          "open": 1618564200000,
          "close": 1618631040000,
          "net": -105.77671404369818
        },
        {
          "open": 1620677040000,
          "close": 1620677160000,
          "net": 97.11690664163962
        },
        {
          "open": 1623960180000,
          "close": 1624040940000,
          "net": 107.8826390873738
        },
        {
          "open": 1627934820000,
          "close": 1628167560000,
          "net": 117.33158815330974
        },
        {
          "open": 1629821760000,
          "close": 1629913200000,
          "net": -104.6029006294542
        },
        {
          "open": 1634919180000,
          "close": 1635168480000,
          "net": -115.46184971804635
        },
        {
          "open": 1635321720000,
          "close": 1635322140000,
          "net": 90.09768553692034
        },
        {
          "open": 1637020920000,
          "close": 1637024640000,
          "net": 121.60103950957757
        },
        {
          "open": 1648776480000,
          "close": 1648825860000,
          "net": -117.39904053381449
        },
        {
          "open": 1649094180000,
          "close": 1649103720000,
          "net": -112.35759947482141
        },
        {
          "open": 1657469460000,
          "close": 1657577100000,
          "net": 150.98150141339298
        },
        {
          "open": 1658776200000,
          "close": 1658805180000,
          "net": 102.71100828609778
        },
        {
          "open": 1660763640000,
          "close": 1660890720000,
          "net": 94.54577841130873
        },
        {
          "open": 1663086720000,
          "close": 1663105380000,
          "net": 90.46869365354215
        },
        {
          "open": 1665159900000,
          "close": 1665432000000,
          "net": 55.193010389999834
        },
        {
          "open": 1667420700000,
          "close": 1667541120000,
          "net": -116.96735627312422
        },
        {
          "open": 1671200340000,
          "close": 1671232440000,
          "net": 65.91397647866992
        },
        {
          "open": 1675614060000,
          "close": 1675661280000,
          "net": 120.15779629227667
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 156.5636619391465
        },
        {
          "open": 1675915440000,
          "close": 1675971120000,
          "net": 91.07781303314728
        },
        {
          "open": 1677254520000,
          "close": 1677528000000,
          "net": -8.970794980151886
        },
        {
          "open": 1681727880000,
          "close": 1681731300000,
          "net": 116.74443325245814
        },
        {
          "open": 1681939380000,
          "close": 1681993080000,
          "net": 96.06505600374906
        },
        {
          "open": 1682919780000,
          "close": 1682974680000,
          "net": 110.5058427846736
        },
        {
          "open": 1683510240000,
          "close": 1683535680000,
          "net": 126.28129565225737
        },
        {
          "open": 1695598080000,
          "close": 1695601380000,
          "net": 89.38373461951143
        },
        {
          "open": 1696963800000,
          "close": 1696996860000,
          "net": 124.75266633328224
        },
        {
          "open": 1699921080000,
          "close": 1699976040000,
          "net": 155.8717243360836
        },
        {
          "open": 1702310880000,
          "close": 1702319400000,
          "net": 87.1722031847079
        },
        {
          "open": 1703583960000,
          "close": 1703612400000,
          "net": 104.69599991027633
        },
        {
          "open": 1703780880000,
          "close": 1703860740000,
          "net": -136.35731952493657
        },
        {
          "open": 1705076220000,
          "close": 1705097100000,
          "net": 134.31711298518636
        },
        {
          "open": 1710432900000,
          "close": 1710462360000,
          "net": -138.86459180097592
        },
        {
          "open": 1711113780000,
          "close": 1711212300000,
          "net": -140.28029873918948
        },
        {
          "open": 1711982160000,
          "close": 1712025420000,
          "net": 147.59135353806624
        },
        {
          "open": 1712682480000,
          "close": 1712778780000,
          "net": -139.19111934361553
        },
        {
          "open": 1716494460000,
          "close": 1716573840000,
          "net": -151.43872352372114
        },
        {
          "open": 1716998640000,
          "close": 1717043640000,
          "net": -147.6190736860564
        },
        {
          "open": 1717171620000,
          "close": 1717329060000,
          "net": -146.23460719010257
        },
        {
          "open": 1718080020000,
          "close": 1718099520000,
          "net": 71.80071590864067
        },
        {
          "open": 1721880540000,
          "close": 1721945160000,
          "net": -148.7690152643381
        },
        {
          "open": 1722298860000,
          "close": 1722457140000,
          "net": 157.71656845020084
        },
        {
          "open": 1722473280000,
          "close": 1722526320000,
          "net": 99.46321638935883
        },
        {
          "open": 1726446960000,
          "close": 1726497300000,
          "net": 186.08560335772626
        },
        {
          "open": 1729667580000,
          "close": 1729702500000,
          "net": 147.83159203971195
        },
        {
          "open": 1730407740000,
          "close": 1730469420000,
          "net": -147.3719147605483
        },
        {
          "open": 1730641620000,
          "close": 1730757180000,
          "net": 120.5993902151509
        },
        {
          "open": 1732562640000,
          "close": 1732609380000,
          "net": 117.87517210634269
        },
        {
          "open": 1733767200000,
          "close": 1733778300000,
          "net": 153.6890688834858
        },
        {
          "open": 1733848320000,
          "close": 1733906640000,
          "net": -162.37107827653432
        },
        {
          "open": 1736271540000,
          "close": 1736336040000,
          "net": 122.80164628974723
        },
        {
          "open": 1737938880000,
          "close": 1737956400000,
          "net": 133.05940173442193
        },
        {
          "open": 1738354980000,
          "close": 1738466940000,
          "net": 172.203934498345
        },
        {
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 127.9920506539941
        },
        {
          "open": 1748562540000,
          "close": 1748656560000,
          "net": 122.87216242990796
        },
        {
          "open": 1751646060000,
          "close": 1751689860000,
          "net": -152.80024426026773
        },
        {
          "open": 1753427460000,
          "close": 1753559340000,
          "net": -181.7598357825994
        },
        {
          "open": 1753807020000,
          "close": 1753858260000,
          "net": -130.93853705420716
        },
        {
          "open": 1753993080000,
          "close": 1754009520000,
          "net": 170.6075929971438
        },
        {
          "open": 1755188880000,
          "close": 1755460800000,
          "net": -13.808742299999999
        },
        {
          "open": 1759854240000,
          "close": 1759921920000,
          "net": -183.42998352425732
        },
        {
          "open": 1760115060000,
          "close": 1760124120000,
          "net": 123.56976861023709
        }
      ],
      "newEntries": 8,
      "retainedEntrySameExitTime": 54
    },
    "SPY-USDT:long": {
      "baseline": 12,
      "candidate": 12,
      "retainedEntries": 12,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 12
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  },
  "E02C": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 62,
      "retainedEntries": 54,
      "displaced": [
        {
          "open": 1604319060000,
          "close": 1604348160000,
          "net": -93.72809563330067
        },
        {
          "open": 1604779380000,
          "close": 1604800080000,
          "net": -93.66643236204395
        },
        {
          "open": 1607430960000,
          "close": 1607468460000,
          "net": 92.09079099126495
        },
        {
          "open": 1607476380000,
          "close": 1607682120000,
          "net": 53.54082303935061
        },
        {
          "open": 1610726520000,
          "close": 1610755680000,
          "net": -102.44911518941483
        },
        {
          "open": 1614299520000,
          "close": 1614528180000,
          "net": 95.92148944652375
        },
        {
          "open": 1616445840000,
          "close": 1616477220000,
          "net": 90.66646201382737
        },
        {
          "open": 1617486780000,
          "close": 1617633540000,
          "net": -107.84481359929359
        },
        {
          "open": 1617797580000,
          "close": 1617906720000,
          "net": -109.30650131894329
        },
        {
          "open": 1618564200000,
          "close": 1618631040000,
          "net": -104.347298989052
        },
        {
          "open": 1620677040000,
          "close": 1620677160000,
          "net": 94.95875316071398
        },
        {
          "open": 1623960180000,
          "close": 1624040940000,
          "net": 106.38426910004917
        },
        {
          "open": 1627934820000,
          "close": 1628167560000,
          "net": 115.82733702313911
        },
        {
          "open": 1629821760000,
          "close": 1629913200000,
          "net": -102.71816368117653
        },
        {
          "open": 1634919180000,
          "close": 1635168480000,
          "net": -112.50128946886568
        },
        {
          "open": 1635321720000,
          "close": 1635322140000,
          "net": 88.39772920603505
        },
        {
          "open": 1637020920000,
          "close": 1637024640000,
          "net": 118.59854470687195
        },
        {
          "open": 1648776480000,
          "close": 1648825860000,
          "net": -114.42691292536348
        },
        {
          "open": 1649094180000,
          "close": 1649103720000,
          "net": -110.83925353597247
        },
        {
          "open": 1657469460000,
          "close": 1657577100000,
          "net": 148.40062104735208
        },
        {
          "open": 1658776200000,
          "close": 1658805180000,
          "net": 101.3323370339354
        },
        {
          "open": 1660763640000,
          "close": 1660890720000,
          "net": 92.8162824647604
        },
        {
          "open": 1663086720000,
          "close": 1663105380000,
          "net": 88.89532506826315
        },
        {
          "open": 1665159900000,
          "close": 1665432000000,
          "net": 54.265396770000685
        },
        {
          "open": 1667420700000,
          "close": 1667541120000,
          "net": -115.03081063946323
        },
        {
          "open": 1671200340000,
          "close": 1671232440000,
          "net": 64.95870145723993
        },
        {
          "open": 1675614060000,
          "close": 1675661280000,
          "net": 118.04358286777915
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 154.05002516489415
        },
        {
          "open": 1675915440000,
          "close": 1675971120000,
          "net": 89.86881551500815
        },
        {
          "open": 1677254520000,
          "close": 1677528000000,
          "net": -8.810602212649176
        },
        {
          "open": 1681727880000,
          "close": 1681731300000,
          "net": 114.72463336919661
        },
        {
          "open": 1681939380000,
          "close": 1681993080000,
          "net": 94.3184186218633
        },
        {
          "open": 1682919780000,
          "close": 1682974680000,
          "net": 109.1902970372364
        },
        {
          "open": 1683510240000,
          "close": 1683535680000,
          "net": 122.92869488272761
        },
        {
          "open": 1695598080000,
          "close": 1695601380000,
          "net": 87.16025863395146
        },
        {
          "open": 1696963800000,
          "close": 1696996860000,
          "net": 121.38097264859763
        },
        {
          "open": 1699921080000,
          "close": 1699976040000,
          "net": 151.5419542156368
        },
        {
          "open": 1702310880000,
          "close": 1702319400000,
          "net": 85.23504311393661
        },
        {
          "open": 1703583960000,
          "close": 1703612400000,
          "net": 106.74886265361508
        },
        {
          "open": 1703780880000,
          "close": 1703860740000,
          "net": -139.24318872123155
        },
        {
          "open": 1705076220000,
          "close": 1705097100000,
          "net": 137.71754622531765
        },
        {
          "open": 1710432900000,
          "close": 1710462360000,
          "net": -141.78805689152276
        },
        {
          "open": 1711113780000,
          "close": 1711212300000,
          "net": -144.23185645015255
        },
        {
          "open": 1711982160000,
          "close": 1712025420000,
          "net": 150.03088004282768
        },
        {
          "open": 1712682480000,
          "close": 1712778780000,
          "net": -142.25026482369498
        },
        {
          "open": 1716494460000,
          "close": 1716573840000,
          "net": -153.76855003947068
        },
        {
          "open": 1716998640000,
          "close": 1717043640000,
          "net": -150.2788768155349
        },
        {
          "open": 1717171620000,
          "close": 1717329060000,
          "net": -148.7131598543416
        },
        {
          "open": 1718080020000,
          "close": 1718099520000,
          "net": 72.67633439533141
        },
        {
          "open": 1721880540000,
          "close": 1721945160000,
          "net": -151.0935311278434
        },
        {
          "open": 1722298860000,
          "close": 1722457140000,
          "net": 160.83966881555133
        },
        {
          "open": 1722473280000,
          "close": 1722526320000,
          "net": 102.43226762486208
        },
        {
          "open": 1726446960000,
          "close": 1726497300000,
          "net": 188.9931909101893
        },
        {
          "open": 1729667580000,
          "close": 1729702500000,
          "net": 149.87064848163902
        },
        {
          "open": 1730407740000,
          "close": 1730469420000,
          "net": -149.84875366408687
        },
        {
          "open": 1730641620000,
          "close": 1730757180000,
          "net": 122.9874969520846
        },
        {
          "open": 1732562640000,
          "close": 1732609380000,
          "net": 119.90750265990032
        },
        {
          "open": 1733767200000,
          "close": 1733778300000,
          "net": 156.16792483321944
        },
        {
          "open": 1733848320000,
          "close": 1733906640000,
          "net": -165.49359901262073
        },
        {
          "open": 1736271540000,
          "close": 1736336040000,
          "net": 124.66227729413733
        },
        {
          "open": 1737938880000,
          "close": 1737956400000,
          "net": 135.07545327585257
        },
        {
          "open": 1738354980000,
          "close": 1738466940000,
          "net": 174.49998695832295
        },
        {
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 129.4465057750622
        },
        {
          "open": 1748562540000,
          "close": 1748656560000,
          "net": 124.76250339036808
        },
        {
          "open": 1751646060000,
          "close": 1751689860000,
          "net": -155.11539947633239
        },
        {
          "open": 1753427460000,
          "close": 1753559340000,
          "net": -181.7598357825994
        },
        {
          "open": 1753807020000,
          "close": 1753858260000,
          "net": -132.2349582131597
        },
        {
          "open": 1753993080000,
          "close": 1754009520000,
          "net": 173.7095492334555
        },
        {
          "open": 1755188880000,
          "close": 1755460800000,
          "net": -14.031463950000001
        },
        {
          "open": 1759854240000,
          "close": 1759921920000,
          "net": -185.53837413947866
        },
        {
          "open": 1760115060000,
          "close": 1760124120000,
          "net": 125.81649167587857
        }
      ],
      "newEntries": 8,
      "retainedEntrySameExitTime": 54
    },
    "SPY-USDT:long": {
      "baseline": 19,
      "candidate": 19,
      "retainedEntries": 19,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 19
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  },
  "P02B": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 126,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 1,
      "retainedEntrySameExitTime": 121
    },
    "SPY-USDT:long": {
      "baseline": 12,
      "candidate": 12,
      "retainedEntries": 12,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 12
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  },
  "P02C": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 126,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 1,
      "retainedEntrySameExitTime": 121
    },
    "SPY-USDT:long": {
      "baseline": 19,
      "candidate": 19,
      "retainedEntries": 19,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 19
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  },
  "X02B": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 96,
      "retainedEntries": 0,
      "displaced": [
        {
          "open": 1603974540000,
          "close": 1603979820000,
          "net": -94.18571805651037
        },
        {
          "open": 1604319060000,
          "close": 1604348160000,
          "net": -93.72809563330067
        },
        {
          "open": 1604779380000,
          "close": 1604800080000,
          "net": -93.66643236204395
        },
        {
          "open": 1606377840000,
          "close": 1606379520000,
          "net": 67.2539011208586
        },
        {
          "open": 1606409580000,
          "close": 1606680000000,
          "net": -79.70720613000007
        },
        {
          "open": 1607430960000,
          "close": 1607468460000,
          "net": 92.09079099126495
        },
        {
          "open": 1607476380000,
          "close": 1607682120000,
          "net": 53.54082303935061
        },
        {
          "open": 1610309520000,
          "close": 1610336160000,
          "net": 130.3304009618227
        },
        {
          "open": 1610347380000,
          "close": 1610611200000,
          "net": -93.44655999999999
        },
        {
          "open": 1610726520000,
          "close": 1610755680000,
          "net": -102.44911518941483
        },
        {
          "open": 1610871000000,
          "close": 1610918160000,
          "net": -103.0307972379368
        },
        {
          "open": 1611116220000,
          "close": 1611220680000,
          "net": 122.94151098902024
        },
        {
          "open": 1613996040000,
          "close": 1614003240000,
          "net": 124.59663334939428
        },
        {
          "open": 1614055200000,
          "close": 1614068880000,
          "net": 86.14778377810624
        },
        {
          "open": 1614299520000,
          "close": 1614528180000,
          "net": 95.92148944652375
        },
        {
          "open": 1615854300000,
          "close": 1616007720000,
          "net": -112.41206477948923
        },
        {
          "open": 1616319720000,
          "close": 1616363460000,
          "net": -109.90741055507941
        },
        {
          "open": 1616445840000,
          "close": 1616477220000,
          "net": 90.66646201382737
        },
        {
          "open": 1617486780000,
          "close": 1617633540000,
          "net": -109.01703983406921
        },
        {
          "open": 1617797580000,
          "close": 1617906720000,
          "net": -109.30650131894329
        },
        {
          "open": 1618564200000,
          "close": 1618631040000,
          "net": -105.77671404369818
        },
        {
          "open": 1618675380000,
          "close": 1618715880000,
          "net": 95.83887410619023
        },
        {
          "open": 1620677040000,
          "close": 1620677160000,
          "net": 97.11690664163962
        },
        {
          "open": 1623960180000,
          "close": 1624040940000,
          "net": 107.8826390873738
        },
        {
          "open": 1627934820000,
          "close": 1628167560000,
          "net": 117.33158815330974
        },
        {
          "open": 1628785800000,
          "close": 1628823060000,
          "net": -108.1095166943464
        },
        {
          "open": 1629249240000,
          "close": 1629397560000,
          "net": -111.47458509254675
        },
        {
          "open": 1629821760000,
          "close": 1629913200000,
          "net": -104.6029006294542
        },
        {
          "open": 1629979440000,
          "close": 1630076580000,
          "net": -109.40040726699223
        },
        {
          "open": 1634919180000,
          "close": 1635168480000,
          "net": -115.46184971804635
        },
        {
          "open": 1635321720000,
          "close": 1635322140000,
          "net": 90.09768553692034
        },
        {
          "open": 1635362640000,
          "close": 1635414720000,
          "net": -113.56658290287777
        },
        {
          "open": 1636049040000,
          "close": 1636082100000,
          "net": -112.30873474568438
        },
        {
          "open": 1636201080000,
          "close": 1636235160000,
          "net": -110.6684503442504
        },
        {
          "open": 1636718760000,
          "close": 1636849380000,
          "net": -113.65557145211451
        },
        {
          "open": 1637020920000,
          "close": 1637024640000,
          "net": 121.60103950957757
        },
        {
          "open": 1640665080000,
          "close": 1640702400000,
          "net": 128.73642757012942
        },
        {
          "open": 1644619860000,
          "close": 1644883200000,
          "net": -39.29861674999991
        },
        {
          "open": 1645113960000,
          "close": 1645132320000,
          "net": 78.25190409814995
        },
        {
          "open": 1646382660000,
          "close": 1646424900000,
          "net": 127.9468765765125
        },
        {
          "open": 1648776480000,
          "close": 1648825860000,
          "net": -117.39904053381449
        },
        {
          "open": 1649094180000,
          "close": 1649103720000,
          "net": -112.35759947482141
        },
        {
          "open": 1649252580000,
          "close": 1649264700000,
          "net": 93.85657006166866
        },
        {
          "open": 1657469460000,
          "close": 1657577100000,
          "net": 150.98150141339298
        },
        {
          "open": 1658776200000,
          "close": 1658805180000,
          "net": 102.71100828609778
        },
        {
          "open": 1660763640000,
          "close": 1660890720000,
          "net": 94.54577841130873
        },
        {
          "open": 1663086720000,
          "close": 1663105380000,
          "net": 90.46869365354215
        },
        {
          "open": 1665159900000,
          "close": 1665432000000,
          "net": 55.193010389999834
        },
        {
          "open": 1667420700000,
          "close": 1667541120000,
          "net": -116.96735627312422
        },
        {
          "open": 1667808120000,
          "close": 1667879640000,
          "net": 89.61946457514745
        },
        {
          "open": 1667880540000,
          "close": 1667880720000,
          "net": 60.24711033142497
        },
        {
          "open": 1671123060000,
          "close": 1671181320000,
          "net": 148.41759812561438
        },
        {
          "open": 1671200340000,
          "close": 1671232440000,
          "net": 65.91397647866992
        },
        {
          "open": 1673011800000,
          "close": 1673011860000,
          "net": -107.21330997518993
        },
        {
          "open": 1675110180000,
          "close": 1675205520000,
          "net": -137.5295309588423
        },
        {
          "open": 1675614060000,
          "close": 1675661280000,
          "net": 120.15779629227667
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 156.5636619391465
        },
        {
          "open": 1675915440000,
          "close": 1675971120000,
          "net": 91.07781303314728
        },
        {
          "open": 1677054900000,
          "close": 1677120240000,
          "net": -139.46651383071682
        },
        {
          "open": 1677254520000,
          "close": 1677528000000,
          "net": -8.970794980151886
        },
        {
          "open": 1681727880000,
          "close": 1681731300000,
          "net": 116.74443325245814
        },
        {
          "open": 1681738260000,
          "close": 1681817580000,
          "net": -137.11907737493618
        },
        {
          "open": 1681939380000,
          "close": 1681993080000,
          "net": 96.06505600374906
        },
        {
          "open": 1682919780000,
          "close": 1682974680000,
          "net": 110.5058427846736
        },
        {
          "open": 1683510240000,
          "close": 1683535680000,
          "net": 126.28129565225737
        },
        {
          "open": 1685542800000,
          "close": 1685666340000,
          "net": 120.97580977996387
        },
        {
          "open": 1688558940000,
          "close": 1688628240000,
          "net": -139.14015683449958
        },
        {
          "open": 1688688180000,
          "close": 1688961600000,
          "net": -70.06531649094791
        },
        {
          "open": 1695598080000,
          "close": 1695601380000,
          "net": 89.38373461951143
        },
        {
          "open": 1696963800000,
          "close": 1696996860000,
          "net": 124.75266633328224
        },
        {
          "open": 1699359180000,
          "close": 1699380420000,
          "net": -130.46851117120156
        },
        {
          "open": 1699921080000,
          "close": 1699976040000,
          "net": 155.8717243360836
        },
        {
          "open": 1699987440000,
          "close": 1699988040000,
          "net": 88.88198212889972
        },
        {
          "open": 1701082740000,
          "close": 1701186240000,
          "net": -112.17435367416033
        },
        {
          "open": 1702310880000,
          "close": 1702319400000,
          "net": 87.1722031847079
        },
        {
          "open": 1703583960000,
          "close": 1703612400000,
          "net": 104.69599991027633
        },
        {
          "open": 1703780880000,
          "close": 1703860740000,
          "net": -136.35731952493657
        },
        {
          "open": 1705076220000,
          "close": 1705097100000,
          "net": 134.31711298518636
        },
        {
          "open": 1708517280000,
          "close": 1708559220000,
          "net": -140.07069787719593
        },
        {
          "open": 1710432900000,
          "close": 1710462360000,
          "net": -138.86459180097592
        },
        {
          "open": 1710624000000,
          "close": 1710832620000,
          "net": 118.42719351656072
        },
        {
          "open": 1710837060000,
          "close": 1710912240000,
          "net": 92.86165381919224
        },
        {
          "open": 1711113780000,
          "close": 1711212300000,
          "net": -140.28029873918948
        },
        {
          "open": 1711982160000,
          "close": 1712025420000,
          "net": 147.59135353806624
        },
        {
          "open": 1712682480000,
          "close": 1712778780000,
          "net": -139.19111934361553
        },
        {
          "open": 1716494460000,
          "close": 1716573840000,
          "net": -151.43872352372114
        },
        {
          "open": 1716998640000,
          "close": 1717043640000,
          "net": -147.6190736860564
        },
        {
          "open": 1717171620000,
          "close": 1717329060000,
          "net": -146.23460719010257
        },
        {
          "open": 1718080020000,
          "close": 1718099520000,
          "net": 71.80071590864067
        },
        {
          "open": 1721880540000,
          "close": 1721945160000,
          "net": -148.7690152643381
        },
        {
          "open": 1722298860000,
          "close": 1722457140000,
          "net": 157.71656845020084
        },
        {
          "open": 1722473280000,
          "close": 1722526320000,
          "net": 99.46321638935883
        },
        {
          "open": 1724762700000,
          "close": 1724794680000,
          "net": 154.29360106962176
        },
        {
          "open": 1726446960000,
          "close": 1726497300000,
          "net": 186.08560335772626
        },
        {
          "open": 1726506780000,
          "close": 1726566900000,
          "net": -150.31944277753215
        },
        {
          "open": 1727717580000,
          "close": 1727795040000,
          "net": 83.51228389330397
        },
        {
          "open": 1729667580000,
          "close": 1729702500000,
          "net": 147.83159203971195
        },
        {
          "open": 1730407740000,
          "close": 1730469420000,
          "net": -147.3719147605483
        },
        {
          "open": 1730641620000,
          "close": 1730757180000,
          "net": 120.5993902151509
        },
        {
          "open": 1732562640000,
          "close": 1732609380000,
          "net": 117.87517210634269
        },
        {
          "open": 1733144100000,
          "close": 1733150100000,
          "net": -159.31139584605683
        },
        {
          "open": 1733767200000,
          "close": 1733778300000,
          "net": 153.6890688834858
        },
        {
          "open": 1733848320000,
          "close": 1733906640000,
          "net": -162.37107827653432
        },
        {
          "open": 1734552240000,
          "close": 1734566340000,
          "net": 163.36135966129245
        },
        {
          "open": 1734573540000,
          "close": 1734632400000,
          "net": 90.80792905740498
        },
        {
          "open": 1736271540000,
          "close": 1736336040000,
          "net": 122.80164628974723
        },
        {
          "open": 1737606120000,
          "close": 1737642960000,
          "net": -160.53274305662475
        },
        {
          "open": 1737938880000,
          "close": 1737956400000,
          "net": 133.05940173442193
        },
        {
          "open": 1738354980000,
          "close": 1738466940000,
          "net": 172.203934498345
        },
        {
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 127.9920506539941
        },
        {
          "open": 1748562540000,
          "close": 1748656560000,
          "net": 122.87216242990796
        },
        {
          "open": 1749735180000,
          "close": 1749749220000,
          "net": -177.19868277279647
        },
        {
          "open": 1749759300000,
          "close": 1749772980000,
          "net": 177.8710697848895
        },
        {
          "open": 1751380860000,
          "close": 1751419080000,
          "net": 159.5159703716212
        },
        {
          "open": 1751646060000,
          "close": 1751689860000,
          "net": -152.80024426026773
        },
        {
          "open": 1752552600000,
          "close": 1752587040000,
          "net": -146.96208998589125
        },
        {
          "open": 1753427460000,
          "close": 1753559340000,
          "net": -181.7598357825994
        },
        {
          "open": 1753807020000,
          "close": 1753858260000,
          "net": -130.93853705420716
        },
        {
          "open": 1753993080000,
          "close": 1754009520000,
          "net": 170.6075929971438
        },
        {
          "open": 1755188880000,
          "close": 1755460800000,
          "net": -13.808742299999999
        },
        {
          "open": 1758305580000,
          "close": 1758520800000,
          "net": 192.58297265666133
        },
        {
          "open": 1759854240000,
          "close": 1759921920000,
          "net": -183.42998352425732
        },
        {
          "open": 1760115060000,
          "close": 1760124120000,
          "net": 123.56976861023709
        },
        {
          "open": 1761700920000,
          "close": 1761724500000,
          "net": -181.06906602129538
        },
        {
          "open": 1761754080000,
          "close": 1761763200000,
          "net": 154.61890211816362
        }
      ],
      "newEntries": 96,
      "retainedEntrySameExitTime": 0
    },
    "SPY-USDT:long": {
      "baseline": 12,
      "candidate": 12,
      "retainedEntries": 12,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 12
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  },
  "X02C": {
    "BTC-USDT:long": {
      "baseline": 31,
      "candidate": 31,
      "retainedEntries": 31,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 31
    },
    "BTC-USDT:short": {
      "baseline": 125,
      "candidate": 96,
      "retainedEntries": 0,
      "displaced": [
        {
          "open": 1603974540000,
          "close": 1603979820000,
          "net": -94.18571805651037
        },
        {
          "open": 1604319060000,
          "close": 1604348160000,
          "net": -93.72809563330067
        },
        {
          "open": 1604779380000,
          "close": 1604800080000,
          "net": -93.66643236204395
        },
        {
          "open": 1606377840000,
          "close": 1606379520000,
          "net": 67.2539011208586
        },
        {
          "open": 1606409580000,
          "close": 1606680000000,
          "net": -79.70720613000007
        },
        {
          "open": 1607430960000,
          "close": 1607468460000,
          "net": 92.09079099126495
        },
        {
          "open": 1607476380000,
          "close": 1607682120000,
          "net": 53.54082303935061
        },
        {
          "open": 1610309520000,
          "close": 1610336160000,
          "net": 130.3304009618227
        },
        {
          "open": 1610347380000,
          "close": 1610611200000,
          "net": -93.44655999999999
        },
        {
          "open": 1610726520000,
          "close": 1610755680000,
          "net": -102.44911518941483
        },
        {
          "open": 1610871000000,
          "close": 1610918160000,
          "net": -103.0307972379368
        },
        {
          "open": 1611116220000,
          "close": 1611220680000,
          "net": 122.94151098902024
        },
        {
          "open": 1613996040000,
          "close": 1614003240000,
          "net": 124.59663334939428
        },
        {
          "open": 1614055200000,
          "close": 1614068880000,
          "net": 86.14778377810624
        },
        {
          "open": 1614299520000,
          "close": 1614528180000,
          "net": 95.92148944652375
        },
        {
          "open": 1615854300000,
          "close": 1616007720000,
          "net": -112.41206477948923
        },
        {
          "open": 1616319720000,
          "close": 1616363460000,
          "net": -108.38091874181441
        },
        {
          "open": 1616445840000,
          "close": 1616477220000,
          "net": 90.66646201382737
        },
        {
          "open": 1617486780000,
          "close": 1617633540000,
          "net": -107.84481359929359
        },
        {
          "open": 1617797580000,
          "close": 1617906720000,
          "net": -109.30650131894329
        },
        {
          "open": 1618564200000,
          "close": 1618631040000,
          "net": -104.347298989052
        },
        {
          "open": 1618675380000,
          "close": 1618715880000,
          "net": 95.83887410619023
        },
        {
          "open": 1620677040000,
          "close": 1620677160000,
          "net": 94.95875316071398
        },
        {
          "open": 1623960180000,
          "close": 1624040940000,
          "net": 106.38426910004917
        },
        {
          "open": 1627934820000,
          "close": 1628167560000,
          "net": 115.82733702313911
        },
        {
          "open": 1628785800000,
          "close": 1628823060000,
          "net": -106.79110795417144
        },
        {
          "open": 1629249240000,
          "close": 1629397560000,
          "net": -109.67660791363515
        },
        {
          "open": 1629821760000,
          "close": 1629913200000,
          "net": -102.71816368117653
        },
        {
          "open": 1629979440000,
          "close": 1630076580000,
          "net": -107.69102590344548
        },
        {
          "open": 1634919180000,
          "close": 1635168480000,
          "net": -112.50128946886568
        },
        {
          "open": 1635321720000,
          "close": 1635322140000,
          "net": 88.39772920603505
        },
        {
          "open": 1635362640000,
          "close": 1635414720000,
          "net": -113.56658290287777
        },
        {
          "open": 1636049040000,
          "close": 1636082100000,
          "net": -109.39162475228997
        },
        {
          "open": 1636201080000,
          "close": 1636235160000,
          "net": -107.83079777132201
        },
        {
          "open": 1636718760000,
          "close": 1636849380000,
          "net": -111.8515147623984
        },
        {
          "open": 1637020920000,
          "close": 1637024640000,
          "net": 118.59854470687195
        },
        {
          "open": 1640665080000,
          "close": 1640702400000,
          "net": 126.43756279209138
        },
        {
          "open": 1644619860000,
          "close": 1644883200000,
          "net": -38.78152968749991
        },
        {
          "open": 1645113960000,
          "close": 1645132320000,
          "net": 75.8806342769939
        },
        {
          "open": 1646382660000,
          "close": 1646424900000,
          "net": 124.86381930960857
        },
        {
          "open": 1648776480000,
          "close": 1648825860000,
          "net": -114.42691292536348
        },
        {
          "open": 1649094180000,
          "close": 1649103720000,
          "net": -110.83925353597247
        },
        {
          "open": 1649252580000,
          "close": 1649264700000,
          "net": 91.72346619663075
        },
        {
          "open": 1657469460000,
          "close": 1657577100000,
          "net": 148.40062104735208
        },
        {
          "open": 1658776200000,
          "close": 1658805180000,
          "net": 101.3323370339354
        },
        {
          "open": 1660763640000,
          "close": 1660890720000,
          "net": 92.8162824647604
        },
        {
          "open": 1663086720000,
          "close": 1663105380000,
          "net": 88.89532506826315
        },
        {
          "open": 1665159900000,
          "close": 1665432000000,
          "net": 54.265396770000685
        },
        {
          "open": 1667420700000,
          "close": 1667541120000,
          "net": -115.03081063946323
        },
        {
          "open": 1667808120000,
          "close": 1667879640000,
          "net": 88.00760370149372
        },
        {
          "open": 1667880540000,
          "close": 1667880720000,
          "net": 59.095891662671626
        },
        {
          "open": 1671123060000,
          "close": 1671181320000,
          "net": 146.03337968182942
        },
        {
          "open": 1671200340000,
          "close": 1671232440000,
          "net": 64.95870145723993
        },
        {
          "open": 1673011800000,
          "close": 1673011860000,
          "net": -105.45210570455028
        },
        {
          "open": 1675110180000,
          "close": 1675205520000,
          "net": -135.58335835093416
        },
        {
          "open": 1675614060000,
          "close": 1675661280000,
          "net": 118.04358286777915
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 154.05002516489415
        },
        {
          "open": 1675915440000,
          "close": 1675971120000,
          "net": 89.86881551500815
        },
        {
          "open": 1677054900000,
          "close": 1677120240000,
          "net": -137.07223891516801
        },
        {
          "open": 1677254520000,
          "close": 1677528000000,
          "net": -8.810602212649176
        },
        {
          "open": 1681727880000,
          "close": 1681731300000,
          "net": 114.72463336919661
        },
        {
          "open": 1681738260000,
          "close": 1681817580000,
          "net": -135.372337535765
        },
        {
          "open": 1681939380000,
          "close": 1681993080000,
          "net": 94.3184186218633
        },
        {
          "open": 1682919780000,
          "close": 1682974680000,
          "net": 109.1902970372364
        },
        {
          "open": 1683510240000,
          "close": 1683535680000,
          "net": 122.92869488272761
        },
        {
          "open": 1685542800000,
          "close": 1685666340000,
          "net": 117.75592130673289
        },
        {
          "open": 1688558940000,
          "close": 1688628240000,
          "net": -135.84968015260262
        },
        {
          "open": 1688688180000,
          "close": 1688961600000,
          "net": -68.08607026239008
        },
        {
          "open": 1695598080000,
          "close": 1695601380000,
          "net": 87.16025863395146
        },
        {
          "open": 1696963800000,
          "close": 1696996860000,
          "net": 121.38097264859763
        },
        {
          "open": 1699359180000,
          "close": 1699380420000,
          "net": -127.0686802612028
        },
        {
          "open": 1699921080000,
          "close": 1699976040000,
          "net": 151.5419542156368
        },
        {
          "open": 1699987440000,
          "close": 1699988040000,
          "net": 86.86193708051564
        },
        {
          "open": 1701082740000,
          "close": 1701186240000,
          "net": -109.57772511688809
        },
        {
          "open": 1702310880000,
          "close": 1702319400000,
          "net": 85.23504311393661
        },
        {
          "open": 1703583960000,
          "close": 1703612400000,
          "net": 106.74886265361508
        },
        {
          "open": 1703780880000,
          "close": 1703860740000,
          "net": -139.24318872123155
        },
        {
          "open": 1705076220000,
          "close": 1705097100000,
          "net": 137.71754622531765
        },
        {
          "open": 1708517280000,
          "close": 1708559220000,
          "net": -143.23018730299736
        },
        {
          "open": 1710432900000,
          "close": 1710462360000,
          "net": -141.78805689152276
        },
        {
          "open": 1710624000000,
          "close": 1710832620000,
          "net": 121.05890892804017
        },
        {
          "open": 1710837060000,
          "close": 1710912240000,
          "net": 95.51484392831306
        },
        {
          "open": 1711113780000,
          "close": 1711212300000,
          "net": -144.23185645015255
        },
        {
          "open": 1711982160000,
          "close": 1712025420000,
          "net": 150.03088004282768
        },
        {
          "open": 1712682480000,
          "close": 1712778780000,
          "net": -142.25026482369498
        },
        {
          "open": 1716494460000,
          "close": 1716573840000,
          "net": -153.76855003947068
        },
        {
          "open": 1716998640000,
          "close": 1717043640000,
          "net": -150.2788768155349
        },
        {
          "open": 1717171620000,
          "close": 1717329060000,
          "net": -148.7131598543416
        },
        {
          "open": 1718080020000,
          "close": 1718099520000,
          "net": 72.67633439533141
        },
        {
          "open": 1721880540000,
          "close": 1721945160000,
          "net": -151.0935311278434
        },
        {
          "open": 1722298860000,
          "close": 1722457140000,
          "net": 160.83966881555133
        },
        {
          "open": 1722473280000,
          "close": 1722526320000,
          "net": 102.43226762486208
        },
        {
          "open": 1724762700000,
          "close": 1724794680000,
          "net": 157.50805109190662
        },
        {
          "open": 1726446960000,
          "close": 1726497300000,
          "net": 188.9931909101893
        },
        {
          "open": 1726506780000,
          "close": 1726566900000,
          "net": -151.8691277546201
        },
        {
          "open": 1727717580000,
          "close": 1727795040000,
          "net": 85.36811242426629
        },
        {
          "open": 1729667580000,
          "close": 1729702500000,
          "net": 149.87064848163902
        },
        {
          "open": 1730407740000,
          "close": 1730469420000,
          "net": -149.84875366408687
        },
        {
          "open": 1730641620000,
          "close": 1730757180000,
          "net": 122.9874969520846
        },
        {
          "open": 1732562640000,
          "close": 1732609380000,
          "net": 119.90750265990032
        },
        {
          "open": 1733144100000,
          "close": 1733150100000,
          "net": -162.59616689442916
        },
        {
          "open": 1733767200000,
          "close": 1733778300000,
          "net": 156.16792483321944
        },
        {
          "open": 1733848320000,
          "close": 1733906640000,
          "net": -165.49359901262073
        },
        {
          "open": 1734552240000,
          "close": 1734566340000,
          "net": 165.662223881874
        },
        {
          "open": 1734573540000,
          "close": 1734632400000,
          "net": 90.80792905740498
        },
        {
          "open": 1736271540000,
          "close": 1736336040000,
          "net": 124.66227729413733
        },
        {
          "open": 1737606120000,
          "close": 1737642960000,
          "net": -162.8935186898104
        },
        {
          "open": 1737938880000,
          "close": 1737956400000,
          "net": 135.07545327585257
        },
        {
          "open": 1738354980000,
          "close": 1738466940000,
          "net": 174.49998695832295
        },
        {
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 129.4465057750622
        },
        {
          "open": 1748562540000,
          "close": 1748656560000,
          "net": 124.76250339036808
        },
        {
          "open": 1749735180000,
          "close": 1749749220000,
          "net": -180.45003475028062
        },
        {
          "open": 1749759300000,
          "close": 1749772980000,
          "net": 180.96447969419194
        },
        {
          "open": 1751380860000,
          "close": 1751419080000,
          "net": 161.67159159285933
        },
        {
          "open": 1751646060000,
          "close": 1751689860000,
          "net": -155.11539947633239
        },
        {
          "open": 1752552600000,
          "close": 1752587040000,
          "net": -148.63211373572963
        },
        {
          "open": 1753427460000,
          "close": 1753559340000,
          "net": -181.7598357825994
        },
        {
          "open": 1753807020000,
          "close": 1753858260000,
          "net": -132.2349582131597
        },
        {
          "open": 1753993080000,
          "close": 1754009520000,
          "net": 173.7095492334555
        },
        {
          "open": 1755188880000,
          "close": 1755460800000,
          "net": -14.031463950000001
        },
        {
          "open": 1758305580000,
          "close": 1758520800000,
          "net": 196.40912443129474
        },
        {
          "open": 1759854240000,
          "close": 1759921920000,
          "net": -185.53837413947866
        },
        {
          "open": 1760115060000,
          "close": 1760124120000,
          "net": 125.81649167587857
        },
        {
          "open": 1761700920000,
          "close": 1761724500000,
          "net": -183.9431781803636
        },
        {
          "open": 1761754080000,
          "close": 1761763200000,
          "net": 156.39613087814507
        }
      ],
      "newEntries": 96,
      "retainedEntrySameExitTime": 0
    },
    "SPY-USDT:long": {
      "baseline": 19,
      "candidate": 19,
      "retainedEntries": 19,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 19
    },
    "PAXG-USDT:long": {
      "baseline": 38,
      "candidate": 38,
      "retainedEntries": 38,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 38
    }
  }
}
```