# Scale-out50%a2R + runner — prueba técnica/económica inicial
Dashboard: http://localhost:9200/#/backtest/0c6cfad7-c5da-465d-a45e-7009d284a1ec
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Hipótesis/protocolo
ORCH_SCALE_OUT_HALF_2R_PROTOCOL_20261018.md previo alrun. ÚNICOcontrol50%a2R,qtyrounddownresearchlot,runnercon gestiónoriginal. No se barrieronporcentaje/R. Inicialstop2ATR,riesgo3%/8%,asignacióninversoATR,gross4.4x,margen90%,shortBTCidénticos. Longs3activosBTC/PAXG/SPY,longLIMITretestshortSTOP. Cuenta10k/5xaislado/fee0.00045cadafillinclusoLIMIT. Normal replay,warmup240,2020-10-15→2025-12-31exclusivo.2026reservado.
## Métricas comunicadas por motor
222trades97L125S,net20028.773774USDT(+200.287737%),saldo30028.773774,fees3986.159163USDT,CAGR23.478932%,DD−9.958176%,Sharpe1.357390,Calmar2.357754. WRlong45.36%,WRshort55.20%;0posicionesterminales.
ReferenciaCAGR28.829387/DD−14.890506/Sharpe1.316428/Calmar1.936092,net27461.463375. Menorretorno ymenorDD enscale-out,no implica regularidadaprobada.
## Validación técnica completada
FuenteMCPguardada releídaigual. Todas las aserciones deventanacompleta finalizaron sinerrores:
- TPparcial0<qty<initial yqtyreal==qtyplaneado.
- Unaúnicareducción porlong;no rearmadoTP.
- Qtyremanente+qtyparcial==qtyinicial.
- STOPreasignadoalmismoprecio conqtyremanente enon_reduced_position.
- afterverificaposiciónremanente ysumqtySTOPdeclarados.
- on_closeverificaparcial+qtyúltimofill==qtyinicial,sinsobrecierre/flip.
NoBEextraal2R: umbraloriginal2.25Rconservado. Trailingoriginaloperaantes/después de reducción. Losassertsde STOPdeclarado verificanintención;ejecucionesrealesyfeesrequierenelreplayV4independiente. No afirmancertificacióndeexchangelive.
## Pendiente obligatorio antes de interpretación MTM
AuditorV3rechazaparciales; NO usar porporcentajes. Root implementaV4 porórdenes ydebe reconciliarporfill fees,PNL,saldos,posiciónyparcialescrossmonth. Ningún VWAPfinalpuedeatribuirla salida tempranaalmes final.
CalendarioMTMmenses/trimestres,contribuciones/tails/concentraciónycostes permanecenpendientes. Candidata investigativa, noaprobada, no elegidaaúncontraobjetivo65–70%/80%.Noabrir2026.
## Setup/limitaciones
SinerrorAPI/MCPnimissingcandles. No se modificaronframework/config/live. SPYproxyBIDyPAXGspot/nativeparity/funding/slippage/colas siguenpendientes. La mecánica parcial sigue ejemplosMCPjesse://strategy_examples Ej2, peroqtyresearchrequiereverificaciónnativaanteslive.
