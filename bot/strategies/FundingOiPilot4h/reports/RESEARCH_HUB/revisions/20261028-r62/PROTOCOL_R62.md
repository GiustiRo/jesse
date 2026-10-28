# PROTOCOL_R62: descubridor automático con barandas

**Fecha:** 2026-10-28. **Rama:** `exploration/gpt-6.1-sol`. **Código:** `research_scripts/r62*.py`. Este protocolo se commitea antes de cualquier resultado económico de r62.

## 0. Decisiones del usuario y presupuesto
- **Objetivo:** un segundo motor de retorno que **no** sea tendencia larga (ese nicho ya lo ocupa R1).
- **Método:** una fábrica al estilo AlphaEvolve/FunSearch con quality-diversity (MAP-Elites).
  - Programas en un lenguaje acotado (DSL), sin Python libre.
  - Proponente: subagentes de Claude Code dentro de la sesión, sin API key.
  - Búsqueda genética local entre generaciones.
- **Liquidaciones:** solo datos gratuitos de Binance.
  - El `liquidationSnapshot` USDT-M fue borrado del archivo: el prefijo `futures/um/daily/liquidationSnapshot/` está vacío, y Binance lo confirmó el 2026-10-06 en el issue 337.
  - Queda el de COIN-M, del 2023-06-25 al 2024-10-14.
  - **Decisión del usuario:** proxy gratuito de cascadas (`futures/um/daily/metrics`), validado con COIN-M (§6).
- **Contadores:**
  - **N global = 150 al empezar.** Suma +1 por cada finalista que entra al embudo (máximo 5, así que el techo es 155).
  - **N_fab (contador nuevo `factory_trials`):** +1 por cada programa único (hash canónico) evaluado sobre datos reales. Techo de 3.000. La calibración sobre datos sintéticos no suma.
  - N_régimen 38 y N_temática 19 no se mueven.
- **Oráculo:** quedan 4 consultas y r62 usa como máximo una (q4).
- **Datos:** 2025 sellado y 2026 reservado. Todo array se corta en `r58.CUT_MS` (2025-01-01, exclusivo). Sin live ni paper.
- **Alts de U50 fuera de la búsqueda** (sesgo de supervivencia, r61). Las alts solo entran por q4.
- **Cómputo:** nativo en Windows (Python 3.12). Nada importa `r50_harness` ni la DB.
- **Series:** toda serie real evaluada se guarda con `r59.save_series('r62', …)`.

## 1. Datos (F0, `r62_data.py`)
- **Barras de 1 h desde los CSV de 1 min de Dukascopy** en `data/` (precio BID, proxy CFD):
  - núcleo: XAU, SPX (USA500, div10), WTI (LIGHTCMD, empalmado: hasta 2020-03-31 y desde 2020-08-01, sin rellenar el hueco), GAS y BOND (desde 2018-03);
  - validación: XAG, NDX (USATECH), COPPER y DEU.
- **BTC y ETH:** 1 h de los perpetuos de `data/r52/<SYM>_1h.npy` (desde 2020-01), con funding de `_funding.npy`.
- **Barras diarias:** se arman a partir de las de 1 h (día UTC; los minutos de fin de semana de los CFD se suman al lunes, como `r50_engines.daily_from_minutes`).
- **ETF diarios** (`data/r50/etf/`): EWJ y EWY, solo para la transferencia (§7.4).
- **Ventanas de desarrollo:**
  - CFD: de 2018-10-01 (inicio de `BENCH_P55_long`) al 2024-12-31;
  - cripto: de 2020-01-01 al 2024-12-31.
- **Salida:** `data/r62/bars/*.npz` (gitignored), con el sha256 en `data/r62/bars_manifest.json`.

## 2. DSL (`r62_dsl.py`)
**Estructura.** Un programa es un JSON:

`{universe, signal: [1–2 piezas], filters: [0–2], exit, size, exec}`

Cada pieza es `{kind, params}`, con cada parámetro tomado de su grilla. Tope: 4 piezas sin contar `exec`, y 6 parámetros. El parser rechaza cualquier `kind`, parámetro o valor fuera del catálogo.

**Hash canónico:** sha1 del JSON normalizado (claves ordenadas, filtros ordenados).

**Complejidad** = número de piezas + número de parámetros.

**Universos (dentro de la búsqueda):**
- `core_1h` / `core_1d`: BTC, ETH, XAU, SPX, WTI, GAS y BOND, cada activo como un libro independiente y la canasta a igual riesgo;
- `crypto_1h`: BTC y ETH;
- `cfd_1h`: XAU, SPX, WTI, GAS y BOND;
- pares a igual vol: `pair_BTC_ETH`, `pair_WTI_GAS`, `pair_SPX_BOND` y `pair_XAU_SPX`.

**Señales** (todas generan eventos de entrada con dirección; ninguna es de continuación de tendencia a más de 5 días):

| kind | parámetros (grilla) | idea |
|---|---|---|
| `zrev` | k ∈ {6, 24, 72} barras; z ∈ {1,5, 2, 2,5} | reversión a la media del z-score del retorno de k barras |
| `rsi2` | umbral ∈ {5, 10, 20} | RSI de 2 en extremo, operado en contra |
| `shock` | z ∈ {2, 3, 4}; modo ∈ {fade, follow} | retorno de una barra mayor a z·σ |
| `spread_z` | k ∈ {24, 120, 480}; z ∈ {1,5, 2, 2,5} | solo en pares: z-score del log-spread a igual vol, en contra |
| `voljump` | ratio ∈ {1,5, 2, 3}; modo ∈ {fade, follow} | vol de 24 h sobre vol de 30 d por encima del ratio; dirección según el último retorno de 24 h |
| `clock` | evento ∈ {funding_hour, cme_gap, month_end}; modo ∈ {fade, follow} | hora de liquidación de funding (00/08/16 UTC, la hora, no el valor: regla r49), hueco CME del fin de semana (BTC/ETH) o último día hábil del mes; dirección según el retorno previo de 8 h |
| `cascade` | z_oi ∈ {2, 3}; z_ret ∈ {2, 3}; modo ∈ {fade, follow} | solo cripto y solo si F0 lo habilita (§6): ΔOI de 1 h < −z_oi·σ con \|ret\| > z_ret·σ |

**Filtros:**

| kind | parámetros | idea |
|---|---|---|
| `volreg` | banda ∈ {low, mid, high} | terciles de la vol de 30 d sobre el año previo (causal) |
| `trendveto` | k ∈ {20, 60} días | no entrar en contra de la tendencia de k días cuando \|z\| > 1 |
| `session` | sesión ∈ {asia, europe, us} | solo en ese horario UTC |
| `btcstate` | estado ∈ {up, flat, down} | estado T90 causal de BTC (r55) |

**Salidas:** `time` (h ∈ {1, 6, 24, 72, 120} barras), `atr` (objetivo ∈ {1, 2} y stop ∈ {1, 2, 3} ATR de 24 barras, con tope de h = 120) y `mean` (cuando el z cruza 0, con tope de 72 barras).

**Tamaño:** `voltgt` (riesgo de 10% anual por activo), `side` ∈ {both, long, short}.

**Ejecución:**
- `taker`: fee de 0,045% por lado + slippage (5 pb en cripto; `r50_engines.SLIP_BPS` o 2 pb en los CFD).
- `maker`, con off ∈ {0,25, 0,5, 1,0} ATR de 1 h y vida m ∈ {1, 3, 6} barras:
  - la orden límite se coloca al cierre de la barra de la señal, a off·ATR a favor (debajo para comprar);
  - **llena solo si una barra posterior, dentro de las m siguientes, cruza el límite estrictamente** (low < límite − 1 pb, o high > límite + 1 pb);
  - el precio de llenado es el límite, sin mejora por hueco;
  - fee de 0,018%. Si no se llena, no hay trade y la orden queda registrada como no llenada;
  - la salida también es maker, al cierre de la barra de salida ± 0 con una barra de vida; si no se llena, sale taker en la barra siguiente.
- **Funding:** los cripto pagan el funding real en las horas de liquidación. Los CFD no tienen carry (aproximación declarada).

**Motor:** `r62_dsl.run(program, bars) → (pos, daily_ret, trades)`, vectorizado sobre barras de 1 h (o diarias). La señal se calcula con datos hasta el cierre de t y la entrada ocurre en t+1 o después. Cada trade guarda la entrada, la salida, la dirección, si fue maker o taker y su PnL.

## 3. Evaluador (`r62_eval.py`)
- **Pliegues:** grupo × año.
  - Grupos: cripto (BTC, ETH), materias (XAU, WTI, GAS) y acciones/bono (SPX, BOND).
  - Años: de 2019 a 2024 (cripto, de 2020 a 2024).
  - Un pliegue cuenta si tiene al menos 10 trades. El programa necesita al menos 5 pliegues válidos; si no, la nota es −∞.
- **Nota** = Sharpe anualizado del **peor** pliegue válido − **λ·complejidad**, con **λ = 0,05**.
- **Serie del programa:** retorno diario de la canasta de su universo (a igual riesgo), en días UTC. Ventana: la de §1 según el universo.
- **Puertas de elegibilidad para el archivo** (deben cumplirse las tres):
  - **e1, costos:** con fees ×2, slippage ×2 y maker con penetración de 2 pb, Sharpe de la serie completa > 0;
  - **e2, contribución marginal:** con `BENCH_P55_long`, combinación 0,85·P55 + 0,15·x̃ (x̃ es la serie escalada a la vol de P55) en días comunes. ΔSharpe contra P55 > 0;
  - **e3, rotación (placebo de timing):** la serie de eventos de entrada de cada activo se desplaza circularmente (el mismo desfase para todos los activos, de 90 días como mínimo) y se vuelve a correr el motor. Son 200 desfases con semilla 62. p = (1 + #{Sharpe rotado ≥ real}) / 201. **Pasa con p < 0,10.** Solo se calcula para los programas que ganarían su celda.
- **Diagnóstico guardado:** Sharpe por pliegue, tasa de llenado maker, tenencia media, sesgo de dirección y la puerta que falló.

## 4. Casilleros MAP-Elites (`r62_factory.py`)
**Ejes:**
- **ρ diaria con `BENCH_R1_long`:** < 0,1 / 0,1–0,3 / > 0,3;
- **tenencia media:** < 1 d / 1–5 d / > 5 d;
- **dirección:** exposición neta media / exposición bruta media > 0,33 (largo), < −0,33 (corto) o neutral.

**Celdas:** 27. **Bloqueadas:** las 3 celdas «largo con ρ > 0,3», que ya ocupa R1.

**Regla:** una celda guarda el programa elegible de mayor nota. Un programa no elegible queda en el registro, pero no entra en el archivo.

## 5. Búsqueda (F2)
- **Semillas:** 20 programas al azar del DSL (semilla 62) más los que proponga la generación 0 del LLM.
- **10 generaciones.** En cada una:
  1. **LLM:** un subagente de Claude Code (modelo sonnet) recibe el paquete anonimizado (§5.1) y devuelve de 8 a 12 programas en JSON. **Si la respuesta usó herramientas** (tool_uses > 0), la generación del LLM se descarta. Si un programa no pasa el parser, se descarta ese programa.
  2. **Búsqueda local:** unas 150 evaluaciones, con estos operadores sobre las élites:
     - mutación a un vecino en la grilla (60%);
     - cambio de una pieza por otra del catálogo (25%);
     - cruce de piezas entre dos élites de la misma fila de ρ (15%).
     
     Los hash ya evaluados no se repiten.
- **Corte:** a las 10 generaciones o con N_fab = 3.000, lo que ocurra primero.
- **Finalistas:** como máximo 5. Se elige la élite de mayor nota de cada celda no bloqueada, por orden de nota. Hay como máximo un finalista por combinación de tenencia y dirección. Cada finalista suma +1 a N.

### 5.1 Anonimización
El paquete que ve el LLM lleva:
- el catálogo del DSL;
- las élites (programa, nota, celda, Sharpe por pliegue con etiquetas F1…Fk barajadas por generación);
- los programas que fallaron y en qué puerta;
- por cada activo, un resumen estadístico de sus retornos estandarizados de 1 h (autocorrelación de los lags 1–24, curtosis, asimetría, perfil por hora del día relativo y correlación cruzada).

Los activos van renombrados A, B, C… con una permutación nueva en cada generación. No van fechas, años, precios, tickers ni nombres de activos. En el DSL que ve el LLM, los universos se nombran por su letra: `U1`…`U9`.

`r62_factory.leak_check(pkg)` frena si encuentra:
- un patrón de año (19xx/20xx);
- un ticker o nombre de activo del universo (BTC, ETH, XAU, GOLD, SPX, WTI, OIL, GAS, BOND, LUNA, FTX…);
- una fecha ISO;
- un número mayor que 1.000.

### 5.2 Registro
Cada evaluación real escribe:
- una línea en `data/r62/factory_log.jsonl` (hash, programa, origen LLM/GA/semilla, generación, nota, puertas, celda);
- su serie diaria, con `save_series('r62', 'R62_P_<hash8>', …)`.

N_fab se escribe en `TRIAL_REGISTRY.json → factory_trials` al cerrar cada generación.

## 6. Proxy de cascadas (F0, `r62_liq.py`)
1. **Bajada** de `data.binance.vision/data/futures/um/daily/metrics/{BTCUSDT,ETHUSDT}`, del 2020-09-01 al 2024-12-31, y de `futures/cm/daily/liquidationSnapshot/{BTCUSD_PERP,ETHUSD_PERP}`, del 2023-06-25 al 2024-10-14.
   - Cada archivo se verifica contra su `.CHECKSUM`.
   - Se guardan en `data/r62/raw/` (gitignored) y se procesan con `python -P` (sin el directorio actual en el path; `-I` también quita los paquetes de usuario donde está numpy).
2. **Cobertura:** primera fecha con OI no nulo; fracción de filas de 5 min presentes por año; huecos de más de 1 día. Se reporta en `R62_PHASE0_*.md` **antes** de que la pieza se use.
3. **Proxy:** intensidad diaria = Σ en el día de max(0, −ΔOI₁ₕ/σ) · \|ret₁ₕ\|/σ, con σ móvil de 30 d y causal.
4. **Validación contra COIN-M:** AUC diaria del proxy de BTCUSDT/ETHUSDT contra el indicador «día en el decil superior del nocional liquidado de BTCUSD_PERP/ETHUSD_PERP».
5. **Habilitación de la pieza `cascade`** (las tres condiciones):
   - cobertura ≥ 90% de las filas de 5 min en cada año de 2021–2024;
   - AUC ≥ 0,70 en los dos símbolos;
   - al menos 30 días del decil superior en la ventana de COIN-M.
   
   Si falla alguna, la pieza sale del menú, lo aviso y no se compra nada.

## 7. Calibración (F1) y embudo (F3)

### 7.1 Generador sintético (`r62_synth.py`)
- **«Regímenes»:** bootstrap estacionario de días completos (bloque medio de 20 días). Cada día lleva sus 24 barras de 1 h de todos los activos a la vez. El bloque siguiente se elige entre los días cuyo estado T90 de BTC sigue la cadena de Markov estimada en desarrollo. Se reconstruyen precios desde los log-retornos. El OI se remuestrea con el mismo índice.
- **«Ruido»:** vol real de 1 h de cada activo (EWMA de 24 barras, sin anticipar) × shocks estandarizados. Los shocks salen de barajar iid las barras de 1 h, con el mismo índice para todos los activos, y la media se pone en 0.
  - Conserva la correlación cruzada contemporánea, la curtosis y la forma de la vol.
  - No deja nada predecible en la media.
  - H/L se arman con el rango relativo de la barra original barajada.
- **«Plantado»:** el «ruido» más dos ventajas:
  - **P1, reversión tras un shock:** en cripto de 1 h, después de \|r\| > 2,5σ, durante las 6 barras siguientes se suma una deriva de −κ·r/6 por barra;
  - **P2, reversión de un par:** el log-spread a igual vol de WTI/GAS pasa a seguir un OU con vida media de 120 barras.
  
  κ y la fuerza del OU se calibran en F1, antes de correr la fábrica, para que los programas «oráculo» conocidos (P1: `shock` fade z 3, salida `time` 6, maker; P2: `spread_z` k 120, z 2, salida `mean`) den un Sharpe neto de 0,8 ± 0,1 (P1) y 0,7 ± 0,1 (P2) en el sintético.

### 7.2 Calibración (F1, N + 0)
Se corre la fábrica completa (§5, con el mismo presupuesto y LLM incluido) sobre 2 semillas de «ruido» y 2 de «plantado». El SPA del §7.3(1) se calcula sobre todas las series de cada corrida.

**La calibración pasa si se cumplen las dos:**
- **C1, ruido:** en las dos semillas, ningún finalista tiene SPA p < 0,05 (contra cash y marginal).
- **C2, plantado:** en las dos semillas, aparece al menos un finalista cuya señal es la pieza plantada (`shock`/fade en cripto, o `spread_z` en `pair_WTI_GAS`), con SPA p < 0,05.

Si una semilla falla y la otra pasa, se corre una tercera, que decide. **Si la calibración falla, la fábrica no se usa sobre datos reales y r62 cierra.** Descriptivo: cuántos programas «elegibles» aparecen en el ruido.

### 7.3 Embudo (F3)
Cada finalista pasa por estos pasos, en orden:

1. **SPA sobre todas las series reales de F2** (`r62_eval.spa_fast`, idéntico a `r59.spa_pvalue` y verificado en el selftest; bloque 20, 2.000 réplicas, semilla 62), en la ventana de desarrollo común, con dos versiones:
   - **(a) contra cash:** G = retornos diarios de cada programa a vol de 10%;
   - **(b) marginal:** G = (0,85·P55 + 0,15·x̃) − P55.
   
   El finalista pasa si p < 0,05 en (a) y en (b) **y** su columna es la del máximo, o su t individual supera el umbral de la distribución bootstrap del máximo, al 5%.
2. **Puertas r49 de manga:**
   - DSR ≥ 0,95 con N = 150 + el número de finalistas (también se reporta con N + N_eff, siendo N_eff = razón de participación de los autovalores de la correlación de todas las series de F2);
   - Sharpe neto ≥ 0,8;
   - al menos 100 trades (30 si es diaria);
   - los 5 mejores trades < 60% del PnL.
3. **PBO** (`r60.pbo_cscv`, S = 16) sobre la matriz de las élites del archivo: < 0,5.
4. **Filtro sintético:** 200 historias de «regímenes» (semilla 62). Se descarta si la mediana del Sharpe sintético es ≤ 0, o si el Sharpe real supera el p95 sintético (suerte de camino).
5. **Transferencia** (con el programa congelado):
   - **Programa en CFD o diario:** se corre sobre los activos de validación (XAG, NDX, COPPER y DEU en 1 h; EWJ y EWY si es diario). Pasa si la canasta tiene Sharpe > 0 y al menos la mitad de los activos son positivos.
   - **Programa cripto:** q4 en H, con criterio en `r59_criteria.py` commiteado antes de consultar:
     - el programa sobre las 50 alts de H a 1 h, con funding y canasta a igual riesgo, en 2021-07-02 → 2024-12-31;
     - márgenes: (a) Sharpe − 0,3; (b) Sharpe con costos ×2; (c) ΔSharpe de 0,85·P55 + 0,15·x̃ contra P55;
     - EE por bootstrap estacionario (bloque 20, 1.000 réplicas).
     
     **Poder** antes de consultar: Φ((½·S_D − 0,3)/EE) ≥ 0,4; si no, se reporta al usuario y no se consulta. **Como máximo una consulta**: si hay varios finalistas cripto, va el de mayor nota.

**Resultado:**
- Un finalista que pase los 5 pasos se propone como «P-r55 + programa» (15% a igual vol), **sujeto a la aprobación del usuario**. Nada se congela sin él y 2025 no se toca.
- Si ninguno pasa, P-r55 queda igual.

## 8. Selftests (F0, `r62.py selftest`)
1. El parser rechaza piezas, parámetros y valores fuera de la grilla, y el hash canónico no cambia al reordenar los filtros.
2. **Maker sin anticipación:**
   - no se llena en la barra de colocación;
   - una barra cuyo low toca el límite sin cruzarlo en más de 1 pb no llena;
   - la señal en t solo usa datos ≤ t (se verifica alterando las barras > t y comparando la señal en t).
3. `spa_fast` = `r59.spa_pvalue` en una matriz pequeña, con la misma semilla.
4. `leak_check` frena con un paquete contaminado y pasa con el real de la generación 0.
5. **Control de casilleros:** un programa «Donchian largo» armado fuera del DSL con el mismo motor (`core_1d`, 20/55, largo) tiene que dar ρ > 0,6 con `BENCH_R1_long` y caer en una celda bloqueada.
6. El corte de datos: ninguna barra ≥ 2025-01-01.

## 9. Advertencias declaradas
1. **D está muy vista.** La fábrica busca sobre los mismos activos y años que r49–r61. El SPA cobra solo lo que la fábrica prueba, no lo que el historial ya probó con otros métodos. Por eso el DSR usa la N global y la transferencia es obligatoria.
2. **Los CFD de Dukascopy no son fills de Binance.** El maker sobre CFD es una aproximación: el libro de los perpetuos TradFi de Binance es fino (`SLIP_BPS`).
3. **El LLM tiene conocimiento previo de ideas genéricas** (por ejemplo, «la reversión intradía funciona»). La anonimización impide que use la historia de activos y fechas concretos, no que use teoría.
4. **El proxy de cascadas no es la serie de liquidaciones.** COIN-M es otro mercado y solo cubre 16 meses.
5. **Poder:** con unos 6 años, el EE del Sharpe es ~0,4, así que un efecto real de 0,5 puede no pasar el SPA contra miles de series. El SPA es conservador a propósito.
6. **El sintético conserva la estructura dentro del bloque** (20 días), así que una ventaja de horizonte corto sobrevive y el filtro no la descarta. Sirve para descartar ventajas que dependen del orden de los regímenes, no para confirmar.

## 10. Enmiendas

### E1 (2026-10-28, en F0, antes de cualquier resultado económico de la fábrica)
Son precisiones de implementación que el protocolo no fijaba o que el código obliga a ajustar. Ninguna sale de ver un resultado de un programa.

1. **`python -P` en lugar de `python -I`** para los scripts que leen datos bajados. `-I` también quita los paquetes de usuario, donde está numpy. `-P` saca del path el directorio actual y el del script, que es lo que protege de un módulo plantado.
2. **Pares solo taker.** Dos patas no se llenan como una sola orden límite, y el spread no tiene rango dentro de la barra. El parser rechaza maker en los universos de pares. El spread se arma con O = H = L = C, así que la entrada taker ocurre al cierre de la barra siguiente.
3. **Segunda señal.** Dos eventos de inicio rara vez coinciden en la misma barra. La segunda señal confirma si disparó en la misma dirección dentro de las 6 barras previas (`CONFIRM_BARS`).
4. **`volreg`:** el tercil de la vol de 30 días se calcula sobre los 365 valores diarios previos y se aplica desde el día siguiente.
5. **Puerta de cascadas (§6.5): falla en sentido estricto.**
   - BTCUSDT: cobertura de 99,6–100% en 2021–2024, AUC 0,837 y 48 días del decil superior. Pasa.
   - ETHUSDT: AUC 0,841, pero sus metrics recién empiezan el **2021-12-01**, así que la cobertura de 2021 es del 8,5%.
   - **Mientras el usuario no decida otra cosa, la pieza `cascade` queda fuera del menú** (`liq_f0.json → cascade_enabled: false`). La opción para decidir es habilitarla con ETH solo desde 2021-12, sin eventos antes.
6. **Control del §8.5 (Donchian 55/20 largo en `core_1d`):** da ρ 0,73 con R1, Sharpe 1,44 y cae en la celda bloqueada `rho2|hold2|long`. Es el control de los casilleros, no un ensayo nuevo (N + 0).
7. **El selftest de q4** corrió un programa de demostración (`shock` fade, maker) sobre la mitad 1 de U50, que es el holdout falso de r60. Dio Sharpe −0,12 (N + 0, como los selftests de r60 y r61). Ese programa no tiene ningún privilegio en la búsqueda.

### E2 (2026-10-28, decisión del usuario tras F0, antes de F1)
- **La pieza `cascade` queda habilitada** aunque la puerta estricta del §6.5 falló por la cobertura de ETH en 2021.
- **Ventanas del OI:**
  - **BTC** desde el 2021-01-01;
  - **ETH** desde el 2021-12-01.
  
  Antes de esas fechas el z de ΔOI vale NaN y la pieza no genera eventos (`r62_eval.OI_FROM`). Con el calentamiento de 30 días, el primer evento posible en ETH cae a fines de 2021-12.
- `liq_f0.json` conserva el veredicto estricto (`cascade_enabled: false`). La habilitación queda registrada en el código (`CASCADE_BY_AMENDMENT = 'E2'`).
- **Consecuencia declarada:** en el pliegue cripto de 2021, solo BTC aporta eventos de cascada.

### E3 (2026-10-28, en F1, antes de cualquier corrida de la fábrica más allá de las semillas)
1. **Fuerza de las ventajas plantadas** (`data/r62/f1_calib_grid.json`, semillas 101–106, distintas de las de las corridas):
   - **P1:** κ = 0,20 da al programa oráculo un Sharpe neto medio de 0,80 (dentro de 0,8 ± 0,1).
   - **P2:** no llega a 0,7. Con costos taker de dos patas (GAS 5 pb), el oráculo alcanza un techo de ~0,5 (α = 50: 0,51; α = 60–70: 0,45–0,48).
   - **Se usa α = 50.** P2 queda más débil que lo previsto, lo que hace C2 más difícil, no más fácil.
2. **SPA marginal (§7.3.1 b):** la columna es la combinación 0,85·P55 + 0,15·x̃ **reescalada a la vol de P55**, menos P55. Así, una media > 0 equivale a ΔSharpe > 0, igual que e2. La forma literal sin reescalar exigiría que el programa le gane a P55 en Sharpe por sí solo.
3. **Paquete:**
   - los conteos (trades y órdenes no llenadas) van en centenas, porque `leak_check` rechaza todo número mayor que 1.000;
   - el filtro `btcstate` se muestra como `leadstate`.
4. **Uso de herramientas del subagente:** para no pegar paquetes de 10–20 mil caracteres en la sesión, el subagente puede usar **solo** Read sobre su `pkg_<g>.json` y Write sobre su `answer_<g>.json`, más la entrega final. Con más de 3 usos de herramientas, la generación del LLM se descarta. La prueba previa al protocolo (un paquete pegado en el prompt) contó 1 uso: la entrega.
