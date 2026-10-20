# BTC R1 exact audit batch1

Job ad66331f9c894766a156a4b6cd75d216, executed-fill + UTC daily MTM reconstruction, all six audited successfully. Source price anchor checks and terminal closures reconciled. Full61months/19quarters and partial63/21 shown. Stress costs same fills, not re-simulated executions or funding. Group cohorts by exit year are not calendar MTM.

```json
{
  "E01B": {
    "n": 202,
    "net": 8869.02621437949,
    "gross_before_fees": 10180.966938133226,
    "fees": 1311.9407237537362,
    "pf_from_trades": 1.778827671493305,
    "PF_engine": 1.778827671493305,
    "sharpe_engine": 1.2980448365292816,
    "cagr_engine": 12.950827844275281,
    "dd_engine": -7.512178630122179,
    "plus5_samefills": 8140.170256738529,
    "plus10_samefills": 7411.314299097565,
    "exbest": 7036.393742556584,
    "ex3best": 4926.8647514943805,
    "ex3best_plus10_samefills": 3501.230846748641,
    "time_any_position_pct": 34.41649150464179,
    "entry_notional_time_initial_equity": 0.3577197553195312,
    "entry_turnover_initial_equity": 145.4170621949121,
    "two_side_turnover_initial_equity": 291.54238305638603,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4667.457357937866,
        "fees": 133.15494392183686,
        "plus10": 4519.507420246935,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05051637201508875
      },
      "BTC-USDT:short": {
        "n": 121,
        "net": 931.4863650859675,
        "fees": 617.7037711721321,
        "plus10": 245.14884156137552,
        "time_open_pct": 5.411703742628598,
        "entry_notional_time_initial_equity": 0.027430917181145712
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1641.7707565439375,
        "fees": 402.07506906132244,
        "plus10": 1195.020679809135,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17269687289856314
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1628.3117348117216,
        "fees": 159.00693959844457,
        "plus10": 1451.637357480116,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10707559322473362
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 152,
        "net": 5598.943723023831,
        "fees": 750.8587150939693
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1641.7707565439375,
        "fees": 402.07506906132244
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1628.3117348117216,
        "fees": 159.00693959844457
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
        "n": 43,
        "net": 1614.6918853450438,
        "by_symbol": {
          "BTC-USDT": 1487.3210755859832,
          "PAXG-USDT": -243.26424643361068,
          "SPY-USDT": 370.6350561926713
        }
      },
      "2022": {
        "n": 24,
        "net": 375.4822229209399,
        "by_symbol": {
          "BTC-USDT": 606.1869609803175,
          "PAXG-USDT": -113.54925800096672,
          "SPY-USDT": -117.15548005841087
        }
      },
      "2023": {
        "n": 36,
        "net": 1962.8761109008726,
        "by_symbol": {
          "BTC-USDT": 2041.2523581385249,
          "PAXG-USDT": -241.3054267098598,
          "SPY-USDT": 162.92917947220747
        }
      },
      "2024": {
        "n": 46,
        "net": 2420.8798757411105,
        "by_symbol": {
          "BTC-USDT": 859.4184377004666,
          "PAXG-USDT": 1058.8888174258595,
          "SPY-USDT": 502.5726206147839
        }
      },
      "2025": {
        "n": 42,
        "net": 2019.2834892732558,
        "by_symbol": {
          "BTC-USDT": 263.0017236243307,
          "PAXG-USDT": 1181.0008702625148,
          "SPY-USDT": 575.2808953864103
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 45,
      "STOP": 121
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4800.6123018597,
        "exbest": 2834.8248861149627,
        "ex3best": 1009.0217867409001,
        "ex3best_plus10": 878.6833975323868,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1922.7064362470924,
            "plus10": 1907.465519576467
          },
          "2022": {
            "n": 4,
            "net": -165.94391838945174,
            "plus10": -176.42177546594144
          },
          "2023": {
            "n": 4,
            "net": 1768.0868355762618,
            "plus10": 1742.808915794572
          },
          "2024": {
            "n": 8,
            "net": 591.3087035420184,
            "plus10": 551.1191460893936
          },
          "2025": {
            "n": 6,
            "net": 61.134196937354375,
            "plus10": 12.746540993710937
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1549.1901362580963,
        "exbest": 742.7295442039408,
        "ex3best": 383.80467267227095,
        "ex3best_plus10": -262.5681882601126,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 30,
            "net": -435.38536066110896,
            "plus10": -528.4606308512446
          },
          "2022": {
            "n": 16,
            "net": 772.1308793697691,
            "plus10": 702.9699212152784
          },
          "2023": {
            "n": 21,
            "net": 273.1655225622631,
            "plus10": 132.82438333082027
          },
          "2024": {
            "n": 28,
            "net": 268.1097341584486,
            "plus10": 95.85124136219156
          },
          "2025": {
            "n": 19,
            "net": 201.86752668697622,
            "plus10": 10.606841930803682
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2043.845825605259,
        "exbest": 613.6639433005716,
        "ex3best": -904.7108600825546,
        "ex3best_plus10": -1318.8232728602638,
        "years": {
          "2021": {
            "n": 6,
            "net": -243.2642464336107,
            "plus10": -286.5178330313629
          },
          "2022": {
            "n": 3,
            "net": -113.54925800096673,
            "plus10": -138.00397589501858
          },
          "2023": {
            "n": 7,
            "net": -241.3054267098598,
            "plus10": -340.0547751032819
          },
          "2024": {
            "n": 7,
            "net": 1058.8888174258595,
            "plus10": 988.2051212538693
          },
          "2025": {
            "n": 15,
            "net": 1181.0008702625155,
            "plus10": 971.3921425849285
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1787.3186744101658,
        "exbest": 882.3643207612074,
        "ex3best": 216.1876841698574,
        "ex3best_plus10": 83.8301252673663,
        "years": {
          "2020": {
            "n": 1,
            "net": 134.04946320405904,
            "plus10": 130.45633254926236
          },
          "2021": {
            "n": 1,
            "net": 370.6350561926713,
            "plus10": 360.20145512399404
          },
          "2022": {
            "n": 1,
            "net": -117.15548005841087,
            "plus10": -123.63102658832013
          },
          "2023": {
            "n": 4,
            "net": 162.92917947220747,
            "plus10": 97.96776716813457
          },
          "2024": {
            "n": 3,
            "net": 502.5726206147839,
            "plus10": 446.84098063628613
          },
          "2025": {
            "n": 2,
            "net": 575.2808953864103,
            "plus10": 539.8018485907592
          }
        }
      }
    },
    "mtm": {
      "name": "E01B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 36,
        "win_months_all": 0.5901639344262295,
        "win_months_active": 0.631578947368421,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.5714285714285714,
      "win_months_active": 0.6101694915254238,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.043935167167247435
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.02968161486672516
      ],
      "daily_close_drawdown_pct": -7.502199249279206,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07722818943084277,
          "SPY-USDT": -0.05399272576099258
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07722818943084277,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.0354796880222028
        },
        "SPY-USDT": {
          "BTC-USDT": -0.05399272576099258,
          "PAXG-USDT": -0.0354796880222028,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.051311512385931124,
        "2021-12-31 00:00:00+00:00": 0.150040152048192,
        "2022-12-31 00:00:00+00:00": 0.03105595985992382,
        "2023-12-31 00:00:00+00:00": 0.1574585431608353,
        "2024-12-31 00:00:00+00:00": 0.16778036502354254,
        "2025-12-31 00:00:00+00:00": 0.11984061253733591
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
        "PAXG-USDT": -0.09170010797301156,
        "SPY-USDT": -0.06005316502637762
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.09170010797301156,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.046903711852584934
      },
      "SPY-USDT": {
        "BTC-USDT": -0.06005316502637762,
        "PAXG-USDT": -0.046903711852584934,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 3,
        "both_nonzero": 28,
        "both_negative_and_portfolio_negative": 3
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
        "portfolio_return": -0.043935167167247435,
        "contributions": {
          "BTC-USDT": -0.04393516716724733,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.0384179941811591,
        "contributions": {
          "BTC-USDT": -0.029356788860400544,
          "PAXG-USDT": -0.009061205320758629,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.01711802433746412,
        "contributions": {
          "BTC-USDT": -0.008002454343143324,
          "PAXG-USDT": -0.00911556999432082,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.013980069887065572,
        "contributions": {
          "BTC-USDT": -0.01409509596258852,
          "PAXG-USDT": -0.008662744030011934,
          "SPY-USDT": 0.008777770105534903
        }
      },
      {
        "month": "2023-11-30 00:00:00+00:00",
        "portfolio_return": -0.010513114439369309,
        "contributions": {
          "BTC-USDT": -0.010513114439369408,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009859583000204064,
        "contributions": {
          "BTC-USDT": -0.009859583000204192,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193289785775716,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193289785775794,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.00901590704146249,
        "contributions": {
          "BTC-USDT": -0.009015907041462481,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.006830161025010439,
        "contributions": {
          "BTC-USDT": 0.0026669467296931925,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009497107754703653
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006190055039593023,
        "contributions": {
          "BTC-USDT": 0.00322180826268023,
          "PAXG-USDT": -0.009411863302273338,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-06-07 00:00:00+00:00",
      "drawdown_pct": -7.502199249279206,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -878.2638956313394,
        "PAXG-USDT": -230.62738508100932,
        "SPY-USDT": -104.64725009108622
      }
    }
  },
  "E01C": {
    "n": 209,
    "net": 9028.417562861008,
    "gross_before_fees": 10431.414351964526,
    "fees": 1402.9967891035176,
    "pf_from_trades": 1.7581676246776599,
    "PF_engine": 1.7581676246776592,
    "sharpe_engine": 1.28889853670307,
    "cagr_engine": 13.133209548881176,
    "dd_engine": -8.168012803517167,
    "plus5_samefills": 8248.974902247943,
    "plus10_samefills": 7469.532241634873,
    "exbest": 7228.22106399072,
    "ex3best": 5083.425322989243,
    "ex3best_plus10_samefills": 3556.76971525415,
    "time_any_position_pct": 36.882553862322645,
    "entry_notional_time_initial_equity": 0.4068785014689445,
    "entry_turnover_initial_equity": 155.52097319681894,
    "two_side_turnover_initial_equity": 311.77706424522614,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4619.755851549879,
        "fees": 133.7105647603396,
        "plus10": 4471.188557371726,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05052334902810474
      },
      "BTC-USDT:short": {
        "n": 121,
        "net": 921.5679814489987,
        "fees": 618.5499365922917,
        "plus10": 234.29027412422974,
        "time_open_pct": 5.411703742628598,
        "entry_notional_time_initial_equity": 0.027478736963625516
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1692.3797700021405,
        "fees": 403.04314355380023,
        "plus10": 1244.5540549423629,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17370692347355368
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1794.7139598599856,
        "fees": 247.69314419708567,
        "plus10": 1519.499355196557,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.1551694920036605
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 152,
        "net": 5541.323832998875,
        "fees": 752.2605013526315
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1692.3797700021405,
        "fees": 403.04314355380023
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1794.7139598599856,
        "fees": 247.69314419708567
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
        "n": 45,
        "net": 1391.8747847940872,
        "by_symbol": {
          "BTC-USDT": 1470.2387039322425,
          "PAXG-USDT": -239.79890441855406,
          "SPY-USDT": 161.43498528039905
        }
      },
      "2022": {
        "n": 25,
        "net": 401.42662475398413,
        "by_symbol": {
          "BTC-USDT": 594.1347263895591,
          "PAXG-USDT": -111.05717230322162,
          "SPY-USDT": -81.65092933235327
        }
      },
      "2023": {
        "n": 38,
        "net": 2460.5116065574025,
        "by_symbol": {
          "BTC-USDT": 2003.5212014994704,
          "PAXG-USDT": -235.31566949872797,
          "SPY-USDT": 692.3060745566604
        }
      },
      "2024": {
        "n": 47,
        "net": 2384.622016243846,
        "by_symbol": {
          "BTC-USDT": 868.7492065164353,
          "PAXG-USDT": 1079.523727381127,
          "SPY-USDT": 436.3490823462828
        }
      },
      "2025": {
        "n": 43,
        "net": 1923.0174673369415,
        "by_symbol": {
          "BTC-USDT": 262.91682766696215,
          "PAXG-USDT": 1199.0277888415171,
          "SPY-USDT": 461.0728508284616
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 61,
      "STOP": 121
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4753.46641631022,
        "exbest": 2819.559352679596,
        "ex3best": 974.094031890645,
        "ex3best_plus10": 843.0364624984732,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1896.4281382645836,
            "plus10": 1881.315931732512
          },
          "2022": {
            "n": 4,
            "net": -163.06022549292155,
            "plus10": -173.3147759278708
          },
          "2023": {
            "n": 4,
            "net": 1736.6303343097597,
            "plus10": 1711.8911460078693
          },
          "2024": {
            "n": 8,
            "net": 600.2616591165709,
            "plus10": 559.2969033469165
          },
          "2025": {
            "n": 6,
            "net": 59.33084132729681,
            "plus10": 10.210278953564824
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1540.1179180412928,
        "exbest": 728.9850087923314,
        "ex3best": 365.605844753547,
        "ex3best_plus10": -281.0829579424902,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 30,
            "net": -426.18943433234125,
            "plus10": -518.0708978782069
          },
          "2022": {
            "n": 16,
            "net": 757.1949518824807,
            "plus10": 689.2726249252221
          },
          "2023": {
            "n": 21,
            "net": 266.89086718971055,
            "plus10": 129.03240449775353
          },
          "2024": {
            "n": 28,
            "net": 268.4875473998641,
            "plus10": 93.14101106505422
          },
          "2025": {
            "n": 19,
            "net": 203.58598633966562,
            "plus10": 9.558046940880843
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2095.422913555941,
        "exbest": 648.6684282344108,
        "ex3best": -897.2716477329675,
        "ex3best_plus10": -1311.9256658202407,
        "years": {
          "2021": {
            "n": 6,
            "net": -239.79890441855403,
            "plus10": -282.43222274058974
          },
          "2022": {
            "n": 3,
            "net": -111.05717230322162,
            "plus10": -135.0703898649728
          },
          "2023": {
            "n": 7,
            "net": -235.315669498728,
            "plus10": -331.88438548617296
          },
          "2024": {
            "n": 7,
            "net": 1079.523727381127,
            "plus10": 1007.6307693863388
          },
          "2025": {
            "n": 15,
            "net": 1199.027788841517,
            "plus10": 986.3102836477592
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2042.4071040570718,
        "exbest": 1041.20385189825,
        "ex3best": 17.55568646581088,
        "ex3best_plus10": -212.4611481422953,
        "years": {
          "2020": {
            "n": 1,
            "net": 125.20189618053519,
            "plus10": 121.60507371313459
          },
          "2021": {
            "n": 3,
            "net": 161.43498528039902,
            "plus10": 127.40108205620794
          },
          "2022": {
            "n": 2,
            "net": -81.65092933235327,
            "plus10": -94.66896547275027
          },
          "2023": {
            "n": 6,
            "net": 692.3060745566604,
            "plus10": 598.2767754356776
          },
          "2024": {
            "n": 4,
            "net": 436.3490823462827,
            "plus10": 366.2810878422828
          },
          "2025": {
            "n": 3,
            "net": 461.0728508284616,
            "plus10": 400.6043016220045
          }
        }
      }
    },
    "mtm": {
      "name": "E01C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 37,
        "win_months_all": 0.6065573770491803,
        "win_months_active": 0.6491228070175439,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.5873015873015873,
      "win_months_active": 0.6271186440677966,
      "win_quarters": 0.8095238095238095,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.046955269279550294
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.03829863262349764
      ],
      "daily_close_drawdown_pct": -8.227718310465637,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07788362467963511,
          "SPY-USDT": -0.10158759569934256
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07788362467963511,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.02107140533279533
        },
        "SPY-USDT": {
          "BTC-USDT": -0.10158759569934256,
          "PAXG-USDT": 0.02107140533279533,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05042509079164881,
        "2021-12-31 00:00:00+00:00": 0.1289562627480143,
        "2022-12-31 00:00:00+00:00": 0.03385041284816226,
        "2023-12-31 00:00:00+00:00": 0.20068989626217837,
        "2024-12-31 00:00:00+00:00": 0.1619902156938462,
        "2025-12-31 00:00:00+00:00": 0.1124216596278349
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
        "PAXG-USDT": -0.09236358466796092,
        "SPY-USDT": -0.11208522743556568
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.09236358466796092,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.014362950761305058
      },
      "SPY-USDT": {
        "BTC-USDT": -0.11208522743556568,
        "PAXG-USDT": -0.014362950761305058,
        "SPY-USDT": 1
      }
    },
    "co_loss_complete_months": {
      "BTC-USDT__PAXG-USDT": {
        "both_negative": 3,
        "both_nonzero": 28,
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
        "portfolio_return": -0.046955269279550294,
        "contributions": {
          "BTC-USDT": -0.029391691171712853,
          "PAXG-USDT": -0.009055148703179779,
          "SPY-USDT": -0.008508429404657713
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.04389147505951252,
        "contributions": {
          "BTC-USDT": -0.04389147505951241,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017094273932338422,
        "contributions": {
          "BTC-USDT": -0.007978684721582665,
          "PAXG-USDT": -0.009115589210755694,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.014215045886934563,
        "contributions": {
          "BTC-USDT": -0.014094468830072693,
          "PAXG-USDT": -0.008662749009096683,
          "SPY-USDT": 0.008542171952234749
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009927079724370902,
        "contributions": {
          "BTC-USDT": -0.009927079724370774,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193175021420918,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193175021420974,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.008964226865126546,
        "contributions": {
          "BTC-USDT": -0.008964226865126518,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.00685293330300818,
        "contributions": {
          "BTC-USDT": 0.002643552775068677,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009496486078076932
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006283439156724024,
        "contributions": {
          "BTC-USDT": 0.003128392411492799,
          "PAXG-USDT": -0.009411831568216934,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.005662224201256949,
        "contributions": {
          "BTC-USDT": 0.0032759433426861728,
          "PAXG-USDT": -0.00893816754394309,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -8.227718310465637,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -662.7152627390869,
        "PAXG-USDT": -205.86733675573072,
        "SPY-USDT": -96.59635326563487
      }
    }
  },
  "P01B": {
    "n": 208,
    "net": 9186.892322591517,
    "gross_before_fees": 10566.61843970654,
    "fees": 1379.7261171150249,
    "pf_from_trades": 1.8255676741114495,
    "PF_engine": 1.8255676741114497,
    "sharpe_engine": 1.3470778681063797,
    "cagr_engine": 13.313322467772526,
    "dd_engine": -6.979598747156956,
    "plus5_samefills": 8420.37781308317,
    "plus10_samefills": 7653.863303574821,
    "exbest": 7347.772656178095,
    "ex3best": 5214.946586027389,
    "ex3best_plus10_samefills": 3714.178545719387,
    "time_any_position_pct": 33.78072633852981,
    "entry_notional_time_initial_equity": 0.36019660637059364,
    "entry_turnover_initial_equity": 152.96008968858456,
    "two_side_turnover_initial_equity": 306.60580380333886,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4687.808098373311,
        "fees": 134.94683559328493,
        "plus10": 4537.867169936327,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05118500932301301
      },
      "BTC-USDT:short": {
        "n": 127,
        "net": 1180.9660696715255,
        "fees": 674.2210193343388,
        "plus10": 431.83160374448227,
        "time_open_pct": 4.543702925205816,
        "entry_notional_time_initial_equity": 0.024901368152379567
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1669.903491565802,
        "fees": 408.4084301767841,
        "plus10": 1216.1163469249302,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.1753046195479979
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1648.2146629808765,
        "fees": 162.1498320106162,
        "plus10": 1468.0481829690807,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.1088056093472032
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 158,
        "net": 5868.774168044835,
        "fees": 809.1678549276238
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1669.903491565802,
        "fees": 408.4084301767841
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1648.2146629808765,
        "fees": 162.1498320106162
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 11,
        "net": 519.8478634586029,
        "by_symbol": {
          "BTC-USDT": 385.7048276336395,
          "PAXG-USDT": 0,
          "SPY-USDT": 134.14303582496333
        }
      },
      "2021": {
        "n": 44,
        "net": 1887.53516222375,
        "by_symbol": {
          "BTC-USDT": 1760.2236616882083,
          "PAXG-USDT": -248.29808643457392,
          "SPY-USDT": 375.60958697011586
        }
      },
      "2022": {
        "n": 24,
        "net": 216.8127483262379,
        "by_symbol": {
          "BTC-USDT": 453.98860239794016,
          "PAXG-USDT": -116.18758056428987,
          "SPY-USDT": -120.9882735074124
        }
      },
      "2023": {
        "n": 39,
        "net": 2301.3619859280543,
        "by_symbol": {
          "BTC-USDT": 2384.4007625200693,
          "PAXG-USDT": -247.97234013287436,
          "SPY-USDT": 164.93356354085978
        }
      },
      "2024": {
        "n": 47,
        "net": 1983.7741118984347,
        "by_symbol": {
          "BTC-USDT": 376.40089296299715,
          "PAXG-USDT": 1094.9973483649173,
          "SPY-USDT": 512.3758705705204
        }
      },
      "2025": {
        "n": 43,
        "net": 2277.560450756435,
        "by_symbol": {
          "BTC-USDT": 508.0554208419818,
          "PAXG-USDT": 1187.3641503326228,
          "SPY-USDT": 582.1408795818295
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 45,
      "STOP": 127
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4822.754933966595,
        "exbest": 2848.688431959886,
        "ex3best": 1003.2231111709355,
        "ex3best_plus10": 871.0176438850706,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1931.181196863252,
            "plus10": 1915.804536197521
          },
          "2022": {
            "n": 4,
            "net": -170.26869697164295,
            "plus10": -181.01409005004243
          },
          "2023": {
            "n": 4,
            "net": 1773.390301924053,
            "plus10": 1747.777922902531
          },
          "2024": {
            "n": 8,
            "net": 599.1092767500285,
            "plus10": 558.1966690381831
          },
          "2025": {
            "n": 6,
            "net": 64.23091578303064,
            "plus10": 15.313058589401805
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1855.187089005864,
        "exbest": 989.6584809397445,
        "ex3best": 625.3101210501359,
        "ex3best_plus10": -83.29201609501106,
        "years": {
          "2020": {
            "n": 7,
            "net": -104.46027639095034,
            "plus10": -124.73063406604834
          },
          "2021": {
            "n": 31,
            "net": -170.95753517504346,
            "plus10": -268.83716163596443
          },
          "2022": {
            "n": 16,
            "net": 624.2572993695833,
            "plus10": 553.0073078747649
          },
          "2023": {
            "n": 24,
            "net": 611.0104605960161,
            "plus10": 433.2305722205725
          },
          "2024": {
            "n": 29,
            "net": -222.70838378703107,
            "plus10": -403.9856641434568
          },
          "2025": {
            "n": 20,
            "net": 443.82450505895133,
            "plus10": 243.14718349461324
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2078.3119217425838,
        "exbest": 638.1618206488272,
        "ex3best": -919.6449921780126,
        "ex3best_plus10": -1340.3611890505163,
        "years": {
          "2021": {
            "n": 6,
            "net": -248.29808643457392,
            "plus10": -292.37154538288337
          },
          "2022": {
            "n": 3,
            "net": -116.18758056428986,
            "plus10": -141.3178373895791
          },
          "2023": {
            "n": 7,
            "net": -247.97234013287436,
            "plus10": -348.48596169250976
          },
          "2024": {
            "n": 7,
            "net": 1094.997348364917,
            "plus10": 1022.9733167765198
          },
          "2025": {
            "n": 15,
            "net": 1187.364150332622,
            "plus10": 975.3183746133826
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1810.3644949914924,
        "exbest": 893.3725647288713,
        "ex3best": 216.08336701701654,
        "ex3best_plus10": 80.91370375614062,
        "years": {
          "2020": {
            "n": 1,
            "net": 134.14303582496333,
            "plus10": 130.54739700158032
          },
          "2021": {
            "n": 1,
            "net": 375.60958697011586,
            "plus10": 365.03594985042696
          },
          "2022": {
            "n": 1,
            "net": -120.9882735074124,
            "plus10": -127.67567041176565
          },
          "2023": {
            "n": 4,
            "net": 164.93356354085975,
            "plus10": 98.44022059666446
          },
          "2024": {
            "n": 3,
            "net": 512.3758705705204,
            "plus10": 455.46147291799156
          },
          "2025": {
            "n": 2,
            "net": 582.1408795818295,
            "plus10": 546.238813014183
          }
        }
      }
    },
    "mtm": {
      "name": "P01B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.6842105263157895,
        "quarters_total": 19,
        "positive_quarters": 15,
        "win_quarters": 0.7894736842105263
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6610169491525424,
      "win_quarters": 0.7619047619047619,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.05413525346476744
      ],
      "worst_quarter": [
        "2023-09-30 00:00:00+00:00",
        -0.020793238239876555
      ],
      "daily_close_drawdown_pct": -6.969751657766077,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.1007715079647061,
          "SPY-USDT": -0.017373180982795795
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.1007715079647061,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03556682459735859
        },
        "SPY-USDT": {
          "BTC-USDT": -0.017373180982795795,
          "PAXG-USDT": -0.03556682459735859,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05572336017161472,
        "2021-12-31 00:00:00+00:00": 0.17524945395405966,
        "2022-12-31 00:00:00+00:00": 0.017474494651890105,
        "2023-12-31 00:00:00+00:00": 0.18229771045425558,
        "2024-12-31 00:00:00+00:00": 0.13291122139658373,
        "2025-12-31 00:00:00+00:00": 0.13469251582612962
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
        "PAXG-USDT": -0.11711383991155692,
        "SPY-USDT": -0.02344056536303093
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.11711383991155692,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.04697337968285576
      },
      "SPY-USDT": {
        "BTC-USDT": -0.02344056536303093,
        "PAXG-USDT": -0.04697337968285576,
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
        "portfolio_return": -0.05413525346476744,
        "contributions": {
          "BTC-USDT": -0.05413525346476749,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.02950283514019647,
        "contributions": {
          "BTC-USDT": -0.02035701047808079,
          "PAXG-USDT": -0.009145824662115717,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017131511608913796,
        "contributions": {
          "BTC-USDT": -0.008015893500938063,
          "PAXG-USDT": -0.009115618107975667,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.015213267982281953,
        "contributions": {
          "BTC-USDT": -0.015327928890793688,
          "PAXG-USDT": -0.008651953732870712,
          "SPY-USDT": 0.008766614641382457
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193243612323099,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193243612323102,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.007824495002687226,
        "contributions": {
          "BTC-USDT": -0.007824495002687162,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006014736546820498,
        "contributions": {
          "BTC-USDT": 0.0033972586965018417,
          "PAXG-USDT": -0.009411995243322365,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.005666171239088302,
        "contributions": {
          "BTC-USDT": 0.00327197131069554,
          "PAXG-USDT": -0.008938142549783772,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2025-06-30 00:00:00+00:00",
        "portfolio_return": -0.005012494959778735,
        "contributions": {
          "BTC-USDT": 0.00003919190157179754,
          "PAXG-USDT": -0.009194758199859881,
          "SPY-USDT": 0.004143071338509349
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.0036991775457581033,
        "contributions": {
          "BTC-USDT": 0.005827713790916035,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009526891336674118
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-06-07 00:00:00+00:00",
      "drawdown_pct": -6.969751657766077,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -802.2538071314766,
        "PAXG-USDT": -233.65999607602953,
        "SPY-USDT": -106.0257260699401
      }
    }
  },
  "P01C": {
    "n": 215,
    "net": 9342.08051433138,
    "gross_before_fees": 10815.166587673699,
    "fees": 1473.0860733423187,
    "pf_from_trades": 1.800962765548735,
    "PF_engine": 1.8009627655487348,
    "sharpe_engine": 1.3357741258053553,
    "cagr_engine": 13.488538642223546,
    "dd_engine": -7.014321226210174,
    "plus5_samefills": 8523.699362474536,
    "plus10_samefills": 7705.318210617688,
    "exbest": 7532.153223575315,
    "ex3best": 5384.094563824975,
    "ex3best_plus10_samefills": 3779.6714203086276,
    "time_any_position_pct": 36.283791673965084,
    "entry_notional_time_initial_equity": 0.41074034334226384,
    "entry_turnover_initial_equity": 163.31860817549745,
    "two_side_turnover_initial_equity": 327.3524607427373,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4637.541635149279,
        "fees": 135.7924569804584,
        "plus10": 4486.661127393213,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05126271349994927
      },
      "BTC-USDT:short": {
        "n": 127,
        "net": 1156.22787244991,
        "fees": 675.1334626744616,
        "plus10": 406.0795805893963,
        "time_open_pct": 4.543702925205816,
        "entry_notional_time_initial_equity": 0.02496582854400984
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1721.8618996790335,
        "fees": 409.41061490366206,
        "plus10": 1266.9612164527427,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17635686609719128
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1826.4491070531537,
        "fees": 252.74953878373663,
        "plus10": 1545.6162861823354,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.1581549352011136
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 158,
        "net": 5793.769507599187,
        "fees": 810.9259196549201
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1721.8618996790335,
        "fees": 409.41061490366206
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1826.4491070531537,
        "fees": 252.74953878373663
      }
    },
    "closed_trade_year_cohorts_NOT_MTM": {
      "2020": {
        "n": 11,
        "net": 511.4720278259998,
        "by_symbol": {
          "BTC-USDT": 386.18271759467035,
          "PAXG-USDT": 0,
          "SPY-USDT": 125.28931023132948
        }
      },
      "2021": {
        "n": 46,
        "net": 1664.5923958583603,
        "by_symbol": {
          "BTC-USDT": 1746.1093981481336,
          "PAXG-USDT": -244.41604973873376,
          "SPY-USDT": 162.8990474489607
        }
      },
      "2022": {
        "n": 25,
        "net": 248.32057301717464,
        "by_symbol": {
          "BTC-USDT": 446.6014381313918,
          "PAXG-USDT": -113.68094211198243,
          "SPY-USDT": -84.59992300223462
        }
      },
      "2023": {
        "n": 41,
        "net": 2811.726216640333,
        "by_symbol": {
          "BTC-USDT": 2341.8664024176137,
          "PAXG-USDT": -242.030617582576,
          "SPY-USDT": 711.8904318052959
        }
      },
      "2024": {
        "n": 48,
        "net": 1922.6915813437272,
        "by_symbol": {
          "BTC-USDT": 360.591376358849,
          "PAXG-USDT": 1116.953689029417,
          "SPY-USDT": 445.14651595546115
        }
      },
      "2025": {
        "n": 44,
        "net": 2183.2777196457823,
        "by_symbol": {
          "BTC-USDT": 512.4181749485309,
          "PAXG-USDT": 1205.0358200829085,
          "SPY-USDT": 465.8237246143413
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 61,
      "STOP": 127
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4773.334092129736,
        "exbest": 2827.614344393211,
        "ex3best": 982.1490236042595,
        "ex3best_plus10": 848.8346747254612,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1920.5018512907177,
            "plus10": 1905.198150789847
          },
          "2022": {
            "n": 4,
            "net": -168.26389690295719,
            "plus10": -178.80850402771185
          },
          "2023": {
            "n": 4,
            "net": 1745.1773979528143,
            "plus10": 1720.0849390473304
          },
          "2024": {
            "n": 8,
            "net": 587.7862474530777,
            "plus10": 546.0089733560077
          },
          "2025": {
            "n": 6,
            "net": 62.17493133103727,
            "plus10": 12.388494969008775
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1831.3613351243748,
        "exbest": 961.0941319434907,
        "ex3best": 590.744774592119,
        "ex3best_plus10": -118.14129137965077,
        "years": {
          "2020": {
            "n": 7,
            "net": -103.9823864299195,
            "plus10": -124.2379568143178
          },
          "2021": {
            "n": 31,
            "net": -174.3924531425838,
            "plus10": -270.74512248233185
          },
          "2022": {
            "n": 16,
            "net": 614.8653350343491,
            "plus10": 544.77750325196
          },
          "2023": {
            "n": 24,
            "net": 596.6890044647993,
            "plus10": 421.98853092892296
          },
          "2024": {
            "n": 29,
            "net": -227.19487109422928,
            "plus10": -411.86795645479015
          },
          "2025": {
            "n": 20,
            "net": 450.2432436174937,
            "plus10": 246.1645821599529
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2131.2725145826953,
        "exbest": 674.8876391624407,
        "ex3best": -911.5394746963847,
        "ex3best_plus10": -1332.832440062451,
        "years": {
          "2021": {
            "n": 6,
            "net": -244.4160497387337,
            "plus10": -287.83511469309383
          },
          "2022": {
            "n": 3,
            "net": -113.68094211198243,
            "plus10": -138.37362614874297
          },
          "2023": {
            "n": 7,
            "net": -242.03061758257599,
            "plus10": -340.3941214505253
          },
          "2024": {
            "n": 7,
            "net": 1116.9536890294173,
            "plus10": 1043.6450272871184
          },
          "2025": {
            "n": 15,
            "net": 1205.0358200829091,
            "plus10": 989.9190514579866
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2079.198645836891,
        "exbest": 1064.2115655430753,
        "ex3best": 15.604843442438494,
        "ex3best_plus10": -219.18938366598124,
        "years": {
          "2020": {
            "n": 1,
            "net": 125.28931023132948,
            "plus10": 121.68997651744257
          },
          "2021": {
            "n": 3,
            "net": 162.8990474489607,
            "plus10": 128.34672710668218
          },
          "2022": {
            "n": 2,
            "net": -84.59992300223462,
            "plus10": -98.01039465097544
          },
          "2023": {
            "n": 6,
            "net": 711.890431805296,
            "plus10": 615.5039050852693
          },
          "2024": {
            "n": 4,
            "net": 445.14651595546115,
            "plus10": 373.55155844130206
          },
          "2025": {
            "n": 3,
            "net": 465.82372461434136,
            "plus10": 404.53451368261494
          }
        }
      }
    },
    "mtm": {
      "name": "P01C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 39,
        "win_months_all": 0.639344262295082,
        "win_months_active": 0.6842105263157895,
        "quarters_total": 19,
        "positive_quarters": 14,
        "win_quarters": 0.7368421052631579
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.6190476190476191,
      "win_months_active": 0.6610169491525424,
      "win_quarters": 0.7142857142857143,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.054012181732322584
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.029468944066625147
      ],
      "daily_close_drawdown_pct": -7.004378337130223,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.10048023804238569,
          "SPY-USDT": -0.06402280766184645
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.10048023804238569,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.0211293213601649
        },
        "SPY-USDT": {
          "BTC-USDT": -0.06402280766184645,
          "PAXG-USDT": 0.0211293213601649,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05488417575072946,
        "2021-12-31 00:00:00+00:00": 0.15425605043501744,
        "2022-12-31 00:00:00+00:00": 0.020394157288963655,
        "2023-12-31 00:00:00+00:00": 0.22630707414385487,
        "2024-12-31 00:00:00+00:00": 0.1261930655678125,
        "2025-12-31 00:00:00+00:00": 0.12723951348878382
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
        "PAXG-USDT": -0.11680012944193045,
        "SPY-USDT": -0.07449425988079593
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.11680012944193045,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.014271042920601763
      },
      "SPY-USDT": {
        "BTC-USDT": -0.07449425988079593,
        "PAXG-USDT": -0.014271042920601763,
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
        "portfolio_return": -0.054012181732322584,
        "contributions": {
          "BTC-USDT": -0.05401218173232263,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.03811197242686881,
        "contributions": {
          "BTC-USDT": -0.020403949313117745,
          "PAXG-USDT": -0.009139401776780381,
          "SPY-USDT": -0.008568621336970658
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.01710408196460722,
        "contributions": {
          "BTC-USDT": -0.007988468390751142,
          "PAXG-USDT": -0.009115613573855975,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.015457478989528983,
        "contributions": {
          "BTC-USDT": -0.01533708168153008,
          "PAXG-USDT": -0.008651858068875183,
          "SPY-USDT": 0.008531460760876266
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193213658204469,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.00919321365820444,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.007856794972000203,
        "contributions": {
          "BTC-USDT": -0.007856794972000192,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006008265305757821,
        "contributions": {
          "BTC-USDT": 0.0034036848797104626,
          "PAXG-USDT": -0.009411950185468239,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.005663708234081244,
        "contributions": {
          "BTC-USDT": 0.003274421930509044,
          "PAXG-USDT": -0.008938130164590155,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2025-06-30 00:00:00+00:00",
        "portfolio_return": -0.0052072330797985344,
        "contributions": {
          "BTC-USDT": 0.000030506776238665538,
          "PAXG-USDT": -0.009194671745894986,
          "SPY-USDT": 0.003956931889857776
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.003792914945441539,
        "contributions": {
          "BTC-USDT": -0.003792914945441537,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-06-07 00:00:00+00:00",
      "drawdown_pct": -7.004378337130223,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -823.6866375859154,
        "PAXG-USDT": -238.51574845508918,
        "SPY-USDT": -108.20421042937778
      }
    }
  },
  "X01B": {
    "n": 206,
    "net": 9234.194391279198,
    "gross_before_fees": 10596.115222063538,
    "fees": 1361.9208307843405,
    "pf_from_trades": 1.796287003921919,
    "PF_engine": 1.7962870039219192,
    "sharpe_engine": 1.3239806209896494,
    "cagr_engine": 13.366850134409681,
    "dd_engine": -7.496635153613385,
    "plus5_samefills": 8477.57170751012,
    "plus10_samefills": 7720.949023741038,
    "exbest": 7417.779905932609,
    "ex3best": 5275.689175292896,
    "ex3best_plus10_samefills": 3794.723629782647,
    "time_any_position_pct": 34.4906434285047,
    "entry_notional_time_initial_equity": 0.36204638942146256,
    "entry_turnover_initial_equity": 150.98647327226607,
    "two_side_turnover_initial_equity": 302.6490735076313,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4663.021116968694,
        "fees": 134.29267887412925,
        "plus10": 4513.807029330772,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.05086836897580137
      },
      "BTC-USDT:short": {
        "n": 125,
        "net": 1256.556119305704,
        "fees": 660.8666762311436,
        "plus10": 522.2598123822113,
        "time_open_pct": 5.535813335668827,
        "entry_notional_time_initial_equity": 0.02876201701071935
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1669.7805103621536,
        "fees": 406.215739766758,
        "plus10": 1218.4296883990894,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.17427680317781127
      },
      "SPY-USDT:long": {
        "n": 12,
        "net": 1644.836644642646,
        "fees": 160.54573591230974,
        "plus10": 1466.4524936289686,
        "time_open_pct": 8.130765749985404,
        "entry_notional_time_initial_equity": 0.10813920025713068
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 156,
        "net": 5919.577236274396,
        "fees": 795.159355105273
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1669.7805103621536,
        "fees": 406.215739766758
      },
      "SPY-USDT": {
        "n": 12,
        "net": 1644.836644642646,
        "fees": 160.54573591230974
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
        "n": 43,
        "net": 1614.6918853450438,
        "by_symbol": {
          "BTC-USDT": 1487.3210755859832,
          "PAXG-USDT": -243.26424643361068,
          "SPY-USDT": 370.6350561926713
        }
      },
      "2022": {
        "n": 24,
        "net": 375.4822229209399,
        "by_symbol": {
          "BTC-USDT": 606.1869609803175,
          "PAXG-USDT": -113.54925800096672,
          "SPY-USDT": -117.15548005841087
        }
      },
      "2023": {
        "n": 39,
        "net": 2141.2346776080594,
        "by_symbol": {
          "BTC-USDT": 2222.7421859917226,
          "PAXG-USDT": -243.5959803821611,
          "SPY-USDT": 162.08847199849674
        }
      },
      "2024": {
        "n": 46,
        "net": 2453.9295284644713,
        "by_symbol": {
          "BTC-USDT": 873.2900868496109,
          "PAXG-USDT": 1071.9438049700266,
          "SPY-USDT": 508.69563664483337
        }
      },
      "2025": {
        "n": 43,
        "net": 2173.043446742414,
        "by_symbol": {
          "BTC-USDT": 388.27375987255334,
          "PAXG-USDT": 1198.2461902088653,
          "SPY-USDT": 586.5234966609964
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 36,
      "MARKET": 45,
      "STOP": 125
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4797.313795842824,
        "exbest": 2846.6066316221013,
        "ex3best": 1001.1413108331501,
        "ex3best_plus10": 869.5310048000192,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1922.7064362470924,
            "plus10": 1907.465519576467
          },
          "2022": {
            "n": 4,
            "net": -165.94391838945174,
            "plus10": -176.42177546594144
          },
          "2023": {
            "n": 4,
            "net": 1752.1170515568722,
            "plus10": 1726.9059772476546
          },
          "2024": {
            "n": 8,
            "net": 604.8982310442311,
            "plus10": 564.2462573405423
          },
          "2025": {
            "n": 6,
            "net": 59.078212485360126,
            "plus10": 9.821977373317026
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1917.4227955368447,
        "exbest": 1063.9731466490416,
        "ex3best": 700.0164735064259,
        "ex3best_plus10": 6.356583044365806,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 30,
            "net": -435.38536066110896,
            "plus10": -528.4606308512446
          },
          "2022": {
            "n": 16,
            "net": 772.1308793697691,
            "plus10": 702.9699212152784
          },
          "2023": {
            "n": 24,
            "net": 470.6251344348507,
            "plus10": 295.67489286141944
          },
          "2024": {
            "n": 28,
            "net": 268.39185580537986,
            "plus10": 93.85747553879531
          },
          "2025": {
            "n": 20,
            "net": 329.1955473871935,
            "plus10": 126.86106904443517
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2075.996250128911,
        "exbest": 628.7741789561767,
        "ex3best": -912.9778733626757,
        "ex3best_plus10": -1331.2238475523804,
        "years": {
          "2021": {
            "n": 6,
            "net": -243.2642464336107,
            "plus10": -286.5178330313629
          },
          "2022": {
            "n": 3,
            "net": -113.54925800096673,
            "plus10": -138.00397589501858
          },
          "2023": {
            "n": 7,
            "net": -243.5959803821611,
            "plus10": -342.51286629062884
          },
          "2024": {
            "n": 7,
            "net": 1071.9438049700263,
            "plus10": 1000.411832079741
          },
          "2025": {
            "n": 15,
            "net": 1198.2461902088648,
            "plus10": 985.0525315363584
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 1805.382380554956,
        "exbest": 884.3160191885586,
        "ex3best": 217.48143904618854,
        "ex3best_plus10": 83.81001762442565,
        "years": {
          "2020": {
            "n": 1,
            "net": 134.04946320405904,
            "plus10": 130.45633254926236
          },
          "2021": {
            "n": 1,
            "net": 370.6350561926713,
            "plus10": 360.20145512399404
          },
          "2022": {
            "n": 1,
            "net": -117.15548005841087,
            "plus10": -123.63102658832013
          },
          "2023": {
            "n": 4,
            "net": 162.08847199849671,
            "plus10": 96.7890968642871
          },
          "2024": {
            "n": 3,
            "net": 508.69563664483337,
            "plus10": 452.28496297175803
          },
          "2025": {
            "n": 2,
            "net": 586.5234966609964,
            "plus10": 550.3516727079872
          }
        }
      }
    },
    "mtm": {
      "name": "X01B",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 37,
        "win_months_all": 0.6065573770491803,
        "win_months_active": 0.6491228070175439,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.5873015873015873,
      "win_months_active": 0.6271186440677966,
      "win_quarters": 0.8095238095238095,
      "worst_month": [
        "2021-08-31 00:00:00+00:00",
        -0.043935167167247435
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.02968161486672516
      ],
      "daily_close_drawdown_pct": -7.486828490893293,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07742718225397774,
          "SPY-USDT": -0.05841069675301356
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07742718225397774,
          "PAXG-USDT": 1,
          "SPY-USDT": -0.03546616258289742
        },
        "SPY-USDT": {
          "BTC-USDT": -0.05841069675301356,
          "PAXG-USDT": -0.03546616258289742,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.051311512385931124,
        "2021-12-31 00:00:00+00:00": 0.150040152048192,
        "2022-12-31 00:00:00+00:00": 0.03105595985992382,
        "2023-12-31 00:00:00+00:00": 0.1717661603955667,
        "2024-12-31 00:00:00+00:00": 0.16799427204987905,
        "2025-12-31 00:00:00+00:00": 0.1273679280962139
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
        "PAXG-USDT": -0.0926537079234676,
        "SPY-USDT": -0.06480453570995955
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.0926537079234676,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.04688802119654246
      },
      "SPY-USDT": {
        "BTC-USDT": -0.06480453570995955,
        "PAXG-USDT": -0.04688802119654246,
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
        "portfolio_return": -0.043935167167247435,
        "contributions": {
          "BTC-USDT": -0.04393516716724733,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.0384179941811591,
        "contributions": {
          "BTC-USDT": -0.029356788860400544,
          "PAXG-USDT": -0.009061205320758629,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.01710078503999235,
        "contributions": {
          "BTC-USDT": -0.007985264355228944,
          "PAXG-USDT": -0.009115520684763425,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.013975266422752375,
        "contributions": {
          "BTC-USDT": -0.014090204741656934,
          "PAXG-USDT": -0.00866282411693078,
          "SPY-USDT": 0.00877776243583532
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009882143460111625,
        "contributions": {
          "BTC-USDT": -0.009882143460111632,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193289785775716,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193289785775794,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.00901590704146249,
        "contributions": {
          "BTC-USDT": -0.009015907041462481,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.006830161025010439,
        "contributions": {
          "BTC-USDT": 0.0026669467296931925,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009497107754703653
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006190055039593023,
        "contributions": {
          "BTC-USDT": 0.00322180826268023,
          "PAXG-USDT": -0.009411863302273338,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.005666942565455413,
        "contributions": {
          "BTC-USDT": 0.0032712177679581414,
          "PAXG-USDT": -0.008938160333413455,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2024-05-20 00:00:00+00:00",
      "trough": "2024-06-07 00:00:00+00:00",
      "drawdown_pct": -7.486828490893293,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -886.1204996328338,
        "PAXG-USDT": -233.43359289761935,
        "SPY-USDT": -105.91803263409201
      }
    }
  },
  "X01C": {
    "n": 213,
    "net": 9407.826225512972,
    "gross_before_fees": 10861.593642289721,
    "fees": 1453.76741677675,
    "pf_from_trades": 1.7764073161597513,
    "PF_engine": 1.7764073161597511,
    "sharpe_engine": 1.3154302129959166,
    "cagr_engine": 13.562426758782898,
    "dd_engine": -8.168012803517177,
    "plus5_samefills": 8600.177660637002,
    "plus10_samefills": 7792.529095761029,
    "exbest": 7620.604115823741,
    "ex3best": 5442.756352116708,
    "ex3best_plus10_samefills": 3859.9175243373616,
    "time_any_position_pct": 36.95670578618555,
    "entry_notional_time_initial_equity": 0.41184408813525536,
    "entry_turnover_initial_equity": 161.17792481160987,
    "two_side_turnover_initial_equity": 323.0594259503889,
    "by_group": {
      "BTC-USDT:long": {
        "n": 31,
        "net": 4618.732513139611,
        "fees": 134.90596125647824,
        "plus10": 4468.837000632415,
        "time_open_pct": 11.577443510246978,
        "entry_notional_time_initial_equity": 0.050880793951029804
      },
      "BTC-USDT:short": {
        "n": 125,
        "net": 1251.4936273012945,
        "fees": 661.421557996964,
        "plus10": 516.5807850824464,
        "time_open_pct": 5.535813335668827,
        "entry_notional_time_initial_equity": 0.028789326270889797
      },
      "PAXG-USDT:long": {
        "n": 38,
        "net": 1721.2570535973296,
        "fees": 407.3640667696651,
        "plus10": 1268.630312742147,
        "time_open_pct": 15.204866584924389,
        "entry_notional_time_initial_equity": 0.1753615213355421
      },
      "SPY-USDT:long": {
        "n": 19,
        "net": 1816.343031474734,
        "fees": 250.07583075364275,
        "plus10": 1538.4809973040194,
        "time_open_pct": 11.413265604017049,
        "entry_notional_time_initial_equity": 0.15681244657779367
      }
    },
    "by_symbol": {
      "BTC-USDT": {
        "n": 156,
        "net": 5870.226140440905,
        "fees": 796.3275192534423
      },
      "PAXG-USDT": {
        "n": 38,
        "net": 1721.2570535973296,
        "fees": 407.3640667696651
      },
      "SPY-USDT": {
        "n": 19,
        "net": 1816.343031474734,
        "fees": 250.07583075364275
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
        "n": 45,
        "net": 1391.8747847940872,
        "by_symbol": {
          "BTC-USDT": 1470.2387039322425,
          "PAXG-USDT": -239.79890441855406,
          "SPY-USDT": 161.43498528039905
        }
      },
      "2022": {
        "n": 25,
        "net": 401.42662475398413,
        "by_symbol": {
          "BTC-USDT": 594.1347263895591,
          "PAXG-USDT": -111.05717230322162,
          "SPY-USDT": -81.65092933235327
        }
      },
      "2023": {
        "n": 41,
        "net": 2643.4703457069663,
        "by_symbol": {
          "BTC-USDT": 2181.5975774639423,
          "PAXG-USDT": -237.62021450236603,
          "SPY-USDT": 699.4929827453907
        }
      },
      "2024": {
        "n": 47,
        "net": 2421.007960261222,
        "by_symbol": {
          "BTC-USDT": 886.4018915038351,
          "PAXG-USDT": 1092.894879266541,
          "SPY-USDT": 441.7111894908456
        }
      },
      "2025": {
        "n": 44,
        "net": 2083.081446821969,
        "by_symbol": {
          "BTC-USDT": 396.0900741571201,
          "PAXG-USDT": 1216.8384655549307,
          "SPY-USDT": 470.15290710991655
        }
      }
    },
    "entry_order_types": {
      "LIMIT": 27,
      "MARKET": 61,
      "STOP": 125
    },
    "audit": "passed",
    "group_stress": {
      "BTC-USDT:long": {
        "gross": 4753.638474396089,
        "exbest": 2831.5104034503743,
        "ex3best": 966.382861246536,
        "ex3best_plus10": 834.0081180114588,
        "years": {
          "2020": {
            "n": 3,
            "net": 490.1651040245898,
            "plus10": 481.78907325873286
          },
          "2021": {
            "n": 6,
            "net": 1896.4281382645836,
            "plus10": 1881.315931732512
          },
          "2022": {
            "n": 4,
            "net": -163.06022549292155,
            "plus10": -173.3147759278708
          },
          "2023": {
            "n": 4,
            "net": 1723.9041475856325,
            "plus10": 1699.2129933924525
          },
          "2024": {
            "n": 8,
            "net": 614.0204918824223,
            "plus10": 572.5480628434134
          },
          "2025": {
            "n": 6,
            "net": 57.2748568753062,
            "plus10": 7.285715333174494
          }
        }
      },
      "BTC-USDT:short": {
        "gross": 1912.9151852982625,
        "exbest": 1055.084502869997,
        "ex3best": 685.1268322656153,
        "ex3best_plus10": -8.41969638495334,
        "years": {
          "2020": {
            "n": 7,
            "net": -148.4019370303809,
            "plus10": -168.6429154264742
          },
          "2021": {
            "n": 30,
            "net": -426.18943433234125,
            "plus10": -518.0708978782069
          },
          "2022": {
            "n": 16,
            "net": 757.1949518824807,
            "plus10": 689.2726249252221
          },
          "2023": {
            "n": 24,
            "net": 457.69342987830925,
            "plus10": 285.8165356201498
          },
          "2024": {
            "n": 28,
            "net": 272.38139962141247,
            "plus10": 94.67049570882605
          },
          "2025": {
            "n": 20,
            "net": 338.8152172818138,
            "plus10": 133.53494213292902
          }
        }
      },
      "PAXG-USDT:long": {
        "gross": 2128.621120366995,
        "exbest": 664.1559105389277,
        "ex3best": -905.7170251615661,
        "ex3best_plus10": -1324.690523918426,
        "years": {
          "2021": {
            "n": 6,
            "net": -239.79890441855403,
            "plus10": -282.43222274058974
          },
          "2022": {
            "n": 3,
            "net": -111.05717230322162,
            "plus10": -135.0703898649728
          },
          "2023": {
            "n": 7,
            "net": -237.62021450236603,
            "plus10": -334.3597388810853
          },
          "2024": {
            "n": 7,
            "net": 1092.894879266541,
            "plus10": 1020.1050815179207
          },
          "2025": {
            "n": 15,
            "net": 1216.838465554931,
            "plus10": 1000.3875827108737
          }
        }
      },
      "SPY-USDT:long": {
        "gross": 2066.4188622283764,
        "exbest": 1047.9537746268563,
        "ex3best": 15.942469145224436,
        "ex3best_plus10": -216.14929743530948,
        "years": {
          "2020": {
            "n": 1,
            "net": 125.20189618053519,
            "plus10": 121.60507371313459
          },
          "2021": {
            "n": 3,
            "net": 161.43498528039902,
            "plus10": 127.40108205620794
          },
          "2022": {
            "n": 2,
            "net": -81.65092933235327,
            "plus10": -94.66896547275027
          },
          "2023": {
            "n": 6,
            "net": 699.4929827453905,
            "plus10": 604.8821416634312
          },
          "2024": {
            "n": 4,
            "net": 441.7111894908456,
            "plus10": 370.7761678138455
          },
          "2025": {
            "n": 3,
            "net": 470.15290710991655,
            "plus10": 408.48549753015084
          }
        }
      }
    },
    "mtm": {
      "name": "X01C",
      "method": "UTC day-close MTM from executed fills, right-edge inclusive",
      "partial_boundary_periods_included": true,
      "complete_periods": {
        "months_total": 61,
        "months_active": 57,
        "positive_months": 38,
        "win_months_all": 0.6229508196721312,
        "win_months_active": 0.6666666666666666,
        "quarters_total": 19,
        "positive_quarters": 16,
        "win_quarters": 0.8421052631578947
      },
      "months_total": 63,
      "months_active": 59,
      "win_months_all": 0.6031746031746031,
      "win_months_active": 0.6440677966101694,
      "win_quarters": 0.8095238095238095,
      "worst_month": [
        "2021-04-30 00:00:00+00:00",
        -0.046955269279550294
      ],
      "worst_quarter": [
        "2021-06-30 00:00:00+00:00",
        -0.03829863262349764
      ],
      "daily_close_drawdown_pct": -8.227718310465637,
      "mtm_route_contribution_correlation": {
        "BTC-USDT": {
          "BTC-USDT": 1,
          "PAXG-USDT": -0.07771894738387049,
          "SPY-USDT": -0.1003653284657363
        },
        "PAXG-USDT": {
          "BTC-USDT": -0.07771894738387049,
          "PAXG-USDT": 1,
          "SPY-USDT": 0.02105578446294732
        },
        "SPY-USDT": {
          "BTC-USDT": -0.1003653284657363,
          "PAXG-USDT": 0.02105578446294732,
          "SPY-USDT": 1
        }
      },
      "yearly_returns": {
        "2020-12-31 00:00:00+00:00": 0.05042509079164881,
        "2021-12-31 00:00:00+00:00": 0.1289562627480143,
        "2022-12-31 00:00:00+00:00": 0.03385041284816226,
        "2023-12-31 00:00:00+00:00": 0.2156127969639383,
        "2024-12-31 00:00:00+00:00": 0.16244301612112677,
        "2025-12-31 00:00:00+00:00": 0.120237352609321
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
        "PAXG-USDT": -0.0929486084491788,
        "SPY-USDT": -0.11139265076360075
      },
      "PAXG-USDT": {
        "BTC-USDT": -0.0929486084491788,
        "PAXG-USDT": 1,
        "SPY-USDT": -0.014376252351834047
      },
      "SPY-USDT": {
        "BTC-USDT": -0.11139265076360075,
        "PAXG-USDT": -0.014376252351834047,
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
        "month": "2021-04-30 00:00:00+00:00",
        "portfolio_return": -0.046955269279550294,
        "contributions": {
          "BTC-USDT": -0.029391691171712853,
          "PAXG-USDT": -0.009055148703179779,
          "SPY-USDT": -0.008508429404657713
        }
      },
      {
        "month": "2021-08-31 00:00:00+00:00",
        "portfolio_return": -0.04389147505951252,
        "contributions": {
          "BTC-USDT": -0.04389147505951241,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-03-31 00:00:00+00:00",
        "portfolio_return": -0.017075133975382628,
        "contributions": {
          "BTC-USDT": -0.007959605627139536,
          "PAXG-USDT": -0.009115528348243175,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-07-31 00:00:00+00:00",
        "portfolio_return": -0.014214382366409484,
        "contributions": {
          "BTC-USDT": -0.014093795852005573,
          "PAXG-USDT": -0.008662717044692032,
          "SPY-USDT": 0.008542130530287989
        }
      },
      {
        "month": "2024-06-30 00:00:00+00:00",
        "portfolio_return": -0.009943338559720405,
        "contributions": {
          "BTC-USDT": -0.009943338559720358,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-09-30 00:00:00+00:00",
        "portfolio_return": -0.009193175021420918,
        "contributions": {
          "BTC-USDT": 0,
          "PAXG-USDT": -0.009193175021420974,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2021-03-31 00:00:00+00:00",
        "portfolio_return": -0.008964226865126546,
        "contributions": {
          "BTC-USDT": -0.008964226865126518,
          "PAXG-USDT": 0,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2022-11-30 00:00:00+00:00",
        "portfolio_return": -0.00685293330300818,
        "contributions": {
          "BTC-USDT": 0.002643552775068677,
          "PAXG-USDT": 0,
          "SPY-USDT": -0.009496486078076932
        }
      },
      {
        "month": "2022-02-28 00:00:00+00:00",
        "portfolio_return": -0.006283439156724024,
        "contributions": {
          "BTC-USDT": 0.003128392411492799,
          "PAXG-USDT": -0.009411831568216934,
          "SPY-USDT": 0
        }
      },
      {
        "month": "2023-09-30 00:00:00+00:00",
        "portfolio_return": -0.0056638553360971455,
        "contributions": {
          "BTC-USDT": 0.0032742676462299268,
          "PAXG-USDT": -0.008938122982326973,
          "SPY-USDT": 0
        }
      }
    ],
    "daily_drawdown_episode": {
      "peak": "2021-03-13 00:00:00+00:00",
      "trough": "2021-06-17 00:00:00+00:00",
      "drawdown_pct": -8.227718310465637,
      "route_pnl_delta_USDT": {
        "BTC-USDT": -662.7152627390869,
        "PAXG-USDT": -205.86733675573072,
        "SPY-USDT": -96.59635326563487
      }
    }
  }
}
```

## Execution path comparisons
Open timestamps matched within each symbol/side; quantities and portfolio capital are endogenous.

```json
{
  "E01B": {
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
      "candidate": 121,
      "retainedEntries": 120,
      "displaced": [
        {
          "open": 1673011800000,
          "close": 1673011860000,
          "net": -107.21330997518993
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 156.5636619391465
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
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 127.9920506539941
        }
      ],
      "newEntries": 1,
      "retainedEntrySameExitTime": 120
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
  "E01C": {
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
      "candidate": 121,
      "retainedEntries": 120,
      "displaced": [
        {
          "open": 1673011800000,
          "close": 1673011860000,
          "net": -105.45210570455028
        },
        {
          "open": 1675872900000,
          "close": 1675912020000,
          "net": 154.05002516489415
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
          "open": 1743159360000,
          "close": 1743241500000,
          "net": 129.4465057750622
        }
      ],
      "newEntries": 1,
      "retainedEntrySameExitTime": 120
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
  "P01B": {
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
      "candidate": 127,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 2,
      "retainedEntrySameExitTime": 75
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
  "P01C": {
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
      "candidate": 127,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 2,
      "retainedEntrySameExitTime": 75
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
  "X01B": {
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
      "candidate": 125,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 125
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
  "X01C": {
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
      "candidate": 125,
      "retainedEntries": 125,
      "displaced": [],
      "newEntries": 0,
      "retainedEntrySameExitTime": 125
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