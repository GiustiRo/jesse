"""Audit public SPX minute files before custom-data import; never fabricate candles."""
import json
import os
from datetime import date

import numpy as np
import pandas as pd
import jesse.models
from jesse import helpers as jh
from research_scripts.dukascopy_download_v3 import _decode

ROOT = os.path.join('research_scripts', 'data')
path = os.path.join(ROOT, 'histdata', 'SPXUSD_div10_1m_2020_2025.csv')
df = pd.read_csv(path)
ts = pd.to_datetime(df['timestamp'], unit='ms', utc=True)
if (ts >= pd.Timestamp('2026-01-01', tz='UTC')).any():
    raise ValueError('lockbox contamination in research CSV')
if df['timestamp'].duplicated().any() or (np.diff(df['timestamp']) <= 0).any():
    raise ValueError('duplicate or unordered research minutes')
buckets = df.groupby(df['timestamp'] // 14400000).size()
bt = pd.to_datetime(buckets.index * 14400000, unit='ms', utc=True)
# Candidate common whole-bar window excludes the daily US futures-style break
# in both summer and winter. It is a coverage diagnostic, not an entry schedule.
chosen = (bt.dayofweek < 5) & (bt.hour < 20)
counts = buckets[chosen]
by_year = {}
for year in range(2020, 2026):
    x = counts[bt[chosen].year == year]
    by_year[str(year)] = {'observed_4h_buckets': len(x), 'complete_240min_buckets': int((x == 240).sum()),
                          'incomplete_buckets': int((x != 240).sum()),
                          'min_count': int(x.min())}
cache = os.path.join(ROOT, 'dukascopy_cache', 'USA500IDXUSD')
comparisons = []
hist = df.set_index('timestamp')['close']
for filename in sorted(os.listdir(cache)):
    if not filename.endswith('.bi5'):
        continue
    day = date.fromisoformat(filename[:-4])
    if day.year >= 2026:
        continue
    with open(os.path.join(cache, filename), 'rb') as fh:
        rows = _decode(fh.read(), day, 1000)
    if not len(rows):
        continue
    duke = pd.Series(rows[:, 4] / 10, index=rows[:, 0].astype('int64'))
    pair = pd.concat([hist.reindex(duke.index), duke], axis=1).dropna()
    if len(pair):
        rel = (pair.iloc[:, 0] / pair.iloc[:, 1] - 1).abs()
        comparisons.append({'day': str(day), 'matched_minutes': len(pair),
                            'median_abs_price_difference_pct': float(rel.median() * 100),
                            'max_abs_price_difference_pct': float(rel.max() * 100)})
out = {'rows': len(df), 'coverage_utc_4h_monfri_00_20': by_year,
       'cross_source_matching_timestamps': comparisons,
       'caveat': 'Both are index/CFD BID proxies; matching is not evidence of Binance fills.'}
out_path = os.path.join(ROOT, 'histdata', 'SPXUSD_source_audit.json')
with open(out_path, 'w') as fh:
    json.dump(out, fh, indent=2)
jh.debug(out)
