# R38 — ordinal del cierre de ruptura: cierre

La segunda oportunidad no produjo una candidata ni cumplió la preferencia comparativa. Ambas cuentas terminaron positivas, con CAGR cercano al 6,8%, lejos del 30% requerido y con regularidad insuficiente.

| Política | Operaciones | Neto USDT | CAGR neto base | PF neto | DD M1 y fills | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
| [FIRST](http://localhost:9200/#/backtest/7d2a7a2f-77e0-4926-ab15-b6772beac17b) | 296 | 4078.95 | 6.778% | 1.213 | 15.959% | 30/62 | 8/20 |
| [SECOND](http://localhost:9200/#/backtest/ff157a56-362d-4a0a-9fd3-c8d90c813577) | 184 | 4152.69 | 6.885% | 1.341 | 17.415% | 27/61 | 12/20 |

FIRST selecciona el primer cierre extremo tras un reset del centro del canal de26 barras previas. SECOND selecciona el segundo, que puede ser consecutivo al primero: no exige un fallo previo ni representa un intento independiente. Ambos sentidos, misma protección y salida estructural; sin filtros de SPY, calendario de bolsa, TP o plazo máximo.

## Qué cambió y qué no mejoró

SECOND añade sólo73,7382USDT de neto frente a FIRST. La descomposición es:
- Bruto menor en400,4829USDT.
- Ahorro de comisiones de423,8891USDT.
- Funding menos negativo en50,3321USDT.

Esto describe las dos políticas completas y no acredita mayor capacidad predictiva por esperar otro cierre. El PF sube, pero el DD empeora de15,96% a17,42%, los meses calendario positivos bajan de30 a27 y la mediana mensual es más negativa. SECOND mejora de8 a12 trimestres positivos; aun así queda bajo el objetivo de16/20. Falla la preferencia prefijada de mayor CAGR, DD no mayor y meses positivos no menores.

FIRST tiene30/62 meses activos positivos (48,39%). SECOND27/61 (44,26%), con27/62 positivos sobre el calendario completo. Sus medianas calendario son−0,14265% y−0,33039%. El neto aritmético sin los dos mejores meses permanece positivo (+242,74 y+404,55USDT), pero no resuelve los otros incumplimientos.

Ambas pasan PF1,2, DD25, exclusión de dos mejores meses yN100 operativo. Ambas fallan CAGR30, M65, Q80 y mediana calendario positiva. N100 no implica potencia estadística ni robustez futura.

## Trayectoria y captura

Años2021–25:
- FIRST:−5,35%,−4,71%,+30,16%,+13,21%,−4,10%.
- SECOND:−0,57%,+2,11%,+34,66%,+7,76%,−11,14%.

La ganancia global no equivale a una entrega anual alta sostenida. Las salidas estructurales sí dejaron durar operaciones más de48h: máximos332h y324h. No hubo TP o vencimiento que ocultase esa captura.

El mismo universo de mercado fue verificado en ambos brazos:832 oportunidades brutas (492up/340down),298 cambios de reset y cero invalidaciones. Un replay independiente de logs reprodujo contadores, censura por lado y selección de ordinales. FIRST seleccionó296 y SECOND184; todos se ejecutaron, sin bloqueo por ocupación o geometría. Las diferencias no proceden de señales encoladas o datos accesibles sólo para una cuenta.

## Auditoría y límites

Se conciliaron484 registros de trades cerrados y4.365 registros de pagos de funding entre las dos cuentas alternativas, sin afirmar independencia ni sumar sus PnL como cartera. Bruto−fees+funding=PNL=saldo−10000. Órdenes MARKET de entrada, stops iniciales, cantidades, cortes mensuales y pagos as-of completos verificados.

FIRST:122STOP y174MARKET por reset. SECOND:71STOP y113MARKET por reset. Cero cierres terminales o desconocidos, sinLIMIT. Las condiciones de reset y sus precios coinciden con las solicitudes y órdenes nativas; los stops permanecieron en sus niveles iniciales.

La reconstrucción cronológica del wallet verificó en cada entrada presupuesto=1% del capital total y cantidad exacta del helper de media cuota, reserva y lote. Error máximo de presupuesto<2,3e−13USDT; error de cantidad cero. El margen no fue la restricción vinculante en esta muestra. No se usó un denominador de5000 para inflar retorno.

Contrato BTC-USDT Binance Perpetual Futures, UTC[2020-10-15,2026-01-01),10000totales/cuota1%activa y resto ocioso,3xaislado/límiteglobal6%. BTC total futuro2% eventual, sin redistribución. Fee taker descontada.00045porlado y funding histórico aplicado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; slippage modelado0 y reserva.001 sólo sizing. Historia ampliamente observada y adaptativa, sin OOS nuevo o economía2026.

Dos motores, sin fallos ni reruns. Check técnico13f36722754144c2924b4cd1a7d61541 PASS104 y snapshot audit16d8909543c24f9d9c61a005d08025b4 PASS, ambos al primer intento. Padres intactos y fuentes nuevas congeladas antes de ejecutar. Las correcciones técnicas previas de27OHLC y terminal nativo se conservaron antes de cualquier PnL.

Crítica independiente: BTC_R38_A_INDEPENDENT_CLOSURE_CRITIQUE_20261022.md, lectura de resultados y universo completos; no segunda auditoría de cada fill/pago. Recibos: BTC_R38_A_RESULTS_20261022.json, BTC_R38_A_DURABLE_INDEX_20261022.json, BTC_R38_UNIVERSE_CHECK_20261022.json yBTC_R38_NATIVE_WALLET_SIZING_CHECK_20261022.json.

Decisión: cerrar FIRST ySECOND sin candidata. No seguir con ordinal3, otro canal, reset, lado o gestión para rescatar esta comparación. La evidencia no refuta toda tendencia por ruptura; sí responde este contraste acotado. El objetivo global permanece activo e incumplido.
