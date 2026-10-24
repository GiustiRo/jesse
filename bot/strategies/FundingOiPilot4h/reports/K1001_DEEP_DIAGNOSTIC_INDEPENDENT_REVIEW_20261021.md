# K1001: revisión independiente del diagnóstico terminado

Estado: conforme en alcance contable y descriptivo, sin nuevo defecto material identificado. Revisión sólo lectura y documental; no se ejecutaron jobs, motores, estrategias, nuevas velas ni pruebas económicas. No se modificaron archivos de root.

## Material leído

- K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md, completo.
- K1001_DEEP_DIAGNOSTIC_JOIN_CODE_V3_20261021.md, completo.
- K1001_MTM_ORIGIN_PROTOCOL_AND_CODE_20261021.md, completo.
- K1001_MONTHLY_MTM_ATTRIBUTION_20261021.json, completo recuperado en tres páginas y parseado.
- K1001_DEEP_DIAGNOSTIC_RESULT_20261021.json, completo recuperado en23 páginas de hasta1200 líneas y parseado; revisión de esquema, resúmenes por origen, cohortes y límites. No se presenta esta lectura como nueva ejecución independiente del join de192 registros.
- Fuente completa BtcResearchR11Base1m y fuente conservada BtcResearchR16LegacyBase1m, especialmente update_position/on_close_position, para contrastar fases y salidas.

## Juicio crítico

La atribución identifica las operaciones realmente seleccionadas por el libro coordinado:31 LONG_RUNNER,116 CORE_SHORT y45 SUPPLEMENT. Prioridad, ocupación, capital y tamaños históricos siguen presentes. Las contribuciones positivas no prueban tres estrategias standalone rentables ni permiten sumar curvas de nuevas cuotas. FINDINGS lo distingue expresamente y mantiene que el objetivo económico no se alcanzó.

R se define consistentemente como neto del trade dividido por qty×distancia del stop inicial acreditado en el log de apertura. El numerador contiene fees/funding; el denominador sólo riesgo de precio. No confundir PF en dólares con PF de R, media de R con retorno de cuenta, ni actual_loss del log de sizing con pérdida realizada: esa magnitud incorpora fees y reserva. Que algunas pérdidas netas excedan−1R no contradice esta definición ni autoriza recalibrar riesgo.

El join no sustituye funding ausente por cero arbitrariamente: exige ledger completo1151, ausencia de pagos para los27 campos omitidos y conciliación individual gross−fee+funding=net. Los pagos se enlazan por trade_id y se comprueba su pertenencia al intervalo de exposición. El MTM conserva la fase efectiva documentada antes del pre R11; no confunde available_at de información con asentamiento de cash.

El MTM por origen es viable por exposición única y wallet completo. Los porcentajes mensuales/anuales usan equity GLOBAL al comienzo del intervalo y son contribuciones, no rentabilidades de subcuentas. La actividad se determina por intervalos/fills, no por PnL distinto de cero. Las razones13/28,33/51,25/36 y40/58 describen contribuciones bajo esa selección; no sustituyen el gate global37/58 ni validan quitar el long. Meses calendario y parciales permanecen diferenciados.

La reconciliación en una frontera abierta es identidad por construcción: todo equity−wallet residual se asigna al único origen expuesto. No es una segunda medición independiente del precio abierto. Los controles adicionales que dan sustento al método son la ausencia comprobada de fills en los cortes,53 fronteras flat con error máximo5.82e−11, ledger terminal por origen y orden de fases acreditado en framework. No generalizar a varias posiciones con marks desconocidos. PRETERMINAL es suficiente aquí porque K ya termina flat y no hay liquidación posterior; no generalizar esa equivalencia a otras sesiones.

La clasificación de salida V3 evita inferir causa por PnL o por submitted_via aislado. Para shorts, TYPE MARKET, created_at/closed_at en el deadline y la fuente R16 con hold fijo sin trailing sostienen TIMEOUT_MARKET. TP LIMIT y STOP se distinguen por ejecución real. El long MARKET con etiqueta stop-loss conserva categoría propia: posible conversión de orden cercana a mercado no demuestra timeout ni TP. No se recomienda forzar una explicación más precisa con datos que no existen.

## Precisiones de presentación, sin cambio de resultados

1. En FINDINGS, «las comisiones nominales no cambiaron» conviene leerlo/cambiarlo por «la tasa de comisión no cambió». Los cargos efectivos en dólares y en R sí varían. La caída de media bruta observada descarta que el cambio de costos sea explicación suficiente, sin identificar causalmente su origen.
2. La resta de las tres mejores operaciones del long es una sensibilidad descriptiva de los dólares ya realizados con tamaños históricos congelados. No representa la cuenta contrafactual que habría operado sin ellas: habría cambiado equity, sizing y posiblemente selección. El texto ya impide convertirla en regla de eliminación; preservar esa salvedad.
3. Las cohortes por año de cierre y la atribución anual MTM son objetos distintos. El diagnóstico los rotula correctamente; no llamar a las medias R por año de cierre rentabilidad anual independiente.
4. PF alto y medias positivas son propiedades de esta muestra ampliamente observada, no intervalos de confianza ni evidencia de independencia estadística. No se añaden claims de significancia, robustez o causalidad.

Conclusión de revisión: el diagnóstico contesta quién aportó, cómo se distribuyeron los payoffs ejecutados y qué límites impiden inferir oportunidades censuradas. Es base documental suficiente para discutir una instrumentación posterior con preguntas prefijadas. No acredita aprobación de nuevas cuentas, modificaciones de entradas/salidas ni objetivos alcanzados.
