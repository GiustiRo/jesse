# Curva de equity recuperada y verificación de equivalencia

Dashboard: http://localhost:9200/#/backtest/eef79402-f4cc-4b9c-8305-9ab870d639e5

El usuario autorizó una excepción acotada a bot/AGENTS.md para corregir persistencia de equity del backtest normal y añadir regresión. Cambio en _execute_backtest: generate_equity_curve=True al llamar al simulador y equity_curve=result.get('equity_curve') al guardar. No se cambió el cálculo de equity, las estrategias, el simulador compartido, Monte Carlo ni live. Sin reinicio: los workers usan spawn y cargan el código al iniciar.

Verificación real contra http://localhost:9200/#/backtest/786c23cb-6785-449a-a191-193804ee0c0f : diccionarios completos de métricas iguales y campos económicos de los 45 trades (símbolo, dirección, entrada, salida, qty, timestamps, PNL y fee) idénticos. Ahora se conservan 2147 puntos Portfolio.

Pruebas en Python 3.11.17 del entorno Docker Jesse existente: 23 passed en test_import_and_backtest_request_boundaries.py; 40 passed adicionales en test_mcp_session_results.py, test_backtest_session_chart_images.py y test_backtest_session_chart_data.py. Sin instalar paquetes. git diff --check limpio.

Auditor v2 sobre curva MTM diaria: 71 meses, 40 activos (posición abierta durante alguna parte del mes), 31 sin posiciones; 29.577% de meses positivos totales; 52.5% de meses activos positivos; 54.167% de trimestres positivos. Peor mes agosto 2021 -7.53%; racha máxima no positiva 9 meses. CAGR publicado 35.1048%, DD diario publicado -12.4126%. Incluye períodos limítrofes parciales. Las curvas son muestras diarias, no la peor pérdida intradía; no confundir drawdown diario con máximo de minuto a minuto. Atribución/correlación por ruta del auditor aún usa cierres realizados, no MTM por instrumento.

Concentración: dos mejores trades nominales = 46.806% del PNL neto del control al 3%. La eliminación nominal es un diagnóstico contable, no un nuevo backtest redimensionado.

2026 no utilizado. Los backtests previos no se rellenan retroactivamente: requieren repetición para almacenar la curva. Pendiente diagnosticar diferencias de horario de muestreo fast/normal; el cambio de persistencia no intenta corregirlas.