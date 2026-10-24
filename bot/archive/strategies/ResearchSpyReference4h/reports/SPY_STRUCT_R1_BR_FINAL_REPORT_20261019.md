# SPY Structural R1 BR — seis resultados reales

Las seis configuraciones terminaron y sus snapshots completos concilian costes, PnL y balance. BR02, que admite rupturas posteriores dentro de un episodio, es la única que supera el neto de Cq. Es una pista de eficiencia con16 operaciones, no una mejora robusta demostrada ni sustitución de la referencia. Las otras cinco no justifican promoción; cuatro tienen sólo4–10 trades.

## Resultados comparables

| Control | N | Neto | Fees | PF | Sharpe | DD motor % | CAGR motor % | Tiempo abierto % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 31 | 751.35 | 286.48 | 1.49 | 0.458 | -5.21 | 1.40 | 15.26 |
| [M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | 38 | 151.60 | 336.73 | 1.07 | 0.106 | -7.72 | 0.29 | 16.00 |
| [BR01](http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b) | 24 | 71.82 | 209.42 | 1.06 | 0.066 | -6.70 | 0.14 | 10.04 |
| [BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810) | 16 | 874.80 | 150.59 | 2.32 | 0.718 | -3.80 | 1.62 | 8.79 |
| [BR03](http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41) | 10 | 223.87 | 89.19 | 1.59 | 0.263 | -4.39 | 0.43 | 6.05 |
| [BR04](http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f) | 7 | 628.91 | 63.13 | 5.85 | 0.661 | -2.17 | 1.18 | 4.47 |
| [BR05](http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1) | 4 | 430.81 | 36.96 | 5.78 | 0.684 | -1.83 | 0.81 | 3.45 |
| [BR06](http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da) | 4 | 179.59 | 38.81 | 2.04 | 0.313 | -2.62 | 0.34 | 1.99 |


Cuenta inicial10 000USDT. N son operaciones cerradas, no fills ni observaciones independientes. DD/CAGR/Sharpe de la tabla pertenecen al muestreo del motor; root completó auditoría MTM a cierre diario UTC de las seis con conciliación terminal. Cq/M son sesiones existentes reutilizadas, sin fulls extra.

BR01 admite sólo la primera señal Cq desde un reset de precio al midpoint del canal26 previo; BR02 admite las siguientes. BR03 compra MARKET cuando el primer contacto real posterior al breakout sostiene el techo al cerrar. BR04 exige primer contacto fallido y reclaim en una barra futura. BR05/06 comparten el hold de BR03 y cambian la entrada al high de la vela de retest o al high original de ruptura, con STOP previsto o MARKET si ese umbral ya está superado.

## BR02: qué mejora y qué sigue sin demostrarse

BR02 gana874.80 frente751.35 de Cq: incremento123.45, o1.23% del capital inicial durante toda la ventana. El PnL bruto de precio es ligeramente MENOR:1025.39 frente1037.82, diferencia−12.43. La comisión baja de286.48 a150.59, ahorro135.88. La identidad contable del incremento es−12.43+135.88=+123.45; describe las carteras realizadas, no un efecto causal puro de reducir fees sobre los mismos trades.

Tiempo abierto8.79% frente15.26%; notional×tiempo a precio de entrada sobre capital inicial/ventana .08121x frente.14149x. Turnover de entrada16.68x frente31.78x del capital inicial. Neto por notional rotado52.44bps frente23.64bps. El menor DD observado y mayor neto con menos participación hacen defendible estudiar eficiencia de esta selección, sin elevar riesgo ni extrapolar retorno a exposición constante.

Sólo siete entradas reales son exactamente comunes con Cq. BR02 tiene nueve entradas adicionales que Cq no ejecutó, mientras Cq tiene24 que BR02 no ejecutó. No es simplemente eliminar15 trades de una lista fija: ocupación, saldo y sizing cambian. BR01/BR02 son cuentas aisladas;24+16 no reconstruye las31 operaciones de Cq y sus PnL no se suman como cartera.

Sin su mejor trade BR02 conserva455.51; sin los tres mejores pierde86.36. Los tres mayores superan su beneficio total. La concentración es menos extrema en ese diagnóstico que Cq, cuyo neto sin tres mejores es−298.22, pero la dependencia de pocos runners persiste. MenorN no demuestra ausencia de señal y tampoco permite afirmar robustez.

| Año de cierre | Neto Cq | Neto BR02 | Trades BR02 |
| --- | ---: | ---: | ---: |
| 2020 | 137.98 | 137.98 | 1 |
| 2021 | 335.83 | 246.38 | 2 |
| 2022 | -215.41 | -110.70 | 2 |
| 2023 | 395.76 | -67.93 | 6 |
| 2024 | -22.51 | 345.72 | 3 |
| 2025 | 119.70 | 323.35 | 2 |


Estas son cohortes por año de CIERRE, no rentabilidades MTM anuales. El cambio es heterogéneo: BR02 empeora mucho2023, mejora2024 y2025, y sigue negativa2022/2023. No se eligen años favorables ni se recorta la ventana.

La auditoría MTM independiente de root da para BR02 DD diario−3.8052545%,12/61 meses completos positivos,18 meses activos y9/19 trimestres completos positivos. Cq tiene15/61 meses positivos,33 activos y también9/19 trimestres positivos. No mejoró el número de trimestres positivos; redujo participación. La regularidad individual no se convierte en obligación de cada señal ni sustituye una evaluación de cartera.

## Los otros contrastes

BR01 termina71.82 y ya pierde44.52 al añadir5bpsRT. Sin su mejor trade es negativa. En esta muestra no respalda priorizar siempre la primera ruptura tras reset; tampoco prueba que toda primera ruptura carezca de utilidad.

BR03 obtiene223.87 con10 trades; sin el mejor queda−61.24. BR04 obtiene628.91 con7, PF5.85 y DDmotor−2.17%. Sus métricas parecen favorables, pero el mejor trade aporta407.91 y los tres mayores explican más del neto; sin ellos pierde54.56. Sólo hay operaciones de cierre2022–2025 y la mejora se concentra en2024/2025. Es insuficiente para promover el reclaim por ese PF.

BR05 obtiene430.81 con cuatro trades, uno por cada cohorte de cierre2020/2021/2023/2024. BR06 gana179.59 con cuatro y sin su mejor pierde93.46. No hay base para elegir el high de retest como ancla superior sólo por comparar dos muestras de cuatro operaciones.

Las entradas ejecutadas de BR05 fueron4STOP. BR06 registró2STOP y2MARKET, coherente con permitir precio actual si el umbral ya está superado y la semántica smart-order. La referencia Cq también contiene24LIMIT+7MARKET; la política intentada no implica un único tipo de fill. No se simula un STOP retroactivo en el high que ya ocurrió.

No hay trayectorias económicas/curvas exactamente idénticas entre las seis recetas. Esa distinción de caminos tampoco las hace independientes: mismo activo, misma historia y episodios relacionados. BR03/BR05 no tienen fills exactamente comunes y BR05/BR06 sólo uno. Una diferencia global mezcla precio, selección de fills y disponibilidad posterior; no se atribuye sólo a mejor ejecución.

## Fricción y concentración

| Control | Neto +5 bps RT | Neto +10 bps RT | Sin mejor trade | Sin tres mejores |
| --- | ---: | ---: | ---: | ---: |
| Cq | 592.19 | 433.04 | 349.58 | -298.22 |
| BR01 | -44.52 | -160.87 | -304.57 | -836.48 |
| BR02 | 791.13 | 707.47 | 455.51 | -86.36 |
| BR03 | 174.32 | 124.77 | -61.24 | -309.79 |
| BR04 | 593.84 | 558.77 | 221.00 | -54.56 |
| BR05 | 410.28 | 389.75 | 153.90 | -90.08 |
| BR06 | 158.02 | 136.46 | -93.46 | -87.89 |


Stress añade costes proporcionales5/10bps por roundtrip sobre los mismos fills/tamaños y ambas piernas. No simula cola, spread variable, impacto ni redimensionamiento. Todas salvo BR01 permanecen positivas con10bpsRT, pero todas quedan negativas sin sus tres mejores trades. Retirar ganadores es diagnóstico de concentración, no descarte automático de una estrategia runner. En muestras de cuatro operaciones su poder para caracterizar un mecanismo es especialmente limitado.

## Contrato causal y límites

El origen Cq se evalúa por precio/history/régimen/calendario/fresh antes de capital o posición. Contadores y episodios evolucionan ocupado; un evento no ejecutable se consume, sin cola. BR01/02 permanecen censuradas hasta primer reset observado. BR03..06 congelanL/H en el origen, exigen low<=L<=high para contacto real y rechazan una primera barra enteramente debajo del nivel. Vida de cuatro observaciones filtradas posteriores, no dieciséis horas garantizadas. Un episodio consumido sigue bloqueado hasta expiry común; no se rearma en esa misma barra.

El futuro reclaim de BR04 ocurre después del primer contacto, nunca en la barra de armado. STOP usa precios conocidos al decidir y sólo se envía para futuro; max(anchor,precioactual) evita LIMIT accidental cuando el umbral ya se superó. La evaluación posterior exige régimen/ATR/fresh actuales. El stop inicial desde fill efectivo, BE2.25R, trail4.2 y tightening permanecen idénticos a Cq.

Root verificó seis fuentes reales, formularios e hiperparámetros contra contrato. QA sintética del before/_origin/_set_struct_event reales mediante AST pasó37assertions, job7fb34653720f43fdabb1b722c50faaa4: arming/contacto/gap/expiry/no-replay/censura/reclaim. Esa prueba lógica no observa oportunidades económicas ni reemplaza el backtest. Los snapshots no exportan todas las vars, señales ocupadas o razones de ausencia de entrada; no se inventan esos conteos.

Condiciones: SPY4h+M1, warm240, fast/debugfalse; UTC Mon-Fri00–20features y baropen00–16entry exactos. Capital10 000, riesgo presupuestado1%, fee.00045 por lado, isolated5x/cap4.4, reserva.001 sólo sizing, límites de cartera/margen originales. Proxies de precio aceptados, funding fuera.2020-10-15→2025-12-31 exclusiva,2026 cerrado; desarrollo reutilizado, no OOS limpio. Sin nuevas fuentes, BTC/PAXG, framework, instalaciones, scripts, reinicios, live/paper/Pi ni cambios de riesgo. No se ejecutó ninguna ronda2/3.

## Trazabilidad y cierre

Protocolo SPY_STRUCT_R1_BR_PROTOCOL_20261019.md y fuente común/diffs SPY_STRUCT_R1_BR_IMPLEMENTATION_REVIEW_20261019.md guardados antes de correr; fuentes autocontenidas SpyStructR1BR01..06, readback6/6 y snapshots completos en notes de cada sesión antesrun.

Auditoría económica8snapshots:43639f36bc2c4a60911d6558528dff69 succeeded. JSON íntegro29680bytes<50KB en SPY_STRUCT_R1_BR_AUDIT_20261019.md. Seis filas exactas y dos referencias separadas en SPY_STRUCT_R1_BR_EXACT_RESULTS_20261019.md; pares completos persistidos en SPY_STRUCT_R1_BR_pairs_*.md. Fuente de análisis SPY_STRUCT_R1_BR_ANALYSIS_SOURCE_20261019.md. MTMroot4161d43204da46aeb06a959be1836d61 succeeded. No se afirma inspección visual adicional de PNG; conclusiones numéricas y MTM son reproducibles independientemente.

BR01 — SpyStructR1BR01

Dashboard: http://localhost:9200/#/backtest/bb193097-9600-4ca0-94a5-434bb1c30e1b

BR02 — SpyStructR1BR02

Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810

BR03 — SpyStructR1BR03

Dashboard: http://localhost:9200/#/backtest/4921c591-e830-43be-80c0-c1ac795ecc41

BR04 — SpyStructR1BR04

Dashboard: http://localhost:9200/#/backtest/6f66fc51-6829-4ee0-80f9-ba26943ba75f

BR05 — SpyStructR1BR05

Dashboard: http://localhost:9200/#/backtest/8932b93b-d380-4699-8f7c-d2fd895553f1

BR06 — SpyStructR1BR06

Dashboard: http://localhost:9200/#/backtest/fb232660-27f5-47d8-a6c4-fb9b152f95da


Ronda1 de esta línea cerrada. BR02 queda como candidata de investigación de eficiencia para decisión central; necesita atribución y estabilidad, no promoción por máximo de tabla. BR04 es una pista mucho más escasa. Las otras recetas no justifican ampliar pruebas para salvarlas. La referencia permanece intacta y no se lanzan rondas adicionales automáticamente.
