# Control de costes: reglas de decisión fijas
Extiende protocolo de atribución antes de ejecutar: congelar no solo distancia mínima short6*0.00045*entry, también breakevenlong entry*(1+2.5*0.00045). Código SIGNAL_FEE no optimizable. La comisiónreal de cada borrador sigue en self.fee_rate, usada paraPnl/fees/risk sizing/reservas.
Borradoresdebase.00045,+10bpsRT.00095,+25bpsRT.0017 por lado. Prueba base debe coincidir en trades,tamaños,métricas con referencia antes de interpretar estrés. Si no coincide, detener esta interpretación y diagnosticar.
Señales basadas en precios y umbrales no se adaptan al coste; tamaños y disponibilidad de capital sí. No se afirma que trayectoria/fills/trades permanezcan fijos. Comparar también con escenariospreviosadaptativos usando igualfee.
Ningún cambio a referencia ni configuración global. Mismos3activos4h,2020Oct15–2025Dec31exclusivo,5xisolated,10000,3%/8%riesgo.2026reservado.
No es simulación de spread,impacto,colas ni missedfills. No estimar robustez conjunta ni aprobarfase2 por estos controles.
