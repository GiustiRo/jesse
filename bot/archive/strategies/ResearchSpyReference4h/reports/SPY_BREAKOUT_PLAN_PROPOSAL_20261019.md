# SPY ruptura/retest — propuesta de plan, sin ejecución

Estado: sólo planificación. Ninguna fuente nueva, backtest o análisis iniciado. Leídos handoffs de atribución/R60, matrices SPY20/SPY40 y el inventario global. La otra línea SPY estudia correcciones sin Donchian; esta conserva el origen de ruptura de máximo26.

## Presupuesto recomendado

Hasta tres rondas condicionadas, no obligación de agotarlas: R1 doce fulls (seis por especialista); R2 hasta doce para atribución de, como máximo, una idea fija por línea; R3 hasta nueve (tres bloques temporales × una referencia compartida y dos candidatas). Techo33 fulls únicos. Si sólo una idea merece avanzar, se reduce; si ninguna, se cierra trasR1. Dos backtests simultáneos por especialista/cuatro globales durante ejecución, un análisis propio/dos globales.

Crítica: la referencia tiene31 operaciones, la búsqueda2020–25 ya es extensa y R60 dejó varias trayectorias idénticas. Treinta y tres fulls no producen33 muestras independientes ni garantizan potencia. R2 no debe rescatar umbrales ni agregar combinaciones; R3 es diagnóstico de dependencia temporal, no OOS limpio. Propuesta de bloques contiguos, sin elegirlos por rentabilidad:2020-10-15→2022-07-01,2022-07-01→2024-04-01,2024-04-01→2025-12-31, todos finales exclusivos; validar warmup/state/terminales emparejados antes de fijar su implementación. No sumar esos tramos como si reconstruyeran una cuenta continua. 2026 cerrado.

## Contrato común

Cuenta10 000, riesgo presupuestado1%, fee.00045 por lado incluidaLIMIT, isolated5x/cap4.4/reserva.001 sólo sizing. Misma fórmula de cantidad/ledger, stop inicial2ATR, BE2.25R, trail4.2ATR y tightening5R/8R originales, sin nueva salida. ProxySPXCFDBID/10 aceptado; funding y nuevas fuentes fuera.

RutaSPY4h+M1, warm240, fast/debugfalse. HistoriaUTC Mon-Fri00–20 y baropen00–16entry EXACTOS. El evento de origen satisface las condiciones de precio Cq: ruptura de high de26barras PREVIAS,0<g<=1 y régimen original EMA20/80, pendiente slow[-5],ADX26,RSI52..76,rango<=3ATR. FreshM1T−60/paridad original enentry. Sin volúmenes, RTH,1h ni BTC/PAXGaux.

En entradas demoradas se conserva el régimen EMA/ADX/RSI/rango y ATRválido a la decisión de entrada, pero el canal pertenece al origen congelado: no exigir de nuevo freshDonchianbreakout al confirmar retest. Stop2ATR y sizing se calculan con ATR disponible en la nueva decisión; para STOP se dimensiona a su precio previsto y on_open conserva stop desde fill efectivo como referencia. Esta política cambia el momento del trigger, no la fórmula de gestión; las distancias y exposición pueden cambiar.

## Seis recetas de ronda1: tres pares, no seis causas independientes

| ID provisional | Regla exacta del evento/entrada | Comparador e interpretación |
| --- | --- | --- |
| BR01 FirstEpisode | Reset de época al cerrar en mitad inferior del canal26 previo: close<=(maxHigh26+minLow26)/2. Tras reset, aceptar sólo la PRIMERA señal Cq calificante; entrada retestLIMIT original, caduca una barra. | BR02 y Cq. Separa primera ruptura tras corrección amplia de reiteraciones durante el mismo tramo. |
| BR02 LaterEpisode | Mismo reset y contador; aceptar únicamente señales Cq posteriores a la primera, contador>=2. Cada señal mantiene LIMIT/caducidad originales. | BR01. No es una inversión de dirección ni un vecino de longitud; hipótesis de madurez del episodio. |
| BR03 RetestHoldMarket | Origen Cq congela nivelL=highDonchian y highH de la vela de ruptura. En las cuatro barras filtradas POSTERIORES, primer touch low<=L: si su close>L, MARKET al close fresco. Si close<=L, descartar para esta receta. | BR04 y Cq/M existentes como contexto. Aceptación del techo recuperado al cerrar frente a compra pasiva sin confirmación. |
| BR04 RetestReclaimMarket | Mismo origen y primer touch; requiere close<=L en ese touch y una barra FUTURA dentro de la vida del episodio que cierre>L. MARKET en ese primer reclaim fresco. Si el primer touch sostuvoL, no entra. | BR03. Diferencia hold inmediato de recuperación después de fracaso; ambas long, no short de rechazo. Poblaciones distintas: no causal puro. |
| BR05 RetestHighStop | Mismo evento hold y mismas condiciones de BR03. En vez de MARKET, ordenar compra al high de la vela de retest; STOP previsto si queda encima de precio, MARKET si ya está alcanzado según semántica del motor. Orden vive una barra, sin reemplazos. | BR03 y BR06. Exige continuar la propia vela de rechazo, no sólo cerrar sobreL. |
| BR06 BreakoutHighStop | Mismo evento hold de BR03/05. Usar como umbral de compra el highH de la ruptura ORIGINAL, no el high de retest. Si el close actual ya superaH, MARKET actual; si no, STOP enH. Vida una barra y sin reemplazos. | BR05. Reafirmar el máximo original frente a continuar sólo la barra local. Cambia ancla de precio, no un número cercano. |

## Estados y causalidad que deben cerrar antes de código

BR01/02 actualizan reset/contador incluso ocupados; cuentan señales de PRECIO/eligibilidad, no planes condicionados al saldo o posición. Arranque de época no observado se considera censurado hasta el primer reset observado; cash de arranque forma parte del resultado. Una primera señal ignorada por ocupación consume su ordinal: no reaparece al cerrar posición. El midpoint es definición exante de corrección dentro del mismo canal26, no un filtro ajustado para aumentarN.

BR03..06 comparten el mismo generador de episodios independiente de posiciones. Sólo uno activo; no sobrescribirL/H por un high futuro. Vida fija de cuatro barras4h filtradas posteriores, aproximadamente una ventana de observación del activo, sin ajuste por resultados. Con huecos/fines de semana cuatro observaciones no son16horas reales: registrar tiempo real y no inventar cotizaciones. Armingbar no es touch. Mantener episodio hasta su vencimiento común aun si una política consume su trigger antes, para impedir rearme desigual sólo por entrar más pronto.

Las confirmaciones sólo se conocen al cierre de una barra posterior. Ni el low que tocóL ni el high ya ocurrido se usan para simular un fill retroactivo: MARKET se envía alclose actual y STOP sólo para futuro. Smart-order puede convertir precios cercanos en MARKET (tolerancia conocida1.5bps); clasificar tipos ejecutados y no afirmar confirmación estricta por encima de un tick sin soporte del motor.

Si un trigger ocurre ocupado, fuera de ventanaentry, sin freshquote o sin régimen válido, se consume sin cola/replay. La señal BR04 es el futuro reclaim, no una orden en espera desde un cierre inválido. STOP permanece sólo la vida original de una barra; gestión de posición conserva comportamiento24/7 original.

Frecuencia exante: BR01/02 dividen oportunidades originales y probablemente tengan muestra menor queCq; BR04 puede ser especialmente escasa. BR03/05/06 comparten oportunidades, no muestras independientes. SiN es bajo se declara inconcluso y no se alarga la espera ni se relajan gates. No prometer30trades a partir de31fills de la referencia.

## Solapes y exclusiones

No propongo compresión→expansión: SqueezeRelease5m y QuietChannel ya fueron descartadas, y cambiar periodo/bandas no resuelve novedad. Tampoco ORB/Drive, gapsRTH SPY20, entropía/ciclo/densidad ni dos tests previos a ruptura de SPY40-10.

BR01/02 alteran la historia ordinal de eventos, no g/ADX/EMA vecinos de R60. BR03/04 pertenecen a aceptación/fallo de nivel ya presentes en el inventario; la diferencia concreta es techo conocido tras ruptura bullish y largo posterior bajo la gestión de referencia, frente a fallos de rango/shorts previos. No los denomino familia inédita. BR05/06 contrastan dos anclas causales de precio en el MISMO hold, sin reoptimizar stop. Se diferencian de la otra línea: no usan mínimo de corrección, insidebar, higherlow ni microcanal1h.

## Decisión y siguientes rondas

Comparar todas las seis y la referencia existente por neto/fees/PF/Sharpe/DDmotor y MTM, N, duración, turnover, exposición temporal/notional-tiempo, stress estático5/10bpsRT, exbest/ex3 y concentración por episodio/año. Pares por origen conocido y fill común sólo si son inequívocos; diferencia de ocupación explícita. No escoger el máximo de tabla sin mejora económica y pregunta mecánica defendible. Cq/M son referencias históricas, no controles idénticos de calendario de oportunidad.

R2 sólo si una idea cambia materialmente la evidencia: fijar UNA por línea y contrastar mecanismo/selección de ejecución/exposición, no vecinos para salvarla. Seis es cupo, no seis controles artificiales si algunos se resuelven por análisis de snapshots. R3 sólo tras sobrevivirR2, con las candidatas fijas y baseline compartida por bloque, sin abrir2026 ni llamarloOOS.

Propuesta pendiente de revisión root. No autoriza código, backtests, instalaciones ni cambios ajenos.