# R12 N204C — datos completos

Job 282a6acd8de14f73ad8881c111200746, diez snapshots completos. Trades/motor conciliados; comparación contra original a igual fee y leverage. Curva diaria, extremos parciales y exposición de referencia con capital inicial. B/C no son muestras independientes.

```json
{
  "rows": [
    {
      "case": "L1",
      "leverage": 1,
      "engine_fee": 0.00045,
      "net": 12307.768574629501,
      "return_pct": 123.07768574629499,
      "cagr_pct": 16.63656691119437,
      "dd_engine_pct": -8.182245647817844,
      "dd_curve_pct": -8.182245647817865,
      "calmar": 2.0332519490699044,
      "sharpe": 1.657760787872279,
      "sortino": 2.986015288408941,
      "pf": 1.9033210447635505,
      "trades": 280,
      "fees": 1596.8976281268197,
      "underwater_days_engine": 219,
      "curve_terminal": 22307.768574629506,
      "wallet_terminal_engine": 22307.768574629506,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 12307.768574629506,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 1888.0956663202141,
      "worst_observed_month_delta": -619.2726655700426,
      "observed_net_ex_best_month": 10419.672908309292,
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
      "net": 13239.619171923641,
      "return_pct": 132.3961917192364,
      "cagr_pct": 17.55567750901328,
      "dd_engine_pct": -9.057235280291742,
      "dd_curve_pct": -9.057235280291732,
      "calmar": 1.9383042358647653,
      "sharpe": 1.5693937539620852,
      "sortino": 2.7272080768780214,
      "pf": 1.8049692385580105,
      "trades": 280,
      "fees": 2012.6368192497744,
      "underwater_days_engine": 219,
      "curve_terminal": 23239.619171923638,
      "wallet_terminal_engine": 23239.619171923638,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13239.619171923638,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2032.9786450637184,
      "worst_observed_month_delta": -887.565188090517,
      "observed_net_ex_best_month": 11206.64052685992,
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
      "net": 13239.442379846789,
      "return_pct": 132.3944237984679,
      "cagr_pct": 17.555505981887354,
      "dd_engine_pct": -9.057883731399553,
      "dd_curve_pct": -9.057883731399608,
      "calmar": 1.9381465364840598,
      "sharpe": 1.569754072854379,
      "sortino": 2.7281116510374783,
      "pf": 1.8050568929499935,
      "trades": 280,
      "fees": 2012.4242239197674,
      "underwater_days_engine": 219,
      "curve_terminal": 23239.442379846816,
      "wallet_terminal_engine": 23239.442379846816,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 13239.442379846816,
      "positive_full_months": 45,
      "complete_months": 61,
      "best_observed_month_delta": 2032.966018077277,
      "worst_observed_month_delta": -887.5608787233687,
      "observed_net_ex_best_month": 11206.476361769539,
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
      "net": 8985.737471167342,
      "return_pct": 89.85737471167342,
      "cagr_pct": 13.084494757736564,
      "dd_engine_pct": -9.299572126581134,
      "dd_curve_pct": -9.29957212658109,
      "calmar": 1.4069996532783393,
      "sharpe": 1.2578757481769922,
      "sortino": 2.1073802362844702,
      "pf": 1.5915854784220584,
      "trades": 280,
      "fees": 3622.8027742579666,
      "underwater_days_engine": 220,
      "curve_terminal": 18985.73747116734,
      "wallet_terminal_engine": 18985.73747116734,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 8985.73747116734,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 1873.133979805667,
      "worst_observed_month_delta": -751.4818716576483,
      "observed_net_ex_best_month": 7112.603491361673,
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
      "net": 23752.54202079666,
      "return_pct": 237.5254202079666,
      "cagr_pct": 26.278804344483575,
      "dd_engine_pct": -14.05970492502373,
      "dd_curve_pct": -14.059704925023752,
      "calmar": 1.8690864768941244,
      "sharpe": 1.6930263025416261,
      "sortino": 3.0834996353747743,
      "pf": 1.961585556075087,
      "trades": 280,
      "fees": 2752.5278666753707,
      "underwater_days_engine": 215,
      "curve_terminal": 33752.5420207966,
      "wallet_terminal_engine": 33752.5420207966,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 23752.5420207966,
      "positive_full_months": 42,
      "complete_months": 61,
      "best_observed_month_delta": 3458.1469742903028,
      "worst_observed_month_delta": -1125.4703279708701,
      "observed_net_ex_best_month": 20294.3950465063,
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
      "net": 35025.678744685174,
      "return_pct": 350.2567874468518,
      "cagr_pct": 33.455125809981176,
      "dd_engine_pct": -14.996090444461485,
      "dd_curve_pct": -14.996090444461474,
      "calmar": 2.2309231818708577,
      "sharpe": 1.6788752302910435,
      "sortino": 2.9274221318499825,
      "pf": 1.8878648354227012,
      "trades": 280,
      "fees": 4913.476656168994,
      "underwater_days_engine": 220,
      "curve_terminal": 45025.6787446852,
      "wallet_terminal_engine": 45025.6787446852,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 35025.6787446852,
      "positive_full_months": 43,
      "complete_months": 61,
      "best_observed_month_delta": 4252.106049563954,
      "worst_observed_month_delta": -2399.7536924227825,
      "observed_net_ex_best_month": 30773.57269512125,
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
      "net": 22494.176256066905,
      "return_pct": 224.94176256066908,
      "cagr_pct": 25.3618920431953,
      "dd_engine_pct": -15.664935932848522,
      "dd_curve_pct": -15.664935932848511,
      "calmar": 1.6190230302833724,
      "sharpe": 1.3527918187943047,
      "sortino": 2.2781882782367004,
      "pf": 1.6372917554992736,
      "trades": 280,
      "fees": 8581.174631667569,
      "underwater_days_engine": 228,
      "curve_terminal": 32494.17625606689,
      "wallet_terminal_engine": 32494.17625606689,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 22494.17625606689,
      "positive_full_months": 42,
      "complete_months": 61,
      "best_observed_month_delta": 4048.383767551808,
      "worst_observed_month_delta": -1901.993107814993,
      "observed_net_ex_best_month": 18445.792488515082,
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
      "net": 27028.235809079888,
      "return_pct": 270.2823580907989,
      "cagr_pct": 28.542282602163027,
      "dd_engine_pct": -15.838151943255985,
      "dd_curve_pct": -15.838151943255962,
      "calmar": 1.8021220344660582,
      "sharpe": 1.663869788187925,
      "sortino": 3.0564702435917237,
      "pf": 1.9430517631501134,
      "trades": 280,
      "fees": 3122.258136863264,
      "underwater_days_engine": 289,
      "curve_terminal": 37028.23580907987,
      "wallet_terminal_engine": 37028.23580907987,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 27028.235809079873,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 4382.949873170699,
      "worst_observed_month_delta": -1419.6480327763202,
      "observed_net_ex_best_month": 22645.285935909174,
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
      "net": 43283.88820390469,
      "return_pct": 432.8388820390469,
      "cagr_pct": 37.836060362626654,
      "dd_engine_pct": -16.834974508152843,
      "dd_curve_pct": -16.834974508152843,
      "calmar": 2.2474676361584867,
      "sharpe": 1.6499855246890753,
      "sortino": 2.8558823634760913,
      "pf": 1.9000460281705105,
      "trades": 280,
      "fees": 5908.334825319312,
      "underwater_days_engine": 229,
      "curve_terminal": 53283.88820390463,
      "wallet_terminal_engine": 53283.88820390463,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 0,
      "new_entry_records_vs_L5": 0,
      "common_entries_changed_exit": 0,
      "observed_curve_net": 43283.88820390463,
      "positive_full_months": 41,
      "complete_months": 61,
      "best_observed_month_delta": 5233.4210581455045,
      "worst_observed_month_delta": -3266.7869884692045,
      "observed_net_ex_best_month": 38050.467145759125,
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
      "net": 28957.541169801505,
      "return_pct": 289.57541169801505,
      "cagr_pct": 29.800655190665836,
      "dd_engine_pct": -17.458336985871725,
      "dd_curve_pct": -17.458336985871735,
      "calmar": 1.7069584127504362,
      "sharpe": 1.355781205932279,
      "sortino": 2.2602208627447395,
      "pf": 1.660473354699775,
      "trades": 280,
      "fees": 10615.734592703238,
      "underwater_days_engine": 283,
      "curve_terminal": 38957.541169801436,
      "wallet_terminal_engine": 38957.541169801436,
      "terminal_gap": 0,
      "curve_points": 1904,
      "median_curve_step_seconds": 86400,
      "removed_entry_records_vs_L5": 1,
      "new_entry_records_vs_L5": 1,
      "common_entries_changed_exit": 4,
      "observed_curve_net": 28957.541169801436,
      "positive_full_months": 40,
      "complete_months": 61,
      "best_observed_month_delta": 4450.120814242593,
      "worst_observed_month_delta": -2651.93485545578,
      "observed_net_ex_best_month": 24507.420355558843,
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
      "return_pct": 3.981733218081418,
      "equity_delta": 398.1733218081408,
      "partial": true
    },
    {
      "case": "L1",
      "year": 2021,
      "return_pct": 20.38213887484901,
      "equity_delta": 2119.370126898435,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2022,
      "return_pct": 9.677460573606766,
      "equity_delta": 1211.3803320326751,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2023,
      "return_pct": 19.689410576361908,
      "equity_delta": 2703.144170905538,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2024,
      "return_pct": 12.566842498254239,
      "equity_delta": 2064.992098689312,
      "partial": false
    },
    {
      "case": "L1",
      "year": 2025,
      "return_pct": 20.601698399236025,
      "equity_delta": 3810.7085242954054,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2020,
      "return_pct": 3.986501604552717,
      "equity_delta": 398.65016045527227,
      "partial": true
    },
    {
      "case": "L3",
      "year": 2021,
      "return_pct": 18.719907379832136,
      "equity_delta": 1946.617678789993,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2022,
      "return_pct": 11.158646312737153,
      "equity_delta": 1377.564774541468,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2023,
      "return_pct": 23.93222711828935,
      "equity_delta": 3284.1794681941246,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2024,
      "return_pct": 16.14683221514688,
      "equity_delta": 2746.0937056872062,
      "partial": false
    },
    {
      "case": "L3",
      "year": 2025,
      "return_pct": 17.650456701508755,
      "equity_delta": 3486.5133842555733,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2020,
      "return_pct": 3.9838234606026868,
      "equity_delta": 398.3823460602689,
      "partial": true
    },
    {
      "case": "L5",
      "year": 2021,
      "return_pct": 18.711231761296542,
      "equity_delta": 1945.6654201970814,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2022,
      "return_pct": 11.156549325981091,
      "equity_delta": 1377.1697778651687,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2023,
      "return_pct": 23.934621951238167,
      "equity_delta": 3284.121546292692,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2024,
      "return_pct": 16.14791972366636,
      "equity_delta": 2746.0085050575035,
      "partial": false
    },
    {
      "case": "L5",
      "year": 2025,
      "return_pct": 17.660034423036652,
      "equity_delta": 3488.0947843741014,
      "partial": true
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2020,
      "return_pct": 3.490360271546855,
      "equity_delta": 349.03602715468514,
      "partial": true
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2021,
      "return_pct": 16.452441723218424,
      "equity_delta": 1702.6691212825044,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2022,
      "return_pct": 8.7231047467365,
      "equity_delta": 1051.2828638660121,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2023,
      "return_pct": 19.3349992937176,
      "equity_delta": 2533.462639634725,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2024,
      "return_pct": 12.428709963270768,
      "equity_delta": 1943.409100079325,
      "partial": false
    },
    {
      "case": "R1A8_L3_F95",
      "year": 2025,
      "return_pct": 7.997092917585791,
      "equity_delta": 1405.8777191500885,
      "partial": true
    },
    {
      "case": "R2A6_L1",
      "year": 2020,
      "return_pct": 5.8362426279706225,
      "equity_delta": 583.6242627970623,
      "partial": true
    },
    {
      "case": "R2A6_L1",
      "year": 2021,
      "return_pct": 42.20348308526194,
      "equity_delta": 4466.658075557238,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2022,
      "return_pct": 13.532402433560065,
      "equity_delta": 2036.6647734131184,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2023,
      "return_pct": 23.129964936917922,
      "equity_delta": 3952.204875741514,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2024,
      "return_pct": 25.344819802431196,
      "equity_delta": 5332.335159193761,
      "partial": false
    },
    {
      "case": "R2A6_L1",
      "year": 2025,
      "return_pct": 27.988769965962202,
      "equity_delta": 7381.054874093908,
      "partial": true
    },
    {
      "case": "R2A6_L3",
      "year": 2020,
      "return_pct": 7.8098610315960215,
      "equity_delta": 780.986103159601,
      "partial": true
    },
    {
      "case": "R2A6_L3",
      "year": 2021,
      "return_pct": 47.51522297256865,
      "equity_delta": 5122.609585557924,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2022,
      "return_pct": 14.226639376459516,
      "equity_delta": 2262.5472065240047,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2023,
      "return_pct": 37.46095564582195,
      "equity_delta": 6805.210732543066,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2024,
      "return_pct": 33.446194639711855,
      "equity_delta": 8351.967538519584,
      "partial": false
    },
    {
      "case": "R2A6_L3",
      "year": 2025,
      "return_pct": 35.117620839708486,
      "equity_delta": 11702.357578381023,
      "partial": true
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2020,
      "return_pct": 6.788781664638988,
      "equity_delta": 678.8781664638991,
      "partial": true
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2021,
      "return_pct": 41.36323111866405,
      "equity_delta": 4417.1290568750155,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2022,
      "return_pct": 11.08055604270608,
      "equity_delta": 1672.7215405930256,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2023,
      "return_pct": 32.11986204352926,
      "equity_delta": 5386.092545428546,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2024,
      "return_pct": 26.819774563480237,
      "equity_delta": 5941.873130112363,
      "partial": false
    },
    {
      "case": "R2A6_L3_F95",
      "year": 2025,
      "return_pct": 15.651242625951213,
      "equity_delta": 4397.481816594041,
      "partial": true
    },
    {
      "case": "R3A9_L1",
      "year": 2020,
      "return_pct": 5.844907335558447,
      "equity_delta": 584.4907335558455,
      "partial": true
    },
    {
      "case": "R3A9_L1",
      "year": 2021,
      "return_pct": 54.76625340180825,
      "equity_delta": 5796.729016430107,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2022,
      "return_pct": 14.850352931847333,
      "equity_delta": 2432.6689474143914,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2023,
      "return_pct": 21.761463627196132,
      "equity_delta": 4094.1775457459407,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2024,
      "return_pct": 28.247822567538925,
      "equity_delta": 6471.029906018241,
      "partial": false
    },
    {
      "case": "R3A9_L1",
      "year": 2025,
      "return_pct": 26.03599382730797,
      "equity_delta": 7649.139659915349,
      "partial": true
    },
    {
      "case": "R3A9_L3",
      "year": 2020,
      "return_pct": 9.986769295860022,
      "equity_delta": 998.6769295860031,
      "partial": true
    },
    {
      "case": "R3A9_L3",
      "year": 2021,
      "return_pct": 60.328368906987606,
      "equity_delta": 6635.322392968381,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2022,
      "return_pct": 12.718765890508399,
      "equity_delta": 2242.8270909695275,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2023,
      "return_pct": 35.60122205962928,
      "equity_delta": 7076.393109885692,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2024,
      "return_pct": 35.73872879518456,
      "equity_delta": 9632.738027042094,
      "partial": false
    },
    {
      "case": "R3A9_L3",
      "year": 2025,
      "return_pct": 45.64027231056242,
      "equity_delta": 16697.93065345293,
      "partial": true
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2020,
      "return_pct": 8.886180238033559,
      "equity_delta": 888.6180238033558,
      "partial": true
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2021,
      "return_pct": 56.037824871736966,
      "equity_delta": 6101.744699131312,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2022,
      "return_pct": 9.186009863511458,
      "equity_delta": 1560.7363955751534,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2023,
      "return_pct": 30.56484078155752,
      "equity_delta": 5670.11390880145,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2024,
      "return_pct": 30.21704486477681,
      "equity_delta": 7318.934807255813,
      "partial": false
    },
    {
      "case": "R3A9_L3_F95",
      "year": 2025,
      "return_pct": 23.517306812066074,
      "equity_delta": 7417.393335234352,
      "partial": true
    }
  ],
  "fills": [
    {
      "case": "L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9038.228165429167,
          "fees": 1057.5438644786084
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 1603.1607636798335,
          "fees": 203.45179029181722
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 1666.379645520496,
          "fees": 335.9019733563946
        }
      },
      "entry_notional_sum": 1772095.7559422115,
      "entry_notional_turnover_initial_equity": 177.20957559422115,
      "time_weighted_entry_notional_over_initial_equity": 0.37701805381872466
    },
    {
      "case": "L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9189.391973780348,
          "fees": 1268.5468227959254
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2035.4760959837363,
          "fees": 280.7890895879873
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2014.7511021595576,
          "fees": 463.3009068658616
        }
      },
      "entry_notional_sum": 2234039.0175696407,
      "entry_notional_turnover_initial_equity": 223.40390175696407,
      "time_weighted_entry_notional_over_initial_equity": 0.4927059397461788
    },
    {
      "case": "L5",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 9189.421279511538,
          "fees": 1268.3982916641712
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2035.4301531490387,
          "fees": 280.7511694974209
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 2014.5909471862112,
          "fees": 463.2747627581751
        }
      },
      "entry_notional_sum": 2233802.5424969783,
      "entry_notional_turnover_initial_equity": 223.38025424969783,
      "time_weighted_entry_notional_over_initial_equity": 0.49265415546712815
    },
    {
      "case": "R1A8_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 7079.372079664216,
          "fees": 2307.803294212386
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 1418.0331979804362,
          "fees": 487.7115946548135
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 488.33219352269356,
          "fees": 827.2878853907675
        }
      },
      "entry_notional_sum": 1905179.5244738404,
      "entry_notional_turnover_initial_equity": 190.51795244738403,
      "time_weighted_entry_notional_over_initial_equity": 0.4095910476219704
    },
    {
      "case": "R2A6_L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 18149.379451518875,
          "fees": 1966.25378924002
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2162.607346388951,
          "fees": 272.29595061258067
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 3440.555222888827,
          "fees": 513.9781268227703
        }
      },
      "entry_notional_sum": 3054780.870846244,
      "entry_notional_turnover_initial_equity": 305.4780870846244,
      "time_weighted_entry_notional_over_initial_equity": 0.6081885615565614
    },
    {
      "case": "R2A6_L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 21831.154933503218,
          "fees": 2821.0849742095797
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 5973.780940936215,
          "fees": 788.2204708790168
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 7220.742870245762,
          "fees": 1304.1712110803967
        }
      },
      "entry_notional_sum": 5451915.075650619,
      "entry_notional_turnover_initial_equity": 545.1915075650619,
      "time_weighted_entry_notional_over_initial_equity": 1.3529648472585263
    },
    {
      "case": "R2A6_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 16664.490619862416,
          "fees": 5002.6208179390915
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 4017.0894194441335,
          "fees": 1326.6467712419917
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 1812.5962167603602,
          "fees": 2251.9070424864844
        }
      },
      "entry_notional_sum": 4511596.56247089,
      "entry_notional_turnover_initial_equity": 451.15965624708895,
      "time_weighted_entry_notional_over_initial_equity": 1.0756979453560753
    },
    {
      "case": "R3A9_L1",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 21226.338968896427,
          "fees": 2272.997666004865
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 2367.6239292800146,
          "fees": 293.82492576530035
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 3434.2729109034503,
          "fees": 555.4355450930985
        }
      },
      "entry_notional_sum": 3465388.8643988436,
      "entry_notional_turnover_initial_equity": 346.5388864398844,
      "time_weighted_entry_notional_over_initial_equity": 0.6802035658113084
    },
    {
      "case": "R3A9_L3",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 223,
          "net": 26371.292313386093,
          "fees": 3325.522742374303
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 6980.541931337071,
          "fees": 939.1713362993862
        },
        "PAXG-USDT": {
          "trades": 38,
          "net": 9932.053959181514,
          "fees": 1643.6407466456221
        }
      },
      "entry_notional_sum": 6554362.252202254,
      "entry_notional_turnover_initial_equity": 655.4362252202254,
      "time_weighted_entry_notional_over_initial_equity": 1.6631422949546812
    },
    {
      "case": "R3A9_L3_F95",
      "by_symbol": {
        "BTC-USDT": {
          "trades": 222,
          "net": 20800.512220324952,
          "fees": 5989.329990703387
        },
        "SPY-USDT": {
          "trades": 19,
          "net": 5078.913012924369,
          "fees": 1700.7273678869208
        },
        "PAXG-USDT": {
          "trades": 39,
          "net": 3078.115936552183,
          "fees": 2925.677234112932
        }
      },
      "entry_notional_sum": 5579998.7486706115,
      "entry_notional_turnover_initial_equity": 557.9998748670612,
      "time_weighted_entry_notional_over_initial_equity": 1.3856472700274718
    }
  ],
  "engine_metrics": {
    "L1": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 22307.768574629506,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.697556607491815,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 1596.8976281268197,
      "net_profit": 12307.7685746295,
      "net_profit_percentage": 123.07768574629499,
      "average_win": 175.2215539473761,
      "average_loss": 103.21985916350124,
      "expectancy": 43.9563163379625,
      "expectancy_percentage": 0.439563163379625,
      "expected_net_profit_every_100_trades": 43.9563163379625,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 25932.78998421166,
      "gross_loss": -13625.021409582163,
      "max_drawdown": -8.182245647817844,
      "max_underwater_period": 219,
      "annual_return": 16.63656691119437,
      "annualization": 365,
      "sharpe_ratio": 1.657760787872279,
      "calmar_ratio": 2.0332519490699044,
      "sortino_ratio": 2.986015288408941,
      "omega_ratio": 1.440473860887152,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -80.16525000000183,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -212.84749197532315,
      "largest_winning_trade": 2007.7867257670353,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L3": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23239.619171923638,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6098374289841717,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2012.6368192497744,
      "net_profit": 13239.619171923641,
      "net_profit_percentage": 132.3961917192364,
      "average_win": 200.5876997636796,
      "average_loss": 124.60121509924953,
      "expectancy": 47.284354185441586,
      "expectancy_percentage": 0.4728435418544159,
      "expected_net_profit_every_100_trades": 47.28435418544159,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29686.979565024583,
      "gross_loss": -16447.36039310094,
      "max_drawdown": -9.057235280291742,
      "max_underwater_period": 219,
      "annual_return": 17.55567750901328,
      "annualization": 365,
      "sharpe_ratio": 1.5693937539620852,
      "calmar_ratio": 1.9383042358647653,
      "sortino_ratio": 2.7272080768780214,
      "omega_ratio": 1.405418024526862,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -118.76974999999948,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -223.99268285843212,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "L5": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 23239.442379846816,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6099156072256704,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2012.4242239197674,
      "net_profit": 13239.442379846789,
      "net_profit_percentage": 132.3944237984679,
      "average_win": 200.57292153053464,
      "average_loss": 124.58598489903284,
      "expectancy": 47.28372278516712,
      "expectancy_percentage": 0.4728372278516712,
      "expected_net_profit_every_100_trades": 47.28372278516712,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 29684.792386519126,
      "gross_loss": -16445.350006672335,
      "max_drawdown": -9.057883731399553,
      "max_underwater_period": 219,
      "annual_return": 17.555505981887354,
      "annualization": 365,
      "sharpe_ratio": 1.569754072854379,
      "calmar_ratio": 1.9381465364840598,
      "sortino_ratio": 2.7281116510374783,
      "omega_ratio": 1.4054903057639654,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -118.76974999999948,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -223.9869819935303,
      "largest_winning_trade": 1998.0559338812498,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R1A8_L3_F95": {
      "total": 280,
      "total_winning_trades": 145,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 18985.73747116734,
      "win_rate": 0.5178571428571429,
      "win_rate_longs": 0.47191011235955055,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.481820962668813,
      "longs_count": 89,
      "longs_percentage": 31.785714285714285,
      "shorts_percentage": 68.21428571428572,
      "shorts_count": 191,
      "fee": 3622.8027742579666,
      "net_profit": 8985.737471167342,
      "net_profit_percentage": 89.85737471167342,
      "average_win": 166.72402521429075,
      "average_loss": 112.51293470299863,
      "expectancy": 32.09191953988338,
      "expectancy_percentage": 0.3209191953988338,
      "expected_net_profit_every_100_trades": 32.09191953988338,
      "average_holding_period": 286689,
      "average_winning_holding_period": 396549.5172413793,
      "average_losing_holding_period": 168690.66666666666,
      "gross_profit": 24174.98365607216,
      "gross_loss": -15189.246184904816,
      "max_drawdown": -9.299572126581134,
      "max_underwater_period": 220,
      "annual_return": 13.084494757736564,
      "annualization": 365,
      "sharpe_ratio": 1.2578757481769922,
      "calmar_ratio": 1.4069996532783393,
      "sortino_ratio": 2.1073802362844702,
      "omega_ratio": 1.313909040228234,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -86.19050000000061,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -184.3100502028544,
      "largest_winning_trade": 1776.8570482567457,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R2A6_L1": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 33752.5420207966,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.7495222527156182,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 2752.52786667537,
      "net_profit": 23752.54202079666,
      "net_profit_percentage": 237.5254202079666,
      "average_win": 327.3917289712159,
      "average_loss": 187.13207474957042,
      "expectancy": 84.83050721713093,
      "expectancy_percentage": 0.8483050721713092,
      "expected_net_profit_every_100_trades": 84.83050721713093,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 48453.97588773996,
      "gross_loss": -24701.433866943295,
      "max_drawdown": -14.05970492502373,
      "max_underwater_period": 215,
      "annual_return": 26.278804344483575,
      "annualization": 365,
      "sharpe_ratio": 1.6930263025416261,
      "calmar_ratio": 1.8690864768941244,
      "sortino_ratio": 3.0834996353747743,
      "omega_ratio": 1.4723612705582767,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -121.29149999999936,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -631.615605378079,
      "largest_winning_trade": 3185.2798692118818,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R2A6_L3": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 45025.6787446852,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6837713397013285,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 4913.476656168994,
      "net_profit": 35025.678744685174,
      "net_profit_percentage": 350.2567874468518,
      "average_win": 503.20956311534707,
      "average_loss": 298.8586105786832,
      "expectancy": 125.0917098024471,
      "expectancy_percentage": 1.250917098024471,
      "expected_net_profit_every_100_trades": 125.0917098024471,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 74475.01534107137,
      "gross_loss": -39449.33659638619,
      "max_drawdown": -14.996090444461485,
      "max_underwater_period": 220,
      "annual_return": 33.455125809981176,
      "annualization": 365,
      "sharpe_ratio": 1.6788752302910435,
      "calmar_ratio": 2.2309231818708577,
      "sortino_ratio": 2.9274221318499825,
      "omega_ratio": 1.4370603175354235,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -454.4704999999958,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -877.7621689372322,
      "largest_winning_trade": 4320.471597288677,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R2A6_L3_F95": {
      "total": 280,
      "total_winning_trades": 145,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 32494.17625606689,
      "win_rate": 0.5178571428571429,
      "win_rate_longs": 0.47191011235955055,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.52437508270622,
      "longs_count": 89,
      "longs_percentage": 31.785714285714285,
      "shorts_percentage": 68.21428571428572,
      "shorts_count": 191,
      "fee": 8581.17463166757,
      "net_profit": 22494.176256066905,
      "net_profit_percentage": 224.94176256066908,
      "average_win": 398.5564724692993,
      "average_loss": 261.4556463109741,
      "expectancy": 80.33634377166752,
      "expectancy_percentage": 0.8033634377166752,
      "expected_net_profit_every_100_trades": 80.33634377166752,
      "average_holding_period": 286689,
      "average_winning_holding_period": 396549.5172413793,
      "average_losing_holding_period": 168690.66666666666,
      "gross_profit": 57790.6885080484,
      "gross_loss": -35296.512251981505,
      "max_drawdown": -15.664935932848522,
      "max_underwater_period": 228,
      "annual_return": 25.3618920431953,
      "annualization": 365,
      "sharpe_ratio": 1.3527918187943047,
      "calmar_ratio": 1.6190230302833724,
      "sortino_ratio": 2.2781882782367004,
      "omega_ratio": 1.3415184597688234,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -296.3950000000041,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -641.109285207141,
      "largest_winning_trade": 4001.9593409920535,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R3A9_L1": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 37028.23580907987,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.7329921130798307,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 3122.2581368632636,
      "net_profit": 27028.235809079888,
      "net_profit_percentage": 270.2823580907989,
      "average_win": 376.274530858431,
      "average_loss": 217.124202711878,
      "expectancy": 96.52941360385675,
      "expectancy_percentage": 0.9652941360385676,
      "expected_net_profit_every_100_trades": 96.52941360385677,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 55688.63056704779,
      "gross_loss": -28660.394757967897,
      "max_drawdown": -15.838151943255985,
      "max_underwater_period": 289,
      "annual_return": 28.542282602163027,
      "annualization": 365,
      "sharpe_ratio": 1.663869788187925,
      "calmar_ratio": 1.8021220344660582,
      "sortino_ratio": 3.0564702435917237,
      "omega_ratio": 1.4766163744897978,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -133.06425000000309,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -945.9144329426985,
      "largest_winning_trade": 4011.0931686371846,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R3A9_L3": {
      "total": 280,
      "total_winning_trades": 148,
      "total_losing_trades": 132,
      "starting_balance": 10000,
      "finishing_balance": 53283.88820390463,
      "win_rate": 0.5285714285714286,
      "win_rate_longs": 0.48863636363636365,
      "win_rate_shorts": 0.546875,
      "ratio_avg_win_loss": 1.6946356467466714,
      "longs_count": 88,
      "longs_percentage": 31.428571428571427,
      "shorts_percentage": 68.57142857142857,
      "shorts_count": 192,
      "fee": 5908.334825319311,
      "net_profit": 43283.88820390469,
      "net_profit_percentage": 432.8388820390469,
      "average_win": 617.3962016380972,
      "average_loss": 364.3238608979826,
      "expectancy": 154.5853150139453,
      "expectancy_percentage": 1.545853150139453,
      "expected_net_profit_every_100_trades": 154.5853150139453,
      "average_holding_period": 287993.14285714284,
      "average_winning_holding_period": 406858.7837837838,
      "average_losing_holding_period": 154719.54545454544,
      "gross_profit": 91374.63784243839,
      "gross_loss": -48090.74963853371,
      "max_drawdown": -16.834974508152843,
      "max_underwater_period": 229,
      "annual_return": 37.836060362626654,
      "annualization": 365,
      "sharpe_ratio": 1.6499855246890753,
      "calmar_ratio": 2.2474676361584867,
      "sortino_ratio": 2.8558823634760913,
      "omega_ratio": 1.4336724044863374,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -537.8257500000182,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -1268.4843317342177,
      "largest_winning_trade": 5164.929878416891,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    },
    "R3A9_L3_F95": {
      "total": 280,
      "total_winning_trades": 145,
      "total_losing_trades": 135,
      "starting_balance": 10000,
      "finishing_balance": 38957.541169801436,
      "win_rate": 0.5178571428571429,
      "win_rate_longs": 0.47191011235955055,
      "win_rate_shorts": 0.5392670157068062,
      "ratio_avg_win_loss": 1.5459579509273766,
      "longs_count": 89,
      "longs_percentage": 31.785714285714285,
      "shorts_percentage": 68.21428571428572,
      "shorts_count": 191,
      "fee": 10615.734592703238,
      "net_profit": 28957.5411698015,
      "net_profit_percentage": 289.57541169801505,
      "average_win": 502.07695673401184,
      "average_loss": 324.7675374565201,
      "expectancy": 103.41978989214829,
      "expectancy_percentage": 1.0341978989214828,
      "expected_net_profit_every_100_trades": 103.41978989214829,
      "average_holding_period": 286689,
      "average_winning_holding_period": 396549.5172413793,
      "average_losing_holding_period": 168690.66666666666,
      "gross_profit": 72801.15872643172,
      "gross_loss": -43843.61755663021,
      "max_drawdown": -17.458336985871725,
      "max_underwater_period": 283,
      "annual_return": 29.800655190665836,
      "annualization": 365,
      "sharpe_ratio": 1.355781205932279,
      "calmar_ratio": 1.7069584127504362,
      "sortino_ratio": 2.2602208627447395,
      "omega_ratio": 1.3471280002197328,
      "serenity_index": null,
      "total_open_trades": 1,
      "open_pl": -394.38850000000093,
      "winning_streak": 7,
      "losing_streak": 6,
      "largest_losing_trade": -969.2976375761822,
      "largest_winning_trade": 4421.181512087111,
      "current_streak": -4,
      "avg_trades_per_day": 0.14713604720030973,
      "avg_trades_per_week": 1.029952330402168,
      "avg_trades_per_month": 4.4788212767774285
    }
  }
}
```

## Todos los meses

```csv
case,month,return_pct,equity_delta,partial
L1,2020-10,-1.908913302195192,-190.89133021951966,True
L1,2020-11,0.25973959100202837,25.478138739832502,False
L1,2020-12,5.730657772012937,563.586513287828,False
L1,2021-01,1.012755871364468,105.30811083126537,False
L1,2021-02,8.528584772264525,895.7983180217161,False
L1,2021-03,0.3670642609819863,41.84268197403435,False
L1,2021-04,-3.797704304189198,-434.4999990717406,False
L1,2021-05,-1.0372478185785017,-114.16595109130867,False
L1,2021-06,1.0024157936802336,109.18770410004618,False
L1,2021-07,6.257223066189788,688.397417702321,False
L1,2021-08,-3.6422152462477597,-425.77647760359105,False
L1,2021-09,-0.9193216720993047,-103.55483051221017,False
L1,2021-10,6.967815408803912,777.6576917477087,False
L1,2021-11,3.2950236308076253,393.372046334287,False
L1,2021-12,1.5067088176526466,185.80341446590683,False
L1,2022-01,-0.4698130633856601,-58.80905433699991,False
L1,2022-02,-1.5936771360446134,-198.55200148359472,False
L1,2022-03,4.729834225132823,579.8863028824289,False
L1,2022-04,0.2719119496474631,34.913681126736265,False
L1,2022-05,0.23230768586275374,29.909573615002955,False
L1,2022-06,0.3022535275049698,39.00549114112255,False
L1,2022-07,-0.9723124864431276,-125.85513105756763,False
L1,2022-08,-0.933553809720522,-119.66332232213608,False
L1,2022-09,2.4583703838850335,312.1731882811491,False
L1,2022-10,0.450953661834097,58.671561465000195,False
L1,2022-11,0.9774723133416874,127.74804360780217,False
L1,2022-12,4.030864109707211,531.9519991137313,False
L1,2023-01,13.752685181114366,1888.0956663202141,False
L1,2023-02,0.9157902155533693,143.01913605723712,False
L1,2023-03,0.09354454947283486,14.742657089320346,False
L1,2023-04,0.3728219738496019,58.81185079019269,False
L1,2023-05,-0.7875651227718383,-124.69985686629843,False
L1,2023-06,2.8253848465974674,443.8366890052803,False
L1,2023-07,-2.1586943778041046,-348.68807271260084,False
L1,2023-08,0.7244550729631483,114.49318291860618,False
L1,2023-09,-0.23572746172529913,-37.52435857794808,False
L1,2023-10,-1.3482156225816722,-214.1102669410211,False
L1,2023-11,0.9301539334159781,145.72629038772357,False
L1,2023-12,3.9173836533114015,619.4412534348321,False
L1,2024-01,-0.38364981838266976,-63.04159885300214,False
L1,2024-02,-0.9019633261803994,-147.64261455498672,False
L1,2024-03,2.400002007692259,389.31353539315023,False
L1,2024-04,3.263648646165196,542.1147966894241,False
L1,2024-05,0.7402195560709535,126.9684693606032,False
L1,2024-06,-2.1856427015585767,-377.67426221085407,False
L1,2024-07,-2.916724950193439,-492.9879509031525,False
L1,2024-08,0.6673604970076852,109.50797361875084,False
L1,2024-09,2.6458022209279397,437.05018151707554,False
L1,2024-10,1.2464455092135784,211.34326806295576,False
L1,2024-11,6.898603903350309,1184.2846945461897,False
L1,2024-12,0.7942520187895541,145.75560602315818,False
L1,2025-01,4.1831615603251215,773.7619058158307,False
L1,2025-02,1.4405057446459146,277.59729731882544,False
L1,2025-03,2.878412892036386,562.684219981169,False
L1,2025-04,0.8773742887761227,176.4496510652134,False
L1,2025-05,3.6199679497326276,734.4029208924294,False
L1,2025-06,1.285825047061051,270.30557621401385,False
L1,2025-07,1.8185268014594191,387.2054842260477,False
L1,2025-08,2.350845841466298,509.6508509098712,False
L1,2025-09,0.9629279426552229,213.6652170343441,False
L1,2025-10,1.9869855122897073,445.1400560129223,False
L1,2025-11,0.346280970918067,79.11801039478087,False
L1,2025-12,-2.7010579301625204,-619.2726655700426,True
L3,2020-10,-1.908913302195192,-190.89133021951966,True
L3,2020-11,0.2646114909586661,25.95602870086259,False
L3,2020-12,5.730368627477911,563.5854619739293,False
L3,2021-01,1.0127203721846056,105.30924860713822,False
L3,2021-02,8.342740337481235,876.318058652505,False
L3,2021-03,0.3676771686168312,41.84268197403435,False
L3,2021-04,-4.690506018306428,-535.7552330393519,False
L3,2021-05,-1.0580134051336176,-115.17920014991614,False
L3,2021-06,0.9997908953306878,107.68933411272337,False
L3,2021-07,6.25691901562504,680.6824017278559,False
L3,2021-08,-3.6435809464243407,-421.1818328244444,False
L3,2021-09,-0.9193184481411376,-102.39714189346341,False
L3,2021-10,7.318848345000628,807.706528164088,False
L3,2021-11,2.700754166862507,319.8688163038478,False
L3,2021-12,1.49392208735053,181.71401715497632,False
L3,2022-01,-0.47520839281430804,-58.66574888749892,False
L3,2022-02,-1.5843424737828848,-194.66185550223418,False
L3,2022-03,4.736140912480291,572.6913285756582,False
L3,2022-04,1.6150224369483324,204.53664130625475,False
L3,2022-05,0.2324126403444593,29.909573615001136,False
L3,2022-06,0.30238976624035185,39.00549114112255,False
L3,2022-07,-0.9727494284591409,-125.85513105756581,False
L3,2022-08,-0.9339774552027613,-119.66332232213608,False
L3,2022-09,2.4594965068433616,312.1731882811491,False
L3,2022-10,0.4493720522493305,58.43965805999869,False
L3,2022-11,0.9753502424344029,127.41173500039258,False
L3,2022-12,4.035022244222097,532.243216331326,False
L3,2023-01,14.814570011014139,2032.9786450637184,False
L3,2023-02,0.9160930083814911,144.33788535611166,False
L3,2023-03,0.09289740851561312,14.770826505086006,False
L3,2023-04,0.36826265661071833,58.60870708161201,False
L3,2023-05,-1.1340720241938995,-181.1513200114423,False
L3,2023-06,4.421537366457029,698.2658659262215,False
L3,2023-07,-1.5025808620644843,-247.78524911077147,False
L3,2023-08,0.7263362017779995,117.97775767288476,False
L3,2023-09,-0.6460981421103185,-105.70705569991878,False
L3,2023-10,-1.3503398465084748,-219.49947962095393,False
L3,2023-11,0.38107037872394667,61.10703291158279,False
L3,2023-12,5.655033660993669,910.2758521199939,False
L3,2024-01,-0.37439000069955375,-63.67255265270069,False
L3,2024-02,-0.7902970741410553,-133.9027165620646,False
L3,2024-03,2.384318899447191,400.7905788174139,False
L3,2024-04,3.4492912294928235,593.6308639936615,False
L3,2024-05,1.3780986344318569,245.35472749629116,False
L3,2024-06,-2.182257690303857,-393.8803383624436,False
L3,2024-07,-1.764761817761562,-311.5745693126519,False
L3,2024-08,1.1996546155435661,208.06519426022714,False
L3,2024-09,2.803809599490137,492.11970572022983,False
L3,2024-10,1.334334686944194,240.76659001291046,False
L3,2024-11,7.170494795300475,1311.1041477222207,False
L3,2024-12,0.8026820261556544,157.29207455411233,False
L3,2025-01,3.5692533156509,705.0383832703737,False
L3,2025-02,2.215448647575502,453.23967835410076,False
L3,2025-03,3.6714993786306938,767.7613280898549,False
L3,2025-04,0.5964896938327025,129.31386669411586,False
L3,2025-05,3.6436162625196333,794.6165603349073,False
L3,2025-06,1.3867454996423945,313.4471337249415,False
L3,2025-07,0.0010404813507891575,0.23844214533892227,False
L3,2025-08,2.3593202647433253,540.6797905492167,False
L3,2025-09,0.9336209468413514,219.00358249662168,False
L3,2025-10,1.5521168194147394,367.48607815159994,False
L3,2025-11,0.34625673235815224,83.25372853501904,False
L3,2025-12,-3.678693604884431,-887.565188090517,True
L5,2020-10,-1.908913302195192,-190.89133021951966,True
L5,2020-11,0.2646114909586661,25.95602870086259,False
L5,2020-12,5.72764557070895,563.317647578926,False
L5,2021-01,1.0034076265094338,104.33816149397899,False
L5,2021-02,8.343828785627316,876.3290169832944,False
L5,2021-03,0.3677168456276192,41.84268197403435,False
L5,2021-04,-4.690805626722138,-535.7318542449157,False
L5,2021-05,-1.058026347205654,-115.16786446256447,False
L5,2021-06,0.9999016641345948,107.68933411272337,False
L5,2021-07,6.257632456561457,680.6853482097522,False
L5,2021-08,-3.6439561628827555,-421.1818328244444,False
L5,2021-09,-0.9193232214755542,-102.38673102458961,False
L5,2021-10,7.319437024610997,807.6851347791362,False
L5,2021-11,2.700869302752862,319.8500080456997,False
L5,2021-12,1.4940719511860712,181.71401715497632,False
L5,2022-01,-0.47525536192319917,-58.66574888749892,False
L5,2022-02,-1.5844003712222499,-194.64963828928012,False
L5,2022-03,4.736616776403535,572.691658257585,False
L5,2022-04,1.6151548745109823,204.53391061906405,False
L5,2022-05,0.23243449921088732,29.909573615002955,False
L5,2022-06,0.3024181406413362,39.00549114112255,False
L5,2022-07,-0.972840430093791,-125.85513105756763,False
L5,2022-08,-0.9340656880471809,-119.66332232213608,False
L5,2022-09,2.4597310462149746,312.1731882811491,False
L5,2022-10,0.449413875943927,58.43965805999869,False
L5,2022-11,0.9730826989446051,127.10374496640361,False
L5,2022-12,4.034752617552262,532.1463934813255,False
L5,2023-01,14.81622174956403,2032.966018077277,False
L5,2023-02,0.9161876576227801,144.33788535611166,False
L5,2023-03,0.09299038023071748,14.784095545142918,False
L5,2023-04,0.36830001738401563,58.60870708161201,False
L5,2023-05,-1.134090987604186,-181.13604005919115,False
L5,2023-06,4.4217760719105215,698.2328524636996,False
L5,2023-07,-1.5027390042826383,-247.78680065797744,False
L5,2023-08,0.7264092642907283,117.97775767288658,False
L5,2023-09,-0.6460731461118252,-105.69241116683224,False
L5,2023-10,-1.3503826148268727,-219.48456805152455,False
L5,2023-11,0.38106198356844256,61.09957386474525,False
L5,2023-12,5.6552185707276825,910.2144761667423,False
L5,2024-01,-0.3744268333266465,-63.67255265270069,False
L5,2024-02,-0.7904412049896226,-133.9139131264128,False
L5,2024-03,2.384288751430197,400.745355197414,False
L5,2024-04,3.4493036848284975,593.5733549220349,False
L5,2024-05,1.3780801195372616,245.3268059301081,False
L5,2024-06,-2.182477137657246,-393.8803383624436,False
L5,2024-07,-1.7651317293754465,-311.60784407975007,False
L5,2024-08,1.2004059093476016,208.1733119324963,False
L5,2024-09,2.8039684337651583,492.0987949952323,False
L5,2024-10,1.3343038635014404,240.7375323555425,False
L5,2024-11,7.171370613964956,1311.1359233918702,False
L5,2024-12,0.8027540515346043,157.29207455411233,False
L5,2025-01,3.5776436029682834,706.6328237494599,False
L5,2025-02,2.215364079724713,453.2187496445622,False
L5,2025-03,3.6715152496749726,767.75786637485,False
L5,2025-04,0.5965010508384827,129.31520652604013,False
L5,2025-05,3.6436474725083823,794.6165603349145,False
L5,2025-06,1.3867569604456342,313.4471337249415,False
L5,2025-07,0.0010404898322713407,0.23844214533892227,False
L5,2025-08,2.3593394965214065,540.6797905492167,False
L5,2025-09,0.9336283817502844,219.00358249662168,False
L5,2025-10,1.5521290653958575,367.48607815159994,False
L5,2025-11,0.3462831329075877,83.25942939992456,False
L5,2025-12,-3.6787033566139105,-887.5608787233687,True
R1A8_L3_F95,2020-10,-1.9097903820102347,-190.9790382010233,True
R1A8_L3_F95,2020-11,0.09414522860311525,9.234725208212694,False
R1A8_L3_F95,2020-12,5.406055383645114,530.7803401474957,False
R1A8_L3_F95,2021-01,0.9293380641569149,96.17753107366116,False
R1A8_L3_F95,2021-02,7.978784512417669,833.4010816728733,False
R1A8_L3_F95,2021-03,0.2487822583255639,28.059192208984314,False
R1A8_L3_F95,2021-04,-4.74445958642955,-536.440570533874,False
R1A8_L3_F95,2021-05,-1.0977347817562544,-118.22859658860398,False
R1A8_L3_F95,2021-06,0.9434012791785129,100.4911482676489,False
R1A8_L3_F95,2021-07,6.006273549940344,645.8243119900017,False
R1A8_L3_F95,2021-08,-3.7366160369447066,-425.91145774221513,False
R1A8_L3_F95,2021-09,-0.9253189100442594,-101.52977228774216,False
R1A8_L3_F95,2021-10,6.943682727947498,754.8393402231632,False
R1A8_L3_F95,2021-11,2.336309687940852,271.6127814272568,False
R1A8_L3_F95,2021-12,1.2975526305228247,154.37413157135052,False
R1A8_L3_F95,2022-01,-0.5421827036979354,-65.34226081549969,False
R1A8_L3_F95,2022-02,-1.6379822738566419,-196.3344993793744,False
R1A8_L3_F95,2022-03,4.430480132827763,522.3548653958296,False
R1A8_L3_F95,2022-04,1.1779124360205007,145.0290935151097,False
R1A8_L3_F95,2022-05,0.18988414375964435,23.654650770000444,False
R1A8_L3_F95,2022-06,0.24750782915829994,30.891617982351818,False
R1A8_L3_F95,2022-07,-1.1357696869515044,-142.10703320337234,False
R1A8_L3_F95,2022-08,-1.0386237754848149,-128.47621953013004,False
R1A8_L3_F95,2022-09,2.2645735878951356,277.2149532694966,False
R1A8_L3_F95,2022-10,0.39734731157923253,49.74228206999942,False
R1A8_L3_F95,2022-11,0.6831678046520739,85.86280189462377,False
R1A8_L3_F95,2022-12,3.546591448102432,448.7926118969772,False
R1A8_L3_F95,2023-01,14.295471979726049,1873.133979805667,False
R1A8_L3_F95,2023-02,0.6045949800346229,90.54488176814993,False
R1A8_L3_F95,2023-03,-0.020153477649365037,-3.03645734093152,False
R1A8_L3_F95,2023-04,0.17646718486852286,26.58236453506106,False
R1A8_L3_F95,2023-05,-1.2879372041088244,-194.35246458660004,False
R1A8_L3_F95,2023-06,3.973666766298023,591.9118509503205,False
R1A8_L3_F95,2023-07,-1.7727519691593807,-274.5597860771195,False
R1A8_L3_F95,2023-08,0.5371561810174841,81.71871063778053,False
R1A8_L3_F95,2023-09,-0.8447955119394224,-129.21089141940502,False
R1A8_L3_F95,2023-10,-1.5588341787411641,-236.40842993883416,False
R1A8_L3_F95,2023-11,-0.00857834513392497,-1.2806878898045397,False
R1A8_L3_F95,2023-12,4.745566011107583,708.4195691904406,False
R1A8_L3_F95,2024-01,-0.4319749169526377,-67.5455447180484,False
R1A8_L3_F95,2024-02,-0.952912895472191,-148.3581044505263,False
R1A8_L3_F95,2024-03,2.1343878991543885,329.134289210524,False
R1A8_L3_F95,2024-04,3.176902634009271,500.3520398129749,False
R1A8_L3_F95,2024-05,0.9470027862632069,153.8882684207765,False
R1A8_L3_F95,2024-06,-2.3130524550393106,-379.4313112964646,False
R1A8_L3_F95,2024-07,-2.1937039255447988,-351.5298725165212,False
R1A8_L3_F95,2024-08,0.8719265060163073,136.6566961480421,False
R1A8_L3_F95,2024-09,2.4760364989770967,391.4518900552339,False
R1A8_L3_F95,2024-10,1.0032780345101688,162.54176665896193,False
R1A8_L3_F95,2024-11,6.736321058820782,1102.3053582333196,False
R1A8_L3_F95,2024-12,0.6523770278598517,113.9436245210527,False
R1A8_L3_F95,2025-01,-0.41874235700261053,-73.61431908334998,False
R1A8_L3_F95,2025-02,0.8041760818601418,140.78103860338888,False
R1A8_L3_F95,2025-03,3.1947368351460614,563.7760549941777,False
R1A8_L3_F95,2025-04,0.3558259578708922,64.79876252600661,False
R1A8_L3_F95,2025-05,3.4280998466032164,626.5058597559946,False
R1A8_L3_F95,2025-06,0.95682523373124,180.86013090676352,False
R1A8_L3_F95,2025-07,-0.636556538608557,-121.47387597959096,False
R1A8_L3_F95,2025-08,2.08739778718694,395.8017937272816,False
R1A8_L3_F95,2025-09,0.5897073106487349,114.15138492332335,False
R1A8_L3_F95,2025-10,1.1366574558820508,221.323649346843,False
R1A8_L3_F95,2025-11,0.22571284062036234,44.44911108689848,False
R1A8_L3_F95,2025-12,-3.807435376811741,-751.4818716576483,True
R2A6_L1,2020-10,-3.428315964862161,-342.83159648621586,True
R2A6_L1,2020-11,-0.06082630579699044,-5.874098784452144,False
R2A6_L1,2020-12,9.66015467594714,932.3299580677303,False
R2A6_L1,2021-01,1.1435921170053431,121.03349276281187,False
R2A6_L1,2021-02,17.994405627632993,1926.2395375853175,False
R2A6_L1,2021-03,1.277038466318392,161.30141707463372,False
R2A6_L1,2021-04,-5.578806995317464,-713.6520765006535,False
R2A6_L1,2021-05,-2.808960532537308,-339.2816078452852,False
R2A6_L1,2021-06,1.6341552277145288,191.8378131155805,False
R2A6_L1,2021-07,12.683503047404798,1513.2817921722308,False
R2A6_L1,2021-08,-5.902896550598735,-793.60811664207,False
R2A6_L1,2021-09,-1.0256997846591065,-129.7589874671321,False
R2A6_L1,2021-10,11.621192896880528,1455.0915994709903,False
R2A6_L1,2021-11,5.467207719368927,764.1029170327183,False
R2A6_L1,2021-12,2.1035673970080104,310.07029479809535,False
R2A6_L1,2022-01,-1.2737204437319627,-191.69852298299884,False
R2A6_L1,2022-02,-1.9802877681478925,-294.24271781579955,False
R2A6_L1,2022-03,6.469931310327004,942.3028648135678,False
R2A6_L1,2022-04,2.9494389633653695,457.3589989364573,False
R2A6_L1,2022-05,0.4640817667384223,74.08602698500181,False
R2A6_L1,2022-06,0.7249756630266502,116.2722419796628,False
R2A6_L1,2022-07,-3.0162217900276067,-487.25136346718136,False
R2A6_L1,2022-08,-1.6085698542899984,-252.01640635588774,False
R2A6_L1,2022-09,3.5419508075657857,545.9950273093273,False
R2A6_L1,2022-10,0.9022693822885008,144.01201450500048,False
R2A6_L1,2022-11,0.7989603788999711,128.67337199508802,False
R2A6_L1,2022-12,5.255544669522827,853.1732375108804,False
R2A6_L1,2023-01,15.557733991102785,2658.3417788491934,False
R2A6_L1,2023-02,1.4825142269871083,292.7267169630977,False
R2A6_L1,2023-03,0.646530724385519,129.55192746016837,False
R2A6_L1,2023-04,-0.014680665323740794,-2.960733093757881,False
R2A6_L1,2023-05,-0.5724345755536375,-115.42918135878062,False
R2A6_L1,2023-06,2.9896565370998385,599.4015493686493,False
R2A6_L1,2023-07,-2.4498256491270687,-505.85418868589113,False
R2A6_L1,2023-08,0.9340961869515274,188.15242599817793,False
R2A6_L1,2023-09,-0.18863415695736796,-38.35097919923646,False
R2A6_L1,2023-10,-2.0665719606866584,-419.3596612774054,False
R2A6_L1,2023-11,1.5574084655730625,309.5063816034635,False
R2A6_L1,2023-12,4.243634293715659,856.4788391138354,False
R2A6_L1,2024-01,-0.09729159272970911,-20.46932606547125,False
R2A6_L1,2024-02,-1.2811247840050721,-269.275552847128,False
R2A6_L1,2024-03,5.14833099069818,1068.2481565579983,False
R2A6_L1,2024-04,6.490249935618797,1416.0203568002107,False
R2A6_L1,2024-05,0.26004888794952663,60.41891508469416,False
R2A6_L1,2024-06,-2.7619115638083946,-643.3622907029458,False
R2A6_L1,2024-07,-4.9688032851693436,-1125.4703279708701,False
R2A6_L1,2024-08,1.223974234240921,263.4636597336648,False
R2A6_L1,2024-09,2.7684362572210963,603.2069788905028,False
R2A6_L1,2024-10,1.1329509540830118,253.68961354203566,False
R2A6_L1,2024-11,15.27070860870554,3458.1469742903028,False
R2A6_L1,2024-12,1.025591363436762,267.7180018807667,False
R2A6_L1,2025-01,4.1828369788525555,1103.0763162456315,False
R2A6_L1,2025-02,1.4657744725612432,402.7151376875372,False
R2A6_L1,2025-03,3.491109925973035,973.2264403179543,False
R2A6_L1,2025-04,0.6563370935325663,189.35656625526462,False
R2A6_L1,2025-05,7.320468871784636,2125.8540293650804,False
R2A6_L1,2025-06,3.139755995983906,978.5274253906318,False
R2A6_L1,2025-07,1.806312606613214,580.6255147286647,False
R2A6_L1,2025-08,1.5054649017026467,492.66141055044136,False
R2A6_L1,2025-09,-0.15772516675348625,-52.39240456376865,False
R2A6_L1,2025-10,4.50340958631279,1493.56198521224,False
R2A6_L1,2025-11,0.40314952802906756,139.726383728972,False
R2A6_L1,2025-12,-3.0055495391624443,-1045.8839308247407,True
R2A6_L3,2020-10,-3.428315964862161,-342.83159648621586,True
R2A6_L3,2020-11,0.5462182525591164,52.74921650036413,False
R2A6_L3,2020-12,11.030664986670535,1071.0684831454528,False
R2A6_L3,2021-01,2.060837183987463,222.17857041443312,False
R2A6_L3,2021-02,17.994602876069198,1979.9757868095821,False
R2A6_L3,2021-03,1.3027071615339336,169.13230056942848,False
R2A6_L3,2021-04,-7.855582126984317,-1033.1875883016546,False
R2A6_L3,2021-05,-1.497726261144472,-181.51072124126586,False
R2A6_L3,2021-06,1.6330510966338085,194.94669049023105,False
R2A6_L3,2021-07,12.604958678344236,1529.2992765779181,False
R2A6_L3,2021-08,-5.914647053139155,-808.0484587866886,False
R2A6_L3,2021-09,-1.5994987411860562,-205.59592069019345,False
R2A6_L3,2021-10,14.553689446395989,1840.7762613497307,False
R2A6_L3,2021-11,7.498119547665305,1086.3989646845293,False
R2A6_L3,2021-12,2.107460808403938,328.24442368187374,False
R2A6_L3,2022-01,-1.2792519189219087,-203.44705302550028,False
R2A6_L3,2022-02,-3.178970365539824,-499.1030724743541,False
R2A6_L3,2022-03,9.573920819264735,1455.3360659228165,False
R2A6_L3,2022-04,1.5029669071541907,250.33990381529293,False
R2A6_L3,2022-05,0.4702828526808922,79.50941231999968,False
R2A6_L3,2022-06,0.728242381624522,123.70093278411878,False
R2A6_L3,2022-07,-3.017334384525494,-516.2638577255893,False
R2A6_L3,2022-08,-1.6064235026896467,-266.5645830369467,False
R2A6_L3,2022-09,3.5436671840975986,578.5782066211759,False
R2A6_L3,2022-10,0.901238650378855,152.3605370849982,False
R2A6_L3,2022-11,0.40070079103846634,68.35170995495719,False
R2A6_L3,2022-12,6.071032880027061,1039.749004283036,False
R2A6_L3,2023-01,23.406763197253923,4252.106049563954,False
R2A6_L3,2023-02,1.5616683374235052,350.0986955758053,False
R2A6_L3,2023-03,-0.2656157912829027,-60.47632674704073,False
R2A6_L3,2023-04,-0.01742354736098406,-3.956516713002202,False
R2A6_L3,2023-05,-1.7941617186003622,-407.34494791000543,False
R2A6_L3,2023-06,6.326058241949939,1410.4939946054983,False
R2A6_L3,2023-07,-2.3166243983934742,-549.2036251439422,False
R2A6_L3,2023-08,0.8179642333087545,189.4230137867453,False
R2A6_L3,2023-09,-1.3735496821271176,-320.68653462201837,False
R2A6_L3,2023-10,-2.674975271633817,-615.955767560652,False
R2A6_L3,2023-11,1.433195152961031,321.1882195573635,False
R2A6_L3,2023-12,9.851932562964883,2239.5244781503607,False
R2A6_L3,2024-01,-0.09245405234666881,-23.08702835470467,False
R2A6_L3,2024-02,-0.4475563578287156,-111.6575533338073,False
R2A6_L3,2024-03,6.215603331751796,1543.7450993633174,False
R2A6_L3,2024-04,6.707153035117508,1769.3707237419258,False
R2A6_L3,2024-05,2.2883837780966587,644.1737374856457,False
R2A6_L3,2024-06,-2.763570524504755,-795.7396947501875,False
R2A6_L3,2024-07,-3.687087716903059,-1032.3166782010194,False
R2A6_L3,2024-08,0.7778708412463642,209.75942383272923,False
R2A6_L3,2024-09,4.501326065526001,1223.2624408756456,False
R2A6_L3,2024-10,1.5626230056465573,443.7671837445887,False
R2A6_L3,2024-11,14.359258658323482,4141.588029676004,False
R2A6_L3,2024-12,1.028073004345642,339.10185443944647,False
R2A6_L3,2025-01,7.536657648149436,2511.4646332976627,False
R2A6_L3,2025-02,2.4753969328895176,887.0531885908713,False
R2A6_L3,2025-03,5.68280719013754,2086.8313063717433,False
R2A6_L3,2025-04,1.1827676466469539,459.0163963379964,False
R2A6_L3,2025-05,7.335291546018441,2880.3993021547794,False
R2A6_L3,2025-06,2.671733322066139,1126.084458089601,False
R2A6_L3,2025-07,2.3190707015615653,1003.5586082763548,False
R2A6_L3,2025-08,1.5059994013273625,666.8223345562656,False
R2A6_L3,2025-09,1.506409789840979,677.049122199016,False
R2A6_L3,2025-10,3.263593238687812,1488.9034698271644,False
R2A6_L3,2025-11,0.6684888176868187,314.92845110235066,False
R2A6_L3,2025-12,-5.060056533180068,-2399.7536924227825,True
R2A6_L3_F95,2020-10,-3.5001337768203356,-350.013377682033,True
R2A6_L3_F95,2020-11,0.14943303235872563,14.420267631940078,False
R2A6_L3_F95,2020-12,10.496984326776925,1014.471276513992,False
R2A6_L3_F95,2021-01,1.9659244235525009,209.93867403592958,False
R2A6_L3_F95,2021-02,17.462431906085097,1901.452226150608,False
R2A6_L3_F95,2021-03,0.9790754472616126,125.22638407027262,False
R2A6_L3_F95,2021-04,-8.387127477281753,-1083.2390677744716,False
R2A6_L3_F95,2021-05,-1.6121200163302651,-190.75017353299154,False
R2A6_L3_F95,2021-06,1.572621295839527,183.07680580571287,False
R2A6_L3_F95,2021-07,12.135301226738914,1434.9487677026282,False
R2A6_L3_F95,2021-08,-6.047335881475002,-801.848423224199,False
R2A6_L3_F95,2021-09,-1.7391041400296348,-216.65208706027988,False
R2A6_L3_F95,2021-10,13.767836484123652,1685.3251695871186,False
R2A6_L3_F95,2021-11,6.475036089151898,901.736605537948,False
R2A6_L3_F95,2021-12,1.806801283980164,267.9141755767396,False
R2A6_L3_F95,2022-01,-1.3616052031143577,-205.5480198155019,False
R2A6_L3_F95,2022-02,-3.2933545634799666,-490.39561770236105,False
R2A6_L3_F95,2022-03,8.961828955723616,1290.5090680767225,False
R2A6_L3_F95,2022-04,0.9203617119557528,144.41002309307623,False
R2A6_L3_F95,2022-05,0.3806354393591116,60.27355588500359,False
R2A6_L3_F95,2022-06,0.6256237290359623,99.44449478394017,False
R2A6_L3_F95,2022-07,-3.1568076090557007,-504.92192961645196,False
R2A6_L3_F95,2022-08,-1.7881755569682967,-276.9844382950687,False
R2A6_L3_F95,2022-09,3.397646201954263,516.8769297750987,False
R2A6_L3_F95,2022-10,0.7959861225987019,125.20600059499884,False
R2A6_L3_F95,2022-11,0.0914206186812816,14.494626909785438,False
R2A6_L3_F95,2022-12,5.66724916150434,899.3568469037837,False
R2A6_L3_F95,2023-01,24.142460794401565,4048.383767551808,False
R2A6_L3_F95,2023-02,1.1376545833572393,236.8268348370584,False
R2A6_L3_F95,2023-03,-0.34344567518872493,-72.3088442104854,False
R2A6_L3_F95,2023-04,-0.22068096769166656,-46.302465273682174,False
R2A6_L3_F95,2023-05,-2.1845728499264916,-457.34749277269657,False
R2A6_L3_F95,2023-06,5.916157884302731,1211.5096616868504,False
R2A6_L3_F95,2023-07,-2.704906774637972,-586.6804905007739,False
R2A6_L3_F95,2023-08,0.6319913350930184,133.36792898794738,False
R2A6_L3_F95,2023-09,-1.7897932989209053,-380.08368478146804,False
R2A6_L3_F95,2023-10,-3.053855640487535,-636.9150023770126,False
R2A6_L3_F95,2023-11,0.9191404525499047,185.84265315180164,False
R2A6_L3_F95,2023-12,8.575338516361896,1749.799679129199,False
R2A6_L3_F95,2024-01,-0.20551344200697708,-45.53113584336097,False
R2A6_L3_F95,2024-02,-0.8128953502567038,-179.72539179528394,False
R2A6_L3_F95,2024-03,5.693389678645389,1248.5355778544035,False
R2A6_L3_F95,2024-04,6.165109620295128,1428.9552950698962,False
R2A6_L3_F95,2024-05,1.5408013305479251,379.14584093545636,False
R2A6_L3_F95,2024-06,-3.1346824316237476,-783.2380686121069,False
R2A6_L3_F95,2024-07,-4.083602506104855,-988.3528210553668,False
R2A6_L3_F95,2024-08,0.4081412490961611,94.74840169978779,False
R2A6_L3_F95,2024-09,4.012956509535992,935.3944396271581,False
R2A6_L3_F95,2024-10,1.352690741335949,327.9565351405581,False
R2A6_L3_F95,2024-11,13.383080183281093,3288.5854801472487,False
R2A6_L3_F95,2024-12,0.8448960216532742,235.39897694397223,False
R2A6_L3_F95,2025-01,-0.4052927298001108,-113.87385987733433,False
R2A6_L3_F95,2025-02,0.15582565882483745,43.604414525929315,False
R2A6_L3_F95,2025-03,5.0713473218675365,1421.3173533545923,False
R2A6_L3_F95,2025-04,0.7302132411951545,215.03131385430243,False
R2A6_L3_F95,2025-05,6.867402263504618,2037.061989836453,False
R2A6_L3_F95,2025-06,1.7845099547295185,565.6867228279662,False
R2A6_L3_F95,2025-07,1.386663538422317,447.41423424167806,False
R2A6_L3_F95,2025-08,1.2706042633906955,415.65196722454857,False
R2A6_L3_F95,2025-09,0.9707816524665569,321.60625961170444,False
R2A6_L3_F95,2025-10,2.3882605915146238,798.8778210309029,False
R2A6_L3_F95,2025-11,0.42949106755472144,147.0967077782916,False
R2A6_L3_F95,2025-12,-5.529665491798063,-1901.993107814993,True
R3A9_L1,2020-10,-3.7936285818260918,-379.36285818260876,True
R3A9_L1,2020-11,0.598566699122749,57.58593017435305,False
R3A9_L1,2020-12,9.363988149713043,906.2676615641012,False
R3A9_L1,2021-01,0.5323265761679519,56.34405712675107,False
R3A9_L1,2021-02,23.202047012365036,2468.8914906422706,False
R3A9_L1,2021-03,2.2663733012807885,297.1153363109388,False
R3A9_L1,2021-04,-5.623690272439874,-753.959247892406,False
R3A9_L1,2021-05,-2.8195847209796066,-356.75873806080745,False
R3A9_L1,2021-06,1.6350869091905418,201.0523078395272,False
R3A9_L1,2021-07,12.695130185722348,1586.5327550611019,False
R3A9_L1,2021-08,-5.904185351743441,-831.5282657278003,False
R3A9_L1,2021-09,-1.0256907300469686,-135.92638618786805,False
R3A9_L1,2021-10,16.289389195417115,2136.5576688697493,False
R3A9_L1,2021-11,5.507282804099045,840.0154765310981,False
R3A9_L1,2021-12,1.792056538899356,288.3925619175516,False
R3A9_L1,2022-01,-2.005566958277194,-328.5363306684958,False
R3A9_L1,2022-02,-1.9544834881789153,-313.74704684019343,False
R3A9_L1,2022-03,8.108285444279751,1276.157886974026,False
R3A9_L1,2022-04,3.7833192399121085,643.7353348070028,False
R3A9_L1,2022-05,0.26526788106180366,46.84320308500537,False
R3A9_L1,2022-06,0.7233959695098102,128.08212339057718,False
R3A9_L1,2022-07,-4.749631575021929,-847.0376547272026,False
R3A9_L1,2022-08,-1.8100319376272211,-307.4650076691578,False
R3A9_L1,2022-09,4.128949390403491,688.6778844444889,False
R3A9_L1,2022-10,0.977395067025566,169.7532924599982,False
R3A9_L1,2022-11,1.2899246357964689,226.2228991791817,False
R3A9_L1,2022-12,5.910762774877987,1049.9823629791608,False
R3A9_L1,2023-01,15.554079153448065,2926.32713983527,False
R3A9_L1,2023-02,1.5569050643626792,338.47452137329674,False
R3A9_L1,2023-03,-0.18496350606788114,-40.8375197811547,False
R3A9_L1,2023-04,-0.2730298961577171,-60.16992672124252,False
R3A9_L1,2023-05,-0.572226933504727,-125.76222098333892,False
R3A9_L1,2023-06,2.9911068710111177,653.6143012400862,False
R3A9_L1,2023-07,-2.449240335759395,-551.2146408114058,False
R3A9_L1,2023-08,0.934157430009841,205.08791477218256,False
R3A9_L1,2023-09,-0.18894137522639243,-41.86829072042383,False
R3A9_L1,2023-10,-2.3099167591355774,-510.896762604978,False
R3A9_L1,2023-11,1.7051972103296897,368.4358773139429,False
R3A9_L1,2023-12,4.24566004517819,932.9871528337062,False
R3A9_L1,2024-01,-0.09229029303362557,-21.14192146413552,False
R3A9_L1,2024-02,-1.2846027765912815,-294.00606531267476,False
R3A9_L1,2024-03,5.14383948840722,1162.1434508546954,False
R3A9_L1,2024-04,6.936992473501791,1647.8868427058478,False
R3A9_L1,2024-05,0.12337868651863815,31.34182425790641,False
R3A9_L1,2024-06,-2.6770667945349214,-680.8929420329769,False
R3A9_L1,2024-07,-5.735164381646385,-1419.6480327763202,False
R3A9_L1,2024-08,1.6393175343079491,382.5142453154913,False
R3A9_L1,2024-09,2.978646759196213,706.4237184551093,False
R3A9_L1,2024-10,1.1161683042530512,272.59829539428756,False
R3A9_L1,2024-11,17.748123807000326,4382.949873170699,False
R3A9_L1,2024-12,1.0346591254554616,300.8606174503111,False
R3A9_L1,2025-01,4.186740847208648,1230.0266190177754,False
R3A9_L1,2025-02,1.6175914465057284,495.1305517485562,False
R3A9_L1,2025-03,3.491250250486777,1085.927321944131,False
R3A9_L1,2025-04,-2.213960188151387,-712.6777839051283,False
R3A9_L1,2025-05,7.894455741611894,2484.9775316870473,False
R3A9_L1,2025-06,3.9755283429516286,1350.1880338601986,False
R3A9_L1,2025-07,1.8067855462902571,638.0241890855104,False
R3A9_L1,2025-08,1.4368220087725314,516.5474637640364,False
R3A9_L1,2025-09,-0.2269955094150622,-82.77899738096312,False
R3A9_L1,2025-10,4.500248184696853,1637.391049218786,False
R3A9_L1,2025-11,0.4031276927696448,153.27661523271672,False
R3A9_L1,2025-12,-3.0042935599909004,-1146.8929343573182,True
R3A9_L3,2020-10,-3.7936285818260918,-379.36285818260876,True
R3A9_L3,2020-11,2.167170217542269,208.49558287527725,False
R3A9_L3,2020-12,11.89875279591266,1169.5442048933346,False
R3A9_L3,2021-01,1.754348305300324,192.9551023196491,False
R3A9_L3,2021-02,21.77531277474085,2437.0128795455403,False
R3A9_L3,2021-03,2.255468153463225,307.38974572636835,False
R3A9_L3,2021-04,-7.518313516060793,-1047.7547772334965,False
R3A9_L3,2021-05,-1.9883395175628982,-256.26276198703636,False
R3A9_L3,2021-06,1.6399433538950792,207.15792518882517,False
R3A9_L3,2021-07,12.60440528296225,1618.3016574270478,False
R3A9_L3,2021-08,-5.902562686930468,-853.3616251996827,False
R3A9_L3,2021-09,-1.599498160094337,-217.59757032771086,False
R3A9_L3,2021-10,19.94324898885358,2669.7065169676953,False
R3A9_L3,2021-11,7.870704747719937,1263.7379864051418,False
R3A9_L3,2021-12,1.8131524421554968,314.03731413603964,False
R3A9_L3,2022-01,-2.000864219670906,-352.83238294200055,False
R3A9_L3,2022-02,-4.1397485936267024,-715.3968653448865,False
R3A9_L3,2022-03,12.098935566790692,2004.2818474283195,False
R3A9_L3,2022-04,1.073723331124854,199.39098008524525,False
R3A9_L3,2022-05,0.26587261732349265,49.90280910000365,False
R3A9_L3,2022-06,0.7215505036341607,135.7910837575182,False
R3A9_L3,2022-07,-4.750357402387095,-900.4367438567133,False
R3A9_L3,2022-08,-1.8101845874254785,-326.82339762515403,False
R3A9_L3,2022-09,4.128171497463029,731.8371511010191,False
R3A9_L3,2022-10,0.9773761988031593,180.42084908999823,False
R3A9_L3,2022-11,-0.12304357434272939,-22.935487939776067,False
R3A9_L3,2022-12,6.765933140235347,1259.627248115954,False
R3A9_L3,2023-01,23.400067892818143,4651.1908757022065,False
R3A9_L3,2023-02,1.6343413832550224,400.87153704977027,False
R3A9_L3,2023-03,-1.375178955288392,-342.8168329261862,False
R3A9_L3,2023-04,-0.2720049783431211,-66.87533980093576,False
R3A9_L3,2023-05,-1.7927686845929158,-439.57247931857637,False
R3A9_L3,2023-06,6.324898742532259,1523.0118466023778,False
R3A9_L3,2023-07,-2.316754997004511,-593.1503493775162,False
R3A9_L3,2023-08,0.8175673168521413,204.46938096263693,False
R3A9_L3,2023-09,-1.3727725633243315,-346.13025708852,False
R3A9_L3,2023-10,-2.9182398035658363,-725.7027614583094,False
R3A9_L3,2023-11,1.5805211892145454,381.5713542713602,False
R3A9_L3,2023-12,9.906852515299015,2429.5261352673842,False
R3A9_L3,2024-01,-0.09366594512921766,-25.24598780935412,False
R3A9_L3,2024-02,-0.44798270474023516,-120.63266417651539,False
R3A9_L3,2024-03,6.508894839452206,1744.861626574464,False
R3A9_L3,2024-04,7.347239720602139,2097.798763039682,False
R3A9_L3,2024-05,2.4816151259702934,760.6150674040036,False
R3A9_L3,2024-06,-2.6766867493761004,-840.7638051607682,False
R3A9_L3,2024-07,-4.459490837532776,-1363.2597723230028,False
R3A9_L3,2024-08,-0.16688699052572753,-48.74200367718004,False
R3A9_L3,2024-09,5.071350284759202,1478.6967469018964,False
R3A9_L3,2024-10,1.1185051174555705,342.67135153413983,False
R3A9_L3,2024-11,16.893328021629728,5233.4210581455045,False
R3A9_L3,2024-12,1.030904257685461,373.31764658922475,False
R3A9_L3,2025-01,9.194120321108334,3363.75695781815,False
R3A9_L3,2025-02,2.5329443442650756,1011.9040341872678,False
R3A9_L3,2025-03,6.116218761617986,2505.3021983561557,False
R3A9_L3,2025-04,2.181101054244672,948.0574665255699,False
R3A9_L3,2025-05,9.913362294370366,4403.017702659141,False
R3A9_L3,2025-06,3.719327475693124,1815.701134963303,False
R3A9_L3,2025-07,2.7672582233030596,1401.1651452390506,False
R3A9_L3,2025-08,1.4332161779447627,745.7720630812182,False
R3A9_L3,2025-09,1.5179612368574125,801.1895685323034,False
R3A9_L3,2025-10,4.288668019913433,2297.9465427324903,False
R3A9_L3,2025-11,1.2006220201884465,670.9048278274859,False
R3A9_L3,2025-12,-5.776742677883617,-3266.7869884692045,True
R3A9_L3_F95,2020-10,-3.9381199556223656,-393.8119955622369,True
R3A9_L3_F95,2020-11,1.600190288312775,153.71728752407944,False
R3A9_L3_F95,2020-12,11.56479185070689,1128.7127318415132,False
R3A9_L3_F95,2021-01,1.7152619520964807,186.76832207141888,False
R3A9_L3_F95,2021-02,21.485748771303182,2379.6296857258694,False
R3A9_L3_F95,2021-03,1.9316917360513663,259.9094327668172,False
R3A9_L3_F95,2021-04,-7.949731305391605,-1090.2997231519457,False
R3A9_L3_F95,2021-05,-2.188825825796936,-276.3310686339337,False
R3A9_L3_F95,2021-06,1.5663930107487012,193.422824697971,False
R3A9_L3_F95,2021-07,12.405580073521993,1555.8728067199336,False
R3A9_L3_F95,2021-08,-6.112110969048823,-861.6603633423165,False
R3A9_L3_F95,2021-09,-1.7390978102850063,-230.18576776882583,False
R3A9_L3_F95,2021-10,19.692885301611106,2561.206282587871,False
R3A9_L3_F95,2021-11,7.499549258288507,1167.4511174218042,False
R3A9_L3_F95,2021-12,1.5295506619799726,255.96115003664818,False
R3A9_L3_F95,2022-01,-2.131499424215688,-362.1494836115089,False
R3A9_L3_F95,2022-02,-4.379709432015034,-728.2674236182083,False
R3A9_L3_F95,2022-03,11.771095008375232,1871.5977282468102,False
R3A9_L3_F95,2022-04,0.29356624080854044,52.171252315631136,False
R3A9_L3_F95,2022-05,0.19486274363678113,34.73177967000083,False
R3A9_L3_F95,2022-06,0.6277736383144772,112.11061981620878,False
R3A9_L3_F95,2022-07,-5.048126506641692,-907.1764611900435,False
R3A9_L3_F95,2022-08,-2.0309508927120468,-346.54888335547366,False
R3A9_L3_F95,2022-09,3.999000626504734,668.5062104615536,False
R3A9_L3_F95,2022-10,0.8950304061274839,155.60406185999818,False
R3A9_L3_F95,2022-11,-0.5141737592321061,-90.19092152127996,False
R3A9_L3_F95,2022-12,6.305447277105358,1100.347916501465,False
R3A9_L3_F95,2023-01,23.988448262897656,4450.120814242593,False
R3A9_L3_F95,2023-02,1.2474290102676866,286.92389015662775,False
R3A9_L3_F95,2023-03,-1.6507145835584325,-384.420786324823,False
R3A9_L3_F95,2023-04,-0.5521200305582008,-126.4560426285534,False
R3A9_L3_F95,2023-05,-2.2189067509284954,-505.40631500589006,False
R3A9_L3_F95,2023-06,5.99852779024459,1335.983752231361,False
R3A9_L3_F95,2023-07,-2.7034328313030542,-638.2222171155008,False
R3A9_L3_F95,2023-08,0.6335452946546694,145.5229607371657,False
R3A9_L3_F95,2023-09,-1.7892872158793205,-413.5963375446918,False
R3A9_L3_F95,2023-10,-3.393595791997428,-770.3988060594311,False
R3A9_L3_F95,2023-11,1.1267603559639738,247.11150415852535,False
R3A9_L3_F95,2023-12,9.211504196111742,2042.951491954067,False
R3A9_L3_F95,2024-01,-0.2056463621169069,-49.81004345125257,False
R3A9_L3_F95,2024-02,-0.7221810773509807,-174.56129847968623,False
R3A9_L3_F95,2024-03,6.274303439659246,1505.634663275403,False
R3A9_L3_F95,2024-04,7.057392924289663,1799.8099613486738,False
R3A9_L3_F95,2024-05,1.9886094155709744,542.935836226894,False
R3A9_L3_F95,2024-06,-3.0295108062102782,-843.5740139333357,False
R3A9_L3_F95,2024-07,-5.035141343012217,-1359.571148404022,False
R3A9_L3_F95,2024-08,-0.6917113326648128,-177.36915242822943,False
R3A9_L3_F95,2024-09,4.806027224436216,1223.840791003382,False
R3A9_L3_F95,2024-10,0.7288143464282415,194.5099712140327,False
R3A9_L3_F95,2024-11,16.33227678455862,4390.615537675403,False
R3A9_L3_F95,2024-12,0.8520703454582446,266.47370320855043,False
R3A9_L3_F95,2025-01,0.1638246550190514,51.67053838248103,False
R3A9_L3_F95,2025-02,-0.3494295001121417,-110.39113301693214,False
R3A9_L3_F95,2025-03,5.581765690244822,1757.2195044779473,False
R3A9_L3_F95,2025-04,1.391847671682367,462.6313308108074,False
R3A9_L3_F95,2025-05,9.683911132208811,3263.6018192230113,False
R3A9_L3_F95,2025-06,2.933287752737268,1084.2862947577814,False
R3A9_L3_F95,2025-07,2.3061386108196302,877.4665125841202,False
R3A9_L3_F95,2025-08,1.1116497446349571,432.727813024394,False
R3A9_L3_F95,2025-09,1.1197512755979577,440.7269414317925,False
R3A9_L3_F95,2025-10,3.5697526757187514,1420.7646869076198,False
R3A9_L3_F95,2025-11,0.9427846876078894,388.62388210710924,False
R3A9_L3_F95,2025-12,-6.3733916135979225,-2651.93485545578,True

```
