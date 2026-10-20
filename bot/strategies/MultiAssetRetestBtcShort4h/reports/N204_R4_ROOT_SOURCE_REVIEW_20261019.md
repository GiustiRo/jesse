# N204 R4 — revisión de13fuentes antes de tickets

FuenteN204inmutable. E: sólo generador y etiquetas,E401helperdíacerradoexacto. X: sólo generador y etiquetas,patronescausales confirmados. T: entryexacta exceptoetiqueta,origina­les/sizing/ledger/HPintactos, gestiónsuplementariaconforme reglas.T404stopqtyremane ytarget1norearmado;actualesfillsparcialespendientesdeauditoría deejecución. D400: cuatrocallobservacionales, métodosbaseexactos alquitarlas,M1postfill cerradas yexitminus1,coverageexplicit. Noextraindicadores ni librerías. QA15022asserts (noobservacionesmercado);D400primerharnessfallófakeOHLCinconsistente,corregidosólofixture.

```json
{
  "sources": {
    "N204EntryR401": {
      "changedMethods": [
        "terminate",
        "_prior_complete_daily_decline",
        "before"
      ],
      "unchangedCore": true
    },
    "N204EntryR402": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "unchangedCore": true
    },
    "N204EntryR403": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "unchangedCore": true
    },
    "N204EntryR404": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "unchangedCore": true
    },
    "N204ExperimentalR401": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "originalsExact": true,
      "setupReviewed": true
    },
    "N204ExperimentalR402": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "originalsExact": true,
      "setupReviewed": true
    },
    "N204ExperimentalR403": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "originalsExact": true,
      "setupReviewed": true
    },
    "N204ExperimentalR404": {
      "changedMethods": [
        "terminate",
        "before"
      ],
      "originalsExact": true,
      "setupReviewed": true
    },
    "N204PathDiagnosticR400": {
      "observationalOnly": true,
      "allOriginalMethodsExactAfterRemovingFourObserverCalls": true,
      "qaChecks": 45
    },
    "N204ExitR401": {
      "changedMethods": [
        "update_position",
        "terminate",
        "before",
        "_exit_full_postfill"
      ],
      "entryExactExceptRecipeLabel": true,
      "originalHelpersExact": true,
      "exitReviewedAgainstFrozenRules": true
    },
    "N204ExitR402": {
      "changedMethods": [
        "update_position",
        "terminate",
        "before",
        "_exit_full_postfill"
      ],
      "entryExactExceptRecipeLabel": true,
      "originalHelpersExact": true,
      "exitReviewedAgainstFrozenRules": true
    },
    "N204ExitR403": {
      "changedMethods": [
        "on_open_position",
        "update_position",
        "terminate",
        "before",
        "_exit_full_postfill"
      ],
      "entryExactExceptRecipeLabel": true,
      "originalHelpersExact": true,
      "exitReviewedAgainstFrozenRules": true
    },
    "N204ExitR404": {
      "changedMethods": [
        "on_open_position",
        "terminate",
        "before",
        "on_reduced_position"
      ],
      "entryExactExceptRecipeLabel": true,
      "originalHelpersExact": true,
      "exitReviewedAgainstFrozenRules": true
    }
  },
  "qa": [
    {
      "family": "E",
      "job": "59da4ea57508489c8f5e01b6ce5fe8cd",
      "checks": 14568,
      "status": "succeeded"
    },
    {
      "family": "X",
      "job": "9f44e855f3c544368430769cf3b412b4",
      "checks": 245,
      "status": "succeeded"
    },
    {
      "family": "T",
      "job": "d584f50ecb0b4a5aaf3746534221de56",
      "checks": 164,
      "status": "succeeded"
    },
    {
      "family": "D400",
      "job": "37753773e9e74a009547d841fd125f6a",
      "checks": 45,
      "status": "succeeded",
      "earlier_fixture_failure": "0f94e1799ab047b6a8b3722fb00de11d"
    }
  ]
}
```