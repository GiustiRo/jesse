# X03 R2 — revisión final independiente de costes

Revisión sólo lectura de X03_R2_RESULTS_20261019.md y X03_R2_ENGINE_CONFIRMATION_20261019.md. Sin nuevas corridas, jobs ni cambios de fuentes.

No se encontraron errores materiales en los números o la conclusión.

- Confirmación N204 fee .00070/lado frente X03 al mismo fee: +923.163802 B y +988.068271 C. Coste motor14bpsRT frente nominal9bpsRT, diferencia+5bpsRT.
- 39/63=61.904762% y39/61=63.934426%: ambos fallan65%mensual. Q17/21B=80.952381%,18/21C=85.714286%, y16/19B/17/19C pasan80%. Falla conjunta justifica no promoción y ninguna sustituta.
- Elegibilidad estática previa N20441/63=65.079365% era correcta y muy estrecha; el informe la distingue de confirmaciónfee real. No trata ambos como la misma prueba.
- FórmulaBE PAXG entrada2661:2661*(1+2.5*.00045)=2663.993625; con.00070=2665.65675. La dependencia causal de la gestión confee y el cambio38→39trades se explican; la penalidad completa no se atribuye aBTC. BTC/SPY mantienen timestamps, pero cantidades/PNL pueden cambiar por capital.
- 42runsmatriz+4controlesfee+2confirmación=48. B/C y variantes redundantes se reconocen dependientes; bootstrap/LOYO se presentan condicionados a muestra reutilizada, sin OOSni probabilidad de no sobreajuste.

Única mejora editorial opcional: en la confirmación, separar la frase de fracciones en “39/61 completos=63.934426%;39/63 incluidos=61.904762%, ambascarteras”. El resultado central ya lo expresa correctamente. “Cierres en mitad superior” deN204 significa estrictamente sobre el punto medio (q>0) en velas válidas, detalle operativo disponible en fuente.

Mantener X03 referencia/N204 investigación congelada es una conclusión coherente; cualquier próxima fase necesita protocolo nuevo y2026continúa cerrado.
