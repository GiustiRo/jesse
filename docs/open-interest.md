# Binance BTC open interest

Open interest is a signal input, not a trading fee or funding payment. It does not
change wallet cash. The feed implemented here is Binance USD-M `BTC-USDT` only.

## Sources and honest coverage

- Current public observation: `GET /fapi/v1/openInterest`. Quantity is returned with
  the venue timestamp and the local receipt timestamp; its quote value is unknown
  and is represented as `None`, never inferred from an unrelated last trade price.
- Recent five-minute history: `GET /futures/data/openInterestHist`, ascending
  pagination with an inclusive cursor and maximum 500 rows per page. Binance
  documents only the latest one month; this importer accepts at most 30 days.
  Requests advance by five-minute UTC bucket labels, since the API can round a
  `last_timestamp + 1ms` cursor back to its preceding bucket. Exact page overlaps
  are deduplicated, conflicting revisions fail, and a nonempty page that makes no
  progress fails explicitly instead of certifying partial coverage. Each request
  covers at most 500 five-minute buckets: a broad request can select its latest
  500 observations and otherwise silently omit the older part. Empty windows are
  preserved as gaps while later windows are still queried. Historical
  labels off the five-minute grid are refused rather than silently skipped.
- Binance's public metrics archives are a different historical product. Importing
  them is deliberately refused pending an audit of units, observation labels,
  original publication timestamps, revisions and coverage. This implementation
  does not claim to provide usable OI history for 2020–2025.

The official REST documentation says its timestamps are period ends and that
periods without trades may be omitted. We preserve gaps, record their number and
maximum duration, and never interpolate them or substitute zero.
Metadata includes expected and missing observation counts, leading/trailing gaps,
`coverage_complete` and a `ready`/`incomplete` status. These are calculated on read,
so an older truncated snapshot remains immutable but is visibly incomplete.

## Availability and stale data

Each historical observation has `observed_at` and `available_at`. Because original
publication timestamps are not supplied, `available_at = observed_at + 6 minutes`
is an explicit research assumption: one full five-minute period plus one minute
of publication allowance. This is conservative against a one-period label shift;
it does not certify historical publication provenance or eliminate archive revision
bias. Do not describe results as strict point-in-time validation on this basis.

The state performs an asof lookup by `available_at`. Future observations remain
invisible. After the configured `max_age_ms` (default ten minutes after availability)
the value becomes `None`. Strategies must handle that absence explicitly. A real
zero OI reported by Binance remains zero and can be distinguished from no data.
The `max_age_ms` option is bounded between five minutes and one day, so an accidental
unit error cannot hold a stale value indefinitely.

## Backend integration contract

`jesse.services.open_interest` exposes:

```python
import_binance_history(start, finish, period='5m', source='rest')
update_dataset(dataset_id, finish)
list_datasets(limit=100)
load_dataset(dataset_id)
describe_dataset(dataset_id, dataset)
get_current(symbol='BTC-USDT')
```

All import/update times are UTC milliseconds and ranges are `[start, finish)`.
Datasets live under `storage/open-interest/<sha256>.json`; checksums are verified
on read. Reimporting identical normalized data returns the same identifier. Updates
preserve the old snapshot and reject conflicting revisions in their overlap.
Only completed successful vendor reads publish a new dataset; HTTP failures,
malformed responses and empty history never certify coverage.

`OpenInterestState.configure(options, start, finish, routes)` accepts:

```json
{"mode":"historical","dataset_id":"<sha256>","max_age_ms":600000}
```

Omitting it or using `{"mode":"disabled"}` leaves the feed off. `advance(time)`
updates the replay clock; `current(exchange, symbol, timestamp=None)` returns an
`OpenInterestObservation` or `None`. Its fields are `quantity_base`, `value_quote`,
`observed_at`, `available_at`, `exchange` and `symbol`. `snapshot()` provides status
and the latest usable observation for metrics/dashboard integration.

## Validation

`tests/test_open_interest.py` exercises canonical persistence and checksum failures,
pagination, duplicate/conflicting/malformed responses, empty data, gaps, retention,
unsupported archives, update idempotence and revisions, no-lookahead boundaries,
stale handling and live public receipt timestamps. All HTTP responses are mocked;
no exchange credentials or orders are needed.

## Primary references

- [Binance REST market data: Open Interest / Open Interest Statistics](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data)
- [Binance Public Data README: publication and update policy](https://github.com/binance/binance-public-data)
- [Archive metrics timestamp report, issue 491](https://github.com/binance/binance-public-data/issues/491)
- [Historical metrics provenance question, issue 509](https://github.com/binance/binance-public-data/issues/509)

The issue reports are user-submitted evidence of unresolved questions, not an
official Binance confirmation of a timestamp change or of historical availability.
