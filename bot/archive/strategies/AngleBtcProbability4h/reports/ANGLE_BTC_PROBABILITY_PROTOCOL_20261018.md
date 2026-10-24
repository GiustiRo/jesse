# Protocolo previo: probabilidad secuencial y expectativa monetaria BTC4h

Estado: implementación para revisión, SIN backtest lanzado. Una sola receta, sin rejilla ni modelo preentrenado. Prefijo propioAngleBtcProbability; referencia original intacta y2026reservado.

## Hipótesis y diferencia limitada
Cuatro estados, definidos por el signo de los dos últimos retornos4h, podrían presentar expectativas de continuación/reversión cambiantes. La estrategia no fija de antemano el sentido rentable: aprende sólo de resultados pasados y puede abstenerse. No agrega información externa ni una teoría nueva; podría ser otra expresión estadística de momentum/reversión ya estudiados. Si no demuestra ventaja neta, no renombrarla como mecanismo independiente ni complicarla conHMM/redes.

Inventario leído porMCP: ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md, registro global y progreso canónico. Trend/medias/breakout/retest/rangos/compresión/dips/gestión/rotación y pares ya están intensamente explorados. Esta prueba cambia la regla de decisión hacia estimación secuencial parsimoniosa, no la fuente informativa.

## Observaciones, maduración y ausencia de fuga
Antes de cada decisión4h se madura exclusivamente la etiqueta de la decisión anterior. Se exigen240M1cerradas ycontiguas con timestamps exactos desde el anteriorcierre hasta el actual; ninguna vela futura, interpolación ni relleno de huecos. Etiqueta madura sólo a+4h; si falta cobertura, no se añade.

Para long y short hipotéticos se calcula retornoR de una entradaMARKET al cierre anterior,stopemergencia3ATR conocido entonces y salida al cierre siguiente si no se tocóstop. PrimercruceM1: apertura adversa que salta stop ejecuta aesaapertura; en otro caso, primerlow/high que toca ejecuta alstop. No depende del ordenhigh/low de toda4h. Es una reconstrucción de etiquetas conM1, NO una garantía general de paridad con el motor bajo todas sus convenciones. No se reportan etiquetas como trades reales.

Cada etiqueta resta ambasfeesBASE0.00045porlado yhaircut10bpsRT; todo dividido por distancia de stop. Costesde señal quedanfijos para posteriores controles de fee efectiva. Haircut ybuffer de sizing NO son slippage efectivamente simulado.

## Tamaño, shrinkage y decisión
Ventana rolling1080etiquetas aceptadas, aproximadamente180días; se acumula ENRUNTIME. Warmup240sólo apoyaATR; no se usa para cargar una tabla futura ni completar1080. Todo startupcash se conserva en métricas y meses/trimestres; no recortar la ventana de evaluación.

Para cada4estados y2direcciones se mantienen n,sumaR,sumaR²,wins. Exigir almenos80observaciones delestado y ventana1080llena. Prior20casos balanceados: mediaR0,momento2=1R²,winrate50%. Media=(sumR)/(n+20);var=(sumR²+20)/(n+20)−media²;SE=sqrt(var/(n+20)). Entrar sólo si media−1SE>0; escoger la dirección conmayor score o mantenercash. La probabilidad(wins+10)/(n+20) se conserva como diagnóstico,no gate51%.

SE es una heurística de prudencia, NO intervalo válido de confirmación: hay dependencia temporal, cambio de régimen y selección acumulada. El sistema no se presenta como probabilidad calibrada sin evaluación adicional. NoKelly ni riesgo ajustado por probabilidad.

## Órdenes y límites
Una rutaBTC-USDT4h,BinancePerpetual,normal,benchmark=True,2020-10-15→2025-12-31exclusivo;10000USDT,5xaislado,fee0.00045porlado,warmup240. EntradasMARKET;3ATRstopfijo;sinTP/trail/parciales/piramidado. Salida al siguiente cierre4h si sobrevive. El motor no vuelve a entrar en el mismo callback que liquida una posición; no se fuerzan reaperturas ni transacciones fuera del ciclo.

Riesgo1%de min(wallet,equity), incluyendo fees reales y10bpsreserve; por debajo de3%/trade y8%global. Gross<=4.4x y90%de margenleverageddisponible. Cantidad variable redondeada haciaabajo. Lot/minnotional nativo, funding eimpacto no están validados para live.

## Falsación y evaluación
Primera corrida única sin cambiar1080/80/20/1SE/3ATR después. Cero operaciones es resultado admisible: evidencia insuficiente, no razón para relajar gates. Neto<=0,DD>25%,expectativa eliminada porcostes o muestraescasa impiden promover. Si promete, ROOT decidirá un control sinestados y vecindario acotado; no está autorizado aún.

Se revisarán PnLneto/fees/númerooperaciones, long/short,concentración,años2020–2025 ycalendarioMTMcon startupcash íntegro. No llamar2024–2025OOSlimpio ni confundir entrenamiento causal de cada predicción con independencia de la investigación completa. Las metas65–70%mesesactivos/80%trimestres se mantienen; reportar también todoslosmeses/períodoscompletos.

Implementación sóloMCP/Strategy/NumPy/stdlib, sin scripts nuevos, red, archivos, randomness, framework, instalaciones, live/Pi o datos externos. Revisar fuente conROOT ANTES de corrida y coordinar máximo2simultáneas.


## Revisión técnica ex ante anterior al primer run

ROOT pidió añadir distancia/entry<=0.75/leverage tanto al armar pendinglabels como al plan de entrada; assert de coherencia también al fill. A5x equivale aproximadamente15%,25% de colchón respecto a distancia ideal1/L, NO cálculo exacto de liquidación con mantenimiento/fees. Es un guard de seguridad fijo, no parámetro de optimización ni ajuste visto el resultado.

Logs self.log al cambiar año y before_terminate resumen contadores ACUMULADOS: labels_total,missing_labels,windowlen,counts4estados,skipwindow/estado/edge/seguridad/cantidad yseñaleslong/short. Son diagnósticos, no resultados económicos inventados. Si hay ocho intentos de maduración fallidos SIN ninguna etiqueta válida, se aborta con error descriptivo de coberturaM1/clock. Una eventual corrida0trades sólo es interpretable con aprendizaje funcional; huecos aislados después de observaciones válidas no producen ese aborto.

Sin cambio a1080/80/20/1SE/3ATR, fees,señales probabilísticas ni riesgo. Gross4.4x es techo de admisión, no garantía continua después de moverse el precio. Esta primera corrida es standaloneBTC; integración con otras patas exige ledgercompartido explícito.
