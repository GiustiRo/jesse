# Control técnico: BTC con reloj de ejecución 1m y política original 4h
Fecha: 2026-10-18. Estado: fuente guardada para revisión, SIN draft ni backtest. Este documento precede a cualquier corrida. NO implementa touch/reclaim.

## Alcance y referencia

[Referencia combinada inmutable](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb): MultiAssetRetestBtcShort4h, BTC/PAXG/SPY 4h. Fuente releída por MCP y coincidente con la copia previa de 12.917 caracteres.

Clase propia: AngleCombinedBtcClockControl1m, clon completo sin importar ni heredar una estrategia mutable. Se modifica exclusivamente el adaptador técnico del reloj BTC. La prueba no busca rentabilidad mejor: debe reproducir la referencia antes de autorizar cualquier atribución a una ejecución diferente.

Formulario propuesto, aún no creado: BTC-USDT trading route 1m; PAXG-USDT y SPY-USDT trading routes 4h, todos Binance Perpetual Futures y la clase propia; auxiliary data route BTC-USDT 4h. Una única trading route por exchange/symbol; la auxiliar tiene distinto timeframe. Balance 10.000, warmup 240, normal replay, benchmark false; start 2020-10-15, finish 2025-12-31 exclusivo; fees 0,00045 por lado, isolated 5x y límites originales. No se abre 2026.

## Adaptaciones técnicas, sin nueva señal

- signal_candles BTC toma el get_candles 4h auxiliar y conserva sólo filas con apertura+4h≤self.time. Excluye toda vela en formación. Retiene toda la historia cerrada expuesta por el store, sin recortar a 240 o introducir un buffer propio.
- Las nuevas decisiones y reintentos BTC sólo son elegibles cuando self.time%4h==0. El cache sigue siendo por índice de ejecución, pero devuelve cero entre límites 4h. PAXG/SPY conservan sus relojes y horarios.
- El test de rango long BTC usa high−low de la última 4h cerrada; self.high/self.low del alias corresponderían a una M1 y alterarían el setup. Precio de decisión sigue siendo el precio del motor en el cierre común, sin sustituirlo por un valor construido.
- _volatility_share consulta el BTC auxiliar 4h cerrado directamente desde cada llamador al timestamp de éste; no usa otro @cached potencialmente anterior. Las demás rutas conservan la expresión raw/filter original. No se usa el ATR de M1 para asignar capital a la cuenta.
- go_long/go_short BTC fijan deadline=Tsetup+4h. should_cancel_entry conserva False antes del deadline, sin quitar la reserva; la elimina sólo al cancelar efectivamente, como la referencia. La cancelación precede a cualquier nueva evaluación según la secuencia del motor, sin rearmado por minuto.
- update_position BTC retorna entre límites 4h. Stops/targets del broker continúan activos a resolución M1, mientras trailing long y salida short 72h sólo se evalúan en el reloj original.
- on_open_position conserva precio real de fill, distancia de plan congelada, best_close inicial, opened_time real y gestión original. Las órdenes siguen siendo LIMIT long y STOP short.
- La primera decisión BTC exige al menos 240 velas 4h cerradas. Si el auxiliar no hereda ese warmup, la prueba falla explícitamente; no se permite ocultar diferencias mediante meses iniciales sin actividad. El número 240 reproduce la configuración original, no es un parámetro nuevo.

Riesgo 3% por trade/8% agregado, techo bruto 4,4x/reparto inverso ATR, reserva de 10 bps para sizing, fees, estructura de planes, ledger, largos PAXG/SPY y shorts BTC permanecen originales. No se cambia framework, importan nuevos datos ni crean scripts.

## Fuente y límites conocidos

La fuente de 15.418 caracteres fue creada y releída por MCP con coincidencia exacta. Las diferencias explícitas son nombre/docstring, constante del reloj 4h, helper de velas cerradas, adaptaciones de elegibilidad/rango/asignación/cancelación/gestión y aserción warmup. No contiene ningún estado touch/reclaimed ni compra MARKET nueva.

Un timeframe de ejecución distinto puede cambiar el orden de callbacks en timestamps comunes, la frescura de otras rutas, el instante observado por el broker o el capital reservado. La intención de equivalencia no prueba que estos detalles sean equivalentes en el motor. El control será informativo precisamente si revela una diferencia técnica. No afirmamos equivalencia por inspección ni por compartir PnL agregado.

## Criterio de comparación previo

Antes de cualquier estrategia reclaim se exige comparación ordenada de:
1. Todos los fills/órdenes relevantes: símbolo, sentido, tipo, cantidad, precio, timestamp y comisión.
2. Trades y estructura una entrada/una salida sin posición terminal pendiente.
3. Wallet, suma de fees y PnL por componentes.
4. Curva de equity y cartera MTM sobre timestamps comunes; no basta comparar CAGR/DD.
5. Primera decisión y warmup efectivos, tiempos de cancelación y nuevas entradas respecto de la referencia.

Las cantidades/precios contables deben coincidir dentro de precisión numérica explícita de la auditoría, sin tolerancias económicas amplias. Cualquier discrepancia debe explicarse por causalidad de ejecución; no se retocan señales para forzar semejanza. Si no hay equivalencia limpia, parar atribución y no lanzar reclaim como si fuera un único cambio.

El presupuesto futuro sería un control técnico primero y sólo, si root certifica equivalencia, una receta reclaim separada previamente revisada. No existe autorización de lanzamiento en este documento: root debe revisar fuente y asignar slot. La referencia y las otras estrategias permanecen intactas.
