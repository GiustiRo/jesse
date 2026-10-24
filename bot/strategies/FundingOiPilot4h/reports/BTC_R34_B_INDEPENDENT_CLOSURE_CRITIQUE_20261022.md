# R34 CROSS archivada — crítica interpretativa del cierre

Fecha local: 2026-10-22. Dictamen: CONFORME para cerrar NO_CUMPLE, sin candidata ni vecinos. La cuenta tiene beneficio bajo costos base, pero no alcanza retorno o regularidad requeridos.

## Alcance

Leí BTC_R34_B_RESULTS_20261022.json completo y BTC_R34_B_UNIVERSE_CHECK_20261022.json completo, sin truncamiento. Contrasté resultados, puertas, R11/ledger resumidos, manifiesto financiero y contadores/causas. No volví a auditar las 117 operaciones, 3256 pagos, órdenes o 174 ventanas de fuente por fila. El PASS técnico y financiero por registros pertenece a root y sus recibos; esta revisión es interpretativa. Sin nuevos jobs, motores, precios o cambios de fuente.

## Resultado y suficiencia

[Cuenta R34 CROSS](http://localhost:9200/#/backtest/949c6c55-5845-4fc1-beec-ebcd618692ec): neto4125.6482USDT y final14125.6482 sobre10000 totales, CAGR6.84565%, PF1.51596 y DD M1+fills10.91649%. No confundir +41.26% acumulado del período con retorno anual ni usar5000 como denominador de la cuota1%.

Pasa PF, DD, neto sin dos mejores meses(+1302.4841) yN117 mínimo operativo. Falla CAGR30, meses30/62=48.39% frente65%, trimestres13/20=65% frente80% y mediana mensual−.30659%. Todos62 meses completos fueron activos: aquí no hay mejora artificial del porcentaje por quitar meses inactivos. Mediana negativa y beneficio agregado pueden coexistir por asimetría de ganancias; no es contradicción contable ni una operativa regular ya acreditada.

2023 aporta el mayor retorno anual(+20.33%);2024(+.907%) y2025(+4.468%) son positivos modestos,2022 pierde−1.503%. No elegir años o régimen a posteriori ni tratar51 ventanas12m solapadas como validaciones independientes. N117 satisface sólo suficiencia preliminar; no estima confianza ni robustez futura.

Bruto4892.7504−fees296.0090+funding(−471.0932)=neto4125.6482. A diferencia de recetas negativas incluso en bruto, aquí los costos modelados no destruyeron el signo positivo, pero eso no salva el objetivo. Tampoco autoriza quitar funding, subir riesgo o anualizar sólo el tiempo de exposición.

## Qué acredita la ejecución y qué no

El resumen del universo registra174 cruces,117 planes/fills y57 bloqueos por posición, invalid0. No son174 operaciones independientes ni57 entradas omitidas que puedan monetizarse: un cruce estando ocupado puede ser precisamente el evento usado para liquidar según la regla sin reverse. No inferir que permitir reversión automática mejoraría el resultado ni construir ese vecino.

Los motivos auditados55STOP/57pricecross/5hold suman117; el tipo nativo tiene62MARKET, que se descompone entre cruce y plazo. Cero terminal/unclassified. Eso acredita que las salidas por estado y por30d tuvieron uso real en esta trayectoria, sin demostrar que una sea superior a una gestión alternativa. Hubo UN motor, sin control pareado de salida; no atribuir PF o beneficio causalmente al exit por cruce.

El cap1x adicional y el cupo diario registraron0 rechazos. Estuvieron presentes pero no restringieron cantidades/entradas bajo esta realización; no es licencia para retirarlos ni prueba de paridad con el sizingV5. Reserva/lote/riesgo, capitalización, ventana y observación también difieren. El archivo original permanece referencia descriptiva: elegible sin confirmaciónV5, no control equivalente ni nuevoOOS. No presentar CAGR21.33→6.85 como estimación aislada del deterioro del mismo programa o efecto de cambiar2%a1%.

R11 y ledger resumidos terminan PRETERMINAL con117 opens/closes y saldo coincidente; no inventar un FINAL adicional al no existir cierre terminal. La semántica del contador nativo preterminal sigue siendo la auditada por root, no una posición pendiente supuesta. DD es M1+fills, no todos los extremos intraminuto.

Los longs54 aportan4488.72USDT y shorts63−363.07. Es atribución dentro de la cuenta mixta, no resultado de una cuenta long-only: retirar shorts cambiaría disponibilidad, capital y selección. No promueve una variante por ese desglose.

## Decisión

La oportunidad documental pendiente quedó evaluada bajo el contrato actual: rentabilidad positiva y riesgo observado moderado, insuficientes para las puertas conjuntas. Se conserva como resultado informativo sin candidata. Cerrar el presupuesto de un motor, sin nuevos cruces, parámetros, lados, cap, reverse, stop o plazo para rescatarlo. No concluir que toda tendencia por medias sea inviable ni que la gestión opuesta haya sido optimizada.
