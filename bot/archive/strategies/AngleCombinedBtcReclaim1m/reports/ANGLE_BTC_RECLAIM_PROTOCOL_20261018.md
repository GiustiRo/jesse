# Protocolo: BTC long touch-and-reclaim causal dentro de la combinada
Fecha: 2026-10-18. Estado: fuente preparada; pendiente de revisión de root ANTES de draft/run. Una sola receta; no barrer latencia ni umbrales.

## Control previo y mecanismo

[Control de reloj aprobado](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1), auditoría 3e58c073425c45a5ba8ef163147f54d7 succeeded: 220 trades/440 órdenes/1.904 puntos y 45 métricas equivalentes a la [referencia original](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), diferencia máxima de curva 3,64e-12. Es control técnico, no nuevo alpha. Fuente completa clonada como AngleCombinedBtcReclaim1m, sin dependencia mutable.

La LIMIT original compra un retest aunque el precio siga descendiendo. Esta modificación long BTC exige una recuperación observable posterior al toque antes de comprar, pagando explícitamente su precio superior. Puede evitar retests fallidos, pero perder entradas buenas o empeorar su coste. No se promete mejora de esperanza ni se añade otro filtro.

## Único cambio de ejecución BTC long

Al cierre 4h T, ejecutar exactamente el plan long original con su prioridad. Si existe, congelar qty, entry boundary, distancia ATR, riesgo monetario y nocional como techos; armar estado interno en vez de mandar la LIMIT. Mantener su reserva en el ledger compartido mientras esté pendiente. Si no existe long, el short STOP original sigue igual.

before() sólo avanza este estado en callbacks BTC M1:
1. Expirar si tiempo≥T+4h, liberar reserva/estado y bloquear el mismo callback para conservar cancelación sin rearmado inmediato.
2. Aceptar como toque una M1 cerrada del período posterior al setup cuya low≤boundary. Su apertura debe ser≥T y cierre>T; el minuto que termina en T no puede usarse retrospectivamente.
3. Sólo una M1 con cierre temporal ESTRICTAMENTE posterior al cierre del minuto de toque puede confirmar reclaim, y únicamente si su precio de cierre>boundary y aún está antes de T+4h. Una mecha y cierre del mismo minuto no bastan según esta receta: se exige una confirmación adicional de persistencia, con latencia explícita. No es una necesidad matemática para evitar lookahead.
4. En _signal revalidar tamaño y cachear una ejecución positiva del mismo callback; sólo entonces should_long=True y go_long emite MARKET al precio actual de ese cierre M1, sin fingir fill al boundary ni imponer un nuevo techo de precio/filtro de chase.

Un estado long armado bloquea todo nuevo setup/short BTC hasta fill o expiración. Tras fill/cierre no hay reentrada automática: planificación nueva sólo en el próximo cierre 4h elegible. Si el tamaño no permite una unidad mínima, restaurar la reserva y conservar el estado hasta otro reclaim válido o caducidad; no transformar la falta de capital en short ni liberar capacidad indebidamente.

## Sizing y reservas

No recalcular ATR ni volatility shares en M1. La distancia de protección se conserva desde el setup y el stop se ancla al fill real. La cantidad nueva nunca excede la original.

En _signal, antes de declarar una señal MARKET positiva, extraer temporalmente sólo la reserva propia del dict, calcular _committed de los demás y restaurarla siempre con try/finally; los callbacks del motor son secuenciales. Revalidar:
- riesgo=min(techo monetario original, 3% capital actual, capacidad restante del 8% agregado);
- nocional=min(techo nocional original que ya incorporaba su share ATR, capacidad restante de 4,4x bruto);
- margen disponible apalancado×0,90, igual al buffer original;
- unit risk=distancia congelada+fees de entrada/stop al precio nuevo+reserva original 10 bps;
- qty=min(qty original, riesgo/unit risk, nocional/precio, margen/precio), redondeada hacia abajo al mismo paso BTC de 0,001.

Si qty>0, cachear reclaim_execution con qty, unit_risk, precio, timestamp e índice; go_long consume esa ejecución, exige precio/tiempo/índice idénticos y caducidad estricta, actualiza la reserva con cantidades efectivas y siempre manda el MARKET. Si qty≤0, _signal devuelve cero manteniendo reserva y prioridad long; nunca should_long=True con go_long vacío. on_open_position exige origen reclaim, compara qty/notional/risk efectivos con los techos congelados con tolerancia aritmética 1e-8, libera setup y aplica stop original desde fill. No piramidado ni fills parciales. La reserva propia no se cuenta dos veces.

En terminación, un setup interno sin fill cancela sólo su reserva, sin fabricar operación ni anticipar una salida. Las posiciones reales conservan la convención terminal del motor original.

## Invariantes conservados y alcance real

PAXG/SPY mantienen fuente de señales/órdenes/gestión/horarios. BTC short conserva STOP, objetivo y salida 72h. Todas las actualizaciones ATR/trailing/72h son sólo en límites 4h; los stops del broker siguen activos M1. El cambio de capital provocado por la nueva ejecución BTC puede modificar fills posteriores de otras patas aunque sus reglas no cambien: se evalúa la cuenta efectiva, no curvas sumadas.

before() exige timeframe BTC='1m' para fallar explícitamente ante un draft mal configurado. La fuente conserva el adaptador aprobado: auxiliary BTC4h cerrado por open+4h≤self.time, rango y asignación BTC sobre 4h, warmup240 real. No se cambia framework, importa datos ni crea scripts. MARKET al precio actual usa la semántica Jesse; las aserciones y auditoría deben confirmar sus fills reales, no asumirlos por nombre.

Formulario propuesto: BTC1m/PAXG4h/SPY4h, auxiliar BTC4h, Binance Perpetual Futures; balance10.000, fee0,00045 por lado también LIMIT/STOP/MARKET, isolated5x, normal replay, benchmark false, warmup240. Ventana 2020-10-15→2025-12-31 exclusiva. 2026 reservado.

## Verificación y decisión previa

Root revisará fuente y asignará slot antes de cualquier draft/run. Primero revisar órdenes BTC long: señal4h→toqueM1 futuro→reclaim en minuto posterior→MARKET antes de expiry; qty y techos; ausencia de LIMIT BTC long, ausencia de rearmado en callback de expiración y de trailing M1. Auditar wallet/fills/fees y cartera MTM V4.

Comparar la combinada real con la referencia/control: 63 meses y21 trimestres, meses activos/completos por separado, años, BTC long/short, exposición/costes/concentración y porcentaje que no retoca/no recupera/no cabe por capital. No fabricar contadores si no quedan archivados por el motor.

Objetivos originales intactos: 65–70% meses activos positivos,80% trimestres,DD≤25% y economía útil. Si no mejora, rechazar esta receta sin variar minutos, límites de reclaim ni umbrales; si parece positiva, robustez posterior preregistrada antes de selección. Todo es desarrollo adaptativo, no OOS.


## Corrección de contrato API anterior a la primera corrida
Root detectó durante review que declarar should_long=True y luego devolver sin orden por qty cero incumplía el contrato Jesse. Se movió exclusivamente la revalidación de tamaño a _signal, con cache positivo del mismo callback y asserts de consumo en go_long. Se añadió assert de timeframe BTC1m. No se cambió alpha, caducidad estricta, umbral ni receta económica; se releyó por MCP para comprobar la persistencia exacta.

Limitación explícita: la reserva del estado armado es un ledger interno de riesgo/nocional; no existe todavía una orden broker, por lo que no es una reserva real de margen del broker. Las demás estrategias del clon comparten ese ledger y respetan sus límites, y se revalida margen disponible al confirmar la entrada. No se afirma inmovilización real de efectivo ni equivalencia de esa reserva con live.


## Corrección explicativa posterior, sin cambiar la receta ni repetirla
Tras ejecutar la receta predeclarada se corrigió una justificación excesiva: low≤boundary y close>boundary dentro de una vela ya cerrada sí implican que el nivel se alcanzó antes de su cierre, pues éste es el último precio. Exigir otra M1 no es necesario para inferir ese orden básico ni evitar fuga temporal; constituye la confirmación adicional de persistencia y demora que esta receta había fijado antes de correr.

Se corrigieron únicamente dos líneas de comentario de la fuente actual y esta explicación del protocolo. La comparación textual excluyendo líneas de comentario confirmó que todo el texto ejecutable permanece idéntico. El snapshot de la corrida conserva la fuente original por procedencia. No se ejecutará una variante same-minute ni se aflojará la latencia después del resultado.
