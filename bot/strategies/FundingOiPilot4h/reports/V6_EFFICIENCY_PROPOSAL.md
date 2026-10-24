# V6 EFFICIENCY — eficiencia direccional finita en 4h

Autor: /root/v6_efficiency, subagente dedicado al sector. Estado: diseño previo a implementación y economía V6. No se crearon estrategias, drafts, jobs analíticos ni backtests. La especificación se define sin consultar resultados nuevos V5, antes de escoger líneas según su PNL. Root debe incorporar esta propuesta en el protocolo y registro global antes de autorizar código o motores.

## Hipótesis y revisión de parentesco

Un desplazamiento neto de varios días que representa una fracción suficientemente grande de todo el recorrido de cierres puede señalar una transición hacia movimiento direccional persistente. La señal mide rectitud de la trayectoria, no sólo distancia entre dos medias o ruptura de un extremo. Se propone seguir el primer cruce de eficiencia y salir cuando la dirección neta de la ventana deja de favorecer la posición. Es una hipótesis falsable; no se presume que reduzca whipsaws o mejore rentabilidad.

Se revisaron por MCP los cierres V1–V4, RESEARCH_PROTOCOL_V1.md, V3_TREND_CHANNEL_PROPOSAL.md, V3_TREND_PULLBACK_PROPOSAL.md, V3_RANGE_REVERSION_PROPOSAL.md y las propuestas V5 CROSS, VWAP y FUNDING_TREND. El diseño no coincide exactamente con sus reglas:
- V1/V2 comparaban precio con extremos del día UTC o retornos, con gates de funding/OI. EFFICIENCY normaliza el desplazamiento por el recorrido absoluto de cierres, sin extremos diarios o señal funding.
- V3 CHANNEL exigía ruptura de un canal excluyendo la barra actual, régimen SMA120 y pendiente; gestionaba trailing y siete días. Aquí no hay canal, régimen SMA ni trailing.
- V3 PULLBACK requería toque y reanudación de tres barras; aquí no hay patrón de toque.
- V3 RANGE y V4 oscilador/shock/reset estudiaron reversiones o normalización. Esta regla sigue persistencia direccional de cuatro días.
- V5 CROSS20/80 detecta cambios de orden de medias; EFFICIENCY no calcula medias de tendencia y puede rechazar un recorrido zigzagueante aunque termine con desplazamiento y medias ordenadas.
- V5 VWAP utiliza centro y dispersión ponderados por volumen; V5 FUNDING_TREND utiliza nivel persistente de funding y precio20d/5d. EFFICIENCY no usa volumen ni funding como gate.

Existe parentesco amplio con continuación tendencial, especialmente CHANNEL y CROSS. No es un experimento estadísticamente independiente: usa el mismo activo y años ya examinados. Cambian conjuntamente entrada, salida, stop y duración respecto de esas líneas; cualquier diferencia de PNL no identificará el efecto aislado del cociente de eficiencia.

V1–V4 terminaron sin candidata; CHANNEL_P V3 conservó evidencia parcial, no promoción. Los 151 backtests económicos nuevos y la reserva interna reutilizada se mantienen visibles. Un nuevo prerregistro limita discreción futura, pero no restaura independencia de los datos. No se declara una búsqueda exhaustiva de estrategias legacy ajenas a estos protocolos.

## Universo y reloj

BTC-USDT Binance Perpetual Futures, decisión4h UTC y ejecución histórica1m completa. Mercado24/7; una ruta, una posición neta, ambos lados simétricos, sin pirámides, parciales o entradas retenidas.

BAR=14.400.000ms y DAY=86.400.000ms. En la decisión T, C_k es el cierre de la barra que terminó exactamente en T−k*BAR. La barra actual B0 abrió T−BAR. Usar sólo filas con open_time+BAR<=T; última apertura exacta T−BAR, alineación4h UTC y timestamps consecutivos.

Cada OHLC exigida debe ser finita, positiva y coherente: high>=max(open,close), low<=min(open,close), high>=low. No rellenar, comprimir, reordenar o sustituir filas ausentes. Las filas futuras quedan fuera de toda validación y cálculo: mutarlas no puede cambiar señales históricas.

Warmup240velas4h, sin operar, suficiente para todas las ventanas definidas. El warmup no aporta una historia OI ficticia anterior al comienzo de sesión.

## Fórmula finita y ventana mínima

Para desplazamiento histórico k=0 o1:

D_k=C_k−C_(k+24).
L_k=sum(abs(C_j−C_(j+1)) para j=k,...,k+23).
E_k=D_k/L_k cuando L_k>0.

Se usan24 diferencias y25 cierres por estado. La escala de desplazamiento es24×4h=96h, cuatro días. Si todos esos cierres son idénticos, L_k=0 y se fija E_k=0 válido y neutral. No se usa epsilon para convertir ruido o cero en otra señal.

**Entrada requiere26 cierres consecutivos:** E0 usa C0...C24; E1 usa C1...C25. E1 se calcula con su propia ventana, no con un valor parcial de E0. Esta precisión fue comunicada y ratificada por root antes del prerregistro. No bastan25 cierres para el cruce. La salida por estado sólo necesita25 cierres para E0.

Implementación numérica propuesta y fijada: calcular las24 diferencias finitas; m=max(abs(delta)). Si m=0, devolver E=0 neutral. Si m>0, usar E=(D/m)/fsum(abs(delta)/m). Esta normalización común evita desbordar la suma de diferencias finitas y es algebraicamente el cociente anterior. Exigir que D, cada delta, m, suma normalizada y E sean finitos, con denominador positivo. No clamp, redondeo o epsilon antes de comparar umbrales. El cociente matemático pertenece a[−1,1]; las comprobaciones con oráculo admiten tolerancia numérica exclusivamente al comparar resultados calculados, nunca cambian desigualdades de señal. La aritmética inválida devuelve features inválidas con campos JSON seguros, sin NaN/Infinity.

Un helper puro deberá recibir candles, now y threshold, sin engine state, IO, red, APIs privadas o indicador inventado. Estado actual/previo, desplazamiento, recorrido normalizado, primeros/últimos timestamps, número de cierres y hash de la ventana quedarán disponibles como evidencia acotada.

## Entrada nominal: cruce fresco

Umbral nominal h=0,35.

- Long si E1<=h y E0>h.
- Short si E1>=−h y E0<−h.

La igualdad previa permite un cruce; igualdad actual no abre. Permanecer por encima o debajo del umbral no permite nueva entrada. Los lados son excluyentes para h>0. No añadir confirmación por color de vela, desplazamiento mínimo en ATR, régimen SMA, ADX, volatilidad, volumen, día/hora o funding.

Entrada MARKET a precio de decisión sólo estando plano, sin pendiente, con cuota UTC libre, start<T<finish y a<T<b en el intervalo activo correspondiente. Una entrada ejecutada como máximo por díaUTC, compartida entre long/short. Una entrada de seguridad consume cuota; un rechazo no la consume.

Una señal bloqueada por posición, cuota, OI, dato inválido o plan no se conserva para después. Después de stop o máximo holding se necesita un nuevo cruce fresco; no reentrar por estado persistente. No abrir en la misma decisión que un cierre previo y no guardar una reversión pendiente para la barra siguiente. Si un cruce opuesto coincide con una salida, no se convierte silenciosamente en stop-and-reverse.

## Salidas, protección y duración

ATR A es la media aritmética de14 true ranges de15 OHLC4h cerradas terminadas en T:
TR=max(high−low,abs(high−previous_close),abs(low−previous_close)).
No Wilder/EMA ni barra en formación. A>0 finita; offset0, incluye la barra de señal.

La distancia nominal d=2,5A se congela antes de entrar. Tras fill real e:
- Stop long=e−d.
- Stop short=e+d.

Sin objetivo LIMIT, trailing, break-even, cambio de distancia por ATR posterior o salida adicional de canal/medias. Instalar protección por toda la cantidad inmediatamente. Si stop posterior al fill no es válido, liquidar MARKET de seguridad, registrar motivo y conservar el trade y sus costes.

Gestionar el indicador sólo en un cierre estrictamente posterior al fill:
- Long: salir MARKET cuando E0<=0.
- Short: salir MARKET cuando E0>=0.

Es salida de estado, no cruce. La igualdad o una ventana plana válida cierran; un dato inválido no inventa neutralidad. La salida necesita sólo25 cierres válidos y no depende de ATR actual, Eprev, OI o disponibilidad de funding. Si no hay E0 válida, conservar el stop y esperar otra decisión válida; los límites de duración y calendario siguen activos.

Holding máximo60barras4h=240h=10días de tiempo absoluto desde opened_at, no60 llamadas. En decisión: prioridad calendario, después edad>=60*BAR, después salida por eficiencia; protección intrabar del motor conserva precedencia temporal. Una sola solicitud MARKET por decisión. El último cierre del fold incluye la liquidación forzada y costes. No usar barras posteriores al corte para terminar posiciones de entrenamiento.

El umbral0,35 exige desplazamiento neto mayor al35% del recorrido de cierres de cuatro días; no equivale a35% de rentabilidad. Stop2,5ATR es protección local intermedia fijada por diseño; hold10d acota la exposición de un mecanismo multidiario. Ninguno es una estimación óptima o una garantía de capturar tendencias.

## Tamaño y costes

Capital inicial10.000USDT por sesión, isolated3x, cap nocional1x y riesgo previsto2% incluyendo fees de entrada/salida al stop:
C=available_margin antes de la orden; p=precio de decisión; s=+1long/−1short.
stop_pre=p−s*d.
u=d+f*(p+stop_pre).
q=floor8(min(C/p,0,02*C/u)).

Exigir capital, precio, distancia, stop_pre y cantidad finitos y positivos; fee finita>=0. El leverage no multiplica tamaño. Los límites de riesgo y nocional se verifican con el precio prefill; funding, gaps y slippage pueden excederlos en ejecución. No redimensionar retrospectivamente usando un fill conocido después.

Fee nominal0,00045por lado; slippage nominal0bps; funding contable históricoON en las dos ablaciones. No significa estimación exhaustiva de costes reales. Configuración exacta por sesión, sin cambiar config global o framework.

Datasets heredados y versionados:
- Funding:9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571.
- OI:6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.

Funding final disponible asofT, contabilidad con effective_at normalizado y raw settled_at preservado; marcas settlement/proxy clasificadas. No usar próximo pago estimado como feature ni cobrar retrospectivamente un pago anterior a entrada.

## Dos nominales y ablación OI

EFFICIENCY_P: regla de precio/ATR anterior; OI no condiciona disponibilidad ni entrada.
EFFICIENCY_POI: misma regla más OI actual>OI observado exactamente en T−24h; ambos valores válidos, positivos, disponibles y frescos. El filtro es igual para ambas direcciones y no interpreta OI como signo.

En4h,24h son6barras. Conservar cada slot de decisión, incluidos ausente, stale y cero. Primeras6decisiones inicializan; primera referencia posible en la7ª. Buffer nominal de al menos8registros. Sin backfill OI desde warmup, interpolación o referencias aproximadas.

OI label+6min como disponibilidad asumida; freshness máximo10min desde disponibilidad en el reloj de observación original. Archivo retrospectivo, sin certificación point-in-time. Ausencia/stale/cero o referencia inválida bloquea sólo POI, no salidas.

La sensibilidad de retrasoOI, si se alcanza esa fase, es4horas de reloj:1barra4h, current observado en T−4h y referencia T−28h. Conservar calidad en sus relojes originales, sin extender stale. Primeras7decisiones inicializan; primera referencia posible8ª y buffer mínimo9. No retrasar4barras4h por arrastrar un escenario horario anterior. P reutiliza su nominal cuando el slot de lag es equivalente.

## Vecinos exactos, sin grilla

Sólo si la nominal llega a robustez y root autoriza esos slots:
- Riesgo R09:stop2,25A.
- Riesgo R11:stop2,75A.
- Señal A09:h=0,315 para ambos lados.
- Señal A11:h=0,385 para ambos lados.

Los vecinos de riesgo mantienen h0,35, ventana24diferencias, salida0, hold60 y restantes reglas. Los de señal mantienen stop2,5A y sólo cambian h de entrada actual/previa; salida0 y ventana24 quedan fijas. No cambiar conjuntamente hold, ATR, período o OI. No elegir el mejor vecino, añadir combinaciones o promover un vecino cuando falla la nominal.

Cada vecino exigido debe mantener neto positivo y DD<=25%; informar también N,PF,CAGR,meses y semestres. La pequeña vecindad no demuestra robustez exhaustiva.

## Gates y fases comunes

Root fija presupuesto V6, nombres definitivos y configuración antes de economía. Este sector aporta sólo dos nominales nuevas, no reutiliza resultados de CHANNEL/CROSS.

Screen propuesto común[2020-09-01,2024-01-01), cuenta continua10.000USDT: N>=30,neto>0,PF>=1,2,absDDmotor<=25% y al menos2/3años completos2021–2023positivos por equity.2020parcial se informa aparte. No se introduce gateCAGR de desarrollo.

Shortlist de hasta dos según ranking común menorabsDD,mayorPF,menorturnover,menor complejidadOI eIDestable. Fijar fuentes/hashes/config/shortlist antes de consultar economía2024–2025 de estas reglas. La confirmación es interna reutilizada, no OOS virgen.

Cuatro semestres2024–2025, train expansivo desde2020Sep; elegibilidad y selección anteriores a cada evaluación. C1train puede reutilizar el screen únicamente si todo es exacto. Calendario individual de replay nominal fijado por train, no por PNL de evaluación. Selector global separado del mejor finalista individual posterior.

Replay continuo[2024-01-01,2026-01-01),731días, capital transportado y cierres semestrales sin reset: N>=100,neto>0,PF>=1,2,DD<=25%,>=3/4semestres positivos y CAGR>=15%. CAGR=(saldo_final/10000)^(365/731)−1. La meta orientativa20–30%anual no se acredita promediando folds o anualizando sólo tiempo expuesto.

Fricción heredada:S1fee0,0009/slip0;S2fee0,00045/slip5bps;S3fee0,0009/slip10bps. S1/S3 requieren neto positivo yDD<=25;S2 se reporta sin gate adicional. Cantidades y fills se recalculan por motor, no haircut. Vecinos y lag anteriores mantienen calendario nominal. Sensibilidades proxy-only/global funding×0,5/1,5 con cantidades fijas son análisis descriptivos, no replays ni oportunidades de promoción.

Si falla muestra o cualquier filtro, conservar el fallo. No agregar reentradas, acortar ventanas/holding o sumar trades de otros ciclos para llegar a100. No reasignar slots omitidos a tuning.2026 queda cerrado; la nueva autorización V5/V6 no lo abre. Sin ML, live/paper, órdenes reales, Pi, cuentas, paquetes, reinicios, commits o push.

## Checks deterministas previstos, aún sin ejecutar

1. Oráculo manual de24deltas para eficiencia actual y previa; trayectoria monotónica±1, plana0, zigzag con desplazamiento nulo0 y dos caminos con mismo desplazamiento pero distinto recorrido. Verificar invariancia a multiplicación positiva y traslación de precios que conserve OHLC>0.
2. Ventana propia E1; entrada exige26cierres, salida25. Prefijos anteriores y mutación de filas futuras no cambian resultados. Timestamps4h exactos, gaps/duplicados/desalineación invalidan.
3. Long/short por reflexión de OHLC positivos; igualdades previas/actuales en±h; estado persistente no reentra; cero válido neutral; valores inválidos no se convierten enE0.
4. Normalización numérica con sumas grandes y diferencia finita; rechazar NaN/Inf/negativo/OHLC incoherente, mantener JSON sin NaN. Tolerancias sólo del oráculo, sin cambiar desigualdades económicas.
5. Salida por estado0 y por ventana plana, sóloT>opened_at; no necesita Eprev/ATR/OI. Sin entrada contraria en la misma decisión, latch o cruce reconstruido después de dato inválido.
6. ATR14aritmética/15OHLC, stop2,5A fijo desde fill,fee del escenario en tamaño,cap1x/floor8/seguridad posterior al fill. No TP/trailing ocultos.
7. CuotaUTC compartida y cambio de día; mismo cierre bloquea reapertura; una solicitud de liquidación porT. Hold60*BAR exacto, calendario prioritario y protección activa ante features inválidas.
8. OI24h=6barras ylag4h=1barra, referencias exactas, slotsNone/cero, calidad en reloj original y ausencia de warmupOI.
9. Logs JSON<=1900caracteres: parámetros/E0/E1/D/recorrido/first/last/hash, ATR/plan/riesgo/qty/fill/stop,OI/provenance y motivos de salida. Counters por mes/dirección y particiones exclusivas concilian barras, oportunidades, rechazos, entradas y cierres.
10. Smoke técnico fijo según protocolo común antes de economía; no alterar fechas para obtener un trade ganador. Falta de fills no acredita esa rama.
11. Snapshots completos para bruto−fees+funding=PNL/saldo con tolerancia1e−6;PF,trades únicos,DDmotor,curva diaria,meses/años/semestres,turnover/exposición/holding,longshort y concentración. Separar counters anteriores al cierre final de trades y saldo posteriores.

## Riesgos y criterio de falsación

La eficiencia de cierres omite oscilaciones intrabar que sí afectan stops; una trayectoria de cierres recta puede ocultar riesgo o gaps. La ventana móvil puede cruzar el umbral sólo porque sale un zigzag viejo, sin nueva aceleración. El umbral no elimina retraso ni falsas transiciones; la salida neta0 puede devolver ganancias antes de cerrar. Los cruces frescos más cuota pueden producir menos de100trades y omitir tendencias después de un stop. OI creciente puede confirmar congestión adversa y su archivo es retrospectivo. Funding y costes pueden borrar una ventaja bruta.

Se considerará fracaso económico o evidencia insuficiente conforme a los gates, no permiso para cambiar h, ventana, salida, stop, duración o dirección después de resultados. Una rentabilidad aislada no constituye candidata aprobada. Sólo esta propuesta está autorizada ahora; no implementación o motores sin GO global.
