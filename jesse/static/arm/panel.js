(() => {
  const UNLOCK_KEY = "jesseArmUnlocked";

  function authToken() {
    for (let i = 0; i < localStorage.length; i += 1) {
      const key = localStorage.key(i);
      try {
        const value = JSON.parse(localStorage.getItem(key) || "");
        if (value && typeof value.authToken === "string" && value.authToken.length > 20) {
          return value.authToken;
        }
      } catch {
        /* skip */
      }
    }
    return "";
  }

  async function api(path, options) {
    const token = authToken();
    const headers = { "Content-Type": "application/json" };
    if (token) headers.Authorization = token;
    const response = await fetch(path, { ...options, headers });
    const data = await response.json().catch(() => ({}));
    return { ok: response.ok, status: response.status, data };
  }

  function modeClass(state) {
    if (!state || !state.armed) return "paused";
    if (!state.allow_trading) return "dry";
    return "live";
  }

  function modeLabel(state) {
    if (!state || !state.armed) return "pausado";
    if (!state.allow_trading) return "dry-run";
    return "en vivo";
  }

  function ensureTab(nav) {
    let tab = document.getElementById("jesse-arm-tab");
    if (!tab) {
      tab = document.createElement("button");
      tab.id = "jesse-arm-tab";
      tab.type = "button";
      tab.innerHTML = '<span class="jesse-arm-dot"></span><span>ARMAS</span>';
      tab.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();
        const panel = document.getElementById("jesse-arm-panel");
        if (panel && panel.classList.contains("is-open")) closePanel();
        else openPanel();
      });
    }
    if (tab.parentElement !== nav) nav.appendChild(tab);
    return tab;
  }

  function findNav() {
    const live = document.querySelector('a[href="/live/"], a[href="/live"]');
    if (live) {
      return live.closest("nav") || live.parentElement;
    }
    return document.querySelector("nav");
  }

  function panelHtml() {
    return `
      <div class="jesse-arm-shell">
        <p class="jesse-arm-kicker">panel de armado</p>
        <h1>Órdenes reales</h1>
        <p class="jesse-arm-lede">Estas llaves aplican al instante, sin recrear el contenedor. La sesión Live tiene que estar corriendo aparte.</p>
        <div class="jesse-arm-gate" id="jesse-arm-gate">
          <label for="jesse-arm-password">Contraseña del dashboard</label>
          <input id="jesse-arm-password" type="password" autocomplete="current-password">
          <p class="jesse-arm-error" id="jesse-arm-error"></p>
          <button class="jesse-arm-btn" type="button" id="jesse-arm-unlock">Entrar</button>
        </div>
        <div class="jesse-arm-board" id="jesse-arm-board" hidden>
          <div class="jesse-arm-status" id="jesse-arm-status"></div>
          <div class="jesse-arm-row">
            <div class="jesse-arm-copy">
              <h2>Operar</h2>
              <p>On: la estrategia dispara entradas y salidas. Off: la sesión sigue viva, sin nuevas señales.</p>
            </div>
            <button type="button" class="jesse-arm-switch" id="jesse-arm-armed" aria-label="Operar"><span></span></button>
          </div>
          <div class="jesse-arm-row">
            <div class="jesse-arm-copy">
              <h2>Órdenes reales</h2>
              <p>On: manda órdenes a Binance. Off: dry-run, no sale nada al exchange.</p>
            </div>
            <button type="button" class="jesse-arm-switch" id="jesse-arm-trading" aria-label="Órdenes reales"><span></span></button>
          </div>
          <p class="jesse-arm-foot">Misma contraseña que el login. Cerrar el panel vuelve a pedirla.</p>
        </div>
      </div>
    `;
  }

  function ensurePanel() {
    let panel = document.getElementById("jesse-arm-panel");
    if (panel) return panel;
    panel = document.createElement("div");
    panel.id = "jesse-arm-panel";
    panel.innerHTML = panelHtml();
    document.body.appendChild(panel);

    panel.querySelector("#jesse-arm-unlock").addEventListener("click", unlock);
    panel.querySelector("#jesse-arm-password").addEventListener("keydown", (event) => {
      if (event.key === "Enter") unlock();
    });
    panel.querySelector("#jesse-arm-armed").addEventListener("click", () => toggle("armed"));
    panel.querySelector("#jesse-arm-trading").addEventListener("click", () => toggle("allow_trading"));
    return panel;
  }

  function paint(state) {
    const tab = document.getElementById("jesse-arm-tab");
    const status = document.getElementById("jesse-arm-status");
    const armed = document.getElementById("jesse-arm-armed");
    const trading = document.getElementById("jesse-arm-trading");
    const klass = modeClass(state);
    if (tab) {
      tab.classList.remove("is-live", "is-dry", "is-paused");
      tab.classList.add(`is-${klass}`);
    }
    if (status) {
      status.className = `jesse-arm-status ${klass}`;
      status.textContent = modeLabel(state);
    }
    if (armed) armed.classList.toggle("is-on", Boolean(state && state.armed));
    if (trading) trading.classList.toggle("is-on", Boolean(state && state.allow_trading));
  }

  async function refreshBadge() {
    if (!authToken()) return;
    const result = await api("/arm/switches");
    if (result.ok) paint(result.data);
  }

  async function unlock() {
    const input = document.getElementById("jesse-arm-password");
    const error = document.getElementById("jesse-arm-error");
    error.textContent = "";
    const result = await api("/arm/unlock", {
      method: "POST",
      body: JSON.stringify({ password: input.value || "" }),
    });
    if (!result.ok) {
      error.textContent = result.status === 401 ? "Contraseña incorrecta." : "No se pudo entrar.";
      return;
    }
    sessionStorage.setItem(UNLOCK_KEY, "1");
    document.getElementById("jesse-arm-gate").hidden = true;
    document.getElementById("jesse-arm-board").hidden = false;
    paint(result.data);
  }

  async function toggle(field) {
    const armed = document.getElementById("jesse-arm-armed").classList.contains("is-on");
    const trading = document.getElementById("jesse-arm-trading").classList.contains("is-on");
    const body = field === "armed" ? { armed: !armed } : { allow_trading: !trading };
    const result = await api("/arm/switches", {
      method: "POST",
      body: JSON.stringify(body),
    });
    if (result.ok) paint(result.data);
  }

  function positionPanel() {
    const panel = document.getElementById("jesse-arm-panel");
    const nav = findNav();
    if (!panel || !nav) return;
    const width = Math.round(nav.getBoundingClientRect().width);
    panel.style.setProperty("--jesse-arm-nav", `${width}px`);
  }

  function openPanel() {
    const panel = ensurePanel();
    positionPanel();
    const unlocked = sessionStorage.getItem(UNLOCK_KEY) === "1";
    document.getElementById("jesse-arm-gate").hidden = unlocked;
    document.getElementById("jesse-arm-board").hidden = !unlocked;
    panel.classList.add("is-open");
    const tab = document.getElementById("jesse-arm-tab");
    if (tab) tab.classList.add("is-open");
    if (unlocked) refreshBadge();
    else {
      const input = document.getElementById("jesse-arm-password");
      input.value = "";
      input.focus();
    }
  }

  function closePanel() {
    const panel = document.getElementById("jesse-arm-panel");
    if (panel) panel.classList.remove("is-open");
    const tab = document.getElementById("jesse-arm-tab");
    if (tab) tab.classList.remove("is-open");
    sessionStorage.removeItem(UNLOCK_KEY);
  }

  function sync() {
    const nav = findNav();
    if (nav) ensureTab(nav);
    refreshBadge();
  }

  document.addEventListener("click", (event) => {
    const tab = document.getElementById("jesse-arm-tab");
    if (tab && tab.contains(event.target)) return;
    const panel = document.getElementById("jesse-arm-panel");
    if (panel && panel.classList.contains("is-open") && !panel.contains(event.target)) {
      const navLink = event.target.closest("a, button");
      if (navLink && navLink !== tab) closePanel();
    }
  });

  const observer = new MutationObserver(() => {
    const nav = findNav();
    if (nav && !document.getElementById("jesse-arm-tab")) ensureTab(nav);
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", sync);
  } else {
    sync();
  }
  setInterval(refreshBadge, 8000);
})();
