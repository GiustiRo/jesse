"""Calendar-close MTM auditor for Jesse snapshot inputs.

Use run_analysis with this module INLINE, followed by main_mtm(names).
inputs/benchmarks.json must include buy-and-hold curves for the same immutable
exchange/symbol price series. Other snapshots supply midnight MARKET fills to
recover the price scale, checked against at least two distinct fills per market.
No database, credentials, network, or source CSV access is needed.

Only complete, flat-terminal sessions with one full entry/exit per trade are
supported. Prices use observed UTC daily closes, carrying the last observed mark
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
    anchors = {}
    for name, snapshot in snapshots.items():
        if name == benchmark_name:
            continue
        for trade in snapshot.get('trades', []):
            for order in trade.get('orders', []):
                stamp = order.get('executed_at')
                if str(order.get('type')).upper() != 'MARKET' or stamp is None or int(stamp) % DAY_MS:
                    continue
                symbol = order['symbol']
                day = pd.Timestamp(int(stamp), unit='ms', tz='UTC') - pd.Timedelta(days=1)
                if symbol in observed and day in observed[symbol].index:
                    anchors.setdefault(symbol, {})[order['id']] = float(order['price']) / float(observed[symbol].loc[day])
    prices, diagnostics = {}, {}
    for symbol, series in observed.items():
        ratios = np.array(list(anchors.get(symbol, {}).values()))
        if len(ratios) < 2:
            raise ValueError('At least two independent midnight MARKET anchors required: ' + symbol)
        scale = float(np.median(ratios))
        if not np.allclose(ratios, scale, rtol=SCALE_RTOL, atol=0):
            raise ValueError('Anchors do not match benchmark price basis: ' + symbol)
        prices[symbol] = series * scale
        diagnostics[symbol] = {'anchor_count': len(ratios), 'scale': scale,
                               'max_relative_error': float(np.max(np.abs(ratios / scale - 1)))}
    return prices, diagnostics


def _returns(equity, initial, frequency):
    end = equity.resample(frequency).last()
    previous = end.shift(1)
    previous.iloc[0] = initial
    return end / previous - 1, previous


def audit_mtm(snapshot, prices, name='session'):
    metrics = snapshot['metrics']
    if metrics['total_open_trades'] != 0:
        raise ValueError('Open terminal positions are absent from the snapshot; reconstruction refused')
    form = snapshot['summary']['form']
    initial = float(metrics['starting_balance'])
    fee_rate = float(form['config']['exchange']['fee'])
    days = pd.date_range(pd.Timestamp(form['start_date'], tz='UTC'),
                         pd.Timestamp(form['finish_date'], tz='UTC') - pd.Timedelta(days=1), freq='D')
    valuation = (days + pd.Timedelta(days=1)).asi8 // 1_000_000
    trades = snapshot['trades']
    by_route = {}
    active = set()
    for trade in trades:
        # Subtract one millisecond to give end-of-minute midnight executions the
        # same right-edge calendar convention as the daily-close valuations.
        left = pd.Timestamp(int(trade['opened_at']), unit='ms') - pd.Timedelta(milliseconds=1)
        right = pd.Timestamp(int(trade['closed_at']), unit='ms') - pd.Timedelta(milliseconds=1)
        active.update(pd.period_range(left.to_period('M'), right.to_period('M'), freq='M'))
    for symbol in sorted({trade['symbol'] for trade in trades}):
        source = prices[symbol]
        # Include prior observations before slicing, so a holiday at window start
        # gets its last known mark rather than inventing a tradable price candle.
        marks = source.reindex(source.index.union(days)).sort_index().ffill().reindex(days)
        if marks.isna().any():
            raise ValueError('No observed mark at start: ' + symbol)
        total = np.zeros(len(days))
        for trade in trades:
            if trade['symbol'] != symbol:
                continue
            executed = [o for o in trade['orders'] if str(o.get('status')).upper() == 'EXECUTED']
            if len(executed) != 2 or sum(not bool(o.get('reduce_only')) for o in executed) != 1:
                raise ValueError('Partial exits or pyramiding require an order-level MTM path')
            quantity = abs(float(trade['qty']))
            entry, exit_price = float(trade['entry_price']), float(trade['exit_price'])
            sign = 1 if trade['type'] == 'long' else -1
            fee = float(trade['fee'])
            expected_fee = quantity * (entry + exit_price) * fee_rate
            expected_pnl = sign * quantity * (exit_price - entry) - fee
            if not np.isclose(fee, expected_fee, rtol=1e-8, atol=1e-6):
                raise ValueError('Variable or missing fee model')
            if not np.isclose(expected_pnl, trade['PNL'], rtol=1e-8, atol=1e-6):
                raise ValueError('Trade PNL does not reconcile at constant position quantity')
            live = (valuation >= int(trade['opened_at'])) & (valuation < int(trade['closed_at']))
            done = valuation >= int(trade['closed_at'])
            total[live] += sign * quantity * (marks.to_numpy()[live] - entry) - quantity * entry * fee_rate
            total[done] += float(trade['PNL'])
        by_route[symbol] = total
    routes = pd.DataFrame(by_route, index=days)
    expected = sum(float(trade['PNL']) for trade in trades)
    if not np.isclose(routes.iloc[-1].sum(), expected, rtol=1e-9, atol=1e-6):
        raise ValueError('Terminal route PNL mismatch')
    if not np.isclose(initial + expected, metrics['finishing_balance'], rtol=1e-9, atol=1e-6):
        raise ValueError('Terminal wallet mismatch')
    equity = initial + routes.sum(axis=1)
    monthly, previous = _returns(equity, initial, 'ME')
    quarterly, _ = _returns(equity, initial, 'QE')
    yearly, _ = _returns(equity, initial, 'YE')
    route_months = routes.resample('ME').last()
    delta = route_months.diff()
    if not delta.empty:
        delta.iloc[0] = route_months.iloc[0]
    contributions = delta.div(previous, axis=0)
    if not np.allclose(contributions.sum(axis=1), monthly, atol=1e-10):
        raise ValueError('Monthly contributions do not reconcile to portfolio return')
    mask = np.array([date.tz_localize(None).to_period('M') in active for date in monthly.index])
    corr = contributions.corr()
    corr_dict = corr.astype(object).where(pd.notna(corr), None).to_dict()
    peaks = np.maximum.accumulate(np.r_[initial, equity.to_numpy()])[1:]
    result = {'name': name, 'method': 'UTC day-close MTM, right-edge inclusive',
              'partial_boundary_periods_included': True,
              'months_total': len(monthly), 'months_active': int(mask.sum()),
              'win_months_all': float((monthly > 0).mean()),
              'win_months_active': float((monthly[mask] > 0).mean()) if mask.any() else None,
              'win_quarters': float((quarterly > 0).mean()),
              'worst_month': [str(monthly.idxmin()), float(monthly.min())],
              'worst_quarter': [str(quarterly.idxmin()), float(quarterly.min())],
              'daily_close_drawdown_pct': float((equity.to_numpy() / peaks - 1).min() * 100),
              'mtm_route_contribution_correlation': corr_dict,
              'yearly_returns': {str(key): float(value) for key, value in yearly.items()},
              'terminal_reconciles': True}
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
    # A cross-month open trade must be marked before it closes; counting only
    # realized PNL would incorrectly assign all profit to February.
    days = pd.date_range('2021-01-30', '2021-02-02', freq='D', tz='UTC')
    trades = [{'symbol': 'X-USD', 'qty': 1, 'entry_price': 100, 'exit_price': 110,
               'type': 'long', 'fee': .21, 'PNL': 9.79,
               'opened_at': int(pd.Timestamp('2021-01-31T12:00:00Z').timestamp()*1000),
               'closed_at': int(pd.Timestamp('2021-02-02T12:00:00Z').timestamp()*1000),
               'orders': [{'status': 'EXECUTED', 'reduce_only': False},
                          {'status': 'EXECUTED', 'reduce_only': True}]}]
    snapshot = {'metrics': {'starting_balance': 10000, 'finishing_balance': 10009.79,
                            'total_open_trades': 0},
                'summary': {'form': {'start_date': '2021-01-31', 'finish_date': '2021-02-03',
                                    'config': {'exchange': {'fee': .001}}}},
                'trades': trades}
    prices = {'X-USD': pd.Series([100, 105, 110, 110], index=days)}
    result, monthly, contributions, equity = audit_mtm(snapshot, prices)
    assert np.isclose(monthly.iloc[0], 4.9/10000)
    assert np.isclose(equity.iloc[-1], 10009.79)
    assert np.isclose(np.prod(1+monthly), 10009.79/10000)
    # Closing exactly at the February boundary belongs to the January close.
    trade = trades[0]
    trade.update(exit_price=105, fee=.205, PNL=4.795,
                 closed_at=int(pd.Timestamp('2021-02-01T00:00:00Z').timestamp()*1000))
    snapshot['metrics']['finishing_balance'] = 10004.795
    result, monthly, _, _ = audit_mtm(snapshot, prices)
    assert result['months_active'] == 1
    assert np.isclose(monthly.iloc[1], 0)
    assert np.isclose(monthly.iloc[0], 4.795/10000)
    # Empty portfolios remain flat and are never assigned invented winning months.
    snapshot['trades'] = []
    snapshot['metrics']['finishing_balance'] = 10000
    result, _, _, _ = audit_mtm(snapshot, prices)
    assert result['months_active'] == 0 and result['win_months_all'] == 0
    print('MTM_SELF_TEST_PASS')


if __name__ == '__main__':
    main_mtm(tuple(sys.argv[1:]) or ('combined',))
