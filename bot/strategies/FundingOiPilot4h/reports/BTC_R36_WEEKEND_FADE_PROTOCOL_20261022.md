# R36 A — reversión del fin de semana frente a intervalo entre semana

## Pregunta y alcance
¿Operar contra el desplazamiento BTC de sábado 00:00 a lunes 00:00 UTC produce una política neta más útil que aplicar la misma regla al desplazamiento martes 00:00 a jueves 00:00 UTC? Son ventanas exactas de 48 horas. El contraste cambia calendario de formación y día de entrada; no identifica un efecto causal puro de liquidez ni observa flujos institucionales. No supone que BTC cierre, ni traslada cierre primario Paxos o sesiones NYSE.

Es una hipótesis de reversión de presión temporal con evento semanal recurrente, sin buscar días por rentabilidad. Ambas direcciones se conservan. No procede de escoger contribuciones long de R32/R34. No relaja el ancla diaria A ni las condiciones de normalización C o cruce B de R34.

## Antecedentes y diferencia
AngleCombinedBtcWeekend4h y AngleCombinedBtcWeekdayControl4h añaden long bull sábado/martes 00 UTC por 48 horas, después de prioridad de otras recetas. Sus fuentes fueron leídas completas; no usan signo contrario al retorno de 48 horas ni operan el lunes/jueves. R20 Season (tanda T) aprende medias por seis fases UTC de cuatro horas; no discrimina fin de semana ni revierte su desplazamiento. ResearchPaxgWeekendReturn1h y WeekdayReturn1h son antecedente próximo reconocido de reversión de dos días: fijaciones NY, umbral ATR, objetivo al ancla y mecanismo de cierre primario PAXG. Ese mecanismo no se afirma para BTC y esas recetas no se copian.
R18 kNN ordenado fue descartado documentalmente como duplicado antes de cualquier protocolo/job; no se reabre.

## Reloj, señal y consumo
Fuentes propuestas: BtcResearchR36WeekendFade1m y BtcResearchR36WeekdayFade1m. Ambas heredan literalmente BtcResearchR32SpecialistBase1m, sin órdenes ni gestión propias. WEEKEND decide sólo lunes 00 UTC y usa C(T−48h) de sábado 00. WEEKDAY decide sólo jueves 00 UTC y usa C(T−48h) de martes 00. Fechas se calculan desde time UTC, nunca desde el día de apertura de la vela 4h.

El padre obtiene exactamente 64 barras 4h cerradas, consecutivas y válidas, última con apertura T−4h/cierre T; assert de paridad del cierre con self.price. C(T) es rows[-1,2] y C(T−48h) es rows[-13,2]. Los 12 intervalos entre ambos ya maduraron. Volumen no condiciona. Retorno de precio positivo => short; negativo => long; igualdad exacta => cash. Se registran desplazamiento bruto y logretorno, sin threshold mínimo ni abstención por coste adicional.

Cada slot semanal se consume una vez, incluyendo retorno cero y ventana inválida. No se difiere si ocupado, sizing falla o sale otra posición en T; estas guardas son las del padre y se aplican después de calcular el evento. Fuera del slot no hay evento. El control NO comparte los mismos seis/semanas retornos ni se presenta como cohorte emparejada; comparte reglas, horizonte, cuenta y disponibilidad exigida. Se contarán slots, ceros, inválidos, eventos, planes y fills por separado.

## Gestión, cuenta y coste
MARKET al precio conocido, stop inicial 2 ATR14 SIMPLE actual calculado por el padre; sin TP, BE ni trailing. HOLD_HOURS=24, TP_R=None. Update heredado revisa edad en cada frontera 4h; entrada normal alineada vence exactamente 24 horas después. Stop operativo M1 durante todo el tiempo y cierre terminal R11. Horarios de entrada no vetan salidas.
Cuenta alternativa BTC-USDT Binance Perpetual Futures, denominador wallet total 10.000 USD, cuota 1% y resto ocioso. legacy_plan recibe .5 wallet y .5 margen libre, riesgo interno .02; conserva reserva .001 sólo sizing, lote .001, buffer margen 90%, 3x aislado y límite global6%. No redistribución, suma de curvas ni cartera; BTC total futuro2% eventual, no2% en cada alternativa.
Fee .00045 por lado taker con descuento, funding histórico ON snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; slip modelado0. Ruta1m/data4h, warmup2404h, fastOFF/logsON. Histórico UTC[2020-10-15,2026-01-01), sin nueva economía2026, datos/imports, estrés, grid, USDC, live o configglobal.

## Decisión y presupuesto
Máximo dos motores, uno por política, sólo root tras freeze/check/manifiesto y autorización de slot. Ningún motor o job autorizado por este documento. Preferencia WEEKEND sólo si CAGR mayor, DD M1+fills no mayor y número de meses calendario positivos no menor que WEEKDAY. Informar las demás diferencias; ninguna preferencia prueba causalidad ni promoción.
Cada cuenta exige r9 intacto: CAGR>=30%, PFnetUSD>=1.2, DD<=25%(objetivo20%), meses completos activos positivos>=65%, trimestres completos positivos>=80%, mediana mensual calendario>0 incluidos meses ociosos, neto quitando dos mejores meses>0 y N>=100 operativo sin potencia estadística implícita. Calendario completo 62 meses/20 trimestres y mes parcial2020 por separado, denominador capital total. No trocar regularidad por sólo meses activos.
Si no cumple, cerrar ambas recetas sin probar vecinos de días, horas, 48h, signo, umbral, targets o gestión. La evidencia es desarrollo histórico observado, no OOS. Se preservan todos resultados/cierres previos.

## Check previo
Supplied-source AST y stubs, arrays fabricados; sin imports del proyecto, velas observadas o motor. Oráculos: lunes/jueves UTC en borde de domingo, ancla exacta [-13] y 48h, signos y reflexión, igualdad cash, slot consumido incluso inválido/ocupado/sizing/sameexit, fuera de slot sin evento, sin uso de volumen, supresión duplicados; padre intacto, cuota y gestión24h/sinTP/ledger FINAL heredados. Guardar código/readback antes de un job que root autorizará aparte. Validar broker nativo y funding después de motores, no fingirlos con stubs.

## Precisión de bordes anterior a fuentes
La ventana tiene 1.904 días, exactamente272 semanas; START es jueves00UTC y FINISH también. Se exige START<T<FINISH ANTES de consumir/calcular retorno: no entrada ni evento en los bordes. Sin fallos de datos, hay272 slots lunes y271 slots jueves elegibles; no se borran eventos para igualar denominadores ni se llaman independientes esas semanas. Se registran actual_close_time=T y prior_close_time=T−48h. Requiere13 cierres para12 intervalos cerrados; los64 del padre contienen ambos. Logretorno=log(Cactual)−log(Cprevio) evita cociente/overflow; la señal usa signo del desplazamiento de precios. Los logs entre brazos no son idénticos porque los relojes son distintos.
