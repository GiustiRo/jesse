import json
from datetime import datetime, timezone
from jesse.strategies import Strategy


class ResearchDataAudit5m(Strategy):
    """Read-only replay: enumerate OI as it becomes available; never submit orders."""
    START = 1598918400000
    FINISH = 1767225600000
    PERIOD = 300000
    LAG = 360000
    MAX_AGE = 600000
    FOUR_H = 14400000
    DAY = 86400000

    def before(self):
        now = int(self.time)
        value, label = self.open_interest, self.open_interest_timestamp
        months = self.vars.setdefault("months", {})
        # Decisions belong to the just-closed bar, including the final boundary.
        month = datetime.fromtimestamp((now - 1) / 1000, timezone.utc).strftime("%Y-%m")
        row = months.setdefault(month, dict(raw=0, zero=0, missing_slots=0,
            decisions4h=0, absent=0, stale=0, zero_current=0,
            initialization=0, invalid_reference=0, nonrising=0, rising=0))
        last = self.vars.get("last")
        if value is not None:
            assert label is not None and value >= 0
            assert label + self.LAG <= now <= label + self.LAG + self.MAX_AGE
            if last is None or label != last[0]:
                previous = last[0] if last else self.START - self.PERIOD
                assert label > previous
                if label > previous + self.PERIOD:
                    gaps = self.vars.setdefault("gaps", [])
                    gaps.append([previous + self.PERIOD, label, (label - previous) // self.PERIOD - 1])
                    for missing in range(previous + self.PERIOD, label, self.PERIOD):
                        key = datetime.fromtimestamp(missing / 1000, timezone.utc).strftime("%Y-%m")
                        months.setdefault(key, dict(raw=0, zero=0, missing_slots=0,
                            decisions4h=0, absent=0, stale=0, zero_current=0,
                            initialization=0, invalid_reference=0, nonrising=0, rising=0))["missing_slots"] += 1
                key = datetime.fromtimestamp(label / 1000, timezone.utc).strftime("%Y-%m")
                target = months.setdefault(key, row.copy())
                target["raw"] += 1
                target["zero"] += int(value == 0)
                if value == 0:
                    self.vars.setdefault("zeros", []).append(label)
                self.vars["last"] = (label, value)
        else:
            assert label is None

        if now % self.FOUR_H == 0:
            row["decisions4h"] += 1
            history = self.vars.setdefault("history4h", [])
            reference = history[-6] if len(history) >= 6 else None
            if value is None:
                row["absent" if last is None else "stale"] += 1
            elif value == 0:
                row["zero_current"] += 1
            elif reference is None or reference[0] != now - self.DAY:
                row["initialization"] += 1
            elif reference[1] is None or reference[1] <= 0:
                row["invalid_reference"] += 1
            elif value > reference[1]:
                row["rising"] += 1
            else:
                row["nonrising"] += 1
            history.append((now, value))
            history[:] = history[-6:]
            rows = self.get_funding_history(count=31)
            assert all(r["available_at"] <= now for r in rows)

    def should_long(self):
        return False

    def go_long(self):
        raise AssertionError("Audit must never trade")

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        for month, row in sorted(self.vars["months"].items()):
            assert row["decisions4h"] == sum(row[k] for k in
                ("absent", "stale", "zero_current", "initialization", "invalid_reference", "nonrising", "rising"))
            self.log("DATA_AUDIT_MONTH " + json.dumps(dict(month=month, **row), sort_keys=True))
        # MCP truncates each log line at 2000 characters; emit bounded records.
        for gap in self.vars.get("gaps", []):
            self.log("DATA_AUDIT_GAP " + json.dumps(gap))
        runs = []
        for label in self.vars.get("zeros", []):
            if runs and label == runs[-1][1]:
                runs[-1][1] += self.PERIOD
                runs[-1][2] += 1
            else:
                runs.append([label, label + self.PERIOD, 1])
        for run in runs:
            self.log("DATA_AUDIT_ZERO_RUN " + json.dumps(run))
        self.log("DATA_AUDIT_TAIL " + json.dumps(dict(last=self.vars.get("last"),
            note="Last raw label(s) not yet available at finish must be reconciled by MCP raw tail page.")))
