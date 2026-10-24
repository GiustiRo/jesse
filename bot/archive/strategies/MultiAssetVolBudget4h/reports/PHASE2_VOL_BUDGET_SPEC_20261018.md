# Variante de presupuesto por volatilidad (especificación, aún sin backtest)

Hipótesis predefinida: reservar nocional para todos los instrumentos según inversa de ATR/precio evita que la ruta evaluada primero consuma todo el margen compartido. Cada instrumento recibe parte de 4.4x nocional máximo de cuenta, con objetivo máximo 3% por trade, presupuesto global 8% y fees/reserva de sizing. Mantiene idénticas entradas/salidas al prototipo MultiAssetBreakout4h.

El reparto se calcula con barras cerradas. Mantiene capital reservado incluso con señales inactivas; puede sacrificar retorno por menor uso del margen. No promete contribuciones iguales de riesgo realizadas: fees, stops, gaps y caps lo impiden. Hay que contrastar ambas ordenaciones de rutas y comparar cartera conjunta con fechas iguales.

Solo BTC/PAXG en esta versión. SPY deshabilitado hasta validar el proxy, calendario y construcción de barras. Aún no ejecutada, sin resultados ni validación. 2026 no utilizado. Ninguna sesión live/paper autorizada o iniciada.

Observación para validación posterior: moving_block_bootstrap crea RNG por pipeline; con seed=None las rutas se remuestrean de forma independiente, y con calendarios distintos la misma semilla tampoco garantiza alineación temporal. Un MC que borre dependencia entre activos no demuestra robustez de diversificación; documentar esa limitación o usar remuestreo conjunto por calendario en una etapa separada.
