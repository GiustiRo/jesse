# V4 — propuesta de reversión de shock de precio y volumen en 1h

Estado: propuesta previa a resultados, sólo diseño. Dueño: /root/atr_oi. No se crearon estrategias, drafts, motores ni jobs. DOCS.md vigente leído: «Timeframes: A explorar/definir» y «Prioridad: rentabilidad, no frecuencia». Se aplica backtest-expert: hipótesis explícita, reglas sin discreción y parámetros congelados antes de medir. V4 consume dos configuraciones nuevas; no retoca V3 ni su evidencia.

## Hipótesis y mecanismo

Después de una hora cuyo cambio de cierre supera dos veces la volatilidad previa y cuyo volumen duplica el promedio diario previo, parte del desplazamiento podría revertirse durante las seis horas siguientes por agotamiento transitorio de órdenes agresivas. Esto es una hipótesis falsable. OHLCV no identifica liquidaciones, profundidad de libro ni un verdadero clímax de liquidez; sólo proporciona un proxy de shock. También puede detectar incorporación persistente de información, en cuyo caso la reversión perderá.

Es distinto de RANGE: no exige baja deriva ni canal estable, y opera inmediatamente contra un desplazamiento anormal. Es distinto de PULLBACK4h: no exige tendencia ni espera reanudación; la posición va contra el shock reciente. No hay filtro SMA/EMA, oscilador, financiación predictiva ni confirmación posterior.

## Universo, reloj y datos permitidos

Sólo BTC-USDT Binance Perpetual Futures; velas de una hora; una posición neta, sin piramidar. Se propone usar el mismo motor económico ya auditado con interfaz de timeframe1h que root consolidará antes de implementar. No se modifica el framework ni se presume que una base con BAR4h sirva sin adaptación explícita.

En cada decisión horaria T UTC sólo se usan velas cerradas con timestamp de apertura t y t+3600000<=T. La vela shock s es la última cerrada, abierta en T−3600000; no se usa la vela en formación abierta en T. Los datos de señal requieren exactamente las últimas25 velas cerradas consecutivas, de s−24 a s. Los timestamps deben aumentar exactamente3600000ms y estar alineados a horas UTC. Este requisito cabe holgadamente en warm_up_candles240 de 1h. El historial OI24h usa25 snapshots horarios, también acotados; no hay indicador con semilla recursiva.

Cada precio O/H/L/C debe ser finito, positivo y coherente: L<=min(O,C)<=max(O,C)<=H. Cada volumen V debe ser finito y no negativo. Se usa el campo volumen de vela normalizado de Jesse (volumen base BTC), de forma consistente en numerador y denominador; se verificará su procedencia antes de cualquier ejecución. No se sustituye por volumen quote, no se suma OI ni se interpolan huecos. Cualquier fallo de calidad invalida la decisión, sin señal.

## Cálculos exactos y señal nominal

Para j=s−14,...,s−1:

TR_j=max(H_j−L_j, abs(H_j−C_{j−1}), abs(L_j−C_{j−1})).

A=(TR_{s−14}+...+TR_{s−1})/14. Es ATR14 mediante media aritmética simple de14 true ranges previos; excluye completamente la vela shock y no tiene semilla Wilder/EMA. Debe ser finito y >0.

B=(V_{s−24}+...+V_{s−1})/24. Es volumen promedio de las24 horas previas, excluye la vela shock y debe ser finito y >0.

D=C_s−C_{s−1}.

Evento shock si y sólo si abs(D)>=2*A y V_s>=2*B. Las igualdades cuentan. D no puede ser0 al exigir A>0. No hay requisito adicional de cuerpo, wick, rango, cierre extremo, drift, noticia ni volumen futuro.

Dirección:
- D<=−2*A y V_s>=2*B: LONG (+1).
- D>=+2*A y V_s>=2*B: SHORT (−1).
- Cualquier otro caso: sin entrada.

Ambas ramas son espejo; nunca pueden activarse juntas. Una vela shock sólo se procesa una vez en su decisión T: sin latch, búsqueda retrospectiva ni señal diferida.

Si está flat, sin orden pendiente, dentro del calendario activo congelado, sin entrada previa ese día UTC y pasa la variante correspondiente, se envía una orden MARKET contraria en T. La decisión usa C_s como precio de referencia; el precio de entrada es el fill real p_e, sujeto al deslizamiento del escenario. No se asume poder entrar antes del cierre shock, en su mínimo/máximo ni al precio anterior al evento. Señales ocurridas mientras hay posición se descartan, sin acumulación.

## Stop, objetivo y vencimiento congelados

Se congela A al decidir la entrada; nunca se recalcula durante la operación. Distancia de stop R=A. Para dirección d en {−1,+1}, desde el fill real p_e:

stop=p_e−d*A; objetivo=p_e+d*A.

Objetivo fijo1R; sin trailing, breakeven, salida de tendencia, parcial ni promedio. Ambos niveles deben ser positivos, finitos y representables; si el plan no es válido se rechaza la entrada antes de enviar, y la validación posterior al fill utiliza el manejo de seguridad ya auditado.

Máximo de seis horas: en la primera decisión con T_actual>=T_fill+6*3600000 se solicita MARKET si sigue abierta. MAX_HOLD_BARS=6 sobre el reloj1h, sin contar la vela shock ni liquidar al final de la sexta vela incorrecta por desfase. Un cierre de calendario tiene prioridad a maximum_hold en la misma decisión. Los stops/objetivos ya vivos pueden ejecutarse intrabar antes de esa decisión; no se rehace retrospectivamente el recorrido. El motor debe conservar su resolución intrabar real y auditar cualquier ambigüedad stop/objetivo en la misma vela mínima; no se presenta la convención del motor como evidencia de trayectoria observada.

Los cierres del calendario activo y del final de sesión fuerzan flat y bloquean entradas en sus bordes estrictos, como el protocolo global. No se transporta posición por un intervalo inactivo. La propuesta no abre 2026; root fijará la cronología de desarrollo/confirmación antes de economía.

Racional de salida: para el evento mínimo2A, un beneficio de1A representa recuperar la mitad de ese desplazamiento desde el fill nominal; no se fuerza volver exactamente al cierre anterior ni se exige continuación favorable3R. Stop1A permite otro movimiento adverso equivalente a media magnitud del umbral mínimo del shock; no permite alejarlo después. Seis horas limita la tesis al desbalance transitorio en vez de convertirla en apuesta de días. No se eligen estos valores por resultados ni para incrementar frecuencia.

## Dos variantes nuevas, únicas

1. VOLUME_SHOCK_1H_PV: exactamente señal de precio+volumen anterior; OI observado sólo para auditoría si la base lo recoge, nunca bloquea.
2. VOLUME_SHOCK_1H_PVOI: exactamente la misma señal y economía, más gate OI24h estricto positivo.

Gate PVOI: en cada decisión horaria T se conserva el snapshot de OI disponible en ese momento con las políticas temporales/versionadas comunes. Comparar quantity_base(T)>quantity_base(T−24h). Ambos extremos deben ser finitos, >0 y válidos; igualdad o descenso bloquean. El extremo de T−24h es el snapshot realmente guardado en aquella decisión; no una consulta retrospectiva que incorpore publicaciones tardías. Ring buffer25 slots horarios, incluidos slots inválidos: no se comprime el tiempo quitando observaciones ausentes, no se hace forward-fill. Sólo se necesitan válidos ambos extremos, no se inventa condición sobre las23 observaciones intermedias.

La validación as-of exige available_at<=su decisión, label<=available_at y antigüedad<=600000ms, usando sin alterar el dataset versionado con supuesto de disponibilidad+6min y publicación original desconocida. Primera referencia incompleta bloquea PVOI y se registra initialization. Missing/stale bloquea, sin look-ahead. A resolución1h,24h son24 barras, no6 barras4h. No se agrega un gate por signo/magnitud de funding. El gate OI no es certificado point-in-time y conserva esa limitación de procedencia.

Esto es ablación del requisito OI: PV mide el evento de precio/volumen; PVOI añade sólo OI24h. No hay una tercera configuración sin volumen, ni búsqueda de ventanas/umbrales.

## Economía común, intacta

Balance inicial10000 por sesión; isolated3x contable, pero límite de exposición notional1x del capital disponible: no se confunde leverage del exchange con capC. Riesgo objetivo máximo2% por stop más fees de entrada/salida. Para fijar la intención de sizing, con capital E antes de la orden, comisión taker f y stop previsto p_s:

q_risk=0.02*E/(A+f*(p_e+p_s)); q_cap=E/p_e; q=floor_a_precision(min(q_risk,q_cap)).

La implementación debe conservar las validaciones, redondeo y protección de fill reales del núcleo auditado; esta fórmula explicita el presupuesto nominal. Si cap1x limita q, se acepta riesgo realizado inferior al2%; no se ajusta R para gastar presupuesto. La decisión planifica con el precio disponible, luego el fill/slippage real define niveles, logs y validación de capital/riesgo sin inventar conocimiento anticipado del fill. Funding acumulado, gaps y fricción de ejecución no están garantizados por el presupuesto de stop+fees y se miden separadamente.

Fee nominal0.00045 por lado, slippage nominal0bps, funding histórico contable ON y datasets congelados del protocolo. No usar defaults globales con funding disabled ni leverage5x. Los estreses exactos los consolidará root antes de resultados; no se crean escenarios extra aquí.

Máximo una entrada por día UTC, compartida entre long y short dentro de cada variante/sesión. Día=floor(T_fill/86400000); el fill de apertura consume ese día. Señal bloqueada por calidad/OI/cap/posición no consume cupo ni queda pendiente; un fill cerrado inmediatamente por seguridad sí lo consume. Si una señal cierra a00UTC se evalúa en el nuevo día de su decisión/fill, aunque su vela shock se abrió el día anterior. Sin reentrada en ese día después del stop/objetivo/hold. Una posición previa no impide una entrada posterior de otro día sólo tras estar flat y cumplir una señal nueva.

## Precompromiso y validación futura, sin ejecución ahora

Todos los números quedan propuestos antes de ver cualquier PnL: timeframe1h; ATR14simple previo; volumen24previo; umbrales2A/2B; stop1A; objetivo1A; máximo6h; OI24h estricto sólo en PVOI. Root puede resolver incompatibilidades de interfaz antes de congelar fuentes; cualquier decisión debe quedar escrita antes de resultados.

No se cambia el mínimoN100, ni los gates de CAGR/PF/drawdown/mayoría temporal/robustez establecidos. Se aplica el protocolo global completo, con presupuesto de dos nuevas configuraciones y confirmación cronológica definida por root; no se escoge la variante por mirar futuro, no se reciclan evaluaciones V3 como train nuevo sin declararlo y no se abre2026. Un N insuficiente es rechazo, no autorización a relajar umbrales o aumentar frecuencia.

Antes de economía corresponde verificar con checks puros: shock exacto en ambos umbrales; espejo long/short; exclusión de vela shock de A/B; ATR constante sin semilla; invalidación por hueco/volumen0promedio/NaN/OHLC; invarianza al anexar vela futura; igualdad OI bloqueada, lag exacto24h y slot inválido sin compresión; cupo UTC de medianoche; stop/target desde fill; sizing+fees+cap; maxhold6h y prioridad de calendario. Esto es un plan, no pruebas ejecutadas.

Riesgos materiales:
- Un shock de alto volumen puede ser continuación informativa, no agotamiento; no hay filtro que lo evite y no se añadirá según pérdidas observadas.
- Reversión1h puede depender más de spread, gaps y trayectoria intrabar; stop/target1A puede tener márgenes netos bajos bajo costes.
- Volumen24h sólo compara con el día previo y no corrige estacionalidad horaria/semanal ni cambios estructurales; esa sencillez es deliberada.
- OI de archivo es retrospectivo con disponibilidad supuesta, y el gate risingOI puede seleccionar precisamente continuación contra la reversión.
- Cap1x puede reducir utilización del riesgo; una operaciónUTCdía puede omitir shocks posteriores, sin selección discrecional del mejor.
- La normalización por volatilidad previa aumenta el tamaño relativo de un shock respecto a su escala, pero no demuestra liquidez suficiente ni edge.

Entrega limitada a este documento. Sin código, fuentes productivas, drafts, backtests, jobs de análisis ni modificaciones a V3.
