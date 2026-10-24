# BTC valor diario: check preparado, pendiente de fuente final
Fecha: 22 de octubre de 2026. Especificación y oráculos fijados antes de implementar. NO se ejecutó un job, no hay fuente nueva y no se afirma PASS. Tras aprobar la ABI aislada, se enlazarán estos casos a los textos supplied-source/AST reales; un modelo que repita fórmulas sin invocar la fuente no será prueba de implementación.

## Oráculos numéricos independientes
Valores ilustrativos fabricados, sin precios observados:
- G=100, C_S=95, C_T=97, ATR_S=2: long; si ATR_T=2, d=4, SL=93, TP VALUE=100 y TP R2=105. Mismo entry/riesgo, captura distinta.
- Reflejo p'=200-p: C_S=105, C_T=103, G=100; short, SL=107, TP VALUE=100 y TP R2=95. Ambos lados existen por regla, no por resultados.
- Long exterior en igualdad C_S=96, C_T=97 admite; short C_S=104, C_T=103 admite.
- Recuperación plana (95→95), centro alcanzado (95→100), centro cruzado (95→101) o dirección equivocada (95→94) rechazan. Reflejos idénticos.
- ATR_S previo no puede incluir B: mutar el rango de B cambia ATR_T/d pero no ATR_S ni G. ATR_T y ATR_S se cotejan con media manual de14TR, no con otra llamada al mismo helper.
- Con volumen positivo concentrado en precios HLC3=100 y volumen cero en la última M1 cuyo close95, G sigue100; el último close es válido para C_S. Con TODOS los volúmenes cero el ancla es inválida. No sustituirla por TWAP o último precio.

## Matriz que ejecutará el harness con la fuente
|Área|Casos y resultado exigido|
|---|---|
|Reloj|T08/12/16/20; S04/08/12/16 y tamaños240/480/720/960. T04 inmaduro sin consumir; T00 sin entradas. Reinicio de D causal.|
|As-of|Referencia exactamente[D,S). Añadir/mutar M1 de B o posterior no cambia G. No leer S como si fuese el close de B.|
|Calidad|Gaps, duplicados, timestamp fraccional, OHLC inválido, V negativo/no finito y V todo0 invalidan el día. V0 parcial permitido. Ventanas válidas al día siguiente recuperan.|
|Paridad|OHLC agregado por bloque frente a4h; último close M1=C_S; C_T=self.price. Tolerancia sólo de representación, nunca en reglas de entrada.|
|VWAP|Media ponderada manual con pocos valores; escala uniforme de V conserva resultado dentro de representación; V enorme finito no overflow por normalización. Sin sigma ni rolling24h accidental.|
|Patrón|Bordes exteriores inclusivos, recuperación/centro estrictos, reflexión long/short y ausencia de señal cuando dirección no coincide.|
|Consumo|Primer patrón bruto consume ANTES de target_guard/sizing/ocupación/same-exit. Cada motivo de rechazo mantiene consumed. No esperar otro horario ni cambiar lado. Raw coincide entre modos.|
|Objetivos|Mismo E/d/ambos objetivos en guard compartido. VALUE no se mueve al agregar volumen; R2 usa distancia2d desde fill. Tipo de orden sólo lo prueba auditoría nativa posterior.|
|Near y fees|Usar is_price_near exacto con .00015, sin epsilon inventado. Target igual/atravesado/near rechaza ambos. Target no-near pero bruto<=fees también rechaza. Beneficio justo igual a fees rechaza; estrictamente mayor admite si todo lo demás pasa.|
|Fill adverso|Con fill que atraviese G o vulnere guard, registrar after_fill_invalid, mantener protección y solicitar cierre MARKET; trade nunca omitido, sin fallback a R2. Verificar que ningún assert heredado impida esa salida segura.|
|Riesgo|Helper legacy real con .5/.5, reserva.001/lote.001; igualdad de qty cuando el estado de cuenta es idéntico. No multiplicar por leverage ni cambiar presupuesto al cambiar TP.|
|Plazo|Entrada08 cierra a00 tras16h; entrada20 tras4h. Deadline evaluado cadaM1 aunque falte ancla/ATR/volumen o el horario no admita entradas. FINISH y safety tienen motivos explícitos.|
|Observador|R11 pre/open/close una vez por fase; ledger antes de FINAL; snapshots no sumados. Datos inválidos de señal no desactivan SL/TP/deadline.|
|Logs|Schema R34_PLAN/OPEN/CLOSE/SUMMARY legible; targets reales, raw/guard/selected diferenciados, cada línea<1800. No tp_r=None que oculte TP, no listas M1 acumuladas.|

## Detalle de near/fees
La comparación exacta del helper nativo debe fijarse por fuente antes del harness. No basta una aproximación algebraicamente parecida en el borde flotante. Fixtures: target idéntico, interior al umbral, borde y exterior, reflejados. Con E=100.02 y target100 short, la distancia puede superar1.5bps pero no las fees base: ambos rechazan. Con objetivos claramente separados (por ejemplo E97 y G100) y d4, ambos pasan esta parte.

La guard compartida exige beneficio bruto mayor que fee*(E+target), no beneficio realizado garantizado. En los bordes de costo usar la desigualdad estricta prescrita y representación conocida; no añadir tolerancia a la señal. Funding se mantiene en economía real.

## Forma y límites del futuro check
Siete/ocho fuentes finales completas según ABI acordada, hashes exactos, AST con imports reales retirados, stubs de estado/órdenes e indicadores sólo si necesarios; arrays fabricados. Versiones Python/NumPy/Pandas explícitas. No importar proyecto real, velas observadas, red, DB, engine o backtest anidado. Salida JSON acotada <48k. La cantidad de asserts no equivale a evidencia independiente.

No está autorizado ejecutar este plan todavía. Root revisará protocolo, CODES y ABI, dará GO de implementación y luego asignará el slot de un check. Congelar/readback de código ejecutable final antes de ese job; preservar fallos técnicos sin retocar alpha por resultados.
