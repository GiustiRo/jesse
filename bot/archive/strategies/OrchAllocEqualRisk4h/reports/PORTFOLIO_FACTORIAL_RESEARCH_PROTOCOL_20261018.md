# Propuesta de arquitectura y presupuesto: comparación factorial de cartera
Fecha: 2026-10-18. Estado: DISEÑO PARA DECISIÓN DE ROOT. No código, drafts, backtests, jobs, datos externos ni cambios de framework. El usuario autorizó investigar BTC/PAXG/SPY con las velas existentes; BTC permanece inicialmente como ancla sin nuevas entradas.

## Diagnóstico que motiva el contraste

Se releyeron el inventario global, el registro central, BTC_NEW_ANGLES_RESULTS_20261018.md y PHASE2_PORTFOLIO_DIAGNOSIS_20261018.md; se consultó el resumen de [la referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). La referencia sigue en 33/61 meses activos y15/21 trimestres positivos, CAGR28,8294%, DD motor−14,8905%,220 trades y fee4.595,62. No es candidata final aceptada.

De28 meses negativos observados,13 presentan BTC no negativo y PAXG/SPY conjunto negativo,8 el caso opuesto y7 ambos negativos; cuatro ni siquiera tienen exposición BTC. Esto justifica estudiar otras patas, pero NO identifica meses operables ex ante ni autoriza quitar sus pérdidas. Los tres mejores longs BTC aportan82,4% del neto de esa pata; PAXG/SPY también dependen de pocas colas positivas. Recortar tendencias para cerrar antes puede reducir CAGR sin arreglar MTM, como mostraron TP/falta de progreso.

La tanda BTC reciente ya examinó volumen, estructura short, permanencia, reclaim, reloj por eventos, falta de progreso y calendario semanal; ninguna resolvió el objetivo. El control martes de mayor CAGR no se seleccionó. El inventario histórico es mucho mayor que esta tanda y no se reinicia el contador al ampliar activos. Funding/VIX/COT y sus descargadores siguen descartados.

## Una comparación ejecutable: factorial2×2 congelado

Antes de escribir fuente, root elige y congela UNA receta material PAXG=P y UNA receta material SPY=S, con sus motivos y solapamientos documentados. Este protocolo no elige indicadores ni los deduce de meses malos. Ambos mecanismos deben estar definidos antes de conocer cualquiera de sus resultados. Sus parámetros, risk policy, horas, prioridad y salidas quedan fijados en el mismo acto.

| Celda | BTC | PAXG | SPY | Papel |
|---|---|---|---|---|
|00|Baseline|Baseline|Baseline|Referencia existente, no repetir por rutina|
|10|Baseline|Receta P|Baseline|Ablación PAXG en cuenta compartida|
|01|Baseline|Baseline|Receta S|Ablación SPY en cuenta compartida|
|11|Baseline|Receta P|Receta S|Combinación primaria predeclarada|

Presupuesto inicial máximo: tres full económicos nuevos. Ejecutar10 y01 primero, en los dos slots coordinados; revisar validez contable/técnica, sin ajustar recetas. Ejecutar después11 exactamente como quedó predeclarada, aunque las patas no hayan mejorado cada métrica aislada: la complementariedad es precisamente la hipótesis. Si hay fallo de datos/contrato/contabilidad, detener y reparar sólo ese problema con registro separado; una reparación no se presenta como una hipótesis nueva de alpha.

Propongo11 como candidata primaria y10/01 como controles de atribución, no alternativas seleccionadas después por el mejor período. Root debe aceptar o modificar explícitamente esta designación ANTES de los runs. No promover a posteriori una ablación porque11 decepcione ni fabricar una combinación que use P sólo en sus años ganadores. Si se prefiere que las tres sean candidatas económicas, declararlo ahora como familia de tres comparaciones y reconocer esa selección adicional; no cambiar esa condición después.

## Restricciones arquitectónicas que hacen interpretable el resultado

1. Conservar las tres rutas, símbolos y cuenta10.000, la prioridad canónica del motor y el mismo cálculo de capital, ledger, reservas de órdenes pendientes, caps de margen y reparto inverso ATR. No eliminar una ruta inactiva ni renormalizar pesos según el resultado de sus señales. No optimizar pesos.
2. La serie que alimenta el ATR de asignación conserva el reloj original por activo; un mecanismo con otra temporalidad usa un auxiliar causal para sus señales. No sustituye silenciosamente el ATR común ni altera el calendario SPY. Si se necesita otro reloj de ejecución, exigir antes un control técnico de equivalencia como el ya realizado para BTC1m; no contar ese control como nuevo alpha.
3. Una trading route por exchange/symbol significa UNA posición neta por activo. No existe una segunda cartera virtual gratuita. Si una receta añade un suplemento, el protocolo debe fijar prioridad baseline long→short→suplemento mientras flat, identidad de la pata para su gestión y efecto de ocupación posterior. Si reemplaza una política, declararlo como reemplazo en10/01/11, no llamarlo contribución añadida.
4. Ninguna pata nueva desplaza o cierra una posición original existente salvo que esa gestión sea la hipótesis explícita predeclarada. No cambiar prioridad dinámicamente por desempeño ni reasignar reglas durante una operación.
5. BTC conserva señales, entradas, gestión y riesgo originales; eso NO conserva sus contribuciones, cantidades ni fills. Capital y ocupación de PAXG/SPY cambian la capacidad que BTC encontrará en decisiones futuras. La evidencia válida es cada cartera simulada, no la suma del BTC original con curvas P/S aisladas.
6. Mantener máximos3% por trade/8% agregado planificado, techo bruto4,4x, isolated5x y fee0,00045 por lado en todos los tipos. La reserva10bps del sizing no simula slippage. Fijar el riesgo de cada receta antes de resultados: no escalar para recuperar el CAGR. Si una receta usa riesgo distinto, su efecto económico incluye esa dosis y no se atribuye sólo al indicador.
7. SPY usa histórico SPX CFD BID dividido por10 y horas filtradas; no usar su tick-volume como negociación. PAXG es proxy Spot de oro. Cotización ejecutable, indicadores causales y timestamps cerrados deben validarse según cada receta; no resolver diferencias con forward fill ni datos externos.

## Qué medir, siempre sobre cuenta MTM

Auditoría V4 habitual con órdenes/fills completos, fees al tiempo de ejecución, wallet y curva reconciliados; mismos cortes diarios UTC. Ventana común2020-10-15→2025-12-31 exclusiva, warmup original y2026sellado. Comparar63 meses/21 trimestres, además de denominadores activos y61meses/19trimestres completos; conservar bordes y cash, sin recortar historia favorable.

Para cada celda:
- Regularidad mensual/trimestral y comparación pareada de signos: rescates y deterioros, no sólo cambio neto de porcentaje.
- CAGR/beneficio neto, DD/tiempo bajo agua, peor mes y trimestre, años, fees/turnover y esperanza por trade. No sustituir esperanza por winrate.
- Exposición y riesgo abierto, capital reservado, señales/planes/fills por pata y causas de bloqueo. Los slots ocupados no equivalen al número de señales contrafactuales perdidas.
- Contribución MTM por símbolo/sentido, simultaneidad de pérdidas, concentración en mejores trades y duración de las colas. Distinguir cambios de reglas de cambios endógenos de capital y ocupación.
- Deltas sobre00 y contraste de interacción11−10−01+00 sobre retornos mensuales alineados, como diferencia descriptiva de políticas. No sumar CAGR, no sumar curvas aisladas ni interpretar esa interacción como causalidad econométrica identificada.

Una regla que sube acierto o regularidad recortando las grandes colas puede destruir la economía. Una regla rentable sola puede empeorar la cartera al ocupar el activo cuando llega su señal principal, consumir margen o añadir fees en los mismos meses malos. Esos efectos son parte del resultado, no ruido a quitar.

## Cómo limitar selección y continuidad

Sin rejillas de parámetros/pesos/horas, sin escoger meses a rescatar, sin elegir sólo años favorables. Tres configuraciones congeladas y todos los descartes visibles. Las ablaciones sirven para diagnosticar la interacción, no para crear combinaciones retrospectivas. No volver a probar familias del inventario sin justificar una diferencia material antes de correr.

Los objetivos65–70%meses activos positivos,80%trimestres,DD≤25% y rentabilidad útil no cambian. Mantener también todos los períodos para evitar una mejora cosmética por inactividad. Las incertidumbres nominales pueden mostrarse descriptivamente, reconociendo dependencia y selección acumulada:2020–2025 no es OOS.

Si11 falla, cerrar esta pareja de mecanismos y evaluar el siguiente razonamiento antes de consumir otras pruebas. Si11 parece cumplir, todavía no es final: reservar presupuesto posterior separado para robustez económica/costes/concentración y especificarlo ANTES de cada prueba, luego congelar selección antes de abrir2026. No prometer que tres runs bastarán ni convertir una meseta de desarrollo en validación independiente.
