# V4 Funding Reset: smoke técnico

[Sesión terminada](http://localhost:9200/#/backtest/72cdd654-a757-488b-9df7-6351496574ba), [2020-09-01,2020-09-08),1h, configuración nominal exacta y funding aplicado. Error null. Checks52helper+61comunes passed.

77líneas completas, máximo817caracteres.21eventos únicos (1inicialización y20rechazos funding_no_reset),42bloques canónicos16+16. SHA256recalculado21/21 idéntico. EVENT.settled_at proviene del accesor público y coincide exactamente con el último rawsettled_at de history, también con jitter. Todas las disponibilidades <=decisión; ningún funding_accessor_mismatch.168decisiones:1inicialización+147repetidas+20no_reset.20rechazos consumidos sin reintento.

Cero trades; no acredita cobertura real de entry/stop/holding/salida SMA24 ni cashflows por posiciones. Esas ramas tienen checks deterministas y deberán auditarse cuando existan fills. Saldo10000, fundingcashflow0 y21settlements procesados. Ausencia de métricas/equity normales con cero trades se conserva como tal.

Evidencia: AUDIT_ResearchV4FundingSmoke1h.json y V4_FUNDING_PROGRESS.json guardados en el proyecto Jesse. No se usó economía de smoke para cambiar parámetros. SCREEN requiere GO explícito root.