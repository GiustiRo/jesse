# Selección previa a validación

Las cuatro sesiones de desarrollo terminaron. Ninguna candidata supera los criterios prerregistrados: F1 SIN_CANDIDATA; F2 SIN_CANDIDATA. Este registro se guarda ANTES de crear/ejecutar validaciones. Las cuatro validaciones siguientes serán diagnóstico A/B sin promoción ni cambios de parámetros.

Análisis MCP b02a70a19ba44892bef081f7e11292be; ledger y trades reconciliados, error por trade 0.

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
      "max_reconciliation_error": 0.0,
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
      "max_reconciliation_error": 0.0,
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
      "max_reconciliation_error": 0.0,
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
      "max_reconciliation_error": 0.0,
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
    }
  ],
  "development_selection": {
    "F1": "SIN_CANDIDATA",
    "F2": "SIN_CANDIDATA"
  },
  "note": "Validation of unselected variants is diagnostic A/B, not selected-strategy WF performance."
}
```
