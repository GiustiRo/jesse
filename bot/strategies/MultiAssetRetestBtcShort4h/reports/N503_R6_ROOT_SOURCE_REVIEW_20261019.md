# N503 R6 — revisión root de diez fuentes

Protocolo guardado antes de fuentes/sesiones/resultados. Fuentes nuevas completas leídas medianteMCP y comparadas con N503:prefijosglobales/imports/constantesidénticos;ERhelper/métodosprotegidosexactos. E before añadegatealsetupcompleto;P601/602vetantraslatch+geometría+counterbase,sinrearmado.P603..605sólo ramasuppdeupdate/onopen,originalesSTOP72h/longprotección/sizing intactos. Readinesspuro noinvoca_short_plan/_signal ni capital/margen/ledger. P602prefijosvisibles143bars,noigualdadcontrafactualbufferhistórico;P604shadowobservaexactnext4h/nuncaasumeSTOPfill;P605progresofavorableC<Eirreversibledesdeprimerfull. No parciales.

E605gateusa240M1cerradosdeltrigger4h,datosOHLC/volumen válidos ycloseigual al4h,cobertura/mismatchcontadosporseparado. Guardshape/emptyantesindexar fueaclaradoantesdeprimerfullE605,sincambioregla,seactualizaronsus2draftssnapshots. QA E194inicialy196finalPASS;P311PASS. Soncontrolesdeimplementación,nuevasobservacionesfinancierasno.

E601estransferenciadeR2N207sobreN503,nomecanismoinédito. P605esreusocontextualdelestancamientopreviamenteprobado,seconservaestacaracterizaciónantesderesultados.

Primeros4fulls corren al guardar,ningúnresultadonuevoha sido consultado. 2026cerrado,20nominales,gateultimateN204+comparaciónseedN503. Máximo6confirmacionesúnicossi hayelegible amboscostos/M/Q;sinbajarumbrales.

```json
{
  "source_reviews": {
    "N503ExploreR601": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_r6_gate"
      ],
      "prefix": true
    },
    "N503ExploreR602": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_r6_gate"
      ],
      "prefix": true
    },
    "N503ExploreR603": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_r6_gate"
      ],
      "prefix": true
    },
    "N503ExploreR604": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_r6_gate"
      ],
      "prefix": true
    },
    "N503ExploreR605": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_r6_gate"
      ],
      "prefix": true
    },
    "N503CapacityR601": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_capacity_context",
        "_capacity_full_bars",
        "_capacity_veto"
      ],
      "prefix": true,
      "beforePreserved": true,
      "originalUpdateBranch": true
    },
    "N503CapacityR602": {
      "protected": true,
      "changed": [
        "terminate",
        "before",
        "_capacity_context",
        "_capacity_full_bars",
        "_capacity_veto"
      ],
      "prefix": true,
      "beforePreserved": true,
      "originalUpdateBranch": true
    },
    "N503CapacityR603": {
      "protected": true,
      "changed": [
        "on_open_position",
        "update_position",
        "terminate",
        "before",
        "_capacity_context",
        "_capacity_full_bars",
        "_capacity_release"
      ],
      "prefix": true,
      "beforePreserved": true,
      "originalUpdateBranch": true
    },
    "N503CapacityR604": {
      "protected": true,
      "changed": [
        "on_open_position",
        "update_position",
        "terminate",
        "before",
        "_capacity_context",
        "_capacity_full_bars",
        "_capacity_release"
      ],
      "prefix": true,
      "beforePreserved": true,
      "originalUpdateBranch": true
    },
    "N503CapacityR605": {
      "protected": true,
      "changed": [
        "on_open_position",
        "update_position",
        "terminate",
        "before",
        "_capacity_context",
        "_capacity_full_bars",
        "_capacity_release"
      ],
      "prefix": true,
      "beforePreserved": true,
      "originalUpdateBranch": true
    }
  },
  "QA": [
    {
      "family": "E_initial",
      "job": "5d43e8e4530140119ca8d5f7a975dcba",
      "checks": 194,
      "status": "succeeded"
    },
    {
      "family": "E_final",
      "job": "c93ea284cfff4f98883ebb99b7943f0f",
      "checks": 196,
      "status": "succeeded",
      "clarification": "E605missingfeedshape/emptyfalse,beforeE605full"
    },
    {
      "family": "P",
      "job": "b03123cc60cc412dac8a64815b322681",
      "checks": 311,
      "status": "succeeded"
    }
  ]
}
```
