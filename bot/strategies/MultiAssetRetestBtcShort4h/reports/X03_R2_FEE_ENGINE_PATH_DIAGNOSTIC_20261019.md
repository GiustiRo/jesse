# Actual commission stress and changed portfolio path

FullengineFee5X03 references FEE5B/C use .00070perside vsoriginal.00045. Increment is2.5bpsperside=5bpsRT. No source/risk/data changes. Static overlays preserve decisions; changing fee_rate within engine affects sizing, entry fee-hurdles and management anchors that referencefee_rate. It is acommission stress, notpureexogenousslippage.

Rootauditedactualfillsandmatchedopenkeys. BTC31longs+192shorts retain entry/exit clocks, PAXGtwoexitclockschange andoneadditionalentry;SPYclocksremain. The2025-01-03PAXGlong withentry2661 exits at2665.65675 inFee5, exactlyentry*(1+2.5*.00070), instead ofnominaltrailingstop2832.535238 inFebruary. Its netprofit~1130/1147becomes~5.6,followedbyareentryearning~189/191. Thus attributing thewholeextraenginepenalty toX03shorts wouldbeincorrect. PAXGpreservedunchanged; no rescueofitsparameters.

Ordersdiagnosticjob 145e859d9ea147fc8caf05bf241f49cd succeeded; snapshotexecutedordersincludeSTOPandprices. Exactexamples:

```json
[
  {
    "name": "X03B",
    "fee_rate": 0.00045,
    "opened_at": 1609070400000,
    "closed_at": 1610092860000,
    "entry": 1925.71,
    "exit": 1927.8764237500002,
    "qty": 3.0758,
    "net": 1.3296986652738463,
    "fee": 5.333787504976613,
    "formula_fee_BE": 1927.8764237500002,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 1925.71,
        "qty": 3.0758,
        "filled_qty": 3.0758,
        "executed_at": 1609070400000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 1927.8764237500002,
        "qty": -3.0758,
        "filled_qty": -3.0758,
        "executed_at": 1610092860000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "X03B",
    "fee_rate": 0.00045,
    "opened_at": 1735876800000,
    "closed_at": 1738539360000,
    "entry": 2661,
    "exit": 2832.535238466888,
    "qty": 6.684,
    "net": 1130.0180786224196,
    "fee": 16.523455290260706,
    "formula_fee_BE": 2663.993625,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2661,
        "qty": 6.684,
        "filled_qty": 6.684,
        "executed_at": 1735876800000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2832.535238466888,
        "qty": -6.684,
        "filled_qty": -6.684,
        "executed_at": 1738539360000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "X03C",
    "fee_rate": 0.00045,
    "opened_at": 1609070400000,
    "closed_at": 1610092860000,
    "entry": 1925.71,
    "exit": 1927.8764237500002,
    "qty": 3.0732,
    "net": 1.3285746596396324,
    "fee": 5.329278808860826,
    "formula_fee_BE": 1927.8764237500002,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 1925.71,
        "qty": 3.0732,
        "filled_qty": 3.0732,
        "executed_at": 1609070400000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 1927.8764237500002,
        "qty": -3.0732,
        "filled_qty": -3.0732,
        "executed_at": 1610092860000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "X03C",
    "fee_rate": 0.00045,
    "opened_at": 1735876800000,
    "closed_at": 1738539360000,
    "entry": 2661.0000000000005,
    "exit": 2832.535238466888,
    "qty": 6.7835,
    "net": 1146.8398618095696,
    "fee": 16.769428330563063,
    "formula_fee_BE": 2663.9936250000005,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2661,
        "qty": 6.7835,
        "filled_qty": 6.7835,
        "executed_at": 1735876800000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2832.535238466888,
        "qty": -6.7835,
        "filled_qty": -6.7835,
        "executed_at": 1738539360000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5B",
    "fee_rate": 0.0007,
    "opened_at": 1609070400000,
    "closed_at": 1609957260000,
    "entry": 1925.71,
    "exit": 1929.0799925,
    "qty": 2.9845,
    "net": 2.0045081034181855,
    "fee": 8.053234512831375,
    "formula_fee_BE": 1929.0799925,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 1925.71,
        "qty": 2.9845,
        "filled_qty": 2.9845,
        "executed_at": 1609070400000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 1929.0799925,
        "qty": -2.9845,
        "filled_qty": -2.9845,
        "executed_at": 1609957260000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5B",
    "fee_rate": 0.0007,
    "opened_at": 1735876800000,
    "closed_at": 1737323280000,
    "entry": 2661,
    "exit": 2665.6567499999996,
    "qty": 6.0093000000000005,
    "net": 5.577172889555381,
    "fee": 22.4066348854425,
    "formula_fee_BE": 2665.6567499999996,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2661,
        "qty": 6.0093000000000005,
        "filled_qty": 6.0093000000000005,
        "executed_at": 1735876800000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2665.6567499999996,
        "qty": -6.0093000000000005,
        "filled_qty": -6.0093000000000005,
        "executed_at": 1737323280000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5B",
    "fee_rate": 0.0007,
    "opened_at": 1737547200000,
    "closed_at": 1738541160000,
    "entry": 2758,
    "exit": 2801.6052233336904,
    "qty": 4.7606,
    "net": 189.0600865640251,
    "fee": 18.526939638341656,
    "formula_fee_BE": 2762.8264999999997,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2758,
        "qty": 4.7606,
        "filled_qty": 4.7606,
        "executed_at": 1737547200000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2801.6052233336904,
        "qty": -4.7606,
        "filled_qty": -4.7606,
        "executed_at": 1738541160000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5C",
    "fee_rate": 0.0007,
    "opened_at": 1609070400000,
    "closed_at": 1609957260000,
    "entry": 1925.7100000000003,
    "exit": 1929.0799925000001,
    "qty": 2.9813,
    "net": 2.0023588570013864,
    "fee": 8.044599783248175,
    "formula_fee_BE": 1929.0799925000001,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 1925.71,
        "qty": 2.9813,
        "filled_qty": 2.9813,
        "executed_at": 1609070400000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 1929.0799925,
        "qty": -2.9813,
        "filled_qty": -2.9813,
        "executed_at": 1609957260000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5C",
    "fee_rate": 0.0007,
    "opened_at": 1735876800000,
    "closed_at": 1737323280000,
    "entry": 2661,
    "exit": 2665.6567499999996,
    "qty": 6.0724,
    "net": 5.635735385907861,
    "fee": 22.641913314089997,
    "formula_fee_BE": 2665.6567499999996,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2661,
        "qty": 6.0724,
        "filled_qty": 6.0724,
        "executed_at": 1735876800000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2665.6567499999996,
        "qty": -6.0724,
        "filled_qty": -6.0724,
        "executed_at": 1737323280000,
        "status": "EXECUTED"
      }
    ]
  },
  {
    "name": "FEE5C",
    "fee_rate": 0.0007,
    "opened_at": 1737547200000,
    "closed_at": 1738541160000,
    "entry": 2758,
    "exit": 2801.6052233336904,
    "qty": 4.8102,
    "net": 191.02987614802197,
    "fee": 18.719969131695805,
    "formula_fee_BE": 2762.8264999999997,
    "executed_orders": [
      {
        "type": "MARKET",
        "side": "buy",
        "reduce_only": false,
        "price": 2758,
        "qty": 4.8102,
        "filled_qty": 4.8102,
        "executed_at": 1737547200000,
        "status": "EXECUTED"
      },
      {
        "type": "STOP",
        "side": "sell",
        "reduce_only": true,
        "price": 2801.6052233336904,
        "qty": -4.8102,
        "filled_qty": -4.8102,
        "executed_at": 1738541160000,
        "status": "EXECUTED"
      }
    ]
  }
]
```

TwoadditionalpredeclaredattributioncontrolswithoutX03atsame.00070feearequeued.Noalpharecipeorcriterionchanges. FullFee5calendaraudit jobf49763a60e184efbbd7128cfb51855e0 passed. Fee5results38/63monthspositive/16of21Qboth, below65%/80%. Their+5/+10columnsinaudit mean EXTRA costs beyondalreadyhigherenginefee, notnominalbase+5/+10.