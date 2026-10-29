# SPY con VIX oficial — factibilidad y prueba mínima, 2026-10-18

Estado: ARCHIVADO SIN EJECUTAR POR DECISIÓN HUMANA. El usuario descartó VIX, COT y el descargador y eligió continuar sólo con BTC mediante precio y velas. No queda consentimiento pendiente ni se realizará descarga. SIN DATOS NUMÉRICOS CARGADOS, SIN FUENTE/DRAFT/BACKTEST NUEVO. Se conserva el objetivo de 65–70% de meses activos positivos, 80% de trimestres y drawdown máximo 25%; no se cambia el criterio para esta propuesta. Sólo desarrollo 2020–2025; 2026 reservado. Funding queda fuera, y no se crean scripts de investigación.

## Qué información añade

Según la [metodología oficial Cboe](https://cdn.cboe.com/resources/vix/VIX_Methodology.pdf), VIX agrega cotizaciones bid/ask de opciones sobre SPX para estimar volatilidad esperada a 30 días, expresada a escala anual. Aporta precios de opciones, información que no se puede reconstruir con las velas de SPY. No indica dirección y tampoco garantiza una probabilidad física de pérdida; contiene precios y primas exigidas en ese mercado. VIX=30 equivale a escala anual del 30%, no a una caída prevista del 30%.

El documento consultado describe publicación indicativa cada 15 segundos entre 03:15–09:15 y 09:30–16:15, hora de Nueva York (convierte desde CT). Por tanto el dato diario final no estaba disponible al cierre de SPY de las 16:00. El horario descrito es el de la metodología consultada, no una certificación de cada publicación histórica ni del momento de actualización del CSV gratuito.

La [página histórica oficial](https://www.cboe.com/tradable-products/vix/vix-historical-data) ofrece cierres diarios desde 1990 y enlaza el [CSV oficial](https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv). No usar futuros VIX como si fueran índice spot ni fabricar un VIX mediante ATR o volatilidad realizada.

## Comprobación de viabilidad con herramientas autorizadas

- MCP get_existing_candles(symbol="VIX") devolvió success, 0 pares VIX y 6 pares totales. Es inspección de datos solicitada por la tarea, no precheck general de un backtest.
- El inventario global previo de archivos de proyecto no contiene rutas con VIX, implied o volatility. Esto no prueba que no exista algún dato con nombre opaco; no se leyó indiscriminadamente cada archivo.
- Abrir el enlace oficial de descarga con web produjo: "400 Unsupported content-type: text/csv". La limitación es del lector web, no una afirmación de que Cboe haya dejado de publicar el histórico.
- El MCP clean_and_import_custom_candle_csv acepta un archivo ya presente en el host/proyecto; no descarga URLs. El resto de herramientas revisadas tampoco proporciona un lector HTTP de datasets genéricos.
- La tarea prohíbe red en estrategias/análisis, filesystem fuera del MCP, instalaciones y scripts nuevos. No se ha recurrido a ninguna de esas vías, ni a mirrors no oficiales, ni a transcripción aproximada de gráficos.

En consecuencia no es posible hoy acreditar filas numéricas exactas de VIX con el recorrido autorizado que se ha probado. No hay prueba económica ejecutada. Para desbloquear bastaría disponer del CSV oficial dentro del proyecto o de un conector que entregue sus filas; después se preservaría un snapshot íntegro del intervalo permitido y su procedencia. No es necesario cambiar el framework ni simular velas M1 de VIX diario.

## Único control propuesto, pendiente de revisión de root

Pregunta: ¿evitar nuevas entradas SPY bajo estrés de volatilidad implícita mejora la regularidad económica de la candidata sin eliminar su esperanza positiva? El VIX no decide largos/cortos ni se combina con nuevas condiciones de precio. Es un filtro externo de gestión de riesgo sobre una familia ya investigada; no una nueva fuente independiente de alpha demostrada.

Mantener intacta la referencia MultiAssetRetestBtcShort4h, sesión 2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb, [dashboard](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Crear eventualmente una variante propia con única diferencia: rechazar una entrada nueva de SPY cuando el último cierre VIX admisible sea ≥30. No cerrar una posición por cruzar ese nivel. Conservar señales, stops, sizing, asignación, riesgo máximo 3% por trade/8% agregado, isolated 5x y fees 0,00045 por lado en todas las órdenes. BTC, PAXG y shorts se conservan.

El nivel 30 es una frontera redonda predeclarada de estrés, no un óptimo encontrado ni una ley económica. No comparar 20/25/35, ni cambiarlo si el resultado decepciona. Cabe que el filtro suprima precisamente los mejores rebotes o aumente concentración; se contrastará esa posibilidad.

### Disponibilidad causal del dato

1. Guardar fecha de sesión y cierre oficial sin fabricar hora de observación intradía.
2. Considerar cada cierre admisible a partir de 09:30 America/New_York del día civil siguiente; exigir además que su fecha NY sea estrictamente anterior a la decisión. El desfase es deliberadamente conservador y no prueba el instante real de publicación del CSV.
3. Usar búsqueda as-of por instante disponible, nunca por igualdad de fecha UTC ni con relleno hacia atrás desde la siguiente publicación. Validar DST con ZoneInfo.
4. Si no hay dato anterior, rechazar la entrada; si su fecha dista más de 4 días civiles de la decisión, rechazar por antigüedad. No adivinar festivos ni hacer backfill con datos futuros. Informar por separado cuántos rechazos son por estrés, ausencia o antigüedad.
5. Los días sin nuevo VIX pueden reutilizar el último ya conocido dentro de ese límite; esto es persistencia de información publicada, no cotización negociable ni volumen inventado. SPY sigue requiriendo su quote M1 real fresca y paridad de precio.
6. El CSV descargado hoy es histórico publicado, no archivo de versiones point-in-time. Un desfase temporal evita usar cierres futuros pero no elimina por sí solo revisiones históricas; reconocer esa limitación.

### Validación y falsación, sin cambiar objetivos

Antes de rentabilidad: comprobar orden/duplicados/valores finitos positivos, fechas limitadas a 2020–2025, joins as-of, DST y una fila deliberadamente futura que no se pueda consumir. El primer valor disponible debe ser posterior a su cierre, nunca sustituirse por ATR.

Un solo backtest normal, ventana común 2020-10-15→2025-12-31 exclusiva, luego auditoría MTM V4, comparación pareada contra la referencia y atribución SPY/años/costes/concentración. Mostrar meses activos y todos los meses, trimestres completos y bordes, cobertura efectiva del gate y exposición. No aceptar la mejora de porcentaje obtenida sólo dejando meses sin actividad. No combinar con las recetas TOM/FOMC descartadas ni elevar riesgo para compensar menos operaciones.

Si no mejora regularidad y economía conjuntamente, rechazar este control; no abrir una rejilla del umbral ni probar la inversión de su signo. Si mejora, robustez posterior preregistrada y revisión del coste real del proxy antes de considerarlo candidato, manteniendo 2026 sellado.
