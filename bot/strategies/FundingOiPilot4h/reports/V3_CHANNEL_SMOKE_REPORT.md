# V3 CHANNEL — smoke técnico
Fecha:2026-10-20. Estado: smoke finalizado; conciliación contable independiente pendiente de root.
[Sesión técnica](http://localhost:9200/#/backtest/cad4e9cd-a835-4a0b-afc6-5fb95749c1e4) sobre [2020-09-01,2020-09-08), 7d, duración motor10.96s. No screening económico ni cambio de parámetros.

## Verificación alcanzada
- Config nominal versionada: 10000USDT,isolated3x,fee0,00045,slip0,funding histórico ON,OI histórico configurado pero gateapagado,warmup240,debugtrue,benchmark/exportfalse.
- 47checks del sector y28checks de base ejecutados y aprobados dentro del smoke antes del primer before.
- 42decisiones4h,4buckets,2entradas (long/short). Un cierreSTOP previo a auditoría y un cierre forzado posterior al borde concilian2trades finales.
- Diez reemplazos de stop favorables en la posición short, siempre en cierres4h posteriores a la entrada; candidato recomputado de HWM/LWM y3ATR. No aflojar ni aplicar el nuevo umbral retrospectivamente.
- Ventanas126barrasfeatures y15ATR cerradas, protección inicial2ATR desdefill,sinTP yqty/riesgo/capC verificadas con procedencia de cada entrada.
- Logs completos58entradas; máxima línea995caracteres. Archivo técnico AUDIT_ResearchV3ChannelSmoke4h.json preserva marcadores y validaciones.
- Fuente inmutable congelada por root antes del resultado, en V3_IMPLEMENTATION_SOURCE_20261020.md/REGISTRY_V3.json. No se modificó tras ver rentabilidad.

## Cobertura no alcanzada
No se ejecutó salida por holding42barras, cruce inmediato de nuevo trailing ni entrada con gatePOI activo. Sus cálculos tienen checks puros/basefakes, pero no afirmar integración real de esas ramas a partir de este smoke.
La conciliación ledger/fees/wallet final la hará root con snapshot completo vía run_analysis; este agente no inició jobs propios ni leyó storage/DB.
El primer stop registró pérdida real superior al presupuesto2%; esos extras no se borran ni se redimensiona retrospectivamente. Se conserva el log loss_over_budget y se conciliará su composición.

## Incidente y cierre
run_backtest devolvió HTTP9000 readtimeout10s. Se preservó respuesta raw completa y se consultó el mismoID hasta estadofinished, sin repetirarranque. El progreso exclusivo es V3_CHANNEL_PROGRESS.json.
No se usó PNL de estos7d para elegir reglas; no se creó otra ventana para forzar casos. No screening,2024–2025,2026,ML,cuentas,Pi,live/paper,instalación o reinicio. Esperar GO root para screening.
