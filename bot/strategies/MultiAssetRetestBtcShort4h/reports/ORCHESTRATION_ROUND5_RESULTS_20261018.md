# Ronda5: estado tras18 pruebas adicionales
Fecha2026-10-18. Objetivo activo y no alcanzado.18 es únicamente el número económico de esta orquestación; la búsqueda global previa incluye muchas más hipótesis y variantes. No son18 réplicas independientes.

| Diseño | CAGR | DD motor | Meses activos positivos | Calendario | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
|[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)|28.829%|−14.891%|33/61|33/63|15/21|
|[Una entrada short por episodio](http://localhost:9200/#/backtest/74b84b33-2030-4b9c-ba19-03a18ef68420)|29.355%|−14.903%|33/61|33/63|15/21|
|[SPY calendario4/4](http://localhost:9200/#/backtest/2f510e3e-6563-4002-b96a-ef2bbd38e52d)|−1.053%|−16.829%|30/63|30/63|9/21|
|[Shock relativo BTC/ETH](http://localhost:9200/#/backtest/62b9f852-8b48-4b4c-b59b-537e9e687a64)|−7.669%|−34.372%|10/63|10/63|1/21|

## Decisiones
Una entrada por episodio mejora poco el rendimiento y nada los signos mensuales/trimestrales. No promovida ni nuevas variantes cooldown. De803.99USDT adicionales,747.27 vienen de la trayectoria de capital de los longs y56.73 de shorts. Cinco shorts originales se omiten (tres perdedores y dos ganadores) y aparece uno nuevo;215 trades coinciden exactamente en precios/tiempos, no todos en tamaño. No exagerar una nueva ventaja short.

SPY4/4 pierde−536.82USDT, con−19.26 antes de fees sobre sus fills.62entradas verificadas a16UTC, una por turno;11STOPy51MARKET. Es adaptación de calendario civil y reloj CFD, no réplica de la literatura bursátil(-1,+3). Fallar aquí no refuta ese paper. No mover ventana ni combinar componente negativo.

Pares:1247baskets completos/2494legs con entradas coincidentes y direcciones opuestas, sin baskets incompletos, fees2947.43 y net−3403.17. El PnL de precio de esos mismos fills es−455.74 antes de fees; no es un nuevo backtest a fee0.191baskets(15.3%) cierran sus patas en momentos distintos, máximo59min y90.67h acumuladas; no se inventa PnL contrafactual de cerrar atómicamente. Ambos sentidos relativos pierden. Rechazado, sin invertir signo, aumentar riesgo, cambiar beta/umbrales/horas o rescatar con ejecución1m después de ver el fallo. OLS de retornos y correlación negativa entre patas no demuestran reversión ni rentabilidad.

## MTM y posiciones alfinal
V4 inline pasó autocontroles, fills/fees y wallet de estas tres sesiones. Cierres forzados del motor: SPY1 y pares2 explican exactamente contador abierto PREterminación y grossopen_pl. Se etiqueta convención de liquidación final, no liquidez ejecutable demostrada; no se alteraron métricas ni framework.
Períodos completos: OneFill33/59activos y14/19quarters, igual referencia; SPY29/61meses y7/19quarters; pares9/61meses y1/19quarters. Inactividad/cash y bordes visibles; no cambiar denominador para aceptar.
Pares añosMTM2020parcial−1.973%,2021−6.226%,2022−8.116%,2023−10.925%,2024−6.346%,2025−6.375%. Una correlación−0.760 entre contribuciones de sus patas no crea alpha.

## Reutilización y documentación
Se retiró antes de crear el control short24h: ya existía [24h](http://localhost:9200/#/backtest/e474571a-bcad-47a9-b650-4ab14cc5029e), junto a48h, con fuentes equivalentes yMTMv3 válido. No se añade al recuento ni se repite.
Inventario global del agente: strategies/OrchManageTurtleDaily/reports/ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md.
Error específico de lecturaBtcTrendMasterHTTP500 documentado, sin workaround; otraslecturas/resultados/importación/reports responden. Esa lectura opcional permanece pendiente, no se modificó el legado.

## Continuación autorizada
Referencia inmutable y2026sin evaluar. Estudiar diseños con información adicional exante: calendario de reuniones programadas de Fed, y disponibilidad pública de financiación/basis. No confundir fundamento publicado con beneficio enSPYCFD. Documentar calendario/cancelaciones, margen y costes antes de implementar. Funding no tiene aún datos/contabilidad local ni autorización para scripts nuevos: preparar propuesta concreta y pedir opt-in si se necesita el módulo research. Ninguna nueva excepción de framework autorizada.
