# R12 N204B — datos completos

Job c3bcc979014e4052bd36ffac2cc8ee16, diez snapshots completos. Trades/motor conciliados; comparación contra original a igual fee y leverage. Curva diaria y extremos parciales; exposición de referencia con capital inicial. B/C no son muestras independientes.

```json
{
  "rows": [
    {
      "case": "L1",
      "leverage": 1,
      "engine_fee": 0.00045,
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
      "observed_net_ex_best_month": 10255.164280770176,
      "same_fee_reference": "L1",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "L3",
      "leverage": 3,
      "engine_fee": 0.00045,
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
      "observed_net_ex_best_month": 10986.50095446948,
      "same_fee_reference": "L3",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "L5",
      "leverage": 5,
      "engine_fee": 0.00045,
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
      "observed_net_ex_best_month": 10987.347382837532,
      "same_fee_reference": "L5",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R1A8_L3_F95",
      "leverage": 3,
      "engine_fee": 0.00095,
      "net": 8979.66148036967,
      "return_pct": 89.79661480369671,
      "cagr_pct": 13.077552464627429,
      "dd_engine_pct": -9.294375302940239,
      "dd_curve_pct": -9.294375302940217,
      "calmar": 1.407039423132655,
      "sharpe": 1.2786336057704855,
      "sortino": 2.17150259921872,
      "pf": 1.6105315697827227,
      "trades": 273,
      "fees": 3463.3132216976737,
      "underwater_days_engine": 328,
      "curve_terminal": 18979.661480369712,
      "wallet_terminal_engine": 18979.661480369712,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 8979.661480369712,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 1903.8963344136955,
      "worst_observed_month_delta": -619.7954427101467,
      "observed_net_ex_best_month": 7075.765145956017,
      "same_fee_reference": "R1A8_L3_F95",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R2A6_L1",
      "leverage": 1,
      "engine_fee": 0.00045,
      "net": 22947.45101803555,
      "return_pct": 229.4745101803555,
      "cagr_pct": 25.69542680275434,
      "dd_engine_pct": -15.086800369856125,
      "dd_curve_pct": -15.086800369856135,
      "calmar": 1.70317271872269,
      "sharpe": 1.6432719742512403,
      "sortino": 2.9938586234211426,
      "pf": 1.9252464114488763,
      "trades": 273,
      "fees": 2715.6914034594265,
      "underwater_days_engine": 215,
      "curve_terminal": 32947.451018035565,
      "wallet_terminal_engine": 32947.451018035565,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 22947.451018035565,
      "positive_full_months": 43,
      "complete_months": 61,
      "best_observed_month_delta": 3374.297844067929,
      "worst_observed_month_delta": -1131.4687689962302,
      "observed_net_ex_best_month": 19573.153173967636,
      "same_fee_reference": "L1",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R2A6_L3",
      "leverage": 3,
      "engine_fee": 0.00045,
      "net": 33646.44571451735,
      "return_pct": 336.4644571451735,
      "cagr_pct": 32.66114541285119,
      "dd_engine_pct": -13.375492042825854,
      "dd_curve_pct": -13.375492042825865,
      "calmar": 2.441864965286977,
      "sharpe": 1.6673336954531102,
      "sortino": 2.93500477848633,
      "pf": 1.8831897423751882,
      "trades": 273,
      "fees": 4638.3937394858685,
      "underwater_days_engine": 287,
      "curve_terminal": 43646.44571451734,
      "wallet_terminal_engine": 43646.44571451734,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 33646.44571451734,
      "positive_full_months": 43,
      "complete_months": 61,
      "best_observed_month_delta": 4344.617091174718,
      "worst_observed_month_delta": -2183.073937511035,
      "observed_net_ex_best_month": 29301.82862334262,
      "same_fee_reference": "L3",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R2A6_L3_F95",
      "leverage": 3,
      "engine_fee": 0.00095,
      "net": 22034.260114574805,
      "return_pct": 220.34260114574806,
      "cagr_pct": 25.019604651986562,
      "dd_engine_pct": -14.030530672409935,
      "dd_curve_pct": -14.030530672409968,
      "calmar": 1.7832258263178795,
      "sharpe": 1.3531375966315193,
      "sortino": 2.299874904336581,
      "pf": 1.6421933394716814,
      "trades": 273,
      "fees": 8202.336901296012,
      "underwater_days_engine": 292,
      "curve_terminal": 32034.26011457478,
      "wallet_terminal_engine": 32034.26011457478,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 22034.26011457478,
      "positive_full_months": 42,
      "complete_months": 61,
      "best_observed_month_delta": 4159.328466420146,
      "worst_observed_month_delta": -1687.9835408884355,
      "observed_net_ex_best_month": 17874.931648154634,
      "same_fee_reference": "R1A8_L3_F95",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R3A9_L1",
      "leverage": 1,
      "engine_fee": 0.00045,
      "net": 25991.369441248953,
      "return_pct": 259.9136944124896,
      "cagr_pct": 27.843953392667544,
      "dd_engine_pct": -16.83063088417821,
      "dd_curve_pct": -16.8306308841782,
      "calmar": 1.6543618349352849,
      "sharpe": 1.6107788898857278,
      "sortino": 2.953083921708469,
      "pf": 1.9038713567447356,
      "trades": 273,
      "fees": 3076.104568852793,
      "underwater_days_engine": 313,
      "curve_terminal": 35991.36944124893,
      "wallet_terminal_engine": 35991.36944124893,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 25991.369441248928,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 4274.4565106131995,
      "worst_observed_month_delta": -1378.8535988672302,
      "observed_net_ex_best_month": 21716.912930635728,
      "same_fee_reference": "L1",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R3A9_L3",
      "leverage": 3,
      "engine_fee": 0.00045,
      "net": 42095.35904107534,
      "return_pct": 420.95359041075335,
      "cagr_pct": 37.24097276822458,
      "dd_engine_pct": -15.629969623726314,
      "dd_curve_pct": -15.629969623726293,
      "calmar": 2.382664436640538,
      "sharpe": 1.65388000240241,
      "sortino": 2.904398154908151,
      "pf": 1.9004479324093184,
      "trades": 273,
      "fees": 5605.456338911144,
      "underwater_days_engine": 278,
      "curve_terminal": 52095.35904107531,
      "wallet_terminal_engine": 52095.35904107531,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 42095.35904107531,
      "positive_full_months": 42,
      "complete_months": 61,
      "best_observed_month_delta": 5109.353625963657,
      "worst_observed_month_delta": -3021.595335476879,
      "observed_net_ex_best_month": 36986.00541511165,
      "same_fee_reference": "L3",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
    },
    {
      "case": "R3A9_L3_F95",
      "leverage": 3,
      "engine_fee": 0.00095,
      "net": 28422.154065079463,
      "return_pct": 284.22154065079457,
      "cagr_pct": 29.456596481112562,
      "dd_engine_pct": -16.152890787542017,
      "dd_curve_pct": -16.152890787541985,
      "calmar": 1.8236114432118293,
      "sharpe": 1.3632669375152793,
      "sortino": 2.3020446498222693,
      "pf": 1.6651245622435058,
      "trades": 273,
      "fees": 10133.144030613075,
      "underwater_days_engine": 292,
      "curve_terminal": 38422.15406507949,
      "wallet_terminal_engine": 38422.15406507949,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 28422.154065079492,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 4583.243095142396,
      "worst_observed_month_delta": -2424.7115415253866,
      "observed_net_ex_best_month": 23838.910969937097,
      "same_fee_reference": "R1A8_L3_F95",
      "new_entries_same_fee": 0,
      "removed_entries_same_fee": 0,
      "changed_exits_same_fee": 0,
      "research_gate": true
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
      "case": "R1A8_L3_F95",
      "year": 2020,
      "return_pct": 3.5707486236852493,
      "equity_delta": 357.0748623685249,
      "partial": true
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2021,
      "return_pct": 18.62164058421374,
      "equity_delta": 1928.657255908216,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2022,
      "return_pct": 8.49427720011644,
      "equity_delta": 1043.5841421901641,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2023,
      "return_pct": 15.730188509352573,
      "equity_delta": 2096.72657477923,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2024,
      "return_pct": 13.102628550484297,
      "equity_delta": 2021.2170927408988,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2025,
      "return_pct": 8.783049938543996,
      "equity_delta": 1532.4015523826783,
      "partial": true
    },
    {
      "case": "R2A6_L1",
      "year": 2020,
      "return_pct": 6.063620363493172,
      "equity_delta": 606.3620363493173,
      "partial": true
    },
    {
      "case": "R2A6_L1",
      "year": 2021,
      "return_pct": 41.377853823423024,
      "equity_delta": 4388.684979383654,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2022,
      "return_pct": 12.280949560370068,
      "equity_delta": 1841.5341605559424,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2023,
      "return_pct": 21.64398719707834,
      "equity_delta": 3644.1074742216733,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2024,
      "return_pct": 26.093004073693173,
      "equity_delta": 5344.026923898142,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2025,
      "return_pct": 27.581079927498543,
      "equity_delta": 7122.735443626836,
      "partial": true
    },
    {
      "case": "R2A6_L3",
      "year": 2020,
      "return_pct": 7.972526922669876,
      "equity_delta": 797.2526922669877,
      "partial": true
    },
    {
      "case": "R2A6_L3",
      "year": 2021,
      "return_pct": 51.36468302811217,
      "equity_delta": 5545.974621127245,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2022,
      "return_pct": 13.56172850923285,
      "equity_delta": 2216.424117889317,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2023,
      "return_pct": 28.75639586101608,
      "equity_delta": 5337.086836004633,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2024,
      "return_pct": 34.73641364472431,
      "equity_delta": 8300.869852122349,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2025,
      "return_pct": 35.55803758045244,
      "equity_delta": 11448.837595106805,
      "partial": true
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2020,
      "return_pct": 6.975439983990617,
      "equity_delta": 697.5439983990618,
      "partial": true
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2021,
      "return_pct": 45.63980884770744,
      "equity_delta": 4882.338632268731,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2022,
      "return_pct": 10.58505293514498,
      "equity_delta": 1649.1388236896437,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2023,
      "return_pct": 24.649485351859934,
      "equity_delta": 4246.865119660641,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2024,
      "return_pct": 28.2295656404167,
      "equity_delta": 6062.549497273871,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2025,
      "return_pct": 16.32563313197586,
      "equity_delta": 4495.824043282832,
      "partial": true
    },
    {
      "case": "R3A9_L1",
      "year": 2020,
      "return_pct": 6.105629042225047,
      "equity_delta": 610.5629042225046,
      "partial": true
    },
    {
      "case": "R3A9_L1",
      "year": 2021,
      "return_pct": 53.549378453192276,
      "equity_delta": 5681.890485596137,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2022,
      "return_pct": 13.458581612226194,
      "equity_delta": 2192.7331361026554,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2023,
      "return_pct": 20.344623024296425,
      "equity_delta": 3760.7415140367266,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2024,
      "return_pct": 28.768884006139615,
      "equity_delta": 6399.905233904814,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2025,
      "return_pct": 25.642599037565226,
      "equity_delta": 7345.53616738609,
      "partial": true
    },
    {
      "case": "R3A9_L3",
      "year": 2020,
      "return_pct": 10.257544263879437,
      "equity_delta": 1025.7544263879427,
      "partial": true
    },
    {
      "case": "R3A9_L3",
      "year": 2021,
      "return_pct": 65.66481430186532,
      "equity_delta": 7240.0411694673385,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2022,
      "return_pct": 11.834374831676753,
      "equity_delta": 2161.6427168014197,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2023,
      "return_pct": 26.99555378945664,
      "equity_delta": 5514.500097501314,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2024,
      "return_pct": 37.39837682014735,
      "equity_delta": 9701.863881081437,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2025,
      "return_pct": 46.155448331277846,
      "equity_delta": 16451.556749835858,
      "partial": true
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2020,
      "return_pct": 9.121620888571247,
      "equity_delta": 912.1620888571251,
      "partial": true
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2021,
      "return_pct": 61.4484682568204,
      "equity_delta": 6705.35645730416,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2022,
      "return_pct": 8.455961553725743,
      "equity_delta": 1489.7305949838992,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2023,
      "return_pct": 22.657691404670267,
      "equity_delta": 4329.261546322185,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2024,
      "return_pct": 32.057080626402936,
      "equity_delta": 7513.061127096953,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2025,
      "return_pct": 24.14438007507007,
      "equity_delta": 7472.58225051517,
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
      "case": "R1A8_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 7178.141631843608,
          "fees": 2318.3702228461852
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1341.8826113230034,
          "fees": 315.8223149728611
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 459.63723720305785,
          "fees": 829.1206838786276
        }
      },
      "entry_notional_sum": 1821381.0585230747,
      "entry_notional_turnover_initial_equity": 182.13810585230746,
      "time_weighted_entry_notional_over_initial_equity": 0.3653732358288946
    },
    {
      "case": "R2A6_L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 18210.665750369335,
          "fees": 1982.282992390466
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1762.6140528945175,
          "fees": 181.1730756671828
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2974.171214771698,
          "fees": 552.235335401778
        }
      },
      "entry_notional_sum": 3014301.377257686,
      "entry_notional_turnover_initial_equity": 301.4301377257686,
      "time_weighted_entry_notional_over_initial_equity": 0.5545868971197383
    },
    {
      "case": "R2A6_L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 21996.979346489046,
          "fees": 2796.7012424718678
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 5283.172336139749,
          "fees": 500.86871793876526
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 6366.29403188856,
          "fees": 1340.8237790752337
        }
      },
      "entry_notional_sum": 5147188.887255833,
      "entry_notional_turnover_initial_equity": 514.7188887255833,
      "time_weighted_entry_notional_over_initial_equity": 1.1785137719156717
    },
    {
      "case": "R2A6_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 17027.127622711014,
          "fees": 5020.297081087131
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 3660.694012944754,
          "fees": 862.4971157072293
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 1346.438478919035,
          "fees": 2319.5427045016495
        }
      },
      "entry_notional_sum": 4312847.548317666,
      "entry_notional_turnover_initial_equity": 431.28475483176663,
      "time_weighted_entry_notional_over_initial_equity": 0.9485127362547282
    },
    {
      "case": "R3A9_L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 21157.240364261143,
          "fees": 2284.6005793233294
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 1905.3719447843923,
          "fees": 196.7042414104177
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2928.757132203441,
          "fees": 594.799748119045
        }
      },
      "entry_notional_sum": 3414522.576703039,
      "entry_notional_turnover_initial_equity": 341.4522576703039,
      "time_weighted_entry_notional_over_initial_equity": 0.621134114656845
    },
    {
      "case": "R3A9_L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 26689.947928988953,
          "fees": 3320.1792723087337
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 6500.204479897058,
          "fees": 588.8936754924254
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 8905.20663218931,
          "fees": 1696.3833911099848
        }
      },
      "entry_notional_sum": 6218776.796758212,
      "entry_notional_turnover_initial_equity": 621.8776796758212,
      "time_weighted_entry_notional_over_initial_equity": 1.4671775761414836
    },
    {
      "case": "R3A9_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 21197.29968997822,
          "fees": 6020.52352322096
        },
        "SPY-USDT": {
          "trades": 12,
          "net": 4917.797215234206,
          "fees": 1076.285849187951
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 2307.0571598670367,
          "fees": 3036.3346582041686
        }
      },
      "entry_notional_sum": 5326776.689681396,
      "entry_notional_turnover_initial_equity": 532.6776689681396,
      "time_weighted_entry_notional_over_initial_equity": 1.2247331887748398
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
    "R1A8_L3_F95": {
      "total": 273,
      "total_winning_trades": 143,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 18979.661480369712,
      "win_rate": 0.5238095238095238,
      "win_rate_longs": 0.4878048780487805,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.464119608893384,
      "longs_count": 82,
      "longs_percentage": 30.036630036630036,
      "shorts_percentage": 69.96336996336996,
      "shorts_count": 191,
      "fee": 3463.313221697674,
      "net_profit": 8979.661480369672,
      "net_profit_percentage": 89.79661480369671,
      "average_win": 165.64756032458126,
      "average_loss": 113.1379972772727,
      "expectancy": 32.892532895127,
      "expectancy_percentage": 0.32892532895126997,
      "expected_net_profit_every_100_trades": 32.892532895127,
      "average_holding_period": 274270.5494505495,
      "average_winning_holding_period": 377676.92307692306,
      "average_losing_holding_period": 160523.53846153847,
      "gross_profit": 23687.60112641512,
      "gross_loss": -14707.939646045452,
      "max_drawdown": -9.294375302940239,
      "max_underwater_period": 328,
      "annual_return": 13.077552464627429,
      "annualization": 365,
      "sharpe_ratio": 1.2786336057704855,
      "calmar_ratio": 1.407039423132655,
      "sortino_ratio": 2.17150259921872,
      "omega_ratio": 1.3268822990569296,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -183.02553173270303,
      "largest_winning_trade": 1805.8801216402499,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R2A6_L1": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 32947.451018035565,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6747006455753923,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 2715.6914034594265,
      "net_profit": 22947.45101803555,
      "net_profit_percentage": 229.4745101803555,
      "average_win": 327.0472554528989,
      "average_loss": 195.28699431565113,
      "expectancy": 84.05659713566135,
      "expectancy_percentage": 0.8405659713566135,
      "expected_net_profit_every_100_trades": 84.05659713566135,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 47748.89929612324,
      "gross_loss": -24801.448278087693,
      "max_drawdown": -15.086800369856125,
      "max_underwater_period": 215,
      "annual_return": 25.69542680275434,
      "annualization": 365,
      "sharpe_ratio": 1.6432719742512403,
      "calmar_ratio": 1.70317271872269,
      "sortino_ratio": 2.9938586234211426,
      "omega_ratio": 1.461821803682292,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -618.8298643785226,
      "largest_winning_trade": 3106.630983552329,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R2A6_L3": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 43646.44571451734,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.638117104668828,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 4638.393739485868,
      "net_profit": 33646.44571451735,
      "net_profit_percentage": 336.4644571451735,
      "average_win": 491.3900988099943,
      "average_loss": 299.97250954127406,
      "expectancy": 123.24705389933098,
      "expectancy_percentage": 1.2324705389933097,
      "expected_net_profit_every_100_trades": 123.24705389933098,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 71742.95442625917,
      "gross_loss": -38096.50871174181,
      "max_drawdown": -13.375492042825854,
      "max_underwater_period": 287,
      "annual_return": 32.66114541285119,
      "annualization": 365,
      "sharpe_ratio": 1.6673336954531102,
      "calmar_ratio": 2.441864965286977,
      "sortino_ratio": 2.93500477848633,
      "omega_ratio": 1.4453138741437446,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -848.2259878807681,
      "largest_winning_trade": 4414.5359188512675,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R2A6_L3_F95": {
      "total": 273,
      "total_winning_trades": 143,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 32034.26011457478,
      "win_rate": 0.5238095238095238,
      "win_rate_longs": 0.4878048780487805,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.4929030358833468,
      "longs_count": 82,
      "longs_percentage": 30.036630036630036,
      "shorts_percentage": 69.96336996336996,
      "shorts_count": 191,
      "fee": 8202.336901296014,
      "net_profit": 22034.260114574805,
      "net_profit_percentage": 220.34260114574806,
      "average_win": 394.02241082525654,
      "average_loss": 263.9303433341299,
      "expectancy": 80.71157551126304,
      "expectancy_percentage": 0.8071157551126303,
      "expected_net_profit_every_100_trades": 80.71157551126304,
      "average_holding_period": 274270.5494505495,
      "average_winning_holding_period": 377676.92307692306,
      "average_losing_holding_period": 160523.53846153847,
      "gross_profit": 56345.20474801168,
      "gross_loss": -34310.944633436884,
      "max_drawdown": -14.030530672409935,
      "max_underwater_period": 292,
      "annual_return": 25.019604651986562,
      "annualization": 365,
      "sharpe_ratio": 1.3531375966315193,
      "calmar_ratio": 1.7832258263178795,
      "sortino_ratio": 2.299874904336581,
      "omega_ratio": 1.350766810976862,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -628.5454712181372,
      "largest_winning_trade": 4111.602062663069,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R3A9_L1": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 35991.36944124893,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6561072760724753,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 3076.1045688527925,
      "net_profit": 25991.369441248957,
      "net_profit_percentage": 259.9136944124896,
      "average_win": 374.97929014895254,
      "average_loss": 226.42210173620572,
      "expectancy": 95.20648146977635,
      "expectancy_percentage": 0.9520648146977635,
      "expected_net_profit_every_100_trades": 95.20648146977635,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 54746.976361747074,
      "gross_loss": -28755.606920498125,
      "max_drawdown": -16.83063088417821,
      "max_underwater_period": 313,
      "annual_return": 27.843953392667544,
      "annualization": 365,
      "sharpe_ratio": 1.6107788898857278,
      "calmar_ratio": 1.6543618349352849,
      "sortino_ratio": 2.953083921708469,
      "omega_ratio": 1.4634815886212282,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -924.119169510839,
      "largest_winning_trade": 3912.782061562744,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R3A9_L3": {
      "total": 273,
      "total_winning_trades": 146,
      "total_losing_trades": 127,
      "starting_balance": 10000,
      "finishing_balance": 52095.35904107531,
      "win_rate": 0.5347985347985348,
      "win_rate_longs": 0.5061728395061729,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6531293658629005,
      "longs_count": 81,
      "longs_percentage": 29.67032967032967,
      "shorts_percentage": 70.32967032967034,
      "shorts_count": 192,
      "fee": 5605.456338911143,
      "net_profit": 42095.35904107534,
      "net_profit_percentage": 420.95359041075335,
      "average_win": 608.525430953778,
      "average_loss": 368.105148647057,
      "expectancy": 154.19545436291338,
      "expectancy_percentage": 1.5419545436291338,
      "expected_net_profit_every_100_trades": 154.19545436291338,
      "average_holding_period": 275608.13186813187,
      "average_winning_holding_period": 388515.20547945204,
      "average_losing_holding_period": 145809.44881889762,
      "gross_profit": 88844.71291925159,
      "gross_loss": -46749.35387817623,
      "max_drawdown": -15.629969623726314,
      "max_underwater_period": 278,
      "annual_return": 37.24097276822458,
      "annualization": 365,
      "sharpe_ratio": 1.65388000240241,
      "calmar_ratio": 2.382664436640538,
      "sortino_ratio": 2.904398154908151,
      "omega_ratio": 1.446164650489596,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -1233.6119102432428,
      "largest_winning_trade": 5031.927900192437,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    },
    "R3A9_L3_F95": {
      "total": 273,
      "total_winning_trades": 143,
      "total_losing_trades": 130,
      "starting_balance": 10000,
      "finishing_balance": 38422.15406507949,
      "win_rate": 0.5238095238095238,
      "win_rate_longs": 0.4878048780487805,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.5137496020395504,
      "longs_count": 82,
      "longs_percentage": 30.036630036630036,
      "shorts_percentage": 69.96336996336996,
      "shorts_count": 191,
      "fee": 10133.144030613075,
      "net_profit": 28422.15406507946,
      "net_profit_percentage": 284.22154065079457,
      "average_win": 497.5820360162564,
      "average_loss": 328.708285271117,
      "expectancy": 104.1104544508405,
      "expectancy_percentage": 1.041104544508405,
      "expected_net_profit_every_100_trades": 104.1104544508405,
      "average_holding_period": 274270.5494505495,
      "average_winning_holding_period": 377676.92307692306,
      "average_losing_holding_period": 160523.53846153847,
      "gross_profit": 71154.23115032466,
      "gross_loss": -42732.07708524521,
      "max_drawdown": -16.152890787542017,
      "max_underwater_period": 292,
      "annual_return": 29.456596481112562,
      "annualization": 365,
      "sharpe_ratio": 1.3632669375152793,
      "calmar_ratio": 1.8236114432118293,
      "sortino_ratio": 2.3020446498222693,
      "omega_ratio": 1.3580896431023664,
      "serenity_index": null,
      "total_open_trades": 0,
      "open_pl": 0,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -951.5284654057557,
      "largest_winning_trade": 4553.397735278629,
      "current_streak": -3,
      "avg_trades_per_day": 0.143457646020302,
      "avg_trades_per_week": 1.004203522142114,
      "avg_trades_per_month": 4.366850744857993
    }
  }
}
```

## Todos los meses

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
R1A8_L3_F95,2020-10,-1.9097903820102347,-190.9790382010233,True
R1A8_L3_F95,2020-11,0.1762326389927793,17.286696500334074,False
R1A8_L3_F95,2020-12,5.4014918169280834,530.7672040692141,False
R1A8_L3_F95,2021-01,0.9287750728197208,96.19392959495599,False
R1A8_L3_F95,2021-02,8.883282420991566,928.5933890154902,False
R1A8_L3_F95,2021-03,0.2724225731881136,31.006761830147298,False
R1A8_L3_F95,2021-04,-3.9177614971507513,-447.12898516165114,False
R1A8_L3_F95,2021-05,-1.0760082777349744,-117.99226965917842,False
R1A8_L3_F95,2021-06,0.9400630575878255,101.97566859511608,False
R1A8_L3_F95,2021-07,5.967956493344717,653.4747260625027,False
R1A8_L3_F95,2021-08,-3.7212263252888844,-431.78126162683475,False
R1A8_L3_F95,2021-09,-0.9253108751461014,-103.37033475278986,False
R1A8_L3_F95,2021-10,7.0763917021911205,783.2183231488034,False
R1A8_L3_F95,2021-11,2.355361142576462,279.14008622480105,False
R1A8_L3_F95,2021-12,1.280478466903312,155.32722263685355,False
R1A8_L3_F95,2022-01,-0.5421037276152396,-66.60141177800142,False
R1A8_L3_F95,2022-02,-1.6446245603079834,-200.95882465521208,False
R1A8_L3_F95,2022-03,3.2713962528787555,393.1620246071561,False
R1A8_L3_F95,2022-04,2.104463735214779,261.19202111766936,False
R1A8_L3_F95,2022-05,0.19192767455371573,24.322084319999703,False
R1A8_L3_F95,2022-06,0.2406184536290601,30.550959345837327,False
R1A8_L3_F95,2022-07,-1.1297050770553207,-143.78207235511945,False
R1A8_L3_F95,2022-08,-1.0433045721886303,-131.28545045270585,False
R1A8_L3_F95,2022-09,2.2678803399903913,282.40397678930094,False
R1A8_L3_F95,2022-10,0.3972801617049937,50.59257749000062,False
R1A8_L3_F95,2022-11,0.6835950572375848,87.39987027811003,False
R1A8_L3_F95,2022-12,3.5469435226808343,456.5883874831288,False
R1A8_L3_F95,2023-01,14.283525855414014,1903.8963344136955,False
R1A8_L3_F95,2023-02,0.6036782313282085,91.95958836724276,False
R1A8_L3_F95,2023-03,-0.01923672544216215,-2.948061296430751,False
R1A8_L3_F95,2023-04,0.17581711215697293,26.93909196943241,False
R1A8_L3_F95,2023-05,-0.39065018882695757,-59.96153507853887,False
R1A8_L3_F95,2023-06,3.9936850201383267,610.6025571466616,False
R1A8_L3_F95,2023-07,-1.753489246011275,-278.80135741491176,False
R1A8_L3_F95,2023-08,0.5394084197660742,84.26100477892942,False
R1A8_L3_F95,2023-09,-0.843367901101455,-132.45315437547833,False
R1A8_L3_F95,2023-10,-1.5581250418694736,-242.64386369113527,False
R1A8_L3_F95,2023-11,-0.3717385467760903,-56.988139523366044,False
R1A8_L3_F95,2023-12,1.0008663699146991,152.86410948312914,False
R1A8_L3_F95,2024-01,-0.42849787979436504,-66.10026648520034,False
R1A8_L3_F95,2024-02,-0.950211513600796,-145.95194277083647,False
R1A8_L3_F95,2024-03,2.1440463409238886,326.19500932504343,False
R1A8_L3_F95,2024-04,3.169749825061041,492.58500698956414,False
R1A8_L3_F95,2024-05,1.0462808475784957,167.74780856662255,False
R1A8_L3_F95,2024-06,-2.3129638458614266,-374.7121346107633,False
R1A8_L3_F95,2024-07,-2.1827610885754356,-345.4395422246489,False
R1A8_L3_F95,2024-08,1.3112172007868184,202.98123188604768,False
R1A8_L3_F95,2024-09,2.475725754170699,388.27668569882735,False
R1A8_L3_F95,2024-10,0.9883135092153772,158.8380379776827,False
R1A8_L3_F95,2024-11,6.7989326724203325,1103.4982334076758,False
R1A8_L3_F95,2024-12,0.6536242075465992,113.2989649808842,False
R1A8_L3_F95,2025-01,-0.385550973223836,-67.26808045324651,False
R1A8_L3_F95,2025-02,0.8053271654393068,139.9657956993251,False
R1A8_L3_F95,2025-03,3.1919543803504036,559.2290554287138,False
R1A8_L3_F95,2025-04,0.38435101835929686,69.48753818738624,False
R1A8_L3_F95,2025-05,3.4050130660400857,617.9647290777648,False
R1A8_L3_F95,2025-06,0.9853442699919279,184.91600172083417,False
R1A8_L3_F95,2025-07,-0.6398930388161195,-121.26968098538782,False
R1A8_L3_F95,2025-08,2.0895293170492657,393.4643315488247,False
R1A8_L3_F95,2025-09,0.585463774896855,112.5480901914998,False
R1A8_L3_F95,2025-10,1.1326719684657816,219.01682388216796,False
R1A8_L3_F95,2025-11,0.22573091689253033,44.14239079494291,False
R1A8_L3_F95,2025-12,-3.162309267764918,-619.7954427101467,True
R2A6_L1,2020-10,-3.428315964862161,-342.83159648621586,True
R2A6_L1,2020-11,0.13645763559375634,13.177943668742955,False
R2A6_L1,2020-12,9.679236457125452,936.0156891667903,False
R2A6_L1,2021-01,1.1417090465987823,121.0937948840201,False
R2A6_L1,2021-02,18.698964068431966,2005.9231113392307,False
R2A6_L1,2021-03,1.2837404004244046,163.46352982493772,False
R2A6_L1,2021-04,-6.713321253906457,-865.8064667822964,False
R2A6_L1,2021-05,-2.812923791527222,-338.423874169157,False
R2A6_L1,2021-06,1.6278607464995654,190.33944312825588,False
R2A6_L1,2021-07,12.665963120166545,1505.0902640228305,False
R2A6_L1,2021-08,-5.905461128546053,-790.6256066518363,False
R2A6_L1,2021-09,-1.0256974397393925,-129.21137576437832,False
R2A6_L1,2021-10,11.649400710823254,1452.4711451428411,False
R2A6_L1,2021-11,5.495928394265026,765.0703850303889,False
R2A6_L1,2021-12,2.106128086661063,309.30062937881667,False
R2A6_L1,2022-01,-1.2807540856824229,-192.0496773039995,False
R2A6_L1,2022-02,-1.981051471572659,-293.2549966098086,False
R2A6_L1,2022-03,7.364837980577321,1068.6190148742062,False
R2A6_L1,2022-04,0.9696415100873823,151.0542583059123,False
R2A6_L1,2022-05,0.46514290000216896,73.16425994500241,False
R2A6_L1,2022-06,0.7259949977824975,114.72593941267769,False
R2A6_L1,2022-07,-3.0137264824403043,-479.70406061828544,False
R2A6_L1,2022-08,-1.6093358839249117,-248.44286464033758,False
R2A6_L1,2022-09,3.541813303249941,537.9716501858566,False
R2A6_L1,2022-10,0.9009461713379352,141.692980455,False
R2A6_L1,2022-11,0.7993452718353833,126.84669050093726,False
R2A6_L1,2022-12,5.25711617579141,840.9109660487811,False
R2A6_L1,2023-01,15.556242696840062,2619.139429633993,False
R2A6_L1,2023-02,1.484940055254147,288.90578831568564,False
R2A6_L1,2023-03,0.6435087823850161,127.05840489603361,False
R2A6_L1,2023-04,-0.013563828889640028,-2.6953613236437377,False
R2A6_L1,2023-05,-0.1328389044920275,-26.393747902824543,False
R2A6_L1,2023-06,3.007171453424462,596.700873205351,False
R2A6_L1,2023-07,-2.448444683723394,-500.4448700900102,False
R2A6_L1,2023-08,0.9327519849020138,185.98003493334545,False
R2A6_L1,2023-09,-0.1886706186196685,-37.969644517303095,False
R2A6_L1,2023-10,-2.0644484453750334,-414.6829120061957,False
R2A6_L1,2023-11,0.5427058771198867,106.76207252092354,False
R2A6_L1,2023-12,3.547952329201731,701.7474065563183,False
R2A6_L1,2024-01,-0.09601689574707528,-19.664921469844558,False
R2A6_L1,2024-02,-1.2839347519978395,-262.7061942716791,False
R2A6_L1,2024-03,5.146143430059924,1039.4343907981602,False
R2A6_L1,2024-04,6.494116226314728,1379.2042939027306,False
R2A6_L1,2024-05,0.3459692457518093,78.24771284451708,False
R2A6_L1,2024-06,-2.7597667811520177,-626.3346990387217,False
R2A6_L1,2024-07,-4.977593872482522,-1098.4986826817149,False
R2A6_L1,2024-08,1.7852561781162901,374.3748358283592,False
R2A6_L1,2024-09,2.778195037482778,592.9986570889232,False
R2A6_L1,2024-10,1.1338651008964584,248.74442363336857,False
R2A6_L1,2024-11,15.208796331446628,3374.297844067929,False
R2A6_L1,2024-12,1.0325553368455642,263.92926319611433,False
R2A6_L1,2025-01,4.1978954984106975,1084.0945725754718,False
R2A6_L1,2025-02,1.4707281654900095,395.7554498299287,False
R2A6_L1,2025-03,3.4825085536446476,950.8838324445642,False
R2A6_L1,2025-04,0.632049719138772,178.5884887590255,False
R2A6_L1,2025-05,7.326647048941881,2083.261600015463,False
R2A6_L1,2025-06,3.154769808842839,962.7505516690508,False
R2A6_L1,2025-07,1.8098576308425374,569.7440883795571,False
R2A6_L1,2025-08,1.5067300850990284,482.9038907921313,False
R2A6_L1,2025-09,-0.1608728577602636,-52.33628105774187,False
R2A6_L1,2025-10,4.5003175259144435,1461.7194131174438,False
R2A6_L1,2025-11,0.40315325795354795,136.83860609817202,False
R2A6_L1,2025-12,-3.3201427042496623,-1131.4687689962302,True
R2A6_L3,2020-10,-3.428315964862161,-342.83159648621586,True
R2A6_L3,2020-11,0.7151495995875612,69.06320116922507,False
R2A6_L3,2020-12,11.011675755986538,1071.0210875839784,False
R2A6_L3,2021-01,2.0582382388387055,222.23318365628074,False
R2A6_L3,2021-02,18.61511546277901,2051.2900192077414,False
R2A6_L3,2021-03,1.2698982939906678,165.98556010361244,False
R2A6_L3,2021-04,-6.110435484626054,-808.8237689759608,False
R2A6_L3,2021-05,-1.4930155919905985,-185.55104741871764,False
R2A6_L3,2021-06,1.6300247961382075,199.55393785220258,False
R2A6_L3,2021-07,12.616978180653394,1569.7969278111104,False
R2A6_L3,2021-08,-5.918657182426756,-829.3067081930658,False
R2A6_L3,2021-09,-1.5994874583875496,-210.8513272975997,False
R2A6_L3,2021-10,14.798764813785148,1919.633538252414,False
R2A6_L3,2021-11,7.489743897993173,1115.3137175487973,False
R2A6_L3,2021-12,2.1035206098676484,336.7005885804301,False
R2A6_L3,2022-01,-1.277856107204367,-208.84292833850122,False
R2A6_L3,2022-02,-3.1806344726525992,-513.1757917013601,False
R2A6_L3,2022-03,6.993050429631742,1092.3989946512374,False
R2A6_L3,2022-04,3.352886685543499,560.3883234922287,False
R2A6_L3,2022-05,0.4667030591129384,80.61826735000432,False
R2A6_L3,2022-06,0.7261491689523725,126.02038663459462,False
R2A6_L3,2022-07,-3.0156511909145034,-527.1549644533843,False
R2A6_L3,2022-08,-1.6110197299066598,-273.12390127827894,False
R2A6_L3,2022-09,3.5438634690867277,591.1290321571942,False
R2A6_L3,2022-10,0.9009485123622429,155.60718475499743,False
R2A6_L3,2022-11,0.40191407585046246,70.04193542446592,False
R2A6_L3,2022-12,6.072523581165612,1062.5175791961192,False
R2A6_L3,2023-01,23.408936893349043,4344.617091174718,False
R2A6_L3,2023-02,1.5646940353180705,358.38172340413803,False
R2A6_L3,2023-03,-0.2649683944646819,-61.63867086639584,False
R2A6_L3,2023-04,-0.016670441041666262,-3.8677109556811047,False
R2A6_L3,2023-05,-0.13216006936004332,-30.65736142026435,False
R2A6_L3,2023-06,6.36186658518918,1473.820963772545,False
R2A6_L3,2023-07,-2.2939168412308586,-565.2281627026459,False
R2A6_L3,2023-08,0.8186210368709368,197.0836638233668,False
R2A6_L3,2023-09,-1.373192203615281,-333.30344951868756,False
R2A6_L3,2023-10,-2.6786138313937835,-641.2296021269321,False
R2A6_L3,2023-11,0.5419264684611624,126.25602303821142,False
R2A6_L3,2023-12,2.018675849154805,472.8523283822615,False
R2A6_L3,2024-01,-0.09150002932988288,-21.865522523454274,False
R2A6_L3,2024-02,-0.4481809194786579,-107.00262419184583,False
R2A6_L3,2024-03,6.208057718096804,1475.52309544745,False
R2A6_L3,2024-04,6.715613072850823,1695.2486148462012,False
R2A6_L3,2024-05,2.50427759493137,674.6183717491986,False
R2A6_L3,2024-06,-2.7660602211984076,-763.7994062405633,False
R2A6_L3,2024-07,-3.687804761211555,-990.1556936083543,False
R2A6_L3,2024-08,1.550667788859661,400.99191465154945,False
R2A6_L3,2024-09,4.499376460216187,1181.5496223845767,False
R2A6_L3,2024-10,1.562853242336315,428.8757899671182,False
R2A6_L3,2024-11,14.353280346663478,4000.3629249853147,False
R2A6_L3,2024-12,1.0245109666666474,326.5227646551575,False
R2A6_L3,2025-01,7.527535409296049,2423.686352135006,False
R2A6_L3,2025-02,2.4733699257609043,856.312685368328,False
R2A6_L3,2025-03,5.677158906314794,2014.1201344561123,False
R2A6_L3,2025-04,1.1861907488500911,444.7234007143343,False
R2A6_L3,2025-05,7.322051833196852,2777.7265833495767,False
R2A6_L3,2025-06,2.7048422470051126,1101.2542674664874,False
R2A6_L3,2025-07,2.3207296872777228,970.4231336793819,False
R2A6_L3,2025-08,1.5125340586546354,647.1506242697433,False
R2A6_L3,2025-09,1.5069715953564211,654.5230528934553,False
R2A6_L3,2025-10,3.260920201749151,1437.6591185390862,False
R2A6_L3,2025-11,0.6684918759129133,304.3321797463286,False
R2A6_L3,2025-12,-4.763466765714652,-2183.073937511035,True
R2A6_L3_F95,2020-10,-3.5001337768203356,-350.013377682033,True
R2A6_L3_F95,2020-11,0.311936171523608,30.10179882219927,False
R2A6_L3_F95,2020-12,10.510808713656928,1017.4555772588956,False
R2A6_L3_F95,2021-01,1.9300202711361347,206.4647676828099,False
R2A6_L3_F95,2021-02,18.302242723998894,1995.678151014421,False
R2A6_L3_F95,2021-03,0.964167291383089,124.37456194546576,False
R2A6_L3_F95,2021-04,-6.3749818357756505,-830.2815535691661,False
R2A6_L3_F95,2021-05,-1.6077624475968721,-196.04701458435375,False
R2A6_L3_F95,2021-06,1.5752315609898426,188.99207541557735,False
R2A6_L3_F95,2021-07,12.16844995859212,1482.9355315496214,False
R2A6_L3_F95,2021-08,-6.059019314539449,-828.2473710087124,False
R2A6_L3_F95,2021-09,-1.7391084950499236,-223.3261069212349,False
R2A6_L3_F95,2021-10,13.972911133176735,1763.1140887953989,False
R2A6_L3_F95,2021-11,6.436559811826914,925.6546123091193,False
R2A6_L3_F95,2021-12,1.783690225210477,273.0268896397847,False
R2A6_L3_F95,2022-01,-1.3651676862913797,-212.69152323600065,False
R2A6_L3_F95,2022-02,-3.2925762122101965,-505.9764788881803,False
R2A6_L3_F95,2022-03,6.596982343377733,980.3917050564905,False
R2A6_L3_F95,2022-04,2.709765584589219,429.27039647400306,False
R2A6_L3_F95,2022-05,0.37947679553045344,61.7442016199966,False
R2A6_L3_F95,2022-06,0.6281194851371241,102.58837450555438,False
R2A6_L3_F95,2022-07,-3.159335607445568,-519.2434197689727,False
R2A6_L3_F95,2022-08,-1.793328970764485,-285.42562721835384,False
R2A6_L3_F95,2022-09,3.399531897689023,531.3652018930461,False
R2A6_L3_F95,2022-10,0.7957426962093006,128.6071822749982,False
R2A6_L3_F95,2022-11,0.08776466873130495,14.297314456094682,False
R2A6_L3_F95,2022-12,5.668336514874683,924.2114965209676,False
R2A6_L3_F95,2023-01,24.14140859618117,4159.328466420146,False
R2A6_L3_F95,2023-02,1.1396052999074424,243.74276925993036,False
R2A6_L3_F95,2023-03,-0.3440923072801416,-74.43436685012784,False
R2A6_L3_F95,2023-04,-0.22175987407614395,-47.80623595126599,False
R2A6_L3_F95,2023-05,-0.3790456707811085,-81.53216312808945,False
R2A6_L3_F95,2023-06,5.9489256868462626,1274.7548282248572,False
R2A6_L3_F95,2023-07,-2.6816182936147404,-608.809805771587,False
R2A6_L3_F95,2023-08,0.6315309580066542,139.53212308154616,False
R2A6_L3_F95,2023-09,-1.7888218951178092,-397.72303009783354,False
R2A6_L3_F95,2023-10,-3.058393421567307,-667.8330519540104,False
R2A6_L3_F95,2023-11,0.1854204133436843,39.25023993677678,False
R2A6_L3_F95,2023-12,1.2655685842836384,268.39534649029883,False
R2A6_L3_F95,2024-01,-0.20823664604199266,-44.720665909517265,False
R2A6_L3_F95,2024-02,-0.8137813220509438,-174.40282525793737,False
R2A6_L3_F95,2024-03,5.696529980854148,1210.8978819737204,False
R2A6_L3_F95,2024-04,6.160889962565963,1384.2078692052128,False
R2A6_L3_F95,2024-05,1.7359192291121595,414.0491775925293,False
R2A6_L3_F95,2024-06,-3.1357349654120625,-760.9148757686562,False
R2A6_L3_F95,2024-07,-4.074374765639277,-957.6819164299341,False
R2A6_L3_F95,2024-08,1.2852788936157378,289.79596070899424,False
R2A6_L3_F95,2024-09,4.01209558243214,916.2469695389445,False
R2A6_L3_F95,2024-10,1.3521515455205746,321.18148046291026,False
R2A6_L3_F95,2024-11,13.422488405632404,3231.403095913465,False
R2A6_L3_F95,2024-12,0.8514164718340878,232.48734524413885,False
R2A6_L3_F95,2025-01,-0.4181161011979406,-115.14263523217232,False
R2A6_L3_F95,2025-02,0.1569926663651966,43.05255957042391,False
R2A6_L3_F95,2025-03,5.0725873363294705,1393.2543887267748,False
R2A6_L3_F95,2025-04,0.7376193661725816,212.87400143503692,False
R2A6_L3_F95,2025-05,6.863481237412605,1995.3838247204185,False
R2A6_L3_F95,2025-06,1.8198881582181414,565.4002725851205,False
R2A6_L3_F95,2025-07,1.3820555750301722,437.18921242935176,False
R2A6_L3_F95,2025-08,1.271976895964344,407.92868511943016,False
R2A6_L3_F95,2025-09,0.9703065849010706,315.13982469036273,False
R2A6_L3_F95,2025-10,2.392274321160137,784.5108671857597,False
R2A6_L3_F95,2025-11,0.4294968928021836,144.21658294076042,False
R2A6_L3_F95,2025-12,-5.0055493286105035,-1687.9835408884355,True
R3A9_L1,2020-10,-3.7936285818260918,-379.36285818260876,True
R3A9_L1,2020-11,0.8308916251405618,79.93706829652365,False
R3A9_L1,2020-12,9.380771430621348,909.9886941085897,False
R3A9_L1,2021-01,0.5370352902233977,56.98246728702725,False
R3A9_L1,2021-02,23.67945189637133,2526.016274770185,False
R3A9_L1,2021-03,2.2692050501397887,299.38896717068565,False
R3A9_L1,2021-04,-6.744430029806403,-910.0226130804967,False
R3A9_L1,2021-05,-2.8068411821995154,-353.1828050408967,False
R3A9_L1,2021-06,1.6317096935790643,199.55393785220258,False
R3A9_L1,2021-07,12.699100313312428,1578.409165164354,False
R3A9_L1,2021-08,-5.92035963720785,-829.3067081930658,False
R3A9_L1,2021-09,-1.0256976628231662,-135.17055710764544,False
R3A9_L1,2021-10,16.326656962702657,2129.5235876180104,False
R3A9_L1,2021-11,5.4919714936087605,833.2833585620101,False
R3A9_L1,2021-12,1.7894210357711327,286.41541059376686,False
R3A9_L1,2022-01,-2.0024851467267735,-326.25395916850175,False
R3A9_L1,2022-02,-1.9475099528045714,-310.943322996538,False
R3A9_L1,2022-03,9.87132081719424,1545.3805551398818,False
R3A9_L1,2022-04,0.8629807517438914,148.43818357730925,False
R3A9_L1,2022-05,0.26361260447598234,45.734348055004375,False
R3A9_L1,2022-06,0.7259527961338774,126.27810372908789,False
R3A9_L1,2022-07,-4.744834046186719,-831.3465153849502,False
R3A9_L1,2022-08,-1.8080716891960336,-301.7624780934675,False
R3A9_L1,2022-09,4.127562654815842,676.4240723831499,False
R3A9_L1,2022-10,0.9771133175993985,166.73854819499684,False
R3A9_L1,2022-11,1.2899454684983214,222.27232153588193,False
R3A9_L1,2022-12,5.911584539605941,1031.7732791308008,False
R3A9_L1,2023-01,15.555204717166294,2875.4086064570984,False
R3A9_L1,2023-02,1.5578224751206182,332.7601517917137,False
R3A9_L1,2023-03,-0.18627127775825425,-40.40849007646102,False
R3A9_L1,2023-04,-0.27250930031852416,-59.006293806927715,False
R3A9_L1,2023-05,-0.13461686546040186,-29.06908583086988,False
R3A9_L1,2023-06,3.0061113477192203,648.2640467110141,False
R3A9_L1,2023-07,-2.448177439048893,-543.8169708656569,False
R3A9_L1,2023-08,0.9321220649171735,201.98449896527381,False
R3A9_L1,2023-09,-0.18898041901227458,-41.33248003256085,False
R3A9_L1,2023-10,-2.3148208983421514,-505.3247194496762,False
R3A9_L1,2023-11,0.6880275469426822,146.71943732166983,False
R3A9_L1,2023-12,3.6074222792050747,774.5628128521093,False
R3A9_L1,2024-01,-0.09238261220505528,-20.551369432570937,False
R3A9_L1,2024-02,-1.2837150669234298,-285.31050900002083,False
R3A9_L1,2024-03,5.1302294866802045,1125.5757436157255,False
R3A9_L1,2024-04,6.942256554209392,1601.2760369301322,False
R3A9_L1,2024-05,0.2001972082366743,49.382481078057026,False
R3A9_L1,2024-06,-2.682203746286971,-662.9415358932529,False
R3A9_L1,2024-07,-5.732478384121942,-1378.8535988672302,False
R3A9_L1,2024-08,1.9983518380229714,453.1163931931369,False
R3A9_L1,2024-09,2.9773288409785437,688.5853505581472,False
R3A9_L1,2024-10,1.1082198556141343,263.935935184345,False
R3A9_L1,2024-11,17.750959852744288,4274.4565106131995,False
R3A9_L1,2024-12,1.0271130655601368,291.2337959251454,False
R3A9_L1,2025-01,4.1825104791797685,1198.1149785276757,False
R3A9_L1,2025-02,1.6243381837622417,484.7666470058248,False
R3A9_L1,2025-03,3.4898466304245535,1058.4256349676507,False
R3A9_L1,2025-04,-2.2323749413892036,-700.6786601077547,False
R3A9_L1,2025-05,7.898499446589979,2423.770021316177,False
R3A9_L1,2025-06,3.9954293310725086,1322.8959167418288,False
R3A9_L1,2025-07,1.809231227784025,622.9749010831729,False
R3A9_L1,2025-08,1.4382142318306812,504.1818583492641,False
R3A9_L1,2025-09,-0.22676254141232866,-80.63740502834844,False
R3A9_L1,2025-10,4.505201158817362,1598.4294752993083,False
R3A9_L1,2025-11,0.4031404651419601,149.47673064032278,False
R3A9_L1,2025-12,-3.320615564054108,-1236.183931409032,True
R3A9_L3,2020-10,-3.7936285818260918,-379.36285818260876,True
R3A9_L3,2020-11,2.4205234946037324,232.86978234826347,False
R3A9_L3,2020-12,11.896754234244856,1172.247502222288,False
R3A9_L3,2021-01,1.7752882607514175,195.7389239909444,False
R3A9_L3,2021-02,23.76620484537475,2666.9230963611535,False
R3A9_L3,2021-03,2.263285821199812,314.3345602282516,False
R3A9_L3,2021-04,-6.1592785102531415,-874.7869906369597,False
R3A9_L3,2021-05,-1.97703983408265,-263.49915767507264,False
R3A9_L3,2021-06,1.6328231852281494,213.3196112381247,False
R3A9_L3,2021-07,12.614870775758646,1674.9753527609282,False
R3A9_L3,2021-08,-5.90748003144631,-883.3313006734897,False
R3A9_L3,2021-09,-1.5994911168352277,-225.03925939858163,False
R3A9_L3,2021-10,20.146818130336342,2789.2039259884586,False
R3A9_L3,2021-11,7.858836815761672,1307.2069452875003,False
R3A9_L3,2021-12,1.8114881140820716,324.99546199608085,False
R3A9_L3,2022-01,-1.9998210300206654,-365.2832216265015,False
R3A9_L3,2022-02,-4.139578772736208,-741.0058104545933,False
R3A9_L3,2022-03,8.433293485343274,1447.1115491598212,False
R3A9_L3,2022-04,3.661012029699462,681.1905274347519,False
R3A9_L3,2022-05,0.2630921220817095,50.74470505500358,False
R3A9_L3,2022-06,0.7272653807389062,140.64260361699053,False
R3A9_L3,2022-07,-4.747911230987079,-924.854932170485,False
R3A9_L3,2022-08,-1.8066688263936315,-335.21549509456236,False
R3A9_L3,2022-09,4.129502125640383,752.3591756948153,False
R3A9_L3,2022-10,0.9766806528310745,185.2908205950007,False
R3A9_L3,2022-11,-0.12355451186958355,-23.669060481297493,False
R3A9_L3,2022-12,6.7648808516372005,1294.3318550724762,False
R3A9_L3,2023-01,23.395002488193526,4778.999701520235,False
R3A9_L3,2023-02,1.6340699071628606,411.890818257325,False
R3A9_L3,2023-03,-1.3764358283238298,-352.6198566674393,False
R3A9_L3,2023-04,-0.27264842246085275,-68.88655694597765,False
R3A9_L3,2023-05,-0.13254398127493516,-33.39687158868037,False
R3A9_L3,2023-06,6.362272546053149,1600.9657152380787,False
R3A9_L3,2023-07,-2.2944107017516924,-614.0850573848111,False
R3A9_L3,2023-08,0.817399821604492,213.75255626939543,False
R3A9_L3,2023-09,-1.37289301878053,-361.95032220183566,False
R3A9_L3,2023-10,-2.922704098493689,-759.9646890458971,False
R3A9_L3,2023-11,0.6857978822957467,173.1100872842835,False
R3A9_L3,2023-12,2.072316791075157,526.6845727666368,False
R3A9_L3,2024-01,-0.09178431093921358,-23.810629414037976,False
R3A9_L3,2024-02,-0.4465171632862974,-115.72888894349671,False
R3A9_L3,2024-03,6.515698184072005,1681.2064360400582,False
R3A9_L3,2024-04,7.347928469568421,2019.4756603482165,False
R3A9_L3,2024-05,2.726059839087136,804.271642112366,False
R3A9_L3,2024-06,-2.681660422087362,-812.7402804692392,False
R3A9_L3,2024-07,-4.451706875888506,-1313.0136859941267,False
R3A9_L3,2024-08,0.7692930950131682,216.79909258522457,False
R3A9_L3,2024-09,5.078472749087681,1442.2048912374667,False
R3A9_L3,2024-10,1.1154960862755914,332.8707546557016,False
R3A9_L3,2024-11,16.933263061359916,5109.353625963657,False
R3A9_L3,2024-12,1.0230905325991024,360.9752629596478,False
R3A9_L3,2025-01,9.193845513527798,3277.0361178038365,False
R3A9_L3,2025-02,2.531236371652401,985.1784179617607,False
R3A9_L3,2025-03,6.113590074710906,2439.6902839482427,False
R3A9_L3,2025-04,2.18612879651221,925.7316972392655,False
R3A9_L3,2025-05,9.900874948086935,4284.251044637109,False
R3A9_L3,2025-06,3.764984705283192,1790.4644494509485,False
R3A9_L3,2025-07,2.7654212631509134,1364.6290436225245,False
R3A9_L3,2025-08,1.4394124523849694,729.9373301828964,False
R3A9_L3,2025-09,1.5190747717011455,781.4230101716748,False
R3A9_L3,2025-10,4.291127022615471,2240.918519510087,False
R3A9_L3,2025-11,1.2006158748729678,653.892170784391,False
R3A9_L3,2025-12,-5.48215221551197,-3021.595335476879,True
R3A9_L3_F95,2020-10,-3.9381199556223656,-393.8119955622369,True
R3A9_L3_F95,2020-11,1.8438188138560463,177.12070172020685,False
R3A9_L3_F95,2020-12,11.538564473475255,1128.8533826991552,False
R3A9_L3_F95,2021-01,1.7215514822902511,187.8584881906354,False
R3A9_L3_F95,2021-02,23.50936857310515,2609.544749148672,False
R3A9_L3_F95,2021-03,1.9367854682308394,265.524868995386,False
R3A9_L3_F95,2021-04,-6.483493592840873,-906.0740773989946,False
R3A9_L3_F95,2021-05,-2.1952709403062154,-286.90031301784074,False
R3A9_L3_F95,2021-06,1.5709433868553058,200.79980293529843,False
R3A9_L3_F95,2021-07,12.414651022950407,1611.7836653013928,False
R3A9_L3_F95,2021-08,-6.1163937337455625,-892.6692717934948,False
R3A9_L3_F95,2021-09,-1.7391061431688226,-238.29284549002114,False
R3A9_L3_F95,2021-10,19.893262807906975,2678.376616154823,False
R3A9_L3_F95,2021-11,7.496692784340486,1210.124678376782,False
R3A9_L3_F95,2021-12,1.5287946662440488,265.28009590152215,False
R3A9_L3_F95,2022-01,-2.1312983807405317,-375.4818875009987,False
R3A9_L3_F95,2022-02,-4.378402758194067,-754.9258086316149,False
R3A9_L3_F95,2022-03,8.187044682654431,1349.8071321706157,False
R3A9_L3_F95,2022-04,2.932483290072252,523.0646392918861,False
R3A9_L3_F95,2022-05,0.19477845005222427,35.76128957999754,False
R3A9_L3_F95,2022-06,0.6246762373776527,114.91384090130668,False
R3A9_L3_F95,2022-07,-5.060364592834743,-936.706770781635,False
R3A9_L3_F95,2022-08,-2.027165807005804,-356.2531252306617,False
R3A9_L3_F95,2022-09,3.9995910455696837,688.6375017002283,False
R3A9_L3_F95,2022-10,0.8951060251501053,160.28068667000116,False
R3A9_L3_F95,2022-11,-0.513085096099053,-92.69711429289964,False
R3A9_L3_F95,2022-12,6.305415171388606,1133.3302111076737,False
R3A9_L3_F95,2023-01,23.986933238196627,4583.243095142396,False
R3A9_L3_F95,2023-02,1.24850090541071,295.77601006630357,False
R3A9_L3_F95,2023-03,-1.648880578430334,-395.5049186043325,False
R3A9_L3_F95,2023-04,-0.5525974717572879,-130.36196171738993,False
R3A9_L3_F95,2023-05,-0.38036612056526753,-89.23541854501673,False
R3A9_L3_F95,2023-06,6.03434990324172,1410.2979297386519,False
R3A9_L3_F95,2023-07,-2.681716717151228,-664.5686595503576,False
R3A9_L3_F95,2023-08,0.6318287725948446,152.37748304182242,False
R3A9_L3_F95,2023-09,-1.7891257699150453,-434.2078120594888,False
R3A9_L3_F95,2023-10,-3.3956727948680987,-809.3608140633114,False
R3A9_L3_F95,2023-11,0.34301855673193327,78.9824377940422,False
R3A9_L3_F95,2023-12,1.4361769197818175,331.82417507886566,False
R3A9_L3_F95,2024-01,-0.20245545309247603,-47.44849390137824,False
R3A9_L3_F95,2024-02,-0.7240272077881693,-169.3431739279149,False
R3A9_L3_F95,2024-03,6.287630188994187,1459.9700628783903,False
R3A9_L3_F95,2024-04,7.0626234058353,1743.0334976291888,False
R3A9_L3_F95,2024-05,2.2348866041037807,590.5178873831792,False
R3A9_L3_F95,2024-06,-3.0376641801427073,-820.5715295779373,False
R3A9_L3_F95,2024-07,-5.03203932388443,-1318.0254009325508,False
R3A9_L3_F95,2024-08,0.45023399043848666,111.99410020406503,False
R3A9_L3_F95,2024-09,4.807354083632154,1201.1961448153816,False
R3A9_L3_F95,2024-10,0.724776017515727,189.80313875908905,False
R3A9_L3_F95,2024-11,16.342462918154045,4310.755532466541,False
R3A9_L3_F95,2024-12,0.8510688909451947,261.1793613008995,False
R3A9_L3_F95,2025-01,0.1632503710738531,50.52529083304762,False
R3A9_L3_F95,2025-02,-0.34633514970490165,-107.3642327186426,False
R3A9_L3_F95,2025-03,5.575496390941237,1722.423206379317,False
R3A9_L3_F95,2025-04,1.3935323570485547,454.5027532635613,False
R3A9_L3_F95,2025-05,9.691729229458112,3205.0217911341897,False
R3A9_L3_F95,2025-06,2.9667000241790698,1076.160958826942,False
R3A9_L3_F95,2025-07,2.308072748222756,862.0845957925194,False
R3A9_L3_F95,2025-08,1.1163254123432775,426.58060572583054,False
R3A9_L3_F95,2025-09,1.1163607848861945,431.3563012077939,False
R3A9_L3_F95,2025-10,3.5691665465555245,1394.5041746806528,False
R3A9_L3_F95,2025-11,0.9427774236349995,381.4983469153449,False
R3A9_L3_F95,2025-12,-5.9361018416387745,-2424.7115415253866,True

```
