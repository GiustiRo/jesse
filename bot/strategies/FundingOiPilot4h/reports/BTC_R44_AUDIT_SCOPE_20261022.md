# R44 — alcance de auditoría antes de motores
Protocolo vigente: BTC_R44_INITIAL_RANGE_PROTOCOL_20261022.md. Revalidación: 0 backtests running; padres R11Base1m y R16LegacyBase1m idénticos a snapshots conservados. Dos motores económicos máximos, sólo BTC.
El turno anterior contestó una consulta de alcance y no produjo nueva evidencia económica (clasificación no progreso para el objetivo de búsqueda); se retoma implementación.
Checks supplied-source AST/stubs con arrays fabricados, sin leer datos de mercado/proyecto/DB/red en run_analysis. Fuentes reales leídas por MCP y entregadas como cadenas; no importar estrategias instaladas.
Snapshot financiero posterior: cada trade/orden ejecutada, fee .00045, apertura MARKET inmediata alineada a M1 (no exigir 4h), funding dataset histórico y cashflow reconciliado, ledger wallet/M1/fronteras UTC y cierres terminales nativos.
Replay independiente JS desde resultados MCP: cuotas .5wallet/.5available_margin y legacy_plan congelado, sin capital5k; calendario por fechaUTC/phase, rangos desde dos OHLC4h expuestos, stop extremo opuesto, entradas estrictamente posteriores a formación y anteriores aldeadline, salidas STOP/deadline/FINISH.
La telemetría prebreak (cantidad y min/max previos) permite comprobar invariantes runtime junto a fuente/sintéticos; sin feed completo M1 no afirmar reconstrucción independiente de ausencia de cada ruptura intermedia. Ningún mes/grupo/horario se retirará según PnL.
No estrés de costos/riesgo, nuevos activos/datos/2026, research_scripts, framework/config global, instalaciones o live/paper.
