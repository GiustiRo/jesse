# K1001: diagnóstico primero y dos escenarios originales con cuota1%

[Long original](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c) y [libro short original](http://localhost:9200/#/backtest/aa79608f-70fd-42aa-8047-ed6bc31133c2). Ambas ejecuciones terminaron y conciliaron. Ninguna alcanza el objetivo económico. El diagnóstico de192 trades del [K1001 original](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4) se completó ANTES de diseñar estos escenarios.

## Qué se midió

Dos mundos alternativos, cada uno con cuenta BTC total10.000USDT y sólo su cuota1% activa; la otra cuota queda inactiva. Se conservan señales, indicadores, latch, prioridad core→suplemento, órdenes, stops, targets y gestión originales. Único cambio económico: grupo permitido y legacy_plan con.5balance/.5available_margin. No subcuenta5.000, no2%por derivada ni redistribución.

BTC-USDT Binance Perpetual Futures, UTC[2020-10-15,2026-01-01),desarrollo ya observado, cuota1%,3xaislado,fee.00045por lado y funding histórico aplicado/verificado con proxies explícitos. Slippage modelado0, reserva.001 sólo sizing. No estrés ni nueva economía2026. No son posiciones simultáneas ni simulación conjunta; NO sumar curvas/CAGR/netos como una cuenta financiada.

|Escenario|N|CAGR neto sobre10.000|PF neto USDT|DD M1+fills|Meses activos positivos|Trimestres positivos|Mediana mes calendario|
|---|---:|---:|---:|---:|---:|---:|---:|
|LONG_ONLY|31|6.7079%|3.5520|8.4730%|13/28=46.43%|8/20=40%|0%|
|SHORT_BOOK|172|5.9247%|1.5277|8.6080%|38/58=65.52%|16/20=80%|0.5191%|

Long neto4030.903490,final14030.903490; short neto3501.965680,final13501.965680. Cada importe pertenece a SU trayectoria alternativa. Neto aritmético sin los dos mejores meses:1397.792214 y2735.482375, respectivamente. El long falla CAGR/M65/Q80/mediana y N100; su muestra es además limitada. El short supera todas las puertas prefijadas salvo CAGR30%. No es candidata por cercanía, PF, regularidad o menor DD. N100 es mínimo operativo preliminar, no potencia ni confianza estadística.

## Preguntas respondidas

**¿Separarlos produce más fills long?** En esta ejecución, no: las31 entradas long coinciden exactamente por origen+signal_at+opened_at con el original; las31 salidas coinciden en tiempo y precio. Diferencia máxima Rneto común1.42e−13. No aparecieron fills long adicionales al retirar los shorts bajo estas reglas/ventana; esto no reconstruye todos los candidatos raw bloqueados. No es una conclusión universal sobre otro diseño.

**¿Qué cambia en short?** Hay158 entradas originales comunes,14 nuevas y3 originales ausentes:172 frente a161 shorts del Koriginal. Las158 salidas comunes conservan tiempo/precio y Rneto, diferencia máxima2.87e−14. La secuencia y disponibilidad importan: no es simplemente añadir11 trades a una lista fija. Los14 nuevos tuvieron neto descriptivo−112.414048 a los tamaños de esta trayectoria; no es efecto causal incremental de cartera ni prueba significativa sobre señales. No rescatar excluyéndolos.

**¿Cada pieza muestra un perfil distinto?** Sí en estos escenarios, sin acreditar diversificación conjunta: long muestra payoff asimétrico y pocas operaciones/meses positivos; short tiene regularidad cercana a las puertas pero una ventaja por operación modesta. CORE_SHORT124trades,net1115.043286,PF1.2075,mediaRneto.08350; SUPPLEMENT48trades,net2386.922394,PF2.8900,mediaRneto.50779. Conservar todo el libro short; no quitar core tras atribución.

**¿El mayor PF long significa mejor señal?** No: el PF enUSDT subió respecto al original pese a ser exactamente las mismas31 trayectorias de precio yRneto. Cambió su ponderación monetaria por cuota/capitalización propia. Las mejoras de PF monetario no son por sí solas mejoras de señal.

**¿Las pérdidas long nunca avanzan favorablemente?** Los18 perdedores tuvieron mediana del máximo M1+fill observado.9205R y medianaRneto−.9817. Los13ganadores,medianas máximo5.9106R yRneto3.4013. Hay devolución observada, pero no demuestra salida mejor: estos máximos se conocen después, no son precios ejecutables, y el trailing opera con cierres4h. No diseñar un target desde los máximos ni llamar al trace MFE/MAE intraminuto. Las salidas originales censuran toda trayectoria posterior.

## Años completos de cada cuenta

|Año|LONG_ONLY|SHORT_BOOK|
|---|---:|---:|
|2021|16.0912%|−0.3930%|
|2022|−1.4756%|16.2705%|
|2023|13.9989%|8.8734%|
|2024|3.1153%|5.5485%|
|2025|−0.0899%|5.0129%|

Son retornos MTM de cuentas alternativas, derivados de fronteras mensualesR11; no cohortes de trades por año. No sumarlos ni escalar cuota para fabricar objetivo30%.

## Auditoría y límites técnicos

203operaciones entre escenarios alternativos,203OPEN/CLOSE/traces únicos,658+520pagos de funding completos. Gross−fees+funding=PNL=equityfinal−10.000 a<1e−6USDT en cada cuenta.31campos funding ausentes(1long/30short) se comprobaron sin pagos por sus ledgers completos, nunca se imputaron ceros por ausencia. Formulario/fuentes/hashes congelados antes de motores y68outcomes sintéticosPASS en primer job. Dos motores económicos nuevos,0fallos/reemplazos/backtests técnicos.50IDs económicos ejecutados y completados desde r9, sin independencia implícita ni sumar con V1–V6.

R11 validó2.741.760marcasM1,63intervalos mensuales/62completos,20trimestres,invalid_windows0; DD es M1+fills, no todos los extremos intraminuto. Trazas203/203 completas, geometría/fills/netos unidos1:1; fuentes/planes/riesgo1% y ledgers conciliados. Comparaciones monetarias contra Koriginal2% no son ablation causal de ocupación porque cuota/capitalización también cambian.

El auditor mecánicoV1 pasólong y falló al parsear una línea K1001_QUOTA_STATSshort: MCP recorta líneas a2000caracteres+[line cut]. Línea original y fallo conservados. V2 recupera sólo prefijo íntegro stage/group/sources/open_years etiquetado PARCIAL; close_years se reconstruye de ejecuciones, no se presenta como campo nativo recuperado. Ausencia de errores diagnósticos inferida bajo logging completo/código congelado que emite primera ocurrencia; tracefinalcerrado inferido de cobertura1:1 y métricaopen0. Nada se inventó del sufijo perdido. No rerun económico por telemetría redundante.

El archivo metadata del análisis incluía pagos completos y superaba el transporte del lector: no se pidió ni parseó truncado. Se usaron los12exports acotados completos de trades y summaries/ledgersMCP. Recibos/fuentes/códigosV1/V2/resultados completos guardados y leídos íntegros.

## Decisión

Dos escenarios cerrados sin candidata. La separación por sí sola no resolvió el objetivo; no modificar cuota ni criterios para aprobar. Original K1001 queda referencia, no ganadora operativa. Una combinación conjunta sigue sin probarse.

Continuar autónomamente con otra pregunta material sustentada en estos datos y contrastada con antecedentes: distinguir la escasez de follow-through de una supuesta mala captura, y conservar el bloque creativo sobre selección de fills. El siguiente diagnóstico/protocolo debe cambiar una decisión real; no reabrir filtrosR14, optimizar extremos retrospectivos ni repetir cuentas por nombre.

## Descriptivos posteriores de periodo y embudo existente

Cohortes por AÑO DE ENTRADA,2021–2023 frente a2024–2025;2020incompleto excluido de esta comparación. No son retornos anuales MTM ni prueba causal, y los tamaños son pequeños. LongN13/14: mediaRneto2.3759→.2422,mediana máximoM1+fill2.6251→1.3271R,mediana devolución1.7672→1.5488R. Menor recorrido favorable observado acompaña el deterioro; no se observa una mayor devolución mediana reciente. No justificar un parche del trailing desde la caída global.

SuplementoN24/23: mediaRneto.8044→.2641,máximo observado mediano1.4191→.5830R,devoluciónmediana.1916→.4771R; señal mixta entre recorrido y captura observados. CoreN73/43: mediaRneto.09495→.14080,máximomediano.7082→.7296R,devoluciónmediana≈0ambos; no todo componente empeoró. Estas cohortes siguen censuradas por las salidas originales; no identifican causalidad ni la ventaja de otra entrada/salida.

Embudo de órdenes long ADMITIDAS en el escenario existente:45planes,31fills,14cancelaciones. No son todas las señales raw, ni14episodios independientes. Dos cancelaciones están separadas exactamente por el TTL4h; la agrupación cronológica no es muestra estadística.45tampoco es techo de trades de otra política, que cambiaría ocupación. Los contadores YA están disponibles y no justifican por sí solos otro replay. La siguiente decisión de valor de información contrasta una medición de trayectorias con una posible comparación económica directa, revisando antecedentes antes de definir un motor.

Recibos y crítica independiente de cierre documentan alcance: revisión nativa de summaries/terminales y códigos, sin segunda auditoría independiente de203filas/1178pagos. El campo estructurado sources.*.observed_max_R del JSON se define como MEDIANA de máximos por trade; no máximo global.
