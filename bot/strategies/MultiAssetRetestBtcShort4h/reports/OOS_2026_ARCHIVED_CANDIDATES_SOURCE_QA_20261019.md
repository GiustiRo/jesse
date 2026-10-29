# QA de fuentes antes de comparar resultados2026

Cuatro copias nuevasN503/P604/C504/K1005 fueron releídas y almacenadas EXACTAMENTE como se crearon. Al revertir únicamente nombredeclass, TRADE_RISK.02→.01, PORTFOLIO_RISK.06→.08 y comentarios de normalización/cap, se recuperan byte a byte los snapshots de desarrollo indicados en el protocolo. Originales intactos. No cambiaron filtros, señales, stops, objetivos, calendarios ni prioridades.

N204 reutiliza CapitalR12N204R2A6 ya congelada enR12: frente al snapshot X03ExploreR204 de bc5aaba6-2746-4e90-b0de-7b7955b66142 sólo difieren nombreclass, constantesriesgo y elcomentario cabeceraR12. Tras revertir esos campos, elcódigo ejecutable coincide; elcomparadorliteral inicial fuefalseporuncomentario, y la inspección de diferencias confirmóque ésa era la única diferencia adicional.

Las fuentes auxiliares dePAXG/SPY son las mismas delperfilK1001. Cada ejecución terminada se verifica contra su formularioexactoesperado y los3snapshots de fuentes. La semántica del sizing uniforme2%/6% a3x se declaraantes de resultados nuevos; no se presentó como fuenteoriginal1%/8% sin cambios.
