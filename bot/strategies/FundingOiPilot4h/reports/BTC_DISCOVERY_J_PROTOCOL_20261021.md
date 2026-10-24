# Tanda J: información ETH para una operativa exclusivamente BTC

## Pregunta y antecedentes
¿Un movimiento excepcional de ETH confirma una entrada definida con BTC antes de que BTC tenga un movimiento igualmente excepcional? ETH se usa únicamente como dato: ninguna posición, asignación o funding ETH. Control BTC define su propia dirección; el tratamiento agrega información externa sin cambiar protección. Esto no es una cartera ni una demostración de causalidad ETH→BTC: shocks comunes y selección de oportunidades siguen siendo explicaciones posibles.

Antecedente OrchLateralRelativeShock1h: OLS96 retornos contemporáneos BTC~ETH, residual2h y confirmación1h, dos patas con beta. Cerrado negativo en ORCHESTRATION_ROUND5_RESULTS_20261018.md; no quitar una pata ni rescatar ese residual. R20PaxgSpyDelayed1h: fixingsNY,20retornosprevios,shockSPY2sigma/PAXGquiet.25sigma y entrada OPUESTA al líder; R20 excluyóBTC. La pregunta J cambia mecanismo a continuación cripto, datos1h continuos y control definido con BTC. No se declara una transferencia exacta o éxito del antecedente.

ETHM1 existente acreditado en ledgerORCH2020-08-15→2026-10-18. No inspeccionar velas antes: el motor valida el tramo2020–25. Ninguna lectura económica2026. No importar datos nuevos por este protocolo; si falta cobertura, registrar limitación y pasar a otra pregunta material sin fabricar datos ni sustituir feeds.

## Reglas previas a economía
Cada cierre1hUTC,26cierres1h completos/consecutivos de BTC yETH, sincronizados.25logretornos poractivo;24anteriores excluyendo actual para desviación muestral sigma(ddof1). Ambas sigma finitas>0 como validez común de datos.

Patrón BTC: abs(rBTC_actual)<=1*sigmaBTC_previa; no exige queBTCestéinmóvil, sólo que su paso sea ordinario frente al shockETH>=2sigma. Dirección=signo de suma de los seis retornos BTC ANTERIORES alactual (r[-7:-1]); suma0=>noentry. UmbralBTC1sigma se fija antes de resultadosJ como escala ordinaria, diferente del .25sigma del antecedentePAXG; no es vecino ensayado ni ajuste por señalesBTCobservadas.

BTC_CONTROL: operar ese patrón. ETH_CONFIRM: mismo patrón y además abs(rETH_actual)>=2*sigmaETH_previa y signoETHactual igual a direcciónBTC. Mismasventanas/historia, BTCdefine direcciónenambos; ninguna OLS/beta/residual ni posiciónopuestaETH. Cada cierre es evento nuevo, consumido siocupado, sincola ni reentradaalmismocierre de salida. No seleccionar lados después de veratribución. Las políticas son anidadas; capital y ocupación hacen que diferencia dePnL nosea un efecto causal aislado del filtro.

MARKETalcloseBTCcerrado; stop2ATR14simpleBTC1h actual congelado, TP2R, liquidación a6h desde opened_at en cierres1h. Horizonte6h expresa propagación próxima, fijado antes de resultado; no ampliar trasfracaso. ProtecciónintrabarM1; terminalmotorconfees. Una posiciónBTCsinpirámides. SizinghelperR10feeaware2%/margen90%/floor8;gaps/fundingpuedensuperarpérdidaprevista.

## Contrato y gates
BTC-USDT Binance Perpetual Futures ruta1m observador, datosBTC1h yETH1h;warmup2401h. [2020-10-15,2026-01-01)UTC, desarrolloampliamenteobservado,noOOS. 10k,2%portrade/6%agregado/3xaislado,fee.00045porlado,fundinghistóricoBTC ON/aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 conproxiesdeclarados;slippage0. Sinestres/variantesriesgo/2026nuevo/ML/live/paper/Pi/configglobal. Ningúnhorariobursátil: BTC yETHcontinuos24/7,noheredarfijaciónNY dePAXGSPY.

ObservadorR11 wallet+PnLabiertoM1yfills, fronteras00:00UTCpostfunding/predecisiónporfase, no agrupaciónestricta de eventos por mes; DDM1noextremotick. Gates:CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,mediana mensual calendario>0incluyendoinactivos,netoquitando2mejoresmeses>0,N100preliminarsinconfianzaporelconteo. Aspiraciones40–50%+/M70. Ganaralcontrolno basta; cada política porseparado. NO_CUMPLEsi falla economía;INCONCLUSAsieconomíafavorable yfaltamuestra/medición. Estrés sólo tras candidata/acuerdo,base noautoriza operar.

## Presupuesto y cierre
Dos corridas económicas continuas, una porpolítica; hastadosreemplazos sólo técnicos documentados, no porPnL. Máximo2motoresglobales y1análisispropio. AST/checks sintéticos de26cierres/24sigmaanteriores/6BTCprevios/sinactualendirección,espejo/control/filtroETH/ceros,asof/gaps/horas/sizing antes de economía;revisiónseparada yreadback/hash/configenmanifiesto. Auditoría posterior completa bruto−fees+funding=PNLsum=equityfinal−10k a1e−6;M1yfronteras/mesesreconciliados. ReportesMCP yHubíndiceúltimo. No barrer .25/.5/1/2sigmas, horas olookbacks alfallar;cerrar ycontinuar autónomamente otra pregunta material.
