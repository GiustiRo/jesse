# V6 C2 — confirmación EFFICIENCY_P

[Evaluación](http://localhost:9200/#/backtest/2f500b89-0097-463f-b7c2-b3e1df4deca9), 2024-07-01→2025-01-01, cuenta independiente de10.000USDT. Elegibilidad y selección fijadas por el entrenamiento en SELECTION_V6_C2.json antes de crear/iniciar esta evaluación. El PNL posterior no modifica esa decisión ni el calendario individual.

Neto -8.176050%, N25, PF0.692828, DDmotor-15.328997%. Son retornos semestrales de cuenta reiniciada; no son CAGR de una cuenta2024–25 continua. La selección fue EFFICIENCY_P, sin otros finalistas V6.

Fullsnapshot financiero PASS: bruto−fees+funding, cantidades, precios de marca, reloj efectivo/raw, órdenes y saldo concilian; máximo error1.2732925824820995e-11USDT. Funding276eventos, proxy0USDT, settlement-48.33672887616885USDT, sinclasificar0USDT. La curva diaria es completa (185puntos) y cubre6meses.

Auditoría de ejecución PASS: 1104decisiones,25entradas y25cierres anteriores al resumen;0forzados posteriores. Motivos: {"efficiency_neutral":13,"stop-loss":11,"maximum_hold":1}. Ventanas26/25/25,ATR15,stop2,5ATR,floor8,cap1x,feesdeescenario ycuotaUTC correctos. Logs completos488líneas en3páginas,máximo1091caracteres. NoLIMIT/trailing ni reentrada enmisma decisión; los cierres de eficiencia son de estado posterior alfill.

Finanzas: V6_C2_EVAL_ACCOUNTING.json. Logs/planes/counters: V6_C2_EVAL_LOG_AUDIT.json yshards raw del manifiesto. Fuente ejecutable congelada; sin parámetros nuevos ni2026. Replay continuo, costes, vecinos y decisión final pertenecen a root después de completar los cuatrofolds.
