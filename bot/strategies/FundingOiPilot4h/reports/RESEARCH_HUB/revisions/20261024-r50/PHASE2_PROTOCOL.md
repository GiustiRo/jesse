# r50 F2: combinación y escalado a vol de cartera

Fecha: 2026-10-25. Aprobado por el usuario («pasemos a F2»). Este archivo se commitea **antes** de implementar y correr la F2.

## 1. Componentes (sin cambios internos)
- **C0**: cartera por clase de F1c.
- **C6**: rupturas cripto R2 + R3 de F1c.
- **N4**: R1 + M2a de F1b.

Cada componente es la curva diaria de su canasta, con la misma implementación, costes y funding de F1b/F1c. **No se re-pondera nada dentro de un componente:** hacerlo sumaría a N.

Las curvas de los componentes se arman desde el inicio de la ventana (común: 2020-10-15; larga: el inicio de F1b) para que la estimación de vol tenga historia.

## 2. Construcción de cartera (por principio, sin barrer variantes)
- **Pesos entre componentes:** riesgo inverso con vol expansiva de los retornos diarios, desde el inicio hasta el último cierre de cada mes. Se aplican desde el día siguiente y se rebalancean mensualmente.
- **Vol objetivo de cartera 17%:** factor k = 0,17 / σ_cartera.
  - σ_cartera sale de la covarianza expansiva de los componentes con los pesos vigentes, anualizada con √365.
  - Rebalanceo mensual, aplicado desde el día siguiente.
  - El control por correlación es este: la covarianza completa entra en σ_cartera.
- **Techo de apalancamiento k ≤ 8.** Sale del tope r49 de 8% de riesgo agregado abierto con mangas que arriesgan 1% por trade: si todas tuvieran un trade abierto a la vez, el riesgo sería 1% × k.
  - Con k ≤ 8, el riesgo por trade de cualquier manga queda debajo del 3% por trade de r49 en las canastas de ≥3 mangas.
  - El nocional por activo queda debajo de 5x.
  - Si el techo limita, se reporta la vol realizada.
- **Inicio:** la cartera se mide desde el primer mes con ≥120 días de historia de todos sus componentes.
- **Sin freno de DD.** El freno es asunto de F5.

## 3. Regla de inclusión (greedy, prerregistrada)
1. Los componentes se ordenan por Sharpe de la ventana común de F1b/F1c: C0 (1,82), C6 (1,53), N4 (1,08).
2. La cartera arranca con el primero.
3. Cada siguiente entra si la cartera con él mejora, en la ventana común, el Sharpe o el % de trimestres positivos de la cartera sin él, y la cartera resultante no es vetada en la ventana larga (Sharpe < 0 o DD < −25%).

Las tres carteras de un solo componente también se reportan, escaladas igual.

## 4. Puertas r9 de cartera (se reportan en las dos ventanas)

| Puerta | Umbral |
|---|---|
| CAGR | ≥ 30% (aspiración 40–50%) |
| DD | ≤ 20% (techo 25%) |
| PF | ≥ 1,2, sobre los trades de todas las mangas (escala-invariante) |
| Meses positivos | ≥ 65% |
| Trimestres positivos | ≥ 80% |
| Mediana mensual | > 0 |
| Sin los 2 mejores meses | resultado positivo |
| DSR | ≥ 0,95 con N = 80 |

La cartera final de la regla §3 se juzga en la ventana común. La ventana larga solo veta, igual que antes.

## 5. N
- La construcción y la regla de inclusión cuentan como **1** ensayo nuevo: N = 81.
- Las carteras de un componente son reportes, no selecciones.

## 6. Salida
- Informe con tabla de puertas r9, retornos por año y factor k realizado.
- Commit y push.
- Resumen al usuario.
- Si la cartera final pasa a F3, se congelan reglas, componentes y construcción antes de mirar los activos de validación.
