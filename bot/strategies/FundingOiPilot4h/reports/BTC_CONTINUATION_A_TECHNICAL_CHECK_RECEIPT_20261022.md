# Continuacion A: recibo tecnico sintetico
Fecha local2026-10-22. Job unico autorizado porroot:4a674bee98ca4510bba6305a40a0d5d4. Estado succeeded,exit0; PASS92outcomes primerintento. Sin rerun,errores,motores economicos,drafts o datosobservados en estecheck. Slotanalysis liberado yroot informado antesdeesta conservacion.

Fuentes finales ya guardadas/readbackexactas en BTC_CONTINUATION_A_SOURCES_20261022.md; codigo completo suministrado antesdeljob en BTC_CONTINUATION_A_SUPPLIED_SYNTHETIC_CHECK_20261022.md. Protocolo vigente BTC_CONTINUATION_A_PROTOCOL_20261022.md; CODESdocumental anterior BTC_CONTINUATION_A_CODES_20261022.md. Los7hashes enresultado coinciden exactamente conexpected freeze. Padresnomutados.

Runtime observado Python3.11.17/NumPy1.26.4/pandas2.2.3. Artefacto resultado6056bytes recuperado completo/truncatedfalse.92outcomes no representan92hipotesis o muestrasindependientes; varios son controles de invalidez/contextos espejo. Es prueba tecnica de textos suministrados constubs/arraysfabricados; no backtest ni broker/venue/indicator kernel ni evidencia economica. NativeMARKET/ordenes/pagos/ledgers quedaran para root despues del par economico, sin motor de preflight. Nada de estePASS certifica objetivo de rentabilidad.

## Recibo de estado completo
```json
{
  "action": "get_analysis_job",
  "status": "success",
  "job": {
    "id": "4a674bee98ca4510bba6305a40a0d5d4",
    "kind": "analysis",
    "workspace": "storage/mcp/analysis/4a674bee98ca4510bba6305a40a0d5d4",
    "inputs": [],
    "status": "succeeded",
    "pid": 2280,
    "exit_code": 0,
    "started_at": "2026-10-22T12:24:33+00:00",
    "finished_at": "2026-10-22T12:24:35+00:00",
    "timeout_minutes": 5,
    "output_truncated": false,
    "expires_at": "2026-10-23T12:24:35+00:00",
    "lifetime": "Deleted when a later analysis starts, once 24 hours have passed since it finished (expires_at), or earlier when finished jobs exceed the 50-job or 2 GiB caps (oldest first)."
  },
  "artifacts": [
    {
      "path": "BTC_CONTINUATION_A_SYNTHETIC_RESULT.json",
      "size_bytes": 6056,
      "kind": "text"
    }
  ],
  "artifacts_truncated": false,
  "output": "",
  "output_lines_returned": 0,
  "earlier_output_omitted": false,
  "output_truncated": false,
  "location": "On the machine running Jesse, inside the Jesse project folder. Not in the assistant's local workspace."
}
```

## Resultado completo
```json
{
  "status": "passed",
  "outcome_count": 92,
  "outcomes": [
    "seven_frozen_source_hashes_exact",
    "fixture_day_exact_UTC_midnight",
    "only_event_and_invalid_overrides",
    "execution_management_observer_inherited",
    "wrapper_flags_and_actual_origins",
    "frozen_previous_day_phase_1",
    "frozen_previous_day_phase_2",
    "frozen_previous_day_phase_3",
    "frozen_previous_day_phase_4",
    "frozen_previous_day_phase_5",
    "frozen_previous_day_phase_6",
    "00_block_old_day_then04_new_day_reset",
    "119_reject_120_accept_side_1",
    "minute_equal_boundary_does_not_count_side_1",
    "current_close_equal_boundary_no_break_side_1",
    "119_reject_120_accept_side_-1",
    "minute_equal_boundary_does_not_count_side_-1",
    "current_close_equal_boundary_no_break_side_-1",
    "price_reflection_symmetry_of_context",
    "only_acceptance_gate_differs",
    "raw_event_and_market_state_common",
    "reject_or_fill_never_waits_reverses_same_day_A_ACCEPTED",
    "same_or_backward_math_clock_idempotent_A_ACCEPTED",
    "reject_or_fill_never_waits_reverses_same_day_A_CLOSE_ONLY",
    "same_or_backward_math_clock_idempotent_A_CLOSE_ONLY",
    "future_minutes_excluded_asof_prefix",
    "common_invalid_day_gap_A_ACCEPTED",
    "invalid_day_no_later_backfill_gap_A_ACCEPTED",
    "common_invalid_day_gap_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_gap_A_CLOSE_ONLY",
    "invalid_consumption_common_gap",
    "common_invalid_day_duplicate_A_ACCEPTED",
    "invalid_day_no_later_backfill_duplicate_A_ACCEPTED",
    "common_invalid_day_duplicate_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_duplicate_A_CLOSE_ONLY",
    "invalid_consumption_common_duplicate",
    "common_invalid_day_timestamp_fraction_A_ACCEPTED",
    "invalid_day_no_later_backfill_timestamp_fraction_A_ACCEPTED",
    "common_invalid_day_timestamp_fraction_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_timestamp_fraction_A_CLOSE_ONLY",
    "invalid_consumption_common_timestamp_fraction",
    "common_invalid_day_nonfinite_A_ACCEPTED",
    "invalid_day_no_later_backfill_nonfinite_A_ACCEPTED",
    "common_invalid_day_nonfinite_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_nonfinite_A_CLOSE_ONLY",
    "invalid_consumption_common_nonfinite",
    "common_invalid_day_nonpositive_A_ACCEPTED",
    "invalid_day_no_later_backfill_nonpositive_A_ACCEPTED",
    "common_invalid_day_nonpositive_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_nonpositive_A_CLOSE_ONLY",
    "invalid_consumption_common_nonpositive",
    "common_invalid_day_invalid_geometry_A_ACCEPTED",
    "invalid_day_no_later_backfill_invalid_geometry_A_ACCEPTED",
    "common_invalid_day_invalid_geometry_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_invalid_geometry_A_CLOSE_ONLY",
    "invalid_consumption_common_invalid_geometry",
    "common_invalid_day_parity_open_A_ACCEPTED",
    "invalid_day_no_later_backfill_parity_open_A_ACCEPTED",
    "common_invalid_day_parity_open_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_parity_open_A_CLOSE_ONLY",
    "invalid_consumption_common_parity_open",
    "common_invalid_day_parity_close_A_ACCEPTED",
    "invalid_day_no_later_backfill_parity_close_A_ACCEPTED",
    "common_invalid_day_parity_close_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_parity_close_A_CLOSE_ONLY",
    "invalid_consumption_common_parity_close",
    "common_invalid_day_parity_high_A_ACCEPTED",
    "invalid_day_no_later_backfill_parity_high_A_ACCEPTED",
    "common_invalid_day_parity_high_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_parity_high_A_CLOSE_ONLY",
    "invalid_consumption_common_parity_high",
    "common_invalid_day_parity_low_A_ACCEPTED",
    "invalid_day_no_later_backfill_parity_low_A_ACCEPTED",
    "common_invalid_day_parity_low_A_CLOSE_ONLY",
    "invalid_day_no_later_backfill_parity_low_A_CLOSE_ONLY",
    "invalid_consumption_common_parity_low",
    "invalid64_hook_consumes_day",
    "invalid_day_recovers_only_next_day",
    "zero_reference_range_invalidates_day",
    "missing_reference_timestamp_invalidates_day",
    "base_consumes_before_open_A_ACCEPTED",
    "base_consumes_before_open_A_CLOSE_ONLY",
    "occupied_common_state_open",
    "base_consumes_before_pending_A_ACCEPTED",
    "base_consumes_before_pending_A_CLOSE_ONLY",
    "occupied_common_state_pending",
    "base_consumes_before_same_exit_A_ACCEPTED",
    "base_consumes_before_same_exit_A_CLOSE_ONLY",
    "occupied_common_state_same_exit",
    "real_shared_plan_quota_ATRsimple_TP48h_origin",
    "request_current_price_no_claim_of_native_fill",
    "compact_observed_synthetic_event_plan_logs"
  ],
  "source_hashes": {
    "BtcResearchR10Base4h": "2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9",
    "BtcResearchR11Base1m": "be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87",
    "BtcResearchR16LegacyBase1m": "56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542",
    "BtcResearchR32SpecialistBase1m": "205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3",
    "BtcResearchR32DayAcceptanceBase1m": "740fe4e337f96d9d01d59c82c2a84ed337940e1df4138d5d724a4017dd654193",
    "BtcResearchR32DayAccepted1m": "a110425ac45a1f4019b62b51c73fa98cba592e1e4302ddb51af1c6f3912a5a50",
    "BtcResearchR32DayCloseOnly1m": "12aae7b292d76547febf4a513ca94c9ec212274fc6acc846045d3177c03610fd"
  },
  "runtime": {
    "python": "3.11.17 (main, Oct  6 2026, 02:01:58) [GCC 12.2.0]",
    "numpy": "1.26.4",
    "pandas": "2.2.3"
  },
  "limitations": [
    "Only supplied-source AST/stubs and fabricated OHLC; no strategy/model imports or observed prices.",
    "Common64OHLC validated by actual shared helper in integration fixtures; M1 tests cover exact240 closed/asof.",
    "No backtest/nested engine/broker/venue validation; MARKET proof requires native orders after the economic pair.",
    "No claim that outcome count is independent evidence or estimates profitability.",
    "Parent execution unchanged; this focuses A state/representation/validity and representative integration."
  ]
}
```
