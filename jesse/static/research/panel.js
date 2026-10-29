(() => {
  'use strict';
  const U = window.JesseResearch;
  function el(tag, text, cls) { const n = document.createElement(tag); if (text !== undefined) n.textContent = text; if (cls) n.className = cls; return n; }
  function token() {
    for (let i=0;i<localStorage.length;i++) { try { const v=JSON.parse(localStorage.getItem(localStorage.key(i))); if (typeof v?.authToken==='string') return v.authToken; } catch {} }
    return '';
  }
  async function request(url, body, signal) {
    const t=token(); if (!t) throw new Error('Autenticación requerida: ingresar al dashboard');
    const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json',Authorization:t},body:JSON.stringify(body),signal});
    if (r.status===401) throw new Error('Autenticación vencida: ingresar al dashboard');
    if (!r.ok) { const d=await r.json().catch(()=>({})); throw new Error(d.error_type==='not_found' ? 'Documento ausente: '+body.path : 'Error de conexión HTTP '+r.status); }
    return r.json();
  }
  window.JesseResearchPanel = { mount(root) {
    root.innerHTML='<link rel="stylesheet" href="/research/panel.css"><header><div><p class="eyebrow">PROGRAMA BTC · PAXG · SPY</p><h1>Investigación</h1><p class="muted">Decisiones, evidencia y próximos pasos</p></div><div class="toolbar"><label>Revisión <select id="revision" aria-label="Revisión"></select></label><button id="refresh">Actualizar</button></div></header><p id="status" role="status" aria-live="polite">Cargando registro…</p><div class="tabs" role="group" aria-label="Vistas"></div><section id="content"></section>';
    const $=s=>root.querySelector(s), content=$('#content'), status=$('#status'), select=$('#revision');
    let index, revision, active='Situación actual', controller, busy=false, destroyed=false, currentId;
    const pending=new Set();
    async function textFile(p,signal){
      const read=new AbortController();pending.add(read);
      const abort=()=>read.abort();signal?.addEventListener('abort',abort,{once:true});
      if(signal?.aborted)abort();
      // Evidence opened on demand needs the same network bound as the index.
      const timeout=setTimeout(abort,20000);
      try{return await U.readText(p,request,read.signal);}finally{clearTimeout(timeout);pending.delete(read);signal?.removeEventListener('abort',abort);}
    }
    function documentButton(parent, label, path) {
      const button=el('button',label); parent.append(button);
      button.onclick=async()=> { button.disabled=true; const pre=el('pre','Cargando…'); parent.append(pre);
        try { pre.textContent=await textFile(path,controller.signal); } catch(e){pre.textContent=e.message;pre.className='error';} finally{button.disabled=false;}
      };
    }
    const labels={hypothesis:'Hipótesis',origin:'Origen',method:'Método',protocol:'Protocolo estructurado',budget:'Presupuesto',versions:'Versiones',periods:'Períodos examinados',results:'Resultados',limitations:'Limitaciones',audit:'Auditoría',decision:'Decisión',scope:'Alcance',period:'Período',cagr_pct:'CAGR %',net_pct:'Retorno neto %',drawdown_engine_pct:'Drawdown del motor %',drawdown_pct:'Drawdown %',dd_engine_pct:'Drawdown del motor %',dd_daily_pct:'Drawdown diario %',pf:'Profit factor',trades:'Operaciones',annual_pct:'Retorno anual %',annual:'Resultados anuales',half_years:'Resultados semestrales',half_year_pct:'Retornos semestrales % (orden cronológico)',positive_half_years:'Semestres positivos',costs:'Costos',exposure:'Exposición',stress:'Estrés',confirmation:'Confirmación posterior',corrected_profitability:'Rentabilidad corregida',findings:'Hallazgos',correlation:'Correlación',simultaneous_losses:'Pérdidas simultáneas',comparable_with_without:'Comparación con/sin componente',net_usdt:'Neto USDT',regularity:'Regularidad',funding_oi:'Funding + OI',funding:'Funding',reference:'Referencia',economic_unique:'Económicas nuevas',nominal_slots:'Slots nominales',technical_attempts:'Intentos técnicos'};
    function valueNode(value){
      if(value==null)return el('span','sin evaluar','muted');
      if(Array.isArray(value)){const list=el('ul');for(const item of value){const li=el('li');li.append(valueNode(item));list.append(li);}return list;}
      if(typeof value==='object'){const dl=el('dl');for(const [k,v] of Object.entries(value)){dl.append(el('dt',labels[k]||k.replaceAll('_',' ')));const dd=el('dd');dd.append(valueNode(v));dl.append(dd);}return dl;}
      // Display rounding never governs gates; originals retain full precision.
      return el('span',typeof value==='boolean'?(value?'Sí':'No'):typeof value==='number'?value.toLocaleString('es-UY',{maximumFractionDigits:6}):String(value));
    }
    function renderValue(parent,key,value) { parent.append(el('h3',labels[key]||key),valueNode(value)); }
    function countsTable(){
      const wrap=el('div',undefined,'table'),table=el('table'),head=el('thead'),tr=el('tr');
      for(const title of ['Ciclo','Económicas nuevas','Slots','Reusos','Intentos técnicos'])tr.append(el('th',title));head.append(tr);table.append(head);
      const body=el('tbody');for(const c of revision.counts.cycles){const row=el('tr');for(const v of [c.cycle,c.economic_unique,c.nominal_slots,c.nominal_slots-c.economic_unique,c.technical_attempts])row.append(el('td',v));body.append(row);}table.append(body);wrap.append(table);content.append(el('h3','Conteos V1–V6'),wrap,el('p','209 económicas únicas · 233 slots · 24 reusos · 23 intentos técnicos. Las sesiones no son muestras independientes.','muted'));
    }
    async function detail(holder, entry) {
      holder.textContent='Cargando ficha…';
      try {
        const x=JSON.parse(await textFile(entry.path,controller.signal));
        if(x.id!==entry.id||!Array.isArray(x.references)||!Array.isArray(x.sessions))throw new Error('Ficha incompleta o identidad incorrecta');
        holder.textContent='';
        holder.append(el('p',`Ejecución: ${x.execution} · Evidencia: ${x.evidence} · Objetivo: ${x.objective}`,'notice'));
        const errors=U.protocolErrors(x.protocol,x.sessions.length>0||x.execution==='cerrado');
        holder.append(el('p',errors.length?'Prerregistro no acreditado por el panel: '+errors.join(', '):'Prerregistro documentado; requiere auditoría de sus fuentes.','muted'));
        for(const k of ['hypothesis','origin','method','protocol','budget','versions','periods','results','limitations','audit','decision']) renderValue(holder,k,x[k]);
        for(const s of x.sessions||[]) { const a=el('a',s.label||'Abrir sesión'); if (/^http:\/\/localhost:9200\/#\/backtest\/[a-f0-9-]{36}$/.test(s.url)) {a.href=s.url;holder.append(a,el('br'));} }
        for(const ref of x.references||[]) {const box=el('div');holder.append(box);documentButton(box,ref.label,ref.path);}
      } catch(e){holder.textContent=e.message;holder.className='error';}
    }
    function explorations() {
      const filters=el('div',undefined,'filters'), list=el('div');content.append(filters,list);const state={};
      const draw=()=>{list.textContent='';const rows=revision.explorations.filter(x=>U.matches(x,state)); if(!rows.length)list.append(el('p','Sin exploraciones para estos filtros.'));
        for(const x of rows){const d=el('details'),s=el('summary',`${x.id} · ${x.title} `),body=el('div');s.append(el('span',`${x.asset} · ${x.execution}`,'badge'));d.append(s,body);list.append(d);let loaded=false;d.addEventListener('toggle',()=>{if(d.open&&!loaded){loaded=true;detail(body,x);}});}};
      for(const [key,name] of [['asset','Activo'],['family','Familia'],['execution','Estado']]) { const label=el('label',name),s=el('select');s.setAttribute('aria-label',name);s.append(new Option('Todos',''));[...new Set(revision.explorations.map(x=>x[key]))].sort().forEach(v=>s.append(new Option(v,v)));s.onchange=()=>{state[key]=s.value;draw();};label.append(s);filters.append(label); } draw();
    }
    function render() {
      content.textContent=''; root.querySelectorAll('.tabs button').forEach(b=>b.setAttribute('aria-pressed',String(b.textContent===active)));
      if(!revision)return;
      if(active==='Exploraciones')return explorations();
      if(active==='Situación actual') {
        const grid=el('div',undefined,'grid');content.append(grid);
        for(const [key,label] of [['objective','Objetivo'],['latest','Último avance'],['next','Próximo paso'],['blockers','Bloqueos']]){const card=el('article',undefined,'card');card.append(el('h2',label),el('p',revision[key]));grid.append(card);}
        renderValue(content,'Decisiones vigentes',revision.decisions);
        countsTable();
        renderValue(content,'Horizonte y evidencia previa',revision.lines);
      } else if(active==='Roadmap') {
        for(const step of revision.roadmap){const card=el('article',undefined,'card');card.append(el('h2',`${step.order}. ${step.title}`),el('p',`Estado: ${step.state} · Depende de: ${step.depends}`),el('p',step.gate));content.append(card);}
      } else {
        renderValue(content,'Proceso obligatorio',revision.methodology);
        renderValue(content,'Historial y referencias reemplazadas',revision.supersedes);
        for(const ref of revision.documents){const box=el('article',undefined,'card');content.append(box);documentButton(box,ref.label,ref.path);}
      }
    }
    for(const name of ['Situación actual','Roadmap','Exploraciones','Metodología y continuidad']) {const b=el('button',name);b.onclick=()=>{active=name;render();};$('.tabs').append(b);}
    async function refresh() {
      if(busy||destroyed)return;busy=true;controller=new AbortController();
      // Bound hung reads so a network failure cannot disable all future refreshes.
      const timeout=setTimeout(()=>controller.abort(),20000);
      try{
        index=U.validateIndex(JSON.parse(await textFile(U.BASE+'index.json',controller.signal)));
        const id=currentId||index.current, selected=index.revisions.find(r=>r.id===id);if(!selected)throw new Error('Revisión retirada del índice');
        const data=JSON.parse(await textFile(selected.path,controller.signal));
        U.validateRevision(data,id);
        const changed=!revision||JSON.stringify(data)!==JSON.stringify(revision);revision=data;
        select.textContent='';for(const r of index.revisions)select.append(new Option(r.id,r.id));select.value=id;
        const age=Date.now()-Date.parse(data.updated_at_utc);
        // Seven days is a freshness hint for documentary upkeep, never engine state.
        status.className=age>7*86400000?'notice':'';
        status.textContent=`Revisión ${id} · Registro: ${data.updated_at_utc} · Leído: ${new Date().toISOString()}${id!==index.current?' · Revisión histórica':''}${age>7*86400000?' · Registro desactualizado (>7 días)':''}. Actualización documental; no monitoriza el motor.`;
        if(changed)render();
      }catch(e){if(!destroyed){status.className='error';status.textContent=`${e.name==='AbortError'?'Tiempo de lectura agotado':e.message}. ${revision?'Se conserva la revisión '+revision.id+'; datos sin actualizar.':'Sin registro cargado.'}`;}}
      finally{clearTimeout(timeout);busy=false;}
    }
    select.onchange=()=>{currentId=select.value;refresh();};$('#refresh').onclick=refresh;
    const visible=()=>{if(!document.hidden)refresh();};document.addEventListener('visibilitychange',visible);
    const timer=setInterval(visible,30000);refresh();
    return {destroy(){destroyed=true;controller?.abort();pending.forEach(c=>c.abort());clearInterval(timer);document.removeEventListener('visibilitychange',visible);}};
  }};
})();
