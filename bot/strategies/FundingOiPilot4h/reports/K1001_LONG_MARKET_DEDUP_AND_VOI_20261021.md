# K1001 LONG MARKET vs LIMIT: deduplicacion y valor de informacion

Fecha: 2026-10-21. Revision independiente documental, sin codigo de estrategia, drafts, jobs, motores ni consultas nuevas de velas. Root acepta preparar una sola comparacion economica; este informe registra el fundamento y los limites, no sustituye su protocolo posterior.

## Recomendacion unica y decision que cambia

Preparar UN contraste de politica LONG_ONLY MARKET frente al LONG_ONLY LIMIT de cuota1% ya ejecutado y congelado. No gastar primero un motor replicando el original para un diagnostico observacional de45cohortes: los contadores ya existen y ese estudio no decide el resultado economico de la politica alternativa.

Pregunta: bajo el mismo setup long K y la misma gestion, compensa comprar la ruptura confirmada frente a esperar el retesteo? La regla original incluye una apuesta adicional: exige cierre por encima del maximo previo26, pero coloca LIMIT en ese maximo por cuatro horas. El contraste no inventa una familia MARKET breakout: identifica el valor de esa pieza concreta de K bajo el contrato actual.

Si la politica completa no mejora materialmente retorno/regularidad con riesgo compatible y no alcanza las puertas, cerrar esta comparacion sin offsets MARKET, TTL alternativos, reclaim, BE, trailing o filtros vecinos. Mejor PF monetario, mas fills o una cancelacion favorable no justifican promocion. Una mejora que siga incumpliendo puertas tampoco cumple el objetivo ni autoriza automaticamente mas vecinos.

## Evidencia que motivo la pregunta

Fuente principal leida completa:
- strategies/FundingOiPilot4h/reports/K1001_QUOTA_SCENARIOS_FINAL_20261021.md.
- Fuentes congeladas BtcResearchR16LegacyBase1m, BtcResearchR16LegacyK1001m, BtcResearchR16K1001QuotaBase1m y wrappers LONG_ONLY/SHORT_BOOK, previamente leidas completas.

[LONG_ONLY congelado](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c):31trades, CAGR6.7079%,13/28meses activos positivos,8/20trimestres,mediana calendario0%. Sus entradas/salidas y R coinciden con el long del K original. El PF monetario mayor resulta de ponderaciones y capitalizacion distintas, no de mejor senal.

Root extrajo despues de logs completos45planes LONG=31fills+14cancelaciones. Estas cancelaciones forman13GRUPOS CRONOLOGICOS contiguos4h, NO13episodios independientes ni13muestras estadisticas. Corrijo expresamente mi mensaje anterior que los llamo episodios. Son planes bajo la politica LIMIT original, no el universo exogeno de otra politica ni upper bound de sus entradas: ocupacion, reentradas, fill y capital posterior pueden cambiar.

Los maximos M1+fills de los31trades no son MFE/MAE intraminuto ni precios ejecutables. Las salidas originales censuran el camino posterior. La devolucion retrospectiva no demuestra una salida mejor y no motiva targets/BE/trailing. El contraste propuesto responde directamente el valor de esperar el retesteo, sin inferirlo de esos maximos.

## Deduplicacion amplia: antecedentes encontrados

| Antecedente leido | Coincidencia | Diferencia material frente al contraste exacto pendiente |
|---|---|---|
| TrendBreakout5m, fuente completa por MCP | Ya usa MARKET y documenta comparacion antigua con LIMIT al nivel roto15-60min. La propia fuente afirma deterioro del neto2020-25 con retesteo. Esa cifra es afirmacion historica del codigo; no reaudite aqui sus sesiones ni encontre recibo en su carpeta reports. | Senales1h y timing5m, canal72h por defecto, EMA50/200 y macroEMA120, SL3ATR, trail3/BE1.5R, guardas diarias/rachas; no setup ni gestion K. No es evidencia independiente ni novedad de mecanismo. |
| BtcMomentumCore4h y BtcMomentumBaseline3, ambas fuentes completas | MARKET Donchian26, EMA20/80 y pendiente, ADX26, RSI52-76 y rango<=3ATR: antecedente muy cercano de la misma familia long. | Sin cota K close<=maximo+ATR; stop con floor.8% y max5.5%; BEdefault1.75R y triggers de tightening basados en HIGH, no solo mejor cierre; inicializacion best_close y sizing/margen distintos, riesgo3/5%, ventana y funding diferentes. No es control exacto de entrada. |
| MultiAssetBreakout4h y MultiAssetBreakoutNear4h, fuentes completas | STOP Donchian4h y gestion emparentada. | Arman ANTES de la ruptura; Near exige high<frontera y distancia<=.5ATR. Cambian admision temporal ademas del tipo de orden. No son MARKET tras cierre confirmado del mismo setup K. |
| Phase2BtcLongContext4h, fuente completa, y atribucion comparable | Long Donchian26 retest LIMIT y gestion ancestral de K. | Es LIMIT, no MARKET. El informe comparable excluye expresamente BTCMomentumBaseline3 como control por reglas diferentes. |
| BTC_NEW_ANGLES_RESULTS_20261018.md, leido | Ya existe experimento negativo de entrada long MARKET tras toque M1 y recuperacion en M1 estrictamente posterior, dentro4h. | Requiere retesteo y confirmacion adicional. La pregunta actual es NO esperar retesteo; no rescatar latencia/reclaim. |
| V1-V2: implementacion V1, FundingWfPilotBase4h/ResearchV2Core4h y cierres | Breakout de limites del dia previo y/o reglas de precio/funding; entradas MARKET. | Senal y gestion fija24h/targets distintas; no ablacion del retest K. |
| V3: ResearchV3Base4h, ResearchV3ChannelP4h y channel_features.py, completos | MARKET tras ruptura de canal con filtro tendencial. | Canal20, SMA120 pendiente6, dos direcciones, gestion trail3/max42barras y restricciones propias; no Donchian26/EMA20-80/ADX/RSI/gestion K. |
| V4-V6: inventarios y cierres consolidados, antecedentes ya revisados | Shock/oscillator/funding/cross/VWAP/deleverage/NR7/eficiencia. | Distintas senales; no se identifico control exacto K LONG LIMIT frente MARKET con gestion preservada. No se reabren sus vecinos ni selectores. |
| Discovery C: protocolo y BtcResearchR11Base1m/Cusum completos | CUSUM entra MARKET tras evento tendencial. | Evento de acumulacion de retornos normalizados, no setup K; ATRsimple/TP2R/48h, gestion distinta. |
| P/U/cuotas posteriores y R14, fuentes/protocolos revisados | P/U/cuotas conservan LONG original; R14 cambia filtros long o ablate suplemento. | No cambian exclusivamente LONG LIMIT a MARKET. R14 ER12>1/3, EMA120/pendiente y ablacion suplemento estan cerrados; progreso24h/1R tambien cerrado. |

Documentos concretos consultados o releidos:
- strategies/BtcMomentumCore4h/reports/BTCUSDT_MomentumCore4h_Report.md.
- strategies/BtcMomentumBaseline3/reports/PHASE2_RISK3_CONTROL_20261018.md.
- strategies/MultiAssetBreakout4h/reports/PHASE2_PROGRESS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_COMPARABLE_ATTRIBUTION_RESULTS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_ATTRIBUTION_ORDER_COST_PROTOCOL_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_RESEARCH_HANDOFF_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_FROZEN_PROTOCOL_20261019.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_PROTOCOL_20261020.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_RESULTS_20261020.md.
- strategies/OrchManageTurtleDaily/reports/ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_V1_IMPLEMENTATION_FINAL.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_CONSOLIDATED_DECISION_20261020.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_WALK_FORWARD_HANDOFF_FINAL_V6_20261020.md.
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_C_PROTOCOL_20261021.md.
- Protocolos/fuentes posteriores A-W/Y/AA y P/U/cuotas ya revisados en esta tarea prolongada, sin encontrar esta ablacion exacta.

El informe Core4h contiene afirmaciones antiguas de campeona/OOS ciego/MonteCarlo que fueron corregidas por handoffs posteriores. Aqui se usa como evidencia de existencia y estructura de la politica historica, NUNCA para revivir certificaciones antiguas ni comparar su CAGR con K actual.

Conclusion acotada de la busqueda: no encontre el contraste EXACTO propuesto entre las fuentes/documentos revisados. No es una prueba universal de ausencia en cada sesion historica. El mecanismo generico de comprar rupturas MARKET ya esta ampliamente explorado; la novedad defendible es el control de una sola pieza en K congelado, ahora sustentado por diagnostico y autorizacion humana para estudiar sus fortalezas.

## Alcance que debe preservar el protocolo posterior

Mantener setup K original, incluida cota de extension<=1ATR, ATR de senal/stop inicial2ATR relativo al fill, gestion original, cuota1% de wallet10k y cuota de margen fija, sin redistribuir inactividad. BTC-USDT unico, funding historico ON y mismo snapshot, fee.00045 por lado, reserva.001 solo sizing, slippage modelado0,3x aislado. Mismo historico de desarrollo observado, sin nueva economia2026, estres o variantes de riesgo. Reusar control LONG_ONLY sin rerun economico; preservar sus fuentes/resultados.

Comparar trayectorias economicas nativas completas. MARKET cambia precio y momento de entrada, ocupacion, stops absolutos anclados al fill y capitalizacion: el contraste es de POLITICA COMPLETA bajo el simulador. No convertir las14canceladas en una lista de trades anadidos a31, no sumar PnL de cohortes como efecto incremental ni prometer45trades en MARKET.

La diferencia entre fills y no-fills esta seleccionada por la trayectoria futura. No identifica causalidad economica, flujo, toxicidad del order book o precio ejecutable real. Cualquier resultado conserva dependencia entre episodios/planes, seleccion adaptativa y muestra limitada. Evaluar puertas originales, concentracion y regularidad sin escoger fechas, horizontes o filtros por PnL.

El valor de informacion de un solo contraste supera aqui al replay observacional previo porque decide si conservar o cerrar la espera de retest bajo este setup. No garantiza encontrar una candidata, resolver toda la escasez de long ni justificar integrar long y short en una cuenta conjunta.
