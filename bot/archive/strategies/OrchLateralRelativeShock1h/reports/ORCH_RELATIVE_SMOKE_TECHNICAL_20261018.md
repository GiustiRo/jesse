# Smoke técnico: dos piernas de shock relativo

[Control técnico](http://localhost:9200/#/backtest/f126ccee-4614-4146-b596-8a838caee863),2020-10-15→2020-11-01exclusivo,normal,benchmark=True,mismos parámetros del protocolo completo. Elegido para verificar implementación mientras ETH se importa; NO es muestra de validación económica ni selección temporal por resultado.

Estado finished,sin excepciones. 30legs=15baskets,15long/15short;0openfinal. Neto−77.7242USDT,fees50.0106; estas cifras se preservan pero no se interpretan como rendimiento esperado de la hipótesis.

AnálisisMCP754cbb4ebbdf4712a941acfa120290a1 succeeded. Cadaopened_at contiene exactamenteBTC/ETH conladosopuestos;identidadPNL=qty*sign*(exit−entry)−fee comprobada en30legs;terminalflat. Hedgeratio de notionalsETH/BTCobservado0.49610–0.76377. Esto no reconstruye independientemente la betaOLS; la causalidad96+3 y cotas de sizing están en código e invariantes.

## Desfase de cierre real, no atomicidad
14baskets tienen cierres simultáneos. Uno tuvo STOPemergenciaETH y BTCcerró2880segundos(48min)después, enel próximo ciclohorario. Máximo ysumadeperiodoshuérfanos observados=2880s. Es la limitación planificada de estrategia1h, no un filldoble atómico ni cobertura continua. Stop3ATRdecontrapierna permaneció activo;gaps/outagespuedensuperarri esgoplanificado. El basket correspondiente neteó+13.8362,pero el signo favorable no elimina ese riesgo.

No apareció entrada parcial/huérfana inicial en esta muestra; eso no demuestra manejo de rechazo realexchange ni prueba todos los caminos de fallo. Control no usó inyección artificial de fallos. Historiales exigieron timestampidénticocontiguo; no se relajaron guards ni cambiaron parámetros para conseguir operaciones.

ETHimport03565c0b-635f-4d7d-8055-61237d918b5a sigue en curso; aúltimocontrol6.8%,2021-01-15. Full original detenido por missingETH se conserva. Esperar importación terminal para crear nuevo full benchmark=True y evaluar2020-2025;noabrir2026. SLOT2liberado tras smoke. Referenciaintacta;sinframework/live/Pi.