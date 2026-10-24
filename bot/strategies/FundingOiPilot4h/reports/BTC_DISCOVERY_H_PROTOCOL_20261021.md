# Tanda H: mechas de rechazo frente a localización del cierre

Registro previo a resultadosH. Pregunta material: ¿el rechazo reflejado por mechas repetidas aporta más que la posición de los cierres dentro del rango? Dos políticas, dos corridas económicas continuas, hasta dos reemplazos exclusivamente técnicos documentados; sin vecinos/optimización, máximo dos motores y un análisis propio. No necesita resultadoGpara fijar reglas.

## Antecedentes y atribución
Transferencia explícita de R40PaxgWickBalance4h aBTC, negativoenPAXG yR40excluyóBTC. Bloque8velas, balance.20 y desplazamiento<=ATRprebloque son elecciones heredadas, no calibraciónBTC. N204E404 mide presión de cierres ponderada porvolumen/cohorteVWAP como suplemento short. Esta comparación BTCsimétrica sinvolumen/cohorte separa algebraicamente cuerpo ymecha: lowerwick−upperwick=O+C−H−L; closepressure=2C−H−L=wickbalance+(C−O). No sonflujo real/orderbook ni se infiere orden intrabar de OHLC. No es etiqueta nueva para mismo N204 ni evidencia independiente por usar dos señales relacionadas.

ATR original R40 usa ta.atr Wilder; aquí se adapta explícitamente a ATR14simple del contrato BTC. Esta diferencia impide atribuir cambios económicos sólo al activo o sólo a las mechas.

## Reglas
En T4h usar23OHLCcerrados consecutivos:15 previos para ATR14simple excluyendo las últimas8velas. Bloqueúltimas8. Denominador=sum(H−L);<=0=>estado0. WICK balance=sum(O+C−H−L)/denom. CLOSEcontrol balance=sum(2C−H−L)/denom. Estado1si>=.20,−1si<=−.20,otro0. Se actualiza estado en cada cierre antes de admisión: disparar sólo transición a estado no nulo distinto, aun si evento ocupado/no cumple desplazamiento. Exigirabs(Cactual−Cantes8)<=ATRprevio. No retrasar cola ni entrar alpersistir estado después de filtro rechazado. Dirección=estado en ambas, ninguna selección long/shortposthoc.

MARKETalclosecerrado, stop2ATRprevio congelado, TP3ATRprevio=1.5R, vencimiento48h en cierres4h. Protección heredada de esta hipótesis y común a ambos controles; diferente del2RdeF explícitamente, no rescate después dePnL. Una posición sinpirámides ysinreentradaalmismocierrede salida. Sizing2%feeaware,90%margen,floor8helpersR10; gaps/funding pueden exceder riesgo previsto.

## Contrato
BTC-USDT Binance Perpetual Futures, ruta1m ydatos4h,warmup2404h;[2020-10-15,2026-01-01)UTCdesarrollo observado.10k,2%portrade/6%agregado/3xaislado,fee.00045porlado,fundinghistóricoON/aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 conproxiesdeclarados;slippage0. Sinestres/variantesriesgo,nuevaeconomía2026,ML,live/paper/Pi/configglobal.

MediciónR11wallet+PnLabiertocadaM1yfill;fronteras00:00UTCpostfunding/predecisión,convenciónporfase,noeventgroupingestrictopormes. DD M1+eventosnoextremotick. Gatesr9:CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,medianacalendario>0incluyendoinactivos,netoquitando2mejoresmeses>0,N>=100preliminarsinconfianzaestadísticapornúmero. Aspiraciones40–50%+/M70. Evaluarcadapolíticapor separado,ganaralcontrolnobasta. NO_CUMPLEsi falla puerta económica,INCONCLUSAsifaltamedición/muestraconeconomíafavorable. Nooperaciónautorizadaporpasarbase,estresrequiereacuerdo.

ChecksAST,identidadalgebraica,mechaespejo,cuerpoaislado,cero rango,desplazamiento/ATRprevio,transiciónconsumida,ventanascausalesysizing antesde economía;readbackhash/configenmanifiesto. Auditoríacompleta posteriorPNLtrade/bruto−fees+funding/equityfinal a1e−6 ymeses/M1/fronteras. Guardartodaslaspruebas/descartes,reportesMCP/Hubíndiceúltimo. Si falla,cerrarpresupuesto ypasarautónomamenteaotra pregunta material; noafinarbloque8/.20/protección.
