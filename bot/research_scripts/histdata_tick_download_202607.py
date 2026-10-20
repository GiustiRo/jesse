"""Public HistData SPX/USD M1 archive fetcher for the Phase 2 data pipeline.

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


def fetch(year, session):
    if year != 2026:
        raise ValueError('Only the authorized July 2026 source check is allowed')
    path = os.path.join(ROOT, 'SPXUSD_T_202607.zip')
    if os.path.exists(path):
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:
                raise ValueError('corrupt cached ZIP')
        return path
    page = f'{BASE}/download-free-forex-historical-data/?/ascii/tick-data-quotes/spxusd/{year}/7'
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
    if (form.fields.get('fxpair') != 'SPXUSD' or form.fields.get('timeframe') != 'T'
            or form.fields.get('platform') != 'ASCII' or form.fields.get('date') != str(year)
            or form.fields.get('datemonth') != '202607'):
        raise ValueError('download form does not match the requested archive')
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


def main():
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    path = fetch(2026, session)
    with zipfile.ZipFile(path) as z:
        csvs = [name for name in z.namelist() if name.lower().endswith('.csv')]
        if len(csvs) != 1:
            raise ValueError("Expected a single tick CSV")
        with z.open(csvs[0]) as fh:
            sample = [fh.readline().decode('utf-8').strip() for _ in range(4)]
        jh.debug({'source': 'HistData ASCII SPXUSD BID/ASK ticks, July 2026',
                  'zip_bytes': os.path.getsize(path),
                  'csv_bytes': z.getinfo(csvs[0]).file_size, 'csv_name': csvs[0],
                  'sample': sample})
    jh.debug({'tick_zip': path})


if __name__ == '__main__':
    main()
