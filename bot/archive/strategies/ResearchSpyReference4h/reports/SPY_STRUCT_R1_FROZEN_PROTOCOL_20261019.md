# SPY estructural, ronda1: protocolo final previo a resultados

Fecha local: 19 de octubre de 2026. Se ejecutarán los doce escenarios preparados, seis por especialista. La etapa anterior sólo dejó planes; no tenía resultados económicos. Esta ronda produce esos resultados antes de decidir si corresponde continuar.

## Matriz fija

| ID | Política |
|---|---|
| BR01 | Primera señal Cq calificante de episodio tras cierre en mitad inferior del canal26 previo; retest original |
| BR02 | Señales Cq posteriores a la primera del mismo episodio; retest original |
| BR03 | Primer retest real de techo congelado que cierra encima; MARKET actual |
| BR04 | Primer retest real cierra debajo/igual y posterior barra recupera techo; MARKET actual |
| BR05 | Mismo hold de BR03; compra futura en máximo de vela de retest |
| BR06 | Mismo hold de BR03; compra futura en máximo de ruptura original, MARKET actual si ya superado |
| PB01 | Dos velas rojas con cierres descendentes, seguida de giro alcista que supera cierre previo; MARKET |
| PB02 | PB01 más cierre por encima del máximo previo |
| PB03 | Inside bar tras corrección descrita en propuesta, cierre por encima del máximo inside; MARKET |
| PB04 | PB03 más recuperación del máximo de vela madre |
| PB05 | Low actual barre mínimo de3velas previas y cierre lo recupera; MARKET |
| PB06 | PB05 más cierre por encima del máximo previo |

Reglas exactas PB preservadas en SPY_PULLBACK_PLAN_PROPOSAL_20261019.md; las seis mantienen filtros EMA20/80, pendiente EMA80[-5], ADX26, RSI52–76, rango4h<=3ATR e historia100, sustituyendo sólo Donchian y distancia al canal por patrón. MARKET al cierre conocido con quote M1 fresca; distancia0<2ATR<price.

BR01/02 cuentan señales de precio/regímen/historia/entrywindow/fresh, antes de sizing, capital o posición. Midpoint usa máximo y mínimo de26velas PREVIAS. Inicio censurado hasta primer reset observado; contar aun ocupado y consumir ordinal sin replay.

BR03–06 comparten generador causal de episodios independiente de ocupación. Origen califica por precio/regímen/historia/ventana/fresh Cq, antes de sizing. Congelar techoL y highH del origen. Sólo un episodio activo durante cuatro observaciones4h FILTRADAS posteriores; armingbar no cuenta como retest. No sobrescribir niveles, rearmar en expirybar ni inferir16horas reales durante cierres. Contador avanza ocupado y fuera de entrywindow si la vela pertenece a historia filtrada.

Primer contacto observable exige low<=L<=high. Si la primera interacción low<=L tienehigh<L, se clasifica gap debajo: episodio inválido para triggers pero conserva bloqueo hasta expiry común. El primer touch decide hold o fracaso. ReclaimBR04 sólo en una barra futura al primer fracaso dentro de la vida original. Evento inválido, ocupado, sin ventana, sin régimen o sin quote se consume sin cola. Todos los episodios permanecen bloqueados hasta vencimiento común aun si una receta entra antes.

BR05/06 sólo colocan orden para futuro, sin rellenar al high ya ocurrido. Si el nivel ya está alcanzado se usa precio actual, no un LIMIT accidental. Smart-order puede convertir cercanía<=1,5bps a MARKET; conservar y registrar tipos efectivos. Orden pendiente vive una barra como referencia. ATR y sizing se calculan en la nueva decisión y stop desde fill efectivo; misma fórmula, exposición potencialmente distinta.

## Comparación y constantes

Referencias existentes, sin reruns adicionales:
- [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639), estrategia AttrSpyCqFreshLimit.
- [M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07), estrategia AttrSpyMarket.

Capital10.000USDT aislado/riesgo1%/fee.00045 por lado/isolated5x/cap4.4/sin piramidar/reserva.001 sólo sizing. Stop2ATR, BE2.25R, trail4.2 y tightening5R/8R originales, ledger y fórmula de cantidad preservados. Datos SPXCFDBID/10 aceptados para SPY; sin funding.

RutaSPY4h+M1, warmup240, fast/debugfalse. UTC Mon–Fri00–20 para historia y barras abiertas00–16 para entradas exactamente como base; gestión original fuera de horario también. Ventana2020-10-15→2025-12-31exclusiva.2026cerrado. No1h enR1, nuevos datos, instalaciones, research_scripts, PAXG/BTC, cambios de framework/config global, reinicios o live/paper/Pi.

Dos backtests simultáneos por especialista/cuatro globales mientras haya cola; un análisis por especialista/dos globales. Fuentes autocontenidas, readback/revisiónroot antes de correr y snapshots completos. Títulos comienzan SPY STRUCT R1. No alterar reglas tras resultados.

## Auditoría y decisión

Doce filas completas, incluyendo pérdidas o cero operaciones. N/neto/fees/PF/Sharpe/CAGR/DDmotor, duración, tiempo abierto, nocional-tiempo a precio de entrada, rotación, neto por nocional, costes estáticos5/10bpsRT, exbest/ex3 y cohortes por cierre claramente distintas de MTM anual.

Análisis por especialista: sus6variantes y2referencias, máximo8snapshots. Exportar resúmenes pequeños e íntegros, sin usar texto truncado. Root auditará cierres diarios UTC con el auditor validado, cuatro anclas históricas y hasta6objetivos por job;61meses/19Q completos y fronteras parciales aparte. Root verificará strategy_codes, formularios y parámetros registrados. Cierres terminales deben conciliar con wallet/open_pl, no prueban liquidez nativa.

Las comparaciones cambian selección, tamaño y ocupación: no son intervenciones sobre idénticas entradas. Patrones emparentados y caminos de la misma historia no son muestras independientes. Identificar trayectorias idénticas sin presentarlas como replicaciones.

Rondas2/3 siguen condicionadas a evidencia material; no consumir el techo33 por obligación, rescatar muestras pequeñas con umbrales adaptativos o seleccionar un máximo marginal. Historial2020–2025 sigue siendo desarrollo reutilizado. Ninguna promoción automática ni apertura2026.
