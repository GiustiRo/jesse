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
# Pre-existing BTC snapshots and configs keep this default; content hashes of
# BTC datasets are unchanged because the dataset schema did not change.
DEFAULT_SYMBOL = 'BTC-USDT'


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


def vendor_symbol(symbol: str) -> str:
    """Jesse `BASE-USDT` to Binance USD-M `BASEUSDT`; only USDT-margined linear perpetuals.

    The settlement and mark-price accounting (qty * mark * rate in USDT) is only
    valid for USDT-quoted linear contracts, so other quotes are refused rather
    than mis-costed.
    """
    if not isinstance(symbol, str) or not re.fullmatch(r'[A-Z0-9]{2,20}-USDT', symbol):
        raise ValueError('Funding symbol must be a Binance USD-M perpetual like BTC-USDT or ETH-USDT')
    return symbol.replace('-', '')


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


def list_datasets(symbol: str | None = None) -> list:
    if not _root().exists():
        return []
    rows = (describe_dataset(path.stem, load_dataset(path.stem)) for path in _root().glob('*.json'))
    return sorted((row for row in rows if symbol is None or row['symbol'] == symbol),
                  key=lambda item: item['finish'], reverse=True)


def update_dataset(dataset_id: str, finish: int) -> dict:
    """Re-fetch the explicit full window so vendor corrections create a new ID.

    Funding snapshots are small (usually three events/day per symbol). A full
    refresh audits the overlap instead of silently merging a revised final rate.
    """
    old = load_dataset(dataset_id)
    if finish < old['finish']:
        raise ValueError('An update cannot shorten existing coverage')
    result = import_binance_history(old['start'], finish, old.get('allow_mark_price_proxy', False),
                                    old.get('symbol', DEFAULT_SYMBOL))
    return result | {'previous_dataset_id': dataset_id, 'changed': result['dataset_id'] != dataset_id}


def _fill_missing_marks(client, events: dict, instrument: str) -> int:
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
            'symbol': instrument, 'interval': '1h', 'startTime': cursor,
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


def import_binance_history(start: int, finish: int, allow_mark_price_proxy: bool = False,
                           symbol: str = DEFAULT_SYMBOL) -> dict:
    """Fetch an explicit [start, finish) window of one perpetual. Public data needs no account keys.

    The API's ascending, inclusive pagination is exhausted, including empty tails.
    Coverage records what the vendor returned, not an assumed eight-hour calendar.
    """
    if type(start) is not int or type(finish) is not int or start < 0 or start >= finish:
        raise ValueError('Expected a nonempty millisecond interval')
    if finish > int(time.time() * 1000):
        raise ValueError('Historical funding coverage cannot extend into the future')
    instrument = vendor_symbol(symbol)
    events = {}
    cursor = start
    with requests.Session() as client:
        while cursor < finish:
            response = client.get('https://fapi.binance.com/fapi/v1/fundingRate', params={
                'symbol': instrument, 'startTime': cursor, 'endTime': finish - 1, 'limit': 1000,
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
                if (row['symbol'] != instrument or row.get('rateType', 'Regular') != 'Regular'
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
                event = {'exchange': EXCHANGE, 'symbol': symbol, 'settled_at': timestamp,
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
        proxy_count = _fill_missing_marks(client, events, instrument) if allow_mark_price_proxy else 0
    if not events:
        raise ValueError('No funding returned; refusing to certify empty coverage')
    dataset = {'schema': 1, 'source': SOURCE, 'exchange': EXCHANGE, 'symbol': symbol,
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
        'coverage_policy': f"vendor_response; {dataset['symbol'].split('-')[0]} maximum eight-hour gap "
                           'with one-second boundary jitter',
        'timestamp_policy': 'minute boundary; vendor jitter <=1000ms retained in raw settled_at',
        'publication_delay_ms': PUBLICATION_DELAY_MS,
        'rate_unit': 'decimal_fraction',
        'mark_price_source': 'mixed; settlement marks + explicit markPriceKlines.1h_open_proxy'
        if dataset.get('mark_price_proxy_count') else 'fundingRate.settlement_mark',
    }


class FundingState:
    """Per-run event cursor and cash ledger. Disabled runs keep their original result shape.

    Each dataset covers one symbol. Events of all configured datasets share one
    cursor ordered by execution minute, then symbol, so a single-dataset run is
    replayed exactly as before multi-symbol support.
    """

    def __init__(self):
        self.dataset_id: str | None = None
        self.dataset_ids: list[str] = []
        self.symbols: list[str] = []
        self.events: list[FundingEvent] = []
        self.index = 0
        self.initial_index = 0
        self.ledger: list[dict] = []
        self.latest: dict[tuple[str, str], FundingEvent] = {}
        self.known: dict[tuple[str, str], FundingEvent] = {}
        self.finish = 0
        self.start = 0
        self.description: dict | None = None
        self.descriptions: dict[str, dict] = {}
        self.excluded_symbols: list[str] = []
        # `dataset_ids` configs report per-symbol evidence; legacy `dataset_id`
        # configs keep their historical snapshot shape byte for byte.
        self.multi_config = False

    @property
    def enabled(self) -> bool:
        return bool(self.dataset_ids)

    @staticmethod
    def _requested_ids(options: dict) -> tuple[list, bool]:
        if 'dataset_ids' in options:
            if 'dataset_id' in options:
                raise ValueError('Use funding.dataset_id or funding.dataset_ids, not both')
            ids = options['dataset_ids']
            if (not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids)
                    or len(set(ids)) != len(ids)):
                raise ValueError('funding.dataset_ids must be a nonempty list of unique dataset IDs')
            return ids, True
        return [options.get('dataset_id', '')], False

    @staticmethod
    def _load_events(dataset: dict, start: int, finish: int) -> list[FundingEvent]:
        """Validate one symbol's snapshot; every check is per dataset, never pooled."""
        symbol = dataset.get('symbol')
        if (dataset.get('schema') != 1 or dataset.get('source') != SOURCE
                or dataset.get('exchange') != EXCHANGE):
            raise ValueError('Unsupported funding dataset')
        vendor_symbol(symbol)
        if not dataset['start'] <= start < finish <= dataset['finish']:
            raise ValueError(f'Funding dataset for {symbol} does not cover the full backtest interval')
        events = [FundingEvent(**row) for row in dataset['events']]
        if any(e.exchange != EXCHANGE or e.symbol != symbol for e in events):
            raise ValueError('Funding event instrument does not match its dataset')
        timestamps = [event.settled_at for event in events]
        if timestamps != sorted(set(timestamps)):
            raise ValueError('Duplicate or unordered funding settlements')
        if any(not dataset['start'] <= t < dataset['finish'] for t in timestamps):
            raise ValueError('Funding settlement falls outside declared coverage')
        boundaries = [event.effective_at for event in events]
        if len(set(boundaries)) != len(boundaries):
            raise ValueError('Multiple funding settlements in one execution minute')
        # One-minute OHLC cannot locate an intraminute settlement relative to
        # an intrabar fill. Reject it rather than inventing a position size.
        if any(t % 60_000 > TIMESTAMP_JITTER_MS for t in timestamps if start <= t < finish):
            raise ValueError('Funding beyond one-second boundary jitter needs finer execution data')
        # Binance USD-M perpetuals settle at most eight hours apart (some every
        # four or one hour). This is an explicit conservative data gate, not a
        # fabricated payment schedule; longer gaps need vendor investigation.
        surrounding = [dataset['start']] + timestamps + [dataset['finish']]
        if not timestamps or any(b - a > MAX_INTERVAL_MS + TIMESTAMP_JITTER_MS for a, b in zip(surrounding, surrounding[1:])):
            raise ValueError(f'Funding coverage for {symbol} has a gap over eight hours; audit the vendor data')
        return events

    def configure(self, options: dict | None, start: int, finish: int, routes: list):
        self.__init__()
        if options is None or (isinstance(options, dict) and options.get('mode') == 'disabled'):
            return
        if not isinstance(options, dict) or options.get('mode') != 'historical':
            raise ValueError('funding.mode must be disabled or historical')
        dataset_ids, multi_config = self._requested_ids(options)
        datasets = {dataset_id: load_dataset(dataset_id) for dataset_id in dataset_ids}
        symbols = [dataset.get('symbol') for dataset in datasets.values()]
        if len(set(symbols)) != len(symbols):
            raise ValueError('Each funding dataset must cover a different symbol')
        events = []
        for dataset in datasets.values():
            events += self._load_events(dataset, start, finish)
        scope = ', '.join(symbols)
        if not any(r.exchange == EXCHANGE and r.symbol in symbols for r in routes):
            raise ValueError(f'Historical funding requires a Binance {scope} trading route')
        exclusions = options.get('exclude_symbols', [])
        if (not isinstance(exclusions, list) or any(not isinstance(s, str) for s in exclusions)
                or any(s in symbols for s in exclusions) or len(set(exclusions)) != len(exclusions)):
            raise ValueError('Funding exclusions must be unique symbols without a configured funding dataset')
        # A route is costed only from its own symbol's dataset. Every route
        # without one must be named, and the omission remains in the results.
        for route in routes:
            if route.symbol not in symbols and route.symbol not in exclusions:
                raise ValueError(f'Other routes require explicit funding.exclude_symbols; only {scope} funding is modeled')
        self.excluded_symbols = list(exclusions)
        # Same-minute settlements of different symbols are independent cash
        # flows; ordering them by symbol only makes the ledger reproducible.
        self.events = sorted(events, key=lambda event: (event.effective_at, event.symbol))
        self.dataset_ids = list(dataset_ids)
        self.symbols = symbols
        self.multi_config = multi_config
        self.descriptions = {dataset['symbol']: describe_dataset(dataset_id, dataset)
                             for dataset_id, dataset in datasets.items()}
        if len(dataset_ids) == 1:
            self.dataset_id = dataset_ids[0]
            self.description = self.descriptions[symbols[0]]
        self.finish = finish
        self.start = start
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
        result = {'mode': 'historical', 'dataset_id': self.dataset_id,
                  'cashflow': sum(row['cashflow'] for row in self.ledger),
                  'ledger': list(self.ledger), 'rate_kind': 'settled',
                  'event_count': len(self.ledger), 'settlements_processed': self.index - self.initial_index,
                  'mark_price_proxy_count': sum(row.get('mark_price_source') == 'markPriceKlines.1h_open_proxy'
                                                for row in self.ledger),
                  'status': 'applied', 'applied': True, 'scope': list(self.symbols),
                  'excluded_symbols': list(self.excluded_symbols),
                  'data': self.description, 'effective_fast_mode': False,
                  'boundary_policy': 'before_strategy_decisions; finish_exclusive',
                  'publication_delay_ms': PUBLICATION_DELAY_MS}
        if self.multi_config:
            cash = {symbol: 0 for symbol in self.symbols}
            for row in self.ledger:
                cash[row['symbol']] += row['cashflow']
            result |= {'dataset_ids': list(self.dataset_ids), 'datasets': dict(self.descriptions),
                       'cashflow_by_symbol': cash}
        return result

    def history(self, timestamp: int, count: int = 100, symbol: str | None = None) -> list[FundingHistoryRow]:
        """Return only settlements that have passed the declared publication lag.

        With several datasets the caller must choose a symbol: silently pooling
        BTC and ETH rates into one window would corrupt rate statistics.
        """
        if type(count) is not int or not 1 <= count <= 1000:
            raise ValueError('Funding history count must be between 1 and 1000')
        if symbol is not None and self.enabled and symbol not in self.symbols:
            raise ValueError(f'No funding dataset is configured for {symbol}')
        if symbol is None and len(self.symbols) > 1:
            raise ValueError('Several funding datasets are configured; pass the symbol whose history is needed')
        rows = []
        for index in range(self.index - 1, -1, -1):
            event = self.events[index]
            if symbol is not None and event.symbol != symbol:
                continue
            if event.available_at <= timestamp:
                rows.append(FundingHistoryRow(exchange=event.exchange, symbol=event.symbol,
                                              settled_at=event.settled_at, rate_decimal=event.rate_decimal,
                                              mark_price=event.mark_price, mark_price_source=event.mark_price_source,
                                              available_at=event.available_at))
                if len(rows) == count:
                    break
        return list(reversed(rows))
