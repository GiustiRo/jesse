# Prima overnight SPY CFD — descarte metodológico antes de simular
Fecha2026-10-18. NO se creó estrategia, draft ni backtestovernight. No existen PnLpropio ni métricasestimar.
## Hipótesis considerada
Comprar al cierre NY16:00 yvender09:30siguientesesión,30m,America/New_York,DSTyfestivos explícitos. Es distinta deRSI/rupturas; no se eligen horarios mirando meses malos.
## Evidencia y obstáculo económico
Fuenteprimaria: Boyarchenko,Larsen,Whelan,NYFedStaffReport917 (2020,rev2022):
https://www.newyorkfed.org/research/staff_reports/sr917
https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf
El paper estudia futuresS&P500 ydriftconcentrado2–3amET, con escala~1.48bpsdiarios(3.7%anual). Esto NO equivale a todalanoche ni asegura mismaedge del CFD.
Comisiónacordada0.00045porlado=9bpsRT,~6veces esa magnitud publicada, antesdespread/funding/impacto. Cambiar apseudomakerbarato violateelcriterio acordado. Una anomalía estadística bruta no estableceedge operable en esteinstrumento.
## Fuentes locales revisadas por MCP
research_scripts/data/histdata/SPXUSD_div10_1m_2020_2025.csv.manifest.json
research_scripts/data/histdata/SPXUSD_div10_1m_2020_2025.csv.ny_hour_counts.csv
research_scripts/data/histdata/SPXUSD_source_audit.json
HistDataSPXCFDBID/10,1,974,135minutos2020–25;origenESTfijoUTC−5sinDST;datosdiscontinuos. ConteoshoraNYmuestran9h y15hobservadas,pero16hvaríamuchoentreinvierno/verano;esto no pruebaarbitrariamente ausencia delquote16:00 exacto. No se auditócompletitud de todos los30mni09:29/15:59exactos. No inventarvelas/fillsenfestivos/earlycloses.
Catálogo MCP queryovernight,Q1/2022:0matchesentre39estrategiasranked;noimplicaausenciauniversal. Noimportarcredenciales.
## Decisión
NO lanzar bajoactualeshurdlesde costes/fuentessinmejorevidenciaprevia. No claimsde PnLpropio, no usar2026. Descartemetodológico acotado, noafirmación de que la primaovernightnoexiste.
