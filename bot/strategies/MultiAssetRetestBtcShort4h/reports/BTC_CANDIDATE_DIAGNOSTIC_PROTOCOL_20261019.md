# Diagnóstico de candidatos BTC posterior a R6

Objeto: N204 referencia, N503 y P604 candidatos. P603 sólo contraste previamente auditado de regularidad frente a neto. Sin nuevas estrategias ni backtests en esta etapa. 2026 cerrado incluso a inspección; ventana2020-10-15→2025-12-31 exclusiva.

Diagnóstico con snapshots completos de seis sesiones B/C y cuatro anclas históricas: cohortes suplemento MARKET / corto STOP / largo BTC / otras rutas; concentración por operación y año; mensual MTM nominal y costes extra5/10; comparación con mismos criterios de R6. Emparejar por símbolo/dirección/tipo de entrada/reloj de apertura; separar altas/bajas/cambio de ejecución/cantidad. Descomposición exacta en operaciones emparejadas: cantidad base × cambio PNL unitario + cambio cantidad × PNL unitario nuevo. No equivale a causalidad.

En P604 estudiar las cuatro salidas modificadas y omitir una a una sólo su componente aritmético sobre rutas grabadas, nunca llamar eso rerun. Omitir años o meses es también diagnóstico aritmético, no OOS/validación ni curva operable. No elegir fechas que rescatar ni umbrales tras ver tablas. Esta fase producirá fortalezas/debilidades y próximas hipótesis; no promociona candidatos. Análisis temporal sólo inputs/ y output/ vía run_analysis.

## Fuente completa del análisis

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


# Diagnostic only: recorded paths, no strategy decisions or hypothetical reruns.
NAMES = ['N204B','N204C','N503B','N503C','P604B','P604C']
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

snaps = {p.stem: json.loads(p.read_text()) for p in Path('inputs').glob('*.json') if p.name!='manifest.json'}
prices, anchors = recover_prices(snaps)
result = {'scope':'Reused development sample; 2026 closed; no new backtests; no causal counterfactuals.', 'sessions':{},'comparisons':{},'price_anchors':anchors}
records={}; months={}
def iso(stamp):
    return pd.Timestamp(stamp,unit='ms',tz='UTC').isoformat()
def group(r):
    return r['symbol']+':'+r['side']+':'+r['entry_type']
def stats(rows):
    nets=np.array([r['net'] for r in rows],float)
    stressed=np.array([r['plus10'] for r in rows],float)
    pos=float(nets[nets>0].sum());neg=float(-nets[nets<0].sum())
    top=sorted(rows,key=lambda x:x['net'],reverse=True)[:3]
    return {'n':len(rows),'net':float(nets.sum()),'fees':sum(r['fee'] for r in rows),
      'plus10':float(stressed.sum()),'PF':pos/neg if neg else None,
      'positive':int((nets>0).sum()),'win_rate':float((nets>0).mean()) if len(rows) else None,
      'median_hold_hours':float(np.median([r['hold_hours'] for r in rows])) if rows else None,
      'net_ex_best3_fixed_records':float(nets.sum()-sum(r['net'] for r in top)),
      'plus10_ex_same_best3_fixed_records':float(stressed.sum()-sum(r['plus10'] for r in top)),
      'best3_share_positive_pnl':sum(max(0,r['net']) for r in top)/pos if pos else None}

for name in NAMES:
    snap=snaps[name];form=snap['summary']['form']
    assert form['start_date']=='2020-10-15' and form['finish_date']=='2025-12-31'
    assert snap['summary']['session_status']=='finished'
    fee=float(form['config']['exchange']['fee'])
    rows=[]
    for t in snap['trades']:
        sign,e,outs=_fills(t,fee)
        executed_entries=[o for o in t['orders'] if str(o.get('status')).upper()=='EXECUTED' and not bool(o.get('reduce_only'))]
        turnover=e['qty']*e['price']+sum(o['qty']*o['price'] for o in outs)
        rows.append({'symbol':t['symbol'],'side':t['type'],'open':e['time'],'close':outs[-1]['time'],
          'entry_type':str(executed_entries[0]['type']).upper(),'entry':e['price'],
          'exit':sum(o['qty']*o['price'] for o in outs)/e['qty'],'qty':e['qty'],
          'net':float(t['PNL']),'fee':float(t['fee']),'turnover':turnover,
          'plus10':float(t['PNL'])-.0005*turnover,
          'hold_hours':(outs[-1]['time']-e['time'])/3600000})
    assert np.isclose(sum(r['net'] for r in rows),snap['metrics']['net_profit'],atol=1e-6)
    records[name]=rows
    mtm,mret,contrib,eq=audit_mtm(snap,prices,name)
    daypnl=(eq-float(snap['metrics']['starting_balance']))
    me=daypnl.resample('ME').last()
    mpnl=me.diff();mpnl.iloc[0]=me.iloc[0]
    costs=pd.Series(0.,index=eq.index)
    for t in snap['trades']:
        _,e,outs=_fills(t,fee)
        for f in [e]+outs:
            d=(pd.Timestamp(f['time'],unit='ms',tz='UTC')-pd.Timedelta(milliseconds=1)).normalize()
            costs.loc[d]+=f['qty']*f['price']
    mturn=costs.resample('ME').sum()
    after5=mpnl-.00025*mturn
    months[name]=pd.DataFrame({'nominal':mpnl,'after5':after5,'after10':mpnl-.0005*mturn})
    yearmtm=daypnl.resample('YE').last().diff();yearmtm.iloc[0]=daypnl.resample('YE').last().iloc[0]
    by_group={}
    for g in sorted(set(group(r) for r in rows)):
        gg=[r for r in rows if group(r)==g]
        by_group[g]=stats(gg)
        by_group[g]['closed_years']={str(y):stats([r for r in gg if pd.Timestamp(r['close'],unit='ms',tz='UTC').year==y]) for y in range(2020,2026)}
    result['sessions'][name]={'overall':stats(rows),'by_group':by_group,'engine_dd':snap['metrics']['max_drawdown'],'daily_dd':mtm['daily_close_drawdown_pct'],
      'year_MTM_USDT':{str(k.year):float(v) for k,v in yearmtm.items()},
      'month_after5':{'positive':int((after5>0).sum()),'months':len(after5),
        'already_negative_nominal':int((mpnl<0).sum()),'flipped_by_extra_cost':int(((mpnl>0)&(after5<=0)).sum())}}

def key(r):
    return (r['symbol'],r['side'],r['entry_type'],r['open'])

for p in ('B','C'):
    for base,new in [('N204'+p,'N503'+p),('N503'+p,'P604'+p)]:
        a={key(r):r for r in records[base]};b={key(r):r for r in records[new]}
        assert len(a)==len(records[base]) and len(b)==len(records[new])
        ledger=[];changed=[]
        for k in sorted(a.keys()|b.keys()):
            x=a.get(k);y=b.get(k)
            if x is None:
                ledger.append({'group':group(y),'kind':'added','delta':y['net'],'path_base_qty':0.,'qty_effect':0.,'open':y['open'],'close':y['close']})
            elif y is None:
                ledger.append({'group':group(x),'kind':'removed','delta':-x['net'],'path_base_qty':0.,'qty_effect':0.,'open':x['open'],'close':x['close']})
            else:
                ux=x['net']/x['qty'];uy=y['net']/y['qty']
                path=x['qty']*(uy-ux);size=(y['qty']-x['qty'])*uy
                assert np.isclose(path+size,y['net']-x['net'],atol=1e-7)
                same=x['close']==y['close'] and abs(x['entry']-y['entry'])<=1e-7 and abs(x['exit']-y['exit'])<=1e-7
                ledger.append({'group':group(y),'kind':'same_execution' if same else 'changed_execution','delta':y['net']-x['net'],'path_base_qty':path,'qty_effect':size,'open':y['open'],'close':y['close']})
                if not same:
                    changed.append({'group':group(y),'open':iso(y['open']),'base_close':iso(x['close']),'new_close':iso(y['close']),
                       'base_net':x['net'],'new_net':y['net'],'delta':y['net']-x['net'],
                       'base_qty':x['qty'],'new_qty':y['qty'],'base_hold_h':x['hold_hours'],'new_hold_h':y['hold_hours'],
                       'path_effect_at_base_qty':path,'quantity_effect_at_new_unit_PNL':size,
                       'base_net_bps_entry_notional':1e4*x['net']/(x['qty']*x['entry']),
                       'new_net_bps_entry_notional':1e4*y['net']/(y['qty']*y['entry'])})
        delta=sum(r['delta'] for r in ledger)
        assert np.isclose(delta,result['sessions'][new]['overall']['net']-result['sessions'][base]['overall']['net'],atol=1e-6)
        groups={}
        for g in sorted(set(r['group'] for r in ledger)):
            groups[g]={kind:{'n':len([r for r in ledger if r['group']==g and r['kind']==kind]),
                         'delta':sum(r['delta'] for r in ledger if r['group']==g and r['kind']==kind),
                         'path_base_qty':sum(r['path_base_qty'] for r in ledger if r['group']==g and r['kind']==kind),
                         'quantity_effect':sum(r['qty_effect'] for r in ledger if r['group']==g and r['kind']==kind)}
                     for kind in ('added','removed','same_execution','changed_execution')}
        md=months[new]-months[base];monthly=[]
        for d,row in md.iterrows():
            monthly.append({'month':d.strftime('%Y-%m'),'delta_nominal':float(row['nominal']),'delta_after5':float(row['after5']),'delta_after10':float(row['after10']),
              'base_after5':float(months[base].loc[d,'after5']),'new_after5':float(months[new].loc[d,'after5'])})
        yd=md['nominal'].resample('YE').sum()
        direct=sum(x['path_effect_at_base_qty'] for x in changed)
        fixed_omit=[{'omit_event_open':r['open'],'direct_path_delta_omitting_one':direct-r['path_effect_at_base_qty'],
                     'recorded_portfolio_delta_minus_event_path_component':delta-r['path_effect_at_base_qty']} for r in changed]
        bestmonths=sorted(monthly,key=lambda x:x['delta_nominal'],reverse=True)
        bestevents=sorted(ledger,key=lambda x:x['delta'],reverse=True)
        summary={'base':base,'new':new,'delta':delta,'groups':groups,'changed_same_entry_executions':changed,
           'changed_path_effect_sum_at_base_qty':direct,'omit_one_changed_path_component_arithmetic':fixed_omit,
           'quantity_component_all_matched':sum(x['qty_effect'] for x in ledger),
           'added_and_removed_component':sum(x['delta'] for x in ledger if x['kind'] in ('added','removed')),
           'all_matched_path_component':sum(x['path_base_qty'] for x in ledger),
           'year_delta_MTM':{str(k.year):float(v) for k,v in yd.items()},
           'delta_omitting_each_recorded_year':{str(k.year):delta-float(v) for k,v in yd.items()},
           'months_improve':sum(r['delta_nominal']>1e-7 for r in monthly),'months_worsen':sum(r['delta_nominal']<-1e-7 for r in monthly),
           'extra5_rescued_months':[r for r in monthly if r['base_after5']<=0<r['new_after5']],
           'extra5_lost_months':[r for r in monthly if r['new_after5']<=0<r['base_after5']],
           'delta_without_best_incremental_month_arithmetic':delta-bestmonths[0]['delta_nominal'],
           'best_incremental_month':bestmonths[0],
           'top3_positive_ledger_deltas':[dict(x,open=iso(x['open']),close=iso(x['close'])) for x in bestevents[:3]],
           'limitations':'Accounting decomposition of recorded portfolios, endogenous sizing and occupancy. Omissions do NOT replay execution, capital or gates. No causal or OOS inference; no p-values after selection.'}
        pair=base+'__'+new;result['comparisons'][pair]=summary
        pd.DataFrame(ledger).to_csv('output/'+pair+'_trade_delta_ledger.csv',index=False)
        Path('output/'+pair+'_month_deltas.json').write_text(json.dumps(monthly,indent=2,allow_nan=False))
        Path('output/'+pair+'_comparison.json').write_text(json.dumps(summary,indent=2,allow_nan=False))
        Path('output/'+pair+'_events.json').write_text(json.dumps(changed,indent=2,allow_nan=False))

fig,axes=plt.subplots(2,1,figsize=(11,7),sharex=True)
for ax,p in zip(axes,('B','C')):
    for base,new,label in [('N204','N503','N503 - N204'),('N503','P604','P604 - N503')]:
        ser=(months[new+p]['nominal']-months[base+p]['nominal']).cumsum()
        ax.plot(ser.index,ser.values,label=label)
    ax.axhline(0,color='black',linewidth=.7);ax.set_ylabel('Portfolio '+p+' delta USDT');ax.legend();ax.grid(alpha=.2)
axes[0].set_title('Recorded monthly MTM differences: development sample only')
fig.tight_layout();fig.savefig('output/candidate_incremental_mtm.png',dpi=120);plt.close(fig)
Path('output/diagnostic_summary.json').write_text(json.dumps(result,indent=2,allow_nan=False))
Path('output/session_profiles.json').write_text(json.dumps(result['sessions'],indent=2,allow_nan=False))
print('DIAGNOSTIC_COMPLETE',json.dumps({k:{'delta':v['delta'],'changed':len(v['changed_same_entry_executions']),'direct_path_effect':v['changed_path_effect_sum_at_base_qty'],'year_delta':v['year_delta_MTM']} for k,v in result['comparisons'].items()},allow_nan=False))

```
