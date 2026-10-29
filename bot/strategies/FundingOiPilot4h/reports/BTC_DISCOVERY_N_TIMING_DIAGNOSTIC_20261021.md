# Diagnóstico previo a composición N

Análisis ac045e27ac7a4c7d97bd6f2507771464 de snapshots completos:193operaciones A,102B y381F. No son muestras independientes ni universo de señales bloqueadas. No se sumaron PnL, equity o retornos para fingir una composición.

Dashboard A: http://localhost:9200/#/backtest/438b717c-7b5e-4589-a84a-687fa63f8645
Dashboard B: http://localhost:9200/#/backtest/62c90517-9034-4b34-91af-f77457895157
Dashboard F: http://localhost:9200/#/backtest/8b78a705-a8f3-4656-9705-e56300623ddf

A estuvo expuesta15,20% deltiempo, B52,53% yF30,03%. A/F se solaparon5,02% delcalendario; B/F15,40%.330entradasF realizadas estuvieron fuera de intervalosA;188fuera deB.119entradasA estuvieron fuera deF y60B fuera deF. Coincidencias de entrada al mismo cierre:12A/F y7B/F, todas de igual dirección en esos fills. La convención considera ocupado también el instante del cierre; no presupone reentrada en ese mismo cierre.

Estas cifras justifican preguntar por composición con capacidad real fija, pero no reconstruyen las señales que cada receta descartó estando ocupada. La trayectoria conjunta puede cambiar operaciones, saldos, cantidades, gestión por origen y funding. Es necesario un motor nuevo para esa política, no empalmar trades de los controles.

Decisión previa: registrar dos políticas de composición, A_FIXED+F y B_STATE+F, con señales/gestiones congeladas, una sola posición, conflictos simultáneos cash y acuerdos coalescidos una vez con origenCORE. No pesos, riesgo extra ni barrido de prioridades. La diferencia entre A/B ya era conocida y no se presenta como descubrimiento independiente; ambas composiciones se fijan antes de su economía. PresupuestoNpropio ysinretocarpadres. La selección de padres previamente positivos es retrospectiva sobre desarrollo ya examinado.

Las dos pueden fallar rentabilidad/regularidad: ambos mecanismos buscan continuación y no se presume diversificación. No basta ganar a un control. Conservar gatesr9 y M1medición; riesgo2%/6%/3x/costosbasefunding/slippage0. Los controles se reutilizan, incluyendo límites de DD/mensuales aproximados A/B; la nueva composición requiere su propia mediciónM1. No estrés ni2026nuevo. Detalles de datos/conteos/código en BTC_DISCOVERY_N_TIMING_DIAGNOSTIC_20261021.json.
