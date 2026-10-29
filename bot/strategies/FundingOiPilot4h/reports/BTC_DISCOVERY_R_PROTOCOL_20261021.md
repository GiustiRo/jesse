# Tanda R — forma ordenada BTC24h: kNN fijo frente a media global

Prerregistro2026-10-21 antes de nuevas fuentes/economía. Pregunta material: ¿la forma ORDENADA de los seis retornos4h más recientes permite estimar el retornoBTC de las próximas24h mejor que la media de todos los orígenes maduros del mismo conjunto? Motivación representacional: un vector distingue orden/trayectoria que un conteo/bin o AR1 no conserva; no se propone porque otras recetas hayan fallado ni se promete que la forma sea predictiva.

El estimador es aprendizaje estadístico no paramétrico mínimo mediante NumPy,kNNcosinefijo. NoHMM,redes,búsquedademodelos,MLframeworks,instalaciones o research_scripts. El usuario autorizó decisiones autónomas; no hace falta nueva aprobación para este diseño acotado.

## Antecedentes y límites históricos

Se leyeron completos R20PaxgPathAnalogue4h,AngleBtcProbability4h,BtcResearchR13GeometryBase1m y dependencia BtcResearchR12ArBase1m. Antecedente R20 fue negativo según inventario previo y excluyóBTC:8retornos/escalaATR,Euclidean,k20,minseparación8,lookback720; no se rescata ese resultado ni se impone su separación. AngleBTC usa4estados discretos/payoffsimulado; M geometría de unavance/rango yG autoregresiónAR1 no equivalen a vectorordenado6/L2/cosine. No afirmar novedad universal ni borrar selección histórica; son mecanismos relacionados/adaptativos sobre datos ampliamente explorados. El valor nominal20 no son20regímenes independientes.

Se releyó jesse://strategy, secciónTradingHours/adaptación: este ensayo usaBTC24/7 y el antecedente citado esPAXG24/7, no un mercado de acciones trasplantado. No se importan horariosNYSE/fixingSPY ni calendarios alBTC; observaciones son UTC4h, no filtro horario económico.

HashesSHA256 de textos completos suministrados:
- BtcResearchR12ArBase1m: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- R20PaxgPathAnalogue4h: 0264fe08fcbc8f31b2ef0d40c225558489a98debf7df5b5dc06436a6a9fffc9e
- AngleBtcProbability4h: d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1
- BtcResearchR13GeometryBase1m: 3968e9a2733fbe9e4a22b32ba71d023defcefa79eae65e992833f1810fb82b97

## Conjunto causal exacto

Cada T4h obtiene372velasBTC4h cerradas consecutivas,últimaopen=T-4h yopen+4h<=T,OHLCpositivo/finito/coherente;asofprice=últimocloseBTC. Ventana exacta372no últimos372válidos,no imputación ni inspecciónprebacktest. Currentindex371.

Orígenes i=6..365 inclusive:360candidatos. Feature_i=seislogreturns usando sietecloses i−6..i. Label_i=log(C[i+6]/C[i]),equivalentemente logC[i+6]−logC[i] para evitar overflow del cociente; targets12..371, todosmaduros enT. Featureactual usa closes365..371. Origenactual371 no entra al entrenamiento, tampoco366..370conlabelinmadura. No se usan labels de mañana ni últimos6retornos como resultadospredictivosactuales.

Normalizar cada feature a longitudL2 unitaria, sin restar media ni dividir porATR/volatilidad. Excluir candidato con vector/norma/labelno finito o normaL2<=0; normacurrentno finita/<=0 implica neutralidadCOMÚN deambos modelos. Compartir>=20orígenes válidos para ambos. La ventanaoriginal360no se extiende para conseguir360válidos. Sin epsilon/clipping/winsorization.

kNN:cosine=dot(unitpast,unitcurrent); ordenar descendente y empates EXACTOS priorizan i más antiguo mediante sortestable. Elegir20primeros, forecastmediauniforme de suslabels. No selección por magnitud/costos/PnL posterior,ninguna distanciaumbral oponderacióndeconfiancia. GLOBAL:media de labels de TODOS losmismosorígenesválidos, no sólo20ni un conjunto distinto. Misma normacurrent/validezcomún tambiénparaGLOBAL.

No separación mínima adicional entre análogos ni embargo de features/current:todos los labels están conocidos enT, pero se solapan con otros labels y pueden compartir parte de la ventanaactual. Es entrenamiento online causal en trayectoria continua, no WFposthoc ni muestra independiente; ventanas/transaccionesrepetidas no son repeticiones estadísticas independientes.

## Señal y gestión

Forecast>.0019 BUY;forecast<−.0019 SELL;restocash. Umbralheredado deG/M/R20 como requisito de señal fijo, NO coste adicional aplicado alPNL. Cada4h es una oportunidad nueva incluso si forecastmantiene signo; no convertir a regla de transición. Calcular/consumir aunocupado, descartar sincola,sinreversa y sin entrada tras salida enmismotimestamp.

Tres fuentes nuevas BtcResearchR18AnalogueBase1m,BtcResearchR18AnalogueKnn1m,BtcResearchR18AnalogueGlobal1m; base hereda R12ArBase1m cuya fuentehash1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343 se verificó. Overridebefore para modelo nuevo; onopen/gestión heredados:stop2ATR14SIMPLE4hBTC actual,sinTP,max24h=6BAR evaluadoen4h,proteccionesM1. No cambiarstop/tiempopor similitud,residuo,refit o vecino. R11observador/cierreterminal congelados.

## Ejecución/costos/riesgo

BTC-USDT BinancePerpetualFutures ruta1m,dataBTC4h,warmup4004h,[2020-10-15,2026-01-01)UTC,10k. Riesgo2%poroperación/6%agregado,3xaislado,una posición sin pirámides. HelperR10 entry_plan unchanged feeaware90%margen/floor8,stop2ATRsimple,no reserva de sizingextraP ni cambiosdeexposición. MARKETBTC alcloseconocido. Fee.00045porlado takerdescuento,fundingBTChistóricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado/marksproxydeclarados,slipaplicado0. 2026excluido.

Sin estrés/riskvariants/importaciones/instalaciones/restarts/globalconfig/framework/live/paper/Pi/scripts ni nueva economía2026. Si motorreportafaltantes detener/informar; no preconsultar cobertura ni importar. No se inspeccionaron velas observadas ni resultados económicos deR en esta preparación; el histórico sigue siendo desarrollo ampliamente observado. No usarPnLQ para escogerK,horizonte o signo.

R11equitywallet+PnLabierto M1/fills,cortesmensualesUTC00postfunding/predecisión porfase,DDM1/eventos,noextremosintraminuto. Logfillcompacto forecast/nválidos/similitud/rangoedad/20orígenes elegidos cuandoKNN; fillsreales separados de señalesocupadas. Modelo forecastbareprice, no payoffconstop/costos ni promesa de calibración. No evidencia de rentabilidad hasta auditoría financiera.

## Presupuesto/gates/cierre

Dos económicas KNN/GLOBAL,más hasta2reemplazos sólo técnicosdocumentados,no porPnL. No vecinos deK20/d6/lookback360/h6/distance/hurdle/signo después de resultados. GLOBAL es control predeclarado, no ganador sustitutivo retrospectivo. Cada cuenta debe cumplir gatesr9: CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65mesesactivospositivos,Q80completos,mediana retornomensualcalendario>0 incluidosinactivos,netoaritmético quitandomejores2meses>0,N>=100preliminar operativo sinconfianza/potencia porconteo. Aspiraciones40–50%+/M70no reemplazangates.

Antesdeeconomía: AST/syntheticprovidedsourceonly,sinimportsestrategias/framework/datosobservados/backtestdesdeanálisis. Oráculos372/360/targets12..371/nooriginactual,no labelsfuturas,L2/cosine/tiesolder,zeros/noeps/common>=20/controlmean,direcciónumbral,historyolderirrelevant,ocupación/noqueue/sameexit,gestiónsinTP24h/SLrisk/sizing/callbackFINAL. Guardarcódigoexacto,resultados,todosintentos/errores,CODES/readbacks/hashes. Root revisará fuentes y usarádrafts/manifiestogenuinos/preflight antes motores.

Después snapshotscompletos reconcilian gross−fees+funding=PNLsum=equityfinal−10k1e-6USDT; verificar2.741.760marcasM1,63intervalos/62meses/20Q/cierreterminal. NO_CUMPLE si falla economía; INCONCLUSA si favorable sinmedición. Hubinmutablearchivosprimero/índiceúltimo. Si fallaR,cerrar su presupuesto y otra pregunta material, sin relajar puertas ni rescatarvecinos.

## Preparación técnica antes de economía

Checkfinal98cb30b8d9ac40a292e01402524fef09 succeeded1169aserciones; fuenteeconómica sin cambios después de escritura inicial. Primercheck1924d886b72041bab1688c2287b27c9d fallóSyntaxError en fake del harness por else360sin espacio, antes de ejecutar pruebas; se corrigió sóloharness. Ambosintentos/código/errores conservados. El origenactual371 nunca se entrena; suclose sí es labelmaduro delúltimoorigen365,distinción comprobada por perturbación. Nuevefuentes readbackidénticas,incluyendo padres/deps/antecedentes, yprotocolo leído completo. Noeconomía/drafts.
