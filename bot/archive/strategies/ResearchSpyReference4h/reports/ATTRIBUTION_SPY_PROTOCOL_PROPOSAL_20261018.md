# ATTRIBUTION SPY — propuesta congelable antes de código y resultados

Esta tanda es una descomposición de la referencia existente, no dieciséis nuevas ideas. Se propone exactamente 16 fulls aislados, sin barridos ni selección de semilla. Ningún run comienza antes de revisión root de protocolo y código.

## Referencia y paridad

C0 copia íntegra ResearchSpyReference4h excepto nombre de clase AttrSpyC0. La referencia aislada1% es [baseline](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2): 31 trades, net751.3477149671152, fees286.47552620734854, DDmotor−5.2131810594609025. Form leído: SPY-USDT4h, data SPY1m, warmup240, debugfalse, fastfalse, benchmarkfalse, 10000, fee.00045/lado, isolated5x. Debe reconciliar secuencia economicamente equivalente de lados/timestamps/precios/qty/PnL/fees, no UUID. Si falla, no interpretar variantes hasta explicar divergencia. No se modifica la fuente original.

SPY conserva EXACTAMENTE historial UTC Mon-Fri00:00–20:00 y elegibilidad de barras abiertas00:00–16:00 (decisiones04/08/12/16UTC). No se cambia a RTH, no calendario festivo nuevo ni completeness gate adicional. ATR14 por defecto sobre historial filtrado, EMA20/80, ADX14≥26, RSI14 52..76; range usa self.high-self.low de la barra actual como referencia. Stops2ATR, trailing4.2ATR y tightening5R*.78/8R*.62 cuando aplique. Reserva sizing.001, capgross4.4, riesgo1%, cartera8%, margin90%, cantidadstep.001 idénticos.

## Matriz fija

| ID / clase | Entrada | Gestión long | Pregunta |
| --- | --- | --- | --- |
| C0 AttrSpyC0 | LIMIT retest original | Original BE+trail+tightening | Paridad exacta |
| E1 AttrSpyE1NoBE | Original LIMIT | Quitar sólo BE; conservar trail y tightening | Aporte incremental de BE condicionado al trail |
| E2 AttrSpyE2NoTrail | Original LIMIT | Sólo BE2.25R al entry*(1+2.5fee), ratchet original | Aporte incremental trail+tightening condicionado a BE |
| E3 AttrSpyE3InitialStop | Original LIMIT | Stop inicial sin BE ni trail hasta stop o fin motor | Papel de gestión frente a exposición larga persistente |
| E4 AttrSpyE4Stop72h | Original LIMIT | Stop inicial y máximo72h | Gestión frente a horizonte acotado |
| M AttrSpyMarket | Mismos filtros completos y evento breakout; MARKET al close | Original completa | Política retest LIMIT versus entrada inmediata |
| R01..05 AttrSpyR01..05 | MARKET por reloj hash, dentro de régimen original sin Donchian | Original completa | Información adicional del evento breakout/retest sobre régimen |
| U01..05 AttrSpyU01..05 | MARKET por mismo reloj, sin régimen | Original completa | Aporte de seleccionar régimen sobre calendario largo |

Diez relojes no son diez hipótesis nuevas. R/U se emparejan seeds101,202,303,404,505. Todos son long-only en SPY: no aíslan un premio short ni equivalen a beta-neutral. C0-E comparan políticas de gestión; stop distinto cambia ocupación y entradas futuras. M cambia ejecución, precio, tamaño y selección de fills. No se denomina efecto causal puro.

## Precisificaciones recomendadas antes de código

M conserva el umbral Donchian anterior y todas las condiciones originales (entry_channel<price<=entry_channel+ATR), pero después de superar filtros fija plannedentry=self.price. Usa stop2ATR desde fill y riesgo calculado con precio MARKET efectivo; no conserva cantidad calculada con el LIMIT porque introduciría diferencia de riesgo. Tamaño continuo y compounding siguen contrato común.

R conserva régimen price>slow, fast>slow[-1]>slow[-5], ADX≥26, RSI52..76, high-low<=3ATR. Retira ambos predicados del canal (breakout y banda<=channel+ATR), no calcula el canal como filtro oculto. U retira TODO ese régimen, incluidos rango y RSI/ADX/EMA, conservando calendario, historia mínima100=max(80+20,26), ATR finito>0, stop2ATR válido y sizing común. No ampliar historia para ganar datos ni adaptar frecuencia al N observado.

R/U usan SHA256 de texto ASCII fijo 'ATTR_V1|seed|SPY-USDT|closed_candle_open_time'; primeros8bytes big endian como uint64; evento si valor<floor(2^64/48). Es reloj pseudoaleatorio determinista de probabilidad aproximada1/48 por barra elegible, sin Pythonhash, PRNG con estado, precio ni futuro en el payload. Mismo payload R/U, semilla y barra. Se computa en before incluso si hay posición; no se acumula evento ni reintenta tras cierre. R simplemente interseca el evento con régimen y elegibilidad. No se recalibra el reloj a trades efectivos. No se espera igual N entre seeds ni entreR/U por ocupación y régimen.

Fresh quote: C0 y E1/E2/E3 conservan literalmente la referencia (sin guard nuevo, para paridad). MARKET M/R/U necesitan M1 en T−60000 exacto y closeM1==self.price (tolerancia1e−10rel/1e−8abs). Recomendación: ASSERT al intentar entrada que cumpla señal y sizing, en vez de saltar silenciosamente. Si falla es incidencia técnica que se reporta y coordina, no resultado económico, sin completar con stale ni usar otro feed. De este modo no se añade filtro oculto a M ni al reloj. La referencia LIMIT tiene ejecución intrabar distinta, no se presenta como equivalente a MARKET sin evidencia. La auditoría completa contrastará timestamps y órdenes disponibles, sin atribuir fuente upstream real a mera continuidad.

E4 cuenta72h desde position.opened_at efectivo, no arming ni self.time del fill intrabar. Se revisa en cada update_position de ruta4h, sin bloquear por horario; primer tick≥72h marca deuda y liquida al primer quoteM1fresh si faltara. Por tanto72h es plazo contractual, no garantía de fill exacto. Stop inicial siempre activo. No añade TP.

E2 no llama trailing ni tightening; actualiza best_close idéntico a referencia y sólo ratchet al BE cuando mejorclose>=2.25R. Requisito currentstop<newstop<self.price se conserva. E1 quita exclusivamente bloqueBE; E3 sólo no-op gestión long. No se cambian reservas ni ledger.

## Lectura de resultados prevista

C0 contra baseline para paridad antes de inferir. Luego tabla conjunta de16: N trades cerrados, net/fees/gross, PF, DDmotor, duración/exposición en horas y porcentaje de ventana, gross inicial y turnover, net por notional, concentración(top1/3), stress+5/+10bpsRT mismosfills. Cohortes año de cierre se etiquetan como trades, no retornosMTManuales. Ninguna selección de semilla: reportar cincoR y cincoU, mediana/rango descriptivos, paresR-U porseed sin testsIID ni pvalues con5.

Pares de entradas comunes sólo por mismo símbolo/lado y timestamp real de fill exacto, verificando diferencia de precio/qty. Si entrada LIMIT vsMARKET no coincide, no forzar nearest matching. Comparaciones de payoff condicionadas al subconjunto común no explican las entradas excluidas ni reparan sesgo de ocupación; lista y número de pares explícitos. E3 puede mantener primera posición hasta fin y casi eliminar nuevas entradas; eso mide política completa, no debilidad estadística del entry por sí solo.

No se promete regularidad ni nuevo MTM si no hace falta para la inferencia. La pregunta primaria es si el beneficio desaparece al retirar gestión, al cambiar retest o al reemplazar timing por reloj dentro/fuera de régimen. Aun si referencia supera semillas, eso no prueba alpha: misma historia reutilizada, exposición distinta y cinco controles dependientes. No elegir ganadora ni optimizar parámetros en función de resultados.

## Restricciones y trazabilidad

2020-10-15 a2025-12-31 exclusiva, 2026cerrado. Precio proxySPXCFDBID/10 aceptado; funding fuera. Sin BTCaux, framework/live/paper/Pi/scripts nuevos. Fuentes autocontenidas AttrSpy*, snapshotnotes antesrun y readback exacto; reportes ATTRIBUTION_SPY*. Máximo2backtests y1análisis propios. Root debe revisar recomendaciones ambiguas y código antes de iniciar. Todos resultados, incluidos negativos/escasos, se conservan.
