# R36 A — mapa de fuentes y contrato previo

Se leyó completa la fuente vigente BtcResearchR32SpecialistBase1m por MCP antes de decidir herencia. Reutiliza R11 observer y helpers R10/R16; no se modifican padres. R36 sólo define LABEL, HOLD_HOURS=24, TP_R=None y métodos de evento/reloj/telemetría. La fuente financiera del padre ya fue auditada; no se copia ni se altera sizing, on_open, update_position o on_close.

Antecedentes leídos completos por MCP: AngleCombinedBtcWeekend4h, AngleCombinedBtcWeekdayControl4h, ResearchPaxgWeekendReturn1h, ResearchPaxgWeekdayReturn1h, BTC_DISCOVERY_T_PROTOCOL_20261021.md. El listado strategies usado para nombres no estaba truncado. No se inspeccionaron precios ni se importó nada.

Las dos hojas nuevas preservarán estructuras idénticas salvo nombre, etiqueta y weekday del slot: lunes=0 y jueves=3 en datetime UTC. La distancia de formación es 12 barras4h=48h, distinta de la tenencia24h. Ancla [-13], actual[-1]. La decisión usa signo de diferencia de precios; logretorno sólo metadato. Igualdad exacta no genera trade, pero consume slot. Slots inválidos se consumen mediante _invalid_event del padre. R36_SLOT y R36_CLOCK resumen contadores semanales acotados; R32_PLAN/OPEN/CLOSE/SUMMARY y R11 permanecen heredados.

Protocolo guardado antes de fuentes. Tras creación se releerán textos exactos y registrarán SHA256 en recibo de implementación/check. Presupuesto económico máximo2, sin autorización de jobs en esta fase.
