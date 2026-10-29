# V6 C1 — confirmación EFFICIENCY_P

[Evaluación](http://localhost:9200/#/backtest/33180680-9dd0-44f1-a7a5-6fcf4ba0c363), 2024-01-01→2024-07-01, cuenta independiente de10.000USDT. Elegibilidad y selección fijadas por el entrenamiento en SELECTION_V6_C1.json antes de crear/iniciar esta evaluación. El PNL posterior no modifica esa decisión ni el calendario individual.

Neto 9.207450%, N19, PF1.587940, DDmotor-11.898304%. Son retornos semestrales de cuenta reiniciada; no son CAGR de una cuenta2024–25 continua. La selección fue EFFICIENCY_P, sin otros finalistas V6.

Fullsnapshot financiero PASS: bruto−fees+funding, cantidades, precios de marca, reloj efectivo/raw, órdenes y saldo concilian; máximo error1.4551915228366852e-11USDT. Funding256eventos, proxy0USDT, settlement-192.15221103810347USDT, sinclasificar0USDT. La curva diaria es completa (183puntos) y cubre6meses.

Auditoría de ejecución PASS: 1092decisiones,19entradas y19cierres anteriores al resumen;0forzados posteriores. Motivos: {"stop-loss":5,"efficiency_neutral":13,"maximum_hold":1}. Ventanas26/25/25,ATR15,stop2,5ATR,floor8,cap1x,feesdeescenario ycuotaUTC correctos. Logs completos425líneas en3páginas,máximo1089caracteres. NoLIMIT/trailing ni reentrada enmisma decisión; los cierres de eficiencia son de estado posterior alfill.

Finanzas: V6_C1_EVAL_ACCOUNTING.json. Logs/planes/counters: V6_C1_EVAL_LOG_AUDIT.json yshards raw del manifiesto. Fuente ejecutable congelada; sin parámetros nuevos ni2026. Replay continuo, costes, vecinos y decisión final pertenecen a root después de completar los cuatrofolds.
