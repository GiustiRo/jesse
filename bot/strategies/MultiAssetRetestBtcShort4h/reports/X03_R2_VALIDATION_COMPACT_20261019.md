# X03 R2 validation final compact audit

V are sensitivity only, never economic selection. All figuresUSDT. Cost+5/+10 overlay fixed executed paths/quantities; nominalfee.00045per side. ReferencewithoutX03: B9234.194391,C9407.826226 nominal; +10 B7720.949024,C7792.529096. B/C dependent development,2026closed. MTM61complete months/19Q; inclusive63/21. Delay4h is strong timing stress, not minute latency. Values from root fully reconciled audits.

```json
[
  {
    "id": "V201",
    "family": "validation",
    "change": "Horizon8 replaces12 jointly in return comparison, q-window and HLC3 VWAP; min10closedbars, sourceATR unchanged.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V201B",
        "url": "http://localhost:9200/#/backtest/dc09487b-eb8a-44c3-97c4-4b2acfeab83f",
        "n": 294,
        "net": 9748.30676532474,
        "cagr": 13.941869913831928,
        "dd_engine": -10.769248655750928,
        "dd_dayclose": -10.759703114362773,
        "pf": 1.525697316754195,
        "sharpe": 1.2720340903848035,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 13,
          "win_quarters": 0.6842105263157895
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.6666666666666666
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 8655.858583166619,
          "extra_cost": 1092.4481821581232,
          "samefills_cagr_pct": 12.704957052879283,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.639344262295082,
            "quarters_total": 19,
            "positive_quarters": 12,
            "win_quarters": 0.631578947368421
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 13,
            "win_quarters": 0.6190476190476191
          },
          "daily_close_drawdown_pct": -11.60720835546588,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.05447514466067571
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.06817725980500988,
            "2021-12-31 00:00:00+00:00": 0.1973629917456774,
            "2022-12-31 00:00:00+00:00": 0.06607972155016273,
            "2023-12-31 00:00:00+00:00": 0.14493216981268753,
            "2024-12-31 00:00:00+00:00": 0.0840288350127889,
            "2025-12-31 00:00:00+00:00": 0.10239137555152289
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2023-03-31 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 7563.410401008496,
          "extra_cost": 2184.8963643162465,
          "samefills_cagr_pct": 11.40804894143972,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 38,
            "win_months_all": 0.6229508196721312,
            "win_months_active": 0.6229508196721312,
            "quarters_total": 19,
            "positive_quarters": 11,
            "win_quarters": 0.5789473684210527
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 38,
            "win_months_all": 0.6031746031746031,
            "win_months_active": 0.6031746031746031,
            "quarters_total": 21,
            "positive_quarters": 12,
            "win_quarters": 0.5714285714285714
          },
          "daily_close_drawdown_pct": -12.513223888355817,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.05580351391420868
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.06618562031256592,
            "2021-12-31 00:00:00+00:00": 0.1884893387432982,
            "2022-12-31 00:00:00+00:00": 0.057615491945997244,
            "2023-12-31 00:00:00+00:00": 0.12757036314680037,
            "2024-12-31 00:00:00+00:00": 0.07088625660439929,
            "2025-12-31 00:00:00+00:00": 0.08534032000385339
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2023-03-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -2314.712474867426,
        "plus10_delta_noX03": -157.53862273253617,
        "supplement": {
          "n": 100,
          "net": 353.67168658495126,
          "fees": 615.6540255995171,
          "gross": 969.3257121844692,
          "plus10": -330.3883418589563,
          "exbest": 1.059142094417382,
          "ex3": -665.7466034297502,
          "ex3_plus10": -1318.955207659558,
          "year_net": {
            "2020": 177.46350267019204,
            "2021": 844.4600444919893,
            "2022": 479.91419899930384,
            "2023": -1.2242167865217226,
            "2024": -701.2593891925133,
            "2025": -445.6824535974985
          }
        },
        "ex3best_plus10": 3358.697817770244,
        "exposure": {
          "time_any_position_pct": 39.26716587843755,
          "entry_notional_time_initial_equity": 0.41970629342250154,
          "two_side_turnover_initial_equity": 436.9792728632491
        },
        "path_check": {
          "counts": {
            "current": 294,
            "reference": 273,
            "retained": 214,
            "removed": 59,
            "added": 80
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 214,
          "identical_to_N201": null
        }
      },
      {
        "name": "V201C",
        "url": "http://localhost:9200/#/backtest/7f1c089a-2751-43fc-989d-8922c09d92a5",
        "n": 301,
        "net": 9928.65929944254,
        "cagr": 14.140723254859267,
        "dd_engine": -10.6994668447837,
        "dd_dayclose": -10.697213442071074,
        "pf": 1.5197980203172834,
        "sharpe": 1.2642622075433985,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.7142857142857143
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 8781.866076113201,
          "extra_cost": 1146.7932233293407,
          "samefills_cagr_pct": 12.850568678996478,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 38,
            "win_months_all": 0.6229508196721312,
            "win_months_active": 0.6229508196721312,
            "quarters_total": 19,
            "positive_quarters": 12,
            "win_quarters": 0.631578947368421
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 38,
            "win_months_all": 0.6031746031746031,
            "win_months_active": 0.6031746031746031,
            "quarters_total": 21,
            "positive_quarters": 13,
            "win_quarters": 0.6190476190476191
          },
          "daily_close_drawdown_pct": -11.572645460608355,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.05458168393741325
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.06726071675988132,
            "2021-12-31 00:00:00+00:00": 0.1756730623930176,
            "2022-12-31 00:00:00+00:00": 0.06869968747630661,
            "2023-12-31 00:00:00+00:00": 0.1874081323710748,
            "2024-12-31 00:00:00+00:00": 0.07784743210069967,
            "2025-12-31 00:00:00+00:00": 0.09438127789162709
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2023-03-31 00:00:00+00:00",
            "2024-08-31 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 7635.072852783862,
          "extra_cost": 2293.5864466586813,
          "samefills_cagr_pct": 11.495092884664725,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 37,
            "win_months_all": 0.6065573770491803,
            "win_months_active": 0.6065573770491803,
            "quarters_total": 19,
            "positive_quarters": 12,
            "win_quarters": 0.631578947368421
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 37,
            "win_months_all": 0.5873015873015873,
            "win_months_active": 0.5873015873015873,
            "quarters_total": 21,
            "positive_quarters": 13,
            "win_quarters": 0.6190476190476191
          },
          "daily_close_drawdown_pct": -12.510137556602906,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.05597306822149406
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.06527051966707575,
            "2021-12-31 00:00:00+00:00": 0.16574043477126787,
            "2022-12-31 00:00:00+00:00": 0.06001514210028858,
            "2023-12-31 00:00:00+00:00": 0.16975761665347067,
            "2024-12-31 00:00:00+00:00": 0.06412297358853958,
            "2025-12-31 00:00:00+00:00": 0.0762563300825485
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2023-03-31 00:00:00+00:00",
            "2024-08-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -2306.9391714869944,
        "plus10_delta_noX03": -157.45624297716586,
        "supplement": {
          "n": 100,
          "net": 309.8048934874902,
          "fees": 616.6369904472292,
          "gross": 926.4418839347207,
          "plus10": -375.3473181205423,
          "exbest": -47.91797773479172,
          "ex3": -731.1698045017082,
          "ex3_plus10": -1384.8264663561213,
          "year_net": {
            "2020": 176.67125489041442,
            "2021": 827.9902991622121,
            "2022": 472.6518851044266,
            "2023": -0.16774469699004158,
            "2024": -720.7543195930328,
            "2025": -446.58648137953963
          }
        },
        "ex3best_plus10": 3426.533612491864,
        "exposure": {
          "time_any_position_pct": 41.45552344251766,
          "entry_notional_time_initial_equity": 0.47306396038332926,
          "two_side_turnover_initial_equity": 458.7172893317365
        },
        "path_check": {
          "counts": {
            "current": 301,
            "reference": 280,
            "retained": 221,
            "removed": 59,
            "added": 80
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 221,
          "identical_to_N201": null
        }
      }
    ]
  },
  {
    "id": "V202",
    "family": "validation",
    "change": "Horizon16 replaces12 jointly; min18closedbars.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V202B",
        "url": "http://localhost:9200/#/backtest/ad180c10-f055-4b12-8432-e369caac8c3a",
        "n": 252,
        "net": 12393.828082449885,
        "cagr": 16.72273680062457,
        "dd_engine": -7.5141067541671935,
        "dd_dayclose": -7.504137840978153,
        "pf": 1.879067166372935,
        "sharpe": 1.552495487450195,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 43,
          "win_months_all": 0.7049180327868853,
          "win_months_active": 0.7049180327868853,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6825396825396826,
          "win_months_all": 0.6825396825396826,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 11431.035668681732,
          "extra_cost": 962.7924137681549,
          "samefills_cagr_pct": 15.74303818003342,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 43,
            "win_months_all": 0.7049180327868853,
            "win_months_active": 0.7049180327868853,
            "quarters_total": 19,
            "positive_quarters": 13,
            "win_quarters": 0.6842105263157895
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 43,
            "win_months_all": 0.6825396825396826,
            "win_months_active": 0.6825396825396826,
            "quarters_total": 21,
            "positive_quarters": 15,
            "win_quarters": 0.7142857142857143
          },
          "daily_close_drawdown_pct": -8.071141615434275,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.04480591649102095
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03656273154663214,
            "2021-12-31 00:00:00+00:00": 0.19373787541001897,
            "2022-12-31 00:00:00+00:00": 0.05391011056953632,
            "2023-12-31 00:00:00+00:00": 0.1947472435387314,
            "2024-12-31 00:00:00+00:00": 0.17460311100116543,
            "2025-12-31 00:00:00+00:00": 0.17102951276864875
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10468.243254913577,
          "extra_cost": 1925.5848275363098,
          "samefills_cagr_pct": 14.727097180215987,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 41,
            "win_months_all": 0.6721311475409836,
            "win_months_active": 0.6721311475409836,
            "quarters_total": 19,
            "positive_quarters": 13,
            "win_quarters": 0.6842105263157895
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 41,
            "win_months_all": 0.6507936507936508,
            "win_months_active": 0.6507936507936508,
            "quarters_total": 21,
            "positive_quarters": 15,
            "win_quarters": 0.7142857142857143
          },
          "daily_close_drawdown_pct": -8.671180133559941,
          "worst_month": [
            "2021-08-31 00:00:00+00:00",
            -0.045888627780044655
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03450278236079263,
            "2021-12-31 00:00:00+00:00": 0.1859489854776446,
            "2022-12-31 00:00:00+00:00": 0.04785084515257143,
            "2023-12-31 00:00:00+00:00": 0.17792251529040315,
            "2024-12-31 00:00:00+00:00": 0.16561963122713141,
            "2025-12-31 00:00:00+00:00": 0.15960439956770434
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": 590.1203790376512,
        "plus10_delta_noX03": 2747.294231172541,
        "supplement": {
          "n": 57,
          "net": 2375.2878470463816,
          "fees": 324.8927258611915,
          "gross": 2700.180572907573,
          "plus10": 2014.2959294228353,
          "exbest": 1976.3008526675037,
          "ex3": 1208.3239091696046,
          "ex3_plus10": 873.2268929714779,
          "year_net": {
            "2020": -118.42346476950006,
            "2021": 637.6451248269489,
            "2022": 194.06806338999112,
            "2023": 512.834645149811,
            "2024": 334.3873183414279,
            "2025": 814.7761601077032
          }
        },
        "ex3best_plus10": 6201.47514765051,
        "exposure": {
          "time_any_position_pct": 37.72435336019151,
          "entry_notional_time_initial_equity": 0.41824682536278085,
          "two_side_turnover_initial_equity": 385.1169655072619
        },
        "path_check": {
          "counts": {
            "current": 252,
            "reference": 273,
            "retained": 218,
            "removed": 55,
            "added": 34
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 218
        }
      },
      {
        "name": "V202C",
        "url": "http://localhost:9200/#/backtest/7895cfd4-60e8-4813-86a3-31c5a4345666",
        "n": 259,
        "net": 12614.450547401677,
        "cagr": 16.94242600899716,
        "dd_engine": -7.701482653717651,
        "dd_dayclose": -7.719927369242862,
        "pf": 1.860716106282739,
        "sharpe": 1.5425914436154662,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 45,
          "win_months_all": 0.7377049180327869,
          "win_months_active": 0.7377049180327869,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.7142857142857143,
          "win_months_all": 0.7142857142857143,
          "win_quarters": 0.8571428571428571
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 11596.179269921118,
          "extra_cost": 1018.271277480559,
          "samefills_cagr_pct": 15.913575466638985,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 44,
            "win_months_all": 0.7213114754098361,
            "win_months_active": 0.7213114754098361,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 44,
            "win_months_all": 0.6984126984126984,
            "win_months_active": 0.6984126984126984,
            "quarters_total": 21,
            "positive_quarters": 18,
            "win_quarters": 0.8571428571428571
          },
          "daily_close_drawdown_pct": -8.084042116582534,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04870289143712392
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03568223345168087,
            "2021-12-31 00:00:00+00:00": 0.1714812268742032,
            "2022-12-31 00:00:00+00:00": 0.05665254742296888,
            "2023-12-31 00:00:00+00:00": 0.23965417440916958,
            "2024-12-31 00:00:00+00:00": 0.16808668002043037,
            "2025-12-31 00:00:00+00:00": 0.16334155390870397
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10577.90799244056,
          "extra_cost": 2036.542554961118,
          "samefills_cagr_pct": 14.844740763765829,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 43,
            "win_months_all": 0.7049180327868853,
            "win_months_active": 0.7049180327868853,
            "quarters_total": 19,
            "positive_quarters": 14,
            "win_quarters": 0.7368421052631579
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 43,
            "win_months_all": 0.6825396825396826,
            "win_months_active": 0.6825396825396826,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -8.693297364592,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.050605913885906184
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03362220809607619,
            "2021-12-31 00:00:00+00:00": 0.1626167557595628,
            "2022-12-31 00:00:00+00:00": 0.05036473416047005,
            "2023-12-31 00:00:00+00:00": 0.22248039203610448,
            "2024-12-31 00:00:00+00:00": 0.15861062542048154,
            "2025-12-31 00:00:00+00:00": 0.15102106153482198
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": 635.8959681697088,
        "plus10_delta_noX03": 2785.3788966795373,
        "supplement": {
          "n": 57,
          "net": 2373.2450996482276,
          "fees": 324.256575305271,
          "gross": 2697.501674953497,
          "plus10": 2012.9600159757038,
          "exbest": 1968.866389129096,
          "ex3": 1183.8597733387305,
          "ex3_plus10": 849.9607665684458,
          "year_net": {
            "2020": -118.42346476950006,
            "2021": 625.1166617001438,
            "2022": 189.53730385510462,
            "2023": 503.8368864396651,
            "2024": 338.14363919699014,
            "2025": 835.034073225823
          }
        },
        "ex3best_plus10": 6302.641489686335,
        "exposure": {
          "time_any_position_pct": 40.12910900916681,
          "entry_notional_time_initial_equity": 0.47342202103598513,
          "two_side_turnover_initial_equity": 407.3085109922234
        },
        "path_check": {
          "counts": {
            "current": 259,
            "reference": 280,
            "retained": 225,
            "removed": 55,
            "added": 34
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 225
        }
      }
    ]
  },
  {
    "id": "V203",
    "family": "validation",
    "change": "TP1.5R instead2R, other rules unchanged.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V203B",
        "url": "http://localhost:9200/#/backtest/282ac385-0a2d-4793-9a80-038232c399d9",
        "n": 276,
        "net": 11525.620848410239,
        "cagr": 15.840841973670727,
        "dd_engine": -8.213630745429445,
        "dd_dayclose": -8.272469532998484,
        "pf": 1.7253869161172548,
        "sharpe": 1.4696217038547552,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10474.25829582605,
          "extra_cost": 1051.362552584192,
          "samefills_cagr_pct": 14.733563043678188,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.639344262295082,
            "quarters_total": 19,
            "positive_quarters": 14,
            "win_quarters": 0.7368421052631579
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 15,
            "win_quarters": 0.7142857142857143
          },
          "daily_close_drawdown_pct": -8.557504215924617,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.039706408770221135
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.042522490982412675,
            "2021-12-31 00:00:00+00:00": 0.21000165817319583,
            "2022-12-31 00:00:00+00:00": 0.08703116328684257,
            "2023-12-31 00:00:00+00:00": 0.1474213493934522,
            "2024-12-31 00:00:00+00:00": 0.12656762268950894,
            "2025-12-31 00:00:00+00:00": 0.15508672530357237
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 9422.89574324186,
          "extra_cost": 2102.725105168384,
          "samefills_cagr_pct": 13.579334086619488,
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
          "daily_close_drawdown_pct": -9.292713422789378,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04094551956948067
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.040651147564516155,
            "2021-12-31 00:00:00+00:00": 0.20151524917153418,
            "2022-12-31 00:00:00+00:00": 0.0796255422455292,
            "2023-12-31 00:00:00+00:00": 0.12949476646154245,
            "2024-12-31 00:00:00+00:00": 0.11623697650377718,
            "2025-12-31 00:00:00+00:00": 0.1412104659877016
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -455.22713263406513,
        "plus10_delta_noX03": 1701.9467195008247,
        "supplement": {
          "n": 79,
          "net": 1520.844590929222,
          "fees": 467.274818083944,
          "gross": 1988.1194090131662,
          "plus10": 1001.650348613728,
          "exbest": 1238.9558628422678,
          "ex3": 725.5050347703158,
          "ex3_plus10": 234.01469791928537,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 730.175311301,
            "2022": 693.0837492868052,
            "2023": -88.14550065909773,
            "2024": -252.59050352355464,
            "2025": 503.4205888760687
          }
        },
        "ex3best_plus10": 5126.528719573868,
        "exposure": {
          "time_any_position_pct": 38.316328020085244,
          "entry_notional_time_initial_equity": 0.4198854764847497,
          "two_side_turnover_initial_equity": 420.54502103367673
        },
        "path_check": {
          "counts": {
            "current": 276,
            "reference": 273,
            "retained": 272,
            "removed": 1,
            "added": 4
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 252
        }
      },
      {
        "name": "V203C",
        "url": "http://localhost:9200/#/backtest/e039907b-67a5-4531-8ffe-14842cc4fd01",
        "n": 283,
        "net": 11733.79935857649,
        "cagr": 16.05488705737621,
        "dd_engine": -9.03097656487648,
        "dd_dayclose": -9.089590048383577,
        "pf": 1.7133864649196842,
        "sharpe": 1.4615197124176413,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 17,
          "win_quarters": 0.8947368421052632
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.8571428571428571
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10627.436839432916,
          "extra_cost": 1106.362519143577,
          "samefills_cagr_pct": 14.897707130933657,
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
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 38,
            "win_months_all": 0.6031746031746031,
            "win_months_active": 0.6031746031746031,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -9.371999100367113,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04882447697538306
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.041636009968650134,
            "2021-12-31 00:00:00+00:00": 0.18802915822911226,
            "2022-12-31 00:00:00+00:00": 0.09015884641262462,
            "2023-12-31 00:00:00+00:00": 0.19001554684634114,
            "2024-12-31 00:00:00+00:00": 0.120540745108068,
            "2025-12-31 00:00:00+00:00": 0.14665325790479522
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 9521.074320289339,
          "extra_cost": 2212.725038287154,
          "samefills_cagr_pct": 13.689227290672346,
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
          "daily_close_drawdown_pct": -9.65614902698726,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.0507243058722473
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03976460713127339,
            "2021-12-31 00:00:00+00:00": 0.1784825741479219,
            "2022-12-31 00:00:00+00:00": 0.08255276020086111,
            "2023-12-31 00:00:00+00:00": 0.17174831971205506,
            "2024-12-31 00:00:00+00:00": 0.1096700908715944,
            "2025-12-31 00:00:00+00:00": 0.1317961905214622
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -420.93770398151537,
        "plus10_delta_noX03": 1728.5452245283132,
        "supplement": {
          "n": 79,
          "net": 1495.853538512425,
          "fees": 466.1016987792188,
          "gross": 1961.9552372916442,
          "plus10": 977.9627620910716,
          "exbest": 1210.1555032891615,
          "ex3": 690.511993494692,
          "ex3_plus10": 200.65248662953167,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 715.3672619345468,
            "2022": 682.0111116280749,
            "2023": -86.04663548170402,
            "2024": -259.8546881713644,
            "2025": 509.475542954872
          }
        },
        "ex3best_plus10": 5216.15900621619,
        "exposure": {
          "time_any_position_pct": 40.65430314707771,
          "entry_notional_time_initial_equity": 0.474464532665764,
          "two_side_turnover_initial_equity": 442.5450076574305
        },
        "path_check": {
          "counts": {
            "current": 283,
            "reference": 280,
            "retained": 279,
            "removed": 1,
            "added": 4
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 259
        }
      }
    ]
  },
  {
    "id": "V204",
    "family": "validation",
    "change": "TP2.5R instead2R.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V204B",
        "url": "http://localhost:9200/#/backtest/ef335fc4-a08a-47b5-ba2f-d29e5b9159fa",
        "n": 272,
        "net": 12701.158448965434,
        "cagr": 17.028293139842088,
        "dd_engine": -8.240289584499838,
        "dd_dayclose": -8.299597504768187,
        "pf": 1.7928850605724411,
        "sharpe": 1.5348307140516815,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 11644.520630934549,
          "extra_cost": 1056.6378180308895,
          "samefills_cagr_pct": 15.96329623616759,
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
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -8.550557193647768,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.039769025129154034
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.042522490982412675,
            "2021-12-31 00:00:00+00:00": 0.1968665784615975,
            "2022-12-31 00:00:00+00:00": 0.08966120654780352,
            "2023-12-31 00:00:00+00:00": 0.1778225235955695,
            "2024-12-31 00:00:00+00:00": 0.1421564118769636,
            "2025-12-31 00:00:00+00:00": 0.18336813842724742
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10587.88281290366,
          "extra_cost": 2113.275636061779,
          "samefills_cagr_pct": 14.855416159939793,
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
          "daily_close_drawdown_pct": -9.276297145590483,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04100591724844738
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04065114756451593,
            "2021-12-31 00:00:00+00:00": 0.18864045980623634,
            "2022-12-31 00:00:00+00:00": 0.08261580150216408,
            "2023-12-31 00:00:00+00:00": 0.1601230881311746,
            "2024-12-31 00:00:00+00:00": 0.1322757580815277,
            "2025-12-31 00:00:00+00:00": 0.17037589980233614
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2023-08-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": 709.7599370277294,
        "plus10_delta_noX03": 2866.933789162619,
        "supplement": {
          "n": 79,
          "net": 2856.213836928551,
          "fees": 473.1845391557621,
          "gross": 3329.3983760843125,
          "plus10": 2330.4532378665936,
          "exbest": 2434.9299643514023,
          "ex3": 1594.9982591251846,
          "ex3_plus10": 1103.5103823492996,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 496.7236753318218,
            "2022": 854.9427569159569,
            "2023": 330.6200239470204,
            "2024": 67.91395856543488,
            "2025": 1171.112476520317
          }
        },
        "ex3best_plus10": 6234.908578825694,
        "exposure": {
          "time_any_position_pct": 38.740147136100894,
          "entry_notional_time_initial_equity": 0.43130746490264876,
          "two_side_turnover_initial_equity": 422.6551272123556
        },
        "path_check": {
          "counts": {
            "current": 272,
            "reference": 273,
            "retained": 272,
            "removed": 1,
            "added": 0
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 257
        }
      },
      {
        "name": "V204C",
        "url": "http://localhost:9200/#/backtest/798a0f06-6005-4bea-bebc-dc22a89093dd",
        "n": 279,
        "net": 12906.321800193173,
        "cagr": 17.230416425872352,
        "dd_engine": -8.99776600090566,
        "dd_dayclose": -9.056476125534452,
        "pf": 1.7784918788213508,
        "sharpe": 1.5243421444414555,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 41,
          "win_months_all": 0.6721311475409836,
          "win_months_active": 0.6721311475409836,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6507936507936508,
          "win_months_all": 0.6507936507936508,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 11794.125068710755,
          "extra_cost": 1112.1967314824271,
          "samefills_cagr_pct": 16.116603049770074,
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
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -9.338205807368327,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.0487242763359943
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04163600996864991,
            "2021-12-31 00:00:00+00:00": 0.1740775028272432,
            "2022-12-31 00:00:00+00:00": 0.0926494219208287,
            "2023-12-31 00:00:00+00:00": 0.22113486357893763,
            "2024-12-31 00:00:00+00:00": 0.13635516860389862,
            "2025-12-31 00:00:00+00:00": 0.17535247080191363
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10681.928337228328,
          "extra_cost": 2224.3934629648543,
          "samefills_cagr_pct": 14.955861961527471,
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
          "daily_close_drawdown_pct": -9.621659883360268,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.05062281319222961
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.039764607131273166,
            "2021-12-31 00:00:00+00:00": 0.16478505555413525,
            "2022-12-31 00:00:00+00:00": 0.08541419274635276,
            "2023-12-31 00:00:00+00:00": 0.20311690234415147,
            "2024-12-31 00:00:00+00:00": 0.125958282823456,
            "2025-12-31 00:00:00+00:00": 0.1614073884637952
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2020-11-30 00:00:00+00:00",
            "2023-08-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": 739.9163129574717,
        "plus10_delta_noX03": 2889.3992414673003,
        "supplement": {
          "n": 79,
          "net": 2850.8857361930754,
          "fees": 471.89784103324814,
          "gross": 3322.783577226324,
          "plus10": 2326.554801711689,
          "exbest": 2423.314044622243,
          "ex3": 1569.8745546712344,
          "ex3_plus10": 1080.3623940508483,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 491.33499769750006,
            "2022": 840.1416718447792,
            "2023": 323.7485619344547,
            "2024": 69.18650080622535,
            "2025": 1191.573058262117
          }
        },
        "ex3best_plus10": 6324.379022386658,
        "exposure": {
          "time_any_position_pct": 41.058671979914756,
          "entry_notional_time_initial_equity": 0.4864830588893267,
          "two_side_turnover_initial_equity": 444.87869259297065
        },
        "path_check": {
          "counts": {
            "current": 279,
            "reference": 280,
            "retained": 279,
            "removed": 1,
            "added": 0
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 264
        }
      }
    ]
  },
  {
    "id": "V205",
    "family": "validation",
    "change": "Supplement timeout24h instead48h.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V205B",
        "url": "http://localhost:9200/#/backtest/e6e91629-fb28-4a05-ac74-2329ee932bfe",
        "n": 278,
        "net": 9992.66891206305,
        "cagr": 14.210949403037754,
        "dd_engine": -8.696777717518078,
        "dd_dayclose": -8.686926182896881,
        "pf": 1.6765138145381184,
        "sharpe": 1.3444871570140557,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 36,
          "win_months_all": 0.5901639344262295,
          "win_months_active": 0.5901639344262295,
          "quarters_total": 19,
          "positive_quarters": 15,
          "win_quarters": 0.7894736842105263
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.5714285714285714,
          "win_months_all": 0.5714285714285714,
          "win_quarters": 0.7619047619047619
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 8992.286542881908,
          "extra_cost": 1000.3823691811406,
          "samefills_cagr_pct": 13.091975572204873,
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
          "daily_close_drawdown_pct": -9.35014469951968,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03987324531473979
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04747562191822885,
            "2021-12-31 00:00:00+00:00": 0.17729847326438275,
            "2022-12-31 00:00:00+00:00": 0.06053046444427146,
            "2023-12-31 00:00:00+00:00": 0.11884902214286908,
            "2024-12-31 00:00:00+00:00": 0.11581566454062231,
            "2025-12-31 00:00:00+00:00": 0.16321410497892042
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 7991.904173700768,
          "extra_cost": 2000.7647383622812,
          "samefills_cagr_pct": 11.924305953933146,
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
          "daily_close_drawdown_pct": -10.559415689137264,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04111406169622622
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04560053741836301,
            "2021-12-31 00:00:00+00:00": 0.16864756415593218,
            "2022-12-31 00:00:00+00:00": 0.05334350431227075,
            "2023-12-31 00:00:00+00:00": 0.10021672914573698,
            "2024-12-31 00:00:00+00:00": 0.1049293139425247,
            "2025-12-31 00:00:00+00:00": 0.1498601206287722
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "plus10_delta_X03": -1886.2187021751643,
        "plus10_delta_noX03": 270.95514995972553,
        "supplement": {
          "n": 80,
          "net": 819.680277060634,
          "fees": 452.27360336380895,
          "gross": 1271.9538804244426,
          "plus10": 317.15405110084583,
          "exbest": 519.5835321628874,
          "ex3": -76.67812798914713,
          "ex3_plus10": -548.4671763813675,
          "year_net": {
            "2020": -16.75763049599996,
            "2021": 515.5100250297684,
            "2022": 490.21363349493436,
            "2023": -451.95064414875765,
            "2024": -308.0257961445703,
            "2025": 590.6906893252586
          }
        },
        "ex3best_plus10": 3949.554974772672,
        "exposure": {
          "time_any_position_pct": 36.97692240322298,
          "entry_notional_time_initial_equity": 0.38786462028934776,
          "two_side_turnover_initial_equity": 400.15294767245604
        },
        "path_check": {
          "counts": {
            "current": 278,
            "reference": 273,
            "retained": 273,
            "removed": 0,
            "added": 5
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 223
        }
      },
      {
        "name": "V205C",
        "url": "http://localhost:9200/#/backtest/608630f0-127d-4330-9a43-34f94b25ac72",
        "n": 285,
        "net": 10184.26004228165,
        "cagr": 14.420067229807266,
        "dd_engine": -8.989091027797668,
        "dd_dayclose": -9.047995777768602,
        "pf": 1.6660662692493984,
        "sharpe": 1.3400725749813454,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 37,
          "win_months_all": 0.6065573770491803,
          "win_months_active": 0.6065573770491803,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.5873015873015873,
          "win_months_all": 0.5873015873015873,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 9132.484119378432,
          "extra_cost": 1051.7759229032085,
          "samefills_cagr_pct": 13.25162135158271,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 37,
            "win_months_all": 0.6065573770491803,
            "win_months_active": 0.6065573770491803,
            "quarters_total": 19,
            "positive_quarters": 16,
            "win_quarters": 0.8421052631578947
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 37,
            "win_months_all": 0.5873015873015873,
            "win_months_active": 0.5873015873015873,
            "quarters_total": 21,
            "positive_quarters": 17,
            "win_quarters": 0.8095238095238095
          },
          "daily_close_drawdown_pct": -9.346306462291388,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.048514988040146756
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04658914090446631,
            "2021-12-31 00:00:00+00:00": 0.15494230253891983,
            "2022-12-31 00:00:00+00:00": 0.06332016207546487,
            "2023-12-31 00:00:00+00:00": 0.16100377947078548,
            "2024-12-31 00:00:00+00:00": 0.11022778155277457,
            "2025-12-31 00:00:00+00:00": 0.15484866211246362
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 8080.708196475224,
          "extra_cost": 2103.551845806417,
          "samefills_cagr_pct": 12.030053302303777,
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
          "daily_close_drawdown_pct": -10.116790265026465,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.05041146564171517
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04471399698512024,
            "2021-12-31 00:00:00+00:00": 0.14525222728925735,
            "2022-12-31 00:00:00+00:00": 0.05590642007788005,
            "2023-12-31 00:00:00+00:00": 0.14203328658301406,
            "2024-12-31 00:00:00+00:00": 0.09880358996247018,
            "2025-12-31 00:00:00+00:00": 0.1404929794819738
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "plus10_delta_X03": -1861.3038277956312,
        "plus10_delta_noX03": 288.1791007141974,
        "supplement": {
          "n": 80,
          "net": 812.8603063060564,
          "fees": 450.371363638525,
          "gross": 1263.2316699445814,
          "plus10": 312.4476800410284,
          "exbest": 507.761948993349,
          "ex3": -94.82356220674276,
          "ex3_plus10": -564.1309329710023,
          "year_net": {
            "2020": -16.75763049599996,
            "2021": 503.65443277455813,
            "2022": 482.87477418345077,
            "2023": -443.01971205587154,
            "2024": -313.67449379403007,
            "2025": 599.7829356939487
          }
        },
        "ex3best_plus10": 4034.6487619593677,
        "exposure": {
          "time_any_position_pct": 39.32037134349273,
          "entry_notional_time_initial_equity": 0.4390492340485712,
          "two_side_turnover_initial_equity": 420.7103691612832
        },
        "path_check": {
          "counts": {
            "current": 285,
            "reference": 280,
            "retained": 280,
            "removed": 0,
            "added": 5
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 230
        }
      }
    ]
  },
  {
    "id": "V206",
    "family": "validation",
    "change": "Supplement timeout72h instead48h.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V206B",
        "url": "http://localhost:9200/#/backtest/046eb445-5e0a-413f-aec9-2498a6a3cb38",
        "n": 267,
        "net": 11516.32016410076,
        "cagr": 15.831240213808485,
        "dd_engine": -8.215762925591497,
        "dd_dayclose": -8.274712644030124,
        "pf": 1.7213389857272847,
        "sharpe": 1.4460389243473863,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 39,
          "win_months_all": 0.639344262295082,
          "win_months_active": 0.639344262295082,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6190476190476191,
          "win_months_all": 0.6190476190476191,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10509.55025148672,
          "extra_cost": 1006.7699126140398,
          "samefills_cagr_pct": 14.771469204684617,
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
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -8.589300468534233,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03965948517746909
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03922648074416646,
            "2021-12-31 00:00:00+00:00": 0.19498654413903083,
            "2022-12-31 00:00:00+00:00": 0.06713206250972248,
            "2023-12-31 00:00:00+00:00": 0.16552169758443025,
            "2024-12-31 00:00:00+00:00": 0.12745614916873893,
            "2025-12-31 00:00:00+00:00": 0.17772725657829946
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 9502.78033887268,
          "extra_cost": 2013.5398252280795,
          "samefills_cagr_pct": 13.668784393813716,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 36,
            "win_months_all": 0.5901639344262295,
            "win_months_active": 0.5901639344262295,
            "quarters_total": 19,
            "positive_quarters": 13,
            "win_quarters": 0.6842105263157895
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 36,
            "win_months_all": 0.5714285714285714,
            "win_months_active": 0.5714285714285714,
            "quarters_total": 21,
            "positive_quarters": 14,
            "win_quarters": 0.6666666666666666
          },
          "daily_close_drawdown_pct": -9.311256367786026,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04089762344813652
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.037357696115467576,
            "2021-12-31 00:00:00+00:00": 0.1869270482165062,
            "2022-12-31 00:00:00+00:00": 0.06055677804434523,
            "2023-12-31 00:00:00+00:00": 0.14821671866170427,
            "2024-12-31 00:00:00+00:00": 0.11712144381708578,
            "2025-12-31 00:00:00+00:00": 0.1643560139528517
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2022-01-31 00:00:00+00:00",
            "2023-03-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -375.342537003251,
        "plus10_delta_noX03": 1781.8313151316388,
        "supplement": {
          "n": 78,
          "net": 1888.9588485405518,
          "fees": 450.8900603509987,
          "gross": 2339.8489088915503,
          "plus10": 1387.9698925949979,
          "exbest": 1515.904997123032,
          "ex3": 833.5076332604523,
          "ex3_plus10": 359.7602226118762,
          "year_net": {
            "2020": -93.97537551153718,
            "2021": 364.22234914491287,
            "2022": 758.9185837989405,
            "2023": 124.09178036044796,
            "2024": -143.90521437264192,
            "2025": 879.6067251204297
          }
        },
        "ex3best_plus10": 5314.831931498683,
        "exposure": {
          "time_any_position_pct": 39.523376831902844,
          "entry_notional_time_initial_equity": 0.42083210462297327,
          "two_side_turnover_initial_equity": 402.7079650456159
        },
        "path_check": {
          "counts": {
            "current": 267,
            "reference": 273,
            "retained": 267,
            "removed": 6,
            "added": 0
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 230
        }
      },
      {
        "name": "V206C",
        "url": "http://localhost:9200/#/backtest/79037f88-5dcd-4c0e-814f-38ad77b5e6af",
        "n": 274,
        "net": 11692.917987921257,
        "cagr": 16.012984776315587,
        "dd_engine": -9.036230298563074,
        "dd_dayclose": -9.09495078954995,
        "pf": 1.708267240547789,
        "sharpe": 1.4357447164593675,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 16,
          "win_quarters": 0.8421052631578947
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.8095238095238095
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 10632.495192483471,
          "extra_cost": 1060.4227954377864,
          "samefills_cagr_pct": 14.903110769318229,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 40,
            "win_months_all": 0.6557377049180327,
            "win_months_active": 0.6557377049180327,
            "quarters_total": 19,
            "positive_quarters": 15,
            "win_quarters": 0.7894736842105263
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 40,
            "win_months_all": 0.6349206349206349,
            "win_months_active": 0.6349206349206349,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -9.37693621983804,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.048747376697453104
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03833994051037393,
            "2021-12-31 00:00:00+00:00": 0.1724308527270999,
            "2022-12-31 00:00:00+00:00": 0.0695279259763526,
            "2023-12-31 00:00:00+00:00": 0.20850331964683133,
            "2024-12-31 00:00:00+00:00": 0.12168325643141054,
            "2025-12-31 00:00:00+00:00": 0.16900061804373867
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 9572.072397045684,
          "extra_cost": 2120.8455908755727,
          "samefills_cagr_pct": 13.746134261919574,
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
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 38,
            "win_months_all": 0.6031746031746031,
            "win_months_active": 0.6031746031746031,
            "quarters_total": 21,
            "positive_quarters": 16,
            "win_quarters": 0.7619047619047619
          },
          "daily_close_drawdown_pct": -9.66066188152629,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.05064569325094992
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.03647110127647002,
            "2021-12-31 00:00:00+00:00": 0.1633016510456462,
            "2022-12-31 00:00:00+00:00": 0.06273450030061745,
            "2023-12-31 00:00:00+00:00": 0.19085019980950713,
            "2024-12-31 00:00:00+00:00": 0.11083118168071437,
            "2025-12-31 00:00:00+00:00": 0.15466844040262306
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2022-01-31 00:00:00+00:00",
            "2023-03-31 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -369.93962722516517,
        "plus10_delta_noX03": 1779.5433012846634,
        "supplement": {
          "n": 78,
          "net": 1881.4468096738856,
          "fees": 449.48991606041966,
          "gross": 2330.936725734306,
          "plus10": 1382.0135696067528,
          "exbest": 1503.2826315246189,
          "ex3": 809.2360558102889,
          "ex3_plus10": 337.49191936959056,
          "year_net": {
            "2020": -93.97537551153718,
            "2021": 363.2817809890612,
            "2022": 743.5464052900188,
            "2023": 122.94184703965021,
            "2024": -147.00334049641185,
            "2025": 892.6554923631048
          }
        },
        "ex3best_plus10": 5380.596702101911,
        "exposure": {
          "time_any_position_pct": 41.85514830384773,
          "entry_notional_time_initial_equity": 0.4739533951418933,
          "two_side_turnover_initial_equity": 424.1691181751146
        },
        "path_check": {
          "counts": {
            "current": 274,
            "reference": 280,
            "retained": 274,
            "removed": 6,
            "added": 0
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 31,
            "same_exit": 31
          },
          "same_exit_retained": 237
        }
      }
    ]
  },
  {
    "id": "V207",
    "family": "validation",
    "change": "Strong timing stress: consume source setup t once, schedule exactly next4h close; original plans priority, expire if occupied/pending/overridden/missingclock, no queue. No revalidation; freeze original distance/TP geometry at signal, place MARKET at due close with current budget and original helpers; protection relative actualfill;48h fromfill. New original events update state independently.",
    "eligibility": null,
    "portfolios": [
      {
        "name": "V207B",
        "url": "http://localhost:9200/#/backtest/37a6818d-37d3-4ffc-b821-f6ed69a1e459",
        "n": 272,
        "net": 8453.326511477679,
        "cagr": 12.469240955610793,
        "dd_engine": -9.107769510949959,
        "dd_dayclose": -9.097961598960957,
        "pf": 1.6142235952298414,
        "sharpe": 1.1967129796142293,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.7142857142857143
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 7561.648003368154,
          "extra_cost": 891.6785081095284,
          "samefills_cagr_pct": 11.405904652482924,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 39,
            "win_months_all": 0.639344262295082,
            "win_months_active": 0.639344262295082,
            "quarters_total": 19,
            "positive_quarters": 14,
            "win_quarters": 0.7368421052631579
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 39,
            "win_months_all": 0.6190476190476191,
            "win_months_active": 0.6190476190476191,
            "quarters_total": 21,
            "positive_quarters": 15,
            "win_quarters": 0.7142857142857143
          },
          "daily_close_drawdown_pct": -9.826179230751608,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.03989439620162305
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.044470317684969896,
            "2021-12-31 00:00:00+00:00": 0.07127967128610146,
            "2022-12-31 00:00:00+00:00": 0.032290336663925556,
            "2023-12-31 00:00:00+00:00": 0.13788641310215022,
            "2024-12-31 00:00:00+00:00": 0.13553133925768646,
            "2025-12-31 00:00:00+00:00": 0.17670176124755277
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2022-08-31 00:00:00+00:00"
          ]
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 6669.969495258625,
          "extra_cost": 1783.3570162190567,
          "samefills_cagr_pct": 10.297998604562085,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 34,
            "win_months_all": 0.5573770491803278,
            "win_months_active": 0.5573770491803278,
            "quarters_total": 19,
            "positive_quarters": 11,
            "win_quarters": 0.5789473684210527
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 34,
            "win_months_all": 0.5396825396825397,
            "win_months_active": 0.5396825396825397,
            "quarters_total": 21,
            "positive_quarters": 12,
            "win_quarters": 0.5714285714285714
          },
          "daily_close_drawdown_pct": -10.60188722397941,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.04114051433641186
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.04259502900178491,
            "2021-12-31 00:00:00+00:00": 0.06370825983959061,
            "2022-12-31 00:00:00+00:00": 0.02490661454569687,
            "2023-12-31 00:00:00+00:00": 0.11950643071620948,
            "2024-12-31 00:00:00+00:00": 0.12552585863800125,
            "2025-12-31 00:00:00+00:00": 0.16393910030139036
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2022-08-31 00:00:00+00:00",
            "2023-03-31 00:00:00+00:00",
            "2023-11-30 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-08-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -3208.15338061731,
        "plus10_delta_noX03": -1050.9795284824204,
        "supplement": {
          "n": 76,
          "net": 572.6372624924381,
          "fees": 385.37015839160205,
          "gross": 958.0074208840401,
          "plus10": 144.44819761288016,
          "exbest": 263.58834605176446,
          "ex3": -282.27053158106327,
          "ex3_plus10": -682.379193439019,
          "year_net": {
            "2020": -45.05361494400006,
            "2021": 237.8064800751803,
            "2022": 130.27728834227096,
            "2023": -190.37010029126827,
            "2024": -284.00153633905745,
            "2025": 723.9787456493127
          }
        },
        "ex3best_plus10": 3040.1310740089266,
        "exposure": {
          "time_any_position_pct": 37.892691364512174,
          "entry_notional_time_initial_equity": 0.3624718580714214,
          "two_side_turnover_initial_equity": 356.6714032438113
        },
        "path_check": {
          "counts": {
            "current": 272,
            "reference": 273,
            "retained": 192,
            "removed": 81,
            "added": 80
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 30,
            "same_exit": 30
          },
          "same_exit_retained": 192
        }
      },
      {
        "name": "V207C",
        "url": "http://localhost:9200/#/backtest/cfda043d-15dc-4443-9655-fbabf6fae45b",
        "n": 279,
        "net": 8588.878495063746,
        "cagr": 12.627232440395009,
        "dd_engine": -9.303970041493237,
        "dd_dayclose": -9.31182948009589,
        "pf": 1.6038888442562014,
        "sharpe": 1.1899904103557868,
        "full_nominal": {
          "months_total": 61,
          "months_active": 61,
          "positive_months": 40,
          "win_months_all": 0.6557377049180327,
          "win_months_active": 0.6557377049180327,
          "quarters_total": 19,
          "positive_quarters": 14,
          "win_quarters": 0.7368421052631579
        },
        "partial_nominal": {
          "months_total": 63,
          "months_active": 63,
          "win_months_active": 0.6349206349206349,
          "win_months_all": 0.6349206349206349,
          "win_quarters": 0.7142857142857143
        },
        "cost5": {
          "extra_bps_RT": 5,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 7651.598578732392,
          "extra_cost": 937.2799163313446,
          "samefills_cagr_pct": 11.51512508809076,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 40,
            "win_months_all": 0.6557377049180327,
            "win_months_active": 0.6557377049180327,
            "quarters_total": 19,
            "positive_quarters": 13,
            "win_quarters": 0.6842105263157895
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 40,
            "win_months_all": 0.6349206349206349,
            "win_months_active": 0.6349206349206349,
            "quarters_total": 21,
            "positive_quarters": 14,
            "win_quarters": 0.6666666666666666
          },
          "daily_close_drawdown_pct": -9.794702032430258,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.048655026853423045
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.043556305434177656,
            "2021-12-31 00:00:00+00:00": 0.0493515637570785,
            "2022-12-31 00:00:00+00:00": 0.035132412663313684,
            "2023-12-31 00:00:00+00:00": 0.17979288825841944,
            "2024-12-31 00:00:00+00:00": 0.12953332297004017,
            "2025-12-31 00:00:00+00:00": 0.16854761254748185
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": []
        },
        "cost10": {
          "extra_bps_RT": 10,
          "engine_fee_basis_per_side": 0.00045,
          "samefills_net": 6714.318662401047,
          "extra_cost": 1874.5598326626891,
          "samefills_cagr_pct": 10.354220563020666,
          "complete_periods": {
            "months_total": 61,
            "months_active": 61,
            "positive_months": 35,
            "win_months_all": 0.5737704918032787,
            "win_months_active": 0.5737704918032787,
            "quarters_total": 19,
            "positive_quarters": 11,
            "win_quarters": 0.5789473684210527
          },
          "partial_periods": {
            "months_total": 63,
            "months_active": 63,
            "positive_months": 35,
            "win_months_all": 0.5555555555555556,
            "win_months_active": 0.5555555555555556,
            "quarters_total": 21,
            "positive_quarters": 12,
            "win_quarters": 0.5714285714285714
          },
          "daily_close_drawdown_pct": -10.600510707298849,
          "worst_month": [
            "2021-04-30 00:00:00+00:00",
            -0.05056520418627153
          ],
          "yearly_returns": {
            "2020-12-31 00:00:00+00:00": 0.041681678568287195,
            "2021-12-31 00:00:00+00:00": 0.04077536087997968,
            "2022-12-31 00:00:00+00:00": 0.02749092668746944,
            "2023-12-31 00:00:00+00:00": 0.16109800979487354,
            "2024-12-31 00:00:00+00:00": 0.11899847981580347,
            "2025-12-31 00:00:00+00:00": 0.15483590260180335
          },
          "nearzero_months": {},
          "positive_to_nonpositive_months": [
            "2022-08-31 00:00:00+00:00",
            "2023-03-31 00:00:00+00:00",
            "2025-07-31 00:00:00+00:00",
            "2025-08-31 00:00:00+00:00",
            "2025-09-30 00:00:00+00:00"
          ]
        },
        "plus10_delta_X03": -3227.6933618698095,
        "plus10_delta_noX03": -1078.210433359981,
        "supplement": {
          "n": 76,
          "net": 584.6247148897473,
          "fees": 383.02105129821535,
          "gross": 967.6457661879627,
          "plus10": 159.04576900284107,
          "exbest": 268.92958519228483,
          "ex3": -283.77010657002086,
          "ex3_plus10": -680.8276988767677,
          "year_net": {
            "2020": -45.05361494400006,
            "2021": 234.11548835923736,
            "2022": 127.67175833753765,
            "2023": -181.85878707439102,
            "2024": -288.9357055987282,
            "2025": 738.6855758100916
          }
        },
        "ex3best_plus10": 3081.2707065438585,
        "exposure": {
          "time_any_position_pct": 40.2543133648625,
          "entry_notional_time_initial_equity": 0.4077925498045885,
          "two_side_turnover_initial_equity": 374.9119665325381
        },
        "path_check": {
          "counts": {
            "current": 279,
            "reference": 280,
            "retained": 199,
            "removed": 81,
            "added": 80
          },
          "btc_long": {
            "reference": 31,
            "retained_entry": 30,
            "same_exit": 30
          },
          "same_exit_retained": 199
        }
      }
    ]
  }
]
```