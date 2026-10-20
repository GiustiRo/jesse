# Protocolo: caducidad de la continuación bajista
Hipótesis exploratoria: si la caída que motiva el short no progresa pronto, mantenerlo72h puede consumir margen y exponerse a un rebote. Probar salida temporal24h y48h frente a72h, sin cambiar entradas/stop/target/longs/riesgo. No usar duración final para filtrar retrospectivamente trades: sería conocimiento futuro. Nuevos backtests reejecutan todas las interacciones.

Referencia congelada [candidata](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), 2026 reservado. Solo2020-10-15 a2025-12-31 exclusivo, modo normal,fee.00045,10000,5xisolated,3%/8%riesgo. Reglas de cierre se comprueban cada4h: duración realizada no será exactamente24/48/72h para fills intrabar.

Diagnóstico previo feb81963abd4403c867fae6472ec7015:123shorts,PF1.3602,winrate55.2846%,ganancia media293.58,pérdida266.85. Ganadoras16.54h/perdedoras25.25h. Duraciones finales<=12h aportan6776.62USDT;>12h suman-1489.60USDT. Agrupar por duración final es descriptivo, NO prueba causal de que salir a12h mejore. Evitar elegir12h para maximizar este histograma. Se predeclaran24/48 por hipótesis de uno/dos ciclos diarios frente a72, no búsqueda fina.
Ganadoras long duran mucho más que perdedoras; no aplicar esta hipótesis a longs.

Criterios: leer ambas variantes, incluso si son peores. Mantener shorts netos positivos, comprobar aporte incremental al portafolio,meses/trimestres MTM frente a referencia yDD<=25%. Si alguna mejora estructuralmente, repetir ambas con+10bpsRT y períodos congelados antes de seleccionarla. No declarar éxito por winrate>51% ni por una única variante ganadora; no retocar objetivos65–70%mesesactivos/80%trimestres. Una mejora parcial sigue siendo candidata no aprobada.

PAXG/SPYlongs muestran dependencia fuerte de su mejor trade (~90%/~94%de su beneficio neto individual); incluir concentración en siguientes controles, no asumir que toda debilidad de regularidad proviene de shorts.
