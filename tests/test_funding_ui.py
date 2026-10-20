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
    let session={mode:'disabled',requested_mode:'disabled',applied:false,status:'disabled',session_status:'draft',funding_config:{mode:'disabled'},open_interest_config:{mode:'disabled'},route_symbols:['BTC-USDT','PAXG-USDT'],ledger:[]};
    await page.addInitScript(() => localStorage.setItem('funding-ui-test',JSON.stringify({authToken:'synthetic-test-token'})));
    await page.route('**/*',async route => {
      const request=route.request();
      if(request.method() !== 'POST') return route.continue();
      const path=new URL(request.url()).pathname; const body=request.postDataJSON();
      calls.push({path,body}); let payload={};
      if(path==='/funding/datasets') payload={datasets:fundingDatasets};
      else if(path==='/open-interest/datasets') payload={datasets:[{dataset_id:oiId,source:'binance-rest',start,finish,observation_count:2016,expected_observation_count:2016,missing_observation_count:0,status:'ready',coverage_complete:true,first_observation:start,last_observation:finish-300000},{dataset_id:incompleteId,source:'binance-rest',start,finish:start+2592*300000,observation_count:500,expected_observation_count:2592,missing_observation_count:2092,status:'incomplete',coverage_complete:false,first_observation:start,last_observation:start+499*300000,leading_gap_ms:0,trailing_gap_ms:2092*300000}]};
      else if(path==='/funding/session') payload=session;
      else if(path==='/funding/session-config') {
        assert.equal(body.funding.dataset_id,fundingId);
        assert.deepEqual(body.funding.exclude_symbols,['PAXG-USDT']);
        assert.equal(body.open_interest.mode,'disabled');
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
        result = subprocess.run(['node', '-e', script], cwd=ROOT, text=True, encoding='utf-8', capture_output=True, timeout=120)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
