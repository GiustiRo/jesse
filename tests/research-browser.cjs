/* Explicit opt-in integration check: uses the running local research dashboard.
 * Never initiates experiments. The request guard fails on any unexpected POST.
 */
const assert=require('node:assert/strict');
const {execFileSync}=require('node:child_process');
const {chromium}=require('playwright');
const U=require('../jesse/static/research/logic.js');
(async()=>{
  const token=execFileSync('docker',['exec','-w','/src/bot','jesse-research-jesse-1','python','-c','from hashlib import sha256; from jesse.services.env import ENV_VALUES; print(sha256(ENV_VALUES["PASSWORD"].encode()).hexdigest())'],{encoding:'utf8'}).trim();
  const browser=await chromium.launch({headless:true,...(process.env.JESSE_UI_BROWSER_EXECUTABLE?{executablePath:process.env.JESSE_UI_BROWSER_EXECUTABLE}:{})});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1000}}), errors=[],unexpected=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.route('**/*',route=>{
      const req=route.request(),url=new URL(req.url());
      if(req.method()==='POST'&&url.pathname!=='/project-files/read'&&!['/general-info','/get-config','/auth/is-authenticated','/auth/validate','/get-exchanges'].includes(url.pathname)){
        // The native shell makes its own read requests; record panel calls only.
        if(req.postData()?.includes('RESEARCH_HUB')||/^\/(?:backtest$|candles\/import|live\/start|project-files\/(?:write|delete|move))/.test(url.pathname)){unexpected.push(url.pathname);return route.abort();}
      }
      return route.continue();
    });
    await page.addInitScript(t=>localStorage.setItem('main',JSON.stringify({authToken:t})),token);
    await page.goto('http://localhost:9200/#/research');
    await page.locator('#jesse-research').waitFor({timeout:30000});
    const panel=page.locator('#jesse-research');
    // Documentary revisions evolve independently of this reader integration test.
    await assert.doesNotReject(()=>panel.getByText(/Revisión [^·]+ · Registro/).waitFor({timeout:30000}));
    await panel.getByRole('button',{name:'Metodología y continuidad',exact:true}).click();
    await panel.getByRole('button',{name:'Exploraciones posteriores: mapa para evitar repeticiones',exact:true}).click();
    await panel.locator('pre').filter({hasText:'Historial de exploraciones ejecutadas y control de repetición'}).waitFor();
    await panel.getByRole('button',{name:'Exploraciones',exact:true}).click();
    assert.equal(await panel.locator('details').count(),12);
    await panel.getByLabel('Activo',{exact:true}).selectOption('BTC');
    assert.equal(await panel.locator('details').count(),9);
    await panel.getByLabel('Estado',{exact:true}).selectOption('sin confirmación');
    assert.equal(await panel.locator('details').count(),1);
    await panel.locator('summary').click();
    await panel.getByText('CAGR de desarrollo no valida 2024–2025.',{exact:false}).waitFor();
    await panel.getByRole('button',{name:'V5_CROSS_SCREEN_REPORT.md',exact:true}).click();
    await panel.locator('pre').filter({hasText:/CROSS/}).last().waitFor();
    await panel.getByLabel('Activo',{exact:true}).selectOption('PAXG');
    await panel.getByText('Sin exploraciones para estos filtros.').waitFor();
    await panel.getByRole('button',{name:'Situación actual',exact:true}).click();
    await page.screenshot({path:process.env.RESEARCH_SCREENSHOT||'research-desktop.png',fullPage:true});
    await page.evaluate(()=>document.documentElement.classList.add('dark'));
    await page.waitForFunction(()=>document.querySelector('#jesse-research')?.dataset.theme==='dark');
    await page.setViewportSize({width:390,height:844});
    await page.screenshot({path:process.env.RESEARCH_MOBILE_SCREENSHOT||'research-mobile.png',fullPage:true});
    assert.equal(await panel.evaluate(n=>n.scrollWidth<=n.clientWidth+1),true);
    // Synthetic unsafe strings test rendering only; they do not replace evidence.
    await page.route('**/project-files/read',async route=>{
      const body=route.request().postDataJSON();
      if(body.path===U.BASE+'index.json')return route.fulfill({status:401,json:{}});
      return route.continue();
    });
    await panel.getByRole('button',{name:'Actualizar',exact:true}).click();
    await panel.getByText(/Autenticación vencida/).waitFor();
    await page.unroute('**/project-files/read');
    await page.route('**/project-files/read',route=>route.fulfill({json:{status:'error',error_type:'not_found'}}));
    await panel.getByRole('button',{name:'Actualizar',exact:true}).click();
    await panel.getByText(/Documento ausente/).waitFor();
    await page.unroute('**/project-files/read');
    await page.route('**/project-files/read',route=>route.abort());
    await panel.getByRole('button',{name:'Actualizar',exact:true}).click();
    await panel.getByText(/Failed to fetch|fetch/).waitFor();
    await page.unroute('**/project-files/read');
    // Deliberately synthetic registry: exercise untrusted text, old revisions,
    // stale timestamps and broken references without modifying stored evidence.
    const unsafe='<img src=x onerror="window.researchXss=true">';
    const revision={format_version:1,id:'fixture',updated_at_utc:'2020-01-01T00:00:00Z',objective:unsafe,latest:'fixture',next:'fixture',blockers:'fixture',counts:{cycles:[]},decisions:[],lines:[],methodology:[],supersedes:[],roadmap:[],documents:[{label:'Missing evidence',path:'strategies/Fixture/missing.md'}],explorations:[]};
    await page.route('**/project-files/read',route=>{
      const body=route.request().postDataJSON();let value;
      if(body.path===U.BASE+'index.json')value={format_version:1,current:'fixture',revisions:[{id:'fixture',path:'strategies/Fixture/revision.json'},{id:'previous',path:'strategies/Fixture/previous.json'}]};
      else if(body.path==='strategies/Fixture/revision.json')value=revision;
      else if(body.path==='strategies/Fixture/previous.json')value={...revision,id:'previous'};
      else return route.fulfill({json:{status:'error',error_type:'not_found'}});
      return route.fulfill({json:{status:'success',kind:'text',content:JSON.stringify(value),has_more:false}});
    });
    await panel.getByRole('button',{name:'Actualizar',exact:true}).click();
    await panel.getByText(/Registro desactualizado/).waitFor();
    await panel.getByText(unsafe,{exact:true}).waitFor();
    assert.equal(await panel.locator('img').count(),0);
    assert.equal(await page.evaluate(()=>window.researchXss),undefined);
    await panel.getByLabel('Revisión',{exact:true}).selectOption('previous');
    await panel.getByText(/Revisión histórica/).waitFor();
    await panel.getByRole('button',{name:'Metodología y continuidad',exact:true}).click();
    await panel.getByRole('button',{name:'Missing evidence',exact:true}).click();
    await panel.getByText(/Documento ausente/).waitFor();
    delete revision.roadmap;
    await panel.getByRole('button',{name:'Actualizar',exact:true}).click();
    await panel.getByText(/Revisión incompleta: roadmap/).waitFor();
    await page.unroute('**/project-files/read');
    await page.evaluate(()=>location.hash='#/candles');
    await panel.waitFor({state:'detached'});
    await page.evaluate(()=>location.hash='#/research');
    await page.locator('#jesse-research').waitFor();
    await page.locator('#jesse-research').getByText(/Revisión [^·]+ · Registro/).waitFor();
    assert.deepEqual(unexpected,[]);
    assert.deepEqual(errors,[]);
    console.log('PASS: authenticated direct route, filters, evidence, themes, mobile, errors, stale/historical revisions, XSS, missing fields/references, navigation; no experiment calls.');
  }finally{await browser.close();}
})().catch(e=>{console.error(e.message);process.exitCode=1;});
