# SPY última ronda — protocolo congelado antes de resultados — 2026-10-19

Hipótesis: la maduración de rupturas dentro de un ciclo podría conservar el beneficio bruto con menos rotación; la mejora BR02 debe resistir definiciones cercanas del reset y contrastes del ordinal. Se ejecutan exactamente doce variantes, seis por cada uno de dos agentes. No ajuste tras observar resultados, no ampliación automática de la ronda.

## Matriz fija

Todas derivan de SpyStructR1BR02, referencias existentes Cq y BR02, sin reruns.

| ID | Único contraste |
|---|---|
| RESET01 | Canal del reset20 en vez26 |
| RESET02 | Canal del reset32 en vez26 |
| RESET03 | Umbral reset low+.4*(high-low), en vez.5 |
| RESET04 | Umbral reset low+.6*(high-low), en vez.5 |
| RESET05 | Dos cierres filtrados consecutivos debajo/igual a su propio midpoint26 |
| RESET06 | Reset debajo/igual EMA20 en vez midpoint26 |
| MECH01 | Exactamente ordinal2 |
| MECH02 | Ordinal>=3 |
| MECH03 | Exactamente ordinal3 |
| MECH04 | Ordinal2 o3 |
| MECH05 | Ordinal>=2 original, entrada a precio actual MARKET en vez retest al techo |
| MECH06 | Ordinal>=2 contando y operando sólo el inicio de cada racha de barras Cq calificantes consecutivas |

Canal de entrada26 y filtros EMA20/80/ADX26/RSI52–76/rango<=3ATR quedan iguales. Censura hasta reset real observado. Contadores antes de posición/capital y sizing; ocupado no congela ni encola. Reset usa barras PREVIAS excluyendo actual; RESET05 considera dos observaciones retenidas cada una con su midpoint causal propio. Offsession no rompe ni cuenta y no se rellenan observaciones faltantes. MECH06 califica por _origin real, incluidos fresh/régimen/entrywindow; una barra filtrada no calificante rompe racha, offsession no interviene. Reset pone prev_eligibleFalse. Esto cambia unidad de oportunidad y se informará como contraste de definición, no un filtro sobre idénticos fills.

## Contrato constante

SPY-USDT 4h + M1, Binance Perpetual Futures como ruta de investigación/proxy ya aceptado; warmup240, fast/debugfalse. Ventana2020-10-15→2025-12-31 exclusiva, último día30/12;2026 cerrado. Capital10.000USDT, riesgo1%, comisión.00045 por lado todos los tipos, isolated5x/cap4.4, reserva.001 sólo sizing. Stop2ATR, BE2.25R, trail4.2, tightening5R/8R y ledger originales; sin piramidar. Original historia UTC Mon–Fri00–20 y entradas baropen00–16. Fresh M1 exacta T−60000 con precio conciliado. Orden pending una barra. No aumentar riesgo para igualar exposición.

Sin funding, nuevos datos, BTC/PAXG, research_scripts, instalaciones, framework/configglobal, reinicios o live/paper/Pi. Dos backtests simultáneos por agente/cuatro globales; máximo dos análisis globales. Fuentes autocontenidas y snapshots íntegros, revisión root antes de ejecutar.

## Evaluación previa

Comparar distribución de los seis vecinos, no elegir sólo máximo. Marcar caminos exactamente iguales como equivalencias, no confirmaciones independientes. Mostrar doce filas aunque negativas o sin operaciones. Neto/fees/bruto/PF/Sharpe/DDmotor/CAGR, N, exposición temporal y nocional-tiempo, costes estáticos5/10bpsRT, sin mejor/sin3mejores, cohortes por cierre. Auditoría órdenes/qty/fees/PNL/wallet/terminales; root MTM diarioUTC con61meses/19Qcompletos y parciales separados. Forzados terminales no acreditan liquidez. Verificar formularios/hp/snapshots contra fuentes.

Todas las variantes mantienen decisiones y ocupación endógenas: comparar fills no identifica por sí solo el efecto predictivo de primeras versus posteriores oportunidades. No inventar recuentos de señales omitidas ni afirmaciones causales que los snapshots no permiten. Esta ronda prueba implementaciones operables del mecanismo y sensibilidad; no reconstruye un estudio de oportunidades virtuales con outcomes futuros.

La historia sigue siendo desarrollo reutilizado. N16BR02 y muchas búsquedas previas hacen insuficiente una mejora aislada o máxima marginal. No promoción ni OOSlimpio por etiquetar esta ronda como validación. Concluir explícitamente si hay estabilidad defendible, sólo candidato exploratorio o si corresponde cerrar investigación SPY y conservar referencia. Preservar2026.

Referencias:
[Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639)
Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

[BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810)
Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810
