# R34 C — normalización de volatilidad frente a espera24h
Fecha: 22 de octubre de 2026. Protocolo previo a fuentes, checks y economía. Root aprobó concepto; presupuesto global siguiente ronda5motores (A2/B1/C2), máximo2motores y1análisis simultáneos. Aquí sólo documentos; C consume como máximo2motores futuros, sin vecinos tras resultados.

## Pregunta y adaptación
Tras un episodio de volatilidad elevada, ¿esperar su disipación observable permite una operativa mejor que esperar un día? Hipótesis: el movimiento reciente puede explotarse después del reajuste desordenado, durante48h; rival: amplitud no informa dirección, o esperar llega tarde. No se afirma flujo, liquidación o causalidad identificada.
Antecedente directo R20SpyPostShockReentry: vol10/60, pico de vol5 y normalización; sólo2trades SPY no prueban ventaja. Transferencia de IDEA a otro subyacente, no estrategia equivalente:10sesiones→10barras4h,60sesiones→60barras4h,5sesiones→5barras4h,episodio20sesiones→20barras4h. Entrada anteslongahoraambossentidos, horizonte240h→48h común. BTC24/7 deliberado, sin horarios SPY/DST/NYSE ni datos del proxy. Leído jesse://strategy, TradingHours/adaptation.

Leídos cercanos V4_VOLUME_SHOCK_1H_PROPOSAL, C_PROTOCOL/CD_FINAL, F_PROTOCOL/F_FINAL, V2_PROTOCOL, Y_PROTOCOL, fuentes MultiAssetVolBudget4h, ResearchPaxgShockContinue/Reverse4h y BtcResearchR12ReversionBase1m. V4 revierte shock1h inmediato6h; F sigue/revierte concentraciónRV/BV24h/48h; CUSUM y absorción no esperan disipación; ATR V2 escala protección; Y aprende asociaciones; recuperaciónE usa excursión deprecio/mitadprofundidad. Esta comparación cambia reloj/contexto de explotación, no agrega gate aR32 ni reclama novedad universal. Propuesta motivada y antecedentes completos: BTC_POST_STRESS_NORMALIZATION_PROPOSAL_20261022.md.

## Variables exactas
RutaM1 propia BTC, dato4h; base R32 valida64OHLC consecutivas, cerradas, coherentes y finitas, terminandoT−4h. Decidir sólo T4hUTC. Usar últimos61cierres C0…C60, r_i=C_i/C_(i−1)−1,60retornos SIMPLES (no log). Sigma poblacional ddof0, sin anualizar: v60 sobre60,v10 sobreúltimos10,v5 sobreúltimos5. Una serie exactamente constante tiene sigma0; aritmética nofinita invalida, sin epsilon,clamp,imputación o búsqueda de filas más viejas.
Estado S=(v60>0 y v10>2v60), estricto;60incluye10, no baseline preevento independiente. Primera observación válida sólo inicializa S. En transición false→true, sin episodio vigente, armar T0, pico=v5. No se opera al armar.

## Episodio común y oportunidades
Conservar un único episodio de T0 hasta edad20barras4h inclusive (80h), aun cuando una oportunidad ya fue consumida o hubo entrada/cierre. Cada decisión válida actualiza pico=max(picoanterior,v5actual) ANTES de evaluar normalización. No hay pico futuro ni búsqueda retrospectiva. Nuevos cruces de S durante el episodio se ignoran y no quedan en cola.
Ambas hojas procesan el MISMO estado de mercado y ambos disparadores:
- NORMAL: primera edad1…20 con v5<0,5pico, estricto. Marcar normal_done en ese instante, incluso si el signo es cero o la cuenta bloquea.
- DAY: edad exacta6barras=24h. Marcar day_done una sola vez, sin condición de amplitud.
NORMAL devuelve la primera oportunidadNORMAL; DAY sóloDAY. Los dos flags se actualizan en AMBAS hojas, por lo que el universo/rearmado no depende de tratamiento, ocupación o entradas anteriores.
A edad20, evaluar/consumir y luego caducar. Si no normalizó, no hay tradeNORMAL; no ampliarTTL. En la siguiente decisión sólo un NUEVO false→true puede armar, sin recuperar cruces ignorados. No terminar episodio al entrar ni cuando se normaliza.
T<=últimoT no-op; salto de reloj o ventana inválida censura episodio y reinicializa. Primera válida posterior sólo inicializa S, sin evento fabricado. Estado avanza antes deSTART/FINISH/ocupación/ATR/sizing según baseR32.

## Dirección, ejecución y economía
En cada oportunidad propia: delta=C_actual−C_cinco_barras_atrás (20h conocidas). Delta>0long,<0short,0consume sin entrada. No usar cambio futuro ni PnL; ambos brazos pueden tener signos distintos por tiempos distintos. Comparación de políticas completas, no efecto puro del reloj en trades idénticos.
Hojas propuestas BtcResearchR34VolNormal1m y BtcResearchR34VolDay1m. Heredan baseR32 intacta: HOLD_HOURS48,TP_RNone; MARKET actual,stop2ATR14simpleACTUALcongelado,48h desde fill evaluado4h,terminalconcostos. NoTP/BE/trailing/parciales/reversión/cola; bloqueo en misma salida. ATR usa15OHLC/14TR, independiente de sigma. Geometría común declarada,noóptima.
Cada alternativa10k total,cuota1%,legacy_plan(.5wallet,.5margin),reserva.001 sólo sizing,lote.001,3xaislado. Otra cuota ociosa sin redistribuir; BTCfuturototal2%,global6%. Fee taker.00045 por lado,fundinghistON9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,slippage0. UTC[2020-10-15,2026-01-01),warmup240común,R11M1+fills yfronteraspostfunding/predecisión. Reutilización adaptativa,noOOS,nosumaralternativas.

## Decisión, evidencia y límites
Gatesr9 completos: CAGR>=30%,PFnetUSDT>=1.2,DDM1<=25%(objetivo20),Mactivos>=65%,Q>=80%,medianacalendario>0,netosin2mejoresmeses>0,N>=100 sólo suficiencia preliminar. PreferenciaNORMAL requiere neto mayor,DDno mayor y no menos mesesCALENDARIOpositivos queDAY, además de sus puertas absolutas para ser candidata. Ventaja relativa no rescata negativo; si no cumple,cerrar comparación.
Logepisodios ARM/NORMAL/DAY/EXPIRE/CENSORED conorigen,tiempo,edad,σ ysigno (incluido0); ambosregistranambosdisparadores, permitiendo verificar mismoestado sinconsultarvelasnuevas. PLAN/OPEN/CLOSE/SUMMARYbase compactos. Reconciliar lifecycle/funding/fees/equity/meses/DD yterminal PRE/FINAL; contadoropenpreterminal no es estadofinal por sísolo.
Checks futuros antes de motores: causalidad/61cierres/ddof/constantes/umbrales,elevado→normal,pico actualizado,edad0/1/6/20/21,ignorarshockintermedio,ambosflags enambas,signo0consumido,ocupado/noqueue,invalidación/reinicio/relojmonotónico,mismoestadoentrehojas,logs<1800 ybasehash. No ejecutados en esteentregable.
Sin fuentes creadas, jobs o motores aún. No vecinos, estrés, riskgrid, nuevosdatos/imports,2026nuevo,USDC,cartera,livepaper,Pi,install oconfigglobal. Root revisa CODES y asigna siguiente paso.
