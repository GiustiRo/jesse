# K1001: localización de debilidad y rival spot–perp — revisión documental
Fecha local2026-10-21. Sin nuevo protocolo, código, análisis job, fuente de estrategia, motor ni precios.

## Una pregunta material y respuesta con evidencia ya disponible
¿La debilidad2024–2025 representa un deterioro uniforme de las tres ramas de K1001, o se concentra en el runner long y el suplemento mientras el short principal conserva un comportamiento diferente?

Es una pregunta diagnóstica material, no una hipótesis económica nueva. Ya puede responderse descriptivamente reutilizando K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md y K1001_QUOTA_SCENARIOS_PERIOD_AND_FUNNEL_20261021.json. No necesita otra ejecución ni una segmentación elegida después del PnL: los orígenes provienen de reglas/logs y los períodos comparados2021–2023/2024–2025 están ya publicados. No se presenta esa división temporal como descubrimiento de cambio estructural.

|Rama y escenario documentado|N2021–23 /2024–25|Media netaR2021–23 /2024–25|Mediana máximoR observado2021–23 /2024–25|
|---|---:|---:|---:|
|LONG_RUNNER en LONG_ONLY cuota1%|13 /14|2.3759 /0.2422|2.6251 /1.3271|
|CORE_SHORT en SHORT_BOOK cuota1%|73 /43|0.0949 /0.1408|0.7082 /0.7296|
|SUPPLEMENT en SHORT_BOOK cuota1%|24 /23|0.8044 /0.2641|1.4191 /0.5830|

Respuesta: no se observa un deterioro uniforme. El long y el suplemento presentan menor resultado por riesgo y menor máximo favorable observado dentro de sus vidas; el core no muestra esa misma dirección en estas medianas y medias. El libro original también informa menor media brutaR en2024–25, por lo que costos constantes/funding pequeño no explican toda la caída.

La mecánica de las reglas ayuda a interpretar por qué no agruparlas por lado: long busca ruptura con continuación prolongada; suplemento vende fallo de avance previo ineficiente; core vende debilidad rápida dentro de una referencia EMA120 todavía ascendente, con objetivo corto. No se demuestra que alguno mida demanda, inventario o liquidaciones reales.

Rival: tamaños pequeños, cambios de selección/ocupación, payoffs distintos, dispersión de grandes ganadores y períodos escogidos históricamente pueden producir estas diferencias. MáximoR está censurado por la salida propia y sólo observa marcasM1+fills, no MFE intraminuto ni beneficio capturable. Por tanto no se atribuye la caída a señal, salida o régimen causal específico, ni se puede calcular la contribución de máximos por restar medianas.

## Qué decisión cambia y qué no
Esta respuesta justifica abandonar la idea de una avería uniforme de K o de que todos los shorts sean una misma especialista bajista. Si se reordena la investigación, se conserva CORE_SHORT como referencia diferenciada y se explicita que long y suplemento son los dos comportamientos cuya contribución tardía perdió fuerza. No se promueve core, no se eliminan ramas ni se cambian filtros, targets, trailing, TTL o riesgo. Su media sigue siendo pequeña y ninguna cuenta alcanza el objetivo.

No recomiendo otro motor para volver a responder esta pregunta. Una pregunta causal posterior sobre calidad de señal necesitaría información que las tablas agregadas no proporcionan. Esta revisión todavía no identifica una intervención nueva suficientemente motivada.

## Rival spot–perp: antecedente exacto y diferencia posible
FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md ya propuso documentalmente H-CARRY: BTC spot largo más perpetuo corto cuando remuneración esperada conocida exceda costos de ambas patas/capital. Quedó pendiente por funding esperado vs realizado, precios spot/mark/index/perp sincronizados, especificaciones/costos/margen y soporte contable de dos patas. No fue una ejecución económica ni un resultado negativo. No se reabre ese carry, que también ampliaría el alcance de una cuenta sóloperp.

V1–V6 y el descarte BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md ya cubren extremos/normalización/persistencia de tasas publicadas y OI; Z descarta reinterpretar funding acumulado como inventario de una cohorte. Q cubre desplazamiento relativo BTC/ETH con beta y V dinámica conjunta VAR/AR de retornos. Son antecedentes cercanos conservados, no respuestas exactas a spot–perp.

Una desviación simultánea entre spot y perpetuo del mismo BTC podría aportar información distinta: precios relativos de dos formas de exposición al mismo subyacente, en vez de tasa liquidada, cantidad de contratos o otro criptoactivo. Pero no se puede asumir que el perpetuo sea quien corrige, que spot lidere, ni que esa prima mida apalancamiento neto; puede converger por movimiento spot, ambos o dinámica de cotización/arbitraje. Un spread de cierres de vela tampoco es spread bid/ask ejecutable.

En los documentos revisados no identifiqué una prueba económica de liderazgo/precio relativo BTCspot–BTCperp equivalente. Esto es búsqueda dirigida, no certificación universal: el listado MCP de reports FundingOiPilot4h se truncó en1000entradas y no se usa su ausencia de nombres como censo. Se revisaron además historia r4, Hub r29 y protocolos completosV1–V6/Q/V, X y el antecedente FRESH exacto.

Estado spot–perp: HOLD documental. No hay evidencia en estas fuentes que acredite observaciones causales sincronizadas ya disponibles para la ventana2020–25; tampoco se acredita que no existan en el servidor. No se consultó coverage, velas ni imports. Se conserva como rival conceptualmente distinto, no como explicación encontrada de la debilidad K ni recomendación de motor. La prima histórica no puede reconstruirse desde funding liquidado o equityK.

## MARKET ya resuelto y contrato
Se leyó K1001_LONG_MARKET_FINAL_20261021.md. Entrada inmediata: CAGR8.2325%,DD6.2330%,N36,M15/33,Q9/20,mediana calendario0; control reutilizado CAGR6.7079%,DD8.4730%,N31,M13/28,Q8/20. No cumple. El contraste no rescata regularidad ni habilita offsets/vecinos.51IDs desde r9, no independientes;209V1–V6 separados.

BTC-USDT exclusivo,10.000totales, riesgo BTC2% compartido (1%+1% cuando corresponda), límiteglobal6%,3x,taker.00045másfunding histórico,slippage modelado0. Sin estrés/nuevaeconomía2026/USDC/livepaper/import/install/configglobal. Todo el trabajo adicional fue lectura documentalMCP y este reporte.

## Fuentes decisivas
- strategies/FundingOiPilot4h/reports/K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md
- strategies/FundingOiPilot4h/reports/K1001_COMPONENT_BEHAVIOR_AND_CREATIVE_QUESTIONS_20261021.md
- strategies/FundingOiPilot4h/reports/K1001_QUOTA_SCENARIOS_PERIOD_AND_FUNNEL_20261021.json
- strategies/FundingOiPilot4h/reports/K1001_LONG_MARKET_FINAL_20261021.md
- strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V1.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V2_20261020.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V3_20261020.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V4_20261020.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V5_20261020.md
- strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V6_20261020.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Q_PROTOCOL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_V_PROTOCOL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Z_DOCUMENTAL_DEDUP_NO_EXPERIMENT_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_X_PROPOSAL_HOLD_20261021.md
