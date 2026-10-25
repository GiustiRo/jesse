# r50 F3: validación en 5 activos no vistos (2026-10-25)

**Veredicto: F3 no pasa.** Por protocolo no se re-ajusta nada y la decisión vuelve al usuario.

- **A. Motor × activo:** Sharpe > 0 en 10 de 21 combinaciones (48%, la puerta pide > 50%), con **7 derrumbes**. Todos son de los motores de reversión, **M2a y N1**, en plata, cobre, EWJ y EWY.
- **B. Regla de clase:** falla en EWJ (Sharpe −0,34) y queda en cero en EWY (−0,01). Pasa en plata (0,39), cobre (0,30) y Nasdaq (0,78).
- **Lectura central:** la **tendencia generaliza y la reversión no.**
  - R1, R2 y R3 son positivos en casi todos los activos nuevos.
  - M2a y N1 se diseñaron sobre SPX, WTI y gas, donde funcionaban, y fuera de ellos se derrumban. Eran sobreajuste a esos activos.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE3_PROTOCOL.md`, commiteado antes de cargar los activos (`ba88fbb9`). Código congelado en `8e6b82e0`.

**N:** sigue en 81. **Corridas Jesse:** 0 de 10.

## A. Motor × activo (Sharpe común / larga)

| Activo | Clase | R1 | R2 | R3 | M2a | N1 |
|---|---|---|---|---|---|---|
| Plata | metales | **0,39 / 0,30** | 0,30 / 0,38 | **0,62 / 0,41** | −0,66 / −0,47 ✗ | −0,72 / −0,49 ✗ |
| Cobre | metales | **0,30 / 0,28** | 0,32 / −0,13 | 0,29 / −0,32 | −0,85 / −0,29 ✗ | −0,93 / −0,56 ✗ |
| Nasdaq 100 | acciones | **0,77 / 0,74** | −0,07 / 0,38 | −0,07 / 0,22 | 0,42 / 0,25 | 0,30 / 0,24 |
| EWJ (1D) | acciones | −0,18 / 0,12 | n/a | n/a | −0,48 / −0,50 | −0,80 / −0,56 ✗ |
| EWY (1D) | acciones | 0,22 / 0,34 | n/a | n/a | −0,56 / −0,29 ✗ | −0,61 / −0,30 ✗ |

✗ = derrumbe (Sharpe < −0,5 o DD < −30% en la común).

**Por familia, Sharpe > 0 en la ventana común:**

| Familia | Positivos | Fracción |
|---|---|---|
| Tendencia (R1, R2, R3) | 10 de 13 | 77% |
| Reversión (M2a, N1) | 2 de 10 | 20% |

**Notas:**
- EWJ y EWY tienen solo velas diarias: R1 corre en diario (adaptación declarada) y R2/R3 no aplican.
- Las mismas reglas en el núcleo daban M2a 0,88 en SPX y N1 0,61 en WTI. La caída fuera de muestra es grande y consistente.

## B. Regla de clase (C0 congelado)

| Activo | Regla | Sharpe común | DD común |
|---|---|---|---|
| Plata | R1 | 0,39 ✓ | −18,8% |
| Cobre | R1 | 0,30 ✓ | −19,1% |
| Nasdaq | R1 + M2a | 0,78 ✓ | −7,3% |
| EWJ | R1 + M2a | **−0,34 ✗** | −20,5% |
| EWY | R1 + M2a | **−0,01 ✗** | −21,6% |
| Canasta de las 5 | — | 0,41 (larga 0,34) | −8,8% |

La regla de acciones falla por su mitad de reversión (M2a). En EWJ y EWY, R1 solo da −0,18 / 0,22 en la común y 0,12 / 0,34 en la larga.

## C. Diagnóstico de cartera (no es puerta)
La cartera F2 (C0 + C6), sumando a C0 las 5 mangas de clase de validación y con la misma construcción:

| | CAGR | DD | Sharpe | Meses + | Trim. + | DSR |
|---|---|---|---|---|---|---|
| Común, con validación | 28,3% | −14,0% | 1,57 | 56% | 70% | 0,86 |
| Común, F2 original | 34,2% | −14,5% | 1,81 | 56% | 75% | 0,96 |
| Larga (2018-09+), con validación | 35,7% | −15,8% | 1,62 | 60% | 80% | 0,99 |

Agregar los activos nuevos baja el Sharpe de 1,81 a 1,57 y los trimestres positivos de 75% a 70%. La cartera sigue siendo rentable porque su núcleo de riesgo (cripto y tendencia) no cambia.

## Conclusiones
1. **La reversión de corto plazo (M2a, N1) queda refutada como regla «todo terreno».** Su éxito en el núcleo era específico de esos activos.
2. **La tendencia (R1) y las rupturas (R2, R3) sí muestran generalidad:**
   - R1 es positivo en 4 de 5 activos nuevos y en 5 de 5 en la ventana larga;
   - R3 es positivo en 3 de 3 en la común.
3. **La cartera F2 sobreestimaba su robustez,** porque C0 incluía reversión elegida mirando el núcleo. La parte que generaliza (tendencia y rupturas, sobre todo en cripto) es la que sostiene el resultado.
4. **Por protocolo no se re-ajusta:**
   - quitar la reversión de C0 ahora sería una decisión mirando la validación;
   - los activos de validación ya fueron vistos, así que una cartera nueva «solo tendencia» no podría validarse en ellos. Necesitaría activos o períodos nuevos, por ejemplo 2026, hoy reservado.

## Opciones para el usuario
- **a)** Cerrar r50 con este diagnóstico: la tendencia/ruptura generaliza, la reversión no, y la cartera C0 + C6 no pasó la validación.
- **b)** Construir una cartera solo de tendencia (R1 + rupturas cripto). Suma a N y queda sin validación independiente, salvo que autorices:
  - usar 2026 como prueba fuera de muestra (hoy reservado);
  - o validar en otros activos nuevos.
- **c)** Ir a F4 (Jesse) solo para confirmar los fills de las mangas que sí generalizan (C6 cripto y R1). Sería un control técnico, no una validación.
