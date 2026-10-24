# Auditoría numérica completa del calendario PAXG

Job f6e032d499ae4fa1a354d3f9471d6fb7 succeeded / exit 0. Snapshots completos: 37 trades weekend y 162 weekday. Las cohortes por año de cierre NO son rentabilidad anual MTM. La curva del motor se muestrea a las 00:01 UTC salvo fronteras.

```json
{
  "weekend": {
    "session_id": "2da06c02-d246-43a0-b265-8837aa9c4be5",
    "trades": 37,
    "net": 400.2243628684158,
    "fees": 259.1256715182893,
    "before_fees": 659.3500343867051,
    "pf_net": 1.5072644677252123,
    "annual_return_engine": 0.7555162665411785,
    "dd_engine": -2.06221309007516,
    "sharpe_engine": 0.42992675556129295,
    "directions": {
      "short": {
        "n": 26,
        "net": 487.2472754749277,
        "wins": 18
      },
      "long": {
        "n": 11,
        "net": -87.02291260651188,
        "wins": 5
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 1,
        "net": 84.73908699299996
      },
      "2021": {
        "n": 7,
        "net": 12.89340612638722
      },
      "2022": {
        "n": 8,
        "net": 337.41607281500035
      },
      "2023": {
        "n": 10,
        "net": -43.72986978672829
      },
      "2024": {
        "n": 7,
        "net": 6.893209608487602
      },
      "2025": {
        "n": 4,
        "net": 2.0124571122689474
      }
    },
    "entry_notional_sum": 288249.445395,
    "net_bps_over_entry_notional": 13.88465335362474,
    "gross_bps_over_entry_notional": 22.87428631417385,
    "extra_roundtrip_5bps_static_samefills": 256.0996401709158,
    "extra_roundtrip_10bps_static_samefills": 111.97491747341581,
    "top3_winners_net": 297.3027657460501,
    "top3_share_of_net": 0.742840249941996,
    "net_ex_top3_descriptive": 102.92159712236571,
    "total_holding_hours": 459.46666666666675,
    "time_exposure_pct": 1.0060138961873066,
    "mean_hold_hours": 12.41801801801802,
    "median_hold_hours": 10.15,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.1940217806810443,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.3358203432289883e-12,
      "max_qty_error": 0.0,
      "wallet_delta": -1.8189894035458565e-12,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 12
      },
      "ordertypes": {
        "entry_MARKET": 37,
        "exit_LIMIT": 19,
        "exit_STOP": 6,
        "exit_MARKET": 12
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000.0,
      "value": 10000.0,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200.0,
      "value": 10400.224362868414,
      "color": "#818CF8",
      "dt": "2025-12-31 00:00:00+00:00"
    },
    "equity_clock_counts": {
      "00:00:00": 2,
      "00:01:00": 1902
    }
  },
  "weekday": {
    "session_id": "3855e023-3d66-4aff-8a13-fbb3110a3255",
    "trades": 162,
    "net": -1245.2758516734245,
    "fees": 1126.1571557605764,
    "before_fees": -119.11869591284812,
    "pf_net": 0.7134625710855745,
    "annual_return_engine": -2.518553382112554,
    "dd_engine": -13.039258944959354,
    "sharpe_engine": -0.7241776081663184,
    "directions": {
      "short": {
        "n": 97,
        "net": -769.1029398675438,
        "wins": 51
      },
      "long": {
        "n": 65,
        "net": -476.1729118058811,
        "wins": 32
      }
    },
    "closed_year_cohorts_not_MTM": {
      "2020": {
        "n": 7,
        "net": -102.71860384954044
      },
      "2021": {
        "n": 23,
        "net": -214.14977043128445
      },
      "2022": {
        "n": 29,
        "net": -363.65233175528573
      },
      "2023": {
        "n": 35,
        "net": -103.18782708453551
      },
      "2024": {
        "n": 30,
        "net": 129.66009465761763
      },
      "2025": {
        "n": 38,
        "net": -591.2274132103959
      }
    },
    "entry_notional_sum": 1251269.3022780002,
    "net_bps_over_entry_notional": -9.952101033776946,
    "gross_bps_over_entry_notional": -0.9519828840680932,
    "extra_roundtrip_5bps_static_samefills": -1870.9105028124245,
    "extra_roundtrip_10bps_static_samefills": -2496.5451539514247,
    "top3_winners_net": 417.1757396547516,
    "top3_share_of_net": null,
    "net_ex_top3_descriptive": -1662.4515913281762,
    "total_holding_hours": 3259.3999999999996,
    "time_exposure_pct": 7.136538798388509,
    "mean_hold_hours": 20.119753086419752,
    "median_hold_hours": 24.0,
    "max_hold_hours": 24.0,
    "max_entry_notional_over_preentry_wallet": 1.518315923951777,
    "terminal": [],
    "audit": {
      "max_fee_error": 1.7763568394002505e-15,
      "max_gross_error": 1.3855583347321954e-12,
      "max_qty_error": 0.0,
      "wallet_delta": -1.6370904631912708e-11,
      "overlaps": 0,
      "expiry_violations": [],
      "market_expiry_clocks": {
        "24.0": 93
      },
      "ordertypes": {
        "entry_MARKET": 162,
        "exit_LIMIT": 28,
        "exit_MARKET": 93,
        "exit_STOP": 41
      }
    },
    "equity_points": 1904,
    "equity_first": {
      "time": 1602720000.0,
      "value": 10000.0,
      "color": "#818CF8",
      "dt": "2020-10-15 00:00:00+00:00"
    },
    "equity_last": {
      "time": 1767139200.0,
      "value": 8754.724148326592,
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
