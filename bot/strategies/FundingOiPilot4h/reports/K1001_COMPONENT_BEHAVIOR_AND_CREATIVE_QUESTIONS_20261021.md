# K1001 — preguntas para entender sus tres comportamientos
Fecha local: 2026-10-21. Documento de preguntas y lectura de fuentes, sin protocolo experimental. La última instrucción humana es ENTENDER K1001 mediante preguntas/respuestas y sólo DESPUÉS considerar pruebas. El bloque creativo actual se limita a preguntas motivadas. No se propone aquí una receta alternativa, filtro, orden distinta, implementación, draft o motor.

## Qué afirma realmente la fuente

Se releyeron completas por MCP CapitalR12K1001R2A6 y BtcResearchR16LegacyBase1m. También P_FINAL, K1001_DIAGNOSTIC_AND_BTC_SPECIALIZATION_DIRECTION y K1001_DEEP_DIAGNOSTIC_DATA_FEASIBILITY. Antecedentes releídos: AngleCombinedBtcAcceptance4h, BTCNovelR901, BTCNovelR902 y cierres R8 ya examinados en esta investigación.

| Rama | Comportamiento definido por reglas | Qué NO queda demostrado por el nombre |
|---|---|---|
| LONG_RUNNER | Ruptura del canal previo26 con EMA20/80 y pendiente, ADX/RSI; compra LIMIT en el máximo previo para un retest durante la próxima4h. Stop2ATR y después runner sin TP/plazo, BE desde2.25R y trailing por mejor CIERRE4h. | Que toda compra sea demanda nueva, que sólo opere mercados alcistas completos, que el retest agregue ventaja o que capture todos los breakouts. |
| CORE_SHORT | RSI3<=20 mientras EMA120 sigue ascendiendo y el precio está por encima de EMA120−ATR. SELL STOP bajo la estructura actual, stop vinculado a EMA20, target1.5ATR y72h. | No es una regla de gran tendencia bajista. Puede vender un movimiento bajista rápido dentro de una referencia lenta aún ascendente; precio puede estar algo por debajo de EMA120. No prueba liquidaciones forzadas. |
| SUPPLEMENT K1001 | Avance previo positivo pero ineficiente ER<=1/3; presión OHLCV neta negativa y pérdida del VWAP de la cohorte positiva, vela final roja. Transición del setup completo y SELL STOP bajo el mínimo de LAS DOS barras. Stop estructural, TP2R y48h. | Cohorte HLC3×V no es coste real de tenedores ni flujo taker. No equivale automáticamente a todo mercado lateral, distribución institucional o apertura de una tendencia bajista. |

Son tres mecanismos asimétricos, no una estrategia long y su copia invertida. LONG_RUNNER deja correr; CORE_SHORT cobra un objetivo relativamente corto; SUPPLEMENT espera fallo de un avance circuitoso y confirmación estructural. Long tiene prioridad sobre core y éste sobre suplemento. Pendientes, ocupación y capital afectan qué termina ejecutándose.

P dejó31/116/45 cierres y aportes positivos de las tres ramas EN ESE LIBRO. Son ejecuciones seleccionadas conjuntamente, no tres cuentas independientes ni evidencia de rentabilidad por régimen. P continúa NO_CUMPLE; no se recalifican sus resultados.

## Primera pregunta: ¿qué significa menor o mayor aporte de cada rama?

La geometría de beneficios es distinta incluso antes de observar PnL:
- LONG_RUNNER: no TP; beneficio potencial no queda fijado a un múltiplo.
- CORE_SHORT: distance=EMA20−entry, con ATR<=distance<=3ATR; target_distance=1.5ATR. Por tanto target/distancia inicial está entre0.5R y1.5R por álgebra de la fuente, no siempre1.5R.
- SUPPLEMENT: target_distance=2×distance, exactamente2R nominal desde el fill.

Pregunta creativa prioritaria: ¿parte de lo que llamamos “debilidad de una rama” es en realidad una forma distinta de capturar/realizar el movimiento, frente a una señal inferior? No se afirma que suceda: primero hay que describir su distribución realizada a escalas comparables.

Con OPEN y trade completo identificados1:1 se pueden describir distancia, target/distancia cuando exista, cantidad, duración, bruto, fees, funding y neto. Separar R de precio basado en qty×distance, múltiplo neto sobre esa misma distancia y múltiplo sobre presupuesto monetario registrado. La reserva.001 y los límites de margen hacen que estos denominadores no sean intercambiables. No asumir que todo fill arriesgó exactamente el objetivo monetario.

No proponer cambiar targets, quitar TP, extender plazo o copiar runner en los shorts a partir de esa tabla. Eso sería una prueba posterior que este documento NO diseña.

## Preguntas por rama y cómo responder sin repetir backtests

1. LONG_RUNNER: ¿su aporte viene de unas pocas tendencias prolongadas o de una captura frecuente y distribuida?
   Con los31trades atribuidos se pueden describir concentración, duración, fees/funding y cohortes de apertura/cierre, conservando todo el histórico2020parcial/2021–2025. No llamar a la suma por año de cierre un retorno anual de una cuenta long. Las31ejecuciones no dan confianza automática ni muestran los breakouts bloqueados o no llenados.

   ¿Qué demuestra realmente el retest? La fuente compra al tocar un nivel por debajo del precio de señal; el fill en sí no demuestra recuperación posterior ni aceptación. Logs de órdenes pueden describir espera hasta fill/cancelación para órdenes efectivamente enviadas, no el universo de setups. Sin una trayectoriaM1 acreditada no se puede clasificar cada retest como rechazo/reclaim, medir MAE/MFE o atribuir pérdida a “comprar mientras caía”. Mantener esa explicación como pregunta sin respuesta, no como defecto empírico ya hallado.

2. CORE_SHORT: ¿captura ventas rápidas en contextos lentos ascendentes, con un payoff realizado diferente del suplemento?
   Ese contexto de admisión es una verdad de la regla; no exige reconstruir etiquetas retrospectivas trend/range. OPEN/target/stop permiten describir reward/risk inicial y trade/funding permiten el resultado realizado. No reconstruir EMA120/RSI/ATR completos desde equity diaria ni clasificar el resto de mercado como bear. La existencia de este short NO acredita que K1001 cubra grandes bajadas cuando la referencia lenta ya desciende.

3. SUPPLEMENT: ¿el avance ineficiente fallido tiene distribución realizada distinta de la venta rápida del CORE_SHORT?
   El mapa de origen es imprescindible porque ambos son short y pueden entrar STOP. No usar side, ordenSTOP, resultado o duración para decidir origen. El setup completo se consume antes de ocupación y sizing;82eventos−45fills no significa37trades bloqueados por otra rama. La cifra mezcla mecanismos y no tiene una causa única sin el registro completo de candidatos.

4. Convivencia: ¿qué periodos y recursos ocupó cada rama REALMENTE?
   Los intervalos de posiciones y, si los logs íntegros lo soportan, órdenes pendientes permiten describir utilización observada. No inferir cuántos trades habrían ejecutado las demás, su PnL contrafactual ni diversificación standalone. Con señales no persistidas no se recupera todo el universo de entradas suprimidas.

5. Regularidad: ¿la irregularidad publicada del libro se explica por concentración temporal observable o faltan datos para atribuirla?
   Reutilizar meses/DD/M1 del libro ya auditados. El cierre por componente no proporciona MTM mensual separado. Si el mapa de origen o cashflows no permiten atribución inequívoca, marcarlo pendiente; no fabricar curvas ni diagnósticos causales de regímenes.

## Datos existentes, orden de lectura y límites

Primero resolver la unión completa OPEN/CLOSE↔192trades, exigiendo unicidad/coherencia y31/116/45; faltantes son UNATTRIBUTED, no matches elegidos por resultado. Después describir las preguntas anteriores con todas las cohortes, financiación histórica y costos reales modelados. No hace falta repetir el accountingP ya conciliado.

Los logs no contienen todos los candidatos/latches por cierre4h ni la trayectoriaM1 íntegra. Este documento no solicita velas adicionales ni introduce un análisisjob. Lo desconocido debe seguir desconocido hasta acordar una medición posterior. Ningún diagnóstico de tres ramas acredita tres cuentas rentables.

## Deduplicación y nuevo pedido humano

El pedido humano nuevo autoriza estudiar K1001 y sostener creatividad derivada; corrige el veto demasiado amplio de no volver a estudiar componentes. No borra los cierres ni vuelve nuevas las preguntas ya ejecutadas.

- P: midió K1001/N204 completos en BTC aislado; no midió standalone ni mapa origen×tiempo detallado. Se reutiliza su evidencia y no se repite la curva original como nuevo avance.
- R8/Y901/Y902: ya contrastó ejecución del SUPLEMENTO (retest LIMIT/VWAP frente STOP estructural en la familia creativa). No presentar “LIMIT contra STOP” como invento ni trasladar su resultado al LONG_RUNNER.
- AngleCombinedBtcAcceptance4h: ya usó ocupaciónM1 del tercio inferior como gate de shorts. No proponer otro umbral de aceptación ni tratar una futura lectura de retest como evidencia de flujo.
- R6: prioridad/capacidad/desplazamiento ya fueron objetos de investigación; preguntar por ocupación realizada no recrea un universo contrafactual ausente.
- R14 y cierres de filtros/gestión: no seleccionar EMA, eficiencia, lado, año o plazo ganador retrospectivamente. El permiso actual permite preguntar por especialización; una eventual comparación necesitará después justificación, control y presupuesto.
- G/Y/AA: no aplicar sus modelos o filtros a K por asociación de nombres ni esperar sus resultados para escoger una condición favorable.

## Riesgo y alcance de esta fase

La cuenta original permanece intacta como evidencia. Su riesgo histórico2% por trade no se convierte en asignación futura2% para CADA derivado.

Refinamiento humano vigente para estudios posteriores: BTC-USDT único; BTC total2%, repartido en dos cuotas fijas1% o tres cuotas fijas2/3%, sin redistribuir la cuota ociosa; límite global6% y3x aislado. El denominador debe ser el capital BTC total, sin inflar exposición cambiando el tamaño nominal de subcuentas. Todavía no se elige arquitectura, número de ramas o convivencia, no se inicia live/paper y USDC queda diferido. Funding histórico real del ledger sigue ON, fee.00045 y slippage modelado0; sin estrés o variaciones de reserva/riesgo para fabricar aprobación.

Estado final: preguntas documentales y lectura de evidencia. CERO nuevas fuentes de estrategia, jobs, drafts, motores, velas inspeccionadas o2026nuevo. Máximo un foco creativo actual: distinguir calidad de la señal de forma de captura del movimiento antes de proponer cambios. Sólo DESPUÉS del diagnóstico se discutirá si una comparación concreta merece protocolo; aquí no se prescribe ninguna.
