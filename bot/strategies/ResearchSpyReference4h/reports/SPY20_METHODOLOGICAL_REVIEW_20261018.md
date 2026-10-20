# SPY20: qué aprendimos y qué evidencia falta

Complemento crítico de SPY20_FINAL_RESULTS_20261018.md. Sin nuevos backtests, reglas o parámetros. Cuatro primarias ganaron, cuatro perdieron y dos no operaron; ninguna produjo todavía una mejora aceptada.

## Lo aprendido

**Una idea económica plausible no equivale a información suficiente.** La liquidación común SPY/PAXG, el deshacer refugio y la cascada bajista no entregaron expectativa neta en estas recetas. Varias pierden también antes de fees. Eso impide atribuir el fracaso exclusivamente a ejecución o intentar arreglarlo subiendo exposición.

**El problema de apertura no se reduce a operar más lento.** El gap aceptado02 y la recuperación cash03 soportan costes mejor que ORB/Drive intradía, pero sus ganancias son pequeñas y frágiles. 02 depende de un ganador mayor que su neto total y pierde en2024/2025;03 tiene25trades y años adversos. Se aprendió a separar dos preguntas concretas sobre precio, no a demostrar una ventaja general de calendario o sesión.

**La restricción de muestra es parte del diseño.** Las reglas de crash04/10 no generaron operaciones y06 sólo dos. Con la ventana desde octubre2020 era razonable anticipar poca potencia para eventos extremos. No es evidencia de ausencia de efecto. Tampoco permite usar su bajo DD como protección demostrada. Bajar umbrales después para obtenerN convertiría el estudio en una búsqueda diferente.

**Riesgo inicial igual no hace equivalentes las exposiciones.** Stops, nocional y capital-tiempo cambian. El retest gana más con mayor exposición y DD; las nuevas señales no demuestran dominancia ni complementariedad por tener otra frecuencia. No corresponde escalar mecánicamente para igualar ganancias ni sumar sus curvas como cartera.

**La selección observacional de datos importa.** Exigir sesiones completas elimina festivos, cierres tempranos y gaps; no reconstruye el calendario NYSE. Los snapshots de operaciones no cuantifican todas las oportunidades ni estados internos descartados. La próxima instrumentación, si se autoriza una etapa nueva, debe contar de antemano sesiones elegibles, fallos de frescura, observaciones faltantes y transiciones de estado. Así se separaría rareza económica de falta de observación, sin inferirlo retrospectivamente del número de trades.

## Evidencia que falta antes de promover02/03

- Un control de mecanismo comparable en eventos, ejecución, protección y horizonte que permita distinguir información de la condición frente a mera exposición. El retest y cash son referencias económicas útiles, pero no identifican ese efecto.
- Estabilidad que no dependa de escoger un año, una dirección o un único ganador después de verlo. Los diagnósticos por cohorte ya revelan debilidades; no son OOS limpio.
- Mejora neta incremental con costes y presupuestos coherentes. Si se estudia complementariedad, debe provenir de una cuenta compartida real y comparación de políticas predeclarada, incluyendo interacciones de tamaño y oportunidades.
- Una selección final congelada antes de cualquier evaluación realmente no utilizada. El desarrollo2020–2025 y sus múltiples cohortes ya participan en selección. Este informe no abre2026.

No se propone eliminar longs de02, cambiar el horario de03 ni reemplazar las dos recetas vacías. Sus posibles controles tendrían que diseñarse y registrarse en una fase posterior; aquí no se introduce una receta postseleccionada.

## Evitar una búsqueda indefinida

El siguiente presupuesto debe comprar una falsación concreta, no otra lista de indicadores. Antes de nuevas corridas: explicar qué dato de precio aporta información diferente, fijar un comparador interpretable, estimar si hay suficientes eventos observables y declarar cuándo se abandona la hipótesis.

Una pista marginal entre diez primarias no debe ascender por ser la mejor de la tanda. Si controles bien delimitados no separan02/03 de exposición y selección, se archivan esas recetas sin recorrer umbrales hasta encontrar un ganador. El objetivo de cartera orienta la evaluación posterior; no justifica rebajar evidencia, retirar períodos adversos ni exigir que toda señal gane en la mayoría de meses.

Los resultados actuales no obligan a funding ni a nuevas fuentes. Obligan a que cada nuevo experimento tenga una pregunta identificable y evidencia capaz de cambiar una decisión. Esta tanda ya entrega sus diez respuestas, incluidas sus limitaciones; no hay prueba de que continuar buscando parámetros produzca una mejora.
