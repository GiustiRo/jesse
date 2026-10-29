const {test}=require('node:test');
const assert=require('node:assert/strict');
const U=require('../jesse/static/research/logic.js');
test('paged reads follow cursor and reject changing, truncated, or absent evidence',async()=>{
  const calls=[];
  const request=async(url,b)=>{calls.push(b);return {status:'success',kind:'text',content:b.start_line===1?'first\n':'second',modified_at:'fixed',has_more:b.start_line===1,next_start_line:401};};
  assert.equal(await U.readText(U.BASE+'index.json',request),'first\nsecond');
  assert.deepEqual(calls.map(c=>c.start_line),[1,401]);
  for(const result of [{status:'error',error_type:'not_found'},{status:'success',kind:'binary'},{status:'success',kind:'text',content:'x',line_truncated:true},{status:'success',kind:'text',content:'x',has_more:true,next_start_line:1}]){
    await assert.rejects(()=>U.readText(U.BASE+'index.json',async()=>result));
  }
  let n=0;await assert.rejects(()=>U.readText(U.BASE+'index.json',async()=>({status:'success',kind:'text',content:'x',modified_at:String(n++),has_more:n===1,next_start_line:2})),/cambió/);
});
test('protocol needs numeric gates and budgets, complete fields and temporal order',()=>{
  assert.ok(U.protocolErrors(null).length);
  const p=Object.fromEntries(['hypothesis','refutation','rules','references','data','costs','risk','windows','selection','code_version','data_version'].map(k=>[k,'declared']));
  Object.assign(p,{budget:{runs:12},criteria:{min_n:30,max_dd:25},registered_at_utc:'2026-10-01T00:00:00Z'});
  assert.deepEqual(U.protocolErrors(p),[]);
  assert.ok(U.protocolErrors(p,true).includes('fecha de primera ejecución ausente'));
  assert.ok(U.protocolErrors({...p,criteria:{N:'30'}}).includes('criteria'));
  assert.ok(U.protocolErrors({...p,first_run_at_utc:'2026-09-30T00:00:00Z'}).length);
});
test('revisions, confinement and independent filters',()=>{
  for(const path of ['../secret','strategies/A/../secret','https://example.org/x','strategies/A/x?y','strategies//A'])assert.throws(()=>U.path(path));
  assert.throws(()=>U.validateIndex({format_version:2}));
  assert.throws(()=>U.validateIndex({format_version:1,current:'absent',revisions:[]}));
  const row={asset:'BTC',family:'trend',execution:'closed'};
  assert.equal(U.matches(row,{asset:'BTC',family:'trend'}),true);
  assert.equal(U.matches(row,{asset:'PAXG'}),false);
});
