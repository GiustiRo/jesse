# BTC discovery C — acumulación de sorpresas y volumen sin progreso
Registro: 2026-10-21 17:59:19 UTC. Antes de implementación y resultados C. Permiso autónomo vigente del usuario, reiterado para avanzar sin aprobación rutinaria. Presupuesto: dos recetas, dos corridas económicas continuas; máximo dos reemplazos sólo por error técnico. No rejilla ni optimización. Máximo dos motores globales; un análisis propio a la vez.

## Pregunta y control de repetición
C1 CUSUM: transferir a BTC la señal exacta de R40PaxgCusumDrift4h, sin inventar metodología. Ese antecedente PAXG fue negativo y R40 excluía BTC. Sobre62cierres4h,61logretornos: normalizar último con media/std muestral(ddof1) de60previos; up=max(0,up+z−.25),down=max(0,down−z−.25);evento al>=4,resetambos;siamboscruzan,noentry. Sigma<=0/no finito/datos inválidos=>reset/sinentry. Consumo ocupado sin cola. Memoria por reset y magnitudes distinguen de Breadth R10,ER V6 y SMA V5. No modificar .25/4 después.
C2 VOLUME_WITHOUT_PROGRESS_ESCAPE: interpretación creativa de OHLCV, no flujo observado. A=barra anterior,B=actual,W=24anterioresaA. V_A>=2media(V_W)>0 y cuerpoA<=.25ATR14preA excluyendoA/B. SóloB:close>highA long,close<lowA short;si no,caduca. Ventana26barras consecutivas,volumenfinito>=0,media0invalida. Difiere V4Shock(desplazamiento grande/contrario inmediato),NR7(rangoestricto7sinvolumen),AngleCombinedBtcVolume(gatealsetup),N204presión(cohortesq). No reentrada por la mismaA ni cola posterior.

R10A/B cerradas sin candidata: no vecinos de signos, ni reversión posthoc de funding. No eliminar shorts por PnL. Una transferencia a otro activo no se presenta como descubrimiento universal ni como ausencia de antecedentes.

## Contrato fijo
BTC-USDT Binance Perpetual Futures; señal y gestión4h, entradas MARKET tras cierre, stop2ATR14simple(media14TR/15OHLC),TP2R,hold48h. Sin trailing/parciales/pirámides. Una posición,riesgo2%inclambosfees;agregado6% no vinculante conuna entrada2%. Reserva margen.90y3x,planfee-aware congelado R10;sin cap1x o cuota diaria extra. Ceros/gaps inválidos no se rellenan.
Cuenta10kporreceta,fee0.00045porlado(takerdescuento confirmado),slippage0modelado,ningúnestrés. FundingON snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571;4198marcasproxyen6576eventosdelsnapshotcompleto,detalledeusoreportado. No importación ni cambio global.
Ventana[2020-10-15,2026-01-01)UTC,warmup240delmayorTF4h. Desarrolloobservado,noOOS. Sin nueva economía2026;segundometodo no recupera ceguera.

## Reloj y medición mejorada
Nueva ruta1m como observador de equity, data_route4h para señales. before resetea dirección cadaM1,signal sóloT múltiplo4h,helper rechaza vela4hno cerrada/gaps yverifica últimoC4h==precioM1. Salida temporal sóloen4h,porloque observaciónM1no añade decisiones fuera delreloj. Protectiveorders siguen ejecuciónM1normal.
EquityBTC=wallet+position.pnl, sinmultiplicarPnLporleverage. No usar portfolio_value abierto en estecheckout: multiplicaotra vezleverage. R10lo usabasóloflat yno afecta susentradas.
DDmuestrado M1+muestrasenapertura/cierre:mayor resoluciónque motor diario,pero noextremosintraminuto. MarcarenbeforeM1 yhooks,porqueentradasMARKETse ejecutandespuésdeafter.
Guardar fronteras00:00UTC enbefore tras funding efectivo y antes de decisiones. Convención uniforme por fase: fundingjustoen00:00entraenelintervaloqueacaba; no afirmar atribución de cada evento por mes[a,b)estricto. Corte final exclusivo no paga fundingfinish; cierre final confee se sustituye enonclose posterior. Publicar fila mensual yresumen al terminar;onclosefinalactualizafrontera yreemite FINAL,que prevalece sobre PRETERMINAL. ActividadporposiciónM1/hooks,noporPnLdistintode0.
Resumencon62mesescompletos esperados(Nov2020–Dic2025),20trimestrescompletos(2021–25),2020Q4parcial aparte;no acreditarevidencia si faltanfronteras/cobertura. Distinciónencuts documentada, nocambio segúnrentabilidad.

## Gates y clasificación
CAGRnetobase>=30%,PF>=1.20,DDM1+eventos<=25%(objetivo20%informativo),Mpositivos/activos>=65%(aspiración70%),Qpositivoscompletos>=80%,medianaretornosmesescompletosinclceros>0,netoaritméticorestante sin2mejoresmeses>0. Sin promesa30%cada año;40–50%aspiración. N>=100convenciónoperativapreliminar,no cálculo de potencia. Inconclusa si puertaseconómicaspasanperofaltamuestra/medición. Fallopuertadecisiva=>NO_CUMPLE,aunqueotrosdatosfaltantes. Pasarbase=sólocandidatapreliminar,nooperar;estrésposteriorconacuerdousuario.

## Checks y cierre
Antes de correr: sintaxis/AST,helpercausalidadprefijosyfuturo,cusumreset,ceros,volumenpreA,consumoevento ynoidentidaddepropuestasprevias;telemetríafraccionesactividad/meses/completos,cierrepostfee,DDsinleverage. Fuentes/hash/config/snapshotantesdeejecutar.
Después: summary, trades/equitycompletos enrun_analysis;fundingapplied,dataset,balances,sumPNL,fees,funding yPF/CAGR. Telemetríafinaldeloslogscompletosdelbloquefinal,deduplicarstageFINAL,registroconservado. Toleranciacontable1e−6USDT,no ceroimputado. Sin pruebas de estrés,variantes de riesgo,ML/OI,nuevosdatos,reinicios,install,Pi,paper/live. No scriptsdeinvestigación.
Si ambos fallan, cerrar C y decidir otra pregunta material; cualquier iteración posterior tiene protocolo nuevo antes de resultados. Registro global de intentos, sin sumar como muestras independientes.
