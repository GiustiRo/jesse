/* Source-owned research reader. The only API operation is an authenticated read. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.JesseResearch = api;
})(globalThis, function () {
  'use strict';
  const BASE = 'strategies/FundingOiPilot4h/reports/RESEARCH_HUB/';
  const required = ['hypothesis', 'refutation', 'rules', 'references', 'data', 'costs', 'risk', 'windows', 'selection', 'code_version', 'data_version'];
  function path(value) {
    if (typeof value !== 'string' || !/^strategies\/[A-Za-z0-9_./-]+$/.test(value) || value.split('/').some(p => !p || p === '.' || p === '..')) throw new Error('Referencia inválida');
    return value;
  }
  function protocolErrors(p,executed=false) {
    if (!p || typeof p !== 'object') return ['protocolo ausente'];
    const errors = required.filter(k => typeof p[k] !== 'string' || !p[k].trim());
    for (const k of ['budget', 'criteria']) {
      if (!p[k] || Array.isArray(p[k]) || typeof p[k] !== 'object' || !Object.keys(p[k]).length || Object.values(p[k]).some(v => typeof v !== 'number' || !Number.isFinite(v))) errors.push(k);
    }
    if (!Number.isFinite(Date.parse(p.registered_at_utc))) errors.push('fecha de prerregistro');
    if (executed&&!p.first_run_at_utc) errors.push('fecha de primera ejecución ausente');
    if (p.first_run_at_utc && !(Date.parse(p.registered_at_utc) < Date.parse(p.first_run_at_utc))) errors.push('cronología no acreditada');
    return errors;
  }
  function validateIndex(i) {
    if (i?.format_version !== 1 || !Array.isArray(i.revisions) || !i.revisions.length || !i.revisions.some(r => r.id === i.current)) throw new Error('Índice incompleto o formato no soportado');
    if (i.revisions.some(r => typeof r.id !== 'string' || !r.id) || new Set(i.revisions.map(r=>r.id)).size !== i.revisions.length) throw new Error('Identificadores de revisión inválidos');
    i.revisions.forEach(r => path(r.path));
    return i;
  }
  function validateRevision(r,id){
    if(r?.format_version!==1 || r.id!==id || !Number.isFinite(Date.parse(r.updated_at_utc)))throw new Error('Revisión incompleta');
    for(const key of ['explorations','documents','decisions','lines','methodology','supersedes','roadmap'])if(!Array.isArray(r[key]))throw new Error('Revisión incompleta: '+key);
    for(const key of ['objective','latest','next','blockers'])if(typeof r[key]!=='string')throw new Error('Revisión incompleta: '+key);
    if(!Array.isArray(r.counts?.cycles))throw new Error('Revisión incompleta: conteos');
    for(const e of r.explorations){path(e.path);for(const k of ['id','title','asset','family','execution'])if(typeof e[k]!=='string')throw new Error('Ficha de índice incompleta');}
    for(const d of r.documents)path(d.path);
    return r;
  }
  async function readText(file, request, signal) {
    path(file);
    let line = 1, result = '', modified;
    // The server caps each page. Follow its cursor; refuse inconsistent pages
    // instead of parsing a truncated JSON document as a complete revision.
    // This UI ceiling bounds malformed cursor streams independently of the
    // server's per-page cap; ordinary reports fit well below 512 pages.
    for (let page = 0; page < 512; page++) {
      const r = await request('/project-files/read', {path:file, start_line:line, max_lines:400}, signal);
      if (r.status !== 'success') throw new Error(r.error_type === 'not_found' ? 'Documento ausente: ' + file : (r.message || 'Error de lectura'));
      if (r.kind !== 'text' || r.line_truncated || typeof r.content !== 'string') throw new Error('Documento binario o línea truncada: ' + file);
      if (modified && modified !== r.modified_at) throw new Error('El documento cambió durante la lectura; actualizar');
      modified = r.modified_at;
      result += r.content;
      if (!r.has_more) return result;
      if (!Number.isInteger(r.next_start_line) || r.next_start_line <= line) throw new Error('Paginación inválida');
      line = r.next_start_line;
      if (!result.endsWith('\n')) result += '\n';
    }
    throw new Error('Documento excede el límite de lectura del panel');
  }
  function matches(x, filters) {
    return ['asset', 'family', 'execution'].every(k => !filters[k] || x[k] === filters[k]);
  }
  return {BASE, path, protocolErrors, validateIndex, validateRevision, readText, matches};
});
