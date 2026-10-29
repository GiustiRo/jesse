"""Audit of the Dukascopy LIGHTCMDUSD 1m CSV before import (r49 Fase 2c).

Read-only over the local CSV: price scale, coverage by New York weekday/hour, gaps during
the expected CFD session, and large discontinuities that could be contract rolls.
"""
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'data', 'LIGHTCMDUSD_div1_1m_2020-08-01_2025-12-31.csv')
    df = pd.read_csv(path)
    ts = pd.to_datetime(df['timestamp'], unit='ms', utc=True)
    ny = ts.dt.tz_convert('America/New_York')
    out = {'rows': len(df), 'first': str(ts.iloc[0]), 'last': str(ts.iloc[-1]),
           'min_low': float(df['low'].min()), 'max_high': float(df['high'].max())}
    # Precio de cierre mensual para validar escala contra niveles conocidos del WTI.
    out['monthly_close_sample'] = {str(k): round(float(v), 2) for k, v in
                                   df.set_index(ts)['close'].resample('QE').last().items()}
    # Cobertura por día de semana y hora de Nueva York.
    cov = df.groupby([ny.dt.dayofweek, ny.dt.hour]).size().unstack(fill_value=0)
    out['ny_hour_minutes_by_dow'] = {int(k): {int(h): int(v) for h, v in row.items()} for k, row in cov.iterrows()}
    # Huecos > 5 min dentro de la sesión esperada (dom 18:00 – vie 17:00 NY, pausa 17–18).
    dt = np.diff(df['timestamp'].to_numpy()) // 60000
    gaps = []
    for i in np.where(dt > 5)[0]:
        a, b = ny.iloc[i], ny.iloc[i + 1]
        expected = (a.hour == 16 and a.minute >= 55 and b.hour == 18) or \
                   (a.dayofweek == 4 and a.hour >= 16 and b.dayofweek == 6 and b.hour >= 18)
        if not expected:
            gaps.append((str(a), str(b), int(dt[i])))
    out['unexpected_gaps_over_5m'] = len(gaps)
    out['largest_unexpected_gaps'] = sorted(gaps, key=lambda g: -g[2])[:15]
    # Saltos de precio entre minutos consecutivos (posibles rolls del CFD continuo).
    c = df['close'].to_numpy()
    o = df['open'].to_numpy()
    jump = np.abs(o[1:] / c[:-1] - 1)
    idx = np.where(jump > 0.02)[0]
    out['jumps_over_2pct'] = [(str(ts.iloc[i]), str(ts.iloc[i + 1]), round(float(c[i]), 3), round(float(o[i + 1]), 3))
                              for i in idx[:40]]
    out['n_jumps_over_2pct'] = int(len(idx))
    print(json.dumps(out, indent=1, default=str)[:20000])


if __name__ == '__main__':
    main()
