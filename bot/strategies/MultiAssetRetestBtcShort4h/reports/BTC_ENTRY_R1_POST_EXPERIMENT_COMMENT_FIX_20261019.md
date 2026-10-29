# Entry R1 post-experiment comment correction

After all six runs finished and their pre/post snapshot QA was saved, root authorized correcting only a false inherited terminate comment in BtcEntryR101/102/103. Original PortCompare sources and completed session snapshots untouched. No rerun.

Old:
```python
        # jh.debug logs even with strategy debug_mode disabled; no decision is changed.
```
New:
```python
        # Backtest debug_mode=True persists this diagnostic; no decision is changed.
```

MCP read_strategy before change exactly matched six-run frozen source. Three writes through write_strategy succeeded; fresh readbacks exactly match submitted source and reversing this single line recreates each original source byte for byte. No executable, import, threshold, function, risk, alpha, state or logging-call change. Thus current sources differ from completed snapshots only in the comment above; original frozen source retained in session snapshots and source QA. Debugtrue was already used in all six runs and18PORT_CAPACITY records captured. Do not normalize against current source without accounting for this documented one-line difference.
