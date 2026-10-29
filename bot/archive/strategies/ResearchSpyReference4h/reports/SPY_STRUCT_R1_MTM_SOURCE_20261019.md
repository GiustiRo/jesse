# SPY Structural R1 — fuente auditoría MTM

Se reutiliza auditor previamente validado: precio diario recuperado del buyhold de control y 19 fills MARKET SPY en16timestamps ancla. Inputs de control sólo recuperan marcas; no son nueva investigación de otros símbolos. Seis variantes por job más cuatro controles. Fronteras UTC incluidas a derecha; 61meses y19trimestres completos, parciales separados. No se usa Portfolio00:01 como cierreUTC. Forcedterminal se concilia por órdenes; no acredita liquidez real.

```python
"""Calendar-close MTM auditor for Jesse snapshot inputs.

Use run_analysis with this module INLINE, followed by main_mtm(names).
inputs/benchmarks.json must include buy-and-hold curves for the same immutable
exchange/symbol price series. Other snapshots supply midnight MARKET fills to
recover the price scale, checked against at least two distinct timestamps per market. Snapshot inputs must share the
same immutable exchange/symbol candle basis; matching symbols alone cannot prove this.
No database, credentials, network, or source CSV access is needed.

Only flat-terminal sessions with one entry and fully executed exit slices are
supported. Each partial exit is accounted at its own execution time. Prices use observed UTC daily closes, carrying the last observed mark
during closures for valuation only. Recorded end-of-minute timestamps are
right-edge inclusive: midnight fills belong to the day ending then.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DAY_MS = 86_400_000
# This tolerance checks numerical identity of source scales, not a trading threshold.
SCALE_RTOL = 1e-8


def recover_prices(snapshots, benchmark_name='benchmarks'):
    benchmark = snapshots[benchmark_name]
    observed = {}
    for curve in benchmark['equity_curve']:
        if curve['name'] == 'Portfolio':
            continue
        points = pd.DataFrame(curve['data'])
        series = pd.Series(points['value'].astype(float).to_numpy(),
                           index=pd.to_datetime(points['time'], unit='s', utc=True)).sort_index()
        if series.index.has_duplicates:
            raise ValueError('Duplicate benchmark dates')
        observed[curve['name']] = series
    anchors, anchor_times = {}, {}
    for name, snapshot in snapshots.items():
        if name == benchmark_name:
            continue
        for trade in snapshot.get('trades', []):
            for order in trade.get('orders', []):
                stamp = order.get('executed_at')
                if (str(order.get('status')).upper() != 'EXECUTED'
                        or str(order.get('type')).upper() != 'MARKET'
                        or stamp is None or int(stamp) % DAY_MS):
                    continue
                symbol = order['symbol']
                day = pd.Timestamp(int(stamp), unit='ms', tz='UTC') - pd.Timedelta(days=1)
                if symbol in observed and day in observed[symbol].index:
                    anchors.setdefault(symbol, {})[order['id']] = float(order['price']) / float(observed[symbol].loc[day])
                    anchor_times.setdefault(symbol, set()).add(int(stamp))
    prices, diagnostics = {}, {}
    for symbol, series in observed.items():
        ratios = np.array(list(anchors.get(symbol, {}).values()))
        if len(ratios) < 2 or len(anchor_times.get(symbol, set())) < 2:
            raise ValueError('At least two independent midnight MARKET anchors required: ' + symbol)
        scale = float(np.median(ratios))
        if not np.allclose(ratios, scale, rtol=SCALE_RTOL, atol=0):
            raise ValueError('Anchors do not match benchmark price basis: ' + symbol)
        prices[symbol] = series * scale
        diagnostics[symbol] = {'anchor_count': len(ratios), 'distinct_anchor_timestamps': len(anchor_times[symbol]), 'scale': scale,
                               'max_relative_error': float(np.max(np.abs(ratios / scale - 1)))}
    return prices, diagnostics


def _returns(equity, initial, frequency):
    end = equity.resample(frequency).last()
    previous = end.shift(1)
    previous.iloc[0] = initial
    return end / previous - 1, previous


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


def audit_mtm(snapshot, prices, name='session'):
    """Calendar-close MTM with one entry and any fully executed partial exits."""
    metrics = snapshot['metrics']
    form = snapshot['summary']['form']
    initial = float(metrics['starting_balance'])
    fee_rate = float(form['config']['exchange']['fee'])
    days = pd.date_range(pd.Timestamp(form['start_date'], tz='UTC'),
                         pd.Timestamp(form['finish_date'], tz='UTC') - pd.Timedelta(days=1), freq='D')
    valuation = (days + pd.Timedelta(days=1)).asi8 // 1_000_000
    by_route, active = {}, set()
    terminal_fills = []
    finish_ms = int(pd.Timestamp(form['finish_date'], tz='UTC').timestamp() * 1000)
    for trade in snapshot['trades']:
        symbol = trade['symbol']
        sign, entry, outgoing = _fills(trade, fee_rate)
        if outgoing[-1]['time'] == finish_ms:
            terminal_fills.append(sign * outgoing[-1]['qty'] * (outgoing[-1]['price'] - entry['price']))
        left = pd.Timestamp(entry['time'], unit='ms') - pd.Timedelta(milliseconds=1)
        right = pd.Timestamp(outgoing[-1]['time'], unit='ms') - pd.Timedelta(milliseconds=1)
        active.update(pd.period_range(left.to_period('M'), right.to_period('M'), freq='M'))
        if symbol not in by_route:
            by_route[symbol] = np.zeros(len(days))
        source = prices[symbol]
        marks = source.reindex(source.index.union(days)).sort_index().ffill().reindex(days)
        if marks.isna().any():
            raise ValueError('No observed mark at start: ' + symbol)
        entered = valuation >= entry['time']
        remaining = np.where(entered, entry['qty'], 0.0)
        cash_pnl = np.where(entered, -entry['fee'], 0.0)
        for fill in outgoing:
            done = valuation >= fill['time']
            remaining[done] -= fill['qty']
            cash_pnl[done] += (sign * fill['qty'] * (fill['price'] - entry['price'])
                               - fill['fee'])
        # A fully closed trade must carry exactly zero quantity afterwards;
        # floating subtraction dust must not create artificial future returns.
        remaining[valuation >= outgoing[-1]['time']] = 0.0
        # Completed slices crystallize PNL only when they execute. Mark the
        # remaining quantity, never the final trade VWAP or original full size.
        by_route[symbol] += cash_pnl + sign * remaining * (marks.to_numpy() - entry['price'])
    routes = pd.DataFrame(by_route, index=days).sort_index(axis=1)
    if routes.empty:
        routes = pd.DataFrame({'Cash': np.zeros(len(days))}, index=days)
    expected = sum(float(t['PNL']) for t in snapshot['trades'])
    if not np.isclose(routes.iloc[-1].sum(), expected, rtol=1e-9, atol=1e-6):
        raise ValueError('Terminal route PNL mismatch')
    if not np.isclose(initial + expected, metrics['finishing_balance'], rtol=1e-9, atol=1e-6):
        raise ValueError('Terminal wallet mismatch')
    # Jesse increments these counters BEFORE its standard end-of-run close.
    # A nonzero counter is not a residual position when complete boundary fills
    # and their pre-close gross PNL explain it. Ambiguous boundaries still fail.
    terminal_count = int(metrics.get('total_open_trades') or 0)
    if terminal_count < 0:
        raise ValueError('Invalid terminal counter')
    if terminal_count and (len(terminal_fills) != terminal_count
            or not np.isclose(sum(terminal_fills), float(metrics['open_pl']), rtol=1e-8, atol=1e-6)):
        raise ValueError('Unexplained terminal position counter; position snapshot required')
    terminal_diagnostics = {
        'pretermination_open_counter': terminal_count,
        'boundary_liquidations_reconciled': terminal_count,
        'boundary_close_is_execution_liquidity_proof': False,
    }
    equity = initial + routes.sum(axis=1)
    monthly, previous = _returns(equity, initial, 'ME')
    quarterly, _ = _returns(equity, initial, 'QE')
    yearly, _ = _returns(equity, initial, 'YE')
    route_months = routes.resample('ME').last()
    delta = route_months.diff()
    delta.iloc[0] = route_months.iloc[0]
    contributions = delta.div(previous, axis=0)
    if not np.allclose(contributions.sum(axis=1), monthly, atol=1e-10):
        raise ValueError('Monthly contributions do not reconcile')
    mask = np.array([date.tz_localize(None).to_period('M') in active for date in monthly.index])
    # Boundary bins are retained for continuity with prior reports. Also show
    # complete bins so a shortened first/last period cannot inflate regularity.
    start = pd.Timestamp(form['start_date'], tz='UTC')
    finish = pd.Timestamp(form['finish_date'], tz='UTC')
    def complete_bins(series, frequency):
        periods = series.index.tz_localize(None).to_period(frequency)
        return np.array([(p.start_time.tz_localize('UTC') >= start
                         and (p.end_time + pd.Timedelta(nanoseconds=1)).tz_localize('UTC') <= finish)
                         for p in periods])
    full_months, full_quarters = complete_bins(monthly, 'M'), complete_bins(quarterly, 'Q')
    full_active = full_months & mask
    complete_summary = {
        'months_total': int(full_months.sum()),
        'months_active': int(full_active.sum()),
        'positive_months': int((monthly[full_months] > 0).sum()),
        'win_months_all': float((monthly[full_months] > 0).mean()) if full_months.any() else None,
        'win_months_active': float((monthly[full_active] > 0).mean()) if full_active.any() else None,
        'quarters_total': int(full_quarters.sum()),
        'positive_quarters': int((quarterly[full_quarters] > 0).sum()),
        'win_quarters': float((quarterly[full_quarters] > 0).mean()) if full_quarters.any() else None,
    }
    corr = contributions.corr()
    corr_dict = corr.astype(object).where(pd.notna(corr), None).to_dict()
    peaks = np.maximum.accumulate(np.r_[initial, equity.to_numpy()])[1:]
    result = {'name': name, 'method': 'UTC day-close MTM from executed fills, right-edge inclusive',
              'partial_boundary_periods_included': True, 'complete_periods': complete_summary,
              'months_total': len(monthly),
              'months_active': int(mask.sum()), 'win_months_all': float((monthly > 0).mean()),
              'win_months_active': float((monthly[mask] > 0).mean()) if mask.any() else None,
              'win_quarters': float((quarterly > 0).mean()),
              'worst_month': [str(monthly.idxmin()), float(monthly.min())],
              'worst_quarter': [str(quarterly.idxmin()), float(quarterly.min())],
              'daily_close_drawdown_pct': float((equity.to_numpy() / peaks - 1).min() * 100),
              'mtm_route_contribution_correlation': corr_dict,
              'yearly_returns': {str(k): float(v) for k, v in yearly.items()},
              'terminal_reconciles': True, 'terminal_diagnostics': terminal_diagnostics}
    return result, monthly, contributions, equity


def main_mtm(names=('combined',)):
    snapshots = {path.stem: json.loads(path.read_text())
                 for path in Path('inputs').glob('*.json') if path.name != 'manifest.json'}
    prices, anchors = recover_prices(snapshots)
    print('PRICE_ANCHORS', json.dumps(anchors))
    results = []
    for name in names:
        result, monthly, contributions, equity = audit_mtm(snapshots[name], prices, name)
        print('CALENDAR_AUDIT', json.dumps(result, allow_nan=False))
        monthly.to_csv('output/' + name + '_calendar_month_returns.csv')
        contributions.to_csv('output/' + name + '_route_mtm_contributions.csv')
        equity.to_csv('output/' + name + '_daily_close_equity.csv')
        results.append(result)
    Path('output/calendar_audit.json').write_text(json.dumps(results, indent=2, allow_nan=False))
    return results


def self_test():
    from copy import deepcopy
    stamp = lambda text: int(pd.Timestamp(text).timestamp()*1000)
    def make(side):
        sign = 1 if side == 'long' else -1
        entry_price = 100.0
        p1,p2 = 100+sign*10,100+sign*20
        opened,partial,closed = (stamp(t) for t in
            ('2021-01-31T12:00:00Z','2021-01-31T18:00:00Z','2021-02-02T12:00:00Z'))
        orders = [
            {'id':'entry','status':'EXECUTED','reduce_only':False,'qty':2,'filled_qty':0,
             'price':100,'executed_at':opened,'side':'BUY' if sign==1 else 'SELL'},
            {'id':'p1','status':'EXECUTED','reduce_only':True,'qty':1,'filled_qty':1,
             'price':p1,'executed_at':partial,'side':'SELL' if sign==1 else 'BUY'},
            {'id':'p2','status':'EXECUTED','reduce_only':True,'qty':1,'filled_qty':0,
             'price':p2,'executed_at':closed,'side':'SELL' if sign==1 else 'BUY'}]
        fee=(200+p1+p2)*.001
        pnl=30-fee
        trade={'symbol':'X-USD','type':side,'qty':2,'entry_price':100,'exit_price':(p1+p2)/2,
               'opened_at':opened,'closed_at':closed,'orders':orders,'fee':fee,'PNL':pnl}
        snapshot={'metrics':{'starting_balance':10000,'finishing_balance':10000+pnl,'total_open_trades':0},
                  'summary':{'form':{'start_date':'2021-01-31','finish_date':'2021-02-03',
                                    'config':{'exchange':{'fee':.001}}}},'trades':[trade]}
        days=pd.date_range('2021-01-30','2021-02-02',freq='D',tz='UTC')
        prices={'X-USD':pd.Series([100,100+sign*5,100+sign*15,p2],index=days)}
        return snapshot,prices
    for side in ('long','short'):
        s,p=make(side)
        result,m,contributions,e=audit_mtm(s,p,side)
        expected_jan=15-(200+s['trades'][0]['orders'][1]['price'])*.001
        assert np.isclose(m.iloc[0],expected_jan/10000)
        assert result['complete_periods']['months_total'] == 0
        assert result['complete_periods']['quarters_total'] == 0
        assert np.isclose(e.iloc[-1],s['metrics']['finishing_balance'])
        assert np.allclose(contributions.sum(axis=1),m)
        assert np.isclose(np.prod(1+m),e.iloc[-1]/10000)
        # The partial fill exactly at midnight belongs to January's right edge.
        s['trades'][0]['orders'][1]['executed_at']=stamp('2021-02-01T00:00:00Z')
        _,boundary,_,_=audit_mtm(s,p)
        assert np.isclose(boundary.iloc[0],m.iloc[0])
        # One minute after midnight is outside January's right edge.
        s['trades'][0]['orders'][1]['executed_at']=stamp('2021-02-01T00:01:00Z')
        _,after,_,_=audit_mtm(s,p)
        assert np.isclose(after.iloc[0],(10-.2)/10000)
        # Submitted reduce quantity can exceed the actual remaining fill.
        s['trades'][0]['orders'][-1]['qty']=2
        s['trades'][0]['orders'][-1]['filled_qty']=1
        _,_,_,actual=audit_mtm(s,p)
        assert np.isclose(actual.iloc[-1],s['metrics']['finishing_balance'])
        s['trades'][0]['orders'][-1]['filled_qty']=0
        # An over-close must be rejected, not silently clipped to fit final PNL.
        bad=deepcopy(s)
        bad['trades'][0]['orders'][-1]['qty']=2
        try:
            audit_mtm(bad,p)
        except ValueError:
            pass
        else:
            raise AssertionError('Over-close accepted')
    # A pre-termination counter can coexist with a fully executed final close.
    s,p=make('long')
    final_time=stamp('2021-02-03T00:00:00Z')
    s['trades'][0]['orders'][-1]['executed_at']=final_time
    s['trades'][0]['closed_at']=final_time
    s['metrics']['total_open_trades']=1
    s['metrics']['open_pl']=20
    r,_,_,_=audit_mtm(s,p)
    assert r['terminal_diagnostics']['boundary_liquidations_reconciled']==1
    s['metrics']['open_pl']=21
    try:
        audit_mtm(s,p)
    except ValueError:
        pass
    else:
        raise AssertionError('Unexplained terminal counter accepted')
    s,p=make('long')
    s['trades']=[]
    s['metrics']['finishing_balance']=10000
    r,_,_,_=audit_mtm(s,p)
    assert r['months_active']==0 and r['win_months_all']==0
    print('MTM_ORDER_SELF_TEST_PASS')



# Llamar main_mtm con seis nombres PB01..06 o BR01..06.
```
