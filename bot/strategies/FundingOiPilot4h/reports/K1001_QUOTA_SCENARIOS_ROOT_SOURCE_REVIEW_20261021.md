# K1001 cuota: revisión de fuentes por root antes de checks

Estado: CONFORME de lectura, pendiente de ejecución sintética y manifiestos. No acredita rentabilidad ni cobertura del broker real. Fecha documental2026-10-21.

Root leyó las tres fuentes actuales completas por read_strategy. Releyó por MCP los cuatro padres y corroboró igualdad literal contra snapshots previos de R16Base, R11 y R10; wrapper K1001 sigue MODE K1001. No override de before ni recomputación del suplemento. _prepare_entry preserva guardas y memo; único cambio económico es allowlist long o core→supp y los argumentos de capital/margen multiplicados por.5. No cambios de stops, targets, indicadores, plazos, fees, funding o reserva.

El observador llama parent una vez, devuelve su equity y usa namespace propio. Open0, pre estrictamente posterior al fill, precios de cierre M1, salida real antes de parentclose/FINAL. Empates conservan primera marca. No utiliza extremos intraminuto o precios futuros. Se preserva el defecto de la primera versión y su corrección: contar fills reales antes de validar trace y last_fill_identity para evitar dobles conteos. Un error diagnóstico queda visible, no borra la operación económica.

La lectura no detecta otro bloqueo material. Se requiere check suministrado por independiente sobre la versión final5f41d87a de base y wrappers703a63b9/23b553cd, hashes completos en IMPLEMENTED_SOURCES. Revisar checks/resultados antes de drafts; luego clonar el formulario genuino de K, funding históricoON, aislado3x,10000 totales, ventana fija2020–2025 y presupuesto2motores. No sumas de curvas ni evidencia conjunta. Medidor ocupación HOLD.
