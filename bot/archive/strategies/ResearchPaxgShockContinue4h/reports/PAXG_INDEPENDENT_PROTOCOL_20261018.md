# PAXG — protocolo previo a resultados, 18 octubre 2026 local

## Pregunta y selección
Desarrollar reglas de precio sobre PAXG spot existente simulado en Binance perpetual, destino operativo aceptado por el usuario. Funding excluido y no implementado. No inferir COMEX, flujo de oro ni microestructura. BTC congelado. El historial 2020–25 es desarrollo ampliamente adaptativo: no OOS limpio.

Dos hipótesis económicas espejo sobre la respuesta posterior al mismo evento: difusión de información (continuación) frente a exceso transitorio (reversión). Pertenece a las familias amplias momentum/MR, pero NO se repite retest Donchian26, Turtle55/10 diario, rotación mensual, fallo de rango o divergencia PAXG/BTC/SPY7d. La diferencia es un shock de cierre normalizado por volatilidad PREVIA, simetría long/short y horizonte fijo sin filtros de tendencia ni un runner. No asumir independencia respecto de investigación histórica.

## Recetas congeladas
ResearchPaxgShockContinue4h y ResearchPaxgShockReverse4h; única diferencia RESPONSE=+1/-1.
Evento en vela4h recién cerrada: abs(close_t-close_t-1)>=1.5*ATR14(candles[:-1]); ATR previo, excluye evento. Umbral1.5 define desplazamiento material ex ante; ATR14 usa default Jesse. Mínimo30 velas y valores finitos/positivos. No Donchian/EMA/RSI/ADX/volumen/calendario/activo auxiliar.
Dirección por signo del shock, o su inversa; MARKET sólo si última M1 propia abre exactamenteT−60seg y precio finito/positivo. Una oportunidad por vela; eventos mientras posición abierta se ignoran y no forman cola. No piramidado. Un evento pasado no se rearma.
Stop fijo2ATR previo desde precio efectivo de entrada, long y short. 2ATR es invalidación ex ante, no seleccionado. Sin target, trailing ni BE. Cierre MARKET a primera decisión4h con tiempo>=48h desde position.opened_at real y M1 fresca;48h contrasta respuesta dos días, sin buscar horizonte óptimo. Stops siempre activos. Si no hay quote propia, deuda de tiempo se mantiene hasta siguiente quote. No calendario oro: token PAXG continuo.
Sizing igual en dos espejos: capital=min(wallet,MTM) no negativo,1%trade fijo,8%agregado máximo,4.4xnocionalbruto,90%leveraged_available_margin y step0.0001 existente. Riesgo incluye fees entrada+stop y reserva10bps ida/vuelta sólo sizing; NO slippage simulado. Una ruta, sin pending MARKET ordinarios. Diseño NO listo para cartera sin ledger de reservas compartido antes integración.

Control ResearchPaxgRetestControl4h: copia completa de referencia MultiAssetRetestBtcShort4h con SÓLO class name y TRADE_RISK=.01, ejecutada aislada sobre PAXG4h. Misma lógica/costes/hp defaults. Con una ruta shareATR=1; no representa el tamaño original de cartera ni réplica de contribución4632USD.
Datos/ejecución para tres runs: Binance Perpetual Futures PAXG-USDT4h, data M1 propia, 2020-10-15→2025-12-31 EXCLUSIVO,10000USDT,5xaislado,fee.00045porlado TODASórdenes incluidaLIMIT,modo normal fast=false. Warmup240 actual suficiente para14y80; no cambio global. Sin nuevas fuentes/scripts/instalaciones/framework/live/Pi/2026.

## Presupuesto y decisiones
Máximo3full iniciales: dos hipótesis + control;2simultáneos propios dentro4global autorizados. Cuarto full reservado exclusivamente a robustez de receta prometedora, con protocolo previo; no rejillas ni rescate de1.5/14/2/48 por malos resultados.
Descartar como candidata si neto<=0 o PF<1.2 o muestra<30 o DD>25%; estos son gates descriptivos desarrollo, no validación estadística. Una superviviente requiere evaluación costes/concentración/temporalidad y luego cartera compartida root. No exigir regularidad mensual a cada señal: objetivo65–70%meses/80%q pertenece a cartera. No exigir superar retest en todo para conservar un complemento, pero dos espejos negativos bien diagnosticados cierran ronda sin optimizar.

## Análisis
Completar cada sesión hasta estado terminal y conservar dashboard_url/snapshots. run_analysis con TODOS trades/equity, uno propio simultáneo; wallet/fees reconciliados, gross=net+fees, direcciones, años,holdings/exposición,concentración top3/neto y bps por nocional,break-even fricción extra sobre mismosfills. MTM calendario únicamente con curva UTC correctamente muestreada o auditorV4 root; no realizado por mes de cierre como equity. Estrés estático posthoc es sensibilidad sobre mismosfills, no cartera dinámica. Regularidad no gate señal; reportar sin esconder inactividad. Resultados y descartes persistentes, referencia intacta.
