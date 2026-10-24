# Protocolo previo — Turtle simplificado diario BTC + PAXG
Fecha: 18 de octubre de 2026. Una receta55/10/ATR20, sin barridos. Fuente y draft se preparan para revisión del orquestador antes de lanzar.
## Hipótesis y solapamientos
Es la misma familia económica de seguimiento tendencial explorada antes. MultiAssetTrendBoth4h usaba Donchian26, EMA20/80, ADX/RSI y trailingATR; el ejemplo MCP TurtleAI añade SMA200/ADX/chop/cooldown. El catálogo devuelve TurtleV2/V3/TurtleAI y SimpleDonchian, sin establecer que sus resultados sean independientes ni suficientes para importar código.
Esta prueba elimina los filtros y cambia a55d de ruptura /10d de salida, permitiendo long/short BTC y PAXG. No representa una nueva ventaja independiente. SPY se excluye para aislar horarios/proxy.
## Señales y ejecución fijadas
Dos rutas1D, Binance Perpetual Futures, BTC-USDT/PAXG-USDT. Long si el cierre del día ya completado supera el máximo de los55d PREVIOS (c[-56:-1,high]); short si cae bajo el mínimo equivalente. MARKET al precio de decisión cerrado, nunca fill retrospectivo en el máximo/mínimo que produjo la señal.
ATR20 de historia cerrada, distancia inicial2ATR congelada al señal. Stop desde actualfill−distancia para long /actualfill+distancia para short.
Sin EMA/ADX/RSI, filtros de volatilidad, TP, BE ni piramidado. Una posición por símbolo, sin reversión simultánea.
Salida protectora por canal10d: en cada decisiónD1 usar últimos10d ya cerrados INCLUYENDO la vela que acaba de terminar; su lowmínimo para long/highmáximo para short puede ratchetear el stop para el día siguiente, sólo si mejora protección y queda al lado válido del precio actual. No ajustar hacia riesgo mayor ni aplicar el nuevo nivel dentro del día que ya terminó. Incluir el día recién cerrado es correcto para un stop futuro; la entrada55d sí excluye explícitamente ese día.
## Capital, riesgo y costes
Capital compartido10kUSDT,5xaislado,fee0.00045porlado en todasórdenes. Riesgo inicial1%poractivo,8%agregado máximo,globalgross4.4x y techoexante2.2xporactivo; el techo está predeclarado para compartir capacidad entre dos rutas, no optimizado.
Sizing incluye feesentry/stop yreserva0.001paraadversefill sólo enpresupuesto,no fricción ejecutada. Margen disponible90%,ledger de reservaspendientesyposiciones abiertas,qtyBTC0.001/PAXG0.0001 de investigación. PAXGSpot es proxy de precios para futuros; short/funding/nativeconstraints no validados.
## Warmup y reloj
Ventana fija2020-10-15→2025-12-31exclusivo,normalreplay. Warmup40D; no importar2019PAXGinexistente. Guardlen>=56 obligatorio: los primeros~16d quedanflat hasta historia suficiente.
El orquestador verificó porlectura del framework que40noesunacota de retención: DynamicNumpyArray sin drop_at crece y los snapshots devuelvenhistoria acumulada. La fuente agregará una aserción técnica al avanzar hasta noviembre para detectar inconsistencia si no alcanza56; no modifica datos.
Cripto24/7: no se añade calendario bursátil ni se crea1Dartificial. 2026reservado; noframework/live/configglobal.
## Criterios y falsación
Mínimoedge netopositivo trascostes y contribuciones poractivo/dirección; muestra, concentración,holdings y costes son imprescindibles. No promover por un gran ganador ni por winrate.
Objetivo final65–70%mesesactivos/80%trimestres yDD<=25% permanece; riesgo1% puede generarCAGRmodesto y se compara economía con exposición, no con3% como si fueran iguales.
Una receta inicial; si fracasa, no barrer55/20 ni añadir filtros. Si sobrevive, preregistrar el siguiente control de costes/períodos antes de correr. Todo resultado queda registrado incluso negativo.
