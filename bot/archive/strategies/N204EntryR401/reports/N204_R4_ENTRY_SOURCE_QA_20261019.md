# N204 R4 entry source QA

Root source review: all4sources complete and protocol-conformant. Onlybefore/terminate change, plus exact2completedUTCdays helper E401. Trading infrastructure/helpers/longshort/sizing/defaults original byte-exact. Finalreadbackverified;N204referenceuntouched.

Job59da4ea57508489c8f5e01b6ce5fe8cd succeeded14568assertions,exit0,2026-10-19T17:16:47Z→17:16:48Z. No session inputs or historicaldata. 600 deterministic syntheticfixtures pervariant,scalaroraclegates/setup/geometry,positiveeventcoverage,latchsameclock/occupiedpending/noqueue,invalidclock/gap/nonpositive/nonfinite/reverse-range,ATRrepaircannotreviveevent,dayboundary00/04/08/12/16/20UTC,missing/duplicated/corruptdaybar,ignoredpartialday,equaldailycloserejected. ATR8stub limitsverificationtoimplementationcausality, notenginefills/predictiveness/realATR or2026.

Exactreproduciblesource persistedN204_R4_ENTRY_QA_SOURCE_20261019.md. All seededfixturesaretestdata,neverstrategy randomness/marketsearch.

```json
{
  "job": {
    "id": "59da4ea57508489c8f5e01b6ce5fe8cd",
    "kind": "analysis",
    "workspace": "storage/mcp/analysis/59da4ea57508489c8f5e01b6ce5fe8cd",
    "inputs": [],
    "status": "succeeded",
    "pid": 24853,
    "exit_code": 0,
    "started_at": "2026-10-19T17:16:47+00:00",
    "finished_at": "2026-10-19T17:16:48+00:00",
    "timeout_minutes": 5,
    "output_truncated": false,
    "expires_at": "2026-10-20T17:16:48+00:00",
    "lifetime": "Deleted when a later analysis starts, once 24 hours have passed since it finished (expires_at), or earlier when finished jobs exceed the 50-job or 2 GiB caps (oldest first)."
  },
  "result": {
    "passed": true,
    "assertions": 14568,
    "coverage": {
      "N204EntryR401": {
        "synthetic_setups": 4,
        "synthetic_events": 4
      },
      "N204EntryR402": {
        "synthetic_setups": 5,
        "synthetic_events": 5
      },
      "N204EntryR403": {
        "synthetic_setups": 5,
        "synthetic_events": 5
      },
      "N204EntryR404": {
        "synthetic_setups": 9,
        "synthetic_events": 9
      }
    },
    "sha256": {
      "N204EntryR401": "7b46e9b73b89066179f030f761f7a9f8f05c9bdc8bf2aae27fc010cdd31ac00d",
      "N204EntryR402": "e826bc2f170f6f052618c8cb5551e1633c496cd53e649a101e1fcd97fcf93479",
      "N204EntryR403": "220cab3536caf0f922015d467f6882ef32466ce49fb1ed71e3965920b67a6477",
      "N204EntryR404": "47d2ee5142191fca2b09ac867ac230c8dd31ba80c6f72b70e9cee715fd2dfc6c"
    },
    "baseline_sha256": "69b36f5d7d14e80ed8684fbb60c41bb4c456b25be9c997fa803155efab6f503b",
    "limits": "Synthetic fixtures and ATR8 stub verify implementation/state/time causality only, not market edge, real ATR values, engine fills or 2026."
  }
}
```
