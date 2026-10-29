# Orquestación — resultados de primera ronda
Cinco hipótesis nuevas, con protocolos previos. Ventana común de desarrollo 2020-10-15 a 2025-12-31 exclusivo; capital 10.000 USDT; comisión .00045 por lado. 2026 no se evaluó.

| Caso | CAGR | Drawdown del motor | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|
|reference|28.83%|-14.89%|54.10% (61 activos)|71.43%|
|alloc_common|23.14%|-14.17%|54.10% (61 activos)|61.90%|
|alloc_risk|31.76%|-17.68%|55.74% (61 activos)|66.67%|
|lateral|0.33%|-13.53%|46.43% (56 activos)|42.86%|
|short_rr|23.43%|-13.30%|58.62% (58 activos)|61.90%|
|short_reclaim|27.29%|-15.00%|54.10% (61 activos)|61.90%|

[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb),
[reloj común](http://localhost:9200/#/backtest/9bbd9545-2154-4842-8902-8c926c7a4a56),
[presupuesto igual de riesgo](http://localhost:9200/#/backtest/72996434-7c02-4589-9400-42a23229ae02),
[fallo de rango](http://localhost:9200/#/backtest/acae5bd3-7f00-439d-991b-7eabbf86b903),
[short mínimo1R](http://localhost:9200/#/backtest/1f0b9301-0754-4044-ab29-9c9d9c979696),
[short invalidación por máximo](http://localhost:9200/#/backtest/2168b24e-632b-4dca-be9c-48677c7b5a58).

## Decisiones
Ninguna alcanza los objetivos 65–70% de meses activos y 80% de trimestres. No se promueve ninguna.
- Repartir exposición con reloj común mejora coherencia temporal del estimador, pero no la regularidad: mismos33meses positivos, menos trimestres.
- Presupuesto igual de riesgo suma un mes positivo y más retorno/exposición, pero pierde un trimestre positivo respecto a referencia.
- Reversión de rango: neto174,55 frente1160,54 de fees; sensible a fricción. No aumentar riesgo ni escoger retrospectivamente BTC long.
- Short mínimo1R: solo+190,65 netos en51shorts,PF1,033; mejor geometría planificada no generó mejor ventaja predictiva.
- Invalidación del máximo: shorts+3500,50/PF1,230, menor aporte y sin mejora mensual. La salida se activó en trades reales; no atribuir diferencias a simple ausencia de uso.

## Auditoría
AnálisisMCP8e2908d962b145dfac0918048ec57aba completado correctamente. AutocontrolesMTMv3,fees por trade,saldos terminales y contribuciones reconciliados. Artefactos temporales: orchestration_round1.json,monthly_matrix.csv y contribuciones por variante.
Los casos tienen63meses de calendario,con distintos activos: no comparar porcentajes activos sin sus denominadores. Ninguno es OOS limpio; no usar2026.
Pruebas anteriores a esta orquestación también existen y deben contarse al valorar selección adaptativa. No calcular una confianza estadística ignorando hipótesis descartadas.

## Próxima ronda
Cambiar premisas en vez de barrer umbrales locales:
- régimen diario bajista y recuperación fallida como componente shortBTC;
- salida long completa a3R/5R como familia predeclarada, con riesgo de perder tendencias;
- reversión de shocks relativos BTC/ETH con beta causal y control explícito de dos piernas (sin asumir cointegración ni atomicidad).
Las tres líneas requieren protocolos y verificación; ninguna se considera rentable o complementaria de antemano. Referencia inmutable, objetivo activo.
