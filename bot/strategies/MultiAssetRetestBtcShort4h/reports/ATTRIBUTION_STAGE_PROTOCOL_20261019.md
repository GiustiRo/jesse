# Atribución de la referencia SPY/PAXG: protocolo global

Investigación autorizada por el usuario tras proponer separar entradas, gestión de salidas y exposición. Inicio entre18/19deoctubre2026. Este protocolo precede a las nuevas ejecuciones. No constituye otra búsqueda de indicadores.

## Preguntas y presupuesto

1. ¿Cuánto cambia la política al quitar break-even, trailing o ambos?
2. ¿Qué ocurre al cerrar a72horas en vez de permitir runners?
3. ¿Qué cambia entre señal con LIMIT de retest y ejecución MARKET, controlando antes la frescura del precio?
4. ¿La señal supera descriptivamente entradas long de reloj fijo dentro de su régimen y entradas long sin ese régimen, bajo la misma gestión?

Presupuesto definitivo:34fulls,17poractivo. No ampliar semillas o escoger la más rentable después de ver resultados. Cinco semillas por grupo sólo dan un rango exploratorio; no permiten inferencia formal de significancia ni crean muestras independientes.

## Matriz común por activo

- C0: copia exacta de la referencia aislada1%, con sólo cambio de nombre. Se exige paridad con la sesión previa antes de lanzar el resto.
- Cq: C0 más guard de cotización fresca exclusivamente para armar entradas LIMIT. No modificar trailing, gestión o stops con ese guard.
- E1: C0 sin break-even, manteniendo trailing4,2ATR y su ajuste tardío en5R/8R.
- E2: C0 sin trailing, manteniendo break-even2,25R.
- E3: C0 sin break-even ni trailing: stop inicial2ATR y liquidación terminal del motor si continúa abierto.
- E4: E3 con máximo72horas desde fill real. Deuda de salida hasta primer tick4h con quote propia fresca; stops siempre activos.
- M: misma señal completa, guard fresco deCq y entrada MARKET al cierre en lugar de LIMIT al canal. Recalcular cantidad con precio efectivo de decisión y la misma distancia inicial2ATR.
- R01..05: long MARKET con reloj causal predefinido, dentro del régimen original de tendencia. Quitar sólo ruptura Donchian y restricción de desviación al nivel; conservar precio>EMA80, EMA20>EMA80>EMA80[-5],ADX≥26,RSI52–76 y rango de vela≤3ATR.
- U01..05: mismo reloj y ejecución queR, sin régimen de tendencia ni filtro de rango. Conservar calendario, historia mínima100observaciones filtradas, ATR válido y sizing común.

Seeds101,202,303,404,505. Para cada vela cerrada, mensaje exactamente ATTR1|{symbol}|{seed}|{closed_candle_open_time}; SHA256, primeros8bytes como entero big-endian, evento si entero%48==0. No incluir clase, grupo, resultados o información futura. AsíR/U del mismo seed comparten calendario potencial, aunque elegibilidad y ocupación produzcan trades distintos. No usar hash dePython o RNG cuyo consumo dependa de posiciones abiertas. No hay replay de eventos ocupados.

Guard fresco común Cq/M/R/U y expiraciónE4: buscar M1 exactaT−60s con searchsorted, precio positivo/finito y paridad con precio de ruta con tolerancia relativa1e−10/absoluta1e−8. Si no se cumple, no armar entrada; una salida vencida conserva deuda. No abortar la simulación sólo por falta de quote. C0/E mantienen su política previa de entradas y gestión; no agregar silenciosamente ese guard.

## Comparabilidad y límites

C0→Cq evalúa el cambio de guard. Cq→M cambia tipo/precio de orden y selección de fills pasivos; M→R cambia la selección de momentos bajo el mismo régimen; R→U retira el régimen. Son contrafactuales de políticas completas con ocupación endógena. Las salidas distintas cambian la disponibilidad para señales posteriores: no se afirma que todas las variantes compartan exactamente las mismas entradas.

No forzar igual duración, frecuencia o capital-tiempo usando información futura. Informar esas diferencias, N, turnover, neto/bruto/fees, DD, holding, exposición temporal y nocional cuando pueda reconstruirse, resultados por lados, concentración y recargos estáticos5/10bpsRT. Normalizaciones descriptivas por turnover o tiempo no crean cuentas operables con exposición igualada.

Cohortes de entradas realmente comunes podrán compararse con timestamps/side y precios tolerados, tamaños normalizados y alcance explícito. Su intersección depende de ocupación y no es un ensayo causal aleatorizado. No confundir el shuffle de trades realizados con el universo de oportunidades no ejecutadas; los snapshots no conservan ese universo completo.

E3 puede sostener posiciones durante años y cerrar sólo por la frontera del motor. Eso es resultado diagnóstico y no validación de liquidez en esa fecha. No promover una variante por ganar con unas pocas exposiciones largas, ni contar años/meses dentro de un runner como observaciones independientes.

## Contrato

Desarrollo2020-10-15 a2025-12-31 EXCLUSIVA.2026reservado y sin consultar. Proxy SPX CFD BID/10 paraSPY y spotPAXG aceptados, sin nuevas fuentes o funding. BTC y referencia original congelados.

10.000USDT por cuenta aislada,1%riesgo planificado,fee0,00045porlado incluidasLIMIT,5xaislado,nocional bruto4,4x,sin piramidado. Reserva10bps exclusivamente en sizing, no slippage simulado. Timeframe4h con auxiliarM1,modo normal,warmup240,debugfalse.

Calendario SPY EXACTO de referencia: barrasMon–FriUTC00–20 para features, ventana de entradaUTC00–16 según apertura de vela. No sustituirlo porRTHNuevaYork. PAXG sin calendario adicional. Gestión/stops activos fuera de ventana de entradas.

Sólo JesseMCP para código, sesiones y reportes; análisis por run_analysis con snapshots completos. Sin scripts de investigación, instalaciones, modificaciones de framework, reinicios, live/paper oPi. Máximo2backtests por especialista/4globales y1análisis por especialista/2globales.

## Puertas de revisión y análisis

Matrices/adendas por activo antes de crear código. Clases autocontenidas AttrSpy.../AttrPaxg...; root revisa fuente común y diferencias, y verifica readbacks antes de primera réplicaC0. RéplicaC0 debe conciliar N, timestamps, lados, precios, cantidades, fees y balances frente a su sesión previa dentro de tolerancias numéricas. Si falla, diagnosticar el problema técnico y no interpretar ablations.

Comparadores previos:
- [SPY aislado1%](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2):31trades,neto751,347715,fee286,475526.
- [PAXG retest aislado1%](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c):35trades,neto546,110572,fee246,608881.

Después de paridad, ejecutar cola fija. No buscar ganadora entre semillas, no cambiarp,seeds, filtros o plazo tras resultados. Analizar distribución descriptiva por grupo y paresR/U, no sólo máximos. Registro acumulado de selecciónR20/R40anterior permanece; no esOOSlimpio.

Si se informa regularidad, root reconstruye MTM diarioUTC desde fills y precios anclados; Portfolio00:01 y cohortes de cierre no se usan como cierres diarios o retornos mensuales. Ningún resultado de esta etapa certifica mejora futura. El entregable es una atribución defendible de la evidencia disponible y sus límites, más un contraste adicional acotado sólo si los hallazgos lo justifican.
