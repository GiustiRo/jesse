# Research protocol V1 — 2026-10-20
Estado: **especificación económica congelada antes de nuevas pruebas; fase0 cerrada APTO CON LÍMITES por addendum del freeze**. No es una confirmación de implementación. No consultar resultados de estas nuevas configuraciones2024–2025 hasta congelar shortlist. No abrir2026.
El freeze técnico y registry.json de esta carpeta son parte del protocolo. La recarga local/MCP y la comprobación de fills deben cerrar fase0 antes de iniciar el lote. No cambiar reglas al implementar: cualquier ambigüedad material exige registrar una versión antes de resultados.

## Universo y convenciones comunes
Sólo BTC-USDT Binance Perpetual Futures. Datos históricos y hashes exactos del freeze, nunca sustitución automática. Intervalo común [2020-09-01,2026-01-01). Velas ejecución1m; decisión4h UTC sobre vela ya cerrada. Sin ML, random chunks, pyramiding ni exposición fuera de una ruta.
Capital10000USDT inicial PLANO por sesión; isolated3x; fee nominal .00045 por lado. Funding contable ON en TODAS las ablaciones, incluso P. Slippage nominal0bps, estrés de fills5/10bps según matriz abajo. No presentar el nominal sin slippage como una estimación exhaustiva de costes reales.
Warmup240velas4h sin operar; rango UTC previo y retornos pueden usar esas velas. Funding history sólo eventos publicados. OI24h se inicializa mediante las decisiones del período de evaluación: primeras seis observaciones4h no tienen referencia24h. No backfill ficticio, ni usar un archivo anterior a septiembre2020.
Se permite una entrada efectiva por día UTC y sólo si plano/sin entrada pendiente. Gate de entrada explícito start<T<finish con T=reloj de decisión; no abrir en el borde final. Gestión protectora siempre activa. El cierre final forzado corresponde al fold, con fees y slippage de market si aplica.
Stop a2% del precio realmente ejecutado; target4%; market exit al primer cierre4h donde edad>=24h. No mover stops/TP, no parciales ni piramidar. En el modelo5m/4h cerrado la resolución temporal debe declararse; no prometer salida subminuto.
Sizing idéntico al piloto: C=available_margin antes de entrar, p=precio de decisión, d=+1long/−1short, stop_pre=p(1−d*.02), L=abs(p−stop_pre)+fee*(p+stop_pre).
notional=min(C, .02*C/L*p); qty=floor8(notional/p). No multiplicar por leverage. Funding y slippage no están dentro del presupuesto2%; reportar pérdidas reales al stop y exceso por fricción. Con slippage, stop/target basados en fill pueden cambiar riesgo y trayectoria: no restaurar retrospectivamente el sizing nominal.

## Variables causales
En T usar sólo velas con open_time+4h<=T. c=cierre de la última; c_prev=cierre de la anterior; c24=cierre de la barra terminada exactamente T−24h. Si falta una barra/referencia exigida no habilitar entrada de esa familia.
D=floorUTCday(T). H/L=máximo high/mínimo low de las seis velas4h únicas del día[D−24h,D). Si son incompletas, no señal.
Funding visible: eventos con available_at<=T, ordenados por timestamp original. r0=último, r−1=anterior.
z0=(r0−mean(30previos))/std(30previos,ddof0); actual excluido. z−1 usa los30anteriores a r−1 y lo excluye. Requerir ptp>0, std positiva finita y z finito; H1/H2 necesitan31eventos; H3 necesita32. No usar funding estimado próximo ni signo de feature importance ML.
OI0=valor causal disponible en T bajo lag6m/max_age10m; OI24=valor efectivamente observado en la decisión T−24h. Requiere valor>0 en ambos y timestamp de referencia exacto, sin rellenar huecos. Gate OI=OI0>OI24, igual para long y short. No interpreta OI como dirección.
Un gate de señal apagado no exige datos de esa señal. La contabilidad funding permanece obligatoria.

## Tres mecanismos; exactamente12especificaciones
Cada familia tiene cuatro ablaciones P,PF,POI,PFOI. PF añade sólo gate funding a P; POI añade sólo OI; PFOI ambos. Las salidas/sizing/calendario son idénticos.

| Familia | Dirección de precio P | Gate funding F |
|---|---|---|
| H1 continuación | long c>H; short c<L; en otro caso0 | bloquear long si r0>0 y z0>2; bloquear short si r0<0 y z0<−2. Datos/statística inválidos: no entrar en variantes F |
| H2 reversión de ruptura | long si c_prev<L y L<=c<=H; short si c_prev>H y L<=c<=H; otro caso0 | long sólo r0<0,z0<−2; short sólo r0>0,z0>2 |
| H3 normalización y régimen | long si c>c24 y c>c_prev; short si c<c24 y c<c_prev; otro caso0 | long si r−1<0,z−1<−2,r−1<r0<=0,abs(z0)<=2; short si r−1>0,z−1>2,0<=r0<r−1,abs(z0)<=2 |

IDs: H1_P,H1_PF,H1_POI,H1_PFOI; H2_P,H2_PF,H2_POI,H2_PFOI; H3_P,H3_PF,H3_POI,H3_PFOI.
No se agregan thresholds, transformaciones OI ni otro timeframe.30eventos,2z y OI24h son elecciones informadas por legacy/pilotos ya vistos, no estimaciones independientes. H2/H3 son hipótesis nuevas, aún sin evidencia.
No deduplicar por nombre o similitud: sólo reutilizar si código completo, lógica, warmup, boundary gate, config, datos y ventana son exactamente equivalentes. H1 no reutiliza automáticamente los pilotos: la instrumentación y gate de borde se deben comparar. Otras familias P no son iguales.
Antes de cada primer resultado capturar implementación completa e inmutable de padre/helpers/subclase, config completa, hashes, datasets, runtime y pruebas de prefijos/mutación futura. registry.json empieza SPECIFIED; no fingir hashes de código aún no escrito. El único cambio permitido sin versión es completar código que implementa literalmente estas fórmulas y su trazabilidad, antes de probarlo.

## Instrumentación obligatoria antes del lote
Persistir por mes, dirección y total: barras, oportunidades precio estando plano/con cupo diario, funding ausente, funding varianza nula/no finita, funding gate económico, OI ausente, OI stale, cero actual, inicialización, referencia inválida, gate OI no creciente, entradas y salidas; anotar denominadores. Mantener flags de causas simultáneas y una partición exclusiva de rechazo con prioridad documentada (precio→funding calidad→funding económico→OI actual→inicialización→referencia→OI económico). No sumar causas simultáneas como si fueran trades distintos.
Entradas: guardar timestamp, margen antes de orden, qty, precio de decisión/fill, stop/TP, funding/OI y sus observed/available timestamps. Fuente de cada feature, unidad y parámetros. Logs <=2000caracteres por línea, debug_mode=true. Validar conservación de conteos en un smoke técnico antes del primer lote.
Nuevas H2/H3 y sensibilidades deben pasar prefijos/mutación futura, rolling statistics y alineación4h/UTC. Las pruebas de fase0 cubren sólo funciones allí identificadas.

## Walk-forward y selección
Train empieza siempre2020-09-01 y termina al inicio de la evaluación; fin exclusivo. Cada sesión independiente,10000,plana.
Exploración E1eval2022-01-01→2022-07-01; E2eval2022-07-01→2023-01-01; E3eval2023-01-01→2023-07-01; E4eval2023-07-01→2024-01-01.
Máximo12×4×2=96sesiones económicas nominales. Un backtest activo; subir a2sólo tras respuesta estable, nunca arrancar ciegamente otra sesión ante timeout.
En cada corte ejecutar/consultar train primero. Elegible:>=30trades,neto>0,PF>=1.2,absDD<=25%. Orden: menor absDD,mayorPF,menor turnover (suma notional de fills ejecutados /10000),menor complejidad (P,PF,POI,PFOI),ID lexicográfico.
Registrar selección antes de ejecutar o consultar evaluación siguiente. Si ninguna cumple: SIN_CANDIDATA; selector plano, retorno0 durante ese semestre. Las demás ablaciones siguen siendo research diagnóstico.
Después de E1–E4 elegir como máximo2finalistas entre configuraciones seleccionadas al menos una vez y con suma de netos de sus cuatro evaluaciones>0, al menos2semestres positivos y>=30trades únicos de evaluación. Si ninguna cumple, cerrar SIN_CANDIDATA, sin fase3. Orden de shortlist: menor peor absDD entre cuatro evaluaciones,luego mayorPF agregado de trades únicos,luego menor turnover,luego simplicidad/ID. Esta selección usa desarrollo visto y se declara como tal.
Guardar FROZEN_SHORTLIST_V1.md y registry completo ANTES de abrir métricas2024–2025 de nuevas configuraciones.

Confirmación C1eval2024-01-01→2024-07-01; C2eval2024-07-01→2025-01-01; C3eval2025-01-01→2025-07-01; C4eval2025-07-01→2026-01-01.
Máximo2×4×2=16nominales. Elegir en cada train entre shortlist con el MISMO selector; pasado evaluado puede entrar en train siguiente. Sin intervención posterior ni cambio de umbrales.
No sumar resultados de train ni trades repetidos. No presentar la ganadora posterior de cada eval como seleccionada antes.2022–2023es exploración ya vista;2024–2025reserva interna del ciclo, no independencia absoluta frente al historial del usuario.

## Índice y reportes
Guardar retornos/DD por fold,meses completos,dirección,exposición,turnover,duraciones,rachas,bloqueos,precio bruto,fees,funding y saldo.
Índice del selector: iniciar10000, escalar cada curva de evaluación seleccionada por índice al comienzo/10000; si SIN_CANDIDATA, índice plano. Incluye cierres/costes de borde y supone reinversión proporcional al comienzo del siguiente semestre. No es replay continuo: cada sesión dimensionó con10000. No sumar balances ni USDTfees como si fueran una cuenta real.
Declarar resolución disponible del índice (curvas almacenadas normalmente diarias), no llamar a su DD un máximo intraminuto. Informar también DD de motor por fold. PF agregado de trades únicos seleccionados: convención nominal de sesiones reseteadas, separar de índice reescalado. Si no hay curvas o trades suficientes, inconcluso, sin fabricar valores.
Describir meses negativos,mediana,peor mes,rachas y concentración por mejor trade/semestre. Retirar mejor semestre y reportar si cambia el signo. Meta20–30%anual sólo con convención válida y tiempo completo; sin cuota mensual.

## Robustez preregistrada: hasta48sesiones
Valores de slippage5/10bps por lado son escenarios deterministas de estrés, no una medición calibrada de fills Binance. No buscar el mínimo coste que salva candidata. Se requiere la integración real de fills descrita en freeze; un haircut posterior no sustituye estas pruebas.
Para cada uno de hasta2finalistas y cada uno de4folds confirmación:
S1 fee.0009,slip0;
S2 fee.00045,slip5;
S3 fee.0009,slip10;
S4 fee.00045,slip0,OI entregado con UN cierre4h adicional de retraso.
Total32. S4 conserva la observación causal obtenida en T−4h y la entrega en T; la frescura se evalúa en el reloj original T−4h y no se prolonga el stale original ni se consulta el futuro. OI24h usa las observaciones igualmente retrasadas. Primeras siete decisiones4h sin referencia suficiente; registrar la inicialización adicional. Si no usa OI es prueba equivalente y se reutiliza, no otro intento económico.
Vecindad: cada finalista, sólo C1 y C4 (fechas fijadas ahora),stop/target1.8%/3.6% y2.2%/4.4%,hold24h y gates intactos:8sesiones.
Máscara común diagnóstico: para cada finalista/fold, ejecutar su contraparte de precio P con la MISMA máscara de calidad/disponibilidad de las features exigidas por el finalista, pero sin sus gates económicos:8sesiones. Comparar contra finalista original, que ya exige esa máscara. Si finalista es P, equivalente sin ejecución adicional. Sin seleccionar la contraparte ni trasladarla a shortlist.
Máximo48; los slots reutilizados NO se convierten en nuevos parámetros libres.

Sensibilidad proxy de marcas funding: run_analysis sobre snapshots para cashflows×0.5 y×1.5, ambos sentidos, con y sin mejor semestre. Es una aproximación contable SIN recálculo de fills/sizing/compounding; no denominarla replay. No atribuir exactitud histórica a una marca proxy.
Ceros/huecos: exclusión operativa siempre; tabla de máscara común y S4 miden sensibilidad, nunca borrar meses afectados.
Bootstrap complementario opcional sólo de retornos mensuales del selector, bloques contiguos3meses,2000muestras,seed42, preservando meses planos; descriptivo, sin elegir reglas, sin sustituir gates ni afirmar significancia estadística. No usar candle MC que desalinearía señales funding/OI salvo diseño específico nuevo.
No hay simulación de latencia ni garantía de ejecución real; queda explícitamente fuera de este soporte. S2/S3miden fills adversos, S1fees.

## Gates de confirmación, sin relajarlos
Neto del índice selector>0;PF de trades únicos seleccionados>=1.2;DD del índice muestreado<=25%;>=100trades seleccionados;mayoría de cuatro semestres positivos (>=3).
Neto agregado positivo bajo S1 y S3, reportando bajo estrés todos los demás límites y tamaño de muestra. Si faltan curvas o simulación de ejecución aplicada, INCONCLUSO, no aprobado por fee duplicada sola.
Comprobar degradación suave de vecinos, concentración y contribución repetida de cada feature frente a comparables; una feature sin aporte puede omitirse únicamente mediante shortlist/selector ya definidos, no crear una configuración nueva tras confirmación. No promover por un mejor fold.100trades no acredita significancia.
Un fallo final implica rechazo o V2declarada; no retuning de esta V1. Si reglas cambian tras confirmación, esa ventana es desarrollo para la nueva versión.

## Presupuesto, incidentes y continuación
Máximo160sesiones económicas=96exploración+16confirmación+48robustez. Intentos técnicos de fase0 separados y todos registrados. Cancelados/retries registran motivo,config,datos,timestamps,duración y dashboard_url real. Retrys sólo por errores técnicos con lógica y datos idénticos.
Al prerregistrar:0sesiones de búsqueda económica V1,4intentos técnicos iniciales fase0; los adicionales se registran en registry.json; ninguno autoriza promoción ni consulta2026.
2026sigue cerrado a nuevas consultas; autorización K1001no se extiende a estas estrategias. Una futura evaluación2026requiere propuesta y autorización específica tras estrategia/protocolo inmutables. No live/paper ni órdenes.
Próximo paso concreto: renovación controlada del servicio/MCP local con permiso según handoff/AGENTS,smoke de propagación5bps,conciliación y cierre de instrumentación/nuevas funciones. Luego trainE1,registro previo de selección y evaluaciónE1.
