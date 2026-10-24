# K1001 cuota1% — Guía breve para auditar Rprecio después de las corridas

Fecha: 2026-10-21. Preparación documental; sin jobs, motores, precios observados, nuevas fuentes o edición de estrategias. Fuentes finales congeladas en K1001_QUOTA_SCENARIOS_IMPLEMENTED_SOURCES_20261021.md. Ninguna fórmula de esta guía cambia decisiones o salidas.

## Unión y conciliación por cierre

1. Recuperar snapshots completos de cada escenario y todas las páginas de logs necesarias. LONG_ONLY y SHORT_BOOK se auditan por separado. No sumar cuentas, curvas o denominadores de capital. El trace no pertenece al snapshot run_analysis por defecto; no leer logs/archivos del proyecto desde analysis ni pegar arrays de resultados en código.
2. K1001_QUOTA_PRICE_TRACE.trade_id debe identificar exactamente UN trade nativo cerrado. Exigir cobertura1:1 y reportar faltantes, extras y duplicados. No hacer nearest-time join para resolver diferencias.
3. En ese trade, exit_order_id debe corresponder a su orden ejecutada de cierre. Contrastar symbol/side, qty efectiva, precio y timestamps. Si el snapshot no exporta algún campo, señalar la ausencia y recuperar por MCP la evidencia disponible; no inventarlo.
4. Unir R16_LEGACY_OPEN con la traza por origen, signal_at y opened_at, exigiendo unicidad; después validar actual_entry=trace.entry, qty, distance y geometría. R16OPEN no lleva trade_id: su asociación requiere comprobar estos campos, no sólo proximidad temporal. Si hay ambigüedad, no asignar arbitrariamente.
5. Contrastar R16_LEGACY_CLOSE con origen, evento temporal de cierre y neto del trade; verificar unicidad y secuencia. Distinguir callback time, opened_at/closed_at y timestamps de órdenes: comprobar su relación, no sustituirlos porque parezcan iguales.
6. trace.net coincide con closed_trade.pnl y el neto realizado del ledger de origen. Las sumas por origen y por año de cierre concilian con R16 y la cuenta. open_years son cohortes por apertura; close_years son cohortes por cierre. No son retornos MTM anuales ni mensuales.
7. Fees y funding se verifican desde órdenes/pagos nativos completos. No se imputan ceros por ausencia de un campo en trade; el diagnóstico previo encontró27 trades sin ese campo pero verificó sus pagos por ledger. Aplicar la misma cautela, sin presuponer la misma cantidad de casos.

Las igualdades numéricas usan primero precisión completa; reconciliación monetaria absoluta<1e-6USDT. Una tolerancia no permite emparejar otro trade, modificar qty, ignorar un fill o ajustar una frontera.

## Fórmulas e invariantes de la traza

Para un trade, E=entrada real, D=distancia inicial de precio, s=+1 long/−1 short, q=cantidad real. Rprecio(p)=s*(p−E)/D. Rprecio de salida se deriva del exit fill real; no es trace.net/(qD).

El conjunto observado incluye open0, cierres M1 del pre ESTRICTAMENTE posteriores a opened_at mientras la posición continúa abierta, y exit fill. No contiene highs/lows ni precios posteriores al cierre. Para trace_complete=true:

- D>0, E>0, precios finitos y origen permitido por el escenario.
- first_at=opened_at y last_at=closed_at; last_stage=exit.
- marks=2+m1_marks; holding0 conserva dos marcas de fases distintas aunque compartan timestamp. No deduplicar sólo por T.
- min_r<=0<=max_r y min_r<=Rsalida<=max_r.
- min/max_at están entre apertura y cierre, con fase open/pre/exit válida. Un pre extremo tiene timestamp>opened_at; nunca usar el cierre del minuto de fill.
- Cambios estrictos conservan la primera fase/fecha en empates; máximo0 puede seguir en open aunque exit vuelva a0.
- El ledger tiene fills y cierres REALES, independientes del éxito de trace; por origen, trace_completed+trace_missing=closes. Las trazas fallidas no se rellenan.
- PRETERMINAL y FINAL son snapshots que pueden superponerse. Usar la emisión terminal pertinente, sin sumar dos veces. Si hay liquidación final, el close/trace propio se completa antes de FINAL.

R16 posee un solo fill de entrada y uno de salida por trade bajo estas reglas. Si la evidencia real contradice ese supuesto, detener su simplificación por trade y conciliar cantidades efectivas de todas las órdenes; no usar solicitado como ejecutado.

No se puede auditar cada extremo M1 desde snapshots de trades que no contienen esas marcas. Los invariantes y los checks sintéticos de fuente permiten validar consistencia y algoritmo; no equivalen a reobservar cada precio del mercado. No llamar los extremos MFE/MAE exactos: son mínimos/máximos de ESTE conjunto muestreado bajo las salidas originales.

## Descriptivos útiles, sin optimizar

Publicar primero cobertura, errores y número de trades por origen/año de apertura y cierre. Luego medianas, cuartiles y rangos de min_r, max_r y Rsalida, con los tamaños de muestra y trace_missing. No tratar miles de M1 de un trade como observaciones independientes ni dar igual significado a31 runners y cientos de shorts.

Describir cuántos trades tuvieron algún mark observado de precio favorable (max_r>0), adverso (min_r<0), o ambos, junto a sus salidas reales. Un trade con max_r=0 pudo tener un movimiento favorable intraminuto no muestreado. min_r no mide qué habría ocurrido sin stop.

La diferencia max_r−Rsalida es una devolución observada desde el mejor mark incluido hasta la salida. Es no negativa en trazas válidas, pero no es dinero ejecutable en el máximo ni prueba de un trailing mejor. Describir su distribución y relación con la gestión original, sin barrer cortes de R o diseñar targets desde ella.

Tiempo hasta el primer máximo/mínimo observado y holding real pueden describirse por origen; conservar casos0 y la fase de la marca. No convertir el orden temporal de dos extremos en causalidad, ni comparar duraciones sin notar que cada gestión censura su propia trayectoria. El long deja de observarse al salir: no conocemos la tendencia posterior dentro de esta traza.

Por separado, Rneto=PnL/(qD); Rfees=fees/(qD); Rfunding=pagos_funding/(qD). La diferencia entre Rprecio de salida y Rneto debe conciliar con costes bajo la geometría real y órdenes efectivas. La reserva.001 no es débito de PnL. Si hay más de un fill, usar flujos efectivos, no forzar la identidad de un único precio promedio sin comprobarla.

Como reporte interpretativo: long con max_r elevado pero salida modesta sugiere devolución observada, no fallo probado de trailing; long con max_r pequeño aporta otra descripción. Shorts con salidas cerca de max_r no acreditan target óptimo. Los resultados por cierres TP/STOP/MARKET se mantienen descriptivos: liquidate puede etiquetar MARKET según PnL y no identifica por sí solo el motivo económico.

## Decisiones posteriores permitidas por la evidencia

Primero aceptar o rechazar integridad del trace y conciliar cuenta, sizing1% y reglas. Después explicar si la debilidad observada convive con poco avance favorable muestreado, devolución durante posiciones, costes, pocos episodios o concentración. Esa distinción es descriptiva, no identificación causal de calidad de señal frente a gestión.

No cambia por sí sola ningún target, trailing, plazo, cuota, lado, fecha o selector. No comparar ganadores aislados, eliminar tres runners ni vender una mejora hipotética. Los gates de cuenta, regularidad calendario y límites del desarrollo ampliamente reutilizado siguen separados de esta descripción. Esperar ambos resultados y su auditoría antes de decidir la siguiente investigación.
