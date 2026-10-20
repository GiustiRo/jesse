# Diagnóstico de la cartera y cambio de enfoque — 18/10/2026

El usuario plantea si la búsqueda se está estancando. Decisión vigente: terminar candidata semanal y su control ya iniciados, no abrir más variantes por ahora y diagnosticar la estructura de la cartera antes de elegir otra familia. Se conservan objetivos y 2026 reservado. Funding/VIX/COT siguen descartados.

## Método y alcance

Referencia: [combinada BTC/PAXG/SPY](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb), ventana 2020-10-15 → 2025-12-31 exclusiva. Job e95fecc2fcbf4e8eb4074bd262486c8d succeeded. Reutiliza auditor V4 con fills ejecutados, fees al tiempo de ejecución y MTM UTC. Las cuatro componentes son BTC long, BTC short, PAXG long y SPY long. Precios permanecen por símbolo; la agrupación sólo cambia la atribución. Equity diaria y retornos mensuales coinciden punto a punto con la referencia; self-tests y saldo reconciliados.

Es contabilidad de una cuenta compartida observada, no una cartera nueva. Reglas PAXG/SPY fijas no implican contribuciones futuras fijas: cambiar BTC cambia capital, reservas, tamaños y fills. No se eliminan pérdidas retrospectivamente ni se eligen los meses más fáciles de rescatar.

## Origen observado de los meses negativos

De 63 meses calendario, hay 33 positivos, 28 negativos y dos inactivos. La referencia tiene 61 meses activos.

| Signo de contribución mensual | Meses negativos de cartera |
|---|---:|
| BTC negativo, PAXG+SPY no negativos | 8 |
| BTC no negativo, PAXG+SPY negativos | 13 |
| Ambos bloques negativos | 7 |
| Total | 28 |

Cuatro de esos 28 meses no tuvieron exposición BTC. En meses completos, las categorías son 7, 12 y 7, respectivamente: 26 negativos, tres sin exposición BTC.

Suma de cambios MTM en dólares durante los meses negativos: BTC long −3.949,51; BTC short +916,39; PAXG long −6.538,96; SPY long −1.539,31. Son cambios contables durante esos meses, no resultados de una estrategia que pudiera anticiparlos ni motivo para suprimir una pata.

La brecha adicional de cartera hasta cero en un mes negativo tiene mediana de 1,3062 puntos porcentuales del equity global previo; cuartiles 1,0231 y 2,5824; rango 0,0781–7,0210. Para ser positivo hay que superar cero. Este déficit adicional es distinto de la contribución BTC total necesaria para compensar PAXG/SPY. Ninguna magnitud es una predicción.

## Concentración y duración

| Componente | Trades | Mejor trade / neto de la pata | Tres mejores / neto | Tres mejores / suma de trades ganadores |
|---|---:|---:|---:|---:|
| BTC long | 31 | 30,03% | 82,40% | 58,59% |
| BTC short | 123 | 11,26% | 30,15% | 7,99% |
| SPY long | 31 | 93,68% | 160,13% | 53,54% |
| PAXG long | 35 | 90,04% | 200,13% | 66,67% |

Ratios sobre neto pueden superar 100% porque el resto incluye pérdidas. Por eso se acompaña el denominador de suma de ganadores. En toda la cartera, los tres mejores trades representan 45,33% del neto y 19,35% de la suma de ganadores; los cinco mejores representan 69,33% y 29,59%.

Longs BTC ganadores: duración media 10,40 días, mediana 9,41; no ganadores: media 4,02, mediana 2,55. Shorts ganadores: media 0,689 días; no ganadores: 1,052. Son cohortes descriptivas, no una regla para decidir a posteriori cuánto esperar.

La concentración es compatible con una operativa tendencial, pero obliga a no confundir rentabilidad total con regularidad mensual ni a exigir progreso rápido sin comprobar que no se corta la contribución principal.

## Distancia a los objetivos

Manteniendo los 61 meses activos y todos los positivos actuales, 65% exige 40 positivos (siete más) y 70% exige 43 (diez más). Si una nueva receta activa los 63 meses, exige 41 y 45, respectivamente; además puede estropear meses ya positivos. En meses completos activos, 33/59 necesita 39 para65% o42 para70%.

Trimestres: 15/21 debe llegar a17 para80%; completos14/19 debe llegar a16. Son condiciones contables necesarias con esos denominadores, no garantías de factibilidad ni prescripción de los períodos a rescatar.

## Conclusión provisional y siguiente decisión

La evidencia justifica frenar modificaciones locales de indicadores y filtros. BTC no es el único origen de los meses malos, y sus longs capturan beneficio en pocos movimientos prolongados. Exigirle compensar las demás patas mientras se recorta esa continuación es una restricción fuerte.

No demuestra imposibilidad de mejorar sólo BTC ni autoriza cambiar PAXG/SPY por cuenta propia. Tras cerrar las dos corridas semanales, el siguiente paso es debatir si el alcance debe ampliarse a estudiar complementariedad y mecanismos de las tres patas usando datos ya disponibles, o mantener BTC como único activo modificable con un presupuesto explícito de hipótesis. No se rebajan los objetivos ni se abre2026. La selección acumulada sobre2020–2025 exige tratar cualquier futura mejora como desarrollo, no validación independiente.

## Atribución trimestral comprobada

Ampliación del análisis en job6767173c23d84f06bb9f7af287b9ab6f succeeded. Se suman cambios MTM en dólares y se dividen por equity de inicio de trimestre; no se suman retornos mensuales. La suma de componentes coincide con el retorno trimestral.

Hay seis trimestres negativos incluyendo el último parcial: uno BTC negativo y otros no negativos, dos BTC no negativo y otros negativos, tres ambos negativos. Durante esos trimestres, cambios MTM: BTC long −1.657,47; BTC short +963,12; PAXG long −2.496,60; SPY long −576,10. Déficits hasta cero: 2021Q2 3,6479 pp; 2022Q2 0,0781; 2022Q3 1,5179; 2023Q3 4,2364; 2024Q3 3,8739; 2025Q4 parcial 2,7766. Son déficits históricos, no períodos a seleccionar mediante un oráculo.

Las comparaciones semanales también concluyeron: candidata23,25%CAGR/34de61mesesactivos, control30,63%/33de62; ambas14de21trimestres. Candidata descartada, control no seleccionable. Mayor rentabilidad del control no resuelve regularidad. El usuario AUTORIZÓ investigar BTC/PAXG/SPY como cartera. Posteriormente reabrió estudio documental de funding y modelos open source/ML; no hay descargas o integración automática.
