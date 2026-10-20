# Protocolo previo: fallo de rango lateral

Hipótesis: baja eficiencia direccional permite que una incursión fallida fuera del rango20 anterior vuelva hacia su midpoint. No es una mejora demostrada. Primera prueba única, sin optimización.

BTC/PAXG/SPY 4h;2020-10-15→2025-12-31 exclusivo;normal,warmup240;10000 compartidos;5xaislado;fee0.00045 porlado todasórdenes. Riesgo1% poroperación,tope8%,nocional4.4x y techoigual1/3ruta. SPY mismoshorariosreferenciaUTC00–20/decisión00–16,datosfiltrados,exits sinrestricción;proxyCFD/BIDsinvolumen,feriados/paridadpendientes. PAXGproxySpot.2026reservado.

Reglas simétricas: ER20<=0.25; vela cerrada perfora extremo del rango20 previo y vuelve dentro, aún antes del midpoint. MARKET al cierre observado. Stop extremo vela±0.25ATR; distancia1–3ATR. Target midpoint congelado, premio>=1R y>=8*feeBASE*precio. Criterio fee fijo incluso al estresar costes. Caducidad48h, unaentrada/unasalida completas.

Justificación: rango20 define contexto multidiario; ER0.25 evita deriva dominante; stopmínimo1ATR reduce ruido y máximo3ATR evita perseguir extremos;1R excluye reversión ya consumada;8feesbase exige espacio para4roundtrips;48h distingue reversión breve de tendencia. No son óptimos calibrados.

Descarte: netono positivo,DD>25%; menos30trades es inconcluso. Revisar concentración1–2trades,componentes ycostes. Si promete,auditorMTMv3ROOT para meses/trimestres y complementariedad; luego vecindario yperíodos. Criteriosfinalescartera65–70%mesesactivos/80%trimestres se mantienen. No filtrar fechas retrospectivas,noabrir2026,noMCindependientecomo certificado. Máximo2prototipos primera ronda; este es el primero.