# Verificación y ampliación documental — 20261021-r2

La revisión r1 conserva la integración inicial. r2 amplía la transcripción de evidencia ya almacenada, sin nuevos backtests: V1/V2 selector convencional sin exposición, seis screenings V4, nominales y años/semestres/costos/exposición V3/V5/V6 y escenarios V3/V6. Fuentes originales referenciadas en cada ficha. Los ceros de V1/V2 describen índice convencional; no se fabrica un replay V4.

Validaciones ejecutadas:
- 87 tests existentes de project-files en el contenedor local, Python3.11.17: PASS; dos warnings preexistentes de dependencias.
- Tres grupos Node de pruebas: paginación, ausencia/truncado/cambio de evidencia, confinamiento de paths, protocolo numérico y cronología, índices y filtros.
- Navegador Chrome instalado, Playwright instalado: ruta directa autenticada, navegación, filtros, fichas, reportes, tema claro/oscuro y viewport móvil390px.
- Respuestas sintéticas sólo en tests para401, documento ausente, fallo de conexión, revisión vieja, contenido malicioso y campos faltantes. No se guardan como evidencia económica.
- Revisión visual escritorio/móvil; contenido de registros se inserta con textContent y no ejecuta HTML.
- Panel llama únicamente POST /project-files/read. No escrituras/ejecuciones/importaciones/trading desde el panel. El shell conserva sus propias lecturas de sesiones.
- Sin cambios de estrategia o bundles Nuxt, sin API/tablas/dependencias nuevas, sin instalaciones ni reinicios.
- Publicación MCP: archivos antes del índice; originales preservados.

Límites: la validación del formato no certifica veracidad de un prerregistro. El inventario multi-activo es inicial y contiene continuaciones aún por examinar antes de definir nuevas referencias. No se ejecutó la suite completa del framework ni un backtest nuevo. Los tests económicos anteriores no son evaluación prospectiva de este programa.
