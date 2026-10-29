# Auditor de calendario v3: método y límites
Implementación solicitada por el handoff: research_scripts/monthly_auditor_v3_mtm.py. Para analizar sesiones, su código se pasa inline a run_analysis; no se ejecuta como research job ni lee fuera de inputs/. Solo escribe en output/.

## Corrección
La curva del motor se muestrea aproximadamente00:01. Su último punto dentro del mes es el comienzo del último día, no su cierre. El auditorv2 no permite afirmar cierres mensuales exactos. Los resultadosv3 sustituyen esas cifras; no cambian los trades ni la rentabilidad final del motor.

El candidato [combinado](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) tiene63 meses de calendario,61 activos;52.3810% positivos sobre todos,54.0984% sobre activos y71.4286% trimestres positivos. Peor mes agosto2021 -7.0210%; peor trimestre2023Q3 -4.2364%. DD al cierre diario -14.8784%, diferente de DD Jesse -14.8905% por instante de muestreo.

## Reconstrucción reproducible
Las curvas benchmark buy-and-hold almacenadas en el [control STOP](http://localhost:9200/#/backtest/2e943276-7815-4280-96c8-d634d2dab817) contienen precios de cierre diario reescalados. Solo se usan sus benchmarks, no su rendimiento de estrategia afectado por el antiguo bug de margen.
Se recupera la escala de cada símbolo con ejecuciones MARKET al cierre diario/midnight de otros snapshots; al menos2 anclas independientes por símbolo y coincidencia relativa1e-8. Se observaron errores inferiores a2e-15, escalasBTC1.1502,PAXG0.192288,SPY0.03484346. Los conteos de anclas dependen de las sesiones incluidas: auditor principal29/12/15.

Se reconstruye el PnL acumulado por ruta: PnL de trades cerrados más qty firmada*(precio observado de cierre-entry) menos comisión de entrada en posiciones abiertas. Coste calculado según fee_rate guardado en cada sesión y ejecución real. Cotización anterior se arrastra por cierres de mercado solo para valoración; no se fabrican velas negociables.
La barra diaria se etiqueta por su día de apertura y cierra a la medianoche siguiente; se incluyen ejecuciones hasta esa frontera (convención derecha inclusiva). Los períodos parciales inicial/final se conservan explícitamente: finish_date2025-12-31 es exclusivo.

## Invariantes y autocontroles
- Identidad de comisiones qty*(entry+exit)*fee_rate y PnL por trade.
- PnL terminal por ruta y saldo final exactamente reconciliados.
- Suma de contribuciones por ruta igual al retorno de cada mes del portafolio.
- Exige una entrada y salida completas y cartera final plana. Rechaza piramidado/parciales, anclas insuficientes, datos no reconciliados y posiciones terminales abiertas.
- Autocontroles sintéticos: posición abierta cruzando mes, comisión, ejecución justo a medianoche y cartera vacía. Todos pasaron en job fb321e7f2f9543f5a98d7b792f3cbdd9.
- Drawdown incluye capital inicial como primer máximo.

## Correlación: dos medidas distintas
Contribuciones mensuales MTM reales de la cuenta compartida (divididas por equity global al inicio del mes): BTC/PAXG -0.03876;BTC/SPY +0.00425;PAXG/SPY -0.11356. No son retornos de tres cuentas independientes.
Los precios subyacentes tienen correlación mensual BTC/SPY +0.53793, BTC/PAXG -0.04727 yPAXG/SPY +0.04197 (62observaciones, último mes parcial). No confundirlas. Las correlaciones MTM por subperíodo son inestables; no garantizan cobertura futura.

## Alcance
Diagnóstico de esta estrategia simple sin parciales ni terminal abierta, no sustituto general del motor. No mide el peor DD intradiario, funding, spread, impacto o paridad con futuros nativos. 2026 no se evaluó.
