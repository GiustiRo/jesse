# Microvalidación funding + walk-forward: resultado
Fecha2026-10-20. Ocho backtests por MCP terminados; 10000USDT iniciales en cada sesión. Sin ML, sin OI como señal, sin consultar/backtestear2026 en este piloto.

## Conclusión
Validación técnica de este recorrido histórico: aprobada con límites explícitos. No acredita todo el live ni robustez económica.
Resultado económico: sin candidata elegible en ninguno de los dos desarrollos, decisión guardada antes de lanzar validaciones en FUNDING_WF_PILOT_SELECTION_20261020.md. No se seleccionó ninguna estrategia. Por ello las validaciones son diagnósticos A/B, no performance de una estrategia seleccionada walk-forward.
El filtro mejora enero-junio2022 (+4.71puntos porcentuales) pero sigue perdiendo; enero-junio2023 empeora ligeramente (-0.53puntos). También empeoró ambos desarrollos. No hay evidencia de ventaja estable de este filtro ni justificación para promoverlo.
La referencia mecánica es un control de plumbing; no replica el modelo legacy ni pretende capturar toda la información que usaba.

## Resultados
A=precio; B=mismo código+gate settled funding. Fees y funding ON en ambas.
F1DEV=sep2020-dic2021; F2DEV=sep2020-dic2022; F1VAL=ene-jun2022; F2VAL=ene-jun2023.
| Tramo | Trades | Neto % | PF | DD % | Precio bruto USDT | Fees USDT | Funding USDT |
|---|---:|---:|---:|---:|---:|---:|---:|
| F1DEVA | 284 | -28.63 | 0.907 | -42.72 | -79.12 | 2310.65 | -473.49 |
| F1DEVB | 277 | -36.00 | 0.873 | -45.25 | -1057.41 | 2101.02 | -441.55 |
| F1VALA | 93 | -10.94 | 0.884 | -20.77 | -380.19 | 700.34 | -13.91 |
| F1VALB | 91 | -6.23 | 0.933 | -17.32 | 103.47 | 711.94 | -14.68 |
| F2DEVA | 473 | -43.40 | 0.898 | -61.60 | -576.64 | 3276.95 | -486.03 |
| F2DEVB | 463 | -48.48 | 0.876 | -61.35 | -1405.53 | 2989.13 | -453.44 |
| F2VALA | 85 | 20.32 | 1.253 | -17.38 | 2906.95 | 849.79 | -24.67 |
| F2VALB | 82 | 19.80 | 1.256 | -17.38 | 2830.78 | 818.96 | -31.89 |

Los desarrollos se solapan y F1VAL luego integra F2DEV como corresponde a expansión cronológica; no sumar sus retornos ni tratar ocho sesiones como muestras independientes. La etiqueta eligible en el JSON de validación es sólo evaluación descriptiva de umbrales: NO altera la selección previa.

## Auditoría
Análisis MCP a360d6fbd8c04c2ab37a060969136100 (snapshot completo de las ocho sesiones).
Se verificó en cada sesión:
- finish<=2025, OI disabled; dataset funding fijado y reglas inalteradas.
- PNL trade=precio bruto-fees+funding; suma trades=net_profit=cambio de balance.
- suma ledger por trade=funding del trade; suma fees=métrica fee; suma funding=métrica cashflow.
- cashflow=-qty firmada*mark_price*rate_decimal.
- cada cargo corresponde a un trade ya abierto antes del effective_at y cerrado en/tras éste.
- error por trade observado0; tolerancia contable de asserts1e-6USDT para redondeo de coma flotante, no tolerancia económica.
- comprobaciones causales internas de eventos available_at<=reloj y rango UTC previo ejecutadas sin excepción.
- cálculo independiente del sizing stop+dos comisiones <=2% para largos/cortos confee0.00045y0.0009; tasas iguales detectadas por ptp.
A/B tienen una sola diferencia de lógica, FUNDING_FILTER. El número de trades cambia, por lo que exposición, compounding y fees también pueden cambiar.
El funding histórico fuerza replay1m (effective_fast_mode=false), decisiones4h.

## Límites
Todos los cargos de funding de estas ocho ventanas usan markPriceKlines.1h_open_proxy como aproximación explícita del precio de liquidación: cada conteo proxy_events coincide con funding_events en JSON. Las tasas son settled, pero los importes no son exactos al precio de liquidación. No ocultar ni confundir cobertura completa de tasas con exactitud de marcas.
Sin slippage independiente ni estrés de ejecución; stop+fees presupuestados2% no limita funding/slippage adicional.
Los contadores PILOT_AUDIT no quedaron disponibles: debug_mode=false y MCP no conserva archivo de logs en estas sesiones; infoLogs vacío. Por tanto no se informa número causal exacto de bloqueos por extremos versus varianza nula, ni se deduce de diferencia de trades. Mejorar persistencia de auditoría antes de research masivo.
MCP section=funding devolvió un falso http_error con HTTP200/status=applied: el backend sí entrega ledger; se usaron snapshots completos independientes de ese wrapper para reconciliar. Corrección puntual del wrapper en revisión, sin alterar resultados ni reiniciar el servidor.
No hubo pruebas live/paper en este piloto ni se conectaron cuentas.

## Próximo bloque recomendado
Preparar hipótesis simples basadas en features causales verificadas del legacy (funding relativo/cambio/persistencia) sin trasladar su ventaja ML como demostrada. Una familia por vez; señal precio, filtro y eventualmente OI se comparan por ablación. Fijar ventanas, presupuesto de intentos y criterios antes de iterar; mejorar auditoría persistente y estrés de fricción antes de promover candidatas. Mantener2026 fuera de la iteración. No modificar este gate para rescatar estos resultados.

## Sesiones
- [F1DEVA](http://localhost:9200/#/backtest/ec889b8f-d80e-4a05-8211-8e749ce391cf)
- [F1DEVB](http://localhost:9200/#/backtest/46ed012c-37a4-4fec-a18b-cde4e45c6fc6)
- [F2DEVA](http://localhost:9200/#/backtest/20c520fb-c95a-4088-9faf-bd9329c80d41)
- [F2DEVB](http://localhost:9200/#/backtest/c5ce161f-e9f7-437a-96de-65a47a436342)
- [F1VALA](http://localhost:9200/#/backtest/be672318-6c15-451c-82a2-b73ed03aae9e)
- [F1VALB](http://localhost:9200/#/backtest/07277a56-c5af-472d-94cb-4c7cde645121)
- [F2VALA](http://localhost:9200/#/backtest/fd99bf7c-ff49-4b92-a8bf-4a3bb5b042c4)
- [F2VALB](http://localhost:9200/#/backtest/ff99feb0-75b6-4490-8e71-ad2ff51a6885)

## Resultados completos y reparto long/short
```json
{
  "rows": [
    {
      "name": "F1DEVA",
      "id": "ec889b8f-d80e-4a05-8211-8e749ce391cf",
      "url": null,
      "trades": 284,
      "net_pct": -28.63253934227886,
      "pf": 0.9067001412450454,
      "dd": -42.718124250199786,
      "sharpe": -0.5310804273775871,
      "gross_price": -79.11610271198262,
      "fees": 2310.6479019426765,
      "funding": -473.4899295732259,
      "net": -2863.2539342278883,
      "funding_events": 421,
      "proxy_events": 421,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 163,
          "gross": 1741.1583534379674,
          "fees": 1352.6865429039415,
          "funding": -630.0215547220477,
          "net": -241.54974418802271
        },
        "short": {
          "trades": 121,
          "gross": -1820.274456149951,
          "fees": 957.9613590387346,
          "funding": 156.53162514882158,
          "net": -2621.704190039865
        }
      },
      "eligible": false
    },
    {
      "name": "F1DEVB",
      "id": "46ed012c-37a4-4fec-a18b-cde4e45c6fc6",
      "url": null,
      "trades": 277,
      "net_pct": -35.999847458224785,
      "pf": 0.873383717623907,
      "dd": -45.252507574734025,
      "sharpe": -0.7932108717956171,
      "gross_price": -1057.4126011679216,
      "fees": 2101.0216560149806,
      "funding": -441.5504886395763,
      "net": -3599.9847458224795,
      "funding_events": 412,
      "proxy_events": 412,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 158,
          "gross": 946.1738209897595,
          "fees": 1221.7345376762203,
          "funding": -585.9806410725049,
          "net": -861.5413577589682
        },
        "short": {
          "trades": 119,
          "gross": -2003.5864221576805,
          "fees": 879.2871183387592,
          "funding": 144.4301524329286,
          "net": -2738.4433880635106
        }
      },
      "eligible": false
    },
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
      "name": "F2DEVA",
      "id": "20c520fb-c95a-4088-9faf-bd9329c80d41",
      "url": null,
      "trades": 473,
      "net_pct": -43.396297145361906,
      "pf": 0.8980333917748814,
      "dd": -61.59508547456305,
      "sharpe": -0.5532940079403438,
      "gross_price": -576.6432569788127,
      "fees": 3276.9525013324314,
      "funding": -486.0339562249466,
      "net": -4339.629714536195,
      "funding_events": 739,
      "proxy_events": 739,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 248,
          "gross": 146.0860740824686,
          "fees": 1787.6642031016702,
          "funding": -675.2564973720704,
          "net": -2316.834626391273
        },
        "short": {
          "trades": 225,
          "gross": -722.7293310612828,
          "fees": 1489.2882982307585,
          "funding": 189.2225411471227,
          "net": -2022.7950881449187
        }
      },
      "eligible": false
    },
    {
      "name": "F2DEVB",
      "id": "c5ce161f-e9f7-437a-96de-65a47a436342",
      "url": null,
      "trades": 463,
      "net_pct": -48.480974164267764,
      "pf": 0.876378986451595,
      "dd": -61.351792363467396,
      "sharpe": -0.696045412494213,
      "gross_price": -1405.5310424599988,
      "fees": 2989.1283745225746,
      "funding": -453.4379994442003,
      "net": -4848.097416426776,
      "funding_events": 730,
      "proxy_events": 730,
      "max_reconciliation_error": 0,
      "directions": {
        "long": {
          "trades": 243,
          "gross": -545.8838561039906,
          "fees": 1628.7530593787944,
          "funding": -628.3247682288572,
          "net": -2802.9616837116437
        },
        "short": {
          "trades": 220,
          "gross": -859.647186356009,
          "fees": 1360.3753151437795,
          "funding": 174.8867687846562,
          "net": -2045.1357327151322
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
    }
  ],
  "development_selection": {
    "F1": "SIN_CANDIDATA",
    "F2": "SIN_CANDIDATA"
  },
  "note": "Validation of unselected variants is diagnostic A/B, not selected-strategy WF performance."
}
```

## Corrección MCP y validación focalizada
Corregidos project_files.py y session_analysis.py para mapear únicamente los estados de dominio applied/disabled/not_applied de backtest funding a status=success, preservando funding_status, ledger y paginación. Errores reales y otras operaciones no se relajan. 123 tests pasaron en test_mcp_session_results.py y test_mcp_project_files.py; Pyrefly 0 errores en ambos servicios; git diff --check limpio. Prueba API→MCP en proceso fresco aprobada. El daemon previamente abierto conserva módulos antiguos: prueba real posterior al fix status=error, error_type=http_error. Requiere recargar su proceso para adoptar el cambio. No se reinició backend, Docker ni trading; esto no afecta los resultados obtenidos ni la auditoría por snapshots.
