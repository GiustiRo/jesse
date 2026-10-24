# SPY LAST RESET — protocolo fijo previo a resultados

Última ronda humana autorizada: seis controles de estabilidad de BR02, sin R3 ni extra-runs. No nuevas ideas independientes ni optimización. Fuente base inmutable en SPY_LAST_RESET_BASE_SNAPSHOT_20261019.md. Root confirma instruccionesDOCS/AGENTS/skills sin cambio y contrato1% autorizado; acceso proyecto exclusivamente MCP, sin fallback aFS/SQL/red.

| ID | Clase | Único cambio del reset |
| --- | --- | --- |
| RESET01 | SpyLastReset01 | Canal del reset20 en vez26. |
| RESET02 | SpyLastReset02 | Canal del reset32 en vez26. |
| RESET03 | SpyLastReset03 | Threshold low+.4*(high-low) en lugar midpoint.5, canal26. |
| RESET04 | SpyLastReset04 | Threshold low+.6*(high-low), canal26. |
| RESET05 | SpyLastReset05 | Dos cierres filtrados observados consecutivos<=midpoint26; cada cierre contra su propio canal26 PREVIO. |
| RESET06 | SpyLastReset06 | close<=EMA20 actual conocida sobre signal_candles en vez midpoint26. |

En RESET01/02 sólo n LOCAL del bloque reset cambia: Donchian de ENTRADA sigue26. En RESET03/04 sólo fracción de reset cambia. RESET05 cuenta observaciones retenidas, offsession no rompe ni cuenta; no se imputan barras ausentes. before sólo actualiza si signal_candles[-1].time==closed_candle_open_time; reset no requiere quoteM1fresh ni ventanaentry, igualBR02. Cada observación existente que NO cumple below reinicia racha0; la segunda y siguientes consecutivas below reinicianepoch_count0. Contador/below/ordinal evolucionan estando ocupado. RESET06 usa la misma llamada EMA20 de ta.ema(signal_candles,period=hpema_fast) ya presente, sin nuevo gate al origen; conserva guard de historia de reset26+1, suficiente paraEMA20.

Ordinal>=2, censura hasta primerreset observado, origenCq antescapital/posición, entryLIMITcanal26 y todos los otros filtros/gestión/sizing/fresh/cancelación EXACTOS aBR02. Stop2ATRdesde fill,BE2.25R,trail4.2/tightening fijos. Sóloreset alterado, no nuevas puertas de entrada/horario.

Mismo contrato:2020-10-15→2025-12-31exclusiva,2026cerrado;10k/riesgo presupuestado1%/fee.00045porladoinclLIMIT/5xisolated/cap4.4/cartera8%/margin90%/reserva.001sólosizing/step.001. SPY4h+M1,warm240,fast/debugfalse,UTCMon-Fri00–20features/baropen00–16entry. ProxySPXCFDBID/10aceptado,fundingfuera. Sin datasets/framework/install/scripts/restarts/PAXG/BTC/live/Pi.

Fuentes autocontenidas, readback/diffs y aprobaciónroot ANTESrun. Títulos SPY LAST RESET01..06, snapshot completo en notes antes iniciar. Máximo2backtestspropios/4globales y1análisispropio/2globales. ReferenciasCq/BR02 existentes SINrerun.

Auditoría8inputs snapshotscompletos:6controles+2refs. Fees/cantidad/PnL/wallet/terminales ytipos,PF/Sharpe/DD/CAGR,N,exposición temporal ynotional×tiempo a precioentry(NO MTM),turnover/netnotional,stressestático5/10bpsRT,exbest/ex3 ycohortesdecierre NOretornosMTManuales. RootMTM. ResúmenesJSON<50KB ypares/filas íntegros pequeños. Reportar TODAS las variantes; iguales son equivalencias de trayectoria, no confirmaciones independientes. No elegir máximo ni rebajarcriterios para rescatar vecina, no nuevosfulls al cierre.