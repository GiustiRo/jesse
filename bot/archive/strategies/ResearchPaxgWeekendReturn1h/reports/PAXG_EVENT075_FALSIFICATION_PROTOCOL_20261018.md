# PAXG 0,75 ATR: controles de falsación posteriores al hallazgo

Fecha local: 18 de octubre de 2026. Protocolo guardado antes de ejecutar dos controles nuevos. La elección de estudiar 0,75 ATR surge de resultados YA observados: 60 trades, +764,04 USD, PF 1,7318 y cohortes 2023–2025 +310,76 USD. Es selección adaptativa de desarrollo. Estos controles NO son validación independiente ni sustituyen la primaria fijada en 1 ATR.

La primaria sigue teniendo débil temporalidad reciente; el vecino de 1,25 ATR sigue fallando muestra, PF y fricción extra. No se prueban más umbrales, horarios, lados ni salidas nuevas.

## Dos preguntas y cambios exactos

A. ResearchPaxgWeekdayEvent0751h: copiar ResearchPaxgWeekdayReturn1h cambiando solamente nombre de clase y EVENT_ATR de 1.0 a 0.75. Conserva ancla lunes 16:00 NY, evento miércoles 16:00 NY, target LIMIT en el ancla, stop 2 ATR y máximo 24 horas. Pregunta: ¿el resultado de 0,75 ATR del fin de semana contrasta también con un control hábil al MISMO umbral? No se compara sólo con el control anterior de 1 ATR.

B. ResearchPaxgWeekend075CloseStress1h: copiar ResearchPaxgWeekendCloseStress1h de root cambiando solamente nombre de clase y EVENT_ATR de 1.0 a 0.75. Conserva ancla viernes 16:00 NY y evento domingo 16:00 NY. No existe target LIMIT: un toque del objetivo en la vela 1h completada genera salida MARKET en ese callback, con deuda de salida si falta la cotización M1 consistente. Stop de 2 ATR y máximo 24 horas conservados. Pregunta: ¿el hallazgo de 0,75 depende del fill pasivo en el ancla?

La referencia comparativa es ResearchPaxgWeekendEvent0751h, sesión ff199ebe-dab0-4c09-9078-fff98188e97c, [dashboard](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c). Su resultado se conserva completo. No se cambia de primaria ni se integra una ganadora automáticamente.

## Condiciones y presupuesto

Dos full económicos nuevos, como máximo dos propios simultáneos y un análisis propio. Al terminar, este agente habrá ejecutado nueve full PAXG; sumado el estrés de 1 ATR ejecutado por root serán diez de la línea PAXG global. No ocultar los descartes ni reiniciar el contador de hipótesis.

Misma ventana 2020-10-15 a 2025-12-31 exclusiva, PAXG-USDT 1h con auxiliares 1m y 4h, Binance Perpetual Futures, modo normal, warmup 240. Capital 10.000 USDT, riesgo del 1%, 5x aislado, fee 0,00045 por lado incluso LIMIT, techo bruto 4,4x y reserva de 10 bps sólo para sizing. Toda la lógica de freshness, paridad M1/1h, ancla causal, ATR de 4h completas y DST de Nueva York se conserva.

No nuevas fuentes, scripts, instalaciones, framework, live/paper, Pi ni 2026. No más búsquedas de umbral después de estos controles.

## Evaluación antes de ver los resultados

Analizar TODOS los snapshots de los dos controles y del hallazgo 0,75. Reconstruir fees, fills, cantidades y wallet; verificar días/horas y holding máximo. Comparar timestamps y sentidos de las entradas del estrés con el 0,75 pasivo, y el máximo desvío de precios; cantidades pueden variar por el capital endógeno.

Reportar neto, antes de fees, PF, actividad, direcciones, concentración, cohortes de cierre por año y agregado 2023–2025. Evaluar costes extra estáticos de 5 y 10 bps RT sobre mismos fills, sin llamarlos backtest dinámico. Root podrá reconstruir MTM calendario exacto; no usar muestras del motor a las 00:01 como cierre diario.

Un control hábil positivo y comparable debilita la especificidad del fin de semana. Pérdida del estrés o fragilidad ante costes debilita ejecutabilidad. Si la evidencia continúa débil, cerrar esta continuación sin más búsqueda. Superar controles conserva una pista de desarrollo, no demuestra mint/redemption causal, estabilidad fuera de muestra ni traslado al perpetual.

Los porcentajes mensuales activos del 0,75 no implican cumplir la meta de cartera: root informó 28/40 activos positivos, pero sólo 28/63 meses de calendario y 16/21 trimestres. La cartera real requiere capital compartido y no suma de curvas.
