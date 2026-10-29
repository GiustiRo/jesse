# Próximo bloque: funding BTC en Jesse — propuesta sin implementar
Fecha2026-10-20, después del cierre R14. Usuario pidió separar funding y planificar antes de avanzar. Sin descargas, importaciones, cambios de framework, pruebas nuevas ni live en este documento.

## Orden y alcance
Dos objetivos separados: contabilizar pagos/cobros históricos correctamente y, sólo después, evaluar si funding agrega información predictiva a BTC. Mantener C principal/Bcontrol,10k,2%/6%,3x y PAXG/SPY congelados. No portar automáticamente el LightGBM anterior ni añadir OI junto con funding.

## 1. Auditar soporte real y cerrar contrato técnico
Inspeccionar motor/persistencia/proveedor/MCP actuales antes de identificar archivos y migraciones exactos; reutilizar soporte existente si satisface invariantes. Las pruebas R14 no validaron un ledger de funding.
Alertas del bot anterior: descargador conserva tasa deAPI, motor divide por100, y cobro se agenda por barras desde entrada. Auditar unidad y reloj antes de portar, sin atribuir automáticamente todo el gap histórico a estos puntos.
Los dos meses reales neutrales son experiencia reportada por el usuario, sin backup identificado; los reportesdemo no sustituyen esa evidencia.

## 2. Datos históricos y contabilidad
Evento mínimo: exchange,symbol,settled_atUTCms,rate_decimal; mark_price de liquidación si existe, fuente y versión. Señales requieren known_at/publication_at; tasa liquidada y estimada son datos distintos.
Una unidad interna: fracción decimal.0.0001=0.01%; nominal10k genera1USDT por liquidación, no0.01USDT. No conversión doble.
Importación idempotente por exchange/symbol/instante; conflictos se reportan. Validar orden,UTC,duplicados,NaN,signo y frecuencia real; no asumir8h si el venue la cambió.
Cashflow=q_signed*mark_price*rate_decimal; longpositivo,shortnegativo; cash-=cashflow. Usar cantidad vigente tras parciales y marca documentada, sin sustituir por entrada silenciosamente.
Aplicar en reloj de settlement del exchange, no cadaNvelas desdeentrada. Documentar precedencia de entrada/salida coincidentes al settlement después de revisar semántica real del motor/proveedor; probar antes/en/después.
Con contabilidad activada, missingevent/mark requerido durante exposición debe bloquear o declarar incompleto; nunca convertir ausencia en coste0. Mantener modo disabled por defecto y no alterarconfigglobal.

## 3. Interfaz, ledger y paridad
Opción por sesión propuesta funding_mode='disabled'|'historical' y datasetversionado, inicialmente BTC BinancePerpetual. El esquema/nombre definitivo se decide tras inspección de soporte para respetar API existente.
Persistir eventos y aporte funding separado de fees; exponer en resultadosMCP y snapshotsrun_analysis. Reconciliar precioPNL-fees-funding=neto y cash/equity en cada settlement. paidpositivo=pago; negativo=cobro.
En runtime reconciliar liquidaciones reales ya incorporadas al wallet: no volver a descontarlas. No pedirclaveslive ni activarcuentas para backtesting.
Disabled debe reproducir anclas en señales,fills,cantidades,fees y equity. Historical puede cambiar sizing por capital: distinguir ledger sobrefillsfijos y replay completo endógeno.

## 4. Pruebas y primer replay contable
Casos: long/short × fundingpositivo/negativo/cero; ejemplo1USDT; UTC y límites de settlement; variospagos; parciales; cierrefinal; duplicados/conflictos; faltantes; frecuencia variable; nodoblecontabilizaciónruntime.
Pruebas causales: señal enT invariante al truncar datos posteriores aT; incluirderivadas/agregadosdiarios. Validar paid vs predicted y known_at.
Tras pasar, congelar versión y ejecutar K1001con/sincostefunding en2020–2025; desglose porlado,mes,año,duración ystress.2026observado es desarrollo, no prueba ciega. La contabilidadcorrecta no necesita mejorar rentabilidad para ser aceptada.

## 5. Señal como investigación posterior
Comparar precio original contra el mismo mecanismo con una sola condiciónfunding. Empezar por tasa liquidada conocida y desviación respecto al pasado, sin copiar12features ni ML.
El signo de la hipótesis y corte grueso se preregistran después del diagnóstico causal2020–2025 y antes de corridascomparativas; no elegirlos para arreglar2026. No contar transformacionesdelmismafuente como evidenciaindependiente.
Si sobrevive costes, años y sensibilidad, congelar y obtener evidencia futura. Reordenar2020–2026 no recupera independencia.

## Entrega previa a implementación
Auditoría de capacidades y datos, contrato técnico con archivos/rutas/migraciones identificados, decisiones de cronología y criterios de aceptación. Después, implementación y pruebasdelmotor; despuésreplaycontable; porúltimoprotocolopredictivo. Se revisa este alcance antes de empezar el bloque. No live/paper ni modificación del bot anterior.
