# BTC valor diario: CODES documental breve
Fecha: 22 de octubre de 2026. Normativa: BTC_DAILY_VALUE_CAPTURE_PROTOCOL_20261022.md. No hay nuevas fuentes, drafts, jobs o motores. Se evita duplicar infraestructura ya congelada.

## Dependencias leídas
- BtcResearchR32SpecialistBase1m, freeze R32 SHA256 205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3. Fuente completa en BTC_CONTINUATION_A_CODES_20261022.md. Su before observa M1 y recibe 64 barras 4h cerradas; el TP 2R/plazo 48h del padre no define la nueva captura.
- BtcResearchR11Base1m, SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87: observador/meses/terminal.
- BtcResearchR10Base4h, SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9: closed_window y atr14 simple.
- BtcResearchR16LegacyBase1m, SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542: sólo legacy_plan/reserva/lote, sin entradas K.
Los tres textos completos y hashes de runtime están en CODES/check/receipt de Continuación A. Releer/hash antes de implementar; el digest histórico no certifica un runtime futuro. Ningún padre se editará.

## Antecedentes y evidencia
ResearchV5VwapPV1h y strategies/ResearchV5Base1h/vwap_features.py, completos: media/varianza HLC3 ponderada rolling24h, escala max(sigma,ATR), reingreso K2, salida MARKET al centro móvil. V5_VWAP_SCREEN_REPORT.md cerró PV/PVOI negativos: PV 546 trades, -33.8694%, PF .883113. No se rescata esa receta variando bandas: la nueva autorización pregunta por captura en ancla diaria excluyendo B frente a 2R, sobre la MISMA entrada.

BTCExploreR801 completo y BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md: coste HLC3 de una única vela de máximo volumen entre12; corto al perderlo, TP2R/48h. X801 redujo neto. No es VWAP diario ni política de retorno al valor; N204 usa otra cohorte rolling y tampoco constituye el control.

OrchManageFastMrBtc4h y MultiAssetSleeves4h, completos: long RSI2/EMA200/SMA5 móvil48h y dip SPY/EMA20 fija5d. Son antecedentes de reversión, no controles equivalentes. La hipótesis no pretende novedad universal.

Hub r33/HANDOFF completo cierra R32 y sus seis pruebas. No seleccionar long-only por contribuciones de cuentas mixtas ni seguir vecinos de aceptación/inside/permanencia.

K1001_LONG_MARKET_FRAMEWORK_AND_ENTRY_TYPES_20261021.md y JSON leídos completos: is_price_near threshold .00015 se evalúa antes de LIMIT/STOP; precio actual solicita MARKET. Es evidencia estática/histórica, no prueba nativa futura. Se exige condición exacta conocida en implementación y audit de órdenes después de los mismos motores. No tarifa maker ni conversión omitida.

## Fuentes futuras propuestas, aún ausentes
BtcResearchR34DailyValueBase1m aislada y dos hojas ValueTarget/TwoRTarget. Root acordará primero la ABI: plan con targetlevel/meta, protección desde fill y deadline00 evaluado M1. R11 conserva fases; R32 no se modifica. No ocultar TP variable como tp_r=None. Schema R34_PLAN/OPEN/CLOSE/SUMMARY y límites de1800 caracteres en protocolo.

Esqueleto normativo, no código creado:
T en08/12/16/20 UTC; S=T-4h; referencia M1 [00,S).
G = HLC3 ponderado por volumen conocido al comenzar B.
C_S exterior a2ATR_S y C_T recupera hacia G sin alcanzarlo.
Primer patrón bruto consume D antes de targets, sizing y ocupación.
E actual; d=2ATR_T; objetivos G y E+side*2d.
Guard común: ambos objetivos correctos, positivos, no-near y profit>fees base.
legacy_plan(.5 wallet,.5 margen,3,fee); TP real G fijo o E_fill+side*2d.
Cierre a medianoche en cada M1, aun sin features válidas.
Ledger antes de FINAL; safety trade nunca omitido.

## Presupuesto y alcance
Dos motores futuros para políticas completas. Cambiar TP cambia ocupación/capitalización: no puede reconstruirse sumando PnL de V5/X801 ni comparando sólo trades comunes. Misma cuota1%, costos base/funding y ventana observada; no datos nuevos, vecinos o preflight económico. Check plan separado preparado; todavía no está ligado a una fuente final ni ejecutado.
