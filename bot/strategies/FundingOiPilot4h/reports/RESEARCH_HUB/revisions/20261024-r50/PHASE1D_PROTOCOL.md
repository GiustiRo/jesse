# r50 F1d: agenda cerrada, compuertas de salida y confirmación única

Fecha: 2026-10-25. Aprobado por el usuario («Perfecto, adelante sigue de forma autónoma»), sobre el proceso de `reports/Búsqueda de estrategias y validación.md`. Este archivo se commitea **antes** de implementar, cargar datos nuevos o correr cualquier prueba de F1d.

## 0. Decisiones del usuario (2026-10-25)
1. **Metas de regularidad a seguimiento.** M65 (meses positivos ≥ 65%) y Q80 (trimestres positivos ≥ 80%) pasan de puerta de aprobación a métrica de seguimiento: se reportan siempre, pero no aprueban ni descartan.
   - Siguen como puertas de cartera: CAGR ≥ 30%, DD ≤ 20%, PF ≥ 1,2, mediana mensual > 0, resultado positivo sin los 2 mejores meses y DSR ≥ 0,95.
2. **2026 autorizado solo para confirmar** motores basados en R1, R2 y R3. Esos motores no se probaron sobre 2026. Se mira **una sola vez**, en la confirmación (§4).
3. **Agenda cerrada:** solo se prueban las variantes listadas en §2. El presupuesto máximo es 40; esta agenda usa 9.

## 1. Datos de exploración
- Núcleo de 7 activos, con las ventanas y costes de F1–F1c.
- **Lente principal para las compuertas:** la ventana larga, desde 2011 o la primera historia disponible; cripto spot desde 2017-08.
- La ventana común (2021–25) también se reporta.
- **Datos que no se usan en exploración:**
  - los activos de validación de F3, ya gastados;
  - los activos de confirmación de §4;
  - 2026.

## 2. Agenda (todo solo-largo, valores fijos)

| Id | Familia | Regla |
|---|---|---|
| T1 | TSMOM 1/3/12 meses, continuo | Para N ∈ {21, 63, 252} días: s_N = clip(r_N / (σ_d·√N), −2, 2) / 2, con σ_d de 60 días. La señal es la media, recortada a ≥ 0. Posición = señal × 17% / vol 30 d, techo 2x, banda 25%, diaria. 7 activos. |
| T2 | T1 con vol de rango | Igual que T1, pero la vol de tamaño usa el estimador de Parkinson de 30 días y la banda es 10% (Baltas-Kosowski). |
| T3 | R1 con vol de rango | R1 (ensamble Donchian 4h), cambiando solo la vol realizada por el estimador de Parkinson sobre las mismas velas. |
| K1 | Carry de funding cripto | Largo spot y corto perpetuo por el mismo nocional, igual a 0,75 × equity, en BTC y en ETH. Se abre si la media de funding de 21 días anualizada supera 10% y se cierra si baja de 0. Costes: perpetuo 0,045% por lado, spot 0,075% por lado. El PnL es funding real más las diferencias de precio spot–perpetuo de Binance, de los dos símbolos almacenados. |
| X1 | Momentum transversal 12-1 | Al cierre de cada mes, ordenar los 7 activos por retorno entre t−13 y t−1 meses y tomar los 3 primeros, sin filtro absoluto. Cada uno recibe 1/3 × 17% / vol 30 d, techo 2x. Costes del activo; funding en BTC y ETH. |
| V1 | Reversión de largo plazo («value») | Igual que X1, pero toma los 3 activos con **menor** retorno de 36 meses (entre t−36 y t−0). |
| T4 | Tope por correlación (construcción) | Sobre la cartera de §3: a fin de mes el factor k se multiplica por CF = √(N / (1 + (N−1)·ρ̄)) / mediana expansiva de CF, con ρ̄ = correlación media de 60 días entre mangas. CF queda entre 0,5 y 1,5. |
| P1 | Cartera base solo tendencia | R1 (7 activos) + C6 (rupturas cripto), con la construcción congelada de F2: riesgo inverso, vol 17%, k ≤ 8. |
| P2 | Cartera final | P1 más las mangas de T1, T2, T3, K1, X1 y V1 que pasen sus compuertas (§3), agregadas en forma greedy por Sharpe largo. Entra la que mejore el Sharpe o los trimestres positivos de la cartera. |

## 3. Compuertas de salida (exploración)

**Por manga o canasta** (T1, T2, T3, K1, X1 y V1). Pasa si cumple todas:
- Sharpe ≥ 0,5 en la ventana larga y ≥ 0,5 en la común;
- Sharpe > 0 en las dos mitades de la ventana larga, separadas en 2018-01-01. K1 usa cripto desde 2020, así que sus mitades son 2020–22 y 2023–25;
- top-5 trades < 60% del PnL, cuando hay trades individuales;
- para T3: mejorar a R1 en Sharpe largo.

**Proceso.** Se calcula el **PBO** (CSCV, S = 16) sobre la matriz de retornos diarios de la ventana larga de todas las canastas evaluadas en F1, F1b, F1c y F1d. La selección de F1d se considera sobreajustada si PBO ≥ 0,3; en ese caso se reporta y no se avanza a la confirmación.

**Cartera** (P1/P2, con o sin T4). En las dos ventanas:
- CAGR ≥ 30%;
- DD ≤ 20%;
- PF ≥ 1,2;
- mediana mensual > 0;
- positiva sin los 2 mejores meses;
- DSR ≥ 0,95 con N declarado.

También se reportan el N efectivo, estimado por correlación media entre canastas, y la regularidad (M65 y Q80) como seguimiento.

T4 se aplica a la cartera final solo si mejora su Sharpe largo sin empeorar el DD. Es una decisión de construcción y cuenta en N.

## 4. Confirmación única (una sola mirada, después de congelar)

**Qué se congela antes:** el código, las mangas y la construcción de la cartera final, en un commit propio.

**Datos de confirmación.** Nunca se cargaron y se cargan recién después del congelamiento. Si alguno no existe en la fuente, se excluye y se reporta, sin sustituirlo.
- **Cripto** (Binance Perpetual Futures, con su funding real): SOL-USDT, XRP-USDT, BNB-USDT y DOGE-USDT, desde 2020-10.
- **CFD** (Dukascopy):
  - DAX (`DEUIDXEUR`);
  - Nikkei 225 (`JPNIDXJPY`);
  - FTSE 100 (`GBRIDXGBP`);
  - soja (`SOYBEANCMDUSX`);
  - azúcar (`SUGARCMDUSD`);
  - cacao (`COCOACMDUSD`).

  Se usan desde su primer dato hasta 2025-12-31.
- **2026:** del 2026-01-01 al último dato disponible antes del 2026-10-24, en los 7 activos del núcleo, solo para las mangas basadas en R1/R2/R3 de la cartera final y para la cartera recortada a esas mangas.

**Asignación en los activos nuevos:**
- cada manga de la cartera final se aplica a todos los activos nuevos de su ámbito: las mangas cripto (C6) a los 4 perpetuos;
- las de 7 activos a los 10 activos nuevos;
- con las configuraciones análogas de F3: los índices como SPX y los commodities agrícolas como el gas.

**Puertas de confirmación:**
- Sharpe > 0 en la mayoría de las combinaciones manga × activo nuevo;
- ningún derrumbe (Sharpe < −0,5 o DD < −30%);
- canasta agregada de los activos nuevos con Sharpe > 0 y t ≥ 1,28 (p < 0,10 de una cola);
- 2026: Sharpe de la cartera recortada ≥ −0,5 y DD no peor que el percentil 5 de un bootstrap por bloques de 21 días de los retornos 2021–25 sobre la misma longitud.

Si falla, la candidata se retira. Cualquier versión modificada vuelve a §2 y necesitaría datos frescos nuevos.

## 5. Después
- **F4:** confirmación en Jesse de las mangas finales, con ≤ 10 corridas y máximo 2 simultáneas.
- **F5:** freno catastrófico y congelamiento.
- **Paper trading:** requiere autorización explícita del usuario. Live queda fuera de alcance.

## 6. N
Nueve variantes nuevas: T1, T2, T3, T4, K1, X1, V1, P1 y P2. **N declarado: 81 + 9 = 90.**
