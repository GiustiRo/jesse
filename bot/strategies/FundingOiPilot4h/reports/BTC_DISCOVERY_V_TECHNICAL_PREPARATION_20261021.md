# V — preparación técnica, sin economía
Estado: fuentes guardadas/readback exacto; check técnico succeeded, revisión final root/independiente pendiente. No drafts ni simulación económica creados por esta tarea.

Protocolo: BTC_DISCOVERY_V_PROTOCOL_20261021.md. Normativa fijada antes de conocer resultado U, fuentes creadas tras aprobación root. U se cerró mientras se preparaba harness; V no se eligió por su PnL.

Job técnico:9f08bcad89ec485a8757da1d6650e9be, started/finished2026-10-21T21:22:13UTC,succeeded,inputs:[],1intento/0errores. NumPy1.26.4.12grupos materiales PASS. Código completo y resultados en BTC_DISCOVERY_V_TECHNICAL_CHECK_20261021.json. HarnessSHA256 4d059e1fb694fcc221595f3d93a5813129d5a1feea62d411e71f66153b77a03c.

- 240-pair non-symmetric VAR oracle, row orientation, scalar G exact
- training indices include latest known target, no unknown target, default rcond
- shared rank/variance/nonfinite invalidity
- LinAlgError cash only, contract/programming errors propagate
- finite coefficient/recursive-state gates, no rescue
- as-of windows, future/prefix irrelevance, gaps, OHLC and monetary rescaling
- mode selection, inherited execution interfaces, ATR14 simple risk distance
- occupied events consumed, no queue, no same-close entry
- hurdle boundary cash and common admission at runtime
- 2-percent fees-aware budget, 90-percent margin, floor8 and invalid stop
- real-fill noTP/24h, observer count and terminal stats delegation
- AST narrow exception, frozen inheritance, no ETH execution/funding or dynamic TP

Fuentes y hashes:
- strategies/BtcResearchR10Base4h/__init__.py: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- strategies/BtcResearchR11Base1m/__init__.py: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- strategies/BtcResearchR12ArBase1m/__init__.py: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- strategies/BtcResearchR22JointBase1m/__init__.py: 7386e9ae363ffcd6efe9696baab7d9abb6b07fef57fd542572926e1659e6f4fc
- strategies/BtcResearchR22JointVar1m/__init__.py: 94722be2699f2c10a924182b2ab73811094e8516680d06b9e1247f9653795f02
- strategies/BtcResearchR22JointAr1m/__init__.py: 399f0f43ed1f43f68014c92f74c37534df40802f82756b9e7d8799a968f340de

Contadores implementados: joint_counts por valid/windows_invalid/returns_invalid/ar_variance_invalid/lstsq_numerical_error/var_rank_invalid/coefficients_invalid/ar_forecast_invalid/recursive_state_invalid/var_forecast_invalid; signals/occupied/entries heredados (entradas contadas en fill real por ARparent). R22_JOINT_OPEN guarda B,intercept,forecastVAR/AR,ARbeta/intercept sólo al fill. R22_JOINT_STATS despuéssuper_emit acompaña PRETERMINAL/FINAL sin barrer logsM1; la gestión no modifica posición por modelo nuevo ni usa ETHorders.

No atrapado de programación: única except np.linalg.LinAlgError de lstsq con inputs finitos. Sin retries/epsilon/fallback/clip/filtros de estabilidad. El control llama return_forecast(btc,True) Gexacto; comprobación adicional de estados recursivos escalares sólo gate común, no sustitución del resultado. rank2 NumPydefault del Xcentrado, orientaciónBfila predictor/columna respuesta, A=B.T. Seis ETH futuros son pronósticos, no realizados.

Paridad de gestión: class JointBase hereda ArBase onopenstop2ATR feeaware/noTP ytimeout6BAR; override de onopen llama super una vez y luego logging. No override de update_position/on_close/before_terminate/entry interfaces. R11observeryR10sizing intactos y hashes releídos después del check. Teststub no prueba broker real/funding/cobertura ni renta. Cualquier fill entre fronteras4h vence en primera decisión4h tras>=24h desdeopened_at. Hurdle .0019señal, no debitocosto; forecastlogpricebruto, ledgerfundingON pendiente verificar en motores.

- Synthetic tests do not validate economic edge, observed coverage, ETH historic availability or live execution.
- Observer engine internals are stubs; frozen R11/R12 source identity and AST inheritance were checked, not framework runtime.
- Future full backtests must verify common admission and applied historical funding with complete financial snapshots.
- NumPy default rank depends on runtime numeric implementation; no condition-number stability cutoff is imposed.

Presupuesto futuro2economías+2reemplazos exclusivamente técnicos, autorización posterior root;0económicas/0drafts/0reemplazos consumidos aquí. No scripts/imports/2026/framework/global/install/restart/live/paper/Pi. Slot análisis liberado al terminarcheck.
