# V6 EFFICIENCY — smoke técnico aprobado

[Sesión EFFICIENCY 4h](http://localhost:9200/#/backtest/4eafad70-21a5-41c0-a300-95eb22f39981), del 1 al 8 de septiembre de 2020. Root creó e inició una única sesión; terminó sin error. Este sector sólo leyó y auditó resultados, sin nuevos drafts, jobs o motores.

La configuración coincide exactamente con el registro V6: BTC-USDT en 4h, capital de 10.000 USDT, warmup de 240 velas, margen isolated3x, fee 0,00045, slippage cero, funding histórico activo y datasets congelados. Fast solicitado es true, pero efectivo false por funding.

## Cobertura observada

Los logs completos contienen 38 líneas y ninguna supera 1.080 caracteres. En runtime pasaron 112 checks del sector y 67 comunes; root había informado 338 checks globales sobre 14 fuentes. Esta auditoría añadió 57 aserciones estructurales correctas.

Las 42 decisiones generaron dos operaciones cerradas, una long y una short. Ambos cruces registran una ventana de entrada de 26 cierres y ventanas independientes Eactual/Eprev de 25. Timestamps, desigualdades frescas con umbral 0,35 y álgebra normalizada son coherentes.

Ambos planes usan ATR actual de 14 TR/15 OHLC, distancia congelada de 2,5ATR y stop anclado al fill. Cumplen riesgo previsto del 2% incluyendo fees, cap nocional de una vez el capital y floor de ocho decimales. Las entradas ocurrieron en días UTC distintos. El control P entró con OI inicializado parcialmente o no creciente, tal como corresponde a la ablación sin filtro OI.

El long cerró mediante un STOP ejecutado. El short cerró MARKET por efficiency_neutral: Eactual=0,1087909774, posterior al fill, con 25 cierres válidos. Ese cierre fue a las 00:00 del 8 de septiembre usando la última vela cerrada del día anterior. Fue una salida indicadora, sin vela futura ni cierre forzado fold_end.

El motor etiqueta esa liquidación MARKET como submitted_via=take-profit. No es un objetivo LIMIT: target_mode es none, los targets registrados son null y no hubo órdenes LIMIT ejecutadas.

Los contadores concilian 42 barras, dos entradas y dos cierres. Las causas primarias son 38 no_cross, dos allowed, una in_position_or_pending y una boundary_or_inactive. Las features tienen 39 no_cross y tres setups; el tercer setup estaba bloqueado por posición. Las particiones por dirección también concilian.

Funding procesó 21 settlements y produjo 15 cashflows, con saldo agregado no nulo y marcas proxy. La reconstrucción financiera completa de órdenes, ledger y equity pertenece a la auditoría central de root.

## Límites

Las operaciones no ejercieron máximo de 60 barras, calendario, invalid_after_fill o cierre final forzado. La procedencia confirma hold60×4h; los checks deterministas no acreditan fills reales de esas ramas. Se ejecutó un STOP; del otro se conservan el plan, log y código congelado, sin otro fill STOP. Los hashes de las ventanas están registrados; este examen de logs no reconstruye sus OHLC originales.

El smoke valida implementación y trazabilidad, no rentabilidad ni parámetros. Queda pendiente GO global para los screenings nominales. No se consultó economía V6 de 2024–2025 ni 2026.

AUDIT_ResearchV6EfficiencySmoke4h.json conserva summary, logs completos, trades con órdenes, aserciones, contadores y límites. V6_EFFICIENCY_PROGRESS.json integra el estado y las fuentes.
