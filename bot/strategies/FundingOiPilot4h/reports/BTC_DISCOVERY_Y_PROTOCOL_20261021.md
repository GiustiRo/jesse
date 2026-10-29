# BTC Discovery Y — protocolo documental de asociación temporal volumen/amplitud

Fecha: 2026-10-21. Estado: fuentes R25 implementadas y FULLcheck sintético PASSED tras revisión y autorización root/independiente. Todavía NO drafts/economía. Protocolo y precisiones T<=last/terminal/asof/constantes fueron guardados/releídos antes de cada fuente correspondiente. Revisión final de recibos antes de motores. Nombres reservados propuestos: BtcResearchR25VolumeLagBase1m, BtcResearchR25VolumeLagState1m, BtcResearchR25VolumeLagSymmetric1m. R24/X queda reservado al HOLD del proxy; no se renombra o sobrescribe.

Y se diseñó y documentó sin consultar resultados económicos de W. Se leyó Hub r22 y se reconocen sus campos stale de roadmap/blockers; no se deducen tareas pendientes de esos campos. Root conserva la publicación del Hub. Este documento no crea un permiso económico.

## 1. Hipótesis económica y falsación

Pregunta: ¿la orientación temporal de la asociación entre volumen BTC y magnitud de retorno modifica la continuación/reversión de la dirección actual y mejora un pronóstico de retorno BTC24h, frente a conservar la dirección actual y la asociación simétrica?

Hipótesis exploratoria: participación que antecede al reajuste de amplitud podría acompañar persistencia; actividad que aparece después del reajuste podría reflejar respuesta tardía y menor persistencia. No se observan atención, agentes, órdenes agresoras, información privada o liquidaciones. D no mide impacto causal ni identifica el origen de un episodio económico.

Debilidad principal: ambas variables son no direccionales y suelen describir o anticipar volatilidad antes que media de retorno. Sólo habría una justificación de señal si su relación temporal cambia la persistencia de la dirección actual. Otra transformación distinta no basta para autorizar una corrida. La relación propuesta puede ser nula, inestable o confundida por autocorrelación, tendencia intraventana, fase UTC, heterocedasticidad o ruido finito.

Falsación de la receta: si STATE no cumple gates r9, rechazar aunque haya una celda o año atractivo; no seleccionar subgrupos. Una utilidad incremental requiere además mayor retorno de libro que SYMMETRIC bajo ventana/capital/costos comunes, sin vender ese delta como significancia o causalidad. Que SYMMETRIC falle no vuelve bueno STATE. Si reproducen economía, registrar equivalencia y no contar evidencia independiente.

Diagnóstico narrativo predeclarado: persistencia s*y mayor con D positivo que negativo dentro de comparaciones de s/q con soporte sería compatible con la explicación anticipatoria. Si es opuesta, ausente o sin soporte, no sostener esa explicación ni cambiar su signo para encajar el resultado. El diagnóstico no orienta órdenes, no selecciona celdas, no modifica forecast/admisión y no constituye un nuevo motor o gate de p-values.

## 2. Contrato fijo y datos permitidos

Sólo BTC-USDT, Binance Perpetual Futures; trading route1m y data routeBTC4h. No ETH/SPY/PAXG u otros inputs. Datos existentes: sin inspección de velas, get_existing_candles, precheck de cobertura, importaciones, descargas o datasets nuevos. El motor informaría faltantes si se autorizara posteriormente. No scripts ni framework/global config.

UTC [2020-10-15,2026-01-01), capital10000USDT;2% objetivo por trade,6% agregado,3x aislado, una posición sin pirámides. Fee0,00045 por lado,taker con descuento para todos tipos. Funding BTC histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado con marcas proxy declaradas; slippage aplicado0. Neto tras fees/funding modelados, no todos costos reales.

Warmup4004h, fijado por lookback392 y ocho filas de margen; no por frecuencias observadas. No replay1000 ni preload de un banco de eventos. Cash inicial se conserva. START<decisión<FINISH para entradas; no consultar2026 para completar labels.

## 3. Característica causal de CADA origen

Cierre4h del origen i. Usar26cierres C_(i−25)..C_i y25volúmenes V_(i−24)..V_i. Por j=i−24..i:
r_j=log(C_j)−log(C_(j−1)).
a_j=abs(r_j).
v_j=log(V_j).

Exigir volúmenes finitos y estrictamente positivos en esas25barras; sin log1p, pseudocuentas, epsilon, winsorizar o imputar. OHLC finitos/positivos/consistentes y timestamps4h exactos. Las25observaciones forman cada serie emparejada. Calcular media25(a), media25(v), std25(a,ddof=0), std25(v,ddof=0). Desviaciones finitas>0 y toda aritmética finita. Rechazar además si las25magnitudes o25logV son exactamente iguales entre sí: np.all(serie==serie[:, :1],axis=1). Es integridad de varianza matemáticamente nula, sin epsilon/cutoff; evita que el redondeo de la media fabrique std>0 para una constante.

A_j=(a_j−media25(a))/std25(a).
Z_j=(v_j−media25(v))/std25(v).
F_i=mean24(Z_j*A_(j+1)).
R_i=mean24(A_j*Z_(j+1)).
S_i=F_i+R_i.
D_i=F_i−R_i.

Ambas direcciones usan los mismos centros y escalas de25, NO centros diferentes sobre cada par de24. Cada origen de entrenamiento recalcula su característica exclusivamente con SU PROPIA ventana26/25 terminada en i. Prohibido normalizar con todo el banco, con el origen actual o con información posterior a i. La característica actual usa su propia ventana; su normalización puede incluir su barra actual porque ya cerró.

Convención de diseño previamente fija:24observaciones anteriores equivalen a cuatro días de barras4h y se agrega la actual para obtener24pares de un lag4h. Las26filas de cierres abarcan100horas de precio; no se afirma que cuatro días sean un ciclo económico demostrado. No buscar otros lags/ventanas.

Estados: s_i=sign(r_i), q_i=sign(S_i), d_i=sign(D_i). Cero EXACTO de r/S/D, desviación<=0/no finita o aritmética no finita => característica inválida. Sin tercer estado, redondeo de signos, umbral a abs(S/D), banda de ruido ni fallback. La fragilidad flotante de signos cercanos a cero se declara, sin elegir tolerancia económica después.

Inversión temporal: invertir conjuntamente el orden de las25PAREJAS(a,v) conserva sus marginales/centros/escalas y asociación contemporánea; intercambia F y R, mantiene S e invierte D salvo error flotante. No es afirmación sobre ventanas rolling sucesivas con extremos distintos, sobre invertir sólo una variable o sobre invertir OHLC crudos. El diagnóstico algebraico no prueba información direccional.

## 4. Ventana de aprendizaje y validez común

Cada T4h usar392OHLCV cerradas consecutivas, current index391, última apertura=T−4h. Row0 es padding DELIBERADO SIN USAR en features/labels seleccionados:391filas bastarían si se reindexara, pero se conserva392 ya fijado. La integridad OHLC/timestamp de row0 SÍ se valida por closed_window392; una row0 inválida no conserva admisión. No mover entrenamiento para aprovechar esa fila.

Orígenes exactos i=26..385 inclusive,360slots con edades6..365barras respecto al current391. Para cada i, feature propia en cierres i−25..i (primer origen usa filas1..26) y25volúmenes i−24..i. Label:
y_i=log(C_(i+6))−log(C_i).
Targets32..391, todos conocidos a T. No entrenar con label del current391 ni adelantar madurez. El label describe precio bruto, no payoff con SL/costos/funding; no importar targetS.

Se conserva360 de antecedentes M/R/S para no escoger historia por frecuencia de ocho celdas:60días de orígenes4h, no60días independientes. Conservar exactamente360slots; excluir sólo orígenes con feature inválida o y no finito, sin buscar olderfill ni completar360válidos. Misma máscara válida para STATE y SYMMETRIC, incluyendo s/q/dtodosnozero aunque SYMMETRIC ignore d.

STATE: media simple de y_i con (s_i,q_i,d_i)==estadoactual.
SYMMETRIC: media simple de y_i con (s_i,q_i)==(s_actual,q_actual), usando TODOS los orígenes de esa misma máscara común, no reincorporar D0/invalid para el control.

Exigir n_celdaactual(s,q,d)>=20 en AMBAS políticas y ambas medias finitas; si falla, ambas cash. No exigir20en las otras siete celdas o completar casos viejos. El control conserva sólo sign(S), no su magnitud, las escalas originales ni todo régimen: no afirmar que es un control perfecto de la asociación simétrica. Ocho celdas y mínimo20 no acreditan potencia ni confianza.

Sin shrinkage, standard errors, SEgates, OLS, kNN, prior, weighting o selección de modelo. Reutilizar una tabla de celdas no es innovación ni motivo suficiente para más intentos. La pregunta versa sólo sobre la interacción económica propuesta.

Forecast>0,0019 LONG; forecast<−0,0019 SHORT; igualdades y banda central cash. Hurdle heredado es regla de señal, no costo extra debitado. No multiplicar la media raw y por s al generar órdenes: ya pronostica retorno BTC. s*y se usa sólo para diagnóstico narrativo. Cada4h es una oportunidad nueva, sin transición de estado adicional.

## 5. Reloj y diagnóstico narrativo separado

Procesar cada nueva frontera4h una sola vez. Para matemática/diagnóstico, T<=last es no-op antes de procesar datos: no retroceder reloj ni crear, madurar o censurar otra vez. El observer R11 conserva su llamada heredada por callback, sin modificarlo por esta deduplicación. T>last+BAR sí censura pendientes afectados por el salto; no se reordena ni rellena historia. Observación/feature/modelo avanzan aunque abierto, con pendingentry o sameexit. Señal ocupada se descarta sin cola, replay, pirámides o reversión; no entry en mismo timestamp de salida real.

El entrenamiento es stateless desde392filas en cadaT: no es un replay1000, banco online de eventos ni walk-forward posthoc. El siguiente registro diagnóstico sí es incremental y no cambia la estrategia:

1. Primero, en cadaT4h, validar el OHLC actual cerrado/asof y procesar pendientes anteriores ANTES de early-returns por feature, volumen, ATR o TRAIN392. Cada pendiente conserva T_origen,C_origen,s/q/d,deadline=T_origen+6BAR,últimoT y número de siguientes barras observadas.
2. Exigir exactamente seis cierres futuros4h consecutivos con OHLC íntegro/asof. Gap, timestamp desalineado o OHLC inválido censura los pendientes afectados; no esperar sólo el precio final, rellenar, madurar tarde o reetiquetar. La invalidez de volumen, de otra feature, std o ATR NO invalida un label cuyo camino de OHLC sea íntegro.
3. Al sexto cierre, agregar una vez y=log(C_T)−log(C_origen) y s*y en bounded counts/sum_y/sum_sy por(s,q,d). El origen sale de pending. No recorrer repetidamente los360orígenes de TRAIN para sumar estas estadísticas. Identidad única por T_origen/deadline mediante reloj monotónico, sin un seen-set infinito.
4. Después de madurar, si la característica de origen ACTUAL es válida en sus26filas y START<T<FINISH, registrar una sola pendiente actual ANTES de insuficiencia TRAIN/celda20/hurdle/ocupación/órdenes. Puede existir origen diagnóstico cuando la ventana TRAIN392 antigua es inválida pero su propia feature26 es válida; declarar esa diferencia de universo en el reporte. No condicionar a fills ni cobertura de las ocho celdas.
5. Hasta seis pendientes simultáneas después de madurar/agregar, ocho acumuladores de celda y contadores de validez/censura; sin guardar toda la historia de mercado. Universo diagnóstico runtime, sin bootstrap retrospectivo de warmup ni eventos anteriores a START. Terminal: pendientes sin seis barras válidas observadas hasta FINISH quedan censuradas; no engineextra, consultas2026 o callback inventado para completarlas. Separar censura de terminal frente a gap/OHLC. Censura terminal idempotente: PRETERMINAL/FINAL repetidos contabilizan cada pendiente una sola vez y dejan la cola vacía o marcada, sin madurar artificialmente a FINISH con un precio final no observado en callback4h.

El diagnóstico resulta igual en ambas políticas si reciben los mismos datos: nunca depende de wallet, posiciones o selección de señal. No es un tercer brazo económico ni un nuevo análisis de mercado autorizado ahora. Las medias agregadas por celdas y sus contrastes son descriptivas: observaciones temporalmente dependientes y seleccionadas en desarrollo, no ensayos independientes. Reportar soporte, no esconder celdas vacías ni fabricar diferencia cuando falte una direcciónD. No orientar estrategia con estas sumas.

## 6. Gestión heredada sin cambios

R10 entry_plan: capitalmax(0,balance)flat,available_margin,3x,fee-aware2%,margen90%,floor8decimales research; riesgo6% agregado no vinculante con una posición. Fee de entrada y stop incluidas en budget; sin reserva legacy0,001/lot0,001 de P/U.

MARKET al precio BTC actual en T4h, corroborado con cierre4h fresco. SL2ATR14SIMPLE BTC actual, media14TR de15OHLC; plan congela distance y fill real hereda stop relativo a entry_price. R12ArBase on_open_position intacto: assertion risk_budget con fees, sin TP, entrycount real y observeropen. Override heredado update_position: primerT4h con T−opened_at>=6BAR liquida; no cambiar por origen del forecast, nuevo estado, horario o volumen. Broker/proteccionesM1 siempre activos. No heredar accidentalmente TP2R/48h del R11.

ATR actual0/None impide plan, pero no madurar label diagnóstico, agregar origen featureválido o calcular TRAIN. Feature/data invalid no extiende posiciones/deadlines reales. Observer R11 completo, PRETERMINAL/FINAL tras comisión terminal; DDwallet+PnLabierto M1/fills, no todos extremos intraminuto. Fronteras mensuales por fase postfunding/predecisión. Labels y pronóstico bruto no representan funding/fees; ledger real sí.

## 7. Telemetría, controles futuros y gates

Resumen acotado por4h/FINAL: ventanasTRAIN válidas/invalid, features actuales válidas/invalid y razones, slots360/validorigins, n_celda/n_control, insuficiencia20, medias/score en fill real, signal/occupied/sameexit/entrycount real; diagnóstico registered/matured/censored_gap/censored_terminal/pending y count/sum_y/sum_sy de ocho celdas. No millones de logsM1 ni usar plan como fill. Contadores descriptivos no son evidencia de potencia.

Checks futuros, si root autoriza implementación más tarde: supplied-source AST/stubs sin importar estrategias reales/framework ni precios observados; oráculo S/D por inversión conjunta con centros25; normalización pororigen,392/row0unused/360slots/targets<=391/no label actual; vol0/log/σ0/rSD0/NaN/sharedmask/n20/controlSgrosero; reflexión de dirección s y rawlabel, hurdle exacto; pending único/madurez6/gapcensura/volumeinvalid-ATRinvalid-TRAINinvalid no impiden camino válido; sin contar train repetido o influir órdenes; gestión/sizing/fill/FINAL. Sin contador de assertions como validación económica.

Gates r9 CADA cuenta: CAGRnetobase>=30%,PF>=1,2,DD<=25%(objetivo20),M65mesesactivoscompletos positivos,Q80trimestrescompletos,mediana mensual calendario>0 incl inactivos,neto sin mejores2meses>0,N>=100 sólo operativo preliminar. Aspiraciones preservadas40–50%+/M70. No relajar al superar control. Auditoría fullsnapshot gross−fees+funding=PNLsum=equityfinal−10000, funding aplicado, M1/calendario/terminalfee conciliados; rolling12m y labels solapados no OOS ni independientes.

## 8. Deduplicación y cierre de presupuesto

Se leyó la propuesta Y y fuentes/cierres completos más cercanos, preservados en BTC_DISCOVERY_Y_CODES_AND_ANTECEDENTS_20261021.md:
- X804/BTCExploreR804: cambio de sumas contemporáneas V*ΔC en dos mitades, no contraste V_j*abs(r_(j+1)) frente a abs(r_j)*V_(j+1).
- N204/K1001/R1/R4/R5/R6/R8/P: cohortesVWAP, localización del cierre, eficiencia, ocupación y convivencia. No se rescata esa operativa ni se suma su runner.
- C/I: volumen sin avance/escape y secuencia low-volume impulso/high-volume reparación. Antecedente económico cercano, no novedad universal; no mover umbrales para relajar sus cierres.
- AngleVolume/Acceptance: nivel de volumen por fase u ocupaciónM1 ya explorados. No repetición ni otro umbral.
- D/X805/U: reloj de volumen y frontera de cohortes; no F−R. U cerrado, sin quitar ramas u otros clocks.
- V4shock/V5VWAP: shock simultáneo, media/dispersion ponderada; no orientación de asociaciones cruzadas.
- F/H/M/O/R/S/T/V/W: partición de saltos, geometría, orden de extremos, vecinoskNN/targetfee-only, faseUTC, VARretornosBTC/ETH y pasajes. Y no cambia ninguno de sus parámetros/modelos/labels/clocks. W sólo protocolo leído para dedup, sin resultados económicos usados para diseño.
- Tabla de medias/gate20 también aparecen en antecedentes: no es una familia de aprendizaje nueva.

Lectura dirigida y listado de estrategias sin truncar; no equivalencia concreta hallada, tampoco ausencia universal acreditada. No hay obligación de implementar por haber encontrado un observable distinto. Revisiones root/independiente pueden retirar Y documentalmente sin simulaciones.

Presupuesto PROPUESTO para aprobación posterior: exactamente dos economías STATE/SYMMETRIC, hasta dos reemplazos exclusivamente técnicos, nunca por PnL. Antes: fuentes nuevas/autorización, readback/hash/checks/revisión y manifiesto con campos reales. Máximo global2backtests y1análisis técnico simultáneos, coordinados con root; ningún slot usado por este documento. No motores/drafts autorizados ahora.

Tras dos resultados, cerrar sin vecinos25/360/20,lag,transformación/log,bandas,ceros/signos,S/D,magnitudes,labels/horizonte/costos/modelo/shrink,lados,fasesUTC/gestión/riesgo. No rescatar la hipótesis cambiando target a volatilidad si falló media. Conservar insuficiencia y fallo económico como hechos distintos, sin seleccionar celdas ganadoras.

X HOLD permanece en BTC_DISCOVERY_X_PROPOSAL_HOLD_20261021.md. Y propuesta previa permanece en BTC_DISCOVERY_Y_PROPOSAL_20261021.md como historial; este protocolo normativo posterior precisa row0unused, máscara, diagnóstico y causalidad. Fuentes nuevas R25 guardadas/readback exacto y2jobs técnicos succeeded (1probe y1fullcheck),0jobsfallidos. Cero drafts/economía o velas inspeccionadas; sin imports/datos nuevos/research_scripts/install/restart/global/framework/live/paper/Pi/nuevos2026.

## Precisión técnica antes del check final
Revisión root/independiente detectó paridad de precio sólo validada después de TRAIN392: corregida ANTES de madurar/capturar diagnóstico. Mismatch entre current4h y self.price (rel1e−10,abs1e−8 heredadas) es asof inválido: censura pending como integridad, no captura origen y bloquea nuevas entradas sin afectar protecciones.

Probe sintético bdc2d3c5c0294a7cbc97ca925e8c4894, NumPy1.26.4, encontró con V=2 constante exacta std(logV)=1.1102230246251565e−16 y feature espuria válida; por eso root aprobó guard de igualdad EXACTA en25logV y25magnitudes antes de fuente final. No se añadió tolerancia económica ni se eliminan signos pequeños no constantes. Versiones33d07… y8113… se preservan con motivo, código exacto de probe y artefacto, sin economía.

## Estado técnico completado, sin economía
FULLcheck7a53cb54457e4d478247cfae6dd4155b PASSED13grupos materiales al primer intento, NumPy1.26.4. Probe previo bdc2d3c5c0294a7cbc97ca925e8c4894 SUCCEEDED, evidencia degeneracyV2constante. Dosjobs técnicos totales,0jobsfallidos/0erroresharness, dos defectosfuente corregidos antesFULLcheck. Fuente final base437833f8ab078a24843b0ce326a4cd556bae8cdcb755be420febe648165251b7; wrappers State01c7aba73af2f10b5af06f46be016e0e90b34e9cb15aad494f97f64cb103b041 y Symmetric2913fee1da3cd5e219fcee4c6691d802716bdace2bccf07011c41537394261d1. PadresR10/R11/R12AR releídos intactos tras check.

Recibos permanentes: BTC_DISCOVERY_Y_TECHNICAL_RECEIPT_20261021.json (JSONestricto, códigos/jobs/artifacts exactos, RawNaNprobe como STRING, tresversionesfuente y motivos), BTC_DISCOVERY_Y_IMPLEMENTED_CODES_20261021.md (CODES final ysupersedidos), BTC_DISCOVERY_Y_TECHNICAL_PREPARATION_20261021.md. Antecedentes completos permanecen separados yreadback paginado exacto313513caracteres. Ningún resultado económico inferido de sintéticos; cobertura/funding/broker deben verificarse si root autoriza motores después de revisar recibos.
