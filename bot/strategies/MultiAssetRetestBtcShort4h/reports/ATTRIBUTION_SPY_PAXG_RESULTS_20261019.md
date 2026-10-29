# Atribución SPY/PAXG: resultados y siguiente investigación

Fecha: 19 de octubre de 2026. **34 backtests completos, 17 por activo; 34 snapshots y 34 auditorías MTM verificados.**

Hay una candidata concreta de desarrollo en PAXG: entrar MARKET con la señal original mejora el resultado total y algunos diagnósticos de concentración respecto a la referencia. En SPY esa misma modificación empeora. No se encontró todavía una sustitución robusta para ambos activos. Ninguna variante se integra en cartera ni se declara validada fuera de muestra.

## Pregunta y condiciones

Esta tanda descompone la referencia en señal, ejecución, gestión y permanencia. No representa 34 nuevas ideas independientes de alpha.

Ventana: 2020-10-15 a 2025-12-31, fecha final exclusiva. 2026 permanece cerrado. Cada activo usa una cuenta aislada de 10.000 USDT, riesgo planificado de 1% por entrada, comisión de 0,00045 por lado en todas las órdenes, margen isolated 5x y cap de nocional 4,4. La reserva de sizing de 10 bps no se cuenta como slippage ya simulado.

Se utilizan los proxies aceptados del proyecto: SPX CFD BID / 10 para SPY y precio spot de PAXG. Se investiga acción de precio con los datos disponibles. Funding y nuevos derivados quedan fuera de esta tanda.

C0 replica exactamente la referencia; Cq agrega frescura M1 sólo al entrar. E1 retira breakeven; E2 retira trailing y mantiene breakeven; E3 conserva únicamente stop inicial; E4 agrega vencimiento de 72 horas al stop inicial. M entra al cierre MARKET conservando el evento y filtros originales, con tamaño recalculado. R01–05 entran por reloj dentro del régimen original, sin breakout/retest; U01–05 usan el mismo reloj sin régimen. Ambas familias conservan gestión original. Seeds fijas 101/202/303/404/505; no se elige una ganadora.

## Comparación principal

Beneficio neto en USDT; DD y CAGR del motor en porcentajes. Tiempo abierto se mide sobre toda la ventana. Meses y trimestres positivos se reconstruyeron a cierre diario UTC y usan 61 meses y 19 trimestres completos.

| Activo / control | N | Neto | PF | DD motor % | CAGR % | Tiempo abierto % | Meses + / 61 | Trimestres + / 19 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [SPY C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 15 | 9 |
| [SPY Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 15 | 9 |
| [SPY E1](http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0) | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 15 | 9 |
| [SPY E2](http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691) | 8 | 4889.75 | 11.78 | -20.72 | 7.93 | 85.95 | 35 | 12 |
| [SPY E3](http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2) | 1 | 3485.35 | — | -11.06 | 5.90 | 98.86 | 40 | 14 |
| [SPY E4](http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5) | 44 | -28.87 | 0.98 | -7.47 | -0.06 | 5.85 | 16 | 9 |
| [SPY M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | 38 | 151.60 | 1.07 | -7.72 | 0.29 | 16.00 | 15 | 9 |
| [PAXG C0](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673) | 35 | 546.11 | 1.31 | -6.92 | 1.03 | 13.36 | 15 | 8 |
| [PAXG Cq](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | 35 | 546.11 | 1.31 | -6.92 | 1.03 | 13.36 | 15 | 8 |
| [PAXG E1](http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b) | 35 | 491.17 | 1.27 | -7.40 | 0.92 | 13.36 | 15 | 8 |
| [PAXG E2](http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc) | 15 | 4325.43 | 6.39 | -10.67 | 7.14 | 40.15 | 22 | 9 |
| [PAXG E3](http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242) | 15 | 3669.37 | 4.02 | -14.75 | 6.18 | 40.57 | 19 | 6 |
| [PAXG E4](http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837) | 47 | -374.35 | 0.83 | -6.41 | -0.73 | 5.76 | 11 | 6 |
| [PAXG M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 38 | 962.13 | 1.57 | -7.65 | 1.78 | 15.20 | 17 | 10 |

## Qué aprendimos de la gestión

En SPY, C0/Cq/E1 tienen las mismas 31 operaciones y resultado exacto. Quitar el breakeven no cambia marginalmente el resultado observado mientras se conserva el trailing. En PAXG, quitarlo reduce el neto de 546,11 a 491,17 y empeora el DD. No hay base para eliminarlo como regla común a ambos activos.

Quitar el trailing aumenta mucho el beneficio en esta historia, pero también cambia ocupación y oportunidades posteriores. En SPY E2, una operación terminal aporta 5.340,43 USDT; sin ella quedan −450,69. E3 es una sola posición durante aproximadamente 5,15 años y el 98,86% de la ventana. En PAXG E2/E3, la operación terminal aporta 5.119,36 / 4.884,91 netos; sin ella quedan −793,93 / −1.215,54. El contador abierto previo a terminación se concilió contra fills y open_pl: son cierres del motor, no posiciones residuales vivas.

E4, stop inicial más 72 horas, pierde en ambos activos. Esto desaconseja ese recorte específico; no demuestra que cualquier salida temporal sea mala. El deadline se revisa en ticks de 4h y conserva deuda de salida hasta una cotización fresca, por lo que 72h no significa ejecución garantizada exactamente a esa hora. El stop inicial sigue activo mientras espera.

La hipótesis útil es que la duración de los grandes movimientos importa. El mayor neto de E2/E3 no constituye por sí mismo una mejora repetible de la señal. Retirar operaciones ganadoras es un diagnóstico de concentración, no un criterio universal de descarte para estrategias que dejan correr tendencias.

## La ejecución depende del activo

En SPY, M reduce el neto de 751,35 a 151,60, empeora el DD de −5,21% a −7,72% y pierde 35,47 con 5 bps adicionales por vuelta. La política de retest es la referencia más sólida entre estos dos diseños en esta muestra.

En PAXG, M mejora varios diagnósticos a la vez:

| Métrica | Referencia C0/Cq | M |
|---|---:|---:|
| Neto | 546,11 | 962,13 |
| PF | 1,31 | 1,57 |
| DD motor | −6,92% | −7,65% |
| Tiempo abierto | 13,36% | 15,20% |
| Neto con 10 bps RT adicionales | 272,10 | 664,66 |
| Neto sin mejor operación | −91,39 | 337,45 |
| Meses completos positivos | 15/61 | 17/61 |
| Trimestres completos positivos | 8/19 | 10/19 |

Sigue concentrada: sin sus tres operaciones de mayor PnL, M queda en −635,13. Sus cohortes de operaciones cerradas de 2021, 2022 y 2023 son negativas; la mejora proviene de 2024–2025. Eso identifica dependencia histórica, no una validación en regímenes diversos. Las cohortes por año de cierre no se confunden con rentabilidad MTM anual.

Comparar M y Cq no aísla un único efecto causal. El precio planificado, el tamaño, los fills y la ocupación posterior cambian. SPY comparte cinco fills exactos y PAXG ninguno, mientras que el diagnóstico secundario por created_at exacto encuentra 25 y 24 decisiones comunes. Esa intersección está seleccionada por doble fill y disponibilidad previa. En PAXG, M paga un precio más alto en esa intersección y su diferencia normalizada de PnL es peor; el mejor resultado global no demuestra mejor precio de ejecución.

La política SPY de retest usa la clasificación automática del motor: sus entradas ejecutadas son 24 LIMIT y 7 MARKET. La proximidad de hasta 1,5 bps al precio actual se convierte primero a MARKET. Se conservó esa semántica en C0/Cq; no se describe la referencia como LIMIT pura ni se modificó el framework.

## Los diez relojes de cada activo

Se publican las cinco seeds por familia. Son caminos dependientes de la misma historia; no constituyen cinco muestras IID, una prueba formal de significación o permiso para seleccionar la seed con mayor beneficio.

En SPY, R tiene mediana neta de 143,16, rango −348,55 a 1.054,72, y tres de cinco caminos positivos. U tiene mediana de 75,74, rango −1.075,46 a 2.572,14, y tres de cinco positivos. El tiempo abierto mediano es 5,00% en R y 26,74% en U. La mediana R con 10 bps adicionales ya es negativa; la U también lo es con 5 bps. Las cinco U presentan más DD de motor que C0.

En PAXG, las cinco U superan el neto de su R emparejada, pero rotan más capital y permanecen mucho más tiempo expuestas. Sus DD de motor abarcan aproximadamente −9,73% a −21,72%, todos peores que el −6,92% de C0. Eso obliga a estudiar participación direccional, costes y riesgo; no prueba que retirar el régimen genere alpha. Los resultados completos, exposición y normalización por nocional se conservan en los informes del activo.

No se igualó exposición a posteriori ni se escogió el camino favorable. El reloj común no garantiza los mismos fills: cada posición anterior altera la disponibilidad.

## Tabla completa de los 34 controles

| Activo / control | N | Neto | DD motor % | Tiempo abierto % | Neto +10 bps RT | Sin mejor operación | Meses + / 61 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [SPY C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) | 31 | 751.35 | -5.21 | 15.26 | 433.04 | 349.58 | 15 |
| [SPY Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | 31 | 751.35 | -5.21 | 15.26 | 433.04 | 349.58 | 15 |
| [SPY E1](http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0) | 31 | 751.35 | -5.21 | 15.26 | 433.04 | 349.58 | 15 |
| [SPY E2](http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691) | 8 | 4889.75 | -20.72 | 85.95 | 4825.94 | -450.69 | 35 |
| [SPY E3](http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2) | 1 | 3485.35 | -11.06 | 98.86 | 3479.97 | 0.00 | 40 |
| [SPY E4](http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5) | 44 | -28.87 | -7.47 | 5.85 | -480.45 | -215.95 | 16 |
| [SPY M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | 38 | 151.60 | -7.72 | 16.00 | -222.54 | -224.73 | 15 |
| [SPY R01](http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41) | 11 | -81.60 | -4.93 | 4.38 | -205.32 | -293.73 | 4 |
| [SPY R02](http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0) | 13 | 1054.72 | -3.25 | 6.11 | 906.30 | 517.16 | 7 |
| [SPY R03](http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9) | 16 | 153.75 | -5.55 | 6.11 | -7.85 | -276.51 | 9 |
| [SPY R04](http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c) | 16 | -348.55 | -6.37 | 5.00 | -502.46 | -595.08 | 5 |
| [SPY R05](http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e) | 9 | 143.16 | -3.17 | 3.76 | 40.86 | -156.40 | 5 |
| [SPY U01](http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8) | 72 | 1874.98 | -11.63 | 30.97 | 1158.56 | 1036.19 | 29 |
| [SPY U02](http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b) | 70 | 2572.14 | -5.49 | 31.99 | 1932.64 | 2005.53 | 27 |
| [SPY U03](http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8) | 74 | -440.28 | -14.79 | 26.74 | -1085.58 | -1050.49 | 24 |
| [SPY U04](http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2) | 79 | -1075.46 | -18.08 | 25.90 | -1674.21 | -1413.33 | 20 |
| [SPY U05](http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841) | 70 | 75.74 | -16.98 | 26.61 | -479.45 | -305.66 | 23 |
| [PAXG C0](http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673) | 35 | 546.11 | -6.92 | 13.36 | 272.10 | -91.39 | 15 |
| [PAXG Cq](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) | 35 | 546.11 | -6.92 | 13.36 | 272.10 | -91.39 | 15 |
| [PAXG E1](http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b) | 35 | 491.17 | -7.40 | 13.36 | 218.58 | -143.00 | 15 |
| [PAXG E2](http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc) | 15 | 4325.43 | -10.67 | 40.15 | 4213.47 | -793.93 | 22 |
| [PAXG E3](http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242) | 15 | 3669.37 | -14.75 | 40.57 | 3560.27 | -1215.54 | 19 |
| [PAXG E4](http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837) | 47 | -374.35 | -6.41 | 5.76 | -721.66 | -618.49 | 11 |
| [PAXG M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae) | 38 | 962.13 | -7.65 | 15.20 | 664.66 | 337.45 | 17 |
| [PAXG R01](http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1) | 33 | 108.95 | -8.42 | 10.21 | -122.16 | -248.62 | 11 |
| [PAXG R02](http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c) | 30 | -153.99 | -8.81 | 8.63 | -378.07 | -510.43 | 10 |
| [PAXG R03](http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796) | 30 | 869.16 | -7.27 | 13.54 | 654.91 | 413.86 | 17 |
| [PAXG R04](http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4) | 25 | 1252.44 | -4.58 | 11.83 | 1041.71 | 715.94 | 12 |
| [PAXG R05](http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8) | 36 | 47.86 | -12.41 | 13.70 | -206.50 | -318.74 | 12 |
| [PAXG U01](http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd) | 118 | 2902.32 | -14.11 | 50.16 | 2020.02 | 2297.83 | 32 |
| [PAXG U02](http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62) | 107 | 37.11 | -18.39 | 39.92 | -724.55 | -538.41 | 26 |
| [PAXG U03](http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d) | 129 | 2611.10 | -19.11 | 51.33 | 1677.47 | 1784.49 | 30 |
| [PAXG U04](http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a) | 126 | 1667.03 | -21.72 | 48.15 | 707.06 | 1035.91 | 29 |
| [PAXG U05](http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b) | 122 | 3873.54 | -9.73 | 49.80 | 2837.86 | 3159.95 | 28 |

## Decisión y siguiente foco

Se conserva la referencia de cartera y se mantiene PAXG M como candidata de investigación. SPY continúa sin reemplazo robusto. No se seleccionan seeds ni los runners terminales de E2/E3 como ganadores.

El siguiente estudio debe contrastar hipótesis más estrechas: estabilidad local de la mejora MARKET en PAXG y selección del evento de retest en SPY. Conviene mantener las salidas constantes durante esos contrastes, porque mezclar entrada y gestión volvería a ocultar el origen del cambio. La propuesta acotada se detalla en PHASE2_RESEARCH_HANDOFF_ATTRIBUTION_20261019.md; no está ejecutada ni forma parte de estos 34 resultados.

Toda la ventana 2020–2025 ya fue usada repetidamente como desarrollo. Repetir escenarios no convierte un máximo observado en evidencia fuera de muestra. Los resultados positivos de M son suficientes para darle prioridad de investigación, todavía insuficientes para declarar mejoras robustas en ambos activos. 2026 sigue reservado.

## Verificación y fuentes

- Dos controles C0 reprodujeron exactamente operaciones, órdenes ejecutadas, cantidades, precios, comisiones, balances y curva almacenada de sus referencias antes de liberar el resto.
- Root contrastó las 34 fuentes ejecutadas contra las fuentes revisadas: igualdad exacta. También verificó invariantes de formularios. No hubo errores ni sesiones pendientes.
- Los análisis de fills conciliaron PnL, fees, cantidades y wallet. La auditoría MTM independiente cubre las 34 sesiones con todos los terminales conciliados.
- Stress 5/10 bps RT significa costes adicionales sobre fills y tamaños congelados, mitad en cada lado; no es un backtest nuevo con impacto, spread o trayectorias de ejecución alteradas.
- Exposición a precio de entrada es suma(nocional inicial × duración) / (capital inicial × ventana); no equivale a nocional MTM ni beta constante.
- Sin instalación, funding, nuevo histórico, live/paper ni cambios de framework.

Protocolo: ATTRIBUTION_STAGE_PROTOCOL_20261019.md.
Implementación/snapshots: ATTRIBUTION_ROOT_IMPLEMENTATION_REVIEW_20261019.md.
MTM reproducible: ATTRIBUTION_MTM_SOURCE_20261019.md y ATTRIBUTION_MTM_RESULTS_20261019.md.
SPY: strategies/ResearchSpyReference4h/reports/ATTRIBUTION_SPY_FINAL_REPORT_20261019.md y ATTRIBUTION_SPY_EXACT_RESULTS_20261019.md.
PAXG: strategies/AttrPaxgC0Retest4h/reports/ATTRIBUTION_PAXG_FINAL_REPORT_20261019.md y ATTRIBUTION_PAXG_EXACT_TABLE_20261019.md.

## Datos normalizados exactos

time_open_pct se expresa en porcentaje en ambos activos. entry_notional_time es la aproximación a precio de entrada. Los DD del motor y a cierre UTC permanecen separados. ex3 retira las tres operaciones de mayor PnL, incluso si alguna es negativa; en muestras con menos de tres se retiran las disponibles.

```json
[
  {
    "asset": "SPY",
    "control": "C0",
    "strategy": "AttrSpyC0",
    "session_id": "798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "dashboard_url": "http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "complete_positive_months": 15,
    "complete_active_months": 33,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "Cq",
    "strategy": "AttrSpyCqFreshLimit",
    "session_id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
    "dashboard_url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "complete_positive_months": 15,
    "complete_active_months": 33,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "E1",
    "strategy": "AttrSpyE1NoBE",
    "session_id": "a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "dashboard_url": "http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "N": 31,
    "net": 751.3477149671152,
    "fees": 286.47552620734854,
    "PF": 1.4930482284215572,
    "DDmotor": -5.2131810594609025,
    "CAGR": 1.3992310944554776,
    "time_open_pct": 15.264093244584572,
    "entry_notional_time": 0.14148527769141334,
    "stress5": 592.1946448519213,
    "stress10": 433.0415747367277,
    "exbest": 349.57799671604494,
    "ex3": -298.2237721588764,
    "complete_positive_months": 15,
    "complete_active_months": 33,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -5.2179628778702085,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "E2",
    "strategy": "AttrSpyE2NoTrail",
    "session_id": "069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "dashboard_url": "http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "N": 8,
    "net": 4889.748865865099,
    "fees": 57.427905819458054,
    "PF": 11.776888992472053,
    "DDmotor": -20.724256024947575,
    "CAGR": 7.934483102177947,
    "time_open_pct": 85.9536842412565,
    "entry_notional_time": 0.5908738437924608,
    "stress5": 4857.844473743178,
    "stress10": 4825.940081621257,
    "exbest": -450.6854868412511,
    "ex3": -453.7254553963321,
    "complete_positive_months": 35,
    "complete_active_months": 57,
    "complete_positive_quarters": 12,
    "DD_UTC_dayclose": -20.72094358027037,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "E3",
    "strategy": "AttrSpyE3InitialStop",
    "session_id": "1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "dashboard_url": "http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "N": 1,
    "net": 3485.34533747049,
    "fees": 4.83561912951,
    "PF": null,
    "DDmotor": -11.060009660496705,
    "CAGR": 5.902901610981659,
    "time_open_pct": 98.86100893326328,
    "entry_notional_time": 0.3586499123691498,
    "stress5": 3482.65888239854,
    "stress10": 3479.97242732659,
    "exbest": 0,
    "ex3": 0,
    "complete_positive_months": 40,
    "complete_active_months": 61,
    "complete_positive_quarters": 14,
    "DD_UTC_dayclose": -11.046906465285566,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "E4",
    "strategy": "AttrSpyE4Stop72h",
    "session_id": "0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "dashboard_url": "http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "N": 44,
    "net": -28.867539957479785,
    "fees": 406.4284583989386,
    "PF": 0.9806463373785479,
    "DDmotor": -7.4718587007506,
    "CAGR": -0.05543334143435219,
    "time_open_pct": 5.847674724119811,
    "entry_notional_time": 0.05938130511605465,
    "stress5": -254.66112795689014,
    "stress10": -480.45471595630033,
    "exbest": -215.9489723917068,
    "ex3": -483.5227560627142,
    "complete_positive_months": 16,
    "complete_active_months": 30,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -7.468516914185863,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "M",
    "strategy": "AttrSpyMarket",
    "session_id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "dashboard_url": "http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "N": 38,
    "net": 151.6012639172099,
    "fees": 336.73029237147995,
    "PF": 1.074122772361648,
    "DDmotor": -7.718707541843617,
    "CAGR": 0.28900965265155065,
    "time_open_pct": 15.996051556022653,
    "entry_notional_time": 0.1446681109984161,
    "stress5": -35.47112073361228,
    "stress10": -222.54350538443452,
    "exbest": -224.7296691424284,
    "ex3": -864.90548009341,
    "complete_positive_months": 15,
    "complete_active_months": 39,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -7.723363450254761,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "R01",
    "strategy": "AttrSpyR01",
    "session_id": "83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "dashboard_url": "http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "N": 11,
    "net": -81.60081391564947,
    "fees": 111.34571187400127,
    "PF": 0.8749054563501013,
    "DDmotor": -4.932604907914506,
    "CAGR": -0.15703098268418092,
    "time_open_pct": 4.376167746832486,
    "entry_notional_time": 0.03730957274807745,
    "stress5": -143.45954273453907,
    "stress10": -205.3182715534287,
    "exbest": -293.7253850607877,
    "ex3": -582.4585689585219,
    "complete_positive_months": 4,
    "complete_active_months": 11,
    "complete_positive_quarters": 2,
    "DD_UTC_dayclose": -5.31258150346231,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "R02",
    "strategy": "AttrSpyR02",
    "session_id": "c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "dashboard_url": "http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "N": 13,
    "net": 1054.7187970764467,
    "fees": 133.5756319487213,
    "PF": 2.9998802602602157,
    "DDmotor": -3.2489130528813193,
    "CAGR": 1.941860175438448,
    "time_open_pct": 6.105053424417586,
    "entry_notional_time": 0.06322744806499223,
    "stress5": 980.5101126604901,
    "stress10": 906.3014282445337,
    "exbest": 517.1645402448297,
    "ex3": -167.29651607237975,
    "complete_positive_months": 7,
    "complete_active_months": 12,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -3.248913052881297,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "R03",
    "strategy": "AttrSpyR03",
    "session_id": "205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "dashboard_url": "http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "N": 16,
    "net": 153.75236671948676,
    "fees": 145.44455054663976,
    "PF": 1.1755046430877696,
    "DDmotor": -5.546613627792163,
    "CAGR": 0.29308530234914976,
    "time_open_pct": 6.11096514275705,
    "entry_notional_time": 0.05947272629465539,
    "stress5": 72.94983863802037,
    "stress10": -7.852689443446081,
    "exbest": -276.5115457456816,
    "ex3": -647.7774062496329,
    "complete_positive_months": 9,
    "complete_active_months": 23,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -5.536279910759556,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "R04",
    "strategy": "AttrSpyR04",
    "session_id": "a657dc36-13bd-440f-a423-917ab3caeb8c",
    "dashboard_url": "http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c",
    "N": 16,
    "net": -348.5522602051562,
    "fees": 138.5202226466887,
    "PF": 0.6337677065518231,
    "DDmotor": -6.36507763263131,
    "CAGR": -0.6781506913298374,
    "time_open_pct": 4.9996350791148485,
    "entry_notional_time": 0.0494161538196295,
    "stress5": -425.50793945331657,
    "stress10": -502.4636187014769,
    "exbest": -595.0770116026313,
    "ex3": -879.0400706838409,
    "complete_positive_months": 5,
    "complete_active_months": 19,
    "complete_positive_quarters": 4,
    "DD_UTC_dayclose": -6.364185580100134,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "R05",
    "strategy": "AttrSpyR05",
    "session_id": "ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "dashboard_url": "http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "N": 9,
    "net": 143.1550705133505,
    "fees": 92.06246981327698,
    "PF": 1.4271005507452341,
    "DDmotor": -3.172735630771384,
    "CAGR": 0.2730000721026027,
    "time_open_pct": 3.7578822911192855,
    "entry_notional_time": 0.0412426233964772,
    "stress5": 92.00925395041884,
    "stress10": 40.863437387487146,
    "exbest": -156.39841665561738,
    "ex3": -310.33598206014244,
    "complete_positive_months": 5,
    "complete_active_months": 9,
    "complete_positive_quarters": 4,
    "DD_UTC_dayclose": -3.1705927902179742,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "U01",
    "strategy": "AttrSpyU01",
    "session_id": "da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "dashboard_url": "http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "N": 72,
    "net": 1874.981553550459,
    "fees": 644.7764810969313,
    "PF": 1.4081758729933123,
    "DDmotor": -11.630293408060766,
    "CAGR": 3.3510228184844726,
    "time_open_pct": 30.97404682664798,
    "entry_notional_time": 0.26339021303636406,
    "stress5": 1516.7723973854968,
    "stress10": 1158.5632412205346,
    "exbest": 1036.1887244199975,
    "ex3": -216.22479047230763,
    "complete_positive_months": 29,
    "complete_active_months": 55,
    "complete_positive_quarters": 12,
    "DD_UTC_dayclose": -11.61565814692982,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "U02",
    "strategy": "AttrSpyU02",
    "session_id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
    "dashboard_url": "http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b",
    "N": 70,
    "net": 2572.1409833508283,
    "fees": 575.5481925280554,
    "PF": 1.6407248804879624,
    "DDmotor": -5.493244162762901,
    "CAGR": 4.4881242819657,
    "time_open_pct": 31.994694050329887,
    "entry_notional_time": 0.2605476399199419,
    "stress5": 2252.3919875019083,
    "stress10": 1932.6429916529887,
    "exbest": 2005.5306829129077,
    "ex3": 959.5942650886718,
    "complete_positive_months": 27,
    "complete_active_months": 53,
    "complete_positive_quarters": 12,
    "DD_UTC_dayclose": -5.578679310841405,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "U03",
    "strategy": "AttrSpyU03",
    "session_id": "63dd9d81-c7bf-417b-823f-728977051fd8",
    "dashboard_url": "http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8",
    "N": 74,
    "net": -440.27560690769474,
    "fees": 580.7699584621895,
    "PF": 0.9008425504447655,
    "DDmotor": -14.787161148432038,
    "CAGR": -0.8598948861797129,
    "time_open_pct": 26.737972207625386,
    "entry_notional_time": 0.2281749269603607,
    "stress5": -762.925583831133,
    "stress10": -1085.5755607545716,
    "exbest": -1050.492371257966,
    "ex3": -2029.0513462937815,
    "complete_positive_months": 24,
    "complete_active_months": 56,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -14.774425567617278,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "U04",
    "strategy": "AttrSpyU04",
    "session_id": "4ac55781-679a-4d6d-a79a-320f162147b2",
    "dashboard_url": "http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2",
    "N": 79,
    "net": -1075.4610284377702,
    "fees": 538.870086556073,
    "PF": 0.7409558002321476,
    "DDmotor": -18.079394862500987,
    "CAGR": -2.1586953401382947,
    "time_open_pct": 25.902230396450047,
    "entry_notional_time": 0.1822818730405191,
    "stress5": -1374.8332987466995,
    "stress10": -1674.2055690556292,
    "exbest": -1413.3304284421129,
    "ex3": -1973.5582185412673,
    "complete_positive_months": 20,
    "complete_active_months": 55,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -18.07843793686279,
    "terminal_reconciles": true
  },
  {
    "asset": "SPY",
    "control": "U05",
    "strategy": "AttrSpyU05",
    "session_id": "37c6ae11-78b0-49c6-9b58-4c9190542841",
    "dashboard_url": "http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841",
    "N": 70,
    "net": 75.7426645169086,
    "fees": 499.6762652877322,
    "PF": 1.0200818630649156,
    "DDmotor": -16.98244814676453,
    "CAGR": 0.14483362605641759,
    "time_open_pct": 26.611125707946513,
    "entry_notional_time": 0.2103348483911586,
    "stress5": -201.85526064294223,
    "stress10": -479.45318580279366,
    "exbest": -305.6646422200623,
    "ex3": -995.5594235388447,
    "complete_positive_months": 23,
    "complete_active_months": 49,
    "complete_positive_quarters": 11,
    "DD_UTC_dayclose": -16.98190577412436,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "C0",
    "strategy": "AttrPaxgC0Retest4h",
    "session_id": "69c90bb0-e2b4-4c6a-a562-edd95399e673",
    "dashboard_url": "http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673",
    "N": 35,
    "net": 546.1105723537391,
    "fees": 246.60888105483386,
    "PF": 1.308334734611165,
    "DDmotor": -6.919378335744097,
    "CAGR": 1.0250706618597727,
    "time_open_pct": 13.357126175045252,
    "entry_notional_time": 0.10379673439549729,
    "stress5": 409.10563843438695,
    "stress10": 272.1007045150348,
    "exbest": -91.38798046904276,
    "ex3": -920.5473327487769,
    "complete_positive_months": 15,
    "complete_active_months": 31,
    "complete_positive_quarters": 8,
    "DD_UTC_dayclose": -6.921781413307038,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "Cq",
    "strategy": "AttrPaxgCqFreshRetest4h",
    "session_id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
    "dashboard_url": "http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
    "N": 35,
    "net": 546.1105723537391,
    "fees": 246.60888105483386,
    "PF": 1.308334734611165,
    "DDmotor": -6.919378335744097,
    "CAGR": 1.0250706618597727,
    "time_open_pct": 13.357126175045252,
    "entry_notional_time": 0.10379673439549729,
    "stress5": 409.10563843438695,
    "stress10": 272.1007045150348,
    "exbest": -91.38798046904276,
    "ex3": -920.5473327487769,
    "complete_positive_months": 15,
    "complete_active_months": 31,
    "complete_positive_quarters": 8,
    "DD_UTC_dayclose": -6.921781413307038,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "E1",
    "strategy": "AttrPaxgE1NoBe4h",
    "session_id": "4cc65389-4537-4e5a-a4f2-1b008214bb1b",
    "dashboard_url": "http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b",
    "N": 35,
    "net": 491.1691478843695,
    "fees": 245.3273484058306,
    "PF": 1.270951168600716,
    "DDmotor": -7.404302414804742,
    "CAGR": 0.9239110792804706,
    "time_open_pct": 13.363366322181355,
    "entry_notional_time": 0.10331003816313365,
    "stress5": 354.87617654779694,
    "stress10": 218.58320521122442,
    "exbest": -142.99809718086283,
    "ex3": -967.8437403488713,
    "complete_positive_months": 15,
    "complete_active_months": 31,
    "complete_positive_quarters": 8,
    "DD_UTC_dayclose": -7.406692973003759,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "E2",
    "strategy": "AttrPaxgE2NoTrail4h",
    "session_id": "4175efce-ac59-4c16-b23a-278fb6c9b8bc",
    "dashboard_url": "http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc",
    "N": 15,
    "net": 4325.434486548319,
    "fees": 100.76522170331324,
    "PF": 6.386025058164697,
    "DDmotor": -10.672145947980683,
    "CAGR": 7.137585313949457,
    "time_open_pct": 40.14855929234542,
    "entry_notional_time": 0.2058407012709682,
    "stress5": 4269.453807824256,
    "stress10": 4213.473129100194,
    "exbest": -793.9250957345803,
    "ex3": -798.422059528828,
    "complete_positive_months": 22,
    "complete_active_months": 37,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -10.674452139731105,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "E3",
    "strategy": "AttrPaxgE3InitialStop4h",
    "session_id": "831637c7-ade9-4be6-a15b-d568cd5d9242",
    "dashboard_url": "http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242",
    "N": 15,
    "net": 3669.3684495321963,
    "fees": 98.18488423879695,
    "PF": 4.018712149634905,
    "DDmotor": -14.745523767615577,
    "CAGR": 6.178572149107242,
    "time_open_pct": 40.56584632451685,
    "entry_notional_time": 0.2010344685193935,
    "stress5": 3614.8212916217535,
    "stress10": 3560.2741337113107,
    "exbest": -1215.5410213511036,
    "ex3": -1055.088340899572,
    "complete_positive_months": 19,
    "complete_active_months": 37,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -14.747724796307693,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "E4",
    "strategy": "AttrPaxgE4InitialStop72h4h",
    "session_id": "573cca4f-01b7-4be4-9af3-e64d9a50c837",
    "dashboard_url": "http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837",
    "N": 47,
    "net": -374.3541041358759,
    "fees": 312.57348013259855,
    "PF": 0.8286523024869447,
    "DDmotor": -6.412482041798828,
    "CAGR": -0.7291338603827469,
    "time_open_pct": 5.764837683190282,
    "entry_notional_time": 0.04255271865552756,
    "stress5": -548.0060375428751,
    "stress10": -721.6579709498743,
    "exbest": -618.4891372949257,
    "ex3": -1034.2078856149242,
    "complete_positive_months": 11,
    "complete_active_months": 30,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -6.293534846043114,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "M",
    "strategy": "AttrPaxgMMarketSignal4h",
    "session_id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
    "dashboard_url": "http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
    "N": 38,
    "net": 962.1262139358278,
    "fees": 267.71818325273483,
    "PF": 1.5743577329815752,
    "DDmotor": -7.64796155547669,
    "CAGR": 1.777532757709932,
    "time_open_pct": 15.204866584924389,
    "entry_notional_time": 0.117065150055092,
    "stress5": 813.3938899065306,
    "stress10": 664.6615658772334,
    "exbest": 337.4547898331979,
    "ex3": -635.127505102286,
    "complete_positive_months": 17,
    "complete_active_months": 31,
    "complete_positive_quarters": 10,
    "DD_UTC_dayclose": -7.65034683398127,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "R01",
    "strategy": "AttrPaxgRegimeSeed1014h",
    "session_id": "fa518c27-144f-4af4-837c-b00c837110b1",
    "dashboard_url": "http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1",
    "N": 33,
    "net": 108.95460408721488,
    "fees": 207.999658866129,
    "PF": 1.0632284670396688,
    "DDmotor": -8.419993423574446,
    "CAGR": 0.20806346552375565,
    "time_open_pct": 10.20621679219945,
    "entry_notional_time": 0.07216537592476113,
    "stress5": -6.6007619495234735,
    "stress10": -122.15612798626182,
    "exbest": -248.61793224837265,
    "ex3": -918.7622952047479,
    "complete_positive_months": 11,
    "complete_active_months": 30,
    "complete_positive_quarters": 4,
    "DD_UTC_dayclose": -8.421614424806378,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "R02",
    "strategy": "AttrPaxgRegimeSeed2024h",
    "session_id": "a8e6461e-2b14-4130-b9f6-0989a4483c8c",
    "dashboard_url": "http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c",
    "N": 30,
    "net": -153.986059114385,
    "fees": 201.6750934612561,
    "PF": 0.901581027887423,
    "DDmotor": -8.810783631607755,
    "CAGR": -0.2972040536758369,
    "time_open_pct": 8.632094062007358,
    "entry_notional_time": 0.0706245613874849,
    "stress5": -266.0277777039717,
    "stress10": -378.0694962935585,
    "exbest": -510.42873477603666,
    "ex3": -1053.1250796810994,
    "complete_positive_months": 10,
    "complete_active_months": 28,
    "complete_positive_quarters": 7,
    "DD_UTC_dayclose": -8.680467236789092,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "R03",
    "strategy": "AttrPaxgRegimeSeed3034h",
    "session_id": "0e7552b8-3491-4925-b230-f31c89b92796",
    "dashboard_url": "http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796",
    "N": 30,
    "net": 869.1587134413251,
    "fees": 192.82187705512342,
    "PF": 1.8098221924048983,
    "DDmotor": -7.269274609205656,
    "CAGR": 1.6114074512330268,
    "time_open_pct": 13.54086384071933,
    "entry_notional_time": 0.09281495138911766,
    "stress5": 762.035448410701,
    "stress10": 654.9121833800768,
    "exbest": 413.8563109430569,
    "ex3": -286.13733683210853,
    "complete_positive_months": 17,
    "complete_active_months": 30,
    "complete_positive_quarters": 7,
    "DD_UTC_dayclose": -7.2736771785766425,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "R04",
    "strategy": "AttrPaxgRegimeSeed4044h",
    "session_id": "0edfce4f-695a-4213-8426-304b9af6d5a4",
    "dashboard_url": "http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4",
    "N": 25,
    "net": 1252.4370318555846,
    "fees": 189.65373944638588,
    "PF": 2.0881540287092446,
    "DDmotor": -4.580992551167007,
    "CAGR": 2.2890676489804473,
    "time_open_pct": 11.825589712150403,
    "entry_notional_time": 0.0951177433437744,
    "stress5": 1147.0738432742592,
    "stress10": 1041.7106546929335,
    "exbest": 715.9431449407707,
    "ex3": -121.07853098667442,
    "complete_positive_months": 12,
    "complete_active_months": 24,
    "complete_positive_quarters": 8,
    "DD_UTC_dayclose": -4.48836597574277,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "R05",
    "strategy": "AttrPaxgRegimeSeed5054h",
    "session_id": "cfff7109-04c5-4420-8a90-fc19ceec6ef8",
    "dashboard_url": "http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8",
    "N": 36,
    "net": 47.8563680668258,
    "fees": 228.91731444382978,
    "PF": 1.0318390691132129,
    "DDmotor": -12.408550923653273,
    "CAGR": 0.09161267176265309,
    "time_open_pct": 13.702341332399135,
    "entry_notional_time": 0.09035797289552172,
    "stress5": -79.31991773530189,
    "stress10": -206.49620353742955,
    "exbest": -318.7382477261987,
    "ex3": -827.7787833117094,
    "complete_positive_months": 12,
    "complete_active_months": 32,
    "complete_positive_quarters": 6,
    "DD_UTC_dayclose": -12.31074513108734,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "U01",
    "strategy": "AttrPaxgUnconditionalSeed1014h",
    "session_id": "6cc08024-0aa2-4cdf-a666-25f4351681bd",
    "dashboard_url": "http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd",
    "N": 118,
    "net": 2902.3188985783913,
    "fees": 794.0684911939976,
    "PF": 1.5141207622803052,
    "DDmotor": -14.109308696330336,
    "CAGR": 5.008957309215956,
    "time_open_pct": 50.15702545688093,
    "entry_notional_time": 0.35702907919320614,
    "stress5": 2461.169736803948,
    "stress10": 2020.020575029505,
    "exbest": 2297.83236505825,
    "ex3": 1254.128240088258,
    "complete_positive_months": 32,
    "complete_active_months": 61,
    "complete_positive_quarters": 10,
    "DD_UTC_dayclose": -14.10930869633047,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "U02",
    "strategy": "AttrPaxgUnconditionalSeed2024h",
    "session_id": "4d938a9b-653e-4226-9a1c-899b689e6b62",
    "dashboard_url": "http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62",
    "N": 107,
    "net": 37.11393470002805,
    "fees": 685.4999184635236,
    "PF": 1.00668130183597,
    "DDmotor": -18.392769242805596,
    "CAGR": 0.07107890035329412,
    "time_open_pct": 39.920410754948314,
    "entry_notional_time": 0.27010513225320176,
    "stress5": -343.71935333526284,
    "stress10": -724.5526413705537,
    "exbest": -538.412619982662,
    "ex3": -1550.7874091733306,
    "complete_positive_months": 26,
    "complete_active_months": 59,
    "complete_positive_quarters": 8,
    "DD_UTC_dayclose": -18.418622808332085,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "U03",
    "strategy": "AttrPaxgUnconditionalSeed3034h",
    "session_id": "e572d0cc-9a77-4998-b2ae-ec335daadf7d",
    "dashboard_url": "http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d",
    "N": 129,
    "net": 2611.0960217982597,
    "fees": 840.2635548479908,
    "PF": 1.4023615106836755,
    "DDmotor": -19.106167261375884,
    "CAGR": 4.550144357964969,
    "time_open_pct": 51.32750919600632,
    "entry_notional_time": 0.3583015908855738,
    "stress5": 2144.282935771598,
    "stress10": 1677.4698497449367,
    "exbest": 1784.4943963902429,
    "ex3": 429.94983049966004,
    "complete_positive_months": 30,
    "complete_active_months": 60,
    "complete_positive_quarters": 10,
    "DD_UTC_dayclose": -19.108228105716208,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "U04",
    "strategy": "AttrPaxgUnconditionalSeed4044h",
    "session_id": "f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
    "dashboard_url": "http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
    "N": 126,
    "net": 1667.0255846903513,
    "fees": 863.9696181936978,
    "PF": 1.2754622165355791,
    "DDmotor": -21.721488669670087,
    "CAGR": 3.0013978599566116,
    "time_open_pct": 48.148391428738265,
    "entry_notional_time": 0.3298446745749119,
    "stress5": 1187.04246347163,
    "stress10": 707.0593422529091,
    "exbest": 1035.9108851990409,
    "ex3": -89.24104755271492,
    "complete_positive_months": 29,
    "complete_active_months": 60,
    "complete_positive_quarters": 9,
    "DD_UTC_dayclose": -21.694133630144496,
    "terminal_reconciles": true
  },
  {
    "asset": "PAXG",
    "control": "U05",
    "strategy": "AttrPaxgUnconditionalSeed5054h",
    "session_id": "54613844-7e5d-4911-9342-071f65e0922b",
    "dashboard_url": "http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b",
    "N": 122,
    "net": 3873.5353640048943,
    "fees": 932.1098628756963,
    "PF": 1.6293339988049484,
    "DDmotor": -9.73397056635823,
    "CAGR": 6.480930642303528,
    "time_open_pct": 49.79506043089857,
    "entry_notional_time": 0.39233893948730564,
    "stress5": 3355.696551296174,
    "stress10": 2837.857738587454,
    "exbest": 3159.9486035330733,
    "ex3": 1892.6570996074734,
    "complete_positive_months": 28,
    "complete_active_months": 60,
    "complete_positive_quarters": 12,
    "DD_UTC_dayclose": -9.733970566358085,
    "terminal_reconciles": true
  }
]
```
