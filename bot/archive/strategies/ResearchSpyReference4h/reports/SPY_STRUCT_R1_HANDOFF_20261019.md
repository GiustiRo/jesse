# Handoff SPY — Structural R1 completada

Fecha:19/10/2026. Leer SPY_STRUCT_R1_RESULTS_20261019.md, protocolo congelado, MTM_SOURCE/RESULTS y STATE_QA de esta carpeta. Doce fulls nuevos terminados; seis BR y seis PB, sin ajustes por resultados. Sin nuevos jobs ni ronda2 iniciada.

Candidata de investigación: [BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810).
Dashboard: http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810

N16/net874.7959/fees150.5940/PF2.3203/Sharpe.7184/DDmotor−3.8005/MTMdiario−3.8053. Coste extra10bpsRT707.4692, sin mejor455.5145, sin3mejores−86.3560. Tiempo8.7875%. Sólo12/61meses completos positivos,9/19Q. Cohortes2022/23 negativas. Beneficio bruto ligeramente inferior aCq: mejora neta123.4481 se explica contablemente por ahorro de fees135.8815 y bruto−12.4334. No prueba causal ni promoción.

La regla salta primera oportunidad Cq después de reset en mitad inferior del canal26 PREVIO y permite siguientes hasta reset. Censura inicial. Cuenta antes de posición/cash/sizing. Fuentesautocontenidas SpyStructR1BR01..06 y SpyStructR1PB01..06; snapshots12/12 exactos y formularios/hiperparámetros verificados. Stop/BE/trail/ledger original. 37invariantes de estado pasaron mediante AST real.

Referencia vigente: [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639).
Dashboard: http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639

CqN31/net751.3477/DDmotor−5.2132; realmente24LIMIT+7MARKET automáticos. BR02 sólo comparte7entradas y tiene9entradas nuevas: no es quitar15trades conservando todo lo demás.

Todos BR rentables pero BR03/04/05/06 N10/7/4/4; no inferir robustez. Ningún PB superaCq; las3rentables se vuelven negativas sin mejortrade. No continuar mezclando filtros para rescatar los perdedores.

Siguiente pregunta discriminante: primeras vs posteriores oportunidades en episodios comunes, incluidas omitidas por ocupación. Después sensibilidad de reset con vecinos predeclarados sin seleccionar máximo. No volver aBTC/PAXG ni abrir2026 por esta evidencia; mantener riesgo1%,10k,fees.00045/side,SPY4h+M1,calendariooriginal,5xaislado,cap4.4,2020-10-15→2025-12-31 exclusiva. Sin funding/datosnuevos/live/framework/restarts/instalaciones/research_scripts. Ventana sigue siendo desarrollo reutilizado.

Informe PB final: strategies/SpyStructR1PB01/reports/SPY_STRUCT_R1_PB_FINAL_REPORT_20261019.md. BR final y exactos por su especialista en esta carpeta. Las fuentes y análisis completos se preservan en informes. Los errores técnicos de salida de análisisPB no alteraron estrategia ni repitieron fulls.
