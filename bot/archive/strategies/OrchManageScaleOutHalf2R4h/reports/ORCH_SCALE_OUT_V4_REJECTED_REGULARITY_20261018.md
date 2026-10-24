# Scale-out 50% a 2R — cierre de regularidad
Dashboard: http://localhost:9200/#/backtest/0c6cfad7-c5da-465d-a45e-7009d284a1ec
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Restricciones y único cambio
BTC/PAXG/SPY 4h, longs en los tres y shorts BTC; 10k, 5x aislado, fee 0.00045 por lado incluso LIMIT; riesgo inicial 3%/8%, asignación original. Desarrollo 2020-10-15 a 2025-12-31 exclusivo; 2026 reservado.
Un único parcial de aproximadamente 50% a 2R (redondeo al lote de investigación), resto con trailing original. Protocolo previo ORCH_SCALE_OUT_HALF_2R_PROTOCOL_20261018.md. Sin parrilla de porcentaje/R.
## Resultado técnico y económico
222 trades (97 long / 125 short), neto +20,028.773774 USDT, CAGR 23.478932%, DD del motor −9.958176%, Sharpe 1.357390, fees 3,986.159163 USDT, 0 posiciones terminales.
Las aserciones de cantidades y salidas no detectaron errores.
## Auditoría independiente V4 por ejecuciones
El orquestador verificó cada fill, fees, PnL y saldo final. V4 reprodujo previamente los resultados V3 de estrategias sin parciales con tolerancia de retornos 1e-9.
- Meses activos positivos: 35/61 = 57.3770%.
- Meses positivos sobre todos los períodos: 35/63 = 55.5556%.
- Trimestres positivos: 14/21 = 66.6667%.
- Peor mes: −5.529%.
- Drawdown de cierres diarios UTC: −9.9515%.
Referencia: 33/61 meses y 15/21 trimestres. El parcial mejora dos meses, pero pierde un trimestre.
## Decisión y límites
DESCARTADA como solución de regularidad: no alcanza 65–70% de meses / 80% de trimestres, ni mejora simultáneamente ambas medidas frente a la referencia. Conservar solo como comparador de menor drawdown; no barrer objetivos o porcentajes para rescatarla.
Se mantiene la referencia. No se cambia framework, live, datos ni 2026. Proxy SPY, PAXG Spot y realismo de fills/funding siguen pendientes. Menor drawdown histórico no certifica ejecución real.
