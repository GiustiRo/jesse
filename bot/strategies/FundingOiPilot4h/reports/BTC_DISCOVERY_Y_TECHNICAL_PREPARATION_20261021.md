# Y — preparación técnica completada, sin economía

Fullcheck [job técnico: sin dashboard de backtest]7a53cb54457e4d478247cfae6dd4155b succeeded/PASSED en primer intento; NumPy1.26.4,13grupos materiales. Un probe previo bdc2d3c5c0294a7cbc97ca925e8c4894 también succeeded. Total2análisis técnicos,0jobsfallidos,0erroresharness,0backtests técnicos/económicos,0drafts/0reemplazos. El probe no fue un fullcheck ni un backtest.

Dos defectos materiales corregidos antes del check completo: asof de routeM1 frente a current4h antes del diagnóstico, y degeneracy exacta de constantes logV/magnitudes pese a std flotante espuria. Se preservan fuentes33d07…/8113…/437833… con motivos y código exacto del probe. NaN del probe se guarda como texto, no objeto JSON no estricto.

Fuentes finales:
- strategies/BtcResearchR10Base4h/__init__.py: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- strategies/BtcResearchR11Base1m/__init__.py: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- strategies/BtcResearchR12ArBase1m/__init__.py: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- strategies/BtcResearchR25VolumeLagBase1m/__init__.py: 437833f8ab078a24843b0ce326a4cd556bae8cdcb755be420febe648165251b7
- strategies/BtcResearchR25VolumeLagState1m/__init__.py: 01c7aba73af2f10b5af06f46be016e0e90b34e9cb15aad494f97f64cb103b041
- strategies/BtcResearchR25VolumeLagSymmetric1m/__init__.py: 2913fee1da3cd5e219fcee4c6691d802716bdace2bccf07011c41537394261d1

Grupos de verificación:
- vectorized per-origin25 vs independent scalar oracle, current26/392 parity
- 392 row0 unused,360 exact slots and known targets, no future centering
- joint temporal reversal F/R, S invariant/D flips, scale offsets cancel
- exact constant-volume2/3/1e9 and constant-magnitude degeneracy, zeros/nonfinite
- shared nonzero-D training mask, STATE20 and symmetric40, no olderfill
- asof closed windows, future/prefix irrelevance, gap and OHLC integrity
- unique runtime origin/deadline, T<=last no-op and six observed-bar label
- gap/OHLC censoring and idempotent terminal without invented final maturity
- diagnostic before TRAIN392 and volume/feature gates; OHLC-only maturity
- asof parity precheck censors pending even when TRAIN392 is unavailable
- mode raw forecasts, shared lifecycle, no queue, exact hurdle, ATR-independent capture
- real-fill SL2ATR/noTP/24h fee budget, bounded support/deadline telemetry, PRE/FINAL idempotence
- AST frozen inheritance, no extra models/TP or broad error swallowing

Recibos permanentes:
- BTC_DISCOVERY_Y_TECHNICAL_RECEIPT_20261021.json: full code, jobs/artifacts, probeRaw como string, tres versiones fuente y hashes, intentos/errores/readbacks.
- BTC_DISCOVERY_Y_IMPLEMENTED_CODES_20261021.md: fuentes finales y supersedidas, wrappers y motivo de cada cambio.
- BTC_DISCOVERY_Y_CODES_AND_ANTECEDENTS_20261021.md: 313513caracteres de fuentes/closures completos, readback paginado exacto.
- BTC_DISCOVERY_Y_PROTOCOL_20261021.md: normativa y precisiones guardadas/releídas antes de fuentes.

Se validó con inputs:[] y AST/stubs suministrados. No imports de estrategias/framework reales ni precios observados. Los stubs no acreditan cobertura histórica, broker real o funding: lo validarán motores/auditoría si root autoriza después. N20/360/13grupos no implica independencia o potencia.

Telemetría incluida en primera versión: R25_VOLUME_OPEN con F/R/S/D, s/q/d, soporte8celdas, medias y forecast raw, origen/deadline forecast, opened_at/holddeadline, SLreal/distance/riskbudget. R25_TRAIN_STATS acotado; R25_DIAG_STATS y una R25_DIAG_CELL por celda para evitar truncamientos. Diagnóstico runtime puroFIFO6, etiqueta OHLC6cierres independiente de volumen/feature/ATR/TRAIN/hurdle/ocupación; no recuento de360slots. No-op T<=last, censura terminal PRE/FINAL idempotente. Contadores no son órdenes hipotéticas.

R10sizing/R11observer/R12AR noTP24h intactos, hashes releídos después del check. Misma fuente final en ambos wrappers; ninguna protección o riesgo depende de D o del diagnóstico. Máscara común exige tres signos válidos aunque controlignoreD. Row0padding participa integridad392pero no features/labels seleccionados.

Root e independiente revisaron fuente final completa conformes; pendiente lectura de este recibo antes de drafts/manifiesto/motores. Slots liberados. Ninguna evidencia de rentabilidad se afirma con sintéticos. Presupuesto futuro2economías y hasta2reemplazos sólo técnicos, máximo global2backtests+1analysis. X continúa HOLD separado. Sin cambio framework/configglobal/imports/installs/restarts/live/paper/Pi/nuevaeconomía2026/scripts.
