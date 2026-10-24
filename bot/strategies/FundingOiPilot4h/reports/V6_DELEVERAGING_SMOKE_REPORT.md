# V6 Deleveraging — smoke técnico aprobado

Dashboard: http://localhost:9200/#/backtest/a4264bf1-b86f-42f8-b356-f7d1a9cf17cf

Sesión técnica de siete días, BTC-USDT4h, 2020-09-01→2020-09-08. Configuración nominal exacta verificada antes de inicio; fuente congelada. Una solicitud de arranque devolvió HTTPread10stimeout; lectura del mismo ID confirmó running y luego finished, sin reintento ni duplicado.

Pasaron70checks del sector y67comunes. Los logs completos incluyen42decisiones,3entradas long y3cierres:2stops y1maximum_hold exactamente48h desde fill. Se verificaron cantidadfloor8,riesgo2%+fees,cap1x,ATR15OHLCactual,stop2A ytarget4A desde fill,cuotaUTC,fundingasof,OIregla declining explícita conratio/ref24h ylas particiones de causas. La variante smoke esP yuse_oi=false: no ejerció el gate económicoPOI aunque su contexto/provenance declining sea correcto. Máxima línea1108<1900.

FundingON procesó21settlements y8cashflows proxy, total−3,9944745549USDT; validación contable financiera completa corresponde al análisis central de root. El nominal técnico terminó con3trades,neto−4,3289966%,DD−4,3557192%,Sharpe−7,8561307, duración de motor1,36s. Estas métricas semanales no seleccionan parámetros.

No hubo fillshort,target,calendar ni cierre final forzado; no se acredita cobertura real de esas ramas. Se instaló target2R según intención/logs pero ningún objetivo se ejecutó. Las pruebas deterministas cubren comparaciones OI y prioridades de reloj; el smoke no las convierte en evidencia económica.

Fuentes sin cambios. No se crearon screenings, jobs analíticos ni otros motores. Auditoría y logs/trades completos enAUDIT_ResearchV6DeleverageSmoke4h.json; prerun, config, rawtimeout y recuperación enV6_DELEVERAGING_PROGRESS.json. Próximo paso: GO central después de todas las pruebas técnicas, manteniendo2026cerrado yel protocolo inmutable.
