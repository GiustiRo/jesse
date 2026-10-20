# fixedBE_implementation_contrasts.json

Analysis e59c586237944330917483c5429ccedd. Original JSON payload SHA256 7b6b5f7761d14408397fcc9268ee98da5c6cedfa550b1a50dfb48f54c4249862. Connector retrieved truncated=false. The JSON payload below preserves original content.

```json
{
  "status": "PASS",
  "pairs": [
    {
      "reference": "X03S_B",
      "fixed": "FBS0B",
      "delta_net": 876.1828221742835
    },
    {
      "reference": "X03S_C",
      "fixed": "FBS0C",
      "delta_net": 843.9889790957641
    },
    {
      "reference": "N204S_B",
      "fixed": "FBS1B",
      "delta_net": 908.6827108157522
    },
    {
      "reference": "N204S_C",
      "fixed": "FBS1C",
      "delta_net": 918.4629418925215
    }
  ],
  "difference_in_differences": [
    {
      "portfolio": "B",
      "N204_minus_X03_dynamicBE": 923.1638021738072,
      "N204_minus_X03_fixedBE": 955.6636908152759,
      "difference_in_differences": 32.499888641468715
    },
    {
      "portfolio": "C",
      "N204_minus_X03_dynamicBE": 988.0682713267342,
      "N204_minus_X03_fixedBE": 1062.5422341234917,
      "difference_in_differences": 74.4739627967574
    }
  ],
  "limitations": "Only stored trade/order lifecycle endpoints, not full amendment/cancel history or unobserved blocked signals. Actual engine fee/sizing/capital/BTC/SPY fee dependencies remain; fixedBE not pure overlay or eligible replacement."
}
```
