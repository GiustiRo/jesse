# Walk-forward exploración V1 — resultado final
Fecha2026-10-20. **SIN_CANDIDATA** en los cuatro cortes. Fase2 completa,96sesiones económicas terminadas:48train+48evaluación. No hay finalistas para fase3.

## Alcance y selección
BTC-USDT Binance Perpetual, decisiones4h/ejecución1m,10000USDT iniciales por sesión,isolated3x,riesgo2% al stop+fees. Fee.00045;slippage nominal0;funding contable activo en TODAS las variantes. Los costes de funding proxy y el archivoOI retrospectivo conservan los límites del freeze.
H1=continuación evitando funding adverso;H2=reversión de ruptura con extremo contrarian;H3=normalización de funding y régimen por precio. P/PF/POI/PFOI son las12configuraciones prerregistradas, sin tuning posterior.
Train expansivo desde2020-09-01. Evaluaciones:E1ene-jun2022,E2jul-dic2022,E3ene-jun2023,E4jul-dic2023;fin exclusivo. Selección train>=30trades,neto>0,PF>=1.2,absDD<=25%;desempates congelados. Ninguna pasó, por lo que el selector estuvo plano.

| Corte | Selección guardada UTC | Primer arranque evaluación UTC | Decisión |
|---|---|---|---|
| E1 | 2026-10-20T20:54:28.856Z | 2026-10-20T20:54:30.063Z | SIN_CANDIDATA |
| E2 | 2026-10-20T21:11:20.750Z | 2026-10-20T21:11:21.837Z | SIN_CANDIDATA |
| E3 | 2026-10-20T21:26:52.143Z | 2026-10-20T21:26:53.178Z | SIN_CANDIDATA |
| E4 | 2026-10-20T21:43:24.391Z | 2026-10-20T21:43:25.332Z | SIN_CANDIDATA |

## Ablaciones de evaluación: investigación diagnóstica
No son resultados de candidatas seleccionadas. PF agrega sólo trades de evaluación no solapados de cada configuración;N excluye train y pilotos anteriores.

| Configuración | E1 neto% | E2 neto% | E3 neto% | E4 neto% | PF agregado | N eval | Semestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
| H1_P | -10.94 | -10.94 | 20.32 | -5.99 | 0.975 | 342 | 1/4 |
| H1_PF | -6.23 | -14.15 | 19.80 | -2.05 | 0.991 | 329 | 1/4 |
| H1_PFOI | 11.40 | -8.93 | 7.30 | -6.52 | 1.016 | 219 | 2/4 |
| H1_POI | 8.92 | -5.52 | 11.94 | -6.62 | 1.042 | 228 | 2/4 |
| H2_P | 4.84 | -14.40 | -7.44 | -4.91 | 0.806 | 124 | 1/4 |
| H2_PF | -1.47 | 0.00 | 0.00 | 0.00 | 0.269 | 2 | 0/4 |
| H2_PFOI | 0.00 | 0.00 | 0.00 | 0.00 | — | 0 | 0/4 |
| H2_POI | -2.23 | -10.74 | 0.48 | 0.40 | 0.799 | 69 | 2/4 |
| H3_P | -27.52 | -11.62 | -1.32 | 18.08 | 0.957 | 672 | 1/4 |
| H3_PF | 4.50 | -3.89 | -7.43 | 3.11 | 0.819 | 28 | 2/4 |
| H3_PFOI | 2.76 | -3.51 | -3.96 | 0.17 | 0.593 | 15 | 2/4 |
| H3_POI | -2.97 | -17.31 | 40.19 | -13.09 | 1.018 | 477 | 1/4 |

No sumar balances de sesiones independientes ni interpretar cuatro netos nominales como rendimiento de una cuenta continua. Cada fold reinicia10000;no se hizo replay de capital continuo. Los reportes por etapa contienen DD de motor,meses,precio bruto,fees,funding,exposición y desgloses long/short.
Fuentes completas por etapa: WALK_FORWARD_E1T_RESULTS.md,E1V,E2T,E2V,E3T,E3V,E4T,E4V en esta carpeta, con su prefijo WALK_FORWARD_ y sufijo _RESULTS.md. Registro completo con dashboard_url,código,hashes,config y tiempos:registry.json. Comparación por snapshots MCP:WALK_FORWARD_COMPARISON_V1.json.

## Qué aportaron las features
OI mejoró retorno de H1 en E1/E2 y redujo DD frente a P en los cuatro semestres, pero empeoró el retorno en E3/E4 y su PF agregado sólo alcanzó1.042. Es un cambio de exposición/selección de trades, no ventaja estable validada.
Combinar funding con OI redujo el PF agregado de H1 de1.042 a1.016. La señal funding aislada en H1 tuvo PF.991 frente a.975 del control, ambos por debajo de1. No domina consistentemente los folds.
H3+OI ganó40.19% en E3,pero perdió E1/E2/E4,con PF agregado1.018. Su train E3 había perdido54.04% y alcanzadoDD−59.66%. Ese semestre ganador no permite promoverla a posteriori.
H2 con funding sólo produjo2trades en evaluación y la combinación ninguno;H3 con funding28y combinada15. La escasez de señal no se presenta como robustez por tener DD pequeño.
Estos resultados rechazan esta especificación V1 bajo sus criterios. No demuestran que toda información funding/OI carezca de utilidad ni que exista una regla universal mejor.

## Contadores operativos,48sesiones de evaluación
Partición primaria por oportunidad,con prioridad congelada. Los flags simultáneos,mes/dirección,barras y entradas están en AUDIT_<nombreestrategia>.json por sesión;pueden coexistir y no se suman como trades independientes.
Las oportunidades cambian al cambiar exposición y días ya usados;la diferencia entre dos filas no es un A/B trade a trade con la misma máscara. Se verificaron todas las96sesiones,incluyendo train. Cada barra está en una causa primaria y cada allowed corresponde a una entrada.

| Configuración | Oportunidades | Entradas | Funding calidad | Funding económico | OI calidad/inicialización/ref | OI no creciente |
|---|---:|---:|---:|---:|---:|---:|
| H1_P | 342 | 342 | 0 | 0 | 0 | 0 |
| H1_PF | 356 | 329 | 22 | 5 | 0 | 0 |
| H1_PFOI | 524 | 219 | 22 | 19 | 1 | 263 |
| H1_POI | 510 | 228 | 0 | 0 | 1 | 281 |
| H2_P | 124 | 124 | 0 | 0 | 0 | 0 |
| H2_PF | 141 | 2 | 5 | 134 | 0 | 0 |
| H2_PFOI | 141 | 0 | 5 | 134 | 0 | 2 |
| H2_POI | 131 | 69 | 0 | 0 | 0 | 62 |
| H3_P | 672 | 672 | 0 | 0 | 0 | 0 |
| H3_PF | 2577 | 28 | 75 | 2474 | 0 | 0 |
| H3_PFOI | 2617 | 15 | 75 | 2510 | 0 | 17 |
| H3_POI | 1312 | 477 | 0 | 0 | 19 | 816 |

Dato ausente,stale,cero actual,inicialización y referencia inválida se conservan separados en los JSON,no se agrupan para la auditoría. La tabla resume para lectura. Los cierres forzados posteriores a before_terminate se contabilizan aparte en forced_final_exit_after_audit y concilian con trades finalizados.
Un lector inicial pidió una página demasiado corta y obtuvo5/6meses en una sesión con cierre forzado:se amplió sólo la lectura de logs, sin repetir backtests ni cambiar señales. Todos los meses quedaron verificados.

## Concentración y meses
Las únicas configuraciones con suma nominal positiva de sus cuatro evaluaciones son H1_POI,H1_PFOI,H3_POI. En las tres cambia el signo al retirar su mejor semestre:
| Configuración | Suma nominal de netos% sin mejor semestre | Mejor trade / neto nominal sumado |
|---|---:|---:|
| H1_POI | -3.22 | 48.85% |
| H1_PFOI | -8.14 | 131.95% |
| H3_POI | -33.38 | 75.48% |
La suma es una descripción de cuatro sesiones10000independientes,no una rentabilidad de cuenta;el cociente de concentración usa esa misma convención. No se inventa un umbral de concentración tras resultados.
Meses de cada configuración:JSON completos en los reportes por etapa. Muestreo diario00:00/00:01 rotulado como día anterior,excepto saldo inicial;el borde mensual es aproximado hasta un minuto. Incluye saldo de cierre final en el último mes,no agrega un mes fuera de la ventana. No es DD intraminuto.
Selector:24meses completos enero2022–diciembre2023, todos0%,mediana0%,peor0%,ningún mes ganador/perdedor y0trades. Índice convencional10000plano,DD0 por ausencia de exposición,PF indefinido. Esto NO supera los gates neto>0/PF>=1.2/N>=100ni acredita la meta anual20–30%.

## Verificación y reproducción
Todos los análisis usan snapshots completos por MCP;máximo error contable observado5.093170329928398e-11USDT frente a tolerancia1e-6. Precio bruto−fees+funding=PNL;ledger vinculado por trade;fees/funding/saldo final conciliados. No se mezclan trades repetidos de train con evaluación.
Los self-checks de prefijos/mutación futura se ejecutaron en todas las sesiones;pasaron las comprobaciones runtime de disponibilidad,riesgo al stop nominal y saldo por trade. Fuente común SHA2564512d21d8bab7bd33389db6e32315cf4ffaf50955cfa6e03f48d25082c1c2546,fuente completa y cada subclase/hash en registry,con12snapshots framework FRAMEWORK_*.py. Los cinco archivos de integración mantienen los hashes registrados antes del primer resultado. Los snapshots preservan esos bytes UTF8.
Fase0:7intentos técnicos documentados,279tests previos y Pyrefly0errores. Slippage5bps efectivamente verificado en fills técnicos,no sólo haircut de PNL. Eso no valida robustez económica de ninguna de estas estrategias.
Durante investigación,un timeout al arrancar H2_P_E1T se recuperó leyendo la MISMA sesión running y luego finished. No hubo arranque duplicado. Se volvió a ejecución serial. Duración de motor acumulada826.70s;no equivale a tiempo de pared,MCP/arranque/importación de módulos/gráficos se reportan aparte. Cada duración individual y excepción está abajo.

## Salida del ciclo
FROZEN_SHORTLIST_V1.md queda vacío por regla prerregistrada:ninguna configuración fue seleccionada siquiera una vez. No se abre confirmación2024–2025 ni se gastan sesiones de robustez en finalistas inexistentes. Presupuesto usado96/160económicas;los64restantes no se reasignan a nuevos parámetros.
Sin nueva consulta económica2026,ML,live/paper,Pi,órdenes,commit/push,cambio global ni sustitución de datasets. El backend local queda disponible y no quedan backtests activos.
Una nueva investigación requerirá versiónV2 con hipótesis,datos,criterios y presupuesto registrados antes de resultados. No relajar estaV1para promover un semestre ganador.

## Sesiones económicas y duración de motor
| Etapa | ID | Dashboard | Segundos | Estado/incidente |
|---|---|---|---:|---|
| E1T | H1_P | [sesión](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770) | 10.69 | finished |
| E1T | H1_PF | [sesión](http://localhost:9200/#/backtest/d3ea7127-8add-4952-8143-bf4c26f69958) | 10.63 | finished |
| E1T | H1_POI | [sesión](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644) | 10.35 | finished |
| E1T | H1_PFOI | [sesión](http://localhost:9200/#/backtest/279d4b93-7932-41a8-9b38-14077469675d) | 10.31 | finished |
| E1T | H2_P | [sesión](http://localhost:9200/#/backtest/232577e2-4517-4257-a069-53217d2c6da8) | 9.81 | Timeout de arranque recuperado; no relanzada |
| E1T | H2_PF | [sesión](http://localhost:9200/#/backtest/969b42d2-0136-488e-915c-0065bc61f839) | 14.22 | finished |
| E1T | H2_POI | [sesión](http://localhost:9200/#/backtest/e7506dac-942f-4cf0-bae7-8608d184490f) | 10.69 | finished |
| E1T | H2_PFOI | [sesión](http://localhost:9200/#/backtest/91ad7aa1-3553-44d3-ad00-64777281ce3b) | 9.67 | finished |
| E1T | H3_P | [sesión](http://localhost:9200/#/backtest/db1f164b-17e3-4dac-8580-bbcdcf6815e9) | 16.22 | finished |
| E1T | H3_PF | [sesión](http://localhost:9200/#/backtest/8b0c6493-efad-40e5-bb12-97a89a821bbb) | 9.91 | finished |
| E1T | H3_POI | [sesión](http://localhost:9200/#/backtest/fdb13394-9dd1-40bf-b0f4-e5136d6c8115) | 14.80 | finished |
| E1T | H3_PFOI | [sesión](http://localhost:9200/#/backtest/18c9272f-edd7-481e-8d8b-2a056e136adc) | 9.20 | finished |
| E1V | H1_P | [sesión](http://localhost:9200/#/backtest/ed789043-2aa2-4714-8963-112eadbc56b8) | 4.51 | finished |
| E1V | H1_PF | [sesión](http://localhost:9200/#/backtest/7ea4be97-2bdc-4bfd-a7d3-401b39af2a40) | 4.63 | finished |
| E1V | H1_POI | [sesión](http://localhost:9200/#/backtest/88e7e822-cb4d-49f7-97ab-ec5743786d29) | 4.22 | finished |
| E1V | H1_PFOI | [sesión](http://localhost:9200/#/backtest/d2c228a6-1cc3-4ca4-b452-424d137c2e2d) | 4.22 | finished |
| E1V | H2_P | [sesión](http://localhost:9200/#/backtest/801e04d7-eb9b-4d92-bc49-7fc2db1fe5cb) | 4.40 | finished |
| E1V | H2_PF | [sesión](http://localhost:9200/#/backtest/372dea0d-af5b-4c45-a712-7b199e4f35fd) | 3.73 | finished |
| E1V | H2_POI | [sesión](http://localhost:9200/#/backtest/6ed903fb-abca-4f00-aadb-a841e8f2d45e) | 4.07 | finished |
| E1V | H2_PFOI | [sesión](http://localhost:9200/#/backtest/76d2e287-1535-4574-ab52-90622ab3b3de) | 3.56 | finished |
| E1V | H3_P | [sesión](http://localhost:9200/#/backtest/5a8a5b98-c60d-46c7-98a1-b256e8575cbf) | 5.76 | finished |
| E1V | H3_PF | [sesión](http://localhost:9200/#/backtest/d79395ab-ab58-4bcc-b4b8-88a363e78bb0) | 3.38 | finished |
| E1V | H3_POI | [sesión](http://localhost:9200/#/backtest/6d688cbc-1adf-4452-a3c9-99a111221146) | 4.68 | finished |
| E1V | H3_PFOI | [sesión](http://localhost:9200/#/backtest/f21f62e6-8b5e-40c0-a108-e564ccfc8562) | 3.54 | finished |
| E2T | H1_P | [sesión](http://localhost:9200/#/backtest/8042b1d6-268a-4c60-9545-1147b44f9851) | 14.36 | finished |
| E2T | H1_PF | [sesión](http://localhost:9200/#/backtest/98a15e51-90f1-4b4d-a5a6-2ed42f6c36e0) | 14.26 | finished |
| E2T | H1_POI | [sesión](http://localhost:9200/#/backtest/aa5a6fd5-08c4-4ce8-9d2e-c9ada34fbe9b) | 13.62 | finished |
| E2T | H1_PFOI | [sesión](http://localhost:9200/#/backtest/2ecc415d-5070-405d-b941-e1329a9524e6) | 12.27 | finished |
| E2T | H2_P | [sesión](http://localhost:9200/#/backtest/58662d33-5a67-4db4-8b66-58172bfb052e) | 11.23 | finished |
| E2T | H2_PF | [sesión](http://localhost:9200/#/backtest/cdaa5c6b-6406-4049-9ac1-18b803045e2a) | 10.33 | finished |
| E2T | H2_POI | [sesión](http://localhost:9200/#/backtest/79742595-c37a-45f7-9f90-c913759abe87) | 10.49 | finished |
| E2T | H2_PFOI | [sesión](http://localhost:9200/#/backtest/2e436b8e-0c9a-4a57-a3a0-6116aa5618e1) | 10.08 | finished |
| E2T | H3_P | [sesión](http://localhost:9200/#/backtest/eef318bf-6b93-4de2-9cef-f8512d472011) | 15.96 | finished |
| E2T | H3_PF | [sesión](http://localhost:9200/#/backtest/2be7a6c4-381b-4353-a473-b6a29b3d6892) | 11.16 | finished |
| E2T | H3_POI | [sesión](http://localhost:9200/#/backtest/0a4a627c-d324-4a0d-9697-e939375859cb) | 14.54 | finished |
| E2T | H3_PFOI | [sesión](http://localhost:9200/#/backtest/2e2b071a-f85f-42ba-9f5d-13107abd5723) | 12.78 | finished |
| E2V | H1_P | [sesión](http://localhost:9200/#/backtest/5ba6d867-c4ca-477a-bd8f-25353a8a9eb7) | 4.82 | finished |
| E2V | H1_PF | [sesión](http://localhost:9200/#/backtest/a5d0a2ec-2c93-438a-b8e1-c4904c9effc8) | 3.91 | finished |
| E2V | H1_POI | [sesión](http://localhost:9200/#/backtest/2a0cb7a0-f1eb-4b57-ade5-7132dfd0106f) | 3.70 | finished |
| E2V | H1_PFOI | [sesión](http://localhost:9200/#/backtest/90be152d-6530-4e40-9bac-8067ccd169db) | 3.59 | finished |
| E2V | H2_P | [sesión](http://localhost:9200/#/backtest/5a46a1f1-df6e-41ba-a8de-495e07a1421a) | 3.33 | finished |
| E2V | H2_PF | [sesión](http://localhost:9200/#/backtest/cce04e8d-ad70-4052-86c4-517d366d6edd) | 2.96 | finished |
| E2V | H2_POI | [sesión](http://localhost:9200/#/backtest/bb3ade90-a481-4f9e-beeb-4f715d9a32e4) | 3.32 | finished |
| E2V | H2_PFOI | [sesión](http://localhost:9200/#/backtest/21c23ca0-a816-4416-b0bc-c5b67c0f6772) | 3.12 | finished |
| E2V | H3_P | [sesión](http://localhost:9200/#/backtest/0a64060d-6f97-4f56-bdd0-323aace59405) | 4.52 | finished |
| E2V | H3_PF | [sesión](http://localhost:9200/#/backtest/ebc60c54-a190-465a-9584-5702df136796) | 3.32 | finished |
| E2V | H3_POI | [sesión](http://localhost:9200/#/backtest/241076dd-c905-4237-a1aa-3ddf2a405fa8) | 4.25 | finished |
| E2V | H3_PFOI | [sesión](http://localhost:9200/#/backtest/2ee58971-a2f6-4249-9e8a-454006769816) | 3.04 | finished |
| E3T | H1_P | [sesión](http://localhost:9200/#/backtest/1f11e4be-bb91-4445-b6df-662f909ed76d) | 15.51 | finished |
| E3T | H1_PF | [sesión](http://localhost:9200/#/backtest/f97329c8-b084-4d4f-b102-098172629c6a) | 14.44 | finished |
| E3T | H1_POI | [sesión](http://localhost:9200/#/backtest/d546fc9f-90bf-45d4-85b7-fa6d29d4736f) | 13.73 | finished |
| E3T | H1_PFOI | [sesión](http://localhost:9200/#/backtest/7aaa0d64-eb5e-4096-8dc4-5fe3058d6411) | 14.10 | finished |
| E3T | H2_P | [sesión](http://localhost:9200/#/backtest/f9de72a4-6440-42f5-aca3-e418cf55ee44) | 12.40 | finished |
| E3T | H2_PF | [sesión](http://localhost:9200/#/backtest/097151bc-8183-4348-892c-4bbf1f07ee73) | 13.63 | finished |
| E3T | H2_POI | [sesión](http://localhost:9200/#/backtest/8bd7e5b0-9015-4292-98b9-708da3278fd5) | 12.71 | finished |
| E3T | H2_PFOI | [sesión](http://localhost:9200/#/backtest/083ce1ce-3167-46f9-abb4-9edb7329c4f5) | 11.23 | finished |
| E3T | H3_P | [sesión](http://localhost:9200/#/backtest/9356960c-5f31-4caa-b688-3871672fea49) | 17.49 | finished |
| E3T | H3_PF | [sesión](http://localhost:9200/#/backtest/732911a4-c86c-42c5-a964-79ed962f820a) | 11.88 | finished |
| E3T | H3_POI | [sesión](http://localhost:9200/#/backtest/d7b8a609-4cc9-4809-8f95-e03fd16ac691) | 15.38 | finished |
| E3T | H3_PFOI | [sesión](http://localhost:9200/#/backtest/6fa05f22-05c6-4f5a-9e88-4e8280a43912) | 11.80 | finished |
| E3V | H1_P | [sesión](http://localhost:9200/#/backtest/853089c6-86ed-4e36-a30e-833b61c5b382) | 3.99 | finished |
| E3V | H1_PF | [sesión](http://localhost:9200/#/backtest/75a05170-6a21-461d-ae17-a87c8d7cca30) | 3.85 | finished |
| E3V | H1_POI | [sesión](http://localhost:9200/#/backtest/22f19971-2e43-4987-b915-8a8504dea4f0) | 3.54 | finished |
| E3V | H1_PFOI | [sesión](http://localhost:9200/#/backtest/0910f976-03e3-4d8f-a9f3-1f654b41f853) | 3.36 | finished |
| E3V | H2_P | [sesión](http://localhost:9200/#/backtest/201fc419-1e0c-4245-baa2-79a5bf7df80a) | 3.52 | finished |
| E3V | H2_PF | [sesión](http://localhost:9200/#/backtest/9e719e69-81e6-43b5-b814-5bc0d02e1ee2) | 2.89 | finished |
| E3V | H2_POI | [sesión](http://localhost:9200/#/backtest/ba6a2f8a-6bff-4c29-b4d4-83fe3808b578) | 3.04 | finished |
| E3V | H2_PFOI | [sesión](http://localhost:9200/#/backtest/6b6cbe4e-c30e-4c77-a34f-d93dc6cfe833) | 3.08 | finished |
| E3V | H3_P | [sesión](http://localhost:9200/#/backtest/8bf944d4-de4b-450a-ba9d-2aee9399d84e) | 4.34 | finished |
| E3V | H3_PF | [sesión](http://localhost:9200/#/backtest/c7abf3e9-0f5f-4c07-b4b4-20249105fcd6) | 2.97 | finished |
| E3V | H3_POI | [sesión](http://localhost:9200/#/backtest/fec06767-c58f-4c48-889d-96fb2840bad4) | 4.10 | finished |
| E3V | H3_PFOI | [sesión](http://localhost:9200/#/backtest/c6f6d185-d860-49b3-ab78-0fdd630f5dd3) | 2.95 | finished |
| E4T | H1_P | [sesión](http://localhost:9200/#/backtest/32a12c2b-8c77-46b8-92b6-a905f6577c3d) | 17.30 | finished |
| E4T | H1_PF | [sesión](http://localhost:9200/#/backtest/2e11d184-8f0e-41d4-bbd0-36f60b08c1c8) | 17.19 | finished |
| E4T | H1_POI | [sesión](http://localhost:9200/#/backtest/34995866-f432-45ce-9611-93ae23b9b91c) | 21.17 | finished |
| E4T | H1_PFOI | [sesión](http://localhost:9200/#/backtest/3aeb8ed2-0c9b-4e79-96b5-4aea50a50f6c) | 16.17 | finished |
| E4T | H2_P | [sesión](http://localhost:9200/#/backtest/0277973d-e8af-4e40-8d90-47429c3d040b) | 15.28 | finished |
| E4T | H2_PF | [sesión](http://localhost:9200/#/backtest/713a0888-ca63-4b98-ab26-165a83f57b0d) | 13.39 | finished |
| E4T | H2_POI | [sesión](http://localhost:9200/#/backtest/7c992620-282b-41ef-b10f-05465afdf269) | 14.54 | finished |
| E4T | H2_PFOI | [sesión](http://localhost:9200/#/backtest/e0e8d591-8633-4a09-b874-4d30d8299963) | 13.45 | finished |
| E4T | H3_P | [sesión](http://localhost:9200/#/backtest/dedaac18-1491-478d-92dd-3ba9913efdb8) | 20.78 | finished |
| E4T | H3_PF | [sesión](http://localhost:9200/#/backtest/76f47461-5b27-4ca6-af5e-4e322d487e32) | 14.04 | finished |
| E4T | H3_POI | [sesión](http://localhost:9200/#/backtest/18d403c9-9f86-4f3f-9253-c0d601884718) | 19.17 | finished |
| E4T | H3_PFOI | [sesión](http://localhost:9200/#/backtest/2f3bada8-e82b-4268-a59d-c3338bc359b1) | 14.18 | finished |
| E4V | H1_P | [sesión](http://localhost:9200/#/backtest/c29d757d-c834-49ba-8145-fbe8c952cc4f) | 3.77 | finished |
| E4V | H1_PF | [sesión](http://localhost:9200/#/backtest/2556bc80-1e69-4196-ba55-d87646c46459) | 3.51 | finished |
| E4V | H1_POI | [sesión](http://localhost:9200/#/backtest/706268de-8c74-401c-a17a-8bb9d55d6767) | 3.43 | finished |
| E4V | H1_PFOI | [sesión](http://localhost:9200/#/backtest/e62bb0ab-f354-41f0-819c-644f24c2336d) | 3.39 | finished |
| E4V | H2_P | [sesión](http://localhost:9200/#/backtest/c14e42b9-192b-4e9a-933e-24b7dbb29ec9) | 3.08 | finished |
| E4V | H2_PF | [sesión](http://localhost:9200/#/backtest/79b80520-9207-4878-826c-9f87c888f1f7) | 2.94 | finished |
| E4V | H2_POI | [sesión](http://localhost:9200/#/backtest/75618e87-4f6a-4249-b69d-dfbc124ac12f) | 3.37 | finished |
| E4V | H2_PFOI | [sesión](http://localhost:9200/#/backtest/045b1386-b9e6-4862-bc80-1b8c98d8a95c) | 3.25 | finished |
| E4V | H3_P | [sesión](http://localhost:9200/#/backtest/bed27bc9-4f98-40c4-b848-261a5f55e541) | 4.93 | finished |
| E4V | H3_PF | [sesión](http://localhost:9200/#/backtest/dd024a64-431d-4c23-835d-39b311415509) | 3.10 | finished |
| E4V | H3_POI | [sesión](http://localhost:9200/#/backtest/1a8bdcf1-bddb-4baa-93a8-113e2213f258) | 4.13 | finished |
| E4V | H3_PFOI | [sesión](http://localhost:9200/#/backtest/be11950c-23b5-4fea-8b63-44db06b49ddc) | 3.05 | finished |
