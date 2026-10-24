# Tanda F: ¿seguir o revertir un movimiento concentrado en saltos?

Protocolo previo e independiente del resultado E. Presupuesto: dos políticas, dos corridas económicas continuas; hasta dos reemplazos sólo por errores técnicos con evidencia, nunca por rentabilidad. No ejecutar hasta liberar los dos motores E. Máximo dos backtests globales y un análisis propio.

## Diferencia material y origen
Antecedente R40SpyJumpComponentFade: 13 incrementos de sesión cash, BV/RV, reversión a cierre y72h; R40 excluyó BTC. V4ShockBTC mide un solo desplazamiento1h>=2ATR yvolumen>=2media24. Aquí se usa la organización de24 retornos horarios BTC, sinvolumen, estado ni señalKalman/recovery de E. No reproduce bandas/RSI/canales. No convertir pérdida del antecedente SPY en resultado BTC ni llamar nuevo al estimador. No son dos hipótesis independientes: son dos respuestas opuestas al mismo evento.

Adaptación deliberada: BTC-USDT perpetuo Binance continuo24/7, sin calendarioneoyorquino ni cierre cash. Se reemplaza sesión13×30m por ventana móvil24×1h y decisiones cada4hUTC; no transferir horarios bursátiles a BTC. No equivalente a instrumento SPYtokenizado ni prueba de paridad. El movimiento24h es entre25cierres horarios consecutivos y telescopa exactamente. Variación RV=sum(r_i²); bipower BV=(pi/2)*(24/23)*sum(abs(r_i*r_(i−1))); J=max(RV−BV,0)/RV. Con24observaciones es heurística, no testestadístico certificado de saltos. SiRV0=>estado0. Evento siJ>=1/3 yabs(sumr)>=.5ATR4h_actual/precioactual. Estado=sign(sumr), otra condición=>0; entrar sólo al cambiar a estado no nulo, consumido aun ocupado, sincola. Cruce solapado no es muestra independiente.

F_FADE entra contra el signo; F_FOLLOW sigue el signo. Protección idéntica: stop2ATR14simple4h congelado, TP2R, salida48h en cierres4h. Ambas direcciones y todos los años se conservan; sin filtros macro/OI/funding/volumen ni selección de lado posterior. Una política supera el comparador sólo relativamente: debe cumplir las puertas absolutas por sí misma.

## Contrato fijo
RutaBTC1m observador/ejecución, datosBTC1h y4h; warmup2404h. [2020-10-15,2026-01-01)UTC, desarrollo2020–25ya observado, sin economía2026. Capital10k, riesgo2%portrade/6%agregado/3xaislado, sizing feeaware helperR10 sin cambios, floor8/margen90%. Fee.00045porlado, funding históricoON/aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; proxyde marcas explícito. Slippage0modelado; sin estrés ni cambio de exposición. Una posición, sinpirámides, no reentrada al salir enmismocierre. Gaps/funding no garantizan tope de pérdida.

Observador R11 wallet+PnLabierto cadaM1yfill; fronteras00:00UTCpostfunding/predecisión. DD M1+eventos, no extremo de tick; convención temporal por fase, no suma estricta de eventos por mes civil. Mesesinactivos incluidos enmediana. Completitud25cierres1h y15OHLC4h, asofexacto yconsecutivos, invalidar/reset antehuecos. No arreglar datos sintéticos.

## Puertas y presupuesto
CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),Mactivos65%,Qcompletos80%,medianamesescalendario>0,netoquitando2mejoresmeses>0;N>=100 preliminar sinconfianzaestadísticaimplícita. Objetivosr9,aspiraciones40–50%+/M70. Ambas evaluadas porseparado sinselectorposthoc. NO_CUMPLEsi falla cualquier puerta económica; INCONCLUSA si económica favorable pero insuficiencia/datos. Ningunapromociónoperativa niestresautomático.

Checks previos: AST, RV/BVtelescopía, saltoaislado vsincrementosdifusos, signos espejo, cero, transición, causalidad/futuro/gaps, ATR/sizingheredados. Readbackfuentes/hash/config enmanifiesto antesde ejecutar. Auditoría completa después: trades bruto−fees+funding=neto=equityfinal−10k a1e−6; cobertura2.741.760M1,63intervalos/62meses/20Q yresultado mensualreconciliado. ReportesMCPysubidaHubíndiceúltimo. No afinar J/ventanas/protecciónsi fallan; elegir otra pregunta material dentrodelobjetivoglobalautónomo.
