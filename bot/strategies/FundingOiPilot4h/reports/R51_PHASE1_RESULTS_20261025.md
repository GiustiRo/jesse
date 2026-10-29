# r51 F1: confirmación de P1 en Jesse (2026-10-25)

**Resultado:** P1 se confirma en Jesse. Pasan la tolerancia 10 de las 11 mangas. La que falla es R1 en el bono:
- el arnés es más optimista que Jesse (Sharpe −1,29 contra −1,44 en reproducción minuto a minuto);
- la causa es el feed muy disperso del CFD del bono;
- por regla gana Jesse, y desde la F2 la curva de R1/bono en la ventana común se toma de Jesse.

No cambia el signo de ninguna manga, así que r51 sigue.

**Conteo**
- Corridas Jesse: 10 de 10. Nueve de confirmación y la de reserva, usada para diagnosticar el bono.
- No suma a N, que sigue en 98.
- Protocolo: `RESEARCH_HUB/revisions/20261025-r51/PROTOCOL_R51.md`, sección F1, commiteado en `8ac56348` antes de correr.

## Configuración
- Ventana 2020-10-15 → 2026-01-01; fee 0,00045; aislado. R1 a 3x y R2/R3 a 5x. Una manga por sesión.
- R1 usa las clases r49 sin cambios:
  - `R49NullDonchianEnsBtc` para BTC, ETH y oro;
  - `R49NullDonchianEnsSpy` para SPX;
  - `R49NullDonchianEnsWti` para WTI, gas y bono.
- R2 y R3 son estrategias nuevas, `R51C6R2` y `R51C6R3`: copia literal de `r50_f1b.r2_r3_decider`.
- Funding real en los perpetuos: BTC `0ab14bc2…` y ETH `22bd891c…`.
- R1 en BTC y en WTI se compararon con sesiones existentes, sin gastar corridas.
- El arnés corre con los costos de Jesse (sin slippage y un solo fee). Es la corrida contra la que se aplica la tolerancia.

## Tabla arnés contra Jesse (curva diaria)
Tolerancia: |ΔSharpe| ≤ 0,10, |ΔCAGR| ≤ 1 pp, |ΔDD| ≤ 1 pp.

| Manga | Sesión Jesse | Sharpe arnés | Sharpe Jesse | CAGR arnés | CAGR Jesse | DD arnés | DD Jesse | Trades (arnés / Jesse) | Pasa |
|---|---|---|---|---|---|---|---|---|---|
| R1 BTC | [b4792187](http://localhost:9200/#/backtest/b4792187-8847-450d-9f52-320edb4a61dd) | 1,041 | 1,040 | 12,90% | 12,90% | −11,8% | −11,9% | 11 / 11 | sí |
| R1 ETH | [88349011](http://localhost:9200/#/backtest/88349011-dd9b-432f-a381-90fedf1dd7ef) | 0,602 | 0,603 | 6,32% | 6,31% | −16,4% | −16,3% | 12 / 13 | sí |
| R1 oro | [5663eced](http://localhost:9200/#/backtest/5663eced-0a44-4bbc-b6f0-6c7757c25f53) | 1,484 | 1,492 | 13,99% | 13,98% | −10,4% | −10,9% | 10 / 10 | sí |
| R1 SPX | [66ad8b9c](http://localhost:9200/#/backtest/66ad8b9c-683f-4088-b450-c413c9fba88b) | 1,021 | 1,019 | 10,04% | 9,99% | −13,6% | −14,2% | 7 / 7 | sí |
| R1 WTI | [063c2564](http://localhost:9200/#/backtest/063c2564-80c9-4e19-9b64-4add88e660a0) | 0,104 | 0,056 | 0,36% | −0,02% | −28,5% | −28,4% | 12 / 13 | sí |
| R1 gas | [8c9cf609](http://localhost:9200/#/backtest/8c9cf609-05c0-4945-ad6b-aa5086e60183) | 0,299 | 0,317 | 2,05% | 2,24% | −23,0% | −23,4% | 14 / 15 | sí |
| R1 bono (rápido) | [1ad8071b](http://localhost:9200/#/backtest/1ad8071b-8f11-4a0f-9211-2891e087ab1d) | −1,322 | −1,501 | −5,18% | −5,69% | −26,4% | −28,2% | 20 / 20 | **no** |
| R1 bono (minuto a minuto) | [42cdf4a0](http://localhost:9200/#/backtest/42cdf4a0-7b6b-4af1-9862-da3396821812) | −1,286 | −1,439 | −5,18% | −5,69% | −26,4% | −28,2% | 20 / 20 | **no** |
| R2 BTC | [4324b19d](http://localhost:9200/#/backtest/4324b19d-24df-4a5d-b22d-59c4a689b94c) | 1,223 | 1,225 | 9,38% | 9,41% | −5,1% | −5,1% | 39 / 39 | sí |
| R2 ETH | [53d66160](http://localhost:9200/#/backtest/53d66160-5393-4d94-8f43-a1a9d643b506) | 1,207 | 1,205 | 9,17% | 9,19% | −6,3% | −6,3% | 36 / 36 | sí |
| R3 BTC | [14fd70de](http://localhost:9200/#/backtest/14fd70de-d056-42f2-a5c6-0f6e9d97dc61) | 1,016 | 1,012 | 7,07% | 7,07% | −7,3% | −7,3% | 31 / 31 | sí |
| R3 ETH | [575f5766](http://localhost:9200/#/backtest/575f5766-7831-4489-9015-e9c21d671532) | 1,112 | 1,105 | 8,20% | 8,20% | −5,5% | −5,5% | 30 / 30 | sí |

Notas de la tabla:
- El Sharpe del bono en el arnés cambia entre las dos filas porque Jesse muestrea la curva en otro horario (00:01 contra 04:00).
- Con los costos del protocolo (slippage del bono y del gas, 5 bp en los stops, maker 0,018% en R3), el arnés queda a menos de 0,03 de Sharpe de estas cifras en todas las mangas.

## Diagnóstico del bono
- El CFD USTBOND de Dukascopy tiene ~10 minutos con datos por hora. WTI y gas tienen ~50–60.
- Con un feed tan disperso, Jesse arma las velas de 4h y decide en otros horarios que el arnés:
  - 12 de 75 órdenes se corren entre 4 h y 6 semanas;
  - la mayor diferencia está en 2025-09 → 10: el arnés entra el 05-09 y Jesse recién el 16-10.
- La reproducción minuto a minuto (`fast_mode=false`) da lo mismo, así que no es un efecto del modo rápido.

**Corrección aplicada**, según la regla del protocolo («gana Jesse»):
- En la ventana común, la curva de R1/bono de P1 se toma de la sesión Jesse `42cdf4a0`.
- La lente larga de P1 no incluye el bono, así que no cambia.
- El efecto sobre P1 es menor: el bono pesa 1/7 de la canasta R1 y la diferencia es de 0,5 pp de CAGR. La F2 lo recalcula.

**Consecuencia para las reglas nuevas del bono (A1, A2, A4):**
- Usan barras diarias, que el feed disperso afecta menos que las de 4h.
- Siguen siendo solo del arnés. Se declara que el arnés puede ser optimista en el bono.
- Los perpetuos TMF y TBT operan 24/7, así que en operación real las barras no tendrían estos huecos.

## Archivos
- Script: `research_scripts/r51_f1_confirm.py`.
- Resultados: `research_scripts/data/r51/f1_confirm.json`.
- Estrategias: `strategies/R51C6R2` y `strategies/R51C6R3`.

## Siguiente paso
F2, el diagnóstico de los trimestres negativos de P1, con la curva Jesse del bono. No suma a N.
