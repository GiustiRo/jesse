# Tanda G: respuesta autorregresiva frente a deriva media

Registrado antes de resultados G. Pregunta: ¿la dependencia de retornos previos añade valor sobre el simple promedio reciente al pronosticar24h BTC? Dos políticas prefijadas: AR1 y deriva sola, dos corridas económicas continuas. No usar resultadoFpara escoger umbrales. Hasta dos reemplazos sólo técnicos documentados, máximo dos motores y un análisis propio. No vecinos, grilla ni selecciónporlado/año.

## Antecedentes y diferencia
Transferencia explícita R20PaxgARResponse4h aBTC, con comparador de media para atribuir contribución AR; R20 excluyóBTC y recetaPAXG fue negativa. BtcAdaptiveTrend2h y BtcRegimeBreakout1h usan filtros de tendencia, no pronósticoAR. V6EFFICIENCY net/path no es autocovarianza. KalmanE es nivel latente y reversión de innovación, no ajuste de dependencia entre retornos. Ni un nombre estadístico ni transferir activo acreditan ventaja; se prueba contra control y puertas absolutas. No machinelearning/HMM ni librerías nuevas.

## Reglas invariables
242 cierres4h consecutivos=>241logretornos r; entrenamiento240pares x=r[:-1],y=r[1:] ya observados al cerrarT. AR OLS: beta=mean((x−meanx)*(y−meany))/varx; intercept=meany−beta*meanx. Forecastdesde último retorno, seis iteraciones v=intercept+beta*v y suma(v), sin clipping de beta. La última y ya fue observada en T y no es etiqueta futura. Control DRIFT: beta0,intercept=mean(y),forecast6*mean(y). Mismaventana/mismas241observaciones/mismos240y; sólo difiere la contribución de dependencia.

EntradaMARKETdirecciónforecast siabs(forecast)>.0019, umbralheredadoR20fijo antesde resultados. Es un umbral de admisión de señal, no un costo extra aplicado ni estrés/slippage simulado. Varx<=0/no finito=>noentryenambaspolíticas. Sin filtro macro/volumen/funding/OI, sin selección de dirección por atribución. En cada cierre4h reevalúa; ocupado descarta sincola, alclose de salida no reentra. Stop2ATR14simple congelado, sinTP para conservar el horizonte del modelo; liquidar24hdesdefill en cierres4h. StopintrabarM1, terminalmotorconfees. Tamaño2%feeawaredeR10, margen90%,floor8, no pirámide.

## Contrato
BTC-USDT Binance Perpetual Futures, ruta1mM1observer y datos4h, [2020-10-15,2026-01-01)UTC desarrollo reutilizado. Warmup3004h porque requiere242cierres; cambio técnico de suficiencia no selección de resultados ni riesgo. 10k,2%/6%/3xaislado, fee.00045porlado, funding históricoON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 (proxiesmarcasdeclarados), slippage0. No estrés ni nuevas pruebas2026. Una posición; futurosgaps/fundingpuedensuperarriesgoprevisto.

ObservaciónR11wallet+PnLabierto porM1yfill;fronterasUTCpostfunding/predecisión, convenciónporfase, no agrupación estricta deeventospormes; DD M1+eventos no extremosintraminuto.62mesescompletos/20Qincluyendoinactivosenmediana.

## Gates y cierre
CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,medianacalendario>0,netoaritméticoquitando2mejoresmeses>0,N>=100preliminar sinconfianzaporelconteo. Aspiraciones40–50%+yM70. Cada política debe cumplirpor sí misma; ganaralcontrolno basta. Sinpromociónoperativa niestresautomático.

AST, OLSsyntético AR exacto,controlmedia, pronósticorecursivo/seisiteraciones, varcero/causalidad/ventanas y source/readback/hash/config antesde economía. Auditoría posterior completa bruto−fees+funding=PNLsum=equityfinal−10k a1e−6, equityM1/cobertura/meses. Guardar fallos/reportesysubirHubíndiceúltimo. Si falla, cerrar estasrecetas ybuscarotra pregunta, no barrerbetas/ventanas/hurdles. Autonomía vigente hasta objetivo con límitesr9.
