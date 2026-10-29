# Diagnóstico de siete MARKET en política retest de referencia

[C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) contiene24 entradas ejecutadas LIMIT y7MARKET. Job0151f890cd9b49459745e5283a570412 succeeded extrae todos los campos de las siete órdenes desde snapshot completo. En siete, created_at==executed_at==opened_at; precio registrado coincide con entry salvo redondeo de float. No se conserva el límite solicitado ni el close de decisión aparte del precio ejecutado en este snapshot: no reconstruir boundary histórico ni su distancia exacta ex post.

| UTC creación = ejecución = apertura | Precio orden | Precio entry | Qty |
| --- | ---: | ---: | ---: |
| 2021-04-09T04:00:00.000Z | 410.1748 | 410.1748 | 30.017 |
| 2023-05-30T12:00:00.000Z | 422.5967 | 422.5967 | 26.01 |
| 2023-10-12T04:00:00.000Z | 438.6092 | 438.6092 | 18.272000000000002 |
| 2023-12-11T16:00:00.000Z | 460.9847 | 460.98470000000003 | 25.316 |
| 2023-12-28T08:00:00.000Z | 479.2623 | 479.2623 | 30.202 |
| 2024-02-02T12:00:00.000Z | 493.6563 | 493.6563 | 22.400000000000002 |
| 2025-10-28T12:00:00.000Z | 687.9354 | 687.9354 | 18.181 |

Root verificó fuente local framework: Strategy.py:674–683 _submit_buy_orders evalúa is_price_near antes de clasificar por precio superior/inferior; helpers.py:1253–1260 define abs(1−order/current)<=0.00015 (1.5bps). Por tanto la intención pasiva puede generar MARKET por smart-order. Fuente de estrategia exige boundary<close, pero la clasificación admite proximidad. Esta semántica explica posibilidad de conversión; los snapshots no prueban cada boundary exacto y no implican fills ficticios. Comisión sigue.00045 en todos los tipos. No se cambia motor ni estrategia.

## Fuente análisis

```python
import json
from pathlib import Path
d=json.load(open('inputs/C0.json'))
rows=[]
for t in d.get('trades',[]):
 for o in t['orders']:
  if o['status']=='EXECUTED' and not o.get('reduce_only') and o['type']=='MARKET':
   rows.append({'trade_id':t['id'],'opened_at':t['opened_at'],'entry_price':t['entry_price'],'qty':t['qty'],'order':o})
Path('output').mkdir(exist_ok=True)
json.dump(rows,open('output/market_entries.json','w'),indent=2)
print(json.dumps(rows))

```

Campos completos disponibles en market_entries.json del job. Sin nueva corrida económica.