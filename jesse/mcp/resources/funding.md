# Binance funding and open interest

This project supports historical funding of **any Binance USD-M USDT-margined
perpetual** (one dataset per symbol: `BTC-USDT`, `ETH-USDT`, ...) and historical
open interest for **BTC-USDT only**, without ML. Live funding/OI remains BTC-only. Funding is optional and disabled by default. Data import and draft
configuration never start a trading session or place an order.

## Sources and units

- Final payments: public `/fapi/v1/fundingRate`. Rates are decimal fractions:
  `0.0001 = 0.01%`, so a 10,000 USDT position pays/receives 1 USDT.
- Settlement marks come from that same response. Some older rows have empty
  marks. Default import refuses them. `allow_mark_price_proxy=true` explicitly
  permits `/fapi/v1/markPriceKlines` hourly **open** at the settlement boundary;
  these costs are approximations. Every affected row and snapshot records the
  source; the dashboard shows the proxy count.
- Live estimate, mark and next settlement: public `/fapi/v1/premiumIndex`.
- Actual account payments: signed `/fapi/v1/income`, `incomeType=FUNDING_FEE`.
  A live account journal is account scope, never invented per-strategy income.
- OI: public `/fapi/v1/openInterest` and `/futures/data/openInterestHist` for
  current/recent observations. Historical REST is limited to the recent month
  (importer conservatively uses 30 days). Binance's public daily metrics ZIPs
  extend the history from September 2020. Downloads verify the published SHA-256,
  retain provenance and detect conflicting duplicates and missing coverage.
  Archive use requires `allow_archive_assumptions=true`: original publication
  times are unknown and files can be revised years later. The label+6m replay
  lag is a research assumption, **not certified point-in-time 2020 data**.

No API keys are needed for historical data or public observations. Signed live
reads use the session's existing saved Binance credentials. Do not copy account
keys into research scripts, tool arguments, source control or reports.

## Backtest workflow through MCP

1. `import_funding(start_date, finish_date, allow_mark_price_proxy=False,
   symbol="BTC-USDT")` imports an explicit UTC `[start,finish)` window of one
   symbol and returns an immutable `dataset_id`, its `symbol`, event count,
   coverage, gaps, timestamp assumptions and price provenance. `symbol` uses
   Jesse's form (`ETH-USDT`); omitting it imports BTC exactly as before, with
   the same content hash for the same vendor history.
2. `list_funding_datasets(symbol=None)`, `get_funding_dataset` inspect snapshots;
   `update_funding_dataset(id,finish_date)` re-fetches the explicit window and
   creates another ID if the vendor history or coverage changed. It always keeps
   the dataset's own symbol. Old runs keep
   the old ID. No automatic substitution of the newest dataset.
   `get_funding_dataset(id,include_events=True,offset=0,limit=50)` reads bounded
   raw settlement pages for research; the OI equivalent pages observations with
   their declared availability times. No need to read backend storage directly.
3. Create a normal backtest draft, then
   `configure_session_market_data(session_id, funding={"mode":"historical",
   "dataset_id":"..."})` for one symbol, or `"dataset_ids":["<btc>","<eth>"]`
   for several (one per symbol). Configuration belongs to **form.config**, not global
   settings. Run using normal `run_backtest`. The dashboard's Import Data tabs
   performs the same import/configuration/read requests. Reload a previously open
   backtest tab after changing its draft configuration.
4. Inspect `get_session_funding(session_id)` or `get_session_results` section
   `funding`. Summaries omit the bulky ledger; paged reads and analysis exports
   retain it. Metrics contain `funding.applied`, dataset/version, signed cashflow,
   scope, exclusions, and a payment ledger (with `symbol`) linked to trade IDs.
   `dataset_ids` runs also report `dataset_ids`, per-symbol `datasets`
   descriptions and `cashflow_by_symbol`; their `dataset_id`/`data` are `null`
   when more than one dataset was used.

### Per-symbol funding

Each route pays funding **only from the dataset of its own symbol**: an
`ETH-USDT` position settles ETH rates against ETH settlement marks, never BTC's.
`scope` lists the symbols with a dataset. Every other route symbol must be listed
explicitly in `funding.exclude_symbols`; there is no fallback to another
symbol's rates and no silent zero. Exclusions cannot name a funded symbol, and
two datasets of the same symbol in one run are refused. The dashboard selects
one version per symbol, asks for explicit exclusions of the remaining routes, and
the result displays them. Spot and SPX/PAXG proxy prices are not automatically
assigned any Binance funding or assumed fully costed.

Validation (coverage of the full window, the eight-hour gap gate, timestamp
jitter, duplicates) runs on each dataset separately, so one symbol's events can
never mask a gap in another. Same-minute settlements of different symbols are
independent cash flows, ordered by symbol in the ledger for reproducibility.

A legacy `dataset_id` config with a BTC dataset is replayed exactly as before
multi-symbol support (pinned by a golden regression test): same dataset IDs,
cashflows, metrics and result shape.

Example: an ETH short-first study with BTC as a second route.

```python
import_funding("2020-01-01", "2026-10-01", allow_mark_price_proxy=True, symbol="ETH-USDT")
configure_session_market_data(session_id, funding={
    "mode": "historical", "dataset_ids": ["<btc dataset_id>", "<eth dataset_id>"]})
# or ETH only, other routes explicitly unfunded:
configure_session_market_data(session_id, funding={
    "mode": "historical", "dataset_id": "<eth dataset_id>", "exclude_symbols": ["PAXG-USDT"]})
```

Binance omits settlement marks on early rows for ETH too (e.g. 2020), so a
window starting there needs `allow_mark_price_proxy=True`; the proxy uses the
same symbol's hourly mark-price candles.

For OI use `import_open_interest`, `list_open_interest_datasets`,
`get_open_interest_dataset`, `update_open_interest_dataset`, and the draft's
`open_interest={"mode":"historical","dataset_id":"..."}`. Missing or stale
OI is `None`, never a zero or an interpolation across gaps.
An archive dataset with gaps requires the draft setting
`open_interest.allow_missing_observations=True` before consumption. The dashboard
offers a separate unchecked acknowledgement for this case. The result records
that decision; it does not repair coverage or change the missing-value policy.

`import_open_interest(...,source="archive",allow_archive_assumptions=True)`
uses the verified daily public archive. `source="auto"` combines archives with
recent REST observations. Dates before actual archive coverage are rejected;
there is no invented January–August 2020 series. Funding final rates already
cover January 2020 onward; some older settlement marks require the explicit
price approximation above. Historical estimated future funding remains unavailable.

Multi-year OI downloads run as background jobs. Request `background=True`, or
use an archive/auto window longer than seven days (background is automatic).
Poll `get_open_interest_import_status(job_id)` until `finished`, `failed` or
`interrupted`; only `finished.result` identifies a published dataset. Updates
accept the same background option and preserve the selected source/assumptions.
Restarted jobs are marked interrupted; re-importing reuses verified daily files.
The dashboard discovers jobs started through MCP as well as jobs initiated from
its own import form. The canonical view is `/#/candles/` (Import Data); the old
`/funding/index.html` URL remains compatible for existing links.

## Timeframes and alignment

Execution candles are stored at one minute; other strategy timeframes are
generated from those candles. Funding is an event series, usually every eight
hours for BTC and ETH (some perpetuals settle every four or one hour), not a
candle timeframe: each payment uses the position at that
event even if the strategy runs at 1h or 4h. Final funding signal availability
follows the one-minute publication assumption described below.

OI is an independent five-minute observation series. At each engine timestamp,
the strategy receives the most recent observation whose `available_at` has
passed. Under label+6m, the 10:00 label first becomes usable at 10:06, never at
10:00. No interpolation invents one-minute samples; stale/missing data is None.
Live uses receipt timestamps and source freshness instead of replaying archive
publication assumptions.

## Accounting and execution assumptions

The signed cashflow is `-signed_qty * settlement_mark * rate_decimal`. Positive
funding debits longs and credits shorts; negative funding reverses that. Leverage
does not multiply the rate again. Actual position quantity at the event is used,
including partial closes. Cash changes immediately and affects later position
sizing. Closed-trade PnL includes financing separately from execution fees.

The OHLC convention processes fills during `[T-1m,T)` first, then settles funding
at T, then strategy decisions and their market orders. An entry decided at T does
not pay that event; an exit decided at T still does. Final date is exclusive.
Binance timestamp jitter up to 1,000 ms after a minute boundary is assigned to
that boundary for accounting; raw timestamps are retained. Larger intraminute
offsets are refused because minute OHLC cannot identify the exact position size.
This is a documented replay approximation, not a claim about millisecond venue
ordering. Final rates become usable for signals at the next minute boundary;
original historical publication timestamps are not supplied by Binance.

Funding forces full minute replay even when the form requests fast mode.
Execution candles of every funded symbol must be uninterrupted and span the full
requested window; other instruments may use sparse timestamp replay. Missing
funding coverage, duplicate/effective timestamps, conflicting history, and gaps
above the explicit eight-hour coverage gate (plus timestamp jitter) of any
dataset are refused. No fabricated zero
payments. A historical debit that exhausts available margin raises an explicit
error: Jesse does not simulate venue-specific funding consumption of isolated
collateral after free margin is gone.

## Strategy access

```python
# Same final-rate signal meaning in historical backtest and enabled live.
final_rate = self.settled_funding_rate       # float decimal fraction | None
final_time = self.settled_funding_timestamp # UTC milliseconds | None
oi = self.open_interest                    # BTC base quantity | None
oi_time = self.open_interest_timestamp      # observation label, UTC ms | None

# Historical-only bounded causal window (oldest first), no future rows.
# Defaults to this route's symbol when it has a dataset; each row has `symbol`.
rows = self.get_funding_history(count=30)
# Another configured symbol, e.g. BTC funding as a signal on an ETH route.
btc_rows = self.get_funding_history(count=30, symbol="BTC-USDT")

# Live-only estimate of the next payment. NOT a historical final rate.
estimate = self.funding_rate
next_time = self.next_funding_timestamp
```

With several datasets and a route symbol that has none, `symbol=` is required:
rates of different symbols are never pooled into one window. A symbol without a
configured dataset raises instead of returning an empty window.
`settled_funding_rate` always reads the route's own symbol.

Historical estimated rates are unavailable (`None` with funding enabled).
Disabled legacy backtests preserve their old `funding_rate == 0` behavior.
The final historical rate is not a known future rate. OI historical availability
uses an explicit period-label plus six-minute lag assumption, with a ten-minute
default maximum age; provenance and missing policy are in each OI snapshot.

## Live configuration and validation boundary

Live session config accepts `funding={"mode":"live"}` and/or
`open_interest={"mode":"live"}`. Existing MCP draft/start configuration preserves
these fields. Disabled sessions make no new funding/OI requests.

The OSS HTTP adapter refreshes public observations every 30 seconds and actual
funding income every 60 seconds. Data older than 90 seconds, bad data, unreconciled
position changes or failed income recovery block new exposure. Protective
reduce-only exits remain available. It confirms cancellation of pending entries
and reconciles fills that race cancellation. An already in-flight venue fill
cannot be undone by this guard.

REST order snapshots can give several fills the same millisecond `updateTime`.
Jesse orders those fills only when the existing position and reduce-only rules
prove a unique sequence; random Jesse UUIDs are never treated as exchange time.
If the sequence remains ambiguous, reconciliation blocks new exposure before
changing the local position or running lifecycle hooks. Resolving that condition
requires explicit reconciliation against exchange trade history; the adapter
does not invent a chronology or automatically adopt the account position.

Income is persisted atomically, deduplicated by transaction ID with decimal
cashflow, and re-read to recover delayed records. **The live wallet already
contains funding: the journal never debits it again.** It does not scale account
income by the UI allocation or attribute it to a trade without evidence.

Enabling these features currently requires one-way mode, a flat BTC account and
no pre-existing BTC orders. It refuses unexplained external position changes.
Changed feature flags need a new session; a saved journal cannot be silently
reinterpreted. Paper funding/OI is explicitly refused before connecting because
real account income cannot cost a simulated position.

Live validation uses mocked venue responses and the native order/position
lifecycle. This is not evidence of a real authenticated Binance session or live
profitability. Start a real session only with the user's separate authorization.
Use `get_session_funding(session_id, live=True)` for the local persisted journal;
the dashboard shows estimate freshness, actual account income and OI status.

## Official references

- [Binance market data](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data)
- [Binance account API](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account)
- [Binance public data](https://github.com/binance/binance-public-data)
- [Binance BTC metrics archive](https://data.binance.vision/?prefix=data/futures/um/daily/metrics/BTCUSDT/)
- [Tardis Binance coverage](https://docs.tardis.dev/historical-data-details/binance-futures)

Alternative vendors require their own adapter, rights and coverage audit. Tardis
documents normalized OI from May 2020 (not January); full history requires access
beyond its first-day-of-month free samples. Coin Metrics exposes an OI catalogue
but its public/community API refused Binance BTC market access during this audit.
Neither source was purchased or silently substituted for Binance archive data.

These are Binance venue data. Other venues, non-USDT (inverse or USDC-margined)
contracts and historic estimated funding need their own adapters and coverage
audits. Importing a new USDT-M symbol needs no code change, but its coverage and
settlement interval should be checked in the returned diagnostics.
