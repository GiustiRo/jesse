# SPY — exposición lenta defensiva, protocolo previo a dos fulls
Fecha local18oct2026. Root autoriza dos fulls adicionales tras archivo de apertura. Historial amplio adaptativo2020–25, sin OOS limpio. Las familias de tendencia/rotación ya se estudiaron; no presentar esta adaptación como mecanismo jamás visto ni usar paper como prueba de edge propio.

## Pregunta económica
Capturar prima direccional de precio del índice a horizonte lento, reduciendo exposición en deterioro persistente, frente a mantener beta con idéntica protección de cola. No seleccionar dirección intradía. Antecedente conceptual consultado por root: Faber, https://mebfaber.com/timing-model/ y https://mebfaber.com/2017/12/13/episode-86-quantitative-approach-tactical-asset-allocation/ . Nuestro método200observaciones no replica10mesesSMA ni su instrumento/precio/calendario.
Diferencia frente OrchRotateMonthlyMomentum4h: aquí SPY independiente y largo/cash; no elección relativa entreBTC/PAXG/SPY por retorno3meses. El control beta permite identificar si un resultado sólo refleja mercado alcista y protección/riesgo.

## Reglas congeladas H2/C2
Binance Perpetual Futures SPY-USDT; proxy aceptado. Ventana2020-10-15→2025-12-31exclusivo;10k,5xisolated,.00045porlado,1%riesgo inicial con fees y10bps reserva sizing;gross<=4.4. Sin funding ni2026.
Reloj observado16UTC: callback4h12:00→16:00 Mon-Fri, quoteM1 exactamente fresca y close igual a self.price. No es cierreNYSE. Registrar una observación real porfechaUTC, sinimputarholidays/gaps. Filtrohorario e historia de señal coinciden.
Acumular200observaciones diarias propias durante desarrollo; startupcash visible. Primerreview mensual válido después de tener200observaciones, luego primer16UTCfresh de cada mes. Se consume revisión aunqueposiciónheld/cash: trasstop no reentrar hasta siguiente mes.
H2 ResearchSpySlowDefense4h: enreview, entrarMARKET siquote>SMA200observaciones; liquidar siquote<=SMA. Media incluye quote ya cerrado y conocido. No nueva entrada entre reviews.
C2 ResearchSpySlowBeta4h: igualreloj/historia mínima/stop/sizing; ignora condiciónSMA, mantieneposición mientras no stop; sólo entra si estáflat enreview.
Ambos: stop inicial10% del fill; ratchet mensual a90%quote sólo si eleva stop, nunca aflojar; sinTP/BE/rebalanceqty. Sólo una posición; stop activo24/7. Gestión discrecional necesitaquote propiafresh, deuda de salida si falta. No anticiparfrontera final; cierreterminal motor etiquetado.
Riesgo1% con stop10% implica nocionalaprox0.0982x al entrar: exposición deliberadamente baja. No extrapolar rendimiento a1x incompatible con límite de riesgo ni subir tamaño para rescate.

## Evaluación
Dos fulls y sin rejillas, vecinos ni umbrales posthoc. Código independiente sólo nuestras estrategias/reportes, snapshots ennotas. Comparar neto,CAGR/DDMTM, costes, exposición, concentración y años sobre cuenta entera incluyendo startupcash. No exigir50trades a sistema lento: pocastransiciones significan incertidumbre alta e incapacidad de validación estadística. No llamaralpha al retorno beta. Si filtro no mejora defensividad ni eficiencia frente C2, archivar filtro; si ambos sólo replican beta protegida, dejarlo explícito. No integracióncartera hasta revisiónroot y simulacióncompartida propia. No sumarcurvas.
V4 root reconstruyeMTM con anclas yfills; no regularidad por mes de cierre ni00:01motor. Shock de costes estático sobrefills es diagnóstico, no nueva simulacióndinámica. Referencia inmutable.