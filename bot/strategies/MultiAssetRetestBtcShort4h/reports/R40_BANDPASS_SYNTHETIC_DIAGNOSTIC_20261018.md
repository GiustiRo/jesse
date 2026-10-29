# R40: diagnóstico sintético del filtro bandpass

**Es un diagnóstico técnico con señales artificiales, no una prueba económica adicional.** Los veinte escenarios primarios permanecen intactos. La [receta SPY40-01](http://localhost:9200/#/backtest/3441ac21-d65a-48f4-9f2d-4a025b474c1c) no generó operaciones; sus snapshots no conservan estados del filtro, amplitudes o gates. Estos experimentos no identifican la causa efectiva de sus cero entradas.

Después de observar ese cero, root probó la función nativa disponible en el mismo runtime de análisis, con periodo20 y bandwidth0,3 fijos. No se usaron velas reales, datos nuevos ni2026. No se ajustó la estrategia, sus thresholds, el framework o paquetes. No se ejecutó otro backtest.

## Hallazgo observado

Con la misma onda de amplitud5 y periodo20, el resultado normalizado cambia materialmente al añadir un nivel constante de500:

|Entrada sintética, longitud|BP en últimos20|BP normalizado en últimos20|
|---|---:|---:|
|5·sin(2πt/20),240|−4,972 /+4,973|−1 /+1|
|500+5·sin(2πt/20),240|−5,025 /+4,926|−0,084 /+0,075|
|5·sin(2πt/20),300|aprox.±4,972|±1|
|500+5·sin(2πt/20),300|−4,984 /+4,959|−0,144 /+0,130|
|Ambos niveles,1000|aprox.±4,972|±1|

A longitud240, la diferencia máxima entre BP de ambos niveles es0,0573, pero la diferencia normalizada alcanza0,9273. A1000, ambas diferencias son menores de1,1e−9. Una serie constante500 de longitud240 aún tiene BP residual absoluto máximo0,0573 en sus últimos20puntos. Todo fue finito.

Esto demuestra sensibilidad de arranque/nivel en estos casos sintéticos. No prueba que todo output del indicador sea erróneo o que normalización deba ser invariante en toda muestra finita. Sí cuestiona asumir que el nombre bp_normalized garantiza oscilación cercana a±1 tras cien o doscientas barras para cualquier nivel de precio.

## Relación con la receta y límites

SPY40-01 usa cruces±0,5 del campo normalizado y retención300B, pasando secuencial=false al wrapper. En el código local de framework inspeccionado, jesse/indicators/bandpass.py llama a slice_candles; jesse/helpers.py:884–888 recorta muestras escalares al warmup configurado, con default240. El formulario de la tanda conserva warmup240. Se distingue esa inspección de fuente local de las llamadas nativas ejecutadas en el runtime de análisis: no se hizo introspección de archivos remotos o de datos de mercado.

La prueba de longitud1000 llama directamente a la función nativa, no al wrapper escalar: no demuestra que aumentar sólo la historia suministrada al wrapper evite su recorte. No se cambió ese comportamiento.

Los resultados alertan sobre una suposición de implementación que la revisión de firma y nombres de campos no resolvía. La receta queda sin evidencia económica; no se debe interpretar como refutación de todos los enfoques de ciclo. Tampoco se atribuye su cero real exclusivamente a este hallazgo sin observar sus estados. Una eventual corrección o contraste de inicialización debe registrarse como investigación posterior y conservar el resultado original, sin presentarla como validación independiente.

## Reproducción

Dos jobs terminales succeeded: a5d0af5c5fcc41eaaf5e69b9f216607e y0401e478bc9a40a3aba6457a4a18f0cf. Sólo leyeron el snapshot de la sesión indicado, generaron arrays sintéticos en memoria y escribieron JSON bajo output/. No scripts persistentes.

### Primer diagnóstico

```python
import json
from pathlib import Path
import numpy as np
import jesse_rust as jr
snapshot=json.loads(Path("inputs/spy_cycle.json").read_text())
print("STORED_TRADES",len(snapshot.get("trades",[])))
result=[]
for n in (100,240,300):
    t=np.arange(n,dtype=np.float64)
    source=np.ascontiguousarray(500+5*np.sin(2*np.pi*t/20))
    arrays=jr.bandpass(source,20,0.3)
    item={"n":n,"test":"synthetic sine level500 amplitude5 period20; not observed market data","fields":{}}
    for name,value in zip(("bp","bp_normalized","signal","trigger"),arrays):
        a=np.asarray(value,dtype=float)
        z=a[-20:]
        finite=z[np.isfinite(z)]
        item["fields"][name]={"last":float(a[-1]) if np.isfinite(a[-1]) else None,"finite_tail_count":int(np.isfinite(z).sum()),"tail_min":float(finite.min()) if len(finite) else None,"tail_max":float(finite.max()) if len(finite) else None}
    result.append(item)
Path("output/bandpass_synthetic.json").write_text(json.dumps(result,indent=2,allow_nan=False))
print(json.dumps(result,allow_nan=False))

```

Salida:
```text
STORED_TRADES 0
[{"n": 100, "test": "synthetic sine level500 amplitude5 period20; not observed market data", "fields": {"bp": {"last": 0.8013706880834435, "finite_tail_count": 20, "tail_min": -11.555041891379652, "tail_max": 12.4314952792091}, "bp_normalized": {"last": 0.003922578600473056, "finite_tail_count": 20, "tail_min": -0.053573701409158805, "tail_max": 0.05218115614469278}, "signal": {"last": 1.0, "finite_tail_count": 20, "tail_min": -1.0, "tail_max": 1.0}, "trigger": {"last": 0.025246041944646504, "finite_tail_count": 20, "tail_min": -0.044605604529404576, "tail_max": 0.058680380168470006}}}, {"n": 240, "test": "synthetic sine level500 amplitude5 period20; not observed market data", "fields": {"bp": {"last": -1.224814701627425, "finite_tail_count": 20, "tail_min": -5.024825680499754, "tail_max": 4.925833458908868}, "bp_normalized": {"last": -0.021256754868030085, "finite_tail_count": 20, "tail_min": -0.08410894617022635, "tail_max": 0.07532470870512842}, "signal": {"last": 1.0, "finite_tail_count": 20, "tail_min": -1.0, "tail_max": 1.0}, "trigger": {"last": 0.013783558779031023, "finite_tail_count": 20, "tail_min": -0.07357734543261843, "tail_max": 0.0674535831036219}}}, {"n": 300, "test": "synthetic sine level500 amplitude5 period20; not observed market data", "fields": {"bp": {"last": -1.194861289604301, "finite_tail_count": 20, "tail_min": -4.983982254728567, "tail_max": 4.959210359316165}, "bp_normalized": {"last": -0.03567178123244871, "finite_tail_count": 20, "tail_min": -0.14350875933158783, "tail_max": 0.13045207693078728}, "signal": {"last": 1.0, "finite_tail_count": 20, "tail_min": -1.0, "tail_max": 1.0}, "trigger": {"last": 0.02349485413384286, "finite_tail_count": 20, "tail_min": -0.12651393376238254, "tail_max": 0.11566066888201769}}}]

```

### Contraste de traslación y longitud

```python
import json
from pathlib import Path
import numpy as np
import jesse_rust as jr
snapshot=json.loads(Path("inputs/spy_cycle.json").read_text())
result=[]
for n in (240,300,1000):
    t=np.arange(n,dtype=np.float64)
    tails={}
    for offset in (0.0,500.0):
        source=np.ascontiguousarray(offset+5*np.sin(2*np.pi*t/20))
        arrays=jr.bandpass(source,20,0.3)
        tails[str(offset)]=[np.asarray(v,dtype=float)[-20:] for v in arrays]
        item={"n":n,"offset":offset,"synthetic":True,"native_call_not_Jesse_scalar_wrapper":True}
        for name,a in zip(("bp","bp_normalized"),tails[str(offset)][:2]):
            item[name]={"tail_min":float(a.min()),"tail_max":float(a.max()),"finite":bool(np.isfinite(a).all())}
        result.append(item)
    result.append({"n":n,"offset_comparison":True,"max_tail_bp_difference":float(np.max(np.abs(tails["0.0"][0]-tails["500.0"][0]))),"max_tail_normalized_difference":float(np.max(np.abs(tails["0.0"][1]-tails["500.0"][1])))})
constant=jr.bandpass(np.full(240,500.0,dtype=np.float64),20,0.3)
result.append({"constant_500_n240":True,"bp_tail_abs_max":float(np.max(np.abs(np.asarray(constant[0])[-20:]))),"normalized_tail_abs_max":float(np.max(np.abs(np.asarray(constant[1])[-20:])))})
Path("output/bandpass_translation.json").write_text(json.dumps(result,indent=2,allow_nan=False))
print(json.dumps(result,allow_nan=False))

```

Salida:
```json
[{"n": 240, "offset": 0.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -4.972447424290346, "tail_max": 4.972520709234804, "finite": true}, "bp_normalized": {"tail_min": -1.0, "tail_max": 1.0, "finite": true}}, {"n": 240, "offset": 500.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -5.024825680499754, "tail_max": 4.925833458908868, "finite": true}, "bp_normalized": {"tail_min": -0.08410894617022635, "tail_max": 0.07532470870512842, "finite": true}}, {"n": 240, "offset_comparison": true, "max_tail_bp_difference": 0.05729276228748148, "max_tail_normalized_difference": 0.9272968809175004}, {"n": 300, "offset": 0.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -4.972477661092202, "tail_max": 4.972495999977325, "finite": true}, "bp_normalized": {"tail_min": -1.0, "tail_max": 1.0, "finite": true}}, {"n": 300, "offset": 500.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -4.983982254728567, "tail_max": 4.959210359316165, "finite": true}, "bp_normalized": {"tail_min": -0.14350875933158783, "tail_max": 0.13045207693078728, "finite": true}}, {"n": 300, "offset_comparison": true, "max_tail_bp_difference": 0.015393451115147894, "max_tail_normalized_difference": 0.8740931663302459}, {"n": 1000, "offset": 0.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -4.972486171758327, "tail_max": 4.972486171759584, "finite": true}, "bp_normalized": {"tail_min": -1.0, "tail_max": 1.0, "finite": true}}, {"n": 1000, "offset": 500.0, "synthetic": true, "native_call_not_Jesse_scalar_wrapper": true, "bp": {"tail_min": -4.972486172516873, "tail_max": 4.97248617079945, "finite": true}, "bp_normalized": {"tail_min": -1.0, "tail_max": 1.0, "finite": true}}, {"n": 1000, "offset_comparison": true, "max_tail_bp_difference": 1.0801839422924786e-09, "max_tail_normalized_difference": 4.4162307144546276e-10}, {"constant_500_n240": true, "bp_tail_abs_max": 0.05729276228749462, "normalized_tail_abs_max": 0.0009333443798623454}]

```
