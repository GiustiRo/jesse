# R38 — manifiesto previo al check, sin motores

```json
{
  "stage": "PRE_CHECK_NOT_ECONOMY",
  "sources": {
    "BtcResearchR10Base4h": "2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9",
    "BtcResearchR11Base1m": "be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87",
    "BtcResearchR16LegacyBase1m": "56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542",
    "BtcResearchR38OrdinalBase1m": "626310f698fb3e74c6f166173c9a6aa0c31dcdd48d1418cf915e26d16e3a4eb4",
    "BtcResearchR38First1m": "7827e83d63ed68a5aa77e2c289c7aadc5364772c64433e1d32fd4d782319815b",
    "BtcResearchR38Second1m": "bf946c5d91a01309776240538452ada27ee7a16cf54542e5f1c65ee1c8806595"
  },
  "protocol": "BTC_R38_ORDINAL_PROTOCOL_20261022.md",
  "codes": "BTC_R38_ORDINAL_CODES_20261022.md",
  "harness": "BTC_R38_ORDINAL_SYNTHETIC_CODE_20261022.md",
  "execution_budget": 2,
  "drafts_created": 0,
  "engines_started": 0,
  "checks_started": 0,
  "leaves": [
    "BtcResearchR38First1m",
    "BtcResearchR38Second1m"
  ],
  "contract": {
    "rows": 27,
    "prior_channel": 26,
    "selected_ordinals": [
      1,
      2
    ],
    "initial_seen": false,
    "reset": "midpoint both sides at equality",
    "target": null,
    "max_hold": null,
    "stop": "2ATR14 simple",
    "exit": "current midpoint after fill; native terminal",
    "quota": 0.01,
    "redistribution": false,
    "fee": 0.00045,
    "funding": "historical ON",
    "start": 1602720000000,
    "finish_exclusive": 1767225600000
  }
}
```
