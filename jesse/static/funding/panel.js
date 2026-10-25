(() => {
  "use strict";
  function mount(root = document, options = {}) {
  const { fundingStatus, utcDate, rate, money, escape: esc } = window.JesseFundingUI;
  const $ = id => root.getElementById(id);
  const state = { kind: "funding", datasets: { funding: [], oi: [] }, loaded: { funding: false, oi: false }, selected: { funding: "", oi: "" }, session: null, offset: 0, total: 0 };
  const PAGE_SIZE = 100;
  const JOB_STORAGE_KEY = "jesse-open-interest-import-job";
  // Archive downloads run server-side. Poll only after the previous read ends
  // and stop the timer on SPA unmount; the job survives in localStorage.
  const JOB_POLL_MS = 4000;
  let jobTimer = null;
  let disposed = false;
  const jobActive = () => state.job && ["queued", "running"].includes(state.job.status);

  function authToken() {
    // Reuse the dashboard's existing login without storing another credential.
    for (let index = 0; index < localStorage.length; index += 1) {
      try {
        const value = JSON.parse(localStorage.getItem(localStorage.key(index)) || "null");
        if (value && typeof value.authToken === "string") return value.authToken;
      } catch { /* Other applications may store ordinary strings on this origin. */ }
    }
    return "";
  }

  async function api(path, body = {}) {
    const token = authToken();
    if (!token) throw new Error("Iniciá sesión en el dashboard y luego volvé a esta página.");
    const response = await fetch(path, { method: "POST", headers: { "Content-Type": "application/json", Authorization: token }, body: JSON.stringify(body) });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) {
      const detail = payload.detail || payload.error || payload.message;
      const error = new Error(response.status === 401 ? "La sesión de acceso venció. Volvé a iniciar sesión en el dashboard." : typeof detail === "string" ? detail : `La solicitud falló (${response.status}).`);
      error.status = response.status;
      throw error;
    }
    return payload;
  }

  function message(text, error = false) {
    const target = $("global-message");
    target.textContent = text;
    target.className = `message ${error ? "error" : "success"}`;
    target.hidden = false;
  }

  async function action(button, task) {
    const original = button.textContent;
    button.disabled = true;
    button.textContent = "Procesando…";
    try { await task(); }
    catch (error) { message(error.message, true); }
    finally {
      button.textContent = original;
      if (button.id === "ledger-prev") button.disabled = state.offset === 0;
      else if (button.id === "ledger-next") button.disabled = state.offset + PAGE_SIZE >= state.total;
      else if (["import-data", "update-data"].includes(button.id) && state.kind === "oi" && jobActive()) button.disabled = true;
      else button.disabled = button.id === "update-data" && !state.selected[state.kind];
    }
  }

  function endpoint(kind = state.kind) { return kind === "funding" ? "/funding" : "/open-interest"; }
  function unwrap(payload) { return payload.dataset || payload; }
  function count(dataset) { return dataset.event_count ?? dataset.record_count ?? dataset.point_count ?? dataset.observation_count ?? 0; }
  function coverageLabel(dataset) {
    if (dataset.coverage_complete === false || dataset.status === "incomplete") return `Incompleta · faltan ${dataset.missing_observation_count ?? "registros"}`;
    if (dataset.coverage_complete === true || dataset.status === "ready") return "Completa";
    return "Consultar cobertura";
  }
  function datasetSelectable(kind, dataset) {
    const incomplete = dataset.coverage_complete === false || dataset.status === "incomplete";
    return !incomplete || kind === "oi" && $("allow-missing-oi").checked;
  }
  function dateOnly(value) { return Number.isFinite(Number(value)) ? new Date(Number(value)).toISOString().slice(0, 10) : "—"; }
  function fillDatasetSelect(kind) {
    const select = $(kind === "funding" ? "funding-dataset" : "oi-dataset");
    const previous = [...select.selectedOptions].map(option => option.value);
    // Funding is a multi-select (one version per symbol); OI keeps its single select.
    select.innerHTML = (kind === "funding" ? "" : '<option value="">Seleccioná una versión</option>') + state.datasets[kind].map(dataset => `<option value="${esc(dataset.dataset_id)}" ${datasetSelectable(kind, dataset) ? "" : "disabled"}>${kind === "funding" ? `${esc(dataset.symbol || "BTC-USDT")} · ` : ""}${esc(dateOnly(dataset.start))} → ${esc(dateOnly(dataset.finish))} · ${esc(dataset.dataset_id.slice(0, 12))} · ${esc(coverageLabel(dataset))}</option>`).join("");
    for (const option of select.options) option.selected = previous.includes(option.value) && !option.disabled;
    if (kind === "oi") renderOISelectionWarning();
    else renderFundingExclusions();
  }

  function selectedFundingSymbols() {
    const ids = [...$("funding-dataset").selectedOptions].map(option => option.value);
    return state.datasets.funding.filter(dataset => ids.includes(dataset.dataset_id)).map(dataset => dataset.symbol || "BTC-USDT");
  }

  // Each route pays only its own symbol's funding. Routes without a selected
  // version must be excluded explicitly; checked boxes survive re-rendering.
  function renderFundingExclusions(saved) {
    const target = $("funding-exclusions");
    const checked = saved || [...root.querySelectorAll('[name="funding-excluded-symbol"]:checked')].map(input => input.value);
    const covered = selectedFundingSymbols();
    const otherSymbols = [...new Set((state.session?.route_symbols || []).filter(symbol => typeof symbol === "string" && !covered.includes(symbol)))];
    target.hidden = otherSymbols.length === 0;
    target.innerHTML = otherSymbols.length ? `<p class="callout warning"><strong>Funding sólo de ${esc(covered.length ? covered.join(", ") : "los símbolos con versión seleccionada")}; otras rutas requieren exclusión explícita.</strong><br>Excluir una ruta significa que sus costos de funding no se modelan. No se agregan exclusiones automáticamente.</p>` + otherSymbols.map(symbol => `<label class="checkbox-row"><input type="checkbox" name="funding-excluded-symbol" value="${esc(symbol)}" ${checked.includes(symbol) ? "checked" : ""}>Excluir ${esc(symbol)} del cálculo de funding</label>`).join("") : "";
  }

  function renderOISelectionWarning() {
    const dataset = state.datasets.oi.find(row => row.dataset_id === $("oi-dataset").value);
    const incomplete = dataset && (dataset.coverage_complete === false || dataset.status === "incomplete");
    $("oi-selection-warning").hidden = !incomplete;
    $("oi-selection-warning").textContent = incomplete ? `Serie incompleta: ${count(dataset)} de ${dataset.expected_observation_count ?? "—"} observaciones; faltan ${dataset.missing_observation_count ?? "registros"}. Mayor hueco: ${dataset.largest_gap_ms == null ? "sin detalle" : `${(dataset.largest_gap_ms / 3600000).toFixed(2)} h`}. No se interpolan faltantes: la estrategia debe manejar None o abstenerse de operar con ese dato.` : "";
  }

  function renderLibrary() {
    const datasets = state.datasets[state.kind];
    $("library-status").textContent = !state.loaded[state.kind] ? "Cargando biblioteca…" : datasets.length ? `${datasets.length} versiones guardadas. Las ventanas son UTC y excluyen el extremo final.` : "Todavía no hay versiones guardadas para este tipo de datos.";
    $("datasets-body").innerHTML = datasets.length ? datasets.map(dataset => `<tr class="${dataset.dataset_id === state.selected[state.kind] ? "dataset-selected" : ""}">
      <td><label class="dataset-choice"><input type="radio" name="dataset" value="${esc(dataset.dataset_id)}" ${dataset.dataset_id === state.selected[state.kind] ? "checked" : ""}><span>${esc(dataset.dataset_id.slice(0, 10))}</span></label></td>
      <td>${esc(dateOnly(dataset.start))} → ${esc(dateOnly(dataset.finish))}<small>Primero: ${esc(utcDate(dataset.first_settlement ?? dataset.first_observation))}<br>Último: ${esc(utcDate(dataset.last_settlement ?? dataset.last_observation))}</small></td>
      <td>${esc(count(dataset))}${dataset.expected_observation_count != null ? ` de ${esc(dataset.expected_observation_count)} esperados` : ""}<small class="${dataset.coverage_complete === false || dataset.status === "incomplete" ? "coverage-warning" : ""}">${esc(coverageLabel(dataset))}</small><small>${dataset.largest_gap_ms == null ? "" : `Mayor separación: ${esc((dataset.largest_gap_ms / 3600000).toFixed(2))} h`}</small>${dataset.gap_count != null ? `<small>Huecos internos: ${esc(dataset.gap_count)}</small>` : ""}${state.kind === "funding" ? `<small>Precios aproximados: ${esc(dataset.mark_price_proxy_count ?? "Sin detalle")}</small>` : ""}</td>
      <td>${esc(dataset.source || "Binance")}<small>${esc(dataset.mark_price_source || "")}</small>${dataset.archive_file_count ? `<small>ZIP verificados: ${esc(dataset.archive_verified_file_count)} de ${esc(dataset.archive_file_count)}</small><small>Duplicados idénticos eliminados: ${esc(dataset.archive_identical_duplicate_rows ?? 0)}</small><small>Archivo retrospectivo; publicación original no certificada. Disponibilidad supuesta: +6 min.</small>` : ""}<small><code title="${esc(dataset.dataset_id)}">${esc(dataset.dataset_id)}</code></small></td></tr>`).join("") : `<tr><td colspan="4" class="empty">${state.loaded[state.kind] ? "Descargá datos para crear la primera versión." : "Consultando versiones guardadas…"}</td></tr>`;
    $("import-data").disabled = state.kind === "oi" && Boolean(jobActive());
    $("update-data").disabled = !state.selected[state.kind] || state.kind === "oi" && Boolean(jobActive());
    fillDatasetSelect("funding");
    fillDatasetSelect("oi");
  }

  async function refreshDatasets() {
    const results = await Promise.allSettled(["funding", "oi"].map(async kind => {
      const payload = await api(`${endpoint(kind)}/datasets`);
      state.datasets[kind] = payload.datasets || [];
      state.loaded[kind] = true;
    }));
    renderLibrary();
    const failures = results.filter(result => result.status === "rejected");
    if (failures.length) throw failures[0].reason;
  }

  function selectKind(kind) {
    state.kind = kind;
    $("tab-funding").setAttribute("aria-pressed", String(kind === "funding"));
    $("tab-oi").setAttribute("aria-pressed", String(kind === "oi"));
    $("period-label").hidden = kind !== "oi";
    $("oi-source-label").hidden = kind !== "oi";
    $("oi-coverage-note").hidden = kind !== "oi";
    $("allow-mark-proxy-label").hidden = kind !== "funding";
    $("funding-symbol-label").hidden = kind !== "funding";
    $("funding-symbol").required = kind === "funding";
    $("mark-proxy-note").hidden = kind !== "funding";
    updateArchiveConsent();
    $("data-description").textContent = kind === "funding" ? "Tasas ya liquidadas y precio de referencia de cada cobro. Cada descarga genera una versión identificable." : "Interés abierto agregado de Binance: cantidad y valor de contratos. Es una señal disponible para la estrategia, sin movimientos de saldo.";
    renderLibrary();
  }

  function updateArchiveConsent() {
    const archival = $("oi-source").value !== "rest";
    $("archive-consent-label").hidden = state.kind !== "oi" || !archival;
    $("oi-coverage-note").textContent = archival ? "Los archivos oficiales de Binance permiten investigar desde septiembre de 2020. Su publicación original no está certificada: se usa una hipótesis conservadora de disponibilidad y pueden existir revisiones históricas." : "La API REST de interés abierto sólo ofrece una ventana reciente. No permite asumir cobertura desde 2020; para períodos anteriores seleccioná el archivo oficial o la fuente automática.";
  }

  function renderJob(job) {
    state.job = job;
    $("oi-job-panel").hidden = false;
    const failed = ["failed", "interrupted"].includes(job.status);
    $("oi-job-panel").className = `callout ${failed ? "warning" : job.status === "finished" ? "positive" : "neutral"}`;
    const labels = { queued: "Importación de OI en cola", running: "Importación de OI en segundo plano", finished: "Importación de OI terminada", failed: "La importación de OI falló", interrupted: "La importación de OI fue interrumpida" };
    $("oi-job-status").textContent = labels[job.status] || `Estado de importación: ${job.status}`;
    const progress = job.progress || {};
    const parts = [];
    if (progress.fetched_days != null && progress.total_days != null) parts.push(`${progress.fetched_days} de ${progress.total_days} días descargados`);
    if (progress.current_date) parts.push(`Fecha: ${progress.current_date}`);
    if (progress.phase) parts.push(`Fase: ${progress.phase}`);
    const error = typeof job.error === "string" ? job.error : job.error?.message;
    $("oi-job-progress").textContent = failed ? error || "No se publicó una nueva versión. La versión anterior se conserva." : parts.join(" · ") || (job.status === "finished" ? "La nueva versión está disponible en la biblioteca." : "Podés seguir usando el dashboard mientras se descargan los datos.");
    $("oi-job-reference").textContent = `Trabajo: ${job.job_id}.${job.updated_at ? ` Actualizado: ${utcDate(job.updated_at)}.` : ""} La consulta se recupera al volver a esta pantalla.`;
    $("import-data").disabled = state.kind === "oi" && Boolean(jobActive());
    $("update-data").disabled = !state.selected[state.kind] || state.kind === "oi" && Boolean(jobActive());
    if (jobActive()) localStorage.setItem(JOB_STORAGE_KEY, JSON.stringify({ job_id: job.job_id, status: job.status }));
    else localStorage.removeItem(JOB_STORAGE_KEY);
  }

  async function pollJob() {
    if (disposed || !state.job || !jobActive()) return;
    try {
      const job = await api("/open-interest/job", { job_id: state.job.job_id });
      if (disposed) return;
      renderJob(job);
      if (job.status === "finished" && job.result?.dataset_id) {
        state.selected.oi = job.result.dataset_id;
        await refreshDatasets();
        message(`Interés abierto importado. Nueva versión: ${job.result.dataset_id}.`);
      } else if (["failed", "interrupted"].includes(job.status)) {
        message($("oi-job-progress").textContent + " La versión anterior se conserva.", true);
      }
    } catch (error) {
      if (!disposed && [400, 404].includes(error.status)) {
        renderJob({ ...state.job, status: "interrupted", error: error.message });
        message(`No se pudo recuperar el trabajo: ${error.message} La versión anterior se conserva.`, true);
      } else if (!disposed) message(`No se pudo consultar la importación: ${error.message} Se reintentará sin reiniciar el trabajo.`, true);
    }
    if (!disposed && jobActive()) jobTimer = setTimeout(pollJob, JOB_POLL_MS);
  }

  async function consumeImportResult(result, kind) {
    if (kind === "oi" && result.job_id) {
      renderJob(result);
      if (result.status === "finished" && result.result?.dataset_id) {
        state.selected.oi = result.result.dataset_id;
        await refreshDatasets();
        message(`Interés abierto importado. Nueva versión: ${result.result.dataset_id}.`);
      } else if (["failed", "interrupted"].includes(result.status)) {
        message($("oi-job-progress").textContent + " La versión anterior se conserva.", true);
      } else jobTimer = setTimeout(pollJob, 0);
      return;
    }
    state.selected[kind] = result.dataset_id;
    await refreshDatasets();
    message(`Versión guardada: ${result.dataset_id}. Revisá su cobertura antes de usarla.`);
  }

  async function discoverJob() {
    try {
      const payload = await api("/open-interest/jobs", { limit: 20 });
      if (disposed || jobActive()) return;
      const jobs = payload.jobs || [];
      const active = jobs.find(job => ["queued", "running"].includes(job.status));
      if (active) { renderJob(active); jobTimer = setTimeout(pollJob, 0); }
      else if (["failed", "interrupted"].includes(jobs[0]?.status)) renderJob(jobs[0]);
    } catch (error) {
      // An older running Jesse process may not expose discovery until restart.
      // Import/data reads still work, and an explicitly saved job can be polled.
      if (!disposed && error.status !== 404) message(`No se pudieron consultar los trabajos de OI: ${error.message}`, true);
    }
  }

  function summaryItem(label, value, note = "") {
    return `<div class="summary-item"><span>${esc(label)}</span><strong>${esc(value)}</strong>${note ? `<small>${esc(note)}</small>` : ""}</div>`;
  }

  function renderSession(result) {
    state.session = result;
    const status = fundingStatus(result);
    $("session-status").className = `callout ${status.tone}`;
    $("session-status").innerHTML = `<strong>${esc(status.label)}</strong><p>${esc(status.detail)}</p>`;
    const applied = result.applied === true;
    const oi = result.open_interest;
    const oiApplied = oi?.applied === true;
    $("session-summary").hidden = false;
    const sessionStatus = result.session_status || result.status;
    $("session-summary").innerHTML = summaryItem("Estado de la sesión", sessionStatus || "—") +
      summaryItem("Funding neto", applied ? money(result.cashflow) : "No confirmado", "Positivo: cobro · negativo: pago") +
      summaryItem("Liquidaciones con posición", applied ? result.event_count ?? result.total ?? 0 : "—") +
      (result.dataset_ids?.length > 1 ? summaryItem("Versiones usadas", result.dataset_ids.map(id => id.slice(0, 12)).join(", "), Object.entries(result.cashflow_by_symbol || {}).map(([symbol, cash]) => `${symbol}: ${money(cash)}`).join(" · ")) : summaryItem("Versión usada", result.dataset_id ? result.dataset_id.slice(0, 16) : "—", result.dataset_id || "Sin versión registrada")) +
      summaryItem("Interés abierto", oiApplied ? "Histórico aplicado" : oi?.mode === "historical" ? "Sin aplicación confirmada" : oi?.mode === "disabled" ? "Desactivado" : "Sin evidencia", oiApplied ? "Fuente disponible a la estrategia; no implica que sus reglas la usen" : oi?.dataset_id || "") +
      (oiApplied ? summaryItem("Versión de interés abierto", oi.dataset_id ? oi.dataset_id.slice(0, 16) : "—", oi.dataset_id || "Sin versión registrada") : "") +
      (oiApplied ? summaryItem("Datos de interés abierto", `${oi.observation_count ?? oi.data?.observation_count ?? "—"} observaciones`, oi.data ? `${coverageLabel(oi.data)} · Primera: ${utcDate(oi.data.first_observation)} · Última: ${utcDate(oi.data.last_observation)}` : "Sin detalle de cobertura") : "") +
      (applied ? summaryItem("Cobertura de funding", (result.scope || ["BTC-USDT"]).join(", "), "El dataset cubre únicamente estos instrumentos") : "") +
      (applied ? summaryItem("Precios aproximados del dataset", result.data?.mark_price_proxy_count ?? result.dataset?.mark_price_proxy_count ?? "Sin detalle", "Cantidad en la versión completa; no equivale a pagos de esta sesión") : "") +
      (applied ? summaryItem("Movimientos con precio aproximado", result.mark_price_proxy_count ?? "Sin detalle", "Pagos y cobros de esta sesión que usaron un precio aproximado") : "") +
      (result.excluded_symbols?.length ? summaryItem("Rutas sin funding modelado", result.excluded_symbols.join(", "), "Exclusiones explícitas: sus costos de funding no se contabilizaron") : "");
    $("session-link").href = result.dashboard_url || `/#/backtest/${encodeURIComponent($("session-id").value.trim())}`;
    $("session-link").hidden = false;
    $("session-config-form").hidden = sessionStatus !== "draft";
    if (sessionStatus === "draft") {
      const funding = result.funding_config || { mode: result.requested_mode || "disabled", dataset_id: result.requested_dataset_id };
      const oi = result.open_interest_config || { mode: "disabled" };
      $("enable-funding").checked = funding.mode === "historical";
      $("enable-oi").checked = oi.mode === "historical";
      $("allow-missing-oi").checked = oi.allow_missing_observations === true;
      fillDatasetSelect("oi");
      const fundingIds = funding.dataset_ids || (funding.dataset_id ? [funding.dataset_id] : []);
      for (const option of $("funding-dataset").options) option.selected = fundingIds.includes(option.value);
      $("oi-dataset").value = oi.dataset_id || "";
      renderOISelectionWarning();
      renderFundingExclusions(funding.exclude_symbols || []);
    }
    const ledger = result.ledger || [];
    state.total = result.total ?? result.event_count ?? ledger.length;
    $("ledger-section").hidden = !applied;
    $("ledger-body").innerHTML = ledger.length ? ledger.map(row => `<tr><td>${esc(utcDate(row.settled_at))}</td><td>${esc(row.symbol || "BTC-USDT")}</td><td>${esc(rate(row.rate_decimal))}</td><td>${esc(row.qty)}</td><td>${esc(Number(row.mark_price).toFixed(4))}</td><td>${esc(row.mark_price_source === "fundingRate.settlement_mark" ? "Liquidación Binance" : row.mark_price_source === "markPriceKlines.1h_open_proxy" ? "Aproximado · apertura mark 1h" : "Sin detalle")}</td><td>${esc(money(row.cashflow))}</td></tr>`).join("") : '<tr><td colspan="7" class="empty">No hubo movimientos de funding con una posición abierta.</td></tr>';
    $("ledger-page").textContent = state.total ? `${state.offset + 1}–${Math.min(state.offset + ledger.length, state.total)} de ${state.total}` : "0 movimientos";
    $("ledger-prev").disabled = state.offset === 0;
    $("ledger-next").disabled = state.offset + PAGE_SIZE >= state.total;
  }

  async function loadSession(reset = false) {
    const id = $("session-id").value.trim();
    if (!id) return;
    if (reset) state.offset = 0;
    const result = await api("/funding/session", { session_id: id, offset: state.offset, limit: PAGE_SIZE });
    renderSession(result);
  }

  async function loadLive() {
    const id = $("live-session-id").value.trim();
    if (!id) return;
    const payload = await api("/funding/live-session", { session_id: id, offset: 0, limit: PAGE_SIZE });
    const result = payload.funding || payload;
    const status = result.status || "unavailable";
    const disabled = result.mode === "disabled" || status === "disabled";
    const synced = !disabled && ["ok", "ready", "synced", "fresh", "healthy"].includes(status) && result.stale !== true;
    $("live-status").className = `callout ${synced ? "positive" : disabled ? "neutral" : "warning"}`;
    $("live-status").innerHTML = `<strong>${esc(disabled ? "Funding live desactivado" : synced ? "Datos de funding actualizados" : "Funding sin actualización confirmada")}</strong><p>${esc(result.error || result.message || (disabled ? "Esta sesión no solicita consumo de funding." : "El saldo del exchange ya contiene los cobros y pagos reales; no se descuentan una segunda vez."))}</p>`;
    $("live-summary").hidden = false;
    $("live-summary").innerHTML = summaryItem("Estado reportado", status) +
      summaryItem("Tasa estimada", rate(result.rate_decimal ?? result.estimated_rate_decimal ?? result.funding_rate ?? result.estimated_rate), "Puede cambiar antes del cobro") +
      summaryItem("Próxima liquidación", utcDate(result.next_funding_timestamp ?? result.next_funding_at)) +
      summaryItem("Última actualización", utcDate(result.updated_at ?? result.observed_at)) +
      summaryItem("Neto conciliado de la cuenta", money(result.cashflow ?? result.income_cashflow), "No atribuido automáticamente a esta estrategia") +
      summaryItem("Interés abierto live", result.open_interest?.value != null ? `${result.open_interest.value} ${result.open_interest.units || "BTC"}` : "—", result.open_interest ? `${result.open_interest.status || "Sin estado"} · ${utcDate(result.open_interest.observed_at)}` : "Sin evidencia");
    const ledger = result.ledger || [];
    $("live-ledger-section").hidden = disabled;
    $("live-ledger-body").innerHTML = ledger.length ? ledger.map(row => `<tr><td>${esc(utcDate(row.time ?? row.settled_at))}</td><td>${esc(row.symbol)}</td><td>${esc(money(row.income ?? row.cashflow))}</td><td>${esc(row.tranId ?? row.transaction_id ?? "—")}</td></tr>`).join("") : '<tr><td colspan="4" class="empty">No hay movimientos conciliados en la ventana reportada.</td></tr>';
  }

  const today = new Date().toISOString().slice(0, 10);
  $("finish-date").value = today;
  $("update-finish").value = today;
  const previous = new Date(); previous.setUTCDate(previous.getUTCDate() - 7);
  $("start-date").value = previous.toISOString().slice(0, 10);
  $("tab-funding").addEventListener("click", () => selectKind("funding"));
  $("tab-oi").addEventListener("click", () => selectKind("oi"));
  $("oi-source").addEventListener("change", updateArchiveConsent);
  $("allow-missing-oi").addEventListener("change", () => fillDatasetSelect("oi"));
  $("oi-dataset").addEventListener("change", renderOISelectionWarning);
  $("funding-dataset").addEventListener("change", () => renderFundingExclusions());
  $("refresh-datasets").addEventListener("click", event => action(event.currentTarget, refreshDatasets));
  $("datasets-body").addEventListener("change", event => {
    if (event.target.name !== "dataset") return;
    state.selected[state.kind] = event.target.value;
    renderLibrary();
  });
  $("import-form").addEventListener("submit", event => {
    event.preventDefault();
    action($("import-data"), async () => {
      const body = { start_date: $("start-date").value, finish_date: $("finish-date").value };
      if (body.start_date >= body.finish_date) throw new Error("La fecha final debe ser posterior a la inicial.");
      const kind = state.kind;
      if (kind === "oi") {
        body.period = $("oi-period").value;
        body.source = $("oi-source").value;
        body.allow_archive_assumptions = $("allow-archive-assumptions").checked;
        body.background = true;
        if (body.source !== "rest" && !body.allow_archive_assumptions) throw new Error("Para usar archivos históricos tenés que aceptar explícitamente la hipótesis de publicación y las posibles revisiones.");
      }
      else {
        body.allow_mark_price_proxy = $("allow-mark-proxy").checked;
        body.symbol = $("funding-symbol").value.trim().toUpperCase();
      }
      const result = unwrap(await api(`${endpoint()}/import`, body));
      await consumeImportResult(result, kind);
    });
  });
  $("update-data").addEventListener("click", event => action(event.currentTarget, async () => {
    const kind = state.kind;
    const result = unwrap(await api(`${endpoint()}/update`, { dataset_id: state.selected[kind], finish_date: $("update-finish").value, ...(kind === "oi" ? { background: true } : {}) }));
    await consumeImportResult(result, kind);
  }));
  $("session-form").addEventListener("submit", event => { event.preventDefault(); action(event.submitter || $("session-form").querySelector("button"), () => loadSession(true)); });
  $("load-drafts").addEventListener("click", event => action(event.currentTarget, async () => {
    const result = await api("/backtest/sessions", { limit: 100, offset: 0, status_filter: "draft" });
    $("drafts").innerHTML = '<option value="">Seleccioná un borrador</option>' + (result.sessions || []).map(session => `<option value="${esc(session.id)}">${esc(session.title || session.id)}</option>`).join("");
    $("drafts-label").hidden = false;
  }));
  $("drafts").addEventListener("change", () => { if ($("drafts").value) { $("session-id").value = $("drafts").value; action($("load-drafts"), () => loadSession(true)); } });
  $("session-config-form").addEventListener("submit", event => {
    event.preventDefault();
    action($("save-config"), async () => {
      const fundingIds = [...$("funding-dataset").selectedOptions].map(option => option.value).filter(Boolean);
      // One version keeps the original dataset_id shape; several use dataset_ids.
      const funding = !$("enable-funding").checked ? { mode: "disabled" } : fundingIds.length > 1 ? { mode: "historical", dataset_ids: fundingIds } : { mode: "historical", dataset_id: fundingIds[0] || "" };
      const open_interest = $("enable-oi").checked ? { mode: "historical", dataset_id: $("oi-dataset").value } : { mode: "disabled" };
      if (open_interest.mode === "historical" && $("allow-missing-oi").checked) open_interest.allow_missing_observations = true;
      if (funding.mode === "historical" && !fundingIds.length || open_interest.mode === "historical" && !open_interest.dataset_id) throw new Error("Seleccioná una versión para cada fuente habilitada.");
      if (funding.mode === "historical") {
        const symbols = selectedFundingSymbols();
        if (new Set(symbols).size !== symbols.length) throw new Error("Seleccioná una sola versión de funding por símbolo.");
        const exclusions = [...root.querySelectorAll('[name="funding-excluded-symbol"]')];
        if (exclusions.some(input => !input.checked)) throw new Error(`El funding sólo cubre ${symbols.join(", ")}. Las demás rutas requieren exclusión explícita; sus costos de funding quedarían sin modelar.`);
        if (exclusions.length) funding.exclude_symbols = exclusions.map(input => input.value);
      }
      await api("/funding/session-config", { session_id: $("session-id").value.trim(), funding, open_interest });
      await loadSession(true);
      message("Configuración guardada en el borrador. Volvé a abrirlo en el dashboard antes de ejecutarlo para cargar estos valores.");
    });
  });
  $("ledger-prev").addEventListener("click", event => action(event.currentTarget, async () => { state.offset = Math.max(0, state.offset - PAGE_SIZE); await loadSession(); }));
  $("ledger-next").addEventListener("click", event => action(event.currentTarget, async () => { state.offset += PAGE_SIZE; await loadSession(); }));
  $("live-form").addEventListener("submit", event => { event.preventDefault(); action(event.submitter || $("live-form").querySelector("button"), loadLive); });
  const refreshTimer = setInterval(() => {
    if (!$("auto-refresh").checked || document.hidden) return;
    Promise.all([$("session-id").value && loadSession(), $("live-session-id").value && loadLive()]).catch(error => message(error.message, true));
  }, 30_000);
  const sessionId = options.sessionId || new URLSearchParams(location.search).get("session_id");
  if (sessionId) $("session-id").value = sessionId;
  if (options.kind) selectKind(options.kind);
  let restoredJob = false;
  try {
    const savedJob = JSON.parse(localStorage.getItem(JOB_STORAGE_KEY) || "null");
    if (savedJob?.job_id) { restoredJob = true; renderJob(savedJob); jobTimer = setTimeout(pollJob, 0); }
  } catch { localStorage.removeItem(JOB_STORAGE_KEY); }
  if (!restoredJob) discoverJob();
  refreshDatasets().then(() => sessionId && loadSession(true)).catch(error => { $("library-status").textContent = "No se pudo cargar la biblioteca."; message(error.message, true); });
  return { selectKind, destroy() { disposed = true; clearInterval(refreshTimer); clearTimeout(jobTimer); } };
  }
  window.JesseFundingPanel = { mount };
  // The same source is mounted inline by the Import Data route extension and
  // standalone for backwards-compatible links to existing session reports.
  if (document.getElementById("import-form")) mount();
})();
