# R9 — código de auditoría y orquestación

Auditor core heredado de R8, sin cambios financieros. Snapshots completos con4anclas; las etiquetas de suplemento son una conciliación metadata separada por logs completos, no cálculo de PNL. Se aceptan snapshots porclaveexchange-symbol o classname concontenidoexacto; fuente K1005 recuperada porread_strategy porque el ensamblaje paginado del informe añadió un salto de línea artificial, sin modificación de estrategia. Guard TPpositivo y QAfinal se documentan antes de vecinos full. Este código y estado del manifiesto permiten rastrear herramientas y criterios; no convierten muestra reutilizada en OOS.

## Core financiero

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
from copy import deepcopy

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
    routes.to_csv('output/' + name + '_daily_route_pnl.csv')
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



import itertools
import hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def interval_union(intervals):
    total=0; right=None
    for left,end in sorted(intervals):
        if right is None or left>right:
            total+=end-left;right=end
        elif end>right:
            total+=end-right;right=end
    return total

def run_portfolio_audit(names):
    snapshots={p.stem:json.loads(p.read_text()) for p in Path('inputs').glob('*.json') if p.name!='manifest.json'}
    prices,anchors=recover_prices(snapshots)
    results={};calendars={};pairs={};figure,axes=plt.subplots(2,1,figsize=(12,8),sharex=True,gridspec_kw={'height_ratios':[2,1]})
    for name in names:
        snap=snapshots[name];metrics=snap['metrics'];form=snap['summary']['form']
        initial=float(metrics['starting_balance']);fee_rate=float(form['config']['exchange']['fee'])
        duration_ms=int((pd.Timestamp(form['finish_date'])-pd.Timestamp(form['start_date'])).total_seconds()*1000)
        detail=[];by_group={};by_symbol={};intervals=[]
        for t in snap['trades']:
            sign,entry,exits=_fills(t,fee_rate)
            net=float(t['PNL']);fee=float(t['fee'])
            turnover=entry['qty']*entry['price']+sum(e['qty']*e['price'] for e in exits)
            hold=int(t['closed_at'])-int(t['opened_at']);intervals.append((int(t['opened_at']),int(t['closed_at'])))
            group=t['symbol']+':'+t['type']
            row={'symbol':t['symbol'],'side':t['type'],'open':int(t['opened_at']),'close':int(t['closed_at']),
                 'qty':entry['qty'],'entry':entry['price'],'exit':float(t['exit_price']),'net':net,'fee':fee,'turnover':turnover,
                 'entry_notional':entry['qty']*entry['price'],'hold_ms':hold,
                 'cost5':turnover*.00025,'cost10':turnover*.0005,
                 'entry_type':next(str(o['type']).upper() for o in t['orders'] if str(o['status']).upper()=='EXECUTED' and not o.get('reduce_only')),
                 'close_year':str(pd.Timestamp(t['closed_at'],unit='ms',tz='UTC').year)}
            detail.append(row)
        net=sum(t['net'] for t in detail);fees=sum(t['fee'] for t in detail)
        assert np.isclose(net,metrics['net_profit'],atol=1e-6,rtol=1e-8)
        assert np.isclose(fees,metrics['fee'],atol=1e-6,rtol=1e-8)
        assert np.isclose(initial+net,metrics['finishing_balance'],atol=1e-6,rtol=1e-8)
        for key in sorted(set(t['symbol']+':'+t['side'] for t in detail)):
            sub=[t for t in detail if t['symbol']+':'+t['side']==key]
            by_group[key]={'n':len(sub),'net':sum(t['net'] for t in sub),'fees':sum(t['fee'] for t in sub),
                           'plus10':sum(t['net']-t['cost10'] for t in sub),
                           'time_open_pct':100*sum(t['hold_ms'] for t in sub)/duration_ms,
                           'entry_notional_time_initial_equity':sum(t['entry_notional']*t['hold_ms'] for t in sub)/(initial*duration_ms)}
        for symbol in sorted(set(t['symbol'] for t in detail)):
            sub=[t for t in detail if t['symbol']==symbol]
            by_symbol[symbol]={'n':len(sub),'net':sum(t['net'] for t in sub),'fees':sum(t['fee'] for t in sub)}
        yearly={}
        for year in sorted(set(t['close_year'] for t in detail)):
            sub=[t for t in detail if t['close_year']==year]
            yearly[year]={'n':len(sub),'net':sum(t['net'] for t in sub),
                          'by_symbol':{symbol:sum(t['net'] for t in sub if t['symbol']==symbol) for symbol in by_symbol}}
        ordered=sorted(detail,key=lambda t:t['net'],reverse=True)
        positive=sum(t['net'] for t in detail if t['net']>0);negative=-sum(t['net'] for t in detail if t['net']<0)
        res={'n':len(detail),'net':net,'gross_before_fees':net+fees,'fees':fees,'pf_from_trades':positive/negative if negative else None,
             'PF_engine':metrics.get('ratio_avg_win_loss')*metrics.get('total_winning_trades',0)/metrics.get('total_losing_trades',1) if metrics.get('total_losing_trades') else None,
             'sharpe_engine':metrics.get('sharpe_ratio'),'cagr_engine':metrics.get('annual_return'),'dd_engine':metrics.get('max_drawdown'),
             'plus5_samefills':sum(t['net']-t['cost5'] for t in detail),
             'plus10_samefills':sum(t['net']-t['cost10'] for t in detail),
             'exbest':sum(t['net'] for t in ordered[1:]),'ex3best':sum(t['net'] for t in ordered[3:]),
             'ex3best_plus10_samefills':sum(t['net']-t['cost10'] for t in ordered[3:]),
             'time_any_position_pct':100*interval_union(intervals)/duration_ms,
             'entry_notional_time_initial_equity':sum(t['entry_notional']*t['hold_ms'] for t in detail)/(initial*duration_ms),
             'entry_turnover_initial_equity':sum(t['entry_notional'] for t in detail)/initial,
             'two_side_turnover_initial_equity':sum(t['turnover'] for t in detail)/initial,
             'by_group':by_group,'by_symbol':by_symbol,'closed_trade_year_cohorts_NOT_MTM':yearly,
             'entry_order_types':{typ:sum(t['entry_type']==typ for t in detail) for typ in sorted(set(t['entry_type'] for t in detail))},
             'audit':'passed'}
        res['entry_type_groups']={}
        for group in sorted(set(t['symbol']+':'+t['side']+':'+t['entry_type'] for t in detail)):
            sub=[t for t in detail if t['symbol']+':'+t['side']+':'+t['entry_type']==group]
            ordered_sub=sorted(sub,key=lambda t:t['net'],reverse=True)
            res['entry_type_groups'][group]={'n':len(sub),'net':sum(t['net'] for t in sub),
                'fees':sum(t['fee'] for t in sub),'gross':sum(t['net']+t['fee'] for t in sub),
                'plus10':sum(t['net']-t['cost10'] for t in sub),
                'exbest':sum(t['net'] for t in ordered_sub[1:]),
                'ex3':sum(t['net'] for t in ordered_sub[3:]),
                'ex3_plus10':sum(t['net']-t['cost10'] for t in ordered_sub[3:]),
                'year_net':{year:sum(t['net'] for t in sub if t['close_year']==year) for year in sorted(set(t['close_year'] for t in sub))}}
        res['group_stress']={}
        for group in by_group:
            sub=sorted([t for t in detail if t['symbol']+':'+t['side']==group],key=lambda t:t['net'],reverse=True)
            res['group_stress'][group]={'gross':sum(t['net']+t['fee'] for t in sub),
                'exbest':sum(t['net'] for t in sub[1:]),'ex3best':sum(t['net'] for t in sub[3:]),
                'ex3best_plus10':sum(t['net']-t['cost10'] for t in sub[3:]),
                'years':{year:{'n':sum(t['close_year']==year for t in sub),
                    'net':sum(t['net'] for t in sub if t['close_year']==year),
                    'plus10':sum(t['net']-t['cost10'] for t in sub if t['close_year']==year)}
                    for year in sorted(set(t['close_year'] for t in sub))}}
        mtm,monthly,contrib,equity=audit_mtm(snap,prices,name)
        res['calendar_numerical_diagnostics']={'nonzero_month_returns_below_1e_10':{str(k):float(v) for k,v in monthly.items() if 0<abs(v)<1e-10},
            'note':'Numerical zero flag only; primary >0 convention unchanged from controls.'}
        res['mtm']=mtm;calendars[name]={'monthly':monthly,'contributions':contrib,'equity':equity}
        monthly.to_csv('output/'+name+'_monthly_returns.csv');contrib.to_csv('output/'+name+'_monthly_contributions.csv');equity.to_csv('output/'+name+'_daily_equity.csv')
        full=(monthly.index>=pd.Timestamp('2020-11-01',tz='UTC'))&(monthly.index<pd.Timestamp('2025-12-01',tz='UTC'))
        assert int(full.sum())==61
        cc=contrib.loc[full]; mm=monthly.loc[full]
        res['complete_month_contribution_correlation']=cc.corr().astype(object).where(pd.notna(cc.corr()),None).to_dict()
        res['co_loss_complete_months']={}
        for a,b in itertools.combinations(cc.columns,2):
            res['co_loss_complete_months'][a+'__'+b]={'both_negative':int(((cc[a]<0)&(cc[b]<0)).sum()),
                'both_nonzero':int(((cc[a]!=0)&(cc[b]!=0)).sum()),'both_negative_and_portfolio_negative':int(((cc[a]<0)&(cc[b]<0)&(mm<0)).sum())}
        res['worst_10_complete_months']=[{'month':str(date),'portfolio_return':float(mm.loc[date]),
            'contributions':{col:float(cc.loc[date,col]) for col in cc.columns}} for date in mm.nsmallest(10).index]
        daily_routes=pd.read_csv('output/'+name+'_daily_route_pnl.csv',index_col=0,parse_dates=True)
        peaks=np.maximum.accumulate(np.r_[initial,equity.to_numpy()])[1:];dd=equity.to_numpy()/peaks-1
        trough=int(np.argmin(dd));peak_value=peaks[trough]
        candidates=np.flatnonzero(np.isclose(equity.to_numpy()[:trough+1],peak_value,rtol=1e-12,atol=1e-8))
        peak=int(candidates[-1]) if len(candidates) else None
        start_vec=daily_routes.iloc[peak] if peak is not None else daily_routes.iloc[0]*0
        res['daily_drawdown_episode']={'peak':'initial' if peak is None else str(equity.index[peak]),'trough':str(equity.index[trough]),
          'drawdown_pct':float(dd[trough]*100),'route_pnl_delta_USDT':{col:float(daily_routes.iloc[trough][col]-start_vec[col]) for col in daily_routes.columns}}
        Path('output/'+name+'_path.json').write_text(json.dumps([{k:t[k] for k in ('symbol','side','open','close','entry','exit','qty','net','fee','entry_type')} for t in detail],separators=(',',':'),allow_nan=False))

        res['engine_fee_per_side']=fee_rate
        res['cost_calendar']={}
        for bps,extra in ((5,.00025),(10,.0005)):
            stressed=deepcopy(snap);additional=0.0
            for trade in stressed['trades']:
                _,ent,outs=_fills(trade,fee_rate)
                cost=extra*(ent['qty']*ent['price']+sum(x['qty']*x['price'] for x in outs))
                trade['fee']=float(trade['fee'])+cost
                trade['PNL']=float(trade['PNL'])-cost
                additional+=cost
            stressed['summary']['form']['config']['exchange']['fee']=fee_rate+extra
            for metric_key in ('net_profit','finishing_balance'):
                stressed['metrics'][metric_key]=float(stressed['metrics'][metric_key])-additional
            stressed['metrics']['fee']=float(stressed['metrics']['fee'])+additional
            stress_mtm,stress_months,stress_contrib,stress_equity=audit_mtm(stressed,prices,name+'_cost'+str(bps))
            expected_net=res['plus5_samefills'] if bps==5 else res['plus10_samefills']
            assert np.isclose(stressed['metrics']['net_profit'],expected_net,rtol=1e-9,atol=1e-6)
            res['cost_calendar'][str(bps)]={'extra_bps_RT':bps,'engine_fee_basis_per_side':fee_rate,
                'samefills_net':stressed['metrics']['net_profit'],'extra_cost':additional,
                'samefills_cagr_pct':100*((stressed['metrics']['finishing_balance']/initial)**(365/(duration_ms/86400000))-1),
                'complete_periods':stress_mtm['complete_periods'],
                'partial_periods':{'months_total':stress_mtm['months_total'],'months_active':stress_mtm['months_active'],
                    'positive_months':int(round(stress_mtm['win_months_active']*stress_mtm['months_active'])),
                    'win_months_all':stress_mtm['win_months_all'],'win_months_active':stress_mtm['win_months_active'],
                    'quarters_total':21,'positive_quarters':int(round(stress_mtm['win_quarters']*21)),'win_quarters':stress_mtm['win_quarters']},
                'daily_close_drawdown_pct':stress_mtm['daily_close_drawdown_pct'],'worst_month':stress_mtm['worst_month'],
                'yearly_returns':stress_mtm['yearly_returns'],
                'nearzero_months':{str(k):float(v) for k,v in stress_months.items() if 0<abs(v)<1e-10},
                'positive_to_nonpositive_months':[str(k) for k in monthly.index if monthly[k]>0 and stress_months[k]<=0]}
            stress_months.to_csv('output/'+name+'_cost'+str(bps)+'_monthly_returns.csv')
        

        # Split path diagnostics so text transport cannot truncate large sessions.
        path_columns=('symbol','side','open','close','entry','exit','qty','net','fee','entry_type')
        path_rows=[{k:t[k] for k in path_columns} for t in detail]
        path_parts=[]
        for part_index,offset in enumerate(range(0,len(path_rows),150)):
            part_path=name+'_path_part'+str(part_index)+'.json'
            Path('output/'+part_path).write_text(json.dumps(path_rows[offset:offset+150],separators=(',',':'),allow_nan=False))
            path_parts.append(part_path)
        Path('output/'+name+'_path_manifest.json').write_text(json.dumps({'rows':len(path_rows),'parts':path_parts}))

        results[name]=res
        Path('output/'+name+'_summary.json').write_text(json.dumps(res,indent=2,allow_nan=False))
        Path('output/'+name+'_trade_audit.json').write_text(json.dumps(detail,separators=(',',':'),allow_nan=False))
        axes[0].plot(equity.index,equity,label=name,lw=1.2)
        axes[1].plot(equity.index,100*dd,label=name,lw=1)
    for base,new in []:
        a,b=results[base],results[new]
        source={symbol:b['by_symbol'].get(symbol,{'net':0})['net']-a['by_symbol'].get(symbol,{'net':0})['net'] for symbol in set(a['by_symbol'])|set(b['by_symbol'])}
        pairs[base+'__'+new]={'net_delta':b['net']-a['net'],'fees_delta':b['fees']-a['fees'],
          'plus10_delta':b['plus10_samefills']-a['plus10_samefills'],'dd_engine_delta':b['dd_engine']-a['dd_engine'],
          'by_symbol_closed_trade_net_delta':source,
          'complete_months_positive_return_delta':int(((calendars[new]['monthly']-calendars[base]['monthly']).loc[lambda z:(z.index>=pd.Timestamp('2020-11-01',tz='UTC'))&(z.index<pd.Timestamp('2025-12-01',tz='UTC'))]>0).sum()),
          'limitation':'Capital, sizing and occupancy endogenous; not fixed-trade causal attribution.'}
    axes[0].set_title('Shared portfolio candidates - 10,000 USDT, 1% planned trade risk')
    axes[0].set_ylabel('Equity at UTC day close (USDT)');axes[0].legend();axes[0].grid(alpha=.2)
    axes[1].set_ylabel('Drawdown (%)');axes[1].grid(alpha=.2);figure.tight_layout();figure.savefig('output/portfolio_equity_drawdown.png',dpi=120);plt.close(figure)
    Path('output/portfolio_summary.json').write_text(json.dumps({'results':results,'comparisons':pairs,'price_anchors':anchors},indent=2,allow_nan=False))
    print('PORTFOLIO_AUDIT',json.dumps({'rows':{n:{'n':r['n'],'net':r['net'],'DD':r['dd_engine'],'plus10':r['plus10_samefills'],'calendar':r['mtm']['complete_periods']} for n,r in results.items()},'comparisons':pairs},allow_nan=False))

run_portfolio_audit(NAMES_PLACEHOLDER)


def r3_month_diagnostics(names):
    """Attribute calendar friction at each fill's right-edge UTC month."""
    snapshots={p.stem:json.loads(p.read_text()) for p in Path('inputs').glob('*.json') if p.name!='manifest.json'}
    tables={}; summaries={}
    for name in names:
        snap=snapshots[name]
        fee=float(snap['summary']['form']['config']['exchange']['fee'])
        initial=float(snap['metrics']['starting_balance'])
        routes=pd.read_csv('output/'+name+'_daily_route_pnl.csv',index_col=0,parse_dates=True)
        eq=pd.read_csv('output/'+name+'_daily_equity.csv',index_col=0,parse_dates=True).iloc[:,0]
        endeq=eq.resample('ME').last()
        pnl=endeq.diff();pnl.iloc[0]=endeq.iloc[0]-initial
        route_end=routes.resample('ME').last()
        route_pnl=route_end.diff();route_pnl.iloc[0]=route_end.iloc[0]
        if not np.allclose(route_pnl.sum(axis=1),pnl,atol=1e-6,rtol=1e-9): raise ValueError('R3 monthly route mismatch')
        ret=pd.read_csv('output/'+name+'_monthly_returns.csv',index_col=0,parse_dates=True).iloc[:,0]
        if not np.array_equal(np.sign(pnl),np.sign(ret)): raise ValueError('R3 monthly sign mismatch')
        idx=pnl.index
        budgets=pd.DataFrame(0.0,index=idx,columns=['turnover','fees'])
        route_budget={sym:pd.DataFrame(0.0,index=idx,columns=['turnover','fees']) for sym in routes.columns}
        permap={d.tz_localize(None).to_period('M'):d for d in idx}
        for trade in snap['trades']:
            _,entry,outs=_fills(trade,fee)
            for fill in [entry]+outs:
                # Midnight execution is the preceding day's inclusive right edge.
                period=(pd.Timestamp(fill['time'],unit='ms',tz='UTC')-pd.Timedelta(milliseconds=1)).tz_localize(None).to_period('M')
                month=permap[period]
                value=abs(fill['qty']*fill['price'])
                budgets.loc[month,'turnover']+=value
                budgets.loc[month,'fees']+=fill['fee']
                route_budget[trade['symbol']].loc[month,'turnover']+=value
                route_budget[trade['symbol']].loc[month,'fees']+=fill['fee']
        assert np.isclose(budgets['fees'].sum(),float(snap['metrics']['fee']),atol=1e-6,rtol=1e-9)
        after={}; costs={}
        for bps in (5,10):
            stress=pd.read_csv('output/'+name+'_cost'+str(bps)+'_daily_route_pnl.csv',index_col=0,parse_dates=True)
            stress_end=(initial+stress.sum(axis=1)).resample('ME').last()
            stressed_pnl=stress_end.diff();stressed_pnl.iloc[0]=stress_end.iloc[0]-initial
            extra=budgets['turnover']*bps/20000.0
            assert np.allclose(pnl-stressed_pnl,extra,atol=1e-6,rtol=1e-9)
            after[bps]=stressed_pnl;costs[bps]=extra
        full=(idx>=pd.Timestamp('2020-11-01',tz='UTC'))&(idx<pd.Timestamp('2025-12-01',tz='UTC'))
        assert int(full.sum())==61 and len(idx)==63
        rows=[]
        for month in idx:
            v=float(pnl.loc[month]);c5=float(costs[5].loc[month]);c10=float(costs[10].loc[month])
            klass=('loss_base' if v<0 else 'zero_base' if v==0 else
                   'positive_within_cost5' if v<=c5 else 'positive_between_cost5_cost10' if v<=c10 else 'positive_above_cost10')
            row={'month':month.strftime('%Y-%m'),'complete':bool(full[idx.get_loc(month)]),
                 'mtm_USDT':v,'return':float(ret.loc[month]),'turnover':float(budgets.loc[month,'turnover']),
                 'fees':float(budgets.loc[month,'fees']),'gross_arithmetic_fixed_path':v+float(budgets.loc[month,'fees']),'cost5':c5,'cost10':c10,
                 'mtm_after5':float(after[5].loc[month]),'mtm_after10':float(after[10].loc[month]),'class':klass,
                 'positive_base':v>0,'positive_after5':bool(after[5].loc[month]>0),
                 'positive_after10':bool(after[10].loc[month]>0),
                 'extra_RT_bps_to_zero':20000*v/float(budgets.loc[month,'turnover']) if v>0 and budgets.loc[month,'turnover']>0 else None,
                 'routes':{sym:{'mtm':float(route_pnl.loc[month,sym]),'fees':float(route_budget[sym].loc[month,'fees']),
                                'turnover':float(route_budget[sym].loc[month,'turnover'])} for sym in routes.columns}}
            rows.append(row)
        tables[name]=rows
        summary={}
        for sample,rr in [('full61',[r for r in rows if r['complete']]),('included63',rows)]:
            values=np.array([r['mtm_USDT'] for r in rr])
            class_counts={k:sum(r['class']==k for r in rr) for k in ('loss_base','zero_base','positive_within_cost5','positive_between_cost5_cost10','positive_above_cost10')}
            assert sum(class_counts.values())==len(rr)
            positive_sum=float(sum(max(0.0,r['mtm_USDT']) for r in rr))
            sorted_positive=sorted((r['mtm_USDT'] for r in rr if r['mtm_USDT']>0),reverse=True)
            summary[sample]={'months':len(rr),'net_mtm':float(values.sum()),'mean_month_USDT':float(values.mean()),
                'median_month_USDT':float(np.median(values)),'sum_positive_months':positive_sum,
                'sum_negative_months':float(sum(min(0.0,r['mtm_USDT']) for r in rr)),
                'worst_month':min(rr,key=lambda r:r['mtm_USDT'])['month'],'worst_month_USDT':float(values.min()),
                'best3_share_positive_mtm':sum(sorted_positive[:3])/positive_sum if positive_sum else None,
                'class_counts':class_counts,'positive_months':sum(r['positive_base'] for r in rr),
                'gross_fixed_path':{'positive_months':sum(r['gross_arithmetic_fixed_path']>0 for r in rr),'negative_months':sum(r['gross_arithmetic_fixed_path']<0 for r in rr),'zero_months':sum(r['gross_arithmetic_fixed_path']==0 for r in rr),
                    'net_before_actual_fees':sum(r['gross_arithmetic_fixed_path'] for r in rr),'fee_total':sum(r['fees'] for r in rr),
                    'fee_absorbed_positive_months':[{'month':r['month'],'gross':r['gross_arithmetic_fixed_path'],'fee':r['fees'],'net':r['mtm_USDT']} for r in rr if r['gross_arithmetic_fixed_path']>0 and r['mtm_USDT']<=0]},
                'co_loss_counts':{s1+'__'+s2:sum(r['routes'][s1]['mtm']<0 and r['routes'][s2]['mtm']<0 for r in rr) for s1,s2 in itertools.combinations(routes.columns,2)},
                'stress':{str(bps):{'positive_months':sum(r['positive_after'+str(bps)] for r in rr),
                    'extra_cost':sum(r['cost'+str(bps)] for r in rr),
                    'flip_months':[{'month':r['month'],'base':r['mtm_USDT'],'extra':r['cost'+str(bps)],'after':r['mtm_after'+str(bps)]} for r in rr if r['mtm_USDT']>0 and not r['positive_after'+str(bps)]],
                    'already_negative_months':sum(r['mtm_USDT']<0 for r in rr),
                    'already_negative_base_sum':sum(r['mtm_USDT'] for r in rr if r['mtm_USDT']<0),
                    'already_negative_after_sum':sum(r['mtm_after'+str(bps)] for r in rr if r['mtm_USDT']<0)} for bps in (5,10)}}
        assert np.isclose(sum(r['mtm_USDT'] for r in rows),float(snap['metrics']['net_profit']),atol=1e-6,rtol=1e-9)
        summaries[name]={'fee_engine_per_side':fee,'notes':'Extra overlays relative to this session fee; fixed paths and quantities. UTC right-edge MTM, not closed-trade cohorts. Class counts use all calendar months; activity-based denominators remain in auditor summary.','samples':summary}
        Path('output/'+name+'_r3_month_rows.json').write_text(json.dumps(rows,separators=(',',':'),allow_nan=False))
        Path('output/'+name+'_r3_month_summary.json').write_text(json.dumps(summaries[name],indent=2,allow_nan=False))
        pd.DataFrame([{k:v for k,v in row.items() if k!='routes'} for row in rows]).to_csv('output/'+name+'_r3_months.csv',index=False)
    paired={}
    candidates=[('X03N_'+p,'N204N_'+p) for p in ('B','C')]+[('X03S_'+p,'N204S_'+p) for p in ('B','C')]
    for base,new in candidates:
        if base not in tables or new not in tables:continue
        rr=[]
        for x,y in zip(tables[base],tables[new]):
            assert x['month']==y['month']
            rr.append({'month':x['month'],'complete':x['complete'],'base_mtm':x['mtm_USDT'],'new_mtm':y['mtm_USDT'],
                'delta':y['mtm_USDT']-x['mtm_USDT'],'delta_after5':y['mtm_after5']-x['mtm_after5'],
                'delta_after10':y['mtm_after10']-x['mtm_after10'],
                'base_positive':x['positive_base'],'new_positive':y['positive_base'],
                'route_deltas':{sym:y['routes'][sym]['mtm']-x['routes'][sym]['mtm'] for sym in x['routes']}})
        delta=sum(x['delta'] for x in rr)
        assert np.isclose(delta,float(snapshots[new]['metrics']['net_profit'])-float(snapshots[base]['metrics']['net_profit']),atol=1e-6,rtol=1e-9)
        paired[base+'__'+new]={'delta':delta,'months_improve':sum(x['delta']>0 for x in rr),
                              'rescued_negative_to_positive':[x['month'] for x in rr if not x['base_positive'] and x['new_positive']],
                              'lost_positive_to_nonpositive':[x['month'] for x in rr if x['base_positive'] and not x['new_positive']]}
        Path('output/'+base+'__'+new+'_month_deltas.json').write_text(json.dumps(rr,separators=(',',':'),allow_nan=False))
    Path('output/r3_month_diagnostic_summary.json').write_text(json.dumps({'sessions':summaries,'comparisons':paired},indent=2,allow_nan=False))
    print('R3_MONTH_DIAGNOSTICS',json.dumps({'names':names,'comparisons':paired,'counts':{n:s['samples']['included63']['class_counts'] for n,s in summaries.items()}},allow_nan=False))

r3_month_diagnostics(NAMES_PLACEHOLDER)


```

## R9ValidateFunction

```javascript
function validR9(s,d){
 const f=s.state.form,syms=["BTC-USDT","PAXG-USDT","SPY-USDT"],cl=[d.strategy,"PortComparePaxgMarket4h",d.portfolio==="B"?"PortCompareSpySecond4h":"PortCompareSpyMarket4h"];
 const v={name:d.name,status:s.status,dates:f.start_date==="2020-10-15"&&f.finish_date==="2025-12-31",routes:f.routes.length===3&&f.routes.every((x,i)=>x.exchange==="Binance Perpetual Futures"&&x.symbol===syms[i]&&x.timeframe==="4h"&&x.strategy===cl[i]),feeds:f.data_routes.length===3&&f.data_routes.every((x,i)=>x.exchange==="Binance Perpetual Futures"&&x.symbol===syms[i]&&x.timeframe==="1m"),settings:f.config.exchange.balance===10000&&f.config.exchange.fee===d.fee&&f.config.exchange.futures_leverage===5&&f.config.exchange.futures_leverage_mode==="isolated"&&f.config.warm_up_candles===240&&f.debug_mode===true&&f.fast_mode===false&&f.export_chart===true,sources:cl.map((c,i)=>(s.strategy_codes["Binance Perpetual Futures-"+syms[i]]??s.strategy_codes[c])===(i===0?(d.source||load("R9Sources")[c]||load("R8Sources")[c]||load("N204R6BaseSources")[c]):load("N204R6BaseSources")[c]))};
 if(!v.dates||!v.routes||!v.feeds||!v.settings||v.sources.some(x=>!x))throw Error("R9contract "+JSON.stringify(v));
 const checks=load("R9FormChecks")||{};checks[d.id]=v;store("R9FormChecks",checks);return v;
}
```

## R9CreatePairFunction

```javascript
async function createR9Pair(batch,strategy,fee,recipe,role="validation",tp=2){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text),base=load("R8Sources")[strategy]||load("R9Sources")[strategy]||load("N204R6BaseSources")[strategy];if(!base)throw Error("unknownsource");
 const reg=load("R9Registry");
 for(const p of ["B","C"]){
 const template=load("R9Template"+p),f=JSON.parse(JSON.stringify(template));f.config.exchange.fee=fee;f.routes[0].strategy=strategy;
 const made=dec(await tools.mcp__jesse_local__create_backtest_draft({exchange:f.exchange,routes:JSON.stringify(f.routes),data_routes:JSON.stringify(f.data_routes),start_date:f.start_date,finish_date:f.finish_date,debug_mode:true,export_chart:true,fast_mode:false,benchmark:false,title:"BTC R9 "+batch+p+" "+role,description:"Frozen R9;2026closed; same shared-risk portfolio; single declared stress/variant."}));
 if(!made.backtest_id)throw Error(JSON.stringify(made));const id=made.backtest_id,d={name:batch+p,id,url:made.dashboard_url,strategy,seed:"Y902",portfolio:p,fee,recipe,role,tp,source:base,status:"draft"};reg.push(d);store("R9Registry",reg);
 const ss=dec(await tools.mcp__jesse_local__get_backtest_session({session_id:id}));if(ss.error)throw Error(JSON.stringify(ss));const state=ss.data.session.state;state.form=f;
 const u=dec(await tools.mcp__jesse_local__update_backtest_draft({backtest_id:id,state:JSON.stringify(state)}));if(u.status==="error")throw Error(JSON.stringify(u));
 const s=dec(await tools.mcp__jesse_local__get_backtest_session({session_id:id}));eval("("+load("R9ValidateFunction")+")")(s.data.session,d);
 }
 return reg.filter(x=>x.name===batch+"B"||x.name===batch+"C").map(x=>({name:x.name,id:x.id,url:x.url}));
}
```

## R9SyncFunction

```javascript
async function syncR9(){
const d=r=>JSON.parse(r.content.find(x=>x.type==="text").text),reg=load("R9Registry"),r=d(await tools.mcp__jesse_local__get_backtest_sessions({title_search:"R9",limit:100}));if(r.status!=="success")throw Error(JSON.stringify(r));
for(const s of r.sessions){const cl=s.state.form.routes[0].strategy;let entry=reg.find(x=>x.id===s.id);if(!entry){const m=cl.match(/^BtcY902ExploreR(100[1-5])$/);if(!m)continue;const p=s.state.form.routes[2].strategy==="PortCompareSpySecond4h"?"B":"C";entry={name:"K"+m[1]+p,id:s.id,url:s.dashboard_url,strategy:cl,source:load("R9Sources")[cl],seed:"Y902",portfolio:p,fee:.00045,recipe:"K"+m[1],tp:2,role:"exploration"};reg.push(entry);}eval("("+load("R9ValidateFunction")+")")(s,entry);entry.status=s.status;}
store("R9Registry",reg);const active=reg.filter(x=>["running","pending"].includes(x.status));if(active.length>4||["validation","exploration"].some(role=>active.filter(x=>x.role===role).length>2))throw Error("capacity");return{registered:reg.length,active:active.map(x=>x.name),finished:reg.filter(x=>x.status==="finished").map(x=>x.name),failed:reg.filter(x=>!["draft","running","pending","finished"].includes(x.status)).map(x=>({name:x.name,status:x.status}))};
}
```

## R9StartFunction

```javascript
async function startR9(batch,names){
 function dec(r){return JSON.parse(r.content.find(x=>x.type==="text").text)}
 const all=[...load("R9Registry"),...load("R9References")];
 await Promise.all(names.map(async name=>{const d=all.find(x=>x.name===name);if(!d)throw Error("unknown "+name);const s=dec(await tools.mcp__jesse_local__get_session_results({session_type:"backtest",session_id:d.id,section:"summary"}));if(s.session_status!=="finished"||s.error)throw Error("not finished clean "+name);store("R9Summary"+name,s);}));
 const r=dec(await tools.mcp__jesse_local__run_analysis({code:load("R9AuditTemplate").replaceAll("NAMES_PLACEHOLDER",JSON.stringify(names)),inputs:[...load("mtminputs").slice(0,4),...names.map(name=>({name,session_type:"backtest",session_id:all.find(x=>x.name===name).id}))],timeout_minutes:5}));
 if(r.status!=="success"||!r.job){store("R9AnalysisLastStartResponse",r);if(r.error_type==="too_many_jobs")return{batch,deferred:true,reason:r.error_type};throw Error("analysis start "+JSON.stringify(r));}
 const j=load("R9Jobs");j.push({batch,names,job:r.job.id,status:r.job.status});store("R9Jobs",j);return{batch,job:r.job.id,status:r.job.status};
}
```

## R9HarvestFunction

```javascript
async function harvestR9(batch){
 function dec(r){return JSON.parse(r.content.find(x=>x.type==="text").text)}
 const jobs=load("R9Jobs"),j=jobs.find(x=>x.batch===batch),aud=load("R9Audits")||{},months=load("R9Months")||{},rows=load("R9MonthRows")||{};
 const st=dec(await tools.mcp__jesse_local__get_analysis_job({job_id:j.job,tail_lines:3}));if(st.job.status!=="succeeded")return {batch,status:st.job.status,output:st.output};
 const fetch=async path=>{const r=dec(await tools.mcp__jesse_local__get_analysis_artifact({job_id:j.job,path:"output/"+path}));if(r.truncated)throw Error("artifact truncated "+path);return JSON.parse(r.content)};
 await Promise.all(j.names.map(async n=>{const [a,m,r]=await Promise.all([fetch(n+"_summary.json"),fetch(n+"_r3_month_summary.json"),fetch(n+"_r3_month_rows.json")]);aud[n]=a;months[n]=m;rows[n]=r;}));
 const global=await fetch("r3_month_diagnostic_summary.json");
 store("R9Audits",aud);store("R9Months",months);store("R9MonthRows",rows);store("R9MonthPairs"+batch,global.comparisons);
 j.status="succeeded";store("R9Jobs",jobs);
 const all=[...load("R9References"),...load("R9Registry")];
 const content="# BTC R9 — "+batch+"\n\n2026 cerrado; muestra de desarrollo2020-10-15→2025-12-31 exclusiva. Auditoría de fills, cantidades, fees,PNL,wallet yterminal, con MTM UTC diario. Costes+5/+10 adicionales al fee de CADA sesión, sobre recorridos y cantidades fijos; no confundir overlays de sesiones ya estresadas con el estrés original. Monthclassallcalendar, denominadores activos se conservan en auditoría.\n\n"+j.names.map(n=>"## ["+n+"]("+all.find(x=>x.name===n).url+")\n\n```json\n"+JSON.stringify({audit:aud[n],month_diagnostics:months[n]},null,2)+"\n```").join("\n\n")+"\n\n## Comparaciones por mes\n```json\n"+JSON.stringify(global.comparisons,null,2)+"\n```";
 const saved=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R9_AUDIT_"+batch+"_20261019.md",content,overwrite:true}));
 return {batch,status:"succeeded",report:saved.path,rows:j.names.map(n=>({name:n,net:aud[n].net,classes:months[n].samples.included63.class_counts,negSum:months[n].samples.included63.sum_negative_months,flip5:months[n].samples.included63.stress["5"].flip_months}))};
}
```

## R9PathFunction

```javascript
async function pathR9(batch){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text);
 const j=load("R9Jobs").find(x=>x.batch===batch),checks=load("R9PathChecks")||{};
 for(const n of j.names){
  let r=dec(await tools.mcp__jesse_local__get_analysis_artifact({job_id:j.job,path:n+"_path.json"})),a;
  if(r.truncated){
   const mr=dec(await tools.mcp__jesse_local__get_analysis_artifact({job_id:j.job,path:n+"_path_manifest.json"}));if(mr.truncated)throw Error("manifest truncated");
   const m=JSON.parse(mr.content);a=[];
   for(const part of m.parts){const p=dec(await tools.mcp__jesse_local__get_analysis_artifact({job_id:j.job,path:part}));if(p.truncated)throw Error("part truncated");a.push(...JSON.parse(p.content));}
   if(a.length!==m.rows)throw Error("missing paths");
  }else a=JSON.parse(r.content);
  store(n+"r9path",a);
 }
 for(const n of j.names){
  const a=load(n+"r9path"),b=load("N204"+n.slice(-1)+"r9path");if(!b)continue;
  const key=t=>[t.symbol,t.side,t.open].join("|"),am=new Map(a.map(t=>[key(t),t]));if(am.size!==a.length)throw Error("duplicates");
  const retained=b.filter(t=>am.has(key(t))),longs=b.filter(t=>t.symbol==="BTC-USDT"&&t.side==="long");
  checks[n]={counts:{current:a.length,reference:b.length,retained:retained.length,removed:b.length-retained.length,added:a.length-retained.length},btc_long:{reference:longs.length,retained_entry:longs.filter(t=>am.has(key(t))).length,same_exit:longs.filter(t=>am.get(key(t))?.close===t.close).length},same_exit_retained:retained.filter(t=>am.get(key(t)).close===t.close).length};
 }
 store("R9PathChecks",checks);return j.names.map(n=>({n,check:checks[n]}));
}
```

## R9SleeveMetadataFunction

```javascript
async function sleeveMetadataR9(batch){
 const dec=r=>{const t=r.content?.find(x=>x.type==="text")?.text;if(!t?.trim().startsWith("{"))throw Error("MCPnonJSON logs: "+t);return JSON.parse(t);},reg=[...load("R9Registry"),...load("R9References")],pair=reg.filter(x=>x.name===batch+"B"||x.name===batch+"C"),results=load("R9SleeveMetadata")||{};
 if(pair.length!==2)throw Error("unknown batch");
 for(const d of pair){
  const paths=load(d.name+"r9path");if(!paths)throw Error("financialpathfirst");
  let offset=0,pages=0,more=true,records=[],terminal=[],linesRead=0;
  while(more){
   const r=dec(await tools.mcp__jesse_local__get_session_results({session_type:"backtest",session_id:d.id,section:"logs",offset,limit:500}));
   if(r.status!=="success")throw Error(JSON.stringify(r));pages++;linesRead+=r.items.length;
   for(const line of r.items){
    if(line.includes("BTC_EXPLORE_FILL ")){const x=JSON.parse(line.slice(line.indexOf("BTC_EXPLORE_FILL ")+"BTC_EXPLORE_FILL ".length));if(x.recipe===d.recipe)records.push(x);}
    else if(line.includes("BTC_EXPLORE ")){const x=JSON.parse(line.slice(line.indexOf("BTC_EXPLORE ")+"BTC_EXPLORE ".length));if(x.recipe===d.recipe)terminal.push(x);}
   }
   more=!!r.has_more;
   if(more){if(r.next_offset==null||r.next_offset<=offset||pages>=200)throw Error("incomplete log paging "+d.name);offset=r.next_offset;}
  }
  const errors=[],matches=[],used=new Set();
  for(const t of paths)if(t.symbol==="BTC-USDT"&&t.side==="short")t.sleeve="unknown";
  if(terminal.length!==1)errors.push("terminal_count_"+terminal.length);
  const expected=terminal[0]?.counts?.fills||0,closed=terminal[0]?.counts?.closes||0;
  if(records.length!==expected)errors.push("fill_count_mismatch");
  for(const r of records){
   const candidates=paths.map((t,i)=>({t,i})).filter(({t})=>t.symbol==="BTC-USDT"&&t.side===r.side&&t.open===r.time&&Math.abs(t.entry-r.entry)<=1e-7&&Math.abs(t.qty-r.qty)<=1e-7);
   if(candidates.length!==1||used.has(candidates[0]?.i)){errors.push("nonbijective_fill_"+r.time);continue;}
   if(!(Number.isFinite(r.distance)&&r.distance>0&&Math.abs(r.target_distance-(d.tp||2)*r.distance)<=1e-7)){errors.push("target_geometry_"+r.time);continue;}
   if(d.strategy!=="X03ExploreR204"&&!(Number.isFinite(r.requested_entry)&&r.requested_entry>0&&Number.isFinite(r.signal_anchor)&&r.signal_anchor>0)){errors.push("missing_requested_metadata_"+r.time);continue;}
   const {t,i}=candidates[0];used.add(i);t.sleeve="supplement";matches.push({open:t.open,entry:t.entry,qty:t.qty,entry_type:t.entry_type,recipe:r.recipe,requested_entry:r.requested_entry,signal_anchor:r.signal_anchor,distance:r.distance,target_distance:r.target_distance});
  }
  if(matches.length!==expected)errors.push("matched_count_mismatch");
  const finishMs=Date.parse(load("R9Summary"+d.name).form.finish_date+"T00:00:00Z"),boundarySupp=[...used].filter(i=>paths[i].close===finishMs).length;
  let boundaryAdjustment=0;
  if(closed!==expected){
   if(closed+boundarySupp===expected&&load("R9Audits")[d.name].mtm.terminal_reconciles)boundaryAdjustment=boundarySupp;
   else errors.push("close_count_not_reconciled");
  }
  const ok=errors.length===0;
  if(ok)for(const t of paths)if(t.symbol==="BTC-USDT"&&t.side==="short"&&t.sleeve==="unknown")t.sleeve="original";
  store(d.name+"r9path",paths);
  results[d.name]={ok,pages,lines_read:linesRead,log_fill_count:records.length,terminal_fills:expected,terminal_closes:closed,boundary_supplement_closes:boundarySupp,boundary_counter_adjustment:boundaryAdjustment,matched:matches.length,errors,observed_supplement_entry_types:Object.fromEntries([...new Set(matches.map(x=>x.entry_type))].map(type=>[type,matches.filter(x=>x.entry_type===type).length])),matches,note:"Metadata reconciliation of complete MCP logs against run_analysis financial paths; not a second financial calculation. STOP type alone never identifies original sleeve."};
 }
 store("R9SleeveMetadata",results);
 const content="# BTC R9 — "+batch+" identificación de suplementos\n\nSe paginaron logs MCP completos de sesionesfinalizadas, sinestimarlos. Conciliaciónbijectiva deBTC_EXPLORE_FILLconpathsdelanálisisfinancieroporclock/entry/qty1e-7ygeometría TP declarada. Etiquetasmetadata, no recalcularPNL ni inferirSTOPoriginalpormerotipo. Error/faltantesbloqueaelegibilidad; no imputaunknown. Losimportesdefills/fees/wallet/MTMson del auditorrun_analysis.\n\n"+pair.map(d=>"## ["+d.name+"]("+d.url+")\n\n```json\n"+JSON.stringify(results[d.name],null,2)+"\n```").join("\n\n");
 const saved=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R9_"+batch+"_SLEEVE_IDENTIFICATION_20261019.md",content,overwrite:false}));
 if(saved.status!=="success")throw Error(JSON.stringify(saved));return pair.map(d=>({name:d.name,ok:results[d.name].ok,matched:results[d.name].matched,types:results[d.name].observed_supplement_entry_types,errors:results[d.name].errors,path:saved.path}));
}
```

## R9MatrixFunction

```javascript
async function matrixR9(final=false){
 const d=r=>JSON.parse(r.content.find(x=>x.type==="text").text),reg=load("R9Registry"),aud=load("R9Audits"),metadata=load("R9SleeveMetadata"),month=load("R9Months");
 if(final&&(reg.length!==20||reg.some(x=>x.status!=="finished"||!aud[x.name]||!load(x.name+"r9path"))))throw Error("incompleteR9");
 const out=[];const key=t=>[t.symbol,t.side,t.entry_type,t.open].join("|");
 for(const r of reg){const a=aud[r.name],p=r.portfolio;if(!a){out.push({name:r.name,pending:true});continue;}
 const ref=r.name.startsWith("F70")?"N70"+p:r.name.startsWith("F95")?"N95"+p:"N204"+p,b=aud[ref],paths=load(r.name+"r9path"),old=load("Y902"+p+"r9path");
 let diversity=null,typed=null;if(metadata[r.name]?.ok&&paths&&old){
 const oldS=old.filter(t=>t.sleeve==="supplement"),newS=paths.filter(t=>t.sleeve==="supplement"),om=new Map(oldS.map(t=>[key(t),t])),nm=new Map(newS.map(t=>[key(t),t]));
 const entryChanges=oldS.filter(t=>!nm.has(key(t))).length+newS.filter(t=>!om.has(key(t))).length+newS.filter(t=>om.has(key(t))&&Math.abs(t.entry-om.get(key(t)).entry)>1e-7).length,exitChanges=newS.filter(t=>{const o=om.get(key(t));return o&&Math.abs(t.entry-o.entry)<=1e-7&&(o.close!==t.close||Math.abs(o.exit-t.exit)>1e-7)}).length;
 diversity={entry_changes:entryChanges,matched_exit_changes:exitChanges};typed=metadata[r.name].observed_supplement_entry_types;
 }
 const f=a.cost_calendar["5"].complete_periods,i=a.cost_calendar["5"].partial_periods;
 const m=month[r.name].samples.included63;
 const obj={name:r.name,url:r.url,role:r.role,fee:r.fee,net:a.net,dd:a.dd_engine,reference:ref,delta_reference:b?a.net-b.net:null,plus10:a.plus10_samefills,months_nominal_calendar:m.positive_months+"/63",months_plus5_active:i.positive_months+"/"+i.months_active,months_plus5_calendar:i.positive_months+"/"+i.months_total,quarters_plus5:i.positive_quarters+"/"+i.quarters_total,diversity,metadata_ok:r.name.startsWith("N95")?true:metadata[r.name]?.ok??null,supplement_fills:metadata[r.name]?.matched,types:typed};
 if(r.role==="exploration"&&aud["Y902"+p]){const y=aud["Y902"+p];obj.delta_Y902=a.net-y.net;obj.delta_plus10_Y902=a.plus10_samefills-y.plus10_samefills;obj.screen={nominal_better_Y902:obj.delta_Y902>1e-7,cost10_atleast_Y902:obj.delta_plus10_Y902>=-1e-7,dd:a.dd_engine>=-25,supplement_atleast30:obj.supplement_fills>=30,mechanism_changes_atleast10:!!diversity&&(r.recipe==="K1001"||r.recipe==="K1002"?diversity.entry_changes:diversity.matched_exit_changes)>=10,metadata:!!obj.metadata_ok,calendar_full_and_included:f.win_months_active>=.65&&i.win_months_active>=.65&&f.win_quarters>=.8&&i.win_quarters>=.8};}
 out.push(obj);
 }
 store("R9Matrix",out);
 const table=["|Prueba|Fee por lado|Neto USDT|DD motor%|Referencia de Δ|Δneto|M positivos nominal/calendario|M +5 activos / calendario|Q+5|Suplfills|","|---|---:|---:|---:|---|---:|---|---|---|---:|"];
 for(const x of out)if(!x.pending)table.push(`|[${x.name}](${x.url})|${x.fee}|${x.net.toFixed(6)}|${x.dd.toFixed(4)}|${x.reference}|${x.delta_reference?.toFixed(6)??"pendiente"}|${x.months_nominal_calendar}|${x.months_plus5_active} / ${x.months_plus5_calendar}|${x.quarters_plus5}|${x.supplement_fills??"pendiente"}|`);
 const content="# BTC R9 — matriz "+(final?"final":"parcial")+"\n\n2026 cerrado. Fee engine por lado explícito; +5/+10 son overlays ADICIONALES al fee de esa fila, sobre fills/cantidades fijos. F70 se compara N70 y F95 con N95 a fee iguales. N95 es referencia nueva y su Δ frente a N204 nominal refleja cambiofee, no una variante ganadora. TPvecinos son sensibilidad, no candidatos seleccionables. Exploraciones Kse comparan conY902 yN204nominales y no se promocionan automáticamente. Denominadores activos/calendar se muestran por separado. Una fuente protegida no garantiza idénticas ejecuciones por ocupación/capital. No OOS ni pruebaanti-overfit.\n\n"+table.join("\n")+"\n\n```json\n"+JSON.stringify(out,null,2)+"\n```\n";
 const saved=d(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R9_RESULTS_MATRIX_20261019.md",content,overwrite:!!load("R9MatrixSaved")}));if(saved.status!=="success")throw Error(JSON.stringify(saved));store("R9MatrixSaved",saved);return{path:saved.path,audited:out.filter(x=>!x.pending).length,pending:out.filter(x=>x.pending).map(x=>x.name)};
}
```

## R9FinalSourceFunction

```javascript
async function finalSourcesR9(){
 const dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text);
 const sources={...load("N204R6BaseSources"),N204ExploreR503:load("R6BaseN503"),...Object.fromEntries(Object.values(load("N204R6Recipes")).flat().map(x=>[x.strategy,load("R6Source"+x.strategy)])),...load("R7Sources"),...load("R8Sources"),...load("R9Sources")};
 const results=await Promise.allSettled(Object.entries(sources).map(async([name,source])=>{
  const r=dec(await tools.mcp__jesse_local__read_strategy({name}));if(r.status!=="success"||r.content!==source)throw Error("sourcechanged "+name);
  return {name,exact:true,chars:source.length};
 }));
 store("R9FinalSourceChecks",results);
 if(results.some(x=>x.status!=="fulfilled"))throw Error(JSON.stringify(results));
 return results.map(x=>x.value);
}
```

## R9FinalManifestFunction

```javascript
async function manifestR9(){
 const reg=load("R9Registry"),f=load("R9FormChecks"),a=load("R9Audits"),jobs=load("R9Jobs"),m=load("R9SleeveMetadata"),s=load("R9FinalSourceChecks"),dec=r=>JSON.parse(r.content.find(x=>x.type==="text").text);
 if(reg.length!==20||reg.some(x=>x.status!=="finished"||a[x.name]?.audit!=="passed"||!a[x.name]?.mtm.terminal_reconciles)||jobs.length!==10||jobs.some(x=>x.status!=="succeeded")||!s||s.some(x=>x.status!=="fulfilled"))throw Error("R9unfinished");
 for(const x of reg){const c=f[x.id];if(!c||!c.dates||!c.routes||!c.feeds||!c.settings||c.sources.length!==3||c.sources.some(b=>!b))throw Error("form"+x.name);if(!x.name.startsWith("N95")&&!m[x.name]?.ok)throw Error("metadata"+x.name);}
 const manifest={round:"R9",development_only:true,closed_2026:true,nominal_reference_fee:.00045,total_new_fulls:20,root_validation:10,exploration:10,forms:20,snapshots:60,registry:reg.map(({source,...rest})=>({...rest,source_chars:source.length})),source_checks:s.map(x=>x.value),form_checks:Object.fromEntries(reg.map(x=>[x.id,f[x.id]])),financial_jobs:jobs,financial_checks:reg.map(x=>({name:x.name,audit:a[x.name].audit,terminal:a[x.name].mtm.terminal_reconciles})),sleeve_metadata:Object.fromEntries(reg.filter(x=>m[x.name]).map(x=>{const y=m[x.name];return[x.name,{ok:y.ok,pages:y.pages,lines_read:y.lines_read,log_fills:y.log_fill_count,matched:y.matched,types:y.observed_supplement_entry_types,boundary_adjustment:y.boundary_counter_adjustment,errors:y.errors}]})),qa:{tp_final:{checks:load("R9TPQAFinal")?.count,job:load("R9TPQAFinalJob")},exploratory:{checks:230,job:"c568aedf303a420a90d74a2d0f2a391d"}},data_handling:{snapshot_key_formats:["exchange-symbol","class"],root_report_page_join_correction:load("R9KPageJoinCorrection"),sources_not_changed_by_correction:true},selection:"Diagnostics and candidates only; no live promotion, no TP-neighbour selection; no additional backtests."};
 const content="# BTC R9 — manifiesto final\n\n20 nuevas corridas terminadas y auditadas,60snapshots,10jobs financieros (el primero incluye2referencias reutilizadas adicionales),"+s.length+"fuentes exactas finales de bases/rondas preservadas yR9. Fuentes originales sin cambios; 2026cerrado. QA es verificación sintética y de fuente, no prueba estadística. Los resultados de incertidumbre se guardan en BTC_R9_UNCERTAINTY_RESULTS_20261019.md con sus propios3jobs descriptivos.\n\n```json\n"+JSON.stringify(manifest,null,2)+"\n```\n";const r=dec(await tools.mcp__jesse_local__save_strategy_report({strategy_name:"MultiAssetRetestBtcShort4h",filename:"BTC_R9_FINAL_MANIFEST_20261019.md",content,overwrite:false}));if(r.status!=="success")throw Error(JSON.stringify(r));store("R9FinalManifest",r);return{path:r.path,new_fulls:20,source_checks:s.length,financial_jobs:jobs.length};
}
```
