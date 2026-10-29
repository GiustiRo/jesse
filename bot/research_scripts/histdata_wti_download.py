"""Public HistData WTI/USD M1 archive fetcher for the r49 Fase 2b oil sleeve (C3).

Adapted from histdata_download.py (SPX proxy). Only the public file_down form on
histdata.com is submitted; payment and account forms are never used. No credentials,
account access, packages or orders. Download approved by the user on 2026-10-24.
"""
import argparse
import hashlib
import io
import json
import os
import time
import zipfile
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import numpy as np
import pandas as pd
import requests
import jesse.models  # Initialize store before standalone jh.debug logging.
from jesse import helpers as jh

BASE = 'https://www.histdata.com'
PAIR = 'WTIUSD'
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'histdata')
os.makedirs(ROOT, exist_ok=True)


class DownloadForm(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.action = None
        self.fields = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'form':
            self.active = a.get('id') == 'file_down'
            if self.active:
                self.action = a.get('action')
        if self.active and tag == 'input' and a.get('name'):
            self.fields[a['name']] = a.get('value', '')

    def handle_endtag(self, tag):
        if tag == 'form':
            self.active = False


def fetch(year, session, month=None):
    if not 2020 <= year <= 2025:
        raise ValueError('2026 lockbox: research archive must be 2020-2025')
    period = f'{year}{month:02d}' if month else str(year)
    path = os.path.join(ROOT, f'{PAIR}_M1_{period}.zip')
    if os.path.exists(path):
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:
                raise ValueError('corrupt cached ZIP')
        return path
    suffix = f'{year}/{month}' if month else str(year)
    page = f'{BASE}/download-free-forex-historical-data/?/ascii/1-minute-bar-quotes/{PAIR.lower()}/{suffix}'
    r = session.get(page, timeout=(10, 45))
    r.raise_for_status()
    form = DownloadForm()
    form.feed(r.text)
    action = urljoin(page, form.action or '')
    u = urlparse(action)
    # The same page includes payment forms. Only the public data endpoint and the
    # requested symbol/year are within the downloader's scope.
    if u.hostname != 'www.histdata.com' or u.path != '/get.php':
        raise ValueError('expected public HistData file_down form not found')
    if (form.fields.get('fxpair') != PAIR or form.fields.get('timeframe') != 'M1'
            or form.fields.get('platform') != 'ASCII' or form.fields.get('date') != str(year)
            or form.fields.get('datemonth') != period):
        raise ValueError(f'download form does not match the requested archive: {form.fields}')
    if not form.fields.get('tk'):
        # HistData only issues a download token to a fresh, unhurried session.
        raise ValueError('empty download token (rate limited); retry later with a new session')
    response = session.post(action, data=form.fields, headers={'Referer': page},
                            timeout=(10, 90), allow_redirects=False)
    response.raise_for_status()
    if not response.content.startswith(b'PK'):
        raise ValueError('expected ZIP download, not HTML or an unexpected redirect')
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        if z.testzip() is not None:
            raise ValueError('downloaded ZIP failed CRC validation')
    with open(path + '.partial', 'wb') as fh:
        fh.write(response.content)
    os.replace(path + '.partial', path)
    return path


def new_session():
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    return session


def read_zip(path):
    with zipfile.ZipFile(path) as z:
        csvs = [n for n in z.namelist() if n.lower().endswith('.csv')]
        if len(csvs) != 1:
            raise ValueError(f'expected one M1 CSV, found {csvs}')
        with z.open(csvs[0]) as fh:
            return pd.read_csv(fh, sep=';', header=None,
                               names=['local_time', 'open', 'high', 'low', 'close', 'volume'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--years', nargs='+', type=int, default=list(range(2020, 2026)))
    # Months published separately when the annual archive stops early (2023 ends on Dec 1).
    ap.add_argument('--extra-months', nargs='*', default=['202312'])
    args = ap.parse_args()
    frames = []
    manifest = {'source': 'HistData WTI/USD M1 BID proxy (CFD)', 'source_timezone': 'EST fixed UTC-05:00, no DST',
                'scale_divisor': 1, 'archives': [], 'lockbox_excluded_from': '2026-01-01T00:00:00Z'}
    jobs = [(y, None) for y in sorted(args.years)] + [(int(p[:4]), int(p[4:])) for p in args.extra_months]
    for year, month in jobs:
        cached = os.path.exists(os.path.join(ROOT, f'{PAIR}_M1_{year}{month:02d}.zip' if month else f'{PAIR}_M1_{year}.zip'))
        path = fetch(year, new_session(), month)
        if not cached:
            time.sleep(20)  # One fresh session per archive, spaced out to get a valid token.
        df = read_zip(path)
        # HistData uses fixed EST even during US daylight saving time.
        ts = pd.to_datetime(df.pop('local_time'), format='%Y%m%d %H%M%S', errors='raise')
        ts = ts.dt.tz_localize('Etc/GMT+5').dt.tz_convert('UTC')
        df.insert(0, 'timestamp', ts.astype('int64') // 1_000_000)
        df = df.loc[(ts >= pd.Timestamp('2020-01-01', tz='UTC')) &
                    (ts < pd.Timestamp('2026-01-01', tz='UTC'))].copy()
        nonpos = int((df[['open', 'high', 'low', 'close']] <= 0).any(axis=1).sum())
        duplicates = int(df.duplicated().sum())
        df = df.drop_duplicates().sort_values('timestamp', kind='stable')
        if df['timestamp'].duplicated().any() or (df['timestamp'] % 60000 != 0).any():
            raise ValueError(f'conflicting duplicate or non-minute timestamps in {year}')
        bad = ((df['high'] < df[['open', 'close', 'low']].max(axis=1)) |
               (df['low'] > df[['open', 'close', 'high']].min(axis=1))).sum()
        with open(path, 'rb') as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        manifest['archives'].append({'year': year, 'month': month, 'zip_sha256': digest, 'zip_bytes': os.path.getsize(path),
                                     'rows': len(df), 'nonpositive_rows': nonpos, 'ohlc_inconsistent_rows': int(bad),
                                     'identical_duplicate_rows_removed': duplicates,
                                     'volume_nonzero_rows': int((df['volume'] != 0).sum()),
                                     'first_ms': int(df['timestamp'].iloc[0]), 'last_ms': int(df['timestamp'].iloc[-1]),
                                     'min_low': float(df['low'].min())})
        jh.debug(manifest['archives'][-1])
        frames.append(df)
    combined = pd.concat(frames, ignore_index=True).sort_values('timestamp', kind='stable')
    # A monthly file may overlap its annual archive: identical rows are dropped, conflicts fail.
    combined = combined.drop_duplicates()
    if combined['timestamp'].duplicated().any():
        raise ValueError('conflicting prices between overlapping archives')
    if (np.diff(combined['timestamp']) <= 0).any():
        raise ValueError('overlapping archives: no silent de-duplication')
    # Jesse needs strictly positive prices. If the April-2020 negative-price episode is
    # present, start the series after the last non-positive minute and disclose it.
    nonpos = (combined[['open', 'high', 'low', 'close']] <= 0).any(axis=1)
    if nonpos.any():
        cut = int(combined.loc[nonpos, 'timestamp'].max())
        manifest['truncated_before_ms'] = cut + 60000
        manifest['truncation_reason'] = 'non-positive prices (April 2020 WTI episode); series starts after the last one'
        combined = combined.loc[combined['timestamp'] > cut].copy()
    out = os.path.join(ROOT, f'{PAIR}_1m_2020_2025.csv')
    combined.to_csv(out + '.partial', index=False, float_format='%.6f')
    dates = pd.to_datetime(combined['timestamp'], unit='ms', utc=True)
    by_hour = combined.groupby([dates.dt.tz_convert('America/New_York').dt.dayofweek,
                               dates.dt.tz_convert('America/New_York').dt.hour]).size()
    by_hour.to_csv(out + '.ny_dow_hour_counts.csv', header=['observed_minutes'])
    gaps = np.diff(combined['timestamp'].to_numpy()) // 60000 - 1
    manifest['rows'] = len(combined)
    manifest['first_ms'] = int(combined['timestamp'].iloc[0])
    manifest['gaps_over_1_minute'] = int((gaps > 0).sum())
    manifest['largest_gaps_minutes'] = sorted(gaps[gaps > 0].tolist(), reverse=True)[:20]
    manifest['ny_hours_observed'] = sorted(set(dates.dt.tz_convert('America/New_York').dt.hour.tolist()))
    with open(out + '.manifest.json', 'w') as fh:
        json.dump(manifest, fh, indent=2)
    os.replace(out + '.partial', out)
    jh.debug({'output': out, 'rows': len(combined), 'first': str(dates.iloc[0]), 'last': str(dates.iloc[-1]),
              'largest_gaps': manifest['largest_gaps_minutes'][:5]})


if __name__ == '__main__':
    main()
