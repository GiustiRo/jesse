# Tanda P: K1001/N204, cuentas BTC individuales

Dos recetas legacy completas medidas en cuentas BTC individuales, sin candidata. Se resuelve la brecha entre contribuciones de cartera y retorno de una cuenta individual; no se atribuyen a BTC los CAGR de las carteras. K1001 yN204 fallanCAGR30%,M65activosyQ80, aun conPF/DD/mediana/concentración favorables. K37/58=63.7931% no65%; ambos15/20Q=75% no80%. No promoverporcercanía ni subirriesgo,retirarreserva,eliminarcomponentes o cambiarplazos para rescatar.

|Cuenta|N|CAGR neto|PF|DD M1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores meses|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4)|192|26.8148%|1.8489|16.5039%|37/58|15/20|1.1820%|15497.8805|1.4994|
|[N204](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61)|222|25.0358%|1.6530|17.8990%|36/60|15/20|1.1131%|13008.2229|1.3792|

## Receta y adaptaciones declaradas

LONG_RUNNER LIMITretsteoDonchian26/EMA20,80/ADX26/RSI52–76,SL2ATRta,BE2.25R/trail4.2ATRconajustesheredados,sinTP/plazo; CORE_SHORT STOPconmacroEMA120ascendente/RSI3<=20,TP1.5ATR,72h; suplementoN204MARKETcohorteVWAP yfallodeavance2R/48h,K1001añadeeficiencia<=1/3ySTOPestructural. Prioridadlong→shortoriginal→suplemento. Setupavanzaocupado; LIMIT/STOPpendientehasta4h,gestiónsólo4h, fill/proteccionesM1.

AislarBTCretira cuotaATRotrasrutas→100%BTC; cuenta/cantidades/funding/M1yúltimodía2025 incluido cambian frente a las anclas de cartera. No réplica idéntica ni ablationcausal de unasola diferencia. Capital10k,riesgo2%stop+fees+reserva.001desizing,6%capadmisiónnovinculanteconunaposición,aislado3x,margen90%confees,lot.001. Reserva.001REDUCEqty,no débito/PnL/slippage aplicado. No variar reserva/lote/capdespués. Feereal.00045porlado taker+fundinghistóricofrozenBTCaplicado/verificado,snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados,slippage0. Neto sólo después de costosefectivamentemodelados. BTC-USDTBinancePerpetualFutures,[2020-10-15,2026-01-01)UTCdesarrolloobservado;noeconomía2026nueva.

## Ledger y auditoría
[BtcResearchR16LegacyK1001m](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4):brutoprecio28115.585676,fees3176.475399,funding-410.421286,neto24528.688991(245.2869%),capitalfinal34528.688991USDT. DDdiarioframework-15.5129% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10650.419092195123},"CORE_SHORT":{"fills":116,"closes":116,"net":4686.29849188876},"SUPPLEMENT":{"fills":45,"closes":45,"net":9191.971406577974}}. Planes313,fills192,cancelaciones121,eventossuplemento82.

[BtcResearchR16LegacyN2041m](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61):brutoprecio25902.273489,fees3518.650568,funding-308.065527,neto22075.557394(220.7556%),capitalfinal32075.557394USDT. DDdiarioframework-16.7707% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10594.666156313726},"CORE_SHORT":{"fills":113,"closes":113,"net":4342.279629642518},"SUPPLEMENT":{"fills":78,"closes":78,"net":7138.611607679111}}. Planes318,fills222,cancelaciones96,eventossuplemento96.

Auditoría0aceae731d224b0585f7fe7ff6ac3d47 succeeded:414registrosentrepolíticasalternativas,noindependientes. Bruto−fees+funding=PNLsum=equityfinal−10000 a<1e−6USDT; fundingconciliado; suma ledger3orígenesconciliadaN/closes/neto. Todoslosorígenespositivosdentrodeambascuentas,noderivartresestrategiasindependientesniquitarelorigenpormétricaretrospectiva. Posicionesfinales0,PRETERMINALno pendiente económicofinal.

Telemetríaexactasegúnconvención:2.741.760marcasM1,63intervalosmensuales/62completos,20Q,invalid0; equitywallet+PnLabierto,DDM1+fillsnoextremosintraminuto; fronterasmensualesUTCpostfunding/predecisiónporfase. Mediana incluyecalendarioinactivo,M65sólomesescompletosactivos. History4hmin241/max11664enambas,compatibleconretencióndecrecimiento. No prueba deigualdadnuméricaconcarteras quenotienenlasmismascondiciones.

## Verificación técnica e intentos

Fuentespadres/R11/R10inmutables;CODES/readbacks/hashesenrecibotécnico. PrimercheckfallóSyntaxErrorenexpresiónVWAPnuevaantesdepruebas,corregido/registado; segundo5962asercionespassconmétodospadreembebidos/featuresartificiales. Checksnoimportanestrategiasrealesnidataobservadanibrokerreal. Auditoríaframeworkreadonlydelcheckoutbindmontado,resguardadaMCP,detectóque docsresumidassimplificaban cancelación: _checkcancela ypuede reevaluarentradasenmismociclo. LazyplanmemoizadoahorapreservarearmadopostTTL/margenliberado,perono tras cierreposición. Replayprocesaminutoexpiryantescancel; verificadaspolíticasdehistoria/taATRscalarúltimas240/EMAseqhistoriacompleta. No editarframework/config ni leerestrategiasporfilesystem,ningúnDockerrestart. Revisiónindependientefinalconforme ymanifiestodeformulariosrealesantesmotores.

Doseconómicascompletadas,0fallos/reemplazos/backteststécnicos. Doschecksprogramáticos,1fallotécnicoy1pass,noeconomíainterna. Desde r9:30económicascompletadas, no30muestrasindependientes;bloqueV1–V6209conservadoseparado. Ppresupuestocerrado,sin nuevosvecinos/ablaciones decomponentes,risk,prioridad,gestiónoplazos. Sinestrés,nuevos2026,live/paper/Pi,instalaciones,reinicios,configglobal. La autorización de contingenciaDockerlocal sólo aplica sifallaMCPdenuevo.

Control de repetición adicional:CROSS_P yaBTCindividual2%/3x/fundingconcapnocional1x,cupo1entrada/día,screen2020-09a2024-01CAGR21.3292%. No estuvo sinfunding ni sinriesgoactual;no nueva economía CROSS ni retirarcappararescatar. No selecciónnuevadefinalistasV5cerradas.

Continuidad:otra pregunta material,protocolo ypresupuestoantesdenuevaprueba;actualmente se contrasta inventario para residualBTC/ETHcontrarian vscontrolprecioBTC, sin estrategias/jobsaprobadosaún. Ningunapromoción ni autorizaciónoperativa/estrés.

## Años y ventanas móviles, descripción

Calculados aritméticamente desde los63intervalos R11 completos delreciboMCP (62mesescompletos para este resumen), usando productos de retornos M1/frontera declarada. Se excluye2020 incompleto de añosanuales;51ventanas12meses solapadas no son independientes ni OOS. No cambian gates/veredictos ni se usan para nuevos filtros.

K1001: añoscompletos={"2021":37.754599469109664,"2022":30.137400778791168,"2023":46.386546735302446,"2024":11.405045108153988,"2025":13.967847464097982};rolling12={"N":51,"positive":46,"min":{"start":"2023-07","finish":"2024-06","return_pct":-7.806699187854072},"max":{"start":"2022-07","finish":"2023-06","return_pct":67.37900185704851}}.

N204: añoscompletos={"2021":37.72403744564716,"2022":27.511781442433957,"2023":42.26544154555545,"2024":10.88869735715441,"2025":11.047192591105404};rolling12={"N":51,"positive":46,"min":{"start":"2023-08","finish":"2024-07","return_pct":-9.240395861709516},"max":{"start":"2022-03","finish":"2023-02","return_pct":69.32315922926566}}.
