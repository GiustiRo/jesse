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
- Historical daily metrics: Binance's official `data.binance.vision` USD-M archive.
  On 2026-10-20 its ordered S3 listing starts with **2020-09-01** for BTCUSDT.
  Earlier dates are refused with the first available date; this does not provide
  January–August 2020. Each ZIP is verified against its official SHA-256 CHECKSUM.
  The first daily ZIP, 2021-01-01 and the June 2026 boundary were inspected before
  implementing this importer; a requested full range is still validated file by file.

Archive import requires `allow_archive_assumptions=True`. The files available today
are retrospective snapshots, not proof of original publication. For example, the
2020-09-01 file's current S3 LastModified is **2026-03-18**, and the inspected June
2026 files were replaced in July 2026. Their CHECKSUM and its Last-Modified header
are recorded in the immutable dataset manifest. A later publisher correction gets
a new input version; an overlapping update rejects a changed archived checksum.

The archive CSV includes `create_time`, `symbol`, `sum_open_interest` and
`sum_open_interest_value`, plus unrelated position/flow ratios. This feed uses only
the two OI fields and preserves the reported BTC quantity and USDT value; it does
not infer their valuation formula or import the unrelated indicators. Current
inspected files use five-minute UTC labels from 00:00 through 23:55. Both inspected
2020/2021 files contained 576 rows with 288 distinct labels and exactly identical
OI duplicates: those are counted and deduplicated. Differing values at a repeated
label, including across adjacent files, cause a failure rather than an arbitrary
choice. A next-day 00:00 label is supported only subject to that conflict check.

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
For archives this policy is named
`retrospective_archive_period_label_plus_6m_assumption`; `point_in_time_certified`
is always false and `original_publication_known` is false. No original availability
timestamp is invented. To require strictly recorded original receipt times, use a
separately audited historical recorder rather than interpreting archive labels as
publication times.

The state performs an asof lookup by `available_at`. Future observations remain
invisible. After the configured `max_age_ms` (default ten minutes after availability)
the value becomes `None`. Strategies must handle that absence explicitly. A real
zero OI reported by Binance remains zero and can be distinguished from no data.
The `max_age_ms` option is bounded between five minutes and one day, so an accidental
unit error cannot hold a stale value indefinitely.

## Backend integration contract

`jesse.services.open_interest` exposes:

```python
import_binance_history(start, finish, period='5m', source='rest',
                       allow_archive_assumptions=False, progress_callback=None)
update_dataset(dataset_id, finish, progress_callback=None)
get_archive_catalog()
list_datasets(limit=100)
load_dataset(dataset_id)
describe_dataset(dataset_id, dataset)
get_current(symbol='BTC-USDT')
```

All import/update times are UTC milliseconds and ranges are `[start, finish)`.
Datasets live under `storage/open-interest/<sha256>.json`; checksums are verified
on read. Reimporting identical normalized data returns the same identifier. Updates
preserve the old snapshot and reject conflicting revisions in their overlap.
Library listings cache at most 200 metadata summaries in memory, keyed by absolute
file path and size/mtime/ctime nanosecond fingerprint. A cold listing still verifies
checksum and schema; changed or removed files invalidate their cached summary.
Explicit `load_dataset` and dataset reads always verify stored bytes and never use
this listing cache. Observation arrays and archive manifests are not cached.
Only completed successful vendor reads publish a new dataset; HTTP failures,
malformed responses and empty history never certify coverage.

`source='archive'` imports verified daily ZIPs without the REST retention limit.
`source='auto'` selects archives for older dates and REST for the most recent
29 complete days, avoiding dependence on same-day ZIP publication. Use `auto`
for a long historical dataset that will later be updated: the chosen policy is
preserved even if its first imported window contains archives only. Sources and
the actual REST subrange remain explicit in dataset metadata.

CDN downloads use at most four workers, with four outstanding day requests rather
than an unbounded work queue. Each worker has its own HTTP session. Progress is
delivered in date order as a dictionary containing `phase`, `source`, `fetched_days`,
`total_days` and `current_date`; REST also reports processed/total buckets. An
exception raised by the callback stops the import. Verified content-addressed ZIPs
survive cancellation and are rechecked/reused on restart. Missing daily CHECKSUMs
remain missing days and make coverage incomplete; they are never filled with zero.
There is no final dataset published for an interrupted archive download.

The immutable snapshot stores the complete per-file manifest. Ordinary MCP/API
metadata returns its counts and at most ten missing dates so multi-year results
do not dump thousands of manifest rows into the conversation. Use the background
market-data job API for a multi-year import rather than relying on a synchronous
HTTP connection remaining open for the full transfer.

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
unsupported source options, update idempotence and revisions, no-lookahead boundaries,
stale handling and live public receipt timestamps. All HTTP responses are mocked;
no exchange credentials or orders are needed.
Archive tests additionally cover the actual publisher CSV schema and identical
historical duplicates, explicit retrospective policy, first-available-date errors,
raw/checksum cache validation, cross-day conflicts, missing files, updates,
archive/REST merging and cancellation with bounded downloads.

## Earlier-history alternatives

Binance's currently listed free archive starts September 2020. Tardis documents
its Binance OI recorder from May 2020 (raw channel May 12; normalized
`derivative_ticker` May 13), with original local receipt timestamps. Most dates
require licensed access; first-of-month samples are public. This is a candidate
for a separate connector, not an already integrated or acquired dataset. It still
does not establish January 2020 OI coverage. Coin Metrics also provides a recorded
market-open-interest product, but usable coverage/licensing must be checked for the
exact Binance BTCUSDT market before any connector or purchase is proposed.

## Primary references

- [Binance REST market data: Open Interest / Open Interest Statistics](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data)
- [Binance Public Data README: publication and update policy](https://github.com/binance/binance-public-data)
- [Binance BTCUSDT daily metrics archive](https://data.binance.vision/?prefix=data/futures/um/daily/metrics/BTCUSDT/)
- [Official ordered bucket listing](https://s3-ap-northeast-1.amazonaws.com/data.binance.vision/?list-type=2&prefix=data/futures/um/daily/metrics/BTCUSDT/&max-keys=2)
- [Archive metrics timestamp report, issue 491](https://github.com/binance/binance-public-data/issues/491)
- [Historical metrics provenance question, issue 509](https://github.com/binance/binance-public-data/issues/509)
- [Tardis Binance futures recorder coverage](https://docs.tardis.dev/historical-data-details/binance-futures)
- [Coin Metrics market-open-interest documentation](https://github.com/coinmetrics/docs-website/blob/master/market-data/market-open-interest.md)

The issue reports are user-submitted evidence of unresolved questions, not an
official Binance confirmation of a timestamp change or of historical availability.
