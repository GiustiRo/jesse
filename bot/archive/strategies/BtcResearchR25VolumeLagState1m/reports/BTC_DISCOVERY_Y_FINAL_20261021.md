# BTC Discovery Y — cierre

Se probó si la orientación temporal de asociación entre volumen y magnitud del retorno añade utilidad direccional frente a conservar la dirección actual y la parte simétrica. Cada origen usa sus 25 observaciones estandarizadas propias: F relaciona volumen previo con amplitud posterior; R hace la relación inversa; S=F+R y D=F−R. STATE estima la media de retorno BTC24h por (signo del retorno actual, signoS, signoD); SYMMETRIC por los dos primeros signos, con la misma máscara válida y mínimo común de 20 casos en la celda actual.

Los 360 slots históricos tienen edades 6..365 barras4h; los targets ya son conocidos. Ventana392, padding row0 fuera de features/labels seleccionados pero incluido en validación OHLC. Normalización por origen, sin centros futuros; constantes exactas, ceros y aritmética no finita inválidos. No se identifica causalidad económica ni velocidad, orden agresor o información privada. La debilidad previa era que volumen/amplitud podrían describir volatilidad sin predecir media direccional.

Contrato UTC [2020-10-15,2026-01-01), 10.000 USDT,2%/6%/3x aislado, fee .00045 por lado y funding BTC histórico aplicado con marcas proxy; slippage modelado cero. R10 sizing, R11 observador y R12AR stop2ATR14simple actual/noTP/timeout24h intactos. Warmup400; entrada MARKET y ninguna variante de riesgo, costos o gestión. Desarrollo reutilizado, no OOS.

| Política | N | CAGR % | PF | DD M1 + fills % | Meses activos positivos | Trimestres positivos | Mediana mensual % | Neto sin dos mejores meses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [STATE](http://localhost:9200/#/backtest/16d1345d-9e3e-4e2a-8f4f-e7864b6296be) | 1528 | -18.239729 | 0.912874 | 75.827951 | 23/62 | 5/20 | -1.173295 | -9546.339273 |
| [SYMMETRIC](http://localhost:9200/#/backtest/d8af0558-41f9-4a44-914e-375e05cc0935) | 1485 | -14.008066 | 0.934406 | 68.519429 | 21/62 | 7/20 | -1.596012 | -8736.062444 |

STATE: bruto de precio 1087.924912, fees 6500.766997, funding -1089.458992, neto -6502.301077, capital final 3497.698923 USDT. Años completos (%): {"2021":-26.652567500166334,"2022":-6.20130211172687,"2023":-25.94393234060137,"2024":-34.40307131567783,"2025":-17.692461698139383}. Peor/mejor ventana12m -40.225525/5.255203%. Ventanas solapadas, descriptivas.

SYMMETRIC: bruto de precio 3582.565275, fees 7491.442595, funding -1540.165745, neto -5449.043065, capital final 4550.956935 USDT. Años completos (%): {"2021":-17.674327179228122,"2022":-5.112515906028037,"2023":-23.28427071553404,"2024":-9.642770680075374,"2025":-33.33548141954748}. Peor/mejor ventana12m -41.201899/13.297961%. Ventanas solapadas, descriptivas.

**Veredicto: NO_CUMPLE en ambas, ninguna candidata.** STATE empeora al control y falla todas las puertas económicas/regularidad/riesgo. Ambas sólo cumplen el conteo preliminar N100, que no acredita potencia ni compensa los fallos. El resultado bruto de precio no soporta los costos base reales modelados. No se retiran costos ni se escogen lados/celdas tras atribución.

## Diagnóstico de la explicación previa

El diagnóstico no seleccionó señales: capturó cada origen runtime válido antes de TRAIN/celda/hurdle/ocupación y maduró su label tras seis barras4h íntegras. Ambas políticas tienen exactamente los mismos acumuladores:11.421 orígenes registrados,11.416 maduros,0 censurados por gaps y5 censurados terminales;pending0. Se comprueba registered=matured+censuras+pending y suma de soportes=matured. Universo diagnóstico distinto del subconjunto elegible por TRAIN/celda20, temporalmente dependiente y observado en desarrollo.

Persistencia media s*y por D dentro de cada pareja(s,q), en puntos porcentuales de logretorno bruto:

| s | q | n D− | n D+ | Media D− % | Media D+ % | Diferencia D+−D− % |
|---:|---:|---:|---:|---:|---:|---:|
| -1 | -1 | 463 | 141 | -0.213749 | -0.525320 | -0.311570 |
| -1 | 1 | 3573 | 1382 | -0.078430 | -0.199234 | -0.120804 |
| 1 | -1 | 498 | 128 | 0.421517 | 0.469391 | 0.047875 |
| 1 | 1 | 3759 | 1472 | 0.015179 | 0.118959 | 0.103780 |

El signo anticipado aparece en las dos parejas con s positivo y se invierte en las dos con s negativo: evidencia mixta que no sostiene una explicación general de participación anticipatoria. No son cuatro ensayos independientes ni p-values; no se conservará sólo el lado favorable. Las medias de etiquetas tampoco son retornos de cuentas operables con stop/costos.

## Verificación y cierre

Hubo10.454 oportunidades con admisión válida común,968 con celda insuficiente y2 features actuales inválidas;11.424 fronteras4h en total. Cero ventanas de datos inválidas, desalineaciones o gaps registrados. Dos defectos de fuente se corrigieron ANTES del único fullcheck y de economía: validación de paridad de precio previa al diagnóstico, y guarda de constancia exacta para evitar que el redondeo de std(log2) crease una relación espuria con volumen constante. No se añade epsilon ni banda económica. Tres versiones y motivos preservados, no tres recetas económicas.

Probe numérico bdc2d3c5c0294a7cbc97ca925e8c4894 succeeded; fullcheck7a53cb54457e4d478247cfae6dd4155b passed13grupos en primer intento. Son dos análisis técnicos distintos, no backtests ni evidencia de utilidad;0 jobs técnicos fallidos. Fuentes finales revisadas por root e independiente, padres intactos. Recibo JSON estricto conserva code/jobs/artifacts, y el NaN del probe como texto exacto.

Auditoría financiera df9b42416f0544fbaef30f617f286c3b succeeded sobre snapshots completos: bruto−fees+funding=sumaPNL=capitalfinal−10000 y funding contra métrica, error<1e−6USDT. STATE flat usa PRETERMINAL ya final; SYMMETRIC usa FINAL después de liquidación y comisión terminal, aunque el contador raw preterminal de abiertos es1. Ambas tienen2.741.760 marcasM1,63 intervalos/62meses/20Q, contribuciones mensuales contiguas reconciliadas y equityfinal verificada. DDM1+fills no cubre todos extremos intraminuto; fronteras UTC postfunding/predecisión por fase. Funding aplicado, proxies2388/2348.

Presupuesto Y cerrado: dos económicas ejecutadas, cero errores o reemplazos económicos.46 IDs económicos desde r9, no muestras/hipótesis independientes; réplica AR/G de V identificada aparte. Cerrar sin vecinos25/360/20,lag,transformación,banda,signos,S/D,magnitud,horizonte,target,shrink,selección de lados/fases,riesgo o gestión. No transformar el target a volatilidad para rescatar esta pregunta. Sin nueva economía2026, imports, datasets, estrés, framework/global config o live/paper/Pi.

Z sobre funding acumulado se retiró documentalmente por equivalencia con carry/veto/reloj ya cerrados;0 economía. X proxy/calendario sigue HOLD. Continúa revisión documental AA de una pregunta económica distinta; sin motores autorizados por este cierre. Evidencia y diagnósticos completos en BTC_DISCOVERY_Y_ACCOUNTING_20261021.json, protocolo/manifiesto previos y TECHNICAL_RECEIPT/CODES. Ninguna promoción.
