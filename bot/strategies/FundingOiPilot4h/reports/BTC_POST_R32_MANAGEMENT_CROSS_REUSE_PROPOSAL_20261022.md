# Después de R32: reutilizar CROSS_P antes de inventar otra salida

Fecha local: 2026-10-22. Estado: propuesta para decisión de root; no protocolo económico final, fuentes nuevas, drafts, jobs, motores o precios observados. Hub vigente r33 leído completo. No se reabren R32 ni K por ajuste de trailing/TP/plazo.

## Recomendación

Priorizar UNA adaptación de la receta CROSS_P congelada al contrato de especialista actual. Pregunta: ¿una entrada por transición de tendencia entre dos escalas y salida por transición opuesta, ya elegible en desarrollo pero nunca confirmada en2024–25 bajo V5, conserva una operativa aprovechable en la trayectoria completa y cuota actuales?

Esto no inventa otro exit indicator ni demuestra que la gestión sea la causa de ventaja. Recupera una pregunta de viabilidad con evidencia pendiente concreta. Si se requiere una atribución de gestión, se propone abajo un control adicional máximo, pendiente de decisión de root; no se ejecuta por defecto.

## Evidencia archivada y selección declarada

[Screening CROSS_P archivado](http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971):77trades, +90.5292% neto del período, CAGR21.3292%, PF1.7118 y DD diario del motor17.6955%, sobre2020-09-01→2024-01-01. No son cifras de una cuenta actual1%, DD M1 o confirmación posterior.

FROZEN_SHORTLIST_V5.md confirma cuatro elegibles y cupo de dos por ranking menorDD. CROSS_P quedó tercera, CROSS_POI cuarta; Funding ocupó ambos lugares. FINAL_DECISION_V5.md confirma que CROSS no tuvo confirmación2024–25. Las pérdidas posteriores de Funding no permiten cambiar retrospectivamente aquel ranking. Esta propuesta declara la selección actual tras conocer todo ese historial; no corrige la selección original ni crea OOS.

El screen auditó35 salidas por cruce opuesto,36stops,5por180barras y1terminal. Son ramas realmente ejercitadas de la receta, sin certificar rentabilidad futura. El mejor screen no basta para aprobar los gates actuales:21.33% no llega a30% y N77 no llega a100; no esconderlo ni transformar su riesgo para obtener el porcentaje.

## Receta que conservaría literalmente

- BTC4h cerrado, medias aritméticas finitas SMA20/SMA80 sobre sus propias ventanas actual y previa;81OHLC consecutivos.
- Entrada long: F_prev<=S_prev y F_now>S_now. Short espejo F_prev>=S_prev y F_now<S_now. Igualdad actual neutral. No entrar por mero estado, sin SMA200, pendiente, RSI, volumen, OI o funding como señal.
- MARKET a precio actual enT4h, sólo flat/sin pending/start<T<finish, máximo una apertura por díaUTC compartida entre lados.
- Distancia inicial3ATR14 SIMPLE actual, congelada y colocada desde fill real. No sustituir por2ATR de R32: sería un nuevo parámetro económico. SinTP, BE, trailing ni stop que siga a la media.
- Salir MARKET cuando aparece cruce opuesto válido enT>opened_at. La salida usa81closes, sin exigir ATR actual u OI para permitirla. Si falta esa ventana no inventar cruce: siguen stop y límite temporal.
- Límite absoluto180barras4h=720h=30d desde fill, al primer cierre4h que alcanza edad, independientemente de datos del indicador. El número es el congelado en V5, no un nuevo vecino de24/48h.
- Protección intrabar nativa; decisión final/fin de ventana y hold tienen prioridad sobre cruce. No stop-and-reverse. El cruce usado para cerrar se consume y no entra enT ni se guarda paraT+1; próxima entrada requiere cruce nuevo. Señales ocupadas/cupo diario se descartan, sin cola.

Hipótesis económica heredada: persistencia a escala de varios días puede requerir que la salida siga el fin de la transición en vez de un objetivo de beneficio. Riesgos heredados: retraso, whipsaws, tendencias perdidas por no reverse, ganancias devueltas, financiación y ocupación larga. Ninguna mejora se presume ni se escoge un lado por su PnL.

## Adaptación explícita al contrato humano actual

Una cuenta BTC alternativa de10000totales, cuota activa1%/otra cuota ociosa, sin redistribución. legacy_plan(event,.5*max(0,wallet),.5*available_margin,3,fee), reserva.001sólo sizing, lote.001 con floor y buffer90% sobre media cuota de margen;6%global/3xaislado. R11 equity wallet+PnL raw y cortesM1+fills, no portfolio_value apalancado.

Difiere del sizing V5 .02*available_margin con cap nocional1x, floor8 y sin reserva. NO es simplemente dividir por dos aquella curva: también cambia el margen/cap efectivo, cantidades, capitalización y ocupación. No usar el screen como control pareado que atribuya efecto aislado al riesgo o la gestión. El perfil nuevo es el obligatorio actual, no una búsqueda entre exposiciones.

Binance Perpetual Futures BTC-USDT; ruta1m/data4h, warmup240; UTC[2020-10-15,2026-01-01). El screen antiguo comienza antes y termina antes. Los años2024–25 no fueron confirmados por ESTA receta V5, pero ya fueron observados ampliamente en otras investigaciones; todo el replay nuevo es desarrollo histórico adaptativo, no holdout/OOS ni walk-forward posterior.

Fee.00045taker porlado, funding históricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 y proxies explícitos, slippage modelado0. Funding ya estaba activado en V5; no presentar esta adaptación como su primera incorporación. SinOI ni nueva dependencia de datos.

R32 base debe permanecer intacta: admite64filas,2ATR y holds24/48h. CROSS exige81filas,3ATR y720h; forzarla allí violaría su contrato. Si root aprueba, se necesita nueva infraestructura mínima aislada heredada del observadorR11 y helperlegacy_plan, reutilizando cross_state congelado y ATRsimple. Sólo adaptar reloj/source de velas a rutaM1/data4h; no reescribir medias ni cambiar semántica de entrada/salida. Eso requerirá protocolo, fuentes/checks/readbacks y auditoría nativa antes de atribuir paridad.

## Control y presupuesto máximo

Recomendación mínima:1motor CROSS_ARCHIVED bajo contrato actual y ventana completa, con referencia archivada meramente descriptiva. Resuelve la viabilidad económica actual, NO el efecto aislado de una salida frente al reloj.

Si root considera necesaria la pregunta específica de gestión:2motores máximo, CROSS_ARCHIVED y CLOCK_ONLY. Entradas, cuota diaria,3ATR, ausenciaTP,720h y todos costos/datos iguales. CLOCK_ONLY omite exclusivamente el cruce de salida: liquida por stop,720h oFINISH. No añadir otro plazo. CROSS_ARCHIVED puede cerrar antes al cambio de tendencia; CLOCK_ONLY es control diagnóstico y también debe cumplir gates para cualquier eventual candidatura, sin promoverlo sólo porque gane a un mal tratamiento.

Las cuentas difieren después por ocupación, tamaños y capital, así que la comparación no mantiene trades pareados ni suma curvas. No tercera política de retorno al origen, reversión automática, vecinos de medias/ATR/plazo o filtros después del resultado. Máximo global2backtests+1analysis coordinado por root; nada iniciado aquí.

Gatesr9 conservados: CAGR>=30%, PFnetUSDT>=1.2, DDM1+fills<=25%(objetivo20), Mactivos>=65%, Q>=80%, medianacalendario>0, netosindosmejoresmeses>0 yN>=100preliminar/no potencia. Muestra pequeña o señal rentable insuficiente se informa sin cambiar puertas; no anualizar sólo tiempo activo. Auditoría financiera y terminal nativa completa será obligatoria; contadorpreterminal no acredita flatfinal.

## Qué alternativas de gestión se revisaron y no se fuerzan

R12AR/DRIFT: salida24h sinTP coherente con forecast6pasos; dos curvas negativas y cierre sin vecinos. No cambiar ese horizonte como rescate.
BSTATE/R14CORE: signos6/24, salida breadthcontrario, sinTP/max180barras; su intervención completa ya probada no es inédita.
V6EFFICIENCY: cruceER24>.35/−.35 y salida por neutralidad de ER rolling, sinTP/max60barras; negativa y con vecinos ya ejecutados. Salir simplemente por estado observable ya existe.
R8Y903: readmisión adversa al anclaVWAP de suplemento con presión positiva y close sobre entry, antes48h; menor neto. ORCHreclaim/R4T401/R7S702/S705 ya probaron cierres de invalidación estructural; no renombrarlos.
R14 fue filtro de entrada/ablación del suplemento, no solución pendiente de gestión; tampoco habilita quitar shorts observados.
La idea inicial de devolver al origen del desplazamiento NO se convierte en estrategia ahora: tiene antecedentes muy próximos y menos evidencia pendiente que CROSS. Se prioriza reutilización sobre fórmula nueva, sin afirmar que toda gestión estructural esté agotada.

## Fuentes consultadas y alcance

Leídos completos porMCP: Hubr33HANDOFF; cardCROSS_P; V5_CROSS_PROPOSAL.md; RESEARCH_PROTOCOL_V5_20261020.md; V5_CROSS_SCREEN_REPORT.md; FROZEN_SHORTLIST_V5.md; FINAL_DECISION_V5.md previamente en esta línea de dedup; ResearchV5CrossP4h yResearchV5Base4h completos; cross_features.py completo. REGISTRY_V5.json: primera página2000líneas con configuración nominal, planned_configurations/CROSS_P, hashes y registro del screen; lectura dirigida, NO declaración de auditoría completa delregistry179k ni de todos sus motores.

HashResearchV5CrossP4h=6e102adcf255761c49599d9aa7c37c39db5396d9eeb18f063927c88e174d6574.
HashResearchV5Base4h=5e0124dbc86305cccfdbbd857ba158a2e7dc10c9fdf2a905f31cfc1dd59890aa.
Hashcross_features.py=5df66fdb107fe3f16484ee5cd1ca91c121c4c8bea0095e3fd95799a354f5e1e0, coincide con hash delregistry5df66fdb....

Para dedup de gestión se leyeron fuentesR12ArBase, BreadthState, EfficiencyP, Y903 yOrchShortReclaimExit; cierresAB/G/H/N yR4/R7/R14. No megasnapshots repetidos, nuevos precios o auditoría de fills viejos.

Decisión pendiente de root: adoptar sólo receta archivada (preferencia por información/menor presupuesto) o exigir ademásCLOCK_ONLY como ablación de gestión. Después se escribiría protocolo final y CODES acotado, no antes de resolver el alcance.
