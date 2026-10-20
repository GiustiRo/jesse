# X03 costes R2 — implementación congelada — 2026-10-19

Leído X03_R2_FROZEN_PROTOCOL_20261019.md antes de crear fuentes. Cuatro estrategias autocontenidas creadas por Jesse MCP, todas leídas de vuelta. Sin drafts, backtests ni análisis iniciados por este agente a esta altura. QA sintética pendiente de slot root.

| Fuente | Cambios funcionales respecto BtcExploreR103 |
|---|---|
| X03CostR201 | before: gate posterior al latch base y geometría original, ATR >= 4*(2*.00095*C). Cuenta rechazos; no rearma al cruzar gate. |
| X03CostR202 | before: retest VWAP congelada, stop absoluto origen y distancia nueva1..3ATR; evento lleva planned_entry. _explore_size: usa ese entry para todos los mismos cálculos de sizing/reserva. SELL existente manda LIMIT por precio encima de mercado; cancelación heredada unabarra. |
| X03CostR203 | before original renombrado _cost_source_event añade V/ATR/stop/due_clock. Wrapper before consume pendiente una vez, descarta reloj distinto/ocupación/órdenes activas/datos inválidos/confirmación fallida. Requiere C_u<V y ATR_origen<=S_origen-C_u<=3ATR_origen; target2d. _signal original conserva prioridades. |
| X03CostR204 | _explore_size valida target neto positivo bajo entry previsto. on_open_position recalcula target una sola vez al fill real sólo en rama suplemento. Helper _cost_net_target resuelve reward neta=2*pérdida stop neta con proxy .00095 por lado. |

Las cuatro sólo cambian ID de receta en eventos/logs y nombre clase además de los métodos anteriores. Helper ledger, capital, committed, volshare, planes long y short originales, riesgo y gestión original conservados. reserve .001 sólo sizing, fee_rate motor se usa en sizing sin hardcode. .00095 es proxy económico fijo en K201/K204 y no sustituye comisiones reales.

K202 mantiene protección relativa a actualfill usando distancia congelada al precio previsto, según protocolo; no infiere que LIMIT llena sin selección adversa y no concede descuento maker. K203 vigila ocupación en before para no admitir una señal cuya posición se cierra más tarde en update_position del mismo ciclo. Nuevos orígenes avanzan siempre; un evento confirmado nunca espera otro cierre.

En readback de implementación se detectó un reemplazo de texto inicial K204 en _short_plan; se corrigió antes de cualquier ejecución y el método original quedó exacto. No se considera resultado ni iteración económica.

Pendiente: root lee fuentes; QA sintética de cronología/expiración/prioridad y fórmula neta; sólo tras ticket root se crean y ejecutan pares B/C. Root centraliza MTM/calendario/fricción: este agente no duplica esas auditorías.


Actualización: root leyó las cuatro fuentes; QA final c784bcf7c3bc4c70b5017ece7864a1ac succeeded140checks. Ver X03_R2_COST_STATE_QA_20261019.md y X03_R2_COST_QA_SOURCE_20261019.md. Espera ticket para drafts/runs.
