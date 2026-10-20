# R14 — BTC sin funding: protocolo congelado 2026-10-20
Autorización: usuario aprueba refinamiento previo y separa funding para un bloque posterior. Sólo Jesse MCP, entorno local. No live/paper/Pi, cambios de framework, descargas ni nuevos scripts.
Información previa: OOS2026 K1001 ya observado y diagnosticado. Todas las hipótesis siguientes están informadas por ese diagnóstico. 2020–2025 es desarrollo reutilizado; ninguna ventana reseteada vuelve a ser prueba independiente.

## Contrato
C principal, B control. Capital10.000USDT compartido, riesgo2%/6%, isolated3x, cap4.4, reserva.001 sólo sizing, warmup240, BTC/PAXG/SPY4h y M1 auxiliares. Fee nominal.00045 por lado y estrés.00095. No tocar configuración global: se fija form.config por sesión.
Ventana principal2020-10-15 inclusiva→2025-12-31 exclusiva, igual a las anclas. PAXG CapitalR12PaxgR2A6 y SPY CapitalR12SpyB/CR2A6 congelados. FuenteBTC CapitalR12K1001R2A6 preservada.

## Tres hipótesis, sin combinaciones ni rejillas
R1401 / BtcRefineR1401: ablación del suplemento K1001; conserva long y short original y su prioridad. before mantiene reloj/counters, pero _signal no admite explore_event. Prueba si complejidad suplementaria tiene aporte incremental robusto, no presume que quitarlo mejore.
R1402 / BtcRefineR1402: cambia sólo admisión long. Tras cumplir el setup original, exige eficiencia direccional de12cambios de cierre >1/3: (C_t-C_t-12)/sum(abs(diff(C_t-12..C_t))). Precio disponible, camino0/valoresno finitos=>rechazo. Mismo horizonte12 y cortegrueso1/3 del contexto explorado, ahora hipótesisopuesta para continuaciónlong; no se eligen mirando resultadosnuevos.
R1403 / BtcRefineR1403: cambia sólo admisión long. Tras setuporiginal, EMA120 actual>EMA120 diezposicionesatrás y precio>EMA120actual; guardlen140 y finite. Reutiliza el horizonte/lapso del short original como contexto lento; no indicador nuevo ni relación calibrada.
Cada variante copia fuente completa, renombra clase y añade auditcounts de admisión/candidatos/rechazos; no cambia stops, targets, duración ni sizing. R1401 sólo cambia fallbackshort, no altera cálculo de evento previo.
Tanda fija:3variantes×B/C×2fees=12backtests. Anclas existentes4sesiones, no rerun salvo divergencia de fuentes/form.
No repetir recetas de progreso24h/1R ni reclaimM1 ya descartadas. No ampliar lista por resultados adversos.

## Anclas
Bnom b9f0cccc-8de0-4076-a7fa-eb9ae8e1be38; Cnom3ec33cac-3ea6-43c7-9cfe-4d315930fee2.
Bestrésbb6e80f2-36f1-4c8f-8c8c-cac840794b8c; Cestrésac57b4d3-cfeb-4add-88cb-19358d701db1.
Antes de usar, verificar finished,formularios y fuentescongeladas.

## Puertas exploratorias previas
Candidata sólo si TODAS:
- Retiene>=90% del neto ancla y DDmotor no empeora en B y C, nominal y estrés. Tolerancia1e-7dinero/1e-9métricas para flotantes, no flexibilización económica.
- Mejora>=5% relativo elCalmar Cestresado.
- >=10entradasBTC diferentes en diferencia simétrica de firmas(symbol,side,opened_at) respectoanclaCnom. No confundir cantidades cambiadas porcapital con señalesnuevas.
- Incremento de retornoanualMTM no negativo en>=3de5bloques2021..2025 enC, nominal y estrés;2025parcial. Registros de años/meses completos y parciales visibles.
- No pierde más de1mespositivo frenteancla en61mesescompletosUTC deC, nominal y estrés.
Estas puertas son filtros operativos con retención de rentabilidad, riesgo, fricción y amplitud; no certifican edge. AblaciónR1401 no exenta. No elegir sólo por2026ni por bruto.

## Validación condicional
Si ninguna pasa: cierreconresultadosnegativos, sin vecinos/splits/2026nuevos. ConservarK1001como referencia, no promover.
Si alguna pasa: elegir porCalmarCestrésmayor; desempateDDmenosprofundo y luegoR1401(menoscompleja),R1402,R1403.
Elegida+ancla enC,nominaly estrés, cuatroventanasreseteadas:2020-10-15→2023-01-01,2023-01-01→2024-01-01,2024-01-01→2025-01-01,2025-01-01→2025-12-31(16corridas). Es prueba temporal de reglas congeladas, no walk-forward de entrenamiento. Pasa si netopositivo bajoambosfees en>=3ventanas, yDD no empeora másde2puntos porcentuales enninguna. Fondosreseteados10k; terminales/señalesbordes declarados.
Sólo siR1402pasa también vecinosER1/4y1/2; siR1403pasa vecinosEMA100/140, mismo lag10. Cada vecinonominalC+Cestrés4corridas; robustez si ambosnetospositivos, cadaCalmarCestrés>=90%ancla y DDestresado>=-25%. No escogermejorvecinopara reemplazarreceta.
Si pasaambasfases, evaluar elegidaB/Cnom+estrésen2026-01-01→2026-10-19(4corridas), sin nuevasdecisiones por eseresultado. Etiquetar desarrollo2026, no OOSconfirmatorio. Sin obligación de ganar2026paradeclarar aprendizaJe.
Si fallaverificacióncondicional,noretocar. SinMC/RSTno pedidos.

## Auditoría y entregas
Leer y comparar fuentes guardadas y snapshots3rutas. Reconciliar PNLtrades/fees/equityterminal, reportar abiertosforzados, anclas2025parciales, concentraciónmejor3BTC/PAXG, frecuencia, l/s, años/meses. Separar resultado por cierres de patrimonio mensual.
Logsadmisión comprueban mecanismo no vacío; no predicen fills de órdenes rechazadas.
Guardar registroURLs,códigos, métricas completas y conclusión por MCP. Alterminar, proponer bloque funding con dosobjetivosseparados: contabilidadpagos y señalpredictiva; abordar unidades/calendariodisponibilidad, paridadinvestigación/runtime y tests de noanticipación. No implementarfunding enestebloque.
