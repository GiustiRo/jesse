# SPY última ronda — diagnóstico conjunto de concentración y coste

Este análisis es POST HOC, añadido tras observar que concentración y costes por separado podían ocultar fragilidad conjunta. No es una validación predeclarada ni un backtest nuevo. Se retiran los mejores trades por neto original y se añade5bps por lado sobre los fills restantes. No se redimensiona capital, se simulan nuevas entradas ni se optimiza el ranking.

Job root `8a1b29dc984a4638a105e0d4d236b908` succeeded; el especialista produjo independientemente el mismo diagnóstico `dcbbcdb9950b4a69b9e516da8f4b0b70`. No son replicaciones de mercado.

MECH01 conserva105.62USDT sin sus3mejores y con10bpsRT extra. MECH05 queda−136.13 yMECH06−42.40. Por tanto, no afirmar que MECH05/06 sobreviven simultáneamente ambos castigos por presentar sus pruebas separadas positivas. MECH01 sólo tiene12operaciones originales y9restantes, no certeza estadística.

```json
{
  "MECH01": {
    "n": 12,
    "net": 1179.9815614338606,
    "plus10_samefills": 1054.288970230002,
    "exbest_plus10": 633.9221258370221,
    "ex3_plus10": 105.62345322528955,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "MECH02": {
    "n": 11,
    "net": 770.5482833495946,
    "plus10_samefills": 639.1192360597395,
    "exbest_plus10": 226.84685930465434,
    "ex3_plus10": -268.03770471781013,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "MECH03": {
    "n": 10,
    "net": 697.9686460382607,
    "plus10_samefills": 580.1149505763839,
    "exbest_plus10": 170.62020129372445,
    "ex3_plus10": -324.2643627287401,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "MECH04": {
    "n": 16,
    "net": 874.7958565504186,
    "plus10_samefills": 707.469188493318,
    "exbest_plus10": 298.59407002831085,
    "ex3_plus10": -223.07893097807573,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "MECH05": {
    "n": 19,
    "net": 1275.1636142229213,
    "plus10_samefills": 1075.5958141500769,
    "exbest_plus10": 600.2455471977295,
    "ex3_plus10": -136.13410899186948,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "MECH06": {
    "n": 12,
    "net": 962.214158299294,
    "plus10_samefills": 829.7056392851879,
    "exbest_plus10": 417.5471705550461,
    "ex3_plus10": -42.40074231197333,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "Cq": {
    "n": 31,
    "net": 751.3477149671146,
    "plus10_samefills": 433.04157473672745,
    "exbest_plus10": 40.91006878171633,
    "ex3_plus10": -587.123656556576,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  },
  "BR02": {
    "n": 16,
    "net": 874.7958565504186,
    "plus10_samefills": 707.469188493318,
    "exbest_plus10": 298.59407002831085,
    "ex3_plus10": -223.07893097807573,
    "definition": "Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry."
  }
}
```

## Fuente exacta

```python
import json
from pathlib import Path
import numpy as np
def _fills(trade, fee_rate):
    """Validate one entry and fully closing exits, retaining each executed fill."""
    if trade['type'] not in ('long', 'short'):
        raise ValueError('Unsupported trade direction')
    if any(str(o.get('status')).upper() == 'PARTIALLY_FILLED' for o in trade['orders']):
        raise ValueError('Partially filled order snapshots are unsupported')
    executed = [o for o in trade['orders'] if str(o.get('status')).upper() == 'EXECUTED']
    entries = [o for o in executed if not bool(o.get('reduce_only'))]
    exits = [o for o in executed if bool(o.get('reduce_only'))]
    if len(entries) != 1 or not exits:
        raise ValueError('Exactly one entry and one or more complete exit fills required')
    ids = [o.get('id') for o in executed if o.get('id') is not None]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate executed order IDs')
    sign = 1 if trade['type'] == 'long' else -1
    entry_side = 'BUY' if sign == 1 else 'SELL'
    def unpack(order, side):
        # Jesse simulations can leave filled_qty at zero after full execution.
        # An EXECUTED order then uses its submitted qty; positive filled_qty wins.
        filled = abs(float(order.get('filled_qty') or 0))
        qty = filled if filled > 0 else abs(float(order['qty']))
        price = float(order['price'])
        stamp = order.get('executed_at')
        if stamp is None or qty <= 0 or price <= 0 or not np.isfinite(qty + price):
            raise ValueError('Invalid/missing executed fill economics')
        if str(order['side']).upper() != side:
            raise ValueError('Fill side inconsistent with position direction')
        return {'qty': qty, 'price': price, 'time': int(stamp),
                'fee': qty * price * fee_rate}
    entry = unpack(entries[0], entry_side)
    outgoing = sorted([unpack(o, 'SELL' if sign == 1 else 'BUY') for o in exits],
                      key=lambda o: o['time'])
    remaining = entry['qty']
    realized = -entry['fee']
    for fill in outgoing:
        if fill['time'] < entry['time']:
            raise ValueError('Exit precedes entry')
        remaining -= fill['qty']
        if remaining < -1e-8:
            raise ValueError('Exit quantities exceed opened position')
        realized += sign * fill['qty'] * (fill['price'] - entry['price']) - fill['fee']
    if not np.isclose(remaining, 0, rtol=0, atol=1e-8):
        raise ValueError('Closed trade does not fully close its entry quantity')
    if entry['time'] != int(trade['opened_at']) or outgoing[-1]['time'] != int(trade['closed_at']):
        raise ValueError('Trade lifecycle and fill timestamps disagree')
    expected_fee = entry['fee'] + sum(fill['fee'] for fill in outgoing)
    if not np.isclose(expected_fee, float(trade['fee']), rtol=1e-8, atol=1e-6):
        raise ValueError('Per-fill commissions do not reconcile to closed trade')
    if not np.isclose(realized, float(trade['PNL']), rtol=1e-8, atol=1e-6):
        raise ValueError('Per-fill realized PNL does not reconcile')
    return sign, entry, outgoing



names=["MECH01","MECH02","MECH03","MECH04","MECH05","MECH06","Cq","BR02"]
results={}
for name in names:
    snap=json.loads(Path('inputs/'+name+'.json').read_text())
    fee=float(snap['summary']['form']['config']['exchange']['fee'])
    trades=[]
    for trade in snap['trades']:
        sign,entry,exits=_fills(trade,fee)
        turnover=entry['qty']*entry['price']+sum(e['qty']*e['price'] for e in exits)
        trades.append({'net':float(trade['PNL']),'cost10':turnover*.0005})
    trades.sort(key=lambda x:x['net'],reverse=True)
    results[name]={'n':len(trades),'net':sum(t['net'] for t in trades),
                   'plus10_samefills':sum(t['net']-t['cost10'] for t in trades),
                   'exbest_plus10':sum(t['net']-t['cost10'] for t in trades[1:]),
                   'ex3_plus10':sum(t['net']-t['cost10'] for t in trades[3:]),
                   'definition':'Remove top original-net trades, then 5bps per side on remaining fills; no resizing/reentry.'}
Path('output/combined_stress.json').write_text(json.dumps(results,indent=2,allow_nan=False))
print(json.dumps(results))

```
