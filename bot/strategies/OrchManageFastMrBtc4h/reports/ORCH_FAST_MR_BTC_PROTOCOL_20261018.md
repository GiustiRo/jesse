# Propuesta acotada: reversión rápida BTC 4h en régimen alcista
Fecha2026-10-18. Estado: receta única autorizada para implementar; fuente y draft preparados para revisión final del orquestador ANTES de simulación. Un único control, sin parrilla RSI/media/stop.
## Historial y solapamiento
MultiAssetSleeves4h fue leído por MCP: BTC conserva ruptura26 MARKET con ADX/RSI14/EMA20>80; únicamente SPY usa MR RSI3<=20, macroEMA120 ascendente, entradaLIMIT bajo el dip, TP estáticoEMA20 y caducidad5d.
La docstring del short actual afirma origen en una sleeve longMR fallida. Esto impide presentar la premisa MR como descubrimiento independiente; la evidencia de código disponible no prueba que BTC ya haya ejecutado esa receta concreta. No ocultar el fracaso de SPY ni cambiar solo RSI3→2 para renombrar una familia.
## Hipótesis material
Reversión de shocks cortos dentro de tendencia alcista. Entrada MARKET tras cierre evita condicionar el fill a una caída futura adicional; salida a media rápida dinámicaSMA5 (20h) evita exigir recuperación a EMA20 congelada; caducidad48h hace explícito el horizonte. El régimen aboveEMA200 ascendente evita permitir pullbacks bajo la media macro. Son modificaciones coordinadas de ejecución/horizonte de la misma premisa MR, no tres ventajas nuevas.
## Receta fija propuesta
BTC-USDT4h, long solamente, standaloneuna ruta para aislarlo de proxies; no reemplaza referencia.
Entrada: cierre>EMA200, EMA200actual>EMA200 de seis intervalos completos atrás ([-1] frente a [-7]), RSI2<=10 y cierre<SMA5. Datos exclusivamente cerrados, mínimo207barras de historia; warmup240.
Orden MARKET al precio de decisión cerrado, comisión0.00045porlado incluso toda LIMIT futura. Stoprealfill−2.5*ATR14 congelado al señal.
Salida completa MARKET cuando cierre>=SMA5actual, o al transcurrir48helapsedUTCdesdeentrada; stop en exchange activo continuamente. Sin parciales/piramidado/reentradasmientrasabierto. No cierres de mes o horarios elegidos por meses malos.
Riesgo1%delcapitalconservador min(wallet,equity),feesamboslados yreserva desizing0.001incluidos; derivarqtyde margen disponible,redondeoBTC0.001, rechazarqty<=0/riesgoinválido/margeninsuficiente. Mantenerpendingreserva,riskglobal8% ygross4.4x como máximos,5xisolated/10k. No cambiosconfigframework/live.
Ventana2020-10-15→2025-12-31exclusivo;2026reservado;noimportardatosnuevos. SPYsolo seconsidera despuésderechazooanálisisBTC,yexigehorariosfiltrados/noindicadoresvolumen.
## Falsación previa
Netopositivo trasfees es mínimo, no aprobación; examinar stop-taillosses, meses/trimestresMTM, costes, aportación poraños y retornos/correlación con referencia antesdecombinar. Si nohayedge neto o es frágil a costes, rechazar sin RSIgrid. Riesgo1% puedeproducirCAGRmodesto;valorarcapacidadcomplementariaexante,noequipararlocon3%cartera.
Si sobrevive, cualquierprueba de robustez o combinación necesita hipótesis/costes/cola preregistrados; no seleccionarregímenesdecalendario mirandoañosmalos.
## Limitaciones
Premisa MR compartehistoriaexpost; noOOS. MARKET de backtest no modelaimpacto/spread/funding;0.00045esfee nofriccióncompleta. EMA200en4h son~33d, no media200d ni coberturacrisis. La caducidad48hseevalúaporcallbacks4h ypuedesuperarloenunafraccióndebarra; documentar.
