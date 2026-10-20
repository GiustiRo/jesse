# ATTRIBUTION SPY — adenda definitiva previa a código

Esta adenda reemplaza ambigüedades de la propuesta y prevalece sobre ella. Total17 fulls SPY, 34 conjuntos. Añadir Cq AttrSpyCqFreshLimit: entrada LIMIT y gestión original, pero guard de frescura sólo en entry, sin filtrar trailing. C0/E1..E4 no reciben ese guard; E4 sí debe liquidar vencimiento a quote fresh. C0 se ejecuta y valida paridad antes de cualquier otra corrida.

Freshhelper: M1 T−60000 exacto mediante searchsorted, precio finito>0 y paridad con self.price rel1e−10/abs1e−8. Insuficiente o desalineado devuelve False; sin assert ni cotización ficticia. Cq/M/R/U comparten mismo fresh entry. No modificar trailing ni historial/calentamiento/calendario por frescura.

C0→Cq distingue filtro de frescura. Cq→M contrasta tipo/precio y selección de fills, con ocupación endógena. MARKET recalcula tamaño al close bajo mismo riesgo. R conserva EMA/ADX/RSI/rango y quita ambos predicados Donchian; U quita todo régimen incluido rango, conservando history100/ATR/calendario/límites.

Hash definitivo exacto: ASCII 'ATTR1|{symbol}|{seed}|{closed_candle_open_time}', SHA256 primeros8bytes bigendian %48==0. Misma fuente por semilla y barra enR/U; sin nombre de clase/modo/run. Seeds101,202,303,404,505. Reloj calculado en before incluso ocupado, no cola ni replay. Mod48 tiene sesgo discreto despreciable, se describe pseudoaleatorio determinista aproximado1/48; no IID inferencial.

E4 deadline desde position.opened_at efectivo,72h; primer tick4h posterior y deuda hasta freshquote, sin filtrar exits por horario. C0 copia exacta salvo clase; revisión root de motor/diffs antes de su ejecución. No RTH: conservar UTC original. Todas las otras restricciones y criterios de análisis de la propuesta permanecen.