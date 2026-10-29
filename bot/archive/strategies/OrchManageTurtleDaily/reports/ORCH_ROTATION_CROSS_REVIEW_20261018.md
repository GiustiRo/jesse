# Revisión cruzada de rotación mensual — solo lectura
Fecha: 18 de octubre de 2026.
Fuentes leídas por MCP: OrchRotateMonthlyMomentum4h y strategies/OrchRotateMonthlyMomentum4h/reports/ORCH_MONTHLY_ROTATION_PROTOCOL_20261018.md.
No se modificaron fuente, protocolo ni sesiones del otro agente. No se evaluó rendimiento ni se lanzó control.

## Causalidad de datos y reloj
La observación de cada ruta exige un minuto propio cerrado exactamente en el callback, con paridad numérica entre su cierre y el precio4h. La búsqueda binaria ignora minutos formándose.
El ranking toma únicamente timestamps comunes estrictamente anteriores a closed_candle_open_time, por lo que no incorpora la ruta extranjera parcialmente actualizada al mismo timestamp. El anchor es una observación anterior o igual a la fecha de tres meses calendario atrás, con lagmáximo7d.
El primer ranking mensual espera una observación común dentro de ese mes, normalmente el segundo día de callbacks elegibles. La entrada espera otro callback propio posterior: normalmente como mínimo el tercer día. El protocolo declara este retraso; no hay fill retrospectivo.

## Historial inicial y selección
Las observaciones arrancan en el período observado, sin bootstrap4h supuesto fresco. La falta de tres meses de historia implica cash mensual; el ranking no reintenta dentro del mes. Con inicio a mediados de octubre, enero puede seguir sin anchor suficientemente antiguo y la primera elegibilidad podría llegar en febrero2021. Esto es una cota conceptual del código, no fecha real observada: comprobar fills antes de informarla.
Cash y meses cero permanecen en el calendario; no seleccionar desde la fecha del primer ganador para borrar startup.

## Salida propia, deuda y entrada siguiente
Cada ruta liquida o cancela únicamente órdenes propias. exit_pending persiste mientras exista posición o entradaACTIVE/QUEUED, y se limpia tras observar desaparición real. Las guardas globales de is_open/pending y time>rank_time impiden que una ruta nueva use una limpieza temprana para solaparse.
entry_used se consume en go_long y también queda activo al mantener el mismo ganador en el nuevo ranking. Si luego ejecuta stop, no puede reentrar en ese mes; espera el siguiente ranking.
El stop inicial y las revisiones posteriores usan precio propio fresco. La revisión mensual del ganador mantenido solo eleva protección.

## Conclusión y límites
No se identificó un fallo concreto de causalidad, solapamiento ni reentrada entre el código y el protocolo. Es una revisión estática, no prueba formal ni certificado de ejecución. Las aserciones del run y el auditor de ejecuciones deben confirmar el comportamiento registrado.
El reloj fijo16UTC no equivale al cierre de NY; está declarado como reloj común. Las cotizacionesBID del CFD y PAXGSpot no garantizan fills/funding nativos. Los rank_records pueden no estar exportados: no inventar sus tiempos exactos.
No se toca2026, framework, configuración global ni live.
