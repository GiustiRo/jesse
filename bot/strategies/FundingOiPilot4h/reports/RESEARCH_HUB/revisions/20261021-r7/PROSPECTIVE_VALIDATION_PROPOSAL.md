# Propuesta de continuidad después de r5
Fecha: 2026-10-21. Estado: BORRADOR PARA DEBATE. No es un protocolo prerregistrado.

## Recomendación
Primero cerrar en papel la viabilidad de una validación prospectiva; después decidir si implementarla y comenzarla. La pregunta es: ¿las referencias congeladas conservan utilidad económica en datos nuevos, con instrumentos y costos representativos de lo que se querría operar?

No repetir el desarrollo 2020–2025 ni reutilizar 2026 ya observado como reserva virgen. No abrir otra búsqueda de estrategias, riesgo o asignación. Esta entrega sólo propone el diseño; no inicia captación de datos, simuladores, backtests, paper ni live.

## Lo acordado y lo que todavía se propone
Se mantiene el perfil de investigación acordado: 2% objetivo por operación, límite agregado de admisión de 6% y 3x aislado. Son reglas de dimensionamiento y admisión; no garantizan una pérdida máxima realizada de 2% o 6% ante gaps, deslizamiento y costos. No modifica el live ni otras configuraciones.

K1001 B/C permanecen como referencias heredadas y N204 B/C como controles. Ninguna es candidata aprobada. B conserva SPY Second/MECH01; C conserva SPY Market/MECH05. No elegir C por su resultado 2026 ni promover N204 automáticamente si K1001 falla.

Todo lo siguiente —horizonte, cuentas virtuales, criterios y costos— se presenta para discutir. No queda aprobado por publicarlo en el Hub.

## Paso 1: comprobar que la pregunta puede medirse
Antes de una implementación, redactar una especificación verificable:
- Instrumentos, contratos y fuentes exactas para BTC, PAXG y la exposición SPY. Su disponibilidad y equivalencia todavía deben comprobarse; el nombre del activo no basta.
- Calendarios, cierres, zona horaria y construcción de velas. Conservar las reglas existentes; adaptar horarios o filtros crea otra versión que requiere una decisión explícita.
- Comisiones aplicables, spread, profundidad, latencia, reglas de fill, tick/step/minnotional y base de disparo last/mark. Un toque de LIMIT no prueba ejecución y una MARKET no asegura el precio de señal.
- Funding por contrato: eventos, tasas, precio de liquidación y tiempos de publicación/recepción. No suponer intervalo universal ni tratar falta de datos como cero.
- Auditoría causal de señales y decisiones: distinguir el tiempo de mercado del momento en que el dato estuvo disponible.

El soporte local documentado de funding cubre BTC-USDT Binance USD-M; no acredita funding completo para PAXG/SPY. Si se necesitan contratos no soportados, habrá una tarea técnica separada que todavía no está autorizada. Tampoco está construido o verificado aquí el observador prospectivo.

Recomiendo resolver la ruta de instrumentos nativos antes de iniciar. Cambiar proxies por instrumentos nativos y agregar costos completos cambia la versión de datos/contabilidad evaluada, incluso conservando parámetros. Se conservará el original histórico y se declarará la nueva versión. Si esta ruta no es viable, volver al debate de alcance: una simulación sobre proxies respondería una pregunta más limitada.

## Paso 2: congelar un protocolo, si acordamos avanzar
Propuesta de comparación:
| Referencia | Función | Capital virtual inicial por libro |
|---|---|---|
| K1001 B | Referencia B | 10.000 USDT |
| K1001 C | Referencia C | 10.000 USDT |
| N204 B | Control comparable B | 10.000 USDT |
| N204 C | Control comparable C | 10.000 USDT |

Cada libro comparte capital entre sus tres activos. Los cuatro libros son independientes contablemente, aunque sus señales y resultados son dependientes estadísticamente. Los 10.000 son una unidad de simulación comparable con los registros revisados, no una inversión requerida. No sumar los cuatro como una cuenta real ni enviarlos a una misma cuenta one-way.

Para estudiar estrés económico de verdad propongo cuatro libros adicionales, uno por referencia, con costos adversos prefijados y sizing recalculado con su propio saldo. Presupuesto total: ocho trayectorias virtuales, cuatro principales y cuatro de estrés, sin variantes adicionales de señales, riesgo o capital. Un recargo sobre fills fijos puede acompañar como sensibilidad descriptiva, pero no sustituye esas trayectorias.

Las comisiones históricas por lado, 0,00045 nominal y 0,00095 estresado, sirven como anclas documentales, no como afirmación de tarifas actuales. Propuesta: fee base al menos el mayor entre 0,00045 y la tarifa aplicable verificada; fee estresado al menos el mayor entre 0,00095 y el base. El estrés adicional de ejecución y funding debe quedar numéricamente definido antes de T0 según el contrato y la calidad de datos, sin escogerlo mirando rentabilidad. Hoy está pendiente. La reserva de sizing histórica 0,001 no cuenta como slippage simulado.

Los libros de estrés también necesitan funding coherente con sus posiciones y fills; no sumar pérdidas o ganancias del libro nominal. Los fills serán estimaciones bajo un modelo documentado, no evidencia de que una orden real habría obtenido esa ejecución.

## Paso 3: observar una ventana nueva sin ajustar reglas
Propuesta: 12 meses corridos desde T0, común para todos los libros. T0 se fijará después del acuerdo, de la preparación técnica y del congelamiento de código, datos, costos y reglas de decisión. No se fija retroactivamente al 19 de octubre ni al comienzo de 2026. El calentamiento previo sólo inicializa estado y no cuenta como rendimiento nuevo.

Informes mensuales descriptivos y revisión de integridad a los seis meses; sin aprobación económica anticipada. Un cambio de estrategia o feed no reinicia silenciosamente el reloj ni borra resultados desfavorables.

Al cierre se incluyen posiciones abiertas a valor de mercado y costos devengados; no inventar una liquidación favorable. PF y número de trades se calculan sobre operaciones cerradas, indicando exposición abierta. El drawdown usa equity con posiciones abiertas, costos y funding, muestreada como mínimo cada minuto y en cada evento disponible; se declara que ese muestreo puede omitir extremos intraminuto.

## Criterios propuestos para debatir
Para que K1001 pueda considerarse para una siguiente fase, B y C tendrían que cumplir, cada una:
- Retorno neto anualizado de al menos 20% en la ventana completa; 30% no es un techo.
- Profit factor neto de operaciones cerradas de al menos 1,20.
- Drawdown observado de equity no superior a 25%.
- Al menos 50 operaciones cerradas.
- Resultado neto positivo en su trayectoria de estrés.

El 20% conecta con la meta del proyecto; PF 1,20 y DD 25% conservan referencias de las puertas OOS anteriores. Los 50 trades son una propuesta de suficiencia operativa para discutir, no un cálculo de potencia ni 50 observaciones independientes. Estas cifras no se aplican retroactivamente para cambiar veredictos cerrados.

Regla de decisión común al cierre de los 12 meses:
1. Fallo técnico material o ruptura del protocolo: no validable; documentar alcance y datos afectados.
2. Incumplimiento de cualquier puerta económica definida: no cumple, aunque también falte muestra.
3. Puertas económicas satisfechas pero falta de muestra en alguna K1001: inconcluso.
4. Ambas K1001 satisfacen todas las puertas y la integridad: cumplió los criterios operativos prospectivos del protocolo.

No hay extensión automática ni selección de la mejor fecha. Una continuación requeriría otra decisión que conserve todo el historial. Un cruce observado del DD de 25% ya impide satisfacer esa puerta; se registra sin rescate. Por tratarse de observación virtual, no implica alterar las reglas o cerrar posiciones a precios ficticios. Los otros indicadores se juzgan en la fecha final fijada.

Ni un año favorable ni este mínimo de trades demuestran estabilidad futura, significación estadística o 20–30% cada año. Cumplir permitiría discutir la siguiente fase; no autoriza operar.

## Qué resolvería y qué no
Resolvería si las carteras congeladas cumplen las puertas en una ventana nueva bajo los supuestos de implementación acordados. Los controles mostrarían si el resultado depende del añadido K1001 o aparece también en N204; un diferencial positivo aislado no demostraría superioridad. Registrar situaciones discordantes únicas, no contar B/C o escenarios de costos como nuevas muestras independientes.

Medir aportes por activo, concentración en grandes operaciones, meses adversos, costos y funding; correlaciones y pérdidas simultáneas al perfil fijo, con denominadores y meses sin actividad explícitos. Son diagnósticos, no nuevas palancas para ajustar reglas durante la prueba.

No acreditaría por sí solo 20–30% anual de cada operativa aislada: la atribución dentro de una cartera con capital compartido no equivale al retorno de una cuenta independiente. Recomiendo evaluar primero la cartera; la meta individual se conserva como pendiente. Si preferimos evaluar piezas aisladas primero, habrá que cambiar el alcance antes de aprobar el protocolo, sin añadir pruebas por defecto.

## Tres decisiones para nuestro debate
1. ¿La prioridad es validar la cartera conjunta, conservando la meta individual como pendiente? Recomiendo que sí.
2. ¿Aceptamos una observación de 12 meses que pueda terminar inconclusa? Recomiendo ventana fija, sin promesa de una respuesta rápida.
3. ¿El 20% será una puerta exigida o una meta orientativa? Propongo exigirlo para considerar cumplido el objetivo económico, separándolo de que el mecanismo tenga alguna utilidad.

Después de discutir esto se podría preparar el protocolo final y el alcance técnico. No se inicia una fase experimental con este borrador.

## Trazabilidad y fuentes
- Evidencia local: r6/VALIDATION_R5_RESULTS.md, r6/RESULTS.json y r5/STAGE.json del mismo Hub; originales conservados.
- Capacidad local: jesse/mcp/resources/funding.md y sección Trading Hours de jesse/mcp/resources/strategy.md; consultar antes de implementar.
- [Binance: tipos de órdenes](https://www.binance.com/en/support/faq/detail/360033779452): límites de ejecución de LIMIT y exposición de MARKET al deslizamiento.
- [Binance: funding](https://www.binance.com/en/support/faq/detail/360033525031): reglas e intervalos que deben verificarse por contrato.
- [Binance: API de datos USD-M](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data): catálogo de metadatos, funding, libros y precios de referencia; no se consultaron aquí cotizaciones ni contratos concretos.
