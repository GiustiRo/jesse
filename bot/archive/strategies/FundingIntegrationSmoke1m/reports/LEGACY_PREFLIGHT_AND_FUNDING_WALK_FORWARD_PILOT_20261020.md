# Preflight del legacy y protocolo de microvalidación funding / walk-forward
Fecha: 2026-10-20 (America/Montevideo)

## Decisión y alcance
Introducir los cambios por etapas. Reutilizar hipótesis y definiciones del legacy después de auditar causalidad y unidades; no transferir automáticamente su modelo ni sus resultados como evidencia de una ventaja de funding.
Sin ML, sin chunks aleatorios, sin optimización amplia, sin live/paper, sin cuenta Binance privada ni operaciones en la Pi.
2026 no se ejecutó ni se usó para seleccionar reglas en este preflight. La ventana común de desarrollo será [2020-09-01,2026-01-01). Los datos anteriores siguen guardados.
El objetivo aquí es integridad del experimento, no cumplir un objetivo de rentabilidad mensual.

## Evidencia del legacy
El promovido top3_cf040_be225_tr300 es LightGBM multiclass con 12 variables: cinco de funding, tres de OI y cuatro de rango/régimen. Cinco funding: funding_rate, funding_zscore, funding_cum_24h, hours_to_next_funding, funding_momentum.
Fuente: C:/dev/trading/regime-trade/shared/models/registry/lightgbm/top3_cf040_be225_tr300/lightgbm_model_metadata.json:2.
Esto acredita que el modelo utilizaba esas entradas, no que cada una fuera rentable aisladamente. No se encontró un A/B limpio del ganador con y sin funding manteniendo todo lo demás fijo.
El legacy ya tenía folds walk-forward en su entrenamiento ML. Esa separación temporal no corrige una variable construida con datos futuros.
Sus agregados archivados incluyen folds de 2026; no se usarán como validación exclusivamente anterior a 2026 ni como puntuación para elegir este nuevo piloto.

## Microvalidación ejecutada: funciones originales con datos sintéticos
Se extrajeron por AST diez funciones/métodos originales, sin importar módulos legacy, abrir modelos binarios ni ejecutar sus scripts. Se ejecutaron en un workspace temporal de análisis MCP con datos sintéticos declarados. No son backtests ni retornos de inversión.

### A. Invariancia respecto al futuro: FALLA localizada
Prueba: conservar exactamente las entradas hasta 2021-01-09 00:00 UTC y cambiar sólo el cierre de las 20:00 del mismo día de 110 a 90.
La variable oi_price_divergence de las 00:00 cambia de 0 a 1. El cálculo sólo con el prefijo disponible devuelve 1.
El OI sintético ya está retrasado al día anterior, respetando la alineación del legacy. El problema restante es close_daily = último cierre del día corriente, remapeado a todas sus velas anteriores.
Fuentes:
- C:/dev/trading/regime-trade/shared/src/data/clean.py:164: el OI sí se desplaza un día; no acusar a todas las variables OI.
- C:/dev/trading/regime-trade/shared/src/features/futures.py:83 y :90: uso de cierre diario corriente y remapeo.
- C:/dev/trading/regime-trade/research/scripts/build_features.py:55: pipeline sin retraso global posterior.
- C:/dev/trading/regime-trade/shared/src/backtest/adapters.py:278: consumo de la fila actual.
La variable está entre las 12 del modelo promovido. No se cuantificó cuánto cambia su rentabilidad al corregirla: eso exigiría rehacer la evaluación; este preflight no reentrena ML.

### B. Unidades y calendario de funding: FALLA reproducida
La normalización original conserva fundingRate=0.0001 como fracción decimal.
Con notional constante de 10000 USDT y long, el cargo correcto por una liquidación es 1 USDT (0.01%).
El motor original divide de nuevo por100 y cobra 0.01 USDT en el ejemplo: factor100 por debajo para esta trayectoria de datos.
Además, con entrada a04:00 y barras4h, el ejemplo no cobra en08:00 y sí en12:00: decide mediante barras transcurridas desde la entrada, no por timestamps del exchange.
Fuentes:
- C:/dev/trading/regime-trade/shared/src/data/download.py:70.
- C:/dev/trading/regime-trade/shared/src/backtest/engine.py:71.
- C:/dev/trading/regime-trade/shared/src/backtest/costs.py:39.
Conclusión acotada: los netos del backtest legacy necesitan recálculo antes de considerarlos comparables con Jesse. Esto no demuestra un error en los cobros reales del exchange ni explica por sí solo la neutralidad observada en producción.
No se modificó el legacy.

## Microvalidación ejecutada: resultados reales ya almacenados en Jesse
Reanálisis independiente por MCP de snapshots completos; no se lanzaron nuevos backtests ni se eligieron períodos según una nueva rentabilidad.

| Control | Ventana UTC | Neto USDT | Sharpe reportado | Trades | DD reportado |
|---|---|---:|---:|---:|---:|
| Funding desactivado | 2025-12-01 → 2025-12-03 | -42.14678279999997 | -13.509256086106294 | 1 | 0 |
| Funding activado | misma | -42.17797454812647 | -13.509256086106294 | 1 | 0 |
| Observador OI | 2021-01-01 → 2021-01-03 | no aplica | no aplica | 0 | no aplica |

Estos son diagnósticos de infraestructura. Sharpe/DD en dos días y un trade no son evidencia económica ni estimación de riesgo fiable.
Control sin funding:
Dashboard: http://localhost:9200/#/backtest/4ccfc043-032f-45fd-b968-5f1521be2700
Control con funding:
Dashboard: http://localhost:9200/#/backtest/5f570095-5625-4a84-bfee-112194a75b8e
Observador OI histórico:
Dashboard: http://localhost:9200/#/backtest/343bd1b4-a212-407e-84ee-75113006b3f5

Comprobaciones aprobadas:
- Entradas, salidas, cantidad y timestamps idénticos entre controles.
- Comisiones idénticas:0.7947828 USDT.
- Tres movimientos de funding suman -0.031191748126504142 USDT.
- Diferencia de PnL:-0.031191748126502716; diferencia de saldo:-0.03119174812673009. Ambas coinciden con el ledger dentro de1e-8.
- Cada movimiento cumple cashflow=-qty*mark*rate. Cero precios aproximados utilizados por estos tres pagos.
- OI llegó a la estrategia en2021, con current.available_at anterior al límite final, applied=true y cero órdenes/trades.
- El archivo OI sigue declarado retrospectivo/no certificado point-in-time; lag+6m es un supuesto. Los huecos no se rellenan.

## Protocolo propuesto para el siguiente piloto acotado, aún no ejecutado
Separar validación técnica de evaluación económica. No introducir OI como regla de decisión en el primer A/B.

### Variables que permanecerán fijas
- BTC-USDT perpetual Binance; candles1m como base. Capital10000 USDT, fee0.00045, isolated3x; sizing, salidas y riesgo idénticos entre A y B.
- Funding contable activado en ambos; así el A/B mide la señal, no confunde añadir una regla con añadir un coste.
- Dataset funding fijo:9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 (cubre hasta2025).
- OI fuera de las decisiones del piloto; cuando se introduzca después, dataset fijo6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf y aceptación explícita de huecos.
- Sin cambios de timeframe, riesgo, stops, universo o umbrales después de ver la validación.
- Registrar todas las variantes y rechazos; no repetir hasta encontrar una ganadora.

### Hipótesis mínima inspirada en el legacy
A: control de precio con reglas completas congeladas antes de ejecutar la primera sesión.
B: exactamente A, bloqueando nuevas entradas cuando el último funding liquidado sea extremo y desfavorable para su dirección.
Bloqueo long:rate>0 y zscore>2; bloqueo short:rate<0 y zscore<-2.
zscore con los30 eventos liquidados anteriores como referencia, excluyendo el actual; exigir30 y desviación>0. Sin historial suficiente, no habilitar nuevas entradas en B.
Los parámetros30 y2 provienen de la configuración legacy, pero el signo del filtro es una hipótesis nueva: el modelo ML no demuestra por sí mismo esa regla. No se presenta como réplica del legacy.
El control A debe definirse antes de los resultados; su elección todavía es una tarea de implementación del piloto, no una variante ya validada ni una candidata promovida.

### Dos folds cronológicos de ensayo
- Fold1: desarrollo [2020-09-01,2022-01-01); validación [2022-01-01,2022-07-01).
- Fold2: desarrollo [2020-09-01,2023-01-01); validación [2023-01-01,2023-07-01).
- La selección y cualquier ajuste permitido utilizan exclusivamente la parte de desarrollo. Evaluar después la configuración congelada en el tramo siguiente.
- Para el primer A/B no se optimizan30 ni2: comparar ambos controles en los mismos tramos, sin escoger umbrales mirando validación.
- Los resultados de validación usados para decidir la familia de investigación quedan registrados como desarrollo del proceso. No se afirma que sobreviva una independencia absoluta después de iteraciones manuales.
- Si el tamaño de muestra no permite una conclusión económica, registrar inconcluso; nunca rebajar criterios por conveniencia ni acudir a2026 para resolverlo.
- 2026 permanece reservado para la candidata final según el acuerdo previo, con exposición previa al año declarada.

### Condiciones antes de pasar a investigación amplia
1. Toda variable nueva debe conservar sus valores pasados al añadir o cambiar datos futuros.
2. Señales sólo con eventos publicados bajo las políticas de disponibilidad declaradas.
3. Costes, fills y feed OI reconciliados; missing/stale tratado explícitamente.
4. A/B con configuración común y contribución de precio, funding y fees por separado.
5. No promover por pasar infraestructura: rentabilidad, muestra, estabilidad y objetivos mensuales son otra evaluación.
6. OI como filtro se probará en una etapa posterior contra la misma referencia; su disponibilidad técnica no obliga a incluirlo en la estrategia.

## Resultado de esta etapa
Jesse pasa las comprobaciones contables y de consumo ya ejecutadas. El legacy falla dos comprobaciones reproducibles de causalidad/contabilidad y no debe portarse literalmente.
No hay una estrategia nueva seleccionada, objetivos de rentabilidad evaluados ni piloto walk-forward económico ejecutado todavía. El entregable es el preflight y un protocolo acotado para comenzar con cambios atribuibles.

## Reproducibilidad y límites
Análisis MCP exitoso:79078c8482024762a2932e9b4650a15c; artifact:micro_validation.json.
El primer intento162bb81b9fde41db9105cc45d9a6e2af falló al faltar la constante de módulo_EPSILON en la extracción; se agregó su valor original1e-10, sin cambiar funciones, y el segundo pasó. Los workspaces son temporales; esta evidencia se conserva en el reporte.
No se auditó todo el legacy ni se reconstruyeron sus retornos corregidos. No se descargaron datos nuevos ni se modificaron credenciales, configuración global, código del legacy, modelos o sesiones reales.

Funciones originales y hashes:
- shared/src/features/futures.py:13 _hours_from_interval: 3b1f4ac60949acdb05eabf1be1e3fb22bdc15034e5e8830ae24261a68d6aabc1
- shared/src/features/futures.py:21 _infer_bar_hours: 7c71d205fa7ae0abec52557d54489605c3bed1272e3079a35d651cca2c1f7f9b
- shared/src/features/futures.py:28 _rolling_zscore: 3ebff8a901ce1f404e564a7ee9e620797f5f3f5faba0d21122f20f3c70b0251d
- shared/src/features/futures.py:34 _threshold_signal: e86e79ddc69ec8211a9557d102549386b7cc6f28864e54258ea0f83d6ba4648d
- shared/src/features/futures.py:43 _daily_last: 63e783c0236ee3521b21044f7b6826185c159a0d92152d5ba0dc6f171d8b103f
- shared/src/features/futures.py:47 _map_daily_feature: dee9a377a88d6e7c0daa6b96adb82d1c469d54759da749feecf9b4e9745ea5ef
- shared/src/features/futures.py:53 add_futures_features: fb9f988d91d8acde150c0622256ec7b27a3dd5ab9ee1ace2173e626a4bf4e31e
- shared/src/backtest/costs.py:39 calculate_funding_cost: 5b44f7e9abe23c5c8078080114edc8b5aef5774198913dc8ef8fb2704c96a7cd
- shared/src/data/download.py:70 _normalise_funding_frame: b6b70053003f96d3ba385d5a83286d58908e760357f94545aa6994848b21c6b4
- shared/src/backtest/engine.py:71 _apply_funding: ba07b37785871ecd8ee55f3e2fc883305e3325333a7303966501f14044603706
