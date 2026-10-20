# SPY20 — aclaraciones congeladas antes de código y resultados

Root revisó y aceptó las diez exploraciones de SPY20_MATRIX_PROTOCOL_20261018.md, conservando los parentescos y sin alegar diez mecanismos independientes.

1. 04/10 probablemente tienen muy pocos episodios porque la muestra empieza en octubre de2020 y el trigger exige pérdida10% en<=5sesiones. 05 también puede ser escaso. No mover umbrales para obtenerN; una muestra insuficiente queda inconclusa, incluso si gana.
2. 01/02/03 y cada uno de los5intervalos de07 requieren cierre del día hábil CIVIL anterior: lunes←viernes, resto←fecha−1día. Si falta porfestivo/cierretemprano/gap, no se observa esa feature. No implica calendarioNYSE completo.
3. DailyATR es media de14true ranges sobre sesiones completas observadas y puede abarcar huecos; no se imputan candles. Se informarán duraciones reales. Horizontes72/120/240h son HORAS desde fill, no número de sesiones; salidas adeudadas requierenquotepropiafresca.
4. 08/09: se necesitan64quotesPAXG sincronizadas con sesionesSPY completas. Numerador esquoteactual−quote3intervalosantes. Normalizador: std(ddof=0) de60cambios entre61quotes que TERMINAN3intervalosantes; se excluyen los3intervalos del evento. Se fija por origen del evento, no convolatilidadposterior. Unidades de precioPAXG, no correlación estimada. Si faltaquotePAXG enesa ventana no hayfeature; historialPAXG24/7no se filtra porRTH.
5. 04/10 stop estructural nunca queda más cerca de2ATR desde fill efectivo; no se relaja trasabrir. ATR/evento ya conocidos alentrar. Crash usa el máximo de cierres de las20sesiones anteriores; empate por la observación MÁS RECIENTE. Rearme sólo al recuperar máximo congelado.
6. Límite dearchivo de historia150sesiones observadas es retención técnica: excede mayorlookback64; los estados deepisodio guardan susanclas aunque envejezcan. Arranque cash visible. No cambia reglas dealpha.
7. Código común se copia íntegro en cada estrategia con señal propia, evitando dependencia deimportsentreestrategias. Root revisa motor+señales antes deprimeros2fulls; luego cola10 con2slotspropios sin pedirpermiso por cadauno.
