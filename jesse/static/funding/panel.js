(() => {
  "use strict";
  const { fundingStatus, utcDate, rate, money, escape: esc } = window.JesseFundingUI;
  const $ = id => document.getElementById(id);
  const state = { kind: "funding", datasets: { funding: [], oi: [] }, selected: { funding: "", oi: "" }, session: null, offset: 0, total: 0 };
  const PAGE_SIZE = 100;

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
      throw new Error(response.status === 401 ? "La sesión de acceso venció. Volvé a iniciar sesión en el dashboard." : typeof detail === "string" ? detail : `La solicitud falló (${response.status}).`);
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
  function dateOnly(value) { return Number.isFinite(Number(value)) ? new Date(Number(value)).toISOString().slice(0, 10) : "—"; }
  function fillDatasetSelect(kind) {
    const select = $(kind === "funding" ? "funding-dataset" : "oi-dataset");
    const previous = select.value;
    select.innerHTML = '<option value="">Seleccioná una versión</option>' + state.datasets[kind].map(dataset => `<option value="${esc(dataset.dataset_id)}" ${dataset.coverage_complete === false || dataset.status === "incomplete" ? "disabled" : ""}>${esc(dateOnly(dataset.start))} → ${esc(dateOnly(dataset.finish))} · ${esc(dataset.dataset_id.slice(0, 12))} · ${esc(coverageLabel(dataset))}</option>`).join("");
    if (state.datasets[kind].some(dataset => dataset.dataset_id === previous)) select.value = previous;
  }

  function renderLibrary() {
    const datasets = state.datasets[state.kind];
    $("library-status").textContent = datasets.length ? `${datasets.length} versiones guardadas. Las ventanas son UTC y excluyen el extremo final.` : "Todavía no hay versiones guardadas para este tipo de datos.";
    $("datasets-body").innerHTML = datasets.length ? datasets.map(dataset => `<tr class="${dataset.dataset_id === state.selected[state.kind] ? "dataset-selected" : ""}">
      <td><label class="dataset-choice"><input type="radio" name="dataset" value="${esc(dataset.dataset_id)}" ${dataset.dataset_id === state.selected[state.kind] ? "checked" : ""}><span>${esc(dataset.dataset_id.slice(0, 10))}</span></label></td>
      <td>${esc(dateOnly(dataset.start))} → ${esc(dateOnly(dataset.finish))}<small>Primero: ${esc(utcDate(dataset.first_settlement ?? dataset.first_observation))}<br>Último: ${esc(utcDate(dataset.last_settlement ?? dataset.last_observation))}</small></td>
      <td>${esc(count(dataset))}${dataset.expected_observation_count != null ? ` de ${esc(dataset.expected_observation_count)} esperados` : ""}<small class="${dataset.coverage_complete === false || dataset.status === "incomplete" ? "coverage-warning" : ""}">${esc(coverageLabel(dataset))}</small><small>${dataset.largest_gap_ms == null ? "" : `Mayor separación: ${esc((dataset.largest_gap_ms / 3600000).toFixed(2))} h`}</small>${state.kind === "funding" ? `<small>Precios aproximados: ${esc(dataset.mark_price_proxy_count ?? "Sin detalle")}</small>` : ""}</td>
      <td>${esc(dataset.source || "Binance")}<small>${esc(dataset.mark_price_source || "")}</small><small><code title="${esc(dataset.dataset_id)}">${esc(dataset.dataset_id)}</code></small></td></tr>`).join("") : '<tr><td colspan="4" class="empty">Descargá datos para crear la primera versión.</td></tr>';
    $("update-data").disabled = !state.selected[state.kind];
    fillDatasetSelect("funding");
    fillDatasetSelect("oi");
  }

  async function refreshDatasets() {
    const results = await Promise.allSettled(["funding", "oi"].map(async kind => {
      const payload = await api(`${endpoint(kind)}/datasets`);
      state.datasets[kind] = payload.datasets || [];
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
    $("oi-coverage-note").hidden = kind !== "oi";
    $("allow-mark-proxy-label").hidden = kind !== "funding";
    $("mark-proxy-note").hidden = kind !== "funding";
    $("data-description").textContent = kind === "funding" ? "Tasas ya liquidadas y precio de referencia de cada cobro. Cada descarga genera una versión identificable." : "Interés abierto agregado de Binance: cantidad y valor de contratos. Es una señal disponible para la estrategia, sin movimientos de saldo.";
    renderLibrary();
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
      summaryItem("Versión usada", result.dataset_id ? result.dataset_id.slice(0, 16) : "—", result.dataset_id || "Sin versión registrada") +
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
      $("funding-dataset").value = funding.dataset_id || "";
      $("oi-dataset").value = oi.dataset_id || "";
      const otherSymbols = [...new Set((result.route_symbols || []).filter(symbol => typeof symbol === "string" && symbol !== "BTC-USDT"))];
      $("funding-exclusions").hidden = otherSymbols.length === 0;
      $("funding-exclusions").innerHTML = otherSymbols.length ? '<p class="callout warning"><strong>Funding sólo BTC; otras rutas requieren exclusión explícita.</strong><br>Excluir una ruta significa que sus costos de funding no se modelan. No se agregan exclusiones automáticamente.</p>' + otherSymbols.map(symbol => `<label class="checkbox-row"><input type="checkbox" name="funding-excluded-symbol" value="${esc(symbol)}" ${(funding.exclude_symbols || []).includes(symbol) ? "checked" : ""}>Excluir ${esc(symbol)} del cálculo de funding</label>`).join("") : "";
    }
    const ledger = result.ledger || [];
    state.total = result.total ?? result.event_count ?? ledger.length;
    $("ledger-section").hidden = !applied;
    $("ledger-body").innerHTML = ledger.length ? ledger.map(row => `<tr><td>${esc(utcDate(row.settled_at))}</td><td>${esc(rate(row.rate_decimal))}</td><td>${esc(row.qty)}</td><td>${esc(Number(row.mark_price).toFixed(4))}</td><td>${esc(row.mark_price_source === "fundingRate.settlement_mark" ? "Liquidación Binance" : row.mark_price_source === "markPriceKlines.1h_open_proxy" ? "Aproximado · apertura mark 1h" : "Sin detalle")}</td><td>${esc(money(row.cashflow))}</td></tr>`).join("") : '<tr><td colspan="6" class="empty">No hubo movimientos de funding con una posición abierta.</td></tr>';
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
      if (state.kind === "oi") { body.period = $("oi-period").value; body.source = "rest"; }
      else body.allow_mark_price_proxy = $("allow-mark-proxy").checked;
      const result = unwrap(await api(`${endpoint()}/import`, body));
      state.selected[state.kind] = result.dataset_id;
      await refreshDatasets();
      message(`Versión guardada: ${result.dataset_id}. Revisá su cobertura antes de usarla.`);
    });
  });
  $("update-data").addEventListener("click", event => action(event.currentTarget, async () => {
    const result = unwrap(await api(`${endpoint()}/update`, { dataset_id: state.selected[state.kind], finish_date: $("update-finish").value }));
    state.selected[state.kind] = result.dataset_id;
    await refreshDatasets();
    message(`Actualización guardada en una nueva versión: ${result.dataset_id}.`);
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
      const funding = $("enable-funding").checked ? { mode: "historical", dataset_id: $("funding-dataset").value } : { mode: "disabled" };
      const open_interest = $("enable-oi").checked ? { mode: "historical", dataset_id: $("oi-dataset").value } : { mode: "disabled" };
      if (funding.mode === "historical" && !funding.dataset_id || open_interest.mode === "historical" && !open_interest.dataset_id) throw new Error("Seleccioná una versión para cada fuente habilitada.");
      if (funding.mode === "historical") {
        const exclusions = [...document.querySelectorAll('[name="funding-excluded-symbol"]')];
        if (exclusions.some(input => !input.checked)) throw new Error("El funding sólo cubre BTC-USDT. Las demás rutas requieren exclusión explícita; sus costos de funding quedarían sin modelar.");
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
  setInterval(() => {
    if (!$("auto-refresh").checked || document.hidden) return;
    Promise.all([$("session-id").value && loadSession(), $("live-session-id").value && loadLive()]).catch(error => message(error.message, true));
  }, 30_000);
  const sessionId = new URLSearchParams(location.search).get("session_id");
  if (sessionId) $("session-id").value = sessionId;
  refreshDatasets().then(() => sessionId && loadSession(true)).catch(error => { $("library-status").textContent = "No se pudo cargar la biblioteca."; message(error.message, true); });
})();
