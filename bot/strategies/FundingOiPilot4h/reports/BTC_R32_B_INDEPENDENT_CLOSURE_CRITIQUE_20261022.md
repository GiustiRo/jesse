# R32 B — revisión interpretativa independiente del cierre

Fecha local: 2026-10-22. Dictamen: CONFORME para cerrar ambas políticas como NO_CUMPLE, sin candidata ni vecinos dentro de esta comparación.

## Alcance

Leí BTC_R32_B_FINAL_20261022.md completo y BTC_R32_B_RESULTS_20261022.json completo en dos páginas (2306 líneas, sin faltante final). Revisé sus resultados, R11/ledger resumidos, gates, límites, manifiesto de auditoría y correcciones técnicas. No volví a auditar355 trades/órdenes,1509 pagos, el join de212 patrones ni los11.120 logs; esas verificaciones por fila pertenecen a los recibos de root. No nuevos jobs, precios, código o motores.

## Interpretación

[ALL](http://localhost:9200/#/backtest/67655c18-3682-4397-b119-52fd1ea8edba) pierde768.5124USDT, CAGR−1.52125% y PF.90739; [PERSIST](http://localhost:9200/#/backtest/9228f0b1-5c61-43ed-9edf-ef1b7556b5f5) pierde863.8837USDT, CAGR−1.71711% y PF.87013. Sobre cuenta total10000/cuota1% fija, el filtro no produce la mejora económica buscada bajo estas reglas. No sumar cuentas, duplicar resultados a2% o cambiar denominador a5000.

El menor DD17.5251→14.4991% es favorable, pero no basta. M+ activos42.37→44.64% mantiene exactamente25 meses positivos y reduce denominador59→56: no agrega un mes calendario ganador; ambos25/62 completos. Q8→9 sí agrega un trimestre positivo bajo sus trayectorias completas. La mediana mejora−.3384→−.0089%, pero sigue negativa, no cero ni positiva. Es un intercambio de métricas, no dominancia ni ganador. Ambas sólo pasan DD/N; N195/160 satisface suficiencia operativa mínima, sin dar confianza estadística.

El bruto de precio ya es negativo en ambas (−300.5871/−489.9542). Comisiones528.4798/433.6587 agravan; funding+60.5544/+59.7293 amortigua. No atribuir fracaso exclusivamente a costos ni interpretar ahorro de fees como señal mejor. PF monetario inferior a1 es coherente con neto negativo; su ponderación por cantidades/capitalización no es un estimador puro de calidad del patrón.

## Universo, atribución y límites

El cierre acredita212 fallos brutos idénticos,168 interiores y44 recuperaciones originales; la implementación registra esos patrones antes de ocupación/sizing. Eso permite saber qué filtro se aplicó, pero no identifica el PnL contrafactual de cada exclusión.195→160 son35 fills menos, no44 trades quitados: ocupación17→8 y capital evolucionan de otra manera. No reconstruir otra cuenta restando filas ni deducir que operar a favor de las44 recuperaciones sería rentable.

Cero resoluciones opuestas/frontera es el resultado de este universo, no una prueba nativa de esas ramas ni motivo para forzar otro motor. Sus definiciones conservan cobertura sintética previa; su ausencia histórica no permite simplificar retrospectivamente la receta o extender la conclusión a esos casos.

La corrección de total_open_trades es semántica de un contador nativo asociado al cierre forzado, no cambio de estrategia ni un error económico reparado con rerun. Sólo datos postcierre/órdenes/ledger y fasePRE/FINAL permiten acreditar flat final; no inferirlo del nombre del contador. En RESULTS B ambos resúmenes propios muestran closes=opens y PRETERMINAL; eso concuerda con la presentación, sin inventar un callbackFINAL adicional ni descartar una liquidación forzada si existiese en otro caso.

No encontré sobreclaim material en FINAL. La conclusión está limitada a permanencia UNA barra adicional después de este fallo de ruptura, al mismo cierre tardío y con gestión común. No demuestra que toda reversión falle, ni que otra espera, lado o salida sea mejor. Historial observado/adaptativo, sin OOS nuevo, DD M1+fills sin todos los extremos intraminuto. Cerrar sin retocar26barras, confirmación, targets o cuotas es coherente con el presupuesto.
