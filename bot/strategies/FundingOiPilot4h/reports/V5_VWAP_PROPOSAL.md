# V5 — reversión con reingreso a VWAP móvil de 24 horas

Estado: propuesta previa a implementación y resultados V5. Dueño: /root/atr_oi. Único entregable: este documento. No se crearon fuentes, drafts, jobs ni motores. Root consolidará protocolo, cronología y presupuesto antes de cualquier prueba. Sólo MCP local; V1–V4 permanecen intactas y 2026 cerrado.

## Hipótesis y diferencia respecto a lo estudiado

Una excursión respecto al centro de negociación ponderado por volumen del último día puede revertir después de que un cierre vuelva dentro de su banda y el precio corrija hacia ese centro. La salida busca normalización respecto al centro móvil actual, sin fijar una ganancia mínima ni asumir que ese centro permanecerá estable.

Antecedentes leídos completos por MCP: RESEARCH_PROTOCOL_V1.md, RESEARCH_PROTOCOL_V2_20261020.md, V3_RANGE_REVERSION_PROPOSAL.md, V3_TREND_PULLBACK_PROPOSAL.md, V4_VOLUME_SHOCK_1H_PROPOSAL.md y V4_OSCILLATOR_1H_PROPOSAL.md. El nombre inicialmente buscado V3_RANGE_PROPOSAL.md no existía; se localizó el correcto desde REGISTRY_V3. No se consultaron resultados económicos nuevos ni precios para elegir reglas.

El parentesco con la familia de reversión es explícito; no representa evidencia estadísticamente independiente:
- RANGE4h entraba en una excursión nueva hacia fuera, contra una media no ponderada de 20 cierres (~80h), con filtro de baja deriva y objetivo LIMIT congelado. Aquí se espera reingreso y corrección real, el centro pondera volumen de 24h, no hay filtro lateral y la salida es un estado de VWAP móvil.
- SHOCK1h exigía cambio de una vela >=2 ATR previos y volumen >=2 veces su media anterior; entraba inmediatamente contra el shock. Aquí no hay umbral de cambio de una vela ni pico de volumen obligatorio: la excursión puede desarrollarse gradualmente.
- OSC1h exigía cruce RSI2 y tendencia SMA200/24, saliendo por RSI50. Aquí no hay RSI ni régimen de tendencia; el volumen determina centro y dispersión.
- H2V1 reingresaba al rango H/L del día UTC anterior. Aquí no hay extremos del día ni ancla UTC: son ventanas móviles de 24 horas, con salida al centro ponderado.

No se afirma que estos cambios produzcan ventaja. Si root juzga insuficiente este diferencial antes de resultados, corresponde excluir la línea por redundante, sin ejecutarla para decidir retrospectivamente si merece llamarse nueva. No se agrega otra hipótesis dentro de este entregable.

## Universo, reloj y calidad

BTC-USDT, Binance Perpetual Futures, decisiones 1h UTC continuas y ejecución histórica 1m según contrato del motor. Una posición neta, sin piramidar, parciales ni entrada retenida.

T es la decisión horaria. El índice i cuenta barras hacia atrás: B0 abre en T−1h y termina en T; B1 es la anterior. C_i/H_i/L_i/O_i/V_i son sus valores. Para entrada se requieren exactamente las últimas 25 velas cerradas B24,...,B0, consecutivas y alineadas a horas UTC. La última apertura debe ser T−3600000; sólo filas con apertura+3600000<=T. Warmup de 240 velas 1h, sin operar.

Todo OHLC requerido debe ser finito, positivo y coherente: L<=min(O,C)<=max(O,C)<=H. V es volumen base BTC, finito y >=0. Huecos, duplicados, NaN/Inf, OHLC incoherente o volumen negativo invalidan la decisión. No imputar, interpolar, comprimir horas o sustituir filas faltantes por otras más viejas. Las filas futuras se ignoran incluso si contienen valores inválidos.

## VWAP proxy y dispersión: cálculo exacto

Precio típico X_i=H_i/3+L_i/3+C_i/3. Se elige HLC3, no close. El centro es un proxy OHLCV de VWAP: no es el VWAP exacto de ticks/fills ni el notional real dividido por BTC. No presupone órdenes maker ni ejecución en ese precio.

Para estado k=0 actual o k=1 previo, usar i=k,...,k+23:
- Pesos α_i=V_i/ΣV_i.
- M_k=Σα_i*X_i.
- Var_k=Σα_i*(X_i−M_k)^2.
- σ_k=sqrt(Var_k), dispersión poblacional ponderada.

Implementación numérica fijada: calcular u_i=V_i/max(V de esa ventana), después α_i=u_i/Σu_i. Requiere maxV>0 y equivale algebraicamente a los pesos anteriores sin necesitar formar una suma de volúmenes grandes que desborde. HLC3 se calcula con las divisiones antes de sumar. Usar dos pasadas para media/varianza, sin E[X²]−E[X]², sin epsilon ni clamp de varianza negativa. Todo intermedio utilizado debe ser finito; varianza negativa invalida. σ=0 es válido.

Una fila con volumen0 conserva su hora y aporta peso0. Si todos los volúmenes de una ventana son0, el estado es inválido: no usar M anterior como sustituto. No hay condición adicional V0>promedio ni cantidad mínima de horas con volumen positivo. Si V0=0 pero la ventana tiene peso total positivo, su cierre puede compararse con el centro si OHLC es válido; registrar ese caso como diagnóstico fijo, sin añadir un veto después de resultados.

Cada M0/σ0 y M1/σ1 usa su propia ventana. No evaluar C1 contra el centro o banda actuales. Ambas ventanas deben ser válidas para entrada; gestión de salida necesita sólo la ventana actual de 24 horas.

El indicador vwap disponible en Jesse es anchored D según la consulta de catálogo comunicada por root. NO se usará para este mecanismo: aquí se requiere rolling24 personalizado, sin reinicio a medianoche ni dependencia de un prefijo anterior a la ventana.

## ATR, banda y única entrada nominal

ATR aritmético finito, sin Wilder/EMA:
A_k=(1/14)*Σ_{i=k}^{k+13} max(H_i−L_i, abs(H_i−C_{i+1}), abs(L_i−C_{i+1})), k=0,1.
Cada A requiere 15 OHLC y debe ser finito y >0. A0 incluye B0; A1 termina en B1. Ambos caben en las 25 velas requeridas.

S_k=max(σ_k,A_k).
Lband_k=M_k−K*S_k; Uband_k=M_k+K*S_k.
Nominal K=2.0. Si dispersión domina, la banda mide excursión respecto a los precios ponderados del día. El suelo ATR evita llamar extremo a una fluctuación diminuta alrededor de un centro casi constante; es una regla económica explícita, no epsilon. Banda inferior negativa no se trunca: simplemente ningún cierre positivo puede quedar debajo de ella.

Long si simultáneamente:
1. C1<Lband_1.
2. Lband_0<=C0<M0.
3. C0>C1.

Short, espejo:
1. C1>Uband_1.
2. M0<C0<=Uband_0.
3. C0<C1.

Se exige excursión previa estricta, reingreso actual que incluye igualdad en borde externo, permanencia del lado de entrada del centro y corrección real de precio. C0=M0 no entra. Permanecer fuera, cruzar ya el centro o cambiar sólo la banda sin corregir precio no habilita. Long/short son excluyentes por C0<M0 o C0>M0. No hay latch ni búsqueda de una excursión vieja: sólo B1/B0.

Orden MARKET en T si está flat/sin pendiente, no hubo cierre en esa misma decisión, la cuota UTC está libre y start<T<finish dentro de la ventana activa estricta. Una señal bloqueada se descarta; no ejecutarla después sin un nuevo patrón. No añadir tendencia, lateralidad, color, RSI, shock de volumen, horario, día o funding como filtros.

## Stop, salida por estado y holding

Congelar A0 de entrada. Distancia d=2*A0. Desde fill real e:
- Long stop=e−d.
- Short stop=e+d.

Stop fijo, sin trailing, breakeven, parciales ni aflojarlo. Sin take-profit LIMIT a VWAP ni objetivo R.

En cada decisión 1h posterior al fill, T>opened_at:
- Long: salir MARKET si C0>=M0 actual.
- Short: salir MARKET si C0<=M0 actual.

Es condición de estado, no cruce fresco. M0 se recalcula por la misma fórmula sobre 24 velas válidas actuales; para esta salida no se exige ventana25, σ ni ATR válidos. No reutilizar el contexto de entrada para cerrar en el mismo T. No simular fill intrabar por tocar VWAP ni insertar LIMIT retrospectiva. El centro puede moverse hacia el precio y provocar cierre sin beneficio: forma parte de la regla.

Si el VWAP de salida es inválido, conservar protección y esperar la siguiente decisión válida; no arrastrar un centro viejo. Cierre de calendario/fin forzado tiene prioridad, después máximo24h absoluto desde opened_at, después estado VWAP. MAX_HOLD_BARS=24 sobre BAR1h. Stops intrabar preexistentes preceden decisiones según motor. Holding/bordes no dependen de calidad VWAP/OI.

## Dos configuraciones nominales

VWAP_PV: precio y volumen ponderado descritos, sin gate económico OI/funding.
VWAP_PVOI: mismas reglas/economía, añade sólo OI24h creciente.

PV requiere volumen porque participa en centro/escala. Esta ablación sólo mide añadir el gate OI; no estima aisladamente el beneficio de VWAP frente a SMA.

OI actual causal válido y >0, mayor estrictamente al valor válido y >0 efectivamente observado en T−24h. Guardar slots horarios incluidos ausentes/cero/stale; referencia exacta24 barras1h, sin comprimir ni backfill desde warmup. Primeras24 decisiones inicialización. Dataset retrospectivo: disponibilidad asumida label+6m y freshness10m desde available_at; no PIT certificado. PV nunca exige calidad OI. Si root ratifica la sensibilidad común de retraso4h, comparar current de T−4h y referencia T−28h, conservando calidad en su reloj original.

## Tamaño, costes, cuota y cronología

C=available_margin preentrada, p=precio de decisión, s=+1 long/−1 short, d=2A0, stop_pre=p−s*d.
u=d+f*(p+stop_pre).
q=floor8(min(C/p, .02*C/u)).

Exigir C,p,d,stop_pre,u,q finitos y positivos, fee finita >=0. Cap notional1x, sin multiplicar tamaño por isolated3x. Si cap limita, aceptar riesgo menor al2%; no cambiar distancia para gastarlo. Plan usa precio disponible, sin conocer fill anticipadamente. Al fill real anclar stop con d congelada; protección inválida implica cierre MARKET de seguridad y entrada auditada, sin borrar trade. Funding/gaps/slippage pueden exceder presupuesto2% y cap prefill.

Capital10000 por sesión; fee nominal.00045 por lado, slip0, funding histórico contable ON incluso PV. Datasets heredados propuestos, sujetos a freeze común:
funding 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571;
OI 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
No tocar configuración global, framework o cuentas.

Máximo una entrada ejecutada por día UTC compartida long/short. Fill inmediato en T consume ese día; un fill cerrado por seguridad también. Rechazo no consume ni queda pendiente. En00UTC corresponde nuevo día aunque B0 abrió el anterior. El VWAP rolling NO se reinicia a00UTC.

Root fijará train/confirmación/presupuesto V5 antes de pruebas. Mantener gates vigentes: no bajar N100 replay, N30 screening ni PF/DD/años/CAGR. 2020–25 ya observados no recuperan independencia; 2024–25 sería confirmación interna reutilizada. V5/V6 no autorizan abrir2026. Sin shortlist, cerrar según protocolo sin reasignar reserva para rescatar nominales.

## Vecinos, sin grilla ni implementación ahora

Nominal K2, stop2A, salida VWAP actual, hold24h.
- Señal A09/A11: sólo K=1.8/2.2 en ambos estados previo/actual. VWAP24, σ, ATR14, corrección de precio, salida y riesgo iguales.
- Riesgo R09/R11: sólo stop=1.8A/2.2A; recalcular sizing con esa distancia. Señal K2 y salida VWAP iguales. No existe TP que deba multiplicarse.

Cuatro vecinos individuales ±10%, sin combinaciones ni selección del ganador. Fricción/lag sólo cuando el protocolo central congele y autorice esas fases. Un vecino no subsana N100 fallido del nominal.

## Checks y evidencia antes de economía

Plan, aún sin ejecutar:
- Oráculo manual de pesos/media/varianza; volumen uniforme equivale a media HLC3. Un único peso positivo produce M=X y σ0. Escalar todos los volúmenes por constante positiva conserva resultados.
- Ceros individuales permitidos, ventana toda cero inválida; gaps/duplicados/OHLC/NaN/Inf/negativos; normalización escalada y overflow; sin epsilon ni quotevolume.
- Ventanas actual/previa independientes;25 cierres suficientes; prefijos más viejos/futuro no cambian señal. ATR14 aritmético, A1 obtenido de su propio cierre anterior.
- Espejo long/short e igualdades de todos los bordes; permanecer fuera, ya cruzar centro y ausencia de corrección no entran. Banda movida sin cambio de precio no habilita.
- Salida de estado sólo T>fill, igualdad cierra; gestión con24 barras sin ATR; datos inválidos no bloquean stop/hold/borde; sin TP retroactivo.
- Riesgo+fees/cap1x/floor8/fill adverso; cuota UTC/midnight/same-decision; OI24h/lag4h/slots inválidos.
- JSON finito y líneas<=1900. Guardar hashes/extremos de ventanas OHLCV24/25, M0/M1, σ0/σ1, A0/A1, S0/S1, K, C0/C1, normalización de pesos, flags ceroV, razones, plan/fill/stop y M actual de salida.
- Particiones mensuales/dirección, causas exclusivas y flags, entradas/cierres forzados; conciliación bruto−fees+funding=PNL/saldo. Reportar exposición, turnover, holding, meses/años/semestres, long/short y concentración, sin sumar cuentas reiniciadas como replay.

## Riesgos y falsación

El centro ponderado puede seguir una caída persistente y parecer normalizar una pérdida. Volumen alto puede ser aceptación de un nuevo precio, no agotamiento. Cambios de pesos desplazan centro/banda aun con corrección pequeña; la condición C0>C1/espejo no elimina ese fenómeno. Velas ceroV contienen información limitada. Stop2A puede ser grande respecto al beneficio restante al centro y los costes borrar la reversión. OI creciente puede reforzar continuación adversa; cuota UTC censura oportunidades.

No se afirma ventaja frente a RANGE/SHOCK antes de medir. Si el nominal falla, documentar sin cambiar HLC3/close, ponderación,24h, sueloATR, reingreso, K, salida o hold. Esas decisiones son económicas congeladas, no reparaciones técnicas. Esperar GO global.
