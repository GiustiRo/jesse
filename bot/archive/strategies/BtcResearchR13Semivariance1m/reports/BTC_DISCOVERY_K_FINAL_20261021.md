# Tanda K: semivarianza con una operación, sin candidata

Dashboard: http://localhost:9200/#/backtest/823a2c19-0f0c-49f3-8ae8-8aeb34e2af66

La transferencia BTC produjo una sola operación ganadora. No cumple el retorno mínimo y no permite estimar una ventaja. El antecedente PAXG también había sido muy escaso; no extrapolamos su frecuencia a BTC, ni aflojamos la receta después de observar el resultado.

Se conservaron60retornos4h,dominancia cuadrática3 y desplazamiento neto<=ATR/C como parte del estado. ATR14simpleBTC actual adaptado explícitamente desde Wilder original; stop2ATR,TP3ATR=1.5R,48h. No se confundió esta representación con eficiencia net/path, RV/BV o mechas.

Ventana [2020-10-15,2026-01-01), desarrollo reutilizado, BTC-USDT Binance Perpetual Futures,10k,2%/6%/3x,fee.00045porlado yfunding histórico aplicado con proxies declarados;slippage0,sinestres/2026nuevo.

N=1; neto67.3791USDT; CAGR0.1288%; DD M1+ejecuciones0.9287%; Sharpe del motor0.3382 (sin inferencia útil con una operación). PF no estimable con pérdidas observadas cero: se conserva null, no un número infinito para aprobar. Meses activos positivos1/1; trimestres1/20; mediana calendario0.0000%; neto quitando mejores2meses0.0000USDT.

NO_CUMPLE: CAGR,regularidadcalendario/concentración y muestra insuficiente. No es evidencia de fracaso universal de toda semivarianza. Presupuesto de una corrida cerrado, sin reemplazos ni vecinos.

Check9b96a29a331b492bb3b1d44f218031e2 passed,fuenteSHA2560e97f8bf81ace3d8874f4c7740a35deadfcd278874992ce4d1c0fb15506b586a;revisión independiente sin erroresmateriales. Auditoría fffc41fe29994a999fa4abe24682cb8f completa: bruto−fees+funding=PNLsum=finishing−10k a1e−6USDT. Telemetría2.741.760M1,63intervalos/62meses/20Q,cero ventanasinválidas;fronteras,contribuciones ysaldo final reconciliados. DD M1 noextremosintraminuto;fronteraspostfunding/predecisión segúnconvenciónporfaseR11. Fundingaplicado,sinposicionesfinales.

Fuentes/configuración previas en BTC_DISCOVERY_K_PROTOCOL_20261021.md y BTC_DISCOVERY_K_MANIFEST_20261021.json;auditoría ytelemetría conservadas. Framework/configglobalintactos,sinlive/paper/Pi. Objetivo autónomo sigue activo, L plantea otra pregunta de alineación de barreras con protocolo propio.
