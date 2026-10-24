# K1001 — decisión sobre valor de información del próximo experimento

Fecha local: 2026-10-21. Decisión anterior a implementar o ejecutar cualquier estrategia nueva de esta fase.

El diagnóstico de registros existentes está completo, revisado y publicado en Hub r26. Respondió quién aportó, cómo se distribuyeron los resultados, qué cambió en2024–2025 y qué datos faltan. No acredita cuentas independientes ni objetivo alcanzado.

Se diseñó y revisó un replay instrumental de la K original para contar candidatos bloqueados y observar extremos M1. Es viable, pero se deja en HOLD sin crear fuentes, drafts, checks o motores: el conteo no indica fills ni rentabilidad y no se había fijado un resultado que cambiase la decisión de estudiar separación. Ejecutarlo ahora añade una capa de infraestructura sin resolver la pregunta económica principal. Propuesta/anexo/review se conservan íntegros; no se presenta como prueba fallida.

Próxima pregunta preferida: ¿qué resultados producen las recetas originales cuando operan sin competencia del grupo contrario, bajo la cuota de riesgo acordada? Dos escenarios contrafactuales nativos propuestos: LONG_ONLY y SHORT_BOOK, este último conserva CORE_SHORT→SUPPLEMENT y su latch original. No se modifican umbrales, entradas, stops, targets o gestión para mejorar un resultado.

Cada escenario representa UN libro BTC de10.000USDT iniciales donde sólo ese grupo está activo y usa1%de la equity total de SU trayectoria; la otra cuota está inactiva y no se presta. Se usa legacy_plan(event,.5*balance,.5*available_margin,3,fee), sin cambiar el helper original: el budget de sizing es .02×.5balance=1%delcapitaltotal, y el margen máximo es .90×.5=.45 del observado. No es1%deuna subcuenta5k ni dos grupos al2%cadauno. La otra mitad del presupuesto permanece reservada.

Son mundos alternativos individuales, no dos cuentas financiadas simultáneamente con el mismo dinero. No se sumarán curvas, CAGRs, balances ni se afirmará que ambos han usado el equity conjunto dinámico. La evaluación conjunta con riesgo BTC total2%requiere después una implementación propia que aún no se acredita. Ambos escenarios podrán responder por separado sobre selección, fills, costos y payoff, con instrumentación mínima dentro de esas pruebas, sin un replay antiguo adicional sólo para contar.

La referenciaP2%se reutiliza como antecedente. Como también cambia la cuota, una diferencia económica no se atribuirá exclusivamente a eliminar competencia. Se comparará la política nueva especificada y se informarán cambios de selección y R sin vender una ablation causal pura. Esta dirección responde al pedido humano de estudiar segmentación con riesgo compartido; no es retirar el lado perdedor retrospectivamente, dado que ambas ramas observadas eran positivas y se conservarán ambos resultados.

Presupuesto propuesto: dos nuevas ejecuciones económicas, protocolo y fuentes/checks/manifiestos antes de motor. No ejecutadas por esta decisión. BTCUSDT, misma historia2020–2025, taker.00045, fundinghistóricoaplicado/proxies,3xaislado,6%global,slippage0. Sin nuevos2026,USDC,estrés, imports, framework/configglobal/live/paper/Pi. Bloque creativo continúa y no condiciona reglas a futuros resultados.

Tareas: reversion_history prepara protocolo+anexo de fuentes y control de repetición; geometry espera aprobación de root antes de implementar; root revisa contrato y mantiene contabilidad. La pregunta y el denominador se fijan ANTES de resultados, no después.
