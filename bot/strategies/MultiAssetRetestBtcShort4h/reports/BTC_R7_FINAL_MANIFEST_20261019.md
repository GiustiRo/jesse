# BTC R7 — registro, fuentes y resultados finales

Los14backtestsnominales estánterminados. No se activaron6fullscondicionalesporausenciadeelegible. 24fuentesexactas,14formulariosy42snapshots. Sinborrados niarchivado; todalaevidenciaconservada. Fuentes nuevas completas en BTC_R7_SOURCE_QA_20261019.md y snapshots; fuentes antiguas siguen en sus carpetas. Este manifiesto es trazabilidad, no prueba antisobreajuste.

- [O700B](http://localhost:9200/#/backtest/8d6837b4-51a5-4128-91f8-a8c7608c5e74) — N503ObserveR700; semilla N503
- [O700C](http://localhost:9200/#/backtest/8210a2a5-1376-457d-b096-1baccacd5d1a) — N503ObserveR700; semilla N503
- [S701B](http://localhost:9200/#/backtest/a05b76ab-842f-428e-ba54-4099070ecea5) — N503ManageR701; semilla N503
- [S701C](http://localhost:9200/#/backtest/ca2c6fea-b723-4308-ba85-199535fde594) — N503ManageR701; semilla N503
- [S702B](http://localhost:9200/#/backtest/3b464cbf-426f-4197-9646-834a8117c943) — N503ManageR702; semilla N503
- [S702C](http://localhost:9200/#/backtest/9ff8c173-f3fa-459d-b467-092ec3c4924e) — N503ManageR702; semilla N503
- [S703B](http://localhost:9200/#/backtest/576a3b11-dc73-46ea-938b-02088406ad52) — N503ManageR703; semilla N503
- [S703C](http://localhost:9200/#/backtest/04acc6c2-7fb2-4e55-b4d6-7aab52722b74) — N503ManageR703; semilla N503
- [S704B](http://localhost:9200/#/backtest/f005ba80-5b39-42f8-9ab5-97fb5568f07c) — N503ManageR704; semilla N503
- [S704C](http://localhost:9200/#/backtest/2d941297-ac9f-4196-ac3b-3066298d6a5d) — N503ManageR704; semilla N503
- [S705B](http://localhost:9200/#/backtest/789d5a10-e2cc-468c-8f76-f20fba9277aa) — N204ManageR705; semilla N204
- [S705C](http://localhost:9200/#/backtest/aedc08d8-2ad7-4c62-8186-a777fe32ae25) — N204ManageR705; semilla N204
- [S706B](http://localhost:9200/#/backtest/de7e68d4-3adb-4afe-9c62-ecb7496877a1) — N204ManageR706; semilla N204
- [S706C](http://localhost:9200/#/backtest/f407f8a8-15b4-41cb-b756-46ced2f041b4) — N204ManageR706; semilla N204

```json
{
  "scope": "R7 14 nominal fulls; no conditional extra run; no deletion/archival; 2026 closed",
  "registry": [
    {
      "name": "O700B",
      "id": "8d6837b4-51a5-4128-91f8-a8c7608c5e74",
      "url": "http://localhost:9200/#/backtest/8d6837b4-51a5-4128-91f8-a8c7608c5e74",
      "strategy": "N503ObserveR700",
      "portfolio": "B",
      "seed": "N503",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 106.85,
      "net_profit": 13328.711712815926,
      "total_trades": 264,
      "error": null
    },
    {
      "name": "O700C",
      "id": "8210a2a5-1376-457d-b096-1baccacd5d1a",
      "url": "http://localhost:9200/#/backtest/8210a2a5-1376-457d-b096-1baccacd5d1a",
      "strategy": "N503ObserveR700",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 106.92,
      "net_profit": 13536.902513059398,
      "total_trades": 271,
      "error": null
    },
    {
      "name": "S701B",
      "id": "a05b76ab-842f-428e-ba54-4099070ecea5",
      "url": "http://localhost:9200/#/backtest/a05b76ab-842f-428e-ba54-4099070ecea5",
      "strategy": "N503ManageR701",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 103.05,
      "net_profit": 13347.964134693448,
      "total_trades": 266,
      "error": null
    },
    {
      "name": "S701C",
      "id": "ca2c6fea-b723-4308-ba85-199535fde594",
      "url": "http://localhost:9200/#/backtest/ca2c6fea-b723-4308-ba85-199535fde594",
      "strategy": "N503ManageR701",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 103.7,
      "net_profit": 13562.21514306048,
      "total_trades": 273,
      "error": null
    },
    {
      "name": "S702B",
      "id": "3b464cbf-426f-4197-9646-834a8117c943",
      "url": "http://localhost:9200/#/backtest/3b464cbf-426f-4197-9646-834a8117c943",
      "strategy": "N503ManageR702",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 102.32,
      "net_profit": 12458.517359615034,
      "total_trades": 265,
      "error": null
    },
    {
      "name": "S702C",
      "id": "9ff8c173-f3fa-459d-b467-092ec3c4924e",
      "url": "http://localhost:9200/#/backtest/9ff8c173-f3fa-459d-b467-092ec3c4924e",
      "strategy": "N503ManageR702",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 102.65,
      "net_profit": 12667.16850214585,
      "total_trades": 272,
      "error": null
    },
    {
      "name": "S703B",
      "id": "576a3b11-dc73-46ea-938b-02088406ad52",
      "url": "http://localhost:9200/#/backtest/576a3b11-dc73-46ea-938b-02088406ad52",
      "strategy": "N503ManageR703",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 104.65,
      "net_profit": 11840.239043329428,
      "total_trades": 265,
      "error": null
    },
    {
      "name": "S703C",
      "id": "04acc6c2-7fb2-4e55-b4d6-7aab52722b74",
      "url": "http://localhost:9200/#/backtest/04acc6c2-7fb2-4e55-b4d6-7aab52722b74",
      "strategy": "N503ManageR703",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 105.04,
      "net_profit": 12033.135279112625,
      "total_trades": 272,
      "error": null
    },
    {
      "name": "S704B",
      "id": "f005ba80-5b39-42f8-9ab5-97fb5568f07c",
      "url": "http://localhost:9200/#/backtest/f005ba80-5b39-42f8-9ab5-97fb5568f07c",
      "strategy": "N503ManageR704",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 103.3,
      "net_profit": 12143.856484375287,
      "total_trades": 273,
      "error": null
    },
    {
      "name": "S704C",
      "id": "2d941297-ac9f-4196-ac3b-3066298d6a5d",
      "url": "http://localhost:9200/#/backtest/2d941297-ac9f-4196-ac3b-3066298d6a5d",
      "strategy": "N503ManageR704",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 103.69,
      "net_profit": 12310.794248954555,
      "total_trades": 280,
      "error": null
    },
    {
      "name": "S705B",
      "id": "789d5a10-e2cc-468c-8f76-f20fba9277aa",
      "url": "http://localhost:9200/#/backtest/789d5a10-e2cc-468c-8f76-f20fba9277aa",
      "strategy": "N204ManageR705",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 105.82,
      "net_profit": 11831.980545599985,
      "total_trades": 275,
      "error": null
    },
    {
      "name": "S705C",
      "id": "aedc08d8-2ad7-4c62-8186-a777fe32ae25",
      "url": "http://localhost:9200/#/backtest/aedc08d8-2ad7-4c62-8186-a777fe32ae25",
      "strategy": "N204ManageR705",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 105.98,
      "net_profit": 12026.165560964964,
      "total_trades": 282,
      "error": null
    },
    {
      "name": "S706B",
      "id": "de7e68d4-3adb-4afe-9c62-ecb7496877a1",
      "url": "http://localhost:9200/#/backtest/de7e68d4-3adb-4afe-9c62-ecb7496877a1",
      "strategy": "N204ManageR706",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 104.72,
      "net_profit": 11521.155997335092,
      "total_trades": 275,
      "error": null
    },
    {
      "name": "S706C",
      "id": "f407f8a8-15b4-41cb-b756-46ced2f041b4",
      "url": "http://localhost:9200/#/backtest/f407f8a8-15b4-41cb-b756-46ced2f041b4",
      "strategy": "N204ManageR706",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished",
      "execution_duration_seconds": 104.96,
      "net_profit": 11716.483213907977,
      "total_trades": 282,
      "error": null
    }
  ],
  "source_QA": {
    "status": "PASS",
    "checks": [
      "N503ManageR701_profit_positive",
      "N503ManageR701_profit_negative",
      "N503ManageR701_profit_zero_fee_boundary",
      "N503ManageR701_invalid_no_exit",
      "N503ManageR701_arms_no_exit",
      "N503ManageR701_shadow_next_profit_exit",
      "N503ManageR701_idempotent",
      "N503ManageR701_no_loss_exit",
      "N503ManageR701_shadow_expired",
      "N503ManageR701_no_order_calls_in_release",
      "N503ManageR702_profit_positive",
      "N503ManageR702_profit_negative",
      "N503ManageR702_profit_zero_fee_boundary",
      "N503ManageR702_invalid_no_exit",
      "N503ManageR702_one_full_bar_no_exit",
      "N503ManageR702_adverse_break_profit_exit",
      "N503ManageR702_no_adverse_break",
      "N503ManageR702_no_loss_exit",
      "N503ManageR702_idempotent",
      "N503ManageR702_no_order_calls_in_release",
      "N503ManageR703_profit_positive",
      "N503ManageR703_profit_negative",
      "N503ManageR703_profit_zero_fee_boundary",
      "N503ManageR703_invalid_no_exit",
      "N503ManageR703_new_best_no_exit",
      "N503ManageR703_half_equal_exit",
      "N503ManageR703_less_half_no_exit",
      "N503ManageR703_no_loss_exit",
      "N503ManageR703_no_progress_no_exit",
      "N503ManageR703_idempotent",
      "N503ManageR703_no_order_calls_in_release",
      "N503ManageR704_profit_positive",
      "N503ManageR704_profit_negative",
      "N503ManageR704_profit_zero_fee_boundary",
      "N503ManageR704_invalid_no_exit",
      "N503ManageR704_ready_profit_exit",
      "N503ManageR704_notready_no_exit",
      "N503ManageR704_ready_loss_no_exit",
      "N503ManageR704_no_order_calls_in_release",
      "N204ManageR705_profit_positive",
      "N204ManageR705_profit_negative",
      "N204ManageR705_profit_zero_fee_boundary",
      "N204ManageR705_invalid_no_exit",
      "N204ManageR705_one_full_bar_no_exit",
      "N204ManageR705_adverse_break_profit_exit",
      "N204ManageR705_no_adverse_break",
      "N204ManageR705_no_loss_exit",
      "N204ManageR705_idempotent",
      "N204ManageR705_no_order_calls_in_release",
      "N204ManageR706_profit_positive",
      "N204ManageR706_profit_negative",
      "N204ManageR706_profit_zero_fee_boundary",
      "N204ManageR706_invalid_no_exit",
      "N204ManageR706_new_best_no_exit",
      "N204ManageR706_half_equal_exit",
      "N204ManageR706_less_half_no_exit",
      "N204ManageR706_no_loss_exit",
      "N204ManageR706_no_progress_no_exit",
      "N204ManageR706_idempotent",
      "N204ManageR706_no_order_calls_in_release",
      "N503ObserveR700_no_order_calls_in_observer"
    ],
    "count": 61,
    "scope": "Inline syntax and pure exit-helper fixtures, not an engine lifecycle test"
  },
  "source_reviews": [
    {
      "name": "N503ManageR701",
      "seed": "N503",
      "protected": 22,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N503ManageR702",
      "seed": "N503",
      "protected": 22,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N503ManageR703",
      "seed": "N503",
      "protected": 22,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N503ManageR704",
      "seed": "N503",
      "protected": 22,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N204ManageR705",
      "seed": "N204",
      "protected": 21,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N204ManageR706",
      "seed": "N204",
      "protected": 21,
      "original_exit": true,
      "entry_unchanged_except_label": true
    },
    {
      "name": "N503ObserveR700",
      "seed": "N503",
      "protected": 22,
      "original_exit": true,
      "entry_unchanged_except_label": true
    }
  ],
  "sources_exact": [
    {
      "name": "BtcExploreR103",
      "exact": true,
      "chars": 21361
    },
    {
      "name": "PortComparePaxgMarket4h",
      "exact": true,
      "chars": 16178
    },
    {
      "name": "PortCompareSpySecond4h",
      "exact": true,
      "chars": 19930
    },
    {
      "name": "PortCompareSpyMarket4h",
      "exact": true,
      "chars": 20101
    },
    {
      "name": "PortCompareBtc4h",
      "exact": true,
      "chars": 15447
    },
    {
      "name": "X03ExploreR204",
      "exact": true,
      "chars": 21582
    },
    {
      "name": "N204ExploreR503",
      "exact": true,
      "chars": 22182
    },
    {
      "name": "N503ExploreR601",
      "exact": true,
      "chars": 22492
    },
    {
      "name": "N503ExploreR602",
      "exact": true,
      "chars": 22644
    },
    {
      "name": "N503ExploreR603",
      "exact": true,
      "chars": 22469
    },
    {
      "name": "N503ExploreR604",
      "exact": true,
      "chars": 22679
    },
    {
      "name": "N503ExploreR605",
      "exact": true,
      "chars": 24147
    },
    {
      "name": "N503CapacityR601",
      "exact": true,
      "chars": 24511
    },
    {
      "name": "N503CapacityR602",
      "exact": true,
      "chars": 24717
    },
    {
      "name": "N503CapacityR603",
      "exact": true,
      "chars": 24908
    },
    {
      "name": "N503CapacityR604",
      "exact": true,
      "chars": 25412
    },
    {
      "name": "N503CapacityR605",
      "exact": true,
      "chars": 25230
    },
    {
      "name": "N503ManageR701",
      "exact": true,
      "chars": 26071
    },
    {
      "name": "N503ManageR702",
      "exact": true,
      "chars": 25731
    },
    {
      "name": "N503ManageR703",
      "exact": true,
      "chars": 25886
    },
    {
      "name": "N503ManageR704",
      "exact": true,
      "chars": 25748
    },
    {
      "name": "N204ManageR705",
      "exact": true,
      "chars": 25132
    },
    {
      "name": "N204ManageR706",
      "exact": true,
      "chars": 25287
    },
    {
      "name": "N503ObserveR700",
      "exact": true,
      "chars": 25970
    }
  ],
  "forms": {
    "8d6837b4-51a5-4128-91f8-a8c7608c5e74": {
      "name": "O700B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "8210a2a5-1376-457d-b096-1baccacd5d1a": {
      "name": "O700C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "a05b76ab-842f-428e-ba54-4099070ecea5": {
      "name": "S701B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "ca2c6fea-b723-4308-ba85-199535fde594": {
      "name": "S701C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "3b464cbf-426f-4197-9646-834a8117c943": {
      "name": "S702B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "9ff8c173-f3fa-459d-b467-092ec3c4924e": {
      "name": "S702C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "576a3b11-dc73-46ea-938b-02088406ad52": {
      "name": "S703B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "04acc6c2-7fb2-4e55-b4d6-7aab52722b74": {
      "name": "S703C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "f005ba80-5b39-42f8-9ab5-97fb5568f07c": {
      "name": "S704B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "2d941297-ac9f-4196-ac3b-3066298d6a5d": {
      "name": "S704C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "789d5a10-e2cc-468c-8f76-f20fba9277aa": {
      "name": "S705B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "aedc08d8-2ad7-4c62-8186-a777fe32ae25": {
      "name": "S705C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "de7e68d4-3adb-4afe-9c62-ecb7496877a1": {
      "name": "S706B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "f407f8a8-15b4-41cb-b756-46ced2f041b4": {
      "name": "S706C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    }
  },
  "jobs": [
    {
      "batch": "O700",
      "names": [
        "O700B",
        "O700C"
      ],
      "job": "2828afd143ca4bb79d8b624c4130b87d",
      "status": "succeeded"
    },
    {
      "batch": "S701",
      "names": [
        "S701B",
        "S701C"
      ],
      "job": "d5b0c8890a9c45b19a1b71d3010fcf04",
      "status": "succeeded"
    },
    {
      "batch": "S702",
      "names": [
        "S702B",
        "S702C"
      ],
      "job": "b10507616e3142e0b0d06d50d65f202c",
      "status": "succeeded"
    },
    {
      "batch": "S703",
      "names": [
        "S703B",
        "S703C"
      ],
      "job": "7ce1ea514cb249eabab5f7634b912d90",
      "status": "succeeded"
    },
    {
      "batch": "S704",
      "names": [
        "S704B",
        "S704C"
      ],
      "job": "f0c08a6f63b344dd86ae7542f0f71972",
      "status": "succeeded"
    },
    {
      "batch": "S705",
      "names": [
        "S705B",
        "S705C"
      ],
      "job": "01ba1d1c1b2c4bf1a94a5e955e1dfff9",
      "status": "succeeded"
    },
    {
      "batch": "S706",
      "names": [
        "S706B",
        "S706C"
      ],
      "job": "8956402d2d7b429c88936f51e364dc5d",
      "status": "succeeded"
    }
  ],
  "paths": {
    "O700B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 260,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 39.324442829776444,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 264,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    },
    "O700C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 267,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 39.32444282977622,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 271,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 0
    },
    "S701B": {
      "counts": {
        "current": 266,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 256,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": true,
        "matched": 266,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 4
    },
    "S701C": {
      "counts": {
        "current": 273,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 263,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": true,
        "matched": 273,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 4
    },
    "S702B": {
      "counts": {
        "current": 265,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 239,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 21
    },
    "S702C": {
      "counts": {
        "current": 272,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 246,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 21
    },
    "S703B": {
      "counts": {
        "current": 265,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 236,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 24
    },
    "S703C": {
      "counts": {
        "current": 272,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 243,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 24
    },
    "S704B": {
      "counts": {
        "current": 273,
        "reference": 273,
        "retained": 258,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 245,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 258,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 262,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 263,
        "max_abs_economic_field_delta": 4019,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": true,
        "matched": 273,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 13
    },
    "S704C": {
      "counts": {
        "current": 280,
        "reference": 280,
        "retained": 265,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 265,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 269,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 270,
        "max_abs_economic_field_delta": 4019,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": true,
        "matched": 280,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 13
    },
    "S705B": {
      "counts": {
        "current": 275,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 248,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 261,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 25
    },
    "S705C": {
      "counts": {
        "current": 282,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 255,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 268,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 25
    },
    "S706B": {
      "counts": {
        "current": 275,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 245,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 273,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 261,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 28
    },
    "S706C": {
      "counts": {
        "current": 282,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 280,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P604": {
        "economic_identity_within_1e_7": false,
        "matched": 268,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_P603": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 4860.737599826942,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "modified_same_entry_exits": 28
    }
  },
  "rank": {
    "matrix": [
      {
        "id": "S701",
        "strategy": "N503ManageR701",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13347.964134693444,
            "delta": 291.3492196157804,
            "delta_seed": 19.25242187751428,
            "plus10": 11232.89487257444,
            "delta10": 301.68512902857583,
            "dd": -8.781604713439906,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 4,
            "annual_delta_MTM": {
              "2021": -89.89581828555129,
              "2022": 83.56662068032529,
              "2023": 399.37641561559394,
              "2024": 119.78760090854121,
              "2025": -221.4855993031124
            },
            "positive_years": 3,
            "best_incremental_month": 159.5974587743549,
            "delta_without_best_month": 131.7517608414255,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_exits": false,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13562.215143060492,
            "delta": 322.77276321369936,
            "delta_seed": 25.31263000108629,
            "plus10": 11332.481937376444,
            "delta10": 329.0664729960572,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 4,
            "annual_delta_MTM": {
              "2021": -79.83235145539038,
              "2022": 83.3418325769635,
              "2023": 413.45286298768224,
              "2024": 121.46865986613193,
              "2025": -215.65824076171702
            },
            "positive_years": 3,
            "best_incremental_month": 155.91302490877388,
            "delta_without_best_month": 166.8597383049255,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true,
              "modified_exits": false,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": 301.68512902857583,
        "worstDD": -9.054184091363382
      },
      {
        "id": "S702",
        "strategy": "N503ManageR702",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12458.517359615034,
            "delta": -598.0975554626293,
            "delta_seed": -870.1943532008954,
            "plus10": 10382.252116941965,
            "delta10": -548.9576266038985,
            "dd": -8.220162236587413,
            "counts": {
              "Mfull": "39/61",
              "Mall": "39/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.030952380952380953,
            "modified_exits": 21,
            "annual_delta_MTM": {
              "2021": 14.876838153766585,
              "2022": -237.65388183369396,
              "2023": 325.1581525127567,
              "2024": 106.75941197951033,
              "2025": -807.2380762749417
            },
            "positive_years": 3,
            "best_incremental_month": 212.0633257199479,
            "delta_without_best_month": -810.1608811825772,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": true,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12667.168502145854,
            "delta": -572.2738777009381,
            "delta_seed": -869.7340109135512,
            "plus10": 10477.608036379504,
            "delta10": -525.8074280008823,
            "dd": -9.051488831192911,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 21,
            "annual_delta_MTM": {
              "2021": 23.840331488836455,
              "2022": -231.08062480032095,
              "2023": 328.3775389271377,
              "2024": 108.19602411419692,
              "2025": -801.6071474307937
            },
            "positive_years": 3,
            "best_incremental_month": 209.7561688452115,
            "delta_without_best_month": -782.0300465461496,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": true,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.04682539682539688,
        "delta10": -548.9576266038985,
        "worstDD": -9.051488831192911
      },
      {
        "id": "S703",
        "strategy": "N503ManageR703",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11840.239043329439,
            "delta": -1216.375871748225,
            "delta_seed": -1488.4726694864912,
            "plus10": 9801.80841282274,
            "delta10": -1129.4013307231235,
            "dd": -8.934485482336708,
            "counts": {
              "Mfull": "38/60",
              "Mall": "38/62",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0370967741935484,
            "modified_exits": 24,
            "annual_delta_MTM": {
              "2021": -214.59944368183642,
              "2022": -256.45661356534583,
              "2023": 345.7487782479202,
              "2024": -208.16466421479345,
              "2025": -882.9039285341605
            },
            "positive_years": 1,
            "best_incremental_month": 184.0236046138798,
            "delta_without_best_month": -1400.399476362105,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12033.135279112626,
            "delta": -1206.307100734166,
            "delta_seed": -1503.767233946779,
            "plus10": 9883.556138240347,
            "delta10": -1119.8593261400401,
            "dd": -9.007698733905556,
            "counts": {
              "Mfull": "37/60",
              "Mall": "37/62",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0532258064516129,
            "modified_exits": 24,
            "annual_delta_MTM": {
              "2021": -200.36782291057534,
              "2022": -252.03388213441394,
              "2023": 346.69440086830764,
              "2024": -211.75064828848917,
              "2025": -888.8491482690006
            },
            "positive_years": 1,
            "best_incremental_month": 179.12946684243616,
            "delta_without_best_month": -1385.436567576602,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.0532258064516129,
        "delta10": -1129.4013307231235,
        "worstDD": -9.007698733905556
      },
      {
        "id": "S704",
        "strategy": "N503ManageR704",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12143.856484375285,
            "delta": -912.758430702379,
            "delta_seed": -1184.855228440645,
            "plus10": 10027.387379943882,
            "delta10": -903.8223636019811,
            "dd": -9.355006819199618,
            "counts": {
              "Mfull": "43/61",
              "Mall": "43/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.032539682539682535,
            "modified_exits": 13,
            "annual_delta_MTM": {
              "2021": -218.63739643705958,
              "2022": -147.79988951402265,
              "2023": 391.9136324697156,
              "2024": -333.613781500233,
              "2025": -604.6209957207611
            },
            "positive_years": 1,
            "best_incremental_month": 161.83722807780214,
            "delta_without_best_month": -1074.595658780181,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12310.794248954551,
            "delta": -928.6481308922412,
            "delta_seed": -1226.1082641048542,
            "plus10": 10084.798143385558,
            "delta10": -918.6173209948283,
            "dd": -9.370866588714543,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 13,
            "annual_delta_MTM": {
              "2021": -214.92002847950062,
              "2022": -147.16443539742795,
              "2023": 387.025010952917,
              "2024": -339.85341313698154,
              "2025": -613.7352648312371
            },
            "positive_years": 1,
            "best_incremental_month": 158.29703357841026,
            "delta_without_best_month": -1086.9451644706514,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.0007936507936507908,
        "delta10": -918.6173209948283,
        "worstDD": -9.370866588714543
      },
      {
        "id": "S705",
        "strategy": "N204ManageR705",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11831.980545599985,
            "delta": -1224.6343694776788,
            "delta_seed": -1224.6343694776788,
            "plus10": 9757.88971174821,
            "delta10": -1173.3200317976534,
            "dd": -8.26327860585957,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 25,
            "annual_delta_MTM": {
              "2021": -97.84545404211894,
              "2022": -409.29530967522624,
              "2023": -68.66321539565979,
              "2024": -18.448192562724216,
              "2025": -630.3821978019369
            },
            "positive_years": 0,
            "best_incremental_month": 157.84071384081835,
            "delta_without_best_month": -1382.4750833184971,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12026.165560964964,
            "delta": -1213.2768188818281,
            "delta_seed": -1213.2768188818281,
            "plus10": 9844.748072362072,
            "delta10": -1158.6673920183148,
            "dd": -9.00529828997393,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 25,
            "annual_delta_MTM": {
              "2021": -88.746213550834,
              "2022": -403.0860223126401,
              "2023": -83.72550061715265,
              "2024": -14.343486324971309,
              "2025": -623.3755960762282
            },
            "positive_years": 0,
            "best_incremental_month": 156.90526423315532,
            "delta_without_best_month": -1370.1820831149835,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.04682539682539688,
        "delta10": -1173.3200317976534,
        "worstDD": -9.00529828997393
      },
      {
        "id": "S706",
        "strategy": "N204ManageR706",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11521.15599733508,
            "delta": -1535.4589177425842,
            "delta_seed": -1535.4589177425842,
            "plus10": 9462.138626543396,
            "delta10": -1469.0711170024679,
            "dd": -8.929296380353158,
            "counts": {
              "Mfull": "37/61",
              "Mall": "37/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.0626984126984127,
            "modified_exits": 28,
            "annual_delta_MTM": {
              "2021": -320.54476014751526,
              "2022": -242.48891655352782,
              "2023": -2.785071494685326,
              "2024": -287.59404923105103,
              "2025": -682.0461203157829
            },
            "positive_years": 0,
            "best_incremental_month": 159.96661545817915,
            "delta_without_best_month": -1695.4255332007633,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 11716.483213907975,
            "delta": -1522.959165938817,
            "delta_seed": -1522.959165938817,
            "plus10": 9549.649290109015,
            "delta10": -1453.7661742713717,
            "dd": -9.035647991860984,
            "counts": {
              "Mfull": "37/61",
              "Mall": "37/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.0626984126984127,
            "modified_exits": 28,
            "annual_delta_MTM": {
              "2021": -306.833144690052,
              "2022": -239.76347287699355,
              "2023": -16.514618068811615,
              "2024": -289.0255790904048,
              "2025": -670.822351212566
            },
            "positive_years": 0,
            "best_incremental_month": 160.5643925227596,
            "delta_without_best_month": -1683.5235584615766,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_exits": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.0626984126984127,
        "delta10": -1469.0711170024679,
        "worstDD": -9.035647991860984
      }
    ],
    "eligible": [],
    "selected": null
  },
  "terminal_logs": {
    "O700B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_R7_OBSERVER_COUNTS {\"context\": 375, \"decisions\": 11418, \"source_event\": 82, \"source_occupied\": 11}",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"N503\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ObserveR700\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "O700C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_R7_OBSERVER_COUNTS {\"context\": 375, \"decisions\": 11418, \"source_event\": 82, \"source_occupied\": 11}",
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67}, \"recipe\": \"N503\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 266, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ObserveR700\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S701B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 4}, \"recipe\": \"S701\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 271, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR701\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S701C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 4}, \"recipe\": \"S701\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 271, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR701\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S702B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 21}, \"recipe\": \"S702\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 267, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR702\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S702C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 21}, \"recipe\": \"S702\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 267, \"margin_limited\": 0, \"notional_or_weight_limited\": 20, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 20, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR702\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S703B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 24}, \"recipe\": \"S703\"}"
    ],
    "S703C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 24}, \"recipe\": \"S703\"}"
    ],
    "S704B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 13}, \"recipe\": \"S704\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 279, \"margin_limited\": 0, \"notional_or_weight_limited\": 23, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 23, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR704\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S704C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 67, \"events\": 82, \"events_occupied\": 11, \"fills\": 67, \"r7_release\": 13}, \"recipe\": \"S704\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 279, \"margin_limited\": 0, \"notional_or_weight_limited\": 22, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 22, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N503ManageR704\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S705B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 96, \"events_occupied\": 13, \"fills\": 80, \"r7_release\": 25}, \"recipe\": \"S705\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 22, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 22, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ManageR705\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S705C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 96, \"events_occupied\": 13, \"fills\": 80, \"r7_release\": 25}, \"recipe\": \"S705\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ManageR705\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S706B": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 96, \"events_occupied\": 13, \"fills\": 80, \"r7_release\": 28}, \"recipe\": \"S706\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 22, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 22, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ManageR706\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 20, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpySecond4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ],
    "S706C": [
      "[INFO | 2025-12-31T00:00:00] ==> BTC_EXPLORE {\"counts\": {\"closes\": 80, \"events\": 96, \"events_occupied\": 13, \"fills\": 80, \"r7_release\": 28}, \"recipe\": \"S706\"}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 45, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}, \"short\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 277, \"margin_limited\": 0, \"notional_or_weight_limited\": 21, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 21, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"N204ManageR706\", \"symbol\": \"BTC-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 38, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortComparePaxgMarket4h\", \"symbol\": \"PAXG-USDT\", \"trade_risk\": 0.01}",
      "[INFO | 2025-12-31T00:00:00] ==> PORT_CAPACITY {\"counts\": {\"long\": {\"capacity_zero\": 0, \"eligible_sizing_attempts\": 19, \"margin_limited\": 0, \"notional_or_weight_limited\": 0, \"risk_budget_limited\": 0, \"sized_below_trade_target\": 0, \"zero_after_lot_rounding\": 0}}, \"notional_cap\": 4.4, \"portfolio_risk\": 0.08, \"strategy\": \"PortCompareSpyMarket4h\", \"symbol\": \"SPY-USDT\", \"trade_risk\": 0.01}"
    ]
  },
  "root_deterministic_review": {
    "status": "PASS",
    "count": 86,
    "checks": [
      "O700B_audit",
      "O700B_terminal",
      "O700B_month_reconcile",
      "O700B_long31",
      "O700C_audit",
      "O700C_terminal",
      "O700C_month_reconcile",
      "O700C_long31",
      "S701B_audit",
      "S701B_terminal",
      "S701B_month_reconcile",
      "S701B_long31",
      "S701C_audit",
      "S701C_terminal",
      "S701C_month_reconcile",
      "S701C_long31",
      "S702B_audit",
      "S702B_terminal",
      "S702B_month_reconcile",
      "S702B_long31",
      "S702C_audit",
      "S702C_terminal",
      "S702C_month_reconcile",
      "S702C_long31",
      "S703B_audit",
      "S703B_terminal",
      "S703B_month_reconcile",
      "S703B_long31",
      "S703C_audit",
      "S703C_terminal",
      "S703C_month_reconcile",
      "S703C_long31",
      "S704B_audit",
      "S704B_terminal",
      "S704B_month_reconcile",
      "S704B_long31",
      "S704C_audit",
      "S704C_terminal",
      "S704C_month_reconcile",
      "S704C_long31",
      "S705B_audit",
      "S705B_terminal",
      "S705B_month_reconcile",
      "S705B_long31",
      "S705C_audit",
      "S705C_terminal",
      "S705C_month_reconcile",
      "S705C_long31",
      "S706B_audit",
      "S706B_terminal",
      "S706B_month_reconcile",
      "S706B_long31",
      "S706C_audit",
      "S706C_terminal",
      "S706C_month_reconcile",
      "S706C_long31",
      "S701B_gates",
      "S701B_eligibility",
      "S701C_gates",
      "S701C_eligibility",
      "S702B_gates",
      "S702B_eligibility",
      "S702C_gates",
      "S702C_eligibility",
      "S703B_gates",
      "S703B_eligibility",
      "S703C_gates",
      "S703C_eligibility",
      "S704B_gates",
      "S704B_eligibility",
      "S704C_gates",
      "S704C_eligibility",
      "S705B_gates",
      "S705B_eligibility",
      "S705C_gates",
      "S705C_eligibility",
      "S706B_gates",
      "S706B_eligibility",
      "S706C_gates",
      "S706C_eligibility",
      "observerB",
      "observerC",
      "duplicateP604B",
      "duplicateP604C",
      "duplicateP603B",
      "duplicateP603C"
    ],
    "note": "Root deterministic cross-check, not independent external review or a second MTM reconstruction."
  },
  "calendar_clarification": "\n## Aclaración de calendario, sin cambiar regla ni ventana\n\nEl término «añoscompletos2021..2025» en la puerta de concentración es una errata descriptiva:2025 está recortado al2025-12-30porfinish_dateexclusiva. El algoritmo congelado compara exactamente los cinco bloques anuales2021..2025 y exige3de5positivos; se mantiene sin modificación. No se reclasifica2025comoaño completo ni seusa2026. Los4añoscalendariocompletos son2021..2024;2020y2025parciales se muestran explícitamente en el informe. Mesesfull61/19Qcorrectos permanecenintactos. Esta aclaraciónno cambia seleccióneconómica, ranking ni presupuesto.\n"
}
```
