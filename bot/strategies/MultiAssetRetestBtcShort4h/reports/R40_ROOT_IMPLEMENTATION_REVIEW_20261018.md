# R40: revisión de root antes de ejecución

Veinte matrices y señales revisadas; diez clases autocontenidas por activo. Los especialistas no iniciaron sus primeros pares hasta la aprobación correspondiente. Toda modificación de diseño se hizo antes de resultados de esa fila.

## PAXG
Matriz en strategies/R20PaxgARResponse4h/reports/R40_PAXG_TEN_EXPERIMENTS_PROTOCOL_20261018.md y revisión en strategies/R40PaxgKalmanInnovation4h/reports/R40_PAXG_IMPLEMENTATION_REVIEW_20261018.md.

Root examinó el motor común y las diez señales. Confirmó 62 precios para sesenta retornos anteriores excluyendo el actual en Kalman/CUSUM; innovación Kalman predictiva anterior a update; labels estacionales contiguas close-to-close asignadas por apertura UTC, ranking diario congelado; ajuste espectral pasado y proyección de seis barras; ATR anterior a ventanas de mechas/centros; KAMA y salida contraria; agregados diarios/semanales completos con lunes UTC; episodios sin replay; beta con sesenta fijaciones anteriores y parámetros de salida congelados. Las etiquetas o parámetros aprendidos no implican muestras independientes ni cointegración.

Dos correcciones previas a ejecución: TP Kalman en nivel absoluto congelado, y entrenamiento estacional busca noventa muestras válidas por franja sin un límite arbitrario de650barras. Las fuentes definitivas de las diez clases se leyeron por MCP. Prefijo común normalizado y diez bloques coinciden exactamente con el informe actualizado.

## SPY
Matriz SPY40_MATRIX_PROTOCOL_20261018.md, revisión SPY40_IMPLEMENTATION_REVIEW_20261018.md y precisiones SPY40_IMPLEMENTATION_CLARIFICATIONS_20261018.md bajo strategies/ResearchSpyReference4h/reports/.

Root examinó el motor común y las diez señales. Verificó bloques2h independientes desde09:30NY, no candles2hUTC; diarios con13barras30m completas; ATR de sesiones previas; bandpass con snapshots de últimos valores observados; entropía ordinal con empates excluidos; labels maduras en OLS/run; ratio de varianzas con veinte intervalos y rangos anteriores; semana completa civil; bins causales de65closes; dos tests con ruptura futura y niveles consumidos. La omisión de overnight en el rango pero inclusión en close-to-close es parte explícita de la hipótesis06, no una igualdad estadística supuesta.

Se corrigió antes de ejecución el funcional RV/BV: trece incrementos de una partición de precios desde apertura hasta los trece cierres, incluyendo uniones entre barras. No se trata como test asintótico formal con trece datos. Referencia matemática: [Barndorff-Nielsen y Shephard](https://shephard.scholars.harvard.edu/sites/g/files/omnuum7741/files/power.pdf). La construcción ordinal se inspira en [Bandt y Pompe](https://doi.org/10.1103/PhysRevLett.88.174102), sin inferir una ventaja de trading de su definición.

Root leyó las diez fuentes completas por MCP y comparó cada una con motor más señal del informe: igualdad20/20 en total entre ambos activos. No se añadieron logs diarios ni hooks finales no documentados; debug_modefalse. Los snapshots no exportan vars ni contadores internos, por lo que los trades no prueban todos los estados u oportunidades ocupadas.

## Motor y contrato
Entradas MARKET con quote M1 fresca y paridad de precio, sizing1% con fees/reserva y techo4,4x, sin piramidado. Targets absolutos o distanciasATR según receta. Stops y gestión permanecen activos fuera del calendario de entradas. Las deudas de salida por señal o tiempo se conservan hasta quote fresca y reinician al nuevo fill. No hay helpers de proyecto mutables omitidos de strategy_codes.

Se conservan las recetas fijadas después de observar resultados. Los primeros fulls verifican ejecución real, no se sustituyen por una validación superficial de sintaxis. No se añadieron tests de framework ni se modificó éste. Cualquier error técnico posterior se registrará por separado de un fracaso económico.
