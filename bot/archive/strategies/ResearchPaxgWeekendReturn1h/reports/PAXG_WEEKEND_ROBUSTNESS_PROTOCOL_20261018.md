# PAXG: protocolo de sensibilidad de la receta de fin de semana

Fecha local: 18 de octubre de 2026. La receta primaria permanece fija en EVENT_ATR = 1.0. Sus resultados ya observados son 37 trades, neto +400,22 USD y PF 1,5073, con 84,3% del beneficio en la cohorte de cierre 2022 y −34,82 USD en el agregado 2023–2025. Estas debilidades se conservan; no se redefine la primaria.

Root autorizó dos vecinos y un estrés de ejecución separado. Este protocolo se guarda ANTES de ejecutar los vecinos y antes de conocer sus resultados.

## Vecinos simétricos

Crear ResearchPaxgWeekendEvent0751h y ResearchPaxgWeekendEvent1251h como copias completas de ResearchPaxgWeekendReturn1h. Sólo cambian el nombre de clase y EVENT_ATR a 0.75 y 1.25. La distancia simétrica de 0,25 ATR comprueba si la expectativa depende de un umbral estrecho; no busca un umbral ganador.

Mantener el ancla del viernes 16:00 de Nueva York, evento del domingo 16:00, ATR 14 de velas 4h completas fijado al ancla, entrada MARKET, target pasivo en el ancla, stop 2 ATR y máximo 24 horas desde el fill real. No elegir sentidos, años, ventanas u horarios después del resultado.

Ambas cuentas usan 10.000 USDT, riesgo del 1%, fee 0,00045 por lado incluso LIMIT, 5x aislado, techo bruto 4,4x y reserva de 10 bps sólo para sizing. PAXG-USDT 1h con auxiliares 1m y 4h, 2020-10-15 a 2025-12-31 exclusiva, modo normal y warmup 240. Mantener como máximo dos backtests y un análisis propios simultáneos.

## Interpretación predeclarada

La primaria no cambia a la variante de mayor neto. Reportar todos los resultados, incluido cualquier deterioro. Examinar el signo del neto, el antes de fees, sensibilidad estática a 5 y 10 bps extra, tamaños, fills, concentración, cohortes de cierre por año y agregado 2023–2025. Root calcula calendario MTM exacto por separado.

Vecinos positivos que dependan también de 2022 no bastan para afirmar robustez temporal. Una variante positiva reciente no rescata retrospectivamente el fallo temporal de la primaria. La señal puede tener baja actividad: no exigirle aisladamente 65% de meses positivos, objetivo que pertenece a la cartera.

Root ejecutará separadamente un estrés de target MARKET al cierre de 1h posterior al toque, sin target LIMIT pasivo, con entradas y stop conservados. Su clase y job son de root. El contraste tensiona ejecución, no constituye un nuevo selector de alpha. No integrar la señal en la cartera antes de evaluar este conjunto.

Al completar estos vecinos, este agente habrá ejecutado SIETE backtests económicos PAXG nuevos: cinco previos y dos vecinos. El estrés de root sería el octavo de esta línea global y se contará aparte. No MC, optimización, datos nuevos, funding, scripts, framework, live/Pi ni 2026.
