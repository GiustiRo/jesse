# Estructura y probabilidades: protocolo independiente previo a datos
2026-10-18. Hipótesis: el orden causal de pivots confirmados 1D/4h aporta información incremental sobre la próxima primera barrera ±ATR14/24h, incluso frente a una tendencia diaria mínima. Causal significa disponible en ese instante; no identifica causas económicas.

Referencia inmutable [dashboard](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb): MultiAssetRetestBtcShort4h, CAGR28.83%, DD14.89%, 33/61 meses activos y15/21 trimestres positivos. Meta65–70%/80% sin rebajar; este experimento predictivo no mide esos objetivos. Sin trading/backtest, riesgo/costes/baseline inalterados, sin2026 ni datos externos.

## Contrato y evidencia de controles
Leído entero el prototipo previo research_scripts/portfolio_roles/causal_multiscale_observer.py; no se modifica. Job4c55194e27aa4907ac24451084d37d97 succeeded, 13 controles sintéticos PASS, ninguna query de datos/red/trading. Signature pública get_candles confirmada; __doc__ ausente. Antes del fullrun se prueba semántica de tupla/límites con una consulta pequeña acotada a2020. Nunca source introspection, SQL, secretos, env ni instalación.

## Diseño fijado antes del adapter/fullrun
Datos sólo BTC-USDT Binance Perpetual Futures almacenados, origen2020-10-15 a fin exclusivo2025-12-31;40d previos para ATR/pivots sin labels ni entrenamiento de warmup. Resolución M1 y agregación4h/1D completa UTC. ATR14 Wilder inicial mediaTR14; primeras TR high-low; gaps reinician ATR.

Pivots high/low estrictos 2izquierda/2derecha confirmados al cerrar segunda barra derecha, sólo ventanas contiguas; ties/outside dual se descartan. Dos highs y dos lows por escala determinan up/down/range. U si ambas up,D si ambas down,M si ambas disponibles restantes,unknown si faltan. Conservar tiempo de extremo/confirmación sin repintar. Tendencia mínima: signo de diferencia de los dos últimos cierres diarios completos;unknown si no hay dos días consecutivos.

Cuatro modelos simultáneos fijados, sin selección de ganador para trading: climatología p0; tendencia diaria; pivots; pivots condicionados adicionalmente a tendencia. Ventana180d por origen, Dirichlet1 en p0, shrink20 contra p0 para tendencia/pivots, y shrink20 contra tendencia para combinado. En pivots unknown, pivots=p0 y combinado=tendencia. No grid de hiperparámetros.

Cada cierre4h emite distribución up/down/none sobre barreras close±ATR14 y horizonte24h. Sólo M1 futuras [T,T+24h). Open fuera de barrera resuelve primero; open dentro con ambas mechas tocando es ambiguous; no inventar orden. Exigir horizonte íntegro de1440min incluso resuelto temprano, fijado antes de ver scores. Gaps/invalidación excluyen mismo episodio en todos modelos. Ambiguous no entrena ni inventa none; producir bounds pareados up/down. Right-censored sin madurar no entrena/puntúa. Todos los labels sólo actualizan al deadline, aun toque temprano. Un nuevo forecast puede usar labels con deadline exactamenteT.

## Evaluación
Scores prequentiales guardados al emitir, mismos episodios admisibles para todos modelos. Global incluye unknown y arranque. Brier multiclase y logloss, comparación pivots−p0 y combinado−tendencia; también tendencia−p0. Reportar año/estado/soporte, distribución de clases, cobertura por motivo/año/estado, bins fijos5 de calibración por clase, bounds ambiguos y cohorte00UTC con horizontes24h no solapados. Sin inferencia IID: hasta6 horizontes superpuestos y estados persistentes. Un promedio pequeño no demuestra información. Nada de aciertos aislados, gates de PnL o argmax para trading.

Resultado favorable requeriría mejorar ambas scoring rules frente a tendencia además de p0, estabilidad temporal sin un año dominante, soporte/cobertura razonables y robustez a ambiguous. Si falla, archivar este recipe sin aflojar reglas después.2020–25 ya explorado; cualquier resultado es desarrollo adaptativo, no OOS limpio.

## Críticas previas
Últimos pivots pueden quedar obsoletos tras gaps; registrar edad/última confirmación y cobertura, sin ajustar umbral luego. Las etiquetas first-touch24h no representan payoff de retests multiday ni garantizan regularidad mensual/trimestral. Una climatología es un benchmark demasiado débil para atribuir valor a estructura; se añade tendencia simple antes de resultados. Exigir cobertura íntegra evita reglas dependientes del outcome, pero condiciona población a disponibilidad de datos y puede inducir selección; cuantificarla, no llamarla imparcial.
