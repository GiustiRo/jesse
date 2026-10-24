# V6 EFFICIENCY: cierre de replay y robustez

V6 queda rechazado. El nominal no alcanza PF≥1.2, N≥100, tres semestres positivos ni CAGR≥15%. Pasa retorno positivo y DD absoluto≤25%. Los costes S1/S3 y tres de cuatro vecinos también fallan retorno positivo. El vecino 0.315 es diagnóstico y no reemplaza al nominal ni modifica el calendario.

Se completaron los ocho motores autorizados y sus auditorías; el noveno slot de lag reutiliza nominal porque USE_OI=False. No quedan motores ni análisis de esta rama activos.

| Escenario | N | Net % | PF | DD % | CAGR % | Decisión prescrita |
|---|---:|---:|---:|---:|---:|---|
|[NOMINAL](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127)|44|0.278594|1.006229|-17.553569|0.139010|Rechazado|
|[S1](http://localhost:9200/#/backtest/f10942a7-0c80-4824-a972-7d3b284b05cf)|44|-1.920348|0.957002|-18.627561|-0.963515|Falla net|
|[S2](http://localhost:9200/#/backtest/445894c0-a830-45f8-8214-fe1454fc56ce)|45|-4.027645|0.915336|-20.875287|-2.031764|Informativo|
|[S3](http://localhost:9200/#/backtest/b7019ab0-8ade-4606-997f-1ccbfd618cc6)|45|-7.895715|0.836047|-23.171310|-4.023624|Falla net|
|[R09](http://localhost:9200/#/backtest/22d643fb-40aa-4425-b2b6-34c4e7df062c)|45|-0.454647|0.990973|-20.223540|-0.227271|Falla net|
|[R11](http://localhost:9200/#/backtest/f140ce43-60a0-49d1-a390-2e89f722b78a)|44|-0.505926|0.987700|-16.435891|-0.252938|Falla net|
|[A09](http://localhost:9200/#/backtest/90239e02-4fc6-420a-80f5-b9a57d843138)|50|10.328758|1.219032|-14.885492|5.030435|Pasa net/DD|
|[A11](http://localhost:9200/#/backtest/67851216-8941-4fbe-a0ea-ee8ff6bf5e63)|41|-2.571433|0.937092|-19.858272|-1.292331|Falla net|

## Diseño congelado

BTC-USDT, Binance Perpetual Futures, 4h, desde 2024-01-01 hasta 2026-01-01 exclusivo, capital inicial 10000 continuo. E24 usa 24 deltas y 25 cierres; el cruce fresco usa 26 cierres para evaluar sus dos ventanas. Nominal h=0.35, stop fijo 2.5 ATR14 aritmético desde fill, salida de estado E≤0 long/E≥0 short, tenencia 60 barras, sin TP/trailing. Riesgo 2% incluyendo stop y ambas comisiones, cap notional1x, floor8, una entrada/día UTC, sin reentrada en el mismo instante de salida.

El calendario TRAIN ON/ON/OFF/OFF conserva separados 2024H1 y 2024H2, con los cuatro bordes fijos. 2025 permanece en efectivo en todos los escenarios; los resultados EVAL diagnósticos de semestres OFF nunca se suman al N de confirmación. Los 44 trades nominales no se agregan entre variantes para alcanzar100. El año2026 permanece cerrado.

S1 fee0.0009/slip0; S2 fee0.00045/slip5bps informativo; S3 fee0.0009/slip10bps. R09/R11 cambian sólo stop2.25/2.75 ATR y A09/A11 sólo h0.315/0.385. Configuración restante, fechas, calendario, capital inicial y fuentes son idénticos. No hubo reselección TRAIN ni tuning a partir de los resultados.

## Verificación

Los ocho snapshots completos pasan contabilidad, config exacta, ruta/fechas, libros de ejecuciones, precios ajustados y financiación; máximo error 2.910383e-11 USDT. Los logs pasan 8126 aserciones: 4386 decisiones y 24 meses por motor, ventanas, cruces, ATR, sizing y capital continuo por entrada, stop desde fill, salida de estado, UTC, ausencia de TP y calendario. Cero cierres forzados en todos. Los doce meses de 2025 permanecen sin exposición y con efectivo constante salvo redondeos≤2.91e−11 USDT.

Las comisiones sí modifican los tamaños: primera entrada0.14083594BTC nominal contra0.13695228BTC con comisión duplicada, ambos con capital10000. Los hashes de señal en las44entradas comunes de costes coinciden; el deslizamiento cambia la secuencia a45trades. Esto verifica motores con sizing propio, no descuentos sobre cantidades congeladas. Los cinco wrappers conservan fuente exacta al terminar las ocho corridas.

Hubo dos timeouts HTTP de inicio (R09/A09). Cada raw quedó guardado y se recuperó el mismo ID en running/errornull; no se repitió ningún start. No hubo cambios de estrategia, calendario o registro principal.

## Evidencia y límites

V6_REPLAY_STRESS_BRANCH_PROGRESS.json contiene estado ligero e IDs/pointers. V6_REPLAY_STRESS_ROWS.json conserva filas completas. V6_REPLAY_CONSISTENCY_AUDIT.json reúne jobs, verificaciones, efectivo2025 y manifests de raw. Cada V6_REPLAY_<escenario>_ACCOUNTING.json guarda output y estado del job; LOG_AUDIT guarda planes, estados, contadores y referencias a todos los shards de logs/operaciones. Formularios, readback, prerun e inicio único quedan separados por escenario. Código de auditoría: V5_V6_ACCOUNTING_CODE.json y V6_REPLAY_AUDITOR_ORCHESTRATION_CODE.json. Fuentes estáticas y postrun: V6_REPLAY_SOURCE_VERIFICATION.json y V6_REPLAY_POSTRUN_SOURCE_READBACK.json.

Los datos históricos ya fueron observados durante la investigación; estas variantes y folds no son muestras independientes ni prueba fuera de muestra nunca vista. OI no interviene en la señal finalista y su archivo sigue siendo retrospectivo, sin certificación point-in-time. La sensibilidad contable de financiación global×1.5 vuelve negativo al nominal (−0.946104%) y mantiene cantidades fijas; no se confunde con los replays reales de costes. Ningún resultado autoriza operar en vivo.
