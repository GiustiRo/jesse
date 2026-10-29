# Tanda M: aprender respuesta según avance y recorrido

## Pregunta y comparación previa
¿La geometría de una vela —cuánto avanzó el cierre frente a su true range— permite aprender una respuesta de continuación o reversión mejor que aprender una única respuesta global? Dos políticas prefijadas, COND y GLOBAL, comparten fechas, validez, protección y costos. Es una tabla de dos medias con etiquetas maduras; no se agregan modelos, librerías ni búsqueda de hiperparámetros.

Antecedentes leídos: R20PaxgPathAnalogue4h usa forma de ocho retornos, veinte vecinos y retorno futuro de seis barras; R40SpyRunDurationResponse aprende respuesta por signo/duración de racha con252 etiquetas y shrink20. FreshStructureProbability archivó pivots1D/4h y etiquetas first-touch±ATR/24h tras empeorar scores; M no rescata esa receta, sus parámetros ni convierte sus probabilidades en órdenes. La representación, el target de retorno y el control de M son distintos. Causalidad aquí significa disponibilidad temporal, no mecanismo económico demostrado. El histórico2020–25 sigue ampliamente explorado; no es OOS nuevo.

## Ventana, geometría y etiquetas
Cada cierre4h T usa exactamente las últimas367 barras OHLC cerradas consecutivas, índices0..366. Los360 orígenes de entrenamiento son i=1..360. Cada uno tiene cierre previo i−1 y target i+6, índices7..366 ya conocidos en T. No se incluye una etiqueta del origen actual366 ni se espera un target futuro para decidir.

TR_i=max(H_i−L_i,abs(H_i−C_(i−1)),abs(L_i−C_(i−1))). E_i=abs(C_i−C_(i−1))/TR_i. Bin1 si E_i>=0,5; bin0 si E_i<0,5. Etiqueta madura: sign(C_i−C_(i−1))*log(C_(i+6)/C_i), retorno24h relativo a seguir aquella vela. Se excluyen orígenes con TR0 o cambio de cierre0; la ventana sigue siendo de360 orígenes temporales, no se amplía hasta obtener360 válidos. Horizontes solapados y persistencia de estados no son réplicas independientes.

La barra actual debe tener TR>0 y cambio de cierre distinto de0. Ambas políticas exigen al menos30 orígenes válidos del bin ACTUAL; este requisito común evita cambiar el universo admisible al comparar modelos. COND usa la media de etiquetas de ese bin; GLOBAL usa la media de todas las etiquetas válidas de los mismos360 orígenes. No shrink, ponderación, selección de ventana, reentrenamiento retrospectivo o cambio de bins.

Si media>0,0019 seguir signo del cambio actual; si media<−0,0019 revertirlo; resto cash. El umbral es de admisión heredado de antecedentes, no un costo añadido, slippage ni estrés simulado. El pronóstico describe retorno sin protección; el backtest evalúa su payoff real con stop, costos y ocupación. Es estimación online causal dentro de una trayectoria continua, no un walk-forward seleccionado al final. Las etiquetas que terminan en el cierreT pueden utilizarse desde ese cierre ya observado.

## Ejecución y presupuesto
Exactamente dos corridas económicas, una por política; hasta dos reemplazos sólo por fallos técnicos documentados, nunca por PnL. Sin vecinos ni barrido de bins, horizonte, ventana o hurdle tras resultados. Máximo dos backtests globales y un análisis propio simultáneo. Preparación no inicia ningún backtest; manifiesto y formularios se guardarán antes de ejecutar.

MARKET al cierre4h observado, stop2ATR14simple4h actual congelado, sinTP, salida24h desde fill en cierres4h. Evento evaluado cada cierre aun ocupado, descartado sin cola; sin reentrada en el mismo cierre de una salida. Una posiciónBTC sin pirámides. Reutilizar base AR R12 congelada para stop/salida24h y observadorR11, no su pronóstico AR. SizingR10 fee-aware,2% objetivo por trade,90% margen,floor8; gaps/funding pueden superar la pérdida prevista.

## Contrato fijo y puertas
BTC-USDT Binance Perpetual Futures, ruta1m observador y datos4h. Warmup400 barras4h para367 de lookback; adaptación técnica de suficiencia, no selección por resultado. Ventana[2020-10-15,2026-01-01)UTC,10k,2%/6%/3x aislado,fee0,00045 porlado, fundingBTC histórico ON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcasproxy declaradas,slippage modelado0. Sin estrés, variantes de riesgo, nuevas pruebas económicas2026, imports, research_scripts, instalaciones, reinicios, configglobal, live/paper oPi.

ObservadorR11: wallet+PnLabierto cadaM1/fill; fronteras00:00UTC después del funding y antes de decisiones según convención por fase, no agrupación estricta de eventos por mes. DD M1+ejecuciones no todos los extremosintraminuto. Gatesr9: CAGR>=30%,PF>=1,2,DD<=25%(objetivo20%),M65 activos,Q80 completos,mediana mensualcalendario>0 incluyendo inactivos,neto aritmético quitando dos mejores meses>0. N>=100 es suficiencia operativa preliminar, no potencia/confianza por conteo. Aspiraciones40–50%+/M70. Cada política por separado; superar control no basta. NO_CUMPLE al fallar economía; INCONCLUSA si economía favorable pero falta muestra/medición. Pasar base no autoriza operar ni estrés automático.

## Verificación y cierre
AST y checks sintéticos de360 orígenes/etiquetas maduras, índices y oráculo independiente, bins/control, ceros, signo de media, exclusión de etiqueta actual, invariancia a historia más vieja, asof/futuros y sizing heredado. Readback/hash completo y revisión separada antes de economía. Se registran intentos y fallos técnicos; no resultados económicos ficticios. Contextos de admisión y contadores de fills follow/fade se guardan como diagnóstico, no selector retrospectivo.

Después: auditoría completa bruto−fees+funding=sumaPnL=equityfinal−10k a1e−6USDT; coberturaM1, fronteras y meses reconciliados. ReportesMCP yHub inmutable, archivos primero/índice al final. Si falla, cerrar las recetas y continuar con otra pregunta material dentro de la autonomía vigente, sin rebajar puertas ni rescatar vecinos.
