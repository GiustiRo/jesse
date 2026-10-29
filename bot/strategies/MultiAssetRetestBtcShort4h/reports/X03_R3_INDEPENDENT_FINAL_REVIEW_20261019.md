# X03 R3 — revisión independiente final del informe principal

Se leyó completo X03_R3_RESULTS_20261019.md y se contrastó con el protocolo, revisión de fuente/QA/paridad, diagnóstico mensual final, auditorías FIXED_STRESS_B/C, ejecución/divergencias fixedBE y X03_R3_ATTRIBUTION_RESULTS_20261019.md. Sólo lectura y revisión de informes; ningún nuevo job o backtest.

No se encontraron errores materiales ni objeciones a la conclusión.

- La preselección de N204 es de investigación: Δ N204−X03 positivo en B/C bajo ambas políticas PAXG al fee alto, DD dentro del límite y QA/paridad correctas. PAXG original permanece oficial, X03 control, sin promoción ni apertura de 2026.
- El fallo mensual se conserva: original39/61 y39/63; fijo40/61 pasa65% sólo en completos y40/63 falla con fronteras. El informe no elige el denominador favorable.
- Las diferencias e interacción concilian con los artefactos: original +923.163802/+988.068271; fijo +955.663691/+1062.542234; diferencia de diferencias +32.499889/+74.473963 USDT. Se interpretan como efecto total condicionado del simulador, con capital/ocupación como mediadores.
- La primera salida diferente observada se sitúa correctamente en enero de2021. Enero de2025 es un efecto económico grande, no la primera divergencia. La primera instrucción STOP diferente sigue desconocida.
- El diagnóstico distingue bruto fijo, neto tras fee propio y overlay adicional. N204 fee alto:43 meses brutos positivos/20 negativos;4 positivos absorbidos por fee propio;39 netos positivos. Otros+5bpsRT producen2flips B/1C y llevan el coste total a19bpsRT. Se reconoce que los20 negativos brutos conservan decisiones dependientes de fees.
- La atribución contiene los17retirados/17añadidos por contraste, incluidos ganadores y perdedores; añadidos netamente negativos y efecto unitario retenido aproximadamente cero. Las cifras de sustitución y cantidad concilian con el informe de atribución. No se llama causal alpha ni compounding puro al término cantidad.
- La documentación de normalización de metadatos y partición de outputs conserva la hipótesis y los resultados originales; no oculta fallos ni utiliza tablas truncadas para conclusiones. El informe distingue gráficos generados de preview no verificada.
- Las8runs nuevas,4controles nulos,8referencias y B/C no se presentan como réplicas independientes. Se explicitan selección histórica y reutilización2020–2025.

No se requieren cambios materiales al borrador revisado. Cualquier examen reservado necesita otro protocolo y autorización humana; esta ronda no crea drafts ni inspecciona2026.
