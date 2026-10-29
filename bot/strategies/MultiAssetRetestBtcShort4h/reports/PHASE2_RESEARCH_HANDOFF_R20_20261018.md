# Continuidad después de veinte exploraciones R20

Leer primero R20_SPY_PAXG_RESEARCH_RESULTS_20261018.md en esta carpeta y los handoffs anteriores. No sustituye la historia previa.

## Estado verificado
Veinte primarias R20 terminadas: diez SPY y diez PAXG, todas finished y sin errores. SPY: cuatro positivas, cuatro negativas, dos sin operaciones; PAXG: diez negativas. Ninguna mejora operativa aceptada. Referencia y BTC congelados, 2026 sin consultar. Las veinte fuentes actuales coinciden exactamente con strategy_codes de sus sesiones. Formularios y summaries verificados por root. No quedan backtests de R20 ejecutándose.

SPY02 pasa apenas cribado pero depende de su mayor ganador y pierde MTM en 2024/2025. SPY03 tiene solo25operaciones y concentración. No se integraron ni se recortaron por dirección. PAXG03/06/07/08/10 tienen menos de30trades; su resultado negativo no demuestra ausencia general de efecto. No relajar disparadores para fabricar muestra.

## Auditoría y artefactos
SPY: informes SPY20_FINAL_RESULTS_20261018.md y SPY20_METHODOLOGICAL_REVIEW_20261018.md bajo strategies/ResearchSpyReference4h/reports/. Dos auditorías MTM root en esta carpeta, R20_MTM_SPY_BATCH1_20261018.md y R20_MTM_SPY_BATCH2_20261018.md. Ocho recetas con operaciones conciliadas a cierre diario UTC, no usar Portfolio00:01 como cierre.

PAXG: matriz y revisión en strategies/ResearchPaxgWeekendReturn1h/reports/R20_PAXG_TEN_EXPERIMENTS_PROTOCOL_20261018.md y R20_PAXG_IMPLEMENTATION_REVIEW_20261018.md. Auditorías de snapshots en jobs5dba914705be496b8fce366a8cb0d72d y a703e1e367cf4d868defe61e9dc17a7c, ambas succeeded. Primer informe guardado en strategies/R20PaxgARResponse4h/reports/R20_PAXG_BATCH1_AUDIT_20261018.md. Concilian fees, cantidades, PnL y wallet; cohortes de cierre no son MTM.

## Nueva autorización R40
Usuario pide otros veinte escenarios exploratorios, con ideas fuera de la caja, nuevos indicadores, lecturas de precio y combinaciones de timeframes. Inferencia de reparto coherente con etapa anterior: diez SPY y diez PAXG. Se reutilizan especialistas /root/spy_research y /root/paxg_research. IDs SPY40-01..10 y PAXG40-01..10; clases R40Spy... y R40Paxg...; matrices y revisión root antes de código y ejecución.

Conservar contrato10kUSDT,1%riesgo planificado,fee0,00045porlado,5xaislado,4,4xnocionalbruto, sin piramidado. Reserva de sizing no es slippage simulado. Desarrollo2020-10-15 a2025-12-31exclusiva. Proxy aceptado, sin funding, nuevos datos, BTC,2026, scripts de investigación, instalaciones o live/paper. Dos backtests por agente/cuatroglobales; un análisis poragente/dosglobales.

R40 no cuenta sensibilidades o controles como ideas nuevas. Declarar mecanismo, información adicional, reglas completas y frecuencia esperable cualitativa antes de resultados. Evitar repetir familias descartadas con otro indicador o usar condiciones que previsiblemente no produzcan muestra. No garantiza mejora; todo2020–2025 sigue siendo desarrollo seleccionado. Guardar pérdidas y ceros y no avanzar de fase sin evidencia.

Cierre PAXG verificado por root: informe strategies/R20PaxgARResponse4h/reports/R20_PAXG_FINAL_20261018.md, última auditoría R20_PAXG_BATCH2_AUDIT_20261018.md y fuente R20_PAXG_ANALYSIS_SOURCE_20261018.md, en esa misma carpeta. Son 3.362 trades primarios y95comparativos conciliados, diez resultados negativos. Hay cuatro DD peores que−25% (01,02,04,05); corrección del informe confirmada. El protocolo global de la nueva tanda está en R40_SPY_PAXG_STAGE_PROTOCOL_20261018.md en esta carpeta.
