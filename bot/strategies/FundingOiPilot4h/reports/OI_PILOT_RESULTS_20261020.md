# OI microvalidación final y diagnóstico de interrupción —2026-10-20
## Estado
Las cuatro ejecuciones C/D terminaron; el timeout de arranque no implicó fallo del proceso de backtest. Se verificaron estados antes de repetir: las dos sesiones2022 ya estaban finished y no se duplicaron; las dos2023 eran draft y se ejecutaron ahora. Sesiones originales con assert value>0 fallidas preservadas; dos drafts antiguos de2023 no ejecutados también preservados. Cuatro sesiones económicas finales, dos errores técnicos previos.
No hay logs del backend expuestos por este MCP que permitan atribuir la demora a CPU, memoria, bloqueo o red. La evidencia disponible es cliente Read timed out10s y posteriores estados finished sin excepción; no se afirma causa raíz del timeout ni se cambió timeout/reinició servicio.

## Validación y resultados
A=referencia; B=referencia+funding; C=referencia+OI; D=referencia+funding+OI. Todas pagan funding y fees; sólo B/D usan funding como filtro.
Ventanas enero-junio2022 y enero-junio2023, ya vistas antes: exploración, no OOS nuevo ni promoción walk-forward. Capital10000 por sesión.
| Variante | Neto2022 % | DD2022 % | Trades2022 | Neto2023 % | DD2023 % | Trades2023 |
|---|---:|---:|---:|---:|---:|---:|
| A | -10.94 | -20.77 | 93 | 20.32 | -17.38 | 85 |
| B | -6.23 | -17.32 | 91 | 19.80 | -17.38 | 82 |
| C | 8.92 | -8.44 | 59 | 11.94 | -12.37 | 56 |
| D | 11.40 | -8.23 | 58 | 7.30 | -15.29 | 54 |

OI mejora2022 y reduce drawdown de C frente a A en ambos tramos, pero reduce retorno2023. D no domina a C: mayor retorno2022 pero menor2023 y peor drawdown2023. PF2022 C1.142/D1.184 no supera1.2. No hay prueba suficiente de ventaja robusta ni autorización live. No sumar retornos ni usar estos dos semestres como aprobación; mayor reducción de exposición explica parte posible del cambio de DD.
45 tests de OI aprobados antes del piloto. Aserciones de lag/antigüedad corrieron en callbacks sin excepción en las cuatro sesiones finales. Snapshots confirman OI aplicado, lag6m y stale10m. Análisis MCP d03d03ccb6884b43a1ccd1087d80a24c reconcilia trade/ledger/fees/balance en las ocho sesiones comparadas; error por trade0. Sin2026, ML, órdenes, live/paper.

## Ceros, huecos e impacto
Son categorías distintas: una observación publicada con cantidad0 existe en el archivo; una observación ausente no existe. No se interpreta cero como desaparición real de todo el OI, ni se reemplaza un hueco por cero. El importador conserva ceros no negativos; este filtro trata cero como referencia inválida.
Biblioteca completa sep2020-dic2025:560390/561024 observaciones,634 ausentes,156huecos, mayor intervalo entre etiquetas37800000ms. Son estadísticas globales del dataset, no conteos de barras del piloto.
2022:1086 decisiones4h por variante,1086 observaciones visibles,0None,3ceros.2023:1086decisiones por variante,0None,0ceros. Esta lectura4h no demuestra ausencia de huecos en la serie5m.
En2022 hubo1 oportunidad bloqueada por referencia inválida/inicialización por variante; en2023 hubo0. El contador blocked_missing agrupa primera24h, cero actual, cero de referencia o dato ausente; no permite atribuir ese único bloqueo exclusivamente a cero. Los ceros pueden afectar una evaluación actual o la comparación24h posterior, aunque no haya señal de precio en ese momento.
No bloquearon stops/salidas ni funding/velas. Se conserva historial y no se interpola; si una entrada exige OI actual o referencia24h válidos, se omite esa entrada hasta disponer de ambos. No se usa automáticamente una estrategia alternativa cuando falta OI.
La condición OI creciente bloqueó82/75 oportunidades2022 C/D y76/70en2023: son decisiones de señal, no errores de datos, y los contadores dependen del estado de posiciones de cada variante.
La cobertura de archivos retrospectivos y el lag label+6m son supuestos explícitos, no certificación point-in-time original. Marcas de funding del piloto son proxy horario, importes aproximados. Sin slippage independiente.
No se inventarán datos de enero-agosto2020 ni se comprará proveedor sin autorización; ventana común ya comienza septiembre2020. Antes de research amplio debe auditarse cobertura/no-ceros y medir sensibilidad a la política de huecos, sin borrar selectivamente períodos perdedores.

## Política para próximas features
Cada feature nueva se incluye en pruebas técnicas y comparación por ablación con y sin ella; no se obliga a incorporarla a la estrategia final. Elegir reglas/ventanas antes de resultados, distinguir costes de señales y reportar datos no disponibles. No rescatar este piloto ajustando umbrales con estos resultados.

## Logs de auditoría
```json
[
  {
    "url": "http://localhost:9200/#/backtest/e520a85a-2da4-4c7e-bca0-876eaf0aed6b",
    "items": [
      "[INFO | 2022-06-29T20:00:00] cancel all remaining orders of BTC-USDT to prepare for a fresh start...",
      "[INFO | 2022-06-30T00:01:00] Saved daily portfolio balance: 10892.27",
      "[INFO | 2022-07-01T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2022-07-01T00:00:00] OI_PILOT_AUDIT {\"bars\": 1086, \"blocked_missing\": 1, \"blocked_nonrising\": 82, \"eligible_before_oi\": 142, \"missing\": 0, \"observed\": 1086, \"passed\": 59, \"zero_values\": 3}",
      "[INFO | 2022-07-01T00:00:00] PILOT_AUDIT {\"adverse_blocks\": 0, \"bars\": 1086, \"entries\": 59, \"price_opportunities\": 142, \"unavailable_blocks\": 0}",
      "[INFO | 2022-07-01T00:00:00] Saved daily portfolio balance: 10892.27"
    ]
  },
  {
    "url": "http://localhost:9200/#/backtest/b55b776b-1c7b-4d46-9e02-d0289abb626a",
    "items": [
      "[INFO | 2022-06-29T20:00:00] cancel all remaining orders of BTC-USDT to prepare for a fresh start...",
      "[INFO | 2022-06-30T00:01:00] Saved daily portfolio balance: 11140.02",
      "[INFO | 2022-07-01T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2022-07-01T00:00:00] OI_PILOT_AUDIT {\"bars\": 1086, \"blocked_missing\": 1, \"blocked_nonrising\": 75, \"eligible_before_oi\": 134, \"missing\": 0, \"observed\": 1086, \"passed\": 58, \"zero_values\": 3}",
      "[INFO | 2022-07-01T00:00:00] PILOT_AUDIT {\"adverse_blocks\": 8, \"bars\": 1086, \"entries\": 58, \"price_opportunities\": 143, \"unavailable_blocks\": 1}",
      "[INFO | 2022-07-01T00:00:00] Saved daily portfolio balance: 11140.02"
    ]
  },
  {
    "url": "http://localhost:9200/#/backtest/3b1e599e-c393-4305-8c18-a1d603f9e638",
    "items": [
      "Net PnL: -228.45 USDT (-6.27%) | Fees: 9.74 USDT",
      "[INFO | 2023-06-30T13:39:00] cancel all remaining orders of BTC-USDT to prepare for a fresh start...",
      "[INFO | 2023-07-01T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2023-07-01T00:00:00] OI_PILOT_AUDIT {\"bars\": 1086, \"blocked_missing\": 0, \"blocked_nonrising\": 76, \"eligible_before_oi\": 132, \"missing\": 0, \"observed\": 1086, \"passed\": 56, \"zero_values\": 0}",
      "[INFO | 2023-07-01T00:00:00] PILOT_AUDIT {\"adverse_blocks\": 0, \"bars\": 1086, \"entries\": 56, \"price_opportunities\": 132, \"unavailable_blocks\": 0}",
      "[INFO | 2023-07-01T00:00:00] Saved daily portfolio balance: 11194.09"
    ]
  },
  {
    "url": "http://localhost:9200/#/backtest/ea8fc49b-0e12-4886-82eb-7ad1a6b105e7",
    "items": [
      "Net PnL: -218.98 USDT (-6.27%) | Fees: 9.33 USDT",
      "[INFO | 2023-06-30T13:39:00] cancel all remaining orders of BTC-USDT to prepare for a fresh start...",
      "[INFO | 2023-07-01T00:00:00] Terminating BTC-USDT...",
      "[INFO | 2023-07-01T00:00:00] OI_PILOT_AUDIT {\"bars\": 1086, \"blocked_missing\": 0, \"blocked_nonrising\": 70, \"eligible_before_oi\": 124, \"missing\": 0, \"observed\": 1086, \"passed\": 54, \"zero_values\": 0}",
      "[INFO | 2023-07-01T00:00:00] PILOT_AUDIT {\"adverse_blocks\": 7, \"bars\": 1086, \"entries\": 54, \"price_opportunities\": 136, \"unavailable_blocks\": 5}",
      "[INFO | 2023-07-01T00:00:00] Saved daily portfolio balance: 10729.99"
    ]
  }
]
```

## Resultados completos
```json
{
  "rows": [
    {
      "name": "F1VALA",
      "id": "be672318-6c15-451c-82a2-b73ed03aae9e",
      "url": null,
      "trades": 93,
      "net_pct": -10.94442032459641,
      "pf": 0.8836627462659472,
      "dd": -20.772017128420362,
      "sharpe": -0.5316383853072065,
      "gross_price": -380.19342023868455,
      "fees": 700.3356315021208,
      "funding": -13.91298071883538,
      "net": -1094.4420324596422,
      "funding_events": 132,
      "proxy_events": 132,
      "max_reconciliation_error": 0,
      "directions": {
        "short": {
          "trades": 55,
          "gross": 849.1955759070488,
          "fees": 415.34608368292675,
          "funding": 14.687773139053423,
          "net": 448.5372653631755
        },
        "long": {
          "trades": 38,
          "gross": -1229.388996145734,
          "fees": 284.98954781919434,
          "funding": -28.600753857888805,
          "net": -1542.9792978228168
        }
      },
      "eligible": false
    },
    {
      "name": "F1VALB",
      "id": "07277a56-c5af-472d-94cb-4c7cde645121",
      "url": null,
      "trades": 91,
      "net_pct": -6.231561761327953,
      "pf": 0.932918161379094,
      "dd": -17.316246071631358,
      "sharpe": -0.2257972414576569,
      "gross_price": 103.4656961265693,
      "fees": 711.9419502481097,
      "funding": -14.679922011255597,
      "net": -623.1561761327953,
      "funding_events": 132,
      "proxy_events": 132,
      "max_reconciliation_error": 0,
      "directions": {
        "short": {
          "trades": 53,
          "gross": 1371.443614951952,
          "fees": 415.29935791698017,
          "funding": 15.178971230431477,
          "net": 971.323228265403
        },
        "long": {
          "trades": 38,
          "gross": -1267.9779188253822,
          "fees": 296.64259233112983,
          "funding": -29.858893241687078,
          "net": -1594.479404398199
        }
      },
      "eligible": false
    },
    {
      "name": "F1VALC",
      "id": "e520a85a-2da4-4c7e-bca0-876eaf0aed6b",
      "url": null,
      "trades": 59,
      "net_pct": 8.922709596086582,
      "pf": 1.1417465005354768,
      "dd": -8.440659642267468,
      "sharpe": 0.7605946130472615,
      "gross_price": 1434.7033690907786,
      "fees": 534.7920857039071,
      "funding": -7.640323778212991,
      "net": 892.270959608658,
      "funding_events": 91,
      "proxy_events": 91,
      "max_reconciliation_error": 0,
      "directions": {
        "short": {
          "trades": 33,
          "gross": 1629.218624001262,
          "fees": 298.9008819023401,
          "funding": 20.21918076559228,
          "net": 1350.5369228645134
        },
        "long": {
          "trades": 26,
          "gross": -194.51525491048363,
          "fees": 235.891203801567,
          "funding": -27.85950454380526,
          "net": -458.2659632558559
        }
      },
      "eligible": false
    },
    {
      "name": "F1VALD",
      "id": "b55b776b-1c7b-4d46-9e02-d0289abb626a",
      "url": null,
      "trades": 58,
      "net_pct": 11.400233956459926,
      "pf": 1.1840928041841576,
      "dd": -8.23091591683709,
      "sharpe": 0.9289213352826722,
      "gross_price": 1684.7239811229902,
      "fees": 536.8306120342154,
      "funding": -7.869973442782157,
      "net": 1140.0233956459927,
      "funding_events": 91,
      "proxy_events": 91,
      "max_reconciliation_error": 0,
      "directions": {
        "short": {
          "trades": 32,
          "gross": 1883.6670103235253,
          "fees": 295.9271698535864,
          "funding": 20.59530312149535,
          "net": 1608.335143591434
        },
        "long": {
          "trades": 26,
          "gross": -198.94302920053505,
          "fees": 240.90344218062887,
          "funding": -28.46527656427749,
          "net": -468.31174794544137
        }
      },
      "eligible": false
    },
    {
      "name": "F2VALA",
      "id": "fd99bf7c-ff49-4b92-a8bf-4a3bb5b042c4",
      "url": null,
      "trades": 85,
      "net_pct": 20.32481024938302,
      "pf": 1.2531034261743548,
      "dd": -17.382653180633735,
      "sharpe": 1.4475037127647217,
      "gross_price": 2906.950078796026,
      "fees": 849.7949004014007,
      "funding": -24.674153456325346,
      "net": 2032.481024938302,
      "funding_events": 178,
      "proxy_events": 178,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 53,
          "gross": 2688.966083522441,
          "fees": 530.2473724835164,
          "funding": -77.08273784944384,
          "net": 2081.6359731894822
        },
        "short": {
          "trades": 32,
          "gross": 217.98399527358592,
          "fees": 319.5475279178843,
          "funding": 52.40858439311851,
          "net": -49.15494825117986
        }
      },
      "eligible": true
    },
    {
      "name": "F2VALB",
      "id": "ff99feb0-75b6-4490-8e71-ad2ff51a6885",
      "url": null,
      "trades": 82,
      "net_pct": 19.79936881015903,
      "pf": 1.2558827801228285,
      "dd": -17.38265320849468,
      "sharpe": 1.4385007044840508,
      "gross_price": 2830.7844512757515,
      "fees": 818.9612899040997,
      "funding": -31.886280355747587,
      "net": 1979.9368810159024,
      "funding_events": 168,
      "proxy_events": 168,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 53,
          "gross": 2693.4791106817274,
          "fees": 528.8370245223417,
          "funding": -76.97702588583755,
          "net": 2087.665060273547
        },
        "short": {
          "trades": 29,
          "gross": 137.30534059402402,
          "fees": 290.124265381758,
          "funding": 45.09074553008997,
          "net": -107.72817925764402
        }
      },
      "eligible": true
    },
    {
      "name": "F2VALC",
      "id": "3b1e599e-c393-4305-8c18-a1d603f9e638",
      "url": null,
      "trades": 56,
      "net_pct": 11.940916093886893,
      "pf": 1.2415890733982684,
      "dd": -12.372376759584524,
      "sharpe": 1.0947471567150149,
      "gross_price": 1738.1443686302882,
      "fees": 525.418230623422,
      "funding": -18.634528618176727,
      "net": 1194.0916093886894,
      "funding_events": 118,
      "proxy_events": 118,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 37,
          "gross": 1240.4298663757415,
          "fees": 349.58841248109945,
          "funding": -48.74700513864054,
          "net": 842.0944487560015
        },
        "short": {
          "trades": 19,
          "gross": 497.71450225454646,
          "fees": 175.8298181423226,
          "funding": 30.112476520463808,
          "net": 351.9971606326877
        }
      },
      "eligible": true
    },
    {
      "name": "F2VALD",
      "id": "ea8fc49b-0e12-4886-82eb-7ad1a6b105e7",
      "url": null,
      "trades": 54,
      "net_pct": 7.299922355594002,
      "pf": 1.150569367900105,
      "dd": -15.287561311665554,
      "sharpe": 0.7354939594668194,
      "gross_price": 1251.5120732335672,
      "fees": 498.4047585667698,
      "funding": -23.115079107398056,
      "net": 729.9922355593997,
      "funding_events": 112,
      "proxy_events": 112,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 37,
          "gross": 1244.6907738781488,
          "fees": 343.5620763852757,
          "funding": -47.900384429093506,
          "net": 853.22831306378
        },
        "short": {
          "trades": 17,
          "gross": 6.821299355417871,
          "fees": 154.84268218149384,
          "funding": 24.78530532169546,
          "net": -123.23607750438045
        }
      },
      "eligible": false
    }
  ],
  "development_selection": "Not performed: exploratory ablation on previously viewed validation windows",
  "note": "Validation of unselected variants is diagnostic A/B, not selected-strategy WF performance."
}
```
