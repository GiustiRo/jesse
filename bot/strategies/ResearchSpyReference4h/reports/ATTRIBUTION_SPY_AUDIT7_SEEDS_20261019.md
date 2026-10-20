# Atribución SPY — cinco semillas R/U completas

Jobf52a488c612b41c79cb8fff5f027e70f succeeded. Diez snapshots terminales completos, sin selección de semilla. Se reconcilian fees, PnL, balances y exposición; pares por filltimestamp exacto. Las cinco diferencias R−U son escenarios dependientes con exposición y ocupación distintas, no estadística inferencialIID. Cohortes por cierre no son retornos MTM.

## Resumen de semillas

```json
{
  "R": {
    "fixed_seeds": [
      101,
      202,
      303,
      404,
      505
    ],
    "stats": {
      "net": {
        "median": 143.1550705133505,
        "mean": 184.2946320376956,
        "min": -348.5522602051562,
        "max": 1054.7187970764467
      },
      "PF": {
        "median": 1.1755046430877696,
        "mean": 1.422231723399029,
        "min": 0.6337677065518231,
        "max": 2.9998802602602157
      },
      "DD_engine_pct": {
        "median": -4.932604907914506,
        "mean": -4.653188970398136,
        "min": -6.36507763263131,
        "max": -3.172735630771384
      },
      "fraction_time_open": {
        "median": 0.04999635079114848,
        "mean": 0.05069940736848251,
        "min": 0.037578822911192855,
        "max": 0.0611096514275705
      },
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": {
        "median": 0.0494161538196295,
        "mean": 0.05013370486476635,
        "min": 0.03730957274807745,
        "max": 0.06322744806499223
      },
      "entry_turnover_initial_equity": {
        "median": 14.782322161739998,
        "mean": 13.783433267625998,
        "min": 10.217402435570001,
        "max": 16.14554577043
      },
      "net_bps_entry": {
        "median": 9.522896835180314,
        "mean": 13.13128417644754,
        "min": -22.630857355429022,
        "max": 71.3500074978949
      },
      "stress5_RT_samefills": {
        "median": 72.94983863802037,
        "mean": 115.30034461221473,
        "min": -425.50793945331657,
        "max": 980.5101126604901
      },
      "stress10_RT_samefills": {
        "median": -7.852689443446081,
        "mean": 46.30605718673385,
        "min": -502.4636187014769,
        "max": 906.3014282445337
      },
      "net_without_top1": {
        "median": -276.5115457456816,
        "mean": -160.90956376397767,
        "min": -595.0770116026313,
        "max": 517.1645402448297
      },
      "net_without_top3": {
        "median": -582.4585689585219,
        "mean": -517.3817088049036,
        "min": -879.0400706838409,
        "max": -167.29651607237975
      }
    },
    "positive_net_count": 3,
    "positive_stress5_count": 3,
    "positive_stress10_count": 2,
    "limitation": "Five dependent scenario controls, no winning-seed selection and no IID significance."
  },
  "U": {
    "fixed_seeds": [
      101,
      202,
      303,
      404,
      505
    ],
    "stats": {
      "net": {
        "median": 75.7426645169086,
        "mean": 601.425713214546,
        "min": -1075.4610284377702,
        "max": 2572.1409833508283
      },
      "PF": {
        "median": 1.0200818630649156,
        "mean": 1.1421561934446207,
        "min": 0.7409558002321476,
        "max": 1.6407248804879624
      },
      "DD_engine_pct": {
        "median": -14.787161148432038,
        "mean": -13.394508345704244,
        "min": -18.079394862500987,
        "max": -5.493244162762901
      },
      "fraction_time_open": {
        "median": 0.2673797220762539,
        "mean": 0.28444013837799964,
        "min": 0.2590223039645005,
        "max": 0.31994694050329886
      },
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": {
        "median": 0.2281749269603607,
        "mean": 0.22894590026966885,
        "min": 0.1822818730405191,
        "max": 0.26339021303636406
      },
      "entry_turnover_initial_equity": {
        "median": 63.79241471099,
        "mean": 63.044665280744006,
        "min": 55.49081408547999,
        "max": 71.51584333126
      },
      "net_bps_entry": {
        "median": 1.364958610991577,
        "mean": 8.62514254512624,
        "min": -17.953889526974002,
        "max": 40.32048316408543
      },
      "stress5_RT_samefills": {
        "median": -201.85526064294223,
        "mean": 285.910048333326,
        "min": -1374.8332987466995,
        "max": 2252.3919875019083
      },
      "stress10_RT_samefills": {
        "median": -479.45318580279366,
        "mean": -29.605616547894236,
        "min": -1674.2055690556292,
        "max": 1932.6429916529887
      },
      "net_without_top1": {
        "median": -305.6646422200623,
        "mean": 54.4463930825528,
        "min": -1413.3304284421129,
        "max": 2005.5306829129077
      },
      "net_without_top3": {
        "median": -995.5594235388447,
        "mean": -850.9599027515058,
        "min": -2029.0513462937815,
        "max": 959.5942650886718
      }
    },
    "positive_net_count": 3,
    "positive_stress5_count": 2,
    "positive_stress10_count": 2,
    "limitation": "Five dependent scenario controls, no winning-seed selection and no IID significance."
  },
  "paired_seed_differences_R_minus_U": [
    {
      "seed": 101,
      "net_R": -81.60081391564947,
      "net_U": 1874.981553550459,
      "net_difference": -1956.5823674661085,
      "time_R": 0.043761677468324864,
      "time_U": 0.30974046826647983,
      "notionaltime_R": 0.03730957274807745,
      "notionaltime_U": 0.26339021303636406,
      "common_entries": 6
    },
    {
      "seed": 202,
      "net_R": 1054.7187970764467,
      "net_U": 2572.1409833508283,
      "net_difference": -1517.4221862743816,
      "time_R": 0.061050534244175864,
      "time_U": 0.31994694050329886,
      "notionaltime_R": 0.06322744806499223,
      "notionaltime_U": 0.2605476399199419,
      "common_entries": 6
    },
    {
      "seed": 303,
      "net_R": 153.75236671948676,
      "net_U": -440.27560690769474,
      "net_difference": 594.0279736271815,
      "time_R": 0.0611096514275705,
      "time_U": 0.2673797220762539,
      "notionaltime_R": 0.05947272629465539,
      "notionaltime_U": 0.2281749269603607,
      "common_entries": 14
    },
    {
      "seed": 404,
      "net_R": -348.5522602051562,
      "net_U": -1075.4610284377702,
      "net_difference": 726.908768232614,
      "time_R": 0.04999635079114848,
      "time_U": 0.2590223039645005,
      "notionaltime_R": 0.0494161538196295,
      "notionaltime_U": 0.1822818730405191,
      "common_entries": 11
    },
    {
      "seed": 505,
      "net_R": 143.1550705133505,
      "net_U": 75.7426645169086,
      "net_difference": 67.41240599644189,
      "time_R": 0.037578822911192855,
      "time_U": 0.26611125707946515,
      "notionaltime_R": 0.0412426233964772,
      "notionaltime_U": 0.2103348483911586,
      "common_entries": 7
    }
  ]
}
```

## Métricas y pares resumidos

```json
{
  "metrics": {
    "AttrSpyR01": {
      "session_id": "83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
      "n": 11,
      "net": -81.60081391564947,
      "gross_price": 29.744897958351785,
      "fee": 111.34571187400127,
      "PF": 0.8749054563501013,
      "return_pct": -0.8160081391564946,
      "DD_engine_pct": -4.932604907914506,
      "hours_open": 1998.6833333333334,
      "fraction_time_open": 0.043761677468324864,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.03730957274807745,
      "entry_turnover_initial_equity": 12.37025851888,
      "roundtrip_turnover_initial_equity": 24.743491527555832,
      "net_bps_entry": -6.5965326263074395,
      "net_per_exposure_entry_time_measure": -0.2187128072107294,
      "max_initial_gross_equity": 1.4695131277252376,
      "mean_hours": 181.69848484848487,
      "max_hours": 822.1666666666666,
      "stress5_RT_samefills": -143.45954273453907,
      "stress10_RT_samefills": -205.3182715534287,
      "net_without_top1": -293.7253850607877,
      "net_without_top3": -582.4585689585219,
      "net_without_top5": -564.5479163192607,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 168.79131639148233,
          "fee": 3.5746040598531006
        },
        "2021": {
          "n": 2,
          "net": 32.17664901745039,
          "fee": 24.600899852491473
        },
        "2022": {
          "n": 1,
          "net": -93.53347295188989,
          "fee": 7.588225023242109
        },
        "2023": {
          "n": 5,
          "net": -8.704614518796092,
          "fee": 56.99794337516536
        },
        "2024": {
          "n": 2,
          "net": -180.3306918538962,
          "fee": 18.584039563249206
        }
      },
      "entry_order_types": {
        "MARKET": 11
      },
      "exit_order_types": {
        "STOP": 11
      },
      "entry_clock_UTC": {
        "Fri 08:00": 1,
        "Thu 12:00": 1,
        "Wed 08:00": 1,
        "Mon 08:00": 2,
        "Tue 16:00": 1,
        "Mon 04:00": 1,
        "Tue 04:00": 1,
        "Wed 04:00": 2,
        "Thu 04:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyR02": {
      "session_id": "c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
      "n": 13,
      "net": 1054.7187970764467,
      "gross_price": 1188.2944290251678,
      "fee": 133.5756319487213,
      "PF": 2.9998802602602157,
      "return_pct": 10.547187970764467,
      "DD_engine_pct": -3.2489130528813193,
      "hours_open": 2788.3,
      "fraction_time_open": 0.061050534244175864,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.06322744806499223,
      "entry_turnover_initial_equity": 14.782322161739998,
      "roundtrip_turnover_initial_equity": 29.683473766382516,
      "net_bps_entry": 71.3500074978949,
      "net_per_exposure_entry_time_measure": 1.6681343773234198,
      "max_initial_gross_equity": 1.5373013702518947,
      "mean_hours": 214.48461538461538,
      "max_hours": 566.1,
      "stress5_RT_samefills": 980.5101126604901,
      "stress10_RT_samefills": 906.3014282445337,
      "net_without_top1": 517.1645402448297,
      "net_without_top3": -167.29651607237975,
      "net_without_top5": -461.0282596819127,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2021": {
          "n": 2,
          "net": 513.384189900414,
          "fee": 17.92400678941042
        },
        "2022": {
          "n": 2,
          "net": 142.17493275326405,
          "fee": 11.989097976748505
        },
        "2023": {
          "n": 4,
          "net": 676.3404909230329,
          "fee": 44.64688774368002
        },
        "2024": {
          "n": 4,
          "net": -236.2084088427781,
          "fee": 51.37663478595442
        },
        "2025": {
          "n": 1,
          "net": -40.97240765748627,
          "fee": 7.639004652927948
        }
      },
      "entry_order_types": {
        "MARKET": 13
      },
      "exit_order_types": {
        "STOP": 13
      },
      "entry_clock_UTC": {
        "Wed 04:00": 1,
        "Mon 04:00": 2,
        "Wed 16:00": 1,
        "Tue 12:00": 2,
        "Thu 12:00": 3,
        "Fri 08:00": 2,
        "Mon 08:00": 1,
        "Tue 08:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyR03": {
      "session_id": "205744ff-a7cd-46e8-893b-17e9ebf31fa9",
      "n": 16,
      "net": 153.75236671948676,
      "gross_price": 299.1969172661266,
      "fee": 145.44455054663976,
      "PF": 1.1755046430877696,
      "return_pct": 1.5375236671948675,
      "DD_engine_pct": -5.546613627792163,
      "hours_open": 2791,
      "fraction_time_open": 0.0611096514275705,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.05947272629465539,
      "entry_turnover_initial_equity": 16.14554577043,
      "roundtrip_turnover_initial_equity": 32.32101123258661,
      "net_bps_entry": 9.522896835180314,
      "net_per_exposure_entry_time_measure": 0.2585258425143089,
      "max_initial_gross_equity": 1.2321821371740393,
      "mean_hours": 174.4375,
      "max_hours": 655.9,
      "stress5_RT_samefills": 72.94983863802037,
      "stress10_RT_samefills": -7.852689443446081,
      "net_without_top1": -276.5115457456816,
      "net_without_top3": -647.7774062496329,
      "net_without_top5": -876.0586843425862,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2021": {
          "n": 3,
          "net": 219.5424666053639,
          "fee": 30.265958261370027
        },
        "2022": {
          "n": 3,
          "net": 52.867882487434585,
          "fee": 17.189810725685902
        },
        "2023": {
          "n": 5,
          "net": 118.59284374369355,
          "fee": 49.85814617339269
        },
        "2024": {
          "n": 3,
          "net": -53.66485280241129,
          "fee": 28.19129766212687
        },
        "2025": {
          "n": 2,
          "net": -183.5859733145939,
          "fee": 19.93933772406426
        }
      },
      "entry_order_types": {
        "MARKET": 16
      },
      "exit_order_types": {
        "STOP": 16
      },
      "entry_clock_UTC": {
        "Wed 08:00": 1,
        "Thu 12:00": 2,
        "Mon 12:00": 2,
        "Tue 04:00": 3,
        "Mon 08:00": 1,
        "Fri 08:00": 1,
        "Wed 12:00": 1,
        "Mon 16:00": 1,
        "Fri 04:00": 1,
        "Tue 08:00": 1,
        "Thu 04:00": 1,
        "Thu 08:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyR04": {
      "session_id": "a657dc36-13bd-440f-a423-917ab3caeb8c",
      "n": 16,
      "net": -348.5522602051562,
      "gross_price": -210.03203755846747,
      "fee": 138.5202226466887,
      "PF": 0.6337677065518231,
      "return_pct": -3.485522602051562,
      "DD_engine_pct": -6.36507763263131,
      "hours_open": 2283.4333333333334,
      "fraction_time_open": 0.04999635079114848,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.0494161538196295,
      "entry_turnover_initial_equity": 15.40163745151,
      "roundtrip_turnover_initial_equity": 30.782271699264157,
      "net_bps_entry": -22.630857355429022,
      "net_per_exposure_entry_time_measure": -0.7053407302344549,
      "max_initial_gross_equity": 1.3681939412530502,
      "mean_hours": 142.71458333333334,
      "max_hours": 679.9666666666667,
      "stress5_RT_samefills": -425.50793945331657,
      "stress10_RT_samefills": -502.4636187014769,
      "net_without_top1": -595.0770116026313,
      "net_without_top3": -879.0400706838409,
      "net_without_top5": -945.5837032974184,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2021": {
          "n": 1,
          "net": -87.53574379017371,
          "fee": 11.183231415431367
        },
        "2022": {
          "n": 3,
          "net": -103.60912490261549,
          "fee": 16.54516014454887
        },
        "2023": {
          "n": 4,
          "net": -37.84200265865744,
          "fee": 36.797028561676356
        },
        "2024": {
          "n": 5,
          "net": -193.6776157233023,
          "fee": 45.618157614100866
        },
        "2025": {
          "n": 3,
          "net": 74.11222686959277,
          "fee": 28.376644910931233
        }
      },
      "entry_order_types": {
        "MARKET": 16
      },
      "exit_order_types": {
        "STOP": 16
      },
      "entry_clock_UTC": {
        "Wed 12:00": 4,
        "Thu 08:00": 2,
        "Mon 04:00": 3,
        "Thu 12:00": 2,
        "Wed 04:00": 1,
        "Tue 12:00": 1,
        "Fri 16:00": 2,
        "Fri 08:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyR05": {
      "session_id": "ee7ee861-0137-4d13-a95d-837cb2a3e97e",
      "n": 9,
      "net": 143.1550705133505,
      "gross_price": 235.21754032662747,
      "fee": 92.06246981327698,
      "PF": 1.4271005507452341,
      "return_pct": 1.4315507051335048,
      "DD_engine_pct": -3.172735630771384,
      "hours_open": 1716.3,
      "fraction_time_open": 0.037578822911192855,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.0412426233964772,
      "entry_turnover_initial_equity": 10.217402435570001,
      "roundtrip_turnover_initial_equity": 20.45832662517266,
      "net_bps_entry": 14.010906530898943,
      "net_per_exposure_entry_time_measure": 0.3471046667840686,
      "max_initial_gross_equity": 1.46648212167,
      "mean_hours": 190.7,
      "max_hours": 518.1,
      "stress5_RT_samefills": 92.00925395041884,
      "stress10_RT_samefills": 40.863437387487146,
      "net_without_top1": -156.39841665561738,
      "net_without_top3": -310.33598206014244,
      "net_without_top5": -314.02732177894984,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2021": {
          "n": 2,
          "net": 258.6540164324854,
          "fee": 22.1566212339599
        },
        "2023": {
          "n": 4,
          "net": -197.05126433626992,
          "fee": 40.84671927921433
        },
        "2024": {
          "n": 1,
          "net": 24.842865786257544,
          "fee": 9.983253560285942
        },
        "2025": {
          "n": 2,
          "net": 56.70945263087748,
          "fee": 19.07587573981681
        }
      },
      "entry_order_types": {
        "MARKET": 9
      },
      "exit_order_types": {
        "STOP": 8,
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Fri 12:00": 2,
        "Wed 04:00": 1,
        "Thu 04:00": 1,
        "Wed 12:00": 1,
        "Mon 08:00": 1,
        "Tue 04:00": 1,
        "Tue 12:00": 1,
        "Wed 08:00": 1
      },
      "terminal_liquidations": [
        "c642a8a9-372a-4adb-826e-16dbeb5cd6b2"
      ],
      "engine_open_count_preterminal": 1
    },
    "AttrSpyU01": {
      "session_id": "da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
      "n": 72,
      "net": 1874.981553550459,
      "gross_price": 2519.75803464739,
      "fee": 644.7764810969313,
      "PF": 1.4081758729933123,
      "return_pct": 18.74981553550459,
      "DD_engine_pct": -11.630293408060766,
      "hours_open": 14146.466666666667,
      "fraction_time_open": 0.30974046826647983,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.26339021303636406,
      "entry_turnover_initial_equity": 71.51584333126,
      "roundtrip_turnover_initial_equity": 143.28366246598475,
      "net_bps_entry": 26.217708779096416,
      "net_per_exposure_entry_time_measure": 0.7118645495349504,
      "max_initial_gross_equity": 1.627684429590486,
      "mean_hours": 196.4787037037037,
      "max_hours": 862.9166666666666,
      "stress5_RT_samefills": 1516.7723973854968,
      "stress10_RT_samefills": 1158.5632412205346,
      "net_without_top1": 1036.1887244199975,
      "net_without_top3": -216.22479047230763,
      "net_without_top5": -1130.368084748569,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 168.79131639148233,
          "fee": 3.5746040598531006
        },
        "2021": {
          "n": 11,
          "net": 667.5123662181792,
          "fee": 86.12348444678923
        },
        "2022": {
          "n": 14,
          "net": 566.2761995069535,
          "fee": 72.37452116244124
        },
        "2023": {
          "n": 12,
          "net": 1427.4810650632614,
          "fee": 130.246140694571
        },
        "2024": {
          "n": 18,
          "net": -1044.8584835174588,
          "fee": 211.99855944596786
        },
        "2025": {
          "n": 16,
          "net": 89.77908988804113,
          "fee": 140.45917128730892
        }
      },
      "entry_order_types": {
        "MARKET": 72
      },
      "exit_order_types": {
        "STOP": 71,
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Fri 08:00": 4,
        "Tue 16:00": 2,
        "Thu 12:00": 1,
        "Tue 04:00": 3,
        "Fri 12:00": 4,
        "Wed 12:00": 2,
        "Fri 04:00": 3,
        "Wed 08:00": 5,
        "Wed 16:00": 4,
        "Mon 08:00": 4,
        "Thu 04:00": 7,
        "Mon 12:00": 7,
        "Thu 08:00": 6,
        "Fri 16:00": 4,
        "Thu 16:00": 3,
        "Wed 04:00": 2,
        "Tue 12:00": 4,
        "Mon 04:00": 5,
        "Mon 16:00": 2
      },
      "terminal_liquidations": [
        "bdc18c58-adf4-421d-a13f-3a17fce914b6"
      ],
      "engine_open_count_preterminal": 1
    },
    "AttrSpyU02": {
      "session_id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
      "n": 70,
      "net": 2572.1409833508283,
      "gross_price": 3147.689175878884,
      "fee": 575.5481925280554,
      "PF": 1.6407248804879624,
      "return_pct": 25.721409833508286,
      "DD_engine_pct": -5.493244162762901,
      "hours_open": 14612.616666666667,
      "fraction_time_open": 0.31994694050329886,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.2605476399199419,
      "entry_turnover_initial_equity": 63.79241471099,
      "roundtrip_turnover_initial_equity": 127.89959833956789,
      "net_bps_entry": 40.32048316408543,
      "net_per_exposure_entry_time_measure": 0.9872056350773956,
      "max_initial_gross_equity": 1.6472629528153622,
      "mean_hours": 208.75166666666667,
      "max_hours": 974.1,
      "stress5_RT_samefills": 2252.3919875019083,
      "stress10_RT_samefills": 1932.6429916529887,
      "net_without_top1": 2005.5306829129077,
      "net_without_top3": 959.5942650886718,
      "net_without_top5": -24.460416754159723,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 22.87548955378361,
          "fee": 7.34693468032535
        },
        "2021": {
          "n": 12,
          "net": 703.1149467662979,
          "fee": 93.41472079159105
        },
        "2022": {
          "n": 12,
          "net": -160.8586197508117,
          "fee": 67.14035124088052
        },
        "2023": {
          "n": 16,
          "net": 533.4561286188031,
          "fee": 138.97121450675652
        },
        "2024": {
          "n": 14,
          "net": 1340.2552945944208,
          "fee": 133.58314860732077
        },
        "2025": {
          "n": 15,
          "net": 133.29774356833505,
          "fee": 135.0918227011813
        }
      },
      "entry_order_types": {
        "MARKET": 70
      },
      "exit_order_types": {
        "STOP": 70
      },
      "entry_clock_UTC": {
        "Thu 08:00": 3,
        "Thu 04:00": 3,
        "Tue 04:00": 4,
        "Mon 12:00": 8,
        "Mon 16:00": 3,
        "Thu 12:00": 7,
        "Fri 04:00": 5,
        "Fri 16:00": 5,
        "Wed 04:00": 3,
        "Fri 12:00": 1,
        "Tue 08:00": 4,
        "Thu 16:00": 1,
        "Mon 04:00": 4,
        "Tue 16:00": 4,
        "Wed 12:00": 2,
        "Tue 12:00": 3,
        "Fri 08:00": 3,
        "Mon 08:00": 4,
        "Wed 16:00": 2,
        "Wed 08:00": 1
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyU03": {
      "session_id": "63dd9d81-c7bf-417b-823f-728977051fd8",
      "n": 74,
      "net": -440.27560690769474,
      "gross_price": 140.49435155449498,
      "fee": 580.7699584621895,
      "PF": 0.9008425504447655,
      "return_pct": -4.402756069076948,
      "DD_engine_pct": -14.787161148432038,
      "hours_open": 12211.766666666666,
      "fraction_time_open": 0.2673797220762539,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.2281749269603607,
      "entry_turnover_initial_equity": 64.52297066711002,
      "roundtrip_turnover_initial_equity": 129.05999076937547,
      "net_bps_entry": -6.823548301568223,
      "net_per_exposure_entry_time_measure": -0.19295529652308416,
      "max_initial_gross_equity": 1.3578716028398357,
      "mean_hours": 165.0238738738739,
      "max_hours": 870.1666666666666,
      "stress5_RT_samefills": -762.925583831133,
      "stress10_RT_samefills": -1085.5755607545716,
      "net_without_top1": -1050.492371257966,
      "net_without_top3": -2029.0513462937815,
      "net_without_top5": -2675.7578819256432,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 1,
          "net": 309.4219660632779,
          "fee": 3.2929018880180827
        },
        "2021": {
          "n": 16,
          "net": 571.5593222133468,
          "fee": 127.9767386767005
        },
        "2022": {
          "n": 17,
          "net": -784.684385785174,
          "fee": 94.72499574865355
        },
        "2023": {
          "n": 16,
          "net": 116.3945247435512,
          "fee": 143.34163632363024
        },
        "2024": {
          "n": 13,
          "net": -61.59589831361469,
          "fee": 121.45753048723812
        },
        "2025": {
          "n": 11,
          "net": -591.3711358290823,
          "fee": 89.97615533794898
        }
      },
      "entry_order_types": {
        "MARKET": 74
      },
      "exit_order_types": {
        "STOP": 74
      },
      "entry_clock_UTC": {
        "Wed 08:00": 4,
        "Thu 04:00": 3,
        "Mon 16:00": 7,
        "Fri 08:00": 4,
        "Fri 04:00": 5,
        "Thu 12:00": 3,
        "Mon 08:00": 4,
        "Wed 04:00": 6,
        "Mon 04:00": 2,
        "Tue 16:00": 2,
        "Fri 16:00": 1,
        "Thu 08:00": 4,
        "Tue 08:00": 4,
        "Thu 16:00": 2,
        "Tue 04:00": 5,
        "Mon 12:00": 4,
        "Tue 12:00": 2,
        "Wed 16:00": 2,
        "Wed 12:00": 7,
        "Fri 12:00": 3
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyU04": {
      "session_id": "4ac55781-679a-4d6d-a79a-320f162147b2",
      "n": 79,
      "net": -1075.4610284377702,
      "gross_price": -536.5909418816971,
      "fee": 538.870086556073,
      "PF": 0.7409558002321476,
      "return_pct": -10.754610284377703,
      "DD_engine_pct": -18.079394862500987,
      "hours_open": 11830.066666666668,
      "fraction_time_open": 0.2590223039645005,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.1822818730405191,
      "entry_turnover_initial_equity": 59.90128360888001,
      "roundtrip_turnover_initial_equity": 119.7489081235718,
      "net_bps_entry": -17.953889526974002,
      "net_per_exposure_entry_time_measure": -0.5899988904539663,
      "max_initial_gross_equity": 1.497476325033219,
      "mean_hours": 149.7476793248945,
      "max_hours": 656.4666666666667,
      "stress5_RT_samefills": -1374.8332987466995,
      "stress10_RT_samefills": -1674.2055690556292,
      "net_without_top1": -1413.3304284421129,
      "net_without_top3": -1973.5582185412673,
      "net_without_top5": -2399.374250524468,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 4,
          "net": 301.1891491753476,
          "fee": 26.020701424259823
        },
        "2021": {
          "n": 16,
          "net": -861.8818616427093,
          "fee": 133.93886975555077
        },
        "2022": {
          "n": 19,
          "net": -550.0410616466902,
          "fee": 86.15350279455656
        },
        "2023": {
          "n": 14,
          "net": 241.2840583054148,
          "fee": 105.41329842695956
        },
        "2024": {
          "n": 15,
          "net": -289.9450852269973,
          "fee": 117.30496002695999
        },
        "2025": {
          "n": 11,
          "net": 83.93377259786406,
          "fee": 70.03875412778655
        }
      },
      "entry_order_types": {
        "MARKET": 79
      },
      "exit_order_types": {
        "STOP": 79
      },
      "entry_clock_UTC": {
        "Wed 08:00": 2,
        "Thu 16:00": 5,
        "Mon 08:00": 7,
        "Fri 12:00": 5,
        "Thu 12:00": 5,
        "Tue 04:00": 3,
        "Wed 12:00": 5,
        "Mon 12:00": 2,
        "Tue 16:00": 7,
        "Fri 08:00": 1,
        "Fri 16:00": 5,
        "Mon 16:00": 2,
        "Wed 04:00": 4,
        "Wed 16:00": 1,
        "Tue 12:00": 5,
        "Thu 08:00": 6,
        "Tue 08:00": 4,
        "Mon 04:00": 5,
        "Thu 04:00": 3,
        "Fri 04:00": 2
      },
      "terminal_liquidations": [],
      "engine_open_count_preterminal": 0
    },
    "AttrSpyU05": {
      "session_id": "37c6ae11-78b0-49c6-9b58-4c9190542841",
      "n": 70,
      "net": 75.7426645169086,
      "gross_price": 575.418929804641,
      "fee": 499.6762652877322,
      "PF": 1.0200818630649156,
      "return_pct": 0.7574266451690861,
      "DD_engine_pct": -16.98244814676453,
      "hours_open": 12153.833333333334,
      "fraction_time_open": 0.26611125707946515,
      "entry_notional_time_over_initial_equity_WINDOW_NOT_MTM": 0.2103348483911586,
      "entry_turnover_initial_equity": 55.49081408547999,
      "roundtrip_turnover_initial_equity": 111.03917006394049,
      "net_bps_entry": 1.364958610991577,
      "net_per_exposure_entry_time_measure": 0.03601051613475404,
      "max_initial_gross_equity": 1.3488063080321755,
      "mean_hours": 173.6261904761905,
      "max_hours": 653.7166666666667,
      "stress5_RT_samefills": -201.85526064294223,
      "stress10_RT_samefills": -479.45318580279366,
      "net_without_top1": -305.6646422200623,
      "net_without_top3": -995.5594235388447,
      "net_without_top5": -1506.063599929835,
      "closed_trade_year_cohorts_NOT_MTM": {
        "2020": {
          "n": 2,
          "net": -167.61224639513162,
          "fee": 14.450341180313332
        },
        "2021": {
          "n": 12,
          "net": 841.3276411019285,
          "fee": 97.3064295509638
        },
        "2022": {
          "n": 17,
          "net": -659.5436362726308,
          "fee": 80.59640256868323
        },
        "2023": {
          "n": 14,
          "net": -461.57438645627406,
          "fee": 113.61266328322213
        },
        "2024": {
          "n": 13,
          "net": 84.57493780062475,
          "fee": 110.86948800387205
        },
        "2025": {
          "n": 12,
          "net": 438.570354738392,
          "fee": 82.84094070067756
        }
      },
      "entry_order_types": {
        "MARKET": 70
      },
      "exit_order_types": {
        "STOP": 69,
        "MARKET": 1
      },
      "entry_clock_UTC": {
        "Tue 16:00": 5,
        "Thu 16:00": 3,
        "Tue 04:00": 4,
        "Mon 04:00": 3,
        "Wed 08:00": 5,
        "Mon 08:00": 5,
        "Thu 12:00": 6,
        "Fri 12:00": 5,
        "Wed 12:00": 4,
        "Fri 08:00": 4,
        "Fri 16:00": 2,
        "Wed 04:00": 4,
        "Wed 16:00": 3,
        "Thu 08:00": 2,
        "Fri 04:00": 2,
        "Tue 08:00": 3,
        "Mon 16:00": 3,
        "Thu 04:00": 1,
        "Tue 12:00": 5,
        "Mon 12:00": 1
      },
      "terminal_liquidations": [
        "ff307ef0-67bd-49f6-a80e-c87fe3db7b4e"
      ],
      "engine_open_count_preterminal": 1
    }
  },
  "pairs": {
    "AttrSpyR01__AttrSpyR02": {
      "common_entries": 0,
      "total_a": 11,
      "total_b": 13,
      "only_a": 11,
      "only_b": 13,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyR03": {
      "common_entries": 1,
      "total_a": 11,
      "total_b": 16,
      "only_a": 10,
      "only_b": 15,
      "sum_normalized_net_a": 0.009842178712653901,
      "sum_normalized_net_b": 0.009842178586308184,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyR04": {
      "common_entries": 0,
      "total_a": 11,
      "total_b": 16,
      "only_a": 11,
      "only_b": 16,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyR05": {
      "common_entries": 1,
      "total_a": 11,
      "total_b": 9,
      "only_a": 10,
      "only_b": 8,
      "sum_normalized_net_a": -0.007152537162957247,
      "sum_normalized_net_b": -0.007152537162957122,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyU01": {
      "common_entries": 6,
      "total_a": 11,
      "total_b": 72,
      "only_a": 5,
      "only_b": 66,
      "sum_normalized_net_a": 0.013915932935473463,
      "sum_normalized_net_b": 0.013915946001305989,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyU02": {
      "common_entries": 0,
      "total_a": 11,
      "total_b": 70,
      "only_a": 11,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 11,
      "total_b": 74,
      "only_a": 11,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyU04": {
      "common_entries": 0,
      "total_a": 11,
      "total_b": 79,
      "only_a": 11,
      "only_b": 79,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR01__AttrSpyU05": {
      "common_entries": 1,
      "total_a": 11,
      "total_b": 70,
      "only_a": 10,
      "only_b": 69,
      "sum_normalized_net_a": -0.007152537162957247,
      "sum_normalized_net_b": -0.007152537162957246,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyR03": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 16,
      "only_a": 13,
      "only_b": 16,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyR04": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 16,
      "only_a": 13,
      "only_b": 16,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyR05": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 9,
      "only_a": 13,
      "only_b": 9,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyU01": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 72,
      "only_a": 13,
      "only_b": 72,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyU02": {
      "common_entries": 6,
      "total_a": 13,
      "total_b": 70,
      "only_a": 7,
      "only_b": 64,
      "sum_normalized_net_a": -0.02192013146334294,
      "sum_normalized_net_b": -0.021920131599201052,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 74,
      "only_a": 13,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyU04": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 79,
      "only_a": 13,
      "only_b": 79,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR02__AttrSpyU05": {
      "common_entries": 0,
      "total_a": 13,
      "total_b": 70,
      "only_a": 13,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyR04": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 16,
      "only_a": 16,
      "only_b": 16,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyR05": {
      "common_entries": 1,
      "total_a": 16,
      "total_b": 9,
      "only_a": 15,
      "only_b": 8,
      "sum_normalized_net_a": -0.007115469659218128,
      "sum_normalized_net_b": -0.007115468001038416,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyU01": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 72,
      "only_a": 16,
      "only_b": 72,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyU02": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 70,
      "only_a": 16,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyU03": {
      "common_entries": 14,
      "total_a": 16,
      "total_b": 74,
      "only_a": 2,
      "only_b": 60,
      "sum_normalized_net_a": 0.015460661012382823,
      "sum_normalized_net_b": 0.015460661012382141,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyU04": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 79,
      "only_a": 16,
      "only_b": 79,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR03__AttrSpyU05": {
      "common_entries": 1,
      "total_a": 16,
      "total_b": 70,
      "only_a": 15,
      "only_b": 69,
      "sum_normalized_net_a": -0.007115469659218128,
      "sum_normalized_net_b": -0.007115468001038415,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyR05": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 9,
      "only_a": 16,
      "only_b": 9,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyU01": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 72,
      "only_a": 16,
      "only_b": 72,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyU02": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 70,
      "only_a": 16,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 74,
      "only_a": 16,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyU04": {
      "common_entries": 11,
      "total_a": 16,
      "total_b": 79,
      "only_a": 5,
      "only_b": 68,
      "sum_normalized_net_a": -0.026575140825980385,
      "sum_normalized_net_b": -0.02657518494103918,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR04__AttrSpyU05": {
      "common_entries": 0,
      "total_a": 16,
      "total_b": 70,
      "only_a": 16,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR05__AttrSpyU01": {
      "common_entries": 1,
      "total_a": 9,
      "total_b": 72,
      "only_a": 8,
      "only_b": 71,
      "sum_normalized_net_a": -0.007152537162957122,
      "sum_normalized_net_b": -0.007152537162957246,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR05__AttrSpyU02": {
      "common_entries": 0,
      "total_a": 9,
      "total_b": 70,
      "only_a": 9,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR05__AttrSpyU03": {
      "common_entries": 1,
      "total_a": 9,
      "total_b": 74,
      "only_a": 8,
      "only_b": 73,
      "sum_normalized_net_a": -0.007115468001038416,
      "sum_normalized_net_b": -0.007115469659218258,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR05__AttrSpyU04": {
      "common_entries": 0,
      "total_a": 9,
      "total_b": 79,
      "only_a": 9,
      "only_b": 79,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyR05__AttrSpyU05": {
      "common_entries": 7,
      "total_a": 9,
      "total_b": 70,
      "only_a": 2,
      "only_b": 63,
      "sum_normalized_net_a": 0.02071098215196148,
      "sum_normalized_net_b": 0.020710981362087356,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU01__AttrSpyU02": {
      "common_entries": 3,
      "total_a": 72,
      "total_b": 70,
      "only_a": 69,
      "only_b": 67,
      "sum_normalized_net_a": 0.06129680277293092,
      "sum_normalized_net_b": 0.061416854111175825,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU01__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 72,
      "total_b": 74,
      "only_a": 72,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU01__AttrSpyU04": {
      "common_entries": 3,
      "total_a": 72,
      "total_b": 79,
      "only_a": 69,
      "only_b": 76,
      "sum_normalized_net_a": 0.022301779206960994,
      "sum_normalized_net_b": 0.022158519403743783,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU01__AttrSpyU05": {
      "common_entries": 2,
      "total_a": 72,
      "total_b": 70,
      "only_a": 70,
      "only_b": 68,
      "sum_normalized_net_a": 0.03732706614786045,
      "sum_normalized_net_b": 0.03732706614786032,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU02__AttrSpyU03": {
      "common_entries": 0,
      "total_a": 70,
      "total_b": 74,
      "only_a": 70,
      "only_b": 74,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU02__AttrSpyU04": {
      "common_entries": 0,
      "total_a": 70,
      "total_b": 79,
      "only_a": 70,
      "only_b": 79,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU02__AttrSpyU05": {
      "common_entries": 1,
      "total_a": 70,
      "total_b": 70,
      "only_a": 69,
      "only_b": 69,
      "sum_normalized_net_a": -0.005003368026405423,
      "sum_normalized_net_b": -0.005003368026405559,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU03__AttrSpyU04": {
      "common_entries": 2,
      "total_a": 74,
      "total_b": 79,
      "only_a": 72,
      "only_b": 77,
      "sum_normalized_net_a": -0.030752598160868342,
      "sum_normalized_net_b": -0.030752598160868345,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU03__AttrSpyU05": {
      "common_entries": 4,
      "total_a": 74,
      "total_b": 70,
      "only_a": 70,
      "only_b": 66,
      "sum_normalized_net_a": -0.058576227800371646,
      "sum_normalized_net_b": -0.05857622612057351,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    },
    "AttrSpyU04__AttrSpyU05": {
      "common_entries": 0,
      "total_a": 79,
      "total_b": 70,
      "only_a": 79,
      "only_b": 70,
      "sum_normalized_net_a": 0,
      "sum_normalized_net_b": 0,
      "limitation": "Intersection conditional on endogenous occupancy, not causal."
    }
  }
}
```

Filas completas por par en artefactos pairs_*.json; curva en equity_engine.png. No nueva receta ni promoción.