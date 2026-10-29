"""r60 F0b: free token-unlock calendar probe (PROTOCOL_R60.md section 2).

Calendar data only. Every fetched document is passed through ``strip_market`` before it
is written, so price / mcap / volume fields never land on disk (protocol rule: no prices
around events). Downloaded files are untrusted data and are only parsed as JSON.

Usage:
    python -I r60_unlocks.py fetch      # DefiLlama datasets bucket, per protocol
    python -I r60_unlocks.py build      # coverage.csv + events.csv from raw/
"""
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r60', 'unlocks')
RAW = os.path.join(OUT, 'raw')
UNIVERSE = os.path.join(HERE, 'data', 'r52', 'universe50.json')
# The free public bucket; api.llama.fi/emission(s) now answers 402 (paid plan).
LLAMA = 'https://defillama-datasets.llama.fi/emissions/{}'

# Universe symbol -> DefiLlama emissions slug (only slugs present in emissionsProtocolsList).
LLAMA_SLUG = {
    'AAVE': 'aave', 'ANKR': 'ankr', 'APE': 'apecoin', 'APT': 'aptos', 'AVAX': 'avalanche',
    'AXS': 'axie-infinity', 'BAT': 'basic-attention', 'BNB': 'binance-smart-chain',
    'LINK': 'chainlink', 'COMP': 'compound-finance', 'CRV': 'curve-finance',
    'DOGE': 'dogecoin', 'FIL': 'filecoin', 'HBAR': 'hedera', 'INJ': 'injective-orderbook',
    'ICP': 'internet-computer', 'LDO': 'lido', 'LTC': 'litecoin', 'NEAR': 'near-protocol',
    'OP': 'optimism-foundation', 'SOL': 'solana', 'TRX': 'tron', 'UNI': 'uniswap',
}

# Market-data keys removed recursively before saving (case-insensitive substring match).
MARKET_KEYS = ('price', 'mcap', 'marketcap', 'volume', 'fdv')

START = datetime(2021, 1, 1, tzinfo=timezone.utc).timestamp()
END = datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp()


def strip_market(obj):
    if isinstance(obj, dict):
        return {k: strip_market(v) for k, v in obj.items()
                if not any(m in k.lower() for m in MARKET_KEYS)}
    if isinstance(obj, list):
        return [strip_market(v) for v in obj]
    return obj


def symbols():
    with open(UNIVERSE) as f:
        uni = json.load(f)
    out = []
    for row in uni:
        s = row['symbol']
        if s in ('BTCUSDT', 'ETHUSDT'):
            continue
        s = s[:-4]
        if s.startswith('1000'):
            s = s[4:]
        out.append(s)
    return out


def fetch():
    os.makedirs(RAW, exist_ok=True)
    for sym, slug in LLAMA_SLUG.items():
        path = os.path.join(RAW, f'llama_{slug}.json')
        if os.path.exists(path):
            continue
        r = requests.get(LLAMA.format(slug), timeout=120)
        print(sym, slug, r.status_code, len(r.content))
        if r.status_code == 200:
            with open(path, 'w') as f:
                json.dump(strip_market(r.json()), f)
        time.sleep(1.5)  # modest pace for a free public bucket


# Universe symbol -> candidate CryptoRank slugs (tried in order until one answers 200).
CR_SLUGS = {
    'ZEC': ['zcash'], 'SOL': ['solana'], 'NEAR': ['near-protocol'], 'XRP': ['ripple'],
    'BNB': ['bnb', 'binance-coin'], 'DOGE': ['dogecoin'], 'UNI': ['uniswap'], 'QNT': ['quant'],
    'ADA': ['cardano'], 'INJ': ['injective-protocol', 'injective'], 'LINK': ['chainlink'],
    'FIL': ['filecoin'], 'AVAX': ['avalanche'], 'XMR': ['monero'], 'AAVE': ['aave'],
    'BCH': ['bitcoin-cash'], 'GTC': ['gitcoin'], 'IOST': ['iostoken', 'iost'],
    'LTC': ['litecoin'], 'DOT': ['polkadot'], 'DASH': ['dash'], 'COMP': ['compound'],
    'XEC': ['ecash'], 'XLM': ['stellar'], 'TRX': ['tron'], 'APT': ['aptos'],
    'HBAR': ['hedera-hashgraph', 'hedera'], 'SHIB': ['shiba-inu'], 'CRV': ['curve', 'curve-dao-token'],
    'ETC': ['ethereum-classic'], 'SAND': ['the-sandbox', 'sandbox'], 'OP': ['optimism'],
    'ATOM': ['cosmos'], 'ICP': ['internet-computer'], 'ANKR': ['ankr'], 'LDO': ['lido-dao', 'lido'],
    'RLC': ['iexec-rlc', 'rlc'], 'BAT': ['basic-attention-token'], 'LUNC': ['terra', 'terra-luna-classic'],
    'MTL': ['metal', 'metal-dao'], 'GALA': ['gala'], 'ZIL': ['zilliqa'], 'ALGO': ['algorand'],
    'EGLD': ['multiversx-egld', 'elrond', 'multiversx'], 'APE': ['ape-coin'], 'ZEN': ['horizen'],
    'AXS': ['axie-infinity'], 'AR': ['arweave'],
}
CR_URL = 'https://cryptorank.io/price/{}/vesting'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'


def fetch_cryptorank():
    """Save only the stripped ``vestingInfo`` block of each public vesting page.

    The raw HTML also carries quotes, so it is parsed in memory and never written. Without
    an account CryptoRank exposes one allocation per coin (``isAuthProtected``).
    """
    import re
    path = os.path.join(RAW, 'cryptorank_vesting.json')
    out = json.load(open(path)) if os.path.exists(path) else {}
    for sym in symbols():
        if sym in out:
            continue
        rec = {'slug': None, 'status': []}
        for slug in CR_SLUGS.get(sym, []):
            r = requests.get(CR_URL.format(slug), headers={'User-Agent': UA}, timeout=60)
            rec['status'].append([slug, r.status_code])
            time.sleep(3)  # polite pace; public page, no API
            if r.status_code != 200:
                continue
            m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.text, re.S)
            if not m:
                continue
            pp = json.loads(m.group(1)).get('props', {}).get('pageProps', {})
            rec['slug'] = slug
            rec['vestingInfo'] = strip_market(pp.get('vestingInfo'))
            break
        out[sym] = rec
        print(sym, rec['status'], 'allocs', len((rec.get('vestingInfo') or {}).get('allocations') or []))
        with open(path, 'w') as f:
            json.dump(out, f)


# Coins with no vesting calendar by design (mined / fair-launch / fully circulating since
# before 2021). Assessed from public protocol design, not from any market data.
BY_DESIGN = {
    'ZEC': 'PoW; founders reward ended 2020-11, Dev Fund is part of block reward (emission, not unlock)',
    'XMR': 'PoW, tail emission; no premine',
    'BCH': 'PoW fork of BTC; no premine',
    'LTC': 'PoW; halvings only (DefiLlama models mining rewards)',
    'DOGE': 'PoW; fixed 10k/block (DefiLlama models mining rewards)',
    'ETC': 'PoW; 5M-block era reductions only',
    'DASH': 'PoW/masternode emission; no vesting',
    'XEC': 'PoW fork of BCH; no vesting',
    'ZEN': 'PoW; treasury share of block reward; no vesting',
    'SHIB': 'Fully circulating at launch (2020); burns only',
    'QNT': 'Fixed supply, fully distributed by 2018; no published vesting',
    'RLC': 'Fully circulating since 2017 ICO',
    'MTL': 'ICO 2017; no published vesting in window',
    'BAT': 'Fully vested (DefiLlama note)',
    'LUNC': 'Post-collapse (2022-05) hyperinflation + burns; no vesting calendar',
}
# Coins with real but discretionary or protocol-inflation supply changes and no free calendar.
NO_FREE_SCHEDULE = {
    'XRP': 'Ripple escrow: 1B XRP/month released, most re-locked; no free per-event dataset found',
    'ADA': 'Reserve-funded staking emission; no vesting cliffs',
    'DOT': 'Protocol inflation ~10%/yr; no vesting cliffs after 2020',
    'ATOM': 'Protocol inflation 7-20%; CryptoRank shows only one hidden-partial allocation (AiB)',
    'XLM': 'SDF discretionary distributions; 2019 burn; no calendar',
    'IOST': 'Protocol inflation; no free calendar found',
    'ZIL': 'Mining/staking emission; no vesting calendar',
    'ALGO': 'Foundation/backer vesting largely done by 2021; no free calendar found',
    'EGLD': 'Staking emission; CryptoRank page 404; no free calendar found',
    'AR': 'Mining emission; CryptoRank has no vesting',
    'SAND': 'Company reserve semiannual cliffs (CryptoRank, only 1 allocation visible without login)',
    'GALA': 'Daily node distribution; CryptoRank shows only 1 allocation without login',
    'GTC': '2y linear team/investor vesting from 2021-05; CryptoRank shows only 1 allocation',
}

DAY = 86400
WEEK = 7 * DAY
# Non-unlock supply flows: kept out of the "unlock" counts (still listed with their category).
EMISSION_CATS = {'staking', 'farming', 'burned'}
EMISSION_LABEL_WORDS = ('staking', 'mining', 'reward', 'minting', 'burn', 'incentive')


def _d(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime('%Y-%m-%d')


def _llama_series(d):
    """label -> {day_ts: cumulative unlocked} from the source's own documentedData."""
    out = {}
    for L in d['documentedData']['data']:
        out[L['label']] = {x['timestamp'] // DAY * DAY: x['unlocked'] for x in L['data']}
    return out


def _unlocked_total_before(series, ts):
    """Source-modeled unlocked supply on the day before ``ts`` (denominator proxy)."""
    day = ts // DAY * DAY - DAY
    tot = 0.0
    for s in series.values():
        keys = [k for k in s if k <= day]
        if keys:
            tot += s[max(keys)]
    return tot


def _is_emission(cat, label):
    return (cat in EMISSION_CATS) or any(w in label.lower() for w in EMISSION_LABEL_WORDS)


def build():
    syms = symbols()
    inv = {v: k for k, v in LLAMA_SLUG.items()}
    cr = json.load(open(os.path.join(RAW, 'cryptorank_vesting.json')))
    events, cov = [], []
    for sym in syms:
        row = {'symbol': sym, 'sources': [], 'has_schedule': 'n', 'first_event_date': '',
               'n_events_2021_2024': 0, 'n_unlock_events_2021_2024': 0,
               'n_cliff_ge1pct_circ_2021_2024': 0, 'fields': '', 'notes': ''}
        slug = LLAMA_SLUG.get(sym)
        notes = []
        if slug:
            d = json.load(open(os.path.join(RAW, f'llama_{slug}.json')))
            m = d['metadata']
            series = _llama_series(d)
            total = m.get('total') or (d.get('supplyMetrics') or {}).get('maxSupply')
            row['sources'].append('defillama')
            allts = [e['timestamp'] for e in m['unlockEvents']]
            row['first_event_date'] = _d(min(allts)) if allts else ''
            daily_cliff = {}
            for e in m['unlockEvents']:
                ts = e['timestamp']
                if not (START <= ts < END):
                    continue
                denom = _unlocked_total_before(series, ts)
                for a in e['cliffAllocations']:
                    amt = a['amount']
                    emis = _is_emission(a.get('category', ''), a['recipient'])
                    typ = 'burn' if amt < 0 else ('cliff_emission' if emis else 'cliff')
                    events.append({'symbol': sym, 'date': _d(ts), 'amount_tokens': round(amt, 4),
                                   'pct_circulating_at_event': round(100 * amt / denom, 4) if denom else '',
                                   'pct_total_supply': round(100 * amt / total, 4) if total else '',
                                   'type': typ, 'recipient': a['recipient'],
                                   'category': a.get('category', ''), 'source': 'defillama'})
                    if typ == 'cliff':
                        daily_cliff[_d(ts)] = daily_cliff.get(_d(ts), 0) + (100 * amt / denom if denom else 0)
                for a in e['linearAllocations']:
                    rate = a.get('newRatePerWeek') or 0
                    end = a.get('endTimestamp') or ts
                    amt = rate * max(end - ts, 0) / WEEK  # tokens over this linear segment
                    emis = _is_emission(a.get('category', ''), a['recipient'])
                    events.append({'symbol': sym, 'date': _d(ts), 'amount_tokens': round(amt, 4),
                                   'pct_circulating_at_event': '',
                                   'pct_total_supply': round(100 * amt / total, 4) if total else '',
                                   'type': ('linear_emission:' if emis else 'linear:') + a.get('unlockType', ''),
                                   'recipient': a['recipient'], 'category': a.get('category', ''),
                                   'source': 'defillama'})
            mine = [e for e in events if e['symbol'] == sym]
            row['n_events_2021_2024'] = len(mine)
            row['n_unlock_events_2021_2024'] = sum(1 for e in mine if e['type'] in ('cliff',) or e['type'].startswith('linear:'))
            # Coin-day aggregation: several allocations on one day count as one cliff event.
            row['n_cliff_ge1pct_circ_2021_2024'] = sum(1 for v in daily_cliff.values() if v >= 1.0)
            nonemis = [lab for lab in series if not _is_emission('', lab)]
            row['has_schedule'] = 'y'
            row['fields'] = 'date;amount;pct_total;pct_circulating(proxy: source unlocked supply);type cliff/linear;recipient;category'
            if m.get('notes'):
                notes.append('DL notes: ' + ' | '.join(m['notes'])[:300])
            if not mine:
                notes.append('no discrete events 2021-2024 in DL event list; daily series only (%d labels)' % len(series))
        c = cr.get(sym, {})
        v = c.get('vestingInfo') or {}
        if v.get('allocations'):
            row['sources'].append('cryptorank(partial: %d allocation visible, rest auth-protected)' % len(v['allocations']))
            if not slug:
                row['has_schedule'] = 'partial'
                row['fields'] = 'date;pct of one allocation;unlock_type (one allocation only)'
        if sym in BY_DESIGN:
            row['has_schedule'] = 'n/a (by design)' if row['has_schedule'] == 'n' else row['has_schedule'] + ' (emission only)'
            notes.append(BY_DESIGN[sym])
        elif sym in NO_FREE_SCHEDULE:
            notes.append(NO_FREE_SCHEDULE[sym])
        row['sources'] = '+'.join(row['sources']) or 'none'
        row['notes'] = ' ; '.join(notes)
        cov.append(row)
    with open(os.path.join(OUT, 'coverage.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=list(cov[0].keys()))
        w.writeheader()
        w.writerows(cov)
    with open(os.path.join(OUT, 'events.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=list(events[0].keys()))
        w.writeheader()
        w.writerows(events)
    print('coins', len(cov), 'events', len(events))
    for r in cov:
        print(r['symbol'], r['sources'], r['has_schedule'], r['n_events_2021_2024'],
              r['n_unlock_events_2021_2024'], r['n_cliff_ge1pct_circ_2021_2024'])


# Fixed before looking at any comparison: coin -> (CryptoRank allocation, DefiLlama label).
# Sample = the middle in-window CryptoRank batch of each coin (SOL has a single batch).
XCHECK = {
    'SOL': 'Strategic Sale', 'NEAR': 'Prior Backers 36m', 'UNI': 'advisors', 'AVAX': 'Team',
    'APT': 'Community', 'CRV': 'Employees', 'OP': 'Retroactive Public Goods Funding',
    'ICP': 'Community Airdrop', 'LDO': 'Validators & Signature Holders', 'APE': 'launch contributors',
}


def xcheck():
    cr = json.load(open(os.path.join(RAW, 'cryptorank_vesting.json')))
    rows = []
    for sym, label in XCHECK.items():
        d = json.load(open(os.path.join(RAW, f'llama_{LLAMA_SLUG[sym]}.json')))
        s = _llama_series(d)[label]
        a = cr[sym]['vestingInfo']['allocations'][0]
        tokens = float(a['tokens'])
        batches = sorted(a['batches'], key=lambda b: b['date'])
        inwin = [b for b in batches if '2021' <= b['date'][:4] <= '2024']
        b = inwin[len(inwin) // 2]
        bts = int(datetime.fromisoformat(b['date'].replace('Z', '+00:00')).timestamp()) // DAY * DAY
        idx = batches.index(b)
        prev_ts = (int(datetime.fromisoformat(batches[idx - 1]['date'].replace('Z', '+00:00')).timestamp()) // DAY * DAY
                   if idx > 0 else bts - 30 * DAY)
        amt_cr = tokens * b['unlock_percent'] / 100

        def at(t):
            ks = [k for k in s if k <= t]
            return s[max(ks)] if ks else 0.0
        # (1) is there a DL jump >= half the CR batch within +-3 days? (date agreement for a cliff)
        win = at(bts + 3 * DAY) - at(bts - 4 * DAY)
        # (2) DL amount released over the same inter-batch interval (handles linear vs stepped)
        inter = at(bts) - at(prev_ts)
        ratio_win = win / amt_cr if amt_cr else float('nan')
        ratio_inter = inter / amt_cr if amt_cr else float('nan')
        rows.append({'symbol': sym, 'cr_allocation': a['name'].strip(), 'dl_label': label,
                     'cr_alloc_tokens': tokens, 'dl_label_final_tokens': round(at(END), 0),
                     'cr_batch_date': b['date'][:10], 'cr_batch_tokens': round(amt_cr, 1),
                     'cr_unlock_type': a.get('unlock_type'),
                     'dl_tokens_pm3d': round(win, 1), 'ratio_pm3d': round(ratio_win, 3),
                     'dl_tokens_since_prev_batch': round(inter, 1), 'ratio_interval': round(ratio_inter, 3),
                     'date_match_pm3d': 'y' if ratio_win >= 0.5 else 'n',
                     'size_match_20pct': 'y' if 0.8 <= ratio_win <= 1.2 else ('interval-only' if 0.8 <= ratio_inter <= 1.2 else 'n')})
    with open(os.path.join(OUT, 'crosscheck.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)


if __name__ == '__main__':
    {'fetch': fetch, 'fetch_cr': fetch_cryptorank, 'build': build, 'xcheck': xcheck}[sys.argv[1]]()
