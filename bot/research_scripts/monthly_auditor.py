"""Auditor de Consistencia Mensual (Fase 2).

Audits one or more stored Jesse backtest sessions for month-to-month regularity instead of
headline CAGR alone. It reads the snapshot JSON that the MCP `run_analysis` tool writes to
`inputs/<name>.json` (keys: `summary`, `metrics`, `trades`, `equity_curve`), so it never
touches the database or credentials and can also run locally on an exported snapshot.

Usage
-----
* Through MCP `run_analysis` (recommended; runs inside the Jesse container)::

      code = "exec(open('/src/bot/research_scripts/monthly_auditor.py').read()); main()"
      inputs = [{"session_type": "backtest", "session_id": "<uuid>", "name": "phase1"}]

  `main()` with no arguments audits every backtest snapshot found in `inputs/`.
* Locally: ``python monthly_auditor.py path/to/snapshot.json [...]``.

Metric definitions (deliberate choices, keep in sync with the Phase 2 handoff, section 4.4)
* Monthly/quarterly returns come from the daily "Portfolio" equity curve (month-end over
  previous month-end), so open-position marking is included, not only realized PnL.
* "Active" month = a month during which at least one position was open for some time.
  Win-rate of months is reported over both all months and active months; flat months count
  as non-winning in the "all months" figure because the goal is monthly regularity.
* Per-route monthly contribution = realized PnL of trades closed in that month divided by the
  portfolio equity at the start of the month. Realized attribution is the only per-route
  signal the snapshot carries (Jesse stores one portfolio curve), so route correlations use it.
* Outlier dependency: each trade becomes a return on the equity at its entry day; the trade
  sequence is re-compounded in close order with and without the top-N trades. This isolates
  the contribution of the luckiest trades under compounding sizing, where simply subtracting
  PnL would understate their effect.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

# Targets from the Phase 2 handoff (section 4.4); used only to print PASS/FAIL markers.
TARGET_WIN_MONTHS = 0.65
TARGET_WIN_QUARTERS = 0.80
TARGET_MAX_ROUTE_CORR = 0.25
TOP_N_OUTLIERS = 2


def _realized_series(snapshot: dict) -> pd.Series:
    """Daily realized-only equity rebuilt from closed trades.

    Some stored sessions carry no equity curve. Realized equity ignores open-position marking,
    so months that end inside a trade look flat until it closes; the report flags this source.
    """
    metrics = snapshot.get('metrics') or {}
    start_balance = float(metrics.get('starting_balance') or 0.0)
    form = (snapshot.get('summary') or {}).get('form') or {}
    trades = _trades_frame(snapshot)
    start = pd.Timestamp(form.get('start_date') or trades['opened'].min().date(), tz='UTC')
    finish = pd.Timestamp(form.get('finish_date') or trades['closed'].max().date(), tz='UTC')
    days = pd.date_range(start.floor('D'), finish.floor('D') + pd.Timedelta(days=1), freq='D', tz='UTC')
    pnl = trades.set_index(trades['closed'].dt.ceil('D'))['pnl'].groupby(level=0).sum()
    return start_balance + pnl.reindex(days, fill_value=0.0).cumsum()


def _portfolio_series(snapshot: dict) -> pd.Series:
    curves = snapshot.get('equity_curve') or []
    portfolio = next((c for c in curves if c.get('name') == 'Portfolio'), None)
    if portfolio is None or not portfolio.get('data'):
        snapshot['_equity_source'] = 'realized-from-trades'
        return _realized_series(snapshot)
    snapshot['_equity_source'] = 'portfolio-curve'
    df = pd.DataFrame(portfolio['data'])
    idx = pd.to_datetime(df['time'], unit='s', utc=True)
    s = pd.Series(df['value'].astype(float).values, index=idx).sort_index()
    return s[~s.index.duplicated(keep='last')]


def _trades_frame(snapshot: dict) -> pd.DataFrame:
    trades = snapshot.get('trades') or []
    if not trades:
        return pd.DataFrame(columns=['symbol', 'type', 'pnl', 'opened', 'closed'])
    df = pd.DataFrame(trades)
    out = pd.DataFrame({
        'symbol': df['symbol'],
        'type': df['type'],
        'pnl': df['PNL'].astype(float),
        'opened': pd.to_datetime(df['opened_at'], unit='ms', utc=True),
        'closed': pd.to_datetime(df['closed_at'], unit='ms', utc=True),
    })
    return out.sort_values('closed').reset_index(drop=True)


def _period_returns(equity: pd.Series, start_balance: float, freq: str) -> pd.Series:
    ends = equity.resample(freq).last().dropna()
    prev = ends.shift(1)
    prev.iloc[0] = start_balance
    return ends / prev - 1.0


def _active_months(trades: pd.DataFrame, months: pd.PeriodIndex) -> set:
    active = set()
    for _, t in trades.iterrows():
        for p in pd.period_range(t['opened'].tz_localize(None).to_period('M'),
                                 t['closed'].tz_localize(None).to_period('M'), freq='M'):
            active.add(p)
    return active & set(months)


def _cagr(start: float, end: float, years: float) -> float:
    if start <= 0 or end <= 0 or years <= 0:
        return float('nan')
    return (end / start) ** (1.0 / years) - 1.0


def _outlier_check(trades: pd.DataFrame, equity: pd.Series, start_balance: float, years: float) -> dict:
    if trades.empty:
        return {}
    daily = equity.resample('D').last().ffill()
    rets = []
    for _, t in trades.iterrows():
        # Equity at the close of the day before entry approximates the sizing base.
        day = (t['opened'] - pd.Timedelta(days=1)).floor('D')
        base = daily.asof(day) if day >= daily.index[0] else start_balance
        base = start_balance if (base is None or not math.isfinite(base) or base <= 0) else float(base)
        rets.append(t['pnl'] / base)
    rets = np.array(rets)
    full = start_balance * np.prod(1.0 + rets)
    order = np.argsort(rets)[::-1]
    keep = np.ones(len(rets), dtype=bool)
    keep[order[:TOP_N_OUTLIERS]] = False
    trimmed = start_balance * np.prod(1.0 + rets[keep])
    top_share = trades['pnl'].nlargest(TOP_N_OUTLIERS).sum() / trades['pnl'].sum() if trades['pnl'].sum() > 0 else float('nan')
    return {
        'recompounded_cagr_all': _cagr(start_balance, full, years),
        f'recompounded_cagr_without_top{TOP_N_OUTLIERS}': _cagr(start_balance, trimmed, years),
        f'top{TOP_N_OUTLIERS}_trade_returns_pct': [round(100 * r, 2) for r in rets[order[:TOP_N_OUTLIERS]]],
        f'top{TOP_N_OUTLIERS}_share_of_net_pnl': top_share,
    }


def audit(snapshot: dict, name: str = 'session') -> dict:
    metrics = snapshot.get('metrics') or {}
    equity = _portfolio_series(snapshot)
    trades = _trades_frame(snapshot)
    start_balance = float(metrics.get('starting_balance') or equity.iloc[0])
    years = (equity.index[-1] - equity.index[0]).total_seconds() / (365.25 * 86400)

    m_ret = _period_returns(equity, start_balance, 'ME')
    q_ret = _period_returns(equity, start_balance, 'QE')
    months = m_ret.index.tz_localize(None).to_period('M')
    m_ret.index = months
    q_ret.index = q_ret.index.tz_localize(None).to_period('Q')

    active = _active_months(trades, months)
    active_mask = np.array([p in active for p in months])
    active_rets = m_ret[active_mask]

    # Longest run of consecutive non-positive months (all months, flat months included).
    longest_bad, run = 0, 0
    for r in m_ret.values:
        run = run + 1 if r <= 0 else 0
        longest_bad = max(longest_bad, run)

    # Per-route realized contribution in % of month-start equity.
    month_start_eq = (equity.resample('ME').last().shift(1).fillna(start_balance))
    month_start_eq.index = month_start_eq.index.tz_localize(None).to_period('M')
    route_contrib = pd.DataFrame(index=months)
    trades_per_route = {}
    if not trades.empty:
        trades['month'] = trades['closed'].dt.tz_localize(None).dt.to_period('M')
        for sym, g in trades.groupby('symbol'):
            pnl_m = g.groupby('month')['pnl'].sum().reindex(months, fill_value=0.0)
            route_contrib[sym] = pnl_m / month_start_eq.reindex(months).values
            trades_per_route[sym] = int(len(g))
    corr = route_contrib.corr() if route_contrib.shape[1] > 1 else None

    result = {
        'name': name,
        'equity_source': snapshot.get('_equity_source'),
        'period': f"{equity.index[0].date()} -> {equity.index[-1].date()}",
        'years': round(years, 2),
        'cagr_equity': _cagr(start_balance, float(equity.iloc[-1]), years),
        'jesse_annual_return_pct': metrics.get('annual_return'),
        'max_drawdown_pct': metrics.get('max_drawdown'),
        'months_total': int(len(m_ret)),
        'months_active': int(active_mask.sum()),
        'months_flat': int((~active_mask).sum()),
        'win_months_all': float((m_ret > 0).mean()),
        'win_months_active': float((active_rets > 0).mean()) if len(active_rets) else float('nan'),
        'quarters_total': int(len(q_ret)),
        'win_quarters': float((q_ret > 0).mean()),
        'worst_month': (str(m_ret.idxmin()), float(m_ret.min())),
        'best_month': (str(m_ret.idxmax()), float(m_ret.max())),
        'worst_quarter': (str(q_ret.idxmin()), float(q_ret.min())),
        'median_month': float(m_ret.median()),
        'longest_nonpositive_month_streak': int(longest_bad),
        'trades_total': int(len(trades)),
        'trades_per_year': float(len(trades) / years) if years > 0 else float('nan'),
        'trades_per_month': float(len(trades) / len(m_ret)) if len(m_ret) else float('nan'),
        'trades_per_route': trades_per_route,
        'route_corr': corr.round(3).to_dict() if corr is not None else None,
        'outliers': _outlier_check(trades, equity, start_balance, years),
        'monthly_returns': m_ret,
        'quarterly_returns': q_ret,
        'yearly_returns': _period_returns(equity, start_balance, 'YE'),
    }
    return result


def _pct(x) -> str:
    return 'n/a' if x is None or (isinstance(x, float) and not math.isfinite(x)) else f"{100 * x:.2f}%"


def _mark(ok: bool) -> str:
    return 'PASS' if ok else 'FAIL'


def print_report(r: dict) -> None:
    print(f"\n===== Monthly Consistency Audit: {r['name']} (equity: {r['equity_source']}) =====")
    print(f"Period {r['period']} ({r['years']} y) | CAGR(equity) {_pct(r['cagr_equity'])} | "
          f"Jesse annual {r['jesse_annual_return_pct']} | MaxDD {r['max_drawdown_pct']}")
    print(f"Months: total {r['months_total']}, active {r['months_active']}, flat {r['months_flat']}")
    print(f"Winning months (all)    {_pct(r['win_months_all'])}  [{_mark(r['win_months_all'] >= TARGET_WIN_MONTHS)} >= {_pct(TARGET_WIN_MONTHS)}]")
    print(f"Winning months (active) {_pct(r['win_months_active'])}")
    print(f"Winning quarters        {_pct(r['win_quarters'])}  [{_mark(r['win_quarters'] >= TARGET_WIN_QUARTERS)} >= {_pct(TARGET_WIN_QUARTERS)}]")
    print(f"Worst month {r['worst_month'][0]} {_pct(r['worst_month'][1])} | Best month {r['best_month'][0]} {_pct(r['best_month'][1])} | "
          f"Median month {_pct(r['median_month'])}")
    print(f"Worst quarter {r['worst_quarter'][0]} {_pct(r['worst_quarter'][1])} | Longest non-positive month streak {r['longest_nonpositive_month_streak']}")
    print(f"Trades {r['trades_total']} | per year {r['trades_per_year']:.1f} | per month {r['trades_per_month']:.2f} | per route {r['trades_per_route']}")
    if r['route_corr']:
        corr = pd.DataFrame(r['route_corr'])
        off = corr.where(~np.eye(len(corr), dtype=bool)).abs().max().max()
        print(f"Route monthly-contribution correlation (max |off-diag| {off:.3f}) [{_mark(off < TARGET_MAX_ROUTE_CORR)} < {TARGET_MAX_ROUTE_CORR}]")
        print(corr.to_string())
    o = r['outliers']
    if o:
        print(f"Outlier check: recompounded CAGR all {_pct(o['recompounded_cagr_all'])} -> without top{TOP_N_OUTLIERS} "
              f"{_pct(o[f'recompounded_cagr_without_top{TOP_N_OUTLIERS}'])} | top{TOP_N_OUTLIERS} returns {o[f'top{TOP_N_OUTLIERS}_trade_returns_pct']}% "
              f"| share of net PnL {_pct(o[f'top{TOP_N_OUTLIERS}_share_of_net_pnl'])}")
    print("Yearly returns: " + ", ".join(f"{i.year}: {_pct(v)}" for i, v in r['yearly_returns'].items()))
    # Month grid: rows = year, cols = month, values in %.
    m = r['monthly_returns']
    grid = pd.DataFrame({'year': [p.year for p in m.index], 'month': [p.month for p in m.index], 'ret': (100 * m.values).round(2)})
    print("Monthly returns grid (%):")
    print(grid.pivot(index='year', columns='month', values='ret').to_string())


def main(paths=None) -> list:
    if not paths:
        folder = 'inputs'
        paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder))
                 if f.endswith('.json') and f != 'manifest.json']
    results = []
    for p in paths:
        with open(p, encoding='utf-8') as fh:
            snap = json.load(fh)
        if 'trades' not in snap or 'equity_curve' not in snap:
            continue
        name = os.path.splitext(os.path.basename(p))[0]
        r = audit(snap, name)
        print_report(r)
        results.append(r)
        if os.path.isdir('output'):
            r['monthly_returns'].to_csv(os.path.join('output', f'{name}_monthly_returns.csv'), header=['return'])
    return results


if __name__ == '__main__':
    main(sys.argv[1:] or None)
