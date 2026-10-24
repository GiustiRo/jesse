# BTC discovery D — ¿cambia la utilidad al cambiar el reloj?
Registro 2026-10-21 18:06:24 UTC, antes de implementación y economíaD. Permiso autónomo vigente. Presupuesto: dos backtests económicos, uno por política; máximo dos reemplazos técnicos, sin vecinos ni estrés. C cerrada sin candidata: CUSUM CAGR8,98%,absorción−1,12%;no se afina susumbrales.

## Una pregunta con control
D_VOLUME: construir bloques con barras4h enteras hasta alcanzar volumenQ=6×media de24barras previas a la que inicia el bloque. CongelarQ al iniciar;no recalcularlo despuésdevervolumen. No dividirbarra, no conservarovershootparabloquefuturo:todo el exceso pertenecealbloquecerrado. Al cerrarse, longsi C>máximoHdetresbloquescompletosanteriores;shortsi C<mínimoL. Excluirbloqueactual delcanal. Sembrartresbloquesantesdeentrada;eventoocupadoseconsume.
D_FIXED: mismocanal de tresbloques,mismaprotecciónycostos;cadabloqueson6barras4h=undíaUTCcompleto. Si se reinicia por datos inválidos, esperaraaperturaUTC00:00paraelcontrol;volumenpuedeiniciarconprimerabarra válida. Control conocido, nootrahipótesisdealpha.
Volumenbasefinito>=0;Q<=0/infinito oventanasdiscontinuas reinicianestado sinentry. Cerosindividualesno se interpolan. EnD_FIXED, ceros noimpiden calendario si datos válidos. No SMA,OI, filtrosfunding, cuerpospequeños o shockgate.

## Antecedentes
CHANNELV3:20barras4h+SMA120/pendiente ytrailing7d;TurtleDailyORCH:55d/ATR20/salidacanal10d. NoequivalenciaeconómicaconcontrolD;senecesitacorridaespecífica. Volumencomo filtroAngle ydireccional-changepriceclockyaestánprobados;estosno se presentancomoideasvírgenes. D cambiaagregacióndeobservacionesporactividadynocalendario,sinprobarvariosQcanales. Una mejoraD_VOLUMEvsD_FIXED sería contrastede políticas completas,no causalidaddevolumen,ni dosmuestrasindependientes.

## Congelado
BTC-USDT BinancePerpetualFutures;observadorM1condata_route4h,signal/gestión4h. 10k,2%/6%/3x,marginbuffer.90,fee.00045takerdescuento,fundingONdataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados,slippage0. Stop2ATR14simple,TP2R,48h. Sinpiramidar,cola o reversiónmismoT.
[2020-10-15,2026-01-01),warmup2404h,desarrolloreutilizado,noOOS.Sinnuevaeconomía2026,imports,estrés,riskvariants,ML,globalconfig,Pi,paper/live. HelpersR10 ytelemetríaR11C congelados;D sólooverridebefore yclock_signal, no cambia las fuentes deC.

## Medición y puertas
MismatelemetríaCdefasepostfunding/predecision a00:00UTC, DDmuestradoM1+eventos(sinpromesaintraminuto),markfeeopen/close yFINALposterioraliquidación. Actividadincluyemesdeejecuciónyexposición deforma conservadora. No confundirCAGRconrendimiento anualgarantizado.
Puertasr9: CAGR>=30%,PF>=1.2,DDM1<=25%,M65activos,Q80,medianacalendariocompletapositiva,netorestantesindosmejoresmesespositivo,N100operativo. Aspiración40–50%/DD20/M70informativa. Positivobajoestrésdiferehasta candidatas yacuerdousuario.
Para justificarvalor delreloj ademásdeaprobarobjetivos,D_VOLUMEdebe superarretornonetoD_FIXED y no tener peorDDM1 bajoidénticoscostos. Si no, no acreditar mejora delreloj. Puedehabercontrol positivo sinprobarefectodelvolumen. Ningúnresultado promueveoperativa.

## Verificación y cierre
AST/helperssintéticos:Qprevioexcluyecurrent,freezedQ,semilla3,sinretrofill/overshoot,calendario6,respetoUTC,gapreset,rechazovolinválido,eventoocupadoconsumidoporstate. Readback/hashes/config antesdeejecutar,máximo2motores. Contabilidadcompleta enrun_analysis,sumtrades/saldo/funding/fees ytelemetría, tolerancia1e−6.
Si fallan,no cambiarQ/número de bloquesniquitarshorts. Registrar control yversionescomoobservaciónexploratoria. Cualquierotra tandaseprerregistraráantes, bajoautonomíaotorgada,sin pedirpermiso rutinario.
