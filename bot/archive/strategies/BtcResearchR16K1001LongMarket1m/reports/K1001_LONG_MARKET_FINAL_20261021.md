# K1001 LONG: MARKET frente a política LIMIT, cierre

[MARKET](http://localhost:9200/#/backtest/1e016570-d981-47d1-b6d8-38fcde982084) frente al [control LONG_ONLY reutilizado](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c). La entrada inmediata mejora el retorno y el DD en este desarrollo, pero NO alcanza el objetivo ni resuelve la regularidad. Comparación cerrada sin candidata y sin vecinos de parámetros.

|Métrica|Control política LIMIT|MARKET al cierre de decisión|
|---|---:|---:|
|Operaciones|31|36|
|Planes / cancelaciones|45 / 14|36 / 0|
|Entradas reales|27LIMIT+4MARKET|36MARKET|
|CAGR neto sobre10.000|6.7079%|8.2325%|
|PF neto USDT|3.5520|3.3049|
|PF neto enRprecio, descriptivo|3.9914|3.7241|
|DD M1+fills|8.4730%|6.2330%|
|Meses completos activos positivos|13/28=46.43%|15/33=45.45%|
|Trimestres completos positivos|8/20=40%|9/20=45%|
|Mediana retorno mes calendario|0%|0%|
|Neto sin dos mejores meses|1397.7922|2342.1259|
|Neto USDT / capital final|4030.9035 /14030.9035|5108.5992 /15108.5992|

Cada cuenta alternativa empieza con10.000 totales y sólo cuota1% activa, helper.5wallet/.5margen,3xaislado; no5.000de denominador ni2%para la pieza. No sumar curvas, netos o retornos como libro conjunto. Retorno+1.5246puntos yDD−2.2400puntos, peroPF y porcentaje de meses activos positivos bajan; no dominancia. El control no se volvió a ejecutar.

## Pregunta y cambio controlado

Se validó legacy_long original completo antes de crear una copia con entry=self.price yorder_kindMARKET. Se mantuvo H<close<=H+ATR, EMA20/80/pendiente,ADX26,RSI52–76,rango<=3ATR,distancia2ATR original y sus guardas. Cantidad recalculada con precio nuevo y mismo helper/quota. Stops desde fill real y runnerBE/trailing originales, sinTP/plazo, sin nuevos predicados o riesgo.

Es continuidad de una familia ancestral MARKET ya explorada, no nuevo mecanismo. Core/Baseline/TrendBreakout5m yV1–V6/R14/CUSUM fueron contrastados; no se encontró este control exacto con señal/gestión/contrato idénticos en las fuentes revisadas. No afirmar ausencia universal. Dedup y protocolo se guardaron antes de fuente y motor.

El control es política nominal LIMIT con conversiónnear nativa(.00015=0.015%), no31LIMITsestrictas. En MARKET se verificaron todas las36órdenes nativas de entrada: tipoMARKET,created_at=executed_at=opened_at=signal_at,precioigualdecision/requestedentry,quantity/risk/D y extensión original. No se dedujo tipo desde metadataorder_kind ni de un stub.

## Qué cambió realmente

Hay24tiempos de señal de entrada comunes,12sóloMARKET y7sóloLIMIT;36frente31 no son14cancelaciones añadidas. Entre comunes, sólo3comparten precio de entrada,16tiempo de salida y15precio de salida. Comprar antes cambia precio, stop absoluto relativo al fill, ocupación, decisiones posteriores y capitalización. Es comparación de políticas simuladas completas, no efecto causal por trade ni ganancias imputadas a cancelaciones.

La media Rneto por tradeMARKET es1.3184,mediana−.2970;15ganadores/21perdedores. Rneto=PNL tras fees/funding/(qty×distancia inicial de precio); el denominador excluye fees/reserva. PF enR es descriptivo y no reemplaza la puertaPF monetaria. Máximo observado se refiere a marcas M1+fill bajo salida original, nunca MFE/MAE intraminuto ni precio ejecutable.

## Costos y auditoría

MARKET: bruto5769.400349766326,fees147.29100099739483,funding−513.5101221360909,neto5108.599226632841,final15108.59922663284USDT. Reconciliación por36trades y717pagos completos a<1e−6;441pagos usan proxy de mark explícito. Dos campos funding ausentes se comprobaron sin pagos por ledger, no se imputaron ceros.

BTC-USDT Binance Perpetual Futures,UTC[2020-10-15,2026-01-01),warmup240,ruta1m/data4h,fee.00045takercon descuento porlado,funding históricoON snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,slippage modelado0,reserva.001sólodesizing,3xaislado,10k/cuota1%. Desarrollo observado/adaptativo, no nueva economía2026niOOS. Sin estrés/capital/riesgogrids.

Fuente nueva y6padres congelados,60outcomes técnicos focalizadosPASS en primer job; Python3.11.17/NumPy1.26.4/pandas2.2.3 observados. Revisión estática de broker antes del único motor; prueba nativa de órdenes DESPUÉS de ese mismo motor, sin preflight oculto. Nuevo emisorSUMMARY/SOURCE/COHORT produce16filas terminales completas, máxima213caracteres incluyendo prefijoMCP; ledger y cohortes exactos, sin inferir campos perdidos. La fila vieja propia también llegó completa, pero la auditoría usa las nuevas filas verificadas.36traces únicas congeometry/exitorder/neto,0errores yposiciónfinal0.

R11:2.741.760marcasM1,63intervalos/62mesescompletos,20trimestres,invalid0,DDM1+fills6.2330%. DD diario nativo4.7548% es otro muestreo; no sustituye al usado en puertas. Metadata de análisis quedó acotada1852bytes y las dos partes de trades47895/1372caracteres completas; no transporte truncado o parsingfallback. Un engine económico nuevo,0fallos/reemplazos/backteststécnicos,checks y auditorías en primer intento.51IDs económicos completados desde r9; no muestras independientes ni sumar a V1–V6.

## Años de las cuentas, MTM

|Año|Control política LIMIT|MARKET|
|---|---:|---:|
|2021|16.0912%|15.6931%|
|2022|−1.4756%|−2.3326%|
|2023|13.9989%|15.7146%|
|2024|3.1153%|4.2052%|
|2025|−0.0899%|0.0190%|

Años completos desde fronteras R11, no cohortes de trades cerrados. No implican30%cada año ni independencia de ventanas solapadas. Ambos conservaron mediana calendario0, por lo que el largo periodo sin ganancias regulares no desaparece con más fills.

## Decisión y continuidad

MARKET falla CAGR30%,M65,Q80,mediana positiva yN100; pasaPF/DD yneto sin2mejores meses. La insuficiencia N es adicional a fallos económicos, no prueba por sí sola de pérdida; resultado positivo no implica candidato. No relajar criterios por cuota1%, llevar a2%, quitar reserva/funding ni promover por mejor comparación relativa.

Se cierra el contraste de espera de retesteo bajo este setup. No buscar ahora offsetMARKET,TTL,reclaim,extensión,BE/trailing,targets o filtros vecinos. No demuestra que la retesteo sea siempre mala ni que esta familia jamás sirva: acota la evidencia de estas dos políticas en historia reutilizada. Una futura cuenta conjunta aún no está probada ni se infiere desde estos resultados.

Continuar autónomamente con otra pregunta material contrastada con historial; bloque creativo documental en curso fuera de esta ablación. No realizar otro motor sólo por decepción o por un nombre nuevo. No hay candidata, aprobación operativa, live/paper ni objetivo cumplido.

Recibos: K1001_LONG_MARKET_RESULTS_20261021.json,RAW_RECEIPT,ANALYSIS_RECEIPT,PRE_ENGINE_MANIFEST,TECHNICAL_CHECK_RECEIPT,FRAMEWORK_AND_ENTRY_TYPES; protocolos/dedup/reviews y códigos completos conservados.
