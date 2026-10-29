# V3 — propuesta de continuación tras pullback de tendencia
Fecha: 2026-10-20.
Estado: DISEÑO ÚNICAMENTE; versiónSMA armonizada por root antes de implementación/resultados. Sustituye el borradorEMA de esta misma tarea; no hubo código, backtests ni resultados entre versiones.
Archivo: strategies/FundingOiPilot4h/reports/V3_TREND_PULLBACK_PROPOSAL.md.
No iniciar sesiones hasta GO global y protocoloV3 guardado por root.

## Hipótesis y alcance
En un régimen de tendencia confirmado por nivel y pendiente de una media lenta, un retroceso a una media rápida seguido de reanudación cerrada puede ofrecer una entrada menos extendida que la ruptura de un rango multibarra.
El sector usa la interacción local de tres barras con medias. No usa extremos del día UTC anterior ni un canal multibarra; H/L de una sola barra del pullback confirma su reanudación.
V2 permanece SIN_CANDIDATA: las evaluaciones ATR+OI positivas no alteran los gates fallidos de train ni prueban esta hipótesis nueva. 2022–2023 y todo resultado de screening que se vea pasan a desarrollo observado.

## Convenciones
BTC-USDT Binance Perpetual Futures, decisión4h UTC sólo sobre barras cerradas; ejecución1m completa. Entrada MARKET. Una posición máxima, sin piramidar, plano/sin entrada pendiente y una entrada ejecutada por día UTC. Gate start<T<finish.
En T, B0 es la barra abierta T−4h que terminó en T. B−1 y B−2 son las dos anteriores. Para cada índicej se conocen OHLC y close Cj. Toda referencia debe existir exactamente en su timestamp; no sustituir barras ausentes ni usar vela en formación.
Historia mínima126 barras4h cerradas consecutivas: permite la SMA120 de seis barras antes. Warmup240velas4h igualV2 propuesto para el protocolo global, sin operar; si no hay126cerradas aún no entrar, contar price_history_invalid. No aumentar warmup según resultado.

## Indicadores reproducibles sin semilla
F_j=SMA20(j)=(C_j+C_(j−1)+...+C_(j−19))/20.
S_j=SMA120(j)=(C_j+C_(j−1)+...+C_(j−119))/120.
S_−6 usa exclusivamente los120cierres que terminan en B−6, no la media actual desplazada por timestamp aproximado. No EMA ni semilla ni recurrencia dependiente del comienzo del fold.
El cálculo puede compartir un buffer de126barras cerradas pero cada suma usa sólo sus índices definidos. F_−1/F_−2 nunca incorporan C0.
Exigir precios finitos/positivos, barras consecutivas cada4h y OHLC coherente (high>=max(open,close),low<=min(open,close),high>=low). Si falta algo, no señal y causa explícita.
SMA20 representa80h (3d8h), SMA120480h (20d), y la comparación seisbarrasantes describe24h de pendiente lenta. Elecciones iniciales fijadas por mecanismo y armonización global, no óptimos estimados ni grilla oculta.

## Entrada long: cuatro condiciones simultáneas
1. Régimen: C0>S0 y S0>S_−6.
2. Aproximación desde arriba: C_−2>F_−2.
3. Pullback en B−1: L_−1<=F_−1<=H_−1.
4. Reanudación ya cerrada: C0>H_−1 y C0>F0.

## Entrada short: espejo exacto
1. Régimen: C0<S0 y S0<S_−6.
2. Aproximación desde abajo: C_−2<F_−2.
3. Pullback en B−1: L_−1<=F_−1<=H_−1.
4. Reanudación ya cerrada: C0<L_−1 y C0<F0.

Igualdad en régimen/aproximación/reanudación no habilita; igualdad en toque sí. La media rápida debe estar dentro del rango completo B−1: no basta que toda la barra haya saltado al lado opuesto. No hay filtro de color de vela, volumen, F>S, cierreB−1 respecto deS, slope rápido ni pendiente lenta de otro horizonte.
El toque se reconoce sólo después de cerrar B−1; la reanudación sólo al cerrar B0. No se entra retroactivamente en el toque y no se exige información de B+1. No hay señal pendiente que sobreviva más barras ni estado discrecional del pullback; se evalúa este patrón de tres barras en cada decisión.
Long/short son mutuamente excluyentes por el régimen; si implementación habilita ambas, falla de invariantes.

## Salida elegida antes de resultados: objetivo3R fijo
A=media aritmética de14 TR de15 OHLC4h cerradas que terminan en B0. Para cada una de las14últimas:
TR_i=max(high_i−low_i,abs(high_i−close_(i−1)),abs(low_i−close_(i−1))).
A=mean(TR), sin suavizadoWilder; exigir A>0 finito y15barras consecutivas.
R=d=2A en unidades de precio, congelado en la decisión de entrada. Desde el fill real e:
- long stop=e−R, target=e+3R;
- short stop=e+R, target=e−3R.
Así, stop2ATR14 y objetivo6ATR14. 3R describe distancia de precio, no beneficio neto tres veces el presupuesto que incluye fees.
Qty completa, STOP protector y LIMIT objetivo. No trailing, break-even, parciales ni cambio de distancia por ATR posterior. No salida adicional al cruzar medias o perder régimen: ésa sería otra hipótesis.
Salida MARKET en primera decisión4h con edad>=72h, o cierre forzado al límite exclusivo del fold con costos. Protecciones operativas aunque falten features tras entrar. Registrar reason explícito holding72h/fold_end/stop-loss/take-profit/invalid_after_fill.
La oportunidad buscada es continuación a varios días. Hold72h permite tres días (18barras4h) para esa extensión; target3R evita añadir una regla de salida de tendencia además del nuevo patrón de entrada. No son estimaciones óptimas ni garantías del ratio obtenido.

## Sizing y costos
C=available_margin antes de la entrada,p=precio de decisión,s=+1long/−1short,f=fee configurada.
d=2A; stop_pre=p−s*d; target_pre=p+s*3d.
Validar C,p,d,stop_pre,target_pre finitos y>0. Si no, distance_invalid, sin truncar barreras a valores favorables.
u=d+f*(p+stop_pre).
qty=floor8(min(C/p,0,02*C/u)).
CapnotionalC, leverage no multiplica tamaño. El presupuesto2% cubre stop y fees planificados de entrada/salida; funding,slippage y gaps adicionales se reportan y pueden excederlo.
Al fill mantener d congelada y anclar ambas protecciones a e. Si pasan a no positivas, registrar entrada y cierre MARKET inmediato, nunca esconder el trade o sustituir reglas.
Capital10000USDT por sesión,isolated3x,fee0,00045 nominal/slip0 para comparabilidadV2; escenarios de ejecución adversa los fijará el protocolo global antes de datos. No hacer haircut posterior como simulación real de fills.

## Dos variantes de ablación
- TREND_PULLBACK_P: sólo precio/SMA/ATR; OI no condiciona disponibilidad ni entrada.
- TREND_PULLBACK_POI: reglaP másOI actual causal válido ypositivo > valor válido/positivo efectivamente observado en la decisión T−24h.
OI no indica dirección. Política heredada V2: label+6m disponibilidad asumida,max_age10m desde disponibilidad, ceros inválidos, sin rellenar huecos. Primeras seis decisiones del período inicializan referencia24h dentro de sesión; no inventarla desde warmup.
Separar ausente,stale,ceroactual,inicialización,referenciainválida yno creciente. OIapagado no exige calidad OI; gestión de posiciones nunca se bloquea por datos.
Funding contable ON en ambas, sin zscore/gatefunding ni uso de próximo pago estimado.
Datasets heredados inmutables:
funding9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571;
OI6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
OI sigue retrospectivo sin certificaciónPIT; funding usa marcasproxy. No se afirma que el retraso asumido conozca la publicación original.

## Pruebas técnicas propuestas
Antes de economía, aún sin ejecutar:
- Sumas SMA20/SMA120 manuales conocidas, media constante y exacta selección de126barras, incluidaS_−6.
- Valores F/S históricos contra sus propios prefijos; mutación futura en B0 o barras posteriores no altera F_−1/F_−2/S_−6.
- Missing/duplicados/NaN/OHLCincoherente/empates; longválido y espejo short; toque sin reanudación, reanudación sin toque y gapenteramente al otro lado deF no habilitan.
- ATR14 arithmetic independiente, stop2A/target6A anclados a fill, capC/floor8/feeestresada y distancia no positiva.
- Holdings72h y cierre de borde con motivo, siempre conciliar bruto−fees+funding=PNL y saldo final.
- Logs <=1900caracteres con hash de buffer y timestamps cuando no quepan126OHLC.

## Auditoría y riesgos
Por oportunidad guardar T,OHLC/timestamps B−2...B0,F_−2,F_−1,F0,S0,S_−6,extremos yhash de buffers que sustentan cadaSMA,valorA yventanaTR,gateOI,plan/sizing/fill/protecciones/rechazos y causadesalida. Contadores mensuales totales y por dirección, particiónexclusiva y flags simultáneos; no sumar flags como trades distintos.
Muestra probablemente menor queH1; ausencia de30trades no justifica ampliar patrón/direcciones/ventanas tras verla. SMA120 retrasada puede mantener régimen tras una reversión. La reanudación de una barra puede ser ruido y6ATR de objetivo puede ser infrecuente dentro72h. Medir frecuencias,exposición,fees,funding yconcentración sin escoger una salida alternativa ex-post.
Screening propuesto por root:[2020-09-01,2024-01-01), seis configuraciones globales entre sectores. Este documento aporta sólo dos. Root congelará gates/selector/presupuesto globales antes de ejecutar; no se propone una grilla adicional ni se reutilizan slotsV2. Sólo elegibles con shortlist congelada podrán abrir WF2024–2025 conforme al nuevo protocolo.
2024–2025 todavía cerrado a esta propuesta,2026 cerrado. Sin código,backtests,consultas económicas nuevas,env/DB/CLIresearch,instalaciones,reinicio,Pi,live/paper ocommit/push en esta entrega.
