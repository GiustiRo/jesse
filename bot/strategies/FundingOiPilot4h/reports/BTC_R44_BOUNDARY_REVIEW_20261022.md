# Revisión independiente previa R44
Revisor creative_next_axis leyó protocolo completo y jesse://strategy/TradingHours. Sin objeción bloqueante al diseño; revisión de fuentes aún pendiente.
Casos exigidos al harness: apertura de vela M1 determina ancla, incluidas fronteras mensuales/anuales y fines de semana; fase00 08:00 forma pero no entra y08:01 es primera elegible, fase12 20:00/20:01. A00:00/12:00 el ciclo anterior vence, la siguiente marca inicia nuevo ciclo.
Dos4h exactas sin anticipación: futura extrema u otra historia no cambia niveles. Ausencia/duplicado/desplazamiento/OHLC/paridad/rango0 descartan formación sin rescate posterior.
Igualdades y mechas no consumen; primera ruptura estricta consume una sola oportunidad total aun con cuenta ocupada, margen insuficiente o qty0. No reaparece después de stop.
Rango90–110: long111 stop90/D21; short89 stop110/D21; precio actual MARKET sinTP niATR. Cuota .5wallet/.5available_margin sin redistribución y lote.001.
Entrada deadline−1m válida; deadline inválida; hold máximo15h59m. last_exit_at bloquea mismo minuto. position_plan sobrevive a cambio de ciclo; gestión/stop fuera de ventana activos.
Primer ciclo anteriorSTART omitido; último parcial permitido. FINISH prioriza cierre terminal nativo. Contadores de cierres y fees antes de FINAL.
Esta revisión documental no equivale a ejecutar estos casos ni a aprobar rentabilidad.
