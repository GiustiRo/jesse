# Tanda N: composición BTC cerrada

Dos políticas prefijadas FIXED(A/F) y STATE(B/F), una posición2% y gestión congelada por origen; sin candidata. Ventana[2020-10-15,2026-01-01)UTC ya observada, Binance Perpetual Futures BTC-USDT,10k,2%/6%/3x,fee.00045porlado,funding aplicado/verificado,slippage0. Neto cubre fees+funding modelados. Sin estrés ni nueva economía2026.

|Política|N|CAGR|PF|DD M1/eventos|M+ activos|Q+|Mediana mensual|Neto sin2mejores meses|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[fixed](http://localhost:9200/#/backtest/372c7574-4df8-472a-8573-83971c3ceb50)|486|21.7721%|1.3323|21.3144%|34/62|13/20|0.4360%|12531.5214|1.0843|
|[state](http://localhost:9200/#/backtest/665cb22e-4298-429c-a3f5-3df4bc45eb03)|305|26.8969%|1.3389|25.0265%|31/62|10/20|-0.2003%|6318.6686|1.0156|

FIXED falla CAGR30%,M65yQ80. STATE falla CAGR30%,M65,Q80,mediana>0yDD25%:25.0265049276% supera25%, sin redondearlo para aprobar. Ambos superanPF1.2 y concentración aritmética, pero no las puertas conjuntas. No se promueve la combinación ni se cambia su riesgo, prioridad, plazos, gestión, signos o filtros después de ver resultados. Presupuesto N cerrado, sin vecinos locales de rescate.

## Trayectorias y cuentas completas
### fixed

Sesión [BtcResearchR14CompositeFixed1m](http://localhost:9200/#/backtest/372c7574-4df8-472a-8573-83971c3ceb50). Neto17941.870859USDT (179.4187%), capitalfinal27941.870859; bruto precio23412.392123,fees4677.168898,funding-793.352367. DD diario framework-19.8622%, distinto de DD M1. Retornos años completos2021–25:{"2021":-0.805730936862159,"2022":12.747498597318142,"2023":28.715893918529623,"2024":28.189795928023663,"2025":42.39164632588142}. Ventanas móviles12meses descriptivas:{"N":51,"positive":44,"min":{"start":"2021-04","finish":"2022-03","return_pct":-10.357268065496417},"max":{"start":"2024-11","finish":"2025-10","return_pct":48.20280083525823}}. No son OOS/WF ni ventanas independientes.

Ledger de orígenes:{"CORE":{"fills":144,"closes":144,"net":9731.366096373515},"IMPULSE":{"fills":342,"closes":342,"net":8210.504762938235}}. Ambos orígenes contribuyen positivo al libro conjunto, sin demostrar diversificación o superioridad fuera del desarrollo. Eventos288CORE/552IMPULSE,17coincidencias y1conflicto; coalescenciaorigCORE. Descartes porocupación:144CORE/197IMPULSE. Son políticas conjuntas ejecutadas, no suma de curvas standalone.

### state

Sesión [BtcResearchR14CompositeState1m](http://localhost:9200/#/backtest/665cb22e-4298-429c-a3f5-3df4bc45eb03). Neto24645.379269USDT (246.4538%), capitalfinal34645.379269; bruto precio33306.619433,fees4983.295671,funding-3677.944492. DD diario framework-24.1504%, distinto de DD M1. Retornos años completos2021–25:{"2021":11.612158858140864,"2022":-12.10442891797927,"2023":114.1682588162102,"2024":46.01947925312804,"2025":-16.44919008076152}. Ventanas móviles12meses descriptivas:{"N":51,"positive":42,"min":{"start":"2025-01","finish":"2025-12","return_pct":-16.44919008076152},"max":{"start":"2022-12","finish":"2023-11","return_pct":123.20335762138193}}. No son OOS/WF ni ventanas independientes.

Ledger de orígenes:{"CORE":{"fills":89,"closes":89,"net":17579.271422149322},"IMPULSE":{"fills":216,"closes":216,"net":7066.10784724794}}. Ambos orígenes contribuyen positivo al libro conjunto, sin demostrar diversificación o superioridad fuera del desarrollo. Eventos288CORE/552IMPULSE,17coincidencias y1conflicto; coalescenciaorigCORE. Descartes porocupación:199CORE/327IMPULSE. Son políticas conjuntas ejecutadas, no suma de curvas standalone.

## Verificación y límites

Auditoría828b44b9212040338fa4bc889a94a538 succeeded; todos los trades completos reconcilian bruto−fees+funding=PnL=capitalfinal−10000 a<1e−6USDT. LedgerCORE+IMPULSE reconcilia fills/closes/N/PnL. Funding aplicado en ambas, con proxies declarados. Telemetría2.741.760marcasM1,63intervalos/62meses completos y20Q; ventanas inválidas0, actividad por exposición/ejecución, mediana calendario incluyeinactivos. Fronteras postfunding/predecisión porfase; DD wallet+PnLabierto M1+fills no extremosintraminuto. PRETERMINAL sinposición final en ambos, sin liquidación pendiente.

Dos backtests económicos terminados,0fallos/reemplazos/technicalbacktests. Dos checks sintéticos exitosos; primero supersedido por2fixes deparidad antes de economía, final131assertionspass; revisiónindependienteconforme. Selección retrospectiva de padres positivos e intenso reuso histórico explícitos;26corridasdesde r9 no son muestras independientes. Se conserva bloqueV1–V6 separado. MCP dejó de responder al recuperar auditoría/guardar reciboO; al reanudar se consultó el mismojob ya terminado, sin repetir análisis ni motores, sinDockerrestart. El reciboO ausente se recupera desde job técnicoexistente.

Continuidad: O, orden de extremos intradiarios vs cuerpo diario, fijada antes de conocer N,2políticas previas. Ver protocolos/manifiestos/telemetrías/recibos y resultados estructurados. No autoriza operar ni estrés automático.
