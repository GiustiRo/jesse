"""Authorized 2026 HistData SPX/USD M1 fetcher for frozen K1001 OOS evaluation.

Only the public file_down form on histdata.com is submitted; payment and account
forms are never used. No credentials, account access, packages or orders.
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


def fetch(period, session):
    year, month = divmod(period, 100)
    if year != 2026 or not 1 <= month <= 10:
        raise ValueError('Only January-October 2026 are authorized')
    path = os.path.join(ROOT, f'SPXUSD_M1_{period}.zip')
    if os.path.exists(path):
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:
                raise ValueError('corrupt cached ZIP')
        return path
    page = f'{BASE}/download-free-forex-historical-data/?/ascii/1-minute-bar-quotes/spxusd/{year}/{month}'
    r = session.get(page, timeout=(10, 45))
    r.raise_for_status()
    form = DownloadForm()
    form.feed(r.text)
    action = urljoin(page, form.action or '')
    u = urlparse(action)
    # The same page includes payment forms. Only this observed public data
    # endpoint and the requested symbol/year are within the downloader's scope.
    if u.hostname != 'www.histdata.com' or u.path != '/get.php':
        raise ValueError('expected public HistData file_down form not found')
    if (form.fields.get('fxpair') != 'SPXUSD' or form.fields.get('timeframe') != 'M1'
            or form.fields.get('platform') != 'ASCII' or form.fields.get('date') != str(year)
            or form.fields.get('datemonth') != str(period)):
        raise ValueError('download form does not match the requested archive')
    response = session.post(action, data=form.fields, headers={'Referer': page},
                            timeout=(10, 90), allow_redirects=False)
    response.raise_for_status()
    if not response.content.startswith(b'PK'):
        jh.debug({'download_status': response.status_code, 'content_type': response.headers.get('Content-Type'),
                  'provider_message': response.text[:1600]})
        raise ValueError('expected ZIP download, not HTML or an unexpected redirect')
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        if z.testzip() is not None:
            raise ValueError('downloaded ZIP failed CRC validation')
    with open(path + '.partial', 'wb') as fh:
        fh.write(response.content)
    os.replace(path + '.partial', path)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--years', nargs='+', type=int, default=[2026], choices=[2026])
    ap.add_argument('--probe', action='store_true')
    args = ap.parse_args()
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    frames = []
    problems = []
    manifest = {'source': 'HistData SPX/USD M1 BID proxy', 'source_timezone': 'EST fixed UTC-05:00, no DST',
                'scale_divisor': 10, 'archives': [], 'authorized_oos_start': '2026-01-01T00:00:00Z', 'finish_exclusive': '2026-10-19T00:00:00Z'}
    for period in range(202601, 202611):
        year = 2026
        path = fetch(period, session)
        with zipfile.ZipFile(path) as z:
            csvs = [n for n in z.namelist() if n.lower().endswith('.csv')]
            if len(csvs) != 1:
                raise ValueError(f'expected one M1 CSV, found {csvs}')
            with z.open(csvs[0]) as fh:
                df = pd.read_csv(fh, sep=';', header=None,
                                 names=['local_time','open','high','low','close','volume'])
        # HistData explicitly uses fixed EST even during US daylight saving time.
        # Localizing to America/New_York would shift every summer bar by one hour.
        ts = pd.to_datetime(df.pop('local_time'), format='%Y%m%d %H%M%S', errors='raise')
        ts = ts.dt.tz_localize('Etc/GMT+5').dt.tz_convert('UTC')
        df.insert(0, 'timestamp', ts.astype('int64') // 1_000_000)
        df = df.loc[(ts >= pd.Timestamp('2026-01-01', tz='UTC')) &
                    (ts < pd.Timestamp('2026-10-19', tz='UTC'))].copy()
        df[['open','high','low','close']] /= 10.0
        prices = df[['open','high','low','close']].to_numpy()
        if (not np.isfinite(df.to_numpy()).all() or (prices <= 0).any()
                or (df['high'] < df[['open','close','low']].max(axis=1)).any()
                or (df['low'] > df[['open','close','high']].min(axis=1)).any()
                or (df['volume'] != 0).any()):
            raise ValueError(f'invalid OHLC or unexpected volume semantics in {year}')
        # The vendor's 2020 annual archive repeats a block of 59 identical
        # observations. Remove exact row copies only, and disclose the count.
        # Conflicting prices at the same timestamp are never resolved by picking one.
        duplicates = int(df.duplicated().sum())
        df = df.drop_duplicates().sort_values('timestamp', kind='stable')
        if df['timestamp'].duplicated().any() or (df['timestamp'] % 60000 != 0).any():
            jh.debug({'period': period, 'conflict_rows': int(df['timestamp'].duplicated(keep=False).sum()),
                      'conflicts_sample': df[df['timestamp'].duplicated(keep=False)].head(12).to_dict('records'),
                      'non_minute_rows': int((df['timestamp'] % 60000 != 0).sum()),
                      'non_minute_sample': df[df['timestamp'] % 60000 != 0].head(12).to_dict('records')})
            problems.append(period)
            continue
        with open(path, 'rb') as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        manifest['archives'].append({'period': period, 'zip_sha256': digest, 'rows': len(df),
                                     'identical_duplicate_rows_removed': duplicates,
                                     'first_ms': int(df['timestamp'].iloc[0]),
                                     'last_ms': int(df['timestamp'].iloc[-1])})
        jh.debug(manifest['archives'][-1])
        frames.append(df)
        time.sleep(1)  # Keep the provider pacing of the original downloader.
    if problems:
        audit_path = os.path.join(ROOT, 'SPXUSD_2026_validation_failure.json')
        manifest['invalid_periods'] = problems
        manifest['status'] = 'rejected_before_import'
        with open(audit_path, 'w') as fh:
            json.dump(manifest, fh, indent=2)
        jh.debug({'invalid_periods': problems, 'audit_path': audit_path})
        raise ValueError('Unresolved source conflicts; no combined CSV or database import')
    if args.probe:
        jh.debug({'probe_rows': frames[0].head(3).to_dict('records')})
        return
    combined = pd.concat(frames, ignore_index=True)
    if (np.diff(combined['timestamp']) <= 0).any():
        raise ValueError('overlapping archives: no silent de-duplication')
    out = os.path.join(ROOT, 'SPXUSD_div10_1m_2026_OOS_20261019.csv')
    combined.to_csv(out + '.partial', index=False, float_format='%.6f')
    # Coverage diagnostics preserve gaps; zero volume does not mean a closed minute.
    dates = pd.to_datetime(combined['timestamp'], unit='ms', utc=True)
    per_day = combined.groupby(dates.dt.strftime('%Y-%m-%d')).size()
    per_day.to_csv(out + '.daily_counts.csv', header=['observed_minutes'])
    by_hour = combined.groupby([dates.dt.tz_convert('America/New_York').dt.month,
                               dates.dt.tz_convert('America/New_York').dt.hour]).size()
    by_hour.to_csv(out + '.ny_hour_counts.csv', header=['observed_minutes'])
    gaps = np.diff(combined['timestamp'].to_numpy()) // 60000 - 1
    manifest['rows'] = len(combined)
    manifest['gaps_over_1_minute'] = int((gaps > 0).sum())
    manifest['largest_gaps_minutes'] = sorted(gaps[gaps > 0].tolist(), reverse=True)[:20]
    manifest['status'] = 'downloaded_and_structurally_valid; calendar/proxy audit still required'
    with open(out + '.manifest.json', 'w') as fh:
        json.dump(manifest, fh, indent=2)
    os.replace(out + '.partial', out)
    jh.debug({'output': out, 'rows': len(combined), 'first_utc': dates.iloc[0].isoformat(),
              'last_utc': dates.iloc[-1].isoformat(), 'days': len(per_day),
              'monthly_rows': combined.groupby(dates.dt.strftime('%Y-%m')).size().to_dict(),
              'largest_gaps': manifest['largest_gaps_minutes']})


if __name__ == '__main__':
    main()
