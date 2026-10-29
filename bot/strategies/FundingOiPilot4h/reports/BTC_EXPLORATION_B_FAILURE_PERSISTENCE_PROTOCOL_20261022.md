# Línea B — persistencia de un fallo de ruptura por cierres

Fecha local: 2026-10-22. Estado: PROPUESTA para revisión de root, antes de implementación. Cero estrategias nuevas, drafts, jobs, motores o precios observados. Autorización de esta ronda: exploración documental con especialistas; no autorización económica automática. CODES flat acompaña las fuentes congeladas.

## Pregunta y motivación económica

Tras un cierre fuera de un rango previo y un regreso inmediato al interior, ¿exigir que el siguiente cierre todavía permanezca dentro mejora la política de reversión frente a revertir todos esos fallos en el mismo momento tardío?

Una ruptura puede atraer entradas de continuación y después regresar al rango. Si el precio vuelve pronto fuera por el lado original, la interpretación de rechazo ha quedado debilitada ANTES de entrar; si permanece dentro una barra adicional, el fallo ha persistido bajo una definición observable. Es una hipótesis predictiva de selección, no flujo observado, identificación de traders atrapados ni causalidad económica demostrada. Un cierre interior no prueba aceptación de una subasta en sentido microestructural. También puede llegar tarde y perder las mejores reversiones o seleccionar retrocesos sin continuación: esa es la explicación rival.

No se construye un STATE que compre recuperaciones. Ambos casos sólo revierten; recuperación se usa para abstenerse en el tratamiento. No se modifica ninguna posición en función de otra señal después de entrar. No deriva del suplemento K, no usa volumen, funding como señal, RSI, EMA, ADX, VWAP ni etiqueta futura TP/STOP.

## Antecedentes y diferencia material limitada

V1 H2 YA investigó reversión de ruptura: c_prev fuera del H/L del díaUTC anterior y c actual dentro, con fronteras dependientes del día, límite diario, stop2%/TP4%/24h, riesgo2%, cuatro variantes de gates funding/OI. V1 terminó sin candidata. No se presenta esta idea como una familia inédita.

OrchLateralFailedRange4h investigó barrido intrabar de rango20 y close dentro, gate eficiencia<=.25 y target al medio, bajo cuenta multiasset con otro riesgo y sin funding. Su cierre fue negativo. Aquí se exige cierre exterior real y dos cierres posteriores, sin eficiencia, targetmedio o gestor distinto entre brazos.

AngleCombinedBtcAcceptance4h añadió120/240 cierresM1 en tercio inferior a shorts originales, descartado. AngleCombinedBtcReclaim1m esperó touch y un cierreM1 posterior de recuperación para el long K original, descartado. Esta propuesta no cambia sus umbrales/latencia: clasifica tres cierres4h frente al MISMO rango congelado antes de la ruptura, y opera reversión simétrica.

R8 X801–X805 sustituyeron referencias de coste/cohorte/compresión/cuerpo/volumen; Y901 LIMIT y Y902 STOP conservaron evento N503 por presiónOHLCV/cohortVWAP/eficiencia. R8 no aprobó todos los gates; Y902 continuó por R9/K y no queda pendiente virgen. No se rescata esa ejecución, su helper de setup ni sus vecinos.

V3 RANGE vendió el cruce exterior z20 en bajo drift, no su regreso y permanencia; CHANNEL opera continuidad del breakout con SMA120, y PULLBACK touchSMA20/reanudación con régimen, sin esta secuencia. V4 shocks revierte desplazamiento>=2ATR y volumen>=2media1h; oscilador RSI2 y funding reset tampoco son la pregunta. V5 VWAP entra al volver a bandas cambiantes de media ponderada24h, sin rango congelado o permanencia extra; CROSS es SMA20/80. V6 eficiencia cruza un ratio de trayectoria, NR7 expande una vela estrecha y deleveraging añade datosOI. Sus cierres se conservan negativos/sin candidata; CROSS_P sin confirmación por ranking no se declara fallida en una fase que no se ejecutó.

O REPAIR usa orden de extremos de seis barras dentro del día; cierre sin candidata y sin vecinos. B no cambia su orden, resolución, dirección o umbrales: pregunta sobre fallo exterior de un nivel conocido y permanencia posterior, sin extremos intradiarios. La nueva observación no consiste en inventar un indicador o cambiar sólo el nombre.

Decisión previa: comparación nueva y pequeña justificada por el filtro temporal de permanencia, con control al mismo momento. No hay sesión archivada acreditada con ESTA receta y contrato exactamente equivalentes entre las fuentes revisadas. No se afirma búsqueda global exhaustiva ni novedad universal. La historia es ampliamente reutilizada/adaptativa; no OOS.

## Regla exacta de precio

BAR=14.400.000ms. En cada T múltiploUTC de4h, BtcResearchR32SpecialistBase1m valida exactamente64 OHLC cerrados consecutivos con último open=T−BAR, mediante closed_window de R10. La hoja toma rows[-29:] para el cálculo descrito abajo. Las64 filas, incluidas las35 anteriores fuera de la fórmula, deben ser finitas/coherentes y positivas en OHLC; no se afirma invariancia de admisión frente a corromperlas. No usar volumen; no exigirlo positivo ni imputarlo. Cerrar29 excluye velas futuras/en formación; requerir close final igual a self.price con tolerancias numéricas heredadas rel1e−10/abs1e−8, no bandas de decisión.

Índices cero: contexto w[0:26]; ruptura b=w[26]; fallo f=w[27]; resolución r=w[28]. Equivalente slices sobre rows64: contexto rows[-29:-3], b=rows[-3], f=rows[-2], r=rows[-1].
L=min(low contexto), H=max(high contexto). Requerir L<H. Fronteras congeladas antes de b: ni b, f o r las redefinen. No elegir otro lookback según resultado.26 es el canal ya usado por la infraestructura histórica; no duración económica estimada. No escoger horaUTC o fase favorable.

s=+1 si close_b>H; s=−1 si close_b<L; otro caso no patrón. Igualdad a cualquier frontera en b NO rompe.
Hay fallo sólo si L<close_f<H. Debe ser la barra inmediatamente siguiente a b; igualdad no vuelve al interior. Si f permanece fuera o retorna más tarde, esta ruptura no se opera bajo esta receta.
Al cierre inmediatamente siguiente r, el control ALL revierte con dirección−s, independientemente de dónde cierre r.
Tratamiento PERSIST sólo revierte dirección−s si L<close_r<H. Si r iguala cualquiera de las fronteras, recupera fuera del lado original o atraviesa la frontera opuesta, tratamiento cash. El control conserva esos casos: excluirlos en común sería cambiar su definición y esconder parte del filtro.
No epsilon económico ni ancho mínimo, extensión, color de vela, amplitud/volumen o distancia al centro como gates adicionales.

Partición diagnóstica EXCLUSIVA de las resoluciones de un fallo:
- interior: L<C_r<H;
- recuperación original: s=+1 y C_r>H, o s=−1 y C_r<L;
- atravesó extremo opuesto: s=+1 y C_r<L, o s=−1 y C_r>H;
- frontera: C_r=H o C_r=L.
No llamar recuperación al cruce opuesto. El tratamiento selecciona sólo interior; no permite separar categorías después y rescatar una mediante tercer motor.

## Caducidad, consumo y ausencia de cola

No se necesita una máquina armada durante días: cada tripleta b/f/r exacta se resuelve una vez en T, ocho horas después del cierre b y cuatro después del cierre f. La confirmación es una sola barra adicional, la mínima observación4h posterior; no se buscará1/2/3barras. La señal caduca en esa T: jamás se espera otra entrada, retest o recuperación posterior.

El patrón se calcula y registra antes de ocupación y sizing, para ambos brazos, también mientras existe posición o pending. Se consume aunque no se ejecute. No cola, pirámide ni reentrada en last_exit_at=T. Sólo un nuevo patrón con distinto timestamp b puede generar otra oportunidad posterior; no se rearma la misma ruptura porque el precio siga dentro. El diseño por ventanas permite patrones distintos que compartan barras, no muestras independientes ni episodios completamente disjuntos.

La hoja memoriza su último timestamp evaluado: T<=last_event no repite patrón ni logs; no retrocede reloj. before común limpia dirección en cadaM1 y evalúa _event sólo4h. rows64 inválidas o gaps invocan _invalid_event heredado sin estado de episodio; asof mismatch produce el assert técnico común. L>=H o ATR inválido => cash, sin rescatar eventos anteriores ni rellenar velas. Mismatch es bloqueo técnico visible; no ocultarlo como ausencia rentable de señales. Protecciones de posiciones existentes continúan bajo la gestión heredada.

## Entrada, gestión y cuota idénticas

Ambos casos ejecutan BTC MARKET a float(self.price) en la resolución r, sólo si START<T<FINISH, plano, sin pending y sin cierre en esa T. No entrada retrospectiva en f ni en el nivel H/L. El tipo real MARKET y created/executed/opened deben auditarse en órdenes nativas; metadata sola no basta.

ATR14 arithmeticTR=atr14(rows) de R10, actual al cierre r, positivo y finito. D=2ATR para ambos. Stop desde fill real E−direction*D; TP desde fill E+direction*2D; salida MARKET en primer cierre4h cuya edad real sea>=48h. No BE/trailing/parciales/otra salida por recuperación o señal opuesta. R11 update_position ya implementa12BAR48h y su observación M1+fills. SL/TP están activos intrabar; las reglas del broker y gaps quedan las nativas. No variar stop, TP o plazo.

Reutilizar exclusivamente legacy_plan(event,.5*max(0,balance),.5*available_margin,leverage,fee), de R16LegacyBase, como helper de sizing, NO su señal/gestión ni herencia K. event conserva origin propio FAILURE_REVERSAL, direction−s, entry=self.price, distanceD, target_distance=2D, hold_hours48 y order_kindMARKET. Exigir stop y target positivos antes de planificar, igual para ambos. Herencia común aprobada: BtcResearchR32SpecialistBase1m, a su vez R11. Las dos hojas sólo definen LABEL único, HOLD_HOURS=48, TP_R=2.0 y _event(rows64,now). La hoja devuelve None o dict(direction=-s,meta compacta). El origen real del plan es LABEL de cada política, no la cadena ilustrativa FAILURE_REVERSAL; no redefinir before, sizing, ejecución, apertura/cierre/gestión ni _emit. El helper legacy_plan se usa únicamente por el padre común, sin herencia de señales K. No crear estrategia en este documento.

Esto significa cuenta alternativa BTC inicial10000 y riesgo objetivo1% del capital TOTAL, otra mitad ociosa, sin redistribución. Helper.02*.5, reserva.001 sólo dimensionamiento, floor lote.001, techo nocional4.4del capital escalado y buffer90% sobre la mitad del margen.3x aislado;6%global. No es una subcuenta de5000 ni dos cuentas sumables ni book conjunto2% ya demostrado.

Auditar qty y pérdida planificada incluyendo fees y reserva; en apertura verificar riesgo al fill real y qty antes de atribuir conformidad. R11 observer se llama exactamente una vez en cada hook heredado, equity=wallet+PnLabierto, sin portfolio_value apalancado. Nada de backtest virtual ni órdenes ficticias. El helper de sizing no agrega slippage cobrado ni limita gaps/funding a1% garantizado.

## Datos y contrato fijo

BTC-USDT, Binance Perpetual Futures; ruta1m/data4h; UTC[2020-10-15,2026-01-01) exclusivo; warmup2404h predeclarado, holgado para29 y heredado del contrato sin indicador recursivo nuevo.10000,3xaislado,fee.00045takercon descuento porlado, funding históricoON/applied dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, proxies explícitos, slippage modelado0. No importar/preinspeccionar cobertura; faltantes los expone motor. No featuresETH/OI/nuevosdatasets, 2026nuevo, USDC, cartera, estrés/riskgrids, live/paper/Pi, installs/configglobal/framework.

## Instrumentación acotada y auditoría

El padre común proporciona R11 minuto/invalid y R32 eventos seleccionados/planes/occupied/rejected_geometry/opens/closes/net/lados. Esos contadores no sustituyen patrones brutos previos al filtro.

B registra una sola línea R32_B_PATTERN por CADA patrón bruto b/f/r, antes del gate del tratamiento y antes de ocupación: policy, T, timestampsb/f/r, L/H, tres closes, s, categoría exclusiva, selected. La suma de estas líneas es el denominador de fallos observados y su partición; ambos brazos deben coincidir por identidad/categoría sin depender de trades. No log de cadaM1 ni de todos los cierres sin patrón. Contadores de no_breakout/no_return de un borrador anterior NO se prometen desde la API hoja; no inferirlos de planes o fills. Las líneas son pequeñas y la auditoría debe recuperarlas completas paginadas; no aumentar payload para evitar páginas.

Meta del evento seleccionado conserva geometría/identidad/categoría, replicada en R32_PLAN; el padre ya registra precio, D, qty/riskbudget/planned_loss y OPEN real con origen, tiempos, SL y target_distance/hold. R32_CLOSE y summary acreditan neto/ledger; trades/orders/funding nativos suministran IDs, bruto/fees/funding y causa de salida, sin exigir que CLOSE replique todo el snapshot. No añadir callbacks en hojas ni modificar el padre común. Sus hooks observan R11 exactamente una vez, actualizan ledger antes de FINAL y validan el riesgo completo con reserva al fill. _emit padre emite filas compactas; toda línea B debe ser<1900caracteres. No nuevo traceRprecio: el observador financiero R11 basta para esta pregunta.

Root congela nueva fuente+dependencias/hash/formulario/runtime y manifiesto antes de ejecutar. Reconciliar gross−fees+funding=PnL=final−10000 tolerancia1e−6, funding ausente sólo0 cuando ledger completo lo acredita, posiciones/cierres finales, ordenrealMARKET, protección y sizing, R11M1+fills/calendar/asof. PRETERMINAL yFINAL son snapshots, no sumandos; flatPRETERMINAL puede ser final económico. No fabricar métrica con registros truncados.

## Evaluación y falsación prefijadas

Puertas r9 intactas: CAGR neto>=30%, PF netoUSDT>=1.2, DD M1+fills<=25%(objetivo20%), meses completos activos positivos>=65%, trimestres completos positivos>=80%, mediana mensual calendario>0 incluyendo inactivos, neto aritmético sin dos mejores meses>0 y N>=100 mínimo operativo preliminar, no confianza/potencia. Informar cuenta total/cuota1%; no anualizar sólo meses activos ni trasladar automáticamente30% a cada pieza como promesa. También todos los meses positivos/denominadores, años2021–25 y ventanas12m descriptivas, concentración, lados, tiempo expuesto, bruto/fees/funding/neto, DD diario separado.

Contraste descriptivo de políticas completas: si tratamiento mejora por operar menos, no concluir información nueva sólo desde menor DD. Comparar retorno, PF, regularidad y riesgo conjuntamente, sin puntaje/cutoff de mejora material posterior. Si no domina, describir intercambio; no proclamar winner por una sola métrica ni quitar el control porque gane. Si tratamiento no aporta o empeora, rechaza este filtro bajo este contrato; no refuta toda reversión. Si ambos fallan gates, sin candidata aunque exista mejora relativa. Muestra escasa se declara insuficiente; no subir riesgo para obtenerCAGR.

Los trades comunes y categorías pueden describirse después, pero no son efectos causales aislados: el filtro modifica ocupación, capital y entradas posteriores. No reconstruir PnL de una cuenta eliminando trades del control ni inferir candidatos perdidos desde los fills. No separar por tipo de salida futuro como señal.

## Presupuesto y secuencia

Exactamente dos políticas futuras, ALL y PERSIST, máximo2motores económicos y0reemplazos automáticos. Un fallo técnico vuelve a root con causa; no consume un permiso abierto de reruns. No tercer motor de continuación/recuperación, ni vecinos de lookback, confirmación, igualdades, extensión, ATR, TP, plazo o cuota después delPnL. La recuperación como futura dirección es hipótesis aparte no autorizada por este presupuesto.

Concurrencia global vigente máximo2backtests+1analysis coordinado por root. Ahora sólo protocolo+CODES; después revisiónroot/independiente, luego autorización de fuentes y checks supplied-source/AST/stubs (sin frameworkimports/estrategias reales/precios), nueva revisión y recién draft/manifiesto/motores. Esta entrega no reserva ni ocupa slots. La fuente R32 común fue escrita por root antes de estas hojas y leída completa mediante MCP; no es una estrategia económica B creada por este agente. La modificación documental de infraestructura/telemetría se registra ANTES de implementación, sin cambiar patrón o filtro.

Checks materiales previstos: oráculo índices29/26/3, fronteras excluyendo b/f/r y congeladas, long/short espejo, equality, retorno inmediato/caducidad, persist/recuperación/opuesto/frontera disjuntos, prefix/futuremutation, gaps/asof, ocupación/memo/noqueue/sameexit, .5/.5/lote/reserva, SL/TP48h y hooksR11/terminal sin duplicación. No confundir mocks con ejecución nativa acreditada. No volver a pedir permiso humano rutinario para documentación dentro de autonomía concedida; root decide revisión y prioridad de motores.

## Incidentes de esta preparación

Primer inventario list_project_files solicitó max_entries4000 y fue rechazado por límite1..1000; corregido a1000, sin mutación/job. El inventario de FundingOiPilot4h/reports truncó a1000 y no se afirma censo completo. strategies raíz sí se leyó sin truncar; búsqueda dirigida de antecedentes y sus fuentes/cierres. No incidente económico, código o conectividad. CODES preserva exactos las fuentes recibidas; no se reinterpretan pendientes antiguos como no ejecutados.
