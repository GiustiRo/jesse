# Portfolio — captura diagnóstica adicional, sin nuevas variantes

Después de terminar CONTROL/A, get_session_results(section=logs) devuelve available=false y No log file exists. get_backtest_session y estado persistido tampoco contienen los contadores; la cadena PORT_CAPACITY aparece sólo en código/notas, no es evidencia de valores. Los snapshots run_analysis no incluyen vars/logs.

Para cumplir el diagnóstico de límites se repetirán exactamente las cuatro configuraciones con debug_mode=true, fastfalse y todas las señales/salidas/fuentes/configuración económica iguales. Son cuatro réplicas diagnósticas adicionales, no cuatro hipótesis ni evidencia estadística independiente. No se usa su rendimiento para seleccionar otra receta. Primarias conservan debugfalse y siguen siendo las cuatro filas de comparación.

Antes de aceptar contadores se verificará identidad de todos los trades económicos y curvas entre primaria y réplica, excluyendo IDs. Si divergen o no se guardan logs, declarar Missing Data, sin tocar framework ni inventar recuentos. Logs se leerán por MCP al final y reportarán los tres JSON PORT_CAPACITY por cartera. Dos slots globales; esperar B/C primarias antes de arrancar las réplicas.

No se editan fuentes ni configuración global. No se abre2026 ni se amplía ventana. Motivo de repetición: información diagnóstica requerida no persistió en modo normal; prueba de equivalencia necesaria y acotada. En total cuatro variantes económicas, ocho ejecuciones full si terminan las cuatro réplicas.
