# r50 F0: infraestructura y datos (2026-10-25)

**Veredicto:** F0 cumplida.
- El arnés `research_scripts/r50_harness.py` reproduce las tres sesiones Jesse de r49 dentro de la tolerancia (error diario de equity < 0,5%). BTC y PAXG coinciden a nivel de orden.
- El núcleo de 7 activos está cargado en Jesse. ETH spot termina en la importación en curso.
- La validación queda con 5 activos: plata, Nasdaq, cobre, EWJ y EWY. El platino quedó excluido por datos.
- Corridas Jesse usadas: 0 de 10. N sin cambios: 57; F1 lo lleva a 63.

## 1. Reproducción arnés vs Jesse

Comparación punto a punto contra la curva diaria Portfolio de cada sesión, en sus instantes de muestreo reales.

| Sesión r49 | Error diario máx. | Error medio | Equity final arnés / Jesse | Sharpe arnés / Jesse (curva) | DD arnés / Jesse | Órdenes, fees y funding |
|---|---|---|---|---|---|---|
| BTC http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd | 4×10⁻¹⁶ | 1×10⁻¹⁶ | 18.845,04 / 18.845,04 | 1,040 / 1,040 | −11,85% / −11,85% | 120 órdenes; fees 78,97 = 78,97; funding −2.376,70 = −2.376,70 |
| PAXG http://localhost:9200/#/backtest/02a484b6-a237-4ffb-a283-7db32354a61e | 0,054% (solo el punto final) | 3×10⁻⁷ | 21.912,56 / 21.900,80 | 1,264 / 1,263 | −13,12% / −13,12% | 102 órdenes idénticas; Jesse agrega el cierre forzado del final (fee 11,76) |
| SPY http://localhost:9200/#/backtest/21063c59-f0f5-4a07-a66a-040f75e3f475 | 0,43% | 0,18% | 16.167,59 / 16.115,61 | 0,905 / 0,899 | −14,6% / −14,7% | 103 contra 104 órdenes; fees 200,46 contra 200,19 |

**Hallazgos técnicos:**
- Las sesiones con funding corren en 1m y muestrean la equity a las 00:01 UTC. Las sesiones sin funding corren en *fast mode* y muestrean a las 04:00 UTC, al cierre de la vela de 4h.
- PAXG spot tiene minutos ilíquidos, así que la diferencia de muestreo explicaba errores de hasta 4,6%. Con el muestreo exacto, desaparecen.
- **SPY**, única divergencia:
  - El 2021-06-14 a las 04:00 el arnés activa juntos los componentes de 20 y 55 días (cierre 425,20 contra un máximo previo de 424,94) y rebalancea; Jesse lo hace un día después.
  - Ninguna vela visible en los datos explica la demora de Jesse. Después las órdenes se vuelven a alinear.
  - Queda como limitación conocida, dentro de tolerancia. En F4, si hay diferencias, gana Jesse.

**Archivos:**
- `research_scripts/data/r50/repro.json`.
- Comandos: `r50_harness.py repro | diff --asset X | probe`.

## 2. Inventario de datos (hasta 2025-12-31; 2026 no se usa)

**Núcleo**

| Activo | Ventana común | Ventana larga | Notas |
|---|---|---|---|
| BTC | Binance Perp BTC-USDT desde 2020-01-01, funding `0ab14bc2…` | Binance Spot BTC-USDT 2017-08-17 → (importado en r50) | Símbolos separados, sin empalme. |
| ETH | Binance Perp ETH-USDT desde 2020-08-15, funding `22bd891c…` | Binance Spot ETH-USDT desde 2017-08-17 | La importación termina al cerrar F0. |
| Oro | Custom Data XAU-USDT 2010-01-01 → 2025-12-31 | ídem | Dukascopy (r49). |
| SPX | Custom Data SPXD-USDT 2011-09-19 → 2025-12-31 | ídem | Dukascopy (r49). |
| WTI | Custom Data WTI-USDT 2011-09-23 → 2025-12-31 | ídem | Sin abr–jul 2020 (precio negativo), como en r49. |
| Gas natural | Custom Data NATGAS-USDT 2012-09-02 → 2025-12-31 | ídem | Ver detalle abajo. |
| Bono largo EE.UU. | Custom Data USTBOND-USDT 2018-03-01 → 2025-12-31 | **sin lente larga** | Ver detalle abajo. |

**Gas natural (Dukascopy GAS.CMD/USD):**
- Divisor 10.000: da 2,71 USD/MMBtu en 2015-03, coherente con el nivel conocido.
- Sin datos antes de 2012-09.
- 4.140 días con datos y 26 días hábiles vacíos, que son feriados.

**Bono (Dukascopy USTBOND.TR/USD):**
- Sin datos útiles antes de 2018. El usuario decidió usar solo 2018+, sin TLT.
- Datos densos desde 2019: mediana de 1.118 filas por día.
- El 2018-03-13 se excluyeron 137 registros con precios en cero (`--drop-bad-records-on`, anotados en el manifiesto); los demás días mantienen el decodificador estricto.
- Escala: 159,4 en 2021-03.

**Validación** (solo F3, motores congelados)

| Activo | Fuente | Estado |
|---|---|---|
| Plata | Dukascopy XAGUSD | Descargando. Escala verificada: 16,4 en 2015-03. |
| Nasdaq 100 | Dukascopy USATECH.IDX/USD | En cola. Escala verificada: 4.478 en 2015-03. |
| Cobre | Dukascopy COPPER.CMD/USD | En cola. Divisor 10.000: 3,13 USD/lb en 2018-03. |
| EWJ | Yahoo, diario 2000-01-03 → 2025-12-31 | Listo. 6.539 velas; chequeos OK (el único hueco es el cierre tras el 11-S). |
| EWY | Yahoo, diario 2000-05-12 → 2025-12-31 | Listo. 6.448 velas; chequeos OK. |
| Platino | — | **Excluido por datos.** Dukascopy no lo tiene (XPTCMDUSD y XPTUSD vacíos); Stooq bloquea las descargas automatizadas con un desafío anti-bots que no se elude. |

Los perpetuos EWJ y EWY existen recién desde 2026-03: no hay confirmación posible en Jesse con 1m.

## 3. Decisiones e incidencias de F0
- **Bono:** solo 2018+, sin lente larga. Su manga no puede ser vetada por historia larga; se reporta como límite.
- **Platino:** excluido según la regla del usuario.
- **EWJ/EWY:** datos diarios de Yahoo (fuente prevista en el plan, «Stooq o Yahoo»).
- **Costes:** enmienda 4b del protocolo F1, antes de cualquier resultado. Slippage extra por lado de 15 bp en el bono, 5 bp en gas y cobre y 10 bp en EWJ, según los libros de Binance medidos.
- **Reinicio de Jesse** por la corrección de funding con margen aislado (merge `7101324e`, hecho por la sesión coordinadora con aprobación del usuario):
  - se coordinó al terminar BTC spot;
  - la descarga de gas retomó desde la caché diaria;
  - ninguna corrida de r50 depende del comportamiento anterior.
- **Importaciones grandes por MCP:** superan el timeout, pero terminan en el host; se verificaron con `get_existing_candles`.

## 4. Protocolo F1
- `RESEARCH_HUB/revisions/20261024-r50/PHASE1_PROTOCOL.md`, commiteado (`c727df98`) antes de cualquier resultado de screening.
- M1, M2a, M2b, M3, M3-nr y M4: N declarado 63.

## 5. Siguiente paso
F1: screening de M1–M4 sobre el núcleo con el protocolo commiteado, al completar ETH spot.
