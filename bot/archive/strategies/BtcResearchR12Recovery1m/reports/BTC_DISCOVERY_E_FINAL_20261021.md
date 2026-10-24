# Tanda E cerrada: ninguna candidata

BTC-USDT Binance Perpetual Futures, [2020-10-15,2026-01-01), desarrollo reutilizado. Riesgo2%/6%/3x,10k,fee.00045 porlado+funding aplicado/verificado con proxies declarados; slippage0, sin estrés.

## BtcResearchR12Kalman1m
Dashboard: http://localhost:9200/#/backtest/9a7ce958-13d0-481e-992d-401e03b579fd

CAGR -13.3487%; neto -5264.05USDT; PF 0.8941; Sharpe -0.6241; DD M1+eventos 62.8177%; 1200 trades; meses activos positivos 25/62; trimestres 8/20. Mediana calendario -0.6019%; neto sin mejores2 meses -6366.87USDT. NO_CUMPLE: retorno, PF y regularidad; Kalman también DD y mediana/concentración. Recovery falla concentración.

## BtcResearchR12Recovery1m
Dashboard: http://localhost:9200/#/backtest/ce148b26-9a50-4ef9-9874-a784a9067c4e

CAGR 2.8942%; neto 1604.79USDT; PF 1.0924; Sharpe 0.2883; DD M1+eventos 16.7839%; 167 trades; meses activos positivos 34/60; trimestres 11/20. Mediana calendario 0.5330%; neto sin mejores2 meses -335.76USDT. NO_CUMPLE: retorno, PF y regularidad; Kalman también DD y mediana/concentración. Recovery falla concentración.

Transferencias explícitas de mecanismos PAXG, no validación independiente ni receta inventada. Protocolo E y fuentes/manifiesto guardados antes de economía. Cierre presupuesto dos corridas, cero reemplazos económicos/técnicos. Sin rescatar vecinos ni retirar shorts posthoc. El canal fallido se retiró antes por duplicación ORCH.

Checks previos finales job80186308c07a431d9e5a695642bb7260: passed. Primer check de harness reparó igualdad exacta exp(logprecio) a isclose; revisión independiente retiró guarda de target2R ficticia de Kalman antes de economía. Fuente final hash7362803d217fa5f9244a4c0bcc174585e6fca0f139e94a8262cfb6e75913a9b0, verificado en el check final y manifiesto antes de economía. No cambio económico posterior.

Auditoría job4eb2134c9dd34ca88619b96843619adf: snapshots completos1200/167trades, bruto-fees+funding=PNLsum=finishing-10k, error<1e-6. Telemetría M1 completa63intervalos/62meses/20Q, suma mensual y equityfinal reconciliadas. DD muestreadoM1yfills, no extremosintraminuto. Fronteras postfunding/predecisión según contratoR11.

Kalman metadata total_open_trades=1 es contador preterminal; FINAL y trades completos incluyen liquidación del motor y su comisión. No tratarlo como posición operativa real ni restar dos veces PnLabierto. Configuración global/framework intactos.

Objetivos r9 no alcanzados, ninguna seleccionada. Continuar autónomamente con otra pregunta material; F ya se registró sin usar los resultados E para definir sus reglas.
