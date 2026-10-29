# Propuesta X en HOLD: desacuerdo entre BTC continuo y la referencia bursátil al reabrir

Fecha: 2026-10-21. Estado: HOLD documental por integridad del proxy y calendario. Root confirmó que no se gastarán motores ni se adquirirán datos para forzar esta idea. No es un protocolo aprobado para implementar. W está en implementación; no consulté resultados económicos de W al formular ni guardar este documento.

## Una pregunta material, todavía no implementable

¿El desacuerdo entre el movimiento de BTC durante el cierre estadounidense y el reajuste de la referencia bursátil al reabrir añade información para pronosticar BTC a 24 horas, frente al movimiento BTC del mismo intervalo sin esa referencia?

El mecanismo propuesto es asincronía informativa entre un mercado continuo y otro con cierre, no liderazgo universal de acciones sobre BTC. El contraste exige que ambos retornos se calculen entre los mismos timestamps. La escala monetaria no importa para logretornos, pero el producto, la convención de precio y la definición de apertura sí.

No sería simplemente sustituir ETH por SPY en V: no hay VAR, regresión entre lags ni pronósticos recursivos conjuntos. Tampoco se propone escoger una fase UTC favorable de T. Sin una reapertura económicamente identificada, esa diferencia material se debilita: sólo quedaría un reloj programado sobre otro proxy, y no lo presentaría como descubrimiento del mecanismo.

## Contraste propuesto para revisión, no autorización

Una posible definición cerrada sería observar a las 10:00 America/New_York, una vez completadas las treinta primeras velas M1 desde 09:30. El punto de referencia sería el cierre de la sesión regular anterior a las 16:00, con su fecha y cierre real acreditados por calendario. Para ambos instrumentos se tomarían cierres conocidos exactamente en esos dos extremos. No usar el open de una vela que aún no cerró ni retrodatando la decisión a 09:30.

B sería el logretorno BTC entre ambos extremos; S, el de la referencia bursátil entre los mismos extremos. S incluiría noche y primeros treinta minutos, por lo que no debe llamarse gap puro. Las fechas de cierres anticipados no pueden sustituirse silenciosamente por 16:00. Los intervalos incluirían el cierre nocturno o fin de semana que realmente corresponda, sin normalizarlos ni filtrar lunes después de resultados.

Tratamiento: media del retorno BTC siguiente a 24 horas condicionada por los signos observados de B y S. Control: media condicionada sólo por signo de B, sobre el mismo banco y eventos. Una propuesta finita para revisión sería los últimos 120 eventos maduros, al menos 20 casos de la celda actual en ambas políticas; no llenar celdas con eventos más viejos. Signos cero o fuente/calendario inválidos implicarían abstención común. La decisión usaría el hurdle heredado ±0,0019 sobre la media de logretorno; no impondría seguir SPY o revertir BTC por intuición.

Los labels serían precio BTC bruto a T+24h, madurados sólo con un camino BTC M1 completo; incluirían fines de semana, sin necesitar un precio bursátil futuro. Banco y señales avanzarían también estando ocupado, sin cola, reversión ni reentrada tras cierre en el mismo timestamp. Inicialización online con cash hasta reunir el banco; no asumir que warmup de cuatro horas ya contiene 120 sesiones bursátiles.

Esto es un borrador exacto de contraste para poder criticarlo, no números aprobados ni una invitación a buscar otros bancos, horas o celdas. No se ha ejecutado ningún caso ni inferido frecuencia.

## Contrato económico que no cambiaría

Sólo se operaría BTC-USDT en Binance Perpetual Futures, ruta de ejecución M1. Ninguna posición SPY, cartera ni hedge. Ventana [2020-10-15,2026-01-01), capital 10.000 USDT, riesgo 2% por operación y 6% agregado, 3x aislado. Comisión taker con descuento de 0,00045 por lado, funding BTC histórico aplicado con el dataset congelado y proxies declaradas, slippage aplicado cero. Sin estrés ni variantes de exposición.

R10 sizing fee-aware, margen 90%, floor de ocho decimales. Stop de dos ATR14 simples BTC de cuatro horas, usando sólo la última frontera 4h cerrada antes de T; precio de entrada MARKET sería BTC M1 fresco en T. No confundir el cierre 4h anterior con precio ejecutable. Sin TP y gestión R12AR de 24 horas desde fill real, evaluada en las primeras fronteras 4h elegibles; no salida forzada al cierre bursátil. Observer R11 y gates r9 intactos: CAGR30, PF1,2, DD25 con objetivo20, M65, Q80, mediana calendario positiva, neto sin dos mejores meses positivo y N100 sólo preliminar.

El forecast sería precio bruto, mientras el ledger real incluiría fees y funding. Ningún resultado de una pierna o cuenta combinada anterior se trasladaría como retorno de esta cuenta BTC.

## Por qué queda en HOLD

1. Los informes R20/R40 identifican el símbolo histórico SPY-USDT como proxy SPX CFD BID dividido por diez, no una serie nativa del ETF SPY ni su subasta. La escala se cancela en logretornos; esa propiedad no corrige el producto o la formación de precios.
2. R20SpyDayNightDisagreement usa America/New_York 09:30–16:00 y advierte expresamente que los días hábiles no equivalen a un calendario NYSE completo. Las fuentes revisadas no aportan una lista acreditada de holidays y early closes 2020–2025 para el producto real.
3. Encontrar timestamps M1 completos no demuestra una sesión económica real ni descarta relleno del proveedor. La presencia de precios un feriado no autoriza llamarlo apertura bursátil. La ausencia no permite elegir automáticamente un cierre anterior conveniente.
4. Existe evidencia documental de SPY M1 ya usado por R20/R40; no inspeccioné ni certifiqué la disponibilidad actual por día. No se consultaron velas, imports, previews o cobertura preliminar.
5. Se leyó jesse://strategy, secciones Trading Hours y Adapting traditional-market research to 24/7 execution. Esa documentación exige identificar producto/horario, calendario explícito y alineación, sin adivinarlos. La propuesta operaría BTC continuo: un eventual filtro bursátil afectaría sólo sus observaciones auxiliares, nunca desactivaría su gestión o protecciones.

Antes de implementar harían falta metadatos y calendario ya existentes que acrediten esos extremos, o una reformulación explícita como observaciones de un CFD a horas fijas. Esa reformulación sería otra pregunta, no una corrección técnica silenciosa. No se autoriza adquirir datos, buscar velas para elegir horarios ni gastar un motor. HOLD no es un resultado económico negativo ni una hipótesis ejecutada.

## Deduplicación realizada

| Antecedente leído | Relación y decisión |
|---|---|
| Hub 20261021-r22: revision.json, HANDOFF.md y DISCOVERY_RESULTS.md | Fuente vigente A–V, 42 ejecuciones por ID y AR replicado; no muestras independientes. Campos stale de roadmap/blockers señalados por root no se usan para inventar pendientes. |
| R4 EXPLORATION_HISTORY.md | Se revisaron continuaciones y rechazos, no sólo handoffs originales. |
| V / BtcResearchR22JointBase1m y cierre V | VAR de retornos sincronizados BTC/ETH, dos ecuaciones y feedback. X no modifica sus lags, activos dentro del VAR, regularización, ventana ni gestión. V sigue cerrado. |
| J / BtcResearchR13ExternalBase1m y cierre J | Shock ETH actual confirma momentum BTC horario; no extremos de sesión bursátil. No rescatar sigmas u horas de J. |
| Q / BtcResearchR17RelativeBase1m y cierre Q | Desplazamiento de niveles BTC/ETH con beta contemporánea; no asincronía de cierre/reapertura. |
| R20SpyDayNightDisagreement | Cinco gaps propios SPY contra cash returns propios, no transmisión a BTC. Antecedente directo de segmentación económica, no receta inédita. |
| R40SpySegmentedResponse | OLS de gap y cash propios SPY para retorno siguiente; no operar BTC con referencia externa. |
| R20PaxgSpyDelayed1h | Shock contemporáneo SPY con PAXG quieto en fixing; antecedente de señal externa, no control de intervalos de cierre/reapertura. |
| MultiAssetRiskOffShort4h | ROC de BTC/SPY/PAXG con treinta barras por cada horario, horizontes económicos distintos. No es el contraste de intervalos exactos propuesto. |
| ResearchSpySlowBeta4h | Observaciones propias SPY a16UTC, control de beta lenta; no se confunde 16UTC con cierre de Nueva York. |
| R/S/T/U y sus cierres | Se conservan kNN/target, fases UTC y relojes de volumen cerrados. X no cambia esos modelos, targets, ventanas o clocks para rescatarlos. |
| W, sólo protocolo | Dos primeros pasajes BTC a barreras, tipos REV/CONT y FAST/SLOW. No se consultó su resultado y X no cambia barreras, resolución, censura o duraciones. |

La búsqueda dirigida no demuestra ausencia universal de otra receta equivalente. No vi una ejecución que respondiera exactamente esta pregunta; la integridad de su medición impide recomendar un motor ahora.

## Descarte adicional antes de llegar a X

Consideré ocupación temporal del precio en M1 frente a cierre OHLC, pero la descarté por antecedente BTC concreto: AngleCombinedBtcAcceptance4h ya cuenta 240 cierres M1 en el tercio inferior del último 4h, exige al menos 120 y comprueba paridad OHLC. Su cierre prohíbe grid de ocupación y nuevas pruebas de aceptación. Cambiar referencia a apertura o el estimador no basta para presentarlo como una nueva familia.

Fuente y cierre:
- strategies/AngleCombinedBtcAcceptance4h/__init__.py
- strategies/AngleCombinedBtcAcceptance4h/reports/ANGLE_BTC_ACCEPTANCE_RESULTS_20261018.md

## Trazabilidad de las fuentes más cercanas

- strategies/R20SpyDayNightDisagreement/__init__.py — SHA256 104677ba8c8bcaad1270a9e599e9baad71d66f82934a0b15072d6adda14fd162
- strategies/R40SpySegmentedResponse/__init__.py — SHA256 02ef14deacd5c24016af7731cb5018fd8ecfb93b97c93d4d2182c23f88ec8246
- strategies/R20PaxgSpyDelayed1h/__init__.py — SHA256 7ab0db6508a8ec8d116c385d13fb8475cc17f5b049fd7f9304f32aed7b36b43c
- strategies/MultiAssetRiskOffShort4h/__init__.py — SHA256 7947fe2844f58b9b9484f68fbe0367fa0aa4b3a4e58d144cdadfcb1e727b6f09
- strategies/ResearchSpySlowBeta4h/__init__.py — SHA256 b61bfb5e250a2a30cdebca6462d1353d891cf8e270d1516a1fa84fd2a2396ab7
- strategies/AngleCombinedBtcAcceptance4h/__init__.py — SHA256 8e41a80a82180a8ad2193b6105bbd2173008e76e89ac4318e9cf774511148ae4

Informes consultados:
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_V_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_U_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_W_PROTOCOL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_C_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_H_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_I_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_M_FINAL_20261021.md
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_O_FINAL_20261021.md
- strategies/FreshAuthorMethods/reports/FRESH_AUTHOR_METHODS_DATA_FEASIBILITY_20261018.md

Resultado de esta tarea: una propuesta documental en HOLD, un descarte por duplicación y ninguna nueva implementación, sesión, análisis, vela o dataset. Se conserva la investigación y continúa la búsqueda documental BTC con los recursos existentes, sin estirar vecinos cerrados.
