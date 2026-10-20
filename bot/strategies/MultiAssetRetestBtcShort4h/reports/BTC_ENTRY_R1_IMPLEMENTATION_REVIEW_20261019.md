# Entry R1 implementation and source diff — 2026-10-19

Frozen protocol: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_FROZEN_PROTOCOL_20261019.md. No drafts, backtests or analysis jobs created in this implementation step. All writes and readbacks through Jesse MCP.

Base PortCompareBtc4h copied completely into three standalone strategies. No imports from mutable strategy modules; originals untouched. Global risk, reservation ledger, capacity counters and every long/position-management method preserved byte for byte. Class names changed only for the clones. Intended future run setting debug=true is a draft setting; no economic strategy parameter changes for logging.

The sole changed existing method in EACH clone is _short_plan: after the original ATR/fee/distance eligibility, immediately before capital and sizing, add:

```python
        if not self._entry_gate(c, entry, atr):
            return False
```

The sole added method is _entry_gate. No original methods removed. All other source bytes equal base after reversing class rename and removing that helper and its call; checked against fresh MCP readback. This includes _plan, _signal, all lifecycle hooks, _ledger, _key, _capital, _committed, _volatility_share, _record_capacity and terminate.

Causality: last array row must equal closed_candle_open_time, close time <= current time; all required timestamps finite, consecutive exactly four hours. R101/R102 use seven closes for six close-to-close intervals; only six corresponding volumes enter R101. Ties carry zero. R103 uses31 rows but only lows of the30 strictly prior rows. No future/pivot confirmation or in-progress bar access. Invalid required windows fail closed. Helpers have no mutable state; occupancy/long priority stay engine baseline.

Original entry=min(signal_low,close−.25ATR), distance=EMA20−entry, stop/target1.5ATR/72h untouched. Sizing runs only after gate, and all downstream formulae stay identical. The R102 difference-of-logs computes the exact frozen log return without a potentially overflowing ratio. The R101 volume classifier is a proxy by return sign, not aggressor delta. Thresholds24h/half/five-day floor fixed before tests; no selection using dates.

## BtcEntryR101

Source: strategies/BtcEntryR101/__init__.py. Fresh readback equals submitted source. Full normalized base equality PASS. Changed existing methods: `_short_plan`; added: `_entry_gate`.

```python
    def _entry_gate(self, candles, entry, atr) -> bool:
        """Require greater down-return volume over the last six closed 4h bars.

        Signed candle volume is only an OHLCV participation proxy, not aggressor
        delta. Six bars define one fixed day; ties carry no directional weight.
        """
        if len(candles) < 7:
            return False
        window = candles[-7:]
        stamps = window[:, 0]
        closes = window[:, 2]
        volumes = window[1:, 5]
        if (not np.all(np.isfinite(stamps))
                or not np.all(np.diff(stamps) == 14_400_000)
                or stamps[-1] != self.closed_candle_open_time
                or stamps[-1] + 14_400_000 > self.time
                or not np.all(np.isfinite(closes)) or np.any(closes <= 0)
                or not np.all(np.isfinite(volumes)) or np.any(volumes <= 0)):
            return False
        changes = np.diff(closes)
        down_volume = float(np.sum(volumes[changes < 0]))
        up_volume = float(np.sum(volumes[changes > 0]))
        return down_volume > up_volume

```

## BtcEntryR102

Source: strategies/BtcEntryR102/__init__.py. Fresh readback equals submitted source. Full normalized base equality PASS. Changed existing methods: `_short_plan`; added: `_entry_gate`.

```python
    def _entry_gate(self, candles, entry, atr) -> bool:
        """Reject a day whose downside is explained mostly by one 4h shock.

        The half-share threshold defines absence of a majority contributor;
        no stop, target, or original RSI threshold is adjusted by this gate.
        """
        if len(candles) < 7:
            return False
        window = candles[-7:]
        stamps = window[:, 0]
        closes = window[:, 2]
        if (not np.all(np.isfinite(stamps))
                or not np.all(np.diff(stamps) == 14_400_000)
                or stamps[-1] != self.closed_candle_open_time
                or stamps[-1] + 14_400_000 > self.time
                or not np.all(np.isfinite(closes)) or np.any(closes <= 0)):
            return False
        # Difference of logs avoids division overflow for valid positive prices.
        downside = np.maximum(-np.diff(np.log(closes)), 0.0)
        total_downside = float(np.sum(downside))
        return total_downside > 0 and float(np.max(downside)) <= total_downside / 2

```

## BtcEntryR103

Source: strategies/BtcEntryR103/__init__.py. Fresh readback equals submitted source. Full normalized base equality PASS. Changed existing methods: `_short_plan`; added: `_entry_gate`.

```python
    def _entry_gate(self, candles, entry, atr) -> bool:
        """Keep the original target above the already observed five-day floor.

        Thirty prior 4h bars define five days. The signal bar is excluded,
        and the target stays fixed; this gate only rejects crowded downside.
        """
        if len(candles) < 31:
            return False
        window = candles[-31:]
        stamps = window[:, 0]
        lows = window[:-1, 4]
        if (not np.all(np.isfinite(stamps))
                or not np.all(np.diff(stamps) == 14_400_000)
                or stamps[-1] != self.closed_candle_open_time
                or stamps[-1] + 14_400_000 > self.time
                or not np.all(np.isfinite(lows)) or np.any(lows <= 0)):
            return False
        return entry - 1.5 * atr >= float(np.min(lows))

```

