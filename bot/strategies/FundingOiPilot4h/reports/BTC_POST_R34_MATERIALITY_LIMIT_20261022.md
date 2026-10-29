# Siguiente pregunta tras R34: sin receta nueva suficientemente justificada

Fecha: 2026-10-22. Alcance documental, sin nuevos precios, clases, análisis, drafts ni motores.

## Decisión

No recomiendo gastar un motor en esta pasada. No identifiqué una condición observable antes de entrar que permita separar una oportunidad recurrente con payoff asimétrico de los mecanismos ya evaluados. Esto describe el alcance de esta búsqueda; no demuestra que se haya agotado toda estrategia posible ni que los datos OHLCV carezcan de información.

La información que falta es concreta: un discriminante previo a la entrada, con una razón económica distinta, que permita distinguir absorción de presión transitoria frente a continuación del desplazamiento. OHLCV permite medir la trayectoria y el volumen agregado, pero no identificar por sí solo liquidaciones, profundidad retirada, lado agresor ni inventario de participantes. No corresponde sustituir esos fenómenos por otra combinación arbitraria de mecha, volumen y retorno y presentarla como una fuente nueva de evidencia.

## Contrastes consultados y descartes

1. Barreras monetarias: descartadas por repetición exacta en BTC. Se releyeron BtcResearchR13RoundBase1m, BtcResearchR13Round1000m y BtcResearchR13RoundShift1m, además de BTC_DISCOVERY_L_PROTOCOL_20261021.md y BTC_DISCOVERY_L_FINAL_20261021.md. L ya compara rechazos horarios de 1000n y 1000n+500, con consumo/rearme, ATR previo, stop1ATR, target2ATR y vencimiento12h. Su cierre prohíbe barrer espaciado, offset, buffer o gestión. El antecedente PAXG R20PaxgRoundBarrier1h tampoco crea una brecha BTC. Mi mensaje preliminar sobre ausencia de equivalente BTC fue incompleto y quedó corregido antes de cualquier propuesta o implementación. No hay propuesta de otro nivel monetario.

2. Agotamiento de una descarga y recuperación: RangeFade5m ya contiene flush de30min, amplitud/volumen, reversión parcial confirmada, régimen4h y targets de recuperación. V4 shock, R8 X803 y las continuaciones N204/K cubren antecedentes cercanos de shock/rechazo/fallo de recuperación. No acredito aquí resultados de RangeFade5m a partir de sus comentarios ni afirmo que se haya ejecutado exactamente esa fuente. Sin un discriminante económico adicional, trasladar su combinación o cambiar reloj/objetivo sería otra receta de trayectoria, no la información nueva solicitada.

3. Tendencia con cola favorable: se releyó ResearchV3ChannelP4h, V3_P_REPLAY_RESULT_20261020.md y FINAL_DECISION_V3.md. CHANNEL_P ya tuvo replay nominal, estrés y vecinos; no es una receta archivada sin evaluación como lo era CROSS_P antes de R34. Su salida trailing no autoriza otro motor cambiando la ventana actual, el riesgo o el plazo para rescatarla.

4. Salida según estructura: R34 ya completa CROSS_P bajo el contrato actual. R12AR, BSTATE/R14 y V6ER, junto con R4/R7 y Y903, son antecedentes de continuidad, caducidad e invalidación observables. Elegir ahora otro estado de retorno al origen, un trailing o un plazo próximo no responde a una pregunta diferente sólo por alterar la asimetría del payoff.

## Qué podría desbloquear otra pregunta

Hace falta una hipótesis que especifique, antes de mirar nuevas curvas: qué información disponible añade, por qué distingue dos mecanismos y qué control conserva lo demás. Una etiqueta como «absorción», «liquidación», «persistencia» o «convexidad» no satisface ese requisito. Si su implementación exige flujo u otra fuente inexistente, debe quedar HOLD y requerir alcance propio; este documento no solicita ni autoriza nuevos datos.

No recomiendo retirar shorts por la atribución de R34, relajar los disparadores escasos A/C, repetir CHANNEL_P ni convertir una mayor relación target/stop en nueva ventaja. El presupuesto propuesto para esta pasada es cero motores. Los objetivos y el contrato de riesgo/costos permanecen intactos.

## Evidencia y límites

Fuentes de lectura MCP: strategies/BtcResearchR13RoundBase1m/__init__.py; strategies/BtcResearchR13Round1000m/__init__.py; strategies/BtcResearchR13RoundShift1m/__init__.py; strategies/R20PaxgRoundBarrier1h/__init__.py; strategies/RangeFade5m/__init__.py; strategies/ResearchV3ChannelP4h/__init__.py.

Reportes del anchor FundingOiPilot4h/reports: BTC_DISCOVERY_L_PROTOCOL_20261021.md; BTC_DISCOVERY_L_FINAL_20261021.md; V3_P_REPLAY_RESULT_20261020.md; FINAL_DECISION_V3.md; RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md; BTC_R34_B_INDEPENDENT_CLOSURE_CRITIQUE_20261022.md.

El inventario raíz consultado no estaba truncado; el inventario de reportes sí tenía límite y no se usa como prueba de ausencia global. Esta revisión es acotada y no reaudita trades ni convierte resultados anteriores en controles económicos equivalentes.
