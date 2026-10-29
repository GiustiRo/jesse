# V6 EFFICIENCY: replay continuo nominal

El [replay nominal](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127) terminó y queda rechazado por los gates congelados. N=44, retorno 0.278594%, PF 1.006229, DD -17.553569% y CAGR 0.139010%. Falla PF≥1.2, N≥100, tres semestres positivos y CAGR≥15%; pasa retorno positivo y DD absoluto≤25%.

Capital inicial 10000; cierre 10027.85940464 USDT. Sólo los dos semestres de 2024 están activos y conservan bordes separados. Los doce meses de 2025 permanecen en efectivo. El diagnóstico positivo de C4 no cambia ese calendario. Hay 44 operaciones, 16 stops, 26 salidas por eficiencia y 2 por tenencia máxima; cero cierres forzados.

Auditoría financiera del snapshot completo PASS, error máximo 9.094947017729282e-12; financiación -244.939517 USDT en 532 eventos con marca exacta, comisiones 235.338240 USDT. Auditoría de logs PASS (1004 aserciones), 4386 barras y 24 meses; comprueba capital continuo por entrada, calendario, ventanas de 26/25 cierres, riesgo, UTC, stops y ausencia de TP.

Evidencias: V6_REPLAY_NOMINAL_ACCOUNTING.json, V6_REPLAY_NOMINAL_LOG_AUDIT.json y shards de logs/operaciones referenciados allí. Las pruebas de costes y vecinos siguen completas pese al rechazo nominal; ningún escenario puede rescatarlo.
