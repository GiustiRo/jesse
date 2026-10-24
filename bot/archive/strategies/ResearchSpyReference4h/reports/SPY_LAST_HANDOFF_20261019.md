# Handoff — cierre de la última exploración SPY — 19/10/2026

Leer primero SPY_LAST_RESULTS_20261019.md. La petición humana fue una última ronda de ambos agentes y reporte al terminar. Se completaron doce fulls predeclarados (seis RESET, seis MECH), sin adaptación ni rondas posteriores. Todos finished y rentables con comisiones base y10bpsRT extra estático. Nueve caminos diferentes entre las doce implementaciones; no son muestras independientes.

## Candidatas congeladas para validación futura

[MECH01](http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592)

Dashboard: http://localhost:9200/#/backtest/527a0334-d067-4662-8252-6949b8bf1592

Clase SpyLastMechanism01. Sólo segunda oportunidad Cq tras reset midpoint26 previo, con censura inicial, conteo antes de ocupación/sizing y gestión BR02 intacta. N12/net1179.9816/PF4.0445/Sharpe1.0083/DDmotor−2.4867%/MTM diario−2.5324%, tiempo8.1308%. Coste extra10bpsRT1054.2890; sin3mejores200.1304. Diagnóstico conjunto POSTHOC ex3+10bpsRT105.6235 sobre nueve trades restantes. Cohortes por cierre y MTM anual positivas salvo2022. Candidata prioritaria por eficiencia/concentración; no promovida.

[MECH05](http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862)

Dashboard: http://localhost:9200/#/backtest/9205534b-372c-4aea-844a-a119d56cf862

Clase SpyLastMechanism05. Ordinal>=2 BR02, entrada a mercado actual antes de sizing en vez retest. N19/net1275.1636/PF2.6548/Sharpe.8824/DDmotor−3.5693%/MTM−3.5743%, tiempo11.4133%. Coste extra10bpsRT1075.5958; sin3mejores31.5144; combinado−136.1341. Alternativa por neto, más concentrada. Incluye forcedterminal−70.01net conciliado. No promover ni eliminar cierre terminal.

MECH06 inicio de racha es positiva962.21/N12, pero diagnóstico conjunto−42.40. No seleccionada por encima de las dos anteriores.

## Estabilidad y equivalencias

RESET01/04 idénticas864.02; RESET02/03 idénticas781.90; RESET05=MECH04=BR02 idénticas874.80. RESET06 EMA20 diferente657.85. Vecinos de reset sobre BR02, no sobre MECH01/05: interacción aún no ensayada. Todas RESET negativas sin tres mejores y negativas en cohortes2022/23.

Cq referencia originalN31/net751.35/DDmotor−5.21; BR02N16/net874.80/−3.80. Mantener fuentes e historial intactos. MECH01 yMECH05 mejoran retrospectivamente, pero N pequeño y muchas búsquedas previas. No hay validación limpia. No sumar trades ni PNL de variantes como cartera.

## Contrato y límites persistentes

10.000USDT, riesgo1%, fee.00045 por lado, isolated5x/cap4.4, reserva.001 sólo sizing. SPY4h+M1/warm240/fastdebugfalse y calendario UTC original. Stop2ATR/BE2.25R/trail4.2/tightening original. 2020-10-15→2025-12-31 exclusiva. 2026 permanece reservado. Sin datos nuevos, funding, BTC/PAXG, instalaciones, framework/configglobal, reinicios, live/paper/Pi o research_scripts.

Root verificó doce snapshots/formularios y ocho hiperparámetros por sesión. QA113assertions de AST real passed; no es evidencia económica. Auditorías especialistas de fills/qty/fees/PNL/wallet/terminales y MTM de las doce conciliadas. Todos los análisis succeeded; no fulls pendientes. Fuentes y resultados exactos preservados por agente.

## Próxima fase

Cerrar exploración de SPY con MECH01 prioritaria y MECH05 alternativa congeladas para validación futura. No continuar buscando combinaciones sobre la misma historia para justificar promoción. Cualquier prueba limpia debe definirse antes de mirar el periodo y requiere decisión explícita sobre usar2026. Esta tarea no abrió2026 ni inició BTC.

Informes centrales:
- strategies/ResearchSpyReference4h/reports/SPY_LAST_RESULTS_20261019.md
- SPY_LAST_FROZEN_PROTOCOL_20261019.md
- SPY_LAST_STATE_QA_20261019.md
- SPY_LAST_MTM_SOURCE_20261019.md
- SPY_LAST_MTM_RESULTS_20261019.md
- SPY_LAST_COMBINED_STRESS_20261019.md

Informe MECH: strategies/SpyLastMechanism01/reports/SPY_LAST_MECHANISM_FINAL_REPORT_20261019.md. Exactos, ocho auditorías y fuentes de análisis en esa carpeta. RESET exactos y auditoría en ResearchSpyReference4h/reports; final del especialista por separado.
