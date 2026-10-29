# V4 — SHOCK smoke técnico

[Sesión](http://localhost:9200/#/backtest/23cdce16-42b9-4a76-96e5-02fbf06106df), terminada sin error, [2020-09-01,2020-09-08),1h;config nominal exacta10000/isolated3x/cap1x/fee.00045/slip0/warmup240/fundingON.

48checks puros SHOCK y61comunes pasaron dentro del motor.168decisiones,5entradas,5trades:4cierres antes del audit y1short forzado posterior. Cuatro longs y un short. Causas reales:1stop-loss,3take-profit,1fold_end. Callback real de cierre de dos argumentos ejercido cinco veces. Particiones de primary/features/dirección, cuotaUTC,ventanasATRoffset1 previas al shock,niveles1A desdefill,riskstop+fees,cap1x ylíneas<=1900 pasan.

No ejercidos por este smoke: maximum_hold6h,calendar_boundary,ni fundingcashflow nozero. Se procesaron21settlements ycashflow0 porque las posiciones no coincidieron con ellos. El funding histórico sí figura applied. total_open_trades1/open_pl9.638653 es metadata precierre forzado; los cinco close logs yel saldo final10270.271259 incluyen cierre final, no una posición residual comprobada.

Root actualizó sólo common_checks a61 antes del arranque (jobdf6eec8e69f141c4b2be765fb954befa); fuente económica congelada sin cambios. Se corrigió descriptor del draft de56a61checks mediante notas, sin tocar estrategia/config ni iniciar otra sesión. Respuesta de inicio started, sin retry ni timeout en este smoke.

Evidencia completa: AUDIT_ResearchV4ShockSmoke1h.json y V4_SHOCK_PROGRESS.json. Esta prueba acredita importación,API,motor,features,protecciones ycallbacks ejercidos; no acredita rentabilidad ni valida mecanismos económicos. Sin SCREEN/jobs adicionales. Token liberado; espera GO central.
