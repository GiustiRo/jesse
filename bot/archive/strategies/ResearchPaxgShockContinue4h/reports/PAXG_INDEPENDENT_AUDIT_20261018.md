# Audit snapshot numeric results

Complete snapshots job aa21b5ab23ab40449bd367ed22386bfc succeeded/exit0. All235+245+35trades. Dates2020-10-15→2025-12-31exclusive. Full numeric results below; engine equity has1902daily00:01samples and2boundary00:00samples, not closingUTCcalendar. Closed-year cohorts are NOT annualMTM.

```json
{
  "continue": {
    "session_id": "73464795-1e47-4f0a-9239-fd8901775dc2",
    "trades": 235,
    "net": -2140.1880400355662,
    "fees": 1632.3561983992379,
    "before_fees": -507.83184163632836,
    "pf_net": 0.7704599075110479,
    "annual_return_engine": -4.513978453921497,
    "dd_engine": -30.658134961248663,
    "sharpe_engine": -0.6826570772887673,
    "directions": {
      "short": {
        "n": 115,
        "net": -1304.2398179969375,
        "wins": 45
      },
      "long": {
        "n": 120,
        "net": -835.9482220386295,
        "wins": 54
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 7,
        "net": -166.41618299112187
      },
      "2021": {
        "n": 28,
        "net": 26.769606902099305
      },
      "2022": {
        "n": 51,
        "net": 146.2183057582952
      },
      "2023": {
        "n": 54,
        "net": -789.6962420811647
      },
      "2024": {
        "n": 27,
        "net": -820.2935328830331
      },
      "2025": {
        "n": 68,
        "net": -536.7699947406409
      }
    },
    "entry_notional_sum": 1813446.024658,
    "net_bps_over_entry_notional": -11.801774141246838,
    "gross_bps_over_entry_notional": -2.800369212709824,
    "extra_roundtrip_5bps_static_samefills": -3046.9110523645663,
    "extra_roundtrip_10bps_static_samefills": -3953.6340646935664,
    "top3_winners_net": 740.1235562952492,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -2880.3115963308155,
    "total_holding_hours": 8388.350000000004,
    "time_exposure_pct": 18.366504641793668,
    "mean_hold_hours": 35.69510638297872,
    "median_hold_hours": 48,
    "max_hold_hours": 48,
    "max_entry_notional_over_preentry_wallet": 1.570672528895789,
    "terminal": [
      {
        "type": "short",
        "net": 204.07879318860063,
        "gross": 210.46366800000064,
        "hours": 40,
        "exit_types": [
          "MARKET"
        ]
      }
    ],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.5631940186722204e-12,
      "max_qty_error": 0,
      "wallet_delta": 3.9108272176235914e-11,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "48.0": 132
      },
      "ordertypes": {
        "entry_MARKET": 235,
        "exit_STOP": 102,
        "exit_MARKET": 133
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000,
      "value": 10000,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200,
      "value": 7859.811959964411,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "reverse": {
    "session_id": "aca7b3b8-3781-4986-8ed6-0ede625ba31c",
    "trades": 245,
    "net": -2398.951177283584,
    "fees": 1613.203342579143,
    "before_fees": -785.747834704441,
    "pf_net": 0.7427065305341316,
    "annual_return_engine": -5.125116945821107,
    "dd_engine": -26.464512036293865,
    "sharpe_engine": -0.7836127316354822,
    "directions": {
      "long": {
        "n": 114,
        "net": -879.3975992231709,
        "wins": 52
      },
      "short": {
        "n": 131,
        "net": -1519.553578060413,
        "wins": 46
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 7,
        "net": 198.90650594087683
      },
      "2021": {
        "n": 27,
        "net": -358.8540523013624
      },
      "2022": {
        "n": 56,
        "net": -1403.2175198131717
      },
      "2023": {
        "n": 54,
        "net": -476.0295512995066
      },
      "2024": {
        "n": 29,
        "net": -270.3896408781385
      },
      "2025": {
        "n": 72,
        "net": -89.36691893228156
      }
    },
    "entry_notional_sum": 1792212.2358020002,
    "net_bps_over_entry_notional": -13.385419033310377,
    "gross_bps_over_entry_notional": -4.3842342943988735,
    "extra_roundtrip_5bps_static_samefills": -3295.0572951845843,
    "extra_roundtrip_10bps_static_samefills": -4191.163413085584,
    "top3_winners_net": 786.4754254299993,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -3185.426602713583,
    "total_holding_hours": 8653.116666666669,
    "time_exposure_pct": 18.94621795994629,
    "mean_hold_hours": 35.31884353741496,
    "median_hold_hours": 48,
    "max_hold_hours": 48,
    "max_entry_notional_over_preentry_wallet": 1.5696868928145145,
    "terminal": [
      {
        "type": "long",
        "net": 13.027247246000192,
        "gross": 18.171920000000192,
        "hours": 32,
        "exit_types": [
          "MARKET"
        ]
      }
    ],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.2363443602225743e-12,
      "max_qty_error": 0,
      "wallet_delta": -2.7284841053187847e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "48.0": 137
      },
      "ordertypes": {
        "entry_MARKET": 245,
        "exit_MARKET": 138,
        "exit_STOP": 107
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000,
      "value": 10000,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200,
      "value": 7601.048822716411,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "control": {
    "session_id": "93a16137-e819-41a3-b325-0631a6627a6c",
    "trades": 35,
    "net": 546.1105723537391,
    "fees": 246.60888105483386,
    "before_fees": 792.719453408573,
    "pf_net": 1.308334734611165,
    "annual_return_engine": 1.0250706618597727,
    "dd_engine": -6.919378335744097,
    "sharpe_engine": 0.23075746266424707,
    "directions": {
      "long": {
        "n": 35,
        "net": 546.1105723537391,
        "wins": 14
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2021": {
        "n": 6,
        "net": -203.7127948722217
      },
      "2022": {
        "n": 3,
        "net": -87.13692885508894
      },
      "2023": {
        "n": 5,
        "net": -55.78962675646495
      },
      "2024": {
        "n": 7,
        "net": 495.49747740212723
      },
      "2025": {
        "n": 14,
        "net": 397.25244543538753
      }
    },
    "entry_notional_sum": 273613.508112,
    "net_bps_over_entry_notional": 19.95919631753693,
    "gross_bps_over_entry_notional": 28.972233822757172,
    "extra_roundtrip_5bps_static_samefills": 409.3038182977391,
    "extra_roundtrip_10bps_static_samefills": 272.4970642417391,
    "top3_winners_net": 1466.657905102516,
    "top3_share_of_net": 2.6856427605516107,
    "net_ex_top3_descriptive": -920.5473327487769,
    "total_holding_hours": 6100.466666666668,
    "time_exposure_pct": 13.357126175045252,
    "mean_hold_hours": 174.29904761904763,
    "median_hold_hours": 98.4,
    "max_hold_hours": 916.75,
    "max_entry_notional_over_preentry_wallet": 1.2221115609877231,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.0516032489249483e-12,
      "max_qty_error": 0,
      "wallet_delta": 3.637978807091713e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {},
      "ordertypes": {
        "entry_LIMIT": 35,
        "exit_STOP": 35
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000,
      "value": 10000,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200,
      "value": 10546.110572353738,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  }
}
```
