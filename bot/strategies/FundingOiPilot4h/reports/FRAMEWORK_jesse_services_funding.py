"""Versioned Binance USD-M funding data; rates are decimal fractions, never percentages."""

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time
from typing import TypedDict

import requests


EXCHANGE = 'Binance Perpetual Futures'
SOURCE = 'binance-usdm-fundingRate-v1'
# A backtest replays minute bars. Vendor millisecond jitter around a scheduled
# boundary is bucketed to that minute, and the original timestamp is retained.
TIMESTAMP_JITTER_MS = 1_000
MAX_INTERVAL_MS = 8 * 3_600_000
PUBLICATION_DELAY_MS = 60_000


class FundingHistoryRow(TypedDict):
    exchange: str
    symbol: str
    settled_at: int
    rate_decimal: float
    mark_price: float
    mark_price_source: str
    available_at: int


@dataclass(frozen=True)
class FundingEvent:
    exchange: str
    symbol: str
    settled_at: int
    rate_decimal: float
    mark_price: float
    mark_price_source: str = 'fundingRate.settlement_mark'

    def __post_init__(self):
        if (type(self.settled_at) is not int or self.settled_at < 0
                or not math.isfinite(self.rate_decimal)
                or not math.isfinite(self.mark_price) or self.mark_price <= 0):
            raise ValueError('Invalid funding timestamp, rate or settlement mark')

    @property
    def effective_at(self) -> int:
        return self.settled_at - self.settled_at % 60_000

    @property
    def available_at(self) -> int:
        # Final rates are not assumed known before their settlement. Binance's
        # historical endpoint does not contain publication timestamps; a full
        # minute of delay is an explicit conservative research assumption.
        return self.effective_at + PUBLICATION_DELAY_MS


def _encode(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def _root() -> Path:
    return Path('storage/funding')


def _path(dataset_id: str) -> Path:
    if not isinstance(dataset_id, str) or not re.fullmatch(r'[0-9a-f]{64}', dataset_id):
        raise ValueError('Funding dataset ID must be a SHA-256 digest')
    return _root() / f'{dataset_id}.json'


def save_dataset(dataset: dict) -> str:
    """Content-addressed snapshots never silently overwrite a revised vendor history."""
    payload = _encode(dataset)
    dataset_id = sha256(payload).hexdigest()
    path = _path(dataset_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as file:
        temporary = file.name
        file.write(payload)
    try:
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return dataset_id


def load_dataset(dataset_id: str) -> dict:
    payload = _path(dataset_id).read_bytes()
    if sha256(payload).hexdigest() != dataset_id:
        raise ValueError('Funding dataset checksum mismatch')
    return json.loads(payload)


def list_datasets() -> list:
    if not _root().exists():
        return []
    return sorted((describe_dataset(path.stem, load_dataset(path.stem))
                   for path in _root().glob('*.json')), key=lambda item: item['finish'], reverse=True)


def update_dataset(dataset_id: str, finish: int) -> dict:
    """Re-fetch the explicit full window so vendor corrections create a new ID.

    Funding snapshots are small (three usual BTC events/day). A full refresh
    audits the overlap instead of silently merging a revised final rate.
    """
    old = load_dataset(dataset_id)
    if finish < old['finish']:
        raise ValueError('An update cannot shorten existing coverage')
    result = import_binance_history(old['start'], finish, old.get('allow_mark_price_proxy', False))
    return result | {'previous_dataset_id': dataset_id, 'changed': result['dataset_id'] != dataset_id}


def _fill_missing_marks(client, events: dict) -> int:
    """Explicit hourly mark-OPEN proxy for old API rows with empty markPrice.

    A candle's open is an approximation, not the exact settlement mark. One
    paginated hourly series avoids a request per historical settlement.
    """
    missing = {stamp - stamp % 60_000: row for stamp, row in events.items() if row['mark_price'] is None}
    if not missing:
        return 0
    if any(stamp % 3_600_000 for stamp in missing):
        raise ValueError('Missing settlement mark outside an hourly boundary; no supported mark proxy')
    cursor, finish = min(missing), max(missing)
    while cursor <= finish:
        response = client.get('https://fapi.binance.com/fapi/v1/markPriceKlines', params={
            'symbol': 'BTCUSDT', 'interval': '1h', 'startTime': cursor,
            'endTime': finish, 'limit': 1500,
        }, timeout=30)
        response.raise_for_status()
        rows = response.json()
        if not isinstance(rows, list) or not rows:
            raise ValueError('Missing historical mark-price candles; no partial snapshot published')
        last = cursor - 1
        for row in rows:
            stamp = int(row[0])
            if stamp < cursor or stamp < last or stamp > finish:
                raise ValueError('Unexpected mark-price candle timestamp')
            if stamp in missing:
                mark = float(row[1])
                if not math.isfinite(mark) or mark <= 0:
                    raise ValueError('Invalid mark-price candle open')
                missing[stamp]['mark_price'] = mark
                missing[stamp]['mark_price_source'] = 'markPriceKlines.1h_open_proxy'
            last = stamp
        cursor = last + 3_600_000
        time.sleep(0.6)
    if any(row['mark_price'] is None for row in missing.values()):
        raise ValueError('Historical mark-price proxy does not cover every missing settlement')
    return len(missing)


def import_binance_history(start: int, finish: int, allow_mark_price_proxy: bool = False) -> dict:
    """Fetch an explicit [start, finish) BTC window. Public data needs no account keys.

    The API's ascending, inclusive pagination is exhausted, including empty tails.
    Coverage records what the vendor returned, not an assumed eight-hour calendar.
    """
    if type(start) is not int or type(finish) is not int or start < 0 or start >= finish:
        raise ValueError('Expected a nonempty millisecond interval')
    if finish > int(time.time() * 1000):
        raise ValueError('Historical funding coverage cannot extend into the future')
    events = {}
    cursor = start
    with requests.Session() as client:
        while cursor < finish:
            response = client.get('https://fapi.binance.com/fapi/v1/fundingRate', params={
                'symbol': 'BTCUSDT', 'startTime': cursor, 'endTime': finish - 1, 'limit': 1000,
            }, timeout=30)
            response.raise_for_status()
            rows = response.json()
            if not isinstance(rows, list):
                raise ValueError('Unexpected Binance funding response')
            if not rows:
                break
            last = cursor - 1
            for row in rows:
                timestamp = int(row['fundingTime'])
                if (row['symbol'] != 'BTCUSDT' or row.get('rateType', 'Regular') != 'Regular'
                        or not cursor <= timestamp < finish or timestamp < last):
                    raise ValueError('Unexpected funding instrument, type, order or time')
                rate = float(row['fundingRate'])
                raw_mark = row.get('markPrice')
                if raw_mark in (None, '') and not allow_mark_price_proxy:
                    raise ValueError('Binance omits some old settlement mark prices. Explicit allow_mark_price_proxy=true '
                                     'uses hourly mark-candle opens as an accounting approximation; otherwise use a newer window')
                mark = float(raw_mark) if raw_mark not in (None, '') else None
                if not math.isfinite(rate) or (mark is not None and (not math.isfinite(mark) or mark <= 0)):
                    raise ValueError('Invalid Binance funding rate or mark')
                event = {'exchange': EXCHANGE, 'symbol': 'BTC-USDT', 'settled_at': timestamp,
                         'rate_decimal': rate, 'mark_price': mark,
                         'mark_price_source': 'fundingRate.settlement_mark'}
                if timestamp in events and events[timestamp] != event:
                    raise ValueError('Conflicting funding settlements')
                events[timestamp] = event
                last = timestamp
            cursor = last + 1
            # Fewer than two requests/second stays below the shared 500/5min
            # budget for a single importer. HTTP 429/418 fail without publishing.
            time.sleep(0.6)
        proxy_count = _fill_missing_marks(client, events) if allow_mark_price_proxy else 0
    if not events:
        raise ValueError('No funding returned; refusing to certify empty coverage')
    dataset = {'schema': 1, 'source': SOURCE, 'exchange': EXCHANGE, 'symbol': 'BTC-USDT',
               'start': start, 'finish': finish, 'events': list(events.values()),
               'allow_mark_price_proxy': allow_mark_price_proxy, 'mark_price_proxy_count': proxy_count}
    dataset_id = save_dataset(dataset)
    return describe_dataset(dataset_id, dataset)


def describe_dataset(dataset_id: str, dataset: dict) -> dict:
    timestamps = [row['settled_at'] for row in dataset['events']]
    gaps = [b - a for a, b in zip([dataset['start']] + timestamps,
                                timestamps + [dataset['finish']])]
    supported_timestamps = all(t % 60_000 <= TIMESTAMP_JITTER_MS for t in timestamps)
    complete = bool(timestamps) and max(gaps, default=0) <= MAX_INTERVAL_MS + TIMESTAMP_JITTER_MS
    return {key: value for key, value in dataset.items() if key != 'events'} | {
        'dataset_id': dataset_id, 'event_count': len(timestamps),
        'first_settlement': min(timestamps, default=None), 'last_settlement': max(timestamps, default=None),
        'largest_gap_ms': max((b - a for a, b in zip(timestamps, timestamps[1:])), default=0),
        'status': 'ready' if complete and supported_timestamps else 'incomplete',
        'coverage_complete': complete, 'supported_timestamps': supported_timestamps,
        'coverage_policy': 'vendor_response; BTC maximum eight-hour gap with one-second boundary jitter',
        'timestamp_policy': 'minute boundary; vendor jitter <=1000ms retained in raw settled_at',
        'publication_delay_ms': PUBLICATION_DELAY_MS,
        'rate_unit': 'decimal_fraction',
        'mark_price_source': 'mixed; settlement marks + explicit markPriceKlines.1h_open_proxy'
        if dataset.get('mark_price_proxy_count') else 'fundingRate.settlement_mark',
    }


class FundingState:
    """Per-run event cursor and cash ledger. Disabled runs keep their original result shape."""

    def __init__(self):
        self.dataset_id: str | None = None
        self.events: list[FundingEvent] = []
        self.index = 0
        self.initial_index = 0
        self.ledger: list[dict] = []
        self.latest: dict[tuple[str, str], FundingEvent] = {}
        self.known: dict[tuple[str, str], FundingEvent] = {}
        self.finish = 0
        self.start = 0
        self.description: dict | None = None
        self.excluded_symbols: list[str] = []

    @property
    def enabled(self) -> bool:
        return self.dataset_id is not None

    def configure(self, options: dict | None, start: int, finish: int, routes: list):
        self.__init__()
        if options is None or (isinstance(options, dict) and options.get('mode') == 'disabled'):
            return
        if not isinstance(options, dict) or options.get('mode') != 'historical':
            raise ValueError('funding.mode must be disabled or historical')
        dataset_id = options.get('dataset_id', '')
        dataset = load_dataset(dataset_id)
        if (dataset.get('schema') != 1 or dataset.get('source') != SOURCE
                or dataset.get('exchange') != EXCHANGE or dataset.get('symbol') != 'BTC-USDT'):
            raise ValueError('Unsupported funding dataset')
        if not dataset['start'] <= start < finish <= dataset['finish']:
            raise ValueError('Funding dataset does not cover the full backtest interval')
        if not any(r.exchange == EXCHANGE and r.symbol == 'BTC-USDT' for r in routes):
            raise ValueError('Historical funding requires a Binance BTC-USDT trading route')
        exclusions = options.get('exclude_symbols', [])
        if (not isinstance(exclusions, list) or any(not isinstance(s, str) for s in exclusions)
                or 'BTC-USDT' in exclusions or len(set(exclusions)) != len(exclusions)):
            raise ValueError('Funding exclusions must be unique non-BTC symbols')
        # Multi-asset proxy research may explicitly cost BTC only. Every other
        # perpetual route must be named, and the omission remains in the results.
        for route in routes:
            if route.symbol != 'BTC-USDT' and route.symbol not in exclusions:
                raise ValueError('Other routes require explicit funding.exclude_symbols; only BTC funding is modeled')
        self.excluded_symbols = list(exclusions)
        self.events = [FundingEvent(**row) for row in dataset['events']]
        if any(e.exchange != EXCHANGE or e.symbol != 'BTC-USDT' for e in self.events):
            raise ValueError('Funding event instrument does not match its dataset')
        timestamps = [event.settled_at for event in self.events]
        if timestamps != sorted(set(timestamps)):
            raise ValueError('Duplicate or unordered funding settlements')
        if any(not dataset['start'] <= t < dataset['finish'] for t in timestamps):
            raise ValueError('Funding settlement falls outside declared coverage')
        boundaries = [event.effective_at for event in self.events]
        if len(set(boundaries)) != len(boundaries):
            raise ValueError('Multiple funding settlements in one execution minute')
        # One-minute OHLC cannot locate an intraminute settlement relative to
        # an intrabar fill. Reject it rather than inventing a position size.
        if any(t % 60_000 > TIMESTAMP_JITTER_MS for t in timestamps if start <= t < finish):
            raise ValueError('Funding beyond one-second boundary jitter needs finer execution data')
        # Binance BTC normally settles at most eight hours apart. This is an
        # explicit conservative data gate, not a fabricated payment schedule.
        # More frequent payments work; longer gaps need vendor investigation.
        surrounding = [dataset['start']] + timestamps + [dataset['finish']]
        if not timestamps or any(b - a > MAX_INTERVAL_MS + TIMESTAMP_JITTER_MS for a, b in zip(surrounding, surrounding[1:])):
            raise ValueError('Funding coverage has a gap over eight hours; audit the vendor data')
        self.dataset_id = dataset_id
        self.finish = finish
        self.start = start
        self.description = describe_dataset(dataset_id, dataset)
        while self.index < len(self.events) and self.events[self.index].effective_at < start:
            event = self.events[self.index]
            self.latest[(event.exchange, event.symbol)] = event
            if event.available_at <= start:
                self.known[(event.exchange, event.symbol)] = event
            self.index += 1
        self.initial_index = self.index

    def settle(self, timestamp: int, engine_store):
        """Settle before strategy decisions at T; fills within [T-1m,T) come first.

        The final boundary is exclusive. A strategy entry at T pays the next
        settlement; an exit decided at T still pays this one. This is an OHLC
        execution convention, not a claim about venue ordering within a millisecond.
        """
        for key, event in self.latest.items():
            if event.available_at <= timestamp:
                self.known[key] = event
        while self.index < len(self.events):
            event = self.events[self.index]
            if event.effective_at > timestamp or event.effective_at >= self.finish:
                break
            position = engine_store.positions.get_position(event.exchange, event.symbol)
            if position is not None and position.is_open:
                amount = -position.qty * event.mark_price * event.rate_decimal
                exchange = position.exchange
                exchange.apply_funding(amount)
                trade = engine_store.closed_trades._get_current_trade(event.exchange, event.symbol)
                trade.funding += amount
                self.ledger.append(asdict(event) | {
                    'qty': position.qty, 'cashflow': amount, 'trade_id': str(trade.id),
                    'effective_at': event.effective_at,
                })
            self.latest[(event.exchange, event.symbol)] = event
            if event.available_at <= timestamp:
                self.known[(event.exchange, event.symbol)] = event
            self.index += 1

    def snapshot(self) -> dict:
        return {'mode': 'historical', 'dataset_id': self.dataset_id,
                'cashflow': sum(row['cashflow'] for row in self.ledger),
                'ledger': list(self.ledger), 'rate_kind': 'settled',
                'event_count': len(self.ledger), 'settlements_processed': self.index - self.initial_index,
                'mark_price_proxy_count': sum(row.get('mark_price_source') == 'markPriceKlines.1h_open_proxy'
                                              for row in self.ledger),
                'status': 'applied', 'applied': True, 'scope': ['BTC-USDT'],
                'excluded_symbols': list(self.excluded_symbols),
                'data': self.description, 'effective_fast_mode': False,
                'boundary_policy': 'before_strategy_decisions; finish_exclusive',
                'publication_delay_ms': PUBLICATION_DELAY_MS}

    def history(self, timestamp: int, count: int = 100) -> list[FundingHistoryRow]:
        """Return only settlements that have passed the declared publication lag."""
        if type(count) is not int or not 1 <= count <= 1000:
            raise ValueError('Funding history count must be between 1 and 1000')
        rows = []
        for index in range(self.index - 1, -1, -1):
            event = self.events[index]
            if event.available_at <= timestamp:
                rows.append(FundingHistoryRow(exchange=event.exchange, symbol=event.symbol,
                                              settled_at=event.settled_at, rate_decimal=event.rate_decimal,
                                              mark_price=event.mark_price, mark_price_source=event.mark_price_source,
                                              available_at=event.available_at))
                if len(rows) == count:
                    break
        return list(reversed(rows))
