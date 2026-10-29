# X03 R3 — cierre verificado

Ronda completada. N204 congelada para investigación, gestión PAXG original, sin promoción. Objetivo mensual no alcanzado.2026 cerrado. No quedan ejecuciones ni análisis en marcha; el único job fallido fue el harness de metadatos, reparado y revisado antes del estrés.

```json
{
  "completed": true,
  "new_backtests": 8,
  "reused_references": 8,
  "finished_contexts": 16,
  "snapshots_checked": 48,
  "nominal_parity_pairs": 4,
  "nominal_parity_max_trade_PNL_delta": 0,
  "source_checks": {
    "unchanged": [
      "BtcExploreR103",
      "PortComparePaxgMarket4h",
      "PortCompareSpySecond4h",
      "PortCompareSpyMarket4h",
      "PortCompareBtc4h",
      "X03ExploreR204",
      "X03ExecPaxgFixedBeR301"
    ],
    "count": 7
  },
  "selection": {
    "btc": "X03ExploreR204",
    "label": "N204",
    "role": "Frozen BTC candidate for future reserved-sample protocol; research only",
    "paxg_official": "PortComparePaxgMarket4h",
    "paxg_counterfactual": "X03ExecPaxgFixedBeR301",
    "counterfactual_adopted": false,
    "control_btc": "BtcExploreR103",
    "conditions": [
      {
        "portfolio": "B",
        "delta_official_fee70": 923.1638021738054,
        "delta_fixedBE_fee70": 955.6636908152759,
        "dd_official": -9.026628677513893,
        "dd_fixed": -9.027061799521373,
        "positive_delta_both": true
      },
      {
        "portfolio": "C",
        "delta_official_fee70": 988.0682713267361,
        "delta_fixedBE_fee70": 1062.5422341235026,
        "dd_official": -9.071459738684062,
        "dd_fixed": -9.073366848682463,
        "positive_delta_both": true
      }
    ],
    "nominal_parity": "4/4 exact executed economics; max per-trade PNL difference0",
    "parity_job": "6f2bfdbdc05c46d49c5c623793a8c444",
    "regularity_goal_met": false,
    "promoted": false,
    "closed_2026": true,
    "source_checks": {
      "unchanged": [
        "BtcExploreR103",
        "PortComparePaxgMarket4h",
        "PortCompareSpySecond4h",
        "PortCompareSpyMarket4h",
        "PortCompareBtc4h",
        "X03ExploreR204",
        "X03ExecPaxgFixedBeR301"
      ],
      "count": 7
    }
  },
  "analysis_jobs": [
    {
      "id": "95e8c3a15693464ba32b9591cd1bd3ce",
      "status": "succeeded"
    },
    {
      "id": "8adb99e2ca9d426999e00867213a1f7a",
      "status": "succeeded"
    },
    {
      "id": "49ca6c739a97403a82ab2c47e48d780f",
      "status": "succeeded"
    },
    {
      "id": "34df7f0acd764f53b30e1a7a644daf0c",
      "status": "succeeded"
    },
    {
      "id": "ae9a7ce44fa747528a8f8d9af569b662",
      "status": "succeeded"
    },
    {
      "id": "7177d5dec4b644b8a9c8be934f142cfd",
      "status": "succeeded"
    },
    {
      "id": "55146e3217cc48ddb080d4186dcc11d1",
      "status": "succeeded"
    },
    {
      "id": "75de1c39efa54164a2fe2b7840d130dd",
      "status": "failed"
    },
    {
      "id": "6f2bfdbdc05c46d49c5c623793a8c444",
      "status": "succeeded"
    },
    {
      "id": "b7aee9a90c834d05ba7c5015ff39755d",
      "status": "succeeded"
    },
    {
      "id": "b2d5bd2e153a4d4389a465360fbef55a",
      "status": "succeeded"
    },
    {
      "id": "411aff846d8644a6ac5fdb613ebadc88",
      "status": "succeeded"
    },
    {
      "id": "e59c586237944330917483c5429ccedd",
      "status": "succeeded"
    }
  ],
  "pending_backtests": [],
  "pending_analysis_jobs": [],
  "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_RESULTS_20261019.md",
  "handoff": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_HANDOFF_20261019.md",
  "independent_final_review": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_INDEPENDENT_FINAL_REVIEW_20261019.md",
  "reserved_2026_closed": true
}
```