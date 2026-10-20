"""Run with Python's unittest runner as well as pytest; no npm install required.

Browser checks are opt-in through JESSE_UI_TEST_URL and reuse an already installed
Playwright via NODE_PATH. All API calls are intercepted with synthetic fixtures;
the browser must never start a trading session or download research data here.
"""

import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
LOGIC = ROOT / 'jesse/static/funding/logic.js'


@unittest.skipUnless(shutil.which('node'), 'Node.js is required for UI logic tests')
class FundingDisplayTests(unittest.TestCase):
    def evaluate(self, expression):
        script = f'const ui=require({json.dumps(str(LOGIC))});process.stdout.write(JSON.stringify({expression}));'
        return json.loads(subprocess.check_output(['node', '-e', script], text=True, encoding='utf-8'))

    def test_zero_cashflow_is_still_confirmed_funding(self):
        status = self.evaluate("ui.fundingStatus({mode:'historical',requested_mode:'historical',applied:true,cashflow:0})")
        self.assertEqual(status['label'], 'Funding aplicado')

    def test_requested_funding_does_not_mean_applied(self):
        status = self.evaluate("ui.fundingStatus({mode:'historical',requested_mode:'historical',applied:false,status:'draft'})")
        self.assertEqual(status['tone'], 'warning')
        self.assertNotEqual(status['label'], 'Funding aplicado')

    def test_legacy_missing_metadata_is_not_reported_as_disabled_or_zero(self):
        status = self.evaluate('ui.fundingStatus({status:"finished"})')
        self.assertEqual(status['label'], 'Sin evidencia')
        self.assertEqual(self.evaluate('ui.money(null)'), '—')
        self.assertEqual(self.evaluate('ui.rate(undefined)'), '—')

    def test_explicit_disabled_is_reported(self):
        status = self.evaluate("ui.fundingStatus({mode:'disabled',requested_mode:'disabled',applied:false})")
        self.assertEqual(status['label'], 'Funding desactivado')

    def test_decimal_rates_and_signed_cashflows_display_correct_units(self):
        self.assertEqual(self.evaluate('ui.rate(.0001)'), '0.01000 %')
        self.assertEqual(self.evaluate('ui.money(-1)'), '-1.0000 USDT')
        self.assertEqual(self.evaluate('ui.money(0)'), '+0.0000 USDT')

    def test_timestamps_are_utc_and_dynamic_labels_are_escaped(self):
        self.assertEqual(self.evaluate('ui.utcDate(0)'), '1970-01-01 00:00:00 UTC')
        self.assertEqual(self.evaluate('ui.escape("<img src=x onerror=alert(1)>")'), '&lt;img src=x onerror=alert(1)&gt;')


@unittest.skipUnless(shutil.which('node') and os.getenv('JESSE_UI_TEST_URL'), 'Set JESSE_UI_TEST_URL for browser checks')
class FundingBrowserTests(unittest.TestCase):
    def run_browser(self, script):
        result = subprocess.run(['node', '-e', script], cwd=ROOT, text=True, encoding='utf-8', capture_output=True, timeout=120)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_configure_draft_view_ledger_import_and_live_status(self):
        script = r'''
const assert = require('node:assert/strict');
const {chromium} = require('playwright');
(async () => {
  const browser = await chromium.launch({headless:true,...(process.env.JESSE_UI_BROWSER_EXECUTABLE?{executablePath:process.env.JESSE_UI_BROWSER_EXECUTABLE}:{})});
  try {
    const page = await browser.newPage({viewport:{width:1280,height:1000}});
    const errors=[]; const calls=[];
    page.on('pageerror', error => errors.push(error.message));
    const fundingId='a'.repeat(64), oiId='b'.repeat(64), nextId='c'.repeat(64), incompleteId='d'.repeat(64);
    const start=Date.UTC(2026,9,1), finish=Date.UTC(2026,9,8);
    let fundingDatasets=[{dataset_id:fundingId,source:'binance-usdm-fundingRate-v1',start,finish,event_count:21,first_settlement:start,last_settlement:finish-28800000,largest_gap_ms:28800000,mark_price_proxy_count:0,mark_price_source:'fundingRate.settlement_mark'}];
    let session={mode:'disabled',requested_mode:'disabled',applied:false,status:'disabled',session_status:'draft',funding_config:{mode:'disabled'},open_interest_config:{mode:'disabled'},route_symbols:['BTC-USDT','PAXG-USDT'],ledger:[]};let configSaves=0;
    await page.addInitScript(() => localStorage.setItem('funding-ui-test',JSON.stringify({authToken:'synthetic-test-token'})));
    await page.route('**/*',async route => {
      const request=route.request();
      if(request.method() !== 'POST') return route.continue();
      const path=new URL(request.url()).pathname; const body=request.postDataJSON();
      calls.push({path,body}); let payload={};
      if(path==='/funding/datasets') payload={datasets:fundingDatasets};
      else if(path==='/open-interest/jobs') payload={jobs:[]};
      else if(path==='/open-interest/datasets') payload={datasets:[{dataset_id:oiId,source:'binance-rest',start,finish,observation_count:2016,expected_observation_count:2016,missing_observation_count:0,status:'ready',coverage_complete:true,first_observation:start,last_observation:finish-300000},{dataset_id:incompleteId,source:'binance-rest',start,finish:start+2592*300000,observation_count:500,expected_observation_count:2592,missing_observation_count:2092,status:'incomplete',coverage_complete:false,first_observation:start,last_observation:start+499*300000,leading_gap_ms:0,trailing_gap_ms:2092*300000}]};
      else if(path==='/funding/session') payload=session;
      else if(path==='/funding/session-config') {
        configSaves++;
        assert.equal(body.funding.dataset_id,fundingId);
        assert.deepEqual(body.funding.exclude_symbols,['PAXG-USDT']);
        if(configSaves===1)assert.equal(body.open_interest.mode,'disabled');
        else{assert.equal(body.open_interest.mode,'historical');assert.equal(body.open_interest.dataset_id,incompleteId);assert.equal(body.open_interest.allow_missing_observations,true);}
        session={...session,requested_mode:'historical',funding_config:body.funding,open_interest_config:body.open_interest};
      } else if(path==='/funding/import') {
        assert.equal(typeof body.allow_mark_price_proxy,'boolean');
        payload={...fundingDatasets[0],dataset_id:nextId};
        fundingDatasets.push(payload);
      } else if(path==='/funding/live-session') payload={mode:'live',status:'stale',rate_decimal:.0001,next_funding_timestamp:finish,observed_at:start,cashflow:-1,ledger:[{transaction_id:'synthetic-income',settled_at:start,cashflow:-1,symbol:'BTCUSDT'}]};
      else throw new Error('Unexpected POST '+path);
      await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)});
    });
    await page.goto(process.env.JESSE_UI_TEST_URL.replace(/\/$/,'')+'/funding/index.html');
    await page.getByText('1 versiones guardadas.',{exact:false}).waitFor();
    await page.locator('#session-id').fill('00000000-0000-0000-0000-000000000001');
    await page.getByRole('button',{name:'Cargar sesión',exact:true}).click();
    await page.getByText('Funding desactivado',{exact:true}).waitFor();
    await page.locator('#enable-funding').check();
    await page.locator('#funding-dataset').selectOption(fundingId);
    assert.equal(await page.locator('[name="funding-excluded-symbol"]').isChecked(),false);
    await page.getByRole('button',{name:'Guardar configuración del borrador',exact:true}).click();
    await page.getByText('El funding sólo cubre BTC-USDT.',{exact:false}).waitFor();
    assert(!calls.some(call=>call.path==='/funding/session-config'));
    await page.locator('[name="funding-excluded-symbol"]').check();
    await page.getByRole('button',{name:'Guardar configuración del borrador',exact:true}).click();
    await page.getByText('Sin aplicación confirmada',{exact:true}).waitFor();
    assert(calls.some(call=>call.path==='/funding/session-config'));
    assert.equal(await page.locator('#allow-missing-oi').isChecked(),false);
    assert.equal(await page.locator('#oi-dataset option[value="'+incompleteId+'"]').getAttribute('disabled'),'');
    await page.locator('#enable-oi').check();await page.locator('#allow-missing-oi').check();await page.locator('#oi-dataset').selectOption(incompleteId);
    assert.equal(await page.locator('#oi-dataset option[value="'+incompleteId+'"]').getAttribute('disabled'),null);
    assert.match(await page.locator('#oi-selection-warning').innerText(),/faltan 2092/);assert.match(await page.locator('#oi-selection-warning').innerText(),/None/);
    await page.getByRole('button',{name:'Guardar configuración del borrador',exact:true}).click();
    await page.waitForFunction(()=>document.getElementById('save-config').disabled===false);assert.equal(configSaves,2);
    await page.locator('#allow-missing-oi').uncheck();
    session={...session,status:'applied',session_status:'finished',mode:'historical',applied:true,dataset_id:fundingId,cashflow:0,event_count:2,total:2,scope:['BTC-USDT'],excluded_symbols:['PAXG-USDT'],mark_price_proxy_count:0,data:{mark_price_proxy_count:4198,mark_price_source:'mixed'},ledger:[{settled_at:start,rate_decimal:.0001,mark_price:10000,qty:1,cashflow:-1},{settled_at:start+28800000,rate_decimal:-.0001,mark_price:10000,qty:1,cashflow:1}]};
    await page.getByRole('button',{name:'Cargar sesión',exact:true}).click();
    await page.getByText('Funding aplicado',{exact:true}).waitFor();
    assert.equal(await page.locator('#session-config-form').isVisible(),false);
    assert.match(await page.locator('#session-summary').innerText(),/\+0\.0000 USDT/);
    assert.match(await page.locator('#session-summary').innerText(),/Rutas sin funding modelado/);
    assert.match(await page.locator('#session-summary').innerText(),/PAXG-USDT/);
    assert.match(await page.locator('#session-summary').innerText(),/Precios aproximados del dataset/);
    assert.match(await page.getByText('Precios aproximados del dataset',{exact:true}).locator('..').innerText(),/4198/);
    assert.match(await page.getByText('Movimientos con precio aproximado',{exact:true}).locator('..').innerText(),/\n0\n/);
    await page.locator('#ledger-section summary').click();
    assert.equal(await page.locator('#ledger-body tr').count(),2);
    assert.match(await page.locator('#ledger-body').innerText(),/0\.01000 %/);
    await page.locator('#start-date').fill('2026-10-01');
    await page.locator('#finish-date').fill('2026-10-08');
    assert.equal(await page.locator('#allow-mark-proxy').isChecked(),false);
    await page.getByRole('button',{name:'Descargar datos',exact:true}).click();
    await page.getByText('2 versiones guardadas.',{exact:false}).waitFor();
    assert.equal(calls.filter(call=>call.path==='/funding/import')[0].body.allow_mark_price_proxy,false);
    await page.locator('#allow-mark-proxy').check();
    await page.getByRole('button',{name:'Descargar datos',exact:true}).click();
    await page.getByText('3 versiones guardadas.',{exact:false}).waitFor();
    assert.equal(calls.filter(call=>call.path==='/funding/import')[1].body.allow_mark_price_proxy,true);
    await page.getByRole('button',{name:'Interés abierto',exact:true}).click();
    assert.equal(await page.locator('#oi-coverage-note').isVisible(),true);
    assert.equal(await page.getByText('Incompleta · faltan 2092',{exact:true}).count(),1);
    assert.match(await page.locator('#oi-dataset').innerText(),/Incompleta · faltan 2092/);
    assert.equal(await page.locator('#oi-dataset option[value="'+incompleteId+'"]').getAttribute('disabled'),'');
    assert.match(await page.locator('#datasets-body').innerText(),/500 de 2592 esperados/);
    await page.locator('#live-session-id').fill('00000000-0000-0000-0000-000000000002');
    await page.getByRole('button',{name:'Consultar estado',exact:true}).click();
    await page.getByText('Funding sin actualización confirmada',{exact:true}).waitFor();
    assert.match(await page.locator('#live-summary').innerText(),/0\.01000 %/);
    assert(calls.every(call=>!['/live','/backtest','/arm/switches'].includes(call.path)));
    assert.deepEqual(errors,[]);
    if(process.env.JESSE_UI_SCREENSHOT) await page.screenshot({path:process.env.JESSE_UI_SCREENSHOT,fullPage:true});
    await page.setViewportSize({width:390,height:844});
    if(process.env.JESSE_UI_SCREENSHOT_MOBILE) await page.screenshot({path:process.env.JESSE_UI_SCREENSHOT_MOBILE,fullPage:true});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'mobile layout overflows: '+await page.evaluate(()=>[...document.querySelectorAll('main,section,form,div,label,select,input')].filter(node=>node.getBoundingClientRect().right>innerWidth).map(node=>node.id||node.className).join(', ')));
    console.log('Funding UI browser checks passed; '+calls.length+' mocked read/config/import requests, no trading requests.');
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exit(1);});
'''
        self.run_browser(script)

    def test_archive_consent_background_progress_reload_and_failure_preserves_dataset(self):
        self.run_browser(r'''
const assert=require('node:assert/strict');const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.JESSE_UI_BROWSER_EXECUTABLE?{executablePath:process.env.JESSE_UI_BROWSER_EXECUTABLE}:{})});try{
 const page=await browser.newPage();const errors=[],calls=[];page.on('pageerror',e=>errors.push(e.message));
 const oldId='a'.repeat(64),newId='b'.repeat(64),jobId='00000000-0000-0000-0000-000000000001';
 let datasets=[{dataset_id:oldId,start:Date.UTC(2020,8,1),finish:Date.UTC(2020,8,2),observation_count:288,coverage_complete:true,status:'ready'}];let imports=0,polls=0;
 await page.addInitScript(()=>localStorage.setItem('test-auth',JSON.stringify({authToken:'synthetic-test-token'})));
 await page.route('**/*',async route=>{const req=route.request();if(req.method()!=='POST')return route.continue();const endpoint=new URL(req.url()).pathname;const body=req.postDataJSON();calls.push({endpoint,body});let payload={};
  if(endpoint==='/funding/datasets')payload={datasets:[]};
  else if(endpoint==='/open-interest/jobs')payload={jobs:[]};
  else if(endpoint==='/open-interest/datasets')payload={datasets};
  else if(endpoint==='/open-interest/import'){imports++;assert.equal(body.source,'archive');assert.equal(body.allow_archive_assumptions,true);assert.equal(body.background,true);payload={job_id:jobId,status:'queued'};}
  else if(endpoint==='/open-interest/job'){assert.equal(body.job_id,jobId);polls++;if(imports>1)payload={job_id:jobId,status:'failed',error:'Synthetic archive outage; previous data retained'};else if(polls===1)payload={job_id:jobId,status:'running',progress:{phase:'archive',fetched_days:1,total_days:3,current_date:'2020-09-01'}};else{const result={...datasets[0],dataset_id:newId};datasets=[...datasets,result];payload={job_id:jobId,status:'finished',result};}}
  else throw Error('Unexpected endpoint '+endpoint);
  await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)});
 });
 await page.goto(process.env.JESSE_UI_TEST_URL+'/funding/index.html');await page.getByRole('button',{name:'Interés abierto',exact:true}).click();
 await page.locator('#oi-source').selectOption('archive');await page.locator('#start-date').fill('2020-09-01');await page.locator('#finish-date').fill('2020-09-04');
 assert.equal(await page.locator('#allow-archive-assumptions').isChecked(),false);
 await page.getByRole('button',{name:'Descargar datos',exact:true}).click();await page.getByText('Para usar archivos históricos tenés que aceptar explícitamente',{exact:false}).waitFor();assert.equal(imports,0);
 await page.locator('#allow-archive-assumptions').check();await page.getByRole('button',{name:'Descargar datos',exact:true}).click();
 await page.getByText('1 de 3 días descargados',{exact:false}).waitFor();assert.equal(await page.locator('#import-data').isDisabled(),true);
 await page.reload();await page.getByText('Importación de OI terminada',{exact:true}).waitFor();await page.getByRole('button',{name:'Interés abierto',exact:true}).click();await page.getByText('2 versiones guardadas.',{exact:false}).waitFor();
 assert.equal(imports,1,'reload restarted the import instead of reading the persisted job');
 assert.equal(await page.locator('input[name="dataset"][value="'+newId+'"]').isChecked(),true);
 await page.locator('#oi-source').selectOption('archive');await page.locator('#allow-archive-assumptions').check();await page.getByRole('button',{name:'Descargar datos',exact:true}).click();
 await page.getByText('La importación de OI falló',{exact:true}).waitFor();assert.match(await page.locator('#oi-job-progress').innerText(),/Synthetic archive outage/);
 assert.equal(await page.locator('#datasets-body tr').count(),2);assert.equal(await page.locator('input[name="dataset"][value="'+newId+'"]').isChecked(),true);assert.equal(await page.locator('#import-data').isDisabled(),false);
 assert.deepEqual(errors,[]);assert(calls.every(call=>!['/live','/backtest','/candles/import'].includes(call.endpoint)));
}finally{await browser.close()}})().catch(error=>{console.error(error);process.exit(1)});
''')

    @unittest.skipUnless(os.getenv('JESSE_UI_REAL_AUTH') == '1', 'Opt in to authenticated local dashboard layout checks')
    def test_native_import_data_tabs_and_spa_cleanup(self):
        self.run_browser(r'''
const assert=require('node:assert/strict');const {execFileSync}=require('node:child_process');const {chromium}=require('playwright');
(async()=>{const token=execFileSync('docker',['exec','-w','/src/bot',process.env.JESSE_UI_DOCKER_CONTAINER||'jesse-research-jesse-1','python','-c','from hashlib import sha256; from jesse.services.env import ENV_VALUES; print(sha256(ENV_VALUES["PASSWORD"].encode()).hexdigest())'],{encoding:'utf8'}).trim();
const browser=await chromium.launch({headless:true,...(process.env.JESSE_UI_BROWSER_EXECUTABLE?{executablePath:process.env.JESSE_UI_BROWSER_EXECUTABLE}:{})});try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[],writes=[];page.on('pageerror',e=>errors.push(e.message));
 page.on('request',req=>{if(req.method()==='POST'&&['/candles/import','/funding/import','/open-interest/import','/live','/backtest'].includes(new URL(req.url()).pathname))writes.push(new URL(req.url()).pathname);});
 await page.addInitScript(value=>localStorage.setItem('main',JSON.stringify({authToken:value})),token);
 await page.goto(process.env.JESSE_UI_TEST_URL+'/#/candles/');await page.getByRole('tab',{name:'Candles',exact:true}).waitFor();
 const candleInput=page.getByLabel('Start date',{exact:true});const previousDate=await candleInput.inputValue();
 await page.getByRole('tab',{name:'Funding',exact:true}).click();await page.locator('#jesse-import-data-panel').getByText('Biblioteca de datos',{exact:true}).waitFor();
 assert(page.url().endsWith('#/candles/'));assert.equal(await page.getByRole('link',{name:'Funding / OI',exact:true}).count(),0);
 assert.equal(await page.getByRole('button',{name:'Add import',exact:true}).isVisible(),false);
 await page.getByRole('tab',{name:'Open Interest',exact:true}).click();await page.locator('#jesse-import-data-panel #oi-source').waitFor();
 await page.getByRole('tab',{name:'Candles',exact:true}).click();assert.equal(await candleInput.inputValue(),previousDate);assert.equal(await page.getByRole('button',{name:'Add import',exact:true}).isVisible(),true);
 await page.getByRole('tab',{name:'Funding',exact:true}).click();await page.getByRole('link',{name:'Home',exact:true}).first().click();await page.waitForTimeout(150);assert.equal(await page.locator('#jesse-import-data-tabs').count(),0);
 await page.getByRole('link',{name:'Import Data',exact:true}).first().click();await page.getByRole('tab',{name:'Funding',exact:true}).click();await page.locator('#jesse-import-data-panel').getByText('Biblioteca de datos',{exact:true}).waitFor();assert.equal(await page.locator('#jesse-import-data-tabs').count(),1);
 await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));assert.deepEqual(errors,[]);assert.deepEqual(writes,[]);
}finally{await browser.close()}})().catch(error=>{console.error(error.message);process.exit(1)});
''')

    def test_external_job_discovery_and_legacy_server_fallback(self):
        self.run_browser(r'''
const assert=require('node:assert/strict');const {chromium}=require('playwright');
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.JESSE_UI_BROWSER_EXECUTABLE?{executablePath:process.env.JESSE_UI_BROWSER_EXECUTABLE}:{})});try{
 const job={job_id:'00000000-0000-0000-0000-000000000099',status:'running',updated_at:Date.UTC(2026,9,20),progress:{phase:'archive',fetched_days:51,total_days:100}};
 for(const legacy of [false,true]){
  const page=await browser.newPage();const calls=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.addInitScript(()=>localStorage.setItem('test-auth',JSON.stringify({authToken:'synthetic-test-token'})));
  await page.route('**/*',async route=>{const req=route.request();if(req.method()!=='POST')return route.continue();const endpoint=new URL(req.url()).pathname;calls.push(endpoint);let payload={};let status=200;
   if(['/funding/datasets','/open-interest/datasets'].includes(endpoint))payload={datasets:[]};
   else if(endpoint==='/open-interest/jobs'){payload=legacy?{detail:'Not Found'}:{jobs:[job]};status=legacy?404:200;}
   else if(endpoint==='/open-interest/job')payload=job;
   else throw Error('Unexpected endpoint '+endpoint);
   await route.fulfill({status,contentType:'application/json',body:JSON.stringify(payload)});
  });
  await page.goto(process.env.JESSE_UI_TEST_URL+'/funding/index.html');
  if(legacy){await page.getByText('Todavía no hay versiones guardadas para este tipo de datos.',{exact:true}).waitFor();assert.equal(await page.locator('#oi-job-panel').isVisible(),false);assert.equal(await page.locator('#global-message').isVisible(),false);}
  else{await page.getByText('51 de 100 días descargados',{exact:false}).waitFor();assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('jesse-open-interest-import-job')).job_id),job.job_id);}
  assert.deepEqual(errors,[]);assert(calls.every(endpoint=>!endpoint.endsWith('/import')&&!endpoint.endsWith('/update')));await page.close();
 }
}finally{await browser.close()}})().catch(error=>{console.error(error);process.exit(1)});
''')


if __name__ == '__main__':
    unittest.main()
