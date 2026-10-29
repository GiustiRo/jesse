# Ronda exploratoria R32: tres preguntas, seis pruebas
Fecha local: 22 de octubre de 2026. Estado: ronda terminada y auditada. Ninguna candidata; el objetivo de investigación sigue pendiente.

Participaron tres subagentes, uno por línea. Se completaron los seis backtests previstos, sin fallos de motor ni repeticiones económicas. Cada fila representa una cuenta alternativa de10.000USDT con cuota de riesgo activa del1% sobre ese capital total y el resto de la cuota BTC ociosa. No son seis operativas ejecutadas juntas.

|Prueba|Operaciones|CAGR neto|PF neto|DD M1+ejecuciones|Meses activos positivos|Trimestres positivos|
|---|---:|---:|---:|---:|---:|---:|
|[A · Aceptación temporal](http://localhost:9200/#/backtest/339e9161-6e59-4acf-a75e-9ddcad2ad902)|435|-0.05%|1.00|20.72%|31/62|9/20|
|[A · Sólo cierre fuera](http://localhost:9200/#/backtest/56d170b7-1aa6-49c0-8ba9-116eaebaefee)|755|-0.76%|0.99|25.01%|29/62|11/20|
|[B · Todos los fallos](http://localhost:9200/#/backtest/67655c18-3682-4397-b119-52fd1ea8edba)|195|-1.52%|0.91|17.53%|25/59|8/20|
|[B · Fallo persistente](http://localhost:9200/#/backtest/9228f0b1-5c61-43ed-9edf-ef1b7556b5f5)|160|-1.72%|0.87|14.50%|25/56|9/20|
|[C · Contención completa](http://localhost:9200/#/backtest/6510739f-6c8d-45b4-904f-67395c95cca0)|523|-4.05%|0.88|28.28%|25/62|8/20|
|[C · Sólo cierre dentro](http://localhost:9200/#/backtest/175b17fe-58e2-456d-ad0c-44f8cd799755)|1265|-5.17%|0.93|40.93%|34/62|9/20|

CAGR anualiza la cuenta completa; no significa retorno de cada año. DD usa marcas M1 y ejecuciones, sin todos los extremos intraminuto. Los meses calendario completos son62 en todas las filas; el denominador activo cambia cuando no hay exposición. N>=100 es sólo suficiencia operativa preliminar, no confianza estadística.

## Qué respondió cada línea

**A. Continuación por aceptación temporal.** Comparó el primer cierre4h fuera del rango del día UTC anterior con exigir que al menos120 de sus240 cierres M1 hubieran permanecido fuera de ese mismo nivel, conocido antes de comenzar el bloque. El evento se consume igual en ambas cuentas, incluso si la posición está ocupada o el filtro rechaza la entrada.

La aceptación mejora los tres criterios comparativos fijados antes de resultados: retorno, DD y meses calendario positivos (31 frente a29). Pero reduce trimestres positivos de11 a9 y termina perdiendo28,27USDT en toda la ventana. Su PF es0,9985: prácticamente equilibrio, sin la rentabilidad o regularidad buscada. Hay preferencia relativa bajo la regla declarada, sin dominancia general ni candidata. La diferencia monetaria frente al control es+363,21USDT: menor bruto (−652,31), ahorro de fees (+918,37) y menor débito de funding (+97,14). Es una descomposición aritmética de cuentas completas, no efectos causales separados. La mejora relativa no demuestra mayor capacidad predictiva: también cambia la actividad y sus costos. No aumentar riesgo, quitar funding ni buscar un nuevo umbral para convertir ese equilibrio en aprobación.

**B. Persistencia del fallo de ruptura.** Tras un cierre exterior y un regreso al rango, ambas políticas esperan una barra adicional. Una revierte todos esos fallos y la otra sólo los que siguen dentro del rango congelado. La permanencia reduce DD, pero empeora retorno y PF. Ambos mantienen25 meses calendario positivos; el porcentaje activo mejora porque el denominador baja de59 a56. No agrega un mes ganador. No se demuestra que esperar esa permanencia produzca la ventaja buscada.

**C. Contención antes de ruptura.** Comparó una vela enteramente contenida dentro de la madre con exigir sólo que su cierre estuviera dentro, antes de romper el rango de esa madre. La contención completa pierde menos y baja DD, pero empeora PF y regularidad. Ambos superan el techo de DD y pierden dinero; no hay una operativa aprovechable bajo esas reglas.

Las tres pertenecen a familias con antecedentes conocidos. Las diferencias de filtro, referencia y reloj fueron explícitas; no se presentaron como fenómenos jamás explorados.

## Qué aprendimos para buscar fortalezas

Los filtros no aportaron lo mismo. En A hay una mejora relativa medible, pero demasiado pequeña para crear una ventaja neta. En B la reducción de riesgo vino acompañada de peor resultado. En C reducir operaciones y pérdida total tampoco mejoró la calidad monetaria o la regularidad. Por eso no conviene considerar un menor DD o un mayor PF aislado como fortaleza suficiente para combinar.

Algunas contribuciones long fueron positivas dentro de cuentas mixtas, pero no acreditan cuentas long independientes. Selección, ocupación y capital cambian al retirar un lado. No se eligió una división definitiva Long/Short, tendencia/rango ni un número de especialistas. La unidad futura sigue siendo un comportamiento explotable con reglas observables antes de entrar.

No hay motivo para estudiar una cartera conjunta con estos seis resultados. Para la siguiente ronda hace falta una diferencia de información o mecanismo que pueda producir ventaja neta; añadir otro filtro de confirmación o cambiar una etiqueta de régimen por inercia no está justificado. Esto cierra estas comparaciones; no declara agotadas las familias ni prohíbe variantes futuras con una pregunta material propia.

## Contrato y auditoría

BTC-USDT perpetuo de Binance, ejecución1m y decisiones4h, UTC[2020-10-15,2026-01-01). Historia extensa ya observada y adaptativa; no OOS nuevo. Taker con descuento0,00045 por lado, funding histórico activado/aplicado/verificado, dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571. Slippage modelado cero; reserva0,001 sólo para sizing, lote0,001. Cuotas iguales futuras dentro del2% BTC total, sin redistribución automática;6% global y3x aislado. No se cambió exposición para rescatar curvas.

A/B compartieron stop2ATR14 simple, TP2R y plazo48h; C stop2ATR14 y plazo24h sin TP. La gestión fue idéntica dentro de cada pareja y declarada antes de resultados. Las diferencias entre líneas no identifican un efecto puro del disparador.

Se conciliaron3.333 operaciones y11.028 pagos de funding completos con sus órdenes, planes y aperturas/cierres nativos. Error financiero menor a1e−6USDT: bruto menos fees más funding igual a PNL y saldo final menos10.000. Se verificaron cantidad/precio/tipo MARKET de entrada, riesgo previsto con reserva, protección, objetivos y plazos reales de salida. Meses contiguos y retornos encadenados contra equity;2.741.760 marcas M1 por cuenta, invalid0.

A tuvo1.146 eventos brutos iguales en ambos brazos,523 que pasan el contexto temporal y cero días inválidos; B212 fallos iguales,168 interiores y44 recuperaciones originales. Estos son eventos previos a selección de cuenta, no operaciones contrafactuales ni muestras independientes.

Cuatro jobs sintéticos (base común y tres líneas) pasaron al primer intento. Hubo cuatro intentos de análisis de snapshots: tres completados y uno fallido por interpretar mal total_open_trades. El framework cuenta posiciones encontradas abiertas ANTES de cerrarlas forzosamente al terminar; se corrigió el auditor y se comprobó PRETERMINAL/FINAL, orden de cierre, PNL y fee terminal. No se repitió ningún backtest por ese incidente ni se modificaron estrategias después de sus resultados. Código, fallo y correcciones se conservan.

Concurrencia respetada: máximo dos motores y un análisis. Los seis motores están terminados; no quedan procesos de esta ronda trabajando.57 IDs económicos completados desde r9, separados de los209 históricos V1–V6; no sumar como muestras independientes. No se ejecutaron estrés de costos, variantes de riesgo, datos nuevos,2026 nuevo,USDC,cartera ni live/paper. Padres, framework y configuración global intactos.

## Evidencia guardada

Informes individuales BTC_R32_A_FINAL_20261022.md, BTC_R32_B_FINAL_20261022.md y BTC_R32_C_FINAL_20261022.md, con resultados JSON, índices durables de registros/raw/artefactos, protocolos, fuentes, checks, manifiestos previos y revisiones críticas independientes de alcance acotado. Las revisiones críticas no reauditaron cada fila financiera.

Los archivos están en strategies/FundingOiPilot4h/reports/ dentro del proyecto Jesse de la máquina ejecutora. El panel de investigación publica esta síntesis y las tarjetas de las tres líneas. Ninguna promoción operativa ni objetivo económico cumplido.
