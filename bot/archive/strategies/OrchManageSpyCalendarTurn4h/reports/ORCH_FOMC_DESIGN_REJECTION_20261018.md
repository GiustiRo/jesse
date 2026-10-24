# Diseño pre-FOMC y revisión del ciclo FOMC — 2026-10-18

Estado: DESCARTE METODOLÓGICO PROPUESTO ANTES DE CÓDIGO O BACKTEST. Ninguna fuente, draft, corrida ni resultado propio nuevo. Este documento se guarda en la estrategia calendario existente por organización; no cambia su receta TOM ya rechazada. Calendario monetario y calendario de fin de mes son mecanismos distintos dentro de la familia amplia de información ex ante. Toda la evaluación local 2020–2025 seguiría siendo desarrollo adaptativo; 2026 permanece reservado.

## Evidencia primaria y decisión

[Lucca y Moench, NYFed Staff Report 512](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf), septiembre de 2011, revisión agosto de 2013 y publicación Journal of Finance 2015: muestra septiembre de 1994–marzo de 2011; documenta unos 49 puntos básicos medios durante la ventana 14:00→14:00 previa a anuncios programados, que entonces se publicaban habitualmente a las 14:15. El mecanismo no quedó resuelto por los modelos habituales. Es evidencia histórica del fenómeno, no una promesa de rentabilidad actual.

[Kurov, Wolfe y Gilbert, The Disappearing Pre-FOMC Announcement Drift](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3134546), escrito el 26 de septiembre de 2020, publicado en Finance Research Letters 40 (2021), DOI [10.1016/j.frl.2020.101781](https://doi.org/10.1016/j.frl.2020.101781): extiende la muestra hasta diciembre de 2019 y encuentra que el efecto prácticamente desaparece después de 2015, tanto con como sin conferencia. El abstract autoral y el del editor fueron accesibles mediante búsqueda; las aperturas directas del artículo fallaron. No se afirma haber leído sus veinte páginas completas. Esta advertencia ya existía antes de nuestra ventana común.

[Knox y Vissing-Jorgensen, revisión y extensión primaria](https://www.federalreserve.gov/econres/feds/files/2026023pap.pdf), borrador fechado agosto de 2025, alojado como FEDS 2026-023: tabla 4 compara el efecto pre-FOMC de 49 bps (t=4,61) en la muestra original con 16 bps (t=1,50) en abril de 2011–diciembre de 2023. Sección 6.2 y figura 5 muestran un ciclo inverso significativo en 2017–2021, con menor retorno en semanas pares. Es información publicada posterior al inicio del desarrollo, usada aquí como evidencia crítica; no se ha consultado rendimiento de 2026 ni se transforma esa inversión en una señal short.

Conclusión: no propongo ejecutar el drift preanuncio ni sustituirlo automáticamente por el ciclo par. La señal preanuncio ya tenía una objeción primaria anterior a 2020; el contraste reciente no la rescata con fuerza. El coste fijo de 9 bps por ida y vuelta consume una parte grande de los 16 bps medios del período posterior, antes de spread, financiación, adaptación horaria o diferencias del CFD. Esto no demuestra inexistencia del fenómeno, pero hace débil su prioridad para este proyecto.

## Adaptación de ejecución evaluada, sin implementar

Sólo SPY long, ruta de 1h y datos fuente de 1m ya disponibles. Entrada a las 14:00 America/New_York del día civil anterior al anuncio; salida a las 13:00 del día anunciado. Son 23 horas y no una réplica de las 24 horas académicas. ZoneInfo transforma DST a UTC; no fijar offsets estacionales manualmente.

Exigir al entrar una vela M1 efectivamente cerrada en ese timestamp y paridad del precio de ejecución con su cierre mediante búsqueda binaria, sin forward fill negociable. Si falta, saltar todo el evento, consumir su identificador y no entrar tarde. Una sola entrada por evento, sin reentrada después del stop. Para la salida: si falta quote, conservar deuda de salida y cerrar en el primer callback propio con quote fresca; registrar retraso y si cruza las 14:00. Por tanto no se podría afirmar que la exposición al anuncio se evita siempre. Un stop con datos ausentes tampoco garantiza salida ejecutable.

Como receta provisional de riesgo por horizonte, habría propuesto stop catastrófico fijo del 2% desde fill real, riesgo inicial máximo del 1% de equity incluyendo ambas comisiones y nocional máximo 1x, dentro del límite agregado del 8% y margen isolated 5x. Es un límite elegido ex ante para acotar una operación de aproximadamente un día, no un percentil calibrado con sus resultados ni garantía frente a gaps. Con fee 0,00045 por lado, la exposición sería aproximadamente 0,01 / (0,02 + 0,00045 × 1,98) = 0,479x; las ocho operaciones anuales costarían unos 0,72% del nocional anual, o 0,345% de equity a esa exposición, antes de otros costes. No se programa ni se propone optimizar stop, horas o tamaño tras ver resultados.

## Calendario oficial verificable y conocido con anticipación

Las siguientes publicaciones originales preceden a los años correspondientes. Las fechas enumeradas son el día final/anuncio de cada reunión programada, contrastadas con el [calendario histórico oficial](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) y la [página histórica 2020](https://www.federalreserve.gov/monetarypolicy/fomchistorical2020.htm). Se usaría exclusivamente 2020–2025.

| Año | Publicación original | Fechas programadas del anuncio |
|---|---|---|
| 2020 | [17 mayo 2019, 10:00 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20190517a.htm) | 01-29, 03-18 CANCELADA, 04-29, 06-10, 07-29, 09-16, 11-05, 12-16 |
| 2021 | [2 julio 2020, 10:00 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200702a.htm) | 01-27, 03-17, 04-28, 06-16, 07-28, 09-22, 11-03, 12-15 |
| 2022 | [4 junio 2021, 11:00 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20210604a.htm) | 01-26, 03-16, 05-04, 06-15, 07-27, 09-21, 11-02, 12-14 |
| 2023 | [24 junio 2022, 14:00 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220624a.htm) | 02-01, 03-22, 05-03, 06-14, 07-26, 09-20, 11-01, 12-13 |
| 2024 | [23 junio 2023, 11:30 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230623a.htm) | 01-31, 03-20, 05-01, 06-12, 07-31, 09-18, 11-07, 12-18 |
| 2025 | [9 agosto 2024, 13:30 EDT](https://www.federalreserve.gov/newsevents/pressreleases/monetary20240809a.htm) | 01-29, 03-19, 05-07, 06-18, 07-30, 09-17, 10-29, 12-10 |

El 15 de marzo de 2020, Powell declaró públicamente que la reunión de ese domingo sustituía a la programada para el martes y miércoles siguientes: [transcripción oficial, página 5](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20200315.pdf). Por tanto cancelar el evento previsto para el 18 antes de su entrada hipotética del 17 sería decisión ex ante legítima. Las acciones de emergencia del 3 y 15 de marzo no eran fechas programadas y se excluyen. Ninguna afecta a nuestra ventana local que empieza en octubre.

Ventana común 2020-10-15→2025-12-31 exclusivo: dos anuncios de 2020 y ocho por año de 2021 a 2025, máximo 42 eventos. No son 42 fills certificados: no se ha ejecutado auditoría de cobertura M1 en esos horarios. La muestra pequeña y los meses sin eventos se reportarían como tales; no se usarían para excluir meses del objetivo general de regularidad.

## Alternativa solicitada: ciclo FOMC

[Cieslak, Morse y Vissing-Jorgensen](https://faculty.haas.berkeley.edu/morse/research/papers/cycle_paper_cieslak_morse_vissingjorgensen.pdf), borrador autoral febrero de 2018, publicado en Journal of Finance en 2019: la muestra 1994–2016 favorece semanas 0, 2, 4 y 6. El día cero es el anuncio; semana cero abarca días -1 a 3 y las siguientes pares 9–13, 19–23 y 29–33. Se excluyen fines de semana y se conservan festivos con retorno cero: no equivale a contar barras CFD. El paper presenta validación 2014–2016 respecto de su borrador inicial; eso no convierte nuestros datos en OOS.

Para una eventual réplica haría falta respetar ese reloj, resets y festivos, además de distinguir rentabilidad excedente de un índice de PnL del proxy. La inversión posterior documentada por la extensión citada desaconseja crear ahora una receta long de semanas pares. Tampoco recomiendo invertir su signo utilizando el período 2017–2021 que se solapa parcialmente con nuestro desarrollo. No abrir una rejilla de semanas, horas ni subperíodos.

Resultado operativo de esta investigación: dos diseños razonados archivados sin corrida, manteniendo intacta la referencia y el presupuesto de pruebas. La literatura aporta motivos para abandonar una propuesta, no sólo motivos para lanzarla.
