"""r63 F0a: list every USDT-M symbol of data.binance.vision and its 1h kline months (PROTOCOL_R63 §1).

Only the S3 listing is read (key names), never a price. Output: data/r63/listing_raw.json.

    python -P research_scripts/r63_list.py
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r63')
S3 = 'https://s3-ap-northeast-1.amazonaws.com/data.binance.vision'
PREFIX = 'data/futures/um/monthly/klines/'
NS = '{http://s3.amazonaws.com/doc/2006-03-01/}'


def s3_list(prefix, delimiter='/'):
    """(common prefixes, keys) of an S3 prefix, following the v1 `marker` pagination."""
    prefixes, keys, marker = [], [], ''
    while True:
        q = urllib.parse.urlencode({'prefix': prefix, 'delimiter': delimiter, 'marker': marker})
        for k in range(8):
            try:
                with urllib.request.urlopen(f'{S3}?{q}', timeout=120) as r:
                    root = ET.fromstring(r.read())
                break
            except Exception:
                time.sleep(2 ** k)
        else:
            raise RuntimeError(f'listing failed: {prefix}')
        prefixes += [p.find(NS + 'Prefix').text for p in root.findall(NS + 'CommonPrefixes')]
        keys += [c.find(NS + 'Key').text for c in root.findall(NS + 'Contents')]
        if root.find(NS + 'IsTruncated').text != 'true':
            return prefixes, keys
        nm = root.find(NS + 'NextMarker')
        marker = nm.text if nm is not None else (keys[-1] if keys else prefixes[-1])


def months_of(sym):
    _, keys = s3_list(f'{PREFIX}{sym}/1h/')
    return sorted({m.group(1) for k in keys if (m := re.search(r'-1h-(\d{4}-\d{2})\.zip$', k))})


def main():
    os.makedirs(OUT, exist_ok=True)
    prefixes, _ = s3_list(PREFIX)
    syms = sorted(p[len(PREFIX):].strip('/') for p in prefixes)
    with ThreadPoolExecutor(16) as ex:
        months = list(ex.map(months_of, syms))
    out = {'source': f'{S3}?prefix={PREFIX}', 'listed_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'n': len(syms), 'symbols': {s: m for s, m in zip(syms, months)}}
    with open(os.path.join(OUT, 'listing_raw.json'), 'w') as f:
        json.dump(out, f, indent=0)
    print(f'{len(syms)} prefixes listed')


if __name__ == '__main__':
    sys.exit(main())
