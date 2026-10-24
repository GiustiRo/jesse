# Tanda N: composición de señales congeladas en un único libro BTC

## Pregunta y selección reconocida
¿Se pueden aprovechar oportunidades de amplitud de signos y de impulso horario que ocurren fuera de la ocupación de la otra receta, manteniendo una única posición BTC y el mismo riesgo? Se prueban dos políticas de composición prefijadas; no se suman curvas de capital ni se compone un PnL desde trades independientes. Los padres se eligieron retrospectivamente entre recetas positivas de un histórico ampliamente examinado. Esta selección adaptativa no es OOS, prueba independiente ni validación por consenso.

Se conservan antecedentes de convivencia/suplementos R6 y ORCH; la composición no es una familia recién inventada. La información nueva es la ocupación y arbitraje de ESTAS máquinas congeladas A/B/F en UN libro, con tamaños dependientes del mismo capital. No se cambian umbrales, entradas o gestiones para rescatar numéricamente A–F.

Controles existentes reutilizados, no reejecutados por N:
- MCP Backtest: BTC discovery A | BtcResearchR10Breadth4h
  Dashboard: http://localhost:9200/#/backtest/438b717c-7b5e-4589-a84a-687fa63f8645
- MCP Backtest: BTC discovery B | Breadth state exits
  Dashboard: http://localhost:9200/#/backtest/62c90517-9034-4b34-91af-f77457895157
- MCP Backtest: BTC discovery F | BtcResearchR12JumpFollow1m
  Dashboard: http://localhost:9200/#/backtest/8b78a705-a8f3-4656-9705-e56300623ddf

Análisis de intervalos ac045e27ac7a4c7d97bd6f2507771464, snapshots completos193A/102B/381F, muestra330entradasF fuera de A,188 fuera de B,119A fuera de F y60B fuera de F; coincidencias al mismo cierre12A/F y7B/F, todas alineadas. Son fills realmente ejecutados standalone, no todas las señales bloqueadas ni oportunidades contrafactuales de la unión. No permiten sumar PnL, asumir ausencia de conflictos nuevos o estimar trayectoria conjunta. El diagnóstico motiva un backtest nuevo de composición, no anticipa su resultado.

## Dos políticas y máquinas congeladas

CORE usa exactamente breadth_signal de BtcResearchR10Base4h sobre26 cierres4h. EstadoCORE usa breadth_state sobre25cierres: al menos4/6 y16/24 cambios del mismo signo; ceros no votan. F usa exactamente jump_state y closed_hours de BtcResearchR12JumpBase1m:24logretornos1h, RV/BV con corrección24/23, J>=1/3 yabs(net)>=.5ATR4h/precio; estado=signo neto, evento al cambiar a estado no nulo distinto.

Cada cierre4h se calculan AMBAS máquinas aun con posición abierta. Se actualizan estados antes de comprobar ocupación; los eventos bloqueados se descartan, no se encolan. Ventanas exactas y consecutivas26×4h y25×1h, ambos cierres alineados con precioBTC actual. Si falta4h válida, reiniciar ambos estados a0; si4h es válida pero falta1h, conservar el estadoCORE calculado para permitir la salida B por estado opuesto, reiniciar F a0 y bloquear nuevas entradas. No puentear huecos. Los contadores de eventos/arbitraje se refieren a cierres con ambas ventanas válidas. ATR14simple4h actual y las fuentes/helpers congelados se conservan.

Plano: una sola señal entra con su origen; si las dos coinciden en dirección, se fusionan en UNA entrada de origenCORE; si discrepan, CASH. Esta regla común queda fijada antes de resultados. Ocupado o con entrada pendiente: descartar ambas, sin reversión ni reentrada en el cierre de una salida. La coincidencia no implica dos órdenes o riesgo4%: una posición con objetivo2% TOTAL. No prioridades alternativas, pesos, votación aprendida ni decisión de gestión por rendimiento posterior.

FIXED: CORE reproduce A y IMPULSE reproduce F, todos stop2ATR/TP2R/48h. STATE: si origenCORE, gestión B exacta: stop2ATR,sinTP,max180barras4h=720h o salida al estadoCORE opuesto; si origenIMPULSE, gestiónF exacta stop2ATR/TP2R/48h. No modificar una posición por señales del otro componente. Se conserva además la guarda de admisión heredada R10 price+direction×2×distance>0, incluso para CORE/STATE sinTP: no crea una orden de beneficio. El origen y la gestión se fijan al fill y no cambian mientras se sostiene la posición. El estado de la máquina no se congela durante esa ocupación.

## Ejecución, costo y medición

BTC-USDT Binance Perpetual Futures, ruta1m observador/ejecución y datos4h+1h; warmup2404h. Ventana[2020-10-15,2026-01-01)UTC, desarrollo observado;10k,2%portrade/6%agregado/3xaislado. Entry_plan R10 fee-aware congelado, margen90%,floor8, distancia inicial2ATR14simple4h. Una posición sin pirámides; funding/gaps pueden superar la pérdida prevista. MARKET al cierre conocido, protecciones M1, gestión en cierres4h.

Fee.00045porlado, taker con descuento según supuesto del usuario; fundingBTC histórico ON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcasproxy declaradas, slippage modelado0. Sin estrés, variantes de riesgo, nuevas pruebas económicas2026, importaciones, ML, research_scripts, instalaciones, reinicios, configglobal, live/paper oPi. Ningún resultado de N autoriza operar ni estrés automático.

ObservadorR11 congelado: wallet+PnLabierto cadaM1/fill, fronteras00:00UTCpostfunding/predecisión según convención por fase, no agrupación estricta de eventos por mes; DD M1+ejecuciones no todos los extremos intraminuto. Instrumentar origen en plan y fill, fills/closes/net porCORE eIMPULSE con closed_trade.pnl. El ledger de cierre debe actualizarse ANTES del callback R11, para que FINAL incluya liquidación terminal y comisión. Después del resumen R11, emitir R14_COMPOSITE_STATS con ambos eventos frescos/transiciones consumidas, coincidencias/conflictos, descartes porocupación y ledger. No emitir logs porcadaM1 ni inferir fills desde admisiones.

## Presupuesto, puertas y cierre

Exactamente dos corridas económicas nuevas: FIXED y STATE. Hasta dos reemplazos sólo por errores técnicos documentados; no porPnL. No barrer prioridad, simultaneidad, plazos, gestión o vecinos después de N. Máximo dos motores globales y un análisis propio. Los controles previos son reusados con sus límites; no sumar como económicas nuevas.

Gatesr9 intactos: CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,mediana mensualcalendario>0 incluyendo inactivos,neto aritmético quitando los dos mejores meses>0. N>=100 preliminar operativo no potencia/confianza por conteo; aspiraciones40–50%+/M70. Cada composición debe cumplir por sí misma, no sólo superar un padre. Si falla economía NO_CUMPLE; si economía favorable pero falta medición/muestra INCONCLUSA.

Antes de economía: AST y checks con código suministrado/stubs, causalidad helpers, arbitraje solo/alineado/conflicto, ambas máquinas avanzan aunocupado, política congelada de origen2R/sinTP/48h/720h/opuesto, no pirámide, reset de huecos, riesgo fee-aware y orden ledgerantesFINAL. Readbacks/hashes y revisión separada; manifiesto con formularios reales antes de motores. No crear sesiones o resultados ficticios en preparación.

Después: auditoría de snapshots completos bruto−fees+funding=PNLsum=equityfinal−10k a1e−6USDT; suma ledgerCORE/IMPULSE reconcilia N yPnL de todos los trades, incluido cierre terminal. Verificar2.741.760marcasM1,63intervalos/62meses/20Q,fronteras y contribuciones. Conservar todas las pruebas/errores y reportesMCP; Hub inmutable archivosprimero/índiceúltimo. Si falla, cerrar este presupuesto y continuar otra pregunta material de forma autónoma, sin relajar objetivos ni atribuir éxito a una suma de curvas.
