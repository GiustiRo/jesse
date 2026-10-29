# Protocolo: combinada con participación de volumen BTC
Fecha: 2026-10-18. Estado: fuente preparada y guardada; pendiente de revisión y slot de root. Ningún backtest ejecutado.

## Ancla e hipótesis

Referencia inmutable: MultiAssetRetestBtcShort4h, sesión [combinada base](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Se leyó la fuente completa y su formulario guardado antes de implementar. Esta variante contiene un clon completo de dicha fuente, clase AngleCombinedBtcVolume4h, sin herencia ni importación mutable desde estrategias de referencia.

La ruptura/retest long y la continuación de selloff short podrían funcionar peor si el movimiento de precio no viene acompañado de participación efectiva en BTC. El único cambio exige volumen suficiente en la vela de señal BTC. El volumen es la columna 5 de OHLCV BTC que ya alimenta la ruta Binance; no se descarga otra fuente. Es volumen agregado del feed histórico existente, no delta de órdenes agresivas, absorción, interés abierto ni prueba de liquidaciones. El volumen alto también puede indicar agotamiento y empeorar ambas direcciones.

El inventario global previo no documenta este gate de volumen relativo. Esa revisión no leyó todas las fuentes antiguas y no prueba ausencia absoluta de mecanismos parecidos. La estrategia sigue perteneciendo a la familia de ruptura/continuación investigada y 2020–2025 sigue siendo desarrollo adaptativo.

## Receta singular predeclarada

Para cada decisión BTC cuando no hay posición ni entrada pendiente:
- Tomar el volumen de la última vela 4h ya cerrada.
- Buscar las 28 fechas civiles UTC exactamente anteriores, mismo timestamp de apertura módulo 86.400.000 ms. Cuatro semanas completas comparan el mismo bloque horario y evitan escoger horas ganadoras.
- Requerir 28 coincidencias exactas, todas estrictamente anteriores a la actual y con volumen positivo finito. Si faltan fechas, hay volumen inválido o la vela señal no corresponde al closed_candle_open_time actual, el gate es falso. No imputar huecos, usar la fila vecina ni incluir volumen actual en la mediana.
- Autorizar la evaluación de la señal BTC únicamente si volumen actual ≥ mediana de esas 28 observaciones. Se gatea antes de resolver la prioridad long/short original; un long rechazado no activa por caída lógica un short distinto.
- El gate no modifica posiciones existentes, stops, targets, caducidad de órdenes ni prioridad canónica de rutas.

No se exploran períodos vecinos, cuantiles ni multiplicadores. El valor 28 representa cuatro semanas completas y la mediana es la referencia robusta singular predeclarada; no están elegidos por rentabilidad local. La selección UTC controla sólo la estacionalidad intradía más obvia, no cambios de régimen de liquidez ni composición del mercado.

## Lo que se conserva

PAXG y SPY conservan la lógica original de entrada/salida y horarios; no usan volumen. BTC conserva ambas direcciones y sus entradas LIMIT/STOP respectivas. No se cambia ningún hiperparámetro de precio, riesgo o gestión; se mantienen 3% por trade, 8% agregado planificado, tope bruto 4,4x y reparto inverso ATR, reserva de 10 bps en sizing, margen isolated 5x y fee fijo 0,00045 por lado, también LIMIT.

Al compartir cuenta, bloquear BTC puede cambiar el capital y las oportunidades que finalmente obtiene otra ruta; conservar reglas PAXG/SPY no implica garantizar idénticos fills. No se suman curvas aisladas ni se presenta este efecto contable como una segunda modificación de alpha.

Formulario de comparación: Binance Perpetual Futures; BTC-USDT, PAXG-USDT y SPY-USDT 4h con la misma clase clonada; balance 10.000, warmup 240, normal/fast_mode false, benchmark false. Ventana 2020-10-15→2025-12-31 exclusiva. 240 barras equivalen a 40 días y permiten formar las 28 fechas previas, pero un hueco aún provoca rechazo explícito. No se importa ni evalúa 2026.

## Auditoría incorporada y revisión

Se guarda en vars un contador por año UTC de decisión: decision_bars, pass, below_median, missing_dates, invalid_volume, stale_signal, long_admitted, short_admitted. Los cinco estados pass/below/missing/invalid/stale deben sumar decision_bars. Los dos contadores admitted son señales nuevas que sobrevivieron el gate y el plan original, no fills certificados.

Los bloqueos representan decisiones flat, no operaciones contrafactuales perdidas: calcular estas últimas exigiría otra cartera y otra secuencia de capital. La fuente no evalúa planes rechazados para fabricar ese contrafactual.

jh.debug emite únicamente un resumen al cambiar de año y uno en before_terminate, con la historia de contadores. No genera un archivo de investigación nuevo ni 1.900 registros diarios. La última observación diagnóstica incluye timestamp señal, extremos temporales de referencia, tamaño 28, volumen y mediana. Las aserciones impiden referencias actuales/futuras o cambio de bloque UTC.

La fuente guardada fue releída por MCP y coincide exactamente con el texto preparado. Antes del ajuste de instrumentación, una comparación textual excluyendo imports, nombre/docstring y el bloque añadido certificó que el resto era idéntico al original; el ajuste posterior sólo sustituyó el after de diagnóstico diario por resumen anual/final. No se editó la referencia.

## Lectura del resultado y falsación

Tras autorización de root: un full normal, revisar fills/fees/invariantes y auditoría cartera MTM V4. Comparar siempre los mismos 63 meses y 21 trimestres, además de meses activos y períodos completos. Informar años, contribución BTC long/short, cambios de exposición, concentración, comisiones y bloqueos por causa. El objetivo original de 65–70% de meses activos positivos, 80% de trimestres y DD≤25% se conserva.

Menos actividad no basta para promover la variante. Si no mejora economía y regularidad de la cuenta, rechazar la receta y no abrir una cuadrícula de volumen. Si parece positiva, requerirá contraste de robustez posterior previamente acordado, sin atribuir independencia estadística a una modificación de la misma familia ni abrir 2026.
