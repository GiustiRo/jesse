# SPY40: matriz propuesta de diez escenarios nuevos

Fecha local:18 de octubre de2026. **Pendiente de revisión root. No se crearon estrategias R40Spy ni se iniciaron corridas.** Esta matriz se fija antes de resultados; los ajustes de diseño que root solicite se registrarán antes de código/ejecución.

Leídos: R40_SPY_PAXG_STAGE_PROTOCOL, R20_SPY_PAXG_RESEARCH_RESULTS y PHASE2_RESEARCH_HANDOFF_R20; inventario global e informes SPY20, y matriz completa PAXG20. Esto incluye AR, análogos, reloj direccional, barreras nominales, escaleras, semivarianza y agotamiento ya probados en PAXG. Las diez propuestas no se presentan como causas económicas ni muestras independientes. Algunas investigan representaciones funcionales nuevas dentro de familias conocidas.

## Contrato y construcción temporal común

- SPY-USDT aislado, Binance Perpetual Futures, proxy SPX CFD BID/10 aceptado. Capital10.000USDT,1%riesgo inicial,fee0,00045porlado incluidaLIMIT,5xaislado,gross<=4,4 y90%margen disponible. Reserva10bps sólo sizing. Sin funding, volumen, BTC, nuevos datos, scripts, instalaciones, framework, live/paper o2026.
- Desarrollo2020-10-15→2025-12-31exclusivo; selección acumulada. Comparadores cash y [retest SPY1%](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2) reutilizados, con distinta exposición. Las comparaciones con negativos previos delimitan parentesco, no identifican efectos causales.
- Ruta30m y auxiliarM1. RTH09:30–16:00 America/New_York, DST porZoneInfo. Cada barra requiere30M1consecutivas disponibles y quoteT−60s igual a close. Una sesión diaria válida tiene13barras consecutivas completas; no rellenar festivos/cierres tempranos ni inferir ausencia de relleno upstream.
- D denota sesión completa observada. A es media simple de14true ranges de D previas; excluye D del evento. Noche/cash usan gap log(apertura/cierreprevio) y cash log(cierre/apertura); gap sólo existe si cierreprevio pertenece al día hábil civil anterior (lunes←viernes, resto−1día). No se aplica un calendario NYSE ficticio.
- B denota bloque2h RTH reconstruido con cuatro30m completas:09:30–11:30,11:30–13:30,13:30–15:30. El último30m se usa para D, no se rellena como cuartoB. Ningún B parcial entra en señales. OHLC del bloque agrega sólo esas barras. No equivalen a candles2h UTC de Jesse.
- Se guardan únicamente estados conocidos en su origen, incluso mientras existe posición. Un evento ocupado se consume sin cola. Se reportarán horas reales y ausencias; historia insuficiente conserva cash de arranque.
- Entradas MARKET. Stop inicial común2A desde fill y sin trailing/BE, salvo salida de fase especificada. Cantidad incluye fees/reserva y techos originales. Una posición, sin piramidado, redondeo0,001. Stops/targets activos24/7. Salida temporal adeuda hasta primer quote propio fresco; no ejecutar a precio ficticio de un cierre ausente.
- Indicadores: MCP get_indicator_details consultado para bandpass,correlation_cycle,voss,frama. Se usa sólo bandpass en01; no FRAMA como sustituto deEMA ni diez crosses. Si hay un indicador con desplazamiento/NaN, se usa únicamente su último valor disponible y valores guardados en decisiones anteriores; nunca rellenar una línea desplazada con valores futuros.

## SPY40-01 — R40SpyCausalCycle2h

**Pregunta/información:** una oscilación de duración intermedia puede tener fase explotable aunque no exista retorno a una media o nivel. El filtro separa banda de frecuencias, no observa ciclo económico ni hace un pronóstico certificado.

**Regla:** al cerrar B, con al menos100B, ta.bandpass con defaults period20/bandwidth0,3. Guardar bp y bp_normalized del ÚLTIMO punto en cada decisión; no usar valores históricos recalculados como si hubieran sido conocidos antes. Long cuando normalized cruza hacia arriba−0,5; short al cruzar hacia abajo+0,5. Exigir amplitud max(bp)−min(bp) de los20valores guardados ANTERIORES >0,0019*precio. NaN/no finito => no señal, sin fallback.

**Salida:** stop2A; salida MARKET si un long alcanza/cruza+0,5 normalized o short−0,5, usando B completos y quote fresca; máximo120h desde fill. Cada cruce es evento nuevo; ocupado se consume.

**Frecuencia esperada:** varias oscilaciones por trimestre, posiblemente decenas de trades por año después de arranque; no exige crash ni nuevo máximo. Es expectativa cualitativa, no conteo medido.

**Contraste/novedad:** familia oscilatoria relacionada con MR, pero fase de banda y amplitud, no RSI3/EMA20, canal fallido u ORB. Cash/retest y negativos MR son contexto; una superviviente requerirá control de fase aparte.

## SPY40-02 — R40SpyJumpComponentFade

**Pregunta/información:** distinguir desplazamiento concentrado en saltos de variación difusa dentro del día; evaluar corrección posterior sin atribuir noticias o flujo.

**Regla:** al cierre D calcular13retornos log(close30m/open30m). RV=sum(r²), BV=(pi/2)*(13/12)*sum(abs(r[i]*r[i−1])). J=max(RV−BV,0)/RV, con RV>0. Si J>=1/3 y abs(log(cierreD/aperturaD))>=0,5*A/cierreDprevio, entrar en sentido contrario al retorno cash. Una oportunidad por D. No existe condición de gap favorable.

**Salida:** stop2A, sin TP, máximo72h desde fill.

**Frecuencia esperada:** episodios distribuidos durante años ordinarios, previsiblemente al menos varios por trimestre; no exige un10% de caída. J es un funcional de13datos, no test de salto estadísticamente validado.

**Contraste/novedad:** SPY20-03 también compraba una sesión bajista, pero exigía noche no negativa y cierre bajo; aquí información adicional es concentración intradía de variación, simétrica long/short. No sustituir RSI por J fingiendo independencia: se contrasta esa representación específica.

## SPY40-03 — R40SpyOccupationFlip

**Pregunta/información:** una sesión puede abandonar al final la zona donde estuvo la mayor parte de sus cierres; duración de aceptación y rechazo final no están resumidos por OHLC diario.

**Regla:** al cierre D, contar sus13closes30m respecto de aperturaRTH. Si al menos10estuvieron por encima pero cierreD<=apertura−0,25A, short. Simétrico: al menos10por debajo y cierreD>=apertura+0,25A =>long. Empates exactos no suman. Se sigue la ruptura final CONTRA la ocupación previa, no se compra automáticamente un día rojo.

**Salida:** stop2A, sin TP, máximo72h. Un evento por sesión.

**Frecuencia esperada:** reversiones intradía ordinarias, del orden mensual o más; no grandes crashes. Las condiciones pueden reducir N y no se cambiarán tras resultados.

**Contraste/novedad:** no ORB/Drive ni gap; aporta orden temporal/ocupación durante toda la sesión frente a único candle de rechazo. Tiene parentesco con subasta fallida y aceptación BTC previamente investigada, pero sin canal/pivots/volumen y con otra definición observable.

## SPY40-04 — R40SpyOrdinalEntropy

**Pregunta/información:** la organización ordinal de recorridos puede representar una persistencia distinta a pendiente, RSI o un run fijo; se prueba predictibilidad, no una causa observada.

**Regla:** con los13closes30m de cada D generar11triples consecutivos, contar sus seis permutaciones y H=−sum(p*log(p))/log(6). Triples con empate invalidan H de esa sesión (no desempate artificial). Umbral de baja entropía: percentil25 de los60H diarios válidos ANTERIORES. Estado elegible si Hactual<=umbral y la diferencia entre conteos estrictamente ascendentes012 y descendentes210 tiene magnitud>=2. Side=signo de esa diferencia. Entrar sólo al pasar desde estado0 u opuesto al estado actual.

**Salida:** stop2A, sin TP, máximo72h. Estados se actualizan aun ocupado.

**Frecuencia esperada:** baja entropía relativa ocupa aproximadamente una fracción de los días, no una cola extrema absoluta; se espera una muestra de varias decenas durante la ventana, sin garantía debido al gate de dirección/empates.

**Contraste/novedad:** no es escalera de seis cambios iguales PAXG20-07, ER o ADX con nombre nuevo: distribuye el orden de subtrayectorias y admite ruido entre ellas. Comparadores cash/retest; control de organización ordinal se coordinaría sólo si sobrevive.

## SPY40-05 — R40SpySegmentedResponse

**Pregunta/información:** el mismo retorno diario puede tener diferente pronóstico dependiendo de su reparto entre noche y cash. Modelo funcional, no inferencia de participantes reales.

**Regla:** en cierre D, features x=[1,gaplogD,cashlogD] si gap existe. OLS y=log(cierreD+1/cierreD), usando los últimos120pares válidos dentro de180D anteriores, cuyos targets estén COMPLETAMENTE maduros al decidir. Para cada par, target es el siguiente D completo observado y debe ocurrir en<=120h. Exigir120pares, rango de matriz3 y números finitos; no recortar coeficientes ni regularizar después. Forecast actual=xactual*beta; entrar en su signo si abs(forecast)>0,0019.

**Salida:** stop2A; MARKET en el siguiente cierre D completo observado después del fill. Failsafe120h desde fill con deuda hasta quote fresca. Sin TP. Cada origen diario produce una predicción nueva; no replay del mismo origen.

**Frecuencia esperada:** oportunidades ordinarias de diario tras varios meses de arranque, quizá decenas/año si el pronóstico supera costes; no se presupone señal suficiente ni se baja el hurdle para obtener N.

**Contraste/novedad:** PAXG20-01 AR usaba retorno4h previo; aquí se contrasta la partición noche/cash con target próximo D. SPY20-07 exigía discrepancia fija5D, sin estimar respuesta. Es selección de representación predictiva, no descubrimiento causal independiente. Cash/retest y AR PAXG sólo contexto.

## SPY40-06 — R40SpyRangeCloseInformation

**Pregunta/información:** variación entre cierres y variación dentro de rangos pueden divergir; se prueba si esa discrepancia precede continuación, sin confundirla con varianza total baja.

**Regla:** al cerrar B, sobre los20B ANTERIORES calcular CC=var(ddof0) de20retornos log entre21closes y PK=mean(log(high/low)²)/(4*log2) de20rangos. Ambos finitos, PK>0. Ratio=CC/PK. Al cruzar ratio desde<=1 a>1, entrar en signo del cambio de precio de los últimos5B cerrados, si su magnitud>=0,5A. Guardar el ratio observado; no usar pasado recalculado. Retornos entre B de días distintos incluyen el intervalo nocturno; el rango B sólo incluye sus2h. Esa asimetría es explícita.

**Salida:** stop2A, sin TP, máximo72h. Un evento por transición; no reentrada mientras ratio>1 sin haber salido del estado.

**Frecuencia esperada:** transiciones de régimen de recorrido del orden mensual, potencialmente decenas de eventos; ratio1 es referencia de igualdad entre estimadores, no umbral ajustado.

**Contraste/novedad:** QuietChannel/Squeeze usaban baja volatilidad total antes de expansión. Aquí se contraponen dos observaciones de riesgo diferentes, sin condición de compresión ni ruptura. Relacionado con información de gaps, pero no copia del AcceptedGap SPY20-02.

## SPY40-07 — R40SpyRunDurationResponse

**Pregunta/información:** una secuencia puede continuar o revertir según duración; estimar respuesta condicional madura evita imponer siempre escalera o siempre reversión.

**Regla:** estado=(signo del último retorno D-close→D-close, duración del run limitada a bucket4para>=4). Retorno cero =>estado0 sin señal. Usar252orígenes diarios ANTERIORES con label próximo D ya madura, ocurrida en<=120h; grupo del estado actual requiere>=15observaciones. Forecast=(suma de labels del grupo +20*media global de labels)/(Ngrupo+20), labels log(nextclose/close). Shrink20 es fijo. Requiere252labels maduros y estado histórico calculado sólo con retornos conocidos al origen. Entrar en signo del forecast si magnitud>0,0019, sin escoger después continuación o reversión.

**Salida:** stop2A y siguiente D completo observado; failsafe120h con deuda fresca, sin TP. Un forecast por origen diario, ocupado se consume.

**Frecuencia esperada:** después de aproximadamente un año de historial, los runs1–3 son frecuentes; la condición de forecast puede producir decenas de trades, pero no se garantiza N. No reducir mínimos/shrink/costes tras resultados.

**Contraste/novedad:** PAXG20-07 forzaba continuación de seis cierres y PAXG20-02 analogía de formas. Aquí el objeto es dependencia de duración con respuesta estimada y shrink fijo, no kNN ni pivots del observador BTC. Se reconoce parentesco de modelos predictivos y selección estadística.

## SPY40-08 — R40SpyWeeklyAuctionRepair

**Pregunta/información:** una semana alcista puede distribuir ganancias antes del viernes; la ubicación y orden del máximo semanal pueden anticipar reparación, distinto de un día oversold o gap.

**Regla:** sólo semanas civiles con los cinco D completos lunes–viernes. Al cierre viernes, requerir cierreViernes>aperturaLunes, cierreViernes por debajo del punto medio (maxHighSemana+minLowSemana)/2 y máximo high semanal ocurrido por última vez lunes/martes/miércoles. Ganancia neta cierreViernes−aperturaLunes >=A, para no vender por un rango minúsculo. Short al cierre viernes. Sin espejo long posthoc.

**Salida:** stop2A; TP LIMIT aperturaLunes de la semana conocida; máximo120h desde fill. Cada semana es un origen nuevo.

**Frecuencia esperada:** algunas semanas de cada año, quizá periodicidad mensual; no exige crisis. Semanas incompletas se omiten, por lo que puede quedar inconcluso y se declarará si ocurre.

**Contraste/novedad:** memoria de recorrido semanal y ganancia que no se sostiene, no calendario turn-of-month4/4 ni shortmacroEMA/Donchian. Parentesco con agotamiento/rechazo reconocido; no afirma flujo de fondos ni efecto viernes causal.

## SPY40-09 — R40SpyCloseDensityReversion

**Pregunta/información:** una zona de concentración de cierres anteriores puede ser referencia distinta a la última close o media. Es un perfil de FRECUENCIA DE CIERRES, no volume profile, TPO real ni valor justo.

**Regla:** a las10NY, con cierre D previo del día hábil civil anterior, usar65closes30m de los cinco D completos anteriores. Fijar ancho de bin0,25*A conocido ANTES del primero de esos cinco D. Bins son floor(price/ancho), anclados en cero. Bin modal por conteo; empate el más cercano al último cierre D, y después bin inferior. Referencia=mediana de closes dentro del bin modal. Si distancia del precio actual a referencia>=A diario previo, entrar hacia referencia. Una oportunidad por sesión.

**Salida:** stop2A; TP LIMIT referencia congelada; máximo48h. No mover perfil/target estando abierto.

**Frecuencia esperada:** desviaciones ordinarias respecto a distribución de una semana, potencialmente varias por trimestre o mes. No evento de10% ni condiciones simultáneas extremas.

**Contraste/novedad:** SPY20-01 anclaba cierre anterior y exigía gap; aquí la referencia resume concentración de65observaciones y no requiere gap. Sigue familia MR de niveles, pero añade distribución de precio-tiempo observada; se falsifica sin llamarlo una fuente independiente de alpha.

## SPY40-10 — R40SpyRepeatedBarrierPressure

**Pregunta/información:** tests repetidos con retirada cada vez menor podrían expresar agotamiento de oferta/demanda. No se observan órdenes ni absorción real; se prueba memoria de intentos.

**Regla:** en cada B completo sin episodio, extremos high/low de los10B ANTERIORES definen dos barreras. Si precio está dentro de ellas y a<=0,5A de alguna, armar la más cercana (empate=>no armar), congelando nivel,side,A. Cada nivel/dirección ya armado no se vuelve a usar en la tanda, incluso si vence. Vida12B posteriores. Para barrera superior, test fallido si high>=nivel−0,1A y close<=nivel; simétrico inferior. Exigir dos tests separados>=2B. Guardar mínimo low desde armado hasta primer test y mínimo desde después del primer test hasta el segundo: el segundo debe ser MAYOR para presión alcista; máximos DECRECIENTES para presión bajista. Una vez confirmados los dos tests y estructura, el primer cierre FUTURO más allá de barrera activa long/short. Si no ocurre antes de vencer, consumir sin reciclar. El B de armado no cuenta como test; el segundo test no puede ser también breakout.

**Salida:** stop2A congelado desde fill, sin TP ni trailing; máximo120h desde fill. Estados y vencimientos se actualizan ocupado; no se guardan entradas pendientes.

**Frecuencia esperada:** patrones de varios días alrededor de extremos locales frecuentes; se espera más actividad que un crash10%, aunque tests+estructura pueden reducir la muestra. Sin ajuste de tolerancia/ventana para N.

**Contraste/novedad:** retest Donchian compraba una ruptura y vuelta al límite; aquí se exige historia de dos rechazos ANTES de ruptura y retirada decreciente. PAXG20-06 recordaba un extremo tras pérdida profunda, sin esta secuencia. Misma familia amplia de presión/breakout y no independencia estadística.

## Criterios, observabilidad y cola

Cada fila tiene un full primario, después de revisión root de matriz y código. Dos slots SPY y uno de análisis, cuatro/dos globales. Mantener diez snapshots autocontenidos; no módulo externo que pueda cambiar silenciosamente el significado de una sesión.

Gates descriptivos: neto>0,PF>=1,2,Naprox30,DD no peor que−25%, y luego5/10bpsRT estáticos, concentración, años y capital-tiempo. Pocas operaciones=>inconcluso, no rebajar filtros. Objetivos mensuales/trimestrales pertenecen a cartera. Comparadores existentes no reemplazan controles de mecanismo; si hay pista, root fija una validación aparte antes de sensibilidad/integración.

Registrar contadores de disponibilidad, sesiones/B válidos, eventos elegibles/ocupados y razones de no señal mediante logs resumidos predefinidos al finalizar, si el contrato de herramientas permite recuperarlos; no fingir variables exportadas a snapshots. Esto es instrumentación de estrategias, no script nuevo. No usar rendimiento para redefinir cobertura. Nunca asumir que frecuencia esperada fue medida.

R40 añade selección al inventario anterior. No abrir2026 ni convertir una subdivisión de2020–2025 en OOS. No prometer que otra tanda encontrará mejora. Matriz pendiente de revisión root; ningún resultado observado.
