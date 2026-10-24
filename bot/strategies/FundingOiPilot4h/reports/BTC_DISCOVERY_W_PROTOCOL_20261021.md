# BTC Discovery W — dos pasajes con barreras competidoras: estado observado frente a tipo

## Estado y pregunta previa
2026-10-21. Root aprobó posteriormente IMPLEMENTACIÓN y checks sintéticos únicamente. CERO drafts/economía o consultas de velas observadas. Nombres BtcResearchR23PassageBase1m/BtcResearchR23PassageState1m/BtcResearchR23PassageType1m. Revisión root e independiente de fuentes/check antes de borradores. Diseño fijado antes del resultado económico V; no depende de su PnL. Guardar este archivo no autoriza motores ni obliga a gastar presupuesto.

Pregunta: ¿añadir FAST/SLOW observado al tipo REV/CONT de un episodio causal de dos pasajes mejora una predicción BTC24h frente al tipo solo, manteniendo las mismas etiquetas/eventos/admisibilidad/costos/gestión? Es comparación predictiva de políticas y representación del estado observado, NO velocidad pura, causalidad económica, información temporal aislada, test de significancia ni promesa de rentabilidad.

El mecanismo permite que después del primer pasaje compitan retorno y continuación. Así cambia estructuralmente la condición de terminación frente a esperar exclusivamente retorno. No añadir TTL, corte diario, otra resolución ni filtros de overshoot para fabricar eventos/muestra. No garantiza terminación si el precio permanece dentro de bandas; incompletos se conservan como censurados, no SLOW. Las propuestas previas de ancla indefinida o reseteo diario fueron descartes de diseño, no nuevas económicas W que se oculten.

## Inventario exacto y cierres
Se leyeron completos por MCP los nueve textos de fuentes siguientes; CODES completo y hashes guardados ANTES de cualquier implementación:
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR12ArBase1m: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- R20PaxgStaircase4h: 9a2a8cda79a41ea1839c46757495e910a4ef18ff9361c29879ce6f0cb050e8c0
- R20PaxgDirectionalOvershoot1h: b422f3ecf6dc7f66fccce8bba0e25e3d83df0e14c724dc408b530a9db7f9ca90
- R40SpyRepeatedBarrierPressure: 01d84640b6d7accfcf259526d35015cd99aa2e881481d955bb9e49aaf90622da
- R40SpyRunDurationResponse: 4d3460d0924855009f3da18e4a871205921716a3e5e818e379c88c1bf8a04907
- AngleBtcProbability4h: d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1
- AngleCombinedBtcEventClock1m: 038554637216a164f0e16b6f01d5063fc78cc70442cea34ee324979c7f92cb70

Diferencias:
- R20PaxgStaircase4h: seis cambios monotónicos, límites individuales .75ATR y avance1.5ATR; no dos pasajes/duración relativa.
- R20PaxgDirectionalOvershoot1h: extremos móviles y umbral2ATR congelado por fase; no ancla absoluta con retorno o2d competidores. PAXG, no resultado BTC trasladable.
- AngleCombinedBtcEventClock1m: cambios1ATR desde extremos M1 para habilitar shorts filtrados de una cartera; descartada y no ajustar amplitud/ATR/STOP/inicialización/timeout/años. W no modifica esa fuente ni receta.
- R40SpyRepeatedBarrierPressure: dos pruebas de una barrera, retrocesos y breakout con caducidad; no competencia de barreras ni media aprendida por tiempos.
- R40SpyRunDurationResponse: signo/longitud de racha diaria cap4,252 casos,shrink20; antecedente de aprendizaje sobre duración, no equivalente exacto. No declarar nueva la idea genérica de aprender por estado.
- AngleBtcProbability4h: cuatro estados por dos signos,labels stop3ATR/4h/costos/haircut y gate1SE. Negativo con aprendizaje completo y cero señales; cierre prohíbe relajar gate, retirar fricción o añadir control incondicional para fabricar trades. W no rescata ese modelo; tiene estado/evento y contraste por tipo distintos, sin borrar su antecedente.
- R/G/S/V tienen modelos/targets/inputs y cierres propios; W no cambia sus ventanas/horizontes/regularización ni retira componentes/lados.

Cierres completos consultados/guardados:
- strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_PROTOCOL_20261018.md
- strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_INITIAL_RESULT_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md

Dashboards históricos, no corridas nuevas W:
http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c
http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967

No equivalente exacto encontrado en inventario acotado; no afirmar censo universal ni independencia respecto a búsqueda global. 2020–25 ampliamente explorado: desarrollo adaptativo, no OOS limpio. No inferir fracaso de toda duración/estructura ni aprobar W por obligación.

## Datos y reloj
BTC-USDT Binance Perpetual Futures, una ruta trading1m para ejecución/observador y data-only BTC4h. Sin ETH u otros activos. Datos existentes, ninguna importación/feed nuevo, preinspección de cobertura, get_candles por herramientas, exportación ni2026 económico nuevo. No scripts o backtests anidados. El motor es autoridad de faltantes: registrar limitación y detener/evaluar insuficiencia, sin importar ni ampliar warmup por PnL.

B=14.400.000ms; decisiones/eventos sólo cierres UTC4h T. Excluir toda vela con open+B>T; últimaopen=T-B. OHLC finito/positivo/coherente, timestamps consecutivos/alineados UTC; no interpolación ni sustitución de filas inválidas por otras más viejas. Close BTC4h coincide con precio route1m actual con tolerancia técnica heredada R12AR. Volumen/funding no son features ni filtros.

Warmup fijo1000 del mayor timeframe4h. La cobertura/retención1000 previa NO está acreditada: no consultar datos para demostrarla antes del motor. Primer T4h con EXACTAS últimas1000 filas cerradas consecutivas válidas permite bootstrap. Si aún no hay ventana válida1000, cash; no usar1000 últimas válidas dispersas ni ampliar lookback. Una vez bootstrap efectuado, no volver a hacerlo aunque haya gaps: recuperación requiere formar nuevos eventos/labels online.

## ATR, guard físico y máquina causal exacta
ATR14 SIMPLE conocida al cerrar T: media de14 true ranges de15OHLC consecutivas, cada TR respecto a su cierre anterior. Reutilizar atr14 de R10 para matemática/modelo y sizing; NO taATR Wilder ni memoria retrospectiva de extremos. Ancla nueva sólo si a=C_T finito>0,d=ATR_T finita>0 y referencias a-2d y a+2d finitas estrictamente positivas. Guard físico sin buffer/epsilon ni filtro económico. Si ATR/guard impide ancla, mantener máquina sin ancla e intentar iniciar una en un cierre posterior válido, sin evento; no borrar banco por sólo ese guard. Protecciones/deadlines de posiciones reales siguen activos.

Estado inicial de episodio: a,d,T0 congelados. Al crear ancla no procesar un cruce en ese mismo cierre.

Primer pasaje, cada cierre posterior T>T0:
- Si a-d<C_T<a+d, esperar.
- Primer C_T>=a+d establece s=+1;primer C_T<=a-d establece s=-1, fecha T1=T.
- Si ese primer cruce ya cumple s*(C_T-a)>=2d, incluido exactamente2d, episodio DEGENERADO: no evento,no label/no FAST/SLOW. Intentar reset ancla en C_T con ATR actual/guard; no procesar de nuevo ese mismo cierre.
- Si d<=s*(C_T-a)<2d, guardar s,T1 y u=T1-T0>0. Congelar a,d: no moverlos a extremos ni ajustar con ATR posterior.

Segundo pasaje, sólo cierre T>T1:
- Si s*(C_T-a)<=0: tipoREV,r=-s.
- Si s*(C_T-a)>=2d: tipoCONT,r=s.
- Si0<s*(C_T-a)<2d: esperar.
Las dos barreras no se satisfacen simultáneamente con d>0. Evento observado completo en T2=T: v=T2-T1>0,fast=(v<u),igualdad v==u =>SLOW. Usar tiempos enteros/bar count, sin interpolar cruce intrabar, ni high/low para fabricar T1/T2, ni dos eventos en un cierre.

Después de completar: guardar evento y reset a=C_T2,d=ATRactual si válido,para procesar recién un cierre posterior. Si nueva ATR/guard inválido queda sin ancla; no reclasificar el evento previo ni alterar su pending label por ese solo motivo. Cada episodio usa d conocida en su propio T0, y el siguiente usa nueva escala. Ninguna cola de señales reales por incompletos.

Overshoots se aceptan/declararán como precios observados de cierres: primer cruce no degenerado puede superar d, segundo puede superar a o2d. No ejecutar trades en barreras históricas ni interpolar un fill en ellas. Si REV cruza mucho más allá de a, sigue siendo REV de ese episodio; el reset no cuenta como otro pasaje.

## Bootstrap matemático UNA vez
En el primer T4h admisible con1000 filas exactas, índices0…999, todos cierres<=T:
1. Rows0…14 suministran las15OHLC de la primera ATR. Intentar primera ancla en close_time(row14), usando sólo rows0…14.
2. Replay cronológico rows15…999, UNA nueva barra por paso y mismas reglas de máquina/ATR causal que runtime. Para ATR de rowj usar rows[j-14:j+1],sin mirar posteriores.
3. Madurar etiquetas previas antes del evento de cada paso. Sólo labels cuyo deadline<=tiempo de ese paso pueden entrar al banco. Al terminar, todos labels en banco están realmente conocidos en T.
4. Mantener máquina/pendientes/banco producidos por replay y último timestamp procesado. NO emitir órdenes ni señales negociables durante replay ni en T de inicialización. Aunque el último row complete evento y banco ya tenga240, ese evento es bootstrap no negociable; su label puede quedar pending matemático.
5. Primer evento negociable debe completarse en T posterior al T de inicialización; no encolar el de inicialización para cuando quede flat.

No entrenamiento precalculado desde futuro, replay financiero, órdenes ficticias, simulación de cuenta o backtest anidado. Sólo características/labels matemáticas con cierres ya disponibles. Todo cash inicial real permanece en calendario/R11. El máximo de eventos es limitado por mínimo dos cierres por episodio y burn-inATR;1000 filas no garantizan240 labels ni20 casos por celda.

Después del bootstrap procesar exactamente una barra NUEVA por T4h, con timestamp estrictamente creciente; no reprocesar barras, reiniciar desde ventana móvil1000 ni consultar pasado para rellenar banco. Ventanas auxiliares de15OHLC sólo sirven a la ATR/validación actual. Un gap o timestamp repetido/atrasado/invalidez se maneja según reset común, no continuación artificial.

## Labels y reset de integridad
Cada evento completo e=(T2,type,fast,r,C_T2,a,d,u,v) genera pending con deadline=T2+6B y seis barras futuras requeridas, no un resultado inmediato. Degenerados/incompletos no generan pending. Al llegar seis cierres futuros consecutivos válidos:
y_e=r*[log(C_(T2+6B))-log(C_T2)].
Precio bruto sin stop/costos/funding de forecast. No dividir por d ni ATR, no target stop-aware S, no cambio de horizonte, no ajustar etiqueta porque se habría cerrado un trade real. Label no es trade ni retorno de cuenta.

En cada nuevo T4h, madurar pendientes antiguas ANTES de crear evento actual. Un label con deadline==T es conocido y puede entrenar forecast actual. Evento actual entra sólo a pending hastaT+6B y jamás entrena su propio forecast. Maduración no se adelanta por tocar alguna barrera o stop real. Pendientes conservan origen/precio/r/tipo/celda; nada se reetiqueta por refit.

Cada label exige las seis futuras barras consecutivas válidas, no sólo target final. Ante gap/OHLC inválido/asof desalineado: reset COMÚN de máquina, pendientes y banco de ambos modelos,neutralidad/cash nuevas entradas. No clasificar gaps como SLOW, no imputar label,guardar banco anterior,backfill con casos viejos ni replay del bootstrap. Recuperación: esperar15OHLC válidas consecutivas para ancla nueva y formar online240 labels nuevos. No repetir warmup1000. Stops y timeout de posiciones reales siguen en el motor/reloj4h; invalidar feature no cancela protección ni extiende plazo.

Censura terminal: episodio abierto a FINISH es incompleto/no label,no SLOW; eventos completos con deadline>FINISH quedan pendientes censurados,no entrenan. No consultar2026 para madurarlos. No equivaler número de eventos a número de labels o trades.

## Dos estimadores y dominio COMPARTIDO
Banco rolling de exactamente los últimos240 eventos con labels maduros válidos desde última inicialización/reset; igual orden temporal/labels para ambos modelos. Hasta que tenga240 COMPLETOS,ambos cash. Después,al madurar otro,retirar el más viejo: no extender ventana para llenar celdas. No filtrar por signo,r,subperíodo,PnL,tamaño de overshoot o duración.

Para evento ACTUAL completo con tipo q y fast f:
STATE:media simple de y de los eventos del banco con(type=q,fast=f).
TYPE_CONTROL:media simple de y de todos eventos del MISMO banco contype=q, sin subdividir por fast.
Exigir n_(q,f)>=20 en AMBOS modelos,además banco240/medias finitas y datos comunes; no permitir que TYPE opere mientras STATE carece de soporte. Si falla,ambos cash aunque control tenga más casos por tipo. No rellenar20 con observaciones fuera de las240. Muestreo/validez idénticos, pero señales/ocupación/capital posteriores pueden diferir.

Sin shrinkage,SE,prior,regresión,kNN,pesos,regímenes,SEgate o modelsearch. El control por tipo evita confundir una mezcla distinta REV/CONT con el añadidoFAST; no usar GLOBAL de ambos tipos como sustituto ni ganador adicional.

Para CADA modelo: scoreBTC=r_actual*media_label. Score>.0019 LONG;score<-.0019 SHORT;igualdad/banda[-.0019,.0019]cash. Esto preserva orientación: media_label positiva significa seguir segundo pasaje r;negativa ir contra él. No interpretar media positiva directamente como long. r sólo es signo observado del segundo pasaje; sin dirección futura.

El hurdle.0019 es regla fija de señal heredada,NO fee extra debitado en PnL ni garantía de rentabilidad. Calcular/consumir evento aun ocupado/pendiente/sameexit; no esperar a quedar flat, encolar,reversa ni entrar tras salir de posición en el mismo T. No nuevo forecast entre eventos sólo porque una label madura o cuenta queda libre. Todos usan calendario/M1observer; decisión económica sólo al evento completo posterior al bootstrap.

## Ejecución, gestión y cuenta congelados
BTC individual,10k,2%por operación/6%agregado/3x aislado;una posición,sin pirámides. Ventana[2020-10-15,2026-01-01)UTC;START<decisión<FINISH. FundingBTC históricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado,marcasproxy declaradas. Fee.00045porlado takerdescuento,slippage aplicado0. Sin variantes riesgo/comisiones ni estrés; sin reservas legacy.001/LOT.001 deU/P por accidente.

Reutilizar entry_plan R10 y on_open/update_position R12AR,observador/cierre R11 SINCAMBIOS:
- Capitalmax(0,balance)flat,available_margin,feeaware2%,margen90%/floor8.
- MARKET precioBTC actual conocido,enT2,NO precio barrera a/2d.
- SL inicial2ATR14SIMPLE BTC ACTUAL de15OHLC enT2,congelado desde plan y relativo al fill real. D del ancla antigua sólo feature,NO distancia de stop si escala actual difiere.
- SinTP/BE/trailing/parciales;timeout24h=6B desde opened_at real,evaluado primeras fronteras4h elegibles;stop brokerM1.
- No guarda de TP ficticio ni ajuste por tipo,fast,duración/forecast;plan inválido=>noentrada,sin alterar banco/máquina.
- Gap/OHLC inválido resetea todo estado predictivo común, sin detener protecciones/deadlines reales. OHLC válido con ATR actual0/None NO impide madurar pending ni procesar episodio con d antigua válida; sólo impide nueva ancla/plan de entrada. Ningún early-return por ATR antes de maduraciones/evento. No heredar TP2R/48h R11 accidentalmente: R12AR override obligatorio.

Labels precio bruto vs ledger real con fees/funding son objetos distintos. Predecir retorno relativo al segundo pasaje no garantiza utilidad con SL/costos o distribución mensual. No corregir target/protección tras PnL.

R11 equitywallet+PnLabierto M1/fills y fronteras00UTC postfunding/predecisión porfase,no agrupación estricta evento por mes;DDM1+fills,no todos extremos intraminuto. Activity/fillcounters reales separados de eventos/labels/replay. Cierre terminal postfee reemplaza PRETERMINAL con FINAL como padre. No modificar framework/config global.

## Telemetría y viabilidad documental
Contadores limitados por etapa bootstrap/runtime y por ventana evaluada: barras válidas/invalid/reset,anclas físicas/ATRrechazadas,primerospasajes,degenerados,REV/CONTFAST/SLOW,empates,censurados,labels pendientes/maduros,banklen/celln,insuficiencia240/20,signals/occupied/sameexit/fills. Guardar en fill real T0/T1/T2,a,d,u/v,r,type,fast,medias/state/type,ncelda/ntipo,bankfirst/last/deadlines,score y SLactual. Historial de eventos no es universo de órdenes hipotéticas. Evitar logporM1;resúmenes bounded y evidencia de fillsreales.

Modelo finito viable con estado de ancla/fase,cola de pendientes madurados por reloj,deque240 y contadores por4celdas/2tipos. Replay1000una vez +procesamiento incremental porbarra,no barridos recursivos del histórico creciente. No necesita MLframework,datos externos,instalaciones o scripts. Estado matemático común debe ser idéntico entre políticas TODA la trayectoria; órdenes/ocupación jamás retroalimentan anclas,features,pendientes o banco. No se implementa nada ahora.

Objeciones que NO se eliminan con filtros:
- T1 puede sobrepasar d sin llegar2d: distancia restanteCONT<d yREV>d. FAST mezcla tiempo,overshoot/distancia,volatilidad y selección;no velocidad pura.
- u=1barra implica siempreSLOW porquev>=1barra;duraciones discretas no comparan oportunidades equivalentes.
- Condicionar porTYPE no aísla efecto causalFAST ni desequilibrios de dirección/regímenes;forecast es descriptivo,score usa orientaciónr.
- Ancla congelada puede quedar vieja;competingbarriers ayudan a terminar tendencias pero no garantizan completitud en rangos. NoTTL/corte diario/resoluciónrescates.
- Ventana240 por EVENTOS cubre tiempo variable;labels24h se solapan y estados persisten,>=20 no da potencia ni ensayos independientes.
- Bootstrap parcial al comenzar1000 puede cambiar trayectoria de anclas frente a historia infinita;su semilla/burn-in están fijados exante,no se escogerán por resultados.

## Verificación futura, presupuesto y gates
Este protocolo requiere revisión root ANTES de código. Si autoriza más tarde: nuevas fuentes separadas,no tocar padres,readback/hash/CODES y revisión independiente;checks temporales suppliedsourceAST/stubs sin imports de estrategias reales/framework/datos observados/backtests anidados. Oráculos sintéticos de barrerasinclusive/deterioro físico,primercruce>=2ddegenerado,unpasoporcierre,REV/CONT ysignos espejo,overshoots,tieSLOW/u1,anclaATRfrozen/nuevadactual;replay1000row14once/nothingatinit/no currentlabel,rolling240full/shared20/typecontrol/score=r*mu;seisconsecutivas/maturitybeforeevent/gapresetall/no backfill;occupiedconsumption/noqueue/sameexit y R10/R11/R12ARSL24h/terminalfee. Registrar todos fallos,fuentes/códigos/checks/versiones,sin claims runtime de fakes.

Presupuesto FUTUROexactamente2económicas STATE/TYPE_CONTROL,máximo2reemplazos exclusivamente técnicosdocumentados,no porPnL. Máximo2backtests globales/1análisispropio coordinado;ninguna sesión/check/draft autorizado por guardar este documento. Root revisa fuentes/check luego antes de manifest/drafts/motores. No vecinos240/20/1000/.0019/d/2d/u-vtie/TTL/resolución/overshoot/horizonte/stop/target/shrink/SE/dirección/riesgo ni aislar REV/CONT/FAST/lados después. Si insuficiente/cerooperaciones no relajar mínimos ni prometer nuevo ensayo.

Gatesr9 para CADA cuenta:CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65mesesactivoscompletos positivos,Q80completos,mediana mensual calendario>0inclinactivos,netoaritmético sin2mejoresmeses>0,N>=100preliminar operativo sinconfianza/potencia porconteo;aspiración40–50%+/M70. Superarcontrol no basta;control no ganador sustituto automático. NO_CUMPLE alfallar economía;INCONCLUSA si economía favorable sinmedición/suficiencia.

Auditoría futura completa gross-fees+funding=PNLsum=equityfinal-10k a1e-6USDT,funding aplicado/conciliado,2.741.760M1,63intervalos/62meses/20Q yterminalfee. Reportar bootstrap/cash/coverage,completos/parciales,eventosvslabels/trades. Sin promociónoperativa/estrésautomático. Sin nueva economía2026,imports,descargas,live/paper/Pi,install/restart/framework/globalconfig,research_scripts oportfolio. ReportesMCP yHub archivosprimero/índiceúltimo sólo cuando corresponda y se autorice.

## Precisión posterior a revisión root/independiente
ATR actual inválida con OHLC válido es distinta de integridad de datos: pendientes maduran y episodios previamente anclados procesan su cierre con d congelada aunque ATRactual0/None; al completar se puede generar evento/label, pero no nueva ancla ni entrada hasta ATR válida. Gap/OHLC inválido sí borra máquina,pending y banco. Estado matemático idéntico entre modelos durante TODA trayectoria, sin retroalimentación de órdenes/ocupación. Estas precisiones se fijaron antes de fuentes.

## Preparación técnica final antes de economía
Tres nuevas fuentes creadas, padres/antecedentes sin cambios. Primer checkf1e8a4381ec2420cabd48a06cf435689 succeeded117 assertions sobre baseef1cf7776c46ae6af17e8a8fcf041d2db9e7a18b9de3c80574c4942203dfda3c. Revisión root pidió instrumentación explícita de cuatro celdas/empates bootstrap,empates runtime,SLactual/deadlines y censura pending; sólo contadores/logs añadidos. Finalb467a1f27b984da9a413a21eaac103c9 succeeded129 assertions sobre based8ac03f4b02fa3c471fdac510a6d9b2f36c2aa80cd3c0a65661a0cd887fafccc. Los117y129se solapan,no sumar como246pruebas independientes. Cinco funciones puras de ancla/máquina/modelo/advance/forecasts ASTidénticas entre versiones; bootstrap sólo añade contadores. Sin fallos de check W. Recibo completo BTC_DISCOVERY_W_TECHNICAL_CHECK_RECEIPT_20261021.json conserva códigos exactos,fuentes suministradas,ambos jobs/artefactos,versiones/motivo y12readbacks finales exactos. Root+independiente conformes; sin drafts/economía desde este agente. Slot análisis liberado. Matemática determinista independiente de órdenes por fuente y fixtures; no afirmar identidad económica de toda trayectoria observada antes de motor/auditoría.
