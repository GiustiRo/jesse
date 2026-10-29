# V3 — CHANNEL P fase C, nominal y robustez completa

Fecha de cierre: 2026-10-20T23:57:55.131Z.

La rama P terminó las seis sesiones nuevas autorizadas, una por vez. LAG1 reutiliza nominal por USE_OI=False. No hay motores P pendientes, no hubo reselección ni modificación de fuentes y el mínimo de 100 operaciones permanece congelado. El nominal tiene 95 operaciones: no se promueve, aunque sea positivo.

| Escenario | Trades | Neto | CAGR | DD absoluto | PF |
| --- | ---: | ---: | ---: | ---: | ---: |
| [NOMINAL](http://localhost:9200/#/backtest/16da36e2-2807-4a9b-85e3-51cf8fa67c75) | 95 | 38.225856% | 17.543463% | 18.413964% | 1.348511 |
| [S1](http://localhost:9200/#/backtest/e57473a7-8862-44cf-b0c2-3e1dfa9cded2) | 95 | 29.446182% | 13.754334% | 19.423694% | 1.271209 |
| [S2](http://localhost:9200/#/backtest/7a95e749-7b91-4b86-83d4-48707705ca8e) | 96 | 26.262996% | 12.348886% | 21.873266% | 1.231014 |
| [S3](http://localhost:9200/#/backtest/1b15432c-4119-4c6e-b88e-23d70e017755) | 97 | 7.500623% | 3.677378% | 24.083283% | 1.065084 |
| [N09](http://localhost:9200/#/backtest/4465ef39-bdcd-4f0c-8387-04879e7878cd) | 105 | 8.810139% | 4.306074% | 24.843384% | 1.073126 |
| [N11](http://localhost:9200/#/backtest/ec6feb7f-5ef5-422b-8c24-af2f102a3bb3) | 92 | 33.678674% | 15.596541% | 18.869020% | 1.330711 |

Todas usan BTC-USDT Binance Perpetual Futures 4h, [2024-01-01,2026-01-01), cuatro intervalos semestrales separados y los cuatro FORCE_BOUNDARIES. Balance inicial 10000 continuo, sin resets. Warmup240, aislado3x, funding histórico contable ON y datasets versionados. Fees/slippage exactos: nominal/N09/N11 .00045/0bps; S1 .0009/0; S2 .00045/5; S3 .0009/10. N09 sólo STOP1.8/TRAIL2.7; N11 sólo STOP2.2/TRAIL3.3.

Los tres wrappers se releyeron al cierre y coinciden exactamente con la creación congelada. Source SHA nominal 6682ccc3a8a5adbf8576130db1dfe0a97446b287fc67b8b52d1110da2b0eea9a; N09 dd3a308cd3372ed5ba8e29254ebc7b3fb9168572eabe02e326fd4c26a7f089f3; N11 926ec08db17bf4b2b798f33e9c60369003d3663ce37fd01ba1d7f77744de3f93. Root compiló/AST/hasheó antes de corridas, job93fc699d8de0433594ab56ce072c22d7.

Las seis auditorías de contadores/procedencia pasan: 4386 decisiones,24 meses,particiones primary/dirección, entradas=trades=cierres,0cierres posteriores al audit, entradas dentro de ventanas estrictas y config/calendario exactos. Cuatro bloqueos boundary_or_inactive por sesión. No hubo solicitud calendar_boundary en estas realizaciones porque estaba flat en los cierres; esa rama no queda cubierta por el replay. El harness estático previo la ejerció, sin afirmar integración por ese solo harness. Nominal/S1/S2/S3:4maximum_hold+1trailing_crossed;N09:1maximum_hold+5trailing_crossed;N11:5maximum_hold+3trailing_crossed.

S3 conserva ganancia reducida y N09 muestra una caída marcada respecto al nominal. Es evidencia de sensibilidad, sin selección del mejor vecino ni relajación de criterios. Estas métricas provienen de summary; root realizará conciliación contable completa de snapshots. Nominal ya fue conciliado centralmente con error máximo2.01e-11.

Incidente de ejecución: N09 run_backtest devolvió HTTPConnectionPool127.0.0.1:9000 Read timed out(read timeout10). Se preservó raw completo y se consultó el mismo ID hasta finished, sin retry/duplicación. También ocurrió un error local JS de scope antes de invocar creación; se corrigió sin crear sesión por ese intento.

Evidencia: V3_P_REPLAY_PROGRESS.json contiene config/IDs/URLs/rawantes-después, summarys y checks; AUDIT_ResearchV3ChannelPReplay4h_NOMINAL.json, AUDIT_ResearchV3ChannelPReplay_S1.json, _S2.json, _S3.json, _N09.json y _N11.json contienen buckets/provenance/logs relevantes. Fuentes completas/padres/readback en V3_P_REPLAY_SOURCES.json; escenarios en V3_REPLAY_SCENARIOS_FROZEN.json.

No se ejecutó run_analysis por esta rama en esta etapa. No datos2026 ni edición de fuentes nominales/framework/ambiente.
