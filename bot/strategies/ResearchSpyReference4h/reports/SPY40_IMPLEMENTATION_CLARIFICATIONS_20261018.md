# SPY40 — aclaraciones del código anteriores a corridas

Sin resultados ni lanzamiento. Matriz y adenda aprobadas gobiernan los parámetros.

- 09: en empate de bins modales, 'más cercano' se concreta como distancia del CENTRO del bin al último cierreD, seguido por índiceinferior. El target es mediana real de closes del bin ganador, no centro inventado.
- 10: 'dos tests antes de ruptura' implica invalidar episodio si un cierre atraviesa barrera antes del segundo test. No se reconvierte ese breakout prematuro en test. El nivel/dirección ya armado queda consumido; esta precisión evita replay oculto.
- B2h completos se forman por grupo independiente, como adenda: hueco enotrogrupo invalidaD pero no bloque correcto posterior.300B/400Dretención fija.
- 01: salidas de fase se guardan como deuda si faltara quote; sólo últimosvalores bandpass observados guardados, no índices dehistorial recalculado.
- 05/07: labels del origenactual noentrenan. El Dactual puede madurar label deorigenanterior y usarse entonces. Los targets a más de120h no entrenan porque la operación tendría failsafe.
- Sin loggingnuevo ni hookfinal no documentado. Countersinternos no se presentan comoartefactos exportados.

Root revisará motor+10señales y readback de cada clase antes de primer run.
