# R11 N204B — datos completos

Snapshots completos de siete políticas. Neto de trades reconciliado con motor a tolerancia0.01 USDT; identidad de entradas única, comparación de entradas y salidas vsL5. Curvas diarias, extremos parciales marcados. B/C no son muestras independientes.

## Métricas, anuales y atribución

```json
{
  "rows": [
    {
      "case": "L1",
      "leverage": 1,
      "net": 12152.567203304845,
      "return_pct": 121.52567203304847,
      "cagr_pct": 16.480484978730516,
      "dd_engine_pct": -8.204094216098524,
      "dd_curve_pct": -8.20409421609849,
      "calmar": 2.0088122521059795,
      "sharpe": 1.637362521623694,
      "sortino": 2.974009553428036,
      "pf": 1.8879776083483994,
      "trades": 273,
      "fees": 1583.9769659425506,
      "underwater_days_engine": 291,
      "curve_terminal": 22152.56720330482,
      "wallet_terminal_engine": 22152.56720330482,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 12152.567203304821,
      "positive_full_months": 44,
      "complete_months": 61,
      "best_observed_month_delta": 1897.4029225346458,
      "worst_observed_month_delta": -690.2121014958502,
      "observed_net_ex_best_month": 10255.164280770176
    },
    {
      "case": "L2",
      "leverage": 2,
      "net": 12855.34847867253,
      "return_pct": 128.5534847867253,
      "cagr_pct": 17.180335443021754,
      "dd_engine_pct": -8.797978610941692,
      "dd_curve_pct": -8.797978610941737,
      "calmar": 1.9527594010805234,
      "sharpe": 1.57536803748525,
      "sortino": 2.77555595592524,
      "pf": 1.81247334860289,
      "trades": 273,
      "fees": 1891.7889678344018,
      "underwater_days_engine": 292,
      "curve_terminal": 22855.348478672557,
      "wallet_terminal_engine": 22855.348478672557,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 12855.348478672557,
      "positive_full_months": 44,
      "complete_months": 61,
      "best_observed_month_delta": 2049.6150495183538,
      "worst_observed_month_delta": -724.5045051702255,
      "observed_net_ex_best_month": 10805.733429154203
    },
    {
      "case": "L3",
      "leverage": 3,
      "net": 13055.772851184418,
      "return_pct": 130.55772851184415,
      "cagr_pct": 17.376733819165977,
      "dd_engine_pct": -8.776453495338233,
      "dd_curve_pct": -8.776453495338254,
      "calmar": 1.9799266102641502,
      "sharpe": 1.5821467962088316,
      "sortino": 2.7910885331528346,
      "pf": 1.8215766518700032,
      "trades": 273,
      "fees": 1913.0334906225373,
      "underwater_days_engine": 291,
      "curve_terminal": 23055.772851184454,
      "wallet_terminal_engine": 23055.772851184454,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13055.772851184454,
      "positive_full_months": 44,
      "complete_months": 61,
      "best_observed_month_delta": 2069.271896714974,
      "worst_observed_month_delta": -731.8206401519856,
      "observed_net_ex_best_month": 10986.50095446948
    },
    {
      "case": "L4",
      "leverage": 4,
      "net": 13057.53457073037,
      "return_pct": 130.57534570730368,
      "cagr_pct": 17.378454022460367,
      "dd_engine_pct": -8.776453495338233,
      "dd_curve_pct": -8.776453495338266,
      "calmar": 1.9801226123617288,
      "sharpe": 1.5824888024946342,
      "sortino": 2.7920682342072305,
      "pf": 1.821768595977286,
      "trades": 273,
      "fees": 1912.9633090873922,
      "underwater_days_engine": 291,
      "curve_terminal": 23057.534570730397,
      "wallet_terminal_engine": 23057.534570730397,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13057.534570730397,
      "positive_full_months": 44,
      "complete_months": 61,
      "best_observed_month_delta": 2069.271896714974,
      "worst_observed_month_delta": -731.8577129707701,
      "observed_net_ex_best_month": 10988.262674015423
    },
    {
      "case": "L5",
      "leverage": 5,
      "net": 13056.614915077666,
      "return_pct": 130.56614915077665,
      "cagr_pct": 17.37755605244038,
      "dd_engine_pct": -8.77680090479469,
      "dd_curve_pct": -8.77680090479468,
      "calmar": 1.9799419219988426,
      "sharpe": 1.582686191771496,
      "sortino": 2.7923923242824853,
      "pf": 1.8217438748916532,
      "trades": 273,
      "fees": 1912.8646543786201,
      "underwater_days_engine": 291,
      "curve_terminal": 23056.614915077673,
      "wallet_terminal_engine": 23056.614915077673,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13056.614915077673,
      "positive_full_months": 44,
      "complete_months": 61,
      "best_observed_month_delta": 2069.267532240141,
      "worst_observed_month_delta": -731.8403737437438,
      "observed_net_ex_best_month": 10987.347382837532
    },
    {
      "case": "M5A15",
      "leverage": 5,
      "net": 6334.294185542128,
      "return_pct": 63.34294185542129,
      "cagr_pct": 9.868492765557434,
      "dd_engine_pct": -6.3144093425155585,
      "dd_curve_pct": -6.3144093425155585,
      "calmar": 1.5628528703566733,
      "sharpe": 1.4456546426941657,
      "sortino": 2.58503649888263,
      "pf": 1.751047436436302,
      "trades": 273,
      "fees": 800.3595318888031,
      "underwater_days_engine": 220,
      "curve_terminal": 16334.294185542125,
      "wallet_terminal_engine": 16334.294185542125,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 6334.294185542125,
      "positive_full_months": 43,
      "complete_months": 61,
      "best_observed_month_delta": 1033.0517126820305,
      "worst_observed_month_delta": -408.38559296510357,
      "observed_net_ex_best_month": 5301.2424728600945
    },
    {
      "case": "R5A15",
      "leverage": 5,
      "net": 43489.00658420746,
      "return_pct": 434.8900658420746,
      "cagr_pct": 37.937673778662905,
      "dd_engine_pct": -17.037682176632153,
      "dd_curve_pct": -17.037682176632163,
      "calmar": 2.2266921864932963,
      "sharpe": 1.5931711100797203,
      "sortino": 2.7621801134430224,
      "pf": 1.898571157107632,
      "trades": 273,
      "fees": 5775.058644051861,
      "underwater_days_engine": 278,
      "curve_terminal": 53489.006584207455,
      "wallet_terminal_engine": 53489.006584207455,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 43489.006584207455,
      "positive_full_months": 40,
      "complete_months": 61,
      "best_observed_month_delta": 5026.797577564386,
      "worst_observed_month_delta": -3102.2219620498727,
      "observed_net_ex_best_month": 38462.20900664307
    }
  ],
  "annual": [
    {
      "case": "L1",
      "year": 2020,
      "return_pct": 4.070072217509657,
      "equity_delta": 407.007221750966,
      "partial": true
    },
    {
      "case": "L1",
      "year": 2021,
      "return_pct": 21.143574400340846,
      "equity_delta": 2200.41331477976,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2022,
      "return_pct": 9.392325241699261,
      "equity_delta": 1184.1299413797515,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2023,
      "return_pct": 17.569552647799046,
      "equity_delta": 2423.113722164262,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2024,
      "return_pct": 13.570166684915531,
      "equity_delta": 2200.3569593494667,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2025,
      "return_pct": 20.29618109869975,
      "equity_delta": 3737.546043880615,
      "partial": true
    },
    {
      "case": "L2",
      "year": 2020,
      "return_pct": 4.070072217509657,
      "equity_delta": 407.007221750966,
      "partial": true
    },
    {
      "case": "L2",
      "year": 2021,
      "return_pct": 20.96190227694732,
      "equity_delta": 2181.506683778289,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2022,
      "return_pct": 10.833298066941822,
      "equity_delta": 1363.7512335844021,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2023,
      "return_pct": 19.055800153269598,
      "equity_delta": 2658.7157617638004,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2024,
      "return_pct": 16.193693604136673,
      "equity_delta": 2689.931351729756,
      "partial": false
    },
    {
      "case": "L2",
      "year": 2025,
      "return_pct": 18.415897546942126,
      "equity_delta": 3554.4362260653434,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2020,
      "return_pct": 4.070072217509657,
      "equity_delta": 407.007221750966,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2021,
      "return_pct": 20.96190227694732,
      "equity_delta": 2181.506683778289,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2022,
      "return_pct": 10.833298066941822,
      "equity_delta": 1363.7512335844021,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2023,
      "return_pct": 19.570858488167907,
      "equity_delta": 2730.578066269918,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2024,
      "return_pct": 16.693549667156326,
      "equity_delta": 2784.958716384521,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2025,
      "return_pct": 18.430282698759303,
      "equity_delta": 3587.9709294163586,
      "partial": true
    },
    {
      "case": "L4",
      "year": 2020,
      "return_pct": 4.070072217509635,
      "equity_delta": 407.00722175096416,
      "partial": true
    },
    {
      "case": "L4",
      "year": 2021,
      "return_pct": 20.96190227694734,
      "equity_delta": 2181.5066837782906,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2022,
      "return_pct": 10.833298066941822,
      "equity_delta": 1363.7512335844021,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2023,
      "return_pct": 19.570858488167907,
      "equity_delta": 2730.578066269918,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2024,
      "return_pct": 16.693549667156326,
      "equity_delta": 2784.958716384521,
      "partial": false
    },
    {
      "case": "L4",
      "year": 2025,
      "return_pct": 18.439332100191596,
      "equity_delta": 3589.732648962301,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2020,
      "return_pct": 4.072162460030948,
      "equity_delta": 407.2162460030959,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2021,
      "return_pct": 20.951927535300708,
      "equity_delta": 2180.5124063046114,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2022,
      "return_pct": 10.834108700431223,
      "equity_delta": 1363.7682051063439,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2023,
      "return_pct": 19.57195771013449,
      "equity_delta": 2730.5810648638217,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2024,
      "return_pct": 16.69381631037472,
      "equity_delta": 2784.8754450986453,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2025,
      "return_pct": 18.43977062028026,
      "equity_delta": 3589.6615477011546,
      "partial": true
    },
    {
      "case": "M5A15",
      "year": 2020,
      "return_pct": 4.1383151615286495,
      "equity_delta": 413.8315161528644,
      "partial": true
    },
    {
      "case": "M5A15",
      "year": 2021,
      "return_pct": 20.817042962805445,
      "equity_delta": 2167.851780791716,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2022,
      "return_pct": 4.897587058423936,
      "equity_delta": 616.1988928830433,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2023,
      "return_pct": 6.392763806933699,
      "equity_delta": 843.7094359130479,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2024,
      "return_pct": 9.38882755277679,
      "equity_delta": 1318.3408234059389,
      "partial": false
    },
    {
      "case": "M5A15",
      "year": 2025,
      "return_pct": 6.343528785829067,
      "equity_delta": 974.3617363955145,
      "partial": true
    },
    {
      "case": "R5A15",
      "year": 2020,
      "return_pct": 9.89366067705193,
      "equity_delta": 989.3660677051921,
      "partial": true
    },
    {
      "case": "R5A15",
      "year": 2021,
      "return_pct": 62.07987375461765,
      "equity_delta": 6822.184581264173,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2022,
      "return_pct": 9.704845970787424,
      "equity_delta": 1728.5835554912665,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2023,
      "return_pct": 28.669112450179355,
      "equity_delta": 5601.983047992777,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2024,
      "return_pct": 39.405823615837136,
      "equity_delta": 9907.45837778875,
      "partial": false
    },
    {
      "case": "R5A15",
      "year": 2025,
      "return_pct": 52.60956979477671,
      "equity_delta": 18439.430953965297,
      "partial": true
    }
  ],
  "fills": [
    {
      "case": "L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9352.10193846799,
          "fees": 1084.2972940121856
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1378.9247509759548,
          "fees": 131.54490821015375
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1421.5405138609024,
          "fees": 368.13476372021154
        }
      },
      "entry_notional_sum": 1758160.6325340667,
      "entry_notional_turnover_initial_equity": 175.81606325340667,
      "time_weighted_entry_notional_over_initial_equity": 0.33982856568813335
    },
    {
      "case": "L2",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9213.643714369819,
          "fees": 1262.715196008023
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1772.6334288051155,
          "fees": 174.2624333359835
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1869.071335497595,
          "fees": 454.81133849039463
        }
      },
      "entry_notional_sum": 2100017.728295531,
      "entry_notional_turnover_initial_equity": 210.00177282955312,
      "time_weighted_entry_notional_over_initial_equity": 0.42535248187742786
    },
    {
      "case": "L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9265.255120056529,
          "fees": 1269.5595840452002
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1831.9498833946188,
          "fees": 181.4200419977966
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1958.5678477332644,
          "fees": 462.0538645795409
        }
      },
      "entry_notional_sum": 2123536.875610146,
      "entry_notional_turnover_initial_equity": 212.35368756101462,
      "time_weighted_entry_notional_over_initial_equity": 0.43704292697554425
    },
    {
      "case": "L4",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9266.942522320614,
          "fees": 1269.47095149157
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1832.0131507647325,
          "fees": 181.42280929244572
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1958.578897645019,
          "fees": 462.0695483033768
        }
      },
      "entry_notional_sum": 2123458.0503576463,
      "entry_notional_turnover_initial_equity": 212.34580503576464,
      "time_weighted_entry_notional_over_initial_equity": 0.4370433954778566
    },
    {
      "case": "L5",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9266.171323565983,
          "fees": 1269.4008395595017
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1831.93144885749,
          "fees": 181.4152869145674
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1958.5121426541887,
          "fees": 462.04852790455146
        }
      },
      "entry_notional_sum": 2123349.367121146,
      "entry_notional_turnover_initial_equity": 212.3349367121146,
      "time_weighted_entry_notional_over_initial_equity": 0.43701881706113144
    },
    {
      "case": "M5A15",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 5266.128011316734,
          "fees": 640.7370437766012
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 396.2086014421211,
          "fees": 37.42255942464004
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 671.9575727832712,
          "fees": 122.19992868756187
        }
      },
      "entry_notional_sum": 888175.0565278996,
      "entry_notional_turnover_initial_equity": 88.81750565278996,
      "time_weighted_entry_notional_over_initial_equity": 0.14902194017753914
    },
    {
      "case": "R5A15",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 24945.68506074423,
          "fees": 3347.0298504268617
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 6717.754361219332,
          "fees": 631.2576156600059
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 11825.567162243884,
          "fees": 1796.7711779649942
        }
      },
      "entry_notional_sum": 6404973.916946084,
      "entry_notional_turnover_initial_equity": 640.4973916946084,
      "time_weighted_entry_notional_over_initial_equity": 1.5734972089480213
    }
  ],
  "engine_metrics": {
    "L1": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 22152.56720330482,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6422818921934699,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1583.9769659425508,
      "net_profit": 12152.567203304847,
      "net_profit_percentage": 121.52567203304847,
      "average_win": 176.97421730039048,
      "average_loss": 107.76116946891474,
      "expectancy": 44.514898180603794,
      "expectancy_percentage": 0.4451489818060379,
      "expected_net_profit_every_100_trades": 44.514898180603794,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 25838.235725857012,
      "gross_loss": -13685.668522552172,
      "max_drawdown": -8.204094216098524,
      "max_underwater_period": 291,
      "annual_return": 16.480484978730516,
      "annualization": 365,
      "sharpe_ratio": 1.637362521623694,
      "calmar_ratio": 2.0088122521059795,
      "sortino_ratio": 2.974009553428036,
      "omega_ratio": 1.4439129547332037,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -212.06647348377024,
      "largest_winning_trade": 2017.5175176528205,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "L2": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 22855.348478672557,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.576603529264158,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1891.7889678344018,
      "net_profit": 12855.348478672531,
      "net_profit_percentage": 128.5534847867253,
      "average_win": 196.42352631368848,
      "average_loss": 124.58650679626759,
      "expectancy": 47.08918856656606,
      "expectancy_percentage": 0.47089188566566065,
      "expected_net_profit_every_100_trades": 47.089188566566065,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 28677.834841798518,
      "gross_loss": -15822.486363125983,
      "max_drawdown": -8.797978610941692,
      "max_underwater_period": 292,
      "annual_return": 17.180335443021754,
      "annualization": 365,
      "sharpe_ratio": 1.57536803748525,
      "calmar_ratio": 1.9527594010805234,
      "sortino_ratio": 2.77555595592524,
      "omega_ratio": 1.4160773418970698,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -218.90751136598547,
      "largest_winning_trade": 2033.7355041291291,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "L3": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 23055.772851184454,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5845221560787013,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1913.0334906225376,
      "net_profit": 13055.772851184414,
      "net_profit_percentage": 130.55772851184415,
      "average_win": 198.26638678325781,
      "average_loss": 125.1269261352065,
      "expectancy": 47.82334377723229,
      "expectancy_percentage": 0.47823343777232286,
      "expected_net_profit_every_100_trades": 47.82334377723229,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 28946.89247035564,
      "gross_loss": -15891.119619171226,
      "max_drawdown": -8.776453495338233,
      "max_underwater_period": 291,
      "annual_return": 17.376733819165977,
      "annualization": 365,
      "sharpe_ratio": 1.5821467962088316,
      "calmar_ratio": 1.9799266102641502,
      "sortino_ratio": 2.7910885331528346,
      "omega_ratio": 1.4189836348578495,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -220.84010456771128,
      "largest_winning_trade": 2033.7355041291291,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "L4": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 23057.534570730397,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5846891211583243,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1912.9633090873922,
      "net_profit": 13057.53457073037,
      "net_profit_percentage": 130.57534570730368,
      "average_win": 198.26771401232764,
      "average_loss": 125.1145801186572,
      "expectancy": 47.82979696238231,
      "expectancy_percentage": 0.4782979696238231,
      "expected_net_profit_every_100_trades": 47.82979696238231,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 28947.086245799837,
      "gross_loss": -15889.551675069464,
      "max_drawdown": -8.776453495338233,
      "max_underwater_period": 291,
      "annual_return": 17.378454022460367,
      "annualization": 365,
      "sharpe_ratio": 1.5824888024946342,
      "calmar_ratio": 1.9801226123617288,
      "sortino_ratio": 2.7920682342072305,
      "omega_ratio": 1.4190668741969679,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -220.85720716241684,
      "largest_winning_trade": 2033.7355041291291,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "L5": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 23056.614915077673,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5846676172002738,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 1912.86465437862,
      "net_profit": 13056.614915077666,
      "net_profit_percentage": 130.56614915077665,
      "average_win": 198.2570236660094,
      "average_loss": 125.10953181228112,
      "expectancy": 47.82642826035775,
      "expectancy_percentage": 0.47826428260357756,
      "expected_net_profit_every_100_trades": 47.82642826035776,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 28945.52545523737,
      "gross_loss": -15888.910540159703,
      "max_drawdown": -8.77680090479469,
      "max_underwater_period": 291,
      "annual_return": 17.37755605244038,
      "annualization": 365,
      "sharpe_ratio": 1.582686191771496,
      "calmar_ratio": 1.9799419219988426,
      "sortino_ratio": 2.7923923242824853,
      "omega_ratio": 1.4191163566028648,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -220.84580543261313,
      "largest_winning_trade": 2033.7355041291291,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "M5A15": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 16334.294185542125,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.5231714001877417,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 800.3595318888032,
      "net_profit": 6334.294185542129,
      "net_profit_percentage": 63.34294185542129,
      "average_win": 101.1523360861333,
      "average_loss": 66.40903057506566,
      "expectancy": 23.202542804183597,
      "expectancy_percentage": 0.23202542804183598,
      "expected_net_profit_every_100_trades": 23.202542804183597,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 14768.241068575462,
      "gross_loss": -8433.946883033339,
      "max_drawdown": -6.3144093425155585,
      "max_underwater_period": 220,
      "annual_return": 9.868492765557434,
      "annualization": 365,
      "sharpe_ratio": 1.4456546426941657,
      "calmar_ratio": 1.5628528703566733,
      "sortino_ratio": 2.58503649888263,
      "omega_ratio": 1.4006588567266758,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -152.5668440230159,
      "largest_winning_trade": 904.4621850848553,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R5A15": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 53489.006584207455,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6514968284429408,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 5775.05864405186,
      "net_profit": 43489.00658420746,
      "net_profit_percentage": 434.8900658420746,
      "average_win": 629.3627517827446,
      "average_loss": 381.08626122892315,
      "expectancy": 159.30039041834237,
      "expectancy_percentage": 1.5930039041834236,
      "expected_net_profit_every_100_trades": 159.30039041834237,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 91886.96176028071,
      "gross_loss": -48397.95517607324,
      "max_drawdown": -17.037682176632153,
      "max_underwater_period": 278,
      "annual_return": 37.937673778662905,
      "annualization": 365,
      "sharpe_ratio": 1.5931711100797203,
      "calmar_ratio": 2.2266921864932963,
      "sortino_ratio": 2.7621801134430224,
      "omega_ratio": 1.4290224328155796,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -2022.6004464765533,
      "largest_winning_trade": 7200.2902546924415,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    }
  }
}
```

## Todos los meses de equity observada

```csv
case,month,return_pct,equity_delta,partial
L1,2020-10,-1.908913302195192,-190.89133021951966,True
L1,2020-11,0.3499214165731068,34.324172010490656,False
L1,2020-12,5.725384517963095,563.574379959995,False
L1,2021-01,1.012038328343512,105.32290191759785,False
L1,2021-02,9.238247797288412,971.1551060934962,False
L1,2021-03,0.3741389494513747,42.964190999035054,False
L1,2021-04,-3.821038753287409,-440.43009924535363,False
L1,2021-05,-1.0575081401437258,-117.23555674293493,False
L1,2021-06,1.0096118691210743,110.74214278737236,False
L1,2021-07,6.286656937438662,696.5317841029464,False
L1,2021-08,-3.648992113940519,-429.707416501873,False
L1,2021-09,-0.9193322704022733,-104.3106595924346,False
L1,2021-10,6.993839497369536,786.2502069435832,False
L1,2021-11,3.2679843356479887,393.0826272460472,False
L1,2021-12,1.4978062007624304,186.0480867722781,False
L1,2022-01,-0.4778599363044256,-60.24581174549712,False
L1,2022-02,-1.5796156617024715,-198.1971370538813,False
L1,2022-03,3.46019724722586,427.2989825512195,False
L1,2022-04,1.2268927581707612,156.7512120046631,False
L1,2022-05,0.23622240038672082,30.550708670001768,False
L1,2022-06,0.30287322488160573,39.26320823561946,False
L1,2022-07,-0.9641123084228487,-125.36199726665654,False
L1,2022-08,-0.9416284331513425,-121.25801034662982,False
L1,2022-09,2.461885485640347,314.043570341104,False
L1,2022-10,0.45066770788204646,58.90346486999988,False
L1,2022-11,0.9741717117711213,127.90064772709411,False
L1,2022-12,4.031668601056526,534.4811033927144,False
L1,2023-01,13.75772017492638,1897.4029225346458,False
L1,2023-02,0.9212534507833547,144.53502459339325,False
L1,2023-03,0.08945107459892299,14.16322554269209,False
L1,2023-04,0.3735781582022035,59.20336515454255,False
L1,2023-05,-0.24435014821130308,-38.86842380670714,False
L1,2023-06,2.8431559737994716,451.15160871012813,False
L1,2023-07,-2.1587639403218617,-352.29167084668916,False
L1,2023-08,0.725064637583217,115.76995792470734,False
L1,2023-09,-0.23705531548804393,-38.1246972536901,False
L1,2023-10,-1.3438219355326964,-215.60940012499123,False
L1,2023-11,-0.07989806766929286,-12.64697116352545,False
L1,2023-12,2.519112610177232,398.428780899756,False
L1,2024-01,-0.38094583149491656,-61.76908736108271,False
L1,2024-02,-0.9010463003340963,-145.54506380995372,False
L1,2024-03,2.4083964339335573,385.520447745057,False
L1,2024-04,3.2611844796606837,534.6017484075855,False
L1,2024-05,0.8268644427349425,139.96724904819712,False
L1,2024-06,-2.1894109471805034,-373.6763886873341,False
L1,2024-07,-2.9331165102263634,-489.64752182306984,False
L1,2024-08,1.579979680581145,256.0217336386704,False
L1,2024-09,2.6409990514977277,434.7120704233421,False
L1,2024-10,1.2465265859218144,210.59878926858437,False
L1,2024-11,6.814767178843728,1165.6964681551908,False
L1,2024-12,0.787452111726461,143.8765143442797,False
L1,2025-01,4.199267221459224,773.2959473724804,False
L1,2025-02,1.432729165528701,274.9166155632083,False
L1,2025-03,2.8854014737276,561.592432660018,False
L1,2025-04,0.886940238629097,177.60824088439404,False
L1,2025-05,3.635879995869473,734.5362708793364,False
L1,2025-06,1.3183544690741567,276.0234884742895,False
L1,2025-07,1.8158579480202164,385.1978403813155,False
L1,2025-08,2.352387722802951,508.0732168528266,False
L1,2025-09,0.9619535332790807,212.65199928761285,False
L1,2025-10,1.994007607624515,445.0409071423019,False
L1,2025-11,0.34625430896906284,78.82118587868172,False
L1,2025-12,-3.0215767192164456,-690.2121014958502,True
L2,2020-10,-1.908913302195192,-190.89133021951966,True
L2,2020-11,0.3499214165731068,34.324172010490656,False
L2,2020-12,5.725384517963095,563.574379959995,False
L2,2021-01,1.012038328343512,105.32290191759785,False
L2,2021-02,9.238247797288412,971.1551060934962,False
L2,2021-03,0.3741389494513747,42.964190999035054,False
L2,2021-04,-3.8361563746826866,-442.17262422910244,False
L2,2021-05,-1.0575380301744985,-117.2204424931333,False
L2,2021-06,1.0097708921372517,110.74214278737236,False
L2,2021-07,6.29043329865806,696.8415254026004,False
L2,2021-08,-3.649431453451224,-429.70741650187483,False
L2,2021-09,-0.9193186773393647,-104.296084376012,False
L2,2021-10,7.428258031462742,834.9834851847863,False
L2,2021-11,2.706658639840809,326.84581222124507,False
L2,2021-12,1.500089494227086,186.0480867722781,False
L2,2022-01,-0.47857763193982494,-60.24581174549712,False
L2,2022-02,-1.5900491662967253,-199.2056223766267,False
L2,2022-03,3.454697016537689,425.93175336676904,False
L2,2022-04,2.576953685665395,328.69029378171945,False
L2,2022-05,0.23421730034485222,30.64425266499893,False
L2,2022-06,0.30904548717018976,40.5292412401177,False
L2,2022-07,-0.9720143113070567,-127.86710251324075,False
L2,2022-08,-0.9424176563547104,-122.7686624270682,False
L2,2022-09,2.46074108893346,317.53949905202717,False
L2,2022-10,0.4507657619866601,59.59917508499893,False
L2,2022-11,0.9771949542186631,129.78478877800626,False
L2,2022-12,4.034848627862897,541.1194286781974,False
L2,2023-01,14.69019567132852,2049.6150495183538,False
L2,2023-02,0.9120156310324479,145.93964857940955,False
L2,2023-03,0.08612180643940981,13.906794144388186,False
L2,2023-04,0.3674068467585556,59.3792901980014,False
L2,2023-05,-0.24323219394120077,-39.45495181452134,False
L2,2023-06,4.442831408120407,718.9234716359988,False
L2,2023-07,-1.782230624177128,-301.2072133560432,False
L2,2023-08,0.7261198937850821,120.53130768509072,False
L2,2023-09,-0.6460288645403267,-108.01537066250603,False
L2,2023-10,-1.3443694671885331,-223.32508519585463,False
L2,2023-11,-0.07568246951513702,-12.403265472750718,False
L2,2023-12,1.4339513100970924,234.8260865042339,False
L2,2024-01,-0.38056181044426873,-63.21504964893029,False
L2,2024-02,-0.7958252778756836,-131.69130356775713,False
L2,2024-03,2.382441326230844,391.1033441683321,False
L2,2024-04,3.462211813351024,581.9000984618287,False
L2,2024-05,1.4404403923455433,250.47930322861794,False
L2,2024-06,-2.1894830074441707,-386.2151095299887,False
L2,2024-07,-2.07452157785315,-357.92430650770257,False
L2,2024-08,1.5806481129307937,267.05710385218845,False
L2,2024-09,2.795838977316323,479.83516500029873,False
L2,2024-10,1.3298035520720175,234.6080669935145,False
L2,2024-11,7.105553552894794,1270.253997255215,False
L2,2024-12,0.80293862891756,153.74004202413926,False
L2,2025-01,3.5599037483444285,687.0938987452319,False
L2,2025-02,2.21851347119566,443.4366090911717,False
L2,2025-03,3.6755573219650506,750.9693903645857,False
L2,2025-04,0.594792004941147,125.99129392668692,False
L2,2025-05,3.647052686253538,777.1287002289464,False
L2,2025-06,1.4017769517024492,309.5898992689363,False
L2,2025-07,0.01248426253455115,2.7958658309362363,False
L2,2025-08,2.352277072758291,526.8610877736501,False
L2,2025-09,0.9363441775281478,214.65483335744648,False
L2,2025-10,1.5516880643867248,359.05183292531365,False
L2,2025-11,0.3462662270484307,81.36731972266352,False
L2,2025-12,-3.0725573465901768,-724.5045051702255,True
L3,2020-10,-1.908913302195192,-190.89133021951966,True
L3,2020-11,0.3499214165731068,34.324172010490656,False
L3,2020-12,5.725384517963095,563.574379959995,False
L3,2021-01,1.012038328343512,105.32290191759785,False
L3,2021-02,9.238247797288412,971.1551060934962,False
L3,2021-03,0.3741389494513747,42.964190999035054,False
L3,2021-04,-3.8361563746826866,-442.17262422910244,False
L3,2021-05,-1.0575380301744985,-117.2204424931333,False
L3,2021-06,1.0097708921372517,110.74214278737236,False
L3,2021-07,6.29043329865806,696.8415254026004,False
L3,2021-08,-3.649431453451224,-429.70741650187483,False
L3,2021-09,-0.9193186773393647,-104.296084376012,False
L3,2021-10,7.428258031462742,834.9834851847863,False
L3,2021-11,2.706658639840809,326.84581222124507,False
L3,2021-12,1.500089494227086,186.0480867722781,False
L3,2022-01,-0.47857763193982494,-60.24581174549712,False
L3,2022-02,-1.5900491662967253,-199.2056223766267,False
L3,2022-03,3.454697016537689,425.93175336676904,False
L3,2022-04,2.576953685665395,328.69029378171945,False
L3,2022-05,0.23421730034485222,30.64425266499893,False
L3,2022-06,0.30904548717018976,40.5292412401177,False
L3,2022-07,-0.9720143113070567,-127.86710251324075,False
L3,2022-08,-0.9424176563547104,-122.7686624270682,False
L3,2022-09,2.46074108893346,317.53949905202717,False
L3,2022-10,0.4507657619866601,59.59917508499893,False
L3,2022-11,0.9771949542186631,129.78478877800626,False
L3,2022-12,4.034848627862897,541.1194286781974,False
L3,2023-01,14.831082093716773,2069.271896714974,False
L3,2023-02,0.9178526835165624,147.0541076239533,False
L3,2023-03,0.09234831870894578,14.931422079900585,False
L3,2023-04,0.37223178242775656,60.240214505280164,False
L3,2023-05,-0.24556258550965104,-39.88860386671513,False
L3,2023-06,4.439513645819382,719.373205202517,False
L3,2023-07,-1.479791197213931,-250.4287250323032,False
L3,2023-08,0.7249947380861599,120.87705794912108,False
L3,2023-09,-0.6458211239488865,-108.4572344145854,False
L3,2023-10,-1.3474054126843105,-224.8178063971318,False
L3,2023-11,-0.0804950270464122,-13.249820073069714,False
L3,2023-12,1.4329051122441427,235.6723519779771,False
L3,2024-01,-0.37531908053085594,-62.61389372485064,False
L3,2024-02,-0.7888973379315267,-131.11654659779015,False
L3,2024-03,2.3891035079018463,393.94197149196043,False
L3,2024-04,3.4484690334131596,582.2069144842208,False
L3,2024-05,1.5012917380555546,262.20453019680645,False
L3,2024-06,-2.1903836831476786,-388.29952666927056,False
L3,2024-07,-1.767324728538433,-306.4393800086109,False
L3,2024-08,1.5832758661998625,269.67506029368815,False
L3,2024-09,2.7940516065692256,483.4380504119399,False
L3,2024-10,1.3493821676452855,239.99895852457485,False
L3,2024-11,7.159214956129656,1290.50858626825,False
L3,2024-12,0.7840715660228703,151.4539917136026,False
L3,2025-01,3.5686817184360287,694.7438881634771,False
L3,2025-02,2.2174202233884888,447.0883683393913,False
L3,2025-03,3.6805802351586925,758.554122103953,False
L3,2025-04,0.5986434365598425,127.91925677194376,False
L3,2025-05,3.6500192292667766,784.6120593797314,False
L3,2025-06,1.4068933324446142,313.46595870559395,False
L3,2025-07,0.003911275157975069,0.8837207675496757,False
L3,2025-08,2.3487339569955745,530.6980651618287,False
L3,2025-09,0.9402777984124588,217.44645620951633,False
L3,2025-10,1.5520571869753086,362.3000277235187,False
L3,2025-11,0.3462470663078365,82.07964624184024,False
L3,2025-12,-3.076480352745725,-731.8206401519856,True
L4,2020-10,-1.908913302195192,-190.89133021951966,True
L4,2020-11,0.3499214165731068,34.324172010490656,False
L4,2020-12,5.7253845179630725,563.5743799599932,False
L4,2021-01,1.0120383283435341,105.32290191759967,False
L4,2021-02,9.238247797288412,971.1551060934962,False
L4,2021-03,0.3741389494513747,42.964190999035054,False
L4,2021-04,-3.8361563746826866,-442.17262422910244,False
L4,2021-05,-1.0575380301744985,-117.2204424931333,False
L4,2021-06,1.0097708921372517,110.74214278737236,False
L4,2021-07,6.29043329865806,696.8415254026004,False
L4,2021-08,-3.649431453451224,-429.70741650187483,False
L4,2021-09,-0.9193186773393647,-104.296084376012,False
L4,2021-10,7.428258031462742,834.9834851847863,False
L4,2021-11,2.706658639840809,326.84581222124507,False
L4,2021-12,1.500089494227086,186.0480867722781,False
L4,2022-01,-0.47857763193982494,-60.24581174549712,False
L4,2022-02,-1.5900491662967253,-199.2056223766267,False
L4,2022-03,3.454697016537689,425.93175336676904,False
L4,2022-04,2.576953685665395,328.69029378171945,False
L4,2022-05,0.23421730034485222,30.64425266499893,False
L4,2022-06,0.30904548717018976,40.5292412401177,False
L4,2022-07,-0.9720143113070567,-127.86710251324075,False
L4,2022-08,-0.9424176563547104,-122.7686624270682,False
L4,2022-09,2.46074108893346,317.53949905202717,False
L4,2022-10,0.4507657619866601,59.59917508499893,False
L4,2022-11,0.9771949542186631,129.78478877800626,False
L4,2022-12,4.034848627862897,541.1194286781974,False
L4,2023-01,14.831082093716773,2069.271896714974,False
L4,2023-02,0.9178526835165624,147.0541076239533,False
L4,2023-03,0.09234831870894578,14.931422079900585,False
L4,2023-04,0.37223178242775656,60.240214505280164,False
L4,2023-05,-0.24556258550965104,-39.88860386671513,False
L4,2023-06,4.439513645819382,719.373205202517,False
L4,2023-07,-1.479791197213931,-250.4287250323032,False
L4,2023-08,0.7249947380861599,120.87705794912108,False
L4,2023-09,-0.6458211239488865,-108.4572344145854,False
L4,2023-10,-1.3474054126843105,-224.8178063971318,False
L4,2023-11,-0.0804950270464122,-13.249820073069714,False
L4,2023-12,1.4329051122441427,235.6723519779771,False
L4,2024-01,-0.37531908053085594,-62.61389372485064,False
L4,2024-02,-0.7888973379315267,-131.11654659779015,False
L4,2024-03,2.3891035079018463,393.94197149196043,False
L4,2024-04,3.4484690334131596,582.2069144842208,False
L4,2024-05,1.5012917380555546,262.20453019680645,False
L4,2024-06,-2.1903836831476786,-388.29952666927056,False
L4,2024-07,-1.767324728538433,-306.4393800086109,False
L4,2024-08,1.5832758661998625,269.67506029368815,False
L4,2024-09,2.7940516065692256,483.4380504119399,False
L4,2024-10,1.3493821676452855,239.99895852457485,False
L4,2024-11,7.159214956129656,1290.50858626825,False
L4,2024-12,0.7840715660228703,151.4539917136026,False
L4,2025-01,3.57734937527201,696.4312904275612,False
L4,2025-02,2.2170926390528756,447.05973026904394,False
L4,2025-03,3.680388725311512,758.5757015953968,False
L4,2025-04,0.5987990872434734,127.96257838576275,False
L4,2025-05,3.649726575955814,784.6120593797314,False
L4,2025-06,1.4067635603237871,313.4612924385401,False
L4,2025-07,0.004142759950842567,0.9360940852311614,False
L4,2025-08,2.348549839116054,530.6980651618287,False
L4,2025-09,0.94029043817494,217.46603529640925,False
L4,2025-10,1.5519467312363755,362.3020384164847,False
L4,2025-11,0.34624547252271043,82.0854764770811,False
L4,2025-12,-3.0764035677876,-731.8577129707701,True
L5,2020-10,-1.908913302195192,-190.89133021951966,True
L5,2020-11,0.35479331652974455,34.80206197152074,False
L5,2020-12,5.722375279512915,563.3055142510948,False
L5,2021-01,1.0026980329190804,104.35295258030783,False
L5,2021-02,9.238916547534837,971.1551060934962,False
L5,2021-03,0.3741637424973687,42.964190999035054,False
L5,2021-04,-3.8363339801451124,-442.16390420529206,False
L5,2021-05,-1.0575416186511033,-117.21288536823158,False
L5,2021-06,1.0098394588378135,110.74214278737236,False
L5,2021-07,6.290785482192618,696.8336953806174,False
L5,2021-08,-3.649664691344756,-429.70741650187483,False
L5,2021-09,-0.9193245935808503,-104.289837854687,False
L5,2021-10,7.428552064284388,834.9611021546953,False
L5,2021-11,2.706693133147575,326.82917346689464,False
L5,2021-12,1.5001844773305129,186.0480867722781,False
L5,2022-01,-0.47860748678001386,-60.24581174549712,False
L5,2022-02,-1.5900756919972947,-199.19645946691162,False
L5,2022-03,3.454970452525874,425.938651769613,False
L5,2022-04,2.577059853986219,328.68401300902224,False
L5,2022-05,0.23423118327543513,30.64425266500075,False
L5,2022-06,0.3090637626388615,40.5292412401177,False
L5,2022-07,-0.9720716144707264,-127.86710251324257,False
L5,2022-08,-0.9424737600749911,-122.7686624270682,False
L5,2022-09,2.4608889748064744,317.53949905202717,False
L5,2022-10,0.4507922015069221,59.59917508499893,False
L5,2022-11,0.9773061606263456,129.79197976008618,False
L5,2022-12,4.035079784694817,541.1194286781974,False
L5,2023-01,14.831867529257249,2069.267532240141,False
L5,2023-02,0.9178969495295508,147.0541076239533,False
L5,2023-03,0.09239962949247893,14.939004388501417,False
L5,2023-04,0.3722493802374327,60.240214505280164,False
L5,2023-05,-0.2455741517897292,-39.88860386671513,False
L5,2023-06,4.4396204667748185,719.356548403759,False
L5,2023-07,-1.4798558817875285,-250.4281034234773,False
L5,2023-08,0.7250287047026127,120.87705794912108,False
L5,2023-09,-0.645812404922419,-108.45072573321522,False
L5,2023-10,-1.3474381788488587,-224.812836383393,False
L5,2023-11,-0.08049879083287248,-13.249820073069714,False
L5,2023-12,1.4329985380595156,235.67668923293604,False
L5,2024-01,-0.3753362981312902,-62.61389372485428,False
L5,2024-02,-0.7889561213324181,-131.12027878590743,False
L5,2024-03,2.389077797383554,393.9193596819641,False
L5,2024-04,3.448460411818588,582.1781599484057,False
L5,2024-05,1.5012766447156656,262.1895779075494,False
L5,2024-06,-2.190486900833155,-388.2995266692669,False
L5,2024-07,-1.7674866412935475,-306.45268991545163,False
L5,2024-08,1.5834088635003463,269.68427585944664,False
L5,2024-09,2.794114650723789,483.42550397693776,False
L5,2024-10,1.3493767072724205,239.98649100315015,False
L5,2024-11,7.159646441401635,1290.5244741030692,False
L5,2024-12,0.7841060112814491,151.4539917136026,False
L5,2025-01,3.5773006516243155,696.3914496625621,False
L5,2025-02,2.2172184329334987,447.06539797933146,False
L5,2025-03,3.6804856045001166,758.5631809921724,False
L5,2025-04,0.5987259430942249,127.94158749481721,False
L5,2025-05,3.649882134165594,784.6120593797314,False
L5,2025-06,1.4068490871192996,313.467459799067,False
L5,2025-07,0.0040656629173518866,0.9186363126755168,False
L5,2025-08,2.3486462436693056,530.6980651618287,False
L5,2025-09,0.9402858197999242,217.4562457529646,False
L5,2025-10,1.5519943375629675,362.29860497951086,False
L5,2025-11,0.3462750627412081,82.08923393023724,False
L5,2025-12,-3.0764518538858088,-731.8403737437438,True
M5A15,2020-10,-1.30056677680348,-130.056677680348,True
M5A15,2020-11,0.5244356337359202,51.76149981178423,False
M5A15,2020-12,4.960102148208301,492.1266940214282,False
M5A15,2021-01,0.9171471015502419,95.51015391072178,False
M5A15,2021-02,9.218505370119146,968.8042262189811,False
M5A15,2021-03,0.6473518764466224,74.30399284086707,False
M5A15,2021-04,-2.570451447328137,-296.9501153768306,False
M5A15,2021-05,-0.6068163515392966,-68.30021307456263,False
M5A15,2021-06,1.0037952828647834,112.29658147469672,False
M5A15,2021-07,6.039114943703683,682.3895600836058,False
M5A15,2021-08,-3.408358276102441,-408.38559296510357,False
M5A15,2021-09,-0.2849034741889356,-32.9733038965569,False
M5A15,2021-10,5.7850987968540935,667.6308773680084,False
M5A15,2021-11,2.0897750058538556,255.1230279290594,False
M5A15,2021-12,0.9500113896777185,118.4025862788294,False
M5A15,2022-01,-0.6116662761865066,-76.95791370400002,False
M5A15,2022-02,-1.0261419947699801,-128.3162384880925,False
M5A15,2022-03,3.3291592439203654,412.0303691079316,False
M5A15,2022-04,0.9796378216706314,125.28039027924751,False
M5A15,2022-05,0.10252709740712351,13.24006218500108,False
M5A15,2022-06,0.2758202160874079,35.65516891264997,False
M5A15,2022-07,-1.309031850487885,-169.68476077641935,False
M5A15,2022-08,-0.7577643368228082,-96.9402640122371,False
M5A15,2022-09,1.432614701273316,181.88462079449346,False
M5A15,2022-10,0.2971302534273468,38.26406182499886,False
M5A15,2022-11,0.5324495528740592,68.77192325228316,False
M5A15,2022-12,1.6401458443569217,212.9714735071866,False
M5A15,2023-01,4.70160038631704,620.5116800226042,False
M5A15,2023-02,0.07098273243688613,9.808673547709986,False
M5A15,2023-03,0.23743964953424346,32.83363565592845,False
M5A15,2023-04,-0.012809357556853307,-1.775509685259749,False
M5A15,2023-05,0.13903954292409093,19.269852687348248,False
M5A15,2023-06,1.4836130645252243,205.90369198934422,False
M5A15,2023-07,-0.7927822275451635,-111.65889129924108,False
M5A15,2023-08,0.29565235224215947,41.31083891520939,False
M5A15,2023-09,-0.21047109740883752,-29.495600936268602,False
M5A15,2023-10,-0.8029776267749922,-112.29313339870896,False
M5A15,2023-11,0.16709905253859958,23.180477566398622,False
M5A15,2023-12,1.0515199394224295,146.11372084798313,False
M5A15,2024-01,0.04716597216452012,6.622853197652148,False
M5A15,2024-02,-0.7375733717720934,-103.61588920608119,False
M5A15,2024-03,1.569503958148677,218.8610268137927,False
M5A15,2024-04,1.7318573643858803,245.29091842097114,False
M5A15,2024-05,0.17265713240133262,24.87773548853511,False
M5A15,2024-06,-1.1274894555789117,-162.7376368068435,False
M5A15,2024-07,-2.048239172118149,-292.3019721685323,False
M5A15,2024-08,0.8462769937104264,118.29757988751953,False
M5A15,2024-09,1.3227443575428488,186.46576734692644,False
M5A15,2024-10,-0.29830848383041175,-42.60845081735715,False
M5A15,2024-11,7.25419784776018,1033.0517126820305,False
M5A15,2024-12,0.5639539946777017,86.13717856732546,False
M5A15,2025-01,0.4665802582723755,71.6664124916897,False
M5A15,2025-02,1.015085027022966,156.64384947473627,False
M5A15,2025-03,1.3279717439504068,207.00745858199116,False
M5A15,2025-04,-0.19524799075860688,-30.839908591624408,False
M5A15,2025-05,2.153496360265783,339.4860011902274,False
M5A15,2025-06,1.1168345034266558,179.85386985333207,False
M5A15,2025-07,-0.8263651955246809,-134.56324361826591,False
M5A15,2025-08,0.7745551338883105,125.08435612631729,False
M5A15,2025-09,0.04859633204541414,7.908698892024404,False
M5A15,2025-10,1.2903081831833418,210.09030021222497,False
M5A15,2025-11,0.11602381697513042,19.134961442661734,False
M5A15,2025-12,-1.0726586711347963,-177.11101965980015,True
R5A15,2020-10,-3.7936285818260918,-379.36285818260876,True
R5A15,2020-11,2.054552476815563,197.6610386826469,False
R5A15,2020-12,11.927401935408643,1171.067887205154,False
R5A15,2021-01,-0.15653150385164238,-17.201819969541248,False
R5A15,2021-02,23.82505393111782,2614.124049433847,False
R5A15,2021-03,2.6838344672376557,364.6334881377097,False
R5A15,2021-04,-6.1750820546488505,-861.4808676226021,False
R5A15,2021-05,-1.998087278380345,-261.53845378736696,False
R5A15,2021-06,1.6391362746579041,210.26680256347572,False
R5A15,2021-07,12.597952428887659,1642.5423617865708,False
R5A15,2021-08,-5.907253539468538,-867.2268572788071,False
R5A15,2021-09,-1.5994928826491894,-220.94570575747093,False
R5A15,2021-10,20.141604315842244,2737.7554349910843,False
R5A15,2021-11,7.152080460433474,1167.9558020801978,False
R5A15,2021-12,1.790466711098615,313.30034668707594,False
R5A15,2022-01,-2.257708835804073,-402.13295279549857,False
R5A15,2022-02,-4.301648375708201,-748.8919335477185,False
R5A15,2022-03,7.501680882266837,1249.8194760200677,False
R5A15,2022-04,3.9561407318321917,708.558463197849,False
R5A15,2022-05,-0.00994356356660564,-1.8513825249974616,False
R5A15,2022-06,0.7278854454010997,135.51081419502952,False
R5A15,2022-07,-4.749556576388092,-890.6635955491474,False
R5A15,2022-08,-1.810234312679404,-323.34223433256557,False
R5A15,2022-09,4.128679314473915,724.110787452224,False
R5A15,2022-10,0.9764932350276867,178.33371844499925,False
R5A15,2022-11,-1.025603638913053,-189.13158561055752,False
R5A15,2022-12,7.0582573990325415,1288.263980541582,False
R5A15,2023-01,24.29000787668798,4746.30013737889,False
R5A15,2023-02,1.6336006338286468,396.74334534266745,False
R5A15,2023-03,-1.6205851669991223,-400.01191634251154,False
R5A15,2023-04,-0.2707085177097168,-65.73659811123434,False
R5A15,2023-05,-0.13089015287925942,-31.698230067609984,False
R5A15,2023-06,6.359832781130392,1538.1720448473425,False
R5A15,2023-07,-1.333420862173007,-343.00788900057887,False
R5A15,2023-08,0.8181098945893028,207.64361413622464,False
R5A15,2023-09,-1.373112763466644,-351.35949104791507,False
R5A15,2023-10,-2.9207995580400437,-737.1274191661469,False
R5A15,2023-11,0.6852015464598793,167.8747338337198,False
R5A15,2023-12,1.9222966125378882,474.19071618992893,False
R5A15,2024-01,-0.09688738463047297,-24.35953984662774,False
R5A15,2024-02,-0.4440583411970511,-111.53749824449551,False
R5A15,2024-03,6.518714738248854,1630.0841625926005,False
R5A15,2024-04,7.375533318525895,1964.5695041462786,False
R5A15,2024-05,3.088300690812895,883.2809856485728,False
R5A15,2024-06,-2.6752935498303154,-788.7876933721382,False
R5A15,2024-07,-3.1489018544660574,-903.588949068333,False
R5A15,2024-08,0.47690909797564185,132.54151884094608,False
R5A15,2024-09,5.079465534027916,1418.4061969650684,False
R5A15,2024-10,1.1117740589067449,326.2248151783024,False
R5A15,2024-11,16.942957029471284,5026.797577564386,False
R5A15,2024-12,1.0198001610736362,353.82729738418857,False
R5A15,2025-01,8.995711385289361,3152.958665465296,False
R5A15,2025-02,2.5323108964426577,967.4069386874398,False
R5A15,2025-03,6.17511451881223,2418.7887281753356,False
R5A15,2025-04,6.814537069308035,2834.0794199537704,False
R5A15,2025-05,9.862349108081748,4381.132544922213,False
R5A15,2025-06,3.7607392829723807,1835.3890157045025,False
R5A15,2025-07,2.831844219172397,1434.0269659411933,False
R5A15,2025-08,1.432156659424888,745.7720630812182,False
R5A15,2025-09,1.5184766466362465,802.0461535838913,False
R5A15,2025-10,4.286860174855112,2298.6648446239997,False
R5A15,2025-11,1.200624973579445,671.3875758763097,False
R5A15,2025-12,-5.481807060460142,-3102.2219620498727,True

```
