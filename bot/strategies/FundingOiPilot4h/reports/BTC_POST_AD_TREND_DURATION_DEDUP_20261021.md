# Pasada posterior a AD — duración de rachas y persistencia: descarte acotado

Fecha: 2026-10-21.
Estado: sin protocolo ejecutable ni propuesta de motores. No se consultaron resultados AA. No se crearon clases, jobs, drafts, análisis, datasets o velas nuevas.

## Pregunta examinada

¿La edad de una racha de retornos del mismo signo cambia la expectativa de continuación o agotamiento, frente a conocer sólo su dirección actual?

Es una pregunta predictiva falsable, sin necesidad de atribuir causalidad. Un contraste podría condicionar en signo y edad, frente a signo solamente, usando los mismos orígenes y etiquetas. Que la edad no aporte expectativa adicional sería un resultado adverso. Sin embargo, no basta con que una comparación pueda programarse: debe aportar información de investigación distinta frente a lo ya seleccionado.

No se fijaron horizonte, bins, truncamientos, shrinkage ni un modelo semimarkov. Esas elecciones no quedan autorizadas por este documento.

## Antecedente directo y límites de novedad

R40SpyRunDurationResponse ya calcula el signo diario y la longitud consecutiva de la racha. Condiciona en (signo, min(edad, 4)), con 252 registros, al menos 15 por grupo y shrinkage hacia media global. Su cierre es negativo en SPY; no es resultado BTC ni refutación universal de edades. Cambiar el instrumento y reloj tampoco vuelve novedosa la representación.

A cuenta persistencia de signos en dos escalas: al menos 4/6 y 16/24 movimientos en una dirección; consume cambios de estado. No es edad consecutiva, pero ya prueba formación de tendencia mediante signos. Su gestión alternativa B y la composición N conservan ese núcleo.

AngleBtcProbability4h usa dos signos para cuatro estados y aprende dos utilidades de órdenes con stops. Su diagnóstico acredita abstención por gate económico, con etiquetas maduras y cobertura. El cierre prohíbe aflojar haircut, incertidumbre o admisión para fabricar entradas. Una tabla de edad con otra muestra mínima no puede presentarse como reparación de Angle.

G usa dependencia lineal de retornos y pronóstico recursivo. R usa seis retornos ordenados normalizados L2. La normalización preserva todos sus signos. En ausencia de ceros, la edad truncada a cuatro es función exacta de los últimos cuatro signos: 1 si el último difiere del previo; 2 o 3 si la primera diferencia hacia atrás ocurre allí; y 4 si los cuatro coinciden. Por tanto, esa edad no incorpora información observada nueva respecto del vector de R. Ceros y su tratamiento tendrían que especificarse; no se usan para reclamar una brecha.

Esto no significa que KNN coseno de R estime bien todas las funciones de sus inputs. Sí significa que reemplazarlo por una tabla, una cadena de signos o una dinámica de duración sería principalmente otra restricción/estimador sobre información ya disponible. El nombre del modelo no acredita por sí solo una nueva fuente predictiva.

## Contrastes cercanos que tampoco se reabren

| Línea | Qué pregunta ya representa | Por qué no usarla para rescatar esta pasada |
|---|---|---|
| W | Tipo REV/CONT y rapidez relativa de dos primeros pasajes ATR frente a tipo solo | No es edad de signos, pero ya contrasta duración observada frente a un control con los mismos eventos. No cambiar barreras, banco, duración o etiquetas tras su cierre. |
| T | Fase de reloj UTC frente a deriva global | Edad endógena no es hora UTC; cambiar un reloj por otro no basta si la señal sólo recodifica signos ya observados. |
| N | Composición ejecutada de dos máquinas congeladas | No añadir edad para elegir sleeves, prioridad o gestión después del resultado. |
| F | Concentración RV/BV de un desplazamiento y seguimiento/reversión | No sustituir salto por racha y elegir el lado que gane. |
| K | Dominancia de semivarianza con desplazamiento pequeño | No sustituir suma cuadrática por conteo para encontrar más operaciones. |
| R | Similitud de trayectorias cortas ordenadas frente a media común | No reabrir dimensión, distancia, ventana o signo bajo etiqueta de persistencia. |

W no prueba que toda duración sea inútil. A/G/R no abarcan todo proceso de precios. La decisión aquí es de materialidad de la siguiente prueba concreta, no una demostración de imposibilidad de BTC ni de todo OHLCV.

## Fuentes y cierres leídos por MCP

Fuentes completas y hashes:
- `strategies/BtcResearchR10Base4h/__init__.py`: `2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9`.
- `strategies/AngleBtcProbability4h/__init__.py`: `d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1`.
- `strategies/R40SpyRunDurationResponse/__init__.py`: `4d3460d0924855009f3da18e4a871205921716a3e5e818e379c88c1bf8a04907`.
- `strategies/BtcResearchR12ArBase1m/__init__.py`: `1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343`.
- `strategies/BtcResearchR18AnalogueBase1m/__init__.py`: `e8fc9ba9710cef644a41e32608b3132d38d6aca55f5027f259b1c147404e9e2e`.
- `strategies/BtcResearchR23PassageBase1m/__init__.py`: `d8ac03f4b02fa3c471fdac510a6d9b2f36c2aa80cd3c0a65661a0cd887fafccc`.
- `strategies/BtcResearchR20SeasonBase1m/__init__.py`: `101e8cb82259af2b303275c19c0810b35a4cd9e5f9210f559df95ba51b39742c`.
- `strategies/BtcResearchR14CompositeBase1m/__init__.py`: `0e678d3928b8bada8981ae6a2bd5b678c3fb43950701e3d71ef843ba0cdb84d4`.
- `strategies/BtcResearchR12JumpBase1m/__init__.py`: `631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6`.
- `strategies/BtcResearchR13Semivariance1m/__init__.py`: `0e97f8bf81ace3d8874f4c7740a35deadfcd278874992ce4d1c0fb15506b586a`.

Cierres completos:
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_A_RESULTS_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_F_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_G_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_K_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_N_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_R_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_T_FINAL_20261021.md`.
- `strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_W_FINAL_20261021.md`.
- `strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_INITIAL_RESULT_20261018.md`.
- `strategies/MultiAssetRetestBtcShort4h/reports/R40_SPY_PAXG_RESEARCH_RESULTS_20261018.md`.

El historial r4 y el inventario nominal sirven como orientación, no como censo global ni prueba de que no exista otra fuente. La revisión no usó resultados AA para decidir parámetros o priorizar signos.

## Decisión y límite concreto

No recomiendo ejecutar duración de racha frente a signo con la justificación actual. La pregunta es computable y falsable, pero su propuesta más directa añade una partición/estimador sobre signos ya observados y un antecedente exacto de otra ruta. No se gana materialidad sólo por pasar de seis números a una edad.

El límite concreto de esta pasada es representacional: recodificar la misma secuencia corta de retornos no equivale a observar un mecanismo nuevo. Cambiar el plazo o ampliar memoria para salir de la equivalencia sería una elección adicional de búsqueda, no una razón económica automática. No se escogió ninguna.

No identifiqué durante esta pasada una alternativa económica suficientemente diferenciada y operacionalizable que pueda recomendar honestamente para dos motores. Eso no afirma agotamiento universal: exige seguir el inventario fuera de estos vecinos, sin prometer una receta por necesidad. AD/MAX y AC/coste minero conservan sus propios HOLD; no se cambian sus razones ni se importan datos para desbloquearlos.

Si una próxima propuesta usa la misma información, deberá expresar qué restricción predictiva distinta pone a prueba y por qué su contraste informa algo que estos cierres no resuelven. No basta declarar una nueva tabla, transformación o literatura. Esta condición es documental, no un nuevo gate estadístico ni un pedido de permiso al usuario.

Presupuesto consumido: cero. Perfil 2%/6%/3x, costes base y gestión permanecen intactos; sin live/paper, nueva economía 2026, imports, instalaciones o cambios globales. No se modificó el Hub.
