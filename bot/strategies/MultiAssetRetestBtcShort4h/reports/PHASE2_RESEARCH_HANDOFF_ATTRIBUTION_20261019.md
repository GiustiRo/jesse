# Handoff de investigación tras atribución SPY/PAXG

Fecha: 19 de octubre de 2026.

## Estado completado

Se ejecutaron los 34 controles fijados en ATTRIBUTION_STAGE_PROTOCOL_20261019.md: 17 SPY y 17 PAXG. Todos finished, sin procesos ni análisis pendientes de raíz. Las dos réplicas C0 pasaron paridad económica exacta antes de liberar el resto. Root verificó las 34 fuentes de sesión contra las revisadas, los formularios y las 34 conciliaciones MTM a cierre diario UTC.

Resultado central: ATTRIBUTION_SPY_PAXG_RESULTS_20261019.md. Datos exactos y fuentes reproducibles en los informes por activo y en ATTRIBUTION_MTM_SOURCE_20261019.md / ATTRIBUTION_MTM_RESULTS_20261019.md. Esta tanda es atribución, no 34 ideas independientes de alpha.

## Referencias y candidata

[SPY C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269): 31 operaciones, neto 751,3477149671152, fees 286,47552620734854, DD motor −5,2131810594609025%, 15/61 meses y 9/19 trimestres completos positivos. Cq y E1 coinciden exactamente en operaciones y resultado observado. M empeora.

[PAXG C0](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673): 35 operaciones, neto 546,1105723537391, fees 246,60888105483386, DD motor −6,919378335744097%, 15/61 meses y 8/19 trimestres completos positivos.

[PAXG M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae): candidata de investigación, no estrategia validada. 38 operaciones, neto 962,1262139358278, fees 267,71818325273483, PF 1,5743577329815752, DD motor −7,64796155547669%, CAGR 1,777532757709932%, tiempo abierto 15,204866584924389%. Neto con 10 bps RT adicionales 664,6615658772334; sin mejor operación 337,4547898331979; sin las tres de mayor PnL −635,127505102286. 17/61 meses y 10/19 trimestres completos positivos. Las cohortes por cierre 2021–2023 siguen negativas y la mejora se concentra en 2024–2025.

Los beneficios grandes al retirar trailing dependen de un único runner terminal en ambos activos. SPY con sólo stop inicial tiene una sola operación durante casi toda la ventana. No promover esas políticas por neto acumulado.

Los relojes R/U tienen dispersión amplia. No elegir una seed. PAXG U supera a su R emparejada en los cinco caminos, con mucha más exposición/rotación y DD mayor; no demuestra alpha del reloj o causalidad del filtro.

No se integra ninguna modificación en la cartera de referencia. SPY sigue sin sustitución robusta; PAXG M merece confirmación local. No avanzar a integración de cartera como si ambos activos ya estuvieran mejorados.

## Condiciones persistentes

- Proyecto Jesse mediante MCP jesse-local. Leer DOCS.md, reglas aplicables del bot y jesse://strategy antes de editar; no acceder a estrategias, informes o sesiones por shell/SQL como sustituto de MCP.
- Proxies aceptados: SPX CFD BID / 10 para SPY y precio spot de PAXG. Desarrollar sobre su acción de precio con los datos disponibles. No reabrir la discusión de funding ni exigir nueva fuente como bloqueo para este estudio.
- Sólo 2020-10-15 a 2025-12-31, final exclusivo; 2026 permanece cerrado.
- 10.000 USDT aislados, riesgo planificado 1%, fee 0,00045 por lado en todas las órdenes, isolated 5x, cap de nocional 4,4, sin piramidar. Reserva 0,001 sólo para sizing.
- Una ruta 4h y data route M1 del mismo activo, warmup 240, fast/debug false. SPY conserva exactamente calendario UTC Mon–Fri 00–20 para features y barras abiertas 00–16 para entradas. PAXG sin restricción horaria.
- Fuentes autocontenidas. Conservar ledger, sizing, stop inicial y gestión salvo hipótesis expresamente fijada.
- Cq/M/R/U: búsqueda exacta M1 T−60s por searchsorted y paridad con self.price. No gatear trailing original por frescura. E4 conserva deuda de salida temporal.
- Dos backtests simultáneos por especialista, cuatro globales; un análisis por especialista, dos globales. Reutilizar agentes ya autorizados cuando corresponda; no crear chats nuevos.
- Sin nuevos research_scripts, instalaciones, datasets, funding, cambios de framework, BTC como nueva ruta, reinicios ni live/paper/Pi.
- Todas las sesiones citadas deben estar enlazadas con su dashboard_url. Preservar todo resultado, incluidos negativos y ceros, antes de escoger una conclusión.

## Propuesta acotada siguiente: 14 nuevas configuraciones, no ejecutadas

Esta sección es un plan posterior. Ninguna de sus configuraciones está implementada o ejecutada; no se incluye en el total de 34.

### PAXG: ocho contrastes de estabilidad local

Pregunta: ¿la mejora de la política MARKET frente a Cq persiste al mover una sola pieza cercana de la señal, o es particular del punto 26/26?

Ejecutar pares Cq y M en estas cuatro configuraciones, alterando un solo parámetro respecto a la referencia y conservando el resto:
1. Donchian 24; ADX mínimo 26.
2. Donchian 28; ADX mínimo 26.
3. Donchian 26; ADX mínimo 24.
4. Donchian 26; ADX mínimo 28.

Los pasos simétricos de dos unidades sirven como perturbaciones locales sencillas, sin estimarlos a partir de los fills ganadores. Son ocho fulls, más las referencias ya existentes Donchian 26 / ADX 26. No escoger el mejor vecino ni optimizar parámetros con el resultado.

Mantener stop 2 ATR, breakeven 2,25 R, trailing 4,2 y tightening originales. M valida primero la distancia contra la frontera Donchian original y sólo entonces sustituye entrada por cierre MARKET y recalcula sizing. Comparar las diferencias pareadas de política a lo largo de todos los vecinos, exposición, costes, concentración y calendario UTC. Un cambio de signo cercano debilita la estabilidad; una mejora consistente prioriza la hipótesis, sin convertirla en validación fuera de muestra.

### SPY: seis contrastes de selección del retest

Pregunta: ¿la referencia depende de una selección estable del evento de breakout/retest, o de un conjunto muy preciso de episodios?

Conservar política Cq y toda la gestión original. Definir g = (close − máxima previa Donchian) / ATR. La referencia exige 0 < g <= 1.

Cuatro variantes cambian únicamente ese intervalo:
1. 0,10 < g <= 1.
2. 0,25 < g <= 1.
3. 0 < g <= 0,50.
4. 0 < g <= 0,75.

Los umbrales son fracciones redondas del desplazamiento máximo ya existente, fijadas antes de mirar esos resultados. Contrastan eventos cercanos a frontera frente a rupturas más extendidas; no se presupone cuál mejorará. No equivalen a controlar spread ni garantizan evitar la conversión MARKET del motor.

Dos variantes adicionales modifican sólo Donchian a 24 o 28, manteniendo el intervalo original. No combinar el mejor intervalo con el mejor canal en esta tanda: hacerlo introduciría una nueva selección adaptativa.

### Evaluación y cierre de la siguiente tanda

Congelar fuentes y tabla de hipótesis antes de ejecutar. Si cambia motor, datos o configuración desde esta atribución, repetir primero la paridad C0 correspondiente e investigar cualquier diferencia.

Informar las 14 configuraciones completas, cuentas aisladas y referencias; N, neto/fees, PF/DD/CAGR, duración, tiempo y nocional-tiempo, turn-over, neto por nocional, costes adicionales estáticos, concentración y meses/trimestres a cierre UTC. Parear decisiones sólo por timestamps exactos y reconocer selección por fills/ocupación. No ajustar exposición a posteriori para favorecer una variante.

Separar una pista de desarrollo de una mejora robusta. Mejor neto con mayor DD o mayor exposición requiere exponer el intercambio, no declararlo automáticamente superior. La referencia también necesita validación: su origen casual no la hace más verdadera que las alternativas.

Después de ese contraste, decidir si merece avanzar una candidata fija a validación adicional. No abrir 2026 durante una búsqueda adaptativa ni usarlo para elegir entre recetas. No integrar cartera, trasladar ejecución a perpetuos o elevar riesgo sólo por encontrar un máximo histórico.
